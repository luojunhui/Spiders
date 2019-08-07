# coding:utf-8
"""
    获取抖音分享页面的信息,如https://www.iesdouyin.com/share/user/66598046050
    share_id 需要事前准备好
    2019年8月7日 测试有效
"""
import datetime
import re

import requests

from util import gen_code_map, re_get_group_text


def main(share_id_arr):
    """
        爬取抖音分享页面的信息
    :param share_id_arr: 分享ID数组
    :return:
    """
    douyin_share_url = 'https://www.iesdouyin.com/share/user/{share_id}'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, "
                      "like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
    }
    font2num_map = gen_code_map('iconfont_9eb9a50.woff')
    for share_id in share_id_arr:
        response = requests.get(url=douyin_share_url.format(share_id=share_id), headers=headers)
        compile = re.compile(r'<i class="icon.*?">(.*?)</i>')
        html_text = response.text
        arr = re.finditer(compile, html_text)
        for row in arr:
            string = row.group()  # 例: <i class="icon iconfont follow-num"> &#xe610; </i>
            key = row.group(1).replace(' ', '')  # 例: &#xe610;
            num_val = font2num_map.get(key, '')
            html_text = html_text.replace(string, num_val)
        item = dict(share_id=share_id)
        item['nickname'] = re_get_group_text(r'<p class="nickname">(.*?)</p>', html_text)
        item['douyin_id'] = re_get_group_text(r'<p class="shortid">抖音ID：(.*?)</p>', html_text)
        item['sign'] = re_get_group_text(r'<p class="signature">(.*?)</p>', html_text)
        item['focus'] = re_get_group_text(r'<span class="focus block"><span class="num">(.*?)'
                                          r'</span><span class="text">关注</span>', html_text)
        item['follower'] = re_get_group_text(r'<span class="follower block"><span class="num">(.*?)'
                                             r'</span><span class="text">粉丝</span>', html_text)
        item['awesome'] = re_get_group_text(r'<span class="liked-num block"><span class="num">(.*?)'
                                            r'</span><span class="text">赞</span>', html_text)
        item['works'] = re_get_group_text(r'作品<span class="num">(.*?)</span>', html_text)
        item['like'] = re_get_group_text(r'喜欢<span class="num">(.*?)</span>', html_text)
        yield item


if __name__ == '__main__':
    share_id_arr = ['66598046050', '95981991280']
    results = main(share_id_arr)
    for item in results:
        info = '''
        昵称:{nickname}
        抖音ID:{douyin_id}
        分享ID:{share_id}
        签名:{sign}
        关注:{focus}
        粉丝:{follower}
        赞:{awesome}
        作品:{works}
        喜欢:{like}'''
        print(info.format(**item))
    print('当前日期:{}'.format(datetime.datetime.now().strftime('%Y-%m-%d')))
