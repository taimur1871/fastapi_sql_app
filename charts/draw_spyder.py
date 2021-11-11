import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# get data for the charts
df = pd.read_csv('/home/taimur/Pictures/App Deployment/temp_working_dir/data/spyder.csv')

# draw charts
def draw_chart(df):
    
    categories = df.columns.to_list()
    
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
          r=df.iloc[0],
          theta=categories,
          fill='toself',
          name='Product A'
    ))
    fig.add_trace(go.Scatterpolar(
          r=df.iloc[1],
          theta=categories,
          fill='toself',
          name='Product B'
    ))
    fig.add_trace(go.Scatterpolar(
          r=df.iloc[2],
          theta=categories,
          fill='toself',
          name='Product B'
    ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          #range=[df.I, 5]
        )),
      showlegend=False
    )

    #fig1.update_xaxes(title_text='bit_len', showticklabels=False)
    #fig1.update_yaxes(title_text='bit_ht', showticklabels=False)

    fig.show()

draw_chart(df)
