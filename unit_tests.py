#!/usr/bin/env python

import unittest
from pyspantask import calculate_score

class TestTask(unittest.TestCase):

  def test_calculate_score(self):
    # Perfect match:
    self.assertEqual(calculate_score(["AA", "BB", "CC", "DD"], ["AA", "BB", "CC", "DD"], False, False), 4)
    self.assertEqual(calculate_score(["AA", "BB", "CC", "DD"], ["AA", "BB", "CC", "DD"], False, True), 4)
    self.assertEqual(calculate_score(["AA", "BB", "CC", "DD"], ["AA", "BB", "CC", "DD"], True, False), 4)
    self.assertEqual(calculate_score(["AA", "BB", "CC", "DD"], ["AA", "BB", "CC", "DD"], True, True), 4)

    # Order violated:
    self.assertEqual(calculate_score(["BB", "AA", "CC", "DD"], ["AA", "BB", "CC", "DD"], False, False), 4)
    self.assertEqual(calculate_score(["BB", "AA", "CC", "DD"], ["AA", "BB", "CC", "DD"], False, True), 2)
    self.assertEqual(calculate_score(["BB", "AA", "CC", "DD"], ["AA", "BB", "CC", "DD"], True, False), 4)
    self.assertEqual(calculate_score(["BB", "AA", "CC", "DD"], ["AA", "BB", "CC", "DD"], True, True), 2)

    # Typos:
    self.assertEqual(calculate_score(["AA", "BX", "CC", "DD"], ["AA", "BB", "CC", "DD"], False, False), 3)
    self.assertEqual(calculate_score(["AA", "BX", "CC", "DD"], ["AA", "BB", "CC", "DD"], False, True), 3)
    self.assertEqual(calculate_score(["AA", "BX", "CC", "DD"], ["AA", "BB", "CC", "DD"], True, False), 4)
    self.assertEqual(calculate_score(["AA", "BX", "CC", "DD"], ["AA", "BB", "CC", "DD"], True, True), 4)

    # Order violated and typos:
    self.assertEqual(calculate_score(["BB", "AA", "CC", "DX"], ["AA", "BB", "CC", "DD"], False, False), 3)
    self.assertEqual(calculate_score(["BB", "AA", "CC", "DX"], ["AA", "BB", "CC", "DD"], False, True), 1)
    self.assertEqual(calculate_score(["BB", "AA", "CC", "DX"], ["AA", "BB", "CC", "DD"], True, False), 4)
    self.assertEqual(calculate_score(["BB", "AA", "CC", "DX"], ["AA", "BB", "CC", "DD"], True, True), 2)

    # Order violated and typos and too many responses:
    self.assertEqual(calculate_score(["XX", "BB", "AA", "CC", "DX"], ["AA", "BB", "CC", "DD"], False, False), 3)
    self.assertEqual(calculate_score(["XX", "BB", "AA", "CC", "DX"], ["AA", "BB", "CC", "DD"], False, True), 1)
    self.assertEqual(calculate_score(["XX", "BB", "AA", "CC", "DX"], ["AA", "BB", "CC", "DD"], True, False), 4)
    self.assertEqual(calculate_score(["XX", "BB", "AA", "CC", "DX"], ["AA", "BB", "CC", "DD"], True, True), 2)

    # Corner case: empty lists
    self.assertEqual(calculate_score([], ["AA", "BB", "CC", "DD"], False, False), 0)
    self.assertEqual(calculate_score([], ["AA", "BB", "CC", "DD"], False, False), 0)
    self.assertEqual(calculate_score([], ["AA", "BB", "CC", "DD"], False, True), 0)
    self.assertEqual(calculate_score([], ["AA", "BB", "CC", "DD"], True, False), 0)

    self.assertEqual(calculate_score(["AA", "BB", "CC", "DD"], [], True, True), 0)
    self.assertEqual(calculate_score(["AA", "BB", "CC", "DD"], [], False, True), 0)
    self.assertEqual(calculate_score(["AA", "BB", "CC", "DD"], [], True, False), 0)
    self.assertEqual(calculate_score(["AA", "BB", "CC", "DD"], [], True, True), 0)

if __name__ == '__main__':
    unittest.main()
