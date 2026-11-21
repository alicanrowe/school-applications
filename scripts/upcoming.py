#!/usr/bin/env python3
"""List application deadlines soonest first, with days left, in the applicant's time zone.

usage: upcoming.py deadlines.csv [--tz America/New_York] [--today YYYY-MM-DD] [--within DAYS]
Flags rows that hit a reminder offset today (28, 14, 7, 2, 1, 0 days left) and inferred dates within 45 days.
"""
import argparse, csv, datetime as dt
from zoneinfo import ZoneInfo

OFFSETS = {28, 14, 7, 2, 1, 0}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv"); p.add_argument("--tz", default="America/New_York")
    p.add_argument("--today"); p.add_argument("--within", type=int, default=400)
    a = p.parse_args()
    me = ZoneInfo(a.tz)
    now = dt.datetime.now(me)
    today = dt.date.fromisoformat(a.today) if a.today else now.date()
    rows = []
    for r in csv.DictReader(open(a.csv)):
        d = dt.date.fromisoformat(r["due_date"])
        if r.get("due_time"):  # a timed deadline: convert to the applicant's zone
            t = dt.time.fromisoformat(r["due_time"])
            local = dt.datetime.combine(d, t, ZoneInfo(r.get("tz") or a.tz)).astimezone(me)
        else:  # a date only: keep the school's calendar date
            local = dt.datetime.combine(d, dt.time(0, 0), me)
        left = (local.date() - today).days
        if 0 <= left <= a.within:
            rows.append((local, left, r))
    rows.sort(key=lambda x: x[0])
    for local, left, r in rows:
        flags = []
        if left in OFFSETS and r.get("hard") == "yes": flags.append("REMIND")
        if "inferred" in r.get("confidence", "") and left <= 45: flags.append("VERIFY")
        when = local.strftime("%a %d %b %Y") + ("" if not r.get("due_time") else local.strftime(", %I:%M %p %Z"))
        print(f"{left:4d}d  {when:32s}  {r['program']}: {r['item']}  [{r['confidence']}] {' '.join(flags)}")

if __name__ == "__main__":
    main()
