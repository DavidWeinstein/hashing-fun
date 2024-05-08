# import HashTest, GeneralHashFunctions
from GeneralHashFunctions import *
from HashTest import * 
import time
lookup_key = "Ni8zUB2sCARuk7jg"
found_count = 0


def lookUp(val):
     global found_count
     boo = False
     hash = DGWHash(val) % capacity
     if sym_table[hash] == -1:
          boo = False
     elif sym_table[hash] != val:
          for i in range(1,100):
            hash = (DGWHash(val) + i^2) % capacity
            if sym_table[hash] == val:
                boo = True
                found_count += 1
                break
     elif sym_table[hash] == val:
          boo = True
          found_count += 1
     return boo

def array_lookup(val):
     global found_count
     global false_count
     false_count = 0 
     start = time.time()
     for i in range(len(key_array)):
          if key_array[i] == val:
            #    print('found')
               found_count += 1
               return True
     end = time.time()
     
     time_taken = (end - start) * 1000
    #  print(time_taken, 'array')
     false_count += 1
     return False


# array_lookup(lookup_key)
start = time.time()
lookUp("123456")
end = time.time()
print("non existent lookup test: " + str(((end - start)) * 1000))

with open("keys.txt", 'r') as r:
     start = time.time()
     for line in r:
          lookUp(line.strip())
     end = time.time()
     print("*****Using hashing lookup*****")
     print("Found " + str(found_count) + " records in " 
           + str((end - start) * 1000) + " milliseconds\n")

with open("keys.txt", 'r') as r:
     start = time.time()
     count = 0
     print("*****Using array search*****")
     found_count = 0

     for line in r:
          count +=1
        #   if count == 100000:
        #        break
          if count % 10000 == 1 and count != 1:
               now = time.time()
               so_far = (now - start) * 1000
               print("Found " + str(found_count) + " records " + str(so_far) + " milliseconds spent so far")
          array_lookup(line.strip())
          # array_lookup(lookup_key)
     end = time.time()
     print(str((end-start) * 1000))

