# Session 7 — Collecting Data: Bias and Experimental Design

**AP Statistics · Twenty-Hour Course · Student edition, to work through on your own**
**CED Topics 1.12, 1.13 · About 204 minutes, plus homework**

---

## How to use this

Session 6 asked how a study chose its units and what that lets it conclude. Today asks what goes wrong. A sampling method can be wrong **in the same direction every time**, and the course description calls that **bias**. An experiment can be well or badly designed, and the course description names exactly what a well-designed one contains. There is very little arithmetic. The marks go to **exact names, directions and reasons**, so the writing is the whole of the work.

:::note amber Write first, then reveal
Every **Your turn** box asks you to do something before the text shows you the answer. **Do it on paper first.** The names of the biases, their directions, the designs and every judgement are hidden behind reveals so that you cannot read them before you commit. A wrong answer you wrote yourself, and then corrected, stays with you; a right one you read does not.
:::

**What you need:** paper and a pen. A calculator helps in Parts 3 and 5. Part 3 has an interactive tool; it works on a phone, but a larger screen is easier.

### How this maps to your tutor's document

Working alone with a pen is slower than working with a tutor, so each part is given about a quarter longer than the tutor's segment. Take the time.

| Your section | Tutor's section | Minutes |
|---|---|---|
| Part 1 — Your Session 6 homework, and a warm-up | 0–12 Homework debrief and diagnostic | 15 |
| Part 2 — Theory: bias in samples, and the design of experiments | 12–54 Theory — bias in samples, and the design of experiments | 53 |
| Part 3 — Lincoln High's travel survey against a known parameter | 54–89 Scenario A | 44 |
| Part 4 — Password, on your own | 89–107 Activity | 23 |
| Part 5 — St Mary's reminder experiment | 107–142 Scenario B | 44 |
| Part 6 — On your own: Riverside's hand-cream trial | 142–154 Solo case | 15 |
| Part 7 — Explain it back | 154–162 Teach it back | 10 |
| **Total** | **162 minutes** | **204** |

If your tutor has not yet set the **Session 5 test**, take it before Part 1: 20 questions, 35 minutes, timed, answer key closed.

:::note red Words you may have met that the course description does not use
**Lurking variable**, **Hawthorne effect**, **selection bias**, **measurement bias**, **interviewer bias**, **sampling error**, **randomized comparative experiment**, **crossover design**, **sampling frame**, **multistage sampling**, **quota sampling** and **scope of inference** are prep-book terms, not examinable. Use *extraneous variable* or *confounding variable* for a lurking variable; the four named biases in Part 2 cover selection and measurement bias; a design in which each unit receives both treatments in a random order is a **matched pairs design**.
:::

---

## Part 1 — Your Session 6 homework, and a warm-up

Get out your marked Session 6 homework and make two lists: the questions you got **wrong**, and the questions you marked with a **?**, including the ones that turned out right.

**Two specific things to check.** They are two of the likeliest errors on that sheet, and both come back today in a new form.

- **B1: did you call Plan Q a cluster sample, or Plan R a stratified one?** Plan Q took 50 patients from every hospital: some from every group, so stratified. Plan R took every patient in 3 of the 124 wards: everyone from some groups, so cluster. Today adds a third way of using groups: in a **randomized block design** the units are grouped first, like strata, and the treatments are then assigned at random inside **every** block. The test of each is the same question: *what happens inside each group, and does every group take part?*
- **E2: did you name the weather but give only one link?** "Warm days bring more customers" earns one mark of two; it says nothing about why warm days also have tables outside. A confounding variable must be associated with **both** variables. Today the word comes back in an experiment, where a variable becomes confounding by travelling with **the treatment a unit got**; and E3's answer, a coin each day, is exactly the fix that Part 2 explains: random assignment.

If you put a **?** on B5, Plan T: "only patients similar to those who replied" was right. Today names what went wrong with it, **voluntary response bias**, and asks which way it pushes the result.

### Warm-up

:::yourturn
Four questions. Answer all four on paper before revealing.

1. In Session 6, the café put up a poster asking members to scan a code and report what they spent. To whom could the results be generalised, and why?
2. A poll of 5,000 people who chose to take part, or a simple random sample of 500 from the same population. Which would you trust to estimate a proportion, and why?
3. St Mary's plans to decide at random which patients get a text reminder. Why at random? Why not let the receptionists choose?
4. What is a placebo, and why would an experiment use one?
:::

:::reveal Reveal — and what your answers mean
| If you said | It means | Do this |
|---|---|---|
| **1:** only members like the ones who replied, because they volunteered | Session 6 held | Carry on; Part 2's *Convenience and voluntary response* names the problem |
| **1:** to all the members, if enough reply | You think size makes a sample trustworthy | Read Part 2's *Bias* subsection slowly, especially "what it does not say". Part 3 is built on this |
| **2:** the random 500, because the 5,000 chose themselves | You have the idea | Carry on; Part 2 adds the word **bias** and its direction |
| **2:** the 5,000, because it is bigger | This is the trap of Part 3 | Read Part 2's *Bias* subsection twice, then let the tool in Part 3 settle it |
| **3:** so the groups are fair, or so the receptionists can't pick | You have the purpose in words | Part 2's *Extraneous variables, and what random assignment is for* gives the exact version |
| **3:** so the results can be generalised | You are mixing up random assignment and random selection | Session 6: random selection generalises, random assignment licenses cause. Then Part 2's cause subsection |
| **4:** a fake treatment, so people don't know whether they got the real one | Sound, informally | Part 2's *Control groups, placebos and the placebo effect* gives the course description's definition, which is a difference between groups, not a feeling |
| **4:** blank | New word | Nothing is assumed; Part 2 starts from the definition |
:::

---

## Part 2 — Theory: bias in samples, and the design of experiments

Every idea the session uses is stated here, each with its code from the course description, the rule, and what the rule does **not** say, which is where most marks are lost. Eighteen subsections: the longest theory part yet, because nearly every term in these two topics is examined by name, and several mean something more precise in the course description than in the prep books.

**Read this part in full before Part 3.** The illustrations are bare on purpose; Parts 3 to 7 apply the same rules to Lincoln High, the Password cards, St Mary's and Riverside. There is nothing to write until the self-check at the end. When a later part says "from Part 2", this is where to look.

**What this part builds on, by name.** From Session 6: *Random selection and how far a generalization reaches (1.10.E.1–4)*; the four random sampling methods (1.11.A.3–6); *Experiment: the researcher imposes treatments (1.10.C.1)*; *Experimental units, factors, levels, treatments and the response (1.10.C.2–4)*; and *Confounding variable in an observational study (1.10.D.5)*. From Session 1: a **parameter** summarises a population and a **statistic** summarises a sample.

### Bias: a systematic error in the sampling method (1.12.A.1)

**Bias** in a sampling method is a **systematic error in the sampling procedure** that results in a statistic being **consistently larger** or **consistently smaller** than the parameter the statistic is used to estimate.

What it does not say. Bias is not the difference between one sample's statistic and the parameter: every random sample misses the parameter by some amount, in one direction or the other, and that is **variation from sample to sample**, not bias. Bias is a property of the **method**, seen over the samples it would produce: they land on the same side, again and again. So a bigger sample from the same method does **not** reduce bias; it reduces the variation, and the estimates cluster more tightly around the wrong value. And "biased" is not a complete answer. The exam wants the mechanism (who is over- or under-represented, and why) and the **direction** (too high or too low), and the unit guide names the missing direction as a common error.

*Illustration:* a method whose samples give 64, 66, 65, 67, 66 when the parameter is 50 has low variability and is biased. A method giving 42, 58, 51, 45, 55 has high variability and is unbiased. The first looks more convincing and is always wrong.

![Four dotplots of 40 values of a statistic from four methods, against a parameter of 50](figures/s07-theory-bias-variability.svg)

*Bias is where a method's estimates centre; variability is how far they spread. The bottom-right method is the dangerous one: consistent, confident and wrong. More data from it would only tighten the cluster around 66.*

### Convenience and voluntary response: samples not chosen by chance (1.12.A.2, 1.12.A.6)

**Nonrandom sampling methods**, for example samples chosen by **convenience** or by **voluntary response**, **introduce potential bias because they do not use random chance to select the individuals** (1.12.A.6). A convenience sample takes the individuals who are easiest to reach. **Voluntary response bias** is a bias that may occur when a sample consists **entirely of volunteers** (1.12.A.2).

What it does not say. It does not say every nonrandom sample gives a wrong answer; it says the answer cannot be trusted, because nothing but luck would make it right. It is Session 6's rule (1.10.E.3) with a name: a sample whose units are deliberately chosen or volunteer themselves is not random, and its results reach only individuals similar to those in it. The direction comes from **who** volunteers or who is convenient: volunteers are usually the people who care most about the question, often those with strong or negative views. A large number of volunteers is still a sample of volunteers.

*Illustration:* a population of 1,000, of whom 200 hold a strong view. A notice invites replies; 150 of the 200 reply and 50 of the other 800. The replies are 150 ÷ 200 = 75% strong view, against 20% in the population: too high, because holding the view is what makes people reply.

### Undercoverage bias: part of the population left out (1.12.A.3)

**Undercoverage bias** may occur when the sampling method **fails to include part of the population**, or a part of the population is **less likely to be selected** based on the sampling method.

What it does not say. It is about who **could be selected**, before anyone is asked anything. It can happen inside a random method: a simple random sample from an out-of-date list still cannot pick anyone missing from the list. It does not need the part to be missed completely; *less likely* is enough. And it causes bias only in so far as the part left out differs, on the variable of interest, from the part included; the direction follows from how it differs.

*Illustration:* a population of 1,000, of whom 300 have property *P*. A method that can reach only the 700 who use one entrance, where 70 of the 700 have *P*, estimates the proportion near 70 ÷ 700 = 0.10, against the parameter 0.30. Too low, because most of the individuals with *P* use the other entrance.

### Nonresponse bias: chosen but not answering (1.12.A.4)

**Nonresponse bias** may occur because of a **failure to obtain responses from some individuals chosen to be sampled**. The respondents and nonrespondents could **differ significantly in ways that are important for the study**.

What it does not say. The individuals were **chosen**, often at random, and then did not respond; that is what separates it from voluntary response, where nobody was chosen, and from undercoverage, where some could never have been chosen. A random sample with nonresponse is no longer protected by its randomness, because the data are the respondents, and they chose themselves out of the chosen. But nonresponse alone is not bias: if the nonrespondents are like the respondents on the variable of interest, the estimate is not pushed either way. The claim needs the second sentence of the definition, a reason the two groups differ, and from it the direction.

*Illustration:* 100 chosen at random; 40 have property *P*. Of the 40, 16 respond; of the 60 without *P*, 54 respond. The respondents give 16 ÷ 70 = 0.23, against 0.40 among all 100: too low, because those with *P* responded less. Had both groups responded at 90%, there would be nonresponse and no bias.

### Response bias: answers pushed one way, including question wording (1.12.A.5)

**Response bias** may occur when **responses to a survey or measurements of observational units tend to differ from the "true" value in one direction**. Examples include questions that are **confusing or leading** (**question wording bias**) and **self-reported responses**.

What it does not say. It is about the **answers**, not who gives them: the right individuals can be chosen at random, every one can respond, and the data can still be biased. It covers measurements as well as questions: a scale that always reads 0.5 kg heavy gives response bias. "In one direction" is the point, again: honest people making random slips in both directions are variation, not bias. Self-reports lean the way people prefer to see themselves: more exercise, less screen time.

*Illustration:* "Most experts agree that X is good. Do you support X?" invites *yes*: the wording leans toward support, so the proportion supporting X comes out too high. "Do you support X?" leans neither way.

### Telling the biases apart, and saying which way they push (1.12.A.2–6)

The four named biases are told apart by **where in the process** the error enters:

| Where it goes wrong | The bias | The question to ask |
|---|---|---|
| Who **can** be chosen | **undercoverage** | Is part of the population left out, or less likely to be chosen? |
| Who **chooses themselves** in | **voluntary response** (and convenience: who the sampler chooses because they are easy) | Did a random mechanism select the individuals at all? |
| Who, having been chosen, **drops out** | **nonresponse** | Were individuals chosen who did not respond, and do they differ? |
| What the respondents **say**, or what a measurement **reads** | **response** (question wording, self-report) | Would the answers lean one way even from the right people? |

What it does not say. One study can have several: a notice on a single door is convenience, voluntary response and undercoverage at once. Naming one correctly, with its mechanism and direction, earns the marks; listing all four without either earns none. And a sentence of the form **"the estimate will be too high/low because [group] is over/under-represented, and [group] tends to [value of the variable]"** is the whole answer.

*Illustration:* "Selected by random number; 30% did not reply" is nonresponse, not voluntary response: they were chosen first. "Anyone could reply" is voluntary response: nobody was chosen.

### The four elements of a well-designed experiment (1.13.A.1)

A well-designed experiment should include:

1. **Comparisons of at least two treatment groups**, one of which could be a control group (1.13.A.1.i);
2. **Random assignment** of treatments to experimental units (1.13.A.1.ii);
3. **Replication** (1.13.A.1.iii);
4. **Direct control** of potential extraneous sources of variation in the response (1.13.A.1.iv).

What it does not say. It does not say an experiment without all four is not an experiment: Session 6's café that printed a larger menu for one week imposed a treatment and was an experiment, a poorly designed one, because it had no comparison. The four are **elements of good design**, each doing a different job, and the subsections below give each job. And *control* here is **direct control**, keeping extraneous variables the same; it is not the same thing as a control group, which belongs to the first element.

*Illustration:* 40 units, two treatments A and B, 20 of each chosen by a random number generator, every unit measured under the same conditions. That has comparison (A against B), random assignment, replication (20 per treatment) and direct control (the same conditions).

### Control groups, placebos and the placebo effect (1.13.A.2–3)

A **control group** is a collection of experimental units **created for comparison**. A control group may be given a **treatment different from the treatment of interest**, to determine if the treatment of interest has an effect; for example a treatment with an **inactive substance, a placebo**, may be given (1.13.A.2).

The **placebo effect** is **the difference between the average response to a placebo and the average response to no treatment** (1.13.A.3).

:::formula
placebo effect = (average response of the placebo group) − (average response of the no-treatment group)
:::

What it does not say. A control group need not receive nothing: it may receive the usual treatment, or a placebo, or a different version of the treatment. It exists so that the treatment of interest has something to be compared with. The placebo effect is not "people feel better when they think they are treated", as the prep books put it; it is a **measured difference between two groups**, so an experiment with a treatment group and a placebo group but no no-treatment group cannot measure it. What a placebo group *can* do is give the comparison with the treatment of interest a fair baseline: both groups then believe they may be treated.

*Illustration:* three groups' average responses are 12 (active treatment), 9 (placebo) and 6 (no treatment). The placebo effect is 9 − 6 = 3. The treatment's effect beyond the placebo is 12 − 9 = 3.

### Single-blind and double-blind experiments (1.13.A.4–5)

In a **single-blind** (also called **single-masked**) experiment, the **participants do not know which treatment they are receiving**, but members of the research team who interact with them do know, **or vice versa** (1.13.A.4).

In a **double-blind** (also called **double-masked**) experiment, **neither** the participants **nor** the members of the research team who interact with them know which treatment each participant is receiving (1.13.A.5).

What it does not say. "Vice versa" matters: when participants must know their treatment (they can see whether they received a text, or which exercise they did), keeping the staff who measure or interact with them unaware is still single-blind. Keeping participants or staff blind is not one of the four elements listed in 1.13.A.1. It serves the same purpose as direct control: it stops one extraneous source of variation, knowing which treatment was given, from differing between the groups and changing how participants respond or how staff measure. And it is about the people who **interact with the participants**; the statistician who prepared the random assignment list will always know.

*Illustration:* a treatment and a placebo, identical in appearance, in bottles labelled 1 and 2 by someone who then takes no part. If neither the participants nor the staff who measure them know what 1 and 2 mean, the experiment is double-blind.

### Extraneous variables, and what random assignment is for (1.13.A.6–7)

An **extraneous source of variation**, also called an **extraneous variable**, is a variable that is **known (or believed) to affect the response** but is **not an explanatory variable being studied** (1.13.A.6).

The **purpose of random assignment** is to **create treatment groups that are as similar as possible with respect to extraneous sources of variation**. If random assignment is successful, the **respective distributions of each extraneous variable will be approximately the same for all the treatment groups** (1.13.A.7).

What it does not say. Random assignment does not make the groups identical: by chance they differ a little, and a larger number of units makes that difference smaller. It balances **every** extraneous variable at once, including the ones nobody thought to measure, which is what no deliberate allocation can do. And it has nothing to do with how the units were **obtained**: random assignment of volunteers is still random assignment, and it gives no licence to generalise beyond people like the volunteers (Session 6: random selection does that).

*Illustration:* 20 units, 10 of them high on an extraneous variable *w*. Split at random into two groups of 10: the number of high-*w* units in the first group is usually 4, 5 or 6 (in about 82% of random splits), and never all 10 unless by an extraordinary chance (1 split in 184,756). Split by letting the units choose, and all 10 high-*w* units may choose the same group.

### Confounding in an experiment (1.13.A.8)

A **confounding variable in an experiment** is a variable that is **related to the explanatory variable** in such a way that it is **difficult to determine which variable, explanatory or confounding, is influencing the change in the response variable**. However, **in a well-designed experiment, the potential for confounding variables is reduced**.

What it does not say. Recall Session 6's version for an observational study (1.10.D.5): associated with both the explanatory and the response variable. In an experiment the explanatory variable is imposed, so a variable becomes confounding when it **travels with the treatment**: every unit that got treatment A also got something else. That happens when the researcher assigns treatments by some rule other than chance, such as by day, by location or by who seems suitable. "Reduced", not "removed": random assignment makes confounding unlikely, not impossible.

*Illustration:* treatment A is given every morning and treatment B every afternoon. If the response differs, time of day and treatment cannot be separated: time of day is confounded with the treatment.

### Replication and direct control (1.13.A.9–10)

**Replication** within an experiment means **more than one experimental unit is assigned to each treatment** (1.13.A.9).

**Direct control** in an experiment means **keeping the settings of certain potential extraneous sources of variation in the response variable the same** from experimental unit to experimental unit (1.13.A.10).

What it does not say. Replication is not repeating the whole experiment another time (Barron's makes the same point); it is having several units in each treatment group, so that a difference between groups is not the difference between two individuals. Direct control does not balance an extraneous variable, as random assignment does; it removes its variation altogether by fixing it, and it can only be applied to variables the researcher can hold fixed. The three jobs are different: direct control fixes the variables it can, random assignment balances the rest, and replication makes the chance differences between groups small.

*Illustration:* with one unit per treatment, a difference of 5 could be the treatment or the two units. With 20 per treatment, all measured at the same temperature, a difference of 5 in the group averages is far harder to put down to the units, and cannot be put down to temperature.

### The completely randomized design (1.13.B.1)

In a **completely randomized design**, **treatments are assigned to experimental units completely at random**. Often the number of experimental units assigned to each treatment will be the same, but the **sample sizes in each treatment do not have to be the same**.

What it does not say. "Completely at random" means every unit is assigned by the random mechanism with no grouping first: the simplest design, and the default when there is no strong extraneous variable to block on. Describing it on the exam means saying **how**: number the units, use a random number generator to choose which units receive each treatment, and give the rest the other.

*Illustration:* number 30 units 1 to 30; a random number generator gives 15 different numbers, and those units receive A; the other 15 receive B.

### The randomized block design, and why to block (1.13.B.2–3)

A **blocking variable** is a **source of extraneous variation** in the response variable. In a **randomized block design**, the experimental units are **first grouped according to similar values of a blocking variable**. These groups are called **blocks**. Units within the same block are **homogeneous** with respect to the blocking variable. After the blocks are formed, the treatments are **randomly assigned to experimental units within each block** so that **all treatments occur within every block** (1.13.B.2).

The **purpose of blocking** is to **separate the variation in the response caused by the blocking variable from the rest of the extraneous variation** in the response. Blocking allows for **more precise comparisons** of the response across the treatments. Within a block, the treatments can be compared without having to worry about variation in the response caused by changes in the blocking variable (1.13.B.3).

What it does not say. The blocks are **not** formed at random: they are formed deliberately from the blocking variable, and the randomness goes **inside** each block. It is the experimental version of Session 6's stratified sample: groups that are alike inside, and every group used. Blocking does not replace random assignment, and it is not what makes a cause-and-effect conclusion possible; that is random assignment's job (1.13.D.1). Blocking's job is **precision**: the comparison is not blurred by a variable known to matter. A variable is worth blocking on only if it is known before the experiment and is related to the response.

*Illustration:* 20 units, of which 12 are type 1 and 8 are type 2, and type affects the response. Block by type; within the 12, a random number generator gives 6 treatment A and 6 treatment B; within the 8, 4 and 4. Compare A and B within each block.

### The matched pairs design (1.13.B.4)

A **matched pairs design** is a **randomized block design with only two treatments**. Experimental units are **arranged in pairs by matching on one or more extraneous sources of variation** in the response variable. Each pair receives both treatments by **randomly assigning one treatment to one member of the pair** and the other treatment to the second member. **Alternatively, each experimental unit may get both treatments while the order of the treatments is randomized**.

What it does not say. The pairs are blocks of size 2, so everything about blocks applies: formed deliberately, random inside. The random step is either **which member** gets which treatment or **which order** a single unit gets them in; a design where every unit gets A first and B second is not randomized, and the order is confounded with the treatment. The comparison is made **within each pair**, which removes the variation between pairs.

![Three experimental designs for 20 units and two treatments: completely randomized, randomized block, and matched pairs](figures/s07-theory-designs.svg)

*Where the chance goes in each design. In all three, a random mechanism assigns the treatments; the block and pair designs first group the units deliberately, so that each comparison is made between units that are alike.*

*Illustration:* 10 units in 5 pairs matched on size. For each pair, a coin decides which unit gets A; the other gets B. Or: each of 10 units gets both, with a coin deciding which comes first.

### Choosing between designs (1.13.C.1)

**One experimental design may be more appropriate than another** based on **the goals of the investigative study, the characteristics of the population, and the sample and variables involved**.

What it does not say. No design is best in general. A justification names the feature of **this** study that makes one design better, and connects it to the design's job, exactly as Session 6's justification of a sampling method did (1.11.B.1). The usual reason to prefer a block or matched pairs design is an extraneous variable, known in advance, that is strongly related to the response: blocking on it gives a more precise comparison. The usual reason to prefer a completely randomized design is that there is no such variable, or pairing is impractical. "Blocking is better" earns nothing on its own.

| Design | Choose it when | Its advantage |
|---|---|---|
| Completely randomized | no strong extraneous variable is known in advance | simplest; random assignment balances everything |
| Randomized block | a known extraneous variable is strongly related to the response | separates that variable's variation, so the comparison is more precise |
| Matched pairs | two treatments, and units can be matched closely, or one unit can take both | removes the variation between pairs; often the most precise |

*Illustration:* if the response depends strongly on a variable *v* that is known for every unit before the experiment, block on *v* and say so: "because *v* is strongly related to the response, blocking on *v* separates its variation from the comparison of the treatments."

### Cause and effect from random assignment, and statistical significance (1.13.D.1)

**Using random assignment** of treatments to experimental units **allows for cause-and-effect conclusions** between the explanatory and the response variables **because the potential for confounding variables is reduced** (1.13.D.1).

The course description's unit guide completes it: *for data collected using well-designed experiments, **statistically significant** differences between or among experimental treatment groups are evidence that the treatments caused the effect.* A difference is **statistically significant** when it is too large to be explained plausibly by the chance variation that random assignment itself creates. Deciding that is a calculation, formally a p-value compared with a significance level (3.7.B.1), and Sessions 15 and 16 teach it. Today the student is told whether a difference is statistically significant, and decides what may be concluded from it.

What it does not say. Random assignment is **the** element to cite for cause; the unit guide says a complete answer "cites the random assignment of treatments and does not refer to other irrelevant elements". A blind design, blocking, replication and a control group all improve an experiment, but none of them is the reason a cause can be claimed. A difference that is **not** statistically significant is not evidence that the treatment does nothing; it means the experiment could not tell the treatment's effect from chance. And cause says nothing about **whom** the conclusion reaches; that is the next subsection.

*Illustration:* treatments A and B assigned at random to 200 units; A's average response is higher, and the difference is statistically significant. Conclusion: A causes a higher response than B, for units like these. Had the difference not been statistically significant: the experiment gives no convincing evidence of a difference, which is not the same as showing there is none.

### Experiments on volunteers: how far the conclusion reaches (1.13.D.2)

Depending on the experimental unit, it **may be unethical or difficult to randomly select experimental units** to participate in an experiment. In that case, the study's experimental units are **obtained from volunteers** and will **represent the population of experimental units similar to those who participated** in the study.

What it does not say. It is Session 6's rule (1.10.E.2–4) applied to experiments: random **selection** decides how far the result reaches, random **assignment** decides whether it can be about cause, and a study can have one without the other. Most experiments on people use volunteers, so most licence cause, for people similar to the volunteers. It does not make the volunteers' result wrong; it limits whom it is about.

| Units selected at random? | Treatments assigned at random? | What the study may conclude |
|---|---|---|
| Yes | Yes | cause and effect, for the whole population sampled |
| No (volunteers, or everyone available) | Yes | cause and effect, for units similar to those in the study |
| Yes | No (observational) | an association, for the whole population sampled |
| No | No | an association, for units similar to those in the study |

*Illustration:* 60 volunteers, treatments assigned by random number, a statistically significant difference: the treatment caused the difference, for people similar to the 60 volunteers.

### Self-check on the theory

Answer each on paper, then open its reveal. If one goes wrong, reread that subsection's "what it does not say" paragraph before Part 3: the rest of the session leans on every one of them.

**Check 1.** A method's estimates are 0.52, 0.49, 0.51, 0.50 and 0.53, and the parameter is 0.40. Is the method biased? What would a larger sample from the same method do?

:::reveal Reveal — check 1
**Biased**: consistently too high. A larger sample would cluster the estimates more tightly, **around the wrong value**. It reduces variation, not bias.
:::

**Check 2.** A random sample of 200 is chosen and 60 never reply. Which bias might that be, and what must be true for it to push the estimate?

:::reveal Reveal — check 2
**Nonresponse bias**: they were chosen, then did not respond. It pushes the estimate only if the 60 **differ** from the 140 on the variable being measured.
:::

**Check 3.** A survey can reach only people who use one particular website. Which bias?

:::reveal Reveal — check 3
**Undercoverage bias**: part of the population cannot be selected at all.
:::

**Check 4.** Name the four elements of a well-designed experiment.

:::reveal Reveal — check 4
**Comparison** of at least two treatment groups, **random assignment**, **replication**, and **direct control** of extraneous sources of variation.
:::

**Check 5.** An experiment has a treatment group and a placebo group. Can it measure the placebo effect?

:::reveal Reveal — check 5
**No.** The placebo effect is the average response to a placebo **minus the average response to no treatment**, so it needs a no-treatment group.
:::

**Check 6.** The participants know which treatment they got, but the nurse who measures them does not. What is that called?

:::reveal Reveal — check 6
**Single-blind**: the "or vice versa" case of the definition.
:::

**Check 7.** In a randomized block design, what is random, and what is not?

:::reveal Reveal — check 7
The **blocks** are formed from the blocking variable, **not** at random. The **treatments** are assigned at random **within every block**.
:::

**Check 8.** Which element of an experiment do you cite to justify a cause-and-effect conclusion?

:::reveal Reveal — check 8
**Random assignment** of treatments, and only that. A blind design, blocking, replication and a control group improve an experiment, but none of them is the reason a cause can be claimed.
:::

---

## Part 3 — Lincoln High's travel survey against a known parameter

Lincoln High from Sessions 1 to 6, with its **1,842 students** in three home areas. In Session 1 a randomly chosen 120 students were asked how they travel, and 43 came by bus: a statistic of 43 ÷ 120 = 0.358. The parameter, the proportion of **all** 1,842 who travel by bus, was unknown. Now it is known. The county's school bus scheme requires every student who travels to school by bus to hold a bus pass, and the office has the full list of passes: a **census**.

| Home area | Students | Bus-pass holders |
|---|---|---|
| Town, within 3 km | 846 | 85 |
| Suburbs, 3 to 10 km | 702 | 316 |
| Villages, beyond 10 km | 294 | 250 |
| **Total** | **1,842** | **651** |

The parameter is 651 ÷ 1,842 = **0.353**. The parameter is almost never known, and that is what makes this part useful: every sampling method's answer can be checked against it.

### Work out the four estimates

Before the bus-pass list existed, staff had tried four ways to estimate the proportion.

| Method | How the students were chosen | In the data | By bus |
|---|---|---|---|
| **A** (Session 1) | A random number generator chose 120 from the roll | 120 | 43 |
| **E** (Session 6) | The first 120 students through the **main gate** on a Monday; the school buses drop at the **side bus bay** | 120 | 12 |
| **F** | A link in the parents' newsletter: *"We are reviewing the bus timetable. Tell us how your child travels."* The first 212 replies | 212 | 128 |
| **G** | A random number generator chose 120; the office **phoned their homes at 4:30 pm** on a Tuesday; 87 answered | 87 | 17 |

:::yourturn
1. Work out each method's estimate of the proportion who travel by bus, and say whether it is too high or too low.
2. Plan A is slightly too high. Is that bias?
3. Sketch the four estimates on a number line from 0 to 0.7, with the parameter marked.
:::

:::reveal Reveal — the four estimates
**1.** A: 43 ÷ 120 = **0.358**, slightly above. E: 12 ÷ 120 = **0.100**, too low. F: 128 ÷ 212 = **0.604**, too high. G: 17 ÷ 87 = **0.195**, too low.

**2. No.** One random sample misses the parameter by chance, and the next would miss the other way; Plan A misses by 0.005. Bias is a method that misses **in the same direction every time** (Part 2, *Bias*).

**3.**

![Four estimates of the proportion of Lincoln High students who travel by bus, against the parameter 0.353](figures/s07-lincoln-estimates.svg)

*Only the random sample lands near the parameter. The other three miss by 0.16 to 0.25, and each misses in the direction its method pushes.*
:::

### The main-gate sample

:::yourturn
1. Plan E: name the bias, and say which way it pushes the estimate and why.
2. Session 6 said Plan E's results reach only students similar to those who arrive first at the main gate. What does today add?
:::

:::reveal Reveal — convenience and undercoverage
**1.** **Undercoverage bias**: the school-bus students arrive at the side bus bay, so most of them cannot be in a sample taken at the main gate. **Too low**, because the part of the population left out is mostly bus users. It is also a **convenience** sample: the first students to arrive where the deputy stood.

"It's biased because it's not random" is true and earns nothing on its own. The answer is **who** is missing and **which way** that pushes the estimate.

**2.** Session 6 said how far the result reaches. Today says what is wrong with it, and in which direction.

*The main-gate sample has undercoverage bias: students who arrive by school bus use the side bus bay and are unlikely to be selected, so the proportion who travel by bus will be too low.*
:::

### The newsletter link: is 212 better than 120?

This is the trap of Part 3.

:::yourturn
1. Plan F has 212 students, nearly twice Plan A's 120. Is it the better estimate? Name its bias and direction.
2. What would it take to fix Plan F?
:::

:::reveal Reveal — voluntary response, and why 212 replies do not help
**1. No.** The 212 chose themselves. The newsletter said the bus timetable was under review, so the parents who reply are those with a stake in the buses: bus users are over-represented. **Voluntary response bias**, and the estimate is **too high**.

More data from a method that pushes up only pushes up with more confidence. The tool at the end of this part shows it.

**2.** Not more replies. Choose the students by a **random mechanism**, then chase the replies.

*The newsletter replies have voluntary response bias: the parents who choose to reply are those who care about the bus timetable, mostly parents of bus users, so the estimate is too high. More replies would not fix it.*
:::

### The 4:30 phone calls

:::yourturn
1. Plan G was chosen at random, like Plan A. Why is it so far off? Name the bias and its direction.
2. Is it voluntary response bias, since the students chose whether to answer?
3. Suppose the bus students answered as often as everyone else. Would 33 missing students still bias the result?
4. Write the answer an examiner wants, in two or three sentences.
:::

:::reveal Reveal — nonresponse from a random sample
**1.** 33 of the 120 chosen did not answer. At 4:30 many bus students are still on the bus, especially from the Villages, so the students who answered are mostly not bus users. **Nonresponse bias**, **too low**.

**2. No.** They were **chosen first**, by random number. Chosen and then lost is nonresponse; never chosen at all is voluntary response.

**3. No.** Nonresponse biases the estimate only when the nonrespondents **differ** from the respondents on the variable of interest.

**4.** The course description's unit guide names the error to avoid: students "forget to support claims about nonresponse bias with evidence indicating whether the sample result is likely to be too high or too low." A model answer:

> *"Plan G has nonresponse bias. Of the 120 students chosen at random, 33 did not answer the 4:30 pm call. Students who travel by bus, especially from the Villages, are likely to be still travelling at 4:30, so bus users are under-represented among those who answered, and the proportion who travel by bus will be too low."*
:::

### Two wordings of one question

The school council wanted a second answer from the survey: should the school keep the **late bus**, which leaves at 5:15 pm after clubs? It chose a new random sample of 120 students and, to see whether the wording mattered, gave a random half one version and the other half the other.

| Version | Wording | Answered yes |
|---|---|---|
| 1 | *"Do you agree that the school should keep the late bus, so that students who live far away can stay for clubs and sport?"* | 49 of 60 |
| 2 | *"Should the school keep paying £38,000 a year for a late bus that most students never use?"* | 17 of 60 |

:::yourturn
1. Work out each percentage. The students were chosen at random and every one answered: where can bias come from?
2. Which version gives the true level of support? Write a neutral version.
3. What kind of study did the council run, splitting the sample into two random halves?
:::

:::reveal Reveal — response bias from question wording
**1.** Version 1: 49 ÷ 60 = **81.7%**. Version 2: 17 ÷ 60 = **28.3%**. The bias comes from **the question**: version 1 leads toward yes, version 2 toward no. The same kind of students gave answers 53.3 percentage points apart. That is **response bias** from question wording (Part 2).

**2. Neither.** Both lead. Neutral: *"Should the school keep the late bus? Yes or no."*

**3.** An **experiment**: it assigned the wording, a treatment, at random. That is why it can say the wording caused the difference.

**The four problems, in one table:**

| Plan | Bias | Direction |
|---|---|---|
| E, main gate | undercoverage (and convenience) | too low |
| F, newsletter | voluntary response | too high |
| G, phone at 4:30 | nonresponse | too low |
| Late-bus question | response bias, question wording | whichever way the wording leads |
:::

### The Sampling Bias tool

:::sim sampling-bias | Sampling Bias | 1500
A simulated Lincoln High with the same 1,842 students and 651 bus users, so the parameter, 0.353, is known. The four buttons are Plans A, E, F and G, and the tool opens with one sample from each at n = 120. Press **Draw 100 samples** for each method and decide which rows are biased before you read the table. Then change the sample size to **480** and do it again. Last, choose the 4:30 phone calls and set the bus users' answer rate to **90%, like everyone else**.
:::

:::yourturn
After using the tool, answer on paper.

1. At n = 120, which methods are biased, and how can you tell from the dots?
2. What happened to every row when you went from 120 to 480? So what does a bigger sample fix, and what does it not?
3. What happened to the phone calls when bus users answered as often as everyone else?
:::

:::reveal Reveal — what the tool shows
The tool's own tests, over 4,000 samples of each kind:

| Method | Centre of the estimates at n = 120 | Their SD at n = 30 | at n = 120 | at n = 480 |
|---|---|---|---|---|
| Simple random sample | 0.353, the parameter | 0.086 | 0.042 | 0.019 |
| First through the main gate | 0.099: too low by 0.255 | 0.054 | 0.026 | 0.011 |
| Newsletter link replies | 0.612: too high by 0.259 (0.580 at n = 480) | 0.087 | 0.043 | 0.019 |
| Phoned at 4:30 pm | 0.195: too low by 0.158 | 0.085 | 0.041 | 0.020 |
| Phoned at 4:30, equal answer rates | 0.353, the parameter | 0.092 | 0.045 | 0.020 |

**1.** The main gate, the newsletter and the phone calls. Their dots all sit **on one side** of the dashed line; the simple random samples fall on **both** sides.

**2.** Every row got **narrower**: the SD roughly halved. The random samples closed in on 0.353; the biased ones closed in on their own **wrong** values. A bigger sample reduces the variation from sample to sample. It does nothing about bias.

**3.** The bias **vanished**, although about one chosen student in ten still did not answer. Nonresponse biases the result only when the nonrespondents differ.
:::

---

## Part 4 — Password, on your own

The course description's activity for topics 1.11–1.12 is a password-style game with nine terms: **simple random sample, stratified random sample, cluster random sample, systematic random sample, bias, voluntary response bias, undercoverage bias, nonresponse bias and response bias**. In class, one partner gives clues and the other names the term. On your own, you play **both** roles: first you write the clues, then you name the terms from someone else's.

**The rule for every clue:** it may not contain any word of the term itself. So *random*, *sample* and *bias* are banned on every card they appear on, and the clue must describe **how the individuals are chosen** or **where the error enters**. A term scores if a clue names it at the first attempt.

### Write a clue for each of the nine terms

:::yourturn
For each of the nine terms, write a clue of one sentence that obeys the rule. Keep each one short enough to say aloud in ten seconds.
:::

:::reveal Reveal — clues that score first time
| Term | A clue that scores first time |
|---|---|
| Simple random sample | "Number everyone and let a generator pick; every possible group of that size is equally likely." |
| Stratified random sample | "Split everyone into groups that are alike inside, then take some from every group." |
| Cluster random sample | "Split everyone into groups that each look like the whole, pick a few groups by chance, and take everyone in them." |
| Systematic random sample | "A starting point chosen by chance, then every k-th one on the list." |
| Bias | "The method lands on the same side of the truth, sample after sample, too high or too low." |
| Voluntary response bias | "Nobody is picked; people choose to take part, usually the ones who care most." |
| Undercoverage bias | "Part of the population could never be picked, or is less likely to be." |
| Nonresponse bias | "They were picked, but some never answered, and they differ from those who did." |
| Response bias | "The right people answer, but the answers lean one way: a leading question, or people describing themselves." |

Check your own against two things. Does it break the rule? And could it describe a **different** term? "People didn't take part" fits both nonresponse and voluntary response; "some people were missed" fits undercoverage and nonresponse. Those are the clues a partner guesses wrong, and they are the confusions the exam uses.
:::

### Name the term from each clue

:::yourturn
Name the term for each clue. Score one for each you get without looking back.

1. "Everyone in a few whole groups, and nobody from the rest."
2. "They were chosen, but a third of them never sent the form back."
3. "The question began 'Most people agree that…'."
4. "Start somewhere by chance, then every 25th."
5. "Anyone who wanted to could phone in."
6. "Some from every group, and the groups are alike inside."
7. "The list we chose from had nobody without a landline."
8. "Every group of 50 had the same chance of being the one chosen."
9. "Sample after sample, the estimate came out above the true value."
:::

:::reveal Reveal — the nine clues named
1. Cluster random sample. 2. Nonresponse bias. 3. Response bias (question wording). 4. Systematic random sample. 5. Voluntary response bias. 6. Stratified random sample. 7. Undercoverage bias. 8. Simple random sample. 9. Bias.

If you mixed up 2 and 5, or 2 and 7, reread Part 2's *Telling the biases apart*: the question is **where** the error enters, at who can be chosen, who chooses themselves in, or who drops out after being chosen.
:::

### Name the term from the study

:::yourturn
The speed round. For each study, name the term (a sampling method or a bias) within ten seconds, and for a bias say which way it pushes the result.

1. The library puts a questionnaire on the front page of its website and uses the 410 that are filled in.
2. Oakfield chooses 60 students by random number to ask how many days of school they missed last term; 11 are absent on survey day and are never asked.
3. The café asks its customers about the menu, between 7 and 9 am only.
4. Riverside asks patients, in front of the nurse who treated them, how good their nurse was.
5. St Mary's chooses 3 of its 40 wards at random and surveys every patient in them.
6. Lincoln High chooses a random start from 1 to 20 on the roll, then every 20th student.
:::

:::reveal Reveal — the speed round
| Study | Term |
|---|---|
| 1 | **Voluntary response bias**: nobody was chosen |
| 2 | **Nonresponse bias**: chosen, then not reached; the absent students are likely to miss more days, so the estimate is **too low** |
| 3 | **Undercoverage bias** (and convenience): afternoon customers cannot be chosen |
| 4 | **Response bias**: the answers will lean favourable, **too high** |
| 5 | **Cluster random sample** |
| 6 | **Systematic random sample** |

Your score out of 24: one for each of your nine clues that obeys the rule and fits only its own term, one for each of the nine clues you named, and one for each of the six studies. Nineteen or more is the standard. Below that, reread the Part 2 subsections of the terms you missed before Part 5.
:::

---

## Part 5 — St Mary's reminder experiment

St Mary's outpatient clinics, from Session 6. The records of 400 of last year's 9,600 outpatients showed that patients who signed up for text reminders missed fewer appointments (7.5% against 20.0%), but the patients had chosen whether to sign up, and **booking method** was a confounding variable: 70.0% of self-booked patients signed up against 10.0% of hospital-booked patients, and 5.0% of self-booked patients missed against 25.0%. Session 6 ended by sketching the experiment that could settle it. Today it is designed, run and concluded.

Next month St Mary's clinics have **800 outpatients** with appointments: **400 self-booked online** and **400 booked by the hospital**. Until now the hospital has not sent reminders to patients who did not sign up, so not sending one is what these patients would otherwise have received.

The trap of Part 5: **each element of a good experiment does a different job, and only one of them, random assignment, is what licenses a conclusion about cause.**

### The four elements, applied

:::yourturn
1. Name the experimental units, the treatments and the response.
2. Where are the four elements of a well-designed experiment in this plan?
3. Name three things St Mary's should keep the same for every patient.
4. The manager suggests sending the no-text group a text about the hospital car park instead. Would that still be a control group? What would comparing it with the reminder group tell you?
:::

:::reveal Reveal — the elements in the reminder experiment
**1.** Units: the 800 patients (their appointments). Treatments: a text reminder the day before, or no text. Response: whether the patient misses the appointment.

**2.** **Comparison**: text against no text; the no-text group is the **control group**. **Random assignment**: a random number generator decides who gets a text. **Replication**: hundreds of patients in each group. **Direct control**: everything else kept the same.

**3.** For example: the wording of the text; when it is sent (10 am the day before); the rule for "missed" (not arrived within 15 minutes of the appointment time); the same month and the same clinics for both groups.

**4. Yes.** A control group may receive a treatment different from the treatment of interest (Part 2). Comparing it with the reminder group would show the effect of the reminder's **content**, beyond the mere fact of receiving a text from the hospital. To measure the effect of the car-park text itself, the way the placebo effect is measured, you would need a third group that gets no text.

On ethics, because skill 2.B says *ethically*: the no-text patients receive what every patient who had not signed up received before, so nobody gets less than usual care, and the result decides whether everyone gets a reminder in future.
:::

### The receptionist's easier plan

> *"Let's send texts to everyone with an appointment on Monday, Tuesday or Wednesday, and none on Thursday or Friday. Much simpler to run."*

:::yourturn
1. What is wrong with the receptionist's plan? Use the right term.
2. It is still an experiment. Doesn't that mean it shows cause?
3. How does random assignment fix it?
:::

:::reveal Reveal — clinic day as a confounding variable
**1.** The **day travels with the treatment**. If Thursday and Friday patients miss more anyway, because different clinics run on those days or Friday afternoons are harder to attend, the difference would be the day, not the text, and nobody could tell which. The day is a **confounding variable in an experiment**: related to the explanatory variable, so it is difficult to tell which one changed the response (1.13.A.8).

**2.** It is an experiment, but a badly designed one. What decided who got a text was the day of the week, not chance, and that is exactly how confounding gets into an experiment.

**3.** A random number generator decides for each patient, so every day, every clinic and every kind of patient ends up in both groups in about the same proportions (1.13.A.7).
:::

### Completely randomized, or blocked by booking method?

Two plans are on the table:

- **Plan 1.** Number the 800 patients; a random number generator chooses 400 different numbers, and those patients get a text; the other 400 do not.
- **Plan 2.** Form two groups by booking method: the 400 self-booked and the 400 hospital-booked. Within each, a random number generator chooses 200 to get a text; the other 200 do not.

:::yourturn
1. Name each design, and say what is random in each.
2. Draw Plan 2 as a diagram, from the 800 patients to the comparison.
3. In Plan 1, will the text group contain exactly 200 self-booked patients? Roughly what percentage of it would you expect to be self-booked, and how far might it stray?
:::

:::reveal Reveal — the two designs, drawn and compared
**1.** Plan 1: **completely randomized design**; all 800 are assigned at random. Plan 2: **randomized block design**, with booking method as the blocking variable; the blocks are formed from booking method, **not** at random, and the texts are assigned at random **inside each block**.

**2.**

![St Mary's reminder experiment as a randomized block design, blocked by booking method](figures/s07-stmarys-block-design.svg)

*The blocks are formed deliberately from booking method; the random number generator works inside each block.*

**3. Not exactly, but close**: about 50%. Random assignment makes the groups similar, not identical.

![Percentage of the text group who self-booked, in 1,000 random assignments of the 800 patients, against 87.5% when patients chose](figures/s07-stmarys-balance.svg)

*In 1,000 completely randomized assignments of the 800 patients, the text group was between 44.5% and 55.0% self-booked, and 996 of the 1,000 were between 45% and 55%. When patients chose for themselves, in Session 6's records, 87.5% of those who signed up had self-booked (140 of 160). The block design fixes it at exactly 50%.*

That picture is the answer to Session 6's confounding problem: letting patients choose put 87.5% of self-booked patients in the reminder group; random assignment puts about half.
:::

:::yourturn
Plan 1 already balances booking method, roughly. Write a justification, of two or three sentences, for St Mary's preferring Plan 2.
:::

:::reveal Reveal — justifying the block design
> *"A randomized block design is more appropriate. Booking method is known for every patient in advance and is strongly associated with missing appointments (25.0% of hospital-booked patients missed last year, against 5.0% of self-booked). Blocking by booking method separates that variation from the comparison of the two treatments, so text and no text are compared among similar patients and the comparison is more precise."*

"Because it's more random" is wrong: both plans assign every patient by random number. Plan 2 is more **precise**, not more random. And "blocking is better" on its own earns nothing: name the feature of this study, and connect it to what blocking does (Part 2, *Choosing between designs*).
:::

### Does blocking license the cause?

:::yourturn
1. The manager says: *"Because we blocked by booking method, we have controlled the confounding variable, so we can say reminders cause fewer missed appointments."* Is that the right reason?
2. Suppose St Mary's formed the blocks and then let each block's clinic manager choose which 200 patients got texts. What would be lost?
:::

:::reveal Reveal — random assignment inside every block
**1. No.** Blocking makes the comparison more precise for the **one** variable blocked on. What allows a cause-and-effect conclusion is **random assignment**: it balances booking method **and** every other extraneous variable, including ones nobody measured, such as a patient's age, distance from the hospital or how organised they are.

**2.** Everything that licenses cause. A manager might text the patients most likely to forget, or least likely. The blocks would be there and the random assignment would not.

*Direct control fixes what it can. Blocking separates one known variable, for precision. Random assignment balances everything else, and it is the only one I cite for cause.*
:::

### Who is blind at St Mary's?

:::yourturn
1. Can the patients be blind to their treatment?
2. Who else interacts with the patients, and should they know who got a text?
3. So is the experiment single-blind, double-blind or neither?
:::

:::reveal Reveal — single-blind, the other way round
**1. No.** A patient who gets a text knows it.

**2.** The receptionists who record whether each patient arrived. They should **not** know, so that "missed" is recorded the same way for everyone.

**3.** **Single-blind**: the participants know their treatment, but the research team who interact with them do not. That is the "or vice versa" case of Part 2's definition.
:::

### The results, and what they allow

The experiment ran with Plan 2.

| Block | Treatment | Patients | Missed |
|---|---|---|---|
| Self-booked online | Text | 200 | 8 |
| Self-booked online | No text | 200 | 12 |
| Booked by the hospital | Text | 200 | 30 |
| Booked by the hospital | No text | 200 | 50 |

The hospital's statistician reports that the overall difference between the text and no-text groups is **statistically significant**: random assignment alone would rarely produce a difference this large if texts made no difference. How that is decided is Sessions 15 and 16.

:::yourturn
1. Work out the percentage who missed in each of the four groups, and for all text and all no-text patients.
2. What would a comparison that ignored booking method have mixed together?
3. What may St Mary's conclude? Which element do you cite?
4. Suppose instead the text group had missed 58 of 400, against 62 of 400, and the difference was not statistically significant. Would that show that reminders do nothing?
5. To whom does the conclusion apply? Could it be generalised to all hospitals?
:::

:::reveal Reveal — a statistically significant difference, and its conclusion
**1.**

| Block | Treatment | Missed |
|---|---|---|
| Self-booked online | Text | 8 ÷ 200 = **4.0%** |
| Self-booked online | No text | 12 ÷ 200 = **6.0%** |
| Booked by the hospital | Text | 30 ÷ 200 = **15.0%** |
| Booked by the hospital | No text | 50 ÷ 200 = **25.0%** |
| **All patients** | **Text** | **38 ÷ 400 = 9.5%** |
| **All patients** | **No text** | **62 ÷ 400 = 15.5%** |

With a text: 2.0 points lower among self-booked patients, 10.0 points lower among hospital-booked patients, 6.0 points lower overall.

**2.** Two kinds of patient who miss at very different rates: 20 of 400 self-booked (5.0%) and 80 of 400 hospital-booked (20.0%). Blocking kept that variation out of the comparison.

**3.** That text reminders **caused** a reduction in missed appointments, because the texts were **randomly assigned** and the difference is statistically significant. Cite random assignment, and nothing else.

**4. No.** 58 ÷ 400 = 14.5% against 15.5%: a difference that small could easily come from the random assignment alone, so the experiment would give no convincing evidence either way. Not significant is not evidence of no effect.

**5.** The 800 were not a random sample of any larger population; they were everyone with an appointment in one month. So the conclusion applies to **patients similar to that month's St Mary's outpatients**, not to all hospitals (Part 2, *Experiments on volunteers*). Session 6's records had random selection and no random assignment; this experiment has the reverse.

> *"Because the text reminders were randomly assigned to patients within each booking-method block, and the difference in the percentage who missed (9.5% with a text, 15.5% without) is statistically significant, we can conclude that text reminders caused a reduction in missed appointments. The patients were all of one month's outpatients, not a random sample, so the conclusion applies to patients similar to St Mary's outpatients that month."*

Nothing in that conclusion mentions blocking, replication or the blind receptionists. They made the experiment better; the conclusion rests on random assignment.
:::

---

## Part 6 — On your own: Riverside's hand-cream trial

Work this without looking back, then check.

Riverside hospital, from Sessions 1 and 3, is testing a new hand cream for nurses, whose hands dry out from constant washing. **Thirty nurses volunteer.** For each nurse, a coin toss decides which hand gets the new cream; the other hand gets a **placebo cream** with the same base, colour and smell but no active ingredient. The pharmacy labels the tubes *L* and *R* for each nurse and keeps the key. For two weeks every nurse applies 1 ml from each tube, to the matching hand, after every wash. Then a skin specialist, who does not know which hand had which cream, scores each hand's dryness from 0 (none) to 10 (severe).

:::yourturn
1. Name the experimental design, and give one reason it is more appropriate here than a completely randomized design with 15 nurses on each cream.
2. What is the placebo cream for? Could this experiment measure the placebo effect?
3. Is the experiment single-blind, double-blind or neither? Say who does not know what.
4. Name one variable that is directly controlled, and why it matters.
5. The new-cream hand scored lower (less dry) for 24 of the 30 nurses, and the hospital's statistician says the difference is statistically significant. What can Riverside conclude, and about whom?
:::

:::reveal Reveal — Riverside's answers
1. A **matched pairs design**: each nurse is a pair of hands, matched on everything about that nurse, and a coin decides which hand gets which cream. It is more appropriate because dryness depends heavily on the nurse (how often they wash, their skin, their ward); comparing two hands of the same nurse removes that variation, so the comparison of the creams is more precise than comparing 15 nurses with 15 others.
2. It is the **control**: a treatment different from the treatment of interest, so that any effect of applying a cream at all is the same on both hands and only the active ingredient differs. It **cannot** measure the placebo effect, which is placebo against **no treatment**, and no hand went without cream.
3. **Double-blind**: the nurses do not know which tube is the new cream, and the specialist who scores the hands does not know either. (The pharmacy knows, but takes no part in treating or measuring.)
4. For example, the **amount of cream** (1 ml per hand), **when it is applied** (after every wash), or the **two weeks**, the same for everyone. Each would otherwise affect dryness separately from which cream was used.
5. The new cream **causes** less dryness than the placebo cream, because the creams were **randomly assigned** to the hands and the difference is statistically significant. The nurses volunteered, so the conclusion applies to **nurses similar to these 30 volunteers**, not to all nurses or all people.

**Check yourself for these:** "completely randomized, because a coin was used" (the coin is inside each pair, which makes it matched pairs); "it measures the placebo effect because there's a placebo" (that needs a no-treatment group); "single-blind, because the pharmacy knows" (the pharmacy does not interact with the nurses); citing the placebo or the double-blind design as the reason for cause in question 5 (the reason is random assignment); and "all nurses" in question 5.
:::

---

## Part 7 — Explain it back

:::yourturn
Out loud, or in writing, as if to someone who has never studied statistics: *what goes wrong with a sample that is biased, and why does a bigger one not help? Then: what does random assignment do in an experiment that blocking does not?*
:::

:::reveal Reveal — what a good answer contains
Four things.

1. **Bias** is a systematic error in the method, so its statistics are consistently too high or too low, and a named bias comes with its mechanism and direction: Lincoln High's newsletter replies were too high because parents of bus users chose to reply.
2. A **bigger sample** from the same method reduces the variation from sample to sample but not the bias, as the tool showed at n = 480.
3. **Random assignment** makes the treatment groups similar on every extraneous variable, measured or not, which is what allows a cause-and-effect conclusion.
4. **Blocking** separates the variation of one known variable for a more precise comparison, and is not the reason a cause can be claimed.

If you could explain bias but said "blocking lets us conclude cause", reread Part 5's *Does blocking license the cause?* before Session 8.
:::

---
---

# Homework — Session 7

**40 marks · bring to Session 8, self-marked**

## How to do this homework

1. Do every part **with the answer key closed.** Where you are unsure, answer anyway and put a **?** beside it.
2. Then open the key and **mark your own work honestly.** Write the correct answer beside anything wrong — do not erase what you originally wrote.
3. **Bring the marked sheet.** Your wrong answers and your question marks are what Session 8 opens with.

Everything here was taught in the session; this sheet is practice. Almost every mark is for a **reason**: when you name a bias, say which way it pushes the result and why; when you name a design, say what is random in it; when you conclude, say which element allows the conclusion and whom it reaches.

---

## Part A — Vocabulary (10 marks)

Match each term to its meaning.

| | Term | | Meaning |
|---|---|---|---|
| 1 | Bias | A | Some individuals chosen to be sampled do not respond, and they may differ from those who do |
| 2 | Voluntary response bias | B | The average response to a placebo minus the average response to no treatment |
| 3 | Undercoverage bias | C | More than one experimental unit is assigned to each treatment |
| 4 | Nonresponse bias | D | A systematic error in a sampling method that makes a statistic consistently larger or smaller than the parameter |
| 5 | Response bias | E | Neither the participants nor the research team who interact with them know which treatment each participant receives |
| 6 | Control group | F | Part of the population is left out of the sampling method, or is less likely to be selected |
| 7 | Placebo effect | G | Answers or measurements tend to differ from the true value in one direction |
| 8 | Double-blind | H | A source of extraneous variation used to group the units before treatments are randomly assigned within each group |
| 9 | Replication | I | A sample made up entirely of volunteers |
| 10 | Blocking variable | J | Experimental units created for comparison, which may receive a placebo or a treatment other than the one of interest |

## Part B — The hospital network's patient survey, again (10 marks)

The hospital network from Sessions 1 and 6 discharged **12,400 patients** last year. It wants to estimate the proportion of all 12,400 who **would recommend their hospital to a friend**. For each plan below, **name the bias**, and **say whether the estimate is likely to be too high or too low**, with a reason (1 mark each).

**B1.** Plan T from Session 6: every discharge letter carried a link headed *"Had a problem during your stay? Tell us here."* 1,150 patients used it. (2)

**B2.** A random number generator chose 300 of the 12,400, and each was posted a questionnaire. 126 were returned. The network found that patients who had been readmitted within a month returned far fewer questionnaires than other patients. (2)

**B3.** A random number generator chose 300 patients from the list of those who had given an **email address**. Only 38% of patients over 75 gave one, against 90% of younger patients, and the network's earlier surveys found that patients over 75 are the most likely to recommend their hospital. (2)

**B4.** The questionnaire asks: *"Our nurses worked tirelessly through a very difficult winter. Would you recommend our hospital to a friend?"* Name the bias and its likely direction, and rewrite the question neutrally. (2)

**B5.** A manager says: *"The link in B1 only got 1,150 replies. Leave it open for three more months and we will have 3,000, which will fix the problem."* Explain why it will not. (2)

## Part C — Oakfield's reading experiment (10 marks)

In Session 6's Odd One Out, an Oakfield teacher compared reading on paper and on a tablet with 48 Year 7 students. She now wants to run it properly. Every student will read the same passage, on paper or on a tablet, and then take the same 20-question comprehension quiz.

**C1.** Name the experimental units, the treatments and the response. (1)

**C2.** A colleague suggests: *"Let the students who like tablets use tablets, and the rest use paper."* Explain why this would make a cause-and-effect conclusion difficult, naming a possible confounding variable. (2)

**C3.** Describe how to assign the 48 students to the two treatments in a **completely randomized design**. (2)

**C4.** The school knows each student's reading age: 20 of the 48 have a reading age above their actual age and 28 do not. Describe a **randomized block design** using reading age, and explain why it may be more appropriate than the completely randomized design. (3)

**C5.** Name one variable the teacher should **directly control**, and say why. (1)

**C6.** Can the students be blind to their treatment? Could the person marking the quizzes be? (1)

## Part D — The library's display experiment (6 marks)

The library service from Sessions 4 and 5 has **18 branches**, with weekly visits from 250 to 2,200. It wants to know whether a **display of new books at the entrance** increases the number of items borrowed per week. It will run the display for eight weeks in 9 of the branches. The branches' weekly visits, in order, are:

```
250  450  630  700  700  710  830  910  910
1090 1160 1350 1400 1410 1480 1550 2020 2200
```

**D1.** Explain why a **matched pairs design** suits this study, and describe how to form the pairs and assign the display. (3)

**D2.** After eight weeks, the branches with the display borrowed more items per week, and the difference is statistically significant. What can the library service conclude, and about which branches? (2)

**D3.** Which element of the design allows the conclusion to be about cause? (1)

## Part E — The café's tables, decided by coin (4 marks)

Session 6's homework E3 asked how the café could find out whether putting tables outside **causes** higher takings. The café has now done it: on each of 40 days in spring, the owner tossed a coin at opening time, heads tables out and tails tables in. Mean takings were higher on table days, and the difference is statistically significant.

**E1.** Can the café conclude that putting tables outside causes higher takings? Justify your answer by citing the relevant element of the design. (2)

**E2.** The owner wants to use the result to decide about tables in December. Comment. (1)

**E3.** Suppose instead the difference had **not** been statistically significant. Would that show that tables make no difference to takings? (1)

---
---

# Answer key

*For the student to mark their own work, after attempting everything.*

### Part A (10 marks, 1 each)

1–D · 2–I · 3–F · 4–A · 5–G · 6–J · 7–B · 8–E · 9–C · 10–H

### Part B (10 marks)

**B1.** (2) **Voluntary response bias** (1): the patients chose themselves. **Too low** (1): the heading invites patients who had a problem, who are the least likely to recommend the hospital, so they are over-represented.

**B2.** (2) **Nonresponse bias** (1): the 300 were chosen, and 174 did not respond. **Too high** (1): readmitted patients, who are likely to be less satisfied, responded less, so satisfied patients are over-represented among the respondents.

> The direction must come with its reason. "Nonresponse bias, because 174 did not reply" earns one mark: nonresponse biases the estimate only when the nonrespondents differ, and the mark is for saying how they differ and which way that pushes.

**B3.** (2) **Undercoverage bias** (1): patients without an email address cannot be selected, and most patients over 75 have none. **Too low** (1): the over-75s are the most likely to recommend, and they are under-represented.

> This one is random and still biased. The random number generator chose from an incomplete list; randomness cannot reach people who are not on it.

**B4.** (2) **Response bias**, from question wording (1): the preamble leads toward *yes*, so the estimate is likely to be **too high**. A neutral version: *"Would you recommend this hospital to a friend? Yes or no."* (1 for a rewrite with no leading preamble.)

**B5.** (2) The bias comes from the **method**, patients choosing themselves in response to a heading about problems (1). More replies from the same method are more of the same patients: the estimate would vary less, around the same wrong value (1).

### Part C (10 marks)

**C1.** (1) Units: the 48 students. Treatments: reading the passage on paper, and on a tablet. Response: the quiz score out of 20. All three needed for the mark.

**C2.** (2) The students would choose their own treatment, so the treatment would travel with whatever made them choose it (1). For example, **how much a student reads on screens at home**: students who like tablets may read on screens more, and that practice could raise their quiz scores on a tablet whatever the effect of the tablet itself; so a difference could be due to it, not to the format (1).

> A confounding variable in an experiment is one related to **which treatment** a unit gets (1.13.A.8). Name the variable **and** say how it is tied to the choice and to the score.

**C3.** (2) Number the students 1 to 48. Use a random number generator to choose 24 different numbers (ignoring repeats); those students read on a tablet (1). The other 24 read on paper; then compare the mean quiz scores of the two groups (1).

**C4.** (3) Form two blocks by reading age: the 20 above their age, and the 28 not (1). Within each block, use a random number generator to assign half to paper and half to tablet: 10 and 10, and 14 and 14 (1). It may be more appropriate because reading age is known in advance and is strongly related to comprehension scores; blocking separates that variation from the comparison of paper and tablet, so the comparison is more precise (1).

> "Blocking is better" earns nothing. The mark is for naming the feature of this study, that reading age is known and affects the scores, and connecting it to what blocking does.

**C5.** (1) For example: **the same passage** and the same quiz for everyone; **the same time allowed**; the same room or time of day. Each could otherwise affect the score separately from the format.

**C6.** (1) The students **cannot** be blind: they can see whether they have paper or a tablet. The person marking the quizzes **can** be, if the quizzes carry only a number; then the experiment is single-blind, the "or vice versa" case.

### Part D (6 marks)

**D1.** (3) Weekly visits vary enormously, from 250 to 2,200, and a branch's borrowing depends strongly on how many people visit; pairing branches with similar visits removes that variation from the comparison (1). Pair the branches in order: (250, 450), (630, 700), (700, 710), (830, 910), (910, 1090), (1160, 1350), (1400, 1410), (1480, 1550), (2020, 2200) (1). In each pair, toss a coin to decide which branch gets the display; the other does not; compare the two branches within each pair (1).

**D2.** (2) The display **caused** an increase in items borrowed per week (1), for **these 18 branches** during those eight weeks, or branches similar to them: all 18 of the service's branches took part, so the conclusion is about this service's branches, not about libraries in general (1).

**D3.** (1) **Random assignment**: the coin in each pair decided which branch got the display. Not the pairing, which made the comparison more precise.

### Part E (4 marks)

**E1.** (2) **Yes** (1). The treatment was **randomly assigned** to the days by a coin, so the weather and every other day-to-day variable should be balanced between table days and no-table days, and the difference is statistically significant (1).

> "Yes, because there were 40 days" cites replication, and "yes, because it was an experiment" cites nothing. The mark is for random assignment.

**E2.** (1) The 40 days were spring days, not a random selection of days from the whole year, so the conclusion applies to days similar to those spring days. December's weather is different, and the result may not hold.

**E3.** (1) **No.** It would mean the difference could plausibly have come from the random assignment alone, so the experiment would give no convincing evidence of an effect; that is not evidence of no effect.

### Marks summary

| Part | Marks |
|---|---|
| A — Vocabulary | 10 |
| B — The hospital network's patient survey, again | 10 |
| C — Oakfield's reading experiment | 10 |
| D — The library's display experiment | 6 |
| E — The café's tables, decided by coin | 4 |
| **Total** | **40** |

---
---

# Reference sheet — keep this

*Every term carries an example from this session. Lincoln High's parameter is 651 of 1,842 = 0.353; St Mary's experiment is next month's 800 outpatients.*

### Bias and its kinds, with Lincoln High's samples (1.12.A)

**Bias** — a systematic error in the sampling method: its statistic is consistently too high or consistently too low. Always give the direction and the reason.
*Example: the newsletter replies gave 0.604 against 0.353, and the tool showed this method centring near 0.61 sample after sample.*

**Convenience sample** — the individuals easiest to reach; nonrandom, so potentially biased.
*Example: the first 120 through the main gate: 0.100.*

**Voluntary response bias** — the sample is made up entirely of volunteers, usually those who care most.
*Example: parents replying to a newsletter about the bus timetable, so bus users over-represented: too high.*

**Undercoverage bias** — part of the population is left out, or less likely to be chosen.
*Example: school-bus students use the side bus bay, so a main-gate sample misses them: too low.*

**Nonresponse bias** — individuals chosen for the sample do not respond, and differ from those who do.
*Example: 33 of 120 did not answer at 4:30 pm; bus users were still travelling: too low.*

**Response bias** — the answers or measurements lean one way; includes question wording (leading or confusing questions) and self-reports.
*Example: the late bus: 81.7% yes to one wording, 28.3% to the other.*

> **A bigger sample does not cure bias.** At n = 480 the biased methods clustered more tightly around their wrong values. Only changing the method helps.

### Well-designed experiments: the elements, with St Mary's (1.13.A)

| Element (1.13.A.1) | Meaning | St Mary's reminder experiment |
|---|---|---|
| **Comparison** of at least two treatment groups | one may be a control group | text against no text |
| **Random assignment** | a random mechanism decides each unit's treatment | a random number generator, inside each block |
| **Replication** | more than one unit per treatment | 200 patients per treatment in each block |
| **Direct control** | keep extraneous variables the same for every unit | same wording, sent at 10 am the day before, same rule for "missed" |

**Control group** — units created for comparison; may receive a placebo or a different treatment.
*Example: the no-text patients; or a car-park text, which would isolate the effect of the reminder's content.*

**Placebo** and **placebo effect** — an inactive treatment; the placebo effect is average response to placebo minus average response to no treatment.
*Example: Riverside's placebo cream. With no untreated hand, that trial cannot measure the placebo effect.*

**Single-blind** — the participants do not know their treatment but the team who interact with them do, **or vice versa**. **Double-blind** — neither knows.
*Example: single-blind at St Mary's (patients know, receptionists do not); double-blind at Riverside (nurses and specialist both unaware).*

**Extraneous variable** — known or believed to affect the response, but not being studied. **Random assignment** makes its distribution about the same in every treatment group.
*Example: booking method. In 1,000 random assignments the text group was 44.5% to 55.0% self-booked, against 87.5% when patients chose.*

**Confounding variable in an experiment** — related to the explanatory variable, so its effect cannot be told apart from the treatment's.
*Example: texting only Monday to Wednesday patients: the day would travel with the text.*

### Three experimental designs, each with its example (1.13.B–C)

| Design | What is random | Choose it when | Example |
|---|---|---|---|
| **Completely randomized** | every unit's treatment, with no grouping first | no strong extraneous variable is known in advance | Plan 1: 400 of the 800 texted, by random number |
| **Randomized block** | treatments within each block; the blocks are formed from the blocking variable | a known variable is strongly related to the response | Plan 2: blocks by booking method, 200 texted in each |
| **Matched pairs** | which member of each pair gets which treatment, or the order for one unit | two treatments, and close matching is possible | Riverside: a coin chooses which hand gets the new cream |

*Model justification: "Booking method is known in advance and strongly associated with missing appointments, so blocking on it separates that variation from the comparison of text and no text, giving a more precise comparison."*

### What an experiment lets you conclude, and about whom (1.13.D)

**Cause and effect** — from **random assignment**, with a **statistically significant** difference. Cite random assignment and nothing else.
*Example: "Because texts were randomly assigned within blocks and 9.5% against 15.5% is statistically significant, texts caused fewer missed appointments."*

**Not statistically significant** — the difference could be chance from the random assignment; not evidence of no effect.
*Example: 14.5% against 15.5% would not have shown that texts do nothing.*

**How far it reaches** — random selection generalises to the population; volunteers or everyone available reach only units similar to them.
*Example: St Mary's: patients similar to that month's outpatients. Riverside: nurses similar to the 30 volunteers.*

| Selected at random? | Assigned at random? | You may conclude |
|---|---|---|
| Yes | Yes | cause, for the whole population sampled |
| No | Yes | cause, for units similar to those in the study: St Mary's, Riverside |
| Yes | No | an association, for the population sampled: Session 6's St Mary's records |
| No | No | an association, for units similar to those in the study: Lincoln's gate sample |

:::note red Not in the course description
**Lurking variable**, **Hawthorne effect**, **selection bias**, **measurement bias**, **interviewer bias**, **sampling error**, **randomized comparative experiment**, **crossover design**, **sampling frame**, **multistage sampling**, **quota sampling** and **scope of inference** appear in the prep books but nowhere in the course description. Use *extraneous variable* or *confounding variable*, name the four biases above, and call a design where each unit receives both treatments in random order a **matched pairs design**.
:::

---

*CED references: Topic 1.12 (1.12.A.1–6), Topic 1.13 (1.13.A.1–10, 1.13.B.1–4, 1.13.C.1, 1.13.D.1–2); Topic 3.7 (3.7.B.1) for the formal meaning of statistically significant; the Unit 1 guide's notes on nonresponse direction, random selection and random assignment, and statistically significant differences in well-designed experiments; the Sample Instructional Activity for topics 1.11–1.12 (Password-style games). Course and Exam Description effective Fall 2026.*

*Supporting reading: Barron's pdf 245–262 · Princeton Review 187–196 · 5 Steps to a 5 126–133.*

*Next session: Topics 2.1–2.3 — two-way tables, with joint, marginal and conditional relative frequencies, and simulation as a way of estimating a probability.*
