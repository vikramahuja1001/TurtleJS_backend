TurtleBlocks JS with Git Backend<br />

The original TurtleBlocks JS project is mantained at https://github.com/walterbender/turtleblocksjs . This project was a part of GSOC 2016 
and the aim of this project was to add git functionaities to the web activity so that user can use basic git functionalities
in the activity itself and need not have the knowldege of git but use it indirectly as a tool to save things. This project uses 
the git backend code https://github.com/vikramahuja1001/GitBackend which is based on dulwich(https://www.dulwich.io). Basic
information of Git is necessary before using the Git Backend. Give Git a try- https://try.github.io/levels/1/challenges/1 .
 Backend app contains the code for the main TB activity. Test app is just a test flask app to test some of its functionalities.<br />

Git Functions Implemented:<br />
1. Create a new file - Create a new .tb file to work on. The user will get prompted for a file name. This file will be saved in
 turtle folder(repo) and will contain the necessary code. Will also set the current file value to the new file created. <br />
2. Save to file - Saves the pallete code in the file which is loaded into the activity, i.e. the current file.<br />
3. Add - Similar to Git Add Command.<br />
4. Status - Similar to Git Status Command <br />
5. Commit - Similar to Git Commit, remember to use add button before committing. User will be prompted to enter a commit message.<br />
6. Commit History - Shows the commit history, i.e., the total number of commits, their timestamp and the person who made them.<br />
7. Revert back to a commit - Revert to any of the previous commit. In order to make any previous commit as the latest state
of the commit, just commit again after reverting to that commit.<br />
8. Diff of last 2 commits <br />
9. Load a File - Load an existing .tb file to the palette.<br />
10. Clone/Pull and Load Turtle Repo - It will clone the Turtle Codes repo (https://github.com/vikramahuja1001/TurtleCodes) if not available
,if it is available then it will check for changes using Git Pull and load that repo for <br />
11. Push - Similar to git push. Will push to the remote Turtle Codes repo (https://github.com/vikramahuja1001/TurtleCodes)<br />

Backend App:
The turtle folder contains the .tb files which contains turtle blocks code, the diffs folder contains equal number of files
as there are in the turtle folder. The files in diff folder are named as diff_file_(filename) and they contain the n*(n-1)
diffs if there are n commits in that file. The diff file is updated each time Revert back to a commit or Diff of 2 last commits
functions are called. Tha app folder contains the main code. Static folder in it contains all the TurtleBlocks JS code which
converted to the flask application. Flask is required to run the JS activities. A views.py file has to be created which will create necessary functions to be called by the browser. XMLHttpRequest has to be used from the browser side to connect the JS functions to their python counterpart.
 There are 3 main files in the app folder: <br />
1. views.py : Contains corresponding python code for the implemented git functions called by the browser.
Functions in views.py: <br />

2. diff_func.py : Code for creating the diff file of commits <br />

3. backend.py : Necesary code for creating the backend.
