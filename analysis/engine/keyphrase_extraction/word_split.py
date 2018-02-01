# -*- coding: UTF-8 -*-

import datetime
import json

from jieba.analyse import extract_tags
import bean.Tag
import dao.mysql


def getKey(brief):
    tags = extract_tags(brief, 1, True);
    for tag in tags:
        print (brief + "tag: %s\t\t weight: %f" % (tag[0], tag[1]))
        t = bean.Tag
        t.tag_name = tag[0]
        t.tag_count = 1
        t.source = '简书'
        if dao.mysql.selectTag(t) > 0:
            dao.mysql.insertTag(t)
            dao.mysql.commit()
        else:
            dao.mysql.insertTag(t)
            dao.mysql.commit()


def json_to_object(content):
    value = json.loads(content)
    print value['_values']
    getKey(value['_values']['title'])


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
print yesterday
filePath = "../../../collector/spider/spiders/hotSpot/hotSpot_" + yesterday.strftime('%Y-%m-%d') + ".txt"
print filePath
with open(filePath, 'a+') as f:
    for line in f:
        json_to_object(line)
dao.mysql.close()
