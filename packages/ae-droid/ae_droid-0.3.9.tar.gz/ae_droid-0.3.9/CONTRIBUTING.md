<!-- THIS FILE IS EXCLUSIVELY MAINTAINED IN THE NAMESPACE ROOT PACKAGE. CHANGES HAVE TO BE DONE THERE. -->
# contributing

we want to make it as easy and fun as possible for you to contribute to this project.

## reporting bugs

before you create a new issue, please check to see if you are running the latest version; the bug may already be
resolved. also search for similar problems in the issue tracker; it may already be an identified problem.


### bug report contents

to help the maintainers of this repository understand the problem, please include as much information as possible:

1. clear description of how to recreate the error, including any error messages shown.
2. the version you are using.
3. Python version.
4. small self-contained code example that reproduces the bug.
5. if applicable, full Python traceback.


## requesting new features

1. provide a clear and detailed explanation of the feature you want and why it's important to add.
2. if you are able to implement the feature yourself (refer to the "contributing (step-by-step)" section below).


## contributing (step-by-step)

1. make sure you have a [GitLab account](https://gitlab.com/users/sign_in) to be able to
   [fork this repository](https://docs.gitlab.com/ce/workflow/forking_workflow.html).

2. clone your forked repo to your local computer, and set up the upstream remote:

        git clone https://gitlab.com/<YourGitLabUserName>/<ThisRepositoryName>.git
        git remote add upstream https://gitlab.com/ae-group/<ThisRepositoryName>.git

3. checkout out a new local feature branch and update it to the latest version of the `develop` branch:

        git checkout -b feature-xxx develop
        git pull --rebase upstream develop

    > please keep your code clean by staying current with the `develop` branch, where code will be merged.
    > if you find another bug, please fix it in a separated branch instead.


4. push the branch to your fork. treat it as a backup.

        git push origin feature-xxx

5. code

  implement the new feature or the bug fix; include tests, and ensure they pass.

7. commit

  for every commit please write a short (max 72 characters) summary in the first line followed with a blank line and
  then more detailed descriptions of the change. Use Markdown syntax for simple styling. please include any
  issue number (in the format #nnn) in your summary.

        git commit -m "issue #123: Put change summary here (can be a issue title)"

  **NEVER leave the commit message blank!** Provide a detailed, clear, and complete description of your commit!

7. issue a Merge Request

  before submitting a [merge request](https://docs.gitlab.com/ce/workflow/forking_workflow.html#merging-upstream),
  update your branch to the latest code.

        git pull --rebase upstream develop

  if you have made many commits, we ask you to squash them into atomic units of work. most issues should have one commit
  only, especially bug fixes, which makes them easier to back port.

        git checkout develop
        git pull --rebase upstream develop
        git checkout feature-xxx
        git rebase -i develop

  push changes to your fork:

        git push -f

  in order to make a Merge Request,
  * navigate to your fork where you just pushed to (e.g. https://gitlab.com/<YourGitHubUserName>/<ThisRepositoryName>)
  * click "Merge Request".
  * write your branch name in the branch field (this is filled with "master" by default)
  * click "Update Commit Range".
  * ensure the changes you implemented are included in the "Commits" tab.
  * ensure that the "Files Changed" incorporate all of your changes.
  * fill in some details about your potential patch including a meaningful title.
  * click "New merge request".
  * in GitLab Issues, comment on your issue by linking to the URL of the pull request. a developer from the project 
    should move to Testing on the Issue Board.


  thanks for your contribution -- we'll get your merge request reviewed. you should also review other merge requests,
  just like other developers will review yours and comment on them. based on the comments, you should address them.
  once the reviewers approve, the maintainers will merge the code.


## Other Resources

* [General GitLab documentation](https://docs.gitlab.com/ce/)
* [GitLab workflow documentation](https://docs.gitlab.com/ce/workflow/README.html)
