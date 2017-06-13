from random import randint
afile1 = open("/Users/a0m0195/FinalModel/etc/Random.txt", "w" )
afile2 = open("/Users/a0m0195/FinalModel/etc/training.transcription", "w" )

mylist = ["READY","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","ZERO","SUBCENTER","SUMMARY","REPEAT","HELLO","HI","NO","YES","START"]



for j in range (50):
	afile1.write("<s> ")
	afile2.write("<s> ")
	for i in range (8):
		lm = randint(0,18)
		afile1.write(mylist[lm])
		afile2.write(mylist[lm])
		afile1.write(" ")
		afile2.write(" ")
	afile1.write("</s> (m"+str(j+1)+")\n\n")
	afile2.write("</s> (m"+str(j+1)+")\n")
afile1.close()
afile2.close()