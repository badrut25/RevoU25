import time
from time import gmtime, strftime

count = int (input("input angka : "))

print("counting start from " + str(count))

while(count < 500):
    count = count + 1
    print(count)
    # time.sleep(1)
    
print ("Start Execution : ",end="")
print (time.ctime())

print ("Seconds elapsed since the epoch are : ",end="")
print (time.time())

# Time Now
print ("Time calculated acc. to given seconds is : ")
print (time.gmtime())

# Format Time
s = strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
print(s)

# format time for Database
s1 = strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
print(s1)

print("count is out of range")

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")

print (numbers_to_strings(1))
 
#if __name__ == "__main__":
#    argument=0
#    print (numbers_to_strings(argument))

try:
    name = input("who is your name? ")
    age = int (input("what is your age? "))
except:
    print("the age is not number")