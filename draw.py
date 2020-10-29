import csv
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def draw(input, output):
    with open(input, "r", encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        indexs = []
        value = []
        for record in csv_reader:
            indexs.append(record[0])
            value.append(int(record[1]))

        plt.bar(indexs, value)
        plt.xlabel("word")
        plt.ylabel("freq")
        plt.title("word freq analysis")
        plt.savefig(output)
        plt.show()

if __name__ == '__main__':
    draw('rank.txt', 'rank.png')
