# Set the path
#import os, sys
#sys.path.append(os.path.dirname(__file__))
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runlocalserver", Server(
    use_debugger=True,
    use_reloader=True,
    port='50001')
)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port='50001')
)

if __name__ == "__main__":
    manager.run()
