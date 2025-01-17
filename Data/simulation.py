import traci
import logging

# تنظیمات لاگ برای خطاها
logging.basicConfig(filename='sumo_errors.log', level=logging.DEBUG)

try:
    # شروع SUMO با پیکربندی مورد نظر
    sumo_cmd = ["sumo", "-c", "C:\\Users\\window_pc_n\\Desktop\\TrafficSignalTimingsOptimization\\Data\\config.sumocfg"]
    traci.start(sumo_cmd)

    # اجرای شبیه‌سازی
    step = 0
    while step < 1000:
        traci.simulationStep()  # اجرای یک مرحله شبیه‌سازی
        step += 1

except traci.FatalTraCIError as e:
    logging.error(f"FatalTraCIError occurred: {e.add_note}")
except Exception as e:
    logging.error(f"Unexpected error: {e.add_note}")
finally:
    traci.close()
