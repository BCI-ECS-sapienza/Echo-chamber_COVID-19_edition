<h1 align="center">Community detection</h1>
<h2>Modularity</h2>
<p><strong><em>Communities</em></strong>: sets of tightly connected nodes
<strong>Define</strong>: <em>Modularity</em> <em>Q</em></p>
<ul>
<li>A measure of how well a network is partitioned into communities</li>
<li>Given a partitioning of the network into groups <img src="https://i.upmath.me/svg/s%20%5Cin%20S" alt="s \in S" />:</li>
</ul>
<p align="center" style="text-align: center;"><img align="center" src="https://i.upmath.me/svg/%20Q%20%3A%3D%20%20%5Csum_%7Bs%20%5Cin%20S%7D%20%5B(%5Ctext%7Bnum%20edges%20within%20group%20s%7D)%20%5C%3B%E2%80%93%5C%3B%20(%5Ctext%7Bexpected%20num%20edges%20within%20group%20s%7D)%5D%20" alt=" Q :=  \sum_{s \in S} [(\text{num edges within group s}) \;–\; (\text{expected num edges within group s})] " /></p>
<p>Given <em>G</em> on <strong><em>n</em></strong> nodes and <strong><em>m</em></strong> edges, the <strong>expected number of edges</strong> between nodes <em>i</em> and <em>j</em> of degrees <img src="https://i.upmath.me/svg/k_i" alt="k_i" /> and <img src="https://i.upmath.me/svg/k_j" alt="k_j" /> is equals to:</p>
<p align="center" style="text-align: center;"><img align="center" src="https://i.upmath.me/svg/%20%5Cfrac%7Bk_i%20k_j%7D%7B2m%7D%20" alt=" \frac{k_i k_j}{2m} " /></p>
<p><strong>Modularity of partitioning S of graph G</strong>:</p>
<p align="center" style="text-align: center;"><img align="center" src="https://i.upmath.me/svg/%20%0A%5Cbegin%7Baligned%7D%20%0AQ(G%2CS)%20%3D%20%5Cunderbrace%7B%5Cfrac%7B1%7D%7B2m%7D%7D_%7B-1%3CQ%3C1%7D%20%5Csum_%7Bs%20%5Cin%20S%7D%20%5Csum_%7Bi%20%5Cin%20S%7D%20%5Csum_%7Bj%20%5Cin%20S%7D%20%5Cbigg(%20A_%7Bij%7D%20-%20%5Cfrac%7Bk_i%20k_j%7D%7B2m%7D%20%5Cbigg)%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20(1)%0A%5Cend%7Baligned%7D%0A" alt=" 
\begin{aligned} 
Q(G,S) = \underbrace{\frac{1}{2m}}_{-1&lt;Q&lt;1} \sum_{s \in S} \sum_{i \in S} \sum_{j \in S} \bigg( A_{ij} - \frac{k_i k_j}{2m} \bigg) \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; (1)
\end{aligned}
" /></p>
<p>where: <img src="https://i.upmath.me/svg/A_%7Bij%7D%20%3D%201%20" alt="A_{ij} = 1 " /> if <img src="https://i.upmath.me/svg/i%E2%86%92j" alt="i→j" />, 0 else</p>
<p>Modularity values take range <img src="https://i.upmath.me/svg/%5B1%2C-1%5D" alt="[1,-1]" />. It is positive if the number of edges within groups exceeds the expected number.</p>
<p><strong>KEY IDEA</strong>: We can identify communities by <strong>maximizing modularity</strong></p>
<h2>Louvain algorithm</h2>
<p>Greedy algorithm for community detection. Complexity at run time: <img src="https://i.upmath.me/svg/%20%5Cbf%7BO(n%20*%20log(n))%7D" alt=" \bf{O(n * log(n))}" />.</p>
<p>Louvain algorithm <strong>greedily maximizes modularity</strong>. Each pass is made of 2 phases:</p>
<ul>
<li><strong>Phase 1</strong>: Modularity is optimized by allowing only local changes to node-communities memberships</li>
<li><strong>Phase 2</strong>: The identified communities are aggregated into super-nodes to build a new network</li>
<li><strong>Goto Phase 1</strong></li>
</ul>
<p>The passes are repeated iteratively <em>until no increase of modularity is possible</em>.</p>
<h4>Phase 1</h4>
<p>Put each node in a graph into a distinct community (one node per community). For each node <em>i</em>, the algorithm performs two calculations:</p>
<ul>
<li>Compute the modularity delta <img src="https://i.upmath.me/svg/(%5CDelta%20Q)" alt="(\Delta Q)" /> when putting node 𝑖 into the community of some neighbor <em>j</em></li>
<li>Move <em>i</em> to the community of node <em>j</em> that yields the largest gain in <img src="https://i.upmath.me/svg/(%5CDelta%20Q)" alt="(\Delta Q)" /></li>
</ul>
<p>This first phase stops when a local maximum of the modularity is attained, i.e., when no individual node move can improve the modularity.
What is <img src="https://i.upmath.me/svg/(%5CDelta%20Q)" alt="(\Delta Q)" /> if we move node <em>i</em> to community <em>C</em>?</p>
<p align="center" style="text-align: center;"><img align="center" src="https://i.upmath.me/svg/%20%0A%5Cbegin%7Baligned%7D%0A%5CDelta%20Q(i%20%E2%86%92%20C)%20%3D%20%5Cunderbrace%7B%5Cbigg%5B%5Cfrac%7B%5Csum_%7Bin%7D%20%5C%3B%2B%5C%3B%20k_%7Bi%2C%20in%7D%7D%7B2m%7D%20-%20%5Cbigg(%20%5Cfrac%7B%5Csum_%7Btot%7D%20%5C%3B%2B%5C%3B%20k_%7Bi%7D%7D%7B2m%7D%20%5Cbigg)%5E2%20%5Cbigg%5D%7D_%7Bgain%7D%20-%20%5Cunderbrace%7B%20%5Cbigg%5B%20%5Cunderbrace%7B%5Cfrac%7B%5Csum_%7Bin%7D%7D%7B2m%7D%20-%20%5Cbigg(%20%5Cfrac%7B%5Csum_%7Btot%7D%7D%7B2m%7D%20%5Cbigg)%5E2%7D_%7BModularity%5C%3Bof%5C%3BC%7D%20-%20%5Cunderbrace%7B%5Cbigg(%20%5Cfrac%7Bk_i%7D%7B2m%7D%20%5Cbigg)%5E2%7D_%7BModularity%5C%3Bof%5C%3Bi%7D%20%5Cbigg%5D%20%7D_%7Bloss%7D%20%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%5C%3B%20(2)%0A%5Cend%7Baligned%7D%0A" alt=" 
\begin{aligned}
\Delta Q(i → C) = \underbrace{\bigg[\frac{\sum_{in} \;+\; k_{i, in}}{2m} - \bigg( \frac{\sum_{tot} \;+\; k_{i}}{2m} \bigg)^2 \bigg]}_{gain} - \underbrace{ \bigg[ \underbrace{\frac{\sum_{in}}{2m} - \bigg( \frac{\sum_{tot}}{2m} \bigg)^2}_{Modularity\;of\;C} - \underbrace{\bigg( \frac{k_i}{2m} \bigg)^2}_{Modularity\;of\;i} \bigg] }_{loss} \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; (2)
\end{aligned}
" /></p>
<p>where:</p>
<ul>
<li><img src="https://i.upmath.me/svg/%20%5Csum_%7Bin%7D%20" alt=" \sum_{in} " /> = sum of link weights between nodes in <em>C</em></li>
<li><img src="https://i.upmath.me/svg/%20%5Csum_%7Btot%7D%20" alt=" \sum_{tot} " /> = sum of all link weights of nodes in <em>C</em></li>
<li><img src="https://i.upmath.me/svg/%20k_%7Bi%2C%20in%7D%20" alt=" k_{i, in} " /> = sum of link weights between node <em>i</em> and <em>C</em></li>
<li><img src="https://i.upmath.me/svg/%20k_%7Bi%7D%20" alt=" k_{i} " /> = sum of all link weights (i.e., degree) of node <em>i</em></li>
<li><strong><em>gain</em></strong>: modularity contribution after merging node <em>i</em></li>
<li><strong><em>loss</em></strong>: modularity contribution before merging node <em>i</em></li>
</ul>
<h4>Phase 2</h4>
<p>The communities obtained in the first phase are contracted into <strong>super-nodes</strong>, and the network is created accordingly:</p>
<ul>
<li>Super-nodes are connected if there is at least one edge between the nodes of the corresponding communities</li>
<li>The weight of the edge between the two super-nodes is the sum of the weights from all edges between their corresponding communities</li>
<li>Phase 1 is then run on the super-node network</li>
</ul>
<h2>Summary</h2>
<p><strong>Modularity</strong>:</p>
<ul>
<li>Overall quality of the partitioning of a graph into communities</li>
<li>Used to determine the number of communities</li>
</ul>
<p><strong>Louvain modularity maximization</strong>:</p>
<ul>
<li>Greedy strategy</li>
<li>Great performance, scales to large networks</li>
</ul>

## Pseudocode

* **Description**: Given a graph G, finds the optimal community for each node

* **Parameters**:
    ```
    G : Graph
        Must be an undirected weighted graph.
    ```
* **Returns**:
    ```
    communities : Dictionary 
        Map each node to a community.
    ```


#### INIT

Put each node in a graph into a distinct community (one node per community).
```javascript
communities = {}
for each (v in G):
    communities[v] = v
```

where *communities[v]* is the community of node *v*.


#### PHASE 1

```javascript
P1(G, communities):

    converged = False

    while(!converged):
        converged = True

        // Set modularity of each node
        for each (v in G):
            max_modularity = -1                         // Modularity is in [-1, 1]
            max_community = None

            for each (edge in v):
                w = edge[0]                             // w is a node such that there exist v → w

                tmp = communities[v]
                communities[v] = communities[w]
                modularity = // See formula (2) above
                if (modularity > max_modularity):
                    max_modularity = modularity
                    max_community = communities[w]

                communities[v] = tmp

            if (max_modularity > 0):
                communities[v] = max_community
                converged = False                       // louvain converges only when the modularity is not updated

                update sum_in
                update sum_tot
                update k_in

    return communities
```


#### PHASE 2

```javascript
P2(G, communities):

    G_new = {}

    for each (c in communities):
        G_new[c] = new set()

    for each (v in G):
        cv = communities[v]
        for each (edge in v):
            w = edge[0]
            cw = communities[w]
            
            if cv != cw:
                G_new[cv][cw] += 1
        delete G[v]

    return G_new, communities
```

#### Example
* **Input Graph**:
<center><img src="./img/input.png" height="250" /></center>

* **Output**:
        Communities = {1: 3, 2: 3, 3: 3, 4: 3, 5: 7, 6: 7, 7: 7, 8: 7}
<center><img src="./img/output.png" width="800" height="200" /></center>
<center><img src="./img/example.png" height="250" /></center>

---
#### Reference 
> CS246: Mining Massive Datasets Jure Leskovec, Stanford University - **Community Detection in Graphs**: http://cs246.stanford.edu

> Vincent D. Blondel, Jean-Loup Guillaume, Renaud Lambiotte, Etienne Lefebvre - **Fast Unfolding of communities in large networks**: https://arxiv.org/abs/0803.0476