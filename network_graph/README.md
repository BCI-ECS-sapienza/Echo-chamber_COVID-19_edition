# Graph

This folder contains scripts to build the network graph:

* **accounts_extractor**: takes as input a folder with multiple jsonl files and output a jsonl file with all the unique accounts and the corresponding number of tweets; 

* **domain_connections**: output a jsonl file with a pseudo inverted index, where to each domain/page (look at report for details) is associated the list of users that cited the domain;

---

Note: these scripts assume to work on **colab**, change the "import data" section to make it work on local environment.
