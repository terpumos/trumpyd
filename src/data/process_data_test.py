#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase
from process_data import ProcessData


class TestProcessData(TestCase):
    def setUp(self):
        self.process_data = ProcessData('./test/input/','./test/output/temp_folder/')


    def test___get_csv_names(self):
        names = ['./test/input/subfolder1/test1.json',
                     './test/input/subfolder1/test2.json',
                     './test/input/subfolder2/test3.json',]
        test_names = [name for name in self.process_data.get_csv_names()]
        print(test_names)
        self.assertEqual(len(test_names),3)
        self.assertTrue(all(name in names for name in test_names))


    def tear_down(self):
        pass


if __name__ == "__main__":
    unittest.main()

