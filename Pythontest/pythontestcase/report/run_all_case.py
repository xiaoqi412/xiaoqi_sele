
import HtmlTestRunner
import unittest

discover = unittest.defaultTestLoader.discover(start_dir="D:\\Pythontest\\pythontestcase\\case\\",
                                               pattern='test*.py',
                                               top_level_dir=None)
# print(discover)

# 文本的报告
# runner = unittest.TextTestRunner()  #返回实例
# runner.run(discover)

# html的报告
reportPath = "D:\\Pythontest\\pythontestcase\\report" + "result.html"
print(reportPath)
file = open(reportPath, "w")
runner = HtmlTestRunner.HTMLTestRunner(stream=file,verbosity=2,descriptions="这个是自动化测试用例")
runner.run(discover)


# reportTitle = "report.html"
# reportPath = "D:\\Pythontest\\pythontestcase\\report\\" + reportTitle


# file.close()

# with open(reportPath, 'wb') as file:
#     runner = HtmlTestRunner.HTMLTestRunner(stream=file)
#     runner.textrun(discover)