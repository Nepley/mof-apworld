from .Variables import *
from .Locations import location_table

def getLocationMapping(shot_type, difficulty):
	mapping = {}
	stage_specific_location_id = {"stage_6": [], "extra": []}

	for location, id in location_table.items():
		character_id = 0
		level = -1
		counter = 0
		shot_type_id = -1
		difficulty_id = -1

		# Check to see what type of location is it in order to skip it or not
		# First pass to see if it's a stage clear or an extra stage location
		valid_location = False
		if "Stage" in location:
			valid_location = True
		else:
			for check in EXTRA_CHECKS:
				if location.endswith(check):
					valid_location = True
					break

		# If it's not, we filter the difficulty
		if not valid_location:
			found = False
			for difficulty_name in DIFFICULTY_LIST:
				if difficulty_name in location:
					found = True
					if difficulty:
						valid_location = True
						break

			# If it's not a difficulty location and we don't want those, it's a valid location
			if not found and not difficulty:
				valid_location = True

		# If it's a valid location, we check if it's a shot type
		if valid_location:
			valid_location = False
			found = False
			for shot in SHOT_TYPE_LIST:
				if shot in location:
					found = True
					if shot_type:
						valid_location = True
						break

			if not found and not shot_type:
				valid_location = True

		if not valid_location:
			continue

		# Character
		for character in CHARACTERS_LIST:
			if (character in location):
				character_id = CHARACTER_NAME_TO_ID[character]
				break

		# Stage
		if "Stage" in location:
			level_id = location.split(" ")[-2]
			level = 6 if level_id == "Extra" else int(level_id)-1
			counter = len(STAGES_LIST[level])-1

			# If it's the final stage clear or the extra stage, we add it to the list
			if level == 5:
				stage_specific_location_id["stage_6"].append(id)
			elif level == 6:
				stage_specific_location_id["extra"].append(id)
		else:
			tmp_level = -1
			for stage in STAGES_LIST:
				tmp_level += 1
				tmp_counter = -1
				for check in stage:
					tmp_counter += 1
					if check in location:
						level = tmp_level
						counter = tmp_counter
						break

				if level >= 0:
					break

		# Shot Type
		if shot_type:
			for shot in SHOT_TYPE_LIST:
				if shot in location:
					shot_type_id = SHOT_NAME_TO_ID[shot]
					break

		# Difficulty
		if difficulty:
			difficulty_counter = -1
			for difficulty_name in DIFFICULTY_LIST:
				difficulty_counter += 1
				if difficulty_name in location:
					difficulty_id = difficulty_counter
					break

		mapping[id] = [character_id, level, counter, shot_type_id, difficulty_id]

	return mapping, stage_specific_location_id

def getPointerAddress(pm, base, offsets):
	address = base
	for offset in offsets[:-1]:
		address = pm.read_uint(address)
		address += offset
	return pm.read_uint(address) + offsets[-1]