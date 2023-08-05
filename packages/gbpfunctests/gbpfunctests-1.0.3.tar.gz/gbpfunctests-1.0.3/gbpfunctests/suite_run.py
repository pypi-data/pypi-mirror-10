#!/usr/bin/env python
import os,sys,optparse,platform,subprocess
from commands import *

def run_func_neg():
    # Assumption is all files are in current directory
    if 'Ubuntu' in platform.linux_distribution():
        directory = "/usr/local/lib/python2.7/dist-packages/gbpfuncnegtest/"
    else:
        directory = "/usr/lib/python2.7/site-packages/gbpfuncnegtest/" ## in RHEL
    cmd_list=["sudo sh -c 'cat /dev/null > test_results.txt'",\
              "sudo sh -c 'cat /dev/null > func_neg.txt'",\
              "sudo sh -c 'ls %s/*func*.py > func_neg.txt'" %(directory),\
              "sudo sh -c 'ls %s/*_neg.py >> func_neg.txt'" %(directory),\
              "sudo chmod 777 %s/*" %(directory)]
    for cmd in cmd_list:
        getoutput(cmd)
    return "func_neg.txt"

def main():
    usage = "usage: suite_run.py [options]"
    parser = optparse.OptionParser(usage=usage)
    helpstr = "Valid values are 'func' OR 'aciint' OR 'dp'"
    parser.add_option('-s', '--suite', help='%s' %(helpstr),dest='suite')
    (opts, args) = parser.parse_args()
    if opts.suite == None:
       print 'Suite value needs to be passed'
       parser.print_help()
       sys.exit(1)
    if opts.suite == 'func':
      fname = run_func_neg()
      num_lines = sum(1 for line in open(fname))
      print "\nNumber of Functional Test Scripts to execute = %s" %(num_lines)
      with open(fname) as f:
        for i,l in enumerate(f,1):
            print "Functional Test Script to execute now == %s" %(l)
            # Assumption: test-scripts are executable from any location
            cmd='%s' %(l.strip()) # Reading the line from text file, also reads trailing \n, hence we need to strip
            print cmd
            #out=getoutput(cmd)
            subprocess.call(cmd,shell=True)
      f = open("test_results.txt")
      contents = f.read()
      f.close()
      print contents
      print "\n\nTotal Number of TestCases Executed= %s" %(contents.count("TESTCASE_GBP_"))
      print "\n\nNumber of TestCases Passed= %s" %(contents.count("PASSED"))
      print "\n\nNumber of TestCases Failed= %s" %(contents.count("FAILED"))
      
if __name__ == "__main__":
    main()

