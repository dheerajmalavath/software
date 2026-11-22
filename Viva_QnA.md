# DevOps & Software Engineering Comprehensive Viva Guide
### 400 Technical Questions & In-Depth Explanations Across All 8 Core Syllabus Topics
#### KMIT Lab Internal II — Software Engineering (23CC501PC) · Ubuntu Linux

---


## Topic 1: Git & GitHub — Version Control & Collaboration (50 Questions)

### Q1. What is Version Control System (VCS), and what is the difference between CVCS and DVCS?
**Explanation & Answer:**

A Version Control System (VCS) tracks changes to source code over time, allowing developers to review history, recall previous versions, and collaborate without overwriting each other's work.
• Centralized VCS (CVCS, e.g. SVN, CVS): Relies on a single central server containing the entire repository history. If the central server goes down or network fails, developers cannot commit changes or view history.
• Distributed VCS (DVCS, e.g. Git, Mercurial): Every developer's local machine contains a complete clone of the entire repository history. Developers can commit, branch, merge, and examine history completely offline, pushing updates to remotes when connected.

---

### Q2. What is the difference between Git and GitHub?
**Explanation & Answer:**

Git is a distributed version control command-line software tool installed locally on an operating system (like Ubuntu) to record snapshots of code changes. GitHub is a cloud-based web hosting service for Git repositories that provides collaboration features including pull requests, code reviews, issue tracking, organization management, webhooks, and CI/CD pipelines (GitHub Actions).

---

### Q3. What is a Git repository, and what is stored inside the .git directory?
**Explanation & Answer:**

A Git repository is a directory containing project source files along with a hidden metadata folder named '.git'. The '.git' folder contains: (1) 'objects/' directory storing all blobs (file contents), trees (directory structures), commits, and annotated tags using SHA-1 hashes; (2) 'refs/' directory storing pointers to branches (heads) and tags; (3) 'HEAD' file pointing to current active branch/commit; and (4) 'config' file holding repository-specific configuration.

---

### Q4. Explain the three main states in Git: Working Directory, Staging Area (Index), and Git Repository.
**Explanation & Answer:**

• Working Directory: The physical filesystem folder where you actively create, modify, and delete files.
• Staging Area (Index): An intermediate holding file (at '.git/index') where changes are selected and reviewed via 'git add' before finalizing them into a commit.
• Git Repository (.git folder): The permanent database where staged changes are safely recorded as immutable commit snapshots via 'git commit'.

---

### Q5. What does 'git init' do?
**Explanation & Answer:**

The 'git init' command initializes a new empty Git repository in the current directory by creating the hidden '.git' metadata subdirectory. It sets up default branch references (usually 'main' or 'master') and configuration files, transforming a normal directory into a version-controlled repository.

---

### Q6. How do you configure author name and email globally in Git on Ubuntu?
**Explanation & Answer:**

Run the following terminal commands:
$ git config --global user.name "dheerajmalavath"
$ git config --global user.email "dheerajmalavath@gmail.com"
The '--global' flag writes these credentials to the user's home configuration file '~/.gitconfig', ensuring all future commits on the machine reflect this identity.

---

### Q7. What is 'git clone', and how does it differ from 'git init'?
**Explanation & Answer:**

'git init' creates a blank repository from scratch locally on your machine. 'git clone <url>' copies an existing remote repository (including full commit history, branches, and tags) from a remote server (like GitHub) to your local machine, and automatically configures a remote named 'origin' pointing back to the source URL.

---

### Q8. What is the difference between cloning via HTTPS vs SSH in GitHub?
**Explanation & Answer:**

• HTTPS ('https://github.com/user/repo.git'): Uses standard SSL/TLS port 443. Requires authentication via GitHub Personal Access Tokens (PAT) since password authentication is deprecated.
• SSH ('git@github.com:user/repo.git'): Uses public-key cryptography on port 22. Once the user's public key ('~/.ssh/id_ed25519.pub') is registered in GitHub settings, pushing and pulling happen securely and passwordlessly without entering tokens.

---

### Q9. How do you generate an SSH key on Ubuntu for GitHub authentication?
**Explanation & Answer:**

In the Ubuntu terminal, execute:
$ ssh-keygen -t ed25519 -C "your.email@example.com" -f ~/.ssh/id_ed25519 -N ""
Then view and copy the public key:
$ cat ~/.ssh/id_ed25519.pub
Paste the output into GitHub → Settings → SSH and GPG Keys. Test with: $ ssh -T git@github.com.

---

### Q10. What is 'git status', and what information does it provide?
**Explanation & Answer:**

'git status' displays the state of the working directory and staging area. It reports: (1) current branch name, (2) whether local branch is up-to-date, ahead, or behind remote tracking branch, (3) staged changes ready to be committed (green), (4) tracked files modified but not staged (red), and (5) untracked files not managed by Git.

---

### Q11. What is 'git add', and what is the difference between 'git add .' and 'git add -A'?
**Explanation & Answer:**

'git add' stages changes from the working tree into the index.
• 'git add .': Stages new and modified files in the current directory and its subdirectories, but in older Git versions may ignore deleted files in parent directories.
• 'git add -A' (or 'git add --all'): Stages all changes across the entire repository root, including new, modified, and deleted files, regardless of current working directory.

---

### Q12. What is 'git commit', and why are atomic commits important?
**Explanation & Answer:**

'git commit' captures a permanent snapshot of the staged changes in the Git history with a unique 40-character SHA-1/SHA-256 hash, author identity, timestamp, and message. Atomic commits mean each commit represents a single, complete, logical unit of work (e.g. one bugfix or one feature). Atomic commits ensure code bisecting, reviewing, and reverting can occur cleanly without breaking unintended features.

---

### Q13. What is the purpose of the '-m' flag in 'git commit'?
**Explanation & Answer:**

The '-m' flag allows providing the commit message directly on the command line (e.g. 'git commit -m "feat: add login validation"'). If '-m' is omitted, Git automatically opens the configured terminal text editor (e.g. nano or vim) to prompt the user for a multi-line commit message.

---

### Q14. How do you amend the most recent commit using 'git commit --amend'?
**Explanation & Answer:**

If you forgot to include a file or made a typo in the last commit message, stage the missing file with 'git add' and run:
$ git commit --amend -m "updated commit message"
This combines the staged changes with the previous commit and generates a new commit hash, replacing the previous commit.

---

### Q15. What is 'git log', and how do you view a concise graph history on Ubuntu?
**Explanation & Answer:**

'git log' displays commit history in reverse chronological order. To view a clean, readable visual tree in Ubuntu terminal, run:
$ git log --oneline --graph --decorate --all
This shows each commit as a single line with abbreviated hash, branch/tag pointers, and graphical ASCII branch lines.

---

### Q16. What is 'git diff', and how does it differ from 'git diff --staged'?
**Explanation & Answer:**

• 'git diff': Shows changes in the working tree that have NOT yet been staged with 'git add'.
• 'git diff --staged' (or 'git diff --cached'): Shows changes that HAVE been staged into the index compared against the last commit (HEAD), representing what will go into the next commit.

---

### Q17. What is a Git branch, and how does Git implement branches under the hood?
**Explanation & Answer:**

In Git, a branch is simply a lightweight, movable 41-byte pointer to a specific commit hash stored in '.git/refs/heads/<branch-name>'. Unlike other VCS systems that duplicate folders, creating or switching branches in Git is instantaneous and costs zero disk space because it merely updates or creates a text pointer file.

---

### Q18. How do you create and switch to a new branch using 'git checkout -b' vs 'git switch -c'?
**Explanation & Answer:**

Both commands accomplish the same goal: creating and checking out a new branch.
• Classic command: $ git checkout -b feature-login
• Modern Git 2.23+ command: $ git switch -c feature-login
'git switch' was introduced to separate branch switching from file restoring ('git restore'), preventing accidental overwriting of files.

---

### Q19. What is the difference between 'git merge' and 'git rebase'?
**Explanation & Answer:**

• 'git merge': Integrates changes from one branch into another by creating a 3-way 'merge commit' that preserves complete historical timeline and branch divergence.
• 'git rebase': Rewrites history by moving the base of your branch onto the latest commit of the target branch, re-applying your commits sequentially on top. This produces a perfectly linear commit history without merge bubbles.

---

### Q20. What is a Fast-Forward merge? When does it occur?
**Explanation & Answer:**

A Fast-Forward merge occurs when there is a direct linear path from the target branch tip to the source branch tip (i.e. no divergent commits were made on the base branch). Git simply moves the branch pointer forward to point to the incoming commit without creating a separate merge commit.

---

### Q21. What is a 3-way merge?
**Explanation & Answer:**

A 3-way merge occurs when both branches have diverged since their common ancestor commit. Git compares three snapshots: (1) Common Ancestor commit, (2) Tip of current branch (HEAD), and (3) Tip of incoming branch. Git automatically merges non-conflicting changes and creates a new 'merge commit' with two parent pointers.

---

### Q22. What causes a merge conflict in Git?
**Explanation & Answer:**

A merge conflict occurs when two different branches have modified the exact same line(s) in a file differently, or when one branch modified a file that the other branch deleted. Because Git cannot determine which version takes precedence, it pauses the merge and inserts conflict markers for manual human resolution.

---

### Q23. How do you identify and resolve a merge conflict step-by-step in Ubuntu using nano?
**Explanation & Answer:**

1. Git alerts: 'CONFLICT (content): Merge conflict in filename'.
2. Open file in Ubuntu: $ nano filename
3. Locate markers: '<<<<<<< HEAD' (current branch code), '=======' (separator), and '>>>>>>> branch' (incoming code).
4. Edit text to final desired code and delete all conflict markers.
5. Save in nano: Ctrl+O, Enter, Ctrl+X.
6. Finalize merge: $ git add filename && git commit -m "fix: resolve merge conflict".

---

### Q24. What are conflict markers (<<<<<<<, =======, >>>>>>>)?
**Explanation & Answer:**

• '<<<<<<< HEAD': Marks the beginning of the conflicting code from your current checked-out branch.
• '=======': Center separator dividing the two conflicting code blocks.
• '>>>>>>> <branch_name>': Marks the end of the conflicting code from the branch being merged.

---

### Q25. How do you abort an in-progress merge conflict?
**Explanation & Answer:**

Run: $ git merge --abort
This completely cancels the merge operation and restores the working tree and staging area to the pristine state prior to running 'git merge'.

---

### Q26. What is 'git remote', and what does 'git remote -v' show?
**Explanation & Answer:**

'git remote' manages connections to remote repositories. 'git remote -v' lists the remote aliases along with their exact fetch and push URLs, typically showing 'origin  https://github.com/... (fetch)' and 'origin  https://github.com/... (push)'.

---

### Q27. What is the purpose of 'git remote add origin <url>'?
**Explanation & Answer:**

It registers a new remote repository connection under the shorthand alias 'origin' pointing to the specified URL. This allows running shorthand commands like 'git push origin main' instead of typing the full URL each time.

---

### Q28. What does 'git push -u origin main' do? What is the '-u' flag?
**Explanation & Answer:**

It pushes the local 'main' branch commits to the 'origin' remote repository. The '-u' (or '--set-upstream') flag links the local branch to the remote tracking branch 'origin/main'. Once set, future operations require only running bare 'git push' or 'git pull'.

---

### Q29. What is the difference between 'git fetch' and 'git pull'?
**Explanation & Answer:**

• 'git fetch': Downloads commits, files, and refs from the remote repository to your local '.git' database without modifying your working files or moving current branch pointers.
• 'git pull': Executes two commands in one: 'git fetch' followed immediately by 'git merge' to integrate remote changes into your active branch.

---

### Q30. What is a detached HEAD state in Git?
**Explanation & Answer:**

A detached HEAD state occurs when HEAD points directly to a specific commit hash or remote tag rather than a local named branch pointer. Any commits made while in a detached HEAD state will not belong to any branch and risk being garbage collected unless explicitly saved into a new branch via 'git branch <new-branch>'.

---

### Q31. How do you undo changes in a working directory file before staging using 'git restore'?
**Explanation & Answer:**

Run: $ git restore <filename>
This discards uncommitted modifications in the working tree, reverting the file back to its state in the most recent commit (HEAD).

---

### Q32. How do you unstage a file using 'git restore --staged'?
**Explanation & Answer:**

Run: $ git restore --staged <filename>
This removes the specified file from the staging area index without altering any modifications made inside the working tree file.

---

### Q33. What is the difference between 'git reset --soft', 'git reset --mixed', and 'git reset --hard'?
**Explanation & Answer:**

• '--soft': Moves HEAD pointer back to target commit. Staged index and working directory remain unchanged.
• '--mixed' (default): Moves HEAD pointer back and un-stages changes from the index. Working directory modifications are preserved.
• '--hard': Moves HEAD pointer back AND wipes all changes from both staging area and working directory, discarding all work permanently.

---

### Q34. What is 'git revert', and how does it differ from 'git reset'?
**Explanation & Answer:**

'git reset' rewrites commit history by moving branch pointers backward, which causes issues if commits were already pushed to shared remotes. 'git revert <commit-hash>' creates a brand new commit that applies the exact inverse diff of the target commit, safely undoing changes without altering existing public history.

---

### Q35. What is 'git stash', and when should a developer use it?
**Explanation & Answer:**

'git stash' takes modified, uncommitted tracked files in your working directory and saves them onto an internal stack, restoring your working tree to a clean HEAD state. It is used when you need to urgently switch branches or pull updates without committing half-finished, broken code.

---

### Q36. How do you list, apply, pop, and drop stashed changes?
**Explanation & Answer:**

• $ git stash list — Displays all saved stash entries (e.g. stash@{0}, stash@{1}).
• $ git stash apply — Re-applies changes from the topmost stash while keeping it on the stash stack.
• $ git stash pop — Re-applies changes and immediately removes the stash entry from the stack.
• $ git stash drop stash@{0} — Deletes a specific stash entry permanently.

---

### Q37. What is a .gitignore file, and why is it essential in DevOps?
**Explanation & Answer:**

'.gitignore' is a text file listing patterns of filenames and folders that Git should deliberately ignore and never track. It prevents committing compiled binaries (target/, *.class), sensitive environment secrets (.env, *.pem), dependencies (node_modules/), and IDE temporary files (.settings/).

---

### Q38. Can .gitignore ignore a file that has already been tracked and committed? How do you fix that?
**Explanation & Answer:**

No. If a file is already tracked by Git, adding it to '.gitignore' will have no effect. To stop tracking it without deleting the physical file on disk, run:
$ git rm --cached <filename>
Then commit the removal: $ git commit -m "chore: stop tracking cached file".

---

### Q39. What is a Git Tag? What is the difference between lightweight and annotated tags?
**Explanation & Answer:**

A Git Tag is an immutable reference pointing to a specific commit, typically used to mark release versions (e.g. v1.0.0).
• Lightweight Tag: A simple bookmark pointer to a commit hash (created with 'git tag v1.0').
• Annotated Tag: A full Git object containing tagger name, email, date, GPG signature, and a release description message (created with 'git tag -a v1.0 -m "Release v1.0"').

---

### Q40. How do you create, list, and push tags to GitHub?
**Explanation & Answer:**

• Create tag: $ git tag -a v1.0.0 -m "Production Release v1.0.0"
• List tags: $ git tag -l
• Push single tag: $ git push origin v1.0.0
• Push all tags: $ git push origin --tags

---

### Q41. What is a Pull Request (PR) in GitHub?
**Explanation & Answer:**

A Pull Request is a GitHub collaboration mechanism where a developer proposes changes from a feature branch to the repository maintainers. It provides a dedicated web interface for automated CI tests, line-by-line code review, discussions, and approval before merging into the main branch.

---

### Q42. What is the difference between Forking and Branching on GitHub?
**Explanation & Answer:**

• Branching: Creates an isolated line of development inside the SAME repository. Used by internal team members with direct write access.
• Forking: Creates an independent remote server-side CLONE of someone else's repository under your own GitHub account. Used in open-source development to propose pull requests without having write access to the upstream repository.

---

### Q43. What is a GitHub Organization, and how does it facilitate team collaboration?
**Explanation & Answer:**

A GitHub Organization is a shared multi-user account designed for businesses and teams. It allows centralized administration of multiple repositories, role-based member permissions (Owners, Members, Billing), teams with specific access rights, and organization-level secrets and webhooks.

---

### Q44. What is a Git patch, and how do you create one with 'git format-patch'?
**Explanation & Answer:**

A Git patch is a formatted Unix mbox file containing diffs, commit metadata, author information, and commit messages. To export the most recent commit as a patch in Ubuntu, run:
$ git format-patch -1 HEAD
This outputs a file named '0001-commit-subject.patch' suitable for sharing over email.

---

### Q45. How do you apply a Git patch in Ubuntu using 'git apply'?
**Explanation & Answer:**

First check whether the patch applies cleanly without errors:
$ git apply --check 0001-feature.patch
If no errors are reported, apply the patch into the working directory:
$ git apply 0001-feature.patch
(Or use 'git am 0001-feature.patch' to apply and preserve commit author and timestamp metadata).

---

### Q46. What is 'git cherry-pick', and when is it used?
**Explanation & Answer:**

'git cherry-pick <commit-hash>' applies the changes from an existing commit on one branch directly onto your current branch, creating a new commit with the same diff. It is used to backport a specific bugfix from a development branch into a production release branch without merging the entire development branch.

---

### Q47. What is 'git blame', and what does it show?
**Explanation & Answer:**

'git blame <filename>' annotates each line of a file with the author name, commit hash, and timestamp of the last commit that modified that specific line. It is used for code archaeology to understand why a line was written and who authored it.

---

### Q48. What is 'git reflog', and how can it recover deleted commits or branches?
**Explanation & Answer:**

'git reflog' (Reference Log) records every movement of the HEAD pointer in your local repository (e.g. commits, resets, checkouts, rebase steps). Even if you accidentally execute 'git reset --hard' or delete a branch, the lost commit hash remains in reflog for ~30-90 days and can be recovered with 'git reset --hard HEAD@{n}'.

---

### Q49. What is a GitHub Webhook, and how does it notify CI/CD servers like Jenkins?
**Explanation & Answer:**

A GitHub Webhook is an HTTP POST notification mechanism triggered by repository events (such as 'git push' or PR creation). GitHub automatically dispatches a JSON payload to a configured external listener URL (e.g. 'http://jenkins-server:9080/github-webhook/'), triggering automated builds without polling.

---

### Q50. What are GitHub Actions, and how do they relate to CI/CD?
**Explanation & Answer:**

GitHub Actions is a built-in CI/CD and workflow automation platform on GitHub. Workflows are defined in YAML files under '.github/workflows/' and automatically run build, test, and container packaging tasks on virtual runners upon push or pull request events.

---


## Topic 2: Apache Maven & Eclipse IDE Build Automation (50 Questions)

### Q1. What is Apache Maven?
**Explanation & Answer:**

Apache Maven is an open-source build automation and project comprehension tool primarily used for Java projects. It standardizes project structures, automatically manages external dependencies via repositories, executes automated tests, and packages applications into distributable formats such as JAR or WAR files based on a central Project Object Model (pom.xml).

---

### Q2. What are the key advantages of Maven over traditional build tools like Ant or manual JAR management?
**Explanation & Answer:**

• Declarative Build: Configuration over coding; developers describe 'what' to build in XML rather than writing explicit imperative scripts.
• Dependency Management: Automatically downloads transitive dependencies and caches them locally, preventing 'JAR hell'.
• Standardized Project Layout: Every Maven project adheres to the exact same folder structure, making onboarding seamless.
• Rich Plugin Ecosystem: Out-of-the-box integration for compilation, testing, packaging, code quality, and deployment.

---

### Q3. What is a POM (Project Object Model) and what is pom.xml?
**Explanation & Answer:**

The Project Object Model (POM) is the core unit of configuration in Maven. 'pom.xml' is the XML file in the root directory that contains all project configuration data, including GroupId, ArtifactId, Version (GAV), dependencies, build plugins, compile goals, profiles, and project metadata.

---

### Q4. What is GAV in Maven? Explain GroupId, ArtifactId, and Version.
**Explanation & Answer:**

GAV uniquely identifies a Maven artifact worldwide across all repositories:
• GroupId: Identifies the organization or domain creating the project (e.g. 'com.example' or 'org.apache.commons').
• ArtifactId: The specific name of the project library or application (e.g. 'oltrs-app' or 'commons-lang3').
• Version: The current release version (e.g. '1.0.0' for stable releases or '1.0-SNAPSHOT' for active development).

---

### Q5. What are the standard Maven build lifecycles? (Clean, Default, Site)
**Explanation & Answer:**

Maven provides three built-in build lifecycles:
1. Clean Lifecycle: Handles project cleanup and artifact deletion (phases: pre-clean, clean, post-clean).
2. Default (Build) Lifecycle: Handles code compilation, testing, packaging, and deployment (23 sequential phases).
3. Site Lifecycle: Handles creation and deployment of project documentation and reports (phases: site, site-deploy).

---

### Q6. What are the phases in the Maven default build lifecycle?
**Explanation & Answer:**

The primary sequential phases in the default lifecycle are:
1. validate: Validates project structure and required configuration information.
2. compile: Compiles Java source code into bytecode (.class files).
3. test: Runs unit tests (using JUnit/TestNG) without packaging.
4. package: Packages compiled code into JAR or WAR format in the target/ folder.
5. verify: Runs integration tests to ensure quality checks are met.
6. install: Installs the package into local repository (~/.m2/repository).
7. deploy: Copies final package to remote repository for sharing across teams.

---

### Q7. What is the difference between a Maven lifecycle, phase, and goal?
**Explanation & Answer:**

• Lifecycle: A high-level sequence of steps (Clean, Default, Site).
• Phase: A distinct stage within a lifecycle (e.g. 'compile', 'test', 'package'). Executing a phase automatically runs all preceding phases.
• Goal: A specific executable task bound to a phase, provided by a plugin (e.g. 'compiler:compile' bound to compile phase, 'surefire:test' bound to test phase).

---

### Q8. Explain the function of 'mvn clean'.
**Explanation & Answer:**

'mvn clean' invokes the clean lifecycle, deleting the entire build output directory ('target/') on disk. This ensures that subsequent compilation runs are completely clean and do not use stale bytecode or outdated resources.

---

### Q9. Explain the function of 'mvn compile'.
**Explanation & Answer:**

'mvn compile' runs validation, copies resources from 'src/main/resources' to 'target/classes', and invokes the 'maven-compiler-plugin' to compile all Java source files under 'src/main/java' into bytecode (.class files) inside 'target/classes/'.

---

### Q10. Explain the function of 'mvn test'.
**Explanation & Answer:**

'mvn test' compiles the application source code, compiles test sources under 'src/test/java', and executes unit test cases using the Surefire plugin, outputting test execution reports and XML summaries into 'target/surefire-reports/'.

---

### Q11. Explain the function of 'mvn package'.
**Explanation & Answer:**

'mvn package' compiles code, runs all unit tests, and packages the compiled classes and web resources into the distributable archive specified in pom.xml ('<packaging>war</packaging>' or '<packaging>jar</packaging>') inside the 'target/' folder.

---

### Q12. Explain the function of 'mvn install'.
**Explanation & Answer:**

'mvn install' executes all phases up to 'package' and then copies the resulting JAR or WAR artifact into the local Maven repository (on Ubuntu at '~/.m2/repository/<groupId>/<artifactId>/<version>/'). This makes the artifact immediately accessible as a dependency to other local Maven projects.

---

### Q13. Explain the function of 'mvn deploy'.
**Explanation & Answer:**

'mvn deploy' is the final phase of the default lifecycle. It copies the finished build package to an external, shared remote repository (such as Nexus, Artifactory, or AWS CodeArtifact) to allow other team members and production servers to download it.

---

### Q14. What is the difference between 'mvn package' and 'mvn install'?
**Explanation & Answer:**

'mvn package' only generates the archive (.jar/.war) locally inside the project's own 'target/' directory. 'mvn install' generates the archive AND installs it into your user's global local repository cache ('~/.m2/repository'), making it available for other projects on your machine.

---

### Q15. What is the standard directory structure of a Maven project?
**Explanation & Answer:**

• 'src/main/java': Production Java source files.
• 'src/main/resources': Production properties and configuration files.
• 'src/main/webapp': Web application resources (WEB-INF/web.xml, JSP, HTML, CSS).
• 'src/test/java': Unit test classes.
• 'src/test/resources': Test-specific configurations.
• 'target/': Generated build output directory.
• 'pom.xml': Maven configuration file in root directory.

---

### Q16. Why does Maven enforce a standard directory structure?
**Explanation & Answer:**

Convention over Configuration. By enforcing a standard structure, any Java developer can open any Maven project and instantly know where source code, tests, and configuration files reside, eliminating the need to write custom build scripts specifying source directories.

---

### Q17. What is the purpose of 'src/main/resources'?
**Explanation & Answer:**

It stores application configuration files (such as 'application.properties', 'log4j.properties', 'hibernate.cfg.xml', or database credentials). During compilation, Maven automatically copies all files from this directory directly into 'target/classes/', placing them at the root of the runtime classpath.

---

### Q18. What is the purpose of 'src/main/webapp' in web applications?
**Explanation & Answer:**

In Maven web projects (with '<packaging>war</packaging>'), 'src/main/webapp' represents the root of the web archive. It contains static web assets (HTML, CSS, JS, JSP) and the protected 'WEB-INF/' folder containing 'web.xml' (Deployment Descriptor).

---

### Q19. What is the local repository in Maven, and where is it located on Ubuntu?
**Explanation & Answer:**

The local repository is a directory on the developer's computer where Maven stores and caches downloaded remote dependencies, plugins, and locally installed artifacts. On Ubuntu Linux, it is located at: '~/.m2/repository/'.

---

### Q20. What is the Maven Central Repository?
**Explanation & Answer:**

Maven Central (repo.maven.apache.org) is the default public remote repository maintained by the Maven community. It contains hundreds of thousands of open-source Java libraries, dependencies, and plugins that Maven searches and downloads automatically.

---

### Q21. What is a Remote Repository in Maven?
**Explanation & Answer:**

A remote repository is an external server (such as an internal corporate repository hosted on Nexus or Artifactory) configured in 'pom.xml' or 'settings.xml' to host private proprietary libraries and mirror public dependencies for faster team downloads.

---

### Q22. In what order does Maven search for dependencies?
**Explanation & Answer:**

1. Local Repository ('~/.m2/repository'): Checks local cache first. If found, uses it immediately.
2. Central Repository: If not in local cache, searches Maven Central.
3. Remote Repositories: If defined in pom.xml, searches external enterprise repositories in listed order.
Once downloaded, Maven caches the dependency in the local repository for future offline use.

---

### Q23. What is a Maven Archetype?
**Explanation & Answer:**

An Archetype is a Maven project templating toolkit. It provides a standardized skeleton and generates pre-configured directory layouts and sample files for specific types of projects (such as standalone console applications, webapps, or Spring Boot services).

---

### Q24. What is 'maven-archetype-quickstart', and what files does it generate?
**Explanation & Answer:**

'maven-archetype-quickstart' generates a minimal standard Java application skeleton. It creates: (1) 'src/main/java/com/example/App.java' (containing main method printing Hello World), (2) 'src/test/java/com/example/AppTest.java' (sample JUnit test case), and (3) a basic 'pom.xml' with JUnit dependency.

---

### Q25. What is 'maven-archetype-webapp', and what files does it generate?
**Explanation & Answer:**

'maven-archetype-webapp' generates a standard Java Web Application skeleton for deployment to servlet containers like Tomcat. It generates: (1) 'src/main/webapp/WEB-INF/web.xml', (2) 'src/main/webapp/index.jsp', and (3) 'pom.xml' with '<packaging>war</packaging>'.

---

### Q26. How do you create a Maven project in Eclipse IDE step-by-step?
**Explanation & Answer:**

1. Open Eclipse → File → New → Other... → Maven → Maven Project → Click Next.
2. Select workspace location → Click Next.
3. Filter archetype by 'quickstart' or 'webapp' → Select 'maven-archetype-quickstart' → Click Next.
4. Enter Group Id ('com.example'), Artifact Id ('my-app'), Version ('1.0-SNAPSHOT'), Package ('com.example').
5. Click Finish. When prompted in Console with Y/N, type 'Y' and press Enter to generate project.

---

### Q27. How do you import an existing Maven project into Eclipse?
**Explanation & Answer:**

1. Open Eclipse → File → Import...
2. Expand 'Maven' folder → Select 'Existing Maven Projects' → Click Next.
3. Click 'Browse...' and select the project root directory containing 'pom.xml'.
4. Ensure checkbox for 'pom.xml' is checked → Click Finish. Eclipse automatically resolves dependencies.

---

### Q28. What does 'Maven -> Update Project' (Alt+F5) do in Eclipse?
**Explanation & Answer:**

Right-clicking a project in Eclipse and selecting Maven → Update Project (Alt+F5) forces Eclipse to re-read 'pom.xml', re-synchronize dependencies, download missing JARs into the local cache, update the Java build path, and apply compiler plugin settings.

---

### Q29. How do you run Maven Clean, Install, and Test inside Eclipse UI?
**Explanation & Answer:**

• Maven Clean: Right-click project or pom.xml → Run As → Maven Clean.
• Maven Install: Right-click project or pom.xml → Run As → Maven Install.
• Maven Test: Right-click project or pom.xml → Run As → Maven Test.
Console output displays build logs and 'BUILD SUCCESS'.

---

### Q30. How do you configure custom Maven goals in Eclipse Run Configurations?
**Explanation & Answer:**

1. Right-click project → Run As → Maven Build...
2. In the Edit Configuration dialog, in the 'Goals' text box, type: 'clean install -DskipTests'.
3. Click 'Apply' and click 'Run'. This configuration is saved under Run Configurations for one-click re-execution.

---

### Q31. What is a dependency in pom.xml?
**Explanation & Answer:**

A dependency is an external library required by the project to compile, test, or execute. It is declared inside the '<dependencies>' tag using GroupId, ArtifactId, Version (GAV), and optional Scope.

---

### Q32. What is dependency scope in Maven? (compile, provided, runtime, test, system)
**Explanation & Answer:**

• 'compile' (default): Available on all classpaths (compile, test, runtime) and packaged into final artifact.
• 'provided': Required for compilation and test, but expected to be provided by JDK or container (e.g. Servlet API provided by Tomcat at runtime).
• 'runtime': Needed for execution but not compilation (e.g. JDBC database drivers).
• 'test': Only available during test compilation and test execution (e.g. JUnit, Mockito); not packaged into production JAR/WAR.
• 'system': Similar to provided, but requires an explicit system path to a local JAR on disk.

---

### Q33. What is transitive dependency, and how does Maven resolve dependency conflicts?
**Explanation & Answer:**

A transitive dependency occurs when Project A depends on Library B, and Library B depends on Library C. Maven automatically includes Library C on the classpath. If two libraries depend on conflicting versions of Library C, Maven resolves conflicts using the 'Nearest Definition' rule.

---

### Q34. What is the 'nearest definition' rule in Maven dependency mediation?
**Explanation & Answer:**

Maven chooses the dependency version that is closest to your project in the dependency tree. If Project A -> B -> C (v1.0) and Project A -> D -> E -> C (v2.0), Maven selects C v1.0 because it is 2 levels deep, whereas C v2.0 is 3 levels deep.

---

### Q35. What is dependency exclusion (<exclusions>), and when is it needed?
**Explanation & Answer:**

An exclusion tag ('<exclusions>') inside a '<dependency>' tells Maven NOT to pull in a specific transitive dependency. It is needed when a transitive dependency has a known security vulnerability, causes a classpath collision, or conflicts with a newer version explicitly declared.

---

### Q36. What is a Maven Plugin, and how does it differ from a dependency?
**Explanation & Answer:**

A dependency is a library containing classes that your application source code calls at runtime. A plugin is an executable extension to Maven itself that performs actions during the build process (e.g. compiling Java files, creating WAR files, executing tests, or generating reports).

---

### Q37. What is the role of maven-compiler-plugin?
**Explanation & Answer:**

The 'maven-compiler-plugin' compiles the Java source code of the project. It allows configuring the source and target Java bytecode compatibility versions (e.g. Java 17) and passing compiler arguments to the javac compiler.

---

### Q38. How do you configure the Java version (e.g. Java 17) in maven-compiler-plugin?
**Explanation & Answer:**

In 'pom.xml' inside '<build><plugins>':
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.11.0</version>
  <configuration>
    <source>17</source>
    <target>17</target>
  </configuration>
</plugin>

---

### Q39. What is maven-surefire-plugin?
**Explanation & Answer:**

The Surefire plugin executes unit tests during the 'test' phase of the build lifecycle. It automatically finds and runs test classes matching '**/*Test.java', '**/Test*.java', or '**/*TestCase.java', generating test reports in TXT and XML formats.

---

### Q40. What is maven-war-plugin?
**Explanation & Answer:**

The WAR plugin packages web applications into Web Application Archive (.war) files. It bundles compiled classes from 'target/classes/', web assets from 'src/main/webapp/', and external dependencies into 'WEB-INF/lib/'.

---

### Q41. What is maven-jar-plugin, and how do you configure the main class in the manifest?
**Explanation & Answer:**

The JAR plugin builds standard Java Archive (.jar) files. To make the JAR directly executable via 'java -jar app.jar', configure the main class in the manifest:
<configuration>
  <archive>
    <manifest>
      <mainClass>com.example.App</mainClass>
    </manifest>
  </archive>
</configuration>

---

### Q42. How do you skip test execution during a Maven build in Ubuntu terminal?
**Explanation & Answer:**

Execute either of the following commands:
$ mvn clean package -DskipTests
(Compiles tests but skips execution).
$ mvn clean package -Dmaven.test.skip=true
(Skips both test compilation and test execution).

---

### Q43. How do you run only a specific test class or test method using Maven CLI?
**Explanation & Answer:**

Use the '-Dtest' parameter:
• Single test class: $ mvn test -Dtest=AppTest
• Specific test method: $ mvn test -Dtest=AppTest#testLoginSuccess
• Wildcard pattern: $ mvn test -Dtest=*ValidationTest

---

### Q44. How do you troubleshoot Maven build failures using debug mode? (The -X switch)
**Explanation & Answer:**

Run the build command appending the '-X' switch:
$ mvn clean package -X
This enables full verbose debug output, printing classpaths, detailed stack traces, exact URLs checked during dependency resolution, and plugin execution internals.

---

### Q45. What causes the 'Unsupported class version error' in Maven, and how do you fix it?
**Explanation & Answer:**

Cause: The Java bytecode was compiled targeting a newer Java version (e.g. Java 17 = version 61.0) than the Java Runtime Environment (JRE) running the application (e.g. Java 11 = version 55.0).
Fix: Align the compiler plugin '<source>' and '<target>' in pom.xml to match the installed runtime JRE, or upgrade the runtime Java version on Ubuntu using 'sudo update-alternatives --config java'.

---

### Q46. What causes 'Failed to execute goal maven-compiler-plugin:compile', and how do you resolve it?
**Explanation & Answer:**

Common Causes: (1) Java syntax errors in source code, (2) missing imported classes/dependencies in pom.xml, or (3) JDK version mismatch.
Resolution: Check the console error line number, fix source code syntax or typo in pom.xml dependency tags, run with '-X' for stack trace, and execute 'mvn clean compile'.

---

### Q47. How do you change the default build output directory from target/ to build_output/ in pom.xml?
**Explanation & Answer:**

In 'pom.xml', specify the '<directory>' tag inside '<build>':
<build>
  <directory>${project.basedir}/build_output</directory>
</build>
After running 'mvn compile', binaries will be written to 'build_output/' instead of 'target/'.

---

### Q48. What is a multi-module Maven project, and what is a parent POM?
**Explanation & Answer:**

A multi-module project organizes a complex system into smaller interdependent sub-projects (e.g. core, service, web). The root directory contains a Parent POM with '<packaging>pom</packaging>' that declares submodules in '<modules><module>core</module>...</modules>', allowing the entire suite of modules to be built in correct dependency order with a single command.

---

### Q49. What is the purpose of <dependencyManagement> vs <dependencies> in parent POMs?
**Explanation & Answer:**

• '<dependencies>': Dependencies declared here are unconditionally inherited by all child submodules.
• '<dependencyManagement>': Acts as a centralized dictionary defining dependency versions and configurations without actually adding them to classpaths. Child modules declare dependencies without specifying '<version>', ensuring uniform versions across the entire enterprise project.

---

### Q50. How do you generate a test coverage and project site documentation report in Maven?
**Explanation & Answer:**

Run: $ mvn site
This compiles project reports, Javadoc, Surefire test reports, and dependency analysis into HTML web documentation located inside 'target/site/index.html'.

---


## Topic 3: Docker Engine & Container CLI Architecture (50 Questions)

### Q1. What is Docker, and what problem does it solve in modern software development?
**Explanation & Answer:**

Docker is an open-source platform that automates the deployment of applications inside lightweight, portable containers. It solves the classic 'it works on my machine' problem by packaging the application code along with its exact runtime, libraries, environment variables, and system dependencies, ensuring 100% consistent execution across development, testing, and cloud production environments.

---

### Q2. What is containerization, and how does it differ from virtualization (Virtual Machines)?
**Explanation & Answer:**

• Virtualization (VMs): Each Virtual Machine runs a complete guest operating system on top of a hypervisor (like VMware/VirtualBox), requiring dedicated kernel memory, slow boot times (minutes), and gigabytes of disk space.
• Containerization (Docker): Containers share the host operating system's Linux kernel and isolate processes using kernel namespaces and cgroups. They boot in milliseconds, consume megabytes of RAM, and are extremely lightweight.

---

### Q3. What is the role of the Linux kernel (cgroups and namespaces) in Docker?
**Explanation & Answer:**

Docker containers rely directly on two core Linux kernel primitives:
1. Namespaces: Provide isolation between containers (PID for process IDs, NET for network interfaces/routes, MNT for filesystem mount points, IPC for inter-process communication, and UTS for hostnames).
2. Control Groups (cgroups): Meter, restrict, and enforce resource limits (CPU quotas, memory caps, block I/O bandwidth, network priority) on container process trees.

---

### Q4. What is a Docker Image?
**Explanation & Answer:**

A Docker Image is an immutable, read-only executable template containing everything needed to run an application—code, runtime, libraries, environment variables, and configuration files. Images are built from layers defined in a Dockerfile and stored in registries like Docker Hub.

---

### Q5. What is a Docker Container?
**Explanation & Answer:**

A Docker Container is a runnable, isolated instance of a Docker Image. When an image is run, Docker adds a thin read-write layer on top of the immutable image layers, allowing the application to execute, read, and write files in an isolated user space.

---

### Q6. What is Docker Hub?
**Explanation & Answer:**

Docker Hub (hub.docker.com) is the default cloud-hosted public and private container image registry. It provides official base images (e.g. ubuntu, openjdk, mysql, tomcat, redis) and allows developers to publish, share, and pull versioned images globally.

---

### Q7. What is the Docker Daemon (dockerd), and how does it interact with the Docker CLI?
**Explanation & Answer:**

The Docker Daemon ('dockerd') is a background service running on the host OS that manages containers, images, networks, storage volumes, and kernel cgroups. The Docker CLI ('docker') acts as a REST client that communicates with the daemon over a local Unix domain socket ('/var/run/docker.sock') or network API.

---

### Q8. How do you start, stop, and verify the Docker daemon on Ubuntu using systemctl?
**Explanation & Answer:**

• Start daemon: $ sudo systemctl start docker
• Stop daemon: $ sudo systemctl stop docker
• Restart daemon: $ sudo systemctl restart docker
• Verify status: $ sudo systemctl status docker
Status should show 'Active: active (running)'.

---

### Q9. How do you run Docker commands without sudo on Ubuntu?
**Explanation & Answer:**

Add the current non-root user to the 'docker' system group and refresh the shell session:
$ sudo usermod -aG docker $USER
$ newgrp docker
This grants permission to communicate with the Unix socket '/var/run/docker.sock' without root elevation.

---

### Q10. What does 'docker pull' do?
**Explanation & Answer:**

'docker pull <image>:<tag>' downloads the specified container image layers from a registry (Docker Hub) to the local Docker engine cache. If no tag is specified, it defaults to pulling the ':latest' tag.

---

### Q11. What does 'docker images' or 'docker image ls' display?
**Explanation & Answer:**

It lists all locally stored images, displaying:
• REPOSITORY (e.g. mysql, redis)
• TAG (e.g. 8.0, latest)
• IMAGE ID (unique truncated hexadecimal identifier)
• CREATED (time elapsed since creation)
• SIZE (disk space consumed on host filesystem).

---

### Q12. What is an image tag, and what does 'latest' mean?
**Explanation & Answer:**

A tag is a human-readable alias or version identifier attached to an image (e.g. 'mysql:8.0' or 'openjdk:17-jdk'). 'latest' is simply a default convention tag applied when no explicit tag is passed during build or pull; it does NOT guarantee the newest version if an older build was tagged as latest.

---

### Q13. How do you remove a Docker image using 'docker rmi'?
**Explanation & Answer:**

Run: $ docker rmi <image-id-or-name>
If a stopped container is still referencing the image, Docker prevents removal. Force removal using '$ docker rmi -f <image>' or delete the referencing container first.

---

### Q14. What is a dangling image, and how do you prune unused images?
**Explanation & Answer:**

A dangling image is an untagged image layer displayed as '<none>:<none>' created when a new image is built with the same tag as an existing image. Prune all dangling and unused images on Ubuntu by running:
$ docker image prune -a -f

---

### Q15. What does 'docker run' do? Explain the combination of 'create' and 'start'.
**Explanation & Answer:**

'docker run' performs three operations sequentially in one command:
1. Pulls the image from Docker Hub if not present locally.
2. Executes 'docker create' to allocate container filesystem layers, network endpoints, and namespace settings.
3. Executes 'docker start' to launch the container's entrypoint process.

---

### Q16. What is the purpose of the '-d' (detached) flag in 'docker run'?
**Explanation & Answer:**

The '-d' (detached mode) flag runs the container as a background daemon process, immediately returning control of the terminal shell to the user and printing the container ID hash. Without '-d', the container runs in foreground mode, attaching its standard output/error directly to the terminal.

---

### Q17. What is port forwarding / port mapping in Docker? What does '-p 9090:8080' mean?
**Explanation & Answer:**

Containers run in isolated network namespaces with private IP addresses. Port forwarding routes host traffic to the container.
Syntax: '-p <HostPort>:<ContainerPort>'.
'-p 9090:8080' binds port 9090 on the Ubuntu host machine to port 8080 inside the container. External requests to http://localhost:9090 are forwarded to container port 8080.

---

### Q18. What is the difference between host port and container port?
**Explanation & Answer:**

• Host Port: The physical network port exposed on the host operating system (Ubuntu), accessed by external clients and web browsers.
• Container Port: The internal private port that the application inside the container listens on (e.g. 8080 for Tomcat, 3306 for MySQL, 5000 for Flask).

---

### Q19. How do you name a container using '--name', and why is it recommended?
**Explanation & Answer:**

Pass the '--name' flag during container launch: '$ docker run -d --name oltrs-app -p 9090:8080 myimage'.
Naming containers is recommended because it provides human-readable aliases for commands ('docker logs oltrs-app', 'docker stop oltrs-app') and enables inter-container DNS communication on custom networks.

---

### Q20. What is the difference between 'docker ps' and 'docker ps -a'?
**Explanation & Answer:**

• 'docker ps': Lists only currently running active containers.
• 'docker ps -a': Lists ALL containers on the system, including running, paused, exited (crashed or stopped), and dead containers.

---

### Q21. What information is shown in 'docker ps' output?
**Explanation & Answer:**

Columns displayed: (1) CONTAINER ID, (2) IMAGE used, (3) COMMAND executed on startup, (4) CREATED timestamp, (5) STATUS (e.g. Up 2 hours, Exited (0)), (6) PORTS mapping, and (7) NAMES assigned to the container.

---

### Q22. What does 'docker stop' do, and how does it differ from 'docker kill'? (SIGTERM vs SIGKILL)
**Explanation & Answer:**

• 'docker stop': Sends a graceful POSIX SIGTERM signal to the container's PID 1 process, allowing it to flush buffers, finish active transactions, and shut down cleanly. If it doesn't terminate within 10 seconds, it sends SIGKILL.
• 'docker kill': Sends an immediate, abrupt SIGKILL signal, terminating the process instantly without graceful cleanup.

---

### Q23. What does 'docker start' do, and how does it differ from 'docker run'?
**Explanation & Answer:**

'docker run' initializes and creates a brand-new container from an image. 'docker start <container-name>' resumes execution of an existing, stopped container, preserving all data and filesystem modifications made in its read-write layer.

---

### Q24. What does 'docker restart' do?
**Explanation & Answer:**

'docker restart <container-name>' stops the running container (via SIGTERM) and immediately starts it back up, reloading process configurations and refreshing network sockets.

---

### Q25. How do you view container logs using 'docker logs'?
**Explanation & Answer:**

Run: $ docker logs <container-name-or-id>
This outputs all standard output (stdout) and standard error (stderr) streams generated by the container's PID 1 process since startup.

---

### Q26. How do you stream live container logs using 'docker logs -f'?
**Explanation & Answer:**

Run: $ docker logs -f --tail 100 <container-name>
The '-f' (follow) flag keeps the terminal connection open to stream new log entries in real-time (similar to 'tail -f' in Linux), while '--tail 100' displays only the latest 100 lines.

---

### Q27. What does 'docker exec' do?
**Explanation & Answer:**

'docker exec' runs a new command inside an already running container within its existing namespaces, without restarting or modifying the container.

---

### Q28. How do you open an interactive terminal shell inside a running container using 'docker exec -it'?
**Explanation & Answer:**

Run: $ docker exec -it <container-name> /bin/bash
(Or '/bin/sh' if the image is minimal/Alpine).
• '-i' (interactive): Keeps standard input (stdin) open.
• '-t' (tty): Allocates a pseudo-terminal, giving the user an interactive shell prompt inside the container.

---

### Q29. What is the difference between '/bin/bash' and '/bin/sh' in 'docker exec'?
**Explanation & Answer:**

• '/bin/bash': The full Bourne Again Shell featuring tab completion, history, and rich scripting. Available in standard Ubuntu/Debian images.
• '/bin/sh': The minimal POSIX Bourne shell. Present in ultra-lightweight distributions like Alpine Linux that lack bash by default.

---

### Q30. How do you remove a stopped container using 'docker rm'?
**Explanation & Answer:**

Run: $ docker rm <container-name-or-id>
This deletes the container's writable layer and metadata from disk.

---

### Q31. How do you forcefully remove a running container using 'docker rm -f'?
**Explanation & Answer:**

Run: $ docker rm -f <container-name>
The '-f' flag issues a SIGKILL signal to the running container process and deletes the container immediately in a single step.

---

### Q32. How do you remove all stopped containers in one command?
**Explanation & Answer:**

Run either of the following commands in Ubuntu:
$ docker container prune -f
$ docker rm $(docker ps -a -q -f status=exited)

---

### Q33. What is 'docker inspect', and what type of information does it return?
**Explanation & Answer:**

'docker inspect <container-or-image>' returns a detailed JSON array describing the low-level configuration of the target. It includes IP addresses, MAC address, gateway, mounted volumes, environment variables, health status, and state flags.

---

### Q34. How do you filter 'docker inspect' output using grep or --format?
**Explanation & Answer:**

• Using grep: $ docker inspect my-redis | grep IPAddress
• Using Go template '--format': $ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-redis
This outputs only the container's private IP address.

---

### Q35. What is container storage ephemerality, and why do containers lose data on removal?
**Explanation & Answer:**

Containers use an ephemeral, copy-on-write storage driver. When a container is deleted ('docker rm'), its top writable layer is wiped permanently. Any files created inside the container (such as MySQL databases) are lost unless saved to an external persistent Docker Volume.

---

### Q36. What is a Docker Volume, and why is it preferred for database storage?
**Explanation & Answer:**

A Docker Volume is a directory managed directly by Docker outside the container's storage driver, stored on the host filesystem. Volumes are preferred because: (1) data persists even when containers are deleted, (2) volumes have higher I/O performance than copy-on-write layers, and (3) volumes can be safely shared across multiple containers.

---

### Q37. How do you create, list, and inspect Docker volumes on Ubuntu?
**Explanation & Answer:**

• Create volume: $ docker volume create mydata
• List volumes: $ docker volume ls
• Inspect volume: $ docker volume inspect mydata

---

### Q38. Where are Docker volumes physically stored on the Ubuntu filesystem?
**Explanation & Answer:**

On Ubuntu Linux, Docker volumes are physically stored under root storage at:
'/var/lib/docker/volumes/<volume-name>/_data/'.

---

### Q39. What is the difference between a named volume and a bind mount?
**Explanation & Answer:**

• Named Volume ('-v mydata:/var/lib/mysql'): Completely managed by Docker inside '/var/lib/docker/volumes/'. Recommended for production data and databases.
• Bind Mount ('-v /home/ubuntu/app:/usr/share/nginx/html'): Mounts any arbitrary physical directory or file from the host filesystem directly into the container. Recommended for local source code development.

---

### Q40. How do you mount a volume to a container using the '-v' flag?
**Explanation & Answer:**

Syntax: '-v <VolumeName>:<ContainerMountPath>'.
Example:
$ docker run -d --name db -v mysql_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 mysql:8.0
MySQL will store all table schemas and records into 'mysql_data'.

---

### Q41. What is Docker networking, and what is the default network driver? (bridge)
**Explanation & Answer:**

Docker networking provides isolated communication channels between containers and external hosts. The default driver is 'bridge', which creates a virtual Linux software bridge interface ('docker0') assigning private IP addresses (typically 172.17.0.0/16) to containers.

---

### Q42. What are the built-in network drivers in Docker? (bridge, host, none, overlay)
**Explanation & Answer:**

• bridge: Default isolated network for standalone containers on a single host.
• host: Removes network isolation; container shares host network stack directly (e.g. port 80 binds directly to host port 80).
• none: Disables all networking; container has only a loopback interface.
• overlay: Enables multi-host container-to-container networking across Swarm or Kubernetes clusters.

---

### Q43. What is a custom bridge network, and why is it better than the default bridge network?
**Explanation & Answer:**

A custom bridge network ('docker network create my-net') provides automatic DNS resolution between containers by container name, better security isolation (only attached containers can communicate), and runtime configurability without stopping containers.

---

### Q44. How does Docker provide automatic DNS service discovery on custom networks?
**Explanation & Answer:**

Docker runs an embedded DNS server at 127.0.0.11 inside each container connected to a custom network. When an app connects to 'db:3306', Docker's internal DNS automatically resolves the service/container name 'db' to its current internal container IP.

---

### Q45. How do you create and connect containers to a custom bridge network?
**Explanation & Answer:**

1. Create network: $ docker network create app-net
2. Run container on network: $ docker run -d --name db --network app-net mysql:8.0
3. Attach existing container: $ docker network connect app-net web

---

### Q46. How do you push a local Docker image to Docker Hub?
**Explanation & Answer:**

1. Login: $ docker login
2. Tag image: $ docker tag myapp:latest dheerajmalavath/myapp:v1
3. Push: $ docker push dheerajmalavath/myapp:v1

---

### Q47. What is 'docker tag', and why must the image name include the Docker Hub username?
**Explanation & Answer:**

'docker tag' creates an alias for an existing image ID. The image name must be prefixed with your Docker Hub username ('<username>/<repo>:<tag>') so that the Docker CLI knows which registry account namespace to upload the image layers to during 'docker push'.

---

### Q48. What is 'docker login', and where are credentials stored?
**Explanation & Answer:**

'docker login' authenticates against Docker Hub or a private registry. On Ubuntu Linux, authentication tokens and credentials are encrypted and stored in '~/.docker/config.json'.

---

### Q49. What is 'docker stats', and what system metrics does it report?
**Explanation & Answer:**

'docker stats' provides a live streaming dashboard of container resource utilization, reporting:
• CPU % usage
• Memory usage vs limit (and Memory %)
• Network I/O (bytes sent/received)
• Block I/O (disk read/written)
• PIDs (total active thread count).

---

### Q50. What is 'docker system prune', and what resources does it clean up?
**Explanation & Answer:**

Run: $ docker system prune -a --volumes -f
This completely purges: (1) all stopped containers, (2) all unused networks, (3) all dangling and unused images, (4) all build cache layers, and (5) all unattached volumes, freeing gigabytes of host disk space.

---


## Topic 4: Docker Compose & Dockerfile Multi-Container Systems (50 Questions)

### Q1. What is Docker Compose?
**Explanation & Answer:**

Docker Compose is an orchestration tool used to define, configure, and execute multi-container Docker applications. Through a single declarative YAML file ('docker-compose.yml'), it provisions multiple interdependent services, inter-container bridge networks, environment variables, and persistent storage volumes in a single execution.

---

### Q2. What is the difference between Dockerfile and Docker Compose?
**Explanation & Answer:**

• Dockerfile: A blueprint script containing instructions ('FROM', 'COPY', 'RUN') used to build a SINGLE Docker image.
• Docker Compose: A configuration tool used to coordinate and run MULTIPLE containers simultaneously, managing their startup dependencies, network communication, port forwarding, and persistent volume mounts.

---

### Q3. What is the structure of a Dockerfile?
**Explanation & Answer:**

A Dockerfile is an ordered text file starting with a base image ('FROM') followed by environment setup ('WORKDIR', 'ENV'), layer additions ('COPY', 'RUN'), metadata ('EXPOSE', 'LABEL'), and an execution command ('CMD' or 'ENTRYPOINT').

---

### Q4. What is the 'FROM' instruction in a Dockerfile?
**Explanation & Answer:**

The 'FROM' instruction specifies the parent base image from which the new image is constructed (e.g. 'FROM tomcat:9.0' or 'FROM openjdk:17-jdk'). It must be the first non-comment instruction in any standard Dockerfile.

---

### Q5. What is the difference between 'RUN', 'CMD', and 'ENTRYPOINT' in a Dockerfile?
**Explanation & Answer:**

• 'RUN': Executes commands at IMAGE BUILD time and commits the result as a new image layer (e.g. 'RUN apt-get update && apt-get install -y curl').
• 'CMD': Specifies the DEFAULT command and parameters executed when the container STARTS at runtime. Can be overridden easily by command line arguments.
• 'ENTRYPOINT': Defines the immutable fixed executable run on container startup that is NOT overridden by command line arguments (arguments appended to entrypoint).

---

### Q6. When should you use 'ENTRYPOINT' vs 'CMD'?
**Explanation & Answer:**

Use 'ENTRYPOINT' when the container is intended to act as a dedicated executable binary (e.g. 'ENTRYPOINT ["java", "-jar", "app.jar"]'). Use 'CMD' to provide default parameters to 'ENTRYPOINT' that users can easily override, or when a default shell command is sufficient.

---

### Q7. What is the 'COPY' instruction, and how does it differ from 'ADD'?
**Explanation & Answer:**

• 'COPY': Copies local files or directories from the host build context into the container filesystem. It is transparent and preferred.
• 'ADD': Performs everything 'COPY' does, but also automatically unpacks local tar archives (tar.gz) and can download files directly from remote URLs (not recommended for simple copies).

---

### Q8. What is the 'WORKDIR' instruction in a Dockerfile?
**Explanation & Answer:**

'WORKDIR /path' sets the working directory inside the container for all subsequent 'RUN', 'CMD', 'ENTRYPOINT', and 'COPY' instructions, automatically creating the directory if it does not already exist (avoiding multiple 'cd' commands).

---

### Q9. What is the 'EXPOSE' instruction, and does it publish the port to the host?
**Explanation & Answer:**

'EXPOSE <port>' acts as internal documentation indicating which network port the application listens on inside the container. It does NOT actually publish or forward the port to the host system. Publishing to the host requires passing '-p <host_port>:<container_port>' at runtime.

---

### Q10. What is the 'ENV' instruction in a Dockerfile?
**Explanation & Answer:**

'ENV KEY=VALUE' sets environment variables that persist both during image build steps and inside the running container at runtime. Used for configuring database connection parameters, Java options ('JAVA_OPTS'), and system paths.

---

### Q11. What is multi-stage Docker build, and why is it used?
**Explanation & Answer:**

A multi-stage build uses multiple 'FROM' statements in a single Dockerfile. Early stages compile the code using full SDKs/compilers (e.g. Maven/JDK), and subsequent final stages copy ONLY the compiled artifact (.war/.jar) into a minimal lightweight JRE runtime image. This drastically reduces final image sizes from 800MB+ down to ~150MB and eliminates compiler security vulnerabilities from production.

---

### Q12. Write a minimal Dockerfile for deploying a WAR file to Apache Tomcat.
**Explanation & Answer:**

FROM tomcat:9.0-jdk11-openjdk-slim
RUN rm -rf /usr/local/tomcat/webapps/*
COPY target/*.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD ["catalina.sh", "run"]

---

### Q13. Write a minimal Dockerfile for running a Spring Boot JAR file.
**Explanation & Answer:**

FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app
COPY target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]

---

### Q14. What are Docker image layers, and how does layer caching improve build performance?
**Explanation & Answer:**

Every instruction in a Dockerfile ('RUN', 'COPY') creates an immutable read-only filesystem layer. Docker caches these layers. When re-building an image, Docker reuses unchanged cached layers instead of re-executing steps, reducing subsequent build times from minutes down to seconds.

---

### Q15. What is a .dockerignore file, and what should be included in it?
**Explanation & Answer:**

'.dockerignore' prevents unwanted files and large directories on the host from being sent to the Docker daemon during build context evaluation. Typically includes: '.git/', 'target/classes/', 'node_modules/', '*.log', and sensitive '.env' files.

---

### Q16. What is docker-compose.yml, and what file format does it use?
**Explanation & Answer:**

'docker-compose.yml' is a YAML (YAML Ain't Markup Language) configuration file. It uses strict 2-space indentation (tabs are strictly prohibited) to define services, volumes, networks, and environment variables.

---

### Q17. What are the top-level keys in a docker-compose.yml file?
**Explanation & Answer:**

The standard top-level keys are:
• 'version': Specifies compose file format specification (e.g. '3.8').
• 'services': Defines the containers to be created and managed.
• 'networks': Declares custom networks shared across services.
• 'volumes': Declares persistent named volumes shared across services.

---

### Q18. What is a 'service' in Docker Compose?
**Explanation & Answer:**

A service in Docker Compose represents an individual containerized application component (e.g. 'app', 'db', 'web', 'redis'). Each service specifies an image or build context, port mappings, environment variables, and runtime dependencies.

---

### Q19. What is the 'build:' directive in Docker Compose?
**Explanation & Answer:**

'build:' tells Docker Compose to build an image from a Dockerfile on the local filesystem rather than pulling a pre-built image from Docker Hub. Example: 'build: .' builds the Dockerfile located in the current project root directory.

---

### Q20. What is the 'image:' directive in Docker Compose?
**Explanation & Answer:**

'image:' specifies the pre-built Docker image to pull and run from a registry (e.g. 'image: mysql:8.0' or 'image: wordpress:latest').

---

### Q21. What happens if both 'build:' and 'image:' are specified in a Compose service?
**Explanation & Answer:**

If both are present, Compose builds the image using the local 'build:' context and tags the resulting image with the name supplied in 'image:'.

---

### Q22. What does 'container_name:' do in Docker Compose?
**Explanation & Answer:**

By default, Compose assigns container names following the pattern '<project>_<service>_<index>'. 'container_name: oltrs-app' forces Docker Compose to assign a custom static name, making CLI inspection and log querying straightforward.

---

### Q23. What is the 'ports:' directive in Docker Compose?
**Explanation & Answer:**

Maps host ports to container ports ('HostPort:ContainerPort'). Example:
ports:
  - "9090:8080"
Forwards incoming traffic on Ubuntu host port 9090 to container port 8080.

---

### Q24. What is the 'environment:' directive, and how can environment variables be passed from a .env file?
**Explanation & Answer:**

'environment:' sets runtime environment variables inside the container (e.g. DB_HOST, DB_NAME, MYSQL_ROOT_PASSWORD). Compose automatically loads key-value pairs from a local '.env' file in the same directory and substitutes them via '${VARIABLE_NAME}' syntax.

---

### Q25. What is the 'depends_on:' directive in Docker Compose?
**Explanation & Answer:**

'depends_on:' controls container startup and shutdown order. Example: 'depends_on: - db' ensures the database container starts BEFORE the application container is launched.

---

### Q26. Does 'depends_on' guarantee that the database inside the container is fully ready to accept connections?
**Explanation & Answer:**

No. 'depends_on' only waits until the dependency container process STARTS running, not until the internal database daemon has completed initialization and is ready to accept client connections.

---

### Q27. How do you solve the race condition where an app container crashes before MySQL finishes initialization?
**Explanation & Answer:**

1. In docker-compose.yml: Add 'restart: always' so Docker continuously restarts the crashed app container until MySQL is ready.
2. Use health checks with 'condition: service_healthy' in depends_on.
3. Implement retry connection logic inside the application code (e.g. JDBC connection pool).

---

### Q28. What is the 'volumes:' directive in Compose, and how do you define a named volume?
**Explanation & Answer:**

Under the service block, specify: '- dbdata:/var/lib/mysql'. At the bottom of 'docker-compose.yml', define the volume globally:
volumes:
  dbdata:
This tells Compose to allocate a persistent named volume that outlives the database container.

---

### Q29. What is the 'networks:' directive in Compose, and how do services talk to each other?
**Explanation & Answer:**

Services attached to the same declared network communicate with each other over an isolated software bridge. Docker's embedded DNS automatically resolves service names (e.g. 'db', 'app') to their respective container IP addresses.

---

### Q30. In a Compose network, what hostname does an application container use to connect to MySQL?
**Explanation & Answer:**

The application uses the SERVICE NAME (e.g. 'db' or 'mysql'), NOT 'localhost' or '127.0.0.1'. Inside container network namespaces, 'localhost' refers strictly to the application container itself, whereas 'db' resolves via Docker DNS to the database container.

---

### Q31. What is the 'restart: always' or 'restart: unless-stopped' policy?
**Explanation & Answer:**

• 'restart: always': Automatically restarts the container if it exits, crashes, or if the Docker daemon reboots, regardless of exit code.
• 'restart: unless-stopped': Restarts the container on crashes or daemon reboot, unless the user explicitly ran 'docker stop'.

---

### Q32. What command starts all services defined in docker-compose.yml in the background?
**Explanation & Answer:**

Run: $ docker compose up -d
Creates networks, volumes, pulls/builds images, and starts all containers in detached mode.

---

### Q33. What is the difference between 'docker compose up' and 'docker compose up -d'?
**Explanation & Answer:**

• 'docker compose up': Runs in foreground mode, interleaving console logs from all containers in the terminal. Closing the terminal stops all containers.
• 'docker compose up -d': Runs containers as background daemons and releases the terminal.

---

### Q34. When should you use 'docker compose up --build -d'?
**Explanation & Answer:**

Use '--build' whenever source code or Dockerfile changes have been made. Without '--build', Compose reuses existing cached local images and ignores your recent code changes.

---

### Q35. What does 'docker compose ps' show?
**Explanation & Answer:**

'docker compose ps' displays the status of all containers belonging specifically to the current compose project, showing service names, container states (Up/Exited), and mapped ports.

---

### Q36. How do you view logs of all services vs a single service in Docker Compose?
**Explanation & Answer:**

• All services: $ docker compose logs -f
• Specific service: $ docker compose logs -f <service-name> (e.g. 'docker compose logs -f app').

---

### Q37. What does 'docker compose stop' do?
**Explanation & Answer:**

'docker compose stop' sends SIGTERM to stop all running service containers without removing the containers, networks, or volume data.

---

### Q38. What does 'docker compose start' do?
**Explanation & Answer:**

'docker compose start' restarts previously stopped containers without re-reading the compose configuration or regenerating container IDs.

---

### Q39. What does 'docker compose restart' do?
**Explanation & Answer:**

'docker compose restart' stops and immediately re-executes all running services, useful for picking up configuration tweaks.

---

### Q40. How do you stop and remove only one specific service while keeping others running?
**Explanation & Answer:**

Run: $ docker compose stop <service_name>
Followed by: $ docker compose rm -f <service_name>
Leaves all other services (like the database) active and untouched.

---

### Q41. What is the difference between 'docker compose down' and 'docker compose down -v'?
**Explanation & Answer:**

• 'docker compose down': Stops and removes containers and networks, but PRESERVES persistent volumes on disk.
• 'docker compose down -v': Stops and removes containers, networks, AND permanently deletes all named volumes, wiping all database data.

---

### Q42. What happens to MySQL database records when 'docker compose down' is executed without -v?
**Explanation & Answer:**

All database tables and records remain completely safe and intact inside the persistent Docker volume. When 'docker compose up -d' is run next time, the database container mounts the existing volume and reloads all records.

---

### Q43. How do you scale a service in Docker Compose? (--scale web=3)
**Explanation & Answer:**

Run: $ docker compose up --scale <service_name>=<count> -d
Example: '$ docker compose up --scale web=3 -d' launches 3 identical, parallel container instances of the 'web' service.

---

### Q44. Why does scaling a service fail if a fixed host port mapping (e.g. 8080:8080) is used?
**Explanation & Answer:**

Because two containers cannot bind to the exact same physical host port (8080) simultaneously on Ubuntu, causing a 'port is already allocated' bind collision error.

---

### Q45. How do you scale a web service behind an Nginx reverse proxy load balancer?
**Explanation & Answer:**

Remove host port mappings from the web service (expose only container port internally), and place an Nginx container in front that binds to host port 80/8080 and load-balances traffic across the scaled service instances.

---

### Q46. How do you execute commands inside a Compose service container? (docker compose exec app ...)
**Explanation & Answer:**

Run: $ docker compose exec <service_name> <command>
Example: '$ docker compose exec app env' or '$ docker compose exec db mysql -u root -p'.

---

### Q47. Explain the architecture of a multi-container Java + MySQL application in Docker Compose.
**Explanation & Answer:**

Consists of: (1) App container running Tomcat/Spring Boot on custom network, (2) DB container running MySQL 8.0 on same network, (3) Persistent named volume mounted at '/var/lib/mysql', and (4) Environment variables linking App to DB hostname 'db'.

---

### Q48. Explain the architecture of a WordPress + MySQL application in Docker Compose.
**Explanation & Answer:**

Consists of: (1) Official WordPress image exposing port 80/9090, (2) MySQL 5.7/8.0 database image, (3) Shared bridge network, and (4) Environment variables 'WORDPRESS_DB_HOST: db:3306', 'WORDPRESS_DB_USER', and 'WORDPRESS_DB_PASSWORD'.

---

### Q49. What is the difference between 'docker-compose' (v1 with hyphen) and 'docker compose' (v2 with space)?
**Explanation & Answer:**

• 'docker-compose' (v1): A legacy standalone Python script that is deprecated and discontinued.
• 'docker compose' (v2): A modern Go-based plugin compiled directly into the official Docker CLI, offering faster execution, resource sharing, and improved command syntax.

---

### Q50. How do you validate the syntax of a docker-compose.yml file without running it? (docker compose config)
**Explanation & Answer:**

Run: $ docker compose config
This parses the YAML file, validates syntax rules, resolves environment variable substitutions, and prints the fully resolved configuration. If syntax is invalid, it reports exact line errors.

---


## Topic 5: Jenkins CI/CD Automation & Pipelines (50 Questions)

### Q1. What is Continuous Integration (CI) and Continuous Delivery/Deployment (CD)?
**Explanation & Answer:**

• Continuous Integration (CI): The practice of frequently committing code to a shared repository (multiple times daily) where automated builds and unit tests execute immediately to detect regressions early.
• Continuous Delivery (CD): Automatically packaging and preparing tested code for release to staging/production with a single manual approval click.
• Continuous Deployment: Fully automated pipeline where every passing commit automatically deploys directly to production with zero manual intervention.

---

### Q2. What role does Jenkins play in a DevOps lifecycle?
**Explanation & Answer:**

Jenkins serves as the central automation orchestrator. It listens for code pushes from Git, checks out code, invokes Maven to compile and run tests, builds Docker container images, scans for security flaws, pushes images to Docker Hub, and triggers deployments to Kubernetes or AWS.

---

### Q3. How is Jenkins deployed inside a Docker container on Ubuntu?
**Explanation & Answer:**

Run the following command:
$ docker run -d --name jenkins --restart=always -p 9080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
Exposes port 9080 for web dashboard and mounts volume 'jenkins_home' to persist configurations.

---

### Q4. What ports does Jenkins expose by default, and what are their purposes? (8080 and 50000)
**Explanation & Answer:**

• Port 8080 (mapped to 9080): HTTP web interface port used by administrators and developers to access the Jenkins dashboard.
• Port 50000: JNLP (Java Network Launch Protocol) agent connection port used by distributed Jenkins worker/agent nodes to communicate with the controller.

---

### Q5. Why is '-v jenkins_home:/var/jenkins_home' critical when running Jenkins in Docker?
**Explanation & Answer:**

All Jenkins job configurations, build histories, plugins, user credentials, and secrets reside inside '/var/jenkins_home'. Mounting a persistent volume ensures that when the Jenkins container is stopped, updated, or recreated, all jobs, credentials, and settings remain completely intact.

---

### Q6. How do you retrieve the initial admin password to unlock Jenkins on Ubuntu?
**Explanation & Answer:**

Run inside the container volume:
$ docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
Outputs a 32-character hexadecimal key to paste into the browser unlock screen at http://localhost:9080.

---

### Q7. What are suggested plugins during initial Jenkins setup?
**Explanation & Answer:**

Suggested plugins include Git, Pipeline, Folders, OWASP Markup Formatter, Credentials Binding, Timestamper, Workspace Cleanup, Ant, Gradle, Mailer, and SSH Slaves. They provide the fundamental baseline for version control and pipeline orchestration.

---

### Q8. How do you manage and install new plugins in Jenkins?
**Explanation & Answer:**

1. In Jenkins dashboard, click 'Manage Jenkins' on the left sidebar.
2. Click 'Plugins' → Select the 'Available plugins' tab.
3. Search for plugin names (e.g. 'Maven Integration', 'Docker Pipeline').
4. Check the desired checkboxes and click 'Install without restart'.

---

### Q9. What plugins are essential for a Java/DevOps CI/CD pipeline in Jenkins? (Git, Pipeline, Maven, Docker)
**Explanation & Answer:**

• Git Plugin: Pulls source code from GitHub repositories.
• Pipeline Plugin: Enables writing Jenkinsfile Pipeline-as-Code.
• Maven Integration Plugin: Integrates Maven tools, automated test parsing, and goals.
• Docker Pipeline & Docker Plugin: Enables building, running, and pushing Docker images within pipeline stages.

---

### Q10. What is a Freestyle project in Jenkins?
**Explanation & Answer:**

A Freestyle project is a legacy, UI-driven job configuration model in Jenkins. Users configure repository URLs, build steps, and post-build actions through dropdowns, text boxes, and checkboxes in the Jenkins web browser interface.

---

### Q11. How do you configure a Git repository in a Freestyle project?
**Explanation & Answer:**

Under the 'Source Code Management' section in the job configuration:
1. Select 'Git'.
2. In 'Repository URL', enter: 'https://github.com/archanareddyse/OLTRS.git'.
3. Provide credentials if private, or leave 'None' if public.

---

### Q12. How do you specify the build branch (e.g. '*/main') in Jenkins?
**Explanation & Answer:**

In the 'Branches to build' field, enter '*/main' (or '*/master'). Always verify on GitHub whether the repository's default branch is 'main' or 'master' to avoid 'Couldn't find any revision to build' errors.

---

### Q13. How do you invoke Maven targets in a Freestyle project?
**Explanation & Answer:**

Under the 'Build Steps' section:
1. Click 'Add build step' dropdown → Select 'Invoke top-level Maven targets'.
2. In 'Maven Version', select configured tool (e.g. 'Maven').
3. In 'Goals', type: 'clean package -DskipTests'.

---

### Q14. What are Post-build Actions in a Freestyle project?
**Explanation & Answer:**

Post-build actions execute after build steps complete. Examples include: (1) Archiving build artifacts (e.g. 'target/*.war'), (2) Publishing JUnit test result reports, (3) Sending email failure notifications, and (4) Triggering downstream build jobs.

---

### Q15. What is an Artifact in Jenkins, and how is it archived?
**Explanation & Answer:**

An artifact is a binary file produced by a build (e.g. 'ticket-reservation.war' or JAR file). Under Post-build Actions, select 'Archive the artifacts' and enter 'target/*.war'. Jenkins stores this file on the controller, displaying a clickable download link on the job summary page.

---

### Q16. What is a Jenkins Pipeline?
**Explanation & Answer:**

A Jenkins Pipeline is a suite of plugins that supports implementing and integrating continuous delivery pipelines into Jenkins. It models an entire software delivery workflow from version control to production as code.

---

### Q17. What is a Jenkinsfile, and why is Pipeline-as-Code superior to Freestyle jobs?
**Explanation & Answer:**

A 'Jenkinsfile' is a text file checked directly into the root of a Git repository containing the pipeline definition. Advantages over Freestyle: (1) Version controlled alongside application code, (2) Code reviewed via Pull Requests, (3) Disaster recovery is instant, and (4) Complex multi-branch logic is easily expressed.

---

### Q18. What are the two types of Jenkins Pipeline syntax? (Declarative vs Scripted)
**Explanation & Answer:**

• Declarative Pipeline: A structured, opinionated syntax enclosed in 'pipeline { ... }' with strict predefined sections ('agent', 'stages', 'steps', 'post'). Easier to read and recommended for most standard CI/CD pipelines.
• Scripted Pipeline: A flexible, code-centric Groovy-based syntax enclosed in 'node { ... }'. Provides maximum programmatic power, loops, conditional logic, and exception handling.

---

### Q19. What is the fundamental structure of a Scripted Pipeline? (node { ... })
**Explanation & Answer:**

node {
    stage('Checkout') { git url: '...' }
    stage('Build') { sh 'mvn clean compile' }
    stage('Test') { sh 'mvn test' }
    stage('Deploy') { sh 'docker run ...' }
}

---

### Q20. What is the fundamental structure of a Declarative Pipeline? (pipeline { agent any ... })
**Explanation & Answer:**

pipeline {
    agent any
    stages {
        stage('Build') {
            steps { sh 'mvn clean compile' }
        }
    }
    post {
        always { cleanWs() }
    }
}

---

### Q21. What is a 'stage' in a Jenkins Pipeline?
**Explanation & Answer:**

A 'stage' represents a major logical phase of the CI/CD pipeline (e.g. 'Checkout', 'Build', 'Test', 'Docker Build', 'Deploy'). Jenkins Stage View UI renders each stage as a distinct graphical column displaying execution time and status (green/red).

---

### Q22. What is a 'step' in a Jenkins Pipeline?
**Explanation & Answer:**

A 'step' is a single basic task that tells Jenkins what action to perform within a stage (e.g. 'sh', 'git', 'echo', 'mail', 'tool', 'archiveArtifacts').

---

### Q23. What is an 'agent' in Declarative Pipeline?
**Explanation & Answer:**

The 'agent' directive specifies WHERE the pipeline or a specific stage will execute. 'agent any' runs on any available agent node; 'agent { docker { image 'maven:3.8-openjdk-17' } }' executes inside an isolated container.

---

### Q24. How do you configure the Maven tool in Jenkins Global Tool Configuration?
**Explanation & Answer:**

1. Manage Jenkins → 'Tools'.
2. Scroll down to 'Maven installations' → Click 'Add Maven'.
3. Enter Name: 'Maven' (matches 'tool "Maven"' in Jenkinsfile).
4. Check 'Install automatically' → Select version 3.9.x → Click 'Save'.

---

### Q25. How do you reference the configured Maven tool inside a Scripted Pipeline? (def mvnHome = tool 'Maven')
**Explanation & Answer:**

In Groovy script box:
def mvnHome = tool 'Maven'
This resolves the absolute installation path of the Maven executable on disk, allowing commands to be executed via: 'sh "${mvnHome}/bin/mvn clean package"'.

---

### Q26. What does 'sh "${mvnHome}/bin/mvn clean package"' do inside a Jenkins pipeline on Ubuntu?
**Explanation & Answer:**

It invokes the Linux shell ('sh') step to run the Maven executable on Ubuntu, compiling the code, running tests, and generating the packaged artifact (.war/.jar) inside the workspace.

---

### Q27. How does Jenkins handle credentials securely? (Credentials Store)
**Explanation & Answer:**

Jenkins provides a centralized encrypted Credentials Store. Credentials are encrypted using master encryption keys and stored at 'credentials.xml'. Pipelines reference credentials safely by an assigned ID (e.g. 'dockerhub-creds') without exposing plaintext secrets in code.

---

### Q28. What credential types are supported in Jenkins?
**Explanation & Answer:**

• Secret text: API tokens, GitHub Personal Access Tokens (PAT).
• Username with password: For Docker Hub, database logins, basic auth.
• SSH Username with private key: For SSH access to remote deployment servers (AWS EC2).
• Secret file: For SSL certificates, Kubernetes kubeconfig files.

---

### Q29. How do you bind credentials in a Scripted Pipeline? (withCredentials([usernamePassword(...)])
**Explanation & Answer:**

withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
    sh 'echo $DH_PASS | docker login -u $DH_USER --password-stdin'
}

---

### Q30. Why does Jenkins mask credentials in console output with ****?
**Explanation & Answer:**

Jenkins has a built-in credential masking filter that intercepts console output. If an environment variable injected by 'withCredentials' is echoed to stdout, Jenkins automatically masks the plaintext password with '****' to prevent security leaks in build logs.

---

### Q31. How do you build and push a Docker image to Docker Hub inside a Jenkins pipeline?
**Explanation & Answer:**

stage('Docker Build & Push') {
    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
        sh '''
            docker build -t dheerajmalavath/oltrs:latest .
            echo $DH_PASS | docker login -u $DH_USER --password-stdin
            docker push dheerajmalavath/oltrs:latest
        '''
    }
}

---

### Q32. What is the purpose of Docker Pipeline plugin in Jenkins?
**Explanation & Answer:**

It allows Jenkins pipelines to run build steps dynamically inside temporary Docker containers (e.g. 'docker.image("maven:3.8").inside { ... }') without needing tool compilers pre-installed on the host system.

---

### Q33. How do you handle pipeline build failures using try-catch in Groovy?
**Explanation & Answer:**

try {
    stage('Build') { sh 'mvn clean compile' }
    stage('Test') { sh 'mvn test' }
} catch (Exception e) {
    stage('Alert') {
        mail to: 'admin@example.com', subject: 'BUILD FAILED', body: e.getMessage()
    }
    error('Build failed due to test errors.')
}

---

### Q34. How do you configure email notifications on build failure in Jenkins?
**Explanation & Answer:**

1. In Manage Jenkins → System → Configure 'E-mail Notification' (SMTP server, port, credentials).
2. In pipeline script, add 'mail to: "...", subject: "...", body: "..."' in failure blocks or Declarative 'post { failure { ... } }'.

---

### Q35. How can you intentionally simulate a build failure to test notification alerting? (SET 4 Q2c)
**Explanation & Answer:**

Insert an intentional failure shell step inside a pipeline stage:
stage('Intentional Failure Test') {
    sh 'exit 1'
}
An exit code of 1 forces Jenkins to immediately fail the stage and trigger the exception handling or failure notification block.

---

### Q36. What is a Build Trigger in Jenkins?
**Explanation & Answer:**

A Build Trigger is a condition or event that automatically initiates job execution. Common triggers include: (1) GitHub Webhook (Push events), (2) Poll SCM (Periodic repo checking), (3) Build periodically (Cron), and (4) Trigger after other projects build.

---

### Q37. What is 'Poll SCM' in Jenkins?
**Explanation & Answer:**

'Poll SCM' configures Jenkins to periodically connect to the remote Git repository on a schedule (e.g. every 5 minutes) and query for new commits. If new commits are detected, it triggers a build.

---

### Q38. What is the difference between 'Poll SCM' and a GitHub Webhook?
**Explanation & Answer:**

• Poll SCM (Pull mechanism): Jenkins periodically pesters GitHub every few minutes asking 'Are there new commits?'. Wastes network bandwidth and causes delay.
• GitHub Webhook (Push mechanism): Real-time event-driven. The millisecond a developer pushes code, GitHub immediately notifies Jenkins via an HTTP POST request, triggering builds instantly.

---

### Q39. What is a GitHub Webhook, and what payload URL does Jenkins expect?
**Explanation & Answer:**

In GitHub Repo → Settings → Webhooks → Add webhook:
Payload URL: 'http://<jenkins-server-ip>:9080/github-webhook/'
Content type: 'application/json'
The trailing slash ('/') is mandatory.

---

### Q40. What is 'Build periodically' in Jenkins?
**Explanation & Answer:**

A scheduled trigger that runs a build at specific recurring clock times based on a standard cron syntax expression, independent of whether source code changes were made.

---

### Q41. Explain the 5 fields of Jenkins cron syntax: MINUTE HOUR DOM MONTH DOW.
**Explanation & Answer:**

1. MINUTE: 0–59
2. HOUR: 0–23 (military time)
3. DOM (Day of Month): 1–31
4. MONTH: 1–12
5. DOW (Day of Week): 0–7 (0 and 7 = Sunday, 1 = Monday, 5 = Friday).

---

### Q42. Write the cron expression to run a build every day at 6:00 PM. (0 18 * * *)
**Explanation & Answer:**

0 18 * * *
(Minute 0, Hour 18 = 6 PM, every day of month, every month, every day of week).

---

### Q43. Write the cron expression to run a build every 15 minutes. (H/15 * * * *)
**Explanation & Answer:**

H/15 * * * *
(Runs approximately every 15 minutes, using Jenkins Hash function to distribute load).

---

### Q44. What does the 'H' (Hash) symbol mean in Jenkins cron expressions?
**Explanation & Answer:**

The 'H' (Hash) symbol tells Jenkins to choose an arbitrary, consistent minute offset based on a hash of the project name. This prevents multiple jobs configured with '0 * * * *' from firing simultaneously at the top of the hour and overwhelming system CPU.

---

### Q45. What is a Jenkins Master (Controller) and Agent (Node) architecture?
**Explanation & Answer:**

Jenkins uses a distributed master-agent architecture:
• Controller (Master): Hosts the web GUI, parses Jenkinsfiles, manages plugin configurations, and schedules jobs.
• Agents (Nodes): Lightweight worker daemons that execute the physical build scripts, compile code, and run tests, reporting results back to the controller.

---

### Q46. Why should heavy builds not run on the Jenkins Controller?
**Explanation & Answer:**

Running heavy compilation or Docker builds on the controller can exhaust CPU, memory, or disk space, causing the Jenkins web interface to freeze, drop webhooks, and disconnect all connected agents.

---

### Q47. What is a multi-branch pipeline in Jenkins?
**Explanation & Answer:**

A multi-branch pipeline automatically discovers branches in a GitHub repository containing a 'Jenkinsfile' and automatically creates individual, isolated pipeline jobs for each branch (e.g. main, feature-auth, dev).

---

### Q48. How do you view the console output of a running or completed build in Jenkins?
**Explanation & Answer:**

Click on the job name → Click on the specific build number (e.g. '#1') in the build history on the left → Click 'Console Output' to view streaming terminal logs.

---

### Q49. What does blue/green, yellow, and red status mean in Jenkins job dashboard?
**Explanation & Answer:**

• Blue / Green: SUCCESS — Build completed cleanly and all tests passed.
• Yellow: UNSTABLE — Build succeeded, but unit tests failed or compiler warnings occurred.
• Red: FAILURE — Build failed during execution (compilation error, syntax error, or aborted step).

---

### Q50. What is Jenkins Blue Ocean, and what advantages does it offer?
**Explanation & Answer:**

Blue Ocean is a modern, visual user interface replacement for the classic Jenkins dashboard. It provides visual pipeline progression graphs, visual stage logs, branch tracking, and an intuitive visual Jenkinsfile editor.

---


## Topic 6: Kubernetes & Minikube Container Orchestration (50 Questions)

### Q1. What is Kubernetes (K8s), and why was it created?
**Explanation & Answer:**

Kubernetes is an open-source container orchestration platform originally developed by Google. It was created to automate the deployment, scaling, health-checking, load-balancing, and lifecycle management of multi-container applications across clusters of physical or virtual machines.

---

### Q2. What are the key features of Kubernetes?
**Explanation & Answer:**

• Automated Self-Healing: Restarts failed containers, replaces pods, and reschedules pods when nodes die.
• Horizontal Auto-Scaling: Dynamically scales application replicas based on CPU/memory usage.
• Service Discovery & Load Balancing: Assigns stable internal DNS names and load-balances network traffic across pods.
• Automated Rollouts and Rollbacks: Progressively deploys image updates with zero downtime and enables one-click rollbacks.
• Storage Orchestration: Mounts local, cloud (EBS), or network storage (NFS) automatically.

---

### Q3. What is the difference between Docker and Kubernetes?
**Explanation & Answer:**

• Docker: A container runtime platform used to build, package, and execute containers on a single host machine.
• Kubernetes: A cluster orchestration engine that coordinates hundreds of Docker containers across multiple nodes, handling auto-scaling, fault tolerance, high availability, and network routing.

---

### Q4. What is Minikube?
**Explanation & Answer:**

Minikube is a tool that provisions a lightweight, single-node Kubernetes cluster locally on a developer's computer. It packages all control plane and worker node components into a single virtual environment, ideal for learning and testing Kubernetes workflows.

---

### Q5. What hypervisor/driver does Minikube use on Ubuntu? (Docker driver)
**Explanation & Answer:**

On Ubuntu Linux, Minikube uses the 'docker' driver by default ('minikube start --driver=docker'). The entire Kubernetes node runs inside an optimized Docker container on the host system without requiring VirtualBox or KVM.

---

### Q6. How do you install Minikube and kubectl on Ubuntu?
**Explanation & Answer:**

# Install Minikube:
$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
$ sudo install minikube-linux-amd64 /usr/local/bin/minikube
# Install kubectl:
$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
$ sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

---

### Q7. What command starts the Minikube cluster? (minikube start --driver=docker)
**Explanation & Answer:**

Run: $ minikube start --driver=docker
Initializes the control plane, starts etcd and kubelet, and configures the local kubeconfig context to point to the minikube cluster.

---

### Q8. What does 'kubectl cluster-info' show?
**Explanation & Answer:**

Displays the active Kubernetes control plane endpoint URL (e.g. 'Kubernetes control plane is running at https://192.168.49.2:8443') and CoreDNS service endpoints.

---

### Q9. What does 'kubectl get nodes' show?
**Explanation & Answer:**

Lists all physical or virtual cluster worker/master nodes, showing: NAME (minikube), STATUS (Ready), ROLES (control-plane), AGE, and Kubernetes VERSION (v1.28.x).

---

### Q10. What is the Kubernetes Control Plane (Master Node), and what are its key components?
**Explanation & Answer:**

The Control Plane manages global cluster state, schedules workloads, and responds to cluster events. Its components are:
1. kube-apiserver: Central gateway exposing the REST API.
2. etcd: Consistent, highly-available distributed key-value store.
3. kube-scheduler: Evaluates resource constraints and assigns newly created pods to healthy worker nodes.
4. kube-controller-manager: Runs core control loops (Node Controller, Replication Controller, Endpoints Controller).

---

### Q11. What is the role of etcd in Kubernetes?
**Explanation & Answer:**

'etcd' is an open-source distributed key-value store that acts as the single source of truth for Kubernetes. Every piece of cluster state, manifest specification, pod status, and secret data is stored in etcd.

---

### Q12. What are the components of a Kubernetes Worker Node?
**Explanation & Answer:**

1. kubelet: Node agent that communicates with the API server and ensures container pods described in PodSpecs are running and healthy.
2. kube-proxy: Network proxy maintaining network rules on nodes and enabling Kubernetes service routing.
3. Container Runtime: Software (e.g. containerd, CRI-O, Docker) responsible for physically pulling and running container images.

---

### Q13. What is a Pod in Kubernetes?
**Explanation & Answer:**

A Pod is the smallest and simplest deployable unit in Kubernetes. A Pod represents a single instance of a running process in your cluster, encapsulating one or more tightly coupled containers, shared storage volumes, and a unique network IP address.

---

### Q14. Can a Pod contain more than one container? When is this pattern used (Sidecar)?
**Explanation & Answer:**

Yes (Multi-container Pod). Containers in the same pod share localhost network interface and storage volumes. Used in the 'Sidecar' pattern, where a helper container assists the main container (e.g. logging agent, proxy sidecar like Envoy, or metrics collector).

---

### Q15. Why are Pods ephemeral?
**Explanation & Answer:**

Pods are mortal and disposable. They can be created, killed, or rescheduled at any moment due to node failures, resource exhaustion, or scaling events. When a pod dies, its private IP is lost permanently. Therefore, deployments and services are used rather than managing standalone pods directly.

---

### Q16. What is a Deployment in Kubernetes?
**Explanation & Answer:**

A Deployment is a higher-level declarative controller that manages a set of identical Pods via a ReplicaSet. It provides declarative updates, automated scaling, rolling upgrades, and instant rollbacks.

---

### Q17. What is a ReplicaSet, and what is its relationship to Deployments and Pods?
**Explanation & Answer:**

A ReplicaSet's sole purpose is to maintain a stable set of replica Pods running at any given time. A Deployment manages ReplicaSets, and a ReplicaSet manages Pods. When a Deployment is updated, it creates a new ReplicaSet and scales down the old one.

---

### Q18. How do you create a Deployment imperatively using kubectl create deployment?
**Explanation & Answer:**

Run: $ kubectl create deployment oltrs-app --image=dheerajmalavath/oltrs:latest
Creates a deployment object named 'oltrs-app' running 1 replica pod of the specified Docker Hub image.

---

### Q19. How do you view all deployments in a cluster?
**Explanation & Answer:**

Run: $ kubectl get deployments
Displays: NAME, READY (e.g. 4/4), UP-TO-DATE, AVAILABLE, and AGE.

---

### Q20. What does 'kubectl describe deployment <name>' provide?
**Explanation & Answer:**

Provides extensive diagnostic metadata: selector labels, replica counts, rolling update strategy (Max Surge, Max Unavailable), pod template specifications, and recent events (scaling events, replica set creation).

---

### Q21. How do you list all running Pods with IP addresses and assigned nodes? (kubectl get pods -o wide)
**Explanation & Answer:**

Run: $ kubectl get pods -o wide
Displays pod name, status (Running), restart count, IP address (e.g. 10.244.0.5), and NODE (minikube).

---

### Q22. How do you inspect Pod logs using kubectl logs?
**Explanation & Answer:**

Run: $ kubectl logs <pod-name>
Stream live logs with: $ kubectl logs -f <pod-name>

---

### Q23. How do you execute an interactive shell inside a Pod? (kubectl exec -it <pod> -- /bin/bash)
**Explanation & Answer:**

Run: $ kubectl exec -it <pod-name> -- /bin/bash
Opens an interactive terminal prompt inside the pod container.

---

### Q24. How do you delete a Pod? What happens immediately after a Pod belonging to a Deployment is deleted?
**Explanation & Answer:**

Run: $ kubectl delete pod <pod-name>
The pod enters 'Terminating' status. Immediately, the parent ReplicaSet observes current count (3) < desired count (4) and instantly creates a brand-new replacement pod with a new name and IP to maintain the desired count.

---

### Q25. Explain Kubernetes Self-Healing: How does it automatically recover crashed or deleted pods?
**Explanation & Answer:**

Kubernetes continuously executes a reconciliation control loop comparing CURRENT state against DESIRED state. If a container crashes or a pod is deleted, the ReplicaSet controller detects the discrepancy in etcd and schedules a replacement pod on a healthy node automatically.

---

### Q26. How do you scale a Deployment to 4 replicas using kubectl scale? (Exam favorite)
**Explanation & Answer:**

Run: $ kubectl scale deployment oltrs-app --replicas=4
Verify with: $ kubectl get pods
All 4 pods will transition from ContainerCreating to Running status.

---

### Q27. What happens if cluster resources are insufficient when scaling to 4 replicas? (Pending status)
**Explanation & Answer:**

Pods enter 'Pending' status. The kube-scheduler cannot find any worker node with sufficient CPU or memory to host the pod. Diagnose via '$ kubectl describe pod <pending-pod>' which shows 'FailedScheduling: Insufficient memory/cpu'.

---

### Q28. What is a Kubernetes Service, and why is it necessary given that Pods are ephemeral and have dynamic IPs?
**Explanation & Answer:**

A Service is an abstraction that defines a logical set of Pods and a policy to access them. Because Pods are ephemeral and receive new dynamic IPs when replaced, a Service provides a single, permanent IP address and DNS name that load-balances traffic across all matching healthy pods.

---

### Q29. What are the three primary types of Kubernetes Services? (ClusterIP, NodePort, LoadBalancer)
**Explanation & Answer:**

1. ClusterIP (Default): Exposes the service on a cluster-internal IP. Reachable ONLY from within the cluster.
2. NodePort: Exposes the service on each Node's IP at a static port (30000–32767). Accessible from external browsers.
3. LoadBalancer: Provisions a cloud provider's external load balancer (e.g. AWS NLB/ALB) and assigns a public routable IP.

---

### Q30. What is ClusterIP service, and when is it used?
**Explanation & Answer:**

ClusterIP provides an internal virtual IP and DNS name for internal microservice communication (e.g. backend web app connecting to internal MySQL database). It prevents exposing internal databases directly to the public internet.

---

### Q31. What is a NodePort service, and what is the standard port range? (30000–32767)
**Explanation & Answer:**

NodePort allocates a high-range port between 30000 and 32767 on all cluster nodes. External traffic sent to '<NodeIP>:<NodePort>' is automatically routed by kube-proxy to the service's target pods.

---

### Q32. What is a LoadBalancer service, and where is it typically deployed?
**Explanation & Answer:**

LoadBalancer integrates directly with cloud platforms (AWS, GCP, Azure). When created, AWS automatically provisions an Elastic Load Balancer (ELB) pointing to cluster NodePorts, giving the application a globally accessible public DNS endpoint.

---

### Q33. How do you expose a Deployment as a NodePort service using kubectl expose?
**Explanation & Answer:**

Run: $ kubectl expose deployment oltrs-app --type=NodePort --port=8080 --target-port=8080
Verify with: $ kubectl get svc

---

### Q34. How do you retrieve the external browser access URL for a NodePort service in Minikube? (minikube service <name> --url)
**Explanation & Answer:**

Run: $ minikube service oltrs-app --url
Outputs accessible URL: http://192.168.49.2:31254, which can be opened in browser or tested with 'curl -I'.

---

### Q35. What is a Rolling Update in Kubernetes?
**Explanation & Answer:**

A Rolling Update incrementally replaces old pod instances with new pod instances with zero application downtime. Kubernetes spins up new pods, waits for readiness checks to pass, and only then terminates the old pods.

---

### Q36. How do you trigger a rolling update to a new container image using kubectl set image?
**Explanation & Answer:**

Run: $ kubectl set image deployment/oltrs-app oltrs=dheerajmalavath/oltrs:v2
Kubernetes initiates rolling update to version v2.

---

### Q37. How do you monitor rollout progress using kubectl rollout status?
**Explanation & Answer:**

Run: $ kubectl rollout status deployment/oltrs-app
Prints progress: 'Waiting for deployment "oltrs-app" rollout to finish: 2 of 4 updated replicas are available... deployment successfully rolled out'.

---

### Q38. How do you check rollout history using kubectl rollout history?
**Explanation & Answer:**

Run: $ kubectl rollout history deployment/oltrs-app
Displays revision numbers (e.g. 1, 2) and change-cause annotations.

---

### Q39. How do you undo/rollback a failed update in Kubernetes? (kubectl rollout undo)
**Explanation & Answer:**

Run: $ kubectl rollout undo deployment/oltrs-app
Reverts pods back to the previous stable ReplicaSet revision instantly.

---

### Q40. What is a Declarative YAML manifest in Kubernetes?
**Explanation & Answer:**

A YAML manifest defines the desired state of Kubernetes objects (Deployments, Services, ConfigMaps). Rather than typing imperative commands, manifests are version-controlled in Git and applied via 'kubectl apply -f'.

---

### Q41. What are the required top-level fields in any Kubernetes YAML manifest?
**Explanation & Answer:**

1. 'apiVersion': API version (e.g. 'apps/v1' for Deployments, 'v1' for Services/Pods).
2. 'kind': Type of object (Deployment, Service, Pod).
3. 'metadata': Object name, namespace, labels.
4. 'spec': Desired state specification (replicas, containers, ports, selectors).

---

### Q42. What is the purpose of Labels and Selectors (matchLabels) in Kubernetes YAML?
**Explanation & Answer:**

Labels are key-value tags attached to objects (e.g. 'app: oltrs'). Selectors ('matchLabels') are queries used by Deployments and Services to identify and group which Pods they control and route traffic to.

---

### Q43. How do you apply YAML configuration files using kubectl apply -f?
**Explanation & Answer:**

Run: $ kubectl apply -f deployment.yaml
Creates or updates the resource to match the YAML specification without deleting existing unaffected state.

---

### Q44. What is a Namespace in Kubernetes, and what are the default namespaces?
**Explanation & Answer:**

A Namespace provides logical cluster partitioning and resource isolation within a physical cluster.
Default namespaces: (1) 'default' (user workloads), (2) 'kube-system' (control plane components), (3) 'kube-public', and (4) 'kube-node-lease'.

---

### Q45. What is a ConfigMap, and how does it decouple configuration from container images?
**Explanation & Answer:**

A ConfigMap stores non-confidential configuration data as key-value pairs (e.g. DB URLs, app settings). Pods consume ConfigMaps as environment variables or mounted files, allowing application configurations to change without rebuilding container images.

---

### Q46. What is a Kubernetes Secret, and how does it store sensitive data?
**Explanation & Answer:**

A Secret stores confidential data (passwords, tokens, SSH keys, TLS certs) encoded in Base64. Secrets are mounted into pod memory (tmpfs) rather than written to persistent node storage, minimizing exposure risk.

---

### Q47. What is a PersistentVolume (PV) and PersistentVolumeClaim (PVC)?
**Explanation & Answer:**

• PersistentVolume (PV): A piece of storage provisioned in the cluster (e.g. AWS EBS, NFS, local disk).
• PersistentVolumeClaim (PVC): A request for storage by a developer (requesting e.g. 10Gi with ReadWriteOnce access). Kubernetes binds matching PVCs to PVs.

---

### Q48. What is a Liveness Probe vs a Readiness Probe in Kubernetes?
**Explanation & Answer:**

• Liveness Probe: Checks if container is alive. If probe fails, kubelet kills the container and restarts it according to restartPolicy.
• Readiness Probe: Checks if application is ready to accept user network traffic. If probe fails, the service stops routing traffic to the pod until it recovers.

---

### Q49. What does 'kubectl get all' show?
**Explanation & Answer:**

Returns a comprehensive snapshot of all resources in the active namespace: pods, services, daemonsets, deployments, and replicasets.

---

### Q50. How do you cleanly delete a Deployment and its associated Service?
**Explanation & Answer:**

Run:
$ kubectl delete deployment oltrs-app
$ kubectl delete service oltrs-app
Terminates all pods, stops traffic routing, and frees cluster resources.

---


## Topic 7: Nagios Infrastructure & Service Monitoring (50 Questions)

### Q1. What is Nagios, and what is its role in DevOps infrastructure management?
**Explanation & Answer:**

Nagios is an industry-standard open-source IT infrastructure monitoring and alerting engine. It monitors mission-critical servers, switches, applications, containers, and network protocols, proactively alerting system administrators via email/SMS when failures occur and when services recover.

---

### Q2. What are the main benefits of using Nagios for IT infrastructure monitoring?
**Explanation & Answer:**

• Proactive Outage Detection: Detects hardware, server, or container downtime before end-users notice.
• Root-Cause Analysis: Distinguishes between network path failure and actual host failure (network topology mapping).
• SLA & Availability Reporting: Generates uptime and compliance reports.
• Extensible Plugin Architecture: Any script returning standard exit codes (0, 1, 2, 3) can act as a custom Nagios monitoring plugin.

---

### Q3. How is Nagios deployed in a containerized environment using Docker on Ubuntu?
**Explanation & Answer:**

Run the following terminal command:
$ docker run -d --name nagios --restart=always -p 8090:80 jasonrivers/nagios:latest
Runs Nagios Core web server on host port 8090.

---

### Q4. What host port is typically mapped to Nagios container port 80? (8090:80)
**Explanation & Answer:**

Host port 8090 is mapped to container port 80 ('-p 8090:80') to avoid port collisions with host Apache/Nginx web servers or default port 80.

---

### Q5. What are the default login credentials for the Nagios Core web interface?
**Explanation & Answer:**

• Username: 'nagiosadmin'
• Password: 'nagios'
Configured in the container's '/etc/nagios/htpasswd.users' Apache basic authentication file.

---

### Q6. What is the URL to access Nagios dashboard locally? (http://localhost:8090)
**Explanation & Answer:**

Open any web browser on Ubuntu and navigate to: 'http://localhost:8090' (or 'http://<server-ip>:8090').

---

### Q7. What is the Tactical Overview in the Nagios web console?
**Explanation & Answer:**

Tactical Overview is the main executive dashboard screen. It summarizes the overall health of the monitored environment in a grid of gauges, displaying total host and service counts grouped by status (Up, Down, Unreachable, OK, Warning, Critical, Unknown).

---

### Q8. What information is displayed in the 'Hosts' view in Nagios?
**Explanation & Answer:**

Lists all monitored host machines/devices, showing: Host Name, Status (UP/DOWN/UNREACHABLE), Last Check timestamp, Duration in current state, and Status Information output from the host check command (e.g. 'PING OK - Packet loss = 0%').

---

### Q9. What information is displayed in the 'Services' view in Nagios?
**Explanation & Answer:**

Lists all monitored service checks grouped by host. Displays: Host, Service Description (e.g. HTTP, SSH, Root Partition), Status (OK/WARNING/CRITICAL/UNKNOWN), Last Check time, Duration, Attempt count (e.g. 1/3), and plugin performance data.

---

### Q10. What does the 'Service Problems' section show in the Nagios dashboard?
**Explanation & Answer:**

Provides a filtered alert view showing ONLY services currently in non-OK states (WARNING, CRITICAL, or UNKNOWN), allowing operations engineers to focus immediately on active failures.

---

### Q11. What is the Event Log in Nagios, and how is it used during troubleshooting?
**Explanation & Answer:**

The Event Log is a chronological audit record of all internal monitoring events: check executions, status transitions (OK → CRITICAL), notification emails dispatched, system shutdowns, and flap detections.

---

### Q12. What does the 'Notifications' view show in Nagios?
**Explanation & Answer:**

Displays historical records of all alert notifications dispatched to contacts, indicating contact name, host/service, notification type (PROBLEM/RECOVERY), and timestamp.

---

### Q13. What is the Nagios Map feature?
**Explanation & Answer:**

Map generates a visual network topology graph showing relationships and parent-child dependencies between routers, switches, and servers, visually highlighting which device failure caused dependent nodes to become unreachable.

---

### Q14. Explain the four Nagios service status codes, labels, and dashboard colors: 0, 1, 2, 3.
**Explanation & Answer:**

• 0: OK (Green) — Service is functioning normally within threshold limits.
• 1: WARNING (Yellow) — Service is functional but approaching critical thresholds (e.g. disk 85% full).
• 2: CRITICAL (Red) — Service is down, unresponsive, or exceeding critical threshold (e.g. HTTP 500 error, port closed).
• 3: UNKNOWN (Orange) — Plugin syntax error or plugin failed to execute properly.

---

### Q15. What are the two types of host status in Nagios? (UP, DOWN, UNREACHABLE)
**Explanation & Answer:**

• UP: Host is responding to ping/check commands.
• DOWN: Host is unresponsive, and all parent routers/switches are UP (the host itself has died).
• UNREACHABLE: Host is unresponsive, but its parent gateway/router is ALSO down (network path broken, host may still be alive).

---

### Q16. What is a 'Soft State' vs a 'Hard State' in Nagios?
**Explanation & Answer:**

• Soft State: A service or host fails a check, but has not yet exceeded 'max_check_attempts'. Nagios retries checks at 'retry_interval' without sending alerts.
• Hard State: Failure persists beyond 'max_check_attempts' (e.g. 3 consecutive failed checks). Nagios records a permanent hard failure and immediately dispatches alerts.

---

### Q17. What is 'max_check_attempts', and how does it transition a Soft state to a Hard state?
**Explanation & Answer:**

'max_check_attempts' defines how many consecutive times a check must fail before triggering an alert. If set to 3, attempt 1/3 (Soft) → attempt 2/3 (Soft) → attempt 3/3 (Hard State triggered → email sent).

---

### Q18. Where are Nagios configuration files located inside the container? (/opt/nagios/etc/)
**Explanation & Answer:**

Inside the container at '/opt/nagios/etc/'. Key object definition files reside under '/opt/nagios/etc/objects/'.

---

### Q19. What is 'nagios.cfg', and what role does it play?
**Explanation & Answer:**

'nagios.cfg' is the primary master configuration file. It controls daemon behavior, specifies log file locations, sets check intervals, and includes all object definition configuration files via 'cfg_file=' directives.

---

### Q20. What is the purpose of 'objects/hosts.cfg'?
**Explanation & Answer:**

Defines physical and virtual machines to be monitored, including hostnames, IP addresses, parent relationships, check intervals, and contact groups.

---

### Q21. What is the purpose of 'objects/services.cfg'?
**Explanation & Answer:**

Defines specific checks performed against monitored hosts (e.g. checking HTTP on port 9090, ping latency, SSH responsiveness, disk usage).

---

### Q22. What is the purpose of 'objects/commands.cfg'?
**Explanation & Answer:**

Maps high-level check commands (e.g. 'check_http') to physical executable plugin binaries and arguments on disk (e.g. '$USER1$/check_http -H $HOSTADDRESS$ -p $ARG1$').

---

### Q23. What is the purpose of 'objects/contacts.cfg' and 'contactgroups.cfg'?
**Explanation & Answer:**

'contacts.cfg' defines administrator identities, email addresses, and notification time periods. 'contactgroups.cfg' bundles contacts into logical teams (e.g. devops-admins).

---

### Q24. What is the purpose of 'objects/templates.cfg'?
**Explanation & Answer:**

Contains common object templates ('linux-server', 'generic-service') defining default check intervals, retry attempts, and notification periods inherited by other definitions via 'use <template>'.

---

### Q25. How do you define a monitored host in Nagios? (Explain fields)
**Explanation & Answer:**

define host {
    use                     linux-server
    host_name               oltrs-web-app
    alias                   Online Ticket Reservation
    address                 172.17.0.1
    max_check_attempts      3
    check_period            24x7
    notification_interval   30
    notification_period     24x7
}

---

### Q26. How do you define a monitored service in Nagios? (Explain fields)
**Explanation & Answer:**

define service {
    use                     generic-service
    host_name               oltrs-web-app
    service_description     HTTP Port 9090 Status
    check_command           check_http!-p 9090 -u /ROOT/
    check_interval          1
    retry_interval          1
    max_check_attempts      2
    notification_period     24x7
}

---

### Q27. What is a Nagios Plugin?
**Explanation & Answer:**

A Nagios Plugin is an independent executable program or script (written in C, Bash, Python, or Perl) that performs a specific monitoring test and exits with a standardized exit code (0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN) along with a single line of status text on stdout.

---

### Q28. Where are standard Nagios plugins installed? (/opt/nagios/libexec/)
**Explanation & Answer:**

In the container, plugins reside at '/opt/nagios/libexec/' (referenced by the macro '$USER1$'). On native Ubuntu, they are at '/usr/lib/nagios/plugins/'.

---

### Q29. What does the 'check_ping' plugin do, and what are warning/critical arguments?
**Explanation & Answer:**

'check_ping' sends ICMP ECHO packets to test network reachability, packet loss, and round-trip time (RTT).
Syntax: 'check_ping -H <ip> -w <rtt,loss%> -c <rtt,loss%>'.
Example: '-w 100.0,20% -c 500.0,60%' triggers Warning if latency exceeds 100ms or loss >20%; Critical if >500ms or >60%.

---

### Q30. What does the 'check_http' plugin do, and how do you monitor a specific port (e.g. 9090)?
**Explanation & Answer:**

'check_http' connects to an HTTP/HTTPS web server, verifies TCP port connection, and validates HTTP status codes (expecting 200/300).
To check port 9090: 'check_http!-p 9090 -u /ROOT/'.

---

### Q31. What does the 'check_ssh' plugin do?
**Explanation & Answer:**

'check_ssh' connects to TCP port 22 on the target host and validates that the SSH server banner (e.g. OpenSSH_8.9) is returned.

---

### Q32. What does the 'check_disk' plugin do?
**Explanation & Answer:**

'check_disk' checks available storage space on local filesystem mount points, triggering Warning/Critical when free disk space falls below thresholds (e.g. '-w 15% -c 5%').

---

### Q33. What does the 'check_tcp' plugin do?
**Explanation & Answer:**

'check_tcp -H <ip> -p <port>' attempts a raw TCP socket connection on the specified port (useful for MySQL port 3306 or Redis port 6379).

---

### Q34. How do you write a custom Nagios plugin script? (Exit codes: 0, 1, 2, 3)
**Explanation & Answer:**

Write a shell script that performs a check, prints a summary message, and exits with:
• exit 0 for OK
• exit 1 for WARNING
• exit 2 for CRITICAL
• exit 3 for UNKNOWN

---

### Q35. How do you run the pre-flight verification command to test Nagios configuration syntax?
**Explanation & Answer:**

Execute inside the container:
$ docker exec -it nagios /opt/nagios/bin/nagios -v /opt/nagios/etc/nagios.cfg
Validates syntax across all configuration files and reports 'Total Errors: 0'.

---

### Q36. Why is running pre-flight verification essential before restarting Nagios?
**Explanation & Answer:**

If a configuration file has a syntax error or missing closing bracket, restarting Nagios will cause the daemon to crash immediately and fail to start, leaving the entire infrastructure unmonitored.

---

### Q37. How do you reload or restart Nagios to apply configuration changes?
**Explanation & Answer:**

Restart the container or send SIGHUP:
$ docker restart nagios
Or inside container: $ /etc/init.d/nagios reload

---

### Q38. What is Active Checking vs Passive Checking in Nagios?
**Explanation & Answer:**

• Active Checking: Nagios daemon initiates checks on a scheduled polling timer (e.g. every 5 minutes) by invoking plugins.
• Passive Checking: External applications or remote hosts initiate checks asynchronously and push results back to Nagios via NSCA (Nagios Service Check Acceptor).

---

### Q39. What is NRPE (Nagios Remote Plugin Executor), and why is it used?
**Explanation & Answer:**

NRPE is an addon that allows Nagios to execute plugins on remote Linux/Ubuntu hosts to monitor local resources that cannot be queried over the network (e.g. CPU load, memory usage, local disk space).

---

### Q40. How does NRPE execute plugins on remote Ubuntu servers?
**Explanation & Answer:**

The Nagios server runs 'check_nrpe', which connects via SSL to the 'nrpe' daemon on the remote Ubuntu host. The remote daemon runs the local plugin and returns the exit code and text output back to the Nagios server.

---

### Q41. What is NSClient++, and what operating system is it used for? (Windows monitoring)
**Explanation & Answer:**

NSClient++ is a lightweight monitoring agent installed on Microsoft Windows servers to allow Nagios to monitor Windows performance counters, Event Logs, and Windows Services.

---

### Q42. What is check scheduling in Nagios? (check_interval and retry_interval)
**Explanation & Answer:**

• 'check_interval': The normal polling interval (in minutes) when the service is in an OK state (e.g. check every 5 minutes).
• 'retry_interval': The aggressive polling interval (e.g. every 1 minute) used when a service enters a Soft failure state until max_check_attempts is reached.

---

### Q43. What is flapping in Nagios monitoring, and how does flap detection prevent alert spam?
**Explanation & Answer:**

Flapping occurs when a service rapidly switches between OK and CRITICAL states (e.g. intermittent network cable). Flap detection tracks state change history percentage; when flapping is detected, Nagios temporarily suppresses email notifications to prevent alert storms.

---

### Q44. How does Nagios send email alerts to system administrators?
**Explanation & Answer:**

When a Hard failure triggers, Nagios passes contact email, host details, and alert text to a local mail transport agent (like 'mail' or 'sendmail') defined in 'commands.cfg' under 'notify-service-by-email'.

---

### Q45. How do you configure Nagios alongside application containers in Docker Compose (SET 8)?
**Explanation & Answer:**

Add a 'nagios' service in 'docker-compose.yml' connected to the same custom bridge network as the application container. Nagios uses the Docker service name (e.g. 'http://app:8080') to monitor the application container directly.

---

### Q46. How does Nagios communicate with target containers on the same Docker bridge network?
**Explanation & Answer:**

Containers on the same user-defined bridge network communicate via Docker's embedded DNS. Nagios resolves the target container name to its container IP directly.

---

### Q47. How do you schedule maintenance downtime for a host in Nagios to silence alerts?
**Explanation & Answer:**

In the Nagios Web UI: Navigate to Host → Click 'Schedule downtime for this host' → Specify start time, end time, and comment. Nagios continues monitoring during this window but suppresses all email notifications.

---

### Q48. What is an escalation in Nagios notification rules?
**Explanation & Answer:**

Escalations define rules where notifications are sent to higher-level management or on-call engineers if an alert remains unacknowledged in CRITICAL state after a specified duration.

---

### Q49. What are the primary differences between Nagios Core and Nagios XI?
**Explanation & Answer:**

• Nagios Core: Free, open-source command-line-driven monitoring daemon with basic web interface.
• Nagios XI: Commercial enterprise edition featuring automated configuration wizards, database backend, advanced reporting, graphical dashboard designer, and role-based access control.

---

### Q50. How does Nagios compare with modern observability tools like Prometheus and Grafana?
**Explanation & Answer:**

Nagios is primarily a host/service status monitoring and alerting tool based on discrete checks. Prometheus is a time-series metric aggregation database that scrapes continuous telemetry metrics (CPU%, latency percentiles) paired with Grafana for rich dynamic metric visualization.

---


## Topic 8: AWS EC2 & Cloud Infrastructure Deployment (50 Questions)

### Q1. What is Cloud Computing, and what are the three main service models? (IaaS, PaaS, SaaS)
**Explanation & Answer:**

Cloud Computing is the on-demand delivery of compute power, database storage, applications, and other IT resources via the internet with pay-as-you-go pricing.
• Infrastructure as a Service (IaaS, e.g. AWS EC2): Provides raw virtual servers, storage, and networking; user manages OS and software.
• Platform as a Service (PaaS, e.g. AWS Elastic Beanstalk, Heroku): Provides a managed platform for deploying code without managing underlying servers.
• Software as a Service (SaaS, e.g. Gmail, Microsoft 365): Complete end-user applications managed by provider.

---

### Q2. What is Amazon Web Services (AWS)?
**Explanation & Answer:**

AWS is Amazon's comprehensive, globally distributed cloud computing platform offering over 200 fully featured services including compute (EC2), storage (S3, EBS), database (RDS), networking (VPC), and developer automation tools.

---

### Q3. What is Amazon EC2 (Elastic Compute Cloud)?
**Explanation & Answer:**

Amazon EC2 provides resizable compute capacity in the cloud. It allows users to launch virtual servers (called 'EC2 instances') with customized operating systems, CPU, memory, storage, and security controls within minutes.

---

### Q4. What is an AMI (Amazon Machine Image)?
**Explanation & Answer:**

An AMI is a pre-configured template that contains the operating system, architecture, and installed software needed to launch an EC2 instance. It acts as a master disk image blueprint (e.g. Ubuntu Server 22.04 LTS).

---

### Q5. Which AMI is used in our laboratory sessions? (Ubuntu Server 22.04 LTS HVM)
**Explanation & Answer:**

Ubuntu Server 22.04 LTS (HVM), SSD Volume Type, 64-bit (x86). It provides a stable, enterprise-grade Linux environment with 5-year long-term support and complete compatibility with Docker and Git.

---

### Q6. What is an EC2 Instance Type, and what does 't2.micro' signify?
**Explanation & Answer:**

Instance types represent hardware configurations optimized for different workloads.
• 't': Burstable general-purpose instance family.
• '2': Generation number (second generation).
• 'micro': Size designation providing 1 vCPU and 1 GiB of RAM.

---

### Q7. What are the specifications of t2.micro, and why is it chosen for student labs?
**Explanation & Answer:**

Specifications: 1 vCPU, 1 GiB Memory, EBS storage only, Low to Moderate network performance. It is chosen because it is 100% Free Tier eligible, allowing students to complete laboratory exercises without incurring cloud charges.

---

### Q8. What is AWS Free Tier, and what are its limits for EC2?
**Explanation & Answer:**

AWS Free Tier provides new accounts with 750 hours per month of Linux and Windows t2.micro (or t3.micro) instances for 12 months, along with 30 GiB of EBS storage, 500 MB container registry storage, and 15 GB data transfer out.

---

### Q9. What is an AWS Region vs an Availability Zone (AZ)?
**Explanation & Answer:**

• AWS Region: A separate geographic area in the world (e.g. 'ap-south-1' Mumbai or 'us-east-1' N. Virginia) containing multiple physical data centers.
• Availability Zone (AZ): One or more discrete data centers within a region with redundant power, networking, and connectivity (e.g. 'ap-south-1a', 'ap-south-1b').

---

### Q10. Why should you select a region geographically close to you (e.g. ap-south-1 Mumbai)?
**Explanation & Answer:**

Selecting a nearby region minimizes network latency (faster SSH terminal response and web page loading) and complies with local data residency regulations.

---

### Q11. What is a Key Pair in AWS EC2?
**Explanation & Answer:**

A Key Pair consists of a public key stored on the EC2 instance and a private key file ('.pem') downloaded to the developer's computer. It uses asymmetric cryptography to authenticate SSH connections securely without transmitting passwords over the network.

---

### Q12. What key format is downloaded for SSH on Ubuntu/Linux? (.pem format)
**Explanation & Answer:**

The '.pem' (Privacy Enhanced Mail) format, containing an OpenSSH RSA or ED25519 private key. (The '.ppk' format is used specifically for PuTTY on Windows).

---

### Q13. What encryption algorithm is used by default for EC2 key pairs? (RSA or ED25519)
**Explanation & Answer:**

RSA (Rivest-Shamir-Adleman, 2048-bit) or ED25519. Both provide strong public-key cryptographic authentication.

---

### Q14. Why does SSH fail with 'UNPROTECTED PRIVATE KEY FILE' on Ubuntu if key permissions are not modified?
**Explanation & Answer:**

The OpenSSH client on Ubuntu strictly enforces permission checks on private key files. If the file permissions are accessible by group or others (e.g. default 0644 or 0755), SSH refuses to use the key because it is insecure, aborting with 'Permission denied (publickey)'.

---

### Q15. What exact command fixes private key permissions on Ubuntu? (chmod 400 ~/.ssh/key.pem)
**Explanation & Answer:**

Run: $ chmod 400 ~/.ssh/devops-key.pem
This sets permissions to read-only for the owner and denies all permissions to group and others ('-r--------').

---

### Q16. What is the SSH command to connect to an Ubuntu EC2 instance from Ubuntu terminal?
**Explanation & Answer:**

Run:
$ ssh -i ~/.ssh/devops-key.pem ubuntu@<EC2-PUBLIC-IP>
Where '-i' specifies the identity private key file, 'ubuntu' is the login user, and '<EC2-PUBLIC-IP>' is the instance's public IPv4 address.

---

### Q17. What is the default SSH username for Ubuntu AMI vs Amazon Linux AMI? (ubuntu vs ec2-user)
**Explanation & Answer:**

• Ubuntu Server AMI: 'ubuntu'
• Amazon Linux / RHEL / CentOS AMI: 'ec2-user'
Using the wrong username causes 'Permission denied (publickey)' errors.

---

### Q18. What is EC2 Instance Connect, and how does it allow browser-based terminal access?
**Explanation & Answer:**

EC2 Instance Connect is an AWS browser-based terminal client that pushes a temporary single-use SSH public key to instance metadata for 60 seconds, allowing users to connect directly from the AWS Console without needing a local SSH client or downloaded '.pem' file.

---

### Q19. What is a VPC (Virtual Private Cloud)?
**Explanation & Answer:**

Amazon VPC is a logically isolated virtual network dedicated to your AWS account, resembling a traditional physical data center network. You control IP address ranges, subnets, route tables, and network gateways.

---

### Q20. What is a Subnet in AWS VPC? (Public Subnet vs Private Subnet)
**Explanation & Answer:**

A Subnet is a segment of a VPC's IP address range designated to a specific Availability Zone.
• Public Subnet: Has a direct route to an Internet Gateway (IGW); instances receive public IPs accessible from the internet.
• Private Subnet: Has no direct route to the internet; used for backend databases and private microservices.

---

### Q21. What is an Internet Gateway (IGW)?
**Explanation & Answer:**

An Internet Gateway is a horizontally scaled, redundant VPC component that enables communication between instances in your VPC and the internet, performing network address translation (NAT) between private and public IPv4 addresses.

---

### Q22. What is a Security Group in AWS?
**Explanation & Answer:**

A Security Group acts as a virtual firewall for your EC2 instance to control incoming and outgoing network traffic at the hypervisor level.

---

### Q23. Are AWS Security Groups stateful or stateless? What does stateful mean?
**Explanation & Answer:**

Security Groups are STATEFUL. 'Stateful' means that if you allow an inbound request (e.g. incoming HTTP traffic on port 80), the response traffic is automatically allowed outbound, regardless of outbound rules.

---

### Q24. What is an Inbound Rule vs an Outbound Rule in a Security Group?
**Explanation & Answer:**

• Inbound Rule: Filters traffic coming INTO the instance from external networks (e.g. allowing port 22 for SSH or port 9090 for web app).
• Outbound Rule: Filters traffic originating from inside the instance going OUT to external networks (e.g. downloading software packages).

---

### Q25. By default, what inbound traffic is allowed in a newly created Security Group? (None, all blocked)
**Explanation & Answer:**

By default, a new custom security group has NO inbound rules. All incoming traffic from the internet is completely blocked until explicit rules are added.

---

### Q26. By default, what outbound traffic is allowed in a newly created Security Group? (All outbound allowed)
**Explanation & Answer:**

By default, an outbound rule allows ALL IPv4 traffic ('0.0.0.0/0') on all ports and protocols to leave the instance.

---

### Q27. Why must Port 22 be open in the Security Group? (SSH remote access)
**Explanation & Answer:**

TCP Port 22 is the standard port used by the Secure Shell (SSH) protocol. If Port 22 is closed, all SSH terminal connection attempts will time out.

---

### Q28. Why must Port 80 and 443 be open?
**Explanation & Answer:**

• Port 80: Standard unencrypted HTTP web traffic.
• Port 443: Standard encrypted HTTPS (SSL/TLS) web traffic.

---

### Q29. You deploy an application on EC2 on port 9090, but the browser times out with ERR_CONNECTION_TIMED_OUT. What is the root cause?
**Explanation & Answer:**

The EC2 instance's Security Group does not have an Inbound Rule allowing incoming TCP traffic on port 9090. The AWS hypervisor drops all packets destined for port 9090, causing the browser to hang and time out.

---

### Q30. Step-by-step, how do you add a Custom TCP inbound rule for port 9090 in AWS Management Console?
**Explanation & Answer:**

1. In EC2 Console left sidebar → Under 'Network & Security', click 'Security Groups'.
2. Click your instance's security group name → Click 'Inbound rules' tab in lower panel.
3. Click 'Edit inbound rules' → Click 'Add rule' at bottom.
4. Set Type: 'Custom TCP' | Port range: '9090' | Source: 'Anywhere-IPv4' (0.0.0.0/0).
5. Click orange 'Save rules' button. Port unblocks instantly.

---

### Q31. What does 0.0.0.0/0 mean in CIDR notation for Security Group source?
**Explanation & Answer:**

'0.0.0.0/0' represents all possible IPv4 addresses in the world. In a security group rule, it means the port is open to incoming requests from any computer on the public internet.

---

### Q32. What is Public IPv4 Address vs Private IPv4 Address on EC2?
**Explanation & Answer:**

• Public IPv4 Address: Routable over the global internet. Used by users, browsers, and remote developers to connect to the instance.
• Private IPv4 Address: Routable only within the VPC network (e.g. 172.31.x.x). Used for secure inter-instance communication within AWS.

---

### Q33. What happens to the Public IPv4 address when an EC2 instance is stopped and started?
**Explanation & Answer:**

The instance releases its dynamic Public IPv4 address back to the AWS pool! When started again, AWS assigns a BRAND-NEW public IP address, breaking existing SSH bookmarks and web URLs.

---

### Q34. What is an Elastic IP address in AWS?
**Explanation & Answer:**

An Elastic IP is a static, persistent public IPv4 address allocated to your AWS account that does NOT change when the instance is stopped, restarted, or rebooted.

---

### Q35. How does an Elastic IP address solve the problem of changing public IP addresses?
**Explanation & Answer:**

Because an Elastic IP remains permanently tied to your AWS account and instance, DNS records and client bookmarks continue working seamlessly across instance stop/start events.

---

### Q36. How do you allocate and associate an Elastic IP address in AWS Management Console?
**Explanation & Answer:**

1. EC2 Console left sidebar → 'Elastic IPs' → Click 'Allocate Elastic IP address' → Click 'Allocate'.
2. Select the allocated IP → Click 'Actions' dropdown → Click 'Associate Elastic IP address'.
3. Choose Resource type: 'Instance' → Select your running EC2 instance → Click 'Associate'.

---

### Q37. Does AWS charge for an allocated Elastic IP that is NOT associated with a running instance?
**Explanation & Answer:**

YES! AWS charges a small hourly fee for Elastic IPs that are allocated but NOT attached to a running instance, to discourage hoarding scarce public IPv4 addresses.

---

### Q38. What is Amazon EBS (Elastic Block Store)?
**Explanation & Answer:**

Amazon EBS provides persistent, raw block-level network storage volumes attached to EC2 instances, functioning like a physical virtual hard disk (SSD/HDD).

---

### Q39. What is the difference between EBS root volume and instance store?
**Explanation & Answer:**

• EBS Volume: Network-attached persistent storage. Data survives instance stop/start cycles.
• Instance Store (ephemeral): Physically attached directly to host server hardware. Data is permanently wiped when the instance is stopped.

---

### Q40. How do you ensure database data persists across EC2 instance stop and start cycles?
**Explanation & Answer:**

Store the database files on an Amazon EBS volume (the default root volume or an attached EBS secondary volume) with 'Delete on Termination' disabled.

---

### Q41. What is the difference between 'Stopping' an EC2 instance and 'Terminating' an EC2 instance?
**Explanation & Answer:**

• Stopping: Shuts down instance compute. EBS storage remains intact and incurs standard storage fees. Can be restarted later.
• Terminating: Permanently deletes the virtual server and attached root volume. The instance cannot be recovered, and all billing halts completely.

---

### Q42. Why must students always 'Terminate' EC2 instances at the end of their lab exam? (To prevent unexpected billing)
**Explanation & Answer:**

Stopped instances still consume EBS storage allocation and can incur charges if left unattended. Terminating the instance releases all compute and storage resources, completely eliminating bill shock.

---

### Q43. How do you install Docker, Git, Java, and Maven inside an Ubuntu EC2 instance?
**Explanation & Answer:**

Execute inside the EC2 SSH shell:
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install -y docker.io git openjdk-17-jdk maven
$ sudo systemctl enable --now docker

---

### Q44. Why must you run 'sudo usermod -aG docker ubuntu && newgrp docker' on EC2?
**Explanation & Answer:**

By default, only root can interact with the Docker daemon. Adding the 'ubuntu' user to the 'docker' group allows running docker commands without typing 'sudo'.

---

### Q45. How do you clone a GitHub repository and build a project inside an EC2 instance?
**Explanation & Answer:**

$ git clone https://github.com/archanareddyse/OLTRS.git
$ cd OLTRS
$ mvn clean package -DskipTests
Builds the WAR file inside 'target/' on the EC2 instance.

---

### Q46. How do you run a multi-container Docker application using Docker Compose inside an EC2 instance?
**Explanation & Answer:**

Create 'docker-compose.yml' using nano on EC2:
$ nano docker-compose.yml
Then start the multi-container application:
$ docker compose up -d

---

### Q47. What is AWS IAM (Identity and Access Management)?
**Explanation & Answer:**

AWS IAM is a web service that helps you securely control access to AWS resources. It manages authentication (who can sign in) and authorization (what permissions and policies they possess).

---

### Q48. What is the difference between an IAM User and an IAM Role?
**Explanation & Answer:**

• IAM User: An identity with long-term credentials (password, access keys) used by a specific human developer.
• IAM Role: An identity with short-term, temporary credentials assigned to an AWS service (such as an EC2 instance) allowing it to securely access S3 or DynamoDB without hardcoding access keys.

---

### Q49. Why should you never use root AWS account credentials for day-to-day deployment tasks?
**Explanation & Answer:**

The root account has unrestricted, god-mode access to all billing and cloud resources. If leaked or compromised, attackers can delete all infrastructure or launch expensive cryptomining farms. Principle of Least Privilege dictates using IAM users.

---

### Q50. What is Amazon CloudWatch, and how does it monitor EC2 instance CPU utilization and status checks?
**Explanation & Answer:**

Amazon CloudWatch is AWS's native monitoring service. It automatically collects EC2 telemetry metrics every 5 minutes (or 1 minute with detailed monitoring), tracking CPUUtilization, NetworkIn/Out, DiskRead/Write, and System/Instance Status Checks, triggering alarms when thresholds are breached.

---

