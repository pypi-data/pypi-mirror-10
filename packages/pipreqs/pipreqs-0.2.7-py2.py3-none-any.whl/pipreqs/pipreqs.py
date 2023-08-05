#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pipreqs - Generate pip requirements.txt file based on imports

Usage:
    pipreqs [options] <path>

Options:
    --use-local         Use ONLY local package information instead of querying PyPI
    --debug             Print debug information
    --savepath <file>   Save the list of requirements in the given file
"""
from __future__ import print_function
import os
import sys
from distutils.sysconfig import get_python_lib
import re
import logging

from docopt import docopt
import yarg
from yarg.exceptions import HTTPError


REGEXP = [
    re.compile(r'^import (.+)$'),
    re.compile(r'^from ((?!\.+).*?) import (?:.*)$')
]




def get_all_imports(path):
    imports = []
    candidates = []

    for root, dirs, files in os.walk(path):
        candidates.append(os.path.basename(root))
        files = [fn for fn in files if os.path.splitext(fn)[1] == ".py"]
        candidates += [os.path.splitext(fn)[0] for fn in files]
        for file_name in files:
            with open(os.path.join(root, file_name), "r") as f:
                lines = filter(
                    filter_line, map(lambda l: l.partition("#")[0].strip(), f))
                for line in lines:
                    if "(" in line:
                        break
                    for rex in REGEXP:
                        s = rex.findall(line)
                        for item in s:
                            res = map(get_name_without_alias, item.split(","))
                            imports = imports + [x for x in res if len(x) > 0]

    packages = set(imports) - set(set(candidates) & set(imports))
    logging.debug('Found packages: {0}'.format(packages))

    with open(join("stdlib"), "r") as f:
        data = [x.strip() for x in f.readlines()]
        return sorted(list(set(packages) - set(data)))


def filter_line(l):
    return len(l) > 0 and l[0] != "#"


def generate_requirements_file(path, imports):
    with open(path, "w") as out_file:
        logging.debug('Writing {num} requirements: {imports} to {file}'.format(
            num=len(imports),
            file=path,
            imports=", ".join([x['name'] for x in imports])
        ))
        fmt = '{name} == {version}'
        out_file.write('\n'.join(fmt.format(**item)
                                 for item in imports) + '\n')


def get_imports_info(imports):
    result = []
    for item in imports:
        try:
            data = yarg.get(item)
        except HTTPError:
            logging.debug(
                'Package %s does not exist or network problems', item)
            continue
        result.append({'name': item, 'version': data.latest_release_id})
    return result


def get_locally_installed_packages():
    packages = {}
    ignore = ["tests", "_tests", "egg", "EGG", "info"]
    for path in sys.path:
	    for root, dirs, files in os.walk(path):
	        for item in files:
	            if "top_level" in item:
	                with open(os.path.join(root, item), "r") as f:
	                    package = root.split("/")[-1].split("-")
	                    try:
	                    	package_import = f.read().strip().split("\n")
	                    except:
	                    	continue
	                    for item in package_import:
	                        if item not in ignore and package[0] not in ignore:
	                            packages[item] = {
	                                'version': package[1].replace(".dist", ""),
	                                'name': package[0]
	                            }
    return packages


def get_import_local(imports):
    local = get_locally_installed_packages()
    result = []
    for item in imports:
        if item.lower() in local:
            result.append(local[item.lower()])
    return result


def get_pkg_names(pkgs):
    result = []
    with open(join("mapping"), "r") as f:
        data = [x.strip().split(":") for x in f.readlines()]
        for pkg in pkgs:
            toappend = pkg
            for item in data:
                if item[0] == pkg:
                    toappend = item[1]
                    break
            result.append(toappend)
    return result


def get_name_without_alias(name):
    if "import " in name:
        match = REGEXP[0].match(name.strip())
        if match:
            name = match.groups(0)[0]
    return name.partition(' as ')[0].partition('.')[0].strip()


def join(f):
    return os.path.join(os.path.dirname(__file__), f)


def init(args):
    candidates = get_all_imports(args['<path>'])
    candidates = get_pkg_names(get_all_imports(args['<path>']))
    logging.debug("Found imports: " + ", ".join(candidates))

    if args['--use-local']:
        logging.debug(
            "Getting package information ONLY from local installation.")
        imports = get_import_local(candidates)
    else:
        logging.debug("Getting packages information from Local/PyPI")
        local = get_import_local(candidates)
        # Get packages that were not found locally
        difference = [x for x in candidates if x.lower() not in [z['name'].lower()
                                                                 for z in local]]
        imports = local + get_imports_info(difference)

    path = args[
        "--savepath"] if args["--savepath"] else os.path.join(args['<path>'], "requirements.txt")
    generate_requirements_file(path, imports)
    print("Successfully saved requirements file in " + path)


def main():  # pragma: no cover
    args = docopt(__doc__, version='xstat 0.1')
    log_level = logging.DEBUG if args['--debug'] else logging.WARNING
    logging.basicConfig(level=log_level, format='%(levelname)s: %(message)s')

    try:
        init(args)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()  # pragma: no cover
