from __future__ import print_function
import datetime
import math
import boto.ec2

import hotcidr.state
from hotcidr.modifydatabase import printSinceSpecifiedTime
from hotcidr.util import *

def get_icmp_control_msg(code):
    #A table of icmp control codes and their description
    controlmsg_dict = {
        '-1': 'All',
        '0': 'Echo Reply',
        '3':'Destination Unreachable',
        '4':'Source Quench',
        '5':'Redirect Message',
        '8':'Echo Request',
        '9':'Router Advertisement',
        '10':'Router Solicitation',
        '11':'Time Exceeded',
        '12':'Parameter Problem: Bad IP header',
        '13':'Timestamp',
        '14':'Timestamp Reply',
        '15':'Information Request',
        '16':'Information Reply',
        '17':'Address Mask Request',
        '18':'Address Mask Reply',
        '30':'Traceroute'
    }

    if isinstance(code,int):
        if code in controlmsg_dict:
            return controlmsg_dict[code]
        else:
            return 'reserved'
    else:
        return 'n/a'

#Format a rule so that it is ready to be printed in print_rule
def format_rule(rule, repo, yamlfile, createdby, createdon, approvedby, approvedon, action):
    #Get the rule parameters, or determine if corrupted (any fields are missing)
    corrupted = False
    corrupted_str = 'n/a'

    rule['date_timestamp'] = createdon
    rule['approved_date_timestamp'] = approvedon

    if 'direction' in rule:
        if rule['direction'] == 'inbound':
            from_or_to = 'from'
        else:
            from_or_to = 'to'
    else:
        corrupted = True
        from_or_to = 'from/to'
        rule['direction'] = corrupted_str

    if 'location' in rule:
        if is_cidr(rule['location']):
            type_str = 'CIDR'
        else:
            type_str = 'group'
    else:
        corrupted = True
        type_str = 'group'
        rule['location'] = corrupted_str

    if 'ports' in rule:
        if hasattr(rule['ports'], 'toport') and rule['ports'].toport:
            rule['toport'] = str(rule['ports'].toport)

        if hasattr(rule['ports'], 'fromport') and rule['ports'].fromport:
            rule['fromport'] = str(rule['ports'].fromport)

    if not 'protocol' in rule:
        corrupted = True

    if not 'protocol' in rule:
        rule['protocol'] = corrupted_str

    if not 'description' in rule:
        rule['description'] = corrupted_str
    
    #Format justification, possibly getting a commit message
    if 'hexsha' in rule:
        commit_message = get_git_commit(rule['hexsha'], repo, yamlfile)
    else:
        commit_message = None

    if not 'justification' in rule and not commit_message:
        rule['justification'] = corrupted_str
    elif not 'justification' in rule and commit_message:
        rule['justification'] = commit_message
    elif 'justification' in rule and commit_message:
        rule['justification'] += ' (commit message: \'' + commit_message + '\')'
   
    #Format ports_str
    if rule['protocol'] == 'icmp':
        if 'fromport' in rule:
            ports_str = get_icmp_control_msg(rule['fromport'])
            rule['toport'] = 'n/a'
            rule['fromport'] = ports_str
        else:
            ports_str = corrupted_str
    else:
        if not 'fromport' in rule or not rule['fromport']:
            rule['fromport'] = corrupted_str
        if not 'toport' in rule or not rule['toport']:
            rule['toport'] = corrupted_str

        if rule['fromport'] == rule['toport']:
            ports_str = (rule['fromport'])
        else:
            ports_str = str(rule['fromport']) + '-' + str(rule['toport'])
 
    #Format created/approved on
    try:
        createdon_str = datetime.datetime.fromtimestamp( float(createdon) ).strftime('%Y-%m-%d %H:%M:%S') + ' UTC'
    except ValueError:
        createdon_str = 'n/a'

    try:
        approvedon_str = datetime.datetime.fromtimestamp( float(approvedon) ).strftime('%Y-%m-%d %H:%M:%S') + ' UTC'
    except ValueError:
        approvedon_str = 'n/a'

    #Format action_str
    action_str = action
    if corrupted:
        action_str = 'corruptly ' + action_str

    rule['action'] = action_str
    rule['approved_author'] = approvedby
    rule['approved_date'] = approvedon_str
    rule['author'] = createdby
    rule['date'] = createdon_str
    rule['ports'] = ports_str
    rule['from_or_to'] = from_or_to
    rule['type'] = type_str

    rule['protocol'] = str(rule['protocol'])
    rule['fromport'] = str(rule['fromport'])
    rule['toport'] = str(rule['toport'])

    return rule

#Print a rule in the correct format
def print_rule(rule, from_time, to_time, output_webserver): 
    #Output rule
    output = ''

    if int(rule['date_timestamp']) >= from_time and int(rule['date_timestamp']) <= to_time:
        if output_webserver:
            output += '\"{action}\",\"{protocol}\",\"{ports}\",\"{direction}\",\"{type_str}\",\"{location}\",\"{createdby}\",\"{createdon}\",\"{approvedby}\",\"{approvedon}\",\"{justification}\",\"{description}\"\n'.format(
                action = rule['action'],
                protocol = rule['protocol'],
                ports = rule['ports'],
                direction = rule['direction'],
                fromto = rule['from_or_to'],
                type_str = rule['type'],
                location = rule['location'],
                createdby = rule['author'],
                createdon = rule['date'],
                approvedby = rule['approved_author'],
                approvedon = rule['approved_date'],
                justification = rule['justification'],
                description = rule['description'] )

        else:
            output += '\t {protocol} {fromport} to {toport} {direction} {fromto} {type_str} {location} {action} by {createdby} on {createdon} approved by {approvedby} on {approvedon} because {justification} {description} \n'.format(
                protocol = rule['protocol'].ljust(5),
                fromport = rule['fromport'].ljust(9),
                toport = rule['toport'].ljust(7),
                direction = rule['direction'].ljust(10),
                fromto = rule['from_or_to'].ljust(7),
                type_str = rule['type'].ljust(6),
                location = rule['location'].ljust(20),
                action = rule['action'].ljust(26),
                createdby = rule['author'].ljust(16),
                createdon = rule['date'].ljust(26),
                approvedby = rule['approved_author'].ljust(16),
                approvedon = rule['approved_date'].ljust(26),
                justification = rule['justification'].ljust(20),
                description = rule['description'] )

    return output

def main(repo, from_time, to_time, region_code, vpc_id, aws_id, aws_key, output, output_webserver, selectedgroup, sort_chronologically, silence):
    #Check repo argument
    repo, is_clone_url = get_valid_repo( repo )
    if not repo:
        print('Error: invalid repo specified', file=sys.stderr)
        return 1

    #Format and check from and to time
    if not from_time:
        from_time = 0
    else:
        if isint(from_time):
            from_time = int(from_time)
        else:
            print('Warning: from-time argument is not an integer. It should be a timestamp in UTC. It will be set to 0.', file=sys.stderr)
            from_time = 0

    if not to_time:
        to_time = int(math.floor(time.time()))
    else:
        if isint(to_time):
            to_time = int(to_time)
        else:
            print('Warning: from-time argument is not an integer. It should be a timestamp in UTC. It will be set to the current time.', file=sys.stderr)
            to_time = int(math.floor(time.time()))

    #Unauthorized rule database connection. This is not included in the current version of hotcidr for the command-line.
    '''
    try:
        #This function should return a dictionary {'added':[<unauthorized added rules>], 'deleted':[<unauthorized deleted rules>]} within the time range
        testDict = get_unauth_rules(to_time, from_time) 
    except:
        print('Warning: MySQL database with unauthorized rules not found. Continuing without printing', file=sys.stderr)

    if 'addedDict' in testDict:
        unauthAddedGroupsRules = testDict['addedDict']
    if 'deletedDict' in testDict:
        unauthDeletedGroupsRules = testDict['deletedDict']
    '''

    #Create output_str as formatted audit output
    output_str = ''

    if output_webserver:
        output_str += '---\n'

    #Handle boxes.yaml
    boxgroups = {}
    try:
        boxesyaml = file( os.path.join(repo, 'boxes.yaml') , 'r')
        boxes = hotcidr.state.load( boxesyaml )
    except IOError:
        print('Warning: ' + os.path.join(repo, 'boxes.yaml') + ' is missing. Audit output will have no instances listed.', file=sys.stderr)
        boxes = []
    except yaml.scanner.ScannerError as e:
        print('Warning: boxes.yaml is not properly formatted:\n' + str(e), file=sys.stderr)
        print('Audit output will have no instances listed', file=sys.stderr)
        boxes = []

    if hasattr(boxes, 'keys'):
        for box in boxes.keys():
            for boxgroup in boxes[box]['groups']:
                if not boxgroup in boxgroups:
                    boxgroups[boxgroup] = []
            
                #Print machines with a domain
                if 'domain' in boxes[box] and boxes[box]['domain']:
                    boxgroups[boxgroup].append( boxes[box]['domain'] )

                #Print machines with an ip
                elif 'ip' in boxes[box] and boxes[box]['ip']:
                    boxgroups[boxgroup].append( boxes[box]['ip'] )

                #Print local machines with no ip-address
                elif 'tags' in boxes[box] and 'Name' in boxes[box]['tags'] and boxes[box]['tags']['Name']:
                    boxgroups[boxgroup].append( boxes[box]['tags']['Name'] )

    #Handle getting the security group ids to print out in auditing
    #Get connection from credentials, or else the boto configuration
    connection = None
    if region_code:
        try:
            if not aws_id or not aws_key:
                connection = boto.ec2.connect_to_region(region_code)
            else:
                connection = boto.ec2.connect_to_region(region_code, aws_access_key_id=aws_id, aws_secret_access_key=aws_key)
        except boto.exception.NoAuthHandlerFound:
            print('Warning: boto credentials and/or region-code are invalid or missing. The audit will not include security group ids.')
            return 1
    else:
        print('Warning: region-code argument required for printing security group ids in audit. The audit will not include security group ids.')

    #If vpc_id specified, filter on it. Otherwise, return all security groups
    groups = None
    if connection:
        if vpc_id:
            groups = connection.get_all_security_groups(filters={'vpc-id':vpc_id})
        else:
            groups = connection.get_all_security_groups()

    #Create a lookup of name given id for each group, to speed up printing later
    nameid_lookup = dict()
    if groups:
        for group in groups:
            #For a single selected group, don't do anything with other non-selected groups
            if selectedgroup and not group.name == selectedgroup:
                continue

            if group.name in nameid_lookup:
                print('Warning: vpc-id has not been specified, and there are two vpcs with the group ' + group.name + '. The audit will not include security group ids.')
                break

            nameid_lookup[group.name.encode('ascii')] = group.id.encode('ascii')

    #Get groups and print auditing info per group OR print audit info for specified file
    if selectedgroup:
        if not selectedgroup.endswith('.yaml'):
            selectedgroup += '.yaml'

        groups = { selectedgroup : os.path.join('groups', selectedgroup) }
    else:
        groups = get_groups_dict(repo)

    groups_num = len(groups)
    i = 0

    for group in groups:
        #Immediately terminate if there are no groups, or else a division by 0 will occur later
        if groups_num == 0:
            print('ERROR: No groups loaded.',file=sys.stderr)
            return 1

        #Print progress
        i += 1
        if not silence:
            print('%s%% Processing %s' % (str(int(100*i/groups_num)), group), file=sys.stderr)
        sys.stderr.flush()

        #Print line seperators 
        if i > 1:
            if output_webserver:
                output_str += '---\n'
            else:
                output_str += '\n'

        #Load yaml file
        try:
            yamlfile = open( os.path.join(repo, groups[group]) , 'r')
            rulesyaml = yamlfile.read()
            yamlfile.close()
            rules = hotcidr.state.load( rulesyaml )
        except IOError:
            print('Warning: ' + os.path.join(repo, groups[group]) + ' is missing.', file=sys.stderr)
            print('Skipping group; it will not be included in the audit output', file=sys.stderr)
            continue
        except yaml.scanner.ScannerError as e:
            print('Warning: ' + os.path.join(repo, groups[group]) + ' is not properly formatted:\n' + str(e), file=sys.stderr)
            print('Skipping group; it will not be included in the audit output', file=sys.stderr)
            continue

        #Print group name, possibly with security group id
        group_name = groups[group].split('/')[1].split('.')[0]
        if group_name in nameid_lookup:
            output_str += nameid_lookup[group_name] + ',' + group_name  + '\n'
        else:
            output_str += group_name  + '\n'

        #Print associated machines
        output_str += 'Machines:\n'
        if group in boxgroups:
            if output_webserver:
                for boxg in boxgroups[group]:
                    output_str += boxg 

                    if not boxg == boxgroups[group][-1]:
                        output_str += ','
            else:
                for boxg in boxgroups[group]:
                    output_str += '\t' + boxg + '\n'
        
        if output_webserver:
            output_str += '\n'

        #Setup necessary data and headers
        added_deleted_rules = get_added_deleted_rules( repo, groups[group] )
        formatted_rules = []

        if output_webserver:
            output_str += 'Action,Protocol,Ports,Direction,Type,Location,Changed by,Changed on,Approved by,Approved on,Justification,Description\n'
        else:
            if not sort_chronologically:
                output_str += 'Rules added:\n'
            else:
                output_str += 'Rules:\n'

        #Get per-group rules that have been created/changed (that exist in the current yaml file)
        for rule in added_deleted_rules['added']:
            #Rule is essentially empty
            if len(rule.keys()) == 3 and 'hexsha' in rule and 'date' in rule and 'author' in rule:
                continue

            approved_authdate = get_commit_approved_authdate(rule['hexsha'], repo, groups[group])
            formatted_rule = format_rule(rule, repo, groups[group], rule['author'], rule['date'], approved_authdate['author'], approved_authdate['date'], 'added')

            if not sort_chronologically:
                output_str += print_rule(formatted_rule, from_time, to_time, output_webserver)
            else:
                formatted_rules.append(formatted_rule)

            approved_authdate = {}

        #Get per-group rules that were added (existed in a past version of the yaml file)
        if not output_webserver and not sort_chronologically:
            output_str += 'Rules previously added:\n'

        for rule in added_deleted_rules['added_previously']:
            approved_authdate = get_commit_approved_authdate(rule['hexsha'], repo, groups[group])
            formatted_rule = format_rule(rule, repo, groups[group], rule['author'], rule['date'], approved_authdate['author'], approved_authdate['date'], 'added previously')

            if not sort_chronologically:
                output_str += print_rule(formatted_rule, from_time, to_time, output_webserver)
            else:
                formatted_rules.append(formatted_rule)

            approved_authdate = {} #For debugging, to make mistakes obvious

        #Get per-group rules that are deleted (existed in a past version of the yaml file)
        if not output_webserver and not sort_chronologically:
            output_str += 'Rules deleted:\n'

        for rule in added_deleted_rules['deleted']:
            approved_authdate = get_commit_approved_authdate(rule['hexsha'], repo, groups[group])
            formatted_rule = format_rule(rule, repo, groups[group], rule['author'], rule['date'], approved_authdate['author'], approved_authdate['date'], 'deleted')

            if not sort_chronologically:
                output_str += print_rule(formatted_rule, from_time, to_time, output_webserver)
            else:
                formatted_rules.append(formatted_rule)

            approved_authdate = {} #For debugging, to make mistakes obvious

        '''
        #Get unauthorized rules
        if group in unauthAddedGroupsRules:
            if not output_webserver and not sort_chronologically:
                output_str += 'Unauthorized rules created:\n'

            for unauthAddedRule in unauthAddedGroupsRules[group]:
                formatted_rule = format_rule(unauthAddedRule, repo, groups[group], 'unknown', unauthAddedRule['secondsAgo'], 'no one', 'n/a', 'unauthorized add')

                if not sort_chronologically:
                    output_str += print_rule(formatted_rule, from_time, to_time, output_webserver)
                else:
                    formatted_rules.append(formatted_rule)

        #Get unauthorized deleted rules
        if group in unauthDeletedGroupsRules:
            if not output_webserver and not sort_chronologically:
                output_str += 'Unauthorized rules deleted:\n'

            for unauthDeletedRule in unauthDeletedGroupsRules[group]:
                formatted_rule = format_rule(unauthDeletedRule, repo, groups[group], 'unknown', unauthDeletedRule['secondsAgo'], 'no one', 'n/a', 'unauthorized delete')

                if not sort_chronologically:
                    output_str += print_rule(formatted_rule, from_time, to_time, output_webserver)
                else:
                    formatted_rules.append(formatted_rule)
        '''

        #Sort formatted_rules chronologically
        if sort_chronologically:
            sort_by_key = 'approved_date'

            formatted_dict = {}
            for formatted_rule in formatted_rules:
                if not formatted_rule[sort_by_key] in formatted_dict:
                    formatted_dict[formatted_rule[sort_by_key]] = []

                formatted_dict[formatted_rule[sort_by_key]].append(formatted_rule)

            for timestamp in sorted(formatted_dict, reverse=True):
                for formatted_rule in formatted_dict[timestamp]:
                    output_str += print_rule(formatted_rule, from_time, to_time, output_webserver)

    #Write file to output if specified, or else print string
    if output:
        f = open(output, 'w')
        f.write(output_str)
        f.close()
    else:
        print(output_str)

    #Remove temporary git repo
    if is_clone_url:
        rmtree(repo)

    if not silence:
        #If i is replaced with groups_num, the number will be inaccurate when a single selectedgroup is audited
        print('Audit successfully completed for %d groups.' % i, file=sys.stderr)
    sys.stderr.flush()

    return output_str

