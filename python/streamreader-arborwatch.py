import sys


ARBORWATCH_052120 = {
    'preheader': '',
    'email-date': '',
    'image': '',
    'heading_1': '',
    'copy_section_1': '',
    'heading_2': '',
    'copy_section_2': '',
    'heading_3': '',
    'copy_section_3': '',
}

NVP = ARBORWATCH_052120
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
