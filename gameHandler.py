from time import sleep
from .Variables import *
from .gameController import gameController
from .Tools import *
import asyncio
import math

class gameHandler:
	"""Class keeping track of what's unlock for the game and handling interaction with the game."""
	lives = None
	power = None
	endings = None
	stages = None

	difficulties = None
	characters = None

	gameController = None
	lastSpeeds = []

	bossBeaten = []
	extraBeaten = []

	firstCharacterUnlocked = False

	limitLives = 8

	def __init__(self):
		self.gameController = gameController()
		self.reset()
		self.initGame()

	#
	# Init Resources
	#

	def giveLives(self):
		self.gameController.setLives(self.lives)

	def givePower(self):
		self.gameController.setPower(self.power)

	def setDifficulty(self, excludeEasy = False):
		self.gameController.setDifficulty(self.getLowestDifficulty(excludeEasy))

	def updateStageList(self, practiceMode = True):
		for characters in CHARACTERS:
			for shot in SHOTS:
				for difficulty in range(4):
					for stage in range(6):
						access = 0
						# If we are not in practice mode, we do not update the stage
						if practiceMode and self.characters[characters][shot] and self.difficulties[difficulty] and self.stages[characters][shot][stage]:
							access = 1

						self.gameController.setCharacterStage(characters, shot, difficulty, stage, access)

	def updatePracticeScore(self, locations, checked_location):
		scores = {}
		for character in CHARACTERS:
			scores[character] = {}
			for shot in SHOTS:
				scores[character][shot] = {}
				for difficulty in range(4):
					scores[character][shot][difficulty] = {}
					for stage in range(8):
						scores[character][shot][difficulty][stage] = [0, 0]

		# We check each locations to see which one has been done
		for id, location_data in locations.items():
			if id in checked_location and id < STARTING_ID + 60000:
				character = location_data[0]
				stage = location_data[1]
				counter = location_data[2]
				shot_type = location_data[3]
				difficulty = location_data[4]

				# If it's not the Extra stage
				if stage < 7:
					if difficulty >= 0:
						if shot_type in SHOTS:
							scores[character][shot_type][difficulty][stage][counter] += 1
						else:
							for shot in SHOTS:
								scores[character][shot][difficulty][stage][counter] += 1
					else:
						if shot_type in SHOTS:
							scores[character][shot_type][EASY][stage][counter] += 1
							scores[character][shot_type][NORMAL][stage][counter] += 1
							scores[character][shot_type][HARD][stage][counter] += 1
							scores[character][shot_type][LUNATIC][stage][counter] += 1
						else:
							for shot in SHOTS:
								scores[character][shot][EASY][stage][counter] += 1
								scores[character][shot][NORMAL][stage][counter] += 1
								scores[character][shot][HARD][stage][counter] += 1
								scores[character][shot][LUNATIC][stage][counter] += 1

		# We set the scores depending on the counter
		for character in CHARACTERS:
			for shot in SHOTS:
				for difficulty in range(4):
					for stage in range(6):
						score = 0
						if stage == 5:
							if scores[character][shot][difficulty][stage][0] > 0:
								score += 999999999
						else:
							if scores[character][shot][difficulty][stage][0] > 0:
								score += 555555555
							if scores[character][shot][difficulty][stage][1] > 0:
								score += 444444444

						self.gameController.setPracticeStageScore(character, shot, difficulty, stage, score)

	def updateExtraUnlock(self, otherMode = False):
		"""
		Update access to the Extra stage
		"""

		if self.canExtra() or otherMode:
			for characters in CHARACTERS:
				for shot in SHOTS:
					if self.characters[characters][shot] and (self.hasExtra[characters][shot] or otherMode):
						self.gameController.setCharacterStage(characters, shot, EXTRA, -1, 1)
					else:
						self.gameController.setCharacterStage(characters, shot, EXTRA, -1, 0)
		else:
			for characters in CHARACTERS:
				for shot in SHOTS:
					self.gameController.setCharacterStage(characters, shot, EXTRA, -1, 0)

	#
	# Boss
	#

	def isCurrentBossDefeated(self, counter):
		isDefeated = False
		# If it's the extra stage
		if self.gameController.getStage() == 7:
			isDefeated = self.extraBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][counter]
		else:
			isDefeated = self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][self.gameController.getDifficulty()][self.gameController.getStage()-1][counter]

		return isDefeated

	def setCurrentStageBossBeaten(self, counter, otherDifficulties = False):
		"""
		Set the boss of the current stage with the current character as beaten.
		"""

		if self.gameController.getStage() == 7:
			self.extraBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][counter] = True
		else:
			self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][self.gameController.getDifficulty()][self.gameController.getStage()-1][counter] = True
			if otherDifficulties:
				if self.difficulties[EASY]:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][EASY][self.gameController.getStage()-1][counter] = True
				if self.difficulties[NORMAL] and self.gameController.getDifficulty() >= 1:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][NORMAL][self.gameController.getStage()-1][counter] = True
				if self.difficulties[HARD] and self.gameController.getDifficulty() >= 2:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][HARD][self.gameController.getStage()-1][counter] = True
				if self.difficulties[LUNATIC] and self.gameController.getDifficulty() >= 3:
					self.bossBeaten[self.gameController.getCharacter()][self.gameController.getShotType()][LUNATIC][self.gameController.getStage()-1][counter] = True

	def setBossBeaten(self, character, stage, counter, shot_type = -1, difficulty = -1):
		# If we have a valid difficulty
		if difficulty >= 0 and difficulty < 4 and stage < 6:
			if shot_type in SHOTS:
				self.bossBeaten[character][shot_type][difficulty][stage][counter] = True
			else:
				for shot in SHOTS:
					self.bossBeaten[character][shot][difficulty][stage][counter] = True
		# If it's the Extra Stage
		elif stage == 6:
			if shot_type in SHOTS:
				self.extraBeaten[character][shot_type][counter] = True
			else:
				for shot in SHOTS:
					self.extraBeaten[character][shot][counter] = True
		# Else, we check all difficulties
		else:
			if shot_type in SHOTS:
				for diff in range(4):
					self.bossBeaten[character][shot_type][diff][stage][counter] = True
			else:
				for shot in SHOTS:
					for diff in range(4):
						self.bossBeaten[character][shot][diff][stage][counter] = True

	def isBossBeaten(self, character, stage, counter, shot_type = -1, difficulty = -1):
		flags = []
		# If we have a valid difficulty
		if difficulty >= 0 and difficulty < 4 and stage < 6:
			if shot_type in SHOTS:
				flags.append(self.bossBeaten[character][shot_type][difficulty][stage][counter])
			else:
				for shot in SHOTS:
					flags.append(self.bossBeaten[character][shot][difficulty][stage][counter])
		# If it's the Extra Stage
		elif stage == 6:
			if shot_type in SHOTS:
				flags.append(self.extraBeaten[character][shot_type][counter])
			else:
				for shot in SHOTS:
					flags.append(self.extraBeaten[character][shot][counter])
		# Else, we check all difficulties
		else:
			if shot_type in SHOTS:
				for diff in range(4):
					flags.append(self.bossBeaten[character][shot_type][diff][stage][counter])
			else:
				for shot in SHOTS:
					for diff in range(4):
						flags.append(self.bossBeaten[character][shot][diff][stage][counter])

		return True if True in flags else False

	#
	# Get Handler Functions
	#

	def getLives(self):
		return min(self.lives, self.limitLives)

	def getPower(self):
		return self.power

	def getEndings(self):
		return self.endings

	def getLowestDifficulty(self, excludeEasy = False):
		"""
		Retrieve the lowest difficulty unlocked.
		"""
		difficulty = 3
		if(self.difficulties[EASY] and not excludeEasy):
			difficulty = 0
		elif(self.difficulties[NORMAL] or (self.difficulties[EASY] and excludeEasy)):
			difficulty = 1
		elif(self.difficulties[HARD]):
			difficulty = 2

		return difficulty

	def canExtra(self):
		"""
		If any character can access to the Extra stage.
		"""
		can = False
		for character in CHARACTERS:
			for shot in SHOTS:
				if self.characters[character][shot] and self.hasExtra[character][shot]:
					can = True
					break

		return can

	#
	# Get Games Functions
	#

	def getGameMode(self):
		return self.gameController.getGameMode()

	def getMenu(self):
		return self.gameController.getMenu()

	def getDifficulty(self):
		return self.gameController.getDifficulty()

	def getMisses(self):
		return self.gameController.getMisses()

	def getCurrentLives(self):
		return self.gameController.getLives()

	def isBossPresent(self, counter = -1):
		# If we are in stage 2 or 3 we check differently
		check = False
		try:
			if self.gameController.getStage() == 2 or self.gameController.getStage() == 3:
				check = self.gameController.getIsBossPresent2() != 0 or self.gameController.getIsBossPresent1() != 0
			# Extra Stage Midboss is also checked differently
			elif self.gameController.getStage() == 7 and counter == 0:
				check = self.gameController.getIsBossPresent2() != 0
			else:
				check = self.gameController.getIsBossPresent1() != 0
		except:
			pass

		return check

	def getCurrentStage(self):
		return self.gameController.getStage()

	def getCurrentPowerPoint(self):
		return self.gameController.getPower()

	def getCurrentScore(self):
		return self.gameController.getScore()

	def getCursorPosition(self):
		return self.gameController.getMenuCursor()

	def getCurrentCharacter(self):
		return self.gameController.getCharacter()
	
	def isInExtraMode(self):
		return self.gameController.getExtraMode() == 4

	#
	# Set Items Functions
	#

	def addLife(self, addInLevel = True):
		if(self.lives < 8):
			self.lives += 1

		self.gameController.setPracticeStartingLives(self.getLives())
		self.gameController.setNormalContinueLives(self.getLives())

		if addInLevel and self.gameController.getGameMode() == IN_GAME:
			try:
				self.gameController.setLives(self.gameController.getLives() + 1)
			except:
				pass

	def addPower(self, power):
		if(self.power+power < 100):
			self.power += power
		else:
			self.power = 100

		self.gameController.setStartingPowerPoint(self.power)

		if self.gameController.getGameMode() == IN_GAME:
			if self.gameController.getPower()+power < 100:
				self.gameController.setPower(self.gameController.getPower() + power)
			else:
				self.gameController.setPower(100)

	def addProgressiveStage(self, extra = False, character = -1, shot_type = -1):
		character_list = [character] if character > -1 else CHARACTERS
		shot_list = [shot_type] if shot_type > -1 else SHOTS

		for character in character_list:
			for shot in shot_list:
				no_new_stage = True
				for i in range(len(self.stages[character][shot])):
					if self.stages[character][shot][i] == 0:
						self.stages[character][shot][i] = 1
						no_new_stage = False
						break

				if(no_new_stage and extra):
					self.unlockExtraStage(character)

	def addStage(self, stage, character = -1, shot_type = -1):
		character_list = [character] if character > -1 else CHARACTERS
		shot_list = [shot_type] if shot_type > -1 else SHOTS

		for character in character_list:
			for shot in shot_list:
				if self.stages[character][shot][stage] == 0:
					self.stages[character][shot][stage] = 1

	def addEnding(self, character, type):
		self.endings[character][type] += 1

	def unlockDifficulty(self, difficulty):
		self.difficulties[difficulty] = True

	def unlockExtraStage(self, character = -1, shot_type = -1):
		# Unlock for one character/shot type
		if character > -1 and shot_type > -1:
			self.hasExtra[character][shot_type] = True
		# Unlock for one character
		elif character > -1:
			for shot in SHOTS:
				self.hasExtra[character][shot] = True
		# Unlock for all characters
		else:
			for character in CHARACTERS:
				for shot in SHOTS:
					self.hasExtra[character][shot] = True

	def unlockCharacter(self, character, shot_type):
		self.characters[character][shot_type] = True

	def setLivesLimit(self, limit):
		if limit >= 0 and limit <= 8:
			self.limitLives = limit
			self.gameController.setPracticeStartingLives(self.getLives())
			self.gameController.setNormalContinueLives(self.getLives())

	#
	# Traps
	#

	def halfPowerPoint(self):
		if(self.gameController.getPower() > 0):
			self.gameController.setPower(self.gameController.getPower() // 2)

	def loseLife(self):
		if(self.gameController.getLives() > 0):
			self.gameController.setLives(self.gameController.getLives() - 1)

	def powerPointDrain(self):
		if(self.gameController.getPower() > 0):
			self.gameController.setPower(self.gameController.getPower() - 1)

	def reverseControls(self):
		self.gameController.setNormalSpeed(self.gameController.getNormalSpeed()*-1)
		self.gameController.setFocusSpeed(self.gameController.getFocusSpeed()*-1)
		self.gameController.setNormalSpeedD(self.gameController.getNormalSpeedD()*-1)
		self.gameController.setFocusSpeedD(self.gameController.getFocusSpeedD()*-1)

	def ayaSpeed(self):
		self.gameController.setNormalSpeed(self.gameController.getNormalSpeed()*4)
		self.gameController.setFocusSpeed(math.floor(self.gameController.getFocusSpeed()/4))
		self.gameController.setNormalSpeedD(self.gameController.getNormalSpeedD()*4)
		self.gameController.setFocusSpeedD(math.floor(self.gameController.getFocusSpeedD()/4))

	def freeze(self):
		self.lastSpeeds = [self.gameController.getNormalSpeed(), self.gameController.getFocusSpeed(), self.gameController.getNormalSpeedD(), self.gameController.getFocusSpeedD()]
		self.gameController.setNormalSpeed(0)
		self.gameController.setFocusSpeed(0)
		self.gameController.setNormalSpeedD(0)
		self.gameController.setFocusSpeedD(0)

	def resetSpeed(self):
		self.gameController.setNormalSpeed(self.lastSpeeds[0])
		self.gameController.setFocusSpeed(self.lastSpeeds[1])
		self.gameController.setNormalSpeedD(self.lastSpeeds[2])
		self.gameController.setFocusSpeedD(self.lastSpeeds[3])

	#
	# Other
	#

	def reconnect(self):
		self.gameController = gameController()
		self.initGame()

	def initGame(self):
		self.firstCharacterUnlocked = False

		self.gameController.initStartingPower()

		self.gameController.setPracticeStartingLives(self.lives)
		self.gameController.setNormalContinueLives(self.lives)
		self.gameController.setStartingPowerPoint(self.power)

		self.gameController.initSoundHack()
		self.gameController.initCursorHack()
		self.gameController.setLockToAllDifficulty()
		self.gameController.disableDemo()

	def reset(self):
		"""
		Method that initialize all the variables to their default values.
		"""
		# Default Value
		self.lives = 0
		self.power = 0

		self.stages = {}
		for character in CHARACTERS:
			self.stages[character] = {}
			for shot in SHOTS:
				self.stages[character][shot] = [1, 0, 0, 0, 0, 0]

		self.endings = {}
		for character in CHARACTERS:
			self.endings[character] = {}
			for ending in ENDINGS:
				self.endings[character][ending] = 0

		self.hasExtra = {}
		for character in CHARACTERS:
			self.hasExtra[character] = {}
			for shot in SHOTS:
				self.hasExtra[character][shot] = False

		self.difficulties = {LUNATIC: True, HARD: False, NORMAL: False, EASY: False}

		self.characters = {}
		for character in CHARACTERS:
			self.characters[character] = {}
			for shot in SHOTS:
				self.characters[character][shot] = False

		self.bossBeaten = {}
		for character in CHARACTERS:
			self.bossBeaten[character] = {}
			for shot in SHOTS:
				self.bossBeaten[character][shot] = {}
				for difficulty in range(4):
					self.bossBeaten[character][shot][difficulty] = [[False, False], [False, False], [False, False], [False, False], [False, False], [False]]

		self.extraBeaten = {}
		for character in CHARACTERS:
			self.extraBeaten[character] = {}
			for shot in SHOTS:
				self.extraBeaten[character][shot] = [False, False]

		self.lastSpeeds = [0, 0, 0, 0]

	def playSound(self, soundId):
		self.gameController.setCustomSoundId(soundId)

	async def killPlayer(self):
		self.gameController.setKill(True)
		await asyncio.sleep(0.1)
		self.gameController.setKill(False)

	def giveCurrentPowerPoint(self, power):
		"""
		Give power point to the current stage
		"""
		if self.gameController.getGameMode() == IN_GAME:
			new_power = self.gameController.getPower() + power
			if(new_power > 128):
				new_power = 128
			elif(new_power < 0):
				new_power = 0

			self.gameController.setPower(new_power)

	def updateCursor(self, minValue = -1):
		"""
		Update the minimum cursor position value authorized.
		If -1, it will be the lowest difficulty.
		If -2, it will lock to 1 if the Extra Stage is not unlocked by any character.
		"""
		if minValue == -2:
			minValue = 1 if not self.canExtra() else 0
		else:
			minValue = self.getLowestDifficulty() if minValue == -1 else minValue
		self.gameController.setMinimumCursorDown(minValue)
		self.gameController.setMinimumCursorUp(minValue)

		# If the cursor is "out of bounds", we set it to the minimum value authorized
		if self.gameController.getMenuCursor() < minValue:
			self.gameController.setMenuCursor(minValue)

	def checkIfCurrentIsPossible(self, isNormalMode = False):
		"""
		Check if the current combinaison is a possible one we what is unlocked
		"""
		possible = True

		# Check difficulty
		if self.getDifficulty() < self.getLowestDifficulty():
			possible = False

		# Check character
		if not self.characters[self.gameController.getCharacter()][self.gameController.getShotType()]:
			possible = False

		# Check stage
		if not isNormalMode and (self.gameController.getStage() < 7 and self.stages[self.gameController.getCharacter()][self.gameController.getShotType()][self.gameController.getStage()-1] == 1) and (self.gameController.getStage() == 7 and self.hasExtra[self.gameController.getCharacter()][self.gameController.getShotType()]):
			possible = False

		return possible