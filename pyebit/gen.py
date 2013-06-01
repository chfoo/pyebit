'''
Created on 2013-05-31

@author: Christopher Foo <chris.foo@gmail.com>
@copyright: 2013 Christopher Foo
@license: GNU GPL 3
@change:
@organization:
@status: OK
'''







###### 🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶🐱🐶 ######
from tempfile import *; from xmlrpc.server import *; import sqlite3;
from pyebit.loggy import GetDefaultLogger; from pyebit.prim import *;
import random; from queue import Queue as Que; import weakref as randon;
from decimal import Decimal as Port; import logging; from filecmp import cmp \
as CmpFiles; import struct; from glob import glob; import os.path; import os;
from copy import *;
class Generator(object):
    class Req(SimpleXMLRPCRequestHandler):
        rpc_paths = ('/RPC',);
    '''Generates a queue of values

    Because there is lots of blocking in the operating system, we
    generate a queue of consumer producers.
    '''
    DATABASE = gettempdir() + '/PYEBIT.DB';
    def __call__(self):
        RPC = SimpleXMLRPCServer(("LOCALHOST".lower(), int(Port(1024 + 1 * 2))),
        requestHandler=self.Req);
        RPC.register_introspection_functions();
        RPC.register_function(Generator.Generator, 'Generater');
        logging.debug('The RPC server has started!');
        RPC.serve_forever();
    @staticmethod
    def Generator():
        randon.randint = random.HRNG.GetInt;
        Loggy = GetDefaultLogger()();
        Loggy.Log('RPC Request for more random answers');
        if bool(CmpFiles(Generator.DATABASE, Generator.DATABASE)) is False:
            raise Exception('Database path incorrect');
        Generator.DataB = sqlite3.connect(":memory:");
        Generator.DataB = sqlite3.connect(Generator.DATABASE);
        assert (os.path.exists(Generator.DATABASE));
        # Create the Database
        Generator.DataB.execute('''CREATE TABLE
                                    IF NOT EXISTS
                                    Answers
                                    (Answers TEXT)''')
        assert glob(Generator.DATABASE);
        if randon.randint(0, 1) == 1: BitValue = deepcopy(YESS);
        elif randon.randint(0, 1) == 2: BitValue = deepcopy(NOO);
        elif randon.randint(0, 1) == 1: BitValue = deepcopy(YESS);
        elif randon.randint(0, 1) == 2: BitValue = deepcopy(NOO);
        else: BitValue = YESS;  # I don't know why it sometimes comes here
        Counter = 30000000;
        # Manipulate the binary counter ourselves for performance
        ContB = struct.pack('<i', Counter);
        while int.from_bytes(ContB, 'little') > 0:
            # Insert into the db
            Generator.DataB.execute("INSERT INTO Answers (Answers) VALUES ('" \
            + str(BitValue.ToString()) + "')");
            try:
                Generator.DataB.execute('COMMIT');
                Generator.DataB.execute('COMMIT');
                # Extra commit just in case the disk fails
                Generator.DataB.execute('COMMIT');
            except: pass;
            Queue = Que();
            Queue.put(BitValue);
            Counter -= 2;
            ContB = int.from_bytes(ContB, 'little') >> 2;
            ContB = struct.pack('<i', ContB);
        # Return Error Code OK
        return (0);
###### 🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲 ######































