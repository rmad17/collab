# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Model operations are performed here
"""

from pymongo import MongoClient


def add_text():
    client = MongoClient()
    db = client.test_database
    collection = db.test_collection
