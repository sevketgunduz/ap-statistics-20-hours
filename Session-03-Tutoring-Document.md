# Session 3 — Summarising and Comparing Distributions

**AP Statistics · Twenty-Hour Course · One-to-one tutoring edition**
**CED Topics 1.7, 1.8, 1.9 · Skills 3.A, 3.B, 4.A, 4.B, 4.C · about 110 minutes, plus the 40-minute Session 1 test**

---

## Where this session sits

Session 2 taught the student to *look* at a distribution and describe it in words. This session puts numbers on those words: a centre, a spread, a position, and an arithmetic test for "unusual". It then asks the student to use those numbers to **compare** two groups, which is where Unit 1 marks are most often lost on the free-response section.

Two promises from earlier sessions are kept here. Session 2 named the 68-minute journey an outlier by eye and said the formal test would come in Session 3; it comes in Scenario A, with the same 25 journeys. Session 1's hospital survey recorded each patient's waiting time to see a doctor and never used it; Scenario B does.

### Learning objectives

Verbatim from the course description.

| Code | Objective | Skill |
|---|---|---|
| 1.7.A | Calculate measures of center and position for quantitative data. | 3.B |
| 1.7.B | Calculate measures of variability for quantitative data. | 3.B |
| 1.7.C | Calculate different units of measurement for summary statistics. | 3.B |
| 1.7.D | Calculate outliers for quantitative data. | 3.B |
| 1.7.E | Compare multiple quantitative one-variable summary statistics. | 4.A |
| 1.7.F | Justify the selection of a summary statistic for describing quantitative data. | 4.B |
| 1.8.A | Construct quantitative one-variable graphical representations of summary statistics. | 3.A |
| 1.8.B | Describe quantitative one-variable graphical representations of summary statistics based on the relationship of the mean and the median. | 4.A |
| 1.9.A | Compare multiple quantitative one-variable graphical representations. | 4.A |
| 1.9.B | Compare multiple quantitative one-variable graphical representations of summary statistics. | 4.A |
| 1.9.C | Justify a claim using multiple quantitative one-variable graphical representations. | 4.B |
| 1.9.D | Calculate z-scores with population parameters. | 3.B |
| 1.9.E | Compare z-scores as measures of relative position for distributions. | 4.C |

Skills: **3.A** construct representations · **3.B** calculate summary statistics and relative positions · **4.A** describe and compare representations and summary statistics · **4.B** justify a claim · **4.C** describe distributions and compare relative positions.

### One quartile convention, used everywhere

:::note teal The convention for this course
**Q1 is the median of the lower half and Q3 the median of the upper half. When n is odd, the overall median is left out of both halves.** This is what a TI-84's 1-Var Stats does, and it is what the workbook, the homework, the answer key and the Boxplot Builder all use.
:::

The course description (1.7.A.5) defines Q1 as "the median value of the lower half of the ordered data set from the minimum value to the position of the median", which does not settle whether the median belongs to the halves when *n* is odd. Some books include it. For the 25 journey times, including it gives Q1 = 13 and Q3 = 25 instead of 12.5 and 26. The outlier verdicts do not change, but the numbers do, so pick one method and hold it. If the student's school uses the other method, say so and let them keep theirs, provided they use it consistently.

### Timing

**The Session 1 test comes first.** As the Session 1 document says, give its 40-minute multiple-choice test at the start of this session, before the homework debrief. The clock below starts when the test is finished.

| Minutes | Segment | Who talks |
|---|---|---|
| 0–10 | Homework debrief and diagnostic | Student |
| 10–55 | **Scenario A**: the commute times summarised: centre, position, spread and the standard deviation by hand, both outlier rules, the boxplot, resistance, changing units (1.7, 1.8) | Both |
| 55–67 | **Activity**: Match Mine (1.9) | Student |
| 67–97 | **Scenario B**: comparing waiting times at two hospitals, z-scores, then a second comparison from a summary table: two library branches (1.7.E–F, 1.8.B, 1.9) | Both |
| 97–105 | Solo case: the café | Student |
| 105–110 | Teach it back, set homework | Student |
| **Total** | **110 minutes of teaching, after the 40-minute Session 1 test** | |

The course description allots six class periods to topics 1.7–1.9. Everything they require is taught in the session; the homework practises it.

---

## 0–10 min · Homework debrief and diagnostic

The student arrives with the Session 2 homework self-marked. Ask for the two lists: *"Which did you get wrong, and which did you put a question mark on?"* Spend the time on those only.

**The two errors to check for specifically:**

- **E1 answered "skewed right".** The test scores sit mostly in the 40s with a tail down to 12, so they are skewed **left**. A student who said right has named the skew after the bulk. Spend two minutes here, because this session gives them a second way to check: for the same scores the mean (37.96) is below the median (40), and in a left-skewed distribution it usually is. They will meet that in homework B5.
- **C1 compared raw counts.** Fiction went from 96 books to 100, but its share fell from 48.0% to 40.0% because the totals were 200 and 250. If the student accepted the librarian's claim, name the general error: *a raw number means nothing until you know what it is measured against.* It comes back today in a new form, when z-scores compare a 62-minute wait with a 41-minute one.

Then the diagnostic. Four quick questions, answers out loud.

**Q1.** *"What is the median of 9, 1, 7, 4?"*

**Q2.** *"Your homework test scores were skewed left. Without calculating anything, would you expect the mean to be above or below the median?"*

**Q3.** *"Two classes both averaged 70 on the same test. What else would you want to know before saying they did equally well?"*

**Q4.** *"In one sentence, what does a standard deviation tell you?"*

| What you hear | What it means | Where to start |
|---|---|---|
| Q1: "5.5" | Sorts first and averages the middle pair | Move straight on |
| Q1: "4" | Averaged 1 and 7, the middle pair **of the unsorted list** | Two seconds: "put them in order first". Watch for it again in Scenario A |
| Q1: "you can't, there's no middle" | Doesn't know the even-*n* rule | Teach it now: the mean of the two middle values |
| Q2: "below" | Has the pull of the tail, or has guessed | Ask "why?" and accept anything about the low scores dragging the mean |
| Q2: "above" | Either the skew direction or the pull is reversed | Check which: ask where the tail is. If they say "right", E1 has not landed |
| Q3: anything about spread, range or consistency | Has the idea of variability | Scenario A gives it a number |
| Q3: "nothing, they're the same" | Centre is the only summary they know | Make Q3 the opening question of Scenario A's spread section |
| Q4: "how spread out the data is" | Correct but vague | Push for "a typical distance from the mean" |
| Q4: blank | Has never met it | Expected. Teach it from the commute data |

---

## 10–55 min · Scenario A — the commute times, summarised

The same 25 journeys from Session 2. Say so; the student has already drawn three pictures of this data, so all of their attention can go on the numbers.

Journey times to school, in minutes, for 25 randomly chosen Lincoln High students:

```
8   9  10  11  12  12  13  14  15  15
16  17  18  18  20  21  22  24  25  27
30  33  36  42  68
```

**The trap this scenario carries: the mean is not "the typical value".** Last session a parent claimed a typical journey takes about half an hour. The student is about to calculate a mean of 21.44 minutes, and it will feel like the answer to "what is typical?" In a right-skewed distribution with an outlier it is not. The median is.

### Centre: two numbers, one question

:::script
ask | Ask | "Work out the mean and the median. Calculator for the mean is fine."
listen | Listen for | Mean = 536 ÷ 25 = 21.44. Median = the 13th value = 18.
ifsay | If "the median is 20" | "Which position is the middle of 25?" (13th, not the value halfway between 8 and 68, or the 12.5th.)
intro | Introduce | Mean *x̄* = Σ *x*ᵢ ÷ *n*. Median = middle of the ordered data; with even *n*, the mean of the two middle values (1.7.A.2–3).
ask | Ask | "The parent from last session said a typical journey is about half an hour. Which of your two numbers should answer him, and why do they differ?"
listen | Listen for | The median, 18. The mean is higher because a few long journeys, especially 68, pull it up.
intro | Introduce | In a right-skewed distribution the mean is usually larger than the median; skewed left, usually smaller; roughly symmetric, close together (1.8.B.1).
:::

Link it to the homework: for the test scores, skewed left, the mean was *below* the median. Same rule, pointing the other way.

### Position: the quartiles, and the convention

:::script
ask | Ask | "The median cuts the 25 journeys into two halves. Where would you cut each half?"
listen | Listen for | At the middle of each half.
intro | Introduce | Q1 and Q3, the medians of the lower and upper halves (1.7.A.5). State the convention: with odd *n*, the median belongs to neither half.
ask | Ask | "So how many values are in each half, and what are Q1 and Q3?"
listen | Listen for | 12 in each. Q1 = (12 + 13) ÷ 2 = 12.5. Q3 = (25 + 27) ÷ 2 = 26.
ifsay | If Q1 = 13 | They included the median in the lower half (13 values, middle is the 7th = 13). "That's a real method, but not ours. Use the one we agreed, every time."
:::

![The 25 journey times split into halves, median excluded, with Q1 and Q3](figures/s03-quartiles-commute.svg)

*The convention in one picture. The 13th value, 18, is the median and is left out; each half then has 12 values, so each quartile is the mean of two values.*

**Five-number summary: 8, 12.5, 18, 26, 68.** Write it on the shared screen; the rest of the scenario uses it.

**Percentile, quickly (1.7.A.6).** *"What percentile is a 30-minute journey?"* 21 of the 25 journeys are 30 minutes or less, and 21 ÷ 25 = 84%, so 30 minutes is the **84th percentile**. Then: *"About what percentile is Q1?"* About the 25th. Here 6 of 25 values, 24%, are at or below 12.5. The course description says "approximately 25%", and this is why.

### Spread: three measures

| Measure | Formula | Commute times |
|---|---|---|
| Range | max − min | 68 − 8 = **60 minutes** |
| Interquartile range | Q3 − Q1 | 26 − 12.5 = **13.5 minutes** |
| Standard deviation | *s* = √[Σ(*x*ᵢ − *x̄*)² ÷ (*n* − 1)] | **13.07 minutes** (calculator, below) |

Range and IQR need only subtraction. The standard deviation is the one to slow down on, and the course says it "can be found with and without using technology" (1.7.B.4), so the student does both: by hand on five values, then by calculator on all 25.

### The standard deviation, by hand (1.7.B)

**Worked example first.** Take five of the 25 journeys: **10, 14, 18, 22, 36** minutes. Write the formula on the screen, then fill the table with the student, one column at a time.

:::formula
s = √[ Σ(xᵢ − x̄)² ÷ (n − 1) ]
:::

| *x* | *x* − *x̄* | (*x* − *x̄*)² |
|---|---|---|
| 10 | −10 | 100 |
| 14 | −6 | 36 |
| 18 | −2 | 4 |
| 22 | 2 | 4 |
| 36 | 16 | 256 |
| **Total** | **0** | **400** |

1. Mean: *x̄* = 100 ÷ 5 = **20** minutes.
2. Deviations from the mean. **They always total 0.** That checks the arithmetic, and it is why the deviations are squared: positive and negative deviations would cancel.
3. Square each deviation and add: **400**.
4. Divide by *n* − 1 = 4: *s*² = 400 ÷ 4 = **100**, the sample variance.
5. Take the square root: *s* = √100 = **10 minutes**.

:::script
ask | Ask | "Which journey contributes most to that 400, and why?"
listen | Listen for | The 36: its deviation of 16 squares to 256, more than the other four together. Squaring makes far-away values count heavily.
intro | Introduce | That is why the standard deviation is nonresistant: one far value dominates the sum of squares. It comes back in the resistance demonstration.
:::

**Then the student's turn, unaided.** Five more of the journeys: **8, 12, 15, 20, 30**.

:::checks
x̄ = 85 ÷ 5 = 17
deviations −9, −5, −2, 3, 13 (total 0)
squares 81, 25, 4, 9, 169 (total 288)
s² = 288 ÷ 4 = 72
s = √72 = 8.49 minutes
:::

| If they get | They did | Say |
|---|---|---|
| 7.59 | divided by *n* = 5 (288 ÷ 5 = 57.6) | "The sample formula divides by *n* − 1. Check it on the formula sheet." |
| 72 | stopped at the variance | "That is *s*². What are its units?" (Minutes squared: take the root.) |
| 0 | squared the total of the deviations | "The deviations always total 0. Square each one first." |

**Then all 25 by calculator.** Nobody squares 25 deviations in an exam. Put the data in a list and run 1-Var Stats: *s* = 13.07 minutes. The calculator reports *Sx* (the sample standard deviation, dividing by *n* − 1) and *σx* (dividing by *n*); the course uses *s*, which is *Sx*.

:::script
ask | Ask | "The calculator says s = 13.07. Put that into a sentence about journeys."
listen | Listen for | A typical journey is about 13 minutes away from the mean of 21.44.
ifsay | If "the journeys are 13 minutes apart" | "Apart from what?" The SD measures distance from the **mean**, not between neighbours.
intro | Introduce | *s* is "a typical deviation of the data values from their mean"; *s*² is the sample variance (1.7.B.4). Both formulas are on the exam formula sheet.
:::

### The outlier test, as promised (1.7.D)

This is the moment Session 2 promised. Make it feel like one: *"Last time you said 68 was an outlier because it looked far away. Now we find out whether the rule agrees."*

:::formula
lower fence = Q1 − 1.5 × IQR     upper fence = Q3 + 1.5 × IQR
:::

:::script
ask | Ask | "Work out 1.5 × IQR, then both fences."
listen | Listen for | 1.5 × 13.5 = 20.25. Lower fence 12.5 − 20.25 = −7.75. Upper fence 26 + 20.25 = 46.25.
ask | Ask | "Is 68 an outlier? And what about 42? It sits quite a way from 36."
listen | Listen for | 68 is above 46.25, so yes. 42 is below 46.25, so no, however lonely it looks.
intro | Introduce | An outlier is a value more than 1.5 × IQR above Q3 or below Q1 (1.7.D.1.i). A value exactly on a fence is not one.
:::

**The second rule.** The course description gives another method, and prep books often skip it (1.7.D.1.ii): an outlier is more than **2 standard deviations** from the mean. Here 21.44 ± 2(13.07) runs from −4.70 to 47.58, and 68 is outside, so the verdict is the same. They do not always agree. The homework (B4) shows the two rules disagreeing about last week's test scores, so do not promise that they match.

### Building the boxplot (1.8.A)

Have the student draw it by hand from the five-number summary and the fences before you show anything.

:::script
ask | Ask | "Where does the right-hand whisker end?"
listen | Listen for | At 42, the largest journey that is not an outlier.
ifsay | If "at 68" | "Is 68 an outlier? Then it gets its own symbol, and the whisker stops at the last value that isn't one."
ifsay | If "at 46.25" | "Is anyone's journey 46.25 minutes? The whisker ends at a data value. The fence is a cut-off you calculate, not something you draw."
:::

![Dotplot and boxplot of 25 journey times, upper fence at 46.25, 68 marked as an outlier](figures/s03-boxplot-commute.svg)

*The dotplot from Session 2 above its boxplot, on the same scale. The dashed line is the fence, drawn here only to show why 68 is separate; it is not part of a boxplot. The whisker stops at 42.*

**One misreading to prevent now:** the right-hand whisker is long and the left short, but each holds about a quarter of the journeys. A longer section means the values are **more spread out**, not that there are more of them.

### Resistance: move the outlier (1.7.F)

:::sim boxplot-builder | Boxplot & 1.5 × IQR Builder | 820
Hand the student the controls. Journey 25 (68 minutes) is selected when it opens. Ask them to **predict first**, then move it: *"If this student's journey had been 118 minutes, what happens to the median? The mean? The fence?"* Then have them slide it down past 46 and watch the whisker jump out to meet it. The static figure below is the same idea for print.
:::

:::script
ask | Ask | "Predict: if the 68 became 118, which of these change: mean, median, IQR, SD, range?"
listen | Listen for | Mean, SD and range change; median and IQR do not.
ifsay | If "the median goes up too" | "Which value is the median? Did the 13th value change?" It did not: 118 is still the largest, so every position below it is untouched.
intro | Introduce | **Resistant**: the median and IQR, which outliers do not greatly affect. **Nonresistant**: the mean, SD and range (1.7.F.1).
:::

![Changing the largest journey from 68 to 118 minutes moves the mean but not the median](figures/s03-resistance.svg)

*The mean moves from 21.44 to 23.44 because the total rose by 50 and 50 ÷ 25 = 2. The median, the IQR and the fence (46.25) do not move at all. The SD jumps from 13.07 to 21.56.*

**Now close the trap.** *"So which pair would you report for these journeys, and why?"* The median and IQR, because the distribution is skewed right with an outlier, and those two are resistant. Then: *"And when would the mean and SD be fine?"* When the distribution is roughly symmetric with no outliers.

> **The sentence to write down:** *With strong skew or outliers, report the median and IQR. The mean and standard deviation are pulled by the tail, so they describe the tail as much as the typical value.*

### Changing units (1.7.C)

The objective is "calculate different units of measurement for summary statistics", and the course description's own sample question tests it by adding a constant to every value. Teach the two kinds of change separately, then combine them.

**Multiplying or dividing every value.** *"The principal wants the report in hours. Which of our summaries change, and to what?"*

| Summary | Minutes | Hours (÷ 60) |
|---|---|---|
| Mean | 21.44 | 0.357 |
| Median | 18 | 0.3 |
| Q1 | 12.5 | 0.208 |
| Q3 | 26 | 0.433 |
| 84th percentile | 30 | 0.5 |
| Range | 60 | 1 |
| IQR | 13.5 | 0.225 |
| Standard deviation | 13.07 | 0.218 |

**Every** summary is divided by 60, the measures of spread included. Shrinking the number line shrinks the distances between values too.

**Adding or subtracting a constant.** *"The gate clock ran 3 minutes fast, so every recorded journey is 3 minutes too long. Correct it. What changes?"*

| Summary | As recorded | Corrected (− 3) |
|---|---|---|
| Mean | 21.44 | 18.44 |
| Median | 18 | 15 |
| Q1, Q3 | 12.5, 26 | 9.5, 23 |
| 84th percentile | 30 | 27 |
| Minimum, maximum | 8, 68 | 5, 65 |
| Range | 60 | **60** |
| IQR | 13.5 | **13.5** |
| Standard deviation | 13.07 | **13.07** |

Every value slides 3 minutes to the left and no two values move closer together, so no measure of spread changes. The fences slide too, to −10.75 and 43.25, so 65 is still the one outlier. **Changing units never changes which values are outliers.**

:::script
ask | Ask | "Sort our summaries into two groups: the ones that behave like data values, and the ones that measure a distance between values."
listen | Listen for | Centre and position: mean, median, quartiles, percentiles, minimum, maximum. Spread: range, IQR, standard deviation.
intro | Introduce | Add a constant: centre and position shift by it; spread is unchanged. Multiply by a positive constant: centre, position and spread are all multiplied by it.
:::

**The combined change: °C to °F.** The café recorded the midday temperature outside on 10 days:

```
12  14  15  15  16  18  19  21  22  28     (°C)
```

In °C: mean 18.0, median 17, Q1 15, Q3 21, IQR 6, standard deviation 4.714. The conversion F = 1.8C + 32 is a multiplication followed by an addition.

:::script
ask | Ask | "Give me the mean, median, IQR and standard deviation in °F, without converting the ten values."
listen | Listen for | Mean 1.8(18.0) + 32 = 64.4 °F. Median 1.8(17) + 32 = 62.6 °F. IQR 1.8(6) = 10.8 °F. SD 1.8(4.714) = 8.49 °F.
ifsay | If the SD is 40.49 | "You added 32. Does adding 32 to every temperature move any two days further apart?" Only the 1.8 touches spread.
:::

Check it by converting the quartiles: Q1 = 1.8(15) + 32 = 59 and Q3 = 1.8(21) + 32 = 69.8, so the IQR is 69.8 − 59 = 10.8. The + 32 cancels in the subtraction, which is exactly why spread ignores it.

**The course description's sample-question form.** Ask it as multiple choice: *"A teacher adds 1 bonus mark to every one of the 24 test scores. Which of these has the same value before and after: (A) the median, (B) the mean, (C) the third quartile, (D) the interquartile range?"* The answer is **(D)**. The other three are centre or position, and each rises by 1.

---

## 55–67 min · Activity — Match Mine

The course description's Sample Instructional Activity for topic 1.9. In class, two students sit either side of a folder, each with a blank 3×3 grid and the same nine cards. One arranges the cards and describes the arrangement; the other rebuilds it from the words alone.

**The one-to-one conversion.** You are the partner. Put the nine cards on the shared screen. Round 1: you describe your hidden grid and the student places the cards. Round 2: the student arranges their own grid on paper, in secret, and describes it; you rebuild it **literally**, placing whichever card the words fit first, even when you can guess what they meant. The literal reading is the point: it is what an examiner does.

![Nine Match Mine cards, histograms A to I on a common 0 to 100 scale](figures/s03-matchmine-cards.svg)

*The nine cards. The pairs are built to punish one missing word each: A and B differ only in spread; A and H only in centre; A and G only in an outlier; C and I only in a gap and a cluster; C and D only in the direction of skew.*

### Round 1: your hidden grid

Read each position aloud, in this order. Do not point.

| Position | Your description | Card |
|---|---|---|
| Top left | Symmetric and unimodal, centred at about 50, with most values between 30 and 70, and **one outlier above 90**, separated by a gap | G |
| Top middle | **Skewed right**, peak between 10 and 20, tail stretching out to about 90 with **no gaps** | C |
| Top right | **Approximately uniform** from 0 to 100, no peak | F |
| Middle left | Symmetric and unimodal, centred at about 50, **narrow**: nearly all values between 30 and 70, **no outliers** | A |
| Centre | Skewed right, peak between 10 and 20, then **a gap from 50 to 80** and a small **cluster** between 80 and 100 | I |
| Middle right | **Skewed left**, peak between 80 and 90, tail stretching down to about 10 | D |
| Bottom left | **Bimodal**, with peaks near 25 and 75 and very few values near 50 | E |
| Bottom middle | Symmetric and unimodal, **centred at about 30**, narrow: nearly all values between 0 and 60 | H |
| Bottom right | Roughly symmetric, a broad single mound centred at about 50, **wide**: values across almost the whole range from 0 to 100 | B |

Check their grid against the last column. Any mismatch is a word they did not hear or did not know; ask which word it was.

### Round 2: the student describes, you rebuild literally

Give them 90 seconds to arrange and three minutes to describe. Rebuild strictly. Typical failures, and the card you should place to expose them:

| They say | You place | Word they needed |
|---|---|---|
| "symmetric, centred at 50" | B (when they meant A) | narrow, or a spread |
| "skewed, peak at the low end" | D (when they meant C) | the direction: skewed **right** |
| "centred at 50, one peak" | G (when they meant A) | "no outliers" |
| "skewed right with a peak at 10 to 20" | I (when they meant C) | "no gaps" |
| "two peaks" or "flat" | whichever comes first | bimodal against uniform |

### The debrief question that makes this topic 1.9

:::script
ask | Ask | "If I turned every card into a boxplot, which two cards would be hardest to tell apart?"
listen | Listen for | E and F: bimodal and uniform. Both have median about 50 and quartiles about 25 and 75.
intro | Introduce | Histograms, dotplots and stemplots can compare centre, variability, shape, outliers, clusters and gaps. Boxplots can compare centre, variability, outliers and skewness or symmetry, but not clusters or gaps (1.9.A.1).
:::

![Card E is bimodal and card F is uniform, yet their boxplots are almost identical](figures/s03-lookalike.svg)

*Card E: 5, 24.45, 50, 75.55, 95. Card F: 1.2, 25, 50, 75, 98.8. The five-number summaries are nearly the same, and E's median sits where almost no data lie.*

---

## 67–97 min · Scenario B — comparing distributions: two hospitals, then two library branches

Back to Session 1's hospital survey. It recorded, for each of the 300 patients, the minutes from arrival to being seen by a doctor. Here are the two largest hospitals.

Waiting time from arrival to being seen by a doctor, in minutes, for the surveyed patients at St Mary's and Riverside:

| Hospital | *n* | *x̄* | *s* | Min | Q1 | Median | Q3 | Max |
|---|---|---|---|---|---|---|---|---|
| St Mary's | 84 | 37.1 | 16.3 | 12 | 25.5 | 34 | 45 | 97 |
| Riverside | 71 | 26.0 | 7.4 | 8 | 21 | 26 | 31 | 44 |

**The trap this scenario carries: two descriptions are not a comparison.** Students who can now produce five numbers for each hospital will write a paragraph about St Mary's and a paragraph about Riverside, and every statement in both will be true. It will not earn the comparison marks. The CED verb is *compare* (1.7.E, 1.9.A–B), and an examiner wants the relationship between the groups stated: *greater than, less than, more variable than*.

### Outliers first

:::script
ask | Ask | "St Mary's four largest waits were 70, 75, 88 and 97 minutes. Which of them are outliers?"
listen | Listen for | IQR = 45 − 25.5 = 19.5; 1.5 × 19.5 = 29.25; upper fence 45 + 29.25 = 74.25. So 75, 88 and 97 are outliers; 70 is not.
ask | Ask | "And Riverside?"
listen | Listen for | IQR = 10; fences 21 − 15 = 6 and 31 + 15 = 46. Minimum 8 and maximum 44 are inside, so no outliers.
:::

![Parallel boxplots of waiting times at St Mary's and Riverside](figures/s03-boxplot-hospitals.svg)

*Both hospitals on one scale, which is the only honest way to compare them. St Mary's upper whisker stops at 70; 75 is an outlier by three quarters of a minute.*

### Write the comparison

Ask for it in writing: *"Compare the waiting times at the two hospitals. Centre, variability, shape, outliers."* Let the student write before you say anything. If what comes back is two separate descriptions, do not correct the content. Ask: *"Which sentence tells me how St Mary's relates to Riverside?"*

> *"The median wait at St Mary's (34 minutes) is **longer than** at Riverside (26 minutes). Waits at St Mary's are **more variable**: the IQR is 19.5 minutes against Riverside's 10, and the range is 85 minutes against 36. St Mary's distribution is **skewed right** (mean 37.1 above median 34, and a longer upper whisker), while Riverside's is **roughly symmetric** (mean and median both 26, and Q1 and Q3 each 5 minutes from the median). St Mary's has **three high outliers**, at 75, 88 and 97 minutes; Riverside has **none**."*

| Component | The comparative words |
|---|---|
| Centre | median 34 **longer than** 26 |
| Variability | IQR 19.5 **against** 10, **more variable** |
| Shape | skewed right **while** roughly symmetric, with the evidence |
| Unusual features | three outliers **against** none |
| **In context** | waiting time, minutes, patients at each hospital |

### Shape from numbers alone (1.8.B)

*"If you had only the table and no picture, how would you know St Mary's is skewed right?"* Two ways: the mean (37.1) is greater than the median (34), and the distance from Q1 to the median (8.5) is smaller than from the median to Q3 (11). The course description's sample scoring guidelines list "the distribution is right-skewed" on its own as an answer that does **not** earn the point, so the student must quote the comparison.

### Relative position: z-scores (1.9.D–E)

:::script
ask | Ask | "One St Mary's patient waited 62 minutes. One Riverside patient waited 41. Whose wait was more unusual for their own hospital?"
listen | Listen for | Most students say the 62-minute wait, because it is longer. Let them commit.
intro | Introduce | z = (*x* − μ) ÷ σ, the number of standard deviations above or below the mean (1.9.D.2). When the population values are unknown, use *x̄* and *s*, as here.
ask | Ask | "Work out both."
listen | Listen for | St Mary's (62 − 37.1) ÷ 16.3 = 1.53. Riverside (41 − 26.0) ÷ 7.4 = 2.03. The Riverside wait is the more unusual one.
:::

Connect it to C1 from the homework: the raw number misled for the same reason as the fiction count. Each hospital has its own centre and spread, and a wait only means something measured against them.

### Justify a claim (1.9.C)

*"The network says: patients are seen faster at Riverside. Supported?"* Yes, and the strongest evidence is positional: Riverside's **Q3 (31 minutes) is below St Mary's median (34)**, so about three quarters of Riverside patients were seen within 31 minutes, while fewer than half of St Mary's were. In the survey that is 55 of 71 Riverside patients (77.5%) against 36 of 84 at St Mary's (42.9%). Same template as Sessions 1 and 2: **state the claim · quote the numbers · say what they do and do not establish · keep it in context.** What they do not establish: *why*. These are survey data, not an experiment, and St Mary's may see sicker patients.

### A second comparison, from a summary table alone (1.7.E–F)

Comparing is practised twice before the homework. This time there is no picture, only the kind of table a free-response question prints, and a new decision: **which measure of spread to compare**. Session 1's library service took a random sample of members at each of two branches and recorded the hours each spent in library buildings last year.

| Branch | *n* | *x̄* | *s* | Min | Q1 | Median | Q3 | Max |
|---|---|---|---|---|---|---|---|---|
| Central | 35 | 40.0 | 11.0 | 16 | 32 | 40 | 48 | 64 |
| Westside | 30 | 28.0 | 17.2 | 8 | 17 | 24.5 | 34 | 96 |

:::script
ask | Ask | "Does either branch have outliers? Use the fences."
listen | Listen for | Central: IQR 16, fences 8 and 72; the minimum 16 and maximum 64 are inside, so none. Westside: IQR 17, fences −8.5 and 59.5; the maximum, 96, is an outlier.
ifsay | If "Westside has exactly one outlier" | "Can the table tell you whether any other Westside value is above 59.5?" It cannot: only that the maximum is. "At least one" is the precise answer.
ask | Ask | "Westside's standard deviation is 17.2 against Central's 11.0. So Westside's members are much more variable. Agree?"
listen | Listen for | Not really. The IQRs are 17 and 16, almost equal. Westside's standard deviation and range are inflated by the 96-hour member, and both are nonresistant.
intro | Introduce | Choose the summary to fit the shape (1.7.F): with an outlier or strong skew in either group, compare medians and IQRs. This is the resistance lesson from Scenario A, applied to a comparison.
:::

Then the written comparison, in full, with a comparative word in every sentence:

> *"The median time spent in the library is higher at Central (40 hours) than at Westside (24.5 hours). The middle half of members is about equally spread at the two branches (IQR 16 hours at Central, 17 at Westside), although Westside has the larger standard deviation and range, largely because of one member who spent 96 hours. Central's distribution is roughly symmetric (mean and median both 40, and Q1 and Q3 each 8 hours from the median), while Westside's is skewed right (mean 28.0 above median 24.5, and a longer upper tail). Westside has a high outlier at 96 hours; Central has none."*

![Parallel boxplots of hours spent in the library, Central and Westside](figures/s03-boxplot-library.svg)

*The same two branches drawn from the raw data. Westside's upper whisker ends at 55, the largest value that is not an outlier. The summary table alone could not tell you where it stops, only that 96 is beyond the fence.*

**The claim.** *"Central's members spend more time in the library."* Supported: Central's **Q1 (32 hours) is above Westside's median (24.5)**, so at least three quarters of the Central sample spent longer than half of the Westside sample. In the data, 32 of 35 Central members (91.4%) spent more than 24.5 hours, against 15 of 30 at Westside. What it does not show is why: the branches may serve different neighbourhoods, and nobody was assigned to a branch.

---

## 97–105 min · Solo case — the café

Unaided. The same café as Session 2's solo case. Watch, say nothing, note where they hesitate.

Drinks sold per hour over 20 opening hours:

```
14  16  17  19  20  21  21  22  23  24
24  25  26  27  28  30  31  33  35  52
```

1. Find the five-number summary.
2. Use the 1.5 × IQR rule to identify any outliers. Show the fences.
3. Draw the boxplot.
4. The mean is 25.4 and the standard deviation 8.39. Which measures of centre and spread would you report for these data, and why?

**Answers.**

1. n = 20 is even, so no value is left out. Median = (24 + 24) ÷ 2 = **24**. Lower half 14 … 24 gives Q1 = (20 + 21) ÷ 2 = **20.5**; upper half 24 … 52 gives Q3 = (28 + 30) ÷ 2 = **29**. Five-number summary **14, 20.5, 24, 29, 52**.
2. IQR = 8.5; 1.5 × 8.5 = 12.75. Fences 20.5 − 12.75 = **7.75** and 29 + 12.75 = **41.75**. **52 is an outlier**; nothing is below 7.75.
3. Box 20.5 to 29, median line at 24, whiskers to 14 and to **35**, and 52 marked separately.
4. The **median (24) and IQR (8.5)**, because there is a high outlier and the distribution is skewed right. The mean (25.4) is above the median, pulled up by the 52, and the SD is inflated by it too.

![Boxplot of drinks sold per hour at the café, 52 marked as an outlier](figures/s03-boxplot-cafe.svg)

*The answer to item 3.*

**Watch for:** the right whisker drawn to 52 or to 41.75; Q1 computed as the 5th value (20) instead of the mean of the 5th and 6th; answering item 4 with "the mean, because it uses all the data" (true of the mean, and exactly why it is pulled by the outlier).

---

## 105–110 min · Teach it back

> *"Explain to me why the median didn't move when the 68-minute journey became 118, and why the fence didn't move either."*

A good answer contains three things. The median is the 13th value, and making the largest value larger does not change which value is 13th. The fence is built from Q1 and Q3, which are also positional and also unchanged. The mean, by contrast, adds up every value, so an extra 50 minutes spread over 25 students raises it by 2.

If it comes out cleanly, the resistance idea has landed. If the student says "because it's resistant" and stops, ask *"what does resistant mean happens inside the calculation?"*; the word without the mechanism will not survive an unfamiliar question. Then set the homework.

---
---

# Homework — Session 3

**45 marks · bring to Session 4, self-marked**

## How to do this homework

1. Do every part **with the answer key closed.** Where you are unsure, answer anyway and put a **?** beside it.
2. Then open the key and **mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote.
3. **Bring the marked sheet.** Your wrong answers and your question marks are what Session 4 opens with.

Everything here was taught in the session; this sheet is practice. You need a calculator for the arithmetic and a ruler for B3 and E2. Use the course's quartile convention throughout: **Q1 and Q3 are the medians of the lower and upper halves, and when n is odd the median is left out of both halves.**

---

## Part A — Vocabulary (6 marks)

Match each term to its meaning.

| | Term | | Meaning |
|---|---|---|---|
| 1 | Resistant statistic | A | The difference Q3 − Q1 |
| 2 | Interquartile range | B | The value that has p% of the data less than or equal to it |
| 3 | Five-number summary | C | The number of standard deviations a value lies above or below the mean |
| 4 | pth percentile | D | A statistic whose value outliers do not greatly affect |
| 5 | z-score | E | Minimum, Q1, median, Q3, maximum |
| 6 | Standard deviation | F | A typical distance of the data values from their mean |

## Part B — Last session's test scores, summarised (13 marks)

These are the same 24 scores, out of 50, that you described in the Session 2 homework:

```
12  24  29  31  33  35  36  37  38  38  39  40
40  41  41  42  42  43  43  44  45  45  46  47
```

**B1.** Find the five-number summary. Write out which values form the lower half and which form the upper half. (3)

**B2.** Calculate the IQR and both fences. List **every** score the 1.5 × IQR rule identifies as an outlier. (3)

**B3.** Draw a boxplot, marking any outliers separately. State the value at which each whisker ends. (3)

**B4.** The mean is 37.96 and the standard deviation is 7.88. Apply the 2-standard-deviation rule for outliers. Do the two rules agree? (2)

**B5.** Compare the mean with the median and say what the comparison suggests about the shape of the distribution. Quote both numbers. (2)

## Part C — Standard deviation by hand (6 marks)

Five library members borrowed these numbers of items last year:

```
2   4   5   7   12
```

**C1.** Calculate the mean. (1)

**C2.** Make a table with columns *x*, *x* − *x̄* and (*x* − *x̄*)². Check that the deviations add to zero. (2)

**C3.** Calculate the sample variance *s*² and the sample standard deviation *s*. **State the formula first.** (2)

**C4.** Interpret your value of *s* in context, in one sentence. (1)

## Part D — Changing units (6 marks)

Return to the 24 test scores from Part B. Their mean is 37.96, median 40, IQR 7.5 and standard deviation 7.88.

**D1.** The teacher adds **3 bonus marks** to every score. Give the new mean, median, IQR and standard deviation. (2)

**D2.** Instead, the teacher converts every original score to a **percentage** by multiplying it by 2. Give the new mean, IQR and standard deviation. (2)

**D3.** The café's fridge log, in °C, has mean 4.0, median 3.95, IQR 0.70 and standard deviation 0.60. Using F = 1.8C + 32, give all four in °F. (2)

## Part E — Comparing two schools' journeys (10 marks)

Nearby Oakfield School asked a random sample of 20 of its students how long their journey to school took, in minutes:

```
6   8   9  10  11  12  12  13  13  14
15  15  16  17  18  19  21  23  26  38
```

**E1.** Find the five-number summary, and use the 1.5 × IQR rule to identify any outliers. Show the fences. (3)

**E2.** On one scale, draw parallel boxplots of the Oakfield journeys and the 25 Lincoln High journeys from the session (five-number summary 8, 12.5, 18, 26, 68; the largest Lincoln High journey that is not an outlier is 42). (2)

**E3.** Compare the two distributions of journey times. Your answer must address **centre, variability, shape and outliers**, use comparative language, and be in context. (5)

## Part F — z-scores (4 marks)

Suppose Lincoln High later timed **every one of its 1,842 students'** journeys. For the whole school, μ = 22 minutes and σ = 11 minutes. Nearby Oakfield School did the same for all its students: μ = 15 minutes and σ = 5 minutes.

Priya, at Lincoln High, takes **38 minutes**. Sam, at Oakfield, takes **26 minutes**.

**F1.** Calculate the z-score for each journey. **State the formula first.** (2)

**F2.** Whose journey is more unusual compared with the other students at their own school? Justify your answer. (1)

**F3.** Another Lincoln High student's journey has a z-score of −0.5. How long is that journey? (1)

---
---

# Answer key

*For the student to mark their own work, after attempting everything.*

### Part A (6 marks, 1 each)

1–D · 2–A · 3–E · 4–B · 5–C · 6–F

### Part B (13 marks)

**B1.** (3) With n = 24 (even), the median is the mean of the 12th and 13th values: (40 + 40) ÷ 2 = **40**. Because n is even, no value is left out; each half has 12 values.

- Lower half: 12 24 29 31 33 **35 36** 37 38 38 39 40 → Q1 = (35 + 36) ÷ 2 = **35.5**
- Upper half: 40 41 41 42 42 **43 43** 44 45 45 46 47 → Q3 = (43 + 43) ÷ 2 = **43**

Five-number summary: **12, 35.5, 40, 43, 47**. One mark for the halves written out, one for Q1 and Q3, one for the median, minimum and maximum.

**B2.** (3) IQR = 43 − 35.5 = **7.5** (1). 1.5 × 7.5 = 11.25, so the lower fence is 35.5 − 11.25 = **24.25** and the upper fence is 43 + 11.25 = **54.25** (1). The outliers are **12 and 24**, both below 24.25; nothing is above 54.25 (1).

> **If you listed only 12, you are not alone.** Last session's model description, written by eye, named one outlier. The rule is stricter than the eye: 24 is below the fence by a quarter of a mark, and "below the fence" is the whole test. When a question says *use the 1.5 × IQR rule*, the rule decides, not the picture.

**B3.** (3) Box from 35.5 to 43 with a line at 40 (1). The left whisker ends at **29**, the smallest score that is not an outlier; the right whisker ends at **47** (1). The scores 12 and 24 are marked separately with a symbol (1).

:::reveal Reveal — the B3 boxplot, after you have drawn yours
![Boxplot of the 24 test scores with outliers at 12 and 24](figures/s03-boxplot-scores.svg)

*The answer to B3. The left whisker stops at 29, not at 12, and not at the fence of 24.25. A fence is a cut-off you calculate; it is never drawn as part of the boxplot.*
:::

**B4.** (2) *x̄* − 2 *s* = 37.96 − 2(7.88) = **22.20** and *x̄* + 2 *s* = 37.96 + 15.76 = **53.72** (1). Only **12** lies more than 2 SD from the mean, so by this rule 24 is **not** an outlier. The two rules disagree about 24 (1).

> Both rules are in the course description (1.7.D.1), and it says there are *many* methods. Neither is "the right one". What loses marks is not saying which rule you used, or not showing the calculation.

**B5.** (2) The mean, **37.96**, is less than the median, **40** (1). That fits a distribution **skewed left**: the long tail of low scores (12 and 24) pulls the mean down, while the median stays with the bulk in the 40s (1).

> This is the same distribution that the Session 2 homework asked you to describe (E1). If you called it skewed right then, the numbers now settle it: the mean is below the median, and the tail is on the left.

### Part C (6 marks)

**C1.** (1) *x̄* = (2 + 4 + 5 + 7 + 12) ÷ 5 = 30 ÷ 5 = **6** items.

**C2.** (2)

| *x* | *x* − *x̄* | (*x* − *x̄*)² |
|---|---|---|
| 2 | −4 | 16 |
| 4 | −2 | 4 |
| 5 | −1 | 1 |
| 7 | 1 | 1 |
| 12 | 6 | 36 |
| **Total** | **0** | **58** |

The deviations total 0, as they always must (1 for the deviations with the check, 1 for the squares totalling 58).

**C3.** (2) *s*² = Σ(*x* − *x̄*)² ÷ (*n* − 1) = 58 ÷ 4 = **14.5** (1), so *s* = √14.5 = **3.81** items (1).

> **Divide by n − 1, not n.** Dividing by 5 gives 11.6 and 3.41, which is wrong for a sample. The formula is on the exam formula sheet with *n* − 1 in it; check it there rather than from memory.

**C4.** (1) *"The number of items these members borrowed typically differs from the mean of 6 items by about 3.8 items."* The mark needs the context (items borrowed) and the idea of a typical distance from the mean.

### Part D (6 marks)

**D1.** (2) Adding 3 to every score moves every value up by 3, so measures of centre and position shift and measures of spread do not. New mean **40.96** and median **43** (1). IQR still **7.5** and SD still **7.88** (1).

**D2.** (2) Multiplying every score by 2 multiplies centre **and** spread by 2. New mean **75.92%** (1). New IQR **15** percentage points and new SD **15.76** percentage points (1).

**D3.** (2) Centre gets both steps: mean 1.8(4.0) + 32 = **39.2 °F** and median 1.8(3.95) + 32 = **39.11 °F** (1). Spread gets only the multiplication: IQR 1.8(0.70) = **1.26 °F** and standard deviation 1.8(0.60) = **1.08 °F** (1). (From the unrounded standard deviation the answer is 1.09; accept either.)

> The pattern to keep: **adding** a constant changes centre but not spread; **multiplying** changes both. If you changed the SD in D1, picture the dotplot sliding three marks to the right: every dot moves, none moves closer to any other.

### Part E (10 marks)

**E1.** (3) *n* = 20 is even, so each half has 10 values. Median = (14 + 15) ÷ 2 = **14.5**. Lower half 6 8 9 10 **11 12** 12 13 13 14 gives Q1 = **11.5**; upper half 15 15 16 17 **18 19** 21 23 26 38 gives Q3 = **18.5**. Five-number summary **6, 11.5, 14.5, 18.5, 38** (1). IQR = 7; 1.5 × 7 = 10.5; fences 11.5 − 10.5 = **1** and 18.5 + 10.5 = **29** (1). **38 is an outlier**; nothing is below 1 (1).

**E2.** (2) One mark for each boxplot, on a shared scale. Oakfield: box 11.5 to 18.5, median 14.5, whiskers to 6 and **26**, and 38 marked separately. Lincoln High: box 12.5 to 26, median 18, whiskers to 8 and **42**, and 68 marked separately.

:::reveal Reveal — the E2 parallel boxplots, after you have drawn yours
![Parallel boxplots of journey times, Lincoln High and Oakfield samples](figures/s03-boxplot-oakfield.svg)

*The answer to E2. Both upper whiskers stop at the largest value that is not an outlier: 42 at Lincoln High and 26 at Oakfield.*
:::

**E3.** (5) One mark each for centre, variability, shape and outliers, each stated as a comparison, and one for context throughout. A model answer:

> *"The median journey is longer at Lincoln High (18 minutes) than at Oakfield (14.5 minutes). Lincoln High's journeys are much more variable: the IQR is 13.5 minutes against Oakfield's 7, and the range 60 minutes against 32. Both distributions are skewed right, Lincoln High's more strongly (its mean, 21.44, is 3.44 minutes above its median, against 1.3 minutes at Oakfield, where the mean is 15.8; and Q1 to median is 5.5 minutes against median to Q3 of 8, compared with 3 against 4 at Oakfield). Each school has one high outlier: a 68-minute journey at Lincoln High and a 38-minute journey at Oakfield."*

> **The most common way to lose these marks is to describe each school separately** — "Lincoln High has a median of 18. Oakfield has a median of 14.5." That is two descriptions, not a comparison. Each sentence needs a comparative word: *longer than, shorter than, more variable than, about the same as.*

> A link to Part F: this sample's mean, 15.8 minutes, is a **statistic**. Part F's μ = 15 minutes for all of Oakfield is a **parameter**. They are close but not equal, as Session 1 said they would be.

### Part F (4 marks)

**F1.** (2) z = (*x* − μ) ÷ σ.
Priya: (38 − 22) ÷ 11 = 16 ÷ 11 = **1.45** (1). Sam: (26 − 15) ÷ 5 = 11 ÷ 5 = **2.20** (1).

**F2.** (1) **Sam's** journey is more unusual for his school: it is 2.20 standard deviations above Oakfield's mean, while Priya's is 1.45 above Lincoln High's, even though Priya's journey is longer in minutes.

**F3.** (1) *x* = μ + zσ = 22 + (−0.5)(11) = 22 − 5.5 = **16.5 minutes**.

> **The raw number is not the comparison.** 38 minutes is longer than 26, but each school has its own centre and spread. This is the same mistake as Session 2's C1, where fiction's raw count went up while its share went down: a number means nothing until you know what it is measured against.

### Marks summary

| Part | Marks |
|---|---|
| A — Vocabulary | 6 |
| B — Test scores summarised | 13 |
| C — Standard deviation by hand | 6 |
| D — Changing units | 6 |
| E — Comparing two schools | 10 |
| F — z-scores | 4 |
| **Total** | **45** |

---
---

# Reference sheet — keep this

*Every term carries an example. The examples use the Lincoln High journey times unless stated: 25 values from 8 to 68 minutes.*

### The quartile convention used in this course

To find Q1 and Q3, split the ordered data into a lower and an upper half at the median. **When n is odd, the median itself belongs to neither half.** Q1 is the median of the lower half and Q3 the median of the upper half. This is what a TI-84's 1-Var Stats does.
*Example: with 25 journey times the median is the 13th value, 18; each half has 12 values; Q1 = 12.5 and Q3 = 26.*

> Other methods exist: some books include the median in both halves, and some software interpolates. They can give slightly different quartiles. The course description calls these *common* methods rather than insisting on one, so pick this one, use it every time, and show your working.

### Centre and position (1.7.A)

**Mean** — the sum of the values divided by how many there are: *x̄* = Σ *x*ᵢ ÷ *n*.
*Example: 536 ÷ 25 = 21.44 minutes.*

**Median** — the middle value of the ordered data. With an odd *n* it is the middle value; with an even *n*, the mean of the two middle values.
*Example: the 13th of 25 journeys, 18 minutes. For 1, 4, 7, 9 it is (4 + 7) ÷ 2 = 5.5.*

**Minimum and maximum** — the smallest and largest values.
*Example: 8 and 68 minutes.*

**First and third quartiles, Q1 and Q3** — the medians of the lower and upper halves. About 25% of values are at or below Q1 and about 75% at or below Q3; together they bound the middle 50%.
*Example: Q1 = 12.5 and Q3 = 26 minutes. (Q2 is another name for the median.)*

**pth percentile** — the value with p% of the data less than or equal to it.
*Example: 21 of the 25 journeys are 30 minutes or less, and 21 ÷ 25 = 84%, so 30 minutes is the 84th percentile.*

### Variability (1.7.B)

**Range** — maximum − minimum.
*Example: 68 − 8 = 60 minutes.*

**Interquartile range (IQR)** — Q3 − Q1, the spread of the middle half.
*Example: 26 − 12.5 = 13.5 minutes.*

**Standard deviation, s** — a typical distance of the values from their mean. *s* = √[Σ(*x*ᵢ − *x̄*)² ÷ (*n* − 1)]. It is on the formula sheet.
*Example by hand: for 10, 14, 18, 22, 36 the mean is 20, the squared deviations total 400, s² = 400 ÷ 4 = 100 and s = 10 minutes. For all 25 journeys (calculator): s = 13.07 minutes, so a typical journey differs from the mean of 21.44 by about 13 minutes.*

**Variance, s²** — the square of the standard deviation.
*Example: s² = 170.76 minutes², calculated before rounding s. The units are squared minutes, which is why s, not s², is the number to report.*

### Outliers (1.7.D)

The course description gives two methods, and both are examinable.

| Rule | An outlier is a value… | Example: journey times |
|---|---|---|
| **1.5 × IQR** | more than 1.5 × IQR above Q3 or below Q1 | fences 12.5 − 20.25 = −7.75 and 26 + 20.25 = 46.25; **68 is an outlier**, 42 is not |
| **2 SD** | more than 2 standard deviations above or below the mean | 21.44 ± 2(13.07) gives −4.70 to 47.58; **68 is an outlier** |

The two rules can disagree. *Example: for last session's test scores the 1.5 × IQR rule flags 12 and 24; the 2 SD rule flags only 12.* Say which rule you are using, and show the calculation. A value exactly on a fence is **not** an outlier ("more than").

> "Fence" is this course's shorthand for Q1 − 1.5 × IQR and Q3 + 1.5 × IQR. The course description does not use the word, so in an exam write the calculation out rather than relying on it.

### Five-number summary and boxplot (1.8.A)

**Five-number summary** — minimum, Q1, median, Q3, maximum.
*Example: 8, 12.5, 18, 26, 68.*

**Boxplot** — a picture of the five-number summary. The box runs from Q1 to Q3 with a line at the median. Whiskers run out to the most extreme values that are **not** outliers, and outliers are marked separately with a symbol such as an asterisk.
*Example: whiskers from 8 to 12.5 and from 26 to 42; 68 is plotted on its own.*

> **Whiskers stop at data, never at a fence.** The upper whisker ends at 42, the largest journey that is not an outlier, not at 46.25 and not at 68. Each whisker and each half of the box holds about a quarter of the data, so **a longer section means more spread, not more values.** Prep books sometimes call this a *modified* boxplot; the course description calls it a boxplot.

### Resistance (1.7.F)

A **resistant** (robust) statistic is one that outliers do not greatly affect, if at all.

| Resistant | Nonresistant |
|---|---|
| median, IQR | mean, standard deviation, range |

*Example: change the 68-minute journey to 118. The median stays 18 and the IQR stays 13.5; the mean rises from 21.44 to 23.44, the SD from 13.07 to 21.56 and the range from 60 to 110.*

**Which to report.** With strong skew or outliers, report the median and IQR. With a roughly symmetric distribution and no outliers, the mean and standard deviation are fine.

### Mean, median and shape (1.8.B)

| Shape | Usually |
|---|---|
| Roughly symmetric | mean ≈ median |
| Skewed right | mean > median |
| Skewed left | mean < median |

*Example: journey times, mean 21.44 > median 18, skewed right. Test scores, mean 37.96 < median 40, skewed left.*

You can also compare the distances Q1 → median and median → Q3. *Example: 12.5 → 18 is 5.5 minutes and 18 → 26 is 8 minutes; the upper half is more spread out, which also suggests right skew.*

> **Say the comparison, not only the verdict.** In the sample scoring guidelines printed in the course description, "The distribution is right-skewed" on its own is listed as an answer that does **not** earn the point. The answers that earn it quote the comparison: the median is smaller than the mean, or the distance from Q1 to the median is smaller than the distance from the median to Q3.

### Changing units (1.7.C)

| Change to every value | Mean, median, quartiles | SD, IQR, range |
|---|---|---|
| **Add** or subtract a constant | shift by that constant | **unchanged** |
| **Multiply** or divide by a constant | multiplied by it | multiplied by it |

*Example: in hours, the mean journey is 21.44 ÷ 60 = 0.357 h and the SD 13.07 ÷ 60 = 0.218 h. If every time is reduced by 3 minutes, the mean becomes 18.44 minutes and the SD stays 13.07.*

**Both at once**, such as °C to °F with F = 1.8C + 32: centre and position get both steps, spread gets only the multiplication.
*Example: café midday temperatures, mean 18.0 °C and SD 4.714 °C, become mean 1.8(18.0) + 32 = 64.4 °F and SD 1.8(4.714) = 8.49 °F.*

Changing units never changes which values are outliers: the fences move with the data.

### z-scores (1.9.D–E)

**z-score** — how many standard deviations a value lies above (positive) or below (negative) the mean: z = (*x* − μ) ÷ σ. When the population values are unknown, use *x̄* and *s*.
*Example: a St Mary's patient who waited 62 minutes: (62 − 37.1) ÷ 16.3 = 1.53. A Riverside patient who waited 41 minutes: (41 − 26.0) ÷ 7.4 = 2.03. The shorter wait is the more unusual one for its hospital.*

z-scores compare relative positions within a distribution or **between** distributions with different centres and spreads.

### Comparing distributions (1.7.E, 1.9)

A comparison covers **centre, variability, shape and outliers**, in context, and every sentence uses a **comparative word**: *greater than, less than, more variable than, similar to.*
*Example: "The median wait at St Mary's (34 minutes) is greater than at Riverside (26 minutes)."*

Choose the summaries to fit the shape: if either group has an outlier or strong skew, compare **medians and IQRs**.
*Example: the Westside library branch has a larger SD than Central (17.2 against 11.0 hours) only because of one 96-hour member; the IQRs, 17 and 16, are almost equal.*

| Display | Can compare |
|---|---|
| Dotplots, histograms, back-to-back stemplots | centre, variability, shape, outliers, **clusters and gaps** |
| Boxplots | centre, variability, outliers, skewness or symmetry — but **not** clusters or gaps |

*Example: a bimodal distribution and a uniform one can have almost identical boxplots (Match Mine cards E and F).*

:::note red Not in the course description
**Chebyshev's rule** ("at least 1 − 1/k² of any data lie within k standard deviations of the mean") appears in 5 Steps to a 5 but nowhere in the course description. It is not examinable. The **empirical rule** (68–95–99.7) *is* in the course, but in topic 2.11 with the normal distribution, not here.
:::

---

*CED references: Topic 1.7 (1.7.A.1–6, 1.7.B.1–4, 1.7.C.1, 1.7.D.1, 1.7.E.1, 1.7.F.1–2), Topic 1.8 (1.8.A.1–2, 1.8.B.1), Topic 1.9 (1.9.A.1, 1.9.B.1, 1.9.C.1, 1.9.D.1–2, 1.9.E.1). Course and Exam Description effective Fall 2026.*

*Supporting reading: Barron's pdf 107–133 · Princeton Review 124–143 · 5 Steps to a 5 66–73.*

*Next session: Topics 5.1–5.2 — scatterplots and correlation. Two variables at once, and the first time the course asks whether one thing is associated with another.*
