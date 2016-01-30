import sys

filenames = ["MERGED1996_PP.csv","MERGED1997_PP.csv","MERGED1998_PP.csv","MERGED1999_PP.csv","MERGED2000_PP.csv","MERGED2001_PP.csv","MERGED2002_PP.csv","MERGED2003_PP.csv","MERGED2004_PP.csv","MERGED2005_PP.csv","MERGED2006_PP.csv","MERGED2007_PP.csv","MERGED2008_PP.csv","MERGED2009_PP.csv","MERGED2010_PP.csv","MERGED2011_PP.csv","MERGED2012_PP.csv","MERGED2013_PP.csv"]

if __name__ == '__main__':
	lists = []
	lists_name = []
	length = 0
	check = False
	start_year = 1995

	try:
		file_cost_value = sys.argv[1]
		f = open(file_cost_value,"rb")
		cost_value = f.readline()
		cost_value = line.strip().split(',')
	except:
		pass

	school_id = {}

	for ar in filenames :
		filename = ar
		f = open("data/"+filename , 'rb')
		
		line = f.readline()
		line = line.strip().split(',')
		if check is False :
			for l in line:
				lists.append(0)
				lists_name.append(l)
			print len(line)
			check = True
			school_id[line[0]] = []#TODO
		else:
			if line[0] not in school_id:
				school_id[line[0]] = []#TODO
		#	for l in xrange(0,len(line)):
		#		if lists_name[l] != line[l]:
		#			quit(0)
		
		line = f.readline()
		while line:
			line = line.strip().split(',')
			#print str(len(line))
			for l in xrange(0,len(line)):
				if line[l].upper() == 'NULL':
					lists[l] += 1 
			length += 1
			#print length
			line = f.readline()
		print length
		f.close()

		year = start_year+1
		yearinfo = {}
		
	length2 = 0 
	for l in xrange(0,len(lists)):
		#print lists_name[l] + '\t'+ str(lists[l])
		if lists[l] == length:
			length2 += 1
			print lists_name[l] + '\t' + str(lists[l]) + '\t' + str(length)
			pass
		pass
	print length2
