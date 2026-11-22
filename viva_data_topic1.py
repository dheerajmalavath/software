"""
Viva Question and Answer Data Store containing 50 questions each for all 8 topics (400 questions total).
"""

# TOPIC 1: GIT & GITHUB (50 Questions)
GIT_QUESTIONS = [
    (
        "What is Version Control System (VCS), and what is the difference between CVCS and DVCS?",
        "A Version Control System (VCS) tracks changes to source code over time, allowing developers to review history, recall previous versions, and collaborate without overwriting each other's work.\n"
        "• Centralized VCS (CVCS, e.g. SVN, CVS): Relies on a single central server containing the entire repository history. If the central server goes down or network fails, developers cannot commit changes or view history.\n"
        "• Distributed VCS (DVCS, e.g. Git, Mercurial): Every developer's local machine contains a complete clone of the entire repository history. Developers can commit, branch, merge, and examine history completely offline, pushing updates to remotes when connected."
    ),
    (
        "What is the difference between Git and GitHub?",
        "Git is a distributed version control command-line software tool installed locally on an operating system (like Ubuntu) to record snapshots of code changes. "
        "GitHub is a cloud-based web hosting service for Git repositories that provides collaboration features including pull requests, code reviews, issue tracking, organization management, webhooks, and CI/CD pipelines (GitHub Actions)."
    ),
    (
        "What is a Git repository, and what is stored inside the .git directory?",
        "A Git repository is a directory containing project source files along with a hidden metadata folder named '.git'. "
        "The '.git' folder contains: (1) 'objects/' directory storing all blobs (file contents), trees (directory structures), commits, and annotated tags using SHA-1 hashes; "
        "(2) 'refs/' directory storing pointers to branches (heads) and tags; (3) 'HEAD' file pointing to current active branch/commit; and (4) 'config' file holding repository-specific configuration."
    ),
    (
        "Explain the three main states in Git: Working Directory, Staging Area (Index), and Git Repository.",
        "• Working Directory: The physical filesystem folder where you actively create, modify, and delete files.\n"
        "• Staging Area (Index): An intermediate holding file (at '.git/index') where changes are selected and reviewed via 'git add' before finalizing them into a commit.\n"
        "• Git Repository (.git folder): The permanent database where staged changes are safely recorded as immutable commit snapshots via 'git commit'."
    ),
    (
        "What does 'git init' do?",
        "The 'git init' command initializes a new empty Git repository in the current directory by creating the hidden '.git' metadata subdirectory. "
        "It sets up default branch references (usually 'main' or 'master') and configuration files, transforming a normal directory into a version-controlled repository."
    ),
    (
        "How do you configure author name and email globally in Git on Ubuntu?",
        "Run the following terminal commands:\n"
        "$ git config --global user.name \"dheerajmalavath\"\n"
        "$ git config --global user.email \"dheerajmalavath@gmail.com\"\n"
        "The '--global' flag writes these credentials to the user's home configuration file '~/.gitconfig', ensuring all future commits on the machine reflect this identity."
    ),
    (
        "What is 'git clone', and how does it differ from 'git init'?",
        "'git init' creates a blank repository from scratch locally on your machine. "
        "'git clone <url>' copies an existing remote repository (including full commit history, branches, and tags) from a remote server (like GitHub) to your local machine, and automatically configures a remote named 'origin' pointing back to the source URL."
    ),
    (
        "What is the difference between cloning via HTTPS vs SSH in GitHub?",
        "• HTTPS ('https://github.com/user/repo.git'): Uses standard SSL/TLS port 443. Requires authentication via GitHub Personal Access Tokens (PAT) since password authentication is deprecated.\n"
        "• SSH ('git@github.com:user/repo.git'): Uses public-key cryptography on port 22. Once the user's public key ('~/.ssh/id_ed25519.pub') is registered in GitHub settings, pushing and pulling happen securely and passwordlessly without entering tokens."
    ),
    (
        "How do you generate an SSH key on Ubuntu for GitHub authentication?",
        "In the Ubuntu terminal, execute:\n"
        "$ ssh-keygen -t ed25519 -C \"your.email@example.com\" -f ~/.ssh/id_ed25519 -N \"\"\n"
        "Then view and copy the public key:\n"
        "$ cat ~/.ssh/id_ed25519.pub\n"
        "Paste the output into GitHub → Settings → SSH and GPG Keys. Test with: $ ssh -T git@github.com."
    ),
    (
        "What is 'git status', and what information does it provide?",
        "'git status' displays the state of the working directory and staging area. It reports: (1) current branch name, (2) whether local branch is up-to-date, ahead, or behind remote tracking branch, "
        "(3) staged changes ready to be committed (green), (4) tracked files modified but not staged (red), and (5) untracked files not managed by Git."
    ),
    (
        "What is 'git add', and what is the difference between 'git add .' and 'git add -A'?",
        "'git add' stages changes from the working tree into the index.\n"
        "• 'git add .': Stages new and modified files in the current directory and its subdirectories, but in older Git versions may ignore deleted files in parent directories.\n"
        "• 'git add -A' (or 'git add --all'): Stages all changes across the entire repository root, including new, modified, and deleted files, regardless of current working directory."
    ),
    (
        "What is 'git commit', and why are atomic commits important?",
        "'git commit' captures a permanent snapshot of the staged changes in the Git history with a unique 40-character SHA-1/SHA-256 hash, author identity, timestamp, and message. "
        "Atomic commits mean each commit represents a single, complete, logical unit of work (e.g. one bugfix or one feature). Atomic commits ensure code bisecting, reviewing, and reverting can occur cleanly without breaking unintended features."
    ),
    (
        "What is the purpose of the '-m' flag in 'git commit'?",
        "The '-m' flag allows providing the commit message directly on the command line (e.g. 'git commit -m \"feat: add login validation\"'). "
        "If '-m' is omitted, Git automatically opens the configured terminal text editor (e.g. nano or vim) to prompt the user for a multi-line commit message."
    ),
    (
        "How do you amend the most recent commit using 'git commit --amend'?",
        "If you forgot to include a file or made a typo in the last commit message, stage the missing file with 'git add' and run:\n"
        "$ git commit --amend -m \"updated commit message\"\n"
        "This combines the staged changes with the previous commit and generates a new commit hash, replacing the previous commit."
    ),
    (
        "What is 'git log', and how do you view a concise graph history on Ubuntu?",
        "'git log' displays commit history in reverse chronological order. To view a clean, readable visual tree in Ubuntu terminal, run:\n"
        "$ git log --oneline --graph --decorate --all\n"
        "This shows each commit as a single line with abbreviated hash, branch/tag pointers, and graphical ASCII branch lines."
    ),
    (
        "What is 'git diff', and how does it differ from 'git diff --staged'?",
        "• 'git diff': Shows changes in the working tree that have NOT yet been staged with 'git add'.\n"
        "• 'git diff --staged' (or 'git diff --cached'): Shows changes that HAVE been staged into the index compared against the last commit (HEAD), representing what will go into the next commit."
    ),
    (
        "What is a Git branch, and how does Git implement branches under the hood?",
        "In Git, a branch is simply a lightweight, movable 41-byte pointer to a specific commit hash stored in '.git/refs/heads/<branch-name>'. "
        "Unlike other VCS systems that duplicate folders, creating or switching branches in Git is instantaneous and costs zero disk space because it merely updates or creates a text pointer file."
    ),
    (
        "How do you create and switch to a new branch using 'git checkout -b' vs 'git switch -c'?",
        "Both commands accomplish the same goal: creating and checking out a new branch.\n"
        "• Classic command: $ git checkout -b feature-login\n"
        "• Modern Git 2.23+ command: $ git switch -c feature-login\n"
        "'git switch' was introduced to separate branch switching from file restoring ('git restore'), preventing accidental overwriting of files."
    ),
    (
        "What is the difference between 'git merge' and 'git rebase'?",
        "• 'git merge': Integrates changes from one branch into another by creating a 3-way 'merge commit' that preserves complete historical timeline and branch divergence.\n"
        "• 'git rebase': Rewrites history by moving the base of your branch onto the latest commit of the target branch, re-applying your commits sequentially on top. This produces a perfectly linear commit history without merge bubbles."
    ),
    (
        "What is a Fast-Forward merge? When does it occur?",
        "A Fast-Forward merge occurs when there is a direct linear path from the target branch tip to the source branch tip (i.e. no divergent commits were made on the base branch). "
        "Git simply moves the branch pointer forward to point to the incoming commit without creating a separate merge commit."
    ),
    (
        "What is a 3-way merge?",
        "A 3-way merge occurs when both branches have diverged since their common ancestor commit. "
        "Git compares three snapshots: (1) Common Ancestor commit, (2) Tip of current branch (HEAD), and (3) Tip of incoming branch. Git automatically merges non-conflicting changes and creates a new 'merge commit' with two parent pointers."
    ),
    (
        "What causes a merge conflict in Git?",
        "A merge conflict occurs when two different branches have modified the exact same line(s) in a file differently, or when one branch modified a file that the other branch deleted. "
        "Because Git cannot determine which version takes precedence, it pauses the merge and inserts conflict markers for manual human resolution."
    ),
    (
        "How do you identify and resolve a merge conflict step-by-step in Ubuntu using nano?",
        "1. Git alerts: 'CONFLICT (content): Merge conflict in filename'.\n"
        "2. Open file in Ubuntu: $ nano filename\n"
        "3. Locate markers: '<<<<<<< HEAD' (current branch code), '=======' (separator), and '>>>>>>> branch' (incoming code).\n"
        "4. Edit text to final desired code and delete all conflict markers.\n"
        "5. Save in nano: Ctrl+O, Enter, Ctrl+X.\n"
        "6. Finalize merge: $ git add filename && git commit -m \"fix: resolve merge conflict\"."
    ),
    (
        "What are conflict markers (<<<<<<<, =======, >>>>>>>)?",
        "• '<<<<<<< HEAD': Marks the beginning of the conflicting code from your current checked-out branch.\n"
        "• '=======': Center separator dividing the two conflicting code blocks.\n"
        "• '>>>>>>> <branch_name>': Marks the end of the conflicting code from the branch being merged."
    ),
    (
        "How do you abort an in-progress merge conflict?",
        "Run: $ git merge --abort\n"
        "This completely cancels the merge operation and restores the working tree and staging area to the pristine state prior to running 'git merge'."
    ),
    (
        "What is 'git remote', and what does 'git remote -v' show?",
        "'git remote' manages connections to remote repositories. "
        "'git remote -v' lists the remote aliases along with their exact fetch and push URLs, typically showing 'origin  https://github.com/... (fetch)' and 'origin  https://github.com/... (push)'."
    ),
    (
        "What is the purpose of 'git remote add origin <url>'?",
        "It registers a new remote repository connection under the shorthand alias 'origin' pointing to the specified URL. "
        "This allows running shorthand commands like 'git push origin main' instead of typing the full URL each time."
    ),
    (
        "What does 'git push -u origin main' do? What is the '-u' flag?",
        "It pushes the local 'main' branch commits to the 'origin' remote repository. "
        "The '-u' (or '--set-upstream') flag links the local branch to the remote tracking branch 'origin/main'. "
        "Once set, future operations require only running bare 'git push' or 'git pull'."
    ),
    (
        "What is the difference between 'git fetch' and 'git pull'?",
        "• 'git fetch': Downloads commits, files, and refs from the remote repository to your local '.git' database without modifying your working files or moving current branch pointers.\n"
        "• 'git pull': Executes two commands in one: 'git fetch' followed immediately by 'git merge' to integrate remote changes into your active branch."
    ),
    (
        "What is a detached HEAD state in Git?",
        "A detached HEAD state occurs when HEAD points directly to a specific commit hash or remote tag rather than a local named branch pointer. "
        "Any commits made while in a detached HEAD state will not belong to any branch and risk being garbage collected unless explicitly saved into a new branch via 'git branch <new-branch>'."
    ),
    (
        "How do you undo changes in a working directory file before staging using 'git restore'?",
        "Run: $ git restore <filename>\n"
        "This discards uncommitted modifications in the working tree, reverting the file back to its state in the most recent commit (HEAD)."
    ),
    (
        "How do you unstage a file using 'git restore --staged'?",
        "Run: $ git restore --staged <filename>\n"
        "This removes the specified file from the staging area index without altering any modifications made inside the working tree file."
    ),
    (
        "What is the difference between 'git reset --soft', 'git reset --mixed', and 'git reset --hard'?",
        "• '--soft': Moves HEAD pointer back to target commit. Staged index and working directory remain unchanged.\n"
        "• '--mixed' (default): Moves HEAD pointer back and un-stages changes from the index. Working directory modifications are preserved.\n"
        "• '--hard': Moves HEAD pointer back AND wipes all changes from both staging area and working directory, discarding all work permanently."
    ),
    (
        "What is 'git revert', and how does it differ from 'git reset'?",
        "'git reset' rewrites commit history by moving branch pointers backward, which causes issues if commits were already pushed to shared remotes. "
        "'git revert <commit-hash>' creates a brand new commit that applies the exact inverse diff of the target commit, safely undoing changes without altering existing public history."
    ),
    (
        "What is 'git stash', and when should a developer use it?",
        "'git stash' takes modified, uncommitted tracked files in your working directory and saves them onto an internal stack, restoring your working tree to a clean HEAD state. "
        "It is used when you need to urgently switch branches or pull updates without committing half-finished, broken code."
    ),
    (
        "How do you list, apply, pop, and drop stashed changes?",
        "• $ git stash list — Displays all saved stash entries (e.g. stash@{0}, stash@{1}).\n"
        "• $ git stash apply — Re-applies changes from the topmost stash while keeping it on the stash stack.\n"
        "• $ git stash pop — Re-applies changes and immediately removes the stash entry from the stack.\n"
        "• $ git stash drop stash@{0} — Deletes a specific stash entry permanently."
    ),
    (
        "What is a .gitignore file, and why is it essential in DevOps?",
        "'.gitignore' is a text file listing patterns of filenames and folders that Git should deliberately ignore and never track. "
        "It prevents committing compiled binaries (target/, *.class), sensitive environment secrets (.env, *.pem), dependencies (node_modules/), and IDE temporary files (.settings/)."
    ),
    (
        "Can .gitignore ignore a file that has already been tracked and committed? How do you fix that?",
        "No. If a file is already tracked by Git, adding it to '.gitignore' will have no effect. "
        "To stop tracking it without deleting the physical file on disk, run:\n"
        "$ git rm --cached <filename>\n"
        "Then commit the removal: $ git commit -m \"chore: stop tracking cached file\"."
    ),
    (
        "What is a Git Tag? What is the difference between lightweight and annotated tags?",
        "A Git Tag is an immutable reference pointing to a specific commit, typically used to mark release versions (e.g. v1.0.0).\n"
        "• Lightweight Tag: A simple bookmark pointer to a commit hash (created with 'git tag v1.0').\n"
        "• Annotated Tag: A full Git object containing tagger name, email, date, GPG signature, and a release description message (created with 'git tag -a v1.0 -m \"Release v1.0\"')."
    ),
    (
        "How do you create, list, and push tags to GitHub?",
        "• Create tag: $ git tag -a v1.0.0 -m \"Production Release v1.0.0\"\n"
        "• List tags: $ git tag -l\n"
        "• Push single tag: $ git push origin v1.0.0\n"
        "• Push all tags: $ git push origin --tags"
    ),
    (
        "What is a Pull Request (PR) in GitHub?",
        "A Pull Request is a GitHub collaboration mechanism where a developer proposes changes from a feature branch to the repository maintainers. "
        "It provides a dedicated web interface for automated CI tests, line-by-line code review, discussions, and approval before merging into the main branch."
    ),
    (
        "What is the difference between Forking and Branching on GitHub?",
        "• Branching: Creates an isolated line of development inside the SAME repository. Used by internal team members with direct write access.\n"
        "• Forking: Creates an independent remote server-side CLONE of someone else's repository under your own GitHub account. Used in open-source development to propose pull requests without having write access to the upstream repository."
    ),
    (
        "What is a GitHub Organization, and how does it facilitate team collaboration?",
        "A GitHub Organization is a shared multi-user account designed for businesses and teams. "
        "It allows centralized administration of multiple repositories, role-based member permissions (Owners, Members, Billing), teams with specific access rights, and organization-level secrets and webhooks."
    ),
    (
        "What is a Git patch, and how do you create one with 'git format-patch'?",
        "A Git patch is a formatted Unix mbox file containing diffs, commit metadata, author information, and commit messages. "
        "To export the most recent commit as a patch in Ubuntu, run:\n"
        "$ git format-patch -1 HEAD\n"
        "This outputs a file named '0001-commit-subject.patch' suitable for sharing over email."
    ),
    (
        "How do you apply a Git patch in Ubuntu using 'git apply'?",
        "First check whether the patch applies cleanly without errors:\n"
        "$ git apply --check 0001-feature.patch\n"
        "If no errors are reported, apply the patch into the working directory:\n"
        "$ git apply 0001-feature.patch\n"
        "(Or use 'git am 0001-feature.patch' to apply and preserve commit author and timestamp metadata)."
    ),
    (
        "What is 'git cherry-pick', and when is it used?",
        "'git cherry-pick <commit-hash>' applies the changes from an existing commit on one branch directly onto your current branch, creating a new commit with the same diff. "
        "It is used to backport a specific bugfix from a development branch into a production release branch without merging the entire development branch."
    ),
    (
        "What is 'git blame', and what does it show?",
        "'git blame <filename>' annotates each line of a file with the author name, commit hash, and timestamp of the last commit that modified that specific line. "
        "It is used for code archaeology to understand why a line was written and who authored it."
    ),
    (
        "What is 'git reflog', and how can it recover deleted commits or branches?",
        "'git reflog' (Reference Log) records every movement of the HEAD pointer in your local repository (e.g. commits, resets, checkouts, rebase steps). "
        "Even if you accidentally execute 'git reset --hard' or delete a branch, the lost commit hash remains in reflog for ~30-90 days and can be recovered with 'git reset --hard HEAD@{n}'."
    ),
    (
        "What is a GitHub Webhook, and how does it notify CI/CD servers like Jenkins?",
        "A GitHub Webhook is an HTTP POST notification mechanism triggered by repository events (such as 'git push' or PR creation). "
        "GitHub automatically dispatches a JSON payload to a configured external listener URL (e.g. 'http://jenkins-server:9080/github-webhook/'), triggering automated builds without polling."
    ),
    (
        "What are GitHub Actions, and how do they relate to CI/CD?",
        "GitHub Actions is a built-in CI/CD and workflow automation platform on GitHub. Workflows are defined in YAML files under '.github/workflows/' "
        "and automatically run build, test, and container packaging tasks on virtual runners upon push or pull request events."
    )
]

print(f"Git questions compiled: {len(GIT_QUESTIONS)}")
