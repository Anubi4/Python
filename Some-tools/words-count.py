__author__ = "Anubi4"

# Code explain：
# 统计文章中每个英文单词出现的频率，并按照从高到低的顺序输出

# -*- coding:utf-8 -*-

from sys import argv

ignore = [',', '.', ':', '!', '?', '”', '"', '\'', '“', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def wordsCount(file_name):
	f = open(file_name)
	txt = f.read()
	for i in ignore:
		txt = txt.replace(i, ' ')

	words1 = txt.split(' ')
	words = map(lambda x:x.lower(), words1)
	dic = {}
	for word in words:
		if word is '':
			continue
		if word in dic:
			dic[word] += 1
		else:
			dic[word] = 1
	return dic

def wordsSort(word_dic):
	dics = sorted(word_dic.iteritems(), key = lambda x:x[1], reverse = True)
	return dics

if __name__ == '__main__':
	file_name = argv[1]
	word_dic = wordsCount(file_name)
	dics = wordsSort(word_dic)
	for i in dics:
		print "%s >>> %d" % (i[0], i[1])
