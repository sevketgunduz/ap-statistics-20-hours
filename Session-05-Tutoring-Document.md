# Session 5 — The Regression Line: Prediction, Residuals and Least Squares

**AP Statistics · Twenty-Hour Course · One-to-one tutoring edition**
**CED Topics 5.3, 5.4, 5.5 · Skills 3.B, 4.A, 4.D · about 142 minutes, plus the 40-minute Session 3 test**

---

## Where this session sits

Session 4 described a relationship between two quantitative variables: its direction, unusual features, form and strength, and the one-number summary *r*. It promised that the line the scatterplots kept hinting at would come next. This session draws that line, uses it to predict, and then asks the question that decides whether the line deserves to be used at all: how far is each individual from it, and do those distances show a pattern?

These are topics 5.3 to 5.5 of the course description's Unit 5, *Regression Analysis*, and they finish Block B. Everything is still **descriptive**: a line fitted to the data in hand, with no inference about a population slope.

Three things carry over. The 25 Lincoln High students come back with their distances and journey times, and the student at 2.5 km who took 33 minutes, the point that "did not fit the pattern" in Session 4, now gets a number that says by how much. The café's iced drinks, a strong curve with *r* = 0.96, return to show what a residual plot catches that *r* cannot. And Session 3's means and standard deviations, with *n* − 1, reappear inside the formula that links the slope to *r*.

### Learning objectives

Verbatim from the course description.

| Code | Objective | Skill |
|---|---|---|
| 5.3.A | Calculate a predicted response value using a linear regression model. | 3.B |
| 5.4.A | Calculate the differences between the observed and predicted values. | 3.B |
| 5.4.B | Interpret the differences between the observed and predicted values. | 4.D |
| 5.4.C | Describe the form of association of bivariate data using residual plots. | 4.A |
| 5.5.A | Calculate the coefficients for the least-squares regression line model. | 3.B |
| 5.5.B | Interpret coefficients for the least-squares regression line model. | 4.D |

Skills: **3.B** Calculate summary statistics, relative positions of points within a distribution, and predicted responses · **4.A** Describe and compare tabular and graphical representations of data, as well as summary statistics · **4.D** Interpret statistical calculations and results to assess meaning or a claim.

### What the course description does and does not ask for

Read this before teaching; the prep books teach more regression than the 2026 framework asks for, and teach some of it in different words.

- **The coefficients come from technology.** The essential knowledge says the least-squares line, its slope *b*, its intercept *a* and *r* are all "calculated using technology" (5.5.A.1–4). The exam formula sheet nevertheless prints ŷ = *a* + *bx*, ȳ = *a* + *b*x̄ and *b* = *r*(*s_y* ÷ *sₓ*). This course therefore teaches **both routes and says which is which**: the calculator is the course description's route and the one to use whenever raw data are given; the formula-sheet route, *b* from *r* and the two standard deviations and then *a* from the point of means, is for questions that give only summary statistics. That the line passes through (x̄, ȳ) is essential knowledge in its own right (5.5.A.1).
- **Reading software output is not a learning objective.** The unit overview says students "will also benefit from having opportunities to practice translating output from technology (i.e., 'calculator speak') into appropriate statistical language". That is advice on teaching, not required content, and no essential-knowledge statement mentions a computer output table. The course description's own sample question gives the model as an equation with *r* and *r*². So this session teaches the translation the overview describes, **from the TI-84's LinReg screen to an equation and sentences in context**. The full computer regression table the prep books drill is shown once, in a red extension block in Scenario A, because everything in it except the two coefficients and R-sq belongs to inference for slope or is absent from the course description.
- **Interpolation is a named term** (5.3.A.4), alongside extrapolation (5.3.A.3). A prediction from an *x*-value inside the interval of *x*-values used to fit the line is interpolation, however thin the data are there.
- **A residual plot has exactly two readings in the course description**: apparent randomness confirms a linear form and says the linear model is appropriate (5.4.C.3); curvature suggests the linear model is not the most appropriate (5.4.C.4). Residuals may be plotted against the predicted values or against *x* (5.4.C.1).
- **The wording of *r*² is fixed**: "the proportion of variation in the response variable that is explained by the linear relationship with the explanatory variable" (5.5.A.5). The course description's sample question 23 builds its distractors out of the ways this sentence goes wrong.
- **5.5.B.1 reads oddly.** Its text is: "The coefficients of the least-squares regression line model (line of best fit) are the slope, b, and the y-intercept, a, because they are based on a sample of values." This course teaches what it can safely be taken to mean: *a* and *b* are the line's coefficients, and they are calculated from the sample in hand, so they are statistics in Session 1's sense.

:::note red Off-syllabus, not taught as examinable
The course description never mentions: the **standard deviation of the residuals** (*s*, printed as "S =" in computer output), the fact that **residuals sum to zero**, **influential points**, **high-leverage points** or **outliers in regression** as special categories, **"fanning"** in a residual plot, **transformations to achieve linearity**, **regression to the mean**, or **inference for the slope** (SE Coef, *t*, P-value). Barron's teaches all of them in its regression chapter (pdf 174–192). Influential points, leverage, transformations and inference for slope are on the removed-topics register. The exam formula sheet prints the slope's sampling distribution, and with it a formula for *s*; treat both as off-syllabus, as the course guide already records. If the student asks, the in-syllabus language is *a point that does not fit the pattern* and *a large residual*.
:::

### Timing

**The Session 3 test comes first.** Following the pattern of the earlier sessions (Session 1's test opened Session 3, Session 2's opened Session 4), give Session 3's 40-minute multiple-choice test at the start of this session, before the homework debrief. The clock below starts when the test is finished.

| Minutes | Segment | Who talks |
|---|---|---|
| 0–10 | Homework debrief and diagnostic | Student |
| 10–35 | **Theory**: the linear regression model and ŷ, interpolation and extrapolation, residuals and their sign, residual plots and their two readings, the least-squares criterion and the point of means, *a*, *b* and *r* by technology and from the formula sheet, *r*², interpreting the slope and the intercept; six check questions (5.3.A–5.5.B) | Both |
| 35–80 | **Scenario A**: Lincoln High distance and journey time, applying the theory: calculator output to equation, two checks on the line, slope and intercept in context, a prediction inside the data and one far outside it, the 33-minute student's residual, *r*², the residual plot, and the Least-squares Fitter | Both |
| 80–97 | **Activity**: Reversing Interpretations, from a residual back to the student, then judging four written interpretations | Student |
| 97–122 | **Scenario B**: the café's iced drinks: a high *r*² and a curved residual plot | Both |
| 122–134 | Solo case: St Mary's, patients arriving and mean wait | Student |
| 134–142 | Teach it back, set homework | Student |
| **Total** | **142 minutes of teaching, after the 40-minute Session 3 test** | |

The course description allots six class periods to topics 5.3–5.5, two each. Every objective is taught in the session, stated first in the theory section and then applied twice; the homework practises it. The session runs longer than the plan's 60 minutes because six objectives, two scenarios and the activity need that long, and nothing has been moved out to make it shorter.

---

## 0–10 min · Homework debrief and diagnostic

The student arrives with the Session 4 homework self-marked. Ask for the two lists: *"Which did you get wrong, and which did you put a question mark on?"* Spend the time on those only.

**The two errors to check for specifically:**

- **F2 agreed with the manager.** "*r* = 0.88 is close to 1, so the water heats at a steady rate and a line describes it well." The plot shows the water heating fast and then levelling off. A student who agreed has read *r* instead of the picture. Two minutes here, because it is today's Scenario B in miniature and today's homework D uses the same coffee machine: this session gives the student a second tool, the residual plot, that shows the curve even more plainly than the scatterplot.
- **B4(b) said the 38-minute Oakfield journey was unusual "because it is the longest time".** That is Session 3's one-variable reasoning. In a scatterplot the point is unusual because it sits far from the pattern *for a student living 6.8 km away*. Fix it now: today that distance from the pattern gets a name and a number, the **residual**, and in today's homework the 38-minute student has a residual of 11.3 minutes, the largest of the twelve.

Then the diagnostic. Four quick questions, answers out loud.

**Q1.** *"A line has the equation y = 5 + 3x. What is y when x = 4? And what does the 3 tell you?"*

**Q2.** *"A weather app forecast 20 °C for midday, and it was actually 23 °C. Was the forecast too high or too low, and by how much?"*

**Q3.** *"Lincoln High's distances and journey times have r = 0.95. Does that show that a straight line is the right model?"*

**Q4.** *"In Session 4, why was the student with the 68-minute journey not unusual in the scatterplot?"*

| What you hear | What it means | Where to start |
|---|---|---|
| Q1: "17; y goes up 3 for each 1 in x" | School algebra is secure | Move on; the theory's *The linear regression model and the predicted value ŷ (5.3.A.1–2)* builds on it |
| Q1: "17", but no meaning for the 3 | Can substitute, has no picture of slope | Spend an extra minute on *Interpreting the slope (5.5.B.1–2)* |
| Q2: "too low, by 3 degrees" | Has the idea of a residual, and its sign | Name it in the theory's *Residuals: observed minus predicted (5.4.A.1)*; the sign rule in *What the sign of a residual says (5.4.B.1)* will feel obvious |
| Q2: "too high" or "−3" | Subtracts in the wrong order | Expected, and the single most common regression error. Slow down on the two sign subsections, and make the student say *observed minus predicted* aloud every time today |
| Q3: "no, you have to look at the plot" | Session 4's 5.2.A.3 has held | Move on; the theory's residual-plot subsections give the tool |
| Q3: "yes, it's close to 1" | Trusts *r* for form | The heart of Scenario B. Do not argue now; let the café's residual plot do it |
| Q4: "it fits the pattern: that student lives furthest away" | Session 4 has held | Move on; today it gets a residual of only 2.7 minutes |
| Q4: "it was an outlier" | Still judging a point against one variable | Re-show Session 4's Lincoln scatterplot for one minute before the theory |

---

## 10–35 min · Theory — the least-squares regression line and its residuals

Every concept the session uses is stated here, before any data. Put each subsection on the shared screen, read the rule with the student, and make sure they can say in their own words what it does **not** say; that is where the marks go. The illustrations are bare, made-up numbers, and most reuse Session 4's tiny data sets so the arithmetic is quick. Lincoln High, the café and St Mary's come afterwards and apply these rules; when a question there needs a definition, point back to the subsection here rather than restating it. The section ends with six check questions.

### The linear regression model and the predicted value ŷ (5.3.A.1–2)

If the form of the relationship between *x* and *y* **appears linear**, the relationship can be approximated by a **linear regression model**: a linear equation that uses the explanatory variable, *x*, to predict the response variable, *y*. The model gives a **predicted response value**, written **ŷ** ("y-hat").

:::formula
ŷ = a + bx
:::

Here *x* is a value of the explanatory variable; ŷ is the predicted value of the response for that *x*; *b* is the **slope** of the regression line; and *a* is its **y-intercept**. The equation is printed in this form on the exam formula sheet.

What it does not say. ŷ is a **prediction**, not the observed value: an individual with that *x* can have a *y* well above or below ŷ. Write ŷ, not *y*, on the left of the equation; the hat is the whole difference between a model and a claim about every individual. And the condition comes first: the model is for relationships whose form appears linear, which is why Session 4's description of form comes before any line is fitted.

*Illustration:* for the model ŷ = 1 + 0.5*x*, an individual with *x* = 4 has predicted response ŷ = 1 + 0.5 × 4 = **3**.

### Interpolation and extrapolation (5.3.A.3–4)

**Interpolation** is predicting a response value using a value of the explanatory variable that is **within** the interval of *x*-values used to determine the regression line. **Extrapolation** is predicting a response value using a value of the explanatory variable that is **beyond** that interval. **The predicted value is less reliable the further the estimate is extrapolated.**

What it does not say. The line is evidence only about the range of *x* it was fitted on; beyond it, nobody knows whether the pattern continues, bends or stops. Extrapolation is not forbidden, and the arithmetic is the same, but the answer must say that it is an extrapolation and so less reliable. The test is the interval of *x*-values, not whether some individual had exactly that *x*: a prediction at an *x* inside the interval where no individual happens to sit is still interpolation.

*Illustration:* a line fitted to *x*-values from 2 to 10. Predicting at *x* = 6 is interpolation; at *x* = 15 it is extrapolation; at *x* = 40 it is a much less reliable extrapolation than at 15.

### Residuals: observed minus predicted (5.4.A.1)

A **residual** is the difference between the **observed** response value and the **predicted** response value, for the given value of the explanatory variable.

:::formula
residual = y − ŷ = observed y − predicted y
:::

Here *y* is the individual's actual response and ŷ = *a* + *bx* is the model's prediction at that individual's *x*. On a scatterplot the residual is the **vertical** distance from the point to the line, measured in the units of *y*.

What it does not say. The order matters: observed minus predicted, never the other way round, and the course description writes it both ways (*y* − ŷ and "observed *y* − predicted *y*") so there is no excuse. A residual is measured in the units of the **response**; it is never a horizontal distance and never says anything about *x*. And it compares the individual with the **prediction for its own *x***, not with the mean of *y*.

*Illustration:* for ŷ = 1 + 0.5*x*, the point (2, 3) has ŷ = 2, so its residual is 3 − 2 = **+1**. The point (1, 1) has ŷ = 1.5, so its residual is 1 − 1.5 = **−0.5**.

### What the sign of a residual says (5.4.B.1)

If the residual is **positive**, the model **underpredicts** (underestimates) the value of the response variable. If the residual is **negative**, the model **overpredicts** (overestimates) it.

| Residual | Point is | The model |
|---|---|---|
| positive, *y* > ŷ | above the line | **underpredicts**: the actual value is higher than predicted |
| negative, *y* < ŷ | below the line | **overpredicts**: the actual value is lower than predicted |
| zero, *y* = ŷ | on the line | predicts exactly |

What it does not say. The sign is about the **model's** error, seen from the individual: a positive residual means the prediction was too low, which students routinely say backwards. An interpretation needs three things: the size, in the response's units; the direction, *more* or *less than predicted*; and the individual's *x*, because the prediction belongs to that *x*.

*Illustration:* the point (2, 3) with residual +1: its response is 1 unit **more than predicted** for *x* = 2, so the model underpredicts it by 1.

### Residual plots (5.4.C.1–2)

A **residual plot** is a scatterplot of the **residuals** against the **predicted response values**, or against the **explanatory variable values**. Residual plots are used to investigate whether the linear regression model is appropriate for the observed data.

What it does not say. The two choices of horizontal axis give the same picture for a line with positive slope and a mirror image for negative slope; either is correct. A residual plot always has a horizontal line at residual = 0, and a point's height above or below it is its residual. The plot is a tool for judging the **model**; it does not replace the scatterplot, which is still where the description of the association comes from.

*Illustration:* for ŷ = 1 + 0.5*x* and the points (1, 1), (2, 3), (3, 2), the residuals are −0.5, +1, −0.5, so the residual plot has points at (1, −0.5), (2, 1) and (3, −0.5).

### Reading a residual plot: randomness or curvature (5.4.C.3–4)

The linear regression model should only be fitted if the data show a linear trend. **Apparent randomness** in a residual plot is confirmation of a **linear form** and indicates that the linear model is **appropriate**. **Curvature** in a residual plot suggests that the linear model is **not the most appropriate** model for the data.

![Two made-up data sets, each with its least-squares line and residual plot](figures/s05-theory-residual-plots.svg)

*A: points scattered about a straight trend. Their residuals jump above and below 0 with no pattern: the linear model is appropriate. B: the five points (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), on the curve y = x², with r = 0.98. The least-squares line is ŷ = −7 + 6x, and the residuals are +2, −1, −2, −1, +2: positive at both ends, negative in the middle. That curve says the linear model is not the most appropriate, although r is very close to 1.*

What it does not say. The residual plot answers a question *r* cannot: Session 4 showed that *r* close to 1 does not prove linear form (5.2.A.3), and the residual plot is how to check. "Apparent randomness" means no systematic shape, not that the residuals are small; a weak linear association has large, patternless residuals, and the linear model is still the appropriate one. Curvature says a straight line is not the *most* appropriate model; it does not say the variables are unrelated.

### Least squares: the line that minimises Σ(residual²) (5.5.A.1)

The simple linear regression model is fitted to the data by **minimising the sum of the squares of the residuals**. The line that does this is called the **least-squares regression line** (LSRL), and it is calculated using technology. The least-squares regression line **passes through the point (x̄, ȳ)**, the point of means.

:::formula
least-squares line: the one line ŷ = a + bx that makes Σ(y − ŷ)² as small as possible
:::

Here the sum Σ runs over all *n* individuals, and each term is one residual squared. The exam formula sheet states the point-of-means fact as ȳ = *a* + *b*x̄.

What it does not say. "Best" means best by this one criterion, the smallest sum of squared residuals; it does not mean the line fits well, or that a line is the right model at all. Squaring stops positive and negative residuals from cancelling, and it makes big residuals count for much more than small ones, so a single point far from the pattern can add a large share of the total.

*Illustration:* for (1, 1), (2, 3), (3, 2), the least-squares line is ŷ = 1 + 0.5*x*, with residuals −0.5, +1, −0.5 and Σ(residual²) = 0.25 + 1 + 0.25 = **1.5**. The line *y* = *x* gives residuals 0, 1, −1 and a sum of **2**; the flat line *y* = 2 gives −1, 1, 0 and also **2**. And the least-squares line passes through (x̄, ȳ) = (2, 2): 1 + 0.5 × 2 = 2.

### Finding a and b: technology, or the formula sheet (5.5.A.2–4)

The slope *b*, the *y*-intercept *a* and the correlation *r* are **calculated using technology** (5.5.A.2–4). On a TI-84, put *x* in L1 and *y* in L2 and run STAT → CALC → LinReg(a+bx), with Stat Diagnostics on so that *r* and *r*² appear.

When only summary statistics are given, the exam formula sheet supplies a second route:

:::formula
b = r × (s_y ÷ sₓ)        then        a = ȳ − b x̄   (from ȳ = a + b x̄)
:::

Here *r* is the correlation; *sₓ* and *s_y* are the sample standard deviations of *x* and *y*, with divisor *n* − 1 as in Session 3; and x̄ and ȳ are the two means.

**The course's rounding convention.** Write *a* and *b* to **4 significant figures, keeping at least 2 decimal places** (8.762, 2.019, −133.03, 0.4183); write an exact value as it is (−3.75). Work predictions and residuals **from the equation as written**, and give them to **1 decimal place** in the units of *y*. Give *r* and *r*² to 2 decimal places, and in the formula-sheet route carry *r* to at least 4 decimal places.

What it does not say. The formula-sheet route is a way to get the same line when the raw data are not available; it is not a second, different line. It also shows why the slope and *r* always have the **same sign**, since *sₓ* and *s_y* are positive, and why *r* is not the slope: *r* is unit-free, and *b* carries the units of *y* per unit of *x*. Rounding *r* too early is the usual error in this route: it shifts *b* in the second decimal place.

*Illustration:* the three points again: *r* = 0.5, *sₓ* = 1, *s_y* = 1, x̄ = 2, ȳ = 2. So *b* = 0.5 × (1 ÷ 1) = **0.5** and *a* = 2 − 0.5 × 2 = **1**: the same line, ŷ = 1 + 0.5*x*.

### The coefficient of determination r² (5.5.A.5)

In simple linear regression, the square of the correlation coefficient, ***r*²**, is called the **coefficient of determination**. The value of *r*² is **the proportion of variation in the response variable that is explained by the linear relationship with the explanatory variable**.

:::formula
r² = (r)², a proportion between 0 and 1, usually quoted as a percentage
:::

What it does not say. It is a proportion of **variation in the response**, not a proportion of individuals, and not a percentage of "correct" predictions. "Explained by the linear relationship" is a statistical phrase, not a claim that *x* causes *y*: Session 4's rule that correlation does not imply causation still holds. It says nothing about whether a line is the right model: a curve can have a high *r*², and only the residual plot shows it. And *r*² has lost the sign of *r*, so it cannot give the direction.

*Illustration:* for the three points, *r* = 0.5, so *r*² = **0.25**: 25% of the variation in *y* is explained by the linear relationship with *x*. For the five points on *y* = *x*², *r*² = 0.96, and their residual plot still curves.

### Interpreting the slope (5.5.B.1–2)

The **coefficients** of the least-squares regression line are its slope, *b*, and its *y*-intercept, *a*. They are calculated from a sample of values, so they are statistics in Session 1's sense (5.5.B.1). The **slope** is interpreted as the **predicted increase or decrease in the response variable for a one-unit increase in the explanatory variable**, in context.

The model sentence has four parts: *For each additional* [one unit of *x*, in context], *the* **predicted** [response, in context] *increases* (or *decreases*) *by* [|*b*| and the units of *y*].

What it does not say. The word **predicted** (or "on average") is not decoration: without it, the sentence claims every individual changes by exactly *b*, which the residuals flatly contradict. The slope describes the fitted line, so it is only as trustworthy as the line; for a curved pattern, one slope misdescribes the rate of change everywhere. And it is a comparison between individuals whose *x* differs by one unit, not a statement that changing one individual's *x* would change its *y*; that would be a causal claim.

*Illustration:* for ŷ = 1 + 0.5*x*: for each one-unit increase in *x*, the predicted *y* increases by **0.5**.

### Interpreting the y-intercept, and when it means nothing (5.5.B.3)

The **y-intercept** is the **predicted value of the response variable when the explanatory variable is 0**, interpreted in context. Sometimes it has **no reasonable interpretation**, because *x* = 0 is **beyond the interval of *x*-values** used to fit the line, so interpreting it would be extrapolation. At other times it has **no logical interpretation** because it is a **negative value for a response that cannot be negative**, such as a height.

What it does not say. The intercept is always part of the equation and always needed for predictions; the question is only whether **it means anything on its own**. Checking takes one sentence each way: is 0 inside the interval of *x*-values, and is the predicted value possible? A correct answer can be "the predicted *y* when *x* = 0 is *a*, but no individual had an *x* near 0, so this is an extrapolation and has no reliable meaning here."

*Illustration:* for ŷ = 1 + 0.5*x* fitted to *x* from 1 to 3, the intercept says the predicted *y* at *x* = 0 is 1, but *x* = 0 is outside 1 to 3, so it is an extrapolation. A line ŷ = −20 + 4*x* for a response that cannot be negative predicts −20 at *x* = 0: impossible, so no logical interpretation.

### Six check questions before the data

:::script
ask | Ask | "A model is ŷ = 4 + 2x. An individual has x = 3 and y = 13. What is the residual, and did the model overpredict or underpredict?"
listen | Listen for | ŷ = 10; residual = 13 − 10 = +3; positive, so the model underpredicts by 3.
ask | Ask | "The line was fitted to x from 5 to 20. Is a prediction at x = 12 interpolation or extrapolation? At x = 30?"
listen | Listen for | 12 is interpolation, inside 5 to 20. 30 is extrapolation, and less reliable.
ask | Ask | "A residual plot shows the residuals high at both ends and low in the middle. What does that tell you?"
listen | Listen for | Curvature: the linear model is not the most appropriate model.
ask | Ask | "What is 'least' about the least-squares line, and which point must it pass through?"
listen | Listen for | The sum of the squared residuals is as small as possible; it passes through (x̄, ȳ).
ask | Ask | "r = −0.8, sₓ = 2 and s_y = 10. What is the slope? And what is r²?"
listen | Listen for | b = −0.8 × 10 ÷ 2 = −4. r² = 0.64, so 64% of the variation in y is explained by the linear relationship with x.
ask | Ask | "r² = 0.95. Is a straight line the right model?"
listen | Listen for | Not from that alone. Look at the residual plot.
ifsay | If any answer goes wrong | Go back to that subsection and reread its "what it does not say" paragraph together before starting Scenario A. The scenarios lean on every one of these.
:::

---

## 35–80 min · Scenario A — Lincoln High: a line for journey time

The same 25 randomly chosen Lincoln High students as in Sessions 2 to 4, with their distance from school and journey time. In Session 4 the student described the scatterplot as a **strong, positive, linear** association with *r* = 0.95, and found one student who does not fit the pattern: 2.5 km away, 33 minutes. Remind them of that description; the line only makes sense because the form is linear.

```
 km   min    km   min    km   min    km   min    km   min
 0.5    8    1.0    9    1.0   10    1.5   11    2.0   12
 1.5   12    2.5   13    3.0   14    4.5   15    3.5   15
 4.0   16    4.5   17    7.0   18    5.5   18    6.0   20
 6.5   21    5.0   22    7.5   24    8.0   25    9.5   27
11.0   30    2.5   33   14.0   36   17.0   42   28.0   68
```

**The trap this scenario carries: a prediction far beyond the data is still only arithmetic, and the arithmetic looks as trustworthy as any other.** The student will compute a prediction for a new student who lives 45 km away without a pause, because nothing in the equation stops them. The distances in the data run from 0.5 to 28 km; the line knows nothing beyond 28. The same trap hides in the intercept, which is a prediction at 0 km, just outside the data.

### From calculator output to an equation in context (5.5.A)

Have the student enter the distances in L1 and the times in L2 and run LinReg(a+bx). The TI-84 shows:

```
LinReg
 y=a+bx
 a=8.762237762
 b=2.018751949
 r²=.8930436544
 r=.94500987
```

:::script
ask | Ask | "Turn that screen into the equation of the line, the way you would write it on the exam."
listen | Listen for | ŷ = 8.762 + 2.019x, where ŷ is the predicted journey time in minutes and x is the distance from school in kilometres. Or, in words: predicted journey time = 8.762 + 2.019 × (distance from school).
intro | Recall | *The linear regression model and the predicted value ŷ (5.3.A.1–2)*: ŷ = a + bx, with a the intercept and b the slope. The course's rounding convention, from *Finding a and b (5.5.A.2–4)*: 4 significant figures, so a = 8.762 and b = 2.019.
ifsay | If "y = 8.762 + 2.019x" | "Is that the journey time of every student who lives x km away?" No, it is the predicted time. The hat is the difference, and on the exam an equation with y instead of ŷ, or with x and y undefined, loses the mark.
ifsay | If they copy "y = a + bx" from the screen | That is calculator speak. The answer is the equation with the numbers in and the variables named: the translation the course description asks students to practise.
:::

:::note red Beyond the course description: a full computer output table
Prep books and older exams print regression output from statistical software like this, for the same 25 students:

| Predictor | Coef | SE Coef | T | P |
|---|---|---|---|---|
| Constant | 8.762 | 1.265 | 6.93 | 0.000 |
| Distance | 2.019 | 0.146 | 13.86 | 0.000 |

S = 4.366 · R-sq = 89.3% · R-sq(adj) = 88.8%

Only three numbers here are in the course description: the **Constant's Coef is *a***, the **Distance Coef is *b***, and **R-sq is *r*²**. SE Coef, T and P belong to inference for the slope, which is on the removed-topics register; S, the standard deviation of the residuals, and R-sq(adj) do not appear in the course description at all. If the student meets a table like this, read off *a*, *b* and *r*², and ignore the rest.
:::

### Checking the line: the point of means and the formula sheet

Two checks, each applying a theory subsection. They take two minutes and they are the fastest way to catch a mistyped list.

:::script
ask | Ask | "From the theory, which point must this line pass through? Use 1-Var Stats on L1 and L2 and check."
listen | Listen for | (x̄, ȳ) = (6.28, 21.44). And 8.762 + 2.019 × 6.28 = 21.44.
intro | Recall | *Least squares: the line that minimises Σ(residual²) (5.5.A.1)*: the least-squares line passes through the point of means; the formula sheet writes it as ȳ = a + b x̄.
ask | Ask | "1-Var Stats also gives sₓ = 6.117 and s_y = 13.07. Use the formula sheet to get the slope from r, and then the intercept."
listen | Listen for | b = 0.9450 × 13.07 ÷ 6.117 = 2.019. a = 21.44 − 2.019 × 6.28 = 8.76.
intro | Recall | *Finding a and b: technology, or the formula sheet (5.5.A.2–4)*: b = r(s_y ÷ sₓ), then a from ȳ = a + b x̄. Same line, second route.
ifsay | If they use r = 0.95 and get b = 2.03 | "Which number did you round?" Carry r to at least 4 decimal places in this route; rounding it to 2 moves b in the second decimal place.
:::

The intercept from the formula-sheet route comes out at 8.761 to three decimal places, not 8.762, only because *b* was rounded to 2.019 before it was used; the calculator's 8.762 is the one to write.

### What the slope and intercept say about the journeys (5.5.B)

:::script
ask | Ask | "Interpret the slope, 2.019, in context."
listen | Listen for | "For each additional kilometre a student lives from school, the predicted journey time increases by about 2.02 minutes."
intro | Recall | *Interpreting the slope (5.5.B.1–2)*: the predicted increase or decrease in the response for a one-unit increase in the explanatory variable, in context. Four parts: each additional unit of x, the word *predicted*, the direction, the amount with units.
ifsay | If "each extra kilometre adds 2.02 minutes to the journey" | "To every student's journey?" Point at the 7 km student who took 18 minutes and the 5 km student who took 22: further away, shorter journey. The slope is a statement about predictions, and the sentence needs *predicted* or *on average*. This is the error AP readers penalise most often on slope questions.
ask | Ask | "Now the intercept, 8.762. What does it say, and does it make sense here?"
listen | Listen for | "A student who lives 0 km from school has a predicted journey time of 8.762 minutes." Then the judgement: no student in the data lives closer than 0.5 km, so x = 0 is outside the interval of x-values, and this is an extrapolation.
intro | Recall | *Interpreting the y-intercept, and when it means nothing (5.5.B.3)*: the predicted response when x = 0, which has no reasonable interpretation when x = 0 is beyond the interval of x-values used to fit the line.
:::

The intercept here is a small extrapolation, 0.5 km beyond the data, and 8.8 minutes is not absurd for a student who lives next to the school. The honest answer says both: this is what the model predicts at 0 km, and it is an extrapolation, so it is not a reliable figure. What it must not say is that "it takes 8.762 minutes to get to school before you have travelled anywhere", as if the intercept were a measured fact.

### Predicting a journey: 12 km, and a student 45 km away (5.3.A)

:::script
ask | Ask | "Predict the journey time of a student who lives 12 km from school."
listen | Listen for | ŷ = 8.762 + 2.019 × 12 = 33.0 minutes.
ask | Ask | "Interpolation or extrapolation?"
listen | Listen for | Interpolation: 12 km is inside the interval of distances used to fit the line, 0.5 to 28 km.
intro | Recall | *Interpolation and extrapolation (5.3.A.3–4)*: within the interval of x-values is interpolation.
:::

Now spring the trap.

:::script
ask | Ask | "A new student is joining next term. She lives in a village 45 km away. What journey time does the line predict for her?"
listen | Listen for | ŷ = 8.762 + 2.019 × 45 = 99.6 minutes. Most students give the number and stop.
ifsay | If they stop at 99.6 | "How far away does the furthest student in the data live?" 28 km. "So what does the line know about 45 km?" Nothing: 45 is beyond the interval of x-values, so this is extrapolation, and the predicted value is less reliable the further the estimate is extrapolated. 45 km is 17 km past the furthest student.
ask | Ask | "Why might the pattern not carry on out to 45 km?"
listen | Listen for | Any sensible reason: a student that far away probably travels by train or a direct bus, which covers the extra kilometres faster than the pattern for students who walk, cycle or take a local bus; or the route might include a long wait for a connection. The data cannot say which, and that is the point.
:::

![The Lincoln High line over the data, extended to 45 km](figures/s05-lincoln-extrapolate.svg)

*The shaded band is the interval of distances used to fit the line, 0.5 to 28 km. The prediction at 12 km, 33.0 minutes, is inside it: interpolation. The dashed extension to 45 km, predicting 99.6 minutes, is extrapolation: the line has no data out there, and nothing guarantees the pattern continues.*

> **The sentence to write down:** *A prediction is only as good as the data behind it. Inside the interval of x-values it is interpolation; beyond it, extrapolation, and less reliable the further it goes. Say which it is, every time.*

### The 33-minute student's residual (5.4.A–B)

:::script
ask | Ask | "The student at 2.5 km who took 33 minutes: what does the line predict for her, and what is her residual?"
listen | Listen for | ŷ = 8.762 + 2.019 × 2.5 = 13.8 minutes. Residual = 33 − 13.8 = +19.2 minutes.
intro | Recall | *Residuals: observed minus predicted (5.4.A.1)*: residual = y − ŷ.
ask | Ask | "Put the +19.2 into a sentence about her."
listen | Listen for | "Her journey took 19.2 minutes longer than the line predicts for a student who lives 2.5 km from school. The model underpredicts her journey time."
intro | Recall | *What the sign of a residual says (5.4.B.1)*: positive means the model underpredicts.
ifsay | If "−19.2" | "Which did you subtract from which?" Observed minus predicted: 33 − 13.8. The sign is the whole meaning of a residual, so the order is not negotiable.
ifsay | If "she took 19.2 minutes longer than average" | "Than which average?" The mean journey is 21.44 minutes; she took 11.6 minutes more than that. The residual compares her with the prediction **for her distance**, not with everybody.
ask | Ask | "And the 68-minute student at 28 km, Session 3's outlier?"
listen | Listen for | ŷ = 8.762 + 2.019 × 28 = 65.3; residual = 68 − 65.3 = +2.7 minutes. Small: the line predicts him well.
:::

![The Lincoln High least-squares line, with the 33-minute student's residual](figures/s05-lincoln-line.svg)

*The least-squares line ŷ = 8.762 + 2.019x through the 25 students, passing through the point of means (6.28, 21.44). The orange segment is the residual of the student at 2.5 km: 33 − 13.8 = 19.2 minutes.*

This is Session 4's trap turned into numbers. The student who is extreme in both variables has a residual of 2.7 minutes: he **fits** the pattern. The student who is ordinary in both variables has a residual of 19.2 minutes, by far the largest of the 25: she is the one who **does not fit**. A residual is exactly the measure of "how far off the pattern" that Session 4 had to judge by eye.

### How much of the variation distance explains (5.5.A.5)

:::script
ask | Ask | "The screen says r² = .8930. Interpret it in context."
listen | Listen for | "About 89% of the variation in journey time is explained by the linear relationship with distance from school."
intro | Recall | *The coefficient of determination r² (5.5.A.5)*: the proportion of variation in the response variable that is explained by the linear relationship with the explanatory variable.
ifsay | If "0.95² = 0.90, so 90%" | "Which r did you square?" The rounded one. Read r² from the screen, 0.8930, or square the unrounded r: 0.94501² = 0.8930. Squaring a rounded r moves r² by about 0.01, enough to lose the mark on a multiple-choice question whose options are one percentage point apart.
ifsay | If "89% of the students' journeys are explained by distance" | "Is it 89% of the students?" No: it is 89% of the **variation** in journey time. Every student's time is partly predictable from distance, and partly not.
ifsay | If "distance causes 89% of the journey time" | r² is a statement about a fitted line, not about causes. Session 4's rule still holds.
:::

The other 11% is the scatter around the line: the residuals. The biggest single piece of it is the 33-minute student.

### The journeys' residual plot (5.4.C)

:::script
ask | Ask | "Before we look: if a straight line is the right model for these journeys, what should the residual plot look like?"
listen | Listen for | Points scattered above and below 0 with no pattern, no curve.
intro | Recall | *Reading a residual plot: randomness or curvature (5.4.C.3–4)*: apparent randomness confirms a linear form; curvature suggests the linear model is not the most appropriate.
:::

![Residual plot for the Lincoln High line: residuals against distance](figures/s05-lincoln-residuals.svg)

*Residuals against distance from school, for the 25 students. The residuals sit in a flat band around 0 from 0.5 km to 28 km, with no curve. One residual, 19.2 minutes, is far above the rest: the student at 2.5 km.*

:::script
ask | Ask | "What does this residual plot tell you about the model?"
listen | Listen for | No curvature: apart from one student, the residuals scatter in a flat band around 0 all the way along. That apparent randomness confirms the linear form, so the linear model is appropriate. The one large residual is the 2.5 km student who does not fit the pattern.
ifsay | If "most of the residuals are negative, so it's a bad line" | "Is there a curve, or a flat band?" Many residuals are around −1 because the 19.2 lifts the line a little; the band is still flat. The course description's question is randomness versus curvature, and there is no curve.
:::

### Least-squares Fitter

:::sim least-squares-fitter | Least-squares Fitter | 1360
Open on **Lincoln High**. Turn on **squares of the residuals** and ask the student to move the two handles until Σ(residual²) is as small as they can make it, and to write the number down. Then **Show the least-squares line**: its sum is 438.3, and nobody beats it. Ask what share of that 438.3 comes from one square: the 33-minute student's residual squared is 19.2² ≈ 368. Then press **Flat line at ȳ**, the line that ignores distance, and watch the sum jump to 4098.2. Leave the **café** until Scenario B.
:::

This is the one tool of the session, and it earns its place on the standard's three tests. The least-squares line is defined by a **process**, making a sum as small as possible over every possible line; a static figure can show one line and its squares, but not that every other line does worse; and the student **drives** it, hunting for the minimum before seeing it. The tool opens on a reasonable line that is not the best, so there is something to improve straight away.

The point to draw out: the squares make the student at 2.5 km count for far more than her share. She is one student in 25, and her square is about 84% of the least-squares total. That is what squaring does, as the theory warned.

---

## 80–97 min · Activity — Reversing Interpretations

The course description's Sample Instructional Activity for topic 5.4: instead of asking students to interpret a residual, give them the residual and the equation of the least-squares line and ask what it tells us about a particular individual. Its own example: "One wolf in the pack had a length of 1.4 m and a residual of −9.87. What does that −9.87 tell us about that particular wolf?" Its sample exam question 24 is the same move as an exam item: given the model and one individual's residual, find that individual's observed value.

**The one-to-one conversion.** The course description imagines a class trading interpretations. Here you are the source of the residuals, and the student does the reversing. Round 1 goes from a residual back to the student it belongs to; Round 2 turns the student into the examiner, judging four written interpretations of the same residual.

### Round 1: from a residual back to the student

Use the Lincoln High line, ŷ = 8.762 + 2.019*x*. Read out one card at a time. For each, the student finds the predicted time, then the actual time, and says in one sentence what the residual tells you about that student.

| Card | Distance | Residual |
|---|---|---|
| A | 7.0 km | −4.9 minutes |
| B | 5.0 km | +3.1 minutes |
| C | 2.5 km | +19.2 minutes |
| D | 7.5 km | +0.1 minutes |

**Answers.**

| Card | Predicted, ŷ | Actual, ŷ + residual | What it tells you |
|---|---|---|---|
| A | 8.762 + 2.019 × 7 = 22.9 | 22.9 − 4.9 = **18.0 min** | Her journey took 4.9 minutes less than the line predicts for a student 7 km away; the model overpredicts |
| B | 18.9 | 18.9 + 3.1 = **22.0 min** | 3.1 minutes longer than predicted for 5 km; the model underpredicts |
| C | 13.8 | 13.8 + 19.2 = **33.0 min** | 19.2 minutes longer than predicted for 2.5 km, the student who does not fit |
| D | 23.9 | 23.9 + 0.1 = **24.0 min** | almost exactly what the line predicts for 7.5 km |

:::script
ask | Ask | "How do you get from a residual back to the actual journey time?"
listen | Listen for | Rearrange residual = y − ŷ: y = ŷ + residual. Predicted plus residual.
intro | Recall | *Residuals: observed minus predicted (5.4.A.1)*, run backwards.
ifsay | If card A gives 27.8 | "Did you add or subtract the −4.9?" y = ŷ + residual = 22.9 + (−4.9) = 18.0. A student who computes 22.9 + 4.9 has used predicted minus observed.
ifsay | If card D is called "a perfect student" | A residual of 0.1 says the line predicts this student almost exactly. It says nothing about whether the journey is short, long, good or bad.
:::

### Round 2: judging four written interpretations

Put these on the shared screen. Each is someone's interpretation of card A's residual: 7 km, residual −4.9 minutes. The student marks each right or wrong and, for each wrong one, names the error.

1. *"This student's journey was 4.9 minutes shorter than the average journey."*
2. *"The model underestimated this student's journey time by 4.9 minutes."*
3. *"This student lives 4.9 km closer to school than the line predicts."*
4. *"This student's journey took 4.9 minutes less than the line predicts for a student who lives 7 km from school, so the model overpredicted her journey time."*

:::script
ask | Ask | "Which of the four would get the mark? For each of the others, what went wrong?"
listen | Listen for | Only 4. (1) compares with the mean journey, 21.44 minutes, not with the prediction for her distance. (2) has the sign backwards: a negative residual means the model **over**estimated. (3) treats the residual as a distance in x; residuals are in the response's units, minutes, and say nothing about where she lives. (4) has the size, the direction relative to the prediction, and the student's x.
intro | Recall | *What the sign of a residual says (5.4.B.1)*: the three parts of an interpretation are the size in the response's units, *more* or *less than predicted*, and the individual's x.
ifsay | If (2) is accepted | "Was her real time above or below the prediction?" Below: 18.0 against 22.9. The model's guess was too high, so it overestimated. Say it the long way until it is automatic.
:::

> **The sentence to write down:** *A residual of −4.9 means the actual value was 4.9 below what the model predicts for that x: the model overpredicts. Actual = predicted + residual.*

---

## 97–122 min · Scenario B — The café's iced drinks: a high r², the wrong model

Back to the café. On the same 10 days as in Sessions 3 and 4, it recorded the midday temperature and the number of iced drinks it sold. In Session 4 the student saw the scatterplot bend upwards, with *r* = 0.96, and learned that a high *r* does not prove a linear form.

| Midday temperature (°C) | 12 | 14 | 15 | 15 | 16 | 18 | 19 | 21 | 22 | 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| Iced drinks sold | 9 | 11 | 13 | 16 | 20 | 31 | 44 | 64 | 74 | 167 |

**The trap this scenario carries: a high *r*², like a high *r*, does not show that a straight line is the right model.** The manager has now fitted a least-squares line and been told that it explains 92% of the variation. That sounds like the end of the argument. The residual plot says otherwise, and it is the tool the course description names for exactly this judgement.

### The manager's line

The manager runs LinReg(a+bx) and gets *a* = −133.03, *b* = 9.885, *r* = 0.96 and *r*² = 0.92.

> *"The line is ŷ = −133.03 + 9.885x, and r² is 0.92, so it explains 92% of the variation. That's an excellent model. I'll use it to plan how many iced drinks to prepare each morning from the forecast."*

:::script
ask | Ask | "Interpret r² = 0.92 correctly first. Is the manager's sentence right so far?"
listen | Listen for | About 92% of the variation in iced drinks sold is explained by the linear relationship with midday temperature. The sentence is right; the conclusion, "an excellent model", does not follow from it.
intro | Recall | *The coefficient of determination r² (5.5.A.5)*, including what it does not say: it says nothing about whether a line is the right model.
ask | Ask | "Session 4 already told you something about this scatterplot. What?"
listen | Listen for | It curves upwards: iced sales rise slowly at first, then fast. A correlation close to 1 does not show linear form.
:::

### Two predictions the line gets wrong

:::script
ask | Ask | "Use the line to predict iced drinks on a 12 °C day. Then find the residual for the actual 12 °C day, when the café sold 9."
listen | Listen for | ŷ = −133.03 + 9.885 × 12 = −14.4 iced drinks. Residual = 9 − (−14.4) = +23.4.
ifsay | If they write the −14.4 down without comment | "Can the café sell −14.4 drinks?" No. And 12 °C is inside the interval of temperatures used, 12 to 28 °C: this is interpolation, and the line still predicts something impossible. The problem is not extrapolation; it is the model.
ask | Ask | "Now 18 °C, when the café sold 31."
listen | Listen for | ŷ = −133.03 + 9.885 × 18 = 44.9. Residual = 31 − 44.9 = −13.9: the model overpredicts by 13.9 drinks.
ifsay | If they notice that 44.9 is the mean | Good. 18 °C is x̄, and the least-squares line always passes through (x̄, ȳ), so the prediction there is ȳ = 44.9 exactly.
:::

The same line underpredicts the coldest day by 23 drinks and overpredicts a middling day by 14. A line that is too low at one end and too high in the middle is not making random errors.

### The iced drinks' residual plot

The student has two residuals. Give the rest, rounded to the nearest drink, since only the pattern matters for the plot:

| Temperature (°C) | 12 | 14 | 15 | 15 | 16 | 18 | 19 | 21 | 22 | 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| Residual (drinks) | +23 | +6 | −2 | +1 | −5 | −14 | −11 | −11 | −10 | +23 |

:::script
ask | Ask | "Sketch the residual plot, residuals against temperature, before I show it. What shape do you get?"
listen | Listen for | Positive at the cold end, negative through the middle, positive again at 28 °C: a U-shaped curve.
intro | Recall | *Reading a residual plot: randomness or curvature (5.4.C.3–4)*: curvature in the residual plot suggests that the linear model is not the most appropriate model for the data.
:::

![Café: the least-squares line for iced drinks, and its residual plot](figures/s05-cafe-iced.svg)

*Left: the least-squares line ŷ = −133.03 + 9.885x. It predicts −14.4 iced drinks at 12 °C, below the dashed zero line. Right: the residuals, positive at both ends and negative in the middle. The curve in the residual plot is the curve in the data, made impossible to miss.*

> **The model answer to the manager:** *"The line does explain about 92% of the variation in iced drinks sold (r² = 0.92), but the residual plot shows clear curvature: the residuals are positive at both ends, around +23 drinks at 12 °C and at 28 °C, and negative in the middle, down to −14 at 18 °C. So a linear model is not the most appropriate model for these data. The line even predicts −14.4 iced drinks at 12 °C. A high r² does not show that a straight line is the right model."*

### What the café can and cannot say

:::script
ask | Ask | "The slope is 9.885. What would it say, and why is it misleading here?"
listen | Listen for | "For each 1 °C increase, the predicted number of iced drinks increases by about 9.9." But the data rise by about 2.75 drinks per degree between 12 and 16 °C and by about 15.5 per degree between 22 and 28 °C. One slope cannot describe a rate that keeps changing.
intro | Recall | *Interpreting the slope (5.5.B.1–2)*: the slope is only as trustworthy as the line.
ask | Ask | "And the intercept, −133.03?"
listen | Listen for | It is the predicted number of iced drinks at 0 °C, and it fails both of the course description's tests: 0 °C is outside 12 to 28 °C, so it is an extrapolation, and a negative number of drinks is impossible.
intro | Recall | *Interpreting the y-intercept, and when it means nothing (5.5.B.3)*: both kinds of meaninglessness at once.
:::

| Statement | Supported? |
|---|---|
| "Iced drink sales and midday temperature have a strong, positive association." | **Yes**: the scatterplot and *r* = 0.96 |
| "About 92% of the variation in iced drinks sold is explained by the linear relationship with temperature." | **Yes**: that is what *r*² = 0.92 means |
| "So the straight line is a good model for planning." | **No**: the residual plot curves, so a linear model is not the most appropriate |
| "Each extra degree brings about 9.9 more iced drinks." | **No**: sales rise by about 2.75 per degree from 12 to 16 °C and about 15.5 per degree from 22 to 28 °C |

:::note red Beyond the course description: fitting a curve instead
Prep books go on to "straighten" data like these with logarithms or powers and fit a line to the transformed values. **Transformations to achieve linearity** are on the removed-topics register: the exam asks only that the student recognise, from the residual plot, that a linear model is not the most appropriate. Saying "a curved model would fit these data better" is enough.
:::

Now reopen the **Least-squares Fitter** on **Café iced drinks**. Show the least-squares line and press **Move my line onto it**: the residual plot underneath is the one the student just sketched. Then let them try to find a straight line whose residual plot does not curve. There is none. Least squares finds the best line; it cannot make a line the right model.

---

## 122–134 min · Solo case — St Mary's: patients arriving and mean wait

Unaided. St Mary's 20 evening shifts from Session 4, where the number of patients arriving turned out to be the confounding variable behind doctors and waits. Now the relationship between patients arriving and the mean wait on each shift. Watch, say nothing, note where they hesitate.

Technology gives, for mean wait (minutes) against patients arriving: *a* = 14.51, *b* = 0.4183, *r* = 0.88, *r*² = 0.77. The patients arriving range from 26 to 77.

![St Mary's, 20 evening shifts: the least-squares line and its residual plot](figures/s05-stmarys.svg)

*Left: patients arriving during each shift against the mean wait of the patients seen that shift, with the least-squares line. Right: the residuals against patients arriving.*

1. Write the equation of the least-squares line in context.
2. Interpret the slope in context.
3. Interpret *r*² in context.
4. Shift 10 had 52 patients arriving and a mean wait of 41 minutes. Calculate its residual and interpret it.
5. The rota manager wants predicted mean waits for an evening with 60 arrivals and for a big-event evening expected to bring 110. Give both predictions and say which you would trust more, and why.
6. Using the residual plot, is a linear model appropriate for these data? Explain.

**Answers.**

1. **Predicted mean wait = 14.51 + 0.4183 × (patients arriving)**, or ŷ = 14.51 + 0.4183*x*, where ŷ is the predicted mean wait in minutes and *x* the number of patients arriving during the shift.
2. *"For each additional patient arriving during a shift, the predicted mean wait increases by about 0.42 minutes."* Equivalently, about 4.2 minutes for every 10 extra patients.
3. *"About 77% of the variation in mean waiting time across these shifts is explained by the linear relationship with the number of patients arriving."*
4. ŷ = 14.51 + 0.4183 × 52 = **36.3** minutes, so the residual is 41 − 36.3 = **+4.7 minutes**. The mean wait on that shift was 4.7 minutes longer than the line predicts for a shift with 52 arrivals: the model underpredicts it.
5. **60 arrivals: 39.6 minutes. 110 arrivals: 60.5 minutes.** Trust the first more: 60 is inside the interval of arrivals used to fit the line, 26 to 77, so it is interpolation. 110 is well beyond 77, so it is extrapolation, and less reliable; a very busy evening could behave quite differently, for instance if the department runs out of beds.
6. **Yes.** The residuals scatter above and below 0 across the whole range of arrivals with no curve: apparent randomness, which confirms a linear form, so the linear model is appropriate.

**Watch for:** "each extra patient **causes** the wait to go up 0.42 minutes" or "adds 0.42 minutes" without *predicted* (item 2); "77% of the patients" or "77% of the shifts" (item 3); a residual of −4.7, or "the model overpredicted" (item 4); giving 60.5 minutes with no comment about extrapolation (item 5); "it's appropriate because *r* = 0.88" (item 6: the residual plot, not *r*, is the evidence).

If the student finishes early, point out who shift 10 is: in Session 4 it was the busy shift with only **4** doctors on duty. It had the longest wait among the similarly busy shifts, and here it has one of the largest positive residuals. That is a suggestion, not a proof, but it is the kind of question residuals are good at raising.

---

## 134–142 min · Teach it back

> *"Explain to me why the café's r² of 0.92 did not make the straight line a good model, and what a residual plot shows that r² cannot."*

A good answer contains three things. *r*², like *r*, measures how well a **line** accounts for the variation in the response, and a strong curve can still have a high *r*², so a high *r*² cannot show that the form is linear. The residual plot shows the pattern of the errors: for the café, positive at both ends and negative in the middle, so the line is systematically too low, then too high, then too low again. And the rule: curvature in the residual plot means the linear model is not the most appropriate, while apparent randomness, as for Lincoln High, confirms a linear form.

If the student gets the first and third but cannot describe the café's residual pattern, that is acceptable. If they say "because 0.92 isn't high enough", the scenario has not landed: go back to the café's residual plot and ask *"what would the residuals look like if the line were right?"* Then set the homework.

---
---

# Homework — Session 5

**40 marks · bring to Session 6, self-marked**

## How to do this homework

1. Do every part **with the answer key closed.** Where you are unsure, answer anyway and put a **?** beside it.
2. Then open the key and **mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote.
3. **Bring the marked sheet.** Your wrong answers and your question marks are what Session 6 opens with.

Everything here was taught in the session; this sheet is practice. You need a calculator, and graph paper or a ruler for D2. Use the course's rounding: *a* and *b* to 4 significant figures, keeping at least 2 decimal places; predictions and residuals to 1 decimal place; *r* and *r*² to 2 decimal places. Where a question gives you *a*, *b*, *r* or *r*², they were found with technology.

---

## Part A — Vocabulary (6 marks)

Match each term to its meaning.

| | Term | | Meaning |
|---|---|---|---|
| 1 | Predicted value, ŷ | A | A scatterplot of the residuals against the predicted values or the explanatory variable |
| 2 | Residual | B | The proportion of the variation in the response variable explained by the linear relationship with the explanatory variable |
| 3 | Extrapolation | C | Observed y minus predicted y |
| 4 | Interpolation | D | Predicting with an x-value inside the interval of x-values used to fit the line |
| 5 | Residual plot | E | The response value the model gives for a particular x, a + bx |
| 6 | Coefficient of determination, *r*² | F | Predicting with an x-value beyond the interval of x-values used to fit the line |

## Part B — Oakfield School's line (10 marks)

The 12 Oakfield School students from Session 4's homework, with their distance from school and journey time:

```
 km   min    km   min    km   min    km   min
 1.0    6    2.4    9    2.6   11    3.4   12
 3.0   13    4.2   14    3.8   15    4.6   17
 6.0   19    5.6   21    7.6   26    6.8   38
```

Technology gives *a* = 0.1929, *b* = 3.896, *r* = 0.88 and *r*² = 0.78.

**B1.** Write the equation of the least-squares regression line in context, saying what each symbol stands for. (1)

**B2.** Interpret the slope in context. (2)

**B3.** Interpret the *y*-intercept, and say whether it has a sensible meaning here. (2)

**B4.** Predict the journey time of a student who lives 5 km away, and of one who lives 20 km away. Which prediction is more reliable, and why? (2)

**B5.** Calculate the residual for the student who lives 6.8 km away and took 38 minutes, and interpret it. (2)

**B6.** Interpret *r*² in context. (1)

## Part C — A line from summary statistics (6 marks)

The five spring mornings from Session 4's homework: temperature at 8 am (*x*, °C) and hot drinks sold between 7 and 10 am (*y*). You do not have the raw data on your calculator, only the summary statistics:

| x̄ | *sₓ* | ȳ | *s_y* | *r* |
|---|---|---|---|---|
| 15 °C | 5 °C | 150 drinks | 20 drinks | −0.9375 |

**C1.** Use the formula sheet to calculate the slope *b* and the intercept *a* of the least-squares line. Show your working. (2)

**C2.** Write the equation in context. (1)

**C3.** Predict the number of hot drinks sold on a morning when it is 10 °C at 8 am. (1)

**C4.** On the 19 °C morning the café sold 125 hot drinks. Find the residual. Did the line overpredict or underpredict? (1)

**C5.** Calculate *r*² and interpret it in context. (1)

## Part D — The coffee machine's residual plot (6 marks)

The café's coffee machine warming up, from Session 4's homework F2. Technology gives the least-squares line ŷ = 41.91 + 3.229*x*, where *x* is minutes since the machine was switched on and ŷ the predicted water temperature in °C, with *r* = 0.88 and *r*² = 0.78.

| Minutes | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Water temperature (°C) | 17 | 34 | 44 | 55 | 61 | 68 | 75 | 79 | 85 | 88 | 90 | 91 | 91 | 93 |
| Residual (°C) | −24.9 | −11.1 | −4.4 | 3.4 | 6.2 | 9.9 | **?** | 11.3 | 10.8 | 7.3 | 2.9 | −2.6 | −9.0 | **?** |

**D1.** Calculate the two missing residuals, at 6 minutes and at 20 minutes. Show your working. (2)

**D2.** Construct the residual plot: residuals against minutes since switched on. (2)

**D3.** The manager says: *"r² = 0.78, so the straight line is a good model for how the water heats up."* Use your residual plot to respond. (2)

## Part E — Reversing interpretations at the library (6 marks)

The 18 library branches from Session 4's homework E. For weekly visits (*y*) against the number of residents each branch serves, in thousands (*x*), technology gives ŷ = −9.824 + 38.10*x* and *r*² = 0.91. The branches serve between 8 and 56 thousand residents.

**E1.** A branch serving 24 thousand residents has a residual of +185.4 visits. How many visits did it actually have in the week? (2)

**E2.** What does the residual of +185.4 tell you about that branch? (1)

**E3.** A branch serving 37 thousand residents had 1160 visits. Find its residual. Did the model overpredict or underpredict its visits? (2)

**E4.** The council plans a new branch in a district of 90 thousand residents. Should it use this line to predict the new branch's visits? Explain. (1)

## Part F — True or false about regression (6 marks)

For each statement, write **true** or **false** and give a reason. (1 mark each)

**F1.** "The Lincoln High line has slope 2.019, so every extra kilometre adds 2.019 minutes to every student's journey."

**F2.** "A residual of −3 means the model predicted a value 3 too low."

**F3.** "The least-squares regression line always passes through the point (x̄, ȳ)."

**F4.** "If *r* = 0.9, then about 81% of the variation in the response variable is explained by the linear relationship with the explanatory variable."

**F5.** "The café's iced-drinks line has *r*² = 0.92, so its residual plot must show no pattern."

**F6.** "Predicting the journey time of a Lincoln High student who lives 20 km away is extrapolation, because no student in the data lives between 17 and 28 km."

---
---

# Answer key

*For the student to mark their own work, after attempting everything.*

### Part A (6 marks, 1 each)

1–E · 2–C · 3–F · 4–D · 5–A · 6–B

### Part B (10 marks)

**B1.** (1) **ŷ = 0.1929 + 3.896*x***, where ŷ is the predicted journey time in minutes and *x* the distance from school in km. Or: predicted journey time = 0.1929 + 3.896 × (distance). Writing *y* instead of ŷ, or leaving the symbols undefined, does not earn the mark.

**B2.** (2) *"For each additional kilometre a student lives from school, the predicted journey time increases by about 3.9 minutes."* One mark for *predicted* (or *on average*) with the right direction and amount; one mark for the context and units.

> **"Each kilometre adds 3.9 minutes" earns one mark, not two.** Without *predicted*, it claims every student's journey grows by exactly 3.9 minutes per kilometre, and the 38-minute student at 6.8 km shows it does not.

**B3.** (2) The intercept says a student living 0 km from school has a predicted journey time of 0.19 minutes (1). It has no sensible meaning: the nearest student lives 1.0 km away, so *x* = 0 is outside the interval of distances used, an extrapolation, and a journey of about 12 seconds is not a real prediction for anyone (1).

**B4.** (2) 5 km: ŷ = 0.1929 + 3.896 × 5 = **19.7 minutes**. 20 km: ŷ = 0.1929 + 3.896 × 20 = **78.1 minutes** (1). The 5 km prediction is more reliable: 5 km is inside the interval of distances used, 1.0 to 7.6 km, so it is interpolation; 20 km is far beyond 7.6 km, an extrapolation (1).

**B5.** (2) ŷ = 0.1929 + 3.896 × 6.8 = 26.7, so the residual is 38 − 26.7 = **+11.3 minutes** (1). This student's journey took 11.3 minutes longer than the line predicts for a student living 6.8 km away: the model underpredicts it (1).

> This is the 38-minute student from Session 4's B4(b), who does not fit the pattern. Its residual is the largest of the twelve: a residual is the number that measures "off the pattern". If you wrote −11.3, you subtracted observed from predicted; the order is observed minus predicted.

**B6.** (1) *"About 78% of the variation in journey time is explained by the linear relationship with distance from school."*

### Part C (6 marks)

**C1.** (2) *b* = *r* × (*s_y* ÷ *sₓ*) = −0.9375 × (20 ÷ 5) = **−3.75** (1). *a* = ȳ − *b*x̄ = 150 − (−3.75)(15) = 150 + 56.25 = **206.25** (1).

> **Watch the double negative.** *a* = 150 − (−3.75 × 15) is 150 **plus** 56.25. A student who writes 150 − 56.25 = 93.75 gets a line that does not pass through (15, 150), which the formula sheet's ȳ = *a* + *b*x̄ says it must: check 206.25 − 3.75 × 15 = 150.

**C2.** (1) **Predicted hot drinks sold = 206.25 − 3.75 × (temperature at 8 am)**, or ŷ = 206.25 − 3.75*x* with the symbols defined.

**C3.** (1) ŷ = 206.25 − 3.75 × 10 = 168.75, about **168.8 hot drinks**. (10 °C is inside the interval of temperatures, 8 to 20 °C: interpolation.)

**C4.** (1) ŷ = 206.25 − 3.75 × 19 = 135.0, so the residual is 125 − 135.0 = **−10.0 drinks**: the line **overpredicted**.

**C5.** (1) *r*² = (−0.9375)² = 0.8789, about **0.88**: about 88% of the variation in hot drinks sold is explained by the linear relationship with the 8 am temperature.

### Part D (6 marks)

**D1.** (2) At 6 minutes: ŷ = 41.91 + 3.229 × 6 = 61.3, residual = 75 − 61.3 = **+13.7 °C** (1). At 20 minutes: ŷ = 41.91 + 3.229 × 20 = 106.5, residual = 93 − 106.5 = **−13.5 °C** (1).

> The 20-minute prediction, 106.5 °C, is above boiling point, for water that never passes 93 °C. That alone is a sign the line is the wrong shape.

**D2.** (2) One mark for the axes, residual (°C) up and minutes across, with a line at 0. One mark for all 14 points plotted correctly.

:::reveal Reveal — the D2 residual plot, after you have drawn yours
![Residual plot for the coffee machine's least-squares line](figures/s05-hw-machine-residuals.svg)

*The answer to D2. The residuals are negative for the first three readings, positive from 3 to 14 minutes, and negative again from 16 minutes on: a clear curve.*
:::

**D3.** (2) The manager is wrong (1). The residual plot shows clear **curvature**: negative residuals at the start, positive in the middle, negative again at the end, so the line is systematically too high, then too low, then too high. Curvature in the residual plot means the linear model is not the most appropriate model, whatever *r*² is (1).

> **A high r² does not show a straight line is right.** This is the café's lesson from Scenario B, and Session 4's F2 again: the water heats fast and then levels off, and the residual plot makes the curve impossible to miss.

### Part E (6 marks)

**E1.** (2) ŷ = −9.824 + 38.10 × 24 = 904.6 (1). Actual = predicted + residual = 904.6 + 185.4 = **1090 visits** (1).

**E2.** (1) That branch had 185.4 more visits than the line predicts for a branch serving 24 thousand residents: the model underpredicts its visits.

**E3.** (2) ŷ = −9.824 + 38.10 × 37 = 1399.9, so the residual is 1160 − 1399.9 = **−239.9 visits** (1). Negative, so the model **overpredicted** its visits (1).

**E4.** (1) **No, or only with a strong warning.** 90 thousand residents is far beyond the interval used to fit the line, 8 to 56 thousand, so the prediction would be an extrapolation, and less reliable the further it goes.

> If E1 came out at 719.2, you used predicted minus residual. Rearranging residual = *y* − ŷ gives *y* = ŷ + residual.

### Part F (6 marks, 1 each)

**F1.** **False.** The slope is the **predicted** increase for each extra kilometre. Individual journeys vary around the line: the student 7 km away took 18 minutes, less than the student 5 km away, who took 22.

**F2.** **False.** A negative residual means observed is **below** predicted, so the model predicted a value 3 too **high**: it overpredicted.

**F3.** **True.** The least-squares line always passes through the point of means (5.5.A.1); the formula sheet writes it as ȳ = *a* + *b*x̄.

**F4.** **True.** *r*² = 0.9² = 0.81, and *r*² is the proportion of the variation in the response explained by the linear relationship with the explanatory variable.

**F5.** **False.** A high *r*² does not show a linear form. The café's residual plot curves: positive at both ends and negative in the middle.

**F6.** **False.** 20 km is inside the interval of distances used to fit the line, 0.5 to 28 km, so it is **interpolation**, by the course description's definition. Extrapolation means beyond the interval, not in a gap within it.

### Marks summary

| Part | Marks |
|---|---|
| A — Vocabulary | 6 |
| B — Oakfield School's line | 10 |
| C — A line from summary statistics | 6 |
| D — The coffee machine's residual plot | 6 |
| E — Reversing interpretations at the library | 6 |
| F — True or false about regression | 6 |
| **Total** | **40** |

---
---

# Reference sheet — keep this

*Every term carries an example. The examples use the 25 Lincoln High students unless stated: distance from school, 0.5 to 28 km, and journey time, 8 to 68 minutes, with least-squares line ŷ = 8.762 + 2.019x.*

### The regression model and prediction: the rules (5.3.A)

**Linear regression model** — a linear equation that uses the explanatory variable *x* to predict the response *y*; used only when the form appears linear.
*Example: predicted journey time = 8.762 + 2.019 × (distance from school).*

**Predicted value, ŷ** — the response the model gives for a particular *x*: ŷ = *a* + *bx*.
*Example: for a student 12 km away, ŷ = 8.762 + 2.019 × 12 = 33.0 minutes.*

**Interpolation** — predicting with an *x*-value within the interval of *x*-values used to fit the line.
*Example: 12 km is inside 0.5 to 28 km. So is 20 km, although no student lives between 17 and 28 km.*

**Extrapolation** — predicting with an *x*-value beyond that interval. Less reliable the further it goes; always say that it is an extrapolation.
*Example: a new student 45 km away: ŷ = 99.6 minutes, 17 km beyond the furthest student in the data.*

### Residuals and residual plots: the rules (5.4)

**Residual** — observed *y* minus predicted *y*: residual = *y* − ŷ. The vertical distance from the point to the line, in the units of *y*.
*Example: the student at 2.5 km who took 33 minutes: 33 − 13.8 = +19.2 minutes.*

| Residual | The model | Example |
|---|---|---|
| positive | **underpredicts**: actual higher than predicted | the 2.5 km student, +19.2: 19.2 minutes longer than predicted for 2.5 km |
| negative | **overpredicts**: actual lower than predicted | the 7 km student, −4.9: 18.0 minutes against a prediction of 22.9 |

**From a residual back to the individual** — actual = predicted + residual.
*Example: 7 km, residual −4.9: 22.9 + (−4.9) = 18.0 minutes.*

> **Interpret a residual in three parts:** the size, in the response's units; *more* or *less than predicted*; and the individual's *x*. "4.9 minutes less than the line predicts for a student who lives 7 km away." Not "less than average", and never about *x*.

**Residual plot** — a scatterplot of the residuals against the predicted values or against *x*, with a line at 0.

| What the residual plot shows | What it means | Example |
|---|---|---|
| **Apparent randomness** | confirms a linear form: the linear model is appropriate | Lincoln High: a flat band around 0, apart from the 2.5 km student. St Mary's shifts |
| **Curvature** | the linear model is not the most appropriate | the café's iced drinks: +23 at 12 °C, −14 at 18 °C, +23 at 28 °C. The coffee machine |

> **A high r or r² does not show a straight line is right.** The café's iced drinks have *r* = 0.96 and *r*² = 0.92, and the residual plot curves. Look at the residual plot.

### The least-squares line and its coefficients: the rules (5.5.A)

**Least-squares regression line (LSRL)** — the line that makes the sum of the squared residuals, Σ(*y* − ŷ)², as small as possible. Found with technology. It always passes through (x̄, ȳ).
*Example: Σ(residual²) = 438.3 for the Lincoln line, smaller than for any other line; the line passes through (6.28, 21.44). The 2.5 km student's square, 19.2² ≈ 368, is most of that total.*

**Slope *b* and *y*-intercept *a*** — the coefficients of the line, calculated from the sample: statistics. Found with technology, or from summary statistics with the formula sheet:

:::formula
ŷ = a + bx        b = r × (s_y ÷ sₓ)        ȳ = a + b x̄, so a = ȳ − b x̄
:::

*Example: r = 0.9450, s_y = 13.07, sₓ = 6.117, so b = 0.9450 × 13.07 ÷ 6.117 = 2.019, and a = 21.44 − 2.019 × 6.28 = 8.76. At the café's spring mornings: b = −0.9375 × 20 ÷ 5 = −3.75 and a = 150 + 3.75 × 15 = 206.25.*

**Coefficient of determination, *r*²** — the square of *r*: the proportion of the variation in the response variable that is explained by the linear relationship with the explanatory variable.
*Example: r² = 0.89: about 89% of the variation in journey time is explained by the linear relationship with distance. Read it from the calculator, not from 0.95², which gives 0.90.*

**Rounding** — *a* and *b* to 4 significant figures, keeping at least 2 decimal places (8.762, 2.019, −133.03, 0.4183; exact values as they are, −3.75). Predictions and residuals worked from the equation as written, to 1 decimal place. *r* and *r*² to 2 decimal places; in *b* = *r*(*s_y* ÷ *sₓ*), carry *r* to 4.

### Model sentences for slope, intercept and r² (5.5.B, 5.5.A.5)

| Quantity | Model sentence | Lincoln High |
|---|---|---|
| **Slope** | For each additional [unit of x], the **predicted** [y] increases (decreases) by [b and units] | For each additional kilometre from school, the predicted journey time increases by about 2.02 minutes |
| **Intercept** | The **predicted** [y] when [x] is 0 is [a]; then check that 0 is inside the x-values and the value is possible | The predicted journey time at 0 km is 8.762 minutes, but no student lives closer than 0.5 km, so it is an extrapolation |
| ***r*²** | About [r² as %] of the variation in [y] is explained by the linear relationship with [x] | About 89% of the variation in journey time is explained by the linear relationship with distance |

**When the intercept means nothing** — when *x* = 0 is beyond the interval of *x*-values (extrapolation), or the predicted value is impossible.
*Example: the café's iced-drinks line has a = −133.03: at 0 °C, outside 12 to 28 °C, and a negative number of drinks. Both.*

> **Keep the word "predicted".** "Each kilometre adds 2.02 minutes" claims every student's journey changes by exactly that, and the residuals show it does not.

### The TI-84 and the formula sheet: a quick guide

| Task | How |
|---|---|
| The line, *r* and *r*² | *x* in L1, *y* in L2 · STAT → CALC → LinReg(a+bx). If *r* and *r*² are missing, turn on Stat Diagnostics |
| Translate the screen | a=8.762237762, b=2.018751949 becomes ŷ = 8.762 + 2.019*x*, with ŷ and *x* named in context |
| Means and SDs for the formula sheet | STAT → CALC → 2-Var Stats, or 1-Var Stats on each list |
| Formula sheet, section I | ŷ = *a* + *bx* · ȳ = *a* + *b*x̄ · *b* = *r*(*s_y* ÷ *sₓ*) · *r* = (1 ÷ (*n* − 1)) Σ *zₓ z_y* |

:::note red Not in the course description
**Standard deviation of the residuals** (*s*, "S =" in computer output), **residuals sum to zero**, **influential points**, **high-leverage points**, **outliers in regression** as a special category, **"fanning"** in a residual plot, **transformations to achieve linearity**, **regression to the mean**, and everything in a computer output table except the coefficients and R-sq (**SE Coef, T, P, R-sq(adj)**, which belong to inference for slope or are absent). Prep books teach all of these; the exam formula sheet prints the slope's sampling distribution. None is examinable under the 2026 course description.
:::

---

*CED references: Topic 5.3 (5.3.A.1–4), Topic 5.4 (5.4.A.1, 5.4.B.1, 5.4.C.1–4), Topic 5.5 (5.5.A.1–5, 5.5.B.1–3); also 5.2.A.3 (a high r does not prove linear form) and the unit overview on translating technology output. Course and Exam Description effective Fall 2026; exam reference information (formula sheet) 2026.*

*Supporting reading: Barron's pdf 174–191 · Princeton Review 147–167 · 5 Steps to a 5 99–104. All three also teach the off-syllabus topics listed above.*

*Next session: Topics 1.10–1.11 — the investigative question revisited, sampling methods, and why randomisation is what licenses inference.*
