# merge jsonl files

import jsonlines
import json
import glob
import sys

if len(sys.argv) > 2:
    outfile = jsonlines.open(sys.argv[2], mode='w')

    for file in glob.glob(sys.argv[1] + "*.jsonl"):
        with jsonlines.open(file) as infile:
            for line in infile:
                outfile.write(line)

    outfile.close()

else:
    print('Correct usage: \n\tpython english_extractor.py [source dir] [dest name]')
