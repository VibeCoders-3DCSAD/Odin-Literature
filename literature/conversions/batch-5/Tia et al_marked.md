---
conversion_metadata:
  converted_at: "2026-07-21T09:00:21Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Tia et al.pdf"
  source_pdf_sha256: "e3c93a961ceaeaacabd22edfdcff9b1db1fa7fc56df14d17995e2f39e9c1605d"
  page_count: 18
  markdown_char_count: 109637
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

5
2
0
2

y
a
M
8
2

]

A
M

.
s
c
[

1
v
5
2
1
2
2
.
5
0
5
2
:
v
i
X
r
a

SENTIMENT SIMULATION USING GENERATIVE AI AGENTS

Melrose Tia1, Jezreel Sophia Lanuzo1, Lei Rigi Baltazar1,
Marie Joy Lopez-Relente2, Diwa Malaya Quiñones3, Jason Albia1∗
1Netopia AI, Inc., Manila, Philippines
2Institute of Statistics, University of the Philippines Los Baños, Laguna
3Department of Psychology, University of the Philippines Diliman, Quezon City
{melrose, sophia, lei, jason}@netopia.ai, {daquinones, mflopez2}@up.edu.ph

ABSTRACT

Traditional sentiment analysis relies on surface-level linguistic patterns and retrospective data, limiting
its ability to capture the psychological and contextual drivers of human sentiment. These limitations
constrain its effectiveness in applications that require predictive insight, such as policy testing,
narrative framing, and behavioral forecasting. We present a robust framework for sentiment simulation
using generative AI agents embedded with psychologically rich profiles. Agents are instantiated
from a nationally representative survey of 2, 485 Filipino respondents, combining sociodemographic
information with validated constructs of personality traits, values, beliefs, and socio-political attitudes.
The framework includes three stages: (1) agent embodiment via categorical or contextualized
encodings, (2) exposure to real-world political and economic scenarios, and (3) generation of
sentiment ratings accompanied by explanatory rationales. Using Quadratic Weighted Accuracy
(QWA), we evaluated alignment between agent-generated and human responses. Contextualized
encoding achieved 92% alignment in replicating original survey responses. In sentiment simulation
tasks, agents reached 81%–86% accuracy against ground truth sentiment, with contextualized profile
encodings significantly outperforming categorical (p < 0.0001, Cohen’s d = 0.70). Simulation
results remained consistent across repeated trials (±0.2 − 0.5% SD) and resilient to variation in
scenario framing (p = 0.9676, Cohen’s d = 0.02). Our findings establish a scalable framework for
sentiment modeling through psychographically grounded AI agents. This work signals a paradigm
shift in sentiment analysis from retrospective classification to prospective and dynamic simulation
grounded in psychology of sentiment formation.

Keywords agentic simulation · sentiment analysis · sentiment simulation · generative AI agents · behavioral science

1

Introduction

Sentiment analysis involves assessing the opinions and attitudes toward specific areas of interests, playing a pivotal
role in influencing decisions across business, societal, and individual domains [1, 2]. While the term sentiment
analysis gained prominence in the early 2000s [3, 4], the broader practice of gauging public opinion has long shaped
policy-making, democratic discourse, and marketing strategies [5]. As digital platforms and user-generated content
increasingly serve as channels for public expression, sentiment analysis enables organizations to harness opinion-rich
and unstructured data to refine communication strategies and to respond effectively to societal trends.

In the socio-political domain, sentiment analysis has supported applications ranging from policy evaluation to campaign
strategy by enabling large-scale interpretation of public opinion. Examples include assessments of public engagement
with government initiatives [6, 7, 8, 9], political campaign analysis [10, 11, 12], and citizen feedback monitoring
via social media [13]. For instance, Sandoval-Almazan et al. (2020) [10] examined Facebook reactions to political
campaign posts in Mexico, uncovering patterns in public engagement. In Indonesia, Sukma et al. (2020) [7] analyzed
Twitter responses to the Omnibus Law, revealing levels of public support and dissent to the policy. In the Philippines,

∗Corresponding author: jason@netopia.ai

---

<!-- PAGE 2 -->

Sentiment Simulation Using Generative AI Agents

Miranda et al. (2021) [12] tracked sentiment around presidential state addresses, while Umali et al. (2020) [13] assessed
citizen satisfaction with various government agencies based on social media commentary.

Beyond politics, sentiment analysis is widely used in the private sector, where it serves as a critical tool in marketing,
advertising, and customer experience strategies. Rathore et al. (2020) [14], for example, analyzed emotional patterns in
online comments before and after product launches to assess market reception and product fit. Giannakis et al. (2022)
[15] showed how consumer sentiment from social media can inform early-stage product development, while Yin et al.
(2022) [16] studied brand loyalty and satisfaction through Twitter sentiment toward e-commerce platforms Lazada and
Shopee. In addition, sentiment analysis has also been applied to evaluate consumer reviews for predicting behavior
and satisfaction [17, 18] and to generate real-time customer insights [19], thereby contributing to product refinement,
enhanced customer engagement, and data-driven business strategies.

Traditional Sentiment Analysis and Their Limitations

Traditional sentiment analysis often relies on structured methods such as surveys, opinion polls, and focus groups,
alongside more recent digital sources like social media [2]. These approaches have paved the way into computational
techniques leveraging machine learning (ML) and natural language processing (NLP) to classify sentiment (e.g.,
negative, neutral, positive) based on large-scale text analysis. These methods analyze linguistic patterns, including
the use of emotionally charged words (e.g., “happy”, “disappointed”) and syntactic structures that convey opinion or
emotions.

Despite advances in ML and deep learning models that boost classification accuracy [20], these approaches are
fundamentally limited. First, they primarily capture surface-level linguistic cues, often oversimplifying the complexity
and nuance of human emotion and opinion. Second, these models function as black-box systems that lack transparency,
offering limited insight into the reasoning behind sentiment predictions [21]. This lack of interpretability impairs trust,
accountability, and applicability in domains requiring nuanced understanding.

Third, and perhaps most critically, current sentiment analysis techniques often fail to account for contextual and
psychological factors, including individual biases, personality traits, values, or temporal circumstances [22, 23, 24]. For
example, Mahmoudi (2021) [22] emphasizes how user-level biases can lead to divergent interpretations of the same
event, which are often ignored in traditional models. Because these systems typically offer retrospective summaries
rather than dynamic simulations, they struggle to support forward-looking applications such as policy testing, narrative
impact studies, or synthetic focus groups [25].

To illustrate, a sentiment model trained on social media posts from a prior election may accurately classify political
opinions from that period [26, 27], but it cannot simulate how a specific group—such as rural, first-time voters, might
react to a new policy announcement or media event. These limitations reveal a broader issue: these models are
inadequate to model sentiment as situated cognition, that is, an emergent, psychologically grounded response shaped by
internal dispositions and external stimuli [28].

Sentiment Simulation using AI and Behavioral Science

Rooted in the above challenges, we propose a conceptual shift: from retrospective sentiment classification to AI
and behavioral science-driven sentiment simulation. This approach integrates two core paradigms: (1) a behavioral
science framework that explains how sentiments arise from psychological drivers, and (2) a simulation-based modeling
paradigm enabled by generative AI.

Behavioral science provides the theoretical foundation for this shift. It conceptualizes sentiment as a dynamic construct
shaped by cognition, emotion, and situational context. Social psychology suggests that sentiment reflects attitudes
formed from beliefs, values, and environmental factors—factors that, in turn, shape behavior [29]. A complementary
analysis by Li and Hovy (2017) [30] further argue that sentiment originates from emotionally driven preferences and
the pursuit of personal goals. These perspectives suggest that sentiment is not just a textual artifact but a behavioral
expression rooted in individual psychology.

In methodical perspective, unlike traditional models that classify past sentiment, generative models such as large
language models (LLMs) enable prospective simulations that can generate behaviorally rich, context-sensitive senti-
ment. These generative models can simulate trust dynamics [31], personality expression [32], and opinion formation
[33]—capabilities that align well with psychological realism. In addition, generative models has also catalyzed new
research on synthetic populations and simulated human studies [34, 35], positioning generative AI as a powerful tool
for behavioral science. Representative studies illustrating these advances are summarized in Table 1.

2

---

<!-- PAGE 3 -->

Sentiment Simulation Using Generative AI Agents

Table 1: Recent studies that inform and support this work, highlighting their domains and key findings.

Study

Domain

Key Findings

Using LLMs to Simulate
Multiple Humans and
Replicate Human Subject
Studies [32]

Generative Agents:
Interactive Simulations of
Human Behavior [36]

Behavioral Economics
and Social Psychology

Human-AI Interaction

Generative Agent Simulations
of 1000 People [24]

Social Science

User Behavior Simulation
with LLM-based Agents [37]

User Behavior
Simulation

Simulated classic behavioral studies (e.g., Ultimatum
Game, Milgram) and found that larger LLMs (GPT-
3.5/4) could replicate established findings across eco-
nomics, psycholinguistics, and social psychology.

Introduced "generative agents"—LLM-driven agents
with memory, planning, and reflection. Demonstrated
emergent behavior in interactive environments (e.g.,
autonomously organizing a Valentine’s Day party)
from a single prompt.

Developed an LLM-based agent architecture to simu-
late 1,052 real individuals based on interviews. Agents
replicated survey responses with ≈ 85% accuracy,
comparable to humans’ own retest accuracy, and pre-
dicted personality traits well.

Developed an LLM-based framework for simulating
user behaviors (e.g., web navigation). Captured social
dynamics like conformity and information cocooning.

Can Large Language Model
Agents Simulate Human Trust
Behavior? [31]

Behavioral Economics Used Trust Games to evaluate agent behavior. GPT-4
agents showed trust-like behavior and strong alignment
with human responses in social dilemmas.

Evaluating the Ability of
LLMs to Emulate Personality
[38]

Personality Modeling

GPT-4 simulated individuals with Big Five profiles.
Generated responses showed high internal consistency
and strong correlation with self-reported personality
scores.

While the above prior studies have illustrated potential of LLMs to simulate behaviors, replicate human experiments, or
model trust, none have yet grounded sentiment simulation in real psychographic survey data. Our work fills this gap by
embedding psychologically validated profiles into generative AI agents to simulate how real people might respond to
socio-political and economic scenarios.

Contribution of the Article

In this study, we present a simple and scalable generative AI agentic framework via structured LLM prompting to
simulate the sentiment response of the survey respondents on several socio-political and economic scenarios. The
AI agents were instantiated to embody the psychological profiles derived from nationally representative survey and
their simulated response is compared with the ground truth data. More precisely, the contributions of this work are as
follows:

• We demonstrate that AI agents can be effectively instantiated to embody the psychological profiles constructed
from empirically generated data. These profiles incorporate socio-demographic data and variables from
validated psychological frameworks and attitudes on key socio-political and economic issues, providing agents
with psychographically grounded priors.

• We show that these AI agents are capable of replicating survey results, as well as sentiment distributions
observed in real-world responses, achieving high levels of individual-level alignment. Furthermore, we
demonstrate that agent responses are robust across alternative framings of the same scenarios, indicating the
consistency and stability of our simulation framework.

3

---

<!-- PAGE 4 -->

Sentiment Simulation Using Generative AI Agents

2 Methodology

2.1 Survey Design and Data Collection

The survey instrument was designed to provide an interdisciplinary understanding of Filipino citizens’ profiles by
integrating multiple well-established psychological frameworks to capture a deeper understanding of public sentiment
towards various socio-political and economic issues in the Philippines.

The instrument consists of 150 items, integrating both sociodemographic variables (age, sex, educational attainment,
religion, and other key identifiers) and different psychological dimensions (personality traits, values, attitudinal
frameworks, beliefs, and social and political behavior). These frameworks are theoretically grounded and considered
temporally stable [39, 40, 41], allowing for the abstraction of consistent psychographic profiles. For greater sensitivity
in capturing the intensity and direction of respondents’ responses, most frameworks were measured using a 7-point
Likert scale. Respondents were asked to express their level of agreement or disagreement with statements about selected
major socio-political and economic issues [42].

Descriptive statistics of a nationally representative sample of 2, 485 registered Filipino voters with 95% confidence
level and 1.97% margin of error are summarized in Table 2. The respondents’ age ranged from 18 to 89 years old,
with the majority (33%) falling within the adult age group (28 − 42 years old). The sample was gender-balanced (50%
female, 50% male), and the majority were married (57%). In terms of socioeconomic status, nearly half of the sample
(49%) reported no monthly income, while 30% were categorized as low income. Most participants had completed at
least high school (52%) or college (21%).

Table 2: Descriptive statistics of the study sample (N = 2, 485).

Variable Category

Age Group

Count (Relative Proportion)

Young Adults (18–27 Years Old)
Adults (28–43 Years Old)
Middle-Aged Adults (44–59 Years Old)
Seniors (60+ Years Old)

Marital Status

Single
Live-In
Married
Separated
Widowed

Monthly Income-Based Socioeconomic Status

No Income
Low Income
Middle Income
High Income

Highest Educational Attainment
No Formal Education
At least Elementary
At least High School
At least Vocational
At least College
At least Graduate Studies

399 (16%)
820 (33%)
736 (30%)
530 (21%)

380 (15%)
395 (16%)
1413 (57%)
77 (3%)
220 (9%)

1213 (49%)
740 (30%)
530 (21%)
2 (<1%)

8 (<1%)
502 (20%)
1294 (52%)
152 (6%)
525 (21%)
4 (<1%)

To our knowledge, our data represents the largest and most demographically diverse samples in the Philippines used to
examine psychological frameworks, offering a robust basis for generalizing the findings to the broader adult population.
Previous psychological studies in the Filipino samples, such as those by Church et al. (1997) [43] (N = 629), Del Pilar
(2017) [44] (N = 576), and Wapaño (2021) [45] (N = 828), were conducted with smaller, more localized samples.

4

---

<!-- PAGE 5 -->

Sentiment Simulation Using Generative AI Agents

2.2 Sentiment Simulation

The sentiment simulation framework leverages generative AI agents, embodied with psychographic and contextual
variables, to model the sentiment of respondents in response to varying socio-political and economic scenarios. The
framework enables generative agents to produce dynamic sentiment responses that are not only reactive to input stimuli
but also aligned with their internal psychological attributes and contextual stimuli. As shown in Figure 1, the simulation
framework consists of three (3) core stages: Agent Embodiment, Agent Exposure to Scenarios, and Agent Response to
Scenarios.
All simulations were conducted using Llama 3.1 70B 1, a state-of-the-art open-weight LLM optimized for instruction
following, long-context reasoning, and alignment with human intent. This model is well-suited for simulating agent
behavior within psychological frameworks due to its architecture that supports multi-turn coherence and robust language
understanding [47].

Figure 1: Sentiment Simulation Framework Using AI Agents.

2.2.1 Agent Embodiment

Each AI agent is embodied with a unique set of sociodemographic and psychographic variables derived from empirical
survey. These variables were embedded into prompt templates using one of two encoding strategies: categorical or
contextualized.

• Categorical encoding involved assigning discrete labels (e.g., Low, Moderate, High) to each psychological

variable, producing a structured but abstract representation of personality and attitudes.

• Contextualized encoding, by contrast, translated these categories into narrative descriptions that reflect how
psychological variables might manifest in scenario-relevant contexts. For example, high openness in policy
domain might be expressed as receptive to new policy ideas or prone to considering multiple perspectives.

1Llama 3.1 70B was selected following rigorous experimentation with various LLMs evaluating their sensitivity to political and

linguistic bias. [46]

5

---

<!-- PAGE 6 -->

Sentiment Simulation Using Generative AI Agents

To evaluate the effectiveness of embodiment, we conducted a survey replication task wherein each agent, embodied
with a specific respondent’s profile, answered the same Likert-scale survey items as the human participant. This task
assessed whether the agent could faithfully reflect the individual’s psychological profile through simulated responses.

2.2.2 Agent Exposure to Scenario

In this phase, agents were presented with real-world scenarios analogous to campaign messages, policy debates,
economic developments, or media coverage of socio-political and economic issues: budget transparency, political
dynasties, inflation, the justice system, and wage policies. These scenarios are crafted as narrative prompts designed to
elicit affective, cognitive, and psychographically grounded responses, engaging the agent’s internal dispositions.

In addition, to examine the impact of scenario framing effects, each scenario was presented with either positive
or negative polarity, simulating ideological differences in real-world discourse (e.g., progressive vs. conservative
perspective). Respondents were randomly assigned to one framing type, while ensuring equal distribution of framing
across the entire sample population.

2.2.3 Agent Response to Scenario

Following scenario exposure, each agent produced a structured sentiment response, rated on a 5-point Likert scale
(Negative, Slightly Negative, Neutral, Slightly Positive, and Positive), along with a brief explanatory rationale for its
simulated sentiment.

After generating its initial sentiment, the agent was prompted with a self-assessment task, asking whether its response
was logically consistent with its psychographic profile and the characteristics of the scenario (see Supplementary
Material D). This iterative validation step reinforced coherence and internal consistency within the simulated responses.

2.3 Performance Evaluation Metrics

2.3.1 Quadratic Weighted Accuracy (QWA)

QWA was employed as the primary metric to evaluate alignment between agent-generated and human responses on an
ordinal scale. It penalizes distant misclassifications more heavily than near-miss errors, making it particularly suitable
for Likert-scale classification tasks, where response categories are inherently ordered.

The QWA score is computed using Eq. (1), with weights that increase quadratically based on the distance between
simulated and actual responses. This scoring method allows for a more nuanced assessment of model performance,
rewarding response predictions that are close to the expected value even when they are not exact matches.

wij = 1 −

(cid:19)2

(cid:18) dij
dmax

(1)

where:
wij is the score assigned to the pair of categories i (true response) and j (simulated response);
dij is the absolute distance between the true and simulated response categories; and
dmax is the maximum possible distance given the range of all possible response categories.

Higher QWA scores indicate that the agents’ responses are statistically accurate and internally coherent, i.e., interpretable
within the context of their embodied psychological profiles. Score matrices are visualized in Supplementary Materials
E.1 and E.2.

2.3.2 Statistical Tests

To evaluate the statistical significance of observed differences in agent–human alignment, we employed both parametric
(paired t-test) and non-parametric (Wilcoxon signed-rank) analysis, depending on the distributional properties of the
QWA scores. Specifically, paired t-test was used when the assumption of normality was satisfied, whereas Wilcoxon
signed-rank test was applied when this assumption was violated, due to their robustness to non-normal distributions. A
commonly used threshold of p < 0.05 was used to determine statistical significance.

In addition to hypothesis testing, we computed Cohen’s d to estimate effect sizes and assess the practical relevance of
observed differences. Effect sizes were interpreted using standard benchmarks: d ≈ 0.2 (small), d ≈ 0.5 (medium),
and d ≥ 0.8 (large). This dual approach enabled a robust interpretation ensuring that the reported improvements in
alignment were not only statistically significant but also practically meaningful.

6

---

<!-- PAGE 7 -->

Sentiment Simulation Using Generative AI Agents

3 Results and Discussion

3.1 Agent Embodiment Evaluation

Agent embodiment was implemented using two distinct encoding strategies: categorical encoding, which uses ranked
labels (e.g., Low, Moderate, High), and contextualized encoding, which embeds psychological variables into narrative
descriptions. These strategies offer differing levels of abstraction in representing individual profiles, allowing us to
compare their effects on simulated sentiment alignment.

These encoding strategies draw from recent works that attempt to embed psychological traits into LLM prompts. For
example, Wang et al. (2025) [38] used personality assessment data, albeit limited to numeric Big Five scores, to prompt
GPT-4 in simulating individual behaviors. Their method mirrors our categorical encoding approach, which also draws
from empirical data but translates scores into ranked labels such as Low, Moderate, or High. In contrast, Xie et al.
(2024) [31] used structured prompts with demographic and background details, similar to our contextualized strategy,
to elicit trust behaviors from LLMs. Our study advances these efforts by grounding both encoding strategies in real
large-scale survey data, allowing systematic comparisons between encoding levels.

Agent alignment with human survey responses is measured using QWA, where identical ratings yield 100% accuracy
score and one-point differences result in proportionally lower score of 97%, capturing the degree of ordinal misalignment.
See Supplementary Material E.1 for details.

Figure 2 illustrates the distribution of QWA scores for the two encoding strategies. The contextualized group’s curve
(blue) is consistently right-shifted, indicating that a larger proportion of agents achieved higher alignment scores
compared to their categorically encoded counterparts. This population-level trend suggests that narrative profile
encoding enables more human-consistent responses.

Figure 2: Cumulative Distribution Function (CDF) Plot: Distributional
Comparison of QWA Scores Across Profile Encoding Strategies.

Figure 3 offers an agent-level comparison. Each line connects the categorical and contextualized scores for a single
agent, highlighting changes in alignment. Most lines extend rightward, reinforcing that contextualized encoding
generally results in improved alignment for individual agents.

To determine whether the observed performance difference was statistically significant, we employed a Wilcoxon
signed-rank test. Preliminary diagnostics using the Shapiro–Wilk test indicated violations of normality (p = 0.0004,
justifying the use of a non-parametric approach. The Wilcoxon signed-rank test yielded a significant result (p < 0.0001),
suggesting that the alignment advantage of contextualized profile encoding is unlikely to be attributable to random
variation. To assess the practical significance of this effect, we calculated Cohen’s d = 0.70, indicating a moderate
effect size. Interpreted probabilistically, this reflects a 76% chance that a randomly selected agent with contextualized
encoding would outperform one using categorical encoding in response alignment [48]. These findings provide
statistical and practical evidence that contextualized profile encoding yields better alignment with human responses
compared to categorical encoding.

7

---

<!-- PAGE 8 -->

Sentiment Simulation Using Generative AI Agents

Figure 3: Paired Dot Plot: Per-Agent Comparison of QWA Scores Across Profile
Encoding Strategies. The vertical axis represents agents that are indexed arbitrarily.

On average, agents using contextualized profiles achieved 92% alignment with original human responses, demonstrating
the model’s capacity to simulate individual-level psychographic data with high fidelity. These results compare favorably
with prior efforts such as [49], which introduced the LLM-Mirror framework to assess the consistency between LLM-
generated responses and human survey data. While their persona-based prompting achieved 69% to 73% consistency
in domains like online advertising, corporate reputation, and customer loyalty, our approach reaches notably higher
alignment levels across a broader array of psychological constructs. Similarly, Yeykelis et al. (2024) [50] found that
AI personas could reproduce findings from experimental media studies with a 76% success rate. Our 92% alignment
suggests a stronger capacity to simulate nuanced attitudinal data, particularly when narrative context is used to express
psychological variables.

Collectively, these results demonstrate that contextualized psychological profile encoding significantly enhances agent-
human alignment and produces more consistent responses. Contextualized encodings guide agents more effectively
by embedding psychological traits within descriptive, scenario-relevant narratives. The performance gap between
categorical and contextualized encodings highlights the benefits of translating psychological variable labels into
rich psychographic contexts, enabling agents to respond more accurately in alignment with their profiles—a critical
foundation for generating psychologically coherent sentiment simulations.

3.2 Sentiment Simulation Performance

Following the high alignment observed in the agent embodiment task, we next evaluate the ability of psychographically
grounded agents to simulate human sentiment across a set of socio-political and economic scenarios: wage policies,
budget transparency, inflation, the justice system, and political dynasties. This analysis provides a broader test of the
model’s ability to generate human sentiment responses in real-world contexts.

Table 3: Sentiment Simulation Accuracy Across Socio-Political and Economic Scenarios.

Scenario

Wage Policies
Budget Transparency
Inflation
Justice System
Political Dynasties

Categorical
SD

Average

Contextualized
SD

Average

80.3%
80.1%
74.9%
86.7%
68.4%

± 0.19%
± 0.21%
± 0.32%
± 0.39%
± 0.20%

83.4% ± 0.20%
82.9% ± 0.33%
81.8% ± 0.17%
86.2% ± 0.26%
81.2% ± 0.51%

Table 3 summarizes sentiment alignment performance across the scenarios, comparing categorical and contextualized
encoding strategies. As shown, contextualized encoding consistently outperformed categorical encoding in four out of
five scenarios, with alignment accuracy gains ranging from 2.8% to 12.8% points. While categorical encoding achieved

8

---

<!-- PAGE 9 -->

Sentiment Simulation Using Generative AI Agents

accuracy levels ranging from 68% to 87%, contextualized profile encoding yielded more stable and higher performance
of 81% to 86%.

The largest accuracy gain occurred in the political dynasties scenario (+12.8%), followed by inflation (+6.9%). For
wage and budget transparency, improvements were more modest (+2.8% and +3.1%, respectively). Interestingly,
performance was nearly identical in the justice system scenario (−0.5%), suggesting that some scenarios may be less
influenced by internal psychological factors and more driven by ideological alignment or external cues.

These findings reinforce that sentiment simulation is enhanced when agents are grounded in contextually expressed
psychological traits, not merely categorical summaries. The more realistically an agent’s internal disposition is modeled,
the more accurately it mirrors human responses. This supports existing research [31] indicating that contextual richness
improves behavioral realism in LLM simulations.

Considering the inherent variability of LLMs, stemming from prompt sensitivity and randomness introduced by
stochastic decoding, we evaluated the stability of simulation outputs over repeated trials. Each scenario was simulated
five (5) times, and performance was averaged to assess internal consistency. As shown also in Table 3, sentiment
alignment scores were highly stable, with standard deviations for contextualized encoding ranging from ±0.17%
to ±0.51%, indicating minimal variability in performance across trials. More precisely, the justice system scenario
exhibited the highest and most stable performance, with QWA scores ranging narrowly from 86.0% to 86.7%. Wage
policies and budget transparency also showed strong stability, with QWA scores clustered tightly around the mid-83%
range. Inflation followed a similar trend, with minor fluctuations around 82%. Although political dynasties had the
lowest overall scores, ranging from 80.1% to 81.4%, the variation across trials was still minimal, indicating internal
consistency even in comparatively more complex or ideologically loaded scenarios.

Ultimately, our framework achieved high alignment performance across all tested scenarios (81% to 86%), reflecting not
only the predictive accuracy of the model, but also its behavioral plausibility. The framework’s consistency across trials
is illustrative of its suitability for use in replicable and scalable behavioral simulations. Our findings highlight three
pillars of effective simulation in behavioral science specifically in social sciences: (1) psychological grounding through
contextualized traits, (2) consistency of performance across diverse and complex scenarios, and (3) sentiment alignment
with empirically plausible human behavior [51, 52]. Moreover, in light of the variability inherent in emotional reasoning
and the influence of framing on an individual’s judgment [53], our results speak not only to technical performance, but
to the psychological credibility of the simulated agents themselves.

3.2.1 Simulation Robustness to Scenario Framing

To further evaluate the framework’s generalizability, we investigated its sensitivity to framing effects, i.e., whether
sentiment alignment varied substantially depending on whether a scenario was presented in a positive or negative light
(e.g., performing well under positive framing but poorly under negative framing). This step is important given that
prior studies in behavioral sciences and communication have shown that framing can substantially alter public opinion
[54, 55].

Figure 4: Quadratic Weighted Accuracy Between Survey and Simulated Sentiments
Across Framing Types of the Different Scenarios.

Figure 4 shows a plot comparison between the average QWA for positive (blue) and negative (orange) framings for
each scenario. Across the five socio-political and economic scenarios, QWA scores remained high 77% to 88%, with no
consistent performance degradation or amplification due to framing. While differences between the positively- and

9

---

<!-- PAGE 10 -->

Sentiment Simulation Using Generative AI Agents

negatively-framed scenarios ranged from 0.4% to 9.7%, the directionality and magnitude of these differences varied
across scenarios. For example, negatively-framed scenarios yielded higher alignment in inflation (+9.7%) and political
dynasty topics (+0.4%), whereas positively-framed scenarios outperformed in justice system (+4.3%), wage policies
(+4.4%), and budget transparency (+0.9%).

In addition, to further evaluate whether scenario framing influences sentiment simulation accuracy, we conducted a
paired sample t-test comparing agent–human alignment scores across positively- and negatively-framed versions of
each issue. The paired t-test was chosen to assess mean differences between framing conditions, with the Shapiro–Wilk
test confirming that the normality assumption was sufficiently met (p = 0.1388) . The analysis yielded a non-significant
result (p = 0.9676), indicating no statistically meaningful difference in simulation accuracy across framing conditions.
Furthermore, to quantify the magnitude of any potential effect, we computed Cohen’s d = 0.02, reflecting a negligible
effect size. This suggests that the difference in QWA scores between framing conditions is practically insignificant,
with sentiment alignment performance remaining stable regardless of scenario prompt framing.

Collectively, these results indicate that scenario framing does not exert a consistent or meaningful influence on simulation
accuracy. The framework allows agents to anchor their evaluations to their psychological attributes, rather than being
influenced by the differences in the scenario polarity framing.

These findings suggest that the agents remained anchored to their psychographic grounding, even under affective
variation in scenario prompts. From a behavioral science perspective, this mirrors the consistency of human behavior
across varied contexts, as documented in research on trait-based models [56]. This coherence supports the notion that
rich, context-sensitive embeddings enable psychologically grounded rather than context-reactive responses.

4 Conclusion

This study presents a psychographically grounded framework for sentiment simulation, leveraging language model
agents embodied with empirically derived psychological profiles. By integrating validated constructs into structured
prompts, we enable AI agents to simulate sentiment responses that are context-sensitive, psychologically coherent, and
behaviorally plausible.

Our evaluation demonstrates that agents instantiated with contextualized profile encodings closely replicate individual-
level sentiment patterns. In a survey replication task, these agents achieved alignment scores of up to 92%, significantly
outperforming categorical encoding strategies. This result underscores the importance of narrative-rich representations
in capturing the depth and nuance of human sentiment.

Beyond static replication, the framework also performs reliably in dynamic simulation tasks. When exposed to real-
world socio-political and economic scenarios, agents achieved high alignment accuracies indicating their capacity to
model realistic sentiment responses. Importantly, these results remained highly stable across five independent trials
and different scenario framings, highlighting the internal consistency of the framework despite the stochastic nature of
language models.

Overall, these results establish a reliable, scalable, and psychologically informed method for modeling public sentiment.
The framework offers practical applications in policy testing, narrative framing analysis, and the development of
synthetic populations for large-scale social simulation. More broadly, this work marks a paradigm shift—from retro-
spective sentiment classification toward prospective, psychologically grounded simulation leveraging the intersection of
generative AI and behavioral sciences.

Acknowledgments

We extend our sincere thanks to Mojhune Gabriel Manzanillo for his dedicated work in generating the experimental
results for this study. We also gratefully acknowledge Adrian Gabonada for his insightful contributions, which
significantly enriched the behavioral science interpretation and the discussion of our findings. We further thank Dannah
Zemirah Junio for her guidance on statistical analysis; her input was instrumental in ensuring the rigor and validity of
our evaluation methods. Model inferences and sentiment simulation were performed using compute resources provided
by the Google Cloud for Startups Program.

References

[1] Bo Pang, Lillian Lee, et al. Opinion mining and sentiment analysis. Foundations and Trends® in information

retrieval, 2(1–2):1–135, 2008.

10

---

<!-- PAGE 11 -->

Sentiment Simulation Using Generative AI Agents

[2] Bing Liu. Sentiment analysis and opinion mining. Springer Nature, 2012.
[3] Tetsuya Nasukawa and Jeonghee Yi. Sentiment analysis: Capturing favorability using natural language processing.

In Proceedings of the 2nd international conference on Knowledge capture, pages 70–77, 2003.

[4] Kushal Dave, Steve Lawrence, and David M Pennock. Mining the peanut gallery: Opinion extraction and semantic
classification of product reviews. In Proceedings of the 12th international conference on World Wide Web, pages
519–528, 2003.

[5] Vincent Price and Peter Neijens. Opinion quality in public opinion research. International Journal of Public

Opinion Research, 9(4):336–360, 1997.

[6] Yannis Charalabidis, Manolis Maragoudakis, and Euripides Loukis. Opinion mining and sentiment analysis in
policy formulation initiatives: The eu-community approach. In Electronic Participation: 7th IFIP 8.5 International
Conference, ePart 2015, Thessaloniki, Greece, August 30–September 2, 2015, Proceedings 7, pages 147–160.
Springer, 2015.

[7] Eki Aidio Sukma, Achmad Nizar Hidayanto, Adam Imansyah Pandesenda, Arif Nur Yahya, Punto Widharto, and
Untung Rahardja. Sentiment analysis of the new indonesian government policy (omnibus law) on social media
twitter. In 2020 International Conference on Informatics, Multimedia, Cyber and Information System (ICIMCIS),
pages 153–158. IEEE, 2020.

[8] Jiri Hradec, Nicole Ostlaender, Alba Bernini, et al. Fables: framework for autonomous behaviour-rich language-

driven emotion-enabled synthetic populations. Technical report, Joint Research Centre, 2023.

[9] Jana Flor V Vizmanos, Sheila V Siar, Jose Ramon G Albert, Janina Luz C Sarmiento, and Angelo C Hernandez.
Like, comment, and share: Analyzing public sentiments of government policies in social media. Technical report,
PIDS Discussion Paper Series, 2023.

[10] Rodrigo Sandoval-Almazan and David Valle-Cruz. Sentiment analysis of facebook users reacting to political

campaign posts. Digital Government: Research and Practice, 1(2):1–13, 2020.

[11] Charles Crabtree, Matt Golder, Thomas Gschwend, and Indri ¯di H Indri ¯dason. It is not only what you say, it is also
how you say it: The strategic use of campaign sentiment. The Journal of Politics, 82(3):1044–1060, 2020.
[12] John Paul P Miranda and Rex P Bringula. Exploring philippine presidentsâ C™ speeches: A sentiment analysis

and topic modeling approach. Cogent Social Sciences, 7(1):1932030, 2021.

[13] Julieta M Umali, John Paul P Miranda, and Anicia L Ferrer. Sentiment analysis: A case study among the selected

government agencies in the philippines. International Journal, 9(3), 2020.

[14] Ashish Kumar Rathore and P Vigneswara Ilavarasan. Pre-and post-launch emotions in new product development:
Insights from twitter analytics of three products. International Journal of Information Management, 50:111–127,
2020.

[15] Mihalis Giannakis, Rameshwar Dubey, Shishi Yan, Konstantina Spanaki, and Thanos Papadopoulos. Social
media and sensemaking patterns in new product development: demystifying the customer sentiment. Annals of
Operations Research, 308:145–175, 2022.

[16] Jenny Yow Bee Yin, Nor Hasliza Md Saad, and Zulnaidi Yaacob. Exploring sentiment analysis on e-commerce

business: Lazada and shopee. Tem journal, 11(4):1508, 2022.

[17] Praphula Kumar Jain, Rajendra Pamula, and Gautam Srivastava. A systematic literature review on machine
learning applications for consumer sentiment analysis using online reviews. Computer science review, 41:100413,
2021.

[18] Pawanjit Singh Ghatora, Seyed Ebrahim Hosseini, Shahbaz Pervez, Muhammad Javed Iqbal, and Nabil Shaukat.
Sentiment analysis of product reviews using machine learning and pre-trained llm. Big Data and Cognitive
Computing, 8(12):199, 2024.

[19] Jan Ole Krugmann and Jochen Hartmann. Sentiment analysis in the age of generative ai. Customer Needs and

Solutions, 11(1):3, 2024.

[20] Yanying Mao, Qun Liu, and Yu Zhang. Sentiment analysis methods, applications, and challenges: A systematic
literature review. Journal of King Saud University-Computer and Information Sciences, page 102048, 2024.
[21] Jamin Rahman Jim, Md Apon Riaz Talukder, Partha Malakar, Md Mohsin Kabir, Kamruddin Nur, and Mo-
hammed Firoz Mridha. Recent advancements and challenges of nlp-based sentiment analysis: A state-of-the-art
review. Natural Language Processing Journal, page 100059, 2024.

[22] Amin Mahmoudi. Identifying biased users in online social networks to enhance the accuracy of sentiment analysis:

A user behavior-based approach. arXiv preprint arXiv:2105.05950, 2021.

11

---

<!-- PAGE 12 -->

Sentiment Simulation Using Generative AI Agents

[23] Junjie Lin, Wenji Mao, and Daniel D Zeng. Personality-based refinement for sentiment classification in microblog.

Knowledge-Based Systems, 132:204–214, 2017.

[24] Jiyoung Park and Sang Eun Woo. Personality associations with attitudes toward ai. In The Impact of Artificial

Intelligence on Societies: Understanding Attitude Formation Towards AI, pages 57–70. Springer, 2024.

[25] Pujen Shrestha, Dario Krpan, Fatima Koaik, Robin Schnider, Dima Sayess, and May Saad Binbaz. Beyond weird:
Can synthetic survey participants substitute for humans in global policy research? Behavioral Science & Policy,
page 23794607241311793, 2025.

[26] Priyavrat Chauhan, Nonita Sharma, and Geeta Sikka. The emergence of social media data and sentiment analysis
in election prediction. Journal of Ambient Intelligence and Humanized Computing, 12:2601–2627, 2021.
[27] Asif Khan, Huaping Zhang, Nada Boudjellal, Arshad Ahmad, and Maqbool Khan. Improving sentiment analysis
in election-based conversations on twitter with elecbert language model. Computers, Materials & Continua, 76(3),
2023.

[28] Wolff-Michael Roth and Alfredo Jornet. Situated cognition. Wiley Interdisciplinary Reviews: Cognitive Science,

4(5):463–478, 2013.

[29] David Myers, Jackie Abell, and Fabio Sani. EBook: Social Psychology 3e. McGraw Hill, 2020.
[30] Jiwei Li and Eduard Hovy. Reflections on sentiment/opinion analysis. A practical guide to sentiment analysis,

pages 41–59, 2017.

[31] Chengxing Xie, Canyu Chen, Feiran Jia, Ziyu Ye, Shiyang Lai, Kai Shu, Jindong Gu, Adel Bibi, Ziniu Hu, David
Jurgens, et al. Can large language model agents simulate human trust behavior? In The Thirty-eighth Annual
Conference on Neural Information Processing Systems, 2024.

[32] Gati V Aher, Rosa I Arriaga, and Adam Tauman Kalai. Using large language models to simulate multiple humans
and replicate human subject studies. In International Conference on Machine Learning, pages 337–371. PMLR,
2023.

[33] Xiaoqing Zhang, Xiuying Chen, Yuhan Liu, Jianzhou Wang, Zhenxing Hu, and Rui Yan. Llm-driven agents for

influencer selection in digital advertising campaigns. arXiv e-prints, pages arXiv–2403, 2024.

[34] Carolyn Q. Zou Aaron Shaw Benjamin Mako Hill Carrie Cai Meredith Ringel Morris Robb Willer Percy Liang
Park, Joon Sung and Michael S. Bernstein. Generative agent simulations of 1,000 people. arXiv preprint, page
arXiv:2411.10109, 2024.

[35] Xiuying Chen Yaqi Wang Ruidi Chang Shichao Pei Nitesh V. Chawla Olaf Wiest Guo, Taicheng and Xiangliang
Zhang. Large language model based multi-agents: A survey of progress and challenges. arXiv preprint, page
arXiv:2402.01680, 2024.

[36] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein.
Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th annual acm symposium
on user interface software and technology, pages 1–22, 2023.

[37] Lei Wang, Jingsen Zhang, Hao Yang, Zhiyuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Ruihua
Song, Wayne Xin Zhao, et al. User behavior simulation with large language model based agents. arXiv preprint
arXiv:2306.02552, 2023.

[38] Yilei Wang, Jiabao Zhao, Deniz S Ones, Liang He, and Xin Xu. Evaluating the ability of large language models to

emulate personality. Scientific reports, 15(1):519, 2025.

[39] American Psychological Association. Personality. https://dictionary.apa.org/personality, n.d. APA

Dictionary of Psychology.

[40] Claudia Russo, Francesca Danioni, Ioana Zagrean, and Daniela Barni. Changing personal values through
value-manipulation tasks: a systematic literature review based on schwartzâC™s theory of basic human values.
European Journal of Investigation in Health, Psychology and Education, 12(7):692–715, 2022.

[41] Frank Tian-fang Ye, Bryant PH Hui, Jacky CK Ng, Ben CP Lam, Algae KY Au, Wesley CH Wu, Hilary KY
Ng, and Sylvia Xiaohua Chen. Social axioms and psychological toll: A study of emotional, behavioral, and
cognitive responses across 35 cultures during the covid-19 pandemic. Applied Psychology: Health and Well-Being,
16(4):1679–1698, 2024.

[42] Pulse Asia Research Inc. Ulat ng bayan: June 2024 nationwide survey on national concerns prior to the sona.

Research report, Pulse Asia Research Inc., July 2024. Accessed: 2025-04-16.

[43] A Timothy Church, Jose Alberto S Reyes, Marcia S Katigbak, and Stephanie D Grimm. Filipino personality

structure and the big five model: A lexical approach. Journal of Personality, 65(3):477–528, 1997.

12

---

<!-- PAGE 13 -->

Sentiment Simulation Using Generative AI Agents

[44] Gregorio EH Del Pilar. The development of the masaklaw na panukat ng loob (mapa ng loob). Philippine Journal

Of Psychology, 50(1):103–141, 2017.

[45] Mary Rachelle R Wapaño. Personality disorders and the five-factor model among filipino non-clinical sample.

International Journal of Research and Innovation in Social Science (IJRISS), V, 2021.

[46] Melrose Tia, Jerome Espina, and Jason Albia. Measuring political bias and framing effects in large language

models (llms): A sensitivity analysis. Manuscript in preparation, 2025.

[47] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle,
Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. arXiv preprint
arXiv:2407.21783, 2024.

[48] Kenneth O McGraw and Seok P Wong. A common language effect size statistic. Psychological bulletin,

111(2):361, 1992.

[49] Sunwoong Kim, Jongho Jeong, Jin Soo Han, and Donghyuk Shin. Llm-mirror: A generated-persona approach for

survey pre-testing. arXiv e-prints, pages arXiv–2412, 2024.

[50] Leo Yeykelis, Kaavya Pichai, James J Cummings, and Byron Reeves. Using large language models to create ai
personas for replication and prediction of media effects: An empirical test of 133 published experimental research
findings. arXiv preprint arXiv:2408.16073, 2024.

[51] Armin Falk and James J Heckman. Lab experiments are a major source of knowledge in the social sciences.

science, 326(5952):535–538, 2009.

[52] David Lazer, Devon Brewer, Nicholas Christakis, James Fowler, and Gary King. Life in the network: the coming

age of computational social science. Science, 323(5915):721–723, 2009.

[53] Daniel Kahneman and Amos Tversky. Choices, values, and frames. American psychologist, 39(4):341, 1984.
[54] Dennis Chong and James N Druckman. Framing theory. Annu. Rev. Polit. Sci., 10(1):103–126, 2007.
[55] Paul M Sniderman and Sean M Theriault. The structure of political argument and the logic of issue framing.

Studies in public opinion: Attitudes, nonattitudes, measurement error, and change, 3(03):133–65, 2004.

[56] Robert R McCrae and Paul T Costa Jr. Personality trait structure as a human universal. American psychologist,

52(5):509, 1997.

[57] Commission on Elections (COMELEC). 2022 registered voters and voters with accessible polling places (final).
https://comelec.gov.ph/?r=2022NLE/Statistics/2022RVVAVmcocfinal, 2022. Accessed: 2024-10-
01.

13

---

<!-- PAGE 14 -->

Sentiment Simulation Using Generative AI Agents

Supplementary Material

A. Survey Design and Implementation Details

A.1 Survey Design and Instrument Specifics

Specific psychological frameworks include personality traits (e.g., HEXACO personality), values (e.g., Basic Personal
Values), attitudinal frameworks (e.g., Affective Intelligence Theory), and beliefs (e.g., Social Axioms).
It also
In addition to the sociodemographics and
encompasses social and political behavior (e.g., Civic Engagement).
psychological frameworks, the survey instrument also includes an additional section to assess general citizen attitudes
toward four major economic issues (e.g., inflation, minimum wage, etc) and four key social issues (e.g., the West
Philippine Sea dispute, corruption, etc).

A.2 Survey Sampling

A multi-stage stratified random sampling design was used to obtain a nationally representative sample of 2, 485
Filipino adults [57]. The sample was proportionally distributed across the 17 administrative regions using probability
proportional to size. Systematic interval sampling selected five (5) households per sampled barangay, and one (1)
respondent per household was randomly chosen using gender-rotated probability to ensure balanced male and female
representation. This sampling design accounted for clustering at multiple geographic levels and stratification by region
and urbanicity. Data were collected through face-to-face interviews from November 22 to December 9, 2024. A hybrid
system of digital tablets and printed forms was used in the field to ensure both flexibility and high data fidelity.

A.3 Weighting Procedure

To correct for unequal selection probabilities inherent in the sampling design, design weights (base weights) were
computed from the joint probabilities of selection at each sampling stage: cities/municipalities, barangays, households,
and eligible respondents. These base weights were then adjusted using post-stratification techniques, anchored on
the official registered voter count data [57] by region and gender. This procedure ensured that the final weighted
sample reflected the actual distribution of registered voters, thereby improving the generalizability and precision of
population-level inferences and estimates.

A.4 Survey Implementation

Randomization techniques were applied to minimize selection bias, and interval sampling was employed to ensure
systematic coverage of both urban and rural areas. The use of in-person interviews allowed for greater engagement and
clarification of questions when necessary, contributing to higher response quality and completeness.

B. Agent Embodiment Setup

Figures 5 and 6 present the prompt formats used in the agent embodiment section of the sentiment simulation. Both
formats operationalize the presentation of sociodemographic and psychographic attributes to the language model,
serving as the foundation for generating agent-specific responses. The categorical format (Figure 5) conveys traits and
attributes through compact, labeled variables (e.g., Extraversion: HIGH), while the contextualized format (Figure 6)
embeds the same information within brief narrative descriptions, enriching each variable with interpretive context.

In both cases, bracketed fields (e.g., < age >, < incomerange >) represent placeholders dynamically populated with
real survey data during prompt instantiation. Text segments rendered in bold correspond to fixed prompt components
that remain consistent across all agents.

C. Agent Exposure to Scenario

Figure 7 presents the prompt structure used to expose an embodied agent to a situational stimulus and elicit a
corresponding affective judgment or sentiment response. In this format, the language model is prompted to imagine
being presented with a particular event, scenario, or statement, and to reflect on how it would personally resonate based
on the agent’s encoded background and perspective.

The < scenario > placeholder is dynamically filled with the target stimulus, while all bolded text constitutes fixed
instructional language consistent across all prompts. The model is then asked to identify the sentiment that best reflects
how someone with its assigned profile would most likely feel in response.

14

---

<!-- PAGE 15 -->

Sentiment Simulation Using Generative AI Agents

Figure 5: Prompt Format for Categorical Profile Encoding.

Figure 6: Prompt Format for Contextualized Profile Encoding.

15

---

<!-- PAGE 16 -->

Sentiment Simulation Using Generative AI Agents

Figure 7: Prompt Format for Instantiating Agent Exposure to Scenario.

D. Agent Response to Scenario

Figure 8 presents the full instruction sequence used to elicit a sentiment judgment, accompanying rationale, and
self-assessed alignment from an embodied agent profile. After being exposed to a scenario, the agent is instructed to
identify the sentiment that most accurately reflects how a person with that profile would likely respond.

In addition to selecting a sentiment from a standardized 5-point scale (Negative to Positive), the model is prompted to
articulate a brief explanation for its judgment. The < reason > placeholder denotes the position where the model is
expected to generate this response. Following this, the model is asked to critically evaluate whether its chosen sentiment
logically aligns with the profile’s described characteristics, including values, personal traits, and contextual background,
and to answer with a binary Yes or No. This prompt format supports deeper analysis of the model’s internal coherence,
linking sentiment expression to reasoning and value alignment within an embodied simulation context. Similarly, all
bolded segments represent fixed instructional text presented uniformly across prompts.

Figure 8: Prompt Format for Generating Agent’s Response to Scenario.

E. Quadratic Weighted Accuracy (QWA) as Evaluation Metric

Figures 9 and 10 present heatmaps of pairwise QWA scores, capturing the degree of alignment between agent-generated
responses and human responses across two core tasks: agent embodiment and sentiment simulation. In both figures,
each matrix cell represents the average agreement score for a specific pair of simulated and survey response values.

16

---

<!-- PAGE 17 -->

Sentiment Simulation Using Generative AI Agents

E.1 On Agent Embodiment Survey Replication Task

Figure 9 presents the QWA matrix for the survey replication task, where the model was prompted to generate Likert-scale
responses to psychographic survey items from the perspective of an embodied agent profile. The matrix shows pairwise
QWA scores between each simulated agent response (rows) and the corresponding human response (columns) on a
7-point ordinal scale.

Figure 9: QWA Matrix of Simulated and Human Responses in the Agent Embodiment Task.

E.2 On Sentiment Simulation Task

Similarly, Figure 10 shows the QWA matrix for the sentiment simulation task. Here, simulated sentiment responses are
compared to human sentiment ratings on a 5-point ordinal scale ranging from Negative to Positive.

Figure 10: QWA Matrix of Simulated and Human Sentiment Responses in the Sentiment Simulation Task.

17

---

<!-- PAGE 18 -->

Sentiment Simulation Using Generative AI Agents

F. Statistical Tests

Paired t-test was used when the assumption of normality was satisfied. The formula is given below:

t =

d
√
sd/

n

(2)

where:

d is the mean of the differences between paired observations;

sd is the standard deviation of the differences; and

n is the number of pairs.

For group comparisons in which the normality assumption was not met, we used the Wilcoxon signed-rank test, see
Equation 3.

W = min(W +, W −)

where:
W + is the sum of positive ranks;
W − is the sum of negative ranks; and

m is its sample size

Accordingly, the Z-score formula is given below:

Z =

W − µW
σW

where:

µW =

n(n + 1)
4

and σW =

(cid:114)

n(n + 1)(2n + 1)
24

n is the sample size of the groups.

(3)

(4)

In addition to hypothesis testing, we computed Cohen’s |d| to quantify the effect size and assess the practical relevance
of observed differences. Cohen’s |d| is calculated as:

|d| =

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

µ1 − µ2
(cid:113) s2
1+s2
2
2

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)

(5)

where:

µ1 and µ2 are the means of each group; and
1 and s2
s2

2 are the standard deviations of each group.

18

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

5202
yaM
82
]AM.sc[
1v52122.5052:viXra
SENTIMENT SIMULATION USING GENERATIVE AI AGENTS
MelroseTia1,JezreelSophiaLanuzo1,LeiRigiBaltazar1,
MarieJoyLopez-Relente2,DiwaMalayaQuiñones3,JasonAlbia1∗
1NetopiaAI,Inc.,Manila,Philippines
2InstituteofStatistics,UniversityofthePhilippinesLosBaños,Laguna
3DepartmentofPsychology,UniversityofthePhilippinesDiliman,QuezonCity
{melrose, sophia, lei, jason}@netopia.ai, {daquinones, mflopez2}@up.edu.ph
ABSTRACT
Traditionalsentimentanalysisreliesonsurface-levellinguisticpatternsandretrospectivedata,limiting
itsabilitytocapturethepsychologicalandcontextualdriversofhumansentiment. Theselimitations
constrain its effectiveness in applications that require predictive insight, such as policy testing,
narrativeframing,andbehavioralforecasting.Wepresentarobustframeworkforsentimentsimulation
usinggenerativeAIagentsembeddedwithpsychologicallyrichprofiles. Agentsareinstantiated
fromanationallyrepresentativesurveyof2,485Filipinorespondents,combiningsociodemographic
informationwithvalidatedconstructsofpersonalitytraits,values,beliefs,andsocio-politicalattitudes.
The framework includes three stages: (1) agent embodiment via categorical or contextualized
encodings, (2) exposure to real-world political and economic scenarios, and (3) generation of
sentiment ratings accompanied by explanatory rationales. Using Quadratic Weighted Accuracy
(QWA), we evaluated alignment between agent-generated and human responses. Contextualized
encodingachieved92%alignmentinreplicatingoriginalsurveyresponses. Insentimentsimulation
tasks,agentsreached81%–86%accuracyagainstgroundtruthsentiment,withcontextualizedprofile
encodings significantly outperforming categorical (p < 0.0001, Cohen’s d = 0.70). Simulation
results remained consistent across repeated trials (±0.2−0.5% SD) and resilient to variation in
scenarioframing(p=0.9676,Cohen’sd=0.02). Ourfindingsestablishascalableframeworkfor
sentimentmodelingthroughpsychographicallygroundedAIagents. Thisworksignalsaparadigm
shiftinsentimentanalysisfromretrospectiveclassificationtoprospectiveanddynamicsimulation
groundedinpsychologyofsentimentformation.
Keywords agenticsimulation·sentimentanalysis·sentimentsimulation·generativeAIagents·behavioralscience
1 Introduction
Sentimentanalysisinvolvesassessingtheopinionsandattitudestowardspecificareasofinterests,playingapivotal
role in influencing decisions across business, societal, and individual domains [1, 2]. While the term sentiment
analysisgainedprominenceintheearly2000s[3,4],thebroaderpracticeofgaugingpublicopinionhaslongshaped
policy-making,democraticdiscourse,andmarketingstrategies[5]. Asdigitalplatformsanduser-generatedcontent
increasinglyserveaschannelsforpublicexpression,sentimentanalysisenablesorganizationstoharnessopinion-rich
andunstructureddatatorefinecommunicationstrategiesandtorespondeffectivelytosocietaltrends.
Inthesocio-politicaldomain,sentimentanalysishassupportedapplicationsrangingfrompolicyevaluationtocampaign
strategybyenablinglarge-scaleinterpretationofpublicopinion. Examplesincludeassessmentsofpublicengagement
with government initiatives [6, 7, 8, 9], political campaign analysis [10, 11, 12], and citizen feedback monitoring
viasocialmedia[13]. Forinstance,Sandoval-Almazanetal. (2020)[10]examinedFacebookreactionstopolitical
campaignpostsinMexico,uncoveringpatternsinpublicengagement. InIndonesia,Sukmaetal. (2020)[7]analyzed
TwitterresponsestotheOmnibusLaw,revealinglevelsofpublicsupportanddissenttothepolicy. InthePhilippines,
∗Correspondingauthor:jason@netopia.ai

SentimentSimulationUsingGenerativeAIAgents
Mirandaetal. (2021)[12]trackedsentimentaroundpresidentialstateaddresses,whileUmalietal. (2020)[13]assessed
citizensatisfactionwithvariousgovernmentagenciesbasedonsocialmediacommentary.
Beyondpolitics,sentimentanalysisiswidelyusedintheprivatesector,whereitservesasacriticaltoolinmarketing,
advertising,andcustomerexperiencestrategies. Rathoreetal. (2020)[14],forexample,analyzedemotionalpatternsin
onlinecommentsbeforeandafterproductlaunchestoassessmarketreceptionandproductfit. Giannakisetal. (2022)
[15]showedhowconsumersentimentfromsocialmediacaninformearly-stageproductdevelopment,whileYinetal.
(2022)[16]studiedbrandloyaltyandsatisfactionthroughTwittersentimenttowarde-commerceplatformsLazadaand
Shopee. Inaddition,sentimentanalysishasalsobeenappliedtoevaluateconsumerreviewsforpredictingbehavior
andsatisfaction[17,18]andtogeneratereal-timecustomerinsights[19],therebycontributingtoproductrefinement,
enhancedcustomerengagement,anddata-drivenbusinessstrategies.
TraditionalSentimentAnalysisandTheirLimitations
Traditionalsentimentanalysisoftenreliesonstructuredmethodssuchassurveys,opinionpolls,andfocusgroups,
alongsidemorerecentdigitalsourceslikesocialmedia[2]. Theseapproacheshavepavedthewayintocomputational
techniques leveraging machine learning (ML) and natural language processing (NLP) to classify sentiment (e.g.,
negative,neutral,positive)basedonlarge-scaletextanalysis. Thesemethodsanalyzelinguisticpatterns,including
theuseofemotionallychargedwords(e.g.,“happy”,“disappointed”)andsyntacticstructuresthatconveyopinionor
emotions.
Despite advances in ML and deep learning models that boost classification accuracy [20], these approaches are
fundamentallylimited. First,theyprimarilycapturesurface-levellinguisticcues,oftenoversimplifyingthecomplexity
andnuanceofhumanemotionandopinion. Second,thesemodelsfunctionasblack-boxsystemsthatlacktransparency,
offeringlimitedinsightintothereasoningbehindsentimentpredictions[21]. Thislackofinterpretabilityimpairstrust,
accountability,andapplicabilityindomainsrequiringnuancedunderstanding.
Third, and perhaps most critically, current sentiment analysis techniques often fail to account for contextual and
psychologicalfactors,includingindividualbiases,personalitytraits,values,ortemporalcircumstances[22,23,24]. For
example,Mahmoudi(2021)[22]emphasizeshowuser-levelbiasescanleadtodivergentinterpretationsofthesame
event,whichareoftenignoredintraditionalmodels. Becausethesesystemstypicallyofferretrospectivesummaries
ratherthandynamicsimulations,theystruggletosupportforward-lookingapplicationssuchaspolicytesting,narrative
impactstudies,orsyntheticfocusgroups[25].
Toillustrate,asentimentmodeltrainedonsocialmediapostsfromapriorelectionmayaccuratelyclassifypolitical
opinionsfromthatperiod[26,27],butitcannotsimulatehowaspecificgroup—suchasrural,first-timevoters,might
react to a new policy announcement or media event. These limitations reveal a broader issue: these models are
inadequatetomodelsentimentassituatedcognition,thatis,anemergent,psychologicallygroundedresponseshapedby
internaldispositionsandexternalstimuli[28].
SentimentSimulationusingAIandBehavioralScience
Rooted in the above challenges, we propose a conceptual shift: from retrospective sentiment classification to AI
andbehavioralscience-drivensentimentsimulation. Thisapproachintegratestwocoreparadigms: (1)abehavioral
scienceframeworkthatexplainshowsentimentsarisefrompsychologicaldrivers,and(2)asimulation-basedmodeling
paradigmenabledbygenerativeAI.
Behavioralscienceprovidesthetheoreticalfoundationforthisshift. Itconceptualizessentimentasadynamicconstruct
shapedbycognition,emotion,andsituationalcontext. Socialpsychologysuggeststhatsentimentreflectsattitudes
formedfrombeliefs,values,andenvironmentalfactors—factorsthat,inturn,shapebehavior[29]. Acomplementary
analysisbyLiandHovy(2017)[30]furtherarguethatsentimentoriginatesfromemotionallydrivenpreferencesand
thepursuitofpersonalgoals. Theseperspectivessuggestthatsentimentisnotjustatextualartifactbutabehavioral
expressionrootedinindividualpsychology.
In methodical perspective, unlike traditional models that classify past sentiment, generative models such as large
languagemodels(LLMs)enableprospectivesimulationsthatcangeneratebehaviorallyrich,context-sensitivesenti-
ment. Thesegenerativemodelscansimulatetrustdynamics[31],personalityexpression[32],andopinionformation
[33]—capabilitiesthatalignwellwithpsychologicalrealism. Inaddition,generativemodelshasalsocatalyzednew
researchonsyntheticpopulationsandsimulatedhumanstudies[34,35],positioninggenerativeAIasapowerfultool
forbehavioralscience. RepresentativestudiesillustratingtheseadvancesaresummarizedinTable1.
2

SentimentSimulationUsingGenerativeAIAgents
Table1: Recentstudiesthatinformandsupportthiswork,highlightingtheirdomainsandkeyfindings.
Study Domain KeyFindings
UsingLLMstoSimulate BehavioralEconomics Simulatedclassicbehavioralstudies(e.g.,Ultimatum
MultipleHumansand andSocialPsychology Game, Milgram)andfoundthatlargerLLMs(GPT-
ReplicateHumanSubject 3.5/4)couldreplicateestablishedfindingsacrosseco-
Studies[32] nomics,psycholinguistics,andsocialpsychology.
GenerativeAgents: Human-AIInteraction Introduced"generativeagents"—LLM-drivenagents
InteractiveSimulationsof withmemory,planning,andreflection. Demonstrated
HumanBehavior[36] emergentbehaviorininteractiveenvironments(e.g.,
autonomously organizing a Valentine’s Day party)
fromasingleprompt.
GenerativeAgentSimulations SocialScience DevelopedanLLM-basedagentarchitecturetosimu-
of1000People[24] late1,052realindividualsbasedoninterviews.Agents
replicated survey responses with ≈ 85% accuracy,
comparabletohumans’ownretestaccuracy,andpre-
dictedpersonalitytraitswell.
UserBehaviorSimulation UserBehavior DevelopedanLLM-basedframeworkforsimulating
withLLM-basedAgents[37] Simulation userbehaviors(e.g.,webnavigation). Capturedsocial
dynamicslikeconformityandinformationcocooning.
CanLargeLanguageModel BehavioralEconomics UsedTrustGamestoevaluateagentbehavior. GPT-4
AgentsSimulateHumanTrust agentsshowedtrust-likebehaviorandstrongalignment
Behavior? [31] withhumanresponsesinsocialdilemmas.
EvaluatingtheAbilityof PersonalityModeling GPT-4 simulated individuals with Big Five profiles.
LLMstoEmulatePersonality Generatedresponsesshowedhighinternalconsistency
[38] andstrongcorrelationwithself-reportedpersonality
scores.
WhiletheabovepriorstudieshaveillustratedpotentialofLLMstosimulatebehaviors,replicatehumanexperiments,or
modeltrust,nonehaveyetgroundedsentimentsimulationinrealpsychographicsurveydata. Ourworkfillsthisgapby
embeddingpsychologicallyvalidatedprofilesintogenerativeAIagentstosimulatehowrealpeoplemightrespondto
socio-politicalandeconomicscenarios.
ContributionoftheArticle
Inthisstudy, wepresentasimpleandscalablegenerativeAIagenticframeworkviastructuredLLMpromptingto
simulatethesentimentresponseofthesurveyrespondentsonseveralsocio-politicalandeconomicscenarios. The
AIagentswereinstantiatedtoembodythepsychologicalprofilesderivedfromnationallyrepresentativesurveyand
theirsimulatedresponseiscomparedwiththegroundtruthdata. Moreprecisely,thecontributionsofthisworkareas
follows:
• WedemonstratethatAIagentscanbeeffectivelyinstantiatedtoembodythepsychologicalprofilesconstructed
from empirically generated data. These profiles incorporate socio-demographic data and variables from
validatedpsychologicalframeworksandattitudesonkeysocio-politicalandeconomicissues,providingagents
withpsychographicallygroundedpriors.
• We show that these AI agents are capable of replicating survey results, as well as sentiment distributions
observed in real-world responses, achieving high levels of individual-level alignment. Furthermore, we
demonstratethatagentresponsesarerobustacrossalternativeframingsofthesamescenarios,indicatingthe
consistencyandstabilityofoursimulationframework.
3

SentimentSimulationUsingGenerativeAIAgents
2 Methodology
2.1 SurveyDesignandDataCollection
The survey instrument was designed to provide an interdisciplinary understanding of Filipino citizens’ profiles by
integratingmultiplewell-establishedpsychologicalframeworkstocaptureadeeperunderstandingofpublicsentiment
towardsvarioussocio-politicalandeconomicissuesinthePhilippines.
Theinstrumentconsistsof150items,integratingbothsociodemographicvariables(age,sex,educationalattainment,
religion, and other key identifiers) and different psychological dimensions (personality traits, values, attitudinal
frameworks,beliefs,andsocialandpoliticalbehavior). Theseframeworksaretheoreticallygroundedandconsidered
temporallystable[39,40,41],allowingfortheabstractionofconsistentpsychographicprofiles. Forgreatersensitivity
incapturingtheintensityanddirectionofrespondents’responses,mostframeworksweremeasuredusinga7-point
Likertscale. Respondentswereaskedtoexpresstheirlevelofagreementordisagreementwithstatementsaboutselected
majorsocio-politicalandeconomicissues[42].
Descriptivestatisticsofanationallyrepresentativesampleof2,485registeredFilipinovoterswith95%confidence
leveland1.97%marginoferroraresummarizedinTable2. Therespondents’agerangedfrom18to89yearsold,
withthemajority(33%)fallingwithintheadultagegroup(28−42yearsold). Thesamplewasgender-balanced(50%
female,50%male),andthemajorityweremarried(57%). Intermsofsocioeconomicstatus,nearlyhalfofthesample
(49%)reportednomonthlyincome,while30%werecategorizedaslowincome. Mostparticipantshadcompletedat
leasthighschool(52%)orcollege(21%).
Table2: Descriptivestatisticsofthestudysample(N =2,485).
Variable Category Count(RelativeProportion)
AgeGroup
YoungAdults(18–27YearsOld) 399(16%)
Adults(28–43YearsOld) 820(33%)
Middle-AgedAdults(44–59YearsOld) 736(30%)
Seniors(60+YearsOld) 530(21%)
MaritalStatus
Single 380(15%)
Live-In 395(16%)
Married 1413(57%)
Separated 77(3%)
Widowed 220(9%)
MonthlyIncome-BasedSocioeconomicStatus
NoIncome 1213(49%)
LowIncome 740(30%)
MiddleIncome 530(21%)
HighIncome 2(<1%)
HighestEducationalAttainment
NoFormalEducation 8(<1%)
AtleastElementary 502(20%)
AtleastHighSchool 1294(52%)
AtleastVocational 152(6%)
AtleastCollege 525(21%)
AtleastGraduateStudies 4(<1%)
Toourknowledge,ourdatarepresentsthelargestandmostdemographicallydiversesamplesinthePhilippinesusedto
examinepsychologicalframeworks,offeringarobustbasisforgeneralizingthefindingstothebroaderadultpopulation.
PreviouspsychologicalstudiesintheFilipinosamples,suchasthosebyChurchetal. (1997)[43](N =629),DelPilar
(2017)[44](N =576),andWapaño(2021)[45](N =828),wereconductedwithsmaller,morelocalizedsamples.
4

SentimentSimulationUsingGenerativeAIAgents
2.2 SentimentSimulation
ThesentimentsimulationframeworkleveragesgenerativeAIagents,embodiedwithpsychographicandcontextual
variables,tomodelthesentimentofrespondentsinresponsetovaryingsocio-politicalandeconomicscenarios. The
frameworkenablesgenerativeagentstoproducedynamicsentimentresponsesthatarenotonlyreactivetoinputstimuli
butalsoalignedwiththeirinternalpsychologicalattributesandcontextualstimuli. AsshowninFigure1,thesimulation
frameworkconsistsofthree(3)corestages: AgentEmbodiment,AgentExposuretoScenarios,andAgentResponseto
Scenarios.
AllsimulationswereconductedusingLlama3.170B1,astate-of-the-artopen-weightLLMoptimizedforinstruction
following,long-contextreasoning,andalignmentwithhumanintent. Thismodeliswell-suitedforsimulatingagent
behaviorwithinpsychologicalframeworksduetoitsarchitecturethatsupportsmulti-turncoherenceandrobustlanguage
understanding[47].
Figure1: SentimentSimulationFrameworkUsingAIAgents.
2.2.1 AgentEmbodiment
EachAIagentisembodiedwithauniquesetofsociodemographicandpsychographicvariablesderivedfromempirical
survey. Thesevariableswereembeddedintoprompttemplatesusingoneoftwoencodingstrategies: categoricalor
contextualized.
• Categoricalencodinginvolvedassigningdiscretelabels(e.g.,Low,Moderate,High)toeachpsychological
variable,producingastructuredbutabstractrepresentationofpersonalityandattitudes.
• Contextualizedencoding,bycontrast,translatedthesecategoriesintonarrativedescriptionsthatreflecthow
psychologicalvariablesmightmanifestinscenario-relevantcontexts. Forexample,highopennessinpolicy
domainmightbeexpressedasreceptivetonewpolicyideasorpronetoconsideringmultipleperspectives.
1Llama3.170BwasselectedfollowingrigorousexperimentationwithvariousLLMsevaluatingtheirsensitivitytopoliticaland
linguisticbias.[46]
5

SentimentSimulationUsingGenerativeAIAgents
Toevaluatetheeffectivenessofembodiment,weconductedasurveyreplicationtaskwhereineachagent,embodied
withaspecificrespondent’sprofile,answeredthesameLikert-scalesurveyitemsasthehumanparticipant. Thistask
assessedwhethertheagentcouldfaithfullyreflecttheindividual’spsychologicalprofilethroughsimulatedresponses.
2.2.2 AgentExposuretoScenario
In this phase, agents were presented with real-world scenarios analogous to campaign messages, policy debates,
economic developments, or media coverage of socio-political and economic issues: budget transparency, political
dynasties,inflation,thejusticesystem,andwagepolicies. Thesescenariosarecraftedasnarrativepromptsdesignedto
elicitaffective,cognitive,andpsychographicallygroundedresponses,engagingtheagent’sinternaldispositions.
In addition, to examine the impact of scenario framing effects, each scenario was presented with either positive
or negative polarity, simulating ideological differences in real-world discourse (e.g., progressive vs. conservative
perspective). Respondentswererandomlyassignedtooneframingtype,whileensuringequaldistributionofframing
acrosstheentiresamplepopulation.
2.2.3 AgentResponsetoScenario
Followingscenarioexposure,eachagentproducedastructuredsentimentresponse,ratedona5-pointLikertscale
(Negative,SlightlyNegative,Neutral,SlightlyPositive,andPositive),alongwithabriefexplanatoryrationaleforits
simulatedsentiment.
Aftergeneratingitsinitialsentiment,theagentwaspromptedwithaself-assessmenttask,askingwhetheritsresponse
was logically consistent with its psychographic profile and the characteristics of the scenario (see Supplementary
MaterialD).Thisiterativevalidationstepreinforcedcoherenceandinternalconsistencywithinthesimulatedresponses.
2.3 PerformanceEvaluationMetrics
2.3.1 QuadraticWeightedAccuracy(QWA)
QWAwasemployedastheprimarymetrictoevaluatealignmentbetweenagent-generatedandhumanresponsesonan
ordinalscale. Itpenalizesdistantmisclassificationsmoreheavilythannear-misserrors,makingitparticularlysuitable
forLikert-scaleclassificationtasks,whereresponsecategoriesareinherentlyordered.
TheQWAscoreiscomputedusingEq.(1),withweightsthatincreasequadraticallybasedonthedistancebetween
simulatedandactualresponses. Thisscoringmethodallowsforamorenuancedassessmentofmodelperformance,
rewardingresponsepredictionsthatareclosetotheexpectedvalueevenwhentheyarenotexactmatches.
(cid:18)
d
(cid:19)2
w =1− ij (1)
ij d
max
where:
w isthescoreassignedtothepairofcategoriesi(trueresponse)andj (simulatedresponse);
ij
d istheabsolutedistancebetweenthetrueandsimulatedresponsecategories;and
ij
d isthemaximumpossibledistancegiventherangeofallpossibleresponsecategories.
max
HigherQWAscoresindicatethattheagents’responsesarestatisticallyaccurateandinternallycoherent,i.e.,interpretable
withinthecontextoftheirembodiedpsychologicalprofiles. ScorematricesarevisualizedinSupplementaryMaterials
E.1andE.2.
2.3.2 StatisticalTests
Toevaluatethestatisticalsignificanceofobserveddifferencesinagent–humanalignment,weemployedbothparametric
(pairedt-test)andnon-parametric(Wilcoxonsigned-rank)analysis,dependingonthedistributionalpropertiesofthe
QWAscores. Specifically,pairedt-testwasusedwhentheassumptionofnormalitywassatisfied,whereasWilcoxon
signed-ranktestwasappliedwhenthisassumptionwasviolated,duetotheirrobustnesstonon-normaldistributions. A
commonlyusedthresholdofp<0.05wasusedtodeterminestatisticalsignificance.
Inadditiontohypothesistesting,wecomputedCohen’sdtoestimateeffectsizesandassessthepracticalrelevanceof
observeddifferences. Effectsizeswereinterpretedusingstandardbenchmarks: d≈0.2(small),d≈0.5(medium),
andd ≥ 0.8(large). Thisdualapproachenabledarobustinterpretationensuringthatthereportedimprovementsin
alignmentwerenotonlystatisticallysignificantbutalsopracticallymeaningful.
6

SentimentSimulationUsingGenerativeAIAgents
3 ResultsandDiscussion
3.1 AgentEmbodimentEvaluation
Agentembodimentwasimplementedusingtwodistinctencodingstrategies: categoricalencoding,whichusesranked
labels(e.g.,Low,Moderate,High),andcontextualizedencoding,whichembedspsychologicalvariablesintonarrative
descriptions. Thesestrategiesofferdifferinglevelsofabstractioninrepresentingindividualprofiles,allowingusto
comparetheireffectsonsimulatedsentimentalignment.
TheseencodingstrategiesdrawfromrecentworksthatattempttoembedpsychologicaltraitsintoLLMprompts. For
example,Wangetal. (2025)[38]usedpersonalityassessmentdata,albeitlimitedtonumericBigFivescores,toprompt
GPT-4insimulatingindividualbehaviors. Theirmethodmirrorsourcategoricalencodingapproach,whichalsodraws
fromempiricaldatabuttranslatesscoresintorankedlabelssuchasLow,Moderate,orHigh. Incontrast,Xieetal.
(2024)[31]usedstructuredpromptswithdemographicandbackgrounddetails,similartoourcontextualizedstrategy,
toelicittrustbehaviorsfromLLMs. Ourstudyadvancestheseeffortsbygroundingbothencodingstrategiesinreal
large-scalesurveydata,allowingsystematiccomparisonsbetweenencodinglevels.
AgentalignmentwithhumansurveyresponsesismeasuredusingQWA,whereidenticalratingsyield100%accuracy
scoreandone-pointdifferencesresultinproportionallylowerscoreof97%,capturingthedegreeofordinalmisalignment.
SeeSupplementaryMaterialE.1fordetails.
Figure2illustratesthedistributionofQWAscoresforthetwoencodingstrategies. Thecontextualizedgroup’scurve
(blue) is consistently right-shifted, indicating that a larger proportion of agents achieved higher alignment scores
compared to their categorically encoded counterparts. This population-level trend suggests that narrative profile
encodingenablesmorehuman-consistentresponses.
Figure2: CumulativeDistributionFunction(CDF)Plot: Distributional
ComparisonofQWAScoresAcrossProfileEncodingStrategies.
Figure3offersanagent-levelcomparison. Eachlineconnectsthecategoricalandcontextualizedscoresforasingle
agent, highlighting changes in alignment. Most lines extend rightward, reinforcing that contextualized encoding
generallyresultsinimprovedalignmentforindividualagents.
To determine whether the observed performance difference was statistically significant, we employed a Wilcoxon
signed-ranktest. PreliminarydiagnosticsusingtheShapiro–Wilktestindicatedviolationsofnormality(p=0.0004,
justifyingtheuseofanon-parametricapproach.TheWilcoxonsigned-ranktestyieldedasignificantresult(p<0.0001),
suggestingthatthealignmentadvantageofcontextualizedprofileencodingisunlikelytobeattributabletorandom
variation. Toassessthepracticalsignificanceofthiseffect,wecalculatedCohen’sd = 0.70,indicatingamoderate
effectsize. Interpretedprobabilistically,thisreflectsa76%chancethatarandomlyselectedagentwithcontextualized
encoding would outperform one using categorical encoding in response alignment [48]. These findings provide
statisticalandpracticalevidencethatcontextualizedprofileencodingyieldsbetteralignmentwithhumanresponses
comparedtocategoricalencoding.
7

SentimentSimulationUsingGenerativeAIAgents
| Figure3: PairedDotPlot:                                                       | Per-AgentComparisonofQWAScoresAcrossProfile |     |     |
| ----------------------------------------------------------------------------- | ------------------------------------------- | --- | --- |
| EncodingStrategies. Theverticalaxisrepresentsagentsthatareindexedarbitrarily. |                                             |     |     |
Onaverage,agentsusingcontextualizedprofilesachieved92%alignmentwithoriginalhumanresponses,demonstrating
themodel’scapacitytosimulateindividual-levelpsychographicdatawithhighfidelity. Theseresultscomparefavorably
withprioreffortssuchas[49],whichintroducedtheLLM-MirrorframeworktoassesstheconsistencybetweenLLM-
generatedresponsesandhumansurveydata. Whiletheirpersona-basedpromptingachieved69%to73%consistency
indomainslikeonlineadvertising,corporatereputation,andcustomerloyalty,ourapproachreachesnotablyhigher
alignmentlevelsacrossabroaderarrayofpsychologicalconstructs. Similarly,Yeykelisetal. (2024)[50]foundthat
AIpersonascouldreproducefindingsfromexperimentalmediastudieswitha76%successrate. Our92%alignment
suggestsastrongercapacitytosimulatenuancedattitudinaldata,particularlywhennarrativecontextisusedtoexpress
psychologicalvariables.
Collectively,theseresultsdemonstratethatcontextualizedpsychologicalprofileencodingsignificantlyenhancesagent-
humanalignmentandproducesmoreconsistentresponses. Contextualizedencodingsguideagentsmoreeffectively
by embedding psychological traits within descriptive, scenario-relevant narratives. The performance gap between
categorical and contextualized encodings highlights the benefits of translating psychological variable labels into
richpsychographiccontexts,enablingagentstorespondmoreaccuratelyinalignmentwiththeirprofiles—acritical
foundationforgeneratingpsychologicallycoherentsentimentsimulations.
3.2 SentimentSimulationPerformance
Followingthehighalignmentobservedintheagentembodimenttask,wenextevaluatetheabilityofpsychographically
groundedagentstosimulatehumansentimentacrossasetofsocio-politicalandeconomicscenarios: wagepolicies,
budgettransparency,inflation,thejusticesystem,andpoliticaldynasties. Thisanalysisprovidesabroadertestofthe
model’sabilitytogeneratehumansentimentresponsesinreal-worldcontexts.
Table3: SentimentSimulationAccuracyAcrossSocio-PoliticalandEconomicScenarios.
| Scenario           | Categorical |        | Contextualized |
| ------------------ | ----------- | ------ | -------------- |
|                    | Average     | SD     | Average SD     |
| WagePolicies       | 80.3%       | ±0.19% | 83.4% ±0.20%   |
| BudgetTransparency | 80.1%       | ±0.21% | 82.9% ±0.33%   |
| Inflation          | 74.9%       | ±0.32% | 81.8% ±0.17%   |
| JusticeSystem      | 86.7%       | ±0.39% | 86.2% ±0.26%   |
| PoliticalDynasties | 68.4%       | ±0.20% | 81.2% ±0.51%   |
Table3summarizessentimentalignmentperformanceacrossthescenarios,comparingcategoricalandcontextualized
encodingstrategies. Asshown,contextualizedencodingconsistentlyoutperformedcategoricalencodinginfouroutof
fivescenarios,withalignmentaccuracygainsrangingfrom2.8%to12.8%points. Whilecategoricalencodingachieved
8

SentimentSimulationUsingGenerativeAIAgents
accuracylevelsrangingfrom68%to87%,contextualizedprofileencodingyieldedmorestableandhigherperformance
of81%to86%.
Thelargestaccuracygainoccurredinthepoliticaldynastiesscenario(+12.8%),followedbyinflation(+6.9%). For
wage and budget transparency, improvements were more modest (+2.8% and +3.1%, respectively). Interestingly,
performancewasnearlyidenticalinthejusticesystemscenario(−0.5%),suggestingthatsomescenariosmaybeless
influencedbyinternalpsychologicalfactorsandmoredrivenbyideologicalalignmentorexternalcues.
Thesefindingsreinforcethatsentimentsimulationisenhancedwhenagentsaregroundedincontextuallyexpressed
psychologicaltraits,notmerelycategoricalsummaries. Themorerealisticallyanagent’sinternaldispositionismodeled,
themoreaccuratelyitmirrorshumanresponses. Thissupportsexistingresearch[31]indicatingthatcontextualrichness
improvesbehavioralrealisminLLMsimulations.
Considering the inherent variability of LLMs, stemming from prompt sensitivity and randomness introduced by
stochasticdecoding,weevaluatedthestabilityofsimulationoutputsoverrepeatedtrials. Eachscenariowassimulated
five (5) times, and performance was averaged to assess internal consistency. As shown also in Table 3, sentiment
alignment scores were highly stable, with standard deviations for contextualized encoding ranging from ±0.17%
to±0.51%,indicatingminimalvariabilityinperformanceacrosstrials. Moreprecisely,thejusticesystemscenario
exhibitedthehighestandmoststableperformance,withQWAscoresrangingnarrowlyfrom86.0%to86.7%. Wage
policiesandbudgettransparencyalsoshowedstrongstability,withQWAscoresclusteredtightlyaroundthemid-83%
range. Inflationfollowedasimilartrend,withminorfluctuationsaround82%. Althoughpoliticaldynastieshadthe
lowestoverallscores,rangingfrom80.1%to81.4%,thevariationacrosstrialswasstillminimal,indicatinginternal
consistencyevenincomparativelymorecomplexorideologicallyloadedscenarios.
Ultimately,ourframeworkachievedhighalignmentperformanceacrossalltestedscenarios(81%to86%),reflectingnot
onlythepredictiveaccuracyofthemodel,butalsoitsbehavioralplausibility. Theframework’sconsistencyacrosstrials
isillustrativeofitssuitabilityforuseinreplicableandscalablebehavioralsimulations. Ourfindingshighlightthree
pillarsofeffectivesimulationinbehavioralsciencespecificallyinsocialsciences: (1)psychologicalgroundingthrough
contextualizedtraits,(2)consistencyofperformanceacrossdiverseandcomplexscenarios,and(3)sentimentalignment
withempiricallyplausiblehumanbehavior[51,52]. Moreover,inlightofthevariabilityinherentinemotionalreasoning
andtheinfluenceofframingonanindividual’sjudgment[53],ourresultsspeaknotonlytotechnicalperformance,but
tothepsychologicalcredibilityofthesimulatedagentsthemselves.
3.2.1 SimulationRobustnesstoScenarioFraming
Tofurtherevaluatetheframework’sgeneralizability,weinvestigateditssensitivitytoframingeffects,i.e.,whether
sentimentalignmentvariedsubstantiallydependingonwhetherascenariowaspresentedinapositiveornegativelight
(e.g.,performingwellunderpositiveframingbutpoorlyundernegativeframing). Thisstepisimportantgiventhat
priorstudiesinbehavioralsciencesandcommunicationhaveshownthatframingcansubstantiallyalterpublicopinion
[54,55].
Figure4: QuadraticWeightedAccuracyBetweenSurveyandSimulatedSentiments
AcrossFramingTypesoftheDifferentScenarios.
Figure4showsaplotcomparisonbetweentheaverageQWAforpositive(blue)andnegative(orange)framingsfor
eachscenario. Acrossthefivesocio-politicalandeconomicscenarios,QWAscoresremainedhigh77%to88%,withno
consistentperformancedegradationoramplificationduetoframing. Whiledifferencesbetweenthepositively-and
9

SentimentSimulationUsingGenerativeAIAgents
negatively-framedscenariosrangedfrom0.4%to9.7%,thedirectionalityandmagnitudeofthesedifferencesvaried
acrossscenarios. Forexample,negatively-framedscenariosyieldedhigheralignmentininflation(+9.7%)andpolitical
dynastytopics(+0.4%),whereaspositively-framedscenariosoutperformedinjusticesystem(+4.3%),wagepolicies
(+4.4%),andbudgettransparency(+0.9%).
Inaddition,tofurtherevaluatewhetherscenarioframinginfluencessentimentsimulationaccuracy,weconducteda
pairedsamplet-testcomparingagent–humanalignmentscoresacrosspositively-andnegatively-framedversionsof
eachissue. Thepairedt-testwaschosentoassessmeandifferencesbetweenframingconditions,withtheShapiro–Wilk
testconfirmingthatthenormalityassumptionwassufficientlymet(p=0.1388). Theanalysisyieldedanon-significant
result(p=0.9676),indicatingnostatisticallymeaningfuldifferenceinsimulationaccuracyacrossframingconditions.
Furthermore,toquantifythemagnitudeofanypotentialeffect,wecomputedCohen’sd=0.02,reflectinganegligible
effectsize. ThissuggeststhatthedifferenceinQWAscoresbetweenframingconditionsispracticallyinsignificant,
withsentimentalignmentperformanceremainingstableregardlessofscenariopromptframing.
Collectively,theseresultsindicatethatscenarioframingdoesnotexertaconsistentormeaningfulinfluenceonsimulation
accuracy. Theframeworkallowsagentstoanchortheirevaluationstotheirpsychologicalattributes,ratherthanbeing
influencedbythedifferencesinthescenariopolarityframing.
These findings suggest that the agents remained anchored to their psychographic grounding, even under affective
variationinscenarioprompts. Fromabehavioralscienceperspective,thismirrorstheconsistencyofhumanbehavior
acrossvariedcontexts,asdocumentedinresearchontrait-basedmodels[56]. Thiscoherencesupportsthenotionthat
rich,context-sensitiveembeddingsenablepsychologicallygroundedratherthancontext-reactiveresponses.
4 Conclusion
Thisstudypresentsapsychographicallygroundedframeworkforsentimentsimulation,leveraginglanguagemodel
agentsembodiedwithempiricallyderivedpsychologicalprofiles. Byintegratingvalidatedconstructsintostructured
prompts,weenableAIagentstosimulatesentimentresponsesthatarecontext-sensitive,psychologicallycoherent,and
behaviorallyplausible.
Ourevaluationdemonstratesthatagentsinstantiatedwithcontextualizedprofileencodingscloselyreplicateindividual-
levelsentimentpatterns. Inasurveyreplicationtask,theseagentsachievedalignmentscoresofupto92%,significantly
outperformingcategoricalencodingstrategies. Thisresultunderscorestheimportanceofnarrative-richrepresentations
incapturingthedepthandnuanceofhumansentiment.
Beyondstaticreplication,theframeworkalsoperformsreliablyindynamicsimulationtasks. Whenexposedtoreal-
worldsocio-politicalandeconomicscenarios,agentsachievedhighalignmentaccuraciesindicatingtheircapacityto
modelrealisticsentimentresponses. Importantly,theseresultsremainedhighlystableacrossfiveindependenttrials
anddifferentscenarioframings,highlightingtheinternalconsistencyoftheframeworkdespitethestochasticnatureof
languagemodels.
Overall,theseresultsestablishareliable,scalable,andpsychologicallyinformedmethodformodelingpublicsentiment.
The framework offers practical applications in policy testing, narrative framing analysis, and the development of
syntheticpopulationsforlarge-scalesocialsimulation. Morebroadly,thisworkmarksaparadigmshift—fromretro-
spectivesentimentclassificationtowardprospective,psychologicallygroundedsimulationleveragingtheintersectionof
generativeAIandbehavioralsciences.
Acknowledgments
WeextendoursincerethankstoMojhuneGabrielManzanilloforhisdedicatedworkingeneratingtheexperimental
results for this study. We also gratefully acknowledge Adrian Gabonada for his insightful contributions, which
significantlyenrichedthebehavioralscienceinterpretationandthediscussionofourfindings. WefurtherthankDannah
ZemirahJunioforherguidanceonstatisticalanalysis;herinputwasinstrumentalinensuringtherigorandvalidityof
ourevaluationmethods. Modelinferencesandsentimentsimulationwereperformedusingcomputeresourcesprovided
bytheGoogleCloudforStartupsProgram.
References
[1] BoPang,LillianLee,etal. Opinionminingandsentimentanalysis. FoundationsandTrends®ininformation
retrieval,2(1–2):1–135,2008.
10

SentimentSimulationUsingGenerativeAIAgents
[2] BingLiu. Sentimentanalysisandopinionmining. SpringerNature,2012.
[3] TetsuyaNasukawaandJeongheeYi. Sentimentanalysis: Capturingfavorabilityusingnaturallanguageprocessing.
InProceedingsofthe2ndinternationalconferenceonKnowledgecapture,pages70–77,2003.
[4] KushalDave,SteveLawrence,andDavidMPennock. Miningthepeanutgallery:Opinionextractionandsemantic
classificationofproductreviews. InProceedingsofthe12thinternationalconferenceonWorldWideWeb,pages
519–528,2003.
[5] VincentPriceandPeterNeijens. Opinionqualityinpublicopinionresearch. InternationalJournalofPublic
OpinionResearch,9(4):336–360,1997.
[6] YannisCharalabidis,ManolisMaragoudakis,andEuripidesLoukis. Opinionminingandsentimentanalysisin
policyformulationinitiatives:Theeu-communityapproach.InElectronicParticipation:7thIFIP8.5International
Conference,ePart2015,Thessaloniki,Greece,August30–September2,2015,Proceedings7,pages147–160.
Springer,2015.
[7] EkiAidioSukma,AchmadNizarHidayanto,AdamImansyahPandesenda,ArifNurYahya,PuntoWidharto,and
UntungRahardja. Sentimentanalysisofthenewindonesiangovernmentpolicy(omnibuslaw)onsocialmedia
twitter. In2020InternationalConferenceonInformatics,Multimedia,CyberandInformationSystem(ICIMCIS),
pages153–158.IEEE,2020.
[8] JiriHradec,NicoleOstlaender,AlbaBernini,etal. Fables: frameworkforautonomousbehaviour-richlanguage-
drivenemotion-enabledsyntheticpopulations. Technicalreport,JointResearchCentre,2023.
[9] JanaFlorVVizmanos,SheilaVSiar,JoseRamonGAlbert,JaninaLuzCSarmiento,andAngeloCHernandez.
Like,comment,andshare: Analyzingpublicsentimentsofgovernmentpoliciesinsocialmedia. Technicalreport,
PIDSDiscussionPaperSeries,2023.
[10] RodrigoSandoval-AlmazanandDavidValle-Cruz. Sentimentanalysisoffacebookusersreactingtopolitical
campaignposts. DigitalGovernment: ResearchandPractice,1(2):1–13,2020.
[11] CharlesCrabtree,MattGolder,ThomasGschwend,andIndrid¯iHIndrid¯ason. Itisnotonlywhatyousay,itisalso
howyousayit: Thestrategicuseofcampaignsentiment. TheJournalofPolitics,82(3):1044–1060,2020.
[12] JohnPaulPMirandaandRexPBringula. ExploringphilippinepresidentsâC™speeches: Asentimentanalysis
andtopicmodelingapproach. CogentSocialSciences,7(1):1932030,2021.
[13] JulietaMUmali,JohnPaulPMiranda,andAniciaLFerrer. Sentimentanalysis: Acasestudyamongtheselected
governmentagenciesinthephilippines. InternationalJournal,9(3),2020.
[14] AshishKumarRathoreandPVigneswaraIlavarasan. Pre-andpost-launchemotionsinnewproductdevelopment:
Insightsfromtwitteranalyticsofthreeproducts. InternationalJournalofInformationManagement,50:111–127,
2020.
[15] Mihalis Giannakis, Rameshwar Dubey, Shishi Yan, Konstantina Spanaki, and Thanos Papadopoulos. Social
mediaandsensemakingpatternsinnewproductdevelopment: demystifyingthecustomersentiment. Annalsof
OperationsResearch,308:145–175,2022.
[16] JennyYowBeeYin,NorHaslizaMdSaad,andZulnaidiYaacob. Exploringsentimentanalysisone-commerce
business: Lazadaandshopee. Temjournal,11(4):1508,2022.
[17] Praphula Kumar Jain, Rajendra Pamula, and Gautam Srivastava. A systematic literature review on machine
learningapplicationsforconsumersentimentanalysisusingonlinereviews. Computersciencereview,41:100413,
2021.
[18] PawanjitSinghGhatora,SeyedEbrahimHosseini,ShahbazPervez,MuhammadJavedIqbal,andNabilShaukat.
Sentiment analysis of product reviews using machine learning and pre-trained llm. Big Data and Cognitive
Computing,8(12):199,2024.
[19] JanOleKrugmannandJochenHartmann. Sentimentanalysisintheageofgenerativeai. CustomerNeedsand
Solutions,11(1):3,2024.
[20] YanyingMao,QunLiu,andYuZhang. Sentimentanalysismethods,applications,andchallenges: Asystematic
literaturereview. JournalofKingSaudUniversity-ComputerandInformationSciences,page102048,2024.
[21] Jamin Rahman Jim, Md Apon Riaz Talukder, Partha Malakar, Md Mohsin Kabir, Kamruddin Nur, and Mo-
hammedFirozMridha. Recentadvancementsandchallengesofnlp-basedsentimentanalysis: Astate-of-the-art
review. NaturalLanguageProcessingJournal,page100059,2024.
[22] AminMahmoudi. Identifyingbiasedusersinonlinesocialnetworkstoenhancetheaccuracyofsentimentanalysis:
Auserbehavior-basedapproach. arXivpreprintarXiv:2105.05950,2021.
11

SentimentSimulationUsingGenerativeAIAgents
[23] JunjieLin,WenjiMao,andDanielDZeng. Personality-basedrefinementforsentimentclassificationinmicroblog.
Knowledge-BasedSystems,132:204–214,2017.
[24] JiyoungParkandSangEunWoo. Personalityassociationswithattitudestowardai. InTheImpactofArtificial
IntelligenceonSocieties: UnderstandingAttitudeFormationTowardsAI,pages57–70.Springer,2024.
[25] PujenShrestha,DarioKrpan,FatimaKoaik,RobinSchnider,DimaSayess,andMaySaadBinbaz. Beyondweird:
Cansyntheticsurveyparticipantssubstituteforhumansinglobalpolicyresearch? BehavioralScience&Policy,
page23794607241311793,2025.
[26] PriyavratChauhan,NonitaSharma,andGeetaSikka. Theemergenceofsocialmediadataandsentimentanalysis
inelectionprediction. JournalofAmbientIntelligenceandHumanizedComputing,12:2601–2627,2021.
[27] AsifKhan,HuapingZhang,NadaBoudjellal,ArshadAhmad,andMaqboolKhan. Improvingsentimentanalysis
inelection-basedconversationsontwitterwithelecbertlanguagemodel. Computers,Materials&Continua,76(3),
2023.
[28] Wolff-MichaelRothandAlfredoJornet. Situatedcognition. WileyInterdisciplinaryReviews: CognitiveScience,
4(5):463–478,2013.
[29] DavidMyers,JackieAbell,andFabioSani. EBook: SocialPsychology3e. McGrawHill,2020.
[30] JiweiLiandEduardHovy. Reflectionsonsentiment/opinionanalysis. Apracticalguidetosentimentanalysis,
pages41–59,2017.
[31] ChengxingXie,CanyuChen,FeiranJia,ZiyuYe,ShiyangLai,KaiShu,JindongGu,AdelBibi,ZiniuHu,David
Jurgens,etal. Canlargelanguagemodelagentssimulatehumantrustbehavior? InTheThirty-eighthAnnual
ConferenceonNeuralInformationProcessingSystems,2024.
[32] GatiVAher,RosaIArriaga,andAdamTaumanKalai. Usinglargelanguagemodelstosimulatemultiplehumans
andreplicatehumansubjectstudies. InInternationalConferenceonMachineLearning,pages337–371.PMLR,
2023.
[33] XiaoqingZhang,XiuyingChen,YuhanLiu,JianzhouWang,ZhenxingHu,andRuiYan. Llm-drivenagentsfor
influencerselectionindigitaladvertisingcampaigns. arXive-prints,pagesarXiv–2403,2024.
[34] CarolynQ.ZouAaronShawBenjaminMakoHillCarrieCaiMeredithRingelMorrisRobbWillerPercyLiang
Park,JoonSungandMichaelS.Bernstein. Generativeagentsimulationsof1,000people. arXivpreprint,page
arXiv:2411.10109,2024.
[35] XiuyingChenYaqiWangRuidiChangShichaoPeiNiteshV.ChawlaOlafWiestGuo,TaichengandXiangliang
Zhang. Largelanguagemodelbasedmulti-agents: Asurveyofprogressandchallenges. arXivpreprint,page
arXiv:2402.01680,2024.
[36] JoonSungPark,JosephO’Brien,CarrieJunCai,MeredithRingelMorris,PercyLiang,andMichaelSBernstein.
Generativeagents: Interactivesimulacraofhumanbehavior. InProceedingsofthe36thannualacmsymposium
onuserinterfacesoftwareandtechnology,pages1–22,2023.
[37] LeiWang,JingsenZhang,HaoYang,ZhiyuanChen,JiakaiTang,ZeyuZhang,XuChen,YankaiLin,Ruihua
Song,WayneXinZhao,etal. Userbehaviorsimulationwithlargelanguagemodelbasedagents. arXivpreprint
arXiv:2306.02552,2023.
[38] YileiWang,JiabaoZhao,DenizSOnes,LiangHe,andXinXu. Evaluatingtheabilityoflargelanguagemodelsto
emulatepersonality. Scientificreports,15(1):519,2025.
[39] AmericanPsychologicalAssociation. Personality. https://dictionary.apa.org/personality,n.d. APA
DictionaryofPsychology.
[40] Claudia Russo, Francesca Danioni, Ioana Zagrean, and Daniela Barni. Changing personal values through
value-manipulationtasks: asystematicliteraturereviewbasedonschwartzâC™stheoryofbasichumanvalues.
EuropeanJournalofInvestigationinHealth,PsychologyandEducation,12(7):692–715,2022.
[41] FrankTian-fangYe,BryantPHHui,JackyCKNg,BenCPLam,AlgaeKYAu,WesleyCHWu,HilaryKY
Ng, and Sylvia Xiaohua Chen. Social axioms and psychological toll: A study of emotional, behavioral, and
cognitiveresponsesacross35culturesduringthecovid-19pandemic. AppliedPsychology:HealthandWell-Being,
16(4):1679–1698,2024.
[42] PulseAsiaResearchInc. Ulatngbayan: June2024nationwidesurveyonnationalconcernspriortothesona.
Researchreport,PulseAsiaResearchInc.,July2024. Accessed: 2025-04-16.
[43] ATimothyChurch,JoseAlbertoSReyes,MarciaSKatigbak,andStephanieDGrimm. Filipinopersonality
structureandthebigfivemodel: Alexicalapproach. JournalofPersonality,65(3):477–528,1997.
12

SentimentSimulationUsingGenerativeAIAgents
[44] GregorioEHDelPilar. Thedevelopmentofthemasaklawnapanukatngloob(mapangloob). PhilippineJournal
OfPsychology,50(1):103–141,2017.
[45] MaryRachelleRWapaño. Personalitydisordersandthefive-factormodelamongfilipinonon-clinicalsample.
InternationalJournalofResearchandInnovationinSocialScience(IJRISS),V,2021.
[46] MelroseTia,JeromeEspina,andJasonAlbia. Measuringpoliticalbiasandframingeffectsinlargelanguage
models(llms): Asensitivityanalysis. Manuscriptinpreparation,2025.
[47] AaronGrattafiori,AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,AbhishekKadian,AhmadAl-Dahle,
AieshaLetman,AkhilMathur,AlanSchelten,AlexVaughan,etal. Thellama3herdofmodels. arXivpreprint
arXiv:2407.21783,2024.
[48] Kenneth O McGraw and Seok P Wong. A common language effect size statistic. Psychological bulletin,
111(2):361,1992.
[49] SunwoongKim,JonghoJeong,JinSooHan,andDonghyukShin. Llm-mirror: Agenerated-personaapproachfor
surveypre-testing. arXive-prints,pagesarXiv–2412,2024.
[50] LeoYeykelis,KaavyaPichai,JamesJCummings,andByronReeves. Usinglargelanguagemodelstocreateai
personasforreplicationandpredictionofmediaeffects: Anempiricaltestof133publishedexperimentalresearch
findings. arXivpreprintarXiv:2408.16073,2024.
[51] ArminFalkandJamesJHeckman. Labexperimentsareamajorsourceofknowledgeinthesocialsciences.
science,326(5952):535–538,2009.
[52] DavidLazer,DevonBrewer,NicholasChristakis,JamesFowler,andGaryKing. Lifeinthenetwork: thecoming
ageofcomputationalsocialscience. Science,323(5915):721–723,2009.
[53] DanielKahnemanandAmosTversky. Choices,values,andframes. Americanpsychologist,39(4):341,1984.
[54] DennisChongandJamesNDruckman. Framingtheory. Annu.Rev.Polit.Sci.,10(1):103–126,2007.
[55] PaulMSnidermanandSeanMTheriault. Thestructureofpoliticalargumentandthelogicofissueframing.
Studiesinpublicopinion: Attitudes,nonattitudes,measurementerror,andchange,3(03):133–65,2004.
[56] RobertRMcCraeandPaulTCostaJr. Personalitytraitstructureasahumanuniversal. Americanpsychologist,
52(5):509,1997.
[57] CommissiononElections(COMELEC). 2022registeredvotersandvoterswithaccessiblepollingplaces(final).
https://comelec.gov.ph/?r=2022NLE/Statistics/2022RVVAVmcocfinal, 2022. Accessed: 2024-10-
01.
13

SentimentSimulationUsingGenerativeAIAgents
SupplementaryMaterial
A.SurveyDesignandImplementationDetails
A.1 SurveyDesignandInstrumentSpecifics
Specificpsychologicalframeworksincludepersonalitytraits(e.g.,HEXACOpersonality),values(e.g.,BasicPersonal
Values), attitudinal frameworks (e.g., Affective Intelligence Theory), and beliefs (e.g., Social Axioms). It also
encompasses social and political behavior (e.g., Civic Engagement). In addition to the sociodemographics and
psychologicalframeworks,thesurveyinstrumentalsoincludesanadditionalsectiontoassessgeneralcitizenattitudes
toward four major economic issues (e.g., inflation, minimum wage, etc) and four key social issues (e.g., the West
PhilippineSeadispute,corruption,etc).
A.2 SurveySampling
A multi-stage stratified random sampling design was used to obtain a nationally representative sample of 2,485
Filipinoadults[57]. Thesamplewasproportionallydistributedacrossthe17administrativeregionsusingprobability
proportionaltosize. Systematicintervalsamplingselectedfive(5)householdspersampledbarangay, andone(1)
respondentperhouseholdwasrandomlychosenusinggender-rotatedprobabilitytoensurebalancedmaleandfemale
representation. Thissamplingdesignaccountedforclusteringatmultiplegeographiclevelsandstratificationbyregion
andurbanicity. Datawerecollectedthroughface-to-faceinterviewsfromNovember22toDecember9,2024. Ahybrid
systemofdigitaltabletsandprintedformswasusedinthefieldtoensurebothflexibilityandhighdatafidelity.
A.3 WeightingProcedure
Tocorrectforunequalselectionprobabilitiesinherentinthesamplingdesign, designweights(baseweights)were
computedfromthejointprobabilitiesofselectionateachsamplingstage: cities/municipalities,barangays,households,
andeligiblerespondents. Thesebaseweightswerethenadjustedusingpost-stratificationtechniques, anchoredon
the official registered voter count data [57] by region and gender. This procedure ensured that the final weighted
samplereflectedtheactualdistributionofregisteredvoters,therebyimprovingthegeneralizabilityandprecisionof
population-levelinferencesandestimates.
A.4 SurveyImplementation
Randomizationtechniqueswereappliedtominimizeselectionbias,andintervalsamplingwasemployedtoensure
systematiccoverageofbothurbanandruralareas. Theuseofin-personinterviewsallowedforgreaterengagementand
clarificationofquestionswhennecessary,contributingtohigherresponsequalityandcompleteness.
B.AgentEmbodimentSetup
Figures5and6presentthepromptformatsusedintheagentembodimentsectionofthesentimentsimulation. Both
formats operationalize the presentation of sociodemographic and psychographic attributes to the language model,
servingasthefoundationforgeneratingagent-specificresponses. Thecategoricalformat(Figure5)conveystraitsand
attributesthroughcompact,labeledvariables(e.g.,Extraversion: HIGH),whilethecontextualizedformat(Figure6)
embedsthesameinformationwithinbriefnarrativedescriptions,enrichingeachvariablewithinterpretivecontext.
Inbothcases,bracketedfields(e.g.,<age>,<incomerange>)representplaceholdersdynamicallypopulatedwith
realsurveydataduringpromptinstantiation. Textsegmentsrenderedinboldcorrespondtofixedpromptcomponents
thatremainconsistentacrossallagents.
C.AgentExposuretoScenario
Figure 7 presents the prompt structure used to expose an embodied agent to a situational stimulus and elicit a
correspondingaffectivejudgmentorsentimentresponse. Inthisformat,thelanguagemodelispromptedtoimagine
beingpresentedwithaparticularevent,scenario,orstatement,andtoreflectonhowitwouldpersonallyresonatebased
ontheagent’sencodedbackgroundandperspective.
The<scenario>placeholderisdynamicallyfilledwiththetargetstimulus,whileallboldedtextconstitutesfixed
instructionallanguageconsistentacrossallprompts. Themodelisthenaskedtoidentifythesentimentthatbestreflects
howsomeonewithitsassignedprofilewouldmostlikelyfeelinresponse.
14

SentimentSimulationUsingGenerativeAIAgents
Figure5: PromptFormatforCategoricalProfileEncoding.
Figure6: PromptFormatforContextualizedProfileEncoding.
15

SentimentSimulationUsingGenerativeAIAgents
Figure7: PromptFormatforInstantiatingAgentExposuretoScenario.
D.AgentResponsetoScenario
Figure 8 presents the full instruction sequence used to elicit a sentiment judgment, accompanying rationale, and
self-assessedalignmentfromanembodiedagentprofile. Afterbeingexposedtoascenario,theagentisinstructedto
identifythesentimentthatmostaccuratelyreflectshowapersonwiththatprofilewouldlikelyrespond.
Inadditiontoselectingasentimentfromastandardized5-pointscale(NegativetoPositive),themodelispromptedto
articulateabriefexplanationforitsjudgment. The<reason>placeholderdenotesthepositionwherethemodelis
expectedtogeneratethisresponse. Followingthis,themodelisaskedtocriticallyevaluatewhetheritschosensentiment
logicallyalignswiththeprofile’sdescribedcharacteristics,includingvalues,personaltraits,andcontextualbackground,
andtoanswerwithabinaryYesorNo. Thispromptformatsupportsdeeperanalysisofthemodel’sinternalcoherence,
linkingsentimentexpressiontoreasoningandvaluealignmentwithinanembodiedsimulationcontext. Similarly,all
boldedsegmentsrepresentfixedinstructionaltextpresenteduniformlyacrossprompts.
Figure8: PromptFormatforGeneratingAgent’sResponsetoScenario.
E.QuadraticWeightedAccuracy(QWA)asEvaluationMetric
Figures9and10presentheatmapsofpairwiseQWAscores,capturingthedegreeofalignmentbetweenagent-generated
responsesandhumanresponsesacrosstwocoretasks: agentembodimentandsentimentsimulation. Inbothfigures,
eachmatrixcellrepresentstheaverageagreementscoreforaspecificpairofsimulatedandsurveyresponsevalues.
16

SentimentSimulationUsingGenerativeAIAgents
E.1 OnAgentEmbodimentSurveyReplicationTask
Figure9presentstheQWAmatrixforthesurveyreplicationtask,wherethemodelwaspromptedtogenerateLikert-scale
responsestopsychographicsurveyitemsfromtheperspectiveofanembodiedagentprofile. Thematrixshowspairwise
QWAscoresbetweeneachsimulatedagentresponse(rows)andthecorrespondinghumanresponse(columns)ona
7-pointordinalscale.
Figure9: QWAMatrixofSimulatedandHumanResponsesintheAgentEmbodimentTask.
E.2 OnSentimentSimulationTask
Similarly,Figure10showstheQWAmatrixforthesentimentsimulationtask. Here,simulatedsentimentresponsesare
comparedtohumansentimentratingsona5-pointordinalscalerangingfromNegativetoPositive.
Figure10: QWAMatrixofSimulatedandHumanSentimentResponsesintheSentimentSimulationTask.
17

SentimentSimulationUsingGenerativeAIAgents
F.StatisticalTests
Pairedt-testwasusedwhentheassumptionofnormalitywassatisfied. Theformulaisgivenbelow:
d
| t= √  |     | (2) |
| ----- | --- | --- |
| s d / | n   |     |
where:
disthemeanofthedifferencesbetweenpairedobservations;
s isthestandarddeviationofthedifferences;and
d
nisthenumberofpairs.
Forgroupcomparisonsinwhichthenormalityassumptionwasnotmet,weusedtheWilcoxonsigned-ranktest,see
Equation3.
| W =min(W+,W−) |     | (3) |
| ------------- | --- | --- |
where:
W+isthesumofpositiveranks;
W−isthesumofnegativeranks;and
misitssamplesize
Accordingly,theZ-scoreformulaisgivenbelow:
W −µ
W
| Z = |     | (4) |
| --- | --- | --- |
σ
W
where:
(cid:114)
n(n+1) n(n+1)(2n+1)
| µ W = and σ W | =   |     |
| ------------- | --- | --- |
| 4             | 24  |     |
nisthesamplesizeofthegroups.
Inadditiontohypothesistesting,wecomputedCohen’s|d|toquantifytheeffectsizeandassessthepracticalrelevance
ofobserveddifferences. Cohen’s|d|iscalculatedas:
| (cid:12)               | (cid:12)  |     |
| ---------------------- | --------- | --- |
| (cid:12) µ −µ          | (cid:12)  |     |
| (cid:12) 1             | 2(cid:12) |     |
| |d|= (cid:12)(cid:113) | (cid:12)  | (5) |
(cid:12) s2+s2(cid:12)
| (cid:12) 1 | 2(cid:12) |     |
| ---------- | --------- | --- |
2
where:
µ andµ arethemeansofeachgroup;and
1 2
s2ands2arethestandarddeviationsofeachgroup.
1 2
18