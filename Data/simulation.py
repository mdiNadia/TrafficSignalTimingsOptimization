import traci

def run_simulation():
    try:
        traci.start([
            "sumo-gui",
            "-c", r"C:\\Users\\window_pc_n\\Desktop\\TrafficSignalTimingsOptimization\\Data\\config.sumocfg"
        ])
        print("Simulation started successfully.")

        # Running the simulation loop
        for step in range(1000):
            traci.simulationStep()
            print(f"Step: {step}")

        traci.close()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_simulation()
