import re
import getpass
import requests


class GithubLogin(object):

    def __init__(self, email, password):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'https://github.com/',
            'Host': 'github.com'
        }

        self.session = requests.Session()
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.email = email
        self.password = password

    def login_Github(self):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token(),
            'login': self.email,
            'password': self.password
        }
        response = self.session.post(
            self.post_url, data=post_data, headers=self.headers
        )

        print('StatusCode:', response.status_code)
        if response.status_code != 200:
            print('Login fail')
        match = re.search(r'"user-login" content="(.*?)"', response.text)
        user_name = match.group(1)
        print('UserName:', user_name)

    def get_token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        if response.status_code != 200:
            print('Get token fail')
            return None
        match = re.search(
            r'name="authenticity_token" value="(.*?)"', response.text
        )
        if not match:
            print('Get Token fail')
            return None
        return match.group(1)


if __name__ == '__main__':
    email = input('Account:')
    password = input('Password:')
    login = GithubLogin(email, password)
    login.login_Github()
