# Hangman-using-Python
It is a Hangman game in GUI format using Python3 and Tkinter package.
It also requires PIL package to allow display of images across Game GUI.

Compiling Code:
  For compiling use Python3. Also make sure you have installed Tkinter and PIL packages for successful compilation.
  To install this packages you can use well-known Python package manager "pip".
  
  Just go to command prompt/terminal and use following commands-
  To install Tkinter package: pip install python-tk
  To install PIL package: pip install Pillow
  
  After this you can use python to run game by using file "hangman.py" file.
  e.g. In command prompt/terminal type- "python hangman.py" without the quotes.
  
About Game:
  This game is about replicating Hangman game on computer. In this game, user have to predict the word for which he is given word length and he has 10 chances to predict each letter from word. Game GUI shows all letters in word by "*" initially. When user predicts a letter correctly, Game GUI turns the particular * into predicted letter from word giving user idea about predicted letter's actual place in word. If user predicts wrong letter, he loses one chance. Game continues till user either predicts all letters correctly or he runs out of chances. If user predicts word correctly, he can continue game for next word while retaining his score. But if he loses he will have to start again.
  
Further work:
  Game is extensible with other ideas like High Score system, Multi-Player battles, expanding game word list, making more interactable GUI, etc.
