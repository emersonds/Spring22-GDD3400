from Constants import *
from pygame import *
from random import *
from Vector import *
from Agent import *
from Sheep import *
from Dog import *
from Graph import *
from Node import *
from GameState import *

class StateMachine:
	""" Machine that manages the set of states and their transitions """

	def __init__(self, startState):
		""" Initialize the state machine and its start state"""
		self.__currentState = startState
		self.__currentState.enter()

	def getCurrentState(self):
		""" Get the current state """
		return self.__currentState

	def update(self, gameState):
		""" Run the update on the current state and determine if we should transition """
		nextState = self.__currentState.update(gameState)

		# If the nextState that is returned by current state's update is not the same
		# state, then transition to that new state
		if nextState != None and type(nextState) != type(self.__currentState):
			self.transitionTo(nextState)

	def transitionTo(self, nextState):
		""" Transition to the next state """
		self.__currentState.exit()
		self.__currentState = nextState
		self.__currentState.enter()

	def draw(self, screen):
		""" Draw any debugging information associated with the states """
		self.__currentState.draw(screen)

class State:
	def enter(self):
		""" Enter this state, perform any setup required """
		print("Entering " + self.__class__.__name__)
		
	def exit(self):
		""" Exit this state, perform any shutdown or cleanup required """
		print("Exiting " + self.__class__.__name__)

	def update(self, gameState):
		""" Update this state, before leaving update, return the next state """
		print("Updating " + self.__class__.__name__)

	def draw(self, screen):
		""" Draw any debugging info required by this state """
		pass

			   
class FindSheepState(State):
	""" This is an example state that simply picks the first sheep to target """

	def update(self, gameState):
		""" Update this state using the current gameState """
		super().update(gameState)
		dog = gameState.getDog()

		# Pick a random sheep
		dog.setTargetSheep(gameState.getHerd()[0])

		# You could add some logic here to pick which state to go to next
		# depending on the gameState

		if (len(gameState.getHerd()) == 0):
			return Idle()
		else:
			return ApproachSheepState()

class ApproachSheepState(State):
	""" This is a state where the dog moves to a point that puts the \
		sheep between the dog and pen """

	def update(self, gameState):
		""" Update this state using the current gameState """
		super().update(gameState)
		dog = gameState.getDog()
		sheep = dog.getTargetSheep()
		pen = gameState.getPenBounds()	# [0] = entrance, [1] = inside
		entrance = pen[0]	# rect(top left x, top y, width, height)
		entranceLeftX = entrance[0]	# Left
		entranceY = entrance[1]		# Top
		entranceRightX = entranceLeftX + entrance[2]	# left + width = right
		entranceMiddle = Vector(entranceLeftX + (entrance[2] * 0.5), entranceY)

		# Find a point that puts sheep between dog and pen
		if not dog.isFollowingPath:
			# If sheep is above pen, find path to push it down
			# Use upper buffer to prevent dog pushing sheep into side of pen
			# This should transition to PushIntoPenState
			if sheep.center.y < (entranceY - Constants.PEN_UPPER_BUFFER):
				if sheep.center.x < entranceLeftX:
					print ("Sheep above and to the left of entrance")
					# Path dog towards a point that would push the sheep into pen
					dogTarget = Vector(sheep.center.x - 20, sheep.center.y - 20)
					dog.calculatePathToNewTarget(dogTarget)
				elif sheep.center.x > entranceRightX:
					print ("Sheep above and to the right of entrance")
					# Path dog towards a point that would push the sheep into pen
					dogTarget = Vector(sheep.center.x + 20, sheep.center.y - 20)
					dog.calculatePathToNewTarget(dogTarget)
				else:
					print ("Sheep above and in the middle of entrance")
					# Path dog towards a point that would push the sheep into pen
					dogTarget = Vector(sheep.center.x, sheep.center.y - 20)
					dog.calculatePathToNewTarget(dogTarget)
			# If sheep is below pen, find path to push it up
			# Use upper buffer to prevent dog pushing sheep into side of pen
			# This should transition to SteerSheepAbovePenState
			# elif sheep.center.y > entranceY: # sheep below pen
			# 	if dog.center.y < sheep.center.y: # dog above sheep
			# 		if sheep.center.x > entranceMiddle.x: # sheep is to right of pen entrance
			# 			targPos = Vector(sheep.center.x - 50, sheep.center.y + 20) # Move dog slightly left of sheep & slightly below
			# 			dog.calculatePathToNewTarget(targPos)
			# 		if sheep.center.x < entranceMiddle.x: # sheep is to left of pen entrance
			# 			targPos = Vector(sheep.center.x + 50, sheep.center.y + 20) # Move dog slightly right of sheep & slightly below
			# 			dog.calculatePathToNewTarget(targPos)
			# 	if dog.center.y >= sheep.center.y: # dog is below or at same level as sheep
			# 		if sheep.center.x > entranceLeftX and sheep.center.x < entranceRightX: # check if sheep is within pen bounds
			# 			if sheep.center.x > sheep.center: # sheep is to right of pen entrance
			# 				targPos = Vector(sheep.center.x - 50, sheep.center.y + 20) # Move dog slightly left of sheep & slightly below
			# 				dog.calculatePathToNewTarget(targPos)
			# 			if sheep.center.x < entranceMiddle.x: # sheep is to left of pen entrance
			# 				targPos = Vector(sheep.center.x + 50, sheep.center.y + 20) # Move dog slightly right of sheep & slightly below
			# 				dog.calculatePathToNewTarget(targPos)
			# 		elif sheep.center.x < entranceLeftX or sheep.center.x > entranceRightX: #sheep is outside of pen bounds
			# 			dog.calculatePathToNewTarget(sheep.center)


class SteerSheepAbovePenState(State):
	""" This is a state that loops until the sheep is above the pen """
	pass

class PushIntoPenState(State):
	""" This is a state where the dog pushes the sheep into the pen """
	pass

class Idle(State):
	""" This is an idle state where the dog does nothing """

	def update(self, gameState):
		super().update(gameState)
		
		# Do nothing
		if len(gameState.getHerd()) > 0:
			return FindSheepState()
		else:
			return Idle()