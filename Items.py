from typing import Dict, NamedTuple, Optional
from .Variables import *

from BaseClasses import Item, ItemClassification

class TItem(Item):
	game: str = DISPLAY_NAME

class TItemData(NamedTuple):
	category: str
	code: Optional[int] = None
	classification: ItemClassification = ItemClassification.filler
	max_quantity: int = 1
	weight: int = 1

def get_items_by_category(category: str) -> Dict[str, TItemData]:
	item_dict: Dict[str, TItemData] = {}
	for name, data in item_table.items():
		if data.category == category:
			item_dict.setdefault(name, data)

	return item_dict

item_table: Dict[str, TItemData] = {
	# Items
	"+1 Life":				TItemData("Items", STARTING_ID + 0, ItemClassification.progression, 9),
	"Lower Difficulty":		TItemData("Items", STARTING_ID + 1, ItemClassification.progression, 3),
	"+0.50 Power Point":		TItemData("Power Point", STARTING_ID + 2, ItemClassification.useful, 10),

	# Characters
	"Reimu A - Homing Type":		TItemData("Characters", STARTING_ID + 100, ItemClassification.progression),
	"Reimu B - Forward Focus Type":	TItemData("Characters", STARTING_ID + 101, ItemClassification.progression),
	"Reimu C - Sealing Type":		TItemData("Characters", STARTING_ID + 102, ItemClassification.progression),
	"Marisa A - High-Power Type":	TItemData("Characters", STARTING_ID + 103, ItemClassification.progression),
	"Marisa B - Piercing Type":		TItemData("Characters", STARTING_ID + 104, ItemClassification.progression),
	"Marisa C - Magic-User Type":	TItemData("Characters", STARTING_ID + 105, ItemClassification.progression),

	# Stages
	"Next Stage":					TItemData("[Progressive][Global] Stages", STARTING_ID + 200, ItemClassification.progression, 6),
	"[Reimu] Next Stage":			TItemData("[Progressive][Character] Stages", STARTING_ID + 201, ItemClassification.progression, 6),
	"[Marisa] Next Stage":			TItemData("[Progressive][Character] Stages", STARTING_ID + 202, ItemClassification.progression, 6),
	"[Reimu A] Next Stage":			TItemData("[Progressive][Shot Type] Stages", STARTING_ID + 203, ItemClassification.progression, 6),
	"[Reimu B] Next Stage":			TItemData("[Progressive][Shot Type] Stages", STARTING_ID + 204, ItemClassification.progression, 6),
	"[Reimu C] Next Stage":			TItemData("[Progressive][Shot Type] Stages", STARTING_ID + 205, ItemClassification.progression, 6),
	"[Marisa A] Next Stage":		TItemData("[Progressive][Shot Type] Stages", STARTING_ID + 206, ItemClassification.progression, 6),
	"[Marisa B] Next Stage":		TItemData("[Progressive][Shot Type] Stages", STARTING_ID + 207, ItemClassification.progression, 6),
	"[Marisa C] Next Stage":		TItemData("[Progressive][Shot Type] Stages", STARTING_ID + 208, ItemClassification.progression, 6),
	"Extra Stage":					TItemData("[Global] Extra Stage", STARTING_ID + 209, ItemClassification.progression),
	"[Reimu] Extra Stage":			TItemData("[Character] Extra Stage", STARTING_ID + 210, ItemClassification.progression),
	"[Marisa] Extra Stage":			TItemData("[Character] Extra Stage", STARTING_ID + 211, ItemClassification.progression),
	"[Reimu A] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 212, ItemClassification.progression),
	"[Reimu B] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 213, ItemClassification.progression),
	"[Reimu C] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 214, ItemClassification.progression),
	"[Marisa A] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 215, ItemClassification.progression),
	"[Marisa B] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 216, ItemClassification.progression),
	"[Marisa C] Extra Stage":		TItemData("[Shot Type] Extra Stage", STARTING_ID + 217, ItemClassification.progression),
	"Stage 2":						TItemData("[Not Progressive][Global] Stages", STARTING_ID + 218, ItemClassification.progression),
	"Stage 3":						TItemData("[Not Progressive][Global] Stages", STARTING_ID + 219, ItemClassification.progression),
	"Stage 4":						TItemData("[Not Progressive][Global] Stages", STARTING_ID + 220, ItemClassification.progression),
	"Stage 5":						TItemData("[Not Progressive][Global] Stages", STARTING_ID + 221, ItemClassification.progression),
	"Stage 6":						TItemData("[Not Progressive][Global] Stages", STARTING_ID + 222, ItemClassification.progression),
	"[Reimu] Stage 2":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 223, ItemClassification.progression),
	"[Reimu] Stage 3":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 224, ItemClassification.progression),
	"[Reimu] Stage 4":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 225, ItemClassification.progression),
	"[Reimu] Stage 5":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 226, ItemClassification.progression),
	"[Reimu] Stage 6":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 227, ItemClassification.progression),
	"[Marisa] Stage 2":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 228, ItemClassification.progression),
	"[Marisa] Stage 3":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 229, ItemClassification.progression),
	"[Marisa] Stage 4":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 230, ItemClassification.progression),
	"[Marisa] Stage 5":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 231, ItemClassification.progression),
	"[Marisa] Stage 6":				TItemData("[Not Progressive][Character] Stages", STARTING_ID + 232, ItemClassification.progression),
	"[Reimu A] Stage 2":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 233, ItemClassification.progression),
	"[Reimu A] Stage 3":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 234, ItemClassification.progression),
	"[Reimu A] Stage 4":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 235, ItemClassification.progression),
	"[Reimu A] Stage 5":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 236, ItemClassification.progression),
	"[Reimu A] Stage 6":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 237, ItemClassification.progression),
	"[Reimu B] Stage 2":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 238, ItemClassification.progression),
	"[Reimu B] Stage 3":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 239, ItemClassification.progression),
	"[Reimu B] Stage 4":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 240, ItemClassification.progression),
	"[Reimu B] Stage 5":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 241, ItemClassification.progression),
	"[Reimu B] Stage 6":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 242, ItemClassification.progression),
	"[Reimu C] Stage 2":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 243, ItemClassification.progression),
	"[Reimu C] Stage 3":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 244, ItemClassification.progression),
	"[Reimu C] Stage 4":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 245, ItemClassification.progression),
	"[Reimu C] Stage 5":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 246, ItemClassification.progression),
	"[Reimu C] Stage 6":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 247, ItemClassification.progression),
	"[Marisa A] Stage 2":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 248, ItemClassification.progression),
	"[Marisa A] Stage 3":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 249, ItemClassification.progression),
	"[Marisa A] Stage 4":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 250, ItemClassification.progression),
	"[Marisa A] Stage 5":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 251, ItemClassification.progression),
	"[Marisa A] Stage 6":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 252, ItemClassification.progression),
	"[Marisa B] Stage 2":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 253, ItemClassification.progression),
	"[Marisa B] Stage 3":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 254, ItemClassification.progression),
	"[Marisa B] Stage 4":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 255, ItemClassification.progression),
	"[Marisa B] Stage 5":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 256, ItemClassification.progression),
	"[Marisa B] Stage 6":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 257, ItemClassification.progression),
	"[Marisa C] Stage 2":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 258, ItemClassification.progression),
	"[Marisa C] Stage 3":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 259, ItemClassification.progression),
	"[Marisa C] Stage 4":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 260, ItemClassification.progression),
	"[Marisa C] Stage 5":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 261, ItemClassification.progression),
	"[Marisa C] Stage 6":			TItemData("[Not Progressive][Shot Type] Stages", STARTING_ID + 262, ItemClassification.progression),

	# Endings and Treasures
	"[Reimu] Ending - Kanako":			TItemData("Endings", STARTING_ID + 300, ItemClassification.progression),
	"[Marisa] Ending - Kanako":			TItemData("Endings", STARTING_ID + 301, ItemClassification.progression),
	"[Reimu] Ending - Suwako":			TItemData("Endings", STARTING_ID + 302, ItemClassification.progression),
	"[Marisa] Ending - Suwako":			TItemData("Endings", STARTING_ID + 303, ItemClassification.progression),

	# Junk
	"+0.05 Power Point":	TItemData("Filler", STARTING_ID + 400),

	# Trap
	"-50% Power Point":				TItemData("Traps", STARTING_ID + 500, ItemClassification.trap),
	"-1 Life":						TItemData("Traps", STARTING_ID + 501, ItemClassification.trap),
	"Reverse Movement":				TItemData("Traps", STARTING_ID + 502, ItemClassification.trap),
	"Aya Speed":					TItemData("Traps", STARTING_ID + 503, ItemClassification.trap),
	"Freeze":						TItemData("Traps", STARTING_ID + 504, ItemClassification.trap),
	"Power Point Drain":			TItemData("Traps", STARTING_ID + 505, ItemClassification.trap),
}

item_groups: Dict[str, str] = {
	"Reimu A": ["Reimu A - Homing Type"],
	"Reimu B": ["Reimu B - Forward Focus Type"],
	"Reimu C": ["Reimu C - Sealing Type"],
	"Marisa A": ["Marisa A - High-Power Type"],
	"Marisa B": ["Marisa B - Piercing Type"],
	"Marisa C": ["Marisa C - Magic-User Type"],
}