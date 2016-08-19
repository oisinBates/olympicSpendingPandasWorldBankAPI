import pandas as pd
import numpy as np
from pandas_datareader import wb
from bokeh.charts import Bar, output_file, show

#suppress scientific notation 
# *loses precision with large numbers https://github.com/pydata/pandas/issues/2697
#pd.set_option('display.float_format', lambda x: '%.3f' % x) 

#Search World Bank API
wb.search('GDP.*Military expenditure.*Health expenditure.*Government expenditure on Education')
#inicators for retrieving data (GDP, Military, Education)
indicators=['NY.GDP.MKTP.CD','MS.MIL.XPND.GD.ZS','SE.XPD.TOTL.GD.ZS']

Canada1988 = dat = wb.download(indicator=indicators,country=['CA'], start=1988, end=1988) 
France1992 = dat = wb.download(indicator=indicators,country=['FR'], start=1992, end=1992) 
Spain1992 = dat = wb.download(indicator=indicators,country=['ES'], start=1992, end=1992) 
Norway1994 = dat = wb.download(indicator=indicators,country=['NO'], start=1994, end=1994) 
US1996 = dat = wb.download(indicator=indicators,country=['US'], start=1996, end=1996) #no Education figure
Japan1998 = dat = wb.download(indicator=indicators,country=['JP'], start=1998, end=1998)
Sydney2000 = dat = wb.download(indicator=indicators,country=['AU'], start=2000, end=2000)
US2002 = dat = wb.download(indicator=indicators,country=['US'], start=2002, end=2002)
Greece2004 = dat = wb.download(indicator=indicators,country=['GR'], start=2004, end=2004)
Italy2006 = dat = wb.download(indicator=indicators,country=['IT'], start=2006, end=2006)
China2008 = dat = wb.download(indicator=indicators,country=['CN'], start=2008, end=2008) #no Education figure
Canada2010 = dat = wb.download(indicator=indicators,country=['CA'], start=2010, end=2010)
GB2012 = dat = wb.download(indicator=indicators,country=['GB'], start=2012, end=2012) #no Education figure
Russia2014 = dat = wb.download(indicator=indicators,country=['RU'], start=2014, end=2014) #no Education figure
Brazil2016 = dat = wb.download(indicator=indicators,country=['BR'], start=2015, end=2015) #no Education figure

#Get Education spending for countries who didn't hold figures for their olympic years
US1995Education = dat = wb.download(indicator='SE.XPD.TOTL.GD.ZS',country=['US'], start=1995, end=1995) 
US1996.iloc[0,2] = US1995Education.iloc[0,0]
China1999Education = dat = wb.download(indicator='SE.XPD.TOTL.GD.ZS',country=['CN'], start=1999, end=1999)
China2008.iloc[0,2] = China1999Education.iloc[0,0]
GB2011Education = dat = wb.download(indicator='SE.XPD.TOTL.GD.ZS',country=['GB'], start=2011, end=2011)
GB2012.iloc[0,2] = GB2011Education.iloc[0,0]
Russia2012Education = dat = wb.download(indicator='SE.XPD.TOTL.GD.ZS',country=['RU'], start=2012, end=2012) 
Russia2014.iloc[0,2] = Russia2012Education.iloc[0,0]
Brazil2012Education = dat = wb.download(indicator='SE.XPD.TOTL.GD.ZS',country=['BR'], start=2012, end=2012)
Brazil2016.iloc[0,2] = Brazil2012Education.iloc[0,0]

#Change Brazil's multiindex 'year' value from 2015 to 2016
index = Brazil2016.index
names = index.names
index = [('Brazil','2016')] 
Brazil2016.index = pd.MultiIndex.from_tuples(index, names = names)

#Concatenate all data frames to a single one
frames = [Canada1988, France1992, Spain1992, Norway1994, US1996, Japan1998, Sydney2000, US2002, 
Greece2004, Italy2006, China2008, Canada2010, GB2012, Russia2014, Brazil2016]
olympicSpending = pd.concat(frames)

#create dataframe with oxford figures and concatenate with world bank
#Figures taken from this paper: http://ssrn.com/abstract=2804554
oxfordOlympicSpending = pd.DataFrame({ 'Type' : pd.Series(['Winter','Winter','Summer','Winter','Summer','Winter','Summer','Winter','Summer','Winter','Summer','Winter','Summer','Winter','Summer'], index=olympicSpending.index), 
					'Olympic overspend %' : pd.Series([65,137,266,277,151,56,90,24,49,80,2,13,76,289,51], index=olympicSpending.index),
					'Olympic cost($Billion)' : pd.Series([1.109,1.997,9.687,2.228,4.143,2.227,5.026,2.520,2.942,4.366,6.810,2.540,14.957,21.890,4.557], index=olympicSpending.index)
				})	

#Concatenate figures from Oxford and the World Bank
olympicSpending = pd.concat([oxfordOlympicSpending, olympicSpending], axis=1, join_axes=[oxfordOlympicSpending.index])

#rename columns
olympicSpending.rename(columns={'NY.GDP.MKTP.CD':'GDP','MS.MIL.XPND.GD.ZS':'Military', 'SE.XPD.TOTL.GD.ZS':'Education'}, inplace=True)
olympicSpending['Military'] = ((olympicSpending['GDP']/100)* olympicSpending['Military'])
olympicSpending['Education'] = ((olympicSpending['GDP']/100)* olympicSpending['Education'])


#save to CSV format
print olympicSpending

olympicSpending.to_csv('olympicSpending.csv')
