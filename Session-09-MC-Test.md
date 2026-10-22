# Session 9 — Multiple-Choice Test

**AP Statistics · Twenty-Hour Course · CED Topics 2.4, 2.5**
**16 questions · 30 minutes · no calculator needed**

---

## Before you start

Every question is set in a scenario, and none can be answered by reciting a definition. You apply a rule to a situation, find what is wrong with a claim, or put two rules together.

**Why this test is shorter than the last three.** Sessions 6, 7 and 8 each had twenty questions because each covered sixteen to eighteen pieces of required content. Topics 2.4 and 2.5 have **two learning objectives and six essential-knowledge statements** between them, so sixteen questions test every one of them at least twice. Length follows content; it is not a judgement about difficulty.

**What is not here.** Conditional probability, independence, the general multiplication rule and the union formula P(A ∪ B) = P(A) + P(B) − P(A ∩ B) are **Session 10** (CED 2.6–2.7). No question needs them, and one question is wrong precisely because a candidate reaches for one of them early.

### What is being tested

| Q | CED objective | Bloom level |
|---|---|---|
| 1 | 2.4.A.2 Theoretical probability, equally likely outcomes | Application |
| 2 | 2.5.A.1 Joint probability from a table | Application |
| 3 | 2.5.A.2 Identifying a mutually exclusive pair | Analysis |
| 4 | 2.5.A Justifying mutual exclusivity (Skill 4.B) | Analysis |
| 5 | 2.4.A.4 Complement of an event | Application |
| 6 | 2.4.A.2 Counting a compound event without the union formula | **Synthesis** |
| 7 | 2.4.A.1 Sample space: non-overlapping outcomes | Analysis |
| 8 | 2.4.A.2 When outcomes are *not* equally likely | Analysis |
| 9 | 2.4.A.1, 2.4.A.3 Reading a total above 1 | **Synthesis** |
| 10 | 2.4.A.4 Complement of a compound event | Application |
| 11 | 2.5.A.2 Mutual exclusivity within one variable | Analysis |
| 12 | 2.4.A.4 "At least" by complement | Application |
| 13 | 2.4.A.4 "At least" over several bands | Analysis |
| 14 | 2.4.A.3 The 0-to-1 bound as a check | **Synthesis** |
| 15 | 2.4.A.4, 2.5.A.2 Mutually exclusive versus complementary | **Synthesis** |
| 16 | 2.5.A Structure of a complete justification | **Synthesis** |

Five questions at synthesis, six at analysis, five at application. Every essential-knowledge statement is tested at least twice.

---
---

# The test

## Questions 1–6 · The theatre's ticket records

> A theatre recorded all **800 tickets** sold for one performance, by seating level and ticket type.
>
> | | Full price | Concession | Total |
> |---|---|---|---|
> | Stalls | 240 | 160 | **400** |
> | Circle | 180 | 60 | **240** |
> | Balcony | 80 | 80 | **160** |
> | **Total** | **500** | **300** | **800** |
>
> One of the 800 tickets is chosen at random, so every ticket is equally likely.

**1.** The probability that the chosen ticket is for the Stalls is

- **(A)** 0.200
- **(B)** 0.375
- **(C)** 0.500
- **(D)** 0.625
- **(E)** 0.875

**2.** The probability that the chosen ticket is for the Stalls **and** is a concession is

- **(A)** 0.400
- **(B)** 0.533
- **(C)** 0.188
- **(D)** 0.875
- **(E)** 0.200

**3.** Which of these pairs of events is **mutually exclusive** for the chosen ticket?

- **(A)** "Stalls" and "concession"
- **(B)** "Stalls" and "Circle"
- **(C)** "Balcony" and "full price"
- **(D)** "Circle" and "concession"
- **(E)** None of these pairs, because every cell of the table contains at least one ticket

**4.** The box-office manager writes: *"A seating level and a ticket type are different things, so 'Stalls' and 'concession' are mutually exclusive."* Which response is best?

- **(A)** The claim is wrong: 160 tickets are both, so P(Stalls ∩ concession) = 0.200, which is not 0.
- **(B)** The claim is right: a ticket's level and its type are recorded separately.
- **(C)** The claim is wrong, because mutually exclusive events must come from the same variable.
- **(D)** The claim cannot be assessed without knowing how many people attended.
- **(E)** The claim is right, because 0.500 × 0.375 = 0.188, which is not 0.200.

**5.** The probability that the chosen ticket is **not** for the Stalls is

- **(A)** 0.200
- **(B)** 0.375
- **(C)** 0.625
- **(D)** 0.500
- **(E)** 0.800

**6.** The theatre wants the probability that the chosen ticket is **for the Stalls or is a concession, or both**. Using only what this session covers, the correct value is

- **(A)** 0.875
- **(B)** 0.675
- **(C)** 0.200
- **(D)** 0.188
- **(E)** It cannot be found without the union formula.

---

## Questions 7–11 · The driving test centre

> A driving test centre has records of **600 booked tests**. Of those, **372 candidates passed**, **198 failed**, and **30 did not attend**. Of the 372 who passed, **95 passed with no minor faults recorded**.
>
> A receptionist writes this list on a whiteboard and calls it "the four things that can happen":
>
> **passed · passed with no faults · failed · did not attend**

**7.** The receptionist's list is **not** a sample space for one booked test because

- **(A)** it has four entries rather than three.
- **(B)** "did not attend" is not really an outcome of a driving test.
- **(C)** the four entries do not have equal probabilities.
- **(D)** 600 is too small a number of records.
- **(E)** the entries overlap: every candidate who passed with no faults is already counted in "passed".

**8.** An administrator reports: *"There are four outcomes on the list, so the probability a booked test is not attended is 1 ÷ 4 = 0.250."* The correct probability, and the fault in the reasoning, are

- **(A)** 0.250; the reasoning is sound.
- **(B)** 0.158; the administrator used the wrong row of the records.
- **(C)** 0.050; counting outcomes only gives a probability when the outcomes are equally likely, and these are not.
- **(D)** 0.050; the reasoning is sound but the arithmetic is wrong.
- **(E)** 0.380; the administrator should have used the complement.

**9.** Adding the proportions for all four entries on the whiteboard gives **1.158**. This total tells you that

- **(A)** a probability has been rounded badly.
- **(B)** the records contain 1,158 tests rather than 600.
- **(C)** the four events are mutually exclusive.
- **(D)** the entries overlap, because the proportions of a genuine sample space add to exactly 1.
- **(E)** the four events are equally likely after all.

**10.** For one booked test chosen at random, the probability that the candidate **did not pass** is

- **(A)** 0.380
- **(B)** 0.330
- **(C)** 0.050
- **(D)** 0.620
- **(E)** 0.255

**11.** For one booked test, the events "passed" and "did not attend" are

- **(A)** not mutually exclusive, because both appear in the same set of records.
- **(B)** mutually exclusive, because a single booked test cannot be both, so the joint probability is 0.
- **(C)** mutually exclusive, because together they account for every booked test.
- **(D)** complementary, because one must happen if the other does not.
- **(E)** impossible to classify without knowing how many candidates re-booked.

---

## Questions 12–14 · The bike-share scheme

> A city bike-share scheme logged **2,000 trips** in one week, by duration.
>
> | Duration | Trips |
> |---|---|
> | Under 10 minutes | 1,280 |
> | 10 to under 20 minutes | 480 |
> | 20 to under 30 minutes | 160 |
> | 30 minutes or more | 80 |
> | **Total** | **2,000** |
>
> One of the 2,000 trips is chosen at random.

**12.** The probability that the chosen trip lasted **at least 10 minutes** is

- **(A)** 0.240
- **(B)** 0.320
- **(C)** 0.640
- **(D)** 0.120
- **(E)** 0.360

**13.** The probability that the chosen trip lasted **at least 20 minutes** is

- **(A)** 0.080
- **(B)** 0.880
- **(C)** 0.120
- **(D)** 0.040
- **(E)** 0.360

**14.** A report claims the probability that a trip lasted **under 10 minutes or at least 30 minutes** is 0.640 + 0.040 + 0.400 = **1.080**. Without checking any of the arithmetic, you can say the claim is wrong because

- **(A)** probabilities must be given to three decimal places.
- **(B)** the two events are mutually exclusive, so their probabilities cannot be added.
- **(C)** the duration bands do not overlap.
- **(D)** no probability can be greater than 1.
- **(E)** the trips were not chosen at random.

---

## Questions 15–16 · Two more

**15.** For one randomly chosen individual, events *A* and *B* are **complementary**. Which statement is true?

- **(A)** *A* and *B* are mutually exclusive, and P(*A*) + P(*B*) = 1.
- **(B)** *A* and *B* are mutually exclusive, but P(*A*) + P(*B*) may be less than 1.
- **(C)** *A* and *B* need not be mutually exclusive.
- **(D)** P(*A* ∩ *B*) = P(*A*) × P(*B*).
- **(E)** *A* and *B* are independent.

**16.** An exam question asks a student to **justify** whether two events are mutually exclusive. Which answer would earn full credit?

- **(A)** "They are mutually exclusive because they describe different categories."
- **(B)** "Let *A* be 'the ticket is for the Stalls' and *B* 'the ticket is a concession'. P(*A* ∩ *B*) = 160 ÷ 800 = 0.200. Because this is not 0, *A* and *B* are not mutually exclusive."
- **(C)** "P(*A* ∩ *B*) = 0.200."
- **(D)** "They are not mutually exclusive."
- **(E)** "They are not mutually exclusive because the two events are independent."

---
---

# Answers and explanations

Each explanation says why the key is right **and what each wrong option reveals.**

> **Answers are collapsed.** Click a question to open it, or press **`e`** to open every explanation at once — useful when the test is on a shared screen.

## Answers 1–6 · The theatre's ticket records

<details>
<summary><strong>Question 1</strong></summary>

**Answer: (C)**

400 of the 800 tickets are Stalls tickets, and every ticket is equally likely, so P(Stalls) = 400 ÷ 800 = **0.500**. The denominator is the sample space — all 800 tickets.

- **(A)** 0.200 is the Stalls-and-concession cell, 160 ÷ 800: one cell rather than the whole row.
- **(B)** 0.375 is P(concession), 300 ÷ 800 — the wrong margin.
- **(D)** 0.625 is 500 ÷ 800, the full-price column.
- **(E)** 0.875 adds P(Stalls) and P(concession) without removing the overlap. See question 6.

</details>

<details>
<summary><strong>Question 2</strong></summary>

**Answer: (E)**

"Stalls **and** concession" is the intersection, and its probability is the **joint** probability: the cell where the row and the column meet, over the table total. 160 ÷ 800 = **0.200**.

- **(A)** 0.400 is 160 ÷ 400 — the cell over its **row** total. That is a conditional relative frequency (Session 8) and a conditional probability (Session 10): the probability a ticket is a concession *given* it is Stalls. A different question.
- **(B)** 0.533 is 160 ÷ 300, the cell over its **column** total — conditioning the other way.
- **(C)** 0.188 is 0.500 × 0.375. Multiplying marginal probabilities assumes independence, which is Session 10 and is not established here. It also happens to be wrong: the true joint probability is 0.200.
- **(D)** 0.875 is the sum of the two margins.

</details>

<details>
<summary><strong>Question 3</strong></summary>

**Answer: (B)**

One ticket has exactly one seating level, so "Stalls" and "Circle" cannot both happen: P(Stalls ∩ Circle) = **0**. Two levels of the **same variable** are always mutually exclusive.

- **(A)**, **(C)** and **(D)** each pair a level with a ticket type — two **different** variables — and in every case the cell where they meet is non-empty: 160, 80 and 60 tickets respectively. None is mutually exclusive.
- **(E)** correctly observes that no cell is empty, then draws the wrong conclusion. A non-empty table rules out mutually exclusive pairs *across* the two variables; it says nothing about two levels of the same variable, which is where the answer is.

</details>

<details>
<summary><strong>Question 4</strong></summary>

**Answer: (A)**

The objective is a **justification** one (2.5.A, Skill 4.B), so the answer has to produce the joint probability. 160 tickets are in both events, so P(Stalls ∩ concession) = 160 ÷ 800 = 0.200, which is not 0. The claim fails.

- **(B)** repeats the manager's error. How a theatre records two variables has no bearing on whether one ticket can have both values.
- **(C)** reaches the right verdict by a false rule. Mutually exclusive events are **not** required to come from the same variable — two events from different variables are mutually exclusive whenever the cell where they meet is empty. Right answer, wrong reason, no credit.
- **(D)** confuses tickets with people. The sample space is the 800 tickets, which is what was sampled.
- **(E)** multiplies the margins, which is an independence calculation (Session 10), and then uses it to support the wrong verdict.

</details>

<details>
<summary><strong>Question 5</strong></summary>

**Answer: (D)**

P(not Stalls) = 1 − P(Stalls) = 1 − 0.500 = **0.500**. Counting gives the same: (240 + 160) Circle and Balcony tickets is 400, and 400 ÷ 800 = 0.500. Both routes must agree, which is the check worth doing.

- **(A)** 0.200 is the Stalls-and-concession cell.
- **(B)** 0.375 is P(concession).
- **(C)** 0.625 is the complement of 0.375 — the complement of the **wrong event**.
- **(E)** 0.800 divides by 1,000, or mis-reads 160 ÷ 200.

</details>

<details>
<summary><strong>Question 6</strong></summary>

**Answer: (B)**

Count the tickets in the event. "Stalls or concession, or both" covers Stalls full price (240), Stalls concession (160), Circle concession (60) and Balcony concession (80): **540** tickets. So the probability is 540 ÷ 800 = **0.675**.

- **(A)** 0.875 adds P(Stalls) = 0.500 and P(concession) = 0.375. The 160 tickets that are both get counted twice, which is exactly the overlap the union formula exists to remove.
- **(C)** 0.200 is only the overlap.
- **(D)** 0.188 multiplies the margins.
- **(E)** is the instructive one. The union formula P(A ∪ B) = P(A) + P(B) − P(A ∩ B) is **2.7.A.3, Session 10**, and you do not have it yet. You do not need it: when the outcomes are equally likely you can always count the outcomes in the event directly. "I have not been taught the formula" is not the same as "it cannot be done."

</details>

## Answers 7–11 · The driving test centre

<details>
<summary><strong>Question 7</strong></summary>

**Answer: (E)**

A sample space is the set of all possible **non-overlapping** outcomes (2.4.A.1). "Passed with no faults" is a *subset* of "passed", so the 95 appear twice. The list is not a sample space, whatever its probabilities.

- **(A)** the number of entries is irrelevant; sample spaces come in all sizes.
- **(B)** "did not attend" is a perfectly good outcome of a booked test — it is one of the three that do form the sample space.
- **(C)** is true but is not the fault being asked about. Unequal probabilities are fine; a sample space never has to be equally likely. Overlap is fatal; inequality is not.
- **(D)** 600 records is ample, and sample-space membership does not depend on how many were observed.

</details>

<details>
<summary><strong>Question 8</strong></summary>

**Answer: (C)**

30 of the 600 tests were not attended, so the probability is 30 ÷ 600 = **0.050**. Counting outcomes and dividing — the administrator's method — only gives a probability when **all outcomes in the sample space are equally likely** (2.4.A.2), and passing, failing and not attending plainly are not.

- **(A)** repeats the error. "Four outcomes" also uses a list that is not a sample space at all (question 7).
- **(B)** 0.158 is 95 ÷ 600, the no-faults group.
- **(D)** gives the right number with the wrong diagnosis: the arithmetic 1 ÷ 4 is correct arithmetic, and the *method* is what fails.
- **(E)** 0.380 is P(did not pass), answering a different question.

</details>

<details>
<summary><strong>Question 9</strong></summary>

**Answer: (D)**

The probabilities of a sample space add to exactly 1 (2.4.A.1). A total above 1 means something has been counted twice — here the 95 no-faults passes, inside the 372 passes. The genuine sample space is passed, failed, did not attend: 0.620 + 0.330 + 0.050 = 1.000 exactly.

- **(A)** rounding moves a third decimal place, not 0.158.
- **(B)** the records contain 600 tests; the inflated total comes from double counting, not from more data.
- **(C)** has it backwards. Mutually exclusive events are exactly what these are **not** — a total above 1 is the signature of overlap.
- **(E)** equal likelihood is a separate question, and nothing here supports it.

</details>

<details>
<summary><strong>Question 10</strong></summary>

**Answer: (A)**

"Did not pass" is the complement of "passed", so P = 1 − 0.620 = **0.380**. Counting agrees: (198 + 30) ÷ 600 = 228 ÷ 600 = 0.380. Note that the complement of "passed" includes those who did not attend — a candidate who never arrived did not pass.

- **(B)** 0.330 is P(failed), which leaves out the 30 who did not attend. This is the common error: treating "did not pass" as "failed".
- **(C)** 0.050 is P(did not attend) alone.
- **(D)** 0.620 is P(passed) — the event itself rather than its complement.
- **(E)** 0.255 is 95 ÷ 372, a conditional probability from Session 10.

</details>

<details>
<summary><strong>Question 11</strong></summary>

**Answer: (B)**

One booked test cannot both be passed and not attended, so P(passed ∩ did not attend) = 0 and the events are mutually exclusive.

- **(A)** confuses appearing in the same data set with being able to occur together. Every event in this scenario comes from the same records.
- **(C)** gives the right verdict with a false reason, and the reason is itself untrue: passed and did not attend leave out the 198 who failed, so they do not account for every test.
- **(D)** is the trap worth noticing. **Complementary is stronger than mutually exclusive**: these two cannot both happen, but they can both *fail* to happen — a candidate who failed is neither. Their probabilities are 0.620 and 0.050, which sum to 0.670, not 1.
- **(E)** re-booking does not change what can happen on one booked test.

</details>

## Answers 12–14 · The bike-share scheme

<details>
<summary><strong>Question 12</strong></summary>

**Answer: (E)**

"At least 10 minutes" is the complement of "under 10 minutes", so P = 1 − (1,280 ÷ 2,000) = 1 − 0.640 = **0.360**. Counting the other three bands agrees: (480 + 160 + 80) ÷ 2,000 = 720 ÷ 2,000 = 0.360.

- **(A)** 0.240 is 480 ÷ 2,000, the 10-to-20 band alone.
- **(B)** 0.320 is (480 + 160) ÷ 2,000 — the commonest slip here, dropping the "30 or more" band from the complement.
- **(C)** 0.640 is P(under 10), the event itself.
- **(D)** 0.120 is P(at least 20), which is question 13.

</details>

<details>
<summary><strong>Question 13</strong></summary>

**Answer: (C)**

Two bands are at least 20 minutes: 160 and 80. So P = (160 + 80) ÷ 2,000 = 240 ÷ 2,000 = **0.120**.

- **(A)** 0.080 is 160 ÷ 2,000 — the 20-to-30 band only, forgetting that "at least 20" includes everything above.
- **(B)** 0.880 is the complement, P(under 20). Right calculation, wrong event.
- **(D)** 0.040 is 80 ÷ 2,000, the 30-or-more band alone.
- **(E)** 0.360 is question 12's answer.

</details>

<details>
<summary><strong>Question 14</strong></summary>

**Answer: (D)**

The probability of an event is a number between 0 and 1, inclusive (2.4.A.3). 1.080 is outside that range, so the claim is wrong — and you know it **before** examining the arithmetic. That is what the bound is for: a cheap check that catches a whole class of errors.

*(The actual fault, for interest: the third term of 0.400 does not correspond to any event, and the two named bands give 0.640 + 0.040 = 0.680.)*

- **(A)** three decimal places is this course's reporting convention, not a rule about validity. 1.080 already has three.
- **(B)** reverses the rule. Mutually exclusive events are exactly the ones whose probabilities **may** safely be added — that is why the overlap term is zero.
- **(C)** is true, and is the reason the two named bands *could* be added. It gives no reason to reject the claim.
- **(E)** the trips were chosen at random; nothing in the scenario suggests otherwise.

</details>

## Answers 15–16 · Two more

<details>
<summary><strong>Question 15</strong></summary>

**Answer: (A)**

Complementary events are mutually exclusive **and more besides**. *B* is "not *A*", so they cannot both happen — P(*A* ∩ *B*) = 0 — and one of them must happen, so P(*A*) + P(*B*) = 1. Both halves are needed.

- **(B)** describes **mutually exclusive but not complementary** — true of "passed" and "did not attend" in question 11, whose probabilities sum to 0.670. It is the correct statement about a different relationship.
- **(C)** is false: complementary events are always mutually exclusive.
- **(D)** applies a multiplication rule that is Session 10, and it is false here anyway: P(*A* ∩ *B*) = 0, while P(*A*) × P(*B*) is 0 only if one of the events is impossible.
- **(E)** confuses the two ideas the session keeps apart. Complementary events with non-zero probabilities are about as far from independent as events get — knowing *A* happened tells you *B* certainly did not.

</details>

<details>
<summary><strong>Question 16</strong></summary>

**Answer: (B)**

Objective 2.5.A is a justification objective assessed on **Skill 4.B**, and a complete justification has three parts: **name both events in context**, **give the joint probability as a number**, and **say what that number shows**. Option (B) does all three.

- **(A)** is a verdict with a false reason — "different categories" is the error the whole session is built around.
- **(C)** gives the number without naming the events or stating the conclusion. On an analytic scale this is partial credit, not full.
- **(D)** is the right verdict with no evidence at all. A verdict alone scores nothing.
- **(E)** supplies a reason that is both off-syllabus for this session and logically unrelated: independence does not determine mutual exclusivity, and in fact two events with non-zero probabilities cannot be both.

</details>

---
---

# Marking and diagnosis

## Score

One mark per question. **Total 16.**

| Score | Reading |
|---|---|
| 14–16 | Secure. Session 10 can build conditional probability straight on top. |
| 11–13 | Sound. Reteach only the items missed, using the table below. |
| 8–10 | The rules are there but not yet doing work. Re-run Scenario A before Session 10. |
| 0–7 | Reteach Session 9. Session 10 puts independence on exactly this ground, and it will not hold. |

## What each miss points to

Each row names the **theory to reread** and **where it is applied**, in the order the session teaches them.

| Missed | Theory to reread | Where it is applied |
|---|---|---|
| 1, 8 | Theoretical probability when every outcome is equally likely (2.4.A.2) · When the outcomes are not equally likely (2.4.A.2) | The register as a sample space of 1,842 students · "Four outcomes, so one chance in four" |
| 2 | Joint probability: the intersection of two events (2.5.A.1) | Probabilities for bus, Villages, and the cell where they meet |
| 3, 11 | Mutually exclusive, or disjoint, events (2.5.A.2) | Which pairs at Lincoln High really are mutually exclusive |
| 4, 16 | Justifying that two events are mutually exclusive (2.5.A, Skill 4.B) | The travel officer's "different groups, so they cannot both happen" |
| 5, 10, 12, 13 | The complement of an event, and the three ways to write it (2.4.A.4) · Complements of compound events: "none", "at least one" and "more than" (2.4.A.4) | Complements of the register's events · Attended, and its complement |
| 6 | Probabilities read off a two-way table (2.4.A.2, 2.5.A.1) | The sentence the office may write |
| 7, 9 | The sample space, and why its outcomes must not overlap (2.4.A.1) | The receptionist's overlapping list |
| 14 | Probability is a number from 0 to 1, inclusive (2.4.A.3) | A thousand appointment records, sorted into four outcomes |
| 15 | Complementary events are mutually exclusive, and more besides (2.4.A.4, 2.5.A.2) · What mutually exclusive does not mean (2.5.A.2) | First appointments and follow-ups: a joint probability that is not zero |

> **The two misses to treat as urgent.** **Question 4 or 16** — a justification without the joint probability is the single most expensive habit in topic 2.5, and the exam marks the number, not the verdict. **Question 15** — mutually exclusive, complementary and independent are three different relationships, and Session 10 adds the third next week on top of the first two.

---

*CED references: Topic 2.4 (2.4.A.1–4), Topic 2.5 (2.5.A.1–2). Course and Exam Description effective Fall 2026.*

*Every number in this test was computed and checked by script: all three tables sum to their stated totals, every probability is exact to 3 decimal places, every sample space sums to 1.000, and each distractor was recomputed from the specific error it represents so that none can coincide with its key.*
