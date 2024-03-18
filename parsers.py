import re
from typing import TextIO

def master_parser(file: TextIO) -> list:
    "returns a list with all the valid snippets in the file"
    string_from_file = file.read()
    parsed = parser3(parser2(parser1(string_from_file)))
    return list(filter(lambda x: len(x) != 0 and '"""' not in x, parsed.split('\n\n')))

def parser1(s: str) -> str:
    "will eliminate comments and multiline strings"
    s = re.sub('#(.|\n)*?\n', '', s)
    return re.sub('"""(.|\n)*?"""', '', s)

def parser2(s: str) -> str:
    "will delete multiline lists and dictionaries"
    s = re.sub('{(.|\n)*?}', '{dict_placeholder_data}', s)
    return re.sub('\[\n(.|\n)*?\]', '[list_data]', s)

def parser3(s: str) -> str:
    "will clean up removing unecessary new lines and spaces before new lines"
    # s = s.replace(':', ':\n')
    # s = s.replace(':\n*[" "]', ':\n\t')  # requires more testing
    return  re.sub(r'\n\s*\n', '\n\n', s)
