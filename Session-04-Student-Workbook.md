# Session 4 — Two Variables: Scatterplots and Correlation

**AP Statistics · Twenty-Hour Course · Student edition, to work through on your own**
**CED Topics 5.1, 5.2 · About 140 minutes, plus homework**

---

## How to use this

The same rule as every session so far, and today you will draw more than you calculate.

:::note amber Write first, then reveal
Every **Your turn** box asks you to do something before the text shows you the answer. **Do it on paper first.** The scatterplot, the descriptions, the sketches and the answers to every claim are hidden behind reveals so that you cannot copy them. A scatterplot you have drawn yourself, with a point in the wrong place, teaches you more than a perfect one you looked at.
:::

**What you need:** paper, a pen, a ruler, and a calculator. Graph paper helps for Part 3. A TI-84 or any calculator that does linear regression will give you *r*.

### How this maps to your tutor's document

Working alone with a pen is slower than working with a tutor, so each part is given about a quarter longer than the tutor's segment. Take the time: the writing is the learning.

| Your section | Tutor's section | Minutes |
|---|---|---|
| Part 1 — Your Session 3 homework, and a warm-up | 0–10 Homework debrief and diagnostic | 12 |
| Part 2 — Why this matters | (the framing) | 3 |
| Part 3 — Lincoln High: distance and journey time | 10–55 Scenario A | 56 |
| Part 4 — Sketch and Switch, on your own | 55–72 Activity | 21 |
| Part 5 — St Mary's evening shifts | 72–92 Scenario B | 25 |
| Part 6 — On your own: the library | 92–102 Solo case | 13 |
| Part 7 — Explain it back | 102–110 Teach it back | 8 |
| **Total** | **110 minutes** | **138** |

If your tutor has not yet set the **Session 2 test**, take it before Part 1: 40 minutes, timed, answer key closed.

---

## Part 1 — Your Session 3 homework, and a warm-up

Get out your marked Session 3 homework and make two lists: the questions you got **wrong**, and the questions you marked with a **?**, including the ones that turned out right.

**Two specific things to check.** They are two of the likeliest errors on that sheet, and both come back today.

- **E3: did you describe each school separately?** "Lincoln High's median is 18. Oakfield's median is 14.5." Two descriptions are not a comparison. Today the same habit appears in a new form: describing two variables one at a time ("distance goes from 0.5 to 28 km, time from 8 to 68 minutes") says nothing about how they relate. The sentence that earns marks links them: *students who live further away tend to have longer journeys.*
- **F2: did you choose Priya?** Her 38 minutes is longer than Sam's 26, but Sam's journey is 2.20 standard deviations above his school's mean and Priya's only 1.45 above hers. If you compared raw minutes, re-read that answer now: today's correlation coefficient is built out of z-scores, and it will only make sense if you trust them.

### Warm-up

:::yourturn
Four questions. Answer all four on paper before revealing.

1. In winter, as the outside temperature rises, a household's heating bill tends to fall. Is that a positive or a negative association?
2. A teacher records hours of revision and test score for 30 students. Which variable would you put on the horizontal axis, and why?
3. Over a summer, ice-cream sales and shark attacks both go up. Do ice-cream sales cause shark attacks?
4. A journey has a z-score of −1.5. What does that tell you about it?
:::

:::reveal Reveal — and what your answers mean
| If you said | It means | Do this |
|---|---|---|
| **1:** negative | Correct: as temperature rises, the bill tends to fall | Carry on |
| **1:** positive, "because they're related" | You are using *positive* to mean *there is a relationship* | Positive means as one increases the other **tends to increase**; negative means it **tends to decrease**. Part 3 practises it |
| **2:** revision, because it affects the score | Correct idea: revision is the **explanatory** variable | Part 3 gives it its name and its axis |
| **2:** "it doesn't matter" or the score | No convention yet | Expected. Part 3's first question is exactly this |
| **3:** no, hot weather drives both | You already see a third variable at work | Part 5 builds on it and names it |
| **3:** yes, they go up together | You are treating "go together" as "cause" | That is the whole of Part 5. Read it slowly |
| **4:** 1.5 standard deviations below the mean | Session 3 has held | Carry on |
| **4:** 1.5 minutes below average, or blank | z-scores have not landed | Redo Session 3's homework F1 before Part 3's correlation section |

Question 3 is the course description's own: it is one of the essential questions for this unit.
:::

---

## Part 2 — Why this matters

Until now you have looked at one variable at a time. Today every individual gives you **two** numbers, and the question is whether they move together.

That question produces the most common reasoning error in statistics: seeing two things move together and concluding that one causes the other. It also produces a quieter error, trusting a single number, the correlation *r*, without looking at the picture it came from. Parts 4 and 5 are built to break both habits.

---

## Part 3 — Lincoln High: distance and journey time

The same 25 randomly chosen Lincoln High students whose journey times you summarised in Sessions 2 and 3. The survey also asked each of them how far they live from school.

Distance from school (km) and journey time (minutes), in the order of the journey times from Session 3:

```
 km   min    km   min    km   min    km   min    km   min
 0.5    8    1.0    9    1.0   10    1.5   11    2.0   12
 1.5   12    2.5   13    3.0   14    4.5   15    3.5   15
 4.0   16    4.5   17    7.0   18    5.5   18    6.0   20
 6.5   21    5.0   22    7.5   24    8.0   25    9.5   27
11.0   30    2.5   33   14.0   36   17.0   42   28.0   68
```

### Two variables, one student each

:::yourturn
Each student gave two numbers. Which one do you think helps explain the other? Which would you put on the horizontal axis?
:::

:::reveal Reveal — explanatory and response
**Distance** helps explain **journey time**: living further away is a reason a journey might take longer.

- The **explanatory variable** explains or predicts the other. It goes on the **x-axis**: distance.
- The **response variable** is the one being explained or predicted. It goes on the **y-axis**: journey time.

Data like these, two quantitative variables measured on the **same individuals**, are called **bivariate quantitative data**. Each student gives one ordered pair, such as (2.5, 33).

The convention matters because every description you write depends on it: *as distance increases, journey time tends to*…. Swap the axes and that sentence is about something else.
:::

### Build the scatterplot

A **scatterplot** shows one point for each individual, with the explanatory variable across and the response variable up.

:::yourturn
Draw the scatterplot by hand. Use an x-axis from 0 to 30 km and a y-axis from 0 to 70 minutes, and label both with the variable **and its units**. Plot all 25 students.

Before you start: where will the student with the 68-minute journey go?
:::

:::reveal Reveal — the scatterplot
![Scatterplot of distance from school and journey time for 25 Lincoln High students](figures/s04-scatter-commute.svg)

*Each dot is one student. The orange dot is the student who lives 2.5 km away and took 33 minutes. The student in the top right is the 68-minute journey from Session 3.*

Check your plot against this one point by point. Two to look at closely: (1.5, 12), which sits just left of (2.0, 12), and (7.0, 18), which is lower than its neighbours.
:::

### Describe the association

A description of a scatterplot covers four things: **direction, unusual features, form and strength**.

| Feature | What it asks |
|---|---|
| **Direction** | As x increases, does y **tend to** increase (positive) or decrease (negative)? |
| **Unusual features** | Are there points that don't fit the general pattern, or clusters? |
| **Form** | Is the pattern linear (straight) or non-linear (it bends)? |
| **Strength** | How closely do the points follow the pattern: strong, moderate or weak? |

:::yourturn
Two questions before the full description.

1. In Session 3, the 68-minute journey was an outlier. **Is it unusual in this scatterplot?**
2. Is any student unusual here? Which, and why?
:::

:::reveal Reveal — the 68-minute journey, and the student who doesn't fit
**1. No.** That student lives 28 km away, further than anyone. Cover the point with your finger and follow the other points up and to the right: the pattern leads straight to it. It is far from the other points, but it **fits** the pattern.

**2. The student at 2.5 km who took 33 minutes.** The other three students who live 2 to 3 km away took 12 to 14 minutes. She is about 20 minutes off the pattern.

This is the trap of the session. In a scatterplot, **unusual features** are clusters or points that **don't fit the general pattern**. That is judged against the pattern, not against one axis. The numbers prove it:

- For distance, Q1 = 2.25, Q3 = 7.75 and IQR = 5.5, so the 1.5 × IQR fences are −6.0 and 16.0 km. **17 and 28 km are outliers** for distance.
- For time, Session 3's fences were −7.75 and 46.25 minutes, so **68 is an outlier** for time.

The 28 km, 68-minute student is an outlier in **both** variables and fits the pattern. The 2.5 km, 33-minute student is inside **all four** fences and is the one point that does not fit.

*In a scatterplot, a point is unusual if it does not fit the pattern of the others. Being the largest value of one variable does not make it unusual, and being ordinary in both variables does not make it typical.*
:::

:::yourturn
Now write the full description of the association between distance and journey time: direction, unusual features, form and strength, **in context**.
:::

:::reveal Reveal — a model description
> *"There is a **strong, positive, linear** association between distance from school and journey time for these 25 students: students who live further from school **tend to** have longer journeys. One student **does not fit the pattern**: she lives 2.5 km away but took 33 minutes, while the other three students living 2 to 3 km away took 12 to 14 minutes. The student with the longest journey, 68 minutes, lives furthest away, 28 km, and fits the pattern."*

Check yours against three common losses:

- **"It's positive" and nothing more.** The course description says writing generally about direction is typically not enough. Say what positive *means* here: further away tends to mean longer.
- **"It's linear because it's a line."** That is named in the course description as a common error. The evidence is that journey time rises by roughly the same amount for each extra kilometre, all the way along, with no bend.
- **No context.** Every sentence should mention distance, journey time or the students.
:::

### Justify a claim

:::yourturn
The head of year says: *"Every student who lives more than 10 km away takes at least half an hour to get to school, but almost nobody closer does."* Use the scatterplot to decide whether the claim is supported. Quote numbers.
:::

:::reveal Reveal — the claim
**Supported, for these 25 students.** All **4** students living more than 10 km away (11, 14, 17 and 28 km) took at least 30 minutes (30, 36, 42 and 68). Of the **21** living within 10 km, only **1** took 30 minutes or more: the 33-minute student at 2.5 km.

What it does not establish: that the same holds for every Lincoln High student. The 25 were chosen at random, which helps, but 4 students is a small group to generalise from. The template is the same as in every session: **state the claim · quote the numbers · say what they do and do not establish · keep it in context.**
:::

### Correlation: one number for a linear association

The **correlation coefficient, r**, summarises the **strength and direction of the linear association** between two quantitative variables. The course expects you to find it with **technology**.

On a TI-84: enter the distances in L1 and the times in L2, then STAT → CALC → LinReg(a+bx). If *r* does not appear, turn on Stat Diagnostics (on the MODE screen on newer models, or DiagnosticOn from the catalogue on older ones). Ignore *a* and *b* until Session 5.

:::yourturn
Find *r* for the 25 students with your calculator. Then put it into one sentence about these students.
:::

:::reveal Reveal — r for the journeys
**r = 0.95.**

*"There is a strong, positive linear association between distance from school and journey time."*

If you wrote "95% of the journey time is explained by distance", that is a different number, *r*², and it belongs to Session 5. If you wrote "distance causes the journey time", *r* cannot tell you that: it measures how closely the points follow a line, not why. Part 5 is about exactly this.
:::

What the course states about *r*:

| Fact | What it means here |
|---|---|
| −1 ≤ *r* ≤ 1, always | 0.95 is near the top of the scale |
| The sign gives the direction | positive: further away, longer journey |
| Strength is how close *r* is to −1 or 1 | 0.95 is close to 1: strong |
| *r* = 0 means **no linear** association | not "no association"; Part 4 shows the difference |
| *r* = 1 or −1 means a **perfect** linear association | every point exactly on a line |
| *r* is unit-free | it does not care about kilometres or minutes |

:::note amber A rough guide to the words, not a rule
The course description gives no cut-offs. This course uses: **|r| of about 0.8 or more, strong; about 0.5 to 0.8, moderate; below about 0.5, weak**. The course description's own sample question describes r = −0.591 as "moderate and negative", which fits. But strength belongs to the scatterplot first: always look at the plot.
:::

### Where r comes from: z-scores

The exam's formula sheet gives *r* in this form. Look at the two brackets: **each one is a z-score**, as in Session 3.

:::formula
r = (1 ÷ (n − 1)) × Σ [ (xᵢ − x̄) ÷ sₓ ] × [ (yᵢ − ȳ) ÷ s_y ]
:::

So *r* is, near enough, **the average product of the z-scores**: turn every distance and every time into a z-score, multiply each student's pair, add up, and divide by *n* − 1. You will find *r* with technology in the exam, but working it once by hand shows why it behaves as it does.

:::yourturn
Five of the 25 students. Their journey times are the five from Session 3's worked example, **10, 14, 18, 22, 36 minutes**, with mean 20 and *s* = 10. Their distances are **1, 3, 7, 5, 14 km**, in the same order.

1. Find the mean and standard deviation of the five distances.
2. Make a table: distance, its z-score, time, its z-score, and the product of the two z-scores.
3. Add the products and divide by *n* − 1 to get *r*.
:::

:::reveal Reveal — r by hand for five students
**1.** *x̄* = 30 ÷ 5 = **6 km**. Deviations −5, −3, 1, −1, 8; squares 25, 9, 1, 1, 64, total 100; *s*² = 100 ÷ 4 = 25; *s*ₓ = **5 km**.

**2.**

| km | *z* for distance | min | *z* for time | product |
|---|---|---|---|---|
| 1 | (1 − 6) ÷ 5 = −1.0 | 10 | (10 − 20) ÷ 10 = −1.0 | +1.00 |
| 3 | −0.6 | 14 | −0.6 | +0.36 |
| 7 | +0.2 | 18 | −0.2 | −0.04 |
| 5 | −0.2 | 22 | +0.2 | −0.04 |
| 14 | +1.6 | 36 | +1.6 | +2.56 |
| **Total** | | | | **3.84** |

**3.** *r* = 3.84 ÷ (5 − 1) = **0.96**.

![The five students plotted as z-scores, with the product of z-scores for each](figures/s04-z-products.svg)

*Each student plotted by their two z-scores. Above the mean on both, or below on both: a positive product. Above on one and below on the other: a negative product.*

The two negative products belong to the students who are above the mean on one variable and below on the other: 7 km but a below-average time, and 5 km but an above-average time. For *r* to be near 0, the points would have to be spread across all four corners, so that positive and negative products cancel.

If you got **0.768**, you divided by *n* = 5 instead of *n* − 1 = 4.
:::

### r has no units

:::yourturn
The principal wants distances in **miles** and times in **hours**. What happens to *r* = 0.95? Explain using z-scores.
:::

:::reveal Reveal — unit-free
**Nothing: r stays 0.95.**

Changing units divides every value, the mean and the standard deviation by the same number, so every z-score is unchanged (Session 3's changing-units rule). The formula uses only z-scores, so *r* is unchanged. The same happens if every time is corrected for a clock that ran 3 minutes fast: subtracting 3 moves the mean by 3 and leaves the standard deviation and the z-scores alone.

That is what the course means by *r* is **unit-free**.
:::

### Guess the correlation

:::sim guess-correlation | Guess the Correlation | 900
Play five rounds on **Linear only**, at 40 points, then one at **15 points**. Set your guess with the slider before you check it; the point is to be wrong and see by how much. Leave **Include non-linear and clusters** until after Part 4.
:::

If every one of your misses is in the same direction, notice it. A common early error is to underestimate strong correlations: a cloud that looks loose can have *r* = 0.8.

---

## Part 4 — Sketch and Switch, on your own

In the classroom version of this activity, students sketch a scatterplot from a verbal prompt, then swap papers and check each other's sketch against the words. The course description's own example prompt is a "weak negative, non-linear association".

### Round 1: sketch from the words

:::yourturn
Sketch four small scatterplots. Label the axes *x* and *y*; no scale is needed.

- **P1** Weak negative, non-linear association
- **P2** Strong positive linear association, with one point that does not fit the pattern
- **P3** Moderate negative linear association
- **P4** No association
:::

:::reveal Reveal — model sketches
![Model sketches for the four Sketch and Switch prompts](figures/s04-sketch-models.svg)

*P1 falls steeply, then levels off, and its points are loose. P2's odd point sits below the band in the middle, not at the end. The r values are given only for the two linear prompts: for P1, a non-linear pattern, r does not measure the strength of the pattern at all.*

| If your sketch | Check this word |
|---|---|
| P1 is a straight falling band | **non-linear**: it needs a bend |
| P1 is a tight curve | **weak**: the points should be loose around it |
| P2's odd point is at the far end of the band | **does not fit**: far along the pattern is still on it, like the 68-minute journey |
| P3 is as tight as P2 | **moderate**: clearly visible, with a lot of scatter |
| P4 is a flat horizontal band | that is correct: y does not change as x changes. A shapeless cloud is also correct |
:::

### Round 2: switch, and check a partner's sketches

Your partner was given four prompts and drew these. The orange point in (d) is the one they meant as unusual.

![Four sketches drawn by a partner, each with the prompt they were given](figures/s04-sketch-partner.svg)

*Each sketch is labelled with the prompt the partner was given.*

:::yourturn
Which sketches match their prompts? For each one that does not, name the word in the prompt that the partner got wrong.
:::

:::reveal Reveal — the review
| Sketch | Matches? | Why |
|---|---|---|
| (a) strong negative linear | **No** | Too loose to be strong: it is **moderate** (r = −0.62) |
| (b) weak positive linear | **Yes** | Weak, positive, linear (r = 0.30) |
| (c) moderate positive, non-linear | **No** | A **strong** and **linear** pattern, not moderate and not curved (r = 0.96) |
| (d) strong positive linear, with a point that does not fit | **No** | The orange point is far out, but **on** the pattern. Cover it and follow the others: they lead to it |

(d) is the same trap as the 68-minute journey. A point that does not fit has to be off the pattern, not merely at the end of it.
:::

### The question that makes this topic 5.2

:::yourturn
Sketch a **strong** association whose correlation *r* is **close to 0**. If you think it cannot be done, say why.
:::

:::reveal Reveal — the café
It can be done: a strong curve that goes down and then up, a U-shape.

The café from Sessions 2 and 3 recorded the midday temperature outside on the same 10 days as in Session 3, and the number of drinks it sold each day, all drinks together and iced drinks alone.

| Midday temperature (°C) | 12 | 14 | 15 | 15 | 16 | 18 | 19 | 21 | 22 | 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| All drinks sold | 257 | 225 | 208 | 206 | 199 | 185 | 186 | 181 | 187 | 259 |
| Iced drinks sold | 9 | 11 | 13 | 16 | 20 | 31 | 44 | 64 | 74 | 167 |

![Café: midday temperature against all drinks sold and against iced drinks sold, 10 days](figures/s04-cafe.svg)

*Left: all drinks. Sales are highest on the coldest day (257) and the hottest (259) and lowest in between (181 at 21 °C), a clear U-shape with r = −0.01. Right: iced drinks alone, a strong curve with r = 0.96.*
:::

:::yourturn
Two claims about the café. Respond to each, using the scatterplots.

1. The manager ran the correlation for all drinks against temperature, got *r* = −0.01, and concluded: *"The weather makes no difference to how many drinks we sell."*
2. A colleague says: *"For iced drinks, r = 0.96, so iced sales rise in a straight line with temperature."*
:::

:::reveal Reveal — what r measures
**1. The manager is wrong.** Temperature matters a lot: cold days and hot days are busy, mild days are quiet. The association is **strong and non-linear**. *r* measures only **linear** association, and *r* = 0 means **no linear association**, not no association.

Why is it near 0? The cold, busy days are below the mean temperature and above the mean sales, so their z-score products are negative. The hot, busy day is above on both, a positive product. They cancel.

**2. The colleague is wrong.** The points bend upwards: iced sales rise slowly at first and then fast. A correlation close to −1 or 1 **does not necessarily mean a linear model is appropriate**.

*r measures the strength and direction of a linear association only. An r near 0 can hide a strong curve, and an r near 1 can belong to a curve. Look at the scatterplot before you trust r.*
:::

Now go back to **Guess the Correlation** in Part 3, switch on **Include non-linear and clusters**, and play three or four rounds. The feedback names each non-linear pattern as it appears.

---

## Part 5 — St Mary's evening shifts

Back to Session 1's hospital survey and St Mary's. The hospital's own records for 20 evening shifts give, for each shift, the number of **doctors on duty** and the **mean waiting time**, in minutes, of the patients seen that shift.

```
Shift  Doctors  Mean wait    Shift  Doctors  Mean wait
  1       3        23          11      5        38
  2       4        27          12      5        36
  3       3        35          13      5        38
  4       3        36          14      7        34
  5       4        30          15      6        46
  6       5        31          16      7        47
  7       5        28          17      7        49
  8       5        35          18      8        40
  9       5        35          19      8        44
 10       4        41          20      8        47
```

**One new point: the individuals are shifts, not patients.** Each dot on the scatterplot is one evening, and its mean wait summarises dozens of patients.

![St Mary's, 20 evening shifts: doctors on duty against mean wait](figures/s04-hospital-doctors.svg)

*Doctors on duty is a whole number, so the points line up in columns.*

:::yourturn
Describe the association between doctors on duty and mean waiting time: direction, unusual features, form, strength, in context. Technology gives *r* = 0.68.
:::

:::reveal Reveal — the description
*"There is a **moderate, positive**, roughly **linear** association between the number of doctors on duty and the mean waiting time: shifts with more doctors on duty **tended to** have longer mean waits. No shift stands far off the pattern. r = 0.68."*

If you said **strong**, compare it with the journeys: there is a lot of scatter here. Shifts with 5 doctors ranged from 28 to 38 minutes. 0.68 fits *moderate* on the course's rough guide.
:::

### The claim

The department manager has seen the same plot:

> *"Our shifts with more doctors have longer waits, r = 0.68. Extra doctors are slowing the department down. We can cut evening staffing without making waits any worse."*

:::yourturn
1. Is the manager's claim supported? Why or why not?
2. Think about a shift with 3 doctors and one with 8. What else is probably different about those two evenings?
:::

:::reveal Reveal — what else changes from shift to shift
**1. No.** The plot shows that more doctors and longer waits **go together** on these shifts. It does not show that one causes the other. The course states it as a rule: a perceived or real relationship between two variables does not mean that changes in one cause changes in the other. **Correlation does not necessarily imply causation.**

**2. How busy they are.** The rota puts more doctors on the evenings it expects to be busy, and busy evenings have longer waits. The records have it: the number of **patients arriving** during each shift. The shifts in the table are numbered in order of it:

| Shift | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Arrivals | 26 | 34 | 36 | 39 | 40 | 44 | 46 | 48 | 50 | 52 |

| Shift | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| Arrivals | 54 | 55 | 56 | 59 | 67 | 70 | 73 | 74 | 75 | 77 |

![St Mary's, 20 evening shifts: patients arriving against doctors on duty](figures/s04-hospital-arrivals.svg)

*Busier shifts had more doctors on duty (r = 0.93).*

Patients arriving is strongly associated with doctors on duty (**r = 0.93**) and with mean wait (**r = 0.88**). That one variable explains the whole pattern: busy evenings get more doctors **and** longer waits.

A variable like this is a **confounding variable**: it provides another explanation for the association, and it is associated with **both** variables. You will study it properly in Session 6.
:::

:::yourturn
Look only at the five shifts with a similar load, 50 to 56 patients (shifts 9 to 13). What do they suggest about doctors and waiting time?
:::

:::reveal Reveal — holding the busyness roughly still
| Arrivals | 50 | 52 | 54 | 55 | 56 |
|---|---|---|---|---|---|
| Doctors | 5 | **4** | 5 | 5 | 5 |
| Mean wait (min) | 35 | **41** | 38 | 36 | 38 |

Among shifts that were about equally busy, the one with **fewer** doctors had the **longest** wait: the opposite of the manager's story. Five shifts cannot settle anything, and these are records, not an experiment. But it shows how the same data can point the other way once the confounding variable is held roughly still.
:::

:::yourturn
Which of these statements do the data support? Decide for each before revealing.

1. "On these 20 shifts, more doctors on duty was associated with longer mean waits."
2. "Extra doctors cause longer waits."
3. "Cutting doctors will not make waits worse."
4. "To find out what extra doctors do to waits, the hospital would need to change staffing deliberately and compare."

Then write a short reply to the manager.
:::

:::reveal Reveal — what the data can and cannot support
| Statement | Supported? |
|---|---|
| 1 | **Yes**: that is what the plot and *r* = 0.68 describe |
| 2 | **No**: an association in observational records; busier evenings explain both |
| 3 | **No**: it is a claim about what *would* happen after a change nobody made |
| 4 | **Yes**, and that is Session 7's experiments |

> *"The data show that shifts with more doctors tended to have longer waits (r = 0.68), but this does not show that doctors cause the waits. Busier shifts had both more doctors (r = 0.93 between arrivals and doctors) and longer waits (r = 0.88 between arrivals and waits), so the number of patients arriving is a confounding variable that could explain the association. These are observational records, so they cannot show what cutting staff would do."*

Now look back at the warm-up's Question 3. Ice-cream sales and shark attacks: hot weather drives both. Same structure, and now you can name the parts.
:::

---

## Part 6 — On your own: the library

No hints and no reveals until all four are done. The library service from Sessions 1 and 3: the same 35 randomly chosen members of the Central branch whose hours in library buildings you summarised last session, now with the number of items each borrowed last year.

![Central library members: hours in library buildings against items borrowed, 35 members](figures/s04-library.svg)

*Hours spent in library buildings and items borrowed last year, 35 Central branch members.*

:::yourturn
1. Which variable would you treat as explanatory, and which as response? Why?
2. Describe the association, in context.
3. Technology gives *r* = 0.40. A librarian says: "r is only 0.40, so time in the library has only a weak relationship with borrowing." Do you agree? Explain.
4. A councillor says: "If we can get members to spend more time in the library, they will borrow more." Does the scatterplot support this?
:::

:::reveal Reveal — the library
**1.** **Hours** explanatory and **items borrowed** response is the natural choice: the question is whether time spent there goes with borrowing more. The reverse can be defended if you argue it; say which, and why.

**2.** *"For most members there is a **strong, positive, linear** association between hours spent in library buildings and items borrowed: members who spent more hours tended to borrow more items, from 4 items at 16 hours to 33 to 37 items at 54 to 64 hours. A **cluster** of five members who spent 49 to 56 hours borrowed only 2 to 6 items each, far below the pattern of the others."*

**3. Disagree, at least with the conclusion.** *r* = 0.40 summarises all 35 members together, and the five members in the cluster do not follow the pattern, which makes the overall linear association weaker. For the other members the pattern is strong. The honest summary names both: a strong positive pattern for most members, and a separate group who spend a lot of time and borrow little.

**4. No.** This is an association in a sample of members, not an experiment: nobody was made to spend more time. Members who choose to spend more time may be keener readers anyway. And the cluster is five members who spend a great deal of time and borrow almost nothing, perhaps using the study space, which the councillor's claim ignores.

**Check yourself against the four classic slips:**

- Did you call the association **negative** because the cluster is low? Direction is about the trend of the whole, not one group.
- Did you call the cluster "outliers" and stop? It is a **group** of five, and a description should say so.
- Did you agree with the librarian "because 0.40 is weak"? That is reading the number without the plot, the exact habit Part 4 was built to break.
- Did you support the councillor "because r is positive"? A positive *r* describes an association, not a cause.
:::

---

## Part 7 — Explain it back

:::yourturn
Close the booklet. Explain out loud, or in writing, as if to someone who missed the session: **why was r for the café's total drinks almost 0, even though temperature clearly mattered? And what does r measure?**
:::

:::reveal Reveal — what a good explanation contains
A good explanation has three parts. *r* measures the strength and direction of a **linear** association only. For the U-shape, the busy cold days sit below the mean temperature and above the mean sales, so their z-score products are negative, while the busy hot day is above on both and gives a positive product; they cancel, so the total is near 0. And therefore you have to look at the scatterplot before you trust *r*: a strong curve can have *r* near 0.

If you said *"because the relationship is weak"*, go back to the café scatterplot in Part 4 and ask yourself whether it is weak. Tell your tutor at the start of Session 5 if this part did not come out cleanly.
:::

---
---

# Homework — Session 4

**40 marks · bring to Session 5, self-marked**

## How to do this homework

1. Do every part **with the answer key closed.** Where you are unsure, answer anyway and put a **?** beside it.
2. Then open the key and **mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote.
3. **Bring the marked sheet.** Your wrong answers and your question marks are what Session 5 opens with.

Everything here was taught in the session; this sheet is practice. You need graph paper or a ruler for B2, and a calculator. Where a question gives you *r*, it was found with technology, as the course expects.

---

## Part A — Vocabulary (6 marks)

Match each term to its meaning.

| | Term | | Meaning |
|---|---|---|---|
| 1 | Explanatory variable | A | How closely the points in a scatterplot follow the general pattern |
| 2 | Response variable | B | Linear or non-linear |
| 3 | Positive association | C | The variable on the y-axis, whose values are explained or predicted |
| 4 | Form | D | A unit-free number between −1 and 1 that summarises the strength and direction of a linear association |
| 5 | Strength | E | The variable on the x-axis, used to explain or predict the other |
| 6 | Correlation coefficient, *r* | F | As one variable increases, the other tends to increase |

## Part B — Oakfield School's journeys (10 marks)

In Session 3's homework you summarised the journey times of 20 Oakfield School students. Twelve of them also gave their distance from school:

```
 km   min    km   min    km   min    km   min
 1.0    6    2.4    9    2.6   11    3.4   12
 3.0   13    4.2   14    3.8   15    4.6   17
 6.0   19    5.6   21    7.6   26    6.8   38
```

**B1.** Which variable is the explanatory variable and which is the response? (1)

**B2.** Construct a scatterplot. Label both axes with the variable and its units. (3)

**B3.** Describe the association. Your answer must address direction, unusual features, form and strength, in context. (4)

**B4.** Technology gives *r* = 0.88.
(a) Interpret this value in context. (1)
(b) In Session 3, the 38-minute journey was an outlier by the 1.5 × IQR rule. Explain why it is also unusual in the scatterplot, and why the reason is different. (1)

## Part C — Reading r (6 marks)

![Four scatterplots, A to D, for matching to correlation values](figures/s04-hw-c.svg)

*Four scatterplots of 30 points each. The axes have no units because r has none.*

**C1.** The four correlations are *r* = −0.93, −0.52, 0.05 and 0.78. Match each plot to its correlation. (4)

**C2.** True or false? Give a reason for each. (2)
(a) "If the Oakfield distances in Part B were measured in miles instead of kilometres, *r* would be smaller than 0.88."
(b) "*r* = −0.93 shows a weaker association than *r* = 0.78, because −0.93 is the smaller number."

## Part D — r from z-scores (6 marks)

On five spring mornings the café recorded the temperature at 8 am and the number of hot drinks it sold between 7 and 10 am:

```
Temperature (°C)     8    12    16    19    20
Hot drinks sold    175   160   155   125   135
```

For the hot drinks, ȳ = 150 and *s_y* = 20.

**D1.** Calculate the mean and the standard deviation of the five temperatures. Show your working. (2)

**D2.** Make a table with columns: temperature, its z-score, hot drinks, its z-score, and the product of the two z-scores. (2)

**D3.** **State the formula**, then calculate *r*. (1)

**D4.** Interpret your value of *r* in context. (1)

## Part E — Computers and visitors (6 marks)

The library service collected data on its 18 branches: the number of public computers in each branch and its number of visits in a typical week. The scatterplot shows a positive, linear pattern with *r* = 0.83. A council report says:

> *"Branches with more public computers get more visitors. If we install more computers in our quieter branches, their visits will rise."*

**E1.** What does *r* = 0.83 tell you about these 18 branches? (1)

**E2.** Does the association show that installing computers causes more visits? Explain. (2)

**E3.** Name a variable that could explain the association, and explain how it could be related to **both** the number of computers and the number of visits. (2)

**E4.** Rewrite the first sentence of the report's claim so that it says only what the data support. (1)

## Part F — What r cannot tell you (6 marks)

![F1: age against items borrowed; F2: minutes since switched on against water temperature](figures/s04-hw-f.svg)

*F1: 20 library members' ages and the number of items each borrowed last year. F2: the café's coffee machine, the water temperature at 14 times after it was switched on.*

**F1.** For the library members, *r* = −0.01. A library assistant concludes: "Age has nothing to do with how much people borrow." Respond, using the scatterplot. (2)

**F2.** For the coffee machine, *r* = 0.88. The café manager says: "r is close to 1, so the water heats up at a steady rate, and a straight line describes it well." Respond, using the scatterplot. (2)

**F3.** Sketch a scatterplot with a **moderate negative linear association and one point that does not fit the pattern.** Mark the point that does not fit. (2)

---
---

# Answer key

*For the student to mark their own work, after attempting everything.*

### Part A (6 marks, 1 each)

1–E · 2–C · 3–F · 4–B · 5–A · 6–D

### Part B (10 marks)

**B1.** (1) **Distance** is the explanatory variable and **journey time** the response: distance helps explain how long a journey takes.

**B2.** (3) One mark for the axes: distance (km) on the x-axis and journey time (minutes) on the y-axis, both labelled with units. One mark for sensible scales. One mark for all 12 points plotted correctly.

:::reveal Reveal — the B2 scatterplot, after you have drawn yours
![Oakfield School: distance from school against journey time, 12 students](figures/s04-oakfield.svg)

*The answer to B2. The orange point is the 38-minute journey at 6.8 km.*
:::

**B3.** (4) One mark each for direction, unusual features, form and strength, in context. A model answer:

> *"There is a strong, positive, linear association between distance from school and journey time for these 12 Oakfield students: students who live further away tend to have longer journeys. One student does not fit the pattern: at 6.8 km, their journey took 38 minutes, while the students living 5.6 to 7.6 km away took 19 to 26 minutes."*

> **"Positive" on its own does not earn the direction mark.** Say what it means: students who live further away *tend to* take longer. If you wrote "it goes up in a line", the form mark needs evidence, not the word *line*: journey time rises at a roughly steady rate as distance increases.

**B4.** (2)
(a) (1) *"There is a strong, positive linear association between distance from school and journey time for these 12 students."*
(b) (1) In Session 3 the 38-minute journey was unusual because it was far above the other **journey times**. In the scatterplot it is unusual because it does not fit the **pattern**: for a student living 6.8 km away, 38 minutes is far longer than the pattern of the other students suggests. A scatterplot judges a point against the relationship, not against one variable.

### Part C (6 marks)

**C1.** (4, 1 each) **A: 0.78 · B: −0.93 · C: 0.05 · D: −0.52.**

> The pair that trips people up is B and D: both fall, and the difference is only how tightly the points follow the line. If you swapped A and D, check the direction first: A rises, D falls.

**C2.** (2)
(a) (1) **False.** *r* is unit-free. Changing kilometres to miles divides every distance, their mean and their standard deviation by the same number, so every z-score, and therefore *r*, is unchanged: still 0.88.
(b) (1) **False.** Strength depends on how close *r* is to −1 or 1, not on its sign. −0.93 is closer to −1 than 0.78 is to 1, so it shows the **stronger** association. The minus sign gives the direction only.

### Part D (6 marks)

**D1.** (2) *x̄* = (8 + 12 + 16 + 19 + 20) ÷ 5 = 75 ÷ 5 = **15 °C** (1). Deviations −7, −3, 1, 4, 5; squares 49, 9, 1, 16, 25, total 100; *s*² = 100 ÷ 4 = 25; *s*ₓ = **5 °C** (1).

**D2.** (2)

| Temperature | *z* | Hot drinks | *z* | Product |
|---|---|---|---|---|
| 8 | −1.4 | 175 | +1.25 | −1.75 |
| 12 | −0.6 | 160 | +0.5 | −0.30 |
| 16 | +0.2 | 155 | +0.25 | +0.05 |
| 19 | +0.8 | 125 | −1.25 | −1.00 |
| 20 | +1.0 | 135 | −0.75 | −0.75 |
| **Total** | | | | **−3.75** |

One mark for the z-scores, one for the products and their total.

**D3.** (1) *r* = (1 ÷ (*n* − 1)) × Σ *z*ₓ*z*_y = −3.75 ÷ 4 = **−0.9375, about −0.94**.

> **Divide by n − 1, not n.** Dividing by 5 gives −0.75. The formula sheet has *n* − 1, for the same reason the standard deviation does. One morning (16 °C) has a positive product: it is above the mean on both. It is outweighed by the four in the "one above, one below" corners.

**D4.** (1) *"There is a strong, negative linear association between the 8 am temperature and the number of hot drinks sold: on warmer mornings the café tended to sell fewer hot drinks."*

### Part E (6 marks)

**E1.** (1) There is a **strong, positive linear association** between the number of public computers and weekly visits at these 18 branches.

**E2.** (2) **No** (1). This is an association between two variables recorded across existing branches; nobody installed computers and watched what happened, so it shows only that branches with more computers tend to have more visits, not why (1).

**E3.** (2) The **number of residents a branch serves** (or its size) (1). Branches serving more people are given more computers, and branches serving more people get more visitors, so the population served can produce the association on its own (1). In the service's records, residents served is strongly associated with both computers (*r* = 0.88) and visits (*r* = 0.95).

> This is a **confounding variable**, the idea from St Mary's: busier shifts had both more doctors and longer waits. Any variable that could plausibly drive both earns the mark if you explain both links, for example opening hours or branch size. Naming a variable without saying how it relates to both variables earns one mark, not two.

**E4.** (1) *"Branches with more public computers tend to have more visits."* Any version that describes an association without claiming that computers cause visits earns the mark.

### Part F (6 marks)

**F1.** (2) The assistant is wrong (1). The scatterplot shows a **strong, non-linear (U-shaped)** association: the youngest and oldest members borrowed the most (31 items at age 8, 39 at 80) and middle-aged members the least (4 items at 47). *r* = −0.01 means there is **no linear** association, not no association (1).

**F2.** (2) The manager is wrong (1). The water heats quickly at first (17 °C to 55 °C in the first 3 minutes) and then levels off near 90 °C (only 88 to 93 °C from 12 to 20 minutes). The association is strong but **non-linear**, and a correlation close to 1 does not show that a straight line is appropriate (1).

> **Look at the plot before you trust r.** Both parts of F are the café lesson from the session. In F1, a strong curve hides behind an *r* near 0. In F2, a curve hides behind an *r* near 1.

**F3.** (2) One mark for a clearly falling straight-line trend with visible scatter (moderate, not tight). One mark for one point that is clearly **off** the pattern and marked, not merely at the end of it.

:::reveal Reveal — a model F3 sketch, after you have drawn yours
![A model sketch: moderate negative linear association with one point that does not fit](figures/s04-hw-f4.svg)

*One possible answer. The orange point is in the middle of the x-range but far above the falling pattern. A point at the far right that continues the downward trend would **not** answer the question: it fits.*
:::

### Marks summary

| Part | Marks |
|---|---|
| A — Vocabulary | 6 |
| B — Oakfield School's journeys | 10 |
| C — Reading r | 6 |
| D — r from z-scores | 6 |
| E — Computers and visitors | 6 |
| F — What r cannot tell you | 6 |
| **Total** | **40** |

---
---

# Reference sheet — keep this

*Every term carries an example. The examples use the 25 Lincoln High students unless stated: distance from school, 0.5 to 28 km, and journey time, 8 to 68 minutes.*

### Two quantitative variables (5.1.A)

**Bivariate quantitative data** — ordered pairs of two quantitative variables, measured on the same individuals.
*Example: (2.5 km, 33 minutes) is one student's pair; there are 25 pairs.*

**Explanatory variable** — the variable used to explain or predict the other. It goes on the **x-axis**.
*Example: distance from school.*

**Response variable** — the variable whose values are explained or predicted. It goes on the **y-axis**.
*Example: journey time.*

**Scatterplot** — a graph of bivariate quantitative data with one point per individual, explanatory on the x-axis and response on the y-axis.
*Example: 25 points, one per student. At St Mary's, 20 points, one per evening shift: the individuals need not be people.*

> Prep books sometimes say *independent* and *dependent* variable. The course description does not; use **explanatory** and **response**.

### Describing a scatterplot (5.1.B)

A description covers **direction, unusual features, form and strength**, in context.

| Feature | Options | Example |
|---|---|---|
| **Direction** | positive: as x increases, y **tends to** increase · negative: y tends to decrease | students who live further away tend to have longer journeys: positive |
| **Unusual features** | points that don't fit the pattern · clusters | the student at 2.5 km who took 33 minutes; at the library, a cluster of five members with 49 to 56 hours and 2 to 6 items |
| **Form** | linear · non-linear | journey time rises at a roughly steady rate with distance: linear. The café's total drinks: non-linear, U-shaped |
| **Strength** | strong · moderate · weak: how closely the points follow the pattern | the journeys: strong. St Mary's doctors and waits: moderate |

> **Unusual means off the pattern.** The 68-minute journey, an outlier for time in Session 3, lives 28 km away and **fits** the pattern. The 33-minute journey is inside every 1.5 × IQR fence and is the one point that does **not** fit.

> **Say it in context, and say "tend to".** "Positive" on its own does not earn the direction mark. And do not argue "it is linear because it is a line": the evidence for linear form is that y changes at a roughly steady rate across the whole range of x.

### Justifying a claim with a scatterplot (5.1.C)

State the claim, quote what the scatterplot shows with numbers, say what it does and does not establish, and keep it in context.
*Example: "All 4 students who live more than 10 km away took at least 30 minutes; of the 21 within 10 km, only 1 did. This supports the claim for these 25 students; 4 students are too few to be sure about the whole school."*

### The correlation coefficient r (5.2.A)

**Correlation coefficient, *r*** — a number that summarises the strength and direction of the **linear** association between two quantitative variables. Found with technology.
*Example: for the 25 students, r = 0.95: a strong, positive linear association between distance and journey time.*

**The formula**, from the exam formula sheet. Each bracket is a z-score:

:::formula
r = (1 ÷ (n − 1)) × Σ [ (xᵢ − x̄) ÷ sₓ ] × [ (yᵢ − ȳ) ÷ s_y ]
:::

*Example by hand: five students at 1, 3, 7, 5, 14 km (mean 6, s = 5) took 10, 14, 18, 22, 36 minutes (mean 20, s = 10). The products of z-scores are 1.00, 0.36, −0.04, −0.04, 2.56, total 3.84, and r = 3.84 ÷ 4 = 0.96.*

| Property | Example |
|---|---|
| Always between −1 and 1, inclusive | 0.95 for the journeys; −0.94 for the spring mornings' hot drinks |
| The sign gives the direction | −0.94: warmer mornings, fewer hot drinks |
| Strength: how close *r* is to −1 or 1 | −0.93 shows a stronger association than 0.78 |
| *r* = 0: **no linear** association | the café's total drinks: r = −0.01, but a strong U-shape |
| *r* = −1 or 1: a perfect linear association | every point exactly on a line |
| Unit-free | in miles and hours, the journeys still have r = 0.95 |

:::note amber Strong, moderate, weak: a rough guide only
The course description gives no cut-offs. This course uses **|r| about 0.8 or more strong, about 0.5 to 0.8 moderate, below about 0.5 weak**. The course description's own sample question calls r = −0.591 moderate. Strength belongs to the scatterplot first; never let the guide overrule the picture.
:::

On a TI-84: distances in L1, times in L2, then STAT → CALC → LinReg(a+bx). If *r* is missing, turn on Stat Diagnostics.

### What r cannot tell you (5.2.A.2–4)

**That the form is linear.** A correlation close to −1 or 1 does not necessarily mean a linear model is appropriate.
*Example: the café's iced drinks have r = 0.96, but the points curve upwards. The coffee machine warming up: r = 0.88, and it levels off.*

**That there is no relationship.** *r* = 0 means no *linear* association.
*Example: the café's total drinks, r = −0.01: busy on cold days and hot days, quiet in between.*

**That one variable causes the other.** Correlation does not necessarily imply causation.
*Example: at St Mary's, shifts with more doctors had longer waits (r = 0.68). Busier evenings had both more doctors and longer waits.*

**Confounding variable** (topic 1.10, taught in Session 6) — a variable associated with both the explanatory and the response variable, which offers another explanation for the association.
*Example: patients arriving at St Mary's, associated with doctors on duty (r = 0.93) and with mean wait (r = 0.88).*

![Eight scatterplots with their correlations, including a U-shaped and a curved pattern](figures/s04-r-gallery.svg)

*What correlations look like. The first six are linear patterns with 40 points each. The last two are the café's: a U-shape with r near 0, and a curve with r near 1.*

:::note red Not in the course description
**Influential points**, **leverage**, **transformations to achieve linearity** and the term **lurking variable** appear in the prep books but nowhere in the course description; the first three are on the course's removed-topics register. Prep books also list two more properties of *r*: that it is not resistant to points that do not fit, and that swapping x and y does not change it. Both follow from the formula, but the course description does not state them, so they are not examinable as stated facts.
:::

---

*CED references: Topic 5.1 (5.1.A.1–2, 5.1.B.1–5, 5.1.C.1), Topic 5.2 (5.2.A.1–4); also 5.5.A.4 (r by technology) and 1.10.D.5 (confounding variable). Course and Exam Description effective Fall 2026; exam reference information (formula sheet) 2026.*

*Supporting reading: Barron's pdf 165–174 · Princeton Review 144–147 · 5 Steps to a 5 93–98.*

*Next session: Topics 5.3–5.5 — the least-squares line, residuals and residual plots, and r². The line that the scatterplots in this session have been hinting at.*
