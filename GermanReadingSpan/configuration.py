# -*- coding: utf-8 -*-

# Which font should be used?
fontname                  = "Helvetica"

# AND AT WHICH SIZE?
fontsize                  = 22

## File with items for the processing component.  Each line must
## contain a processing item (sentence or operation) and the proper
## response (y or n), separated by a tab.
processing_items_file     = "sentences_german.txt"

# File with items for the recall component.  Each line holds one item.
target_items_file         = "target_words_german.txt"

# Key mapping.  Character after colon indicates, which key to map to
# the respective response.
responses = {
  'y': 'j',
  'n': 'f'
}

# Number of items for calibration trials.  Don't set this number too
# low.
practice_processing_items = 12
measure_time_after_trial  = 4

# Number of items for practice trials.
practice_levels           = (3, 4)
practice_items_per_level  = 1

# Tested memory levels.  Order doesn't matter.
levels                    = (3, 7)

# Number of sets per size.
items_per_level           = 3

# Time-out factor: Mean reaction time plus x standard deviations.
time_out_factor           = 2.5

# Presentation duration of target items.
target_display_time       = 1000

# Presentation duration of accuracy feedback.
response_display_time     = 1000

# Whether or not minor typos are tolerated when participants enter the
# recalled items.  If `True`, the entered item is counted as correct
# if there's at most one of the following types of typos: omission of
# a character, addition of a character, substitution of a character,
# two adjacent characters swapped.

# Note: Don't set this to `True` if your target items are very short,
# e.g., single digits, because by substitution every digit can be
# turned into the correct one.
allow_sloppy_spelling     = True

# Whether participants need to enter target items in the order in
# which they were presented.
heed_order                = True

# Whether the order of target items should be pseudo random order or
# truly random.  Pseudo random means that we see each item once before
# they start repeating.  Truly random means that items are sampled
# randomly for each trial.
pseudo_random_targets     = True

########################################
## Instructions shown to participants: #
########################################

welcome_text = """Herzlich Willkommen!

Der folgende Test dauert insgesamt etwa 15 Minuten.


Drücken Sie die Leertaste, sobald Sie bereit sind."""

# Text shown at the beginning of the test.  Describes overall
# structure of the test and provides instructions for the first phase
# in which just the processing task is practiced (and time is
# measured):

instructions1 = """Im folgenden Test sollen Sie bewerten, ob Sätze einen Sinn ergeben und sich Wörter merken, die zwischen den Sätzen angezeigt werden.

Lesen Sie jeden Satz laut vor und beginnen Sie damit sofort, wenn er auf dem Bildschirm erscheint. Drücken Sie die J-Taste, wenn Sie den Satz für sinnvoll halten und die F-Taste, falls nicht.

Sie üben zunächst die Beurteilung der Sätze und erhalten eine Rückmeldung darüber, ob Sie richtig oder falsch geantwortet haben.  Das wird während des eigentlichen Tests nicht mehr geschehen.

Arbeiten Sie bitte genau und zügig und machen Sie keine Pausen!  Falls Sie noch Fragen haben, stellen Sie sie bitte jetzt.

Bitte legen Sie nun Ihre Finger auf F- und J-Taste und drücken Sie die Leertaste, um mit der Übung zu beginnen."""

# Instructions shown after the processing trials and before practice
# trials for the full task.  This second phase is supposed to
# familiarize participants with the complete task and specifically the
# memory component.

instructions2 = """Im zweiten Teil der Übung wird nach jeder Ihrer Bewertungen zusätzlich kurz ein Wort eingeblendet. Ihre Aufgabe ist es, sich diese Wörter zu merken, bis Sie nach einigen Sätzen dazu aufgefordert werden, sie in der richtigen Reihenfolge einzugeben.

Trennen Sie die Wörter mit Leerzeichen und drücken Sie "Enter", wenn Sie fertig sind. Bitte vermeiden Sie Tippfehler und nehmen Sie eine Korrektur vor, falls Ihnen doch ein Fehler unterlaufen ist. Auf Groß- und Kleinschreibung müssen Sie nicht achten.

Legen Sie Ihre Finger auf F- und J-Taste und drücken Sie die Leertaste, um fortzufahren."""

# These instructions appear after the practice period and
# prepares participants for the actual test:

instructions3 = """Sie sollten jetzt eine Vorstellung davon haben, was von Ihnen erwartet wird. Wenn Sie keine Fragen mehr haben, beginnen wir nun mit dem eigentlichen Test.

Geben Sie die Bewertung so schnell wie möglich ab!  Sie haben nur eine begrenzte Zeit dafür zur Verfügung.


Legen Sie nun Ihre Finger auf F- und J-Taste und drücken Sie die Leertaste, um fortzufahren."""

# Text shown after correct and incorrect responses during processing
# trials and text for summarizing feedback.

practice_correct_response = "Sehr gut!"

practice_incorrect_response = "Leider falsch!"

practice_summary = """Von %(total)s Versuchen haben Sie %(correct)s korrekt bewertet.

Drücken Sie die Leertaste, um fortzufahren."""

# Text between operations.
next_message = """Legen Sie Ihre Finger auf F- und J-Taste
und drücken Sie die Leertaste, um fortzufahren."""

target_request = """Geben Sie die Wörter ein, an die Sie sich erinnern."""

# Message shown when a participant takes too much time:
time_out_message = "Zeit abgelaufen!"

# Message shown when the main test is completed.
finished_message = """Fertig!

Drücken Sie die Leertaste, um fortzufahren."""

# Final message:
good_bye_text = """Vielen Dank für die Teilnahme!"""
