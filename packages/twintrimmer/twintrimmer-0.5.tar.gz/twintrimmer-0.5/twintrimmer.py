#! /usr/bin/env python3
'''
Twin trim

A duplicate file remover
'''
import sys
import os
import hashlib
import argparse
import functools
import re
import logging
import textwrap
from collections import defaultdict, namedtuple

LOGGER = logging.getLogger('')

Filename = namedtuple('Filename', ['name', 'base', 'ext', 'path'])


def create_filenames(filenames, root):
    '''
    Makes a generator that yields Filename objects

    Filename objects are a helper to allow multiple representations
    of the same file to be transferred cleanly.
    '''
    LOGGER.info("Creating Filename objects")
    for filename in filenames:
        yield Filename(filename, *os.path.splitext(filename),
                       path=os.path.join(root, filename))


def generate_checksum(filename, hash_name='md5'):
    '''
    A helper function that will generate the
    check sum of a file.

    According to the hashlib documentation:
    - hashlib.sha1 should be prefered over hashlib.new('sha1')
    - the list of available function will change depending on the openssl
      library
    - the same function might exist with multiple spellings i.e. SHA1 and sha1
    '''
    LOGGER.info("Generating checksum with %s for %s", hash_name, filename)

    if hash_name.lower() in ('md5', 'MD5'):
        hash_func = hashlib.md5()
    elif hash_name.lower() in ('sha1', 'SHA1'):
        hash_func = hashlib.sha1()
    elif hash_name.lower() in ('sha256', 'SHA256'):
        hash_func = hashlib.sha256()
    elif hash_name.lower() in ('sha512', 'SHA512'):
        hash_func = hashlib.sha512()
    elif hash_name.lower() in ('sha224', 'SHA224'):
        hash_func = hashlib.sha224()
    elif hash_name.lower() in ('sha384', 'SHA384'):
        hash_func = hashlib.sha384()
    else:
        hash_func = hashlib.new(hash_name)

    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(128 * hash_func.block_size), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def is_substring(string1, string2):
    '''
    Returns a match if one string is a substring of the other

    For example::

        is_substring('this', 'this1') -> True
        is_substring('that1', 'that') -> True

    But::

        is_substring('that', 'this')  -> False

    '''
    return string1 in string2 or string2 in string1


def pick_shorter_name(file1, file2):
    '''
    This convenience function will help to find the shorter (often better)
    filename.  If the file names are the same length it returns the file
    that is less, hoping for numerically.

    It picks "file.txt" over "file (1).txt", but beware it also picks
    "f.txt" over "file.txt".

    It also picks "file (1).txt" over "file (2).txt"
    '''
    LOGGER.debug("Finding the shortest of %s and %s", file1.name, file2.name)
    if len(file1.name) > len(file2.name):
        return file2
    elif len(file1.name) < len(file2.name) or file1.name < file2.name:
        return file1
    else:
        return file2


def ask_for_best(default, rest):
    '''
    This function allows the user to interactively select which file is
    selected to be preserved.
    '''
    files = [default] + list(rest)
    for num, file in enumerate(files):
        if file == default:
            print("{0}. {1} (default)".format(num, file.name))
        else:
            print("{0}. {1}".format(num, file.name))

    try:
        while True:
            result = input('Pick which file to keep (^C to skip): ')
            if result == '':
                best = default
                break
            elif result.isdigit() and int(result) in range(len(files)):
                best = files[int(result)]
                break
            elif result in [file.name for file in files]:
                best = [file for file in files if file.name == result][0]
                break
        rest = set(files) - {best}
        LOGGER.warning('User picked %s over %s', best, default)

    except KeyboardInterrupt:
        print('\nSkipped')
        LOGGER.warning('User skipped in interactive mode')
        best = default
        rest = {}

    return best, rest


def generate_checksum_dict(filenames, hash_name):
    '''
    This function will create a dictionary of checksums mapped to
    a list of filenames.
    '''
    LOGGER.info("Generating dictionary based on checksum")
    checksum_dict = defaultdict(set)

    for filename in filenames:
        try:
            checksum_dict[generate_checksum(filename.path,
                                            hash_name)].add(filename)
        except OSError as err:
            LOGGER.error('Checksum generation error: %s', err)

    return checksum_dict


def generate_filename_dict(filenames, expr=r'(^.+?)(?: \(\d\))*(\..+)$'):
    '''
    This function will create a dictionary of filename parts mapped to a list
    of the real filenames.
    '''
    LOGGER.info("Generating dictionary based on regular expression")
    filename_dict = defaultdict(set)

    regex = re.compile(expr)

    for filename in filenames:
        match = regex.match(filename.name)
        if match:
            LOGGER.debug('Regex groups for %s: %s', filename.name,
                         str(match.groups()))
            filename_dict[match.groups()].add(filename)

    return filename_dict


def remove_by_checksum(list_of_names, no_action, interactive, hash_name):
    '''
    This function first groups the files by checksum, and then removes all
    but one copy of the file.
    '''
    files = generate_checksum_dict(list_of_names, hash_name)
    for file in files:
        if len(files[file]) > 1:
            LOGGER.info("Investigating duplicate checksum %s", file)
            LOGGER.debug("Keys for %s are %s", file,
                         ', '.join([item.name for item in files[file]]))
            best = functools.reduce(pick_shorter_name, files[file])
            rest = files[file] - {best}

            if interactive:
                best, rest = ask_for_best(best, rest)

            for bad in rest:
                if no_action:
                    print('{0} would have been deleted'.format(bad.path))
                    LOGGER.info('%s would have been deleted', bad.path)
                else:
                    LOGGER.info('%s was deleted', bad.path)
                    try:
                        os.remove(bad.path)
                    except OSError as err:
                        LOGGER.error('File deletion error: %s', err)
            LOGGER.info('%s was kept as only copy', best.path)

        else:
            LOGGER.debug('Skipping non duplicate checksum %s for key %s', file,
                         ', '.join([item.name for item in files[file]]))


def walk_path(path, no_action, recursive, skip_regex, regex_pattern,
              interactive, hash_name):
    '''
    This function steps through the directory structure and identifies
    groups for more in depth investigation.
    '''
    for root, _, filenames in os.walk(path):
        if not recursive and root != path:
            LOGGER.debug("Skipping child directory %s", root)
            continue

        if not skip_regex:
            names = generate_filename_dict(create_filenames(filenames, root),
                                           regex_pattern)

            for name in names:
                if len(names[name]) > 1:
                    LOGGER.info("Investigating duplicate name %s", name)
                    LOGGER.debug("Keys for %s are %s", name,
                                 ', '.join([item.name
                                            for item in names[name]]))
                    remove_by_checksum(names[name], no_action, interactive,
                                       hash_name)
                else:
                    LOGGER.debug('Skipping non duplicate name %s for key %s',
                                 name, ', '.join([item.name
                                                  for item in names[name]]))
        else:
            remove_by_checksum(create_filenames(filenames, root), no_action,
                               interactive, hash_name)


def main():
    '''
        The main function handles all the parsing of arguments.
    '''
    epilog = r'''
    examples:

        find matches with default regex:

            $ ./twintrimmer.py -n ~/downloads

        find matches ignoring the extension:

            $  ls examples/
            Google.html  Google.html~
            $ ./twintrimmer.py -n -p '(^.+?)(?: \(\d\))*\..+' examples/
            examples/Google.html~ would have been deleted

        find matches with "__1" added to basename:

            $ ls examples/underscore/
            file__1.txt  file.txt
            $ ./twintrimmer.py -n -p '(.+?)(?:__\d)*\..*' examples/underscore/
            examples/underscore/file__1.txt to be deleted
    '''

    parser = argparse.ArgumentParser(
        description='tool for removing duplicate files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(epilog))
    parser.add_argument('path', help='path to check')
    parser.add_argument('-n', '--no-action',
                        default=False,
                        action='store_true',
                        help='show what files would have been deleted')
    parser.add_argument('-r', '--recursive',
                        default=False,
                        action='store_true',
                        help='search directories recursively')
    parser.add_argument('--verbosity',
                        type=int,
                        default=1,
                        help='set print debug level')
    parser.add_argument('--log-file', help='write to log file.')
    parser.add_argument('--log-level',
                        type=int,
                        default=3,
                        help='set log file debug level')
    parser.add_argument('-p', '--pattern',
                        type=str,
                        default=r'(^.+?)(?: \(\d\))*(\..+)$',
                        help='set filename matching regex')
    parser.add_argument(
        '-c', '--only-checksum',
        default=False,
        action='store_true',
        dest='skip_regex',
        help='toggle searching by checksum rather than name first')

    parser.add_argument('-i', '--interactive',
                        default=False,
                        action='store_true',
                        help='ask for file deletion interactively')

    parser.add_argument('--hash-function',
                        type=str,
                        default='md5',
                        choices=hashlib.algorithms_available,
                        help='set hash function to use for checksums')
    args = parser.parse_args()

    if not os.path.isdir(args.path):
        parser.error('path was not a directory: "{0}"'.format(args.path))

    if args.log_level != 3 and not args.log_file:
        parser.error('Log level set without log file')

    if args.pattern != r'(^.+?)(?: \(\d\))*(\..+)$' and args.skip_regex:
        parser.error('Pattern set while skipping regex checking')

    try:
        re.compile(args.pattern)
    except re.error:
        parser.error('Invalid regular expression: "{0}"'.format(args.pattern))

    stream = logging.StreamHandler()
    stream.setLevel((5 - args.verbosity) * 10)
    formatter_simple = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')
    stream.setFormatter(formatter_simple)
    LOGGER.addHandler(stream)
    LOGGER.setLevel(logging.DEBUG)

    if args.log_file:
        try:
            log_file = logging.FileHandler(args.log_file)
        except OSError as err:
            sys.exit("Couldn't open log file: {0}".format(err))
        log_file.setFormatter(formatter_simple)
        log_file.setLevel((5 - args.log_level) * 10)
        LOGGER.addHandler(log_file)

    LOGGER.debug("Args: %s", args)

    walk_path(args.path, args.no_action, args.recursive, args.skip_regex,
              args.pattern, args.interactive, args.hash_function)


if __name__ == '__main__':
    main()
