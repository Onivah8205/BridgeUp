import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.clf()

earthquakedata = open('currentQuakes.txt')

ColumnNames = earthquakedata.readline()

#creating empty lists
lat = []
longitude = []

#setting picture as a variable
image = mpimg.imread ("mapp.jpg")

for line in earthquakedata:
    #line.split turns each row into a list of individual strings
    line = line.split(',')
    lat.append(float(line[1])) #turns 2nd item in list into a float
    longitude.append(float(line[2])) #turns 3rd item in list into a float

#create scatter plot
plt.scatter(longitude, lat)

#puts image behind scatter plot; extent defines where the image should be
plt.imshow(image, extent=[-197,196,87,-63])

#plotting x and y labels
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show() #creates graph
