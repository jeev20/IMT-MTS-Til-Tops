import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import folium

df = pd.read_csv('TrondheimPeaks_Combined_years.csv', sep=',')

# Plotting using folium
IMT_til_topps = folium.Map(location = [63.4316705, 10.3960588], zoom_start = 10, tiles='OpenStreetMap')

# let us interate through the dataframe to capture all locations in a for loop
for column, row in df.iterrows():
   
    # We would also like to display some useful information as popup of the markers when clicked 
    
    if row['Visited'] == 'Yes':
        col = 'green'
    elif row['Visited'] == 'No':
        col = 'red'

    marker_information = "<h4>{} - IMT Topps {}</h4>  \n <h6>The elevation is <i>{} meters</i></h6> \n The terrain is {}. \n <h6>Peaked? : {}</h6>".format (row['Peak'], row['Year'], row['Elevation (m)'],row['Terrain Type'],row['Visited'] ) 

    
    # Label the marker
    folium.Marker([row['Latitude'], row['Longitude']], popup=marker_information, icon=folium.Icon(color=col)).add_to(IMT_til_topps)

# Now you can save this map as an html compatiple file
IMT_til_topps.save(outfile='PeaksVisitedbyme.html')


# Plotting using folium
IMT_til_topps = folium.Map(location = [63.4316705, 10.3960588], zoom_start = 9, tiles='OpenStreetMap')


feature_group1 = folium.FeatureGroup(name='2017')
feature_group2 = folium.FeatureGroup(name='2018')
feature_group3 = folium.FeatureGroup(name='2019')
feature_group4 = folium.FeatureGroup(name='2020')

# let us interate through the dataframe to capture all locations in a for loop
for column, row in df.iterrows():
   
    # We would also like to display some useful information as popup of the markers when clicked 

    marker_information = "<h4>{} - IMT Topps {}</h4>  \n <h6>Elevation: {} meters</h6> \n Terrain: {}".format (row['Peak'], row['Year'], row['Elevation (m)'],row['Terrain Type'] )
    marker_information_MTS = "<h4>{} - MTS Topps {}</h4>  \n <h6>Elevation: {} meters</h6> \n Terrain: {}".format (row['Peak'], row['Year'], row['Elevation (m)'],row['Terrain Type'] )
    if row['Year'] == 2017:
        col = 'blue' 
        x = folium.Marker([row['Latitude'], row['Longitude']], popup=marker_information, icon=folium.Icon(prefix='fa',icon='circle', color=col)).add_to(feature_group1)
    elif row['Year'] == 2018:
        col = 'darkpurple'
        x = folium.Marker([row['Latitude'], row['Longitude']], popup=marker_information, icon=folium.Icon(prefix='fa',icon='circle', color=col)).add_to(feature_group2)
    elif row['Year'] == 2019:
        col = 'darkblue'
        x = folium.Marker([row['Latitude'], row['Longitude']], popup=marker_information, icon=folium.Icon(prefix='fa', icon='circle', color=col)).add_to(feature_group3)
    elif row['Year'] == 2020:
        col = 'green'
        x = folium.Marker([row['Latitude'], row['Longitude']], popup=marker_information_MTS, icon=folium.Icon(prefix='fa', icon='circle', color=col)).add_to(feature_group4)


IMT_til_topps.add_child(feature_group1)
IMT_til_topps.add_child(feature_group2)
IMT_til_topps.add_child(feature_group3)
IMT_til_topps.add_child(feature_group4)


# turn on layer control
IMT_til_topps.add_child(folium.map.LayerControl())


# Now you can save this map as an html compatiple file
IMT_til_topps.save(outfile='index.html')
