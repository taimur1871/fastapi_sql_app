from os import name
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

def draw_chart(df):

    # update labels for wear chart
    df_wear = df.wear.value_counts()
    df_wear.rename(index={'lvl_1':'light', 'lvl_2':'moderate', 'lvl_3':'severe', 'lvl_4':'extreme'},
                    inplace=True)

    # set colors for pie chart
    #colors = ['green', 'blue', 'orange','red']

    # draw charts
    #fig = go.Figure(go.Bar(x = df[['cut_loc','wear_num']].groupby(df['cut_loc']).mean().index,
    #                y = df[['cut_loc','wear_num']].groupby(df['cut_loc']).mean().values.ravel()))
    '''
    fig1 = px.pie(df_wear, values = df_wear.values, names=df_wear.index, color=df_wear.index,
                color_discrete_map={'light':'green', 'moderate':'lightgreen',
                                    'severe':'gold', 'extreme':'red'})
    '''
    fig2 = px.pie(df, values = df['wear_type'].value_counts().values,
                names=df['wear_type'].value_counts().index,
                color=df['wear_type'].value_counts().index,
                color_discrete_map={'no':'green', 'worn':'blue',
                                    'chipped':'gold', 'broken':'red'})

    #fig.show()
    #fig1.show()
    fig2.show()
    '''
    # save charts
    with open('./html/bar_loc.html', 'w') as f:
                f.write(fig.to_html(include_plotlyjs='cdn'))
        
    with open('./html/wear.html', 'w') as f:
                f.write(fig1.to_html(include_plotlyjs='cdn'))

    with open('./html/wear_type.html', 'w') as f:
                f.write(fig2.to_html(include_plotlyjs='cdn'))
    '''