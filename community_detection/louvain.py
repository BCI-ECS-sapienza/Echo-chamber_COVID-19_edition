import math
from tqdm import tqdm
from collections import Counter, defaultdict

"""### Initialization"""

# In the case of first init we have to initialize also the communities
def first_init(G):
  communities = {}
  super_nodes = defaultdict(list)

  sum_in = {}                 # sum of link weights between nodes in 𝐶
  sum_tot = Counter()         # sum of all link weights of nodes in 𝐶
  k_in = {}                   # sum of link weights between node 𝑖 and 𝐶
  k_i = {}                    # sum of all link weights (i.e., degree) of node 𝑖

  for v in G:
      communities[v] = v      # At the beginning every node is a community
      sum_in[v] = 0
      k_i[v] = 0
      k_in[v] = Counter()
      for w in G[v]:
          k_i[v] += G[v][w]
          sum_tot[v] += G[v][w]
          k_in[v][w] = G[v][w]

  return communities, super_nodes, sum_in, sum_tot, k_i, k_in

def init(G):
  sum_in = {}                 
  sum_tot = Counter()         
  k_i = {}
  k_in = {}

  for v in G:
      sum_in[v] = 0
      k_i[v] = 0
      k_in[v] = Counter()
      for w in G[v]:
          k_i[v]+= G[v][w]
          sum_tot[v]+= G[v][w]
          k_in[v][w] = G[v][w]

  return sum_in, sum_tot, k_i, k_in


"""### PHASE 1
Put each node in a graph into a distinct community (one node per community). For each node v, the algorithm performs two calculations:

- Compute the modularity delta (∆𝑄) when putting node v into the community of some neighbor w
- Move v to the community of node w that yields the largest gain in ∆𝑄
"""
def P1(G, communities, sum_in, sum_tot, k_i, k_in):

  converged = False
  ok = 0

  # This m corresponds to the number of edges, we need it to calculate modularity
  m = 0
  for i in G:
      for j in G[i]:
          if i < j:
              m+=G[i][j]
  
  while not converged:
    converged = True
    ok += 1

    # Needed for the statistics
    n_nodes = len(G.keys())
    updates = 0

    for v, neighbors in tqdm(G.items()):        
      max_modularity = -1
      max_community = None

      for w in neighbors:
        C = communities[w]

        # Modularity moving node v into the community C of the neighbor w
        gain = (sum_in[C] + k_in[v][C])/(2*m) - pow(((sum_tot[C]+k_i[v])/(2*m)),2)
        loss = (sum_in[C])/(2*m) - pow((sum_tot[C])/(2*m),2) - pow((k_i[v])/(2*m),2)

        modularity = gain - loss

        # Update max_modularity and max_community, if moving node v into the community C of the neighbor w increase the curr modularity
        if (modularity > max_modularity):
          max_modularity = modularity
          max_community = communities[w]
      
      # Change the community of v if the max_modularity is greather than 0, then update the values
      if max_modularity > 0 and (max_community != communities[v]):
        updates += 1
        old_community = communities[v]
        communities[v] = max_community
        converged = False

        for w in neighbors:
            weight = G[v][w]

            # update sum_in
            if communities[w] == old_community:
                sum_in[old_community] -= weight
            if communities[w] == max_community:
                sum_in[max_community] += weight

            # update sum_tot
            if communities[w] != old_community and communities[w] != max_community:
                sum_tot[old_community] -= weight
                sum_tot[max_community] += weight
            elif communities[w] == old_community:
                sum_tot[old_community] += weight
                sum_tot[max_community] += weight
            elif communities[w] == max_community:
                sum_tot[old_community] -= weight
                sum_tot[max_community] -= weight

            # update k_in
            k_in[w][old_community] -= weight
            k_in[w][max_community] += weight
              
    # statistics
    perc = updates/n_nodes
    print(f"Updates per iteration:    {updates}")
    print(f"% update    :    {perc*100}%")

  # If the 'for' iteration are at least 2 continue with phase2, otherwise break
  if ok > 1:
    return communities, True
  else:
    return communities, False



"""### Phase 2
The communities obtained in the first phase are contracted into super-nodes, and the network is created accordingly:

- Super-nodes are connected if there is at least one edge between the nodes of the corresponding communities
- The weight of the edge between the two super-nodes is the sum of the weights from all edges between their corresponding communities
- Phase 1 is then run on the super-node network
"""

def P2(G, communities, super_nodes):

  G_new = {}
  
  # Update communities of merged nodes
  for node in tqdm(G):
    if node != communities[node]:
      merged_nodes = super_nodes[node]

      for merged_node in merged_nodes:
        communities[merged_node] = communities[node]
      
      super_nodes[communities[node]].extend(merged_nodes)
      del super_nodes[node]

  # Set community graph nodes
  for c in set(communities.values()):
    G_new[c] = Counter()

  for v in tqdm(list(G)):
    cv = communities[v]
    for w in G[v]:
      cw = communities[w]
      
      if cv != cw:
        G_new[cv][cw] += 1
        G_new[cw][cv] += 1

    del G[v]

  return G_new, communities, super_nodes



"""### Louvain method"""

def louvain(G):

  communities, super_nodes, sum_in, sum_tot, k_i, k_in = first_init(G)
  iter = 0

  while True:
      iter += 1

      communities, ok = P1(G, communities, sum_in, sum_tot, k_i, k_in)

      if not ok:
          break

      G, communities, super_nodes = P2(G, communities, super_nodes)

      sum_in, sum_tot, k, kin = init(G)
      print(f"# Total iteration: {iter}")
  return communities


''' Print communities '''
def print_communities(communities):

  output = []
  for c in communities:
    if communities[c] not in output:
      output.append(communities[c])

  print(output)
  print(communities)



"""### Test"""

G1 = {
    1: Counter({2:10, 3:10, 4:10, 5:1}),
    2: Counter({1:10, 3:10, 4:10, 6:1}),
    3: Counter({1:10, 2:10, 4:10}),
    4: Counter({1:10, 2:10, 3:10}),
    5: Counter({6:10, 7:10, 8:10, 1:1}),
    6: Counter({5:10, 7:10, 8:10, 2:1}),
    7: Counter({5:10, 6:10, 8:10}),
    8: Counter({5:10, 6:10, 7:10})
}

if __name__ == '__main__':
  print("TEST")
  communities = louvain(G1)
  print_communities(communities)
  exit()