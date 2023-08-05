from __future__ import print_function
import os, sys, time
import git
import hotcidr.state
from hotcidr import util
from util import isint
import yaml

def main(repo = None, dont_push = None, silence = None):
    repo, is_git_repo = util.get_valid_repo( repo )

    groups = util.get_groups_dict(repo)

    #Sanity check expirations
    try:
        expirationsyaml = file( os.path.join(repo, 'expirations.yaml') , 'r')
        expirations = hotcidr.state.load(expirationsyaml)
    except IOError:
        print('Error: ' + os.path.join(repo, 'expirations.yaml') + ' is missing, and is necessary for expiration checking.',file=sys.stderr)
        return 1
    except yaml.scanner.ScannerError as e:
        print('Error: expirations.yaml is not properly formatted:\n' + str(e), file=sys.stderr)
        print('expirations.yaml is necessary for expiration checking.', file=sys.stderr)
        return 1

    if expirations:
        if 'rules' in expirations:
            expirations = expirations['rules']
        else:
            print('Error: expirations.yaml is not properly formatted. Rules must be under a \'rules:\' tag.', file=sys.stderr)

    #Immediately terminate if there are no groups, or else a division by 0 will occur later
    groups_num = len(groups)
    if groups_num == 0:
        print('ERROR: No groups loaded.',file=sys.stderr)
        return 1

    if not silence:
        i = 0

    any_rules_removed = False
    for group in groups:
        #Print processing
        if not silence:
            print('Processing ' + groups[group], file=sys.stderr)
            sys.stderr.flush()

        try:
            rulesyaml = file( os.path.join(repo, groups[group]) , 'r')
            rules = hotcidr.state.load(rulesyaml)
        except IOError:
            print('Warning: ' + os.path.join(repo, groups[group]) + ' is missing. It will be skipped.',file=sys.stderr)
            continue
        except yaml.scanner.ScannerError as e:
            print('Warning: ' + os.path.join(repo, groups[group]) + ' is not properly formatted and will be skipped:\n' + str(e), file=sys.stderr)
            continue

        added_rules = util.get_added_deleted_rules( repo, groups[group] )['added']
        rules_removed = False

        for added_rule in added_rules:

            #Handle expirations.yaml: add expiration field to all matching rules
            if expirations:
                for expired_rule in expirations:
                    if 'expiration' in expired_rule and isint(expired_rule['expiration']):
                        #TODO: Rather than count the fields in expired_rule, check that they are each in util.expected_rule_fields
                        if len(expired_rule.keys()) >= 2:
                            rule_is_expired = True
                            for field in util.expected_rule_fields:
                                if not field in added_rule or not field in expired_rule:
                                    continue

                                if not added_rule[field] == expired_rule[field]:
                                    rule_is_expired = False
                                    break

                            #Give the rule an expiration, so it will be seen as if it was originally added in <group>.yaml
                            if rule_is_expired:
                                added_rule['expiration'] = int(expired_rule['expiration'])
                        else:
                            print('Warning: rule in expirations.yaml has no fields to match: ' + expired_rule)
                    else:
                        print('Warning: rule in expirations.yaml is missing a valid expiration field: ' + expired_rule)

            #Handle expirations in <group>.yaml
            if 'expiration' in added_rule and isint(added_rule['expiration']):
                if int(added_rule['expiration']) < int(time.time()) - int(added_rule['date']):
                    if not silence:
                        print('Removed rule: ' + str(added_rule))
                    added_rules.remove(added_rule)
                    rules_removed = True

        #Prepare added_rules for loading back into yaml file
        for added_rule in added_rules:
            del added_rule['hexsha']
            del added_rule['author']
            del added_rule['date']

        if rules_removed:
            any_rules_removed = True

            #Edit yaml with new rules
            rules['rules'] = added_rules
            f = open( os.path.join( repo, groups[group] ), 'w' )
            f.write( hotcidr.state.dump(rules, default_flow_style=False) )
            f.close()

        #Print progress
        if not silence:
            i += 1
            print('Progress: ' + str(int(100*i/groups_num)), file=sys.stderr)

    #Commit and push changes if there were any rule changes
    if any_rules_removed:
        #Commit and push file
        git.Git( repo ).add( groups[group] ) 
        git.Git( repo ).commit('-m','Automatically removed expired rule')

        if not dont_push:
            try:
                git.Git( repo ).push()
            except git.exc.GitCommandError:
                print('Error: ' + repo + ' cannot be pushed: no remote exists? Try specifying the --dont-push argument.')
                return 1

    #Remove temporary git repo
    if is_git_repo:
        rmtree( repo )

    return 0
