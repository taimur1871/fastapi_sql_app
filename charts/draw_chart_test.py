import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# get data for the charts
#df_map = random_coord.df[['Well', 'Latitude', 'Longitude', 'Distance']]
#df = pd.read_csv('/home/taimur/Pictures/App Deployment/temp_working_dir/data/A2658')

# draw charts
def draw_chart(df):
    '''
    fig1 = px.scatter(df, x='adj_x', y='adj_y', color='wear', 
                    color_discrete_map={'lvl_1': 'green','lvl_2':'olive', 'lvl_3': 'gold','lvl_4': 'red',}, 
                    hover_name='name', size=len(df)*[4])
    '''
    fig1 = px.scatter(df, x='adj_x', y='adj_y', color='wear', 
                    color_discrete_map={'lvl_1': 'green','lvl_2':'olive', 'lvl_3': 'gold','lvl_4': 'red',}, 
                    hover_name='cut_loc', size=len(df)*[4])

    #fig1.update_xaxes(title_text='bit_len', showticklabels=False)
    #fig1.update_yaxes(title_text='bit_ht', showticklabels=False)

    fig1.show()
