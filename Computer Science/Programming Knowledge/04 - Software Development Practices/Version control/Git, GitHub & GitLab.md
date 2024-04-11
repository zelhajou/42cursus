# Git, GitHub & GitLab

[Git & Github](Git%20&%20Github.md)

# Workflow

⭐ [Syncing](https://www.atlassian.com/git/tutorials/syncing)

[Understanding the GitHub flow](https://guides.github.com/introduction/flow/)

[GitLab workflow](GitLab%20workflow.md)

⭐ [Git flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html#git-flow-and-its-problems)

⭐ [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

# Tutorials

[Great tutorial by Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init)

# Solving problems

![Git,%20GitHub%20&%20GitLab%2084df2435f11b4d5d98be222ef85572d4/Untitled.png](Mathematics%20and%20Computer%20Science/Computer%20Science/01%20-%20Programming%20Knowledge/04%20-%20Software%20Development%20Practices/Version%20control/Git,%20GitHub%20&%20GitLab%2084df2435f11b4d5d98be222ef85572d4/Untitled.png)

Source: [http://justinhileman.info/article/git-pretty/git-pretty.png](http://justinhileman.info/article/git-pretty/git-pretty.png)

- If work has been done on the wrong branch:

```bash
git stash
git checkout branch123
git stash apply
```

Once everything is back to normal, to clean the stash, remove it from the stash list:

```bash
git stash list
git stash drop <stash_name>
```

Source: [https://stackoverflow.com/questions/5964118/git-working-on-wrong-branch-how-to-copy-changes-to-existing-topic-branch](https://stackoverflow.com/questions/5964118/git-working-on-wrong-branch-how-to-copy-changes-to-existing-topic-branch)