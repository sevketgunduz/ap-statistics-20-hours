# Session 1 — What Is a Statistical Study?

**AP Statistics · Twenty-Hour Course · Student edition, to work through on your own**
**CED Topics 1.1, 1.2, 1.3 · About 75 minutes, plus homework**

---

## How to use this

This booklet covers exactly the same ground as your tutor's Session 1, in the same order, using the same two scenarios. If you are doing it before the session, you will arrive ready. If you are doing it instead of the session, or to revise afterwards, it works alone.

**There is one rule, and the whole thing collapses without it.**

> Every **Your turn** box asks you a question before the text answers it. **Write your answer down first — on paper, in words — and only then reveal the answer.**

You will be tempted to read ahead. Don't. Reading an answer produces a strong feeling of "yes, I knew that", and that feeling is not knowledge — it is recognition, and it disappears in an exam. Writing your answer first is the only way to find out whether you actually knew it.

**What you need:** paper, a pen, and about 75 minutes. No calculator today.

### How this maps to your tutor's document

| Your section | Tutor's section | Minutes |
|---|---|---|
| Part 1 — What do you already know? | 0–6 The diagnostic | 8 |
| Part 2 — Why this matters | 6–8 Frame the hour | 3 |
| Part 3 — The commute study | 8–22 Scenario A | 20 |
| Part 4 — Six studies: hold your ground | 22–30 Challenge Sort | 12 |
| Part 5 — The hospital survey | 30–46 Scenario B | 20 |
| Part 6 — On your own: the gym | 46–54 Solo case | 8 |
| Part 7 — Explain it back | 54–60 Teach it back | 5 |

---

## Part 1 — What do you already know?

Four questions. Answer all four on paper before reading any further. Guessing is fine; leaving one blank is not.

**Q1.** A school wants to know the average height of its students. It measures 50 of them. What would you call the 50, and what would you call all the students?

**Q2.** If I told you the average height of those 50 was 168 cm — is that the answer to the school's question?

**Q3.** Give me two things you could measure about a person where one is a number and one is not.

**Q4.** Is a phone number a number?

<details>
<summary><strong>Now check — what your answers tell you</strong></summary>

| If you said | What it means | What to do |
|---|---|---|
| **Q1:** the 50 are a *sample*, all students are the *population* | You have the vocabulary | Good — read Part 3 quickly, slow down at "parameter or statistic" |
| **Q1:** you weren't sure, or you swapped them | The foundation isn't there yet | Read Part 3 slowly and write out every answer. Don't rush to Part 5 |
| **Q2:** "no — it's only an estimate of the real answer" | You already have the central idea of the whole course | Excellent. Part 3 will name what you already understand |
| **Q2:** "yes" | **This is the most common answer, and it is the gap this session closes.** The 50 tell you about the 50 | Part 3 is the important part for you. Do not skim it |
| **Q3:** e.g. height in cm (a number) and eye colour (not) | Fine | Move on |
| **Q4:** "no — it's a label, you can't average phone numbers" | You already have the digits test | Part 5 will confirm it |
| **Q4:** "yes, it's made of digits" | A real trap is waiting for you | Part 5 is built around exactly this. Watch for it |

</details>

---

## Part 2 — Why this matters

Everything in this course is one of four moves:

> **Pose a question · Collect data · Analyse data · Interpret the result**

Those four are the College Board's four **Statistical Practices**, and every topic between now and the exam is a tool used at one of those four stages. The exam is built on them: two of your four free-response questions are aimed directly at them.

Today is entirely the first two moves. There is almost no calculation. That can make this session feel like it doesn't count — it does. If you cannot say precisely what your population is, everything in Unit 3 falls apart, and Unit 3 is the largest single part of the exam.

---

## Part 3 — The commute study

Read this twice before you go on.

> Lincoln High School has **1,842 students**. The principal wants to reorganise the morning bus timetable but does not know how students currently get to school. She asks a randomly chosen **120 students** to record, on one Tuesday: how they primarily travelled to school, how many minutes the journey took, and how many separate vehicles they had to change between.
>
> Of the 120 surveyed, **43 came by bus**, and their journeys averaged **24.6 minutes**.

### Who is the study about?

**Your turn.** Write down: who is this study actually about? All 1,842 students, or the 120 who answered?

<details>
<summary><strong>Reveal</strong></summary>

All **1,842**. Ask yourself whether the principal would be satisfied knowing only about those 120 — of course not. She has to run a timetable for the whole school.

- **Population** — all the individuals of interest. Here, all 1,842 Lincoln High students. We write its size as **N = 1,842**.
- **Sample** — the subset you actually collect data from. Here, the 120 surveyed. We write its size as **n = 120**.

Notice the population is decided by **the question**, not by the data. The principal is not trying to say anything about students at other schools, so they are not in the population.

</details>

### What is one row of the data?

**Your turn.** Imagine the results as a spreadsheet. What does one row represent?

<details>
<summary><strong>Reveal</strong></summary>

**One student.** This is the question that catches people out — plenty of people answer "one journey" or "one bus".

- **Observational unit** — the individual each piece of data is collected *from*. One row of your spreadsheet.

The data are not about journeys and not about buses. They are about students, each of whom happens to have a journey.

</details>

### Sorting the variables

Three things were measured on each student: **mode of travel**, **journey time in minutes**, and **number of vehicle changes**.

**Your turn.** Sort them into "numbers" and "not numbers". Then look again at the two that are numbers — is there any difference between them? Could someone change 1.4 vehicles? Could a journey take 24.61 minutes?

<details>
<summary><strong>Reveal</strong></summary>

- **Variable** — a characteristic that may change from one observational unit to another.
- **Categorical** (also called qualitative) — the values are category names or group labels.
- **Quantitative** (also called numerical) — the values are measured or counted quantities, and generally have **units of measure**.
- **Discrete** quantitative — countable. Things you *count*.
- **Continuous** quantitative — can take any value in an interval. Things you *measure*.

| Variable | Type | Why |
|---|---|---|
| Mode of travel | Categorical | Bus, car, walk, bike are group labels |
| Journey time | Quantitative, **continuous** | Measured in minutes; 24.61 is possible |
| Number of vehicle changes | Quantitative, **discrete** | Counted; you change 0, 1 or 2, never 1.4 |

</details>

![Decision tree for classifying a variable](figures/variable-types.svg)

*Keep this. It is the fastest way to classify any variable you meet, and the box on the left is the trap that Part 5 is built around.*

### The centre of the whole course

This next bit is the most important thing in the session. Take it slowly.

**Your turn.** Two questions, and they are not the same question.

1. What proportion of **all 1,842** students come to school by bus?
2. What proportion of **the 120 surveyed** came to school by bus?

<details>
<summary><strong>Reveal</strong></summary>

1. **We don't know.** Nobody asked all 1,842. If you wrote 0.358, ask yourself: how many of the 1,842 did she actually ask?
2. **43 ÷ 120 = 0.358.** We know this exactly, because we computed it from data we have.

That difference has names:

- **Parameter** — a numerical summary of a variable for the **population**. Usually **unknown**.
- **Statistic** — a numerical summary of a variable for the **sample**. **Known**, because you computed it.

| Quantity | Which | Do we know it? |
|---|---|---|
| Proportion of **all 1,842** who come by bus | Parameter | No |
| 43 ÷ 120 = 0.358, proportion of the **sampled** students | Statistic | Yes |
| Mean journey time of **all 1,842** | Parameter | No |
| 24.6 minutes, the mean for the **120** | Statistic | Yes |

**Every single thing you do from Session 13 onwards is about the gap between those two columns.** That is the subject. Confidence intervals, hypothesis tests, p-values — all of it is machinery for saying something responsible about the left column when all you have is the right one.

**The memory hook:** **P**opulation goes with **P**arameter. **S**ample goes with **S**tatistic.

</details>

![A sample inside a population, a statistic estimating an unknown parameter](figures/study-structure.svg)

*This one picture is most of AP Statistics. The sample sits **inside** the population — it is a subset, not a separate group. You measure the sample, compute a statistic, and use it to estimate a parameter you will never actually see.*

### The investigative question

An **investigative question** is the question the study exists to answer. A good one has a defined purpose, can be answered with data you are able to collect, and — this is the part people miss — **is not changed after you see the results**.

**Your turn.** Here is the trap. Read it and commit to an answer before revealing.

> The principal looks at her results and notices that cyclists have much longer journeys than she expected. She's curious, so she rewrites her report to answer: *"Why do cyclists take so long?"*
>
> Is that allowed?

<details>
<summary><strong>Reveal</strong></summary>

**No** — and most people say yes, because it sounds like good scientific curiosity.

Two things are wrong with it:

1. **How many cyclists were there?** Out of 120 students, perhaps four. A pattern in four people is very weak evidence.
2. **She only asked the question because she spotted the pattern.** If she had gone looking, she could probably have found *some* odd-looking pattern in any of the three variables. Choosing your question after seeing which pattern looks interesting is how you end up "discovering" things that are just noise.

This is CED requirement **1.1.B.1**: an investigative question should not be changed based on the data analysis or results.

It is a perfectly good question — for a **new** study, collecting **new** data, designed to answer it.

</details>

---

## Part 4 — Six studies: hold your ground

Your tutor does this by arguing with you. On your own, the argument is printed.

For each study: write down the **population**, the **sample**, the **observational unit**, and **one variable with its type**. Then read the challenge — someone disagreeing with you — and write a one-sentence rebuttal **before** you reveal the resolution.

If the challenge makes you change your mind, that is useful information: it means your first answer was a guess, not a reason.

### Study 1
*A supermarket chain wants to know how long its customers wait at the checkout. Staff time 200 randomly chosen customers one Saturday.*

**Challenge:** *"The population is the 200 customers they timed — those are the people the study is about."*

<details>
<summary><strong>Reveal</strong></summary>

Population: all the chain's customers. Sample: the 200 timed. Unit: one customer. Variable: waiting time in minutes — quantitative, continuous.

The challenge confuses the sample with the population. The 200 are who they *measured*; the chain's customers generally are who they want to *know about*. If the 200 were the population, there would be nothing left to estimate and no reason to sample.

</details>

### Study 2
*A phone manufacturer tests 500 randomly selected batteries from a production run of 80,000, to estimate how long the run's batteries last.*

**Challenge:** *"The observational unit is the production run."*

<details>
<summary><strong>Reveal</strong></summary>

Population: all 80,000 batteries in the run, N = 80,000. Sample: the 500 tested, n = 500. Unit: **one battery**. Variable: lifetime in hours — quantitative, continuous.

The production run is the population, not the unit. The unit is whatever a single measurement is taken from — and you measure the lifetime of one battery at a time.

</details>

### Study 3
*A researcher wants to know the average lifespan of a species of tortoise. She studies the 23 tortoises living at one zoo.*

**Challenge:** *"The population is the 23 tortoises, because those are the ones she studied."*

<details>
<summary><strong>Reveal</strong></summary>

Population: all tortoises of that species. Sample: the 23 at the zoo. Unit: one tortoise. Variable: lifespan in years — quantitative, continuous.

Again, what she *studied* is the sample. What she wants to *know about* is the species — that is the population, and it is much larger than 23.

Worth noticing for later: 23 tortoises at a single zoo may be a poor stand-in for the whole species, since zoo animals are fed and protected. The sample is still a sample; it just may not be a good one. Session 6 is about exactly that.

</details>

### Study 4
*A city surveys 600 of its 140,000 residents about a proposed bus route, recording for each whether they support it. Support is coded 1 for yes and 0 for no.*

**Challenge:** *"Support is recorded as 1 and 0, so it's a quantitative variable."*

<details>
<summary><strong>Reveal</strong></summary>

Population: all 140,000 residents, N = 140,000. Sample: the 600 surveyed, n = 600. Unit: one resident. Variable: whether they support the route — **categorical**.

The 1 and the 0 are labels standing in for "yes" and "no". They have no units, and arithmetic on them is not measuring anything — "the average support is 0.62" only means something because you have secretly converted it into *a proportion of yeses*, which is a categorical summary.

Coding a category as a digit does not turn it into a quantity. Hold this thought for Part 5.

</details>

### Study 5
*A researcher tests every lightbulb coming off one production line during one shift, to judge the quality of the factory's output.*

**Challenge:** *"This isn't a sample at all — she tested every single one."*

<details>
<summary><strong>Reveal</strong></summary>

**It depends on the investigative question**, and that is the whole point of this card.

- If the question is *"how good was this shift's output?"* — she measured every item of interest. That is a **census**, not a sample, and her figures are **parameters**.
- If the question is *"how good is this factory's output in general?"* — then one shift is a **sample** of the factory's ongoing production, and her figures are **statistics**.

**The population is not a property of the data. It is a property of the question you are asking.** Two researchers with identical data can have different populations.

</details>

### Study 6
*A teacher records the marks of all 28 students in her class, to decide whether to re-teach a topic to that class.*

**Challenge:** *"She calculates the mean mark. That's a statistic."*

<details>
<summary><strong>Reveal</strong></summary>

Population: the 28 students in her class. Sample: **there isn't one** — she measured everybody. Unit: one student. Variable: mark — quantitative (discrete if marks are whole numbers).

Her mean is a **parameter**, not a statistic, because it summarises the entire population of interest.

This is the card worth remembering: **"the mean" is not automatically a statistic.** Whether a number is a parameter or a statistic depends entirely on whether you measured everybody or only some.

</details>

---

## Part 5 — The hospital survey

> A regional hospital network discharged **12,400 patients** last year across six hospitals. To review its care, the network surveys **300** of those patients, recording for each: which hospital treated them, their room number, the number of nights they stayed, and the time in minutes from arrival to being seen by a doctor.
>
> Results by hospital: **St Mary's 84, Riverside 71, Northgate 52, Parkview 45, Eastwood 30, Hillcrest 18.**

**Your turn.** You should be able to do these without help now. Population and N? Sample and n? Observational unit?

<details>
<summary><strong>Reveal</strong></summary>

Population: all 12,400 patients discharged last year, **N = 12,400**. Sample: the 300 surveyed, **n = 300**. Observational unit: one discharged patient.

If you needed to stop and think about these, go back and reread Part 3 before continuing.

</details>

### The digits trap

**Your turn.** Classify all four variables: hospital, room number, nights stayed, minutes until seen by a doctor.

Then, before revealing — answer this one honestly: **what is the average room number in this hospital?**

<details>
<summary><strong>Reveal</strong></summary>

If you tried to answer the room-number question, you probably realised you couldn't say what it would *mean*. Suppose it came out as 247.6. Is there a room 247.6? What would a manager do with that number?

| Variable | Type | Why |
|---|---|---|
| Hospital | Categorical | Six group labels |
| Room number | **Categorical** | Written with digits, but it is a label. No units of measure. The mean means nothing |
| Nights stayed | Quantitative, discrete | A count, with units. 5 nights is genuinely two more than 3 |
| Minutes until seen | Quantitative, continuous | Measured; 47.3 minutes is possible |

**The digits test — memorise this.** A variable written with digits is not automatically quantitative. Ask two questions:

> Does it have **units of measure**? Does **arithmetic on it mean anything**?

If the answer to both is no — ZIP code, room number, shirt number, phone number, the 1/0 coding from Study 4 — it is **categorical**.

If you answered "yes, it's a number" to Q4 back in Part 1, this is the correction. Go back and look at that question again now.

</details>

### The frequency formulas

Everything in this section is a division. The only difficulty is knowing which number goes underneath.

Let **n** be the sample size and **f** the frequency — the count — in one category.

| Quantity | Symbol | Formula | In words |
|---|---|---|---|
| Frequency | *f* | the count itself | How many are in this category |
| Relative frequency | *rf* | **rf = f ÷ n** | What fraction of the whole are in this category |
| Percentage | *100rf* | **100rf = (f ÷ n) × 100** | The same thing, out of 100 |
| Cumulative frequency | *cf* | **cf = running total of f** | How many are in this category **or below** |
| Cumulative relative frequency | *crf* | **crf = cf ÷ n** | What fraction are in this category or below |
| Cumulative percentage | *100crf* | **100crf = (cf ÷ n) × 100** | The same thing, out of 100 |

> **A note on notation.** Some textbooks write the last two as *100cf*. That is shorthand for "the cumulative figure expressed as a percentage" — it does **not** mean 100 × cf. The denominator is always *n*.

**The five self-checks.** Learn these; they catch nearly every arithmetic slip you will make:

- Σ*f* = *n* — the frequencies add to the sample size
- Σ*rf* = 1 — the relative frequencies add to one
- Σ*100rf* = 100% — the percentages add to one hundred
- the **last** *cf* = *n*
- the **last** *crf* = 1

### Building the categorical table

**Your turn.** Build the full table for the six hospitals: *f*, *rf* to three decimal places, and *100rf* to one decimal place. Then apply the self-checks. Do this on paper before revealing — it takes about three minutes.

<details>
<summary><strong>Reveal</strong></summary>

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

</details>

**Your turn.** Could you add a cumulative frequency column to that table? Why, or why not?

<details>
<summary><strong>Reveal</strong></summary>

**No** — and the reason is the interesting part.

Cumulative means "this category **or below**". That phrase only means something if the categories have an **order**. Hospital names have none. *"Riverside or fewer"* is not a sentence — it doesn't describe anything.

Cumulative columns belong to variables you can line up in order. Which is exactly why the next table works and this one doesn't.

</details>

### Building the ordered table

The same 300 patients, now by **number of nights stayed**. This variable *is* ordered, so all six quantities apply.

**Your turn.** Copy this and fill in the four missing columns.

| Nights | *f* | *rf* | *100rf* | *cf* | *crf* | *100crf* |
|---|---|---|---|---|---|---|
| 1 | 96 | | | | | |
| 2 | 84 | | | | | |
| 3 | 60 | | | | | |
| 4 | 36 | | | | | |
| 5 or more | 24 | | | | | |
| **Total** | **300** | | | | | |

<details>
<summary><strong>Reveal</strong></summary>

| Nights | *f* | *rf* | *100rf* | *cf* | *crf* = cf ÷ 300 | *100crf* |
|---|---|---|---|---|---|---|
| 1 | 96 | 0.320 | 32.0% | 96 | 0.320 | 32.0% |
| 2 | 84 | 0.280 | 28.0% | 180 | 0.600 | 60.0% |
| 3 | 60 | 0.200 | 20.0% | 240 | 0.800 | 80.0% |
| 4 | 36 | 0.120 | 12.0% | 276 | 0.920 | 92.0% |
| 5 or more | 24 | 0.080 | 8.0% | 300 | 1.000 | 100% |
| **Total** | **300** | **1.000** | **100%** | | | |

The running total, one step at a time:
**96 → 96 + 84 = 180 → 180 + 60 = 240 → 240 + 36 = 276 → 276 + 24 = 300** ✓

Checks: last *cf* = 300 = *n* ✓ · last *crf* = 1.000 ✓

</details>

**Your turn.** Now use it. What percentage of these patients stayed **three nights or fewer**? And what percentage stayed **more than three nights**?

<details>
<summary><strong>Reveal</strong></summary>

**80.0%** — read straight off the *100crf* column at the "3 nights" row. That is what the cumulative column is *for*. Without it you would have to add 96 + 84 + 60 and then divide by 300 — which is exactly the work the column already did.

**100% − 80.0% = 20.0%** stayed more than three nights. Taking the complement is the second reason the column is worth having: once you have "or fewer", you get "more than" for free.

</details>

> **Be aware:** cumulative frequency does **not** appear anywhere in the current AP Statistics course description. It is here because Barron's uses it heavily and because it makes "or fewer" questions trivial — but you will not be examined on it as a technique. Learn it for reading your prep book, not for the exam. There is a fuller note at the end.

### Justifying a claim

**Your turn.** An administrator says: *"Most of our discharged patients came from St Mary's."* Using your table, is she right? Write a full sentence.

<details>
<summary><strong>Reveal</strong></summary>

**No.** St Mary's accounts for 28.0% — the largest single share, but nowhere near a majority. "Most" means more than half.

A defensible version of her claim:

> *"St Mary's accounted for more discharged patients than any other single hospital in the sample, at 28.0%, though it still treated fewer than three in ten."*

**This is the shape of every justification in this course**, and you will use it in every unit from here to the exam:

> **State the claim · quote the number · say what the number does and does not establish · keep it in context.**

"In context" means naming the variable, its units and the individuals. A number on its own never earns the mark.

</details>

---

## Part 6 — On your own: the gym

No hints, no reveals until you have finished all six. Write full answers.

> A gym has **2,300 members**. It surveys **180** of them, recording: membership type (basic/premium/student), locker number, number of visits last month, and minutes spent per visit.
>
> Of the 180 surveyed, **54 had premium membership**.

1. Population and **N**? Sample and **n**?
2. Observational unit?
3. Classify all four variables.
4. Calculate the relative frequency and percentage for premium membership. Show the formula.
5. Is that figure a parameter or a statistic? How do you know?
6. Name one parameter here whose value you do not know.

<details>
<summary><strong>Reveal</strong></summary>

1. Population: all 2,300 gym members, N = 2,300. Sample: the 180 surveyed, n = 180.
2. One gym member.
3. Membership type — categorical. **Locker number — categorical** (digits, but a label with no units). Number of visits — quantitative, discrete. Minutes per visit — quantitative, continuous.
4. rf = f ÷ n = 54 ÷ 180 = **0.300**, so 100rf = 0.300 × 100 = **30.0%**.
5. A **statistic** — it was computed from the 180 members in the sample, not from all 2,300 in the population.
6. For example, the true proportion of all 2,300 members with premium membership. Or the mean number of visits for all 2,300.

**If you classified locker number as quantitative**, the digits test has not stuck yet. Go back to Part 5 and read that section again now, while you can see why it matters. This will come back.

</details>

---

## Part 7 — Explain it back

The last five minutes, and the most useful.

**Your turn.** Without looking at anything above, write a short paragraph — five or six sentences — explaining the difference between a parameter and a statistic **to someone who has never taken this course**. Use the gym example.

Then check it against this list.

<details>
<summary><strong>The checklist</strong></summary>

A good answer:

- [ ] names both terms
- [ ] says a parameter describes the **population** and is usually **unknown**
- [ ] says a statistic describes the **sample** and is **known** because you computed it
- [ ] gives a concrete example of each from the gym
- [ ] stays **in context** — mentions members, membership type, the gym

A model answer:

> *"A gym has 2,300 members, but the survey only asked 180 of them. The true proportion of all 2,300 members who hold premium membership is a **parameter** — it describes the whole population, and nobody knows what it is, because nobody asked all 2,300. The proportion among the 180 who were surveyed is 54 ÷ 180 = 0.300, or 30.0%. That is a **statistic** — it describes the sample, and we know it exactly because we worked it out from data we actually have. The statistic is our best guess at the parameter, but the two are not the same number, and the rest of this course is about how far apart they are likely to be."*

If your paragraph came out fluently, this session has landed. If it didn't, that is worth telling your tutor at the start of the next session — it is much more useful to them than saying "it was fine".

</details>

---

## Test yourself

When you have finished this booklet and marked the homework, there is a **22-question test** on this session — `Session-01-MC-Test.md`, or **Session 1 · Test** in the site navigation.

**Do not take it today.** You have just read the answers to everything; you would score well and learn nothing. Leave it until you have done Session 2, then sit it cold with a 40-minute limit. A good score a week later actually means something.

Every explanation says why the right answer is right **and what each wrong answer means** — so if you miss one, you find out which idea to go back to, not just that you lost a mark. The answers stay hidden until you click a question.

---
---

# Homework — Session 1

**40 marks assessed, plus a 6-mark extension · bring to Session 2**

## How to do this homework

1. Do every part **with the answer key closed.** Where you are unsure, write your answer anyway and put a **?** beside it.
2. Then open the key and **mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote. Your tutor needs to see the wrong answer to know what to fix.
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

**B6.** Write down one quantity in this situation that is a **parameter**. You do not know its value — describe it in words. (1)

## Part C — Investigative questions (6 marks)

For each proposed question, state whether it is a **good investigative question**. If not, explain what is wrong and rewrite it so that it is.

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

**D2.** Add an *rf* column and a *100rf* column. State the formula for each before you use it. Proportions to three decimal places, percentages to one. (4)

**D3.** Apply two of the self-checks: show that Σ*f* = *n* and Σ*rf* = 1. (1)

**D4.** A student claims: *"Most students in this class come to school by bus."* Using your table, justify whether this claim is supported. (2)

## Part E — Challenge (4 marks)

A hospital records the **room number** of every patient and the **number of nights** each patient stayed.

**E1.** Both variables are recorded using digits. Explain clearly why one is categorical and the other is quantitative. Your explanation must refer to units of measure. (2)

**E2.** The hospital calculates the mean of each variable. One of these means is meaningful and one is not. Say which is which, and explain why. (2)

## Part F — Extension: cumulative frequency (6 marks)

> **Not assessed on the AP exam.** These 6 marks are separate from the 40 above.

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

*Open only after attempting everything.*

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

> **If you answered "parameter" to B5:** check the denominator. 450 is the number actually asked, so this number describes the sample. Flag this one for your tutor — it is the most common error on this sheet.

### Part C (6 marks)

**C1.** Not a good question. (1) "Any good" is not defined and cannot be measured — no data collection would settle it. A rewrite must name a measurable variable, e.g. *"What proportion of registered members visited a branch at least once in the last year?"* (1)

**C2.** Good question. (1) Defined purpose, specific measurable variable, and the required data can be collected. (1)

**C3.** Not acceptable **for this study**. (1) The question was chosen after seeing the results, which violates the principle that an investigative question should not be changed based on the data analysis. The Eastside pattern may be real or may be chance variation. It is a legitimate question for a **new** study collecting **new** data. (1)

### Part D (10 marks)

**D1–D2.** (7) Formulas: rf = f ÷ n, 100rf = (f ÷ n) × 100, with n = 40.

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

> **If you answered "yes, supported":** this is the same plurality-versus-majority distinction as the hospital example in Part 5. The largest share is not the same as "most". Flag it.

### Part E (4 marks)

**E1.** (2) Number of nights is quantitative because it is a counted quantity with a unit of measure (nights), and differences are meaningful — 5 nights is two more than 3. Room number has no unit of measure; it is a label identifying a location, so it is categorical even though it is written with digits.

**E2.** (2) The mean number of nights is meaningful — it is the average length of stay and could inform staffing. The mean room number is meaningless, because room numbers are labels; averaging them produces a number corresponding to nothing, and possibly not even a real room.

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

Every term carries an example. This is the page to revise from.

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
*Example: travel mode changes from student to student, so it is a variable. "School name" is the same in every row, so it is not.*

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

> **The digits test.** A variable written with digits is not automatically quantitative. Does it have **units**? Does **arithmetic on it mean anything**? If not — ZIP code, room number, shirt number, phone number, a 1/0 code for yes/no — it is categorical.

> **Discrete or continuous describes the variable, not its summaries.** Number of vehicle changes is discrete, yet the mean number of changes could be 1.4. No student changed 1.4 vehicles — 1.4 is a property of the data set, not a value the variable can take. The same point returns in Unit 2, where a discrete random variable routinely has a non-whole expected value.

### Frequency calculations

Let **n** be the sample size and **f** the count in one category.

| Quantity | Symbol | Formula | Example (f = 84, n = 300) |
|---|---|---|---|
| Frequency | *f* | the count itself | 84 |
| Relative frequency | *rf* | f ÷ n | 84 ÷ 300 = 0.280 |
| Percentage | *100rf* | (f ÷ n) × 100 | 28.0% |
| Cumulative frequency | *cf* | running total of f | 96, then 96 + 84 = 180, … |
| Cumulative relative frequency | *crf* | cf ÷ n | 180 ÷ 300 = 0.600 |
| Cumulative percentage | *100crf* | (cf ÷ n) × 100 | 60.0% |

**Self-checks:** Σ*f* = *n* · Σ*rf* = 1 · Σ*100rf* = 100% · last *cf* = *n* · last *crf* = 1

**Frequency table** — the **count** in each category.
*Example: St Mary's 84, Riverside 71, … totalling 300.*

**Relative frequency table** — the **proportion** in each category. Must total 1.
*Example: St Mary's 0.280, Riverside 0.237, … totalling 1.000.*

> **Cumulative columns need ordered categories.** "This category or below" only means something if the categories line up. Nights stayed (1, 2, 3, 4, 5+) can be cumulated. Hospital names cannot — *"Riverside or fewer"* is not a sentence.

> **Percentages of the same total are added, never averaged.** If espresso is 23.0% of orders and tea is 19.0%, together they are **42.0%** — not 21.0%. Averaging percentages is the commonest arithmetic error with these tables.

> **Relative frequency always depends on n.** Drop a category and the total falls, so every remaining percentage rises. A 6% category is not "too small to matter" — removing it changes every other figure in the column.

---

## A note on cumulative frequency and the exam

Cumulative frequency, cumulative relative frequency and **cumulative relative frequency plots (ogives)** do **not** appear anywhere in the descriptive statistics of the AP Statistics Course and Exam Description effective Fall 2026. The only occurrence of "cumulative" in all 244 pages is *cumulative probability distribution*, in topic 2.8 — a probability topic, not a data-display one.

Barron's teaches ogives across roughly a dozen pages, including as a Unit 1 display. 5 Steps mentions cumulative frequency only in passing.

**What this means for you.** The cumulative formulas are worth knowing — they make "or fewer" questions immediate, and you need them to read Barron's without confusion. But do not spend revision time on constructing or interpreting ogives. It will not be examined.

---

*CED references: Topic 1.1 (1.1.A.1–6, 1.1.B.1–2), Topic 1.2 (1.2.A.1–5, 1.2.B.1–2, 1.2.C.1–2), Topic 1.3 (1.3.A.1–2, 1.3.B.1–2). Course and Exam Description effective Fall 2026.*

*Further reading: Barron's pdf 79–83 · Princeton Review 99–104 · 5 Steps to a 5 53–58.*

*Next session: Topics 1.4–1.6 — bar charts and pie charts, dotplots, stemplots and histograms, and the four things you must say to describe any distribution.*
