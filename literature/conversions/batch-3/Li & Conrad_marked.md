---
conversion_metadata:
  converted_at: "2026-07-21T13:57:48Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Li & Conrad.pdf"
  source_pdf_sha256: "41f5be4c55c97bdb06c4754a651481ee73fc85f770e05d5cb5c8da6b45f43370"
  page_count: 52
  markdown_char_count: 260082
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Persona-Based Simulation of Human Opinion at
Population Scale

Mao Li1* and Frederick G. Conrad1

1Institute for Social Research, University of Michigan, 426 Thompson
St., Ann Arbor, 48104, MI, US.

*Corresponding author(s). E-mail(s): maolee@umich.edu;
Contributing authors: fconrad@umich.edu;

Abstract

What does it mean to model a person, not merely to predict isolated responses,
preferences, or behaviors, but to simulate how an individual interprets events,
forms opinions, makes judgments, and acts consistently across contexts? This
question matters because social science requires not only observing and predict-
ing human outcomes, but also simulating interventions and their consequences.
Although large language models (LLMs) can generate human-like answers, most
existing approaches remain predictive, relying on demographic correlations rather
than representations of individuals themselves.
We introduce SPIRIT (Semi-structured Persona Inference and Reasoning for
Individualized Trajectories), a framework designed explicitly for simulation
rather than prediction. SPIRIT infers psychologically grounded, semi-structured
personas from public social media posts, integrating structured attributes (e.g.,
personality traits and world beliefs) with unstructured narrative text reflecting
values and lived experience. These personas prompt LLM-based agents to act as
specific individuals when answering survey questions or responding to events.
Using the Ipsos KnowledgePanel, a nationally representative probability sample
of U.S. adults, we show that SPIRIT-conditioned simulations recover self-
reported responses more faithfully than demographic persona and reproduce
human-like heterogeneity in response patterns. We further demonstrate that per-
sona banks can function as virtual respondent panels for studying both stable
attitudes and time-sensitive public opinion.

Keywords: Persona inference, Synthetic respondents, Large language models, Social
simulation, Social Media

1

6
2
0
2

r
a

M
8
2

]

Y
C
.
s
c
[

1
v
6
5
0
7
2
.
3
0
6
2
:
v
i
X
r
a

---

<!-- PAGE 2 -->

1 Introduction

Large language models (LLMs) are increasingly used to simulate opinion formation,
opinion change, and decision making, opening new possibilities for computational
social science and user-centric NLP applications [1–3]. A common approach gives the
model a short demographic profile (for example age, gender, education), often called
a persona, and asks it to answer as if it were a person with that profile. [1, 2]. This
approach is conceptually appealing because demographics are widely available and
central to population inference. However, it assumes that demographics alone largely
account for variation in opinions and behaviors across people. Recent studies show
that results can change sharply when the question wording, examples, or formatting
in the prompt changes. [4–6].

In response, researchers have attempted to address these limitations in two main
ways. One tries to increase diversity by simulating many more synthetic respondents,
sometimes with a larger set of profile fields [3, 7, 8]. These methods can produce a
wider range of answers and may reduce obvious skews, such as always producing the
same view for a given demographic group. But they still do not show that the mix
of simulated people matches any real population, or that simulated group differences
align with observed group differences.

Another approach focuses on enriching personas using detailed survey responses or
text produced by the simulated individual, such as life narratives or interviews. [3, 9–
12]. These methods yield more vivid and coherent simulated responses, improving
realism and consistency. Yet, they remain centered on individual-level fidelity and
leave open the question of how collections of such personas relate to population-level
distributions.

Despite their differences, both approaches leave unresolved a core challenge for
using LLMs in social scientific inference: how to estimate population-level distribu-
tions, especially when personas are derived from either prompting an LLM to play
a particular role (e.g., “You are a 50-year-old Republican female from Kansas”) or
sampling multiple users from non-probability sources, such as social media. Scaling
the number of synthetic respondents or enriching persona descriptions can make sim-
ulations look more realistic, but these approaches do not, by themselves, make the
results suitable for population inference. The central problem is that the data obtained
from the persona(s) are constrained by who they represent, which will not necessarily
be the target population (often the general public). This mirrors a basic distinction
in survey research: probability samples, with known inclusion probabilities, support
design-based population estimation, whereas non-probability samples require addi-
tional assumptions and methods, such as calibration, to adjust for selection bias and
unequal inclusion [13].

At a more fundamental level, demographics capture only a small portion of what
shapes opinions and decisions [14]. Many influential factors are not explained by age,
gender, or education, such as personality traits [15], basic beliefs about the world [16],
political identity [17], narrative identity [18], and the information environments people
inhabit [19]. As a result, demographic-based personas are often not sufficiently nuanced
to provide realistic, person-specific responses. When the prompt underspecifies the
individual person, the model tends to fill in the gaps using broad patterns learned

2

---

<!-- PAGE 3 -->

during training [20, 21], which can dominate the simulated responses. The gap between
what demographics determine about an individual’s opinion and what the model must
infer based on the particular set of demographics, limits the accuracy of persona-based
simulations of public opinion and behavior at a population level. These limitations
suggest that realistic simulation requires richer, more psychologically grounded person-
representations than demographics alone can provide.

Studies of everyday self-expression on social media show that people’s language and
behavior patterns are associated with self-reported personality measures, indicating
that online traces reflect enduring differences between individuals [22]. Classic work by
Kosinski and colleagues further showed that simple digital records, such as Facebook
“Likes,” can be used to predict a range of personal attributes [23]. Building on these
findings, studies report that LLMs can infer traits directly from users’ social media
text in a prompt-based setting, with performance comparable to models trained on
labeled data in some tasks [24]. Evidence also suggests that this signal is not limited
to social media: Wright and colleagues show that generative models can estimate Big
Five personality traits (a common five-dimension personality framework) from brief
open-ended narratives, producing respectable agreement with self-reports [25].

Prior work often stops at trait prediction and does not provide a clear way to
organize inferred attributes into a reusable persona for simulation and evaluation.
To move the enterprise forward, we introduce SPIRIT (Semi-structured Persona
Inference and Reasoning for Individualized Trajectories), a framework that constructs
structured, multi-dimensional personas from social media text and applies them in
LLM-based behavioral simulation.

We first recruited panel members from a probability-based online panel (the Ipsos
KnowledgePanel) who were also social media users, and collected their user handles
on Reddit, Twitter, or both. Participants consented to linking their public posts to
their Ipsos survey responses, which allowed the model to infer a SPIRIT persona for
each individual. Because KnowledgePanel is designed to represent the U.S. population
under a probability-based recruitment design, this starting point supports population-
level inference.

We refer to the resulting collection of SPIRIT personas as a Persona Bank. Con-
ceptually, it functions as a virtual twin panel that can be surveyed using standardized
instruments. At the same time, our linkage procedure imposes additional eligibility
requirements (having an account, posting, and consenting to link), which can introduce
selection bias. We therefore construct weights and apply them to each persona-bank
respondent to align weighted estimates with U.S. population benchmarks. By com-
bining established ideas from survey methodology [26–28] with LLM-based persona
inference and simulation, SPIRIT provides a practical foundation for population-level
simulation.

In summary, SPIRIT provides a persona framework in which personas are (1)
inferred from authentic social media posts and (2) reweighted to support population-
level generalization. Unlike prior approaches that focus on either increasing the number
of synthetic respondents or enriching persona detail without addressing the sampling
problem, SPIRIT operates at two levels: at the individual level, it prompts an LLM to
adopt a person-specific persona to answer survey questions; at the population level, it

3

---

<!-- PAGE 4 -->

combines those person-level responses with calibration weights so that aggregates can
be interpreted as U.S. population estimates.

Across multiple survey questions on prominent political

issues, SPIRIT per-
sona outperforms demographic persona, producing simulations that are more stable
across questions, easier to interpret, and more consistent at both the individual and
population levels.

Our contributions are threefold:

1. We introduce SPIRIT, a semi-structured persona framework that infers multi-
dimensional user representations from social media text that are interpretable and
uses them to prompt an LLM to respond to survey questions as the individual
represented by the persona would respond.

2. We provide a systematic evaluation of our framework, showing that demo-
graphic personas yield unrealistic response distributions and lower-confidence
estimates, while SPIRIT personas better recover coherent, person-specific response
patterns—highlighting the limits of demographic attributes alone for simulating
how opinions are formed and change.

3. We develop and empirically evaluate the Persona Bank. In particular, we calibrate
persona-based simulations to population benchmarks and validate the resulting
virtual panel against survey and polling results concerning salient political issues
measured by high-quality opinion polls.

2 Results

The Ipsos KnowledgePanel collects a substantially broad set of respondent informa-
tion; for the purposes of this study, we obtained a subset of 81 survey questions
from the Ipsos records spanning a wide range of topics, from demographic charac-
teristics to attitudes toward public health and vaccines. To construct a demographic
persona for comparison, we use seven demographic variables—age, race, gender, polit-
ical ideology, income, education, and urbanicity—as persona inputs. The remaining
52 non-demographic questions (spanning from self-rated health to political attitudes)
are then used as held-out evaluation outcomes to assess how well different persona
constructions recover respondents’ self-reported views and dispositions (full question
wording is provided in Appendix C).

We evaluate the proposed framework along two complementary dimensions: (i)
inference accuracy and (ii) the distribution of inferred user-level responses. We com-
pare the demographic personas against the SPIRIT personas, which relies exclusively
on non-demographic attributes inferred from user-generated text, across LLMs of
increasing size.

2.1 Framework Evaluation

2.1.1 Accuracy of user-level inference

Inference accuracy is evaluated at the user level. Each user is associated with a set of
questions; for each question, the model produces an inferred response that is compared
against the user’s self-reported value. We compute the mean accuracy per user and

4

---

<!-- PAGE 5 -->

Fig. 1 Framework evaluation across models and conditioning strategies. A, Distribution of per-user
position-weighted mean inferred values for the same eligible Ipsos KnowledgePanel participants linked
to public social media accounts, comparing their self-reported responses with simulated responses
generated under the demographic persona and the SPIRIT persona (with non-demographic attributes
inferred from text). For each participant, responses are aggregated across survey items using a
position-weighted mean, such that identical composite values arise only from identical response
patterns. Human responses are shown as an empirical reference for the level of population-level
heterogeneity expected when aggregating across many items. Demographic personas yield highly
concentrated distributions, whereas SPIRIT personas preserve substantially greater individual-level
variation, closely resembling human heterogeneity. B, User-level inference accuracy across models
ordered by size. SPIRIT personas consistently outperform demographic personas with performance
gains saturating for larger models.

then average across users within each persona condition (i.e., SPIRIT persona vs.
demographic persona).

As shown in Figure 1B, under the SPIRIT personas, inference accuracy increases
monotonically with model size. Smaller models (e.g., Gemma-3-4B and LLaMA-3.1-
8B) perform substantially worse than larger models, while gains begin to plateau from
Gemma-3-27B to GPT-5-mini and GPT-5.2. This pattern is expected: the core require-
ments of the framework—reading user posts, constructing non-demographic persona
representations, and reasoning over them—rely primarily on stable comprehension
and moderate-level reasoning rather than highly complex capabilities (e.g., Coding or

5

---

<!-- PAGE 6 -->

solving math problems). Once these competencies are met, additional model capacity
yields diminishing returns.

Comparing the demographic personas with the SPIRIT personas, we observe a
consistent accuracy advantage for the SPIRIT personas across all models. While
demographic personas’ accuracy improves modestly with model size, these gains pre-
sumably reflect improved guessing by larger models based on correlations between
demographics and responses to survey items (e.g., income and credit score), rather
than grounded inference from individual-specific signals. Overall, the observed 8–9%
absolute improvement indicates the SPIRIT personas substantially outperform the
demographic personas.

2.1.2 Distributional properties of inferred responses

Accuracy alone does not capture how well LLMs simulate the full pattern of user
responses, especially their variability: accuracy can remain high even when inferred
answers are overly concentrated. We therefore examine the distribution of inferred
user-level mean responses under each persona condition. For each user, we aggregate
inferred responses across all 52 survey questions into a single composite score that
summarizes their overall response pattern. We compute a position-weighted per-user
mean, where each item response is weighted by its position in the survey sequence
(details are provided in Methods 4.3).

A key property of this construction is that two users will obtain the same com-
posite score only if their response sequences are identical across all questions. Because
perfectly identical sequences are unlikely in realistic survey settings, and would effec-
tively eliminate individual heterogeneity, we expect substantive user-level differences
to manifest as a dispersed distribution of composite scores rather than one concen-
trated around a single value. This composite score preserves the ordering of responses
while reducing each user’s response profile to a single summary measure that still
captures meaningful heterogeneity across users.

The same aggregation rule is applied to inferred responses and human self-reports.

The resulting distributions are visualized using box plots (Figure 1A).

To provide a meaningful reference point, we include the distribution of human self-
reported responses. This human distribution is not treated as a target to be matched
exactly, but rather as an empirical benchmark for population-level heterogeneity.

Across all models, SPIRIT personas produce broader and more differentiated dis-
tributions than demographic personas, more closely resembling the spread observed
in human responses. In contrast, the demographic personas yield markedly nar-
rower distributions, indicating homogenized predictions driven by shared demographic
profiles.

This behavior is expected. For certain questions, such as credit score or media con-
sumption, the demographic personas provide strong predictive signals. For example,
high household income is strongly associated with excellent credit scores, and age cor-
relates with lower social media use and greater reliance on television or newspapers.
When such correlations dominate, demographic persona inference tends to collapse
individuals with similar demographic profiles into near-identical predictions, thereby
reducing population-level diversity.

6

---

<!-- PAGE 7 -->

Consistent with this pattern, the median inferred value under demographic
personas is concentrated around approximately 1.5. This reflects a tendency for
demographic persona inference to default to negative responses (e.g., No) for many
behavioral and health-related questions (e.g., drinking alcohol or reporting anxiety-
related conditions), which substantially compresses the range of possible inferred
responses. In addition, the demographic personas yield lower confidence estimates than
the SPIRIT personas, a result that is expected given the limited informational con-
tent available when inference relies solely on demographic attributes. Further analyses
unpacking these distributional and confidence differences are provided in Appendix D.
SPIRIT personas mitigate this effect by incorporating linguistic, behavioral, and
psychological signals extracted from user-generated text. This is particularly salient
for attributes weakly determined by demographics, including psychological traits and
mental health-related indicators. As a result, SPIRIT personas preserve individual-
level variation that is otherwise lost under demographic personas.

It is important to note that inference accuracy is computed using a strict exact-
match criterion between inferred values and self-reported responses. This metric does
not account for measurement error inherent in survey responses. Prior work has shown
that human responses—particularly for Likert-type items—are subject to instability
over time [3, 29]; even when the same individual is re-interviewed after a short interval,
responses may differ due to interpretation, recall, or response scale ambiguity. For
example, distinctions between categories such as sometimes and often may reflect
measurement noise rather than substantive disagreement.

To account for this, we additionally compute an off-by-one rate for the best-
performing configurations (GPT-5.2 and GPT-5-mini with SPIRIT personas). The
off-by-one rate is defined as the proportion of inferred responses whose ordinal dis-
tance from the corresponding self-reported value is exactly one category, aggregated
across survey items at the individual level. We find off-by-one rates of 0.18 for GPT-5.2
and 0.19 for GPT-5-mini, indicating that approximately 83% of inferred responses are
either exact matches or differ by at most one response category from the self-reported
value.

We focus our main comparison on the 52 non-demographic items because the
remaining 29 items are demographic variables, and some of these are used to construct
the demographic persona. Including them in the primary evaluation would therefore
make the comparison less fair. We nevertheless extend the analysis to all 81 items as
a supplementary check. Because SPIRIT is inferred only from users’ historical Reddit
and Twitter/X posts and does not use any self-reported survey attributes, including
demographics, this broader analysis allows us to assess whether the inferred personas
can also recover demographic characteristics that were never given as inputs.

A clear pattern emerges across domains. SPIRIT performs particularly well on
health- and vaccine-related items, which tend to reflect more stable beliefs and to
show stronger consistency across related questions. In contrast, performance is weaker
on short-horizon behavioral items such as beer consumption (e.g., whether someone
drank in the past week or month). These behaviors are inherently more variable and
sensitive to recent circumstances, so even the same person may answer differently over
time, making them harder to infer reliably from long-run posting histories.

7

---

<!-- PAGE 8 -->

Importantly, this is not the primary use case we emphasize. Our goal is to support
inference and simulation of comparatively stable orientations and belief systems, where
internal consistency is expected and substantively meaningful, rather than to predict
transient, week-to-week behaviors. The results of this extended evaluation are reported
in Appendix F.

These results show that the proposed framework improves not only inference
accuracy but also the realism and expressiveness of inferred user responses. While
demographic personas perform well for easily predictable attributes probably because
population-level correlations, SPIRIT personas capture individual differences and
avoid overly homogeneous simulations.

2.2 Persona banks as virtual respondent panels

While the first part of the results establishes the validity of the proposed framework by
benchmarking simulated responses against self-reported values, such validation alone
is not the ultimate objective of this work. The self-reported data available for bench-
marking may not themselves be of substantive interest to researchers. The broader
goal is to enable SPIRIT personas to simulate public opinion across a wide, if not
unconstrained, range of topics and questions.

We therefore turn to a second set of analyses that treat the group of SPIRIT
personas as a persona bank, i.e., a collection of virtual respondents that can be sur-
veyed using standardized survey instruments. Conceptually, this persona bank serves
as a virtual respondent panel, allowing us to examine public attitudes toward rapidly
evolving and event-driven issues for which traditional survey data are often delayed
or expensive.

2.2.1 Surveying the persona bank

We focus on four public issues that were highly salient during the study period: (i)
opinions about abortion [30], (ii) attitudes toward immigration [31], (iii) public reac-
tions to the Epstein files [32], and (iv) views on U.S. military actions in Venezuela
[33]. For each topic, we reused survey questions from contemporaneous public opin-
ion polls, preserving the original wording and response options. These questions are
posed to the persona bank, and the resulting simulated responses are aggregated to
produce population-level estimates, with each respondent weighted accordingly (as
described in Method 4.2.4). Full question wordings and response options are provided
in Appendix E.

We interpret the first two question clusters (i.e., opinions about abortion and atti-
tudes toward immigration) as measuring relatively stable, crystallized opinions that
tend to be anchored in enduring belief structures [34]. By contrast, clusters (iii) and
(iv) capture more time- and event-sensitive judgments, for which expressed opin-
ions are often constructed from whatever considerations and facts are most salient at
the moment of response [35]. Accordingly, for clusters (iii) and (iv), we allow simu-
lated LLM respondents to retrieve up-to-date external information via web search, as
described in Method 4.4.

8

---

<!-- PAGE 9 -->

Fig. 2 persona-bank responses compared with polling benchmarks, grouped by question type. A,
Long-term attitudinal questions (abortion and immigration) drawn from general opinion surveys. B,
Event-sensitive questions (Epstein files and Venezuela policy attitudes) fielded in late 2025 to early
2026, for which simulated respondents may require contemporaneous context. Shaded regions indicate
issue-specific clusters and are used to avoid implying continuity across unrelated issues. Within each
issue-specific cluster, persona-bank estimates reproduce coherent question-to-question patterns that
align with polling benchmarks. After calibration, Twitter-based estimates track benchmarks more
closely in absolute level than Reddit-based estimates, which exhibit systematic shifts in magnitude.
Both Twitter- and Reddit-based estimates preserve the same directional structure.

2.2.2 Trend alignment with polling benchmarks

Figure 2 compares weighted estimates derived from Twitter- and Reddit-based SPIRIT
persona banks with polling benchmarks across multiple domains. All simulated
responses are generated by querying the same underlying set of simulated respondents,
i.e., the persona-bank, which makes comparisons across questions within an issue-
specific cluster directly interpretable. In contrast, the polling benchmarks are drawn
from different survey organizations and respondent samples, and therefore should not
be interpreted as forming a single, internally comparable scale across clusters.

Accordingly, our evaluation emphasizes within-cluster pattern alignment rather
than cross-cluster comparisons. We focus on whether persona-bank responses move up
as polling benchmark estimates move up and down as polling benchmark estimates
move down across related questions within each issue-specific cluster.

In Panel A, which displays measures of long-term and crystallized attitudes on
abortion and immigration, the Twitter-based persona bank closely tracks polling
benchmarks after calibration, both in magnitude and in direction of question-to-
question changes. The Reddit-based persona bank exhibits larger shifts in absolute

9

---

<!-- PAGE 10 -->

levels, particularly for immigration-related items, but preserves consistent directional
patterns that mirror the polling benchmark. As documented in Appendix A, these
differences in magnitude are consistent with known compositional differences in the
Reddit sample, which is more educated and more politically liberal than the population
in general.

Panel B examines event- and time-sensitive questions related to the Epstein files
and U.S. policy toward Venezuela. Despite the additional complexity introduced by
time-sensitive information and heterogeneous polling sources, persona-bank responses
again reproduce coherent within-cluster structure. Items eliciting stronger support
in polling data are generally ranked higher by persona-bank responses, while lower-
support items remain comparatively low. This agreement across polling references
strengthens the interpretation that persona-bank responses capture coherent, item-
to-item attitude patterns (that is, consistent changes in direction across related
questions).

Importantly, these trend-alignment patterns are not an artifact of calibration.
When responses are aggregated without weighting, persona-bank estimates continue
to reproduce the same within-cluster directional structure, albeit with substantially
larger deviations in absolute levels. Weighting mainly reduces the magnitude of these
differences, which we attributed to the slection bias, i.e., who is and who is not repre-
sented in the sample. Unweighted results are reported in Appendix F.6, showing that
weighting improves accuracy without changing the main conclusions.

At the same time, we observe two systematic deviations from typical human survey
behavior. For the items asking “whether the Epstein files should be released”, “Has
the Trump administration clearly explained what the U.S. intends to do regarding
Venezuela?” or “Does the Trump administration need to explain...” nearly all simu-
lated respondents selected “Yes,” “has not explained clearly” and “needs to explain”,
whereas attitudes from real-world respondents are more heterogeneous. Survey respon-
dents may answer these questions based on more nuanced consideration, e.g., affect,
partisan cues, or general distrust in institutions, rather than treating them as relatively
factual judgments, the way LLM seems to do.

Another deviation arises for items that implicitly require respondents to reason
through a multi-step mechanism. Consider: “Do you think U.S. military action in
Venezuela would decrease the amount of drugs coming into the U.S.?” In conventional
survey settings, many respondents do not fully account for the link between policy
interventions and downstream outcomes. Instead, they often rely on low-effort heuris-
tics: a response of “Yes, would decrease” can function as an intuitive, affirmation of
the policy, whereas “no effect” can express doubt about the policy with low effort
and without having to explain why. In contrast, simulated agents are systematically
more likely to “work the problem.” They lay out a causal chain (e.g., displacement
of routes, adaptation by trafficking organizations, enforcement fragmentation, and
downstream supply responses) and, after tracing these steps, frequently converge on
“increase” as the most coherent implication of intervention. This pattern is consistent
with established evidence that survey respondents often satisfice rather than opti-
mize when questions are cognitively demanding [36], whereas the simulated agents are
not programmed to reduce effort. These deviations are therefore not random errors,

10

---

<!-- PAGE 11 -->

but reflect a systematic difference in how human and simulated agents respond to
surveys. Additional topic- and item-level analyses of these patterns are reported in
Appendix F.4.

Taken together, these results indicate that persona banks can serve as a credible
source of information about public opinion. Even when absolute levels diverge, most
notably for Reddit, the SPIRIT personas reproduce coherent patterns of opinion and
consistent trends. This supports our intuition that persona-based virtual panels (i.e.,
the persona bank) are useful for comparative analysis and rapid-response measure-
ment, especially in settings where traditional surveys are expensive or too slow to
field.

3 Discussion

This study introduces SPIRIT, a semi-structured persona inference framework that
builds rich representations of individuals based on their attributes, inferred from their
social media traces, extending well beyond demographics. Because SPIRIT is built
from an address-based probability panel, the target population is well-defined (i.e.,
US population), and we are able to provide calibration weights to project aggregated
results back to U.S. population benchmarks. Across two complementary evaluations,
we demonstrate both the validity of the proposed framework and the broader potential
of surveying a reusable persona bank for downstream computational social science
analyses.

3.1 From validation to simulation
In the first part of our analysis, we show that SPIRIT personas can faithfully infers
a wide range of self-reported attributes under a strict exact-match evaluation. These
results establish the internal validity of the framework: inferred SPIRIT personas are
not arbitrary abstractions, but capture meaningful individual-level signals reflected in
survey responses.

However, recovering self-reported values is not the ultimate objective of persona-
based modeling. Self-reports are inherently limited in scope and timeliness, and many
substantive research questions concern attitudes toward events that unfold faster than
traditional surveys can capture. The second part of our results, therefore, reframes
inferred SPIRIT personas as a persona bank —a virtual respondent panel that can be
queried using standardized survey instruments to study emerging public opinion. Our
findings show that, after appropriate weighting, persona-bank responses reproduce
trends across questions and topics that closely align with contemporaneous polling
benchmarks. This suggests that persona-based virtual panels can serve as a useful
source for rapid-response ( e.g., immediately after a political debate or in the aftermath
of a natural disaster) and exploratory public opinion research.

3.2 Why demographic attributes alone are insufficient

A central insight of this work is that simulating human opinion requires substantially
more information than demographic attributes alone. Although demographics are an

11

---

<!-- PAGE 12 -->

important part of who people are, our results show that personas comprised only
of demographic attributes tend to produce compressed response distributions (i.e.,
simulated answers concentrate on a narrow subset of options) and answers that lean
heavily on broad demographic “stereotypes” rather than on person-specific evidence.
Importantly, in our experimental design, we intentionally exclude demographic
attributes from the SPIRIT personas in order to isolate the contribution of non-
demographic signals derived from users’ historical posts. This design choice should not
be read as a recommendation to omit demographics in applied settings. On the con-
trary, SPIRIT is designed to accommodate as much relevant information as possible.
The broader goal is to construct personas that are richly grounded in lived experi-
ence, so the model reasons not about what a typical person with certain demographics
might think, but about how a particular individual who has a particular demographic
profile would plausibly respond given their expressed values, beliefs, and behavioral
patterns. In short, demographics are a core component of identity, but they are not
the whole story.

3.3 The role of data richness and user expression

The quality and richness of input data play a critical role in the success of persona-
based inference. In our study, users whose attitudes are most faithfully reconstructed
are typically those who leave dense and expressive digital traces, sharing opinions,
experiences, and reactions across a variety of contexts. This observation highlights an
important boundary condition: persona-based simulation is most effective when users
provide meaningful signals in their language.

At the same time, this limitation also points to future opportunities. Social media
posts are only one source of qualitative information. In principle, personas could be
augmented with additional data sources, such as open-ended and qualitative sur-
vey responses, diaries, or product reviews. Extending persona construction beyond
social media represents a promising direction for building more comprehensive and
structured representations of individuals.

3.4 Opinion questions, factual judgments, and model guardrails
While SPIRIT performs well on many attitudinal questions, we also identify cases
where it diverges from survey benchmarks. In particular, two types of items are more
prone to mismatch. First, the model is more likely to diverge on items that go beyond
subjective opinion and instead ask respondents to make evaluative judgments, espe-
cially when those judgments carry a strong moral or quasi-factual character. On these
items, the simulated responses tend to be highly skewed in ways that do not match
the observed survey distributions. Second, for questions that ask respondents to antic-
ipate downstream consequences and therefore require causal reasoning, the simulated
responses tend to be more consistently extreme and directional than those observed
in human survey data.

These patterns suggest that large language models do not always act purely as
simulators of individual belief states. Instead, they may default to responses shaped
by built-in safety constraints, normative assumptions, or implicit notions of “correct”

12

---

<!-- PAGE 13 -->

behavior. In these cases, the model behaves less like a representation of a specific
human respondent and more like a helpful assistant, optimized to produce socially
acceptable or morally justified answers.

This distinction highlights a fundamental tension in persona-based simulation. For
research purposes, the goal is not to predict what a population should think, nor to
output normatively desirable responses, but to approximate how individuals actually
think and react. Even when explicitly instructed to “be” a particular person, LLMs
may override a persona in situations involving strong moral priors or factual judg-
ments. Future work should examine how to represent the internal contradictions that
characterize individuals, including socially undesirable traits, while also accounting
for the built-in constraints that LLMs impose on harmful speech and behavior.

3.5 Extending persona banks through agentic capabilities

Finally, our results point toward a broader research agenda in which persona banks are
embedded within agentic systems. To enable simulation of responses to newly unfold-
ing events, we augment persona-based reasoning with selective information retrieval,
allowing agents to access contemporaneous context when necessary. This design paral-
lels recent advances in agent frameworks that integrate search, tool use, and external
observation [37].

More broadly, persona-based agents need not remain respondents. Future work
could explore multi-agent interactions in which personas deliberate, exchange informa-
tion, or influence one another, offering a controlled environment for studying opinion
formation, polarization, and social dynamics. When combined with probability-based
weighting and structured personas, such systems may provide a valuable experimental
testbed for population-level reasoning under well-defined assumptions.

4 Methods

4.1 Data

4.1.1 Panel recruitment and consented account linkage

We partnered with the Ipsos KnowledgePanel, a nationally recruited, probability-
based survey panel (i.e., whose members represent the U.S. population). Panelists
were screened for active usage of Twitter/X and Reddit and invited to consent to
the retrieval of their posts. Consenting participants provided their handles on either
or both platforms, which enabled the collection of their publicly available posts and
linkage to their survey responses. From consenting panelists, we received handles for
1,410 Twitter/X users and 893 Reddit users, including 452 individuals who provided
accounts on both platforms.

Importantly, although panelists provided handles, not all of the submitted handles
were valid or retrievable at the time of data collection. For example, some handles
contained typographical errors, were suspended/deleted, or pointed to accounts that
were private or otherwise inaccessible via the platform APIs. We therefore retained
only handles that could be associated with (i) an account and (ii) publicly accessible
content that could be retrieved through the APIs.

13

---

<!-- PAGE 14 -->

4.1.2 Post collection and linkage to survey responses

For each valid handle, we collected all publicly available posts retrievable via the
platform’s APIs, subject to platform access constraints at the time of collection. These
posts were linked to their attitudes and preferences maintained by Ipsos, enabling the
construction and evaluation of the individualized personas (Appendix C).

This design thus supports persona-based simulation evaluation by providing: (i)
respondent-level ground truth for opinions and attitudes (via Ipsos survey responses
collected independently of this work), (ii) longitudinal, historical text traces for per-
sona construction (via all public posts), and (iii) a probability-based sampling frame
with survey weights, enabling simulation fidelity to be assessed not only at the indi-
vidual level but also in terms of population-calibrated aggregates benchmarked to the
U.S. adult population.

4.2 SPIRIT framework

Fig. 3 Overview of the SPIRIT framework. A probability-based sample from the Ipsos Knowl-
edgePanel is linked to respondents’ social media accounts, and their historical posts are collected to
infer structured user personas with a painter model. These inferred personas form a persona bank
that serves as digital twins for Stage 2 reasoning, where a reasoner model simulates responses to
downstream tasks such as survey items. The simulated responses are then weighted to produce U.S.
population-level estimates.

We propose SPIRIT (Semi-structured Persona Inference and Reasoning for
Individualized Trajectories), a two-stage framework for grounding LLM-based simula-
tion in interpretable, semi-structured, and faithful personas inferred from social media
traces. As illustrated in Figure 3, SPIRIT comprises (i) a Painter module that infers

14

---

<!-- PAGE 15 -->

a multi-dimensional persona profile from a user’s social media posts, and (ii) a Rea-
soner module that prompts an LLM on the inferred persona to simulate structured
responses for downstream tasks (e.g., survey-style items).

4.2.1 Inputs and persona artifacts

For each user, the system consumes a single concatenated document consisting of all
available historical posts from Reddit and Twitter/X, ordered by timestamp (each
post is associated with its original posting time). The Painter outputs (detailed scheme
can be seen in Appendix G): (i) a semi-structured persona profile encoded as a
JSON (JavaScript Object Notation) object that captures psychologically and socially
meaningful attributes (e.g., traits, world beliefs, values/identities, attitudes), together
with uncertainty annotations; and (ii) a narrative persona that summarizes the
profile in readable third-person form.

In external survey experiments, demographic attributes (e.g., age, gender, race,
party identification) are loaded from user profiles and provided as supplementary
content during downstream prompting.

4.2.2 Painter: semi-structured persona inference from posts

Persona schema.

The persona profile follows a fixed schema that is designed to be (i) multi-dimensional,
covering traits (Big Five), worldview beliefs, values/identities, and domain attitudes,
and (ii) auditable, with explicit uncertainty scores and brief justifications. The schema
is implemented as a typed data model to enforce structural consistency across users.

Inference procedure.

Given a user’s posts, the Painter infers persona attributes by synthesizing recurring
linguistic signals (e.g., affect, self-references, moral language, expressed preferences,
and stance patterns) into the persona schema. To reduce overinterpretation, Painter
is instructed to treat all inferences as probabilistic and to express low confidence
when evidence is weak. Prompt templates and an illustrative example are provided in
Appendix G.2.

4.2.3 Reasoner: persona inference for downstream tasks

Task formulation.

The Reasoner answers downstream questions by prompting an LLM with the inferred
persona (and demographic attributes when available). For each question, the output
includes: (i) a selected response option (value/label), (ii) a categorical confidence rat-
ing, and (iii) a brief textual rationale grounded in persona evidence. This formulation
supports survey-style prediction enriched with qualitative evidence, as well as model
uncertainty when persona signals are ambiguous.

15

---

<!-- PAGE 16 -->

4.2.4 Calibration weights via raking to Census/ACS margins

The persona bank requires respondents to (i) have a social media account, (ii) have
ever posted, and (iii) consent to link. Because not everyone in the panel necessar-
ily conforms to these requirements, the resulting sample might deviate from the U.S.
adult population in basic composition. To reduce this type of selection bias, we con-
struct weights that calibrate the persona-bank marginals to external U.S. population
benchmarks.

Benchmarks.

We use marginal distributions from U.S. Census and ACS releases as targets: gender
(2020 Census), race/ethnicity (2020 Census), region (2020 Census), and age and edu-
cation (ACS 2022; education among adults 25+). We additionally include the panel
variable corresponding to the candidate for whom the respondent voted in the 2024
U.S. presidential election, using the election results (three-category vote preference)
as a calibration margin.

Variables and preprocessing.

Weights are computed for respondents included in the persona bank. We rake on six
margins: PPGENDER, PPEDUC5, PPETHM, PPREG4, age group, and candidate2024. Age
is discretized into four groups (18–29, 30–44, 45–64, 65+).

Raking procedure.

We apply iterative proportional fitting (raking) to match each sample margin to its
target [38]. Starting from equal base weights w(0)
i = 1, we iterate over margins and
update weights by multiplying an adjustment factor for the respondent’s category:

wi ← wi ×

Tv,c
ˆPv,c

,

where Tv,c is the benchmark proportion for category c of variable v, and ˆPv,c is the
current weighted sample proportion for that category. We cycle through all mar-
gins repeatedly until convergence (maximum absolute adjustment tol < 0.001) or a
maximum of 50 iterations.

Normalization and use.
After raking, we rescale weights to have mean 1 within the persona bank, wi ← wi/ ¯w,
so weighted estimates preserve the sample’s effective scale. These weights are then
used to compute weighted population-level aggregates of simulated survey responses
from the persona bank. After normalization (mean = 1), the raking weights show
moderate dispersion: SD = 1.32, median = 0.63 (IQR: 0.30–1.23), with a minimum of
0.012 and a maximum of 14.42 (n = 1517).

16

---

<!-- PAGE 17 -->

4.3 Position-weighted user-level response composite score

To summarize each respondent’s overall response pattern across the survey, we convert
item-level outputs into a single user-level composite score. Let i index users and q ∈
{1, . . . , Q} index survey items, where Q = 52 in the main analysis. Each item has an
inferred numeric response ˆyiq (and, for human benchmarks, an observed self-report
yiq).

We first assign each question a deterministic position weight based on its location
in the survey sequence. In implementation, we take the set of unique question IDs
appearing in the analysis data, order them according to the survey sequence used in
the questionnaire, and assign weights wq ∈ {1, . . . , Q} so that earlier items receive
smaller weights and later items receive larger weights:

We then compute the position-weighted mean for each user:

wq = q.

¯ˆy pos
i =

(cid:80)Q

q=1 wq ˆyiq
(cid:80)Q
q=1 wq

.

We apply the same transformation to the human benchmark responses:

¯y pos
i =

(cid:80)Q

q=1 wq yiq
(cid:80)Q
q=1 wq

.

(1)

(2)

(3)

This composite score is fully deterministic and model-agnostic. Because later items
receive larger weights, the summary retains information about the survey order-
ing while yielding a compact scalar representation of each user’s 52-item response
sequence. In the empirical analysis, we compute ¯ˆy pos
for each model and experimen-
tal condition and compare its distribution to the corresponding distribution of ¯y pos
among human respondents.

i

i

4.4 External survey stress tests with timely events

Motivation and topics.

To evaluate whether persona-conditioned simulation can handle both stable attitudes
and time-sensitive information needs, we constructed external survey item sets span-
ning four widely discussed topics at the time of writing: abortion, the Epstein files, U.S.
actions related to Venezuela, and immigration policy. The Epstein-file and Venezuela-
action conditions were treated as time-sensitive cases where events may plausibly
post-date model training (i.e., will not be included in the training data).

Runtime stack.
Generation is performed through a locally deployed, OpenAI-compatible vLLM end-
point, using google/gemma-3-27b-it as the base model. For time-sensitive conditions,

17

---

<!-- PAGE 18 -->

the pipeline incorporates a web search component (i.e., Tavily, which is configured via
a search backend) to obtain up-to-date context before answering.

4.4.1 Time-sensitive protocol: persona-guided information

acquisition

For time-sensitive topics, we use a lightweight information acquisition protocol. The
model first elicits the persona’s pre-existing impressions, then generates persona-
consistent search queries and summarizes retrieved information, and finally answers
survey items conditioned on both persona and the synthesized context. This design
separates prior beliefs from newly acquired context, allowing us to examine whether
access to recent information changes inferred responses in a direction consistent with
the persona.

4.4.2 Stable-attitude protocol: direct persona-conditioned answers

For attitudes often treated as crystallized (e.g., on topics such as abortion and
immigration policy), the model answers directly without external search, producing
survey-style responses conditioned only on persona and demographics.

Appendix materials.

Full prompt templates, schema specifications, and example model inputs/outputs for
both Painter and Reasoner are provided in Appendix G.

Acknowledgements. We thank the U.S. Census Bureau for supporting this
research. We also thank Ipsos for providing access to survey data and for their support
of the external benchmarking component.

Declarations

• Funding. The author(s) disclosed receipt of the following financial support for the
research, authorship, and/or publication of this article: This work was supported
by the U.S. Census Bureau under CB20ADR0160002.

• Conflict of interest / Competing interests. The authors declare no competing

interests.

• Ethics approval and consent to participate. This study was conducted under
IRB approval (HUM00259279), with informed consent from all participants. This
study uses observational, user-generated content from public social media platforms
(Reddit and Twitter/X) and does not involve any interaction or intervention with
human participants. Because the content was not collected with consent for redistri-
bution, we treat both the underlying posts and derived persona artifacts as sensitive
research materials and adopt a data-minimization approach in dissemination.

• Consent for publication. We do not publish raw social media posts, user-
names/handles, or direct identifiers. Any illustrative examples in the manuscript
are paraphrased to reduce re-identification risk.

• Data availability. To balance transparency with privacy, we will release (i) aggre-
gated results reported in the paper and (ii) data products for the external survey

18

---

<!-- PAGE 19 -->

benchmarking component, including the survey question sets, response options, and
item-level model outputs used for comparison. We do not publicly release the under-
lying raw social media posts or full persona artifacts (semi-structured persona JSON
and narrative personas), as these may contain personally identifiable information
or enable re-identification through linkage. Researchers who require access to per-
sona artifacts for verification or extension may contact the corresponding author to
discuss controlled-access arrangements.

• Materials availability. All non-sensitive study materials (e.g., external survey
instruments, mapping tables, and evaluation scripts) will be made available with
the public release of the external survey component. Materials that directly contain
or reconstruct user-level social media traces will be withheld from public release.
• Code availability. Code for the SPIRIT pipeline (Painter and Reasoner modules),
the external survey study, and the analysis scripts will be released upon acceptance
of the manuscript. The release will include documentation sufficient to reproduce
the reported external survey experiments using the publicly available materials, and
guidance for running persona-based simulations under controlled data access.

Appendix A Ipsos KnowledgePanel Participant

Demographic Distribution

This section details the demographic composition of the participants drawn from the
Ipsos KnowledgePanel for the Twitter and Reddit arms of the study (see Table A1).
The sample distribution reflects several key characteristics of social media users
that deviate from U.S. Census benchmarks. Notably, both samples are more male-
dominated (approx. 61%) and highly educated (over 50% with a Bachelor’s degree)
than the general population. Political ideology is skewed toward the left, particularly
on Reddit, where 58.8% of participants identify as some level of Liberal. Additionally,
the Reddit sample is significantly younger than the Twitter sample, with 76.1% of
respondents falling under the age of 45, compared to 56% for Twitter.

Appendix B Experimental Environment and

Computational Cost

B.1 Computing Environment

All framework-level experiments were conducted on a single-node, multi-GPU system
equipped with 8 NVIDIA H100 GPUs (80GB memory each). Model infer-
ence was deployed using vLLM with bfloat16 (BF16) precision, enabling efficient
batched inference while maintaining numerical stability for long-context inputs.

The system was configured to support long input sequences required for persona
inference from social media histories. No gradient computation or model fine-tuning
was performed; all experiments were conducted in inference-only mode.

19

---

<!-- PAGE 20 -->

Table A1 Demographic Characteristics of Twitter and Reddit Participants

Twitter (N = 1, 031) Reddit (N = 774)

Characteristic

Gender
Male
Female

Age Category

18–29
30–44
45–60
60+

Race/Ethnicity

White, Non-Hispanic
Hispanic
Black, Non-Hispanic
2+ Races, Non-Hispanic
Other, Non-Hispanic

Education

Bachelor’s degree or higher
Some college / Associate’s
HS Graduate / GED
No HS diploma

Urbanicity
Urban
Suburban
Rural

Political Ideology

Liberal
Moderate
Conservative
Refused

n

628
403

192
386
290
163

665
146
113
54
53

545
285
150
28

430
443
157

437
275
306
13

%

60.9
39.1

18.6
37.4
28.1
15.8

64.5
14.2
11.0
5.2
5.1

52.9
27.6
14.5
2.7

41.7
43.0
15.2

42.4
26.7
29.7
1.3

n

%

475
299

197
392
135
50

525
108
45
46
50

427
205
74
21

346
330
97

455
189
124
6

61.4
38.6

25.5
50.6
17.4
6.5

67.8
14.0
5.8
5.9
6.5

55.2
26.5
9.6
2.7

44.7
42.6
12.5

58.8
24.4
16.0
0.8

B.2 Token-Level Accounting

To provide a transparent and model-agnostic estimate of computational usage, we
report aggregated input and output token counts rather than wall-clock time or GPU-
hours. This choice reflects the fact that inference cost is primarily driven by token
volume and sequence length, while runtime depends on deployment-specific factors
such as batching strategy and hardware utilization.

Table B2 summarizes total token usage across platforms for framework execution.

Table B2 Aggregated token usage by
platform

Platform Input tokens Output tokens
12,650,506
Reddit
9,715,741
Twitter

41,924,612
77,077,952

20

---

<!-- PAGE 21 -->

Input tokens include persona inference prompts as well as persona-conditioned
reasoning prompts. Output tokens correspond to structured persona representations
and downstream generated responses.

B.3 Cost Estimation and Variability

We intentionally do not report GPU-hours or exact cost. Token-level account-
ing provides an order-of-magnitude indication of computational scale that remains
comparable across hardware and deployment environments.

Actual runtime and cost may vary substantially depending on batching efficiency,
concurrency, and hardware utilization. Moreover, the framework incorporates struc-
tured output validation using a schema-based mechanism implemented with Pydantic,
which introduces controlled variability in generation cost.

Specifically, model outputs are validated against a predefined JSON schema, with
a retry mechanism capped at ten attempts per prompt. In practice, the number of
retries required depends strongly on model capability: higher-capacity models exhibit
substantially higher compliance rates with the schema and therefore require fewer
retries. As a result, the reported token counts should be interpreted as coarse-grained
estimates rather than exact execution costs.

These sources of variability reflect engineering trade-offs rather than conceptual

limitations of the proposed framework.

B.4 Practical Implications

Despite these sources of variability, the overall computational footprint of the frame-
work remains well within the reach of typical academic research environments. Because
persona inference is performed once per user and then reused for multiple downstream
tasks, the cost of persona construction can be amortized across analyses and scenarios.
Importantly, the framework does not rely on model fine-tuning or large-scale retrain-
ing, making population-level experiments feasible without prohibitive computational
overhead.

A key practical constraint is the reliability of persona construction. Although we
implement a retry mechanism (up to ten attempts) to enforce schema-compliant out-
puts, smaller models (Gemma-3-4B and LLaMA-3.1-8B) still fail to produce valid
persona representations for a nontrivial fraction of users. These failures propagate to
downstream reasoning and reduce overall performance, suggesting a minimum model
capacity requirement for robust deployment. Accordingly, we report results from these
smaller models only as a reference point; they should not be interpreted as definitive
evidence about the framework’s performance.

Appendix C Data Dictionary and Variable

Definitions

This section details the complete set of survey questions collected from Ipsos Knowl-
edgePanel and used in the evaluation (see Table C3). The table below maps the

21

---

<!-- PAGE 22 -->

internal variable identifiers (e.g., pph10221) to the verbatim question text presented
to participants and the available response options.

Table C3: Survey Questions and Response Options Dictionary

Variable

QFLAG

Question Text

QFLAG

pph10221

Q37: Do you NOW smoke cigarettes?

ppsi1916

pph21906

Q210: Do you currently use mari-
juana. . . ?

Q110: How often do you think
vaccines have dangerous side effects?

Response Options

1: Qualified
2: Terminated
3: Partial
4: Non-responder

1: Every day
2: Some days
3: Not at all

1: Every day
2: Some days
3: Not at all

1: Never
2: Rarely
3: Sometimes
4: Often
5: Very often

pph21908

Q130: Overall do you think

1: The benefits... outweigh the risks
2: The risks... outweigh the benefits

pph20030

Q49: Overall, how do you rate the
quality of medical care received from
your regular doctor in the past 12
months?

pph20031

Q50: Overall, how satisfied are you
with your healthcare coverage?

1: Excellent
2: Very good
3: Good
4: Fair
5: Poor
6: Have not seen...
7: Do not have...

1: Very satisfied
2: Moderately satisfied
3: Slightly satisfied
4: Not satisfied

vote2024

candidate2024

QPID600f: Did you happen to vote in
the November 2024 elections for the
U.S. President and Congress?

1: Yes
2: No

QPID600g: Which candidate did
you vote for in the 2024 Presidential
election?

1: Kamala Harris (Democrat)
2: Donald Trump (Republican)
3: Another candidate...

Continued on next page

22

---

<!-- PAGE 23 -->

Variable

Question Text

Response Options

Table C3 – continued from previous page

urb sub rur

Urban/Suburban/Rural

ppcm1301

GOVEMP1: Employer type

E140

E140: Which category best describes
your level of employment?

1: Urban
2: Rural
3: Suburban

1: Government
2: Private-for-profit company
3: Non-profit organization...
4: Self-employed
5: Working in family business

1: Entry level
2: Experienced (non-manager)
3: Manager/Supervisor...
4: Executive...

MilVet 1

MilVet 2

MilVet 3

pppa1640

DOV: Current Service Member

1: Current Service Member

DOV: Veteran Service Member

1: Veteran Service Member

DOV: Non-Military

1: Non-Military

Q254: Have you ever been a member
of the Reserve or National Guard?

1: Yes
2: No

pppa1648

Q26: What is your religion?

1: Catholic
2: Evangelical/Protestant...
3: Jehovah’s Witness
4: LDS (Mormon)
5: Jewish
6: Islam/Muslim
7: Orthodox
8: Hindu
9: Buddhist
10: Unitarian
11: Other Christian
12: Other non-Christian
13: No religion

ppp20197

votereg now

QEG22: Are you a citizen of the
United States?

1: Yes
2: No

Are you currently registered to vote in
the U.S.?

1: Yes, registered
3: No, not registered
4: Not sure
5: No, not eligible

Continued on next page

23

---

<!-- PAGE 24 -->

Variable

ppfs1482

Table C3 – continued from previous page

Question Text

Response Options

Q108: Where do you think your credit
score falls

1: Very poor
2: Poor
3: Fair
4: Good
5: Excellent
6: Don’t know

1: Excellent
2: Very good
3: Good
4: Fair
5: Poor

pph10001

Q1: In general, would you say your
health is. . .?

pph11301

ppp10035

Q25 1: Are you a caregiver for one or
more children under the age of 18?

1: Yes
2: No

Q16: In general, how interested are
you in politics and public affairs?

ppcm0160

Q26: Occupation (detailed) in current
or main job

ppfsasset

Q22: Approx total amount of house-
hold savings and investable assets?

ppc21505

CU40: How concerned are you about
providing personal information over
the internet?

1: Very interested
2: Somewhat interested
3: Slightly interested
4: Not at all interested

1: Management
2: Business/Financial...
(See full list in data source for codes
3-35)
1: Under $25,000
2: $25k - $49,999
3: $50k - $99,999
4: $100k - $249,999
5: $250k - $499,999
6: $500k - $999,999
7: $1M - $1.9M
8: $2M or more
9: Not sure

1: Not at all concerned
2: Slightly concerned
3: Somewhat concerned
4: Very concerned

E104 RET

E104: Do any of the following
currently describe you? ... [Retired]

1: Yes
2: No

Continued on next page

24

---

<!-- PAGE 25 -->

Variable

Question Text

Response Options

Table C3 – continued from previous page

E104 STUD

E104: ... [A student]

E104 STAYHOM

E104 INTERN

E104: ... [A stay-at-home spouse or
partner]

E104: ... [Unpaid job/internship/vol-
unteer]

E104 FREELANC

E104: ... [Freelancer/independent
contractor]

pph10301-7

Q39/Q40: Alcohol consumption (Beer,
Wine, Liquor)

pph21901-5

Q100: Vaccine attitudes (Series)

1: Yes
2: No

1: Yes
2: No

1: Yes
2: No

1: Yes
2: No

0: No
1: Yes

1: Do not agree
2: Somewhat agree
3: Agree
4: Strongly agree

1: Do not agree
2: Somewhat agree
3: Agree
4: Strongly agree

ppc21607

pph1*

ppm2223*

ppp20072

CU44: I use social network sites to
communicate with others more than
email...

Q19/Q19a: Medical/Mental Health
Conditions (ADHD, Anxiety, Depres-
sion, etc.)

0: No
1: Yes (Condition present)

Q9: News Sources (TV, Paper,
Internet, Radio, Social Media)

Q27: How often do you attend
religious services?

ppp22210

Q34: Household gun ownership

ppp22211

Q36: Personal gun ownership

25

0: No
1: Yes

1: More than once a week
2: Once a week
3: 1-2 times a month
4: Few times a year
5: Once a year or less
6: Never

1: Yes
2: No

1: Yes
2: No

Continued on next page

---

<!-- PAGE 26 -->

Variable

Question Text

Response Options

Table C3 – continued from previous page

ppm22229

Q10: How closely do you follow
politics...?

1: Very closely
2: Fairly closely
3: Not very closely
4: Not at all closely

vote2020

candidate2020

Did you happen to vote in the
November 2020 elections...?

1: Yes
2: No

Which candidate did you vote for in
the 2020 Presidential election?

1: Joe Biden (Democrat)
2: Donald Trump (Republican)
3: Another candidate

partyid7

DERIVED: Political party affiliation
(7 categories)

ppp10012

Q11: In general, do you think of
yourself as...

PPEDUCAT

Education (4 Categories)

PPETHM

Race / Ethnicity

PPGENDER

Gender

26

1: Strong Rep
2: Not Strong Rep
3: Leans Rep
4: Undecided/Ind/Other
5: Leans Dem
6: Not Strong Dem
7: Strong Dem

1: Extr. liberal
2: Liberal
3: Slightly liberal
4: Moderate
5: Slightly conservative
6: Conservative
7: Extr. conservative

1: No HS diploma
2: HS grad
3: Some college/Assoc
4: Bachelor’s or higher

1: White, Non-Hisp
2: Black, Non-Hisp
3: Other, Non-Hisp
4: Hispanic
5: 2+ Races, Non-Hisp

1: Male
2: Female

Continued on next page

---

<!-- PAGE 27 -->

Variable

PPREG4

Table C3 – continued from previous page

Question Text

Response Options

Region 4 - Based on State of Resi-
dence

PPRENT

Ownership Status of Living Quarters

PPMSACAT

MSA Status

PPEDUC5

Education (5 Categories)

PPINC7

Household Income

PPMARIT5

Marital Status

PPEMPLOY

Current Employment Status

PPHOUSE4

Housing Type

1: Northeast
2: Midwest
3: South
4: West

1: Owned
2: Rented
3: Occupied w/o rent

0: Non-Metro
1: Metro

1: No HS
2: HS grad
3: Some college
4: Bachelor’s
5: Master’s or higher
1: Less than $10k
2: $10k-$24,999
3: $25k-$49,999
4: $50k-$74,999
5: $75k-$99,999
6: $100k-$149,999
7: $150k+

1: Married
2: Widowed
3: Divorced
4: Separated
5: Never married

1: Full-time
2: Part-time
3: Not working

1: 1-family detached
2: Condo/townhouse
3: 2+ apartments
4: Other

Appendix D Unpacking response confidence and

diversity

To further understand the behavioral differences between demographic persona and
SPIRIT persona conditioning, we conduct a set of diagnostic analyses focusing on

27

---

<!-- PAGE 28 -->

response confidence, answer diversity, and their relationship to inference accuracy. All
analyses in this section are conducted on GPT-5-mini, which represents a stable and
a well-performing model in the main experiments.

D.1 Response confidence distribution

Figure D1A compares the distribution of response-level confidence categories across
conditions. Demographic persona conditioning is dominated by low-confidence
responses, whereas SPIRIT persona conditioning produces substantially higher pro-
portions of medium- and high-confidence responses.

This pattern is expected. Under demographic persona conditioning, inference relies
on sparse, population-level signals that are often insufficient to support confident
predictions at the individual level. By contrast, SPIRIT persona conditioning incorpo-
rates non-demographic attributes inferred from user-generated text, providing richer
contextual grounding and enabling more confident responses.

28

---

<!-- PAGE 29 -->

Fig. D1 Diagnostic analyses of response confidence and diversity for GPT-5-mini. A, Distribution
of response-level confidence categories under demographic persona and SPIRIT persona conditioning.
B, Distribution of response entropy per question, where lower entropy indicates more fixed or biased
response tendencies. C, Relationship between user-level accuracy and the number of low-confidence
responses per user, shown separately for each condition with linear trend lines.

D.2 Response diversity and answer tendency

We next examine response diversity using entropy computed at the question level
(Figure D1B). To quantify response diversity, we compute Shannon entropy at the
question level. For each question, we collect the inferred categorical responses across

29

---

<!-- PAGE 30 -->

users and estimate the empirical response distribution. Let p(v) denote the proportion
of users assigned response value v for a given question. Response entropy is defined as

H = −

(cid:88)

v

p(v) log2 p(v),

where higher entropy indicates greater variability in inferred responses, and lower
entropy reflects more concentrated or deterministic response patterns. Entropy is com-
puted only for questions with more than one valid inferred response. Lower entropy
indicates more fixed or biased response tendencies, whereas higher entropy reflects
greater variability across users.

Demographic persona conditioning exhibits substantially lower response entropy,
indicating a strong tendency toward fixed or default answers. In practice, this manifests
as systematic preference for negative responses (e.g., answering “No” to behavioral or
health-related questions), which compresses the range of possible inferred values. In
contrast, SPIRIT persona conditioning yields higher entropy distributions, suggesting
that persona-based inference better preserves heterogeneity across users and questions.

D.3 Low-confidence responses and user-level accuracy

Finally, we analyze the relationship between inference accuracy and the number of low-
confidence responses per user (Figure D1C). Under demographic persona conditioning,
users with larger numbers of low-confidence responses exhibit a clearer degradation
in accuracy. This trend reflects the cumulative effect of uncertain, weakly grounded
inferences.

By comparison, SPIRIT persona conditioning substantially reduces the prevalence
of low-confidence responses and weakens the negative association between low con-
fidence and accuracy. This suggests that persona-based inference not only improves
overall performance but also stabilizes reasoning at the user level by reducing reliance
on uncertain guesses.

These analyses clarify why demographic persona conditioning can appear compet-
itively accurate on some attributes while still producing degenerate response patterns.
Demographic persona inference tends to rely on population-level shortcuts, leading
to low-confidence, low-diversity predictions. SPIRIT persona conditioning mitigates
these issues by grounding inference in non-demographic attributes, resulting in more
confident, diverse, and behaviorally plausible responses.

Appendix E Subtentive questions

E.1 Epstein files questions

The following questions (Table E4) are used to measure public attitudes toward the
release of the Jeffrey Epstein investigation files and potential involvement of pub-
lic figures. Question wording closely follows contemporary public opinion surveys
conducted in late 2025 to early 2026.

30

---

<!-- PAGE 31 -->

Table E4 Epstein files survey questions and response options

Question ID

Question wording and response options

EPSTEIN FILES
RELEASE

TRUMP EPSTEIN
INVOLVEMENT

Should the U.S. government release all of its files from the
investigation of Jeffrey Epstein?
(1) Yes

(98) Not sure

(2) No

Do you think that Donald Trump was involved in crimes
allegedly committed by Jeffrey Epstein?
(1) Yes

(98) Not sure

(2) No

E.2 Abortion attitude question

Attitudes toward abortion are measured using a standard four-category item com-
monly employed in U.S. public opinion surveys (Table E5).

Table E5 Abortion attitude survey question

Question ID

Question wording and response options

ABRTLGL

Do you think abortion should be:
(1) Legal in all cases
(2) Legal in most cases
(3) Illegal in most cases
(4) Illegal in all cases

E.3

Immigration policy battery

Attitudes toward immigration are measured using a policy battery. For each item,
respondents are asked how much they favor or oppose the proposed policy (Table E6).
Response categories for all immigration items are: (1) Strongly favor, (2) Somewhat
favor, (3) Somewhat oppose, (4) Strongly oppose, (98) Don’t know, (99) Refused.

E.4 Venezuela military action questions

The following questions (Table E7) probe public attitudes toward U.S. policy
and potential military action involving Venezuela. These items are adapted from
contemporaneous polling instruments.

Appendix F Effects of Social Media Trace Quality

on Persona-Based Simulation Accuracy

This appendix reports additional analyses examining how the quality and informative-
ness of social media traces relate to the accuracy of SPIRIT-based persona simulations,
as well as a full category-level breakdown of performance across all 81 survey questions
using GPT-5-Mini.

31

---

<!-- PAGE 32 -->

Table E6 Immigration policy battery items and response categories

Item ID

BRDER
REF

SKILL
DIV

LABOR

DEPORT

STUD

MARRY

Policy description

Improving security along the country’s borders
Admitting more civilian refugees from countries where
people are trying to escape violence and war
Legally admitting more high-skilled immigrants
Legally admitting immigrants from all over the world
to ensure the nation’s immigrant population is diverse
Legally admitting immigrants who can fill labor short-
ages
Enforcing mass deportations of immigrants living in the
country illegally
Allowing international students who receive a college
degree in the U.S. to legally work and stay in the coun-
try
Allowing undocumented immigrants to legally work and
stay in the country if they are married to a U.S. citizen

F.1 Trace Quantity and Persona Confidence as Proxies for

Information Quality

Figure F2 presents two complementary analyses linking characteristics of users’ social
media traces to downstream prediction accuracy.

Panel A relates prediction accuracy to the total amount of textual information
available for each individual, measured as the log-transformed total number of charac-
ters across all observed posts. A positive association is observed for both Twitter and
Reddit users: individuals who contribute longer or more extensive social media traces
tend to yield more accurate persona-based predictions. This pattern is consistent with
the intuition that richer behavioral signals allow the persona inference module to
estimate latent attributes more precisely, thereby improving simulation fidelity.

Panel B examines prediction accuracy as a function of the number of low-confidence
persona attributes inferred for a given individual. Each persona dimension produced
by SPIRIT is accompanied by a confidence score; attributes falling below a prede-
fined threshold are flagged as low-confidence. A clear negative relationship emerges: as
the number of low-confidence attributes increases, simulation accuracy declines. This
pattern holds across platforms and mirrors the result in Panel A from the opposite
direction—when less information can be reliably inferred from the trace, downstream
predictions degrade.

Together, these results show that both trace quantity and persona-level inferen-
tial confidence serve as meaningful proxies for information quality, and that SPIRIT
responds to variation in observational signal in theoretically expected ways.

32

---

<!-- PAGE 33 -->

Table E7 Venezuela-related survey questions

Question ID

Question wording and response options

VZ Q12

VZ Q13

VZ Q14

VZ Q15

VZ Q16

VZ Q17

VZ Q18

VZ Q19

Has the Trump administration clearly explained what the
U.S. intends to do regarding Venezuela?
(1) Yes

(3) Not sure

(2) No

Does the Trump administration need to explain what the
U.S. intends to do regarding Venezuela?
(1) Yes

(3) Not sure

(2) No

How much of a threat do you think Venezuela is to the United
States?
(1) Major threat
Not sure
Would you approve or disapprove of potential U.S. military
action in Venezuela?
(1) Approve

(2) Minor threat

(3) Not a threat

(2) Disapprove

(3) Not sure

(4)

Should President Trump need congressional approval before
taking military action in Venezuela?
(1) Yes

(3) Not sure

(2) No

Do you approve or disapprove of the current military attacks
on boats suspected of bringing drugs from Venezuela?
(1) Approve

(2) Disapprove

(3) Not sure

Should the administration show evidence that there are
drugs on the boats being attacked?
(1) Yes

(3) Not sure

(2) No

Do you think U.S. military action in Venezuela would
decrease the amount of drugs coming into the U.S.?
(1) Yes

(2) No change

(4) Not sure

(3) Increase

Fig. F2 Relationship between social media trace quality and prediction accuracy. (A)
Accuracy as a function of the log-transformed total number of characters across all observed posts
for each individual. (B) Accuracy as a function of the number of low-confidence persona attributes
inferred by SPIRIT. Points represent individual users, colored by platform (Twitter vs. Reddit). Solid
lines indicate linear trends.

33

---

<!-- PAGE 34 -->

Table F8 Prediction accuracy by survey question category. Reported values are mean
exact-match accuracy, standard deviation, number of questions, total responses, and off-by-one
rate for GPT-5-Mini across all 81 survey items. Categories are ordered from worst to best
average accuracy.

Category
Finances
Technology
Religion
Politics / Media
Alcohol
Vaccines
Demographics
Guns
Employment
Health
Voting
Military

Avg. Acc.
0.245
0.257
0.483
0.504
0.569
0.594
0.677
0.726
0.738
0.764
0.832
0.929

Std. Dev. # Questions Responses Off-by-one

0.430
0.437
0.500
0.500
0.495
0.491
0.468
0.446
0.440
0.425
0.374
0.257

3
2
2
11
8
7
12
2
9
16
5
4

5,185
3,570
3,580
19,388
11,432
12,220
21,669
3,584
14,752
26,610
8,169
6,547

0.407
0.394
0.152
0.388
–
0.309
0.091
0.274
0.129
0.341
0.103
0.027

F.2 Performance Across Survey Question Categories

To complement the individual-level quality analysis, we report performance disaggre-
gated by question category across the full set of 81 survey items. Table F8 summarizes
mean exact-match accuracy, standard deviation, and off-by-one rates for each category.
Substantial heterogeneity is observed across domains. Categories involving
abstract, private, or infrequently expressed attributes (e.g., finances and technology)
exhibit the lowest accuracy and highest variance. In contrast, domains associated
with stable self-concepts and repeated public expression—such as health, employ-
ment, voting, and military attitudes—show substantially higher accuracy and lower
dispersion.

These category-level patterns align with the trace-quality analysis above, reinforc-
ing the conclusion that persona-based simulation performs best when attitudes are
internally consistent and well-supported by observable discourse.

F.3 Summary

Across both individual- and category-level analyses, prediction accuracy scales sys-
tematically with the informativeness of social media traces. Persona confidence scores
provide a useful internal diagnostic of simulation reliability, while category-level perfor-
mance reflects theoretically grounded differences in attitude expression and stability.
Together, these results support the use of SPIRIT as a principled framework for
bridging organic digital traces and survey-based measurement.

F.4

Item-level deviations in the Venezuela questions

Table F9 and Table F10 compare the weighted distribution of responses from the
persona-conditioned virtual panel with contemporaneous CBS poll marginals for two
Venezuela-related items. These two items illustrate a recurring pattern: compared
to human respondents, LLM-based agents were less likely to select an unqualified,

34

---

<!-- PAGE 35 -->

low-engagement option (e.g., “not a threat” or “no change”) and instead allocated
more probability mass to analytically elaborated categories (e.g., “minor threat” or
“would increase drugs”). We interpret this as a deliberation bias: when prompted
to explain, simulated agents tend to treat questions as requiring causal analysis and
internally consistent justification, whereas survey respondents often rely on heuristics
or satisficing strategies.

Table F9 Venezuela Q14: perceived threat to the United
States. Weighted AI-agent responses versus CBS poll
marginals.

Response option Agents (%) CBS (%) Diff (pp)

Major threat
Minor threat
Not a threat

20.1
79.9
0.0

13
48
39

+7.1
+31.9
-39.0

For Q14 (Table F9), agents almost never selected “not a threat” (0%), a response
that accounts for 39% in the CBS poll. Instead, agents concentrated on “minor threat”.
Inspecting the generated rationales suggests that agents tended to (i) acknowledge
multiple indirect channels (e.g., regional instability, migration spillovers, transnational
crime) while (ii) rejecting the stronger framing of an existential or imminent threat.
This combination naturally pushes responses toward “minor threat” rather than “not
a threat”, even when the overall stance is closer to skepticism than alarmism.

Table F10 Venezuela Q19: whether U.S. military action would decrease drugs
entering the U.S. Weighted AI-agent responses versus CBS poll marginals.

Response option

Agents (%) CBS (%) Diff (pp)

Yes, would decrease drugs
No, would not change amount of drugs
Would increase drugs

39.6
11.8
48.6

37
56
7

+2.6
-44.2
+41.6

For Q19 (Table F10), the binary framing (“decrease” vs. “not decrease”) yielded
a closer match to the poll, but the three-category version shows a substantial redistri-
bution: agents rarely selected “no change” and instead shifted heavily toward “would
increase drugs.” The corresponding rationales frequently invoked systems-style argu-
ments (e.g., displacement/“balloon” effects, cartel adaptation, governance breakdown,
and instability-induced expansion of illicit markets). This reasoning is coherent, but
it likely overstates the degree of analytic engagement typical in survey response pro-
cesses, where respondents may interpret “no change” as a satisficing default or an
expression of general skepticism about policy efficacy without committing to a backfire
mechanism.

35

---

<!-- PAGE 36 -->

Interpretation.

Taken together, these deviations are consistent with a deliberation bias in LLM-
based panels: simulated respondents preferentially construct mechanistic explanations
and therefore avoid options that imply categorical dismissal (e.g., “not a threat”) or
minimal updating (e.g., “no change”) (the full reaosning summary can be seen in
Appendix F.5). In practice, this implies that matching human marginals may require
either (i) explicitly modeling satisficing/low-effort response styles in the Reasoner
prompt, or (ii) treating certain response categories as capturing heterogeneous human
heuristics that are not well represented by analytic, justification-seeking generation.

F.5 Consolidated reasoning patterns by item and response

option (Venezuela module)

To aid interpretability, we summarize the dominant reasoning patterns produced by
the simulated panel for each Venezuela item and each response option. For each ques-
tion, we group free-text rationales by the chosen answer category and then synthesize
the recurring themes into a short paragraph. The goal is not to reproduce verbatim
outputs, but to document the qualitative logic that most frequently accompanied each
response.

Venezuela Q12: Has the administration clearly explained the reasons for
the Venezuela actions?
Yes, has explained clearly. Rationales selecting “Yes” generally framed the admin-
istration’s messaging as clear and direct, emphasizing an unambiguous stance against
socialism and a straightforward objective of opposing the Maduro regime. These
responses highlighted a consistent rhetorical posture (e.g., firmness, anti-socialist fram-
ing, willingness to act) and interpreted any perceived ambiguity as arising from media
interpretation rather than from the administration’s communication.

No, has not explained clearly. Rationales selecting “No” converged on the view
that the administration relied on broad slogans and posturing without articulating a
coherent strategy. Respondents described the approach as vague, reactive, and lack-
ing concrete details about objectives, mechanisms, or end goals. In this framing, the
absence of an explicit plan and the perceived volatility of messaging were treated as
evidence that the reasons were not clearly explained.

Venezuela Q13: Should the administration explain the reasons to the
American people?
Yes, needs to explain. Responses selecting “Yes” treated potential military involve-
ment as a uniquely consequential decision that requires public justification and
democratic accountability. Rationales emphasized constitutional principles, oversight,
and the need for clarity about goals, risks, and an exit strategy. Many invoked histor-
ical caution regarding past U.S. interventions and rejected vague ideological framing
as insufficient for legitimizing force.

No, does not need to explain. Responses selecting “No” primarily appealed
to national-security discretion and executive authority. Rationales emphasized that

36

---

<!-- PAGE 37 -->

revealing strategy could undermine effectiveness by telegraphing intentions, and por-
trayed Congress and the media as slow, politicized, or prone to leaks. This cluster
valued decisiveness and secrecy over deliberation, framing transparency demands as
counterproductive in security contexts.

Venezuela Q14: Is Venezuela a threat to the United States?
Major threat. Rationales selecting “major threat” framed Venezuela as a proximate
national-security risk, frequently citing drug trafficking as the concrete mechanism
through which Venezuela could harm U.S. interests. Responses emphasized regional
spillovers (migration, criminal networks), geographic proximity, and the possibility of
hostile foreign influence. While socialism was often mentioned, it typically served as an
explanatory factor for state collapse rather than as the sole basis of threat perception.
Minor threat. Rationales selecting “minor threat” rejected an existential framing
while still acknowledging serious problems. Venezuela was described as primarily a
humanitarian crisis and a source of indirect regional instability rather than a direct
military adversary. Drug trafficking and spillovers were recognized but positioned as
contingent and incremental risks. Many explicitly contrasted Venezuela with higher-
order geopolitical threats (e.g., major powers), treating the “major threat” framing
as inflated or politically instrumental.

Not a threat. In our simulation, this option was rarely selected; consequently,
no stable reasoning cluster emerged for “not a threat” beyond generic dismissal of
relevance to U.S. security.

Venezuela Q15: Do you approve or disapprove of U.S. military action in
Venezuela?
Approve. Approval rationales were typically conditional and reluctant: respondents
expressed general discomfort with war but accepted intervention if it were limited
in scope, short in duration, and tied to concrete objectives such as disrupting drug
trafficking or removing specific regime actors. “Quick and decisive” intervention, rather
than prolonged engagement or nation-building, was the dominant constraint.

Disapprove. Disapproval rationales emphasized the historical track record of
U.S. interventions, mission creep, civilian harm, and unintended consequences. Many
argued that military force is a poor instrument for complex political and humanitarian
crises and preferred non-military alternatives. Even when acknowledging the severity
of Venezuela’s situation, respondents viewed intervention as high-risk and low-reward
absent a direct, imminent threat.

Venezuela Q16: Should the administration obtain congressional approval
before military action?
Yes, needs congressional approval. Rationales selecting “Yes” strongly empha-
sized constitutional checks and balances and treated congressional authorization as a
basic requirement for initiating war. War-making was framed as qualitatively differ-
ent from routine executive action and therefore requiring collective deliberation and
democratic legitimacy, regardless of partisan preferences.

37

---

<!-- PAGE 38 -->

No, does not need congressional approval. Rationales selecting “No” priori-
tized speed and executive discretion, portraying Congress as too slow, gridlocked, or
prone to politicization for crisis response. This cluster framed unilateral action as nec-
essary for effective leadership, with transparency and deliberation treated as secondary
to operational effectiveness in national-security contexts.

Venezuela Q17: Do you approve or disapprove of attacking boats
suspected of drug trafficking?
Approve. Approval rationales morally foregrounded the harms of drugs (often framed
as existential to communities) and treated traffickers as legitimate targets. Many used
ends-justify-the-means reasoning, arguing that decisive interdiction deters smuggling
and protects U.S. borders, sometimes downplaying uncertainty in identification.

Disapprove. Disapproval rationales stressed due process, evidentiary standards,
and the risk of misidentifying civilians. These responses framed boat attacks as extra-
judicial violence with high potential for escalation and norm violation. Suspicion alone
was treated as an unacceptably low threshold for lethal force.

Venezuela Q18: Should the administration provide evidence that
Venezuela poses a threat before taking action?
Yes, should show evidence. This cluster emphasized legitimacy through trans-
parency, arguing that extraordinary force requires demonstrable evidence and public
accountability. Concerns about wrongful harm, false positives, and precedent-setting
abuses were central. Evidence was treated as a prerequisite to action rather than a
post hoc justification.

No, does not need to show evidence. This cluster justified acting on suspi-
cion by appealing to operational secrecy and trust in military or intelligence expertise.
Releasing evidence was portrayed as tactically dangerous (exposing sources and meth-
ods) and procedurally impractical in time-sensitive interdiction. The risk of false
positives was implicitly accepted as less costly than letting drugs through.

Venezuela Q19: Will military action decrease drugs reaching the United
States?
Yes, would decrease drugs. Rationales selecting “Yes” invoked supply-chain dis-
ruption and deterrence: reducing supply increases cost and risk for traffickers and
can slow or reduce flow, even if temporarily. These responses treated interdiction as
an imperfect but pragmatically beneficial mechanism, emphasizing chokepoints and
upstream disruption.

No, would not change the amount of drugs. Rationales selecting “no change”
emphasized demand-side constraints and adaptive trafficking networks. This cluster
described interdiction as whack-a-mole displacement that shifts routes and meth-
ods without meaningfully reducing total flow as long as U.S. demand remains high.
Military force was framed as misaligned with the structural drivers of the drug market.
Would increase drugs. Rationales selecting “would increase” extended the
adaptive-systems critique into a backfire mechanism. Responses argued that military
disruption generates instability, violence, and governance vacuums that strengthen

38

---

<!-- PAGE 39 -->

trafficking organizations, diversify routes, and increase incentives through higher
prices. The dominant causal chain was: disruption → chaos/instability → cartel
adaptation/expansion → equal or higher trafficking volume, often accompanied by
historical analogies to past enforcement shocks.

F.6 Unweighted persona-bank estimates

Fig. F3 Comparison of weighted and unweighted persona-bank responses with polling benchmarks.
Solid lines denote weighted estimates, while dotted lines denote unweighted aggregates. Results
are shown for both Twitter- and Reddit-based persona banks across long-term attitudinal ques-
tions (Panel A) and event-sensitive questions (Panel B). Unweighted estimates reproduce the same
within-cluster directional patterns as weighted estimates, but exhibit substantially larger deviations
in absolute levels, particularly for Reddit. This pattern indicates that weighting primarily improves
calibration by mitigating selection-induced level bias, while preserving the underlying attitudinal
structure expressed by the simulated respondents.

Figure F3 reports persona-bank estimates aggregated without weights alongside
the weighted results shown in the main text. This comparison clarifies the role of
weighting in the analysis.

Across both panels, unweighted persona-bank responses continue to reproduce
coherent question-to-question structure within each issue-specific cluster. Items receiv-
ing higher support in polling benchmarks are generally ranked higher by simulated
respondents, and lower-support items remain comparatively lower. This indicates that
trend alignment is not an artifact of calibration, but instead reflects stable attitudinal
gradients captured by the inferred personas.

39

---

<!-- PAGE 40 -->

At the same time, unweighted estimates exhibit substantially larger deviations
in absolute levels, particularly for the Reddit-based persona bank. These devia-
tions are consistent with known compositional imbalances in the underlying social
media samples, including overrepresentation of highly educated and politically liberal
users. Weighting, therefore, plays a critical role in improving calibration by reducing
selection-induced level bias, rather than altering the qualitative patterns of opinion
expressed by the simulated respondents.

Appendix G Persona schema

G.1 JSON Schema for Painter
The Painter module is instructed to follow the exact top-level structure below (no
additional top-level fields). Field values are constrained to the enumerated options
shown.

{

"personality_big5": {

{ "approx_level": "...", "confidence": "...", "rationale": "..." },

"openness":
"conscientiousness": { "approx_level": "...", "confidence": "...", "rationale": "..." },
{ "approx_level": "...", "confidence": "...", "rationale": "..." },
"extraversion":
{ "approx_level": "...", "confidence": "...", "rationale": "..." },
"agreeableness":
{ "approx_level": "...", "confidence": "...", "rationale": "..." }
"neuroticism":

},

"primal_world_beliefs": {

"good_vs_bad": {

"value": "leans_good | balanced | leans_bad | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},

"safe_vs_dangerous": {

"value": "leans_safe | balanced | leans_dangerous | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"enticing_vs_dull": {

"value": "leans_enticing | balanced | leans_dull | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"alive_vs_mechanistic": {

"value": "leans_alive | balanced | leans_mechanistic | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},

"pleasurable_vs_miserable": {

40

---

<!-- PAGE 41 -->

"value": "leans_pleasurable | balanced | leans_miserable | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"regenerative_vs_degenerative": {

"value": "leans_regenerative | balanced | leans_degenerative | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"progressing_vs_declining": {

"value": "leans_progressing | balanced | leans_declining | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"harmless_vs_threatening": {

"value": "leans_harmless | balanced | leans_threatening | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"cooperative_vs_competitive": {

"value": "leans_cooperative | balanced | leans_competitive | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"stable_vs_fragile": {

"value": "leans_stable | balanced | leans_fragile | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"just_vs_unjust": {

"value": "leans_just | balanced | leans_unjust | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},

"interesting_vs_boring": {

"value": "leans_interesting | balanced | leans_boring | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"beautiful_vs_ugly": {

"value": "leans_beautiful | balanced | leans_ugly | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"abundant_vs_barren": {

"value": "leans_abundant | balanced | leans_barren | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},

41

---

<!-- PAGE 42 -->

"worth_exploring_vs_not_worth_exploring": {

"value": "leans_worth_exploring | balanced | leans_not_worth_exploring | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"meaningful_vs_meaningless": {

"value": "leans_meaningful | balanced | leans_meaningless | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"improvable_vs_too_hard_to_improve": {

"value": "leans_improvable | balanced | leans_too_hard_to_improve | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"funny_vs_not_funny": {

"value": "leans_funny | balanced | leans_not_funny | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},

"intentional_vs_unintentional": {

"value": "leans_intentional | balanced | leans_unintentional | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"needs_me_vs_doesnt_need_me": {

"value": "leans_needs_me | balanced | leans_doesnt_need_me | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"interactive_vs_indifferent": {

"value": "leans_interactive | balanced | leans_indifferent | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},

"interconnected_vs_separable": {

"value": "leans_interconnected | balanced | leans_separable | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"changing_vs_static": {

"value": "leans_changing | balanced | leans_static | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"hierarchical_vs_nonhierarchical": {

"value": "leans_hierarchical | balanced | leans_nonhierarchical | unclear",
"confidence": "high | medium | low",

42

---

<!-- PAGE 43 -->

"rationale": "..."

},
"understandable_vs_too_hard_to_understand": {

"value": "leans_understandable | balanced | leans_too_hard_to_understand | unclear",
"confidence": "high | medium | low",
"rationale": "..."

},
"acceptable_vs_unacceptable": {

"value": "leans_acceptable | balanced | leans_unacceptable | unclear",
"confidence": "high | medium | low",
"rationale": "..."

}

},

"values_and_identities": {
"salient_identities": [

{

}

"identity": "short label (e.g., parent, gamer, activist, student, etc.)",
"confidence": "high | medium | low",
"rationale": "..."

],
"core_values": [

"value_label": "e.g., equality, order, tradition, autonomy, care, loyalty, etc.",
"confidence": "high | medium | low",
"rationale": "..."

{

}

]

},

"life_experiences": {

"education_and_work": [

{

}

"summary": "...",
"confidence": "high | medium | low",
"rationale": "..."

],
"family_and_relationships": [

{

}

"summary": "...",
"confidence": "high | medium | low",
"rationale": "..."

],
"turning_points_or_themes": [

{

"summary": "Important repeated experiences",
"confidence": "high | medium | low",

43

---

<!-- PAGE 44 -->

"rationale": "..."

}

]

},

"opinions_and_beliefs": {

"politics_and_society": [

{

}

"topic": "e.g., elections, immigration, public health, identity politics, etc.",
"stance_summary": "1{3 sentences summarizing their likely opinion",
"confidence": "high | medium | low",
"rationale": "..."

],
"work_and_career": [

{

}

"topic": "work, jobs, academia, gig economy, etc.",
"stance_summary": "1{3 sentences",
"confidence": "high | medium | low",
"rationale": "..."

],
"technology_and_social_media": [

{

}

"topic": "e.g., views on platforms, algorithms, AI, online communities",
"stance_summary": "1{3 sentences",
"confidence": "high | medium | low",
"rationale": "..."

],
"other_recurrent_themes": [

"topic": "any other recurring domain (e.g., mental health, sports fandom, gaming, religion)",
"stance_summary": "1{3 sentences",
"confidence": "high | medium | low",
"rationale": "..."

{

}

]

},

"interaction_style": {

"tone": {

"value": "e.g., sarcastic, earnest, hostile, humorous, supportive, analytical, etc.",
"confidence": "high | medium | low",
"rationale": "..."

},
"conflict_style": {

"value": "confrontational | avoidant | accommodating | mixed | unclear",
"confidence": "high | medium | low",
"rationale": "..."

44

---

<!-- PAGE 45 -->

},
"information_orientation": {

"value": "news_junkie | casually_informed | low_information | niche_expert | unclear",
"confidence": "high | medium | low",
"rationale": "..."

}

},

"meta": {

"overall_uncertainty_comment": "2{4 sentences",
"notable_absences": "Brief list or sentence"

}

}

G.2 Painter prompt template
System prompt. The following template is used for the Painter module to infer a
tentative, probabilistic persona profile from a user’s historical posts.

You are an expert computational social scientist trained in survey methodology,
personality psychology, and political behavior.

Your task is to infer a *tentative*, *probabilistic* profile of a single social
media user from their posts.

CRITICAL RULES:
- Use ONLY the textual evidence in the posts (plus ordinary background knowledge

about language, not about any specific real person).

- Treat all inferences as uncertain hypotheses, not facts.
- When evidence is weak or absent, say "unknown" and explain briefly.
- DO NOT include any demographic fields in your output (age, gender, region, etc.).

Assume demographics are handled elsewhere in the pipeline.

- Do not attempt to identify or de-anonymize the user, and avoid directly quoting any specific posts;

paraphrase them instead.

You must produce TWO parts:

1) A JSON object describing:

- personality_big5
- primal_world_beliefs
- values_and_identities
- life_experiences
- opinions_and_beliefs
- interaction_style
- meta

2) After the JSON, print a line with exactly:

---
Then output a 2{3 paragraph third-person narrative persona.

45

---

<!-- PAGE 46 -->

JSON SCHEMA (follow this structure exactly; no extra top-level fields):
[see Appendix~\ref{app:persona_schema}]

IMPORTANT OUTPUT FORMAT:
- First, output ONLY the JSON object (no surrounding prose).
- Then a line with exactly three hyphens: ---
- Then the third-person narrative persona (2{3 paragraphs, ~150{300 words).

G.3

External survey study prompt templates

This appendix documents the prompt templates used in the external survey
study. Prompts are shown as templates; runtime fields (e.g., {persona json},
{persona narrative}, {demographics}, {question text}) are populated program-
matically.

G.3.1 Direct-attitude prompting (no search)

You are participating in a survey. Answer the questions as the person described
below. Use only the information in the persona profile. If the persona provides
no evidence, choose the most plausible option but mark LOW confidence.

PERSONA (JSON):
{persona_json}

PERSONA (Narrative):
{persona_narrative}

DEMOGRAPHICS (provided as context; do not infer new demographics):
{demographics}

INSTRUCTIONS:
- Treat this as a survey response, not a factual exam.
- Give your best answer based on your views/values/habits implied by the persona.
- Do not overthink; avoid long analysis.
- Output a JSON object with one entry per question in the required schema:

{ "value": <int_or_string>, "label": <string>, "confidence": "high|medium|low",

"reason": <1-3 sentences> }

QUESTION:
{question_text}

RESPONSE OPTIONS:
{options_list}

G.3.2 Time-sensitive prompting with information acquisition

(three-step)

Step 1: Pre-existing knowledge / prior impressions.

You are participating in a survey about a recent public issue. Answer as the

46

---

<!-- PAGE 47 -->

person described below.

PERSONA (JSON):
{persona_json}

PERSONA (Narrative):
{persona_narrative}

DEMOGRAPHICS (provided as context; do not infer new demographics):
{demographics}

TASK:
Before searching the web, state what you (as this person) already know or
believe about the topic. If you know little or nothing, say so.

OUTPUT (JSON only):
{

"knowledge_level": "none|minimal|moderate|extensive",
"what_i_know": "1-4 sentences",
"where_i_heard_it": "e.g., news, social media, friends, unknown",
"prior_impression": "1-3 sentences (or ’unknown’)"

}

TOPIC:
{topic_name}

Step 2: Persona-conditioned query generation.

Generate 3-5 web search queries that YOU (as this person) would actually type to
learn more about the topic. Queries should reflect your interests, priors, and
trusted sources implied by the persona.

PERSONA (JSON):
{persona_json}

PERSONA (Narrative):
{persona_narrative}

OUTPUT (JSON only):
{ "queries": ["...", "...", "..."] }

TOPIC:
{topic_name}

Step 2b: Summarize retrieved information.

Below are search results (titles/snippets). Summarize what you learned, focusing
on the most relevant points for forming an opinion. Keep it concise.

PERSONA (JSON):
{persona_json}

47

---

<!-- PAGE 48 -->

PERSONA (Narrative):
{persona_narrative}

SEARCH RESULTS:
{search_results}

OUTPUT (JSON only):
{

"key_points": ["...", "...", "..."],
"timeframe": "what time period the info seems to cover (if clear)",
"source_fit": "1-2 sentences on why these sources feel credible or not to you",
"updated_impression": "1-3 sentences (or ’unchanged’)"

}

Step 3: Post-search survey response.

Now answer the survey question as the person described below. Use the persona
AND what you learned from the search summary. This is a survey response, not a
factual exam.

PERSONA (JSON):
{persona_json}

PERSONA (Narrative):
{persona_narrative}

DEMOGRAPHICS:
{demographics}

PRE-KNOWLEDGE (before search):
{preknowledge_json}

SEARCH SUMMARY:
{search_summary_json}

INSTRUCTIONS:
- Choose the option that best matches your view.
- Do not write a long essay; 1-3 sentences of justification is enough.
- Output JSON only in the required schema:

{ "value": <int_or_string>, "label": <string>,

"confidence": "high|medium|low",
"reason": <1-3 sentences>,
"influenced_by_search": true|false }

QUESTION:
{question_text}

RESPONSE OPTIONS:
{options_list}

48

---

<!-- PAGE 49 -->

References

[1] Argyle, L. P. et al.

Out of One, Many: Using Language Models
Political Analysis 31, 337–351 (2023).
https://www.cambridge.org/core/journals/political-analysis/article/

to Simulate Human Samples.
URL
out-of-one-many-using-language-models-to-simulate-human-samples/
035D7C8A55B237942FB6DBAD7CAA4E49.

[2] Horton, J. J. Large Language Models as Simulated Economic Agents: What Can
We Learn from Homo Silicus? (2023). URL http://arxiv.org/abs/2301.07543.

[3] Park, J. S. et al. Generative Agent Simulations of 1,000 People (2024). URL

http://arxiv.org/abs/2411.10109.

[4] Wang, A., Morgenstern, J. & Dickerson, J. P. Large language models that replace
human participants can harmfully misportray and flatten identity groups. Nature
Machine Intelligence 7, 400–411 (2025). URL https://www.nature.com/articles/
s42256-025-00986-z.

[5] Murthy, S. K., Ullman, T. & Hu, J. Chiruzzo, L., Ritter, A. & Wang, L. (eds)
One fish, two fish, but not the whole sea: Alignment reduces language models’
conceptual diversity. (eds Chiruzzo, L., Ritter, A. & Wang, L.) Proceedings of
the 2025 Conference of the Nations of the Americas Chapter of the Association
for Computational Linguistics: Human Language Technologies (Volume 1: Long
Papers), 11241–11258 (Association for Computational Linguistics, Albuquerque,
New Mexico, 2025). URL https://aclanthology.org/2025.naacl-long.561/.

[6] Dillion, D., Tandon, N., Gu, Y. & Gray, K. Can AI language models replace
human participants? Trends in Cognitive Sciences 27, 597–600 (2023). URL
https://www.sciencedirect.com/science/article/pii/S1364661323000980.

[7] Yang, Z. et al. OASIS: Open Agent Social Interaction Simulations with One

Million Agents (2025). URL http://arxiv.org/abs/2411.11581.

[8] Ge, T. et al. Scaling Synthetic Data Creation with 1,000,000,000 Personas (2025).

URL http://arxiv.org/abs/2406.20094.

[9] Zhang, S. et al. Personalizing Dialogue Agents: I have a dog, do you have pets

too? (2018). URL http://arxiv.org/abs/1801.07243.

[10] Kang, M. et al. Deep Binding of Language Model Virtual Personas: a Study on

Approximating Political Partisan Misperceptions (2025).

[11] Moon, S. et al. Virtual Personas for Language Models via an Anthology of

Backstories (2024). URL http://arxiv.org/abs/2407.06576.

49

---

<!-- PAGE 50 -->

[12] Toubia, O. et al. Twin-2K-500: A dataset for building digital twins of over 2,000
people based on their answers to over 500 questions (2025). URL http://arxiv.
org/abs/2505.17479.

[13] Lohr, S. L. Sampling: Design and Analysis 3 edn (Chapman and Hall/CRC, Boca
Raton, 2021). URL https://www.taylorfrancis.com/books/9780429298899.

[14] Li, C. J. et al. Simulating Society Requires Simulating Thought (2025). URL

http://arxiv.org/abs/2506.06958.

[15] Mairesse, F., Walker, M. A., Mehl, M. R. & Moore, R. K. Using Linguistic Cues
for the Automatic Recognition of Personality in Conversation and Text. Journal
of Artificial Intelligence Research 30, 457–500 (2007). URL https://jair.org/
index.php/jair/article/view/10520.

[16] Clifton, J. D. W. et al. Primal world beliefs. Psychological Assessment 31, 82–99

(2019).

[17] Jost, J. T. & Amodio, D. M. Political ideology as motivated social cognition:
Behavioral and neuroscientific evidence. Motivation and Emotion 36, 55–64
(2012).

[18] McAdams, D. P. Narrative identity (Springer Science + Business Media, New

York, NY, US, 2011).

[19] Schwartz, H. A. et al. Personality, gender, and age in the language of social
media: the open-vocabulary approach. PLoS One 8, e73791 (2013). URL https:
//dx.plos.org/10.1371/journal.pone.0073791.

[20] Ferrara, E. Should ChatGPT be Biased? Challenges and Risks of Bias in Large
Language Models. First Monday (2023). URL http://arxiv.org/abs/2304.03738.

[21] Mohsin, M. A. et al. On the Fundamental Limits of LLMs at Scale (2025). URL

http://arxiv.org/abs/2511.12869.

[22] Bailey, E. R., Matz, S. C., Youyou, W. & Iyengar, S. S. Authentic self-
expression on social media is associated with greater subjective well-being. Nature
Communications 11, 4889 (2020). URL https://www.nature.com/articles/
s41467-020-18539-w.

[23] Kosinski, M., Stillwell, D. & Graepel, T. Private traits and attributes are pre-
dictable from digital records of human behavior. Proceedings of the National
Academy of Sciences 110, 5802–5805 (2013). URL https://pnas.org/doi/full/10.
1073/pnas.1218772110.

[24] Park, P. S., Schoenegger, P. & Zhu, C. Diminished Diversity-of-Thought in a
Standard Large Language Model (2023). URL http://arxiv.org/abs/2302.07267.

50

---

<!-- PAGE 51 -->

[25] Wright, A. G. C. et al. Assessing personality using zero-shot generative AI scoring
of brief open-ended text. Nature Human Behaviour 1–15 (2026). URL https:
//www.nature.com/articles/s41562-025-02389-x.

[26] Kish, L. Survey sampling A Wiley Interscience Publication (Wiley, New York,

1995).

[27] Little, R. J. A. & Rubin, D. B. Statistical analysis with missing data 3rd edition
edn. Wiley series in probability and statistics (Wiley, Hoboken, NJ, 2020).

[28] S¨arndal, C.-E., Swensson, B. & Wretman, J. H. Model assisted survey sampling
1. softcover print edn. Springer series in statistics (Springer, New York Berlin
Heidelberg, 2003).

[29] ALWIN, D. F. & KROSNICK, J. A. The Reliability of Survey Attitude
Measurement: The Influence of Question and Respondent Attributes. Sociolog-
ical Methods & Research 20, 139–181 (1991). URL https://doi.org/10.1177/
0049124191020001005.

[30] Pew Research Center. Public Opinion on Abortion (2025). URL https://www.

pewresearch.org/religion/fact-sheet/public-opinion-on-abortion/.

[31] Krogstad, S. M. a. J. M.

Trump and Harris Supporters Differ on
Mass Deportations but Favor Border Security, High-Skilled Immigration
(2024).
URL https://www.pewresearch.org/race-and-ethnicity/2024/09/27/
trump-and-harris-supporters-differ-on-mass-deportations-but-favor-border-security-high-skilled-immigration/.

[32] Taylor

Orth.

release

ment
(2025).
53427-bipartisan-majorities-want-government-to-release-jeffrey-epstein-records-november-15-17-2025-economist-yougov-poll.

Jeffrey

Bipartisan
its
URL

majorities
Epstein

govern-
want
YouGov
records
https://today.yougov.com/politics/articles/

the
|

to

[33] Anthony Salvanto & Jennifer De Pinto.

would oppose U.S. military action in Venezuela,
explained - CBS News
poll-venezuela-u-s-military-action-trump/.

(2025).

CBS News poll finds most
say Trump hasn’t
URL https://www.cbsnews.com/news/

[34] Converse, P. E. The nature of belief systems in mass publics (1964). Critical
Review 18, 1–74 (2006). URL http://www.tandfonline.com/doi/abs/10.1080/
08913810608443650.

[35] Zaller, J. & Feldman, S. A Simple Theory of the Survey Response: Answering
Questions versus Revealing Preferences. American Journal of Political Science
36, 579–616 (1992). URL https://www.jstor.org/stable/2111583.

[36] Krosnick, J. A. Response strategies for coping with the cognitive demands of
attitude measures in surveys. Applied Cognitive Psychology 5, 213–236 (1991).

51

---

<!-- PAGE 52 -->

URL https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.2350050305.

[37] Yao, S. et al. ReAct: Synergizing Reasoning and Acting in Language Models

(2023). URL http://arxiv.org/abs/2210.03629.

[38] Deville, J.-C., S¨arndal, C.-E. & Sautory, O. Generalized raking procedures in
survey sampling. Journal of the American Statistical Association 88, 1013–
1020 (1993). URL https://www.tandfonline.com/doi/abs/10.1080/01621459.
1993.10476369.

52

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Persona-Based Simulation of Human Opinion at
Population Scale
Mao Li1* and Frederick G. Conrad1
1Institute for Social Research, University of Michigan, 426 Thompson
St., Ann Arbor, 48104, MI, US.
*Corresponding author(s). E-mail(s): maolee@umich.edu;
Contributing authors: fconrad@umich.edu;
Abstract
What does it mean to model a person, not merely to predict isolated responses,
preferences, or behaviors, but to simulate how an individual interprets events,
forms opinions, makes judgments, and acts consistently across contexts? This
questionmattersbecausesocialsciencerequiresnotonlyobservingandpredict-
ing human outcomes, but also simulating interventions and their consequences.
Althoughlargelanguagemodels(LLMs)cangeneratehuman-likeanswers,most
existingapproachesremainpredictive,relyingondemographiccorrelationsrather
than representations of individuals themselves.
We introduce SPIRIT (Semi-structured Persona Inference and Reasoning for
Individualized Trajectories), a framework designed explicitly for simulation
ratherthanprediction.SPIRITinferspsychologicallygrounded,semi-structured
personas from public social media posts, integrating structured attributes (e.g.,
personality traits and world beliefs) with unstructured narrative text reflecting
valuesandlivedexperience.ThesepersonaspromptLLM-basedagentstoactas
specific individuals when answering survey questions or responding to events.
Using the Ipsos KnowledgePanel, a nationally representative probability sample
of U.S. adults, we show that SPIRIT-conditioned simulations recover self-
reported responses more faithfully than demographic persona and reproduce
human-likeheterogeneityinresponsepatterns.Wefurtherdemonstratethatper-
sona banks can function as virtual respondent panels for studying both stable
attitudes and time-sensitive public opinion.
Keywords:Personainference,Syntheticrespondents,Largelanguagemodels,Social
simulation,SocialMedia
1
6202
raM
82
]YC.sc[
1v65072.3062:viXra

1 Introduction
Large language models (LLMs) are increasingly used to simulate opinion formation,
opinion change, and decision making, opening new possibilities for computational
social science and user-centric NLP applications [1–3]. A common approach gives the
model a short demographic profile (for example age, gender, education), often called
a persona, and asks it to answer as if it were a person with that profile. [1, 2]. This
approach is conceptually appealing because demographics are widely available and
central to population inference. However, it assumes that demographics alone largely
account for variation in opinions and behaviors across people. Recent studies show
that results can change sharply when the question wording, examples, or formatting
in the prompt changes. [4–6].
In response, researchers have attempted to address these limitations in two main
ways. One tries to increase diversity by simulating many more synthetic respondents,
sometimes with a larger set of profile fields [3, 7, 8]. These methods can produce a
wider range of answers and may reduce obvious skews, such as always producing the
same view for a given demographic group. But they still do not show that the mix
of simulated people matches any real population, or that simulated group differences
align with observed group differences.
Anotherapproachfocusesonenrichingpersonasusingdetailedsurveyresponsesor
text produced by the simulated individual, such as life narratives or interviews. [3, 9–
12]. These methods yield more vivid and coherent simulated responses, improving
realism and consistency. Yet, they remain centered on individual-level fidelity and
leave open the question of how collections of such personas relate to population-level
distributions.
Despite their differences, both approaches leave unresolved a core challenge for
using LLMs in social scientific inference: how to estimate population-level distribu-
tions, especially when personas are derived from either prompting an LLM to play
a particular role (e.g., “You are a 50-year-old Republican female from Kansas”) or
sampling multiple users from non-probability sources, such as social media. Scaling
the number of synthetic respondents or enriching persona descriptions can make sim-
ulations look more realistic, but these approaches do not, by themselves, make the
resultssuitableforpopulationinference.Thecentralproblemisthatthedataobtained
from the persona(s) are constrained by who they represent, which will not necessarily
be the target population (often the general public). This mirrors a basic distinction
in survey research: probability samples, with known inclusion probabilities, support
design-based population estimation, whereas non-probability samples require addi-
tional assumptions and methods, such as calibration, to adjust for selection bias and
unequal inclusion [13].
At a more fundamental level, demographics capture only a small portion of what
shapes opinions and decisions [14]. Many influential factors are not explained by age,
gender,oreducation,suchaspersonalitytraits[15],basicbeliefsabouttheworld[16],
politicalidentity[17],narrativeidentity[18],andtheinformationenvironmentspeople
inhabit[19].Asaresult,demographic-basedpersonasareoftennotsufficientlynuanced
to provide realistic, person-specific responses. When the prompt underspecifies the
individual person, the model tends to fill in the gaps using broad patterns learned
2

duringtraining[20,21],whichcandominatethesimulatedresponses.Thegapbetween
whatdemographicsdetermineaboutanindividual’sopinionandwhatthemodelmust
inferbasedontheparticularsetofdemographics,limitstheaccuracyofpersona-based
simulations of public opinion and behavior at a population level. These limitations
suggestthatrealisticsimulationrequiresricher,morepsychologicallygroundedperson-
representations than demographics alone can provide.
Studiesofeverydayself-expressiononsocialmediashowthatpeople’slanguageand
behavior patterns are associated with self-reported personality measures, indicating
thatonlinetracesreflectenduringdifferencesbetweenindividuals[22].Classicworkby
Kosinski and colleagues further showed that simple digital records, such as Facebook
“Likes,” can be used to predict a range of personal attributes [23]. Building on these
findings, studies report that LLMs can infer traits directly from users’ social media
text in a prompt-based setting, with performance comparable to models trained on
labeled data in some tasks [24]. Evidence also suggests that this signal is not limited
to social media: Wright and colleagues show that generative models can estimate Big
Five personality traits (a common five-dimension personality framework) from brief
open-ended narratives, producing respectable agreement with self-reports [25].
Prior work often stops at trait prediction and does not provide a clear way to
organize inferred attributes into a reusable persona for simulation and evaluation.
To move the enterprise forward, we introduce SPIRIT (Semi-structured Persona
InferenceandReasoningforIndividualizedTrajectories),aframeworkthatconstructs
structured, multi-dimensional personas from social media text and applies them in
LLM-based behavioral simulation.
We first recruited panel members from a probability-based online panel (the Ipsos
KnowledgePanel) who were also social media users, and collected their user handles
on Reddit, Twitter, or both. Participants consented to linking their public posts to
their Ipsos survey responses, which allowed the model to infer a SPIRIT persona for
eachindividual.BecauseKnowledgePanelisdesignedtorepresenttheU.S.population
underaprobability-basedrecruitmentdesign,thisstartingpointsupportspopulation-
level inference.
WerefertotheresultingcollectionofSPIRITpersonasasaPersona Bank.Con-
ceptually,itfunctionsasavirtualtwinpanelthatcanbesurveyedusingstandardized
instruments. At the same time, our linkage procedure imposes additional eligibility
requirements(havinganaccount,posting,andconsentingtolink),whichcanintroduce
selection bias. We therefore construct weights and apply them to each persona-bank
respondent to align weighted estimates with U.S. population benchmarks. By com-
bining established ideas from survey methodology [26–28] with LLM-based persona
inference and simulation, SPIRIT provides a practical foundation for population-level
simulation.
In summary, SPIRIT provides a persona framework in which personas are (1)
inferred from authentic social media posts and (2) reweighted to support population-
levelgeneralization.Unlikepriorapproachesthatfocusoneitherincreasingthenumber
of synthetic respondents or enriching persona detail without addressing the sampling
problem,SPIRIToperatesattwolevels:attheindividuallevel,itpromptsanLLMto
adopt a person-specific persona to answer survey questions; atthe population level, it
3

combines those person-level responses with calibration weights so that aggregates can
| be interpreted | as U.S. population |     | estimates. |
| -------------- | ------------------ | --- | ---------- |
Across multiple survey questions on prominent political issues, SPIRIT per-
sona outperforms demographic persona, producing simulations that are more stable
across questions, easier to interpret, and more consistent at both the individual and
| population        | levels. |                |     |
| ----------------- | ------- | -------------- | --- |
| Our contributions |         | are threefold: |     |
1. We introduce SPIRIT, a semi-structured persona framework that infers multi-
dimensional user representations from social media text that are interpretable and
uses them to prompt an LLM to respond to survey questions as the individual
| represented | by the persona |     | would respond. |
| ----------- | -------------- | --- | -------------- |
2. We provide a systematic evaluation of our framework, showing that demo-
graphic personas yield unrealistic response distributions and lower-confidence
estimates,whileSPIRITpersonasbetterrecovercoherent,person-specificresponse
patterns—highlighting the limits of demographic attributes alone for simulating
| how opinions | are formed | and | change. |
| ------------ | ---------- | --- | ------- |
3. WedevelopandempiricallyevaluatethePersonaBank.Inparticular,wecalibrate
persona-based simulations to population benchmarks and validate the resulting
virtual panel against survey and polling results concerning salient political issues
| measured | by high-quality | opinion | polls. |
| -------- | --------------- | ------- | ------ |
2 Results
The Ipsos KnowledgePanel collects a substantially broad set of respondent informa-
tion; for the purposes of this study, we obtained a subset of 81 survey questions
from the Ipsos records spanning a wide range of topics, from demographic charac-
teristics to attitudes toward public health and vaccines. To construct a demographic
personaforcomparison,weusesevendemographicvariables—age,race,gender,polit-
ical ideology, income, education, and urbanicity—as persona inputs. The remaining
52 non-demographic questions (spanning from self-rated health to political attitudes)
are then used as held-out evaluation outcomes to assess how well different persona
constructions recover respondents’ self-reported views and dispositions (full question
| wording is | provided in Appendix |     | C). |
| ---------- | -------------------- | --- | --- |
We evaluate the proposed framework along two complementary dimensions: (i)
inference accuracy and (ii) the distribution of inferred user-level responses. We com-
pare the demographic personas against the SPIRIT personas, which relies exclusively
on non-demographic attributes inferred from user-generated text, across LLMs of
| increasing     | size.         |     |           |
| -------------- | ------------- | --- | --------- |
| 2.1 Framework  | Evaluation    |     |           |
| 2.1.1 Accuracy | of user-level |     | inference |
Inference accuracy is evaluated at the user level. Each user is associated with a set of
questions;foreachquestion,themodelproducesaninferredresponsethatiscompared
against the user’s self-reported value. We compute the mean accuracy per user and
4

Fig.1 Frameworkevaluationacrossmodelsandconditioningstrategies.A,Distributionofper-user
position-weightedmeaninferredvaluesforthesameeligibleIpsosKnowledgePanelparticipantslinked
to public social media accounts, comparing their self-reported responses with simulated responses
generatedunderthedemographicpersonaandtheSPIRITpersona(withnon-demographicattributes
inferred from text). For each participant, responses are aggregated across survey items using a
position-weighted mean, such that identical composite values arise only from identical response
patterns. Human responses are shown as an empirical reference for the level of population-level
heterogeneity expected when aggregating across many items. Demographic personas yield highly
concentrated distributions, whereas SPIRIT personas preserve substantially greater individual-level
variation, closely resembling human heterogeneity. B, User-level inference accuracy across models
ordered by size. SPIRIT personas consistently outperform demographic personas with performance
gainssaturatingforlargermodels.
then average across users within each persona condition (i.e., SPIRIT persona vs.
demographic persona).
As shown in Figure 1B, under the SPIRIT personas, inference accuracy increases
monotonically with model size. Smaller models (e.g., Gemma-3-4B and LLaMA-3.1-
8B)performsubstantiallyworsethanlargermodels,whilegainsbegintoplateaufrom
Gemma-3-27BtoGPT-5-miniandGPT-5.2.Thispatternisexpected:thecorerequire-
ments of the framework—reading user posts, constructing non-demographic persona
representations, and reasoning over them—rely primarily on stable comprehension
and moderate-level reasoning rather than highly complex capabilities (e.g., Coding or
5

solving math problems). Once these competencies are met, additional model capacity
yields diminishing returns.
Comparing the demographic personas with the SPIRIT personas, we observe a
consistent accuracy advantage for the SPIRIT personas across all models. While
demographic personas’ accuracy improves modestly with model size, these gains pre-
sumably reflect improved guessing by larger models based on correlations between
demographics and responses to survey items (e.g., income and credit score), rather
than grounded inference from individual-specific signals. Overall, the observed 8–9%
absolute improvement indicates the SPIRIT personas substantially outperform the
demographic personas.
2.1.2 Distributional properties of inferred responses
Accuracy alone does not capture how well LLMs simulate the full pattern of user
responses, especially their variability: accuracy can remain high even when inferred
answers are overly concentrated. We therefore examine the distribution of inferred
user-level mean responses under each persona condition. For each user, we aggregate
inferred responses across all 52 survey questions into a single composite score that
summarizes their overall response pattern. We compute a position-weighted per-user
mean, where each item response is weighted by its position in the survey sequence
(details are provided in Methods 4.3).
A key property of this construction is that two users will obtain the same com-
positescoreonlyiftheirresponsesequencesareidenticalacrossallquestions.Because
perfectly identical sequences are unlikely in realistic survey settings, and would effec-
tively eliminate individual heterogeneity, we expect substantive user-level differences
to manifest as a dispersed distribution of composite scores rather than one concen-
trated around a single value. This composite score preserves the ordering of responses
while reducing each user’s response profile to a single summary measure that still
captures meaningful heterogeneity across users.
Thesameaggregationruleisappliedtoinferredresponsesandhumanself-reports.
The resulting distributions are visualized using box plots (Figure 1A).
Toprovideameaningfulreferencepoint,weincludethedistributionofhumanself-
reported responses. This human distribution is not treated as a target to be matched
exactly, but rather as an empirical benchmark for population-level heterogeneity.
Across all models, SPIRIT personas produce broader and more differentiated dis-
tributions than demographic personas, more closely resembling the spread observed
in human responses. In contrast, the demographic personas yield markedly nar-
rowerdistributions,indicatinghomogenizedpredictionsdrivenbyshareddemographic
profiles.
Thisbehaviorisexpected.Forcertainquestions,suchascreditscoreormediacon-
sumption, the demographic personas provide strong predictive signals. For example,
highhouseholdincomeisstronglyassociatedwithexcellentcreditscores,andagecor-
relates with lower social media use and greater reliance on television or newspapers.
When such correlations dominate, demographic persona inference tends to collapse
individuals with similar demographic profiles into near-identical predictions, thereby
reducing population-level diversity.
6

Consistent with this pattern, the median inferred value under demographic
personas is concentrated around approximately 1.5. This reflects a tendency for
demographic persona inference to default to negative responses (e.g., No) for many
behavioral and health-related questions (e.g., drinking alcohol or reporting anxiety-
related conditions), which substantially compresses the range of possible inferred
responses.Inaddition,thedemographicpersonasyieldlowerconfidenceestimatesthan
the SPIRIT personas, a result that is expected given the limited informational con-
tentavailablewheninferencereliessolelyondemographicattributes.Furtheranalyses
unpackingthesedistributionalandconfidencedifferencesareprovidedinAppendixD.
SPIRIT personas mitigate this effect by incorporating linguistic, behavioral, and
psychological signals extracted from user-generated text. This is particularly salient
for attributes weakly determined by demographics, including psychological traits and
mental health-related indicators. As a result, SPIRIT personas preserve individual-
level variation that is otherwise lost under demographic personas.
It is important to note that inference accuracy is computed using a strict exact-
match criterion between inferred values and self-reported responses. This metric does
notaccountformeasurementerrorinherentinsurveyresponses.Priorworkhasshown
that human responses—particularly for Likert-type items—are subject to instability
overtime[3,29];evenwhenthesameindividualisre-interviewedafterashortinterval,
responses may differ due to interpretation, recall, or response scale ambiguity. For
example, distinctions between categories such as sometimes and often may reflect
measurement noise rather than substantive disagreement.
To account for this, we additionally compute an off-by-one rate for the best-
performing configurations (GPT-5.2 and GPT-5-mini with SPIRIT personas). The
off-by-one rate is defined as the proportion of inferred responses whose ordinal dis-
tance from the corresponding self-reported value is exactly one category, aggregated
acrosssurveyitemsattheindividuallevel.Wefindoff-by-oneratesof0.18forGPT-5.2
and0.19forGPT-5-mini,indicatingthatapproximately83%ofinferredresponsesare
eitherexactmatchesordifferbyatmostoneresponsecategoryfromtheself-reported
value.
We focus our main comparison on the 52 non-demographic items because the
remaining29itemsaredemographicvariables,andsomeoftheseareusedtoconstruct
the demographic persona. Including them in the primary evaluation would therefore
make the comparison less fair. We nevertheless extend the analysis to all 81 items as
a supplementary check. Because SPIRIT is inferred only from users’ historical Reddit
and Twitter/X posts and does not use any self-reported survey attributes, including
demographics, this broader analysis allows us to assess whether the inferred personas
can also recover demographic characteristics that were never given as inputs.
A clear pattern emerges across domains. SPIRIT performs particularly well on
health- and vaccine-related items, which tend to reflect more stable beliefs and to
showstrongerconsistencyacrossrelatedquestions.Incontrast,performanceisweaker
on short-horizon behavioral items such as beer consumption (e.g., whether someone
drank in the past week or month). These behaviors are inherently more variable and
sensitivetorecentcircumstances,soeventhesamepersonmayanswerdifferentlyover
time, making them harder to infer reliably from long-run posting histories.
7

Importantly,thisisnottheprimaryusecaseweemphasize.Ourgoalistosupport
inferenceandsimulationofcomparativelystableorientationsandbeliefsystems,where
internal consistency is expected and substantively meaningful, rather than to predict
transient,week-to-weekbehaviors.Theresultsofthisextendedevaluationarereported
in Appendix F.
These results show that the proposed framework improves not only inference
accuracy but also the realism and expressiveness of inferred user responses. While
demographic personas perform well for easily predictable attributes probably because
population-level correlations, SPIRIT personas capture individual differences and
avoid overly homogeneous simulations.
2.2 Persona banks as virtual respondent panels
Whilethefirstpartoftheresultsestablishesthevalidityoftheproposedframeworkby
benchmarking simulated responses against self-reported values, such validation alone
is not the ultimate objective of this work. The self-reported data available for bench-
marking may not themselves be of substantive interest to researchers. The broader
goal is to enable SPIRIT personas to simulate public opinion across a wide, if not
unconstrained, range of topics and questions.
We therefore turn to a second set of analyses that treat the group of SPIRIT
personas as a persona bank, i.e., a collection of virtual respondents that can be sur-
veyed using standardized survey instruments. Conceptually, this persona bank serves
as a virtual respondent panel, allowing us to examine public attitudes toward rapidly
evolving and event-driven issues for which traditional survey data are often delayed
or expensive.
2.2.1 Surveying the persona bank
We focus on four public issues that were highly salient during the study period: (i)
opinions about abortion [30], (ii) attitudes toward immigration [31], (iii) public reac-
tions to the Epstein files [32], and (iv) views on U.S. military actions in Venezuela
[33]. For each topic, we reused survey questions from contemporaneous public opin-
ion polls, preserving the original wording and response options. These questions are
posed to the persona bank, and the resulting simulated responses are aggregated to
produce population-level estimates, with each respondent weighted accordingly (as
described in Method 4.2.4). Full question wordings and response options are provided
in Appendix E.
Weinterpretthefirsttwoquestionclusters(i.e.,opinionsaboutabortionandatti-
tudes toward immigration) as measuring relatively stable, crystallized opinions that
tend to be anchored in enduring belief structures [34]. By contrast, clusters (iii) and
(iv) capture more time- and event-sensitive judgments, for which expressed opin-
ions are often constructed from whatever considerations and facts are most salient at
the moment of response [35]. Accordingly, for clusters (iii) and (iv), we allow simu-
lated LLM respondents to retrieve up-to-date external information via web search, as
described in Method 4.4.
8

Fig. 2 persona-bank responses compared with polling benchmarks, grouped by question type. A,
Long-termattitudinalquestions(abortionandimmigration)drawnfromgeneralopinionsurveys.B,
Event-sensitive questions (Epstein files and Venezuela policy attitudes) fielded in late 2025 to early
2026,forwhichsimulatedrespondentsmayrequirecontemporaneouscontext.Shadedregionsindicate
issue-specificclustersandareusedtoavoidimplyingcontinuityacrossunrelatedissues.Withineach
issue-specific cluster, persona-bank estimates reproduce coherent question-to-question patterns that
align with polling benchmarks. After calibration, Twitter-based estimates track benchmarks more
closelyinabsolutelevelthanReddit-basedestimates,whichexhibitsystematicshiftsinmagnitude.
BothTwitter-andReddit-basedestimatespreservethesamedirectionalstructure.
2.2.2 Trend alignment with polling benchmarks
Figure2comparesweightedestimatesderivedfromTwitter-andReddit-basedSPIRIT
persona banks with polling benchmarks across multiple domains. All simulated
responsesaregeneratedbyqueryingthesameunderlyingsetofsimulatedrespondents,
i.e., the persona-bank, which makes comparisons across questions within an issue-
specific cluster directly interpretable. In contrast, the polling benchmarks are drawn
from different survey organizations and respondent samples, and therefore should not
be interpreted as forming a single, internally comparable scale across clusters.
Accordingly, our evaluation emphasizes within-cluster pattern alignment rather
thancross-clustercomparisons.Wefocusonwhetherpersona-bankresponsesmoveup
as polling benchmark estimates move up and down as polling benchmark estimates
move down across related questions within each issue-specific cluster.
In Panel A, which displays measures of long-term and crystallized attitudes on
abortion and immigration, the Twitter-based persona bank closely tracks polling
benchmarks after calibration, both in magnitude and in direction of question-to-
question changes. The Reddit-based persona bank exhibits larger shifts in absolute
9

levels, particularly for immigration-related items, but preserves consistent directional
patterns that mirror the polling benchmark. As documented in Appendix A, these
differences in magnitude are consistent with known compositional differences in the
Redditsample,whichismoreeducatedandmorepoliticallyliberalthanthepopulation
in general.
Panel B examines event- and time-sensitive questions related to the Epstein files
and U.S. policy toward Venezuela. Despite the additional complexity introduced by
time-sensitive information andheterogeneouspollingsources,persona-bankresponses
again reproduce coherent within-cluster structure. Items eliciting stronger support
in polling data are generally ranked higher by persona-bank responses, while lower-
support items remain comparatively low. This agreement across polling references
strengthens the interpretation that persona-bank responses capture coherent, item-
to-item attitude patterns (that is, consistent changes in direction across related
questions).
Importantly, these trend-alignment patterns are not an artifact of calibration.
When responses are aggregated without weighting, persona-bank estimates continue
to reproduce the same within-cluster directional structure, albeit with substantially
larger deviations in absolute levels. Weighting mainly reduces the magnitude of these
differences, which we attributed to the slection bias, i.e., who is and who is not repre-
sented in the sample. Unweighted results are reported in Appendix F.6, showing that
weighting improves accuracy without changing the main conclusions.
Atthesametime,weobservetwosystematicdeviationsfromtypicalhumansurvey
behavior. For the items asking “whether the Epstein files should be released”, “Has
the Trump administration clearly explained what the U.S. intends to do regarding
Venezuela?” or “Does the Trump administration need to explain...” nearly all simu-
lated respondents selected “Yes,” “has not explained clearly” and “needs to explain”,
whereasattitudesfromreal-worldrespondentsaremoreheterogeneous.Surveyrespon-
dents may answer these questions based on more nuanced consideration, e.g., affect,
partisancues,orgeneraldistrustininstitutions,ratherthantreatingthemasrelatively
factual judgments, the way LLM seems to do.
Another deviation arises for items that implicitly require respondents to reason
through a multi-step mechanism. Consider: “Do you think U.S. military action in
VenezuelawoulddecreasetheamountofdrugscomingintotheU.S.?”Inconventional
survey settings, many respondents do not fully account for the link between policy
interventions and downstream outcomes. Instead, theyoften rely on low-effort heuris-
tics: a response of “Yes, would decrease” can function as an intuitive, affirmation of
the policy, whereas “no effect” can express doubt about the policy with low effort
and without having to explain why. In contrast, simulated agents are systematically
more likely to “work the problem.” They lay out a causal chain (e.g., displacement
of routes, adaptation by trafficking organizations, enforcement fragmentation, and
downstream supply responses) and, after tracing these steps, frequently converge on
“increase”asthemostcoherentimplicationofintervention.Thispatternisconsistent
with established evidence that survey respondents often satisfice rather than opti-
mizewhenquestionsarecognitivelydemanding[36],whereasthesimulatedagentsare
not programmed to reduce effort. These deviations are therefore not random errors,
10

but reflect a systematic difference in how human and simulated agents respond to
surveys. Additional topic- and item-level analyses of these patterns are reported in
Appendix F.4.
Taken together, these results indicate that persona banks can serve as a credible
source of information about public opinion. Even when absolute levels diverge, most
notably for Reddit, the SPIRIT personas reproduce coherent patterns of opinion and
consistent trends. This supports our intuition that persona-based virtual panels (i.e.,
the persona bank) are useful for comparative analysis and rapid-response measure-
ment, especially in settings where traditional surveys are expensive or too slow to
field.
3 Discussion
This study introduces SPIRIT, a semi-structured persona inference framework that
buildsrichrepresentationsofindividualsbasedontheirattributes,inferredfromtheir
social media traces, extending well beyond demographics. Because SPIRIT is built
from an address-based probability panel, the target population is well-defined (i.e.,
US population), and we are able to provide calibration weights to project aggregated
results back to U.S. population benchmarks. Across two complementary evaluations,
wedemonstrateboththevalidityoftheproposedframeworkandthebroaderpotential
of surveying a reusable persona bank for downstream computational social science
analyses.
3.1 From validation to simulation
In the first part of our analysis, we show that SPIRIT personas can faithfully infers
a wide range of self-reported attributes under a strict exact-match evaluation. These
results establish the internal validity of the framework: inferred SPIRIT personas are
notarbitraryabstractions,butcapturemeaningfulindividual-levelsignalsreflectedin
survey responses.
However, recovering self-reported values is not the ultimate objective of persona-
based modeling. Self-reports are inherently limited in scope and timeliness, and many
substantiveresearchquestionsconcernattitudestowardeventsthatunfoldfasterthan
traditional surveys can capture. The second part of our results, therefore, reframes
inferred SPIRIT personas as a persona bank—a virtual respondent panel that can be
queried using standardized survey instruments to study emerging public opinion. Our
findings show that, after appropriate weighting, persona-bank responses reproduce
trends across questions and topics that closely align with contemporaneous polling
benchmarks. This suggests that persona-based virtual panels can serve as a useful
sourceforrapid-response(e.g.,immediatelyafterapoliticaldebateorintheaftermath
of a natural disaster) and exploratory public opinion research.
3.2 Why demographic attributes alone are insufficient
A central insight of this work is that simulating human opinion requires substantially
more information than demographic attributes alone. Although demographics are an
11

important part of who people are, our results show that personas comprised only
of demographic attributes tend to produce compressed response distributions (i.e.,
simulated answers concentrate on a narrow subset of options) and answers that lean
heavily on broad demographic “stereotypes” rather than on person-specific evidence.
Importantly, in our experimental design, we intentionally exclude demographic
attributes from the SPIRIT personas in order to isolate the contribution of non-
demographicsignalsderivedfromusers’historicalposts.Thisdesignchoiceshouldnot
be read as a recommendation to omit demographics in applied settings. On the con-
trary, SPIRIT is designed to accommodate as much relevant information as possible.
The broader goal is to construct personas that are richly grounded in lived experi-
ence,sothemodelreasonsnotaboutwhatatypicalpersonwithcertaindemographics
mightthink,butabouthowaparticularindividualwhohasaparticulardemographic
profile would plausibly respond given their expressed values, beliefs, and behavioral
patterns. In short, demographics are a core component of identity, but they are not
the whole story.
3.3 The role of data richness and user expression
The quality and richness of input data play a critical role in the success of persona-
based inference. In our study, users whose attitudes are most faithfully reconstructed
are typically those who leave dense and expressive digital traces, sharing opinions,
experiences, and reactions across a variety of contexts. This observation highlights an
important boundary condition: persona-based simulation is most effective when users
provide meaningful signals in their language.
At the same time, this limitation also points to future opportunities. Social media
posts are only one source of qualitative information. In principle, personas could be
augmented with additional data sources, such as open-ended and qualitative sur-
vey responses, diaries, or product reviews. Extending persona construction beyond
social media represents a promising direction for building more comprehensive and
structured representations of individuals.
3.4 Opinion questions, factual judgments, and model guardrails
While SPIRIT performs well on many attitudinal questions, we also identify cases
where it diverges from survey benchmarks. In particular, two types of items are more
pronetomismatch.First,themodelismorelikelytodivergeonitemsthatgobeyond
subjective opinion and instead ask respondents to make evaluative judgments, espe-
ciallywhenthosejudgmentscarryastrongmoralorquasi-factualcharacter.Onthese
items, the simulated responses tend to be highly skewed in ways that do not match
theobservedsurveydistributions.Second,forquestionsthataskrespondentstoantic-
ipate downstream consequences and therefore require causal reasoning, the simulated
responses tend to be more consistently extreme and directional than those observed
in human survey data.
These patterns suggest that large language models do not always act purely as
simulators of individual belief states. Instead, they may default to responses shaped
by built-in safety constraints, normative assumptions, or implicit notions of “correct”
12

behavior. In these cases, the model behaves less like a representation of a specific
human respondent and more like a helpful assistant, optimized to produce socially
acceptable or morally justified answers.
Thisdistinctionhighlightsafundamentaltensioninpersona-basedsimulation.For
research purposes, the goal is not to predict what a population should think, nor to
output normatively desirable responses, but to approximate how individuals actually
think and react. Even when explicitly instructed to “be” a particular person, LLMs
may override a persona in situations involving strong moral priors or factual judg-
ments. Future work should examine how to represent the internal contradictions that
characterize individuals, including socially undesirable traits, while also accounting
for the built-in constraints that LLMs impose on harmful speech and behavior.
3.5 Extending persona banks through agentic capabilities
Finally,ourresultspointtowardabroaderresearchagendainwhichpersonabanksare
embedded within agentic systems. To enable simulation of responses to newly unfold-
ing events, we augment persona-based reasoning with selective information retrieval,
allowingagentstoaccesscontemporaneouscontextwhennecessary.Thisdesignparal-
lels recent advances in agent frameworks that integrate search, tool use, and external
observation [37].
More broadly, persona-based agents need not remain respondents. Future work
couldexploremulti-agentinteractionsinwhichpersonasdeliberate,exchangeinforma-
tion, or influence one another, offering a controlled environment for studying opinion
formation, polarization, and social dynamics. When combined with probability-based
weightingandstructuredpersonas,suchsystemsmayprovideavaluableexperimental
testbed for population-level reasoning under well-defined assumptions.
4 Methods
4.1 Data
4.1.1 Panel recruitment and consented account linkage
We partnered with the Ipsos KnowledgePanel, a nationally recruited, probability-
based survey panel (i.e., whose members represent the U.S. population). Panelists
were screened for active usage of Twitter/X and Reddit and invited to consent to
the retrieval of their posts. Consenting participants provided their handles on either
or both platforms, which enabled the collection of their publicly available posts and
linkage to their survey responses. From consenting panelists, we received handles for
1,410 Twitter/X users and 893 Reddit users, including 452 individuals who provided
accounts on both platforms.
Importantly,althoughpanelistsprovidedhandles,notallofthesubmittedhandles
were valid or retrievable at the time of data collection. For example, some handles
contained typographical errors, were suspended/deleted, or pointed to accounts that
were private or otherwise inaccessible via the platform APIs. We therefore retained
only handles that could be associated with (i) an account and (ii) publicly accessible
content that could be retrieved through the APIs.
13

4.1.2 Post collection and linkage to survey responses
For each valid handle, we collected all publicly available posts retrievable via the
platform’sAPIs,subjecttoplatformaccessconstraintsatthetimeofcollection.These
posts were linked to their attitudes and preferences maintained by Ipsos, enabling the
construction and evaluation of the individualized personas (Appendix C).
This design thus supports persona-based simulation evaluation by providing: (i)
respondent-level ground truth for opinions and attitudes (via Ipsos survey responses
collected independently of this work), (ii) longitudinal, historical text traces for per-
sona construction (via all public posts), and (iii) a probability-based sampling frame
with survey weights, enabling simulation fidelity to be assessed not only at the indi-
viduallevelbutalsointermsofpopulation-calibratedaggregatesbenchmarkedtothe
U.S. adult population.
4.2 SPIRIT framework
Fig. 3 Overview of the SPIRIT framework. A probability-based sample from the Ipsos Knowl-
edgePanelislinkedtorespondents’socialmediaaccounts,andtheirhistoricalpostsarecollectedto
infer structured user personas with a painter model. These inferred personas form a persona bank
that serves as digital twins for Stage 2 reasoning, where a reasoner model simulates responses to
downstreamtaskssuchassurveyitems.ThesimulatedresponsesarethenweightedtoproduceU.S.
population-levelestimates.
We propose SPIRIT (Semi-structured Persona Inference and Reasoning for
IndividualizedTrajectories),atwo-stageframeworkforgroundingLLM-basedsimula-
tionininterpretable,semi-structured,andfaithfulpersonasinferredfromsocialmedia
traces. As illustrated in Figure 3, SPIRIT comprises (i) a Painter module that infers
14

a multi-dimensional persona profile from a user’s social media posts, and (ii) a Rea-
soner module that prompts an LLM on the inferred persona to simulate structured
| responses    | for downstream |     | tasks   | (e.g.,    | survey-style | items). |     |
| ------------ | -------------- | --- | ------- | --------- | ------------ | ------- | --- |
| 4.2.1 Inputs |                | and | persona | artifacts |              |         |     |
For each user, the system consumes a single concatenated document consisting of all
available historical posts from Reddit and Twitter/X, ordered by timestamp (each
postisassociatedwithitsoriginalpostingtime).ThePainteroutputs(detailedscheme
can be seen in Appendix G): (i) a semi-structured persona profile encoded as a
JSON (JavaScript Object Notation) object that captures psychologically and socially
meaningfulattributes(e.g.,traits,worldbeliefs,values/identities,attitudes),together
with uncertainty annotations; and (ii) a narrative persona that summarizes the
| profile in | readable | third-person |     | form. |     |     |     |
| ---------- | -------- | ------------ | --- | ----- | --- | --- | --- |
In external survey experiments, demographic attributes (e.g., age, gender, race,
party identification) are loaded from user profiles and provided as supplementary
| content        | during  | downstream      | prompting. |     |         |           |            |
| -------------- | ------- | --------------- | ---------- | --- | ------- | --------- | ---------- |
| 4.2.2 Painter: |         | semi-structured |            |     | persona | inference | from posts |
| Persona        | schema. |                 |            |     |         |           |            |
Thepersonaprofilefollowsafixedschemathatisdesignedtobe(i)multi-dimensional,
covering traits (Big Five), worldview beliefs, values/identities, and domain attitudes,
and(ii)auditable,withexplicituncertaintyscoresandbriefjustifications.Theschema
is implemented as a typed data model to enforce structural consistency across users.
| Inference | procedure. |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- |
Given a user’s posts, the Painter infers persona attributes by synthesizing recurring
linguistic signals (e.g., affect, self-references, moral language, expressed preferences,
and stance patterns) into the persona schema. To reduce overinterpretation, Painter
is instructed to treat all inferences as probabilistic and to express low confidence
when evidence is weak. Prompt templates and an illustrative example are provided in
| Appendix        | G.2. |         |     |           |     |            |       |
| --------------- | ---- | ------- | --- | --------- | --- | ---------- | ----- |
| 4.2.3 Reasoner: |      | persona |     | inference | for | downstream | tasks |
Task formulation.
TheReasoneranswersdownstreamquestionsbypromptinganLLMwiththeinferred
persona (and demographic attributes when available). For each question, the output
includes: (i) a selected response option (value/label), (ii) a categorical confidence rat-
ing, and (iii) a brief textual rationale grounded in persona evidence. This formulation
supports survey-style prediction enriched with qualitative evidence, as well as model
| uncertainty | when | persona | signals | are | ambiguous. |     |     |
| ----------- | ---- | ------- | ------- | --- | ---------- | --- | --- |
15

4.2.4 Calibration weights via raking to Census/ACS margins
The persona bank requires respondents to (i) have a social media account, (ii) have
ever posted, and (iii) consent to link. Because not everyone in the panel necessar-
ily conforms to these requirements, the resulting sample might deviate from the U.S.
adult population in basic composition. To reduce this type of selection bias, we con-
struct weights that calibrate the persona-bank marginals to external U.S. population
benchmarks.
Benchmarks.
We use marginal distributions from U.S. Census and ACS releases as targets: gender
(2020 Census), race/ethnicity (2020 Census), region (2020 Census), and age and edu-
cation (ACS 2022; education among adults 25+). We additionally include the panel
variable corresponding to the candidate for whom the respondent voted in the 2024
U.S. presidential election, using the election results (three-category vote preference)
as a calibration margin.
Variables and preprocessing.
Weights are computed for respondents included in the persona bank. We rake on six
margins: PPGENDER, PPEDUC5, PPETHM, PPREG4, age group, and candidate2024. Age
is discretized into four groups (18–29, 30–44, 45–64, 65+).
Raking procedure.
We apply iterative proportional fitting (raking) to match each sample margin to its
target [38]. Starting from equal base weights w(0) = 1, we iterate over margins and
i
update weights by multiplying an adjustment factor for the respondent’s category:
T
w ←w × v,c,
i i Pˆ
v,c
where T is the benchmark proportion for category c of variable v, and Pˆ is the
v,c v,c
current weighted sample proportion for that category. We cycle through all mar-
gins repeatedly until convergence (maximum absolute adjustment tol < 0.001) or a
maximum of 50 iterations.
Normalization and use.
Afterraking,werescaleweightstohavemean1withinthepersonabank,w ←w /w¯,
i i
so weighted estimates preserve the sample’s effective scale. These weights are then
used to compute weighted population-level aggregates of simulated survey responses
from the persona bank. After normalization (mean = 1), the raking weights show
moderate dispersion: SD=1.32, median =0.63 (IQR: 0.30–1.23), with a minimum of
0.012 and a maximum of 14.42 (n=1517).
16

| 4.3 Position-weighted |     | user-level |     | response |     | composite | score |     |
| --------------------- | --- | ---------- | --- | -------- | --- | --------- | ----- | --- |
Tosummarizeeachrespondent’soverallresponsepatternacrossthesurvey,weconvert
item-level outputs into a single user-level composite score. Let i index users and q ∈
{1,...,Q} index survey items, where Q=52 in the main analysis. Each item has an
inferred numeric response yˆ (and, for human benchmarks, an observed self-report
iq
y ).
iq
We first assign each question a deterministic position weight based on its location
in the survey sequence. In implementation, we take the set of unique question IDs
appearing in the analysis data, order them according to the survey sequence used in
the questionnaire, and assign weights w ∈ {1,...,Q} so that earlier items receive
q
| smaller weights | and later items | receive | larger | weights: |     |     |     |     |
| --------------- | --------------- | ------- | ------ | -------- | --- | --- | --- | --- |
|                 |                 |         | w      | =q.      |     |     |     | (1) |
q
| We then compute | the position-weighted |     |     | mean | for each | user: |     |     |
| --------------- | --------------------- | --- | --- | ---- | -------- | ----- | --- | --- |
(cid:80)Q
w yˆ
|          |                         |     | y¯ˆpos = | q=1       | q iq .    |            |     | (2) |
| -------- | ----------------------- | --- | -------- | --------- | --------- | ---------- | --- | --- |
|          |                         |     | i        | (cid:80)Q | w         |            |     |     |
|          |                         |     |          | q=1       | q         |            |     |     |
| We apply | the same transformation |     | to the   | human     | benchmark | responses: |     |     |
(cid:80)Q
w y
|     |     |     | y¯pos | q=1       | q iq |     |     |     |
| --- | --- | --- | ----- | --------- | ---- | --- | --- | --- |
|     |     |     | =     |           | .    |     |     | (3) |
|     |     |     | i     | (cid:80)Q | w    |     |     |     |
|     |     |     |       | q=1       | q    |     |     |     |
Thiscompositescoreisfullydeterministicandmodel-agnostic.Becauselateritems
receive larger weights, the summary retains information about the survey order-
ing while yielding a compact scalar representation of each user’s 52-item response
sequence. In the empirical analysis, we compute y¯ˆpos for each model and experimen-
|     |     |     |     |     | i   |     |     | y¯pos |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
tal condition and compare its distribution to the corresponding distribution of
i
| among human  | respondents. |        |       |      |        |        |     |     |
| ------------ | ------------ | ------ | ----- | ---- | ------ | ------ | --- | --- |
| 4.4 External | survey       | stress | tests | with | timely | events |     |     |
| Motivation   | and topics.  |        |       |      |        |        |     |     |
To evaluate whether persona-conditioned simulation can handle both stable attitudes
and time-sensitive information needs, we constructed external survey item sets span-
ningfourwidelydiscussedtopicsatthetimeofwriting:abortion,theEpsteinfiles,U.S.
actionsrelatedtoVenezuela,andimmigrationpolicy.TheEpstein-fileandVenezuela-
action conditions were treated as time-sensitive cases where events may plausibly
| post-date | model training (i.e., | will | not be | included | in  | the training | data). |     |
| --------- | --------------------- | ---- | ------ | -------- | --- | ------------ | ------ | --- |
| Runtime   | stack.                |      |        |          |     |              |        |     |
Generation is performed through a locally deployed, OpenAI-compatible vLLM end-
point,usinggoogle/gemma-3-27b-itasthebasemodel.Fortime-sensitiveconditions,
17

thepipelineincorporatesawebsearchcomponent(i.e.,Tavily,whichisconfiguredvia
a search backend) to obtain up-to-date context before answering.
4.4.1 Time-sensitive protocol: persona-guided information
acquisition
For time-sensitive topics, we use a lightweight information acquisition protocol. The
model first elicits the persona’s pre-existing impressions, then generates persona-
consistent search queries and summarizes retrieved information, and finally answers
survey items conditioned on both persona and the synthesized context. This design
separates prior beliefs from newly acquired context, allowing us to examine whether
access to recent information changes inferred responses in a direction consistent with
the persona.
4.4.2 Stable-attitude protocol: direct persona-conditioned answers
For attitudes often treated as crystallized (e.g., on topics such as abortion and
immigration policy), the model answers directly without external search, producing
survey-style responses conditioned only on persona and demographics.
Appendix materials.
Full prompt templates, schema specifications, and example model inputs/outputs for
both Painter and Reasoner are provided in Appendix G.
Acknowledgements. We thank the U.S. Census Bureau for supporting this
research.WealsothankIpsosforprovidingaccesstosurveydataandfortheirsupport
of the external benchmarking component.
Declarations
• Funding. The author(s) disclosed receipt of the following financial support for the
research, authorship, and/or publication of this article: This work was supported
by the U.S. Census Bureau under CB20ADR0160002.
• Conflict of interest / Competing interests.Theauthorsdeclarenocompeting
interests.
• Ethics approval and consent to participate. This study was conducted under
IRB approval (HUM00259279), with informed consent from all participants. This
studyusesobservational,user-generatedcontentfrompublicsocialmediaplatforms
(Reddit and Twitter/X) and does not involve any interaction or intervention with
humanparticipants.Becausethecontentwasnotcollectedwithconsentforredistri-
bution,wetreatboththeunderlyingpostsandderivedpersonaartifactsassensitive
research materials and adopt a data-minimization approach in dissemination.
• Consent for publication. We do not publish raw social media posts, user-
names/handles, or direct identifiers. Any illustrative examples in the manuscript
are paraphrased to reduce re-identification risk.
• Data availability.Tobalancetransparencywithprivacy,wewillrelease(i)aggre-
gated results reported in the paper and (ii) data products for the external survey
18

benchmarkingcomponent,includingthesurveyquestionsets,responseoptions,and
item-levelmodeloutputsusedforcomparison.Wedonotpubliclyreleasetheunder-
lyingrawsocialmediapostsorfullpersonaartifacts(semi-structuredpersonaJSON
and narrative personas), as these may contain personally identifiable information
or enable re-identification through linkage. Researchers who require access to per-
sona artifacts for verification or extension may contact the corresponding author to
| discuss | controlled-access | arrangements. |     |     |     |     |     |
| ------- | ----------------- | ------------- | --- | --- | --- | --- | --- |
•
Materials availability. All non-sensitive study materials (e.g., external survey
instruments, mapping tables, and evaluation scripts) will be made available with
thepublicreleaseoftheexternalsurveycomponent.Materialsthatdirectlycontain
or reconstruct user-level social media traces will be withheld from public release.
•
Code availability.CodefortheSPIRITpipeline(PainterandReasonermodules),
the externalsurveystudy, andthe analysis scriptswill bereleasedupon acceptance
of the manuscript. The release will include documentation sufficient to reproduce
thereportedexternalsurveyexperimentsusingthepubliclyavailablematerials,and
guidance for running persona-based simulations under controlled data access.
| Appendix | A   | Ipsos       | KnowledgePanel |     |              | Participant |     |
| -------- | --- | ----------- | -------------- | --- | ------------ | ----------- | --- |
|          |     | Demographic |                |     | Distribution |             |     |
This section details the demographic composition of the participants drawn from the
Ipsos KnowledgePanel for the Twitter and Reddit arms of the study (see Table A1).
The sample distribution reflects several key characteristics of social media users
that deviate from U.S. Census benchmarks. Notably, both samples are more male-
dominated(approx.61%)andhighlyeducated(over50%withaBachelor’sdegree)
thanthegeneralpopulation.Politicalideologyisskewedtowardtheleft,particularly
onReddit,where58.8%ofparticipantsidentifyassomelevelofLiberal.Additionally,
the Reddit sample is significantly younger than the Twitter sample, with 76.1% of
| respondents   | falling under | the           | age of | 45, compared | to 56%      | for Twitter. |     |
| ------------- | ------------- | ------------- | ------ | ------------ | ----------- | ------------ | --- |
| Appendix      | B             | Experimental  |        |              | Environment |              | and |
|               |               | Computational |        |              | Cost        |              |     |
| B.1 Computing |               | Environment   |        |              |             |              |     |
All framework-level experiments were conducted on a single-node, multi-GPU system
equipped with 8 NVIDIA H100 GPUs (80GB memory each). Model infer-
ence was deployed using vLLM with bfloat16 (BF16) precision, enabling efficient
batched inference while maintaining numerical stability for long-context inputs.
The system was configured to support long input sequences required for persona
inference from social media histories. No gradient computation or model fine-tuning
| was performed; | all experiments |     | were | conducted | in inference-only |     | mode. |
| -------------- | --------------- | --- | ---- | --------- | ----------------- | --- | ----- |
19

Table A1 DemographicCharacteristicsofTwitterandRedditParticipants
|     |                |     | Twitter(N | =1,031) | Reddit(N =774) |
| --- | -------------- | --- | --------- | ------- | -------------- |
|     | Characteristic |     | n         | %       | n %            |
Gender
|     | Male   |     | 628 | 60.9 | 475 61.4 |
| --- | ------ | --- | --- | ---- | -------- |
|     | Female |     | 403 | 39.1 | 299 38.6 |
Age Category
|     | 18–29 |     | 192 | 18.6 | 197 25.5 |
| --- | ----- | --- | --- | ---- | -------- |
|     | 30–44 |     | 386 | 37.4 | 392 50.6 |
|     | 45–60 |     | 290 | 28.1 | 135 17.4 |
|     | 60+   |     | 163 | 15.8 | 50 6.5   |
Race/Ethnicity
|     | White,Non-Hispanic   |     | 665 | 64.5 | 525 67.8 |
| --- | -------------------- | --- | --- | ---- | -------- |
|     | Hispanic             |     | 146 | 14.2 | 108 14.0 |
|     | Black,Non-Hispanic   |     | 113 | 11.0 | 45 5.8   |
|     | 2+Races,Non-Hispanic |     | 54  | 5.2  | 46 5.9   |
|     | Other,Non-Hispanic   |     | 53  | 5.1  | 50 6.5   |
Education
|     | Bachelor’sdegreeorhigher |     | 545 | 52.9 | 427 55.2 |
| --- | ------------------------ | --- | --- | ---- | -------- |
|     | Somecollege/Associate’s  |     | 285 | 27.6 | 205 26.5 |
|     | HSGraduate/GED           |     | 150 | 14.5 | 74 9.6   |
|     | NoHSdiploma              |     | 28  | 2.7  | 21 2.7   |
Urbanicity
|     | Urban    |     | 430 | 41.7 | 346 44.7 |
| --- | -------- | --- | --- | ---- | -------- |
|     | Suburban |     | 443 | 43.0 | 330 42.6 |
|     | Rural    |     | 157 | 15.2 | 97 12.5  |
Political Ideology
|     | Liberal      |            | 437 | 42.4 | 455 58.8 |
| --- | ------------ | ---------- | --- | ---- | -------- |
|     | Moderate     |            | 275 | 26.7 | 189 24.4 |
|     | Conservative |            | 306 | 29.7 | 124 16.0 |
|     | Refused      |            | 13  | 1.3  | 6 0.8    |
| B.2 | Token-Level  | Accounting |     |      |          |
To provide a transparent and model-agnostic estimate of computational usage, we
reportaggregatedinput andoutput tokencountsratherthanwall-clocktimeorGPU-
hours. This choice reflects the fact that inference cost is primarily driven by token
volume and sequence length, while runtime depends on deployment-specific factors
| such as | batching strategy | and hardware | utilization. |     |     |
| ------- | ----------------- | ------------ | ------------ | --- | --- |
Table B2 summarizes total token usage across platforms for framework execution.
Table B2 Aggregatedtokenusageby
platform
|     |     | Platform | Inputtokens | Outputtokens |     |
| --- | --- | -------- | ----------- | ------------ | --- |
|     |     | Reddit   | 41,924,612  | 12,650,506   |     |
|     |     | Twitter  | 77,077,952  | 9,715,741    |     |
20

Input tokens include persona inference prompts as well as persona-conditioned
reasoning prompts. Output tokens correspond to structured persona representations
| and downstream | generated       | responses. |             |     |     |
| -------------- | --------------- | ---------- | ----------- | --- | --- |
| B.3            | Cost Estimation | and        | Variability |     |     |
We intentionally do not report GPU-hours or exact cost. Token-level account-
ing provides an order-of-magnitude indication of computational scale that remains
| comparable | across hardware | and deployment |     | environments. |     |
| ---------- | --------------- | -------------- | --- | ------------- | --- |
Actual runtime and cost may vary substantially depending on batching efficiency,
concurrency, and hardware utilization. Moreover, the framework incorporates struc-
turedoutputvalidationusingaschema-basedmechanismimplementedwithPydantic,
| which introduces | controlled | variability | in  | generation | cost. |
| ---------------- | ---------- | ----------- | --- | ---------- | ----- |
Specifically, model outputs are validated against a predefined JSON schema, with
a retry mechanism capped at ten attempts per prompt. In practice, the number of
retries required depends strongly on model capability: higher-capacity models exhibit
substantially higher compliance rates with the schema and therefore require fewer
retries. As a result, the reported token counts should be interpreted as coarse-grained
| estimates | rather than exact | execution | costs. |     |     |
| --------- | ----------------- | --------- | ------ | --- | --- |
These sources of variability reflect engineering trade-offs rather than conceptual
| limitations | of the proposed        | framework. |     |     |     |
| ----------- | ---------------------- | ---------- | --- | --- | --- |
| B.4         | Practical Implications |            |     |     |     |
Despite these sources of variability, the overall computational footprint of the frame-
workremainswellwithinthereachoftypicalacademicresearchenvironments.Because
personainferenceisperformedonceperuserandthenreusedformultipledownstream
tasks,thecostofpersonaconstructioncanbeamortizedacrossanalysesandscenarios.
Importantly, the framework does not rely on model fine-tuning or large-scale retrain-
ing, making population-level experiments feasible without prohibitive computational
overhead.
A key practical constraint is the reliability of persona construction. Although we
implement a retry mechanism (up to ten attempts) to enforce schema-compliant out-
puts, smaller models (Gemma-3-4B and LLaMA-3.1-8B) still fail to produce valid
persona representations for a nontrivial fraction of users. These failures propagate to
downstream reasoning and reduce overall performance, suggesting a minimum model
capacityrequirementforrobustdeployment.Accordingly,wereportresultsfromthese
smaller models only as a reference point; they should not be interpreted as definitive
| evidence | about the framework’s | performance. |     |     |              |
| -------- | --------------------- | ------------ | --- | --- | ------------ |
| Appendix | C Data                | Dictionary   |     |     | and Variable |
Definitions
This section details the complete set of survey questions collected from Ipsos Knowl-
edgePanel and used in the evaluation (see Table C3). The table below maps the
21

internal variable identifiers (e.g., pph10221) to the verbatim question text presented
| to participants | and | the available | response |           | options. |              |              |            |     |     |
| --------------- | --- | ------------- | -------- | --------- | -------- | ------------ | ------------ | ---------- | --- | --- |
|                 |     | Table C3:     | Survey   | Questions |          | and Response | Options      | Dictionary |     |     |
| Variable        |     | Question      |          | Text      |          |              | Response     | Options    |     |     |
| QFLAG           |     | QFLAG         |          |           |          |              | 1: Qualified |            |     |     |
2: Terminated
3: Partial
4: Non-responder
| pph10221 |     | Q37: | Do you | NOW | smoke | cigarettes? | 1: Every | day |     |     |
| -------- | --- | ---- | ------ | --- | ----- | ----------- | -------- | --- | --- | --- |
2: Some days
|          |     |           |      |               |        |               | 3: Not    | at all |     |     |
| -------- | --- | --------- | ---- | ------------- | ------ | ------------- | --------- | ------ | --- | --- |
| ppsi1916 |     | Q210:     | Do   | you currently |        | use mari-     | 1: Every  | day    |     |     |
|          |     | juana...? |      |               |        |               | 2: Some   | days   |     |     |
|          |     |           |      |               |        |               | 3: Not    | at all |     |     |
| pph21906 |     | Q110:     | How  | often         | do you | think         | 1: Never  |        |     |     |
|          |     | vaccines  | have | dangerous     |        | side effects? | 2: Rarely |        |     |     |
3: Sometimes
4: Often
5: Very often
pph21908 Q130: Overall do you think 1: The benefits... outweigh the risks
|          |     |         |          |         |               |          | 2: The       | risks... | outweigh | the benefits |
| -------- | --- | ------- | -------- | ------- | ------------- | -------- | ------------ | -------- | -------- | ------------ |
| pph20030 |     | Q49:    | Overall, | how     | do you        | rate the | 1: Excellent |          |          |              |
|          |     | quality | of       | medical | care received | from     | 2: Very      | good     |          |              |
|          |     | your    | regular  | doctor  | in the        | past 12  | 3: Good      |          |          |              |
|          |     | months? |          |         |               |          | 4: Fair      |          |          |              |
5: Poor
|     |     |     |     |     |     |     | 6: Have   | not seen... |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | --- |
|     |     |     |     |     |     |     | 7: Do not | have...     |     |     |
pph20031 Q50: Overall, how satisfied are you 1: Very satisfied
|     |     | with | your | healthcare | coverage? |     | 2: Moderately |           | satisfied |     |
| --- | --- | ---- | ---- | ---------- | --------- | --- | ------------- | --------- | --------- | --- |
|     |     |      |      |            |           |     | 3: Slightly   | satisfied |           |     |
4: Not satisfied
| vote2024 |     | QPID600f:    |           | Did you | happen    | to vote in | 1: Yes |     |     |     |
| -------- | --- | ------------ | --------- | ------- | --------- | ---------- | ------ | --- | --- | --- |
|          |     | the November |           | 2024    | elections | for the    | 2: No  |     |     |     |
|          |     | U.S.         | President | and     | Congress? |            |        |     |     |     |
candidate2024 QPID600g: Which candidate did 1: Kamala Harris (Democrat)
|     |     | you       | vote for | in the | 2024 | Presidential | 2: Donald  | Trump        | (Republican) |              |
| --- | --- | --------- | -------- | ------ | ---- | ------------ | ---------- | ------------ | ------------ | ------------ |
|     |     | election? |          |        |      |              | 3: Another | candidate... |              |              |
|     |     |           |          |        |      |              |            |              | Continued    | on next page |
22

|             | Table                | C3   | – continued | from | previous page |         |
| ----------- | -------------------- | ---- | ----------- | ---- | ------------- | ------- |
| Variable    | Question             | Text |             |      | Response      | Options |
| urb sub rur | Urban/Suburban/Rural |      |             |      | 1: Urban      |         |
2: Rural
3: Suburban
| ppcm1301 | GOVEMP1: | Employer |     | type | 1: Government         |                 |
| -------- | -------- | -------- | --- | ---- | --------------------- | --------------- |
|          |          |          |     |      | 2: Private-for-profit | company         |
|          |          |          |     |      | 3: Non-profit         | organization... |
4: Self-employed
|      |             |                |     |                | 5: Working     | in family business |
| ---- | ----------- | -------------- | --- | -------------- | -------------- | ------------------ |
| E140 | E140: Which | category       |     | best describes | 1: Entry       | level              |
|      | your level  | of employment? |     |                | 2: Experienced | (non-manager)      |
3: Manager/Supervisor...
4: Executive...
MilVet 1 DOV: Current Service Member 1: Current Service Member
MilVet 2 DOV: Veteran Service Member 1: Veteran Service Member
| MilVet 3 | DOV: Non-Military |         |             |          | 1: Non-Military |     |
| -------- | ----------------- | ------- | ----------- | -------- | --------------- | --- |
| pppa1640 | Q254: Have        | you     | ever been   | a member | 1: Yes          |     |
|          | of the Reserve    |         | or National | Guard?   | 2: No           |     |
| pppa1648 | Q26: What         | is your | religion?   |          | 1: Catholic     |     |
2: Evangelical/Protestant...
|     |     |     |     |     | 3: Jehovah’s | Witness |
| --- | --- | --- | --- | --- | ------------ | ------- |
4: LDS (Mormon)
5: Jewish
6: Islam/Muslim
7: Orthodox
8: Hindu
9: Buddhist
10: Unitarian
|     |     |     |     |     | 11: Other | Christian     |
| --- | --- | --- | --- | --- | --------- | ------------- |
|     |     |     |     |     | 12: Other | non-Christian |
13: No religion
| ppp20197 | QEG22: | Are you | a citizen | of the | 1: Yes |     |
| -------- | ------ | ------- | --------- | ------ | ------ | --- |
|          | United | States? |           |        | 2: No  |     |
votereg now Are you currently registered to vote in 1: Yes, registered
|     | the U.S.? |     |     |     | 3: No, not | registered |
| --- | --------- | --- | --- | --- | ---------- | ---------- |
4: Not sure
|     |     |     |     |     | 5: No, not | eligible |
| --- | --- | --- | --- | --- | ---------- | -------- |
Continued on next page
23

|          | Table       | C3 – continued | from        | previous page |         |     |
| -------- | ----------- | -------------- | ----------- | ------------- | ------- | --- |
| Variable | Question    | Text           |             | Response      | Options |     |
| ppfs1482 | Q108: Where | do you think   | your credit | 1: Very       | poor    |     |
|          | score falls |                |             | 2: Poor       |         |     |
3: Fair
4: Good
5: Excellent
6: Don’t know
| pph10001 | Q1: In general, | would you | say your | 1: Excellent |      |     |
| -------- | --------------- | --------- | -------- | ------------ | ---- | --- |
|          | health is.      | . .?      |          | 2: Very      | good |     |
3: Good
4: Fair
5: Poor
| pph11301 | Q25 1:        | Are you a caregiver | for one or | 1: Yes |     |     |
| -------- | ------------- | ------------------- | ---------- | ------ | --- | --- |
|          | more children | under the           | age of 18? | 2: No  |     |     |
ppp10035 Q16: In general, how interested are 1: Very interested
|          | you in politics | and public | affairs?   | 2: Somewhat              | interested          |           |
| -------- | --------------- | ---------- | ---------- | ------------------------ | ------------------- | --------- |
|          |                 |            |            | 3: Slightly              | interested          |           |
|          |                 |            |            | 4: Not at                | all interested      |           |
| ppcm0160 | Q26: Occupation | (detailed) | in current | 1: Management            |                     |           |
|          | or main         | job        |            | 2: Business/Financial... |                     |           |
|          |                 |            |            | (See full                | list in data source | for codes |
3-35)
$25,000
| ppfsasset | Q22: Approx  | total amount   | of house- | 1: Under |           |     |
| --------- | ------------ | -------------- | --------- | -------- | --------- | --- |
|           | hold savings | and investable | assets?   | 2: $25k  | - $49,999 |     |
|           |              |                |           | $50k     | $99,999   |     |
3: -
|     |     |     |     | 4: $100k | - $249,999 |     |
| --- | --- | --- | --- | -------- | ---------- | --- |
|     |     |     |     | 5: $250k | - $499,999 |     |
|     |     |     |     | $500k    | $999,999   |     |
6: -
|     |     |     |     | 7: $1M | - $1.9M |     |
| --- | --- | --- | --- | ------ | ------- | --- |
$2M
|     |     |     |     | 8:  | or more |     |
| --- | --- | --- | --- | --- | ------- | --- |
9: Not sure
ppc21505 CU40: How concerned are you about 1: Not at all concerned
|     | providing     | personal information | over | 2: Slightly | concerned |     |
| --- | ------------- | -------------------- | ---- | ----------- | --------- | --- |
|     | the internet? |                      |      | 3: Somewhat | concerned |     |
4: Very concerned
| E104 RET | E104: Do  | any of the following |               | 1: Yes |           |              |
| -------- | --------- | -------------------- | ------------- | ------ | --------- | ------------ |
|          | currently | describe you?        | ... [Retired] | 2: No  |           |              |
|          |           |                      |               |        | Continued | on next page |
24

|           | Table     | C3          | – continued |     | from | previous | page |         |
| --------- | --------- | ----------- | ----------- | --- | ---- | -------- | ---- | ------- |
| Variable  | Question  | Text        |             |     |      | Response |      | Options |
| E104 STUD | E104: ... | [A student] |             |     |      | 1:       | Yes  |         |
2: No
| E104 STAYHOM  | E104: ...     | [A stay-at-home         |                     | spouse   | or     | 1:  | Yes      |       |
| ------------- | ------------- | ----------------------- | ------------------- | -------- | ------ | --- | -------- | ----- |
|               | partner]      |                         |                     |          |        | 2:  | No       |       |
| E104 INTERN   | E104: ...     | [Unpaid                 | job/internship/vol- |          |        | 1:  | Yes      |       |
|               | unteer]       |                         |                     |          |        | 2:  | No       |       |
| E104 FREELANC | E104: ...     | [Freelancer/independent |                     |          |        | 1:  | Yes      |       |
|               | contractor]   |                         |                     |          |        | 2:  | No       |       |
| pph10301-7    | Q39/Q40:      | Alcohol                 | consumption         |          | (Beer, | 0:  | No       |       |
|               | Wine, Liquor) |                         |                     |          |        | 1:  | Yes      |       |
| pph21901-5    | Q100: Vaccine |                         | attitudes           | (Series) |        | 1:  | Do not   | agree |
|               |               |                         |                     |          |        | 2:  | Somewhat | agree |
3: Agree
|          |             |                |             |       |         | 4:  | Strongly       | agree    |
| -------- | ----------- | -------------- | ----------- | ----- | ------- | --- | -------------- | -------- |
| ppc21607 | CU44:       | I use social   | network     | sites | to      | 1:  | Do not         | agree    |
|          | communicate |                | with others | more  | than    | 2:  | Somewhat       | agree    |
|          | email...    |                |             |       |         | 3:  | Agree          |          |
|          |             |                |             |       |         | 4:  | Strongly       | agree    |
| pph1*    | Q19/Q19a:   | Medical/Mental |             |       | Health  | 0:  | No             |          |
|          | Conditions  | (ADHD,         | Anxiety,    |       | Depres- | 1:  | Yes (Condition | present) |
sion, etc.)
| ppm2223* | Q9: News  | Sources | (TV,   | Paper, |     | 0:  | No  |     |
| -------- | --------- | ------- | ------ | ------ | --- | --- | --- | --- |
|          | Internet, | Radio,  | Social | Media) |     | 1:  | Yes |     |
ppp20072 Q27: How often do you attend 1: More than once a week
|     | religious | services? |     |     |     | 2:  | Once a    | week         |
| --- | --------- | --------- | --- | --- | --- | --- | --------- | ------------ |
|     |           |           |     |     |     | 3:  | 1-2 times | a month      |
|     |           |           |     |     |     | 4:  | Few times | a year       |
|     |           |           |     |     |     | 5:  | Once a    | year or less |
6: Never
| ppp22210 | Q34: Household |     | gun ownership |     |     | 1:  | Yes |     |
| -------- | -------------- | --- | ------------- | --- | --- | --- | --- | --- |
2: No
| ppp22211 | Q36: Personal |     | gun ownership |     |     | 1:  | Yes |     |
| -------- | ------------- | --- | ------------- | --- | --- | --- | --- | --- |
2: No
Continued on next page
25

|          | Table        | C3      | – continued   | from   | previous | page           |             |
| -------- | ------------ | ------- | ------------- | ------ | -------- | -------------- | ----------- |
| Variable | Question     | Text    |               |        | Response |                | Options     |
| ppm22229 | Q10: How     | closely | do you        | follow | 1:       | Very closely   |             |
|          | politics...? |         |               |        | 2:       | Fairly closely |             |
|          |              |         |               |        | 3:       | Not very       | closely     |
|          |              |         |               |        | 4:       | Not at         | all closely |
| vote2020 | Did you      | happen  | to vote       | in the | 1:       | Yes            |             |
|          | November     | 2020    | elections...? |        | 2:       | No             |             |
candidate2020 Which candidate did you vote for in 1: Joe Biden (Democrat)
|          | the 2020       | Presidential | election? |             | 2:  | Donald     | Trump (Republican) |
| -------- | -------------- | ------------ | --------- | ----------- | --- | ---------- | ------------------ |
|          |                |              |           |             | 3:  | Another    | candidate          |
| partyid7 | DERIVED:       | Political    | party     | affiliation | 1:  | Strong     | Rep                |
|          | (7 categories) |              |           |             | 2:  | Not Strong | Rep                |
3: Leans Rep
4: Undecided/Ind/Other
5: Leans Dem
|          |          |          |        |          | 6:  | Not Strong    | Dem     |
| -------- | -------- | -------- | ------ | -------- | --- | ------------- | ------- |
|          |          |          |        |          | 7:  | Strong        | Dem     |
| ppp10012 | Q11: In  | general, | do you | think of | 1:  | Extr. liberal |         |
|          | yourself | as...    |        |          | 2:  | Liberal       |         |
|          |          |          |        |          | 3:  | Slightly      | liberal |
4: Moderate
|     |     |     |     |     | 5:  | Slightly | conservative |
| --- | --- | --- | --- | --- | --- | -------- | ------------ |
6: Conservative
7: Extr. conservative
| PPEDUCAT | Education | (4  | Categories) |     | 1:  | No HS | diploma |
| -------- | --------- | --- | ----------- | --- | --- | ----- | ------- |
2: HS grad
3: Some college/Assoc
|        |                  |     |     |     | 4:  | Bachelor’s      | or higher |
| ------ | ---------------- | --- | --- | --- | --- | --------------- | --------- |
| PPETHM | Race / Ethnicity |     |     |     | 1:  | White,          | Non-Hisp  |
|        |                  |     |     |     | 2:  | Black, Non-Hisp |           |
|        |                  |     |     |     | 3:  | Other, Non-Hisp |           |
4: Hispanic
|          |        |     |     |     | 5:  | 2+ Races, | Non-Hisp |
| -------- | ------ | --- | --- | --- | --- | --------- | -------- |
| PPGENDER | Gender |     |     |     | 1:  | Male      |          |
2: Female
Continued on next page
26

|          |     | Table    | C3 –    | continued | from     | previous     | page    |
| -------- | --- | -------- | ------- | --------- | -------- | ------------ | ------- |
| Variable |     | Question | Text    |           |          | Response     | Options |
| PPREG4   |     | Region 4 | - Based | on State  | of Resi- | 1: Northeast |         |
|          |     | dence    |         |           |          | 2: Midwest   |         |
3: South
4: West
| PPRENT |     | Ownership | Status | of Living | Quarters | 1: Owned |     |
| ------ | --- | --------- | ------ | --------- | -------- | -------- | --- |
2: Rented
|          |     |            |     |     |     | 3: Occupied  | w/o rent |
| -------- | --- | ---------- | --- | --- | --- | ------------ | -------- |
| PPMSACAT |     | MSA Status |     |     |     | 0: Non-Metro |          |
1: Metro
| PPEDUC5 |     | Education | (5 Categories) |     |     | 1: No | HS  |
| ------- | --- | --------- | -------------- | --- | --- | ----- | --- |
2: HS grad
3: Some college
4: Bachelor’s
|        |     |           |        |     |     | 5: Master’s | or higher |
| ------ | --- | --------- | ------ | --- | --- | ----------- | --------- |
| PPINC7 |     | Household | Income |     |     | 1: Less     | than $10k |
2: $10k-$24,999
$25k-$49,999
3:
4: $50k-$74,999
$75k-$99,999
5:
6: $100k-$149,999
7: $150k+
| PPMARIT5 |     | Marital Status |     |     |     | 1: Married |     |
| -------- | --- | -------------- | --- | --- | --- | ---------- | --- |
2: Widowed
3: Divorced
4: Separated
5: Never married
| PPEMPLOY |     | Current Employment |     | Status |     | 1: Full-time |     |
| -------- | --- | ------------------ | --- | ------ | --- | ------------ | --- |
2: Part-time
3: Not working
| PPHOUSE4 |     | Housing Type |     |     |     | 1: 1-family | detached |
| -------- | --- | ------------ | --- | --- | --- | ----------- | -------- |
2: Condo/townhouse
3: 2+ apartments
4: Other
| Appendix | D   | Unpacking | response |     | confidence |     | and |
| -------- | --- | --------- | -------- | --- | ---------- | --- | --- |
diversity
To further understand the behavioral differences between demographic persona and
SPIRIT persona conditioning, we conduct a set of diagnostic analyses focusing on
27

responseconfidence,answerdiversity,andtheirrelationshiptoinferenceaccuracy.All
analyses in this section are conducted on GPT-5-mini, which represents a stable and
| a well-performing |          | model in   | the main     | experiments. |     |
| ----------------- | -------- | ---------- | ------------ | ------------ | --- |
| D.1               | Response | confidence | distribution |              |     |
Figure D1A compares the distribution of response-level confidence categories across
conditions. Demographic persona conditioning is dominated by low-confidence
responses, whereas SPIRIT persona conditioning produces substantially higher pro-
| portions | of medium- | and high-confidence |     | responses. |     |
| -------- | ---------- | ------------------- | --- | ---------- | --- |
Thispatternisexpected.Underdemographicpersonaconditioning,inferencerelies
on sparse, population-level signals that are often insufficient to support confident
predictionsattheindividuallevel.Bycontrast,SPIRITpersonaconditioningincorpo-
rates non-demographic attributes inferred from user-generated text, providing richer
| contextual | grounding | and enabling | more | confident | responses. |
| ---------- | --------- | ------------ | ---- | --------- | ---------- |
28

Fig. D1 DiagnosticanalysesofresponseconfidenceanddiversityforGPT-5-mini.A,Distribution
ofresponse-levelconfidencecategoriesunderdemographicpersonaandSPIRITpersonaconditioning.
B,Distributionofresponseentropyperquestion,wherelowerentropyindicatesmorefixedorbiased
responsetendencies.C,Relationshipbetweenuser-levelaccuracyandthenumberoflow-confidence
responsesperuser,shownseparatelyforeachconditionwithlineartrendlines.
D.2 Response diversity and answer tendency
We next examine response diversity using entropy computed at the question level
(Figure D1B). To quantify response diversity, we compute Shannon entropy at the
question level. For each question, we collect the inferred categorical responses across
29

usersandestimatetheempiricalresponsedistribution.Letp(v)denotetheproportion
ofusersassignedresponsevaluev foragivenquestion.Responseentropyisdefinedas
(cid:88)
H =− p(v)log p(v),
2
v
where higher entropy indicates greater variability in inferred responses, and lower
entropyreflectsmoreconcentratedordeterministicresponsepatterns.Entropyiscom-
puted only for questions with more than one valid inferred response. Lower entropy
indicates more fixed or biased response tendencies, whereas higher entropy reflects
greater variability across users.
Demographic persona conditioning exhibits substantially lower response entropy,
indicatingastrongtendencytowardfixedordefaultanswers.Inpractice,thismanifests
as systematic preference for negative responses (e.g., answering “No” to behavioral or
health-related questions), which compresses the range of possible inferred values. In
contrast,SPIRITpersonaconditioningyieldshigherentropydistributions,suggesting
thatpersona-basedinferencebetterpreservesheterogeneityacrossusersandquestions.
D.3 Low-confidence responses and user-level accuracy
Finally,weanalyzetherelationshipbetweeninferenceaccuracyandthenumberoflow-
confidenceresponsesperuser(FigureD1C).Underdemographicpersonaconditioning,
users with larger numbers of low-confidence responses exhibit a clearer degradation
in accuracy. This trend reflects the cumulative effect of uncertain, weakly grounded
inferences.
Bycomparison,SPIRITpersonaconditioningsubstantiallyreducestheprevalence
of low-confidence responses and weakens the negative association between low con-
fidence and accuracy. This suggests that persona-based inference not only improves
overallperformancebutalsostabilizesreasoningattheuserlevelbyreducingreliance
on uncertain guesses.
These analyses clarify why demographic persona conditioning can appear compet-
itivelyaccurateonsomeattributeswhilestillproducingdegenerateresponsepatterns.
Demographic persona inference tends to rely on population-level shortcuts, leading
to low-confidence, low-diversity predictions. SPIRIT persona conditioning mitigates
these issues by grounding inference in non-demographic attributes, resulting in more
confident, diverse, and behaviorally plausible responses.
Appendix E Subtentive questions
E.1 Epstein files questions
The following questions (Table E4) are used to measure public attitudes toward the
release of the Jeffrey Epstein investigation files and potential involvement of pub-
lic figures. Question wording closely follows contemporary public opinion surveys
conducted in late 2025 to early 2026.
30

|     | Table E4    | Epsteinfilessurveyquestionsandresponseoptions |                                     |           |                 |              |              |                |
| --- | ----------- | --------------------------------------------- | ----------------------------------- | --------- | --------------- | ------------ | ------------ | -------------- |
|     | Question    | ID                                            | Question                            |           | wording         | and response | options      |                |
|     | EPSTEIN     |                                               | FILES Should                        | the       | U.S. government | release      | all of its   | files from the |
|     | RELEASE     |                                               | investigationofJeffreyEpstein?      |           |                 |              |              |                |
|     |             |                                               | (1)Yes                              |           | (2)No           | (98)Notsure  |              |                |
|     | TRUMP       | EPSTEIN                                       | Do                                  | you think | that            | Donald Trump | was involved | in crimes      |
|     | INVOLVEMENT |                                               | allegedlycommittedbyJeffreyEpstein? |           |                 |              |              |                |
|     |             |                                               | (1)Yes                              |           | (2)No           | (98)Notsure  |              |                |
| E.2 | Abortion    |                                               | attitude                            | question  |                 |              |              |                |
Attitudes toward abortion are measured using a standard four-category item com-
| monly | employed | in                             | U.S. public                 | opinion | surveys | (Table       | E5).    |     |
| ----- | -------- | ------------------------------ | --------------------------- | ------- | ------- | ------------ | ------- | --- |
|       | Table E5 | Abortionattitudesurveyquestion |                             |         |         |              |         |     |
|       | Question | ID                             | Question                    |         | wording | and response | options |     |
|       | ABRTLGL  |                                | Doyouthinkabortionshouldbe: |         |         |              |         |     |
(1)Legalinallcases
(2)Legalinmostcases
(3)Illegalinmostcases
(4)Illegalinallcases
| E.3 | Immigration |     | policy | battery |     |     |     |     |
| --- | ----------- | --- | ------ | ------- | --- | --- | --- | --- |
Attitudes toward immigration are measured using a policy battery. For each item,
respondentsareaskedhowmuchtheyfavororopposetheproposedpolicy(TableE6).
Response categories for all immigration items are: (1) Strongly favor, (2) Somewhat
favor, (3) Somewhat oppose, (4) Strongly oppose, (98) Don’t know, (99) Refused.
| E.4 | Venezuela |     | military | action | questions |     |     |     |
| --- | --------- | --- | -------- | ------ | --------- | --- | --- | --- |
The following questions (Table E7) probe public attitudes toward U.S. policy
and potential military action involving Venezuela. These items are adapted from
| contemporaneous |     |     | polling instruments. |               |        |            |       |          |
| --------------- | --- | --- | -------------------- | ------------- | ------ | ---------- | ----- | -------- |
| Appendix        |     | F   | Effects              | of            | Social | Media      | Trace | Quality  |
|                 |     |     | on                   | Persona-Based |        | Simulation |       | Accuracy |
Thisappendixreportsadditionalanalysesexamininghowthequalityandinformative-
nessofsocialmediatracesrelatetotheaccuracyofSPIRIT-basedpersonasimulations,
aswellasafullcategory-levelbreakdownofperformanceacrossall81surveyquestions
using GPT-5-Mini.
31

| Table | E6 Immigrationpolicybatteryitemsandresponsecategories |                                           |                   |                |       |
| ----- | ----------------------------------------------------- | ----------------------------------------- | ----------------- | -------------- | ----- |
| Item  | ID                                                    | Policy description                        |                   |                |       |
| BRDER |                                                       | Improvingsecurityalongthecountry’sborders |                   |                |       |
| REF   |                                                       | Admitting more                            | civilian refugees | from countries | where |
peoplearetryingtoescapeviolenceandwar
| SKILL |     | Legallyadmittingmorehigh-skilledimmigrants |            |               |           |
| ----- | --- | ------------------------------------------ | ---------- | ------------- | --------- |
| DIV   |     | Legally admitting                          | immigrants | from all over | the world |
toensurethenation’simmigrantpopulationisdiverse
| LABOR |     | Legallyadmittingimmigrantswhocanfilllaborshort- |     |     |     |
| ----- | --- | ----------------------------------------------- | --- | --- | --- |
ages
| DEPORT |     | Enforcingmassdeportationsofimmigrantslivinginthe |     |     |     |
| ------ | --- | ------------------------------------------------ | --- | --- | --- |
countryillegally
| STUD |     | Allowing international | students | who receive | a college |
| ---- | --- | ---------------------- | -------- | ----------- | --------- |
degreeintheU.S.tolegallyworkandstayinthecoun-
try
| MARRY |     | Allowingundocumentedimmigrantstolegallyworkand |     |     |     |
| ----- | --- | ---------------------------------------------- | --- | --- | --- |
stayinthecountryiftheyaremarriedtoaU.S.citizen
| F.1 Trace   | Quantity | and Persona | Confidence | as Proxies | for |
| ----------- | -------- | ----------- | ---------- | ---------- | --- |
| Information |          | Quality     |            |            |     |
FigureF2presentstwocomplementaryanalyseslinkingcharacteristicsofusers’social
| media traces | to downstream | prediction accuracy. |     |     |     |
| ------------ | ------------- | -------------------- | --- | --- | --- |
Panel A relates prediction accuracy to the total amount of textual information
availableforeachindividual,measuredasthelog-transformedtotalnumberofcharac-
ters across all observed posts. A positive association is observed for both Twitter and
Reddit users: individuals who contribute longer or more extensive social media traces
tendtoyieldmoreaccuratepersona-basedpredictions.Thispatternisconsistentwith
the intuition that richer behavioral signals allow the persona inference module to
estimate latent attributes more precisely, thereby improving simulation fidelity.
PanelBexaminespredictionaccuracyasafunctionofthenumberoflow-confidence
persona attributes inferred for a given individual. Each persona dimension produced
by SPIRIT is accompanied by a confidence score; attributes falling below a prede-
finedthresholdareflaggedaslow-confidence.Aclearnegativerelationshipemerges:as
the number of low-confidence attributes increases, simulation accuracy declines. This
pattern holds across platforms and mirrors the result in Panel A from the opposite
direction—when less information can be reliably inferred from the trace, downstream
| predictions | degrade. |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
Together, these results show that both trace quantity and persona-level inferen-
tial confidence serve as meaningful proxies for information quality, and that SPIRIT
responds to variation in observational signal in theoretically expected ways.
32

Table E7 Venezuela-relatedsurveyquestions
| Question ID | Question      | wording and    | response | options |           |          |
| ----------- | ------------- | -------------- | -------- | ------- | --------- | -------- |
| VZ Q12      | Has the Trump | administration |          | clearly | explained | what the |
U.S.intendstodoregardingVenezuela?
|        | (1)Yes   | (2)No (3)Notsure     |     |         |         |          |
| ------ | -------- | -------------------- | --- | ------- | ------- | -------- |
| VZ Q13 | Does the | Trump administration |     | need to | explain | what the |
U.S.intendstodoregardingVenezuela?
|        | (1)Yes                                           | (2)No (3)Notsure |     |     |     |     |
| ------ | ------------------------------------------------ | ---------------- | --- | --- | --- | --- |
| VZ Q14 | HowmuchofathreatdoyouthinkVenezuelaistotheUnited |                  |     |     |     |     |
States?
|     | (1)Majorthreat | (2)Minorthreat |     | (3)Notathreat |     | (4) |
| --- | -------------- | -------------- | --- | ------------- | --- | --- |
Notsure
| VZ Q15 | WouldyouapproveordisapproveofpotentialU.S.military |     |     |     |     |     |
| ------ | -------------------------------------------------- | --- | --- | --- | --- | --- |
actioninVenezuela?
|        | (1)Approve                                          | (2)Disapprove |     | (3)Notsure |     |     |
| ------ | --------------------------------------------------- | ------------- | --- | ---------- | --- | --- |
| VZ Q16 | ShouldPresidentTrumpneedcongressionalapprovalbefore |               |     |            |     |     |
takingmilitaryactioninVenezuela?
|        | (1)Yes                                              | (2)No (3)Notsure |     |     |     |     |
| ------ | --------------------------------------------------- | ---------------- | --- | --- | --- | --- |
| VZ Q17 | Doyouapproveordisapproveofthecurrentmilitaryattacks |                  |     |     |     |     |
onboatssuspectedofbringingdrugsfromVenezuela?
|        | (1)Approve | (2)Disapprove  |      | (3)Notsure |      |           |
| ------ | ---------- | -------------- | ---- | ---------- | ---- | --------- |
| VZ Q18 | Should the | administration | show | evidence   | that | there are |
drugsontheboatsbeingattacked?
|        | (1)Yes       | (2)No (3)Notsure |                 |     |           |       |
| ------ | ------------ | ---------------- | --------------- | --- | --------- | ----- |
| VZ Q19 | Do you think | U.S.             | military action | in  | Venezuela | would |
decreasetheamountofdrugscomingintotheU.S.?
|     | (1)Yes | (2)Nochange | (3)Increase |     | (4)Notsure |     |
| --- | ------ | ----------- | ----------- | --- | ---------- | --- |
Fig. F2 Relationship between social media trace quality and prediction accuracy. (A)
Accuracy as a function of the log-transformed total number of characters across all observed posts
for each individual. (B) Accuracy as a function of the number of low-confidence persona attributes
inferredbySPIRIT.Pointsrepresentindividualusers,coloredbyplatform(Twittervs.Reddit).Solid
linesindicatelineartrends.
33

Table F8 Prediction accuracy by survey question category.Reportedvaluesaremean
exact-matchaccuracy,standarddeviation,numberofquestions,totalresponses,andoff-by-one
rateforGPT-5-Miniacrossall81surveyitems.Categoriesareorderedfromworsttobest
averageaccuracy.
Category Avg. Acc. Std. Dev. # Questions Responses Off-by-one
| Finances        |     | 0.245  | 0.430  |     | 3        |     | 5,185      | 0.407 |
| --------------- | --- | ------ | ------ | --- | -------- | --- | ---------- | ----- |
| Technology      |     | 0.257  | 0.437  |     | 2        |     | 3,570      | 0.394 |
| Religion        |     | 0.483  | 0.500  |     | 2        |     | 3,580      | 0.152 |
| Politics/Media  |     | 0.504  | 0.500  |     | 11       |     | 19,388     | 0.388 |
| Alcohol         |     | 0.569  | 0.495  |     | 8        |     | 11,432     | –     |
| Vaccines        |     | 0.594  | 0.491  |     | 7        |     | 12,220     | 0.309 |
| Demographics    |     | 0.677  | 0.468  |     | 12       |     | 21,669     | 0.091 |
| Guns            |     | 0.726  | 0.446  |     | 2        |     | 3,584      | 0.274 |
| Employment      |     | 0.738  | 0.440  |     | 9        |     | 14,752     | 0.129 |
| Health          |     | 0.764  | 0.425  |     | 16       |     | 26,610     | 0.341 |
| Voting          |     | 0.832  | 0.374  |     | 5        |     | 8,169      | 0.103 |
| Military        |     | 0.929  | 0.257  |     | 4        |     | 6,547      | 0.027 |
| F.2 Performance |     | Across | Survey |     | Question |     | Categories |       |
To complement the individual-level quality analysis, we report performance disaggre-
gatedbyquestioncategoryacrossthefullsetof81surveyitems.TableF8summarizes
meanexact-matchaccuracy,standarddeviation,andoff-by-oneratesforeachcategory.
Substantial heterogeneity is observed across domains. Categories involving
abstract, private, or infrequently expressed attributes (e.g., finances and technology)
exhibit the lowest accuracy and highest variance. In contrast, domains associated
with stable self-concepts and repeated public expression—such as health, employ-
ment, voting, and military attitudes—show substantially higher accuracy and lower
dispersion.
These category-level patterns align with the trace-quality analysis above, reinforc-
ing the conclusion that persona-based simulation performs best when attitudes are
| internally consistent | and | well-supported |     | by observable |     | discourse. |     |     |
| --------------------- | --- | -------------- | --- | ------------- | --- | ---------- | --- | --- |
F.3 Summary
Across both individual- and category-level analyses, prediction accuracy scales sys-
tematically with the informativeness of social media traces. Persona confidence scores
provideausefulinternaldiagnosticofsimulationreliability,whilecategory-levelperfor-
mance reflects theoretically grounded differences in attitude expression and stability.
Together, these results support the use of SPIRIT as a principled framework for
| bridging organic | digital | traces     | and survey-based |        | measurement. |     |           |     |
| ---------------- | ------- | ---------- | ---------------- | ------ | ------------ | --- | --------- | --- |
| F.4 Item-level   |         | deviations |                  | in the | Venezuela    |     | questions |     |
Table F9 and Table F10 compare the weighted distribution of responses from the
persona-conditioned virtual panel with contemporaneous CBS poll marginals for two
Venezuela-related items. These two items illustrate a recurring pattern: compared
to human respondents, LLM-based agents were less likely to select an unqualified,
34

low-engagement option (e.g., “not a threat” or “no change”) and instead allocated
more probability mass to analytically elaborated categories (e.g., “minor threat” or
“would increase drugs”). We interpret this as a deliberation bias: when prompted
to explain, simulated agents tend to treat questions as requiring causal analysis and
internally consistent justification, whereas survey respondents often rely on heuristics
or satisficing strategies.
|     | Table F9 VenezuelaQ14:perceivedthreattotheUnited |     |     |     |     |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
States.WeightedAI-agentresponsesversusCBSpoll
marginals.
|     | Responseoption | Agents(%) |      | CBS(%) | Diff(pp) |       |
| --- | -------------- | --------- | ---- | ------ | -------- | ----- |
|     | Majorthreat    |           | 20.1 |        | 13       | +7.1  |
|     | Minorthreat    |           | 79.9 |        | 48       | +31.9 |
|     | Notathreat     |           | 0.0  |        | 39       | -39.0 |
For Q14 (Table F9), agents almost never selected “not a threat” (0%), a response
thataccountsfor39%intheCBSpoll.Instead,agentsconcentratedon“minorthreat”.
Inspecting the generated rationales suggests that agents tended to (i) acknowledge
multipleindirectchannels(e.g.,regionalinstability,migrationspillovers,transnational
crime) while (ii) rejecting the stronger framing of an existential or imminent threat.
This combination naturally pushes responses toward “minor threat” rather than “not
a threat”, even when the overall stance is closer to skepticism than alarmism.
| Table F10 | VenezuelaQ19:whetherU.S.militaryactionwoulddecreasedrugs |     |     |     |     |     |
| --------- | -------------------------------------------------------- | --- | --- | --- | --- | --- |
enteringtheU.S.WeightedAI-agentresponsesversusCBSpollmarginals.
| Responseoption                 |     |     |     | Agents(%) | CBS(%) | Diff(pp) |
| ------------------------------ | --- | --- | --- | --------- | ------ | -------- |
| Yes,woulddecreasedrugs         |     |     |     | 39.6      |        | 37 +2.6  |
| No,wouldnotchangeamountofdrugs |     |     |     | 11.8      |        | 56 -44.2 |
| Wouldincreasedrugs             |     |     |     | 48.6      |        | 7 +41.6  |
For Q19 (Table F10), the binary framing (“decrease” vs. “not decrease”) yielded
aclosermatchtothepoll,butthethree-categoryversionshowsasubstantialredistri-
bution: agents rarely selected “no change” and instead shifted heavily toward “would
increase drugs.” The corresponding rationales frequently invoked systems-style argu-
ments(e.g.,displacement/“balloon”effects,carteladaptation,governancebreakdown,
and instability-induced expansion of illicit markets). This reasoning is coherent, but
it likely overstates the degree of analytic engagement typical in survey response pro-
cesses, where respondents may interpret “no change” as a satisficing default or an
expressionofgeneralskepticismaboutpolicyefficacywithoutcommittingtoabackfire
mechanism.
35

Interpretation.
Taken together, these deviations are consistent with a deliberation bias in LLM-
basedpanels:simulatedrespondentspreferentiallyconstructmechanisticexplanations
and therefore avoid options that imply categorical dismissal (e.g., “not a threat”) or
minimal updating (e.g., “no change”) (the full reaosning summary can be seen in
Appendix F.5). In practice, this implies that matching human marginals may require
either (i) explicitly modeling satisficing/low-effort response styles in the Reasoner
prompt,or(ii)treatingcertainresponsecategoriesascapturingheterogeneoushuman
heuristics that are not well represented by analytic, justification-seeking generation.
F.5 Consolidated reasoning patterns by item and response
option (Venezuela module)
To aid interpretability, we summarize the dominant reasoning patterns produced by
the simulated panel for each Venezuela item and each response option. For each ques-
tion, we group free-text rationales by the chosen answer category and then synthesize
the recurring themes into a short paragraph. The goal is not to reproduce verbatim
outputs,buttodocumentthequalitativelogicthatmostfrequentlyaccompaniedeach
response.
Venezuela Q12: Has the administration clearly explained the reasons for
the Venezuela actions?
Yes, has explained clearly.Rationalesselecting“Yes”generallyframedtheadmin-
istration’s messaging as clear and direct, emphasizing an unambiguous stance against
socialism and a straightforward objective of opposing the Maduro regime. These
responseshighlightedaconsistentrhetoricalposture(e.g.,firmness,anti-socialistfram-
ing,willingnesstoact)andinterpretedanyperceivedambiguityasarisingfrommedia
interpretation rather than from the administration’s communication.
No,hasnotexplainedclearly.Rationalesselecting“No”convergedontheview
that the administration relied on broad slogans and posturing without articulating a
coherent strategy. Respondents described the approach as vague, reactive, and lack-
ing concrete details about objectives, mechanisms, or end goals. In this framing, the
absence of an explicit plan and the perceived volatility of messaging were treated as
evidence that the reasons were not clearly explained.
Venezuela Q13: Should the administration explain the reasons to the
American people?
Yes, needs to explain.Responsesselecting“Yes”treatedpotentialmilitaryinvolve-
ment as a uniquely consequential decision that requires public justification and
democratic accountability. Rationales emphasized constitutional principles, oversight,
and the need for clarity about goals, risks, and an exit strategy. Many invoked histor-
ical caution regarding past U.S. interventions and rejected vague ideological framing
as insufficient for legitimizing force.
No, does not need to explain. Responses selecting “No” primarily appealed
to national-security discretion and executive authority. Rationales emphasized that
36

revealing strategy could undermine effectiveness by telegraphing intentions, and por-
trayed Congress and the media as slow, politicized, or prone to leaks. This cluster
valued decisiveness and secrecy over deliberation, framing transparency demands as
counterproductive in security contexts.
Venezuela Q14: Is Venezuela a threat to the United States?
Major threat.Rationalesselecting“majorthreat”framedVenezuelaasaproximate
national-security risk, frequently citing drug trafficking as the concrete mechanism
through which Venezuela could harm U.S. interests. Responses emphasized regional
spillovers (migration, criminal networks), geographic proximity, and the possibility of
hostileforeigninfluence.Whilesocialismwasoftenmentioned,ittypicallyservedasan
explanatoryfactorforstatecollapseratherthanasthesolebasisofthreatperception.
Minorthreat.Rationalesselecting“minorthreat”rejectedanexistentialframing
while still acknowledging serious problems. Venezuela was described as primarily a
humanitarian crisis and a source of indirect regional instability rather than a direct
military adversary. Drug trafficking and spillovers were recognized but positioned as
contingent and incremental risks. Many explicitly contrasted Venezuela with higher-
order geopolitical threats (e.g., major powers), treating the “major threat” framing
as inflated or politically instrumental.
Not a threat. In our simulation, this option was rarely selected; consequently,
no stable reasoning cluster emerged for “not a threat” beyond generic dismissal of
relevance to U.S. security.
Venezuela Q15: Do you approve or disapprove of U.S. military action in
Venezuela?
Approve. Approval rationales were typically conditional and reluctant: respondents
expressed general discomfort with war but accepted intervention if it were limited
in scope, short in duration, and tied to concrete objectives such as disrupting drug
traffickingorremovingspecificregimeactors.“Quickanddecisive”intervention,rather
than prolonged engagement or nation-building, was the dominant constraint.
Disapprove. Disapproval rationales emphasized the historical track record of
U.S. interventions, mission creep, civilian harm, and unintended consequences. Many
arguedthatmilitaryforceisapoorinstrumentforcomplexpoliticalandhumanitarian
crises and preferred non-military alternatives. Even when acknowledging the severity
of Venezuela’s situation, respondents viewed intervention as high-risk and low-reward
absent a direct, imminent threat.
Venezuela Q16: Should the administration obtain congressional approval
before military action?
Yes, needs congressional approval. Rationales selecting “Yes” strongly empha-
sized constitutional checks and balances and treated congressional authorization as a
basic requirement for initiating war. War-making was framed as qualitatively differ-
ent from routine executive action and therefore requiring collective deliberation and
democratic legitimacy, regardless of partisan preferences.
37

No, does not need congressional approval. Rationales selecting “No” priori-
tized speed and executive discretion, portraying Congress as too slow, gridlocked, or
pronetopoliticizationforcrisisresponse.Thisclusterframedunilateralactionasnec-
essaryforeffectiveleadership,withtransparencyanddeliberationtreatedassecondary
| to operational | effectiveness        | in national-security |               | contexts. |           |       |
| -------------- | -------------------- | -------------------- | ------------- | --------- | --------- | ----- |
| Venezuela      | Q17: Do              | you approve          | or disapprove | of        | attacking | boats |
| suspected      | of drug trafficking? |                      |               |           |           |       |
Approve.Approvalrationalesmorallyforegroundedtheharmsofdrugs(oftenframed
asexistentialtocommunities)andtreatedtraffickersaslegitimatetargets.Manyused
ends-justify-the-means reasoning, arguing that decisive interdiction deters smuggling
and protects U.S. borders, sometimes downplaying uncertainty in identification.
Disapprove. Disapproval rationales stressed due process, evidentiary standards,
andtheriskofmisidentifyingcivilians.Theseresponsesframedboatattacksasextra-
judicialviolencewithhighpotentialforescalationandnormviolation.Suspicionalone
| was treated | as an unacceptably | low threshold      |                | for lethal | force.   |      |
| ----------- | ------------------ | ------------------ | -------------- | ---------- | -------- | ---- |
| Venezuela   | Q18: Should        | the administration |                | provide    | evidence | that |
| Venezuela   | poses a threat     | before             | taking action? |            |          |      |
Yes, should show evidence. This cluster emphasized legitimacy through trans-
parency, arguing that extraordinary force requires demonstrable evidence and public
accountability. Concerns about wrongful harm, false positives, and precedent-setting
abuses were central. Evidence was treated as a prerequisite to action rather than a
| post hoc | justification. |     |     |     |     |     |
| -------- | -------------- | --- | --- | --- | --- | --- |
No, does not need to show evidence. This cluster justified acting on suspi-
cionbyappealingtooperationalsecrecyandtrustinmilitaryorintelligenceexpertise.
Releasingevidencewasportrayedastacticallydangerous(exposingsourcesandmeth-
ods) and procedurally impractical in time-sensitive interdiction. The risk of false
| positives | was implicitly | accepted as less | costly | than letting | drugs | through. |
| --------- | -------------- | ---------------- | ------ | ------------ | ----- | -------- |
Venezuela Q19: Will military action decrease drugs reaching the United
States?
Yes, would decrease drugs. Rationales selecting “Yes” invoked supply-chain dis-
ruption and deterrence: reducing supply increases cost and risk for traffickers and
can slow or reduce flow, even if temporarily. These responses treated interdiction as
an imperfect but pragmatically beneficial mechanism, emphasizing chokepoints and
| upstream | disruption. |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- |
No,wouldnotchangetheamountofdrugs.Rationalesselecting“nochange”
emphasized demand-side constraints and adaptive trafficking networks. This cluster
described interdiction as whack-a-mole displacement that shifts routes and meth-
ods without meaningfully reducing total flow as long as U.S. demand remains high.
Militaryforcewasframedasmisalignedwiththestructuraldriversofthedrugmarket.
Would increase drugs. Rationales selecting “would increase” extended the
adaptive-systems critique into a backfire mechanism. Responses argued that military
disruption generates instability, violence, and governance vacuums that strengthen
38

trafficking organizations, diversify routes, and increase incentives through higher
prices. The dominant causal chain was: disruption → chaos/instability → cartel
adaptation/expansion → equal or higher trafficking volume, often accompanied by
historical analogies to past enforcement shocks.
F.6 Unweighted persona-bank estimates
Fig.F3 Comparisonofweightedandunweightedpersona-bankresponseswithpollingbenchmarks.
Solid lines denote weighted estimates, while dotted lines denote unweighted aggregates. Results
are shown for both Twitter- and Reddit-based persona banks across long-term attitudinal ques-
tions (Panel A) and event-sensitive questions (Panel B). Unweighted estimates reproduce the same
within-clusterdirectionalpatternsasweightedestimates,butexhibitsubstantiallylargerdeviations
in absolute levels, particularly for Reddit. This pattern indicates that weighting primarily improves
calibration by mitigating selection-induced level bias, while preserving the underlying attitudinal
structureexpressedbythesimulatedrespondents.
Figure F3 reports persona-bank estimates aggregated without weights alongside
the weighted results shown in the main text. This comparison clarifies the role of
weighting in the analysis.
Across both panels, unweighted persona-bank responses continue to reproduce
coherentquestion-to-questionstructurewithineachissue-specificcluster.Itemsreceiv-
ing higher support in polling benchmarks are generally ranked higher by simulated
respondents,andlower-supportitemsremaincomparativelylower.Thisindicatesthat
trendalignmentisnotanartifactofcalibration,butinsteadreflectsstableattitudinal
gradients captured by the inferred personas.
39

At the same time, unweighted estimates exhibit substantially larger deviations
in absolute levels, particularly for the Reddit-based persona bank. These devia-
tions are consistent with known compositional imbalances in the underlying social
media samples, including overrepresentation of highly educated and politically liberal
users. Weighting, therefore, plays a critical role in improving calibration by reducing
selection-induced level bias, rather than altering the qualitative patterns of opinion
expressed by the simulated respondents.
Appendix G Persona schema
G.1 JSON Schema for Painter
The Painter module is instructed to follow the exact top-level structure below (no
additional top-level fields). Field values are constrained to the enumerated options
shown.
{
"personality_big5": {
"openness": { "approx_level": "...", "confidence": "...", "rationale": "..." },
"conscientiousness": { "approx_level": "...", "confidence": "...", "rationale": "..." },
"extraversion": { "approx_level": "...", "confidence": "...", "rationale": "..." },
"agreeableness": { "approx_level": "...", "confidence": "...", "rationale": "..." },
"neuroticism": { "approx_level": "...", "confidence": "...", "rationale": "..." }
},
"primal_world_beliefs": {
"good_vs_bad": {
"value": "leans_good | balanced | leans_bad | unclear",
"confidence": "high | medium | low",
"rationale": "..."
},
"safe_vs_dangerous": {
"value": "leans_safe | balanced | leans_dangerous | unclear",
"confidence": "high | medium | low",
"rationale": "..."
},
"enticing_vs_dull": {
"value": "leans_enticing | balanced | leans_dull | unclear",
"confidence": "high | medium | low",
"rationale": "..."
},
"alive_vs_mechanistic": {
"value": "leans_alive | balanced | leans_mechanistic | unclear",
"confidence": "high | medium | low",
"rationale": "..."
},
"pleasurable_vs_miserable": {
40

| "value": "leans_pleasurable |       |          | |   | balanced | leans_miserable |     | | unclear", |
| --------------------------- | ----- | -------- | --- | -------------------------- | --- | ----------- |
| "confidence":               | "high | | medium | |   | low",                      |     |             |
| "rationale":                | "..." |          |     |                            |     |             |
},
| "regenerative_vs_degenerative": |     |     |     | {   |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- |
"value": "leans_regenerative | balanced | leans_degenerative | unclear",
| "confidence": | "high | | medium | |   | low", |     |     |
| ------------- | ----- | -------- | --- | ----- | --- | --- |
| "rationale":  | "..." |          |     |       |     |     |
},
| "progressing_vs_declining": |       |          | {   |                            |     |             |
| --------------------------- | ----- | -------- | --- | -------------------------- | --- | ----------- |
| "value": "leans_progressing |       |          | |   | balanced | leans_declining |     | | unclear", |
| "confidence":               | "high | | medium | |   | low",                      |     |             |
| "rationale":                | "..." |          |     |                            |     |             |
},
| "harmless_vs_threatening": |       |          | {          |                     |     |             |
| -------------------------- | ----- | -------- | ---------- | ------------------- | --- | ----------- |
| "value": "leans_harmless   |       |          | | balanced | | leans_threatening |     | | unclear", |
| "confidence":              | "high | | medium | |          | low",               |     |             |
| "rationale":               | "..." |          |            |                     |     |             |
},
| "cooperative_vs_competitive": |     |     | {   |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- |
"value": "leans_cooperative | balanced | leans_competitive | unclear",
| "confidence": | "high | | medium | |   | low", |     |     |
| ------------- | ----- | -------- | --- | ----- | --- | --- |
| "rationale":  | "..." |          |     |       |     |     |
},
| "stable_vs_fragile":   |       | {        |          |                 |     |             |
| ---------------------- | ----- | -------- | -------- | --------------- | --- | ----------- |
| "value": "leans_stable |       | |        | balanced | | leans_fragile |     | | unclear", |
| "confidence":          | "high | | medium | |        | low",           |     |             |
| "rationale":           | "..." |          |          |                 |     |             |
},
| "just_vs_unjust":    | {     |            |     |                |             |     |
| -------------------- | ----- | ---------- | --- | -------------- | ----------- | --- |
| "value": "leans_just |       | | balanced |     | | leans_unjust | | unclear", |     |
| "confidence":        | "high | | medium   | |   | low",          |             |     |
| "rationale":         | "..." |            |     |                |             |     |
},
| "interesting_vs_boring":    |       | {        |     |                         |     |             |
| --------------------------- | ----- | -------- | --- | ----------------------- | --- | ----------- |
| "value": "leans_interesting |       |          | |   | balanced | leans_boring |     | | unclear", |
| "confidence":               | "high | | medium | |   | low",                   |     |             |
| "rationale":                | "..." |          |     |                         |     |             |
},
| "beautiful_vs_ugly":      |       | {        |            |              |     |             |
| ------------------------- | ----- | -------- | ---------- | ------------ | --- | ----------- |
| "value": "leans_beautiful |       |          | | balanced | | leans_ugly |     | | unclear", |
| "confidence":             | "high | | medium | |          | low",        |     |             |
| "rationale":              | "..." |          |            |              |     |             |
},
| "abundant_vs_barren":    |       | {        |            |                |     |             |
| ------------------------ | ----- | -------- | ---------- | -------------- | --- | ----------- |
| "value": "leans_abundant |       |          | | balanced | | leans_barren |     | | unclear", |
| "confidence":            | "high | | medium | |          | low",          |     |             |
| "rationale":             | "..." |          |            |                |     |             |
},
41

| "worth_exploring_vs_not_worth_exploring": |     |     | {   |     |
| ----------------------------------------- | --- | --- | --- | --- |
"value": "leans_worth_exploring | balanced | leans_not_worth_exploring | unclear",
| "confidence": | "high | | medium | low", |     |     |
| ------------- | ------- | -------------- | --- | --- |
| "rationale":  | "..."   |                |     |     |
},
| "meaningful_vs_meaningless": |         | {              |                     |             |
| ---------------------------- | ------- | -------------- | ------------------- | ----------- |
| "value": "leans_meaningful   |         | | balanced     | | leans_meaningless | | unclear", |
| "confidence":                | "high | | medium | low", |                     |             |
| "rationale":                 | "..."   |                |                     |             |
},
| "improvable_vs_too_hard_to_improve": |     |     | {   |     |
| ------------------------------------ | --- | --- | --- | --- |
"value": "leans_improvable | balanced | leans_too_hard_to_improve | unclear",
| "confidence": | "high | | medium | low", |     |     |
| ------------- | ------- | -------------- | --- | --- |
| "rationale":  | "..."   |                |     |     |
},
| "funny_vs_not_funny": | {       |                |                   |             |
| --------------------- | ------- | -------------- | ----------------- | ----------- |
| "value": "leans_funny |         | | balanced     | | leans_not_funny | | unclear", |
| "confidence":         | "high | | medium | low", |                   |             |
| "rationale":          | "..."   |                |                   |             |
},
| "intentional_vs_unintentional": |     | {   |     |     |
| ------------------------------- | --- | --- | --- | --- |
"value": "leans_intentional | balanced | leans_unintentional | unclear",
| "confidence": | "high | | medium | low", |     |     |
| ------------- | ------- | -------------- | --- | --- |
| "rationale":  | "..."   |                |     |     |
},
| "needs_me_vs_doesnt_need_me": |     | {   |     |     |
| ----------------------------- | --- | --- | --- | --- |
"value": "leans_needs_me | balanced | leans_doesnt_need_me | unclear",
| "confidence": | "high | | medium | low", |     |     |
| ------------- | ------- | -------------- | --- | --- |
| "rationale":  | "..."   |                |     |     |
},
| "interactive_vs_indifferent": |     | {   |     |     |
| ----------------------------- | --- | --- | --- | --- |
"value": "leans_interactive | balanced | leans_indifferent | unclear",
| "confidence": | "high | | medium | low", |     |     |
| ------------- | ------- | -------------- | --- | --- |
| "rationale":  | "..."   |                |     |     |
},
| "interconnected_vs_separable": |     | {   |     |     |
| ------------------------------ | --- | --- | --- | --- |
"value": "leans_interconnected | balanced | leans_separable | unclear",
| "confidence": | "high | | medium | low", |     |     |
| ------------- | ------- | -------------- | --- | --- |
| "rationale":  | "..."   |                |     |     |
},
| "changing_vs_static":    | {       |                |                |             |
| ------------------------ | ------- | -------------- | -------------- | ----------- |
| "value": "leans_changing |         | | balanced     | | leans_static | | unclear", |
| "confidence":            | "high | | medium | low", |                |             |
| "rationale":             | "..."   |                |                |             |
},
| "hierarchical_vs_nonhierarchical": |     |     | {   |     |
| ---------------------------------- | --- | --- | --- | --- |
"value": "leans_hierarchical | balanced | leans_nonhierarchical | unclear",
| "confidence": | "high | | medium | low", |     |     |
| ------------- | ------- | -------------- | --- | --- |
42

| "rationale": | "..." |     |
| ------------ | ----- | --- |
},
"understandable_vs_too_hard_to_understand": {
"value": "leans_understandable | balanced | leans_too_hard_to_understand | unclear",
| "confidence": | "high | | medium | low", |
| ------------- | ----- | ---------------- |
| "rationale":  | "..." |                  |
},
| "acceptable_vs_unacceptable": |     | {   |
| ----------------------------- | --- | --- |
"value": "leans_acceptable | balanced | leans_unacceptable | unclear",
| "confidence": | "high | | medium | low", |
| ------------- | ----- | ---------------- |
| "rationale":  | "..." |                  |
}
},
| "values_and_identities": |     | {   |
| ------------------------ | --- | --- |
| "salient_identities":    |     | [   |
{
"identity": "short label (e.g., parent, gamer, activist, student, etc.)",
| "confidence": | "high | | medium | low", |
| ------------- | ----- | ---------------- |
| "rationale":  | "..." |                  |
}
],
| "core_values": | [   |     |
| -------------- | --- | --- |
{
"value_label": "e.g., equality, order, tradition, autonomy, care, loyalty, etc.",
| "confidence": | "high | | medium | low", |
| ------------- | ----- | ---------------- |
| "rationale":  | "..." |                  |
}
]
},
| "life_experiences":   | {   |     |
| --------------------- | --- | --- |
| "education_and_work": |     | [   |
{
| "summary":    | "...", |                  |
| ------------- | ------ | ---------------- |
| "confidence": | "high  | | medium | low", |
| "rationale":  | "..."  |                  |
}
],
| "family_and_relationships": |     | [   |
| --------------------------- | --- | --- |
{
| "summary":    | "...", |                  |
| ------------- | ------ | ---------------- |
| "confidence": | "high  | | medium | low", |
| "rationale":  | "..."  |                  |
}
],
| "turning_points_or_themes": |     | [   |
| --------------------------- | --- | --- |
{
| "summary":    | "Important | repeated experiences", |
| ------------- | ---------- | ---------------------- |
| "confidence": | "high      | | medium | low",       |
43

| "rationale": | "..." |     |     |     |
| ------------ | ----- | --- | --- | --- |
}
]
},
| "opinions_and_beliefs": | {   |     |     |     |
| ----------------------- | --- | --- | --- | --- |
| "politics_and_society": | [   |     |     |     |
{
"topic": "e.g., elections, immigration, public health, identity politics, etc.",
| "stance_summary": | "1{3           | sentences summarizing | their likely | opinion", |
| ----------------- | -------------- | --------------------- | ------------ | --------- |
| "confidence":     | "high | medium | | low",               |              |           |
| "rationale":      | "..."          |                       |              |           |
}
],
| "work_and_career": | [   |     |     |     |
| ------------------ | --- | --- | --- | --- |
{
| "topic":          | "work, jobs, academia, | gig economy, | etc.", |     |
| ----------------- | ---------------------- | ------------ | ------ | --- |
| "stance_summary": | "1{3                   | sentences",  |        |     |
| "confidence":     | "high | medium         | | low",      |        |     |
| "rationale":      | "..."                  |              |        |     |
}
],
| "technology_and_social_media": |     | [   |     |     |
| ------------------------------ | --- | --- | --- | --- |
{
"topic": "e.g., views on platforms, algorithms, AI, online communities",
| "stance_summary": | "1{3           | sentences", |     |     |
| ----------------- | -------------- | ----------- | --- | --- |
| "confidence":     | "high | medium | | low",     |     |     |
| "rationale":      | "..."          |             |     |     |
}
],
| "other_recurrent_themes": | [   |     |     |     |
| ------------------------- | --- | --- | --- | --- |
{
"topic": "any other recurring domain (e.g., mental health, sports fandom, gaming, religion)",
| "stance_summary": | "1{3           | sentences", |     |     |
| ----------------- | -------------- | ----------- | --- | --- |
| "confidence":     | "high | medium | | low",     |     |     |
| "rationale":      | "..."          |             |     |     |
}
]
},
| "interaction_style": | {   |     |     |     |
| -------------------- | --- | --- | --- | --- |
"tone": {
"value": "e.g., sarcastic, earnest, hostile, humorous, supportive, analytical, etc.",
| "confidence": | "high | medium | | low", |     |     |
| ------------- | -------------- | ------- | --- | --- |
| "rationale":  | "..."          |         |     |     |
},
| "conflict_style": | {   |     |     |     |
| ----------------- | --- | --- | --- | --- |
"value": "confrontational | avoidant | accommodating | mixed | unclear",
| "confidence": | "high | medium | | low", |     |     |
| ------------- | -------------- | ------- | --- | --- |
| "rationale":  | "..."          |         |     |     |
44

},
"information_orientation": {
"value": "news_junkie | casually_informed | low_information | niche_expert | unclear",
"confidence": "high | medium | low",
"rationale": "..."
}
},
"meta": {
"overall_uncertainty_comment": "2{4 sentences",
"notable_absences": "Brief list or sentence"
}
}
G.2 Painter prompt template
System prompt. The following template is used for the Painter module to infer a
tentative, probabilistic persona profile from a user’s historical posts.
You are an expert computational social scientist trained in survey methodology,
personality psychology, and political behavior.
Your task is to infer a *tentative*, *probabilistic* profile of a single social
media user from their posts.
CRITICAL RULES:
- Use ONLY the textual evidence in the posts (plus ordinary background knowledge
about language, not about any specific real person).
- Treat all inferences as uncertain hypotheses, not facts.
- When evidence is weak or absent, say "unknown" and explain briefly.
- DO NOT include any demographic fields in your output (age, gender, region, etc.).
Assume demographics are handled elsewhere in the pipeline.
- Do not attempt to identify or de-anonymize the user, and avoid directly quoting any specific posts;
paraphrase them instead.
You must produce TWO parts:
1) A JSON object describing:
- personality_big5
- primal_world_beliefs
- values_and_identities
- life_experiences
- opinions_and_beliefs
- interaction_style
- meta
2) After the JSON, print a line with exactly:
---
Then output a 2{3 paragraph third-person narrative persona.
45

JSON SCHEMA (follow this structure exactly; no extra top-level fields):
[see Appendix~\ref{app:persona_schema}]
| IMPORTANT | OUTPUT    | FORMAT: |          |        |                 |         |     |
| --------- | --------- | ------- | -------- | ------ | --------------- | ------- | --- |
| - First,  | output    | ONLY    | the JSON | object | (no surrounding | prose). |     |
| - Then a  | line with | exactly |          | three  | hyphens: ---    |         |     |
- Then the third-person narrative persona (2{3 paragraphs, ~150{300 words).
| G.3 External |     | survey |     | study | prompt templates |     |     |
| ------------ | --- | ------ | --- | ----- | ---------------- | --- | --- |
This appendix documents the prompt templates used in the external survey
study. Prompts are shown as templates; runtime fields (e.g., {persona json},
{persona narrative}, {demographics}, {question text}) are populated program-
matically.
| G.3.1 | Direct-attitude |     |     | prompting | (no search) |     |     |
| ----- | --------------- | --- | --- | --------- | ----------- | --- | --- |
You are participating in a survey. Answer the questions as the person described
below. Use only the information in the persona profile. If the persona provides
no evidence, choose the most plausible option but mark LOW confidence.
PERSONA (JSON):
{persona_json}
PERSONA (Narrative):
{persona_narrative}
| DEMOGRAPHICS | (provided |     | as context; |     | do not infer | new demographics): |     |
| ------------ | --------- | --- | ----------- | --- | ------------ | ------------------ | --- |
{demographics}
INSTRUCTIONS:
| - Treat this | as  | a survey | response, |     | not a factual | exam. |     |
| ------------ | --- | -------- | --------- | --- | ------------- | ----- | --- |
- Give your best answer based on your views/values/habits implied by the persona.
| - Do not | overthink; | avoid | long | analysis. |     |     |     |
| -------- | ---------- | ----- | ---- | --------- | --- | --- | --- |
- Output a JSON object with one entry per question in the required schema:
{ "value": <int_or_string>, "label": <string>, "confidence": "high|medium|low",
| "reason": | <1-3 | sentences> |     | }   |     |     |     |
| --------- | ---- | ---------- | --- | --- | --- | --- | --- |
QUESTION:
{question_text}
| RESPONSE | OPTIONS: |     |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- |
{options_list}
| G.3.2 | Time-sensitive |     |     | prompting | with information |     | acquisition |
| ----- | -------------- | --- | --- | --------- | ---------------- | --- | ----------- |
(three-step)
| Step 1: Pre-existing |     |     | knowledge |     | / prior impressions. |     |     |
| -------------------- | --- | --- | --------- | --- | -------------------- | --- | --- |
You are participating in a survey about a recent public issue. Answer as the
46

| person described | below. |     |     |     |     |     |
| ---------------- | ------ | --- | --- | --- | --- | --- |
PERSONA (JSON):
{persona_json}
PERSONA (Narrative):
{persona_narrative}
| DEMOGRAPHICS | (provided | as  | context; | do not infer | new | demographics): |
| ------------ | --------- | --- | -------- | ------------ | --- | -------------- |
{demographics}
TASK:
Before searching the web, state what you (as this person) already know or
| believe      | about the | topic. | If you | know little or | nothing, | say so. |
| ------------ | --------- | ------ | ------ | -------------- | -------- | ------- |
| OUTPUT (JSON | only):    |        |        |                |          |         |
{
| "knowledge_level":  |      | "none|minimal|moderate|extensive", |           |                 |          |           |
| ------------------- | ---- | ---------------------------------- | --------- | --------------- | -------- | --------- |
| "what_i_know":      | "1-4 | sentences",                        |           |                 |          |           |
| "where_i_heard_it": |      | "e.g.,                             | news,     | social media,   | friends, | unknown", |
| "prior_impression": |      | "1-3                               | sentences | (or ’unknown’)" |          |           |
}
TOPIC:
{topic_name}
| Step 2: | Persona-conditioned |     |     | query generation. |     |     |
| ------- | ------------------- | --- | --- | ----------------- | --- | --- |
Generate 3-5 web search queries that YOU (as this person) would actually type to
learn more about the topic. Queries should reflect your interests, priors, and
| trusted | sources implied |     | by the | persona. |     |     |
| ------- | --------------- | --- | ------ | -------- | --- | --- |
PERSONA (JSON):
{persona_json}
PERSONA (Narrative):
{persona_narrative}
| OUTPUT (JSON | only):  |        |        |     |     |     |
| ------------ | ------- | ------ | ------ | --- | --- | --- |
| { "queries": | ["...", | "...", | "..."] | }   |     |     |
TOPIC:
{topic_name}
| Step 2b: | Summarize | retrieved |     | information. |     |     |
| -------- | --------- | --------- | --- | ------------ | --- | --- |
Below are search results (titles/snippets). Summarize what you learned, focusing
| on the most | relevant | points | for | forming an opinion. |     | Keep it concise. |
| ----------- | -------- | ------ | --- | ------------------- | --- | ---------------- |
PERSONA (JSON):
{persona_json}
47

PERSONA (Narrative):
{persona_narrative}
SEARCH RESULTS:
{search_results}
| OUTPUT (JSON | only): |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- |
{
| "key_points": | ["...", | "...", "..."], |                |          |              |
| ------------- | ------- | -------------- | -------------- | -------- | ------------ |
| "timeframe":  | "what   | time period    | the info seems | to cover | (if clear)", |
"source_fit": "1-2 sentences on why these sources feel credible or not to you",
| "updated_impression": |     | "1-3 sentences | (or ’unchanged’)" |     |     |
| --------------------- | --- | -------------- | ----------------- | --- | --- |
}
| Step 3: Post-search |     | survey response. |     |     |     |
| ------------------- | --- | ---------------- | --- | --- | --- |
Now answer the survey question as the person described below. Use the persona
AND what you learned from the search summary. This is a survey response, not a
factual exam.
PERSONA (JSON):
{persona_json}
PERSONA (Narrative):
{persona_narrative}
DEMOGRAPHICS:
{demographics}
| PRE-KNOWLEDGE | (before | search): |     |     |     |
| ------------- | ------- | -------- | --- | --- | --- |
{preknowledge_json}
SEARCH SUMMARY:
{search_summary_json}
INSTRUCTIONS:
| - Choose | the option | that best matches | your view. |     |     |
| -------- | ---------- | ----------------- | ---------- | --- | --- |
- Do not write a long essay; 1-3 sentences of justification is enough.
| - Output                | JSON only in       | the required | schema:   |     |     |
| ----------------------- | ------------------ | ------------ | --------- | --- | --- |
| { "value":              | <int_or_string>,   | "label":     | <string>, |     |     |
| "confidence":           | "high|medium|low", |              |           |     |     |
| "reason":               | <1-3 sentences>,   |              |           |     |     |
| "influenced_by_search": |                    | true|false   | }         |     |     |
QUESTION:
{question_text}
| RESPONSE | OPTIONS: |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- |
{options_list}
48

References
[1] Argyle, L. P. et al. Out of One, Many: Using Language Models
to Simulate Human Samples. Political Analysis 31, 337–351 (2023).
URL https://www.cambridge.org/core/journals/political-analysis/article/
out-of-one-many-using-language-models-to-simulate-human-samples/
035D7C8A55B237942FB6DBAD7CAA4E49.
[2] Horton, J. J. Large Language Models as Simulated Economic Agents: What Can
We Learn from Homo Silicus? (2023). URL http://arxiv.org/abs/2301.07543.
[3] Park, J. S. et al. Generative Agent Simulations of 1,000 People (2024). URL
http://arxiv.org/abs/2411.10109.
[4] Wang,A.,Morgenstern,J.&Dickerson,J.P. Largelanguagemodelsthatreplace
humanparticipantscanharmfullymisportrayandflattenidentitygroups. Nature
Machine Intelligence 7,400–411(2025). URLhttps://www.nature.com/articles/
s42256-025-00986-z.
[5] Murthy, S. K., Ullman, T. & Hu, J. Chiruzzo, L., Ritter, A. & Wang, L. (eds)
One fish, two fish, but not the whole sea: Alignment reduces language models’
conceptual diversity. (eds Chiruzzo, L., Ritter, A. & Wang, L.) Proceedings of
the 2025 Conference of the Nations of the Americas Chapter of the Association
for Computational Linguistics: Human Language Technologies (Volume 1: Long
Papers), 11241–11258 (Association for Computational Linguistics, Albuquerque,
New Mexico, 2025). URL https://aclanthology.org/2025.naacl-long.561/.
[6] Dillion, D., Tandon, N., Gu, Y. & Gray, K. Can AI language models replace
human participants? Trends in Cognitive Sciences 27, 597–600 (2023). URL
https://www.sciencedirect.com/science/article/pii/S1364661323000980.
[7] Yang, Z. et al. OASIS: Open Agent Social Interaction Simulations with One
Million Agents (2025). URL http://arxiv.org/abs/2411.11581.
[8] Ge,T.etal. ScalingSyntheticDataCreationwith1,000,000,000Personas(2025).
URL http://arxiv.org/abs/2406.20094.
[9] Zhang, S. et al. Personalizing Dialogue Agents: I have a dog, do you have pets
too? (2018). URL http://arxiv.org/abs/1801.07243.
[10] Kang, M. et al. Deep Binding of Language Model Virtual Personas: a Study on
Approximating Political Partisan Misperceptions (2025).
[11] Moon, S. et al. Virtual Personas for Language Models via an Anthology of
Backstories (2024). URL http://arxiv.org/abs/2407.06576.
49

[12] Toubia, O. et al. Twin-2K-500: A dataset for building digital twins of over 2,000
people based on their answers to over 500 questions (2025). URL http://arxiv.
org/abs/2505.17479.
[13] Lohr,S.L. Sampling:DesignandAnalysis 3edn(ChapmanandHall/CRC,Boca
Raton, 2021). URL https://www.taylorfrancis.com/books/9780429298899.
[14] Li, C. J. et al. Simulating Society Requires Simulating Thought (2025). URL
http://arxiv.org/abs/2506.06958.
[15] Mairesse, F., Walker, M. A., Mehl, M. R. & Moore, R. K. Using Linguistic Cues
for the Automatic Recognition of Personality in Conversation and Text. Journal
of Artificial Intelligence Research 30, 457–500 (2007). URL https://jair.org/
index.php/jair/article/view/10520.
[16] Clifton,J.D.W.et al. Primalworldbeliefs. Psychological Assessment 31,82–99
(2019).
[17] Jost, J. T. & Amodio, D. M. Political ideology as motivated social cognition:
Behavioral and neuroscientific evidence. Motivation and Emotion 36, 55–64
(2012).
[18] McAdams, D. P. Narrative identity (Springer Science + Business Media, New
York, NY, US, 2011).
[19] Schwartz, H. A. et al. Personality, gender, and age in the language of social
media: the open-vocabulary approach. PLoS One 8, e73791 (2013). URL https:
//dx.plos.org/10.1371/journal.pone.0073791.
[20] Ferrara, E. Should ChatGPT be Biased? Challenges and Risks of Bias in Large
Language Models. First Monday (2023). URL http://arxiv.org/abs/2304.03738.
[21] Mohsin, M. A. et al. On the Fundamental Limits of LLMs at Scale (2025). URL
http://arxiv.org/abs/2511.12869.
[22] Bailey, E. R., Matz, S. C., Youyou, W. & Iyengar, S. S. Authentic self-
expressiononsocialmediaisassociatedwithgreatersubjectivewell-being.Nature
Communications 11, 4889 (2020). URL https://www.nature.com/articles/
s41467-020-18539-w.
[23] Kosinski, M., Stillwell, D. & Graepel, T. Private traits and attributes are pre-
dictable from digital records of human behavior. Proceedings of the National
Academy of Sciences 110, 5802–5805 (2013). URL https://pnas.org/doi/full/10.
1073/pnas.1218772110.
[24] Park, P. S., Schoenegger, P. & Zhu, C. Diminished Diversity-of-Thought in a
Standard Large Language Model (2023). URL http://arxiv.org/abs/2302.07267.
50

[25] Wright,A.G.C.etal. Assessingpersonalityusingzero-shotgenerativeAIscoring
of brief open-ended text. Nature Human Behaviour 1–15 (2026). URL https:
//www.nature.com/articles/s41562-025-02389-x.
[26] Kish, L. Survey sampling A Wiley Interscience Publication (Wiley, New York,
1995).
[27] Little, R. J. A. & Rubin, D. B. Statistical analysis with missing data 3rd edition
edn. Wiley series in probability and statistics (Wiley, Hoboken, NJ, 2020).
[28] S¨arndal, C.-E., Swensson, B. & Wretman, J. H. Model assisted survey sampling
1. softcover print edn. Springer series in statistics (Springer, New York Berlin
Heidelberg, 2003).
[29] ALWIN, D. F. & KROSNICK, J. A. The Reliability of Survey Attitude
Measurement: The Influence of Question and Respondent Attributes. Sociolog-
ical Methods & Research 20, 139–181 (1991). URL https://doi.org/10.1177/
0049124191020001005.
[30] Pew Research Center. Public Opinion on Abortion (2025). URL https://www.
pewresearch.org/religion/fact-sheet/public-opinion-on-abortion/.
[31] Krogstad, S. M. a. J. M. Trump and Harris Supporters Differ on
Mass Deportations but Favor Border Security, High-Skilled Immigration
(2024). URL https://www.pewresearch.org/race-and-ethnicity/2024/09/27/
trump-and-harris-supporters-differ-on-mass-deportations-but-favor-border-security-high-skilled-immigration/.
[32] Taylor Orth. Bipartisan majorities want the govern-
ment to release its Jeffrey Epstein records | YouGov
(2025). URL https://today.yougov.com/politics/articles/
53427-bipartisan-majorities-want-government-to-release-jeffrey-epstein-records-november-15-17-2025-economist-yougov-poll.
[33] Anthony Salvanto & Jennifer De Pinto. CBS News poll finds most
would oppose U.S. military action in Venezuela, say Trump hasn’t
explained - CBS News (2025). URL https://www.cbsnews.com/news/
poll-venezuela-u-s-military-action-trump/.
[34] Converse, P. E. The nature of belief systems in mass publics (1964). Critical
Review 18, 1–74 (2006). URL http://www.tandfonline.com/doi/abs/10.1080/
08913810608443650.
[35] Zaller, J. & Feldman, S. A Simple Theory of the Survey Response: Answering
Questions versus Revealing Preferences. American Journal of Political Science
36, 579–616 (1992). URL https://www.jstor.org/stable/2111583.
[36] Krosnick, J. A. Response strategies for coping with the cognitive demands of
attitude measures in surveys. Applied Cognitive Psychology 5, 213–236 (1991).
51

URL https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.2350050305.
[37] Yao, S. et al. ReAct: Synergizing Reasoning and Acting in Language Models
(2023). URL http://arxiv.org/abs/2210.03629.
[38] Deville, J.-C., S¨arndal, C.-E. & Sautory, O. Generalized raking procedures in
survey sampling. Journal of the American Statistical Association 88, 1013–
1020 (1993). URL https://www.tandfonline.com/doi/abs/10.1080/01621459.
1993.10476369.
52