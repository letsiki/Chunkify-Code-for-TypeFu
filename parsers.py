import re
from typing import TextIO

def master_parser(file: TextIO) -> list:
    "returns a list with all the valid snippets in the file"
    string_from_file = file.read()
    parsed = parser3(parser2(parser1(string_from_file)))
    return split_to_list(parsed)

def parser1(s: str) -> str:
    "will eliminate comments and multiline strings"
    s = re.sub('#(.|\n)*?\n', '', s)
    return re.sub('"""(.|\n)*?"""', '', s)

def parser2(s: str) -> str:
    "will delete multiline lists and dictionaries"
    s = re.sub('{(.|\n)*?}', '{key: value}', s)
    return re.sub('\[\n(.|\n)*?\]', '[list_data]', s)

def parser3(s: str) -> str:
    "will clean up removing unecessary new lines and spaces before new lines"
    return  re.sub(r'\n\s*\n', '\n', s)

def split_to_list(s: str) -> list[str]:
    "Will split code blocks, like functions, into a list and return it"
    l = s.split('def ')
    for i in range(1, len(l)):
        l[i] = 'def ' + l[i]
    l.append('---EOF---')
    return l
