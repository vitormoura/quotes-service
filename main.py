import os

from app import create_app

# App configuration file path
cwd = os.getcwd()
config_file = os.path.join(cwd, 'config/appsettings.json')

# Creating app with appsettings
application = create_app(config_file)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)
    