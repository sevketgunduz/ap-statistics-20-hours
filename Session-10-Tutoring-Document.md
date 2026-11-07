# Session 10 — Conditional Probability, Independence and Unions

**AP Statistics · Twenty-Hour Course · One-to-one tutoring edition**
**CED Topics 2.6, 2.7 · Skill 3.C · about 165 minutes, plus the 35-minute Session 8 test**

---

## Where this session sits

Session 9 could calculate the probability of an event and the probability of its complement, and could say whether two events were mutually exclusive. It could not answer the one question every two-way table in this course has been waiting for: *given* that the student lives in the Villages, how probable is the bus? That question is topic 2.6, and answering it changes one thing only — the denominator. Session 8 did the same arithmetic under the name **conditional relative frequency**; today it acquires its probability name, its notation P(A | B), and a formula.

From that definition two further rules fall out and nothing else does. Rearranged, it gives the **general multiplication rule**, P(A ∩ B) = P(A) × P(B | A), which is the only product form the course description states. Set against the unconditional probability, it gives the definition of **independence**: A and B are independent exactly when knowing about A leaves B's probability alone. And alongside both sits the **union** — the probability that A or B or both occur — whose rule subtracts the outcomes that the naive sum counts twice. Session 9 counted those students by hand at Lincoln High and left the formula for today.

The session also closes the confusion the last one opened deliberately. *Mutually exclusive* and *independent* are not two shades of the same idea; for events with non-zero probability they are mutually impossible, and the proof is two lines long. It is in the theory section, and the activity is built on it.

Both scenarios carry forward. Lincoln High's travel register — the same 1,842 students, the same table since Session 8 — supplies every conditional probability in Scenario A, including the pair of numbers that Session 8's homework and Session 9's diagnostic both caught students fusing. St Mary's clinic supplies Scenario B's unions and an audit of two records drawn without replacement.

### Learning objectives for topics 2.6 and 2.7

Verbatim from the course description.

| Code | Objective | Skill |
|---|---|---|
| 2.6.A | Calculate conditional probabilities. | 3.C |
| 2.7.A | Calculate probabilities for independent events and for the union of two events. | 3.C |

Skill **3.C**: *Calculate and estimate expected counts, percentages, probabilities, and intervals.*

Two objectives and five essential-knowledge statements: 2.6.A.1, 2.6.A.2, and 2.7.A.1 to 2.7.A.3. Every one is stated in the theory section and then applied at least twice.

### What the course description does and does not ask for

Read this before teaching. On this pair of topics the prep books carry noticeably more machinery than the 2026 framework does, and two of the additions are the ones students most often quote back in an exam.

- **The course description never states P(A ∩ B) = P(A) × P(B).** Checked page by page through Unit 2: the only product form anywhere in the framework is 2.6.A.2's **general** rule, P(A ∩ B) = P(A) × P(B | A). The familiar special case is a **theorem**, obtained by substituting 2.7.A.1's P(B | A) = P(B) into the general rule, and the theory section has the student perform that substitution. It is perfectly usable — it is not off-syllabus content, it is a consequence of content — but the examinable statements are the general rule and the definition of independence, and a student who has memorised only the short form cannot tell when it applies.
- **The course description never uses the phrase "addition rule."** Its wording is *the probability of the union* (2.7.A.2), and the formula is 2.7.A.3. All three prep books use the other name; the red box below records it.
- **"Dependent events" is not a term the framework defines.** It names *independent*, and the correct description of the other case is simply **not independent**. Say "not independent"; it costs nothing and it keeps the student inside the definition.
- **Without replacement is already taught.** Sampling without replacement is 1.11.A.1, from Session 6, and it is the cleanest reason a second probability differs from the first. It is recalled by code in the theory and used in Scenario B and the homework; it is not re-taught.
- **Session 9's content is recalled, not re-taught.** The sample space and its nonoverlapping outcomes (2.4.A.1), the counting formula and its "if equally likely" clause (2.4.A.2), the 0-to-1 bound (2.4.A.3), the complement in its three notations (2.4.A.4), joint probability as the intersection (2.5.A.1) and mutually exclusive as P(A ∩ B) = 0 (2.5.A.2) are all assumed. The first theory subsection names them, and the scenarios point back to Session 9's subsection titles where a definition is needed.
- **2.6.A.1's formula divides by P(B), so P(B) must not be 0.** The framework does not spell that out; say it once, because a student who conditions on an impossible event is usually conditioning on the wrong variable.
- **Both objectives are Skill 3.C — calculate.** Unlike 2.5.A, neither asks for a justification in the Skill 4.B sense. The habits Session 9 built are still right (name the event, name the group you are dividing by), but the mark here is on the number and the denominator that produced it.

:::note red Off-syllabus names and diagrams, not taught as examinable
The course description never uses **"addition rule"** for 2.7.A.3 — its phrase is *the probability of the union*. Barron's pdf 272, 275, 276, 5 Steps pdf 165 and Princeton Review Chapter 6 (*"Union (addition rule)"*) all use the other name. **Venn diagrams** (5 Steps pdf 64; Princeton Review Chapter 6) and **tree diagrams** (Barron's pdf 272, 276; 5 Steps pdf 164, 176) have **zero** occurrences in the framework; no exam question requires either, and no diagram of either kind appears anywhere in this session. The representation the framework does name for two categorical variables is the **two-way table** (2.1.A.1), which is what today uses. **Bayes' theorem** has zero occurrences and is not in this course at any point — the only reversal of a conditional the student needs is to recompute P(A | B) from the table, which is what Scenario A does. **"Dependent events"**, **"law of total probability"**, **"exhaustive"** and **"odds"** are also absent. **Law of averages** and **gambler's fallacy** remain on the register from Session 8, and the prep-book phrase "addition rule" joins it from Session 9.
:::

### Timing and who talks

**The Session 8 test comes first.** Following the pattern of the earlier sessions — Session 6's test opened Session 8, Session 7's opened Session 9 — give Session 8's multiple-choice test at the start of this session, before the homework debrief: 20 questions, 35 minutes, as the test page states. The pattern has not been confirmed as a rule; if your own plan differs, follow it. The clock below starts when the test is finished.

| Minutes | Segment | Who talks |
|---|---|---|
| 0–14 | Homework debrief and diagnostic | Student |
| 14–56 | **Theory**: Session 9 recalled; conditional probability and its denominator; P(A \| B) against P(B \| A); the general multiplication rule; drawing without replacement; independence; deriving the product form; testing independence from a table; the union and the word "or"; the probability of a union and the double count; mutually exclusive against independent; a decision list; seven check questions (2.6–2.7) | Both |
| 56–90 | **Scenario A**: Lincoln High's register — P(bus \| Villages), the inverted conditional, an independence test, and the union Session 9 counted by hand | Both |
| 90–110 | **Activity**: three recognition cards, then twelve event pairs sorted into four boxes, one of which stays empty | Student |
| 110–142 | **Scenario B**: St Mary's clinic — unions and the double count, conditional probabilities both ways, and two records drawn without replacement | Both |
| 142–156 | Solo case: the café's loyalty members, conditioned on the drink | Student |
| 156–165 | Teach it back, set homework | Student |
| **Total** | **165 minutes of teaching, after the 35-minute Session 8 test** | |

The course description allots four class periods to topics 2.6 and 2.7 (two each). This is the longest session in Unit 2 and deliberately so: five essential-knowledge statements, four of which are formulas, and the one confusion in the unit that survives to the exam if it is not dismantled here. Nothing is cut, compressed or moved into the homework; the homework practises what the session has already taught.

:::note teal Why there is no interactive tool in this session
STANDARDS.md §5 asks three questions of any simulation, and this content fails the second. Conditional probability, the multiplication rule, independence and the union are all facts about one fixed sample space, read off a table that does not change; a table with the conditioning total ringed shows everything a tool could, and the student's pen does the driving. The processes that need a tool — a statistic scattering around a parameter, a sampling distribution forming — arrive in Sessions 11 and 12.
:::

---

## 0–14 min · Homework debrief and diagnostic

### The Session 9 homework: two lists and two errors

The student arrives with the Session 9 homework self-marked. Ask for the two lists: *"Which did you get wrong, and which did you put a question mark on?"* Spend the time on those only.

**The two errors to check for specifically:**

- **B7 and D4: a verdict without a joint probability, or "different things, so not mutually exclusive".** B7 asked whether "is in Year 9" and "has school lunch" are mutually exclusive; the answer is no, because P(Year 9 ∩ school lunch) = 35 ÷ 200 = 0.175. D4 asked the same of "treated at St Mary's" and "would recommend", where the number is 63 ÷ 300 = 0.210. A student who wrote the right verdict with no number got one mark of two. Four minutes here, because today the *same* pair of events gets a second and harder question asked of it — not "can they both happen?" but "does one of them change the probability of the other?" — and a student who cannot produce P(A ∩ B) cannot produce P(A | B) either, since the intersection is the numerator of the definition.
- **E2: the four library members, and the rule that was not available yet.** The sheet said so explicitly: getting from one member to four needs the multiplication rule, 2.6.A.2, which is today. The key gave the exact answer, P(none of the four borrows both formats) = 0.2401 and so P(at least one) = 0.7599, against the student's 0.700. **That calculation is this session's content and we will do it.** If the student put a **?** here, promise them the answer and keep the promise: the theory's *Drawing without replacement* subsection and the homework's Part D both turn on exactly this step.

Worth thirty seconds each if they were marked wrong: **B5**, the "three lunch types so 0.333" reflex, which the solo case will test again; and **C4**, where the complement and the count were two roads to 0.850 — today adds a third road to several answers, and the student should expect them to agree.

Then the diagnostic.

### Four diagnostic questions on "given", "and" and "or"

Four quick questions, answers out loud. They test Session 8's conditioning and Session 9's joint probability, which are the two things today is built on.

**Q1.** *"From Lincoln High's table: of the 294 Villages students, 250 travel by bus, and there are 651 bus users in all. Give me 250 ÷ 294 and 250 ÷ 651 in words — what is each one the probability of?"*

**Q2.** *"P(A) = 0.600 and P(B) = 0.500. What is P(A ∩ B)?"*

**Q3.** *"A café's loyalty members: 150 of 240 usually drink coffee and 120 of 240 usually add food. How many usually do at least one of the two?"*

**Q4.** *"Two events cannot both happen. If I tell you the first one happened, what do you now know about the second?"*

| What you hear | What it means | Where to start |
|---|---|---|
| Q1: "of the Villages students, the probability of bus; and of the bus users, the probability of Villages" | Session 8's conditioning survived, and the two directions are already separate | Move briskly through the theory's first four subsections; the notation is new, the arithmetic is not |
| Q1: the same number twice, or "both are 0.850" | The Session 8 B3 error is still live, and today is where it becomes expensive | Teach *P(A \| B) and P(B \| A) are different numbers* slowly, and make Scenario A's inverted-conditional section the centre of the session |
| Q1: "0.850 and 0.384" with no words attached | The arithmetic is right and the meaning is not attached to it | Insist on the phrase *"of the …"* before every fraction today, exactly as Session 8 required |
| Q2: "you cannot tell without more information" | 2.5.A.1's limit held — this is the correct answer | Say so, and promise the two things that would let them answer: P(B \| A), or independence |
| Q2: "0.300" | The product form has been imported from somewhere, without its condition | Teach *The general multiplication rule* and *Deriving the product form* as one block, and do not let the short form be written before the long one |
| Q3: "270 — no, wait, that is more than 240" | The double count has been spotted unaided | Let them finish: the overlap is 84, so the answer is 186. Then name it: that is 2.7.A.3 |
| Q3: "270" | The union will be computed as a sum all session unless this is fixed now | Teach *The probability of a union, and the outcomes counted twice* with the café counts on the screen; Scenario B carries the same trap |
| Q4: "the second one definitely did not happen" | Ready for the mutually-exclusive-against-independent proof | Run that subsection at pace and spend the time on the activity instead |
| Q4: "nothing — they're unrelated" | The two ideas are fused; this is the confusion the session exists to fix | Do not move past *Mutually exclusive against independent* until they can state P(A \| B) = 0 for a mutually exclusive pair |

---

## 14–56 min · Theory — conditional probability, independence and unions

Every concept the session uses is stated here, before any scenario data. Put each subsection on the shared screen, read the rule with the student, and have them say what it does **not** say. Each subsection carries two examples doing different jobs: the *Illustration* is deliberately bare, so the structure shows with nothing to distract from it, and the *Education example* is a study of the kind this course is about, so the rule is seen doing something. Read bare first and concrete second.

The bare cases are two made-up tables and one box of ten units. The **40-unit table** is new and is deliberately *not* independent; the **30-unit table** is the one Session 9 used, and it turns out to be exactly independent, which is why the product appeared to work there. Lincoln High, the library, St Mary's and the café come afterwards and apply these rules; when a question there needs a definition, point back to the subsection here.

**The education examples continue the strand from Sessions 6 to 9**: the **district** — its 400 Year 11 pupils cross-tabulated by revision attendance and result, and its summer-school lottery of 50 applicants for 30 places, 14 of them from the two smallest schools — and the **university's first-year statistics module** of 318 students, whose scripts go to a marking moderation panel. Thirteen subsections and a set of checks. Keep each subsection to about three minutes and make the student speak in every one.

**The two made-up tables, for reference.**

| 40 units | Yes | No | Total |
|---|---|---|---|
| Type A | 18 | 6 | **24** |
| Type B | 4 | 12 | **16** |
| **Total** | **22** | **18** | **40** |

| 30 units (Session 9's) | Yes | No | Total |
|---|---|---|---|
| Type A | 4 | 8 | **12** |
| Type B | 6 | 12 | **18** |
| **Total** | **10** | **20** | **30** |

:::checks
40-unit table: 24 + 16 = 40 · 22 + 18 = 40
30-unit table: 12 + 18 = 30 · 10 + 20 = 30
:::

### What Session 9 established, and the question it could not answer (2.4–2.5 recalled)

Retrieval, not teaching. Make the student give all six back before anything new is said.

| From Session 9 | In one line | Code |
|---|---|---|
| Sample space | all possible **nonoverlapping** outcomes of a random process | 2.4.A.1 |
| P(E) by counting | outcomes in E ÷ outcomes in the sample space, **if** they are equally likely | 2.4.A.2 |
| The 0-to-1 bound | every probability is a number from 0 to 1 inclusive | 2.4.A.3 |
| The complement | P(E′) = P(Ē) = P(E^C) = 1 − P(E) | 2.4.A.4 |
| Joint probability | P(A ∩ B), the probability that **both** occur | 2.5.A.1 |
| Mutually exclusive | they cannot occur together, so P(A ∩ B) = 0 | 2.5.A.2 |

What Session 9 could not do. Every probability it calculated had the **whole sample space** underneath it: 1,842 students, 1,000 records, 240 members. It had no way to answer *"of the Villages students, how probable is the bus?"* — and it said so, three times, pointing here. That restriction is the whole of topic 2.6, and everything else in this session follows from it.

*Illustration:* in the 40-unit table, Session 9 could give P(A) = 24 ÷ 40 = **0.600**, P(yes) = 22 ÷ 40 = **0.550**, P(A ∩ yes) = 18 ÷ 40 = **0.450** and P(A′) = **0.400**. What it could not give is the probability that a unit is marked yes **when you already know it is type A**.

*Education example:* for one of the district's 400 Year 11 pupils chosen at random, Session 9 gave P(attended the revision programme) = 240 ÷ 400 = **0.600**, P(passed) = 260 ÷ 400 = **0.650** and P(attended ∩ passed) = 180 ÷ 400 = **0.450**. The governors' actual question — *does attending the programme raise a pupil's chance of passing?* — needs the probability of passing **among the attenders**, which Session 8 computed as a conditional relative frequency of 75.0% and Session 9 was not allowed to call a probability.

### Conditional probability: the probability of A given B (2.6.A.1)

The probability that event A will occur **given that event B has occurred** is called a **conditional probability**, written **P(A | B)**, and defined as the joint probability divided by the probability of the condition.

:::formula
P(A | B) = P(A ∩ B) ÷ P(B)

P(A | B) — the probability of A given B, read "the probability of A given B"
P(A ∩ B) — the probability that A and B both occur (2.5.A.1)
P(B) — the probability of the event being conditioned on; it must not be 0
:::

The vertical bar is not division and never was; it reads *given*. What the formula says is that conditioning **shrinks the sample space to B** and then asks what share of that smaller space is also A. The numerator is the overlap because, once you know B happened, the only way A can still happen is in the part of A that lies inside B.

What it does not say. It does not say P(A) — a conditional probability is a different number from the unconditional one, except in the special case this session calls independence. It does not say P(A ∩ B): the intersection is the numerator, not the answer, and the two differ by a factor of 1 ÷ P(B), which is always 1 or more. It is undefined when P(B) = 0; conditioning on something that cannot happen is not a question. And the bar is **not symmetric** — P(A | B) and P(B | A) are different quantities with different denominators, which gets a subsection of its own two below.

*Illustration:* in the 40-unit table, P(yes | type A) = P(A ∩ yes) ÷ P(A) = 0.450 ÷ 0.600 = **0.750**. Read straight off the table it is 18 ÷ 24 = 0.750, the same thing: 24 units are type A, and 18 of those are marked yes.

*Education example:* for one of the district's 400 Year 11 pupils, P(passed | attended) = P(attended ∩ passed) ÷ P(attended) = 0.450 ÷ 0.600 = **0.750**, or 180 ÷ 240 directly. Against P(passed) = 0.650 for a pupil chosen from all 400, and P(passed | did not attend) = 80 ÷ 160 = **0.500**. This is Session 8's 75.0% and 50.0% with a probability name attached, and it is the number the governors asked for.

### Why the denominator changes: a cell over a row total (2.6.A.1)

Say this out loud, because it is the cheapest win in the session. **Conditional probability is the same arithmetic Session 8 did, renamed.** In a two-way table:

| Quantity | Divide the cell by | Session 8's name |
|---|---|---|
| P(row ∩ column) | the **table** total | joint relative frequency |
| P(column \| row) | that **row's** total | conditional relative frequency |
| P(row \| column) | that **column's** total | conditional relative frequency |

So the only thing that changes when the word *given* appears is which total goes underneath. Install the habit Session 8 installed and Session 9 kept: **say the group out loud — "of the type A units, …" — before writing the fraction.** The group named after "of" is the denominator, every time.

What it does not say. It does not say the cell changes. The numerator of P(yes | A), of P(A | yes) and of P(A ∩ yes) is the same 18 units; only the denominator distinguishes them, which is precisely why the three are so easy to confuse. And it does not say that the row total is always right — if the condition is a column, the column total is the denominator, and a student working mechanically down a table will reach for the row total both times.

*Illustration:* the same 18 units, three ways. P(A ∩ yes) = 18 ÷ **40** = 0.450. P(yes | A) = 18 ÷ **24** = 0.750. P(A | yes) = 18 ÷ **22** = 0.818. One cell, three denominators, three different numbers.

*Education example:* of the district's 400 Year 11 pupils, the 180 who both attended and passed give P(attended ∩ passed) = 180 ÷ **400** = 0.450, P(passed | attended) = 180 ÷ **240** = 0.750, and P(attended | passed) = 180 ÷ **260** = **0.692**. The district's report quotes the first as "45% of our Year 11 cohort", the second as "75% of attenders passed" and the third as "69% of those who passed had attended". All three are true, all three are about the same 180 pupils, and they answer three different questions.

### P(A | B) and P(B | A) are different numbers (2.6.A.1)

This is the session's first trap, and it has already cost marks twice in this course: Session 8's homework B3 and Session 9's diagnostic Q1 both caught it. The two conditionals share a numerator and have different denominators, so they are equal only when P(A) = P(B).

:::formula
P(A | B) = P(A ∩ B) ÷ P(B)        P(B | A) = P(A ∩ B) ÷ P(A)
:::

The practical test is a sentence. *"Of the B group, what share are A?"* is P(A | B). *"Of the A group, what share are B?"* is P(B | A). If a question does not make clear which group it is restricting to, the question is ambiguous — but exam questions always do, in the words *of*, *given*, *among* or *for those who*.

What it does not say. It does not say one of them is wrong. Both are legitimate probabilities about the same data; the error is answering the question that was not asked. And reversing a conditional is **not** a matter of flipping the fraction: 1 ÷ 0.750 is not 0.818, and there is no rule in this course that converts P(A | B) into P(B | A). You go back to the table and divide the same cell by the other total.

*Illustration:* in the 40-unit table, P(yes | A) = 18 ÷ 24 = **0.750** and P(A | yes) = 18 ÷ 22 = **0.818**. Same 18 units. In the other row, P(A | yes) is large because most yes units are type A, while P(yes | B) = 4 ÷ 16 = **0.250** is small.

*Education example:* the district's report must keep two sentences apart. *"Of the pupils who attended the revision programme, 75% passed"* is P(passed | attended) = 0.750. *"Of the pupils who passed, 69% had attended"* is P(attended | passed) = 0.692. A governor who reads the second as the first concludes that attendance guarantees nothing much; a governor who reads the first as the second concludes that three-quarters of the district's passes came from the programme. Neither conclusion is in the data, and both are common.

### The general multiplication rule (2.6.A.2)

The **general multiplication rule** states that the probability that events A and B both will occur is equal to the probability that A will occur multiplied by the conditional probability that B will occur given that A has occurred.

:::formula
P(A ∩ B) = P(A) × P(B | A)

P(A ∩ B) — the probability that both occur (2.5.A.1)
P(A) — the probability of the first event
P(B | A) — the probability of B given that A has occurred (2.6.A.1)
:::

It is the definition of conditional probability with the denominator moved across, and it is the **only product form the course description states**. It works in either order, because the intersection does not care which event you call A: P(A ∩ B) = P(B) × P(A | B) is the same rule. Choose whichever conditional you actually know.

What it does not say. It does not say P(A) × P(B). The second factor is **conditional**, and dropping the condition is the most expensive single slip on this topic — it silently assumes independence. It does not say the two events happen in sequence; "and" means both hold for the same individual or the same trial, as Session 9 insisted, and the rule applies just as well to one student with two recorded characteristics. And it is not a way of *checking* a joint probability you read off a table: in a table the cell is the better source, and the rule earns its keep where there is no table, which is exactly the case of two draws.

*Illustration:* in the 40-unit table, P(A) = 0.600 and P(yes | A) = 0.750, so P(A ∩ yes) = 0.600 × 0.750 = **0.450** — which is 18 ÷ 40, the cell. Note what the naive product would have given: 0.600 × 0.550 = 0.330, which is not 0.450.

*Education example:* for a district Year 11 pupil, P(attended) = 0.600 and P(passed | attended) = 0.750, so P(attended ∩ passed) = 0.600 × 0.750 = **0.450** — matching the 180 pupils in the cell. The naive product, 0.600 × 0.650 = **0.390**, is what the district would have predicted if attendance made no difference to passing; the gap between 0.390 and 0.450 is the programme's apparent effect, and it is also a preview of how independence is tested.

### Drawing without replacement, where the second probability depends on the first (2.6.A.2, 1.11.A.1)

Where the general multiplication rule is indispensable is a pair of **draws without replacement** — sampling in which a selected individual is not returned before the next selection, which is 1.11.A.1 from Session 6. Remove one individual and both the numerator and the denominator of the next probability change, so the second draw's probability genuinely depends on the first, and the conditional factor is not optional.

:::formula
P(first is A ∩ second is A) = P(first is A) × P(second is A | first is A)
:::

In practice the second factor is read off the reduced population: one fewer A, one fewer individual. The arithmetic is easy; the discipline is remembering that the second denominator is *n* − 1.

What it does not say. It does not say the two draws are independent — they are exactly the standard example of two events that are not. It does not say the effect is always large: taking one record out of 1,000 barely moves the second probability, and Scenario B shows that case honestly, while taking one applicant out of 50 moves it noticeably. And **with** replacement is a different design (1.11.A.2): the individual goes back, the population is restored, and the draws then are independent — which is the only reason the product form ever applies to repeated draws.

*Illustration:* a box of 10 units, 3 of them type A. Two are drawn without replacement. P(first is A) = 3 ÷ 10 = **0.300**; given that, 2 of the remaining 9 are type A, so P(second is A | first is A) = 2 ÷ 9 = **0.222**. Therefore P(both are A) = 0.300 × 0.222 = **0.067**. Treating the draws as independent gives 0.300 × 0.300 = 0.090 — a third too high. And if the first is not type A, P(second is A | first is not A) = 3 ÷ 9 = 0.333, a different number again: that is what "depends on the first" means.

*Education example:* the district's summer school has 50 applicants for 30 places, 14 of them from the two smallest schools, and names are drawn at random without replacement. P(the first name drawn is from a small school) = 14 ÷ 50 = **0.280**. Given that, 13 of the remaining 49 applicants are, so P(the second is too | the first was) = 13 ÷ 49 = **0.265**, and P(both of the first two are from small schools) = 0.280 × 0.265 = **0.074**. Multiplying 0.280 by itself gives 0.078, which overstates it — and the size of the gap is the honest reason the course teaches the general rule rather than the short one.

### Independent events, defined by what knowing one tells you about the other (2.7.A.1)

Events A and B are **independent if and only if** knowing whether A has occurred, or will occur, does not change the probability that B will occur. When A and B are independent,

:::formula
P(A | B) = P(A)   and   P(B | A) = P(B)

Both equalities hold together: if one is true the other is, for events of non-zero probability.
:::

"If and only if" is doing real work in that sentence. It means the equality is not a symptom of independence, it **is** independence; a student who wants to decide whether two events are independent has exactly one thing to do, which is compare a conditional probability with its unconditional partner.

What it does not say. It does not say *unrelated in the world* — independence is a numerical statement about probabilities, and two events can be causally connected in some complicated way and still, in these data, satisfy the equality. It does not say *mutually exclusive*; they are opposites, and the subsection five below proves it. It does not say the two events never occur together — independent events with non-zero probabilities **must** occur together sometimes, since P(A ∩ B) = P(A) × P(B) > 0. And it does not say "approximately equal is good enough": in a table of real counts 0.560 against 0.500 is not independence, and the honest answer is *not independent*, since the framework gives no tolerance (a test for this kind of question arrives in Session 17).

*Illustration:* in Session 9's 30-unit table, P(yes) = 10 ÷ 30 = **0.333**, P(yes | type A) = 4 ÷ 12 = **0.333** and P(yes | type B) = 6 ÷ 18 = **0.333**. Knowing the type tells you nothing about the mark, so "type A" and "yes" are independent. In the 40-unit table they are not: P(yes | A) = 0.750 against P(yes) = 0.550.

*Education example:* the university module's 318 scripts are graded, and then the moderation panel selects **one script in six at random** for remarking. Because the selection is random, P(a script is moderated | it is graded A) = 1 ÷ 6 = **0.167**, which is P(moderated) for every grade. "Graded A" and "selected for moderation" are independent, **by the design of the draw** — randomisation is the one mechanism that guarantees independence rather than merely exhibiting it. Note what independence does not promise: in the realised sample, exactly one in six of the 44 A scripts need not be chosen. Independence is a statement about probabilities, not about counts.

### Deriving the product form, and why it is not a second rule to memorise (2.7.A.1 with 2.6.A.2)

**Have the student write these three lines themselves, now.** They are the whole derivation, and a student who has written them knows when the short rule applies, which a student who has memorised it does not.

1. The general multiplication rule, 2.6.A.2: P(A ∩ B) = P(A) × P(B | A).
2. The definition of independence, 2.7.A.1: if A and B are independent, then P(B | A) = P(B).
3. Substitute the second into the first: P(A ∩ B) = P(A) × P(B).

:::formula
If — and only if — A and B are independent:   P(A ∩ B) = P(A) × P(B)
:::

So the product form is a **theorem**, true exactly when independence holds, and false otherwise. Every prep book prints it as a rule of its own, and the course description does not state it anywhere; what it states is the general rule and the definition. The practical consequence is a two-way street the student should be able to walk in both directions: given independence, multiply; and given a table, comparing P(A) × P(B) against the actual P(A ∩ B) is an equivalent way of testing independence.

What it does not say. It does not license multiplying whenever the word "and" appears, which is the single commonest error on this topic across all three books' practice sets. It does not apply to two draws without replacement. And it is not the definition: a student asked to *define* independent events must give 2.7.A.1's sentence, or P(A | B) = P(A), not the product.

:::note amber The one sentence to write in the margin
**Multiply only when you have the conditional, or when you have checked independence.** P(A) × P(B | A) always works. P(A) × P(B) works only when the second factor has been shown equal to P(B | A).
:::

*Illustration:* in the 30-unit table, P(A) × P(yes) = 0.400 × 0.333 = **0.133**, and the cell gives P(A ∩ yes) = 4 ÷ 30 = **0.133**. Session 9 called that agreement a coincidence of the numbers and refused to use it as a method. It was not a coincidence: the two variables in that table are independent, which is the only circumstance in which the product works, and the student now has the test that shows it. In the 40-unit table the same product gives 0.600 × 0.550 = 0.330 against an actual 0.450, and there it really is wrong.

*Education example:* for the module's scripts, P(graded A) = 44 ÷ 318 = **0.138** and P(moderated) = **0.167**, and since the two are independent by the design of the draw, P(graded A ∩ moderated) = 0.138 × 0.167 = **0.023**. For the district's Year 11 pupils the same move is not available: P(attended) × P(passed) = 0.600 × 0.650 = 0.390, while the actual joint probability is 0.450, so the events are not independent and only the general rule — 0.600 × 0.750 — reaches the right answer.

### Testing independence from a two-way table (2.7.A.1)

A table gives every number needed, so the test is mechanical. Pick a row level and a column level and compare one pair of numbers.

| Step | What to compute | Verdict |
|---|---|---|
| 1 | P(column level) = column total ÷ table total | the unconditional probability |
| 2 | P(column level \| row level) = cell ÷ row total | the conditional probability |
| 3 | compare | equal → independent; unequal → **not independent** |

An equivalent route compares the cell's probability with the product of the two marginals, P(A) × P(B), and reaches the same verdict for the same reason. Either is acceptable; say which you used.

What it does not say. It does not say one comparison settles the whole table — strictly, the two *variables* are independent only if the equality holds for every row and column pair, and when a question asks about two named **events** one comparison is exactly what is wanted. It does not say that counts decide: "there are more bus users in the Villages" is a count, and Session 8 refused that as evidence of association for the same reason. And it does not say that "not independent" means "mutually exclusive" — it almost never does, and for a pair of events that overlap it cannot.

*Illustration:* 30-unit table, P(yes) = 0.333 against P(yes | A) = 0.333: **independent**. 40-unit table, P(yes) = 0.550 against P(yes | A) = 0.750: **not independent**, and the direction is informative too — being type A raises the chance of a yes by 0.200.

*Education example:* for the district's Year 11 pupils, P(passed) = 0.650 and P(passed | attended) = 0.750, so attendance and passing are **not independent** for a randomly chosen pupil: knowing a pupil attended raises the probability of a pass from 0.650 to 0.750. Session 8 reached the same verdict from the same counts and called it an **association**; today's verdict is its probability counterpart. Both stop short of cause, which is Session 7's territory and needs random assignment.

### The union of two events, and the word "or" (2.7.A.2)

The probability that event A **or** event B (**or both**) will occur is the probability of the **union** of A and B, written **P(A ∪ B)**.

:::formula
A ∪ B — the event that A occurs, or B occurs, or both
:::

Read ∪ as "union" or as "or". The parenthesis in the framework's sentence is the point: the statistical *or* is **inclusive**, so the union contains the individuals in A alone, the individuals in B alone, and the individuals in both. Everyday English often means the exclusive *or* — "tea or coffee" from a waiter does not invite both — and that is where the misreading comes from.

What it does not say. It does not exclude the overlap, so *"bus or Villages"* includes the students who are both. It is not the intersection: A ∪ B is at least as probable as either event alone, while A ∩ B is at most as probable as either; if a student's union comes out smaller than P(A), they have computed the wrong thing. And it is itself just an event, so Session 9's counting applies — the union can always be counted directly off a table, which is what Session 9 did.

*Illustration:* in the 40-unit table, A ∪ yes is the 24 type A units together with the 4 type B units marked yes — 28 units in all, so P(A ∪ yes) = 28 ÷ 40 = **0.700**. Note that it is bigger than P(A) = 0.600 and bigger than P(yes) = 0.550, as a union must be.

*Education example:* for a district Year 11 pupil, *"attended the revision programme or passed"* collects the 180 who did both, the 60 who attended without passing and the 80 who passed without attending: 320 pupils, so P(attended ∪ passed) = 320 ÷ 400 = **0.800**. Only the 80 pupils who neither attended nor passed are outside the union — which is a useful way to describe what a union is.

### The probability of a union, and the outcomes counted twice (2.7.A.3)

The probability of the union is the sum of the two probabilities minus the probability of the intersection.

:::formula
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

P(A) + P(B) — counts every individual in the overlap twice
P(A ∩ B) — the overlap, subtracted once to correct that
:::

This is the rule Session 9 deliberately withheld. At Lincoln High it counted 695 students in "bus or Villages" by hand and then pointed at the 250 in the overlap as the students the next session's rule would subtract. That is this rule, and the subtraction is the entire content of it.

What it does not say. It does not say P(A) + P(B); that is right only when P(A ∩ B) = 0, which is Session 9's **mutually exclusive** (2.5.A.2) and is therefore the special case rather than the norm. It does not fail when the events are mutually exclusive — the rule still holds, it just subtracts zero, so there is only one rule to remember. And it gives no licence to add more than two probabilities without thought: three events have overlaps between every pair, and the course description does not ask for that case.

The giveaway that a student has added without subtracting is a probability above 1, which Session 9's 0-to-1 bound (2.4.A.3) catches for free. It does not always fire — 0.513 at Lincoln High is a perfectly respectable-looking wrong answer — so the habit has to be structural: **whenever you add two probabilities, say out loud whether the events can both happen.**

*Illustration:* 40-unit table. P(A) + P(yes) = 0.600 + 0.550 = 1.150, which is already impossible. Subtract the overlap: 1.150 − 0.450 = **0.700**, matching the 28 units counted directly. The 18 units in the cell were counted once in the 24 and once in the 22.

*Education example:* for a district Year 11 pupil, P(attended) + P(passed) = 0.600 + 0.650 = 1.250 — impossible, and caught by the bound. The correct value is 0.600 + 0.650 − 0.450 = **0.800**, which matches the 320 pupils counted. The 180 who both attended and passed are the ones the naive sum counted twice, and 1.250 − 0.800 = 0.450 is exactly their joint probability.

### Mutually exclusive against independent: why no pair with non-zero probability is both (2.5.A.2, 2.6.A.1, 2.7.A.1)

The two ideas use different machinery and answer different questions, and students fuse them because both sentences begin "the two events are…". Session 9 warned about it; here is the proof, which fits in two lines and uses nothing outside 2.5.A.2, 2.6.A.1 and 2.7.A.1.

Suppose P(A) > 0, P(B) > 0, and A and B are mutually exclusive. Then:

1. Mutually exclusive means P(A ∩ B) = 0 (2.5.A.2).
2. So P(A | B) = P(A ∩ B) ÷ P(B) = 0 ÷ P(B) = **0** (2.6.A.1).
3. But independence would require P(A | B) = P(A), and P(A) > 0 (2.7.A.1).

Since 0 ≠ P(A), the two events are **not** independent. Mutually exclusive events are the most dependent pair there is: learning that B happened tells you with certainty that A did not.

| | Mutually exclusive | Independent |
|---|---|---|
| The question it answers | can they both happen? | does knowing one change the other? |
| The test | P(A ∩ B) = 0 | P(A \| B) = P(A) |
| Typical pair | two levels of the **same** variable | one level from **each** of two variables |
| If one occurs | the other certainly did not | the other's probability is unchanged |
| Both at once | impossible, unless one of them has probability 0 | |

What it does not say. It does not say *every* pair is one or the other: most pairs are **neither**, which is what Lincoln High's Villages and bus turn out to be, and "neither" is the commonest verdict in real data. It does not say the two tests are alternatives for the same question — a complete answer about a pair of events may need both. And the exception at the bottom of the table is genuine but empty in practice: an event of probability 0 is trivially both, which is why the framework's examples and every exam question specify non-zero probabilities.

*Illustration:* in the 40-unit table, "type A" and "type B" are mutually exclusive, so P(A | B) = 0 while P(A) = 0.600 — not independent. "Type A" and "yes" are not mutually exclusive, since P(A ∩ yes) = 0.450, and not independent either, since 0.750 ≠ 0.550: **neither**. In the 30-unit table, "type A" and "yes" are independent and not mutually exclusive.

*Education example:* for a module script, "graded A" and "graded B" are mutually exclusive (one grade per script, so P of the intersection is 0) and therefore certainly not independent — learning that a script was graded A drops the probability that it was graded B from 0.292 to 0.000. "Graded A" and "selected for moderation" are independent and not mutually exclusive, since both can happen and P of the intersection is 0.023. And "attended the revision programme" and "passed", for a district pupil, are neither. Three pairs, three verdicts, and no pair in the fourth box.

### Which rule the question is asking for: a decision list (2.6–2.7)

The activity drills recognition; this is the list it drills. Read the question, find the word, pick the rule.

| The question says | What is wanted | Rule | Code |
|---|---|---|---|
| "and", "both" | the joint probability | the cell ÷ table total, or P(A) × P(B \| A) | 2.5.A.1, 2.6.A.2 |
| "given", "of the …", "among", "for those who" | a conditional probability | the cell ÷ the conditioning total | 2.6.A.1 |
| "or", "at least one of the two" | the union | P(A) + P(B) − P(A ∩ B) | 2.7.A.3 |
| "not", "none", "at least one" (of several) | a complement | 1 − P(E) | 2.4.A.4 |
| "are they independent?" | compare two numbers | P(A \| B) against P(A) | 2.7.A.1 |
| "can they both happen?" | one number | P(A ∩ B), and whether it is 0 | 2.5.A.2 |
| two draws, nothing returned | the general multiplication rule | P(A) × P(B \| A), second denominator *n* − 1 | 2.6.A.2, 1.11.A.1 |

What it does not say. It does not say the words are infallible: *"what proportion of the bus users live in the Villages"* contains no "given" and is still a conditional probability, because "of the bus users" names the group. The reliable question is always **which group is this probability about?**

*Illustration:* "Of the type A units, what share are yes?" → conditional, 18 ÷ 24. "What is the probability a unit is type A and yes?" → joint, 18 ÷ 40. "Type A or yes?" → union, 0.700. Same table, three words, three denominators.

*Education example:* the district's four questions about Year 11, in the order a report would ask them. *"What share of our pupils both attended and passed?"* → joint, 0.450. *"Of the attenders, what share passed?"* → conditional, 0.750. *"What share attended, passed, or both?"* → union, 0.800. *"Does attending change the chance of passing?"* → an independence comparison, 0.750 against 0.650.

### Seven check questions before the scenarios

Ask all seven. If any goes wrong, reread that subsection's "what it does not say" paragraph before Scenario A. Checks 3 to 6 use the 40-unit table.

**C1.** *"Write the definition of P(A | B), and say what the bar means."*
→ *P(A | B) = P(A ∩ B) ÷ P(B). The bar reads "given"; it is not division, and P(B) must not be 0 (2.6.A.1).*

**C2.** *"In a two-way table, what is the difference between P(A ∩ B) and P(B | A)?"*
→ *The same cell over two different totals: the table total for the joint probability, the A row's total for the conditional (2.6.A.1).*

**C3.** *"Give me P(yes | type A) and P(type A | yes) from the 40-unit table."*
→ *18 ÷ 24 = 0.750 and 18 ÷ 22 = 0.818. Different denominators, different numbers (2.6.A.1).*

**C4.** *"State the general multiplication rule, and then derive the version for independent events."*
→ *P(A ∩ B) = P(A) × P(B | A) (2.6.A.2). If A and B are independent then P(B | A) = P(B) (2.7.A.1), so substituting gives P(A ∩ B) = P(A) × P(B). The short form is a consequence, not a separate rule.*

**C5.** *"Are 'type A' and 'yes' independent in the 40-unit table? Show your test."*
→ *No. P(yes) = 22 ÷ 40 = 0.550 and P(yes | A) = 18 ÷ 24 = 0.750; the two are unequal, so the events are not independent (2.7.A.1).*

**C6.** *"P(A) = 0.600, P(yes) = 0.550, P(A ∩ yes) = 0.450. What is P(A ∪ yes), and why is it not 1.150?"*
→ *0.600 + 0.550 − 0.450 = 0.700. The 18 units in the overlap are counted in both totals, so one copy is subtracted; 1.150 is above 1 and so cannot be a probability (2.7.A.3, 2.4.A.3).*

**C7.** *"Can two events with non-zero probability be both mutually exclusive and independent? Prove your answer."*
→ *No. Mutually exclusive gives P(A ∩ B) = 0, so P(A | B) = 0 ÷ P(B) = 0; independence would need P(A | B) = P(A), which is greater than 0. The two cannot hold together (2.5.A.2, 2.6.A.1, 2.7.A.1).*

---

## 56–90 min · Scenario A — Lincoln High's register: the probability of bus given the Villages

Lincoln High's travel register, unchanged since Session 8: a **census** of all **1,842 students**, each recorded with a home area and a main travel mode. Session 9 read it as probabilities for one student chosen at random from the whole roll, with 1,842 underneath every fraction. Today the office starts asking questions about **parts** of the roll, and the denominator moves.

**The trap this scenario carries: P(A | B) answered with P(B | A).** The two numbers are both in the table, both look like reasonable answers, and the student has already met both — 0.850 as Session 8's conditional relative frequency and 0.384 as the one the homework kept confusing it with. The error is not arithmetic. It is answering a question about bus users when the question was about Villages students, and the fix is the habit Session 8 installed: name the group after "of" before writing the fraction.

### The register again, now with the row total as a denominator

| Home area | Bus | Car | Walk or cycle | Total |
|---|---|---|---|---|
| Town, within 3 km | 85 | 203 | 558 | 846 |
| Suburbs, 3 to 10 km | 316 | 281 | 105 | 702 |
| Villages, beyond 10 km | 250 | 38 | 6 | 294 |
| **Total** | **651** | **522** | **669** | **1,842** |

:::checks
row totals 846 + 702 + 294 = 1,842
column totals 651 + 522 + 669 = 1,842
:::

:::script
ask | Ask | "Session 9 gave P(bus) = 0.353 and P(Villages ∩ bus) = 0.136. What was underneath both of those?"
listen | Listen for | 1,842 — the whole roll, because one student was chosen at random from all of them.
intro | Recall | *Why the denominator changes: a cell over a row total (2.6.A.1)*: the cell stays, the total moves.
ask | Ask | "Now the office asks: of the students who live in the Villages, what is the probability that one chosen at random travels by bus? Which total goes underneath?"
listen | Listen for | 294, the Villages row total — because the group named after "of" is the Villages students.
ask | Ask | "Write it in notation before you divide."
listen | Listen for | P(bus | Villages), with B = travels mainly by bus and V = lives in the Villages. Then 250 ÷ 294 = 0.850.
ifsay | If they write 250 ÷ 1,842 | "Read your own answer back as a sentence beginning 'of the'. Of the what? That fraction is about all 1,842 students."
ask | Ask | "Have you seen 0.850 before?"
listen | Listen for | Session 8, as a conditional relative frequency: 85.0% of Villages students take the bus. Same arithmetic, new name and new notation.
:::

> **The sentence to write down:** *P(A | B) is the same cell as P(A ∩ B) with a different number underneath: the total of the group being conditioned on, not the table total. Say "of the …" out loud first, and the denominator chooses itself.*

### P(bus | Villages) and the general multiplication rule on the same cell

:::script
ask | Ask | "Check 0.850 against the definition instead of the table. What do you need?"
listen | Listen for | P(A | B) = P(A ∩ B) ÷ P(B), so P(bus | Villages) = 0.136 ÷ 0.160 = 0.850 — the joint probability over the probability of the condition.
intro | Recall | *Conditional probability: the probability of A given B (2.6.A.1)*.
ask | Ask | "Now run it backwards. If I give you P(Villages) and P(bus | Villages), how do you get the joint probability?"
listen | Listen for | P(V ∩ B) = P(V) × P(B | V) = 0.160 × 0.850 = 0.136, which is the cell, 250 ÷ 1,842.
intro | Recall | *The general multiplication rule (2.6.A.2)*: the definition with the denominator moved across.
ask | Ask | "Do it in the other order as a check."
listen | Listen for | P(V ∩ B) = P(B) × P(V | B) = 0.353 × 0.384 = 0.136. Same answer; the rule does not care which event is called A.
ask | Ask | "Session 9 asked you whether 0.353 × 0.160 = 0.056 was the joint probability. Now say exactly why it was not."
listen | Listen for | Because that is P(V) × P(B), the product form, which needs independence — and P(bus | Villages) = 0.850 is nowhere near P(bus) = 0.353, so the condition fails.
intro | Recall | *Deriving the product form, and why it is not a second rule to memorise (2.7.A.1 with 2.6.A.2)*.
ask | Ask | "Give me P(bus | Town) and P(bus | Suburbs) as well."
listen | Listen for | 85 ÷ 846 = 0.100 and 316 ÷ 702 = 0.450. Three home areas, three very different conditional probabilities.
:::

### The governor's "0.850 of bus users live in the Villages"

This is the trap. A school governor, given the figure, writes to the county:

> *"The register shows that 0.850 of our bus users live in the Villages, so the village routes carry nearly the whole bus service."*

:::script
ask | Ask | "Is the governor's sentence true? Which probability has been quoted?"
listen | Listen for | It is false as written. 0.850 is P(bus | Villages) — of the Villages students, the probability of the bus. The governor's sentence is P(Villages | bus), which is a different number.
intro | Recall | *P(A | B) and P(B | A) are different numbers (2.6.A.1)*.
ask | Ask | "Compute what the governor actually claimed."
listen | Listen for | P(Villages | bus) = 250 ÷ 651 = 0.384. Of the 651 bus users, 38.4% live in the Villages — well under half.
ask | Ask | "Same numerator both times. What changed?"
listen | Listen for | The denominator: 294 Villages students for one, 651 bus users for the other. The same 250 students, divided by two different groups.
ifsay | If "so which one is right?" | "Both are right answers to different questions. The governor asked a question about bus users and read the answer to a question about Villages students."
ask | Ask | "How much damage does it do? Write the true sentence for each number."
listen | Listen for | *"Of the students who live in the Villages, 85.0% travel by bus"* and *"of the students who travel by bus, 38.4% live in the Villages."* The governor's funding case rests on the second and quotes the first, which is more than twice as large.
ask | Ask | "Is there any rule in this course that turns 0.850 into 0.384?"
listen | Listen for | No. You go back to the table and divide the same 250 by the other total. There is no formula for reversing a conditional in this course.
:::

:::note amber Where this error has already cost marks, and where it will again
This is the third appearance of the same slip. Session 8's homework B3 asked for 42 ÷ 70 and 42 ÷ 95 and many students gave one number twice; Session 9's diagnostic asked for 250 ÷ 294 and 250 ÷ 651; today it has notation and a name. It returns in Session 17, where a chi-square table of counts has to be read as conditional distributions in a stated direction, and on any exam question whose stem begins *"of those who …"*. The permanent fix is mechanical: **underline the group named after "of" in the question, then find its total.**
:::

### Is travelling by bus independent of living in the Villages?

:::script
ask | Ask | "The county now asks whether travel mode is independent of home area. What exactly do you compare?"
listen | Listen for | P(bus | Villages) against P(bus): 0.850 against 0.353. They are not equal, so the two events are not independent.
intro | Recall | *Testing independence from a two-way table (2.7.A.1)*: conditional against unconditional, cell ÷ row total against column total ÷ table total.
ask | Ask | "Say what that means in words, for one student."
listen | Listen for | Knowing a student lives in the Villages raises the probability they travel by bus from 0.353 to 0.850 — knowing about one event changes the other, which is exactly what independence rules out.
ask | Ask | "Test it the other way, with the product."
listen | Listen for | P(V) × P(B) = 0.160 × 0.353 = 0.056, against the actual P(V ∩ B) = 0.136. Unequal, so not independent — the same verdict by the equivalent route.
ask | Ask | "Session 9 said these two events were not mutually exclusive. Are they independent, then?"
listen | Listen for | No. They are **neither**: 250 students are in both, so not mutually exclusive, and 0.850 ≠ 0.353, so not independent. Most pairs of events are in that box.
intro | Recall | *Mutually exclusive against independent: why no pair with non-zero probability is both (2.5.A.2, 2.6.A.1, 2.7.A.1)*.
ask | Ask | "Give me a pair from this table that **is** mutually exclusive, and show what its conditional probability does."
listen | Listen for | "Lives in Town" and "lives in the Villages": P(Town ∩ Villages) = 0, so P(Town | Villages) = 0 ÷ 0.160 = 0, against P(Town) = 0.459. Mutually exclusive, and therefore as far from independent as a pair can be.
ask | Ask | "Is there any pair here you would expect to be independent?"
listen | Listen for | None of them, and the data agree: every home area has a different bus probability — 0.100, 0.450, 0.850. Home area and travel mode are strongly associated, which Session 8 established from the same counts.
:::

> **The rule to write down:** *Mutually exclusive asks whether both can happen; independent asks whether one changes the other. A pair can be neither — and at Lincoln High, every pair of one home area with one travel mode is.*

### "Bus or Villages": the union Session 9 counted and could not yet calculate

:::script
ask | Ask | "Session 9 counted the students who travel by bus or live in the Villages, straight off the table. Do that count again."
listen | Listen for | The three bus cells, 85 + 316 + 250 = 651, plus the two remaining Villages cells, 38 + 6 = 44, giving 695 students, so 695 ÷ 1,842 = 0.377.
ask | Ask | "Now reach the same answer from P(bus), P(Villages) and P(bus ∩ Villages)."
listen | Listen for | P(V ∪ B) = 0.160 + 0.353 − 0.136 = 0.377. The rule and the count agree.
intro | Recall | *The probability of a union, and the outcomes counted twice (2.7.A.3)*.
ask | Ask | "What are the 250 students doing in that subtraction?"
listen | Listen for | They were counted once inside the 294 Villages students and once inside the 651 bus users, so one copy has to be removed. 0.160 + 0.353 = 0.513 counts them twice, and 0.513 − 0.136 = 0.377.
ifsay | If "but 0.513 looks like a probability" | "It does, and that is the problem — the 0-to-1 bound does not catch this one. Count 695 out of 1,842 and compare. How many students does 0.513 claim? 945. Where would the extra 250 come from?"
ask | Ask | "Does 'or' here include the students who are both?"
listen | Listen for | Yes — the statistical "or" is inclusive, so the union contains the 250 who live in the Villages and take the bus.
intro | Recall | *The union of two events, and the word "or" (2.7.A.2)*.
ask | Ask | "Try the rule on a pair that is mutually exclusive: P(lives in Town ∪ lives in the Villages)."
listen | Listen for | 0.459 + 0.160 − 0 = 0.619, which matches 846 + 294 = 1,140 over 1,842. The rule still applies; it just subtracts zero.
:::

### The sentence the office may now write

:::script
ask | Ask | "One paragraph for the governors, using today's rules. Write it."
listen | Listen for | Something like: *"Of Lincoln High's 294 students who live in the Villages, the probability that one chosen at random travels by bus is 250 ÷ 294 = 0.850. Of the 651 students who travel by bus, the probability that one lives in the Villages is 250 ÷ 651 = 0.384; the two figures answer different questions. Travel mode is not independent of home area: the probability of travelling by bus rises from 0.353 for a student chosen from the whole roll to 0.850 for a Villages student. The probability that a randomly chosen student travels by bus or lives in the Villages, or both, is 0.353 + 0.160 − 0.136 = 0.377."*
ask | Ask | "What may the paragraph still not claim?"
listen | Listen for | That living in the Villages **causes** bus use — this is observational data with no random assignment (Session 7); that the figures apply to any other school (Session 6); and that 0.850 and 0.384 are interchangeable.
ask | Ask | "Which number would you give the county if they asked how many buses the village routes need?"
listen | Listen for | Neither on its own — they want the count, 250 students. A conditional probability answers a question about a chosen individual, not a question about capacity, and saying which is which is half the skill.
:::

---

## 90–110 min · Activity — twelve event pairs: independent, mutually exclusive, both or neither

The master plan's activity for this session, adapted from 5 Steps content tip 14: sort event pairs into four boxes, then answer the question that resolves the confusion for good. Pairs become **one-to-one** the way the conversion table prescribes — the student sorts and justifies every pair aloud, and the tutor probes **every** answer, including the correct ones, so that a right verdict reached by the wrong route is caught.

Two things to know before you start. The fourth box, *both*, stays **empty**, and that is the designed outcome rather than a flaw in the pairs. And the library's table turns out to be exactly independent throughout, which makes it the only context in the course where the equality actually holds — so it does most of the work in the independent box.

### Three Think-Pair-Share cards, named but not calculated

The course description's Sample Instructional Activity for topics 2.4 to 2.7 is Think-Pair-Share: five probability questions, one each for the complement rule, a mutually exclusive event, a conditional probability, the general multiplication rule and an independent event, with students naming only the formula needed. Session 9 ran the first two cards. **These are the other three**, four minutes as a warm-up, on the library table below. No calculation: name the rule, its code, and which numbers would go into it.

| Card | The rule to name | The numbers they would use | Code |
|---|---|---|---|
| *"Of the Central members, what is the probability that the chosen member borrows e-books only?"* | conditional probability, P(A \| B) = P(A ∩ B) ÷ P(B) | 15 over the Central row total, 150 | 2.6.A.1 |
| *"What is the probability that the chosen member is from Central **and** borrows both formats?"* | the general multiplication rule, P(A) × P(B \| A) — or the cell over 250 | 0.600 × (45 ÷ 150), or 45 over 250 | 2.6.A.2 |
| *"Is 'borrows both formats' independent of branch?"* | the definition of independence: compare P(both \| Central) with P(both) | 45 ÷ 150 against 75 ÷ 250 | 2.7.A.1 |

If they calculate anyway, let them finish and then ask for the rule and its code; recognition is the skill being drilled, and a student who can only get there through the arithmetic has not got there. For your reference the three answers are 0.100, 0.180 and yes, independent.

### The twelve pairs, and the four boxes to sort them into

Three tables, all seen before. One individual is chosen at random from each.

**The library service's sample of 250 members** (Session 8's solo case, Session 9's activity):

| Branch | Print only | E-books only | Both | Total |
|---|---|---|---|---|
| Central | 90 | 15 | 45 | **150** |
| Westside | 60 | 10 | 30 | **100** |
| **Total** | **150** | **25** | **75** | **250** |

**Lincoln High's travel register**, as in Scenario A, and **one roll of a fair six-sided die**.

Hand over the twelve pairs and four headed boxes — *independent* · *mutually exclusive* · *both* · *neither*. The student sorts, then justifies each with a number.

| | The pair | Source |
|---|---|---|
| 1 | "a Central member" and "borrows print only" | library |
| 2 | "a Westside member" and "borrows both formats" | library |
| 3 | "a Central member" and "borrows e-books, in either form" | library |
| 4 | "the roll is even" and "the roll is greater than 4" | die |
| 5 | "a Central member" and "a Westside member" | library |
| 6 | "borrows print only" and "borrows e-books only" | library |
| 7 | "lives in Town" and "lives in the Suburbs" | Lincoln High |
| 8 | "the roll is a 2" and "the roll is a 5" | die |
| 9 | "lives in the Villages" and "travels by bus" | Lincoln High |
| 10 | "lives in Town" and "walks or cycles" | Lincoln High |
| 11 | "lives in the Suburbs" and "travels by bus" | Lincoln High |
| 12 | "borrows print, in either form" and "borrows e-books, in either form" | library |

### Marking the sort, one pair at a time

Probe every pair, including the ones they placed correctly: ask for the two numbers, not the verdict. The intersection decides *mutually exclusive*; the comparison decides *independent*; a pair needs both tests before it can be called *neither*.

| Pair | Verdict | The numbers that decide it |
|---|---|---|
| 1 | **Independent** | P(print only) = 150 ÷ 250 = 0.600; P(print only \| Central) = 90 ÷ 150 = 0.600. Equal. Not mutually exclusive: 90 members are both |
| 2 | **Independent** | P(both formats) = 75 ÷ 250 = 0.300; P(both formats \| Westside) = 30 ÷ 100 = 0.300. Equal |
| 3 | **Independent** | P(borrows e-books) = (25 + 75) ÷ 250 = 0.400; given Central, (15 + 45) ÷ 150 = 0.400. Equal |
| 4 | **Independent** | P(even) = 0.500; P(even \| greater than 4) = P(6) ÷ P(5 or 6) = 1 ÷ 2 = 0.500. Equal, and the 6 is in both, so not mutually exclusive |
| 5 | **Mutually exclusive** | each member belongs to one branch, so P(Central ∩ Westside) = 0, and P(Central \| Westside) = 0 against P(Central) = 0.600 |
| 6 | **Mutually exclusive** | "print only" excludes e-books by definition, so the intersection is empty: P = 0 |
| 7 | **Mutually exclusive** | each student has exactly one home area: P(Town ∩ Suburbs) = 0 |
| 8 | **Mutually exclusive** | one roll gives one face: P = 0, and P(2 \| 5) = 0 against P(2) = 0.167 |
| 9 | **Neither** | P(V ∩ bus) = 250 ÷ 1,842 = 0.136, not 0, so not mutually exclusive; P(bus \| V) = 0.850 against P(bus) = 0.353, so not independent |
| 10 | **Neither** | P(Town ∩ walk) = 558 ÷ 1,842 = 0.303, not 0; P(walk \| Town) = 558 ÷ 846 = 0.660 against P(walk) = 669 ÷ 1,842 = 0.363 |
| 11 | **Neither** | P(Suburbs ∩ bus) = 316 ÷ 1,842 = 0.172, not 0; P(bus \| Suburbs) = 316 ÷ 702 = 0.450 against 0.353 |
| 12 | **Neither** | P(print ∩ e-books) = P(borrows both formats) = 0.300, not 0; P(print \| e-books) = 75 ÷ 100 = 0.750 against P(print) = 225 ÷ 250 = 0.900 |
| | **Both** | **empty** |

**Four in each of three boxes, and nothing in the fourth.** Three things to say while marking:

- Pairs 5 to 8 are all **two levels of one variable**, which is where mutually exclusive pairs almost always come from. Pairs 1 to 4 and 9 to 11 take one level from each of two variables, which is where independence and "neither" live.
- Pair 12 is the one worth the most time. Both events come from the **same** variable, and they still overlap, because "borrows print" and "borrows e-books" both include the 75 members who do both. A student who sorted it as mutually exclusive has read "print" as "print only"; a student who sorted it as independent has not compared 0.750 with 0.900.
- The library pairs are independent and the Lincoln High pairs are not, and the student should be able to say why that is a fact about the data rather than about the subject: the library's branches happen to have identical borrowing profiles, and Lincoln High's home areas have very different travel profiles.

:::note amber The two wrong routes to a right verdict
A student can place pair 5 in *mutually exclusive* because "a member can only be in one branch" — correct, and worth full credit. A student can place pair 1 in *independent* because "branch and format sound unrelated" — the right box for the wrong reason, and it will fail on pair 9, where the words also sound unrelated and the numbers say otherwise. Ask for the numbers on every pair, including the easy ones.
:::

### The question that settles it: why "both" is empty

:::script
ask | Ask | "Your *both* box is empty. Prove that it has to be, for any two events with non-zero probability."
listen | Listen for | If they are mutually exclusive, P(A ∩ B) = 0, so P(A | B) = 0 ÷ P(B) = 0; independence needs P(A | B) = P(A), which is greater than 0; so the two cannot hold together.
intro | Recall | *Mutually exclusive against independent: why no pair with non-zero probability is both (2.5.A.2, 2.6.A.1, 2.7.A.1)*.
ask | Ask | "Say it without symbols, in one sentence."
listen | Listen for | If two events cannot both happen, then learning that one happened tells you the other certainly did not — which is the largest possible change to its probability, and independence means no change at all.
ask | Ask | "Run it the other way. If A and B are independent and both have non-zero probability, can they be mutually exclusive?"
listen | Listen for | No: P(A ∩ B) = P(A) × P(B), which is a product of two positive numbers, so it cannot be 0. Independent events with non-zero probability must overlap.
ask | Ask | "Where does the 'non-zero' get used?"
listen | Listen for | At the last step: if P(A) were 0, then P(A | B) = 0 = P(A) and the pair would be both, trivially. Every exam question specifies positive probabilities, which is why.
ask | Ask | "Which box was the biggest, and should that surprise you?"
listen | Listen for | *Neither* and *mutually exclusive* and *independent* came out level here at four each, because the pairs were chosen to. In real data *neither* is much the largest — most pairs of events overlap and influence one another.
:::

---

## 110–142 min · Scenario B — St Mary's clinic: unions, and an audit of two records

St Mary's outpatient clinic from Sessions 6 to 9. Session 9 built the sample space of one appointment from the clinic's **1,000 records** and cross-tabulated them by whether the appointment was a patient's **first** or a **follow-up**. The manager now wants two things Session 9 could not supply: the probability that an appointment is *either* a first appointment *or* a missed one, and the probability that two records pulled for audit are both missed appointments.

**The trap this scenario carries: a union computed as a sum.** Session 9 set it up deliberately and named the students who would be counted twice; here the clinic's own administrator makes the error on the clinic's own numbers, and the wrong answer, 0.500, is a perfectly plausible-looking probability that the 0-to-1 bound will not catch. The second half of the scenario carries a quieter companion: two draws treated as independent when the first draw changes the second.

### The appointment table, conditioned on first appointment or follow-up

| | On time | Late | Cancelled in advance | Missed without notice | Total |
|---|---|---|---|---|---|
| First appointment | 280 | 32 | 28 | 60 | **400** |
| Follow-up | 490 | 38 | 32 | 40 | **600** |
| **Total** | **770** | **70** | **60** | **100** | **1,000** |

:::checks
row totals 400 + 600 = 1,000
column totals 770 + 70 + 60 + 100 = 1,000
the eight cells are mutually exclusive and cover all 1,000 records
:::

:::script
ask | Ask | "Session 9 left a question hanging on this table: is a first appointment more likely to be missed than a follow-up? You can answer it now. What do you compute?"
listen | Listen for | P(missed | first) = 60 ÷ 400 = 0.150 and P(missed | follow-up) = 40 ÷ 600 = 0.067. Two conditional probabilities, each a cell over its own row total.
intro | Recall | *Why the denominator changes: a cell over a row total (2.6.A.1)*.
ask | Ask | "So what is the answer, in a sentence the manager can use?"
listen | Listen for | Of first appointments, 15.0% are missed without notice; of follow-ups, 6.7%. A first appointment is more than twice as likely to be missed.
ask | Ask | "Now P(first | missed). Which total, and what does it mean?"
listen | Listen for | 60 ÷ 100 = 0.600. Of the 100 missed appointments, 60 were first appointments.
intro | Recall | *P(A | B) and P(B | A) are different numbers (2.6.A.1)*.
ask | Ask | "0.150 and 0.600 come from the same 60 records. Which one tells the manager whether to send extra reminders to new patients?"
listen | Listen for | 0.150 — it is about the risk attached to a first appointment. 0.600 describes who the missed appointments were, which is a different fact and is also useful, for deciding where the losses are concentrated.
ifsay | If they cannot separate them | "Write both sentences out in full, starting 'of the'. Of the 400 first appointments… of the 100 missed appointments…"
ask | Ask | "Check 0.150 against the definition."
listen | Listen for | P(missed ∩ first) ÷ P(first) = 0.060 ÷ 0.400 = 0.150.
ask | Ask | "And give me the joint probability from the general multiplication rule."
listen | Listen for | P(first) × P(missed | first) = 0.400 × 0.150 = 0.060, the cell over 1,000.
intro | Recall | *The general multiplication rule (2.6.A.2)*.
:::

### The administrator's 0.500 for "a first appointment or a missed one"

The clinic's administrator, asked how often an appointment is either a first appointment or a missed one, writes:

> *"P(first) = 0.400 and P(missed) = 0.100, so P(first or missed) = 0.500. Half of all appointments are either a new patient or a no-show."*

:::script
ask | Ask | "Is 0.500 right? Settle it by counting before you use any rule."
listen | Listen for | No. Count the records: 400 first appointments plus the 40 missed follow-ups = 440, so the probability is 0.440, not 0.500.
ask | Ask | "Where did the extra 0.060 come from?"
listen | Listen for | The 60 records that are both a first appointment and a missed one. They are inside the 400 and inside the 100, so the sum counts them twice.
intro | Recall | *The probability of a union, and the outcomes counted twice (2.7.A.3)*.
ask | Ask | "Write the rule and apply it."
listen | Listen for | P(first ∪ missed) = P(first) + P(missed) − P(first ∩ missed) = 0.400 + 0.100 − 0.060 = 0.440, matching the count.
ask | Ask | "Why did the 0-to-1 bound not catch this error?"
listen | Listen for | Because 0.500 is a legal probability. The bound only catches a double count when the sum exceeds 1, as it did on Session 9's library card. Here nothing looks wrong, which is why the check has to be the question *can both happen?* rather than *does the answer look sensible?*
intro | Recall | *Probability is a number from 0 to 1, inclusive (2.4.A.3)* — Session 9's bound is a safety net, not the test.
ask | Ask | "The administrator's sentence also says 'either … or'. Does the clinic's 0.440 include the 60?"
listen | Listen for | Yes. The statistical "or" is inclusive: A ∪ B contains A alone, B alone and both.
intro | Recall | *The union of two events, and the word "or" (2.7.A.2)*.
ifsay | If they want the exclusive version | "Then you would subtract the overlap twice: 0.440 − 0.060 = 0.380, the records that are one but not the other. Legitimate arithmetic, but it is not what P(A ∪ B) means, and no exam question asks for it under that name."
:::

> **The check to write down:** *Before adding two probabilities, ask whether the two events can both happen. If they can, subtract the joint probability once. A sum that stays under 1 is not evidence that it was right.*

### Which of the clinic's pairs may simply be added

:::script
ask | Ask | "Give me P(cancelled in advance ∪ missed without notice)."
listen | Listen for | 0.060 + 0.100 = 0.160, and no subtraction, because an appointment cannot be both: P(cancelled ∩ missed) = 0. Check: 60 + 100 = 160 records over 1,000.
intro | Recall | *Mutually exclusive, or disjoint, events (2.5.A.2)* from Session 9, and the union rule subtracting zero.
ask | Ask | "So is there a second rule for mutually exclusive events?"
listen | Listen for | No — one rule. P(A) + P(B) − P(A ∩ B) with P(A ∩ B) = 0 is P(A) + P(B). The special case is the general rule with a zero in it.
ask | Ask | "Session 9 asked you for P(attended), the patient who came on time or late. Which kind of calculation was that?"
listen | Listen for | A union of two mutually exclusive outcomes: 0.770 + 0.070 = 0.840, with nothing to subtract — which is why Session 9 could do it without today's rule.
ask | Ask | "Now a harder one: P(attended ∪ first appointment)."
listen | Listen for | P(attended) = 0.840, P(first) = 0.400, and the overlap is the first appointments that were attended: 280 + 32 = 312, so 0.312. The union is 0.840 + 0.400 − 0.312 = 0.928. Check by counting: 840 + 400 − 312 = 928 records.
ifsay | If they add to 1.240 | "You have just claimed a probability above 1. Which records did you count twice?" The 312.
ask | Ask | "Is 'attended' independent of 'first appointment'?"
listen | Listen for | No. P(attended | first) = 312 ÷ 400 = 0.780 against P(attended | follow-up) = 528 ÷ 600 = 0.880 and P(attended) = 0.840. Knowing it is a first appointment lowers the probability of attendance.
intro | Recall | *Testing independence from a two-way table (2.7.A.1)*.
:::

### Are missed appointments independent of first appointments?

:::script
ask | Ask | "State the independence question for this table precisely, then answer it."
listen | Listen for | Are "first appointment" and "missed without notice" independent? Compare P(missed | first) = 0.150 with P(missed) = 0.100. Not equal, so not independent.
ask | Ask | "Check it with the product form as well, and say why you are allowed to use the product as a test but not as a method."
listen | Listen for | P(first) × P(missed) = 0.400 × 0.100 = 0.040, against the actual joint probability 0.060. As a **test** the mismatch is the evidence; as a **method** it would have given 0.040, which is wrong by a third, because the product form requires the independence it is being used to check.
intro | Recall | *Deriving the product form, and why it is not a second rule to memorise (2.7.A.1 with 2.6.A.2)*.
ask | Ask | "Three verdicts on one pair of events, then: mutually exclusive, independent, neither. Which, and with what evidence?"
listen | Listen for | Neither. P(first ∩ missed) = 0.060 ≠ 0, so not mutually exclusive; P(missed | first) = 0.150 ≠ 0.100 = P(missed), so not independent.
ask | Ask | "And a pair here that is mutually exclusive, with its conditional probability?"
listen | Listen for | "Cancelled in advance" and "missed without notice": P of the intersection is 0, so P(cancelled | missed) = 0 against P(cancelled) = 0.060. Or "first appointment" and "follow-up".
ask | Ask | "What should the clinic actually do with 0.150 against 0.100?"
listen | Listen for | Target reminders at first appointments — and say explicitly that this is an association in observational records, not a demonstration that being a new patient causes the no-show. Session 7's rule: no random assignment, no cause.
:::

### Two records drawn for audit, without replacement

The clinic's auditor pulls **two different records at random** from the 1,000 — one record cannot be pulled twice, so this is sampling **without replacement**, 1.11.A.1.

:::script
ask | Ask | "What is the probability that the first record pulled is a missed appointment?"
listen | Listen for | 100 ÷ 1,000 = 0.100.
ask | Ask | "Given that it was, what is the probability that the second one is too? Think about what is left."
listen | Listen for | 999 records remain and 99 of them are missed, so P(second missed | first missed) = 99 ÷ 999 = 0.099.
intro | Recall | *Drawing without replacement, where the second probability depends on the first (2.6.A.2, 1.11.A.1)*.
ask | Ask | "Now the probability that both are missed appointments."
listen | Listen for | P(both) = P(first missed) × P(second missed | first missed) = 0.100 × 0.099 = 0.010, or 0.0099 to four places.
ask | Ask | "What would the product form have given, and how wrong is it?"
listen | Listen for | 0.100 × 0.100 = 0.0100 against the true 0.0099 — the same to three decimal places, and wrong by about one per cent of itself.
ifsay | If "so it does not matter" | "Here it barely does, because removing one record from a thousand hardly changes anything. In the summer-school lottery it moved 0.078 to 0.074, and in a box of ten units it moved 0.090 to 0.067. The method has to be right whether or not the difference shows; you do not get to decide afterwards which populations were large enough."
ask | Ask | "Why are the two draws not independent, in a sentence?"
listen | Listen for | Because the first record is not returned, so knowing it was missed leaves one fewer missed record among one fewer record, which changes the second probability from 0.100 to 0.099. Independence would require no change at all.
ask | Ask | "Give me the probability that at least one of the two is a missed appointment."
listen | Listen for | Complement of "neither is missed": P(neither) = (900 ÷ 1,000) × (899 ÷ 999) = 0.900 × 0.900 = 0.810, so P(at least one) = 1 − 0.810 = 0.190.
intro | Recall | Session 9's *Complements of compound events: "none", "at least one" and "more than" (2.4.A.4)*, now with the multiplication rule that makes it computable.
ask | Ask | "That is the calculation your Session 9 homework, question E2, could not finish. What was it?"
listen | Listen for | The four library members: P(none of the four borrows both formats) and so P(at least one). With one member chosen at a time from a large membership, independence is assumed, and 0.700⁴ = 0.2401, so P(at least one) = 0.7599 — not the 0.700 the sheet's student wrote.
:::

### What St Mary's may now write about two appointments

:::script
ask | Ask | "The manager wants a short note for the board. Write it."
listen | Listen for | Something like: *"Of the clinic's 400 first appointments, 15.0% were missed without notice, against 6.7% of the 600 follow-ups; a first appointment is more than twice as likely to be missed. Of the 100 missed appointments, 60.0% were first appointments. The probability that a randomly chosen record is a first appointment or a missed appointment, or both, is 0.400 + 0.100 − 0.060 = 0.440 — not 0.500, which counts the 60 records in both groups twice. For two different records drawn at random, the probability that both are missed appointments is 0.100 × 0.099 = 0.010."*
ask | Ask | "Which of those four sentences is the one the clinic should act on, and what must the note not say?"
listen | Listen for | The first: 0.150 against 0.067 is the operational fact. It must not say that first appointments *cause* missed appointments, must not generalise beyond St Mary's, and must not present 0.600 as the chance that a new patient misses.
:::

---

## 142–156 min · Solo case — the café's loyalty members, conditioned on the drink

Unaided. The café from Sessions 2 to 9 has **1,260 loyalty members**, and a random sample of **240** of them was classified by usual drink and by whether they usually add food — the same table as Session 9's solo case, with harder questions. Watch, say nothing, note where they hesitate.

| Usual drink | Adds food | No food | Total |
|---|---|---|---|
| Coffee | 84 | 66 | **150** |
| Tea | 22 | 28 | **50** |
| Cold drink | 14 | 26 | **40** |
| **Total** | **120** | **120** | **240** |

One of the 240 sampled members is chosen at random. Give every probability to 3 decimal places, from the counts.

1. Give P(adds food | coffee) and P(coffee | adds food). Say in words what each one is about, and explain why they differ.
2. Use the general multiplication rule to find P(tea ∩ adds food) from P(tea) and P(adds food | tea), then check it against the cell.
3. Is "usual drink is coffee" independent of "adds food"? Show the test you used and state the verdict.
4. Give P(coffee ∪ adds food), both by the rule and by counting members.
5. The café's manager writes: *"62.5% of members drink coffee and 50% add food, so 112.5% of members do one or the other."* Name the two things wrong with that sentence.
6. Two different members are chosen at random from the 240 for a tasting panel. Give the probability that both usually drink coffee, and say why 0.625 × 0.625 is not the right calculation.
7. Give a pair of events from this table that is mutually exclusive, and show what happens to the conditional probability when you condition on one of them.

**Answers.**

1. **P(adds food | coffee) = 84 ÷ 150 = 0.560** — of the 150 coffee members, 56.0% add food. **P(coffee | adds food) = 84 ÷ 120 = 0.700** — of the 120 food-adding members, 70.0% drink coffee. Same 84 members, two different groups to divide by, so two different numbers; neither can be obtained from the other without going back to the table.
2. P(tea) = 50 ÷ 240 = **0.208** and P(adds food | tea) = 22 ÷ 50 = **0.440**, so P(tea ∩ adds food) = 0.208 × 0.440 = **0.092**. The cell gives 22 ÷ 240 = 0.092. The two agree, as 2.6.A.2 guarantees.
3. **Not independent.** P(adds food) = 120 ÷ 240 = **0.500**; P(adds food | coffee) = 84 ÷ 150 = **0.560**. The two are unequal, so knowing that a member drinks coffee changes the probability that they add food, and the events are not independent. (Equivalently, P(coffee) × P(adds food) = 0.625 × 0.500 = 0.313 against the actual joint probability 0.350.)
4. By the rule: P(coffee ∪ adds food) = 0.625 + 0.500 − 0.350 = **0.775**. By counting: 150 coffee members plus the 36 non-coffee members who add food (22 + 14) gives 186, and 186 ÷ 240 = **0.775**. Equivalently 150 + 120 − 84 = 186.
5. First, **the overlap has not been subtracted**: the 84 members who do both are counted in the 62.5% and again in the 50%, and the correct figure is 0.775 (2.7.A.3). Second, **112.5% is not a possible probability** — the 0-to-1 bound, 2.4.A.3, rules it out, so the sentence could be refused before any recomputation.
6. Two **different** members means sampling **without replacement**. P(first drinks coffee) = 150 ÷ 240 = 0.625; given that, 149 of the remaining 239 members drink coffee, so P(second | first) = 149 ÷ 239 = 0.623, and P(both) = 0.625 × 0.623 = **0.390**. The product 0.625 × 0.625 = 0.391 assumes the two draws are independent, which they are not: taking one coffee member out leaves one fewer among one fewer, so the second probability is not 0.625. Here the difference is small; the method is still wrong.
7. **"Usual drink is coffee" and "usual drink is tea"**, among others. Each member has exactly one usual drink, so P(coffee ∩ tea) = 0 ÷ 240 = 0 and the events are mutually exclusive. Conditioning collapses the probability: P(coffee | tea) = 0 ÷ 0.208 = **0**, against P(coffee) = 0.625 — which is also the proof that they are not independent.

**Watch for:** the two conditionals in question 1 given as the same number, which is the session's first trap and is why the question comes first; 0.625 × 0.500 used for the joint probability in question 2 or 3 instead of 0.625 × 0.560; "coffee and adds food are independent because the menu has nothing to do with food" in question 3, which is a verdict with no numbers; 1.125 left standing in question 4; in question 5, naming only one of the two faults — both marks are in the question, and the 0-to-1 bound is the faster of the two; in question 6, the product form used because the difference "looks the same anyway"; and in question 7, a pair taken from different variables, which will not give an intersection of 0 in this table.

---

## 156–165 min · Teach it back

> *"Explain to me how a conditional probability differs from a joint probability, using the same cell of a table for both. Then explain how you decide whether two events are independent, and why that is a different question from whether they are mutually exclusive. Finish by telling me where the rule P(A ∩ B) = P(A) × P(B) comes from and when you are allowed to use it."*

A good answer contains five things. A **conditional probability** P(A | B) is the joint probability divided by P(B), which in a table means the same cell divided by the total of the group being conditioned on rather than by the table total — 250 ÷ 294 rather than 250 ÷ 1,842 (2.6.A.1). The two **directions** are different numbers: P(bus | Villages) = 0.850 and P(Villages | bus) = 0.384 share a numerator and nothing else, and no rule in this course converts one into the other. **Independence** is tested by comparing P(A | B) with P(A); equal means independent, unequal means not independent, and the question it answers — does knowing one change the other? — is not the question *mutually exclusive* answers, which is whether both can happen at all (2.7.A.1 against 2.5.A.2). Two events with non-zero probability can never be both, because mutual exclusivity forces P(A | B) = 0 while independence requires P(A | B) = P(A) > 0. And the **product form** is derived, not given: the course description states P(A ∩ B) = P(A) × P(B | A), and substituting P(B | A) = P(B) — which is what independence means — produces the short version, so it may be used only when independence has been established or assumed (2.6.A.2 with 2.7.A.1).

If they recite the product form as a rule in its own right, ask for its derivation and do not accept the answer until the two lines are written down. If they say two events are independent "because they are unrelated", go back to activity pair 1 against pair 9: both sound unrelated, and only one of them is. If the two conditionals come out as one number, put the register back on the screen and make them write both sentences in full, starting *"of the"*. Then set the homework.

---
---

# Homework — Session 10

**40 marks · bring to Session 11, self-marked**

## How to do this homework

1. Do every part **with the answer key closed.** Where you are unsure, answer anyway and put a **?** beside it.
2. Then open the key and **mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote.
3. **Bring the marked sheet.** Your wrong answers and your question marks are what Session 11 opens with.

Everything here was taught in the session; this sheet is practice. Give every probability to **3 decimal places**, worked from the counts. **Name each event** before you use a letter for it, and before writing any fraction, **say which group it is about** — the group named after "of" is the denominator. When you use the general multiplication rule, write the conditional factor out; when you use the product form P(A) × P(B), say in the same breath why independence holds. Nothing here needs a Venn diagram, a tree diagram or Bayes' theorem; none of the three is in this course.

---

## Part A — Notation and the four rules (8 marks)

One mark each. Answer in a line.

**A1.** Write the definition of P(A | B) as a formula, and say in words what the vertical bar means. (1)

**A2.** In a two-way table, which total goes underneath the cell for P(A ∩ B), and which goes underneath it for P(A | B)? (1)

**A3.** State the general multiplication rule. (1)

**A4.** Complete the definition: *events A and B are independent if and only if …* (1)

**A5.** Starting from the general multiplication rule, derive P(A ∩ B) = P(A) × P(B) and state the condition under which it is true. (1)

**A6.** State the rule for the probability of the union of two events, and say what the subtraction is for. (1)

**A7.** P(A) = 0.300, P(B) = 0.400 and P(A ∩ B) = 0. Give P(A | B), and say whether A and B are independent. (1)

**A8.** Two cards are drawn from a shuffled pack **without replacement**. In one sentence, why is the second draw's probability not the same as the first's? (1)

## Part B — Oakfield's lunch survey, conditioned on the year group (12 marks)

Oakfield School's council asked a random sample of **200 students** from Years 7, 9 and 11 how they usually have lunch. This is the table from Sessions 8 and 9; the questions are new.

| Year | School lunch | Packed lunch | Off site | Total |
|---|---|---|---|---|
| Year 7 | 42 | 21 | 7 | **70** |
| Year 9 | 35 | 28 | 7 | **70** |
| Year 11 | 18 | 24 | 18 | **60** |
| **Total** | **95** | **73** | **32** | **200** |

One of the 200 students is chosen at random.

**B1.** Give P(has school lunch | is in Year 7), and write the sentence it answers, beginning "Of the …". (1)

**B2.** Give P(is in Year 7 | has school lunch), and explain in one sentence why it is not the same number as B1. (2)

**B3.** Use the general multiplication rule to find P(is in Year 11 ∩ eats off site) from P(is in Year 11) and P(eats off site | is in Year 11), then check your answer against the cell. (2)

**B4.** Are "is in Year 7" and "eats off site" independent? Show the comparison you made and give the verdict. (2)

**B5.** Give P(is in Year 11 ∪ eats off site), and check it by counting students. (2)

**B6.** A council member writes: *"30% are in Year 11 and 16% eat off site, so 46% are in Year 11 or eat off site."* Say what is wrong and give the correct figure. (2)

**B7.** Give P(is in Year 7 | is in Year 11), and say what the answer tells you about those two events. (1)

## Part C — The library's members: unions and the double count (8 marks)

The library service's sample of **250 members**, from Sessions 8 and 9.

| Branch | Print only | E-books only | Both | Total |
|---|---|---|---|---|
| Central | 90 | 15 | 45 | **150** |
| Westside | 60 | 10 | 30 | **100** |
| **Total** | **150** | **25** | **75** | **250** |

One member is chosen at random.

**C1.** Give P(borrows print only ∪ borrows e-books only), both by the rule and by counting members, and say why the two routes agree. (2)

**C2.** Give P(is a Central member ∪ borrows both formats), and check it by counting. (2)

**C3.** A librarian adds 0.600 and 0.300 for C2 and reports 0.900. Which members have been counted twice, and how many are there? (1)

**C4.** Is "is a Westside member" independent of "borrows print only"? Show the comparison, and then use the result to find P(Westside ∩ print only) two different ways. (2)

**C5.** Give P(is a Central member ∪ is a Westside member) using the union rule, and say why the subtraction contributes nothing here. (1)

## Part D — Hillcrest's patients: two drawn without replacement (6 marks)

From the hospital network survey of Sessions 1 and 9: **Hillcrest** was the smallest site surveyed, with **18 patients**, of whom **9 said they would recommend it**. The network's reviewer picks **two different patients** from those 18, at random.

**D1.** Give the probability that the first patient picked would recommend Hillcrest. (1)

**D2.** Given that the first would recommend it, give the probability that the second would too. (1)

**D3.** Give the probability that both patients picked would recommend Hillcrest, naming the rule you used. (2)

**D4.** A reviewer computes 0.500 × 0.500 = 0.250 instead. Explain what that calculation assumes, why the assumption fails here, and why the error is larger at Hillcrest than it would be at a site with 1,000 patients. (2)

## Part E — Independent, mutually exclusive, or neither (6 marks)

One mark each. For each pair, give the verdict **and** the number or comparison that decides it. One of the three boxes will stay empty; say which at the end.

**E1.** Oakfield: "is in Year 9" and "is in Year 11". (1)

**E2.** Oakfield: "is in Year 7" and "has school lunch". (1)

**E3.** The library: "is a Central member" and "borrows e-books only". (1)

**E4.** The library: "borrows print only" and "borrows both formats". (1)

**E5.** The library: "is a Westside member" and "borrows print only". (1)

**E6.** Hillcrest: "the first patient picked would recommend" and "the second patient picked would recommend". (1)

---
---

# Answer key

*For the student to mark their own work, after attempting everything.*

### Part A answers · Notation and the four rules (8 marks, 1 each)

**A1.** (1) P(A | B) = P(A ∩ B) ÷ P(B). The bar reads **"given"** — it is not division — and P(B) must not be 0.

**A2.** (1) For P(A ∩ B), the **table total**. For P(A | B), the total of **B**, the group being conditioned on: that row's or that column's total.

**A3.** (1) P(A ∩ B) = P(A) × P(B | A): the probability that A occurs, multiplied by the conditional probability that B occurs given that A has occurred.

**A4.** (1) *… knowing whether A has occurred, or will occur, does not change the probability that B will occur* — equivalently, P(A | B) = P(A) and P(B | A) = P(B).

**A5.** (1) Independence gives P(B | A) = P(B); substituting that into P(A ∩ B) = P(A) × P(B | A) gives **P(A ∩ B) = P(A) × P(B)**, true **only when A and B are independent**.

**A6.** (1) P(A ∪ B) = P(A) + P(B) − P(A ∩ B). The subtraction removes the second copy of the individuals who are in both events, since P(A) + P(B) counts them twice.

**A7.** (1) P(A | B) = 0 ÷ 0.400 = **0**. They are **not** independent: independence would need P(A | B) = P(A) = 0.300.

**A8.** (1) Because the first card is not returned, so the second draw is made from 51 cards, one of which is already gone — the pool, and therefore the probability, has changed.

> A5 and A7 are the two statements the session was built around. If A5 came out as "P(A ∩ B) = P(A) × P(B), that's the rule", with no derivation, reread *Deriving the product form, and why it is not a second rule to memorise*: the course description never states the short form, and a student who cannot derive it cannot tell when it applies.

### Part B answers · Oakfield's lunch survey, conditioned on the year group (12 marks)

**B1.** (1) 42 ÷ 70 = **0.600**. *"Of the 70 Year 7 students, the probability that one chosen at random has school lunch is 0.600."*

**B2.** (2) 42 ÷ 95 = **0.442** (1). The numerator is the same 42 students, but the group being conditioned on is now the 95 school-lunch students rather than the 70 Year 7 students, so the denominator — and therefore the answer — is different (1).

**B3.** (2) P(Year 11) = 60 ÷ 200 = 0.300 and P(off site | Year 11) = 18 ÷ 60 = 0.300, so P(Year 11 ∩ off site) = 0.300 × 0.300 = **0.090** (1). The cell gives 18 ÷ 200 = 0.090, which agrees (1).

**B4.** (2) P(off site) = 32 ÷ 200 = **0.160**; P(off site | Year 7) = 7 ÷ 70 = **0.100** (1). The two are unequal, so the events are **not independent** — being in Year 7 lowers the probability of eating off site (1).

**B5.** (2) P(Year 11 ∪ off site) = 0.300 + 0.160 − 0.090 = **0.370** (1). By counting: 60 Year 11 students plus the 14 off-site students in Years 7 and 9 gives 74, and 74 ÷ 200 = 0.370 — equivalently 60 + 32 − 18 = 74 (1).

**B6.** (2) The **18 students who are both in Year 11 and eat off site have been counted twice**, once in the 60 and once in the 32; the union rule subtracts them once (1). The correct figure is **0.370** (1).

**B7.** (1) 0 ÷ 0.300 = **0**. No student is in two year groups, so the events are mutually exclusive — and the conditional probability of 0 against P(Year 7) = 0.350 shows they are therefore not independent.

> B1 and B2 are the session's first trap, and they are the same two numbers Session 8's homework B3 asked for. If they came out equal, the fix is mechanical: underline the group named after "of" in the question before writing anything down. B6 is the second trap, and note that 0.460 is a legal-looking probability — the 0-to-1 bound will not rescue you here.

### Part C answers · The library's members: unions and the double count (8 marks)

**C1.** (2) By the rule: 0.600 + 0.100 − 0 = **0.700** (1). By counting: 150 + 25 = 175 members, and 175 ÷ 250 = 0.700 (1). The two agree because the events are **mutually exclusive** — "print only" and "e-books only" cannot both describe one member, so P of the intersection is 0 and there is nothing to subtract.

**C2.** (2) P(Central) = 150 ÷ 250 = 0.600, P(both formats) = 75 ÷ 250 = 0.300, P(Central ∩ both formats) = 45 ÷ 250 = 0.180, so the union is 0.600 + 0.300 − 0.180 = **0.720** (1). By counting: 150 + 75 − 45 = 180 members, and 180 ÷ 250 = 0.720 (1).

**C3.** (1) The **45 Central members who borrow both formats**, counted once in the 150 Central members and once in the 75 who borrow both. Their joint probability, 0.180, is exactly the difference between 0.900 and 0.720.

**C4.** (2) P(print only) = 150 ÷ 250 = 0.600 and P(print only | Westside) = 60 ÷ 100 = 0.600, so the two events **are independent** (1). Then P(Westside ∩ print only) = 60 ÷ 250 = **0.240** from the cell, and 0.400 × 0.600 = 0.240 from the product form, which is available here precisely because independence has been shown (1).

**C5.** (1) 0.600 + 0.400 − 0 = **1.000**. Each member belongs to exactly one branch, so the two events are mutually exclusive and the intersection contributes 0; the union is the whole sample space, which is why the answer is 1.

> C4 is the only place in this course where the product form is legitimately used on real data, and the reason is worth remembering: the library's two branches have identical borrowing profiles — 0.600, 0.100, 0.300 in both rows — so every branch-and-format pair in that table is independent. Lincoln High's register is the opposite case, and there the same multiplication is wrong.

### Part D answers · Hillcrest's patients: two drawn without replacement (6 marks)

**D1.** (1) 9 ÷ 18 = **0.500**.

**D2.** (1) After one recommending patient is taken, 8 of the remaining 17 would recommend, so **8 ÷ 17 = 0.471**.

**D3.** (2) The **general multiplication rule**, P(A ∩ B) = P(A) × P(B | A) (1): 0.500 × 0.471 = **0.235** (1). Exactly, (9 ÷ 18) × (8 ÷ 17) = 72 ÷ 306 = 0.235.

**D4.** (2) It assumes the two draws are **independent**, which is what licenses P(A) × P(B); the assumption fails because the patients are drawn **without replacement**, so removing one recommending patient leaves 8 of 17 rather than 9 of 18 (1). The error is larger at Hillcrest because removing one patient from 18 changes the pool by a large fraction, moving 0.500 to 0.471; removing one from 1,000 would move 0.500 to about 0.4995, and the two calculations would agree to three decimal places (1).

> The honest point in D4 is the one the session made twice: the method does not become correct when the population is large, it merely stops being visibly wrong. Write the conditional factor every time and the question never arises.

### Part E answers · Independent, mutually exclusive, or neither (6 marks)

**E1.** (1) **Mutually exclusive.** Each student is in exactly one year group, so P(Year 9 ∩ Year 11) = 0.

**E2.** (1) **Neither.** P(Year 7 ∩ school lunch) = 42 ÷ 200 = 0.210, which is not 0; and P(school lunch | Year 7) = 0.600 against P(school lunch) = 95 ÷ 200 = 0.475, which are unequal.

**E3.** (1) **Independent.** P(e-books only) = 25 ÷ 250 = 0.100 and P(e-books only | Central) = 15 ÷ 150 = 0.100. Not mutually exclusive — 15 members are both.

**E4.** (1) **Mutually exclusive.** "Print only" means no e-books, so no member is in both: P of the intersection is 0.

**E5.** (1) **Independent.** P(print only) = 0.600 and P(print only | Westside) = 60 ÷ 100 = 0.600, as C4 showed.

**E6.** (1) **Neither.** Both can happen, so they are not mutually exclusive; and P(second recommends | first recommends) = 0.471 against P(second recommends) = 0.500, so they are not independent.

**The empty box is *both*.** Two events with non-zero probability can never be both mutually exclusive and independent: if they are mutually exclusive then P(A | B) = 0 ÷ P(B) = 0, while independence would require P(A | B) = P(A), which is greater than 0.

> Two in each of three boxes, and nothing in the fourth — the same shape as the session's activity. A verdict with no number earns nothing here; the number *is* the answer.

### Marks summary

| Part | Marks |
|---|---|
| A — Notation and the four rules | 8 |
| B — Oakfield's lunch survey, conditioned on the year group | 12 |
| C — The library's members: unions and the double count | 8 |
| D — Hillcrest's patients: two drawn without replacement | 6 |
| E — Independent, mutually exclusive, or neither | 6 |
| **Total** | **40** |

---
---

# Reference sheet — keep this

*Every term carries an example from this session. Lincoln High's register covers all 1,842 students; St Mary's clinic has 1,000 appointment records; the library's sample is 250 members and the café's 240.*

### Conditional probability: the definition and its denominator (2.6.A.1)

**P(A | B)** — the probability that A occurs **given** that B has occurred.

:::formula
P(A | B) = P(A ∩ B) ÷ P(B),  with P(B) ≠ 0
:::

In a two-way table it is the **cell divided by the total of the group conditioned on**, not by the table total. Say *"of the …"* out loud before writing the fraction; the group named is the denominator.

| | Lincoln High | The number |
|---|---|---|
| Joint, cell ÷ table total | P(Villages ∩ bus) | 250 ÷ 1,842 = **0.136** |
| Conditional, cell ÷ row total | P(bus \| Villages) | 250 ÷ 294 = **0.850** |
| Conditional, cell ÷ column total | P(Villages \| bus) | 250 ÷ 651 = **0.384** |

**P(A | B) and P(B | A) are different numbers.** 0.850 is "of the Villages students, how many take the bus"; 0.384 is "of the bus users, how many live in the Villages". Same 250 students; nothing in this course converts one into the other.

### The general multiplication rule: the reference version (2.6.A.2)

:::formula
P(A ∩ B) = P(A) × P(B | A)   —   and equally   P(A ∩ B) = P(B) × P(A | B)
:::

The second factor is **conditional**. Use this rule whenever there is no cell to read, which in practice means **two draws without replacement** (1.11.A.1): the second probability is taken from the reduced pool, denominator *n* − 1.

- St Mary's: P(first ∩ missed) = 0.400 × 0.150 = **0.060**, matching the cell 60 ÷ 1,000.
- St Mary's audit, two records without replacement: P(both missed) = (100 ÷ 1,000) × (99 ÷ 999) = **0.010**.
- The café's tasting panel, two members without replacement: P(both drink coffee) = (150 ÷ 240) × (149 ÷ 239) = **0.390**.

### Independence: the test, and the product that follows (2.7.A.1)

A and B are **independent if and only if** knowing whether A has occurred does not change the probability of B — equivalently P(A | B) = P(A) and P(B | A) = P(B).

**The test, from a table:** compare the conditional probability with the unconditional one. Equal → independent. Unequal → **not independent** (the course description does not use the term "dependent events").

| Example | Comparison | Verdict |
|---|---|---|
| Lincoln High: bus and Villages | P(bus \| Villages) = 0.850 vs P(bus) = 0.353 | not independent |
| St Mary's: missed and first appointment | P(missed \| first) = 0.150 vs P(missed) = 0.100 | not independent |
| The café: adds food and coffee | P(food \| coffee) = 0.560 vs P(food) = 0.500 | not independent |
| The library: print only and Westside | P(print only \| Westside) = 0.600 vs P(print only) = 0.600 | **independent** |

**The product form is derived, not given.** Substituting P(B | A) = P(B) into the general multiplication rule gives P(A ∩ B) = P(A) × P(B), which is true **only** under independence. The library: 0.400 × 0.600 = 0.240 = 60 ÷ 250. Lincoln High: 0.160 × 0.353 = 0.056, against an actual 0.136 — the form does not apply.

### The probability of a union: the reference version (2.7.A.3)

**A ∪ B** is the event that A occurs, or B occurs, **or both** — the statistical "or" is inclusive.

:::formula
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
:::

The subtraction removes the second copy of the individuals in both events. Before adding two probabilities, ask whether both events can happen; if they can, subtract once.

| Example | Calculation | Counted directly |
|---|---|---|
| Lincoln High: bus or Villages | 0.353 + 0.160 − 0.136 = **0.377** | 695 ÷ 1,842 |
| St Mary's: first appointment or missed | 0.400 + 0.100 − 0.060 = **0.440** | 440 ÷ 1,000 |
| The café: coffee or adds food | 0.625 + 0.500 − 0.350 = **0.775** | 186 ÷ 240 |
| St Mary's: cancelled or missed (mutually exclusive) | 0.060 + 0.100 − 0 = **0.160** | 160 ÷ 1,000 |

There is only **one** union rule: for mutually exclusive events it subtracts zero. The wrong sums to recognise are St Mary's 0.500 and the café's 1.125 — the first is a legal-looking probability and the second is not, which is why the 0-to-1 bound (2.4.A.3) is a safety net rather than the check.

### Telling mutually exclusive from independent: the reference table (2.5.A.2, 2.7.A.1)

| | Mutually exclusive | Independent |
|---|---|---|
| Question | can both happen? | does knowing one change the other? |
| Test | P(A ∩ B) = 0 | P(A \| B) = P(A) |
| Usual source | two levels of the **same** variable | one level from **each** of two variables |
| Session example | Town and Villages: P = 0 | Westside and print only: 0.600 = 0.600 |
| If one occurs | the other certainly did not | the other is unchanged |

**No pair with non-zero probability is both.** Mutually exclusive forces P(A | B) = 0 ÷ P(B) = 0; independence requires P(A | B) = P(A) > 0. And most pairs are **neither** — Villages and bus, first appointment and missed, coffee and adds food are all in that box.

### Which denominator, which rule: Lincoln High and St Mary's side by side (2.6–2.7)

| The question says | The rule | Lincoln High | St Mary's |
|---|---|---|---|
| "and", "both" | cell ÷ table total, or P(A) × P(B \| A) | P(Villages ∩ bus) = 0.136 | P(first ∩ missed) = 0.060 |
| "of the …", "given", "among" | cell ÷ conditioning total | P(bus \| Villages) = 0.850 | P(missed \| first) = 0.150 |
| the other direction | the same cell ÷ the other total | P(Villages \| bus) = 0.384 | P(first \| missed) = 0.600 |
| "or", "at least one of the two" | P(A) + P(B) − P(A ∩ B) | 0.377 | 0.440 |
| "are they independent?" | P(A \| B) against P(A) | 0.850 vs 0.353 → no | 0.150 vs 0.100 → no |
| "can both happen?" | P(A ∩ B), is it 0? | 0.136 → no | 0.060 → no |
| two drawn, none returned | P(A) × P(B \| A), denominator *n* − 1 | — | (100 ÷ 1,000) × (99 ÷ 999) = 0.010 |
