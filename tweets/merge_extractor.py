# merge jsonl files

import json
import glob


outfile = open('tweets_dataset.jsonl','w', encoding= 'utf-8-sig')

for file in glob.glob("final_dataset/*.jsonl"):
    with open(file, 'r', encoding='utf-8-sig') as infile:
        for line in infile.readlines():
            outfile.write(line)

outfile.close()
