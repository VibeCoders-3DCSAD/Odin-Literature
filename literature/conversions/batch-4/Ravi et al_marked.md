---
conversion_metadata:
  converted_at: "2026-07-21T08:18:30Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Ravi et al.pdf"
  source_pdf_sha256: "f3da5896100785cdd7b64347216dd984176a42913313158d087397c7d7042784"
  page_count: 11
  markdown_char_count: 136264
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

TRuST-M: Evaluating User Trust and Explainability in LLM-Based
Web Moderation Systems

Kamalakkannan Ravi
Kamalakkannan.Ravi@ucf.edu
University of Central Florida
Orlando, Florida, USA

Hemant Surale
hsurale@uwaterloo.ca
University of Waterloo
Waterloo, Ontario, Canada

Jiann-Shiun Yuan
Jiann-Shiun.Yuan@ucf.edu
University of Central Florida
Orlando, Florida, USA

Abstract
As online social platforms face increasing challenges in moderating
nuanced threats across web communities, trust in automated mod-
eration systems is critical. TRuST-M examines this problem in web
and social-network environments, where moderation occurs under
time pressure and public scrutiny. Large language models (LLMs)
achieve strong classification performance but remain difficult to
interpret, reducing user confidence and accountability in real-world
workflows. This work introduces TRuST-M, a human-centered eval-
uation framework that studies how explanation methods influence
trust, understanding, and perceived effectiveness in LLM-based
threat moderation. The framework integrates a RoBERTa model
pretrained on 1M Telegram posts and fine-tuned on 15,063 labeled
messages across three classes (No Threat, Judicial Threat, Non-
Judicial Threat), achieving 95.8% accuracy, weighted F1 of 0.96,
and Cohen’s kappa of 0.94 on a held-out set. A within-subjects
study (n=31) evaluated six messages of varying complexity with
predictions and three explanation methods: Integrated Gradients,
LIME, and attention visualization. LIME was preferred by 58% of
participants for its intuitive word-level highlights, though longer
response times were noted, while attention visualizations were
rated least helpful due to unclear token emphasis. Statistical analy-
sis revealed positive correlations between explanation clarity, user
trust, and confidence in moderation decisions. We frame TRuST-M
as an interpretable decision-support system for human-in-the-loop
moderation, emphasizing calibrated trust and moderator compre-
hension rather than model replacement. The findings show that
explanation clarity and response time meaningfully shape trust and
decision confidence in AI-assisted moderation, advancing trans-
parent, usable, and trustworthy moderation tools for the social
web.

CCS Concepts
• Human-centered computing → User studies; Empirical stud-
ies in HCI; • Computing methodologies → Natural language
processing; Machine learning; • Security and privacy → Social
aspects of security and privacy; Usability in security and privacy;
• Information systems → Social networks; Decision support
systems.

This work is licensed under a Creative Commons Attribution 4.0 International License.
WSDM Companion ’26, Boise, ID, USA
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2358-2/2026/02
https://doi.org/10.1145/3779211.3793172

Keywords
Explainable AI (XAI), Human–AI interaction, Trust in AI, Content
moderation, Threat detection, Large language models (LLMs), User
study, Social transparency, Decision support, Social networks

ACM Reference Format:
Kamalakkannan Ravi, Hemant Surale, and Jiann-Shiun Yuan. 2026. TRuST-
M: Evaluating User Trust and Explainability in LLM-Based Web Moderation
Systems. In The Nineteenth ACM International Conference on Web Search and
Data Mining (WSDM Companion ’26), February 22–26, 2026, Boise, ID, USA.
ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/3779211.3793172

1 Introduction
The widespread deployment of large language models (LLMs) on
online platforms has created both opportunities and challenges for
large-scale content moderation. These systems can rapidly classify
user-generated content for misinformation, hate speech, and nu-
anced threats [26, 39, 66]. However, their opaque decision-making
makes it difficult for moderators and end users to understand why
decisions are made, raising concerns about accountability, fair-
ness, and public trust [8, 18, 48, 53]. Research shows that users
are more likely to accept or challenge automated decisions when
given clear explanations [19, 22], yet transparency tools remain rare
in moderation workflows, especially in safety-sensitive contexts
where misclassification of political content can cause real harm
[24, 33, 51, 55, 70].

Beyond accuracy, effective deployment requires usable trans-
parency: auditing signals must be actionable and comprehensible
to decision-makers [65]. TRuST-M approaches this need by elevat-
ing explanation clarity as a primary design objective. In social-web
moderation settings, our goal is not to replace human judgment but
to support it—treating explainability and trust as first-class require-
ments in human-in-the-loop decision support. This contributes to
broader efforts toward reliable, transparent moderation practices
in fast-moving web environments.

Many safety-critical AI applications—from clinical decision sup-
port [2, 12, 16, 30, 62] to judicial threat assessment [52]—require
not only accuracy but explanations that users can interpret and act
upon. In content moderation, explanations help verify AI reasoning,
resolve disagreements, and calibrate trust [37, 45, 53]. Yet despite
extensive work in explainable AI (XAI), few techniques have been
evaluated for usability or impact in real-world moderation settings
[43, 56, 59].

Aligning LLM-based moderation with human expectations is
further shaped by trade-offs between accuracy, usability, and in-
terpretability. While gradient-based saliency, perturbation-based
attribution, and attention visualization are common XAI meth-
ods, evidence of their effectiveness for end users remains limited

---

<!-- PAGE 2 -->

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

[70, 71]. Few studies assess how users interpret these explanations
or whether they meaningfully improve decision outcomes in prac-
tice [3, 41].

We address this gap with TRuST-M (Threat Reasoning and User
Study of Trust in Moderation), a human-centered evaluation of
explainability in LLM-based threat moderation. Our interactive
Total Freedom Interface (TFI) integrates three explanation tech-
niques—gradient saliency, local perturbation via LIME, and atten-
tion visualization—within a RoBERTa classifier for judicial and
non-judicial threats. Our contributions are:

and SHAP [43]. Attention-based explanations have been applied in
NLP [70], though their interpretability remains debated [57].

Despite these advances, relatively few studies apply XAI directly
to real moderation workflows. Existing work exploring user trust
with post-hoc explanations [4, 44] rarely considers politically sen-
sitive or high-stakes scenarios. Similarly, Ravi and Vela [49] used
attention maps for ideology classification but did not evaluate us-
ability or satisfaction. To date, no prior work has systematically
evaluated how end users interpret diverse explanations during ac-
tual threat moderation tasks.

• A practical trust–explainability evaluation framework embed-
ded in a live moderation interface, integrating complemen-
tary attribution views and mapping them to measured trust,
usability, and perceived effectiveness.

• A within-subjects user study (n=31) quantifying how expla-
nation clarity, response time, and format affect trust, usabil-
ity, and moderation behavior.

• Statistical evidence linking explanation clarity to trust, and
trust to perceived moderation effectiveness, independent of
demographic factors.

• Actionable design guidelines: (a) prioritize low–cognitive-
load visualizations; (b) ensure response times support real-
time decisions; (c) explore hybrid explanation formats that
combine complementary strengths.

2 Related Work
Our work builds on three interconnected research areas: (1) LLM-
based threat detection in NLP, (2) explainable AI (XAI) for content
moderation, and (3) human-centered evaluation of trust in AI sys-
tems. We contribute a user-facing system that integrates multiple
explanation techniques, empirically measures their impact on trust
and decision-making, and provides actionable design guidance for
practitioners. Below, we review each area and identify the research
gaps addressed in this study.

2.1 LLM-Based Threat Detection (NLP Domain)
Large language models (LLMs) have significantly advanced au-
tomated online content moderation, including detection of hate
speech, misinformation, and threats [26, 39, 66]. LLMs often out-
perform traditional classifiers [51], yet remain susceptible to over-
generalization, cultural bias, and misclassification—particularly in
politically sensitive or ambiguous contexts [23, 27, 48].

Most prior work focuses on binary or coarse-grained tasks such
as hate speech [17, 68], toxic language [64], or cyber threats [6].
Far fewer studies address nuanced threat categories such as politi-
cally motivated or judicial threats [28, 32, 69]. Ravi and Yuan [52]
proposed a taxonomy for legal threat classification, but adoption
remains limited due to the lack of domain-specific guidance for
training LLMs in sensitive threat contexts.

2.2 Explainability for Content Moderation (XAI

Domain)

Explainable AI (XAI) methods aim to improve transparency in
model predictions. Common techniques include gradient-based
saliency maps [59], perturbation-based methods such as LIME [53],

2.3 Human-Centered Evaluation and Trust (HCI

Domain)

Interpretability is both a technical and human-centered challenge,
involving usability, comprehension, and trust calibration [19, 29, 41].
Ehsan et al. [22] highlight the need for social-science-informed eval-
uation. In safety-critical domains such as healthcare and criminal
justice, studies show that explanation format influences decision-
making, disagreement resolution, and appropriate reliance on AI
[10, 35].

In content moderation, comparable empirical research is scarce
despite similarly high stakes [54, 58, 61]. Recent work on bias and
fairness emphasizes that usable transparency is essential for account-
able decision support [9]. Our study operationalizes this perspective
by treating trust and explanation clarity as measurable constructs
within interactive moderation interfaces. Trust in AI is shaped by ex-
planation complexity, message ambiguity, and user characteristics
[3, 33], yet few controlled studies isolate these factors in politically
sensitive threat detection. Existing findings seldom translate into
actionable interface-level design recommendations [7, 20, 63].

Our focus is the social-web moderation setting (Telegram), where
we evaluate interpretable, human-in-the-loop decision support for
moderators.

3 Problem Statement
We evaluate how different explanation techniques influence user
trust, satisfaction, and accuracy in AI-assisted threat detection and
content moderation. Building on the gaps identified in Related Work,
we formalize three research gaps:

RG 1 – Domain-Specific Threat Detection Models. We de-
velop a custom pretrained and fine-tuned RoBERTa-based classifier
for nuanced threats (judicial and non-judicial), incorporating tar-
geted task framing, dataset design, and labeling strategies to reduce
ambiguity and improve interpretability (see Task, Data, and Model).
RG 2 – Real-World Evaluation of XAI in Moderation. We
conduct a within-subject user study using the Total Freedom In-
terface (TFI) to examine how explanation complexity, message
ambiguity, and user characteristics affect trust, satisfaction, and
classification accuracy in high-stakes moderation scenarios (see
User Study Experiment).

RG 3 – Interface-Level Design Guidance for Trust. We ana-
lyze behavioral data and participant feedback to derive actionable
design guidelines for trustworthy moderation interfaces, linking
empirical findings to deployment-oriented strategies (see Evalua-
tion Results).

---

<!-- PAGE 3 -->

TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

By addressing these gaps, we assess how explanation methods
shape trust, usability, and effectiveness in AI-assisted moderation,
and we provide grounded design recommendations and limita-
tions—expanded in Evaluation Results and Discussion. Our main
contribution is an evaluation and design framework that operational-
izes trust and explanation clarity for human-in-the-loop moderation
on the social web.

4 Task, Data, and Model
To address the research gaps identified above, we designed a refined
threat-classification task, compiled a domain-specific dataset, and
developed a custom-pretrained and fine-tuned LLM classifier to
serve as the foundation for the user study.

4.1 Task: Refined Threat Detection
Prior moderation research often relies on coarse categories such as
normal, hate, or offensive speech [17]. While effective for broad fil-
tering, such taxonomies lack the nuance needed to capture political
rhetoric and implicit calls for violence that characterize contem-
porary online discourse [5]. Newer multi-level schemes add nu-
ance but frequently blur boundaries between lawful and unlawful
rhetoric [50].

To address this, we adopt a three-class taxonomy [52]:

(1) No Threat: Strongly worded but non-harmful expressions

(e.g., “Live free or die”).

(2) Judicial Threat: Advocacy for legal or punitive action (e.g.,

“Lock her up”).

(3) Non-Judicial Threat: Direct or implied calls for unlawful
violence (e.g., “It’s time to start a civil war”). Mixed cases
default to this class for severity.

This taxonomy provides a clearer separation between lawful-
punitive and unlawful threats while remaining simple enough for
consistent annotation and user interpretation in politically sensitive
moderation contexts.

4.2 Data
To ensure ideological breadth, we collected Telegram channels from
both far-left and far-right communities, though far-right content
predominated due to higher posting volume. This imbalance may
skew predictions and increase false positives for certain ideological
groups, a limitation we acknowledge and discuss in our ethical con-
siderations. Future iterations will explore channel-level stratified
sampling, post-stratification reweighting, and robustness checks
across ideological slices to assess stability under distributional shift.
The full dataset contains 2.3M replies, of which 15,076 were
annotated into No Threat, Judicial Threat, or Non-Judicial Threat
classes using criminology-informed guidelines. After refinement to
resolve borderline cases, 15,063 labeled examples remained. This
dataset was selected for its rich coverage of politically charged and
grievance-driven discourse [11], providing a realistic testbed for
evaluating moderation in high-risk contexts.

4.3 Modeling
The 15,063 labeled examples were divided into training (10,554),
development (2,248), and test (2,261) splits using class-stratified

sampling. We used RoBERTa, a robust transformer architecture
with strong performance across NLP tasks [42]. To capture platform-
specific language and conversational patterns, we first pretrained
RoBERTa on 1M unlabeled Telegram replies (12,260 steps; ≈137
hours), followed by fine-tuning on the labeled set for 100 epochs
(≈168 hours).

The resulting model achieved 95.8% accuracy, weighted F1 of 0.96,
and Cohen’s kappa of 0.94 on the held-out test set, demonstrating
high agreement and strong reliability despite class imbalance and
linguistic ambiguity. These properties provide a stable foundation
for evaluating explanation quality and user trust in our subsequent
user study.

5 User Study Experiment
The experiment evaluated how explainability-enhanced AI threat
detection influences Trust (T), perceived Explainability (E), Usability
(U), and Moderation Confidence (MC) when users classify polit-
ically sensitive web and social-network content. Specifically, we
examined whether combining predictions, confidence scores, and
explanations improves user understanding and decision confidence
in high-stakes moderation scenarios.

Unlike prior work focused primarily on classification accuracy
[31, 39], our study investigates human–AI interaction and user
responses to different explanation types [22, 41, 47]. Although ex-
plainability has been examined in domains such as finance and
healthcare, its role in online moderation—especially for ambiguous
threats—is underexplored [1, 13]. We address this gap through an
empirical evaluation of how three explanation methods shape trust,
judgment confidence, and overall user experience.

Using a within-subjects design, participants classified six mes-
sages under three conditions: no explanation (baseline), a single
explanation method, and all three methods. Each message belonged
to one of the classes No Threat, Judicial Threat, or Non-Judicial
Threat. After completing the tasks, participants filled out a System
Usability Scale (SUS) survey and provided qualitative feedback.

5.1 Participants
We recruited 31 participants (15 female, 16 male), aged 18–44,
through flyers and word-of-mouth. Six participants held PhDs, two
held Master’s degrees, and five held Bachelor’s degrees. Thirteen
participants had prior moderation experience, including two pro-
fessional moderators. AI familiarity was high: 44% (N=14) were
somewhat familiar, 34.3% (N=11) very familiar, and 19% (N=6) unfa-
miliar. Most had never used XAI tools (81.2%). All participants were
active users of web and social-network platforms but unfamiliar
with the explanation methods tested. Each participant received a
$10 gift card upon completion.

5.2 Explainable AI Interface
We developed the Total Freedom Interface (TFI), a custom web-
based application implemented in Python using Streamlit v1.46.1
[60]. TFI integrates the RoBERTa threat classifier (Section 4.3) with
three qualitatively different explanation techniques:

• XAI Method 1 – Integrated Gradients [36]: A gradient-
based attribution method that computes path-integrated gra-
dients to identify influential tokens.

---

<!-- PAGE 4 -->

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

• XAI Method 2 – LIME (Local Interpretable Model-agnostic
Explanations) [53]: A perturbation-based technique that
estimates feature importance via local surrogate models; in-
tuitive but computationally more expensive.

• XAI Method 3 – Final-Layer Attention Visualization
[67]: A visualization of last-layer attention weights. While
attention is debated as a faithful explanation [34, 57, 70], it
serves as a widely recognized baseline.

To avoid framing effects, these were shown (see Figure 1) under
anonymized labels (XAI Method 1–3). In this study, the method–label
mapping remained fixed; future replications will randomize these
mappings.

Participants selected pre-loaded Telegram replies from the test
set and triggered the model’s prediction. The classifier output
one of three labels—No Threat, Judicial Threat, or Non-Judicial
Threat—with distinct color-coded cues. Each explanation method
used its own visualization (e.g., heatmaps, bar charts, token high-
lighting). The interface recorded total interaction time per message,
serving as a coarse measure of cognitive effort.

TFI included usability accommodations such as dark mode, large
fonts, and a responsive layout. At the end of the experiment, the
system exported session logs for analysis.

5.3 Procedure
The experiment lasted about 30 minutes and followed a three-stage
protocol:

(1) Onboarding and Demonstration (5 minutes): Partici-
pants received a brief overview of the study, viewed a live
demonstration with a neutral example, and were warned
about politically sensitive content. The three explanation
methods were introduced at a high level.

(2) Task Execution (10–15 minutes): Participants classified
six messages. For each message, they viewed the prediction
and examined all three anonymized explanation methods.
Interaction time was logged for each message.

(3) Survey and Feedback (10 minutes): Participants com-
pleted the System Usability Scale (SUS) and provided ratings
of explainability, trust, model preference, and moderation
confidence. Open-ended feedback captured suggestions for
improvement.

All interaction logs and survey data were anonymized and stored
on secure university-maintained systems. No personally identifiable
information was collected. The anonymized dataset will be publicly
released to support reproducibility.

5.4 Task Design
Each participant evaluated six pre-loaded Telegram replies—two
per class (No Threat, Judicial Threat, Non-Judicial Threat). For each
class, one message was designated “easy” and one “hard” based
on annotator experience. Easy messages contained explicit threat
markers and unanimous annotator agreement; hard messages con-
tained implicit, sarcastic, or context-dependent language requiring
guideline consultation. Message order was fixed for all participants
to maintain consistent difficulty progression and reduce learning
effects.

For each message, participants followed a standardized workflow
in TFI: click Start Timer, select a message, trigger Predict, review
the model’s classification, examine all three explanation methods,
and click End Timer. Figure 1 illustrates the interface.

After completing all six messages, participants exported a CSV

log of interaction times.

5.4.1 Measaurements. We collected both objective and subjective
measures to analyze how the three XAI methods influenced partici-
pant decision-making. Five measures were used:

• Interaction Time: Total time per message, from Start Timer
to End Timer, including prediction and examination of all
explanation methods.

• Trust in AI: Post-task rating of confidence in the model’s

threat classification (1–5 scale).

• Perceived Explainability: Participant ratings of how well

each explanation clarified the model’s reasoning.

• Moderation Effectiveness: Participant perceptions of how

well the tool supported moderation decisions.

• System Usability: A 19-item usability assessment capturing

ease of use, efficiency, and satisfaction.

In total: 6 messages × 3 explanation methods = 18 explanation in-
teractions per participant, in addition to six time-logged prediction
tasks and four categories of subjective ratings.

6 Evaluation Results
We now present the results of our user study evaluating the impact
of three explanation techniques—Integrated Gradients, LIME, and
attention visualization—on trust, usability, and classification effec-
tiveness in AI-assisted threat moderation. All quantitative metrics
and subjective evaluations are based on data from 31 participants;
statistical tests and visualizations use the cleaned dataset described
below.

6.1 Data Preparation and Cleaning
We first removed trials with incomplete sessions or invalid logs (e.g.,
missing End Timer clicks). For each participant, extreme interaction-
time outliers (more than three standard deviations from that par-
ticipant’s mean) were excluded to reduce the impact of distraction
or disengagement. Across all sessions, fewer than 4% of trials were
dropped due to data quality concerns. The final dataset comprised
31 participants × 6 messages × 3 explanation views = 558 explana-
tion interactions, plus 186 timed classification tasks and 31 sets of
post-task survey responses.

6.2 Analysis Overview
We used non-parametric chi-squared and Mann–Whitney tests
to examine within-subject effects of explanation type and mes-
sage difficulty on trust, explainability, and moderation confidence.
When appropriate, post hoc pairwise comparisons (e.g., Tukey HSD)
were used to identify differences between explanation techniques,
and Greenhouse–Geisser or Huynh–Feldt corrections were applied
when sphericity assumptions were violated.

For interaction time, we assessed normality using Shapiro–Wilk
tests. When normality was violated, we applied a log transforma-
tion before running ANOVA and pairwise 𝑡-tests with Bonferroni

---

<!-- PAGE 5 -->

TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Figure 1: Annotated screenshot of the Total Freedom Interface (TFI) showing LIME-based explanation (XAI Method 2). Key
components include: (Input Text), (Prediction), (XAI Selection), (Prediction Score), (Candidate Words & Contributions), and
(Influential Words). Participants sequentially trigger predictions and explore explanations.

Figure 2: Mean interaction times by threat example (error
bars represent standard deviation).

corrections. We used Spearman’s 𝜌 for association tests because
(i) Likert-type ratings are ordinal and (ii) residuals for several mea-
sures deviated from normality; Spearman correlation is robust un-
der these conditions.

Figure 3: Mean Likert ratings aggregated by usability, trust,
explainability, and confidence in moderation decisions (error
bars represent standard deviation).

---

<!-- PAGE 6 -->

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

Figure 4: Aggregated user ratings for Trust (TQ1–TQ3), Explainability (EQ1–EQ3), and Moderation Confidence (MQ1–MQ3).
Error bars indicate standard deviation.

6.3 Interaction Time
Average interaction time per message varied by example and dif-
ficulty (Figure 2), with statistically significant differences across
pairs. As expected, “easy” tasks generally took less time than “hard”
ones, except for judicial threats.

For example, an easy No-Threat task averaged 112.5 seconds,
compared to 160.3 seconds for its harder counterpart—a difference
of 43.8 seconds. In contrast, the “easy” judicial threat took longer
than its harder counterpart, suggesting additional verification in
severe cases. All differences were significant (p<0.05).

The increased time on the “easy” judicial threat may reflect a con-
firmation–verification effect: when content appears clearly severe,
participants may invest extra time to double-check the AI’s output
before accepting it. This is consistent with work on confirmation
bias and decision-making under emotionally charged evidence [46],
as well as findings that even straightforward explanations can lead
users to spend more time validating model reasoning [40].

6.4 Trust and Explainability
Subjective ratings of trust and explainability were collected on a
5-point Likert scale (5 = highest). Overall, participants reported
relatively high ratings for both, with averages around 4.2. Figure 3
shows the mean trust and explainability scores aggregated across
all explanation methods.

To test whether explanation clarity is associated with trust in
the model, we ran a Spearman rank-order correlation. We observed
a positive, statistically significant association between trust and
explanation clarity (𝜌 = 0.493, 𝑝 = 0.005), indicating a moderate,
monotonic relationship (see Figure 5). In other words, participants
who perceived the explanations as clearer also tended to report
higher trust in the system.

6.5 Usability
Participants rated the interface as easy to understand and operate,
with usability receiving the highest aggregated scores (mean = 4.27,
SD = 0.56). The main complexity, according to comments, stemmed
from interpreting the explanation methods themselves rather than
from basic navigation or controls.

We used a 19-item standardized usability assessment to evaluate
overall usability. All participants reported that the interface was
easy to use and did not interfere with their interaction flow. Usabil-
ity showed increasing correlations with Trust (𝜌 = 0.38, 𝑝 < 0.05),
Explainability (𝜌 = 0.57, 𝑝 < 0.01), and Moderation Confidence
(𝜌 = 0.72, 𝑝 < 0.01), suggesting that while usability alone does
not guarantee trust, it is an important enabling factor for effective
decision support.

6.6 Moderation Effectiveness
Participants also rated how helpful the tool was for real-world
content moderation. As shown in Figure 3, moderation effective-
ness scores were slightly lower on average than trust, usability,
and explainability, although these differences were not statistically
significant.

Moderation effectiveness was strongly correlated with trust
(𝜌 = 0.62, 𝑝 < 0.01) and explainability (𝜌 = 0.66, 𝑝 < 0.01), in-
dicating that participants who trusted the model more and found
explanations clearer also felt more confident using the tool for mod-
eration decisions. Education level was associated with usability
satisfaction: 83% of PhD respondents rated the system “Excellent”
or “Best Imaginable,” compared to 50% of Bachelor’s degree holders
who rated it “Good” or “Fair” (𝜒 2 (6, 𝑁 = 31) = 20.99, 𝑝 < 0.05).
No significant effects were found for gender, age, or prior AI/ML
experience.

---

<!-- PAGE 7 -->

TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Overall, 58% of participants (18/31) preferred Method 2; the remain-
ing methods collectively accounted for the rest (∼6/31).

Interest in Hybrid Explanations. A smaller subset of participants
suggested that combining methods could improve interpretability.
For instance, P13 remarked:

“If you combine methods 2 and 3, it would be easier
for general people to interpret the outputs of the tool.
Because plots are always easy and quick to evaluate
and compare, and it doesn’t take a long time to read
passages like what happens in method one.”

This comment about general people hints that explanation pref-
erences may vary with background and familiarity, reinforcing
the quantitative finding that education level influences usability
perceptions.

Demographic Effects on Usability. Consistent with the quantita-
tive analysis, qualitative responses suggested that users with more
advanced education or analytical training were more comfortable
with the interface and explanations. As noted earlier, education
level was significantly associated with overall experience ratings
(𝜒 2 (6, 𝑁 = 31) = 20.99, 𝑝 < 0.05). However, due to unbalanced
group sizes, we could not reliably infer how prior experience with
moderation tools or AI/ML systems affected trust, explainability,
or moderation confidence.

Limitations of Method 3 (Attention Visualization). Partici-
pants frequently criticized Method 3 for confusing scores and un-
clear token importance. P22 wrote:

“XAI Method 3 was the least helpful as it did not give
the more important words greater attention scores.”

Similarly, P19 and P20 raised concerns about emphasis on non-
informative tokens:

“[...] XAI Method 3 was often giving higher attention
to special tokens like inverted commas, which can be
worked upon since they are not always the most infor-
mative tokens.” — P19
“Model 3 would constantly return high values for words
that don’t seem relevant at all to the threat.” — P20

P27 suggested that adding more detail on why specific tokens
were highlighted could help make this method more understand-
able.

Together, these findings indicate that improving the responsiveness
of Method 2 and refining the interpretability of Method 3 could
further enhance user experience and strengthen confidence in AI-
assisted moderation.

7 Discussion
Our findings reinforce prior work in explainable AI (XAI) and
human–AI interaction by showing that explanation quality directly
influences user trust and perceived effectiveness in moderation
tasks. In line with Ehsan et al. [22] and Liao et al. [41], we observed
a statistically significant positive correlation between perceived
explanation clarity and trust in the system (𝜌 = 0.493, 𝑝 = 0.005).
This suggests that the interpretability of model outputs remains a
central factor in user acceptance of AI-assisted decisions, even when
underlying model accuracy is high (accuracy = 95.8%, F1 = 0.96).

Figure 5: Spearman correlation among usability, trust, ex-
plainability, and confidence in moderation decisions (corre-
lation coefficients shown in cells).

These patterns suggest that domain-specific familiarity and ana-
lytical comfort may influence how users experience the interface,
potentially more than general AI literacy. To mitigate risks of bias
or misuse, we recommend that any deployment pair this type of
tool with human oversight, fairness audits, and context-specific
training.

6.7 Qualitative Feedback
We conducted a thematic analysis of open-ended responses and
grouped them into recurring themes.

Preference for Method 2 (LIME). Participants generally pre-
ferred simpler, color-coded visualizations over dense or text-heavy
explanations. Many expressed confusion when different methods
highlighted different tokens for the same message, suggesting the
value of explanation alignment.

When asked which explanation method was most or least helpful,
there was a strong inclination toward Method 2, which provided
color-coded highlights and ranked word importance. For example,
P23 noted:

“Method 2 was the most helpful, as it clearly separated
the words that were important for the label given.”

Similarly, P3 commented:

“Model 2 was good because it clearly highlighted the
words that were important, and it used a darker high-
light to signify more importance or emphasis (which
was easy to recognize), and also the explanation of rank-
ing words from top to bottom in terms of how much they
fit what the model was looking for helped understand
things very clearly.”

At the same time, several participants raised concerns about

response time for Method 2. As P10 put it:

“Faster XAI method 2 implementation would help [for
a] real-world use case.”

---

<!-- PAGE 8 -->

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

In this way, RG 1 is addressed not only at the model-performance
level but also in a trust-sensitive evaluation setting.

7.1 Explanation Method Performance
Participants’ strong preference for the perturbation-based method
(LIME, Method 2) highlights the value of intuitive, word-level visual-
izations for threat moderation. This aligns with Poursabzi-Sangdeh
et al. [47], who found that simpler, localized explanations can im-
prove users’ reasoning about model outputs. These results speak
directly to RG 2 by providing a within-subject, realistic comparison
of multiple explanation types under identical task conditions.

Latency concerns raised by several participants indicate that
computational cost remains a barrier to real-time deployment, con-
tributing to RG 3 by emphasizing the need for responsiveness in
trustworthy moderation interfaces [38].

The limited utility of attention-based visualizations (Method 3)
goes beyond user unfamiliarity and reflects structural weaknesses
in raw attention interpretability. Prior critiques [57, 70] note that
attention weights may not align with causal reasoning; in our study,
this manifested as misleading salience on low-value tokens. Includ-
ing Method 3 served as both a baseline and a targeted test of these
critiques in a high-stakes setting, further advancing RG 2 by ex-
amining diverse explanation strategies—even those with known
limitations—in realistic conditions. In practice, pairing attention
with plain-language legends and token filtering aligns with broader
principles of usable transparency, ensuring that explanation arti-
facts are understandable and actionable rather than merely available
[65].

7.2 Trust, Usability, and Moderation Confidence
Trust and perceived moderation effectiveness were highly corre-
lated (𝜌 = 0.62, 𝑝 < 0.01), supporting Jacovi and Goldberg’s [33]
assertion that trust is closely tied to perceived task success. This
addresses RG 2 by linking explanation clarity and user trust to
measurable, task-level outcomes in a high-stakes, web-based mod-
eration setting.

Usability emerged as a necessary but not sufficient condition
for trust. The TFI received high usability ratings (mean = 4.27), yet
trust varied more strongly with explanation clarity than with ease
of use. This distinction reinforces that usability and interpretability
are orthogonal design dimensions [41], directly informing RG 3
by suggesting that interface design must explicitly support sense-
making, not only efficient interaction.

7.3 Human Factors in Moderation
7.3.1 Cognitive Effort and Task Complexity. Interaction-time anal-
ysis showed that message difficulty significantly influenced cog-
nitive effort, except in the “easy” judicial-threat category, where
participants still spent more time despite lower classification com-
plexity. This likely reflects verification behavior: when content
appears clearly severe, moderators may extend review time to
confirm correctness—consistent with confirmation-bias effects in
decision-making [46]. In high-stakes contexts, even clear-cut cases
can prompt additional scrutiny due to perceived risk.

This finding supports RG 2 by illustrating how real-world am-
biguity and perceived severity shape explanation use, even when

objective task difficulty is low. From a design standpoint, it con-
tributes to RG 3 by suggesting tiered interaction modes: latency-
sensitive “quick review” flows for routine cases and richer “deep
review” flows for high-impact or ambiguous content, potentially
combined with explicit system-confidence cues to help moderators
balance speed and thoroughness.

7.3.2 Demographic Effects. Education level correlated positively
with usability satisfaction: 83% of PhD respondents rated the system
as “Excellent” or “Best Imaginable,” compared to 50% of Bachelor’s
degree holders (𝜒 2 (6, 𝑁 = 31) = 20.99, 𝑝 < 0.05). No significant
differences appeared in trust or explainability ratings by gender,
age, or prior AI/ML tool experience. This contrasts with domains
where AI familiarity improves trust calibration [19, 29], suggesting
that moderation performance may depend more on domain-specific
knowledge (e.g., platform policies, threat typologies) than general
AI literacy. Several non-technical participants with prior modera-
tion experience reported high confidence interpreting explanations,
while technically skilled but moderation-inexperienced participants
described occasional uncertainty.

This outcome further supports RG 2 by indicating that domain-
specific familiarity—not just AI literacy—shapes moderator perfor-
mance and satisfaction. It also has practical implications for RG 3,
underscoring the value of onboarding and training that emphasize
platform policies and threat taxonomies, rather than relying solely
on generic AI education.

7.4 Design Implications
Our results yield actionable guidelines for explainable moderation
tools, representing direct outputs of RG 3 as concrete, deployable
recommendations:

• Prioritize simple, local visualizations. Participants re-
sponded best to visualizations that clearly highlight relevant
words and avoid visual clutter. Designs that make impor-
tance cues immediately visible scored highest for both trust
and usability.

• Treat latency as a first-class design constraint. Even
strong explanations lose value if slow to load. The slower
response time of the preferred method (LIME) suggests that
in fast-paced moderation, latency can directly affect engage-
ment, workflow continuity, and ultimately trust.

• Adopt hybrid explanation strategies. Some participants
proposed combining the clarity of word-level highlights with
lightweight visual overviews. Hybrid approaches may miti-
gate the limitations of individual methods and better serve
heterogeneous user needs.

• Match explanation depth to risk. For legally sensitive or
high-impact content, moderators often spend extra time veri-
fying even straightforward cases. Providing tiered modes—such
as quick review for routine items and deep review for critical
or ambiguous ones—can help align explanation depth and
interaction time with task criticality.

By operationalizing explanation clarity, trust, and moderator
usability in a live web context, TRuST-M advances algorithmic
transparency and fairness [22] objectives for systems deployed on
social-network platforms, in line with broader efforts toward inter-
pretable, human-aligned AI on the social web.

---

<!-- PAGE 9 -->

TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

7.5 Limitations and Future Work
This study involved a modest participant pool (𝑛 = 31), with
only two professional moderators, which limits generalization to
expert-heavy or large-scale operational environments. The under-
representation of domain experts affects RG 2 and RG 3, and broader
evaluation is needed to validate these findings. In future work, we
plan to scale to cohorts of >50 moderators across multiple platforms
to strengthen external validity and expert coverage.

The fixed-order presentation of six messages, while providing
consistent difficulty progression, may have introduced order effects.
Future studies should use randomized or counterbalanced designs
and randomize both message order and the mapping of anonymized
XAI labels to methods to remove residual framing effects.

Demographic analysis showed that higher education levels were
associated with greater usability satisfaction, while prior AI or
moderation-tool experience did not significantly affect trust or
explainability ratings. This diverges from other domains [19, 29],
and targeted recruitment of professional moderators could clarify
whether cognitive framing, risk perception, or task-specific heuris-
tics drive this pattern.

Our saliency, perturbation, and attention-based explanations
are complementary to other interpretability families, such as logic-
based or symbolic surrogates that translate black-box reasoning
into human-understandable rule sets [25]. Integrating such neuro-
symbolic or rule-inductive approaches in moderation UIs may en-
hance global interpretability and policy alignment, but this remains
outside the current experimental scope.

Several participants noted slower response times for the perturba-
tion based method (LIME, Method 2), highlighting the need to explic-
itly assess latency in real-time workflows. Attention-based visualiza-
tions (Method 3) consistently underperformed in perceived useful-
ness and clarity, likely due to misleading emphasis on non-semantic
tokens—a limitation documented in prior NLP interpretability re-
search [34, 57, 70]. Its inclusion here served as both a baseline and
an empirical validation of these critiques in high-stakes modera-
tion (RG 2). Future work should quantify latency impacts, optimize
computation pipelines, and refine attention-based methods via con-
textual weighting, token filtering, or hybrid strategies.

Finally, as this work was conducted in a controlled, single-session
lab setting, longitudinal field deployments in operational environ-
ments are needed to assess how trust, accuracy, and explanation
preferences evolve with sustained, high-volume, and contextually
diverse threat exposure. Such deployments would extend RG 3 by
examining how design guidelines hold up under real-world work-
load, policy change, and adversarial adaptation.

8 Conclusion
This paper introduced TRuST-M, a framework for evaluating how
explanation methods shape user trust, usability, and perceived
effectiveness in LLM-based threat moderation. Using a domain-
adapted RoBERTa classifier and three complementary explanation
techniques—gradient-based saliency, LIME, and attention visualiza-
tion—we conducted a within-subjects study to examine moderation
decisions in a social-web setting. Explanation clarity showed a
significant positive correlation with trust (𝜌 = 0.493, 𝑝 = 0.005),
LIME’s localized highlights were preferred by 58% of participants

despite latency costs, and trust aligned closely with perceived mod-
eration effectiveness (𝜌 = 0.62, 𝑝 < 0.01). Usability alone did not
guarantee trust, underscoring the importance of interpretable, cog-
nitively lightweight visualizations.

We recommend prioritizing explanation formats that minimize
cognitive load, reducing latency for real-time workflows, and explor-
ing hybrid strategies that combine complementary strengths. Future
work should validate these findings with larger and more expert-
diverse cohorts, and through longitudinal deployments in opera-
tional moderation pipelines to refine explanation design and estab-
lish standards for transparent, accountable AI. Extending TRuST-M
toward fairness-aware and globally interpretable evaluation rep-
resents a promising direction for aligning automated moderation
tools with real-world policy and practitioner needs.

Overall, TRuST-M positions explainability as an interpretable
decision-support layer for web and social-network moderation, aligned
with ongoing efforts to build transparent, trustworthy, and respon-
sibly deployed AI systems.

Ethical Considerations
This study received University IRB approval (ID: STUDY0000ZZ00)
under secondary data analysis. All model-development data were
drawn from publicly accessible Telegram channels without collect-
ing personally identifiable information. The dataset contained both
far-right and far-left sources, though far-right content was more
prevalent; this imbalance is acknowledged as a limitation (see Data
section).

Participants were briefed using a neutral demonstration mes-
sage, provided an explicit content warning, and were encouraged to
ask questions throughout to safeguard well-being. Interaction logs,
timing data, and survey responses were anonymized and stored
securely on university systems. All anonymized data and analy-
sis code will be released to support reproducibility (see Procedure
section).

While TRuST-M aims to strengthen trust and usability in AI-
assisted moderation, we note potential risks, including over-reliance
on automated outputs or inadvertent suppression of lawful speech
and emphasize the need for human oversight in deployment (see
Moderation Effectiveness). For real-world implementations, we rec-
ommend integrating lightweight bias-visualization modules [14]
and adopting reproducible evaluation and unlearning checklists to
ensure ongoing fairness and accountability [15, 21].

References
[1] Muhammad Ali, Piotr Sapiezynski, Aleksandra Korolova, Alan Mislove, and
Aaron Rieke. 2021. Ad Delivery Algorithms: The Hidden Arbiters of Political
Messaging. In Proceedings of the 14th ACM International Conference on Web Search
and Data Mining (Virtual Event, Israel) (WSDM ’21). Association for Computing
Machinery, New York, NY, USA, 13–21. doi:10.1145/3437963.3441801

[2] Ali Amini, Mohammad Alijanpour, Behnam Latifi, and Ali Motie Nasrabadi. 2025.
ADHDeepNet From Raw EEG to Diagnosis: Improving ADHD Diagnosis through
Temporal-Spatial Processing, Adaptive Attention Mechanisms, and Explainability
in Raw EEG Signals. arXiv preprint arXiv:2509.08779 (2025).

[3] Siddhant Arora, Danish Pruthi, Norman Sadeh, William W. Cohen, Zachary C.
Lipton, and Graham Neubig. 2022. Explain, Edit, and Understand: Rethinking
User Study Design for Evaluating Model Explanations. Proceedings of the AAAI
Conference on Artificial Intelligence 36, 5 (Jun. 2022), 5277–5285. doi:10.1609/aaai.
v36i5.20464

[4] Marzieh Babaeianjelodar, Gurram Poorna Prudhvi, Stephen Lorenz, Keyu Chen,
Interpretable

Sumona Mondal, Soumyabrata Dey, and Navin Kumar. 2022.

---

<!-- PAGE 10 -->

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

and High-Performance Hate and Offensive Speech Detection. In HCI Interna-
tional 2022 – Late Breaking Papers: Interacting with eXtended Reality and Artificial
Intelligence, Jessie Y. C. Chen, Gino Fragomeni, Helmut Degen, and Stavroula
Ntoa (Eds.). Springer Nature Switzerland, Cham, 233–244.

[5] Babak Bahador. 2023. Monitoring hate speech and the limits of current definition.
In Challenges and perspectives of hate speech research, Christian Strippel, Sünje
Paasch-Colberg, Martin Emmer, and Joachim Trebbe (Eds.). Digital Communica-
tion Research, Vol. 12. Berlin, 291–298. doi:10.48541/dcr.v12.17

[6] Vahid Behzadan, Carlos Aguirre, Avishek Bose, and William Hsu. 2018. Corpus
and Deep Learning Classifier for Collection of Cyber Threat Indicators in Twitter
Stream. In 2018 IEEE International Conference on Big Data (Big Data). 5002–5007.
doi:10.1109/BigData.2018.8622506

[7] Ghazaleh Beigi, Ruocheng Guo, Alexander Nou, Yanchao Zhang, and Huan Liu.
2019. Protecting User Privacy: An Approach for Untraceable Web Browsing
History and Unambiguous User Profiles. In Proceedings of the Twelfth ACM Inter-
national Conference on Web Search and Data Mining (Melbourne VIC, Australia)
(WSDM ’19). Association for Computing Machinery, New York, NY, USA, 213–221.
doi:10.1145/3289600.3291026

[8] Reuben Binns, Max Van Kleek, Michael Veale, Ulrik Lyngs, Jun Zhao, and Nigel
Shadbolt. 2018. ’It’s Reducing a Human Being to a Percentage’: Perceptions of Jus-
tice in Algorithmic Decisions. In Proceedings of the 2018 CHI Conference on Human
Factors in Computing Systems (Montreal QC, Canada) (CHI ’18). Association for
Computing Machinery, New York, NY, USA, 1–14. doi:10.1145/3173574.3173951
[9] Ludovico Boratto, Stefano Faralli, Mirko Marras, and Giovanni Stilo. 2023. Fourth
international workshop on algorithmic bias in search and recommendation (bias
2023). In European Conference on Information Retrieval. Springer, 373–376.
[10] Adrian Bussone, Simone Stumpf, and Dympna O’Sullivan. 2015. The Role of
Explanations on Trust and Reliance in Clinical Decision Support Systems. In 2015
International Conference on Healthcare Informatics. 160–169. doi:10.1109/ICHI.
2015.26

[11] Hongliu Cao. 2025. Writing Style Matters: An Examination of Bias and Fairness in
Information Retrieval Systems. In Proceedings of the Eighteenth ACM International
Conference on Web Search and Data Mining (Hannover, Germany) (WSDM ’25).
Association for Computing Machinery, New York, NY, USA, 336–344. doi:10.
1145/3701551.3703514

[12] Yuyan Chen, Jin Zhao, Zhihao Wen, Zhixu Li, and Yanghua Xiao. 2024. Tem-
poralMed: Advancing Medical Dialogues with Time-Aware Responses in Large
Language Models. In Proceedings of the 17th ACM International Conference on Web
Search and Data Mining (Merida, Mexico) (WSDM ’24). Association for Computing
Machinery, New York, NY, USA, 116–124. doi:10.1145/3616855.3635860

[13] Philipp Christmann, Rishiraj Saha Roy, and Gerhard Weikum. 2022. Beyond NED:
Fast and Effective Search Space Reduction for Complex Question Answering over
Knowledge Bases. In Proceedings of the Fifteenth ACM International Conference on
Web Search and Data Mining (Virtual Event, AZ, USA) (WSDM ’22). Association
for Computing Machinery, New York, NY, USA, 172–180. doi:10.1145/3488560.
3498488

[14] Francesca Ciccarelli, Andrea D’Angelo, and Giovanni Stilo. 2024. Towards a
Novel Visual Evaluation of Algorithmic Bias: Insights on the Italian Academic
System. (2024).

[15] Andrea D’Angelo, Claudio Savelli, Gabriele Tagliente, Flavio Giobergia, Elena Bar-
alis, Giovanni Stilo, et al. 2025. ERASURE: A Modular and Extensible Framework
for Machine Unlearning. In Titolo volume non avvalorato. ACM.

[16] Fatemeh Dashtiahangar and Jiann-Shiun Yuan. 2025. Bridging Morphology and
Molecular Signatures: Multi-Task Deep Learning for Multi-Omics Prediction from
Histopathology. In 2025 IEEE/CVF Conference on Computer Vision and Pattern
Recognition Workshops (CVPRW). IEEE, 1–9.

[17] Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017.
Automated Hate Speech Detection and the Problem of Offensive Language. Pro-
ceedings of the International AAAI Conference on Web and Social Media 11, 1 (May
2017), 512–515. doi:10.1609/icwsm.v11i1.14955

[18] Chenlong Deng, Yujia Zhou, and Zhicheng Dou. 2022. Improving Personalized
Search with Dual-Feedback Network. In Proceedings of the Fifteenth ACM Inter-
national Conference on Web Search and Data Mining (Virtual Event, AZ, USA)
(WSDM ’22). Association for Computing Machinery, New York, NY, USA, 210–218.
doi:10.1145/3488560.3498447

[19] Finale Doshi-Velez and Been Kim. 2017. Towards A Rigorous Science of In-
terpretable Machine Learning. arXiv: Machine Learning (2017). https://api.
semanticscholar.org/CorpusID:11319376

[20] Yijun Duan and Adam Jatowt. 2019. Across-Time Comparative Summarization of
News Articles. In Proceedings of the Twelfth ACM International Conference on Web
Search and Data Mining (Melbourne VIC, Australia) (WSDM ’19). Association
for Computing Machinery, New York, NY, USA, 735–743. doi:10.1145/3289600.
3291008

[21] Giordano d’Aloisio, Andrea D’Angelo, Antinisca Di Marco, and Giovanni Stilo.
2023. Debiaser for Multiple Variables to enhance fairness in classification tasks.
Information Processing & Management 60, 2 (2023), 103226.

[22] Upol Ehsan, Q. Vera Liao, Michael Muller, Mark O. Riedl, and Justin D. Weisz.
2021. Expanding Explainability: Towards Social Transparency in AI systems. In

Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems
(Yokohama, Japan) (CHI ’21). Association for Computing Machinery, New York,
NY, USA, Article 82, 19 pages. doi:10.1145/3411764.3445188

[23] Yi Fang, Luo Si, Naveen Somasundaram, and Zhengtao Yu. 2012. Mining con-
trastive opinions on political texts using cross-perspective topic model. In Pro-
ceedings of the Fifth ACM International Conference on Web Search and Data Mining
(Seattle, Washington, USA) (WSDM ’12). Association for Computing Machinery,
New York, NY, USA, 63–72. doi:10.1145/2124295.2124306

[24] Alessandro Flaborea, Bardh Prenkaj, Bharti Munjal, Marco Aurelio Sterpa, Dario
Aragona, Luca Podo, and Fabio Galasso. 2023. Are We Certain It’s Anomalous?. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition
(CVPR) Workshops. 2897–2907.

[25] Daniele Fossemò, Filippo Mignosi, Luca Raggioli, Matteo Spezialetti, Fabio Aurelio
D’Asaro, et al. 2022. Using Inductive Logic Programming to globally approximate
Neural Networks for preference learning: challenges and preliminary results. In
CEUR WORKSHOP PROCEEDINGS. 67–83.

[26] Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A.
Smith. 2020. RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Lan-
guage Models. In Findings of the Association for Computational Linguistics: EMNLP
2020, Trevor Cohn, Yulan He, and Yang Liu (Eds.). Association for Computational
Linguistics, Online, 3356–3369. doi:10.18653/v1/2020.findings-emnlp.301
[27] Vahid Ghafouri, Vibhor Agarwal, Yong Zhang, Nishanth Sastry, Jose Such, and
Guillermo Suarez-Tangil. 2023. AI in the Gray: Exploring Moderation Policies in
Dialogic Large Language Models vs. Human Answers in Controversial Topics.
In Proceedings of the 32nd ACM International Conference on Information and
Knowledge Management (Birmingham, United Kingdom) (CIKM ’23). Association
for Computing Machinery, New York, NY, USA, 556–565. doi:10.1145/3583780.
3614777

[28] Rishav Hada, Amir Ebrahimi Fard, Sarah Shugars, Federico Bianchi, Patricia
Rossini, Dirk Hovy, Rebekah Tromble, and Nava Tintarev. 2023. Beyond Digital
"Echo Chambers": The Role of Viewpoint Diversity in Political Discussion. In
Proceedings of the Sixteenth ACM International Conference on Web Search and
Data Mining (Singapore, Singapore) (WSDM ’23). Association for Computing
Machinery, New York, NY, USA, 33–41. doi:10.1145/3539597.3570487

[29] Robert R. Hoffman, Shane T. Mueller, Gary Klein, and Jordan Litman. 2018.
Metrics for Explainable AI: Challenges and Prospects. CoRR abs/1812.04608
(2018). arXiv:1812.04608 http://arxiv.org/abs/1812.04608

[30] Sanne A. Hoogenboom, Kamalakkannan Ravi, Megan M. Engels, Ismail Irmakci,
Elif Keles, Candice W. Bolan, Michael B. Wallace, and Ulas Bagci. 2021. 79
Missed Diagnosis of Pancreatic Ductal Adenocarcinoma Detection using Deep
Convolutional Neural Network. Gastroenterology 160, 6, Supplement (2021), S–18.
doi:10.1016/S0016-5085(21)00794-0

[31] Tao Huang. 2025. Content moderation by llm: From accuracy to legitimacy.

Artificial Intelligence Review 58, 10 (2025), 1–32.

[32] Zexi Huang, Arlei Silva, and Ambuj Singh. 2022. POLE: Polarized Embedding for
Signed Networks. In Proceedings of the Fifteenth ACM International Conference on
Web Search and Data Mining (Virtual Event, AZ, USA) (WSDM ’22). Association
for Computing Machinery, New York, NY, USA, 390–400. doi:10.1145/3488560.
3498454

[33] Alon Jacovi and Yoav Goldberg. 2021. Aligning Faithful Interpretations with their
Social Attribution. Transactions of the Association for Computational Linguistics 9
(2021), 294–310. doi:10.1162/tacl_a_00367

[34] Sarthak Jain and Byron C. Wallace. 2019. Attention is not Explanation. In Pro-
ceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume 1 (Long
and Short Papers), Jill Burstein, Christy Doran, and Thamar Solorio (Eds.). As-
sociation for Computational Linguistics, Minneapolis, Minnesota, 3543–3556.
doi:10.18653/v1/N19-1357

[35] Weina Jin, Xiaoxiao Li, and Ghassan Hamarneh. 2022. Evaluating Explainable AI
on a Multi-Modal Medical Imaging Task: Can Existing Algorithms Fulfill Clinical
Requirements? Proceedings of the AAAI Conference on Artificial Intelligence 36,
11 (Jun. 2022), 11945–11953. doi:10.1609/aaai.v36i11.21452

[36] Narine Kokhlikyan, Vivek Miglani, Miguel Martin, Edward Wang, Bilal Alsallakh,
Jonathan Reynolds, Alexander Melnikov, Natalia Kliushkina, Carlos Araya, Siqi
Yan, and Orion Reblitz-Richardson. 2020. Captum: A unified and generic model
interpretability library for PyTorch. CoRR abs/2009.07896 (2020). arXiv:2009.07896
https://arxiv.org/abs/2009.07896

[37] Anastasiia Kornilova and Lucas Bernardi. 2021. Mining the stars: learning quality
ratings with user-facing explanations for vacation rentals. In Proceedings of the
14th ACM International Conference on Web Search and Data Mining. 976–983.
[38] Sanmi Koyejo and Bo Li. 2024. Towards Trustworthy Large Language Models.
In Proceedings of the 17th ACM International Conference on Web Search and Data
Mining (Merida, Mexico) (WSDM ’24). Association for Computing Machinery,
New York, NY, USA, 1126–1127. doi:10.1145/3616855.3636454

[39] Deepak Kumar, Yousef Anees AbuHashem, and Zakir Durumeric. 2024. Watch
your language: Investigating content moderation with large language models. In
Proceedings of the International AAAI Conference on Web and Social Media, Vol. 18.
865–878.

---

<!-- PAGE 11 -->

TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Detection. In Proceedings of the 17th ACM International Conference on Web Search
and Data Mining (Merida, Mexico) (WSDM ’24). Association for Computing
Machinery, New York, NY, USA, 626–635. doi:10.1145/3616855.3635771

[59] Karen Simonyan, Andrea Vedaldi, and Andrew Zisserman. 2014. Deep Inside
Convolutional Networks: Visualising Image Classification Models and Saliency
Maps. In Workshop at International Conference on Learning Representations.
[60] Snowflake Inc. 2025. Streamlit: A Faster Way to Build and Share Data Apps.

https://pypi.org/project/streamlit/. https://streamlit.io Version 1.46.1.

[61] Donghyun Son, Byounggyu Lew, Kwanghee Choi, Yongsu Baek, Seungwoo Choi,
Beomjun Shin, Sungjoo Ha, and Buru Chang. 2023. Reliable Decision from
Multiple Subtasks through Threshold Optimization: Content Moderation in the
Wild. In Proceedings of the Sixteenth ACM International Conference on Web Search
and Data Mining (Singapore, Singapore) (WSDM ’23). Association for Computing
Machinery, New York, NY, USA, 285–293. doi:10.1145/3539597.3570439

[62] Azwad Tamir and Jiann-Shiun Yuan. 2025. Prot-GO: A Parallel Transformer
Encoder-Based Fusion Model for Accurately Predicting Gene Ontology (GO)
Terms from Full-Scale Protein Sequences. Electronics 14, 19 (2025), 3944.
[63] Theodora Tsikrika, Babak Akhgar, Vasilis Katos, Stefanos Vrochidis, Pete Burnap,
and Matthew L. Williams. 2017. 1st International Workshop on Search and Mining
Terrorist Online Content & Advances in Data Science for Cyber Security and
Risk on the Web. In Proceedings of the Tenth ACM International Conference on Web
Search and Data Mining (Cambridge, United Kingdom) (WSDM ’17). Association
for Computing Machinery, New York, NY, USA, 823–824. doi:10.1145/3018661.
3022760

[64] Ameya Vaidya, Feng Mai, and Yue Ning. 2020. Empirical Analysis of Multi-Task
Learning for Reducing Identity Bias in Toxic Comment Detection. Proceedings
of the International AAAI Conference on Web and Social Media 14, 1 (May 2020),
683–693. doi:10.1609/icwsm.v14i1.7334

[65] Jonathan Vasquez, Carlotta Domeniconi, and Huzefa Rangwala. 2024. DispaRisk:
Auditing Fairness Through Usable Information. arXiv preprint arXiv:2405.12372
(2024).

[66] Bertie Vidgen, Alex Harris, Dong Nguyen, Rebekah Tromble, Scott Hale, and
Helen Margetts. 2019. Challenges and frontiers in abusive content detection. In
Proceedings of the Third Workshop on Abusive Language Online, Sarah T. Roberts,
Joel Tetreault, Vinodkumar Prabhakaran, and Zeerak Waseem (Eds.). Association
for Computational Linguistics, Florence, Italy, 80–93. doi:10.18653/v1/W19-3509
[67] Jesse Vig. 2019. A Multiscale Visualization of Attention in the Transformer Model.
In Proceedings of the 57th Annual Meeting of the Association for Computational
Linguistics: System Demonstrations. Association for Computational Linguistics,
Florence, Italy, 37–42. doi:10.18653/v1/P19-3007

[68] Zeerak Waseem and Dirk Hovy. 2016. Hateful Symbols or Hateful People? Predic-
tive Features for Hate Speech Detection on Twitter. In Proceedings of the NAACL
Student Research Workshop, Jacob Andreas, Eunsol Choi, and Angeliki Lazaridou
(Eds.). Association for Computational Linguistics, San Diego, California, 88–93.
doi:10.18653/v1/N16-2013

[69] Ingmar Weber, Ana-Maria Popescu, and Marco Pennacchiotti. 2013. Data-driven
political science. In Proceedings of the Sixth ACM International Conference on Web
Search and Data Mining (Rome, Italy) (WSDM ’13). Association for Computing
Machinery, New York, NY, USA, 777–778. doi:10.1145/2433396.2433498

[70] Sarah Wiegreffe and Yuval Pinter. 2019. Attention is not not Explanation. In
Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing and the 9th International Joint Conference on Natural Language Pro-
cessing (EMNLP-IJCNLP), Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan
(Eds.). Association for Computational Linguistics, Hong Kong, China, 11–20.
doi:10.18653/v1/D19-1002

[71] Chih-Kuan Yeh, Cheng-Yu Hsieh, Arun Sai Suggala, David I. Inouye, and Pradeep
Ravikumar. 2019. On the (in)fidelity and sensitivity of explanations. Curran
Associates Inc., Red Hook, NY, USA.

[40] Isaac Lage, Emily Chen, Jeffrey He, Menaka Narayanan, Been Kim, Sam Gershman,
and Finale Doshi-Velez. 2019. An evaluation of the human-interpretability of
explanation. arXiv preprint arXiv:1902.00006 (2019).

[41] Q. Vera Liao, Daniel Gruen, and Sarah Miller. 2020. Questioning the AI: Informing
Design Practices for Explainable AI User Experiences. In Proceedings of the 2020
CHI Conference on Human Factors in Computing Systems (Honolulu, HI, USA)
(CHI ’20). Association for Computing Machinery, New York, NY, USA, 1–15.
doi:10.1145/3313831.3376590

[42] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer
Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. RoBERTa: A
Robustly Optimized BERT Pretraining Approach. CoRR abs/1907.11692 (2019).
arXiv:1907.11692 http://arxiv.org/abs/1907.11692

[43] Scott M. Lundberg and Su-In Lee. 2017. A unified approach to interpreting
model predictions. In Proceedings of the 31st International Conference on Neural
Information Processing Systems (Long Beach, California, USA) (NIPS’17). Curran
Associates Inc., Red Hook, NY, USA, 4768–4777.

[44] Christian Meske and Enrico Bunde. 2022. Design Principles for User Interfaces
in AI-Based Decision Support Systems: The Case of Explainable Hate Speech
Detection. 25, 2 (March 2022), 743–773. doi:10.1007/s10796-021-10234-5
[45] Anna Muratova. 2021. Interpretability and Effectiveness of Machine Learning
Methods for Sequence Mining in Various Domains. In Proceedings of the 14th
ACM International Conference on Web Search and Data Mining (Virtual Event,
Israel) (WSDM ’21). Association for Computing Machinery, New York, NY, USA,
1113–1114. doi:10.1145/3437963.3441670

[46] Raymond S Nickerson. 1998. Confirmation bias: A ubiquitous phenomenon in

many guises. Review of general psychology 2, 2 (1998), 175–220.

[47] Forough Poursabzi-Sangdeh, Daniel G Goldstein, Jake M Hofman, Jennifer Wort-
man Wortman Vaughan, and Hanna Wallach. 2021. Manipulating and measuring
model interpretability. In Proceedings of the 2021 CHI conference on human factors
in computing systems. 1–52.

[48] Inioluwa Deborah Raji, Timnit Gebru, Margaret Mitchell, Joy Buolamwini, Joon-
seok Lee, and Remi Denton. 2020. Saving Face: Investigating the Ethical Concerns
of Facial Recognition Auditing. In Proceedings of the AAAI/ACM Conference on AI,
Ethics, and Society (New York, NY, USA) (AIES ’20). Association for Computing
Machinery, New York, NY, USA, 145–151. doi:10.1145/3375627.3375820

[49] Kamalakkannan Ravi and Adan Ernesto Vela. 2024. RICo: Reddit ideological
communities. Online Social Networks and Media 42 (2024), 100279. doi:10.1016/j.
osnem.2024.100279

[50] Kamalakkannan Ravi, Adan Ernesto Vela, Elizabeth Jenaway, and Steven
Windisch. 2023. Exploring Multi-Level Threats in Telegram Data with AI-Human
Annotation: A Preliminary Study. In 2023 International Conference on Machine
Learning and Applications (ICMLA). 1520–1527. doi:10.1109/ICMLA58977.2023.
00229

[51] Kamalakkannan Ravi and Jiann-Shiun Yuan. 2024. Ideological orientation and
extremism detection in online social networking sites: A systematic review.
Intelligent Systems with Applications 24 (2024), 200456. doi:10.1016/j.iswa.2024.
200456

[52] Kamalakkannan Ravi and Jiann-Shiun Yuan. 2025. ThreatGram101: Extreme
Telegram Replies Data with Threat Levels. In Information Management and Big
Data, Juan Antonio Lossio-Ventura, Eduardo Ceh-Varela, Eduardo Díaz, Freddy
Paz Espinoza, Claude Tadonki, and Hugo Alatrista-Salas (Eds.). Springer Nature
Switzerland, Cham, 275–291.

[53] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. 2016. "Why Should I
Trust You?": Explaining the Predictions of Any Classifier. In Proceedings of the
22nd ACM SIGKDD International Conference on Knowledge Discovery and Data
Mining (San Francisco, California, USA) (KDD ’16). Association for Computing
Machinery, New York, NY, USA, 1135–1144. doi:10.1145/2939672.2939778
[54] Koustav Rudra, Niloy Ganguly, Jeanne Mifsud Bonnici, Eric Müller-Budack, and
Ritumbra Manuvie. 2025. Disinformation and Misinformation in the Age of
Generative AI. In Proceedings of the Eighteenth ACM International Conference on
Web Search and Data Mining (Hannover, Germany) (WSDM ’25). Association for
Computing Machinery, New York, NY, USA, 1122–1123. doi:10.1145/3701551.
3705708

[55] Ramit Sawhney, Harshit Joshi, Saumya Gandhi, and Rajiv Ratn Shah. 2021. To-
wards Ordinal Suicide Ideation Detection on Social Media. In Proceedings of the
14th ACM International Conference on Web Search and Data Mining (Virtual Event,
Israel) (WSDM ’21). Association for Computing Machinery, New York, NY, USA,
22–30. doi:10.1145/3437963.3441805

[56] Ramprasaath R. Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedan-
tam, Devi Parikh, and Dhruv Batra. 2020. Grad-CAM: Visual Explanations from
Deep Networks via Gradient-Based Localization. Int. J. Comput. Vision 128, 2
(Feb. 2020), 336–359. doi:10.1007/s11263-019-01228-7

[57] Sofia Serrano and Noah A. Smith. 2019. Is Attention Interpretable?. In Proceedings
of the 57th Annual Meeting of the Association for Computational Linguistics, Anna
Korhonen, David Traum, and Lluís Màrquez (Eds.). Association for Computational
Linguistics, Florence, Italy, 2931–2951. doi:10.18653/v1/P19-1282

[58] Paras Sheth, Raha Moraffah, Tharindu S. Kumarage, Aman Chadha, and Huan
Liu. 2024. Causality Guided Disentanglement for Cross-Platform Hate Speech

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

TRuST-M: Evaluating User Trust and Explainability in LLM-Based
Web Moderation Systems

Kamalakkannan Ravi
Kamalakkannan.Ravi@ucf.edu
University of Central Florida
Orlando, Florida, USA

Hemant Surale
hsurale@uwaterloo.ca
University of Waterloo
Waterloo, Ontario, Canada

Jiann-Shiun Yuan
Jiann-Shiun.Yuan@ucf.edu
University of Central Florida
Orlando, Florida, USA

Abstract
As online social platforms face increasing challenges in moderating
nuanced threats across web communities, trust in automated mod-
eration systems is critical. TRuST-M examines this problem in web
and social-network environments, where moderation occurs under
time pressure and public scrutiny. Large language models (LLMs)
achieve strong classification performance but remain difficult to
interpret, reducing user confidence and accountability in real-world
workflows. This work introduces TRuST-M, a human-centered eval-
uation framework that studies how explanation methods influence
trust, understanding, and perceived effectiveness in LLM-based
threat moderation. The framework integrates a RoBERTa model
pretrained on 1M Telegram posts and fine-tuned on 15,063 labeled
messages across three classes (No Threat, Judicial Threat, Non-
Judicial Threat), achieving 95.8% accuracy, weighted F1 of 0.96,
and Cohen’s kappa of 0.94 on a held-out set. A within-subjects
study (n=31) evaluated six messages of varying complexity with
predictions and three explanation methods: Integrated Gradients,
LIME, and attention visualization. LIME was preferred by 58% of
participants for its intuitive word-level highlights, though longer
response times were noted, while attention visualizations were
rated least helpful due to unclear token emphasis. Statistical analy-
sis revealed positive correlations between explanation clarity, user
trust, and confidence in moderation decisions. We frame TRuST-M
as an interpretable decision-support system for human-in-the-loop
moderation, emphasizing calibrated trust and moderator compre-
hension rather than model replacement. The findings show that
explanation clarity and response time meaningfully shape trust and
decision confidence in AI-assisted moderation, advancing trans-
parent, usable, and trustworthy moderation tools for the social
web.

CCS Concepts
• Human-centered computing → User studies; Empirical stud-
ies in HCI; • Computing methodologies → Natural language
processing; Machine learning; • Security and privacy → Social
aspects of security and privacy; Usability in security and privacy;
• Information systems → Social networks; Decision support
systems.

This work is licensed under a Creative Commons Attribution 4.0 International License.
WSDM Companion ’26, Boise, ID, USA
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2358-2/2026/02
https://doi.org/10.1145/3779211.3793172

Keywords
Explainable AI (XAI), Human–AI interaction, Trust in AI, Content
moderation, Threat detection, Large language models (LLMs), User
study, Social transparency, Decision support, Social networks

ACM Reference Format:
Kamalakkannan Ravi, Hemant Surale, and Jiann-Shiun Yuan. 2026. TRuST-
M: Evaluating User Trust and Explainability in LLM-Based Web Moderation
Systems. In The Nineteenth ACM International Conference on Web Search and
Data Mining (WSDM Companion ’26), February 22–26, 2026, Boise, ID, USA.
ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/3779211.3793172

1 Introduction
The widespread deployment of large language models (LLMs) on
online platforms has created both opportunities and challenges for
large-scale content moderation. These systems can rapidly classify
user-generated content for misinformation, hate speech, and nu-
anced threats [26, 39, 66]. However, their opaque decision-making
makes it difficult for moderators and end users to understand why
decisions are made, raising concerns about accountability, fair-
ness, and public trust [8, 18, 48, 53]. Research shows that users
are more likely to accept or challenge automated decisions when
given clear explanations [19, 22], yet transparency tools remain rare
in moderation workflows, especially in safety-sensitive contexts
where misclassification of political content can cause real harm
[24, 33, 51, 55, 70].

Beyond accuracy, effective deployment requires usable trans-
parency: auditing signals must be actionable and comprehensible
to decision-makers [65]. TRuST-M approaches this need by elevat-
ing explanation clarity as a primary design objective. In social-web
moderation settings, our goal is not to replace human judgment but
to support it—treating explainability and trust as first-class require-
ments in human-in-the-loop decision support. This contributes to
broader efforts toward reliable, transparent moderation practices
in fast-moving web environments.

Many safety-critical AI applications—from clinical decision sup-
port [2, 12, 16, 30, 62] to judicial threat assessment [52]—require
not only accuracy but explanations that users can interpret and act
upon. In content moderation, explanations help verify AI reasoning,
resolve disagreements, and calibrate trust [37, 45, 53]. Yet despite
extensive work in explainable AI (XAI), few techniques have been
evaluated for usability or impact in real-world moderation settings
[43, 56, 59].

Aligning LLM-based moderation with human expectations is
further shaped by trade-offs between accuracy, usability, and in-
terpretability. While gradient-based saliency, perturbation-based
attribution, and attention visualization are common XAI meth-
ods, evidence of their effectiveness for end users remains limited

73WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

[70, 71]. Few studies assess how users interpret these explanations
or whether they meaningfully improve decision outcomes in prac-
tice [3, 41].

We address this gap with TRuST-M (Threat Reasoning and User
Study of Trust in Moderation), a human-centered evaluation of
explainability in LLM-based threat moderation. Our interactive
Total Freedom Interface (TFI) integrates three explanation tech-
niques—gradient saliency, local perturbation via LIME, and atten-
tion visualization—within a RoBERTa classifier for judicial and
non-judicial threats. Our contributions are:

and SHAP [43]. Attention-based explanations have been applied in
NLP [70], though their interpretability remains debated [57].

Despite these advances, relatively few studies apply XAI directly
to real moderation workflows. Existing work exploring user trust
with post-hoc explanations [4, 44] rarely considers politically sen-
sitive or high-stakes scenarios. Similarly, Ravi and Vela [49] used
attention maps for ideology classification but did not evaluate us-
ability or satisfaction. To date, no prior work has systematically
evaluated how end users interpret diverse explanations during ac-
tual threat moderation tasks.

• A practical trust–explainability evaluation framework embed-
ded in a live moderation interface, integrating complemen-
tary attribution views and mapping them to measured trust,
usability, and perceived effectiveness.

• A within-subjects user study (n=31) quantifying how expla-
nation clarity, response time, and format affect trust, usabil-
ity, and moderation behavior.

• Statistical evidence linking explanation clarity to trust, and
trust to perceived moderation effectiveness, independent of
demographic factors.

• Actionable design guidelines: (a) prioritize low–cognitive-
load visualizations; (b) ensure response times support real-
time decisions; (c) explore hybrid explanation formats that
combine complementary strengths.

2 Related Work
Our work builds on three interconnected research areas: (1) LLM-
based threat detection in NLP, (2) explainable AI (XAI) for content
moderation, and (3) human-centered evaluation of trust in AI sys-
tems. We contribute a user-facing system that integrates multiple
explanation techniques, empirically measures their impact on trust
and decision-making, and provides actionable design guidance for
practitioners. Below, we review each area and identify the research
gaps addressed in this study.

2.1 LLM-Based Threat Detection (NLP Domain)
Large language models (LLMs) have significantly advanced au-
tomated online content moderation, including detection of hate
speech, misinformation, and threats [26, 39, 66]. LLMs often out-
perform traditional classifiers [51], yet remain susceptible to over-
generalization, cultural bias, and misclassification—particularly in
politically sensitive or ambiguous contexts [23, 27, 48].

Most prior work focuses on binary or coarse-grained tasks such
as hate speech [17, 68], toxic language [64], or cyber threats [6].
Far fewer studies address nuanced threat categories such as politi-
cally motivated or judicial threats [28, 32, 69]. Ravi and Yuan [52]
proposed a taxonomy for legal threat classification, but adoption
remains limited due to the lack of domain-specific guidance for
training LLMs in sensitive threat contexts.

2.2 Explainability for Content Moderation (XAI

Domain)

Explainable AI (XAI) methods aim to improve transparency in
model predictions. Common techniques include gradient-based
saliency maps [59], perturbation-based methods such as LIME [53],

2.3 Human-Centered Evaluation and Trust (HCI

Domain)

Interpretability is both a technical and human-centered challenge,
involving usability, comprehension, and trust calibration [19, 29, 41].
Ehsan et al. [22] highlight the need for social-science-informed eval-
uation. In safety-critical domains such as healthcare and criminal
justice, studies show that explanation format influences decision-
making, disagreement resolution, and appropriate reliance on AI
[10, 35].

In content moderation, comparable empirical research is scarce
despite similarly high stakes [54, 58, 61]. Recent work on bias and
fairness emphasizes that usable transparency is essential for account-
able decision support [9]. Our study operationalizes this perspective
by treating trust and explanation clarity as measurable constructs
within interactive moderation interfaces. Trust in AI is shaped by ex-
planation complexity, message ambiguity, and user characteristics
[3, 33], yet few controlled studies isolate these factors in politically
sensitive threat detection. Existing findings seldom translate into
actionable interface-level design recommendations [7, 20, 63].

Our focus is the social-web moderation setting (Telegram), where
we evaluate interpretable, human-in-the-loop decision support for
moderators.

3 Problem Statement
We evaluate how different explanation techniques influence user
trust, satisfaction, and accuracy in AI-assisted threat detection and
content moderation. Building on the gaps identified in Related Work,
we formalize three research gaps:

RG 1 – Domain-Specific Threat Detection Models. We de-
velop a custom pretrained and fine-tuned RoBERTa-based classifier
for nuanced threats (judicial and non-judicial), incorporating tar-
geted task framing, dataset design, and labeling strategies to reduce
ambiguity and improve interpretability (see Task, Data, and Model).
RG 2 – Real-World Evaluation of XAI in Moderation. We
conduct a within-subject user study using the Total Freedom In-
terface (TFI) to examine how explanation complexity, message
ambiguity, and user characteristics affect trust, satisfaction, and
classification accuracy in high-stakes moderation scenarios (see
User Study Experiment).

RG 3 – Interface-Level Design Guidance for Trust. We ana-
lyze behavioral data and participant feedback to derive actionable
design guidelines for trustworthy moderation interfaces, linking
empirical findings to deployment-oriented strategies (see Evalua-
tion Results).

74TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

By addressing these gaps, we assess how explanation methods
shape trust, usability, and effectiveness in AI-assisted moderation,
and we provide grounded design recommendations and limita-
tions—expanded in Evaluation Results and Discussion. Our main
contribution is an evaluation and design framework that operational-
izes trust and explanation clarity for human-in-the-loop moderation
on the social web.

4 Task, Data, and Model
To address the research gaps identified above, we designed a refined
threat-classification task, compiled a domain-specific dataset, and
developed a custom-pretrained and fine-tuned LLM classifier to
serve as the foundation for the user study.

4.1 Task: Refined Threat Detection
Prior moderation research often relies on coarse categories such as
normal, hate, or offensive speech [17]. While effective for broad fil-
tering, such taxonomies lack the nuance needed to capture political
rhetoric and implicit calls for violence that characterize contem-
porary online discourse [5]. Newer multi-level schemes add nu-
ance but frequently blur boundaries between lawful and unlawful
rhetoric [50].

To address this, we adopt a three-class taxonomy [52]:

(1) No Threat: Strongly worded but non-harmful expressions

(e.g., “Live free or die”).

(2) Judicial Threat: Advocacy for legal or punitive action (e.g.,

“Lock her up”).

(3) Non-Judicial Threat: Direct or implied calls for unlawful
violence (e.g., “It’s time to start a civil war”). Mixed cases
default to this class for severity.

This taxonomy provides a clearer separation between lawful-
punitive and unlawful threats while remaining simple enough for
consistent annotation and user interpretation in politically sensitive
moderation contexts.

4.2 Data
To ensure ideological breadth, we collected Telegram channels from
both far-left and far-right communities, though far-right content
predominated due to higher posting volume. This imbalance may
skew predictions and increase false positives for certain ideological
groups, a limitation we acknowledge and discuss in our ethical con-
siderations. Future iterations will explore channel-level stratified
sampling, post-stratification reweighting, and robustness checks
across ideological slices to assess stability under distributional shift.
The full dataset contains 2.3M replies, of which 15,076 were
annotated into No Threat, Judicial Threat, or Non-Judicial Threat
classes using criminology-informed guidelines. After refinement to
resolve borderline cases, 15,063 labeled examples remained. This
dataset was selected for its rich coverage of politically charged and
grievance-driven discourse [11], providing a realistic testbed for
evaluating moderation in high-risk contexts.

4.3 Modeling
The 15,063 labeled examples were divided into training (10,554),
development (2,248), and test (2,261) splits using class-stratified

sampling. We used RoBERTa, a robust transformer architecture
with strong performance across NLP tasks [42]. To capture platform-
specific language and conversational patterns, we first pretrained
RoBERTa on 1M unlabeled Telegram replies (12,260 steps; ≈137
hours), followed by fine-tuning on the labeled set for 100 epochs
(≈168 hours).

The resulting model achieved 95.8% accuracy, weighted F1 of 0.96,
and Cohen’s kappa of 0.94 on the held-out test set, demonstrating
high agreement and strong reliability despite class imbalance and
linguistic ambiguity. These properties provide a stable foundation
for evaluating explanation quality and user trust in our subsequent
user study.

5 User Study Experiment
The experiment evaluated how explainability-enhanced AI threat
detection influences Trust (T), perceived Explainability (E), Usability
(U), and Moderation Confidence (MC) when users classify polit-
ically sensitive web and social-network content. Specifically, we
examined whether combining predictions, confidence scores, and
explanations improves user understanding and decision confidence
in high-stakes moderation scenarios.

Unlike prior work focused primarily on classification accuracy
[31, 39], our study investigates human–AI interaction and user
responses to different explanation types [22, 41, 47]. Although ex-
plainability has been examined in domains such as finance and
healthcare, its role in online moderation—especially for ambiguous
threats—is underexplored [1, 13]. We address this gap through an
empirical evaluation of how three explanation methods shape trust,
judgment confidence, and overall user experience.

Using a within-subjects design, participants classified six mes-
sages under three conditions: no explanation (baseline), a single
explanation method, and all three methods. Each message belonged
to one of the classes No Threat, Judicial Threat, or Non-Judicial
Threat. After completing the tasks, participants filled out a System
Usability Scale (SUS) survey and provided qualitative feedback.

5.1 Participants
We recruited 31 participants (15 female, 16 male), aged 18–44,
through flyers and word-of-mouth. Six participants held PhDs, two
held Master’s degrees, and five held Bachelor’s degrees. Thirteen
participants had prior moderation experience, including two pro-
fessional moderators. AI familiarity was high: 44% (N=14) were
somewhat familiar, 34.3% (N=11) very familiar, and 19% (N=6) unfa-
miliar. Most had never used XAI tools (81.2%). All participants were
active users of web and social-network platforms but unfamiliar
with the explanation methods tested. Each participant received a
$10 gift card upon completion.

5.2 Explainable AI Interface
We developed the Total Freedom Interface (TFI), a custom web-
based application implemented in Python using Streamlit v1.46.1
[60]. TFI integrates the RoBERTa threat classifier (Section 4.3) with
three qualitatively different explanation techniques:

• XAI Method 1 – Integrated Gradients [36]: A gradient-
based attribution method that computes path-integrated gra-
dients to identify influential tokens.

75WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

• XAI Method 2 – LIME (Local Interpretable Model-agnostic
Explanations) [53]: A perturbation-based technique that
estimates feature importance via local surrogate models; in-
tuitive but computationally more expensive.

• XAI Method 3 – Final-Layer Attention Visualization
[67]: A visualization of last-layer attention weights. While
attention is debated as a faithful explanation [34, 57, 70], it
serves as a widely recognized baseline.

To avoid framing effects, these were shown (see Figure 1) under
anonymized labels (XAI Method 1–3). In this study, the method–label
mapping remained fixed; future replications will randomize these
mappings.

Participants selected pre-loaded Telegram replies from the test
set and triggered the model’s prediction. The classifier output
one of three labels—No Threat, Judicial Threat, or Non-Judicial
Threat—with distinct color-coded cues. Each explanation method
used its own visualization (e.g., heatmaps, bar charts, token high-
lighting). The interface recorded total interaction time per message,
serving as a coarse measure of cognitive effort.

TFI included usability accommodations such as dark mode, large
fonts, and a responsive layout. At the end of the experiment, the
system exported session logs for analysis.

5.3 Procedure
The experiment lasted about 30 minutes and followed a three-stage
protocol:

(1) Onboarding and Demonstration (5 minutes): Partici-
pants received a brief overview of the study, viewed a live
demonstration with a neutral example, and were warned
about politically sensitive content. The three explanation
methods were introduced at a high level.

(2) Task Execution (10–15 minutes): Participants classified
six messages. For each message, they viewed the prediction
and examined all three anonymized explanation methods.
Interaction time was logged for each message.

(3) Survey and Feedback (10 minutes): Participants com-
pleted the System Usability Scale (SUS) and provided ratings
of explainability, trust, model preference, and moderation
confidence. Open-ended feedback captured suggestions for
improvement.

All interaction logs and survey data were anonymized and stored
on secure university-maintained systems. No personally identifiable
information was collected. The anonymized dataset will be publicly
released to support reproducibility.

5.4 Task Design
Each participant evaluated six pre-loaded Telegram replies—two
per class (No Threat, Judicial Threat, Non-Judicial Threat). For each
class, one message was designated “easy” and one “hard” based
on annotator experience. Easy messages contained explicit threat
markers and unanimous annotator agreement; hard messages con-
tained implicit, sarcastic, or context-dependent language requiring
guideline consultation. Message order was fixed for all participants
to maintain consistent difficulty progression and reduce learning
effects.

For each message, participants followed a standardized workflow
in TFI: click Start Timer, select a message, trigger Predict, review
the model’s classification, examine all three explanation methods,
and click End Timer. Figure 1 illustrates the interface.

After completing all six messages, participants exported a CSV

log of interaction times.

5.4.1 Measaurements. We collected both objective and subjective
measures to analyze how the three XAI methods influenced partici-
pant decision-making. Five measures were used:

• Interaction Time: Total time per message, from Start Timer
to End Timer, including prediction and examination of all
explanation methods.

• Trust in AI: Post-task rating of confidence in the model’s

threat classification (1–5 scale).

• Perceived Explainability: Participant ratings of how well

each explanation clarified the model’s reasoning.

• Moderation Effectiveness: Participant perceptions of how

well the tool supported moderation decisions.

• System Usability: A 19-item usability assessment capturing

ease of use, efficiency, and satisfaction.

In total: 6 messages × 3 explanation methods = 18 explanation in-
teractions per participant, in addition to six time-logged prediction
tasks and four categories of subjective ratings.

6 Evaluation Results
We now present the results of our user study evaluating the impact
of three explanation techniques—Integrated Gradients, LIME, and
attention visualization—on trust, usability, and classification effec-
tiveness in AI-assisted threat moderation. All quantitative metrics
and subjective evaluations are based on data from 31 participants;
statistical tests and visualizations use the cleaned dataset described
below.

6.1 Data Preparation and Cleaning
We first removed trials with incomplete sessions or invalid logs (e.g.,
missing End Timer clicks). For each participant, extreme interaction-
time outliers (more than three standard deviations from that par-
ticipant’s mean) were excluded to reduce the impact of distraction
or disengagement. Across all sessions, fewer than 4% of trials were
dropped due to data quality concerns. The final dataset comprised
31 participants × 6 messages × 3 explanation views = 558 explana-
tion interactions, plus 186 timed classification tasks and 31 sets of
post-task survey responses.

6.2 Analysis Overview
We used non-parametric chi-squared and Mann–Whitney tests
to examine within-subject effects of explanation type and mes-
sage difficulty on trust, explainability, and moderation confidence.
When appropriate, post hoc pairwise comparisons (e.g., Tukey HSD)
were used to identify differences between explanation techniques,
and Greenhouse–Geisser or Huynh–Feldt corrections were applied
when sphericity assumptions were violated.

For interaction time, we assessed normality using Shapiro–Wilk
tests. When normality was violated, we applied a log transforma-
tion before running ANOVA and pairwise 𝑡-tests with Bonferroni

76TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Figure 1: Annotated screenshot of the Total Freedom Interface (TFI) showing LIME-based explanation (XAI Method 2). Key
components include: (Input Text), (Prediction), (XAI Selection), (Prediction Score), (Candidate Words & Contributions), and
(Influential Words). Participants sequentially trigger predictions and explore explanations.

Figure 2: Mean interaction times by threat example (error
bars represent standard deviation).

corrections. We used Spearman’s 𝜌 for association tests because
(i) Likert-type ratings are ordinal and (ii) residuals for several mea-
sures deviated from normality; Spearman correlation is robust un-
der these conditions.

Figure 3: Mean Likert ratings aggregated by usability, trust,
explainability, and confidence in moderation decisions (error
bars represent standard deviation).

77WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

Figure 4: Aggregated user ratings for Trust (TQ1–TQ3), Explainability (EQ1–EQ3), and Moderation Confidence (MQ1–MQ3).
Error bars indicate standard deviation.

6.3 Interaction Time
Average interaction time per message varied by example and dif-
ficulty (Figure 2), with statistically significant differences across
pairs. As expected, “easy” tasks generally took less time than “hard”
ones, except for judicial threats.

For example, an easy No-Threat task averaged 112.5 seconds,
compared to 160.3 seconds for its harder counterpart—a difference
of 43.8 seconds. In contrast, the “easy” judicial threat took longer
than its harder counterpart, suggesting additional verification in
severe cases. All differences were significant (p<0.05).

The increased time on the “easy” judicial threat may reflect a con-
firmation–verification effect: when content appears clearly severe,
participants may invest extra time to double-check the AI’s output
before accepting it. This is consistent with work on confirmation
bias and decision-making under emotionally charged evidence [46],
as well as findings that even straightforward explanations can lead
users to spend more time validating model reasoning [40].

6.4 Trust and Explainability
Subjective ratings of trust and explainability were collected on a
5-point Likert scale (5 = highest). Overall, participants reported
relatively high ratings for both, with averages around 4.2. Figure 3
shows the mean trust and explainability scores aggregated across
all explanation methods.

To test whether explanation clarity is associated with trust in
the model, we ran a Spearman rank-order correlation. We observed
a positive, statistically significant association between trust and
explanation clarity (𝜌 = 0.493, 𝑝 = 0.005), indicating a moderate,
monotonic relationship (see Figure 5). In other words, participants
who perceived the explanations as clearer also tended to report
higher trust in the system.

6.5 Usability
Participants rated the interface as easy to understand and operate,
with usability receiving the highest aggregated scores (mean = 4.27,
SD = 0.56). The main complexity, according to comments, stemmed
from interpreting the explanation methods themselves rather than
from basic navigation or controls.

We used a 19-item standardized usability assessment to evaluate
overall usability. All participants reported that the interface was
easy to use and did not interfere with their interaction flow. Usabil-
ity showed increasing correlations with Trust (𝜌 = 0.38, 𝑝 < 0.05),
Explainability (𝜌 = 0.57, 𝑝 < 0.01), and Moderation Confidence
(𝜌 = 0.72, 𝑝 < 0.01), suggesting that while usability alone does
not guarantee trust, it is an important enabling factor for effective
decision support.

6.6 Moderation Effectiveness
Participants also rated how helpful the tool was for real-world
content moderation. As shown in Figure 3, moderation effective-
ness scores were slightly lower on average than trust, usability,
and explainability, although these differences were not statistically
significant.

Moderation effectiveness was strongly correlated with trust
(𝜌 = 0.62, 𝑝 < 0.01) and explainability (𝜌 = 0.66, 𝑝 < 0.01), in-
dicating that participants who trusted the model more and found
explanations clearer also felt more confident using the tool for mod-
eration decisions. Education level was associated with usability
satisfaction: 83% of PhD respondents rated the system “Excellent”
or “Best Imaginable,” compared to 50% of Bachelor’s degree holders
who rated it “Good” or “Fair” (𝜒 2 (6, 𝑁 = 31) = 20.99, 𝑝 < 0.05).
No significant effects were found for gender, age, or prior AI/ML
experience.

78TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Overall, 58% of participants (18/31) preferred Method 2; the remain-
ing methods collectively accounted for the rest (∼6/31).

Interest in Hybrid Explanations. A smaller subset of participants
suggested that combining methods could improve interpretability.
For instance, P13 remarked:

“If you combine methods 2 and 3, it would be easier
for general people to interpret the outputs of the tool.
Because plots are always easy and quick to evaluate
and compare, and it doesn’t take a long time to read
passages like what happens in method one.”

This comment about general people hints that explanation pref-
erences may vary with background and familiarity, reinforcing
the quantitative finding that education level influences usability
perceptions.

Demographic Effects on Usability. Consistent with the quantita-
tive analysis, qualitative responses suggested that users with more
advanced education or analytical training were more comfortable
with the interface and explanations. As noted earlier, education
level was significantly associated with overall experience ratings
(𝜒 2 (6, 𝑁 = 31) = 20.99, 𝑝 < 0.05). However, due to unbalanced
group sizes, we could not reliably infer how prior experience with
moderation tools or AI/ML systems affected trust, explainability,
or moderation confidence.

Limitations of Method 3 (Attention Visualization). Partici-
pants frequently criticized Method 3 for confusing scores and un-
clear token importance. P22 wrote:

“XAI Method 3 was the least helpful as it did not give
the more important words greater attention scores.”

Similarly, P19 and P20 raised concerns about emphasis on non-
informative tokens:

“[...] XAI Method 3 was often giving higher attention
to special tokens like inverted commas, which can be
worked upon since they are not always the most infor-
mative tokens.” — P19
“Model 3 would constantly return high values for words
that don’t seem relevant at all to the threat.” — P20

P27 suggested that adding more detail on why specific tokens
were highlighted could help make this method more understand-
able.

Together, these findings indicate that improving the responsiveness
of Method 2 and refining the interpretability of Method 3 could
further enhance user experience and strengthen confidence in AI-
assisted moderation.

7 Discussion
Our findings reinforce prior work in explainable AI (XAI) and
human–AI interaction by showing that explanation quality directly
influences user trust and perceived effectiveness in moderation
tasks. In line with Ehsan et al. [22] and Liao et al. [41], we observed
a statistically significant positive correlation between perceived
explanation clarity and trust in the system (𝜌 = 0.493, 𝑝 = 0.005).
This suggests that the interpretability of model outputs remains a
central factor in user acceptance of AI-assisted decisions, even when
underlying model accuracy is high (accuracy = 95.8%, F1 = 0.96).

Figure 5: Spearman correlation among usability, trust, ex-
plainability, and confidence in moderation decisions (corre-
lation coefficients shown in cells).

These patterns suggest that domain-specific familiarity and ana-
lytical comfort may influence how users experience the interface,
potentially more than general AI literacy. To mitigate risks of bias
or misuse, we recommend that any deployment pair this type of
tool with human oversight, fairness audits, and context-specific
training.

6.7 Qualitative Feedback
We conducted a thematic analysis of open-ended responses and
grouped them into recurring themes.

Preference for Method 2 (LIME). Participants generally pre-
ferred simpler, color-coded visualizations over dense or text-heavy
explanations. Many expressed confusion when different methods
highlighted different tokens for the same message, suggesting the
value of explanation alignment.

When asked which explanation method was most or least helpful,
there was a strong inclination toward Method 2, which provided
color-coded highlights and ranked word importance. For example,
P23 noted:

“Method 2 was the most helpful, as it clearly separated
the words that were important for the label given.”

Similarly, P3 commented:

“Model 2 was good because it clearly highlighted the
words that were important, and it used a darker high-
light to signify more importance or emphasis (which
was easy to recognize), and also the explanation of rank-
ing words from top to bottom in terms of how much they
fit what the model was looking for helped understand
things very clearly.”

At the same time, several participants raised concerns about

response time for Method 2. As P10 put it:

“Faster XAI method 2 implementation would help [for
a] real-world use case.”

79WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

In this way, RG 1 is addressed not only at the model-performance
level but also in a trust-sensitive evaluation setting.

7.1 Explanation Method Performance
Participants’ strong preference for the perturbation-based method
(LIME, Method 2) highlights the value of intuitive, word-level visual-
izations for threat moderation. This aligns with Poursabzi-Sangdeh
et al. [47], who found that simpler, localized explanations can im-
prove users’ reasoning about model outputs. These results speak
directly to RG 2 by providing a within-subject, realistic comparison
of multiple explanation types under identical task conditions.

Latency concerns raised by several participants indicate that
computational cost remains a barrier to real-time deployment, con-
tributing to RG 3 by emphasizing the need for responsiveness in
trustworthy moderation interfaces [38].

The limited utility of attention-based visualizations (Method 3)
goes beyond user unfamiliarity and reflects structural weaknesses
in raw attention interpretability. Prior critiques [57, 70] note that
attention weights may not align with causal reasoning; in our study,
this manifested as misleading salience on low-value tokens. Includ-
ing Method 3 served as both a baseline and a targeted test of these
critiques in a high-stakes setting, further advancing RG 2 by ex-
amining diverse explanation strategies—even those with known
limitations—in realistic conditions. In practice, pairing attention
with plain-language legends and token filtering aligns with broader
principles of usable transparency, ensuring that explanation arti-
facts are understandable and actionable rather than merely available
[65].

7.2 Trust, Usability, and Moderation Confidence
Trust and perceived moderation effectiveness were highly corre-
lated (𝜌 = 0.62, 𝑝 < 0.01), supporting Jacovi and Goldberg’s [33]
assertion that trust is closely tied to perceived task success. This
addresses RG 2 by linking explanation clarity and user trust to
measurable, task-level outcomes in a high-stakes, web-based mod-
eration setting.

Usability emerged as a necessary but not sufficient condition
for trust. The TFI received high usability ratings (mean = 4.27), yet
trust varied more strongly with explanation clarity than with ease
of use. This distinction reinforces that usability and interpretability
are orthogonal design dimensions [41], directly informing RG 3
by suggesting that interface design must explicitly support sense-
making, not only efficient interaction.

7.3 Human Factors in Moderation
7.3.1 Cognitive Effort and Task Complexity. Interaction-time anal-
ysis showed that message difficulty significantly influenced cog-
nitive effort, except in the “easy” judicial-threat category, where
participants still spent more time despite lower classification com-
plexity. This likely reflects verification behavior: when content
appears clearly severe, moderators may extend review time to
confirm correctness—consistent with confirmation-bias effects in
decision-making [46]. In high-stakes contexts, even clear-cut cases
can prompt additional scrutiny due to perceived risk.

This finding supports RG 2 by illustrating how real-world am-
biguity and perceived severity shape explanation use, even when

objective task difficulty is low. From a design standpoint, it con-
tributes to RG 3 by suggesting tiered interaction modes: latency-
sensitive “quick review” flows for routine cases and richer “deep
review” flows for high-impact or ambiguous content, potentially
combined with explicit system-confidence cues to help moderators
balance speed and thoroughness.

7.3.2 Demographic Effects. Education level correlated positively
with usability satisfaction: 83% of PhD respondents rated the system
as “Excellent” or “Best Imaginable,” compared to 50% of Bachelor’s
degree holders (𝜒 2 (6, 𝑁 = 31) = 20.99, 𝑝 < 0.05). No significant
differences appeared in trust or explainability ratings by gender,
age, or prior AI/ML tool experience. This contrasts with domains
where AI familiarity improves trust calibration [19, 29], suggesting
that moderation performance may depend more on domain-specific
knowledge (e.g., platform policies, threat typologies) than general
AI literacy. Several non-technical participants with prior modera-
tion experience reported high confidence interpreting explanations,
while technically skilled but moderation-inexperienced participants
described occasional uncertainty.

This outcome further supports RG 2 by indicating that domain-
specific familiarity—not just AI literacy—shapes moderator perfor-
mance and satisfaction. It also has practical implications for RG 3,
underscoring the value of onboarding and training that emphasize
platform policies and threat taxonomies, rather than relying solely
on generic AI education.

7.4 Design Implications
Our results yield actionable guidelines for explainable moderation
tools, representing direct outputs of RG 3 as concrete, deployable
recommendations:

• Prioritize simple, local visualizations. Participants re-
sponded best to visualizations that clearly highlight relevant
words and avoid visual clutter. Designs that make impor-
tance cues immediately visible scored highest for both trust
and usability.

• Treat latency as a first-class design constraint. Even
strong explanations lose value if slow to load. The slower
response time of the preferred method (LIME) suggests that
in fast-paced moderation, latency can directly affect engage-
ment, workflow continuity, and ultimately trust.

• Adopt hybrid explanation strategies. Some participants
proposed combining the clarity of word-level highlights with
lightweight visual overviews. Hybrid approaches may miti-
gate the limitations of individual methods and better serve
heterogeneous user needs.

• Match explanation depth to risk. For legally sensitive or
high-impact content, moderators often spend extra time veri-
fying even straightforward cases. Providing tiered modes—such
as quick review for routine items and deep review for critical
or ambiguous ones—can help align explanation depth and
interaction time with task criticality.

By operationalizing explanation clarity, trust, and moderator
usability in a live web context, TRuST-M advances algorithmic
transparency and fairness [22] objectives for systems deployed on
social-network platforms, in line with broader efforts toward inter-
pretable, human-aligned AI on the social web.

80TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

7.5 Limitations and Future Work
This study involved a modest participant pool (𝑛 = 31), with
only two professional moderators, which limits generalization to
expert-heavy or large-scale operational environments. The under-
representation of domain experts affects RG 2 and RG 3, and broader
evaluation is needed to validate these findings. In future work, we
plan to scale to cohorts of >50 moderators across multiple platforms
to strengthen external validity and expert coverage.

The fixed-order presentation of six messages, while providing
consistent difficulty progression, may have introduced order effects.
Future studies should use randomized or counterbalanced designs
and randomize both message order and the mapping of anonymized
XAI labels to methods to remove residual framing effects.

Demographic analysis showed that higher education levels were
associated with greater usability satisfaction, while prior AI or
moderation-tool experience did not significantly affect trust or
explainability ratings. This diverges from other domains [19, 29],
and targeted recruitment of professional moderators could clarify
whether cognitive framing, risk perception, or task-specific heuris-
tics drive this pattern.

Our saliency, perturbation, and attention-based explanations
are complementary to other interpretability families, such as logic-
based or symbolic surrogates that translate black-box reasoning
into human-understandable rule sets [25]. Integrating such neuro-
symbolic or rule-inductive approaches in moderation UIs may en-
hance global interpretability and policy alignment, but this remains
outside the current experimental scope.

Several participants noted slower response times for the perturba-
tion based method (LIME, Method 2), highlighting the need to explic-
itly assess latency in real-time workflows. Attention-based visualiza-
tions (Method 3) consistently underperformed in perceived useful-
ness and clarity, likely due to misleading emphasis on non-semantic
tokens—a limitation documented in prior NLP interpretability re-
search [34, 57, 70]. Its inclusion here served as both a baseline and
an empirical validation of these critiques in high-stakes modera-
tion (RG 2). Future work should quantify latency impacts, optimize
computation pipelines, and refine attention-based methods via con-
textual weighting, token filtering, or hybrid strategies.

Finally, as this work was conducted in a controlled, single-session
lab setting, longitudinal field deployments in operational environ-
ments are needed to assess how trust, accuracy, and explanation
preferences evolve with sustained, high-volume, and contextually
diverse threat exposure. Such deployments would extend RG 3 by
examining how design guidelines hold up under real-world work-
load, policy change, and adversarial adaptation.

8 Conclusion
This paper introduced TRuST-M, a framework for evaluating how
explanation methods shape user trust, usability, and perceived
effectiveness in LLM-based threat moderation. Using a domain-
adapted RoBERTa classifier and three complementary explanation
techniques—gradient-based saliency, LIME, and attention visualiza-
tion—we conducted a within-subjects study to examine moderation
decisions in a social-web setting. Explanation clarity showed a
significant positive correlation with trust (𝜌 = 0.493, 𝑝 = 0.005),
LIME’s localized highlights were preferred by 58% of participants

despite latency costs, and trust aligned closely with perceived mod-
eration effectiveness (𝜌 = 0.62, 𝑝 < 0.01). Usability alone did not
guarantee trust, underscoring the importance of interpretable, cog-
nitively lightweight visualizations.

We recommend prioritizing explanation formats that minimize
cognitive load, reducing latency for real-time workflows, and explor-
ing hybrid strategies that combine complementary strengths. Future
work should validate these findings with larger and more expert-
diverse cohorts, and through longitudinal deployments in opera-
tional moderation pipelines to refine explanation design and estab-
lish standards for transparent, accountable AI. Extending TRuST-M
toward fairness-aware and globally interpretable evaluation rep-
resents a promising direction for aligning automated moderation
tools with real-world policy and practitioner needs.

Overall, TRuST-M positions explainability as an interpretable
decision-support layer for web and social-network moderation, aligned
with ongoing efforts to build transparent, trustworthy, and respon-
sibly deployed AI systems.

Ethical Considerations
This study received University IRB approval (ID: STUDY0000ZZ00)
under secondary data analysis. All model-development data were
drawn from publicly accessible Telegram channels without collect-
ing personally identifiable information. The dataset contained both
far-right and far-left sources, though far-right content was more
prevalent; this imbalance is acknowledged as a limitation (see Data
section).

Participants were briefed using a neutral demonstration mes-
sage, provided an explicit content warning, and were encouraged to
ask questions throughout to safeguard well-being. Interaction logs,
timing data, and survey responses were anonymized and stored
securely on university systems. All anonymized data and analy-
sis code will be released to support reproducibility (see Procedure
section).

While TRuST-M aims to strengthen trust and usability in AI-
assisted moderation, we note potential risks, including over-reliance
on automated outputs or inadvertent suppression of lawful speech
and emphasize the need for human oversight in deployment (see
Moderation Effectiveness). For real-world implementations, we rec-
ommend integrating lightweight bias-visualization modules [14]
and adopting reproducible evaluation and unlearning checklists to
ensure ongoing fairness and accountability [15, 21].

References
[1] Muhammad Ali, Piotr Sapiezynski, Aleksandra Korolova, Alan Mislove, and
Aaron Rieke. 2021. Ad Delivery Algorithms: The Hidden Arbiters of Political
Messaging. In Proceedings of the 14th ACM International Conference on Web Search
and Data Mining (Virtual Event, Israel) (WSDM ’21). Association for Computing
Machinery, New York, NY, USA, 13–21. doi:10.1145/3437963.3441801

[2] Ali Amini, Mohammad Alijanpour, Behnam Latifi, and Ali Motie Nasrabadi. 2025.
ADHDeepNet From Raw EEG to Diagnosis: Improving ADHD Diagnosis through
Temporal-Spatial Processing, Adaptive Attention Mechanisms, and Explainability
in Raw EEG Signals. arXiv preprint arXiv:2509.08779 (2025).

[3] Siddhant Arora, Danish Pruthi, Norman Sadeh, William W. Cohen, Zachary C.
Lipton, and Graham Neubig. 2022. Explain, Edit, and Understand: Rethinking
User Study Design for Evaluating Model Explanations. Proceedings of the AAAI
Conference on Artificial Intelligence 36, 5 (Jun. 2022), 5277–5285. doi:10.1609/aaai.
v36i5.20464

[4] Marzieh Babaeianjelodar, Gurram Poorna Prudhvi, Stephen Lorenz, Keyu Chen,
Interpretable

Sumona Mondal, Soumyabrata Dey, and Navin Kumar. 2022.

81WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Ravi, Surale, and Yuan

and High-Performance Hate and Offensive Speech Detection. In HCI Interna-
tional 2022 – Late Breaking Papers: Interacting with eXtended Reality and Artificial
Intelligence, Jessie Y. C. Chen, Gino Fragomeni, Helmut Degen, and Stavroula
Ntoa (Eds.). Springer Nature Switzerland, Cham, 233–244.

[5] Babak Bahador. 2023. Monitoring hate speech and the limits of current definition.
In Challenges and perspectives of hate speech research, Christian Strippel, Sünje
Paasch-Colberg, Martin Emmer, and Joachim Trebbe (Eds.). Digital Communica-
tion Research, Vol. 12. Berlin, 291–298. doi:10.48541/dcr.v12.17

[6] Vahid Behzadan, Carlos Aguirre, Avishek Bose, and William Hsu. 2018. Corpus
and Deep Learning Classifier for Collection of Cyber Threat Indicators in Twitter
Stream. In 2018 IEEE International Conference on Big Data (Big Data). 5002–5007.
doi:10.1109/BigData.2018.8622506

[7] Ghazaleh Beigi, Ruocheng Guo, Alexander Nou, Yanchao Zhang, and Huan Liu.
2019. Protecting User Privacy: An Approach for Untraceable Web Browsing
History and Unambiguous User Profiles. In Proceedings of the Twelfth ACM Inter-
national Conference on Web Search and Data Mining (Melbourne VIC, Australia)
(WSDM ’19). Association for Computing Machinery, New York, NY, USA, 213–221.
doi:10.1145/3289600.3291026

[8] Reuben Binns, Max Van Kleek, Michael Veale, Ulrik Lyngs, Jun Zhao, and Nigel
Shadbolt. 2018. ’It’s Reducing a Human Being to a Percentage’: Perceptions of Jus-
tice in Algorithmic Decisions. In Proceedings of the 2018 CHI Conference on Human
Factors in Computing Systems (Montreal QC, Canada) (CHI ’18). Association for
Computing Machinery, New York, NY, USA, 1–14. doi:10.1145/3173574.3173951
[9] Ludovico Boratto, Stefano Faralli, Mirko Marras, and Giovanni Stilo. 2023. Fourth
international workshop on algorithmic bias in search and recommendation (bias
2023). In European Conference on Information Retrieval. Springer, 373–376.
[10] Adrian Bussone, Simone Stumpf, and Dympna O’Sullivan. 2015. The Role of
Explanations on Trust and Reliance in Clinical Decision Support Systems. In 2015
International Conference on Healthcare Informatics. 160–169. doi:10.1109/ICHI.
2015.26

[11] Hongliu Cao. 2025. Writing Style Matters: An Examination of Bias and Fairness in
Information Retrieval Systems. In Proceedings of the Eighteenth ACM International
Conference on Web Search and Data Mining (Hannover, Germany) (WSDM ’25).
Association for Computing Machinery, New York, NY, USA, 336–344. doi:10.
1145/3701551.3703514

[12] Yuyan Chen, Jin Zhao, Zhihao Wen, Zhixu Li, and Yanghua Xiao. 2024. Tem-
poralMed: Advancing Medical Dialogues with Time-Aware Responses in Large
Language Models. In Proceedings of the 17th ACM International Conference on Web
Search and Data Mining (Merida, Mexico) (WSDM ’24). Association for Computing
Machinery, New York, NY, USA, 116–124. doi:10.1145/3616855.3635860

[13] Philipp Christmann, Rishiraj Saha Roy, and Gerhard Weikum. 2022. Beyond NED:
Fast and Effective Search Space Reduction for Complex Question Answering over
Knowledge Bases. In Proceedings of the Fifteenth ACM International Conference on
Web Search and Data Mining (Virtual Event, AZ, USA) (WSDM ’22). Association
for Computing Machinery, New York, NY, USA, 172–180. doi:10.1145/3488560.
3498488

[14] Francesca Ciccarelli, Andrea D’Angelo, and Giovanni Stilo. 2024. Towards a
Novel Visual Evaluation of Algorithmic Bias: Insights on the Italian Academic
System. (2024).

[15] Andrea D’Angelo, Claudio Savelli, Gabriele Tagliente, Flavio Giobergia, Elena Bar-
alis, Giovanni Stilo, et al. 2025. ERASURE: A Modular and Extensible Framework
for Machine Unlearning. In Titolo volume non avvalorato. ACM.

[16] Fatemeh Dashtiahangar and Jiann-Shiun Yuan. 2025. Bridging Morphology and
Molecular Signatures: Multi-Task Deep Learning for Multi-Omics Prediction from
Histopathology. In 2025 IEEE/CVF Conference on Computer Vision and Pattern
Recognition Workshops (CVPRW). IEEE, 1–9.

[17] Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017.
Automated Hate Speech Detection and the Problem of Offensive Language. Pro-
ceedings of the International AAAI Conference on Web and Social Media 11, 1 (May
2017), 512–515. doi:10.1609/icwsm.v11i1.14955

[18] Chenlong Deng, Yujia Zhou, and Zhicheng Dou. 2022. Improving Personalized
Search with Dual-Feedback Network. In Proceedings of the Fifteenth ACM Inter-
national Conference on Web Search and Data Mining (Virtual Event, AZ, USA)
(WSDM ’22). Association for Computing Machinery, New York, NY, USA, 210–218.
doi:10.1145/3488560.3498447

[19] Finale Doshi-Velez and Been Kim. 2017. Towards A Rigorous Science of In-
terpretable Machine Learning. arXiv: Machine Learning (2017). https://api.
semanticscholar.org/CorpusID:11319376

[20] Yijun Duan and Adam Jatowt. 2019. Across-Time Comparative Summarization of
News Articles. In Proceedings of the Twelfth ACM International Conference on Web
Search and Data Mining (Melbourne VIC, Australia) (WSDM ’19). Association
for Computing Machinery, New York, NY, USA, 735–743. doi:10.1145/3289600.
3291008

[21] Giordano d’Aloisio, Andrea D’Angelo, Antinisca Di Marco, and Giovanni Stilo.
2023. Debiaser for Multiple Variables to enhance fairness in classification tasks.
Information Processing & Management 60, 2 (2023), 103226.

[22] Upol Ehsan, Q. Vera Liao, Michael Muller, Mark O. Riedl, and Justin D. Weisz.
2021. Expanding Explainability: Towards Social Transparency in AI systems. In

Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems
(Yokohama, Japan) (CHI ’21). Association for Computing Machinery, New York,
NY, USA, Article 82, 19 pages. doi:10.1145/3411764.3445188

[23] Yi Fang, Luo Si, Naveen Somasundaram, and Zhengtao Yu. 2012. Mining con-
trastive opinions on political texts using cross-perspective topic model. In Pro-
ceedings of the Fifth ACM International Conference on Web Search and Data Mining
(Seattle, Washington, USA) (WSDM ’12). Association for Computing Machinery,
New York, NY, USA, 63–72. doi:10.1145/2124295.2124306

[24] Alessandro Flaborea, Bardh Prenkaj, Bharti Munjal, Marco Aurelio Sterpa, Dario
Aragona, Luca Podo, and Fabio Galasso. 2023. Are We Certain It’s Anomalous?. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition
(CVPR) Workshops. 2897–2907.

[25] Daniele Fossemò, Filippo Mignosi, Luca Raggioli, Matteo Spezialetti, Fabio Aurelio
D’Asaro, et al. 2022. Using Inductive Logic Programming to globally approximate
Neural Networks for preference learning: challenges and preliminary results. In
CEUR WORKSHOP PROCEEDINGS. 67–83.

[26] Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A.
Smith. 2020. RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Lan-
guage Models. In Findings of the Association for Computational Linguistics: EMNLP
2020, Trevor Cohn, Yulan He, and Yang Liu (Eds.). Association for Computational
Linguistics, Online, 3356–3369. doi:10.18653/v1/2020.findings-emnlp.301
[27] Vahid Ghafouri, Vibhor Agarwal, Yong Zhang, Nishanth Sastry, Jose Such, and
Guillermo Suarez-Tangil. 2023. AI in the Gray: Exploring Moderation Policies in
Dialogic Large Language Models vs. Human Answers in Controversial Topics.
In Proceedings of the 32nd ACM International Conference on Information and
Knowledge Management (Birmingham, United Kingdom) (CIKM ’23). Association
for Computing Machinery, New York, NY, USA, 556–565. doi:10.1145/3583780.
3614777

[28] Rishav Hada, Amir Ebrahimi Fard, Sarah Shugars, Federico Bianchi, Patricia
Rossini, Dirk Hovy, Rebekah Tromble, and Nava Tintarev. 2023. Beyond Digital
"Echo Chambers": The Role of Viewpoint Diversity in Political Discussion. In
Proceedings of the Sixteenth ACM International Conference on Web Search and
Data Mining (Singapore, Singapore) (WSDM ’23). Association for Computing
Machinery, New York, NY, USA, 33–41. doi:10.1145/3539597.3570487

[29] Robert R. Hoffman, Shane T. Mueller, Gary Klein, and Jordan Litman. 2018.
Metrics for Explainable AI: Challenges and Prospects. CoRR abs/1812.04608
(2018). arXiv:1812.04608 http://arxiv.org/abs/1812.04608

[30] Sanne A. Hoogenboom, Kamalakkannan Ravi, Megan M. Engels, Ismail Irmakci,
Elif Keles, Candice W. Bolan, Michael B. Wallace, and Ulas Bagci. 2021. 79
Missed Diagnosis of Pancreatic Ductal Adenocarcinoma Detection using Deep
Convolutional Neural Network. Gastroenterology 160, 6, Supplement (2021), S–18.
doi:10.1016/S0016-5085(21)00794-0

[31] Tao Huang. 2025. Content moderation by llm: From accuracy to legitimacy.

Artificial Intelligence Review 58, 10 (2025), 1–32.

[32] Zexi Huang, Arlei Silva, and Ambuj Singh. 2022. POLE: Polarized Embedding for
Signed Networks. In Proceedings of the Fifteenth ACM International Conference on
Web Search and Data Mining (Virtual Event, AZ, USA) (WSDM ’22). Association
for Computing Machinery, New York, NY, USA, 390–400. doi:10.1145/3488560.
3498454

[33] Alon Jacovi and Yoav Goldberg. 2021. Aligning Faithful Interpretations with their
Social Attribution. Transactions of the Association for Computational Linguistics 9
(2021), 294–310. doi:10.1162/tacl_a_00367

[34] Sarthak Jain and Byron C. Wallace. 2019. Attention is not Explanation. In Pro-
ceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume 1 (Long
and Short Papers), Jill Burstein, Christy Doran, and Thamar Solorio (Eds.). As-
sociation for Computational Linguistics, Minneapolis, Minnesota, 3543–3556.
doi:10.18653/v1/N19-1357

[35] Weina Jin, Xiaoxiao Li, and Ghassan Hamarneh. 2022. Evaluating Explainable AI
on a Multi-Modal Medical Imaging Task: Can Existing Algorithms Fulfill Clinical
Requirements? Proceedings of the AAAI Conference on Artificial Intelligence 36,
11 (Jun. 2022), 11945–11953. doi:10.1609/aaai.v36i11.21452

[36] Narine Kokhlikyan, Vivek Miglani, Miguel Martin, Edward Wang, Bilal Alsallakh,
Jonathan Reynolds, Alexander Melnikov, Natalia Kliushkina, Carlos Araya, Siqi
Yan, and Orion Reblitz-Richardson. 2020. Captum: A unified and generic model
interpretability library for PyTorch. CoRR abs/2009.07896 (2020). arXiv:2009.07896
https://arxiv.org/abs/2009.07896

[37] Anastasiia Kornilova and Lucas Bernardi. 2021. Mining the stars: learning quality
ratings with user-facing explanations for vacation rentals. In Proceedings of the
14th ACM International Conference on Web Search and Data Mining. 976–983.
[38] Sanmi Koyejo and Bo Li. 2024. Towards Trustworthy Large Language Models.
In Proceedings of the 17th ACM International Conference on Web Search and Data
Mining (Merida, Mexico) (WSDM ’24). Association for Computing Machinery,
New York, NY, USA, 1126–1127. doi:10.1145/3616855.3636454

[39] Deepak Kumar, Yousef Anees AbuHashem, and Zakir Durumeric. 2024. Watch
your language: Investigating content moderation with large language models. In
Proceedings of the International AAAI Conference on Web and Social Media, Vol. 18.
865–878.

82TRuST-M: Evaluating User Trust and Explainability in LLM-Based Web Moderation Systems

WSDM Companion ’26, February 22–26, 2026, Boise, ID, USA

Detection. In Proceedings of the 17th ACM International Conference on Web Search
and Data Mining (Merida, Mexico) (WSDM ’24). Association for Computing
Machinery, New York, NY, USA, 626–635. doi:10.1145/3616855.3635771

[59] Karen Simonyan, Andrea Vedaldi, and Andrew Zisserman. 2014. Deep Inside
Convolutional Networks: Visualising Image Classification Models and Saliency
Maps. In Workshop at International Conference on Learning Representations.
[60] Snowflake Inc. 2025. Streamlit: A Faster Way to Build and Share Data Apps.

https://pypi.org/project/streamlit/. https://streamlit.io Version 1.46.1.

[61] Donghyun Son, Byounggyu Lew, Kwanghee Choi, Yongsu Baek, Seungwoo Choi,
Beomjun Shin, Sungjoo Ha, and Buru Chang. 2023. Reliable Decision from
Multiple Subtasks through Threshold Optimization: Content Moderation in the
Wild. In Proceedings of the Sixteenth ACM International Conference on Web Search
and Data Mining (Singapore, Singapore) (WSDM ’23). Association for Computing
Machinery, New York, NY, USA, 285–293. doi:10.1145/3539597.3570439

[62] Azwad Tamir and Jiann-Shiun Yuan. 2025. Prot-GO: A Parallel Transformer
Encoder-Based Fusion Model for Accurately Predicting Gene Ontology (GO)
Terms from Full-Scale Protein Sequences. Electronics 14, 19 (2025), 3944.
[63] Theodora Tsikrika, Babak Akhgar, Vasilis Katos, Stefanos Vrochidis, Pete Burnap,
and Matthew L. Williams. 2017. 1st International Workshop on Search and Mining
Terrorist Online Content & Advances in Data Science for Cyber Security and
Risk on the Web. In Proceedings of the Tenth ACM International Conference on Web
Search and Data Mining (Cambridge, United Kingdom) (WSDM ’17). Association
for Computing Machinery, New York, NY, USA, 823–824. doi:10.1145/3018661.
3022760

[64] Ameya Vaidya, Feng Mai, and Yue Ning. 2020. Empirical Analysis of Multi-Task
Learning for Reducing Identity Bias in Toxic Comment Detection. Proceedings
of the International AAAI Conference on Web and Social Media 14, 1 (May 2020),
683–693. doi:10.1609/icwsm.v14i1.7334

[65] Jonathan Vasquez, Carlotta Domeniconi, and Huzefa Rangwala. 2024. DispaRisk:
Auditing Fairness Through Usable Information. arXiv preprint arXiv:2405.12372
(2024).

[66] Bertie Vidgen, Alex Harris, Dong Nguyen, Rebekah Tromble, Scott Hale, and
Helen Margetts. 2019. Challenges and frontiers in abusive content detection. In
Proceedings of the Third Workshop on Abusive Language Online, Sarah T. Roberts,
Joel Tetreault, Vinodkumar Prabhakaran, and Zeerak Waseem (Eds.). Association
for Computational Linguistics, Florence, Italy, 80–93. doi:10.18653/v1/W19-3509
[67] Jesse Vig. 2019. A Multiscale Visualization of Attention in the Transformer Model.
In Proceedings of the 57th Annual Meeting of the Association for Computational
Linguistics: System Demonstrations. Association for Computational Linguistics,
Florence, Italy, 37–42. doi:10.18653/v1/P19-3007

[68] Zeerak Waseem and Dirk Hovy. 2016. Hateful Symbols or Hateful People? Predic-
tive Features for Hate Speech Detection on Twitter. In Proceedings of the NAACL
Student Research Workshop, Jacob Andreas, Eunsol Choi, and Angeliki Lazaridou
(Eds.). Association for Computational Linguistics, San Diego, California, 88–93.
doi:10.18653/v1/N16-2013

[69] Ingmar Weber, Ana-Maria Popescu, and Marco Pennacchiotti. 2013. Data-driven
political science. In Proceedings of the Sixth ACM International Conference on Web
Search and Data Mining (Rome, Italy) (WSDM ’13). Association for Computing
Machinery, New York, NY, USA, 777–778. doi:10.1145/2433396.2433498

[70] Sarah Wiegreffe and Yuval Pinter. 2019. Attention is not not Explanation. In
Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing and the 9th International Joint Conference on Natural Language Pro-
cessing (EMNLP-IJCNLP), Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan
(Eds.). Association for Computational Linguistics, Hong Kong, China, 11–20.
doi:10.18653/v1/D19-1002

[71] Chih-Kuan Yeh, Cheng-Yu Hsieh, Arun Sai Suggala, David I. Inouye, and Pradeep
Ravikumar. 2019. On the (in)fidelity and sensitivity of explanations. Curran
Associates Inc., Red Hook, NY, USA.

[40] Isaac Lage, Emily Chen, Jeffrey He, Menaka Narayanan, Been Kim, Sam Gershman,
and Finale Doshi-Velez. 2019. An evaluation of the human-interpretability of
explanation. arXiv preprint arXiv:1902.00006 (2019).

[41] Q. Vera Liao, Daniel Gruen, and Sarah Miller. 2020. Questioning the AI: Informing
Design Practices for Explainable AI User Experiences. In Proceedings of the 2020
CHI Conference on Human Factors in Computing Systems (Honolulu, HI, USA)
(CHI ’20). Association for Computing Machinery, New York, NY, USA, 1–15.
doi:10.1145/3313831.3376590

[42] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer
Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. RoBERTa: A
Robustly Optimized BERT Pretraining Approach. CoRR abs/1907.11692 (2019).
arXiv:1907.11692 http://arxiv.org/abs/1907.11692

[43] Scott M. Lundberg and Su-In Lee. 2017. A unified approach to interpreting
model predictions. In Proceedings of the 31st International Conference on Neural
Information Processing Systems (Long Beach, California, USA) (NIPS’17). Curran
Associates Inc., Red Hook, NY, USA, 4768–4777.

[44] Christian Meske and Enrico Bunde. 2022. Design Principles for User Interfaces
in AI-Based Decision Support Systems: The Case of Explainable Hate Speech
Detection. 25, 2 (March 2022), 743–773. doi:10.1007/s10796-021-10234-5
[45] Anna Muratova. 2021. Interpretability and Effectiveness of Machine Learning
Methods for Sequence Mining in Various Domains. In Proceedings of the 14th
ACM International Conference on Web Search and Data Mining (Virtual Event,
Israel) (WSDM ’21). Association for Computing Machinery, New York, NY, USA,
1113–1114. doi:10.1145/3437963.3441670

[46] Raymond S Nickerson. 1998. Confirmation bias: A ubiquitous phenomenon in

many guises. Review of general psychology 2, 2 (1998), 175–220.

[47] Forough Poursabzi-Sangdeh, Daniel G Goldstein, Jake M Hofman, Jennifer Wort-
man Wortman Vaughan, and Hanna Wallach. 2021. Manipulating and measuring
model interpretability. In Proceedings of the 2021 CHI conference on human factors
in computing systems. 1–52.

[48] Inioluwa Deborah Raji, Timnit Gebru, Margaret Mitchell, Joy Buolamwini, Joon-
seok Lee, and Remi Denton. 2020. Saving Face: Investigating the Ethical Concerns
of Facial Recognition Auditing. In Proceedings of the AAAI/ACM Conference on AI,
Ethics, and Society (New York, NY, USA) (AIES ’20). Association for Computing
Machinery, New York, NY, USA, 145–151. doi:10.1145/3375627.3375820

[49] Kamalakkannan Ravi and Adan Ernesto Vela. 2024. RICo: Reddit ideological
communities. Online Social Networks and Media 42 (2024), 100279. doi:10.1016/j.
osnem.2024.100279

[50] Kamalakkannan Ravi, Adan Ernesto Vela, Elizabeth Jenaway, and Steven
Windisch. 2023. Exploring Multi-Level Threats in Telegram Data with AI-Human
Annotation: A Preliminary Study. In 2023 International Conference on Machine
Learning and Applications (ICMLA). 1520–1527. doi:10.1109/ICMLA58977.2023.
00229

[51] Kamalakkannan Ravi and Jiann-Shiun Yuan. 2024. Ideological orientation and
extremism detection in online social networking sites: A systematic review.
Intelligent Systems with Applications 24 (2024), 200456. doi:10.1016/j.iswa.2024.
200456

[52] Kamalakkannan Ravi and Jiann-Shiun Yuan. 2025. ThreatGram101: Extreme
Telegram Replies Data with Threat Levels. In Information Management and Big
Data, Juan Antonio Lossio-Ventura, Eduardo Ceh-Varela, Eduardo Díaz, Freddy
Paz Espinoza, Claude Tadonki, and Hugo Alatrista-Salas (Eds.). Springer Nature
Switzerland, Cham, 275–291.

[53] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. 2016. "Why Should I
Trust You?": Explaining the Predictions of Any Classifier. In Proceedings of the
22nd ACM SIGKDD International Conference on Knowledge Discovery and Data
Mining (San Francisco, California, USA) (KDD ’16). Association for Computing
Machinery, New York, NY, USA, 1135–1144. doi:10.1145/2939672.2939778
[54] Koustav Rudra, Niloy Ganguly, Jeanne Mifsud Bonnici, Eric Müller-Budack, and
Ritumbra Manuvie. 2025. Disinformation and Misinformation in the Age of
Generative AI. In Proceedings of the Eighteenth ACM International Conference on
Web Search and Data Mining (Hannover, Germany) (WSDM ’25). Association for
Computing Machinery, New York, NY, USA, 1122–1123. doi:10.1145/3701551.
3705708

[55] Ramit Sawhney, Harshit Joshi, Saumya Gandhi, and Rajiv Ratn Shah. 2021. To-
wards Ordinal Suicide Ideation Detection on Social Media. In Proceedings of the
14th ACM International Conference on Web Search and Data Mining (Virtual Event,
Israel) (WSDM ’21). Association for Computing Machinery, New York, NY, USA,
22–30. doi:10.1145/3437963.3441805

[56] Ramprasaath R. Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedan-
tam, Devi Parikh, and Dhruv Batra. 2020. Grad-CAM: Visual Explanations from
Deep Networks via Gradient-Based Localization. Int. J. Comput. Vision 128, 2
(Feb. 2020), 336–359. doi:10.1007/s11263-019-01228-7

[57] Sofia Serrano and Noah A. Smith. 2019. Is Attention Interpretable?. In Proceedings
of the 57th Annual Meeting of the Association for Computational Linguistics, Anna
Korhonen, David Traum, and Lluís Màrquez (Eds.). Association for Computational
Linguistics, Florence, Italy, 2931–2951. doi:10.18653/v1/P19-1282

[58] Paras Sheth, Raha Moraffah, Tharindu S. Kumarage, Aman Chadha, and Huan
Liu. 2024. Causality Guided Disentanglement for Cross-Platform Hate Speech

83