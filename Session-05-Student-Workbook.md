# Session 5 — The Regression Line: Prediction, Residuals and Least Squares

**AP Statistics · Twenty-Hour Course · Student edition, to work through on your own**
**CED Topics 5.3, 5.4, 5.5 · About 177 minutes, plus homework**

---

## How to use this

The same rule as every session so far. Today you will calculate more than last time, and most of the marks are in the sentences you write about each number.

:::note amber Write first, then reveal
Every **Your turn** box asks you to do something before the text shows you the answer. **Do it on paper first.** The equations, predictions, residuals, residual plots and every interpretation are hidden behind reveals so that you cannot copy them. A residual you worked out with the wrong sign, and then corrected, will stay with you; one you read will not.
:::

**What you need:** paper, a pen, a ruler, and a calculator that does linear regression. A TI-84 is assumed: STAT → CALC → LinReg(a+bx), with Stat Diagnostics on so that *r* and *r*² appear.

### How this maps to your tutor's document

Working alone with a pen is slower than working with a tutor, so each part is given about a quarter longer than the tutor's segment. Take the time: the writing is the learning.

| Your section | Tutor's section | Minutes |
|---|---|---|
| Part 1 — Your Session 4 homework, and a warm-up | 0–10 Homework debrief and diagnostic | 13 |
| Part 2 — Theory: the least-squares line and its residuals | 10–35 Theory — the least-squares regression line and its residuals | 31 |
| Part 3 — Lincoln High: a line for journey time | 35–80 Scenario A | 56 |
| Part 4 — Reversing Interpretations, on your own | 80–97 Activity | 21 |
| Part 5 — The café's iced drinks | 97–122 Scenario B | 31 |
| Part 6 — On your own: St Mary's shifts | 122–134 Solo case | 15 |
| Part 7 — Explain it back | 134–142 Teach it back | 10 |
| **Total** | **142 minutes** | **177** |

If your tutor has not yet set the **Session 3 test**, take it before Part 1: 40 minutes, timed, answer key closed.

---

## Part 1 — Your Session 4 homework, and a warm-up

Get out your marked Session 4 homework and make two lists: the questions you got **wrong**, and the questions you marked with a **?**, including the ones that turned out right.

**Two specific things to check.** They are two of the likeliest errors on that sheet, and both come back today.

- **F2: did you agree with the manager?** "*r* = 0.88 is close to 1, so the water heats at a steady rate." The plot shows the water heating fast and then levelling off. If you agreed, you read *r* instead of the picture. Today gives you a second tool, the **residual plot**, that shows a curve even more plainly, and this session's homework D uses the same coffee machine.
- **B4(b): did you say the 38-minute Oakfield journey was unusual "because it is the longest"?** That is one-variable reasoning from Session 3. In a scatterplot it is unusual because it sits far from the pattern *for a student living 6.8 km away*. Today that distance from the pattern gets a name and a number, the **residual**, and in this session's homework the 38-minute student has the largest residual of the twelve.

### Warm-up

:::yourturn
Four questions. Answer all four on paper before revealing.

1. A line has the equation *y* = 5 + 3*x*. What is *y* when *x* = 4? And what does the 3 tell you?
2. A weather app forecast 20 °C for midday, and it was actually 23 °C. Was the forecast too high or too low, and by how much?
3. Lincoln High's distances and journey times have *r* = 0.95. Does that show that a straight line is the right model?
4. In Session 4, why was the student with the 68-minute journey not unusual in the scatterplot?
:::

:::reveal Reveal — and what your answers mean
| If you said | It means | Do this |
|---|---|---|
| **1:** 17, and *y* goes up 3 for each 1 in *x* | School algebra is secure | Carry on |
| **1:** 17, but nothing for the 3 | You can substitute but have no picture of slope yet | Read Part 2's *Interpreting the slope* slowly |
| **2:** too low, by 3 degrees | You already have the idea of a residual, and its sign | Part 2 names it |
| **2:** too high, or "−3" | You subtracted in the wrong order | The most common regression error. Read Part 2's two residual subsections slowly, and say *observed minus predicted* aloud every time today |
| **3:** no, you have to look at the plot | Session 4 has held | Carry on; Part 2 gives you the residual plot |
| **3:** yes, it is close to 1 | You are trusting *r* for form | That is the whole of Part 5. Read it slowly |
| **4:** it fits the pattern: that student lives furthest away | Session 4 has held | Carry on; today that student's residual is only 2.7 minutes |
| **4:** it was an outlier | You are still judging a point against one variable | Look again at Session 4's Lincoln scatterplot before Part 2 |
:::

---

## Part 2 — Theory: the least-squares line and its residuals

Session 4 described a relationship between two variables. Today you fit a line to it, use the line to predict, and then check whether the line deserves to be used at all.

Two errors run through this topic, and every part of today is built to catch them. The first is getting the sign of a residual backwards, which turns every interpretation upside down. The second is trusting a single number, *r* or *r*², to tell you that a straight line is the right model, when only the residual plot can.

**Read this part in full before Part 3.** It states every idea the session uses, each with its code from the course description, the rule, the formula where there is one, and what the rule does **not** say, which is where most marks are lost. The illustrations use bare, made-up numbers on purpose, most of them Session 4's tiny data sets; Parts 3 to 7 apply the same rules to real data. There is nothing to write until the self-check at the end. When a later part says "from Part 2", this is where to look.

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

### Self-check on the theory

Answer each on paper, then open its reveal. If one goes wrong, reread that subsection's "what it does not say" paragraph before Part 3: the rest of the session leans on every one of them.

**Check 1.** A model is ŷ = 4 + 2*x*. An individual has *x* = 3 and *y* = 13. What is the residual, and did the model overpredict or underpredict?

:::reveal Reveal — check 1
ŷ = 4 + 2 × 3 = 10, so the residual is 13 − 10 = **+3**. Positive, so the model **underpredicts** by 3: the actual value is 3 more than predicted.
:::

**Check 2.** A line was fitted to *x*-values from 5 to 20. Is a prediction at *x* = 12 interpolation or extrapolation? At *x* = 30?

:::reveal Reveal — check 2
*x* = 12 is inside 5 to 20: **interpolation**. *x* = 30 is beyond 20: **extrapolation**, and less reliable the further beyond it goes.
:::

**Check 3.** A residual plot shows the residuals high at both ends and low in the middle. What does that tell you?

:::reveal Reveal — check 3
**Curvature**: the linear model is not the most appropriate model for the data.
:::

**Check 4.** What is "least" about the least-squares line, and which point must it pass through?

:::reveal Reveal — check 4
The **sum of the squared residuals** is as small as it can be for any line. The line always passes through the point of means, **(x̄, ȳ)**.
:::

**Check 5.** *r* = −0.8, *sₓ* = 2 and *s_y* = 10. What is the slope of the least-squares line? What is *r*², and what does it mean?

:::reveal Reveal — check 5
*b* = *r* × (*s_y* ÷ *sₓ*) = −0.8 × 10 ÷ 2 = **−4**. *r*² = 0.64: **64% of the variation in *y* is explained by the linear relationship with *x***. The slope and *r* always have the same sign.
:::

**Check 6.** *r*² = 0.95. Is a straight line the right model?

:::reveal Reveal — check 6
**Not from that alone.** A strong curve can have a high *r*². Look at the residual plot: apparent randomness confirms a linear form, curvature says the linear model is not the most appropriate.
:::

---

## Part 3 — Lincoln High: a line for journey time

The same 25 randomly chosen Lincoln High students as in Sessions 2 to 4. In Session 4 you described the scatterplot as a **strong, positive, linear** association with *r* = 0.95, and found one student who does not fit the pattern: 2.5 km away, 33 minutes. The line makes sense only because the form is linear.

```
 km   min    km   min    km   min    km   min    km   min
 0.5    8    1.0    9    1.0   10    1.5   11    2.0   12
 1.5   12    2.5   13    3.0   14    4.5   15    3.5   15
 4.0   16    4.5   17    7.0   18    5.5   18    6.0   20
 6.5   21    5.0   22    7.5   24    8.0   25    9.5   27
11.0   30    2.5   33   14.0   36   17.0   42   28.0   68
```

### From calculator output to an equation

:::yourturn
Enter the distances in L1 and the times in L2 and run LinReg(a+bx). Write down *a*, *b*, *r*² and *r* exactly as the screen shows them.

Then write the equation of the least-squares line **the way you would on the exam**: rounded by the course's convention from Part 2, with every symbol named in context.
:::

:::reveal Reveal — the equation of the Lincoln High line
The TI-84 shows:

```
LinReg
 y=a+bx
 a=8.762237762
 b=2.018751949
 r²=.8930436544
 r=.94500987
```

**ŷ = 8.762 + 2.019*x***, where ŷ is the **predicted** journey time in minutes and *x* is the distance from school in kilometres. Or in words: predicted journey time = 8.762 + 2.019 × (distance from school).

Check yours against two common losses:

- **"y = 8.762 + 2.019x".** Without the hat, the equation claims every student who lives *x* km away takes exactly that long. It is a prediction: write ŷ, or "predicted journey time".
- **"y = a + bx", copied from the screen.** That is calculator speak. The answer is the equation with the numbers in and the variables named: the translation the course description asks you to practise.

The rounding is Part 2's convention: 4 significant figures, so 8.762 and 2.019.
:::

:::note red Beyond the course description: a full computer output table
Prep books and older exams print regression output from statistical software like this, for the same 25 students:

| Predictor | Coef | SE Coef | T | P |
|---|---|---|---|---|
| Constant | 8.762 | 1.265 | 6.93 | 0.000 |
| Distance | 2.019 | 0.146 | 13.86 | 0.000 |

S = 4.366 · R-sq = 89.3% · R-sq(adj) = 88.8%

Only three numbers here are in the course description: the **Constant's Coef is *a***, the **Distance Coef is *b***, and **R-sq is *r*²**. SE Coef, T and P belong to inference for the slope, which is on the course's removed-topics register; S, the standard deviation of the residuals, and R-sq(adj) do not appear in the course description at all. If you meet a table like this, read off *a*, *b* and *r*², and ignore the rest.
:::

### Checking the line

Two quick checks, each from a Part 2 subsection. They are also the fastest way to catch a mistyped list.

:::yourturn
1. Part 2 says the least-squares line passes through one particular point. Use 1-Var Stats on L1 and L2 to find it, and check that the line goes through it.
2. 1-Var Stats also gives *sₓ* = 6.117 km and *s_y* = 13.07 minutes. Use the formula sheet's route to find the slope from *r*, and then the intercept.
:::

:::reveal Reveal — two checks on the line
**1.** The point of means, (x̄, ȳ) = **(6.28, 21.44)**. And 8.762 + 2.019 × 6.28 = 21.44. It passes through.

**2.** *b* = *r* × (*s_y* ÷ *sₓ*) = 0.9450 × 13.07 ÷ 6.117 = **2.019**. Then *a* = ȳ − *b*x̄ = 21.44 − 2.019 × 6.28 = **8.76**. The same line by the second route. (It comes out at 8.761 to three decimal places, only because *b* was rounded before it was used; write the calculator's 8.762.)

If you got *b* = 2.03, you used *r* = 0.95. In this route carry *r* to at least 4 decimal places: rounding it to 2 moves *b* in the second decimal place.
:::

### What the slope and intercept say

:::yourturn
1. Interpret the slope, 2.019, in context.
2. Interpret the intercept, 8.762, in context. Does it have a sensible meaning here?
:::

:::reveal Reveal — slope and intercept in context
**1.** *"For each additional kilometre a student lives from school, the **predicted** journey time increases by about 2.02 minutes."* Four parts, from Part 2's *Interpreting the slope*: each additional unit of *x*, the word *predicted*, the direction, and the amount with units.

If you wrote *"each extra kilometre adds 2.02 minutes to the journey"*, look at the student 7 km away who took 18 minutes and the one 5 km away who took 22: further away, shorter journey. The slope describes predictions, and the sentence needs *predicted* or *on average*. This is the error examiners penalise most often on slope questions.

**2.** *"A student who lives 0 km from school has a predicted journey time of 8.762 minutes."* Then the judgement, from Part 2's *Interpreting the y-intercept*: no student lives closer than 0.5 km, so *x* = 0 is outside the interval of distances used to fit the line. It is an extrapolation, only a small one, and 8.8 minutes is not absurd for someone living next to the school; but it is not a reliable figure. What you must not write is that it takes 8.762 minutes "before you have travelled anywhere", as if the intercept were a measured fact.
:::

### Predicting two journeys

:::yourturn
1. Predict the journey time of a student who lives **12 km** from school. Is this interpolation or extrapolation?
2. A new student joins next term. She lives in a village **45 km** away. What does the line predict for her? How much would you trust it, and why?
:::

:::reveal Reveal — 12 km, and 45 km
**1.** ŷ = 8.762 + 2.019 × 12 = **33.0 minutes**. **Interpolation**: 12 km is inside the interval of distances used to fit the line, 0.5 to 28 km.

**2.** ŷ = 8.762 + 2.019 × 45 = **99.6 minutes**, and this is the trap of the scenario. The arithmetic is exactly as easy as for 12 km, and it looks as trustworthy. It is not. The furthest student in the data lives 28 km away, so 45 km is **extrapolation**, 17 km beyond the data, and a prediction is less reliable the further it is extrapolated. There is a good reason to doubt it: a student that far away probably travels by train or a direct bus, which covers the extra kilometres faster than the pattern for students who walk, cycle or take a local bus. The data cannot say, and that is the point.

![The Lincoln High line over the data, extended to 45 km](figures/s05-lincoln-extrapolate.svg)

*The shaded band is the interval of distances used to fit the line. The prediction at 12 km is inside it: interpolation. The dashed extension to 45 km is extrapolation: the line has no data out there.*

*A prediction is only as good as the data behind it. Inside the interval of x-values it is interpolation; beyond it, extrapolation, and less reliable the further it goes. Say which it is, every time.*
:::

### The 33-minute student's residual

:::yourturn
1. The student at 2.5 km took 33 minutes. What does the line predict for her? What is her residual?
2. Write one sentence saying what her residual tells you about her.
3. Now the 68-minute student at 28 km, Session 3's outlier. Find his residual. What do the two residuals, side by side, tell you?
:::

:::reveal Reveal — two residuals, and Session 4's trap in numbers
**1.** ŷ = 8.762 + 2.019 × 2.5 = 13.8 minutes. Residual = observed − predicted = 33 − 13.8 = **+19.2 minutes**.

**2.** *"Her journey took 19.2 minutes longer than the line predicts for a student who lives 2.5 km from school: the model underpredicts her journey time."*

**3.** ŷ = 8.762 + 2.019 × 28 = 65.3, so his residual is 68 − 65.3 = **+2.7 minutes**. Small: the line predicts him well.

![The Lincoln High least-squares line, with the 33-minute student's residual](figures/s05-lincoln-line.svg)

*The least-squares line through the 25 students, passing through the point of means. The orange segment is the 2.5 km student's residual.*

This is Session 4's trap turned into numbers. The student extreme in **both** variables has a residual of 2.7: he fits the pattern. The student ordinary in both has a residual of 19.2, the largest of the 25: she is the one who does not fit. A residual measures exactly the "how far off the pattern" that Session 4 had to judge by eye.

Check yours against two common losses:

- **−19.2.** You subtracted observed from predicted. Residual = observed − predicted, always; the sign is the whole meaning.
- **"19.2 minutes longer than average."** The mean journey is 21.44 minutes, and she took 11.6 more than that. A residual compares her with the prediction **for her distance**, not with everybody.
:::

### How much variation distance explains

:::yourturn
The screen gave *r*² = .8930. Interpret it in context.
:::

:::reveal Reveal — r² for the journeys
*"About **89%** of the variation in journey time is explained by the linear relationship with distance from school."* That is Part 2's wording for *r*², word for word, with the variables put in.

Three ways this goes wrong:

- **"0.95² = 0.90, so 90%."** You squared the rounded *r*. Read *r*² from the screen, or square the unrounded *r*: 0.94501² = 0.8930. On a multiple-choice question whose options are a percentage point apart, that costs the mark.
- **"89% of the students' journeys are explained."** It is 89% of the **variation** in journey time, not 89% of the students.
- **"Distance causes 89% of the journey time."** *r*² describes a fitted line, not causes. Session 4's rule still holds.

The other 11% is the scatter around the line: the residuals. The biggest single piece of it is the 33-minute student.
:::

### The journeys' residual plot

:::yourturn
1. Before you look: if a straight line is the right model for these journeys, what should the residual plot look like?
2. Find the residuals of the students at 0.5 km (8 minutes) and 7.0 km (18 minutes). With the two you already have, you have four points of the residual plot.
3. Open the reveal, check your four points against the full plot, and say what it tells you about the model.
:::

:::reveal Reveal — the journeys' residual plot
**1.** Points scattered above and below 0 with no pattern and no curve: Part 2's *apparent randomness*.

**2.** 0.5 km: ŷ = 9.8, residual 8 − 9.8 = **−1.8**. 7.0 km: ŷ = 22.9, residual 18 − 22.9 = **−4.9**. With 2.5 km (+19.2) and 28 km (+2.7).

![Residual plot for the Lincoln High line: residuals against distance](figures/s05-lincoln-residuals.svg)

*Residuals against distance from school, for all 25 students.*

**3.** The residuals sit in a flat band around 0 all the way from 0.5 km to 28 km, with **no curve**. That apparent randomness confirms the linear form, so **the linear model is appropriate**. The one large residual, 19.2, is the 2.5 km student who does not fit the pattern.

If you thought "most of the residuals are negative, so it is a bad line": many residuals are around −1 because the 19.2 lifts the line a little, but the band is still flat. The course description's question is randomness versus curvature, and there is no curve.
:::

### Least-squares Fitter

:::sim least-squares-fitter | Least-squares Fitter | 1360
Open on **Lincoln High**. Turn on **squares of the residuals**, move the two handles until Σ(residual²) is as small as you can make it, and **write your best number down** before you press **Show the least-squares line**. Then work out what share of the least-squares total comes from one square, the 33-minute student's. Then try **Flat line at ȳ**. Leave the **café** until Part 5.
:::

:::reveal Reveal — what the fitter shows
Nobody beats the least-squares line: its Σ(residual²) is **438.3**, and that is what "least squares" means, the smallest sum of squared residuals of any line. The 2.5 km student's square is 19.2² ≈ 368, about **84%** of the total, from one student in 25. Squaring makes big residuals count for far more than small ones, as Part 2 warned. The flat line at ȳ, which ignores distance altogether, leaves a sum of **4098.2**.
:::

---

## Part 4 — Reversing Interpretations, on your own

The course description's own activity for residuals: instead of interpreting a residual you have calculated, you are given the residual and the equation and asked what it tells you about that individual. Its example is a wolf 1.4 m long with a residual of −9.87; its sample exam question 24 is the same move as an exam item. Today's individuals are Lincoln High students, with the line ŷ = 8.762 + 2.019*x*.

### Round 1: from a residual back to the student

:::yourturn
For each card, find the predicted journey time, then the student's **actual** journey time, and write one sentence saying what the residual tells you about that student.

| Card | Distance | Residual |
|---|---|---|
| A | 7.0 km | −4.9 minutes |
| B | 5.0 km | +3.1 minutes |
| C | 2.5 km | +19.2 minutes |
| D | 7.5 km | +0.1 minutes |
:::

:::reveal Reveal — the four students
Rearrange residual = *y* − ŷ: **actual = predicted + residual**.

| Card | Predicted, ŷ | Actual, ŷ + residual | What it tells you |
|---|---|---|---|
| A | 8.762 + 2.019 × 7 = 22.9 | 22.9 − 4.9 = **18.0 min** | Her journey took 4.9 minutes less than the line predicts for a student 7 km away; the model overpredicts |
| B | 18.9 | 18.9 + 3.1 = **22.0 min** | 3.1 minutes longer than predicted for 5 km; the model underpredicts |
| C | 13.8 | 13.8 + 19.2 = **33.0 min** | 19.2 minutes longer than predicted for 2.5 km: the student who does not fit |
| D | 23.9 | 23.9 + 0.1 = **24.0 min** | almost exactly what the line predicts for 7.5 km |

If card A gave you **27.8**, you added 4.9 instead of adding −4.9: that is predicted minus observed, backwards. And card D is not a "perfect" student: a residual of 0.1 says only that the line predicts this student almost exactly, nothing about whether the journey is short or long.
:::

### Round 2: judge four interpretations

:::yourturn
Each of these is someone's interpretation of card A's residual: 7 km, residual −4.9 minutes. Mark each right or wrong, and for each wrong one, name the error.

1. *"This student's journey was 4.9 minutes shorter than the average journey."*
2. *"The model underestimated this student's journey time by 4.9 minutes."*
3. *"This student lives 4.9 km closer to school than the line predicts."*
4. *"This student's journey took 4.9 minutes less than the line predicts for a student who lives 7 km from school, so the model overpredicted her journey time."*
:::

:::reveal Reveal — which interpretation earns the mark
**Only 4.**

1. **Wrong: compares with the mean**, 21.44 minutes, not with the prediction for her distance.
2. **Wrong: the sign is backwards.** Her actual time, 18.0, is below the prediction, 22.9, so the model's guess was too high: it **over**estimated.
3. **Wrong: treats the residual as a distance in *x*.** Residuals are in the response's units, minutes, and say nothing about where she lives.
4. **Right**: it has the size in minutes, *less than predicted*, and the student's distance.

*A residual of −4.9 means the actual value was 4.9 below what the model predicts for that x: the model overpredicts. Actual = predicted + residual.*
:::

---

## Part 5 — The café's iced drinks

Back to the café. On the same 10 days as in Sessions 3 and 4, it recorded the midday temperature and the number of iced drinks it sold. In Session 4 you saw the scatterplot bend upwards, with *r* = 0.96.

| Midday temperature (°C) | 12 | 14 | 15 | 15 | 16 | 18 | 19 | 21 | 22 | 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| Iced drinks sold | 9 | 11 | 13 | 16 | 20 | 31 | 44 | 64 | 74 | 167 |

### The manager's line

The manager runs LinReg(a+bx) and gets *a* = −133.03, *b* = 9.885, *r* = 0.96 and *r*² = 0.92.

> *"The line is ŷ = −133.03 + 9.885x, and r² is 0.92, so it explains 92% of the variation. That's an excellent model. I'll use it to plan how many iced drinks to prepare each morning from the forecast."*

:::yourturn
1. Write the correct interpretation of *r*² = 0.92. Is the manager's first sentence right?
2. What did Session 4 already tell you about this scatterplot that should make you cautious about the second sentence?
:::

:::reveal Reveal — what r² does and does not settle
**1.** *"About 92% of the variation in iced drinks sold is explained by the linear relationship with midday temperature."* The manager's first sentence is right. The conclusion, "an excellent model", does not follow from it: Part 2 says *r*² says nothing about whether a line is the right model.

**2.** The scatterplot **curves upwards**: iced sales rise slowly at first and then fast. A correlation close to 1 does not show a linear form (Session 4, 5.2.A.3), and neither does an *r*² close to 1.

**This is the trap of the scenario: a high r², like a high r, does not show that a straight line is the right model.**
:::

### Two predictions the line gets wrong

:::yourturn
1. Use the line to predict iced drinks on a 12 °C day. The café actually sold 9 on its 12 °C day: find the residual.
2. Do the same for 18 °C, when it sold 31.
:::

:::reveal Reveal — −14.4 drinks, and 44.9
**1.** ŷ = −133.03 + 9.885 × 12 = **−14.4 iced drinks**, which is impossible. The residual is 9 − (−14.4) = **+23.4**. And 12 °C is **inside** the interval of temperatures used, 12 to 28 °C: this is interpolation, and the line still predicts something impossible. The problem is not extrapolation; it is the model.

**2.** ŷ = −133.03 + 9.885 × 18 = **44.9**, so the residual is 31 − 44.9 = **−13.9**: the model overpredicts by 13.9 drinks. (44.9 is ȳ, because 18 °C is x̄ and the least-squares line passes through the point of means.)

The same line underpredicts the coldest day by 23 drinks and overpredicts a middling day by 14. A line that is too low at one end and too high in the middle is not making random errors.
:::

### The iced drinks' residual plot

Here are all ten residuals, rounded to the nearest drink, since only the pattern matters for the plot:

| Temperature (°C) | 12 | 14 | 15 | 15 | 16 | 18 | 19 | 21 | 22 | 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| Residual (drinks) | +23 | +6 | −2 | +1 | −5 | −14 | −11 | −11 | −10 | +23 |

:::yourturn
Sketch the residual plot, residuals against temperature, with a line at 0. What shape do you get, and what does it tell you about the linear model? Then write your answer to the manager in two or three sentences, quoting numbers.
:::

:::reveal Reveal — the residual plot, and the answer to the manager
![Café: the least-squares line for iced drinks, and its residual plot](figures/s05-cafe-iced.svg)

*Left: the least-squares line, predicting −14.4 iced drinks at 12 °C, below the dashed zero line. Right: the residuals, positive at both ends and negative in the middle.*

The residuals are **positive at the cold end, negative through the middle and positive again at 28 °C**: a curve. By Part 2's *Reading a residual plot*, **curvature suggests the linear model is not the most appropriate model** for these data.

> *"The line does explain about 92% of the variation in iced drinks sold (r² = 0.92), but the residual plot shows clear curvature: the residuals are positive at both ends, around +23 drinks at 12 °C and at 28 °C, and negative in the middle, down to −14 at 18 °C. So a linear model is not the most appropriate model for these data. The line even predicts −14.4 iced drinks at 12 °C. A high r² does not show that a straight line is the right model."*
:::

### What the café can and cannot say

:::yourturn
1. The slope is 9.885. What would it say in context, and why is it misleading here? (Look at how fast sales rise between 12 and 16 °C, and between 22 and 28 °C.)
2. The intercept is −133.03. Does it have a meaning? Use both of Part 2's tests.
3. Decide which of these four statements the data support:
   - "Iced drink sales and midday temperature have a strong, positive association."
   - "About 92% of the variation in iced drinks sold is explained by the linear relationship with temperature."
   - "So the straight line is a good model for planning."
   - "Each extra degree brings about 9.9 more iced drinks."
:::

:::reveal Reveal — slope, intercept and what is supported
**1.** *"For each 1 °C increase in midday temperature, the predicted number of iced drinks sold increases by about 9.9."* But sales rise by about **2.75 drinks per degree** from 12 to 16 °C (9 to 20) and about **15.5 per degree** from 22 to 28 °C (74 to 167). One slope cannot describe a rate that keeps changing: the slope is only as trustworthy as the line.

**2.** It is the predicted number of iced drinks at 0 °C, and it fails **both** tests: 0 °C is outside 12 to 28 °C, so it is an extrapolation, and a negative number of drinks is impossible.

**3.**

| Statement | Supported? |
|---|---|
| "Iced drink sales and midday temperature have a strong, positive association." | **Yes**: the scatterplot and *r* = 0.96 |
| "About 92% of the variation in iced drinks sold is explained by the linear relationship with temperature." | **Yes**: that is what *r*² = 0.92 means |
| "So the straight line is a good model for planning." | **No**: the residual plot curves, so a linear model is not the most appropriate |
| "Each extra degree brings about 9.9 more iced drinks." | **No**: sales rise by about 2.75 per degree from 12 to 16 °C and about 15.5 per degree from 22 to 28 °C |
:::

:::note red Beyond the course description: fitting a curve instead
Prep books go on to "straighten" data like these with logarithms or powers and fit a line to the transformed values. **Transformations to achieve linearity** are on the course's removed-topics register: the exam asks only that you recognise, from the residual plot, that a linear model is not the most appropriate. Saying "a curved model would fit these data better" is enough.
:::

Now go back to the **Least-squares Fitter** in Part 3 and choose **Café iced drinks**. Show the least-squares line and press **Move my line onto it**: the residual plot underneath is the one you just sketched. Then try to find a straight line whose residual plot does not curve. There is none. Least squares finds the best line; it cannot make a line the right model.

---

## Part 6 — On your own: St Mary's shifts

No hints in this part. St Mary's 20 evening shifts from Session 4, where the number of patients arriving turned out to be the confounding variable behind doctors and waits. Now the relationship between patients arriving and the mean wait on each shift.

Technology gives, for mean wait (minutes) against patients arriving: *a* = 14.51, *b* = 0.4183, *r* = 0.88, *r*² = 0.77. The patients arriving range from 26 to 77.

![St Mary's, 20 evening shifts: the least-squares line and its residual plot](figures/s05-stmarys.svg)

*Left: patients arriving during each shift against the mean wait of the patients seen that shift, with the least-squares line. Right: the residuals against patients arriving.*

:::yourturn
1. Write the equation of the least-squares line in context.
2. Interpret the slope in context.
3. Interpret *r*² in context.
4. Shift 10 had 52 patients arriving and a mean wait of 41 minutes. Calculate its residual and interpret it.
5. The rota manager wants predicted mean waits for an evening with 60 arrivals and for a big-event evening expected to bring 110. Give both predictions and say which you would trust more, and why.
6. Using the residual plot, is a linear model appropriate for these data? Explain.
:::

:::reveal Reveal — St Mary's
1. **Predicted mean wait = 14.51 + 0.4183 × (patients arriving)**, or ŷ = 14.51 + 0.4183*x*, where ŷ is the predicted mean wait in minutes and *x* the number of patients arriving during the shift.
2. *"For each additional patient arriving during a shift, the predicted mean wait increases by about 0.42 minutes."* Equivalently, about 4.2 minutes for every 10 extra patients.
3. *"About 77% of the variation in mean waiting time across these shifts is explained by the linear relationship with the number of patients arriving."*
4. ŷ = 14.51 + 0.4183 × 52 = **36.3** minutes, so the residual is 41 − 36.3 = **+4.7 minutes**. The mean wait on that shift was 4.7 minutes longer than the line predicts for a shift with 52 arrivals: the model underpredicts it.
5. **60 arrivals: 39.6 minutes. 110 arrivals: 60.5 minutes.** Trust the first more: 60 is inside the interval of arrivals used to fit the line, 26 to 77, so it is interpolation. 110 is well beyond 77, an extrapolation, and less reliable; a very busy evening could behave quite differently, for instance if the department runs out of beds.
6. **Yes.** The residuals scatter above and below 0 across the whole range of arrivals with no curve: apparent randomness, which confirms a linear form, so the linear model is appropriate.

**Check for these losses:** "each extra patient **causes** the wait to go up 0.42 minutes", or "adds 0.42 minutes" without *predicted* (item 2); "77% of the patients" or "77% of the shifts" (item 3); a residual of −4.7, or "the model overpredicted" (item 4); giving 60.5 minutes with no comment about extrapolation (item 5); "it's appropriate because *r* = 0.88" (item 6: the residual plot, not *r*, is the evidence).

One more thing, if you have the time. In Session 4, shift 10 was the busy shift with only **4** doctors on duty, and it had the longest wait of the similarly busy shifts. Here it has one of the largest positive residuals. That is a suggestion, not a proof, but it is the kind of question residuals are good at raising.
:::

---

## Part 7 — Explain it back

:::yourturn
Out loud, or in writing, as if to someone who missed the session: *why did the café's r² of 0.92 not make the straight line a good model, and what does a residual plot show that r² cannot?*
:::

:::reveal Reveal — what a good explanation contains
Three things. *r*², like *r*, measures how well a **line** accounts for the variation in the response, and a strong curve can still have a high *r*², so a high *r*² cannot show that the form is linear. The residual plot shows the pattern of the errors: for the café, positive at both ends and negative in the middle, so the line is systematically too low, then too high, then too low again. And the rule: **curvature in the residual plot means the linear model is not the most appropriate; apparent randomness, as for Lincoln High, confirms a linear form.**

If you said *"because 0.92 isn't high enough"*, go back to the café's residual plot in Part 5 and ask yourself what the residuals would look like if the line were right. Tell your tutor at the start of Session 6 if this part did not come out cleanly.
:::

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
