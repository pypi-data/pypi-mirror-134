"""
Created on 07/12/2021

@author: antoine
"""
import unittest
from datetime import datetime, timedelta
from graphgenerator.custom_classes.GraphBuilder import GraphBuilder
from graphgenerator.config import tz


class TestGraphBuilder(unittest.TestCase):

    def test_date(self):
        GB = GraphBuilder(
            search="#funny",
            minretweets=1,
            since="2004-10-11",
            maxresults=10
        )
        self.assertEqual(GB.min_date, (datetime.now(tz=tz) - timedelta(days=7)).strftime("%Y-%m-%d"))

