import plotly.graph_objects as go
import numpy as np

class Drawer:
    def __init__(self, fun, x_from=-5, x_to=5, y_from=-5, y_to=5, delta=0.1):
        self.x_from, self.x_to = x_from, x_to
        self.y_from, self.y_to = y_from, y_to 
        self.delta = delta
        self.fun = fun

        x = [x for x in np.arange(self.x_from,self.x_to+self.delta/2., self.delta)]
        y = [y for y in np.arange(self.y_from,self.y_to+self.delta/2., self.delta)]
        z = [ [self.fun(x,y) for x in np.arange(self.x_from,self.x_to+self.delta/2., self.delta) ] 
                    for y in np.arange(self.y_from,self.y_to+self.delta/2., self.delta) ]

        self.z_min = min(z)
        self.z_max = max(z)
        self.fig = go.Figure(go.Surface(
            x = x,
            y = y,
            z = z,
            opacity=0.50,
            ))


    def add_triangles(self,triangles):
        for i,triangle in enumerate(triangles):
            x=[]
            y=[]
            z=[]
            for point in triangle:
                x.append(point[0])
                y.append(point[1])
                z.append(point[2])

            self.fig.add_trace(
                go.Mesh3d(
                    visible=False,
                    x=x,
                    y=y,
                    z=z,
                    color='black',
                    # opacity=0.50,
                    i=[0],
                    j=[1],
                    k=[2],
                    name="step {}".format(i),
                    # showscale=True
                ))
        self.fig.data[1].visible=True


        steps = []

        for i in range(len(self.fig.data)):
            step = dict(
                method="restyle",
                args=["visible", [False] * len(self.fig.data)],
            )
            step["args"][1][i] = True  # Toggle i'th trace to "visible"
            step["args"][1][0] = True  # Toggle i'th trace to "visible"

            steps.append(step)

        sliders = [dict(
            active=0,
            currentvalue={"prefix": "Iteration: "},
            pad={"t": 50},
            steps=steps
        )]

        self.fig.update_layout(
            sliders=sliders
        )

    def Draw(self):
        self.fig.update_layout(
        scene = dict(
                     xaxis = dict(range=[self.x_from,self.x_to],),
                     yaxis = dict(range=[self.y_from,self.y_to],),
                     zaxis = dict(range=[self.z_min,self.z_max],),),
                     )
        self.fig.show()


if __name__ == "__main__":
    drawer = Drawer(lambda x,y: x*y)
    drawer.add_triangles([
        ((0,0,1),(1,1,1),(3,4,1)),
        ((2,3,4),(5,6,8),(3,4,1))])
    drawer.Draw()