# script to extract only english tweets from jsonl file
#   usage:  python english_extractor.py [source] [dest]

import jsonlines
import sys

if len(sys.argv) > 2:
    with jsonlines.open(sys.argv[1]) as reader, jsonlines.open(sys.argv[2], mode='w') as writer:
        for line in reader:
            if line['lang'] == 'en':
                writer.write(line)
    print('Done!')

else:
    print('Correct usage: \n\tpython english_extractor.py [source] [dest]')
