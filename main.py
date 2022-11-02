from simulator import Simulator
from simulator.data_generator import generate_table_b, generate_table_a, generate_table_c

def main():
    simulator = Simulator()

    table = generate_table_a(100)

    s = 0

    for i in range(len(table)):
        print(f'{i}: {table[i]}')

    #print(generate_table_b(100))

    # simulator.run(price=8, costs=[1, 5, 8, 10], lookup_table_type='b')
    # simulator.run(price=5, costs=[1, 5, 8, 10], lookup_table_type='b')
    # simulator.run(price=10, costs=[1, 5, 8, 10], lookup_table_type='b')
    # simulator.run(price=15, costs=[1, 5, 8, 10], lookup_table_type='b')


if __name__ == '__main__':
    main()