# Copyright 2020 Jarred Vardy <vardy@riseup.net>
#
# This file is part of DemocracyBot.
#
# DemocracyBot is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DemocracyBot is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DemocracyBot. If not, see http://www.gnu.org/licenses/.

import unittest

from test_test import TestTestCase


def run_tests():
    tests = [TestTestCase]
    loader = unittest.TestLoader()
    all_suites = []
    for test in tests:
        suite = loader.loadTestsFromTestCase(test)
        all_suites.append(suite)

    macro_test_suite = unittest.TestSuite(all_suites)
    test_runner = unittest.TextTestRunner()
    results = test_runner.run(macro_test_suite)


if __name__ == "__main__":
    run_tests()
