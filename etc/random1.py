from random import randint
afile = open("/Users/a0m0195/FinalModel/etc/Random.txt", "w" )

mylist = ["READY","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","ZERO","SUBCENTER","SUMMARY","REPEAT","HELLO","HI","NO","YES","START"]



for j in range (20):
	afile.write("<s> ")
	for i in range (8):
		lm = randint(0,18)
		afile.write(mylist[lm])
		afile.write(" ")
	afile.write("</s> (d"+str(j+1)+")\n")
afile.close()