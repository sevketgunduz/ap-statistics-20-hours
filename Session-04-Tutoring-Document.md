# Session 4 — Two Variables: Scatterplots and Correlation

**AP Statistics · Twenty-Hour Course · One-to-one tutoring edition**
**CED Topics 5.1, 5.2 · Skills 3.A, 4.A, 4.B, 4.D · about 110 minutes, plus the 40-minute Session 2 test**

---

## Where this session sits

Sessions 1 to 3 looked at one variable at a time. This session records two numbers for each individual and asks whether they move together. It is the first time the course asks whether one thing is *associated* with another, and the first time a student can be tempted to say that one thing *causes* another.

These are the first two topics of the course description's Unit 5, *Regression Analysis*. This course brings them forward so that they follow straight on from Unit 1's summaries; Session 5 continues with the least-squares line (5.3–5.5). Everything today is **descriptive**. There is no line of best fit yet, and no inference of any kind.

Three things carry over from earlier sessions. The 25 Lincoln High journey times come back, now with each student's distance from school beside them. Session 3's outlier, the 68-minute journey, gets a second verdict. And Session 3's z-scores, with the same *n* − 1, turn out to be what the correlation coefficient is made from.

### Learning objectives

Verbatim from the course description.

| Code | Objective | Skill |
|---|---|---|
| 5.1.A | Construct scatterplots depicting the relationship between two quantitative variables. | 3.A |
| 5.1.B | Describe the characteristics of a scatterplot. | 4.A |
| 5.1.C | Justify a claim using scatterplots depicting the relationship between two quantitative variables. | 4.B |
| 5.2.A | Interpret the correlation for a linear relationship. | 4.D |

Skills: **3.A** Construct tabular and graphical representations of data and distributions · **4.A** Describe and compare tabular and graphical representations of data, as well as summary statistics · **4.B** Justify a claim based on statistical calculations and results · **4.D** Interpret statistical calculations and results to assess meaning or a claim.

### What the course description does and does not ask for

Read this before teaching; several prep-book habits do not match the 2026 framework.

- **The four features of a scatterplot** are form, direction, strength and unusual features (5.1.B.1). The course description lists them in that order; this course teaches them in the order *direction, unusual features, form, strength*, which is the order a student notices them in, and it makes no difference to the marks.
- **Unusual features** are "clusters of individual points or points that don't fit in the general pattern of association" (5.1.B.5). That definition is about the *pattern*, not about either variable on its own. Scenario A is built around it.
- **The correlation coefficient *r* is found with technology.** Topic 5.5 says so outright: "In simple linear regression, the correlation coefficient, r, is calculated using technology" (5.5.A.4). The exam's formula sheet prints the formula anyway, in z-score form. This session works it by hand once, on five points, to show *why* *r* behaves as it does. It is not a required calculation.
- **No cut-offs for strong, moderate and weak.** The course description says only that strength "can be described as strong, moderate, or weak" (5.1.B.4) and that it depends on how close *r* is to −1 or 1 (5.2.A.2). Its own sample question calls *r* = −0.591 "moderate and negative". This course uses a rough guide, stated in the Scenario A section and on the reference sheet, and says every time that it is only a guide.
- **Correlation does not imply causation** is essential knowledge in its own right (5.2.A.4). So is the point that a high *r* does not prove the form is linear (5.2.A.3), and that *r* = 0 means no *linear* association (5.2.A.2).

:::note red Off-syllabus terms, not taught as examinable
The course description never uses **influential point**, **leverage**, **transformation** (to achieve linearity), **lurking variable**, or **independent/dependent variable**. The first three are on the removed-topics register. Prep books use all five. If the student has met them, say that the exam uses *points that don't fit the pattern*, *explanatory* and *response*, and *confounding variable* (topic 1.10, Session 6) instead.
:::

### Timing

**The Session 2 test comes first.** As with the Session 1 test at the start of Session 3, give Session 2's 40-minute multiple-choice test at the start of this session, before the homework debrief. The clock below starts when the test is finished.

| Minutes | Segment | Who talks |
|---|---|---|
| 0–10 | Homework debrief and diagnostic | Student |
| 10–55 | **Scenario A**: Lincoln High distance and journey time: the two variables, building the scatterplot, describing it, the point that does not fit, justifying a claim, then *r*: what it means, where it comes from, why it has no units, and Guess the Correlation (5.1, 5.2.A.1–2) | Both |
| 55–72 | **Activity**: Sketch and Switch, then *r* measures only linear association: the café (5.1.B, 5.2.A.2–3) | Student |
| 72–92 | **Scenario B**: St Mary's evening shifts: correlation is not causation (5.1.C, 5.2.A.4) | Both |
| 92–102 | Solo case: the library | Student |
| 102–110 | Teach it back, set homework | Student |
| **Total** | **110 minutes of teaching, after the 40-minute Session 2 test** | |

The course description allots three class periods to topics 5.1–5.2 (one and two). Everything they require is taught in the session; the homework practises it.

---

## 0–10 min · Homework debrief and diagnostic

The student arrives with the Session 3 homework self-marked. Ask for the two lists: *"Which did you get wrong, and which did you put a question mark on?"* Spend the time on those only.

**The two errors to check for specifically:**

- **E3 described each school separately.** "Lincoln High's median is 18. Oakfield's median is 14.5." Two descriptions are not a comparison, and the sheet's own key says so. Two minutes here, because the same habit costs marks today in a new form: a scatterplot description that says "distance goes from 0.5 to 28 km and time goes from 8 to 68 minutes" has described two variables and said nothing about how they relate. The sentence that earns the mark links them: *students who live further away tend to have longer journeys*.
- **F2 chose Priya.** Priya's 38 minutes is longer than Sam's 26, but Sam's journey is 2.20 standard deviations above his school's mean and Priya's only 1.45 above hers. A student who picked Priya compared raw minutes. Fix it now, because today's correlation coefficient is built entirely out of z-scores: each value measured against its own variable's mean and standard deviation. A student who does not trust z-scores will not understand why *r* has no units.

Then the diagnostic. Four quick questions, answers out loud.

**Q1.** *"In winter, as the outside temperature rises, a household's heating bill tends to fall. Is that a positive or a negative association?"*

**Q2.** *"A teacher records hours of revision and test score for 30 students. Which variable would you put on the horizontal axis, and why?"*

**Q3.** *"Over a summer, ice-cream sales and shark attacks both go up. Do ice-cream sales cause shark attacks?"*

**Q4.** *"A journey has a z-score of −1.5. What does that tell you about it?"*

| What you hear | What it means | Where to start |
|---|---|---|
| Q1: "negative" | Has the idea of direction | Move on; Scenario A puts it in context |
| Q1: "positive, because they're related" | Thinks *positive* means *there is a relationship* | Teach it now: positive means as one increases the other tends to increase; negative means the other tends to decrease (5.1.B.3) |
| Q2: "revision, because it affects the score" | Has the explanatory idea, informally | Name it in Scenario A: explanatory on the x-axis, response on the y-axis |
| Q2: "doesn't matter" or "the score" | No convention yet | Expected. Scenario A's first question is exactly this |
| Q3: "no, hot weather drives both" | Already sees a third variable | Scenario B will build on it; ask them to name it again there |
| Q3: "yes, they go up together" or long hesitation | Treats association as cause | The heart of Scenario B. Do not correct it now; let Scenario B do it |
| Q4: "1.5 standard deviations below the mean" | Session 3 has held | Move on |
| Q4: "1.5 minutes below average" or blank | z-scores have not landed | Re-do Session 3's F1 in two minutes before Scenario A's correlation section |

The Q3 question is the course description's own: it is one of Unit 5's two essential questions.

---

## 10–55 min · Scenario A — Lincoln High: distance and journey time

The same 25 randomly chosen Lincoln High students whose journey times the student summarised in Sessions 2 and 3. The survey also asked each of them how far they live from school. Say so; the journey times are old friends, so all the attention can go on the new variable and the relationship.

Distance from school (km) and journey time (minutes), in the order of the journey times from Session 3:

```
 km   min    km   min    km   min    km   min    km   min
 0.5    8    1.0    9    1.0   10    1.5   11    2.0   12
 1.5   12    2.5   13    3.0   14    4.5   15    3.5   15
 4.0   16    4.5   17    7.0   18    5.5   18    6.0   20
 6.5   21    5.0   22    7.5   24    8.0   25    9.5   27
11.0   30    2.5   33   14.0   36   17.0   42   28.0   68
```

**The trap this scenario carries: "unusual" in a scatterplot is judged against the pattern, not against either axis.** The student has just spent a session learning that 68 minutes is an outlier. They will look for it here and call it the unusual point. In the scatterplot it is not unusual at all: that student lives 28 km away, and the journey continues the pattern of everyone else. The point that does not fit is one that neither the 1.5 × IQR rule for distance nor the rule for time would ever flag.

### Two variables, one student each (5.1.A)

:::script
ask | Ask | "Each of the 25 students gave us two numbers. Which one do we think helps explain the other?"
listen | Listen for | Distance explains journey time: living further away is a reason a journey might take longer.
intro | Introduce | **Bivariate quantitative data**: ordered pairs of two quantitative variables, measured on the same individuals (5.1.A.1). The **explanatory variable** explains or predicts the **response variable**. Explanatory goes on the x-axis, response on the y-axis (5.1.A.2).
ifsay | If "does it matter which way round?" | "The course fixes the convention, and every description you write depends on it: *as distance increases, time tends to*…. Swap the axes and that sentence is about something else."
:::

Point out that the individuals are the **students**, as in Session 1. Each dot on the scatterplot will be one student. That matters again in Scenario B, where the individuals are not people.

### Building the scatterplot (5.1.A)

Have the student draw it by hand before you show anything: x-axis from 0 to 30 km, y-axis from 0 to 70 minutes, both labelled with the variable **and its units**. Twenty-five points take about five minutes; let them take it.

:::script
ask | Ask | "Before you plot: where will the student with the 68-minute journey go?"
listen | Listen for | At 28 km across and 68 minutes up, the top right corner.
ifsay | If the axes start at 8 and 0.5 | "That works, but start both at 0 today. We are about to ask whether points are close to a pattern, and a squashed axis makes that harder to see." (Not starting at 0 is not an error; it is a choice to make on purpose.)
:::

![Scatterplot of distance from school and journey time for 25 Lincoln High students](figures/s04-scatter-commute.svg)

*The finished scatterplot. Each dot is one student. The orange dot is the student who lives 2.5 km away and took 33 minutes. The student in the top right is the 68-minute journey from Session 3.*

### Describing the association (5.1.B)

The course description asks for four things: **direction, unusual features, form and strength** (5.1.B.1). Take them in the order the eye finds them.

:::script
ask | Ask | "Direction first. As distance goes up, what happens to journey time? Say it about the students."
listen | Listen for | "Students who live further from school tend to have longer journeys."
intro | Introduce | **Positive association**: as the explanatory variable increases, the response tends to increase. **Negative**: it tends to decrease (5.1.B.3). "Tends to" is the phrase to use: not every student who lives further takes longer.
ifsay | If "it's positive" and nothing else | "Positive what? Say it about distance and journey time." The course description is blunt: writing generally about direction is "typically insufficient"; students are expected to say what the direction means in context.
ask | Ask | "Is there any student who doesn't fit what the others are doing?"
listen | Listen for | The student at 2.5 km who took 33 minutes. The other three students living 2 to 3 km away took 12 to 14 minutes.
:::

Now spring the trap before moving to form and strength.

:::script
ask | Ask | "In Session 3 the 68-minute journey was an outlier. Is it unusual here?"
listen | Listen for | Most students say yes. Let them commit, then ask them to look at the scatterplot again.
ifsay | If "yes, it's the biggest" | "Is it where you would expect a student who lives 28 km away to be? Cover it with your finger and follow the other points up and to the right. Where does the pattern go?" It goes straight to it.
intro | Introduce | **Unusual features** of a scatterplot are clusters, or points that don't fit the general pattern of association (5.1.B.5). The 68-minute journey is far from the other points but **fits** the pattern. The 33-minute journey is not extreme in either variable but **does not fit** it.
:::

The numbers make it undeniable. By the 1.5 × IQR rule, the distances have Q1 = 2.25, Q3 = 7.75, IQR = 5.5 and fences at −6.0 and 16.0 km, so **17 and 28 km are both outliers** for distance. For journey time, Session 3's fences were −7.75 and 46.25 minutes, so **68 is an outlier** for time. The student at 28 km and 68 minutes is an outlier in *both* variables and still fits the pattern. The student at 2.5 km and 33 minutes is inside *all four* fences and is the one point that does not fit.

> **The sentence to write down:** *In a scatterplot, a point is unusual if it does not fit the pattern of the others. Being the largest value of one variable does not make it unusual, and being ordinary in both variables does not make it typical.*

Then form and strength.

:::script
ask | Ask | "Form: do the points follow a straight-line pattern, or a curve?"
listen | Listen for | Linear: they rise at a roughly steady rate.
ifsay | If "linear, because it's a line" | "What about the points tells you that?" The course description names this as a common error: using the word *line* to explain why a relationship is linear. The evidence is that journey time goes up by about the same amount for each extra kilometre, all the way along, with no bend.
intro | Introduce | **Form**: linear or non-linear (5.1.B.2).
ask | Ask | "Strength: how closely do the points follow that pattern?"
listen | Listen for | Closely, apart from the 33-minute student. Strong.
intro | Introduce | **Strength** is how closely the points follow the general pattern: strong, moderate or weak (5.1.B.4).
:::

The model description, in full. Ask the student to write their own first, then compare.

> *"There is a **strong, positive, linear** association between distance from school and journey time for these 25 students: students who live further from school **tend to** have longer journeys. One student **does not fit the pattern**: she lives 2.5 km away but took 33 minutes, while the other three students living 2 to 3 km away took 12 to 14 minutes. The student with the longest journey, 68 minutes, lives furthest away, 28 km, and fits the pattern."*

| Feature | What the model says |
|---|---|
| Direction | positive: further away **tends to** mean longer |
| Unusual features | the 2.5 km, 33-minute student, with the comparison that shows it |
| Form | linear |
| Strength | strong |
| **In context** | distance, journey time, students, units |

The student may wonder why the 33-minute journey took so long; perhaps she walks, or drops a younger sibling at another school first. The data cannot say. A description reports what the plot shows; it is fine to suggest a reason, as long as it is labelled as a suggestion.

### Justify a claim (5.1.C)

*"The head of year says: every student who lives more than 10 km away takes at least half an hour to get to school, but almost nobody closer does. Does the scatterplot support that?"*

Yes, for these 25 students. All **4** students living more than 10 km away (11, 14, 17 and 28 km) took at least 30 minutes (30, 36, 42 and 68). Of the **21** living within 10 km, only **1** took 30 minutes or more: the 33-minute student at 2.5 km. Same template as Sessions 1 to 3: **state the claim · quote the numbers · say what they do and do not establish · keep it in context.** What they do not establish is that the same holds for every Lincoln High student. These 25 were chosen at random, which helps, but 4 students is a small group to generalise from.

### Correlation: one number for a linear association (5.2.A)

:::script
ask | Ask | "If you had to put one number on how strong this linear pattern is, what would you want the number to do?"
listen | Listen for | Anything like: be big when the points are close to the pattern, small when they are scattered, and say whether it goes up or down.
intro | Introduce | The **correlation coefficient, *r***, summarises the **strength and direction of the linear association** between two quantitative variables (5.2.A.1).
:::

Get *r* from technology, because that is what the course expects (5.5.A.4). On a TI-84, enter the distances in L1 and the times in L2, then STAT → CALC → LinReg(a+bx). If *r* does not appear, turn on Stat Diagnostics (on the MODE screen on newer models, or DiagnosticOn from the catalogue on older ones). Ignore *a* and *b* until Session 5.

**For the 25 students, r = 0.95.**

:::script
ask | Ask | "Put r = 0.95 into a sentence about these students."
listen | Listen for | "There is a strong, positive linear association between distance from school and journey time."
ifsay | If "95% of journey time is explained by distance" | "That is a different number, r², and it is Session 5's. Today r tells you strength and direction of a linear association, nothing more."
ifsay | If "distance causes 95% of the time" | "r measures how closely the points follow a line. It says nothing about why." Hold this for Scenario B.
:::

The facts about *r* that the course description states (5.2.A.1–2):

| Fact | What it means here |
|---|---|
| −1 ≤ *r* ≤ 1, always | 0.95 is near the top of the scale |
| The sign gives the direction | positive: further away, longer journey |
| Strength is how close *r* is to −1 or 1 | 0.95 is close to 1: strong |
| *r* = 0 means **no linear** association | not "no association"; the activity shows the difference |
| *r* = 1 or −1 means a **perfect** linear association | every point exactly on a line |
| *r* is unit-free | below: it does not care about kilometres or minutes |

:::note amber A rough guide to the words, not a rule
The course description gives no cut-offs. This course uses: **|r| of about 0.8 or more, strong; about 0.5 to 0.8, moderate; below about 0.5, weak**. The course description's own sample question describes r = −0.591 as "moderate and negative", which fits. But strength belongs to the scatterplot first: always look at the plot, and never let the guide overrule what the points show.
:::

### Where r comes from: z-scores, from Session 3

The exam's formula sheet gives *r* in this form. Write it on the screen and point at the two brackets: **each one is a z-score**, exactly as in Session 3, with the sample mean and standard deviation.

:::formula
r = (1 ÷ (n − 1)) × Σ [ (xᵢ − x̄) ÷ sₓ ] × [ (yᵢ − ȳ) ÷ s_y ]
:::

So *r* is, near enough, **the average product of the z-scores**: turn every distance and every time into a z-score, multiply each student's pair, add them up, divide by *n* − 1.

**Worked example.** Five of the 25 students, and their journey times are the five from Session 3's worked standard deviation: **10, 14, 18, 22, 36 minutes**, mean 20 and *s* = 10. Their distances are **1, 3, 7, 5, 14 km**.

:::script
ask | Ask | "You found in Session 3 that these journey times have mean 20 and s = 10. Now find the mean and standard deviation of the five distances."
listen | Listen for | x̄ = 30 ÷ 5 = 6 km. Deviations −5, −3, 1, −1, 8; squares 25, 9, 1, 1, 64, total 100; s² = 100 ÷ 4 = 25; sₓ = 5 km.
ask | Ask | "Now the z-score of each distance and each time, then each student's product."
:::

| km | *z* for distance | min | *z* for time | product |
|---|---|---|---|---|
| 1 | (1 − 6) ÷ 5 = −1.0 | 10 | (10 − 20) ÷ 10 = −1.0 | +1.00 |
| 3 | −0.6 | 14 | −0.6 | +0.36 |
| 7 | +0.2 | 18 | −0.2 | −0.04 |
| 5 | −0.2 | 22 | +0.2 | −0.04 |
| 14 | +1.6 | 36 | +1.6 | +2.56 |
| **Total** | | | | **3.84** |

*r* = 3.84 ÷ (5 − 1) = **0.96**.

![The five students plotted as z-scores, with the product of z-scores for each](figures/s04-z-products.svg)

*Each student plotted by their two z-scores. Students above the mean on both, or below on both, add a positive product; students above on one and below on the other add a negative product. A positive association puts most points in the top-right and bottom-left.*

:::script
ask | Ask | "Two students gave negative products. What do they have in common?"
listen | Listen for | Each is above the mean on one variable and below on the other: 7 km but a below-average time, 5 km but an above-average time.
ask | Ask | "So what would the points look like for r near 0?"
listen | Listen for | Spread across all four corners, so the positive and negative products cancel.
:::

This is the only time the session computes *r* by hand. Its job is to make three properties obvious rather than memorised: the sign comes from which corners the points sit in; *r* cannot be pushed outside −1 and 1; and *r* has no units, because z-scores have none.

### What r does not change with: units (5.2.A.1)

:::script
ask | Ask | "The principal wants distances in miles and times in hours. What happens to r?"
listen | Listen for | Nothing. It stays 0.95.
ifsay | If "it gets smaller, because the numbers are smaller" | "What happens to a z-score when you divide every value, the mean and the standard deviation by the same number?" (Session 3: the z-score does not change. So nothing in the formula changes.)
intro | Introduce | *r* is **unit-free** (5.2.A.1). Converting to miles, or to hours, or correcting every time for a clock that ran 3 minutes fast, leaves *r* = 0.95 exactly.
:::

This is Session 3's changing-units table with one new line: adding or multiplying by a positive constant moves the mean and stretches the standard deviation, and the z-scores, and so *r*, are untouched.

### Guess the correlation

:::sim guess-correlation | Guess the Correlation | 900
Five rounds, on **Linear only**, at 40 points. The student sets a guess with the slider and checks it; you say nothing until the number appears. Then one round at **15 points**, to see how much a small sample can look like almost anything. Save **Include non-linear and clusters** for after the activity, where it earns its place.
:::

The thing to watch for is systematic underestimation of strong correlations: a cloud that looks loose to a beginner can have *r* = 0.8. If the student's misses are all in one direction, say so; that is the calibration this tool is for.

---

## 55–72 min · Activity — Sketch and Switch

The course description's Sample Instructional Activity for topic 5.1: students sketch a scatterplot from a verbal prompt, such as its own example, a "weak negative, non-linear association", then switch papers and review each other's work.

**The one-to-one conversion.** You are the partner, twice over. In Round 1 you give the prompts and the student sketches; you review the sketches **literally**, against the words of the prompt and nothing else. In Round 2 the roles switch: the student reviews four sketches that "your partner" drew, and has to find the ones that do not match their prompts. The literal review is the point, as it was in Match Mine: an examiner reads the words.

### Round 1: you give the prompts, the student sketches

Give them one at a time, about a minute each. Axes need only *x* and *y* labels; no scale.

| Prompt | What a matching sketch needs |
|---|---|
| **P1** Weak negative, non-linear association | A downward trend that bends (steep then levelling off, or the reverse), with the points loosely scattered around the curve |
| **P2** Strong positive linear association, with one point that does not fit the pattern | A tight rising band, and one point well **off** the band, not merely at its end |
| **P3** Moderate negative linear association | A falling straight-line trend, clearly visible but with a lot of scatter |
| **P4** No association | A cloud with no trend in any direction |

![Model sketches for the four Sketch and Switch prompts](figures/s04-sketch-models.svg)

*Model answers. P1 falls steeply, then levels off, and its points are loose. P2's odd point sits below the band in the middle, not at the end. The r values are given only for the two linear prompts: for P1, a non-linear pattern, r does not measure the strength of the pattern at all.*

| What the student draws | What to say |
|---|---|
| P1 as a straight falling band | "Which word did you draw? Non-linear needs a bend." |
| P1 as a tight curve | "Weak means the points are loose around the pattern." |
| P2's odd point at the top-right end of the band | "Does that point fit the pattern or not?" This is Scenario A's trap again: far along the line is not off it. |
| P3 as tight as P2 | "What separates moderate from strong?" Only how close the points are to the pattern. |
| P4 as a flat horizontal band | Correct: y does not change as x changes. A round, shapeless cloud is also correct. Both have *r* near 0. |

### Round 2: switch — the student reviews your partner's sketches

Put this on the shared screen. Each sketch is labelled with the prompt the partner was given. The orange point in (d) is the one the partner meant as unusual.

![Four sketches drawn by a partner, each with the prompt they were given](figures/s04-sketch-partner.svg)

*The partner's four sketches. Two match their prompts and two do not; the student should find which and say which word was missed.*

:::script
ask | Ask | "Which of these match their prompts? For any that don't, which word in the prompt did the partner get wrong?"
listen | Listen for | (a) is not strong: the points are too loose; it is moderate (r = −0.62). (b) matches: weak, positive, linear (r = 0.30). (c) is neither moderate nor non-linear: it is a strong straight-line pattern (r = 0.96). (d) does not match: the orange point is far out but **on** the pattern, so the partner has not drawn a point that does not fit.
ifsay | If (d) is accepted | "Cover the orange point. Now follow the pattern out to the right. Where does it go?" It goes straight to the orange point. Same verdict as the 68-minute journey.
:::

### The debrief question that makes this topic 5.2

:::script
ask | Ask | "Sketch me a strong association with r close to 0."
listen | Listen for | Usually a pause, then either "impossible" or a U-shape. If it is a U-shape, ask why its r would be near 0. If they say impossible, give them the café.
:::

The café from Sessions 2 and 3. It recorded the midday temperature outside on the same 10 days as in Session 3, and the number of drinks it sold on each day, all drinks together and iced drinks on their own.

| Midday temperature (°C) | 12 | 14 | 15 | 15 | 16 | 18 | 19 | 21 | 22 | 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| All drinks sold | 257 | 225 | 208 | 206 | 199 | 185 | 186 | 181 | 187 | 259 |
| Iced drinks sold | 9 | 11 | 13 | 16 | 20 | 31 | 44 | 64 | 74 | 167 |

The manager ran the correlation for all drinks against temperature, got **r = −0.01**, and concluded: *"The weather makes no difference to how many drinks we sell."*

![Café: midday temperature against all drinks sold and against iced drinks sold, 10 days](figures/s04-cafe.svg)

*Left: all drinks. Sales are highest on the coldest day (257) and the hottest (259) and lowest in between (181 at 21 °C), a clear U-shape with r = −0.01. Right: iced drinks alone, a strong curve with r = 0.96.*

:::script
ask | Ask | "Is the manager right?"
listen | Listen for | No. Temperature matters a lot: cold days and hot days are busy, mild days are quiet. The association is strong and non-linear, so r, which measures linear association, is near 0.
intro | Introduce | *r* = 0 indicates **no linear association** (5.2.A.2). It does not mean no association.
ask | Ask | "Using the z-score products: why does the U-shape give r near 0?"
listen | Listen for | The cold, busy days are below the mean temperature and above the mean sales: negative products. The hot, busy day is above on both: a positive product. They cancel.
ask | Ask | "Now the iced drinks: r = 0.96. Does that make the relationship linear?"
listen | Listen for | No. The points bend upwards: iced sales rise slowly at first and then fast.
intro | Introduce | A correlation close to −1 or 1 does not necessarily mean a linear model is appropriate (5.2.A.3). **Look at the scatterplot before you trust r.**
:::

> **The sentence to write down:** *r measures the strength and direction of a linear association only. An r near 0 can hide a strong curve, and an r near 1 can belong to a curve.*

Now hand the student **Guess the Correlation** again, with **Include non-linear and clusters** switched on, for three or four rounds. The feedback names each non-linear pattern as it appears.

---

## 72–92 min · Scenario B — St Mary's evening shifts: correlation is not causation

Back to Session 1's hospital survey and St Mary's. The hospital's own records for 20 evening shifts give, for each shift, the number of **doctors on duty** and the **mean waiting time**, in minutes, of the patients seen that shift. (They record one more variable, which stays hidden until the student asks for it.)

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

**The trap this scenario carries: an association, however strong, does not show that one variable causes the other.** The student has just learned to describe an association and to put a number on it. Both skills make a causal claim feel earned. It is not.

### Describe it first

Before the claim, the description, so that the skills from Scenario A get used on a second data set. One new point: **the individuals are shifts, not patients**. Each dot is one evening, and its mean wait summarises dozens of patients.

![St Mary's, 20 evening shifts: doctors on duty against mean wait](figures/s04-hospital-doctors.svg)

*Doctors on duty is a whole number, so the points line up in columns.*

:::script
ask | Ask | "Describe the association between doctors on duty and mean waiting time."
listen | Listen for | A moderate, positive, roughly linear association: shifts with more doctors on duty tended to have longer mean waits. No point stands far off the pattern. r = 0.68.
ifsay | If "strong" | "Compare it with the journeys. How closely do these points follow the pattern?" There is a lot of scatter: shifts with 5 doctors range from 28 to 38 minutes. 0.68 fits *moderate* on the course's rough guide.
:::

### The claim

The department manager has seen the same plot:

> *"Our shifts with more doctors have longer waits, r = 0.68. Extra doctors are slowing the department down. We can cut evening staffing without making waits any worse."*

:::script
ask | Ask | "Is that supported?"
listen | Listen for | Probably "no", but the reason matters. Push for why: "the plot shows they go together, not that one causes the other."
intro | Introduce | A perceived or real relationship between two variables does not mean that changes in one cause changes in the other: **correlation does not necessarily imply causation** (5.2.A.4).
:::

### What else changes from shift to shift

:::script
ask | Ask | "Think about a shift with 3 doctors and one with 8. What else is probably different about those two evenings?"
listen | Listen for | How busy they are. The rota puts more doctors on the evenings it expects to be busy, and busy evenings have longer waits.
:::

The records have it: the number of **patients arriving** during each shift. The shifts in the table above are numbered in order of it:

```
Shift      1   2   3   4   5   6   7   8   9  10
Arrivals  26  34  36  39  40  44  46  48  50  52

Shift     11  12  13  14  15  16  17  18  19  20
Arrivals  54  55  56  59  67  70  73  74  75  77
```

Show the second plot.

![St Mary's, 20 evening shifts: patients arriving against doctors on duty](figures/s04-hospital-arrivals.svg)

*Busier shifts had more doctors on duty (r = 0.93).*

Patients arriving is strongly associated with doctors on duty (**r = 0.93**) and with mean wait (**r = 0.88**). That one variable explains the whole pattern: busy evenings get more doctors **and** longer waits. The number of patients arriving is a **confounding variable**, defined in the course description as a variable that "provides an alternative explanation for the observed relationship between the explanatory and response variables", and which "must be associated with both" (1.10.D.5). Session 6 teaches it properly; today it needs only a name and the idea.

Then the detail that turns the manager's claim upside down. Look only at the five shifts with a similar load, 50 to 56 patients:

| Arrivals | 50 | 52 | 54 | 55 | 56 |
|---|---|---|---|---|---|
| Doctors | 5 | **4** | 5 | 5 | 5 |
| Mean wait (min) | 35 | **41** | 38 | 36 | 38 |

Among shifts that were about equally busy, the one with **fewer** doctors had the **longest** wait. Five shifts cannot settle anything, and these are records, not an experiment. But it shows how the same data can point the opposite way once the confounding variable is held roughly still.

### What the data can and cannot support

| Statement | Supported? |
|---|---|
| "On these 20 shifts, more doctors on duty was associated with longer mean waits." | **Yes**: that is what the plot and *r* = 0.68 describe |
| "Extra doctors cause longer waits." | **No**: an association in observational records; busier evenings explain both |
| "Cutting doctors will not make waits worse." | **No**: it is a claim about what *would* happen after a change nobody made |
| "To find out what extra doctors do to waits, the hospital would need to change staffing deliberately and compare." | **Yes**, and that is Session 7's experiments |

> **The model answer to the manager:** *"The data show that shifts with more doctors tended to have longer waits (r = 0.68), but this does not show that doctors cause the waits. Busier shifts had both more doctors (r = 0.93 between arrivals and doctors) and longer waits (r = 0.88 between arrivals and waits), so the number of patients arriving is a confounding variable that could explain the association. These are observational records, so they cannot show what cutting staff would do."*

Link it back to the diagnostic's Q3. Ice-cream sales and shark attacks: hot weather drives both. Same structure, and now the student can name the parts.

---

## 92–102 min · Solo case — the library

Unaided. The library service from Sessions 1 and 3: the same 35 randomly chosen members of the Central branch, whose hours in library buildings the student summarised last session, now with the number of items each borrowed last year. Watch, say nothing, note where they hesitate.

![Central library members: hours in library buildings against items borrowed, 35 members](figures/s04-library.svg)

*Hours spent in library buildings and items borrowed last year, 35 Central branch members.*

1. Which variable would you treat as explanatory, and which as response? Why?
2. Describe the association, in context.
3. Technology gives r = 0.40. A librarian says: "r is only 0.40, so time in the library has only a weak relationship with borrowing." Do you agree? Explain.
4. A councillor says: "If we can get members to spend more time in the library, they will borrow more." Does the scatterplot support this?

**Answers.**

1. **Hours** explanatory and **items borrowed** response is the natural choice: the question is whether time spent there goes with borrowing more. The reverse can be defended if it is argued; the answer must say which and why.
2. *"For most members there is a **strong, positive, linear** association between hours spent in library buildings and items borrowed: members who spent more hours tended to borrow more items, from 4 items at 16 hours to 33 to 37 items at 54 to 64 hours. A **cluster** of five members who spent 49 to 56 hours borrowed only 2 to 6 items each, far below the pattern of the others."*
3. **Disagree, at least with the conclusion.** *r* = 0.40 summarises all 35 members together, and the five members in the cluster do not follow the pattern, which makes the overall linear association weaker. For the other members the pattern is strong. The honest summary names both: a strong positive pattern for most members, and a separate group who spend a lot of time and borrow little.
4. **No.** This is an association in a sample of members, not an experiment: nobody was made to spend more time. Members who choose to spend more time may be keener readers anyway. And the cluster is five members who spend a great deal of time and borrow almost nothing (perhaps they use the study space), which the councillor's claim ignores.

**Watch for:** "negative" because the cluster points are low (the direction is about the trend, not a group); calling the cluster "outliers" and moving on without saying they are a group; answering item 3 with "0.40 is weak, so yes", which is reading the number without looking at the plot, the exact habit the activity was built to break; answering item 4 with "yes, r is positive".

---

## 102–110 min · Teach it back

> *"Explain to me why r for the café's total drinks was almost 0, even though temperature clearly mattered. Then tell me what r does measure."*

A good answer contains three things. *r* measures the strength and direction of a **linear** association only. For the U-shape, the busy cold days sit below the mean temperature and above the mean sales, so their z-score products are negative, while the busy hot day is above on both and gives a positive product; they cancel, so the sum is near 0. And therefore the scatterplot has to be looked at before *r* is trusted: a strong curve can have *r* near 0.

If the student gets the first and third but not the second, that is acceptable; the mechanism is a bonus. If they say "because the relationship is weak", the activity has not landed: go back to the café plot and ask *"is it weak?"* Then set the homework.

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
