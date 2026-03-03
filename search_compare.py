import random
import time
from typing import List, Tuple


def sequential_search(a_list: List[int], item: int) -> Tuple[bool, float]:
    start = time.perf_counter()
    found = False
    pos = 0

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    elapsed = time.perf_counter() - start
    return found, elapsed


def ordered_sequential_search(a_list: List[int], item: int) -> Tuple[bool, float]:
    start = time.perf_counter()
    found = False
    pos = 0
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    elapsed = time.perf_counter() - start
    return found, elapsed


def binary_search_iterative(a_list: List[int], item: int) -> Tuple[bool, float]:
    start = time.perf_counter()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    elapsed = time.perf_counter() - start
    return found, elapsed


def binary_search_recursive(a_list: List[int], item: int) -> Tuple[bool, float]:
    def _helper(lst: List[int], target: int) -> bool:
        if len(lst) == 0:
            return False
        midpoint = len(lst) // 2
        if lst[midpoint] == target:
            return True
        if target < lst[midpoint]:
            return _helper(lst[:midpoint], target)
        return _helper(lst[midpoint + 1:], target)

    start = time.perf_counter()
    found = _helper(a_list, item)
    elapsed = time.perf_counter() - start
    return found, elapsed


def _avg_time(times: List[float]) -> float:
    return sum(times) / len(times) if times else 0.0


def main() -> None:
    sizes = [500, 1000, 5000]
    trials = 100
    target = 99999999

    for n in sizes:
        seq_times = []
        ord_seq_times = []
        bin_it_times = []
        bin_rec_times = []

        for _ in range(trials):
            lst = [random.randint(1, 1000000) for _ in range(n)]

            _, t = sequential_search(lst, target)
            seq_times.append(t)

            sorted_lst = lst[:]
            sorted_lst.sort()

            _, t = ordered_sequential_search(sorted_lst, target)
            ord_seq_times.append(t)

            _, t = binary_search_iterative(sorted_lst, target)
            bin_it_times.append(t)

            _, t = binary_search_recursive(sorted_lst, target)
            bin_rec_times.append(t)

        print(f"\n--- List size: {n} (avg over {trials} lists) ---")
        print(f"Sequential Search took {_avg_time(seq_times):10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {_avg_time(ord_seq_times):10.7f} seconds to run, on average")
        print(f"Binary Search (Iterative) took {_avg_time(bin_it_times):10.7f} seconds to run, on average")
        print(f"Binary Search (Recursive) took {_avg_time(bin_rec_times):10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()