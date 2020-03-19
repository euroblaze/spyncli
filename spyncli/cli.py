"""
spyncli

Usage:
  spyncli users login <username> <password>
  spyncli users register <first_name> <last_name> <email> <username> <password>
  spyncli users update [--name=first_name] [--surname=last_name] [--email=email] [--usr=username] [--pwd=password]
  spyncli git read [--name=module name] [--id=module id] [--conf=configset id]
  spyncli git update <id> [--url=GIT_URL] [--usr=GIT_USER] [--pwd=GIT_PASS] [--b=GIT_BRANCH] [--name=MODULE_NAME]
  spyncli git delete <id>
  spyncli git create <configset_id> <git_url> <username> <password> <branch> <module_name>
  spyncli configset read [--id=configset id] [--name=configset name]
  spyncli configset delete <id>
  spyncli configset create <name> (--url=LIST_GIT_URLS...) (--usr=LIST_USERS...) (--pwd=LIST_PASS...) (--b=LIST_BRANCH...) (--name=LIST_MODULE...)
  spyncli clones read [--id=CLONE_ID] [--name=CLONE_NAME]
  spyncli replicas read
  spyncli replicas scale <clone_id> <final_number>
  spyncli -h | --help
  spyncli --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  spyncli users

Help:
  For help using this tool, please open an issue on the Github repository:
"""

from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import spyncli.commands
    options = docopt(__doc__, version=VERSION)
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(spyncli.commands, k) and v:
            module = getattr(spyncli.commands, k)
            spyncli.commands = getmembers(module, isclass)
            command = [command[1] for command in spyncli.commands if command[0] != 'Base'][0]
            command = command(options)
            try:
                command.run()
            except:
                pass
