# Exercise 6.1
# Suppose you have the set C of all frequent closed itemsets on a data set D, 
# as well as the support count for each frequent closed itemset. 
# Describe an algorithm to determine whether a given itemset X is frequent or not,# and the support of X if it is frequent.

def is_frequent(X_itemset, C_itemset):
    X = frozenset(X_itemset)

    # We'll set the support of X to -1 and if it's still -1 after the loop,
    # then the itemset X is not frequent, and if it's not -1, it will be equal
    # to the actual support of X.
    X_support = -1

    # Find the maximum support count among itemsets that X is a subset of.
    for itemset, support in C_itemset.items():
        if X.issubset(itemset) and support > X_support:
            X_support = support

    return X_support

def main():
    # closed_itemsets are gathered from Example 6.3 of Han's book
    closed_itemsets = {
            frozenset([1]): 6,
            frozenset([2]): 7,
            frozenset([3]): 6,
            frozenset([1, 2]): 4,
            frozenset([1, 3]): 4,
            frozenset([2, 3]): 4,
            frozenset([2, 4]): 2,
            frozenset([1, 2, 3]): 2,
            frozenset([1, 2, 5]): 2
    }

    # some tests
    X = [5]
    print(f"support({set(X)}): {is_frequent(X, closed_itemsets)}")
    
    X = [2, 3]
    print(f"support({set(X)}): {is_frequent(X, closed_itemsets)}")

    X = [2, 5]
    print(f"support({set(X)}): {is_frequent(X, closed_itemsets)}")
   
    X = [1, 3, 5]
    print(f"support({set(X)}): {is_frequent(X, closed_itemsets)}")

    X = [1, 2, 3]
    print(f"support({set(X)}): {is_frequent(X, closed_itemsets)}")


if __name__ == "__main__":
    main()

