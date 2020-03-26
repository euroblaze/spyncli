from .base import Base


class Clones(Base):
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
            if not self.options['--id'] and not self.options['--name']:
                response = requests.get(API + "clouds/clones", auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())
            elif self.options['--id']:
                response = requests.get(API + "clouds/clones/%s" % self.options['--id'], auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())
            elif self.options['--name']:
                response = requests.get(API + "clouds/clones/%s" % self.options['--name'], auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())

	if self.options['delete']:
		response = requests.get(API + "clouds/clones/remove/%s" % self.options['<id>'], auth=(auth_username, auth_password))
		print(response.status_code, response.content.decode())

