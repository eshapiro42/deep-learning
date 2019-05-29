import numpy as np
import plotly.graph_objs as go
# from plotly.plotly import iplot
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

np.random.seed(0)

x = (np.random.rand(1000) - .5) * 10
y = 2 * x + np.random.normal(0, 5, x.shape)
y2 = 1.9507894884184496 * x

scatter = go.Scatter(x=x, y=y, mode='markers')
regression = go.Scatter(x=x, y=y2, mode='lines')

layout = dict(showlegend=False)
figure=dict(data=[scatter, regression], layout=layout) 
iplot(figure)