# A Spanish Operation Span Task

This test battery includes material for conducting an operation span task in which the participants have to memorize high-frequency Spanish target words.  This task was used in a eyetracking study by Titus von der Malsburg and Shravan Vasishth ([Language and Cognitive Processes, 2013](http://www.tandfonline.com/doi/abs/10.1080/01690965.2012.728232)).  See the article for details about how the test material was compiled.

## Running the test

In order run the test, you have to download the test program `py-span-task.py`.  Store the program in the same directory in which the test battery was saved.  Then open a terminal, enter the directory in with test battery, and enter the following command:

    python py-span-task.py configuration.py

Then, you will be prompted to enter an ID for the participant that is tested.  Once you have entered the ID, the test will start and instructions for the participant will be displayed.  When the test is finished, the test program will create a new file with the test results.  The name of this file is the participant ID with the added suffix `.dat`.  At any time you can abort the test by pressing the escape key on you keyboard.  No test results will be saved in this case.




