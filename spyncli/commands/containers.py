from .base import Base


class Containers(Base):
    """Clones Class"""

    @property
    def run(self):

        import requests
        import os
        from environs import Env

        env = Env()
        env.read_env()
        API = env.str("API")
        auth_username = env.str("auth_username")
        auth_password = env.str("auth_password")

        if self.options['read']:
                response = requests.get(API + "clouds/clones/pods/retrieve/%s" % self.options['<namespace>'], auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())

        if self.options['restart']:
                print(self.options['<namespace>'])
                print(self.options['<name>'])
                response = requests.post(API + "clouds/clones/pods/delete/%s/%s" % (self.options['<namespace>'], self.options['<name>']), auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())


