from Drawer import *
from Simplex2D import *

test_functions={
    "Paraboloid":
    (lambda x,y: x**2+y**2,(0,0)),

    "Rosenbrock":
    (lambda x,y: 100*(y-x**2)**2+(1-x)**2,(1,1)),

    "Booth":
    (lambda x,y: (x+2*y-7)**2+(2*x+y-5)**2,(1,3))
}
if __name__ == "__main__":    
    for (f_name,f_data) in test_functions.items():
        f,(true_x,true_y)= f_data
        simplexes = simplex(f,return_simplexes=True)
        triangles = [ ((point.x,point.y,f(point.x,point.y)) for point in triangle ) for triangle in simplexes ]
        drawer = Drawer(f,x_from=-3.5,x_to=3.5,y_from=-3.5,y_to=3.5)
        drawer.add_triangles(triangles)
        drawer.Draw()
        print("Function: {f_name}, result: {res}, true min: ({true_x},{true_y}), iterations: {iterations}".format(
            f_name=f_name,
            res = simplexes[-1][0],
            true_x = true_x,
            true_y = true_y,
            iterations = len(simplexes)
            ))        
