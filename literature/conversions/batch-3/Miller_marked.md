---
conversion_metadata:
  converted_at: "2026-07-21T14:17:10Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Miller.pdf"
  source_pdf_sha256: "1db1bd3e32bb817ed1a615bcb2a50949bd57c7b6b38ba001e0f9bffb75125259"
  page_count: 10
  markdown_char_count: 119518
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Explainable AI is Dead, Long Live Explainable AI!
Hypothesis-driven Decision Support using Evaluative AI

Tim Miller
tmiller@unimelb.edu.au
The University of Melbourne
Melbourne, VIC, Australia

ABSTRACT
In this paper, we argue for a paradigm shift from the current model
of explainable artificial intelligence (XAI), which may be counter-
productive to better human decision making. In early decision
support systems, we assumed that we could give people recommen-
dations and that they would consider them, and then follow them
when required. However, research found that people often ignore
recommendations because they do not trust them; or perhaps even
worse, people follow them blindly, even when the recommenda-
tions are wrong. Explainable artificial intelligence mitigates this by
helping people to understand how and why models give certain rec-
ommendations. However, recent research shows that people do not
always engage with explainability tools enough to help improve
decision making. The assumption that people will engage with
recommendations and explanations has proven to be unfounded.
We argue this is because we have failed to account for two things.
First, recommendations (and their explanations) take control from
human decision makers, limiting their agency. Second, giving rec-
ommendations and explanations does not align with the cognitive
processes employed by people making decisions. This position pa-
per proposes a new conceptual framework called Evaluative AI
for explainable decision support. This is a machine-in-the-loop par-
adigm in which decision support tools provide evidence for and
against decisions made by people, rather than provide recommenda-
tions to accept or reject. We argue that this mitigates issues of over-
and under-reliance on decision support tools, and better leverages
human expertise in decision making.

CCS CONCEPTS
• Computing methodologies → Artificial intelligence; • Human-
centered computing → HCI theory, concepts and models.

ACM Reference Format:
Tim Miller. 2023. Explainable AI is Dead, Long Live Explainable AI!: Hypothesis-
driven Decision Support using Evaluative AI. In 2023 ACM Conference on
Fairness, Accountability, and Transparency (FAccT ’23), June 12–15, 2023,
Chicago, IL, USA. ACM, New York, NY, USA, 10 pages. https://doi.org/10.
1145/3593013.3594001

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0192-4/23/06. . . $15.00
https://doi.org/10.1145/3593013.3594001

1 INTRODUCTION
Imagine you have two friends, Bluster and Prudence1. Whenever
you have a difficult decision to make, you can approach them for
help. Both have shown excellent judgement on complex decisions
in the past. Bluster always tells you what they think is the right
decision, even when they are not confident, and then tells you
why they think that. But Bluster does not consider what you think.
Would that be helpful? If your decision and reasons were the same
as Bluster’s, it would give you confidence. If not, Bluster could
change your mind to an answer that you were happier with or that
resulted in better outcomes. Prudence, in contrast, hardly ever gives
their opinion, especially when not confident. Prudence instead asks
you what you are proposing and then provides feedback: evidence
for and against your proposed decision. If you propose alternatives,
Prudence provides feedback on these, giving feedback until you
reach a decision. But Prudence never gives you an answer. Would
this be helpful? Prudence helps you to form a decision, and provides
feedback on your own options, rather than justifying their own
opinion. This would help you to question your decisions, and would
give you control over which options you receive feedback for.

Reader, which would you prefer? An informal survey conducted
by the author during a recent talk showed that just three out of over
100 people preferred Bluster; the remaining 100+ people preferring
Prudence. Prudence helps us find strengths and weaknesses in
our thinking and gives us control over which options we discuss
with them. The ability to assess the strengths and weaknesses of
judgements and decisions is key to expert decision making [18, 20].
Despite this preference, the current model of (explainable) AI-
assisted decision support gives us Bluster instead of Prudence, right?
AI decision aids are designed to tell the user what they think the
best answer is (e.g. a recommendation), and explain why that is
considered the best answer. This is a ‘recommend and defend’2
approach. If the user disagrees or does not find the reasons convinc-
ing, the machine offers little else. A counterfactual explanation [27]
allows us to ask why another option is not the best answer; but does
not provide us with reasons the alternative may well be the right
answer or a good answer. ‘Recommend and defend’ approaches,
which we call recommendation-driven decision support, do little
to help us critique its answers or our own ideas.

The Bluster model of recommendation-driven decision support
leads to two problems. First, AI tools are not correct all of the time,
so we should be sceptical at least some of the time. However, people
find it difficult to correctly calibrate their trust in a decision aid [10,
13, 21, 37]. Research shows that people tend to either under-rely on

1Thanks to Piers Howe for these names.
2Sean Koon introduced this nice term to me.

---

<!-- PAGE 2 -->

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

but that the evaluative AI paradigm is still a form of explainable
AI, and many of the current paradigm will play a part in this new
conceptualisation; so, long live explainable AI!

Section 2 reviews related work on cognitive decision making,
what makes a good decisions, and the main modes of explainable AI.
Section 3 evaluates how current decision support models align with
human decision making processes, with a focus on explainable and
interpretable AI. Section 4 presents evaluative AI, a new conceptual
framework for human-centred decision making, and argues that
this framework aligns better the cognitive processes humans use
for decision making. It also presents a high-level research agenda
for evaluative AI. Section 5 concludes the paper.

2 AI-ASSISTED DECISION SUPPORT
2.1 Decision making and decision support
Before we consider what makes good decision support, we consider
what good decision making is. A definition of ‘decision making’ is
surprisingly elusive. Often, definitions consider three steps [12]: (1)
an assessment of the situation, such as what options are available;
(2) making judgements and trade-off about options; and (3) selecting
an option or committing to a course of action. Hoffman and Yates
[12] argue that this ‘final-point notion’, in which there is a point
that decision “made” is a (sometimes useful) simplification of the
decision-making process. However, as a model, it misses some
important aspects of decision support; importantly: that decision
making is a process, not a point in time.

Table 1 outlines 10 cardinal decision issues, defined by Yates and
Potworowski [45]. These include issues such as deriving options
and making judgements, but also factors such as exploring conse-
quences of actions, and who will be part of deciding. The issues
in italics are the aspects that we believe to be of most importance
to AI-assisted decision support. While the first three and the final
issue can be supported, these are less relevant for AI research.

We define a decision aid (DA) as any system that supports the
process of deciding. But what is a good DA? In Table 2, we propose
six criteria for good decision support. The first five are based on
the 10 cardinal issues from Table 1 [12, 45]. The criteria that are
omitted can certainly be supported by a DA, but these criteria are
decisions in their own right, and therefore the six criteria apply to
each. The sixth criteria is understandable, which simply means that
a good DA helps people understand how and why it works, and
where it fails. This is a common criteria for AI-based DAs [9], and
is important to calibrate trust & reliance, and to find mistakes.

Note two things about the criteria in Table 2. First, a DA helps
a decision maker. It does not necessarily provide the answers for
any of the criteria. Second, it goes beyond recommendations and
judgements, which are typically the focus in XAI; largely because
these are considered to be some of the harder problems.

2.2 Cognitive processes for decision making
Hoffman et al. [11] argue that, when a person tried to understand a
system output, they engage in the cognitive process known as ab-
ductive reasoning. Abductive reasoning is the process of forming
hypotheses and judging their likelihood for the purpose of explain-
ing observations or facts [30]. This abductive process is engaged
as soon as people start interacting with a system, irrelevant of any

Figure 1: Contrastive explanation vs. Evaluative AI. Con-
trastive paradigms are ‘recommend and defend’ approaches.
They provide evidence that supports the recommendation
and refutes all others. Evaluative AI proposes not necessarily
giving recommendations from machines, but instead provid-
ing evidence for/against each option.

tools, meaning they have no effect on decision making, or they over-
rely on tools [1, 6, 37], likely because providing recommendations
makes them fixate on that recommendation. Both under- and over-
reliance have negative consequences [29]. Second, Bluster reduces
our locus of control [36], because we cannot control which options
we received feedback for.

This paper argues for a paradigm shift: that the decision aids
(DAs) should be less like Bluster, and more like Prudence, which
we call hypothesis-driven decision support, . We propose a new
conceptual framework for decision support, with two key properties
not present in the current paradigm. First, evaluative AI tools do
not provide recommendations. They mitigate fixation by either
allowing the decision maker to determine which options are best or
helping them to narrow down to a manageable set of options [34].
Second, instead of justifying AI recommendations, DAs generate
and present evidence to support or refute human judgements, and
explain trade-offs between any set of options, not just the machine
recommendation. This helps with trust calibration because the
machine does not give recommendations, as well as over/under-
reliance because there is no recommendation to follow. We argue
that the reason this Prudence-like approach is more effective for
decision support because it aligns with the cognitive decision-
making process that people use when making judgements
and decisions [11, 17, 30]. We call this paradigm evaluative AI.
Figure 1 shows the difference between evaluative AI and perhaps
the most common form of explainability: contrastive explanation.
Contrastive explanation is like Bluster — it gives us an answer and
justifies it, telling us why it is correct and why other options are
not. Evaluative AI is like Prudence — it helps us critique our own
ideas. This provides a better feedback loop – if the evidence helps
use eliminate our preferred hypothesis, we start to explore others.
Evaluative AI is not intended to be used in all scenarios. It is
more suitable for medium- and high-stakes decisions when the de-
cision maker is ultimately accountable, and low frequency decision
making where the decision maker has time to explore options.

We conclude that for decision making, the recommendation-
driven paradigm of explainable AI is ‘dead’ (for some situations),

---

<!-- PAGE 3 -->

Explainable AI is Dead, Long Live Explainable AI!

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Table 1: The 10 ‘cardinal decision issues’ outlined by Yates
and Potworowski [45]. The issues in italics represent those
that are of most interest to explainable AI.

Cardinal issue Definition

Need

Mode

Investment

Options

Possibilities

Judgement

Value

Trade-offs

Acceptability

Why do we need to make a decision at all?

Who will decide and how will they do it?

What kinds of amounts of resources will be
invested in the process?

What are the different actions we could take
to solve the need?

What outcomes could happen if for each ac-
tion, if it were taken?

Which of the outcomes would happen if we
took the action?

How much would any stakeholder care if this
outcome happened?

How do we trade-off the outcomes to settle
on an action?

How can we get other stakeholders to accept
our decision?

Implementation Now we have decided, how can we action it?

Table 2: Criteria for good decision support, based on the 10
‘cardinal decision issues’ [45]

Criteria

Options

Possibilities

Definition

Help to identify options, as well as help to
narrow down the list of feasible or realistic
options

Help to to identify possible outcomes for each
of the identified options

Judgement

Help to judge which outcomes are most likely

Value

Trade-offs

Help to identify the positive and negative im-
pacts on stakeholders for each of the identi-
fied options

Help to make trade-offs on the above criteria
for each options

Understandable Help to understand how and why the tools

works as it does, and when it fails

particular explainability or interpretability tools. As such, Hoff-
man et al. argue that abductive reasoning is a suitable foundational
model for conceptualising explainable AI.

Peirce [30] defines the process of abductive reasoning as five

step process, outlined in Figure 23:

(1) Observe an event or phenomenon: A person observes an event,
usually one that is surprising and does not fit their current

3The final step of extending the explanation is omitted because it simply repeats the
process when new events are observed.

Figure 2: A model of abductive reasoning. When someone
observes an event, they generate hypotheses of the cause,
and then judge the plausibility of (some) hypotheses; poten-
tially iterating to generate more hypotheses as new evidence
emerges. Eventually, the understanding is resolved.

mental model. This leads to them to start searching for ex-
planatory hypotheses.

(2) Generate hypotheses: The person generates potential reasons
for why they would have observed the event or phenomenon.
The reasons are hypotheses.

(3) Judge the plausibility of the hypotheses: The person searches
for evidence that may support or undermine different hy-
potheses, perhaps ruling out some or making some more
likely. Some hypotheses are ruled out, while others are judged
as more likely. This process may lead to new hypotheses.
(4) Resolve understanding: A particular hypothesis fits the new
observation and previous experience of the decision maker,
so is adopted as the most likely cause of the observation.
This may be a tentative resolution.

(5) Extend: Revise and extend the process when new evidence

is observed or considered.

This philosophical model of decision making is supported by
research from cognitive science. Klein et al. [17] present a theory
of sensemaking known as the Data/Frame Theory, built from stud-
ies with expert decision makers. The frame, a generalisation of a
hypothesis, is a model of how something works, while the data
contains observations made and inferences that combine the obser-
vations and the frame. The data is used to adjust the frame (similar
to judging plausibility) and the frame is used to determine what new
data to find, what outcomes to evaluate, and how these relate. Klein
et al. show that people make decisions by first using their intuition
to narrow down to a set of likely options (the frames), and then go-
ing through each option one-by-one, searching for evidence (data)
to make judgements. Good decision makers search for evidence
that both supports and refutes a hypothesis. Klein et al. [17] argue
that abductive reasoning plays a central role in this process. We
build the evaluative AI framework around the Data/Frame model.
Hoffman et al. [11] argue that abductive reasoning is a suitable
foundation for conceptualising explainable AI. In this paper, we
argue for a similar — yet orthogonal — view; specifically, explain-
able AI for decision making. In decision making, the decision
maker is involved in two (related) reasoning processes. First,
the decision maker is trying to make a judgement/decision about
the world (e.g. a diagnosis). The observed event is something that
needs explaining, such as a medical symptom, the hypotheses are
the potential causes of that observation, such as a disease, and
the judgement is about the likelihood of a particular hypotheses
being true given the evidence. Second, the decision maker is also

---

<!-- PAGE 4 -->

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

making a judgement about the DA (e.g. whether its reasoning is
sound, as proposed by Hoffman et al. [11]). The observed event is
an output 𝑜 of an AI system 𝑓 given an input 𝑖. The hypotheses char-
acterise which combinations of inputs 𝑖 and computations (parts
of 𝑓 ) caused this output to occur. The process of judgement is to
determine why the system produced the output that it did. Table 3
outlines this for a medical diagnosis scenario. Decision makers need
to ‘invert’ the explainable AI process to align with the decision-
making process. Hoffman et al. argue that machines reasoning in
an abductive manner align better with this process. The argument
in this paper is similar, but rather than necessarily giving abductive
explanations, we argue that DAs should be designed to explicitly
support abductive reasoning.

Table 3: How Explainable AI and Evaluative AI align against
the human abductive reasoning process.

Human
Reasoning

Explainable AI Evaluative AI

Event to explain AI diagnosis

Medical symptoms

Hypotheses

AI reasoning

Medical conditions

Evidence

Judgement

Models,
Explainability

Evidence for/against
hypotheses

Causes between
inputs & AI
diagnosis

Likelihood of
medical conditions

2.3 Explainable AI and decision making
The initial assumption of AI-assisted DAs was that people would
follow recommendations when required, leading to better deci-
sions. However, issues such as warranted and unwarranted distrust
[13] mean that AI systems are often deployed and then largely
ignored [9, 37]. Explainable/interpretable AI aims to mitigate these
by helping people to understand why decisions are made. How-
ever, recent research has shown that the recommendation-driven
explainable/interpretable AI has little effect on decision making
[1, 6–8, 28, 32], although this is not always the case [22, 23, 41].
The two primary issues are over-reliance and under-reliance. Over-
reliance means decision makers accept a machine recommendations
even when it is wrong, caused by unwarranted trust [13]. This is
often attributed to automation bias, where the machine is “must
be right” because it is a machine. Under-reliance means decision
makers reject a machine recommendation even when it is correct,
caused by unwarranted distrust [13]. This is often attributed to
algorithmic aversion, where machine outputs are rejected but would
be accepted had they come from a human. In either case, a poor
decision can often be attributed to fixation [17] — searching for
evidence to support one hypothesis without considering others.

Some experimental studies [2, 5, 42] indicate that most partici-
pants do not cognitively engage with explainability tools. Partic-
ipants who do seem to believe that they understand explanatory
information, leading to over-confidence [2], even when presented
with explanations that contain no useful information [5]. We have
seen this in currently unpublished observational studies. In a study

where expert board gamers used an AI-based recommendation
system, we saw that many players did not truly engage with recom-
mendations or explanatory information either. When they did, we
saw some behavioural changes, but not enough to see a statistically
significant improvement in decision making.

Similarly, in experiments on a general task with general partic-
ipants, Buçinca et al. [1] and Gajos and Mamykina [6] show that
explainability did not mitigate over-reliance, and in some cases it
increased over-reliance. They assert that this is because participants
did not pay attention to explainability information. They propose
three cognitive forcing strategies to mitigate over-reliance, such as
forcing people to give a decision before seeing a recommendation.
Their results showed that cognitive forcing slightly mitigated over-
reliance, compared to feature-based and uncertainty judgements,
particularly disregarding incorrect AI recommendations, but with
no statistically significant differences in task performance. Interest-
ingly, despite cognitive forcing functions being more effective, they
were least preferred by participants. Buçinca et al. [1] attribute this
to the phenomenon of people not wanting to exert mental energy
[19]. This indicates that Evaluative AI could prove useful by not
fixating people on particular recommendations, but allowing peo-
ple to assess whether evidence supports their hypotheses, rather
than trying to understand the DA’s reasoning.

These studies show that the recommendation-driven XAI does
little to mitigate over- and under-reliance. This has lead to several
authors to argue that XAI research should return to the founda-
tion of cognitive and social processes involved in decision making
[7, 8, 15, 42, 44]. Some authors [1, 6, 42] have attributed the cause
of ignoring explanatory information to the ‘failure’ of system 1
processing in dual process theory [14]. In brief, the theory is that
system 1 thinking (fast, heuristic, and biased) ‘interferes’ with sys-
tem 2 thinking (slow and more accurate). The conclusion that is
often, but not always drawn, is that DAs should aim to support
system 2 thinking and prevent system 1 ‘interference’.

However, we caution against the idea of prioritising sys-
tem 2 thinking over system 1 thinking, for three reasons. First,
research in Naturalistic Decision Making (NDM) demonstrates
that ‘system 1’ thinking, which they call intuition, is a power-
ful source of problem solving that often produces better and/or
faster decisions than system 2 [16]. For example, Coderre et al.
[3] found that intuition significantly outperformed hypothetico-
deductive reasoning in gastroenterology clinical diagnoses. Klein
[18] show that experts make decisions by first using their intu-
itive problem solving ability to generate likely options, and then
using both intuition and slower structured thinking to assess which
options will work. As such, any technique that aims to ‘override’
intuitive thinking risks losing the benefits of expertise and prior
knowledge. Second, there is now sufficient research questioning
whether the system 1 vs system 2 distinction is so clear [25, 35].
For example, many experiments showing biases system 1 thinking,
such as base-rate fallacies, could be partly attributed to the experi-
ment design [35], which may not reflect many environments where
real decisions are made. Finally, we need further research using
expert decisions makers, rather than just general participants, as
well as studies where poor decisions have real consequences. The
effect of system 1 thinking may differ between contexts such as
the experience of the decision maker and the stakes of the decision.

---

<!-- PAGE 5 -->

Explainable AI is Dead, Long Live Explainable AI!

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

In short, we argue against simply treating intuition as ‘bad’. DAs
should exploit the strengths of intuition and expertise, as well as
structured thinking.

3 (EXPLAINABLE) AI AS DECISION SUPPORT
This section provides a narrative of how we have arrived at the
current status quo. We evaluate the four dominant paradigms of
decision support against the criteria of decision support identified in
Table 2. The four paradigms we discuss are: (1) recommendations; (2)
recommendations with explanatory information; (3) interpretable
models; and (4) cognitive forcing.

3.1 Giving recommendations with no

explanatory information

The idea of decision support using AI came from the use of AI
as automation. Given situations in which an AI model provides
more accurate judgements/decisions than human decision makers,
a simple of model of AI-assisted DAs is to give recommendations,
which decision makers can then take into account. Recommenda-
tions can be ranked lists of options such as in many recommender
systems, but the typical model is to propose just the one recom-
mendation that the AI model determines is the most likely or ‘best’.
The assumption here is that for situations in which DAs can handle
many more factors simultaneously, it can provide insight when the
assumptions of the underlying modelling theory hold. This model
is depicted below in Figure 3.

Figure 3: A model of giving recommendations for decision
support. This assumes that decision makers will carefully
consider recommendations. However, empirical evidence
suggests this is not the case.

The primary issue with this model was that, even if the DA
gives better judgements/decisions than the human, people tend
to ignore this due to unwarranted distrust [9, 10, 13, 26, 37, 39] or
accept wrong decisions due to unwarranted trust [1, 6, 29]. The
inability to scrutinise why decisions are made mean that the only
information to rely upon to judge the correctness is: (1) extrinsic
information such as accuracy measures; and (2) the decision makers’
own expertise and knowledge. Given the former does not change
from decision to decision, it is unsurprising that experts rely on
their own expertise and novices over-rely on the tool [37].

Comparing this to the properties that comprise good decision
support outlined in Table 2, we can see why this approach is largely
inneffective. Giving only recommendations:

(1) does not help to provide new options or to filter out unlikely

options;

(2) does not consider possibilities or judgements beyond one

option;

(3) does not help determine stakeholder values;

(4) does not support making trade-offs; and
(5) does not provide understanding of the machine decision.

Can this still be useful? Of course! If a recommendation matches
or is similar to our own judgement, it gives us confidence in our
own decision, although this confidence may be misplaced. Further,
if a recommendation is not similar to our own judgement, it may
decrease our confidence and make us reconsider, potentially helping
us to make a better decision. However, in either case, we receive
no further support to help with the decision.

3.2 Giving recommendations with explanatory

information

One solution to mis-calibrated trust is to provide explanatory infor-
mation. This means giving justifications for decisions, providing
evidence to support the decisions, and making models simple and
easy to understand (see more on this in Section 3.3). A model of
interaction between decision maker and DA is shown in Figure 4.
Comparing this to the properties that comprise good decision
support outlined in Table 2, we can see the criteria that the default
model of XAI bring are that it:

(1) does not help to provide new options or to filter out unlikely

options;

(2) partially considers possibilities or judgements beyond one
option: contrastive explanations argue why other options
are NOT recommended;

(3) does not help determine stakeholder values;
(4) partially supports making trade-offs; and
(5) does provide understanding of the machine decision.

So, explainability provides understanding. Contrastive explana-
tions [27] partially support trade-offs when they answer ‘Why 𝐴
instead of 𝐵?’, where 𝐴 is the output and 𝐵 a foil. However, this still
defends the recommendation. Can this be useful? Of course! If we
agree with the recommendation, we can check that we agree for
similar reasons; and if we disagree, we can check the reasons why,
potentially helping us to improve our initial decision.

3.3 Giving recommendations with an

interpretable model

The third paradigm is to give recommendations using an ‘inter-
pretable’ model. Rudin [33] argues that for high-stakes decisions,
people should avoid using black-box models altogether, and instead
should use interpretable models. Interpretable models use a small
set of features with a low complexity of interaction between them.
The model of interaction with an interpretable model is same as
for recommendations with explanatory information, outlined in Fig-
ure 4. The assumption is that because the model is interpretable, it
contains most of the explanatory information that is required. How-
ever, interpretable models are not designed with decision support in
mind. The model’s options, possibilities, and trade-offs would have
to be calculated by the decision maker. Assistance to calculate these
is a combination of interpretability and explainability, so overlaps
with the previous section. Effectively, the purpose of interpretable
models is complementary to the criteria in Table 2.

---

<!-- PAGE 6 -->

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

Figure 4: A model of explainable AI for decision support. This assumes that the problem of distrust can be mitigates by
giving reasons or explanations for decisions. However, empirical evidence suggests people do not pay careful attention to the
reasons/explanations.

Comparing this to the properties that comprise good decision
support outlined in Table 2, we can see the criteria that the inter-
pretability brings are that it:

(1) does not help to provide new options or to filter out unlikely

options;

(2) does not consider possibilities or judgements beyond one

option;

(3) does not help determine stakeholder values;
(4) does not support making trade-offs; and
(5) does provide understanding of the machine decision.

3.4 Cognitive forcing
The final paradigm is cognitive forcing. The assumption of cog-
nitive forcing is that forcing people to engage with the decision
cognitively can mitigate over-reliance. Gajos and Mamykina [6]
and Buçinca et al. [1] implement this idea using three approaches,
as outlined in Section 2.3. The commonality between these three
approaches is that decisions are initially withheld from the deci-
sion maker, but explanatory information is provided, forcing the
decision maker to engage with the explanatory information. This
model is depicted below in Figure 5. Withholding recommenda-
tions ‘forces’ the decision maker to cognitively engage with the
decision and therefore, to consider different options and make trade-
offs. Giving explanatory information from the start may help the
decision maker to focus on useful information.

Comparing this to the properties that comprise good decision
support outlined in Table 2, we can see the criteria that cognitive
forcing brings are that it:

(1) partially helps to provide new options or to filter out un-

likely options by forcing the decision maker to do so;
(2) does not consider possibilities or judgements beyond one

option;

(3) does not help determine stakeholder values;
(4) partially supports making trade-offs; and
(5) does provide understanding of the machine decision.

While this is an improvement beyond the default XAI approaches,
weaknesses remain. First, this approach is still an instance of our
friend Bluster, rather than our friend Prudence – it is just that
Bluster pauses before stating their opinion. Second, it does not
provide helpful decision-making information for options other than
the recommendation.

Next, we propose a model that builds on the strength of cognitive
forcing, but on a foundation of the cognitive science of decision
making.

4 EVALUATIVE AI: A CONCEPTUAL

FRAMEWORK OF EXPLAINABLE DECISION
SUPPORT

In this section, we present a new conceptual framework of hypothesis-
driven explainable decision support called evaluative AI. The two
primary design criteria for this are:

(1) Support the properties of good decision making outlined in
Section 2.3. That is, support the decision maker’s cognitive
decision making process.

(2) Provide better internal locus of control [36] to the decision

maker about which options to explore and when.

To do this, we propose that the vision of evaluative AI is to:

Support the decision maker to access the infor-
mation they want and need to evaluate a hypoth-
esis, when they want it.

4.1 Conceptual framework
The conceptual framework for evaluative AI is shown in Figure 6.
Evaluative AI does not (necessarily) provide recommendations, but
instead offers support to filter out unlikely options, generate new
hypotheses, or both. The decision maker then analyses a hypothesis,
asking the DA to provide evidence for and against the hypothesis.
Evidence could also be presented contrastively: what is the evi-
dence for/against a particular hypothesis rather than some other
hypothesis. Importantly, the decision maker to maintains control
over which hypotheses to explore.

4.1.1 Options. Existing explainable AI approaches tend to pro-
vide one or sometimes two options to consider. The evaluative AI
paradigm argues that the presentation of options should be context-
specific. For example, given a probabilistic classifier, a evaluative
AI system could highlight options that are within a certain prob-
ability of the most likely, perhaps withholding the probabilities
themselves. Alternatively, it could use uncertainty estimates, which
are known to help decision making [40], and from that, determine
which options to filter. Approaches such as this help to reduce fixa-
tion because there is no single recommendation. Cognitive forcing
takes a similar approach, but current cognitive forcing techniques
are recommendation-driven [1, 6].

Judgement support. All five paradigms support judgements.
4.1.2
The evaluative AI framework puts the human at the centre of the
judgement process. In this framework, the judgement is made by
the human decision maker with support from the DA, which gives
feedback (evidence for/against) of proposed hypotheses. This is

---

<!-- PAGE 7 -->

Explainable AI is Dead, Long Live Explainable AI!

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Figure 5: A model of cognitive forcing. By withholding recommendations (for perhaps a short period) and giving an ‘explanation’,
it forces people to engage, limiting over-reliance. However, it is still a ‘recommend and defend’ approach.

to support human decision makers. However, research into machine-
assisted option awareness is still in its infancy.

4.2 Example: Diagnosis
Consider an example of a DA for diagnosing skin cancers, such as
the ISIC 2018 lesion diagnosis challenge4. There are seven possible
disease categories: (1) melanoma; (2) melanocytic nevus; (3) basal
cell carcinoma; (4) actinic keratosis; (5) benign keratosis; (6) der-
matofibroma; and (7) vascular lesion. Given a dermoscopic image
of a legion along with some meta information, such as where the
lesion is found, the task is to diagnose the most likely category.

Figure 7 shows a simple prototype interface for such a system.
In this case, there are seven hypotheses/diagnoses. The DA filters
out those that are unlikely, leaving just three: melanoma, basal
cell carcinoma (BCC), or actinic keratsosis (AK)5, highlighted with
bold text. By highlighting only likely hypothesis instead of just one,
this could help to mitigate fixation on just one option. Hypotheses
can be explored. In Figure 7, the location of the lesion, its colour,
scarring, and that it sometimes bleeds, is strong support for a BCC
diagnosis. However, the asymmetric shape, itchiness, and recent
colour change are evidence against BCC. Other forms of evidence
could be provided to the decision maker, such as finding similar
instances using case-based reasoning [38, 44]. It is up to the de-
cision maker to make the final decision, integrating their expert
knowledge and the information from the DA.

4.3 Summary
Comparing model to the properties that comprise good decision
support outlined in Table 2, we can see the criteria that evaluative
AI brings are that it:

(1) does help to provide new options or to filter out unlikely

options by forcing the decision maker to do so;

(2) does help to identify possibilities and support judgement

for options;

(3) does not help determine stakeholder values;
(4) does support making trade-offs; and
(5) does provide understanding of the machine decision.

Table 4 compares the five approaches to explainable DAs. Evalu-
ative AI explicitly aims to provide support for options, judgement,
understanding, and trade-offs. The difference between cognitive
forcing and evaluative AI is two-fold:

(1) Cognitive processes: Evaluative AI is built on the Data/Frame
model of sensemaking [17], so supports the decision maker’s
cognitive process by allowing them to explore hypotheses,

4See https://challenge.isic-archive.com/landing/2018/47/.
5It is unlikely that these three would be the case as AK is quite different from BCC
and melanoma, but this makes for a good illustrative example.

Figure 6: A model of Evaluative AI, which aligns with decision
making processes, keeping the decision maker in control and
asking users to rely on evidence instead of recommendations.

supporting judgement, rather than giving judgement. The dif-
ference is who owns control over which hypotheses to explore. In
a recommendation-driven approach, both the human and machine
provide a judgement. In the evaluative AI paradigm, the human
provides judgement and the machine provides feedback.

4.1.3 Trade-off support. Contrastive explanations trade-off out-
comes. However, they explain only why non-recommended options
are ‘incorrect’. This is a ‘persuasive’ approach — it justifies why the
machine’s decision is correct. The evaluative AI framework instead:

(1) explains trade-offs between any two sets of options; and
(2) provides evidence both for and against each option, irrele-

vant of the judged likelihood of that option.

Good decision makers assess an option by looking for evidence
that supports it, but also evidence that refutes it. For example, in
a study with anaesthesiology residents, Rudolph [34] showed that
participants who fixated on an initial option did poorly, but that
participants who kept an open mind on all options do not per-
form much better. Instead, those who jump to an initial conclusion
and test it, looking for negative evidence, make the best decisions.
Recommendation-driven approaches typically do not provide evi-
dence against the recommendation, nor evidence supporting other
options. Evaluative AI supports both, rather than aiming to per-
suade that the machine is correct.

Supporting trade-offs has gained interest in recent years under
the name option awareness — the analysis and understanding of
various options and their relative trade-offs [31]. Pfaff et al. [31]
show that using visual analytics to allow decision makers to explore
options increases their option awareness, resulting in more accurate
and faster decisions. More recently, Drury et al. [4] proposed a
framework in which machines consider their own option awareness

---

<!-- PAGE 8 -->

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

Figure 7: A simple prototype of a diagnostic interface using evaluative AI

Table 4: A summary of the decision support provided by different paradigms. 1/𝑛means that this only provides information to
confirm the recommended option(s); ✔/✘means partial support for other options. Evaluative AI explicitly provides support
to explore options and perform trade-offs. XAI and cognitive forcing allow this if they support contrastive explanation. In
evaluative AI, it should be default.

Support provided

Decision support Options Possibilities

Judgement Value Trade-offs Understandable

Recommendation
XAI
Interpretability
Cognitive forcing
Evaluative AI

✘
✘
✘
✔/✘
✔

1/𝑛
1/𝑛
✘
1/𝑛
✔

1/𝑛
1/𝑛
✘
1/𝑛
✔

✘
✘
✘
✘
✘

✘
✔/✘
✘
✔/✘
✔

✘
✔
✔
✔
✔

rather than providing only the information to the justifies a
machine recommendation.

(2) Control: Evaluative AI explicitly hands control of which
hypotheses are investigated and prioritised to the decision
maker, resulting a machine-in-the-loop paradigm [7, 8],
rather than a human-in-the-loop paradigm.

For this reason, we assert that evaluative AI obtains the benefits
of cognitive forcing, while giving control to the decision maker to
explore the strengths and weaknesses of any option, rather than just
the strengths recommendations and the weaknesses of alternatives.

4.4 Long live explainable AI!
This article proposes a paradigm shift from recommendation-driven
decision support to hypothesis-driven decision support. Does this
imply that explainable AI is dead? We do not believe so.

First, there are applications of XAI beyond decision support,
such as verification, regulation, scientific discovery, generating
insights about underlying data, etc. Further, there are applications
where recommendation-driven approaches may be the best way to
improve decisions, such as making decisions at scale.

Second, for a machine to judge decisions, we will need an un-
derlying decision-making model, meaning that recommendation
approaches such as machine learning, planning, and optimisation
will be required, along with XAI techniques.

Third, evaluative AI is explainable AI. The cognitive and so-
cial aspects of good explainability apply to evaluative AI: [26]: (1)
explanations are contrastive; (2) explanations are selected; (3) ex-
planations are interactive; and (4) explanations are causal.

Fourth, from the earlier example, it is clear that many existing
tools will play a part in evaluative AI: constrastive explanation [27],
Weights of Evidence (WoE) [24], feature importance, case-based
reasoning techniques [38], etc., all generate evidence. New models
of XAI are needed, but existing work lays a solid foundation.

4.5 Challenges and Limitations
There are clear potential limitations with this approach. First, if
people tend to dismiss recommendations and any explainability
information, why would they pay attention to evidence? The eval-
uative AI framework makes the same assumptions as earlier work:
that people care at all about what a machine has to say. A very real

---

<!-- PAGE 9 -->

Explainable AI is Dead, Long Live Explainable AI!

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

risk is that decision makers will not engage with a tool that sup-
ports cognitive reasoning either. However, one argument against
this is that this evaluative AI provides decision makers with better
control [36, 43], and follows a process that they will naturally
follow, rather than recommendation-driven approaches, which
somewhat disrupt the decision-making process.

Second, it is difficult to imagine evaluative AI solutions will result
in lower cognitive load. A strength of the recommendation-driven
approaches is that they reduce the information that a decision maker
needs to consider to just the most relevant. Evaluative AI will likely
result in designs that force more engagement with the decision, but
less preferred by decision makers [1]. However, following a model
of abductive reasoning can still reduce information compared to
having no decision support; e.g. presenting only the most likely
hypotheses; prioritising access to the most important information,
etc. Striking this balance is a challenge.

4.6 An incomplete research agenda
In this section, we present an incomplete research agenda based
around the evaluative AI framework.

4.6.1 Observing events. The first step is observing an event. While
it is difficult to control the attention a decision maker pays to
information, we can support this in several ways:

(1) Design interfaces to make it clear what has happened,
what data is being used, etc. [11]. This includes allowing
people to explore relevant attributes of a system.

(2) Highlight anomalous behaviour/events, as these are typ-
ically the events that people require to make decisions or to
understand [26].

4.6.2 Generating options. The ability for the machine to put for-
ward options can help decision makers in two ways. First, it can
present options that decision makers did not consider. Second, it
can speed up decision making in time-sensitive environments by
filtering out some options and/or allowing options to be assessed
more systematically.

Generating options can be supported in several ways beyond

providing 1-2 recommendations or a ranking:

(1) Provide probabilities over options: This can help the
decision maker to narrow down likely options, but is perhaps
subject to over-fixation (on the most likely option) in the
same way that recommendations are.

(2) Provide a set of likely options: This can help to narrow
down the set of hypothesis without giving a recommenda-
tion, as in the example in Section 4.2, reducing fixation.
(3) Provide uncertainty measures: The DA provides its uncer-
tainty about its filtered options (a decision of set of decisions)
to encourage healthy scepticism [46].

(4) Intervention: The DA does not initially narrow down op-
tions, but allows the decision maker to explore and select
their answer, and then intervenes if it disagrees above some
threshold, prompting the decision maker to consider the
DA’s most likely responses.

(5) Relate inputs and hypotheses: The decision maker selects
the inputs they believe are important and the tool shows
which hypotheses are supported or denied by that evidence.

Judging plausibility. Judging the plausibility of outcomes can

4.6.3
be supported several ways by a DA:

(1) Explainable/interpretable AI: Provide reasoning steps
that link the evidence to the hypothesis, such as rules, deci-
sion steps, or explanations.

(2) Provide evidence weights: Show how different inputs pos-

itively and negatively contribute to a hypothesis.

(3) Provide epistemic uncertainty: Show uncertainty in the

form of e.g. an uncertainty measure using entropy.

(4) Provide aleatoric uncertainty: Show a measure of uncer-

tainty of the evidence itself.

(5) Evidence selection: Allowing the decision maker to change

evidence (inputs) and ask the DA to re-evaluate.

(6) Argumentation: The decision maker identifies evidence
that supports (refutes) a hypothesis, and the DA highlights:
(a) other evidence that strongly refutes (supports) that hy-
pothesis; and (b) other hypotheses that are strongly sup-
ported (refuted) by that evidence.

4.6.4 Resolution and re-evaluation. For any DA, it is important that
justification for that decision is recorded. Allowing the decision
maker to record: (a) the outcome; (b) evidence for/against that
outcomes; and (c) alternatives that were not chosen and why; is
important for both decision resolution and also re-evaluation. Note
that recording evidence must include evidence that is used by the
human decision maker but not available to the DA. Further research
is required to determine how to support decision makers when re-
evaluating a decision to come up to speed quickly and effectively.

5 CONCLUSION
Our friends Bluster and Prudence can both be useful in supporting
our decisions, but Prudence puts us in control and is better at
helping us weigh up different options. Bluster can be useful; for
example, in low stakes decisions or if time is limited; but overall,
Bluster does not support our cognitive process as well as Prudence.
This paper calls for AI-assisted DAs to follow the lead of Prudence,
and it presents a new conceptual framework of machine-in-the-loop
DAs. We call this conceptual framework evaluative AI.

However, evaluative AI is not a panacea for DAs. Our friend
Prudence makes us do more work, which people prefer to avoid
[19], so we may find that participants prefer less work, but with
worse results Buçinca et al. [1]. This is a side effect of having people
cognitively engage with decisions; however, one that we may need
to accept if we want to truly improve AI-assisted decision support.
We conclude by repeating that the current paradigm of explain-
able AI as justified recommendations is ‘dead’. But the new para-
digm that includes hypothesis-driven explainability could take the
throne, so long live explainable AI!

ACKNOWLEDGMENTS
This research was partly funded by Australian Research Council
Discovery Grant DP190103414. Thanks to Liz Sonenberg, Piers
Howe, Eduardo Velloso, and Tim Schrills for valuable feedback on
drafts of this article.

---

<!-- PAGE 10 -->

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

REFERENCES
[1] Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z Gajos. 2021. To Trust
or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in
AI-assisted Decision-making. Proc. ACM Hum.-Comput. Interact. 5, CSCW1 (April
2021), 1–21. https://doi.org/10.1145/3449287

[2] Michael Chromik, Malin Eiband, Felicitas Buchner, Adrian Kruger, and Andreas
Butz. 2021.
I think I get your point, AI! the illusion of explanatory depth in
explainable AI. 26th International Conference on Intelligent User Interfaces (2021).
https://dl.acm.org/doi/abs/10.1145/3397481.3450644

[3] S Coderre, H Mandin, P H Harasym, and G H Fick. 2003. Diagnostic reasoning
strategies and diagnostic success. Medical education 37, 8 (Aug. 2003), 695–703.
https://doi.org/10.1046/j.1365-2923.2003.01577.x

[4] Jill L Drury, Gary L Klein, Lashon Booker, Kathy Ryall, and Samantha Dubrow.
2022. Reimagining Situation Awareness and Option Awareness for Human-
Machine Teaming. In 2022 IEEE Conference on Cognitive and Computational
Aspects of Situation Management (CogSIMA). 9–15.
https://doi.org/10.1109/
CogSIMA54611.2022.9830660

[5] Malin Eiband, Daniel Buschek, Alexander Kremer, and Heinrich Hussmann. 2019.
The Impact of Placebic Explanations on Trust in Intelligent Systems. In Extended
Abstracts of CHI. ACM, 1–6. https://doi.org/10.1145/3290607.3312787

[6] Krzysztof Z Gajos and Lena Mamykina. 2022. Do People Engage Cognitively
with AI? Impact of AI Assistance on Incidental Learning. In 27th International
Conference on Intelligent User Interfaces (Helsinki, Finland) (IUI ’22). ACM, New
York, NY, USA, 794–806. https://doi.org/10.1145/3490099.3511138

[7] Ben Green and Yiling Chen. 2019. Disparate Interactions: An Algorithm-in-the-
Loop Analysis of Fairness in Risk Assessments. In Proceedings of the Conference
on Fairness, Accountability, and Transparency (Atlanta, GA, USA). ACM, New
York, NY, USA, 90–99. https://doi.org/10.1145/3287560.3287563

[8] Ben Green and Yiling Chen. 2019. The Principles and Limits of Algorithm-in-
the-Loop Decision Making. Proc. ACM Hum.-Comput. Interact. 3, CSCW (Nov.
2019), 1–24. https://doi.org/10.1145/3359152

[9] David Gunning and David Aha. 2019. DARPA’s explainable artificial intelligence
(XAI) program. AI magazine 40, 2 (June 2019), 44–58. https://doi.org/10.1609/
aimag.v40i2.2850

[10] Robert R Hoffman. 2017. A taxonomy of emergent trusting in the human–machine
relationship. Cognitive systems engineering: The future for a changing world (2017),
137–164.

[11] Robert R Hoffman, Tim Miller, and William J Clancey. 2022. Psychology and AI at
a Crossroads: How Might Complex Systems Explain Themselves? The American
journal of psychology 135, 4 (2022), 365–378.

[12] Robert R Hoffman and Frank J Yates. 2005. Decision making [human-centered
computing]. IEEE intelligent systems 20, 4 (July 2005), 76–83. https://doi.org/10.
1109/MIS.2005.67

[13] Alon Jacovi, Ana Marasović, Tim Miller, and Yoav Goldberg. 2021. Formalizing
Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust
in AI. In Proceedings of the ACM Conference on Fairness, Accountability, and
Transparency. ACM, 624–635. https://doi.org/10.1145/3442188.3445923

[14] Daniel Kahneman. 2011. Thinking, Fast and Slow. Penguin UK.
[15] Harmanpreet Kaur, Eytan Adar, Eric Gilbert, and Cliff Lampe. 2022. Sensible
AI: Re-imagining Interpretability and Explainability using Sensemaking Theory.
(May 2022). arXiv:2205.05057 [cs.HC] http://arxiv.org/abs/2205.05057

[16] Gary Klein. 2015. A naturalistic decision making perspective on studying intuitive
decision making. Journal of applied research in memory and cognition 4, 3 (Sept.
2015), 164–168. https://doi.org/10.1016/j.jarmac.2015.07.001

[17] Gary Klein, Jennifer K Phillips, Erica L Rall, and Deborah A Peluso. 2007. A
data–frame theory of sensemaking. In Expertise out of context. Psychology Press,
118–160.

[18] Gary A Klein. 2017. Sources of Power: How People Make Decisions. MIT Press.
[19] Wouter Kool and Matthew Botvinick. 2018. Mental labour. Nature human
behaviour 2, 12 (Dec. 2018), 899–908. https://doi.org/10.1038/s41562-018-0401-9
[20] Kathryn Ann Lambe, Gary O’Reilly, Brendan D Kelly, and Sarah Curristan.
2016. Dual-process cognitive interventions to enhance diagnostic reason-
ing: a systematic review. BMJ quality & safety 25, 10 (Oct. 2016), 808–820.
https://doi.org/10.1136/bmjqs-2015-004417

[21] John D Lee and Katrina A See. 2004. Trust in automation: designing for appro-
priate reliance. Human factors 46, 1 (2004), 50–80. https://doi.org/10.1518/hfes.
46.1.50_30392

[22] Benedikt Leichtmann, Andreas Hinterreiter, Christina Humer, Marc Streit, and
Martina Mara. 2022. Explainable Artificial Intelligence improves human decision-
making: Results from a mushroom picking experiment at a public art festival.
(Sept. 2022). https://doi.org/10.31219/osf.io/68emr

[23] Prashan Madumal, Tim Miller, Liz Sonenberg, and Frank Vetere. 2020. Explainable
Reinforcement Learning through a Causal Lens. Proceedings of AAAI 34, 03 (April
2020), 2493–2500. https://doi.org/10.1609/aaai.v34i03.5631

[24] David Alvarez Melis, Harmanpreet Kaur, Hal Daumé, III, Hanna Wallach, and
Jennifer Wortman Vaughan. 2021. From Human Explanation to Model Inter-
pretability: A Framework Based on Weight of Evidence. In Proceedings of the

AAAI Conference on Human Computation and Crowdsourcing. 35–47. https:
//ojs.aaai.org/index.php/HCOMP/article/view/18938

[25] Hugo Mercier and Dan Sperber. 2017. The Enigma of Reason. Harvard University

Press.

[26] Tim Miller. 2019. Explanation in artificial intelligence: Insights from the social
sciences. Artificial intelligence (2019). https://www.sciencedirect.com/science/
article/pii/S0004370218305988

[27] Tim Miller. 2021. Contrastive explanation: A structural-model approach. Knowl-

edge Engineering Review 36 (2021), e14.

[28] Mahsan Nourani, Chiradeep Roy, Jeremy E Block, Donald R Honeycutt, Tahrima
Rahman, Eric Ragan, and Vibhav Gogate. 2021. Anchoring Bias Affects Mental
Model Formation and User Reliance in Explainable AI Systems. In 26th Interna-
tional Conference on Intelligent User Interfaces (IUI ’21). ACM, New York, NY, USA,
340–350. https://doi.org/10.1145/3397481.3450639

[29] Raja Parasuraman and Victor Riley. 1997. Humans and Automation: Use, Misuse,
Disuse, Abuse. Human factors 39, 2 (June 1997), 230–253. https://doi.org/10.
1518/001872097778543886

[30] Charles S Peirce. 2009. Writings of Charles S. Peirce: A Chronological Edition,

Volume 8: 1890–1892. Indiana University Press.

[31] Mark S Pfaff, Gary L Klein, Jill L Drury, Sung Pil Moon, Yikun Liu, and Steven O
Entezari. 2013. Supporting Complex Decision Making Through Option Awareness.
Journal of Cognitive Engineering and Decision Making 7, 2 (June 2013), 155–178.
https://doi.org/10.1177/1555343412455799

[32] Forough Poursabzi-Sangdeh, Daniel G Goldstein, Jake M Hofman, Jennifer Wort-
man Vaughan, and Hanna Wallach. 2021. Manipulating and Measuring Model
Interpretability. In Proceedings of the CHI 2021. ACM, New York, NY, USA, 1–52.
https://doi.org/10.1145/3411764.3445315

[33] Cynthia Rudin. 2019. Stop explaining black box machine learning models for
high stakes decisions and use interpretable models instead. Nature Machine
Intelligence 1, 5 (May 2019), 206–215. https://doi.org/10.1038/s42256-019-0048-x
[34] J W Rudolph. 2003. Into the big muddy and out again: Error persistence and crisis

management in the operating room. Ph. D. Dissertation.

[35] Christin Schulze and Ralph Hertwig. 2021. A description-experience gap in
statistical intuitions: Of smart babies, risk-savvy chimps, intuitive statisticians,
and stupid grown-ups. Cognition 210 (May 2021), 104580. https://doi.org/10.
1016/j.cognition.2020.104580

[36] Ben Shneiderman, Catherine Plaisant, Maxine S Cohen, Steven Jacobs, Niklas
Elmqvist, and Nicholas Diakopoulos. 2016. Designing the User Interface: Strategies
for Effective Human-Computer Interaction, 6th Edition. Pearson.

[37] Venkatesh Sivaraman, Leigh A Bukowski, Joel Levin, Jeremy M Kahn, and Adam
Perer. 2023. Ignore, Trust, or Negotiate: Understanding Clinician Acceptance
of AI-Based Treatment Recommendations in Health Care. In Proceedings of CHI.
https://arxiv.org/abs/2302.00096

[38] Frode Sørmo, Jörg Cassens, and Agnar Aamodt. 2005. Explanation in case-based
reasoning–perspectives and goals. Artificial intelligence review 24, 2 (Oct. 2005),
109–143. https://doi.org/10.1007/s10462-005-4607-7

[39] William R Swartout and Johanna D Moore. 1993. Explanation in Second Gen-
eration Expert Systems. In Second Generation Expert Systems. Springer Berlin
Heidelberg, 543–585. https://doi.org/10.1007/978-3-642-77927-5_24

[40] Richard Tomsett, Alun Preece, Dave Braines, Federico Cerutti, Supriyo
Chakraborty, Mani Srivastava, Gavin Pearson, and Lance Kaplan. 2020. Rapid
Trust Calibration through Interpretable and Uncertainty-Aware AI. Patterns (New
York, N.Y.) 1, 4 (July 2020), 100049. https://doi.org/10.1016/j.patter.2020.100049
[41] Jasper van der Waa, Elisabeth Nieuwburg, Anita Cremers, and Mark Neerincx.
2021. Evaluating XAI: A comparison of rule-based and example-based explana-
tions. Artificial intelligence 291 (Feb. 2021), 103404. https://doi.org/10.1016/j.
artint.2020.103404

[42] Q Vera Liao and Kush R Varshney. 2021. Human-Centered Explainable AI (XAI):
From Algorithms to User Experiences. (Oct. 2021). arXiv:2110.10790 [cs.AI]
http://arxiv.org/abs/2110.10790

[43] Mor Vered, Piers Howe, Tim Miller, Liz Sonenberg, and Eduardo Velloso. 2020.
Demand-Driven Transparency for Monitoring Intelligent Agents. IEEE Transac-
tions on Human-Machine Systems 50, 3 (June 2020), 264–275. https://doi.org/10.
1109/THMS.2020.2988859

[44] Danding Wang, Qian Yang, Ashraf Abdul, and Brian Y Lim. 2019. Designing
Theory-Driven User-Centric Explainable AI. In Proceedings of the CHI 2019 (CHI
’19, Paper 601). ACM, New York, NY, USA, 1–15. https://doi.org/10.1145/3290605.
3300831

[45] Frank J Yates and Georges A Potworowski. 2012. Evidence-Based Decision Man-
agement. Oxford University Press, 198—-222. https://doi.org/10.1093/oxfordhb/
9780199763986.013.0012

[46] Yunfeng Zhang, Q Vera Liao, and Rachel K E Bellamy. 2020. Effect of confidence
and explanation on accuracy and trust calibration in AI-assisted decision making.
In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency
(Barcelona, Spain). ACM, New York, NY, USA, 295–305. https://doi.org/10.1145/
3351095.3372852

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Explainable AI is Dead, Long Live Explainable AI!
Hypothesis-driven Decision Support using Evaluative AI

Tim Miller
tmiller@unimelb.edu.au
The University of Melbourne
Melbourne, VIC, Australia

ABSTRACT
In this paper, we argue for a paradigm shift from the current model
of explainable artificial intelligence (XAI), which may be counter-
productive to better human decision making. In early decision
support systems, we assumed that we could give people recommen-
dations and that they would consider them, and then follow them
when required. However, research found that people often ignore
recommendations because they do not trust them; or perhaps even
worse, people follow them blindly, even when the recommenda-
tions are wrong. Explainable artificial intelligence mitigates this by
helping people to understand how and why models give certain rec-
ommendations. However, recent research shows that people do not
always engage with explainability tools enough to help improve
decision making. The assumption that people will engage with
recommendations and explanations has proven to be unfounded.
We argue this is because we have failed to account for two things.
First, recommendations (and their explanations) take control from
human decision makers, limiting their agency. Second, giving rec-
ommendations and explanations does not align with the cognitive
processes employed by people making decisions. This position pa-
per proposes a new conceptual framework called Evaluative AI
for explainable decision support. This is a machine-in-the-loop par-
adigm in which decision support tools provide evidence for and
against decisions made by people, rather than provide recommenda-
tions to accept or reject. We argue that this mitigates issues of over-
and under-reliance on decision support tools, and better leverages
human expertise in decision making.

CCS CONCEPTS
• Computing methodologies → Artificial intelligence; • Human-
centered computing → HCI theory, concepts and models.

ACM Reference Format:
Tim Miller. 2023. Explainable AI is Dead, Long Live Explainable AI!: Hypothesis-
driven Decision Support using Evaluative AI. In 2023 ACM Conference on
Fairness, Accountability, and Transparency (FAccT ’23), June 12–15, 2023,
Chicago, IL, USA. ACM, New York, NY, USA, 10 pages. https://doi.org/10.
1145/3593013.3594001

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
FAccT ’23, June 12–15, 2023, Chicago, IL, USA
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0192-4/23/06. . . $15.00
https://doi.org/10.1145/3593013.3594001

1 INTRODUCTION
Imagine you have two friends, Bluster and Prudence1. Whenever
you have a difficult decision to make, you can approach them for
help. Both have shown excellent judgement on complex decisions
in the past. Bluster always tells you what they think is the right
decision, even when they are not confident, and then tells you
why they think that. But Bluster does not consider what you think.
Would that be helpful? If your decision and reasons were the same
as Bluster’s, it would give you confidence. If not, Bluster could
change your mind to an answer that you were happier with or that
resulted in better outcomes. Prudence, in contrast, hardly ever gives
their opinion, especially when not confident. Prudence instead asks
you what you are proposing and then provides feedback: evidence
for and against your proposed decision. If you propose alternatives,
Prudence provides feedback on these, giving feedback until you
reach a decision. But Prudence never gives you an answer. Would
this be helpful? Prudence helps you to form a decision, and provides
feedback on your own options, rather than justifying their own
opinion. This would help you to question your decisions, and would
give you control over which options you receive feedback for.

Reader, which would you prefer? An informal survey conducted
by the author during a recent talk showed that just three out of over
100 people preferred Bluster; the remaining 100+ people preferring
Prudence. Prudence helps us find strengths and weaknesses in
our thinking and gives us control over which options we discuss
with them. The ability to assess the strengths and weaknesses of
judgements and decisions is key to expert decision making [18, 20].
Despite this preference, the current model of (explainable) AI-
assisted decision support gives us Bluster instead of Prudence, right?
AI decision aids are designed to tell the user what they think the
best answer is (e.g. a recommendation), and explain why that is
considered the best answer. This is a ‘recommend and defend’2
approach. If the user disagrees or does not find the reasons convinc-
ing, the machine offers little else. A counterfactual explanation [27]
allows us to ask why another option is not the best answer; but does
not provide us with reasons the alternative may well be the right
answer or a good answer. ‘Recommend and defend’ approaches,
which we call recommendation-driven decision support, do little
to help us critique its answers or our own ideas.

The Bluster model of recommendation-driven decision support
leads to two problems. First, AI tools are not correct all of the time,
so we should be sceptical at least some of the time. However, people
find it difficult to correctly calibrate their trust in a decision aid [10,
13, 21, 37]. Research shows that people tend to either under-rely on

1Thanks to Piers Howe for these names.
2Sean Koon introduced this nice term to me.

333FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

but that the evaluative AI paradigm is still a form of explainable
AI, and many of the current paradigm will play a part in this new
conceptualisation; so, long live explainable AI!

Section 2 reviews related work on cognitive decision making,
what makes a good decisions, and the main modes of explainable AI.
Section 3 evaluates how current decision support models align with
human decision making processes, with a focus on explainable and
interpretable AI. Section 4 presents evaluative AI, a new conceptual
framework for human-centred decision making, and argues that
this framework aligns better the cognitive processes humans use
for decision making. It also presents a high-level research agenda
for evaluative AI. Section 5 concludes the paper.

2 AI-ASSISTED DECISION SUPPORT
2.1 Decision making and decision support
Before we consider what makes good decision support, we consider
what good decision making is. A definition of ‘decision making’ is
surprisingly elusive. Often, definitions consider three steps [12]: (1)
an assessment of the situation, such as what options are available;
(2) making judgements and trade-off about options; and (3) selecting
an option or committing to a course of action. Hoffman and Yates
[12] argue that this ‘final-point notion’, in which there is a point
that decision “made” is a (sometimes useful) simplification of the
decision-making process. However, as a model, it misses some
important aspects of decision support; importantly: that decision
making is a process, not a point in time.

Table 1 outlines 10 cardinal decision issues, defined by Yates and
Potworowski [45]. These include issues such as deriving options
and making judgements, but also factors such as exploring conse-
quences of actions, and who will be part of deciding. The issues
in italics are the aspects that we believe to be of most importance
to AI-assisted decision support. While the first three and the final
issue can be supported, these are less relevant for AI research.

We define a decision aid (DA) as any system that supports the
process of deciding. But what is a good DA? In Table 2, we propose
six criteria for good decision support. The first five are based on
the 10 cardinal issues from Table 1 [12, 45]. The criteria that are
omitted can certainly be supported by a DA, but these criteria are
decisions in their own right, and therefore the six criteria apply to
each. The sixth criteria is understandable, which simply means that
a good DA helps people understand how and why it works, and
where it fails. This is a common criteria for AI-based DAs [9], and
is important to calibrate trust & reliance, and to find mistakes.

Note two things about the criteria in Table 2. First, a DA helps
a decision maker. It does not necessarily provide the answers for
any of the criteria. Second, it goes beyond recommendations and
judgements, which are typically the focus in XAI; largely because
these are considered to be some of the harder problems.

2.2 Cognitive processes for decision making
Hoffman et al. [11] argue that, when a person tried to understand a
system output, they engage in the cognitive process known as ab-
ductive reasoning. Abductive reasoning is the process of forming
hypotheses and judging their likelihood for the purpose of explain-
ing observations or facts [30]. This abductive process is engaged
as soon as people start interacting with a system, irrelevant of any

Figure 1: Contrastive explanation vs. Evaluative AI. Con-
trastive paradigms are ‘recommend and defend’ approaches.
They provide evidence that supports the recommendation
and refutes all others. Evaluative AI proposes not necessarily
giving recommendations from machines, but instead provid-
ing evidence for/against each option.

tools, meaning they have no effect on decision making, or they over-
rely on tools [1, 6, 37], likely because providing recommendations
makes them fixate on that recommendation. Both under- and over-
reliance have negative consequences [29]. Second, Bluster reduces
our locus of control [36], because we cannot control which options
we received feedback for.

This paper argues for a paradigm shift: that the decision aids
(DAs) should be less like Bluster, and more like Prudence, which
we call hypothesis-driven decision support, . We propose a new
conceptual framework for decision support, with two key properties
not present in the current paradigm. First, evaluative AI tools do
not provide recommendations. They mitigate fixation by either
allowing the decision maker to determine which options are best or
helping them to narrow down to a manageable set of options [34].
Second, instead of justifying AI recommendations, DAs generate
and present evidence to support or refute human judgements, and
explain trade-offs between any set of options, not just the machine
recommendation. This helps with trust calibration because the
machine does not give recommendations, as well as over/under-
reliance because there is no recommendation to follow. We argue
that the reason this Prudence-like approach is more effective for
decision support because it aligns with the cognitive decision-
making process that people use when making judgements
and decisions [11, 17, 30]. We call this paradigm evaluative AI.
Figure 1 shows the difference between evaluative AI and perhaps
the most common form of explainability: contrastive explanation.
Contrastive explanation is like Bluster — it gives us an answer and
justifies it, telling us why it is correct and why other options are
not. Evaluative AI is like Prudence — it helps us critique our own
ideas. This provides a better feedback loop – if the evidence helps
use eliminate our preferred hypothesis, we start to explore others.
Evaluative AI is not intended to be used in all scenarios. It is
more suitable for medium- and high-stakes decisions when the de-
cision maker is ultimately accountable, and low frequency decision
making where the decision maker has time to explore options.

We conclude that for decision making, the recommendation-
driven paradigm of explainable AI is ‘dead’ (for some situations),

334Explainable AI is Dead, Long Live Explainable AI!

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Table 1: The 10 ‘cardinal decision issues’ outlined by Yates
and Potworowski [45]. The issues in italics represent those
that are of most interest to explainable AI.

Cardinal issue Definition

Need

Mode

Investment

Options

Possibilities

Judgement

Value

Trade-offs

Acceptability

Why do we need to make a decision at all?

Who will decide and how will they do it?

What kinds of amounts of resources will be
invested in the process?

What are the different actions we could take
to solve the need?

What outcomes could happen if for each ac-
tion, if it were taken?

Which of the outcomes would happen if we
took the action?

How much would any stakeholder care if this
outcome happened?

How do we trade-off the outcomes to settle
on an action?

How can we get other stakeholders to accept
our decision?

Implementation Now we have decided, how can we action it?

Table 2: Criteria for good decision support, based on the 10
‘cardinal decision issues’ [45]

Criteria

Options

Possibilities

Definition

Help to identify options, as well as help to
narrow down the list of feasible or realistic
options

Help to to identify possible outcomes for each
of the identified options

Judgement

Help to judge which outcomes are most likely

Value

Trade-offs

Help to identify the positive and negative im-
pacts on stakeholders for each of the identi-
fied options

Help to make trade-offs on the above criteria
for each options

Understandable Help to understand how and why the tools

works as it does, and when it fails

particular explainability or interpretability tools. As such, Hoff-
man et al. argue that abductive reasoning is a suitable foundational
model for conceptualising explainable AI.

Peirce [30] defines the process of abductive reasoning as five

step process, outlined in Figure 23:

(1) Observe an event or phenomenon: A person observes an event,
usually one that is surprising and does not fit their current

3The final step of extending the explanation is omitted because it simply repeats the
process when new events are observed.

Figure 2: A model of abductive reasoning. When someone
observes an event, they generate hypotheses of the cause,
and then judge the plausibility of (some) hypotheses; poten-
tially iterating to generate more hypotheses as new evidence
emerges. Eventually, the understanding is resolved.

mental model. This leads to them to start searching for ex-
planatory hypotheses.

(2) Generate hypotheses: The person generates potential reasons
for why they would have observed the event or phenomenon.
The reasons are hypotheses.

(3) Judge the plausibility of the hypotheses: The person searches
for evidence that may support or undermine different hy-
potheses, perhaps ruling out some or making some more
likely. Some hypotheses are ruled out, while others are judged
as more likely. This process may lead to new hypotheses.
(4) Resolve understanding: A particular hypothesis fits the new
observation and previous experience of the decision maker,
so is adopted as the most likely cause of the observation.
This may be a tentative resolution.

(5) Extend: Revise and extend the process when new evidence

is observed or considered.

This philosophical model of decision making is supported by
research from cognitive science. Klein et al. [17] present a theory
of sensemaking known as the Data/Frame Theory, built from stud-
ies with expert decision makers. The frame, a generalisation of a
hypothesis, is a model of how something works, while the data
contains observations made and inferences that combine the obser-
vations and the frame. The data is used to adjust the frame (similar
to judging plausibility) and the frame is used to determine what new
data to find, what outcomes to evaluate, and how these relate. Klein
et al. show that people make decisions by first using their intuition
to narrow down to a set of likely options (the frames), and then go-
ing through each option one-by-one, searching for evidence (data)
to make judgements. Good decision makers search for evidence
that both supports and refutes a hypothesis. Klein et al. [17] argue
that abductive reasoning plays a central role in this process. We
build the evaluative AI framework around the Data/Frame model.
Hoffman et al. [11] argue that abductive reasoning is a suitable
foundation for conceptualising explainable AI. In this paper, we
argue for a similar — yet orthogonal — view; specifically, explain-
able AI for decision making. In decision making, the decision
maker is involved in two (related) reasoning processes. First,
the decision maker is trying to make a judgement/decision about
the world (e.g. a diagnosis). The observed event is something that
needs explaining, such as a medical symptom, the hypotheses are
the potential causes of that observation, such as a disease, and
the judgement is about the likelihood of a particular hypotheses
being true given the evidence. Second, the decision maker is also

335FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

making a judgement about the DA (e.g. whether its reasoning is
sound, as proposed by Hoffman et al. [11]). The observed event is
an output 𝑜 of an AI system 𝑓 given an input 𝑖. The hypotheses char-
acterise which combinations of inputs 𝑖 and computations (parts
of 𝑓 ) caused this output to occur. The process of judgement is to
determine why the system produced the output that it did. Table 3
outlines this for a medical diagnosis scenario. Decision makers need
to ‘invert’ the explainable AI process to align with the decision-
making process. Hoffman et al. argue that machines reasoning in
an abductive manner align better with this process. The argument
in this paper is similar, but rather than necessarily giving abductive
explanations, we argue that DAs should be designed to explicitly
support abductive reasoning.

Table 3: How Explainable AI and Evaluative AI align against
the human abductive reasoning process.

Human
Reasoning

Explainable AI Evaluative AI

Event to explain AI diagnosis

Medical symptoms

Hypotheses

AI reasoning

Medical conditions

Evidence

Judgement

Models,
Explainability

Evidence for/against
hypotheses

Causes between
inputs & AI
diagnosis

Likelihood of
medical conditions

2.3 Explainable AI and decision making
The initial assumption of AI-assisted DAs was that people would
follow recommendations when required, leading to better deci-
sions. However, issues such as warranted and unwarranted distrust
[13] mean that AI systems are often deployed and then largely
ignored [9, 37]. Explainable/interpretable AI aims to mitigate these
by helping people to understand why decisions are made. How-
ever, recent research has shown that the recommendation-driven
explainable/interpretable AI has little effect on decision making
[1, 6–8, 28, 32], although this is not always the case [22, 23, 41].
The two primary issues are over-reliance and under-reliance. Over-
reliance means decision makers accept a machine recommendations
even when it is wrong, caused by unwarranted trust [13]. This is
often attributed to automation bias, where the machine is “must
be right” because it is a machine. Under-reliance means decision
makers reject a machine recommendation even when it is correct,
caused by unwarranted distrust [13]. This is often attributed to
algorithmic aversion, where machine outputs are rejected but would
be accepted had they come from a human. In either case, a poor
decision can often be attributed to fixation [17] — searching for
evidence to support one hypothesis without considering others.

Some experimental studies [2, 5, 42] indicate that most partici-
pants do not cognitively engage with explainability tools. Partic-
ipants who do seem to believe that they understand explanatory
information, leading to over-confidence [2], even when presented
with explanations that contain no useful information [5]. We have
seen this in currently unpublished observational studies. In a study

where expert board gamers used an AI-based recommendation
system, we saw that many players did not truly engage with recom-
mendations or explanatory information either. When they did, we
saw some behavioural changes, but not enough to see a statistically
significant improvement in decision making.

Similarly, in experiments on a general task with general partic-
ipants, Buçinca et al. [1] and Gajos and Mamykina [6] show that
explainability did not mitigate over-reliance, and in some cases it
increased over-reliance. They assert that this is because participants
did not pay attention to explainability information. They propose
three cognitive forcing strategies to mitigate over-reliance, such as
forcing people to give a decision before seeing a recommendation.
Their results showed that cognitive forcing slightly mitigated over-
reliance, compared to feature-based and uncertainty judgements,
particularly disregarding incorrect AI recommendations, but with
no statistically significant differences in task performance. Interest-
ingly, despite cognitive forcing functions being more effective, they
were least preferred by participants. Buçinca et al. [1] attribute this
to the phenomenon of people not wanting to exert mental energy
[19]. This indicates that Evaluative AI could prove useful by not
fixating people on particular recommendations, but allowing peo-
ple to assess whether evidence supports their hypotheses, rather
than trying to understand the DA’s reasoning.

These studies show that the recommendation-driven XAI does
little to mitigate over- and under-reliance. This has lead to several
authors to argue that XAI research should return to the founda-
tion of cognitive and social processes involved in decision making
[7, 8, 15, 42, 44]. Some authors [1, 6, 42] have attributed the cause
of ignoring explanatory information to the ‘failure’ of system 1
processing in dual process theory [14]. In brief, the theory is that
system 1 thinking (fast, heuristic, and biased) ‘interferes’ with sys-
tem 2 thinking (slow and more accurate). The conclusion that is
often, but not always drawn, is that DAs should aim to support
system 2 thinking and prevent system 1 ‘interference’.

However, we caution against the idea of prioritising sys-
tem 2 thinking over system 1 thinking, for three reasons. First,
research in Naturalistic Decision Making (NDM) demonstrates
that ‘system 1’ thinking, which they call intuition, is a power-
ful source of problem solving that often produces better and/or
faster decisions than system 2 [16]. For example, Coderre et al.
[3] found that intuition significantly outperformed hypothetico-
deductive reasoning in gastroenterology clinical diagnoses. Klein
[18] show that experts make decisions by first using their intu-
itive problem solving ability to generate likely options, and then
using both intuition and slower structured thinking to assess which
options will work. As such, any technique that aims to ‘override’
intuitive thinking risks losing the benefits of expertise and prior
knowledge. Second, there is now sufficient research questioning
whether the system 1 vs system 2 distinction is so clear [25, 35].
For example, many experiments showing biases system 1 thinking,
such as base-rate fallacies, could be partly attributed to the experi-
ment design [35], which may not reflect many environments where
real decisions are made. Finally, we need further research using
expert decisions makers, rather than just general participants, as
well as studies where poor decisions have real consequences. The
effect of system 1 thinking may differ between contexts such as
the experience of the decision maker and the stakes of the decision.

336Explainable AI is Dead, Long Live Explainable AI!

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

In short, we argue against simply treating intuition as ‘bad’. DAs
should exploit the strengths of intuition and expertise, as well as
structured thinking.

3 (EXPLAINABLE) AI AS DECISION SUPPORT
This section provides a narrative of how we have arrived at the
current status quo. We evaluate the four dominant paradigms of
decision support against the criteria of decision support identified in
Table 2. The four paradigms we discuss are: (1) recommendations; (2)
recommendations with explanatory information; (3) interpretable
models; and (4) cognitive forcing.

3.1 Giving recommendations with no

explanatory information

The idea of decision support using AI came from the use of AI
as automation. Given situations in which an AI model provides
more accurate judgements/decisions than human decision makers,
a simple of model of AI-assisted DAs is to give recommendations,
which decision makers can then take into account. Recommenda-
tions can be ranked lists of options such as in many recommender
systems, but the typical model is to propose just the one recom-
mendation that the AI model determines is the most likely or ‘best’.
The assumption here is that for situations in which DAs can handle
many more factors simultaneously, it can provide insight when the
assumptions of the underlying modelling theory hold. This model
is depicted below in Figure 3.

Figure 3: A model of giving recommendations for decision
support. This assumes that decision makers will carefully
consider recommendations. However, empirical evidence
suggests this is not the case.

The primary issue with this model was that, even if the DA
gives better judgements/decisions than the human, people tend
to ignore this due to unwarranted distrust [9, 10, 13, 26, 37, 39] or
accept wrong decisions due to unwarranted trust [1, 6, 29]. The
inability to scrutinise why decisions are made mean that the only
information to rely upon to judge the correctness is: (1) extrinsic
information such as accuracy measures; and (2) the decision makers’
own expertise and knowledge. Given the former does not change
from decision to decision, it is unsurprising that experts rely on
their own expertise and novices over-rely on the tool [37].

Comparing this to the properties that comprise good decision
support outlined in Table 2, we can see why this approach is largely
inneffective. Giving only recommendations:

(1) does not help to provide new options or to filter out unlikely

options;

(2) does not consider possibilities or judgements beyond one

option;

(3) does not help determine stakeholder values;

(4) does not support making trade-offs; and
(5) does not provide understanding of the machine decision.

Can this still be useful? Of course! If a recommendation matches
or is similar to our own judgement, it gives us confidence in our
own decision, although this confidence may be misplaced. Further,
if a recommendation is not similar to our own judgement, it may
decrease our confidence and make us reconsider, potentially helping
us to make a better decision. However, in either case, we receive
no further support to help with the decision.

3.2 Giving recommendations with explanatory

information

One solution to mis-calibrated trust is to provide explanatory infor-
mation. This means giving justifications for decisions, providing
evidence to support the decisions, and making models simple and
easy to understand (see more on this in Section 3.3). A model of
interaction between decision maker and DA is shown in Figure 4.
Comparing this to the properties that comprise good decision
support outlined in Table 2, we can see the criteria that the default
model of XAI bring are that it:

(1) does not help to provide new options or to filter out unlikely

options;

(2) partially considers possibilities or judgements beyond one
option: contrastive explanations argue why other options
are NOT recommended;

(3) does not help determine stakeholder values;
(4) partially supports making trade-offs; and
(5) does provide understanding of the machine decision.

So, explainability provides understanding. Contrastive explana-
tions [27] partially support trade-offs when they answer ‘Why 𝐴
instead of 𝐵?’, where 𝐴 is the output and 𝐵 a foil. However, this still
defends the recommendation. Can this be useful? Of course! If we
agree with the recommendation, we can check that we agree for
similar reasons; and if we disagree, we can check the reasons why,
potentially helping us to improve our initial decision.

3.3 Giving recommendations with an

interpretable model

The third paradigm is to give recommendations using an ‘inter-
pretable’ model. Rudin [33] argues that for high-stakes decisions,
people should avoid using black-box models altogether, and instead
should use interpretable models. Interpretable models use a small
set of features with a low complexity of interaction between them.
The model of interaction with an interpretable model is same as
for recommendations with explanatory information, outlined in Fig-
ure 4. The assumption is that because the model is interpretable, it
contains most of the explanatory information that is required. How-
ever, interpretable models are not designed with decision support in
mind. The model’s options, possibilities, and trade-offs would have
to be calculated by the decision maker. Assistance to calculate these
is a combination of interpretability and explainability, so overlaps
with the previous section. Effectively, the purpose of interpretable
models is complementary to the criteria in Table 2.

337FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

Figure 4: A model of explainable AI for decision support. This assumes that the problem of distrust can be mitigates by
giving reasons or explanations for decisions. However, empirical evidence suggests people do not pay careful attention to the
reasons/explanations.

Comparing this to the properties that comprise good decision
support outlined in Table 2, we can see the criteria that the inter-
pretability brings are that it:

(1) does not help to provide new options or to filter out unlikely

options;

(2) does not consider possibilities or judgements beyond one

option;

(3) does not help determine stakeholder values;
(4) does not support making trade-offs; and
(5) does provide understanding of the machine decision.

3.4 Cognitive forcing
The final paradigm is cognitive forcing. The assumption of cog-
nitive forcing is that forcing people to engage with the decision
cognitively can mitigate over-reliance. Gajos and Mamykina [6]
and Buçinca et al. [1] implement this idea using three approaches,
as outlined in Section 2.3. The commonality between these three
approaches is that decisions are initially withheld from the deci-
sion maker, but explanatory information is provided, forcing the
decision maker to engage with the explanatory information. This
model is depicted below in Figure 5. Withholding recommenda-
tions ‘forces’ the decision maker to cognitively engage with the
decision and therefore, to consider different options and make trade-
offs. Giving explanatory information from the start may help the
decision maker to focus on useful information.

Comparing this to the properties that comprise good decision
support outlined in Table 2, we can see the criteria that cognitive
forcing brings are that it:

(1) partially helps to provide new options or to filter out un-

likely options by forcing the decision maker to do so;
(2) does not consider possibilities or judgements beyond one

option;

(3) does not help determine stakeholder values;
(4) partially supports making trade-offs; and
(5) does provide understanding of the machine decision.

While this is an improvement beyond the default XAI approaches,
weaknesses remain. First, this approach is still an instance of our
friend Bluster, rather than our friend Prudence – it is just that
Bluster pauses before stating their opinion. Second, it does not
provide helpful decision-making information for options other than
the recommendation.

Next, we propose a model that builds on the strength of cognitive
forcing, but on a foundation of the cognitive science of decision
making.

4 EVALUATIVE AI: A CONCEPTUAL

FRAMEWORK OF EXPLAINABLE DECISION
SUPPORT

In this section, we present a new conceptual framework of hypothesis-
driven explainable decision support called evaluative AI. The two
primary design criteria for this are:

(1) Support the properties of good decision making outlined in
Section 2.3. That is, support the decision maker’s cognitive
decision making process.

(2) Provide better internal locus of control [36] to the decision

maker about which options to explore and when.

To do this, we propose that the vision of evaluative AI is to:

Support the decision maker to access the infor-
mation they want and need to evaluate a hypoth-
esis, when they want it.

4.1 Conceptual framework
The conceptual framework for evaluative AI is shown in Figure 6.
Evaluative AI does not (necessarily) provide recommendations, but
instead offers support to filter out unlikely options, generate new
hypotheses, or both. The decision maker then analyses a hypothesis,
asking the DA to provide evidence for and against the hypothesis.
Evidence could also be presented contrastively: what is the evi-
dence for/against a particular hypothesis rather than some other
hypothesis. Importantly, the decision maker to maintains control
over which hypotheses to explore.

4.1.1 Options. Existing explainable AI approaches tend to pro-
vide one or sometimes two options to consider. The evaluative AI
paradigm argues that the presentation of options should be context-
specific. For example, given a probabilistic classifier, a evaluative
AI system could highlight options that are within a certain prob-
ability of the most likely, perhaps withholding the probabilities
themselves. Alternatively, it could use uncertainty estimates, which
are known to help decision making [40], and from that, determine
which options to filter. Approaches such as this help to reduce fixa-
tion because there is no single recommendation. Cognitive forcing
takes a similar approach, but current cognitive forcing techniques
are recommendation-driven [1, 6].

Judgement support. All five paradigms support judgements.
4.1.2
The evaluative AI framework puts the human at the centre of the
judgement process. In this framework, the judgement is made by
the human decision maker with support from the DA, which gives
feedback (evidence for/against) of proposed hypotheses. This is

338Explainable AI is Dead, Long Live Explainable AI!

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Figure 5: A model of cognitive forcing. By withholding recommendations (for perhaps a short period) and giving an ‘explanation’,
it forces people to engage, limiting over-reliance. However, it is still a ‘recommend and defend’ approach.

to support human decision makers. However, research into machine-
assisted option awareness is still in its infancy.

4.2 Example: Diagnosis
Consider an example of a DA for diagnosing skin cancers, such as
the ISIC 2018 lesion diagnosis challenge4. There are seven possible
disease categories: (1) melanoma; (2) melanocytic nevus; (3) basal
cell carcinoma; (4) actinic keratosis; (5) benign keratosis; (6) der-
matofibroma; and (7) vascular lesion. Given a dermoscopic image
of a legion along with some meta information, such as where the
lesion is found, the task is to diagnose the most likely category.

Figure 7 shows a simple prototype interface for such a system.
In this case, there are seven hypotheses/diagnoses. The DA filters
out those that are unlikely, leaving just three: melanoma, basal
cell carcinoma (BCC), or actinic keratsosis (AK)5, highlighted with
bold text. By highlighting only likely hypothesis instead of just one,
this could help to mitigate fixation on just one option. Hypotheses
can be explored. In Figure 7, the location of the lesion, its colour,
scarring, and that it sometimes bleeds, is strong support for a BCC
diagnosis. However, the asymmetric shape, itchiness, and recent
colour change are evidence against BCC. Other forms of evidence
could be provided to the decision maker, such as finding similar
instances using case-based reasoning [38, 44]. It is up to the de-
cision maker to make the final decision, integrating their expert
knowledge and the information from the DA.

4.3 Summary
Comparing model to the properties that comprise good decision
support outlined in Table 2, we can see the criteria that evaluative
AI brings are that it:

(1) does help to provide new options or to filter out unlikely

options by forcing the decision maker to do so;

(2) does help to identify possibilities and support judgement

for options;

(3) does not help determine stakeholder values;
(4) does support making trade-offs; and
(5) does provide understanding of the machine decision.

Table 4 compares the five approaches to explainable DAs. Evalu-
ative AI explicitly aims to provide support for options, judgement,
understanding, and trade-offs. The difference between cognitive
forcing and evaluative AI is two-fold:

(1) Cognitive processes: Evaluative AI is built on the Data/Frame
model of sensemaking [17], so supports the decision maker’s
cognitive process by allowing them to explore hypotheses,

4See https://challenge.isic-archive.com/landing/2018/47/.
5It is unlikely that these three would be the case as AK is quite different from BCC
and melanoma, but this makes for a good illustrative example.

Figure 6: A model of Evaluative AI, which aligns with decision
making processes, keeping the decision maker in control and
asking users to rely on evidence instead of recommendations.

supporting judgement, rather than giving judgement. The dif-
ference is who owns control over which hypotheses to explore. In
a recommendation-driven approach, both the human and machine
provide a judgement. In the evaluative AI paradigm, the human
provides judgement and the machine provides feedback.

4.1.3 Trade-off support. Contrastive explanations trade-off out-
comes. However, they explain only why non-recommended options
are ‘incorrect’. This is a ‘persuasive’ approach — it justifies why the
machine’s decision is correct. The evaluative AI framework instead:

(1) explains trade-offs between any two sets of options; and
(2) provides evidence both for and against each option, irrele-

vant of the judged likelihood of that option.

Good decision makers assess an option by looking for evidence
that supports it, but also evidence that refutes it. For example, in
a study with anaesthesiology residents, Rudolph [34] showed that
participants who fixated on an initial option did poorly, but that
participants who kept an open mind on all options do not per-
form much better. Instead, those who jump to an initial conclusion
and test it, looking for negative evidence, make the best decisions.
Recommendation-driven approaches typically do not provide evi-
dence against the recommendation, nor evidence supporting other
options. Evaluative AI supports both, rather than aiming to per-
suade that the machine is correct.

Supporting trade-offs has gained interest in recent years under
the name option awareness — the analysis and understanding of
various options and their relative trade-offs [31]. Pfaff et al. [31]
show that using visual analytics to allow decision makers to explore
options increases their option awareness, resulting in more accurate
and faster decisions. More recently, Drury et al. [4] proposed a
framework in which machines consider their own option awareness

339FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

Figure 7: A simple prototype of a diagnostic interface using evaluative AI

Table 4: A summary of the decision support provided by different paradigms. 1/𝑛means that this only provides information to
confirm the recommended option(s); ✔/✘means partial support for other options. Evaluative AI explicitly provides support
to explore options and perform trade-offs. XAI and cognitive forcing allow this if they support contrastive explanation. In
evaluative AI, it should be default.

Support provided

Decision support Options Possibilities

Judgement Value Trade-offs Understandable

Recommendation
XAI
Interpretability
Cognitive forcing
Evaluative AI

✘
✘
✘
✔/✘
✔

1/𝑛
1/𝑛
✘
1/𝑛
✔

1/𝑛
1/𝑛
✘
1/𝑛
✔

✘
✘
✘
✘
✘

✘
✔/✘
✘
✔/✘
✔

✘
✔
✔
✔
✔

rather than providing only the information to the justifies a
machine recommendation.

(2) Control: Evaluative AI explicitly hands control of which
hypotheses are investigated and prioritised to the decision
maker, resulting a machine-in-the-loop paradigm [7, 8],
rather than a human-in-the-loop paradigm.

For this reason, we assert that evaluative AI obtains the benefits
of cognitive forcing, while giving control to the decision maker to
explore the strengths and weaknesses of any option, rather than just
the strengths recommendations and the weaknesses of alternatives.

4.4 Long live explainable AI!
This article proposes a paradigm shift from recommendation-driven
decision support to hypothesis-driven decision support. Does this
imply that explainable AI is dead? We do not believe so.

First, there are applications of XAI beyond decision support,
such as verification, regulation, scientific discovery, generating
insights about underlying data, etc. Further, there are applications
where recommendation-driven approaches may be the best way to
improve decisions, such as making decisions at scale.

Second, for a machine to judge decisions, we will need an un-
derlying decision-making model, meaning that recommendation
approaches such as machine learning, planning, and optimisation
will be required, along with XAI techniques.

Third, evaluative AI is explainable AI. The cognitive and so-
cial aspects of good explainability apply to evaluative AI: [26]: (1)
explanations are contrastive; (2) explanations are selected; (3) ex-
planations are interactive; and (4) explanations are causal.

Fourth, from the earlier example, it is clear that many existing
tools will play a part in evaluative AI: constrastive explanation [27],
Weights of Evidence (WoE) [24], feature importance, case-based
reasoning techniques [38], etc., all generate evidence. New models
of XAI are needed, but existing work lays a solid foundation.

4.5 Challenges and Limitations
There are clear potential limitations with this approach. First, if
people tend to dismiss recommendations and any explainability
information, why would they pay attention to evidence? The eval-
uative AI framework makes the same assumptions as earlier work:
that people care at all about what a machine has to say. A very real

340Explainable AI is Dead, Long Live Explainable AI!

FAccT ’23, June 12–15, 2023, Chicago, IL, USA

risk is that decision makers will not engage with a tool that sup-
ports cognitive reasoning either. However, one argument against
this is that this evaluative AI provides decision makers with better
control [36, 43], and follows a process that they will naturally
follow, rather than recommendation-driven approaches, which
somewhat disrupt the decision-making process.

Second, it is difficult to imagine evaluative AI solutions will result
in lower cognitive load. A strength of the recommendation-driven
approaches is that they reduce the information that a decision maker
needs to consider to just the most relevant. Evaluative AI will likely
result in designs that force more engagement with the decision, but
less preferred by decision makers [1]. However, following a model
of abductive reasoning can still reduce information compared to
having no decision support; e.g. presenting only the most likely
hypotheses; prioritising access to the most important information,
etc. Striking this balance is a challenge.

4.6 An incomplete research agenda
In this section, we present an incomplete research agenda based
around the evaluative AI framework.

4.6.1 Observing events. The first step is observing an event. While
it is difficult to control the attention a decision maker pays to
information, we can support this in several ways:

(1) Design interfaces to make it clear what has happened,
what data is being used, etc. [11]. This includes allowing
people to explore relevant attributes of a system.

(2) Highlight anomalous behaviour/events, as these are typ-
ically the events that people require to make decisions or to
understand [26].

4.6.2 Generating options. The ability for the machine to put for-
ward options can help decision makers in two ways. First, it can
present options that decision makers did not consider. Second, it
can speed up decision making in time-sensitive environments by
filtering out some options and/or allowing options to be assessed
more systematically.

Generating options can be supported in several ways beyond

providing 1-2 recommendations or a ranking:

(1) Provide probabilities over options: This can help the
decision maker to narrow down likely options, but is perhaps
subject to over-fixation (on the most likely option) in the
same way that recommendations are.

(2) Provide a set of likely options: This can help to narrow
down the set of hypothesis without giving a recommenda-
tion, as in the example in Section 4.2, reducing fixation.
(3) Provide uncertainty measures: The DA provides its uncer-
tainty about its filtered options (a decision of set of decisions)
to encourage healthy scepticism [46].

(4) Intervention: The DA does not initially narrow down op-
tions, but allows the decision maker to explore and select
their answer, and then intervenes if it disagrees above some
threshold, prompting the decision maker to consider the
DA’s most likely responses.

(5) Relate inputs and hypotheses: The decision maker selects
the inputs they believe are important and the tool shows
which hypotheses are supported or denied by that evidence.

Judging plausibility. Judging the plausibility of outcomes can

4.6.3
be supported several ways by a DA:

(1) Explainable/interpretable AI: Provide reasoning steps
that link the evidence to the hypothesis, such as rules, deci-
sion steps, or explanations.

(2) Provide evidence weights: Show how different inputs pos-

itively and negatively contribute to a hypothesis.

(3) Provide epistemic uncertainty: Show uncertainty in the

form of e.g. an uncertainty measure using entropy.

(4) Provide aleatoric uncertainty: Show a measure of uncer-

tainty of the evidence itself.

(5) Evidence selection: Allowing the decision maker to change

evidence (inputs) and ask the DA to re-evaluate.

(6) Argumentation: The decision maker identifies evidence
that supports (refutes) a hypothesis, and the DA highlights:
(a) other evidence that strongly refutes (supports) that hy-
pothesis; and (b) other hypotheses that are strongly sup-
ported (refuted) by that evidence.

4.6.4 Resolution and re-evaluation. For any DA, it is important that
justification for that decision is recorded. Allowing the decision
maker to record: (a) the outcome; (b) evidence for/against that
outcomes; and (c) alternatives that were not chosen and why; is
important for both decision resolution and also re-evaluation. Note
that recording evidence must include evidence that is used by the
human decision maker but not available to the DA. Further research
is required to determine how to support decision makers when re-
evaluating a decision to come up to speed quickly and effectively.

5 CONCLUSION
Our friends Bluster and Prudence can both be useful in supporting
our decisions, but Prudence puts us in control and is better at
helping us weigh up different options. Bluster can be useful; for
example, in low stakes decisions or if time is limited; but overall,
Bluster does not support our cognitive process as well as Prudence.
This paper calls for AI-assisted DAs to follow the lead of Prudence,
and it presents a new conceptual framework of machine-in-the-loop
DAs. We call this conceptual framework evaluative AI.

However, evaluative AI is not a panacea for DAs. Our friend
Prudence makes us do more work, which people prefer to avoid
[19], so we may find that participants prefer less work, but with
worse results Buçinca et al. [1]. This is a side effect of having people
cognitively engage with decisions; however, one that we may need
to accept if we want to truly improve AI-assisted decision support.
We conclude by repeating that the current paradigm of explain-
able AI as justified recommendations is ‘dead’. But the new para-
digm that includes hypothesis-driven explainability could take the
throne, so long live explainable AI!

ACKNOWLEDGMENTS
This research was partly funded by Australian Research Council
Discovery Grant DP190103414. Thanks to Liz Sonenberg, Piers
Howe, Eduardo Velloso, and Tim Schrills for valuable feedback on
drafts of this article.

341FAccT ’23, June 12–15, 2023, Chicago, IL, USA

Tim Miller

REFERENCES
[1] Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z Gajos. 2021. To Trust
or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in
AI-assisted Decision-making. Proc. ACM Hum.-Comput. Interact. 5, CSCW1 (April
2021), 1–21. https://doi.org/10.1145/3449287

[2] Michael Chromik, Malin Eiband, Felicitas Buchner, Adrian Kruger, and Andreas
Butz. 2021.
I think I get your point, AI! the illusion of explanatory depth in
explainable AI. 26th International Conference on Intelligent User Interfaces (2021).
https://dl.acm.org/doi/abs/10.1145/3397481.3450644

[3] S Coderre, H Mandin, P H Harasym, and G H Fick. 2003. Diagnostic reasoning
strategies and diagnostic success. Medical education 37, 8 (Aug. 2003), 695–703.
https://doi.org/10.1046/j.1365-2923.2003.01577.x

[4] Jill L Drury, Gary L Klein, Lashon Booker, Kathy Ryall, and Samantha Dubrow.
2022. Reimagining Situation Awareness and Option Awareness for Human-
Machine Teaming. In 2022 IEEE Conference on Cognitive and Computational
Aspects of Situation Management (CogSIMA). 9–15.
https://doi.org/10.1109/
CogSIMA54611.2022.9830660

[5] Malin Eiband, Daniel Buschek, Alexander Kremer, and Heinrich Hussmann. 2019.
The Impact of Placebic Explanations on Trust in Intelligent Systems. In Extended
Abstracts of CHI. ACM, 1–6. https://doi.org/10.1145/3290607.3312787

[6] Krzysztof Z Gajos and Lena Mamykina. 2022. Do People Engage Cognitively
with AI? Impact of AI Assistance on Incidental Learning. In 27th International
Conference on Intelligent User Interfaces (Helsinki, Finland) (IUI ’22). ACM, New
York, NY, USA, 794–806. https://doi.org/10.1145/3490099.3511138

[7] Ben Green and Yiling Chen. 2019. Disparate Interactions: An Algorithm-in-the-
Loop Analysis of Fairness in Risk Assessments. In Proceedings of the Conference
on Fairness, Accountability, and Transparency (Atlanta, GA, USA). ACM, New
York, NY, USA, 90–99. https://doi.org/10.1145/3287560.3287563

[8] Ben Green and Yiling Chen. 2019. The Principles and Limits of Algorithm-in-
the-Loop Decision Making. Proc. ACM Hum.-Comput. Interact. 3, CSCW (Nov.
2019), 1–24. https://doi.org/10.1145/3359152

[9] David Gunning and David Aha. 2019. DARPA’s explainable artificial intelligence
(XAI) program. AI magazine 40, 2 (June 2019), 44–58. https://doi.org/10.1609/
aimag.v40i2.2850

[10] Robert R Hoffman. 2017. A taxonomy of emergent trusting in the human–machine
relationship. Cognitive systems engineering: The future for a changing world (2017),
137–164.

[11] Robert R Hoffman, Tim Miller, and William J Clancey. 2022. Psychology and AI at
a Crossroads: How Might Complex Systems Explain Themselves? The American
journal of psychology 135, 4 (2022), 365–378.

[12] Robert R Hoffman and Frank J Yates. 2005. Decision making [human-centered
computing]. IEEE intelligent systems 20, 4 (July 2005), 76–83. https://doi.org/10.
1109/MIS.2005.67

[13] Alon Jacovi, Ana Marasović, Tim Miller, and Yoav Goldberg. 2021. Formalizing
Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust
in AI. In Proceedings of the ACM Conference on Fairness, Accountability, and
Transparency. ACM, 624–635. https://doi.org/10.1145/3442188.3445923

[14] Daniel Kahneman. 2011. Thinking, Fast and Slow. Penguin UK.
[15] Harmanpreet Kaur, Eytan Adar, Eric Gilbert, and Cliff Lampe. 2022. Sensible
AI: Re-imagining Interpretability and Explainability using Sensemaking Theory.
(May 2022). arXiv:2205.05057 [cs.HC] http://arxiv.org/abs/2205.05057

[16] Gary Klein. 2015. A naturalistic decision making perspective on studying intuitive
decision making. Journal of applied research in memory and cognition 4, 3 (Sept.
2015), 164–168. https://doi.org/10.1016/j.jarmac.2015.07.001

[17] Gary Klein, Jennifer K Phillips, Erica L Rall, and Deborah A Peluso. 2007. A
data–frame theory of sensemaking. In Expertise out of context. Psychology Press,
118–160.

[18] Gary A Klein. 2017. Sources of Power: How People Make Decisions. MIT Press.
[19] Wouter Kool and Matthew Botvinick. 2018. Mental labour. Nature human
behaviour 2, 12 (Dec. 2018), 899–908. https://doi.org/10.1038/s41562-018-0401-9
[20] Kathryn Ann Lambe, Gary O’Reilly, Brendan D Kelly, and Sarah Curristan.
2016. Dual-process cognitive interventions to enhance diagnostic reason-
ing: a systematic review. BMJ quality & safety 25, 10 (Oct. 2016), 808–820.
https://doi.org/10.1136/bmjqs-2015-004417

[21] John D Lee and Katrina A See. 2004. Trust in automation: designing for appro-
priate reliance. Human factors 46, 1 (2004), 50–80. https://doi.org/10.1518/hfes.
46.1.50_30392

[22] Benedikt Leichtmann, Andreas Hinterreiter, Christina Humer, Marc Streit, and
Martina Mara. 2022. Explainable Artificial Intelligence improves human decision-
making: Results from a mushroom picking experiment at a public art festival.
(Sept. 2022). https://doi.org/10.31219/osf.io/68emr

[23] Prashan Madumal, Tim Miller, Liz Sonenberg, and Frank Vetere. 2020. Explainable
Reinforcement Learning through a Causal Lens. Proceedings of AAAI 34, 03 (April
2020), 2493–2500. https://doi.org/10.1609/aaai.v34i03.5631

[24] David Alvarez Melis, Harmanpreet Kaur, Hal Daumé, III, Hanna Wallach, and
Jennifer Wortman Vaughan. 2021. From Human Explanation to Model Inter-
pretability: A Framework Based on Weight of Evidence. In Proceedings of the

AAAI Conference on Human Computation and Crowdsourcing. 35–47. https:
//ojs.aaai.org/index.php/HCOMP/article/view/18938

[25] Hugo Mercier and Dan Sperber. 2017. The Enigma of Reason. Harvard University

Press.

[26] Tim Miller. 2019. Explanation in artificial intelligence: Insights from the social
sciences. Artificial intelligence (2019). https://www.sciencedirect.com/science/
article/pii/S0004370218305988

[27] Tim Miller. 2021. Contrastive explanation: A structural-model approach. Knowl-

edge Engineering Review 36 (2021), e14.

[28] Mahsan Nourani, Chiradeep Roy, Jeremy E Block, Donald R Honeycutt, Tahrima
Rahman, Eric Ragan, and Vibhav Gogate. 2021. Anchoring Bias Affects Mental
Model Formation and User Reliance in Explainable AI Systems. In 26th Interna-
tional Conference on Intelligent User Interfaces (IUI ’21). ACM, New York, NY, USA,
340–350. https://doi.org/10.1145/3397481.3450639

[29] Raja Parasuraman and Victor Riley. 1997. Humans and Automation: Use, Misuse,
Disuse, Abuse. Human factors 39, 2 (June 1997), 230–253. https://doi.org/10.
1518/001872097778543886

[30] Charles S Peirce. 2009. Writings of Charles S. Peirce: A Chronological Edition,

Volume 8: 1890–1892. Indiana University Press.

[31] Mark S Pfaff, Gary L Klein, Jill L Drury, Sung Pil Moon, Yikun Liu, and Steven O
Entezari. 2013. Supporting Complex Decision Making Through Option Awareness.
Journal of Cognitive Engineering and Decision Making 7, 2 (June 2013), 155–178.
https://doi.org/10.1177/1555343412455799

[32] Forough Poursabzi-Sangdeh, Daniel G Goldstein, Jake M Hofman, Jennifer Wort-
man Vaughan, and Hanna Wallach. 2021. Manipulating and Measuring Model
Interpretability. In Proceedings of the CHI 2021. ACM, New York, NY, USA, 1–52.
https://doi.org/10.1145/3411764.3445315

[33] Cynthia Rudin. 2019. Stop explaining black box machine learning models for
high stakes decisions and use interpretable models instead. Nature Machine
Intelligence 1, 5 (May 2019), 206–215. https://doi.org/10.1038/s42256-019-0048-x
[34] J W Rudolph. 2003. Into the big muddy and out again: Error persistence and crisis

management in the operating room. Ph. D. Dissertation.

[35] Christin Schulze and Ralph Hertwig. 2021. A description-experience gap in
statistical intuitions: Of smart babies, risk-savvy chimps, intuitive statisticians,
and stupid grown-ups. Cognition 210 (May 2021), 104580. https://doi.org/10.
1016/j.cognition.2020.104580

[36] Ben Shneiderman, Catherine Plaisant, Maxine S Cohen, Steven Jacobs, Niklas
Elmqvist, and Nicholas Diakopoulos. 2016. Designing the User Interface: Strategies
for Effective Human-Computer Interaction, 6th Edition. Pearson.

[37] Venkatesh Sivaraman, Leigh A Bukowski, Joel Levin, Jeremy M Kahn, and Adam
Perer. 2023. Ignore, Trust, or Negotiate: Understanding Clinician Acceptance
of AI-Based Treatment Recommendations in Health Care. In Proceedings of CHI.
https://arxiv.org/abs/2302.00096

[38] Frode Sørmo, Jörg Cassens, and Agnar Aamodt. 2005. Explanation in case-based
reasoning–perspectives and goals. Artificial intelligence review 24, 2 (Oct. 2005),
109–143. https://doi.org/10.1007/s10462-005-4607-7

[39] William R Swartout and Johanna D Moore. 1993. Explanation in Second Gen-
eration Expert Systems. In Second Generation Expert Systems. Springer Berlin
Heidelberg, 543–585. https://doi.org/10.1007/978-3-642-77927-5_24

[40] Richard Tomsett, Alun Preece, Dave Braines, Federico Cerutti, Supriyo
Chakraborty, Mani Srivastava, Gavin Pearson, and Lance Kaplan. 2020. Rapid
Trust Calibration through Interpretable and Uncertainty-Aware AI. Patterns (New
York, N.Y.) 1, 4 (July 2020), 100049. https://doi.org/10.1016/j.patter.2020.100049
[41] Jasper van der Waa, Elisabeth Nieuwburg, Anita Cremers, and Mark Neerincx.
2021. Evaluating XAI: A comparison of rule-based and example-based explana-
tions. Artificial intelligence 291 (Feb. 2021), 103404. https://doi.org/10.1016/j.
artint.2020.103404

[42] Q Vera Liao and Kush R Varshney. 2021. Human-Centered Explainable AI (XAI):
From Algorithms to User Experiences. (Oct. 2021). arXiv:2110.10790 [cs.AI]
http://arxiv.org/abs/2110.10790

[43] Mor Vered, Piers Howe, Tim Miller, Liz Sonenberg, and Eduardo Velloso. 2020.
Demand-Driven Transparency for Monitoring Intelligent Agents. IEEE Transac-
tions on Human-Machine Systems 50, 3 (June 2020), 264–275. https://doi.org/10.
1109/THMS.2020.2988859

[44] Danding Wang, Qian Yang, Ashraf Abdul, and Brian Y Lim. 2019. Designing
Theory-Driven User-Centric Explainable AI. In Proceedings of the CHI 2019 (CHI
’19, Paper 601). ACM, New York, NY, USA, 1–15. https://doi.org/10.1145/3290605.
3300831

[45] Frank J Yates and Georges A Potworowski. 2012. Evidence-Based Decision Man-
agement. Oxford University Press, 198—-222. https://doi.org/10.1093/oxfordhb/
9780199763986.013.0012

[46] Yunfeng Zhang, Q Vera Liao, and Rachel K E Bellamy. 2020. Effect of confidence
and explanation on accuracy and trust calibration in AI-assisted decision making.
In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency
(Barcelona, Spain). ACM, New York, NY, USA, 295–305. https://doi.org/10.1145/
3351095.3372852

342