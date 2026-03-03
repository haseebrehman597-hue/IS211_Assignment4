import random
import time
from typing import List, Tuple


def insertion_sort(a_list: List[int]) -> Tuple[List[int], float]:
    start = time.perf_counter()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value

    elapsed = time.perf_counter() - start
    return a_list, elapsed


def shell_sort(a_list: List[int]) -> Tuple[List[int], float]:
    def gap_insertion_sort(lst: List[int], start_idx: int, gap: int) -> None:
        for i in range(start_idx + gap, len(lst), gap):
            current_value = lst[i]
            position = i
            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap
            lst[position] = current_value

    start = time.perf_counter()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count //= 2

    elapsed = time.perf_counter() - start
    return a_list, elapsed


def python_sort(a_list: List[int]) -> Tuple[List[int], float]:
    start = time.perf_counter()
    a_list.sort()
    elapsed = time.perf_counter() - start
    return a_list, elapsed


def _avg_time(times: List[float]) -> float:
    return sum(times) / len(times) if times else 0.0


def main() -> None:
    sizes = [500, 1000, 5000]
    trials = 100

    for n in sizes:
        ins_times = []
        shell_times = []
        py_times = []

        for _ in range(trials):
            lst = [random.randint(1, 1000000) for _ in range(n)]

            _, t = insertion_sort(lst[:])
            ins_times.append(t)

            _, t = shell_sort(lst[:])
            shell_times.append(t)

            _, t = python_sort(lst[:])
            py_times.append(t)

        print(f"\n--- List size: {n} (avg over {trials} lists) ---")
        print(f"Insertion Sort took {_avg_time(ins_times):10.7f} seconds to run, on average")
        print(f"Shell Sort took {_avg_time(shell_times):10.7f} seconds to run, on average")
        print(f"Python Sort took {_avg_time(py_times):10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()