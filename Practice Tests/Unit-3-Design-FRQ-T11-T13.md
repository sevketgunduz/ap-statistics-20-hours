# Practice Test — Collecting Data (Section II: Free Response, T11–T13)

Source: scanned practice test (`Taranmış Belge.pdf`, pages 6–7), questions T11, T12 and T13.
Topics: experimental design, control and placebos, blocking and matched pairs, confounding,
blinding, investigative questions, stratified random sampling, nonresponse bias.

> **Show all your work. Indicate clearly the methods you use, because you will be graded on the
> correctness of your methods as well as on the accuracy and completeness of your results and
> explanations.**

---

## T11 — Elephants, bees and acacia trees

Elephants sometimes damage trees in Africa. It turns out that elephants dislike bees. They
recognize beehives in areas where they are common and avoid them. Can this information be used to
keep elephants away from trees? Researchers want to design an experiment to answer these questions
using 72 acacia trees and three treatments: active hives, empty hives, and no hives.

a. Identify the experimental units in this experiment.
b. Explain why it is beneficial to include some trees that have no hives.
c. Describe how the researchers could carry out a completely randomized design for this
   experiment. Include a description of how the treatments should be assigned.

### Solution

**a. Experimental units**

The **72 acacia trees**. (Not the elephants — the elephants are not assigned treatments; the trees
are what receive active hives, empty hives, or no hives.)

**b. Why include trees with no hives**

The no-hive trees are the **control group**. They provide a baseline for how much damage acacia
trees suffer when nothing at all is done. Without them, researchers could compare active hives to
empty hives but would have no way of knowing whether *either* kind of hive reduces damage compared
with leaving a tree alone.

Note the role of the two hive groups together: the **empty hive acts as a placebo**, so that if
active-hive trees do better than empty-hive trees, the difference can be attributed to the live bees
rather than to the mere presence of a box hanging in the tree. The no-hive group then tells you the
effect of hanging anything at all.

**c. Completely randomized design**

1. Number the acacia trees **1 through 72**.
2. Use a random number generator (or draw 72 numbered slips from a hat) to pick **24 distinct
   numbers at random** — those trees get **active hives**.
3. From the remaining 48, randomly pick **24 more** — those get **empty hives**.
4. The remaining **24 trees get no hives** (control).
5. Leave the treatments in place for the same fixed period, then measure the **amount of elephant
   damage** on each tree by the same method.
6. Compare the distributions of damage across the three groups; if the active-hive group shows
   substantially less damage than could plausibly arise by chance, attribute the difference to the
   active hives.

Equal group sizes (24/24/24) are not required, but they give the most precise comparisons.

---

## T12 — Caffeine withdrawal and tapping speed

Many people start their day with a jolt of caffeine from coffee or a soft drink. Most experts agree
that people who consume large amounts of caffeine each day may suffer from physical withdrawal
symptoms if they stop ingesting their usual amounts of caffeine. Researchers recruited 11 volunteers
who were caffeine dependent and who were willing to take part in a caffeine withdrawal experiment.
The experiment was conducted on two 2-day periods that occurred one week apart. During one of the
2-day periods, each subject was given a capsule containing the amount of caffeine normally ingested
by that subject in one day. During the other study period, the subjects were given placebos. The
order in which each subject received the two types of capsules was randomized. The subjects' diets
were restricted during each of the study periods. At the end of each 2-day study period, subjects
were evaluated using a tapping task in which they were instructed to press a button 200 times as
fast as they could.

a. Describe a statistical benefit of directly controlling the diets of subjects during the
   experiment.
b. How was blocking used in the design of this experiment? What is the benefit of blocking in this
   context?
c. Researchers randomized the order of the treatments to avoid confounding. Explain how confounding
   might occur if the researchers gave all subjects the placebo first and the caffeine second. In
   this context, what problem does confounding cause?
d. Could this experiment have been carried out in a double-blind manner? Explain your answer.

### Solution

**a. Statistical benefit of controlling the subjects' diets**

Diet is a source of variability in tapping performance — other foods and drinks contain caffeine,
and food intake affects alertness. By holding diet fixed for every subject in both study periods,
the researchers **remove that variability from the response variable**. Less unexplained variation
in tapping counts means any difference between the caffeine condition and the placebo condition
stands out more clearly, so the experiment is **more likely to detect a real effect of caffeine**
(and the observed difference is less likely to be explainable by diet).

**b. How blocking was used, and its benefit**

**Each subject is a block** — this is a *matched-pairs* design, the special case of a randomized
block design with blocks of size 2. Every one of the 11 volunteers received **both** treatments
(caffeine capsule in one 2-day period, placebo in the other), with the order randomized separately
for each subject.

**Benefit:** people differ enormously in their natural tapping speed and in how caffeine-dependent
they are. Blocking by subject means the caffeine-versus-placebo comparison is made *within* each
person, so this large person-to-person variability never contaminates the comparison. With only 11
volunteers, this is what makes the experiment sensitive enough to detect a caffeine effect at all.

**c. Confounding if placebo always came first**

If every subject took the placebo in week 1 and caffeine in week 2, then **treatment would be
completely entangled with time order**. Subjects would be doing the tapping task for the second time
in the caffeine period, so they would have had practice and would likely tap faster regardless of
what was in the capsule. Other period effects point the same way — by week 2 the subjects are more
used to the restricted diet and the lab routine.

So if caffeine-period tapping scores came out higher, there would be **no way to separate the effect
of the caffeine from the effect of practice/familiarity**. That is exactly what confounding means:
the effect of the explanatory variable cannot be distinguished from the effect of another variable,
here the order of the periods. Randomizing the order breaks the link — about half the subjects get
caffeine first — so practice effects are spread across both treatments instead of favouring one.

**d. Could it be double-blind? Yes.**

Capsules make this easy. The caffeine capsule and the placebo capsule can be made **identical in
appearance, weight and taste**, so a subject cannot tell which one they swallowed — that is the
first blind. A third party prepares and codes the capsules, so the **staff member who hands out the
capsules and records the tapping results does not know which subject is in which condition** either
— that is the second blind. (The tapping task is counted by the button/machine anyway, which further
protects the measurement.)

Both blinds matter here: subjects who knew they were caffeine-deprived might *expect* to perform
worse and slack off, and an evaluator who knew the assignment might unconsciously encourage or time
subjects differently.

---

## T13 — Estimating the proportion enrolled in a four-year college

The counseling department at a large high school wants to estimate the proportion of last year's
graduating class who are enrolled in a four-year college or university. To do this, they hope to
survey 50 of the 800 graduates from last year.

a. Determine the investigative question for this statistical study. Make sure to include the three
   components.
b. Describe how to select a stratified random sample of 50 students. Explain your choice of strata.
c. What is the advantage of using a stratified random sample instead of a simple random sample in
   this context?
d. When the counselors send an email to the 50 students selected for the sample, only 21 students
   respond. Explain how nonresponse could lead to bias and what effect the bias will have on the
   estimated proportion of students who are enrolled in a four-year college or university.

### Solution

**a. Investigative question (three components)**

> *"What proportion of the 800 students in last year's graduating class at this high school are
> currently enrolled in a four-year college or university?"*

- **Population:** the 800 graduates from last year's class at this high school
- **Variable:** whether or not the graduate is enrolled in a four-year college or university
  (categorical, two outcomes)
- **Parameter of interest:** the **proportion** *p* of that population enrolled in a four-year
  college or university

**b. Selecting a stratified random sample of 50**

Choose strata made up of students who are **similar to one another on the variable being measured**.
A good choice is the students' **academic program/track** (for example: AP–honours track, standard
college-prep track, and vocational/general track), because college enrolment rates differ sharply
between those groups while students within a group tend to be alike. (Last year's GPA bands would
work equally well, and for the same reason.)

Then sample **proportionally**: 50/800 = 1/16 of the class, so take 1/16 of each stratum. If, say,
the strata contain 240, 400 and 160 students, the sample would be 15, 25 and 10 students
respectively.

Within each stratum, **number the students, use a random number generator to draw the required
number of distinct labels (ignoring repeats)**, and survey those students. Combine the three
sub-samples into the sample of 50.

**c. Advantage over an SRS of the same size**

Because students within a stratum are similar with respect to college enrolment, stratification
**guarantees that every track is represented in the correct proportion** — an SRS could by chance
pull mostly AP students or mostly vocational students. Removing that source of chance variation
makes the sample-to-sample variability of the estimate **smaller**, so the stratified estimate of
*p* is **more precise** (a smaller margin of error) than an SRS of 50 would give.

**d. Nonresponse and its effect**

Only 21 of the 50 selected students replied, so the estimate is really based on the 21 who chose to
answer — and **the 29 non-responders are unlikely to be like the responders**. Graduates who are
enrolled at a four-year college still have an active school-linked email, stay in touch with the
school, and are generally pleased to report where they ended up. Graduates who are working, in the
military, at a two-year college, or not in school at all are harder to reach and have less incentive
to reply.

That makes the respondents **overrepresent four-year college students**, so the sample proportion
will tend to come out **larger than the true proportion *p*** — the estimate is biased **too high**.
Note that this bias is a property of the design, not of sample size: surveying more students the
same way would not fix it; following up persistently with the non-responders would.
