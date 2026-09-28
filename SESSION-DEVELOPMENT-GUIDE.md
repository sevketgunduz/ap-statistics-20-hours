# Developing the next session

How Sessions 5–20 are made, so that each one comes out the same as the last. **STANDARDS.md is the contract** and wins wherever this guide and it disagree. This guide is the working method, plus the facts one session hands to the next.

---

## The short version

```
/build-session 5
```

The command runs the whole sequence below for one session and stops before publishing. After you have looked at the result, say **push**.

| Step | Who | Output |
|---|---|---|
| 1. Scope | the command | the session's CED topics, from the plan, checked against the CED |
| 2. Build the session | the `session-builder` agent | tutor script, workbook, figures, tool if earned, data registered |
| 3. Review the session | the command | the checklist in *Reviewing a built session*, below |
| 4. Write the test | the command | `Session-NN-MC-Test.md`, its figures, its manifest entry |
| 5. Build and verify | the command | a clean `build.py`, links, nav, 400 px |
| 6. Publish | you say "push" | one commit to `main`, which redeploys the site |

The session always comes first and the test second, because the test's distractors, conventions and reteach table are taken from the finished session.

---

## The rules every session follows

These are in STANDARDS.md, and repeated here because they are the ones most often broken.

| Rule | Where | In one line |
|---|---|---|
| CED is the only authority | §0.1 | objective codes quoted verbatim from the PDF; anything with zero CED hits goes in a red extension block |
| Every number is computed | §0.3, §7 | a script produces every table, statistic and mark total before it is written down |
| Nothing deferred for time | §0.6 | the session is as long as the content needs; homework only practises |
| **Theory before examples** | §3, §3.1 | a *Theory — …* section states every concept, with its code, rule, formula and limits, before any scenario, activity or solo case |
| Write first, then reveal | §3 | every workbook `:::yourturn` is followed by a `:::reveal`; anything the student constructs is hidden |
| Distinguishable headings | §4 | no two headings on a page read the same; `build.py` fails with INDISTINCT HEADINGS |
| Headings colour by level | §4 | H1 navy, H2 violet, H3 blue, H4 plum, set in `course.css`; never coloured by hand |
| Colour has meaning | §4 | teal = keep, amber = trap, red = off-syllabus; never decorative |
| Simulations earn their place | §5 | change or process · not showable statically · student drives it |

### What "theory first" looks like in practice

```
## 0–10 min · Homework debrief and diagnostic      ← retrieval of earlier theory only
## 10–30 min · Theory — the least-squares line      ← every concept, stated
### The least-squares regression line (5.3.A)
### Residuals (5.4.A)
### ...
## 30–70 min · Scenario A — ...                     ← applies the theory to data
```

A scenario's `intro` line says *"Recall the residual from the theory section"*, not *"Introduce: a residual is …"*. If a scenario needs a concept the theory section does not state, the theory section is incomplete.

---

## Conventions carried from session to session

A later session and its test must use these exactly as earlier sessions did.

| Convention | Value | Set in |
|---|---|---|
| Quartiles | median of each half; when *n* is odd the median is in **neither** half (TI-84 1-Var Stats) | Session 3 |
| Standard deviation | sample *s*, divisor *n* − 1 | Session 3 |
| Outlier rules | 1.5 × IQR and 2 SD, both from the CED; a value exactly on a fence is **not** an outlier | Session 3 |
| z-scores | z = (*x* − μ) ÷ σ; use *x̄* and *s* when parameters are unknown | Session 3 |
| Correlation | *r* = (1 ÷ (*n* − 1)) Σ z<sub>x</sub> z<sub>y</sub>; reported to 2 dp; found by technology (CED 5.5.A.4) | Session 4 |
| Strength guide | \|*r*\| ≥ ~0.8 strong, ~0.5–0.8 moderate, < ~0.5 weak — a course rule, not the CED's | Session 4 |
| Scatterplot description | direction ("tend to"), unusual features, form, strength, in context | Session 4 |
| Variable names | explanatory / response, never independent / dependent | Session 4 |
| Calculator | TI-84; LinReg(a+bx) with Stat Diagnostics on | Session 4 |
| Regression | ŷ = a + bx with ŷ and x named in context; residual = y − ŷ (positive underpredicts); a and b to 4 significant figures keeping at least 2 dp; predictions and residuals to 1 dp from the equation as written; *r*² read from the calculator | Session 5 |
| Sampling and study design | method names in full (simple random / stratified random / cluster random / systematic random); stratified = some from every group, cluster = everyone from some groups; an SRS makes every sample of size n equally likely; an experiment imposes treatments; random selection → generalisation, random assignment → cause; a confounding variable is linked to both variables | Session 6 |
| Session tests | Session 1's test opens Session 3 (as Session 1's document says); Session 4's builder placed Session 2's at the start of Session 4. **Not yet confirmed** as the general rule | Sessions 3–4 |

### Data

Every data set is registered once in `build/datasets.json`, with the sessions that use it. Read it before designing a scenario; register every new set before quoting a number from it.

**Contexts already used in sessions** (reuse them for continuity; the data carry forward): Lincoln High commute and distance · the hospital survey, St Mary's and Riverside, St Mary's evening shifts · the café (drinks per hour, midday temperatures, fridge log, spring mornings, coffee machine) · the library (Central and Westside branches, 18 branches, members' ages) · Oakfield School · the Session 2 test scores out of 50 · the gym (Session 1) · Session 6's Lincoln High sampling plans, St Mary's text reminders, café loyalty members, hospital-network survey and Oakfield's 900-student roll.

**Contexts already used in tests** (do not reuse these as teaching scenarios, and do not reuse any session context in a test):

| Test | Contexts |
|---|---|
| Session 1 | municipal recycling, school library, café orders, football club, school nurse, university bookshop, voters, gym members |
| Session 2 | gym bookings, two towns' transport, 10-point quiz, phone batteries, family workshop ages, bus delays, basketball heights, ice cream, die rolls |
| Session 3 | animal shelter, weather °C/°F, swimming gala, pizza shops, maths/history exams, athletics, tomato plants |
| Session 4 | used cars, house fires, screen time and sleep, height and arm span, engine size and fuel use, flats and rent, revision hours |
| Session 5 | taxi fares, car braking distances, rainfall and wheat yield, candle burning, school heating and outdoor temperature |
| Session 6 | commuter train carriages, bakery oven experiment, new drivers, breakfast and grades, step-count app, Northbridge water company, radio phone-in, revision app, housing estate |

Add the new session's contexts to both lists as part of step 3.

---

## Reviewing a built session

Before the test is written, check the session against this list. Every item is a problem an earlier session actually had.

- [ ] The *Theory — …* section comes before the first scenario in **both** documents, and covers every concept used later
- [ ] Every learning objective in the orientation table matches the CED PDF word for word
- [ ] Timing tables state the honest length; there is no "over-full", "short of time" or "cut if slow"
- [ ] Homework introduces nothing new, and its marks sum to the stated total
- [ ] Homework, answer key and reference sheet are identical in tutor and workbook
- [ ] Every `:::yourturn` in the workbook is followed by a `:::reveal`
- [ ] No fenced code block sits inside a `>` quote (the builder does not render it)
- [ ] Headings name their content and read as a clean list in the sidebar
- [ ] Off-syllabus terms appear only in red blocks, and any new one is added to STANDARDS.md §8
- [ ] The agent's report lists its verifications, with results, and names what it could not verify

---

## Writing the test

`Session-04-MC-Test.md` is the current template. Copy its structure, not its content.

1. **Size.** 20–22 questions, roughly two per learning objective, so every objective is tested at least twice. Fewer objectives means fewer questions; say so on the page.
2. **Contexts.** New ones only (see the tables above).
3. **Level.** Mostly analysis and synthesis. Tabulate the Bloom level of each question and state the counts.
4. **Distractors.** Each wrong option is a named misconception, preferably one the session itself warns about. The explanation for each question says why the key is right **and** what each wrong option reveals.
5. **Conventions.** Use exactly the session's formulas, notation, rounding and quartile method.
6. **Headings.** *Questions N–M · Context* over the questions, *Answers N–M · Context* over the explanations. Answers are inside `<details>`.
7. **Diagnosis.** A score table, then a table mapping each missed question to two **exact section headings** of the session: the *theory to reread* (a subsection of *Theory — …*) and *where it is applied* (the scenario or activity section). That is the order the session teaches in. Check every heading exists, by script.
8. **Verification.** A script computes every number, recomputes each distractor from the error it represents, and checks that the answer letters are spread roughly evenly across A–E. Figures are rendered to PNG and inspected.
9. **Manifest.** Entry `sNNx`, out `sNN-test.html`, variant `test`, topics `CED … · N questions`, placed after the session's student workbook.

---

## Build, verify, publish

```
python build/build.py
```

It must end with no MISSING SOURCES and no INDISTINCT HEADINGS. Then check:

- nav JSON parses on every page, and every relative link resolves
- at 400 px wide there is no page overflow; wide tables scroll inside their own box
- the browser console shows no errors on the new pages

Publishing is one commit to `main` and a push, which redeploys GitHub Pages. Commit only the session's files: if another session is being built at the same time, leave its files out of the commit.

---

## Known pitfalls

| Pitfall | What to do |
|---|---|
| Code blocks inside `>` quotes render as literal ``` | Put data in a code block outside the quote |
| `figures/` is excluded by `.gitignore` | The committed copies are `site/assets/figures/`, produced by the build; always rebuild before committing |
| The Unit 1 Explorer is an HTML fragment | It is kept in `build/fragments/unit1-explorer.html`; the original Session 1–2 tutor fragments are kept there too, for reference only (the tutor pages now build from markdown) |
| Most of `.claude/` is local | `.claude/agents/` and `.claude/skills/` are committed, so the agent and `/build-session` travel with the repository; local settings and `launch.json` stay out of git |
| The site's own Dark toggle makes figure labels hard to read when the operating system is in light mode | Known and site-wide; do not make it worse; the fix is for `build.py` to inline the page-token figure versions |
| The 2026 formula sheet prints geometric distributions and the slope sampling distribution, but the CED omits both | Treat them as off-syllabus until the register (§8) is rechecked |
| Rounded z-scores can sum to a different *r* than the exact data | Choose data whose rounded products give the same 2 dp answer |

---

## The sessions still to build

From `AP-Statistics-20-Hour-Lesson-Plan.md`. Check each topic range against the CED before building.

| Session | CED topics | Content | Tool proposed in STANDARDS.md §5 |
|---|---|---|---|
| 5 | 5.3–5.5 | least-squares line, residuals and residual plots, slope, intercept and *r*² in context, software output | Least-squares fitter · Influence |
| 6 | 1.10–1.11 | investigative question revisited, sampling methods, why randomisation licenses inference | — |
| 7 | 1.12–1.13 | bias, experiments versus observational studies, control, blocking, blinding, confounding, scope of inference | Sampling bias |
| 8 | 2.1–2.3 | two-way tables: joint, marginal, conditional; simulation | — |
| 9 | 2.4–2.5 | law of large numbers, probability rules, mutually exclusive events | — |
| 10 | 2.6–2.7 | conditional probability, independence, multiplication rule | — |
| 11 | 2.8–2.10 | random variables, expected value and SD, combining, binomial | Binomial explorer |
| 12 | 2.11–2.12 | normal distribution; sampling distributions and the CLT | Central Limit Theorem · Normal area |
| 13 | 3.1–3.3 | estimators, sampling distribution of p̂, one-proportion z-interval | CI coverage |
| 14 | 3.4–3.6 | interpreting intervals and confidence levels, hypotheses, p-values | CI coverage |
| 15 | 3.7–3.8 | one-proportion z-test, Type I/II errors, power | Power explorer |
| 16 | 3.9–3.13 | two proportions: interval and test | — |
| 17 | 3.14–3.15 | chi-square homogeneity and independence (not goodness-of-fit) | — |
| 18 | 4.1–4.3 | sampling distribution of x̄, *t*, one-sample and paired intervals | — |
| 19 | 4.4–4.6 | one-sample and paired *t*-tests, x̄₁ − x̄₂ | — |
| 20 | 4.7–4.10 + synthesis | two-sample *t*; choosing the procedure | Procedure chooser drill |

Block labels for `manifest.json`: Sessions 1–3 *Block A · Describing one variable* · 4–5 *Block B · Describing two variables* · 6–7 *Block C · Collecting data* · 8–12 *Block D · Probability and distributions* · 13–17 *Block E · Inference for proportions* · 18–20 *Block F · Inference for means, and synthesis*.

---

## Retrofits done

Sessions 1–4 were brought up to these rules on 2026-09-29. Each has a *Theory — …* section before its first scenario, and scenario `intro` lines recall it. Sessions 1–2's tutor scripts were converted from their original HTML pages to markdown, checked piece by piece against the originals, which are kept in `build/fragments/`. Every test's reteach table now names both the theory to reread and where it is applied. The Unit 1 Explorer is embedded in Sessions 1 and 2.
