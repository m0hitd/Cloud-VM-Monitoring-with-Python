import psutil
import time

def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, mem, disk

if __name__ == "__main__":
    while True:
        cpu, mem, disk = get_metrics()
        print(f"CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%")
        time.sleep(5)
