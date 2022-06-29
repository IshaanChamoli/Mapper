import gmplot
apikey = '' # (your API key here)
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13)

gmap.directions(
    (37.799001, -122.442692),
    (37.832183, -122.477914),
    waypoints=[
        (37.801036, -122.434586),
        (37.805461, -122.437262)
    ]
)

gmap.draw('map.html')
