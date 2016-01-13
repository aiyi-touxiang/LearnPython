from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# 测试组织成类的形式,继承自 unittest.TestCase。


class NewVisitorTest(unittest.TestCase):

    # setUp 和 tearDown 是特殊的方法,分别在各个测试方法之前和之后运行。
    # 我使用这两 个方法打开和关闭浏览器。注意,这两个方法有点类似 try/except 语句,
    # 就算测试中 出错了,也会运行 tearDown 方法。1 测试结束后,Firefox 窗口不会一直停留在桌面上了。
    def setUp(self):
        self.browser = webdriver.Chrome('../../chromedriver')
        # 让浏览器等待3秒
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    # 测试的主要代码写在名为 test_can_start_a_list_and_retrieve_it_later 的方法中。
    # 名字以 test_ 开头的方法都是测试方法,由测试运行程序运行。
    # 类中可以定义多个测 试方法。为测试方法起个有意义的名字是个好主意。

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://127.0.0.1:8000')

        # 她注意到网页的标题和头部都包含"To-Do"这个词
        # 使用 self.assertIn 代替 assert 编写测试断言。unittest 提供了很多这种用于编写测 试断言的辅助函数,
        # 如 assertEqual、assertTrue 和 assertFalse 等。更多断言辅助函 数参见 unittest 的文档,
        # 地址是 http://docs.python.org/3/library/unittest.html。
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一个文本框中输入了“Buy peacock feathers(”购买孔雀羽毛)
        # 伊迪丝的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车键后,页面更新了
        # 待办事项表格中显示了“1: Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list-table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # 页面中又显示了一个文本框,可以输入其他的待办事项
        # 她输入了“Use peacock feathers to make a fly(”使用孔雀羽毛做假蝇)
        # 伊迪丝做事很有条理
        self.fail('Finish the test!')

        # 页面再次更新,她的清单中显示了这两个待办事项
        # 伊迪丝想知道这个网站是否会记住她的清单

        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 她访问那个URL,发现她的待办事项列表还在

        # 她很满意,去睡觉了

        # 不管怎样,self.fail 都会失败,生成指定的错误消息。我使用这个方法提醒测试结束了。


# 最后是 if __name__ == '__main__' 分句(如果你之前没见过这种用法,我告诉你,
# Python 脚本使用这个语句检查自己是否在命令行中运行,而不是在其他脚本中导入)。
# 我们调用 unittest.main() 启动 unittest 的测试运行程序,这个程序会在文件中自动 查找测试类和方法,然后运行。
if __name__ == '__main__':
    # warnings='ignore' 的作用是禁止抛出 ResourceWarning 异常。写作本书时这个异常会抛出,
    # 但你阅读时我可能已经把这个参数去掉了。你可以把这个参数删掉,看一下效果。
    unittest.main(warnings='ignore')
