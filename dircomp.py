import sys
import os
import logging
import hashlib
import itertools

BY_CONTENT = True

LOGGING_FORMAT = '[%(levelname)s] %(asctime)-15s (%(module)s, %(lineno)s, %(funcName)s): %(message)s'
logging.basicConfig(format=LOGGING_FORMAT)
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)


def hash_of_content(path):
    hasher = hashlib.sha1()
    hasher.update(open(path, 'rb').read())
    return hasher.hexdigest()


class Entry(object):
    def __init__(self, path):
        self.name = os.path.basename(path)
        self.path = path
        self.size = os.path.getsize(path)
        self._content_hash = None
        #self._content_hash = self.content_hash()
        self.key = None
    def key(self):
        if self.key is not None:
            return self.key

        if BY_CONTENT:
            self.key = (self.content_hash(), self.size)
        else:
            self.key = (self.name, self.size)

        return self.key

    def content_hash(self):
        if  self._content_hash is None:
            self._content_hash = hash_of_content(self.path)
        return self._content_hash

    def __eq__(self, other):
        if BY_CONTENT:
            # making use of short circuit
            return self.size == other.size and self.content_hash() == other.content_hash()
        else:
            return self.size == other.size and self.name == other.name

    def __str__(self):
        return '%s (%d bytes%s)' % (self.path, self.size, ', sha1: ' + self._content_hash if self._content_hash is not None else '')


def scan_dir(path):
    # logger = logging.getLogger(__name__)
    # logger.setLevel(logging.INFO)

    s = []
    for root, dirs, files in os.walk(path):
        logger.info('root = %s; dirs = %s; files = %s', root, dirs, files)
        for fname in files:
            filepath = os.path.join(root, fname)
            #logger.info('analyzing %s', filepath)
            e = Entry(filepath)
            logger.info('New entry: %s', e)
            s.append(e)

    s.sort(key = Entry.key)
    return {key : list(l) for key, l in itertools.groupby(s, key = Entry.key)}

def analyze(dic1, dic2):
    both, only1, only2 = [], [], []
    for key, l in dic1.iteritems():
        # logger.debug("%s %s", key, map(str, l))
        if key in dic2:
            both.append((key, l + dic2[key]))
        else:
            only1.append((key, l))
    for key, l in dic2.iteritems():
        if key not in dic1:
            only2.append((key, l))
    return (both, only1, only2)


def print_result_list(res):
    for key, l in res:
        # print '\t', key, ':'
        for e in l:
            print '\t\t%s' % e.path

if __name__ == '__main__':
    try:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    except IndexError, e:
        logger.critical('Two folders must be specified')
        exit(0)

    logger.info('DIR 1: %s', dir1)
    logger.info('DIR 2: %s', dir2)


    logger.info('Scanning DIR 1 (%s)', dir1)
    data1 = scan_dir(dir1)
    logger.info('Scanned DIR 1 (%s)', dir1)

    logger.info('Scanning DIR 2 (%s)', dir2)
    data2 = scan_dir(dir2)
    logger.info('Scanned DIR 2 (%s)', dir2)

    logger.info('Analyzing folders....')
    both, only1, only2 = analyze(data1, data2)
    logger.info('Analysis finished.')

    print 'On both sides:'
    print_result_list(both)
    print 'Only in DIR 1 (%s)' % dir1
    print_result_list(only1)
    print 'Only in DIR 2 (%s)' % dir2
    print_result_list(only2)







