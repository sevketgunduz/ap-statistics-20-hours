# Session 8 — Two-Way Tables and Simulation

**AP Statistics · Twenty-Hour Course · One-to-one tutoring edition**
**CED Topics 2.1, 2.2, 2.3 · Skills 3.B, 3.C, 4.A, 4.B · about 167 minutes, plus the 35-minute Session 6 test**

---

## Where this session sits

This session opens **Block D · Probability and distributions**. It starts where Session 2 left off. Session 2 compared one categorical variable across data sets of different sizes and found that shares, not counts, carry the comparison. Today there are two categorical variables for the same individuals, arranged in a **two-way table**, and the question is whether one of them is **associated** with the other. The tool for answering it is the **conditional relative frequency**: a share worked out inside one level of a variable. It is the most important calculation of the session, because Session 10 defines **conditional probability** on exactly these tables.

The second half starts probability. Before any rule exists, a probability can be **estimated** by running a random process many times and taking a relative frequency, and the course description names both the method, **simulation**, and the reason it works, the **law of large numbers**. Sessions 9 to 11 then build the rules that make the long simulations unnecessary.

Both scenarios continue earlier sessions. Lincoln High's bus-pass census from Session 7 grows into a travel register for all 1,842 students, a two-way table of home area against travel mode. And St Mary's, which proved in Session 7 that text reminders cut missed appointments, now has to decide how many patients to book into each clinic session, a question only a probability can answer.

### Learning objectives for topics 2.1–2.3

Verbatim from the course description.

| Code | Objective | Skill |
|---|---|---|
| 2.1.A | Compare tabular and graphical representations for the relationship between two categorical variables. | 4.A |
| 2.1.B | Justify a claim using tabular and graphical representations for the distributions of two categorical variables. | 4.B |
| 2.2.A | Calculate summary statistics from two-way tables. | 3.B |
| 2.2.B | Compare summary statistics for two categorical variables. | 4.A |
| 2.2.C | Justify a claim using summary statistics for two categorical variables. | 4.B |
| 2.3.A | Estimate probabilities using simulations. | 3.C |

Skills: **3.B** Calculate summary statistics, relative positions of points within a distribution, and predicted responses · **3.C** Calculate and estimate expected counts, percentages, probabilities, and intervals · **4.A** Describe and compare tabular and graphical representations of data, as well as summary statistics · **4.B** Justify a claim based on statistical calculations and results.

### What the course description does and does not ask for

Read this before teaching; the prep books and the plan differ from the 2026 framework in several places.

- **Three graphs are named, and all three are examinable** (2.1.A.2): **side-by-side bar charts**, **segmented bar charts** and **mosaic plots**. In each, the frequency or relative frequency of each level of one variable is shown **for each category of the other**. Today draws all three for the same Lincoln High table.
- **The mosaic plot is named but not described.** The course description does not say what its bar widths mean. The standard construction, which Barron's teaches and exam questions use, makes each bar's **width** the marginal relative frequency of its group, so each tile's **area** is a joint relative frequency. The theory states this as the construction, not as a course-description sentence.
- **Three relative frequencies are defined exactly** (2.2.A.1–3): **joint** (a cell over the table total), **marginal** (a row or column total over the table total) and **conditional** (a cell over its own row total, or over its own column total). The course description's words are *joint relative frequency*, *marginal relative frequency* and *conditional relative frequency*. Barron's uses other names for the same ideas, listed in the red box below; today uses the course description's.
- **Association is decided by comparing conditional relative frequencies** (2.1.A.3, 2.2.B.1): the distribution of one variable, compared across the levels of the other. Nothing today calculates whether a difference is too large to be chance; that is the chi-square test, Session 17.
- **The law of large numbers is in topic 2.3** (2.3.A.7), not 2.4. The course plan lists it under Session 9; the course description puts it with simulation, and it is taught today, where the simulation makes it visible.
- **A simulation is described by what it does, not by named steps** (2.3.A.4): model random events so that simulated outcomes match real ones, associate every outcome with a value determined by chance, and record the counts of simulated outcomes and the count total. The five steps used today are the course's way of organising that sentence; they are not a list the course description gives.
- **The course description says "random number generator"**, as in Session 6 (1.11.A). It never names the printed tables of digits that 5 Steps recommends for exam answers (red box below). Today's hand simulation uses a row of digits produced by a random number generator, which is the same thing on paper.

:::note red Off-syllabus terms, not taught as examinable
The course description never uses **Simpson's paradox**, which Barron's teaches with two surgeons (pdf 158–160) and mosaic plots; it appears today only in a red extension block. It also never uses **marginal distribution**, **conditional distribution**, **joint distribution**, **stacked bar chart**, **table of random digits**, **law of averages** or **gambler's fallacy**. The first four are other names for things the session teaches under the course description's names (marginal, conditional and joint relative frequencies; a segmented bar chart; digits from a random number generator). The last two are prep-book names for a misreading of the law of large numbers that the theory section addresses directly.
:::

### Timing and who talks

**The Session 6 test comes first.** Following the pattern of the earlier sessions (Session 1's test opened Session 3, Session 2's opened Session 4, and so on to Session 5's, which opened Session 7), give Session 6's multiple-choice test at the start of this session, before the homework debrief: 20 questions, 35 minutes, as the test page states. The pattern has not been confirmed as a rule; if your own plan differs, follow it. The clock below starts when the test is finished.

| Minutes | Segment | Who talks |
|---|---|---|
| 0–12 | Homework debrief and diagnostic | Student |
| 12–54 | **Theory**: two-way tables; joint, marginal and conditional relative frequencies; conditioning on rows or columns; side-by-side bar charts, segmented bar charts and mosaic plots; choosing a graph; association; justifying a claim; random process, outcome and event; simulation and its five steps; probability as long-run relative frequency; the law of large numbers; eight check questions (2.1–2.3) | Both |
| 54–92 | **Scenario A**: Lincoln High's travel register: one table, all three kinds of relative frequency, the trap of conditioning the wrong way, all three graphs of the same data, and an association claim | Both |
| 92–112 | **Activity**: Quiz-Quiz-Trade with the hospital waiting table and the café's members | Student |
| 112–147 | **Scenario B**: St Mary's overbooking: from a relative frequency to a model, twenty clinic sessions by hand, the trap of counting patients instead of sessions, and the Overbooking Simulation tool | Both |
| 147–159 | Solo case: the library's two branches | Student |
| 159–167 | Teach it back, set homework | Student |
| **Total** | **167 minutes of teaching, after the 35-minute Session 6 test** | |

The course description allots four class periods to topics 2.1–2.3 (two, one and one). Everything they require is taught in the session, first stated in the theory section and then applied; the homework practises it. The theory section has sixteen subsections in 42 minutes, because each of the three graphs and each of the three relative frequencies is examined by name.

---

## 0–12 min · Homework debrief and diagnostic

### The Session 7 homework: two lists and two errors

The student arrives with the Session 7 homework self-marked. Ask for the two lists: *"Which did you get wrong, and which did you put a question mark on?"* Spend the time on those only.

**The two errors to check for specifically:**

- **B1 said "too high".** The discharge-letter link was voluntary response, and the reflex is that volunteers push an estimate up. Here they push it **down**: the heading *"Had a problem during your stay?"* invites the patients least likely to recommend the hospital. The direction comes from **who** volunteers, never from a rule. Two minutes here, because the error has the same shape as today's trap. "The proportion of repliers who had a problem" and "the proportion of patients with a problem who replied" are two different numbers, one worked out inside the repliers and one inside the patients with a problem. Today names both: they are **conditional relative frequencies**, conditioned in opposite directions.
- **D3 cited the pairing.** "Because the branches were paired" earns nothing: pairing made the comparison more precise, and the coin in each pair, **random assignment**, is what allows a conclusion about cause. Keep it in mind for Scenario A, where a strong association comes from a census with no random assignment at all, so it shows an association and no more.

E1 is worth ten seconds if it was marked with a **?**: "yes, because there were 40 days" cites replication; the mark was for the coin.

Then the diagnostic.

### Four diagnostic questions on tables, shares and chance

Four quick questions, answers out loud.

**Q1.** *"In Session 1, 84 of the 300 surveyed patients were at St Mary's. What is St Mary's relative frequency, and what number goes underneath?"*

**Q2.** *"Last year St Mary's had 70 of the 200 surveyed patients; this year 84 of 300. Did St Mary's share go up?"*

**Q3.** *"In Session 4, distance from school and journey time were associated. What did that word mean, and did it show that distance causes long journeys?"*

**Q4.** *"A coin is tossed 10 times and lands heads 7 times. Is the probability of heads 0.7? How would you find out?"*

| What you hear | What it means | Where to start |
|---|---|---|
| Q1: "0.280; the 300 goes underneath, the total" | Session 1's 1.3.A held | Move on; the theory's joint and conditional subsections change which total goes underneath |
| Q1: "84 ÷ 12,400" or hesitation over the total | Unsure which total a share is taken of | The heart of Scenario A. Take the theory's *Conditional relative frequency* and *Rows or columns* subsections slowly |
| Q2: "no, it fell from 35.0% to 28.0%" | Session 2's comparison rule held | Move on at pace; today applies it inside a two-way table |
| Q2: "yes, 84 is more than 70" | Session 2's comparison trap is back | Recall Session 2's *Comparing data sets with different totals (1.4.C)* before the theory, then stress it in *Association between two categorical variables* |
| Q3: "they tend to move together; no, association is not cause" | Sessions 4 and 6 held | The theory gives association its categorical meaning: the shares differ from group to group |
| Q3: "yes, living further away causes it" | Treats association as cause | Recall Session 6: an observational study shows association, random assignment is needed for cause. Scenario A's census is observational |
| Q4: "no, 10 tosses is too few; toss it many more times" | Has the law of large numbers in words | The theory's *Probability as long-run relative frequency* and *The law of large numbers* give the exact version |
| Q4: "yes, 7 out of 10" or "no, it has to be 0.5, so tails is due" | Treats a short run as the probability, or expects the coin to compensate | Take the law of large numbers' "what it does not say" slowly; the Scenario B tool settles it |

---

## 12–54 min · Theory — two categorical variables, and probability by simulation

Every concept the session uses is stated here, before any data. Put each subsection on the shared screen, read the rule with the student, and have them say what it does **not** say; that is where the marks go. The illustrations are deliberately bare: two made-up tables with groups A and B, a die and a coin. Lincoln High, the hospital cards, St Mary's and the library come afterwards and apply these rules; when a question there needs a definition, point back to the subsection here rather than restating it. The section ends with eight check questions.

**What this section builds on, by name.** From Session 1: *Frequency and relative frequency tables (1.3.A.1–2)*, rf = f ÷ n, and the template for a claim. From Session 2: *Bar charts (1.4.A)*, *Pie charts and the slice angle (1.4.A)* and *Comparing data sets with different totals (1.4.C)*. From Session 4: an **association** between two variables. From Session 6: an observational study shows association, not cause, and a **random number generator** chooses at random (1.11.A.3). They are recalled where they are needed and not re-taught.

Sixteen subsections. Keep each to about two and a half minutes and make the student speak in each one.

### Two-way tables, also called contingency tables (2.1.A.1)

A **two-way table**, also called a **contingency table**, can be used to **summarize and compare data for two categorical variables**. The entries in the cells of the table can be **frequencies** (counts) or **relative frequencies** (proportions).

The levels of one variable label the rows and the levels of the other label the columns. Every individual is counted in exactly **one cell**: the cell for its row level and its column level. The **row totals** and **column totals** sit in the margins, and the **table total** in the corner.

:::checks
Σ cells in a row = row total
Σ cells in a column = column total
Σ row totals = Σ column totals = table total
:::

What it does not say. Which variable goes across and which goes down is a choice, not a rule; the table holds the same information either way. The cells count **individuals**, one each; a table in which one person could appear twice is not a two-way table. A table of relative frequencies must say what each proportion is relative to, because the next three subsections show three different answers. And it is Session 1's one-way table with a second variable: each row, on its own, is a one-way frequency table of the column variable for that row's individuals.

*Illustration:* 50 individuals, in groups A and B, each answering yes or no.

| | Yes | No | Total |
|---|---|---|---|
| Group A | 12 | 8 | 20 |
| Group B | 6 | 24 | 30 |
| **Total** | **18** | **32** | **50** |

### Joint relative frequency: one cell over the table total (2.2.A.1)

A **joint relative frequency** in a two-way table is a **cell frequency divided by the total for the entire table**.

:::formula
joint relative frequency = cell frequency ÷ table total
:::

*Cell frequency* is the count in one cell, the individuals with one particular row level **and** one particular column level. *Table total* is the count of every individual in the table.

What it does not say. A joint relative frequency describes a **pair of levels among everyone**: the proportion of all the individuals who are *A and yes*. The word to listen for is **and**. All the joint relative frequencies in a table add to 1, because every individual is in exactly one cell. It does not answer "what proportion of the A group said yes"; that restricts to the A group, and is the conditional relative frequency below.

*Illustration:* in the table above, the joint relative frequency of *Group A and yes* is 12 ÷ 50 = **0.240**. The four joint relative frequencies are 0.240, 0.160, 0.120 and 0.480, and they add to 1.

### Marginal relative frequency: a row or column total over the table total (2.2.A.2)

A **marginal relative frequency** in a two-way table is a **row total divided by the total for the entire table**, or a **column total divided by the total for the entire table**.

:::formula
marginal relative frequency = row total ÷ table total, or column total ÷ table total
:::

What it does not say. A marginal relative frequency is Session 1's relative frequency for **one variable on its own**, ignoring the other. It takes its name from the margins, where the totals sit. The row marginals add to 1, and so do the column marginals. Marginal relative frequencies say **nothing** about the relationship between the variables: two tables with the same margins can have completely different cells.

*Illustration:* Group A's marginal relative frequency is 20 ÷ 50 = **0.400**; *yes* has 18 ÷ 50 = **0.360**.

### Conditional relative frequency: restricting to one level (2.2.A.3)

A **conditional relative frequency** is a relative frequency **computed by restricting to a particular level, or category of interest**. A conditional relative frequency can be **a cell frequency in a row divided by the total for that row**, or **a cell frequency in a column divided by the total for that column**.

:::formula
conditional relative frequency = cell frequency ÷ its row total, or cell frequency ÷ its column total
:::

The total underneath is the total of the level you **restrict to**, the condition. Everything outside that row, or that column, is ignored.

What it does not say. The condition is announced by the words **of**, **among**, **within** or **for**: "*of the Group A individuals*, what proportion said yes?" restricts to the A row. The conditional relative frequencies inside one level add to 1, because together they cover everyone at that level; rounded values may add to 0.999 or 1.001, as in Session 1, and a larger gap is an error. The course's convention for writing them: compute each from the counts, give proportions to 3 decimal places and percentages to 1, and say the condition in the sentence: *"Of the 20 Group A individuals, 12, or 60.0%, said yes."*

*Illustration:* of Group A, 12 ÷ 20 = **0.600** said yes; of Group B, 6 ÷ 30 = **0.200** said yes.

### Rows or columns: conditioning the other way asks a different question (2.2.A.3)

A cell can be divided by its **row total** or by its **column total**. The two answers are different numbers, answering different questions, and the question decides which.

| Question | Restricts to | Calculation |
|---|---|---|
| Of the Group A individuals, what proportion said yes? | the A **row** | 12 ÷ 20 = 0.600 |
| Of the individuals who said yes, what proportion are in Group A? | the yes **column** | 12 ÷ 18 = 0.667 |

What it does not say. Nothing in the cell itself says which total to use; only the wording does. So the first step is always to find the condition, the words after *of*, *among* or *given*, and put **that** level's total underneath. The course description's own sample question is phrased *"of all pints of blood classified as positive, approximately what proportion is blood type A?"*: the condition is *positive*, so the positive total goes underneath, whatever order the table's rows and columns are in. Swapping the condition is the most common error with two-way tables, and it will cost marks again in Session 10, where these two numbers become two different **conditional probabilities**.

*Illustration:* of the 32 who said no, 8 ÷ 32 = 0.250 are in Group A; of the 20 in Group A, 8 ÷ 20 = 0.400 said no. Same cell, two questions, two answers.

### Side-by-side bar charts (2.1.A.2)

**Side-by-side bar charts**, **segmented bar charts** and **mosaic plots** are examples of graphs used to **display the relationship between two categorical variables**. In these graphs, **the frequency or relative frequency of each category, or level, of one of the categorical variables is displayed for each category of the other categorical variable** (2.1.A.2). This subsection and the next two take them one at a time.

A **side-by-side bar chart** puts a **cluster of bars** at each level of one variable, the groups, with one bar for each level of the other variable. A bar's height is a frequency, or the **conditional relative frequency** of that level **within that group**.

What it does not say. Read it in two directions: **within a cluster**, the bars show how one group is distributed across the categories; **across clusters**, bars of the same colour compare one category from group to group, and the eye judges those heights accurately. When the groups are different sizes, the heights must be relative frequencies within each group, for exactly Session 2's reason: bars of counts mix up "more of this category" with "a bigger group". The bars in one cluster add to 100%, but nothing in the picture shows it, and the chart shows nothing about how big each group is.

*Illustration:* a second made-up table, 100 individuals in groups A (60) and B (40), each in one of three categories X, Y and Z. Within A: X 30, Y 18, Z 12, so 50%, 30%, 20%. Within B: X 8, Y 12, Z 20, so 20%, 30%, 50%.

![Side-by-side bar chart of the made-up table: within Group A, X 50%, Y 30%, Z 20%; within Group B, X 20%, Y 30%, Z 50%](figures/s08-theory-side-by-side.svg)

*Each cluster is one group. The X bars, blue, fall from 50% in Group A to 20% in Group B; the Z bars rise from 20% to 50%. The Y bars are level at 30%.*

### Segmented bar charts (2.1.A.2)

A **segmented bar chart** draws **one bar for each level** of one variable. When it shows relative frequencies, every bar is **100% tall**, and it is divided into **segments**, one for each level of the other variable, whose heights are the **conditional relative frequencies** within that group.

What it does not say. A segment's value is its **height**, the top edge minus the bottom edge; only the bottom segment can be read straight off the axis. Reading the top of the Y segment in Group A gives 80%, which is X and Y together, not Y. Each bar is Session 2's pie chart unrolled into a column: the parts of one whole, which is why the segments stack to 100%. Because every bar is the same height, a segmented bar chart of relative frequencies **hides the group sizes**: a group of 4 and a group of 4,000 look equally tall. The bottom segments are the easiest to compare across bars, because they share a baseline; the middle ones are the hardest.

*Illustration:* the same made-up table as above.

![Segmented bar chart of the made-up table: Group A split X 50%, Y 30%, Z 20%; Group B split X 20%, Y 30%, Z 50%](figures/s08-theory-segmented.svg)

*Both bars are 100% tall, although Group A has 60 individuals and Group B only 40. The Y segments are the same height, 30%, but sit at different levels, which is why they look different.*

### Mosaic plots, where widths carry the marginal relative frequencies (2.1.A.2)

A **mosaic plot** is a segmented bar chart in which each bar's **width** is proportional to the size of its group. The course description names the mosaic plot without describing it; this is the standard construction, and the one exam questions show.

- Each bar's **width** is the **marginal relative frequency** of its group, so the widths add to the whole width.
- Within each bar, the segment **heights** are the **conditional relative frequencies**, exactly as in a segmented bar chart.
- So each tile's **area**, width times height, is the **joint relative frequency** of that cell.

:::formula
tile area = (row total ÷ table total) × (cell ÷ row total) = cell ÷ table total
:::

What it does not say. A tall segment is a large share **of its group**, not necessarily many individuals: in a narrow bar, a tall segment can be a small part of the whole table. Read the three things from three features: **widths** for the marginal relative frequencies, **heights** for the conditional ones, **areas** for the joint ones. A mosaic plot shows everything a segmented bar chart shows plus the group sizes, at the price of exact values, which are harder to read. Built the other way round, with bars for the column variable, it shows the other conditioning: a different picture of the same table.

*Illustration:* Group A's bar is 60 ÷ 100 = 0.6 of the width and Group B's 0.4. The tile for *A and X* is 0.6 wide and 0.5 high, so its area is 0.6 × 0.5 = 0.30 of the whole, which is 30 ÷ 100, the joint relative frequency.

![Mosaic plot of the made-up table: Group A's bar is 60% of the width and Group B's 40%; heights as in the segmented bar chart](figures/s08-theory-mosaic.svg)

*The same heights as the segmented bar chart, but Group A's bar is half as wide again as Group B's. The largest tile, A and X, is 30% of the area, the largest cell.*

### Choosing among the three graphs (2.1.A.2)

All three graphs show the relative frequency of one variable's levels within each level of the other. They differ in what they make easy to see.

| Graph | Easy to read | Hidden or hard |
|---|---|---|
| Side-by-side bar chart | one category compared across groups, by bar height | that each cluster is a whole; group sizes |
| Segmented bar chart | each group as a whole; the bottom segment across groups | middle segments; group sizes |
| Mosaic plot | each group as a whole, **and** the group sizes (widths), **and** joint shares (areas) | exact values, especially in narrow bars |

What it does not say. No graph is best in general; the exam asks which graph shows a particular feature, or what a given graph shows and does not show, and the answer names the feature (Skill 4.A). A two-way table of counts holds everything any of the graphs shows, and more exactly; the graphs make the comparison visible.

*Illustration:* the question "which group is larger?" can be answered from the table or the mosaic plot, but not from a segmented or side-by-side bar chart of relative frequencies.

### Association between two categorical variables (2.1.A.3, 2.2.B.1)

**Graphical representations** of two categorical variables can be used to **compare the relationship of one categorical variable across the levels of the other** categorical variable and **determine whether the two variables are associated** (2.1.A.3). **Summary statistics** for two categorical variables can be used to **compare distributions for evidence of association** between the two variables (2.2.B.1).

The rule. Two categorical variables are **associated** when the **conditional relative frequencies of one variable differ across the levels of the other**. When they are the same, or nearly the same, for every level, the variables are **not associated**: knowing an individual's level of one variable tells you nothing about the other.

In the graphs: segmented bars that look alike, side-by-side clusters that repeat the same pattern, or a mosaic plot whose horizontal divisions run straight across, all mean no association. Bars that differ mean association.

What it does not say. It is decided by **conditional relative frequencies**, never by counts: two groups of different sizes always have different counts (Session 2's rule). The verdict does not depend on the direction of conditioning: when the row conditionals are the same in every row, the column conditionals are the same in every column too. Association is **not cause**: most two-way tables come from observational data, and Session 6's rule holds (only random assignment licenses cause). And "nearly the same" is a judgement. With sample data, a small difference could be chance, and deciding whether it is too large for chance is the chi-square test in Session 17; until then, describe how large the difference is, and say "strong evidence" only when the differences are large.

*Illustration:* in the left panel below, both groups split 50%, 30%, 20%: no association, although Group A has 30 X individuals and Group B only 20. In the right panel, the made-up table from above: the splits differ, so group and category are associated.

![Two segmented bar charts: on the left both groups split X 50%, Y 30%, Z 20%, not associated; on the right the groups split differently, associated](figures/s08-theory-association.svg)

*Left: the counts differ (30 against 20 in category X) because the groups differ in size, but every share is the same. Right: X falls from 50% to 20% and Z rises from 20% to 50%.*

### Justifying a claim from a two-way table or its graphs (2.1.B.1, 2.2.C.1)

**Tabular and graphical representations** for the distributions of two categorical variables **may reveal information that can be used to justify claims about the variable in context** (2.1.B.1). **Summary statistics** for two categorical variables **may reveal information that can be used to justify claims about the variables in context** (2.2.C.1).

A justified claim uses Session 1's template: **state the claim · quote the numbers · say what they do and do not establish · keep it in context.** For a two-way table, "the numbers" means the **conditional relative frequencies being compared, both of them**, with the condition named.

What it does not say. One number cannot justify a comparison: "60.0% of Group A said yes" says nothing about Group B. A joint relative frequency does not justify a claim about a group, because it is a share of everyone. Counts do not justify a comparison between groups of different sizes. And the claim must not go beyond the data: a census describes its population, a random sample generalises to its population (Session 6), and neither gives cause without random assignment.

*Illustration:* "Group A individuals were more likely to say yes than Group B individuals: 60.0% of Group A (12 of 20) against 20.0% of Group B (6 of 30)."

### Random process, outcome and event (2.3.A.1–3)

A **random process** generates **results that are determined by chance** (2.3.A.1). An **outcome** is **the result of one trial of a random process** (2.3.A.2). An **event** is **a collection of outcomes** (2.3.A.3).

A **trial** is one run of the random process: one roll of a die, one toss of a coin, one clinic session.

What it does not say. "Random" does not mean haphazard or patternless: each result is unpredictable, but many results show a regular pattern, and that regularity is what the next four subsections use. What counts as the outcome is a choice made to fit the question: for a clinic session it could be the list of which patients came, or only how many came. An event can contain one outcome or many; "an even number" is one event made of three outcomes.

*Illustration:* roll a die once. The random process is the roll; one outcome is 4; the event *even* is the collection {2, 4, 6}, and it happens when any of those three outcomes does.

### Simulation: outcomes assigned to values chosen by chance (2.3.A.4)

**Simulation** is **a way to model random events such that simulated outcomes closely match real-world outcomes**. **All possible outcomes are associated with a value to be determined by chance.** **Record the counts of simulated outcomes and the count total.**

In practice the values are usually **digits from a random number generator**, each of 0 to 9 equally likely, and the outcomes are given shares of the digits equal to their probabilities.

What it does not say. A simulation is only as good as its **model**. If the probabilities put in are wrong, or the simulated results influence each other when the real ones do not (or the other way round), the simulated outcomes will not match the real ones, however many trials are run. The digits must match the probability exactly: a probability of 0.1 is one digit of the ten; a probability of 0.155 needs three-digit numbers, 000 to 154 out of 000 to 999. And one trial may use several digits: a trial is one run of the **whole** process being modelled.

*Illustration:* an outcome with probability 0.3 is modelled by the digits 0, 1 and 2, three of the ten; the digits 3 to 9 mean it does not happen.

### Five steps for carrying out a simulation (2.3.A.4)

The course organises 2.3.A.4 into five steps. The course description gives the content of the steps, not this list, and the exam marks the content: a stated model, a correct assignment of values, a clear trial, counts, and an estimate in context.

1. **Model.** State the random process, the probability of each outcome, and any assumption, such as that one result does not affect another.
2. **Assign.** Say which random values stand for which outcomes, so that each outcome's share of the values equals its probability.
3. **Define one trial and the event.** Say what one trial consists of (how many digits, standing for what), what is recorded, and what counts as the event happening.
4. **Run many trials.** Record the count of each simulated outcome, and the count total.
5. **Estimate.** Divide, and state the estimate in context, as an estimate.

:::formula
estimated probability of the event = (number of trials in which the event happened) ÷ (total number of trials)
:::

What it does not say. The denominator is the number of **trials**, not the number of digits used. A trial that uses five digits counts once. Getting that wrong is Scenario B's trap. Step 1's assumptions are part of the answer: an estimate from a simulation is an estimate **under the model**.

*Illustration:* the event *at least one 0 in two digits*, where each digit stands for one try with probability 0.1 of the outcome. Five trials: 37, 05, 90, 41, 22. The event happened in 2 of the 5 trials (05 and 90), so the estimate is 2 ÷ 5 = 0.4, from ten digits and five trials.

### Probability as long-run relative frequency, estimated from data (2.3.A.5–6)

The **probability** of an outcome or event is its **long-run relative frequency**, that is, its **relative frequency over a large number of trials** (2.3.A.5). The **relative frequency** of an outcome or event **determined from empirical data** can be used to **estimate the actual, or true, probability** of that outcome or event (2.3.A.6).

:::formula
relative frequency of an event = (number of times it happened) ÷ (number of trials)
:::

This is Session 1's rf = f ÷ n, with trials in place of individuals.

What it does not say. A relative frequency from a limited number of trials, or from a limited set of records, is an **estimate** of the probability, not the probability; the probability is the value the relative frequency settles on in the long run. Estimates come from two places: **real data**, such as a hospital's records of how often appointments are missed, and **simulated data**. A probability is not a promise about the next trial: a probability of 0.9 of turning up does not mean the next patient will come.

*Illustration:* a process repeated 1,000 times, with the event happening 312 times, gives an estimated probability of 312 ÷ 1,000 = 0.312.

### The law of large numbers (2.3.A.7)

The **law of large numbers** states that **for independent trials, as the number of trials increases, the long-run relative frequency of the outcome or event gets closer and closer to a single value**.

**Independent trials** are trials in which the result of one does not change the chances in another. The formal definition of independent events is topic 2.7, in Session 10.

What it does not say. It says nothing about the **short run**: after a few trials the relative frequency can be far from the value it will settle on, and two short runs of the same process usually disagree. It does not say the results **even out** by compensating: after a run of tails, the next toss of a fair coin is still heads with probability 0.5, because independent trials have no memory. The count of heads can drift further from half the tosses even while the relative frequency closes in on 0.5. The single value is the **probability** (2.3.A.5), which is why more trials give a better estimate.

*Illustration:* suppose a fair coin gives 7 heads in its first 10 tosses (0.7, two more than half) and 5,040 heads in 10,000 (0.504, forty more than half). The gap in the **count** grew from 2 to 40; the gap in the **relative frequency** shrank from 0.2 to 0.004.

### Eight check questions before the scenarios

Use the first made-up table (groups A and B, yes and no: 12, 8; 6, 24) for questions 1 to 4.

:::script
ask | Ask | "What proportion of all 50 are in Group B and said no? Which kind of relative frequency is that?"
listen | Listen for | 24 ÷ 50 = 0.480, a joint relative frequency: one cell over the table total.
ask | Ask | "Of those who said yes, what proportion are in Group B?"
listen | Listen for | 6 ÷ 18 = 0.333. The condition is *said yes*, so the yes column total, 18, goes underneath.
ask | Ask | "Group B has 24 no answers and Group A only 8. Does that alone show Group B is more likely to say no?"
listen | Listen for | No: the groups are different sizes. Compare 24 ÷ 30 = 80.0% with 8 ÷ 20 = 40.0%.
ask | Ask | "In a mosaic plot of this table with a bar for each group, which bar is wider, and what does its width show?"
listen | Listen for | Group B's: its width is 30 ÷ 50 = 0.600, the marginal relative frequency of Group B.
ask | Ask | "Two segmented bars look identical. What does that say about the two variables?"
listen | Listen for | Not associated: the conditional relative frequencies are the same in both groups.
ask | Ask | "In a simulation, what are you counting in the numerator and in the denominator?"
listen | Listen for | The number of trials in which the event happened, over the total number of trials.
ask | Ask | "How would you use random digits for an outcome with probability 0.4?"
listen | Listen for | Four of the ten digits, say 0 to 3, mean the outcome happens; 4 to 9 mean it does not.
ask | Ask | "A fair coin has landed tails five times running. Is heads now more likely than 0.5?"
listen | Listen for | No. The tosses are independent; the law of large numbers is about the long-run relative frequency, not about the next toss making up for the others.
ifsay | If any answer goes wrong | Go back to that subsection and reread its "what it does not say" paragraph together before Scenario A. The scenarios lean on every one of them.
:::

---

## 54–92 min · Scenario A — Lincoln High's travel register: home area and travel mode

Lincoln High from Sessions 1 to 7, with its **1,842 students** in three home areas. In Session 7 the office's bus-pass list, a census, showed that 651 students travel mainly by bus. This year the office went further: every student's record now carries their **main travel mode**, taken from the travel form every family completes at registration. So there is a **census** of two categorical variables, home area and travel mode, for all 1,842 students.

**The trap this scenario carries: conditioning the wrong way.** "85.0% of the Villages students take the bus" and "38.4% of the bus users live in the Villages" come from the same cell, 250 students, divided by two different totals. Students who can do every calculation still swap them, because the table does not say which total to use; only the question does. The course description's sample question is built on exactly this, and Session 10 will turn the two numbers into two different conditional probabilities.

### The whole school in one two-way table

| Home area | Bus | Car | Walk or cycle | Total |
|---|---|---|---|---|
| Town, within 3 km | 85 | 203 | 558 | 846 |
| Suburbs, 3 to 10 km | 316 | 281 | 105 | 702 |
| Villages, beyond 10 km | 250 | 38 | 6 | 294 |
| **Total** | **651** | **522** | **669** | **1,842** |

:::script
ask | Ask | "What are the individuals, and what are the two variables?"
listen | Listen for | The individuals are the 1,842 students. The variables are home area (Town, Suburbs, Villages) and main travel mode (bus, car, walk or cycle), both categorical.
intro | Recall | *Two-way tables, also called contingency tables (2.1.A.1)*: each student is counted in exactly one cell.
ask | Ask | "Check the table: do the row totals and the column totals both come to 1,842? And where have you seen 651 before?"
listen | Listen for | 846 + 702 + 294 = 1,842, and 651 + 522 + 669 = 1,842. The 651 bus users are Session 7's bus-pass census, and the Bus column's cells, 85, 316 and 250, are its three home areas.
ask | Ask | "Is this a sample or a population? What does that mean for any proportion you work out?"
listen | Listen for | The whole population, a census: every proportion is a parameter of Lincoln High (Session 1), and there is no question of generalising.
:::

### Joint, marginal and conditional shares of the 1,842 students

:::script
ask | Ask | "What proportion of all 1,842 students live in the Villages and travel by bus?"
listen | Listen for | 250 ÷ 1,842 = 0.136, a joint relative frequency.
intro | Recall | *Joint relative frequency: one cell over the table total (2.2.A.1)*: the word to hear was **and**.
ask | Ask | "What proportion of the school lives in the Villages? And what proportion travels by bus?"
listen | Listen for | 294 ÷ 1,842 = 0.160 and 651 ÷ 1,842 = 0.353. Both are marginal relative frequencies; 0.353 is Session 7's parameter.
intro | Recall | *Marginal relative frequency: a row or column total over the table total (2.2.A.2)*.
ask | Ask | "Of the Villages students, what proportion travel by bus?"
listen | Listen for | 250 ÷ 294 = 0.850, a conditional relative frequency: restricted to the Villages row, so the Villages total goes underneath.
intro | Recall | *Conditional relative frequency: restricting to one level (2.2.A.3)*.
:::

Now have the student build the whole table of conditional relative frequencies within each home area. Do not build it yourself; this is Skill 3.B and they need the pen. Each cell is divided by **its own row total**.

| Home area | Bus | Car | Walk or cycle | Total |
|---|---|---|---|---|
| Town (846) | 85 ÷ 846 = 0.100 (10.0%) | 203 ÷ 846 = 0.240 (24.0%) | 558 ÷ 846 = 0.660 (66.0%) | 1.000 |
| Suburbs (702) | 316 ÷ 702 = 0.450 (45.0%) | 281 ÷ 702 = 0.400 (40.0%) | 105 ÷ 702 = 0.150 (15.0%) | 1.000 |
| Villages (294) | 250 ÷ 294 = 0.850 (85.0%) | 38 ÷ 294 = 0.129 (12.9%) | 6 ÷ 294 = 0.020 (2.0%) | 0.999 |

:::checks
Town row sums to 1.000
Suburbs row sums to 1.000
Villages row: 0.999, rounding
:::

:::script
ask | Ask | "The Villages row adds to 0.999. Mistake?"
listen | Listen for | Rounding: each value was rounded to three places. The unrounded shares, 250/294 + 38/294 + 6/294, add to exactly 1. A gap bigger than 0.001 or so would be an error.
:::

### Of the Villages students, or of the bus users?

This is the trap. The county's transport officer reads the table and writes:

> *"85% of Lincoln High's bus users come from the Villages, so the Villages route is where almost all our bus spending goes."*

:::script
ask | Ask | "Is the officer right? Where did the 85% come from?"
listen | Listen for | No. 85.0% is 250 ÷ 294, which is **of the Villages students**. The officer's sentence is about **the bus users**, so it needs the Bus column's total underneath: 250 ÷ 651 = 0.384. Only 38.4% of the bus users come from the Villages.
intro | Recall | *Rows or columns: conditioning the other way asks a different question (2.2.A.3)*: find the condition, and put that level's total underneath.
ifsay | If "it's the same cell, so it's the same number" | "Same 250 students. Out of how many? The officer is talking about all the bus users. How many bus users are there?" 651. So 250 of 651.
ask | Ask | "So where do most bus users come from?"
listen | Listen for | The Suburbs: 316 ÷ 651 = 0.485, 48.5% of bus users. More Suburbs students take the bus than Villages students, although a Villages student is far more likely to.
ask | Ask | "Write both true sentences about those 250 students, each with its condition."
listen | Listen for | *"Of the 294 Villages students, 250 (85.0%) travel by bus."* *"Of the 651 bus users, 250 (38.4%) live in the Villages."*
:::

> **The sentence to write down:** *The condition is the group I am restricting to, named after "of" or "among". Its total goes underneath: of the Villages students, 250 ÷ 294 = 85.0% take the bus; of the bus users, 250 ÷ 651 = 38.4% live in the Villages.*

### Three graphs of travel mode within each home area

Show the three graphs in turn. They show the same conditional relative frequencies, the ones the student has calculated.

![Side-by-side bar chart of travel mode within each home area at Lincoln High](figures/s08-lincoln-side-by-side.svg)

*Side-by-side bars. Each cluster is one home area; the heights are the percentages within that area. The blue bus bars climb from 10.0% in Town to 85.0% in the Villages.*

:::script
ask | Ask | "From the side-by-side bars: in which home area is walking or cycling most common, and how do you compare bus use across the areas?"
listen | Listen for | Town, 66.0% of its students. Bus use is compared by the three blue bars' heights: 10.0%, 45.0%, 85.0%.
intro | Recall | *Side-by-side bar charts (2.1.A.2)*: compare bars of one colour across clusters.
:::

![Segmented bar chart of travel mode within each home area at Lincoln High](figures/s08-lincoln-segmented.svg)

*Segmented bars. Each home area is one bar, 100% tall. The bus segment is at the bottom of every bar, so it is the easiest to compare.*

:::script
ask | Ask | "Read the car segment in the Suburbs bar."
listen | Listen for | From 45% to 85%: its height is 40.0%. Not 85%, which is where its top edge is: that is bus and car together.
intro | Recall | *Segmented bar charts (2.1.A.2)*: a segment's value is its height, top minus bottom.
ask | Ask | "Looking only at this chart, which home area has the most students?"
listen | Listen for | It cannot tell you: every bar is 100% tall. The Villages bar looks as big as Town's, and Town has almost three times as many students.
:::

![Mosaic plot of home area and travel mode at Lincoln High](figures/s08-lincoln-mosaic.svg)

*Mosaic plot. The same heights as the segmented bars, but each column's width is the home area's share of the school: Town 45.9%, Suburbs 38.1%, Villages 16.0%. The Villages walk-or-cycle tile, 2.0% of a narrow column, is the thin strip at its top.*

:::script
ask | Ask | "What does the mosaic plot show that the segmented bar chart does not?"
listen | Listen for | How big each home area is: the widths are the marginal relative frequencies, 846, 702 and 294 out of 1,842.
intro | Recall | *Mosaic plots, where widths carry the marginal relative frequencies (2.1.A.2)*.
ask | Ask | "The Villages bus tile is very tall. Is it the biggest group of bus users?"
listen | Listen for | No. Tall means a large share of the Villages; the tile's area is 0.160 × 0.850 = 0.136 of the whole, which is 250 ÷ 1,842. The Suburbs bus tile, 0.381 × 0.450 = 0.172, is larger: 316 students. The mosaic shows the officer's mistake at a glance.
ask | Ask | "Which graph would you give the principal to show how bus use changes with distance, and which to show where the bus users live?"
listen | Listen for | Either bar chart shows the change in bus use from 10.0% to 85.0%. Only the mosaic plot, of the three, also shows the group sizes, so it is the one that shows where the bus users are, by area.
intro | Recall | *Choosing among the three graphs (2.1.A.2)*.
:::

### Conditioning on travel mode instead

The table can be read the other way: within each travel mode, which home areas do the students come from? Each cell is now divided by **its column total**.

| Home area | Bus (651) | Car (522) | Walk or cycle (669) |
|---|---|---|---|
| Town | 85 ÷ 651 = 0.131 (13.1%) | 203 ÷ 522 = 0.389 (38.9%) | 558 ÷ 669 = 0.834 (83.4%) |
| Suburbs | 316 ÷ 651 = 0.485 (48.5%) | 281 ÷ 522 = 0.538 (53.8%) | 105 ÷ 669 = 0.157 (15.7%) |
| Villages | 250 ÷ 651 = 0.384 (38.4%) | 38 ÷ 522 = 0.073 (7.3%) | 6 ÷ 669 = 0.009 (0.9%) |
| **Total** | **1.000** | **1.000** | **1.000** |

![Segmented bar chart of home area within each travel mode at Lincoln High](figures/s08-lincoln-segmented-by-mode.svg)

*The same table, conditioned on travel mode. The bus bar answers the officer's question: 48.5% of bus users are from the Suburbs and 38.4% from the Villages.*

:::script
ask | Ask | "This chart and the first segmented chart look nothing alike. Do they disagree about whether home area and travel mode are associated?"
listen | Listen for | No. Both show bars that differ from one another, so both show an association. They answer different questions: the first shows how each area's students travel; this one shows where each mode's students live.
intro | Recall | *Association between two categorical variables (2.1.A.3, 2.2.B.1)*: the verdict does not depend on the direction of conditioning.
:::

### Are home area and travel mode associated?

:::script
ask | Ask | "Are home area and travel mode associated at Lincoln High? Give the numbers."
listen | Listen for | Yes, strongly. The conditional relative frequencies of travel mode differ greatly across the home areas: bus use is 10.0% in Town, 45.0% in the Suburbs and 85.0% in the Villages, and walking or cycling falls from 66.0% to 15.0% to 2.0%.
ifsay | If "yes: 316 Suburbs students take the bus and only 85 Town students" | "Town has 846 students and the Suburbs 702. What does Session 2 say about comparing counts from groups of different sizes?" Compare shares: 10.0% against 45.0%. Here the conclusion happens to be right, and the evidence is still wrong.
ask | Ask | "Does living in the Villages cause students to take the bus?"
listen | Listen for | This is observational data, a census with nothing assigned, so it shows an association and cannot on its own show cause. Distance is an obvious explanation, and the table is consistent with it; it does not prove it. And because it is a census, there is no sampling to worry about: the association is a fact about all 1,842 students.
:::

:::note red Extension — not in the course description: Simpson's paradox
Barron's (pdf 158–160) teaches **Simpson's paradox**: a comparison between two groups can reverse when a third variable is taken into account. Its example has one surgeon with a higher survival rate than another in both good-condition and poor-condition patients, and a lower one overall, because he operates on many more poor-condition patients. The course description never mentions it, and it will not be examined by name. The idea underneath it is examined, and it is Session 6's: a comparison can be confounded by a third variable.
:::

### The claim the principal may write

:::script
ask | Ask | "The principal wants one sentence for the governors about how students' travel depends on where they live. Write it, with the numbers."
listen | Listen for | The model below: the claim, both ends of the comparison with the condition named, what it does not establish, and the context.
intro | Recall | *Justifying a claim from a two-way table or its graphs (2.1.B.1, 2.2.C.1)*.
:::

> **The model claim (2.2.C):** *"At Lincoln High, how students travel is strongly associated with where they live. Of the 846 Town students, 10.0% travel mainly by bus and 66.0% walk or cycle; of the 294 Villages students, 85.0% travel by bus and 2.0% walk or cycle. These figures come from the travel register for all 1,842 students, so they describe the whole school. They show an association, not that home area causes the choice of travel."*

**The link forward.** Choose one Lincoln High student at random. The probability that they travel by bus, **given** that they live in the Villages, is 250 ÷ 294 = 0.850; the probability that they live in the Villages, given that they travel by bus, is 250 ÷ 651 = 0.384. Session 10 calls these **conditional probabilities** and defines them on tables exactly like this one. Say so now, and do not go further.

---

## 92–112 min · Activity — Quiz-Quiz-Trade with the hospital waiting table

The course description's Sample Instructional Activity for topics 2.1–2.2: *"Give students a card containing a question with a two-way table and have them write the answer on the back. Then have them stand up and find a partner. One student quizzes the other, and then they reverse roles. Have them switch cards, find a new partner, and repeat the process."*

**The one-to-one conversion.** There is no room of partners, so the four moves become four rounds with you. In **Round 1** the student writes the answers on the backs of four cards, which is the move that makes each card theirs. In **Round 2** the student quizzes you with those cards, and you answer two of them wrongly on purpose: checking a partner's answer against your own back is where the calculation is really learned, and the two planted errors are the two the exam uses. In **Round 3** the roles reverse and you quiz the student with four harder cards. In **Round 4**, the trade, the "new partner" is a new table: the student answers four cards on a table they have not seen, which is the repetition the activity is for. A point for each card answered or error caught with its fix: 14 in all, and 11 is the standard.

### The hospital waiting table the cards are written on

In Session 3 the hospital survey recorded, for each surveyed patient, the minutes from arrival to being seen by a doctor. For the 84 St Mary's patients and the 71 Riverside patients, those waits are now grouped into three categories. Every card uses this table.

| Hospital | Under 20 min | 20 to 39 min | 40 min or more | Total |
|---|---|---|---|---|
| St Mary's | 8 | 46 | 30 | 84 |
| Riverside | 14 | 54 | 3 | 71 |
| **Total** | **22** | **100** | **33** | **155** |

### Round 1: the student writes the backs of cards 1–4

Hand over cards 1 to 4, fronts only. The student writes each answer, with its calculation, on the back.

| Card | Front | Back |
|---|---|---|
| 1 | What proportion of all 155 patients were St Mary's patients who waited 40 minutes or more? | 30 ÷ 155 = 0.194, joint |
| 2 | What proportion of all 155 patients waited under 20 minutes? | 22 ÷ 155 = 0.142, marginal |
| 3 | Of the Riverside patients, what proportion waited under 20 minutes? | 14 ÷ 71 = 0.197, conditional on the Riverside row |
| 4 | Of the patients who waited 40 minutes or more, what proportion were at St Mary's? | 30 ÷ 33 = 0.909, conditional on the 40-or-more column |

### Round 2: the student quizzes the tutor with cards 1–4

The student reads each card to you and checks your answer against their back. Answer cards 2 and 4 correctly. Answer cards 1 and 3 with the two classic errors:

:::script
ask | Card 1, your answer | "30 ÷ 84 = 0.357." The student must catch it: that is the proportion **of St Mary's patients** who waited 40 or more, a conditional relative frequency. The card asks about **all 155**, a joint one: 30 ÷ 155 = 0.194.
ask | Card 3, your answer | "14 ÷ 22 = 0.636." The student must catch it: that is the proportion **of the under-20 patients** who were at Riverside, conditioned the wrong way. The card restricts to Riverside: 14 ÷ 71 = 0.197.
ifsay | If the student accepts either | Ask them to read the card's condition aloud, word by word, and say which total it names. Then they mark it.
intro | Recall | *Joint relative frequency (2.2.A.1)* and *Rows or columns: conditioning the other way asks a different question (2.2.A.3)*.
:::

A point for each error caught **with its fix**, two in all.

### Round 3: roles reversed, cards 5–8

Now you quiz the student. Card 8 needs the mosaic plot below on the screen.

| Card | Front | Back |
|---|---|---|
| 5 | What proportion of the 155 patients were at St Mary's, and where would you see it in a mosaic plot with a bar for each hospital? | 84 ÷ 155 = 0.542, marginal. It is the width of the St Mary's bar |
| 6 | "Riverside had more patients who waited 20 to 39 minutes: 54 against 46. So a Riverside patient was more likely to wait 20 to 39 minutes." Is the reasoning sound? | The conclusion is true and the reasoning is not. Compare shares, not counts: 54 ÷ 71 = 76.1% of Riverside patients against 46 ÷ 84 = 54.8% of St Mary's |
| 7 | Are waiting time and hospital associated in these data? Justify with numbers. | Yes. 35.7% of St Mary's patients (30 of 84) waited 40 minutes or more, against 4.2% of Riverside's (3 of 71); 9.5% of St Mary's waited under 20, against 19.7% of Riverside's |
| 8 | In the mosaic plot, which tile has the largest area, and what proportion of the 155 patients does it stand for? | Riverside, 20 to 39 minutes: 0.458 wide and 0.761 high, an area of 0.348, which is 54 ÷ 155. It is larger than St Mary's 20-to-39 tile, 46 ÷ 155 = 0.297, although that tile is in the wider bar |

![Mosaic plot of hospital and waiting time for the 155 surveyed patients at St Mary's and Riverside](figures/s08-hospital-mosaic.svg)

*Card 8's plot. St Mary's bar is wider, because it had more patients (54.2% of the 155). Its orange 40-minutes-or-more segment is tall, 35.7% of its patients; Riverside's is a thin strip, 4.2%.*

:::script
ifsay | If card 7 is answered "yes, 30 St Mary's patients waited 40 minutes and only 3 at Riverside" | "Right answer. Would it still be evidence if St Mary's had had 840 patients?" Counts depend on the group size; the shares, 35.7% and 4.2%, are the evidence.
intro | Recall | *Association between two categorical variables (2.1.A.3, 2.2.B.1)* and *Mosaic plots, where widths carry the marginal relative frequencies (2.1.A.2)*.
:::

A caution for card 7: these are 155 surveyed patients, a sample, so the right word is *these data show an association*. Whether a difference this size could be chance is Session 17's test; here, 35.7% against 4.2% is too large for anyone to put down to chance by eye, and the student should say how large it is.

### Round 4: trade the decks and meet the café's table

Swap decks, and bring in a "new partner": a table the student has not seen. The café from Sessions 1 to 7 has **1,260 loyalty-card members**, 504 using the app and 756 a paper card (Session 6). Its till records each member's usual visit time.

| Card type | Before 10 am | 10 am to 2 pm | After 2 pm | Total |
|---|---|---|---|---|
| App | 280 | 140 | 84 | 504 |
| Paper card | 210 | 378 | 168 | 756 |
| **Total** | **490** | **518** | **252** | **1,260** |

Read the four cards at speed; one point each.

| Card | Front | Back |
|---|---|---|
| T1 | What proportion of all members use the app and usually visit before 10 am? | 280 ÷ 1,260 = 0.222, joint |
| T2 | What proportion of all members usually visit after 2 pm? | 252 ÷ 1,260 = 0.200, marginal |
| T3 | Of the app users, what proportion usually visit before 10 am? And of the before-10 visitors, what proportion use the app? | 280 ÷ 504 = 0.556, and 280 ÷ 490 = 0.571. Two conditions, two totals; both needed for the point |
| T4 | Are card type and visit time associated? One comparison is enough. | Yes: 55.6% of app users visit before 10 am, against 27.8% of paper-card users (210 of 756) |

Total out of 14: Round 1 out of 4, Round 2 out of 2, Round 3 out of 4, Round 4 out of 4. Eleven or more is the standard. Below that, the missed cards point to the theory subsection to reread before Scenario B: joint and marginal cards to their subsections, conditional cards to *Rows or columns*, association cards to *Association between two categorical variables*.

---

## 112–147 min · Scenario B — St Mary's overbooking: estimating a probability by simulation

St Mary's outpatient clinics, from Sessions 6 and 7. Session 7's experiment showed that text reminders cause fewer missed appointments, and the hospital now texts every outpatient the day before. At one clinic, each morning session has **10 appointment slots**. The records of the **1,000 appointments** at that clinic since the texts began show that **100 were missed**.

The clinic manager wants to stop wasting slots. Her proposal: book **11 patients** into each 10-slot session. If one of the 11 misses, every slot is used. The risk is a session in which **all 11 turn up**, and one patient cannot be seen that morning. She asks: *how often will that happen?*

There is no rule yet for calculating it; Session 10 provides one. Today it is estimated the way the course description says a probability can always be estimated: by simulation.

**The trap this scenario carries: a trial is one run of the whole random process, here one clinic session of 11 patients, and the estimate counts trials.** Students who have drawn 220 random digits count the zeros among all 220 and report 21 ÷ 220 = 0.095. That number is only the miss rate that was put into the model, per patient, and it answers nothing the manager asked. The estimate is (sessions in which all 11 turned up) ÷ (sessions simulated).

### From a relative frequency to a probability model

:::script
ask | Ask | "What is the probability that a St Mary's patient at this clinic misses an appointment?"
listen | Listen for | It cannot be known exactly; it can be estimated from the records: 100 ÷ 1,000 = 0.100.
intro | Recall | *Probability as long-run relative frequency, estimated from data (2.3.A.5–6)*: a relative frequency from empirical data estimates the true probability.
ask | Ask | "The simulation will treat every booked patient as missing with probability 0.10, each independently of the others. What does 'independently' mean here, and when might it be false?"
listen | Listen for | One patient missing does not change the chance that another misses. It would be false on a day of heavy snow or a bus strike, when many patients miss together. The simulation's answer holds only under the model.
intro | Recall | *The law of large numbers (2.3.A.7)*: independent trials; and *Simulation: outcomes assigned to values chosen by chance (2.3.A.4)*: a simulation is only as good as its model.
:::

### Planning the simulation: digits, trial and event

:::script
ask | Ask | "Step 2: how will you use random digits for one patient?"
listen | Listen for | One digit per patient. Digit 0 means the patient misses; 1 to 9 mean they turn up. One digit of ten matches the probability 0.10.
ask | Ask | "Step 3: what is one trial, and what is recorded?"
listen | Listen for | One trial is one clinic session: 11 digits, one for each booked patient. Record the number of the 11 who turn up (the number of digits that are not 0).
ask | Ask | "What is the event the manager asked about? Is it one outcome or several?"
listen | Listen for | All 11 turn up: more patients than slots. With the outcome recorded as *how many turned up*, that event is the one outcome 11. The event *at least one slot unused* would be the collection of outcomes 0 to 9.
intro | Recall | *Random process, outcome and event (2.3.A.1–3)* and *Five steps for carrying out a simulation (2.3.A.4)*.
:::

> **Steps 1–3, as they would be written in an exam answer:** *Model: each of the 11 booked patients misses with probability 0.10, independently. Assign: one random digit per patient; 0 = misses, 1–9 = turns up. Trial: 11 digits, one clinic session; record how many of the 11 turn up. Event: all 11 turn up, so there are more patients than the 10 slots.*

### Twenty clinic sessions by hand

These are 220 digits from a random number generator, set out as 20 rows of 11: one row per trial. Give the student the digits and ask for Step 4: for each trial, the number who turned up; then the count of each outcome and the count total.

```
Trial  1   6 9 8 3 3 1 7 3 1 4 6
Trial  2   8 6 4 3 8 8 2 8 4 4 5
Trial  3   7 2 1 0 9 8 7 0 0 9 8
Trial  4   5 7 1 8 5 1 2 7 0 3 5
Trial  5   9 4 5 4 6 8 8 2 7 2 7
Trial  6   7 7 8 3 1 4 9 9 0 3 5
Trial  7   7 0 2 1 5 2 8 0 0 2 5
Trial  8   0 2 2 5 4 9 0 0 9 0 2
Trial  9   4 8 7 7 3 0 9 8 9 3 8
Trial 10   1 2 5 5 8 4 0 6 3 4 9
Trial 11   0 5 8 7 6 9 7 4 7 4 8
Trial 12   6 1 0 1 5 8 8 2 2 3 3
Trial 13   3 7 2 8 5 4 3 6 4 4 8
Trial 14   4 1 9 6 3 0 4 7 7 8 4
Trial 15   3 9 4 3 6 5 6 8 9 9 3
Trial 16   8 7 6 7 2 5 2 5 6 1 2
Trial 17   2 9 1 9 8 0 4 0 6 9 0
Trial 18   1 5 6 3 8 7 3 7 2 5 3
Trial 19   8 2 9 0 9 6 4 3 3 9 5
Trial 20   9 8 2 8 5 6 8 8 4 2 6
```

The number who turned up in each trial, 1 to 20: **11, 11, 8, 10, 11, 10, 8, 7, 10, 10, 10, 10, 11, 10, 11, 11, 8, 11, 10, 11**.

| Patients who turned up | 7 | 8 | 9 | 10 | 11 | Total |
|---|---|---|---|---|---|---|
| Count of trials | 1 | 3 | 0 | 8 | 8 | **20** |
| Relative frequency | 0.05 | 0.15 | 0.00 | 0.40 | 0.40 | **1.00** |

:::checks
Σ counts = 20 = count total
Σ relative frequencies = 1.00
:::

:::script
ask | Ask | "Step 5: estimate the probability that all 11 turn up."
listen | Listen for | 8 of the 20 sessions had all 11 turn up: 8 ÷ 20 = 0.40.
ask | Ask | "And the probability that exactly 10 turn up? That at least one slot is unused?"
listen | Listen for | 8 ÷ 20 = 0.40, and 4 ÷ 20 = 0.20 (the sessions with 7 or 8). The three add to 1: every session is in exactly one of the three events.
:::

### Counting sessions, not patients

This is the trap. Put a second student's answer on the screen:

> *"I counted the zeros in all the digits. There were 21 of the 220, so the probability of a missed appointment is 21 ÷ 220 = 0.095, and 199 of 220 patients turned up, which is 90.5%. So overbooking will overflow about 90% of the time."*

:::script
ask | Ask | "What has this student estimated, and what did the manager ask?"
listen | Listen for | They estimated the chance that **one patient** misses, which is the 0.10 the model put in; the 0.095 is that 0.10 with some chance variation. The manager asked how often a **session** overflows. That needs the sessions: 8 of 20.
intro | Recall | *Five steps for carrying out a simulation (2.3.A.4)*: the denominator is the number of trials, not the number of digits.
ifsay | If "but 90% of patients turned up, so 90% of sessions are full" | "In trial 3, 8 of 11 came. In trial 1, all 11. Is 'a patient turns up' the same event as 'every patient in the session turns up'?" No: a session overflows only if all 11 come, which is much rarer than any one of them coming.
ask | Ask | "Write the estimate the way an exam answer should."
listen | Listen for | *"In 8 of the 20 simulated sessions all 11 booked patients turned up, so the estimated probability that a session booked with 11 overflows is 8 ÷ 20 = 0.40."*
:::

> **The sentence to write down:** *One trial is one whole clinic session. I count the sessions in which the event happened and divide by the number of sessions, never by the number of digits.*

### The Overbooking Simulation tool: more trials

:::sim overbooking-simulation | Overbooking Simulation | 1260
The same model: 10 slots, each booked patient misses with probability 0.10, a digit per patient with 0 for a miss. It opens with one run of 20 trials at 11 booked, like the hand simulation. Ask the student to press **Run 10 trials** a few times and describe the line, then **Run 1,000 trials** until the run passes 5,000. Then **Start a new run** and compare its first 20 trials with the hand run. Last, try **12 booked**, and the event **At least one slot unused**.
:::

This is the session's one tool, and it earns its place on the standard's three tests. The law of large numbers is about what a relative frequency **does** as trials accumulate, a process; a static figure can show some finished runs, but not that each new run starts somewhere different and cannot be predicted, and not how the estimate for a policy the student chooses settles; and the student **drives** it, choosing the number booked, the miss rate, the event and how many trials to run. The static figure below is for print and for the workbook reveal.

What the student should see, from the tool's unit tests: across 200 runs of each length, the estimate from 20 trials has a standard deviation of about 0.10 around the long-run value, from 200 trials about 0.03, and from 2,000 trials about 0.01. Only a third of 20-trial runs landed within 0.05 of the long-run value; every 5,000-trial run did.

![Running relative frequency of an overfull session against the number of trials, for the hand run and five long runs](figures/s08-stmarys-running.svg)

*The hand run (orange) starts at 1.0, because the first two sessions overflowed, and ends at 0.40 after 20. Five runs of 10,000 sessions (grey) wander widely before 100 trials and all end between 0.31 and 0.33. The dashed line is the value Session 10's rules give, 0.314.*

:::script
ask | Ask | "What happened to the line as the trials went from 20 to 5,000?"
listen | Listen for | It jumped about at first and then settled, near 0.31. Different runs disagreed early and agreed late.
intro | Recall | *The law of large numbers (2.3.A.7)*: for independent trials, the relative frequency gets closer and closer to a single value.
ask | Ask | "So was the hand estimate of 0.40 wrong?"
listen | Listen for | Not wrong: an estimate from 20 trials, with a lot of chance variation. The long run shows the probability is nearer 0.31. Twenty trials is too few to rely on.
ask | Ask | "The first two hand sessions both overflowed. After two trials, was the next one less likely to overflow, to even things out?"
listen | Listen for | No. Each session is independent; its chance is the same whatever came before. The relative frequency settles because later trials swamp the early ones, not because they compensate.
:::

### Booking 10, 11 or 12: what the simulation tells the manager

Where long runs of the tool settle, to two decimal places (200,000 simulated sessions for each policy in its unit tests):

| Patients booked into 10 slots | More turn up than slots | Exactly 10 turn up | At least one slot unused |
|---|---|---|---|
| 10 | 0.00 | 0.35 | 0.65 |
| 11 | 0.31 | 0.38 | 0.30 |
| 12 | 0.66 | 0.23 | 0.11 |

:::script
ask | Ask | "What does booking an eleventh patient buy, and what does it cost?"
listen | Listen for | Sessions with an unused slot fall from about 65% to about 30%. In exchange, about 31% of sessions have one patient too many.
ask | Ask | "Which should St Mary's choose?"
listen | Listen for | The simulation cannot choose: it depends on whether an unused slot or a patient who must wait for the afternoon is worse. What it does is tell the manager how often each will happen, which is what a decision needs.
ask | Ask | "Before the texts, the miss rate was 15.5% (Session 7). Set the tool to 0.155 with 11 booked. Is overbooking more or less risky than it was?"
listen | Listen for | Less likely to overflow before the texts: about 0.16 against 0.31. Better attendance makes overbooking riskier: the texts that cut missed appointments also make it likelier that all 11 come.
:::

### What St Mary's may conclude from the simulation

> **The model conclusion (2.3.A):** *"Assuming each booked patient misses with probability 0.10, independently of the others, a simulation of 5,000 clinic sessions booked with 11 patients estimates that about 31% of sessions will have more patients than the 10 slots, and about 30% will still have an unused slot. Twenty sessions simulated by hand gave 0.40; the estimate from 5,000 sessions is much closer to the long-run value."*

:::script
ask | Ask | "What would make that conclusion wrong, however many trials were run?"
listen | Listen for | A wrong model: a miss probability that is not 0.10 at this clinic, or patients who do not miss independently, for example many missing together on a snowy day. More trials cure chance variation; they cannot cure a wrong model.
:::

---

## 147–159 min · Solo case — the library's two branches

Unaided. The library service from Sessions 3 to 7 took a random sample of **250 members** of its Central and Westside branches and recorded how each member borrows: **print only**, **e-books only**, or **both**. Watch, say nothing, note where they hesitate.

| Branch | Print only | E-books only | Both | Total |
|---|---|---|---|---|
| Central | 90 | 15 | 45 | 150 |
| Westside | 60 | 10 | 30 | 100 |
| **Total** | **150** | **25** | **75** | **250** |

1. Find the conditional relative frequencies of borrowing format within each branch.
2. A librarian says: *"Central members are more likely to borrow print only: 90 of them do, against 60 at Westside."* Evaluate the claim.
3. Are branch and borrowing format associated in these data? Describe what a segmented bar chart of format within each branch would look like.
4. In a mosaic plot with a bar for each branch, how wide is each bar, and what does the width show?
5. Use 75 ÷ 250 to estimate the probability that a member borrows both formats. A reading group has 4 members chosen at random. Plan a simulation to estimate the probability that **none** of the 4 borrows both formats, assuming members are independent. Then carry out these 10 trials and give your estimate:

```
4725  3455  7469  5319  0807  7246  7605  7354  5256  9119
```

**6.** What would you expect to happen to your estimate if you ran 1,000 trials?

**Answers.**

1. Central: print only 90 ÷ 150 = **0.600**, e-books only 15 ÷ 150 = **0.100**, both 45 ÷ 150 = **0.300**. Westside: 60 ÷ 100 = **0.600**, 10 ÷ 100 = **0.100**, 30 ÷ 100 = **0.300**.
2. **Not supported.** Central has more print-only members because it has more members in the sample (150 against 100). The shares are equal: 60.0% of Central members and 60.0% of Westside members borrow print only.
3. **Not associated**: the conditional relative frequencies are identical in the two branches, so knowing a member's branch tells you nothing about how they borrow. The two segmented bars would be **identical**: 60% print only, 10% e-books only, 30% both.
4. Central's bar is 150 ÷ 250 = **0.600** of the width and Westside's **0.400**: the marginal relative frequencies of branch, which show that Central had more of the sampled members. The horizontal divisions would run straight across both bars.
5. Estimate: 75 ÷ 250 = **0.300**. **Model:** each member borrows both formats with probability 0.30, independently. **Assign:** digits 0, 1, 2 = borrows both; 3 to 9 = does not. **Trial:** 4 digits, one reading group. **Event:** none of the 4 digits is 0, 1 or 2. The trials with no 0, 1 or 2 are **3455**, **7469** and **7354**: 3 of 10, so the estimate is **3 ÷ 10 = 0.3**.
6. By the law of large numbers, the relative frequency would settle closer to a single value, the probability, and the estimate would be more reliable than one from 10 trials. (Session 10's rules give 0.240.)

![Segmented bar chart of borrowing format within each library branch: both branches split 60%, 10%, 30%](figures/s08-library-segmented.svg)

*Question 3's segmented bar chart. The bars are identical although Central had 150 sampled members and Westside 100: no association.*

**Watch for:** "Central, because 90 is more than 60" (Session 2's comparison trap inside a two-way table); calling the variables associated because the counts differ; "0.3 because 3 digits in 10 are 0, 1 or 2" instead of counting trials in question 5 (Scenario B's trap: the digits containing 0, 1 or 2 number 9 of the 40, which is irrelevant); and "the estimate will become exactly 0.3" in question 6: it settles on the probability, which the student does not know.

---

## 159–167 min · Teach it back

> *"Explain to me how you decide from a two-way table whether two categorical variables are associated, and what goes wrong if you divide by the wrong total. Then explain how a simulation estimates a probability, and what running more trials does."*

A good answer contains four things. **Association** is judged by comparing **conditional relative frequencies** of one variable across the levels of the other: different shares mean associated, the same shares mean not, and counts are never the evidence (2.1.A.3, 2.2.B.1). The **total underneath** is the total of the condition, the group named after *of* or *among*: of the Villages students 85.0% take the bus, of the bus users 38.4% live in the Villages, and the two are different questions (2.2.A.3). A **simulation** models each outcome by random values with matching shares, runs trials of the whole process, and estimates the probability as the number of trials in which the event happened over the number of trials (2.3.A.4–6). **More trials** make the relative frequency settle near a single value, the probability, by the **law of large numbers**; it says nothing about the next trial (2.3.A.7).

If the student gets the association half and swaps the conditions, that is the part to recheck at the start of Session 9. If they say "more trials make the results even out", go back to the hand run's first two sessions and ask again *"did the third session know about them?"* Then set the homework.

---
---

# Homework — Session 8

**40 marks · bring to Session 9, self-marked**

## How to do this homework

1. Do every part **with the answer key closed.** Where you are unsure, answer anyway and put a **?** beside it.
2. Then open the key and **mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote.
3. **Bring the marked sheet.** Your wrong answers and your question marks are what Session 9 opens with.

Everything here was taught in the session; this sheet is practice. Give every proportion to 3 decimal places and every percentage to 1, worked from the counts. Name the **condition** whenever you give a conditional relative frequency ("of the Year 7 students, …"), quote **both** numbers in any comparison, and in a simulation say what **one trial** is.

---

## Part A — Vocabulary (10 marks)

Match each term to its meaning.

| | Term | | Meaning |
|---|---|---|---|
| 1 | Two-way table | A | A cell frequency divided by the total for its own row, or for its own column |
| 2 | Joint relative frequency | B | A collection of outcomes |
| 3 | Marginal relative frequency | C | For independent trials, as the number of trials increases, the relative frequency gets closer and closer to a single value |
| 4 | Conditional relative frequency | D | A cell frequency divided by the total for the entire table |
| 5 | Segmented bar chart | E | A table summarising data for two categorical variables, also called a contingency table |
| 6 | Mosaic plot | F | The result of one trial of a random process |
| 7 | Associated | G | One bar for each group, divided into segments whose heights are the relative frequencies within that group |
| 8 | Outcome | H | A row total or a column total divided by the total for the entire table |
| 9 | Event | I | A segmented bar chart whose bar widths show the groups' shares of the whole table |
| 10 | Law of large numbers | J | The conditional relative frequencies of one variable differ across the levels of the other |

## Part B — Oakfield's lunch survey (12 marks)

Oakfield School's council asked a random sample of **200 students** from Years 7, 9 and 11 how they usually have lunch.

| Year | School lunch | Packed lunch | Off site | Total |
|---|---|---|---|---|
| Year 7 | 42 | 21 | 7 | 70 |
| Year 9 | 35 | 28 | 7 | 70 |
| Year 11 | 18 | 24 | 18 | 60 |
| **Total** | **95** | **73** | **32** | **200** |

**B1.** What proportion of the 200 students are in Year 11 and have lunch off site? Name the kind of relative frequency. (1)

**B2.** What proportion of the 200 students bring a packed lunch? (1)

**B3.** Of the Year 7 students, what proportion have school lunch? Of the students who have school lunch, what proportion are in Year 7? (2)

**B4.** Make a table of the conditional relative frequencies of lunch type **within each year group**. (3)

**B5.** A council member says: *"Year 9 students are more likely than Year 11 students to bring a packed lunch: 28 of them do, against 24."* Evaluate the claim. (2)

**B6.** Is lunch type associated with year group in these data? Justify your answer with numbers. (2)

**B7.** Describe what a segmented bar chart of lunch type within each year group would show. (1)

## Part C — The hospital network's recommendation mosaic (8 marks)

The 300 patients of the Session 1 hospital survey were also asked whether they **would recommend** their hospital to a friend. The mosaic plot shows the answers, with a bar for each hospital. Its widths are the hospitals' shares of the 300.

![Mosaic plot of hospital and whether the patient would recommend it, the 300 surveyed patients](figures/s08-hw-recommend-mosaic.svg)

*Read the answers from the plot; estimates within 0.03 of the key earn the mark.*

**C1.** Which hospital had the most surveyed patients, and how can you tell from the plot? (1)

**C2.** Estimate the proportion of Hillcrest's surveyed patients who would recommend it. (1)

**C3.** At which hospital was the proportion who would recommend it highest? (1)

**C4.** Estimate the proportion of **all 300** patients who were Riverside patients who would recommend Riverside. Show how you used the plot. (2)

**C5.** Is whether a patient would recommend their hospital associated with which hospital treated them? Justify with estimates from the plot. (2)

**C6.** A segmented bar chart of the same data would lose one piece of information that the mosaic plot shows. What is it? (1)

## Part D — The café's scratch sleeves, simulated (6 marks)

Every coffee at the café comes in a scratch sleeve, and **1 in 5 sleeves** wins a free pastry, independently of the others. A customer buys **4 coffees** this week. Estimate the probability that they win **at least one** pastry.

**D1.** Say how you will use random digits for one sleeve. (1)

**D2.** Say what one trial is and what counts as the event. (1)

**D3.** Carry out these 10 trials. For each, say whether the event happened, and give the count. (2)

```
5459  9274  0312  1120  4724  9693  1054  1203  7800  2472
```

**D4.** Give your estimate of the probability, in context. (1)

**D5.** Another student counts the winning digits among all 40, finds 11, and writes *"the probability is 11 ÷ 40 = 0.275."* What has gone wrong? (1)

## Part E — Long runs and short runs (4 marks)

**E1.** St Mary's has booked 11 patients into each of its last three 10-slot sessions, and in all three at least one patient missed. The receptionist says: *"We've been lucky three times, so the next session is bound to overflow."* Comment, using the law of large numbers. (2)

**E2.** One simulation of 20 sessions estimated the probability of an overflow as 0.40; another, of 5,000 sessions, estimated 0.316. Which estimate should St Mary's use, and why? (2)

---
---

# Answer key

*For the student to mark their own work, after attempting everything.*

### Part A answers · Vocabulary (10 marks, 1 each)

1–E · 2–D · 3–H · 4–A · 5–G · 6–I · 7–J · 8–F · 9–B · 10–C

### Part B answers · Oakfield's lunch survey (12 marks)

**B1.** (1) 18 ÷ 200 = **0.090**, a **joint** relative frequency. Both the number and the name are needed for the mark.

**B2.** (1) 73 ÷ 200 = **0.365**, a marginal relative frequency.

**B3.** (2) Of the Year 7 students: 42 ÷ 70 = **0.600** (1). Of the school-lunch students: 42 ÷ 95 = **0.442** (1).

> Same cell, two totals. If you wrote 0.600 for both, reread *Rows or columns: conditioning the other way asks a different question* in the theory. This is the error Session 10 will punish.

**B4.** (3) One mark per correct row.

| Year | School lunch | Packed lunch | Off site |
|---|---|---|---|
| Year 7 | 42 ÷ 70 = 0.600 | 21 ÷ 70 = 0.300 | 7 ÷ 70 = 0.100 |
| Year 9 | 35 ÷ 70 = 0.500 | 28 ÷ 70 = 0.400 | 7 ÷ 70 = 0.100 |
| Year 11 | 18 ÷ 60 = 0.300 | 24 ÷ 60 = 0.400 | 18 ÷ 60 = 0.300 |

**B5.** (2) **Not supported** (1). The counts differ because the year groups differ in size (70 Year 9s against 60 Year 11s); the shares are equal: 28 ÷ 70 = 40.0% and 24 ÷ 60 = 40.0% (1).

**B6.** (2) **Yes** (1): the conditional relative frequencies differ across the years. For example, school lunch falls from 60.0% of Year 7 to 50.0% of Year 9 and 30.0% of Year 11, and eating off site rises from 10.0% in Years 7 and 9 to 30.0% in Year 11 (1, for at least one comparison with both numbers).

> "Yes, because 42 Year 7s have school lunch and only 18 Year 11s" earns the first mark and not the second: the evidence must be shares.

**B7.** (1) Three bars, one per year, each 100% tall, with segments 60/30/10, 50/40/10 and 30/40/30. The school-lunch segment shrinks from Year 7 to Year 11 and the off-site segment grows in Year 11. Any description with the three bars' segment heights, or that says the bars differ, earns the mark.

### Part C answers · The hospital network's recommendation mosaic (8 marks)

The plot's data: St Mary's 63 of 84 would recommend (0.750), Riverside 64 of 71 (0.901), Northgate 39 of 52 (0.750), Parkview 27 of 45 (0.600), Eastwood 24 of 30 (0.800), Hillcrest 9 of 18 (0.500).

**C1.** (1) **St Mary's**: its bar is the widest, and the widths are the hospitals' shares of the 300 (84 ÷ 300 = 0.280).

**C2.** (1) About **0.50**: the boundary in Hillcrest's bar is halfway up.

**C3.** (1) **Riverside**, about 0.90.

**C4.** (2) The tile's area: Riverside's width, about 0.24 of the whole (71 ÷ 300 = 0.237), times the height of its recommend segment, about 0.90 (1), gives about **0.21**. Exactly: 64 ÷ 300 = 0.213 (1 for an answer from 0.19 to 0.23).

> A tile's area is a joint relative frequency: width (marginal) × height (conditional). The height alone, 0.90, is the proportion **of Riverside's patients**, not of all 300.

**C5.** (2) **Yes** (1): the proportion who would recommend differs a lot from hospital to hospital, from about 0.90 at Riverside to about 0.50 at Hillcrest (1, for two hospitals compared with estimates).

**C6.** (1) The **group sizes**: how many of the 300 patients each hospital had. In a segmented bar chart every bar is the same width and 100% tall.

> The survey is a sample, and Hillcrest's bar has only 18 patients; with so few, its 50% could be far from Hillcrest's true proportion. That is worth noticing, and it is Session 13's subject, not today's mark.

### Part D answers · The café's scratch sleeves, simulated (6 marks)

**D1.** (1) One digit per sleeve: **0 or 1 = wins** a pastry (2 digits of 10, probability 0.2); **2 to 9 = does not win**. Any two digits for a win earn the mark.

**D2.** (1) One trial is **4 digits, one customer's 4 coffees**. The event: **at least one** of the 4 digits is a 0 or 1.

**D3.** (2) The event happened in trials 3 (0312), 4 (1120), 7 (1054), 8 (1203) and 9 (7800); it did not in trials 1 (5459), 2 (9274), 5 (4724), 6 (9693) and 10 (2472). Count: **5 of 10** (2; 1 if one trial is misread).

**D4.** (1) *"The estimated probability that a customer who buys 4 coffees wins at least one pastry is 5 ÷ 10 = 0.5."* The context is needed for the mark.

**D5.** (1) They counted **sleeves** instead of **customers**: 11 ÷ 40 estimates the chance that one sleeve wins, which the model already says is 0.2. The question is about customers, so the denominator is the 10 trials.

### Part E answers · Long runs and short runs (4 marks)

**E1.** (2) The receptionist is wrong (1). Each session is independent of the others, so the chance that a session booked with 11 overflows is the same, about 0.31, whatever happened in the last three; the law of large numbers is about the relative frequency over many sessions, and it says nothing about the next one making up for earlier ones (1).

**E2.** (2) The **5,000-session estimate, 0.316** (1): by the law of large numbers, the relative frequency gets closer to the probability as the number of trials increases, and 20 trials leave much more room for chance (1).

### Marks summary

| Part | Marks |
|---|---|
| A — Vocabulary | 10 |
| B — Oakfield's lunch survey | 12 |
| C — The hospital network's recommendation mosaic | 8 |
| D — The café's scratch sleeves, simulated | 6 |
| E — Long runs and short runs | 4 |
| **Total** | **40** |

---
---

# Reference sheet — keep this

*Every term carries an example from this session. Lincoln High's travel register covers all 1,842 students; St Mary's clinic sessions have 10 slots and a miss probability of 0.10.*

### Two-way tables and their three relative frequencies, with Lincoln High (2.1.A.1, 2.2.A)

**Two-way table (contingency table)** — two categorical variables for the same individuals; each individual in exactly one cell.
*Example: home area × travel mode for the 1,842 Lincoln High students; 250 are in the Villages-and-bus cell.*

**Joint relative frequency** — a cell over the table total: a pair of levels among everyone. Listen for **and**.
*Example: Villages and bus: 250 ÷ 1,842 = 0.136.*

**Marginal relative frequency** — a row or column total over the table total: one variable on its own.
*Example: Villages 294 ÷ 1,842 = 0.160; bus 651 ÷ 1,842 = 0.353.*

**Conditional relative frequency** — a cell over its own row total or its own column total: restricted to one level. The condition follows **of**, **among** or **given**, and its total goes underneath.
*Example: of the Villages students, 250 ÷ 294 = 0.850 travel by bus; of the bus users, 250 ÷ 651 = 0.384 live in the Villages.*

> **Write them this way:** from the counts, proportions to 3 decimal places, percentages to 1, with the condition in the sentence. Conditional relative frequencies within one level add to 1; 0.999 or 1.001 is rounding.

### Graphs of two categorical variables, each with its example (2.1.A.2)

| Graph | What it shows | Lincoln High example | What it hides |
|---|---|---|---|
| **Side-by-side bar chart** | a cluster of bars per group; heights are the shares within the group | bus bars 10.0%, 45.0%, 85.0% across Town, Suburbs, Villages | group sizes; that each cluster is a whole |
| **Segmented bar chart** | one 100% bar per group; segment heights are the shares within the group | the Suburbs car segment runs from 45% to 85%: 40.0% | group sizes |
| **Mosaic plot** | a segmented bar chart with widths = marginal shares, so tile areas = joint shares | Town 45.9% wide, Villages 16.0%; the Villages bus tile is 0.136 of the area | exact values in narrow bars |

### Association and claims: the reference version (2.1.A.3, 2.1.B, 2.2.B–C)

**Associated** — the conditional relative frequencies of one variable differ across the levels of the other. The same shares mean not associated. Counts are never the evidence.
*Example: associated at Lincoln High (bus 10.0%, 45.0%, 85.0%); not associated at the library (both branches 60/10/30, though Central had 90 print-only members against Westside's 60).*

**A justified claim** — the claim, both conditional relative frequencies with the condition, what they do not establish, in context.
*Example: "Of the 846 Town students, 10.0% travel by bus; of the 294 Villages students, 85.0%. This census shows an association, not a cause."*

> **Association is not cause.** A two-way table from observational data shows an association only (Session 6).

### Simulation and long-run relative frequency, with St Mary's (2.3.A)

**Random process · outcome · event** — results determined by chance · the result of one trial · a collection of outcomes.
*Example: one clinic session of 11 booked patients · 10 turned up · "more turn up than slots", the outcome 11.*

**Simulation** — model the random process so that simulated outcomes match real ones; give each outcome values with shares equal to its probability; record the counts and the count total.
*Example: one digit per patient, 0 = misses (probability 0.10); 11 digits per session.*

**The five steps** — model · assign · define one trial and the event · run many trials, recording counts · estimate = trials with the event ÷ trials.
*Example: 8 of 20 hand sessions overflowed: estimate 0.40.*

**Probability** — the long-run relative frequency; a relative frequency from data or a simulation estimates it.
*Example: 100 of 1,000 appointments missed estimates the miss probability as 0.10.*

**Law of large numbers** — for independent trials, as the number of trials increases, the relative frequency gets closer and closer to a single value. It says nothing about the next trial.
*Example: 0.40 after 20 sessions; about 0.31 after 5,000, in every run.*

:::note red Not in the course description
**Simpson's paradox**, **marginal distribution**, **conditional distribution**, **joint distribution**, **stacked bar chart**, **table of random digits**, **law of averages** and **gambler's fallacy** appear in the prep books but nowhere in the course description. Use the course description's names: joint, marginal and conditional **relative frequencies**; **segmented** bar chart; digits from a **random number generator**; and the law of large numbers, which says the long-run relative frequency settles, not that short runs even out.
:::

---

*CED references: Topic 2.1 (2.1.A.1–3, 2.1.B.1), Topic 2.2 (2.2.A.1–3, 2.2.B.1, 2.2.C.1), Topic 2.3 (2.3.A.1–7); Topic 2.7 for the formal definition of independent events; Topics 3.14–3.15 for the chi-square test that Session 17 applies to two-way tables; the Unit 2 guide's note that probability formulas can be presented intuitively with two-way tables; the Sample Instructional Activity for topics 2.1–2.2 (Quiz-Quiz-Trade). Course and Exam Description effective Fall 2026.*

*Supporting reading: Barron's pdf 152–160, 272–273 · Princeton Review 167–170 · 5 Steps to a 5 154–156.*

*Next session: Topics 2.4–2.5 — sample spaces, probability rules and complements, and mutually exclusive events.*
