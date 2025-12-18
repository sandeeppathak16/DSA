## Graph Algorithm Selection Cheat Sheet

### Unweighted Graph

* **Shortest path** → **BFS**

### Weighted Graph

* **All weights ≥ 0** → **Dijkstra**
* **Negative weights present** → **Bellman–Ford**

### Directed Acyclic Graph (DAG)

* **Ordering / dependencies** → **Topological Sort**
* **Shortest path** → **Topological Sort + DP**

### Undirected Graph

* **Connected components** → **DFS / BFS / DSU**
* **Minimum Spanning Tree (MST)** → **Kruskal / Prim**

### All-Pairs Shortest Path

* **Floyd–Warshall**

## Common Problems → Algorithms

| Problem                    | Correct Algorithm           |
| -------------------------- | --------------------------- |
| Network Delay Time         | **Dijkstra**                |
| Course Schedule            | **Topological Sort**        |
| Word Ladder                | **BFS**                     |
| Cheapest Flights (k stops) | **Bellman–Ford / BFS + DP** |
| Number of Islands          | **DFS / BFS**               |
| Redundant Connection       | **DSU (Union–Find)**        |
| Minimum Spanning Tree      | **Kruskal / Prim**          |

