import dash
from dash import dcc,Input,Output,html
import pandas as pd
import numpy as np
import plotly_express as px

# creating dummy data
dy = pd.DataFrame(np.random.randint(0,100,(200,2)))
dy.columns = ['x','y']
dy['Gender'] = np.random.choice(['M','F'],200)


dt = dy.groupby('Gender')['x'].agg('mean').reset_index().rename(columns = {0:'n'})
print(dt.head())
# create the graph
fig = px.scatter(dy,x = 'x',y = 'y',title = "scatter plot of dummy data")
fig1 = px.pie(dt,values = 'x',names = 'Gender',title = "A pie chart of the gender vs X")

app = dash.Dash(__name__)

app.layout = html.Div(
    children = [
        dcc.Graph(id = "01",figure  = fig),
        dcc.Graph(id = "02",figure  = fig1)
        ]
)




if __name__ == '__main__':
    app.run_server(debug = True)