
**Git** It is an open source version control system (VCS). this means that when developers create something, they make constant changes to the code, releasing new versions up to and after the release.<br>
version control systems keep these revisions straight, stroring the modifications in a central repository, allowing developers to easily collaborate.

## Basic Concepts
**main**    : default development branch <br>
**origin**  : default upstream repo<br>
**HEAD**    : current branch<br>
**HEAD^**   : parent of HEAD<br>
**HEAD~4**  : grea-great grandparent of HEAD<br>

## Commands Sequence

| flow | Commands |
| :--- | :------- |
|**CREATE** | init / Clone
|**BROWSE** | status / log / show / diff / branch |
|**CHANGE** | |
|**REVERT** | reset / checkout / revert |
|**UPDATE** | pull / fetch / merge / am |
|**BRANCH** | checkout branch |
|**COMMIT** | commit |
|**PUBLISH** | push / format-patch |

## SETUP

Configuring user information used across all local repositories

- set a name that is identifiable for credit when review version history
``` 
git config --global user.name “[firstname lastname]”
```
- set an email address that will be associated with each history marker
```
git config --global user.email “[valid-email]”
```
- set automatic command line coloring for Git for easy reviewing
```
git config --global color.ui auto
```

## SETUP & INIT
Configuring user information, initializing and cloning repositories

- initialize an existing directory as a Git repository
``` 
git init
``` 
- retrieve an entire repository from a hosted location via URL

``` 
git clone [url]
``` 

## STAGE & SNAPSHOT
Working with snapshots and the Git staging area

- show modified files in working directory, staged for your next commit
```
git status
``` 
- add a file as it looks now to your next commit (stage)
```
git add [file]
``` 
- unstage a file while retaining the changes in working directory
``` 
git reset [file]
``` 
- To view the merge conclicts
``` 
git diff // (complete conflict diff)
git diff --base $file // (against base file)
git diff --ours $file // (against your changes)
git diff --theirs $file //(against other changes)
```

- diff of what is staged but not yet commited
``` 
git diff --staged
``` 
- commit your staged content as a new commit snapshot
``` 
git commit -m “[descriptive message]”
```
- Add alĺchanges made to tracked files & commit
``` 
git commit -am “[commit message]”
``` 

## BRANCH & MERGE
Isolating work in branches, changing context, and integrating changes

- list your branches. a * will appear next to the currently active branch
```
git branch
``` 
- create a new branch at the current commit
``` 
git branch [branch-name]
``` 
- switch to another branch and check it out into your working directory
```
git checkout
```
- Create a new branch and switch to it
``` 
git checkout -b <new-branch>
```
- merge the specified branch’s history into the current one
```
git merge [branch]
```
- Merge & squash all commits into one new commit
```
git merge --squash a
```
- Delete a merged branch
``` 
git branch -d <branch>
```
- Delete a branch, whether merged on not
``` 
git branch -D <branch>
```
- Add a tag to current commit (often used for new version releases)
``` 
git tag <tag-name>
```

- show all commits in the current branch’s history
```
git log
```

## INSPECT & COMPARE
Examining logs, diffs and object information

- show the commit history for the currently active branch
```
git log
```
- show the commits on branchA that are not on branchB
```
git log branchB..branchA
```
- show the commits that changed file, even across renames
```
git log --follow [file]
```
- show the diff of what is in branchA that is not in branchB
```
git diff branchB...branchA
```
- show any object in Git in human-readable format
```
git show [SHA]
```
## SHARE & UPDATE
Retrieving updates from another repository and updating local repos

- add a git URL as an alias
```
git remote add [alias] [url]
```
- fetch down all the branches from that Git remote
```
git fetch [alias]
```
- merge a remote branch into your current branch to bring it up to date
```
git merge [alias]/[branch]
```
- Transmit local branch commits to the remote repository branch
```
git push [alias] [branch]
```
- fetch and merge any commits from the tracking remote branch
```
git pull
```

## TRACKING PATH CHANGES
Versioning file removes and path changes

- delete the file from project and stage the removal for commit
```
git rm [file]
```
- change an existing file path and stage the move
```
git mv [existing-path] [new-path]
```
- show all commit logs with indication of any paths that moved
```
git log --stat -M
```

## REWRITE HISTORY
Rewriting branches, updating commits and clearing history

- apply any commits of current branch ahead of specified one
```
git rebase [branch]
```
- Interatively clean up a branches commits before rebasing onto main
```
git rebase -i main
```
- Interatively rebase the last 3 commits on current branch
```
git rebase -i Head~3
```
- clear staging area, rewrite working tree from specified commit
```
git reset --hard [commit]
```

## TEMPORARY COMMITS
Temporarily store modified, tracked files in order to change branches

- Save modified and staged changes
```
git stash
```
* list stack-order of stashed file changes
```
git stash list
```
- write working from top of stash stack
```
git stash pop
```
- discard the changes from top of stash stack
```
git stash drop
```

## IGNORING PATTERNS
Preventing unintentional staging or commiting of files
- Save a file with desired paterns as .gitignore with either direct string matches or wildcard globs
```
logs/
*.notes
pattern*/
```
- system wide ignore patern for all local repositorie
```
git config --global core.excludesfile [file]
```