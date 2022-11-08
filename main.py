from simulator import Simulator
from simulator.data_generator import DataGeneratorEfficiencyChecker

def main():
    simulator = Simulator()
    simulator.run(8, [1, 5, 8, 10], 'a')

if __name__ == '__main__':
    main()