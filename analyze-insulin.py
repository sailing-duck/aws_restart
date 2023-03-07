"""
lab 118
"""
import re

with open('preproinsulin-seq.txt','r') as file:
    content = file.read()

print(content)
content = re.sub(r'\/\/|\s|\r|\n|\d+|ORIGIN', '', content)

with open('preproinsulin-seq-clean.txt','w') as file:
    file.write(content)

lsinsulin = content[0:24]
binsulin = content[24:54]
cinsulin = content[54:89]
ainsulin = content[89:110]

with open('lsinsulin-seq-clean.txt','w') as file:
    file.write(lsinsulin)
    
with open('binsulin-seq-clean.txt','w') as file:
    file.write(binsulin)
    
with open('cinsulin-seq-clean.txt','w') as file:
    file.write(cinsulin)
    
with open('ainsulin-seq-clean.txt','w') as file:
    file.write(ainsulin)