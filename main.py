# coding = utf-8
"""
@author: zhou
@time:2019/7/31 19:18
@File: main.py
"""

from weibo_spider import WeiBo
from config import headers


def main(name, spider_type, text, page, iscomment, comment_page):
    print("开始...")
    weibo = WeiBo(name, headers)
    print("以名字搜索...")
    print("获取 UID...")
    uid = weibo.get_uid()
    print("获取 UID 结束")
    print("获取用户信息...")
    userinfo = weibo.get_userinfo(uid)
    print("获取用户信息结束")
    if spider_type == "Text" or spider_type == "text":
        print("爬取微博...")
        blog_info = weibo.get_blog_by_text(userinfo['containerid'], text, name)
        if isinstance(blog_info, str):
            print("搜索到微博，爬取成功")
            if iscomment == "Yes" or iscomment == "YES" or iscomment == "yes":
                print("现在爬取评论")
                comment_info = weibo.get_comment(blog_info, comment_page)
                weibo.download_comment(comment_info)
                print("评论爬取成功，请查看文件")
                return True
            return True
        else:
            print("没有搜索到微博，爬取结束")
            return False
    elif spider_type == "Page" or spider_type == "page":
        blog_info = weibo.get_blog_by_page(userinfo['containerid'], page, name)
        if blog_info and len(blog_info) > 0:
            print("爬取成功，请查看文件")
            return True
    else:
        print("请输入正确选项")
        return False


if __name__ == '__main__':
    target_name = input("type the name: ")
    spider_type = input("type spider type(Text or Page): ")
    text = "你好"
    page_count = 10
    iscomment = "No"
    comment_page_count = 100
    while spider_type not in ("Text", "text", "Page", "page"):
        spider_type = input("type spider type(Text or Page): ")
    if spider_type == "Page" or spider_type == "page":
        page_count = input("type page count(Max is 50): ")
        while int(page_count) > 50:
            page_count = input("type page count(Max is 50): ")
    elif spider_type == "Text" or spider_type == "text":
        text = input("type blog text for search: ")
        iscomment = input("type need crawl comment or not(Yes or No): ")
        while iscomment not in ("Yes", "YES", "yes", "No", "NO", "no"):
            iscomment = input("type need crawl comment or not(Yes or No): ")
        if iscomment == "Yes" or iscomment == "YES" or iscomment == "yes":
            comment_page_count = input("type comment page count(Max is 1000): ")
            while int(comment_page_count) > 1000:
                comment_page_count = input("type comment page count(Max is 1000): ")
    result = main(target_name, spider_type, text, int(page_count), iscomment, int(comment_page_count))
    if result:
        print("爬取成功！！")
    else:
        print("爬取失败！！")

