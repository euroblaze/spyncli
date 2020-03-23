from .base import Base
from os.path import abspath, dirname

class Deploy(Base):
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

        if self.options['deploy']:
            print('yaHAG')
            files = [('snapshot', open(str(self.options['<snapshot>']),'rb'))]
            data = {'odoo_username':self.options['<odoo_username>'],
                    'odoo_password':self.options['<odoo_password>'],
                    'snapshots':open(self.options['<snapshot>'], 'rb')}
            print(data)
            response = requests.post(API + "deploy/%s" % self.options['<configset_id>'],
                                     auth=(auth_username, auth_password),
                                     files=files,
                                     data=data)
            print(response.status_code, response.content.decode())
