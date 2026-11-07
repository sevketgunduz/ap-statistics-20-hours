# Session 10 — Conditional Probability, Independence and Unions

**AP Statistics · Twenty-Hour Course · Student edition, to work through on your own**
**CED Topics 2.6, 2.7 · About 205 minutes, plus homework**

---

## How to use this

Session 9 could calculate the probability of an event and of its complement, and could decide whether two events were mutually exclusive. It could not answer the question every two-way table in this course has been waiting for: *given* that the student lives in the Villages, how probable is the bus? That is topic 2.6, and answering it changes exactly one thing — the number underneath the fraction. You have done this arithmetic before, in Session 8, under the name **conditional relative frequency**. Today it gets its probability name, its notation P(A | B), and a formula.

Three more things follow from that one definition and nothing else does. Rearranged, it becomes the **general multiplication rule**, P(A ∩ B) = P(A) × P(B | A). Compared against the unconditional probability, it defines **independence**. And alongside them sits the **union** — the probability that A or B or both occur — whose rule subtracts the individuals that a plain sum counts twice. Session 9 counted those students by hand at Lincoln High and promised you the formula; here it is.

This session also closes the confusion the last one opened on purpose. *Mutually exclusive* and *independent* are not two shades of one idea. For events with non-zero probability they cannot both be true at once, and the proof is two lines long. You will write it yourself, twice.

:::note amber Write first, then reveal
Every **Your turn** box asks you to do something before the text shows you the answer. **Do it on paper first.** Every probability, every verdict and every derivation on these pages is hidden behind a reveal so that you cannot read it before you commit. A wrong answer you wrote yourself and then corrected stays with you; a right one you read does not.
:::

**What you need:** paper, a pen and a calculator. There is no interactive tool in this session, and the reason is worth knowing: conditional probability, the multiplication rule, independence and the union are all facts about one fixed table that does not change, so a table with the right total ringed shows everything a simulation could. The tools return in Sessions 11 and 12, where things genuinely move.

### How this maps to your tutor's document

Working alone with a pen is slower than working with a tutor, so each part is given about a quarter longer than the tutor's segment. Take the time.

| Your section | Tutor's section | Minutes |
|---|---|---|
| Part 1 — Your Session 9 homework, and a warm-up | 0–14 Homework debrief and diagnostic | 15 |
| Part 2 — Theory: conditional probability, independence and unions | 14–56 Theory — conditional probability, independence and unions | 53 |
| Part 3 — Lincoln High's register: bus given the Villages | 56–90 Scenario A | 42 |
| Part 4 — Sorting twelve event pairs, on your own | 90–110 Activity | 25 |
| Part 5 — St Mary's clinic: unions, and an audit of two records | 110–142 Scenario B | 40 |
| Part 6 — On your own: the café's members, conditioned on the drink | 142–156 Solo case | 18 |
| Part 7 — Explain it back | 156–165 Teach it back | 12 |
| **Total** | **165 minutes** | **205** |

If your tutor has not yet set the **Session 8 test**, take it before Part 1: 20 questions, 35 minutes, timed, answer key closed.

:::note red Words and pictures you may have met that the course description does not use
The **addition rule** is a prep-book name for P(A ∪ B) = P(A) + P(B) − P(A ∩ B); the course description's phrase is *the probability of the union* (2.7.A.3). **Venn diagrams** and **tree diagrams** appear nowhere in the framework, and no exam question requires either — there is not one of either in this session, deliberately. **Bayes' theorem** is also absent and is not in this course at any point; the only way you ever reverse a conditional probability here is to go back to the table and divide the same cell by the other total. **"Dependent events"** is not a term the framework defines: the correct phrase for the other case is simply *not independent*, and that is what these pages say. **"Law of total probability"**, **"exhaustive"** and **"odds"** are absent too. **Law of averages** and **gambler's fallacy**, from Session 8, remain prep-book names for a misreading of the law of large numbers.

One more, and it is the important one: **the course description never states P(A ∩ B) = P(A) × P(B).** Every prep book prints it as a rule. The framework gives only the *general* rule, P(A) × P(B | A), plus the definition of independence, and the short form follows from those two by a substitution that you will perform yourself in Part 2. It is perfectly usable once derived — but if you memorise it on its own you will not be able to tell when it applies, and that is the single most expensive mistake on this topic.
:::

---

## Part 1 — Your Session 9 homework, and a warm-up

Get out your marked Session 9 homework and make two lists: the questions you got **wrong**, and the questions you marked with a **?**, including the ones that turned out right.

**Two specific things to check.** Both come back today, harder.

- **B7 and D4: did you give a verdict without a number?** B7 asked whether "is in Year 9" and "has school lunch" are mutually exclusive — no, because P(Year 9 ∩ school lunch) = 35 ÷ 200 = 0.175. D4 asked the same of "treated at St Mary's" and "would recommend" — no, because 63 ÷ 300 = 0.210. A right verdict with no joint probability was worth one mark of two. Today the **same pairs of events** get a second and harder question asked of them: not "can they both happen?" but "does one of them change the probability of the other?" The joint probability you were asked for is the **numerator** of the formula you are about to meet, so a student who cannot produce it cannot produce a conditional probability either.
- **E2: the four library members, and the rule that was not available yet.** The answer key said so outright — getting from one member to four needs the multiplication rule, 2.6.A.2, which is this session. It gave the exact answer, P(none of the four borrows both formats) = 0.2401 and so P(at least one) = 0.7599, against the 0.700 in the question. **You will do that calculation in Part 5.**

Worth a minute each if they were wrong: **B5**, the "three lunch types so 0.333" reflex, which Part 6 tests again in a new form; and **C4**, where the complement and a direct count were two roads to 0.850. Today several answers have two or three roads, and you should expect them to agree — when they do not, one of them is a misread question rather than an arithmetic slip.

### Warm-up: four questions on "given", "and" and "or"

:::yourturn
Answer all four on paper before revealing. Two of them are deliberately unanswerable as asked; say so if you think so.

1. From Lincoln High's table: of the 294 Villages students, 250 travel by bus, and there are 651 bus users in all. Give 250 ÷ 294 and 250 ÷ 651 **in words** — what is each one the probability of?
2. P(A) = 0.600 and P(B) = 0.500. What is P(A ∩ B)?
3. A café's loyalty members: 150 of 240 usually drink coffee and 120 of 240 usually add food. How many usually do at least one of the two?
4. Two events cannot both happen. If you are told the first one happened, what do you now know about the second?
:::

:::reveal Reveal — the four warm-up answers
1. **250 ÷ 294 = 0.850** is *"of the students who live in the Villages, the probability that one chosen at random travels by bus."* **250 ÷ 651 = 0.384** is *"of the students who travel by bus, the probability that one chosen at random lives in the Villages."* The same 250 students over two different groups. If you gave one number twice, that is the error Session 8's homework B3 caught and today's Part 3 is built on — and it is the commonest single mistake on this topic.
2. **You cannot tell.** Session 9 said this explicitly: P(A ∩ B) is not P(A) × P(B). To answer you would need either the conditional probability P(B | A), or a guarantee that A and B are independent — and both of those are today's content. If you wrote 0.300, you have imported the product form from somewhere without its condition, which Part 2 will take apart.
3. **186.** Not 270: the 84 members who drink coffee *and* add food are inside the 150 and inside the 120, so adding counts them twice. 150 + 120 − 84 = 186. That subtraction is rule 2.7.A.3, and it is most of Part 5.
4. **That the second one certainly did not happen.** Knowing about the first changes the second's probability all the way to 0, which is the largest change there is — the opposite of independence. If you answered "nothing, they're unrelated", the two ideas are fused in your head, and untangling them is what Part 4 exists for.
:::

---

## Part 2 — Theory: conditional probability, independence and unions

Read this part in full before you do anything else. It states every rule the rest of the session uses, in the order the course description states them, with the formula, what it does **not** say, a bare illustration and a real study. Read the bare one first: it shows the structure with nothing to distract you. Then read the study: it shows the rule doing something.

The bare cases are two made-up tables and one box of ten units. The **40-unit** table is new and is deliberately **not** independent. The **30-unit** table is the one Session 9 used — and it turns out to be exactly independent, which is why the product seemed to work there; by the end of this part you will be able to prove it was not a coincidence.

The real studies continue the strand from Sessions 6 to 9: the **district** — its 400 Year 11 pupils cross-tabulated by revision attendance and result, and its summer-school lottery of 50 applicants for 30 places, 14 of them from the two smallest schools — and the **university's first-year statistics module** of 318 students, whose scripts go to a marking moderation panel.

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

Say all six of these back before you read on. If one has gone, reread that subsection of Session 9 now, because everything below is phrased in them.

| From Session 9 | In one line | Code |
|---|---|---|
| Sample space | all possible **nonoverlapping** outcomes of a random process | 2.4.A.1 |
| P(E) by counting | outcomes in E ÷ outcomes in the sample space, **if** they are equally likely | 2.4.A.2 |
| The 0-to-1 bound | every probability is a number from 0 to 1 inclusive | 2.4.A.3 |
| The complement | P(E′) = P(Ē) = P(E^C) = 1 − P(E) | 2.4.A.4 |
| Joint probability | P(A ∩ B), the probability that **both** occur | 2.5.A.1 |
| Mutually exclusive | they cannot occur together, so P(A ∩ B) = 0 | 2.5.A.2 |

What Session 9 could not do. Every probability it calculated had the **whole sample space** underneath: 1,842 students, 1,000 records, 240 members. It had no way to answer *"of the Villages students, how probable is the bus?"* — and it told you so three times, pointing here. Lifting that restriction is the whole of topic 2.6, and everything else in this session follows from it.

*Illustration:* in the 40-unit table, Session 9 could give P(A) = 24 ÷ 40 = **0.600**, P(yes) = 22 ÷ 40 = **0.550**, P(A ∩ yes) = 18 ÷ 40 = **0.450** and P(A′) = **0.400**. What it could not give is the probability that a unit is marked yes **when you already know it is type A**.

*Education example:* for one of the district's 400 Year 11 pupils chosen at random, Session 9 gave P(attended the revision programme) = 240 ÷ 400 = **0.600**, P(passed) = 260 ÷ 400 = **0.650** and P(attended ∩ passed) = 180 ÷ 400 = **0.450**. The governors' actual question — *does attending raise a pupil's chance of passing?* — needs the probability of passing **among the attenders**, which Session 8 computed as 75.0% and Session 9 was not allowed to call a probability.

### Conditional probability: the probability of A given B (2.6.A.1)

The probability that event A will occur **given that event B has occurred** is called a **conditional probability**, written **P(A | B)**, and is defined as the joint probability divided by the probability of the condition.

:::formula
P(A | B) = P(A ∩ B) ÷ P(B)

P(A | B) — the probability of A given B, read "the probability of A given B"
P(A ∩ B) — the probability that A and B both occur (2.5.A.1)
P(B) — the probability of the event being conditioned on; it must not be 0
:::

The vertical bar is not division; it reads **given**. What the formula says is that conditioning **shrinks the sample space to B**, and then asks what share of that smaller space is also A. The numerator is the overlap because, once you know B happened, the only way A can still happen is in the part of A that lies inside B.

What it does not say. It does not say P(A) — a conditional probability is a different number from the unconditional one, except in the special case called independence. It does not say P(A ∩ B): the intersection is the **numerator**, not the answer, and the two differ by a factor of 1 ÷ P(B), which is always 1 or more. It is undefined when P(B) = 0; conditioning on something that cannot happen is not a question. And the bar is **not symmetric** — P(A | B) and P(B | A) are different quantities with different denominators.

*Illustration:* in the 40-unit table, P(yes | type A) = P(A ∩ yes) ÷ P(A) = 0.450 ÷ 0.600 = **0.750**. Read straight off the table it is 18 ÷ 24 = 0.750: 24 units are type A, and 18 of those are marked yes. Same number, two routes.

*Education example:* for one of the district's 400 Year 11 pupils, P(passed | attended) = 0.450 ÷ 0.600 = **0.750**, or 180 ÷ 240 directly — against P(passed) = **0.650** for a pupil chosen from all 400, and P(passed | did not attend) = 80 ÷ 160 = **0.500**. This is Session 8's 75.0% and 50.0% with a probability name attached, and it is the number the governors asked for.

### Why the denominator changes: a cell over a row total (2.6.A.1)

This is the cheapest win in the session, so say it out loud. **Conditional probability is the arithmetic you did in Session 8, renamed.** In a two-way table:

| Quantity | Divide the cell by | Session 8's name |
|---|---|---|
| P(row ∩ column) | the **table** total | joint relative frequency |
| P(column \| row) | that **row's** total | conditional relative frequency |
| P(row \| column) | that **column's** total | conditional relative frequency |

The only thing the word *given* changes is which total goes underneath. Keep the habit Session 8 installed: **say the group out loud — "of the type A units, …" — before writing the fraction.** The group named after "of" is the denominator, every time.

What it does not say. It does not say the cell changes. The numerator of P(yes | A), of P(A | yes) and of P(A ∩ yes) is the same 18 units; only the denominator distinguishes them, which is exactly why the three are so easy to confuse. And it does not say the row total is always right — if the condition is a column, the column total is the denominator, and working mechanically down a table will give you the row total both times.

*Illustration:* the same 18 units, three ways. P(A ∩ yes) = 18 ÷ **40** = 0.450. P(yes | A) = 18 ÷ **24** = 0.750. P(A | yes) = 18 ÷ **22** = 0.818. One cell, three denominators, three different numbers.

*Education example:* of the district's 400 Year 11 pupils, the 180 who both attended and passed give P(attended ∩ passed) = 180 ÷ **400** = 0.450, P(passed | attended) = 180 ÷ **240** = 0.750, and P(attended | passed) = 180 ÷ **260** = **0.692**. The district's report quotes the first as "45% of our Year 11 cohort", the second as "75% of attenders passed", and the third as "69% of those who passed had attended". All three are true, all three describe the same 180 pupils, and they answer three different questions.

### P(A | B) and P(B | A) are different numbers (2.6.A.1)

This is the session's first trap and it has already cost marks twice in this course: Session 8's homework B3 and Session 9's diagnostic both caught it. The two conditionals share a numerator and have different denominators, so they are equal only when P(A) = P(B).

:::formula
P(A | B) = P(A ∩ B) ÷ P(B)        P(B | A) = P(A ∩ B) ÷ P(A)
:::

The practical test is a sentence. *"Of the B group, what share are A?"* is P(A | B). *"Of the A group, what share are B?"* is P(B | A). Exam questions always make the group explicit, in the words *of*, *given*, *among* or *for those who* — so underline that group before you write anything.

What it does not say. It does not say one of them is wrong: both are legitimate probabilities about the same data, and the error is answering the question that was not asked. And reversing a conditional is **not** flipping the fraction — 1 ÷ 0.750 is not 0.818, and there is no rule in this course that converts P(A | B) into P(B | A). You go back to the table and divide the same cell by the other total.

*Illustration:* in the 40-unit table, P(yes | A) = 18 ÷ 24 = **0.750** and P(A | yes) = 18 ÷ 22 = **0.818** — the same 18 units. And P(yes | B) = 4 ÷ 16 = **0.250** is small while P(A | yes) is large, which is a good reminder that the two directions carry different information.

*Education example:* the district's report has to keep two sentences apart. *"Of the pupils who attended the revision programme, 75% passed"* is P(passed | attended) = 0.750. *"Of the pupils who passed, 69% had attended"* is P(attended | passed) = 0.692. A governor who reads the second as the first concludes the programme guarantees little; one who reads the first as the second concludes that three-quarters of the district's passes came from the programme. Neither conclusion is in the data, and both are common.

### The general multiplication rule (2.6.A.2)

The **general multiplication rule** states that the probability that events A and B both will occur is equal to the probability that A will occur multiplied by the conditional probability that B will occur given that A has occurred.

:::formula
P(A ∩ B) = P(A) × P(B | A)

P(A ∩ B) — the probability that both occur (2.5.A.1)
P(A) — the probability of the first event
P(B | A) — the probability of B given that A has occurred (2.6.A.1)
:::

It is the definition of conditional probability with the denominator moved across, and it is the **only product form the course description states**. It works in either order, because the intersection does not care which event you call A: P(A ∩ B) = P(B) × P(A | B) is the same rule. Use whichever conditional probability you actually have.

What it does not say. It does not say P(A) × P(B). The second factor is **conditional**, and dropping the condition is the most expensive single slip on this topic, because it silently assumes independence. It does not say the two events happen in sequence: "and" means both hold for the same individual or the same trial, so the rule applies perfectly well to one student with two recorded characteristics. And it is not mainly a way of *checking* a joint probability you could read off a table — in a table the cell is the better source, and the rule earns its keep where there is no table, which in practice means two draws.

*Illustration:* in the 40-unit table, P(A) = 0.600 and P(yes | A) = 0.750, so P(A ∩ yes) = 0.600 × 0.750 = **0.450** — which is 18 ÷ 40, the cell. The naive product would have given 0.600 × 0.550 = 0.330, which is not 0.450.

*Education example:* for a district Year 11 pupil, P(attended) = 0.600 and P(passed | attended) = 0.750, so P(attended ∩ passed) = 0.600 × 0.750 = **0.450**, matching the 180 pupils in the cell. The naive product, 0.600 × 0.650 = **0.390**, is what the district would have expected if attendance made no difference to passing; the gap between 0.390 and 0.450 is the programme's apparent effect, and it is also a preview of how independence is tested.

### Drawing without replacement, where the second probability depends on the first (2.6.A.2, 1.11.A.1)

Where the general multiplication rule is indispensable is a pair of **draws without replacement** — sampling in which a selected individual is not returned before the next selection, which is 1.11.A.1 from Session 6. Take one individual out and both the numerator and the denominator of the next probability change, so the second draw's probability genuinely depends on the first, and the conditional factor is not optional.

:::formula
P(first is A ∩ second is A) = P(first is A) × P(second is A | first is A)
:::

In practice the second factor is read off the reduced population: one fewer A, one fewer individual. The arithmetic is easy; the discipline is remembering that the second denominator is *n* − 1.

What it does not say. It does not say the two draws are independent — they are the standard example of two events that are not. It does not say the effect is always large: taking one record out of 1,000 barely moves the second probability, while taking one applicant out of 50 moves it noticeably. And **with** replacement is a different design (1.11.A.2): the individual goes back, the population is restored, and the draws then *are* independent — which is the only reason the product form ever applies to repeated draws.

*Illustration:* a box of 10 units, 3 of them type A, and two drawn without replacement. P(first is A) = 3 ÷ 10 = **0.300**. Given that, 2 of the remaining 9 are type A, so P(second is A | first is A) = 2 ÷ 9 = **0.222**, and P(both are A) = 0.300 × 0.222 = **0.067**. Treating the draws as independent gives 0.300 × 0.300 = 0.090 — a third too high. And if the first is *not* type A, P(second is A | first is not A) = 3 ÷ 9 = 0.333, a different number again: that is what "depends on the first" means.

*Education example:* the district's summer school has 50 applicants for 30 places, 14 of them from the two smallest schools, and names are drawn at random without replacement. P(the first name drawn is from a small school) = 14 ÷ 50 = **0.280**; given that, 13 of the remaining 49 are, so P(the second is too | the first was) = 13 ÷ 49 = **0.265**, and P(both of the first two are from small schools) = 0.280 × 0.265 = **0.074**. Multiplying 0.280 by itself gives 0.078, which overstates it — and the size of that gap is the honest reason the course teaches the general rule rather than the short one.

### Independent events, defined by what knowing one tells you about the other (2.7.A.1)

Events A and B are **independent if and only if** knowing whether A has occurred, or will occur, does not change the probability that B will occur. When A and B are independent,

:::formula
P(A | B) = P(A)   and   P(B | A) = P(B)

Both equalities hold together: if one is true the other is, for events of non-zero probability.
:::

"If and only if" is doing real work there. The equality is not a symptom of independence — it **is** independence. So deciding whether two events are independent is one task with one step: compare a conditional probability with its unconditional partner.

What it does not say. It does not say *unrelated in the world*: independence is a numerical statement about probabilities. It does not say *mutually exclusive*; the two are opposites, as the subsection five below proves. It does not say the events never occur together — independent events with non-zero probabilities **must** sometimes occur together, since P(A ∩ B) = P(A) × P(B) > 0. And it does not say "close enough": 0.560 against 0.500 in a table of real counts is **not independent**, because the framework gives no tolerance, and the test that would let you judge a near miss does not arrive until Session 17.

*Illustration:* in Session 9's 30-unit table, P(yes) = 10 ÷ 30 = **0.333**, P(yes | type A) = 4 ÷ 12 = **0.333**, and P(yes | type B) = 6 ÷ 18 = **0.333**. Knowing the type tells you nothing about the mark, so "type A" and "yes" are independent there. In the 40-unit table they are not: P(yes | A) = 0.750 against P(yes) = 0.550.

*Education example:* the university module's 318 scripts are graded, and then the moderation panel selects **one script in six at random** for remarking. Because the selection is random, P(a script is moderated | it is graded A) = 1 ÷ 6 = **0.167**, which is P(moderated) for every grade. "Graded A" and "selected for moderation" are independent **by the design of the draw** — randomisation is the one mechanism that *guarantees* independence rather than merely exhibiting it. Note what independence does not promise: in the scripts actually chosen, exactly one in six of the 44 A scripts need not appear. Independence is a statement about probabilities, not about counts.

### Deriving the product form, and why it is not a second rule to memorise (2.7.A.1 with 2.6.A.2)

**Write these three lines out now, on paper, before reading the reveal below.** They are the whole derivation, and a student who has written them can tell when the short rule applies, which a student who has memorised it cannot.

1. The general multiplication rule, 2.6.A.2: P(A ∩ B) = P(A) × P(B | A).
2. The definition of independence, 2.7.A.1: if A and B are independent, then P(B | A) = P(B).
3. Substitute the second into the first.

:::formula
If — and only if — A and B are independent:   P(A ∩ B) = P(A) × P(B)
:::

So the product form is a **theorem**, true exactly when independence holds and false otherwise. Every prep book prints it as a rule of its own; the course description does not state it anywhere. What it states is the general rule and the definition. The practical consequence is a two-way street you should be able to walk in both directions: given independence, multiply — and given a table, comparing P(A) × P(B) against the actual P(A ∩ B) is an equivalent way of **testing** independence.

What it does not say. It does not license multiplying whenever the word "and" appears, which is the commonest error on this topic in every prep book's practice set. It does not apply to two draws without replacement. And it is not the definition: asked to *define* independent events, you give 2.7.A.1's sentence, or P(A | B) = P(A) — not the product.

:::note amber The one sentence to write in your margin
**Multiply only when you have the conditional, or when you have checked independence.** P(A) × P(B | A) always works. P(A) × P(B) works only when the second factor has been shown equal to P(B | A).
:::

*Illustration:* in the 30-unit table, P(A) × P(yes) = 0.400 × 0.333 = **0.133**, and the cell gives P(A ∩ yes) = 4 ÷ 30 = **0.133**. Session 9 called that agreement a coincidence of the numbers and refused to use it as a method. It was not a coincidence: the two variables in that table are independent, which is the only circumstance in which the product works, and you now have the test that shows it. In the 40-unit table the same product gives 0.600 × 0.550 = 0.330 against an actual 0.450, and there it really is wrong.

*Education example:* for the module's scripts, P(graded A) = 44 ÷ 318 = **0.138** and P(moderated) = **0.167**, and since the two are independent by the design of the draw, P(graded A ∩ moderated) = 0.138 × 0.167 = **0.023**. For the district's Year 11 pupils the same move is not available: P(attended) × P(passed) = 0.600 × 0.650 = 0.390, while the actual joint probability is 0.450, so the events are not independent and only the general rule — 0.600 × 0.750 — reaches the right answer.

### Testing independence from a two-way table (2.7.A.1)

A table gives you every number you need, so the test is mechanical. Pick a row level and a column level, and compare one pair of numbers.

| Step | What to compute | Verdict |
|---|---|---|
| 1 | P(column level) = column total ÷ table total | the unconditional probability |
| 2 | P(column level \| row level) = cell ÷ row total | the conditional probability |
| 3 | compare | equal → independent; unequal → **not independent** |

An equivalent route compares the cell's probability with the product of the two marginal probabilities, P(A) × P(B), and reaches the same verdict for the same reason. Either is acceptable; say which you used.

What it does not say. It does not say one comparison settles the whole table — strictly, two *variables* are independent only if the equality holds for every row-and-column pair, and when a question asks about two named **events**, one comparison is exactly what is wanted. It does not say counts decide: "there are more bus users in the Villages" is a count, and Session 8 refused counts as evidence of association for the same reason. And it does not say that "not independent" means "mutually exclusive" — for a pair of events that overlap, it cannot.

*Illustration:* 30-unit table, P(yes) = 0.333 against P(yes | A) = 0.333 → **independent**. 40-unit table, P(yes) = 0.550 against P(yes | A) = 0.750 → **not independent**, and the direction is informative too: being type A raises the chance of a yes by 0.200.

*Education example:* for the district's Year 11 pupils, P(passed) = 0.650 and P(passed | attended) = 0.750, so attendance and passing are **not independent** for a randomly chosen pupil — knowing a pupil attended raises the probability of a pass from 0.650 to 0.750. Session 8 reached the same verdict from the same counts and called it an **association**; today's verdict is its probability counterpart. Both stop short of cause, which needs random assignment (Session 7).

### The union of two events, and the word "or" (2.7.A.2)

The probability that event A **or** event B (**or both**) will occur is the probability of the **union** of A and B, written **P(A ∪ B)**.

:::formula
A ∪ B — the event that A occurs, or B occurs, or both
:::

Read ∪ as "union" or as "or". The parenthesis in the framework's sentence is the point: the statistical *or* is **inclusive**, so the union contains the individuals in A alone, those in B alone, and those in both. Everyday English often means the exclusive *or* — "tea or coffee" from a waiter does not invite both — and that is where the misreading comes from.

What it does not say. It does not exclude the overlap, so *"bus or Villages"* includes the students who are both. It is not the intersection: A ∪ B is at least as probable as either event on its own, while A ∩ B is at most as probable as either, so a union that comes out smaller than P(A) is the wrong calculation. And it is itself just an event, so Session 9's counting still applies — a union can always be counted directly off a table, which is what Session 9 did.

*Illustration:* in the 40-unit table, A ∪ yes is the 24 type A units together with the 4 type B units marked yes — 28 in all, so P(A ∪ yes) = 28 ÷ 40 = **0.700**. Note it is bigger than P(A) = 0.600 and bigger than P(yes) = 0.550, as a union must be.

*Education example:* for a district Year 11 pupil, *"attended the revision programme or passed"* collects the 180 who did both, the 60 who attended without passing and the 80 who passed without attending: 320 pupils, so P(attended ∪ passed) = 320 ÷ 400 = **0.800**. Only the 80 who neither attended nor passed are outside the union, which is a useful way of seeing what a union is.

### The probability of a union, and the outcomes counted twice (2.7.A.3)

The probability of the union is the sum of the two probabilities minus the probability of the intersection.

:::formula
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

P(A) + P(B) — counts every individual in the overlap twice
P(A ∩ B) — the overlap, subtracted once to correct that
:::

This is the rule Session 9 deliberately withheld. At Lincoln High it counted 695 students in "bus or Villages" by hand and then pointed at the 250 in the overlap as the students the next session's rule would subtract. This is that rule, and the subtraction is the entire content of it.

What it does not say. It does not say P(A) + P(B); that is right only when P(A ∩ B) = 0, which is Session 9's **mutually exclusive** (2.5.A.2) and is therefore the special case, not the norm. It does not fail when the events are mutually exclusive — the rule still holds and simply subtracts zero, so there is only **one** union rule to remember. And it gives no licence to add more than two probabilities without thought: three events have overlaps between every pair, and the course description does not ask for that case.

The giveaway that someone has added without subtracting is a probability above 1, which Session 9's 0-to-1 bound (2.4.A.3) catches for free. But it does not always fire — 0.513 at Lincoln High is a perfectly respectable-looking wrong answer — so the habit has to be structural: **whenever you add two probabilities, say out loud whether the events can both happen.**

*Illustration:* 40-unit table. P(A) + P(yes) = 0.600 + 0.550 = 1.150, already impossible. Subtract the overlap: 1.150 − 0.450 = **0.700**, matching the 28 units counted directly. The 18 units in the cell were counted once in the 24 and once in the 22.

*Education example:* for a district Year 11 pupil, P(attended) + P(passed) = 0.600 + 0.650 = 1.250 — impossible, and caught by the bound. The correct value is 0.600 + 0.650 − 0.450 = **0.800**, matching the 320 pupils counted. The 180 who both attended and passed are the ones the naive sum counted twice, and 1.250 − 0.800 = 0.450 is exactly their joint probability.

### Mutually exclusive against independent: why no pair with non-zero probability is both (2.5.A.2, 2.6.A.1, 2.7.A.1)

The two ideas use different machinery and answer different questions, and they get fused because both sentences begin "the two events are…". Session 9 warned you; here is the proof, which fits in three lines and uses nothing outside 2.5.A.2, 2.6.A.1 and 2.7.A.1.

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

What it does not say. It does not say *every* pair is one or the other: most pairs are **neither**, which is what Lincoln High's Villages and bus turn out to be, and "neither" is the commonest verdict in real data. It does not say the two tests are alternatives for the same question — a full answer about a pair of events may need both. And the exception at the bottom of the table is genuine but empty in practice: an event of probability 0 is trivially both, which is why every exam question specifies non-zero probabilities.

*Illustration:* in the 40-unit table, "type A" and "type B" are mutually exclusive, so P(A | B) = 0 while P(A) = 0.600 — not independent. "Type A" and "yes" are not mutually exclusive, since P(A ∩ yes) = 0.450, and not independent either, since 0.750 ≠ 0.550: **neither**. In the 30-unit table, "type A" and "yes" are independent and not mutually exclusive.

*Education example:* for a module script, "graded A" and "graded B" are mutually exclusive — one grade per script, so P of the intersection is 0 — and therefore certainly not independent: learning that a script was graded A drops the probability that it was graded B from 0.292 to 0.000. "Graded A" and "selected for moderation" are independent and not mutually exclusive, since both can happen and P of the intersection is 0.023. And "attended the revision programme" and "passed", for a district pupil, are neither. Three pairs, three verdicts, and no pair in the fourth box.

### Which rule the question is asking for: a decision list (2.6–2.7)

Part 4 drills this recognition; here is the list it drills. Read the question, find the word, pick the rule.

| The question says | What is wanted | Rule | Code |
|---|---|---|---|
| "and", "both" | the joint probability | the cell ÷ table total, or P(A) × P(B \| A) | 2.5.A.1, 2.6.A.2 |
| "given", "of the …", "among", "for those who" | a conditional probability | the cell ÷ the conditioning total | 2.6.A.1 |
| "or", "at least one of the two" | the union | P(A) + P(B) − P(A ∩ B) | 2.7.A.3 |
| "not", "none", "at least one" (of several) | a complement | 1 − P(E) | 2.4.A.4 |
| "are they independent?" | compare two numbers | P(A \| B) against P(A) | 2.7.A.1 |
| "can they both happen?" | one number | P(A ∩ B), and whether it is 0 | 2.5.A.2 |
| two draws, nothing returned | the general multiplication rule | P(A) × P(B \| A), second denominator *n* − 1 | 2.6.A.2, 1.11.A.1 |

What it does not say. The words are not infallible: *"what proportion of the bus users live in the Villages"* contains no "given" and is still a conditional probability, because "of the bus users" names the group. The reliable question is always **which group is this probability about?**

*Illustration:* "Of the type A units, what share are yes?" → conditional, 18 ÷ 24. "What is the probability a unit is type A and yes?" → joint, 18 ÷ 40. "Type A or yes?" → union, 0.700. Same table, three words, three denominators.

*Education example:* the district's four questions about Year 11, in the order a report would ask them. *"What share of our pupils both attended and passed?"* → joint, 0.450. *"Of the attenders, what share passed?"* → conditional, 0.750. *"What share attended, passed, or both?"* → union, 0.800. *"Does attending change the chance of passing?"* → an independence comparison, 0.750 against 0.650.

### Self-check on the theory

Answer each on paper, then open its reveal. If one goes wrong, reread that subsection's "what it does not say" paragraph before Part 3; everything after this leans on all seven. Checks 3 to 6 use the **40-unit** table (type A: 18 yes, 6 no; type B: 4 yes, 12 no).

**Check 1.** Write the definition of P(A | B), and say what the bar means.

:::reveal Reveal — check 1
P(A | B) = P(A ∩ B) ÷ P(B). The bar reads **"given"** — it is not a division sign — and P(B) must not be 0, because conditioning on an impossible event is not a question (2.6.A.1).
:::

**Check 2.** In a two-way table, what is the difference between P(A ∩ B) and P(B | A)?

:::reveal Reveal — check 2
**The same cell over two different totals.** P(A ∩ B) divides it by the **table** total; P(B | A) divides it by the **A row's** total. The numerator never changes; only the group you are asking about does (2.6.A.1).
:::

**Check 3.** Give P(yes | type A) and P(type A | yes) from the 40-unit table.

:::reveal Reveal — check 3
P(yes | A) = 18 ÷ 24 = **0.750** and P(A | yes) = 18 ÷ 22 = **0.818**. Different denominators, different numbers, same 18 units. If you wrote one number twice, that is the session's first trap, and Part 3 is built on it (2.6.A.1).
:::

**Check 4.** State the general multiplication rule, then derive the version for independent events.

:::reveal Reveal — check 4
P(A ∩ B) = P(A) × P(B | A) (2.6.A.2). If A and B are independent then P(B | A) = P(B) (2.7.A.1), so substituting gives **P(A ∩ B) = P(A) × P(B)**. The short form is a consequence of the two statements, not a third rule — and it is true only when independence holds.
:::

**Check 5.** Are "type A" and "yes" independent in the 40-unit table? Show your test.

:::reveal Reveal — check 5
**No.** P(yes) = 22 ÷ 40 = **0.550**; P(yes | A) = 18 ÷ 24 = **0.750**. The two are unequal, so knowing that a unit is type A changes the probability of a yes, and the events are not independent (2.7.A.1). Equivalently, P(A) × P(yes) = 0.600 × 0.550 = 0.330 against the actual joint probability 0.450.
:::

**Check 6.** P(A) = 0.600, P(yes) = 0.550 and P(A ∩ yes) = 0.450. Give P(A ∪ yes), and say why it is not 1.150.

:::reveal Reveal — check 6
0.600 + 0.550 − 0.450 = **0.700**, which matches the 28 units counted directly. The 18 units in the overlap sit inside both the 24 and the 22, so one copy is subtracted. And 1.150 is above 1, so it cannot be a probability at all (2.7.A.3, 2.4.A.3).
:::

**Check 7.** Can two events with non-zero probability be both mutually exclusive and independent? Prove your answer.

:::reveal Reveal — check 7
**No.** Mutually exclusive gives P(A ∩ B) = 0, so P(A | B) = 0 ÷ P(B) = 0; independence would require P(A | B) = P(A), which is greater than 0. The two cannot hold together, so the "both" box is always empty (2.5.A.2, 2.6.A.1, 2.7.A.1). In words: if two events cannot both happen, learning that one did tells you the other certainly did not — the largest change there is, where independence means no change at all.
:::

---

## Part 3 — Lincoln High's register: bus given the Villages

Lincoln High's travel register, unchanged since Session 8: a **census** of all **1,842 students**, each recorded with a home area and a main travel mode. Session 9 read it as probabilities for one student chosen at random from the whole roll, with 1,842 underneath every fraction. Today the office starts asking about **parts** of the roll, and the denominator moves.

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

Give every probability to 3 decimal places, worked from the counts.

### Choosing the denominator when the question says "of the"

:::yourturn
1. Session 9 gave P(bus) = 0.353 and P(Villages ∩ bus) = 0.136. What number was underneath both of those, and why?
2. The office now asks: *of the students who live in the Villages, what is the probability that one chosen at random travels by bus?* Write the probability in notation first, naming both events, then compute it.
3. Which total went underneath this time, and what in the question told you so?
:::

:::reveal Reveal — the denominator moves, the cell does not
1. **1,842**, the whole roll, because one student was chosen at random from all 1,842. Every probability in Session 9 had the table total underneath.
2. Let **B** = "the chosen student travels mainly by bus" and **V** = "the chosen student lives in the Villages". The question asks for **P(B | V)** = 250 ÷ 294 = **0.850**.
3. **294**, the Villages row total — because the question says *of the students who live in the Villages*, and the group named after "of" is the denominator. You have seen 0.850 before: in Session 8 it was a conditional relative frequency, "85.0% of Villages students take the bus". Same arithmetic, new name and new notation.

**The sentence to write down:** *P(A | B) is the same cell as P(A ∩ B) with a different number underneath — the total of the group being conditioned on, not the table total. Say "of the …" out loud first, and the denominator chooses itself.*
:::

### The same cell, by the definition and by the multiplication rule

:::yourturn
1. Check 0.850 using the definition P(A | B) = P(A ∩ B) ÷ P(B), with the numbers Session 9 gave you.
2. Now run it backwards: from P(V) and P(bus | V), find P(V ∩ bus) using the general multiplication rule. Then do it in the other order, from P(bus) and P(V | bus).
3. Session 9 asked whether 0.353 × 0.160 = 0.056 was the joint probability, and said no. Say precisely why, using today's vocabulary.
4. Give P(bus | Town) and P(bus | Suburbs) as well.
:::

:::reveal Reveal — three routes to 0.136
1. P(bus | V) = P(V ∩ bus) ÷ P(V) = 0.136 ÷ 0.160 = **0.850**. The joint probability over the probability of the condition (2.6.A.1).
2. P(V ∩ bus) = P(V) × P(bus | V) = 0.160 × 0.850 = **0.136**, which is the cell, 250 ÷ 1,842. The other order: P(V ∩ bus) = P(bus) × P(V | bus) = 0.353 × 0.384 = **0.136**. The rule does not care which event you call A (2.6.A.2).
3. Because 0.353 × 0.160 is P(bus) × P(V) — the **product form**, which requires independence. It is not independent: P(bus | V) = 0.850 is nowhere near P(bus) = 0.353, so the substitution that produces the short rule is not available here, and 0.056 is wrong by a factor of about two and a half.
4. P(bus | Town) = 85 ÷ 846 = **0.100** and P(bus | Suburbs) = 316 ÷ 702 = **0.450**. Three home areas, three very different conditional probabilities — which is already most of an independence verdict.
:::

### The governor's "0.850 of bus users live in the Villages"

A school governor, given the figure, writes to the county:

> *"The register shows that 0.850 of our bus users live in the Villages, so the village routes carry nearly the whole bus service."*

:::yourturn
1. Is the governor's sentence true? Which probability is 0.850, and which probability does the sentence actually describe?
2. Compute the number the governor meant.
3. Both probabilities come from the same 250 students. What changed?
4. Write the one true sentence for each number, beginning "Of the …".
5. Is there any rule in this course that turns 0.850 into 0.384?
:::

:::reveal Reveal — the inverted conditional, and what it costs
1. **False as written.** 0.850 is **P(bus | Villages)** — of the Villages students, the probability of the bus. The governor's sentence describes **P(Villages | bus)** — of the bus users, the probability of the Villages. Different question, different denominator, different number.
2. P(Villages | bus) = 250 ÷ 651 = **0.384**. Of the 651 bus users, 38.4% live in the Villages — well under half.
3. Only the **denominator**: 294 Villages students for the first, 651 bus users for the second. The numerator is the same 250 students both times.
4. *"Of the students who live in the Villages, 85.0% travel by bus."* *"Of the students who travel by bus, 38.4% live in the Villages."* The governor's funding case rests on the second and quotes the first, which is more than twice as large.
5. **No.** You go back to the table and divide the same 250 by the other total. There is no formula in this course for reversing a conditional probability — and the one that exists in the wider subject, Bayes' theorem, is not in the framework at all.
:::

:::note amber Where this error has already cost you marks, and where it will again
This is its third appearance. Session 8's homework B3 asked for 42 ÷ 70 and 42 ÷ 95; Session 9's diagnostic asked for 250 ÷ 294 and 250 ÷ 651; today it has notation and a name. It returns in Session 17, where a table of counts has to be read as conditional distributions in a stated direction, and on any exam question whose stem begins *"of those who …"*. The permanent fix is mechanical: **underline the group named after "of" in the question, then find its total before you write anything.**
:::

### Is travelling by bus independent of living in the Villages?

:::yourturn
1. State precisely what you compare to answer this, then answer it.
2. Say what your verdict means in words, for one student.
3. Test it again by the product route, and check that you get the same verdict.
4. Session 9 established that these two events are **not mutually exclusive**. Together with your answer to 1, which of the four boxes — independent, mutually exclusive, both, neither — do they belong in?
5. Give a pair from this table that **is** mutually exclusive, and show what happens to its conditional probability.
:::

:::reveal Reveal — not independent, and not mutually exclusive either
1. Compare **P(bus | Villages) = 0.850** with **P(bus) = 0.353**. They are unequal, so the two events are **not independent** (2.7.A.1).
2. Knowing that a student lives in the Villages raises the probability that they travel by bus from 0.353 to 0.850. Independence means knowing one event changes nothing about the other; here it changes a great deal.
3. P(V) × P(bus) = 0.160 × 0.353 = **0.056** against the actual P(V ∩ bus) = **0.136**. Unequal, so not independent — the same verdict by the equivalent route.
4. **Neither.** P(V ∩ bus) = 0.136 ≠ 0, so not mutually exclusive; 0.850 ≠ 0.353, so not independent. Most pairs of events in real data are in this box, and it needs **two** pieces of evidence, not one.
5. **"Lives in Town" and "lives in the Villages."** No student has two home areas, so P(Town ∩ Villages) = 0, and therefore P(Town | Villages) = 0 ÷ 0.160 = **0**, against P(Town) = 846 ÷ 1,842 = **0.459**. Mutually exclusive — and the collapse from 0.459 to 0 is exactly why that makes them as far from independent as a pair can be.

**The rule to write down:** *Mutually exclusive asks whether both can happen; independent asks whether one changes the other. A pair can be neither — and at Lincoln High every pair of one home area with one travel mode is.*
:::

### "Bus or Villages": the union Session 9 counted by hand

:::yourturn
1. Count the students who travel by bus **or** live in the Villages, straight off the table, exactly as Session 9 did. Give the probability.
2. Now reach the same answer from P(bus), P(Villages) and P(bus ∩ Villages).
3. What are the 250 students doing in that subtraction? What does 0.353 + 0.160 = 0.513 claim, in students?
4. Does "or" here include the students who are both?
5. Apply the union rule to a mutually exclusive pair: P(lives in Town ∪ lives in the Villages). Check it by counting.
:::

:::reveal Reveal — one rule, two routes, and the 250 counted twice
1. The three bus cells, 85 + 316 + 250 = 651, plus the two remaining Villages cells, 38 + 6 = 44, gives **695** students, so the probability is 695 ÷ 1,842 = **0.377**.
2. P(V ∪ bus) = P(V) + P(bus) − P(V ∩ bus) = 0.160 + 0.353 − 0.136 = **0.377**. The rule and the count agree, which is the point of doing both (2.7.A.3).
3. The 250 were counted once inside the 294 Villages students and once inside the 651 bus users, so one copy must be removed. 0.513 claims 0.513 × 1,842 ≈ **945** students are in the union, when 695 are — an overstatement of exactly 250. Note that 0.513 is a legal-looking probability, so the 0-to-1 bound will not rescue you here.
4. **Yes.** The statistical "or" is inclusive: A ∪ B contains A alone, B alone, and both (2.7.A.2).
5. 0.459 + 0.160 − 0 = **0.619**, matching 846 + 294 = 1,140 over 1,842 = 0.619. The rule still applies; it just subtracts zero. **There is only one union rule.**
:::

### The paragraph the office may now write

:::yourturn
Write one paragraph for the governors, using today's rules: a conditional probability in each direction, an independence verdict with its evidence, and a union. Then list what the paragraph may **not** claim.
:::

:::reveal Reveal — the paragraph, and its limits
*"Of Lincoln High's 294 students who live in the Villages, the probability that one chosen at random travels by bus is 250 ÷ 294 = 0.850. Of the 651 students who travel by bus, the probability that one lives in the Villages is 250 ÷ 651 = 0.384; the two figures answer different questions. Travel mode is not independent of home area: the probability of travelling by bus rises from 0.353 for a student chosen from the whole roll to 0.850 for a Villages student. The probability that a randomly chosen student travels by bus or lives in the Villages, or both, is 0.353 + 0.160 − 0.136 = 0.377."*

**It may not claim** that living in the Villages **causes** bus use — these are observational records with no random assignment (Session 7); that the figures describe any other school (Session 6); or that 0.850 and 0.384 are interchangeable. And if the county asks how many buses the village routes need, the answer is neither probability but the **count**, 250 students: a conditional probability is about one chosen individual, not about capacity.
:::

---

## Part 4 — Sorting twelve event pairs, on your own

This is the master plan's activity for this session, adapted from 5 Steps content tip 14. Twelve pairs of events go into four boxes — **independent**, **mutually exclusive**, **both**, **neither** — and then one question settles the confusion for good.

Two warnings before you start. **One of the four boxes will stay empty**, and that is the designed outcome, not a sign you have gone wrong. And a verdict with no number behind it is worth nothing: the intersection decides *mutually exclusive*, the comparison of a conditional with an unconditional probability decides *independent*, and a pair needs **both** tests before you may call it *neither*.

### Three recognition cards: name the rule, do not calculate

The course description's activity for topics 2.4 to 2.7 asks you to identify only the **formula** needed, with no arithmetic. Session 9 ran the first two cards; these are the other three. For each, name the rule, give its code, and say which numbers from the library table below would go into it — then stop.

| Branch | Print only | E-books only | Both | Total |
|---|---|---|---|---|
| Central | 90 | 15 | 45 | **150** |
| Westside | 60 | 10 | 30 | **100** |
| **Total** | **150** | **25** | **75** | **250** |

:::yourturn
One member is chosen at random from the 250. Name the rule for each card. No calculation.

1. *"Of the Central members, what is the probability that the chosen member borrows e-books only?"*
2. *"What is the probability that the chosen member is from Central **and** borrows both formats?"*
3. *"Is 'borrows both formats' independent of branch?"*
:::

:::reveal Reveal — the three rules named
1. **Conditional probability**, P(A | B) = P(A ∩ B) ÷ P(B), **2.6.A.1**. The numbers: 15, over the Central row total of 150.
2. **The general multiplication rule**, P(A ∩ B) = P(A) × P(B | A), **2.6.A.2** — or the cell over the table total, which is quicker when you have the table. The numbers: 0.600 × (45 ÷ 150), or 45 over 250.
3. **The definition of independence**, **2.7.A.1**: compare P(both formats | Central) with P(both formats). The numbers: 45 ÷ 150 against 75 ÷ 250.

If you calculated anyway, the answers are 0.100, 0.180 and *yes, independent* — but the skill being drilled is the recognition, and a student who can only reach the rule through the arithmetic has not reached it.
:::

### The twelve pairs, and the four boxes

The three sources are the library table above, **Lincoln High's travel register** from Part 3, and **one roll of a fair six-sided die**. One individual, or one roll, chosen at random each time.

:::yourturn
Draw four boxes — *independent*, *mutually exclusive*, *both*, *neither* — and put each pair in one of them. Beside every pair write **the number or the comparison** that decides it, not just the verdict. Expect this to take fifteen minutes; do not reveal until all twelve are placed and justified.

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
:::

:::reveal Reveal — the sort, with the deciding numbers
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
| 9 | **Neither** | P(V ∩ bus) = 250 ÷ 1,842 = 0.136, not 0; and P(bus \| V) = 0.850 against P(bus) = 0.353 |
| 10 | **Neither** | P(Town ∩ walk) = 558 ÷ 1,842 = 0.303, not 0; and P(walk \| Town) = 558 ÷ 846 = 0.660 against P(walk) = 669 ÷ 1,842 = 0.363 |
| 11 | **Neither** | P(Suburbs ∩ bus) = 316 ÷ 1,842 = 0.172, not 0; and P(bus \| Suburbs) = 316 ÷ 702 = 0.450 against 0.353 |
| 12 | **Neither** | P(print ∩ e-books) = P(borrows both formats) = 0.300, not 0; and P(print \| e-books) = 75 ÷ 100 = 0.750 against P(print) = 225 ÷ 250 = 0.900 |
| | **Both** | **empty** |

**Four in each of three boxes, and nothing in the fourth.** Three things to notice:

- Pairs 5 to 8 are all **two levels of one variable**, which is where mutually exclusive pairs almost always come from. Pairs 1 to 4 and 9 to 11 take one level from each of two variables, which is where independence and "neither" live.
- **Pair 12 is the hard one.** Both events come from the same variable and they still overlap, because "borrows print" and "borrows e-books" both include the 75 members who do both. If you sorted it as mutually exclusive you read "print" as "print only"; if you sorted it as independent you did not compare 0.750 with 0.900.
- The library pairs are independent and the Lincoln High pairs are not, and that is a fact about these data rather than about libraries: the library's two branches happen to have identical borrowing profiles — 0.600, 0.100, 0.300 in both rows — while Lincoln High's home areas have very different travel profiles.

**One more check on yourself.** If you placed pair 1 in *independent* because "branch and format sound unrelated", you got the right box for the wrong reason, and the same reasoning puts pair 9 in the wrong box, since Villages and bus also sound unrelated. The words never decide; the numbers do.
:::

### Why the "both" box has to be empty

:::yourturn
1. Prove that no two events with non-zero probability can be both mutually exclusive and independent. Three lines.
2. Say the same thing in one sentence with no symbols in it.
3. Now run it the other way: if A and B are independent and both have non-zero probability, can they be mutually exclusive?
4. Where exactly does the condition "non-zero probability" get used?
:::

:::reveal Reveal — the two-line proof, both ways round
1. Suppose P(A) > 0, P(B) > 0, and A and B are mutually exclusive. Then P(A ∩ B) = 0 (2.5.A.2), so P(A | B) = 0 ÷ P(B) = **0** (2.6.A.1). Independence would require P(A | B) = P(A) > 0 (2.7.A.1). Since 0 ≠ P(A), they are **not independent**.
2. If two events cannot both happen, then learning that one happened tells you the other certainly did not — which is the largest possible change to its probability, and independence means no change at all.
3. **No.** If they are independent then P(A ∩ B) = P(A) × P(B), a product of two positive numbers, which cannot be 0. **Independent events with non-zero probability must overlap** — so the implication fails in both directions, which is what makes the box empty rather than merely unusual.
4. At the **last step** of 1, and at the "positive numbers" step of 3. If P(A) were 0 then P(A | B) = 0 = P(A), and the pair would be both, trivially. That is why every exam question on this specifies non-zero probabilities.
:::

---

## Part 5 — St Mary's clinic: unions, and an audit of two records

St Mary's outpatient clinic from Sessions 6 to 9. Session 9 built the sample space of one appointment from the clinic's **1,000 records** and cross-tabulated them by whether the appointment was a patient's **first** or a **follow-up**. The manager now wants two things Session 9 could not supply: the probability that an appointment is *either* a first appointment *or* a missed one, and the probability that two records pulled for audit are both missed appointments.

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

### The question Session 9 left hanging on this table

:::yourturn
1. *Is a first appointment more likely to be missed than a follow-up?* Compute the two numbers that answer it, and write the manager's sentence.
2. Now give P(first appointment | missed without notice). Which total did you use, and what does the answer mean?
3. 0.150 and 0.600 come from the same 60 records. Which of them tells the manager whether to send extra reminders to new patients, and what does the other one tell her?
4. Check your 0.150 against the definition of conditional probability, and then produce P(first ∩ missed) from the general multiplication rule.
:::

:::reveal Reveal — two directions, two different uses
1. **P(missed | first) = 60 ÷ 400 = 0.150** and **P(missed | follow-up) = 40 ÷ 600 = 0.067**. Each is a cell over its own row total. *"Of the clinic's first appointments, 15.0% were missed without notice, against 6.7% of follow-ups — a first appointment is more than twice as likely to be missed."*
2. **P(first | missed) = 60 ÷ 100 = 0.600**, using the **missed** column total. Of the 100 missed appointments, 60.0% were first appointments.
3. **0.150** is the one to act on: it is the risk attached to a first appointment, so it is what justifies extra reminders for new patients. **0.600** describes who the missed appointments *were*, which is a different and also useful fact — it says where the losses are concentrated. Writing both sentences out in full, each beginning "of the", is the way to keep them apart.
4. P(missed | first) = P(missed ∩ first) ÷ P(first) = 0.060 ÷ 0.400 = **0.150** (2.6.A.1). And P(first ∩ missed) = P(first) × P(missed | first) = 0.400 × 0.150 = **0.060**, which is the cell, 60 ÷ 1,000 (2.6.A.2).
:::

### The administrator's 0.500 for "a first appointment or a missed one"

The clinic's administrator, asked how often an appointment is either a first appointment or a missed one, writes:

> *"P(first) = 0.400 and P(missed) = 0.100, so P(first or missed) = 0.500. Half of all appointments are either a new patient or a no-show."*

:::yourturn
1. Settle it by **counting records** before you use any rule. What is the right answer?
2. Where did the extra 0.060 come from?
3. Write the union rule and apply it.
4. Why did Session 9's 0-to-1 bound not catch this error, and what check should you use instead?
5. Does the clinic's 0.440 include the 60 records that are both?
:::

:::reveal Reveal — the double count, on a number that looks legal
1. Count: 400 first appointments plus the 40 missed follow-ups = **440** records, so the probability is **0.440**, not 0.500.
2. From the **60 records that are both** a first appointment and a missed one. They sit inside the 400 and inside the 100, so the sum counts them twice.
3. P(first ∪ missed) = P(first) + P(missed) − P(first ∩ missed) = 0.400 + 0.100 − 0.060 = **0.440**, matching the count (2.7.A.3).
4. Because **0.500 is a legal probability**. The bound only catches a double count when the sum exceeds 1, as it did on Session 9's library card. Here nothing looks wrong, so the check has to be structural: **before adding two probabilities, ask whether the two events can both happen.** If they can, subtract the joint probability once.
5. **Yes** — the statistical "or" is inclusive, so A ∪ B contains A alone, B alone and both (2.7.A.2). If you wanted "one but not the other" you would subtract the overlap twice, giving 0.440 − 0.060 = 0.380 — legitimate arithmetic, but not what P(A ∪ B) means, and no exam question asks for it under that name.
:::

### Which of the clinic's pairs may simply be added

:::yourturn
1. Give P(cancelled in advance ∪ missed without notice), and say why.
2. Is there a second union rule, for mutually exclusive events?
3. Session 9 computed P(attended) — the patient came on time or late — as 0.770 + 0.070 = 0.840. Which kind of calculation was that, and why was it available without today's rule?
4. Give P(attended ∪ first appointment). Check it by counting records.
5. Is "attended" independent of "first appointment"?
:::

:::reveal Reveal — one rule, sometimes with a zero in it
1. 0.060 + 0.100 − 0 = **0.160**, with no subtraction needed because an appointment cannot be both: P(cancelled ∩ missed) = 0 (2.5.A.2). Check: 60 + 100 = 160 records over 1,000.
2. **No — there is one rule.** P(A) + P(B) − P(A ∩ B) with P(A ∩ B) = 0 *is* P(A) + P(B). The mutually exclusive case is the general rule with a zero in it, which is why you only ever have to remember one thing.
3. A **union of two mutually exclusive outcomes**. Nothing had to be subtracted, so Session 9 could do it with counting alone.
4. P(attended) = 0.840 and P(first) = 0.400; the overlap is the first appointments that were attended, 280 + 32 = 312, so 0.312. The union is 0.840 + 0.400 − 0.312 = **0.928**. By counting: 840 + 400 − 312 = **928** records. If you got 1.240 you added without subtracting, and the 0-to-1 bound caught you that time.
5. **No.** P(attended | first) = 312 ÷ 400 = **0.780**, against P(attended | follow-up) = 528 ÷ 600 = **0.880** and P(attended) = **0.840**. Knowing an appointment is a first appointment lowers the probability of attendance, so the two are not independent (2.7.A.1).
:::

### Are missed appointments independent of first appointments?

:::yourturn
1. State the independence question for this pair precisely, then answer it with the comparison.
2. Check it with the product route — and then say why the product is allowed as a **test** but not as a **method** here.
3. Give all three verdicts for this pair: mutually exclusive, independent, or neither — with the evidence for each.
4. What should the clinic actually do with 0.150 against 0.100, and what may it not conclude?
:::

:::reveal Reveal — not independent, and why the product is a test and not a method
1. Are "first appointment" and "missed without notice" independent? Compare **P(missed | first) = 0.150** with **P(missed) = 0.100**. Unequal, so **not independent**.
2. P(first) × P(missed) = 0.400 × 0.100 = **0.040**, against the actual joint probability **0.060**. As a *test*, that mismatch **is** the evidence of non-independence. As a *method* it would have handed you 0.040 for the joint probability — wrong by a third — because the product form requires the very independence it is being used to check.
3. **Neither.** P(first ∩ missed) = 0.060, which is not 0, so not mutually exclusive; and 0.150 ≠ 0.100, so not independent. A mutually exclusive pair here would be "cancelled in advance" and "missed without notice", or "first appointment" and "follow-up".
4. Target reminders at **first appointments** — 0.150 against 0.067 is the operational fact. It may **not** conclude that being a new patient *causes* the no-show: these are observational records with no random assignment, so Session 7's rule applies, and it is an association.
:::

### Two records drawn for audit, without replacement

The clinic's auditor pulls **two different records at random** from the 1,000. One record cannot be pulled twice, so this is sampling **without replacement** (1.11.A.1).

:::yourturn
1. P(the first record pulled is a missed appointment)?
2. Given that it was, P(the second one is too)? Think about what is left.
3. P(both are missed appointments)? Name the rule.
4. What would 0.100 × 0.100 have given, and how wrong is it? Why is that *not* an argument for using it?
5. In one sentence, why are the two draws not independent?
6. P(at least one of the two is a missed appointment)?
7. Finally, finish the Session 9 homework question E2 that could not be done then: four library members are chosen at random, each borrowing both formats with probability 0.300. Give P(none of the four borrows both formats) and P(at least one does).
:::

:::reveal Reveal — the audit, and the promise from Session 9 kept
1. 100 ÷ 1,000 = **0.100**.
2. 999 records remain and 99 of them are missed, so P(second missed | first missed) = 99 ÷ 999 = **0.099**.
3. The **general multiplication rule**: P(both) = P(first missed) × P(second missed | first missed) = 0.100 × 0.099 = **0.010** — 0.0099 to four places (2.6.A.2).
4. 0.100 × 0.100 = **0.0100**, which agrees to three decimal places and is wrong by about one per cent of itself. It is **not** an argument for using it: here it barely matters because one record out of a thousand changes almost nothing, but in the summer-school lottery the same shortcut moved 0.074 to 0.078, and in a box of ten units it moved 0.067 to 0.090. You do not get to decide after the fact which populations were large enough.
5. Because the first record is not returned, so knowing it was a missed appointment leaves one fewer missed record among one fewer record, and the second probability drops from 0.100 to 0.099 — independence would require no change at all.
6. Use the complement of "neither is missed": P(neither) = (900 ÷ 1,000) × (899 ÷ 999) = 0.900 × 0.900 = **0.810**, so P(at least one) = 1 − 0.810 = **0.190** (2.4.A.4 with 2.6.A.2).
7. With one member drawn at a time from a large membership the four draws are taken as independent, so the derived product form applies four times: P(none borrows both) = 0.700 × 0.700 × 0.700 × 0.700 = **0.2401**, and P(at least one) = 1 − 0.2401 = **0.7599**. The sheet's wrong answer was 1 − 0.300 = 0.700, which is the probability for **one** named member — close to 0.7599 by accident, which is exactly why the reasoning had to be refused rather than the number checked.
:::

### The note St Mary's may now write about two appointments

:::yourturn
Write the manager's note for the board: the two conditional probabilities with their direction stated, the union with its subtraction shown, and the audit probability. Then say which single sentence the clinic should act on, and what the note must not say.
:::

:::reveal Reveal — the note, and what it may not claim
*"Of the clinic's 400 first appointments, 15.0% were missed without notice, against 6.7% of the 600 follow-ups; a first appointment is more than twice as likely to be missed. Of the 100 missed appointments, 60.0% were first appointments. The probability that a randomly chosen record is a first appointment or a missed appointment, or both, is 0.400 + 0.100 − 0.060 = 0.440 — not 0.500, which counts the 60 records in both groups twice. For two different records drawn at random, the probability that both are missed appointments is 0.100 × 0.099 = 0.010."*

**Act on the first sentence:** 0.150 against 0.067 is the operational fact, and it points at reminders for new patients. The note must **not** say that first appointments cause missed appointments, must not generalise beyond St Mary's, and must not offer 0.600 as the chance that a new patient misses — that is the other direction of the conditional, and it is the governor's error from Part 3 in a new coat.
:::

---

## Part 6 — On your own: the café's members, conditioned on the drink

No help on this part, and no checking answers until all seven are done. The café from Sessions 2 to 9 has **1,260 loyalty members**, and a random sample of **240** of them was classified by usual drink and by whether they usually add food — the same table as Session 9's solo case, with harder questions.

| Usual drink | Adds food | No food | Total |
|---|---|---|---|
| Coffee | 84 | 66 | **150** |
| Tea | 22 | 28 | **50** |
| Cold drink | 14 | 26 | **40** |
| **Total** | **120** | **120** | **240** |

:::yourturn
One of the 240 sampled members is chosen at random. Give every probability to 3 decimal places, from the counts.

1. Give P(adds food | coffee) and P(coffee | adds food). Say in words what each is about, and why they differ.
2. Use the general multiplication rule to find P(tea ∩ adds food) from P(tea) and P(adds food | tea), then check it against the cell.
3. Is "usual drink is coffee" independent of "adds food"? Show your test and state the verdict.
4. Give P(coffee ∪ adds food), both by the rule and by counting members.
5. The manager writes: *"62.5% of members drink coffee and 50% add food, so 112.5% of members do one or the other."* Name the **two** things wrong with that sentence.
6. Two different members are chosen at random for a tasting panel. Give the probability that both usually drink coffee, and say why 0.625 × 0.625 is not the right calculation.
7. Give a pair of events from this table that is mutually exclusive, and show what happens to the conditional probability when you condition on one of them.
:::

:::reveal Reveal — the café answers, with the marks they carry
1. **P(adds food | coffee) = 84 ÷ 150 = 0.560** — of the 150 coffee members, 56.0% add food. **P(coffee | adds food) = 84 ÷ 120 = 0.700** — of the 120 food-adding members, 70.0% drink coffee. The same 84 members over two different groups, so two different numbers; neither can be got from the other without returning to the table.
2. P(tea) = 50 ÷ 240 = **0.208** and P(adds food | tea) = 22 ÷ 50 = **0.440**, so P(tea ∩ adds food) = 0.208 × 0.440 = **0.092**. The cell gives 22 ÷ 240 = 0.092. They agree, as 2.6.A.2 guarantees.
3. **Not independent.** P(adds food) = 120 ÷ 240 = **0.500**; P(adds food | coffee) = **0.560**. Unequal, so knowing a member drinks coffee changes the probability that they add food. (Equivalently, P(coffee) × P(adds food) = 0.625 × 0.500 = 0.313 against the actual 0.350.)
4. By the rule: 0.625 + 0.500 − 0.350 = **0.775**. By counting: the 150 coffee members plus the 36 non-coffee members who add food (22 + 14) gives 186, and 186 ÷ 240 = **0.775** — equivalently 150 + 120 − 84 = 186.
5. First, **the overlap has not been subtracted**: the 84 members who do both are counted in the 62.5% and again in the 50%, and the correct figure is 0.775 (2.7.A.3). Second, **112.5% is not a possible probability at all** — the 0-to-1 bound, 2.4.A.3, rules it out, so the sentence can be refused before any recomputation. Both faults are worth stating.
6. Two **different** members means **without replacement**. P(first drinks coffee) = 150 ÷ 240 = **0.625**; given that, 149 of the remaining 239 do, so P(second | first) = 149 ÷ 239 = **0.623**, and P(both) = 0.625 × 0.623 = **0.390**. The product 0.625 × 0.625 = 0.391 assumes the draws are independent, which they are not: taking one coffee member out leaves one fewer among one fewer. Here the difference is small; the method is still wrong.
7. **"Usual drink is coffee" and "usual drink is tea"** (or any two drinks). Each member has exactly one usual drink, so P(coffee ∩ tea) = 0 ÷ 240 = **0** and the events are mutually exclusive. Conditioning collapses the probability: P(coffee | tea) = 0 ÷ 0.208 = **0** against P(coffee) = **0.625** — which is also the proof that they are not independent.

**Watch for, in your own work:** the two conditionals in question 1 given as the same number — the session's first trap, which is why it comes first; 0.625 × 0.500 used in question 2 or 3 instead of 0.625 × 0.560; a verdict in question 3 with no numbers ("the menu has nothing to do with food"); 1.125 left standing in question 4; only one of the two faults named in question 5 — the 0-to-1 bound is the faster of them; the product form used in question 6 because the answers "look the same anyway"; and a pair taken from two different variables in question 7, which will not give an intersection of 0 in this table.
:::

---

## Part 7 — Explain it back

Say this out loud, to a person if you can and to an empty room if not. Speaking it is the test; reading it is not.

:::yourturn
> *"Explain how a conditional probability differs from a joint probability, using the same cell of a table for both. Then explain how you decide whether two events are independent, and why that is a different question from whether they are mutually exclusive. Finish by saying where the rule P(A ∩ B) = P(A) × P(B) comes from and when you are allowed to use it."*

Say it all the way through before revealing, then check yourself against the five things a good answer contains.
:::

:::reveal Reveal — the five things a good answer contains
1. **Conditional probability.** P(A | B) = P(A ∩ B) ÷ P(B), which in a table means the same cell divided by the total of the group being conditioned on rather than by the table total — 250 ÷ 294 rather than 250 ÷ 1,842 (2.6.A.1).
2. **The two directions are different numbers.** P(bus | Villages) = 0.850 and P(Villages | bus) = 0.384 share a numerator and nothing else, and no rule in this course converts one into the other; you go back to the table.
3. **Independence is tested by comparison.** Compare P(A | B) with P(A): equal means independent, unequal means not independent. At Lincoln High, 0.850 against 0.353 — not independent. In the library, 0.600 against 0.600 — independent.
4. **It is a different question from mutual exclusivity.** *Mutually exclusive* asks whether both can happen (test: is P(A ∩ B) = 0?); *independent* asks whether one changes the other. Two events with non-zero probability can never be both, because mutual exclusivity forces P(A | B) = 0 while independence requires P(A | B) = P(A) > 0 — and most pairs are neither.
5. **The product form is derived, not given.** The course description states P(A ∩ B) = P(A) × P(B | A) (2.6.A.2); substituting P(B | A) = P(B), which is what independence means (2.7.A.1), produces the short version. So it may be used only when independence has been established or assumed — never because the question contains the word "and".

If you recited the product form as a rule in its own right, write the derivation out again before you move on. If you said two events are independent "because they are unrelated", go back to Part 4 and compare pair 1 with pair 9: both sound unrelated, and only one of them is. And if the two conditional probabilities came out as one number, put the register back in front of you and write both sentences in full, each beginning *"of the"*.
:::

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
