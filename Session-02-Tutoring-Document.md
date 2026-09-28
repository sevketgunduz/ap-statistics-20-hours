# Session 2 — Shape of the Data: Showing and Describing One Variable

**AP Statistics · Twenty-Hour Course · One-to-one tutoring edition**
**CED Topics 1.4, 1.5, 1.6 · Skills 3.A, 4.A, 4.B · about 82 minutes · Homework 40 marks**

---

## Where this session sits

Turning tables into pictures, and then learning the four things you must say about every picture. The second half is the half that earns marks in April.

Session 1 gave the student the vocabulary and the tables. This session turns tables into **pictures**, then teaches the language for describing what the picture shows.

The second half is the more important half. Constructing a histogram is a five-minute skill. **Describing a distribution in a way that earns marks** is a skill students still get wrong in April, because it requires saying four specific things in context, and most students say two of them.

Every concept is stated first, in the theory section, before any data appear. The two scenarios, the activity and the solo case then apply it. The data are Session 1's: the hospital survey becomes bar and pie charts, and 25 of the Lincoln High journey times become a dotplot, a stem-and-leaf plot and a histogram.

### Learning objectives

Verbatim from the course description.

| Code | Objective | Skill |
|---|---|---|
| 1.4.A | Construct categorical one-variable graphical representations. | 3.A |
| 1.4.B | Justify a claim using categorical one-variable graphical representations. | 4.B |
| 1.4.C | Compare multiple categorical one-variable tabular and graphical representations. | 4.A |
| 1.5.A | Construct quantitative one-variable graphical representations. | 3.A |
| 1.6.A | Describe distributions of quantitative one-variable graphical representations. | 4.A |
| 1.6.B | Justify a claim using distributions of quantitative one-variable graphical representations. | 4.B |

Skills: **3.A** Construct tabular and graphical representations of data and distributions · **4.A** Describe and compare tabular and graphical representations of data, as well as summary statistics · **4.B** Justify a claim based on statistical calculations and results.

### What the course description does and does not ask for

Read this before teaching; several prep-book habits do not match the 2026 framework.

- **Histograms may be drawn sideways.** Topic 1.5.A.2 says a histogram "can be constructed with bins on the vertical axis with bars appearing horizontally". Accept one drawn that way.
- **The bin-width formula is not the course description's.** It says only that altering bin widths can change the appearance of a histogram. The formula (max − min) ÷ number of bins is a construction aid this course uses, and the theory section says so.
- **"Stemplot" is not a course-description word.** It always writes *stem-and-leaf plot*. The short form is fine in speech; use the full name in written answers.
- **SOCS is named by the course description itself**, as Shape, Outliers/Gaps, Center, Spread, together with a warning that students recite it and then omit gaps and outliers. The required list (1.6.A.1) is shape, center, variability and unusual features, in context.
- **Centre and variability are informal here.** Topic 1.6 requires them in every description but gives no measures; the median, mean, range and standard deviation are topic 1.7, next session. Today the centre is the middle value counted off a display, and the spread is "from … to …".
- **Outliers are a judgement here.** Topic 1.6.A.4 defines them as "unusually small or large relative to the rest of the data". The 1.5 × IQR and 2-standard-deviation rules are topic 1.8, next session.

:::note red Off-syllabus, not taught
Prep books often put **cumulative frequency plots (ogives)** next to histograms. The course description never mentions them, and they are on the removed-topics register (STANDARDS.md §8). If the student has met them, say they will not be examined.
:::

### Timing

| Minutes | Segment | Who talks |
|---|---|---|
| 0–8 | Homework debrief and diagnostic | Student |
| 8–30 | **Theory**: bar and pie charts, comparing data sets, dotplots, stem-and-leaf plots, histograms and bin width, the four components of a description, shape, centre and spread, unusual features, justifying a claim (1.4, 1.5, 1.6), then a theory check | Tutor, then student |
| 30–40 | **Scenario A**: the hospital survey in pictures, and the comparison trap (1.4) | Both |
| 40–54 | **Activity**: Build & Defend with the commute times, then bin width (1.5) | Student |
| 54–68 | **Scenario B**: describing the commute distribution (1.6) | Both |
| 68–76 | Solo case: the café | Student |
| 76–82 | Teach it back, set homework | Student |
| **Total** | **82 minutes** | |

The theory section makes this session longer than the plan's 60 minutes. Nothing is cut or moved to homework; the homework practises what the session taught.

---

## 0–8 min · Homework debrief and diagnostic

The student should arrive with Session 1's homework **self-marked**. Do not re-mark it. Ask for the two lists instead.

:::script
ask | Ask | "Which ones did you get wrong, and which ones did you put a question mark on?"
:::

Spend the time on those only. The question-marked items that turned out *right* are the most valuable: that is where confidence is missing but knowledge is not.

### The two Session 1 errors to check for

- **B5 answered "parameter".** The denominator test has not landed. Two minutes: *"how many did they actually ask?"*
- **D4 answered "yes, supported".** Plurality versus majority. Two minutes, because it recurs in every unit, starting today with "most" and "usually".

### Diagnostic: three retrieval questions

:::script
ask | Q1 | "Give me a categorical variable and a quantitative variable, from anything."
ask | Q2 | "If I have a table of counts for six hospitals, what could I draw?"
ask | Q3 | "What does a histogram show that a list of numbers doesn't?"
listen | Listen for | Q3 is the one that matters. Anything about **shape** or **pattern**. If the answer is only "it's easier to read", that is the gap this session fills.
:::

| What you hear | What it means | Where to start |
|---|---|---|
| Q1: a correct pair, e.g. travel mode and journey time | Session 1's variable types are secure | The theory section, at full pace |
| Q1: a number-coded category offered as quantitative (a postcode, a shirt number) | The categorical/quantitative line is not secure, and today's displays depend on it | Two minutes first: "would an average of it mean anything?" |
| Q2: "a bar chart or a pie chart" | Ready for topic 1.4 | Theory, *Bar charts* |
| Q2: "a histogram" | Categorical and quantitative displays are merged | Stress the bars-apart and bars-touching contrast in *Bar charts* and *Histograms and bins* |
| Q3: shape, pattern, "where the values pile up" | The idea of a distribution is there | Theory at full pace |
| Q3: "it's easier to read", "it looks nicer" | A graph is seen as decoration | Spend longest on *The four components of a description*; that is today's gap |

---

## 8–30 min · Theory — graphs and descriptions for one variable

Every concept the session uses is stated here, before any data. Teach it at the board: read the definition, work the illustration, then ask the question hidden in "what it does and does not say". Scenario A, the activity, Scenario B and the solo case apply these subsections and point back to them by name.

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

### Checking the theory before any data

Five quick questions, answered aloud, before Scenario A. Each one tests a subsection above, on made-up numbers.

:::script
ask | Ask | "A bar chart and a histogram both have bars. Give me two differences."
listen | Listen for | Categorical against quantitative; bars apart against bars touching, because a histogram's axis is a number line.
ask | Ask | "A category has 9 of 36 units. What is its slice angle?"
listen | Listen for | (9 ÷ 36) × 360° = 90°.
ask | Ask | "Last year a category held 30 of 100; this year 40 of 200. Did it grow?"
listen | Listen for | The count rose, 30 to 40; the share fell, 30% to 20%. Compare relative frequencies when totals differ.
ask | Ask | "The long tail stretches toward the small values. What is the shape called?"
listen | Listen for | Skewed left.
ifsay | If "skewed right" | "Point at the tail. Which way does it point?" The bulk is on the right, which is exactly why the error happens.
ask | Ask | "What must every description of a distribution contain?"
listen | Listen for | Shape, centre, variability, unusual features, in context. If context is missing, ask "about what?"
:::

---

## 30–40 min · Scenario A — the hospital survey, now in pictures

Deliberate continuity: this is **the same data the student tabulated last session**. Say so. Seeing a familiar table become a graph is the cheapest way to make the table–graph relationship obvious.

> The same **300 surveyed patients**, by hospital:
> **St Mary's 84 · Riverside 71 · Northgate 52 · Parkview 45 · Eastwood 30 · Hillcrest 18**

This scenario's trap is the comparison at the end: counts compared across two surveys of different size.

### Bar height: frequency or relative frequency

:::script
intro | Recall | *Bar charts (1.4.A)*: the height is a frequency or a relative frequency.
ask | Ask | "If you drew a bar chart of this, what would the height of the St Mary's bar be?"
listen | Listen for | Either **84** or **0.280**. Both are correct, and that is the point: a bar chart can show frequency *or* relative frequency.
ask | Ask | "So what changes if you plot relative frequency instead of frequency?" → nothing about the picture, only the scale. Make them say it.
:::

### Slice angles for the six hospitals

A pie chart shows each category's share of the whole, so the slice must be sized by relative frequency, not by count. The student applies the formula from *Pie charts and the slice angle (1.4.A)*, working each angle from *f* ÷ *n*.

:::formula
slice angle = (f ÷ n) × 360°  ·  slice share of area = 100rf
:::

| Hospital | *f* | *rf* = f ÷ 300 | Angle = (f ÷ 300) × 360° |
|---|---|---|---|
| St Mary's | 84 | 0.280 | 84 ÷ 300 × 360 = **100.8°** |
| Riverside | 71 | 0.237 | 71 ÷ 300 × 360 = **85.2°** |
| Northgate | 52 | 0.173 | 52 ÷ 300 × 360 = **62.4°** |
| Parkview | 45 | 0.150 | 45 ÷ 300 × 360 = **54.0°** |
| Eastwood | 30 | 0.100 | 30 ÷ 300 × 360 = **36.0°** |
| Hillcrest | 18 | 0.060 | 18 ÷ 300 × 360 = **21.6°** |
| **Total** | **300** | **1.000** | **360.0°** |

:::checks
angles total 360° ✓
same logic as Σrf = 1
:::

:::note amber Work from f ÷ n, not from the rounded rf
A student who multiplies the rounded 0.237 by 360 gets 85.3°, and 0.173 × 360 gives 62.3°. Both are a tenth out. Carry the unrounded fraction into the angle.
:::

### From table to graph

Show the student all three side by side. **The colour is the link**: St Mary's is the same blue in the table, the bar chart and the pie chart, so the eye carries one hospital across all three representations. Nothing is added or lost between them; the same six numbers are re-encoded as height, then as area.

**Table — the counts → Bar chart — height → Pie chart — area**

![Table of surveyed patients by hospital with each hospital's chart colour](figures/s02-hospital-table.svg)

*Step 1 · the table. The counts, with every derived column the two graphs will need. The colour chip is what ties each row to its bar and its slice.*

![Bar chart of surveyed patients by hospital](figures/bar-hospital.svg)

*Step 2 · bar chart. Height encodes the count. Good for comparing categories: the eye judges length accurately, so it is obvious that St Mary's exceeds Riverside by roughly 13 patients.*

![Pie chart of surveyed patients by hospital with slice angles](figures/pie-hospital.svg)

*Step 3 · pie chart. Area encodes the share. Good for part-to-whole: you can see at a glance that St Mary's is a bit over a quarter of the circle. Poor for comparing Northgate with Parkview, whose slices are close.*

:::script
intro | Recall | *Justifying a claim from a categorical graph (1.4.B)*: choose the display that answers the question.
ask | Ask | "Which of those two graphs would you use to answer 'did more than half our patients come from one hospital?'"
listen | Listen for | The pie, because the question is about a share of the whole, and half a circle is something you can see without arithmetic.
ask | Then | "And which one to answer 'how many more patients did Northgate see than Parkview?'" → the bar chart. The slices are too close to judge.
:::

### The comparison trap: last year against this year (1.4.C)

This is the part of topic 1.4 that actually gets examined. Give the student last year's figures.

> Last year the network surveyed **200** patients:
> **St Mary's 70 · Riverside 40 · Northgate 30 · Parkview 30 · Eastwood 20 · Hillcrest 10**

:::script
ask | Ask | "Did St Mary's handle more or fewer of the surveyed patients this year than last?"
listen | Expect | "More": 84 is bigger than 70. Let them commit.
ask | Then ask | "How many patients were surveyed each year?"
intro | Recall | *Comparing data sets with different totals (1.4.C)*: the rule from the theory section now has to be used on real numbers.
:::

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

:::note red The rule the student writes down
When two data sets have different totals, compare **relative frequencies**, never raw counts. A bar chart of counts across two unequal groups is misleading, and saying so is worth marks.
:::

:::script
ask | Ask | "Which hospital's share changed most?"
listen | Listen for | St Mary's, down 7.0 percentage points. Riverside rose 3.7. Everything else barely moved.
:::

---

## 40–54 min · Activity — Build & Defend with the commute times (1.5)

More continuity: Session 1's commute study measured journey time. Here are 25 of those journeys.

Journey times to school, in minutes, for 25 randomly chosen Lincoln High students:

```
 8   9  10  11  12  12  13  14  15  15
16  17  18  18  20  21  22  24  25  27
30  33  36  42  68
```

Already sorted, deliberately: sorting is not the skill being taught today.

The course description's sample activity for topic 1.5 is a **Gallery Walk**: groups of four each construct a dotplot, stem-and-leaf plot, histogram or boxplot of student journey times, then discuss what each graph shows more easily. One-to-one, **the student builds all three** of this session's displays, and then you interrogate which is best for which question. (The boxplot is topic 1.9, in Session 3.)

### Build: dotplot, stem-and-leaf plot and histogram

:::script
intro | Recall | *Dotplots (1.5.A.4)*, *Stem-and-leaf plots (1.5.A.3)* and *Histograms and bins (1.5.A.2)*. Give roughly four minutes for all three.
:::

**A dotplot**: one dot per value, stacked where values repeat.

**A stem-and-leaf plot**: stems are the tens digit, leaves the units, both ordered.

```
0 | 8 9
1 | 0 1 2 2 3 4 5 5 6 7 8 8
2 | 0 1 2 4 5 7
3 | 0 3 6
4 | 2
5 |
6 | 8
```

:::note amber Do not let them omit the empty 5 row
That blank row *is* the gap. A stemplot that skips unused stems has destroyed the information it exists to show.
:::

![Dotplot of 25 journey times in minutes](figures/dotplot-commute.svg)

*The dotplot. Every one of the 25 values is still visible as its own dot. This is the display that makes the outlier and the gap unmissable: the 68 sits alone, with nothing between 42 and 68.*

**A histogram**, bins of width 10:

| Interval | *f* |
|---|---|
| 0 – under 10 | 2 |
| 10 – under 20 | 12 |
| 20 – under 30 | 6 |
| 30 – under 40 | 3 |
| 40 – under 50 | 1 |
| 50 – under 60 | 0 |
| 60 – under 70 | 1 |
| **Total** | **25** |

:::formula
bin width = (maximum − minimum) ÷ number of bins  →  (68 − 8) ÷ 6 = 10
:::

The working rule asks for six bins; the table has seven because it starts at 0, a round boundary below the minimum, exactly as *Histograms and bins (1.5.A.2)* warns. Check that the frequencies total 25.

### Defend: which display answers which question

Ask these three, and make the student commit to one display each time. This is *What every quantitative display shows (1.5.A.1)* put to work.

| Question | Best display | Why |
|---|---|---|
| *"What was the exact longest journey?"* | Stemplot or dotplot | Both keep every individual value; the histogram has thrown them away |
| *"Roughly what does the overall shape look like?"* | Histogram | Bins smooth out noise and make the single peak obvious |
| *"Is there a journey far from all the others?"* | Dotplot or stemplot | The isolated 68 and the empty row are visible as a gap |

**The principle, in the student's own words:** histograms trade individual values for a clearer shape. Dotplots and stemplots keep every value but get unreadable with large *n*.

### Rebuilding the histogram with width-5 bins (1.5.A.2)

The course description says bin width changes the picture explicitly, so it is fair game (*Bin width changes the appearance*, in the theory section). Rebuild the same data with bins of width 5:

| Interval | *f* | | Interval | *f* |
|---|---|---|---|---|
| 5 – under 10 | 2 | | 30 – under 35 | 2 |
| 10 – under 15 | 6 | | 35 – under 40 | 1 |
| 15 – under 20 | 6 | | 40 – under 45 | 1 |
| 20 – under 25 | 4 | | 45 – under 65 | 0 |
| 25 – under 30 | 2 | | 65 – under 70 | 1 |
| Total | 25 | | | |

![Histogram of journey times, bin width 10](figures/hist-width10.svg)

*Bin width 10. One obvious peak between 10 and 20 minutes. The shape reads as clearly skewed right.*

![Histogram of journey times, bin width 5](figures/hist-width5.svg)

*Bin width 5. The same 25 journeys. The peak has split into two equal bars of 6 and the distribution looks flatter, almost as if it had two modes.*

:::script
ask | Ask | "Same data. Does it look the same?"
:::

**Both histograms are drawn on the same vertical scale**, so the comparison is honest: the width-5 bars really are shorter, because each bin now catches about half as many journeys. **Neither picture is wrong.** A histogram is a choice, and the choice affects the story, which is why the exam asks you to describe *shape* rather than trust one picture.

:::sim unit1-explorer | Unit 1 Explorer: Bin Width | 760
Open the **Bin Width** tab (the explorer opens on Sample & Estimate). It holds the same journey times, café drinks and test scores as this session. Let the student drag the width from 10 to 5 and then to 2, and say which features survive every width: the right skew, the single main peak and the 68 far from the rest. The exact bar heights do not survive.
:::

---

## 54–68 min · Scenario B — describing the commute distribution (1.6)

This is the heart of the session. The same 25 journeys, now described rather than drawn. This scenario's trap is different from Scenario A's: **naming the skew for the bulk instead of the tail**, and stopping before all four components are said, in context.

:::note teal The four components
Recall *The four components of a description (1.6.A.1)*: **shape, center, and variability (spread)**, plus **any unusual features** (outliers, gaps or clusters), **in context**. Many textbooks compress this to **SOCS**; it is the same four things in a different order. **Make the student write all four every single time.**
:::

### Shape of the journeys: which tail is longer

:::script
intro | Recall | *Shape: skew and symmetry (1.6.A.2)* and its figure: skew is named for the tail.
ask | Ask | "Which tail is longer?"
intro | Answer | The right. So: skewed right, unimodal (*Shape: counting the peaks*, 1.6.A.3).
ifsay | If "skewed left" | "Put a finger on the long thin tail. Which way does it point?" The tall bars are on the left, which is exactly why the error happens.
:::

:::note amber The reliable trick for direction
Skew is named for **where the tail points**, not where the bulk sits. Students reverse this constantly. Have them point at the tail with a finger and say the direction out loud.
:::

:::sim unit1-explorer | Unit 1 Explorer: Name That Shape | 760
Open the **Name That Shape** tab. A new histogram each round, with feedback on every answer. Ask for a streak of eight before moving on; anything less means the direction is still guesswork.
:::

### Centre, spread and unusual features of the journeys

:::script
intro | Recall | *Centre and variability, read from a graph (1.6.A.1)* and *Unusual features: outliers, gaps and clusters (1.6.A.4–6)*.
:::

- **Shape**: skewed right, unimodal, one main peak between 10 and 20 minutes.
- **Center**: about 18 minutes, countable off the stemplot as the 13th of 25 values, position (25 + 1) ÷ 2. *(Formal mean and median are topic 1.7, next session.)*
- **Variability**: from 8 to 68 minutes.
- **Unusual features**: an outlier at 68, and a gap between 42 and 68 with nothing in it.

Note the honest limit: the formal 1.5 × IQR outlier rule is topic 1.8, next session. Right now "unusually large relative to the rest" is the course description's own definition and is sufficient.

### The model answer and its checklist

Have the student write this out in full, then compare against yours.

> *"The distribution of journey times for these 25 students is **skewed right** and **unimodal**, with one main peak between 10 and 20 minutes. The **centre** is about 18 minutes. Journey times **range from 8 to 68 minutes**. There is an **outlier at 68 minutes**, separated from the rest by a **gap** between 42 and 68 — this student's journey took far longer than anyone else's."*

| Component | Present? | The words |
|---|---|---|
| Shape | ✓ | skewed right, unimodal |
| Center | ✓ | about 18 minutes |
| Variability | ✓ | 8 to 68 minutes |
| Unusual features | ✓ | outlier at 68, gap 42–68 |
| **In context** | ✓ | "journey times", "minutes", "students" |

:::note red Context is not decoration
A description that says "skewed right with an outlier" and never mentions journeys, minutes or students will lose the interpretation mark even though every statistical word is correct.
:::

### Justifying a claim: the half-hour journey (1.6.B)

:::script
intro | Recall | *Justifying a claim from a quantitative distribution (1.6.B)*: state the claim, quote the number, say what it does and does not establish, keep it in context.
ask | Ask | "A parent says: a typical journey to this school takes about half an hour. Does this data support that?"
intro | Answer | No. The centre is about 18 minutes, not 30.
:::

The claim is probably driven by the long right tail, journeys of 30, 33, 36, 42 and 68 minutes, but those are the minority: five of the 25. A supportable version: *"Most journeys take under 20 minutes, though a small number take considerably longer, up to 68 minutes."*

Same template as last session: **state the claim · quote the number · say what it does and does not establish · keep it in context.**

---

## 68–76 min · Solo case — the café

Unaided. Watch, say nothing, note where they hesitate.

A café recorded the number of drinks sold per hour over 20 opening hours:

```
14  16  17  19  20  21  21  22  23  24
24  25  26  27  28  30  31  33  35  52
```

1. Construct a stem-and-leaf plot using tens as stems.
2. Construct a frequency table with bins of width 10, starting at 10.
3. Describe the distribution. All four components, in context.
4. The manager claims: *"We usually sell over 30 drinks an hour."* Is that supported? Justify.

### Café answers and what to watch for

```
1 | 4 6 7 9
2 | 0 1 1 2 3 4 4 5 6 7 8
3 | 0 1 3 5
4 |
5 | 2
```

**Bins:** 10 – under 20 → 4; 20 – under 30 → 11; 30 – under 40 → 4; 40 – under 50 → 0; 50 – under 60 → 1. Total 20.

**Description:** skewed right, unimodal, main peak in the 20s. Centre about 24 drinks per hour (median of 20 values = (24 + 24) ÷ 2 = 24). Ranges from 14 to 52 drinks per hour. Outlier at 52, separated by a gap between 35 and 52.

**Claim:** not supported. The centre is about 24, and only **4 of the 20 hours** sold more than 30 (31, 33, 35, 52): that is 20% of hours, not "usually". A supportable version: *"Sales are usually in the twenties per hour, with one unusually busy hour of 52."*

:::note amber Watch for
Describing shape and centre and stopping. Calling it "skewed left" because the bulk sits on the left. Omitting the empty `4 |` stem.
:::

---

## 76–82 min · Teach it back

:::script
ask | Ask | "Describe the café distribution to me out loud, as if I can't see the graph. I'll stop you the moment you miss one of the four."
:::

Doing it aloud rather than in writing is the point: it exposes whether the four components are a habit or a checklist they consult.

**A good answer contains:** skewed right and unimodal, with the main peak in the twenties · a centre of about 24 drinks per hour · a spread from 14 to 52 drinks per hour · the outlier at 52 and the gap between 35 and 52 · and the context throughout: drinks, per hour, over these 20 opening hours.

Then set the homework.

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
