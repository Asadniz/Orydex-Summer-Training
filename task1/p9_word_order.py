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
    lst = list(words)
    result = list()
    word_list = [None] * len(lst)
    word_count = 0
    ind = 0
    for i in range (len(words)):
        if words[i] in word_list:
            continue
        word_list.append(words[i])
        count = 1
        for j in range (i + 1, len(words)):
            if words[i] == words[j]:
                print ("index i is", i, "index j is", j)
                print (words[i], " is in ", words[j])
                count += 1
        word_count += 1
        result.append(count)
        ind += 1
    return (word_count, result)


if __name__ == "__main__":
    distinct_count, counts = word_order(sample_words)
    print(distinct_count)
    print(counts)
