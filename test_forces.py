from axisandallies.forces import Forces
import unittest


class ForcesTestCase(unittest.TestCase):

    def setUp(self):
        self.a = Forces(I=2, A=2, F=0, B=0, attacking=True)
        self.d = Forces(I=4, A=0, F=0, B=0, attacking=False)

    def test_total_strength(self):
        self.assertEqual(self.a.total_strength(), 8)


if __name__ == '__main__':
    unittest.main()
