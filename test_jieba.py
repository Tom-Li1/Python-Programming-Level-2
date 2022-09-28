import jieba

with open("test_file.txt", "r", encoding = "utf-8") as file:
    words = jieba.lcut(file.read())

counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        # value = dict.get(key, return value if key does not exist)
        counts[word] = counts.get(word, 0) + 1

# list(dict.items()) -> [(k, v), (k, v), ...]
items = list(counts.items())
# list.sort(key = function(x))
# key receives a function, and the function receives one argument which is each element of the list
# function() returns a value. It is the representative of the element for sort.
# Hence .sort can rearrange the list according to representatives of elements rather than elements themselves.
items.sort(key = lambda x:x[1], reverse = True)

for word, count in items:
    print("{0:<10}{1:>5}".format(word, count))

# lcut(s)
# lcut(s, cut_all = <True / False>)
# lcut_for_search(s)
# add_word(w)