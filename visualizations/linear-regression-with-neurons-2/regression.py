import numpy as np
import plotly.graph_objs as go
from plotly.plotly import iplot
# from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
init_notebook_mode(connected=True)

np.random.seed(1)

x = (np.random.rand(1000) - .5) * 10
y = -2 * x + np.random.normal(0, 2, x.shape) + 5
y2 =  -1.9978732544888549 * x + 5.09462933978991

scatter = go.Scatter(x=x, y=y, mode='markers')
regression = go.Scatter(x=x, y=y2, mode='lines')

layout = dict(showlegend=False)
figure=dict(data=[scatter, regression], layout=layout) 
iplot(figure)