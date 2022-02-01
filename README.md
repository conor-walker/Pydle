# Pydle
A word game similar to Wordle, implemented in Python!

## Features
- Randomly selects a 5 letter word from over 5000 possibilities
- Tells you what letters are in the right position, which are present in the word but not in the right place, and which are not in the word at all
- Seed-based, so the word is the same when run on a given day - just like the real thing!
- That's about it - it's fairly barebones as-is!

## Prerequisites & Running
To run from source, you'll need to have Python installed and accessible on your system. 
- Download the repository locally
- Open a terminal in the **src** folder
- Enter ```python pydle.py``` in the terminal window. 
- And enjoy!
Compiled binaries are provided in the releases section for Windows and Unix systems. For Windows, the exe can run as-is. For MacOS/Linux, download the pydle file, adn in a terminal window run the command ```chmod +x /path/pydle```, then ```pydle``` while still in the directory.

## Future
I don't anticipate spending a huge amount of time on this in the near future, but small things I'd like to throw in are:
- Make the output slightly prettier, or as pretty as it can be in a terminal. No plans of making a full GUI version just yet!
- Validate that users word is an actual real word

## License
Published under GPL, so go nuts! Contributions and forks of any stripe welcome :)
