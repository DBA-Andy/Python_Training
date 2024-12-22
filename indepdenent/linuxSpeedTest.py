#!/usr/bin/python3

import os
import time
import psutil
import subprocess
import speedtest


def cpu_benchmark():
    print("\nStarting CPU Benchmark...")
    start = time.time()
    for _ in range(10**7):
        pass
    duration = time.time() - start
    print(f"CPU Benchmark Completed: Time taken for 10 million loops: {duration:.2f} seconds")
    return duration


def memory_benchmark():
    print("\nStarting Memory Benchmark...")
    mem_info = psutil.virtual_memory()
    print(f"Total Memory: {mem_info.total / (1024**3):.2f} GB")
    print(f"Available Memory: {mem_info.available / (1024**3):.2f} GB")
    return mem_info


def disk_benchmark():
    print("\nStarting Disk Benchmark...")
    test_file = "disk_test.tmp"
    block_size = 1024 * 1024  # 1 MB
    block_count = 100  # 100 MB
    try:
        start = time.time()
        with open(test_file, "wb") as f:
            for _ in range(block_count):
                f.write(os.urandom(block_size))
        duration = time.time() - start
        speed = (block_size * block_count) / duration / (1024**2)
        print(f"Disk Write Speed: {speed:.2f} MB/s")
    finally:
        if os.path.exists(test_file):
            os.remove(test_file)


def network_benchmark():
    print("\nStarting Network Benchmark...")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / (1024**2)  # Convert to Mbps
        upload_speed = st.upload() / (1024**2)  # Convert to Mbps
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
    except Exception as e:
        print(f"Network test failed: {e}")


if __name__ == "__main__":
    print("Linux Host Speed Test\n")
    cpu_benchmark()
    memory_benchmark()
    disk_benchmark()
    network_benchmark()

