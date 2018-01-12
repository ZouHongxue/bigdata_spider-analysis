import jieba
from jieba.analyse import extract_tags

class WordSplit():

    __doc_urls__ = []

    def __init__(self, doc_urls):
        self.__doc_urls__ = doc_urls

    def getKey(self):
        for doc_url in self.__doc_urls__:
            with open(doc_url) as f:
                mytext = f.read()
            tags = extract_tags(mytext, 5, True);
            for tag in tags:
                print (doc_url+"tag: %s\t\t weight: %f" % (tag[0], tag[1]))


doc_urls = ["test.txt", "test2.txt"]
wordsplit = WordSplit(doc_urls)
wordsplit.getKey()