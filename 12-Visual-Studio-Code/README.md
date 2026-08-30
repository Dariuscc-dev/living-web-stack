# Visual Studio Code Fundamentals

> A concise reference covering the core concepts, tools, and workflow of Visual Studio Code (VS Code) for real development projects.

## What is VS Code?

Visual Studio Code is a lightweight, extensible code editor developed by Microsoft. It brings together file editing, an integrated terminal, Git integration, debugging tools, and extensions in a single environment.

VS Code itself does not run your code. It relies on external tools such as language runtimes (Python, Node.js), Git, and extensions to complete the development workflow.

## VS Code vs an IDE

| Aspect | VS Code | Full IDE |
|---|---|---|
| Core | Lightweight, extension-based | Complete out of the box |
| Customization | Very high | More opinionated |
| Resource usage | Generally lower | Often higher |
| Best for | Web, scripting, data, automation | Native/enterprise projects |

## Interface Overview

| Area | Purpose |
|---|---|
| Activity Bar | Switch between Explorer, Search, Git, Debug, Extensions |
| Side Bar | Shows content for the active section (e.g. file tree) |
| Editor Group | Main area where files are opened and edited |
| Panel | Terminal, Output, Problems, Debug Console |
| Status Bar | File info, Git branch, language mode, errors |
| Command Palette | `Ctrl+Shift+P` — search and run any VS Code command |

## Core Concepts

- **File**: a unit of code, config, or data (`app.py`, `index.html`, `data.csv`)
- **Folder**: groups related files
- **Project**: an organized folder with code, config, and dependencies
- **Workspace**: the root folder(s) opened in VS Code; opening the root (not a loose file) lets VS Code detect virtual environments, settings, and dependencies correctly

## Extensions

Extensions add language support, formatting, linting, database access, and more.

| Extension | Purpose |
|---|---|
| Python | Run, debug, and analyze Python |
| Pylance | Advanced Python autocompletion and analysis |
| Prettier | Code formatting for JS/HTML/CSS/JSON |
| ESLint | JavaScript/TypeScript linting |
| GitLens | Extended Git history and blame info |
| Live Share | Real-time collaboration |

Install only what you need — extensions consume resources and can conflict with each other.

## Language Server

A Language Server analyzes code in the background to provide autocompletion, error detection, go-to-definition, and safe renaming — all before running the program.

## Runtime vs Editor

| Layer | Role | Example |
|---|---|---|
| VS Code | Editor and orchestrator | — |
| Extension | Language integration | Python extension |
| Runtime | Actually executes code | `python`, `node` |

Installing a language extension does not install the runtime itself.

## Integrated Terminal

Open with `` Ctrl+` ``. Common commands:

```bash
pwd                     # current directory
ls / dir                # list files
git status              # repo status
python --version        # check Python
node --version           # check Node.js
python app.py           # run a script
```

## Python Virtual Environments

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\Activate.ps1     # Windows PowerShell

python -m pip install -r requirements.txt
python -m pip freeze > requirements.txt
```

Virtual environments isolate dependencies per project, avoiding "works on my machine" issues.

## Debugging

Instead of relying on `print()`, use the built-in debugger:

| Shortcut | Action |
|---|---|
| `F5` | Start/continue debugging |
| `Shift+F5` | Stop debugging |
| `F9` | Toggle breakpoint |
| `F10` | Step over |
| `F11` | Step into |
| `Shift+F11` | Step out |

A **breakpoint** pauses execution on a specific line so you can inspect variables and the call stack.

## Project Configuration (`.vscode/`)

| File | Purpose |
|---|---|
| `settings.json` | Editor behavior for this project |
| `launch.json` | Run/debug configurations |
| `tasks.json` | Automated tasks (build, test, etc.) |
| `extensions.json` | Recommended extensions for the team |

## Git & GitHub Basics

| Term | Meaning |
|---|---|
| Repository | Git-tracked folder |
| Commit | Saved snapshot of changes |
| Branch | Alternate line of work |
| Push / Pull | Upload / download changes |
| Clone | Copy a remote repo locally |
| Pull Request | Proposal to review and merge changes |
| `.gitignore` | Files Git should not track |

```bash
git status
git add .
git commit -m "feat: add CSV processing script"
git push
```

## Secrets & Security

Never hardcode credentials. Use a `.env` file and add it to `.gitignore`:

```env
API_KEY=your_key_here
```

```gitignore
.env
.venv/
__pycache__/
```

## Common Anti-Patterns

| Anti-pattern | Better practice |
|---|---|
| Opening a loose file | Open the project's root folder |
| Using global Python | Use a `.venv` |
| No `requirements.txt` | Track dependencies |
| Installing every extension | Install only what's needed |
| Secrets in code | Use `.env` + `.gitignore` |
| Debugging with `print()` only | Use breakpoints |

## Essential Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+Shift+P` | Command Palette |
| `Ctrl+P` | Quick open file |
| `Ctrl+,` | Settings |
| `Ctrl+/` | Toggle comment |
| `Shift+Alt+F` | Format document |
| `F12` | Go to definition |
| `F2` | Rename symbol |
| `Ctrl+F` / `Ctrl+H` | Find / Replace |
| `Ctrl+Shift+F` | Find in all files |
| `Ctrl+D` | Select next match |
| `Ctrl+\`` | Open terminal |
| `Ctrl+B` | Toggle sidebar |

## Quick Checklist

- [ ] Root folder opened as workspace
- [ ] `.gitignore` present
- [ ] No secrets in code
- [ ] Python uses `.venv`
- [ ] Dependencies tracked in `requirements.txt`
- [ ] README explains setup and usage
- [ ] Changes reviewed with `git status` before commit

## Resources

- [VS Code Docs](https://code.visualstudio.com/docs)
- [Keyboard Shortcuts](https://code.visualstudio.com/docs/reference/default-keybindings)
- [Python in VS Code](https://code.visualstudio.com/docs/languages/python)
- [Git in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)
- [Debugging in VS Code](https://code.visualstudio.com/docs/debugtest/debugging)
