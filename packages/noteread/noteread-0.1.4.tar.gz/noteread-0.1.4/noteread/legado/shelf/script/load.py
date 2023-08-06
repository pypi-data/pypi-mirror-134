import json
import os
from datetime import datetime, timedelta

from notedrive.others.github.utils import (all_file_to_github,
                                           upload_data_to_github)
from noteread.legado.shelf.base import BookSource, BookSourceCorrect
from notetool.tool.pyrss import RSS2, RSSItem

book = BookSource(lanzou_fid=4147049)
book_correct = BookSourceCorrect(lanzou_fid=4147049)


def load():
    urls = [

        "https://cdn.jsdelivr.net/gh/bushixuanqi/book-source/%E5%85%A8%E7%BD%91%E9%80%9A%E7%94%A8.json",
        "https://cdn.jsdelivr.net/gh/bushixuanqi/book-source/%E4%B9%A6%E6%BA%90%E5%90%88%E9%9B%86.json",

        "https://gitee.com/z507525872/book-source/raw/master/32yousheng.json",
        "https://gitee.com/jia_to_hui/read-30-preferred-book-source/raw/master/bookSource.json",
        "https://guaner001125.coding.net/p/coding-code-guide/d/booksources/git/raw/master/sources/guaner.json",
        "https://haxc.coding.net/p/booksrc/d/booksrc/git/raw/master/Book3.0Source.json",
        "https://haxc.coding.net/p/booksrc/d/booksrc/git/raw/master/bookSource.json",

        "https://namofree.gitee.io/yuedu3/legado3_booksource_by_Namo.json",
        "https://no-mystery.gitee.io/shuyuan/%E5%85%A8%E7%BD%91%E9%80%9A%E7%94%A8.json",
        "https://olixina.coding.net/p/yuedu/d/source/git/raw/master/bookSource.json",
        "https://pbpobing.coding.net/p/yueduyuan/d/sy/git/raw/master/syhj.json",
        "https://pbpobing.coding.net/p/yueduyuan/d/sy/git/raw/master/yshj.json",
        "https://pbpobing.coding.net/p/yueduyuan/d/sy/git/raw/master/3syhj.json",
        "https://pbpobing.coding.net/p/yueduyuan/d/sy/git/raw/master/3yshj.json",

        "https://shuyuan.miaogongzi.site/shuyuan/1612930793.txt",
        "https://shuyuan.miaogongzi.site/shuyuan/1615385692.txt",
        "https://shuyuan.miaogongzi.net/shuyuan/1617076136.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1617281456.json",

        "https://shuyuan.miaogongzi.net/shuyuan/1617406392.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1619463469.txt",
        "https://shuyuan.miaogongzi.net/shuyuan/1619872864.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1619911647.txt",
        "https://shuyuan.miaogongzi.net/shuyuan/1619967369.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1620929243.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1622744487.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1623355431.json",

        "https://shuyuan.miaogongzi.net/shuyuan/1624832786.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1622509629.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1626191885.txt",
        "https://shuyuan.miaogongzi.net/shuyuan/1626711440.json"
        "https://shuyuan.miaogongzi.net/shuyuan/1626966311.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1627802706.txt",
        "https://shuyuan.miaogongzi.net/shuyuan/1630342495.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1631138099.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1632140979.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1633030418.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1633826458.json",
        "https://shuyuan.miaogongzi.net/shuyuan/1630342495.json",

        "https://slaijie.gitee.io/legado/legado/BookSource210116.json",
        "https://tangguochaotian.coding.net/p/tangguoshuyuan1015/d/tangguo/git/raw/master/exportBookSource.json",
        "https://tianyuzhange.coding.net/p/booksource/d/shuyuan/git/raw/master/2.0shuyuan.json",

        "https://gitee.com/ch4nge/readbook/raw/master/booksource_fl",

        "https://gitee.com/ch4nge/readbook/raw/master/booksource200",
        "https://gitee.com/ch4nge/readbook/raw/master/booksource40",
        "https://gitee.com/YiJieSS/Yuedu/raw/master/bookSource.json",
    ]
    from noteread.legado.shelf.libs.core import load_from_url
    load_from_url(cate1='1', urls=urls, book=book)


def upload_version(cate1='1', repo='notechats/notefile', git_dir='notechats/noteread/data', split_num=1000, num=10):
    datas = book_correct.select(condition={'cate1': cate1})

    dd = datetime.now().strftime('%Y%m%d%H%M%S')
    for i in range(num):
        data = datas[i * split_num:(i + 1) * split_num]
        data = [json.loads(d['jsons']) for d in data]
        data = json.dumps(data)

        git_path = f"{git_dir}/legado-source-{dd}-{i}.json"
        upload_data_to_github(data, git_path, repo)


def data2xml(repo='notechats/notefile', git_dir='notechats/noteread'):
    files = all_file_to_github(os.path.join(git_dir, 'data'), repo_str=repo)
    files = sorted(files, key=lambda x: x, reverse=True)

    items = []
    for _file in files:
        res = os.path.basename(_file).split('.')[0].split('-')
        date = datetime.strptime(res[2], '%Y%m%d%H%M%S') + timedelta(seconds=int(res[3]))

        # github:
        link = f'http://www.baidu.com?wd=yuedu://rsssource/importonline?src=https://raw.githubusercontent.com/{repo}/master/file'
        # "gitee":
        # link = f'https://gitee.com/{repo}/raw/master/file'
        item = RSSItem(
            title=os.path.basename(_file),
            link=link,
            description=_file,
            # guid=PyRSS2Gen.Guid("https://github.com/notechats/notefile/tree/master/notechats/noteread"),
            pubDate=date)
        items.append(item)

    rss = RSS2(
        title="yuedu feed",
        link="https://github.com/notechats/notefile/tree/master/notechats/noteread",
        description="阅读的书源",
        lastBuildDate=datetime.now(),
        items=items)

    res = rss.to_xml(encoding='UTF-8')
    git_path = f"{git_dir}/legado-source.xml"

    upload_data_to_github(res, git_path, repo)


# load()
# correct_source(book, book_correct)
# book.db_save()
print(len(book.select_all()))
print(len(book_correct.select_all()))

# upload_version(cate1='1')
data2xml()
