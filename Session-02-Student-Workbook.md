# Session 2 — Shape of the Data: Showing and Describing One Variable

**AP Statistics · Twenty-Hour Course · Student edition, to work through on your own**
**CED Topics 1.4, 1.5, 1.6 · About 105 minutes, plus homework**

---

## How to use this

Same rule as last time, and it matters more in this session than it did in the last one.

> Every **Your turn** box asks you to do something before the text shows you the answer. **Do it on paper first.** Several of these ask you to *draw* a graph — and the finished graph is hidden behind the reveal precisely so that you cannot copy it.

Drawing a histogram by looking at a histogram teaches you nothing. Drawing one from a list of 25 numbers, getting a bin boundary wrong, and finding out where you went wrong — that is the whole exercise.

**The one exception is Part 3, the theory.** Read it in full, with nothing hidden, before you start on any data. Every task after it uses something Part 3 states, and says which subsection to look back at.

**What you need:** paper, a pen, a ruler, and a protractor. Squared paper helps but is not essential. No calculator today.

### How this maps to your tutor's document

| Your section | Tutor's section | Minutes |
|---|---|---|
| Part 1 — Your Session 1 homework, and a warm-up | 0–8 Homework debrief and diagnostic | 10 |
| Part 2 — Why this matters | (the framing) | 2 |
| Part 3 — Theory: graphs and descriptions for one variable | 8–30 Theory | 28 |
| Part 4 — The hospital survey, in pictures | 30–40 Scenario A | 13 |
| Part 5 — Build & Defend: the commute times in three displays | 40–54 Activity | 18 |
| Part 6 — Describing the commute distribution | 54–68 Scenario B | 18 |
| Part 7 — On your own: the café | 68–76 Solo case | 10 |
| Part 8 — Explain it back | 76–82 Teach it back | 6 |
| **Total** | **82 minutes with a tutor** | **105** |

Working alone with a pen is slower than working with a tutor, so this takes about a quarter longer than the tutor's 82 minutes. Take the time; skipping the writing is what makes the session not work.

---

## Part 1 — Your Session 1 homework, and a warm-up

Before anything else, get out your marked Session 1 homework and make two lists:

1. The questions you got **wrong**.
2. The questions you marked with a **?** — including the ones that turned out right.

That second list is the more useful one. A question you guessed correctly is a question you will get wrong under exam pressure.

**Two specific things to check.** These are the two most common errors on that sheet, and both come back repeatedly:

- **B5** — did you answer *"parameter"*? The value 171 ÷ 450 came from the 450 people actually asked, so it describes the **sample**. It is a statistic. Check the denominator, every time.
- **D4** — did you answer *"yes, supported"*? Bus was 42.5%, which is the **largest** share but not **most**. "Most" means more than half. This plurality-versus-majority distinction appears in every unit of this course, and it comes back today.

### Warm-up: three questions

:::yourturn
Answer on paper before revealing.

1. Give me a categorical variable and a quantitative variable, from anything at all.
2. If I have a table of counts for six hospitals, what could I draw?
3. What does a histogram show you that a plain list of numbers doesn't?
:::

:::reveal Reveal — the answers, and what yours mean
**Q1.** Anything valid. Travel mode and journey time; eye colour and height; membership type and number of visits.

**Q2.** A bar chart or a pie chart. Both are for a single categorical variable.

**Q3.** This is the question that matters. The answer you want is something about **shape** or **pattern** — a histogram lets you see at a glance whether the values pile up at one end, whether there is a single peak, whether anything sits far away from everything else.

If your answer was only *"it's easier to read"* or *"it looks nicer"*, that is exactly the gap this session fills. A graph is not decoration for a list of numbers; it shows you a property of the data — its shape — that the list contains but hides.

| If you said | It means | What to do |
|---|---|---|
| Q1: a correct pair | Session 1's variable types are secure | Read Part 3 at a normal pace |
| Q1: a number-coded category as quantitative, such as a postcode | The categorical/quantitative line is not secure | Ask of each variable: would an average of it mean anything? If not, it is categorical |
| Q2: a bar chart or a pie chart | Ready for topic 1.4 | Carry on |
| Q2: a histogram | Categorical and quantitative displays are merged | Read *Bar charts* and *Histograms and bins* in Part 3 side by side |
| Q3: shape, pattern, where values pile up | The idea of a distribution is there | Carry on |
| Q3: "easier to read" | A graph is being treated as decoration | Spend longest on *The four components of a description* in Part 3 |
:::

---

## Part 2 — Why this matters

This session has two halves, and they are not equally important.

The first half is **construction**: turning a table into a bar chart, a pie chart, a dotplot, a stemplot, a histogram. This is genuinely a five-minute skill once you have the formulas.

The second half is **description**: saying what a distribution looks like in a way that earns marks. Students still get this wrong in April, because a full description requires **four** specific things, in context, and most people say two of them and stop.

Part 3 states every idea before you use it. Part 6 is where the marks are, so give it your full attention.

---

## Part 3 — Theory: graphs and descriptions for one variable

Read this part straight through. Nothing is hidden, and there is nothing to write until the checks at the end. Parts 4 to 7 apply these subsections, one at a time, to data.

Two things are retrieved from Session 1 rather than taught again: the frequency *f* of a category, its relative frequency and its percentage; and what **in context** means (1.1.A.6), which is naming the variable, its units and the individuals the numbers are about.

:::formula
rf = f ÷ n  ·  100rf = (f ÷ n) × 100  (f = a category's count, n = the total count)
:::

### Bar charts (1.4.A)

A **bar chart**, also called a **bar graph**, displays the frequencies (counts) or the relative frequencies (proportions) for the categories of one categorical variable. Each bar represents one category, and the **height or length** of the bar corresponds to the frequency or relative frequency of the observational units in that category (1.4.A.1).

**What it does and does not say.** Switching from frequency to relative frequency changes the numbers on the axis and nothing else, because every bar is divided by the same *n*. The bars are drawn apart, because categories are separate things with no position on a number line; bars that touch belong to a histogram, which is for a quantitative variable. The course description fixes no order for the categories. The eye judges length accurately, which makes the bar chart the display for comparing one category with another.

*Illustration: three categories with counts 6, 3 and 1 (n = 10) give bars of 6, 3 and 1 on a frequency axis, or 0.6, 0.3 and 0.1 on a relative-frequency axis. Same bars, different scale.*

### Pie charts and the slice angle (1.4.A)

A **pie chart** displays frequencies or relative frequencies for categorical data. Each slice represents one category. The **area** of each slice, as a fraction of the total area, corresponds to the relative frequency of that category, so the slices' areas together equal 1, or 100% of the total area (1.4.A.2).

:::formula
slice angle = (f ÷ n) × 360°  ·  slice share of the area = 100rf
:::

Here *f* is the category's frequency, *n* the total and 360° the whole circle.

**What it does and does not say.** The slices must be the parts of **one whole**: if the categories do not add up to a single total, there is no pie to draw. Work each angle from *f* ÷ *n*, not from a relative frequency already rounded to three decimals, which can be out by a tenth of a degree. The angles must total 360°; that is the same check as Σrf = 1, because 360° is the whole just as 1 is. The eye judges area and angle poorly, so a pie chart is good for part-to-whole questions ("is this more than half?") and poor for comparing two slices of similar size.

*Illustration: a category with f = 5 out of n = 20 has rf = 0.25 and a slice angle of 0.25 × 360° = 90°, a quarter of the circle.*

### Justifying a claim from a categorical graph (1.4.B)

Graphical representations of a categorical variable reveal information that can be used to justify claims about the variable **in context** (1.4.B.1). A justification quotes the number the graph shows and says what it does and does not establish.

**What it does and does not say.** Choose the display that answers the question asked: a share of the whole is read from a pie chart, a comparison between two categories from a bar chart. The largest category is not automatically "most": most means **more than half**, the plurality-versus-majority distinction from Session 1.

*Illustration: if the largest slice is 0.4 of the circle, "this is the most common category" is supported, but "most units are in this category" is not, because 0.4 is less than half.*

### Comparing data sets with different totals (1.4.C)

Frequency and relative frequency tables, bar charts and pie charts can be used to compare two or more data sets in terms of the **same categorical variable** (1.4.C.1).

**The rule.** When the data sets have different totals, compare **relative frequencies** (or percentages), never raw counts. A raw count mixes two changes together: a change in the variable, and a change in how many units there were altogether. A bar chart of counts for two groups of different size is therefore misleading, and saying so is worth marks. When the totals are equal, counts and relative frequencies give the same comparison.

*Illustration: a category holds 3 of 10 units in one data set and 4 of 20 in another. Its count rose from 3 to 4; its share fell from 0.30 to 0.20.*

### What every quantitative display shows (1.5.A.1)

Histograms, stem-and-leaf plots and dotplots give a visual representation of the **distribution** of a quantitative variable: which values occur, and how often. They show the frequency or relative frequency of the values, or of intervals of values, and they keep the **natural ordering** of the variable, smallest to largest (1.5.A.1).

**What it does and does not say.** The three displays differ in what they keep. A dotplot and a stem-and-leaf plot keep **every individual value**, so an exact value can be read off, but they become unreadable when *n* is large. A histogram gives up the individual values in exchange for a clearer view of the **shape**, and it works for any *n*. None of the three is for a categorical variable.

*Illustration: for the values 2, 2, 3, 7, all three displays put 2 before 3 before 7, and all three show that 2 occurs twice.*

### Dotplots (1.5.A.4)

A **dotplot** represents each value by a dot, placed above the horizontal axis (or beside the vertical axis) at that value, with nearly identical values **stacked** on top of each other (1.5.A.4).

**What it does and does not say.** Every value is visible, so gaps and isolated values are obvious, provided the axis is evenly scaled across the whole range, including the stretches where there is no data. Squeezing out an empty stretch of axis hides the gap. With hundreds of values a dotplot becomes a smear.

*Illustration: for 1, 3, 3, 4, 9 there is one dot at 1, two stacked at 3, one at 4, empty axis from 5 to 8, and one dot at 9.*

### Stem-and-leaf plots (1.5.A.3)

A **stem-and-leaf plot** splits each value into two parts: a **stem** (the first digit or digits) and a **leaf** (usually the single digit after the stem). Both stems and leaves are ordered from smallest to largest (1.5.A.3). It is often shortened to *stemplot*; the course description always writes the full name.

**What it does and does not say.** Every stem between the smallest and the largest is written, **even when it has no leaves**. An empty row is a gap in the data; a stemplot that skips it has destroyed the spacing it exists to show. Every value survives and can be read back: stem 1, leaf 8 is 18.

*Illustration: 7, 12, 15 and 31, with tens as stems. The empty 2 row is what shows that nothing lies between 15 and 31.*

```
0 | 7
1 | 2 5
2 |
3 | 1
```

### Histograms and bins (1.5.A.2)

A **histogram** places the observed values into ordered intervals, called **bins**, along the horizontal axis. Each bar represents one bin, and its height shows the frequency or relative frequency of the observations in that interval (1.5.A.2). It can also be drawn with the bins on the vertical axis and the bars running horizontally (1.5.A.2).

**Conventions.** Bins have equal width and are written "10 – under 20": a value exactly on a boundary goes in the **upper** bin. Adjacent bars **touch**, because the axis is a continuous number line; the only space between bars is a bin that is genuinely empty. The bin frequencies total *n*, and the relative frequencies total 1.

When a question fixes the number of bins, this working rule gives their width:

:::formula
bin width = (maximum − minimum) ÷ number of bins
:::

**What it does and does not say.** The rule is a construction aid; the course description gives no formula for bin width. Round the answer to a convenient width and start the first bin at or just below the minimum. Because "under" excludes the top boundary, a maximum that lands exactly on the last boundary, or a first bin that starts below the minimum, needs one more bin than the rule assumed.

*Illustration: 3, 4, 9, 10 and 12, with bins of width 5 starting at 0, give 0 – under 5: 2; 5 – under 10: 1; 10 – under 15: 2. The 10 sits on a boundary, so it goes in the upper bin. The total is 5.*

### Bin width changes the appearance (1.5.A.2)

Altering the bin widths can change the appearance of the histogram (1.5.A.2). Narrow bins show more detail and more noise; wide bins show the overall shape but can hide gaps and small clusters.

**What it does and does not say.** Neither picture is wrong: a histogram is a **choice**. What an exam rewards is a description of the features that survive every sensible width, such as the direction of skew, the main peak and a value far from the rest, not a reading of one bar's height. Two histograms can only be compared fairly on the **same vertical scale**.

*Illustration: the values 1, 2, 6, 7 with width 2 from 0 give bars of 1, 1, 0, 2, with a visible gap; with width 4 from 0 they give 2, 2, and the gap has disappeared.*

### The four components of a description (1.6.A.1)

A description of the distribution of one quantitative variable includes **shape**, **center** and **variability (spread)**, as well as any **unusual features** such as outliers, gaps or clusters, **in context** (1.6.A.1).

**What it does and does not say.** All four, every time. The course description itself names the acronym **SOCS** (Shape, Outliers/Gaps, Center, Spread) and warns that students recite it and then leave out the unusual features; it is the same four components in a different order. The commonest lost mark in Unit 1 is describing shape and centre and stopping. The second is a description in which every statistical word is correct but nothing says what was measured, in what units, or on whom: that loses the interpretation mark.

*Illustration: "skewed right, centre about 5, from 1 to 12, one outlier at 12" has all four components and no context. It becomes a full description only when it names the variable, its units and the individuals.*

### Shape: skew and symmetry (1.6.A.2)

A distribution is **skewed to the right** (positively skewed) if the right tail, toward larger values, is longer than the left. It is **skewed to the left** (negatively skewed) if the left tail, toward smaller values, is longer than the right. It is **approximately symmetric** if the left half is approximately the mirror image of the right half (1.6.A.2).

**What it does and does not say.** Skew is named for **where the tail points**, not where the bulk sits, and the bulk is always on the opposite side from the tail. Students reverse this constantly; putting a finger on the long thin tail and saying its direction out loud fixes it. "Approximately" symmetric is the realistic claim: real data never mirror exactly. Skew needs an ordered quantitative scale, so a bar chart of categories has no skew.

![Skewed right versus skewed left, tails labelled](figures/skew-compare.svg)

*The single most common error in Unit 1. In both pictures the bulk sits opposite the tail. Skew is named for the tail, so the left picture, bulk on the left and tail stretching right, is skewed right.*

### Shape: counting the peaks (1.6.A.3)

A distribution with one main peak is **unimodal**; one with two prominent peaks is **bimodal**. A distribution in which each frequency or relative frequency is approximately the same, with no prominent peaks, is **approximately uniform** (1.6.A.3). A peak is also called a **mode**, which is where *unimodal* and *bimodal* get their names.

**What it does and does not say.** Only *prominent* peaks count: a bar one or two higher than its neighbours is noise, not a second mode. The number of peaks you see can change with the bin width. A bimodal distribution often means two different groups have been mixed together, and then a single centre describes neither of them.

*Illustration: frequencies of 1, 5, 2, 1, 6, 1 across six bins are bimodal; frequencies of 4, 5, 4, 4, 5, 4 are approximately uniform.*

### Centre and variability, read from a graph (1.6.A.1)

Every description needs a **centre** (a typical value) and a **variability** (how spread out the values are). Topic 1.7, next session, gives the formal measures. Today the centre is read as the **middle value** of the ordered data, and the variability as the smallest and largest values, "from … to …", always with units.

:::formula
middle value of n ordered values: position (n + 1) ÷ 2  ·  when n is even, halfway between the (n ÷ 2)th and (n ÷ 2 + 1)th values
:::

**What it does and does not say.** This middle value is the **median**, which topic 1.7 defines formally in Session 3, along with the mean, the range and the standard deviation. The tallest bar of a histogram is the most common interval, not the centre; the two can differ, especially when the distribution is skewed. "From 2 to 20 minutes" describes the spread; it is not yet a single number.

*Illustration: for 2, 5, 7, 9, 20, n = 5, the middle is at position (5 + 1) ÷ 2 = 3, so the centre is 7, and the values run from 2 to 20. For 2, 5, 7, 9 the centre is halfway between 5 and 7, which is 6.*

### Unusual features: outliers, gaps and clusters (1.6.A.4–6)

**Outliers** are data points that are unusually small or large relative to the rest of the data (1.6.A.4). A **gap** is a region in a distribution between two values in which there are no observed data (1.6.A.5). **Clusters** are concentrations of values, usually separated by gaps (1.6.A.6).

**What it does and does not say.** In topic 1.6 an outlier is a judgement read from the graph, and that is the course description's own definition; the numerical tests (the 1.5 × IQR rule and the 2-standard-deviation rule) arrive with topic 1.8 in Session 3. A gap is a stretch with **no** values, not a bin with a low count. Say where each feature is, from which value to which.

*Illustration: in 1, 2, 2, 3, 9, 10, 10, 11, 30 there are two clusters (1 to 3 and 9 to 11), gaps from 3 to 9 and from 11 to 30, and 30 is an outlier.*

### Justifying a claim from a quantitative distribution (1.6.B)

Graphical representations of a quantitative variable may reveal information that can be used to justify claims about the variable **in context** (1.6.B.1). The template is Session 1's: **state the claim · quote the number · say what the number does and does not establish · keep it in context.** If the claim is not supported, give a version that is.

**What it does and does not say.** "Most" and "usually" mean more than half, so count the values on each side from the display rather than judging by eye. A long tail is memorable, and a claim built on it often describes a minority.

*Illustration: for 2, 3, 3, 4, 4, 5, 18, the claim "values are usually above 10" fails: only 1 of the 7 values is above 10, and the middle value is 4.*

### Check the theory before the data

Five short questions on made-up numbers. Answer each one on paper, then open its reveal.

**Check 1.** A bar chart and a histogram both have bars. Give two differences.

:::reveal Reveal — check 1
A bar chart is for a **categorical** variable and a histogram for a **quantitative** one. A bar chart's bars are **apart**, because categories are separate; a histogram's bars **touch**, because its axis is a number line. See *Bar charts (1.4.A)* and *Histograms and bins (1.5.A.2)*.
:::

**Check 2.** A category has 9 of 36 units. What is its slice angle?

:::reveal Reveal — check 2
(9 ÷ 36) × 360° = 0.25 × 360° = **90°**, a quarter of the circle.
:::

**Check 3.** Last year a category held 30 of 100 units; this year it holds 40 of 200. Did it grow?

:::reveal Reveal — check 3
Its **count** rose from 30 to 40, but its **share** fell from 30% to 20%. The totals differ, so the comparison that counts is the share: relative to the whole, it shrank. See *Comparing data sets with different totals (1.4.C)*.
:::

**Check 4.** The long tail of a distribution stretches toward the small values. What is its shape called?

:::reveal Reveal — check 4
**Skewed left.** If you said "skewed right", you named it for the bulk, which sits on the right. Skew is named for the tail.
:::

**Check 5.** What must every description of a distribution contain?

:::reveal Reveal — check 5
**Shape, centre, variability and unusual features, in context**: naming the variable, its units and the individuals.
:::

---

## Part 4 — The hospital survey, in pictures

This is the same data you tabulated in Session 1. Nothing new has been collected — you are only going to re-encode it.

> The same **300 surveyed patients**, by hospital:
> **St Mary's 84 · Riverside 71 · Northgate 52 · Parkview 45 · Eastwood 30 · Hillcrest 18**

### What does the height of a bar mean?

:::yourturn
Look back at *Bar charts (1.4.A)* if you need to. If you drew a bar chart of this, what would the height of the St Mary's bar be?
:::

:::reveal Reveal — the St Mary's bar
Either **84** or **0.280** — and both are right. That is the point.

As *Bar charts (1.4.A)* says, the height can show either the **frequency** (the count, 84) or the **relative frequency** (the proportion, 0.280). Switching between them changes nothing about the shape of the picture — only the numbers on the axis.

One rule that is easy to lose marks on: **the bars must not touch.** Categories are separate things, and the gaps say so. Bars that touch mean a histogram, which is for quantitative data, and that is a different graph entirely.
:::

### Slice angles for the six hospitals

A pie chart shows each category's **share of the whole**, so a slice has to be sized by relative frequency, not by count. Use the formula from *Pie charts and the slice angle (1.4.A)*.

:::yourturn
Calculate all six slice angles, to one decimal place, working each one from f ÷ 300 rather than from a rounded rf. Then apply the self-check: what must they total?
:::

:::reveal Reveal — the six slice angles
| Hospital | *f* | *rf* = f ÷ 300 | Angle = (f ÷ 300) × 360° |
|---|---|---|---|
| St Mary's | 84 | 0.280 | 84 ÷ 300 × 360 = **100.8°** |
| Riverside | 71 | 0.237 | 71 ÷ 300 × 360 = **85.2°** |
| Northgate | 52 | 0.173 | 52 ÷ 300 × 360 = **62.4°** |
| Parkview | 45 | 0.150 | 45 ÷ 300 × 360 = **54.0°** |
| Eastwood | 30 | 0.100 | 30 ÷ 300 × 360 = **36.0°** |
| Hillcrest | 18 | 0.060 | 18 ÷ 300 × 360 = **21.6°** |
| **Total** | **300** | **1.000** | **360.0°** |

**The self-check: the angles must total 360°.** This is the same check as Σrf = 1 from last session, wearing a different hat — because 360° *is* the whole, just as 1 is.

If you got 85.3° for Riverside or 62.3° for Northgate, you multiplied the rounded 0.237 or 0.173 by 360. The answer is a tenth out; carry the unrounded fraction into the angle.
:::

### From table to graph

Here is the same data three ways. Look at what stays the same and what changes.

![Table of surveyed patients by hospital with each hospital's chart colour](figures/s02-hospital-table.svg)

*The table — the counts, with every derived column the two graphs need. The colour chip ties each row to its bar and its slice.*

![Bar chart of surveyed patients by hospital](figures/bar-hospital.svg)

*Bar chart — **height** encodes the count.*

![Pie chart of surveyed patients by hospital with slice angles](figures/pie-hospital.svg)

*Pie chart — **area** encodes the share.*

Notice the colour: St Mary's is the same blue in the table and both graphs, so your eye can follow one hospital across all three. Nothing has been added or lost between the table and these graphs. The same six numbers are simply re-encoded — first as height, then as area.

:::yourturn
Two questions. Using *Justifying a claim from a categorical graph (1.4.B)*, decide which graph you would use for each, and why.

1. *"Did more than half our patients come from a single hospital?"*
2. *"How many more patients did Northgate see than Parkview?"*
:::

:::reveal Reveal — which graph for which question
1. **The pie chart.** The question is about a share of the whole, and "more than half the circle" is something you can see instantly without doing any arithmetic. (The answer is no — St Mary's is the biggest slice at 28.0%, nowhere near half.)
2. **The bar chart.** The eye judges *length* accurately but judges *area* and *angle* badly. Northgate's 52 and Parkview's 45 are close enough that the two slices look almost identical, but the difference in bar height is easy to read.

**The general principle:** pie charts are for part-to-whole at a glance. They are poor whenever you need to compare categories that are close in size, and they become unreadable past about six slices.
:::

### The comparison trap: last year against this year

This is the part of this topic that actually gets examined.

> The **previous** year, the same network surveyed **200** patients:
> **St Mary's 70 · Riverside 40 · Northgate 30 · Parkview 30 · Eastwood 20 · Hillcrest 10**

:::yourturn
Did St Mary's handle **more** or **fewer** of the surveyed patients this year than last? Commit to an answer before revealing.
:::

:::reveal Reveal — last year against this year
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

St Mary's count went **up** (70 → 84) while its share went **down** (35.0% → 28.0%). Both statements are true, and they point in opposite directions. The share that changed most was St Mary's, down 7.0 percentage points; Riverside rose 3.7, and everything else barely moved.

This is the rule from *Comparing data sets with different totals (1.4.C)* — write it down:

> When two data sets have **different totals**, compare **relative frequencies**, never raw counts.

A bar chart of raw counts across two groups of different size is misleading, and noticing that is worth marks. The reason is that a raw count mixes up two different things: a change in the variable, and a change in how many people you asked.
:::

---

## Part 5 — Build & Defend: the commute times in three displays

More of Session 1's data. The commute study measured journey time; here are 25 of those journeys. In a classroom this is a Gallery Walk, with a different group building each display; working alone, you build all three.

Journey times to school, in minutes, for 25 randomly chosen Lincoln High students:

```
 8   9  10  11  12  12  13  14  15  15
16  17  18  18  20  21  22  24  25  27
30  33  36  42  68
```

They are already sorted. Sorting is not the skill being tested today.

### Build all three displays

:::yourturn
On paper, construct all three of these, using *Dotplots (1.5.A.4)*, *Stem-and-leaf plots (1.5.A.3)* and *Histograms and bins (1.5.A.2)*. Give yourself about six minutes. Do not reveal until all three are drawn.

1. A **dotplot** — one dot per value, stacked where values repeat.
2. A **stem-and-leaf plot** — stems are the tens digit, leaves the units, both in order.
3. A **histogram** with bins of width 10.
:::

:::reveal Reveal — the dotplot
![Dotplot of 25 journey times in minutes](figures/dotplot-commute.svg)

*Every one of the 25 values is still visible as its own dot.*

Two dots stack above 12 and above 15 and above 18, because two students had each of those times.

This is the display that makes the **outlier** and the **gap** unmissable: 68 sits on its own, with nothing at all between 42 and 68.
:::

:::reveal Reveal — the stem-and-leaf plot
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
:::

:::reveal Reveal — the histogram
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

*Bin width 10 — one obvious peak between 10 and 20 minutes.*

Three things to check on your drawing:

- **The bars touch.** Unlike a bar chart, a histogram runs along a continuous number line, so there are no gaps between adjacent bins — except where a bin is genuinely empty, like 50–60 here.
- **Your frequencies total 25.** Same self-check as always: Σf = n.
- **Boundary values go up.** A journey of exactly 20 minutes goes in the upper bin, which is why these are written "20 – under 30".

The width of 10 is what the working rule gives for six bins: (68 − 8) ÷ 6 = **10**. The table has seven bins, not six, because it starts at the round boundary 0, below the minimum of 8 — the case *Histograms and bins (1.5.A.2)* warns about.
:::

### Which display for which question?

:::yourturn
Three questions. Which of your three drawings answers each one best, and why? *What every quantitative display shows (1.5.A.1)* is the subsection to use.

1. *"What was the exact longest journey?"*
2. *"Roughly what does the overall shape look like?"*
3. *"Is there a journey far away from all the others?"*
:::

:::reveal Reveal — the best display for each question
1. **The stemplot or the dotplot.** Both keep every individual value — you can read 68 straight off. The histogram has thrown the individual values away; all it can tell you is that one journey was somewhere between 60 and 70 minutes.
2. **The histogram.** Grouping into bins smooths out the noise and makes the single peak obvious. A dotplot of 250 values would be an unreadable smear; a histogram of 250 values still shows the shape.
3. **The dotplot or the stemplot.** The isolated dot and the empty stem row show the gap directly.

**The trade-off, in one sentence:** histograms give up individual values in exchange for a clearer shape; dotplots and stemplots keep every value but stop working when *n* gets large.
:::

### The same journeys with width-5 bins

:::yourturn
*Bin width changes the appearance (1.5.A.2)* says the picture can change. Before revealing: if you redrew your histogram with bins of width **5** instead of 10, what would happen to the single peak? Build the width-5 frequency table to find out.
:::

:::reveal Reveal — the width-5 histogram
It does not look the same — and the AP course description says so explicitly, which makes it fair game in an exam.

| Interval | *f* | | Interval | *f* |
|---|---|---|---|---|
| 5 – under 10 | 2 | | 30 – under 35 | 2 |
| 10 – under 15 | 6 | | 35 – under 40 | 1 |
| 15 – under 20 | 6 | | 40 – under 45 | 1 |
| 20 – under 25 | 4 | | 45 – under 65 | 0 |
| 25 – under 30 | 2 | | 65 – under 70 | 1 |
| Total | 25 | | | |

![Histogram of journey times, bin width 5](figures/hist-width5.svg)

*Bin width 5 — the same 25 journeys.*

Compare it with the width-10 version above. **Both are drawn on the same vertical scale**, so the comparison is fair — the width-5 bars really are shorter, because each bin now catches about half as many journeys.

At width 10 there is one obvious tall bar and a clear single peak. At width 5 that peak has split into two equal bars of 6, and the distribution looks flatter — almost as though it had two peaks rather than one.

**Neither picture is wrong.** A histogram is a *choice*, and the choice affects the story it tells. This is exactly why an exam question asks you to describe the **shape** rather than to trust one particular picture.
:::

:::sim unit1-explorer | Unit 1 Explorer: Bin Width | 760
Open the **Bin Width** tab (the explorer opens on Sample & Estimate). It holds the same journey times as above. Drag the width from 10 to 5, then to 2, and write down which features survive every width. Your list should include the right skew, the single main peak and the 68 far from the rest; the exact bar heights do not survive.
:::

---

## Part 6 — Describing the commute distribution

The most important part of the session. Everything before this was construction; this is interpretation, and interpretation is where the marks are.

You have the four components from *The four components of a description (1.6.A.1)*:

> **Shape · Centre · Variability (spread) · Unusual features**, in context

Miss one and you lose the mark. The commonest failure in Unit 1 is describing shape and centre, feeling finished, and stopping.

### Shape: which tail is longer?

:::yourturn
Look at your histogram of the journey times, and at the figure in *Shape: skew and symmetry (1.6.A.2)*. Which tail is longer — the left or the right? So which way is it skewed, and how many peaks does it have?
:::

:::reveal Reveal — the shape of the journeys
The **right** tail is longer: the bulk of journeys sit between 10 and 20 minutes, but the data stretches out to 30, 33, 36, 42 and finally 68.

So the distribution is **skewed right**, and **unimodal**.

If you answered "skewed left" because the tall bars are on the left, you have just made the single most common error in this unit. **Skew is named for the tail, not for the bulk.** Look again at the skew figure in Part 3: in both pictures the bulk sits on the opposite side from the tail.

The physical trick that works: put a finger on the long thin tail and say out loud which direction it points. That is the name.
:::

:::sim unit1-explorer | Unit 1 Explorer: Name That Shape | 760
Open the **Name That Shape** tab. It draws a new distribution each round and tells you whether you named it correctly. Keep going until you have a streak of eight; anything less means the direction is still guesswork.
:::

### Centre, spread and unusual features of the journeys

:::yourturn
Using *Centre and variability, read from a graph (1.6.A.1)* and *Unusual features: outliers, gaps and clusters (1.6.A.4–6)*, find three things from your stemplot: the centre, the spread, and any unusual features.
:::

:::reveal Reveal — centre, spread and unusual features
- **Centre** — with 25 values the middle is at position (25 + 1) ÷ 2 = 13. Counting to the 13th value on the stemplot gives **18 minutes**. *(Calculating the mean and median properly is Session 3.)*
- **Variability (spread)** — from **8 to 68 minutes**.
- **Unusual features** — an **outlier at 68 minutes** and a **gap between 42 and 68**.

> A note on honesty: there is a formal arithmetic test for outliers — the 1.5 × IQR rule — and it arrives in Session 3. For now, "unusually large relative to the rest" is the course's own definition and is entirely sufficient.
:::

### Write the whole description

:::yourturn
Write a complete description of the journey-time distribution. All four components, in context. Aim for three or four sentences. Do this properly before revealing — this is the exact task the exam sets.
:::

:::reveal Reveal — model answer and checklist
> *"The distribution of journey times for these 25 students is **skewed right** and **unimodal**, with one main peak between 10 and 20 minutes. The **centre** is about 18 minutes. Journey times **range from 8 to 68 minutes**. There is an **outlier at 68 minutes**, separated from the rest of the data by a **gap** between 42 and 68 — this student's journey took far longer than anyone else's."*

Mark your own against this:

- [ ] **Shape** — named the skew direction, and said unimodal
- [ ] **Centre** — gave a number, about 18 minutes
- [ ] **Variability** — gave the range, 8 to 68
- [ ] **Unusual features** — named the outlier *and* the gap
- [ ] **In context** — used the words "journey times", "minutes", "students"

**That last box is not decoration.** A description reading "skewed right and unimodal with an outlier" is statistically perfect and will still lose the interpretation mark, because it never says what the numbers are *about*. Name the variable, its units, and the individuals — every single time.
:::

### Justifying a claim: the half-hour journey

:::yourturn
A parent says: *"A typical journey to this school takes about half an hour."* Does the data support that? Write a full answer, using the template in *Justifying a claim from a quantitative distribution (1.6.B)*.
:::

:::reveal Reveal — the half-hour claim
**No.** The centre is about 18 minutes, not 30. Only five of the 25 journeys took 30 minutes or more.

What has probably happened is that the parent is thinking of the long right tail — the journeys of 30, 33, 36, 42 and 68 minutes — which are memorable but are the minority.

A supportable version of the claim:

> *"Most journeys take under 20 minutes, though a small number take considerably longer, up to 68 minutes."*

This is the same four-step template you met in Session 1, and you will use it in every unit from here to the exam:

> **State the claim · quote the number · say what the number does and does not establish · keep it in context.**
:::

---

## Part 7 — On your own: the café

No hints and no looking back at the reveals until all four are done. Write full answers.

A café recorded the number of drinks sold per hour over 20 opening hours:

```
14  16  17  19  20  21  21  22  23  24
24  25  26  27  28  30  31  33  35  52
```

:::yourturn
1. Construct a stem-and-leaf plot using tens as stems.
2. Construct a frequency table with bins of width 10, starting at 10.
3. Describe the distribution — all four components, in context.
4. The manager claims: *"We usually sell over 30 drinks an hour."* Is that supported? Justify.
:::

:::reveal Reveal — the café answers
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
:::

---

## Part 8 — Explain it back

:::yourturn
Close the booklet. Describe the café distribution out loud — or write it — as if to somebody who cannot see the graph. Stop yourself the moment you miss one of the four components.
:::

:::reveal Reveal — what a good explanation contains
Skewed right and unimodal, with the main peak in the twenties · a centre of about 24 drinks per hour · a spread from 14 to 52 drinks per hour · the outlier at 52 and the gap between 35 and 52 · and the context throughout: drinks, per hour, over these 20 opening hours.
:::

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

**C1.** A librarian says: *"Fiction borrowing went up this term — it rose from 96 books to 100."* Calculate the percentage for Fiction in each term, and explain why the comparison is misleading. (4)

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

**B1.** (3) rf = f ÷ n, 100rf = (f ÷ n) × 100, with n = 250.

| Section | *f* | *rf* | *100rf* | Angle |
|---|---|---|---|---|
| Fiction | 100 | 100 ÷ 250 = 0.400 | 40.0% | 144.0° |
| Non-fiction | 65 | 65 ÷ 250 = 0.260 | 26.0% | 93.6° |
| Reference | 40 | 40 ÷ 250 = 0.160 | 16.0% | 57.6° |
| Periodicals | 30 | 30 ÷ 250 = 0.120 | 12.0% | 43.2° |
| Other | 15 | 15 ÷ 250 = 0.060 | 6.0% | 21.6° |
| **Total** | **250** | **1.000** | **100%** | **360.0°** |

**B2.** (4) Formula: angle = (f ÷ n) × 360°. Values in the table above.

**B3.** (1) 144.0 + 93.6 + 57.6 + 43.2 + 21.6 = **360.0°** ✓

**B4.** (2) Bars of height 0.400, 0.260, 0.160, 0.120, 0.060 with **both axes labelled** — one mark is for the labels. Bars must **not touch**: this is categorical data, not a histogram.

### Part C (6 marks)

**C1.** (4) Fiction last term: 96 ÷ 200 = **48.0%** (1). Fiction this term: 100 ÷ 250 = **40.0%** (1). The comparison is misleading because the terms had different totals — 200 against 250 (1). Fiction's raw count rose by 4, but its **share fell from 48.0% to 40.0%**: relative to everything else borrowed, fiction became less popular, not more (1).

**C2.** (2) When two data sets have different totals, compare **relative frequencies or percentages**, not raw counts (1). Raw counts confound a change in the variable with a change in the overall total (1).

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

| Interval | *f* |
|---|---|
| 10 – under 20 | 1 |
| 20 – under 30 | 2 |
| 30 – under 40 | 8 |
| 40 – under 50 | 13 |
| **Total** | **24** |

**D3.** (2) bin width = (max − min) ÷ number of bins = (47 − 12) ÷ 7 = 35 ÷ 7 = **5**

**D4.** (1) The row must stay because it shows a value at 12 — an unusually low score, well separated from the rest. Skipping stems destroys the spacing that lets a stemplot show gaps and outliers.

### Part E (8 marks)

**E1.** (5) One mark each for shape, centre, variability, unusual features and context.

> *"The distribution of test scores for these 24 students is **skewed left** and **unimodal**, with one main peak in the 40s. The **centre** is about 40 marks. Scores **range from 12 to 47** out of 50. There is an **outlier at 12**, separated by a **gap** between 12 and 24 — one student scored far below everyone else."*

Accept "negatively skewed" for skewed left.

:::note amber The most common error here is "skewed right"
The bulk sits on the right, in the 40s, but the *tail* stretches left toward 12. Skew is named for the tail. If you got this wrong, flag it — it costs a mark every time it appears, and it will appear again.
:::

**E2.** (3) **Not** supported (1). From the frequency table only 1 + 2 + 8 = **11 of 24** students scored below 40, which is 45.8% — fewer than half (1). Supportable version: *"Slightly fewer than half the class scored below 40, and the most common band was 40–49."* (1)

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

*The student's to keep. Every term carries an example.*

### Displays for one categorical variable

**Bar chart (bar graph)** — one bar per category; height or length shows frequency **or** relative frequency. Bars do not touch.
*Example: six bars, one per hospital; the St Mary's bar reaches 84, or 0.280 on a relative frequency scale.*

**Pie chart** — one slice per category; each slice's area as a fraction of the whole equals its relative frequency. Slices total 1, or 100% of the area.
*Example: the St Mary's slice takes up 28.0% of the circle — an angle of 100.8°.*

### Displays for one quantitative variable

All three keep the natural ordering of the values, smallest to largest.

**Dotplot** — one dot per value, placed above its position on the axis; near-identical values stack.
*Example: two dots stacked above 12, because two students had 12-minute journeys.*

**Stem-and-leaf plot** — each value splits into a **stem** (leading digits) and a **leaf** (usually the final digit). Both ordered smallest to largest.
*Example: 18 becomes stem 1, leaf 8. Keep empty stems — a blank row is a gap in the data.*

**Histogram** — values grouped into ordered intervals (**bins**); each bar's height is the frequency or relative frequency in that bin. Bars touch, because the scale is continuous.
*Example: the bin "10 – under 20" has height 12, because 12 journeys fell in that range.*

:::note amber Bin width changes the appearance
Narrow bins show detail and noise; wide bins show shape. Neither is wrong, but the picture is a **choice**.
:::

### Formulas and self-checks

| Quantity | Formula | Example |
|---|---|---|
| Bar height | *f* or *rf* | 84, or 0.280 |
| Pie slice angle | (f ÷ n) × 360° | 0.280 × 360 = 100.8° |
| Pie slice share of area | 100rf | 28.0% |
| Histogram bar height | *f* or *rf* in that bin | 12, or 12 ÷ 25 = 0.480 |
| Bin width | (max − min) ÷ number of bins | (68 − 8) ÷ 6 = 10 |

:::checks
Σf = n
Σrf = 1
angles total 360°
bin frequencies total n
:::

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

:::note red Skew is named for the tail, not the bulk
Point at the long tail and say its direction out loud. This single error costs more marks in Unit 1 than anything else.
:::

:::note teal In context means
Naming the variable, its units, and the individuals — every time. Not "skewed right with an outlier", but "journey times for these 25 students are skewed right, with one student's journey of 68 minutes far longer than anyone else's."
:::

Many textbooks use the mnemonic **SOCS** — shape, outliers, centre, spread. It is the same four components the CED lists as shape, centre, variability and unusual features.

---

*CED references: Topic 1.4 (1.4.A.1–2, 1.4.B.1, 1.4.C.1), Topic 1.5 (1.5.A.1–4), Topic 1.6 (1.6.A.1–6, 1.6.B.1). Course and Exam Description effective Fall 2026.*

*Supporting reading: Barron's pdf 83–96 · Princeton Review 105–124 · 5 Steps to a 5 60–65.*

*Next session: Topics 1.7–1.9 — mean, median, standard deviation, the 1.5 × IQR outlier rule, boxplots, and comparing two distributions. The formal outlier test promised above arrives there.*
