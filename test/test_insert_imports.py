# -*- coding: utf-8 -*-
'''
@author: Pierre Thibault (pierre.thibault1 -at- gmail.com)
@license: MIT
@since: 2011-04-26

'''

from __future__ import with_statement

__docformat__ = "epytext en"


import filecmp
import os
import shutil
import StringIO
import sys
import unittest

import insert_imports

class Test(unittest.TestCase):
    """
    Here we copy a source as a temp dir, we process all the files of temp dir
    and we verify we have the result expected by comparing with a result dir.
    """

    _temp_dir_created = False
    _SOURCE_DIR = "source_dir"
    _TMP_DIR = "source_dir~"
    _RESULT_DIR = "result_dir"

    def setUp(self):
        if not self._temp_dir_created:
            self.__delete_tmp_dir()
            shutil.copytree(self._SOURCE_DIR, self._TMP_DIR)
            self._temp_dir_created = True

    def tearDown(self):
        self.__delete_tmp_dir()


    def test_main(self):
        for (dirpath, dirnames, filenames) in os.walk(self._TMP_DIR): #@UnusedVariable
            filenames = ["%s/%s" % (self._TMP_DIR, f) \
                         for f in filenames if f.endswith(".py")]
            insert_imports.main(filenames)
            dircmp = filecmp.dircmp(self._TMP_DIR, self._RESULT_DIR)
            self.assertTrue(dircmp.left_only == dircmp.right_only == [], \
              "Some files missing in copy \n Left:\n%s\nRight:\n%s" % \
                (str(dircmp.left_only), str(dircmp.right_only)))
            self.assertTrue(dircmp.diff_files == [], \
              "Some files not identical: " + str(dircmp.diff_files))
            
    def test_help(self):
        for param in ("-h", "--help"):
            string_file = StringIO.StringIO()
            try: 
                sys.stdout = string_file
                try:
                    insert_imports.main((param,))  # Will do a system exit
                except:
                    pass
                self.assertEqual(insert_imports.__doc__+"\n", \
                                 string_file.getvalue())
            finally:
                string_file.close()
                sys.stdout = sys.__stdout__
    
    def test_bad_flag(self):
        string_file = StringIO.StringIO()
        try: 
            sys.stdout = string_file
            try:
                insert_imports.main(("--bad_flag",))  # Will do a system exit
            except:
                pass
            self.assertEqual(self.__invalid_arguments_message(), \
                             string_file.getvalue())
        finally:
            string_file.close()
            sys.stdout = sys.__stdout__
        
    def test_bad_file(self):
        string_file = StringIO.StringIO()
        try: 
            sys.stdout = string_file
            try:
                insert_imports.main(("xxx",))  # Will do a system exit
            except:
                pass
            self.assertTrue(string_file.getvalue() \
              .startswith('Unable to process source_file "%s": ' % ("xxx",)))
        finally:
            string_file.close()
            sys.stdout = sys.__stdout__
    
    def test_zero_arg(self):
        string_file = StringIO.StringIO()
        try: 
            sys.stdout = string_file
            try:
                insert_imports.main(())  # Will do a system exit
            except:
                pass
            self.assertEqual(self.__invalid_arguments_message(), \
                             string_file.getvalue())
        finally:
            string_file.close()
            sys.stdout = sys.__stdout__
    
    def __invalid_arguments_message(self):
        return "".join(("Invalid argument(s).", "\n", insert_imports.__doc__, \
                        "\n"))
    
    def __delete_tmp_dir(self):
        if os.path.exists(self._TMP_DIR):
            shutil.rmtree(self._TMP_DIR)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()