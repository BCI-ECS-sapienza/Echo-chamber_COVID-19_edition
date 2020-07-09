# Network graph

This folder contains scripts to build the network graph:

* **domains_index**: output a jsonl file with a pseudo inverted index, where to each domain/page (look at the report for details) is associated the list of users that cited the domain;

* **graph_construction**: output the networkx graph 

* **sample_accounts_tweets**: output a sample of the desired number of accounts from the collection, save them in a jsonl file, and finally retrieve all the corresponding tweets that are then saved in a different jsonl file


--- 
### Instructions 

Each script takes as input a json file that is the result of a previous script, make sure to follow the order:
1. After preprocessing, use **accounts_extractor** to make a list of all the users in _accounts.jsonl_;
2. We cannot use all data to build the graph, thus sample some accounts with **sample_accounts_tweets**. _sampled_accounts.jsonl_ contains all the users sampled, while _sampled_tweets.jsonl_ contains all the corresponding tweets;
3. **domains_index** to build a pseudo inverted index < domain : users >, which makes easier to find the connections derived by common domains shared;
4. run ... to find all the connections given by retweets and replies;
5. Build the graph!;