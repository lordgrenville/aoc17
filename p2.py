import pandas as pd
from itertools import product

# copy the string to clipboard first...
df = pd.read_clipboard(header=None)
print((df.max(1) - df.min(1)).sum())


# part 2
def find_pair(li):
    li = list(filter(lambda x: x[0] != x[1], [x for x in product(li, li)]))
    pair = list(filter(lambda x: x[0] % x[1] == 0, li))[0]
    return pair[0] // pair[1]


print(df.apply(find_pair, 1).sum())
