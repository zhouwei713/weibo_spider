# coding = utf-8
"""
@author: zhou
@time:2019/7/31 19:46
@File: weibo_spider.py
"""

import requests
from bs4 import BeautifulSoup
import config
import time
from tools import checkTime, get_blog_info
import json
import pandas as pd


class WeiBo(object):

    def __init__(self, name, headers):
        self.name = name
        self.headers = headers

    def get_uid(self):
        try:
            url = 'https://s.weibo.com/user?q=%s' % self.name
            print(url)
            res = requests.get(url, headers=self.headers).text
            content = BeautifulSoup(res, 'html.parser')
            user = content.find('div', attrs={'class': 'card card-user-b s-pg16 s-brt1'})
            user_info = user.find('div', attrs={'class': 'info'}).find('div')
            href_list = user_info.find_all('a')
            if len(href_list) == 3:
                title = href_list[1].get('title')
                if title == '微博个人认证':
                    uid = href_list[2].get('uid')
                    return uid
                elif title == '微博会员':
                    uid = href_list[2].get('uid')
                    return uid
                elif title == '微博官方认证':
                    uid = href_list[2].get('uid')
                    return uid
            else:
                print("There are something wrong")
                return False
        except:
            raise

    def get_userinfo(self, uid):
        print(uid)
        try:
            url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=%s' % uid
            res = requests.get(url).json()
            containerid = res['data']['tabsInfo']['tabs'][1]['containerid']
            mblog_counts = res['data']['userInfo']['statuses_count']
            followers_count = res['data']['userInfo']['followers_count']
            userinfo = {
                "containerid": containerid,
                "mblog_counts": mblog_counts,
                "followers_count": followers_count
            }
            return userinfo
        except:
            raise

    def get_blog_by_page(self, containerid, page, name):
        print('containerid: ', containerid)
        blog_list = []
        if page > 50:
            print("页数不能大于50")
            return False
        try:
            for i in range(page):
                url = 'https://m.weibo.cn/api/container/getIndex?containerid=%s&page=%s' % (containerid, i)
                res = requests.get(url, headers=self.headers).json()
                cards = res['data']['cards']
                try:
                    for j in range(len(cards)):
                        print("-----正在爬取第" + str(i) + "页，第" + str(j + 1) + "条微博------")
                        blog_dict = get_blog_info(cards, j, name, i)
                        blog_list.append(blog_dict)
                except:
                    raise
            return blog_list

        except:
            raise

    def get_blog_by_text(self, containerid, blog_text, name):
        print('containerid: ', containerid)
        blog_list = []
        page = 1
        while True:
            try:
                url = 'https://m.weibo.cn/api/container/getIndex?containerid=%s&page=%s' % (containerid, page)
                res_code = requests.get(url).status_code
                if res_code == 418:
                    print("访问太频繁，过会再试试吧")
                    return False
                res = requests.get(url).json()
                cards = res['data']['cards']
                print('page', page)
                print('cards: ', cards)
                if len(cards) > 0:
                    for i in range(len(cards)):
                        print("-----正在爬取第" + str(page) + "页，第" + str(i+1) + "条微博------")
                        blog_dict = get_blog_info(cards, i, name, page)
                        if blog_dict is False:
                            continue
                        blog_list.append(blog_dict)
                        mblog_text = blog_dict['mblog_text']
                        create_time = blog_dict['create_time']
                        if blog_text in mblog_text:
                            print("成功找到相关微博")
                            return blog_dict['mblog_id']
                        elif checkTime(create_time, config.day) is False:
                            print("在配置的时间内没有找到相关微博")
                            return blog_list
                        time.sleep(config.sleep_time)
                    page += 1
                    time.sleep(config.sleep_time)
                else:
                    print("没有任何微博哦！")
                    break

            except:
                pass

    def get_comment(self, mblog_id, page):
        comment = []
        for i in range(0, page):
            print("-----正在爬取第" + str(i) + "页评论")
            url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id=%s&page=%s' % (mblog_id, i)
            req = requests.get(url, headers=self.headers).text
            html = json.loads(req)['data']['html']
            content = BeautifulSoup(html, "html.parser")
            comment_text = content.find_all('div', attrs={'class': 'WB_text'})
            for c in comment_text:
                _text = c.text.split("：")[1]
                comment.append(_text)
            time.sleep(config.sleep_time)

        return comment

    def download_comment(self, comment):
        comment_pd = pd.DataFrame(columns=['comment'], data=comment)
        timestamp = str(int(time.time()))
        comment_pd.to_csv(timestamp + 'comment.csv', encoding='utf-8')

    def download_pic(self):
        pass


if __name__ == '__main__':
    pass

