import os





def generate_resume():
    FILENAME = 'index.html'
    THEME = 'elegant'

    GENERATE_COMMAND = 'hackmyresume BUILD resume.json TO out/{filename} -t jsonresume-theme-{theme} -o options.json'.format(
        filename=FILENAME, theme=THEME)

    os.system(GENERATE_COMMAND)


generate_resume()