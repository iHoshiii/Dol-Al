import itertools

n = int(input("Number of Variables: "))
expr = input("Find: ").lower().replace(" ", "")

variables = [chr(ord('p') + i) for i in range(n)]

print("\nOutput:")

# header
print(" ".join(v.upper() for v in variables), expr.upper())

for row in itertools.product(['T', 'F'], repeat=n):
    values = dict(zip(variables, row))
    
    # helper function to evaluate a variable or its negation
    def eval_var(term):
        if term.startswith('-') or term.startswith('¬'):
            var = term[1:]
            return 'F' if values.get(var, 'F') == 'T' else 'T'
        else:
            return values.get(term, 'F')
    
    result = 'F'
    
    if expr in ["p^q", "p&q"]:
        result = 'T' if eval_var('p') == 'T' and eval_var('q') == 'T' else 'F'
    elif expr in ["pvq", "p|q"]:
        result = 'T' if eval_var('p') == 'T' or eval_var('q') == 'T' else 'F'
    elif expr.startswith('-') or expr.startswith('¬'):
        result = eval_var(expr)
    else:
        result = eval_var(expr)
    
    print(" ".join(row), result)