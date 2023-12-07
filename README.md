# quacklibs
CS50 final project

Video link: 

Cite sources/help: In this project, we received extensive help from the CS50 duck and, in repayment, we have dedicated the entire lore of the website to DDB, whom all of the QuackLibs are about. We also used ChatGPT for help with debugging. Talia wrote our amazing QuackLibs and used ChatGPT to help modify them to fit each reading level, they were then checked for readability using an online readability checker. 

Our final project is an online version of the classic game, MadLibs, for which we have put a CS50 spin on. We chose to design an interactive website entitled QuackLibs that feature personally-designed MadLibs that feature CS 50's beloved DDB as the main character in all the storylines. Our website allows a user to choose which reading level they are at, with 5 different reading levels spanning 2nd grade and below, 3rd grade to 5th grade, 6th grade to 8th grade, 9th grade to 11th grade, and 12th grade and above. The user has the option of either selecting the "Go to Page" button that is shown on the card associated with the desired reading level the user wishes to play at or under the navigation bar shown at the top of the page by clicking the button associated with their desired reading level. This redirects the user to a page that confirms the reading level they have selected to play at, and allows the user to press "Start a QuackLib Now!" in order to begin a MadLib at the selected reading level. The code associated with these redirect pages is shown in the .html files with the name "level#.html" (with the # ranging from 1-5 based on level with 1 as grade 2 and below) that are listed under the "templates" folder. 

From there, we implemented a randomization function that is shown in our "random.js" file listed under the "static" folder, which randomizes which input form the user receives. We hand-wrote three different unique MadLibs storylines that feature CS 50 DDB as the main character, and then used a combination of ChatGPT and our own human edits to modify these storylines to be of less or more difficulty to match the reading level they were to correspond to. From there, we used a reading level calculator (please reference exact link shown above) that we used to confirm that the storylines' difficulty was on-par with the reading level we associated it with. This process was done for all three storylines, with the storylines themselves remaining the same across all 5 reading level options, but the difficulty varying based on the reading level. The storylines that we created are "Duck Takes a Tour!," "Duck Disappearance!," and "Duck Goes to Disney!" that have associated input and output .html files that are shown in the "templates" folder. The .html input form files associated with "Duck Takes a Tour!" are shown in town#.html (with the # ranging from 1-5 based on level with 1 as grade 2 and below). The .html output form files associated with "Duck Takes a Tour!" are shown in town#_done.html (with the # ranging from 1-5 based on level with 1 as grade 2 and below). The .html input form files associated with "Duck Disappearance!" are shown in disappearance#.html (with the # ranging from 1-5 based on level with 1 as grade 2 and below). The .html output form files associated with "Duck Disappearance!" are shown in disappearance#_done.html (with the # ranging from 1-5 based on level with 1 as grade 2 and below). The .html input form files associated with "Duck Goes to Disney!" are shown in disney#.html (with the # ranging from 1-5 based on level with 1 as grade 2 and below). The .html output form files associated with "Duck Goes to Disney!" are shown in disney#_done.html (with the # ranging from 1-5 based on level with 1 as grade 2 and below). The styling for all of these .html files originates from our "style.css" file listed under the "static" folder. 




and fill in an input form with the words needed to complete the QuackLib.- Users then get back the story, with their words filled into it. MadLibs (and QuackLibs) are supposed to have silly outputs that perhaps don't make the most sense. 

This program was created in a WSL space on VS Code and requires python, JavaScript, CSS, jinja, and html. To compile the program, first make sure you have python-dotenv installed. If you do not, you should be able to install using pip install python-dotenv. From there, make sure you are in the folder quacklibs within the quacklibs project (the terminal should say quacklibs/quacklibs$). You should then be able to run the application using "flask run" in the terminal. 

You should then be able to use the link in the terminal to take youself to the homepage of our website where you should be greeted by some cute ducks. You can use either the navigation bar or the links on the homepage to navigate to the page of the reading level that best suits you. Click the begin QuackLib now button to begin the form for a randomly selected QuackLib. All blanks are required and some will auto-capitalize. It is in your best interest to fill out the form with the requested word (if it asks for a noun, you should actually provide a noun). We will not stop you from inputting a verb in place of a noun, but the story will not make as much sense and will not be as fun when you are done. When you are finished filling in your words, click the submit button at the bottom of the page to receive your completed QuackLib. You may complete another by using the navigation bar to return to your reading level and randomly generating a new QuackLib. 