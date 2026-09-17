# Session 1 — What Is a Statistical Study?

**AP Statistics · Twenty-Hour Course · One-to-one tutoring edition**
**CED Topics 1.1, 1.2, 1.3 · Skills 1.A, 2.A, 3.A, 4.A · 60 minutes**

*Revision 2 — every term now carries a worked example, and frequency calculations are given as formulas and applied.*

---

## What changes when it is one student

This is not the classroom document with the group sizes edited out. Four things genuinely change, and they change the structure of the hour.

**You can diagnose before you teach.** In a class you must cover 1.1 through 1.3 because thirty students need all of it. With one student you can find out in six minutes what they already have, and spend the hour on what they do not.

**Definitions stop being a block to deliver.** One-to-one, a definition dump is the fastest way to lose a student. Terms are introduced **as they arise inside a scenario**, and the reference sheet at the back is something you hand over — not something you read aloud.

**You are the only other voice in the room.** Every peer-discussion structure has to be replaced, and two moves cover almost all of it: *you argue the opposing position*, or *you produce deliberately flawed work and the student marks it*.

**The failure mode is you talking.** Target: **the student talks at least half the hour.** If you have explained for four minutes without the student saying anything, stop and ask them something.

### Timing

| Minutes | Segment | Who talks |
|---|---|---|
| 0–6 | Diagnostic — find out what they already have | Student |
| 6–8 | Frame: the statistical investigation cycle | Tutor |
| 8–22 | **Scenario A** — terms introduced as they arise | Both |
| 22–30 | Challenge Sort — you argue the other side | Student |
| 30–46 | **Scenario B** — the digits trap, then the formulas and tables | Both |
| 46–54 | Solo case — student works unaided while you watch | Student |
| 54–60 | Teach-it-back, set homework | Student |

---

## 0–6 min · The diagnostic

Do not teach yet. Ask these four, in order, and write down what you hear.

**Q1.** *"A school wants to know the average height of its students. It measures 50 of them. What would you call the 50, and what would you call all the students?"*

**Q2.** *"If I told you the average height of those 50 was 168 cm — is that the answer to the school's question?"*

**Q3.** *"Give me two things you could measure about a person where one is a number and one is not."*

**Q4.** *"Is a phone number a number?"*

### How to branch

| What you hear | What it means | Where to start |
|---|---|---|
| Q1 confident, Q2 says "not exactly, it's an estimate" | Population/sample and the inference idea are already there | Start at Scenario A but move fast to parameter vs statistic; bank the time for the formulas in Scenario B |
| Q1 confident, Q2 says "yes" | Vocabulary present, concept absent. **The most common profile** | Spend the extra time on the parameter/statistic table in Scenario A. Do not rush it |
| Q1 hesitant or reversed | Foundation missing | Teach Scenario A slowly and in full. Reaching only the start of Scenario B is fine — push the tables to Session 2 |
| Q4 says "yes, it's digits" | The digits trap is live | Note it, but **do not correct it yet**. Let Scenario B do the work |

> **If all four come back clean,** do not spend the hour confirming what they know. Go straight to Scenario A's investigative-question trap and Scenario B's formulas, and use the recovered time on the Part D homework dataset in the session, with you marking live.

---

## 6–8 min · Frame the hour

Two minutes, and one of the few stretches where you hold the floor.

Everything in this course is one of four moves: **pose a question, collect data, analyse data, interpret the result.** Those are the College Board's four Statistical Practices, and every topic between now and the exam is a tool used at one of the four stages.

Then say what this hour is for: *"Today is entirely the first two. Almost no calculation. If you can't say precisely what your population is, everything in Unit 3 falls apart, and that's the biggest part of the exam."*

---

## 8–22 min · Scenario A — the commute study

> Lincoln High School has **1,842 students**. The principal wants to reorganise the morning bus timetable but does not know how students currently get to school. She asks a randomly chosen **120 students** to record, on one Tuesday: how they primarily travelled to school, how many minutes the journey took, and how many separate vehicles they had to change between.
>
> Of the 120 surveyed, **43 came by bus**, and their journeys averaged **24.6 minutes**.

Hand this over on paper. Thirty seconds to read. Then work it through by asking, not telling.

### The sequence of questions

**Ask:** *"Who is this study actually about?"*
Listen for: all 1,842 students. If they say "the 120", ask *"would the principal be happy knowing about only those 120?"*
**Introduce:** population, **N = 1,842**. Then sample, **n = 120**.

**Ask:** *"If I gave you the spreadsheet, what would one row be?"*
The best question in the session for surfacing confusion. Anyone answering "a journey" or "a bus" has not got it.
**Introduce:** observational unit — one student.

**Ask:** *"Three things were measured. Sort them into numbers and not-numbers."*
Then push: *"Journey time and number of vehicle changes are both numbers. Is there any difference between them?"*
If it does not come: *"Could someone change 1.4 vehicles? Could a journey take 24.61 minutes?"*
**Introduce:** categorical, quantitative, discrete, continuous.

| Variable | Type | The test |
|---|---|---|
| Mode of travel | Categorical | Values are group labels |
| Journey time | Quantitative, continuous | Measured; 24.61 minutes is possible |
| Vehicle changes | Quantitative, discrete | Counted; never 1.4 |

### The centre of the session — parameter vs statistic

Do not define these first. Build the table with the student, one row at a time.

**Ask:** *"What proportion of all 1,842 students come by bus?"*
The correct answer is **"we don't know."** Wait for it. If they offer 0.358, ask *"how many of the 1,842 did we actually ask?"*

**Ask:** *"What proportion of the 120 came by bus?"* → 43/120 = **0.358**. Known.

| Quantity | Which | Known? |
|---|---|---|
| Proportion of **all 1,842** who come by bus | Parameter | No |
| 43/120 = 0.358, proportion of the **sampled** | Statistic | Yes |
| Mean journey time of **all 1,842** | Parameter | No |
| 24.6 minutes, mean of the **120** | Statistic | Yes |

**Then say the thing that makes the course make sense:** *"Every single thing we do from Session 13 onwards is about the gap between those two columns. That's it. That's the subject."*

**Memory hook, offered only after they have built the table:** **P**opulation goes with **P**arameter. **S**ample goes with **S**tatistic.

### The investigative-question trap

**Ask:** *"What question is this study trying to answer?"*

Then spring it:

> *"The principal looks at her results and notices cyclists have much longer journeys than she expected. She's curious, so she rewrites her report to answer: why do cyclists take so long? Is that allowed?"*

Most students say yes. Let them commit before you push.

**Then ask:** *"How many of the 120 were cyclists — what if it was four? And she only asked the question because she spotted the pattern. Could she have found a pattern in any of the variables if she'd gone looking?"*

**The principle (CED 1.1.B.1):** an investigative question should not be changed based on the data analysis or results. It is a legitimate question for a **new** study with **new** data.

---

## 22–30 min · Challenge Sort

This replaces the classroom card-sort in groups of four. **You argue the opposite of whatever the student says**, including when they are right.

**Setup.** Six short study descriptions. The student identifies population, sample, observational unit, one variable and its type — out loud, one card at a time. After every answer, push back once: *"Are you sure? I'd have said the population was…"* Take the wrong position with a straight face.

The point is to separate **secure reasoning** from **correct guessing**. A student who knows why will hold their ground. A student who guessed will fold immediately.

> **Say this before you start:** *"I'm going to disagree with you sometimes even when you're right. Your job is to hold your position if you can justify it."* Without the warning it becomes demoralising.

### The two cards that carry the learning

**Card 5.** *A researcher tests every lightbulb coming off one production line during one shift, to judge the quality of the factory's output.*
Census of that shift, or sample of ongoing production? **It depends on the investigative question** — the population is not a property of the data, it is a property of what you are asking.

**Card 6.** *A teacher records the marks of all 28 students in her class to decide whether to re-teach a topic to that class.*
There is no sampling at all. The population is the 28 and she measured all of them, so her mean is a **parameter**. The more valuable card: "the mean" is a parameter or a statistic depending entirely on whether you measured everybody.

---

## 30–46 min · Scenario B — the hospital survey

> A regional hospital network discharged **12,400 patients** last year across six hospitals. To review its care, the network surveys **300** of those patients, recording for each: which hospital treated them, their room number, the number of nights they stayed, and the time in minutes from arrival to being seen by a doctor.
>
> Results by hospital: **St Mary's 84, Riverside 71, Northgate 52, Parkview 45, Eastwood 30, Hillcrest 18.**

Run population, sample and observational unit fast — the student should do these unprompted now. **N = 12,400, n = 300**, one discharged patient. If they still need prompting, slow down: Scenario A has not landed.

### The digits trap

**Ask:** *"Classify all four variables."*

Wait for room number. Most students call it quantitative. Do not correct it — ask:

> *"What's the average room number in this hospital?"*

Let them compute something, or realise they cannot. Then: *"If the answer is 247.6, is there a room 247.6? What would that number tell a manager?"*

**The test, which the student should state back to you:** does it have **units of measure**, and does **arithmetic on it mean anything**?

| Variable | Type | Why |
|---|---|---|
| Hospital | Categorical | Six group labels |
| Room number | **Categorical** | Digits, but a label. No units. The mean means nothing |
| Nights stayed | Quantitative, discrete | A count, with units. 5 nights is two more than 3 |
| Minutes until seen | Quantitative, continuous | Measured; 47.3 is possible |

If the diagnostic Q4 caught them out, close the loop: *"Same thing as the phone number, isn't it?"*

---

### The frequency formulas

Write these out with the student before building anything. Every one is a division; the difficulty is knowing which number goes underneath.

Let **n** be the sample size and **f** the frequency (count) in one category.

| Quantity | Symbol | Formula | In words |
|---|---|---|---|
| Frequency | *f* | the count itself | How many are in this category |
| Relative frequency | *rf* | **rf = f ÷ n** | What fraction of the whole are in this category |
| Percentage | *100rf* | **100rf = (f ÷ n) × 100** | The same thing, out of 100 |
| Cumulative frequency | *cf* | **cf = running total of f** | How many are in this category **or below** |
| Cumulative relative frequency | *crf* | **crf = cf ÷ n** | What fraction are in this category or below |
| Cumulative percentage | *100crf* | **100crf = (cf ÷ n) × 100** | The same thing, out of 100 |

> **A note on notation.** Some textbooks write these last two as *100cf*. That is shorthand for "the cumulative figure expressed as a percentage" — it does **not** mean 100 × cf. The denominator is always *n*.

**The four self-checks.** Get the student to state these, because they catch nearly every arithmetic slip:

- Σ*f* = *n* — the frequencies add to the sample size
- Σ*rf* = 1 — the relative frequencies add to one
- Σ*100rf* = 100% — the percentages add to one hundred
- the **last** *cf* = *n*, and the **last** *crf* = 1

---

### Applying the formulas · part 1, the categorical table

Have the student build this. Do not build it yourself — this is Skill 3.A and they need the pen.

| Hospital | *f* | *rf* = f ÷ 300 | *100rf* |
|---|---|---|---|
| St Mary's | 84 | 84 ÷ 300 = 0.280 | 28.0% |
| Riverside | 71 | 71 ÷ 300 = 0.237 | 23.7% |
| Northgate | 52 | 52 ÷ 300 = 0.173 | 17.3% |
| Parkview | 45 | 45 ÷ 300 = 0.150 | 15.0% |
| Eastwood | 30 | 30 ÷ 300 = 0.100 | 10.0% |
| Hillcrest | 18 | 18 ÷ 300 = 0.060 | 6.0% |
| **Total** | **300** | **1.000** | **100%** |

Checks: Σ*f* = 300 = *n* ✓ · Σ*rf* = 1.000 ✓ · Σ*100rf* = 100% ✓

**Ask:** *"Could we add a cumulative frequency column to this table?"*

The answer is **no**, and the reason is the point. Cumulative means "this category **or below**", which requires the categories to have an **order**. Hospital names have none. "Riverside or fewer" is not a sentence. Cumulative columns belong to variables you can line up — which is why the next table works and this one does not.

---

### Applying the formulas · part 2, the ordered table

The same 300 patients, now by **number of nights stayed**. This variable *is* ordered, so all six quantities apply.

| Nights | *f* | *rf* | *100rf* | *cf* | *crf* = cf ÷ 300 | *100crf* |
|---|---|---|---|---|---|---|
| 1 | 96 | 0.320 | 32.0% | 96 | 0.320 | 32.0% |
| 2 | 84 | 0.280 | 28.0% | 180 | 0.600 | 60.0% |
| 3 | 60 | 0.200 | 20.0% | 240 | 0.800 | 80.0% |
| 4 | 36 | 0.120 | 12.0% | 276 | 0.920 | 92.0% |
| 5 or more | 24 | 0.080 | 8.0% | 300 | 1.000 | 100% |
| **Total** | **300** | **1.000** | **100%** | | | |

**Show the running total explicitly**, one row at a time:
96 → 96 + 84 = 180 → 180 + 60 = 240 → 240 + 36 = 276 → 276 + 24 = 300 ✓

Checks: last *cf* = 300 = *n* ✓ · last *crf* = 1.000 ✓

**Then ask the question cumulative frequency exists to answer:**

> *"What percentage of these patients stayed three nights or fewer?"*

Read it straight off the *100crf* column: **80.0%**. Without that column the student has to add 96 + 84 + 60 and then divide — which is exactly the work the column has already done.

Follow up with: *"And what percentage stayed more than three nights?"* → 100% − 80.0% = **20.0%**. The complement is the other reason the column is worth having.

> **Flag this for the student, honestly.** Cumulative frequency does not appear anywhere in the current CED's descriptive statistics. It is worth knowing because Barron's uses it heavily and it makes the "or fewer" questions trivial — but it will not be examined as a technique. See the note at the end of this document.

---

### The claim — and the habit that earns marks all year

> *"An administrator says: most of our discharged patients came from St Mary's. Is she right?"*

Wait. Many students say yes, because 28.0% is the biggest number in the column.

**Ask:** *"What does 'most' mean?"* → more than half. 28.0% is not.

Then get them to rewrite it: *"St Mary's accounted for more discharged patients than any other single hospital in the sample, at 28.0%, though it still treated fewer than three in ten."*

**The template for the whole course:** state the claim · quote the number · say what it does and does not establish · keep it in context.

---

## 46–54 min · Solo case

The student works this **unaided** while you watch and say nothing. Resist helping. Where they hesitate tells you what to open Session 2 with.

> A gym has **2,300 members**. It surveys **180** of them, recording: membership type (basic/premium/student), locker number, number of visits last month, and minutes spent per visit.
>
> Of the 180 surveyed, **54 had premium membership**.

1. Population and **N**? Sample and **n**?
2. Observational unit?
3. Classify all four variables.
4. Calculate the relative frequency and percentage for premium membership. Show the formula.
5. Is that figure a parameter or a statistic? How do you know?
6. Name one parameter here whose value you do not know.

**Answers.** 2,300 gym members / 180 surveyed / one member / membership type categorical, **locker number categorical**, visits quantitative-discrete, minutes quantitative-continuous / rf = 54 ÷ 180 = 0.300, so 100rf = 30.0% / statistic, because it came from the 180 sampled not all 2,300 / e.g. the true proportion of all 2,300 members with premium membership.

**Watch for:** locker number classified as quantitative. If that happens *after* Scenario B, the digits test has not transferred — reteach it at the start of Session 2 rather than patching it now.

---

## 54–60 min · Teach it back

Close with the student talking, not you.

> *"Explain to me, as if I've never taken this course, the difference between a parameter and a statistic. Use the gym example."*

A good answer names both, says which is known and which is not, and stays in context. If it comes out fluently, the session landed. If not, that is what Session 2 opens with — and no amount of recapping in the last four minutes will fix it, so do not try.

---

## Assessment — the Session 1 test

A **22-question multiple-choice test** covers this session: `Session-01-MC-Test.md`, or **Session 1 · Test** in the site navigation. Every question is scenario-based; none can be answered by recalling a definition.

**When to use it.** Not at the end of this hour — the student has just been told everything and will score well for the wrong reason. Set it **at the start of Session 3**, after the Session 1 homework has been marked and Session 2 has been taught. By then a high score means the material has survived a week, which is what you actually want to know.

Allow **40 minutes**. On the shared screen the answer key is collapsed — click a question to open its explanation, or press **`e`** to open all of them at once.

### Reading the score

| Score /22 | What to do |
|---|---|
| 19–22 | Secure. Do not revisit. |
| 15–18 | Reteach only the items missed, using the diagnostic table in the test. |
| 11–14 | Vocabulary present, concepts not yet working. Re-run Scenario A before going further. |
| 0–10 | Reteach Session 1. Units 3 and 4 depend entirely on this material. |

### The two misses to treat as urgent

- **Question 4 or 22** — parameter versus statistic. Everything from Session 13 onward is built on it.
- **Question 18, especially if they chose option (E)** — counts rising while shares fall. This recurs in every unit and never gets cheaper to fix.

Each wrong answer in the test's key names the misconception it represents, so a marked script tells you what to reteach rather than just how much.

---
---

# Homework — Session 1

**40 marks assessed, plus a 6-mark extension · bring to Session 2**

## How to do this homework

1. **Do every part with the answer key closed.** Where you are unsure, write your answer anyway and put a **?** beside it.
2. **Then open the key and mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote. Your tutor needs to see the wrong answer to know what to fix.
3. **Bring the marked sheet.** The questions you got wrong, and the ones you marked **?** even though they turned out right, are what Session 2 opens with.

A question you guessed correctly is worth flagging. A `?` beside a right answer is more useful to your tutor than a silent tick.

---

## Part A — Vocabulary (8 marks)

Match each term to its definition.

| | Term | | Definition |
|---|---|---|---|
| 1 | Observational unit | A | A numerical summary of a variable for a sample |
| 2 | Population | B | A characteristic that may change from one unit to another |
| 3 | Sample | C | All the items or individuals of interest |
| 4 | Variable | D | A table showing the proportion in each category |
| 5 | Parameter | E | The item or individual a datum is collected from |
| 6 | Statistic | F | A numerical summary of a variable for a population |
| 7 | Frequency table | G | The subset actually measured |
| 8 | Relative frequency table | H | A table showing the count in each category |

## Part B — A new study (12 marks)

> A city has **34,000 registered library members**. The library service wants to know how members use its branches, so it contacts a random **450** of them and records, for each: the branch they use most often, the number of items they borrowed last year, whether they have ever used the e-book service (yes/no), and the total time in hours they spent in library buildings last year.
>
> Of the 450 contacted, **171 said they had used the e-book service**, and members borrowed an average of **22.4 items**.

**B1.** State the population and give **N**. (1)

**B2.** State the sample and give **n**. (1)

**B3.** What is the observational unit? (1)

**B4.** Copy and complete this table for all four variables measured. (6)

| Variable | Categorical or quantitative? | If quantitative: discrete or continuous? |
|---|---|---|
| Branch used most often | | |
| Number of items borrowed | | |
| Ever used e-book service | | |
| Hours spent in buildings | | |

**B5.** Calculate the relative frequency and the percentage of surveyed members who have used the e-book service. **Write the formula you used**, then substitute. Is the result a parameter or a statistic? Explain how you know. (2)

**B6.** Write down one quantity here that is a **parameter**. You do not know its value — describe it in words. (1)

## Part C — Investigative questions (6 marks)

For each, state whether it is a **good investigative question**. If not, explain what is wrong and rewrite it so that it is.

**C1.** "Is our library any good?" (2)

**C2.** "What proportion of registered members used the e-book service in the last year?" (2)

**C3.** After seeing the data, a manager proposes: "Why do members at the Eastside branch borrow so many more items than everyone else?" (2)

## Part D — Building tables (10 marks)

A class of 40 students recorded how each one primarily travelled to school today:

```
Bus   Car   Walk  Bus   Bus   Train Car   Walk  Bus   Bike
Car   Bus   Walk  Bus   Car   Bus   Walk  Bus   Train Car
Bus   Bike  Walk  Bus   Car   Bus   Walk  Car   Bus   Bus
Walk  Car   Bike  Bus   Car   Bus   Walk  Bus   Car   Bus
```

**D1.** Construct a frequency table for mode of travel. (3)

**D2.** Add an *rf* column and a *100rf* column. State the formula for each before you use it. Give proportions to three decimal places and percentages to one decimal place. (4)

**D3.** Apply two of the self-checks: show that Σ*f* = *n* and Σ*rf* = 1. (1)

**D4.** A student claims: *"Most students in this class come to school by bus."* Using your table, justify whether this claim is supported. (2)

## Part E — Challenge (4 marks)

A hospital records the **room number** of every patient and the **number of nights** each patient stayed.

**E1.** Both are recorded using digits. Explain why one is categorical and the other quantitative. Your explanation must refer to units of measure. (2)

**E2.** The hospital calculates the mean of each. One mean is meaningful and one is not. Say which, and explain why. (2)

## Part F — Extension: cumulative frequency (6 marks)

> **Not assessed on the AP exam.** Cumulative frequency does not appear in the current CED. It is here because Barron's uses it heavily and because it makes "or fewer" questions immediate. These 6 marks are separate from the 40 above.

A sports club surveyed **250** members on how many times they visited in the past week.

| Visits | *f* |
|---|---|
| 0 | 40 |
| 1 | 65 |
| 2 | 70 |
| 3 | 45 |
| 4 or more | 30 |

**F1.** Add columns for *rf*, *100rf*, *cf*, *crf* and *100crf*. (3)

**F2.** Apply the two cumulative self-checks: show that the final *cf* equals *n*, and the final *crf* equals 1. (1)

**F3.** What percentage of surveyed members visited **2 times or fewer**? Read it from your table. (1)

**F4.** What percentage visited **more than 2 times**? Get this from your answer to F3 rather than by adding rows. (1)

---
---

# Answer key

*For the student to mark their own work, after attempting everything.*

### Part A (8 marks, 1 each)

1–E · 2–C · 3–G · 4–B · 5–F · 6–A · 7–H · 8–D

### Part B (12 marks)

**B1.** All 34,000 registered library members; N = 34,000. (1)
**B2.** The 450 members contacted; n = 450. (1)
**B3.** One registered library member. (1)

**B4.** (6 — one per correct cell)

| Variable | Type | Discrete/continuous |
|---|---|---|
| Branch used most often | Categorical | — |
| Number of items borrowed | Quantitative | Discrete |
| Ever used e-book service | Categorical | — |
| Hours spent in buildings | Quantitative | Continuous |

**B5.** rf = f ÷ n = 171 ÷ 450 = **0.380**; 100rf = 0.380 × 100 = **38.0%**. (1)
It is a **statistic**, because it was computed from the 450 members in the sample, not from all 34,000 in the population. (1)

**B6.** Any population quantity, e.g. "the true proportion of all 34,000 registered members who have used the e-book service". (1)

> **If you answered "parameter" to B5:** check the denominator. 450 is the number actually asked, so this number describes the sample. Flag it — the most common error on this sheet.

### Part C (6 marks)

**C1.** Not a good question. (1) "Any good" is not defined and cannot be measured — no data collection would settle it. A rewrite must name a measurable variable, e.g. *"What proportion of registered members visited a branch at least once in the last year?"* (1)

**C2.** Good question. (1) Defined purpose, specific measurable variable, and the data can be collected. (1)

**C3.** Not acceptable **for this study**. (1) The question was chosen after seeing the results, which violates the principle that an investigative question should not be changed based on the data analysis. It is legitimate for a **new** study collecting **new** data. (1)

### Part D (10 marks)

**D1.** (3)

| Mode | *f* |
|---|---|
| Bus | 17 |
| Car | 10 |
| Walk | 8 |
| Bike | 3 |
| Train | 2 |
| **Total** | **40** |

**D2.** (4) Formulas: rf = f ÷ n, 100rf = (f ÷ n) × 100, with n = 40.

| Mode | *f* | *rf* | *100rf* |
|---|---|---|---|
| Bus | 17 | 17 ÷ 40 = 0.425 | 42.5% |
| Car | 10 | 10 ÷ 40 = 0.250 | 25.0% |
| Walk | 8 | 8 ÷ 40 = 0.200 | 20.0% |
| Bike | 3 | 3 ÷ 40 = 0.075 | 7.5% |
| Train | 2 | 2 ÷ 40 = 0.050 | 5.0% |
| **Total** | **40** | **1.000** | **100%** |

**D3.** (1) Σf = 17 + 10 + 8 + 3 + 2 = 40 = n ✓ · Σrf = 0.425 + 0.250 + 0.200 + 0.075 + 0.050 = 1.000 ✓

**D4.** (2) The claim is **not** supported. Bus is the most common mode at 42.5%, but "most" means more than half, and 42.5% is below 50%. A supportable version: *"More students travel by bus than by any other single mode, at 42.5%, but fewer than half the class travels by bus."*

> **If you answered "yes, supported":** same plurality-vs-majority distinction as the hospital example in the lesson. Largest share is not the same as most. Flag it.

### Part E (4 marks)

**E1.** (2) Number of nights is quantitative because it is a counted quantity with a unit of measure (nights), and differences are meaningful — 5 nights is two more than 3. Room number has no unit of measure; it is a label identifying a location, so it is categorical even though written with digits.

**E2.** (2) The mean number of nights is meaningful — it is the average length of stay and could inform staffing. The mean room number is meaningless, because room numbers are labels; averaging them produces a number corresponding to nothing, and may not even be a real room.

### Part F — Extension (6 marks)

**F1.** (3) With n = 250:

| Visits | *f* | *rf* | *100rf* | *cf* | *crf* | *100crf* |
|---|---|---|---|---|---|---|
| 0 | 40 | 0.160 | 16.0% | 40 | 0.160 | 16.0% |
| 1 | 65 | 0.260 | 26.0% | 105 | 0.420 | 42.0% |
| 2 | 70 | 0.280 | 28.0% | 175 | 0.700 | 70.0% |
| 3 | 45 | 0.180 | 18.0% | 220 | 0.880 | 88.0% |
| 4 or more | 30 | 0.120 | 12.0% | 250 | 1.000 | 100% |
| **Total** | **250** | **1.000** | **100%** | | | |

Running total: 40 → 105 → 175 → 220 → 250.

**F2.** (1) Final cf = 250 = n ✓ · Final crf = 250 ÷ 250 = 1.000 ✓

**F3.** (1) **70.0%** — read directly from the *100crf* row for 2 visits.

**F4.** (1) 100% − 70.0% = **30.0%**.

### Marks summary

| Part | Marks |
|---|---|
| A — Vocabulary | 8 |
| B — New study | 12 |
| C — Investigative questions | 6 |
| D — Building tables | 10 |
| E — Challenge | 4 |
| **Assessed total** | **40** |
| F — Extension (not AP-assessed) | 6 |

---
---

# Reference sheet — keep this

*Do not read this aloud in the session. Give it to the student at the end. Every term carries an example.*

### Components of a study

**Statistical study** — data are collected from a sample to answer an investigative question about a larger population.
*Example: asking 120 of a school's 1,842 students how they travel, to learn how the whole school travels.*

**Datum · data · data set** — one piece of information about an individual; the plural; a collection of them.
*Example: "Maria walks to school" is one datum. All 120 completed survey forms together are the data set.*

**Population (N)** — all the items or individuals of interest.
*Example: all 1,842 students at Lincoln High, so N = 1,842.*

**Sample (n)** — the subset from which data are actually obtained.
*Example: the 120 students who filled in the survey, so n = 120.*

**In context** — connecting a result back to the real situation it came from. Every interpretation on the exam must be in context; a number alone never earns the point.
*Example: not "0.358", but "35.8% of the students surveyed travelled to school by bus."*

**Investigative question** — has a defined purpose, can be answered with data you can collect, and is not changed after you see the results.
*Example: good — "What proportion of Lincoln High students travel by bus?" Bad — "Is our school any good?", because nothing measurable would settle it.*

> **An investigative question is not an action question.** *"What proportion of members used the e-book service last year?"* is investigative — it names a measurable variable and data can settle it. *"Should we buy more e-books?"* is a **decision**, and *"How can we increase usage?"* is an **action**. A study can inform both, but it cannot answer either. Watch too for questions that **presuppose their own conclusion**: *"Why don't students read any more?"* assumes a fact that has not been established.

### Describing what was measured

**Observational unit** — the individual a datum is collected *from*. One row of your spreadsheet.
*Example: one student. Not one journey, and not one bus.*

**Variable** — a characteristic that may change from one unit to another.
*Example: travel mode changes from student to student, so it is a variable. "School name" is the same for every row, so it is not.*

**Parameter** — a numerical summary for the **population**. Usually unknown.
*Example: the true proportion of all 1,842 students who take the bus. Nobody has measured it.*

**Statistic** — a numerical summary for the **sample**. Known, because you computed it.
*Example: 43 ÷ 120 = 0.358, the proportion of surveyed students who took the bus.*

**Sample size (n) and population size (N)** — facts about the study's design and the population's extent. **Neither is a parameter or a statistic**, because neither is a numerical summary of a variable.
*Example: in the commute study n = 120 and N = 1,842. Neither number tells you what proportion take the bus — that is the parameter, and it is still unknown.*

> **P**opulation → **P**arameter.  **S**ample → **S**tatistic.

### Types of variable

**Categorical (qualitative)** — values are category names or group labels.
*Example: travel mode (bus, car, walk, bike); eye colour; a yes/no answer.*

**Quantitative (numerical)** — numerical values for a measured or counted quantity, generally with **units of measure**.
*Example: journey time in minutes; number of siblings; height in centimetres.*

**Discrete** — countable. Things you *count*.
*Example: number of vehicle changes — 0, 1, 2. Never 1.4.*

**Continuous** — any value in an interval. Things you *measure*.
*Example: journey time — 24 minutes, or 24.6, or 24.61.*

> **The digits test.** A variable written with digits is not automatically quantitative. Does it have **units**? Does **arithmetic on it mean anything**? If not — ZIP code, room number, shirt number, phone number — it is categorical.

> **Discrete or continuous describes the variable, not its summaries.** Number of vehicle changes is discrete, yet the mean number of changes could be 1.4. No student changed 1.4 vehicles — 1.4 is a property of the data set, not a value the variable can take. The same point returns in Unit 2, where a discrete random variable routinely has a non-whole expected value.

### Frequency calculations

Let **n** be the sample size and **f** the count in one category.

| Quantity | Symbol | Formula | Example (f = 84, n = 300) |
|---|---|---|---|
| Frequency | *f* | the count itself | 84 |
| Relative frequency | *rf* | f ÷ n | 84 ÷ 300 = 0.280 |
| Percentage | *100rf* | (f ÷ n) × 100 | 28.0% |
| Cumulative frequency | *cf* | running total of f | 96, then 96+84 = 180, … |
| Cumulative relative frequency | *crf* | cf ÷ n | 180 ÷ 300 = 0.600 |
| Cumulative percentage | *100crf* | (cf ÷ n) × 100 | 60.0% |

**Self-checks:** Σ*f* = *n* · Σ*rf* = 1 · Σ*100rf* = 100% · last *cf* = *n* · last *crf* = 1

**Frequency table** — the **count** in each category.
*Example: St Mary's 84, Riverside 71, … totalling 300.*

**Relative frequency table** — the **proportion** in each category. Must total 1.
*Example: St Mary's 0.280, Riverside 0.237, … totalling 1.000.*

> **Cumulative columns need ordered categories.** "This category or below" only means something if the categories line up. Nights stayed (1, 2, 3, 4, 5+) can be cumulated. Hospital names cannot — "Riverside or fewer" is not a sentence.

> **Percentages of the same total are added, never averaged.** If espresso is 23.0% of orders and tea is 19.0%, together they are **42.0%** — not 21.0%. Averaging percentages is the commonest arithmetic error with these tables.

> **Relative frequency always depends on n.** Drop a category and the total falls, so every remaining percentage rises. A 6% category is not "too small to matter" — removing it changes every other figure in the column.

---
---

# A note on cumulative frequency and the exam

Cumulative frequency, cumulative relative frequency and **cumulative relative frequency plots (ogives)** do **not** appear anywhere in the descriptive statistics of the CED effective Fall 2026. The only occurrence of "cumulative" in all 244 pages is *cumulative probability distribution*, in topic 2.8 — a probability topic, not a data-display one.

Barron's teaches ogives across roughly a dozen pages, including as a display in Unit 1. 5 Steps mentions cumulative frequency only in passing.

**What this means practically.** Teach the cumulative formulas if the student finds them useful — they make "or fewer" questions immediate and they are needed to read Barron's without confusion. But do not spend session time on constructing or interpreting ogives, and tell the student plainly that it will not be examined.

**This belongs on the removed-topics list** in the master plan, as a seventh entry alongside inference for slopes, chi-square goodness-of-fit, geometric distributions, transformations to achieve linearity, influential points and leverage, and the Investigative Task.

---
---

# Converting the remaining nineteen sessions

Every activity in the master plan came from the CED's Sample Instructional Activities, which assume a class. Ten work one-to-one essentially unchanged — they were already pair activities. The rest need substitution.

Two moves cover almost all of it: **you take the opposing position**, or **you produce deliberately flawed work and the student marks it**.

| # | Classroom activity | One-to-one version |
|---|---|---|
| 1 | Population or Sample? (groups of 4) | **Challenge Sort** — student sorts aloud, you argue the opposite side each time |
| 2 | Gallery Walk (4 groups, 4 displays) | **Build & Defend** — student builds all four displays, then you ask which best answers each of three different questions |
| 3 | Match Mine (pairs, screen between) | Works as-is. You describe, student sketches unseen; then swap |
| 4 | Sketch and Switch (pairs swap) | **Sketch and Critique** — student sketches from a prompt; you sketch one with a deliberate error and they find it |
| 5 | Reversing Interpretations (pairs) | Works as-is. You supply the residual and equation |
| 6 | Odd One Out (groups of 4) | Student sorts four studies aloud and justifies; you add a fifth card mid-task |
| 7 | Password-Style Game (pairs) | Works as-is. Alternate who gives clues |
| 8 | Quiz-Quiz-Trade (class circulation) | **Card Author** — student *writes* the question cards; you answer some wrong on purpose and they mark you |
| 9 | Think-Pair-Share (pairs) | **Think-Aloud** — student names the formula for each of the five, narrating the reasoning, no calculation |
| 10 | Independent or Mutually Exclusive? sort | Works as-is. Probe every answer, including the right ones |
| 11 | Predict and Confirm (neighbour talk) | Student writes the prediction down **before** running the simulation |
| 12 | Reversing Interpretations (pairs, 4 curves) | Works as-is |
| 13 | The Scribe and the Calculator (pairs) | Works as-is, and is excellent one-to-one. Take the two roles, then swap |
| 14 | Sentence Starters | Works as-is. You supply flawed conclusion sentences to repair |
| 15 | Consequences Sort (groups) | Student ranks the six scenarios; you take the opposing view on two |
| 16 | Error Analysis (pairs, 20 sets) | Works as-is. Time it — twenty in eight minutes builds exam pace |
| 17 | Homogeneity or Independence? sort | Works as-is |
| 18 | Quick Write (whole class) | Works as-is. Two minutes, no notes, pen down at time |
| 19 | Round Table (groups of 4, papers rotate) | **Mark My Work** — student does problem 1; you do problem 2 with a planted error; they mark yours |
| 20 | Graphic Organizer (teams) | Student builds the flowchart alone; you stress-test it with edge cases |

**Work unchanged:** 3, 5, 7, 10, 12, 13, 14, 16, 17, 18. **Need substitution:** 1, 2, 4, 6, 8, 9, 11, 15, 19, 20.

### Two things to carry through every session

**Diagnose before you teach.** Open every session with two or three questions establishing what is already there. The plan's per-session content is a menu, not a script.

**Protect the talk ratio.** The student should be talking at least half of every hour. Four minutes of unbroken explanation from you is the signal to stop and ask something.

---

*CED references: Topic 1.1 (1.1.A.1–6, 1.1.B.1–2), Topic 1.2 (1.2.A.1–5, 1.2.B.1–2, 1.2.C.1–2), Topic 1.3 (1.3.A.1–2, 1.3.B.1–2). Course and Exam Description effective Fall 2026.*

*Supporting reading: Barron's pdf 79–83 · Princeton Review 99–104 · 5 Steps to a 5 53–58.*
