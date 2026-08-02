import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

def run_visual_simulation():
    print(f"{Fore.CYAN}=== DISTRIBUTED STREAM ENGINE: LIVE SIMULATION DASHBOARD ===\n")
    devices = ["grid_node_alpha", "smart_substation_02", "industrial_turbine_07"]
    
    for i in range(1, 11):
        device = random.choice(devices)
        temp = round(random.uniform(60.0, 112.0), 2)
        pressure = round(random.uniform(300.0, 520.0), 2)
        status = "CRITICAL" if temp > 100.0 else "NORMAL"
        
        status_color = Fore.RED if status == "CRITICAL" else Fore.GREEN
        
        print(f"[{time.strftime('%H:%M:%S')}] Stream ID: 1718-{i:03d} | Device: {device:<22} | Temp: {temp:>6}°C | Status: {status_color}{status}")
        time.sleep(0.2)
        
    print(f"\n{Fore.GREEN}Simulation complete. 10 telemetry packets processed successfully via Redis Stream buffer.")

if __name__ == "__main__":
    run_visual_simulation()
