from dataclasses import dataclass
from Options import Choice, Range, Toggle, PerGameCommonOptions

class Mode(Choice):
	"""
	Which mode you are playing on.
    Practice Mode: You need to unlock the stage in order to progress.
    Normal Mode: The resources are only given at Stage 1. Restriction in life or difficulty for stages 3/4 and 5/6 and character are the only logical gate
	"""
	display_name = "Mode played"
	option_practice = 0
	option_normal = 1
	default = 0

class StageUnlock(Choice):
	"""
	[Practice] How the stage unlock are grouped in Practice mode and for the Extra Stage if it's apart
    Global: No group
    By Character: Stage group by character
    By Shot Type: Stage group by shot type. Need check by shot type or check by difficulty in order to have enough locations. Stages will be unlocked by character if there is not enought location.
	"""
	display_name = "Stage unlock mode"
	option_global = 0
	option_by_character = 1
	option_by_shot_type = 2

class ProgressiveStage(Toggle):
	"""
	[Practice] In Practice mode, determine if stages are unlocked progressively
	"""
	display_name = "Progressive Stage Unlock"
	default = True

class ExcludeLunatic(Toggle):
	"""Exclude Lunatic difficulty. Start on Hard instead."""
	display_name = "Exclude Lunatic difficulty"

class NumberLifeMid(Range):
	"""Number of life the randomizer expect you to have before facing Nitori and Aya"""
	display_name = "Number of life expected in order to face Nitori and Aya"
	range_start = 0
	range_end = 8
	default = 0

class DifficultyMid(Choice):
	"""The difficulty expected in order to face Nitori and Aya (Starting from Lunatic and go to Easy)"""
	display_name = "Difficulty in order to face Nitori and Aya"
	option_lunatic = 0
	option_hard = 1
	option_normal = 2
	option_easy = 3
	default = 0

class NumberLifeEnd(Range):
	"""Number of life the randomizer expect you to have before facing Sanae and Kanako"""
	display_name = "Number of life expected in order to face Sanae and Kanako"
	range_start = 0
	range_end = 8
	default = 0

class DifficultyEnd(Choice):
	"""The difficulty expected in order to face Sanae and Kanako (Starting from Lunatic and go to Easy)"""
	display_name = "Difficulty in order to face Sanae and Kanako"
	option_lunatic = 0
	option_hard = 1
	option_normal = 2
	option_easy = 3
	default = 0

class ExtraStage(Choice):
	"""
	Determine if the extra stage is included
    Linear: The extra stage is considered as the 7th stage.
    Apart: The extra stage has it's own item for it to be unlocked
    This option will follow the rule of how the stage are unlocked in Practice Mode (Global, By Character or By Shot Type)
	"""
	display_name = "Determine if the extra stage is included"
	option_exclude = 0
	option_include_linear = 1
	option_include_apart = 2
	default = 0

class NumberLifeExtra(Range):
	"""Number of life the randomizer expect you to have before facing Suwako"""
	display_name = "Number of life expected in order to face Suwako"
	range_start = 0
	range_end = 8
	default = 0

class ShotTypeCheck(Toggle):
	"""If each shot type have their own check and are not just separated by character"""
	display_name = "Shot Type Check"

class DifficultyCheck(Choice):
	"""
	If checks are separated by difficulty.
	"""
	display_name = "Difficulty Check"
	option_false = 0
	option_true = 1

class CheckMultipleDifficulty(Toggle):
	"""
	For difficulty check, choose if the check of the highest difficulty include the check of the lower difficulties that are unlocked. Can be changed later.
	"""
	display_name = "Multiple Difficulty Check"

class Goal(Choice):
	"""
	If the Extra stage is included, determine which boss is the goal.
	"""
	display_name = "Goal"
	option_kanako = 0
	option_suwako = 1
	option_all = 2
	default = 0

class EndingRequired(Choice):
	"""
	How many time do you need to beat the required boss if it's the selected goal.
	"""
	display_name = "How many time do you need to beat the required boss"
	option_once = 0
	option_all_characters = 1
	option_all_shot_types = 2
	default = 0

class DeathLink(Toggle):
	"""
	When you die, everyone who enabled death link dies. Of course, the reverse is true too. Can be changed later.
	"""
	display_name = "Death Link"

class DeathLinkTrigger(Choice):
	"""
	When does a death link is triggerd. Can be changed later.
    Life: Send a death link when losing a life
    Game Over: Send a death link when getting a game over
	"""
	display_name = "Death Link Trigger"
	option_life = 0
	option_game_over = 1
	default = 0

class DeathLinkAmnesty(Range):
	"""
	Number of death before sending a DeathLink. Can be changed later.
	"""
	display_name = "DeathLink Amnesty"
	range_start = 0
	range_end = 10
	default = 0

class RingLink(Toggle):
    """
    Whether your in-level Power Point gain/loss is linked to other players. Can be changed later.
    """
    display_name = "Ring Link"

class LimitLives(Range):
	"""Limit on the maximum number of lives you can have. It only apply on the client, not on the item pool or logic. Can be changed later."""
	display_name = "Lives limit"
	range_start = 0
	range_end = 9
	default = 9

class Traps(Range):
	"""Percentage of fillers that are traps"""
	display_name = "Percentage of fillers that are traps"
	range_start = 0
	range_end = 100
	default = 0

class PowerPointTrap(Range):
	"""
	Weight of the -50% power point trap.
    This trap reduce the power point by 50%
	"""
	display_name = "-50% power point trap"
	range_start = 0
	range_end = 100
	default = 20

class LifeTrap(Range):
	"""
	Weight of the -1 life trap.
    This trap remove 1 life
	"""
	display_name = "-1 life trap"
	range_start = 0
	range_end = 100
	default = 0

class ReverseMovementTrap(Range):
	"""
	Weight of the Reverse Movement trap.
    This trap reverse the movement of the player
	"""
	display_name = "Reverse Movement trap"
	range_start = 0
	range_end = 100
	default = 20

class AyaSpeedTrap(Range):
	"""
	Weight of the Aya speed trap.
    This trap make the speed of the player more extreme (faster normally, slower focus)
	"""
	display_name = "Aya speed trap"
	range_start = 0
	range_end = 100
	default = 20

class FreezeTrap(Range):
	"""
	Weight of the freeze trap.
    This trap freeze the player for a short amount of time
	"""
	display_name = "Freeze trap"
	range_start = 0
	range_end = 100
	default = 5

@dataclass
class Th10Options(PerGameCommonOptions):
	mode: Mode
	stage_unlock: StageUnlock
	progressive_stage: ProgressiveStage
	exclude_lunatic: ExcludeLunatic
	number_life_mid: NumberLifeMid
	difficulty_mid: DifficultyMid
	number_life_end: NumberLifeEnd
	difficulty_end: DifficultyEnd
	extra_stage: ExtraStage
	number_life_extra: NumberLifeExtra
	shot_type: ShotTypeCheck
	difficulty_check: DifficultyCheck
	check_multiple_difficulty: CheckMultipleDifficulty
	goal: Goal
	ending_required: EndingRequired
	death_link: DeathLink
	death_link_trigger: DeathLinkTrigger
	death_link_amnesty: DeathLinkAmnesty
	ring_link: RingLink
	limit_lives: LimitLives
	traps: Traps
	power_point_trap: PowerPointTrap
	life_trap: LifeTrap
	reverse_movement_trap: ReverseMovementTrap
	aya_speed_trap: AyaSpeedTrap
	freeze_trap: FreezeTrap