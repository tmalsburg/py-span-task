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
	'y':'j',
	'n':'f'
}

# NUMBER OF ITEMS FOR PROCESSING TRIALS. DON'T SET THIS NUMBER TOO LOW! 15
practice_processing_items = 12

# NUMBER OF ITEMS FOR PRACTIVE TRIALS. THESE CAN BE FEW. 3,4
practice_levels = (2,3)
practice_items_per_level = 1

# MEMORY LEVELS IN ACTUAL TEST, ORDER DOESN'T MATTER 2,3,4,5,6,7
levels = (3,4,5,6,7)

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
## If pseudo_random_targets is set to True, the list of recall items will be
## shuffled, iterated over, and re-shuffled once the last element of the list
## has been presented.  If set to False, random items will be selected from the
## list in every trial
pseudo_random_targets = True
allow_sloppy_spelling = False
heed_order=True

###############
## TEXT BITS ##
###############

welcome_text = """Herzlich Willkommen!

Der folgende Test dauert insgesamt etwa 15 Minuten.


Drücken Sie die Leertaste, sobald Sie bereit sind."""

# TEXT SHOWN AT THE BEGINNING OF THE TEST:
instructions1 = """Im folgenden Test sollen Sie zwei Dinge tun: die Richtigkeit von arithmetischen Rechnungen bewerten und sich Buchstaben einprägen, die nach jeder Rechnung erscheint.

Lesen Sie jede Rechnung sofort laut vor, wenn sie auf dem Bildschirm erscheint. Drücken Sie die J-Taste, wenn Sie das Ergebnis als korrekt bewerten und die F-Taste, falls Sie das Ergebnis für falsch halten.

Nach jeder Rechnung erscheint ein Buchstabe, den Sie sich einprägen sollen. Sie sollen den Buchstaben nun laut vorlesen und sich einprägen. Nach einer variierenden Anzahl von Rechnungen erscheint ein Fragezeichen auf dem Bildschirm und Sie müssen die seit der letzten Eingabe gesehenen Buchstaben in der richtigen Reihenfolge aufschreiben.

Sie üben zunächst nur die Beurteilung der Rechnungen und erhalten nach jeder Rechnung eine Rückmeldung darüber, ob Sie richtig oder falsch geantwortet haben.  Das wird während des eigentlichen Tests nicht mehr geschehen. Arbeiten Sie so schnell wie möglich und versuchen Sie dennoch, jede Rechnung richtig zu bewerten.  Machen Sie während der Übung keine Pausen!


Legen Sie Ihre Finger auf F- und J-Taste und drücken Sie die Leertaste, um mit der Übung zu beginnen."""


## TEXT SHOWN AFTER THE PROCESSING TRIALS AND BEFORE PRACTICE TRIALS.
## THIS SECOND PHASE OF THE OVERALL TEST IS SUPPOSED TO MAKE PARTICIPANTS FAMILIAR WITH THE MEMORY TASK.
instructions2 = """Im zweiten Teil der Übung wird nach jeder Ihrer Bewertungen zusätzlich kurz ein Buchstaben eingeblendet. Ihre Aufgabe ist es, sich diese Buchstaben zu merken, bis Sie nach einigen Rechnungen dazu aufgefordert werden, sie in der richtigen Reihenfolge einzugeben.

Trennen Sie die Buchstaben mit Leerzeichen und drücken Sie "Enter", wenn Sie fertig sind. Bitte vermeiden Sie Tippfehler und nehmen Sie eine Korrektur vor, falls Ihnen doch ein Fehler unterlaufen ist. Auf Groß- und Kleinschreibung müssen Sie nicht achten.


Legen Sie Ihre Finger auf F- und J-Taste und drücken Sie die Leertaste, um fortzufahren."""

## THESE INSTRUCTIONS APPEAR AFTER THE FAMILIARIZATION PERIOD AND PREPARES PARTICIPANTS FOR THE ACTUAL TEST:
instructions3 = """Sie sollten jetzt eine Vorstellung davon haben, was von Ihnen erwartet wird. Wenn Sie keine Fragen mehr haben, beginnen wir nun mit dem eigentlichen Test.

Geben Sie jede Bewertung so schnell wie möglich ab! Nach einer bestimmten Zeit wird die Rechnung abgebrochen.


Legen Sie nun Ihre Finger auf F- und J-Taste und drücken Sie die Leertaste, um fortzufahren."""

## TEXT SHOWN AFTER CORRECT AND INCORRECT RESPONSES DURING PROCESSING TRIALS AND TEXT FOR SUMMARIZING FEEDBACK
practice_correct_response = "Sehr gut!"
practice_incorrect_response = "Leider falsch!"
practice_summary = """Von %(total)s Rechnungen haben Sie %(correct)s korrekt bewertet.


Drücken Sie die Leertaste, um fortzufahren."""

# TEXT BETWEEN OPERATIONS
next_message = """Legen Sie Ihre Finger auf F- und J-Taste und drücken Sie die Leertaste, um fortzufahren."""

# MESSAGE SHOWN WHEN A PARTICIPANT TAKES TOO MUCH TIME:
time_out_message = "Zeit abgelaufen!"

## FINAL MESSAGE
finished_message = """Fertig!


Drücken Sie die Leertaste, um fortzufahren."""

## TEXT SHOWN AFTER THE LAST RUN:
good_bye_text = """Vielen Dank für die Teilnahme!"""
