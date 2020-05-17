import requests


class DouBanLogin(object):
    def __init__(self, account, password):
        self.url = "https://accounts.douban.com/passport/login"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
            'Referer': 'https://accounts.douban.com/passport/login',
            'Host': 'accounts.douban.com',
            'Origin': 'https://accounts.douban.com',
        }
        self.data = {
            # "ck": "",
            "name": account,
            "password": password,
            "remember": "false"
            # "ticket": ""
        }
        self.session = requests.Session()

    def get_cookie(self):
        html = self.session.post(url=self.url, headers=self.headers, data=self.data)
        print(html.text)

    def get_user_data(self):
        """
       今天触发反爬了，回头看看为什么
       如果返回信息就成功
       :return:
       """
        url = "https://www.douban.com/people/207378789/"
        html = self.session.get(url).text
        print(html)

    def run(self):
        """运行程序"""
        self.get_cookie()
        self.get_user_data()


if __name__ == '__main__':
    account = input("请输入你的账号:")
    password = input("请输入你的密码:")
    login = DouBanLogin(account, password)
    login.run()
