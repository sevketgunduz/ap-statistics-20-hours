# Session 2 — Showing and Describing One Variable

**AP Statistics · Twenty-Hour Course · Student edition, to work through on your own**
**CED Topics 1.4, 1.5, 1.6 · About 75 minutes, plus homework**

---

## How to use this

Same rule as last time, and it matters more in this session than it did in the last one.

> Every **Your turn** box asks you to do something before the text shows you the answer. **Do it on paper first.** Several of these ask you to *draw* a graph — and the finished graph is hidden behind the reveal precisely so that you cannot copy it.

Drawing a histogram by looking at a histogram teaches you nothing. Drawing one from a list of 25 numbers, getting a bin boundary wrong, and finding out where you went wrong — that is the whole exercise.

**What you need:** paper, a pen, a ruler, and a protractor. Squared paper helps but is not essential. No calculator today.

### How this maps to your tutor's document

| Your section | Tutor's section | Minutes |
|---|---|---|
| Part 1 — Your Session 1 homework, and a warm-up | 0–8 Homework debrief and diagnostic | 8 |
| Part 2 — Why this matters | (the framing) | 2 |
| Part 3 — The hospital survey, in pictures | 8–18 Scenario A | 18 |
| Part 4 — The commute times, in pictures | 18–32 Scenario B | 20 |
| Part 5 — Describing a distribution | 32–46 The four components | 18 |
| Part 6 — On your own: the café | 46–54 Solo case | 8 |
| Part 7 — Explain it back | 54–60 Teach it back | 5 |

---

## Part 1 — Your Session 1 homework, and a warm-up

Before anything else, get out your marked Session 1 homework and make two lists:

1. The questions you got **wrong**.
2. The questions you marked with a **?** — including the ones that turned out right.

That second list is the more useful one. A question you guessed correctly is a question you will get wrong under exam pressure.

**Two specific things to check.** These are the two most common errors on that sheet, and both come back repeatedly:

- **B5** — did you answer *"parameter"*? The value 171 ÷ 450 came from the 450 people actually asked, so it describes the **sample**. It is a statistic. Check the denominator, every time.
- **D4** — did you answer *"yes, supported"*? Bus was 42.5%, which is the **largest** share but not **most**. "Most" means more than half. This plurality-versus-majority distinction appears in every unit of this course.

### Warm-up

Three questions. Answer on paper before reading on.

**Q1.** Give me a categorical variable and a quantitative variable, from anything at all.

**Q2.** If I have a table of counts for six hospitals, what could I draw?

**Q3.** What does a histogram show you that a plain list of numbers doesn't?

<details>
<summary><strong>Reveal — and what Q3 tells you</strong></summary>

**Q1.** Anything valid. Travel mode and journey time; eye colour and height; membership type and number of visits.

**Q2.** A bar chart or a pie chart. Both are for a single categorical variable.

**Q3.** This is the question that matters. The answer you want is something about **shape** or **pattern** — a histogram lets you see at a glance whether the values pile up at one end, whether there is a single peak, whether anything sits far away from everything else.

If your answer was only *"it's easier to read"* or *"it looks nicer"*, that is exactly the gap this session fills. A graph is not decoration for a list of numbers; it shows you a property of the data — its shape — that the list contains but hides.

</details>

---

## Part 2 — Why this matters

This session has two halves, and they are not equally important.

The first half is **construction**: turning a table into a bar chart, a pie chart, a dotplot, a stemplot, a histogram. This is genuinely a five-minute skill once you have the formulas.

The second half is **description**: saying what a distribution looks like in a way that earns marks. Students still get this wrong in April, because a full description requires **four** specific things, in context, and most people say two of them and stop.

If you are short of time today, spend it on Part 5.

---

## Part 3 — The hospital survey, in pictures

This is the same data you tabulated in Session 1. Nothing new has been collected — you are only going to re-encode it.

> The same **300 surveyed patients**, by hospital:
>
> **St Mary's 84 · Riverside 71 · Northgate 52 · Parkview 45 · Eastwood 30 · Hillcrest 18**

### What does the height of a bar mean?

**Your turn.** If you drew a bar chart of this, what would the height of the St Mary's bar be?

<details>
<summary><strong>Reveal</strong></summary>

Either **84** or **0.280** — and both are right. That is the point.

A **bar chart** shows one bar per category, and the height (or length) can show either the **frequency** (the count, 84) or the **relative frequency** (the proportion, 0.280). Switching between them changes nothing about the shape of the picture — only the numbers on the axis.

One rule that is easy to lose marks on: **the bars must not touch.** Categories are separate things, and the gaps say so. Bars that touch mean a histogram, which is for quantitative data, and that is a different graph entirely.

</details>

### The pie chart formula

A pie chart shows each category's **share of the whole**, so a slice has to be sized by relative frequency, not by count.

> **Slice angle = (f ÷ n) × 360°**
>
> and equivalently, **slice as a percentage of the total area = 100rf**

**Your turn.** Calculate all six slice angles, to one decimal place. Then apply the self-check: what must they total?

<details>
<summary><strong>Reveal</strong></summary>

| Hospital | *f* | *rf* = f ÷ 300 | Angle = rf × 360° |
|---|---|---|---|
| St Mary's | 84 | 0.280 | 0.280 × 360 = **100.8°** |
| Riverside | 71 | 0.237 | 0.237 × 360 = **85.2°** |
| Northgate | 52 | 0.173 | 0.173 × 360 = **62.4°** |
| Parkview | 45 | 0.150 | 0.150 × 360 = **54.0°** |
| Eastwood | 30 | 0.100 | 0.100 × 360 = **36.0°** |
| Hillcrest | 18 | 0.060 | 0.060 × 360 = **21.6°** |
| **Total** | **300** | **1.000** | **360.0°** |

**The self-check: the angles must total 360°.** This is the same check as Σ*rf* = 1 from last session, wearing a different hat — because 360° *is* the whole, just as 1 is.

</details>

### From table to graph

Here is the same data three ways. Look at what stays the same and what changes.

![Bar chart of surveyed patients by hospital](figures/bar-hospital.svg)

*Bar chart — **height** encodes the count.*

![Pie chart of surveyed patients by hospital with slice angles](figures/pie-hospital.svg)

*Pie chart — **area** encodes the share.*

Notice the colour: St Mary's is the same blue in both, so your eye can follow one hospital across the two pictures. Nothing has been added or lost between the table and these graphs. The same six numbers are simply re-encoded — first as height, then as area.

**Your turn.** Two questions. Decide which graph you would use for each, and why.

1. *"Did more than half our patients come from a single hospital?"*
2. *"How many more patients did Northgate see than Parkview?"*

<details>
<summary><strong>Reveal</strong></summary>

1. **The pie chart.** The question is about a share of the whole, and "more than half the circle" is something you can see instantly without doing any arithmetic. (The answer is no — St Mary's is the biggest slice at 28.0%, nowhere near half.)

2. **The bar chart.** The eye judges *length* accurately but judges *area* and *angle* badly. Northgate's 52 and Parkview's 45 are close enough that the two slices look almost identical, but the difference in bar height is easy to read.

**The general principle:** pie charts are for part-to-whole at a glance. They are poor whenever you need to compare categories that are close in size, and they become unreadable past about six slices.

</details>

### The comparison trap

This is the part of this topic that actually gets examined.

> The **previous** year, the same network surveyed **200** patients:
>
> **St Mary's 70 · Riverside 40 · Northgate 30 · Parkview 30 · Eastwood 20 · Hillcrest 10**

**Your turn.** Did St Mary's handle **more** or **fewer** of the surveyed patients this year than last? Commit to an answer before revealing.

<details>
<summary><strong>Reveal</strong></summary>

Most people say **more**, because 84 is bigger than 70. Now look at the sample sizes: **200** patients last year, **300** this year.

| Hospital | Last year *f* (n=200) | Last year % | This year *f* (n=300) | This year % |
|---|---|---|---|---|
| St Mary's | 70 | 35.0% | 84 | **28.0%** |
| Riverside | 40 | 20.0% | 71 | 23.7% |
| Northgate | 30 | 15.0% | 52 | 17.3% |
| Parkview | 30 | 15.0% | 45 | 15.0% |
| Eastwood | 20 | 10.0% | 30 | 10.0% |
| Hillcrest | 10 | 5.0% | 18 | 6.0% |
| **Total** | **200** | **100%** | **300** | **100%** |

St Mary's count went **up** (70 → 84) while its share went **down** (35.0% → 28.0%). Both statements are true, and they point in opposite directions.

**The rule — write this down:**

> When two data sets have **different totals**, compare **relative frequencies**, never raw counts.

A bar chart of raw counts across two groups of different size is misleading, and noticing that is worth marks. The reason is that a raw count mixes up two different things: a change in the variable, and a change in how many people you asked.

</details>

---

## Part 4 — The commute times, in pictures

More of Session 1's data. The commute study measured journey time; here are 25 of those journeys.

> Journey times to school, in minutes, for 25 randomly chosen Lincoln High students:
>
> ```
> 8   9  10  11  12  12  13  14  15  15
> 16  17  18  18  20  21  22  24  25  27
> 30  33  36  42  68
> ```

They are already sorted. Sorting is not the skill being tested today.

### Build all three

**Your turn.** On paper, construct all three of these. Give yourself about six minutes. Do not reveal until all three are drawn.

1. A **dotplot** — one dot per value, stacked where values repeat.
2. A **stem-and-leaf plot** — stems are the tens digit, leaves the units, both in order.
3. A **histogram** with bins of width 10.

<details>
<summary><strong>Reveal — the dotplot</strong></summary>

![Dotplot of 25 journey times in minutes](figures/dotplot-commute.svg)

Every one of the 25 values is still visible as its own dot. Two dots stack above 12 and above 15 and above 18, because two students had each of those times.

This is the display that makes the **outlier** and the **gap** unmissable: 68 sits on its own, with nothing at all between 42 and 68.

</details>

<details>
<summary><strong>Reveal — the stem-and-leaf plot</strong></summary>

```
0 | 8 9
1 | 0 1 2 2 3 4 5 5 6 7 8 8
2 | 0 1 2 4 5 7
3 | 0 3 6
4 | 2
5 |
6 | 8
```

**Check your `5 |` row.** If you left it out because there are no values in the fifties, go back and put it in.

That blank row *is* the gap. A stemplot that skips its unused stems has destroyed exactly the information it exists to show — and an examiner reading it would have no way to see that nothing lies between 42 and 68.

</details>

<details>
<summary><strong>Reveal — the histogram</strong></summary>

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

![Histogram of journey times, bin width 10](figures/hist-width10.svg)

Two things to check on your drawing:

- **The bars touch.** Unlike a bar chart, a histogram runs along a continuous number line, so there are no gaps between adjacent bins — except where a bin is genuinely empty, like 50–60 here.
- **Your frequencies total 25.** Same self-check as always: Σ*f* = *n*.

If a value landed on a boundary — say a journey of exactly 20 minutes — the convention is that it goes in the **upper** bin, which is why these are written "20 – under 30".

</details>

### The bin width formula

When a question tells you how many bins to use, you have to work out how wide they are:

> **bin width = (maximum − minimum) ÷ number of bins**

For this data, with 6 bins: (68 − 8) ÷ 6 = **10**.

### Which display for which question?

**Your turn.** Three questions. Which of your three drawings answers each one best, and why?

1. *"What was the exact longest journey?"*
2. *"Roughly what does the overall shape look like?"*
3. *"Is there a journey far away from all the others?"*

<details>
<summary><strong>Reveal</strong></summary>

1. **The stemplot or the dotplot.** Both keep every individual value — you can read 68 straight off. The histogram has thrown the individual values away; all it can tell you is that one journey was somewhere between 60 and 70 minutes.

2. **The histogram.** Grouping into bins smooths out the noise and makes the single peak obvious. A dotplot of 250 values would be an unreadable smear; a histogram of 250 values still shows the shape.

3. **The dotplot or the stemplot.** The isolated dot and the empty stem row show the gap directly.

**The trade-off, in one sentence:** histograms give up individual values in exchange for a clearer shape; dotplots and stemplots keep every value but stop working when *n* gets large.

</details>

### The same data, different bins

**Your turn.** Before revealing: if you redrew that histogram with bins of width **5** instead of 10, would it look the same?

<details>
<summary><strong>Reveal</strong></summary>

**No** — and the AP course description says so explicitly, which makes it fair game in an exam.

| Interval | *f* | | Interval | *f* |
|---|---|---|---|---|
| 5 – under 10 | 2 | | 30 – under 35 | 2 |
| 10 – under 15 | 6 | | 35 – under 40 | 1 |
| 15 – under 20 | 6 | | 40 – under 45 | 1 |
| 20 – under 25 | 4 | | 45 – under 65 | 0 |
| 25 – under 30 | 2 | | 65 – under 70 | 1 |

![Histogram of journey times, bin width 5](figures/hist-width5.svg)

Compare it with the width-10 version above. **Both are drawn on the same vertical scale**, so the comparison is fair — the width-5 bars really are shorter, because each bin now catches about half as many journeys.

At width 10 there is one obvious tall bar and a clear single peak. At width 5 that peak has split into two equal bars of 6, and the distribution looks flatter — almost as though it had two peaks rather than one.

**Neither picture is wrong.** A histogram is a *choice*, and the choice affects the story it tells. This is exactly why an exam question asks you to describe the **shape** rather than to trust one particular picture.

</details>

---

## Part 5 — Describing a distribution

The most important part of the session. Everything before this was construction; this is interpretation, and interpretation is where the marks are.

### The four components

A full description of a distribution needs **four** things, and it must be **in context**:

> **Shape · Centre · Variability (spread) · Unusual features**

Miss one and you lose the mark. The commonest failure in Unit 1 is describing shape and centre, feeling finished, and stopping.

Many textbooks compress this into the mnemonic **SOCS** — *shape, outliers, centre, spread*. It is the same four components in a different order; use whichever you will remember.

### Shape: the word people get backwards

The vocabulary:

- **Skewed right** (positively skewed) — the right tail, toward larger values, is longer.
- **Skewed left** (negatively skewed) — the left tail, toward smaller values, is longer.
- **Approximately symmetric** — the left half is roughly a mirror image of the right.
- **Unimodal** — one main peak. **Bimodal** — two prominent peaks. **Approximately uniform** — frequencies all roughly equal, no prominent peak.

**Your turn.** Look at your histogram of the journey times. Which tail is longer — the left or the right? So which way is it skewed?

<details>
<summary><strong>Reveal</strong></summary>

The **right** tail is longer: the bulk of journeys sit between 10 and 20 minutes, but the data stretches out to 30, 33, 36, 42 and finally 68.

So the distribution is **skewed right**, and **unimodal**.

If you answered "skewed left" because the tall bars are on the left, you have just made the single most common error in this unit:

![Skewed right versus skewed left, tails labelled](figures/skew-compare.svg)

**Skew is named for the tail, not for the bulk.** In both pictures above, the bulk sits on the opposite side from the tail. The left picture — bulk on the left, tail reaching right — is skewed *right*.

The physical trick that works: put a finger on the long thin tail and say out loud which direction it points. That is the name.

</details>

### The other three components

- **Centre** — roughly where the bulk sits. You can count to the middle value off a stemplot: with 25 values, the middle one is the 13th, which is **18 minutes**. *(Calculating the mean and median properly is Session 3.)*
- **Variability (spread)** — how far the values reach. Here, from **8 to 68 minutes**.
- **Unusual features** — an **outlier** is a value unusually small or large relative to the rest; a **gap** is a region with no data at all; a **cluster** is a concentration of values, usually separated by gaps.

Here there is an **outlier at 68 minutes** and a **gap between 42 and 68**.

> A note on honesty: there is a formal arithmetic test for outliers — the 1.5 × IQR rule — and it arrives in Session 3. For now, "unusually large relative to the rest" is the course's own definition and is entirely sufficient.

### Write the whole thing

**Your turn.** Write a complete description of the journey-time distribution. All four components, in context. Aim for three or four sentences. Do this properly before revealing — this is the exact task the exam sets.

<details>
<summary><strong>Reveal — model answer and checklist</strong></summary>

> *"The distribution of journey times for these 25 students is **skewed right** and **unimodal**, with one main peak between 10 and 20 minutes. The **centre** is about 18 minutes. Journey times **range from 8 to 68 minutes**. There is an **outlier at 68 minutes**, separated from the rest of the data by a **gap** between 42 and 68 — this student's journey took far longer than anyone else's."*

Mark your own against this:

- [ ] **Shape** — named the skew direction, and said unimodal
- [ ] **Centre** — gave a number, about 18 minutes
- [ ] **Variability** — gave the range, 8 to 68
- [ ] **Unusual features** — named the outlier *and* the gap
- [ ] **In context** — used the words "journey times", "minutes", "students"

**That last box is not decoration.** A description reading "skewed right and unimodal with an outlier" is statistically perfect and will still lose the interpretation mark, because it never says what the numbers are *about*. Name the variable, its units, and the individuals — every single time.

</details>

### Justifying a claim

**Your turn.** A parent says: *"A typical journey to this school takes about half an hour."* Does the data support that? Write a full answer.

<details>
<summary><strong>Reveal</strong></summary>

**No.** The centre is about 18 minutes, not 30. Only five of the 25 journeys took 30 minutes or more.

What has probably happened is that the parent is thinking of the long right tail — the journeys of 30, 33, 36, 42 and 68 minutes — which are memorable but are the minority.

A supportable version of the claim:

> *"Most journeys take under 20 minutes, though a small number take considerably longer, up to 68 minutes."*

This is the same four-step template you met in Session 1, and you will use it in every unit from here to the exam:

> **State the claim · quote the number · say what the number does and does not establish · keep it in context.**

</details>

---

## Part 6 — On your own: the café

No hints, no reveals, until all four are done. Write full answers.

> A café recorded the number of drinks sold per hour over 20 opening hours:
>
> ```
> 14  16  17  19  20  21  21  22  23  24
> 24  25  26  27  28  30  31  33  35  52
> ```

1. Construct a stem-and-leaf plot using tens as stems.
2. Construct a frequency table with bins of width 10, starting at 10.
3. Describe the distribution — all four components, in context.
4. The manager claims: *"We usually sell over 30 drinks an hour."* Is that supported? Justify.

<details>
<summary><strong>Reveal</strong></summary>

**1. Stemplot.**

```
1 | 4 6 7 9
2 | 0 1 1 2 3 4 4 5 6 7 8
3 | 0 1 3 5
4 |
5 | 2
```

Did you keep the empty `4 |` row? It is what shows the gap between 35 and 52.

**2. Frequency table.**

| Interval | Frequency |
|---|---|
| 10 – under 20 | 4 |
| 20 – under 30 | 11 |
| 30 – under 40 | 4 |
| 40 – under 50 | 0 |
| 50 – under 60 | 1 |
| **Total** | **20** |

**3. Description.** *"The distribution of drinks sold per hour over these 20 hours is skewed right and unimodal, with one main peak in the twenties. The centre is about 24 drinks per hour — with 20 values the middle is halfway between the 10th and 11th, both 24. Sales range from 14 to 52 drinks per hour. There is an outlier at 52, separated from the rest by a gap between 35 and 52."*

**4. The claim is not supported.** The centre is about 24 drinks per hour, and only **4 of the 20 hours** sold more than 30 — that is 31, 33, 35 and 52, or 20% of hours. "Usually" would need more than half. A supportable version: *"Sales are usually in the twenties per hour, with one unusually busy hour of 52."*

**Check yourself against the three classic slips:**

- Did you describe shape and centre and then stop? All four components, always.
- Did you call it "skewed left" because the bars are tall on the left? Skew is named for the tail.
- Did you drop the empty `4 |` stem?

</details>

---

## Part 7 — Explain it back

**Your turn.** Close the booklet. Describe the café distribution out loud — or write it — as if to somebody who cannot see the graph. Stop yourself the moment you miss one of the four components.

Saying it aloud rather than writing it is deliberate. It exposes whether the four components have become a habit or are still a checklist you have to go and look up. In an exam you will not have the checklist.

If it came out fluently, this session has landed. If it didn't, tell your tutor at the start of the next session — "I can build the graphs but the description doesn't come out in the right order" is far more useful to them than "it was fine".

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

**D3.** If you wanted exactly 7 bins, what bin width would you use? **State the formula and substitute.** (2)

**D4.** A student says the `1 | 2` row should be deleted because it only has one value. Explain why they are wrong. (1)

## Part E — Describing a distribution (8 marks)

Using the test-score data from Part D:

**E1.** Describe the distribution. Your answer must cover **all four components** and be **in context**. (5)

**E2.** A teacher claims: *"Most of the class scored below 40."* Using your displays, justify whether this claim is supported. (3)

---
---

# Answer key

*Open only after attempting everything.*

### Part A (6 marks, 1 each)

1–C · 2–F · 3–D · 4–A · 5–B · 6–E

### Part B (10 marks)

**B1–B2.** (7) Formulas: rf = f ÷ n · 100rf = (f ÷ n) × 100 · angle = (f ÷ n) × 360°, with n = 250.

| Section | *f* | *rf* | *100rf* | Angle |
|---|---|---|---|---|
| Fiction | 100 | 100 ÷ 250 = 0.400 | 40.0% | 144.0° |
| Non-fiction | 65 | 65 ÷ 250 = 0.260 | 26.0% | 93.6° |
| Reference | 40 | 40 ÷ 250 = 0.160 | 16.0% | 57.6° |
| Periodicals | 30 | 30 ÷ 250 = 0.120 | 12.0% | 43.2° |
| Other | 15 | 15 ÷ 250 = 0.060 | 6.0% | 21.6° |
| **Total** | **250** | **1.000** | **100%** | **360.0°** |

**B3.** (1) 144.0 + 93.6 + 57.6 + 43.2 + 21.6 = **360.0°** ✓

**B4.** (2) Bars of height 0.400, 0.260, 0.160, 0.120, 0.060, with **both axes labelled** — one of the two marks is for the labels. The bars must **not touch**: this is categorical data, not a histogram.

### Part C (6 marks)

**C1.** (4)
Fiction last term: 96 ÷ 200 = **48.0%** (1)
Fiction this term: 100 ÷ 250 = **40.0%** (1)
The comparison is misleading because the two terms had different totals — 200 books against 250. (1) Fiction's raw count rose by 4, but its **share of all borrowing fell from 48.0% to 40.0%**. Relative to everything else being borrowed, fiction became *less* popular, not more. (1)

**C2.** (2) When two data sets have different totals, compare **relative frequencies or percentages**, not raw counts. (1) A raw count confuses a change in the variable with a change in the overall total. (1)

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

**E1.** (5) One mark each for shape, centre, variability, unusual features, and context.

> *"The distribution of test scores for these 24 students is **skewed left** and **unimodal**, with one main peak in the 40s. The **centre** is about 40 marks. Scores **range from 12 to 47** out of 50. There is an **outlier at 12**, separated from the rest of the data by a **gap** between 12 and 24 — one student scored far below everyone else."*

"Negatively skewed" is accepted for skewed left.

> **The most common error here is "skewed right".** The bulk of the data sits on the right, in the 40s — but the *tail* stretches left, down to 12. Skew is named for the tail. If you got this wrong, flag it: it costs a mark every time it appears, and it will appear again.

**E2.** (3) The claim is **not** supported. (1) From the frequency table, only 1 + 2 + 8 = **11 of 24** students scored below 40, which is 11 ÷ 24 = 45.8% — fewer than half. (1) A supportable version: *"Slightly fewer than half the class scored below 40, and the single most common band was 40–49."* (1)

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

Every term carries an example. This is the page to revise from.

### Displays for one categorical variable

**Bar chart (bar graph)** — one bar per category; the height or length shows the frequency **or** relative frequency. Bars do **not** touch.
*Example: six bars, one per hospital; the St Mary's bar reaches 84, or 0.280 on a relative frequency scale.*

**Pie chart** — one slice per category; each slice's area as a fraction of the whole equals that category's relative frequency. The slices total 1, or 100% of the area.
*Example: the St Mary's slice takes up 28.0% of the circle — an angle of 100.8°.*

### Displays for one quantitative variable

All three keep the natural ordering of the values, smallest to largest.

**Dotplot** — one dot per value, placed above its position on the axis; near-identical values stack.
*Example: two dots stacked above 12, because two students had 12-minute journeys.*

**Stem-and-leaf plot** — each value splits into a **stem** (the leading digit or digits) and a **leaf** (usually the final digit). Stems and leaves are both ordered smallest to largest.
*Example: 18 becomes stem 1, leaf 8. Keep empty stems — a blank row is a gap in the data.*

**Histogram** — values grouped into ordered intervals (**bins**); each bar's height is the frequency or relative frequency in that bin. Bars **touch**, because the scale is continuous.
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

**Shape — skewed right (positive)** — the right tail, toward larger values, is longer.
*Example: journey times — most under 20 minutes, stretching out to 68.*

**Shape — skewed left (negative)** — the left tail, toward smaller values, is longer.
*Example: test scores — most in the 40s, stretching down to 12.*

**Shape — symmetric and peaks** — approximately symmetric if the left half mirrors the right. **Unimodal** = one main peak; **bimodal** = two; **approximately uniform** = frequencies roughly equal.
*Example: the commute data is unimodal, peaking between 10 and 20 minutes.*

**Centre** — roughly where the bulk sits.
*Example: about 18 minutes.*

**Variability (spread)** — how far the values reach.
*Example: from 8 to 68 minutes.*

**Unusual features** — an **outlier** is unusually small or large relative to the rest; a **gap** is a region with no observed data; a **cluster** is a concentration of values, usually separated by gaps.
*Example: the 68-minute journey is an outlier; nothing lies between 42 and 68, so that is a gap.*

> **Skew is named for the tail, not the bulk.** Put a finger on the long thin tail and say its direction out loud. This single error costs more marks in Unit 1 than anything else.

> **In context** means naming the variable, its units and the individuals — every time. Not "skewed right with an outlier", but "journey times for these 25 students are skewed right, with one student's journey of 68 minutes far longer than anyone else's."

Many textbooks use the mnemonic **SOCS** — shape, outliers, centre, spread. It is the same four components the course description lists as shape, centre, variability and unusual features.

---

*CED references: Topic 1.4 (1.4.A.1–2, 1.4.B.1, 1.4.C.1), Topic 1.5 (1.5.A.1–4), Topic 1.6 (1.6.A.1–6, 1.6.B.1). Course and Exam Description effective Fall 2026.*

*Further reading: Barron's pdf 83–96 · Princeton Review 105–124 · 5 Steps to a 5 60–65.*

*Next session: Topics 1.7–1.9 — mean, median, standard deviation, the 1.5 × IQR outlier rule, boxplots, and comparing two distributions. The formal outlier test promised above arrives there.*
