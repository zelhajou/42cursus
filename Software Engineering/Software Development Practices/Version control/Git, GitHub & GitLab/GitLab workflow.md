# GitLab workflow

# GitLab branch workflow

### **Check out, review, and merge locally**

**Step 1.** Fetch and check out the branch for this merge request

`git fetch origin
git checkout -b '1607-adjust-schedule-for-new-layout' 'origin/1607-adjust-schedule-for-new-layout'`

**Step 2.** Review the changes locally

**Step 3.** Merge the branch and fix any conflicts that come up

`git fetch origin
git checkout 'develop'
git merge --no-ff '1607-adjust-schedule-for-new-layout'`

**Step 4.** Push the result of the merge to GitLab

`git push origin 'develop'`

**Tip:** You can also checkout merge requests locally by [following these guidelines](https://gitlab.com/help/user/project/merge_requests/reviews/index.md#checkout-merge-requests-locally-through-the-head-ref)