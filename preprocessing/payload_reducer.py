# script to extract only english tweets
#   usage:  python payload_reducer.py [source] [dest]

import jsonlines
import json
import sys

if len(sys.argv) > 2:
    with jsonlines.open(sys.argv[1]) as reader, jsonlines.open(sys.argv[2], mode='w') as writer:
        for line in reader:
            x = {
                "created_at": line['created_at'],
                "id": line['id'],
                "full_text": line['full_text'],
                "entities": {
                    "hashtags": line['entities']['hashtags'],
                    "symbols": line['entities']['symbols'],
                    "user_mentions": line['entities']['user_mentions'],
                    "urls": line['entities']['urls']
                },
                "user": {
                    "id": line['user']['id'],
                    "name": line['user']['name'],
                    "screen_name": line['user']['screen_name'],
                    "location": line['user']['location']
                },
                "retweet_count": line['retweet_count'],
            }
            writer.write(x)
    print('Done!')

else:
    print('Correct usage: \n\tpython payload_reducer.py [source] [dest]')