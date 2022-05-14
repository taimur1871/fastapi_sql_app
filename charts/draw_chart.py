import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


def draw_chart(df):
    df = df[df['cut_loc'] != 'gauge']
    # draw charts
    fig = make_subplots(rows=2, cols=2,
                        specs=[[{"type": "domain"}, {"type": "domain"}],
                               [{"type": "bar"}, {"type": "domain"}]],
                        )

    fig.add_trace(go.Bar(x=df[['cut_loc', 'wear_num']].groupby(df['cut_loc']).mean().index,
                         y=df[['cut_loc', 'wear_num']].groupby(df['cut_loc']).mean().values.ravel()),
                  row=2, col=1)

    fig.add_trace(go.Pie(labels=df.wear.value_counts().index,
                         values=df['wear'].value_counts().values),
                  row=1, col=2)

    fig.add_trace(go.Pie(labels=df.cut_loc.value_counts().index,
                         values=df['cut_loc'].value_counts().values),
                  row=1, col=1)

    fig.add_trace(go.Pie(labels=df['wear_type'].value_counts().index,
                         values=df['wear_type'].value_counts().values),
                  row=2, col=2)

    fig.show()

    # save charts
    with open('./html/test.html', 'w') as f:
        f.write(fig.to_html(include_plotlyjs='cdn'))
