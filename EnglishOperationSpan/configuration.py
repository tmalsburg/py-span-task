# -*- coding: utf-8 -*-

# WHICH FONT SHOULD BE USED?
fontname = "Helvetica"

# AND AT WHICH SIZE?
fontsize = 28

## FILE WITH ITEMS FOR THE PROCESSING COMPONENT. EACH LINE MUST CONTAIN A PROCESSING ITEM (SENTENCE OR OPERATION) AND THE PROPER RESPNSE (y OR n), SEPERATED BY A TAB.
processing_items_file = "operations.txt"

# FILE WITH ITEMS FOR THE RECALL COMPONENT. EACH LINE HOLDS ONE ITEM
target_items_file = "consonants.txt"

# KEY MAPPING. CHARACTER AFTER COLOM INDICATES, WHICH KEY TO MAP TO THE RESPECTIVE RESPONSE.
responses = {
	'y':'c',
	'n':'i'
}

# NUMBER OF ITEMS FOR PROCESSING TRIALS. DON'T SET THIS NUMBER TOO LOW! 15
practice_processing_items = 12

# NUMBER OF ITEMS FOR PRACTIVE TRIALS. THESE CAN BE FEW. 3,4
practice_levels = (2,3)
practice_items_per_level = 2

# MEMORY LEVELS IN ACTUAL TEST, ORDER DOESN'T MATTER 2,3,4,5,6,7
levels = (2,3,4,5)

# NUMBER OF SETS PER SIZE. WE RECOMMEND 3.
items_per_level = 3

# TIME-OUT FACTOR: MEAN RT PLUS HOW MANY STANDARD DEVIATIONS?
time_out_factor = 2.5

# HOW MANY CALIBRATION TRIALS SHOULD BE EXCLUDED FROM TIME-OUT CALCULATION?
measure_time_after_trial = 2

# PRESENTATION DURATION TARGET ITEMS
target_display_time = 1000

# PRESENTATION DURATION ACCURACY FEEDBACK
response_display_time = 1000

## Whether or not minor typos are corrected for when people enter the recalled
## items.  If set to true the entered item is counted as correct if there's at
## most one of the following types of typos: omission of a caracter, addition of
## a character, substitution of a character, two adjacent characters are
## swapped.
## Note: Don't use this if your target items are very short, e.g. single digits,
## because by substitution every digit can be turned into the correct one.
allow_sloppy_spelling = False
## If pseudo_random_targets is set to True, the list of recall items will be
## shuffled, iterated over, and re-shuffled once the last element of the list
## has been presented.  If set to False, random items will be selected from the
## list in every trial
pseudo_random_targets = True
heed_order=True

###############
## TEXT BITS ##
###############

welcome_text = """Welcome!

This experiment will take about 15 minutes.

Press the space bar to continue."""

# TEXT SHOWN AT THE BEGINNING OF THE TEST:
instructions1 = """

In the following task you will need to do two things: check the validity of math equations and memorize the letters that appear after each item.
Read each math fact aloud as soon as you can. Press the C key if the equation is correct, or press the I key if the equation is incorrect.

After each equation a letter that we want you to memorize will appear. Please read the letter aloud and memorize it . After a certain number of items, a question mark will appear on the screen. At that point you will need to type in the list of letters in the order that you read them. For example 'h w k j'.

Before the experiment starts, you will be doing some practice problems. During the practice problems, you will be told if you answered accurately or not. In the real experiment, there will be no feedback. Please work as quickly and as accurately as possible. Please only take breaks when directed to do so.

Please place your fingers on the C and I keys and then press the space bar to continue to the math equation practice section."""

## TEXT SHOWN AFTER THE PROCESSING TRIALS AND BEFORE PRACTICE TRIALS.
## THIS SECOND PHASE OF THE OVERALL TEST IS SUPPOSED TO MAKE PARTICIPANTS FAMILIAR WITH THE MEMORY TASK.
instructions2 = """In the second part of this experiment you will now see a letter after each equation. Your task is to remember these letters until you are prompted with a question mark to enter them in the correct order.

Make sure to separate the characters with spaces ('h w k j'), and press "Enter" when you're done. 
Please make sure your answer is correct before hitting Enter. You can make corrections using the arrow keys. Feel free to use upper or lower case in your answers.

Place your fingers on C and I keys and press the spacebar to continue to the final practice round."""

## THESE INSTRUCTIONS APPEAR AFTER THE FAMILIARIZATION PERIOD AND PREPARES PARTICIPANTS FOR THE ACTUAL TEST:
instructions3 = """You should now understand the experiment. If you do not have any more questions, we will now start with the actual experiment. If are not sure what you are being asked to do, please stop now and ask the experimenter for help.

Make sure to respond as quickly and accurately as possible! There is a time limit for every item, so you will need to work fast.

Please place your fingers on the C and I keys and press the spacebar to continue to the final part of the experiment."""

## TEXT SHOWN AFTER CORRECT AND INCORRECT RESPONSES DURING PROCESSING TRIALS AND TEXT FOR SUMMARIZING FEEDBACK
practice_correct_response = "Very Good!"
practice_incorrect_response = "Oops! Better luck next time."
practice_summary = """Out of %(total)s problems, you answered %(correct)s correctly.

Please press the space bar to continue."""

# TEXT BETWEEN OPERATIONS
next_message = """Please place your fingers on the C and I keys and press the spacebar to continue."""

# MESSAGE SHOWN WHEN A PARTICIPANT TAKES TOO MUCH TIME:
time_out_message = "You are out of time!"

## FINAL MESSAGE
finished_message = """All done!

Please press the space bar to continue."""

## TEXT SHOWN AFTER THE LAST RUN:
good_bye_text = """Thanks so much for participating!"""
