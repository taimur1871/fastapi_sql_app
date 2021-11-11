# python 3
# import modules
import plotly.express as px

def draw_map(df_map):
        # make map
        fig = px.scatter_mapbox(df_map, lat='Latitude', lon='Longitude',
                                size='Distance', color_discrete_sequence=['red'],
                                zoom=8)

        # show street map
        fig.update_layout(mapbox_style="open-street-map")

        # show geographical version
        #fig.update_layout(mapbox_style="carto-positron")
        #fig.update_layout(mapbox_style="carto-darkmatter")
        #fig.update_layout(mapbox_style="stamen-terrain")
        #fig.update_layout(mapbox_style="stamen-toner")
        #fig.update_layout(mapbox_style="stamen-watercolor")

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.show()

        with open('example_map.html', 'w') as f:
                f.write(fig.to_html(include_plotlyjs='cdn'))
