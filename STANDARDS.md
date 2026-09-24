# Course production standard

**AP Statistics · twenty-hour course · one-to-one tuition, delivered live on a shared screen and revisited afterwards.**

This is the contract every session must satisfy. Agree it once; then sessions 3–20 are production rather than design.

---

## 0. The non-negotiables

1. **The CED effective Fall 2026 is the only authority.** Every learning objective, definition and piece of required content is verified against it before it is written. The three prep books are secondary sources for practice and page references only.
2. **Nothing off-syllabus is taught as if it were examinable.** Content absent from the CED may appear, but only inside an explicitly marked extension block. The running list is in §8.
3. **Every number is computed, never asserted.** Each table, statistic, angle, bin count and mark total is produced and checked by a script before it reaches a page. See §7.
4. **Two documents per session, from one set of scenarios.** Tutor script and student workbook share the same data, the same order and the same worked examples.
5. **A simulation must earn its place.** See §5.
6. **Every required concept is taught in the session, never deferred to homework to save time.** Assume the tutor and student have as long as the content needs. If a session's CED topics need more than the plan's 60 minutes, the session gets longer; its timing table states the honest length, and nothing is cut, compressed or moved out. Homework practises and extends what the session taught; it never carries the first teaching of anything the CED requires.

---

## 1. File and build layout

```
10.AP_Statistics/
  STANDARDS.md                 this file
  Session-NN-Tutoring-Document.md      authoring source (markdown + directives)
  Session-NN-Student-Workbook.md       authoring source
  figures/*.svg                generated diagrams, two variants per figure
  build/
    manifest.json              page order, titles, nav — the single source of truth
    build.py                   markdown + directives -> site/
    assets/course.css          the only stylesheet
    assets/course.js           the only script (sidebar, nav, theme, keys)
    tools/*.html               simulation sources
  site/                        GENERATED — never edit by hand
```

**Build:** `python build/build.py`. Output is relative-path only, so it works from `file://` and on any static host (GitHub Pages, Netlify, Cloudflare Pages) with no configuration.

**Naming:** `sNN-tutor.html`, `sNN-student.html`, `tools/<tool-id>.html`. Zero-padded, lower case, hyphens.

---

## 2. Page shell — every page gets this, free

Supplied by `course.css` + `course.js`; authors write only the body.

| Feature | Behaviour |
|---|---|
| **Contents sidebar** | Left. This page's H2/H3 headings, then the whole course map. Scroll-spy highlights the current section. |
| **Resizable** | Drag the right edge, 190–560 px. Persists in `localStorage`. Keyboard: focus the grip, ← →. |
| **Collapsible** | "Contents" button or `c`. Persists. Auto-overlay below 640 px with a scrim. |
| **Prev / Next** | Top bar buttons and a large pager at the foot. Order comes from `manifest.json`. Keyboard ← →. |
| **Tutor ↔ Student** | Segmented switch in the top bar on any page with a `session` number. |
| **Theme** | Light/dark toggle, `d`. Persists. Respects the OS default when unset. |
| **Expand all reveals** | `e` — opens or closes every `<details>` on the page at once. Useful when projecting. |
| **Print** | Chrome, sidebar and simulation frames drop out; reveals print open. |

Authors must not re-implement any of these, and must not add a second stylesheet.

---

## 3. Session anatomy — fixed order

### Tutor script

1. **Orientation** — where the session sits, learning objectives table (code · objective · skill), timing table with who talks.
2. **Homework debrief** (sessions 2+) — the two lists, plus the two named errors most likely from the previous sheet.
3. **Diagnostic** — 3–4 questions with a branch table: *what you hear → what it means → where to start.*
4. **Scenario A** — worked via `:::script` ask/listen/if-say lines. Terms introduced as they arise, never front-loaded.
5. **Activity** — the one-to-one conversion of the CED's Sample Instructional Activity for that topic.
6. **Scenario B** — second worked context, carrying a different trap from A.
7. **Solo case** — student works unaided while the tutor stays silent; answers given, plus "watch for".
8. **Teach it back** — student explains aloud; what a good answer contains.
9. **Homework + answer key** with mark allocations and teacher notes on likely wrong answers.
10. **Reference sheet** — every term with an example.

### Student workbook

Same seven parts, same scenarios, same order, plus a mapping table to the tutor's clock sections. Differences:

- **Write-first rule** stated at the top, and honoured: every `:::yourturn` is followed by a `:::reveal`, never by the answer in plain text.
- **Anything the student must construct is hidden.** A finished graph visible on the page destroys the exercise.
- Diagnostic becomes **self-scoring**: a table saying what each possible answer means.
- Timing is **longer than the tutor's** — about a quarter longer for the same content, because working alone with a pen is slower, and promising the tutor's time makes students skip the writing. Neither document is capped at 60 minutes (§0.6).
- Homework and reference sheet are **identical to the tutor copy**. One version of the marking, one version of the revision page.

---

## 4. Component library — the authoring directives

Only these. No inline `<style>`, no ad-hoc markup.

```
:::note teal|amber|red   Label
  ...
:::

:::script
  ask    | Ask        | "What proportion of all 1,842 take the bus?"
  listen | Listen for | "We don't know."
  ifsay  | If 0.358   | "How many of the 1,842 did we actually ask?"
  intro  | Introduce  | Population, N = 1,842.
:::

:::yourturn
  Write down: who is this study actually about?
:::

:::reveal   Reveal — the dotplot
  ...
:::

:::formula
  slice angle = (f ÷ n) × 360°
:::

:::checks
  Σf = n
  Σrf = 1
:::

:::sim  unit1-explorer | Sample & Estimate | 760
  Why it is here and what to do with it.
:::
```

Plus standard markdown: headings, tables, blockquotes, lists, `- [ ]` checklists, fenced code for raw data, and `![alt](figures/name.svg)` followed by an italic caption line.

**Tone rules.** Colour carries meaning: **teal** = the idea to keep, **amber** = a trap or a caution, **red** = off-syllabus or a hard error. Never decorative.

**Heading rules.** Every section and subsection heading on a page must be distinguishable from every other heading on that page, because the contents sidebar lists them all and students navigate and revise from it.

- **No two headings may read the same.** They are compared ignoring formatting, case, a leading time range ("10–55 min ·") and bracketed codes ("(1.7.C)"). So *Changing units* and *Changing units (1.7.C)* clash, and so do a section and its own subsection with the same name.
- **Parallel parts of a page say which part they belong to.** A test's question groups are *Questions 1–4 · The gym*, and the matching answer groups are *Answers 1–4 · The gym*. A reference-sheet entry that covers a topic taught earlier on the page gets its own wording, such as *Changing units: the rules (1.7.C)*.
- **A heading names what is under it.** "Part 3", "Working through it" and "More practice" say nothing on their own; add the content: *Part 3 — The commute times, summarised*.

`build.py` enforces the first rule and fails with **INDISTINCT HEADINGS** naming each clash. The other two are for the author to judge.

---

## 5. When a simulation earns its place

Build one only if **all three** hold:

1. The idea is about **change, variation or a process**, not a fact.
2. A static figure genuinely cannot show it — if a picture with a caption works, draw the picture.
3. The student **drives** it. Watching an animation is not interaction.

Each simulation is a standalone page in `tools/`, embedded in the session with `:::sim` and also linkable full-screen for projection.

**Rules for every tool:** opens in a realistic working state, never an empty shell · all marks use `--data` / `--s1…--s6` tokens · works keyboard-only · no library unless it carries real weight · every generator and statistic unit-tested in Node before publishing (§7).

### Inventory — proposed, needs your approval

| Session | Tool | Why it cannot be a picture |
|---|---|---|
| 1 | **Sample & Estimate** ✅ built | A statistic scattering around a fixed parameter is a *process* |
| 2 | **Bin Width** ✅ built | The point is that the picture changes |
| 2 | **Name That Shape** ✅ built | Drill, needs feedback per attempt |
| 3 | **Boxplot & 1.5 × IQR builder** | Drag a point past the fence and watch it become an outlier |
| 3 | **Mean vs median** | Drag one value; watch the mean chase it and the median refuse |
| 4 | **Guess the correlation** | *r* intuition is only built by repeated guessing |
| 5 | **Least-squares fitter** | Drag a line, watch residuals and Σ(residual²) respond |
| 5 | **Influence** | Move one point; watch the line swing |
| 7 | **Sampling bias** | Compare random vs convenience sampling over many draws |
| 11 | **Binomial explorer** | Sliders on *n* and *p* |
| 12 | **Central Limit Theorem** | **The single most valuable tool in the course** |
| 12 | **Normal area** | Shade and read a probability |
| 13–14 | **Confidence-interval coverage** | Draw 100 intervals, count how many capture *p*. Nothing else makes "95% confident" mean what it means |
| 15 | **Power explorer** | Four sliders, one picture |
| 20 | **Procedure chooser drill** | Scenario in, procedure out, with feedback |

Fifteen tools. I would build the six marked as highest value first: **CLT**, **CI coverage**, **guess the correlation**, **boxplot/IQR**, **least-squares fitter**, **power**.

---

## 6. Data and continuity

- **Scenarios carry across sessions.** The Lincoln High commute study and the hospital survey are introduced in Session 1 and reused in Session 2 as tables, then graphs. A student meeting familiar data can spend attention on the new idea.
- **Register a data set once**, in `build/datasets.json` (to be added), so every document and every tool reads the same numbers.
- **Each scenario carries one trap**, and no two scenarios in a session carry the same one.
- Contexts must be plausible and neutral: schools, hospitals, libraries, cafés, gyms, transport. No contexts that could distress or that require cultural knowledge.

---

## 7. Verification — what "checked" means

Before any page is published:

1. **Arithmetic** — every table recomputed in Python; Σf = n, Σrf = 1, Σ100rf = 100%, pie angles = 360°, final cf = n, final crf = 1, mark totals match the stated total.
2. **CED fidelity** — every objective code quoted verbatim from the CED PDF; any term absent from the CED flagged and marked as extension.
3. **Simulation logic** — generators and statistics extracted from the built file and unit-tested in Node; empirical results compared against theory where theory exists.
4. **Figures** — rendered and visually inspected for collisions, overflow and dead space.
5. **Build** — `build.py` runs clean (no MISSING SOURCES, no INDISTINCT HEADINGS), nav JSON parses on every page, every relative asset path resolves.
6. **Page** — renders at 400 px wide; both themes; keyboard-only navigation works.

A session is not finished until all six pass.

---

## 8. The removed-topics register

Absent from the CED effective Fall 2026, still taught by the prep books. Never present these as examinable.

| Topic | Barron's | Princeton | 5 Steps |
|---|---|---|---|
| Inference for slopes | Unit 9 entire | within Ch. 7 | Ch. 13 entire |
| Chi-square goodness-of-fit | pdf 433–437 | within Ch. 7 | 279–284 |
| Geometric distributions | pdf 296–298 | Ch. 6 | 179–180 |
| Transformations to achieve linearity | pdf 192–194 | Ch. 4 | 106–110 |
| Influential points / leverage as formal terms | pdf 186–191 | Ch. 4 | 105 |
| The Investigative Task (FRQ 6) | pdf 512–535 | 77–84 | 5S20 Ch. 14 |
| Cumulative frequency plots (ogives) | ~12 pages | — | in passing |

Add a row whenever a new one is found; never remove one without re-checking the CED.

---

## 9. Publishing

Static output, relative paths, no build step needed at the host. Suitable for GitHub Pages, Netlify or Cloudflare Pages free tiers.

**Before going public:** confirm that reproducing CED learning-objective text and prep-book page references at this volume is acceptable for a public site. Page *references* are certainly fine; extended *quotation* of CED essential-knowledge wording on an open site is worth checking. The safe form — paraphrase the requirement, cite the code — is already what most of the documents do.

---

## 10. Definition of done, per session

- [ ] Both markdown sources written to §3 anatomy
- [ ] All arithmetic script-verified (§7.1)
- [ ] CED codes verified against the PDF (§7.2)
- [ ] Figures generated, both variants, visually checked
- [ ] Simulation built and unit-tested, or a written reason none was needed
- [ ] `manifest.json` updated; `build.py` clean
- [ ] Homework marks total correctly; answer key complete with teacher notes
- [ ] Reference sheet: every term has an example
- [ ] Removed-topics register updated if anything new surfaced
