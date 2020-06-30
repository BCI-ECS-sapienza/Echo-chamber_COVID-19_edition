# list all the unique accounts with relatives number of tweets in the dataset

import jsonlines
import json
import glob
import sys


accounts = {}


if len(sys.argv) > 1:
# dictionary with all the accounts
    for file in glob.glob(sys.argv[1]+"/*.jsonl"):
        with jsonlines.open(file) as infile:
            for line in infile:
                user = line['user']['name']
                if user in accounts:
                    accounts[user] += 1
                else:
                    accounts[user] = 1


    # write dictionary on file
    with open('accounts.txt', 'w') as output:
        for elem in accounts.items():
            output.write('%s %s\n' % elem)

    # output number accounts
    print(len(accounts))

else:
    print('Correct usage: \n\tpython count_tweets.py [jsonl files dir]')
