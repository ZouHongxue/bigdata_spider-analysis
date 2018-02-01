# -*- coding: UTF-8 -*-

import json
import logging as info
# '''
# json转对象
# '''
#
# with open('../../../spider/douban/douban/spiders/hotSpot.txt', 'a+') as f:
#     for line in f:
#         hotSpot = HotSpot()
#         value = json.loads(line)
#         hotSpot.__dict__ = value
#         print hotSpot['brief']
import time

'''
获取当前时间
'''

print time.strftime('%Y-%m-%d',time.localtime(time.time()))

info.basicConfig(
    level=info.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='mysql_info.log',
    filemode='a+'
)

info.info('test')