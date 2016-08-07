import textwrap

def format(text):
    res = ''
    for str in text.split('\n'):
        str = textwrap.indent(str, '  ')
        str = textwrap.fill(str, 80)
        res += str + '\n\n'
    return res
