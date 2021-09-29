import random
import numpy as np
import time


   
def dijkstra(A, srcNode):
  INF = 1000000  
  n = len(A)

  status = [False for i in range(n)]
  dist = [INF for i in range(n)]
  dist[srcNode] = 0
  Q = dist.copy() # both Q and dist has [0, INF, INF, INF, etc]


  while not checkEmpty(Q):
    u = extractCheapest(Q)
    if (u == -1) :
      raise Exception("Something Wrong")
    
    status[u] = True
    for nb in range(n): 
      neighbour_arr = A[u]
      # if neighbour_arr[nb] == 0: continue
      if status[nb] == False and dist[nb] > dist[u] + neighbour_arr[nb]:
        dist[nb] = dist[u] + neighbour_arr[nb]
        Q[nb] = dist[nb]
        # put n back in Q in increasing order of dist

  print(dist)
    
  
def checkEmpty(Q):
  for i in range(len(Q)):
    if Q[i] != -1:
      return False
  return True  


def extractCheapest(Q): # extracts node with smallest dist and remove it from queue

  min = 1000000
  minnode = -1 # initialising 

  for i in range(len(Q)): # going through each node
    if min > Q[i] and Q[i] >= 0: # there is a smaller cost than min
      min = Q[i]
      minnode = i      
       
  Q[minnode] = -1
  return minnode    


def createGraph(n, e):
  A = [[0 for x in range(n)] for y in range(n)] 

  randomVertices = [] # creating a list of vertices with edges
  while e != 0:
    r_1 = random.randint(0, n-1)
    r_2 = random.randint(0, n-1)
    while r_2 == r_1:
      r_2 = random.randint(0, n-1)
    if (r_1, r_2) in randomVertices:
      continue
    randomVertices.append((r_1, r_2))
    e -= 1

  for i in range(n):
    for j in range(n):
      if i == j:
        A[i][j] = 0
      elif (i, j) in randomVertices:
        A[i][j] = random.randint(1, 100) # inputting the weight into the previously found edges
      else: continue
  
  return A


def main():


  # n_increment = []
  # for i in range(19):
  #   n_increment.append(2 ** (i + 1))
  
  # for var_n in n_increment:
  #   var_e = var_n ** 2 - var_n
  #   while var_e >= 2 * var_n + 3:
  #     n = var_n
  #     e = var_e
  #     A_Matrix = createGraph(n, e)
  #     G = Graph(n)
  #     G.graph = A_Matrix

  #     tic = time.time()
  #     G.dijkstra(0)
  #     toc = time.time()

  #     time_elapsed = (toc - tic) * 1000000 # this is in microseconds

  #     print("n = " + str(var_n) + ", e = " + str(var_e) + ", time elapsed = " + str(time_elapsed))
  #     var_e /= 2


  # A = createGraph(5, 14)
  # print(np.array(A))


  # #  confirms that code is working
  n = 500
  e = n
  while e <= n * (n - 1):
    A = createGraph(n, e) # n is the number of vertices, e is the number of edges with weight (e >= n - 1)
    tic = time.time()
    dijkstra(A, 0)
    toc = time.time()
    time_elapsed = (toc - tic) * 1000000
    print("n = " + str(n) + ", e = " + str(e) + ", time elapsed = " + str(time_elapsed))
    e += 100


  return

if __name__ == "__main__":
  main()