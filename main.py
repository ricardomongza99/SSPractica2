from simulator import Simulator
from simulator.data_generator import generate_table_b, generate_table_a, generate_table_c

def main():
    simulator = Simulator()

    simulator.run_iterations(iterations=[100, 1_000, 10_000, 100_000], price=10, cost=8, lookup_table_type='a')
    #simulator.run(price=20, costs=[15, 16, 17, 18], lookup_table_type='c')
    #simulator.run(price=8, costs=[1, 5, 8, 10], lookup_table_type='c')
    #simulator.run(price=10, costs=[1, 5, 8, 10], lookup_table_type='a')
    #simulator.run(price=15, costs=[1, 5, 8, 10], lookup_table_type='c')


if __name__ == '__main__':
    main()