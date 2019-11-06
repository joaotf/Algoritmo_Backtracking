from collections import defaultdict 

class Graph: 
   
    def __init__(self,vertices): 

        self.V= vertices  
        self.graph = defaultdict(list)  
   
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   

    def printAllPathsUtil(self, u, d, visited, path): 
        visited[u]= True
        path.append(u) 

        if u ==d: 
            print(path)
        else: 
            for i in self.graph[u]: 
                if visited[i]==False: 
                    self.printAllPathsUtil(i, d, visited, path) 

        path.pop() 
        visited[u]= False

    def printAllPaths(self,s, d): 
        visited =[False]*(self.V)       
        path = [] 
        self.printAllPathsUtil(s, d,visited, path) 
   
   
   
g = Graph(9) 

g.addEdge(0, 1) 
g.addEdge(0, 7)
g.addEdge(1, 7)
g.addEdge(1, 2)
g.addEdge(7, 6)
g.addEdge(7, 8)
g.addEdge(8, 6)
g.addEdge(8, 2)
g.addEdge(2, 3)
g.addEdge(2, 5)
g.addEdge(6, 5)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 6)

   
a = int(input("Digite o inicio\n"))
b = int(input("Digite o fim\n"))
g.printAllPaths(a,b) 
