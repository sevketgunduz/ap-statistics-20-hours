# Session 3 — Summarising and Comparing Distributions

**AP Statistics · Twenty-Hour Course · Student edition, to work through on your own**
**CED Topics 1.7, 1.8, 1.9 · About 140 minutes, plus homework**

---

## How to use this

The same rule as the last two sessions, and today there is more to calculate.

:::note amber Write first, then reveal
Every **Your turn** box asks you to do something before the text shows you the answer. **Do it on paper first.** The five-number summaries, fences, boxplots and comparisons are all hidden behind reveals so that you cannot copy them. Copying a boxplot teaches you nothing. Drawing one and finding the whisker in the wrong place teaches you where the whisker goes.
:::

**What you need:** paper, a pen, a ruler and a calculator. A TI-84 or any calculator with a one-variable statistics mode will save time on the standard deviation.

**One convention, used all the way through.** To find the quartiles, split the ordered data at the median. **When n is odd, the median itself goes in neither half.** Q1 is the median of the lower half and Q3 is the median of the upper half. This is what a TI-84 does. Other methods exist and give slightly different answers; if your school uses one of them, that is fine, but use one method every time.

### How this maps to your tutor's document

Working alone with a pen is slower than working with a tutor, so each part is given about a quarter longer than the tutor's segment. Take the time: the writing is the learning.

| Your section | Tutor's section | Minutes |
|---|---|---|
| Part 1 — Your Session 2 homework, and a warm-up | 0–10 Homework debrief and diagnostic | 12 |
| Part 2 — Why this matters | (the framing) | 3 |
| Part 3 — The commute times, summarised | 10–55 Scenario A | 56 |
| Part 4 — Match Mine, on your own | 55–67 Activity | 15 |
| Part 5 — Comparing: two hospitals, then two library branches | 67–97 Scenario B | 38 |
| Part 6 — On your own: the café | 97–105 Solo case | 10 |
| Part 7 — Explain it back | 105–110 Teach it back | 6 |
| **Total** | **110 minutes** | **140** |

If your tutor has not yet set the **Session 1 test**, take it before Part 1: 40 minutes, timed, answer key closed.

---

## Part 1 — Your Session 2 homework, and a warm-up

Get out your marked Session 2 homework and make two lists: the questions you got **wrong**, and the questions you marked with a **?**, including the ones that turned out right.

**Two specific things to check.** They are the two most common errors on that sheet, and both come back today.

- **E1: did you call the test scores "skewed right"?** Most scores are in the 40s and the tail stretches down to 12, so the distribution is skewed **left**. Skew is named after the tail, not the bulk. Today gives you a second check that does not depend on your eyes: for these scores the mean is **below** the median, which is what usually happens when the tail is on the left. You will calculate both in the homework.
- **C1: did you agree that fiction borrowing "went up"?** Its count rose from 96 to 100, but its share fell from 48.0% to 40.0%, because the totals were 200 and 250. The general lesson is that **a raw number means nothing until you know what it is measured against.** It comes back in Part 5, in a different form.

### Warm-up

:::yourturn
Four questions. Answer all four on paper before revealing.

1. What is the median of 9, 1, 7, 4?
2. The Session 2 test scores were skewed left. Without calculating, would you expect the mean to be above or below the median?
3. Two classes both averaged 70 on the same test. What else would you want to know before saying they did equally well?
4. In one sentence, what does a standard deviation tell you?
:::

:::reveal Reveal — and what your answers mean
| If you said | It means | Do this |
|---|---|---|
| **1:** 5.5 | You sorted first and averaged the middle two, 4 and 7. Correct. | Carry on |
| **1:** 4 | You averaged 1 and 7, the middle pair of the **unsorted** list | Always order the data first. Watch for it in Part 3 |
| **1:** "there's no middle" | You have not met the rule for an even number of values | The median is then the mean of the two middle values |
| **2:** below | Correct: the low tail pulls the mean down | Carry on |
| **2:** above | The skew direction or the pull of the tail is reversed | Re-read the E1 note above, then Part 3 explains the pull |
| **3:** anything about spread, range or consistency | You already have the idea of variability | Part 3 gives it three numbers |
| **3:** "nothing, they're the same" | Centre is the only summary you are using | Read Part 3's spread section slowly |
| **4:** "how spread out the data are" | Right idea, too vague to earn a mark | The precise version: **a typical distance of the values from their mean** |
| **4:** blank | Not met yet | Expected. Part 3 teaches it |
:::

---

## Part 2 — Why this matters

Session 2 taught you to describe a distribution in words. This session gives those words numbers: a centre, a spread, a position, and an arithmetic test for "unusual". Then it asks you to **compare** two groups using them.

Comparing is where the marks are lost. Students who can find every summary statistic still write one paragraph about each group and never say how the groups relate, and that earns nothing for "compare". If you are short of time today, protect Part 5.

---

## Part 3 — The commute times, summarised

The same 25 journeys you drew three ways in Session 2. Nothing new has been collected.

Journey times to school, in minutes, for 25 randomly chosen Lincoln High students:

```
8   9  10  11  12  12  13  14  15  15
16  17  18  18  20  21  22  24  25  27
30  33  36  42  68
```

### Centre: mean and median

:::yourturn
Calculate the **mean** and the **median**. Then answer: last session a parent claimed a typical journey takes about half an hour. Which of your two numbers should answer him, and why are they different?
:::

:::reveal Reveal — mean, median, and which is "typical"
**Mean:** *x̄* = Σ *x* ÷ *n* = 536 ÷ 25 = **21.44 minutes**.

**Median:** the middle of 25 ordered values is the **13th**, which is **18 minutes**. (With an even number of values it would be the mean of the two middle ones.)

**Which is typical?** The **median**. The mean is higher because a few long journeys, above all the 68, pull it upwards: every minute of every journey goes into the total. The median only cares which value is in the middle.

This is a general pattern, and the course states it directly:

| Shape | Usually |
|---|---|
| Roughly symmetric | mean ≈ median |
| Skewed right | mean > median |
| Skewed left | mean < median |

These journeys are skewed right, and 21.44 > 18. The Session 2 test scores are skewed left, and there the mean is below the median.
:::

### Position: the quartiles

:::yourturn
The median splits the 25 journeys into two halves. Using this course's convention, how many values are in each half? Find **Q1** (the median of the lower half) and **Q3** (the median of the upper half). Then write the **five-number summary**: minimum, Q1, median, Q3, maximum.
:::

:::reveal Reveal — the quartiles and the five-number summary
With *n* = 25 the median is the 13th value, and it goes in **neither** half. That leaves **12 values in each half**, so each quartile is the mean of the two middle values of its half.

![The 25 journey times split into halves, median excluded, with Q1 and Q3](figures/s03-quartiles-commute.svg)

- Q1 = (12 + 13) ÷ 2 = **12.5**
- Q3 = (25 + 27) ÷ 2 = **26**

**Five-number summary: 8, 12.5, 18, 26, 68.**

If you got **Q1 = 13 and Q3 = 25**, you included the median in both halves. That is a genuine method some books use, but it is not this course's; switch now and stay switched.
:::

:::yourturn
One more position question. What **percentile** is a journey of 30 minutes? (The pth percentile is the value with p% of the data less than or equal to it.)
:::

:::reveal Reveal — percentile
The question is: *what percentage of the journeys took 30 minutes or less?*

1. **Order the data.** The 25 journeys above are already sorted.
2. **Count the journeys of 30 minutes or less, including the 30 itself.** The first two rows are 20 journeys, all under 30, and the 30 is the 21st value. That is **21 journeys**.
3. **Divide by the total.** 21 ÷ 25 = 0.84 = **84%**.
4. **Answer in context.** 30 minutes is the **84th percentile**: 84% of these students' journeys took 30 minutes or less.

**Check:** 4 journeys are longer than 30 minutes (33, 36, 42 and 68), and 4 ÷ 25 = 16%. 84% + 16% = 100%.

| If you wrote | What went wrong |
|---|---|
| 80th | You counted only the journeys *less than* 30 (20 of 25) and left out the 30 itself. The definition says "less than **or equal to**". |
| 21st | You gave the **position** of 30 in the ordered list, not the percentage. |
| 44th | You divided the value by the maximum (30 ÷ 68). A percentile counts values; it does not compare their sizes. |

Q1 is roughly the 25th percentile and Q3 roughly the 75th. "Roughly" is exact language: here 6 of the 25 values (24%) are at or below Q1 = 12.5.
:::

### Spread: three measures

| Measure | Formula | Commute times |
|---|---|---|
| Range | max − min | 68 − 8 = **60 minutes** |
| Interquartile range (IQR) | Q3 − Q1 | 26 − 12.5 = **13.5 minutes** |
| Standard deviation | *s* = √[Σ(*x*ᵢ − *x̄*)² ÷ (*n* − 1)] | **13.07 minutes** (calculator, below) |

Range and IQR need only subtraction. The standard deviation takes more work, and the course expects you to find it both by hand and with technology. The formula is on the exam formula sheet.

### The standard deviation, by hand

:::formula
s = √[ Σ(xᵢ − x̄)² ÷ (n − 1) ]
:::

**A worked example.** Take five of the 25 journeys: **10, 14, 18, 22, 36** minutes.

| *x* | *x* − *x̄* | (*x* − *x̄*)² |
|---|---|---|
| 10 | −10 | 100 |
| 14 | −6 | 36 |
| 18 | −2 | 4 |
| 22 | 2 | 4 |
| 36 | 16 | 256 |
| **Total** | **0** | **400** |

1. Mean: *x̄* = 100 ÷ 5 = **20** minutes.
2. Deviations from the mean. **They always total 0.** That checks your arithmetic, and it is why the deviations are squared: positive and negative deviations would cancel.
3. Square each deviation and add: **400**.
4. Divide by *n* − 1 = 4: *s*² = 400 ÷ 4 = **100**, the sample variance.
5. Take the square root: *s* = √100 = **10 minutes**.

Notice which journey contributes most: the 36, whose deviation of 16 squares to 256, more than the other four together. Squaring makes far-away values count heavily, which is why the standard deviation is pulled by outliers.

:::yourturn
Your turn, the same way. Five more of the journeys: **8, 12, 15, 20, 30**. Make the three-column table, check that the deviations total 0, then find *s*² and *s*.
:::

:::reveal Reveal — the standard deviation of 8, 12, 15, 20, 30
| *x* | *x* − *x̄* | (*x* − *x̄*)² |
|---|---|---|
| 8 | −9 | 81 |
| 12 | −5 | 25 |
| 15 | −2 | 4 |
| 20 | 3 | 9 |
| 30 | 13 | 169 |
| **Total** | **0** | **288** |

*x̄* = 85 ÷ 5 = **17**. *s*² = 288 ÷ 4 = **72**. *s* = √72 = **8.49 minutes**.

| If you got | You | Fix |
|---|---|---|
| 7.59 | divided by *n* = 5 (288 ÷ 5 = 57.6) | The sample formula divides by *n* − 1 |
| 72 | stopped at the variance | Take the square root; 72 is in minutes squared |
| 0 | squared the total of the deviations | Square each deviation first, then add |
:::

**All 25 by calculator.** Nobody squares 25 deviations in an exam. Enter the journeys in a list and run 1-Var Stats: *s* = **13.07 minutes**. The calculator shows *Sx* (the sample standard deviation, dividing by *n* − 1) and *σx* (dividing by *n*); the course uses *s*, which is *Sx*.

:::yourturn
Put *s* = 13.07 minutes into one sentence about these journeys.
:::

:::reveal Reveal — what s means
*"A typical journey differs from the mean of 21.44 minutes by about 13 minutes."*

The standard deviation is **a typical distance of the values from their mean**. It is not the distance between neighbouring values, and it is not the range. Its square, *s*² = 170.76, is the **variance**, in minutes squared, which is why *s* is the number people report.
:::

### The outlier test that Session 2 promised

In Session 2 you called the 68-minute journey an outlier because it looked far from everything else. Here is the arithmetic test.

:::formula
lower fence = Q1 − 1.5 × IQR     upper fence = Q3 + 1.5 × IQR
:::

An outlier is any value **more than** 1.5 × IQR above Q3 or below Q1: beyond a fence.

:::yourturn
Calculate both fences. Is 68 an outlier? Is 42? It sits a fair way from 36.
:::

:::reveal Reveal — the fences
1.5 × IQR = 1.5 × 13.5 = **20.25**.

- Lower fence: 12.5 − 20.25 = **−7.75**. No journey is below it.
- Upper fence: 26 + 20.25 = **46.25**.

**68 is an outlier**: it is above 46.25. Session 2's judgement by eye was right, and now it is justified.

**42 is not an outlier**, however isolated it looks: it is below 46.25. When a question says *use the 1.5 × IQR rule*, the rule decides, not the picture. A value exactly on a fence is not an outlier either, because the rule says *more than*.
:::

**A second rule.** The course description lists another method, and some prep books skip it: an outlier is a value more than **2 standard deviations** from the mean. Here 21.44 ± 2(13.07) runs from −4.70 to 47.58, so 68 is an outlier by this rule too. The two rules do not always agree: the homework has a data set where they disagree. Say which one you are using.

### Build the boxplot

A **boxplot** draws the five-number summary. The box runs from Q1 to Q3 with a line at the median. The whiskers run out to the most extreme values that are **not** outliers, and any outlier is marked on its own with a symbol such as an asterisk.

:::yourturn
Draw the boxplot of the journey times on a scale from 0 to 70, by hand. Before you draw the right-hand whisker, decide exactly where it ends.
:::

:::reveal Reveal — the boxplot
![Dotplot and boxplot of 25 journey times, upper fence at 46.25, 68 marked as an outlier](figures/s03-boxplot-commute.svg)

The right-hand whisker ends at **42**, the largest journey that is not an outlier.

- If yours runs to **68**: 68 is an outlier, so it gets its own symbol and the whisker stops before it.
- If yours runs to **46.25**: nobody's journey is 46.25 minutes. The whisker ends at a data value. The fence is a cut-off you calculate; it is never part of the drawing. (It is dashed in the figure above only to show why 68 stands apart.)

**One misreading to avoid.** The right whisker is long and the left short, but each holds about a quarter of the journeys. A longer section means the values there are **more spread out**, not that there are more of them.
:::

### Resistance: what happens if the outlier moves

:::sim boxplot-builder | Boxplot & 1.5 × IQR Builder | 820
**Do not touch it yet.** Answer the prediction below on paper first, then come back and test it. Journey 25 (68 minutes) is selected when the tool opens: drag its dot, or move the slider, up to 118. Then slide it **down** past 46 and watch the moment it stops being an outlier. Keyboard: choose a value in the menu, then use the arrow keys on the slider.
:::

:::yourturn
Predict before you touch the tool. Suppose that student's journey had been **118** minutes instead of 68. For each of the mean, median, IQR, standard deviation and range, write **changes** or **stays the same**. Then test your prediction with the tool above.
:::

:::reveal Reveal — what changed and what didn't
![Changing the largest journey from 68 to 118 minutes moves the mean but not the median](figures/s03-resistance.svg)

| Statistic | 68 as recorded | If it were 118 | |
|---|---|---|---|
| Median | 18 | 18 | stays the same |
| IQR | 13.5 | 13.5 | stays the same |
| Mean | 21.44 | 23.44 | changes |
| Standard deviation | 13.07 | 21.56 | changes |
| Range | 60 | 110 | changes |

**Why the median does not move:** it is the 13th value, and making the largest value larger does not change which value is 13th. Q1, Q3 and so the fences are positional in the same way, so they do not move either.

**Why the mean does:** it adds up every value. An extra 50 minutes shared among 25 students raises it by 50 ÷ 25 = 2.

That is what **resistant** means: outliers do not greatly affect the value. The **median and IQR** are resistant. The **mean, standard deviation and range** are not.
:::

:::note teal The sentence to keep
With strong skew or outliers, report the **median and IQR**. The mean and standard deviation are pulled by the tail. With a roughly symmetric distribution and no outliers, the mean and standard deviation are fine.
:::

### Changing units

There are two kinds of change, and they behave differently.

:::yourturn
**Multiplying or dividing.** The principal wants the report in hours. Convert each of these to hours: mean 21.44, median 18, Q1 12.5, Q3 26, the 84th percentile 30, range 60, IQR 13.5, standard deviation 13.07 (all in minutes). Which of them change?
:::

:::reveal Reveal — minutes to hours
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
:::

:::yourturn
**Adding or subtracting.** The gate clock ran 3 minutes fast, so every recorded journey is 3 minutes too long. After subtracting 3 from every journey, what are the new mean, median, Q1, Q3, 84th percentile, minimum, maximum, range, IQR and standard deviation? Is 68, now 65, still an outlier?
:::

:::reveal Reveal — subtracting 3 minutes
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

Every value slides 3 minutes to the left and no two values move closer together, so no measure of spread changes. The fences slide too, to −10.75 and 43.25, so **65 is still the one outlier**. Changing units never changes which values are outliers.
:::

:::note teal The two groups, and the rule for each
**Centre and position** (mean, median, quartiles, percentiles, minimum, maximum) behave like data values. **Spread** (range, IQR, standard deviation) measures distances between values.

| Change to every value | Centre and position | Spread |
|---|---|---|
| Add or subtract a constant | shift by that constant | unchanged |
| Multiply or divide by a positive constant | multiplied or divided by it | multiplied or divided by it |
:::

:::yourturn
**Both at once: °C to °F.** The café recorded the midday temperature outside on 10 days:

```
12  14  15  15  16  18  19  21  22  28     (°C)
```

In °C the mean is 18.0, median 17, Q1 15, Q3 21, IQR 6 and standard deviation 4.714. Using F = 1.8C + 32, give the mean, median, IQR and standard deviation in °F **without** converting the ten values.
:::

:::reveal Reveal — °C to °F
- Mean: 1.8(18.0) + 32 = **64.4 °F**
- Median: 1.8(17) + 32 = **62.6 °F**
- IQR: 1.8(6) = **10.8 °F**
- Standard deviation: 1.8(4.714) = **8.49 °F**

Centre and position get both steps; spread gets only the multiplication. Check it through the quartiles: Q1 = 1.8(15) + 32 = 59 and Q3 = 1.8(21) + 32 = 69.8, so the IQR is 69.8 − 59 = 10.8. The + 32 cancels in the subtraction, which is exactly why spread ignores it.

If you got a standard deviation of 40.49, you added 32. Adding 32 to every temperature moves no two days further apart.
:::

:::yourturn
**The course description's own question type.** A teacher adds 1 bonus mark to every one of the 24 test scores. Which of these has the same value before and after?

(A) the median (B) the mean (C) the third quartile (D) the interquartile range
:::

:::reveal Reveal — the bonus mark
**(D) the interquartile range.** The median, the mean and the third quartile are centre or position, and each rises by 1. Q1 and Q3 both rise by 1, so their difference does not change.
:::

---

## Part 4 — Match Mine, on your own

In the classroom version of this activity, two students sit either side of a folder with the same nine cards. One arranges them on a 3×3 grid and describes the arrangement; the other rebuilds it from the words alone. Precise language is the whole game.

Here are the nine cards:

![Nine Match Mine cards, histograms A to I on a common 0 to 100 scale](figures/s03-matchmine-cards.svg)

*Look closely at the pairs: several differ in only one feature.*

### Rebuild your partner's grid

Your partner has described their grid. Seven of the descriptions are precise. Two are not.

| Position | Your partner says |
|---|---|
| Top left | Symmetric and unimodal, centred at about 50, most values between 30 and 70, and one outlier above 90, separated by a gap |
| Top middle | Skewed right, with its peak between 10 and 20 |
| Top right | Approximately uniform from 0 to 100, no peak |
| Middle left | Symmetric and unimodal, centred at about 50 |
| Centre | Skewed right, peak between 10 and 20, then a gap from 50 to 80 and a small cluster between 80 and 100 |
| Middle right | Skewed left, peak between 80 and 90, tail stretching down to about 10 |
| Bottom left | Bimodal, with peaks near 25 and 75 and very few values near 50 |
| Bottom middle | Symmetric and unimodal, centred at about 30, narrow, nearly all values between 0 and 60 |
| Bottom right | Roughly symmetric, a broad single mound centred at about 50, wide, with values across almost the whole range from 0 to 100 |

:::yourturn
1. Write the letter of the card you would place in each position.
2. For the two imprecise descriptions, list **every** card that fits the words as written, and the word or phrase your partner should have added.
:::

:::reveal Reveal — the grid
| | Left | Middle | Right |
|---|---|---|---|
| **Top** | G | C | F |
| **Middle** | A | I | D |
| **Bottom** | E | H | B |

**Top middle** ("skewed right, peak between 10 and 20") fits **C and I**. It needed **"no gaps"**, or "tail stretching smoothly to about 90".

**Middle left** ("symmetric and unimodal, centred at about 50") fits **A, B and G**. It needed a **spread** ("narrow, nearly all values between 30 and 70") and **"no outliers"**.

You only placed those two by elimination, because the other seven were precise. In an exam there is nothing to eliminate against: an examiner reads each description on its own. The missing words are the same four components you learned in Session 2: shape, centre, variability, unusual features.
:::

:::yourturn
Write a description of card **B** and a description of card **H** that could not be matched to any other card. Then check each against all nine.
:::

:::reveal Reveal — model descriptions
**B:** *"Roughly symmetric and unimodal, a broad mound centred at about 50, with a wide spread: values across almost the whole range from 0 to 100, and no gaps or outliers."* The word doing the work is **wide**; without it this also fits A.

**H:** *"Symmetric and unimodal, centred at about 30, narrow, with nearly all values between 0 and 60 and no outliers."* The word doing the work is the **centre**, 30; without it this also fits A.
:::

### The question that makes this topic 1.9

:::yourturn
If every card were redrawn as a **boxplot**, which two cards would be hardest to tell apart? Why?
:::

:::reveal Reveal — the lookalike pair
**E and F**: bimodal and uniform. Both have a median of about 50 and quartiles of about 25 and 75.

![Card E is bimodal and card F is uniform, yet their boxplots are almost identical](figures/s03-lookalike.svg)

Card E's five-number summary is 5, 24.45, 50, 75.55, 95; card F's is 1.2, 25, 50, 75, 98.8. And E's median sits exactly where almost no data are.

**The rule this illustrates:** histograms, dotplots and stemplots can compare centre, variability, shape, outliers, **clusters and gaps**. Boxplots can compare centre, variability, outliers and skewness or symmetry, but **not clusters or gaps**.
:::

---

## Part 5 — Comparing: two hospitals, then two library branches

Session 1's hospital survey recorded, for each of its 300 patients, the minutes from arrival to being seen by a doctor. You never used that variable. Here it is for the two largest hospitals.

Waiting time from arrival to being seen by a doctor, in minutes, for the surveyed patients at St Mary's and Riverside:

| Hospital | *n* | *x̄* | *s* | Min | Q1 | Median | Q3 | Max |
|---|---|---|---|---|---|---|---|---|
| St Mary's | 84 | 37.1 | 16.3 | 12 | 25.5 | 34 | 45 | 97 |
| Riverside | 71 | 26.0 | 7.4 | 8 | 21 | 26 | 31 | 44 |

### Outliers first

:::yourturn
St Mary's four largest waits were 70, 75, 88 and 97 minutes. Which of them are outliers by the 1.5 × IQR rule? Does Riverside have any outliers?
:::

:::reveal Reveal — outliers at each hospital
**St Mary's:** IQR = 45 − 25.5 = 19.5; 1.5 × 19.5 = 29.25; upper fence 45 + 29.25 = **74.25**. So **75, 88 and 97 are outliers**, and 70 is not. The upper whisker ends at 70. (75 is an outlier by three quarters of a minute; the rule is a rule.)

**Riverside:** IQR = 31 − 21 = 10; 1.5 × 10 = 15; fences 21 − 15 = **6** and 31 + 15 = **46**. The minimum (8) and maximum (44) are both inside, so **no outliers**.
:::

Here are both hospitals on one scale. A comparison is only honest when the two groups share an axis.

![Parallel boxplots of waiting times at St Mary's and Riverside](figures/s03-boxplot-hospitals.svg)

### Write the comparison

:::yourturn
**Compare** the waiting times at the two hospitals. Cover **centre, variability, shape and outliers**, in context. Write it in full before you reveal. This is exactly the task a free-response question sets.
:::

:::reveal Reveal — model comparison and the trap
> *"The median wait at St Mary's (34 minutes) is **longer than** at Riverside (26 minutes). Waits at St Mary's are **more variable**: the IQR is 19.5 minutes against Riverside's 10, and the range is 85 minutes against 36. St Mary's distribution is **skewed right** (mean 37.1 above median 34, and a longer upper whisker), while Riverside's is **roughly symmetric** (mean and median both 26, and Q1 and Q3 each 5 minutes from the median). St Mary's has **three high outliers**, at 75, 88 and 97 minutes; Riverside has **none**."*

Mark your own:

- [ ] **Centre**: a comparison of the medians, with numbers
- [ ] **Variability**: IQR (or range) compared, with numbers
- [ ] **Shape**: both shapes named, with the evidence
- [ ] **Outliers**: both hospitals mentioned
- [ ] **Comparative words** in every sentence: *longer than, more variable, while, against*
- [ ] **In context**: waiting time, minutes, patients

**The trap.** If you wrote *"St Mary's has a median of 34 and an IQR of 19.5. Riverside has a median of 26 and an IQR of 10"*, every number is right and the comparison mark is still lost. Those are two descriptions placed side by side. The reader should not have to do the comparing for you.
:::

### Shape from the table alone

:::yourturn
Suppose you had only the table and no boxplots. Give **two** separate pieces of evidence from the numbers that St Mary's is skewed right.
:::

:::reveal Reveal — shape from summary statistics
1. The **mean (37.1) is greater than the median (34)**: the long upper tail pulls the mean up.
2. The distance from **Q1 to the median (8.5 minutes)** is smaller than from **the median to Q3 (11 minutes)**: the upper part of the middle half is more spread out.

The course description's own sample scoring guidelines list *"The distribution is right-skewed"*, on its own, as an answer that does **not** earn the point. The credit is for quoting the comparison.
:::

### Relative position: z-scores

:::yourturn
One St Mary's patient waited **62 minutes**. One Riverside patient waited **41 minutes**. Whose wait was more unusual **for their own hospital**? Write down your instinct first, then calculate.

Use z = (*x* − mean) ÷ standard deviation.
:::

:::reveal Reveal — z-scores
- St Mary's: z = (62 − 37.1) ÷ 16.3 = **1.53**
- Riverside: z = (41 − 26.0) ÷ 7.4 = **2.03**

The **Riverside** wait is the more unusual one: about 2 standard deviations above its hospital's mean, against 1.5 for the St Mary's wait, even though it is 21 minutes shorter.

A **z-score** is the number of standard deviations a value lies above (positive) or below (negative) the mean. The course defines it with the population mean μ and standard deviation σ; when those are unknown, as here, you use the sample's *x̄* and *s*.

If your instinct was the 62-minute wait, that is the C1 mistake from your Session 2 homework in a new form: a raw number compared without asking what it is measured against. Each hospital has its own centre and spread.
:::

### Justify a claim

:::yourturn
The hospital network says: *"Patients are seen faster at Riverside."* Is this supported? Use the boxplots or the table, and say what the data do **not** show.
:::

:::reveal Reveal — the claim
**Supported.** The strongest evidence is positional: Riverside's **Q3 (31 minutes) is below St Mary's median (34 minutes)**. So about three quarters of Riverside patients were seen within 31 minutes, while fewer than half of St Mary's patients were. In the survey that is 55 of 71 at Riverside (77.5%) against 36 of 84 at St Mary's (42.9%).

**What it does not show:** *why*. These are survey data, not an experiment. St Mary's may see more seriously ill patients, or be busier at different times; nothing here says that Riverside's methods cause the shorter waits.

The same template as Sessions 1 and 2: **state the claim · quote the numbers · say what they do and do not establish · keep it in context.**
:::

### A second comparison, from a summary table alone

This time there is no picture, only the kind of table a free-response question prints. Session 1's library service took a random sample of members at each of two branches and recorded the hours each spent in library buildings last year.

| Branch | *n* | *x̄* | *s* | Min | Q1 | Median | Q3 | Max |
|---|---|---|---|---|---|---|---|---|
| Central | 35 | 40.0 | 11.0 | 16 | 32 | 40 | 48 | 64 |
| Westside | 30 | 28.0 | 17.2 | 8 | 17 | 24.5 | 34 | 96 |

:::yourturn
1. Use the 1.5 × IQR rule to decide whether either branch has outliers. Show both fences for each.
2. Westside's standard deviation is 17.2 against Central's 11.0. Someone concludes that Westside's members are much more variable. Do you agree? Which measure of spread should you compare here, and why?
:::

:::reveal Reveal — outliers, and which spread to compare
**1.** Central: IQR = 48 − 32 = 16; fences 32 − 24 = **8** and 48 + 24 = **72**. The minimum (16) and maximum (64) are inside, so **no outliers**. Westside: IQR = 34 − 17 = 17; fences 17 − 25.5 = **−8.5** and 34 + 25.5 = **59.5**. The maximum, 96, is above 59.5, so Westside has **at least one high outlier**. The table cannot say whether any other Westside value is above 59.5, only that the maximum is.

**2.** Not really. The **IQRs are 16 and 17, almost equal**. Westside's standard deviation and range are inflated by the 96-hour member, and both are nonresistant. With an outlier or strong skew in either group, compare **medians and IQRs**. That is the resistance lesson from Part 3, applied to a comparison.
:::

:::yourturn
Now write the full comparison of the two branches: centre, variability, shape and outliers, in context, with a comparative word in every sentence.
:::

:::reveal Reveal — model comparison
> *"The median time spent in the library is higher at Central (40 hours) than at Westside (24.5 hours). The middle half of members is about equally spread at the two branches (IQR 16 hours at Central, 17 at Westside), although Westside has the larger standard deviation and range, largely because of one member who spent 96 hours. Central's distribution is roughly symmetric (mean and median both 40, and Q1 and Q3 each 8 hours from the median), while Westside's is skewed right (mean 28.0 above median 24.5, and a longer upper tail). Westside has a high outlier at 96 hours; Central has none."*

![Parallel boxplots of hours spent in the library, Central and Westside](figures/s03-boxplot-library.svg)

*The same two branches drawn from the raw data. Westside's upper whisker ends at 55, the largest value that is not an outlier. The summary table alone could not tell you where it stops, only that 96 is beyond the fence.*

Check your own against the same list as the hospital comparison: centre, variability, shape with evidence, outliers for both, comparative words, context.
:::

:::yourturn
The library service says: *"Central's members spend more time in the library."* Is that supported? Quote a comparison of positions, and say what the data do not show.
:::

:::reveal Reveal — the library claim
**Supported.** Central's **Q1 (32 hours) is above Westside's median (24.5 hours)**, so at least three quarters of the Central sample spent longer than half of the Westside sample. In the data, 32 of 35 Central members (91.4%) spent more than 24.5 hours, against 15 of 30 at Westside.

**What it does not show:** why. The branches may serve different neighbourhoods, and nobody was assigned to a branch.
:::

---

## Part 6 — On your own: the café

No hints and no reveals until all four are done. It is the same café as Session 2's solo case.

Drinks sold per hour over 20 opening hours:

```
14  16  17  19  20  21  21  22  23  24
24  25  26  27  28  30  31  33  35  52
```

:::yourturn
1. Find the five-number summary.
2. Use the 1.5 × IQR rule to identify any outliers. Show the fences.
3. Draw the boxplot.
4. The mean is 25.4 and the standard deviation 8.39. Which measures of centre and spread would you report for these data, and why?
:::

:::reveal Reveal — the café
**1.** *n* = 20 is even, so no value is left out and each half has 10. Median = (24 + 24) ÷ 2 = **24**. Lower half 14 16 17 19 **20 21** 21 22 23 24 gives Q1 = (20 + 21) ÷ 2 = **20.5**. Upper half 24 25 26 27 **28 30** 31 33 35 52 gives Q3 = (28 + 30) ÷ 2 = **29**. Five-number summary: **14, 20.5, 24, 29, 52**.

**2.** IQR = 29 − 20.5 = 8.5, and 1.5 × 8.5 = 12.75. Fences: 20.5 − 12.75 = **7.75** and 29 + 12.75 = **41.75**. **52 is an outlier**; nothing is below 7.75.

**3.**

![Boxplot of drinks sold per hour at the café, 52 marked as an outlier](figures/s03-boxplot-cafe.svg)

Box from 20.5 to 29, median at 24, whiskers to 14 and to **35**, and 52 marked separately.

**4.** The **median (24) and IQR (8.5)**. There is a high outlier and the distribution is skewed right; the mean (25.4) is above the median because the 52 pulls it up, and the standard deviation is inflated by it too.

**Check yourself against the three classic slips:**

- Did the right whisker go to 52, or to 41.75? It ends at 35.
- Did you take Q1 as the 5th value (20) instead of the mean of the 5th and 6th?
- Did you choose the mean "because it uses all the data"? That is true, and it is exactly why an outlier drags it.
:::

---

## Part 7 — Explain it back

:::yourturn
Close the booklet. Explain out loud, or in writing, as if to someone who missed the session: **why did the median not move when the 68-minute journey became 118, and why did the fence not move either?**
:::

:::reveal Reveal — what a good explanation contains
A good explanation has three parts. The median is the 13th value, and making the largest value larger does not change which value is 13th. The fences are built from Q1 and Q3, which are positional in the same way. The mean adds up every value, so an extra 50 minutes over 25 students raises it by 2.

If you said *"because the median is resistant"* and stopped, you have the word but not the reason, and an unfamiliar exam question will need the reason. Tell your tutor at the start of Session 4 if this part did not come out cleanly.
:::

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
