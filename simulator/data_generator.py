
"""
Creates lookup table for uniform distribution
Example: size=100 -> [0.01, 0.02, 0.03,..., 1]
"""
def generate_table_a(size):
    table = [0] * size
    table[0] = 1.0 / size
    for i in range(1, size):
        table[i] = round(table[i-1] + 1.0 / size, 2)
    return table

def generate_table_b(size):
    max = (size * (size + 1)) / 2
    table = [0] * size
    table[0] = 1.0 / max
    for i in range(1, size):
        table[i] = table[i-1] + (i + 1) / max
    return table

def generate_table_c(size):
    max = size * size / 4
    table = [0] * size
    for i in range(1, int(size/2)):
        table[i] = table[i-1] + i / max
    for i in range(int(size/2), size):
        table[i] = table[i-1] + (size - i) / max
    return table