from statistics import mean 

class Point:
    def __init__(self,x,y):
        self.x,self.y = x, y
    def __str__(self):
        return "({0:.3f},{1:.3f})".format(self.x,self.y)
    def __repr__(self):
        return "Point({0:.3f},{1:.3f})".format(self.x,self.y)
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def __truediv__(self,other):
        return Point(self.x/other,self.y/other)
    def __mul__(self,other):
        return Point(self.x*other,self.y*other)
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)


def simplex(fun,p=Point(0,0), max_iterations=1000, epsilon = 0.000001,return_simplexes=False):
    """
        Nelder–Mead 2d method

        Parameters:
            fun(x,y)               : function to minimize
            p(Point)               : initial point
            max_iteration(int)     : max number of iterations
            epsilon(float)         : min dispersion of function in simplex vertices
            return_simplexes(bool) : returns list of simplexes if True, best single point otherwise

        Returns:
            [(Point, Point, Point)] : list of simplexes if return_simplexes=True
            Point                   : min point if return_simplexes=False

    """

    e1 = Point(1,0)
    e2 = Point(0,1)

    f = lambda p: fun(p.x,p.y)
    simplexes = []
    
    l,g,h = p+e1,p+e2,p

    for i in range(max_iterations):        
        l,g,h = sorted([l,g,h],key= lambda t: f(t))        
        if return_simplexes==True:
            simplexes.append((l,g,h))  

        fl,fg,fh = f(l),f(g),f(h)
        m = (l+g)/2.0 

        # print(fl,fg,fh)
        # Check
        arr = [fl,fg,fh,f(m)]
        av = mean(arr)
        if sum([(x-av)**2/(len(arr)+1) for x in arr ]) < epsilon:
            break

        # reflection
        r = m + (m-h)*1
        fr = f(r)
        if fl<fr<fg:
            h=r
            continue
        
        # Expansion
        if fr<fl:
            e = m+(r-m)*2
            fe = f(e)
            if fe<fr:
                h=e
            else:
                h = r
            continue

        # Contraction
        # f(r)>f(g)
        c = m + (h-m)*0.5
        fc = f(c)
        if fc<fh:
            h = c
            continue

        # Shrink
        g = l +(g-l)*0.5
        h = l +(h-l)*0.5
    if return_simplexes==True:
        return simplexes
    else:
        return l


if __name__ == "__main__":
    def f(x,y):
        # return 100*(y-x**2)**2+(1-x)**2
        # return x**2+y**2
        # return x**2+x*y+y**2-6*x-9*y
        return (x+2*y-7)**2+(2*x+y-5)**2

    print(simplex(f, return_simplexes=False))

