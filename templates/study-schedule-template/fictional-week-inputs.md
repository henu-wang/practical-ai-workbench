# Fictional week: input, capacity and coverage

Original manually prepared example, not model output or a real course/student record. All course names, deadlines, workload estimates and availability below are supplied fictional inputs. Times are local with no timezone conversion.

## Date and constraints

Week: Monday 2026-10-12 to Sunday 2026-10-18.
No study after 20:00. No assumed commute study. Friday has no usable study slot. Buffer can be deliberately reassigned only after updating the plan; it is not counted as completed work.

## Fixed commitments supplied by the fictional learner

- Monday–Friday: work 09:00–17:00; commute 08:15–09:00 and 17:00–17:45; dinner/personal tasks 17:45–19:00.
- Tuesday and Thursday: class 20:00–21:00; no additional study after class.
- Wednesday: family commitment 19:45–21:00.
- Friday: family commitment 19:00–21:00.
- Saturday: volunteering and travel 12:00–17:00.
- Sunday: personal commitment 11:30–15:00.
- The learner offers only the usable slots below. Unlisted time is not available merely because no obligation has been described.

## Confirmed usable slots

| Date | Day | Start | End | Minutes |
| --- | --- | --- | --- | --- |
| 2026-10-12 | Monday | 19:00 | 20:00 | 60 |
| 2026-10-13 | Tuesday | 19:00 | 20:00 | 60 |
| 2026-10-14 | Wednesday | 19:00 | 19:45 | 45 |
| 2026-10-15 | Thursday | 19:00 | 20:00 | 60 |
| 2026-10-17 | Saturday | 10:00 | 12:00 | 120 |
| 2026-10-18 | Sunday | 10:00 | 11:30 | 90 |

Usable total: 435 minutes. Reserve Saturday 15 and Sunday 30 = 45 buffer minutes. Remaining study capacity: 390 minutes.

## Supplied course/unit estimates

| Unit | Deadline | Estimated minutes | Planned study | Unplaced minutes | Coverage note |
| --- | --- | --- | --- | --- | --- |
| Information skills: evaluating supplied notes | 2026-10-19 17:00 | 120 | 90 | 30 | First pass, recall and practice present; planned review missing |
| Academic writing: paragraph draft | 2026-10-19 17:00 | 120 | 90 | 30 | First pass, drafting and review present; extra revision practice missing |
| Introductory statistics: practice set | 2026-10-18 17:00 | 120 | 120 | 0 | First pass, practice and review present; time allocation does not prove completion |
| Computing basics: small exercise | 2026-10-19 17:00 | 90 | 90 | 0 | First pass, practice and review present; time allocation does not prove completion |
| Optional statistics reflection | Unknown | Unknown | 0 | Unknown | Not placed; confirm date and estimate before budgeting |

Known estimated work 450 vs 390 study capacity leaves 60 minutes unplaced. Unknown reflection is additional unknown work, not included in that 60. Every dated unit has at least one block before its deadline, but two known estimates are not fully covered.

## Complete planned output

The CSV assigns every offered minute exactly once: 390 study +45 buffer. All blocks are within offered slots and outside fixed commitments. No blocks after 20:00; no Friday block. Monday 19:45–20:00 is the only quiz handoff in this example.

Monday: information skills 45 first pass, 15 recall.
Tuesday: academic writing 30 first pass, 30 practice.
Wednesday: statistics 30 first pass, 15 review.
Thursday: computing 30 first pass, 30 practice.
Saturday: statistics 45 practice, writing 30 review, computing 30 review, buffer 15.
Sunday: information skills 30 practice, statistics 30 review, buffer 30.

## Decision rather than a hidden overload

Keep the default buffer and report 60 minutes of uncovered work. The learner must choose priorities, negotiate a requirement where possible, or supply genuine extra availability; this example makes none of those decisions automatically. Rearranging the same minutes cannot eliminate the deficit.

If the learner deliberately assigns all 45 buffer minutes to the uncovered tasks, 15 known minutes still remain and the week has no slippage margin. Unknown reflection remains unresolved. If Thursday's 60-minute block is missed, the planned buffer can cover only 45; at least 15 more minutes of that missed work must be displaced or left uncovered, in addition to the original gap. Recheck deadlines when moving work.

## Scope of checks

Local arithmetic/file checks verify these supplied dates and allocations. They do not validate an official syllabus, determine realistic workload for a real learner, run a planning model, create calendar events or establish learning outcomes.
