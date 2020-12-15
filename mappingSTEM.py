import pandas
import matplotlib.pyplot as plt

# gather data from CSV
df = pandas.read_csv('2016-2017-computer-science-report-1.csv')

# get latitude + longitude + num of STEM classes info and make into lists
lats = df['latitude'].tolist()
longs = df['longitude'].tolist()
numofSTEM = df['# of Comp Sci Courses'].tolist()

# set map as background
map = plt.imread('mapNYC.png')

# set size of window
fig, ax = plt.subplots(figsize = (8,6))

# set title of window
fig.canvas.set_window_title('Distribution of K-12 Computer Science Courses in NYC')

# set x and y boundaries based on max and min lat and long
ax.imshow(map, extent=[-74.1975, -73.7132, 40.5232, 40.8881])

# make lists of sizes to show number diff by size
sizing = []
for i in range(0, len(numofSTEM)):
    # proportions to better demonstrate diff in num of CS classes
    sizing.append(((numofSTEM[i])+5)*7)

# create the scatter plot
scatter = ax.scatter(longs, lats, c=numofSTEM, s=sizing, alpha=0.6, label=numofSTEM)

# add a legend
legend1 = ax.legend(*scatter.legend_elements(), title="Number of STEM Classes")
ax.add_artist(legend1)

# set title, x axis label, y axis label
ax.set_title('Distribution of K-12 Computer Science Courses in NYC')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

#show plot
plt.show()
