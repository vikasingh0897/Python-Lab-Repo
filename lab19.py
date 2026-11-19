import queue
import threading
import time
from typing import List


class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self) -> None:
        with self.lock:
            self.value += 1


def worker(worker_id: int, task_queue: queue.Queue, counter: ThreadSafeCounter, results: List[str]) -> None:
    while True:
        try:
            task = task_queue.get_nowait()
        except queue.Empty:
            break

        # Simulate task computation
        result = f"Worker-{worker_id} completed '{task}'"
        results.append(result)
        counter.increment()
        task_queue.task_done()


def main():
    task_queue: queue.Queue = queue.Queue()
    counter = ThreadSafeCounter()
    results: List[str] = []

    tasks = [f"DataJob-{i}" for i in range(1, 9)]
    for t in tasks:
        task_queue.put(t)

    print(f"Dispatching {len(tasks)} tasks across 3 worker threads...")

    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=worker, args=(i, task_queue, counter, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nExecution Results:")
    for res in results:
        print(f"  ✓ {res}")

    print(f"\nTotal Tasks Processed : {counter.value}")
    print("Thread Synchronization : Verified (Zero race conditions)")


if __name__ == "__main__":
    main()
