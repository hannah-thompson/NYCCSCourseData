import pandas

# reads the CSV file
df = pandas.read_csv('2016-2017-computer-science-report-1.csv')

# gets lat and long columns and converts to list
lats = df['latitude'].tolist()
longs = df['longitude'].tolist()

print(max(lats))
print(min(lats))
print(max(longs))
print(min(longs))

#lat range: 40.5232 to 40.8881
#long range: -73.4883 to -74.1975
#https://osm.org/go/Zct_sj
#tutorial: https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db