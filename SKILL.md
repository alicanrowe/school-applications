---
name: school-applications
description: Use when applying to grad school, art and design MFAs, or craft and trade schools: the applicant names the programs they're interested in, and Claude researches each program's current deadlines and requirements, keep one tracker, schedule deadline reminders, line up recommendation letters, and tailor the portfolio and essays to each program.
metadata:
  author: Alican Rowe (@alicanrowe)
---

# School applications

Get an applicant from "I want to apply to these places" to every application ready to submit, with no deadline missed. Claude researches, tracks, reminds and drafts. **The applicant submits and pays. Claude never submits an application, pays a fee, or sends a message to a school or a recommender without the applicant's go ahead.**

## Files
- `references/programs.md`: one entry per researched program (what it asks for, when it was last checked, its source pages), in the format at the top of the file. A starting point only; re-verify every cycle.
- `references/tailoring.md`: how to tailor a portfolio and essays to research labs, MFAs and craft schools.
- `references/recommendations.md`: letter logistics, who to ask, timing, and a request note template.
- `data/deadlines.csv`: one row per dated item (program, item, due date, time, time zone, confidence, source).
- `scripts/upcoming.py`: prints what's due, soonest first, with days left and which reminder offsets fall today.

Keep the applicant's own material (portfolio picks, draft essays, recommender names) **outside** this skill folder, in the project's working files, so the skill stays free of private data when it is published.

## Workflow

1. **Programs.** Start from the programs the applicant names (a couple is plenty; more can come later). Confirm the exact program at each school (degree, department, start term). Ask only if it is genuinely ambiguous; otherwise pick the obvious one and say so.
2. **Research, from the school's own pages.** For each program, check `references/programs.md` first (re-verify anything there), then open the official apply page, timeline/FAQ, portfolio rules and the department page. Record: deadline with time and time zone, fee and waivers, every component (statements with limits, portfolio count/format/platform, letters, transcripts official or unofficial, CV, tests, interview or visit), decision date, cost and aid deadlines. Mark each fact **confirmed** (read on the school's page for this cycle) or **inferred** (last cycle's pattern, a search snippet, a third-party page). Search snippets are leads, not sources. If a site blocks automated reads, say so and list it as an open question, or read it in a browser.
3. **Tracker.** One table, soonest deadline first, all times converted to the applicant's time zone, with fee, components, decision date and a status column. Put "this week" tasks above it. Put open questions (anything inferred) below it, each with the contact to ask.
4. **Reminders.** Schedule one recurring weekly check-in (see below) and one-shot reminders 14, 7 and 2 days before each hard deadline, plus a "ask recommenders now" reminder 4 weeks before the first letter deadline. Never schedule more than one recurring task per applicant; update it instead.
5. **Letters.** Count distinct writers needed across all programs, map writers to programs, note how each school collects letters (portal invite, email, mail) and the due date. Draft the request note. Recommenders need 3 to 4 weeks; holidays eat a week.
6. **Portfolio.** Inventory the applicant's work (site, project files, photos). Classify each piece as built-and-photographed, in progress, or render/design only. Then pick per program using `references/tailoring.md`. Flag gaps early (e.g. a craft school wants photos of real work and the applicant mostly has renders).
7. **Essays.** Find the one story that runs through the applicant's work, then outline each school's essay to its own prompt and limit. Some schools forbid AI-generated content (check each school's policy): give outlines, questions and line edits, not finished prose, unless the school allows it and the applicant asks.
8. **Transcripts and documents.** Note which schools take unofficial copies and which need an official one sent by the registrar; transcript ordering often needs the old student login, so start it early.
9. **Before each deadline.** Run the pre-submit check: every component present, word counts within limits, portfolio within count and file limits, groups/advisors named where required, letters confirmed received, fee ready. Hand the applicant a one-screen checklist; they submit.

## Weekly check-in (the recurring scheduled task)
Each run:
1. Run `python3 scripts/upcoming.py <deadlines.csv>`; report anything due within 21 days, and anything inferred whose date is within 45 days.
2. Re-open the official page for every program with a deadline in the next 60 days and compare with the tracker. Update the tracker and `data/deadlines.csv` if anything changed, and say what changed.
3. Check letter status and open questions; nudge only the applicant, never the recommender.
4. Post a short digest: next three deadlines with days left, what to do this week, anything changed. Stay quiet-ish: if nothing is due within 21 days and nothing changed, a two-line note is enough.
5. After decisions arrive, drop the program from reminders; when every program is decided, end the recurring task.

## Rules
- Times in the applicant's time zone, with the school's own zone noted when it differs.
- Every date in the tracker carries confirmed or inferred.
- Don't invent requirements. A missing fact is an open question with a contact.
- When this skill learns something (a page moved, a rule changed, a better way to tailor), update `references/` and the date at the top of `programs.md`.

## Excuses that don't count
Each of these is a shortcut that ends in a broken result. If you catch yourself thinking the left column, do the right column.

| The excuse | What to do instead |
|---|---|
| "The deadline is the same as last cycle" | Check the program's current page and record the date with the link. |
| "The recommender knows the deadline" | Put each letter's due date in the tracker and schedule a reminder. |
| "I'll submit it for them" | Applications, fees and sign-ins are the applicant's; prepare everything, they submit. |
| "While I'm in here I'll also tidy/refactor this other bit" | Change only what the task needs. Smallest diff that works; no new options, helpers or files nobody asked for. Note other ideas for later instead. |

## Keep this skill improving
When a step here goes wrong or the owner corrects something, write the lesson into this skill (dated) in the same session, add a check to a script if one could have caught it, and publish it with the skills publish script. No private data.
