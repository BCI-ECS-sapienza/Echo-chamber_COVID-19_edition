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
            if('retweeted_status' in line):
                x['retweeted_status'] = {
                    "created_at": line['retweeted_status']['created_at'],
                "id": line['retweeted_status']['id'],
                "full_text": line['retweeted_status']['full_text'],
                "entities": {
                    "hashtags": line['retweeted_status']['entities']['hashtags'],
                    "symbols": line['retweeted_status']['entities']['symbols'],
                    "user_mentions": line['retweeted_status']['entities']['user_mentions'],
                    "urls": line['retweeted_status']['entities']['urls']
                },
                "user": {
                    "id": line['retweeted_status']['user']['id'],
                    "name": line['retweeted_status']['user']['name'],
                    "screen_name": line['retweeted_status']['user']['screen_name'],
                    "location": line['retweeted_status']['user']['location']
                },
                "retweet_count": line['retweeted_status']['retweet_count'],
                }
            writer.write(x)
    print('Done!')

else:
    print('Correct usage: \n\tpython payload_reducer.py [source] [dest]')