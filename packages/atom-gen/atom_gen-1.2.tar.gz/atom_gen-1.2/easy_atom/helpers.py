#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fonctions d'aide pour le logging, la lecture de configuration

"""
__author__ = 'Frederic Laurent'
__version__ = "1.0"
__copyright__ = 'Copyright 2017, Frederic Laurent'
__license__ = "MIT"

import json
import logging
import os.path
import os
import sys
import math
import io

from collections import namedtuple
from itertools import (takewhile, repeat)
from json.decoder import JSONDecodeError


def lines_count(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024 * 1024) for _ in repeat(None)))
    return sum(buf.count(b'\n') for buf in bufgen)


def load_json(config_filename):
    """
    Lecture d'un fichier de configuration au format JSON
    Produit un dictionnaire python

    :param config_filename: nom du fichier
    :return: données lues dans 1 dictionnaire
    """
    data = {}
    logger = stdout_logger("atom_helpers", logging.WARNING)

    if not os.path.exists(config_filename):
        return data
    else:
        with io.open(config_filename, 'r', encoding='utf-8') as fin:
            try:
                udata=fin.read()
                data = json.loads(udata.encode('utf-8'))
            except TypeError as msg_e:
                logger.warning("load_json_config typeError :%s" % msg_e)
            except JSONDecodeError as msg_j:
                logger.warning("load_json_config JSONdecode :%s" % msg_j)
    return data


def json_to_object(filename):
    """
    Lecture d'un fichier json et produit l'object Python correspond

    :param filename: nom du fichier
    :return: données lues dans 1 object
    """
    logger = stdout_logger("atom_helpers", logging.WARNING)

    if not os.path.exists(filename):
        logger.warning("Filename {} does not exist".format(filename))
        return None
    else:
        with open(filename, 'r') as fin:
            data = fin.read()
            try:
                return json.loads(data,
                                  object_hook=lambda d: namedtuple('JDATA', d.keys())(*d.values()))
            except:
                return None


def object_to_dict(obj):
    if isinstance(obj, (str, int, bool, float)):
        return obj
    local_dict = {}
    for k, v in obj._asdict().items():
        if hasattr(v, "_asdict"):
            local_dict[k] = object_to_dict(v)
        elif isinstance(v, list):
            local_dict[k] = list(map(lambda x: object_to_dict(x), v))
        else:
            local_dict[k] = v
    return local_dict


def object_to_json(obj, filename):
    resdict = object_to_dict(obj)
    save_json(filename, resdict)


def save_json(filename, data):
    bdir = os.path.dirname(filename)
    if not os.path.exists(bdir):
        os.makedirs(bdir)
        
    with open(filename, 'w') as fout:
        fout.write(json.dumps(data, sort_keys=True, indent=4))


def make_error_logger(name, level, filename):
    """
        Création d'un Logger d'erreur

    :param name: nom du logger
    :param level: niveau de logging
    :param filename: nom du fichier d'erreur
    :return: logger
    """
    formatter = logging.Formatter("%(asctime)s %(levelname)s - %(message)s",
                                  "%d/%m %H:%M:%S")
    sth_err = logging.FileHandler(filename)
    sth_err.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(sth_err)
    logger.setLevel(level)
    return logger


def config_logger(streamhandler, name, level, fmt=None):
    """
    Configure un logger sur la sortie standard avec un niveau
    :param fmt: formatter
    :param streamhandler: handler
    :param name: nom du logger
    :param level: niveau
    :return: logger ou loggers
    """
    if not fmt:
        formatter = logging.Formatter(
            "%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(lineno)d - %(message)s")
    else:
        formatter = logging.Formatter(fmt)
    streamhandler.setFormatter(formatter)

    # if there are multiple logger to set
    if isinstance(name, list):
        loggers = []
        for logname in name:
            # print "Logger [%s] addHandler %s - level %s" % (logname, streamhandler, level)

            logger = logging.getLogger(logname)
            logger.addHandler(streamhandler)
            logger.setLevel(level)
            loggers.append(logger)
        return loggers
    else:
        # print "Logger [%s] addHandler %s" % (name, sth_sysout)
        logger = logging.getLogger(name)
        logger.addHandler(streamhandler)
        logger.setLevel(level)
        return logger


def stdout_logger(name, level):
    """
        Création d'un logger sur la sortie standard
    :param name: nom du logger
    :param level: niveau
    :return: logger
    """
    sth_sysout = logging.StreamHandler(sys.stdout)
    return config_logger(sth_sysout, name, level)


def file_logger(filename, name, level):
    """
        Création d'un logger dans 1 fichier
    :param filename: nom du fichier
    :param name: nom du logger
    :param level: niveau
    :return: logger
    """
    sth_file = logging.FileHandler(os.path.abspath(filename))
    return config_logger(sth_file, name, level)


def file_size(size_bytes):
   if size_bytes == 0:
       return "0 o"
   size_name = ("o", "Ko", "Mo", "Go", "To", "Po", "Eo", "Zo", "Yo")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])