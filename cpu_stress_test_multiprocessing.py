#!/usr/bin/python3

import multiprocessing
import time
import math


def is_prime(n):
    """Check if a number is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def cpu_stress_task(duration):
    """Perform a CPU-intensive task for the specified duration."""
    print(f"Process {multiprocessing.current_process().name} started.")
    end_time = time.time() + duration
    count = 0
    num = 1
    while time.time() < end_time:
        if is_prime(num):
            count += 1
        num += 1
    print(f"Process {multiprocessing.current_process().name} completed. Primes found: {count}")


def cpu_stress_test(processes=4, duration=10):
    """
    Stress test the CPU using multiple processes.

    Args:
        processes (int): Number of processes to spawn.
        duration (int): Duration for the test in seconds.
    """
    print(f"Starting CPU stress test with {processes} processes for {duration} seconds...")
    process_list = []
    for i in range(processes):
        process = multiprocessing.Process(target=cpu_stress_task, args=(duration,), name=f"Worker-{i+1}")
        process_list.append(process)
        process.start()

    for process in process_list:
        process.join()

    print("CPU stress test completed.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Multiprocess CPU stress test.")
    parser.add_argument("--processes", type=int, default=multiprocessing.cpu_count(), help="Number of processes to use (default: number of CPU cores).")
    parser.add_argument("--duration", type=int, default=10, help="Duration of the test in seconds (default: 10).")
    args = parser.parse_args()

    cpu_stress_test(processes=args.processes, duration=args.duration)

