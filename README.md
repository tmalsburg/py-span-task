Py-Span-Task
============

Py-Span-Task is a simple application for testing working memory span.  It follows the recommendations given in Conway, Kane, Bunting, Hambrick, Wilhelm, & Engle ([Psychonomic Bulletin & Review, 2005](http://link.springer.com/article/10.3758/BF03196772)) and can be configured to perform operation span tests and reading span tests.  A protocol of the test procedure is saved into a simple text file that can be further analysed in statistical programs such as R or SPSS.

Py-Span-Task is written in Python and uses the TK-toolkit for graphical user interfaces.  On Linux and OS X systems, the necessary software for running Py-Span-Task should already be installed.  Running Py-Span-Task on Windows may require installing Python (which usually already includes the TK-toolkit).

## Frequently asked questions

### What's the state of this project?

We wrote the first version of Py-Span-Task in 2010.  Since then, researchers in a number of labs have successfully used this software to obtain working memory scores.  The software can thus be considered to be relatively reliable and ready for production use.

### Why have we written this software?

Operation and reading span tests play an important role in our research area.  Applications for testing working memory span were already available, however, running them required expensive software licenses.  Since these memory tests are actually relatively simple, we decided to write our own software.  Apart from saving money another benefit of having our own software is that we know exactly what the software is doing and that we can fix it ourselves if something doesn't work as it is supposed to.  Since we publish the code for our test software, other researchers can also check how exactly we obtained our data.

### Can everybody use this software?

Yes, everybody is invited to use our software and we will soon provide a manual and example configurations showing how to run different types of tests.  We may also provide test material for tests in several languages.  You can use, modify, and improve this material if you want.  Note, however, that *we can't take any responsibility for the correctness of the software or its results*.  If you use our software in your research, we would be happy if you could acknowledge that in your publications.  There is currently no paper about this software that could be cited.  Simply mention the name of the software so that other people can find it on the web.

### Can everybody modify the test software and the test batteries?

Yes, feel free to do so.  If you modify the test software or the test material, please consider sharing these changes with us so that we may integrate them in our version.  If you create new test material, or if you translate one of our tests into another language, we would also be happy to integrate these materials in our repository.

### Does Py-Span-Task support non-western scripts?

Yes, it does provided your configuration files and test materials are saved with the appropriate character encoding and provided that you are using a font that supports these scripts.  On OS X and modern Linux distributions, the best solution is to encode all your files in UTF-8.  It is likely that they are already saved in this encoding and in this case you are ready to roll.  Windows is a different matter, because (to my knowledge) it doesn't use UTF-8.  Create a new entry in the issue tracker in case you run into problems on Windows and we will help you to fix it.

### What if I find an error in the software or the test materials?

If you find bugs in the software, or errors in the material, please let us know and we will fix them.  For reporting the problem, please use the issue tracker provided by Github.  The issue tracker can also be used for feature requests.
