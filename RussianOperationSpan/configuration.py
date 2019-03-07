# -*- coding: utf-8 -*-

# WHICH FONT SHOULD BE USED?
fontname = "Helvetica"

# AND AT WHICH SIZE?
fontsize = 24

## FILE WITH ITEMS FOR THE PROCESSING COMPONENT. EACH LINE MUST CONTAIN A PROCESSING ITEM (SENTENCE OR OPERATION) AND THE PROPER RESPNSE (y OR n), SEPERATED BY A TAB.
processing_items_file = "operations.txt"

# FILE WITH ITEMS FOR THE RECALL COMPONENT. EACH LINE HOLDS ONE ITEM
target_items_file = "consonants.txt"

# KEY MAPPING. CHARACTER AFTER COLOM INDICATES, WHICH KEY TO MAP TO THE RESPECTIVE RESPONSE.
responses = {
	'y':'0',
	'n':'1'
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

welcome_text = """Здравствуйте!

Этот эксперимент займёт у вас около 15 минут.

Нажмите пробел, чтобы продолжить."""

# TEXT SHOWN AT THE BEGINNING OF THE TEST:
instructions1 = """

В этом тесте мы попросим вас делать два задания: проверять,
 верны ли математические уравнения, и запоминать буквы, 
которые возникают на экране после каждого уравнения. 
Прочитайте уравнение вслух сразу же, как только увидите его. 
Нажмите "1", если уравнение верно, и "0", если оно неверно.

После уравнения вы увидите на экране букву. Прочитайте ее вслух и запомните. После нескольких циклов "уравнение + буква" на экране появится знак вопроса. Тогда вам нужно будет напечатать все буквы в том порядке, в котором вы их прочитали, например, "к ф м б".

В начале вы сделаете несколько пробных заданий, чтобы привыкнуть к процедуре эксперимента. Во время тренировки вы узнаете, правильные ли ответы вы даете. Во время эксперимента вы не узнаете, правильно ли вы отвечаете. Пожалуйста, постарайтесь выполнять задание максимально быстро и правильно. Вы можете сделать перерыв, когда на экране появится сообщение о перерыве.

Пожалуйста, расположите ваши пальцы на клавишах 1 и 0, а потом нажмите на пробел, чтобы перейти к тренировке, пока что только с уравнениями."""

## TEXT SHOWN AFTER THE PROCESSING TRIALS AND BEFORE PRACTICE TRIALS.
## THIS SECOND PHASE OF THE OVERALL TEST IS SUPPOSED TO MAKE PARTICIPANTS FAMILIAR WITH THE MEMORY TASK.
instructions2 = """Во второй части тренировки вы увидите по букве после каждого уравнения. Ваша задача -- запоминать эти буквы, пока вы не увидите знак вопроса. Тогда запишите их в том порядке, в котором вы их видели, например, 'к ф м б'. Отделяйте буквы при записи с помощью пробела, и нажмите Enter, когда введете все буквы. 

Пожалуйста, проверьте, что вы напечатали те буквы, которые хотели, прежде чем нажимать на Enter. Вы можете отредактировать свой ответ.

Пожалуйста, расположите ваши пальцы на клавишах 1 и 0, а потом нажмите на пробел, чтобы перейти ко второй тренировке."""

## THESE INSTRUCTIONS APPEAR AFTER THE FAMILIARIZATION PERIOD AND PREPARES PARTICIPANTS FOR THE ACTUAL TEST:
instructions3 = """Надеемся, что сейчас вам уже понятна процедура эксперимента. Если у вас нет никаких вопросов, мы начинаем настоящее тестирование. Если вы не уверены, что знаете, что нужно делать, попросите экспериментатора о помощи.

Постарайтесь отвечать как можно быстрее и правильнее! Каждое задание ограничено во времени, и вам нужно отвечать быстро.

Пожалуйста, расположите ваши пальцы на клавишах 1 и 0, а потом нажмите на пробел, чтобы перейти к эксперименту."""

## TEXT SHOWN AFTER CORRECT AND INCORRECT RESPONSES DURING PROCESSING TRIALS AND TEXT FOR SUMMARIZING FEEDBACK
practice_correct_response = "Очень хорошо!"
practice_incorrect_response = "Ой! В следующий раз получится лучше."
practice_summary = """Вы ответили правильно на %(correct)s из %(total)s проб.

Нажмите пробел, чтобы продолжить."""

# TEXT BETWEEN OPERATIONS
next_message = """Пожалуйста, расположите ваши пальцы на клавишах 1 и 0, а потом нажмите на пробел."""

# MESSAGE SHOWN WHEN A PARTICIPANT TAKES TOO MUCH TIME:
time_out_message = "Слишком долго!"

## FINAL MESSAGE
finished_message = """Готово!

Пожалуйста, нажмите на пробел."""

## TEXT SHOWN AFTER THE LAST RUN:
good_bye_text = """Спасибо за участие!"""
