# -*- coding: utf-8 -*-

fontsize = 22
fontname = "Helvetica"

# File with the items from the processing task.  Sentences in case of reading
# span or equations in the case of operation span.  In this file theres one
# item per line.  The first half of a line shows the item, then there's a
# delimiting tab, and finally there's the correct answer for the verification
# task: y or n.  Examples:
#      The queen of England is smoking secretly.    y
#      (1*2)+1 = 3  y
# Take care that your editor stores tabs as real tabs and does not expand them
# to ordinary spaces.
processing_items_file = "operations.txt"

# The items that participants have to memorize.  In this file there's one item
# per line.  Items can be letters, digits or sentences -- any string is ok.
target_items_file = "target_words_spanish.txt"

# Possible responses and their respective keys:
# In front of the colon is the response as indicated in the file with the
# verification items (a.k.a. processing_items_file).  After the colon you can
# specify the key on the keyboard that the participant is supposed to use to
# indicate the respective answer.

responses = {
  'y':'j',
  'n':'f'
}

welcome_text = """¡Bienvenido!

La duración del test será de 20 minutos.

Presione la barra espaciadora cuando esté preparado para comenzar el test."""

# Text shown at the beginning of the test:
instructions1 = """
En este test, debe indicar si el resultado de las siguientes operaciones matemáticas es correcto.  Entre las operaciones, aparecerán palabras que debe recordar. 

Sin embargo, en esta primera práctica, únicamente debe juzgar el resultado de las operaciones matemáticas. En primer lugar, lea en voz alta la operación y después compruebe si el resultado es correcto. Presione la tecla "j" si cree que el resultado de la operación es correcto. Si, por el contrario, cree que el resultado es incorrecto, presione la tecla "f".

Después de cada respuesta, se le informará si ha respondido correctamente. Esta información únicamente aparecerá durante los ejercicios de práctica, pero no durante el test principal.

Responda con precisión, pero tan rápido como sea posible.  No realice ningún descanso y no se distraiga.

Si tiene alguna otra pregunta, por favor realícela en este momento.

Cuando esté preparado, sitúe los dedos índice sobre las teclas marcadas y utilice el dedo pulgar para presionar la barra espaciadora y comenzar la práctica.
""".strip()

# Whether or not minor typos are corrected for when people enter the recalled
# items.  If set to True the entered item is counted as correct if there's at
# most one of the following types of typos: omission of a caracter, addition of
# a character, substitution of a character, two adjacent characters are
# swapped. NOTE: don't use this if your target items are very short, e.g.
# single digits, because by substitution every digit can be turned into the
# correct one.
allow_sloppy_spelling = True

# Number of processing items for practice:
# Don't set this number too low.  The reaction times are measures during these
# practice trials and the mean + 2.5 * SD is used for the time-out during the
# actual test.
practice_processing_items = 8

# In the practice phase it is measured how much time people need to solve the
# distractor task.  This time plus two standard deviations is later in the main
# test used as a time-out.  In the first practice trials people often take much
# longer than later because of initial confusion.  Therefore, it's advisable to
# measure processing time only after a few practice trials.  This variable
# controls when the measurements start.
measure_time_after_trial = 2

# This specifies whether or not the order of target items should be obeyed when
# people enter the items in the recall phase.
heed_order = False

# This controls the order in which target items are presented.  Either the list
# of items is shuffled and then each element is presented one after the other.
# When the list is finished it is shuffled again and the process starts all
# over.  Set pseudo_random_targets to True to get this behavior.  In the
# alternative mode a target item it drawn randomly from the set of all items.
# The crucial difference is that an item can appear in two consecutive trials
# then.  Set pseudo_random_targets to False to get the latter behavior.  If
# there are only few target items, say the digits from 0 to 9, then true random
# selection is preferable.  Otherwise, people can easily guess: if they saw
# 1,3,5,7,9 in the last trial, they can guess that in the next they will see
# 0,2,4,6,8.  If the number of target item is large, shuffled presentation is
# better, because it avoids repetitions.
pseudo_random_targets = True

# Number of combined items (processing + memory) for practice:
# These can be few.  It's just meant to give people a feeling for the time-out
# and to give them a chance to ask question before the actual tests starts.
practice_levels = (2,4)
practice_items_per_level = 2
practice_correct_response = "¡Muy bien!"
practice_incorrect_response = "¡Lo siento, incorrecto!"
practice_summary = """De %(total)s operaciones, ha obtenido %(correct)s
respuestas correctas.

Presione la barra espaciadora para continuar."""

# Text shown after the practice items and introduces the task /with/ target
# items.  This second phase of the overall test is supposed to make
# participants familiar with the memory task.
instructions2 = """
En la segunda parte, después de cada operación matemática, aparecerá una palabra que tiene que recordar.  Después de algunas operaciones, se le pedirá que teclee las palabras en cualquier orden y separadas por un espacio. Se pueden ignorar los acentos en las palabras cuando teclees la respuesta. Cuando haya terminado, presione la tecla enter. Una vez que haya tecleado las palabras, ya no tendrá que recordarlas.

¡Por favor, responda tan rápido como pueda!  Si tarda demasiado tiempo en responder, se le indicará en la pantalla.  Cuando teclee las palabras, puede tomarse el tiempo que sea necesario.

Cuando esté preparado, sitúe los dedos índice sobre las teclas marcadas y utilice el dedo pulgar para presionar la barra espaciadora y comenzar la práctica.
""".strip()

# These instructions appear after the familiarization period and prepares
# participants for the main test:
instructions3 = """
En este momento ya debe conocer el funcionamiento del test.  Si no tiene ninguna pregunta, puede comenzar con el test principal.

Cuando esté preparado, sitúe los dedos índice sobre las teclas marcadas y presione la barra espaciadora con el dedo pulgar para continuar.
""".strip()

# The levels of memory load that are tested.  Each number tells the load.
# Order doesn't matter.
levels = (2,3,4,5,6)
items_per_level = 5
next_message = """
Cuando esté preparado, sitúe los dedos índice sobre las teclas marcadas y presione la barra espaciadora con el dedo pulgar para continuar.
""".strip()
finished_message = """¡Bien hecho!

Presione la barra espaciadora para continuar."""

# Time-out factor:
# The factor multiplied with the sd plus mean rt of the practice trials is the
# time-out, i.e. the time after which the presentation of the processing item
# is interrupted and the response is counted as wrong.
time_out_factor = 2.5
# Message shown when a participant takes too much time:
time_out_message = "¡Demasiado lento!"

# How long will the target items be displayed:
target_display_time = 1000
# How long will the response (correct or wrong) be displayed during the
# practice trials:
response_display_time = 1000

# Text shown after the last run:
good_bye_text = """¡Gracias por su colaboración!"""

