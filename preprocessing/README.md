# Preprocessing


This folder contains scripts for tweets preprocessing:

* **accounts_extractor**: takes as input a folder with multiple jsonl files and output a jsonl file with all the unique accounts with the corresponding number of tweets;

* **count_tweets**: takes as input a single jsonl file and output the number of tweets inside it;

* **english_extractor**: takes as input a single jsonl file containing tweets in multiple languages and output a new jsonl file with only english tweets;

* **payload_reducer**: takes as input a single jsonl file and remove from each tweet unnecessary (for us) information;

---
### Utils

Contains some extra scripts:

* **merge_jsonl**: takes as input a folder with multiple jsonl files and output a single merged file, in the correct format and encoding;

* **resize_dataset**: takes 1 every 10 tweets in the initial dataset;

---
Note: While most of the project is made to work on _colab_ (or similar) with Jupiter notebooks, in this folder we have mostly command line scripts to perform on local environment. Indeed, initial raw data are much bigger and require too much time to be uploaded.
