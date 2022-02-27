import time

from plotly import express as px
from typing import List


def even(i: int) -> bool:
    res = [True, False]
    while True:
        try:
            return res[i]
        except IndexError:
            res += res


def benchmark_even_modulo(nums: List[int]) -> List[float]:
    results = []
    for n in nums:
        start = time.time()
        _ = n // 2 == 0
        results.append(time.time() - start)
    return results


def benchmark_even(nums: List[int]) -> List[float]:
    results = []
    for n in nums:
        start = time.time()
        even(n)
        results.append(time.time() - start)
    return results


if __name__ == "__main__":
    # numbers = [x ** 2 for x in range(1000)]
    numbers = [x for x in range(100000)]
    slow_results = benchmark_even(numbers)
    fast_results = benchmark_even_modulo(numbers)

    df = {"inputs": numbers, "idiot-way": slow_results, "modulo": fast_results}

    fig = px.line(
        df,
        x="inputs",
        y=["idiot-way", "modulo"],
        title="Reddit nonsense vs math",
        labels={
            "inputs": "x for x in range(100000)",
            "idiot-way": "Reddit nonsense",
            "modulo": "Math",
        },
    )
    fig.update_layout(
        yaxis_title="Seconds to solve",
    )
    fig.write_html("myfigure.html")
