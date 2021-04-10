import sys
print("======FileErrorVirus======")
#stop = input("Write stop to stop")
names = ["File1","File2","File3","File4","File5"]
howmuch = "6"
namesmore = "File"
crash = True
write = ""
while crash == True:
    result = howmuch + namesmore
    names.append(result)
    howmuch += "1"
    while len(write) < 30:
        write +="_First Virus_"
    if len(names) > 3:
        crash = False
print(names)  
