import itertools

n = int(input("Enter number of variables: "))

variables = [chr(ord('p') + i) for i in range(n)]

print("\nOutput:")

# print header with spacing
header = variables + ["¬P", "P^Q", "PvQ", "P→Q", "P↔Q"]
print("".join(f"{h:<5}" for h in header))

for row in itertools.product(['T','F'], repeat=n):

    p = row[0]
    q = row[1] if n > 1 else 'F'

    not_p = 'F' if p == 'T' else 'T'
    p_and_q = 'T' if p == 'T' and q == 'T' else 'F'
    p_or_q = 'T' if p == 'T' or q == 'T' else 'F'
    p_imp_q = 'F' if p == 'T' and q == 'F' else 'T'
    p_bi_q = 'T' if p == q else 'F'

    row_data = list(row) + [not_p, p_and_q, p_or_q, p_imp_q, p_bi_q]

    print("".join(f"{item:<5}" for item in row_data))