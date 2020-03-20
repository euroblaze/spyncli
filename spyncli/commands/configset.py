from .base import Base

class Configset(Base):
    """Configuration Set Class!"""

    @property
    def run(self):

        import requests
        import json
        from environs import Env

        env = Env()
        env.read_env()
        API = env.str("API")
        auth_username = env.str("auth_username")
        auth_password = env.str("auth_password")

        if self.options['read']:
            if not self.options['--id'] and not self.options['--name']:
                response = requests.get(API + "configsets/",
                                        auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())
            if self.options['--id']:
                response = requests.get(API + "configsets/%s/" % self.options['--id'],
                                        auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())
            if self.options['--name']:
                response = requests.get(API + "configsets/%s/" % self.options['--name'],
                                        auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())

        if self.options['delete']:
            response = requests.delete(API + "configsets/remove/%s/" % self.options['<id>'],
                                       auth=(auth_username, auth_password))
            print(response.status_code, response.content.decode())

        if self.options['create']:
            headers = {'Content-type': 'application/json'}
            data = {'name': self.options['<name>'],
                    'url': list(self.options['--url']),
                    'username': list(self.options['--usr']),
                    'password': list(self.options['--pwd']),
                    'branch': list(self.options['--b']),
                    'module': list(self.options['--name'])}
            response = requests.post(API + "configsets/insert",
                                     auth=(auth_username, auth_password),
                                     data=json.dumps(data),
                                     headers=headers)
            print(response.status_code, response.content.decode())
