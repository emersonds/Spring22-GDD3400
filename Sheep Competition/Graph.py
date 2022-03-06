import Constants
import Node
import pygame
import Vector

from pygame import *
from Vector import *
from Node import *
from enum import Enum

class SearchType(Enum):
	BREADTH = 0
	DJIKSTRA = 1
	A_STAR = 2
	BEST_FIRST = 3

class Graph():
	def __init__(self):
		""" Initialize the Graph """
		self.nodes = []			# Set of nodes
		self.obstacles = []		# Set of obstacles - used for collision detection

		# Initialize the size of the graph based on the world size
		self.gridWidth = int(Constants.WORLD_WIDTH / Constants.GRID_SIZE)
		self.gridHeight = int(Constants.WORLD_HEIGHT / Constants.GRID_SIZE)

		# Create grid of nodes
		for i in range(self.gridHeight):
			row = []
			for j in range(self.gridWidth):
				node = Node(i, j, Vector(Constants.GRID_SIZE * j, Constants.GRID_SIZE * i), Vector(Constants.GRID_SIZE, Constants.GRID_SIZE))
				row.append(node)
			self.nodes.append(row)

		## Connect to Neighbors
		for i in range(self.gridHeight):
			for j in range(self.gridWidth):
				# Add the top row of neighbors
				if i - 1 >= 0:
					# Add the upper left
					if j - 1 >= 0:		
						self.nodes[i][j].neighbors += [self.nodes[i - 1][j - 1]]
					# Add the upper center
					self.nodes[i][j].neighbors += [self.nodes[i - 1][j]]
					# Add the upper right
					if j + 1 < self.gridWidth:
						self.nodes[i][j].neighbors += [self.nodes[i - 1][j + 1]]

				# Add the center row of neighbors
				# Add the left center
				if j - 1 >= 0:
					self.nodes[i][j].neighbors += [self.nodes[i][j - 1]]
				# Add the right center
				if j + 1 < self.gridWidth:
					self.nodes[i][j].neighbors += [self.nodes[i][j + 1]]
				
				# Add the bottom row of neighbors
				if i + 1 < self.gridHeight:
					# Add the lower left
					if j - 1 >= 0:
						self.nodes[i][j].neighbors += [self.nodes[i + 1][j - 1]]
					# Add the lower center
					self.nodes[i][j].neighbors += [self.nodes[i + 1][j]]
					# Add the lower right
					if j + 1 < self.gridWidth:
						self.nodes[i][j].neighbors += [self.nodes[i + 1][j + 1]]

	def getNodeFromPoint(self, point):
		""" Get the node in the graph that corresponds to a point in the world """
		point.x = max(0, min(point.x, Constants.WORLD_WIDTH - 1))
		point.y = max(0, min(point.y, Constants.WORLD_HEIGHT - 1))

		# Return the node that corresponds to this point
		return self.nodes[int(point.y/Constants.GRID_SIZE)][int(point.x/Constants.GRID_SIZE)]

	def placeObstacle(self, point, color):
		""" Place an obstacle on the graph """
		node = self.getNodeFromPoint(point)

		# If the node is not already an obstacle, make it one
		if node.isWalkable:
			# Indicate that this node cannot be traversed
			node.isWalkable = False		

			# Set a specific color for this obstacle
			node.color = color
			for neighbor in node.neighbors:
				neighbor.neighbors.remove(node)
			node.neighbors = []
			self.obstacles += [node]

	def reset(self):
		""" Reset all the nodes for another search """
		for i in range(self.gridHeight):
			for j in range(self.gridWidth):
				self.nodes[i][j].reset()

	def buildPath(self, endNode):
		""" Go backwards through the graph reconstructing the path """
		path = []
		node = endNode
		while node is not 0:
			node.isPath = True
			path = [node] + path
			node = node.backNode

		# If there are nodes in the path, reset the colors of start/end
		if len(path) > 0:
			path[0].isPath = False
			path[0].isStart = True
			path[-1].isPath = False
			path[-1].isEnd = True
		return path

	def findPath_Breadth(self, start, end):
		""" Breadth Search by Dylan Emerson """
		#print("BREADTH-FIRST")
		self.reset()

		# TODO: Add your breadth-first code here!
		# Initialize toVisit list with start node
		toVisit = [self.getNodeFromPoint(start)]
		toVisit[0].isVisited = True

		# While toVisit has nodes to visit
		while len(toVisit) > 0:

			# Remove first node from toVisit
			currentNode = toVisit.pop(0)

			# First node is "visited"
			currentNode.isExplored = True

			# Check each neighbor if it is the end node
			for neighbor in currentNode.neighbors:

				# If neighbor has not been visited
				if neighbor.isVisited == False:

					# Add it to toVisit list and "visit" it
					toVisit.append(neighbor)
					neighbor.isVisited = True

					# Set neighbor back pointer to current node
					neighbor.backNode = currentNode
					
					# Check is neighbor is the end node
					if neighbor == self.getNodeFromPoint(end):
						print("GOAL REACHED")
						return self.buildPath(neighbor)
		return []

	def findPath_Djikstra(self, start, end):
		""" Djikstra's Search by Dylan Emerson """
		#print("DJIKSTRA")
		self.reset()

		# TODO: Implement Djikstra's Search
		# Initialize priority list
		toVisit = [self.getNodeFromPoint(start)]
		toVisit[0].isVisited = True
		toVisit[0].costFromStart = 0

		while len(toVisit) > 0:
			# Sort list
			toVisit.sort(key=lambda x:x.costFromStart)

			# Remove first node from toVisit
			currentNode = toVisit.pop(0)

			# First node is "visited"
			currentNode.isExplored = True

			# Check if current node is the end node
			if currentNode == self.getNodeFromPoint(end):
				print("GOAL REACHED")
				return self.buildPath(currentNode)

			# Check each neighbor if it is the end node
			for neighbor in currentNode.neighbors:
				# Get distance from current node to neighbor
				currentDistance = (neighbor.center - currentNode.center).length()

				# If neighbor has not been visited
				if neighbor.isVisited == False:
					# Set it visited
					neighbor.isVisited = True

					# Set its cost from the starting node
					# This is the distance from current node to neighbor node,
					# plus the currentNode's cost from start
					neighbor.costFromStart = currentDistance + currentNode.costFromStart

					# Set neighbor back pointer to current node
					neighbor.backNode = currentNode

					# Add to queue
					toVisit.append(neighbor)

				# If it has been visited, check if distance is shorter
				else:
					# Check if the distance between the current neighbor and
					# the current node plus the current node cost from start
					# is less than the current neighbor's cost from start
					if currentDistance + currentNode.costFromStart < neighbor.costFromStart:
						# Shorter path has been found to neighbor, so change it's costFromStart
						# neighbor costFromStart becomes new shorter distance
						neighbor.costFromStart = currentDistance + currentNode.costFromStart
						neighbor.backNode = currentNode
		self.reset()

		return []

	def findPath_AStar(self, start, end):
		""" A Star Search by Dylan Emerson """
		#print("A_STAR")
		self.reset()

		# TODO: Implement A Star Search
		# Initialize priority queue
		toVisit = [self.getNodeFromPoint(start)]

		# Set starting node visited and cost values
		toVisit[0].isVisited = True
		toVisit[0].costFromStart = 0
		toVisit[0].costToEnd = (toVisit[0].center - self.getNodeFromPoint(end).center).length()
		toVisit[0].cost = toVisit[0].costFromStart + toVisit[0].costToEnd

		while len(toVisit) > 0:
			# Sort list
			toVisit.sort(key=lambda x:x.cost)

			# Remove first node from toVisit
			currentNode = toVisit.pop(0)

			# First node is "visited"
			currentNode.isExplored = True

			# Check if current node is the end node
			if currentNode == self.getNodeFromPoint(end):
				print("GOAL REACHED")
				return self.buildPath(currentNode)

			# Check each neighbor if it is the end node
			for neighbor in currentNode.neighbors:

				# Get distance from current node to neighbor
				currentDistance = (neighbor.center - currentNode.center).length()

				# If neighbor has not been visited
				if neighbor.isVisited == False:
					# Set it visited
					neighbor.isVisited = True

					# Set its cost from the starting node
					# This is the distance from current node to neighbor node,
					# plus the currentNode's cost from start
					neighbor.costFromStart = currentDistance + currentNode.costFromStart

					# Set its cost to the end node
					neighbor.costToEnd = (neighbor.center - self.getNodeFromPoint(end).center).length()

					# Set its total cost
					neighbor.cost = neighbor.costFromStart + neighbor.costToEnd

					# Set neighbor back pointer to current node
					neighbor.backNode = currentNode

					# Add to queue
					toVisit.append(neighbor)

				# If it has been visited, check if distance is shorter
				else:
					# Check if the distance between the current neighbor and
					# the current node plus the current node cost from start
					# is less than the current neighbor's cost from start
					if currentDistance + currentNode.costFromStart < neighbor.costFromStart:
						# Shorter path has been found to neighbor, so change it's costFromStart
						# neighbor costFromStart becomes new shorter distance
						neighbor.costFromStart = currentDistance + currentNode.costFromStart

						# Recalculate cost to end and total cost
						neighbor.costToEnd = (neighbor.center - self.getNodeFromPoint(end).center).length()
						neighbor.cost = neighbor.costFromStart + neighbor.costToEnd

						# Set back pointer to current node
						neighbor.backNode = currentNode
		return []

	def findPath_BestFirst(self, start, end):
		""" Best First Search by Dylan Emerson """
		#print("BEST_FIRST")
		self.reset()

		# TODO: Implement Best First Search
		# Initialize priority list
		toVisit = [self.getNodeFromPoint(start)]

		# First node is visited and 
		toVisit[0].isVisited = True

		# Set cost to end for start node
		toVisit[0].costToEnd = (toVisit[0].center - self.getNodeFromPoint(end).center).length()

		while len(toVisit) > 0:
			# Sort list by cost to end node
			toVisit.sort(key=lambda x:x.costToEnd)

			# Remove first node from toVisit
			currentNode = toVisit.pop(0)

			# First node is "visited"
			currentNode.isExplored = True

			# Check if current node is the end node
			if currentNode == self.getNodeFromPoint(end):
				print("GOAL REACHED")
				return self.buildPath(currentNode)

			# Check each neighbor's cost to end
			for neighbor in currentNode.neighbors:

				# If neighbor has not been visited
				if neighbor.isVisited == False:

					# Set it visited
					neighbor.isVisited = True

					# Set cost to end as distance to end node
					neighbor.costToEnd = (neighbor.center - self.getNodeFromPoint(end).center).length()

					# Set neighbor back pointer to current node
					neighbor.backNode = currentNode

					# Add to queue
					toVisit.append(neighbor)

		return []

	def draw(self, screen):
		""" Draw the graph """
		for i in range(self.gridHeight):
			for j in range(self.gridWidth):
				self.nodes[i][j].draw(screen)