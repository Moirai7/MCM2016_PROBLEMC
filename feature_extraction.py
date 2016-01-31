import sys
import cPickle as pickle
#import plotly.plotly as py
#import plotly.graph_objs as go

x=['1996-11-04 22:23:00', '1997-11-04 22:23:00', '1998-11-04 22:23:00', '1999-11-04 22:23:00', '2000-11-04 22:23:00', '2001-11-04 22:23:00', '2002-11-04 22:23:00', '2003-11-04 22:23:00', '2004-11-04 22:23:00', '2005-11-04 22:23:00', '2006-11-04 22:23:00', '2007-11-04 22:23:00', '2008-11-04 22:23:00', '2009-11-04 22:23:00', '2010-11-04 22:23:00', '2011-11-04 22:23:00', '2012-11-04 22:23:00', '2013-11-04 22:23:00']

uselessid = ["UNITID","OPEID","opeid6","INSTNM","CITY","STABBR","ZIP","AccredAgency","INSTURL","NPCURL","sch_deg","st_fips","RELAFFIL"]
filenames = ["MERGED1996_PP.csv","MERGED1997_PP.csv","MERGED1998_PP.csv","MERGED1999_PP.csv","MERGED2000_PP.csv","MERGED2001_PP.csv","MERGED2002_PP.csv","MERGED2003_PP.csv","MERGED2004_PP.csv","MERGED2005_PP.csv","MERGED2006_PP.csv","MERGED2007_PP.csv","MERGED2008_PP.csv","MERGED2009_PP.csv","MERGED2010_PP.csv","MERGED2011_PP.csv","MERGED2012_PP.csv","MERGED2013_PP.csv"]

if __name__ == '__main__':
	check = True
	max = []
	min = []
	max_min = False
	
	try:
		max_min = 'feature_max_min'
		f = open(max_min,"rb")
		max = f.readline()
		max = line.strip().split(',')
		min = f.readline()
		min = line.strip().split(',')
		f.close()
	except:
		max_min = False
		max = [-999999999 for n in range(1400)]
		min = [999999999 for n in range(1400)]
		pass

	start_year = 1995
	school_info = False
	try:
		schood_info = sys.argv[1]
		school_id = pickle.load(open(school_info, 'rb'))
	except:
		school_id = {}
		pass

	lists_name = []
	if school_info is False:
		for ar in filenames :
			year = start_year+1
			f = open("data2/save_simplfy/"+ar , 'rb')
			line = f.readline()
			if check :
				line = line.strip().split(',')
				for l in line:
					lists_name.append(l)
				check = False
			line = f.readline()
			while line:
				line = line.strip().split(',')
				all_value = []
				list_index = 0
				for l in xrange(0,len(lists_name)):
					if lists_name[l] not in uselessid:
						if line[l].upper() == 'NULL' or line[l].upper() == 'PRIVACYSUPPRESSED':
							if max_min is False :
								pass
							else:
								all_value.append((max[list_index]+min[list_index])/2)
							continue
						temp = float(line[l]) if '.' in line[l] else int(line[l])
						if max_min is False :
							if temp>max[list_index]:
								max[list_index] = temp
							else:
								min[list_index] = temp
						else:
							all_value.append((temp-min[list_index])/(max[list_index]-min[list_index]))
						list_index += 1
				if max_min is not False :
					if school_id.has_key(line[0]) is False:
						school_id[line[0]] = []
					school_id[str(line[0])].append(all_value)
				line = f.readline()
			f.close()
			pickle.dump(school_id,open('result/school_info', 'wb'))
	
	if max_min is False :
		print(max)
		print(min)
	else:
		#just use one school_id
		choose_id = ''#TODO
		years = school_id[choose_id]
		list = []
		data = []
		for value in xrange(0,len(years[0])):
			for year in xrange(0,len(years)):
				list.append(years[year][value])
		#	data.append([
		#		go.Scatter(
		#			x=x,
		#			y=list,
		#			name=value
		#		)
		#	])
		#layout = go.Layout(xaxis=dict(title='Years'),yaxis=dict(title='Param'))
		#fig = go.Figure(data=data, layout=layout)
		#plot_url = py.plot(fig, filename='latex')
		pass