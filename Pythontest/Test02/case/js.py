import time
from selenium import  webdriver

driver = webdriver.Firefox()
driver.get("http://www.people.com.cn/")

time.sleep(1)
tag = driver.find_element("link text","首页")
driver.execute_script("arguments[0].scrollIntoView();",tag)





# 纵向滚动
js1 = "document.documentElement.scrollTop=10000" # python里面是一个字符串
driver.execute_script(js1)

time.sleep(1)
js2 = "document.documentElement.scrollTop=0"
driver.execute_script(js2)

# 横向滚动
js3 = "window.scrollTo(0,10000)"  # 底部
driver.execute_script(js3)
js4 = "window.scrollTo(0,0)"    # 顶部
driver.execute_script(js4)


# 滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
# 滚动到顶部
js5 = "window.scrollTo(0,0)"
driver.execute_script(js5)


