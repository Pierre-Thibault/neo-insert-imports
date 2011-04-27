#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Pierre Thibault (pierre.thibault1 -at- gmail.com)
@license: MIT
@since: 2011-04-26

NAME
       insert_imports - add the necessary dead code for web2py controllers and
       models to avoid warnings and errors from the Eclipse Pydev static code
       analyzer.

SYNOPSIS
       insert_imports [OPTION]... FILE...

DESCRIPTION

This script is made for people using the web2py framework with Eclipse and 
Pydev. It inserts the dead code necessary to avoid the warnings and errors
reported by Pydev due to the missing web2py imports. Web2py does automatically
insert a set of common imports for models and controllers so the user does not
have to explicitly import them in the code. This cause a problem with Pydev
since from a Pythonic point of view, these imports are missing and the static
code analyzer reports the issue as warnings or errors. This script was made to
automate the process of adding the necessary dead code to suppress these
warnings and errors.

The script is made to be used as a tool to be added in your PATH. Just call the
tool with the files to process as arguments. It will add the code just before
the Python code or at the end of the file unless the mark "STATIC_IMPORT_MARK"
(with or without quotes) is present in the file.

OPTION
    -h,  --help          Display this help message.

TIPS:

Use the power of the shell. For example if you are located in the applications
directory of web2py, you can use:

    insert_imports */controllers/*.py
    insert_imports */models/*.py
    
to process all the controllers and all the models for all applications.
'''

from __future__ import with_statement
import getopt
import os
import os.path
import re
import sys

__docformat__ = "epytext en"

# Mark the files that are already having the code to insert:
STATIC_IMPORT_MARK = "STATIC_IMPORT_MARK"

# Code to insert:
CODE_TO_INSERT = \
"""# Static analyzer import helpers: (STATIC_IMPORT_MARK)
if 0: 
    import gluon
    global cache; cache = gluon.cache.Cache()
    global LOAD; LOAD  = gluon.compileapp.LoadFactory()
    import gluon.compileapp.local_import_aux as local_import #@UnusedImport
    from gluon.contrib.gql import GQLDB #@UnusedImport
    from gluon.dal import Field #@UnusedImport
    global request; request = gluon.globals.Request()
    global response; response = gluon.globals.Response()
    global session; session = gluon.globals.Session()
    from gluon.html import A #@UnusedImport
    from gluon.html import B #@UnusedImport
    from gluon.html import BEAUTIFY #@UnusedImport
    from gluon.html import BODY #@UnusedImport
    from gluon.html import BR #@UnusedImport
    from gluon.html import CENTER #@UnusedImport
    from gluon.html import CODE #@UnusedImport
    from gluon.html import DIV #@UnusedImport
    from gluon.html import EM #@UnusedImport
    from gluon.html import EMBED #@UnusedImport
    from gluon.html import embed64 #@UnusedImport
    from gluon.html import FIELDSET #@UnusedImport
    from gluon.html import FORM #@UnusedImport
    from gluon.html import H1 #@UnusedImport
    from gluon.html import H2 #@UnusedImport
    from gluon.html import H3 #@UnusedImport
    from gluon.html import H4 #@UnusedImport
    from gluon.html import H5 #@UnusedImport
    from gluon.html import H6 #@UnusedImport
    from gluon.html import HEAD #@UnusedImport
    from gluon.html import HR #@UnusedImport
    from gluon.html import HTML #@UnusedImport
    from gluon.html import I #@UnusedImport
    from gluon.html import IFRAME #@UnusedImport
    from gluon.html import IMG #@UnusedImport
    from gluon.html import INPUT #@UnusedImport
    from gluon.html import LABEL #@UnusedImport
    from gluon.html import LEGEND #@UnusedImport
    from gluon.html import LI #@UnusedImport
    from gluon.html import LINK #@UnusedImport
    from gluon.html import MARKMIN #@UnusedImport
    from gluon.html import MENU #@UnusedImport
    from gluon.html import META #@UnusedImport
    from gluon.html import OBJECT #@UnusedImport
    from gluon.html import OL #@UnusedImport
    from gluon.html import ON #@UnusedImport
    from gluon.html import OPTGROUP #@UnusedImport
    from gluon.html import OPTION #@UnusedImport
    from gluon.html import P #@UnusedImport
    from gluon.html import PRE #@UnusedImport
    from gluon.html import STYLE #@UnusedImport
    from gluon.html import SCRIPT #@UnusedImport
    from gluon.html import SELECT #@UnusedImport
    from gluon.html import SPAN #@UnusedImport
    from gluon.html import TABLE #@UnusedImport
    from gluon.html import TAG #@UnusedImport
    from gluon.html import TBODY #@UnusedImport
    from gluon.html import TD #@UnusedImport
    from gluon.html import TEXTAREA #@UnusedImport
    from gluon.html import TFOOT #@UnusedImport
    from gluon.html import TH  #@UnusedImport
    from gluon.html import THEAD #@UnusedImport
    from gluon.html import TITLE #@UnusedImport
    from gluon.html import TR #@UnusedImport
    from gluon.html import TT #@UnusedImport
    from gluon.html import UL #@UnusedImport
    from gluon.html import URL #@UnusedImport
    from gluon.html import XHTML #@UnusedImport
    from gluon.html import XML #@UnusedImport
    from gluon.html import xmlescape #@UnusedImport
    from gluon.http import HTTP #@UnusedImport
    from gluon.http import redirect #@UnusedImport
    import gluon.languages.translator as T #@UnusedImport
    from gluon.sql import DAL
    global db; db = DAL()
    from gluon.sql import SQLDB #@UnusedImport
    from gluon.sql import SQLField #@UnusedImport
    from gluon.sqlhtml import SQLFORM #@UnusedImport
    from gluon.sqlhtml import SQLTABLE #@UnusedImport
    from gluon.tools import  Auth
    global auth; auth = Auth()
    from gluon.tools import Crud
    global crud; crud = Crud()
    from gluon.tools import fetch #@UnusedImport
    from gluon.tools import geocode #@UnusedImport
    from gluon.tools import Mail
    global mail; mail = Mail()
    from gluon.tools import PluginManager
    global plugins; plugins = PluginManager()
    from gluon.tools import prettydate #@UnusedImport
    from gluon.tools import Recaptcha #@UnusedImport
    from gluon.tools import Service
    global service; service = Service()
    from gluon.validators import CLEANUP  #@UnusedImport
    from gluon.validators import CRYPT #@UnusedImport
    from gluon.validators import IS_ALPHANUMERIC #@UnusedImport
    from gluon.validators import IS_DATE #@UnusedImport
    from gluon.validators import IS_DATE_IN_RANGE #@UnusedImport
    from gluon.validators import IS_DATETIME #@UnusedImport
    from gluon.validators import IS_DATETIME_IN_RANGE #@UnusedImport
    from gluon.validators import IS_DECIMAL_IN_RANGE #@UnusedImport
    from gluon.validators import IS_EMAIL #@UnusedImport
    from gluon.validators import IS_EMPTY_OR #@UnusedImport
    from gluon.validators import IS_EQUAL_TO #@UnusedImport
    from gluon.validators import IS_EXPR #@UnusedImport
    from gluon.validators import IS_FLOAT_IN_RANGE #@UnusedImport
    from gluon.validators import IS_IMAGE #@UnusedImport
    from gluon.validators import IS_IN_DB #@UnusedImport
    from gluon.validators import IS_IN_SET #@UnusedImport
    from gluon.validators import IS_INT_IN_RANGE #@UnusedImport
    from gluon.validators import IS_IPV4 #@UnusedImport
    from gluon.validators import IS_LENGTH #@UnusedImport
    from gluon.validators import IS_LIST_OF #@UnusedImport
    from gluon.validators import IS_LOWER #@UnusedImport
    from gluon.validators import IS_MATCH #@UnusedImport
    from gluon.validators import IS_NOT_EMPTY #@UnusedImport
    from gluon.validators import IS_NOT_IN_DB #@UnusedImport
    from gluon.validators import IS_NULL_OR #@UnusedImport
    from gluon.validators import IS_SLUG #@UnusedImport
    from gluon.validators import IS_STRONG  #@UnusedImport
    from gluon.validators import IS_TIME #@UnusedImport
    from gluon.validators import IS_UPLOAD_FILENAME #@UnusedImport
    from gluon.validators import IS_UPPER #@UnusedImport
    from gluon.validators import IS_URL #@UnusedImport

"""

# Regular expressions:
RE_IS_COMMENT = re.compile(r"^\s*#.*$")
RE_IS_BLANK = re.compile(r"^\s*$")
RE_FROM_FUTURE = re.compile(r"^from\s+__future__\s+import.*$")

def main(argv):                         
    """Parse the arguments and start the main process."""
    
    try:                                
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.GetoptError:
        exit_with_parsing_error()
    for opt, arg in opts: #@UnusedVariable
        if opt in ("-h", "--help"):
            usage()                     
            sys.exit()
    if len(args) == 0:
        exit_with_parsing_error()
    else:
        insert_imports(*args)

def exit_with_parsing_error():              
    """Report invalid arguments and usage."""
    
    print("Invalid argument(s).")
    usage()
    sys.exit(2)

def usage():
    """Display the documentation"""
    
    print(__doc__)

def insert_imports(*args):
    """
    Process all the files in args.
    """

    for source_file_name in args:
        try:
            source_file_size = os.path.getsize(source_file_name)
            dest_file_name = source_file_name+"~"
            with open(source_file_name) as source_file:
                if _is_marked(source_file):
                    continue # The file is marked, we have nothing to do
                source_file.seek(0)
                insert_line = _find_insert_line(source_file)
                source_file.seek(0)
                with open(dest_file_name, 'w') as dest_file:
                    # Write to dest_file the code before the insertion:
                    source_line = "\n"
                    for i in range(insert_line-1): #@UnusedVariable
                        source_line = source_file.readline()
                        dest_file.write(source_line)
                    if not source_line.endswith("\n"):
                        # Add a line sep if the last line has none:
                        dest_file.write("\n")
                    if source_file_size == source_file.tell():
                        # Add line if at the end of file
                        dest_file.write("\n")
                    
                    # Make the insertion:
                    dest_file.write(CODE_TO_INSERT)
                    
                    # Write the rest of the source file:
                    for line in source_file:
                        dest_file.write(line)
            # Swap the files:
            temp_source_file_name = source_file_name+"~~"
            os.rename(source_file_name, temp_source_file_name)
            os.rename(dest_file_name, source_file_name)
            os.remove(temp_source_file_name)
        except Exception, e:
            print 'Unable to process source_file "%s": %s' % \
              (source_file_name, str(e))

def _is_marked(file):
    """
    Return True if the file contains the mark.
    """

    for line in file:
        if line.find(STATIC_IMPORT_MARK) != -1:
            return True
    return False

def _find_insert_line(file):
    """
    Return the line number where the insertion should occur.
    """

    count = 1
    for line in file:
        if not RE_IS_BLANK.match(line) and not RE_IS_COMMENT.match(line) \
          and not RE_FROM_FUTURE.match(line):
            return count
        count += 1
    return count 

if __name__ == "__main__":
    # Unable to test the next line (OK)
    main(sys.argv[1:])  # Start the process (without the application name)
