import jieba


def parse(input, rankLength, output):
    txt = open(input, "r", encoding='utf-8').read()
    words = jieba.lcut_for_search(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())

    items.sort(key=lambda x: x[1], reverse = True)
    fp = open(output, "w", encoding='utf-8')

    for i in range(rankLength):
        word, count = items[i]
        rank = "{0}\t{1}".format(word, count)
        print(rank)
        fp.write(rank + '\n')

    fp.close()


if __name__ == '__main__':
    parse("comment.txt", 10, "rank.txt")
