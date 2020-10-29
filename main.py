import spider
import wordfreq
import draw

BVid = 'BV1hD4y19756'
TXT = 'comment.txt'
RANK = 'rank.txt'
JPG ='rank.png'
rank = 40 #关键字数量

spider.Spider(BVid, TXT, 0)
wordfreq.parse(TXT, rank, RANK)
draw.draw(RANK, JPG)
