#Program to find the Minimum Spanning Tree using Prim's Algorithm and Heap Data Structure

import sys

#Implementation of Heap
class Heap:
	
	s = 0
	a = []
	p = {}
	key = {}

	def __init__(self):
		self.s = -1

	def heapify_up(self, i):
		while i>0:
			j = i//2
			if self.key[self.a[i]] < self.key[self.a[j]]:
				temp = self.a[i]
				self.a[i] = self.a[j]
				self.a[j] = temp
				self.p[self.a[i]] = i
				self.p[self.a[j]] = j
				i = j
			else:
			 	break

	def heapify_down(self,i):
		j=-1
		while 2*i <= self.s:
			if 2*i == self.s or self.key[self.a[2*i]] <= self.key[self.a[2*i + 1]]:
				j = 2*i
			else:
				j = 2*i + 1
			if self.key[self.a[j]] < self.key[self.a[i]]:
				temp = self.a[i]
				self.a[i] = self.a[j]
				self.a[j] = temp
				self.p[self.a[i]] = i
				self.p[self.a[j]] = j
				i = j
			else:
				break
	
	def decrease_key(self, v, key_value):
		self.key[v] = key_value
		self.heapify_up(self.p[v])

	def extract_min(self):
		ret = self.a[0]
		self.a[0]=self.a[self.s]
		self.p[self.a[0]] = 0
		self.s-=1
		if self.s>=0:
			self.heapify_down(0)
		return ret

	def insert(self, v, key_value):
		self.a.append(v)
		self.s +=1
		self.p[v] = self.s
		self.key[v] = key_value
		self.heapify_up(self.s)

	def printdata(self):
		print "Value of array a: ", self.a
		print "Value of p: ", self.p
		print "Value of key: ", self.key

#Reading data from file
f = open("input.txt")
lines = f.readlines()
f.close()

#Global variables for the Minimum Spanning Tree
Q = Heap()
n,m = map(int,lines[0].strip().split(" "))
edges = [[-1 for x in range(0,n+1)] for y in range(0,n+1)]
d = {}
pi = {}
S = []
V = []
total_weight = 0
edges_mst = [None]*(n-1)

#Add all nodes to the list V
for i in range(1,n+1):
	V.append(i)

#Add all edges to the edges matrix 
for i in range(0,m):
	p,q,r = map(int,lines[i+1].strip().split(" "))
	edges[p][q] = r
	edges[q][p] = r #Adding the edges for both because it is an undirected graph

#Choosing the Arbitrary vertex as "Vertex 1" 
d[1] = 0
Q.insert(1,d[1])

#Inserting the Infinity value for all other vertices
for i in range(1,n+1):
	d[i] = sys.maxint
	Q.insert(i,d[i])

#Finding the Minimum Spanning Tree
while set(S)!=set(V):
	u = Q.extract_min()
	S.append(u)
	left = list(set(V) - set(S))
	for v in left:
		if edges[u][v] != -1:
			if edges[u][v] < d[v]:
				d[v] = edges[u][v]
				Q.decrease_key(v,d[v])
				pi[v] = u

#Adding the list of edges into a string array and calculating total weight
i = 0
for v in list(set(V) - set({1})):
	total_weight+=edges[v][pi[v]]	
	if v < pi[v]:
		edges_mst[i] = str(v) + " " + str(pi[v]) + " " + str(edges[v][pi[v]])		
	else:
		edges_mst[i] = str(pi[v]) + " " + str(v) + " " + str(edges[v][pi[v]])
	i+=1

#Writing Output to the file
with open("output.txt",'w') as f:
	f.write(str(total_weight)+"\n")
	for i in range(0, n-1):
		f.write(edges_mst[i]+ "\n")