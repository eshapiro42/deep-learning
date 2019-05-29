import numpy as np
import plotly.graph_objs as go
# from plotly.plotly import icreate_animations
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

x = np.array([1,2,3])
y = 2 * x
costs = []
weights = np.linspace(-1, 5, 1000)
for w in weights:
    y_hat = w * x
    cost = np.sum((y-y_hat)**2) / y.shape[0]
    costs.append(cost)    
x = weights
y = np.array(costs)

t = np.linspace(0,2)

xx = t
yy = 4.66666667 * t**2 - 18.66666667 * t + 18.66666667

x = x.tolist()
y = y.tolist()
xx = xx.tolist()
yy = yy.tolist()

data = [
    dict(
        x=[0], 
        y=[18.66666667], 
        mode='markers', 
        marker=dict(color='red', size=10)
    ),
    dict(
        x=x, 
        y=y, 
        mode='lines', 
        line=dict(width=2, color='#1F77B4')
    ),
]

layout = dict(
    showlegend=False,
    width=500, height=400,
    updatemenus=[
        dict(
            type='buttons', showactive=False,
             y=1.25,
             x=.51,
            xanchor='center',
            yanchor='top',
            pad=dict(t=0, r=10),
            buttons=[
                dict(
                    label='Play',
                    method='animate',
                    args=[
                        None, 
                        dict(
                            frame=dict(duration=50, redraw=True),
                            transition=dict(duration=0),
                            fromcurrent=True,
                            mode='immediate'
                        )
                    ]
                )
            ]
        )
    ]
)

frames = [
    dict(
        data=[
            dict(
                x=[xx[k]], 
                y=[yy[k]], 
                mode='markers', 
                marker=dict(color='red', size=10)
            )
        ]
    ) for k in range(50)]    
          
figure = dict(data=data, layout=layout, frames=frames)          
# icreate_animations(figure)
iplot(figure)