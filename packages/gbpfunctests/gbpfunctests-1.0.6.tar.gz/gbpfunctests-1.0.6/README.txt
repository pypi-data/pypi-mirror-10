# This test-suite comprise:
# GBP Functional Testcases
#
# Assumptions:
# 1. The pip install will put this package by default in
#     /usr/lib/python2.7/site-packages/gbpfunctests/ (for RHEL)
#    /usr/local/lib/python2.7/dist-packages/gbpfunctests/ (for Ubuntu)
#
# 2. Before the user runs any test,user will source the rc file needed for keystone authentication
#
# Usage: User can run each test-script or entire test-suite(run_suite.sh) in any of two ways:
#        1. If the default location of the package is appended to the $PATH
#           then executable files can be run rom anywhere
#        2. The executable can be run from the default location
#        3. To run any standalone testsuite file, execute "python tc_gbp_*" in "testcases" directory
#        4. To run the complete suite, execute "python suite_run.py" in "testcases" directory
#
# Test Report: Depending on the location from where the suite is run, a file "test_reports.txt" 
#              get created in that location. This comprise the consolidated test results of the suite
