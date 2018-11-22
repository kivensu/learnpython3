# -*- coding: utf-8 -*-
# @Author: kivensu
# @Date:   2018-11-21 15:55:42
# @Last Modified by:   kivensu
# @Last Modified time: 2018-11-21 15:55:42
# @Email: 749243884@qq.com
import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        format_name = get_formatted_name('lisa', 'wang')
        self.assertEqual(format_name, 'Lisa Wang')


unittest.main()
