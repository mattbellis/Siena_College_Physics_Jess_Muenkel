#########################################################################
#This program counts the number of vowels in the English text file
#########################################################################

import matplotlib.pylab as plt 
import numpy

English=open("English Text.txt","r").read()		#Reads in the English Text
English.lower()
sentences = English.split('.')

file=open('englishfile.txt','w')

for s in sentences:
    output = ""

    s = s.strip(' ').replace(' ','')
    print s
    print len(s)
    if len(s)>0:
      

      number=s.count("a")/(len(s)*1.0)			#counts the number of A's
      output += "%f " % (number)
      print "The number of A's is "+str(number)
      
      number=s.count("e")/(len(s)*1.0)			#counts the number of E's
      output += "%f " % (number)
      print "The number of E's is "+str(number)
      number=s.count("i")/(len(s)*1.0)			#counts the number of I's
      output += "%f " % (number)
      print "The number of I's is "+str(number)
      number=s.count("o")/(len(s)*1.0)				#counts the number of O's
      output += "%f " % (number)
      print "The number of O's is "+str(number)
      number=s.count("u")/(len(s)*1.0)				#counts the number of U's
      output += "%f " % (number)
      print "The number of U's is "+str(number)

      output += "\n"
      file.write(output)

file.close()
