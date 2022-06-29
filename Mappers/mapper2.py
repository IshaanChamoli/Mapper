# Creating a straight line from one point to another... not using the actual routes

import gmplot

lat = [28.5731, 28.4592 ]
lang = [77.1604, 77.0725]
gmapOne = gmplot.GoogleMapPlotter(lat[0], lang[0], 15)
gmapOne.scatter(lat, lang, "#ff000", size=50, marker = False)
gmapOne.plot(lat, lang, "blue", edge_width =2.5)
gmapOne.draw("map.html")
