import itertools

n = int(input("No. of Variable: "))
expr = input("Find: ").lower()

variables = [chr(ord('p') + i) for i in range(n)]

print("\nOutput:")

# header
print(" ".join(v.upper() for v in variables), expr.replace(" ", "").upper())

for row in itertools.product(['T','F'], repeat=n):

    values = dict(zip(variables, row))

    p = values.get('p','F')
    q = values.get('q','F')

    result = 'F'

    if expr == "p v q":
        result = 'T' if p == 'T' or q == 'T' else 'F'

    elif expr == "p ^ q":
        result = 'T' if p == 'T' and q == 'T' else 'F'

    print(" ".join(row), result)