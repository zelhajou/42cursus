# Git & Github

- **What kind of program is Git?**
    
    ◦ Git is a version control program.
    
- **What are the differences between Git and a text editor in terms of what they save and their record keeping?**
    
    ◦ A text editor can only make and save changes to a file.
    ◦ Git tracks changes to the files and their contents over time.
    
- **Does Git work at a local or remote level?**
    
    Git works on a local level. Any changes you make are saved locally with Git.
    
- **Does GitHub work at a local or remote level?**
    
    GitHub works on a remote level. You must push your local changes (using Git) to GitHub.
    
- **Why is Git useful for an individual developer?**
    
    Git is useful for creating snapshots of your work. If you realize halfway through that you've messed up, it's much easier to reset.
    
- **Why are Git and GitHub useful for a team of developers?**
    
    Git and GitHub are useful for teams because they can merge code together. A developer can work on one part of the code while a second developer works on another part. They can then use Git and GitHub to easily combine their changes.
    

**Git** is like a really epic save button for your files and directories. Officially, Git is a version control system. save in Git records differences in the files and folders AND keeps a historical record of each save

> Git enables you to review how your project grows and to easily look at or restore file states from the past. Once connected to a network, Git allows you to push your project to GitHub for sharing and collaborating with other developers.
> 

> Git is a program you install which allows you to annotate the changes you make to create an easily navigable system history.
> 

V**ersion control :**  Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later

[Git - About Version Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

[git - the simple guide](https://rogerdudler.github.io/git-guide/)

[GitHub Git Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet/)

**GitHub** is a service that allows you to upload your code using Git and to manage your code with a nice web interface. GitHub and Git are not the same thing or even the same company.

[GitHub Guides](https://guides.github.com/)

> while Git works on your local machine, GitHub is a remote storage facility on the web for all your coding projects.
> 

### Git Config

```bash
git config --global user.name "Your Name"
git config --global user.email "yourname@example.com"
```

> GitHub recently changed the default branch on new repositories from `master` to `main`, change the default branch for Git using this command:
> 

```
git config --global init.defaultBranch main
```

> To enable colorful output with `git`, type
> 

```
git config --global color.ui auto
```

> To verify things are working properly, enter these commands and verify that the output matches your name and email address.
> 

```
git config --get user.name
git config --get user.email
```

### **Create an SSH Key**

An SSH key is a cryptographically secure identifier. It’s like a really long password used to identify your machine. GitHub uses SSH keys to allow you to upload to your repository without having to type in your username and password every time.

First, we need to see if you have an SSH key already installed. Type this into the terminal:

```
ls ~/.ssh/id_rsa.pub
```

```bash
ssh-keygen -C <youremail>
```

### **Link Your SSH Key with GitHub**

Now, you need to tell GitHub what your SSH key is so that you can push your code without typing in a password every time.

First, you’ll navigate to where GitHub receives our SSH key. Log into GitHub and click on your profile picture in the top right corner. Then, click on `Settings` in the drop-down menu.

Next, on the left-hand side, click SSH and GPG keys. Then, click the green button in the top right corner that says New SSH Key. Name your key something that is descriptive enough for you to remember where it came from. Leave this window open while you do the next steps.

Now you need to copy your public SSH key. To do this, we’re going to use a command called `[cat](http://www.linfo.org/cat.html)` to read the file to the console. (Note that the `.pub` file extension is important in this case.)

```
cat ~/.ssh/id_rsa.pub
```

Highlight and copy the output, which starts with `ssh-rsa` and ends with your email address.

Now, go back to GitHub in your browser window and paste the key you copied into the key field. Then, click `Add SSH key`. You’re done! You’ve successfully added your SSH key!

### **Testing your key**

Follow the directions in [this article from GitHub](https://help.github.com/en/articles/testing-your-ssh-connection) to verify your SSH connection **(Don’t forget to omit the `$` when you copy and paste the code!)**. You should see this response in your terminal: **Hi username! You’ve successfully authenticated, but GitHub does not provide shell access.** Fear not the part about not being provided shell access. If you see this message, you’ve successfully added your SSH key and you can move on.

---

- Commands related to a remote repository:
    - `git clone git@github.com:USER-NAME/REPOSITORY-NAME.git` or `git clone https://github.com/user-name/repository-name.git`
    - `git push origin main`
    
- Commands related to workflow:
    - `git add .`
    - `git commit -m "A message describing what you have done to make this snapshot different"`
- Commands related to checking status or log history
    - `git status`
    - `git log`
    
    The basic Git syntax is `program | action | destination**.**`
    
    For example,
    
    - `git add .` is read as `git | add | .`, where the period represents everything in the current directory;
    - `git commit -m "message"` is read as `git | commit -m | "message"`; and
    - `git status` is read as `git | status | (no destination)`.
    
    - **Explain the two-stage system that Git uses to save files.**
        
        ◦ A **save** in Git is divided into two terminal commands: `add` and `commit`. The combination of these two commands gives you control of exactly what you want to be remembered in your snapshot.
            ◦ **Staging:** Think of `add` as adjusting the number of people or elements to be included in a photo. With Git, you can select the changes you want to save with `git add`. Imagine a project that contains multiple files where changes have been made to several files. You want to save some of the changes you have made and leave some other changes to continue working on them.
            ◦ **Committing:** Think of `commit` as actually taking a photo, resulting in a snapshot. For example, to commit a file named README.md, type `git commit -m "Add README.md"`. The `-m` flag stands for "message" and must always be followed by a commit message inside quotation marks. In this example, the commit message was `"Add README.md"`.
        
        ◦ A **save** in Git is divided into two terminal commands: `add` and `commit`. The combination of these two commands gives you control of exactly what you want to be remembered in your snapshot.
            ◦ **Staging:** Think of `add` as adjusting the number of people or elements to be included in a photo. With Git, you can select the changes you want to save with `git add`. Imagine a project that contains multiple files where changes have been made to several files. You want to save some of the changes you have made and leave some other changes to continue working on them.
            ◦ **Committing:** Think of `commit` as actually taking a photo, resulting in a snapshot. For example, to commit a file named README.md, type `git commit -m "Add README.md"`. The `-m` flag stands for "message" and must always be followed by a commit message inside quotation marks. In this example, the commit message was `"Add README.md"`.
        
    - **Explain what `origin` is in `git push origin main`.**
        
        In Git, `origin` is a placeholder name for the URL of the remote repository. Git sets up the origin by default when it clones a remote repository. You can use `origin` to access the remote repository without having to enter a full URL every time. This also means that you can have multiple remotes for a repository by giving each a unique name.
        
    - **Explain what `main` is in `git push origin main`.**
        
        In Git, `main` is the branch of the remote repository you want to push your changes to. We will get more into branches in a later lesson, but the main thing to remember is that `main` is the official branch in your projects where production-ready code lives.
        
    
    [elsewhencode/project-guidelines](https://github.com/elsewhencode/project-guidelines#git-workflow)
    
    [Git and Git Flow Cheat Sheet](http://bilalarslan.me/git-cheat-sheet/)
    
    [gitignore.io](https://www.toptal.com/developers/gitignore)
    
    [Learn Git Branching](https://learngitbranching.js.org/?demo=&locale=fr_FR)
    
    **GITHUB :** 
    
    [tiimgreen/github-cheat-sheet](https://github.com/tiimgreen/github-cheat-sheet)
    
    [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions)