#!/usr/bin/env python2

import logging

import os
from subprocess import Popen
from sys import stderr


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


JAVA_BIN_PATH = 'java'
DOT_BIN_PATH = 'dot'
STANFORD_IE_FOLDER = 'stanford-openie'

tmp_folder = '/tmp/openie/'
if not os.path.exists(tmp_folder):
    os.makedirs(tmp_folder)


def process_entity_relations(entity_relations_str):
    entity_relations = list()
    for s in entity_relations_str:
        entity_relations.append(s[s.find("(") + 1:s.find(")")].split(';'))
    return entity_relations

def stanford_ie(input_filename):
    out = tmp_folder + 'out.txt'
    input_filename = input_filename.replace(',', ' ')

    new_filename = ''
    for filename in input_filename.split():
        if filename.startswith('/'):  # absolute path.
            new_filename += '{} '.format(filename)
        else:
            new_filename += '../{} '.format(filename)

    absolute_path_to_script = os.path.dirname(os.path.realpath(__file__)) + '/'
    command = 'cd {};'.format(absolute_path_to_script)
    command += 'cd {}; {} -mx4g -cp "stanford-openie.jar:stanford-openie-models.jar:lib/*" ' \
               'edu.stanford.nlp.naturalli.OpenIE {} -format ollie > {}'. \
        format(STANFORD_IE_FOLDER, JAVA_BIN_PATH, new_filename, out)

    java_process = Popen(command, stdout=stderr, stderr=open(os.devnull, 'w'), shell=True)
    java_process.wait()
    assert not java_process.returncode, 'ERROR: Call to stanford_ie exited with a non-zero code status.'

    with open(out, 'r') as output_file:
        results_str = output_file.readlines()
        logger.info(results_str)
    os.remove(out)

    results = process_entity_relations(results_str)

    return results

def relations(filename):
    entities_relations = stanford_ie(filename)
    return entities_relations

# print relations('samples.txt')
# java -mx4g -cp "stanford-openie.jar:stanford-openie-models.jar:lib/*" edu.stanford.nlp.naturalli.OpenIE samples.txt -format ollie > out.txt
