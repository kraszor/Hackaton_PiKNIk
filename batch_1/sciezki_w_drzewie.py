from copy import deepcopy


# maximum sum path
def binary_tree(tree):
    str_tree = deepcopy(tree)
    sum_tree = deepcopy(tree)
    for row in range(len(tree) - 1, 0, -1):
        for col in range(0, row):
            maximum = max(sum_tree[row][col], sum_tree[row][col + 1])
            index = sum_tree[row][col:col + 2].index(maximum)
            index = index + len(sum_tree[row][0:col])
            sum_tree[row - 1][col] += maximum
            str_tree[row - 1][col] = "{}+{}".format(str(str_tree[row - 1][col]), str(str_tree[row][index]))
    return str_tree[0][0]


tree = [[1], [4, 4], [9, 8, 6], [1, 5, 7, 5], [2, 3, 5, 2, 1]]


print(binary_tree(tree))
