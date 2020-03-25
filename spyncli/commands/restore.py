from .base import Base
from os.path import abspath, dirname

class Restore(Base):
    """Restore Class"""

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

	if self.options['perform']:
		response = requests.post(API + "backups/restore",
					auth=(auth_username, auth_password),
					data={'namespace': self.options['<namespace>'],
						'name': self.options['<name>']})
		print(response.status_code, response.content.decode())

