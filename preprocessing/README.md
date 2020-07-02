# Preprocessing 


This folder contains scripts for tweets preprocessing:

**count_tweets**: takes as input a single jsonl file and output the number of tweets inside it;

**english_extractor**: takes as input a single jsonl file containing tweets in multiple languages and output a new jsonl file with only english tweets;

**naive_accounts_extractor**: takes as input a folder with multiple jsonl files and output a txt file with all the unique accounts and the corresponding number of tweets; 

**payload_reducer**: takes as input a single jsonl file and remove from each tweet unnecessary (for us) information;

---
### Utils

Contains some extra scripts we have used:

**merge_jsonl**: takes as input a folder with multiple jsonl files and output a single merged file, in the correct format and encoding;

**resize_dataset**: takes 1 every 10 tweets in the initial dataset;

