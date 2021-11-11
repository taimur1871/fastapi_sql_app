import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

# get data for the charts
#df_map = random_coord.df[['Well', 'Latitude', 'Longitude', 'Distance']]
#df = pd.read_csv('/home/taimur/Pictures/App Deployment/temp_working_dir/A2658')


def draw_chart(df, df_map):
    center_lat = df_map['Latitude'].mean()
    center_long = df_map['Longitude'].mean()

    # draw charts
    fig = make_subplots(rows = 2, cols = 2,
                        specs=[[{"type": "xy"}, {"type": "domain"}],
                            [{"type": "scattergeo"}, {"type": "domain"}]],
                        )

    fig.add_trace(go.Scatter(x = df['adj_x'], y = df['adj_y'],
                            mode='markers'), row=1, col=1)

    fig.add_trace(go.Scattergeo(lat=df_map.Latitude, lon=df_map.Longitude,
                                text=df_map['Distance'],
                                mode='markers'), row=2, col=1)

    fig.add_trace(go.Pie(labels = df.wear.value_counts().index,
                        values = df['wear'].value_counts().values),
                row=1, col=2)

    fig.add_trace(go.Pie(labels = df['wear_type'].value_counts().index,
                        values = df['wear_type'].value_counts().values),
                    row=2, col=2)

    fig.update_geos(
        landcolor='lightgreen',
        oceancolor='MidnightBlue',
        showocean=True,
        lakecolor='LightBlue',
        scope='usa',
        projection_scale=5,
        center={'lat':center_lat, 'lon':center_long},
        subunitcolor='black',
        )

    fig.show()
