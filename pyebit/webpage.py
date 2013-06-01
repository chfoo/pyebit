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
# Useful constants
HTML = 'HTML';
GT = '>';
LT = '<';
EQUAL = "=";
BODY = "BODY";
HEAD = "HEAD"
TITLE = "TITLE";
NBSP = "&NBSP;";
HTML5 = "HTML5";
NEWLINE = '\r\n'; SPACE = " ";
STYLE = "Style";
# Don't forget to update the CONSANTS TABLE
__CONSTANTS__ = {HTML: True, GT: True, LT: True, EQUAL: True, HEAD: True}
import io; from pyebit.loggy import GetDefaultLogger; import sqlite3; from \
sched import *; import shutil; from calendar import HTMLCalendar; from difflib \
import *; from json import dumps as DumpJSON; import codecs; from datetime \
import datetime; import pickle as pickel; from pyebit.loggy import \
GetDefaultLogger; from pyebit.prim import *; from http.server import *;
import webbrowser; from zlib import *; from time import *; from csv import *;
import random; from pyebit.ran import *; import cgitb; from textwrap import *;
from email.utils import *; from pyebit.gen import *; import threading; from \
tempfile import *; cgitb.enable(); from re import *; from urllib.parse import *
class Web_Page(BaseHTTPRequestHandler):
    '''The WebPage Interface for the User to get the answer'''
    Loggy = GetDefaultLogger()();
    Buffer = io.StringIO();
    Username = 'Computer User';
    Choice = None;
    def __del__(self):
        pass;
    def __init__(ｓｅｌｆ):
        Web_Page.Choice = NONE;
    class ProducerRetreiver(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self);
            self.daemon = False or True;
            self.Run = self.__Start;
            self.run == self.Run;
            self.start();
        def __Start(self):
            DATABASE = gettempdir() + '/PYEBIT.DB';
            Database = sqlite3.connect(DATABASE);
            while super:
                if Web_Page.Choice == 'PROCESING':
                    # Make a request to the GEN server
                    Web_Page.Loggy.Log('Make a request to the GEN server');
                    import xmlrpc.client;
                    proxy = xmlrpc.client.ServerProxy("http://localhost:1026/RP"
                    "C");
                    proxy.Generater();
                    # Check if the database has an answer
                    for DBR in Database.execute('''Select * From Answers'''):
                        Answer = DBR[0];
                        break;
                    else:
                        # Sleep to not use up CPU
                        sleep(5);
                        Answer = NONE;
                    # We have a Bit answer
                    if Answer:
                        Web_Page.Loggy.Log('# We have a Bit answer');
                        Web_Page.Choice = Answer;
                        # It is possible that the database has gone corrupt
                        # so check if it has not corrupted
                        if not match('[YyEeSsNnOo]', Web_Page.Choice):
                            Web_Page.Choice = NONE;
                        elif not get_close_matches(Web_Page.Choice.upper(), ['Y'
                        'ES', 'NO']):
                            Web_Page.Choice = NONE;
                # Wait until there is a request
                Event().wait(timeout=5);
                scheduler(time, sleep);
        def Run(self): pass;
        def run(self): self.__Start();
    def Start(ｓｅｌｆ, UserName):
        random.HRNG = High_Random_Number_Generator();
        import threading;
        Web_Page.Username, Web_Page.Email = parseaddr(UserName);
        ｓｅｌｆ.Loggy.Log('The web page starts up');
        # Start up the web server
        # We use 0.0.0.0 so it can be hosted on a LAN
        ｓｅｌｆ.HTTPServer = HTTPServer(EVERYWHERE, Web_Page_Fire_Fox);
        # TODO: Use ssl.wrap_socket for Phase 2
        webbrowser.open_new('http://localhost:1025/index.htm');
        T = threading.Thread(target=Generator());
        T.daemon = True;
        T.start();
        PC = ｓｅｌｆ.ProducerRetreiver();
        ｓｅｌｆ.HTTPServer.serve_forever();
    def MakeText(ɟʅəs):
        '''Make the webpage''';
        # The XML module is too complex and has too much overhead so we
        # make the HYML ourselves
        # String concatenation is very expensive so a String Buffer is useful
        ɟʅəs.Buffer.seek(0)  # Be sure to clear the buffers
        ɟʅəs.Buffer.write(LT);
        assert __CONSTANTS__[LT] is True;
        ɟʅəs.Buffer.write("!DOCTYPE html");
        ɟʅəs.Buffer.write(GT + NEWLINE);
        assert __CONSTANTS__[GT] is True;
        assert __CONSTANTS__[EQUAL] is True;
        for C in [A for A in __CONSTANTS__ if A not in frozenset([LT, GT,
        EQUAL])]: assert __CONSTANTS__[C] is True;
        # Put web page title
        ɟʅəs.Buffer.write(LT + "TITLE" + GT + 'The Python Enterprise Bit' + \
        Web_Page.CloseTag('TITLE'));
        ɟʅəs.Buffer.write(LT + BODY + SPACE + STYLE + EQUAL + \
        '"BACKGROUND-COLOR: #B0B0B0; COLOR: #000000; FONT-FAMILY: ' + \
        "'TIMES NEW ROMAN'" + ', serif;' + \
        '''BACKGROUND: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUg'''
        '''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');'''.replace('\r', '').replace(
        '\n', "") + '"' + GT)
        # Put Welcome message
        ɟʅəs.Buffer.write(LT + "DIV" + SPACE + STYLE + EQUAL + \
        "FONT-SIZE:400%" + GT + "Welcome ")
        ɟʅəs.Buffer.write("%s" % (ɟʅəs.Username) + Web_Page.CloseTag("DIV"))
        ɟʅəs.Buffer.write(NEWLINE)
        if ɟʅəs.IsProcessing:
            # Put waiting mesg
            ɟʅəs.Buffer.write(LT + "MARQUEE" + GT)
            ɟʅəs.Buffer.write(LT + 'BLINK STYLE="' + \
            ɟʅəs.MakeBorderStyle() + '">Please wait.')
            ɟʅəs.Buffer.write(ɟʅəs.CloseTag('MARQUEE'))
            ɟʅəs.Buffer.write(NEWLINE)
            ɟʅəs.Buffer.write(ɟʅəs.CloseTag('BLINK'))
            ɟʅəs.Buffer.write(LT + "PROGRESS" + GT + 'Please wait')
            ɟʅəs.Buffer.write(ɟʅəs.CloseTag('PROGRESS'))
        elif ɟʅəs.Choice is None:
            ɟʅəs.Buffer.write(LT + 'STRONG' + GT + \
            "Please click the QUERY button to get an answer!" + ɟʅəs.CloseTag(
            'STRONG'))
            ɟʅəs.Buffer.write(ɟʅəs.CloseTag('BR') * 2)
        else:
            ɟʅəs.Buffer.write('The Bit answers: ')
            ɟʅəs.Buffer.write(NEWLINE)
            ɟʅəs.Buffer.write(NEWLINE)
            ɟʅəs.Buffer.write(LT + "INPUT VALUE" + EQUAL)
            # Use csv in case the user wants to put the answer into Excel
            Writ = writer(ɟʅəs.Buffer)
            Writ.writerow(list([ɟʅəs.Choice]))
            ɟʅəs.Buffer.write(GT)
            DATABASE = gettempdir() + '/PYEBIT.DB'
            Database = sqlite3.connect(DATABASE)
            Database.execute('DROP TABLE IF EXISTS Answers')
            ɟʅəs.Buffer.write(LT + 'BR' + GT)
            ɟʅəs.Buffer.write(NEWLINE)
            ɟʅəs.Buffer.write(LT + 'STRONG' + GT + "Please click the "
            "QUERY button to get an answer!" + ɟʅəs.CloseTag('STRONG'))
            ɟʅəs.Buffer.write(NEWLINE)
            ɟʅəs.Buffer.write(NEWLINE)
            ɟʅəs.Buffer.write(ɟʅəs.CloseTag('BR').replace('/', '') * 2)
        ɟʅəs.Buffer.write(LT + 'FORM METHOD=POST' + GT)
        ɟʅəs.Buffer.write(NEWLINE)
        ɟʅəs.Buffer.write(NEWLINE)
        ɟʅəs.Buffer.write(LT + 'BUTTON TYPE=SUBMIT ><IMG ' + ' ' \
        + SPACE + NEWLINE + STYLE + EQUAL + '"WIDTH:329PX;HEIGHT:110PX;'
        '\'\';BACKGROUND:url(\'data:image/png;base64,' + ＢＵｔｔＯｎ + "');" \
        + '">')
        ɟʅəs.Buffer.write(ɟʅəs.CloseTag('BUTTON'))
        ɟʅəs.Buffer.write(ɟʅəs.CloseTag('FORM'))
        # Users are office users that need a calendar to meet deadlines
        ɟʅəs.Buffer.write(LT + "i" + GT + "The time is %s" % datetime.today().ctime())
        ɟʅəs.Buffer.write(HTMLCalendar().formatmonth(datetime.today().year, datetime.today().month))
        ɟʅəs.Buffer.write(ɟʅəs.CloseTag('BR') * 2)
        ɟʅəs.Buffer.write(NEWLINE)
        ɟʅəs.Buffer.write(NEWLINE)
        ɟʅəs.Buffer.write(NEWLINE)
        ɟʅəs.Buffer.write(' ')
        # Put Friendly User interface message
        ɟʅəs.Buffer.write('<SMALL>How are you?</SMALL>') if set((str(int(time()))[-1])) & set('12345') else ɟʅəs.Buffer.write(NBSP + LT + "SMALL" + GT + 'Have nice day!')
        # Put Copyright Message
        if ' ' == ' ': ɟʅəs.Buffer.write("Copyright: 2013 by Christopher Foo. All rights reserved.")
        ɟʅəs.Buffer.write('</HTML>')
        # JSON API support
        ɟʅəs.Buffer.write("<!--")
        ɟʅəs.Buffer.write(DumpJSON(dict(ANSWER=ɟʅəs.Choice)))
        ɟʅəs.Buffer.seek(0)
        # Encode the String
        codec = codecs.getencoder('ROT-13')
        yield codec(ɟʅəs.Buffer.read())[0]
        # Clean out the old buffer while reusing the space by copying the data
        # into a tmp which will be garbage collected. But the original
        # buffer will still be allocated
        Tmp = io.StringIO()
        shutil.copyfileobj(ɟʅəs.Buffer, Tmp)
    @classmethod
    def CloseTag(cls, tag):
        return LT + '/' + tag + GT
    def MakeBorderStyle(self):
        return "BORDER: 1PX SOLID WHITE"
    def do_GET(self):
        OK = 200
        self.Buffer = Web_Page.Buffer; self.Username = Web_Page.Username
        self.Choice = Web_Page.Choice
        self.Loggy.Log('Get request')
        self.send_response(200,)
        # Pretty print the html
        Dat = list(self.MakeText())[0]
        codec = codecs.getdecoder('ROT-13')
        Dat = codec(Dat)[0]
        Dat2 = ''
        for Line in wrap(Dat):
            Dat2 += Line
            if Line[-1] == ">": Dat2 += '\r\n'
            elif Line[-1] != ' ': Dat2 += ' '
        # Compress to save memory while we wait and push HTML to the client
        Dat = compress(Dat.encode('utf8'))
        self.send_header('Content-Length', len(decompress(Dat)))
        if self.IsProcessing: self.send_header('ReFresh', 4)
        else: self.send_header('ReFresh', 1)
        self.send_header('Content-Type', 'text/html; charset=UTF-8')
        self.end_headers()
        self.wfile.write(decompress(Dat))
    @property
    def IsProcessing(self):
        return self.Choice == 'PROCESING'
    def do_POST(self):
        urlparse(self.path)
        self.Choice = 'PROCESING'
        OK = 200
        self.Buffer = Web_Page.Buffer; self.Username = Web_Page.Username
        self.Choice = Web_Page.Choice
        self.Loggy.Log('Get request')
        self.send_response(200,)
        Dat = list(self.MakeText())[0].encode('utf7')
        self.send_header('Content-Length', len(Dat))
        self.send_header('ReFresh', 1)
        self.send_header('Content-Type', 'text/html; charset=UTF-7')
        self.end_headers()
        self.wfile.write(Dat)
        Web_Page.Choice = 'PROCESING'
        Choice < -NewChoice
class Web_Page_Fire_Fox(Web_Page):
    '''The WebPage Interface optimized for FireFox™'''
    def __init__(self, *argument, **mappery):
        BaseHTTPRequestHandler.__init__(self, *argument, **mappery)
    def MakeBorderStyle(self):
        return "border: 1px SOLID WHITE"
Webpage = Web_Page()
ＢＵｔｔＯｎ = "" \
"""iVBORw0KGgoAAAANSUhEUgAAAUkAAABvCAYAAABhCDI3AAAABmJLR0QA/wD/AP+gvaeTAAAACXBI
WXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QYOAzIxswPN0AAAABl0RVh0Q29tbWVudABDcmVhdGVk
IHdpdGggR0lNUFeBDhcAACAASURBVHja7Z3pb1z3dffPcJnhKpKiRJGUKMlaaEm2vEeOl9SJYcMt
Wicx0jZGU7QN0jdNULRo33T5Awr0Vf2mQQF3cwvXqYMmqeMlsSvXsSW5am3JsqzFEiVqJyWSIiUu
M8Mh+bzocy6+85lzRxuTPMDDCwSRJXLm3vv7/c7yPd/zPZljx44t2NK1dC1dS9fSxesfN2/e/Ds1
S+9h6Vq6lq6lK7z+wcxsyUguXUvX0rV0VbmWjOTStXQtXUvXkpFcupaupWvpWjKSS9fStXQtXUtG
culaupaupetnedVV+8ddu3ZZbW2tzc/PJ3+3sPC/jKH5+XnLZDIVf85kMjY3N2c1NTW2sLBgCwsL
VldXl/yef0Ztba3V1PyvjZ6bmyv73tra2uR39Xdqamosk8nYwsJCck/z8/PJ5/ifS6WSZTKZ5B5q
amqspqYm+Z65ubmy58pkMmV/9u/we5+bmyv7Hv9d/x3/bP/umpoam5+ft7q6OiuVSsn78c/w+/e/
9+/zf6uvr0+eu1QqJfdSX19vc3NzZe9A34m/N38X/nfV1qe2tjb5rkwmY7W1tcl78nc4NzeX3IPe
rz9/fX198r36Gf4ztbW1yfPrPetaz83NlX3O3Nyc1dXVWW1trZVKpYo95O/V79/vxZ/Xn8/Xz+9N
11jX3dcx2o/8Wf8c/7O/l/n5+eTd+uf4uurf67vl/vZ35mtTKpXK3pP/m78P3cv+GfpMfu/+9/pn
fU9lkdP/3cf6nbpv/PN1T+gZ5N72y9+P7h19N9yntC3+XbOzs8n36XvTe9L75p/9DGUyGTtw4ECq
/Xv55Zf/85pGUm9cN45uMj0Uuol04fzh/ObUCOpB9ofUDe+/o0ZX780PiRoHNYq6ePoS1fCpwfF/
142um93MbHZ2Njn4/pk8jJlMJjGYfoB8Y+sh4ALSmOj9czPV1NSUGTXd7HV1dcl36s+7wfF3qOtC
Y+3Pp5vQ792/g4dFjTgdnh4mNc7qYPzn+W6KxWLZO6bxp5Pwa3Z2tsyY6ef6Gupe9GfU+9a9oT+v
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
JWoENPpiEYQprHPsdHRqJpOxnp4eu3DhQpmRHB4etpaWFrt69WqFYAFbUaMuDF1jjk1lNZMQDgeJ
XSsT0WJLNHdGI8s0A6DGOhJkribim/aZUaGHgUg09iIyCP67a9euDffPvn377MKFCxX6CjqTXSNw
UoAUp3ajR52H3bt3l1G1dBqoR4ns52agQKgnGn0bjaRg08It8yTp4fXLmBpTAt9fgvflKrjqwKse
xqiX8nosPrtSSBeIpqVdj5acFmUYIfjhe+WVV2zfvn327LPPpvIfDxw4YO+8845dvnzZZmZm7Pjx
43blypUyp1BfX28bN260lpaWhCpDp6TCqLW1tbZ169ZExMCvwcHBMlJ7RNEi9KE8QDoDTa/9e7W3
mpXIDRs2VPQZe6+vFp3IktC9QaMRDYIaGxuzb3/72/aP//iPdu7cuXC8rBKV0zBtLZxwLEQ0+sPv
Pa1nn3qfhBL08xklV4O72DlDAxiNOtYRshHGe/vtt4f7xztjfJ/re/Q1Vy5oNC5FI3ud90Nb4hxR
8qN1TAnn8xCyYCCgv8NATt8l5yLddCRJJn9EBo4qwtFIWW4mGiyNGnXA1rWMJMv/eiCUYMqNVw1f
8uhXK62qWD49PW0vvviitbe329e//nXr7+9Pfre5udnuvPNOa2xstLfeessGBgaS321ubrZ8Pm8D
AwPW19dnnZ2dZc++du1aa2xstLNnzybFkYgF4NzLPXv22NDQUCLh5rL6Xihxg8bITVMxYmQaGXLN
VEk9Ggh/991323e/+90yMWNGFNlstuzvCaYrpEEYpaamxo4ePWr/9E//ZA888ID94i/+orW3t1t9
fb1NTU0lPDydoeOGIiKDT05OVsyKpoPRavLevXvtjTfesHvuuSfVqEXFPlLGdLwwjZfex8zMTILn
skmDVXw1AlNTU7Z79247efKkdXZ22mOPPVa21+rr623Dhg22e/fucP/4ZyqpnxQaOgPdC1ooUzgt
yjr97DKwiahTlFBjYY6QBrMNzphflHSbURnDWk0bKDCqnoSYIFMublBWtTKZTOoMEG6sSHmYVBI3
EGmKywoK+wb1xTt37px997vftbvuusu+/OUv24oVKyp+f2pqyl577TW7ePFiBVTR0NBgExMTNjg4
aO3t7WX/XiqVbOXKlZbNZu3kyZNJcSeqsGcyGXvggQds3759CbbpTmvlypV24sQJy+fztnr16ooo
RLFgGjpfjytXriS96cPDwzY1NWWdnZ328MMPW29vb9m6+eFta2uz5cuX26effmrbt28v20PLli2z
wcFBm56etjVr1lQ4V84117k6rrj9n//5n7Znzx576qmn7IknnrBsNmutra22atUq279/f8LNi6LS
trY2y+fzZUpCQ0NDFXgpKTPFYtH27dtn7733nuVyOfvSl75kn/nMZ8K9yKiFDpYGQvepNyRowe/s
2bNlbbrRfHs1wKOjo7Z79247cuSIrV+/3p5++mnbtGlT4jTGx8fLvnvHjh3h/unq6rITJ04klC6S
2QmBMNMys2T8xtDQkI2MjCTUnwceeMDa29vDEcXVWCP8+TTWDPnZLO5Vm8d+04UbNVgcwsMv4cGh
1dbUIA0v9P9++eWXbXx83JqbmxdlBkhUdU2TVGN7YrFYtF27dtmpU6fMzOyJJ56wJ598soLu4p97
9OjR5P0pQdYN4d69e23FihW2ffv2iuqiC/z29/fboUOH7NChQ9bf328dHR0VM3E2btxou3btsmPH
jtnWrVuTTZzL5Wzr1q126tQp27t3r9XW1iaiGi0tLUk1vVAoWLFYtKmpKRsfH7eRkREbHh5Oikwr
V660NWvW2B133GGrV6+2trY2K5VKlsvlbHx8vGx8qh+Sxx9/3N59913r6+tL0lLf/Js2bbKTJ0/a
rl27rK6uztrb2629vT2ZmZLNZpPWuUKhYJOTkzY0NGSnTp2ygYEB6+zstN/6rd+yu+++O3kH7e3t
Ce9OI0mNVs3MVq1aZefPn7dNmzaVQQFTU1N2/vx5a2xsTEYNXL161c6dO2fHjx+3gYEBa2trs8cf
f9zuu+++Cm1M3YsDAwP2zjvv2Gc/+1nbtm1bRSTMyFKLFt4vv27durJIN5/P2+DgYDK0zUeM5PN5
m5mZsZGREbtw4YJ9+umnSafZ17/+ddu8eXPy7G1tbbZy5UrbtWtXWYq6efNme+edd6ruH5971N7e
bi0tLdbQ0JB0S7mC1NTUlE1OTibKRq5u5Pvn3nvvLds/CwsLdurUqQqZM+3C0znZ0Sha0vE0slS5
NG2fvdGqdmLXjh07lmpO33zzzbB9j+mFejMC0iqAyTa2KOxdWFiw5557zvr6+uzXf/3XrzlbZLGv
HTt22EsvvVT2bN/73vdsYmLCvvSlL1l/f3/qQVFHcfXqVaurq0sGh7lx+973vmdTU1P2G7/xG4kA
RrXPKRaLNjExYQ0NDTYyMlLWw+vqQgcPHrTt27cnHE9GjSMjI3bkyBE7c+aMXb582aamppK0tq6u
znK5nC1btsw6Ojps1apV1tPTY11dXRX6jX5Yuru77f33369Ia3wPHD582IrFot17770VA7T0nj79
9FM7e/asjY2NJfekh6SxsTFR8t64caP19fUl6bqTqB966CEbGRlJigGRMZqbm7P333/fisWiPf30
0xX45YULF2zv3r02MDBgMzMzVl9fb21tbbZ69WrbvHmzrVu37ro5hXV1dXblyhVrb29PtBN1rjW7
gnwd33vvvUTDkvc3PDxsH3zwgZ06dcomJiaSwCWbzVpLS4utWrXK+vr6bOPGjSFe2t/fb+3t7fb6
669XnLlCoWAfffTRz3T/dHV12SuvvJLafqzpNxkyrDuwsUMHhHFiZYT37t+/P3UtX3755cw1I0kF
q8lBi2TUIvUT/VnifAr8a1p78eJF+/M///OfiuT/9V5aaDh06JD9wR/8gd11113X/D0/DL29vdbb
22unTp0qS98OHz5sf/zHf2y33377dX2OimT86Ec/qtDmbGhosDvuuMPOnz+fVJgVVzL731ESjzzy
yKK8l76+PmtqakrWT7/HHWJ/f78dP37cjh49mgxNIxuhs7PTHnrooZu+j8bGRtu+fbtls1k7ePBg
SBfyvVlfX28PPPCA/du//ZudP3/eVq9eXYYPdnV12a/8yq8syvtxxsK2bdvs3Xffreibp+q977Ed
O3bY97//fRseHk7GO/j9rVixwp566qmbXq/169fbsWPHKih6jhFv27btZ7p/nEHCbj3F4KOBgwzC
IjsVBXXEL6PC801Xt5WUSgEKGkX9dx1QpZQH7aRxw+jf4VL2NztbZDEvkpvb29tv2GD7pDjy/To7
O2/qs3RqIbs3nMo0NTVlg4ODPxWOW1tbm919993W3d1tp06dqhBAVdWk+fl527Rpk7W2ttq5c+dC
6bdbcV7r1q2zBx54wGpqamznzp02OTlZtueiyZ0NDQ32xBNP2KFDh+zy5cs3/L2OpzU3N9vFixer
/mxHR4c1NzeX8YlVrYfFTe9++dznPmeHDx+2sbGxW+YidnV12Wc+8xlbt26dDQwM2AcffFCRpXik
lcvlbPXq1T+z/eMMCK+Us7/cIRzOu6e0GsfEKIyhTSxRY0gkInxTmGSaCIQrY7vBSxPJJZDNFiQF
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""".replace('\n'
, '').replace("\r", '');
###### 🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲 ######

































