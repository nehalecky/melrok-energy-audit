# Set the path
#import os, sys
#sys.path.append(os.path.dirname(__file__))
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)

class RunDevelopServer(Server):
    use_debugger=True,
    use_reloader=True,
    port='50001'

    
# Turn on debugger by default and reloader
manager.add_command("runlocalserver", RunDevelopServer())

# Turn on debugger by default and reloader
manager.add_command("runserver", RunDevelopServer( 
    host='0.0.0.0')
)

if __name__ == "__main__":
    manager.run()
