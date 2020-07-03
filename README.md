# Mapping the echo-chamber: COVID-19 edition

Network analysis experiment for the "Web Information Retrieval" course at La Sapienza University of Rome.


The goal is to find the polarization of the communities inside the Twitter social network regarding Coronavirus related topics. Indeed, with social media, misinformation about COVID-19, or vaccines, for example, can reach huge audiences and circulate very quickly. Therefore, it is crucial to find ways to recognize reliable information.

For the experiment documents:
* ##### [Short report]()
* ##### [Presentation slides]()



## Data & methodology

Network seed dataset:
* The "**Coronavirus Tweet Ids**" dataset from Harvard University [version 1]
  -  Contains the ids of 51,798,932 tweets related to Coronavirus or COVID-19;
  -  Collected between March 3, 2020 and March 19, 2020 from the Twitter API using Social Feed Manager;
  - Collected using the POST statuses/filter method of the Twitter Stream API, using the track parameter with the following keywords: #Coronavirus, #Coronaout- break, #COVID19;

Once hydrated the dataset we executed the following steps:
1. Build the users graph:
   - node ⇒ user;
   - edge ⇒ interaction or common domain cited (undirected and weighted);
2. Run the Louvain’s method, used to extract communities from large networks;
3. Check the polarization, which requires to analyze the contents of some tweets inside each community, since there is no previous classification for the instances of the dataset;
4. Run Word2Vec for semantic deviation



---
## Authors
* ##### [Manuel Ivagnes](https://www.linkedin.com/in/manuel-ivagnes-4a5ba018b)
* ##### [Riccardo Bianchini](http://linkedin.com/in/riccardo-bianchini-7a391219b)
* ##### [Valerio Coretti](https://www.linkedin.com/in/valerio-coretti-2913721a3)
