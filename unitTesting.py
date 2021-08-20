import unittest
import project as prog

class testProject(unittest.TestCase):

    def test_add(self):
        result = prog.Testing.add(21851470, 17095922, 12740828)
        self.assertEqual(result, 50000000)

    def test_mean(self):
        num = prog.sortTop3Countries
        result = round(prog.Testing.mean(num), 1)
        self.assertEqual(result, 17229406.7)