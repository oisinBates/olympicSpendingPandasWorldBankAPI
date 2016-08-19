import pandas as pd
import numpy as np
from bokeh.models import FixedTicker, NumeralTickFormatter
from bokeh.layouts import gridplot
from bokeh.charts import Line, show, output_file

#read in data frame  
olympicSpending = pd.read_csv('olympicSpending.csv')
#dictionary of data, formatted for creating charts
olympicHostsData = dict(olympicCost=olympicSpending.iloc[:,2].values,
			olympicOverspend=olympicSpending.iloc[:,3].values,
			gdp=olympicSpending.iloc[:,5].values,
			militarySpending=olympicSpending.iloc[:,6].values,
			educationSpending=olympicSpending.iloc[:,7].values,
			graphIndex=range(1,16),# ie: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            )

#array for inserting country names
chartIndexText= ['CA\'88', 'FR\'92', 'ES\'92', 'NO\'94','US\'96', 'JP\'98', 'AU\'00', 'US\'02', 
'GR\'04', 'IT\'06', 'CN\'08', 'CA\'10', 'GB\'12', 'RU\'14','BR\'16']

chartTicks=range(0,15)

#create line charts
olympicCostChart = Line(olympicHostsData, y=['olympicCost'],
            dash=['olympicCost'],
            color=['olympicCost'],
            legend_sort_field = 'color',
            legend_sort_direction = 'ascending',
            title="Cost of Olympics",xlabel='Host Countries', ylabel='Constant 2015 US($Billions)', legend=True)
#Specify ticks to be shown on all x-axis indexes 
olympicCostChart.xaxis[0].ticker=FixedTicker(ticks=chartTicks)
#Add list of host countries over x-axis 
olympicCostChart.text(range(0,15), np.full(15,0), text=chartIndexText, angle=45, text_font_style='normal', text_alpha=.5,text_font_size="12pt", text_align='center')
#Convert from scientific notation to dollars
olympicCostChart.yaxis[0].formatter = NumeralTickFormatter(format="$ 0,000")

olympicOverspendChart = Line(olympicHostsData, y=['olympicOverspend'],
            dash=['olympicOverspend'],
            color=['olympicOverspend'],
            legend_sort_field = 'color',
            legend_sort_direction = 'ascending',
            title="Overspending by Olympic hosts",xlabel='Host Countries', ylabel='percentage overspend', legend=True)
olympicOverspendChart.xaxis[0].ticker=FixedTicker(ticks=chartTicks)
olympicOverspendChart.text(range(0,15), np.full(15,0), text=chartIndexText, angle=45, text_font_style='normal', text_alpha=.5,text_font_size="12pt", text_align='center')

gdpChart = Line(olympicHostsData, y=['gdp'],
            dash=['gdp'],
            color=['gdp'],
            legend_sort_field = 'color',
            legend_sort_direction = 'ascending',
            title="Host country GDP in Olympic years(World Bank)",xlabel='Host Countries', ylabel='Current US$', legend=True)
gdpChart.xaxis[0].ticker=FixedTicker(ticks=chartTicks)
gdpChart.text(range(0,15), np.full(15,0), text=chartIndexText, angle=45, text_font_style='normal', text_alpha=.5,text_font_size="12pt", text_align='center')
gdpChart.yaxis[0].formatter = NumeralTickFormatter(format="$ 0,000")

educationANDmilitaryBudgetChart = Line(olympicHostsData, y=['militarySpending','educationSpending'],
            dash=['militarySpending','educationSpending'],
            color=['militarySpending','educationSpending'],
            legend_sort_field = 'color',
            legend_sort_direction = 'ascending',
            title="Education and military spending in Olympic years(WorldBank)",xlabel='Host Countries', ylabel='Current US$', legend=True)
educationANDmilitaryBudgetChart.xaxis[0].ticker=FixedTicker(ticks=chartTicks)
educationANDmilitaryBudgetChart.text(range(0,15), np.full(15,0), text=chartIndexText, angle=45, text_font_style='normal', text_alpha=.5,text_font_size="12pt", text_align='center')
educationANDmilitaryBudgetChart.yaxis[0].formatter = NumeralTickFormatter(format="$ 0,000")

#Save and display the charts
output_file("olympicspending.html", title="Bokeh line charts on the finances of Olympic host countries")
show(gridplot(gdpChart, educationANDmilitaryBudgetChart, olympicOverspendChart, olympicCostChart, ncols=2))