# from random import randint
afile = open("/Users/a0m0195/FinalModel/etc/fileid.txt", "w" )


temp = 0
for i in range(50):
    temp += 1
    afile.write("m"+str(temp))
    afile.write("\n")
    # print(mylist[line])

afile.close()
