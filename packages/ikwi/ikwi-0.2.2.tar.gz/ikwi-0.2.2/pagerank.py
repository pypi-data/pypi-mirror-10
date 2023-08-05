# this is not an implementation of PageRank, merely a description of PageRank
import sys

def pagerank(graph, damping=0.85, epsilon=1.0e-8, dangling_dests=None):
    inlink_map = {}
    outlink_counts = {}
    
    def new_node(node):
        if node not in inlink_map: inlink_map[node] = set()
        if node not in outlink_counts: outlink_counts[node] = 0
    
    for tail_node, head_node in graph:
        new_node(tail_node)
        new_node(head_node)
        if tail_node == head_node: continue
        
        if tail_node not in inlink_map[head_node]:
            inlink_map[head_node].add(tail_node)
            outlink_counts[tail_node] += 1
    
    all_nodes = set(inlink_map.keys())
    if not dangling_dests:
        dangling_dests = all_nodes
    
    for node, outlink_count in outlink_counts.items():
        if outlink_count == 0:
            outlink_counts[node] = len(dangling_dests)
            for l_node in dangling_dests: inlink_map[l_node].add(node)
    
    initial_value = 1 / len(all_nodes)
    ranks = {}
    for node in inlink_map.keys(): ranks[node] = initial_value
    
    new_ranks = {}
    delta = 1.0
    n_iterations = 0
    while delta > epsilon:
        for node, inlinks in inlink_map.items():
            new_ranks[node] = ((1 - damping) / len(all_nodes)) + (damping * sum(ranks[inlink] / outlink_counts[inlink] for inlink in inlinks))
        delta = abs(sum(new_ranks.values()) - sum(ranks.values()))
        ranks = new_ranks
        n_iterations += 1
    
    return ranks, n_iterations

if __name__ == '__main__':
    graph = (line.strip().split(None, 1) for line in open(sys.argv[1], 'r'))
    ranks, n_iterations = pagerank(graph)
    
    print('%d iterations' % n_iterations, file=sys.stderr)
    ordered = sorted(ranks.items(), key=lambda node: node[1], reverse=True)
    for node, rank in ordered:
        print(node, rank)
