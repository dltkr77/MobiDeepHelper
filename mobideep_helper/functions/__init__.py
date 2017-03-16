# -*- coding: utf-8 -*-

def split_text(*args, **kwargs):
    delimiter = kwargs.get('delimiter', ',')
    return args[0].split(delimiter)


def slice_list(*args, **kwargs):
    start = kwargs.get('start', 0)
    end = kwargs.get('end', -1)
    return args[0][start:end]
