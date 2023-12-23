#For the Plotting of the graph I used chat gbt, where I used the
#context 'I have a png of britian and a csv file with lattitudes and longitudes for cooordinates for circles to put on
#my png. How could i pull this off on python' It advised to use the packages below

import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Load CSV file using the pandas package
grow_locations = pd.read_csv(r"C:\Users\angus\Programmes\PythonAssighnment2\data\GrowLocations.csv")
britain_map= Image.open(r'C:\Users\angus\Programmes\PythonAssighnment2\map\map7.png')

#Looking at our csv file we note that lattitude and longitude have the wrong column ID's
#we can correct this with
grow_locations = grow_locations.rename(columns={'Latitude':'Longitude', 'Longitude':'Latitude'})

#Now I can edit our Latitude and longitude values and check that each one
#is within our bounding box!
grow_locations = grow_locations[
    #Make sure the Longitude is greater than the minimum Longitude
    (grow_locations['Longitude'] >= -10.592)&
    #Logitue less than max Longitude
    (grow_locations['Longitude'] <= 1.6848)&
    #same as above but for Latitude
    (grow_locations['Latitude'] >= 50.681)&
    (grow_locations['Latitude'] <= 57.985)
]



# Plot circles on the map
plt.scatter(grow_locations['Longitude'], grow_locations['Latitude'], s=50, c='red', alpha=0.7)

# Set the bounding box for the map
bbox = [-10.592, 1.6848, 50.681, 57.985]

# Display the map with circles and bounding box
plt.imshow(britain_map, extent=bbox)

# Save the resulting image
plt.savefig('output_image.png', bbox_inches='tight', pad_inches=0.1)
plt.show()