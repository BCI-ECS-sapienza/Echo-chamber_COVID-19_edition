# script to count tweets in jsonl file
#   usage:  python count_tweets.py [source]

import jsonlines
import sys


count = 0
if len(sys.argv) > 1:
    with jsonlines.open(sys.argv[1]) as reader:
        for line in reader:
            count += 1

    print(count)

else:
    print('Correct usage: \n\tpython count_tweets.py [source]')
