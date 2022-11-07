from simulator import Simulator
from simulator.data_generator import generate_table_b, generate_table_a, generate_table_c

def main():
    simulator = Simulator()

    #simulator.run(5, [1, 5, 8, 10], table='a')
    #simulator.run(8, [1, 5, 8, 10], table='a')
    simulator.run(10, [1, 5, 8, 10], table='a')
    #simulator.run(15, [1, 5, 8, 10], table='a')


if __name__ == '__main__':
    main()