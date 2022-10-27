from simulator import Simulator

def main():
    simulator = Simulator()
    simulator.run_a(price=15, costs=[1, 5, 8, 10])

if __name__ == '__main__':
    main()