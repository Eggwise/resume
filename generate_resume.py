import os



FILENAME = 'resume.html'
THEME = 'elegant'

GENERATE_COMMAND = 'hackmyresume BUILD resume.json TO out/resume.html -t node_modules/jsonresume-theme-{theme}'.format(filename=FILENAME, theme=THEME)

os.system(GENERATE_COMMAND)