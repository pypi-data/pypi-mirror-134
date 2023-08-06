import sympy
import numpy as np

def mean(f, t, a, b):
    '''
    Symbolically computes the definite
    integral representing the mean value of a
    function using uniform probability measure.

    Parameters
    ----------
    f: SymPy expression.
        Function to be integrated.
    t: `sympy.core.symbol.Symbol`.
        Independent variable to be integrated with respect to.
    a: Undefined.
        Lower bound of integration.
    b: Undefined.
        Upper bound of integration.

    Returns
    -------
    result: SymPy expression.
        Definite mean of function over given interval.
    '''
    f = sympy.sympify(f)
    result = 1/(b-a) * sympy.integrate(f, (t,a,b))
    return result

def std(f, t, a, b):
    '''
    Symbolically computes the definite
    integral representing the standard deviation of a
    function using uniform probability measure.

    Parameters
    ----------
    f: SymPy expression.
        Function to be integrated.
    t: `sympy.core.symbol.Symbol`.
        Independent variable to be integrated with respect to.
    a: Undefined.
        Lower bound of integration.
    b: Undefined.
        Upper bound of integration.

    Returns
    -------
    result: SymPy expression.
        Definite standard deviation of function over given interval.
    '''
    f = (sympy.sympify(f) - mean(f, t, a, b))**2
    return sympy.sqrt(1/(b-a) * sympy.integrate(f, (t,a,b)))

def pdev(f, t, a, b, p=2):
    '''
    Symbolically computes the definite
    integral representing the Minkowski deviation of
    order p of a function using uniform probability measure.

    Parameters
    ----------
    f: SymPy expression.
        Function to be integrated.
    t: `sympy.core.symbol.Symbol`.
        Independent variable to be integrated with respect to.
    a: Undefined.
        Lower bound of integration.
    b: Undefined.
        Upper bound of integration.

    Returns
    -------
    result: SymPy expression.
        Definite Minkowski deviation of order p of function over given interval.
    '''
    f = (sympy.Abs(sympy.sympify(f) - mean(f, t, a, b)))**p
    return (1/(b-a) * sympy.integrate(f, (t,a,b)))**(1/p)

if __name__ == "__main__":
    t = sympy.Symbol('x')
    tau = sympy.Symbol('\\tau')
    w = sympy.Symbol('w')
    p = sympy.Symbol('p')
    result = sympy.simplify(pdev('x', t, tau - w, tau + w,sympy.sympify('3')))
    print(sympy.latex(sympy.simplify(sympy.expand(result))))
