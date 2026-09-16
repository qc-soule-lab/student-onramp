*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p00e — which tab am I in?  (coding · step 0 · skills: two_prompts)

## Prompt (show to student)
You have two JupyterLab terminal tabs open: the one where you typed `claude` and are reading
this, and a plain shell. You want to see what files are in the `data/` folder, so you plan to
type `ls data`.

1. Which of the two tabs do you type it in?
2. Before you type, how do you tell that tab apart from the other one — what do you look at?
3. What happens if you type `ls data` into the *other* tab instead?

## Answer key
1. The **plain shell tab**. It is the only one of the two that runs commands in your account.
2. Look at the line where you type. The shell's prompt ends in **`$`** (something like
   `jovyan@jupyter-...:~$`) and it answers only with program output, or with nothing. The Claude
   tab's input line starts with **`>`** inside the Claude Code frame, and it answers in sentences.
   If unsure, type `pwd` in the tab: the shell prints a path; Claude replies in words.
3. Typed at the `>` prompt, `ls data` is a message to Claude. Nothing ran in your shell and your
   directory did not change; Claude may describe the command or offer to run it, but you have not
   run it. The reverse mistake, a sentence typed at the `$` prompt, gets `command not found`,
   because the shell tried to run the first word as a program.

Key idea: two tabs, two prompts. Commands go to the `$` tab and come back as output. Questions,
predictions, and reports of what happened go to the `>` tab and come back as words. Claude is a
program running in a tab, the same way vi is: `claude` enters it and `/exit` leaves it. In this
course the student runs every command in the shell tab; Claude does not type in the terminal.

## Hint ladder
- **R1:** Look at the two tabs. What does the line where you type start or end with in each one? Which of the two has ever printed a file listing for you?
- **R2:** One tab's prompt ends in a dollar sign and speaks only in program output; the other's starts with an angle bracket and speaks in sentences. Only one of them can run a command in your account. Which is it, and what becomes of a command sent to the other?
- **R3 (reveal):** the answer key above.

## Scoring (→ rubric §3)
- `correct`: routes `ls data` to the shell tab, names a reliable tell (the prompt symbol, or the kind of reply each tab gives), and predicts that the command does not run if sent to Claude.
- `partial`: routes it to the shell tab but cannot say how to tell the tabs apart, or is unsure what happens on a mis-route.
- `wrong`: would type it at the Claude prompt, or cannot say which tab runs commands.
**Anchor (Constitution III):** if you named the `$` / `>` tell or said "that goes in the shell tab" before the student did, that was the reveal — a restated answer scores `wrong`, depth 2.
