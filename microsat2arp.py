#! /usr/bin/env python
#This program reads a file exported by the acessory program microsat, part of the ms package,
#and exports in .arp format (Arlequin) for two populations.
#Usage example: ./ms 1 1 -t 1 ./microsat -a 50 -i | python microsat2arp.py 1 1 > output.arp. 
#Enter the number of populations and the population sizes after calling the script

#It is necessary to use the option -i in the microsat software.
#The maximum number of accepted populations is 10.

import re
import sys

data = sys.stdin.readlines()#Attribute the values in the lines to a variable named data
arg = map(int, sys.argv[1:])

#Inform population sizes, that will be multiplied by 2, to account for both alleles
PopNumber=arg[0]
PopList = []*PopNumber
PopList = arg[1:]
PopList = [i/2 for i in PopList]
PopSum = sum(PopList)
#Initialize two independent counters for line numbers. One counter must be initialized per population
LineNumber = 1

#Print the header of the Arlequin file, using the sample size in Pop1
print """[Profile]
     Title="P.aurisetus group SSR"
     NbSamples=%d
     GenotypicData=1
     GameticPhase=0
     RecessiveData=0
     DataType=MICROSAT
     LocusSeparator=WHITESPACE
     MissingData='?'
     CompDistMatrix=1
[Data]
  [[Samples]]
    SampleName = "Pop1" 
    SampleSize = %d
    SampleData = {""" % (PopNumber, PopList[0])
while LineNumber <= PopList[0]:
    for Line in data:
        if LineNumber <= PopList[0]*2:#Uses each line of the microsat output and converts to the arlequin format. Must be multiplied by 2 to account for both alleles.
            if LineNumber%2 != 0:
               print re.sub(r'(\d+)\n',r'      Pop1  1  \1',Line)
            else:
               print re.sub(r'(\d+)\n',r'               \1',Line)
        LineNumber += 1
if PopNumber == 1:
	print"""    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
    }"""
else:
	print """    }
    
    SampleName = "Pop2" 
    SampleSize = %d
    SampleData = {""" % (PopList[1])

	LineNumber = 1
	for Line in data:
		if PopList[0]*2 < LineNumber <= (PopList[0]+PopList[1])*2: 
			if LineNumber%2 != 0:
				print re.sub(r'(\d+)\n',r'      Pop2  1  \1',Line)
			else:
				print re.sub(r'(\d+)\n',r'               \1',Line)
		LineNumber += 1
	if PopNumber == 2:
		print"""    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
          "Pop2"
    }"""
	else:
		print """    }
    
    SampleName = "Pop3" 
    SampleSize = %d
    SampleData = {""" % (PopList[2])

		LineNumber = 1
		for Line in data:
			if (PopList[0]+PopList[1])*2 < LineNumber <= (PopList[0]+PopList[1]+PopList[2])*2: 
				if LineNumber%2 != 0:
					print re.sub(r'(\d+)\n',r'      Pop3  1  \1',Line)
				else:
					print re.sub(r'(\d+)\n',r'               \1',Line)
			LineNumber += 1

		if PopNumber == 3:
			print """    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
          "Pop2"
          "Pop3"
    }"""
		else:
			print """    }
    
    SampleName = "Pop4" 
    SampleSize = %d
    SampleData = {""" % (PopList[3])

			LineNumber = 1
			for Line in data:
				if (PopList[0]+PopList[1]+PopList[2])*2 < LineNumber <= (PopList[0]+PopList[1]+PopList[2]+PopList[3])*2: 
					if LineNumber%2 != 0:
						print re.sub(r'(\d+)\n',r'      Pop4  1  \1',Line)
					else:
						print re.sub(r'(\d+)\n',r'               \1',Line)
				LineNumber += 1

			if PopNumber == 4:
				print """    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
          "Pop2"
          "Pop3"
          "Pop4"
    }"""

			else:
				print """    }
    
    SampleName = "Pop5" 
    SampleSize = %d
    SampleData = {""" % (PopList[4])

				LineNumber = 1
				for Line in data:
					if (PopList[0]+PopList[1]+PopList[2]+PopList[3])*2 < LineNumber <= (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4])*2: 
						if LineNumber%2 != 0:
							print re.sub(r'(\d+)\n',r'      Pop5  1  \1',Line)
						else:
							print re.sub(r'(\d+)\n',r'               \1',Line)
					LineNumber += 1

				if PopNumber == 5:
					print """    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
          "Pop2"
          "Pop3"
          "Pop4"
          "Pop5"
    }"""
				else:
					print """    }
    
    SampleName = "Pop6" 
    SampleSize = %d
    SampleData = {""" % (PopList[5])

					LineNumber = 1
					for Line in data:
						if (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4])*2 < LineNumber <= (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4]+PopList[5])*2: 
							if LineNumber%2 != 0:
								print re.sub(r'(\d+)\n',r'      Pop6  1  \1',Line)
							else:
								print re.sub(r'(\d+)\n',r'               \1',Line)
						LineNumber += 1

					if PopNumber == 6:
						print """    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
          "Pop2"
          "Pop3"
          "Pop4"
          "Pop5"
          "Pop6"
    }"""

					else:
						print """    }
    
    SampleName = "Pop7" 
    SampleSize = %d
    SampleData = {""" % (PopList[6])

						LineNumber = 1
						for Line in data:
							if (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4]+PopList[5])*2 < LineNumber <= (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4]+PopList[5]+PopList[6])*2: 
								if LineNumber%2 != 0:
									print re.sub(r'(\d+)\n',r'      Pop7  1  \1',Line)
								else:
									print re.sub(r'(\d+)\n',r'               \1',Line)
							LineNumber += 1

						if PopNumber == 7:
							print """    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
          "Pop2"
          "Pop3"
          "Pop4"
          "Pop5"
          "Pop6"
          "Pop7"
    }"""

						else:
							print """    }
    
    SampleName = "Pop8" 
    SampleSize = %d
    SampleData = {""" % (PopList[7])

							LineNumber = 1
							for Line in data:
								if (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4]+PopList[5]+PopList[6])*2 < LineNumber <= (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4]+PopList[5]+PopList[6]+PopList[7])*2: 
									if LineNumber%2 != 0:
										print re.sub(r'(\d+)\n',r'      Pop8  1  \1',Line)
									else:
										print re.sub(r'(\d+)\n',r'               \1',Line)
								LineNumber += 1

							if PopNumber == 8:
								print """    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
          "Pop2"
          "Pop3"
          "Pop4"
          "Pop5"
          "Pop6"
          "Pop7"
          "Pop8"
    }"""

							else:
								print """    }
    
    SampleName = "Pop9" 
    SampleSize = %d
    SampleData = {""" % (PopList[8])

								LineNumber = 1
								for Line in data:
									if (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4]+PopList[5]+PopList[6]+PopList[7])*2 < LineNumber <= (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4]+PopList[5]+PopList[6]+PopList[7]+PopList[8])*2: 
										if LineNumber%2 != 0:
											print re.sub(r'(\d+)\n',r'      Pop9  1  \1',Line)
										else:
											print re.sub(r'(\d+)\n',r'               \1',Line)
									LineNumber += 1

								if PopNumber == 9:
									print """    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
          "Pop2"
          "Pop3"
          "Pop4"
          "Pop5"
          "Pop6"
          "Pop7"
          "Pop8"
          "Pop9"
    }"""

								else:
									print """    }
    
    SampleName = "Pop10" 
    SampleSize = %d
    SampleData = {""" % (PopList[9])

									LineNumber = 1
									for Line in data:
										if (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4]+PopList[5]+PopList[6]+PopList[7]+PopList[8])*2 < LineNumber <= (PopList[0]+PopList[1]+PopList[2]+PopList[3]+PopList[4]+PopList[5]+PopList[6]+PopList[7]+PopList[8]+PopList[9])*2: 
											if LineNumber%2 != 0:
												print re.sub(r'(\d+)\n',r'      Pop10  1  \1',Line)
											else:
												print re.sub(r'(\d+)\n',r'               \1',Line)
										LineNumber += 1

									if PopNumber == 10:
										print """    }

[[Structure]]
    StructureName="P.aurisetus group SSR Structure"
    NbGroups=1
    IndividualLevel=0
    Group = {
          "Pop1"
          "Pop2"
          "Pop3"
          "Pop4"
          "Pop5"
          "Pop6"
          "Pop7"
          "Pop8"
          "Pop9"
          "Pop10"
    }"""
									if PopNumber > 10:
										print "Maximum number of populations supported is 10."
