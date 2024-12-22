#!/usr/bin/python3

import threading
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
    print(f"Thread {threading.current_thread().name} started.")
    end_time = time.time() + duration
    count = 0
    num = 1
    while time.time() < end_time:
        if is_prime(num):
            count += 1
        num += 1
    print(f"Thread {threading.current_thread().name} completed. Primes found: {count}")


def cpu_stress_test(threads=4, duration=10):
    """
    Stress test the CPU using multiple threads.

    Args:
        threads (int): Number of threads to spawn.
        duration (int): Duration for the test in seconds.
    """
    print(f"Starting CPU stress test with {threads} threads for {duration} seconds...")
    thread_list = []
    for i in range(threads):
        thread = threading.Thread(target=cpu_stress_task, args=(duration,), name=f"Worker-{i+1}")
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    print("CPU stress test completed.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Multithreaded CPU stress test.")
    parser.add_argument("--threads", type=int, default=4, help="Number of threads to use (default: 4).")
    parser.add_argument("--duration", type=int, default=10, help="Duration of the test in seconds (default: 10).")
    args = parser.parse_args()

    cpu_stress_test(threads=args.threads, duration=args.duration)

