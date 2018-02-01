# -*- coding: UTF-8 -*-

import json
from items import HotSpot

'''
json转对象
'''

with open('../../../spider/douban/douban/spiders/hotSpot.txt', 'a+') as f:
    for line in f:
        hotSpot = HotSpot()
        value = json.loads(line)
        hotSpot.__dict__ = value
        print hotSpot['brief']
