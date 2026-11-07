# Session 10 — Multiple-Choice Test

**AP Statistics · Twenty-Hour Course · CED Topics 2.6, 2.7**
**18 questions · 35 minutes · a calculator is permitted but every number divides exactly**

---

## Before you start

Every question is set in a scenario, and none can be answered by reciting a formula. You choose a denominator, apply a rule to a situation, find what is wrong with a claim, or put two rules together.

**Why eighteen questions.** Topics 2.6 and 2.7 have **two learning objectives and five essential-knowledge statements**, but four of the five are formulas and the pair carries the one confusion in Unit 2 that survives to the exam. Eighteen questions test every statement at least twice and the two that are most often misapplied — the denominator of a conditional probability, and independence — six and seven times.

**The habit this test is built to catch.** Almost every wrong answer below is a real error with a name: a cell divided by the wrong total, a conditional read backwards, the product form used where independence was never established, a union found by adding. Each explanation names the error rather than only correcting the arithmetic.

**What is not here.** No question needs Bayes' theorem, a Venn diagram or a tree diagram; none of the three is in the course description, and no rule converts P(A | B) into P(B | A). Where a conditional has to be reversed, you reverse it by going back to the table.

### What is being tested

| Q | CED objective | Bloom level |
|---|---|---|
| 1 | 2.6.A.1 Conditional probability: cell over row total | Application |
| 2 | 2.6.A.1 Conditioning the other way: cell over column total | Application |
| 3 | 2.6.A.1 P(A \| B) read as P(B \| A) | Analysis |
| 4 | 2.6.A.1, 2.5.A.1 Joint against conditional, same cell | Analysis |
| 5 | 2.6.A.2 The general multiplication rule | Application |
| 6 | 2.7.A.1 Testing independence from a table | Analysis |
| 7 | 2.7.A.3, 2.7.A.2 The probability of a union | **Synthesis** |
| 8 | 2.7.A.1 Independence as an exact comparison | Analysis |
| 9 | 2.6.A.1, 2.7.A.1 Independence runs both ways | **Synthesis** |
| 10 | 2.6.A.2, 2.7.A.1 When the product form is legitimate | **Synthesis** |
| 11 | 2.7.A.3 A union whose events overlap heavily | Application |
| 12 | 2.7.A.1 Independent read as mutually exclusive | Analysis |
| 13 | 2.6.A.2 Without replacement: the second denominator | Application |
| 14 | 2.6.A.1 Two draws by the general rule | Application |
| 15 | 2.7.A.1 The product form where it does not apply | Analysis |
| 16 | 2.6.A.2 "At least one" through its complement | **Synthesis** |
| 17 | 2.7.A.1 Why no non-zero pair is both | **Synthesis** |
| 18 | 2.7.A.2, 2.7.A.3 Which rule the question asks for | **Synthesis** |

Six questions at synthesis, six at analysis, six at application. Every essential-knowledge statement is tested at least twice.

---
---

# The test

## Questions 1–7 · The city museum's visitor records

> A city museum recorded all **1,200 visitors** on one Saturday, by ticket holding and whether the visitor joined a guided tour.
>
> | | Guided tour | No tour | Total |
> |---|---|---|---|
> | Member | 180 | 300 | **480** |
> | Non-member | 120 | 600 | **720** |
> | **Total** | **300** | **900** | **1,200** |
>
> One of the 1,200 visitors is chosen at random, so every visitor is equally likely.

**1.** The probability that the chosen visitor joined a guided tour, **given that the visitor is a member**, is

- **(A)** 0.150
- **(B)** 0.600
- **(C)** 0.250
- **(D)** 0.375
- **(E)** 0.625

**2.** The probability that the chosen visitor is a member, **given that the visitor joined a guided tour**, is

- **(A)** 0.375
- **(B)** 0.600
- **(C)** 0.150
- **(D)** 0.250
- **(E)** 0.400

**3.** The museum's press office writes: *"Our figures show that 0.600 of the museum's members joined a guided tour."* Which response is best?

- **(A)** The claim is right: 180 of the tour group are members, and 180 ÷ 300 = 0.600.
- **(B)** The claim is right, but it should be written as a percentage.
- **(C)** The claim is wrong: the correct figure is 0.150, the proportion of all visitors who were members on a tour.
- **(D)** The claim cannot be assessed, because the table does not record how many members the museum has in total.
- **(E)** The claim is wrong: 0.600 is the probability a **tour-goer is a member**. The proportion of **members** who joined a tour is 180 ÷ 480 = 0.375.

**4.** Three visitors each quote a different number for the same cell of the table: 0.150, 0.375 and 0.600. The number that answers *"what is the probability the chosen visitor is a member **and** joined a guided tour?"* is

- **(A)** 0.150, because the denominator is all 1,200 visitors.
- **(B)** 0.375, because the denominator is the 480 members.
- **(C)** 0.600, because the denominator is the 300 tour-goers.
- **(D)** Any of the three: all are probabilities of the 180 visitors in that cell.
- **(E)** None of the three, because an "and" probability requires the multiplication rule rather than the table.

**5.** Using the **general multiplication rule**, P(member ∩ tour) is

- **(A)** 0.400 × 0.250 = 0.100
- **(B)** 0.400 + 0.375 − 0.150 = 0.625
- **(C)** 0.400 × 0.375 = 0.150
- **(D)** 0.250 × 0.600 = 0.150, which is the only correct route
- **(E)** 0.375 × 0.600 = 0.225

**6.** Is joining a guided tour **independent** of being a member?

- **(A)** Yes: 180 visitors are both, so the two events can occur together.
- **(B)** Yes, approximately: 0.375 and 0.250 are close enough to treat as equal.
- **(C)** No: the events are mutually exclusive, and mutually exclusive events are never independent.
- **(D)** No: P(tour | member) = 0.375 but P(tour) = 0.250, so knowing a visitor is a member changes the probability.
- **(E)** It cannot be decided from a table; independence is a property of the population, not the sample.

**7.** The museum wants the probability that the chosen visitor **is a member or joined a guided tour, or both**. That probability is

- **(A)** 0.650
- **(B)** 0.500
- **(C)** 0.150
- **(D)** 0.350
- **(E)** 0.100

---

## Questions 8–12 · The language school's enrolments

> A language school recorded all **800 enrolments** in one year, by class time and whether the student achieved the end-of-course certificate.
>
> | | Certificate | No certificate | Total |
> |---|---|---|---|
> | Evening class | 180 | 60 | **240** |
> | Daytime class | 420 | 140 | **560** |
> | **Total** | **600** | **200** | **800** |
>
> One of the 800 enrolments is chosen at random.

**8.** Is achieving the certificate **independent** of enrolling in an evening class?

- **(A)** No: 180 ≠ 420, so the two class times produced different numbers of certificates.
- **(B)** No: P(certificate) = 0.750 but P(evening) = 0.300, and these are not equal.
- **(C)** Yes: the events are not mutually exclusive, and any pair that can occur together is independent.
- **(D)** No: P(evening ∩ certificate) = 0.225, which is not 0.
- **(E)** Yes: P(certificate | evening) = 180 ÷ 240 = 0.750, and P(certificate) = 600 ÷ 800 = 0.750. They are equal.

**9.** The probability that the chosen enrolment is an **evening** one, given that it achieved the certificate, is

- **(A)** 0.300
- **(B)** 0.750
- **(C)** 0.225
- **(D)** 0.400
- **(E)** 0.625

**10.** A student calculates P(evening ∩ certificate) two ways: by the general rule, 0.300 × 0.750 = 0.225; and by the product form, 0.300 × 0.750 = 0.225. Which comment is correct?

- **(A)** Only the general rule is valid; the product form is not in the course description and may not be used.
- **(B)** The two agree by coincidence, because 180 happens to be a round number.
- **(C)** Both are valid here, and they agree because independence has been established: substituting P(certificate | evening) = P(certificate) into the general rule turns it into the product form.
- **(D)** Only the product form is valid, because the events are independent and the general rule applies to events that are not.
- **(E)** Neither is valid: with a two-way table the joint probability must be read as 180 ÷ 800.

**11.** The probability that the chosen enrolment is an evening class **or** achieved the certificate, **or both**, is

- **(A)** 1.050
- **(B)** 0.825
- **(C)** 0.225
- **(D)** 0.450
- **(E)** 0.975

**12.** A tutor tells the class: *"Evening enrolment and the certificate are independent, so a student cannot be in both groups."* Which response is best?

- **(A)** The tutor is right: independent events have no outcomes in common.
- **(B)** The tutor is right about the conclusion but has the reason wrong; the correct reason is that P(evening) + P(certificate) exceeds 1.
- **(C)** The tutor is wrong: the events are not independent, so the conclusion does not follow.
- **(D)** The tutor is wrong: 180 enrolments are in both groups, so P(evening ∩ certificate) = 0.225. "Cannot both happen" describes **mutually exclusive** events, which these are not. Independence says only that knowing one leaves the other's probability unchanged.
- **(E)** The tutor is wrong, because independence can only be claimed after a significance test.

---

## Questions 13–16 · The town's recycling audit

> A town's recycling audit holds **25 sacks**, of which **10 contain glass**. Two sacks are chosen at random **without replacement**, one after the other.

**13.** Given that the **first** sack contained glass, the probability that the **second** sack also contains glass is

- **(A)** 0.375
- **(B)** 0.400
- **(C)** 0.360
- **(D)** 0.417
- **(E)** 0.160

**14.** The probability that **both** sacks contain glass is

- **(A)** 0.160
- **(B)** 0.400
- **(C)** 0.775
- **(D)** 0.080
- **(E)** 0.150

**15.** The auditor calculates the probability that both sacks contain glass as 0.400 × 0.400 = 0.160. What is wrong?

- **(A)** Nothing: with 25 sacks the difference is too small to matter.
- **(B)** The auditor should have added, not multiplied, because the question asks for two sacks.
- **(C)** The product form assumes the two draws are independent. Without replacement they are not: after a glass sack is removed, 9 of the remaining 24 contain glass, so the second probability is 0.375, not 0.400. The general rule gives 0.400 × 0.375 = 0.150.
- **(D)** The auditor used the wrong denominator in the first probability; it should be 10 ÷ 24.
- **(E)** The two sacks are mutually exclusive, so the probability is 0.

**16.** The probability that **at least one** of the two sacks contains glass is

- **(A)** 0.650
- **(B)** 0.800
- **(C)** 0.150
- **(D)** 0.350
- **(E)** 0.550

---

## Questions 17–18 · Two more

**17.** For two events A and B, P(A) = 0.400 and P(B) = 0.250. A report claims the two are **both mutually exclusive and independent**. Which response is best?

- **(A)** The claim is possible: the two properties describe different things and do not interfere.
- **(B)** The claim is possible only if A and B come from different variables.
- **(C)** The claim is impossible, because P(A) + P(B) = 0.650, which is less than 1.
- **(D)** The claim is impossible: mutually exclusive forces P(A ∩ B) = 0, while independent forces P(A ∩ B) = 0.400 × 0.250 = 0.100. No pair with non-zero probabilities can satisfy both.
- **(E)** The claim is impossible, because mutually exclusive events always have P(B | A) = P(B).

**18.** A charity knows P(donor gives monthly) = 0.300, P(donor attends an event) = 0.200, and P(gives monthly ∩ attends an event) = 0.080. It wants the probability that a donor **gives monthly or attends an event, or both**. Which calculation answers the question?

- **(A)** 0.300 × 0.200 = 0.060, because "or" with two events calls for the multiplication rule.
- **(B)** 0.300 + 0.200 − 0.080 = 0.420, because the 0.080 who do both are counted in each of the first two terms and must be removed once.
- **(C)** 0.300 + 0.200 = 0.500, because the two groups are separate categories.
- **(D)** 0.080 ÷ 0.300 = 0.267, because "or" conditions one event on the other.
- **(E)** It cannot be found, because the charity has not said whether the two events are independent.

---
---

# Answers and explanations

Each explanation says why the key is right **and what each wrong option reveals.**

> **Answers are collapsed.** Click a question to open it, or press **`e`** to open every explanation at once — useful when the test is on a shared screen.

## Answers 1–7 · The city museum's visitor records

<details>
<summary><strong>Question 1</strong></summary>

**Answer: (D)**

"Given that the visitor is a member" replaces the sample space. The group is no longer all 1,200 visitors but the **480 members**, and the question asks how many of them joined a tour: 180 ÷ 480 = **0.375**.

- **(A)** 0.150 is 180 ÷ 1,200 — the cell over the **table total**. That is the joint probability, not a conditional one. See question 4.
- **(B)** 0.600 is 180 ÷ 300, the cell over its **column** total: conditioning on the tour rather than on membership. That is question 2's answer, and mixing the two is the most expensive error in this topic.
- **(C)** 0.250 is P(tour), 300 ÷ 1,200 — the unconditional probability, which ignores "given".
- **(E)** 0.625 is 1 − 0.375, the probability a member did **not** join a tour.

</details>

<details>
<summary><strong>Question 2</strong></summary>

**Answer: (B)**

The conditioning event is now the tour, so the denominator is the **300 tour-goers**, and 180 of them are members: 180 ÷ 300 = **0.600**.

- **(A)** 0.375 is the same cell over the **row** total — question 1's conditional, the other way round.
- **(C)** 0.150 is the cell over the table total: the joint probability.
- **(D)** 0.250 is P(tour), the margin, with no conditioning at all.
- **(E)** 0.400 is P(member), 480 ÷ 1,200 — the other margin.

**The pair to hold together.** Questions 1 and 2 use the **same 180 visitors**. The answers differ because the denominators differ: 0.375 asks *of the members*, 0.600 asks *of the tour-goers*. P(A | B) and P(B | A) are different numbers, and no rule in this course converts one into the other.

</details>

<details>
<summary><strong>Question 3</strong></summary>

**Answer: (E)**

The press office has 0.600 the right way round for the arithmetic and the wrong way round for the sentence. 180 ÷ 300 = 0.600 is the probability that a **tour-goer is a member**. The claim as written — *0.600 of the museum's members* — conditions on membership, so its denominator must be 480, giving **0.375**.

- **(A)** states the correct calculation and then calls the wrong sentence right. The arithmetic is not the error; the denominator named in words is.
- **(B)** treats a reversed conditional as a formatting problem.
- **(C)** is wrong twice: 0.150 is the joint probability, whose denominator is all 1,200 visitors, so it is not "the proportion of members" either.
- **(D)** The table does not need total membership. The conditional is a statement about the 480 members **in this table**, and 480 is in the margin.

</details>

<details>
<summary><strong>Question 4</strong></summary>

**Answer: (A)**

"Member **and** joined a tour" is the intersection, and its probability is the **joint** probability: the cell over the **whole sample space**, 180 ÷ 1,200 = **0.150**. The word "and" sets no conditioning event, so the denominator stays at 1,200.

- **(B)** 0.375 names the right denominator for its own question — *given a member* — but that is a conditional, not an "and".
- **(C)** 0.600 is the conditional the other way.
- **(D)** All three are legitimate probabilities built from the same 180 visitors, but they answer three different questions. The question asked for one of them.
- **(E)** The multiplication rule is one route to the joint probability — question 5 takes it — but a two-way table gives it directly. The two agree.

**The one thing to carry forward.** One cell, three denominators: 1,200 gives the joint probability, 480 gives the conditional on membership, 300 gives the conditional on the tour. Read the words, then choose the denominator.

</details>

<details>
<summary><strong>Question 5</strong></summary>

**Answer: (C)**

The general multiplication rule is P(A ∩ B) = P(A) × P(B | A). Taking A as "member": P(member) = 0.400 and P(tour | member) = 0.375, so P(member ∩ tour) = 0.400 × 0.375 = **0.150** — the same number the table gives directly, as it must.

- **(A)** 0.400 × 0.250 multiplies the two **marginal** probabilities. That is the product form, and it is only valid when the events are independent. Here they are not, and 0.100 ≠ 0.150 is the proof. Question 6 makes the comparison.
- **(B)** is the union formula, which answers question 7, and it has P(tour) replaced by a conditional besides.
- **(D)** reaches 0.150 by the rule taken the other way round, P(tour) × P(member | tour) = 0.250 × 0.600, which is correct — but the option claims it is the *only* correct route. Either order works; that is why the rule has two forms.
- **(E)** multiplies the two conditionals, which is not a rule at all.

</details>

<details>
<summary><strong>Question 6</strong></summary>

**Answer: (D)**

Independence asks one question: does knowing B change the probability of A? Here P(tour | member) = 0.375 and P(tour) = 0.250. They are not equal, so membership **does** change the probability of a tour, and the events are **not independent**.

- **(A)** confuses independence with the events being able to occur together. Overlapping is what makes them *not* mutually exclusive; it says nothing about independence.
- **(B)** There is no "approximately" in this definition. 0.375 and 0.250 are different numbers, computed from exact counts, and the comparison is exact.
- **(C)** The events are not mutually exclusive either — 180 visitors are both, so P(member ∩ tour) = 0.150, not 0. The verdict is right for the wrong reason, which earns no credit.
- **(E)** A two-way table of all 1,200 visitors is the population here, and the framework's test is this comparison. No significance test is involved — that is Unit 3.

</details>

<details>
<summary><strong>Question 7</strong></summary>

**Answer: (B)**

P(A ∪ B) = P(A) + P(B) − P(A ∩ B) = 0.400 + 0.250 − 0.150 = **0.500**. By counting: 480 members plus 300 tour-goers is 780, but the 180 who are both have been counted twice, so the union contains 480 + 300 − 180 = 600 visitors, and 600 ÷ 1,200 = 0.500. The two routes agree.

- **(A)** 0.650 is 0.400 + 0.250, the union found by adding. It counts the 180 in the overlap twice, and is the single most common error on 2.7.A.3.
- **(C)** 0.150 is the **intersection**, not the union: "and" instead of "or".
- **(D)** 0.350 removes the overlap twice, 0.400 + 0.250 − 2(0.150). Subtracting the double count once is enough — the overlap belongs in the union, just not twice.
- **(E)** 0.100 is P(member) × P(tour), the product form, which is neither a union nor correct here.

**"Or" is inclusive.** The union includes the 180 who did both. If a question means one or the other but not both, it has to say so.

</details>

## Answers 8–12 · The language school's enrolments

<details>
<summary><strong>Question 8</strong></summary>

**Answer: (E)**

P(certificate | evening) = 180 ÷ 240 = 0.750 and P(certificate) = 600 ÷ 800 = 0.750. They are **equal**, so knowing an enrolment is an evening one tells you nothing about the certificate: the events are independent. The check works from the other row too — P(certificate | daytime) = 420 ÷ 560 = 0.750.

- **(A)** compares raw counts. 180 and 420 differ because the two rows have different sizes, 240 and 560. Independence is a comparison of **probabilities**, never of counts.
- **(B)** compares P(certificate) with P(evening). Those are two different events; there is no reason for them to be equal, and their inequality means nothing. The comparison must be P(A | B) against P(A).
- **(C)** confuses the two relationships. Overlapping means not mutually exclusive, which is a different statement.
- **(D)** correctly shows the events are not mutually exclusive, then draws the wrong conclusion from it.

</details>

<details>
<summary><strong>Question 9</strong></summary>

**Answer: (A)**

Conditioning on the certificate makes the denominator the **600 certificate holders**, of whom 180 enrolled in evening classes: 180 ÷ 600 = **0.300**. Notice that this equals P(evening) = 240 ÷ 800 = 0.300. That is not a coincidence: **independence runs both ways**. If knowing the class time leaves the certificate's probability unchanged, then knowing the certificate leaves the class time's probability unchanged.

- **(B)** 0.750 is P(certificate | evening) — question 8's conditional, reversed.
- **(C)** 0.225 is the joint probability, 180 ÷ 800.
- **(D)** 0.400 is 240 ÷ 600 — the evening **row total** over the certificate **column total**, two margins divided by each other, which is not a probability of anything.
- **(E)** 0.625 is 500 ÷ 800, a number from the wrong table; nothing in this one produces it.

</details>

<details>
<summary><strong>Question 10</strong></summary>

**Answer: (C)**

Both calculations are right, and they agree for a reason. The course description states only the **general** rule, P(A ∩ B) = P(A) × P(B | A). Question 8 established that P(certificate | evening) = P(certificate) = 0.750. Substituting that equality into the general rule turns P(A) × P(B | A) into P(A) × P(B) — the product form. It is a **consequence** of the general rule plus independence, not a second rule, and it is available here precisely because independence was checked first.

- **(A)** The product form is not off-syllabus; it is a theorem derived from content that is on it. What is not permitted is using it before independence has been established.
- **(B)** The agreement is structural, not coincidental: the table was independent, so the two routes had to meet.
- **(D)** reverses the relationship. The general rule applies to **every** pair, independent or not; the product form is the special case.
- **(E)** Reading 180 ÷ 800 is a third correct route. All three give 0.225.

**The order that matters.** Check independence, then use the product form — never the reverse. In question 5's museum table the same substitution was not available, and the product form gave 0.100 against a true 0.150.

</details>

<details>
<summary><strong>Question 11</strong></summary>

**Answer: (B)**

P(evening ∪ certificate) = 0.300 + 0.750 − 0.225 = **0.825**. By counting: 240 + 600 − 180 = 660 enrolments, and 660 ÷ 800 = 0.825.

- **(A)** 1.050 is 0.300 + 0.750, the union by adding. It should be rejected on sight: a probability cannot exceed 1, so the 0-to-1 bound catches this error before any other reasoning does.
- **(C)** 0.225 is the intersection.
- **(D)** 0.450 is 0.750 − 0.300, a difference of margins.
- **(E)** 0.975 subtracts 0.075 — a quarter of the overlap — and corresponds to no step.

**Independence does not change the union formula.** These events are independent, which fixes the value of P(A ∩ B) at 0.225, but the subtraction still happens. Only mutual exclusivity removes that term, by making it zero.

</details>

<details>
<summary><strong>Question 12</strong></summary>

**Answer: (D)**

180 enrolments are evening classes **and** achieved the certificate, so P(evening ∩ certificate) = 0.225, which is not 0. "Cannot both happen" is the definition of **mutually exclusive**, and these events plainly are not. Independence is a different claim altogether: knowing the class time leaves the certificate's probability at 0.750.

- **(A)** states the confusion the question is testing. Independent events generally *do* have outcomes in common; here 180 of them.
- **(B)** reaches the wrong conclusion and supports it with an irrelevance. P(A) + P(B) exceeding 1 does show the events must overlap — which contradicts the tutor rather than confirming them.
- **(C)** rejects the tutor's independence claim, but question 8 established it. The independence is correct; the inference from it is not.
- **(E)** Significance tests belong to Unit 3. Independence here is settled by comparing two probabilities from the table.

</details>

## Answers 13–16 · The town's recycling audit

<details>
<summary><strong>Question 13</strong></summary>

**Answer: (A)**

The first sack is not replaced. After a glass sack is removed, **24 sacks remain and 9 of them contain glass**, so P(second has glass | first had glass) = 9 ÷ 24 = **0.375**. Both the numerator and the denominator fall by one.

- **(B)** 0.400 is 10 ÷ 25, the **first** draw's probability — the answer you get by forgetting that a sack was removed.
- **(C)** 0.360 is 9 ÷ 25: the numerator reduced but not the denominator.
- **(D)** 0.417 is 10 ÷ 24, which is P(second has glass | first had **none**) — the denominator reduced but not the numerator. Right arithmetic, wrong condition.
- **(E)** 0.160 is 0.400², the probability of two glass sacks **with** replacement, and not a conditional probability at all.

</details>

<details>
<summary><strong>Question 14</strong></summary>

**Answer: (E)**

By the general multiplication rule, P(both) = P(first) × P(second | first) = (10 ÷ 25) × (9 ÷ 24) = 0.400 × 0.375 = **0.150**.

- **(A)** 0.160 is 0.400 × 0.400, the product form, which assumes the draws are independent. Question 15 takes this apart.
- **(B)** 0.400 is the first draw alone.
- **(C)** 0.775 adds the two probabilities, 0.400 + 0.375 — a union calculation applied to an "and".
- **(D)** 0.080 halves the correct answer, as though order mattered and only one arrangement counted. Both sacks containing glass is a single event; there is nothing to halve.

</details>

<details>
<summary><strong>Question 15</strong></summary>

**Answer: (C)**

0.400 × 0.400 is the product form, and the product form requires independence. Drawing **without replacement** makes the two draws **not independent** by construction: the first sack changes what is left for the second, so P(second has glass | first had glass) = 9 ÷ 24 = 0.375, not 0.400. The general rule gives 0.400 × 0.375 = 0.150, and 0.160 overstates it by 0.010.

- **(A)** The error is small here — 0.010 — and it is still an error. It shrinks as the pile grows: with 1,000 sacks and 400 glass, both routes give 0.250 to three decimal places. "Too small to matter" is a judgement about a particular n, not a reason the method is sound.
- **(B)** Adding answers "or", not "and".
- **(D)** The first draw is from all 25 sacks, so 10 ÷ 25 is right. It is the **second** denominator that changes.
- **(E)** The two sacks are not events at all, let alone mutually exclusive ones, and 0.150 ≠ 0.

</details>

<details>
<summary><strong>Question 16</strong></summary>

**Answer: (A)**

"At least one" is the complement of "**none**", which is the cheaper event to compute. P(neither has glass) = (15 ÷ 25) × (14 ÷ 24) = 210 ÷ 600 = 0.350, so P(at least one) = 1 − 0.350 = **0.650**. Note the second factor: 14 of the remaining 24, because a non-glass sack was removed.

- **(B)** 0.800 is 0.400 + 0.400, treating "at least one" as a union of two events that overlap — and both draws can produce glass, so the overlap is real and this double counts it.
- **(C)** 0.150 is P(both), the opposite end of the question.
- **(D)** 0.350 is P(neither) — the complement computed correctly and then not subtracted from 1.
- **(E)** 0.550 corresponds to no step.

**Three Session 9 habits, reused.** The complement written as 1 − P(none) is 2.4.A.4; "at least one" as the complement of "none" is the same move Session 9 made on the bike-share bands; and the second denominator of 24 is this session's contribution.

</details>

## Answers 17–18 · Two more

<details>
<summary><strong>Question 17</strong></summary>

**Answer: (D)**

The two properties make incompatible demands on the same number. Mutually exclusive means P(A ∩ B) = 0. Independent means P(A ∩ B) = P(A) × P(B) = 0.400 × 0.250 = 0.100. A single quantity cannot be both 0 and 0.100, so **no pair of events with non-zero probabilities is both**.

- **(A)** The properties are indeed different things, which is why they are often confused — but they are not independent of each other. Each pins down P(A ∩ B), and they pin it to different values.
- **(B)** Different variables has nothing to do with it. The museum's membership and tour came from different variables and were neither mutually exclusive nor independent.
- **(C)** P(A) + P(B) = 0.650 ≤ 1 shows only that the events *could* be mutually exclusive. It does not address independence, and it is not the contradiction.
- **(E)** This gets the implication backwards. If A and B are mutually exclusive and P(A) > 0, then P(B | A) = 0 ÷ 0.400 = 0 — while P(B) = 0.250. Knowing A happened rules B out entirely — the furthest a pair of events can get from **independent**, not an example of it.

**Why "both" is the empty box.** Mutually exclusive events with non-zero probability are as far from independent as a pair can be: one occurring makes the other impossible. That is the reverse of independence, not a companion to it.

</details>

<details>
<summary><strong>Question 18</strong></summary>

**Answer: (B)**

"Or … or both" is the **union**, and the union formula is P(A ∪ B) = P(A) + P(B) − P(A ∩ B) = 0.300 + 0.200 − 0.080 = **0.420**. The 0.080 who do both appear inside the 0.300 and again inside the 0.200, so they are counted twice by the addition and removed once by the subtraction.

- **(A)** multiplies, which gives an intersection, not a union — and the product form at that, which the charity's own figures contradict: 0.300 × 0.200 = 0.060, but P(A ∩ B) = 0.080, so these events are **not independent**.
- **(C)** 0.500 is the union by adding, with the overlap left double counted.
- **(D)** 0.267 is P(attends | gives monthly), a conditional probability. "Or" never conditions.
- **(E)** Independence is not needed. The union formula requires P(A ∩ B), and the charity has supplied it directly. Independence would only matter if that value had to be **computed** rather than given.

**The decision the question is really testing.** "And" → the general multiplication rule. "Or" → the union formula. "Given" → a conditional, and a new denominator. The charity's figures contain a bonus finding: because 0.300 × 0.200 ≠ 0.080, giving monthly and attending events are not independent.

</details>

---
---

# Marking and diagnosis

## Score

One mark per question. **Total 18.**

| Score | Reading |
|---|---|
| 16–18 | Secure. Unit 2's probability rules are complete; Session 11 can move to random variables. |
| 13–15 | Sound. Reteach only the items missed, using the table below. |
| 9–12 | The formulas are there but the denominators are not yet chosen from the words. Re-run Scenario A before Session 11. |
| 0–8 | Reteach Session 10. Conditional probability reappears in every remaining unit, and it will not hold. |

## What each miss points to

Each row names the **theory to reread** and **where it is applied**, in the order the session teaches them.

| Missed | Theory to reread | Where it is applied |
|---|---|---|
| 1, 4 | Conditional probability: the probability of A given B (2.6.A.1) · Why the denominator changes: a cell over a row total (2.6.A.1) | The register again, now with the row total as a denominator |
| 2, 3 | P(A \| B) and P(B \| A) are different numbers (2.6.A.1) | The governor's "0.850 of bus users live in the Villages" |
| 5, 14 | The general multiplication rule (2.6.A.2) | P(bus \| Villages) and the general multiplication rule on the same cell |
| 6, 8 | Independent events, defined by what knowing one tells you about the other (2.7.A.1) · Testing independence from a two-way table (2.7.A.1) | Is travelling by bus independent of living in the Villages? · Are missed appointments independent of first appointments? |
| 7, 11 | The union of two events, and the word "or" (2.7.A.2) · The probability of a union, and the outcomes counted twice (2.7.A.3) | "Bus or Villages": the union Session 9 counted and could not yet calculate · The administrator's 0.500 for "a first appointment or a missed one" |
| 9, 10, 15 | Deriving the product form, and why it is not a second rule to memorise (2.7.A.1 with 2.6.A.2) | Which of the clinic's pairs may simply be added |
| 12, 17 | Mutually exclusive against independent: why no pair with non-zero probability is both (2.5.A.2, 2.6.A.1, 2.7.A.1) | The question that settles it: why "both" is empty |
| 13, 16 | Drawing without replacement, where the second probability depends on the first (2.6.A.2, 1.11.A.1) | Two records drawn for audit, without replacement |
| 18 | Which rule the question is asking for: a decision list (2.6–2.7) | The sentence the office may now write |

> **The three misses to treat as urgent.** **Question 3 or 4** — a cell divided by the wrong total is the error that costs most marks in Unit 2, and it costs them silently, because the arithmetic is always correct. **Question 10 or 15** — using the product form before independence has been established is the habit the prep books install, and it gives a wrong answer whenever the events are not independent. **Question 17** — mutually exclusive and independent are opposite relationships, not compatible ones, and every later unit assumes the student can tell them apart.

---

*CED references: Topic 2.6 (2.6.A.1–2), Topic 2.7 (2.7.A.1–3). Course and Exam Description effective Fall 2026.*

*Every number in this test was computed and checked by script: all three tables sum to their stated totals, every probability is exact to 3 decimal places, the language school's table is exactly independent and the museum's is exactly not, and each distractor was recomputed from the specific error it represents so that none can coincide with its key.*
