
#step1
f = open("pythonessay.txt", "r")

#step2
print(f.read())

#step3
print(f.readline())

#step4
f = open("pythonessay.txt", "r")
for x in f:
    print(x)

#step 5
import os
if os.path.exists("pythonessay.txt"):
    os.remove("pythonessay.txt")
else:
    print("The file does not exist")
