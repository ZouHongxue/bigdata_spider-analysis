# coding=utf-8

import MySQLdb
import logging
import time

info = logging.getLogger('info')
error = logging.getLogger('error')

info_name = 'log/mysql_info' + time.strftime('%Y%m', time.localtime(time.time())) + '.log'
error_name = 'log/mysql_error' + time.strftime('%Y%m', time.localtime(time.time())) + '.log'

fh = logging.FileHandler(info_name)
fh1 = logging.FileHandler(error_name)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
fh1.setFormatter(formatter)

info.addHandler(fh)
info.setLevel(logging.DEBUG)
error.addHandler(fh1)
error.setLevel(logging.ERROR)

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='php',
    charset='utf8'
)
cur = conn.cursor()


def insertTag(tag):
    sql = "insert tag (tag_name,tag_count,source) values (%s,%s,%s)"
    i = 0
    print tag.tag_count
    try:
        i = cur.execute(sql, (tag.tag_name, tag.tag_count, tag.source))
    except Exception as e:
        error.error('数据库写入标签错误，具体信息：')
        print e
        error.error(e)
    info.info('数据库写入标签')
    print 'insert'
    print i


def commit():
    conn.commit()


def close():
    cur.close()
    conn.close()


def selectTag(tag):
    sql = "select count(*) from tag where tag_name = %s and source = %s"
    i = 0
    try:
        i = cur.execute(sql, (tag.tag_name, tag.source))
    except Exception as e:
        error.error('数据库查找标签错误，具体信息：')
        error.error(e)
    finally:
        info.info('数据库查找标签')
    print 'search'
    count = cur.fetchmany(i)[0][0]
    print count
    return count


def updateTag(tag):
    sql = "update tag set tag_count = tag_count+1 where tag_name = %s and source =%s"
    i = 0
    try:
        i = cur.execute(sql, (tag.tag_name, tag.source))
    except Exception as e:
        error.error('数据库更新标签错误，具体信息：')
        error.error(e)
    info.info('数据库更新标签')
    print 'update'
    print i
