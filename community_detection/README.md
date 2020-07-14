<h1 align="center">Community detection</h1>

## Modularity
***Communities***: sets of tightly connected nodes
**Define**: *Modularity* *Q*
* A measure of how well a network is partitioned into communities
* Given a partitioning of the network into groups $s \in S$:
$$ Q :=  \sum_{s \in S} [(\text{num edges within group s}) \;–\; (\text{expected num edges within group s})] $$

Given *G* on ***n*** nodes and ***m*** edges, the **expected number of edges** between nodes *i* and *j* of degrees $k_i$ and $k_j$ is equals to: $$ \frac{k_i k_j}{2m} $$

**Modularity of partitioning S of graph G**: 
$$ 
\begin{aligned} 
Q(G,S) = \underbrace{\frac{1}{2m}}_{-1<Q<1} \sum_{s \in S} \sum_{i \in S} \sum_{j \in S} \bigg( A_{ij} - \frac{k_i k_j}{2m} \bigg) \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; (1)
\end{aligned}
$$

where: $ A_{ij} = 1 $ if $i→j$, 0 else

Modularity values take range $[1,-1]$. It is positive if the number of edges within groups exceeds the expected number.

**KEY IDEA**: We can identify communities by **maximizing modularity**

## Louvain algorithm
Greedy algorithm for community detection. Complexity at run time: $ \bf{O(n * log(n))}$.

Louvain algorithm **greedily maximizes modularity**. Each pass is made of 2 phases:
* **Phase 1**: Modularity is optimized by allowing only local changes to node-communities memberships
* **Phase 2**: The identified communities are aggregated into super-nodes to build a new network
* **Goto Phase 1**

The passes are repeated iteratively *until no increase of modularity is possible*.

#### Phase 1
Put each node in a graph into a distinct community (one node per community). For each node *i*, the algorithm performs two calculations:
* Compute the modularity delta $(\Delta Q)$ when putting node 𝑖 into the community of some neighbor *j*
* Move *i* to the community of node *j* that yields the largest gain in $(\Delta Q)$

This first phase stops when a local maximum of the modularity is attained, i.e., when no individual node move can improve the modularity.
What is $(\Delta Q)$ if we move node *i* to community *C*?

$$ 
\begin{aligned}
\Delta Q(i → C) = \underbrace{\bigg[\frac{\sum_{in} \;+\; k_{i, in}}{2m} - \bigg( \frac{\sum_{tot} \;+\; k_{i}}{2m} \bigg)^2 \bigg]}_{gain} - \underbrace{ \bigg[ \underbrace{\frac{\sum_{in}}{2m} - \bigg( \frac{\sum_{tot}}{2m} \bigg)^2}_{Modularity\;of\;C} - \underbrace{\bigg( \frac{k_i}{2m} \bigg)^2}_{Modularity\;of\;i} \bigg] }_{loss} \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; (2)
\end{aligned}
$$

where:
* $ \sum_{in} $ = sum of link weights between nodes in *C* 
* $ \sum_{tot} $ = sum of all link weights of nodes in *C* 
* $ k_{i, in} $ = sum of link weights between node *i* and *C* 
* $ k_{i} $ = sum of all link weights (i.e., degree) of node *i*
* ***gain***: modularity contribution after merging node *i*
* ***loss***: modularity contribution before merging node *i*

#### Phase 2
The communities obtained in the first phase are contracted into **super\-nodes**, and the network is created accordingly:
* Super\-nodes are connected if there is at least one edge between the nodes of the corresponding communities
* The weight of the edge between the two super\-nodes is the sum of the weights from all edges between their corresponding communities
* Phase 1 is then run on the super-node network

## Summary
**Modularity**:
* Overall quality of the partitioning of a graph into communities
* Used to determine the number of communities

**Louvain modularity maximization**:
* Greedy strategy
* Great performance, scales to large networks

## Pseudocode
* **Description**: Given a graph G, finds the optimal community for each node

* **Parameters**:
    ```
    G : Graph
        Must be an undirected weighted graph in the form of a dictionary: {v : {neighbors}}
            where 'neighbors' is a Counter structure like: {w1:weight, w2:weight, ...}
            - w1 = neighbour node linked to v
            - weight = weigth of the edge v -> w1
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
<img src="./input.png" height="300" />

* **Output**:
        Communities = {1: 3, 2: 3, 3: 3, 4: 3, 5: 7, 6: 7, 7: 7, 8: 7}
<img src="./output.png" width="800" height="200" />
<img src="./example.png" height="300" />

---
#### Reference 
> CS246: Mining Massive Datasets Jure Leskovec, Stanford University - Community Detection in Graphs: http://cs246.stanford.edu