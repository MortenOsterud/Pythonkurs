import math
def a(x):
    return x, x
def b(x):
    return x, 2*x+1
def c(x):
    return x, -0.5*x+1
def d(x):
    return x, 3
def e(x):
    return x, -3.15*x+12.1
def f(x):
    return x, 1700/x
def g(x):
    return x, 500/x + 200
def h(x):
    return x, x**2
def i(x):
    return x, -x**2 + 2
def j(x):
    return x, 0.5*x**2 -2*x + 1
def k(x):
    return x, 1000*1.2**x
def l(x):
    return x, 500*0.9**x
def m(x):
    return x, 97*x-73.1
def n(x):
    return x, -3*x**2-2*x-4
def o(x):
    return x, 45/x + 10
def p(x):
    return x, 35000*1.25**x
def q(x):
    return x, 35 / (0.1*x)
def r(x):
    return x, math.sqrt(x)
def s(x):
    return x, (x+2)/(x+1)
def t(x):
    return x, 12/(x+1)
def u(x):
    return x, x**3
def v(x):
    return x, x**5
def w(x):
    return x, math.log10(x)
    
 
def test1(funksjon1, funksjon2):
    x_testverdier = [1000, 1.25, 33]
    godkjent = True
    for x in x_testverdier:
        if not math.isclose(funksjon1(x)[1],funksjon2(x)[1]):
            godkjent = False
    if godkjent:
        print("Godkjent", funksjon1.__name__)
    else:
        print("Feil funksjonsuttrykk", funksjon1.__name__)
        
def test(ny_a, ny_b, ny_c, ny_d, ny_e, ny_f, ny_g, ny_h, ny_i, ny_j, ny_k, ny_l, ny_m, ny_n, ny_o, ny_p, ny_q, ny_r, ny_s, ny_t, ny_u, ny_v, ny_w):
    test1(a, ny_a)          
    test1(b, ny_b)
    test1(c, ny_c)
    test1(d, ny_d)
    test1(e, ny_e)
    test1(f, ny_f)
    test1(g, ny_g)
    test1(h, ny_h)
    test1(i, ny_i)
    test1(j, ny_j)
    test1(k, ny_k)
    test1(l, ny_l)
    test1(m, ny_m)
    test1(n, ny_n)
    test1(o, ny_o)
    test1(p, ny_p)
    test1(q, ny_q)
    test1(r, ny_r)
    test1(s, ny_s)
    test1(t, ny_t)
    test1(u, ny_u)
    test1(v, ny_v)
    test1(w, ny_w)