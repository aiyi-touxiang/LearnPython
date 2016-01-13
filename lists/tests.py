from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from .views import home_page

# Create your tests here.

# 故意编写一个会失败的愚蠢的测试


class HomePage(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homePage_returns_correct_html(self):
        # 创建了一个HttpRequest对象,用户在浏览器中请求网页时,Django看到的就是HttpRequest对象
        request = HttpRequest()
        # 把这个HttpRequest对象传给home_page视图,得到响应
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
