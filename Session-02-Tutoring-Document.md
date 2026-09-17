# Session 2 — Showing and Describing One Variable

**AP Statistics · Twenty-Hour Course · One-to-one tutoring edition**
**CED Topics 1.4, 1.5, 1.6 · Skills 3.A, 4.A, 4.B · 60 minutes**

---

## Where this session sits

Session 1 gave the student the vocabulary and the tables. This session turns tables into **pictures**, and then teaches the language for describing what the picture shows.

The second half is the more important half. Constructing a histogram is a five-minute skill. Describing a distribution in a way that earns marks is a skill students still get wrong in April, because it requires saying four specific things in context and most students say two of them.

### Learning objectives

| Code | Objective | Skill |
|---|---|---|
| 1.4.A | Construct categorical one-variable graphical representations | 3.A |
| 1.4.B | Justify a claim using categorical graphical representations | 4.B |
| 1.4.C | Compare multiple categorical tabular and graphical representations | 4.A |
| 1.5.A | Construct quantitative one-variable graphical representations | 3.A |
| 1.6.A | Describe distributions of quantitative graphical representations | 4.A |
| 1.6.B | Justify a claim using quantitative distributions | 4.B |

### Timing

| Minutes | Segment | Who talks |
|---|---|---|
| 0–8 | Homework debrief and diagnostic | Student |
| 8–18 | **Scenario A** — bar charts, pie charts, and the comparison trap (1.4) | Both |
| 18–32 | **Scenario B** — building three displays (1.5) + Build & Defend | Student |
| 32–46 | Describing the distribution (1.6) — the four components | Both |
| 46–54 | Solo case | Student |
| 54–60 | Teach-it-back, set homework | Student |

---

## 0–8 min · Homework debrief and diagnostic

The student should arrive with Session 1's homework **self-marked**. Do not re-mark it. Ask for the two lists instead:

> *"Which ones did you get wrong, and which ones did you put a question mark on?"*

Spend the time on those only. The question-marked items that turned out right are the most valuable — that is where confidence is missing but knowledge is not.

**The two errors to check for specifically:**

- **B5 answered "parameter".** The denominator test has not landed. Two minutes: *"how many did they actually ask?"*
- **D4 answered "yes, supported".** Plurality versus majority. Two minutes, because it recurs in every unit.

Then three quick retrieval questions before you start teaching:

**Q1.** *"Give me a categorical variable and a quantitative variable, from anything."*
**Q2.** *"If I have a table of counts for six hospitals, what could I draw?"*
**Q3.** *"What does a histogram show that a list of numbers doesn't?"*

Q3 is the one that matters. Listen for anything about **shape** or **pattern**. If the answer is only "it's easier to read", that is the gap this session fills.

---

## 8–18 min · Scenario A — the hospital survey, now in pictures

Deliberate continuity: this is **the same data the student tabulated last session**. Say so. Seeing a familiar table become a graph is the cheapest possible way to make the table–graph relationship obvious.

> The same **300 surveyed patients**, by hospital:
> **St Mary's 84, Riverside 71, Northgate 52, Parkview 45, Eastwood 30, Hillcrest 18.**

### The two displays and what each axis means

**Ask:** *"If you drew a bar chart of this, what would the height of the St Mary's bar be?"*

Listen for either **84** or **0.280** — both are correct, and that is the point. A bar chart can show frequency **or** relative frequency. The shape is identical; only the axis label changes.

**Ask:** *"So what changes if you plot relative frequency instead of frequency?"* → nothing about the picture, only the scale. Make them say it.

### The pie chart formula

A pie chart shows each category's share of the whole, so the slice must be sized by relative frequency, not by count.

> **Slice angle = (f ÷ n) × 360°**
> and equivalently, **slice as a percentage of the area = 100rf**

Have the student compute all six:

| Hospital | *f* | *rf* = f ÷ 300 | Angle = rf × 360° |
|---|---|---|---|
| St Mary's | 84 | 0.280 | 0.280 × 360 = **100.8°** |
| Riverside | 71 | 0.237 | 0.237 × 360 = **85.2°** |
| Northgate | 52 | 0.173 | 0.173 × 360 = **62.4°** |
| Parkview | 45 | 0.150 | 0.150 × 360 = **54.0°** |
| Eastwood | 30 | 0.100 | 0.100 × 360 = **36.0°** |
| Hillcrest | 18 | 0.060 | 0.060 × 360 = **21.6°** |
| **Total** | **300** | **1.000** | **360.0°** |

**The self-check:** the angles must total 360°. Same logic as Σ*rf* = 1 from last session — it is the same check wearing a different hat.

### From table to graph

Show the student all three side by side. **The colour is the link** — St Mary's is the same blue in the table, the bar chart and the pie chart, so the eye carries one hospital across all three. Nothing is added or lost between them; the same six numbers are re-encoded as height, then as area.

> **Table (the counts) → Bar chart (height) → Pie chart (area)**

![Bar chart of surveyed patients by hospital](figures/bar-hospital.svg)

*Bar chart — height encodes the count. Good for **comparing** categories: the eye judges length accurately, so it is obvious St Mary's exceeds Riverside by about 13 patients.*

![Pie chart of surveyed patients by hospital with slice angles](figures/pie-hospital.svg)

*Pie chart — area encodes the share. Good for **part-to-whole**: St Mary's is visibly a bit over a quarter of the circle. Poor for comparing Northgate with Parkview, whose slices are close.*

**Ask:** *"Which of those two would you use to answer 'did more than half our patients come from one hospital?'"* → the pie, because the question is about a share of the whole and half a circle is visible without arithmetic.

**Then:** *"And which to answer 'how many more patients did Northgate see than Parkview?'"* → the bar chart. The slices are too close to judge.

---

### The comparison trap (1.4.C)

This is the part of topic 1.4 that actually gets examined. Give the student last year's figures:

> Last year the network surveyed **200** patients:
> **St Mary's 70, Riverside 40, Northgate 30, Parkview 30, Eastwood 20, Hillcrest 10.**

**Ask:** *"Did St Mary's handle more or fewer of the surveyed patients this year than last?"*

Almost every student says **more** — 84 is bigger than 70. Let them commit.

**Then ask:** *"How many patients were surveyed each year?"*

| Hospital | Last year *f* (n=200) | Last year % | This year *f* (n=300) | This year % |
|---|---|---|---|---|
| St Mary's | 70 | 35.0% | 84 | **28.0%** |
| Riverside | 40 | 20.0% | 71 | 23.7% |
| Northgate | 30 | 15.0% | 52 | 17.3% |
| Parkview | 30 | 15.0% | 45 | 15.0% |
| Eastwood | 20 | 10.0% | 30 | 10.0% |
| Hillcrest | 10 | 5.0% | 18 | 6.0% |
| **Total** | **200** | **100%** | **300** | **100%** |

St Mary's count went **up** (70 → 84) while its share went **down** (35.0% → 28.0%).

> **The rule the student should write down:** when two data sets have different totals, compare **relative frequencies**, never raw counts. A bar chart of counts across two unequal groups is misleading, and saying so is worth marks.

**Ask:** *"Which hospital's share changed most?"* → St Mary's, down 7.0 percentage points. Riverside rose 3.7. Everything else barely moved.

---

## 18–32 min · Scenario B — the commute times, now in pictures

More continuity: Session 1's commute study measured journey time. Here are 25 of those journeys.

> Journey times to school, in minutes, for 25 randomly chosen Lincoln High students:
>
> ```
> 8   9  10  11  12  12  13  14  15  15
> 16  17  18  18  20  21  22  24  25  27
> 30  33  36  42  68
> ```

Already sorted, deliberately — sorting is not the skill being taught today.

### Build & Defend

This replaces the classroom Gallery Walk, where four groups each built one display. One-to-one, **the student builds all three**, and then you interrogate which is best for which question.

Give roughly four minutes for the student to produce, by hand:

**A dotplot** — one dot per value, stacked where values repeat.

**A stem-and-leaf plot** — stems are the tens digit, leaves the units, both ordered smallest to largest:

```
0 | 8 9
1 | 0 1 2 2 3 4 5 5 6 7 8 8
2 | 0 1 2 4 5 7
3 | 0 3 6
4 | 2
5 |
6 | 8
```

> **Do not let them omit the empty `5 |` row.** That blank row *is* the gap. A stemplot that skips unused stems has destroyed the information it exists to show.

![Dotplot of 25 journey times in minutes](figures/dotplot-commute.svg)

*The dotplot — every one of the 25 values is still its own dot. This is the display that makes the outlier and the gap unmissable: 68 sits alone, with nothing between 42 and 68.*

**A histogram**, bins of width 10:

| Interval | Frequency |
|---|---|
| 0 – under 10 | 2 |
| 10 – under 20 | 12 |
| 20 – under 30 | 6 |
| 30 – under 40 | 3 |
| 40 – under 50 | 1 |
| 50 – under 60 | 0 |
| 60 – under 70 | 1 |
| **Total** | **25** |

**The bin-width formula**, when a question tells you how many bins to use:

> **bin width = (maximum − minimum) ÷ number of bins**
> Here: (68 − 8) ÷ 6 = 10

### Then defend

Ask these three, and make the student commit to one display each time:

| Question | Best display | Why |
|---|---|---|
| *"What was the exact longest journey?"* | Stemplot or dotplot | Both keep every individual value; the histogram has thrown them away |
| *"Roughly what does the overall shape look like?"* | Histogram | Bins smooth out noise and make the single peak obvious |
| *"Is there a journey far away from all the others?"* | Dotplot or stemplot | The isolated 68 and the empty gap are visible as a gap |

**The general principle, in the student's own words:** histograms trade individual values for a clearer shape. Dotplots and stemplots keep every value but get unreadable with large *n*.

### Bin width changes the picture (1.5.A.2)

The CED says this explicitly, so it is fair game. Rebuild the same data with bins of width 5:

| Interval | *f* | | Interval | *f* |
|---|---|---|---|---|
| 5 – under 10 | 2 | | 35 – under 40 | 1 |
| 10 – under 15 | 6 | | 40 – under 45 | 1 |
| 15 – under 20 | 6 | | 45 – under 50 | 0 |
| 20 – under 25 | 4 | | 50 – under 65 | 0 |
| 25 – under 30 | 2 | | 65 – under 70 | 1 |
| 30 – under 35 | 2 | | **Total** | **25** |

![Histogram of journey times, bin width 10](figures/hist-width10.svg)

*Bin width 10 — one obvious peak between 10 and 20 minutes; the shape reads as clearly skewed right.*

![Histogram of journey times, bin width 5](figures/hist-width5.svg)

*Bin width 5 — the same 25 journeys. The peak splits into two equal bars of 6 and the distribution looks flatter, almost bimodal.*

**Ask:** *"Same data. Does it look the same?"*

**Both histograms are drawn on the same vertical scale**, so the comparison is honest — the width-5 bars really are shorter, because each bin now catches half as many journeys. **Neither picture is wrong.** The lesson is that a histogram is a choice, and the choice affects the story. That is why the exam asks you to describe *shape* rather than trust one picture.

---

## 32–46 min · Describing the distribution (1.6)

This is the heart of the session.

### The four components

The CED requires a description to cover **shape, center, and variability (spread)**, plus **any unusual features** — outliers, gaps, or clusters — **in context**. Many textbooks compress this to the mnemonic **SOCS** (shape, outliers, center, spread); it is the same four things in a different order.

**Make the student write all four every single time.** The commonest lost mark in Unit 1 is describing shape and centre and stopping.

### The vocabulary, applied to the commute data

**Shape** — *skewed right* (positively skewed) if the right tail toward larger values is longer; *skewed left* (negatively skewed) if the left tail is longer; *approximately symmetric* if the left half roughly mirrors the right.

Also: *unimodal* (one main peak), *bimodal* (two prominent peaks), *approximately uniform* (all frequencies roughly equal, no prominent peak).

> **Ask:** *"Which tail is longer?"* → the right. So: **skewed right, unimodal.**
>
![Skewed right versus skewed left, tails labelled](figures/skew-compare.svg)

*The single most common error in Unit 1. In both pictures the bulk sits opposite the tail. Skew is named for the tail, so the left picture — bulk on the left, tail stretching right — is skewed **right**.*

> **The reliable trick for the direction:** the skew is named for **where the tail points**, not where the bulk sits. Students reverse this constantly. Have them point at the tail with a finger and say the direction out loud.

**Center** — where the bulk of the data sits. The student can use the median, 18 minutes, from a stemplot by counting to the 13th of 25 values. *(Formal calculation of mean and median is topic 1.7 — next session. Today an approximate centre read off the graph is enough.)*

**Variability (spread)** — how far the values reach. Here, from 8 to 68 minutes.

**Unusual features** — *outliers* are values unusually small or large relative to the rest; a *gap* is a region with no observed data; *clusters* are concentrations of values usually separated by gaps.

> Here: **68 minutes is an outlier**, and there is a **gap between 42 and 68** with nothing in it.
>
> Note the honest limit: the formal 1.5 × IQR rule for outliers is topic 1.8, next session. Right now "unusually large relative to the rest" is the CED's own definition and is sufficient.

### The model answer

Have the student write this out in full. Then compare against yours.

> *"The distribution of journey times for these 25 students is **skewed right** and **unimodal**, with one main peak between 10 and 20 minutes. The **centre** is about 18 minutes. Journey times **range from 8 to 68 minutes**. There is an **outlier at 68 minutes**, separated from the rest of the data by a **gap** between 42 and 68 minutes — this student's journey took far longer than anyone else's."*

**Mark it against the checklist with them:**

| Component | Present? | The words |
|---|---|---|
| Shape | ✓ | skewed right, unimodal |
| Center | ✓ | about 18 minutes |
| Variability | ✓ | 8 to 68 minutes |
| Unusual features | ✓ | outlier at 68, gap 42–68 |
| **In context** | ✓ | "journey times", "minutes", "students" |

> **The context requirement is not decoration.** A description that says "skewed right with an outlier" and never mentions journeys, minutes or students will lose the interpretation mark even though every statistical word is correct.

### Justifying a claim (1.6.B)

**Ask:** *"A parent says: a typical journey to this school takes about half an hour. Does this data support that?"*

No. The centre is about 18 minutes, not 30. The claim is probably driven by the long right tail — a few journeys of 30, 33, 36, 42 and 68 minutes — but those are the minority. A supportable version: *"Most journeys take under 20 minutes, though a small number take considerably longer, up to 68 minutes."*

Same template as last session: **state the claim · quote the number · say what it does and does not establish · keep it in context.**

---

## 46–54 min · Solo case

Unaided. Watch, say nothing, note where they hesitate.

> A café recorded the number of drinks sold per hour over 20 opening hours:
>
> ```
> 14  16  17  19  20  21  21  22  23  24
> 24  25  26  27  28  30  31  33  35  52
> ```

1. Construct a stem-and-leaf plot using tens as stems.
2. Construct a frequency table with bins of width 10, starting at 10.
3. Describe the distribution. All four components, in context.
4. The manager claims: *"We usually sell over 30 drinks an hour."* Is that supported? Justify.

**Answers.**

Stemplot:
```
1 | 4 6 7 9
2 | 0 1 1 2 3 4 4 5 6 7 8
3 | 0 1 3 5
4 |
5 | 2
```
Bins: 10–under 20 → 4; 20–under 30 → 11; 30–under 40 → 4; 40–under 50 → 0; 50–under 60 → 1. Total 20.

Description: skewed right, unimodal, main peak in the 20s. Centre about 24 drinks per hour (median of 20 values = mean of 10th and 11th = (24+24)/2 = 24). Ranges from 14 to 52 drinks per hour. Outlier at 52, separated by a gap between 35 and 52.

Claim: not supported. The centre is about 24 drinks per hour, and only 4 of the 20 hours sold more than 30 (31, 33, 35 and 52) — that is 20% of hours, not "usually". A supportable version: *"Sales are usually in the twenties per hour, with one unusually busy hour of 52."*

**Watch for:** describing shape and centre and stopping; calling it "skewed left" because the bulk is on the left; omitting the empty `4 |` stem.

---

## 54–60 min · Teach it back

> *"Describe the café distribution to me out loud, as if I can't see the graph. I'll stop you the moment you miss one of the four."*

Doing it aloud rather than in writing is the point — it exposes whether the four components are a habit or a checklist they consult. Then set the homework.

---
---

# Homework — Session 2

**40 marks · bring to Session 3, self-marked**

## How to do this homework

1. Do every part **with the answer key closed.** Where you are unsure, answer anyway and put a **?** beside it.
2. Then open the key and **mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote.
3. **Bring the marked sheet.** Your wrong answers and your question marks are what Session 3 opens with.

You will need a ruler and a protractor for Part B.

---

## Part A — Vocabulary (6 marks)

Match each term to its meaning.

| | Term | | Meaning |
|---|---|---|---|
| 1 | Skewed right | A | Two prominent peaks |
| 2 | Skewed left | B | A region of the distribution containing no data |
| 3 | Unimodal | C | The tail toward larger values is longer |
| 4 | Bimodal | D | One main peak |
| 5 | Gap | E | All frequencies roughly equal, no prominent peak |
| 6 | Approximately uniform | F | The tail toward smaller values is longer |

## Part B — Categorical displays (10 marks)

A school library recorded which section each of **250 borrowed books** came from last term.

| Section | Frequency |
|---|---|
| Fiction | 100 |
| Non-fiction | 65 |
| Reference | 40 |
| Periodicals | 30 |
| Other | 15 |

**B1.** Add an *rf* column and a *100rf* column. State the formula for each before you use it. (3)

**B2.** Calculate the pie chart slice angle for every section. **State the formula first.** Give each to one decimal place. (4)

**B3.** Show that your angles total 360°. (1)

**B4.** Draw a bar chart of the relative frequencies. Label both axes. (2)

## Part C — Comparing two data sets (6 marks)

The **previous** term the library recorded **200** borrowed books:

| Section | Frequency |
|---|---|
| Fiction | 96 |
| Non-fiction | 44 |
| Reference | 30 |
| Periodicals | 20 |
| Other | 10 |

**C1.** A librarian says: *"Fiction borrowing went up this term — it rose from 96 books to 100."* Calculate the percentage for Fiction in each term, and explain why the librarian's comparison is misleading. (4)

**C2.** State the general rule about comparing two data sets that have different totals. (2)

## Part D — Quantitative displays (10 marks)

Twenty-four students sat a test marked out of 50. Their scores:

```
12  24  29  31  33  35  36  37  38  38  39  40
40  41  41  42  42  43  43  44  45  45  46  47
```

**D1.** Construct a stem-and-leaf plot using tens as stems. Order the leaves. (4)

**D2.** Construct a frequency table using bins of width 10, starting at 10. (3)

**D3.** The test had 24 students and the scores run from 12 to 47. If you wanted exactly 7 bins, what bin width would you use? **State the formula and substitute.** (2)

**D4.** One student looks at your stemplot and says the `1 | 2` row should be deleted because it only has one value. Explain why they are wrong. (1)

## Part E — Describing a distribution (8 marks)

Using the test-score data from Part D:

**E1.** Describe the distribution. Your answer must cover **all four components** and be **in context**. (5)

**E2.** A teacher claims: *"Most of the class scored below 40."* Using your displays, justify whether this claim is supported. (3)

---
---

# Answer key

*For the student to mark their own work, after attempting everything.*

### Part A (6 marks, 1 each)

1–C · 2–F · 3–D · 4–A · 5–B · 6–E

### Part B (10 marks)

**B1.** (3) Formulas: rf = f ÷ n, 100rf = (f ÷ n) × 100, with n = 250.

| Section | *f* | *rf* | *100rf* |
|---|---|---|---|
| Fiction | 100 | 100 ÷ 250 = 0.400 | 40.0% |
| Non-fiction | 65 | 65 ÷ 250 = 0.260 | 26.0% |
| Reference | 40 | 40 ÷ 250 = 0.160 | 16.0% |
| Periodicals | 30 | 30 ÷ 250 = 0.120 | 12.0% |
| Other | 15 | 15 ÷ 250 = 0.060 | 6.0% |
| **Total** | **250** | **1.000** | **100%** |

**B2.** (4) Formula: angle = (f ÷ n) × 360°

| Section | Working | Angle |
|---|---|---|
| Fiction | 0.400 × 360 | **144.0°** |
| Non-fiction | 0.260 × 360 | **93.6°** |
| Reference | 0.160 × 360 | **57.6°** |
| Periodicals | 0.120 × 360 | **43.2°** |
| Other | 0.060 × 360 | **21.6°** |

**B3.** (1) 144.0 + 93.6 + 57.6 + 43.2 + 21.6 = **360.0°** ✓

**B4.** (2) Bar chart with section on one axis and relative frequency on the other, bars of height 0.400, 0.260, 0.160, 0.120, 0.060. **Both axes labelled** — one mark is for the labels. Bars should not touch; this is categorical data, not a histogram.

### Part C (6 marks)

**C1.** (4)
Fiction last term: 96 ÷ 200 = 0.480 = **48.0%** (1)
Fiction this term: 100 ÷ 250 = 0.400 = **40.0%** (1)
The comparison is misleading because the two terms had different totals — 200 books against 250. (1) Fiction's raw count rose by 4, but its **share of all borrowing fell from 48.0% to 40.0%**. Relative to everything else being borrowed, fiction became less popular, not more. (1)

**C2.** (2) When two data sets have different totals, compare **relative frequencies or percentages**, not raw counts. (1) Raw counts confound a change in the variable with a change in the overall total. (1)

### Part D (10 marks)

**D1.** (4)

```
1 | 2
2 | 4 9
3 | 1 3 5 6 7 8 8 9
4 | 0 0 1 1 2 2 3 3 4 5 5 6 7
```

Count check: 1 + 2 + 8 + 13 = 24 ✓

**D2.** (3)

| Interval | Frequency |
|---|---|
| 10 – under 20 | 1 |
| 20 – under 30 | 2 |
| 30 – under 40 | 8 |
| 40 – under 50 | 13 |
| **Total** | **24** |

**D3.** (2) bin width = (maximum − minimum) ÷ number of bins = (47 − 12) ÷ 7 = 35 ÷ 7 = **5**

**D4.** (1) The `1 | 2` row must stay because it shows there is a value at 12 — an unusually low score, well separated from the rest. Deleting or skipping stems destroys the spacing that lets a stemplot show gaps and outliers.

### Part E (8 marks)

**E1.** (5) One mark each for shape, centre, variability, unusual features, and context. Model answer:

> *"The distribution of test scores for these 24 students is **skewed left** and **unimodal**, with one main peak in the 40s. The **centre** is about 40 marks. Scores **range from 12 to 47** out of 50. There is an **outlier at 12**, separated from the rest of the data by a **gap** between 12 and 24 — one student scored far below everyone else."*

Accept "negatively skewed" for skewed left.

> **The most common error here is "skewed right."** The bulk of the data sits on the right, in the 40s, but the *tail* stretches left toward 12. Skew is named for the tail. If you got this wrong, flag it — it costs a mark every time it appears, and it will appear again.

**E2.** (3) The claim is **not** supported. (1) From the frequency table, only 1 + 2 + 8 = **11 of 24 students** scored below 40, which is 11 ÷ 24 = 45.8% — fewer than half. (1) A supportable version: *"Slightly fewer than half the class scored below 40, and the single most common band was 40–49."* (1)

### Marks summary

| Part | Marks |
|---|---|
| A — Vocabulary | 6 |
| B — Categorical displays | 10 |
| C — Comparing data sets | 6 |
| D — Quantitative displays | 10 |
| E — Describing a distribution | 8 |
| **Total** | **40** |

---
---

# Reference sheet — keep this

*Give it to the student at the end. Every term carries an example.*

### Displays for one categorical variable

**Bar chart (bar graph)** — one bar per category; the height or length shows the frequency **or** relative frequency. Bars do not touch.
*Example: six bars, one per hospital, the St Mary's bar reaching 84 (or 0.280 on a relative frequency scale).*

**Pie chart** — one slice per category; each slice's area as a fraction of the whole equals that category's relative frequency. The slices total 1, or 100% of the area.
*Example: the St Mary's slice takes up 28.0% of the circle.*

### Displays for one quantitative variable

All three keep the natural ordering of the values, smallest to largest.

**Dotplot** — one dot per value, placed above its position on the axis; near-identical values stack.
*Example: two dots stacked above 12, because two students had 12-minute journeys.*

**Stem-and-leaf plot** — each value splits into a **stem** (leading digit or digits) and a **leaf** (usually the final digit). Stems and leaves are both ordered smallest to largest.
*Example: the value 18 becomes stem 1, leaf 8. Keep empty stems — a blank row is a gap in the data.*

**Histogram** — values are grouped into ordered intervals (**bins**) along the axis; each bar's height is the frequency or relative frequency in that bin. Bars touch, because the scale is continuous.
*Example: the bin "10 – under 20" has height 12, because 12 journeys fell in that range.*

> **Changing the bin width changes the appearance of a histogram.** Narrow bins show detail and noise; wide bins show shape. Neither is wrong, but the picture is a choice.

### Formulas

| Quantity | Formula | Example |
|---|---|---|
| Bar height | *f* or *rf* | 84, or 0.280 |
| Pie slice angle | **(f ÷ n) × 360°** | 0.280 × 360 = 100.8° |
| Pie slice share of area | **100rf** | 28.0% |
| Histogram bar height | *f* or *rf* in that bin | 12, or 12 ÷ 25 = 0.480 |
| Bin width | **(maximum − minimum) ÷ number of bins** | (68 − 8) ÷ 6 = 10 |

**Self-checks:** Σ*f* = *n* · Σ*rf* = 1 · pie angles total 360° · bin frequencies total *n*

### Describing a distribution

A full description needs **four** things, **in context**. Miss one and you lose the mark.

**Shape**
- *Skewed right (positively skewed)* — the right tail, toward larger values, is longer. *Example: journey times, most under 20 minutes but stretching to 68.*
- *Skewed left (negatively skewed)* — the left tail, toward smaller values, is longer. *Example: test scores, most in the 40s but stretching down to 12.*
- *Approximately symmetric* — the left half roughly mirrors the right.
- *Unimodal* — one main peak. *Bimodal* — two prominent peaks. *Approximately uniform* — frequencies roughly equal, no prominent peak.

> **Skew is named for the tail, not the bulk.** Point at the long tail and say its direction out loud. This single error costs more marks in Unit 1 than anything else.

**Center** — roughly where the bulk sits.
*Example: about 18 minutes.*

**Variability (spread)** — how far the values reach.
*Example: from 8 to 68 minutes.*

**Unusual features**
- *Outlier* — a value unusually small or large relative to the rest. *Example: the 68-minute journey.*
- *Gap* — a region of the distribution with no observed data. *Example: nothing between 42 and 68 minutes.*
- *Cluster* — a concentration of values, usually separated by gaps.

> Many textbooks use the mnemonic **SOCS** — shape, outliers, centre, spread. It is the same four components the CED lists as shape, centre, variability and unusual features.

### In context means

Naming the variable, its units, and the individuals — every time.
*Example: not "skewed right with an outlier", but "journey times for these 25 students are skewed right, with one student's journey of 68 minutes far longer than anyone else's."*

---

*CED references: Topic 1.4 (1.4.A.1–2, 1.4.B.1, 1.4.C.1), Topic 1.5 (1.5.A.1–4), Topic 1.6 (1.6.A.1–6, 1.6.B.1). Course and Exam Description effective Fall 2026.*

*Supporting reading: Barron's pdf 83–96 · Princeton Review 105–124 · 5 Steps to a 5 60–65.*

*Next session: Topics 1.7–1.9 — mean, median, standard deviation, the 1.5 × IQR outlier rule, boxplots, and comparing two distributions. The formal outlier test promised above arrives there.*
