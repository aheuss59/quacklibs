We chose to use a flask application because we knew we wanted to have a more dynamic webpage that allowed for ideas like randomization of the QuackLib template when the user pressed a button. We also knew we would want to use jinja to modify the stories based on user input. 

Our app.py code is fairly simple and mostly serves to redirect the user to various pages. It's primary role is to take user input from the forms and pass that input to the "done" version of that html page. 

One thing our group spent a long time on is the most effective way to collect user input given that all of our forms were of different lengths and requested different types of words. We considered at one point having a uniform file that everyone filled out and then randomizing the output instead, but decided it didn't make a lot of sense for users to fill in more words than were needed. Because of this, we opted to use individual forms for each QuackLib. The setup for this takes the form of an html page (ex. disney1.html) that has an output page (disney1_done.html), sort of like quote and quoted from finance. 

Something that we wanted to do was implement a feature that randomized which QuackLib the user got to fill out. I chose to create a function for this in a separate JavaScript file (random.js) because it would be used on multiple different pages and was lengthy code. We discussed in office hours that despite the fact that python might be preferable for simplicity of the code, the random number generating aspect in JavaScript would work better. In random.js, a random number between 0-2 is generated. That number is then used to index into a list of links, which is passed to the function. The user is then redirected to that link. This gives the user limited control over which QuackLib they play. One flaw with this method is that the user may fill out the same QuackLib more than once, but we also think it's fun that user might get to replay the same story, but have a completely different output. 



Talia - talk about your implememntation of the capitalizing and underlining here, also your required, you could also talk about why you chose the format that you did for the form itself. 

Stephanie - why you did aesthetics the way you did

We designed the process also so that once the user clicks the submit button, the "done" template is generated with the output text and a fun picture related to the story. 

