from math import sqrt
from math import sin
from math import cos

def newton(f_prime, f_doubleprime, x0, max_iterations= 1000, x_tol=0.00001):
    x_new = x0+x_tol*2
    iteration = 0
    while iteration<max_iterations and abs(x_new-x0)>x_tol:
        x0=x_new
        x_new = x0 - f_prime(x0)/f_doubleprime(x0)
    return x_new

def golden_section(f,a,b,max_iterations = 1000, x_tol = 0.00001):
    fi = (1+sqrt(5))/2
    
    x1, x2 = b - (b-a)/fi, a + (b-a)/fi
    f_left,f_right=f(x1),f(x2)

    iteration = 0
    while iteration<max_iterations and abs(x2-x1)>x_tol:

        if f_left>f_right:
            a = x1
            x1 = b - (b-a)/fi
            x2 = a + (b-a)/fi
            f_left = f_right
            f_right = f(x2)
        else:
            b = x2
            x1 = b - (b-a)/fi
            x2 = a + (b-a)/fi
            f_right = f_left
            f_left = f(x1)
        iteration+=1
    return (x1+x2)/2

if __name__ == "__main__":
    f_calls = 0
    def f(x):
        global f_calls
        f_calls+=1
        return 89*x**13+27*x**2

    print("golden section: {gold_res}, {gold_calls} calls".format(
        gold_res=golden_section(f,-0.5,+0.5,x_tol=0.00000001),
        gold_calls=f_calls))

    prime_calls, doubleprime_calls = 0,0
    def f_prime(x):
        global prime_calls
        prime_calls+=1
        return 89*13*x**12+27**2*x

    def f_secondprime(x):
        global doubleprime_calls
        doubleprime_calls+=1
        return 89*13*12*x**11


    print("newton: {newton_res}, {prime_calls} prime calls, {doubleprime_calls} second prime calls".format(
        newton_res= newton(f_prime, f_secondprime, 3),
        prime_calls = prime_calls,
        doubleprime_calls = doubleprime_calls
    ))

        




