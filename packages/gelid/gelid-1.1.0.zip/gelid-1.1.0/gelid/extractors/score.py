# -*- coding: UTF-8 -*-
# lvjiyong on 2015/4/26.

# -*- coding: UTF-8 -*-
# lvjiyong on 2015/4/3.
import math
import re
import time
import jieba
import six
from gelid.extractors import html


class Score(object):
    """
    临时用于计分的，算法以新闻内容结合个人喜好进行评分
    """

    def __init__(self, article):
        content = article['content']
        self.article = article
        self.html = content  # .encode('utf-8')
        # 中文
        self.zh_text = None
        # 中文字数
        self.zh_count = 0
        # 图片数
        self.pic_count = 0
        # 段落数
        self.p_count = 0
        # 排名
        self.search_rank = 1
        # 网站指数
        self.site_rank = 1
        # 时间相关度，如果有时间date_rank= date - now = day，相关度-date_rank
        self.date_rank = 1
        # title相关度，以标题关键词出现次数为rank
        self.title_rank = 0

        self.default_rank = 0
        if content:
            self.default_rank = 0
            self.calculate()
        else:
            self.default_rank = -999999999

    def set_title_rank(self, title, keyword):
        """
        统计标题与关键词匹配分
        :param title:
        :param keyword:
        :return:
        """
        if not title and not self.html:
            self.title_rank = 0
        else:
            title = title.lower()
            keyword = keyword.lower()
            _rank = -2
            seg_title = jieba.cut(title)
            title_list = [t for t in seg_title]
            title_list = set(title_list)
            seg_keyword = jieba.cut(keyword)
            keyword_list = [t for t in seg_keyword]
            keyword_list = set(keyword_list)
            for k in keyword_list:
                for t in title_list:
                    if len(k) > 1 and k in t:
                        _rank += 2
            _rank *= 1.200
            self.title_rank = _rank

    def calculate(self):
        """
        计算所有得分
        :return:
        """
        timestamp = self.article.get('posted_date')
        if timestamp:
            if isinstance(timestamp, six.integer_types):
                timestamp = float(timestamp)
            if isinstance(timestamp, float):
                self.set_date_rank(timestamp)
        self.set_zh_count()
        self.set_p_count()
        self.set_pic_count()
        title = self.article.get('title')
        keyword = self.article.get('keyword')
        if title and keyword:
            self.set_title_rank(title, keyword)

    def set_date_rank(self, timestamp):
        """
        计算时间分
        :param timestamp:
        :return:
        """
        if timestamp is None or timestamp == 0:
            self.date_rank = 0
        else:
            self.date_rank = (time.time() - timestamp) / 60.000 * 60 * 24

    def set_p_count(self):
        """
        通过P含量计处得分，暂未使用，将来将使用p量与每p文字量综合计算得分
        :return:
        """
        pattern = "<p"
        result = re.findall(pattern, self.html, re.I | re.M)
        self.p_count = len(result) * 1.000

    def set_pic_count(self):
        """
        计算图片得分
        :return:
        """
        result = html.images(self.html)
        self.pic_count = len(result) * 1.000

    def set_zh_count(self):
        """
        计算中文字得分
        :return:
        """
        pattern = u"[^\u4e00-\u9fa5]+"
        pattern = re.compile(pattern, re.I | re.M)
        result = re.sub(pattern, '', self.html)
        seg_list = jieba.cut(result)
        b = [s for s in seg_list]
        a = set(b)
        result = "".join(a)
        self.zh_text = result
        self.zh_count = len(self.zh_text) * 1.000

    @property
    def rank(self):
        """
        获取得分
        :return:
        """
        if self.default_rank < 0:
            return self.default_rank
        zh_score = math.sqrt(self.zh_count * 5)
        pic_score = math.sqrt(self.pic_count) * 20
        p_score = 0  # math.sqrt(self.p_count) * 5
        search_score = math.sqrt(self.search_rank) * 10
        site_score = math.sqrt(self.site_rank) * 10

        date_score = - math.sqrt((math.log10(self.date_rank + 1) + 1)) * 10
        title_score = self.title_rank * 10
        rank_score = zh_score + pic_score + p_score + site_score + search_score + date_score + title_score
        return rank_score


def rank(articles):
    """
    批量计算文章，并以得分高低输出
    :param articles:
    :return:
    """
    ranks = [(article, Score(article).rank) for article in articles]
    ranks = sorted(ranks, key=lambda _rank: _rank[1], reverse=True)
    return ranks




