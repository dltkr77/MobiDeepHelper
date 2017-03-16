# -*- coding: utf-8 -*-

from .. import getclass


class Transformer:
    def __init__(self, config):
        self.config = config

    def transform(self, data):
        return data


class ChainTransformer(Transformer):
    def __init__(self, config):
        Transformer.__init__(self, config)
        self.functions_module_path = 'mobideep_helper.functions'
        self.func_list = self.config['functions']

        self.functions = []
        self.argument_dict = {}

        for func in self.func_list:
            for key, kwargs in func.items():
                path = '%s.%s' % (self.functions_module_path, key)
                self.functions.append(getclass(path))
                self.argument_dict[key] = kwargs

    def transform(self, data):
        for func in self.functions:
            data = func(data, **self.get_kwargs(func.__name__))
        return data

    def get_functions(self):
        return self.functions

    def get_kwargs(self, func):
        return self.argument_dict.get(func)