import sys


CITIZENSCIENCE_052120 = {
    'preheader': '',
    'image': '',
    'main_text_p-1': '',
    'main_text_p-2': '',
    'main_text_p-3': '',
    'button_link': '',
    'button_label': '',
}

NVP = CITIZENSCIENCE_052120
#


def replacekeys(line):
    # built-in dictionary method that returns a list of its (key, value) tuple pairs
    for name, value in NVP.items():
        line = line.replace(f'%%{name}%%', value)

    return line


# read redirected standard input line by line

for line in sys.stdin:
    # stdout is redirected to > filename.html
    print(replacekeys(line), end='')
