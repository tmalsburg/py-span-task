# -*- coding: utf-8 -*-

# WHICH FONT SHOULD BE USED?
fontname = "Helvetica"

# AND AT WHICH SIZE?
fontsize = 22

## FILE WITH ITEMS FOR THE PROCESSING COMPONENT. EACH LINE MUST CONTAIN A PROCESSING
## ITEM (SENTENCE OR OPERATION) AND THE PROPER RESPNSE (y OR n), SEPERATED BY A TAB.
processing_items_file = "sentences_german.txt"

# FILE WITH ITEMS FOR THE RECALL COMPONENT. EACH LINE HOLDS ONE ITEM
target_items_file = "target_words_german.txt"

# KEY MAPPING. CHARACTER AFTER COLOM INDICATES, WHICH KEY TO MAP TO THE RESPECTIVE RESPONSE.
responses = {
  'y':'j',
  'n':'f'
}

# NUMBER OF ITEMS FOR CALIBRATION TRIALS. DON'T SET THIS NUMBER TOO LOW!
practice_processing_items = 15
measure_time_after_trial = 4

# NUMBER OF ITEMS FOR PRACTIVE TRIALS. THESE CAN BE FEW.
practice_levels = (3,4)
practice_items_per_level = 1

# TESTED MEMORY LEVELS, ORDER DOESN'T MATTER
levels = (3,7)

# NUMBER OF SETS PER SIZE. WE RECOMMEND 3.
items_per_level = 3

# TIME-OUT FACTOR: MEAN RT PLUS HOW MANY STANDARD DEVIATIONS?
time_out_factor = 2.5

# PRESENTATION DURATION TARGET ITEMS
target_display_time = 1000

# PRESENTATION DURATION ACCURACY FEEDBACK
response_display_time = 1000

## WHETHER OR NOT MINOR TYPOS ARE CORRECTED FOR WHEN PEOPLE ENTER THE RECALLED ITEMS. IF SET TO TRUE THE ENTERED ITEM IS COUNTED AS CORRECT IF THERE'S AT  MOST ONE OF THE FOLLOWING TYPES OF TYPOS: OMISSION OF A CARACTER, ADDITION OF A CHARACTER, SUBSTITUTION OF A CHARACTER, TWO ADJACENT CHARACTERS ARE SWAPPED.
## NOTE: DON'T USE THIS IF YOUR TARGET ITEMS ARE VERY SHORT, E.G. SINGLE DIGITS, BECAUSE BY SUBSTITUTION EVERY DIGIT CAN BE TURNED INTO THE CORRECT ONE.
allow_sloppy_spelling = True
heed_order=True
pseudo_random_targets = True

###############
## TEXT BITS ##
###############

welcome_text = """Herzlich Willkommen!

Der folgende Test dauert insgesamt etwa 15 Minuten.


Drücken Sie die Leertaste, sobald Sie bereit sind."""

# TEXT SHOWN AT THE BEGINNING OF THE TEST:
instructions1 = """Im folgenden Test sollen Sie bewerten, ob Sätze einen Sinn ergeben
und sich Wörter einprägen, die zwischen den Sätzen erscheinen.

Lesen Sie jeden Satz laut vor und beginnen Sie damit sofort,
wenn er auf dem Bildschirm erscheint. Drücken Sie die J-Taste,
wenn Sie den Satz für sinnvoll halten und die F-Taste,
falls Sie das nicht tun."""

instructions2 = """Sie üben zunächst die Beurteilung der Sätze und erhalten eine
Rückmeldung darüber, ob Sie richtig oder falsch geantwortet haben.
Das wird während des eigentlichen Tests nicht mehr geschehen.

Arbeiten Sie bitte genau und zügig und machen Sie keine Pausen!
Falls Sie noch Fragen haben, stellen Sie sie bitte jetzt.


Bitte legen Sie nun Ihre Finger auf F- und J-Taste
und drücken Sie die Leertaste, um mit der Übung zu beginnen."""

## TEXT SHOWN AFTER THE PROCESSING TRIALS AND BEFORE PRACTICE TRIALS.
## THIS SECOND PHASE OF THE OVERALL TEST IS SUPPOSED TO MAKE PARTICIPANTS FAMILIAR WITH THE MEMORY TASK.
instructions3 = """Im zweiten Teil der Übung wird nach jeder Ihrer Bewertungen zusätzlich
kurz ein Wort eingeblendet. Ihre Aufgabe ist es, sich diese Wörter
zu merken, bis Sie nach einigen Sätzen dazu aufgefordert werden,
sie einzugeben.

Trennen Sie die Wörter mit Leerzeichen und drücken Sie "Enter",
wenn Sie fertig sind. Bitte vermeiden Sie Tippfehler und nehmen
Sie eine Korrektur vor, falls Ihnen doch ein Fehler unterlaufen ist.
Groß- und Kleinschreibung ist nicht wichtig.


Legen Sie Ihre Finger auf F- und J-Taste
und drücken Sie die Leertaste, um fortzufahren."""

## THESE INSTRUCTIONS APPEAR AFTER THE FAMILIARIZATION PERIOD AND PREPARES PARTICIPANTS FOR THE ACTUAL TEST:
instructions4 = """Sie sollten jetzt eine Vorstellung davon haben,
was von Ihnen erwartet wird. Wenn Sie keine Fragen mehr haben,
beginnen wir nun mit dem eigentlichen Test.

Geben Sie die Bewertung so schnell wie möglich ab!
Nach einer bestimmten Zeit wird die Rechnung abgebrochen.


Legen Sie nun Ihre Finger auf F- und J-Taste
und drücken Sie die Leertaste, um fortzufahren."""

## TEXT SHOWN AFTER CORRECT AND INCORRECT RESPONSES DURING PROCESSING TRIALS AND TEXT FOR SUMMARIZING FEEDBACK
practice_correct_response = "Sehr gut!"
practice_incorrect_response = "Leider falsch!"
practice_summary = """Von %(total)s Rechnungen haben Sie %(correct)s korrekt bewertet.

Drücken Sie die Leertaste, um fortzufahren."""

# TEXT BETWEEN OPERATIONS
next_message = """Legen Sie Ihre Finger auf F- und J-Taste
und drücken Sie die Leertaste, um fortzufahren."""
target_request = """Geben Sie die Wörter ein, an die Sie sich erinnern."""

# MESSAGE SHOWN WHEN A PARTICIPANT TAKES TOO MUCH TIME:
time_out_message = "Zeit abgelaufen!"

## FINAL MESSAGE
finished_message = """Fertig!

Drücken Sie die Leertaste, um fortzufahren."""

## TEXT SHOWN AFTER THE LAST RUN:
good_bye_text = """Vielen Dank für die Teilnahme!"""
