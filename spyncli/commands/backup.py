from .base import Base
from os.path import abspath, dirname

class Backup(Base):
    """Backup Class"""

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
		response = requests.post(API + "backups/backup",
					auth=(auth_username, auth_password),
					data={'namespace': self.options['<namespace>']})
		print(response.status_code, response.content.decode())

