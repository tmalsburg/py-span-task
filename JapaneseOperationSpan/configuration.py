# -*- coding: utf-8 -*-

fontsize = 20
fontname = "Arial"

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
target_items_file = "consonants.txt"

# Possible responses and their respective keys:
# In front of the colon is the response as indicated in the file with the
# verification items (a.k.a. processing_items_file).  After the colon you can
# specify the key on the keyboard that the participant is supposed to use to
# indicate the respective answer.

responses = {
  'y':'1',
  'n':'0'
}

welcome_text = """
ようこそ！

このテストでは２つのことを同時にやっていただきます。

（１）数式が正しいかどうかを判断
（２）アルファベットの文字を記憶

（次に進むにはスペースバーを押してください）"""

# Text shown at the beginning of the test:
instructions1 = """
最初に「数式」の練習をやってもらいます。

出てきた数式を【声を出して音読】し，
正しい場合は1，間違っている場合は0をタイプしてください。

たとえば，「( 1 + 2 ) x 3 = 4」なら
「いち たす に かける さん は よん」というように音読し，
この計算は間違っていますから，0をタイプしてください。

この練習では，あなたの回答が正しいかどうか，
フィードバックが示されます。
このフィードバックは，本番では出てきません。

できるだけ素早く，かつ正しく問題をこなしてください。
途中で休憩は取らないでください。

指を1と0のキーに置き，スペースバーを押して練習問題を始めてください。
""".strip()

# Whether or not minor typos are corrected for when people enter the recalled
# items.  If set to True the entered item is counted as correct if there's at
# most one of the following types of typos: omission of a character, addition of
# a character, substitution of a character, two adjacent characters are
# swapped. NOTE: don't use this if your target items are very short, e.g.
# single digits, because by substitution every digit can be turned into the
# correct one.
allow_sloppy_spelling = False

# Number of processing items for practice:
# Don't set this number too low.  The reaction times are measures during these
# practice trials and the mean + 2.5 * SD is used for the time-out during the
# actual test.
practice_processing_items = 25

# In the practice phase it is measured how much time people need to solve the
# distractor task.  This time plus two standard deviations is later in the main
# test used as a time-out.  In the first practice trials people often take much
# longer than later because of initial confusion.  Therefore, it's advisable to
# measure processing time only after a few practice trials.  This variable
# controls when the measurements start.
measure_time_after_trial = 10

# This specifies whether or not the order of target items should be obeyed when
# people enter the items in the recall phase.
heed_order = True

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
pseudo_random_targets = False

# Number of combined items (processing + memory) for practice:
# These can be few.  It's just meant to give people a feeling for the time-out
# and to give them a chance to ask question before the actual tests starts.
practice_levels = (2,3)
practice_items_per_level = 2
practice_correct_response = "ご名答！"
practice_incorrect_response = "残念！"
practice_summary = """%(total)s 回で，%(correct)s 回正解しました. 


（続けるにはスペースバーを押してください）"""


# Text shown after the practice items and introduces the task /with/ target
# items.  This second phase of the overall test is supposed to make
# participants familiar with the memory task.
instructions2 = """
次に「計算」に「文字暗記」を組み合わせた練習をやってみましょう。

今回はそれぞれの計算問題のあとにアルファベットの文字が出てきます。

これらの文字を【音読したうえで，暗記】して，
？マークが出たら，【覚えた文字を正しい順番で】タイプしてください。
一部を忘れたばあいは覚えているものだけでもタイプしてください。

大文字小文字は関係ありませんので小文字で答えてもらってけっこうです。

タイプし終わったらEnterキーを押してください。

指を1と0のキーに置き，スペースバーを押して問題を始めてください。
""".strip()

# These instructions appear after the familiarization period and prepares
# participants for the main test:
instructions3 = """
さあ，これで要領はだいたいわかったかと思います。

もし質問があれば，今実験担当者にしてください。
もし良ければ，本番のテストを始めてください。

なるべく素早く，正確にタスクをこなしてください。
十数回繰り返したあとテストは自動的に終了します。

指を1と0のキーに置き，スペースバーを押して問題を始めてください。
""".strip()

# The levels of memory load that are tested.  Each number tells the load.
# Order doesn't matter.
levels = (3,4,5,6)
items_per_level = 3
next_message = """（指を1と0のキーに置き，スペースバーを押して問題を始めてください）""".strip()

finished_message = """
スペースバーを押してください"""

# Time-out factor:
# The factor multiplied with the sd plus mean rt of the practice trials is the
# time-out, i.e. the time after which the presentation of the processing item
# is interrupted and the response is counted as wrong.
time_out_factor = 2.5
# Message shown when a participant takes too much time:
time_out_message = "時間切れです！"

# How long will the target items be displayed:
target_display_time = 800 #as in UnswortHeitzSchrockEngle2005
# How long will the response (correct or wrong) be displayed during the
# practice trials:
response_display_time = 1000

# Text shown after the last run:
good_bye_text = """
おつかれさまでした。
これでテストは終わりです！"""

