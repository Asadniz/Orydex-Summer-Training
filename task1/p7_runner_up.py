"""
Task 1 — Problem 7 (Easy): Find the Runner-Up Score

HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Adapted as a function so it can be tested automatically.
"""

sample_scores = [2, 3, 6, 6, 5]


def find_runner_up(scores: list[int]) -> int:
    """Return the runner-up score: the second highest *distinct* value.

    Example: [2, 3, 6, 6, 5] -> 5 (6 is the highest, 5 is the runner-up).
    """
    # TODO: Remove duplicate scores, then return the second largest value.
    
    if len(scores) <= 1:
        return -1

    lst = []
    for num in scores:
        if num not in lst:
            lst.append(num)
    
    if len(lst) == 1:
        return -1
    
    if lst[0] > lst[1]:
        best = lst[0]
        runner_up = lst[1]
    else:
        best = lst[1]
        runner_up = lst[0]
    
    for i in range(2, len(lst)):
        if lst[i] > best:
            runner_up = best
            best = lst[i]
        elif lst[i] < best and lst[i] > runner_up:
            runner_up = lst[i]
    return runner_up


if __name__ == "__main__":
    print(find_runner_up(sample_scores))
