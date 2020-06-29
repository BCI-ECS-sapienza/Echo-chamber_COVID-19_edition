# script to extract 1 on 10 tweets from a database seed ids files
# files are still devided to run Twarc on each group component in parallel

for i in range(6):
    file = open("tweet_ids/ids" + str(i) + ".txt", 'w')

    # iterate old
    count = 10
    with open('original_tweet_ids/coronavirus-through-19-Mar-2020-0' + str(i) + '.txt') as openfileobject:
        for line in openfileobject:
            if count == 10:
                file.write(line)
                count = 0
            count += 1

print('Done!')
