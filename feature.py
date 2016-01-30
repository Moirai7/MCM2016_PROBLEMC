import sys
import re
import ast
rt = re.compile('[a-zA-Z\s]')

uselessid = ["UNITID","OPEID","opeid6","INSTNM","CITY","STABBR","ZIP","AccredAgency","INSTURL","NPCURL","sch_deg","st_fips","RELAFFIL"]
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

	max = []
	min = []
	
	for ar in filenames :
		year = start_year+1
		filename = ar
		f = open("data/"+filename , 'rb')
		
		line = f.readline()
		line = line.strip().split(',')
		if check is False :
			for l in line:
				lists.append(0)
				lists_name.append(l)
				max.append(-999999999)
				min.append(999999999)
			check = True

		all_value = {}
		line = f.readline()
		while line:
			line = line.strip().split(',')
			for l in xrange(0,len(line)):
				if line[l].upper() == 'NULL' or line[l].upper() == 'PRIVACYSUPPRESSED':
					all_value[lists_name[l]] = 0.5
				elif lists_name[l] in uselessid:
					pass
				else:
					all_value[lists_name[l]] = line[l]#TODO
					try:
						temp = float(line[l]) if '.' in line[l] else int(line[l])
						if temp>max[l]:
							max[l] = temp
						if temp<min[l]:
							min[l] = temp
					except:
						import traceback
						traceback.print_exc() 
						print line[l]
						print lists_name[l]
			if school_id.has_key(line[0]) is False:
				school_id[line[0]] = {}
			school_id[str(line[0])][str(year)] = all_value
			length += 1
			line = f.readline()

			#print school_id
			#raw_input()
		f.close()
		print length

	for l in xrange(0,len(lists_name)):
		print lists_name[l] + '\t'+ str(max[l]) + '\t'+ str(min[l])
		pass
