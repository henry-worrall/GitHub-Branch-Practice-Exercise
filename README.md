# GitHub Branching Practice Exercise

Welcome to this practice exercise where you will familiarise yourself with how an organisation might use GitHub for collaboration!

## Aims

To provide an understanding as to what Git and GitHub are, and why they might be useful in a collaborative environment. To give an example of how you can use GitHub for file management and version control.

## Prerequisites 

Users must have:

1.	A GitHub account - [Join GitHub](https://github.com/join) 
2.	Installed Git on your computer and configured your Git username and commit email address – [Set up Git](https://docs.github.com/en/github/getting-started-with-github/set-up-git) (follow steps 1-3).
3.	Ensured you can access your command line/terminal, and can access a text/code editor (e.g. notepad/sublime) on your computer.

If you don't configure your email and username in steps 2 and 3 of the Git Setup guide, then you can't push your changes from the command line!

MacOS users can follow this [YouTube video](https://www.youtube.com/watch?v=ZM3I16Z-lxI) if they are having issues with installing Git.

## Git and GitHub

Git and GitHub go hand-in-hand together, however, they are not the same thing.

**Git** is an open-source programme for tracking changes in text files. It was written by the author of the Linux operating system and is the core technology that GitHub is built on top of.

**GitHub** is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Motivation

GitHub provides an easy way to share code and collaborate with others. Companies use Git and GitHub to track and store changes made to files. This is particularly useful for developers, who use Git to trace errors associated with a new feature, or rollback software to a previous version.

Git maintains a record of the changes during the construction and lifetime of a product, whilst not replicating entire files. In this way, file storage is reduced and there is no need to call files '`file.txt`', '`file-edit.txt`', '`file-edit-2.txt`', etc.

Another reason for using Git is that it allows people to work on the same files simultaneously without disrupting the main product. This principle is known as *branching* and is what this exercise will cover.

**Branching** lets users create a separate 'branch' of work where they can make changes or introduce new features to the product independently of the main version (the master branch). Once a feature has been tested, it can be merged back with the latest version of the master branch.

<figure>
    <img src="https://guides.github.com/activities/hello-world/branching.png" alt="" width="100%"  style="display: block;"/>
</figure>

*Example of how you would integrate a new feature into the going master solution using a GitHub branch.*

Finally, hosting your code on GitHub is also a great way of showcasing what you're capable of. Whether it's to prospective clients or future employers, showing them that you can code is far more persuasive than telling them. It also shows that you can use version control, which is a desired skill by many employers.

## Instructions

### 1. Clone this Repository

To download this repository to your local computer, click the 'code' button at the top of the page and copy the HTTPS address given.

<figure align="center">
<img src="screenshots/clone-repo.jpg?raw=true" alt="" width="40%"  style="display: center;"/>
</figure>

Open a terminal (command prompt, or Git Bash if you have it) and change to the directory you'd like to work in using the *cd* command (see Command Line Commands [here]( https://www.codecademy.com/articles/command-line-commands)). Run the *clone* command with the appropriate address. 
    
    git clone https://github.com/henry-worrall/GitHub-Branch-Practice-Exercise.git

You should now be able to see all of the repository files in your local file explorer.

### 2. Create a Branch

**This is really important!** Before you start editing files in a collaborative environment, you must change to an independent branch. This avoids situations where you accidentally introduce a bug which breaks the functionality of the entire team’s project. If a bug is introduced on your branch, it won't affect anyone else's work.

Create a branch with a descriptive title, e.g. *henry-feature-name*. This is done using the *branch* command.

    git branch henry-bug-fix

You can see a list of the available branches with the branch list command:

    git branch --list

You should be able to see the master (or main) branch and the branch you have just created. The asterisk indicates which branch you are currently on. In order to work independently on your new branch, you need to switch to it using the *checkout* command.

    git checkout henry-bug-fix

Currently, your new branch is an exact copy of the master branch. However, any changes you make whilst you have checked-out your branch will not affect the master branch. Therefore, you can now make edits to the code without worrying.

### 3. Make edits

On your new branch, make edits to the files. You can create a new file or edit an existing file, or delete a file (with caution!).

For this exercise, try to:
- create a new file
- edit the `main.py` file. 

The new file can be anything you like: text, Python, Ruby, HTML, R. It can be as simple or complicated as you like.

Edit the list in the `main.py` file to include your name. If you run the script, you will now see your name included with fellow Graycians!

### 4. Commit

As with all significant changes you make whilst using Git, you need to commit your changes to your branch. If you don’t commit a change, then the edits will not be logged in Git. Committing is a two-part process.  

1. Stage (i.e. select) the files you wish to commit
2. Commit the changes

To stage the files you have to use the *add* command:

    # adds all files with changes
    git add .

    # adds just the main.py file 
    git add main.py

You can check which files have and haven't been staged using the *status* command.

Once you have selected the appropriate files, commit the changes using the *commit* command. It’s best practice to provide a short descriptive message relating the changes you have made.

    git commit -m "Added myself to list"

### 5. Merge and Integrate Changes

There are many different processes that you could follow to integrate your changes with the master branch. However, I shall describe to you what I consider to be the best practice when it comes to working in a collaborative environment. I shall outline the steps below, before walking through them.

1. Pull the most recent version of the master to your local computer
2. Merge the master into your branch - best practice!
3. Push your branch to GitHub
4. Set up a pull-request - allows for peer review

Firstly, to pull the most recent version of the master branch you must ensure you are on the master branch. Then execute the *pull* command.

    git checkout master
    git pull

*Note that the first time you pull from a GitHub repository, you might need to specify the remote origin master branch. In this case, it will tell you the command*

If team members have made changes to the master branch whilst you have been building your new feature, this will update your local version of the master, mirroring the latest version on GitHub.

Next, you need to merge the most up-to-date version of the master branch into your new feature. To do this, ensure that you are on your branch and execute the *merge* command. You will need to select the branch you wish to merge in (i.e. master).

    git checkout henry-bug-fix
    git merge master

*Note that merging the master into your branch is the best practice since this will only alter your branch and not the master. Therefore, if the merge introduces a bug, it will only affect your branch and not the master.*

Your command line will either tell you that the merge has been automatically completed successfully, or that there have been some conflicts. If the merge tells you that you have a conflict, you will need to amend the conflicting file(s). You can amend them by opening them up in your code/text editor.

A conflict will appear in the conflicting file like this:

    <<<<<<< HEAD
    The file as it appears in your checked-out branch (i.e. your branch).
    =======
    The file as it appears in the branch you are merging in (i.e. the master branch). 
    >>>>>>> master

Change the file appropriately by removing the <<<<<, ======, >>>>> lines and editing the code so it includes your solution, and the doesn't break anyone else's work.

Once you have resolved the conflicts appropriately, stage and commit the merged files.

    git add .
    git commit

*Note that if you do not supply any arguments after the commit command, Git will open up a temporary file which must then close. If file opens the in the terminal, you can close it by pressing* <kbd>Esc</kbd> &rightarrow; <kbd>:wq</kbd> &rightarrow; <kbd>enter</kbd>*. This can be avoided by using the message arguments.*

You can now push your merged branch to GitHub using the *push* command.

    git push

*Note that the first time you push changes to GitHub, you may be asked to authenticate yourself.*

Your feature is now ready to be peer-reviewed and fully integrated with the team's master branch, using a pull request

### 6. Set up a Pull Request

It is worth mentioning that a *pull request* differs from the *pull command*. As we saw above, the pull command is issued from the command line and fetches any updates which are on GitHub and adds them to our local repository. 

A pull request allows for peer review of your code and new feature. It allows others to comment and notify you of any bugs or functionality issues that might be present in your code. A pull request is therefore a collaborative feature of GitHub.

If you navigate back to the GitHub repository in your browser, you will be able to find your branch with your new features coded in. Click the "Compare & pull request" button to initiate a pull request. If you cannot see this button, you can set up a pull request in the "Pull requests" tab.

<figure>
<img src="screenshots/initiate-pull-request.png?raw=true" alt="" width="100%"  style="display: block;"/>
</figure>

You can then submit your pull request and leave any comments that you feel appropriate.

<figure>
<img src="screenshots/submit-pull-request.jpg?raw=true" alt="" width="100%"  style="display: block;"/>
</figure>

Your pull request will then appear on the "pull requests" tab. Other members of your team can now check out your code, suggest improvements or fixes. If needed, you can make any necessary changes and push them to GitHub (you will not need to create a new pull request). Once everyone is happy with your new branch's feature, someone will authorise the pull request, and your work will be fully integrated with the team's master branch.

You can confirm this by pulling the master branch to your local repository.

## Outcomes

You have now successfully introduced a new feature into the repository! I hope that after completing this exercise you have a good understanding of the following:

- What Git and GitHub are
- Why they are useful for version control and collaboration, and
- How to use GitHub:
    - clone a repository 
    - create and switch branches
    - stage changes
    - commit changes
    - pull/fetch changes from GitHub to your local repository
    - merge branches
    - push changes to GitHub
    - make pull requests

If you have any feedback or suggestions about this exercise, then I would love to hear them!
