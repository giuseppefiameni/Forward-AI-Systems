import psutil
import torch

class ResourceMonitor:
    @staticmethod
    def log_system_metrics():
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent
        print(f"[System] CPU: {cpu_usage}% | RAM: {mem_usage}%")
        
        if torch.cuda.is_available():
            gpu_mem = torch.cuda.memory_allocated() / 1e6
            print(f"[GPU] Allocated Memory: {gpu_mem:.2f} MB")

if __name__ == "__main__":
    ResourceMonitor.log_system_metrics()