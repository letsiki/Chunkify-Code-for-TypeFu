from parsers import master_parser
from constants import PREFIX, POSTFIX, WPC, SEP
import os
import glob
from datetime import datetime as dt


data = []
path = r'.\data\sample'
for filename in glob.glob(os.path.join(path, '*.py')):  # code to access and loop through all .py in a path
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in read-only mode
        data += master_parser(f)

final_string = ""
# print(sorted(list(map(len, data)), reverse=True))
# sorted_data = sorted(data, key=len)
current_chunk_len = 0
for e in data:
    if len(e) > WPC:
        continue
    if current_chunk_len < WPC:
        final_string += e + '\n'
        current_chunk_len += len(e)
    else:
        current_chunk_len = 0
        final_string += SEP

with open(file=rf'.\data\exported\TF{dt.now().strftime("%d%m%y_%H%M")}.tfd', mode='w') as f:
    f.write(PREFIX + final_string + POSTFIX)

