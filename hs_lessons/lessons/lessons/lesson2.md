#### Git revert

Earlier, we saw how the files in the staging area could be *restored* to an earlier version. This was when the changes
had not been committed. But what if we committed our changes and then decided to go back to the previous version? This
is exactly where the *revert* command comes into play. It helps to revert to another commit. Of course, to demonstrate
it, we need more than one commit. Therefore, let us create some more changes, commit them and then use this revert
feature to go back to an earlier commit.

To the *greet* function that we have been working, I added the another line to the welcome message. The greeting now
says - "Welcome, {name}! How are you doing today?". Thereafter, the commands, as explained previously, were executed in
the order - `git add code.py` `git commit -m "welcome msg edited with an introductory question"`. Use `git status` to
check if the git commands you issued worked or not. At the end, the staging area should be clear and we now have two
commits.

Now, for some reason, we do not like the existing welcome message and would like to go back (or *undo*) to the previous
version.