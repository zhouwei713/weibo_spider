# coding = utf-8
"""
@author: zhou
@time:2019/8/1 10:32
@File: tools.py
"""

import datetime
from config import day


def checkTime(inputtime, day):
    try:
        intime = datetime.datetime.strptime("2019-" + inputtime, '%Y-%m-%d')
    except:
        return "时间转换失败"

    now = datetime.datetime.now()
    n_days = now - intime
    days = n_days.days
    if days < day:
        return True
    else:
        return False


def get_blog_info(cards, i, name, page):
    blog_dict = {}
    print('card_type: ', cards[i]['card_type'])
    if cards[i]['card_type'] == 9:
        scheme = cards[i]['scheme']  # 微博地址
        mblog = cards[i]['mblog']
        mblog_text = mblog['text']
        create_time = mblog['created_at']
        mblog_id = mblog['id']
        reposts_count = mblog['reposts_count']  # 转发数量
        comments_count = mblog['comments_count']  # 评论数量
        attitudes_count = mblog['attitudes_count']  # 点赞数量
        with open(name, 'a', encoding='utf-8') as f:
            f.write("----第" + str(page) + "页，第" + str(i + 1) + "条微博----" + "\n")
            f.write("微博地址：" + str(scheme) + "\n" + "发布时间：" + str(create_time) + "\n"
                    + "微博内容：" + mblog_text + "\n" + "点赞数：" + str(attitudes_count) + "\n"
                    + "评论数：" + str(comments_count) + "\n" + "转发数：" + str(reposts_count) + "\n")
        blog_dict['mblog_id'] = mblog_id
        blog_dict['mblog_text'] = mblog_text
        blog_dict['create_time'] = create_time
        return blog_dict
    else:
        print("没有在card中发现任何微博")
        return False


if __name__ == '__main__':
    a = checkTime("3-5", day)
    print(a)
