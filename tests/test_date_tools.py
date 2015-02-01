import unittest
from datetime import datetime

import pyhelpers.date_tools as date_tools

class LengthOfTimeCalc(unittest.TestCase):

    def test_should_return_1_year_and_0_months(self):
        start_date = datetime(2001,1,1)
        end_date = datetime(2002,1,1)

        years, months = date_tools.get_length_of_time(start_date, end_date)

        self.assertEqual(years, 1, msg="Years should = 1")
        self.assertEqual(months, 0, msg="Months should = 0")

    def test_should_return_2_years_and_4_months(self):
        start_date = datetime(2001,1,1)
        end_date = datetime(2003,5,1)
        years, months = date_tools.get_length_of_time(start_date, end_date)

        self.assertEqual(years, 2, msg="Years should = 1")
        self.assertEqual(months, 4, msg="Months should = 0")

    def test_start_and_end_date_are_equal_should_return_0_0(self):
        start_date = datetime(2001,1,1)
        end_date = datetime(2001,1,1)
        years, months = date_tools.get_length_of_time(start_date, end_date)

        self.assertEqual(years, 0, msg="Years should = 0")
        self.assertEqual(months, 0, msg="Months shold = 0")

    def test_raise_execption_if_start_date_is_greater_than_end_date(self):

        start_date = datetime(2001,1,1)
        end_date = datetime(2000,1,1)

        with self.assertRaises(Exception):
            years, months = date_tools.get_length_of_time(start_date, end_date=end_date)

if __name__ == '__main__':
    unittest.main()
