"""
Task 1 — Problem 9 (Medium): Word Order

HackerRank: https://www.hackerrank.com/challenges/word-order/problem

Adapted as a function so it can be tested automatically.
"""

sample_words = ["bcdef", "abcdefg", "bcde", "bcdef"]


def word_order(words: list[str]) -> tuple[int, list[int]]:
    """Return the count of distinct words and how many times each appears.

    The occurrence counts must be ordered by each word's first appearance.

    Example: ["bcdef", "abcdefg", "bcde", "bcdef"] -> (3, [2, 1, 1])
    (3 distinct words; "bcdef" appears twice, then "abcdefg" and "bcde" once.)
    """
    # TODO: Count occurrences while preserving first-appearance order,
    # then return (number_of_distinct_words, list_of_counts).
    pass


if __name__ == "__main__":
    distinct_count, counts = word_order(sample_words)
    print(distinct_count)
    print(counts)
