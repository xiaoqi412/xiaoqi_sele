import requests,jsonpath


公共参数 = {
    "application": "app",
    "applicaiton_client_type": "weixin"
}

请求参数 = {
    "accounts": "huace_xm",
    "pwd": 123456,
    "type": "username"
}


login = requests.request(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",
                        method="POST",
                        params=公共参数,
                        data=请求参数) # 发一个请求出去
print(login.text)
token = login.json()["data"]["token"]
print(token)
tokens = jsonpath.jsonpath(login.json(), "$..token")
print(tokens[0])





加入购物车 = {
    "goods_id":"3",
	"stock":"2",
    "spec": [
        {
            "type": "套餐",
            "value": "套餐二"
        },
        {
            "type": "颜色",
            "value": "银色"
        },
        {
            "type": "容量",
            "value": "64G"
        }
    ]
}

shopping = requests.request(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/save&token="+tokens[0],
                        method="POST",
                        params=公共参数,
                        data=加入购物车)
print(shopping.url)
print(shopping.text)
