# School applications skill

A Claude skill for applying to graduate programs, art and design MFAs, and craft schools. Tell Claude the couple of programs you're interested in; it researches each one's current deadlines and requirements from the school's own pages, keeps one tracker in your time zone, schedules reminders before every deadline, plans recommendation letters, and tailors your portfolio and essays to what each program judges. You submit and pay; Claude never does.

## What's in it
- **`SKILL.md`**: the workflow, the weekly check-in, and the rules.
- **`references/programs.md`**: the format for each researched program; Claude fills in one entry per program you name.
- **`references/tailoring.md`**: how research labs, MFAs and craft schools read a portfolio and an essay differently.
- **`references/recommendations.md`**: letter planning and a request note template.
- **`data/deadlines.csv`** and **`scripts/upcoming.py`**: deadlines soonest first with days left, reminder and verify flags (Python 3.9+, no dependencies). The CSV ships with one example row; replace it with your programs.

```
python3 scripts/upcoming.py data/deadlines.csv --tz America/New_York
```
