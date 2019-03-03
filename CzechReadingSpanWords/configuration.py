# -*- coding: utf-8 -*-

# WHICH FONT SHOULD BE USED?
fontname = "Helvetica"

# AND AT WHICH SIZE?
fontsize = 22

## FILE WITH ITEMS FOR THE PROCESSING COMPONENT. EACH LINE MUST CONTAIN A PROCESSING
## ITEM (SENTENCE OR OPERATION) AND THE PROPER RESPNSE (y OR n), SEPERATED BY A TAB.
processing_items_file = "sentences_czech.txt"

# FILE WITH ITEMS FOR THE RECALL COMPONENT. EACH LINE HOLDS ONE ITEM
target_items_file = "target_words_czech.txt"

# KEY MAPPING. CHARACTER AFTER COLOM INDICATES, WHICH KEY TO MAP TO THE RESPECTIVE RESPONSE.
responses = {
  'y':'a',
  'n':'n'
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
time_out_factor = 3.5

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

welcome_text = """Vítejte v testu pracovní paměti!

V tomto testu máte za úkol ohodnotit, zda věty, které budete číst,
dávají smysl, a zapamatovat si přitom slova, která se vám budou zobrazovat po přečtení každé z vět.
Test trvá celkově 15 minut.

Pro jeho spuštění zmáčkněte mezerník."""

# TEXT SHOWN AT THE BEGINNING OF THE TEST:
instructions1 = """Nejprve si vyzkoušíte hodnocení vět. Potom, co
ohodnotíte větu, se Vám objeví zpráva, jestli jste odpověděli správně,
anebo špatně. Jde zatím o nácvik, v samotném hlavním testu už zpětnou
vazbu dostávat nebudete.

Pokud je věta smysluplná, stiskněte klávesu A. Pokud není smysluplná, stiskněte klávesu N. 

Snažte se vyvarovat chyb a postupujte podle pokynů. Při čtení nedělejte přestávky.
Pokud máte nějaké dotazy, je nyní čas se zeptat.

Nyní položte prst levé ruky na klávesu A a prst pravé ruky na klávesu N a
pro pokračování stiskněte mezerník."""

## TEXT SHOWN AFTER THE PROCESSING TRIALS AND BEFORE PRACTICE TRIALS.
## THIS SECOND PHASE OF THE OVERALL TEST IS SUPPOSED TO MAKE PARTICIPANTS FAMILIAR WITH THE MEMORY TASK.
instructions2 = """V druhé části cvičení se Vám po ohodnocení každé věty
objeví nějaké slovo. Vaším úkolem bude si tato slova zapamatovat.
Po několika větách se zobrazí symbol otazníku a Vaším úkolem bude
napsat všechna slova, která se mezi větami objevila.

To, co napíšete, uvidíte v dolním řádku. 
Jednotlivá slova oddělujte mezerami a až budete hotovi, zmáčkněte 
klávesu Enter. Vyvarujte se překlepů a raději si po sobě jednotlivá slova 
ještě jednou přečtěte, jestli jsou napsána správně. 
Velká a malá písmena nehrají roli.

Položte prst levé ruky na klávesu A a prst pravé ruky na klávesu N.
Pro pokračování stiskněte mezerník."""

## THESE INSTRUCTIONS APPEAR AFTER THE FAMILIARIZATION PERIOD AND PREPARES PARTICIPANTS FOR THE ACTUAL TEST:
instructions3 = """Toto je konec cvičení. Nyní už máte představu o tom, co je Vaším úkolem
v tomto testu. Nemáte-li další otázky, můžete začít se samotným testem.

Hodnoťte věty co nejrychleji! Pokud Vám to bude trvat příliš dlouho, věta zmizí.


Položte prst levé ruky na klávesu A a prst pravé ruky na klávesu N.
Pro pokračování stiskněte mezerník."""

## TEXT SHOWN AFTER CORRECT AND INCORRECT RESPONSES DURING PROCESSING TRIALS AND TEXT FOR SUMMARIZING FEEDBACK
practice_correct_response = "Velmi dobře!"
practice_incorrect_response = "Bohužel špatně!"
practice_summary = """Z celkového počtu %(total)s vět jste správně ohodnotili %(correct)s.

Pro pokračování stiskněte mezerník."""

# TEXT BETWEEN OPERATIONS
next_message = """Položte prst levé ruky na klávesu A a prst pravé ruky na klávesu N.
Pro pokračování stiskněte mezerník."""
target_request = """Uveďte všechna slova, která se objevila mezi větami, na která si vzpomínáte."""

# MESSAGE SHOWN WHEN A PARTICIPANT TAKES TOO MUCH TIME:
time_out_message = "Čas překročen!"

## FINAL MESSAGE
finished_message = """Hotovo!

Pro pokračování stiskněte mezerník."""

## TEXT SHOWN AFTER THE LAST RUN:
good_bye_text = """Mnohokrát děkujeme za Váš čas! Na shledanou!"""
