import pymem
import pymem.exception
from .Tools import getPointerAddress
from .Variables import *

class gameController:
	"""Class accessing the game memory"""

	def __init__(self):
		self.pm = pymem.Pymem(GAME_NAME)

		self.addrStage = self.pm.base_address+ADDR_STAGE
		self.addrDifficulty = self.pm.base_address+ADDR_DIFFICULTY
		self.addrCharacter = self.pm.base_address+ADDR_CHARACTER
		self.addrShotType = self.pm.base_address+ADDR_SHOT_TYPE

		self.addrLives = self.pm.base_address+ADDR_LIVES
		self.addrPower = self.pm.base_address+ADDR_POWER

		self.addrPracticeStartingLives = self.pm.base_address+ADDR_PRACTICE_STARTING_LIVES
		self.addrNormalContinueLives = self.pm.base_address+ADDR_NORMAL_CONTINUE_LIVES
		self.addrStartingPowerPoint = self.pm.base_address+ADDR_STARTING_POWER_POINT

		self.addrScore =  self.pm.base_address+ADDR_SCORE

		self.addrStages = {
			REIMU: {
				SHOT_A: {
					EASY: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_STAGE_1[0], ADDR_REIMU_A_EASY_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_STAGE_2[0], ADDR_REIMU_A_EASY_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_STAGE_3[0], ADDR_REIMU_A_EASY_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_STAGE_4[0], ADDR_REIMU_A_EASY_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_STAGE_5[0], ADDR_REIMU_A_EASY_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_STAGE_6[0], ADDR_REIMU_A_EASY_STAGE_6[1:])
					],
					NORMAL: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_STAGE_1[0], ADDR_REIMU_A_NORMAL_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_STAGE_2[0], ADDR_REIMU_A_NORMAL_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_STAGE_3[0], ADDR_REIMU_A_NORMAL_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_STAGE_4[0], ADDR_REIMU_A_NORMAL_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_STAGE_5[0], ADDR_REIMU_A_NORMAL_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_STAGE_6[0], ADDR_REIMU_A_NORMAL_STAGE_6[1:])
					],
					HARD: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_STAGE_1[0], ADDR_REIMU_A_HARD_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_STAGE_2[0], ADDR_REIMU_A_HARD_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_STAGE_3[0], ADDR_REIMU_A_HARD_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_STAGE_4[0], ADDR_REIMU_A_HARD_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_STAGE_5[0], ADDR_REIMU_A_HARD_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_STAGE_6[0], ADDR_REIMU_A_HARD_STAGE_6[1:])
					],
					LUNATIC: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_STAGE_1[0], ADDR_REIMU_A_LUNATIC_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_STAGE_2[0], ADDR_REIMU_A_LUNATIC_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_STAGE_3[0], ADDR_REIMU_A_LUNATIC_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_STAGE_4[0], ADDR_REIMU_A_LUNATIC_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_STAGE_5[0], ADDR_REIMU_A_LUNATIC_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_STAGE_6[0], ADDR_REIMU_A_LUNATIC_STAGE_6[1:])
					],
					EXTRA: getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EXTRA[0], ADDR_REIMU_A_EXTRA[1:])
				},
				SHOT_B: {
					EASY: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_STAGE_1[0], ADDR_REIMU_B_EASY_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_STAGE_2[0], ADDR_REIMU_B_EASY_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_STAGE_3[0], ADDR_REIMU_B_EASY_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_STAGE_4[0], ADDR_REIMU_B_EASY_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_STAGE_5[0], ADDR_REIMU_B_EASY_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_STAGE_6[0], ADDR_REIMU_B_EASY_STAGE_6[1:])
					],
					NORMAL: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_STAGE_1[0], ADDR_REIMU_B_NORMAL_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_STAGE_2[0], ADDR_REIMU_B_NORMAL_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_STAGE_3[0], ADDR_REIMU_B_NORMAL_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_STAGE_4[0], ADDR_REIMU_B_NORMAL_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_STAGE_5[0], ADDR_REIMU_B_NORMAL_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_STAGE_6[0], ADDR_REIMU_B_NORMAL_STAGE_6[1:])
					],
					HARD: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_STAGE_1[0], ADDR_REIMU_B_HARD_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_STAGE_2[0], ADDR_REIMU_B_HARD_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_STAGE_3[0], ADDR_REIMU_B_HARD_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_STAGE_4[0], ADDR_REIMU_B_HARD_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_STAGE_5[0], ADDR_REIMU_B_HARD_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_STAGE_6[0], ADDR_REIMU_B_HARD_STAGE_6[1:])
					],
					LUNATIC: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_STAGE_1[0], ADDR_REIMU_B_LUNATIC_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_STAGE_2[0], ADDR_REIMU_B_LUNATIC_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_STAGE_3[0], ADDR_REIMU_B_LUNATIC_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_STAGE_4[0], ADDR_REIMU_B_LUNATIC_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_STAGE_5[0], ADDR_REIMU_B_LUNATIC_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_STAGE_6[0], ADDR_REIMU_B_LUNATIC_STAGE_6[1:])
					],
					EXTRA: getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EXTRA[0], ADDR_REIMU_B_EXTRA[1:])
				},
				SHOT_C: {
					EASY: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_STAGE_1[0], ADDR_REIMU_C_EASY_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_STAGE_2[0], ADDR_REIMU_C_EASY_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_STAGE_3[0], ADDR_REIMU_C_EASY_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_STAGE_4[0], ADDR_REIMU_C_EASY_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_STAGE_5[0], ADDR_REIMU_C_EASY_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_STAGE_6[0], ADDR_REIMU_C_EASY_STAGE_6[1:])
					],
					NORMAL: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_STAGE_1[0], ADDR_REIMU_C_NORMAL_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_STAGE_2[0], ADDR_REIMU_C_NORMAL_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_STAGE_3[0], ADDR_REIMU_C_NORMAL_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_STAGE_4[0], ADDR_REIMU_C_NORMAL_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_STAGE_5[0], ADDR_REIMU_C_NORMAL_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_STAGE_6[0], ADDR_REIMU_C_NORMAL_STAGE_6[1:])
					],
					HARD: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_STAGE_1[0], ADDR_REIMU_C_HARD_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_STAGE_2[0], ADDR_REIMU_C_HARD_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_STAGE_3[0], ADDR_REIMU_C_HARD_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_STAGE_4[0], ADDR_REIMU_C_HARD_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_STAGE_5[0], ADDR_REIMU_C_HARD_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_STAGE_6[0], ADDR_REIMU_C_HARD_STAGE_6[1:])
					],
					LUNATIC: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_STAGE_1[0], ADDR_REIMU_C_LUNATIC_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_STAGE_2[0], ADDR_REIMU_C_LUNATIC_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_STAGE_3[0], ADDR_REIMU_C_LUNATIC_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_STAGE_4[0], ADDR_REIMU_C_LUNATIC_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_STAGE_5[0], ADDR_REIMU_C_LUNATIC_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_STAGE_6[0], ADDR_REIMU_C_LUNATIC_STAGE_6[1:])
					],
					EXTRA: getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EXTRA[0], ADDR_REIMU_C_EXTRA[1:])
				}
			},
			MARISA: {
				SHOT_A: {
					EASY: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_STAGE_1[0], ADDR_MARISA_A_EASY_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_STAGE_2[0], ADDR_MARISA_A_EASY_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_STAGE_3[0], ADDR_MARISA_A_EASY_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_STAGE_4[0], ADDR_MARISA_A_EASY_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_STAGE_5[0], ADDR_MARISA_A_EASY_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_STAGE_6[0], ADDR_MARISA_A_EASY_STAGE_6[1:])
					],
					NORMAL: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_STAGE_1[0], ADDR_MARISA_A_NORMAL_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_STAGE_2[0], ADDR_MARISA_A_NORMAL_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_STAGE_3[0], ADDR_MARISA_A_NORMAL_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_STAGE_4[0], ADDR_MARISA_A_NORMAL_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_STAGE_5[0], ADDR_MARISA_A_NORMAL_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_STAGE_6[0], ADDR_MARISA_A_NORMAL_STAGE_6[1:])
					],
					HARD: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_STAGE_1[0], ADDR_MARISA_A_HARD_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_STAGE_2[0], ADDR_MARISA_A_HARD_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_STAGE_3[0], ADDR_MARISA_A_HARD_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_STAGE_4[0], ADDR_MARISA_A_HARD_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_STAGE_5[0], ADDR_MARISA_A_HARD_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_STAGE_6[0], ADDR_MARISA_A_HARD_STAGE_6[1:])
					],
					LUNATIC: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_STAGE_1[0], ADDR_MARISA_A_LUNATIC_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_STAGE_2[0], ADDR_MARISA_A_LUNATIC_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_STAGE_3[0], ADDR_MARISA_A_LUNATIC_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_STAGE_4[0], ADDR_MARISA_A_LUNATIC_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_STAGE_5[0], ADDR_MARISA_A_LUNATIC_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_STAGE_6[0], ADDR_MARISA_A_LUNATIC_STAGE_6[1:])
					],
					EXTRA: getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EXTRA[0], ADDR_MARISA_A_EXTRA[1:])
				},
				SHOT_B: {
					EASY: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_STAGE_1[0], ADDR_MARISA_B_EASY_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_STAGE_2[0], ADDR_MARISA_B_EASY_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_STAGE_3[0], ADDR_MARISA_B_EASY_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_STAGE_4[0], ADDR_MARISA_B_EASY_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_STAGE_5[0], ADDR_MARISA_B_EASY_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_STAGE_6[0], ADDR_MARISA_B_EASY_STAGE_6[1:])
					],
					NORMAL: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_STAGE_1[0], ADDR_MARISA_B_NORMAL_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_STAGE_2[0], ADDR_MARISA_B_NORMAL_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_STAGE_3[0], ADDR_MARISA_B_NORMAL_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_STAGE_4[0], ADDR_MARISA_B_NORMAL_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_STAGE_5[0], ADDR_MARISA_B_NORMAL_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_STAGE_6[0], ADDR_MARISA_B_NORMAL_STAGE_6[1:])
					],
					HARD: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_STAGE_1[0], ADDR_MARISA_B_HARD_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_STAGE_2[0], ADDR_MARISA_B_HARD_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_STAGE_3[0], ADDR_MARISA_B_HARD_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_STAGE_4[0], ADDR_MARISA_B_HARD_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_STAGE_5[0], ADDR_MARISA_B_HARD_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_STAGE_6[0], ADDR_MARISA_B_HARD_STAGE_6[1:])
					],
					LUNATIC: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_STAGE_1[0], ADDR_MARISA_B_LUNATIC_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_STAGE_2[0], ADDR_MARISA_B_LUNATIC_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_STAGE_3[0], ADDR_MARISA_B_LUNATIC_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_STAGE_4[0], ADDR_MARISA_B_LUNATIC_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_STAGE_5[0], ADDR_MARISA_B_LUNATIC_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_STAGE_6[0], ADDR_MARISA_B_LUNATIC_STAGE_6[1:])
					],
					EXTRA: getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EXTRA[0], ADDR_MARISA_B_EXTRA[1:])
				},
				SHOT_C: {
					EASY: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_STAGE_1[0], ADDR_MARISA_C_EASY_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_STAGE_2[0], ADDR_MARISA_C_EASY_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_STAGE_3[0], ADDR_MARISA_C_EASY_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_STAGE_4[0], ADDR_MARISA_C_EASY_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_STAGE_5[0], ADDR_MARISA_C_EASY_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_STAGE_6[0], ADDR_MARISA_C_EASY_STAGE_6[1:])
					],
					NORMAL: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_STAGE_1[0], ADDR_MARISA_C_NORMAL_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_STAGE_2[0], ADDR_MARISA_C_NORMAL_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_STAGE_3[0], ADDR_MARISA_C_NORMAL_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_STAGE_4[0], ADDR_MARISA_C_NORMAL_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_STAGE_5[0], ADDR_MARISA_C_NORMAL_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_STAGE_6[0], ADDR_MARISA_C_NORMAL_STAGE_6[1:])
					],
					HARD: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_STAGE_1[0], ADDR_MARISA_C_HARD_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_STAGE_2[0], ADDR_MARISA_C_HARD_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_STAGE_3[0], ADDR_MARISA_C_HARD_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_STAGE_4[0], ADDR_MARISA_C_HARD_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_STAGE_5[0], ADDR_MARISA_C_HARD_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_STAGE_6[0], ADDR_MARISA_C_HARD_STAGE_6[1:])
					],
					LUNATIC: [
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_STAGE_1[0], ADDR_MARISA_C_LUNATIC_STAGE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_STAGE_2[0], ADDR_MARISA_C_LUNATIC_STAGE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_STAGE_3[0], ADDR_MARISA_C_LUNATIC_STAGE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_STAGE_4[0], ADDR_MARISA_C_LUNATIC_STAGE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_STAGE_5[0], ADDR_MARISA_C_LUNATIC_STAGE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_STAGE_6[0], ADDR_MARISA_C_LUNATIC_STAGE_6[1:])
					],
					EXTRA: getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EXTRA[0], ADDR_MARISA_C_EXTRA[1:])
				}
			}
		}

		self.addrInput = self.pm.base_address+ADDR_INPUT
		self.addrGameMode = self.pm.base_address+ADDR_GAME_MODE
		self.addrMenu = getPointerAddress(self.pm, self.pm.base_address+ADDR_MENU[0], ADDR_MENU[1:])
		self.addrMenuCursor = getPointerAddress(self.pm, self.pm.base_address+ADDR_MENU_CURSOR[0], ADDR_MENU_CURSOR[1:])
		self.addrIsBossPresent1 = getPointerAddress(self.pm, self.pm.base_address+ADDR_IS_BOSS_PRESENT_1[0], ADDR_IS_BOSS_PRESENT_1[1:])
		self.addrIsBossPresent2 = getPointerAddress(self.pm, self.pm.base_address+ADDR_IS_BOSS_PRESENT_2[0], ADDR_IS_BOSS_PRESENT_2[1:])
		self.addrDemoCondition = self.pm.base_address+ADDR_DEMO_CONDITION
		self.addrFocusCondition = self.pm.base_address+ADDR_FOCUS_CONDITION
		self.addrExtraMode = self.pm.base_address+ADDR_EXTRA_MODE

		self.addrKillCondition = self.pm.base_address+ADDR_KILL_CONDITION

		self.addrExtraLockCharacterHack = [
			self.pm.base_address+ADDR_EXTRA_LOCK_CHARACTER_HACK[0],
			self.pm.base_address+ADDR_EXTRA_LOCK_CHARACTER_HACK[1],
			self.pm.base_address+ADDR_EXTRA_LOCK_CHARACTER_HACK[2],
		]

		self.addrNormalSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED[0], ADDR_NORMAL_SPEED[1:])
		self.addrFocusSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED[0], ADDR_FOCUS_SPEED[1:])
		self.addrNormalSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED_D[0], ADDR_NORMAL_SPEED_D[1:])
		self.addrFocusSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED_D[0], ADDR_FOCUS_SPEED_D[1:])

		self.addrCustomSoundId = self.pm.base_address+ADDR_CUSTOM_SOUND_ID
		self.addrSoundHack1 = self.pm.base_address+ADDR_SOUND_HACK_1
		self.addrSoundHack2 = self.pm.base_address+ADDR_SOUND_HACK_2
		self.addrMinimumCursorDownHack = self.pm.base_address+ADDR_MIN_CURSOR_DOWN_HACK
		self.addrMinimumCursorUpHack = self.pm.base_address+ADDR_MIN_CURSOR_UP_HACK
		self.addPowerHack = self.pm.base_address+ADDR_POWER_HACK

		self.addrMinimumCursorDown = self.pm.base_address+ADDR_MINIMUM_CURSOR_DOWN
		self.addrMinimumCursorUp = self.pm.base_address+ADDR_MINIMUM_CURSOR_UP

		self.addrPracticeScore = {
			REIMU:
			{
				SHOT_A:
				{
					EASY:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_1[0], ADDR_REIMU_A_EASY_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_2[0], ADDR_REIMU_A_EASY_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_3[0], ADDR_REIMU_A_EASY_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_4[0], ADDR_REIMU_A_EASY_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_5[0], ADDR_REIMU_A_EASY_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_EASY_SCORE_6[0], ADDR_REIMU_A_EASY_SCORE_6[1:])
					],
					NORMAL:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_1[0], ADDR_REIMU_A_NORMAL_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_2[0], ADDR_REIMU_A_NORMAL_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_3[0], ADDR_REIMU_A_NORMAL_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_4[0], ADDR_REIMU_A_NORMAL_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_5[0], ADDR_REIMU_A_NORMAL_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_NORMAL_SCORE_6[0], ADDR_REIMU_A_NORMAL_SCORE_6[1:])
					],
					HARD:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_1[0], ADDR_REIMU_A_HARD_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_2[0], ADDR_REIMU_A_HARD_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_3[0], ADDR_REIMU_A_HARD_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_4[0], ADDR_REIMU_A_HARD_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_5[0], ADDR_REIMU_A_HARD_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_HARD_SCORE_6[0], ADDR_REIMU_A_HARD_SCORE_6[1:])
					],
					LUNATIC:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_1[0], ADDR_REIMU_A_LUNATIC_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_2[0], ADDR_REIMU_A_LUNATIC_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_3[0], ADDR_REIMU_A_LUNATIC_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_4[0], ADDR_REIMU_A_LUNATIC_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_5[0], ADDR_REIMU_A_LUNATIC_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_A_LUNATIC_SCORE_6[0], ADDR_REIMU_A_LUNATIC_SCORE_6[1:])
					],
				},
				SHOT_B:
				{
					EASY:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_1[0], ADDR_REIMU_B_EASY_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_2[0], ADDR_REIMU_B_EASY_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_3[0], ADDR_REIMU_B_EASY_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_4[0], ADDR_REIMU_B_EASY_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_5[0], ADDR_REIMU_B_EASY_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_EASY_SCORE_6[0], ADDR_REIMU_B_EASY_SCORE_6[1:])
					],
					NORMAL:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_1[0], ADDR_REIMU_B_NORMAL_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_2[0], ADDR_REIMU_B_NORMAL_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_3[0], ADDR_REIMU_B_NORMAL_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_4[0], ADDR_REIMU_B_NORMAL_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_5[0], ADDR_REIMU_B_NORMAL_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_NORMAL_SCORE_6[0], ADDR_REIMU_B_NORMAL_SCORE_6[1:])
					],
					HARD:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_1[0], ADDR_REIMU_B_HARD_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_2[0], ADDR_REIMU_B_HARD_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_3[0], ADDR_REIMU_B_HARD_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_4[0], ADDR_REIMU_B_HARD_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_5[0], ADDR_REIMU_B_HARD_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_HARD_SCORE_6[0], ADDR_REIMU_B_HARD_SCORE_6[1:])
					],
					LUNATIC:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_1[0], ADDR_REIMU_B_LUNATIC_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_2[0], ADDR_REIMU_B_LUNATIC_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_3[0], ADDR_REIMU_B_LUNATIC_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_4[0], ADDR_REIMU_B_LUNATIC_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_5[0], ADDR_REIMU_B_LUNATIC_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_B_LUNATIC_SCORE_6[0], ADDR_REIMU_B_LUNATIC_SCORE_6[1:])
					],
				},
				SHOT_C:
				{
					EASY:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_SCORE_1[0], ADDR_REIMU_C_EASY_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_SCORE_2[0], ADDR_REIMU_C_EASY_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_SCORE_3[0], ADDR_REIMU_C_EASY_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_SCORE_4[0], ADDR_REIMU_C_EASY_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_SCORE_5[0], ADDR_REIMU_C_EASY_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_EASY_SCORE_6[0], ADDR_REIMU_C_EASY_SCORE_6[1:])
					],
					NORMAL:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_SCORE_1[0], ADDR_REIMU_C_NORMAL_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_SCORE_2[0], ADDR_REIMU_C_NORMAL_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_SCORE_3[0], ADDR_REIMU_C_NORMAL_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_SCORE_4[0], ADDR_REIMU_C_NORMAL_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_SCORE_5[0], ADDR_REIMU_C_NORMAL_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_NORMAL_SCORE_6[0], ADDR_REIMU_C_NORMAL_SCORE_6[1:])
					],
					HARD:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_SCORE_1[0], ADDR_REIMU_C_HARD_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_SCORE_2[0], ADDR_REIMU_C_HARD_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_SCORE_3[0], ADDR_REIMU_C_HARD_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_SCORE_4[0], ADDR_REIMU_C_HARD_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_SCORE_5[0], ADDR_REIMU_C_HARD_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_HARD_SCORE_6[0], ADDR_REIMU_C_HARD_SCORE_6[1:])
					],
					LUNATIC:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_SCORE_1[0], ADDR_REIMU_C_LUNATIC_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_SCORE_2[0], ADDR_REIMU_C_LUNATIC_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_SCORE_3[0], ADDR_REIMU_C_LUNATIC_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_SCORE_4[0], ADDR_REIMU_C_LUNATIC_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_SCORE_5[0], ADDR_REIMU_C_LUNATIC_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_REIMU_C_LUNATIC_SCORE_6[0], ADDR_REIMU_C_LUNATIC_SCORE_6[1:])
					],
				}
			},
			MARISA:
			{
				SHOT_A:
				{
					EASY:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_1[0], ADDR_MARISA_A_EASY_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_2[0], ADDR_MARISA_A_EASY_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_3[0], ADDR_MARISA_A_EASY_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_4[0], ADDR_MARISA_A_EASY_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_5[0], ADDR_MARISA_A_EASY_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_EASY_SCORE_6[0], ADDR_MARISA_A_EASY_SCORE_6[1:])
					],
					NORMAL:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_1[0], ADDR_MARISA_A_NORMAL_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_2[0], ADDR_MARISA_A_NORMAL_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_3[0], ADDR_MARISA_A_NORMAL_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_4[0], ADDR_MARISA_A_NORMAL_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_5[0], ADDR_MARISA_A_NORMAL_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_NORMAL_SCORE_6[0], ADDR_MARISA_A_NORMAL_SCORE_6[1:])
					],
					HARD:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_1[0], ADDR_MARISA_A_HARD_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_2[0], ADDR_MARISA_A_HARD_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_3[0], ADDR_MARISA_A_HARD_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_4[0], ADDR_MARISA_A_HARD_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_5[0], ADDR_MARISA_A_HARD_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_HARD_SCORE_6[0], ADDR_MARISA_A_HARD_SCORE_6[1:])
					],
					LUNATIC:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_1[0], ADDR_MARISA_A_LUNATIC_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_2[0], ADDR_MARISA_A_LUNATIC_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_3[0], ADDR_MARISA_A_LUNATIC_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_4[0], ADDR_MARISA_A_LUNATIC_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_5[0], ADDR_MARISA_A_LUNATIC_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_A_LUNATIC_SCORE_6[0], ADDR_MARISA_A_LUNATIC_SCORE_6[1:])
					],
				},
				SHOT_B:
				{
					EASY:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_1[0], ADDR_MARISA_B_EASY_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_2[0], ADDR_MARISA_B_EASY_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_3[0], ADDR_MARISA_B_EASY_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_4[0], ADDR_MARISA_B_EASY_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_5[0], ADDR_MARISA_B_EASY_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_EASY_SCORE_6[0], ADDR_MARISA_B_EASY_SCORE_6[1:])
					],
					NORMAL:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_1[0], ADDR_MARISA_B_NORMAL_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_2[0], ADDR_MARISA_B_NORMAL_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_3[0], ADDR_MARISA_B_NORMAL_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_4[0], ADDR_MARISA_B_NORMAL_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_5[0], ADDR_MARISA_B_NORMAL_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_NORMAL_SCORE_6[0], ADDR_MARISA_B_NORMAL_SCORE_6[1:])
					],
					HARD:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_1[0], ADDR_MARISA_B_HARD_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_2[0], ADDR_MARISA_B_HARD_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_3[0], ADDR_MARISA_B_HARD_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_4[0], ADDR_MARISA_B_HARD_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_5[0], ADDR_MARISA_B_HARD_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_HARD_SCORE_6[0], ADDR_MARISA_B_HARD_SCORE_6[1:])
					],
					LUNATIC:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_1[0], ADDR_MARISA_B_LUNATIC_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_2[0], ADDR_MARISA_B_LUNATIC_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_3[0], ADDR_MARISA_B_LUNATIC_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_4[0], ADDR_MARISA_B_LUNATIC_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_5[0], ADDR_MARISA_B_LUNATIC_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_B_LUNATIC_SCORE_6[0], ADDR_MARISA_B_LUNATIC_SCORE_6[1:])
					],
				},
				SHOT_C:
				{
					EASY:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_SCORE_1[0], ADDR_MARISA_C_EASY_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_SCORE_2[0], ADDR_MARISA_C_EASY_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_SCORE_3[0], ADDR_MARISA_C_EASY_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_SCORE_4[0], ADDR_MARISA_C_EASY_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_SCORE_5[0], ADDR_MARISA_C_EASY_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_EASY_SCORE_6[0], ADDR_MARISA_C_EASY_SCORE_6[1:])
					],
					NORMAL:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_SCORE_1[0], ADDR_MARISA_C_NORMAL_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_SCORE_2[0], ADDR_MARISA_C_NORMAL_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_SCORE_3[0], ADDR_MARISA_C_NORMAL_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_SCORE_4[0], ADDR_MARISA_C_NORMAL_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_SCORE_5[0], ADDR_MARISA_C_NORMAL_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_NORMAL_SCORE_6[0], ADDR_MARISA_C_NORMAL_SCORE_6[1:])
					],
					HARD:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_SCORE_1[0], ADDR_MARISA_C_HARD_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_SCORE_2[0], ADDR_MARISA_C_HARD_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_SCORE_3[0], ADDR_MARISA_C_HARD_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_SCORE_4[0], ADDR_MARISA_C_HARD_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_SCORE_5[0], ADDR_MARISA_C_HARD_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_HARD_SCORE_6[0], ADDR_MARISA_C_HARD_SCORE_6[1:])
					],
					LUNATIC:
					[
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_SCORE_1[0], ADDR_MARISA_C_LUNATIC_SCORE_1[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_SCORE_2[0], ADDR_MARISA_C_LUNATIC_SCORE_2[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_SCORE_3[0], ADDR_MARISA_C_LUNATIC_SCORE_3[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_SCORE_4[0], ADDR_MARISA_C_LUNATIC_SCORE_4[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_SCORE_5[0], ADDR_MARISA_C_LUNATIC_SCORE_5[1:]),
						getPointerAddress(self.pm, self.pm.base_address+ADDR_MARISA_C_LUNATIC_SCORE_6[0], ADDR_MARISA_C_LUNATIC_SCORE_6[1:])
					],
				}
			}
		}

	def getStage(self):
		return int.from_bytes(self.pm.read_bytes(self.addrStage, 1))

	def getDifficulty(self):
		return int.from_bytes(self.pm.read_bytes(self.addrDifficulty, 1))

	def getCharacter(self):
		return int.from_bytes(self.pm.read_bytes(self.addrCharacter, 1))
	
	def getShotType(self):
		return int.from_bytes(self.pm.read_bytes(self.addrShotType, 1))

	def getLives(self):
		return int.from_bytes(self.pm.read_bytes(self.addrLives, 1))

	def getPower(self):
		return int.from_bytes(self.pm.read_bytes(self.addrPower, 1))

	def getScore(self):
		return self.pm.read_int(self.addrScore)

	def getCharacterStageAccess(self, character, shot, difficulty, stage):
		if difficulty == EXTRA:
			return int.from_bytes(self.addrStages[character][shot][difficulty], 1)
		else:
			return int.from_bytes(self.addrStages[character][shot][difficulty][stage], 1)

	def getInput(self):
		return int.from_bytes(self.pm.read_bytes(self.addrInput, 1))

	def getGameMode(self):
		try:
			mode = int.from_bytes(self.pm.read_bytes(self.addrGameMode, 1))
		except pymem.exception.MemoryReadError as e:
			mode = -2

		return mode

	def getMenu(self):
		try:
			self.addrMenu = getPointerAddress(self.pm, self.pm.base_address+ADDR_MENU[0], ADDR_MENU[1:])
			menu = int.from_bytes(self.pm.read_bytes(self.addrMenu, 1))
		except pymem.exception.MemoryReadError as e:
			menu = -1

		return menu

	def getMenuCursor(self):
		self.addrMenuCursor = getPointerAddress(self.pm, self.pm.base_address+ADDR_MENU_CURSOR[0], ADDR_MENU_CURSOR[1:])
		return int.from_bytes(self.pm.read_bytes(self.addrMenuCursor, 1))

	def getNormalSpeed(self):
		self.addrNormalSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED[0], ADDR_NORMAL_SPEED[1:])
		return self.pm.read_int(self.addrNormalSpeed)

	def getFocusSpeed(self):
		self.addrFocusSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED[0], ADDR_FOCUS_SPEED[1:])
		return self.pm.read_int(self.addrFocusSpeed)

	def getNormalSpeedD(self):
		self.addrNormalSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED_D[0], ADDR_NORMAL_SPEED_D[1:])
		return self.pm.read_int(self.addrNormalSpeedD)

	def getFocusSpeedD(self):
		self.addrFocusSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED_D[0], ADDR_FOCUS_SPEED_D[1:])
		return self.pm.read_int(self.addrFocusSpeedD)

	def getCustomSoundId(self):
		return int.from_bytes(self.pm.read_bytes(self.addrCustomSoundId, 1))

	def getIsBossPresent1(self):
		self.addrIsBossPresent1 = getPointerAddress(self.pm, self.pm.base_address+ADDR_IS_BOSS_PRESENT_1[0], ADDR_IS_BOSS_PRESENT_1[1:])
		return int.from_bytes(self.pm.read_bytes(self.addrIsBossPresent1, 4))

	def getIsBossPresent2(self):
		self.addrIsBossPresent2 = getPointerAddress(self.pm, self.pm.base_address+ADDR_IS_BOSS_PRESENT_2[0], ADDR_IS_BOSS_PRESENT_2[1:])
		return int.from_bytes(self.pm.read_bytes(self.addrIsBossPresent2, 4))

	def getPracticeStageScore(self, characterId, difficultyId, stageId):
		return int.from_bytes(self.pm.read_bytes(self.addrPracticeScore[characterId][difficultyId][stageId], 4))

	def getMinimumCursorDown(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMinimumCursorDown, 1))

	def getMinimumCursorUp(self):
		return int.from_bytes(self.pm.read_bytes(self.addrMinimumCursorUp, 1))
	
	def getExtraMode(self):
		return int.from_bytes(self.pm.read_bytes(self.addrExtraMode, 1))

	def setMenuCursor(self, newCursor):
		self.addrMenuCursor = getPointerAddress(self.pm, self.pm.base_address+ADDR_MENU_CURSOR[0], ADDR_MENU_CURSOR[1:])
		self.pm.write_bytes(self.addrMenuCursor, bytes([newCursor]), 1)

	def setStage(self, newStage):
		self.pm.write_short(self.addrStage, newStage)

	def setDifficulty(self, newDifficulty):
		self.pm.write_short(self.addrDifficulty, newDifficulty)

	def setCharacter(self, newCharacter):
		self.pm.write_short(self.addrCharacter, newCharacter)

	def setLives(self, newLives):
		self.pm.write_bytes(self.addrLives, bytes([newLives]), 1)

	def setPower(self, newPower):
		self.pm.write_bytes(self.addrPower, bytes([newPower]), 1)

	def setPracticeStartingLives(self, newPracticeStartingLives):
		self.pm.write_bytes(self.addrPracticeStartingLives, bytes([newPracticeStartingLives]), 1)

	def setNormalContinueLives(self, newNormalContinueLives):
		self.pm.write_bytes(self.addrNormalContinueLives, bytes([newNormalContinueLives]), 1)

	def setStartingPowerPoint(self, newStartingPowerPoint):
		self.pm.write_bytes(self.addrStartingPowerPoint, bytes([newStartingPowerPoint]), 1)

	def setCharacterStage(self, character, shot_type, difficulty, stage, new_value):
		if difficulty == EXTRA:
			self.pm.write_int(self.addrStages[character][shot_type][difficulty], new_value)
		else:
			self.pm.write_int(self.addrStages[character][shot_type][difficulty][stage], new_value)

	def setInput(self, newInput):
		self.pm.write_bytes(self.addrInput, bytes([newInput]), 1)

	def setMinimumCursorDown(self, minimumCursorDown):
		self.pm.write_bytes(self.addrMinimumCursorDown, bytes([minimumCursorDown]), 1)

	def setMinimumCursorUp(self, minimumCursorUp):
		self.pm.write_bytes(self.addrMinimumCursorUp, bytes([minimumCursorUp]), 1)

	def setNormalSpeed(self, newNormalSpeed):
		self.addrNormalSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED[0], ADDR_NORMAL_SPEED[1:])
		self.pm.write_int(self.addrNormalSpeed, newNormalSpeed)

	def setFocusSpeed(self, newFocusSpeed):
		self.addrFocusSpeed = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED[0], ADDR_FOCUS_SPEED[1:])
		self.pm.write_int(self.addrFocusSpeed, newFocusSpeed)

	def setNormalSpeedD(self, newNormalSpeedD):
		self.addrNormalSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_NORMAL_SPEED_D[0], ADDR_NORMAL_SPEED_D[1:])
		self.pm.write_int(self.addrNormalSpeedD, newNormalSpeedD)

	def setFocusSpeedD(self, newFocusSpeedD):
		self.addrFocusSpeedD = getPointerAddress(self.pm, self.pm.base_address+ADDR_FOCUS_SPEED_D[0], ADDR_FOCUS_SPEED_D[1:])
		self.pm.write_int(self.addrFocusSpeedD, newFocusSpeedD)

	def setPracticeStageScore(self, characterId, shotId, difficultyId, stageId, newScore):
		return self.pm.write_int(self.addrPracticeScore[characterId][shotId][difficultyId][stageId], newScore)

	def setKill(self, active):
		if active:
			self.pm.write_bytes(self.addrKillCondition, bytes([0x90, 0x90, 0x90, 0x90, 0x90]), 5)
		else:
			self.pm.write_bytes(self.addrKillCondition, bytes([0xE9, 0xDC, 0x02, 0x00, 0x00]), 5)

	def setLockToAllDifficulty(self):
		self.pm.write_bytes(self.addrExtraLockCharacterHack[0], bytes([0x90, 0x90]), 2)
		self.pm.write_bytes(self.addrExtraLockCharacterHack[1], bytes([0x90, 0x90, 0x90, 0x90, 0x90, 0x90]), 6)
		self.pm.write_bytes(self.addrExtraLockCharacterHack[2], bytes([0x90, 0x90, 0x90, 0x90, 0x90, 0x90]), 6)

	def setFocus(self, active):
		if active:
			self.pm.write_bytes(self.addrFocusCondition, bytes([0x0F, 0x84, 0xEA, 0x00, 0x00, 0x00]), 6)
		else:
			self.pm.write_bytes(self.addrFocusCondition, bytes([0xE9, 0xEB, 0x00, 0x00, 0x00, 0x90]), 6)

	def initSoundHack(self):
		soundIdHex = "00"+hex(self.addrCustomSoundId)[2:]
		soundId = [int(soundIdHex[i:i+2], 16) for i in range(0, len(soundIdHex), 2)]
		self.pm.write_bytes(self.addrSoundHack2, bytes([0x53,
														0x8B, 0x3D, soundId[3], soundId[2], soundId[1], soundId[0],
														0xB9, 0x90, 0x25, 0x49, 0x00,
														0xE8, 0xE5, 0xA5, 0x02, 0x00,
														0xC7, 0x05, soundId[3], soundId[2], soundId[1], soundId[0], 0x30, 0x00, 0x00, 0x00,
														0xB9, 0x01, 0x00, 0x00, 0x00,
														0xB8, 0x01, 0x00, 0x00, 0x00,
														0xC3]), 38)

		self.pm.write_bytes(self.addrSoundHack1, bytes([0x81, 0x3D, soundId[3], soundId[2], soundId[1], soundId[0], 0x30, 0x00, 0x00, 0x00,
												  		0x75, 0x0B,
														0xC3]), 13)

	def setCustomSoundId(self, soundId = 0x0D):
		self.pm.write_bytes(self.addrCustomSoundId, bytes([soundId]), 1)

	def initStartingPower(self):
		self.pm.write_bytes(self.addPowerHack, bytes([0xC6, 0x05, 0x48, 0x4C, 0x47, 0x00, 0x00, 0x90, 0x90,	0x83, 0xE1, 0xFB]), 12)

	def initCursorHack(self):
		self.pm.write_bytes(self.addrMinimumCursorUpHack, bytes([0x4E, 0x85, 0xC9, 0x74, 0x04, 0x89, 0x30]), 7)
		self.pm.write_bytes(self.addrMinimumCursorDownHack, bytes([0xC6, 0x00, 0x00, 0x90, 0xEB, 0x0A]), 6)

	def disableDemo(self):
		self.pm.write_bytes(self.addrDemoCondition, bytes([0x90]), 1)