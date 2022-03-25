import pytest

from api import eval_input

cases = [
    ('242/33',
     [{'title': 'SymPy', 'input': '242/33', 'output': {'type': 'Tex', 'tex': '\\frac{22}{3}'}},
      {'name': 'float_approximation', 'variable': 'None', 'title': 'Floating-point approximation',
       'input': '(22/3).evalf()', 'parameters': ['digits']}]),
    ('12',
     [{'title': 'SymPy', 'input': '12', 'output': {'type': 'Tex', 'tex': '12'}},
      {'name': 'digits', 'variable': 'None', 'title': 'Digits in base-10 expansion of number',
       'input': 'len(str(12))'},
      {'name': 'roman_numeral', 'variable': 'None', 'title': 'Roman numeral', 'input': None},
      {'name': 'chinese_numeral', 'variable': 'None', 'title': 'Chinese numeral', 'input': None},
      {'name': 'binary_form', 'variable': 'None', 'title': 'Binary form', 'input': 'np.base_repr(12)'},
      {'name': 'factorization', 'variable': 'None', 'title': 'Factors', 'input': 'factorint(12)'},
      {'name': 'factorizationDiagram', 'variable': 'None', 'title': 'Factorization Diagram',
       'input': 'factorint(12)'}]),
    ('div(x**2 - 4 + x, x-2)',
     [{'input': 'div(x**2-4+x,x-2)', 'title': 'SymPy',
       'output': {'tex': '\\mathrm{div}(x^{2} + x - 4, x - 2)', 'type': 'Tex'}},
      {'input': 'div(x**2-4+x,x-2)',
       'output': {'list': [{'tex': 'x + 3', 'type': 'Tex'}, {'tex': '2', 'type': 'Tex'}], 'type': 'List'},
       'title': 'Result'}]),
    ('factor(x**2 - 1)',
     [{'input': 'factor(x**2-1)', 'title': 'SymPy',
       'output': {'tex': '\\mathrm{Factorization~of~}x^{2} - 1', 'type': 'Tex'}},
      {'input': 'factor(x**2-1)', 'title': 'Result',
       'output': {'tex': '\\left(x - 1\\right) \\left(x + 1\\right)', 'type': 'Tex'}}]),
    ('solve(x**2 + 4*x + 181, x)',
     [{'title': 'SymPy', 'input': 'solve(x**2+4*x+181,x)',
       'output': {'type': 'Tex', 'tex': '\\mathrm{solve}\\;x^{2} + 4 x + 181=0\\;\\mathrm{for}\\;x'}},
      {'title': 'Result', 'input': 'solve(x**2+4*x+181,x)',
       'output': {'type': 'List',
                  'list': [{'type': 'Tex', 'tex': '-2 - \\sqrt{177} i', 'numeric': True,
                            'expression': '-2 - sqrt(177)*I', 'approximation': '-2.0 - 13.3041346956501 i'},
                           {'type': 'Tex', 'tex': '-2 + \\sqrt{177} i', 'numeric': True,
                            'expression': '-2 + sqrt(177)*I', 'approximation': '-2.0 + 13.3041346956501 i'}]}}]),
    ('sin(2*x)',
     [{'title': 'SymPy', 'input': 'sin(2*x)', 'output': {'type': 'Tex', 'tex': '\\sin{\\left(2 x \\right)}'}},
      {'name': 'trig_alternate', 'variable': 'x', 'title': 'Alternate forms', 'input': None, 'pre_output': ''},
      {'name': 'plot', 'variable': 'x', 'title': 'Plot', 'input': None,
       'parameters': ['xmin', 'xmax', 'tmin', 'tmax', 'pmin', 'pmax']},
      {'name': 'roots', 'variable': 'x', 'title': 'Roots', 'input': 'solve(sin(2*x), x)', 'pre_output': 'x'},
      {'name': 'diff', 'variable': 'x', 'title': 'Derivative', 'input': 'diff(sin(2*x), x)',
       'pre_output': '\\frac{d}{d x} \\sin{\\left(2 x \\right)}'},
      {'name': 'integral_alternate', 'variable': 'x', 'title': 'Antiderivative forms', 'input': None, 'pre_output': ''},
      {'name': 'series', 'variable': 'x', 'title': 'Series expansion around 0', 'input': 'series(sin(2*x), x, 0, 10)'}
      ]),
    ('diff(f(x)*g(x)*h(x))',
     [{'input': "diff(Function('f')(x)*Function('g')(x)*Function('h')(x))", 'title': 'SymPy',
       'output': {'tex': '\\frac{d}{d x} f{\\left(x \\right)} g{\\left(x \\right)} h{\\left(x \\right)}',
                  'type': 'Tex'}},
      {'name': 'diff', 'input': 'diff(f(x)*g(x)*h(x), x)', 'title': 'Derivative', 'variable': 'x',
       'pre_output': '\\frac{d}{d x} f{\\left(x \\right)} g{\\left(x \\right)} h{\\left(x \\right)}'}]),
    ('integrate(tan(x))',
     [{'input': 'integrate(tan(x))', 'output': {'tex': '\\int \\tan{\\left(x \\right)}\\, dx', 'type': 'Tex'},
       'title': 'SymPy'},
      {'name': 'integral_alternate_fake', 'input': None, 'pre_output': '',
       'title': 'Antiderivative forms', 'variable': 'x'},
      {'name': 'intsteps', 'input': 'integrate(tan(x), x)',
       'title': 'Integral Steps', 'variable': 'x'}]),
    ('10!!',
     [{'title': 'SymPy', 'input': 'factorial2(10)', 'output': {'type': 'Tex', 'tex': '3840'}},
      {'name': 'digits', 'variable': 'None', 'title': 'Digits in base-10 expansion of number',
       'input': 'len(str(3840))'},
      {'name': 'factorization', 'variable': 'None', 'title': 'Factors',
       'input': 'factorint(3840)'}]),
    ('totient(42)',
     [{'title': 'SymPy', 'input': 'totient(42)', 'output': {'type': 'Tex', 'tex': '12'}},
      {'name': 'totient', 'variable': 'None', 'title': 'Step', 'input': 'totient(42)'}]),
    ('totient(x)',
     [{'title': 'SymPy', 'input': 'totient(x)', 'output': {'type': 'Tex', 'tex': '\\phi\\left(x\\right)'}}]),
    ('isprime(12321)',
     [{'title': 'SymPy', 'input': 'isprime(12321)',
       'output': {'type': 'Tex', 'tex': '\\mathrm{Is~}12321\\mathrm{~prime?}'}},
      {'name': 'result', 'variable': 'None', 'title': 'Result', 'input': 'isprime(12321)'},
      {'name': 'is_prime', 'variable': 'None', 'title': 'Step', 'input': 'isprime(12321)'}]),
    ('rsolve(y(n+2)-y(n+1)-y(n), y(n))',
     [{'title': 'SymPy',
       'input': "rsolve(Function('y')(n+2)-Function('y')(n+1)-Function('y')(n),Function('y')(n))",
       'output': {'type': 'Tex',
                  'tex': '\\mathrm{Solve~the~recurrence~}- y{\\left(n \\right)} - y{\\left(n + 1 \\right)} + '
                         'y{\\left(n + 2 \\right)} = 0'}},
      {'title': 'Result',
       'input': "rsolve(Function('y')(n+2)-Function('y')(n+1)-Function('y')(n),Function('y')(n))",
       'output': {'type': 'Tex',
                  'tex': 'C_{0} \\left(\\frac{1}{2} - \\frac{\\sqrt{5}}{2}\\right)^{n} + C_{1} \\left(\\frac{1}{2} + '
                         '\\frac{\\sqrt{5}}{2}\\right)^{n}'}},
      {'title': 'Simplification',
       'input': '(C0*(1 - sqrt(5))**n + C1*(1 + sqrt(5))**n)/2**n',
       'output': {'type': 'Tex',
                  'tex': '2^{- n} \\left(C_{0} \\left(1 - \\sqrt{5}\\right)^{n} + C_{1} \\left(1 + '
                         '\\sqrt{5}\\right)^{n}\\right)'}},
      None]),
    ('diophantine(x**2 - 4*x*y + 8*y**2 - 3*x + 7*y - 5)',
     [{'title': 'SymPy', 'input': 'diophantine(x**2-4*x*y+8*y**2-3*x+7*y-5)',
       'output': {'type': 'Tex',
                  'tex': '\\begin{align}&\\mathrm{Solve~the~diophantine~equation~}x^{2} - 4 x y - 3 x + 8 y^{2} + 7 y '
                         '- 5 = 0\\\\&\\mathrm{where~}(x, y)\\mathrm{~are~integers}\\end{align}'}},
      {'title': 'Result', 'input': 'diophantine(x**2-4*x*y+8*y**2-3*x+7*y-5)',
       'output': {'type': 'Table', 'titles': ('x', 'y'),
                  'rows': [[{'type': 'Tex', 'tex': '5'}, {'type': 'Tex', 'tex': '1'}],
                           [{'type': 'Tex', 'tex': '2'}, {'type': 'Tex', 'tex': '1'}]]}}]),
    ('plot(sin(x) + cos(2*x))',
     [{'input': 'plot(sin(x)+cos(2*x))', 'title': 'SymPy',
       'output': {'tex': '\\mathrm{Plot~}\\sin{\\left(x \\right)} + \\cos{\\left(2 x \\right)}', 'type': 'Tex'}},
      {'name': 'plot', 'input': ['sin(x) + cos(2*x)'], 'parameters': ['xmin', 'xmax', 'tmin', 'tmax', 'pmin', 'pmax'],
       'title': 'Plot', 'variable': 'x'}]),
    ('plot(r=1-sin(theta))',
     [{'input': 'plot(r=1-sin(theta))', 'title': 'SymPy',
       'output': {'tex': '\\mathrm{Plot~}\\left\\{ \\mathtt{\\text{r}} : 1 - \\sin{\\left(\\theta \\right)}\\right\\}',
                  'type': 'Tex'}},
      {'name': 'plot', 'input': ['r = 1 - sin(theta)'], 'parameters': ['xmin', 'xmax', 'tmin', 'tmax', 'pmin', 'pmax'],
       'title': 'Plot', 'variable': 'x'}]),
    ('π',
     [{'title': 'SymPy', 'input': 'π', 'output': {'type': 'Tex', 'tex': '\\pi'}},
      {'name': 'float_approximation', 'variable': 'None', 'title': 'Floating-point approximation',
       'input': '(pi).evalf()', 'parameters': ['digits']}]),
    ('factor(12)',
     [{'ambiguity': 'factorint(12)',
       'description': [{'type': 'Expression', 'value': 'factor'},
                       {'type': 'Text', 'value': ' factors polynomials, while '},
                       {'type': 'Expression', 'value': 'factorint'},
                       {'type': 'Text', 'value': ' factors integers.'}]},
      {'title': 'SymPy', 'input': 'factor(12)', 'output': {'type': 'Tex', 'tex': '\\mathrm{Factorization~of~}12'}},
      {'title': 'Result', 'input': 'factor(12)', 'output': {'type': 'Tex', 'tex': '12'}}]),
]


@pytest.mark.parametrize('expression, expected', cases)
def test(expression: str, expected: dict):
    actual = eval_input(expression)['result']
    assert len(actual) == len(expected)
    for a, e in zip(actual, expected):
        assert e is None or a == e
