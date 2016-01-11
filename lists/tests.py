from django.test import TestCase

# Create your tests here.

# 故意编写一个会失败的愚蠢的测试
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)