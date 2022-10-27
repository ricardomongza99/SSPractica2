
"""
Creates lookup table for uniform distribution
Example: size=100 -> [0.01, 0.02, 0.03,..., 1]
"""
def generate_table_a(size):
    table = [0] * size
    table[0] = 1.0 / size
    for i in range(1, size):
        table[i] = table[i-1] + 1.0/size
    return table

# TODO
def generate_table_b(size):
    return []

# TODO
def generate_table_c(size):
    return []