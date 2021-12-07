"""
create crossplot based on data selected
"""
import plotly.express as px
import pandas as pd
import os


# draw charts
def draw_chart(df, x_axis, y_axis, color_code):
    
    fig = px.scatter(df, x=x_axis, y=y_axis, color=color_code, size=len(df)*[4])

    save_path = './static'
    save_path = os.path.join(save_path, 'crossplot.html')
    
    with open(save_path, 'w') as f:
        f.write(fig.to_html(include_plotlyjs='cdn'))
