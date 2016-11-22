import json
import yaml

from token_injector import TokenInjector


class BossConf:
    """Config parser with token interpreter"""

    config = None
    token_injector = None

    def __init__(self, config_path, config_file="config.yaml"):

        # load config object
        conf_obj = BossConf.__load_config(config_path, config_file)
        if conf_obj:
            self.config = conf_obj
        else:
            raise Exception(' '.join(['Config', '/'.join([config_path, config_file]), 'could not be loaded']))

    @staticmethod
    def __load_config(config_path, config_file):

        conf_obj = None

        # detect extension
        ext = BossConf.__get_conf_extension(config_file)

        path = '/'.join(['/'.join(config_path), config_file])

        # open file
        with open(path, 'r') as f:
            content = f.read()
            if ext:
                if ext == 'json':
                    conf_obj = json.loads(content)
                elif ext == 'yaml':
                    conf_obj = yaml.load(content)
            else:
                try:
                    conf_obj = yaml.load(content)
                except Exception:
                    try:
                        conf_obj = json.loads(content)
                    except Exception:
                        raise Exception(' '.join(['File', path, 'is neither json nor yaml']))

        return conf_obj

    @staticmethod
    def __get_conf_extension(file_name):
        ext = None
        if '.' in file_name:
            ext = file_name.split('.')[-1]
            if ext:
                if ext == 'json':
                    ext = 'json'
                elif ext == 'yaml':
                    ext = 'yaml'

        return ext

    """ Public """

    def get(self, nmsp=None, token_mapping=None, only_key=False, return_if_none=None):
        """ abstract getter """
        if nmsp:
            if type(nmsp) is list:
                data = self.config
                if data:
                    i = 0
                    rec_level = len(nmsp)
                    for p_nmsp in nmsp:
                        i += 1
                        if p_nmsp in data:
                            if only_key and i == rec_level and type(data[p_nmsp]) is dict:
                                data = data[p_nmsp].keys()
                            else:
                                data = data[p_nmsp]
                        else:
                            data = None
                            break
            else:
                data = self.config[nmsp]
        else:
            data = self.config
        if token_mapping:
            self.token_injector = TokenInjector(token_mapping, '`%s`')
            data = self.get_untokenized_data(data, token_mapping)

        # change default if none
        if not data and return_if_none:
            data = return_if_none

        return data

    def get_untokenized_data(self, data, mapping):
        """ untokenize tree data """
        untokenized_data = {}
        for key, value in data.iteritems():
            if type(value) == list:
                val_container = []
                for val in value:
                    val_container.append(self.token_injector(val))
                untokenized_data[key] = val_container
            elif type(value) == dict:
                untokenized_data[key] = self.get_untokenized_data(value, mapping)
            else:
                untokenized_data[key] = self.token_injector(value)

        return untokenized_data
