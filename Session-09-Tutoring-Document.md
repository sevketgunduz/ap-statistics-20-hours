# Session 9 — Probability, Complements and Mutually Exclusive Events

**AP Statistics · Twenty-Hour Course · One-to-one tutoring edition**
**CED Topics 2.4, 2.5 · Skills 3.C, 4.B · about 143 minutes, plus the 35-minute Session 7 test**

---

## Where this session sits

Session 8 estimated a probability by running a random process many times and taking a relative frequency. Today the course gives the first rules that calculate a probability instead of estimating one, and there are only two: count the outcomes in the event when every outcome is equally likely, and subtract from 1 to get the complement. Alongside them sits one definition with a test attached — the **joint probability** P(A ∩ B), and the claim that two events are **mutually exclusive**, which is true exactly when that joint probability is 0.

This is a short session by content. Topics 2.4 and 2.5 carry two learning objectives and six essential-knowledge statements between them, against the eleven that Session 8 had. Nothing is cut and nothing is pushed into the homework; the clock below is simply shorter, and the time is spent on the three places where marks are actually lost: a sample space whose outcomes overlap, a counting formula used when the outcomes are not equally likely, and the word *mutually exclusive* treated as though it meant *unrelated*. The last of those matters most, because Session 10 drops independence on top of it and a student who has fused the two ideas cannot be untangled afterwards.

Both scenarios carry forward. Lincoln High's travel register — the same 1,842 students and the same two-way table as Session 8 — is now read as probabilities for **one student chosen at random**, which is the bridge Session 10 needs for conditional probability. St Mary's clinic, whose missed-appointment rate drove Session 8's overbooking simulation, supplies the sample space of a single appointment, where the outcomes are definitely not equally likely.

### Learning objectives for topics 2.4 and 2.5

Verbatim from the course description.

| Code | Objective | Skill |
|---|---|---|
| 2.4.A | Calculate probabilities for events and their complements. | 3.C |
| 2.5.A | Justify why two events are mutually exclusive (or disjoint) using joint probability. | 4.B |

Skills: **3.C** Calculate and estimate expected counts, percentages, probabilities, and intervals · **4.B** Justify a claim based on statistical calculations and results.

Two objectives, so the session is built around six essential-knowledge statements: 2.4.A.1 to 2.4.A.4 and 2.5.A.1 to 2.5.A.2. Every one of them is stated in the theory section and then applied twice.

### What the course description does and does not ask for

Read this before teaching. The plan's line for this session, and all three prep books, reach further than the 2026 framework does here.

- **The addition rule is not in this session.** P(A ∪ B) = P(A) + P(B) − P(A ∩ B) is **2.7.A.3**, which is Session 10. The plan's line for Session 9 says "the addition rule that follows from them"; follow the course description instead. Today's scenarios may *count* the students in an event like "bus or Villages" straight off the table, because counting outcomes is 2.4.A.2 — but the rule that reaches the same answer from P(bus), P(Villages) and P(bus and Villages) is next session's, and is not stated today.
- **Note also that the course description never uses the phrase "addition rule."** Its words are *the probability of the union* (2.7.A.2). The red box below lists where the prep books use the other name.
- **Conditional probability, the general multiplication rule and independence are all Session 10** (topics 2.6 and 2.7). They may be named as forward pointers — and *mutually exclusive is not independent* is taught today as a limit on 2.5.A.2 — but nothing today calculates with them.
- **The law of large numbers is 2.3.A.7 and was taught in Session 8.** It is recalled by name in the diagnostic and in Scenario B, where 0.100 arrives as a relative frequency from 1,000 records; it is not re-taught.
- **2.4.A.2's counting formula carries a condition in its own sentence**: *"If all outcomes in the sample space are equally likely, then …"*. That clause is where most of the marks on this topic are won and lost, and the theory gives it a subsection of its own.
- **2.4.A.1 says "nonoverlapping"**, and that word is doing work. A list of possibilities is not a sample space unless no two entries can happen together. Scenario B's trap is built on it.
- **The course description gives three notations for the complement** (2.4.A.4): **E′**, **Ē** and **E^C**. All three may appear in an exam question, so all three are used today.
- **2.5.A is a justification objective, Skill 4.B.** The mark is not for the words "mutually exclusive"; it is for showing P(A ∩ B) = 0 and saying why that cell, or that pair of levels, is empty.

:::note red Off-syllabus terms, not taught as examinable
The course description never uses **"addition rule"** — its phrase is *the probability of the union*, topic 2.7. All three prep books use the other name: Barron's pdf 272, 275, 276; 5 Steps pdf 165; Princeton Review Chapter 6, which heads the formula *"Union (addition rule)"*. It never names a **Venn diagram** (5 Steps pdf 64; Princeton Review Chapter 6 draws two, for a complement and for disjoint events) or a **tree diagram** (Barron's pdf 272, 276; 5 Steps pdf 164, 176); both are drawing aids, and no exam question requires either, so today's pictures are two-way tables, which the course description does name (2.1.A.1). It does not use **exhaustive**, **complementary events** as a noun phrase, or **odds**; its wording is *the complement of an event E*. **Law of averages** and **gambler's fallacy** were registered in Session 8 and are still prep-book names for a misreading of the law of large numbers.
:::

### Timing and who talks

**The Session 7 test comes first.** Following the pattern of the earlier sessions — Session 1's test opened Session 3, and so on to Session 6's, which opened Session 8 — give Session 7's multiple-choice test at the start of this session, before the homework debrief: 20 questions, 35 minutes, as the test page states. The pattern has not been confirmed as a rule; if your own plan differs, follow it. The clock below starts when the test is finished.

| Minutes | Segment | Who talks |
|---|---|---|
| 0–12 | Homework debrief and diagnostic | Student |
| 12–47 | **Theory**: random process, outcome and event recalled; the sample space and nonoverlapping outcomes; equally likely outcomes and P(E); outcomes that are not equally likely; the 0-to-1 bound; the complement and its three notations; complements of compound events; joint probability and the intersection; mutually exclusive events; justifying mutual exclusivity; what mutually exclusive does not mean; complements as a special case; probabilities off a two-way table; six check questions (2.4–2.5) | Both |
| 47–79 | **Scenario A**: Lincoln High's travel register read as probabilities for one randomly chosen student, the trap of calling two events from different variables mutually exclusive, and complements of the register's events | Both |
| 79–95 | **Activity**: Think-Aloud, five cards on the library's borrowing records | Student |
| 95–123 | **Scenario B**: St Mary's clinic — the sample space of one appointment, an overlapping list, outcomes that are not equally likely, and a joint probability that is not zero | Both |
| 123–135 | Solo case: the café's loyalty members | Student |
| 135–143 | Teach it back, set homework | Student |
| **Total** | **143 minutes of teaching, after the 35-minute Session 7 test** | |

The course description allots four class periods to topics 2.4 and 2.5 (two each). Everything they require is taught in the session, first stated in the theory section and then applied twice; the homework practises it. The session is shorter than Sessions 6 to 8 because the content is smaller, not because anything has been moved out.

---

## 0–12 min · Homework debrief and diagnostic

### The Session 8 homework: two lists and two errors

The student arrives with the Session 8 homework self-marked. Ask for the two lists: *"Which did you get wrong, and which did you put a question mark on?"* Spend the time on those only.

**The two errors to check for specifically:**

- **B3 gave the same number twice.** "Of the Year 7 students, what proportion have school lunch?" is 42 ÷ 70 = 0.600; "of the school-lunch students, what proportion are Year 7?" is 42 ÷ 95 = 0.442. Same 42 students, two totals. Three minutes here, because today every probability is a count over a total and the student has to choose the total before dividing. The habit to install: *name the group you are counting out of, out loud, before you write the fraction.* Today that group is almost always the whole sample space, which is easier — and that is exactly why the error hides until Session 10 brings it back as conditional probability.
- **D5 blamed the wrong denominator.** The student who counted 11 winning digits out of 40 and wrote 0.275 was counting **sleeves** when the question asked about **customers**. The 0.2 was already the model's input; dividing digits by digits can only return it. Today the same discipline appears as: what are the equally likely things? At Lincoln High they are the 1,842 students; at St Mary's they are the 1,000 appointment records — and they are *not* the four outcomes in the clinic's sample space.

E1 is worth thirty seconds if it was marked with a **?**: *"we've been lucky three times, so the next session is bound to overflow"* is wrong because the sessions are independent, and the law of large numbers says nothing about the next one. Today recalls the law of large numbers by name in Scenario B and does not re-teach it.

Then the diagnostic.

### Four diagnostic questions on shares, chance and the word "not"

Four quick questions, answers out loud.

**Q1.** *"From Session 8's Lincoln High table: of the 294 Villages students, 250 travel by bus. What proportion is that? And of the 651 bus users, what proportion live in the Villages?"*

**Q2.** *"St Mary's records show 100 of 1,000 appointments were missed. What does 100 ÷ 1,000 give you, and what is it an estimate of?"*

**Q3.** *"A café sells coffee, tea and cold drinks. One loyalty member is picked at random. Is the probability that their usual drink is tea equal to one third?"*

**Q4.** *"The probability that a Lincoln High student travels by bus is 0.353. What is the probability that a student does not travel by bus?"*

| What you hear | What it means | Where to start |
|---|---|---|
| Q1: "0.850, and 0.384" | Session 8's conditioning held | Move on at pace; today's denominators are easier, and Session 10 brings these two back as conditional probabilities |
| Q1: the same number twice, or hesitation | The Session 8 homework's B3 error is live | Slow down on the theory's *Probabilities read off a two-way table*, and make them say the group out loud before every fraction today |
| Q2: "0.100, an estimate of the probability that a patient misses" | 2.3.A.5–6 held | Scenario B uses exactly that number; recall the law of large numbers there in one sentence |
| Q2: "the probability is 0.100" with no "estimate" | Treats a relative frequency as the probability itself | Recall Session 8's *Probability as long-run relative frequency, estimated from data (2.3.A.5–6)* before the theory |
| Q3: "no — only if the three are equally popular" | Already has 2.4.A.2's condition | Take the theory's *When the outcomes are not equally likely* briskly; they will still need it for Scenario B |
| Q3: "yes, three drinks, so one third" | The equally-likely reflex, and today's second trap | Teach *Theoretical probability when every outcome is equally likely* and the subsection after it slowly. This is the solo case's question 5 and Scenario B's trap |
| Q4: "0.647, because they add to 1" | The complement is already intuitive | Spend the time on complements of **compound** events instead; that is where it breaks |
| Q4: "0.5" or "I'd need the other numbers" | No complement rule yet | *The complement of an event, and the three ways to write it* is the session's core; do it with the table in front of you |

---

## 12–47 min · Theory — probability, complements and mutually exclusive events

Every concept the session uses is stated here, before any data. Put each subsection on the shared screen, read the rule with the student, and have them say what it does **not** say; that is where the marks go. Each subsection carries two examples doing different jobs: the *Illustration* is deliberately bare, so the structure is visible with nothing to distract from it, and the *Education example* is a study of the kind this course is about, so the rule is seen doing something. Read bare first and concrete second. The bare ones here are a fair six-sided die and one made-up table of 30 units. Lincoln High, the library cards, St Mary's and the café come afterwards and apply these rules; when a question there needs a definition, point back to the subsection here rather than restating it. The section ends with six check questions.

**What this section builds on, by name.** From Session 8: *Random process, outcome and event (2.3.A.1–3)*, *Probability as long-run relative frequency, estimated from data (2.3.A.5–6)*, *The law of large numbers (2.3.A.7)*, and the three relative frequencies of a two-way table (2.2.A.1–3). From Session 1: rf = f ÷ n. They are recalled where they are needed and not re-taught.

**The education examples form one strand**, continued from Sessions 6 to 8: the **district** — its summer-school lottery of 50 applicants for 30 places, and its 400 Year 11 pupils cross-tabulated by revision attendance and result — and the **university's first-year statistics module** of 318 students, whose scripts go to a marking moderation panel. Thirteen subsections. Keep each to about two and a half minutes and make the student speak in each one.

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

### Six check questions before the scenarios

Ask all six. If any goes wrong, reread that subsection's "what it does not say" paragraph before Scenario A.

**C1.** *"A list of outcomes for one appointment reads: attended, attended late, cancelled, missed. Why is that not a sample space?"*
→ *"Attended" overlaps with "attended late": a patient who arrived late attended. Outcomes in a sample space must be nonoverlapping (2.4.A.1).*

**C2.** *"A sample space has five outcomes. What is the probability of each?"*
→ *Unknown. It is 1/5 each only if the five are equally likely, which five grades or five drink types are not (2.4.A.2).*

**C3.** *"P(E) = 0.28. Write the complement three ways and give its probability."*
→ *P(E′) = P(Ē) = P(E^C) = 1 − 0.28 = 0.72 (2.4.A.4).*

**C4.** *"What does P(A ∩ B) mean in words, and what does it not mean?"*
→ *The probability that A and B both occur, for the same individual or trial. Not P(A) × P(B), and not "the proportion of the A group who are B" (2.5.A.1).*

**C5.** *"How do you justify that two events are mutually exclusive?"*
→ *Name the two events, show P(A ∩ B) = 0 from the counts, and say that a joint probability of 0 means they cannot occur at the same time (2.5.A, Skill 4.B).*

**C6.** *"Two events cannot both happen. Does knowing one happened tell you anything about the other?"*
→ *Yes — it tells you the other did not, so the probability drops to 0. That is why mutually exclusive is the opposite of independent, which is 2.7.A.1 and Session 10.*

---

## 47–79 min · Scenario A — Lincoln High's travel register: one student chosen at random

Lincoln High's travel register from Session 8: a **census** of all **1,842 students**, each recorded with a home area and a main travel mode. The table is unchanged. What changes is the question. Last session asked about shares of groups; today the office picks **one student at random** from the roll — every student equally likely — and asks for probabilities.

**The trap this scenario carries: two events from different variables called mutually exclusive because they look like different groups.** "Lives in the Villages" and "travels by bus" occupy a row label and a column label, which to the eye are different parts of the table, and students conclude the two cannot both happen. The 250 students in the cell where that row and that column meet are the counter-argument, and they are the same 250 that Session 8's conditioning trap was built on. A pair of events is mutually exclusive when the cell where they meet is **empty** — never because of where their labels sit.

### The register as a sample space of 1,842 students

| Home area | Bus | Car | Walk or cycle | Total |
|---|---|---|---|---|
| Town, within 3 km | 85 | 203 | 558 | 846 |
| Suburbs, 3 to 10 km | 316 | 281 | 105 | 702 |
| Villages, beyond 10 km | 250 | 38 | 6 | 294 |
| **Total** | **651** | **522** | **669** | **1,842** |

:::script
ask | Ask | "The office picks one student at random from the roll of 1,842. What is the sample space, and are its outcomes equally likely?"
listen | Listen for | The sample space is the 1,842 students; one student is drawn, so the outcomes are nonoverlapping, and "at random" makes them equally likely.
intro | Recall | *The sample space, and why its outcomes must not overlap (2.4.A.1)* and *Theoretical probability when every outcome is equally likely (2.4.A.2)*.
ask | Ask | "So what goes underneath every probability today?"
listen | Listen for | 1,842, the size of the sample space — unless the question changes who is being chosen.
ifsay | If "it depends on the question" | "Last session, yes. Today the student is drawn from the whole roll every time. Which total is that?"
ask | Ask | "Is 'travel mode' a sample space? What about 'the nine cells'?"
listen | Listen for | Both are. The three modes are nonoverlapping and cover everyone, and so do the nine cells — but the three modes are not equally likely, while the 1,842 students are.
intro | Recall | *When the outcomes are not equally likely (2.4.A.2)*: the student is the equally likely thing, not the category.
:::

### Probabilities for bus, Villages, and the cell where they meet

:::script
ask | Ask | "Write P(B) where B is 'the student travels by bus'. Name the event first."
listen | Listen for | B = the chosen student travels mainly by bus. P(B) = 651 ÷ 1,842 = 0.353.
intro | Recall | *Probabilities read off a two-way table (2.4.A.2, 2.5.A.1)*: a column total over the table total.
ask | Ask | "Now V = 'the student lives in the Villages'."
listen | Listen for | P(V) = 294 ÷ 1,842 = 0.160.
ask | Ask | "What is P(V ∩ B), and which number in the table is it?"
listen | Listen for | P(V ∩ B) = 250 ÷ 1,842 = 0.136: the cell where the Villages row meets the Bus column.
intro | Recall | *Joint probability: the intersection of two events (2.5.A.1)*: the word to hear is **and**.
ask | Ask | "0.353 × 0.160 is 0.056. Is that P(V ∩ B)?"
listen | Listen for | No. Multiplying is not the rule; the joint probability is counted from the cell, and 0.136 is more than twice 0.056.
ifsay | If "but that's how you do 'and'" | "Where did you meet that rule? It is 2.6.A.2 and 2.7.A.1, Session 10, and it carries a condition that fails here. Today we count the cell."
ask | Ask | "And what is 0.850, the number we used all through Session 8?"
listen | Listen for | 250 ÷ 294, which restricts to the Villages students. Not a probability of this session's kind; it is Session 10's conditional probability.
:::

> **The sentence to write down:** *Today's denominator is 1,842 every time, because one student is drawn at random from all 1,842. A joint probability is the cell where the two labels meet, divided by 1,842 — never a product, and never a row total.*

### The travel officer's "different groups, so they cannot both happen"

This is the trap. The county's transport officer, reading the register, writes:

> *"Villages students and bus users are different groups in this table, so no student can be in both. The two events are mutually exclusive: P(Villages ∩ bus) = 0."*

:::script
ask | Ask | "Is the officer right? Test the claim the way 2.5.A asks you to."
listen | Listen for | No. P(V ∩ B) = 250 ÷ 1,842 = 0.136, which is not 0, so the events are not mutually exclusive: 250 students are in both.
intro | Recall | *Justifying that two events are mutually exclusive (2.5.A, Skill 4.B)*: name the events, give the joint probability, say what it shows.
ask | Ask | "Where did the officer's reasoning go wrong, exactly?"
listen | Listen for | "Different groups" is not "incompatible". Home area and travel mode are two different variables recorded for the same student, so a student has one of each; the labels sit apart in the table, but the student sits in the cell where they cross.
ifsay | If "but they are in different rows and columns" | "Put your finger on the Villages row. Now slide along to the Bus column. What is in the cell?" 250. "Who are those 250?"
ask | Ask | "Write the full justification the exam wants, in one sentence."
listen | Listen for | *"Let V be 'the student lives in the Villages' and B be 'the student travels by bus'. P(V ∩ B) = 250 ÷ 1,842 = 0.136, which is not 0, so V and B can occur at the same time and are not mutually exclusive."*
ask | Ask | "Is the officer's claim even close? How big is 0.136?"
listen | Listen for | More than one student in eight of the whole school is both. It is the fourth largest of the nine cells.
:::

:::note amber The officer's error has a twin
The same officer would probably say that *"lives in the Villages"* and *"travels by bus"* are **independent**, because the words sound unrelated. They are not — Session 8 showed 85.0% of Villages students take the bus against 10.0% of Town students — and that is Session 10's test, not today's. Today's answer stops at "not mutually exclusive, because the joint probability is 0.136".
:::

### Which pairs at Lincoln High really are mutually exclusive

:::script
ask | Ask | "Give me a pair of events from this table that really is mutually exclusive, and justify it."
listen | Listen for | "Lives in Town" and "lives in the Villages": each student has exactly one home area, so no student is in both and P(Town ∩ Villages) = 0. Or "travels by bus" and "travels by car", for the same reason.
intro | Recall | *What mutually exclusive does not mean (2.5.A.2)*: not different, not different people — one individual, two events that cannot both hold.
ask | Ask | "What do those pairs have in common, and what does the officer's pair not have?"
listen | Listen for | Both events are **levels of the same variable**, and each student is recorded at exactly one level. The officer's pair takes one level from each of two different variables, so a student can hold both.
ask | Ask | "Could two events from different variables ever be mutually exclusive in a table like this?"
listen | Listen for | Yes — if the cell where they meet is empty. If no Villages student walked or cycled, that cell would be 0 and the pair would be mutually exclusive in these data.
ask | Ask | "The Villages walk-or-cycle cell holds 6 students. So what is P(Villages ∩ walk or cycle)?"
listen | Listen for | 6 ÷ 1,842 = 0.003. Small, but not 0 — so not mutually exclusive, only rare.
intro | Recall | *Mutually exclusive, or disjoint, events (2.5.A.2)*: it does not mean unlikely.
:::

> **The rule to write down:** *Two levels of the same variable are mutually exclusive, because each individual has exactly one level. Two events from different variables are mutually exclusive only if the cell where they meet is empty — and 0.003 is not empty.*

### Complements of the register's events

:::script
ask | Ask | "P(B) = 0.353. What is P(B′), and what does B′ mean in words?"
listen | Listen for | P(B′) = 1 − 0.353 = 0.647. B′ is "the student does not travel mainly by bus": the car users and the walkers and cyclists.
intro | Recall | *The complement of an event, and the three ways to write it (2.4.A.4)*.
ask | Ask | "Check it from the counts instead."
listen | Listen for | 522 + 669 = 1,191 students are not bus users, and 1,191 ÷ 1,842 = 0.647. Two roads, one answer.
ask | Ask | "Write the same thing with the other two notations."
listen | Listen for | P(B̄) = 0.647 and P(B^C) = 0.647. All three mean "not B".
ask | Ask | "Now T = 'lives in Town'. Give P(T) and P(T′) and check them."
listen | Listen for | P(T) = 846 ÷ 1,842 = 0.459; P(T′) = 1 − 0.459 = 0.541, which is the 996 Suburbs and Villages students: 996 ÷ 1,842 = 0.541. And 0.459 + 0.541 = 1.
ask | Ask | "P(Town ∩ Villages) = 0. Does that mean P(Villages) = 1 − P(Town)?"
listen | Listen for | No. They are mutually exclusive but not complements: P(Villages) = 0.160, not 0.541, because the Suburbs students are in neither event.
intro | Recall | *Complementary events are mutually exclusive, and more besides (2.4.A.4, 2.5.A.2)*: only a complement licenses the subtraction.
ifsay | If they subtract anyway | "Add your two numbers. 0.459 + 0.160 = 0.619. What happened to the other 0.381 of the school?"
:::

:::note teal What you may and may not do with "or", today
The event *"travels by bus **or** lives in the Villages"* is a perfectly legitimate event, and today you may count its outcomes directly off the table: the three Bus cells (85 + 316 + 250 = 651) plus the two remaining Villages cells (38 + 6 = 44) gives **695 students**, so the probability is 695 ÷ 1,842 = **0.377**. That is 2.4.A.2 — counting the outcomes in an event — and nothing more. The general rule that reaches 0.377 from P(bus), P(Villages) and P(bus ∩ Villages) is **2.7.A.3**, the probability of the union, and it is Session 10's. Do not write it today; notice instead why 0.353 + 0.160 = 0.513 is wrong, and that the 250 students counted twice are exactly the ones the next session's rule subtracts.
:::

### The sentence the office may write

:::script
ask | Ask | "The office wants one paragraph about a randomly chosen student, for the governors. Write it."
listen | Listen for | Something like: *"If one of Lincoln High's 1,842 students is chosen at random, the probability that they travel mainly by bus is 651 ÷ 1,842 = 0.353, and the probability that they do not is 0.647. The probability that they both live in the Villages and travel by bus is 250 ÷ 1,842 = 0.136 — not 0, so those two are not mutually exclusive. Living in Town and living in the Villages are mutually exclusive, because each student has exactly one home area."*
ask | Ask | "What is this paragraph not entitled to say?"
listen | Listen for | Anything about cause, anything about students at other schools, and anything about whether home area and travel mode are independent. The first two are Sessions 6 and 7; the third is Session 10.
:::

---

## 79–95 min · Activity — Think-Aloud with the library's borrowing records

The course description's Sample Instructional Activity for topics 2.4 to 2.7 is **Think-Pair-Share**: five probability questions, one each for the complement rule, a mutually exclusive event, a conditional probability, the general multiplication rule and an independent event; students name only the formula needed, without calculating, then compare with a partner.

**Two changes, both deliberate.** With one student there is no partner, so this becomes **Think-Aloud**, the master plan's conversion: the student names the rule and narrates the reasoning while the tutor stays silent, and the tutor's turn comes in round 2. And three of the activity's five questions — conditional probability, the general multiplication rule, an independent event — are topics 2.6 and 2.7, which is Session 10. Those three cards are replaced by three drawn from today's content: counting equally likely outcomes, the 0-to-1 bound, and reading a sample space. The activity's shape, *name the rule, do not calculate*, is kept exactly, because it is the part that works.

### The five cards, and the library table they are written on

The library service's sample of **250 members** of its Central and Westside branches, from Session 8's solo case, recording how each member borrows.

| Branch | Print only | E-books only | Both | Total |
|---|---|---|---|---|
| Central | 90 | 15 | 45 | **150** |
| Westside | 60 | 10 | 30 | **100** |
| **Total** | **150** | **25** | **75** | **250** |

One member is chosen at random from the 250. The five cards:

1. *"What is the probability that the chosen member does **not** borrow e-books?"*
2. *"What is the probability that the chosen member borrows **both** print and e-books?"*
3. *"Show that 'borrows print only' and 'borrows e-books only' are mutually exclusive."*
4. *"What is the probability that the chosen member is a Central branch member?"*
5. *"A librarian says: 0.900 of members borrow print and 0.300 borrow both, so the probability of borrowing print is 1.200. What is wrong?"*

### Round 1: the student names the rule and narrates

The student takes each card in turn and says, out loud and without calculating: which rule or definition applies, what its code is, and which numbers from the table would go into it. Stay silent. Note which cards they reach for a calculator on.

| Card | The rule to name | The numbers they would use | Code |
|---|---|---|---|
| 1 | the complement rule, P(E′) = 1 − P(E) | E = borrows e-books: 25 + 75 = 100 over 250, then 1 minus it | 2.4.A.4 |
| 2 | joint probability, P(A ∩ B), counted from the overlap | the Both column, 75, over 250 | 2.5.A.1 |
| 3 | mutually exclusive: show P(A ∩ B) = 0 | no member is in both columns, so the count is 0 | 2.5.A.2 |
| 4 | equally likely outcomes: outcomes in E over outcomes in the sample space | the Central row total, 150, over 250 | 2.4.A.2 |
| 5 | the 0-to-1 bound: no probability exceeds 1 | 0.900 and 0.300 count the 75 "both" members twice | 2.4.A.3 |

**If they calculate anyway**, let them finish the number and then ask for the rule's name and code; the point of the activity is the recognition, and a student who can only get there through the arithmetic has not got there. The answers, for your reference only: 0.600, 0.300, 0, 0.600, and 1.200 is impossible.

### Round 2: the student marks the tutor's wrong narration

Now reverse the roles the Think-Pair-Share intends for the partner. Read these five narrations aloud, one per card, as if confident. The student says, for each, whether it is right and what is wrong with it.

1. *"Not borrowing e-books — that's the print-only members, 150 over 250, so 0.600."* → **Right**, and the complement rule gets there too: 1 − 0.400 = 0.600. Both roads are legitimate; ask which is shorter if the table had eight columns.
2. *"Both print and e-books — multiply: 0.900 × 0.400 = 0.360."* → **Wrong.** P(A ∩ B) is counted from the overlap, 75 ÷ 250 = 0.300. Multiplying is Session 10's rule and carries a condition. Note that 0.360 is close enough to 0.300 to look plausible, which is why the method has to be refused rather than the number checked.
3. *"Print only and e-books only are mutually exclusive because they are in different columns."* → **Wrong reasoning, right conclusion**, which earns nothing under Skill 4.B. The justification is that no member is counted in both columns, so P = 0 ÷ 250 = 0. Different columns is the travel officer's error from Scenario A.
4. *"Central members: 150 over 250, so 0.600 — but wait, is 'Central' equally likely?"* → The member is equally likely; **Central is not** one of the equally likely outcomes, it is an event collecting 150 of them. Make the student say that distinction in their own words.
5. *"1.200 just means it's very likely."* → **Wrong.** 2.4.A.3 puts a ceiling of 1 on every probability, so 1.200 is not a probability at all. The error is adding two events that share 75 members.

### Round 3: the student writes two cards of their own

The Think-Pair-Share's trade step, with the tutor as the partner. The student writes two new cards on this table and hands them over:

- one pair of events that **is** mutually exclusive, with the justification on the back;
- one pair that **is not**, with the joint probability on the back.

Good answers: *"Central and Westside"* — each member belongs to one branch, so P = 0. *"Central and borrows both formats"* — 45 members are both, so P = 45 ÷ 250 = **0.180**, not 0. Answer their cards out loud yourself, and let them mark you. If their "not mutually exclusive" pair comes out at 0, they have taken two levels of the same variable; send them to the other variable.

---

## 95–123 min · Scenario B — St Mary's clinic: the sample space of one appointment

St Mary's outpatient clinic from Sessions 6 to 8. Session 8 took one number from its records — 100 of 1,000 appointments missed — and used it to simulate overbooking. The clinic has now classified all **1,000 appointment records** since the text reminders began, and the manager wants to describe what happens at **one** appointment.

**The trap this scenario carries: a list of four outcomes treated as four equally likely outcomes, on a list that is not a sample space to begin with.** Both halves show up in the same breath, and they are the two failure modes of 2.4.A.1 and 2.4.A.2: an "or" in a category label that makes two entries overlap, and the reflex that *k* categories means 1/*k* each. Scenario A's sample space was 1,842 equally likely students and hid both problems; this one does not.

### A thousand appointment records, sorted into four outcomes

| What happened at the appointment | Records |
|---|---|
| Attended on time | 770 |
| Attended late | 70 |
| Cancelled in advance | 60 |
| Missed without notice | 100 |
| **Total** | **1,000** |

:::script
ask | Ask | "Is this list a sample space for one appointment? Check both requirements."
listen | Listen for | Yes. Every appointment ends in one of the four, and no appointment is in two of them — nonoverlapping and complete.
intro | Recall | *The sample space, and why its outcomes must not overlap (2.4.A.1)*.
ask | Ask | "Where do the probabilities come from, and what are they?"
listen | Listen for | From the 1,000 records: 0.770, 0.070, 0.060 and 0.100. They are estimates of the probabilities, from relative frequencies.
intro | Recall | Session 8's *Probability as long-run relative frequency, estimated from data (2.3.A.5–6)* — and the law of large numbers (2.3.A.7) is why 1,000 records make these worth using. Neither is re-taught today.
ask | Ask | "Add them. What should they come to, and why?"
listen | Listen for | 0.770 + 0.070 + 0.060 + 0.100 = 1.000, because the probability of the sample space is 1.
intro | Recall | *The sample space, and why its outcomes must not overlap (2.4.A.1)*: that sum is the check.
ask | Ask | "Is 0.100 familiar?"
listen | Listen for | It is Session 8's missed-appointment rate, the input to the overbooking simulation. Same records, now one outcome of four.
:::

### The receptionist's overlapping list

A receptionist writes the clinic's outcomes up on the whiteboard like this:

> *"Four things can happen: the patient **attends**, the patient **attends late**, the patient **cancels**, the patient **misses**."*

:::script
ask | Ask | "Is that a sample space? Test it."
listen | Listen for | No. "Attends" and "attends late" overlap: a patient who came late attended. The outcomes are not nonoverlapping, so it fails 2.4.A.1.
intro | Recall | *The sample space, and why its outcomes must not overlap (2.4.A.1)*: *all possible* **nonoverlapping** *outcomes*.
ask | Ask | "Show the damage with numbers. What would the four probabilities be on the receptionist's list?"
listen | Listen for | "Attends" would be 840 ÷ 1,000 = 0.840, then late 0.070, cancelled 0.060, missed 0.100 — which add to 1.070. More than 1, so something is wrong.
ask | Ask | "Which rule has that broken, and what does the excess 0.070 represent?"
listen | Listen for | The probability of the sample space is 1; the excess 0.070 is the late attenders, counted twice.
ask | Ask | "Fix the list two ways."
listen | Listen for | Either split "attends" into *on time* and *late*, which is the clinic's table; or keep "attends" as one outcome and drop "attends late", giving a three-outcome sample space: attended 0.840, cancelled 0.060, missed 0.100, which adds to 1.000.
intro | Recall | *The sample space, and why its outcomes must not overlap (2.4.A.1)*: there is more than one correct sample space, and both of these are.
:::

> **The check to write down:** *Add the probabilities of a proposed sample space. More than 1 means two outcomes overlap; less than 1 means one is missing.*

### "Four outcomes, so one chance in four"

The clinic's new administrator reads the four-row table and reports to the manager:

> *"There are four possible outcomes, so the probability that a patient misses without notice is 1 in 4, or 0.25. One appointment in four is being wasted."*

:::script
ask | Ask | "What has the administrator done, and what is the right answer?"
listen | Listen for | Applied the equally likely formula to outcomes that are not equally likely. The right answer is 100 ÷ 1,000 = 0.100, from the records.
intro | Recall | *When the outcomes are not equally likely (2.4.A.2)*: the formula's "if" clause.
ask | Ask | "What would have to be true for 0.25 to be right?"
listen | Listen for | The four outcomes would have to be equally likely — as many missed appointments as on-time ones. Nothing about a clinic makes that true, and the records say otherwise.
ifsay | If "but there are four outcomes" | "How many of the 1,000 records are in each row? Does 770 look like 250 to you?"
ask | Ask | "What **is** equally likely in this scenario, then?"
listen | Listen for | The 1,000 records: one drawn at random gives each record the same chance. So every probability here is a count of records over 1,000.
intro | Recall | *When the outcomes are not equally likely (2.4.A.2)*: find the level at which outcomes are equally likely, or take the probabilities from data.
ask | Ask | "How much would the administrator's error cost the clinic?"
listen | Listen for | It inflates the waste by a factor of two and a half — 0.25 against 0.100 — which on a 10-slot session is the difference between planning for 2.5 wasted slots and 1.
:::

:::note amber Where the 1-in-k reflex comes from, and where it costs again
Every student meets probability on dice and coins, where the counting formula is right because the process is symmetric. Nothing about a clinic, a café menu or a grade distribution is symmetric. The reflex comes back in Session 11 on random variables — where a probability distribution has to be given, not assumed — and in Session 12, where a student who thinks five categories means 0.2 each cannot read a normal table either. Ask the question every time: **what makes these outcomes equally likely?**
:::

### Attended, and its complement

:::script
ask | Ask | "Let A be 'the patient attended', on time or late. What is P(A)?"
listen | Listen for | 770 + 70 = 840 records, so P(A) = 840 ÷ 1,000 = 0.840.
intro | Recall | *Theoretical probability when every outcome is equally likely (2.4.A.2)*, applied to the 1,000 equally likely records; A collects two of the four outcomes.
ask | Ask | "What is A′ in words, and what is P(A′)?"
listen | Listen for | A′ is "the patient did not attend": cancelled in advance or missed without notice. P(A′) = 1 − 0.840 = 0.160, and from the counts 60 + 100 = 160, so 0.160.
intro | Recall | *The complement of an event, and the three ways to write it (2.4.A.4)*.
ask | Ask | "Are A and 'missed without notice' mutually exclusive? Justify it."
listen | Listen for | Yes: a record cannot be both attended and missed, so P(A ∩ missed) = 0. They are different levels of the same variable.
intro | Recall | *Justifying that two events are mutually exclusive (2.5.A, Skill 4.B)*.
ask | Ask | "Are they complements?"
listen | Listen for | No. A′ also contains the 60 cancelled in advance, so P(A) + P(missed) = 0.940, not 1.
intro | Recall | *Complementary events are mutually exclusive, and more besides (2.4.A.4, 2.5.A.2)*.
ask | Ask | "The manager says a cancelled appointment and a missed one are 'the same thing — an empty chair'. Statistically, are they the same event?"
listen | Listen for | No: they are two mutually exclusive outcomes, P(cancelled ∩ missed) = 0. The clinic can refill a slot cancelled in advance and cannot refill one missed without notice, which is why the records keep them apart.
:::

### First appointments and follow-ups: a joint probability that is not zero

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

:::script
ask | Ask | "One record is drawn at random. Give me P(first appointment) and P(missed without notice)."
listen | Listen for | 400 ÷ 1,000 = 0.400 and 100 ÷ 1,000 = 0.100.
intro | Recall | *Probabilities read off a two-way table (2.4.A.2, 2.5.A.1)*: row and column totals over the table total.
ask | Ask | "Now P(first ∩ missed). Which cell, and what does the number mean?"
listen | Listen for | 60 ÷ 1,000 = 0.060. Six per cent of all appointment records are first appointments that were missed without notice.
ask | Ask | "The manager claims first appointments and missed appointments are mutually exclusive, 'because a patient who misses never had a first appointment'. Justify or refute."
listen | Listen for | Refute: P(first ∩ missed) = 0.060, which is not 0, so the two events occur together in 60 of the 1,000 records and are not mutually exclusive.
intro | Recall | *Justifying that two events are mutually exclusive (2.5.A, Skill 4.B)*: name, calculate, conclude.
ask | Ask | "Find me a pair here that is mutually exclusive, and one more that is not."
listen | Listen for | Mutually exclusive: "first appointment" and "follow-up", P = 0, since each record is one or the other; or any two of the four outcomes. Not: "follow-up" and "missed", P = 40 ÷ 1,000 = 0.040; or "first" and "on time", P = 0.280.
ask | Ask | "Add P(first ∩ missed) and P(follow-up ∩ missed). What do you get, and why?"
listen | Listen for | 0.060 + 0.040 = 0.100 = P(missed). The two cells are mutually exclusive and between them hold every missed record, so their counts add: 60 + 40 = 100.
intro | Recall | *Probabilities read off a two-way table (2.4.A.2, 2.5.A.1)*: an event built from whole cells has the sum of those cells' counts.
ifsay | If "so you can always add probabilities" | "Only when the events cannot both happen. Try it with 'first appointment' and 'missed': 0.400 + 0.100 = 0.500. How many records are in one or the other? 440, which is 0.440. Who did you count twice?" The 60.
:::

:::note teal The question this table is really waiting for
*"Is a first appointment more likely to be missed than a follow-up?"* needs 60 ÷ 400 against 40 ÷ 600 — two **conditional** probabilities, 2.6.A.1, Session 10. Session 8 computed exactly these as conditional relative frequencies. Today the table answers only: how probable is each combination, and which pairs cannot occur together. Say so to the student, so they know the session stopped deliberately rather than ran out of rules.
:::

### What St Mary's may write about a single appointment

:::script
ask | Ask | "Write the manager's paragraph about one appointment chosen at random from the 1,000 records."
listen | Listen for | Something like: *"The four outcomes — attended on time, attended late, cancelled in advance, missed without notice — are nonoverlapping and cover every appointment, with probabilities 0.770, 0.070, 0.060 and 0.100, which add to 1. For one record drawn at random, the probability the patient attended is 0.840 and the probability they did not is 0.160. 'Attended' and 'missed without notice' are mutually exclusive, since P of the intersection is 0; 'first appointment' and 'missed without notice' are not, since P of the intersection is 0.060."*
ask | Ask | "What may the paragraph not claim?"
listen | Listen for | That the four outcomes are equally likely; that the probabilities are exact rather than estimated from 1,000 records; and anything about whether first appointments are more likely to be missed, which needs Session 10.
:::

---

## 123–135 min · Solo case — the café's loyalty members

Unaided. The café from Sessions 2 to 8 has **1,260 loyalty members**, and a random sample of **240** of them was classified by usual drink and by whether they usually add food. Watch, say nothing, note where they hesitate.

| Usual drink | Adds food | No food | Total |
|---|---|---|---|
| Coffee | 84 | 66 | **150** |
| Tea | 22 | 28 | **50** |
| Cold drink | 14 | 26 | **40** |
| **Total** | **120** | **120** | **240** |

One of the 240 sampled members is chosen at random.

1. Write the sample space for the chosen member's **usual drink**, with each probability, and check it.
2. Give P(adds food) and P(coffee ∩ adds food). Name the second one.
3. Are "coffee" and "tea" mutually exclusive? Are "coffee" and "adds food"? Justify each with a joint probability.
4. Give the probability that the member's usual drink is **not** coffee, in all three notations.
5. The café's manager says: *"There are three drinks, so the probability that a member's usual drink is tea is 1 in 3."* Evaluate.
6. The manager then says: *"P(coffee and adds food) = 0.350 and P(tea and adds food) = 0.092, so P(adds food) = 0.442."* What has been left out, and what is the correct value?

**Answers.**

1. The sample space is {coffee, tea, cold drink}: nonoverlapping, and every member has exactly one usual drink. P(coffee) = 150 ÷ 240 = **0.625**, P(tea) = 50 ÷ 240 = **0.208**, P(cold drink) = 40 ÷ 240 = **0.167**. They add to **1.000**, as the probability of the sample space must.
2. P(adds food) = 120 ÷ 240 = **0.500**. P(coffee ∩ adds food) = 84 ÷ 240 = **0.350**, a **joint probability** — the cell where the coffee row meets the adds-food column.
3. **Coffee and tea: mutually exclusive.** Each member has exactly one usual drink, so no member is in both and P(coffee ∩ tea) = 0 ÷ 240 = 0. **Coffee and adds food: not mutually exclusive.** P(coffee ∩ adds food) = 0.350, which is not 0, so 84 members are in both.
4. P(coffee′) = P(coffee bar) = P(coffee^C) = 1 − 0.625 = **0.375**, which is the 90 tea and cold-drink members: 90 ÷ 240 = 0.375.
5. **Wrong.** The counting formula needs the outcomes to be **equally likely**, and three drinks on a menu are not: the records give 150, 50 and 40. P(tea) = 50 ÷ 240 = **0.208**, not 0.333. What is equally likely here is the **member**, which is why every probability is a count over 240.
6. The **cold drink** cell has been left out: P(cold drink ∩ adds food) = 14 ÷ 240 = **0.058**. The three joint probabilities are mutually exclusive and between them hold every food-adding member, so they add to P(adds food): 0.350 + 0.092 + 0.058 = **0.500**, matching 84 + 22 + 14 = 120 over 240.

**Watch for:** 1 in 3 in question 5, which is today's second trap and the solo case's main purpose; "coffee and adds food are mutually exclusive because they are different variables", which is Scenario A's travel-officer error; a complement written as 1 − 150 or as 150 ÷ 90 in question 4; multiplying 0.625 × 0.500 = 0.313 for the joint probability in question 2, which is close enough to 0.350 to look right and is not a method they have; and in question 6, adding the three joint probabilities and then worrying that 0.500 "should be bigger" — the three cells really do account for all 120 food-adders.

---

## 135–143 min · Teach it back

> *"Explain to me what a sample space is and what has to be true before you can find a probability by counting outcomes. Then explain how you would prove to an examiner that two events are mutually exclusive, and why that is not the same as saying they are unrelated."*

A good answer contains four things. A **sample space** is the set of all possible **nonoverlapping** outcomes of a random process, and its probability is 1 — so adding the outcomes' probabilities is the check, with a total above 1 meaning two of them overlap (2.4.A.1). **Counting** gives P(E) = outcomes in E ÷ outcomes in the sample space **only if the outcomes are equally likely**; four clinic outcomes and three drinks are not, and there the equally likely things are the records or the members, or the probabilities come from data (2.4.A.2). A **justification of mutual exclusivity** names the two events, gives P(A ∩ B) = 0 from the counts, and says that a joint probability of 0 means the events cannot occur at the same time; "different categories" is not a justification (2.5.A, 2.5.A.1–2). And **mutually exclusive is not unrelated**: if A happens, B certainly did not, so knowing about A changes B's probability completely — which is the opposite of independence, defined next session (2.7.A.1).

If they say "different variables, so not mutually exclusive", stop and ask for the general rule: it is the **count in the cell** that decides, and a cell of 0 would make two events from different variables mutually exclusive. If they reach for multiplication on a joint probability, go back to the Lincoln High cell: 0.353 × 0.160 = 0.056 against the true 0.136. Then set the homework.

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
