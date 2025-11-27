# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

print("\n\n\nItaly is a country in Europe with a population of almost 60 million people, a quarter of whom are between the ages of 45 and 48.\n")
print("In Italy the pay gap between men and women is 5 percent, well below the general European avarage\n")
print("employed women in Italy represent 42% of the workforce, therefore in a minority compared to men and far from the 81% in Sweden. It represents the last place in the European ranking. If we look at the activity rate, the gap grows further where the male rate reaches 75\n")

input("Press return to continue.\n")

print("While exploring the Women's Well-being dataset, I found that the gender of the Well-being providers is almost always male")


print("\n\nBased on these findings, my proposed research question is:\n")
print("What is the gender gap in the Well-being dataset?\n")
countryMatchBooleanList = (lwd["country_name"]=="Italy" )
cd=lwd.loc[countryMatchBooleanList]

# create a scatter plot
plt.scatter(lwd["DP_earn_more_p"],lwd["DP_earn_more_equal_p"])

plt.legend(loc='upper right')
plt.title("Number of Well-being providers in Italy")
plt.xlabel("Women earning more or equal than her partner")
plt.ylabel("Year")

plt. ylim(0,20)

plt.show()
