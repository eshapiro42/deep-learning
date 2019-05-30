import numpy as np
import plotly.graph_objs as go
# from plotly.plotly import iplot
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
init_notebook_mode(connected=True)

np.random.seed(1)

x = (np.random.rand(1000) - .5) * 10
y = -2 * x + np.random.normal(0, 2, x.shape) + 5

def cost(w, b):
    y_hat = w * x + b
    return np.mean((y - y_hat)**2)

cost = np.vectorize(cost)

w = np.linspace(-5, 1, 100)
b = np.linspace(2, 8, 100)

W, B = np.meshgrid(w, b)
Z = cost(W, B)

surface = go.Surface(x=W, y=B, z=Z, colorscale='Viridis')

layout = go.Layout(
    scene = dict(
        xaxis = dict(title='w'),
        yaxis = dict(title='b'),
        zaxis = dict(title='cost'),
    )
)

figure = go.Figure(data=[surface], layout=layout)
iplot(figure)