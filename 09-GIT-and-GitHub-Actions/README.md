# 09 - Git and GitHub (Contributing to Projects)

## Module Goal

This module documents my fundamental understanding of Git as a version control system and GitHub as a collaboration platform, including how to contribute to external repositories through forks, branches and pull requests. It reflects a working knowledge level: I understand the core workflow and can describe why each step matters, without yet having deep experience maintaining large-scale collaborative projects.

---

## Git vs GitHub

It's important not to confuse these two terms:

- **Git**: a distributed version control system installed locally, used to track the history of changes, branches and versions of code.
- **GitHub**: a cloud platform that hosts Git repositories, enabling team collaboration, remote access to code, and extra tools like Pull Requests, Issues and Actions.

GitHub is the most popular option (backed by Microsoft). GitLab is a strong alternative, along with Bitbucket and Azure Repos.

---

## How Git Really Works

Git doesn't work like a simple timeline — it behaves more like a graph of changes, where a main branch forks off, accumulates commits, and later converges again through a merge or pull request.

Typical flow:
```
Remote repository (upstream) → Fork (your own copy) → Clone (local copy)
→ Working branch → Local commits → Push to your remote → Pull Request to base repo
```

### Fork vs Clone
- **Fork**: creates a copy of the repository under your own GitHub account. This happens on GitHub's servers and gives you full ownership over that copy.
- **Clone**: downloads a repository (with its full history) to your local machine so you can work on it. Cloning does **not** give you write access to the original repository.

---

## Exploring a GitHub Repository

- **Code**: files, folders and commit history.
- **Issues**: report bugs, suggest improvements, or ask questions.
- **Pull Requests**: where proposed code is reviewed, discussed and merged.
- **Actions**: CI/CD automation tool to build, test or deploy code automatically.
- **Projects**: Kanban-style boards to organize and prioritize work.
- **Wiki**: extended documentation space for the project.
- **Security**: tools to detect vulnerabilities in code, dependencies or exposed secrets.
- **Insights**: statistics about repository activity and contributions.

---

## Core Workflow Concepts

| Concept | What it actually does | When to use it |
|---|---|---|
| **Clone** | Copies the remote repo to your machine | To start working locally |
| **Branch** | Isolates a line of work from `main` | For features, fixes, small PRs |
| **Commit** | Records a small, traceable unit of change | After every meaningful change |
| **Push** | Publishes your commits to a remote you control | To back up work / open a PR |
| **Pull Request (PR)** | Requests to merge your branch into a target branch | Once your changes are ready for review |
| **Upstream** | The original remote repo you forked from | To sync your fork with the latest changes |

---

## GitHub Flow

The course favors **GitHub Flow** over more complex models like GitFlow, especially for modern web projects. GitHub Flow is a lightweight, branch-based workflow that supports frequent deployments:

- Create short, descriptive branches.
- Commit frequently.
- Open Pull Requests early (even as **Draft PRs**) to encourage discussion.
- Merge into the main branch only after the code has been reviewed and tested.
- Keep `main` always in a deployable state.

The longer a branch lives, the more it drifts from `main`, generating more conflicts and making integration more expensive — hence the preference for short-lived branches and small PRs.

---

## Standard Workflow to Contribute to an External Repository

```bash
# 1. Clone your fork (not the original repo) using SSH
git clone --depth 1 git@github.com:your-username/project.git
cd project

# 2. Add the original repository as "upstream"
git remote add upstream git@github.com:original-owner/project.git

# 3. Check configured remotes
git remote -v

# 4. Create a new branch and switch to it
git switch -c fix/accessibility-issues

# 5. Check the current status
git status

# 6. Stage and commit your changes
git add file
git commit -m "fix: improve accessibility labels"

# 7. Push to your own fork
git push origin fix/accessibility-issues
```

Then open a **Compare & pull request** from GitHub (or from your editor) targeting the base repository.

> Note: `git checkout` is considered outdated because it tried to do multiple unrelated things at once. The modern approach uses `git switch` for changing branches and `git restore` for restoring files.

---

## Keeping Your Fork in Sync

```bash
git fetch upstream        # Get new changes from the original repo
git switch main           # Switch to your local main branch
git pull upstream main    # Merge new changes locally
git push origin main      # Update your fork on GitHub
```

Alternatively, GitHub's web interface offers a **"Sync fork"** button that does this automatically.

---

## Common Software Licenses

| License | Type |
|---|---|
| **MIT** | Very permissive and simple |
| **Apache 2.0** | Permissive, with patent protection clauses |
| **GNU GPLv3** | Copyleft — derivatives must keep the same license |
| **BSD** | Permissive, minimal restrictions |
| **Creative Commons** | Common for documentation/creative assets, less common for pure code |

---

## Best Practices for Successful Pull Requests

- Be surgical: focus on a single issue per PR.
- Be explicit: PRs should be short but well explained.
- Avoid noisy commits: don't add trivial or unrelated commits to the history.
- Keep changes to a minimum — if you spot another improvement, open a separate PR.
- Coordinate with maintainers before large changes.
- Read the project's `CONTRIBUTING.md` before contributing; it defines the operational rules of the project.
- After a PR is merged, delete the feature branch to keep the repository clean.

---

## Advanced Tools and Environments

- **Multiple remotes**: it's possible to configure more than `origin` and `upstream` using `git remote add`.
- **GitHub Desktop**: a visual app to manage repositories without relying solely on the terminal.
- **GitHub Codespaces**: a full cloud development environment (with free monthly hours), useful for contributing without local setup.
- **GitHub CLI (`gh`)**: simplifies cloning forks and automatically configures the `upstream` remote (e.g. `gh repo clone your-username/project`).
- **GitKraken / SourceTree**: graphical interfaces (GUI) for visualizing complex branch graphs.
- **LazyGit**: a fast terminal UI (TUI) tool to manage Git without leaving the console.

---

## Common Anti-Patterns

- **Confusing fork with clone**: cloning the original repo, making changes, and then discovering you can't push due to missing permissions.
- **Working directly on `main`**: mixes experimental changes with your baseline, complicating sync and rollback.
- **Giant PRs**: bundling fixes, refactors and features into a single review increases rejection risk and merge time.
- **Not reading `CONTRIBUTING.md`**: ignoring naming conventions, tests or requirements causes the PR to fail review.
- **Not syncing your fork**: your `main` falls behind upstream, and you end up working on an outdated base.

---

## GitHub Actions (CI/CD)

**GitHub Actions** is GitHub's built-in automation tool, used to create custom workflows that automatically test, build or deploy code whenever certain events happen (e.g. a push or a pull request).

Key ideas:
- Workflows are defined in YAML files inside `.github/workflows/`.
- They can run tests automatically on every PR, ensuring only code that passes checks reaches `main`.
- They can also automate deployments after a successful merge.

---

## Package Management Note: pnpm

**pnpm** ("performant npm") is a Node.js package manager focused on speed and disk efficiency. Unlike npm or Yarn, which duplicate dependencies across projects, pnpm uses a centralized content-addressable store with hard links, significantly reducing installation time and disk usage.

---

## Current Level

This module reflects a **fundamental/working** level: I understand the difference between Git and GitHub, I can explain the fork/clone/branch/commit/push/PR workflow, I understand why short-lived branches and small PRs matter, and I know the basic steps to contribute to an external repository and keep a fork in sync. I am still building deeper experience with advanced Git operations (rebase, cherry-pick, conflict resolution at scale) and writing custom GitHub Actions workflows from scratch.

## Next Steps

- Practice resolving merge conflicts confidently
- Learn `git rebase` and when to prefer it over merge
- Write a basic custom GitHub Actions workflow (e.g. run tests on push)
- Explore GitHub CLI (`gh`) for a faster day-to-day workflow
