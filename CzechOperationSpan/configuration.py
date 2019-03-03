# -*- coding: utf-8 -*-

# WHICH FONT SHOULD BE USED?
fontname = "Helvetica"

# AND AT WHICH SIZE?
fontsize = 20

## FILE WITH ITEMS FOR THE PROCESSING COMPONENT. EACH LINE MUST CONTAIN A PROCESSING ITEM (SENTENCE OR OPERATION) AND THE PROPER RESPNSE (y OR n), SEPERATED BY A TAB.
processing_items_file = "operations.txt"

# FILE WITH ITEMS FOR THE RECALL COMPONENT. EACH LINE HOLDS ONE ITEM
target_items_file = "consonants.txt"

# KEY MAPPING. CHARACTER AFTER COLOM INDICATES, WHICH KEY TO MAP TO THE RESPECTIVE RESPONSE.
responses = {
	'y':'a',
	'n':'n'
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

welcome_text = """Vítejte v testu pracovní paměti!

Tento test bude trvat asi 15 minut.

Pro pokračování stiskněte mezerník."""

# TEXT SHOWN AT THE BEGINNING OF THE TEST:
instructions1 = """

V následující úloze budete mít za úkol dvě věci: ohodnotit správnost matematických rovnic a zapamatovat si písmena, která se mezi jednotlivými rovnicemi budou zobrazovat.

Předtím, než samotný test začne, si budete moci vše vyzkoušet. V této cvičné fázi se vám bude objevovat informace, zda jste rovnice ohodnotili správně, anebo ne. V samotném testu už tuto zpětnou vazbu dostávat nebudete. Postupujte svižně, bez otálení, ale vyvarujte se chyb. Případné pauzy dělejte pouze ve chvíli, kdy vám to úloha řekne.

Nyní položte ukazováček levé ruky na písmeno A a ukazováček pravé ruky na písmeno N a pro pokračování k první cvičné úloze stiskněte mezerník."""

## TEXT SHOWN AFTER THE PROCESSING TRIALS AND BEFORE PRACTICE TRIALS.
## THIS SECOND PHASE OF THE OVERALL TEST IS SUPPOSED TO MAKE PARTICIPANTS FAMILIAR WITH THE MEMORY TASK.
instructions2 = """Ve druhé cvičné části se vám po jednotlivých rovnicích budou objevovat určitá písmena. Vaším úkolem je si tato písmena zapamatovat do té doby, než se objeví otazník. Poté budete muset tato písmena napsat v tom pořadí, v jakém se objevila.

Jednotlivá písmena oddělujte mezerami (například h v k j). Až budete hotovi, stiskněte klávesu Enter. To, co napíšete, se Vám objeví v dolním řádku na obrazovce. 

Dejte pozor, abyste písmena uvedli správně. Před zmáčknutím klávesy Enter si svou odpověď zkontrolujte (například kvůli případným překlepům) a případně ji opravte. Je jedno, jestli budete při odpovědi používat velká, anebo malá písmena.

Nyní položte ukazováček levé ruky na písmeno A a ukazováček pravé ruky na písmeno N a pro pokračování k druhé cvičné úloze stiskněte mezerník."""

## THESE INSTRUCTIONS APPEAR AFTER THE FAMILIARIZATION PERIOD AND PREPARES PARTICIPANTS FOR THE ACTUAL TEST:
instructions3 = """Toto je konec cvičení. Nyní už máte představu o tom, co je Vaším úkolem. Nemáte-li další otázky, můžete začít s hlavním testem. Pokud Vám ještě není zcela jasné, co se po Vás v tomto testu chce, máte nyní možnost zeptat se přímo osoby, která Vám test zadává.

Snažte se odpovídat svižně, ale vyvarujte se chyb! U každé rovnice je nastaven určitý časový limit, takže s odpovědí přehnaně neotálejte.

Nyní položte ukazováček levé ruky na písmeno A a ukazováček pravé ruky na písmeno N a pro pokračování stiskněte mezerník."""

## TEXT SHOWN AFTER CORRECT AND INCORRECT RESPONSES DURING PROCESSING TRIALS AND TEXT FOR SUMMARIZING FEEDBACK
practice_correct_response = "Velmi dobře!"
practice_incorrect_response = "Bohužel špatně."
practice_summary = """Z celkového počtu %(total)s rovnic jste ohodnotili správně %(correct)s.

Pro pokračování stiskněte mezerník."""

# TEXT BETWEEN OPERATIONS
next_message = """Umístěte prsty na klávesy A a N a pro pokračování stiskněte mezerník."""

# MESSAGE SHOWN WHEN A PARTICIPANT TAKES TOO MUCH TIME:
time_out_message = "Čas překročen!"

## FINAL MESSAGE
finished_message = """Hotovo!

Pro pokračování stiskněte mezerník."""

## TEXT SHOWN AFTER THE LAST RUN:
good_bye_text = """Mnohokrát děkujeme za Váš čas! Na shledanou!"""
