#!/usr/bin/env python
#
#  export_tests.py:  testing export cases.
#
#  Subversion is a tool for revision control. 
#  See http://subversion.tigris.org for more information.
#    
# ====================================================================
# Copyright (c) 2000-2003 CollabNet.  All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.  The terms
# are also available at http://subversion.tigris.org/license-1.html.
# If newer versions of this license are posted there, you may use a
# newer version instead, at your option.
#
######################################################################

# General modules
import shutil, string, sys, re, os

# Our testing module
import svntest


# (abbreviation)
Skip = svntest.testcase.Skip
XFail = svntest.testcase.XFail
Item = svntest.wc.StateItem

 
######################################################################
# Tests
#
#   Each test must return on success or raise on failure.


#----------------------------------------------------------------------

def export_empty_directory(sbox):
  "export an empty directory"
  sbox.build()
  
  svntest.main.safe_rmtree(sbox.wc_dir)
  export_target = sbox.wc_dir
  empty_dir_url = svntest.main.current_repo_url + '/A/C'
  svntest.main.run_svn(None, 'export', empty_dir_url, export_target)
  if not os.path.exists(export_target):
    raise svntest.Failure

def export_greek_tree(sbox):
  "export the greek tree"
  sbox.build()

  svntest.main.safe_rmtree(sbox.wc_dir)
  export_target = sbox.wc_dir
  expected_output = svntest.main.greek_state.copy()
  expected_output.wc_dir = sbox.wc_dir
  expected_output.desc[''] = Item()
  expected_output.tweak(contents=None, status='A ')

  svntest.actions.run_and_verify_export(svntest.main.current_repo_url,
                                        export_target,
                                        expected_output,
                                        svntest.main.greek_state.copy())

########################################################################
# Run the tests


# list all tests here, starting with None:
test_list = [ None,
              export_empty_directory,
              export_greek_tree,
             ]

if __name__ == '__main__':
  svntest.main.run_tests(test_list)
  # NOTREACHED


### End of file.
