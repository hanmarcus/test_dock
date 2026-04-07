# Introduction to programming with Python (PWP)

## Preface

This repo is a Python 3 tutorial for newcomers, also covering some basic computer programming concepts. For the more tech-savvy, it is also a preconfigured development environment, which may help with setup friction and allows everyone to focus more on writing programs. It is more than a simple Python container, there are many other useful pre-built functionalities, as you'll later see.

**Who is this resource for?**
* Complete beginners to computer programming, this will get you up and running with a basic knowledge of how programs work using Python as a medium.
* Advanced beginners (I see you), this will hopefully take you a step forward, as it also covers some less familiar concepts in later chapters.

**Note:** 
The focus is on Python fundamentals, covering up to **file** and **exception handling**. For now, the repo has not included object-oriented programming (OOP) concepts. 

**Contributions:**
This is a open-source effort, feel free to submit your ideas on any of the following: course structure, best/better coding practices, additional material (OOP, metaprogramming, ...). The objective is to create something that approximates an introductory yet comprehensive Python bible.

---

## Learning Objectives

By the end of this repository, the following capabilities should be achieved:

* 

---

## DevContainer setup

### Prerequisites

* Docker installed
* VS Code installed
* Dev Containers extension installed

### Steps

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-name>
```

2. Open in VS Code
3. Reopen in container:

> Command Palette → "Dev Containers: Reopen in Container"

4. Wait for environment build

---

## Repository Structure

```
.
├── .devcontainer/        # DevContainer configuration
├── labs/                # Exercises per chapter
├── tests/               # Automated test cases
├── workspace/           # Student working directory
├── README.md
```

---

## Workflow

1. Navigate to a lab
2. Copy lab files into workspace

```bash
cp -r labs/lab1 workspace/
```

3. Implement solution inside `workspace/`
4. Run validation

```bash
check lab1/filename.py
```

---
