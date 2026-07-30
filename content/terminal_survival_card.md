*AI-generated draft (Claude, Anthropic) — for review.*

# Terminal survival card

Keep this open — about a dozen commands carry you through the whole course.

| Need | Command |
|---|---|
| Where am I? | `pwd` |
| What's here? | `ls` · `ls -lh` (with sizes) |
| Go somewhere | `cd <dir>` · `cd ..` (up) · `cd ~` (home) · `cd -` (previous) |
| Finish a name for me | start typing, press **Tab** |
| Two names share a prefix? | press **Tab** twice to list them, then type one more letter |
| Where am I really? | `pwd` — the absolute truth about your location |
| Run that again | press **↑** (up arrow) |
| Peek at a file | `head file` · `head -n 5 file` · `cat file` (whole file — small ones only) |
| Make / remove | `mkdir d` · `touch f` · `rm f` · `rmdir d` |
| Edit in vi | `vi file` → `i` (insert) → `Esc` → `:wq` (save+quit) · `:q!` (quit, no save) · `:q` (quit) |
| `No such file or directory` | you're in the wrong folder — `pwd`/`ls`, then `cd` there |

Rule of thumb: if you're about to type a long path, **Tab** it (double-**Tab** if it stalls —
that means more than one match); if you're about to retype a command, **↑** it. A path that starts
with `~` or `/` works from **anywhere**; a bare name (`data`, `../content`) is read from **where you
stand** — `pwd` tells you where that is.

## Handy extras (Part 2 — practiced, not required)

| Need | Command |
|---|---|
| Page a big file | `less file` → **Space**/**b** scroll, **`q`** to quit |
| Count lines | `wc -l file` |
| Search inside a file | `grep -i word file` · `-n` line numbers · `-c` count |
| Combine commands (pipe) | `cmd1 \| cmd2` — e.g. `ls data \| wc -l` |
| Save output to a file | `cmd > file` (overwrite) · `cmd >> file` (append) |
| Many files at once | `*` = any chars · `?` = one — e.g. `ls data/*.nc` |
| Copy · move/rename | `cp a b` · `mv a b` (move **or** rename) |
| Forgot a flag? | `cmd --help` · `man cmd` (**`q`** to quit) |

