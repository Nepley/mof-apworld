from typing import List
from .Variables import *

from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import TItem, get_items_by_category, item_table, item_groups
from .Locations import location_table
from .Options import Th10Options
from .Regions import create_regions
from .Rules import set_rules
import re

def launch_client():
	"""Launch a client instance"""
	from worlds.th10.Client import launch
	launch_subprocess(launch, name="GameClient")

components.append(Component(
	SHORT_NAME+" Client",
	"GameClient",
	func=launch_client,
	component_type=Type.CLIENT
))

class TWorld(World):
	game = DISPLAY_NAME
	options: Th10Options
	options_dataclass = Th10Options

	item_name_groups = item_groups
	item_name_to_id = {name: data.code for name, data in item_table.items()}
	location_name_to_id = {name: id for name, id in location_table.items()}

	def fill_slot_data(self) -> dict:
		# Failsafe if the ending required is set to all shot type and the shot type are not their own checks.
		ending_required = self.options.ending_required.value
		if not self.options.shot_type.value and self.options.ending_required.value == ALL_SHOT_TYPE_ENDING:
			ending_required = ALL_CHARACTER_ENDING

		data = {
			"mode": self.options.mode.value,
			"stage_unlock": self.options.stage_unlock.value,
			"exclude_lunatic": self.options.exclude_lunatic.value,
			"number_life_mid": self.options.number_life_mid.value,
			"difficulty_mid": self.options.difficulty_mid.value,
			"number_life_end": self.options.number_life_end.value,
			"difficulty_end": self.options.difficulty_end.value,
			"extra_stage": self.options.extra_stage.value,
			"number_life_extra": self.options.number_life_extra.value,
			"shot_type": self.options.shot_type.value,
			"difficulty_check": self.options.difficulty_check.value,
			"check_multiple_difficulty": self.options.check_multiple_difficulty.value,
			"goal": self.options.goal.value,
			"ending_required": ending_required,
			"death_link": self.options.death_link.value,
			"death_link_trigger": self.options.death_link_trigger.value,
			"death_link_amnesty": self.options.death_link_amnesty.value,
			"ring_link": self.options.ring_link.value,
			"limit_lives": self.options.limit_lives.value,
		}

		return data

	def create_items(self):
		item_pool: List[TItem] = []
		character_list = []
		progressive_stage_list = []
		stages = []
		extra_stages = []
		total_locations = len(self.multiworld.get_unfilled_locations(self.player))
		number_placed_item = 0
		mode = getattr(self.options, "mode")
		stage_unlock = getattr(self.options, "stage_unlock")
		progressive_stage = getattr(self.options, "progressive_stage")
		exclude_lunatic = getattr(self.options, "exclude_lunatic")
		extra = getattr(self.options, "extra_stage")
		goal = getattr(self.options, "goal")
		shot_type = getattr(self.options, "shot_type")
		difficulty_check = getattr(self.options, "difficulty_check")
		traps = getattr(self.options, "traps")
		power_point_trap = getattr(self.options, "power_point_trap")
		life_trap = getattr(self.options, "life_trap")
		reverse_movement_trap = getattr(self.options, "reverse_movement_trap")
		aya_speed_trap = getattr(self.options, "aya_speed_trap")
		freeze_trap = getattr(self.options, "freeze_trap")

		for name, data in item_table.items():
			quantity = data.max_quantity

			# Categories to be ignored, they will be added in a later stage if necessary.
			if data.category == "Filler":
				continue

			# Will be added later
			if data.category == "Traps":
				continue

			# Will be added manually later
			if data.category == "Endings":
				continue

			# Will be added later
			if data.category in ["[Progressive][Global] Stages", "[Progressive][Character] Stages", "[Progressive][Shot Type] Stages"]:
				progressive_stage_list.append({"name": name, "data": data})
				continue

			# Will be added later
			if data.category in ["[Not Progressive][Global] Stages", "[Not Progressive][Character] Stages", "[Not Progressive][Shot Type] Stages"]:
				stages.append({"name": name, "data": data})
				continue

			# Will be added later
			if data.category == "Characters":
				character_list.append(name)
				continue

			# Will be added later
			if data.category in ["[Global] Extra Stage", "[Character] Extra Stage", "[Shot Type] Extra Stage"]:
				extra_stages.append({"name": name, "data": data})
				continue

			# If Lunatic is excluded, we remove one Lower difficulty
			if data.category == "Items" and name == "Lower Difficulty" and exclude_lunatic:
				quantity -= 1

			item_pool += [self.create_item(name) for _ in range(0, quantity)]

		# Selecting starting character
		chosen = self.random.choice(character_list)
		self.multiworld.push_precollected(self.create_item(chosen))
		character_list.remove(chosen)
		for character in character_list:
			item_pool += [self.create_item(character) for _ in range(0, 1)]

		# Stages
		if mode in PRACTICE_MODE:
			# If we have stage by shot type but we don't any option adding location, we change it to stage by character
			if stage_unlock == STAGE_BY_SHOT_TYPE and not shot_type and not difficulty_check:
				stage_unlock = STAGE_BY_CHARACTER

			if progressive_stage:
				for stage in progressive_stage_list:
					quantity = stage['data'].max_quantity
					# If there is no extra stage or it's separated, we remove one stage
					if extra != EXTRA_LINEAR:
						quantity -= 1

					if stage_unlock == STAGE_GLOBAL and stage['data'].category == "[Progressive][Global] Stages":
						item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

					if stage_unlock == STAGE_BY_CHARACTER and stage['data'].category == "[Progressive][Character] Stages":
						item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

					if stage_unlock == STAGE_BY_SHOT_TYPE and stage['data'].category == "[Progressive][Shot Type] Stages":
						item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]
			else:
				for stage in stages:
					quantity = stage['data'].max_quantity

					if stage_unlock == STAGE_GLOBAL and stage['data'].category == "[Not Progressive][Global] Stages":
						item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

					if stage_unlock == STAGE_BY_CHARACTER and stage['data'].category == "[Not Progressive][Character] Stages":
						item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

					if stage_unlock == STAGE_BY_SHOT_TYPE and stage['data'].category == "[Not Progressive][Shot Type] Stages":
						item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

				# If Extra is enabled linearly, we change it to apart
				if extra == EXTRA_LINEAR:
					extra = EXTRA_APART

		# Extra
		if extra == EXTRA_APART and (mode in PRACTICE_MODE or mode in NORMAL_MODE):
			# If we have stage by shot type but we don't any option adding location, we change it to stage by character
			if stage_unlock == STAGE_BY_SHOT_TYPE and not shot_type and not difficulty_check:
				stage_unlock = STAGE_BY_CHARACTER

			for stage in extra_stages:
				quantity = stage['data'].max_quantity

				if stage_unlock == STAGE_GLOBAL and stage['data'].category == "[Global] Extra Stage":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

				if stage_unlock == STAGE_BY_CHARACTER and stage['data'].category == "[Character] Extra Stage":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

				if stage_unlock == STAGE_BY_SHOT_TYPE and stage['data'].category == "[Shot Type] Extra Stage":
					item_pool += [self.create_item(stage['name']) for _ in range(0, quantity)]

		# Endings
		# If we have the extra stage and the extra boss is a potential goal
		if extra and goal in [ENDING_EXTRA, ENDING_ALL]:
			if shot_type:
				self.multiworld.get_location("[Reimu A] Stage Extra Clear", self.player).place_locked_item(self.create_item("[Reimu] Ending - Suwako"))
				self.multiworld.get_location("[Reimu B] Stage Extra Clear", self.player).place_locked_item(self.create_item("[Reimu] Ending - Suwako"))
				self.multiworld.get_location("[Reimu C] Stage Extra Clear", self.player).place_locked_item(self.create_item("[Reimu] Ending - Suwako"))
				self.multiworld.get_location("[Marisa A] Stage Extra Clear", self.player).place_locked_item(self.create_item("[Marisa] Ending - Suwako"))
				self.multiworld.get_location("[Marisa B] Stage Extra Clear", self.player).place_locked_item(self.create_item("[Marisa] Ending - Suwako"))
				self.multiworld.get_location("[Marisa C] Stage Extra Clear", self.player).place_locked_item(self.create_item("[Marisa] Ending - Suwako"))
				number_placed_item += 6
			else:
				self.multiworld.get_location("[Reimu] Stage Extra Clear", self.player).place_locked_item(self.create_item("[Reimu] Ending - Suwako"))
				self.multiworld.get_location("[Marisa] Stage Extra Clear", self.player).place_locked_item(self.create_item("[Marisa] Ending - Suwako"))
				number_placed_item += 2

		# If the final boss is a potential goal
		if not extra or goal in [ENDING_NORMAL, ENDING_ALL]:
			if shot_type:
				self.multiworld.get_location("[Reimu A] Stage 6 Clear", self.player).place_locked_item(self.create_item("[Reimu] Ending - Kanako"))
				self.multiworld.get_location("[Reimu B] Stage 6 Clear", self.player).place_locked_item(self.create_item("[Reimu] Ending - Kanako"))
				self.multiworld.get_location("[Reimu C] Stage 6 Clear", self.player).place_locked_item(self.create_item("[Reimu] Ending - Kanako"))
				self.multiworld.get_location("[Marisa A] Stage 6 Clear", self.player).place_locked_item(self.create_item("[Marisa] Ending - Kanako"))
				self.multiworld.get_location("[Marisa B] Stage 6 Clear", self.player).place_locked_item(self.create_item("[Marisa] Ending - Kanako"))
				self.multiworld.get_location("[Marisa C] Stage 6 Clear", self.player).place_locked_item(self.create_item("[Marisa] Ending - Kanako"))
				number_placed_item += 6
			else:
				self.multiworld.get_location("[Reimu] Stage 6 Clear", self.player).place_locked_item(self.create_item("[Reimu] Ending - Kanako"))
				self.multiworld.get_location("[Marisa] Stage 6 Clear", self.player).place_locked_item(self.create_item("[Marisa] Ending - Kanako"))
				number_placed_item += 2

		if traps > 0:
			remaining_locations = total_locations - (len(item_pool) + number_placed_item)

			# If we have traps, we count how many of them we need to add
			number_traps = int(remaining_locations * traps / 100)

			if number_traps > 0:
				trapList = self.random.choices(["-50% Power Point", "-1 Life", "Reverse Movement", "Aya Speed", "Freeze"], weights=[power_point_trap, life_trap, reverse_movement_trap, aya_speed_trap, freeze_trap], k=number_traps)
				for trap in trapList:
					item_pool.append(self.create_item(trap))

		# Fill any empty locations with filler items.
		while len(item_pool) + number_placed_item < total_locations:
			item_pool.append(self.create_item(self.get_filler_item_name()))

		self.multiworld.itempool += item_pool

	def get_filler_item_name(self) -> str:
		fillers = get_items_by_category("Filler")
		weights = [data.weight for data in fillers.values()]
		return self.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

	def create_item(self, name: str, classification = "") -> TItem:
		data = item_table[name]
		classification = data.classification if classification == "" else classification
		return TItem(name, classification, data.code, self.player)

	def set_rules(self):
		set_rules(self.multiworld, self.player)

	def create_regions(self):
		create_regions(self.multiworld, self.player, self.options)