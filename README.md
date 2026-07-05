# Touhou 10 ~ Mountain of Faith Apworld

This is an implementation of touhou 10 for [Archipelago](https://github.com/ArchipelagoMW/Archipelago)<br />

## How does this randomizer work ?
At the start, you start with only one character and one shot type, with zero resources and with only the Lunatic difficulty.<br />
Each item will make it easier and easier to clear the differents stages.

## Locations
* MidBoss Defeated
* Boss Defeated
* Stage Cleared

## Items
* Characters/Shot Types
* Stages (Practice Mode)
* Extra Stage (If enabled)
* Pack of 0.50 Power Points
* Lives
* Lower Difficulty

**Filler**: 0.05 Power Point

## Options
**Mode:** Practice or Normal mode.
In Practice mode, you play stage by stage individually and need to unlock the stages.<br />
In Normal mode, you need to finish the game normally with the resources only given at the start. Futhermore, only the resources act as a gate. If you put everything at minimum in the yaml, the logic consider you can finish at sphere 1.<br />

**Exclude Lunatic:** You can exclude the Lunatic difficulty and therefore, start with the Hard difficulty.

**Resources:** You can set the resources needed for the stages 3/4 and stages 5/6.

**Extra Stage:** You can enable the extra stage and choose if it act as the 7th stage or if it is unlocked separately. In normal mode, it is unlocked after clearing the stage 6 if it's not it's own unlock.

**Goal:** If the extra stage is enabled, you can choose which goal you want between Kanako, Suwako or both.

**Endings Required:** If you must clear your goal with just one character, both of them or with all shot types if they are enabled as separate check.

**Shot Type:** If checks are separated by shot type.

**Difficulty:** If checks are separated by difficulty. If Lunatic is excluded, no check will be behind it. An option also allow to complete easier (and unlocked) difficulty when doing an harder one.

**Traps:** You can choose to have traps replacing a percentages of filler items. You can set the weight of each individual trap.

**Death Link:** [Not Implemented] You can choose to activate Death Link.

**Ring Link:** You can choose to activate Ring Link, synchronizing your gain and loss of Power Points.

## How to use

**Backup your score.dat if you care about your scores, practice stage access and Extra unlock**

1. Launch the game
2. Launch the client "Touhou MoF" found in the Archipelago launcher
3. Connect the client to the server.
4. If the message "Touhou MoF process found. Starting loop..." appeared, you're good to go
