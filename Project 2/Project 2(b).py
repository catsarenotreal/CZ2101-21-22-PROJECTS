import heapq
import random
import time
import csv


def heapDijkstra(srcNode, A, neighbour): 
  INF = 1000000
  n = len(A)

  queue = [(0, srcNode)]
  dist = []

  for i in range(n):
    dist.append(INF)
  dist[0] = 0 # dist = [0, INF, INF, INF etc.]

  while len(queue) != 0: 

    curr_dist, shortest_node = heapq.heappop(queue) 
    
    adj = neighbour[shortest_node] 
    
    for nb_node in range(len(adj)): 
      weight = A[shortest_node][nb_node][1] 
      distance = weight + curr_dist

      if distance < dist[adj[nb_node]]:
        dist[adj[nb_node]] = distance
        heapq.heappush(queue, (distance, adj[nb_node])) 



def createAList(n, e):
  A = {}
  neighbour_index = {}

  for i in range(n):
    A[i] = []
    neighbour_index[i] = []

  if e == n * (n - 1):
    for i in range(n):
      for j in range(n):
        if i != j:
          A[i].append([j, random.randint(1, 100)])
          neighbour_index[i].append(j)
    return A, neighbour_index

  while e != 0:
    starting_index = random.randint(0, n-1)
    target_index = random.randint(0, n-1)

    while len(A[starting_index]) == n - 1: 
      starting_index = random.randint(0, n-1)

    while (starting_index == target_index) or (target_index in neighbour_index[starting_index]): 
      target_index = random.randint(0, n-1)

    A[starting_index].append([target_index, random.randint(1, 100)])
    neighbour_index[starting_index].append(target_index)
    e -= 1

  return A, neighbour_index


def incrementingN():
  name = ['n', 'e', 'time']
  filename = "B_test.csv"
  rows = []

  n_increment = []
  for i in range(10):
    n_increment.append(2 ** (i + 1))
  n_increment.pop(0)
  
  for n in n_increment:

    print("n = " + str(n) + ":")

    e = n + 1
    A_List_1, neighbour_1 = createAList(n, e)

    tic = time.time()
    heapDijkstra(0, A_List_1, neighbour_1)
    toc = time.time()

    time_elapsed = (toc - tic) * 1000000 # this is in microseconds
    

    print("e = " + str(e) + ", time elapsed = " + str(time_elapsed))

    e = n ** 2 - n
    A_List_2, neighbour_2 = createAList(n, e)

    tic = time.time()
    heapDijkstra(0, A_List_2, neighbour_2)
    toc = time.time()

    time_elapsed = (toc - tic) * 1000000 # this is in microseconds
    rows.append([time_elapsed])

    print("e = " + str(e) + ", time elapsed = " + str(time_elapsed))

  with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile) 

    csvwriter.writerow(name) 

    csvwriter.writerows(rows)


def fixed_n_500():
  name = ['n', 'e', 'time']
  filename = "B_test.csv"
  rows = []


  n = 500
  e = 500 
  while e <= 500 * 499:
    A, neighbour = createAList(n, e)
    
    tic = time.time()
    heapDijkstra(0, A, neighbour)
    toc = time.time()

    time_elapsed = (toc - tic) * 1000000 # this is in microseconds
    rows.append([time_elapsed])

    print("e = " + str(e) + ", time elapsed = " + str(time_elapsed))
    e += 10000
  
  with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile) 

    csvwriter.writerow(name) 

    csvwriter.writerows(rows)



def main():
  # uncomment to run
  # incrementingN() 
  fixed_n_500()
  pass



if __name__ == "__main__":
  main()