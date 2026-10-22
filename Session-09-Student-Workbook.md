# Session 9 — Probability, Complements and Mutually Exclusive Events

**AP Statistics · Twenty-Hour Course · Student edition, to work through on your own**
**CED Topics 2.4, 2.5 · About 179 minutes, plus homework**

---

## How to use this

Session 8 estimated a probability by running a random process many times and taking a relative frequency. This session gives you the first rules that **calculate** a probability instead, and there are only two: count the outcomes in the event when every outcome is equally likely, and subtract from 1 to get the complement. Alongside them sits one definition with a test attached — the **joint probability** P(A ∩ B), and the claim that two events are **mutually exclusive**, which is true exactly when that joint probability is 0.

This is a shorter session than the last three, because topics 2.4 and 2.5 are smaller: two learning objectives and six statements of required knowledge. Nothing has been left out and nothing has been pushed into the homework. The time goes where the marks go — a list of outcomes that overlaps, a counting formula used where the outcomes are not equally likely, and the words *mutually exclusive* treated as though they meant *unrelated*. The last of those matters most, because Session 10 puts **independence** on top of it, and the two are easy to fuse and hard to separate afterwards.

:::note amber Write first, then reveal
Every **Your turn** box asks you to do something before the text shows you the answer. **Do it on paper first.** Every probability, every justification and every verdict is hidden behind a reveal so that you cannot read it before you commit. A wrong answer you wrote yourself, and then corrected, stays with you; a right one you read does not.
:::

**What you need:** paper, a pen and a calculator. There is no interactive tool in this session: complements and mutually exclusive events are facts about a fixed sample space, not processes that change, so a table does the job a simulation would do badly.

### How this maps to your tutor's document

Working alone with a pen is slower than working with a tutor, so each part is given about a quarter longer than the tutor's segment. Take the time.

| Your section | Tutor's section | Minutes |
|---|---|---|
| Part 1 — Your Session 8 homework, and a warm-up | 0–12 Homework debrief and diagnostic | 15 |
| Part 2 — Theory: probability, complements and mutually exclusive events | 12–47 Theory — probability, complements and mutually exclusive events | 44 |
| Part 3 — Lincoln High's travel register, one student at random | 47–79 Scenario A | 40 |
| Part 4 — Think-Aloud with the library's borrowing records, on your own | 79–95 Activity | 20 |
| Part 5 — St Mary's clinic: one appointment at random | 95–123 Scenario B | 35 |
| Part 6 — On your own: the café's loyalty members | 123–135 Solo case | 15 |
| Part 7 — Explain it back | 135–143 Teach it back | 10 |
| **Total** | **143 minutes** | **179** |

If your tutor has not yet set the **Session 7 test**, take it before Part 1: 20 questions, 35 minutes, timed, answer key closed.

:::note red Words you may have met that the course description does not use
The **addition rule** is a prep-book name for P(A ∪ B) = P(A) + P(B) − P(A ∩ B); the course description calls it *the probability of the union* and puts it in topic **2.7**, which is Session 10. It is not in this session, and you do not need it for anything on these pages. **Venn diagrams** and **tree diagrams** are never named by the course description and no exam question requires either — the representation it does name for two categorical variables is the **two-way table**, which is what this session uses. **Exhaustive**, **complementary events** as a noun phrase and **odds** do not appear either; the course description's wording is *the complement of an event E*. **Law of averages** and **gambler's fallacy**, from Session 8, remain prep-book names for a misreading of the law of large numbers.
:::

---

## Part 1 — Your Session 8 homework, and a warm-up

Get out your marked Session 8 homework and make two lists: the questions you got **wrong**, and the questions you marked with a **?**, including the ones that turned out right.

**Two specific things to check.** They are two of the likeliest errors on that sheet, and both come back today in a new form.

- **B3: did you give the same number twice?** "Of the Year 7 students, what proportion have school lunch?" is 42 ÷ 70 = 0.600; "of the school-lunch students, what proportion are Year 7?" is 42 ÷ 95 = 0.442. Same 42 students, two different totals. Today every probability is a count over a total, so install the habit now: **name the group you are counting out of, out loud, before you write the fraction.** Today that group is almost always the whole sample space, which is easier — and that is exactly why this error hides until Session 10 brings it back as conditional probability.
- **D5: whose denominator was it?** The student who counted 11 winning digits out of 40 and wrote 0.275 was counting **sleeves** when the question asked about **customers**. Today the same discipline appears as a question you ask of every scenario: *what are the equally likely things?* At Lincoln High they are the 1,842 students; at St Mary's they are the 1,000 appointment records — and they are **not** the four outcomes on the clinic's list.

If you put a **?** on E1: *"we've been lucky three times, so the next session is bound to overflow"* is wrong because the sessions are independent, and the law of large numbers says nothing about the next one. Today recalls the law of large numbers by name in Part 5 and does not re-teach it.

### Warm-up: four questions on shares, chance and "not"

:::yourturn
Four questions. Answer all four on paper before revealing.

1. From Session 8's Lincoln High table: of the 294 Villages students, 250 travel by bus. What proportion is that? And of the 651 bus users, what proportion live in the Villages?
2. St Mary's records show 100 of 1,000 appointments were missed. What does 100 ÷ 1,000 give you, and what is it an estimate of?
3. A café sells coffee, tea and cold drinks. One loyalty member is picked at random. Is the probability that their usual drink is tea equal to one third?
4. The probability that a Lincoln High student travels by bus is 0.353. What is the probability that a student does **not** travel by bus?
:::

:::reveal Reveal — and what your answers mean
| If you said | It means | Do this |
|---|---|---|
| **1:** 0.850, and 0.384 | Session 8's conditioning held | Carry on at pace; today's denominators are easier, and Session 10 brings these two back as conditional probabilities |
| **1:** the same number twice, or you hesitated | The Session 8 homework's B3 error is still live | Read Part 2's *Probabilities read off a two-way table* twice, and say the group out loud before every fraction you write today |
| **2:** 0.100, an estimate of the probability that a patient misses | Session 8's 2.3.A.5–6 held | Part 5 uses exactly that number |
| **2:** "the probability is 0.100", with no "estimate" | You are treating a relative frequency as the probability itself | Reread Session 8's *Probability as long-run relative frequency, estimated from data (2.3.A.5–6)* before Part 2 |
| **3:** no — only if the three drinks are equally popular | You already have 2.4.A.2's condition | Read *When the outcomes are not equally likely* anyway; you will need it in Part 5 |
| **3:** yes, three drinks, so one third | The equally-likely reflex, and today's second trap | Read *Theoretical probability when every outcome is equally likely* and the subsection after it slowly. It is Part 5's trap and Part 6's question 5 |
| **4:** 0.647, because they add to 1 | The complement is already intuitive | Spend your time on *Complements of compound events* instead; that is where it breaks |
| **4:** 0.5, or "I'd need the other numbers" | You have no complement rule yet | *The complement of an event, and the three ways to write it* is the core of this session |
:::

---

## Part 2 — Theory: probability, complements and mutually exclusive events

Every idea the session uses is stated here, each with its code from the course description, the rule, the formula where there is one, and what the rule does **not** say, which is where most marks are lost. Thirteen subsections, for six statements of required knowledge and the three errors that cost most.

**Read this part in full before Part 3.** Each subsection carries two examples, and they do different work. The *Illustration* is deliberately bare, so you can see the structure with nothing to distract you. The *Education example* is a real study of the kind this course is about, so you can see the same rule doing something. Read both; if one clicks and the other does not, that is fine. The bare ones here are a fair six-sided die and one made-up table of 30 units. Parts 3 to 7 then apply the same rules to Lincoln High, the library, St Mary's and the café. There is nothing to write until the self-check at the end. When a later part says "from Part 2", this is where to look.

**What this part builds on, by name.** From Session 8: *Random process, outcome and event (2.3.A.1–3)*, *Probability as long-run relative frequency, estimated from data (2.3.A.5–6)*, *The law of large numbers (2.3.A.7)*, and the three relative frequencies of a two-way table (2.2.A.1–3). From Session 1: rf = f ÷ n. None of them is re-taught.

**The education examples form one strand**, continued from Sessions 6 to 8: the **district** — its summer-school lottery of 50 applicants for 30 places, and its 400 Year 11 pupils cross-tabulated by revision attendance and result — and the **university's first-year statistics module** of 318 students, whose scripts go to a marking moderation panel.

### Random process, outcome and event, recalled from Session 8 (2.3.A.1–3)

A **random process** generates results determined by chance. An **outcome** is the result of one trial of a random process. An **event** is a **collection of outcomes**.

This is retrieval, not new teaching: the student met all three in Session 8's simulation. What changes today is that the event's probability will be **calculated** rather than estimated from trials. Make the student say the three definitions back before moving on, because every rule below is phrased in them.

What it does not say. An event need not be a single outcome; "an even score" is one event covering three outcomes. And an event is a *collection*, which means it can be described in words — "at least one", "not a bus user" — without anyone listing its outcomes. Deciding which outcomes a worded event collects is most of the work in this session.

*Illustration:* rolling a fair six-sided die once is the random process. "A 4" is an outcome. "An even score" is an event, the collection {2, 4, 6}.

*Education example:* the district has 30 places on a summer school and 50 applicants, so it allocates them by lottery, drawing names one at a time. The **random process** is the draw. The **outcome** of the first draw is one particular applicant's name. An **event** is a collection of those outcomes, such as *"the first name drawn is from one of the two smallest schools"* — one description covering the 14 applicants from those two schools.

### The sample space, and why its outcomes must not overlap (2.4.A.1)

The **sample space** of a random process is the set of all possible **nonoverlapping** outcomes. The **probability of the sample space is 1**.

Two requirements, both load-bearing. *All possible*: nothing that could happen is left off the list. *Nonoverlapping*: no two entries on the list can happen together. A list that fails either test is not a sample space, and the counting rule in the next subsection will give nonsense when applied to it.

:::checks
every possible outcome appears in the list
no two listed outcomes can both happen
P(sample space) = 1
:::

What it does not say. It does not say the outcomes are equally likely — that is a separate condition, imposed in the next subsection and often absent. It does not say there is one correct sample space for a given situation: for two coin tosses, {HH, HT, TH, TT} and {0 heads, 1 head, 2 heads} are both legitimate sample spaces, and they are not equally likely in the same way. And "the probability of the sample space is 1" is the most useful check in the topic: if the probabilities you have written down do not add to 1, either an outcome is missing or two of them overlap.

*Illustration:* for one roll of a fair die the sample space is {1, 2, 3, 4, 5, 6}, and 1/6 × 6 = 1. The list {1, 2, 3, 4, 5, 6, even} is **not** a sample space: "even" overlaps with 2, 4 and 6.

*Education example:* for the first name drawn in the district's lottery, the sample space is the **50 applicants** — every applicant could be drawn, and only one is. A governor who instead lists the outcomes as *{a Year 5 applicant, a Year 6 applicant, an applicant from the two smallest schools}* has not written a sample space: an applicant can be in Year 6 **and** from one of the two smallest schools, so the entries overlap, and the three probabilities will add to more than 1.

### Theoretical probability when every outcome is equally likely (2.4.A.2)

If all outcomes in the sample space are **equally likely**, then the **theoretical probability** that an event E will occur is the number of outcomes in event E divided by the total number of outcomes in the sample space. The probability of event E occurring is written **P(E)**.

:::formula
P(E) = (number of outcomes in event E) ÷ (total number of outcomes in the sample space)
:::

*Number of outcomes in E* is the count of the sample space's outcomes that make E happen. *Total number of outcomes in the sample space* is the count of everything that could happen. The notation P(E) is read "the probability of E", and E is always named in words somewhere on the page.

What it does not say. The formula is only licensed by the **"if"** at the front of the sentence, and the course description puts that clause in writing. Where the outcomes are not equally likely, counting them gives a number that is not a probability at all. The counting is of **outcomes**, not of categories, not of digits and not of trials. And the word *theoretical* is deliberate: this probability comes from the structure of the process, not from data — which is why it needs no trials, where Session 8's estimate needed thousands.

*Illustration:* one roll of a fair die, E = "an even score". Three of the six equally likely outcomes are in E, so P(E) = 3 ÷ 6 = **0.5**.

*Education example:* in the district's lottery every one of the 50 applicants is equally likely to be the first name drawn, and 14 of them come from the two smallest schools. So P(the first name is from one of the two smallest schools) = 14 ÷ 50 = **0.280**. The "equally likely" clause is what the lottery buys: that is the whole reason the district draws names rather than letting head teachers nominate.

### When the outcomes are not equally likely (2.4.A.2)

Most real sample spaces are not equally likely, and then the counting formula does not apply. Two moves are available, and both are in the course already.

First, **look for a level at which the outcomes are equally likely.** One individual chosen at random from a population of *N* makes the *N* individuals equally likely, so P(E) = (individuals in E) ÷ N, even though the categories they fall into are wildly unequal. Second, **take the probability from data**: Session 8's 2.3.A.5–6 says a relative frequency from empirical data estimates the probability, so each outcome's probability can be read off a frequency table.

What it does not say. Neither move makes unequal outcomes equal. If a sample space has *k* outcomes, 1/*k* is the probability of each one **only** when the process makes them equally likely; the number of categories on a list tells you nothing on its own. Watch for the reflex with any short list — three drink types, four appointment outcomes, five grades — because a short list looks like a die, and a die is where the student learned the formula.

:::note amber The most common wrong answer in this topic
*"There are four outcomes, so the probability of each is 1/4."* Ask one question every time: **what makes those four equally likely?** If nothing does, the probabilities have to come from counts of equally likely individuals, or from data.
:::

*Illustration:* a sample space of three outcomes with probabilities 0.625, 0.208 and 0.167 is a perfectly good sample space — they are nonoverlapping, they cover everything, and they add to 1 — and not one of them is 1/3.

*Education example:* the university's first-year statistics module has 318 students, whose final grades were A 44, B 93, C 103, D 59 and F 19. For one script drawn at random for the moderation panel, the sample space of **grades** has five outcomes with probabilities 0.138, 0.292, 0.324, 0.186 and 0.060, which add to 1.000 — nothing like 1/5 each. What *is* equally likely is the **script**: each of the 318 has the same chance of being drawn, which is why 44 ÷ 318 = 0.138 is legitimate in the first place.

### Probability is a number from 0 to 1, inclusive (2.4.A.3)

The probability of an event is a number **between 0 and 1, inclusive**.

:::formula
0 ≤ P(E) ≤ 1
:::

The two ends are reachable. An event that cannot happen has probability **0**; an event that is certain has probability **1**, and the sample space is such an event (2.4.A.1). Everything else lies strictly between.

What it does not say. It does not say a probability of 0 means "impossible in principle" — in a finite sample space it does, and that is the only case this course meets, but the phrase to use is *cannot occur*. It does not license a percentage above 100 or a negative answer: both are arithmetic errors with a visible signature, and an answer of 1.6 or −0.2 should stop the student before they write the next line. The commonest route to a number above 1 is adding two probabilities whose events overlap — which is precisely what 2.5.A.2 and Session 10 are about.

*Illustration:* for one roll of a fair die, P(the score is 7) = **0** and P(the score is less than 7) = **1**. A student who reports P = 1.4 has not made a rounding slip; they have made a structural one.

*Education example:* the moderation panel's clerk reports that the probability a drawn script is a C is 103 ÷ 100 = **1.03**, having used the wrong denominator. The 0-to-1 bound catches it instantly: the denominator must be the 318 scripts in the sample space, giving 0.324.

### The complement of an event, and the three ways to write it (2.4.A.4)

The **complement** of an event E — written **E′**, **Ē** or **E^C** — is the event "not E": everything in the sample space that is not in E. Its probability is **1 minus P(E)**.

:::formula
P(E′) = 1 − P(E)      (also written P(Ē) or P(E^C))
:::

*E′* is "E prime", *Ē* is "E bar", *E^C* is "E complement". All three appear in exam questions; they mean the same thing. Rearranged, the rule says P(E) + P(E′) = 1, which is the form most useful as a check.

What it does not say. The complement is taken **within the sample space**: "not an A grade" means B, C, D or F, not "any grade at any university". The complement of E is not "the opposite of E" in any everyday sense — the complement of "scores more than 60" is "scores 60 or less", and the boundary value belongs to the complement, which is where a mark goes. And E and E′ between them cover the whole sample space with no overlap, which is why their probabilities add to exactly 1.

*Illustration:* 30 units, 12 of them of type A. P(A) = 12 ÷ 30 = **0.400**, so P(A′) = 1 − 0.400 = **0.600**, which is the 18 units that are not type A. Check: 0.400 + 0.600 = 1.

*Education example:* 19 of the module's 318 scripts were graded F, so P(F) = **0.060** and P(F′) = 1 − 0.060 = **0.940** — the 299 scripts that passed. Counting those 299 directly gives 299 ÷ 318 = 0.940, the same number by the longer road. The complement rule is worth having because the short road exists: with five grades, "not an F" takes one subtraction instead of four additions.

### Complements of compound events: "none", "at least one" and "more than" (2.4.A.4)

The complement rule is easy on a simple event and is where marks are lost on a worded one. Three pairs are worth knowing by heart, and all three are just "everything in the sample space that is not in E".

| Event E | Its complement E′ |
|---|---|
| at least one of them happens | **none** of them happens |
| none of them happens | **at least one** happens |
| more than 10 turn up | **10 or fewer** turn up |
| all of them happen | **at least one does not** happen |

What it does not say. "At least one" does **not** have complement "exactly one", and "more than 10" does not have complement "fewer than 10": the boundary has to land somewhere, and it lands in the complement. Nor does the complement of a statement about **several** individuals reduce to a statement about **one**: if each member of a group of four has probability 0.300 of something, 1 − 0.300 is the probability that **one named member** does not — it is not the probability that none of the four does. Getting from one member to four needs the multiplication rule, **2.6.A.2**, which is Session 10; Session 8 reached the same answer by simulation instead.

*Illustration:* a process is run four times. E = "at least one success". Then E′ = "no successes in the four runs" — not "exactly one success", and not "the first run fails".

*Education example:* the district's lottery draws 30 of the 50 applicants. For one named applicant, E = "gets a place" has P(E) = 30 ÷ 50 = **0.600**, so P(E′) = **0.400**. But a head teacher who asks *"what is the probability that at least one of my school's 14 applicants gets a place?"* is asking about a **compound** event, whose complement is *"not one of the 14 gets a place"* — and 1 − 0.600 is not its answer. Session 8 estimated questions of exactly that shape by simulation; Session 10 calculates them.

### Joint probability: the intersection of two events (2.5.A.1)

The probability that events A and B **both** will occur, sometimes called the **joint probability**, is the probability of the **intersection** of A and B, written **P(A ∩ B)**.

:::formula
P(A ∩ B) = P(A and B both occur)
:::

*A ∩ B* is read "A intersect B" or "A and B". It is itself an event — the collection of outcomes that are in A **and** in B — so everything above applies to it: its probability is a number from 0 to 1, and where outcomes are equally likely it is counted the same way as any other event.

What it does not say. The word to listen for is **and**, and it must mean *both at once for the same individual*, not *one and then the other*. P(A ∩ B) is not P(A) × P(B); multiplying is 2.6.A.2 and 2.7.A.1, Session 10, and it is only correct under conditions the student does not yet have. And P(A ∩ B) is not the same as "the proportion of the A group who are also B": that restricts to A and is a conditional probability, 2.6.A.1 — Session 8 taught the same distinction as joint against conditional **relative** frequency, and it is the single idea Session 10 most depends on.

*Illustration:* 30 units, each of type A or type B, and each marked yes or no.

| | Yes | No | Total |
|---|---|---|---|
| Type A | 4 | 8 | **12** |
| Type B | 6 | 12 | **18** |
| **Total** | **10** | **20** | **30** |

P(A ∩ yes) = 4 ÷ 30 = **0.133**: the four units that are both. P(A) = 0.400 and P(yes) = 0.333, and 0.400 × 0.333 is 0.133 only by coincidence of these numbers — do not let that pass as a method.

*Education example:* of the district's 400 Year 11 pupils, 240 attended the optional revision programme and 260 passed; **180** did both. For one pupil chosen at random, P(attended ∩ passed) = 180 ÷ 400 = **0.450**. Read it as: 45.0% of all Year 11 pupils in the district both attended and passed. It is not the same as *"75.0% of the attenders passed"*, which Session 8 computed from the same 180 as a conditional relative frequency, and which Session 10 will write as a conditional probability.

### Mutually exclusive, or disjoint, events (2.5.A.2)

Two events are **mutually exclusive**, or **disjoint**, if they **cannot occur at the same time**. This means that if two events are mutually exclusive, then **P(A ∩ B) = 0**.

:::formula
A and B mutually exclusive  ⟹  P(A ∩ B) = 0
:::

The two names are interchangeable; the course description gives both, and an exam question may use either. The definition is about the events, and the equation is its consequence — which is what makes the equation usable as evidence.

What it does not say. It does not say *unlikely*: an event pair with P(A ∩ B) = 0.001 is not mutually exclusive, merely rare. It does not say the two events cover everything between them — "scores an A" and "scores an F" cannot both happen and leave B, C and D uncovered. And it says nothing about whether one event tells you anything about the other; that is independence, 2.7.A.1, Session 10, and the two ideas are opposites rather than relatives. The subsection after next deals with that directly.

*Illustration:* in the table above, "type A" and "type B" are mutually exclusive: no unit is both, so P(A ∩ B) = **0**. "Type A" and "yes" are not: four units are both, so P(A ∩ yes) = 0.133.

*Education example:* for one of the module's 318 scripts, "graded A" and "graded B" are mutually exclusive — one script carries one grade, so no script is in both events and P(A ∩ B) = 0. "Graded A" and "submitted by a student who attended the revision workshop" are not: a script can be, and 11 of them are.

### Justifying that two events are mutually exclusive (2.5.A, Skill 4.B)

Objective 2.5.A asks the student to **justify** the claim, not to recognise it, and Skill 4.B means the justification has to run through a calculation. A complete answer has three parts.

1. **Name the two events** precisely, in context.
2. **Give the joint probability**, as a number: P(A ∩ B) = 0, or P(A ∩ B) = some positive value.
3. **Say what that shows**, in a sentence: zero means they cannot occur together, so they are mutually exclusive; anything positive means some individuals are in both, so they are not.

What it does not say. Asserting "they are mutually exclusive because they are different categories" earns nothing: *different* is not *incompatible*, and the two scenarios today both turn on that gap. Nor is a statement about the **data** automatically a statement about the **process**: a cell with a count of 0 makes the joint probability 0 for a randomly chosen individual from *this* table, which is what the question asks, but it does not prove the combination is impossible in general — say which you mean.

*Illustration:* "Type A and type B are mutually exclusive: no unit is both, so P(A ∩ B) = 0 ÷ 30 = 0, and two events whose joint probability is 0 cannot occur at the same time." That is the full three-part answer in one sentence.

*Education example:* a governor claims that, for a randomly chosen Year 11 pupil, *"attended the revision programme"* and *"passed"* are mutually exclusive, because the district's report lists them in separate columns. The justification goes the other way: P(attended ∩ passed) = 180 ÷ 400 = **0.450**, which is not 0, so the two events can and very often do occur together, and they are **not** mutually exclusive. The pair that is mutually exclusive here is *"attended"* and *"did not attend"* — P = 0, because each pupil appears in exactly one of those rows.

### What mutually exclusive does not mean (2.5.A.2)

Three confusions, each worth naming out loud. The third is the expensive one.

- **Not "different".** Two events can be about different variables and still happen together. "Lives in the Villages" and "travels by bus" are different facts about a student, and 250 students have both.
- **Not "different people".** Mutually exclusive is about **one** individual, or **one** trial. "Some students walk and others take the bus" does not make *walking* and *bus* mutually exclusive — what does is that no single student is recorded as both.
- **Not "independent".** Independence is defined in **2.7.A.1**, Session 10: knowing whether A happened does not change the probability of B. Mutually exclusive events are about as far from that as events can get — if A happens, B certainly did not, so knowing about A changes B's probability all the way to 0. Two events with positive probabilities cannot be both mutually exclusive and independent.

:::note amber Why this is worth four minutes now
Session 10 defines independence and then asks students to decide which of the two properties a pair of events has. A student who has fused the two words arrives at that lesson unable to separate them, and the error survives to the exam. Write the distinction down today, in these words: **mutually exclusive = they cannot both happen; independent = whether one happens tells you nothing about the other.**
:::

*Illustration:* in the bare table, "type A" and "yes" are not mutually exclusive, because P(A ∩ yes) = 0.133 ≠ 0. Whether they are *independent* is a different question with a different test, and it is not asked today.

*Education example:* for a Year 11 pupil in the district, *"attended the revision programme"* and *"passed"* are not mutually exclusive — 180 pupils are both. Nor are they independent, since Session 8 found that 75.0% of attenders passed against 50.0% of non-attenders, so knowing about attendance changes the chance of passing. Two separate judgements, two separate pieces of evidence, and today only the first one is asked for.

### Complementary events are mutually exclusive, and more besides (2.4.A.4, 2.5.A.2)

E and E′ are a special pair. They **cannot both happen**, so P(E ∩ E′) = 0 and they are mutually exclusive; and together they **cover the whole sample space**, so P(E) + P(E′) = 1. Mutual exclusivity on its own gives only the first of those.

What it does not say. The converse fails, and that is the point of stating it. Two mutually exclusive events need not be complements: "graded A" and "graded B" cannot both happen, but they do not cover the sample space, and P(A) + P(B) is nowhere near 1. So a student who finds P(X ∩ Y) = 0 may **not** conclude P(Y) = 1 − P(X). Only a complement licenses that subtraction.

*Illustration:* for one roll of a die, "even" and "odd" are complements: P = 0.5 each, they cannot both happen, and they add to 1. "Rolls a 2" and "rolls a 5" are mutually exclusive and add to 1/3 — not complements.

*Education example:* for a module script, "graded F" and "not graded F" are complements: 0.060 + 0.940 = 1. "Graded A" and "graded F" are mutually exclusive but not complements — their probabilities add to 0.138 + 0.060 = 0.198, and the missing 0.802 is the B, C and D scripts that neither event covers.

### Probabilities read off a two-way table (2.4.A.2, 2.5.A.1)

Choosing **one individual at random** from the *N* individuals in a two-way table makes those *N* individuals equally likely, so every probability in this session is a count over *N*. That makes the table the session's working surface, and gives each of Session 8's relative frequencies a probability to match.

| Probability for one randomly chosen individual | Where the count comes from | Session 8's name for the same number |
|---|---|---|
| P(a row level) | that row's total ÷ *N* | marginal relative frequency |
| P(a column level) | that column's total ÷ *N* | marginal relative frequency |
| P(row level ∩ column level) | the cell where they meet ÷ *N* | joint relative frequency |
| P(not a row level) | *N* minus that row total, over *N*, or 1 − P(row level) | — |

Two consequences to state once. **The cells are mutually exclusive**, because each individual sits in exactly one of them; so the count of any event built from whole cells is the sum of those cells' counts, and the nine joint probabilities of a 3 × 3 table add to 1. And **a pair of events from the two different variables is mutually exclusive only if the cell where they meet is empty** — the layout of the table says nothing about it; only the count in that cell does.

What it does not say. A cell divided by its **row** total is not a probability of the kind this session calculates: it restricts the sample space to that row, and is Session 8's conditional relative frequency, which Session 10 writes as a conditional probability. Today's denominator is the table total, every time, unless a question explicitly changes who is being chosen at random.

*Illustration:* from the bare 30-unit table, for one unit chosen at random: P(type A) = 12 ÷ 30 = **0.400**, P(yes) = 10 ÷ 30 = **0.333**, P(A ∩ yes) = 4 ÷ 30 = **0.133**, P(not type A) = 18 ÷ 30 = **0.600**. The four cells, 4, 8, 6 and 12, are mutually exclusive and add to all 30.

*Education example:* for one of the district's 400 Year 11 pupils, chosen at random: P(attended) = 240 ÷ 400 = **0.600**, P(passed) = 260 ÷ 400 = **0.650**, P(attended ∩ passed) = 180 ÷ 400 = **0.450**, P(did not attend) = 160 ÷ 400 = **0.400**. Every one of those is a count off the table over 400, because the pupil was chosen at random from all 400.


### Self-check on the theory

Answer each on paper, then open its reveal. If one goes wrong, reread that subsection's "what it does not say" paragraph before Part 3: the rest of the session leans on every one of them. Checks 4 and 5 use the made-up table of 30 units (type A 4 yes and 8 no; type B 6 yes and 12 no).

**Check 1.** A list of outcomes for one appointment reads: *attended, attended late, cancelled, missed*. Why is that not a sample space?

:::reveal Reveal — check 1
"Attended" **overlaps** with "attended late": a patient who arrived late did attend, so two entries can both be true of the same appointment. A sample space is the set of all possible **nonoverlapping** outcomes (2.4.A.1). The giveaway is that the four probabilities would add to more than 1.
:::

**Check 2.** A sample space has five outcomes. What is the probability of each?

:::reveal Reveal — check 2
**You cannot tell.** It is 0.2 each only if the five outcomes are **equally likely** (2.4.A.2), and five grades, five drink types or five hospitals are not. The number of entries on a list tells you nothing about their probabilities.
:::

**Check 3.** P(E) = 0.28. Write the complement in all three notations and give its probability.

:::reveal Reveal — check 3
P(E′) = P(Ē) = P(E^C) = 1 − 0.28 = **0.72** (2.4.A.4). All three notations mean "not E", and all three can appear in an exam question.
:::

**Check 4.** What is P(type A ∩ yes) in the 30-unit table, and what does the symbol mean in words?

:::reveal Reveal — check 4
4 ÷ 30 = **0.133**. P(A ∩ yes) is the probability that a randomly chosen unit is **both** type A **and** marked yes — the four units in the cell where the two meet. It is not P(A) × P(yes), and it is not "the proportion of type A units that are yes" (2.5.A.1).
:::

**Check 5.** How would you justify that "type A" and "type B" are mutually exclusive?

:::reveal Reveal — check 5
Name the events, give the number, say what it shows: *"Let A be 'the unit is type A' and B be 'the unit is type B'. No unit is both, so P(A ∩ B) = 0 ÷ 30 = 0, and two events with a joint probability of 0 cannot occur at the same time, so they are mutually exclusive."* (2.5.A, Skill 4.B.) "Because they are different categories" earns nothing.
:::

**Check 6.** Two events cannot both happen. Does knowing that one of them happened tell you anything about the other?

:::reveal Reveal — check 6
**Yes** — it tells you the other did **not**, so its probability drops to 0. That is why mutually exclusive is the opposite of **independent**, which is defined in 2.7.A.1 next session. Two events with positive probabilities can never be both.
:::

---

## Part 3 — Lincoln High's travel register, one student at random

Lincoln High's travel register from Session 8: a **census** of all **1,842 students**, each recorded with a home area and a main travel mode. The table is unchanged. What changes is the question — the office now picks **one student at random** from the roll, every student equally likely, and asks for probabilities.

| Home area | Bus | Car | Walk or cycle | Total |
|---|---|---|---|---|
| Town, within 3 km | 85 | 203 | 558 | **846** |
| Suburbs, 3 to 10 km | 316 | 281 | 105 | **702** |
| Villages, beyond 10 km | 250 | 38 | 6 | **294** |
| **Total** | **651** | **522** | **669** | **1,842** |

**The trap in this part: two events from different variables called mutually exclusive because they look like different groups.** "Lives in the Villages" and "travels by bus" sit on a row label and a column label, which to the eye are different parts of the table. The 250 students in the cell where that row and that column cross are the counter-argument.

### The register as a sample space of 1,842 students

:::yourturn
1. The office picks one student at random from the roll of 1,842. What is the sample space, and are its outcomes equally likely?
2. What number goes underneath every probability in this part, and why?
3. Is "travel mode" a sample space? Are "the nine cells" a sample space? Are either of those sets of outcomes equally likely?
:::

:::reveal Reveal — the sample space, and what is equally likely
1. The sample space is the **1,842 students**. One student is drawn, so the outcomes are nonoverlapping and cover everyone, and "at random" makes them **equally likely** (Part 2, *The sample space* and *Theoretical probability when every outcome is equally likely*).
2. **1,842**, the size of the sample space — every time, unless a question changes who is being chosen at random.
3. Both are sample spaces: the three travel modes are nonoverlapping and cover everyone, and so do the nine cells. But **neither is equally likely** — 651, 522 and 669 are not equal, and the nine cells run from 6 to 558. The equally likely thing is the **student**, not the category (Part 2, *When the outcomes are not equally likely*).
:::

### Bus, Villages, and the cell where they meet

:::yourturn
Name each event in words before you use a letter for it.

1. Let B be "the chosen student travels mainly by bus". Give P(B).
2. Let V be "the chosen student lives in the Villages". Give P(V).
3. Give P(V ∩ B). Which number in the table is it?
4. 0.353 × 0.160 = 0.056. Is that P(V ∩ B)? Say why or why not.
5. What is 250 ÷ 294 = 0.850, the number you used throughout Session 8?
:::

:::reveal Reveal — three probabilities and two things they are not
1. P(B) = 651 ÷ 1,842 = **0.353** — the Bus column total over the table total.
2. P(V) = 294 ÷ 1,842 = **0.160** — the Villages row total over the table total.
3. P(V ∩ B) = 250 ÷ 1,842 = **0.136**: the cell where the Villages row meets the Bus column. The word that tells you it is a joint probability is **and** (Part 2, *Joint probability*).
4. **No.** A joint probability is counted from the cell, not multiplied. 0.136 is more than twice 0.056. Multiplying is 2.6.A.2 and 2.7.A.1, Session 10, and it carries a condition that fails here.
5. It is 250 ÷ **294**, which restricts to the Villages students — Session 8's conditional relative frequency, and Session 10's conditional probability. It is not a probability of the kind this session calculates, because the denominator is not the sample space.
:::

> **The sentence to write down:** *Today's denominator is 1,842 every time, because one student is drawn at random from all 1,842. A joint probability is the cell where the two labels meet, divided by 1,842 — never a product, and never a row total.*

### The travel officer's claim about different groups

The county's transport officer, reading the register, writes:

> *"Villages students and bus users are different groups in this table, so no student can be in both. The two events are mutually exclusive: P(Villages ∩ bus) = 0."*

:::yourturn
1. Test the claim the way 2.5.A asks you to, and write the full justification in one sentence.
2. Where exactly did the officer's reasoning go wrong?
3. How big is the error? Say what 0.136 means in plain words about the school.
:::

:::reveal Reveal — not mutually exclusive, and why
1. *"Let V be 'the student lives in the Villages' and B be 'the student travels by bus'. P(V ∩ B) = 250 ÷ 1,842 = 0.136, which is not 0, so V and B can occur at the same time and are **not** mutually exclusive."* Three parts: name the events, give the joint probability, say what it shows (Part 2, *Justifying that two events are mutually exclusive*).
2. **"Different" is not "incompatible."** Home area and travel mode are two different variables recorded for the **same** student, so every student has one of each. The labels sit apart in the table; the student sits in the cell where they cross.
3. More than one student in eight of the whole school both lives in the Villages and takes the bus — 250 of them. It is the fourth largest of the nine cells, not an empty one.
:::

:::note amber The officer's error has a twin
The same officer would probably go on to say that *"lives in the Villages"* and *"travels by bus"* are **independent**, because the words sound unrelated. They are not — Session 8 found 85.0% of Villages students take the bus against 10.0% of Town students — but that is Session 10's test, with its own evidence. Today's answer stops at "not mutually exclusive, because the joint probability is 0.136".
:::

### Finding the pairs that really are mutually exclusive

:::yourturn
1. Give a pair of events from this table that really **is** mutually exclusive, and justify it.
2. What do such pairs have in common that the officer's pair does not?
3. Could two events from **different** variables ever be mutually exclusive in a table like this? Give the condition.
4. Give P(Villages ∩ walk or cycle). Are those two mutually exclusive?
:::

:::reveal Reveal — same variable, or an empty cell
1. "Lives in Town" and "lives in the Villages": each student has exactly one home area, so no student is in both and P(Town ∩ Villages) = 0 ÷ 1,842 = **0**. "Travels by bus" and "travels by car" work the same way.
2. Both events are **levels of the same variable**, and each student is recorded at exactly one level. The officer's pair takes one level from each of **two** variables, so a student can hold both.
3. **Yes — if the cell where they meet is empty.** If no Villages student walked or cycled, that cell would be 0 and the pair would be mutually exclusive in these data. The layout of the table decides nothing; only the count in the cell does.
4. 6 ÷ 1,842 = **0.003**. Not 0, so **not** mutually exclusive — only rare. Mutually exclusive does not mean unlikely.
:::

> **The rule to write down:** *Two levels of the same variable are mutually exclusive, because each individual has exactly one level. Two events from different variables are mutually exclusive only if the cell where they meet is empty — and 0.003 is not empty.*

### Complements of the register's events

:::yourturn
1. P(B) = 0.353. What is B′ in words, and what is P(B′)? Check it from the counts as well.
2. Write the same answer in the other two notations.
3. Let T be "lives in Town". Give P(T) and P(T′), and check them against each other.
4. P(Town ∩ Villages) = 0. Does that mean P(Villages) = 1 − P(Town)?
:::

:::reveal Reveal — complements, and the subtraction you may not make
1. B′ is **"the student does not travel mainly by bus"** — the car users and the walkers and cyclists. P(B′) = 1 − 0.353 = **0.647**. From the counts: 522 + 669 = 1,191, and 1,191 ÷ 1,842 = 0.647. Two roads, one answer.
2. P(B̄) = **0.647** and P(B^C) = **0.647**. All three notations mean "not B" (Part 2, *The complement of an event*).
3. P(T) = 846 ÷ 1,842 = **0.459**; P(T′) = 1 − 0.459 = **0.541**, which is the 996 Suburbs and Villages students: 996 ÷ 1,842 = 0.541. And 0.459 + 0.541 = **1**.
4. **No.** Town and Villages are mutually exclusive but **not complements**: P(Villages) = 0.160, not 0.541, because the Suburbs students are in neither event. Add your two numbers — 0.459 + 0.160 = 0.619 — and ask what happened to the other 0.381 of the school. Only a complement licenses the subtraction (Part 2, *Complementary events are mutually exclusive, and more besides*).
:::

:::note teal What you may and may not do with "or", today
The event *"travels by bus **or** lives in the Villages"* is a perfectly legitimate event, and today you may count its outcomes directly off the table: the three Bus cells (85 + 316 + 250 = 651) plus the two remaining Villages cells (38 + 6 = 44) gives **695 students**, so the probability is 695 ÷ 1,842 = **0.377**. That is 2.4.A.2 — counting the outcomes in an event — and nothing more. The general rule that reaches 0.377 from P(bus), P(Villages) and P(bus ∩ Villages) is **2.7.A.3**, the probability of the union, and it is Session 10's. Do not write it today. Notice instead why 0.353 + 0.160 = 0.513 is wrong: the 250 students in both have been counted twice, and they are exactly the ones next session's rule subtracts.
:::

### The paragraph the office may write

:::yourturn
Write one paragraph for the governors about a student chosen at random from the roll, using at least one probability, one complement and one mutually-exclusive judgement. Then write one sentence saying what the paragraph is **not** entitled to claim.
:::

:::reveal Reveal — a model paragraph, and its limits
*"If one of Lincoln High's 1,842 students is chosen at random, the probability that they travel mainly by bus is 651 ÷ 1,842 = 0.353, and the probability that they do not is 0.647. The probability that they both live in the Villages and travel by bus is 250 ÷ 1,842 = 0.136 — not 0, so those two events are not mutually exclusive. Living in Town and living in the Villages are mutually exclusive, because each student has exactly one home area."*

Not entitled to claim: anything about **cause** (Session 6), anything about students at **other schools** (Session 7 — this is a census of Lincoln High and generalises nowhere), and anything about whether home area and travel mode are **independent**, which is Session 10's question with Session 10's evidence.
:::

---

## Part 4 — Think-Aloud with the library's borrowing records, on your own

The course description's suggested activity for these topics is **Think-Pair-Share**: five probability questions, and students name only the formula needed, without calculating. Working alone, you do the naming yourself and then mark five narrations that may or may not be right — which is the part the partner would have done. Three of the activity's original five questions are Session 10 content; the three replacements here are from this session.

### The five cards, and the library table they are written on

The library service's sample of **250 members** of its Central and Westside branches, from Session 8's solo case.

| Branch | Print only | E-books only | Both | Total |
|---|---|---|---|---|
| Central | 90 | 15 | 45 | **150** |
| Westside | 60 | 10 | 30 | **100** |
| **Total** | **150** | **25** | **75** | **250** |

One member is chosen at random from the 250.

1. *"What is the probability that the chosen member does **not** borrow e-books?"*
2. *"What is the probability that the chosen member borrows **both** print and e-books?"*
3. *"Show that 'borrows print only' and 'borrows e-books only' are mutually exclusive."*
4. *"What is the probability that the chosen member is a Central branch member?"*
5. *"A librarian says: 0.900 of members borrow print and 0.300 borrow both, so the probability of borrowing print is 1.200. What is wrong?"*

### Naming the rule for each of the five cards

:::yourturn
For each of the five cards, write down **only**: which rule or definition applies, its code, and which numbers from the table would go into it. **Do not calculate the answers.** If you find yourself reaching for a calculator, that is the habit this exercise exists to break.
:::

:::reveal Reveal — the five rules
| Card | The rule | The numbers | Code |
|---|---|---|---|
| 1 | the complement rule, P(E′) = 1 − P(E) | E = borrows e-books: 25 + 75 = 100 over 250, then 1 minus it | 2.4.A.4 |
| 2 | joint probability, P(A ∩ B), counted from the overlap | the Both column, 75, over 250 | 2.5.A.1 |
| 3 | mutually exclusive: show P(A ∩ B) = 0 | no member is in both columns, so the count is 0 | 2.5.A.2 |
| 4 | equally likely outcomes: outcomes in E over outcomes in the sample space | the Central row total, 150, over 250 | 2.4.A.2 |
| 5 | the 0-to-1 bound: no probability exceeds 1 | 0.900 and 0.300 count the 75 "both" members twice | 2.4.A.3 |

The answers, which you were not asked for: 0.600, 0.300, 0, 0.600, and 1.200 is not a probability at all.
:::

### Marking five narrations that may be wrong

:::yourturn
Here are five narrations, one per card, written as if confidently. For each, say whether it is right, and if not, what is wrong with it.

1. *"Not borrowing e-books — that's the print-only members, 150 over 250, so 0.600."*
2. *"Both print and e-books — multiply: 0.900 × 0.400 = 0.360."*
3. *"Print only and e-books only are mutually exclusive because they are in different columns."*
4. *"Central members: 150 over 250, so 0.600 — but wait, is 'Central' equally likely?"*
5. *"1.200 just means it's very likely."*
:::

:::reveal Reveal — marking the five
1. **Right**, and the complement rule gets there too: 1 − 0.400 = 0.600. Both routes are legitimate. Ask yourself which would be shorter if the table had eight columns.
2. **Wrong.** P(A ∩ B) is counted from the overlap: 75 ÷ 250 = **0.300**. Multiplying is Session 10's rule and carries a condition. Note that 0.360 is close enough to 0.300 to look plausible — which is why the method has to be refused, not the number checked.
3. **Right conclusion, wrong reasoning**, which earns nothing under Skill 4.B. The justification is that no member is counted in both columns, so P = 0 ÷ 250 = 0. "Different columns" is the travel officer's error from Part 3.
4. A good question to have asked. The **member** is equally likely; **Central is not an outcome** at all — it is an event collecting 150 of the 250 equally likely outcomes. The arithmetic is right and the reason matters.
5. **Wrong.** 2.4.A.3 puts a ceiling of 1 on every probability, so 1.200 is not a probability. The error is adding two events that share the 75 members who borrow both.
:::

### Writing two cards of your own

:::yourturn
Write two new cards on this table:

- one pair of events that **is** mutually exclusive, with the justification on the back;
- one pair that **is not**, with the joint probability on the back.
:::

:::reveal Reveal — two cards that work
**Mutually exclusive:** *"Central and Westside."* Each member belongs to exactly one branch, so no member is in both and P(Central ∩ Westside) = 0 ÷ 250 = **0**.

**Not mutually exclusive:** *"Central and borrows both formats."* 45 members are both, so P(Central ∩ both) = 45 ÷ 250 = **0.180**, which is not 0.

If your "not mutually exclusive" pair came out at 0, you took two levels of the **same** variable — branch, or borrowing format. Go to the other variable for the second event.
:::

---

## Part 5 — St Mary's clinic: one appointment at random

St Mary's outpatient clinic from Sessions 6 to 8. Session 8 took one number from its records — 100 of 1,000 appointments missed — and used it to simulate overbooking. The clinic has now classified all **1,000 appointment records** since the text reminders began, and the manager wants to describe what happens at **one** appointment.

**The trap in this part: a list of four outcomes treated as four equally likely outcomes, on a list that is not a sample space to begin with.** Both halves turn up in the same breath. Part 3's sample space was 1,842 equally likely students and hid both problems; this one does not.

### A thousand appointment records, sorted into four outcomes

| What happened at the appointment | Records |
|---|---|
| Attended on time | 770 |
| Attended late | 70 |
| Cancelled in advance | 60 |
| Missed without notice | 100 |
| **Total** | **1,000** |

:::yourturn
1. Is this list a sample space for one appointment? Check both requirements.
2. Where do the four probabilities come from, and what are they?
3. Add them. What should the total be, and why?
4. Is 0.100 familiar from anywhere?
:::

:::reveal Reveal — a sample space, and where its probabilities come from
1. **Yes.** Every appointment ends in exactly one of the four, so the list is complete, and no appointment is in two of them, so the outcomes are **nonoverlapping** (Part 2, *The sample space*).
2. From the 1,000 records, as relative frequencies: **0.770, 0.070, 0.060, 0.100**. They are **estimates** of the probabilities — Session 8's 2.3.A.5–6 — and the law of large numbers (2.3.A.7) is why 1,000 records make them worth using.
3. **1.000**, because the probability of the sample space is 1 (2.4.A.1). That sum is the check you run on any proposed sample space.
4. **0.100** is Session 8's missed-appointment rate, the input to the overbooking simulation. Same records, now one outcome of four.
:::

### The receptionist's overlapping list

A receptionist writes the clinic's outcomes on the whiteboard like this:

> *"Four things can happen: the patient **attends**, the patient **attends late**, the patient **cancels**, the patient **misses**."*

:::yourturn
1. Is that a sample space? Test it.
2. Show the damage with numbers: what would the four probabilities be on the receptionist's list, and what would they add to?
3. Which rule has that broken, and what does the excess represent?
4. Fix the list in two different ways.
:::

:::reveal Reveal — where the overlap shows up in the arithmetic
1. **No.** "Attends" and "attends late" **overlap**: a patient who came late attended. The outcomes are not nonoverlapping, so the list fails 2.4.A.1.
2. "Attends" would be 770 + 70 = 840, so 840 ÷ 1,000 = 0.840; then late 0.070, cancelled 0.060, missed 0.100. Those add to **1.070**.
3. The probability of the sample space is **1**, so a total above 1 says something is counted twice. The excess **0.070** is exactly the late attenders, counted once as "attends" and once as "attends late".
4. Either **split** "attends" into *on time* and *late*, which is the clinic's four-row table; or **keep** "attends" as one outcome and drop "attends late", giving a three-outcome sample space: attended 0.840, cancelled 0.060, missed 0.100, which adds to 1.000. Both are correct sample spaces for the same situation.
:::

> **The check to write down:** *Add the probabilities of a proposed sample space. More than 1 means two outcomes overlap; less than 1 means one is missing.*

### "Four outcomes, so one chance in four"

The clinic's new administrator reads the four-row table and reports:

> *"There are four possible outcomes, so the probability that a patient misses without notice is 1 in 4, or 0.25. One appointment in four is being wasted."*

:::yourturn
1. What has the administrator done, and what is the right answer?
2. What would have to be true for 0.25 to be right?
3. What **is** equally likely in this scenario?
4. How much does the error cost the clinic, on a 10-slot session?
:::

:::reveal Reveal — the "if" clause in the formula
1. They applied the counting formula to outcomes that are **not equally likely**. The right answer comes from the records: 100 ÷ 1,000 = **0.100** (Part 2, *When the outcomes are not equally likely*).
2. The four outcomes would have to be equally likely — as many missed appointments as on-time ones, 250 of each. The records say 770 against 100.
3. The **1,000 records**: one drawn at random gives each record the same chance. Every probability here is a count of records over 1,000.
4. It inflates the waste by a factor of two and a half — 0.25 against 0.100 — which on a 10-slot session is the difference between planning for 2.5 wasted slots and 1.
:::

:::note amber Where the 1-in-k reflex comes from, and where it costs again
Everyone meets probability first on dice and coins, where counting is right because the process is **symmetric**. Nothing about a clinic, a café menu or a grade distribution is symmetric. The reflex comes back in Session 11 on random variables, where a probability distribution has to be **given**, not assumed, and in Session 12, where a student who thinks five categories means 0.2 each cannot read a normal table either. Ask it every time: **what makes these outcomes equally likely?**
:::

### Attended, and its complement

:::yourturn
1. Let A be "the patient attended", on time or late. Give P(A).
2. What is A′ in words, and what is P(A′)? Check it from the counts.
3. Are A and "missed without notice" mutually exclusive? Justify it.
4. Are they complements?
5. The manager says a cancelled appointment and a missed one are "the same thing — an empty chair". Statistically, are they the same event?
:::

:::reveal Reveal — one event collecting two outcomes
1. 770 + 70 = 840 records, so P(A) = 840 ÷ 1,000 = **0.840**. A is one event collecting two of the four outcomes.
2. A′ is **"the patient did not attend"**: cancelled in advance or missed without notice. P(A′) = 1 − 0.840 = **0.160**, and from the counts 60 + 100 = 160, so 0.160.
3. **Yes.** A record cannot be both attended and missed, so P(A ∩ missed) = 0 ÷ 1,000 = 0 — two levels of the same variable.
4. **No.** A′ also contains the 60 cancelled in advance, so P(A) + P(missed) = 0.940, not 1. Mutually exclusive, not complementary.
5. **No** — they are two mutually exclusive outcomes, P(cancelled ∩ missed) = 0. The clinic can refill a slot cancelled in advance and cannot refill one missed without notice, which is why the records keep them apart.
:::

### First appointments and follow-ups

The clinic's records also show whether each appointment was a patient's **first** at the clinic or a **follow-up**.

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

:::yourturn
One record is drawn at random.

1. Give P(first appointment) and P(missed without notice).
2. Give P(first ∩ missed). Which cell is it, and what does the number mean in words?
3. The manager claims first appointments and missed appointments are mutually exclusive, "because a patient who misses never had a first appointment". Justify or refute.
4. Find one more pair here that **is** mutually exclusive and one more that **is not**.
5. Add P(first ∩ missed) and P(follow-up ∩ missed). What do you get, and why?
6. Now try the same addition with P(first appointment) and P(missed): 0.400 + 0.100 = 0.500. How many records are actually in one or the other?
:::

:::reveal Reveal — the cells, and when adding is allowed
1. P(first) = 400 ÷ 1,000 = **0.400**; P(missed) = 100 ÷ 1,000 = **0.100**.
2. P(first ∩ missed) = 60 ÷ 1,000 = **0.060**: the cell where the First row meets the Missed column. Six per cent of all appointment records are first appointments that were missed without notice.
3. **Refute.** P(first ∩ missed) = 0.060, which is not 0, so the two events occur together in 60 of the 1,000 records and are **not** mutually exclusive.
4. Mutually exclusive: "first appointment" and "follow-up", P = 0, since each record is one or the other; or any two of the four outcomes. Not mutually exclusive: "follow-up" and "missed", P = 40 ÷ 1,000 = **0.040**; or "first" and "on time", P = **0.280**.
5. 0.060 + 0.040 = **0.100** = P(missed). The two cells are **mutually exclusive** and between them hold every missed record, so their counts add: 60 + 40 = 100.
6. **440**, which is 0.440, not 0.500. Adding worked in question 5 and fails here because "first" and "missed" **can** both happen: the 60 records in both were counted twice. The rule that handles this in general is 2.7.A.3, Session 10.
:::

:::note teal The question this table is really waiting for
*"Is a first appointment more likely to be missed than a follow-up?"* needs 60 ÷ 400 against 40 ÷ 600 — two **conditional** probabilities, 2.6.A.1, Session 10. Session 8 computed exactly these as conditional relative frequencies. Today this table answers only: how probable is each combination, and which pairs cannot occur together. The session stops here deliberately; it has not run out of rules.
:::

### The manager's paragraph about one appointment

:::yourturn
Write the manager's paragraph about one appointment chosen at random from the 1,000 records, then one sentence on what it may not claim.
:::

:::reveal Reveal — a model paragraph, and its limits
*"The four outcomes — attended on time, attended late, cancelled in advance, missed without notice — are nonoverlapping and cover every appointment, with probabilities 0.770, 0.070, 0.060 and 0.100, which add to 1. For one record drawn at random, the probability the patient attended is 0.840 and the probability they did not is 0.160. 'Attended' and 'missed without notice' are mutually exclusive, since the probability of the intersection is 0; 'first appointment' and 'missed without notice' are not, since the probability of the intersection is 0.060."*

It may not claim that the four outcomes are **equally likely**; that the probabilities are **exact** rather than estimated from 1,000 records; or anything about whether first appointments are **more likely** to be missed, which needs Session 10.
:::

---

## Part 6 — On your own: the café's loyalty members

Nothing here is new. Work through all six questions with the reveal closed, then mark yourself.

The café from Sessions 2 to 8 has **1,260 loyalty members**, and a random sample of **240** of them was classified by usual drink and by whether they usually add food.

| Usual drink | Adds food | No food | Total |
|---|---|---|---|
| Coffee | 84 | 66 | **150** |
| Tea | 22 | 28 | **50** |
| Cold drink | 14 | 26 | **40** |
| **Total** | **120** | **120** | **240** |

:::yourturn
One of the 240 sampled members is chosen at random.

1. Write the sample space for the chosen member's **usual drink**, with each probability, and check it.
2. Give P(adds food) and P(coffee ∩ adds food). Name the second one.
3. Are "coffee" and "tea" mutually exclusive? Are "coffee" and "adds food"? Justify each with a joint probability.
4. Give the probability that the member's usual drink is **not** coffee, in all three notations.
5. The café's manager says: *"There are three drinks, so the probability that a member's usual drink is tea is 1 in 3."* Evaluate.
6. The manager then says: *"P(coffee and adds food) = 0.350 and P(tea and adds food) = 0.092, so P(adds food) = 0.442."* What has been left out, and what is the correct value?
:::

:::reveal Reveal — the six answers, and what to watch for
1. {coffee, tea, cold drink} — nonoverlapping, and every member has exactly one usual drink. P(coffee) = 150 ÷ 240 = **0.625**, P(tea) = 50 ÷ 240 = **0.208**, P(cold drink) = 40 ÷ 240 = **0.167**. They add to **1.000**, as the probability of a sample space must.
2. P(adds food) = 120 ÷ 240 = **0.500**. P(coffee ∩ adds food) = 84 ÷ 240 = **0.350**, a **joint probability** — the cell where the coffee row meets the adds-food column.
3. **Coffee and tea: mutually exclusive.** Each member has exactly one usual drink, so P(coffee ∩ tea) = 0 ÷ 240 = 0. **Coffee and adds food: not mutually exclusive.** P(coffee ∩ adds food) = 0.350, which is not 0 — 84 members are in both.
4. P(coffee′) = P(coffee bar) = P(coffee^C) = 1 − 0.625 = **0.375**, which is the 90 tea and cold-drink members: 90 ÷ 240 = 0.375.
5. **Wrong.** The counting formula needs the outcomes to be **equally likely**, and three drinks on a menu are not: the records give 150, 50 and 40. P(tea) = 50 ÷ 240 = **0.208**, not 0.333. What is equally likely here is the **member**, which is why every probability is a count over 240.
6. The **cold drink** cell was left out: P(cold drink ∩ adds food) = 14 ÷ 240 = **0.058**. The three joint probabilities are mutually exclusive and between them hold every food-adding member, so they add to P(adds food): 0.350 + 0.092 + 0.058 = **0.500**, matching 84 + 22 + 14 = 120 over 240.

**Watch for:** 1 in 3 in question 5, which is this session's second trap; "coffee and adds food are mutually exclusive because they are different variables", which is Part 3's travel-officer error; a complement written as 1 − 150, or as 150 ÷ 90, in question 4; multiplying 0.625 × 0.500 = 0.313 for the joint probability in question 2, which is close enough to 0.350 to look right and is not a method you have; and in question 6, doubting 0.500 because it "should be bigger" — those three cells really do account for all 120 food-adders.
:::

---

## Part 7 — Explain it back

:::yourturn
Say all of this out loud, to a person or to a recording, without looking back at Part 2.

*Explain what a sample space is and what has to be true before you can find a probability by counting outcomes. Then explain how you would prove to an examiner that two events are mutually exclusive, and why that is not the same as saying they are unrelated.*
:::

:::reveal Reveal — what a good answer contains
Four things.

**A sample space** is the set of all possible **nonoverlapping** outcomes of a random process, and its probability is 1 — so adding the outcomes' probabilities is the check, with a total above 1 meaning two of them overlap (2.4.A.1).

**Counting** gives P(E) = outcomes in E ÷ outcomes in the sample space **only if the outcomes are equally likely**. Four clinic outcomes and three drinks are not; there the equally likely things are the records or the members, or the probabilities come from data (2.4.A.2).

**A justification of mutual exclusivity** names the two events, gives P(A ∩ B) = 0 from the counts, and says that a joint probability of 0 means the events cannot occur at the same time. "Different categories" is not a justification (2.5.A, 2.5.A.1–2).

**Mutually exclusive is not unrelated.** If A happens, B certainly did not, so knowing about A changes B's probability completely — the opposite of independence, which is defined next session (2.7.A.1).

If you said "different variables, so not mutually exclusive", go back: it is the **count in the cell** that decides, and a cell of 0 would make two events from different variables mutually exclusive. If you reached for multiplication on a joint probability, go back to the Lincoln High cell: 0.353 × 0.160 = 0.056 against the true 0.136.
:::

---
---

# Homework — Session 9

**40 marks · bring to Session 10, self-marked**

## How to do this homework

1. Do every part **with the answer key closed.** Where you are unsure, answer anyway and put a **?** beside it.
2. Then open the key and **mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote.
3. **Bring the marked sheet.** Your wrong answers and your question marks are what Session 10 opens with.

Everything here was taught in the session; this sheet is practice. Give every probability to **3 decimal places**, worked from the counts. **Name each event** before you use a letter for it. When you claim two events are mutually exclusive, show the **joint probability** and say what it means — the words alone earn nothing. Nothing on this sheet needs multiplication, the probability of a union, or a conditional probability; if you find yourself wanting one, you have misread the question.

---

## Part A — Vocabulary and notation (10 marks)

Match each term to its meaning.

| | Term | | Meaning |
|---|---|---|---|
| 1 | Sample space | A | A number between 0 and 1, inclusive |
| 2 | Outcome | B | The probability that two events both occur |
| 3 | Event | C | The set of all possible nonoverlapping outcomes of a random process |
| 4 | Equally likely outcomes | D | 1 − P(E) |
| 5 | P(E) | E | A collection of outcomes |
| 6 | The complement of E | F | Two events that cannot occur at the same time |
| 7 | P(E′) | G | The result of one trial of a random process |
| 8 | Joint probability | H | The event "not E" |
| 9 | Mutually exclusive | I | The condition that licenses dividing the outcomes in E by the outcomes in the sample space |
| 10 | The probability of any event | J | The probability that event E occurs |

## Part B — Oakfield's lunch survey as probabilities (12 marks)

Oakfield School's council asked a random sample of **200 students** from Years 7, 9 and 11 how they usually have lunch. This is the Session 8 table; the questions are new.

| Year | School lunch | Packed lunch | Off site | Total |
|---|---|---|---|---|
| Year 7 | 42 | 21 | 7 | **70** |
| Year 9 | 35 | 28 | 7 | **70** |
| Year 11 | 18 | 24 | 18 | **60** |
| **Total** | **95** | **73** | **32** | **200** |

One of the 200 students is chosen at random.

**B1.** What is the sample space for the chosen student, and what makes its outcomes equally likely? (1)

**B2.** Give P(the student is in Year 11 and has lunch off site). Name this kind of probability. (1)

**B3.** Let K be "the student brings a packed lunch". Give P(K) and P(K′), and check them against each other. (2)

**B4.** Write the sample space for the chosen student's **lunch type**, with its three probabilities, and check the total. (2)

**B5.** A council member says: *"There are three lunch types, so the probability a student eats off site is about 0.333."* Evaluate the claim and give the correct probability. (2)

**B6.** Are "is in Year 7" and "is in Year 11" mutually exclusive? Justify with a joint probability. (2)

**B7.** Are "is in Year 9" and "has school lunch" mutually exclusive? Justify with a joint probability. (2)

## Part C — The gym's prize draw (8 marks)

The gym of Session 1 now has **400 members**, each on exactly one membership: **off-peak 160**, **peak 180**, **student 60**. One member's name is drawn at random to win a year's free membership.

**C1.** Write the sample space for the winner's membership type, with its three probabilities, and check the total. (2)

**C2.** Give P(the winner is on a student membership). (1)

**C3.** Give P(the winner is not on a student membership), using the complement rule. (1)

**C4.** Find the same probability a second way, by counting members. State which rule each route used. (2)

**C5.** A staff member reports that the probability of an off-peak winner is 160 ÷ 100 = 1.6. Name the rule this breaks and give the correct probability. (2)

## Part D — The hospital network's recommendation records (6 marks)

The **300 patients** of the Session 1 hospital survey were each treated at exactly one of six hospitals and each said whether they **would recommend** it.

| Hospital | Would recommend | Patients surveyed |
|---|---|---|
| St Mary's | 63 | 84 |
| Riverside | 64 | 71 |
| Northgate | 39 | 52 |
| Parkview | 27 | 45 |
| Eastwood | 24 | 30 |
| Hillcrest | 9 | 18 |
| **Total** | **226** | **300** |

One of the 300 surveyed patients is chosen at random.

**D1.** Give P(the patient would recommend their hospital). (1)

**D2.** Give P(the patient was treated at St Mary's and would recommend it). (1)

**D3.** Justify, using a joint probability, whether "was treated at St Mary's" and "was treated at Riverside" are mutually exclusive. (2)

**D4.** Justify, using a joint probability, whether "was treated at St Mary's" and "would recommend their hospital" are mutually exclusive. (2)

## Part E — Complements, written three ways (4 marks)

The library's sample of **250 members**: print only 150, e-books only 25, both formats 75.

**E1.** Let F be "the chosen member borrows e-books". Give P(F), then write the complement in all three notations the course description uses, say what it means in words, and give its probability. (2)

**E2.** A student writes: *"Each member borrows both formats with probability 0.300. A reading group has four members chosen at random, so the probability that at least one of them borrows both formats is 1 − 0.300 = 0.700."* Explain what has gone wrong, and say what the complement of "at least one of the four borrows both" actually is. (2)

---
---

# Answer key

*For the student to mark their own work, after attempting everything.*

### Part A answers · Vocabulary and notation (10 marks, 1 each)

1–C · 2–G · 3–E · 4–I · 5–J · 6–H · 7–D · 8–B · 9–F · 10–A

### Part B answers · Oakfield's lunch survey as probabilities (12 marks)

**B1.** (1) The **200 surveyed students**. The student is chosen **at random**, which makes all 200 equally likely; that is the condition in 2.4.A.2, and it is why every probability below is a count over 200.

**B2.** (1) 18 ÷ 200 = **0.090**, a **joint probability**, P(Year 11 ∩ off site). Both the number and the name are needed.

**B3.** (2) P(K) = 73 ÷ 200 = **0.365** (1). P(K′) = 1 − 0.365 = **0.635**, which is the 127 students who do not bring a packed lunch: 127 ÷ 200 = 0.635, and 0.365 + 0.635 = 1 (1).

**B4.** (2) {school lunch, packed lunch, off site}, with P = 95 ÷ 200 = **0.475**, 73 ÷ 200 = **0.365**, 32 ÷ 200 = **0.160** (1). They add to **1.000**, as the probability of the sample space must (1).

**B5.** (2) **Wrong** (1): the three lunch types are not equally likely, and 2.4.A.2's formula applies only when the outcomes are. The correct value is 32 ÷ 200 = **0.160**, from the counts (1).

> This is the session's second trap. "Three categories, so one third each" is the reflex; the question to ask is always *what makes these equally likely?* Here, nothing does — what is equally likely is the student.

**B6.** (2) **Yes** (1). Each student is in exactly one year group, so no student is in both events: P(Year 7 ∩ Year 11) = 0 ÷ 200 = 0, and a joint probability of 0 means the events cannot occur at the same time (1).

**B7.** (2) **No** (1). P(Year 9 ∩ school lunch) = 35 ÷ 200 = **0.175**, which is not 0, so 35 of the students are in both events and they are not mutually exclusive (1).

> B6 and B7 are the session's first trap in miniature. Two **levels of the same variable** are mutually exclusive; two events from **different variables** are mutually exclusive only if the cell where they meet is empty. Saying "no, because they are different things" earns the first mark at most.

### Part C answers · The gym's prize draw (8 marks)

**C1.** (2) {off-peak, peak, student}, with P = 160 ÷ 400 = **0.400**, 180 ÷ 400 = **0.450**, 60 ÷ 400 = **0.150** (1). They add to **1.000** (1). The outcomes are nonoverlapping because each member is on exactly one membership.

**C2.** (1) 60 ÷ 400 = **0.150**.

**C3.** (1) 1 − 0.150 = **0.850**.

**C4.** (2) By counting: 160 + 180 = 340 members are not on a student membership, and 340 ÷ 400 = **0.850** (1). The first route used the **complement rule**, P(E′) = 1 − P(E), 2.4.A.4; the second used **counting equally likely outcomes**, 2.4.A.2, adding two mutually exclusive membership types (1).

> Both roads are correct and the complement is shorter — which is the whole reason 2.4.A.4 exists. With six hospitals, as in Part D, the saving is larger still.

**C5.** (2) It breaks **2.4.A.3**: a probability is a number between 0 and 1 inclusive, so 1.6 cannot be one (1). The denominator must be the 400 members of the sample space, giving 160 ÷ 400 = **0.400** (1).

### Part D answers · The hospital network's recommendation records (6 marks)

**D1.** (1) 226 ÷ 300 = **0.753**.

**D2.** (1) 63 ÷ 300 = **0.210**.

**D3.** (2) **Yes, mutually exclusive** (1). Each surveyed patient was treated at exactly one hospital, so no patient is in both events: P(St Mary's ∩ Riverside) = 0 ÷ 300 = 0, and a joint probability of 0 means the two cannot occur at the same time (1).

**D4.** (2) **No** (1). P(St Mary's ∩ would recommend) = 63 ÷ 300 = **0.210**, which is not 0, so 63 patients are in both events (1).

> D3 and D4 together are objective 2.5.A. The mark is for the joint probability, not for the verdict: an answer that says "mutually exclusive" without 0 ÷ 300, or "not mutually exclusive" without 0.210, earns one mark of the two. Note also what D4 is **not** asking — whether hospital and recommendation are independent, or whether St Mary's patients recommend more often than others. Those are Session 10 and Session 8 respectively.

### Part E answers · Complements, written three ways (4 marks)

**E1.** (2) P(F) = (25 + 75) ÷ 250 = 100 ÷ 250 = **0.400** (1). The complement is **F′**, **F̄** or **F^C**, meaning *"the chosen member does not borrow e-books"* — the 150 print-only members — with P(F′) = 1 − 0.400 = **0.600**, which matches 150 ÷ 250 (1).

**E2.** (2) The 0.300 is the probability for **one** member, so 1 − 0.300 = 0.700 is the probability that **one named member** does not borrow both formats; it says nothing about four members (1). The complement of *"at least one of the four borrows both"* is *"none of the four borrows both"* — not "exactly one", and not "the first one does not" (1).

> Getting from one member to four needs the multiplication rule, 2.6.A.2, which is Session 10. Session 8 estimated this very probability by simulation in its solo case: 3 of 10 trials had none, giving 0.3. The exact value, which Session 10 will produce, is 0.2401, so P(at least one) = 0.7599 — close to 0.700 by accident, which is exactly why the reasoning has to be refused rather than the number checked.

### Marks summary

| Part | Marks |
|---|---|
| A — Vocabulary and notation | 10 |
| B — Oakfield's lunch survey as probabilities | 12 |
| C — The gym's prize draw | 8 |
| D — The hospital network's recommendation records | 6 |
| E — Complements, written three ways | 4 |
| **Total** | **40** |

---
---

# Reference sheet — keep this

*Every term carries an example from this session. Lincoln High's register covers all 1,842 students; St Mary's clinic has 1,000 appointment records; the library's sample is 250 members and the café's 240.*

### Sample space, outcomes and events, with St Mary's (2.4.A.1)

**Random process · outcome · event** — results determined by chance · the result of one trial · a collection of outcomes (2.3.A.1–3, Session 8).
*Example: drawing one of St Mary's 1,000 appointment records · "cancelled in advance" · "the patient attended", which collects two of the four outcomes.*

**Sample space** — the set of all possible **nonoverlapping** outcomes. P(sample space) = 1.
*Example: {attended on time, attended late, cancelled in advance, missed without notice}, with 0.770 + 0.070 + 0.060 + 0.100 = 1.000.*

**Not a sample space** — a list whose entries can both happen.
*Example: {attends, attends late, cancels, misses} — "attends" contains the late attenders, and the probabilities add to 1.070.*

> **The check:** add the probabilities. More than 1 means two outcomes overlap; less than 1 means one is missing.

### Calculating P(E), and the 0-to-1 bound: the rules (2.4.A.2–3)

:::formula
P(E) = (number of outcomes in event E) ÷ (total number of outcomes in the sample space),  if all outcomes are equally likely
0 ≤ P(E) ≤ 1
:::

**Equally likely outcomes** — the condition in the formula's own sentence, without which the counting is meaningless.
*Example: the 1,842 Lincoln High students are equally likely when one is drawn at random; the three travel modes are not, and the four clinic outcomes are not.*

**When they are not equally likely** — find what is (usually one individual drawn from *N*), or take the probabilities from data (2.3.A.5–6).
*Example: P(missed) = 100 ÷ 1,000 = 0.100 from the records, not 1 ÷ 4 = 0.25 from the four rows.*

**The 0-to-1 bound** — an answer above 1 or below 0 is a structural error, usually a wrong denominator or two overlapping events added.
*Example: 160 ÷ 100 = 1.6 for the gym's off-peak winner; the denominator is the 400 members, giving 0.400.*

### Complements: notation and the rule (2.4.A.4)

:::formula
P(E′) = 1 − P(E)      written also as P(Ē) or P(E^C)
:::

**The complement of E** — everything in the sample space that is not in E, taken within that sample space.
*Example: B = travels by bus, P(B) = 0.353; B′ = does not travel mainly by bus, P(B′) = 0.647, which is the 1,191 car users, walkers and cyclists.*

**Compound complements** — "at least one" ↔ "none"; "more than 10" ↔ "10 or fewer"; "all" ↔ "at least one does not". The boundary value belongs to the complement.
*Example: the complement of "at least one of the four reading-group members borrows both formats" is "none of the four does" — and 1 − 0.300 is not its probability, because 0.300 is for one member.*

> **Why the rule earns its keep:** with six hospitals, P(not Hillcrest) is one subtraction, 1 − 0.060 = 0.940, instead of five additions.

### Joint probability and mutually exclusive events: the reference version (2.5.A)

**Joint probability, P(A ∩ B)** — the probability that A and B **both** occur, for the same individual or trial. Counted from the cell where they meet; never a product.
*Example: P(Villages ∩ bus) = 250 ÷ 1,842 = 0.136 — while 0.353 × 0.160 = 0.056, which is not the answer to anything here.*

**Mutually exclusive (disjoint)** — the events cannot occur at the same time, so P(A ∩ B) = 0.
*Example: "lives in Town" and "lives in the Villages" — each student has one home area, so P = 0.*

**Not mutually exclusive** — any positive joint probability, however small.
*Example: P(Villages ∩ walk or cycle) = 6 ÷ 1,842 = 0.003. Rare is not impossible.*

**A justification (Skill 4.B)** — name both events in context, give P(A ∩ B) as a number, say what that number means.
*Example: "P(St Mary's ∩ would recommend) = 63 ÷ 300 = 0.210, which is not 0, so the two events occur together for 63 patients and are not mutually exclusive."*

> **Mutually exclusive is not independent.** Mutually exclusive = they cannot both happen. Independent = whether one happens tells you nothing about the other (2.7.A.1, Session 10). If A and B are mutually exclusive and A happens, B's probability drops to 0 — the opposite of telling you nothing.

> **Mutually exclusive is not complementary.** E and E′ are mutually exclusive **and** cover the sample space, so P(E) + P(E′) = 1. "Attended" and "missed without notice" are mutually exclusive and add to 0.940, because the cancellations are in neither.

### Reading Lincoln High's table as probabilities (2.4.A.2, 2.5.A.1)

For one individual chosen at random from the *N* in a two-way table, every probability is a count over *N*.

| Probability | Count | Lincoln High example |
|---|---|---|
| P(a row level) | row total ÷ *N* | P(Villages) = 294 ÷ 1,842 = 0.160 |
| P(a column level) | column total ÷ *N* | P(bus) = 651 ÷ 1,842 = 0.353 |
| P(row ∩ column) | the cell where they meet ÷ *N* | P(Villages ∩ bus) = 250 ÷ 1,842 = 0.136 |
| P(not a row level) | 1 − P(row level) | P(not Town) = 1 − 0.459 = 0.541 |

**Cells are mutually exclusive** — each individual is in exactly one, so an event built from whole cells has the sum of their counts, and all nine cells add to *N*.
*Example: the Bus column's 85 + 316 + 250 = 651; the two missed cells at St Mary's, 60 + 40 = 100.*

**Different variables, empty cell** — two events from different variables are mutually exclusive only when the cell where they meet holds 0. The table's layout decides nothing.
*Example: the travel officer called "Villages" and "bus" mutually exclusive because the labels sit apart; the cell holds 250.*

> **A cell over its row total is not today's probability.** 250 ÷ 294 = 0.850 restricts to the Villages students. That is Session 8's conditional relative frequency and Session 10's conditional probability; today's denominator is the table total.

:::note red Not in the course description
The **addition rule** is a prep-book name (Barron's pdf 272, 275, 276; 5 Steps pdf 165; Princeton Review Chapter 6); the course description's phrase is *the probability of the union*, P(A ∪ B), topic **2.7.A.2–3**, Session 10. **Venn diagrams** (5 Steps pdf 64; Princeton Review Chapter 6) and **tree diagrams** (Barron's pdf 272, 276; 5 Steps pdf 164, 176) are never named by the course description and no exam question requires either; the required representation for two categorical variables is the **two-way table** (2.1.A.1). **Exhaustive**, **complementary events** as a noun phrase and **odds** do not appear either — the course description says *the complement of an event E*. **Law of averages** and **gambler's fallacy**, from Session 8, remain prep-book names for a misreading of the law of large numbers.
:::

---

*CED references: Topic 2.4 (2.4.A.1–4), Topic 2.5 (2.5.A.1–2); Topic 2.3 (2.3.A.1–3, 2.3.A.5–7) for random process, outcome, event and the law of large numbers, taught in Session 8; Topics 2.6–2.7 for conditional probability, the general multiplication rule, independence and the probability of the union, all Session 10; the Sample Instructional Activity for topics 2.4–2.7 (Think-Pair-Share), converted to Think-Aloud and restricted to 2.4–2.5. Course and Exam Description effective Fall 2026.*

*Supporting reading: Barron's pdf 272–280 · Princeton Review Chapter 6, Anticipating Patterns, 205–265 · 5 Steps to a 5 pdf 160–166.*

