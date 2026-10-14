# DATASCI 350 - Data Science Computing

## Quiz 02 (make-up) - Building a website with Quarto and GitHub Pages

### Scenario

A sports newsletter wants a small public website about the history of the men's FIFA World Cup. This repository holds `worldcups.csv`, with one row for each tournament from 1930 to 2022. Your job is to build a three-page Quarto website from it and publish the site on GitHub Pages.

This quiz is worth 6% of the final grade and covers lectures 10 and 11. It is open-book and open-notes. It is an individual assessment. You have 75 minutes.

You must be able to explain every command and every line you submit. The instructor may ask you to walk through part of your work, during the quiz or right after it.

### Data

`worldcups.csv` has 22 rows and eight columns:

| Column | Meaning |
|--------|---------|
| `year` | Tournament year |
| `host` | Host country |
| `host_continent` | Continent of the host country |
| `winner` | Champion |
| `teams` | Number of teams |
| `matches` | Number of matches played |
| `goals` | Total goals scored |
| `attendance_k` | Total attendance, in thousands |

The file `create-dataset.py` shows how the dataset was built.

The quiz grades your Quarto and Git work, not your Python. Any working plot earns the marks. Where a task needs code you have not seen, the task gives it to you.

Each page runs its own Python, so start every page with this chunk:

```python
import pandas as pd
import matplotlib.pyplot as plt

cups = pd.read_csv("worldcups.csv")
```

The path is relative, so it works while your pages sit next to `worldcups.csv`. If you get a `FileNotFoundError`, check where your pages are (task 1). Never use an absolute path like `/Users/you/...` (lecture 10).

### Rules

- Work from the command line and your editor. Files created or uploaded through the GitHub website lose points, because the grader reads your commit history.
- Record every command you run in a file named `commands.txt` in the repository's root directory.
- Type every Git command yourself, in any terminal (VS Code's terminal is fine). Do not use the buttons in VS Code's Source Control panel: they leave no command to record.
- When you finish, post the link to your published website and the link to your fork on Canvas, in the "Assignments" tab under Quiz 02.
- State your AI use on the home page (task 5). The syllabus AI policy applies.

### If `git push` asks for credentials

Your machine should already be logged in to GitHub. If a push fails with an authentication error, do not create tokens: run `gh auth login`, choose GitHub.com, then HTTPS, and log in with the browser. After that, `git push` works normally.

### Setup

1. Fork this repository to your GitHub account.
2. Clone your fork to your machine from the command line.
3. Change directory into the cloned repository.

### Tasks

Each task is worth 1 point.

1. Create a Quarto website project inside the cloned repository. From the repository folder, run `quarto create project website .` (the `.` means "this folder"). Press Enter at the title question. At the next question, press the down arrow to choose `(don't open)`, then Enter. Do not use VS Code's `Quarto: Create Project` here: in a folder that already has files, it puts the site in a new subfolder. The folder now has `_quarto.yml`, `index.qmd`, `about.qmd`, `styles.css` and a hidden `.gitignore`.

2. Add these two lines to the end of `.gitignore`:

    ```text
    /_site/
    __pycache__/
    ```

    Then stage and commit `.gitignore` with the message "Add gitignore", before you render anything. If `ls -a` shows no `.gitignore`, you are not inside your cloned repository: go back to setup step 3 and redo task 1.

3. Edit `_quarto.yml`:
    - Set the website title to `World Cup Numbers`.
    - Delete `about.qmd` and remove it from the navigation bar.
    - Add `goals.qmd` and `crowds.qmd` (tasks 6 and 7 create them) to the navigation bar, with exactly these link texts: `Matches and Goals`, `Crowds and Champions`.

4. In `_quarto.yml`, replace the theme setting with one single theme from [Quarto's theme list](https://quarto.org/docs/output-formats/html-themes.html). Then add `freeze: auto` under a new `execute:` key.

5. Edit `index.qmd`. The home page needs a title, two or three sentences about the dataset, links to the other two pages, and a final line saying which AI tools you used during the quiz (or that you used none).

6. Create `goals.qmd` with a title, a short introduction and a scatter plot of `matches` against `goals`. Show the code (`echo: true`). Give the plot a caption with `fig-cap` and a label that starts with `fig-`. In the introduction, refer to the plot with `@fig-...`, so it renders as a numbered link.

7. Create `crowds.qmd` with a title and a line plot of `attendance_k` over `year`. Below the plot, write one sentence that reports the number of tournaments in the data and the number Brazil won, using inline code, so the sentence updates if the data changes. Select Brazil's titles with this line:

    ```python
    brazil = cups[cups["winner"] == "Brazil"]
    ```

    `len(cups)` counts the rows of `cups`, and `len(brazil)` counts the rows of `brazil`.

8. Render the website. Check that a `_freeze/` folder appeared, then stage and commit everything with the message "Add site pages and freeze".

9. Publish the site with `quarto publish gh-pages`, as in lecture 11. Open the published link and check that all three pages load and the navigation bar works. If something is broken, fix it and publish again. If `quarto publish` fails on your machine, use the manual route: set `output-dir: docs` in `_quarto.yml`, render, commit, push, and enable GitHub Pages from the `docs` folder in your fork's settings. The first build can take a couple of minutes. Write in `commands.txt` which route you used.

10. Finish `commands.txt` with every command you ran. Write the final `git add`, `git commit` and `git push` lines into it before you run them. Stage and commit it with the message "Add command log", then push to your fork (`quarto publish` does not push your `main` branch). Submit the two links on Canvas. Done! 😊

### Bonus tasks

Try these only after you finish the main tasks. Record every step in `commands.txt`, then publish, commit and push again.

1. Edit `styles.css` to change the link colour and one font setting, and make sure `_quarto.yml` points at it.
2. Give the site a pair of light and dark themes in `_quarto.yml`, so a toggle appears in the navigation bar.

Best of luck!
