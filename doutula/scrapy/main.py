#!/usr/bin/env python
# encoding: utf-8

"""
@description: run spider

@author: BaoQiang
@time: 2017/5/16 12:38
"""

from scrapy import cmdline


def run_spider():
    cmdline.execute('scrapy crawl doutula_spider'.split())


def main():
    run_spider()


if __name__ == '__main__':
    main()
