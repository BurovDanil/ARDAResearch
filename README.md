
The purpose of this repository is for our ARDA research paper experiment.

The idea of the assignment is to test if using the command line to do some basic git commands is more efficient than using GitHub Desktop.

The person will be given a repository consisting of two branches. The first assignment will be done in the main. And the second assignment will be done in the branch called '2nd assignment'.

<h2> First assignment </h2>

1) Clone the repository in the desired directory on your machine (copy the URL from GitHub website before starting the experiment)
2) When you have cloned the repository, find the file called 'TicTacToeController.java' with the help of the command '-cd ('Change directory')' and the command '-ls('list')'.
3) After finding the file enter the text editor (vim 'filename') and do the following things.
    - Edit the 'set the current player' to 'currentPlayer'.
    - Scroll down and find the method 'initialize()' and do what is said the comment.
    - Navigate to the method called checkForWinner().
    - There is a comment that describes what should be done.
    - Save the file using ':w' and quit the file after with ':q'
4) Now we need to enter the text editor for the file 'Application.java'.
    - Edit eveything that has in quotes FIXME.
    - Instead of FIXME for the fxml write down 'TicTacToe'
    - Set the title to be 'TicTacToe'
    - Save and quit.
5) View the current status of the branch. 
6) Add the untracked files for staging.
7) Commit your changes to the branch and give it the message 'submit (number is given by us :3)'.
8) And then push the changes to the main branch.
9) After you have pushed the changes to the branch revert the changes to the commit you just made.

<h2> Second assignment </h2>

1) Switch the branch from main to 2ndAssignment.
2) There are stashed files in the branch, first see what is stashed with the command 'git stash show' and press 'q' after you review it.
3) Get the stashed changes out of the branch.
4) Push all the changes from the stash.
5) Switch to the main after you have pushed the staged changes.
5) Merge the main into the 2ndAssignment branch.
6) Resolve the merging issue in the files specified.
7) Push all the merged changes into the main.


