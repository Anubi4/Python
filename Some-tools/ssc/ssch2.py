#coding=utf-8

history_file = open('hist.txt')
history_num = []
for i in history_file.readlines():
      history_num.append(i.replace('\n',''))
history_file.close()

file_list = open('result.txt')
num_list = []
for num in file_list.readlines():
      num_list.append(num.replace('\n',''))
file_list.close()

def get_cpnum():
      import requests
      from bs4 import BeautifulSoup as bs

      cp_url = 'http://chart.cp.360.cn/zst/getchartdata?lotId=255401&chartType=x2fb&spanType=0&span=100&r=0.642043098146788#roll_0'
      context = requests.get(cp_url)
      soup = bs(context.content)

      cpnum = []
      num = soup.find_all(attrs={'class':'num'})
      for i in num:
            cpnum.append(i.text.strip('\n'))
      return cpnum

def max_omits(history_num, num):
      omit = 0
      omit_list = []
      for i in history_num:
            if i not in num:
                  omit += 1
            else:
                  omit_list.append(omit)
                  omit = 0
      return omit_list


def current_omit(current_num, num):
      c_omit = 0
      for i in current_num:
            if i not in num:
                  c_omit += 1
            else:
                  c_omit = 0
            continue

      return c_omit

def main():
      cpnum = get_cpnum()
      omits_count = {}
      miss_list = {}
      for num in num_list:
            c_omits = current_omit(cpnum, num)
            miss_list[str(num)] = c_omits

      max_num = sorted(miss_list.iteritems(), key = lambda x : x[1])
      print "Current number is %s" % cpnum[-1]
      for i in range(-20, 0):
            max_omit = max_omits(history_num,max_num[i][0])
            max_omit.sort()
            print max_num[i][0] + "  Current omission:%s" %max_num[i][1] + "  History biggest omission:%s" %max_omit[-1]
            
if __name__ == '__main__':
      import time
      while True:
            main()
            time.sleep(300)
            print '*' * 125
