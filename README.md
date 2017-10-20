# Collating and graphing Olympic data with Pandas and Bokeh


I recently came across a [study from the University of Oxford](http://ssrn.com/abstract=2804554) on the costs incured by Olympic host nations. 
As I had been recently looking at the APIs available with the [Pandas](http://pandas.pydata.org/) library, I decided to concantenate some data from the World Bank, alongside the findings of the aforementioned Oxford study.

From the World Bank, I chose some of the most obvious representations of each country's wealth and spending: GDP, and military and education spending. There were many other possible metrics, but it transpired that most were not consistently available in the same years. As of such, I decided to decrease the scale of the data I wished to represent.

Even so, it was necessary to pull some educational data from the nearest available year. The following substitutions were made for countries with no data for their Olympic years: 

* US 1996 : 1995 Education
* China 2008 : 1999 Education
* GB 2012 : 2011 Education
* Russia 2014 : 2012 Education
* Brazil 2016 : 2012 Education

The World Bank's GDP figures were not available in constant 2015 US dollars, so current rates were used. In contrast, the Oxford study's figures were at the 2015 rate. Finally, as Brazil was hosting in the current year, its 2015 GDP and military spending was used, but recorded in the data frame alongside the projected 2016 data for the Rio Olympics.



The graph, created with [Bokeh](http://bokeh.pydata.org/), can be viewed at [oisinbates.com/assets/olympicspending](http://oisinbates.com/assets/olympicspending.html)
