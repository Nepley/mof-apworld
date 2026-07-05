from typing import Optional
import asyncio
import colorama
import time
import random
from .gameHandler import *
from .Tools import *
import traceback
from kivy.uix.boxlayout import BoxLayout
from kvui import GameManager

from CommonClient import (
	CommonContext,
	ClientCommandProcessor,
	get_base_parser,
	logger,
	server_loop,
	gui_enabled,
)

class TouhouClientProcessor(ClientCommandProcessor):
	def _cmd_multiple_difficulty_check(self, active = None):
		"""Toggle the possibility to check multiple difficulty check by doing the highest difficulty
		:param active: If "on" or "true", enable it. If "off" or "false", disable it."""
		changed = False
		if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
			if active is not None:
				if active.lower() in ["on", "true"]:
					self.ctx.check_multiple_difficulty = True
					changed = True
					logger.info("Multiple difficulty check enabled")
				elif active.lower() in ("off", "false"):
					self.ctx.check_multiple_difficulty = False
					changed = True
					logger.info("Multiple difficulty check disabled")
				else:
					logger.error("Invalid argument, use 'on' or 'off'")
			else:
				logger.info(f"Multiple difficulty check is {'enabled' if self.ctx.check_multiple_difficulty else 'disabled'}")
		else:
			logger.error("Multiple difficulty check cannot be changed before connecting to the game and server")

		return changed

	# def _cmd_deathlink(self, active = None):
	# 	"""Toggle DeathLink on or off
	#     :param active: If "on" or "true", enable DeathLink. If "off" or "false", disable DeathLink."""
	# 	changed = False
	# 	if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
	# 		if active is not None:
	# 			if active.lower() in ["on", "true"]:
	# 				if "DeathLink" not in self.ctx.tags:
	# 					self.ctx.tags.add("DeathLink")
	# 					self.ctx.death_link_is_active = True
	# 					changed = True
	# 				logger.info("DeathLink enabled")
	# 			elif active.lower() in ("off", "false"):
	# 				if "DeathLink" in self.ctx.tags:
	# 					self.ctx.tags.remove("DeathLink")
	# 					self.ctx.death_link_is_active = False
	# 					changed = True
	# 				logger.info("DeathLink disabled")
	# 			else:
	# 				logger.error("Invalid argument, use 'on' or 'off'")

	# 			if changed:
	# 				asyncio.create_task(self.ctx.send_msgs([{"cmd": "ConnectUpdate", "tags": self.ctx.tags}]))
	# 		else:
	# 			logger.info(f"DeathLink is {'enabled' if self.ctx.death_link_is_active else 'disabled'}")
	# 	else:
	# 		logger.error("DeathLink cannot be changed before connecting to the game and server")

	# 	return changed

	# def _cmd_deathlink_trigger(self, value = None):
	# 	"""Get or Set the trigger for the DeayhLink trigger
	#     :param value: Possibler values are "life" or "gameover"
	# 	"""
	# 	if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
	# 		if value is not None:
	# 			if value.lower() == "life":
	# 				self.ctx.death_link_trigger = DEATH_LINK_LIFE
	# 				logger.info("DeathLink trigger set to 'Life'")
	# 				return True
	# 			elif value.lower() == "gameover":
	# 				self.ctx.death_link_trigger = DEATH_LINK_GAME_OVER
	# 				logger.info("DeathLink trigger set to 'Game Over'")
	# 				return True
	# 			else:
	# 				logger.error("Invalid argument, use 'life' or 'gameover'")
	# 				return False
	# 		else:
	# 			trigger = "Life" if self.ctx.death_link_trigger == DEATH_LINK_LIFE else "Game Over"
	# 			logger.info(f"Current DeathLink Trigger: {trigger}")
	# 			return True
	# 	else:
	# 		logger.error("DeathLink amnesty cannot be accessed before connecting to the game and server")
	# 		return False

	# def _cmd_deathlink_amnesty(self, value = -1):
	# 	"""Get or Set the number of death before sending a DeathLink
	#     :param value: Set the amnesty to this value, must be between 0 and 10."""
	# 	if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
	# 		if value == -1:
	# 			logger.info(f"Current DeathLink amnesty: {self.ctx.death_link_amnesty}")
	# 			return True
	# 		else:
	# 			try:
	# 				value = int(value)
	# 				if value < 0 or value > 10:
	# 					raise ValueError
	# 				self.ctx.death_link_amnesty = value
	# 				logger.info(f"New DeathLink amnesty: {value}")
	# 				return True
	# 			except ValueError:
	# 				logger.error("Invalid argument, amnesty must be between 0 and 10")
	# 				return False
	# 	else:
	# 		logger.error("DeathLink amnesty cannot be accessed before connecting to the game and server")
	# 		return False

	def _cmd_ringlink(self, active = None):
		"""Toggle RingLink on or off
		:param active: If "on" or "true", enable RingLink. If "off" or "false", disable RingLink."""
		changed = False
		if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
			if active is not None:
				if active.lower() in ("on", "true"):
					if "RingLink" not in self.ctx.tags:
						self.ctx.tags.add("RingLink")
						self.ctx.ring_link_is_active = True
						changed = True
					logger.info("RingLink enabled")
				elif active.lower() in ("off", "false"):
					if "RingLink" in self.ctx.tags:
						self.ctx.tags.remove("RingLink")
						changed = True
						self.ctx.ring_link_is_active = False
					logger.info("RingLink disabled")
				else:
					logger.error("Invalid argument, use 'on' or 'off'")

				if changed:
					asyncio.create_task(self.ctx.send_msgs([{"cmd": "ConnectUpdate", "tags": self.ctx.tags}]))
			else:
				logger.info(f"RingLink is {'enabled' if self.ctx.ring_link_is_active else 'disabled'}")
		else:
			logger.error("RingLink cannot be changed before connecting to the game and server")

		return changed

	def _cmd_limits(self, lives = -1):
		"""Get or Set the max limits for lives
		:param lives: New max lives value, must be between 0 and 8."""
		if self.ctx.handler is not None and self.ctx.handler.gameController is not None:
			if lives == -1:
				logger.info(f"Current max lives: {self.ctx.handler.limitLives}")
				return True
			else:
				try:
					lives = int(lives)
					if lives < 0 or lives > 8:
						raise ValueError
					self.ctx.handler.setLivesLimit(lives)
					logger.info(f"New max lives: {lives}")
					return True
				except ValueError:
					logger.error("Invalid argument, limits must be between 0 and 8")
					return False
		else:
			logger.error("Limits cannot be accessed before connecting to the game and server")
			return False

class TouhouContext(CommonContext):
	"""Touhou Game Context"""
	def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
		super().__init__(server_address, password)
		self.game = DISPLAY_NAME
		self.items_handling = 0b111  # Item from starting inventory, own world and other world
		self.command_processor = TouhouClientProcessor
		self.reset()

	def reset(self):
		self.handler = None # gameHandler
		self.pending_death_link = False

		self.current_power_point = -1
		self.ring_link_id = None
		self.last_power_point = -1

		self.inError = False
		self.msgQueue = []

		# List of items/locations
		self.all_location_ids = None
		self.location_name_to_ap_id = None
		self.location_ap_id_to_name = None
		self.item_name_to_ap_id = None
		self.item_ap_id_to_name = None
		self.previous_location_checked = None
		self.location_mapping = None
		self.stage_specific_location_id = None

		self.is_connected = False
		self.last_death_link = 0
		self.last_ring_link = 0
		self.death_link_is_active = False
		self.ring_link_is_active = False
		self.death_link_amnesty = 0
		self.death_link_trigger = DEATH_LINK_LIFE

		self.victory_sent = False

		# Counter
		self.difficulties = 3
		self.traps = {"power_point_drain": 0, "reverse_control": 0, "aya_speed": 0, "freeze": 0, "life": 0, "power_point": 0}
		self.can_trap = True

		self.options = None
		self.check_multiple_difficulty = False
		self.ExtraMenu = False
		self.minimalCursor = 0

	def make_gui(self):
		ui = super().make_gui()
		ui.base_title = f"{DISPLAY_NAME} Client"
		return ui

	def run_gui(self) -> None:
		start_gui(self)

	async def server_auth(self, password_requested: bool = False):
		if password_requested and not self.password:
			await super().server_auth(password_requested)
		await self.get_username()
		await self.send_connect()

	def on_package(self, cmd: str, args: dict):
		"""
		Manage the package received from the server
		"""
		if cmd == "Connected":
			self.previous_location_checked = args['checked_locations']
			self.all_location_ids = set(args["missing_locations"] + args["checked_locations"])
			self.options = args["slot_data"] # Yaml Options
			self.is_connected = True
			self.check_multiple_difficulty = self.options['check_multiple_difficulty']
			self.location_mapping, self.stage_specific_location_id = getLocationMapping(self.options['shot_type'], self.options['difficulty_check'] == DIFFICULTY_CHECK)

			if self.handler is not None:
				self.handler.reset()

			asyncio.create_task(self.send_msgs([{"cmd": "GetDataPackage", "games": [DISPLAY_NAME]}]))

		if cmd == "ReceivedItems":
			asyncio.create_task(self.give_item(args["items"]))

		elif cmd == "DataPackage":
			if not self.all_location_ids:
				# Connected package not received yet, wait for datapackage request after connected package
				return
			self.location_name_to_ap_id = args["data"]["games"][DISPLAY_NAME]["location_name_to_id"]
			self.location_name_to_ap_id = {
				name: loc_id for name, loc_id in
				self.location_name_to_ap_id.items() if loc_id in self.all_location_ids
			}
			self.location_ap_id_to_name = {v: k for k, v in self.location_name_to_ap_id.items()}
			self.item_name_to_ap_id = args["data"]["games"][DISPLAY_NAME]["item_name_to_id"]
			self.item_ap_id_to_name = {v: k for k, v in self.item_name_to_ap_id.items()}
		elif cmd == "Bounced":
			tags = args.get("tags", [])
			# we can skip checking "DeathLink" in ctx.tags, as otherwise we wouldn't have been send this
			if "DeathLink" in tags and self.last_death_link != args["data"]["time"]:
				self.last_death_link = args["data"]["time"]
				self.on_deathlink(args["data"])
			elif "RingLink" in tags and self.ring_link_id != None:
				self.last_ring_link = args["data"]["time"]
				self.on_ringlink(args["data"])

	def client_recieved_initial_server_data(self):
		"""
		This method waits until the client finishes the initial conversation with the server.
		This means:
			- All LocationInfo packages recieved - requested only if patch files dont exist.
			- DataPackage package recieved (id_to_name maps and name_to_id maps are popualted)
			- Connection package recieved (slot number populated)
			- RoomInfo package recieved (seed name populated)
		"""
		return self.is_connected

	async def wait_for_initial_connection_info(self):
		"""
		This method waits until the client finishes the initial conversation with the server.
		See client_recieved_initial_server_data for wait requirements.
		"""
		if self.client_recieved_initial_server_data():
			return

		logger.info("Waiting for connect from server...")
		while not self.client_recieved_initial_server_data() and not self.exit_event.is_set():
			await asyncio.sleep(1)

	async def give_item(self, items):
		"""
		Give an item to the player. This method will always give the oldest
		item that the player has recieved from AP, but not in game yet.

		:NetworkItem item: The item to give to the player
		"""

		gotAnyItem = False

		# We wait for the link to be etablished to the game before giving any items
		while self.handler is None or self.handler.gameController is None:
			await asyncio.sleep(0.5)

		for item in items:
			item_id = item.item - STARTING_ID
			match item_id:
				case 0: # Life
					self.handler.addLife()
					gotAnyItem = True
				case 1: # Lower Difficulty
					self.difficulties -= 1
					self.handler.unlockDifficulty(self.difficulties)
					gotAnyItem = True
				case 2: # 25 Power Point
					self.handler.addPower(10)
					gotAnyItem = True
				case 100: # Reimu A
					self.handler.unlockCharacter(REIMU, SHOT_A)
					gotAnyItem = True
				case 101: # Reimu B
					self.handler.unlockCharacter(REIMU, SHOT_B)
					gotAnyItem = True
				case 102: # Reimu C
					self.handler.unlockCharacter(REIMU, SHOT_C)
					gotAnyItem = True
				case 103: # Marisa A
					self.handler.unlockCharacter(MARISA, SHOT_A)
					gotAnyItem = True
				case 104: # Marisa B
					self.handler.unlockCharacter(MARISA, SHOT_B)
					gotAnyItem = True
				case 105: # Marisa C
					self.handler.unlockCharacter(MARISA, SHOT_C)
					gotAnyItem = True
				case 200: # Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addProgressiveStage(isExtraStageLinear)
					gotAnyItem = True
				case 201: # [Reimu] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addProgressiveStage(isExtraStageLinear, REIMU)
					gotAnyItem = True
				case 202: # [Marisa] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addProgressiveStage(isExtraStageLinear, MARISA)
					gotAnyItem = True
				case 203: # [Reimu A] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addProgressiveStage(isExtraStageLinear, REIMU, SHOT_A)
					gotAnyItem = True
				case 204: # [Reimu B] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addProgressiveStage(isExtraStageLinear, REIMU, SHOT_B)
					gotAnyItem = True
				case 205: # [Reimu C] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addProgressiveStage(isExtraStageLinear, REIMU, SHOT_C)
					gotAnyItem = True
				case 206: # [Marisa A] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addProgressiveStage(isExtraStageLinear, MARISA, SHOT_A)
					gotAnyItem = True
				case 207: # [Marisa B] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addProgressiveStage(isExtraStageLinear, MARISA, SHOT_B)
					gotAnyItem = True
				case 208: # [Marisa C] Next Stage
					isExtraStageLinear = self.options['extra_stage'] == EXTRA_LINEAR
					self.handler.addProgressiveStage(isExtraStageLinear, MARISA, SHOT_C)
					gotAnyItem = True
				case 209: # Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart or (self.options['mode'] in PRACTICE_MODE and not self.options['progressive_stage']):
						self.handler.unlockExtraStage()
						gotAnyItem = True
				case 210: # [Reimu] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart or (self.options['mode'] in PRACTICE_MODE and not self.options['progressive_stage']):
						self.handler.unlockExtraStage(REIMU)
						gotAnyItem = True
				case 211: # [Marisa] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart or (self.options['mode'] in PRACTICE_MODE and not self.options['progressive_stage']):
						self.handler.unlockExtraStage(MARISA)
						gotAnyItem = True
				case 212: # [Reimu A] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart or (self.options['mode'] in PRACTICE_MODE and not self.options['progressive_stage']):
						self.handler.unlockExtraStage(REIMU, SHOT_A)
						gotAnyItem = True
				case 213: # [Reimu B] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart or (self.options['mode'] in PRACTICE_MODE and not self.options['progressive_stage']):
						self.handler.unlockExtraStage(REIMU, SHOT_B)
						gotAnyItem = True
				case 214: # [Reimu C] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart or (self.options['mode'] in PRACTICE_MODE and not self.options['progressive_stage']):
						self.handler.unlockExtraStage(REIMU, SHOT_C)
						gotAnyItem = True
				case 215: # [Marisa A] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart or (self.options['mode'] in PRACTICE_MODE and not self.options['progressive_stage']):
						self.handler.unlockExtraStage(MARISA, SHOT_A)
						gotAnyItem = True
				case 216: # [Marisa B] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart or (self.options['mode'] in PRACTICE_MODE and not self.options['progressive_stage']):
						self.handler.unlockExtraStage(MARISA, SHOT_B)
						gotAnyItem = True
				case 217: # [Marisa C] Extra Stage
					isExtraStageApart = self.options['extra_stage'] == EXTRA_APART
					if isExtraStageApart or (self.options['mode'] in PRACTICE_MODE and not self.options['progressive_stage']):
						self.handler.unlockExtraStage(MARISA, SHOT_C)
						gotAnyItem = True
				case 218: # Stage 2
					self.handler.addStage(1)
					gotAnyItem = True
				case 219: # Stage 3
					self.handler.addStage(2)
					gotAnyItem = True
				case 220: # Stage 4
					self.handler.addStage(3)
					gotAnyItem = True
				case 221: # Stage 5
					self.handler.addStage(4)
					gotAnyItem = True
				case 222: # Stage 6
					self.handler.addStage(5)
					gotAnyItem = True
				case 223: # [Reimu] Stage 2
					self.handler.addStage(1, REIMU)
					gotAnyItem = True
				case 224: # [Reimu] Stage 3
					self.handler.addStage(2, REIMU)
					gotAnyItem = True
				case 225: # [Reimu] Stage 4
					self.handler.addStage(3, REIMU)
					gotAnyItem = True
				case 226: # [Reimu] Stage 5
					self.handler.addStage(4, REIMU)
					gotAnyItem = True
				case 227: # [Reimu] Stage 6
					self.handler.addStage(5, REIMU)
					gotAnyItem = True
				case 228: # [Marisa] Stage 2
					self.handler.addStage(1, MARISA)
					gotAnyItem = True
				case 229: # [Marisa] Stage 3
					self.handler.addStage(2, MARISA)
					gotAnyItem = True
				case 230: # [Marisa] Stage 4
					self.handler.addStage(3, MARISA)
					gotAnyItem = True
				case 231: # [Marisa] Stage 5
					self.handler.addStage(4, MARISA)
					gotAnyItem = True
				case 232: # [Marisa] Stage 6
					self.handler.addStage(5, MARISA)
					gotAnyItem = True
				case 233: # [Reimu A] Stage 2
					self.handler.addStage(1, REIMU, SHOT_A)
					gotAnyItem = True
				case 234: # [Reimu A] Stage 3
					self.handler.addStage(2, REIMU, SHOT_A)
					gotAnyItem = True
				case 235: # [Reimu A] Stage 4
					self.handler.addStage(3, REIMU, SHOT_A)
					gotAnyItem = True
				case 236: # [Reimu A] Stage 5
					self.handler.addStage(4, REIMU, SHOT_A)
					gotAnyItem = True
				case 237: # [Reimu A] Stage 6
					self.handler.addStage(5, REIMU, SHOT_A)
					gotAnyItem = True
				case 238: # [Reimu B] Stage 2
					self.handler.addStage(1, REIMU, SHOT_B)
					gotAnyItem = True
				case 239: # [Reimu B] Stage 3
					self.handler.addStage(2, REIMU, SHOT_B)
					gotAnyItem = True
				case 240: # [Reimu B] Stage 4
					self.handler.addStage(3, REIMU, SHOT_B)
					gotAnyItem = True
				case 241: # [Reimu B] Stage 5
					self.handler.addStage(4, REIMU, SHOT_B)
					gotAnyItem = True
				case 242: # [Reimu B] Stage 6
					self.handler.addStage(5, REIMU, SHOT_B)
					gotAnyItem = True
				case 243: # [Reimu C] Stage 2
					self.handler.addStage(1, REIMU, SHOT_C)
					gotAnyItem = True
				case 244: # [Reimu C] Stage 3
					self.handler.addStage(2, REIMU, SHOT_C)
					gotAnyItem = True
				case 245: # [Reimu C] Stage 4
					self.handler.addStage(3, REIMU, SHOT_C)
					gotAnyItem = True
				case 246: # [Reimu C] Stage 5
					self.handler.addStage(4, REIMU, SHOT_C)
					gotAnyItem = True
				case 247: # [Reimu C] Stage 6
					self.handler.addStage(5, REIMU, SHOT_C)
					gotAnyItem = True
				case 248: # [Marisa A] Stage 2
					self.handler.addStage(1, MARISA, SHOT_A)
					gotAnyItem = True
				case 249: # [Marisa A] Stage 3
					self.handler.addStage(2, MARISA, SHOT_A)
					gotAnyItem = True
				case 250: # [Marisa A] Stage 4
					self.handler.addStage(3, MARISA, SHOT_A)
					gotAnyItem = True
				case 251: # [Marisa A] Stage 5
					self.handler.addStage(4, MARISA, SHOT_A)
					gotAnyItem = True
				case 252: # [Marisa A] Stage 6
					self.handler.addStage(5, MARISA, SHOT_A)
					gotAnyItem = True
				case 253: # [Marisa B] Stage 2
					self.handler.addStage(1, MARISA, SHOT_B)
					gotAnyItem = True
				case 254: # [Marisa B] Stage 3
					self.handler.addStage(2, MARISA, SHOT_B)
					gotAnyItem = True
				case 255: # [Marisa B] Stage 4
					self.handler.addStage(3, MARISA, SHOT_B)
					gotAnyItem = True
				case 256: # [Marisa B] Stage 5
					self.handler.addStage(4, MARISA, SHOT_B)
					gotAnyItem = True
				case 257: # [Marisa B] Stage 6
					self.handler.addStage(5, MARISA, SHOT_B)
					gotAnyItem = True
				case 258: # [Marisa C] Stage 2
					self.handler.addStage(1, MARISA, SHOT_C)
					gotAnyItem = True
				case 259: # [Marisa C] Stage 3
					self.handler.addStage(2, MARISA, SHOT_C)
					gotAnyItem = True
				case 260: # [Marisa C] Stage 4
					self.handler.addStage(3, MARISA, SHOT_C)
					gotAnyItem = True
				case 261: # [Marisa C] Stage 5
					self.handler.addStage(4, MARISA, SHOT_C)
					gotAnyItem = True
				case 262: # [Marisa C] Stage 6
					self.handler.addStage(5, MARISA, SHOT_C)
					gotAnyItem = True
				case 300 | 301: # Ending - Kanako
					values = {300: REIMU, 301: MARISA}
					character = values[item_id]
					self.handler.addEnding(character, ENDING_NORMAL)
					if self.checkVictory():
						await self.send_msgs([{"cmd": 'StatusUpdate', "status": 30}])
					gotAnyItem = True
				case 308 | 309: # Ending - Suwako
					values = {308: REIMU, 309: MARISA}
					character = values[item_id]
					self.handler.addEnding(character, ENDING_EXTRA)
					if self.checkVictory():
						await self.send_msgs([{"cmd": 'StatusUpdate', "status": 30}])
					gotAnyItem = True
				case 400: # 1 Power Point
					self.handler.addPower(1)
					gotAnyItem = True
				case 500: # -50% Power Point
					self.traps["power_point"] += 1
				case 501: # -1 Life
					self.traps["life"] += 1
				case 502: # Reverse Movement
					self.traps["reverse_control"] = 1
				case 503: # Aya Speed
					self.traps["aya_speed"] = 1
				case 504: # Freeze
					self.traps["freeze"] += 1
				case 505: # Power Point Drain
					self.traps["power_point_drain"] = 1
				case _:
					logger.error(f"Unknown Item: {item}")

		if gotAnyItem:
			self.handler.playSound(0x1F)

		# Update the stage list
		self.handler.updateStageList()

	async def update_locations_checked(self):
		"""
		Check if any locations has been checked since last called, if a location has ben checked, we send a message and update our list of checked location
		"""
		new_locations = []

		for id, map in self.location_mapping.items():
			# Check if the boss is beaten and the location is not already checked
			if self.handler.isBossBeaten(*map) and id not in self.previous_location_checked:
				# We add it to the list of checked locations
				new_locations.append(id)

				if self.options['mode'] in NORMAL_MODE:
					# If we are in normal mode, the extra stage is set to linear and the stage 6 has just been cleared. We unlock it if it's not already.
					if self.options['extra_stage'] == EXTRA_LINEAR:
						if not self.handler.canExtra() and id in self.stage_specific_location_id["stage_6"]:
							self.handler.unlockExtraStage()

		# If we have new locations, we send them to the server and add them to the list of checked locations
		if new_locations:
			self.previous_location_checked = self.previous_location_checked + new_locations
			await self.send_msgs([{"cmd": 'LocationChecks', "locations": new_locations}])

	def on_deathlink(self, data):
		"""
		Method that is called when a death link is recieved.
		"""
		self.pending_death_link = True
		return super().on_deathlink(data)

	def on_ringlink(self, data):
		"""
		Method that is called when a ring link is recieved.
		"""
		game_mode = self.handler.getGameMode()
		# If we failed to get the game mode, we cancel the ring link
		if game_mode == -2:
			return

		# We check if we are in a state where we can receive a ring link
		if self.handler.gameController and game_mode == IN_GAME and not self.inError:
			# We check if it was not sent by us
			if data["source"] != self.ring_link_id:
				self.handler.playSound(0x15) if data["amount"] < 5 else self.handler.playSound(0x1F)
				self.handler.giveCurrentPowerPoint(data["amount"])
				self.last_power_point = self.handler.getCurrentPowerPoint()

	async def send_death_link(self):
		"""
		Send a death link to the server if it's active.
		"""
		if self.death_link_is_active:
			await self.send_death()

	def giveResources(self):
		"""
		Give the resources to the player
		"""
		isNormalMode = self.options['mode'] in NORMAL_MODE
		return self.handler.initResources(isNormalMode)

	def updateStageList(self):
		"""
		Update the stage list in practice mode
		"""
		mode = self.options['mode']

		if mode in PRACTICE_MODE or mode in NORMAL_MODE:
			self.handler.updateStageList(mode in PRACTICE_MODE)

		if mode in PRACTICE_MODE:
			self.handler.updatePracticeScore(self.location_mapping, self.previous_location_checked)

	def setRingLinkTag(self, active):
		if active:
			self.tags.add("RingLink")
			self.ring_link_is_active = True
		else:
			self.tags.remove("RingLink")
			self.ring_link_is_active = False
		asyncio.create_task(self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}]))

	def checkVictory(self):
		"""
		Check if the player has won the game.
		"""
		goal = self.options['goal']
		type = self.options['ending_required']
		extra = self.options['extra_stage']
		characters = CHARACTERS

		normal_a_victory = True
		normal_b_victory = True
		extra_victory = True

		if (goal == ENDING_NORMAL or goal == ENDING_ALL):
			if type == ONE_ENDING:
				normal_a_victory = False
				for character in characters:
					normal_a_victory = normal_a_victory or self.handler.endings[character][ENDING_NORMAL]
			elif type == ALL_CHARACTER_ENDING:
				for character in characters:
					normal_a_victory = normal_a_victory and self.handler.endings[character][ENDING_NORMAL]

		if (goal == ENDING_EXTRA or goal == ENDING_ALL) and extra != NO_EXTRA:
			if type == ONE_ENDING:
				extra_victory = False
				for character in characters:
					extra_victory = extra_victory or self.handler.endings[character][ENDING_EXTRA]
			elif type == ALL_CHARACTER_ENDING:
				for character in characters:
					extra_victory = extra_victory and self.handler.endings[character][ENDING_EXTRA]

		return normal_a_victory and normal_b_victory and extra_victory

	async def main_loop(self):
		"""
		Main loop that handles giving resources and updating locations.
		"""
		try:
			bossPresent = False
			currentMode = -1 # -1: No mode, 0: In Game, 1: In Menu
			currentLives = 0
			bossCounter = -1
			resourcesGiven = False
			noCheck = True #We start by disabling the checks since we don't know where the player would be when connecting the client
			currentScore = 0
			currentStage = 0

			while not self.exit_event.is_set() and self.handler and not self.inError:
				await asyncio.sleep(0.5)
				gameMode = self.handler.getGameMode()
				# If we failed to get the game mode, we skip the loop
				if gameMode == -2:
					continue

				# Mode Check
				if(gameMode == IN_GAME and not noCheck):
					# A level has started
					if(currentMode != 0):
						currentMode = 0
						bossCounter = -1
						bossPresent = False
						currentScore = 0
						currentStage = self.handler.getCurrentStage()

						# If the current situation is technically not possible, we lock checks
						if(not self.handler.checkIfCurrentIsPossible((self.options['mode'] in NORMAL_MODE))):
							noCheck = False

					if(not resourcesGiven):
						await asyncio.sleep(0.5)
						resourcesGiven = True
						currentLives = self.handler.getCurrentLives()

					# We check if the current score is the same or higher than the previous one
					if(currentScore <= self.handler.getCurrentScore()):
						currentScore = self.handler.getCurrentScore()
					else:
						# If the score is lower, it mean the stage has been restarted, we end the loop and act like we just enter the stage
						currentMode = -1
						resourcesGiven = False
						continue
 
					# Boss Check
					nbBoss = 2 if self.handler.getCurrentStage() != 6 else 1
					if(not bossPresent):
						if(self.handler.isBossPresent(bossCounter+1) and bossCounter < nbBoss-1):
							bossPresent = True
							bossCounter += 1
					else:
						if bossPresent:
							# If the boss is defeated, we update the locations
							if(not self.handler.isBossPresent(bossCounter)):
								if(not self.handler.isCurrentBossDefeated(bossCounter)):
									self.handler.setCurrentStageBossBeaten(bossCounter, self.check_multiple_difficulty)
									await self.update_locations_checked()
								#If the stage is ending, we disable traps and reset the counter
								if bossCounter == nbBoss-1:
									self.can_trap = False
									bossCounter = -1
								bossPresent = False

					# If we're in practice mode and a boss spawn while there is no more boss in the stage, it's not normal and we stop sending checks
					if (self.options['mode'] in PRACTICE_MODE and bossCounter > nbBoss):
						noCheck = True

					# If the stage has changed and we're in normal mode, we reset some values
					if currentStage != self.handler.getCurrentStage() and self.options['mode'] in NORMAL_MODE:
						currentStage = self.handler.getCurrentStage()
						self.can_trap = True
						bossCounter = -1

					# Death Check
					if(currentLives != self.handler.getCurrentLives()):
						currentLives = self.handler.getCurrentLives()
				elif(gameMode != IN_GAME):
					# We enter in the menu
					if(currentMode != 1):
						currentMode = 1
						resourcesGiven = False
						noCheck = False # We enable the checks once we're in the menu
		except Exception as e:
			logger.error(f"Main ERROR:")
			logger.error(traceback.format_exc())
			self.inError = True

	async def menu_loop(self):
		"""
		Loop that handles the characters lock and difficulty lock, depending on the menu.
		Also handle starting item from options
		"""
		try:
			mode = self.options['mode']
			exclude_lunatic = self.options['exclude_lunatic']

			if exclude_lunatic:
				self.difficulties -= 1
				self.handler.unlockDifficulty(self.difficulties)

			while not self.exit_event.is_set() and self.handler and not self.inError:
				await asyncio.sleep(0.1)
				game_mode = self.handler.getGameMode()
				# If we failed to get the game mode, we skip the loop
				if game_mode == -2:
					continue

				if game_mode != IN_GAME:
					menu = self.handler.getMenu()
					if menu == -1:
						await asyncio.sleep(0.5)
						continue

					# We check where we are in the menu in order to determine how we lock/unlock the characters
					if (menu == MAIN_MENU or self.handler.isInExtraMode()) or self.handler.getDifficulty() == EXTRA:
						self.ExtraMenu = True
					elif (menu != MAIN_MENU) or self.handler.getDifficulty() < EXTRA:
						self.ExtraMenu = False

					# If we're in the difficulty menu, we put the minimal value to the lowest difficulty
					if menu in [DIFFICULTY_MENU]:
						self.minimalCursor = -1
					# If we're in the main menu and we play in practice mode, we lock the access to normal mode
					elif menu == MAIN_MENU and mode not in NORMAL_MODE:
						# 1 If we have access to the extra stage, 2 if we don't
						self.minimalCursor = 1 if self.handler.canExtra() else 2
					else:
						self.minimalCursor = 0

					try:
						self.updateStageList()
						self.handler.updateExtraUnlock(not self.ExtraMenu)
						self.handler.updateCursor(self.minimalCursor)
					except Exception as e:
						pass
		except Exception as e:
			logger.error(f"Menu ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def trap_loop(self):
		"""
		Loop that handles traps.
		"""

		try:
			PowerPointDrain = False
			ReverseControls = False
			AyaSpeed = False
			Freeze = False
			InLevel = False
			TransitionTimer = 2
			counterTransition = 0
			freezeTimer = 2
			counterFreeze = 0
			currentScore = 0
			restarted = False
			while not self.exit_event.is_set() and self.handler and not self.inError:
				await asyncio.sleep(1)
				game_mode = self.handler.getGameMode()
				# If we failed to get the game mode, we skip the loop
				if game_mode == -2:
					continue

				if game_mode == IN_GAME and not restarted:
					# If we enter a level and some time has passed, we activate the traps
					if not InLevel and counterTransition < TransitionTimer:
						counterTransition += 1
					elif not InLevel:
						currentScore = 0
						InLevel = True
						counterTransition = 0

					# We check if the score is correct in order to know if the stage has been restarted
					if(currentScore <= self.handler.getCurrentScore()):
						currentScore = self.handler.getCurrentScore()
					else:
						restarted = True
						continue

					if InLevel and self.can_trap:
						# Checks if we need to add a new trap
						if not PowerPointDrain and self.traps['power_point_drain'] > 0:
							PowerPointDrain = True
							self.traps['power_point_drain'] -= 1
							self.handler.playSound(0x1F)
						elif not ReverseControls and self.traps['reverse_control'] > 0:
							ReverseControls = True
							self.traps['reverse_control'] -= 1
							self.handler.playSound(0x0D)
							self.handler.reverseControls()
						elif not AyaSpeed and self.traps['aya_speed'] > 0:
							AyaSpeed = True
							self.traps['aya_speed'] -= 1
							self.handler.playSound(0x0D)
							self.handler.ayaSpeed()
						elif not Freeze and self.traps['freeze'] > 0:
							Freeze = True
							self.traps['freeze'] -= 1
							self.handler.playSound(0x0D)
							self.handler.freeze()
						elif self.traps['life'] > 0:
							self.traps['life'] -= 1
							self.handler.playSound(0x04)
							self.handler.loseLife()
						elif self.traps['power_point'] > 0:
							self.traps['power_point'] -= 1
							self.handler.playSound(0x1F)
							self.handler.halfPowerPoint()

						# Power Point Drain apply each loop until the player dies or the level is exited
						if PowerPointDrain:
							self.handler.powerPointDrain()

						# Freeze apply each loop until the timer is done
						if Freeze:
							if counterFreeze < freezeTimer:
								counterFreeze += 1
							else:
								Freeze = False
								counterFreeze = 0
								self.handler.resetSpeed()
				else:
					InLevel = False
					PowerPointDrain = False
					ReverseControls = False
					AyaSpeed = False
					Freeze = False
					counterTransition = 0
					counterFreeze = 0
					self.can_trap = True
					restarted = False
					currentScore = 0
		except Exception as e:
			logger.error(f"Trap ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def death_link_loop(self):
		"""
		Loop that handles death link.
		"""
		try:
			self.pending_death_link = False
			onGoingDeathLink = False
			inLevel = False
			currentMisses = 0
			currentLives = 0
			nb_death = 0

			while not self.exit_event.is_set() and self.handler and not self.inError:
				if(self.death_link_is_active):
					await asyncio.sleep(0.5)
				else:
					await asyncio.sleep(2)
					inLevel = False
					continue
				game_mode = self.handler.getGameMode()
				# If we failed to retrieve the game mode, we skip the loop
				if game_mode == -2:
					continue

				if game_mode == IN_GAME:
					# If we enter a level, we set the variables
					if not inLevel:
						inLevel = True
						currentMisses = self.handler.getMisses()
						currentLives = self.handler.getCurrentLives()
						onGoingDeathLink = False
						self.pending_death_link = False

					# If a death link is sent, we set the flag
					if self.pending_death_link and not onGoingDeathLink:
						onGoingDeathLink = True

					# If a misses has been added, that mean the player has been killed and we check if it was because of the death link
					# (Receiving a death link is checked by misses as it's more reliable and the player could have deathbomb the death link)
					if currentMisses < self.handler.getMisses():
						# If the player is killed by a death link, we tell the loop it's done
						if onGoingDeathLink:
							onGoingDeathLink = False
							self.pending_death_link = False
						else:
							if self.death_link_trigger == DEATH_LINK_LIFE or (self.death_link_trigger == DEATH_LINK_GAME_OVER and currentLives == 0):
								nb_death += 1
								if nb_death >= self.death_link_amnesty:
									await self.send_death_link()
									nb_death = 0
								else:
									logger.info(f"DeathLink: {nb_death}/{self.death_link_amnesty}")

						currentMisses += 1
						await asyncio.sleep(1)  # We wait a little
					# If no death has occured but a death link is pending, we try to kill the player
					elif self.pending_death_link:
						await self.handler.killPlayer()

					# If the number of lives changed, we update it.
					if currentLives != self.handler.getCurrentLives():
						currentLives = self.handler.getCurrentLives()
				else:
					inLevel = False
		except Exception as e:
			logger.error(f"DeathLink ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def message_loop(self):
		"""
		Loop that handles displaying message
		"""
		try:
			while not self.exit_event.is_set() and self.handler and not self.inError:
				if self.msgQueue != []:
					msg = self.msgQueue[0]
					self.msgQueue.pop(0)
					task = asyncio.create_task(self.handler.displayMessage(msg['msg'], msg['color']))
					await asyncio.wait([task])
				else:
					await asyncio.sleep(0.1)
		except Exception as e:
			logger.error(f"Message ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def ring_link_loop(self):
		"""
		Loop that handles Ring Link
		"""
		try:
			self.last_power_point = -1
			self.ring_link_id = random.randint(0, 999999)
			self.timer = 0.5

			while not self.exit_event.is_set() and self.handler and not self.inError:
				if(self.ring_link_is_active):
					await asyncio.sleep(self.timer)
				else:
					await asyncio.sleep(2)
					self.last_power_point = -1
					continue
				game_mode = self.handler.getGameMode()
				# If we failed to retrieve the game mode, we skip the loop
				if game_mode == -2:
					continue

				if game_mode == IN_GAME:
					# We wait a little before sending ring link
					self.timer = 0.1
					curent_power = self.handler.getCurrentPowerPoint()

					# If last_power_point is -1, that mean it's the first loop, so we just wait a little and then set it
					if self.last_power_point == -1:
						await asyncio.sleep(1)
						self.last_power_point = curent_power
						continue

					# If the power point has changed, we send a ring link
					if self.last_power_point != curent_power:
						diff_power = curent_power-self.last_power_point
						self.last_power_point = curent_power
						asyncio.create_task(self.send_msgs([{"cmd": "Bounce", "tags": ["RingLink"], "data": {"amount": diff_power, "source": self.ring_link_id, "time": time.time()}}]))
				else:
					self.last_power_point = -1
					self.timer = 0.5
		except Exception as e:
			logger.error(f"RingLink ERROR: {e}")
			logger.error(traceback.format_exc())
			self.inError = True

	async def connect_to_game(self):
		"""
		Connect the client to the game process
		"""
		self.handler = None

		while not self.handler:
			try:
				self.handler = gameHandler()
			except Exception as e:
				await asyncio.sleep(2)

	async def reconnect_to_game(self):
		"""
		Reconnect to client to the game process without resetting everything
		"""

		while not self.handler.gameController:
			try:
				self.handler.reconnect()
			except Exception as e:
				await asyncio.sleep(2)

class APQuestControlsView(BoxLayout):
    border_on = False

class TouhouManager(GameManager):
	ctx: TouhouContext

	def __init__(self, ctx: TouhouContext) -> None:
		super().__init__(ctx)
		self.base_title = f"{DISPLAY_NAME} Client | AP version:"

	def build(self):
		container = super().build()

		return container

async def game_watcher(ctx: TouhouContext):
	"""
	Client loop, watching the game process.
	Start the different loops once connected that will handle the game.
	It will also attempt to reconnect if the connection to the game is lost.

	:TouhouContext ctx: The client context instance.
	"""

	await ctx.wait_for_initial_connection_info()

	while not ctx.exit_event.is_set():
		# client disconnected from server
		if not ctx.server:
			# We reset the context
			ctx.reset()
			await ctx.wait_for_initial_connection_info()

		# First connection
		if ctx.handler is None and not ctx.inError:
			logger.info(f"Waiting for connection to {SHORT_NAME}...")
			asyncio.create_task(ctx.connect_to_game())
			while(ctx.handler is None and not ctx.exit_event.is_set()):
				await asyncio.sleep(1)

		# Connection following an error
		if ctx.inError:
			logger.info(f"Connection lost. Waiting for connection to {SHORT_NAME}...")
			ctx.handler.gameController = None

			asyncio.create_task(ctx.reconnect_to_game())
			await asyncio.sleep(1)
			while(ctx.handler.gameController is None and not ctx.exit_event.is_set()):
				await asyncio.sleep(1)

		if ctx.handler and ctx.handler.gameController:
			ctx.inError = False
			logger.info(f"{SHORT_NAME} process found. Starting loop...")

			# We start all the diffrent loops
			loops = []
			loops.append(asyncio.create_task(ctx.main_loop()))
			loops.append(asyncio.create_task(ctx.menu_loop()))
			loops.append(asyncio.create_task(ctx.trap_loop()))
			# loops.append(asyncio.create_task(ctx.death_link_loop()))
			loops.append(asyncio.create_task(ctx.ring_link_loop()))

			# We update the locations checked if there was any location that was already checked before the connection
			await ctx.update_locations_checked()
			ctx.updateStageList()

			# Activating Death Link / Ring Link if needed
			# if ctx.options['death_link']:
			# 	await ctx.update_death_link(True)
			# 	ctx.death_link_is_active = True

			# if ctx.options['death_link_amnesty']:
			# 	ctx.death_link_amnesty = ctx.options['death_link_amnesty']

			# if ctx.options['death_link_trigger']:
			# 	ctx.death_link_trigger = ctx.options['death_link_trigger']

			if ctx.options['ring_link']:
				ctx.setRingLinkTag(True)

			# We set the limits for lives
			ctx.handler.setLivesLimit(ctx.options['limit_lives'])

			# Infinite loop while there is no error. If there is an error, we exit this loop in order to restart the connection
			while not ctx.exit_event.is_set() and ctx.server and not ctx.inError:
				await asyncio.sleep(1)

			# If we're here, we stop all the loops
			for loop in loops:
				try:
					loop.cancel()
				except:
					pass

def start_gui(context: TouhouContext):
    context.ui = TouhouManager(context)
    context.ui_task = asyncio.create_task(context.ui.async_run(), name="UI")

def launch():
	"""
	Launch a client instance (wrapper / args parser)
	"""
	async def main(args):
		"""
		Launch a client instance (threaded)
		"""
		ctx = TouhouContext(args.connect, args.password)
		ctx.server_task = asyncio.create_task(server_loop(ctx))
		if gui_enabled:
			ctx.run_gui()
		ctx.run_cli()
		watcher = asyncio.create_task(
			game_watcher(ctx),
			name="GameProgressionWatcher"
		)
		await ctx.exit_event.wait()
		await watcher
		await ctx.shutdown()

	parser = get_base_parser(description=SHORT_NAME+" Client")
	args, _ = parser.parse_known_args()

	colorama.init()
	asyncio.run(main(args))
	colorama.deinit()