# 抖音分享页面数据爬取
    
    ![抖音分享页面](/src/douyin/ resource/20190807.png)

## 主要难点:
1. 页面上的数字反爬

## 解决方式:
1. 获取分享页面所使用的字体文件.
2. 使用python库`fontTools`与[百度字体编辑器](http://fontstore.baidu.com/static/editor/index.html)分析字体文件.
3. 从上步骤中解析出数字映射表,可参考`util.py`下的`gen_code_map`方法.

## 使用Python3运行/测试:
1. 进入项目下的douyin文件夹.
2. ```pip install -r resource/requirements.txt```,如安装太慢请使换国内源.
3. ```python douyin_share_page.py```,查看控制台输出.
