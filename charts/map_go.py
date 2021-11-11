# python 3
# import modules
import plotly.graph_objects as go
import random_coord

df_map = random_coord.df

# make map
fig = go.Figure(go.Scattermapbox(lat=df_map['Latitude'], lon=df_map['Longitude'],
                                mode='markers',
                                marker=go.scattermapbox.Marker(size=14),
                                ))

# show street map
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox=dict(
        center=go.layout.mapbox.Center(
            lat=df_map['Latitude'].mean(),
            lon=df_map['Longitude'].mean()
            ),
        zoom=8,
        pitch=30,
        )
    )

# show geographical version
#fig.update_layout(mapbox_style="carto-positron")
#fig.update_layout(mapbox_style="carto-darkmatter")
#fig.update_layout(mapbox_style="stamen-terrain")
#fig.update_layout(mapbox_style="stamen-toner")
#fig.update_layout(mapbox_style="stamen-watercolor")

#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

#with open('example_map.html', 'w') as f:
#        f.write(fig.to_html(include_plotlyjs='cdn'))
