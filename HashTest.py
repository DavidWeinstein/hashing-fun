from GeneralHashFunctions import *
from numpy.random import seed
from numpy.random import randint
import random, string

# Code for making keys.txt file

# keys = []
# for i in range(1000000):
#     x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
#     keys.append(x)
# with open("keys.txt", 'w') as w:
#     for key in keys:
#         w.write(key + '\n')


print("We are hashing the value: nJJop5E7aMsieaKS in 11 standard hashing algorithms, and DGWHash hacked together by me.\n" )
print("RSHash:",RSHash('nJJop5E7aMsieaKS'))
print("JSHash:", JSHash('nJJop5E7aMsieaKS'))
print("PJWHash:", PJWHash ('nJJop5E7aMsieaKS'))
print ("ELFHash:",ELFHash ('nJJop5E7aMsieaKS'))
print ("BKDRHash:",BKDRHash('nJJop5E7aMsieaKS'))
print ("SDBMHash:",SDBMHash('nJJop5E7aMsieaKS'))
print ("DJBHash:",DJBHash ('nJJop5E7aMsieaKS'))
print ("DEKHash:",DEKHash ('nJJop5E7aMsieaKS'))
print ("BPHash:",BPHash  ('nJJop5E7aMsieaKS'))
print ("FNVHash:",FNVHash ('nJJop5E7aMsieaKS'))
print ("APHash:",APHash  ('nJJop5E7aMsieaKS'))
print("DGWHash:",DGWHash('nJJop5E7aMsieaKS'))
print("******************************\n\n")
hash_keys_set = set()
# hash_vals_set = set()
count=0

key_array = []
with open("keys.txt", 'r') as r:
    for line in r:
        hash = DGWHash(line.strip())
        hash_keys_set.add(hash)
        key_array.append(line.strip())
# print("There is " + str(len(key_array) - len(hash_keys_set)) + " collisions in hashing function")


sym_table = []
capacity = 2000003
for i in range(capacity):
    sym_table.append(-1)

with open("keys.txt", 'r') as r:
    count = 0
    for line in r:
        hash = DGWHash(line.strip()) % capacity
        if sym_table[hash] == -1:
            sym_table[hash] = line.strip()
        else:
            rehash_i = 1
            count +=1
            while(True):
                hash = (DGWHash(line.strip()) + rehash_i^2) % capacity
                if sym_table[hash] == -1:
                    sym_table[hash] = line.strip()
                    break
                else:
                    rehash_i += 1


print("Collisions when inserting to sym table that are dealt with: "+ str(count) + "\n\n")
