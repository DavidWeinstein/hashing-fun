#
#**************************************************************************
#*                                                                        *
#*          General Purpose Hash Function Algorithms Library              *
#*                                                                        *
#* Author: Arash Partow - 2002                                            *
#* URL: http://www.partow.net                                             *
#* URL: http://www.partow.net/programming/hashfunctions/index.html        *
#*                                                                        *
#* Copyright notice:                                                      *
#* Free use of the General Purpose Hash Function Algorithms Library is    *
#* permitted under the guidelines and in accordance with the MIT License. *
#* http://www.opensource.org/licenses/MIT                                 *
#*                                                                        *
#**************************************************************************
#


def RSHash(key):
    a    = 378551
    b    =  63689
    hash =      0
    for i in range(len(key)):
      hash = hash * a + ord(key[i])
      a = a * b
    return hash


def JSHash(key):
    hash = 1315423911
    for i in range(len(key)):
      hash ^= ((hash << 5) + ord(key[i]) + (hash >> 2))
    return hash


def PJWHash(key):
   BitsInUnsignedInt = 4 * 8
   ThreeQuarters     = (BitsInUnsignedInt  * 3) // 4 #modified for py3
   OneEighth         = BitsInUnsignedInt // 8 #modified for py3
   HighBits          = (0xFFFFFFFF) << (BitsInUnsignedInt - OneEighth)
   hash              = 0
   test              = 0

   for i in range(len(key)):
     hash = (hash << OneEighth) + ord(key[i])
     test = hash & HighBits
     if test != 0:
       hash = (( hash ^ (test >> ThreeQuarters)) & (~HighBits));
   return (hash & 0x7FFFFFFF)


def ELFHash(key):
    hash = 0
    x    = 0
    for i in range(len(key)):
      hash = (hash << 4) + ord(key[i])
      x = hash & 0xF0000000
      if x != 0:
        hash ^= (x >> 24)
      hash &= ~x
    return hash


def BKDRHash(key):
    seed = 131 # 31 131 1313 13131 131313 etc..
    hash = 0
    for i in range(len(key)):
      hash = (hash * seed) + ord(key[i])
    return hash


def SDBMHash(key):
    hash = 0
    for i in range(len(key)):
      hash = ord(key[i]) + (hash << 6) + (hash << 16) - hash;
    return hash


def DJBHash(key):
    hash = 5381
    for i in range(len(key)):
       hash = ((hash << 5) + hash) + ord(key[i])
    return hash


def DEKHash(key):
    hash = len(key);
    for i in range(len(key)):
      hash = ((hash << 5) ^ (hash >> 27)) ^ ord(key[i])
    return hash


def BPHash(key):
    hash = 0
    for i in range(len(key)):
       hash = hash << 7 ^ ord(key[i])
    return hash


def FNVHash(key):
    fnv_prime = 0x811C9DC5
    hash = 0
    for i in range(len(key)):
      hash *= fnv_prime
      hash ^= ord(key[i])
    return hash


def APHash(key):
    hash = 0xAAAAAAAA
    for i in range(len(key)):
      if ((i & 1) == 0):
        hash ^= ((hash <<  7) ^ ord(key[i]) * (hash >> 3))
      else:
        hash ^= (~((hash << 11) + ord(key[i]) ^ (hash >> 5)))
    return hash

'''
Added DGWHash to compare how many collisions I receive in my algorithm vs the other standard
hashing algorithms from the internet. Will also attempt to compare lookup speed with all algos.
'''
def DGWHash(key):
   largest_prime_to_a_milli = 999983
   largest_prime_to_1000 = 997
   hash = 1
   for i in range(len(key)):
      hash ^= ord(key[i]) * largest_prime_to_a_milli // largest_prime_to_1000
      hash = hash << 4
      # hash ^= ord(key[i])
   return hash

