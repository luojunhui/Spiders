# coding:utf-8
import re

from fontTools.ttLib import TTFont


def gen_code_map(ttf_file):
    """
         字体转数字,
         字体文件: https://s3.pstatp.com/ies/resource/falcon/douyin_falcon/static/font/iconfont_9eb9a50.woff
         在线打开字体文件: http://fontstore.baidu.com/static/editor/index.html
         查看对应的num_x的值,num_map字典根据上一步骤确定值
     :ttf_file: 字体文件路径
     :return: font2num_map 字符映射字典
     """
    num_map = {
        'num_': '1',
        'num_1': '0',
        'num_2': '3',
        'num_3': '2',
        'num_4': '4',
        'num_5': '5',
        'num_6': '6',
        'num_7': '9',
        'num_8': '7',
        'num_9': '8',
    }
    # 解析字体库font文件
    font = TTFont(ttf_file)
    bestCmap = font['cmap'].tables[0].ttFont.getBestCmap()
    font2num_map = {}
    for key in bestCmap:
        _ = '&{};'.format(hex(key).replace('0xe', '#xe'))
        font2num_map[_] = num_map.get(bestCmap[key], '')
    return font2num_map


def re_get_group_text(pattern, string):
    """
        使用正则获取内容
    :param pattern: Pattern,必须有分组
    :param string: 匹配的文本
    :return: 去空格后的文本,无匹配内容返回空字符串
    """
    _ = re.search(pattern, string)
    if _:
        return _.group(1).replace(' ', '')
    return ''
