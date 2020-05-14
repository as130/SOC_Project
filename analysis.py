
import sqlite3
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
TOTAL=200

conn = sqlite3.connect('security.db')
c = conn.cursor()


query = "SELECT Year FROM articles;"

c.execute(query)
conn.commit()

years_arr = []
year_counts_arr = [0]


curr_year = '2008'
curr_pos = 0
# Adjunct, Argument, Imperative, Binding, Question, Auxiliary
for row in c :
    year = row[0]
    if year != curr_year :
        curr_year = year
        curr_pos += 1
        year_counts_arr.append(1)
    else :
        year_counts_arr[curr_pos] = year_counts_arr[curr_pos] + 1
    if (year not in years_arr) :
        years_arr.append(year)

print(years_arr)
print(year_counts_arr)

years_arr = years_arr[: len(years_arr) - 2] 
year_counts_arr = year_counts_arr[: len(year_counts_arr) - 2] 


y_pos = np.arange(len(years_arr))

plt.bar(y_pos, year_counts_arr, align='center', alpha=0.5)
plt.xticks(y_pos, years_arr)
plt.ylabel('Number of Publicly-Available Articles Related to Malicious Activity')
plt.xlabel('Year')
plt.title('Figure 1 \n Relationship Between Year and Number of Publicly-Available Articles \n Related to Cybercrime')
plt.annotate('Note: Outliers were removed from \nthis set due to a lack of data', (0,0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
plt.show()
