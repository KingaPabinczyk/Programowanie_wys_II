from typing import List

def average(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Lista nie może być pusta.")
    return sum(numbers) / len(numbers)


print(average([1.5, 2.5, 3.5]))  # 2.5
print(average([10.0, 20.0, 30.0, 40.0]))  # 25.0
