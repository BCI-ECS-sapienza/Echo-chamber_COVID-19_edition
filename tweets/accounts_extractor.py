# list all the unique accounts with relatives number of tweets

import jsonlines
import json
import glob


accounts = {}

# dictionary with all the accounts
for file in glob.glob("final_dataset/*.jsonl"):
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
