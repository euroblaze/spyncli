from .base import Base
from os.path import abspath, dirname

class Users(Base):
    """Users Class"""

    @property
    def run(self):

        import requests
        from environs import Env

        env = Env()
        env.read_env()
        API = env.str("API")
        auth_username = env.str("auth_username")
        auth_password = env.str("auth_password")
        dir_path = abspath(dirname(__file__))

        if self.options['login']:
            response = requests.post(API + "user/login/", data={'username': self.options['<username>'],
                                                                'password': self.options['<password>']})
            if response.status_code == 200:
                with open(dir_path+'/.env', 'r') as file:
                    lines = file.readlines()
                    lines[1] = "auth_username=%s\n" % self.options['<username>']
                    lines[2] = "auth_password=%s\n" % self.options['<password>']
                with open(dir_path+"/.env", "w") as file:
                    for line in lines:
                        file.write(line)
            print(response.status_code, response.content.decode())

        if self.options['register']:
            response = requests.post(API + "user/register/", data={'username': self.options['<username>'],
                                                                   'first_name': self.options['<first_name>'],
                                                                   'last_name': self.options['<last_name>'],
                                                                   'email': self.options['<email>'],
                                                                   'password': self.options['<password>'],
                                                                   'confirm_password': self.options['<password>']})
            print(response.status_code, response.content.decode())

        if self.options['update']:
            data = {}
            if self.options['--usr']:
                data['username'] = self.options['--usr']
            if self.options['--name']:
                data['first_name'] = self.options['--name']
            if self.options['--surname']:
                data['last_name'] = self.options['--surname']
            if self.options['--pwd']:
                data['password'] = self.options['--pwd']
            if self.options['--email']:
                data['email'] = self.options['--email']
            response = requests.put(API + "user/", auth=(auth_username, auth_password), data=data)
            print(response.status_code, response.content.decode())

