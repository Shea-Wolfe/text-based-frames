## Getting started

* The key files in this repo are classes.py, text_parser.py, generation.py, and game_unpacker.py.
* Once you have the above files.  Run `python generation.py` and follow the commands to create your own game.
* At the end of generation you will be prompted to enter a name for your games.  This will write it as a pickled file in the current repo.
* To play a game you've created run `python game_unpacker.py your_gamename_here` 
* Saving a game in progress works the same as creating a game, the name you provide will be written out as a pickled file.  
* To resume a saved game run `python game_unpacker.py your_savename_here`
* There is a suite of tests included that can be run using nose, which is included in the requirements.txt. 
* To run the tests simply enter `nosetests` after you have installed nose using pip.
* Please note that creating a game, saving a game, or running the test suite all write files to the current directory, so be sure that writing is enabled.

## Description

* This repo is dedicated to creating simple text based games using python. 


## Future plans
* Twitter integration
* Try to get it running in a browser rather than terminal

