# Session 5 — Multiple-Choice Test

**AP Statistics · Twenty-Hour Course · CED Topics 5.3, 5.4, 5.5**
**20 questions · 35 minutes · calculator allowed**

---

## Before you start

None of the scenarios here is one you worked in Session 5. Lincoln High, the café's iced drinks, St Mary's, Oakfield, the coffee machine, the library and the spring mornings have all been left out. You meet a new regression line and have to read it, rather than remember what the last one said.

The test uses the session's conventions throughout:

- The model is **ŷ = a + bx**, where ŷ is the *predicted* response.
- A **residual is observed minus predicted**, y − ŷ. A positive residual means the model **underpredicts**; a negative residual means it **overpredicts**.
- a and b are given to four significant figures, keeping at least two decimal places. Predictions and residuals are worked from the equation as written.
- *r*² is read from the calculator, not squared from a rounded *r*.

Where you need them, the formula-sheet results are **b = r (s_y ÷ s_x)** and **a = ȳ − b x̄**; the line always passes through (x̄, ȳ).

The CED has six learning objectives for these three topics, so this test has 20 questions.

### What is being tested

| Q | CED objective | Bloom level |
|---|---|---|
| 1 | 5.3.A Predict a response from the line | Application |
| 2 | 5.4.A Calculate a residual | Application |
| 3 | 5.4.B Interpret a negative residual | Analysis |
| 4 | 5.5.B Interpret the slope in context | Application |
| 5 | 5.5.B Interpret the intercept, and judge whether it means anything | **Synthesis** |
| 6 | 5.3.A Extrapolation | Analysis |
| 7 | 5.5.A Interpret *r*² | Application |
| 8 | 5.3.A Interpolation inside a gap in the data | Analysis |
| 9 | 5.4.C A high *r*² and a curved residual plot | **Synthesis** |
| 10 | 5.4.B + 5.4.C Reading over- and underprediction from a residual plot | Analysis |
| 11 | 5.4.C Which residual plot supports a linear model | Analysis |
| 12 | 5.5.A The slope from summary statistics | Application |
| 13 | 5.5.A The intercept from summary statistics | Analysis |
| 14 | 5.5.A The line passes through (x̄, ȳ) | Analysis |
| 15 | 5.5.A What least squares minimises | Analysis |
| 16 | 5.4.A Working back from a residual to the observed value | Analysis |
| 17 | 5.5.A From calculator output to an equation in context | Analysis |
| 18 | 5.5.A *r* from *r*² and the direction | **Synthesis** |
| 19 | 5.5.B The slope is not a measure of strength | **Synthesis** |
| 20 | 5.3.A + 5.4.B + 5.5.A Find the single error | **Synthesis** |

Six questions at synthesis, nine at analysis, five at application. All six learning objectives of Session 5 are tested at least twice.

---
---

# The test

## Questions 1–8 · Taxi fares

> A taxi firm recorded the **distance**, in kilometres, and the **fare**, in pounds, of **14 trips**. No trip in the sample was between 8.0 km and 14.2 km. The least-squares regression line is
>
> **predicted fare = 3.01 + 1.183 × distance**
>
> with *r* = 0.99 and *r*² = 0.99. The shortest trip was 1.2 km and the longest 18.0 km.

![Scatterplot of fare against distance for 14 taxi trips, with the least-squares line](figures/t05-taxi.svg)

*Each point is one trip; the orange line is the least-squares line.*

**1.** What fare does the line predict for a 10 km trip?

- **(A)** £11.83
- **(B)** £4.20
- **(C)** £14.84
- **(D)** £31.28
- **(E)** It cannot be predicted, because no trip in the sample was 10 km

**2.** One trip was **5.6 km** and cost **£11.03**. Its residual is

- **(A)** +£1.39
- **(B)** −£1.39
- **(C)** £9.64
- **(D)** £11.03
- **(E)** +£1.18

**3.** The 18.0 km trip has a residual of **−£0.99**. Which interpretation is correct?

- **(A)** The model underpredicted this fare by £0.99.
- **(B)** The trip was 0.99 km shorter than the line predicted.
- **(C)** Every fare the line predicts is out by about £0.99.
- **(D)** This trip cost £0.99 less than the line predicts for an 18.0 km trip, so the model overpredicted its fare.
- **(E)** The fare for this trip was £0.99.

**4.** Which sentence interprets the **slope** correctly?

- **(A)** Every trip costs £1.183 more than the trip before it.
- **(B)** For each additional kilometre, the predicted fare increases by about £1.18.
- **(C)** Each kilometre costs £3.01.
- **(D)** The predicted fare for a trip of 0 km is £1.18.
- **(E)** About 1.18% of the variation in fare is explained by distance.

**5.** Which is the best interpretation of the **intercept**, 3.01?

- **(A)** Every trip includes a fixed £3.01 charge; the data prove it.
- **(B)** An intercept never has a meaning in context, so it should not be interpreted.
- **(C)** The average fare for the 14 trips is £3.01.
- **(D)** The fare rises by £3.01 for each kilometre.
- **(E)** The predicted fare for a 0 km trip is £3.01. The shortest trip was 1.2 km, so x = 0 lies outside the data and this is an extrapolation. It may reflect a fixed charge, but these data cannot confirm that.

**6.** The firm uses the line to quote **£73.99** for a **60 km** airport trip. The best comment is:

- **(A)** 60 km is far outside the interval of distances used to fit the line, 1.2 to 18.0 km. This is an extrapolation, and the quote is unreliable.
- **(B)** The quote is reliable, because *r*² = 0.99.
- **(C)** The quote is reliable, because the line is linear everywhere.
- **(D)** The quote is an interpolation, because a 60 km taxi trip is realistic.
- **(E)** The quote should have been 60 × 1.183 = £70.98, leaving out the intercept.

**7.** Which sentence interprets *r*² = 0.99 correctly?

- **(A)** 99% of the fares were predicted correctly by the line.
- **(B)** 99% of the points lie on the line.
- **(C)** About 99% of the variation in fare is explained by the linear relationship with distance.
- **(D)** The fare increases by 0.99 of a pound for each kilometre.
- **(E)** Distance causes 99% of the fare.

**8.** The firm predicts the fare for an **11 km** trip, although no trip in the sample was between 8.0 and 14.2 km. This prediction is

- **(A)** an extrapolation, because no trip near 11 km was recorded
- **(B)** an interpolation, because 11 km lies within the interval of distances used to fit the line, 1.2 to 18.0 km
- **(C)** impossible, because the line has no values in the gap
- **(D)** an extrapolation, because 11 is greater than the mean distance
- **(E)** neither, because 11 km is not one of the recorded distances

---

## Questions 9–11 · Residual plots

> A road-safety study measured the **stopping distance**, in metres, of a car braking from **16 different speeds** between 20 and 120 km/h. The least-squares line has *r*² = 0.96. The scatterplot and its residual plot are shown.

![Scatterplot of stopping distance against speed, and its residual plot](figures/t05-braking.svg)

*The residual plot shows each residual, observed minus predicted, against speed.*

**9.** A student writes: *"r² = 0.96, so a linear model is appropriate for stopping distance."* The best response is:

- **(A)** Correct: any *r*² above 0.9 confirms a linear form.
- **(B)** Correct, because the scatterplot rises from left to right.
- **(C)** Incorrect, because *r*² should be exactly 1 before a line is used.
- **(D)** Incorrect. The residual plot shows a clear curve: positive residuals at low and high speeds and negative residuals in the middle. Curvature in the residual plot suggests a linear model is not the most appropriate model, however high *r*² is.
- **(E)** Incorrect, because some residuals are larger than 5 m.

**10.** What does the residual plot say about the line's predictions?

- **(A)** The line underpredicts at every speed, because most residuals are far from 0.
- **(B)** The line is equally accurate at every speed.
- **(C)** At 60 km/h the line underpredicts, and at 120 km/h it overpredicts.
- **(D)** Nothing, because a residual plot shows only the direction of the association.
- **(E)** At 60 km/h the residual is about −5 m, so the line overpredicts the stopping distance there. At 120 km/h it is about +10 m, so the line underpredicts.

**11.** Four regressions produced the residual plots below. Each is plotted against the explanatory variable, with a dashed line at 0.

![Four residual plots labelled A to D](figures/t05-residual-plots.svg)

For which regression does the residual plot support a **linear** model?

- **(A)** A only
- **(B)** B only
- **(C)** A and C, because their points are evenly balanced above and below 0
- **(D)** D only, because its residuals cross 0 several times
- **(E)** All four, because every residual plot has points both above and below 0

---

## Questions 12–14 · Rainfall and wheat

> Over 30 seasons on one farm, **growing-season rainfall** (x, in mm) and **wheat yield** (y, in tonnes per hectare) had these summaries:
>
> x̄ = 420 mm, s_x = 60 mm, ȳ = 7.2 t/ha, s_y = 0.9 t/ha, *r* = 0.75.

**12.** The slope of the least-squares line of yield on rainfall is

- **(A)** 0.01125 t/ha per mm
- **(B)** 50 t/ha per mm
- **(C)** 0.015 t/ha per mm
- **(D)** 0.675 t/ha per mm
- **(E)** 0.00844 t/ha per mm

**13.** The intercept of the least-squares line is

- **(A)** 11.93 t/ha
- **(B)** 7.189 t/ha
- **(C)** 2.475 t/ha
- **(D)** 419.9 t/ha
- **(E)** 4.725 t/ha

**14.** What yield does the line predict for a season with exactly **420 mm** of rain?

- **(A)** 2.475 t/ha
- **(B)** 11.93 t/ha
- **(C)** 5.4 t/ha
- **(D)** 4.725 t/ha
- **(E)** 7.2 t/ha

---

## Questions 15–20 · Separate questions

**15.** The least-squares regression line is the line that

- **(A)** passes through as many of the data points as possible
- **(B)** makes the sum of the residuals as large as possible
- **(C)** minimises the perpendicular distances from the points to the line
- **(D)** minimises the sum of the squares of the residuals
- **(E)** joins the point with the smallest x-value to the point with the largest

**16.** For the taxi line in questions 1–8, a **7.0 km** trip had a residual of **−£1.35**. The line predicts £11.29 for 7.0 km. What was the actual fare?

- **(A)** £12.64
- **(B)** £9.94
- **(C)** £1.35
- **(D)** £11.29
- **(E)** It cannot be found without the scatterplot

**17.** A candle maker records the **height** of a candle, in cm, after it has burned for x **hours**. A TI-84 gives:

```
LinReg
y=a+bx
a=24.07333333
b=-2.351666667
r²=.9991768
r=-.9995883
```

Which equation, written in context, is correct?

- **(A)** predicted height = −2.352 + 24.07 × hours
- **(B)** predicted height = 24.07 − 0.9996 × hours
- **(C)** predicted height = 24.07 − 0.9992 × hours
- **(D)** predicted hours = 24.07 − 2.352 × height
- **(E)** predicted height = 24.07 − 2.352 × hours

**18.** For a school, the least-squares line of **daily gas used for heating** on **outdoor temperature** has a **negative slope** and *r*² = 0.64. The correlation between the two variables is

- **(A)** 0.64
- **(B)** 0.80
- **(C)** −0.80
- **(D)** −0.64
- **(E)** 0.41

**19.** Two regressions are fitted to different data sets. Line P has slope **5.2** and *r*² = **0.30**. Line Q has slope **0.4** and *r*² = **0.95**. Which statement is correct?

- **(A)** Q describes the stronger linear relationship. The slope's size depends on the units of the variables and says nothing about how closely the points follow the line.
- **(B)** P describes the stronger linear relationship, because its slope is 13 times larger.
- **(C)** They are equally strong, because both slopes are positive.
- **(D)** P is stronger, because a steeper line fits the data more closely.
- **(E)** Strength cannot be judged without the intercepts.

**20.** A student writes this report on the taxi line from questions 1–8. **Exactly one** of the five statements is incorrect.

> **I.** The equation is ŷ = 3.01 + 1.183x, where ŷ is the predicted fare in pounds and x is the distance in km.
> **II.** The 5.6 km trip has a positive residual, so the model underpredicted its fare.
> **III.** About 99% of the variation in fare is explained by the linear relationship with distance.
> **IV.** Predicting the fare for a 60 km airport trip is an interpolation, because 60 km is a perfectly reasonable taxi journey.
> **V.** The line passes through the point (x̄, ȳ) = (7.89, 12.34).

Which statement is incorrect?

- **(A)** I
- **(B)** II
- **(C)** III
- **(D)** IV
- **(E)** V

---
---

# Answers and explanations

Each explanation says why the key is right **and what misconception each wrong option represents.** A wrong answer tells you which idea to reteach, and the diagnostic table at the end maps every distractor to a specific gap.

> **Answers are collapsed.** Click a question to open it, or press **`e`** to open every explanation at once. That keeps the key hidden while the test is on a shared screen.

## Answers 1–8 · Taxi fares

<details>
<summary><strong>Question 1</strong></summary>

**Answer: (C)**

ŷ = 3.01 + 1.183 × 10 = 3.01 + 11.83 = **£14.84**.

- **(A)** £11.83 forgets the intercept, using only b × 10.
- **(B)** £4.20 is a + b, the prediction for 1 km, not 10.
- **(D)** £31.28 swaps the coefficients: 3.01 × 10 + 1.183. Read which number multiplies x.
- **(E)** confuses "no observation at 10 km" with "cannot predict". A regression line exists to predict at x-values that were not observed. 10 km is inside the interval of distances used, so this is an interpolation (question 8).

</details>

<details>
<summary><strong>Question 2</strong></summary>

**Answer: (A)**

Predicted: 3.01 + 1.183 × 5.6 = 9.64. Residual = observed − predicted = 11.03 − 9.64 = **+£1.39** (CED 5.4.A.1).

- **(B)** subtracts the wrong way round: predicted − observed. The order is fixed, and it matters, because the sign carries the interpretation (question 3).
- **(C)** is the predicted fare, not the residual.
- **(D)** is the observed fare.
- **(E)** is the slope, rounded. A residual belongs to one individual; the slope belongs to the line.

</details>

<details>
<summary><strong>Question 3</strong></summary>

**Answer: (D)**

A negative residual means the observed value is **below** the predicted one, so the model **overpredicts** (CED 5.4.B.1). A full interpretation gives the size in the response's units, says "less than predicted", and names the individual's x-value. (D) does all three.

- **(A)** reverses the rule. Positive means underprediction; negative means overprediction.
- **(B)** puts the residual on the wrong axis. Residuals are vertical distances in the **response** units, pounds, not kilometres.
- **(C)** applies one trip's residual to the whole line. Each residual belongs to one individual.
- **(E)** confuses the residual with the fare itself.

</details>

<details>
<summary><strong>Question 4</strong></summary>

**Answer: (B)**

CED 5.5.B.2: the slope is the **predicted** increase in the response for a one-unit increase in the explanatory variable, in context. "Predicted" matters: the line describes what it predicts, not what every trip does.

- **(A)** drops "predicted" and turns a model into a rule about consecutive trips. Fares scatter around the line; question 2's trip is £1.39 above it.
- **(C)** confuses the slope with the intercept.
- **(D)** describes the intercept, with the slope's value.
- **(E)** confuses the slope with *r*². They are different numbers with different meanings.

</details>

<details>
<summary><strong>Question 5</strong></summary>

**Answer: (E)**

CED 5.5.B.3: the intercept is the predicted response when x = 0, and it sometimes has no reasonable interpretation. Two tests decide:
- **Is x = 0 inside the data?** No: the shortest trip was 1.2 km, so this is an extrapolation.
- **Is the value possible?** Yes: £3.01 is a plausible starting charge.

So (E) gives the interpretation and its limit.

- **(A)** overclaims. The data are consistent with a fixed charge, but a line fitted from 1.2 km upward cannot *prove* what happens at 0 km.
- **(B)** overcorrects. Many intercepts are meaningful. The judgement is made each time, using the two tests above.
- **(C)** confuses the intercept with the mean fare, which is ȳ = £12.34.
- **(D)** confuses the intercept with the slope.

</details>

<details>
<summary><strong>Question 6</strong></summary>

**Answer: (A)**

CED 5.3.A.3: extrapolation is predicting at an x-value beyond the interval used to fit the line, and it is less reliable the further out it goes. 60 km is more than three times the longest trip in the data. Nothing in these 14 trips says fares keep rising at the same rate: airport trips might have a fixed tariff, a motorway, a waiting charge.

- **(B)** treats *r*² as a guarantee beyond the data. *r*² describes how well the line fits the trips it was fitted to, and says nothing about distances nobody observed.
- **(C)** assumes the pattern continues, which is exactly the assumption extrapolation cannot check.
- **(D)** defines interpolation by whether the x-value is realistic. It is defined by whether x lies within the data's interval (question 8).
- **(E)** drops the intercept. It is also irrelevant: the problem is the extrapolation, not the arithmetic.

</details>

<details>
<summary><strong>Question 7</strong></summary>

**Answer: (C)**

CED 5.5.A.5: *r*² is the proportion of the variation in the response that is explained by the linear relationship with the explanatory variable. (C) is the course's model sentence, in context.

- **(A)** reads *r*² as a success rate. Almost no fare is predicted exactly; every point has a residual.
- **(B)** reads *r*² as a proportion of points on the line.
- **(D)** confuses *r*² with the slope.
- **(E)** reads *r*² as a causal share. It measures variation explained by a linear relationship, not causation (Session 4).

</details>

<details>
<summary><strong>Question 8</strong></summary>

**Answer: (B)**

CED 5.3.A.4: interpolation is predicting at an x-value **within the interval** of x-values used to determine the line. The interval here is 1.2 to 18.0 km, and 11 km is inside it. The gap in the data does not change the definition. The session's own convention says so: a prediction in a gap still counts as interpolation.

- **(A)** redefines extrapolation as "far from any observation". It is "beyond the interval".
- **(C)** confuses the line with the points. The line is defined for every x.
- **(D)** compares with the mean. Extrapolation is about the interval's ends, not its centre.
- **(E)** thinks both words apply only to recorded values. Predicting at a recorded x-value is also an interpolation; the question is where x lies.

It is still worth saying, as a caution, that no trips near 11 km were recorded. But the prediction is an interpolation.

</details>

## Answers 9–11 · Residual plots

<details>
<summary><strong>Question 9</strong></summary>

**Answer: (D)**

CED 5.4.C.4: *curvature in the residual plot for a linear regression model suggests that the linear model is not the most appropriate model.* Here the residuals are positive, then negative, then positive again, a clear U. The scatterplot curves upwards, because stopping distance grows faster than speed, and the straight line cuts across the curve. This is Session 5's café lesson in a new context: a high *r*² does not make a line the right model.

- **(A)** treats *r*² as a test of form. *r*² measures how much variation the line explains; the residual plot tests whether a line is the right shape.
- **(B)** reads direction as form. A curve can rise from left to right too.
- **(C)** sets an impossible standard.
- **(E)** judges by the size of the residuals rather than their **pattern**. Large residuals scattered at random would still support a linear model.

</details>

<details>
<summary><strong>Question 10</strong></summary>

**Answer: (E)**

Read the residual plot with the sign rule (CED 5.4.B.1):
- **At 60 km/h** the residual is −5.1 m. Negative means the observed value is below the line, so the line **overpredicts**.
- **At 120 km/h** the residual is +9.9 m. Positive means the line **underpredicts**.

So the line is wrong in a predictable way at each end and in the middle, which is what curvature means.

- **(A)** ignores the sign. Residuals below 0 are overpredictions.
- **(B)** would need residuals scattered at random with no pattern; these follow a curve.
- **(C)** reverses the sign rule.
- **(D)** confuses a residual plot with a scatterplot. A residual plot shows how far each prediction was from the observation, and in which direction.

</details>

<details>
<summary><strong>Question 11</strong></summary>

**Answer: (B)**

CED 5.4.C.3: *apparent randomness in a residual plot … indicates that the simple linear regression model is an appropriate model.* Only B has no pattern. A is a U, C is an inverted U, and D is an S-shaped wave: all three show curvature.

- **(C)** and **(E)** use a test that every residual plot passes. Least-squares residuals always fall on both sides of 0. What matters is whether they form a **pattern**.
- **(D)** mistakes crossing 0 several times for randomness. D crosses 0 in an orderly wave, rising, falling and rising again. That is a pattern.
- **(A)** picks the most striking plot. A striking pattern is the opposite of what a linear model needs.

</details>

## Answers 12–14 · Rainfall and wheat

<details>
<summary><strong>Question 12</strong></summary>

**Answer: (A)**

From the formula sheet: b = r (s_y ÷ s_x) = 0.75 × (0.9 ÷ 60) = 0.75 × 0.015 = **0.01125** t/ha per mm. Each extra millimetre of rain goes with a predicted 0.01125 t/ha more wheat, or about 1.1 t/ha per extra 100 mm.

- **(B)** 50 inverts the ratio: r (s_x ÷ s_y). The units give it away. The slope is response units per explanatory unit, so s_y goes on top.
- **(C)** 0.015 forgets *r*. It would be the slope only if the correlation were perfect.
- **(D)** 0.675 multiplies r by s_y and forgets to divide by s_x.
- **(E)** 0.00844 uses *r*² instead of *r*.

</details>

<details>
<summary><strong>Question 13</strong></summary>

**Answer: (C)**

a = ȳ − b x̄ = 7.2 − 0.01125 × 420 = 7.2 − 4.725 = **2.475** t/ha.

- **(A)** 11.93 adds instead of subtracting: ȳ + b x̄.
- **(B)** 7.189 subtracts b alone, forgetting to multiply by x̄.
- **(D)** 419.9 swaps the roles of the variables: x̄ − b ȳ.
- **(E)** 4.725 is b x̄, the amount to subtract, not the intercept.

The intercept is also an extrapolation here. No season had 0 mm of rain, so 2.475 t/ha describes nothing the farm has seen (question 5).

</details>

<details>
<summary><strong>Question 14</strong></summary>

**Answer: (E)**

420 mm is x̄, and the least-squares line always passes through (x̄, ȳ) (CED 5.5.A.1). So the prediction is ȳ = **7.2 t/ha** with no calculation needed. Check: 2.475 + 0.01125 × 420 = 2.475 + 4.725 = 7.2.

- **(A)** gives the intercept, the prediction at 0 mm.
- **(B)** comes from the wrong intercept in question 13, option (A).
- **(C)** multiplies ȳ by *r*. That is a half-remembered idea from beyond the course; the line through the means needs no *r* at all.
- **(D)** is b x̄ alone, again forgetting the intercept.

</details>

## Answers 15–20 · Separate questions

<details>
<summary><strong>Question 15</strong></summary>

**Answer: (D)**

CED 5.5.A.1: *the simple linear regression model is fit to the data by minimising the sum of the squares of the residuals.* That is where the name "least squares" comes from. The Least-squares Fitter in Session 5 shows it: every other line you try has a larger Σ(residual²).

- **(A)** A line through the most points need not fit the rest well. With real data the least-squares line may pass through none of the points.
- **(B)** reverses the goal.
- **(C)** uses perpendicular distances. Residuals are **vertical** distances, in the response's units, because the line predicts y from x.
- **(E)** uses only the two extreme points and ignores all the others.

</details>

<details>
<summary><strong>Question 16</strong></summary>

**Answer: (B)**

Residual = observed − predicted, so observed = predicted + residual = 11.29 + (−1.35) = **£9.94**. This is Session 5's Reversing Interpretations activity: from a residual back to the individual.

- **(A)** £12.64 subtracts the residual instead of adding it, which is the sign error again.
- **(C)** confuses the residual with the fare.
- **(D)** is the predicted fare, which the question already gave.
- **(E)** is too cautious. The equation and the residual are enough.

</details>

<details>
<summary><strong>Question 17</strong></summary>

**Answer: (E)**

In LinReg(a+bx), **a is the intercept and b is the slope**. Rounded by the course convention, a = 24.07 and b = −2.352. So: predicted height = 24.07 − 2.352 × hours. The candle starts about 24 cm tall and loses a predicted 2.35 cm for each hour it burns.

- **(A)** swaps a and b. A height that starts at −2.352 cm is the giveaway.
- **(B)** and **(C)** put *r* or *r*² where the slope belongs. Neither is a slope; they measure how well the line fits, not how steep it is (question 19).
- **(D)** swaps the variables. The response is height, which depends on hours burned, so height is predicted.

</details>

<details>
<summary><strong>Question 18</strong></summary>

**Answer: (C)**

*r*² is the square of *r*, so |*r*| = √0.64 = 0.80. The sign of *r* matches the sign of the slope, and the slope is negative: warmer days, less gas. So *r* = **−0.80**.

- **(A)** and **(D)** do not take the square root.
- **(B)** takes the root and drops the sign. √0.64 has two candidates, ±0.80, and the direction of the association picks one.
- **(E)** squares instead of taking the root: 0.64² = 0.41.

</details>

<details>
<summary><strong>Question 19</strong></summary>

**Answer: (A)**

Strength is how closely the points follow the line, and *r*² puts a number on it: 0.95 against 0.30. The slope's size depends on the units. The same data measured in centimetres rather than metres would have a slope 100 times larger and exactly the same *r*² (Session 4: *r* is unit-free). This is Session 4's "strength is not steepness", now for the fitted line.

- **(B)** and **(D)** read steepness as strength.
- **(C)** reads the sign of the slope as strength. The sign gives the direction only.
- **(E)** is wrong: intercepts say nothing about strength, and *r*² answers the question directly.

</details>

<details>
<summary><strong>Question 20</strong></summary>

**Answer: (D)**

Statement IV confuses interpolation with a realistic prediction. The two words are defined by the **interval** of x-values used to fit the line (CED 5.3.A.3–4), not by whether the x-value makes sense in the real world. 60 km is far beyond 18.0 km, so it is an extrapolation (question 6).

- **(A)** I is correct, with both symbols defined in context.
- **(B)** II is correct: question 2's residual is +£1.39, and positive means underprediction.
- **(C)** III is correct: it is the model *r*² sentence (question 7).
- **(E)** V is correct. The 14 trips have mean distance 7.89 km and mean fare £12.34, and the line passes through the point of means (CED 5.5.A.1).

</details>

---
---

# Marking and diagnosis

## Score

One mark per question. **Total 20.**

| Score | Reading |
|---|---|
| 17–20 | Session 5 is secure. Block B is complete; move to Session 6. |
| 13–16 | Solid. Reteach only the specific items missed, using the table below. |
| 9–12 | The arithmetic works, but the interpretations are not yet reliable. Re-run the Reversing Interpretations activity and Scenario B before moving on. |
| 0–8 | Reteach Session 5. Its slope, intercept and residual sentences return in every free-response question on regression, and the prediction habit matters in Block D. |

## What each miss points to

| Missed | The gap | Theory to reread | Where it is applied |
|---|---|---|---|
| 1, 14 | Using ŷ = a + bx, and the line through (x̄, ȳ) | *The linear regression model and the predicted value ŷ (5.3.A.1–2)* | *Predicting a journey: 12 km, and a student 45 km away (5.3.A)* and *Checking the line: the point of means and the formula sheet* |
| 2, 16 | Residual = observed − predicted, forwards and backwards | *Residuals: observed minus predicted (5.4.A.1)* | *The 33-minute student's residual (5.4.A–B)* and *Round 1: from a residual back to the student* |
| 3, 10 | The sign rule: positive underpredicts, negative overpredicts | *What the sign of a residual says (5.4.B.1)* | *Round 2: judging four written interpretations* |
| 4, 19 | The slope sentence with "predicted", and slope is not strength | *Interpreting the slope (5.5.B.1–2)* | *What the slope and intercept say about the journeys (5.5.B)* |
| 5 | When the intercept means nothing | *Interpreting the y-intercept, and when it means nothing (5.5.B.3)* | *What the slope and intercept say about the journeys (5.5.B)* |
| 6, 8, 20 | Interpolation and extrapolation are defined by the interval of x | *Interpolation and extrapolation (5.3.A.3–4)* | *Predicting a journey: 12 km, and a student 45 km away (5.3.A)* |
| 7, 18 | What *r*² means, and its link to *r* | *The coefficient of determination r² (5.5.A.5)* | *How much of the variation distance explains (5.5.A.5)* |
| 9, 11 | Residual plots: randomness supports a line, curvature does not | *Reading a residual plot: randomness or curvature (5.4.C.3–4)* | *The iced drinks' residual plot* and *The journeys' residual plot (5.4.C)* |
| 12, 13, 17 | Finding a and b: the formula sheet and the calculator | *Finding a and b: technology, or the formula sheet (5.5.A.2–4)* | *From calculator output to an equation in context (5.5.A)* |
| 15 | What least squares minimises | *Least squares: the line that minimises Σ(residual²) (5.5.A.1)* | *Least-squares Fitter* |

> **Three misses worth treating as urgent.** **Question 3 or 10**, the residual sign rule, is the most common regression error on free-response questions, and it costs the interpretation mark every time. **Question 9**, trusting *r*² over the residual plot, is Session 4's lesson about *r* returning in a new form; a student who misses it will fit lines to curves on the exam. **Question 6 or 20**, extrapolation, is examined almost every year, and the arithmetic gives no warning.

---

*CED references: Topic 5.3 (5.3.A.1–4), Topic 5.4 (5.4.A.1, 5.4.B.1, 5.4.C.1–4), Topic 5.5 (5.5.A.1–5, 5.5.B.1–3). Course and Exam Description effective Fall 2026; exam reference information (formula sheet) 2026.*

*All numbers in this test were computed and verified by script. That covers the taxi line, fitted from the 14 plotted trips, with every prediction, residual and the point of means; the braking regression and its residuals; the four residual plots, each a genuine least-squares residual plot with mean 0 and no correlation with x; the formula-sheet slope and intercept; the candle output; and each distractor, recomputed from the error it represents.*
