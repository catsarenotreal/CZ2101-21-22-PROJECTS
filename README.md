# CZ2101-21-22-PROJECT

Project 1: Integration of InsertionSort and MergeSort
In MergeSort, when the sizes of subarrays are small, the overhead of many recursive
calls makes the algorithm inefficient. Therefore, in real use, we often combine
MergeSort with InsertionSort to come up with a hybrid sorting algorithm for better
efficiency. The idea is to set a small integer S as a threshold for the size of subarrays.
Once the size of a subarray in a recursive call of MergeSort is less than or equal to S,
the algorithm will switch to InsertionSort, which is efficient for small input.

  (a) Implement the above hybrid algorithm. Analyze its time complexity in terms of
  the number of key comparisons with respect to S and the size of the input list
  n. Study how to determine an optimal value of S for best performance of this
  hybrid algorithm on different input cases and input sizes.

  (b) Implement the original version of MergeSort (as learnt in lecture). Compare its
  performance against the above hybrid algorithm in terms of the number of key
  comparisons and CPU time on different input cases and input sizes. You can
  use the optimal value of S obtained in (a) for this task.

Show your running program with printings of CPU time, and present your analysis.


###########################################################################################

Project 2: Implementation of Dijkstra's Algorithm via Array and Heap
In the Dijkstra's algorithm, the choice of the input graph representation and the priority
queue implementation will affect its time complexity.

  (a) Suppose the input graph G = (V, E) is stored in an adjacency matrix and we
  use an array for the priority queue. Implement the Dijkstra's algorithm using this
  setting and analyze its time complexity with respect to |V| and |E| both
  theoretically and empirically.

  (b) Suppose the input graph G = (V, E) is stored in an array of adjacency lists and
  we use a minimizing heap for the priority queue. Implement the Dijkstra's
  algorithm using this setting and analyze its time complexity with respect to |V|
  and |E| both theoretically and empirically.
