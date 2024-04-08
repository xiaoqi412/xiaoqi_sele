from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# driver.get("http://www.cnblogs.com/surewing")
#
# # 判断title完全等于，返回布尔值
# title = EC.title_is("cherry小樱桃 - 博客")
# print(title(driver))
#
# # 判断title包含
# title = EC.title_contains("cherry小樱桃 - 博客")
# print(title(driver))

# 判断元素value属性
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# locator =("id","s_username_top")
# text ="百度一下，你就知道"
# result = EC.text_to_be_present_in_element_value(locator,text)
# print(result)


driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
locator =("id","kw")
text ="百度一下，你就知道"
result = EC.text_to_be_present_in_element(locator,text)
print(result)


