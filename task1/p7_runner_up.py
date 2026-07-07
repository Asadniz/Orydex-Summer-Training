"""
Task 1 — Problem 7 (Easy): Find the Runner-Up Score

HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Adapted as a function so it can be tested automatically.
"""

sample_scores = [2, 3, 6, 6, 5]

from helper import b_sort

def find_runner_up(scores: list[int]) -> int:
    """Return the runner-up score: the second highest *distinct* value.

    Example: [2, 3, 6, 6, 5] -> 5 (6 is the highest, 5 is the runner-up).
    """
    # TODO: Remove duplicate scores, then return the second largest value.
    if (len(scores)) == 0:
        return -1
    if (len(scores)) == 1:
        return scores[0]
    
    lst = []
    for num in scores:
        if num not in lst:
            lst.append(num)
    print (lst, "\n")
    b_sort(lst)
    print (lst, "\n")
    return lst[-2]



if __name__ == "__main__":
    print(find_runner_up(sample_scores))
