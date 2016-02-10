import pandas as pd
filenames = ["MERGED1996_PP.csv","MERGED1997_PP.csv","MERGED1998_PP.csv","MERGED1999_PP.csv","MERGED2000_PP.csv","MERGED2001_PP.csv","MERGED2002_PP.csv","MERGED2003_PP.csv","MERGED2004_PP.csv","MERGED2005_PP.csv","MERGED2006_PP.csv","MERGED2007_PP.csv","MERGED2008_PP.csv","MERGED2009_PP.csv","MERGED2010_PP.csv","MERGED2011_PP.csv","MERGED2012_PP.csv","MERGED2013_PP.csv"]

for ar in filenames :
	df = pd.read_csv('data/'+ar, header=0, low_memory=False)
	df2 = pd.read_csv('result/'+ar, header=0, low_memory=False)

	df2 = df2.ix[:len(df)-1]
	df2.to_csv('result2/'+ar, index = False)
