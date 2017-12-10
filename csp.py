class Gra:
    def __init__(self):
    
      self.Plimit = 3
      self.Qlimit = 2
      self.Rlimit = 1
         
      # Country with respective persons Graph
      self.graph = {
        'P': ['x', 'y', 'z'],
        'Q': ['a', 'b'],
        'R': ['s']
      }
    
       # array of rooms
      self.rooms = ['A', 'B', 'C', 'D', 'E', 'F']
    
      # array of countries
      self.countries = ['P', 'Q', 'R']
      
      # array of All hotel rooms assigned to person (currently all empty)
      self.roomAssigned = {
        'A': None,
        'B': None,
        'C': None,
        'D': None,
        'E': None,
        'F': None,
      }
      
      # adjacency matrix of Nodes A to F
      self.adjM = {
        'A': [1,1,1,0,0,0], 
        'B': [1,1,1,0,0,0],
        'C': [1,1,1,1,1,0], 
        'D': [0,0,1,1,1,1],
        'E': [0,0,1,0,1,0], 
        'F': [0,0,0,1,0,1]  
      }
      
      self.P_count = 0
      self.Q_count = 0
      self.R_count = 0
      
    def isPossible(self, node, country):
      
      for index in range(len(self.rooms)):
        node1 = self.rooms[index]
        if self.adjM[node][index] == 1 and country == self.roomAssigned[node1]:
          return False
      return True
   
    def csp(self, indx):
      nodeIndex = indx
      node = self.rooms[nodeIndex]
      for i in range(len(self.countries)):
        if self.isPossible(node, self.countries[i]):
          
          if self.iscorrect(self.countries[i]):
           
            self.roomAssigned[node] = self.countries[i]
          if nodeIndex + 1 < 6:
            nodeIndex += 1
            self.csp(nodeIndex)
          else:
            self.allocatePersonsToRooms()
            return
          
    def iscorrect(self, country):
      if country == "P":
        if self.P_count < self.Plimit:
          self.P_count += 1
          return True
      
      if country == "Q":
        if self.Q_count < self.Qlimit:
          self.Q_count += 1
          return True
      
      if country == "R":
        if self.R_count < self.Rlimit:
          self.R_count += 1
          return True

      return False
           
    def allocatePersonsToRooms(self):
      arrayP = self.graph['P']
      arrayQ = self.graph['Q']
      arrayR = self.graph['R']
      PIndex = 0
      QIndex = 0
      RIndex = 0
      
      for x in range(len(self.rooms)):
        if self.roomAssigned[self.rooms[x]] == 'P':
          self.roomAssigned[self.rooms[x]] = arrayP[PIndex]
          PIndex += 1
        if self.roomAssigned[self.rooms[x]] == 'Q':
          self.roomAssigned[self.rooms[x]] = arrayQ[QIndex]
          QIndex += 1
        if self.roomAssigned[self.rooms[x]] == 'R':
          self.roomAssigned[self.rooms[x]] = arrayR[RIndex]
          RIndex += 1
              
g = Gra()
g.csp(0)
print "results" 
print g.roomAssigned

