---
name: build-session
description: Build the next numbered session of the AP Statistics twenty-hour course end to end — scope from the plan and CED, tutor script and workbook via the session-builder agent, review, then the multiple-choice test, build and verification. Stops before publishing. Use when the user asks to build, develop or prepare a session (5 through 20), e.g. "/build-session 5".
argument-hint: <session number, e.g. 5>
disable-model-invocation: true
---

# Build session $ARGUMENTS

You are building **Session $ARGUMENTS** of the AP Statistics twenty-hour course in `C:\10.AP_Statistics`. If no session number was given, work out the next one: the lowest number with no `Session-NN-Tutoring-Document.md`. Say which one you chose.

## 0. Read first

1. `STANDARDS.md`, all of it. It is the contract and wins every disagreement.
2. `SESSION-DEVELOPMENT-GUIDE.md`, all of it. It gives the conventions, the contexts already used, the review checklist, the test method and the pitfalls.
3. The session's entry in `AP-Statistics-20-Hour-Lesson-Plan.md`.
4. The previous session's tutor script, for its homework (the debrief this session opens with) and its section headings.

## 1. Scope

Take the CED topic range from the plan. Extract those topics from `ap-statistics-course-and-exam-description.pdf`, using `get_toc()` to find the pages. Confirm the plan's topic split matches the CED's. If it doesn't, follow the CED and tell the user. Note the block label and the tool proposed in STANDARDS.md §5 for this session.

## 2. Build the session

Launch the `session-builder` agent in the background, with a self-contained prompt. It must include:

- the session number, CED topics, block label and manifest entries (`sNNt` and `sNNs`, `kind: md`, placed in the right block group, creating the group if it is new)
- the four rules most often broken, stated explicitly:
  1. **theory before examples** (§3.1)
  2. **nothing deferred for time** (§0.6)
  3. **distinguishable headings** (§4)
  4. **write first, then reveal**
- the continuity it must use: the previous session's homework debrief, conventions from the guide's table, and data from `build/datasets.json`
- the contexts it must avoid (the guide's test-context table)
- the proposed tool, to be built only if it passes the three tests in §5
- no test, no commit and no push, and no edits to earlier sessions or STANDARDS.md (proposals go in its report)
- a final report containing:
  - files created or changed
  - the CED objectives, verbatim
  - off-syllabus findings
  - the two traps and why they were chosen
  - the tool decision
  - the tutor-script headings in order, exactly as written
  - timing totals
  - homework structure and marks
  - every convention the test must match
  - every verification and its result
  - anything it could not verify

Tell the user the agent is running. Do not duplicate its work while it runs.

## 3. Review the session

When the agent reports, work through the guide's *Reviewing a built session* checklist yourself, by script where you can:

- the theory section precedes the first scenario in both documents
- the objectives match the CED verbatim
- no deferral phrases appear ("over-full", "short of time", "cut", "in this hour")
- homework marks sum to the stated total
- homework, answer key and reference sheet are identical in both documents
- every `:::yourturn` is followed by a `:::reveal`
- no code block sits inside a quote
- the build is clean

Fix small faults directly. Send anything substantial back to the same agent, continuing its context, with the specific fault. Then add the session's contexts to the guide's context lists.

## 4. Write the test

Follow the guide's *Writing the test* method, with `Session-04-MC-Test.md` as the structural template:

- Write a Python script in the scratchpad first. It computes every number, recomputes each distractor from its error, checks the answer letters are balanced, and renders every figure to PNG for you to inspect.
- Then write `Session-NN-MC-Test.md`, and its figures as `figures/tNN-*.svg`.
- Check by script that every section named in the reteach table exists as a heading in the tutor script.
- Add the `sNNx` manifest entry after the student workbook.

## 5. Build and verify

Run `python build/build.py`. It must report no MISSING SOURCES and no INDISTINCT HEADINGS. Then:

- check that nav JSON parses and every relative link resolves on all pages
- serve `site/` with the `site` launch configuration and check the new pages at 400 px: no page overflow and no console errors
- stop the server

## 6. Report and stop

Tell the user, briefly:

- what the session teaches and its two traps
- the test's size, its contexts and the traps it checks
- every verification and its result
- anything unverified
- decisions only the user can make

Update the course-progress memory. **Do not commit or push** until the user says so. When they do, commit only this session's files.
