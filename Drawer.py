import plotly.graph_objects as go
import numpy as np

def f(x,y):
    return x**2+y**2

class Drawer:
    def __init__(self, fun, x_from=-1, x_to=1, y_from=-1, y_to=1, delta=0.1):
        self.x_from, self.x_to = x_from, x_to
        self.y_from, self.y_to = y_from, y_to 
        self.delta = delta
        self.fun = fun
        self.fig = go.Figure(go.Surface(
            x = [x for x in np.arange(self.x_from,self.x_to+self.delta/2., self.delta)],
            y = [y for y in np.arange(self.y_from,self.y_to+self.delta/2., self.delta)],
            z = [ [self.fun(x,y) for x in np.arange(self.x_from,self.x_to+self.delta/2., self.delta) ] 
                    for y in np.arange(self.y_from,self.y_to+self.delta/2., self.delta) ]))

    def add_trace(self,x,y,z):
        self.fig.add_trace(go.Surface(x=x,y=y,z=z))

    def Draw(self):
        self.fig.show()


if __name__ == "__main__":
    drawer = Drawer(lambda x,y: x*y)
    drawer.Draw()