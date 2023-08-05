#! /usr/bin/python3
import argparse
import os
import sys
from pathlib import Path
import sys
import select



import yaml
from jinja2 import Environment



def get_arguments():
    p = argparse.ArgumentParser(description='Quick jinja2 templater')

    p.add_argument(
        '-y',
        '--yaml',
        help='yaml variables',
        default="vars.yaml",
    )
    p.add_argument(
        'template',
        help='jinja2 template',
    )

    args = p.parse_args()
    return args

def start_with_args():
    args = get_arguments()

    with open(args.template, 'r') as template_file:
        data = template_file.read()
    vars = {}
    if select.select([sys.stdin,],[],[],0.0)[0]:
        print("Have data!")
    elif os.path.isfile(args.yaml) :
        with open(args.yaml) as vars_file:
            vars = yaml.load(vars_file, Loader=yaml.BaseLoader)

    out = Environment(loader=yaml.BaseLoader).from_string(data).render(**vars)

    sys.stdout.write(out)