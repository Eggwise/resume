import os



INSTALL_COMMAND = 'npm install -g hackmyresume'

THEME_NAME = 'elegant'
INSTALL_THEME_COMMAND = 'npm install jsonresume-theme-{0}'.format(THEME_NAME)



os.system(INSTALL_COMMAND)

os.system(INSTALL_THEME_COMMAND)