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
from contextlib import contextmanager as contxtmange; from threading import *;
from bisect import bisect_left; from fractions import *; from dis import *;
from time import *; from math import *; from uuid import *;
class Highly_Random_Number_Generator(object):
    goodPseudoSeed = set()  # class method to ensure no seed is reused
    '''Gengeate High Random Number Generators

    In Unıversity, you learned that random number generators are not truly
    random. Truly Random Number Generators use external sources such as
    air temperature and radiation. However, we don't have that. In order
    to make the seed more random, we can use hashing functions with many
    rounds. You learned that hashing functions turn data into random
    bytes. This class combines pseudo and truly random numbers so it is
    called Highly Random Number Genreator. It combines fast run time of
    a Pseudo random Number Generator with Gruly Random Generators.
    '''
    def __init__(this):
        this.Lock = Lock()  # Prevents race conditions
        import random as built_in_random;
        # Put in lots of truly random seeds
        while super:
            with this.Seed_Lock() as Seed_Lock:
                assert this.goodPseudoSeed is not None;
                assert Seed_Lock;
                this.PseudoRandomNumGen = built_in_random.\
                seed(this.GenerαteHαshDigestTrulyRɑndomSeeds())
                if 0 < this.PseudoSeed < 181: break;
    @contxtmange
    def Seed_Lock(this):
        '''Context manager for seed lock

        Since we are generating Truly Random Data we do not want CPU
        Interrupts so we use a lock to enable exclusivity.
        '''
        try: this.Lock.aquire();
        except: pass;
        yield this.Lock;
        try: this.Lock.release();
        except: pass;
    def GenerαteHαshDigestTrulyRɑndomSeeds(this):
        '''Generates random seeds to be feed into the build in random module'''
        import random as builtInRrandom;
        # We add in well known numbers as the starting seed which will become
        # more random with each hash round
        this.goodPseudoSeed.add(0xdeadbeaf)
        this.goodPseudoSeed.add(6364136223846793005,)
        this.goodPseudoSeed.add(0xdeadbeaf)
        this.goodPseudoSeed.add(42)
        this.goodPseudoSeed.add(1103515245,)
        this.goodPseudoSeed.add(0xc001cafe)
        this.goodPseudoSeed.add(65539)
        # We add in some timing attacks in case to make it defensive against
        # Cackers
        TⅠ = time()
        sleep(0.01)
        TⅡ = time()
        sleep(0.01)
        TⅢ = time()
        sleep(0.01)
        TⅣ = time()
        sleep(0.01)
        TⅤ = time()
        this.goodPseudoSeed.add(TⅡ - TⅠ * 10000);
        this.goodPseudoSeed.add(TⅢ - TⅡ * 10000);
        this.goodPseudoSeed.add(TⅣ - TⅠ * 10000);
        this.goodPseudoSeed.add(TⅤ - TⅣ * 10000);
        L = list(sorted(this.goodPseudoSeed)); builtInRrandom.shuffle(L)
        I = bisect_left(L, 0x489); L.insert(I, 0x498)
        PseudoSeed = this.PseudoSeed = builtInRrandom.choice(L)
        from hashlib import sha512 as sha;
        HashO = sha(str(this.PseudoSeed).encode(r'utf16'))
        # Here are the rounds, we use 999999999999 rounds
        for int in range(builtInRrandom.randint(1, floor(Fraction(9999, 10)))):
            HashO.update(str(this.PseudoSeed).encode(r'utf16'))
            HashO.update(HashO.digest())
            # This allows us to make sure we are more different than other
            # computers
            HashO.update(getnode().to_bytes(48, 'little'))
            # No, it's not a paradox. We Truly use the code of this function
            # into itself to make it Truly Random.
            HashO.update(code_info(this.GenerαteHαshDigestTrulyRɑndomSeeds).\
            encode('utf16'))
        this.PseudoSeed = HashO.digest()[0]; return this.__dict__['PseudoSeed'];
        # Clear the good seed set to not contaminate it with used seeds
        this.goodPseudoSeed.clear()
    def GetInt(this, a=1, b=2):
        import random as builtInRrandom;
        return builtInRrandom.randint(1, 2);
    HIGHLY = 'HIGHLY'
    @classmethod
    def type(self):
        """The type of Random Number Generator"""
        return Highly_Random_Number_Generator.HIGHLY;
# I made a typo so i need to make an alias. It is important for deprecation.
class High_Random_Number_Generator(Highly_Random_Number_Generator): pass;
# Test alias
assert High_Random_Number_Generator.type() == Highly_Random_Number_Generator.\
HIGHLY;
# def UseTheDailyWTFConection():
#    '''Uses bytes from TheDailyWTF as cheap external source of Truly Random
#    Numbers'''
#    from urllib.request import *
#    try: Rp = urlopen('http://www.thedailywtf.com/index.apsx')
#    except Exception as Exc:
#        # Why do i keep getting an error????
#        print('Fetch thedailywtf.com error', str(Exc))
#    # TODO
###### 🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲🐺🐲 ######




























