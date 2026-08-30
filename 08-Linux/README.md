# 08 - Linux Fundamentals

## Module Goal

This module documents my fundamental understanding of Linux: what it is used for, how it's organized, and the basic terminal skills needed to navigate the filesystem, manage packages, process text and handle permissions. It reflects a beginner-to-working level, focused on core concepts rather than deep system administration expertise.

---

## What is Linux used for?

Linux is extremely versatile due to its modular design. Common use cases include:

- **Servers and Cloud**: most web servers and cloud services (AWS, Azure, Google Cloud) run on Linux.
- **Supercomputers**: nearly all of the world's fastest supercomputers run Linux.
- **Mobile devices**: Android is built on top of the Linux kernel.
- **Embedded systems**: routers, appliances, and infotainment systems.
- **Desktop**: development environments, research, and privacy-focused setups.

### Pros and Cons

| Advantages | Disadvantages |
|---|---|
| Open source, auditable code | Learning curve — the terminal requires practice |
| More resistant to common malware | Limited support for some commercial software (Adobe/Office) |
| High stability, long uptimes without reboots | Some hardware drivers may not work well |
| Full system customization | Fragmentation across many distributions |

---

## Kernel vs Distribution

- The **Linux kernel** is the core engine of the operating system.
- A **distribution (distro)** is that kernel packaged with an interface and a set of tools.

Examples:
- **Debian**: one of the most stable "mother" distributions, base for many others.
- **Debian-based**: Ubuntu, Kali Linux.
- **Red Hat-based**: RHEL, Fedora, CentOS, Rocky Linux.
- **Independent**: Arch Linux, openSUSE.

---

## What are dependencies?

Programs often need external pieces (libraries, codecs) to work correctly. **Package managers** like `apt` handle this automatically: they check for missing pieces and download them.

---

## Related Job Roles

- **System Administrator (SysAdmin)**: maintains servers and networks.
- **DevOps Engineer**: automates cloud deployments.
- **Cybersecurity Engineer**: pentesting and vulnerability analysis.
- **Cloud Data Engineer**: manages large-scale data infrastructure.
- **Backend/Embedded Developer**: builds software for native Linux environments.

---

## Core Concepts: Terminal, Filesystem and Permissions

The shell acts as an interpreter: it receives a command, executes the matching binary, and returns output (`STDOUT`), errors (`STDERR`), or applies persistent changes to disk. Working in Linux is fundamentally about reading system state, transforming data, and applying changes with the right privileges.

Five critical areas of control:
1. **Location** — knowing and changing your working directory.
2. **Filesystem** — creating, editing, reading and organizing files.
3. **Package management** — installing and removing software.
4. **Text processing** — filtering and transforming data streams.
5. **Permissions** — controlling access to files and directories.

---

## Navigation and File Management

```bash
pwd                 # Show current directory
ls -la              # List visible and hidden files
cd Desktop          # Move into a directory
touch note.txt      # Create an empty file
nano note.txt       # Edit a file
cat note.txt        # Read file contents
mkdir -p backup     # Create a destination directory
cp note.txt backup  # Copy a file
mv note.txt backup  # Move a file
rm -f backup/note.txt  # Delete a file
```

---

## Search and Error Handling

```bash
find / -name "note.txt" 2>/dev/null   # Search and silence errors
find / -name "*.txt" 2>/dev/null      # Search by extension
```

`2>/dev/null` redirects error output (`STDERR`) so it doesn't clutter the useful output (`STDOUT`) — essential for clean search results.

---

## Package Management

```bash
sudo apt update              # Refresh repositories
sudo apt install -y <pkg>    # Install from repository
sudo apt remove -y <pkg>     # Uninstall a package
sudo apt autoremove -y       # Clean up orphaned dependencies
sudo dpkg -i package.deb     # Install a local .deb file
sudo apt install -f -y       # Fix broken dependencies
```

- `apt` manages official repositories and resolves dependencies automatically.
- `dpkg` installs local `.deb` files manually, which can leave "unmet dependencies" if not followed up with `apt install -f`.

---

## Text Processing

```bash
grep -n "ERROR" app.log            # Search for a pattern, show line numbers
cat app.log | grep -v "healthcheck"  # Exclude noise
cat /etc/passwd | tr ':' ' '        # Replace delimiters
cat /etc/passwd | awk '{print $1}'  # Extract the first column
cat /etc/passwd | cut -c 1-10       # Trim characters
cat /etc/passwd | sed 's/user/admin/g'  # Substitute patterns
```

Tools like `grep`, `awk`, `cut`, `tr` and `sed` form an ecosystem for filtering and transforming text streams — extremely useful for analyzing logs without extra software.

---

## Permissions Management

```bash
ls -l file.txt        # Inspect permissions
chmod u-r file.txt     # Remove read permission for the owner
chmod u+r file.txt     # Restore read permission for the owner
chmod 640 secret.txt   # rw- r-- --- policy
chmod 755 script.sh    # Executable for everyone
```

Permission bits apply to three groups: **owner**, **group**, and **others**, each with **read (r)**, **write (w)**, and **execute (x)** permissions. Note: permissions behave differently on directories than on files — execute permission on a directory is what allows you to enter/access it.

---

## Common Anti-Patterns

- **Operating blindly**: running destructive commands without checking the current path with `pwd` first.
- **Wildcard abuse**: using `rm` with wildcards in production without validating the context first.
- **Ignoring dependencies**: installing with `dpkg` without following up can leave the system in an "unmet dependencies" state.
- **Confusing outputs**: not distinguishing useful output from errors makes diagnosis harder; `2>/dev/null` helps keep reports clean.
- **Excessive privileges**: using `chmod 777` as a "quick fix" is a critical security risk, not a real solution.
- **Misunderstanding permissions on directories**: not knowing how permissions affect directories differently from files can block legitimate access.

---

## Useful Extra Commands

```bash
cd ..            # Move up one directory level
clear            # Clear the terminal (or Ctrl+L)
ls -l            # Long-format listing with details
ls -a            # List all files, including hidden ones
echo "text"      # Print text or variables
```

In `nano`, use `Ctrl+O` to save and `Ctrl+X` to exit.

```bash
rm -r folder         # Recursive delete (required for folders)
ls note*             # Wildcard search for files starting with "note"
rm *.txt             # Delete all files with .txt extension
sudo apt install synaptic   # Install Synaptic (graphical package manager)
sudo apt install gdebi      # Install GDebi (.deb installer)
su username                 # Switch to another user's session
grep -v "text"              # Invert match (exclude matches)
grep -v -E "pattern"        # Invert match using extended regex
```

---

## Current Level

This module reflects a **fundamental** level: I understand what Linux is used for, the difference between the kernel and a distribution, and I can perform basic terminal operations — navigating the filesystem, managing files, installing/removing packages, filtering text, and adjusting permissions. I do not yet have deep system administration experience, advanced scripting skills, or hands-on production server management.

## Next Steps

- Practice writing basic Bash scripts to automate repetitive tasks
- Get comfortable with process management (`ps`, `top`, `kill`)
- Learn about users and groups administration (`useradd`, `usermod`, `/etc/passwd`)
- Explore basic networking commands (`ping`, `curl`, `netstat`/`ss`)
