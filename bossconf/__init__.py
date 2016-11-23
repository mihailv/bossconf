""" cli/lib dispatcher """
from bossconf import BossConf

def __out(data):
    import json
    """ output """
    if data:
        print json.dumps(data, sort_keys=True, indent=2, separators=(',', ': '))
    else:
        print data

def main(): pass


def main_cli():
    import os
    import select
    import sys

    # args
    args = sys.argv
    stdin = select.select([sys.stdin,],[],[],0.0)[0]

    if stdin:

        # validation
        if len(args) < 2 or len(args) > 2:
            print 'BossConf needs 1 argument(when used via pipe) keys to parse: ["lev1,lev2"]'
            exit(1)

        get_string = args[1].strip()
        if not get_string:
            print 'Empty config key'
            exit(1)
        
        # prep lookup str
        if ',' in get_string:
            get_string = [ str_mem.strip() for str_mem in get_string.split(',') ]
        else:
            get_string = [get_string.strip()]
        
        # get cli list
        stdin_str_members = stdin[0].readlines()

        # detect data type of stdin
        if stdin_str_members[0][0] == '{' or stdin_str_members[0][0] == '[':
            data_type = 'json'
        else:
            data_type = 'yaml'

        if data_type == 'json':
            # get string from stdin
            stdin_str_members_clean = []
            for stdin_str_member in stdin_str_members:
                stdin_str_members_clean.append(stdin_str_member.replace('\n','').strip())
            stdin_str = ''.join(stdin_str_members_clean)
        else:
            stdin_str = ''.join(stdin_str_members)

        # Run program
        __out(BossConf(None, None, stdin_str).get(get_string))

    else:
        if len(args) < 3 or len(args) > 3:
            print 'BossConf needs 2 arguments: [conf_file_path, "lev1,lev2"]'
            exit(1)

        conf_path = args[1].strip()
        get_string = args[2].strip()

        if not conf_path:
            print 'Empty path to config'
            exit(1)

        if not get_string:
            print 'Empty config key'
            exit(1)

        # check conf file path is abs
        if not os.path.isabs(conf_path):
            orig_path = os.getcwd()
            abs_conf_path = os.path.normpath('/'.join([orig_path, conf_path]))
        else:
            abs_conf_path = conf_path

        # check if conf file exists
        if os.path.isfile(abs_conf_path):

            # prep lookup str
            if ',' in get_string:
                get_string = [ str_mem.strip() for str_mem in get_string.split(',') ]
            else:
                get_string = [get_string.strip()]

            # run BossConf
            conf_file_name = abs_conf_path.split('/')[-1]
            conf_dir_path = abs_conf_path.split('/')[:-1]
            if conf_file_name and conf_dir_path:
                __out(BossConf(None, None, stdin_str).get(get_string))
        else:
            print 'File does not exist at ' + abs_conf_path
            exit(1)
