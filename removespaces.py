import os
import glob

for f in glob.glob('**/*.pdf', recursive=True):
    print(f)
    newname = f.replace(' ', '')
    os.rename(f, newname)