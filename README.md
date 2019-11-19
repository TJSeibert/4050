# 4050 Project

## TO-DO
  * Create views and implement search by currently running and coming soon
  * Add search by title and category
  * Display results of search (movie, title, rating, trailer(will do trailer at the end))
  * More details button under movie leads to page with more detail (Title, Category, Cast, Directory, Producer, Synopsis, Reviews, Trailer picture and video)
  * Checkout view to schedule a movie

## Git Guide

### Cloning the repository

Before cloning the repository you will need to have access to it. If you are seeing this more than likely you are looking at the repository right now, so that shouldn't be an issue.

The first step to get coding is to clone the repository so you can start working on the code while git tracks all the changes you make. To do this, simply open up git bash and navigate to the directory
where you want to keep your code and enter the clone command. 

```
git clone https://github.com/TJSeibert/4050.git
```

### Branches 
Before you start coding, you should make sure you are working in the correct branch. Generally, we will want to have a separate branch for each feature we are working on.
This way we can work on that feature without effecting the other features. For example, one of the features we need to create for program one is the join method. This method
will have its own branch (at least for now). The other methods may have their own branches as well. Creating a branch is easy.

```
git branch [branch-name]
```

Once a branch has been created, you can easily switch to it using the format

```
git checkout [branch-name]
```

Once you have switched to the correct branch, you can go ahead and start making changes to the code (you don't TECHNICALLY have to do this before making your changes, but it will help you avoid accidentally commiting to the wrong branch). 

### Commiting, pushing, and pulling

#### commit
A commit is a tracked change to your code that is accompanied by a short message 
that describes the change. As you write your code, please be sure to make periodic commits to track your changes. 
This should be done any time you finish some aspect or complete a small change. It is usually best to commit after making sure the change you made works. 
However, for an especially difficult to solve bug, you may need to make several commits for different attempted solutions. Use your best judgement!

A commit takes two steps. The first is to add the files you have changed which will be included in the commit. You can also add directories and all the directories' contents will be added. 

```
git add [file-name/directory-name]
```
Once the files to track have been added, you can make your commit with your commit message.

```
git commit -m "Example commit message."
```
For you commit message just give a brief (1-2 sentences at most) description of the changes you made. 

#### push
Pushing is when you upload your changes to github. If you are working on a branch with someone else, it is important to push fairly often. You will want to push
when you have made a change you are fairly certain will work and not cause issues. This allows others who are working on the branch with you to pull your code so they 
can be sure they are using the latest version, it allows the group to see what you've done, and safely backs up the files on github. If you are working alone on a branch,
it is not especially important to push often, but it's still good to do so when you complete some aspect. You can also push so the group can see your code if you need help
with something.

In order to push you may need to set up your the place where you want to push to. This is called setting your remote.

```
git remote add origin https://github.com/TJSeibert/4050.git
```
Note: you can name your remote anything, but here it has been named "origin". 

Once your remote is set up, you can set it as the upstream for your branch. This means your branch will push to this remote. 

```
git push --set-upstream origin [branch name]
```
Once this is done, you can push changes to this branch much more simply with `git push`. 
#### pull
Pulling is when you update the code on your machine to be consistent with the version on github. If you are working alone on a branch,
this is not especially important. If you are working with someone on a branch you will want to pull fairly often. Each time you
sit down to write some code, you may want to pull first. Additionally, as features get completed and their branches are merged into the master,
you will need to pull to make sure your code is up to date, and to avoid cloning everything again. 

To pull, simply checkout the branch you wish to pull...

```
git checkout [branch name]
```
...and then pull.
```
git pull
```

If you encounter errors, they are likely due to untracked changes. Make sure you either commit all your changes before pulling. If you
have changes you do not wish to keep, you can use git stash to stash them before pulling. Stashed changes can be recalled later. You can
also do ```git clean -f``` to permanently remove changes but be careful because there is **NO GOING BACK** if you use this.

## Django Startup

You should be able to start up the website immediately by using

```
python3 manage.py runserver
```
Then, you can simply go to http://127.0.0.1:8000/ to see what we have. 
