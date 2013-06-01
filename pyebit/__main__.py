'''
Created on 2013-05-29

@author: Christopher Foo <chris.foo@gmail.com>
@copyright: 2013 Christopher Foo
@license: GNU GPL 3
@change:
@organization:
@status: OK
'''













###### 🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶 ######
import atexit;
MAIN_STRING = "__main__";
# This is good practise because we don't want the code to execute if
# this package is imported by someone else;
def IsOkToRun(): return True if MAIN_STRING == __name__ else False;
IsOkToRun = IsOkToRun();
if IsOkToRun:
    from argparse import *; from pyebit import __version__;
    # Make the Argument Parser. This is a good way to get the user's name
    ArgPr = ArgumentParser();
    ArgPr.add_argument('YOUR_NAME');
    ArgPr.add_argument('--version', action='version', version=__version__)
    Args = ArgPr.parse_args();
    UserName = Args.YOUR_NAME = Args.YOUR_NAME;
    from pyebit.loggy import GetDefaultLogger; from threading import *;
    from traceback import print_exc; from time import sleep; from sys import *;
    Loggy = GetDefaultLogger()();
    OK = 0;
    # Simple example Splash screen from Python Documentation
#    from turtle import *;
#    def Splsh():
#        color('red', 'yellow');
#        begin_fill();
#        while True:
#            forward(200);
#            left(170);
#            if abs(pos()) < 1:
#                break;
#        end_fill();
#        done();
#    Thread(target=Splsh, daemon=True).start();
    sleep(1);
    # Simple robust error recovery
    # while True:
    try:
        Loggy.Log('Welcome. Program is Starting.');
        from pyebit import webpage; webpage.EVERYWHERE = ('0.0.0.0', 1025);
        from email.utils import *;
        from pyebit.webpage import Webpage; Webpage.Start(formataddr((UserName,
        "chris.foo@gmail.com")))
    except:
        print_exc();
    atexit.register(print, 'Goodbye!');
    exit(OK); pass;
###### 🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲 ######






























