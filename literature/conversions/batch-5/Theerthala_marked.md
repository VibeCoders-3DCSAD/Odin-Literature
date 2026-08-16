---
conversion_metadata:
  converted_at: "2026-07-21T08:58:58Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Theerthala.pdf"
  source_pdf_sha256: "f88c256ed66b2e72fa46c7a6faccfb2039048f041fb7caf766f78e1f15c63117"
  page_count: 24
  markdown_char_count: 229726
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Synthesizing Behaviorally-Grounded Reasoning Chains: A
Data-Generation Framework for Personal Finance LLMs

Akhil Theerthala
Perfios Software Solutions

Abstract

Personalized financial advice requires consid-
eration of user goals, constraints, risk toler-
ance, and jurisdiction. Prior LLM work has
focused on support systems for investors and fi-
nancial planners. Simultaneously, numerous re-
cent studies examine broader personal finance
tasks, including budgeting, debt management,
retirement, and estate planning, through agen-
tic pipelines that incur high maintenance costs,
yielding less than 25% of their expected finan-
cial returns. In this study, we introduce a novel
and reproducible framework that integrates rel-
evant financial context with behavioral finance
studies to construct supervision data for end-to-
end advisors. Using this framework, we create
a 19k sample reasoning dataset and conduct a
comprehensive fine-tuning of the Qwen-3-8B
model on the dataset. Through a held-out test
split and a blind LLM-jury study, we demon-
strate that through careful data curation and
behavioral integration, our 8B model achieves
performance comparable to significantly larger
baselines (14-32B parameters) across factual
accuracy, fluency, and personalization metrics
while incurring 80% lower costs than the larger
counterparts.
Keywords: Financial Datasets; Personal Fi-
nance; Reasoning Models; Large Language
Models

1 Introduction

Legal counseling, healthcare, and finance are
among the numerous high-stakes domains in which
personalized advice is essential. However, the de-
velopment of this personalized advice is fraught
with obstacles, requiring substantial investments
and years of human expertise. Recent research ef-
forts have thoroughly investigated automated deci-
sion support systems in various areas, emphasizing
their cost-effectiveness. In the financial sector, a
variety of support systems have been investigated,
with a particular emphasis on asset recommenda-
tions and investment predictions. (Sanz-Cruzado

et al., 2024; Luo et al., 2025; Takayanagi et al.,
2023)

Recent advances in large language models
(LLMs) have shown effective performance in act-
ing as decision support systems for investors
(Gupta, 2023) and financial planners (Huang et al.,
2024). The core advantage of natural language gen-
eration presents these automated support systems
with a unique advantage that was never available
in previous applications. This advantage has re-
peatedly shown its power in linguistic tasks such
as streamlining complex financial narratives from
extensive documents, corporate discourses, news
sources, and social media.(Gueta et al., 2025; Lee
and Lay-Ki, 2024) The utility of these models is
also being explored in Time series (Liu and Jia,
2025) and Financial reasoning applications (Liu
et al., 2025).

Notwithstanding this capability, recent research
indicates that no model excels across all financial
task categories, which include text summarization,
sentiment analysis, causal analysis, forecasting,
It
and text classification (Matlin et al., 2025).
has been demonstrated that attaining robust per-
formance frequently necessitates the utilization of
large, expensive models, thereby constraining the
practicality of these solutions. Due to these in-
herent limitations and the complexity of financial
advisory, many studies focusing on broader finan-
cial decision systems have preferred an agentic
approach over training financial domain-specific
language models. (Okpala et al., 2025; Joshi, 2025;
Takayanagi et al., 2025a)

Although the initial agentic frameworks focused
on answering simple inquiries,(Lakkaraju et al.,
2023) recent studies have accelerated the devel-
opment of these systems to provide practical and
actionable advice to the end user (Takayanagi et al.,
2025b; Okpala et al., 2025). These agents can now
dynamically interact with users and can assist in
various tasks such as recommendation, question an-

Proceedings of The 10th Workshop on Financial Technology and Natural Language. EMNLP-2025, Suzhou, China

---

<!-- PAGE 2 -->

swering, search, and customer profiling. (Li et al.,
2024; Takayanagi et al., 2025a; Han et al., 2024)

Although agentic systems demonstrate potential
in providing tailored financial advice, their efficacy
is hindered by considerable constraints, including
the integration with legacy systems, compliance
with data security regulations, and high inference
(Cemri et al., 2025; Wang et al., 2025).
costs.
In support of these concerns, a recent study by
(Meimandi et al., 2025) illustrates that a confluence
of technical and cost-related factors hinders these
applications from realizing even 25% of their an-
ticipated returns. This research also establishes an
important differentiation: success in benchmarks
does not necessarily equate to success in deploy-
ment. In practical terms, these proactive financial
advisors frequently encounter a swift deterioration
in performance within a matter of months following
their implementation, attributable to the inherent
volatility of real-world conditions. Concurrently,
studies show that the extent of personalization is
often limited by the volume of context and informa-
tion that can be supplied to an agent, impacting the
overall performance. (Zhou et al., 2025; Winder
et al., 2024)

One of the direct ways to address these limita-
tions is to tune a model with a domain-specific
context that integrates financial, behavioral, and
psychological information. This work aims to close
this gap by providing a reproducible framework to
generate financial advice through a well-structured
chain-of-thought.
In particular, the framework
constructs supervision data to train models to (a)
provide personalized guidance for users’ financial
dilemmas, (b) reliably apply core financial knowl-
edge, and (c) recognize and mitigate user-side be-
havioral biases by integrating behavioral and his-
torical evidence.

To address these limitations, we propose a
novel, data-centric framework for synthesising
behaviorally-grounded reasoning chains. Rather
than relying on complex agentic architectures, our
approach directly bakes financial, behavioural, and
psychological knowledge into the training data it-
self. Crucially, we treat the inference of the user’s
psychological state not as an afterthought, but as
a standalone, foundational phase in the reasoning
chain. This design choice is directly motivated by
recent findings that users’ trust and engagement
are heavily influenced by the persona of the ad-
visor (Takayanagi et al., 2025a), not just the raw
accuracy of its advice. By isolating and explic-

itly modelling this psychological dimension, our
framework ensures that personalisation and empa-
thetic framing are intrinsic to the model’s reasoning
process, leading to more effective and trustworthy
financial guidance.

It should also be considered that although re-
cent agentic frameworks respond based on real-
time knowledge; most of these knowledge sources
need to be manually curated (Aggarwal and Singh,
2024).
In addition to this, we should note that
most of the recommendations needed for general
financial advice do not require real-time financial
knowledge. Instead, this advice needs an agent
that can inherently retrieve the relevant informa-
tion from its memory. We address this problem
by carefully crafting a chain-of-thought section to
retrieve the financial context relevant to the query.
Recent studies have shown that inherent biases
often limit users’ ability to make many wealth-
making financial decisions. (Baker et al., 2017;
Agrawal, 2012) These biases are highly variable
and often depend on the age, experience and lo-
cation of the user. Many financial agents do not
directly address these biases when providing finan-
cial advice to the user. In this study, we have tried
to integrate these biases into the reasoning model’s
natural chain-of-thought to tune the final responses
towards acknowledging and addressing these bi-
ases.

Each stage of chain-of-thought generation is ver-
ified by a set of Large Language Model juries that
rank various generations and pick the best version
suitable for the user queries. We used this frame-
work to generate a 19k sample dataset, which is
used to finetune a Qwen-3-8B model. This model
is then compared to models of similar sizes to de-
termine the impact of this framework.

This paper introduces a principled, data-centric
framework as a step toward smaller, more trust-
worthy personal finance LLMs, and we outline its
use as a backbone policy within agentic workflows
to thin planning chains and lower orchestration
cost—an evaluation we defer to future work.

2 Related Works

The application of automated systems to finan-
cial advice is not a new undertaking. Prior to the
widespread adoption of large language models, re-
search focused on applying classic techniques such
as collaborative filtering and case-based reasoning
to well-defined domains such as loan and insurance

---

<!-- PAGE 3 -->

policy recommendation, as surveyed by Zibriczky
(2016). However, the advent of powerful LLMs
has opened new frontiers and presented a distinct
set of challenges and approaches.

Much of the recent literature has focused on
benchmarking the capabilities of general-purpose
LLMs on a range of isolated financial tasks. For in-
stance, a comprehensive study by Hean et al. (2025)
evaluated leading models such as ChatGPT and
Claude against standardized financial literacy ques-
tionnaires covering diverse topics from mortgages
to taxes. While their findings show that newer
models are consistently improving and can achieve
high accuracy on specific topics, they also reveal
significant limitations, concluding that LLMs still
struggle to provide accurate responses for com-
plex financial queries. This highlights a critical
performance gap: off-the-shelf models are often
insufficient for the nuanced demands of holistic
financial advice.

To overcome the limitations of single models
and address more complex, multi-step planning,
a significant body of research has shifted towards
developing sophisticated agentic workflows. A re-
cent survey by Ding et al. (2024) provides a com-
prehensive overview of this landscape, categoriz-
ing these systems into distinct architectural pat-
terns such as reflection-driven and debate-driven
agents. A clear example is the work of Okpala et al.
(2025), who designed "agentic crews" composed
of multiple specialized LLM agents, such as data
scientists and compliance checkers, to automate
the entire financial modelling and risk manage-
ment pipeline. While powerful, such multi-agent
systems demonstrate significant architectural com-
plexity and high maintenance costs. Furthermore,
research into these conversational agents has re-
vealed significant risks; Takayanagi et al. (2025a)
found in a user study that participants often placed
more trust in a confident, "extroverted" agent even
when it provided lower-quality advice, highlighting
the potential for these complex systems to mislead
inexpert users.

We argue, however, that the primary bottleneck
is not architectural complexity, but the inherent
irrationality of the models themselves, necessitat-
ing a data-centric approach. This need is rooted
in the tendency of LLMs to amplify human cog-
nitive biases. The groundbreaking work of Zhou
et al. (2025) introduced a comprehensive frame-
work based on behavioral finance to demonstrate
that LLMs exhibit significant financial biases, such

as anchoring and overconfidence. Their crucial
finding that fine-tuning on financial data can some-
times exacerbate these irrational tendencies under-
scores the profound risks of using uncurated data.
This is supported by empirical studies exposing a
significant "product bias" in leading LLMs (Zhi
et al., 2025) and by findings that LLM-generated
advice systematically increases portfolio risk by
reinforcing investment biases such as geographi-
cal concentration and trend chasing (Winder et al.,
2024). Taken together, these findings reveal that a
model’s pre-trained knowledge is an unreliable and
potentially risky foundation for financial advice.

Therefore, our work addresses a critical gap.
While large-scale financial language models like
FinGPT, which continuously ingest real-time mar-
ket data to update and adapt the underlying model
(Yang et al., 2023; Wang et al., 2023; Zhang et al.,
2023; Liu et al., 2023), have been proposed, our
approach differs fundamentally in its core contribu-
tion. Whereas such work focuses on scaling model
capacity and live data ingestion, our work intro-
duces a novel and reproducible methodology for
creating the supervision data itself. By integrat-
ing the relevant financial context with behavioral
finance studies, we construct a high-quality reason-
ing dataset designed to train smaller, more efficient
end-to-end advisors that are grounded in sound,
unbiased principles from their inception.

3 Dataset construction

3.1 Data Collection and Processing

Our first step was to collect a large pool of real-
world finance questions. Reddit (Reddit, [2025])
proved ideal as a source of complex scenarios
that span the breadth of personal finance do-
mains—from debt consolidation and retirement
planning to tax optimization and insurance deci-
sions. The platform’s subreddits, particularly r/per-
sonalfinance, which receives hundreds of thousands
to millions of user queries, contain authentic scenar-
ios that capture the intricate, multi-faceted nature of
real financial decision-making, providing the sce-
nario diversity essential for training comprehensive
advisory models.

To comply with Reddit’s terms and conditions,
we exclusively utilized publicly available archived
data from posts prior to June 2023, ensuring all col-
lected queries were ethically sourced and properly
de-identified.

After ingestion, we filtered the raw corpus in two

---

<!-- PAGE 4 -->

Table 1: A detailed breakdown of the dataset generated via our proposed framework. This table presents the
distribution of approximately 19k samples across eight distinct categories of personal finance. Each category
includes key metrics, such as the average token count for the initial query, the generated chain-of-thought
delineating the reasoning steps, and the final answer.

Category

Description

Debt Management & Credit

Retirement Planning

Tax Planning & Optimization

Investing & Wealth Building

Strategies for debt reduction (e.g. snow-
ball, avalanche), credit-score improve-
ment, and loan analysis.
Strategies, income-needs analysis, bene-
fits optimization (e.g. 401(k), pensions)
and withdrawal strategies.
Tax-minimization strategies,
under-
standing deductions and credits, and
investment-tax implications.
Investment strategies based on risk tol-
erance, diversification, asset allocation,
and long-term growth.

Budgeting & Cash-Flow Management Creating budgets,

Insurance & Risk Management

Savings & Emergency Funds

Estate Planning & Legacy

tracking expenses,
managing income streams, and improv-
ing cash flow.
Assessing insurance needs (life, health,
property), understanding policies, and
managing financial risks.
Strategies for building savings, establish-
ing emergency funds, and goal-based
saving.
Wills, trusts, inheritance considerations,
and minimising estate taxes (accounting
for regional variations).

Count

5175

Avg.
Query
Tokens
215.76

Avg.
CoT
Tokens
628.30

Avg.
Response
Tokens

393.69

3286

198.10

648.28

407.02

3019

182.96

630.20

397.81

2994

200.16

653.54

402.98

2503

221.53

628.71

394.47

1035

213.86

621.53

389.65

638

177.18

652.25

382.95

196

216.90

653.47

409.06

stages:

• Topical validity – retained posts that con-
tained an explicit, answerable personal fi-
nance question (e.g., budgeting, credit, re-
tirement), discarding generic news, advertise-
ments, or off-topic commentary.

• Contextual clustering – grouped seman-
tically similar posts and removed near-
duplicates to reduce noise.

This pipeline yielded 405k unique questions. We
sampled 19k representative queries that span eight
thematic categories. Table 1 contains the detailed
description of the final dataset generated using the
framework. The entire 405k-item corpus remains
available for future scaling. Details about prompt
templates and specific instructions used in each
phase of the generation framework are presented in
Appendix A.1.

3.2 Generation methodology

On a high level, the dataset generation framework
can be divided into two parts: (i) chain-of-thought
generation and (ii) response generation.

Our chain-of-thought generation is divided into
four major phases, as illustrated in Fig. 1. This

modular approach helps us focus on developing
an independent rubric for each phase while giving
the ability to stitch them together as a coherent
chain-of-thought.

3.2.1 Query Analysis
The issue with natural language inquiries is the po-
tential inconsistency of the information supplied to
the model. There may be significant redundancy,
or essential information may be hidden at times.
Thus, the initial stage of answer creation, the ques-
tion analysis phase, serves as a fundamental step in
which the user’s question is deconstructed into its
essential components. This is required to ascertain
the (i) primary conflict from the user’s input; (ii)
the principal players in the dilemma; and (iii) the
essential financial facts to address the inquiry. This
facilitates the optimization of subsequent cognitive
processes while remaining aligned with the user’s
inquiry.

3.2.2 Context Analysis
Context analysis (Modular RAG). After intent
parsing, we assemble a compact evidence pack via
a modular RAG framework (Gao et al., 2024) built
on two self-curated corpora snapshotted through
February 2025: (i) a financial corpus of ∼600k

---

<!-- PAGE 5 -->

Figure 1: Dataset generation pipeline. Four modular chain-of-thought phases feed into final response generation.
Each phase includes LLM-jury validation (not shown) to ensure quality.

tokens—practical sources such as Investopedia
and a Bogleheads snapshot (Investopedia, 2025;
Bogleheads, 2025) covering core concepts (e.g.,
retirement accounts, debt-repayment strategies),
plus curated summaries of policy changes for ma-
jor U.S. credit-card products and other consumer-
policy/market updates; and (ii) a behavioral cor-
pus of ∼300k tokens—research and practitioner
write-ups spanning psychology of risk, investor
behavior, behavioral portfolio theory, behavioral
asset pricing, psychological effects of debt, and
generational differences.

are

chunks

Candidate

retrieved with
text-embeddings-3-large (OpenAI, 2025b)
re-ranked with all-MiniLM-L12-v2
(top-25),
(Sentence-Transformers, 2021), and the top-15
are condensed by gemini-2.0-flash (Google, 2025;
Team et al., 2025a) to remove residual noise and
unify terminology. The streamlined context and
the user query then feed the downstream reasoning
stage. Further details are provided in Appendix B.

3.2.3 Psychological Cue identification

In parallel to context identification, a psychological
cue identification module is run to identify cues
from the text. We extract the overall sentiment of
the text, the primary emotions identifiable from
the choice of words in the query, and the level of
certainty present in the information. Using these
cues, we try to generalize a set of communicative
intents that might be behind the user’s query. By
breaking down the assessment into four distinct
categories, the process ensures a comprehensive

evaluation of the user’s intent. This intent is utilized
to direct the final response into a tone that is most
suitable for the user, rather than directly providing
them a monotonous response.

To operate the cue-identification at scale, and in
line with the prior studies which demonstrate that
state-of-the-art large language models outperform
human annotators in judgment tasks(Boji´c et al.,
2025; O’Leary, 2025), we adopt an LLM-based
framework for cue identification similar to the other
stages in the framework.

3.2.4 Response Formulation

The final phase of the chain-of-thought is a distinct
response formulation phase, in which we synthe-
size a set of instructions, consolidating information
from all preceding phases. This produces a set of
directives that must be adhered to throughout the
response-generation phase.

3.3 Response generation

A conclusive response is formulated to address the
user’s inquiry, utilizing the previously optimized
stages of information. This concluding comment
is based on the financial context presented and is
articulated in a suitable tone for the user.

3.4 Data Validation

Given that various open and proprietary LLMs au-
tomate numerous generations, there is a clear ne-
cessity to assess and authenticate their outputs. We
employed a series of juries, specifically gemini-2.0-
flash and o4-mini (OpenAI, 2025a), to evaluate and

---

<!-- PAGE 6 -->

rank various generations for each phase. Each juror
assessed the created information within a three-
shot evaluation framework, ultimately selecting the
highest-ranked response for subsequent generation
jobs.

4 Evaluation

To test whether our dataset enables practical deci-
sion support, we fine-tune Qwen-3-8B (Yang et al.,
2025) for five epochs and compare it with baselines
of similar size.

We perform an additional assessment of the per-
formance using two separate held-out datasets. We
employ these methods to assess the quality of the
responses through both quantitative and qualitative
measures.

4.1 Quantitative Evaluation

To assess the quantitative performance of the mod-
els, we utilize a held-out dataset comprising 500
distinct queries across various categories of per-
sonal finance. Ground truths were produced by the
generation framework presented in Section 3.2 (not
the fine-tuned model) prior to training and validated
by independent jurors. Following the ground-truth
generation, we calculate the BERTScore (Zhang
et al., 2020) using the Qwen-3-8B-embeddings
(Zhang et al., 2025) model to assess the seman-
tic accuracy of the responses. We also calculate
the BLEURT (Sellam et al., 2020) score to assess
the fluency (or) human-likeness of the responses,
respectively. The quantitative scores of various
models utilized in this evaluation are detailed in
Table 2.

Our 8B model achieves semantic accuracy com-
parable to leading baselines, including Gemma3-
27B/12B and Mistral-24B. In particular, our model
surpasses these larger models by approximately
3–5% in human-likeness and fluency. This indi-
cates a reduced deviation from ground-truth data
and enhanced fluency signals compared to models
twice its size.

4.2 Qualitative Evaluation

To complement reference-based metrics and, criti-
cally, to assess the model’s generalization capabili-
ties, we run a list-wise blind LLM-jury ranking on
504 queries that were entirely held out and unseen
during the training phase. These test queries were
collected from a subsequent time period to ensure
no data contamination. Meanwhile, all the candi-
dates were zero-shot generated in their respective

Model

BERTScore ↑ BLEURT

Gemma3-27B-IT
(Team et al., 2025b)
Gemma3-12B-IT
Mistral-24B-2501
(MistralAI, 2025b)
QWQ-32B (Qwen, 2025)
(reasoning)

0.7142

0.4374

0.7139

0.4390

0.7133

0.4464

0.7069

0.4452

DeepSeek-Qwen-14B
(reasoning)
(DeepSeekAI, 2025)
Ours (8 B)
Llama-3 8B (Meta,
2024)
Mistral-7B v0.3
(MistralAI, 2025a)

0.7069
0.7000
0.6881

0.4513
0.4600
0.4547

0.6650

0.4501

Table 2: Automatic evaluation on the 500-query test set.
Bold marks the best score in each column; higher is
better.

default inference settings to get their best perfor-
mance. This setup allows us to evaluate whether
our fine-tuned model has merely learned to mimic
the training data or if it has successfully internal-
ized a generalizable framework for the response
generation that can be applied to novel user prob-
lems.

To mitigate familial bias and leakage, we ex-
cluded judges from model families used anywhere
in our pipeline. In particular, Gemini models were
omitted because they were used during dataset gen-
eration/validation, and Qwen-family judges were
omitted because the system under test is Qwen-8B.
A few otherwise suitable judges were also excluded
for cost reasons. The final judge pool comprises
models from unrelated families; none overlapped
with training or data-creation components.

For each query, every judge sees all k
anonymized candidates simultaneously (no ground
truth and no model identities) and returns a full
ranking; candidate order is uniformly randomized
per replicate. We use two main judges, namely
DeepSeek-V3-0324 (DeepSeek-AI et al., 2025) and
Kimi-k2 (AI, 2025). Kimi-k2 is run three times,
and DeepSeek-v3-0324 is run five times on inde-
pendently shuffled anonymized candidate orders
for each query to reduce possible biases. These
judges were chosen in order to avoid same-family
bias prevalent in modern LLM-judge studies.

---

<!-- PAGE 7 -->

Table 3: Rank correlations between judge sets (higher is
better). τ measures how often the judges agree with A >
B, and ρ measures how closely the full rank lists track.

Metric

Kendall’s τ

Spearman’s ρ

Plausibility
Accuracy
Relevance

Overall

0.6183
0.6183
0.6910

0.6429

0.7711
0.7635
0.8264

0.7904

are

The

rankings

converted

to Borda
points(Saari, 2023) and averaged across judges
and replicates to obtain the representative score
of a response. We receive the ranking judgments
according to three criteria, namely their financial
accuracy, plausibility, and relevance to the query,
and report the aggregate Borda scores in Fig.2.
Whereas Appendix C.1 presents the in-depth
analysis of the evaluation results.

To examine rank consistency between the judge
sets, we compute Kendall’s τ and Spearman’s ρ
over per-query model ranks. Kendall’s τ assesses
pairwise order agreement (do both judges prioritize
model A above model B?). Spearman’s ρ assesses
how closely the complete ranked lists move to-
gether and penalizes significant rank differences.
We observe τ ≈ 0.62-0.69 and ρ ≈ 0.76-0.83
(overall τ = 0.64, ρ = 0.79), indicating substantial
agreement. The consistently higher ρ than τ sug-
gests disagreements are mostly local swaps rather
than wholesale reorderings. Relevance demon-
strates the strongest alignment (τ = 0.691, ρ =
0.826). Table 3 shows τ and ρ for each metric and
overall.

Our experimental results demonstrate that a well-
curated, behavior-tuned finance dataset can elevate
an 8B open model to achieve performance parity
with models two to three times its size, thus validat-
ing the practical utility of our framework. Details
about the entire training environment and settings
are presented in Appendix D.

4.3 Qualitative Analysis and Error Patterns

Analysis of the 504 held-out responses reveals con-
sistent patterns across the three evaluation dimen-
sions. When models produce inaccurate responses,
they typically also exhibit degraded reasoning qual-
ity—accuracy and plausibility failures often co-
occur. However, relevance remains relatively inde-
pendent; responses can stay on-topic and address

Figure 2: LLM-jury evaluation on 504 unseen subreddit
queries: stacked bars show Borda-average scores for
accuracy (blue), plausibility (orange), and relevance
(green); taller bars indicate stronger overall preference.
Our 8 B system (fourth from left) outperforms all other
sub-14 B models and approaches the 27 B–32 B
leaders. The y-axis represents the average Borda points
a model has received.

user constraints even when containing factual er-
rors or poor reasoning.

Strengths. The model consistently produces
well-structured responses with clear headers, se-
quential action steps, and appropriate empathetic
framing. It reliably extracts user-specific details
(monetary amounts, timelines, constraints) and in-
corporates them into tailored advice. Responses
typically acknowledge emotional context before
providing practical guidance—a pattern that en-
hances perceived helpfulness.

Failure Modes. The primary weakness is factual
hallucination, particularly for jurisdiction-specific
regulations and tax details. The model occasion-
ally generates plausible-sounding but incorrect
specifics (e.g., non-existent grant programs, out-
dated tax brackets). These errors are most frequent
in regulation-heavy domains (taxes, insurance) and
least common in general planning tasks (budgeting,
debt management).

Implications. While the model maintains strong
structural and empathetic qualities across all re-
sponses, factual grounding remains the key bottle-
neck. This suggests that adding targeted retrieval
for regulatory information and calculation verifica-
tion would yield the highest marginal improvement.
Even with current limitations, the model’s consis-
tent task alignment and user-responsive framing
provide practical utility for non-critical advisory
scenarios.

---

<!-- PAGE 8 -->

4.4 Cost Analysis

Beyond performance metrics, practical deploy-
ment requires careful cost consideration. Table
4 presents a comprehensive cost analysis of the
model produced by our framework against several
baselines, comparing hosting infrastructure, infer-
ence latency, and total operational expenses.

Our data-centric approach delivers exceptional
cost efficiency in the personal finance domain. By
enabling a compact 8B model to achieve perfor-
mance competitive with much larger systems, our
method facilitates at least an 80% reduction in op-
erational costs when compared to baselines with
over 12B parameters. This dramatic cost reduc-
tion stems from targeted behavioral integration and
principled data construction, rather than sheer com-
putational scale.

The efficiency translates to practical deployment
advantages: at a hosting cost of $0.8 per hour
and an average inference time of 34.15 seconds,
our model enables responsive financial advisory
services without prohibitive infrastructure require-
ments. These results validate the effectiveness of
our novel data generation framework. They demon-
strate that by carefully integrating financial and
behavioral signals into training data, it is possible
to create competent, domain-specific models that
are also economically viable. This presents a com-
pelling approach for developing production-ready
financial advisory tools that do not rely solely on
expensive, large-scale models.

5 Future Works

We will advance this research by first determin-
ing the optimal path for global scaling: either fi-
nalizing a US-optimized pipeline for systematic
market porting or—contingent on high-precision
detection of regional signals (e.g., currency sym-
bols, policy terminology, and spelling conven-
tions)—implementing a Mixture-of-Experts (MoE)
framework. In the latter case, a shared backbone
model will process universal financial logic while
lightweight regional experts handle localized nu-
ances. This core model will deploy as a backbone
policy within a thin agentic stack, minimizing la-
tency and cost by resolving queries internally and
invoking external tools (e.g., regulatory databases
or fact-checking APIs) only for uncertainty reso-
lution. We will rigorously measure resulting cost-
latency trade-offs across regions. Rather than addi-
tional supervised fine-tuning, we will treat financial

advice generation as an alignment problem, test-
ing preference-based optimization (e.g., DPO/IPO)
to refine outputs and deploying rule-based com-
pliance layers to enforce regulatory fidelity, bias
mitigation, and tone consistency. Success will be
quantified through targeted evaluations of safety,
compliance adherence, and user trust metrics.

6 Conclusion

Our research establishes a data-centric framework
that enables an 8B-parameter model to achieve se-
mantic fidelity and human-likeness on par with,
and sometimes exceeding, 27–32B baselines in our
held-out evaluations and blind LLM-jury study. On
a 500-query test, the model outperforms Gemma3-
27B by 5% on BLEURT and is competitive on
BERTScore, with only a 2% difference; jury rank-
ings show the 8B system approaching the 27–32B
leaders. These gains stem from three synergistic
components: explicit psychological cues, retrieval-
augmented grounding, and a thin agentic execu-
tion layer. The modular design supports incremen-
tal extension (e.g., regional experts with minimal
retraining). While geographic scope, behavioral
depth, and privacy safeguards remain limitations,
this work offers a cost-aware backbone for stand-
alone personal-finance assistants and a viable alter-
native to monolithic cloud deployments—leaving
a precise cost/latency audit to future work.

Limitations

Several aspects of our work leave room for future
improvements. First, our study is limited to in-
quiries sourced solely from Reddit, which may
overlook other demographics and query formats,
suggesting a need for more diverse data sources.
Second, our 19k sample dataset, though sufficient
for proof-of-concept, lacks the scale and diversity
needed to cover the full spectrum of real-world
personal finance scenarios. Future work should ex-
pand the corpus with varied sources beyond Reddit
to improve generalization. Third, our psycholog-
ical analysis remains rudimentary, deriving only
basic sentiment from phrases rather than incorpo-
rating enhanced psychological indicators such as
risk tolerance or financial stress through specialized
surveys or transfer learning from clinical datasets.
Finally, our framework’s scope excludes tasks be-
yond core natural language processing, particularly
multi-modal data processing and reasoning capa-
bilities, which represent critical areas for future

---

<!-- PAGE 9 -->

Table 4: Cost and Inference Performance Analysis for Deployment. Total costs reflect the expense to infer 504
queries from the test set, with each model benchmarked using four concurrent requests.

Model

Size (GB) Endpoint Cost

GPU

Inference Time Total Time Total Cost

($/h)

3.8
2.5
1.8
0.8
3.8
1.8
0.8
0.8

4xL4
1xA100
1xL40S
1xL4
1xA100
1xL40S
1xL4
1xL4

(s/query)

167.86
64.34
58.26
34.15
37.99
54.18
33.58
29.15

(h)

5.82
2.23
2.02
1.19
1.32
1.88
1.17
1.01

($)

22.33
5.63
3.67
0.96
5.05
3.41
0.94
0.82

QWQ-32B
Gemma3-27B
Gemma3-12B
Ours (8B)
Mistral-24B-2501
DeepSeek-Qwen-14B
Llama3-8B
Mistral-7B

65.0
46.4
20.0
16.4
46.1
29.5
16.1
14.5

research expansion.

Acknowledgements

I want to express my sincere gratitude to Raghu
Ram Theerthala (KPIT Technologies) for his
valuable contributions to the related works section
and insightful discussions during the brainstorming
sessions that helped shape this research. I am grate-
ful to Prathyusha Akundi, Syed Md. Bilal, Ashish
Kubade, and Sai Narayan for their careful review
of the manuscript and constructive feedback that
improved the clarity and quality of this work. This
research was supported by Perfios Software So-
lutions, which sponsored the computational costs
and infrastructure required for model training and
evaluation.

Data & Code Availability

The dataset, model, and code artifacts described
in this paper are publicly available on Hugging
Face. All data has been de-identified following
the ethical guidelines described in Section 6, with
personally identifiable information removed from
Reddit sources. The resources are released under
the Apache 2.0 license to facilitate reproducibility
and future research in behavioral finance and LLM
applications.

The following resources are available:

• Model: Fine-tuned Qwen-3-8B model at

https://huggingface.co/
Akhil-Theerthala/Kuvera-8B-qwen3-v0.
2.1

• Dataset: 19k sample reasoning dataset at

https://huggingface.co/
datasets/Akhil-Theerthala/
Kuvera-PersonalFinance-V2.1

Ethical Considerations

We curate data from publicly available Reddit
posts and aggressively de-identify them: user-
(e.g.,
names/links/metadata are removed, PII
names, emails, phone numbers, addresses, IDs)
is scrubbed, and queries are lightly rephrased so
only the financial situation remains; no raw identi-
fiers are stored or released. The system is for ed-
ucational use only—not fiduciary or personalized
financial advice—and our prompts/filters forbid un-
safe guidance (e.g., evasion, “guaranteed returns”).
Evaluation uses multiple LLM judges; we report
inter-judge agreement and run judge-swap checks
to limit model-family bias.

References

Rohit Aggarwal and Harpreet Singh. 2024. Overcoming
limitations of ai agents: Integrating tacit knowledge
through inferred latent themes. Available at SSRN
4843878.

Khushbu Agrawal. 2012. A conceptual framework of
behavioral biases in finance. IUP Journal of Behav-
ioral Finance.

Moonshot AI. 2025.

Kimi-k2-instruct (revision

2f7e011).

H Kent Baker, Greg Filbeck, and Victor Ricciardi. 2017.
How behavioural biases affect finance professionals.
The European Financial Review, pages 25–29.

Bogleheads. 2025. Bogleheads - investing advice in-

spired by john bogle.

Ljubiša Boji´c, Olga Zagovora, Asta Zelenkauskaite,
Vuk Vukovi´c, Milan ˇCabarkapa, Selma Veseljevi´c
Jerkovi´c, and Ana Jovanˇcevi´c. 2025. Comparing
large language models and human annotators in la-
tent content analysis of sentiment, political leaning,
emotional intensity and sarcasm. nature briefing.

---

<!-- PAGE 10 -->

Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A.
Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt
Keutzer, Aditya Parameswaran, Dan Klein, Kannan
Ramchandran, Matei Zaharia, Joseph E. Gonzalez,
and Ion Stoica. 2025. Why do multi-agent llm sys-
tems fail? Preprint, arXiv:2503.13657.

DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingx-
uan Wang, Bochao Wu, Chengda Lu, Chenggang
Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan,
Damai Dai, Daya Guo, Dejian Yang, Deli Chen,
Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai,
and 181 others. 2025. Deepseek-v3 technical report.
Preprint, arXiv:2412.19437.

DeepSeekAI. 2025. deepseek-ai/deepseek-r1-distill-

qwen-14b.

Han Ding, Yinheng Li, Junhao Wang, and Hang Chen.
2024. Large language model agent in financial trad-
ing: A survey. Preprint, arXiv:2408.06361.

Yunfan Gao, Yun Xiong, Meng Wang, and Haofen
Wang. 2024. Modular rag: Transforming rag systems
into lego-like reconfigurable frameworks. Preprint,
arXiv:2407.21059.

Google. 2025. Gemini 2.0 flash. https://cloud.
google.com/vertex-ai/generative-ai/docs/
model-reference/inference.

Almog Gueta, Amir Feder, Zorik Gekhman, Ariel Gold-
stein, and Roi Reichart. 2025. Can llms learn macroe-
conomic narratives from social media? Preprint,
arXiv:2406.12109.

Udit Gupta. 2023. Gpt-investar: Enhancing stock
investment strategies through annual report analy-
arXiv preprint
sis with large language models.
arXiv:2309.03079.

Xuewen Han, Neng Wang, Shangkun Che, Hongyang
Yang, Kunpeng Zhang, and Sean Xin Xu. 2024.
Enhancing investment analysis: Optimizing ai-
agent collaboration in financial research. Preprint,
arXiv:2411.04788.

Oudom Hean, Utsha Saha, and Binita Saha. 2025. Can
ai help with your personal finances? Applied Eco-
nomics, page 1–9.

Zengyi Huang, Chang Che, Haotian Zheng, and Chen Li.
2024. Research on generative artificial intelligence
for virtual financial robo-advisor. Academic Journal
of Science and Technology, 10(1):74–80.

Investopedia. 2025.

Investopedia.

https://www.

investopedia.com/.

Satyadhar Joshi. 2025. A comprehensive review of gen
ai agents: Applications and frameworks in finance,
investments and risk domains. International Jour-
nal of Innovative Science and Research Technology,
pages 1339–1355.

Kausik Lakkaraju, Sara E Jones, Sai Krishna Revanth
Vuruma, Vishal Pallagani, Bharath C Muppasani, and
Biplav Srivastava. 2023. Llms for financial advise-
ment: A fairness and efficacy study in personal de-
cision making. In Proceedings of the Fourth ACM
International Conference on AI in Finance, ICAIF
’23, page 100–107, New York, NY, USA. Association
for Computing Machinery.

Meisin Lee and Soon Lay-Ki. 2024. ’finance wizard’ at
the finllm challenge task: Financial text summariza-
tion. Preprint, arXiv:2408.03762.

Jinzheng Li, Jingshu Zhang, Hongguang Li, and Yiqing
Shen. 2024. An agent framework for real-time fi-
nancial information searching with large language
models. Preprint, arXiv:2502.15684.

Xiao-Yang Liu, Guoxuan Wang, Hongyang Yang, and
Daochen Zha. 2023. Data-centric fingpt: Democra-
tizing internet-scale data for financial large language
models. NeurIPS Workshop on Instruction Tuning
and Instruction Following.

Zhaowei Liu, Xin Guo, Fangqi Lou, Lingfeng Zeng,
Jinyi Niu, Zixuan Wang, Jiajie Xu, Weige Cai, Zi-
wei Yang, Xueqian Zhao, Chao Li, Sheng Xu, Dezhi
Chen, Yun Chen, Zuo Bai, and Liwen Zhang. 2025.
Fin-r1: A large language model for financial rea-
soning through reinforcement learning. Preprint,
arXiv:2503.16252.

Zian Liu and Renjun Jia. 2025. Llm4fts: Enhancing
large language models for financial time series pre-
diction. Preprint, arXiv:2505.02880.

Yichen Luo, Yebo Feng, Jiahua Xu, Paolo Tasca, and
Yang Liu. 2025. Llm-powered multi-agent system
for automated crypto portfolio management. arXiv
preprint arXiv:2501.00826.

Glenn Matlin, Mika Okamoto, Huzaifa Pardawala,
Yang Yang, and Sudheer Chava. 2025. Finance
Preprint,
language model evaluation (flame).
arXiv:2506.15846.

Kiana Jafari Meimandi, Gabriela Aránguiz-Dias,
Grace Ra Kim, Lana Saadeddin, and Mykel J.
Kochenderfer. 2025. The measurement imbalance in
agentic ai evaluation undermines industry productiv-
ity claims. Preprint, arXiv:2506.02064.

Meta. 2024. meta-llama/llama-3.1-8b-instruct.

MistralAI. 2025a. mistralai/mistral-7b-instruct-v0.3.

MistralAI. 2025b. mistralai/mistral-small-24b-instruct-

2501.

Izunna Okpala, Ashkan Golgoon, and Arjun Ravi Kan-
nan. 2025. Agentic ai systems applied to tasks in
financial services: Modeling and model risk manage-
ment crews. Preprint, arXiv:2502.05439.

---

<!-- PAGE 11 -->

Daniel E. O’Leary. 2025. Editorial: Analysis of senti-
ment estimates and cognitive fallacies in large lan-
Intelligent Systems in Accounting,
guage models.
Finance and Management, 32(3):e70010. E70010
9691779.

2025a.

OpenAI.
card.
2221c875-02dc-4789-800b-e7758f3722c1/
o3-and-o4-mini-system-card.pdf.

system
https://cdn.openai.com/pdf/

o4-mini

and

o3

OpenAI. 2025b. Openai text-embeddings-3.

Qwen. 2025. Qwen/qwq-32b.

Reddit. [2025]. Reddit: The heart of the internet.

https://www.reddit.com.

Donald G. Saari. 2023. Selecting a voting method: the
case for the borda count. Constitutional Political
Economy, 34(3):357–366.

Javier Sanz-Cruzado, Edward Richards, and Richard
McCreadie. 2024. Far-ai: A modular platform for in-
vestment recommendation in the financial domain. In
Advances in Information Retrieval, pages 267–271,
Cham. Springer Nature Switzerland.

Thibault Sellam, Dipanjan Das, and Ankur P. Parikh.
2020. Bleurt: Learning robust metrics for text gener-
ation. Preprint, arXiv:2004.04696.

Sentence-Transformers. 2021. all-minilm-l12-v2.

Takehiro Takayanagi, Kiyoshi Izumi, Atsuo Kato,
Naoyuki Tsunedomi, and Yukina Abe. 2023. Per-
sonalized stock recommendation with investors’ at-
tention and contextual information. In Proceedings
of the 46th International ACM SIGIR Conference on
Research and Development in Information Retrieval,
SIGIR ’23, page 3339–3343, New York, NY, USA.
Association for Computing Machinery.

Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya
Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin,
Tatiana Matejovicova, Alexandre Ramé, Morgane
Rivière, Louis Rouillard, Thomas Mesnard, Geoffrey
Cideron, Jean bastien Grill, Sabela Ramos, Edouard
Yvinec, Michelle Casbon, Etienne Pot, Ivo Penchev,
and 197 others. 2025b. Gemma 3 technical report.
Preprint, arXiv:2503.19786.

Kesen Wang, Daulet Toibazar, Abdulrahman Alfulayt,
Abdulaziz S. Albadawi, Ranya A. Alkahtani, Asma A.
Ibrahim, Haneen A. Alhomoud, Sherif Mohamed,
and Pedro J. Moreno. 2025. Multi-agent interactive
question generation framework for long document
understanding. Preprint, arXiv:2507.20145.

Neng Wang, Hongyang Yang, and Christina Dan Wang.
2023. Fingpt: Instruction tuning benchmark for open-
source large language models in financial datasets.
NeurIPS Workshop on Instruction Tuning and Instruc-
tion Following.

Philipp Winder, Christian Hildebrand, and Jochen Hart-
mann. 2024. Biased echoes: Generative ai models
reinforce investment biases and increase portfolio
risks of private investors.

An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025. Qwen3 technical report. Preprint,
arXiv:2505.09388.

Hongyang Yang, Xiao-Yang Liu, and Christina Dan
Wang. 2023. Fingpt: Open-source financial large lan-
guage models. FinLLM Symposium at IJCAI 2023.

Boyu Zhang, Hongyang Yang, and Xiao-Yang Liu. 2023.
Instruct-fingpt: Financial sentiment analysis by in-
struction tuning of general-purpose large language
models. FinLLM Symposium at IJCAI 2023.

Takehiro Takayanagi, Kiyoshi Izumi, Javier Sanz-
Cruzado, Richard McCreadie, and Iadh Ounis. 2025a.
Are generative ai agents effective personalized finan-
cial advisors? Preprint, arXiv:2504.05862.

Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.
Weinberger, and Yoav Artzi. 2020. Bertscore:
Preprint,
Evaluating text generation with bert.
arXiv:1904.09675.

Takehiro Takayanagi, Masahiro Suzuki, Kiyoshi Izumi,
Javier Sanz-Cruzado, Richard McCreadie, and Iadh
Ounis. 2025b. Finpersona: An llm-driven conver-
sational agent for personalized financial advising.
In Advances in Information Retrieval, pages 13–18,
Cham. Springer Nature Switzerland.

Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang,
Huan Lin, Baosong Yang, Pengjun Xie, An Yang,
Dayiheng Liu, Junyang Lin, Fei Huang, and Jingren
Zhou. 2025. Qwen3 embedding: Advancing text
embedding and reranking through foundation models.
Preprint, arXiv:2506.05176.

Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-
Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan
Schalkwyk, Andrew M. Dai, Anja Hauth, Katie
Millican, David Silver, Melvin Johnson, Ioannis
Antonoglou, Julian Schrittwieser, Amelia Glaese,
Jilin Chen, Emily Pitler, Timothy Lillicrap, Angeliki
Lazaridou, and 1332 others. 2025a. Gemini: A fam-
ily of highly capable multimodal models. Preprint,
arXiv:2312.11805.

Yuhan Zhi, Xiaoyu Zhang, Longtian Wang, Shumin
Jiang, Shiqing Ma, Xiaohong Guan, and Chao Shen.
2025. Exposing product bias in llm investment rec-
ommendation. Preprint, arXiv:2503.08750.

Yuhang Zhou, Yuchen Ni, Zhiheng Xi, Zhangyue Yin,
Yu He, Gan Yunhui, Xiang Liu, Zhang Jian, Sen Liu,
Xipeng Qiu, Yixin Cao, Guangnan Ye, and Hongfeng
Chai. 2025. Are LLMs rational investors? a study

---

<!-- PAGE 12 -->

on the financial bias in LLMs. In Findings of the As-
sociation for Computational Linguistics: ACL 2025,
pages 24139–24173, Vienna, Austria. Association
for Computational Linguistics.

6

7

8

### Key Points ###
{key_points_to_keep_in_mind}

David Zibriczky. 2016. Recommender systems meet
finance: A literature review. In International Work-
10
shop on Personalization & Recommender Systems in
11
Financial Services.

9

12

Appendices

13

14

---
**Inputs**:
{inputs}
---
**Your Response**:"""

A Prompting Guidelines followed for the
generation and evaluation stages

A.1.2

Individual Phases

1. Classification:

A.1 Guidelines followed in the generation

stage.

This section focuses on outlining the guidelines
followed in crafting the prompts for each phase of
generating and evaluating the outputs.

A.1.1 Overarching principles
There are three core principles followed for the
process of crafting the prompts:

a. Modularity

b. Deconstruction

c. Personification

The goal of the overall prompt crafting is to
keep the overall structure of the prompts similar
and swappable depending on the task at hand. As
with the framework, where the complex task of
generating a suitable response is broken down into
individual phases, the prompts are broken down to
make sure the structure of the instructions given to
the model remains the same.

Each stage of the prompting had a unique, suit-
able persona (e.g., linguistic analysis expert, expert
financial reasoning engine). This role-playing tech-
nique primes the model to access relevant knowl-
edge, adopt the appropriate tone, and constrain its
behavior to the specific requirements of the task.

The generic structure of the prompt is as follows:

1

2

3

4

5

"""
You are a {persona}, whose task is to

(cid:44)→

{task_details}.

### INSTRUCTION ###
{instructions_for_the_task}

a. The primary goal of this stage is to
classify incoming user queries into suit-
able categories of personal finance. The
prompt constrains the model by forc-
ing a single-label classification (ONE of
the following) based on PRIMARY IN-
TENT, which prevents ambiguity and en-
sures a decisive output for downstream
routing.

b. Each category has a Scope and an ex-
ample that the model uses to make its
decisions. If the query does not fall into
any of the categories, the query is labeled
Not_Applicable.

2. Query Analysis:

a. The primary goal of this prompt is to
direct the model to break down the user
query into more specific and manageable
pieces of information.

b. Since most of the user queries on Reddit
and in general are often filled with unre-
lated noise, this stage directs the model
to distil the user’s query into essential se-
mantic elements, eliminating the conver-
sational distractions and concentrating
on actionable concerns and their impact
on the key stakeholders.

3. Context Analysis:

a. The context analysis is one of the key
prompts that influences the quality of the
output by the framework. The prompt
directs the final model to generate action-
able and insightful contextual summaries
that are placed into the model’s natural
chain-of-thought.

---

<!-- PAGE 13 -->

b. The prompt explicitly asks for a Concise
chain-of-thought Analysis Block and in-
structs the model that this is an inter-
nal reasoning step, not the final answer.
This step forces the model to externalise
its reasoning process, exploring multiple
scenarios and their consequences before
concluding.

c. By requiring the model to detail the
Stakeholder Impact for each approach,
the prompt ensures a holistic analysis
that considers the financial and emo-
tional consequences for all relevant par-
ties mentioned in the query.
This
scenario-based analysis moves the re-
sponses beyond simple fact-based anal-
ysis to a more human-centred form of
reasoning.

4. Psychological analysis

a. The goal of this prompt is to direct the
model and extract the key information
about the user’s state of mind when ask-
ing the query.

b. The prompt demands that every conclu-
sion about sentiment, emotion, or intent
be justified by referencing specific words
or phrases. This approach grounds the
analysis in textual evidence, preventing
the model from making unfounded psy-
chological assumptions and improving
the explainability of its affective under-
standing.

c. This analysis is a separate step from the
financial reasoning (Context Analysis).
This deliberate separation prevents the
user’s emotional state from biasing the
objective financial analysis, and vice-
versa, allowing for a final response that
can synthesise both aspects without com-
promising either.

5. Response Rubric

a. This stage consolidates all the previously
collected information and creates a com-
plete rubric that can direct the model into
generating the final response.

b. The key information from the previ-
ous stages gets highlighted while being
linked to different parts of the user query
for easier reference and understanding.

1

2

3

4

5

6

7

8

9

6. Response Generation

a. This final stage synthesises all preced-
ing analyses into a coherent, user-facing
response.

b. The prompt provides the model with all
previous outputs (the original query and
the comprehensive chain-of-thought) and
explicitly instructs it to integrate both fac-
tual accuracy and emotional intelligence
seamlessly. It acts as a final "assembly"
instruction, guiding the model on how to
combine the rational and affective com-
ponents.

c. The use of clear positive (Do) and neg-
ative (Do not) instructions creates strict
behavioral boundaries. For instance, "Do
not reference the chain-of-thought analy-
sis" ensures the final output is natural and
user-friendly, hiding the complex under-
lying cognitive architecture from the end-
user. These instructions create a helpful
response without being robotic or trans-
parent about its inner workings.

d. These responses are generated in a way
that ensure the ability to train non-
reasoning models from the same dataset.

A.2 Prompt Guidelines for Evaluation

through LLM-as-a-Judge

The goal of the evaluation is to determine which
responses are naturally ranked better than the oth-
ers. Since this is a list-wise ranking with a high
room for confusion or hallucination, the evaluation
criterion are strictly defined.

The overall prompt structure for each of the case

are as follows:

(cid:44)→

"""
You are a {persona}. Your task is to
rank financial advice responses
from best to worst based *solely*
on the strict definition of
{target_aspect}.

(cid:44)→

(cid:44)→

(cid:44)→

### **Evaluation Criteria**
{Evaluation Criterion}

#### **I. Primary Criteria (What to

look for):**

(cid:44)→
{primary_set_of_instructions}

---

<!-- PAGE 14 -->

10

11

12

13

14

15

16

17

18

19

20

21

22

#### **II. Explicit Penalties (What to

penalize):**

(cid:44)→
{penalizing_instructions}

#### ** III. Key Points to note:**
{additional_instructions}
---

**Query:** {query}

**Responses to Rank:**
{anonymized_shuffled_model_responses}
"""

1. Accuracy:

a. The goal of this prompt is to direct the
model to review the search results and
the query to estimate the accuracy of the
output.

b. The responses are penalized if and only if
the responses demonstrate wrong/harm-
ful advice (or) inappropriate financial
concepts to the query.

c. The model is specifically instructed not
to penalise on the style or relevance of
the response and solely focus on the ac-
curacy of the financial concepts provided
in the text. This guides the model to rank
solely based on the accuracy of the finan-
cial concepts present in the response.

2. Plausibility:

a. A response is defined to be plausible if
it sounds reasonable and believable to a
typical user. Some of the key character-
istics include

• Logical flow and coherent reasoning

structure

• Sensible approach to the problem
b. A response is penalized if it contains un-
necessarily verbose or contain excessive
detail. The responses are also penalized
if they contain complex or hard-to-follow
reasoning.

c. The model is specifically instructed not
to penalise on the accuracy or relevance
of the responses.

3. Relevance:

a. A response is considered relevant if it
address every component of the user’s
query. A relevant response should incor-
porate the specific figures, constraints,
and details mentioned in the user’s query,
and answer the questions immediately
without generic introductions.

b. Any partial relevance or additional con-
text not relevant to the query is penalized.

B Modular RAG for Context Analysis

Goal. Given a user query, the context-analysis
phase assembles a compact, high-signal context
pack from two specialized corpora: (i) Behavioral
insights (behavioral economics and psychology)
and (ii) Financial concepts (mainstream personal fi-
nance knowledge). The context pack is then passed
to the response generator.

Corpora. Behavioral insights are sourced from
peer-reviewed research and reputable psychology
venues, complemented by carefully selected psy-
chology blogs for practitioner framing. Financial
concepts are drawn from practical, high-visibility
sources such as Investopedia, Bogleheads, and
other widely cited personal-finance viewpoints. All
raw pages are converted to Markdown with headers
and section structure preserved to retain document
semantics.

Preprocessing and indexing.

• Scraping & normalization: We scrape public
pages (respecting robots/terms), remove boiler-
plate (nav, ads), and normalize to Markdown with
stable headings.

• Semantic chunking: Documents are segmented
into modular chunks along header/semantic
boundaries to keep each chunk topically coher-
ent; we attach metadata (source, URL or han-
dle, snapshot time, section path, corpus tag:
behavioral or financial).

• Dense indexing: Each chunk is embedded with
text-embeddings-large-003 and stored in a
vector databsase (ChromaDB).

Retrieval and re-ranking (per query).

1. Dual retrieval: From each index, retrieve the
top-k candidates (k=25) using the query em-
bedding.

---

<!-- PAGE 15 -->

2. Cross-encoder

re-ranking:
Concate-
nate candidates
from both corpora and
re-rank with a lightweight cross-encoder
(sentence-transformers/all-minilm-l12-v2);
keep top-m (m=15).

3. LLM synthesis/filter: A fast LLM (gemini-2.0-
flash) receives {top-m chunks, query} and (a)
extracts salient facts, definitions, and decision
criteria; (b) discards residual off-topic spans; (c)
emits a streamlined, source-attributed context.

Assembly and handoff. The streamlined context
(with inline source attributions and corpus tags) is
passed, together with the user input, to the final
LLM that completes the context-analysis phase.

Behavioral vs. financial module roles. The be-
havioral module surfaces cognitive-bias descrip-
tors, debiasing tactics, and user-state cues (e.g., loss
aversion framing, present bias prompts). The finan-
cial module surfaces actionable rules of thumb,
definitions, procedures, and typical constraints
(e.g., contribution limits, insurance concepts, pay-
off ordering heuristics). Both modules contribute to
the same context pack; behavioral cues guide how
advice is framed, while financial chunks ground
what advice is provided.

Limitations.
(1) Coverage and staleness depend
on the snapshot of public sources; (2) blogs can in-
troduce style bias despite re-ranking; (3) the synthe-
sis step may over-prioritize well-structured sources.
We mitigate these by preserving source attributions,
tracking snapshot timestamps, and prompting syn-
thesis to prefer higher-priority sources when con-
flicts arise.

C Deeper Evaluation Results

C.1 Score Definitions and Rationale

We evaluate responses along three orthogonal
axes—Accuracy, Plausibility, and Relevance—to
separate factual correctness, reasoning quality, and
task alignment. This decomposition avoids a single
scalar that can reward fluent but unsafe answers
or penalize terse yet correct ones, and it enables
targeted error analysis and ablations.

Accuracy (financial correctness).
• Objective. Judge reviews the response against
the query and retrieved evidence and scores only
the validity of financial concepts, calculations,
and advice.

• Penalties. Deductions occur iff the answer con-
tains wrong or harmful guidance, or misapplies
financial concepts to the user’s situation.

• Non-considerations. Style, tone, verbosity, and
even partial coverage are not penalized; the judge
is instructed to focus exclusively on correctness.

Plausibility (reasoning quality).
• Objective. Assess whether the answer reads as
reasonable and believable to a typical user—i.e.,
it exhibits a clear logical flow and a coherent
problem-solving structure.

• Penalties. Overly verbose, needlessly complex,
or hard-to-follow chains of reasoning are penal-
ized.

• Non-considerations. Factual correctness and
topical coverage are not scored here; the lens is
purely rhetorical/structural.

Relevance (task alignment).
• Objective. Verify that the response directly ad-
dresses every component of the user’s query, in-
corporates the user’s numbers, constraints, and
context, and answers without generic preambles.

• Penalties. Partial coverage, tangential content,
or extra context not pertinent to the query is pe-
nalized.

• Non-considerations. Factual accuracy and stylis-

tic polish are ignored for this axis.

C.2 Borda Points

Definition. For a listwise ranking of n systems,
the item placed at rank r (r = 1 is best) receives a
Borda score

b = n − r,

so the top entry gets n − 1 points and the last gets
0.

Motivation. Borda aggregation is well–suited to
LLM-as-a-judge experiments where relative qual-
ity matters more than absolute scores:

• Full-order utilisation: every position con-
tributes signal, ensuring that small but con-
sistent advantages are captured rather than dis-
carded by winner-takes-all rules.

• Cardinal comparability: with a fixed candi-
date set, raw points can be averaged across
queries and judges without normalisation, giv-
ing a stable, interpretable mean.

---

<!-- PAGE 16 -->

• Robustness to mild noise: swapping adjacent
middle ranks changes the total by only ±1, so
individual judge idiosyncrasies exert limited
influence on the final average.

Interpretation. Higher mean Borda points in-
dicate that a system outranks its peers more often.
The maximum possible mean is n − 1; the gap to
this ceiling offers an intuitive sense of head-room.

Limitations.

• Rank-reversal: inserting or removing a candi-
date can change every system’s score, compli-
cating longitudinal comparisons.

• Independence of Irrelevant Alternatives (IIA)
violation: a judge’s relative preference be-
tween two systems can affect, and be affected
by, ranks assigned to others.

• Equal-interval assumption: the method treats
the gap between successive ranks as uni-
form, ignoring situations where judges per-
ceive larger quality jumps near the top.

• Strategic susceptibility: if human judges know
what influences the aggregation, they could in-
flate or deflate lower ranks to benefit a favored
system.

C.3 LLM-Jury Protocol

LLM-based judging scales across topics, is inex-
pensive, and achieves strong agreement with hu-
man raters when rubrics are explicit and task con-
text is provided. It also captures holistic qualities
(e.g., coherence, task fit) that single-number simi-
larity metrics may miss.

It should be noted that zero-shot judging is vul-
nerable to position bias (earlier items rank higher),
same-family bias (preference for outputs from the
judge’s own family), and prompt/leniency variance.
We therefore (i) use multi-shot prompts to anchor
criteria, (ii) evaluate with listwise ranking on in-
dependently shuffled candidate lists, and (iii) di-
versify judges across model families to minimize
correlated bias.

Judge pool and prompting. We employ two
main heterogeneous judges: DeepSeek-v3-0324 (5-
shot), Kimi-k2 (3-shot). For each query and cri-
terion (Accuracy, Plausibility, Relevance), judges
rank anonymized model outputs in a single list.
Few-shot exemplars are held constant within a run
and varied across repeats to reduce overfitting to

any one demonstration set. A subsample of these
rankings were further validated by o4-mini model
to consolidate the relative performance.

Scoring and aggregation (per criterion). For
each query, judges perform multi-shot listwise rank-
ing over anonymized outputs using the rubrics in
Sec. C. Ranks are converted to raw Borda points
b = n − r. We then:

1. average b across shuffles/repeats for each judge;

2. average across the judges to obtain a per-query,

per-criterion score for each model;

3. average across all queries within a category (e.g.,
the “overall” set or a PF subcategory) to obtain
the model’s criterion-wise mean in that cate-
gory.

The stacked bars in Fig. 2 display these criterion-
wise means (Accuracy, Plausibility, Relevance) for
each model. For a single category-level number,
we also report the unweighted average of the three
criterion-wise means as the model’s final represen-
tation score in that category.

C.4 Overall Category Scores (Accuracy,

Plausibility, Relevance)

We report criterion-wise means derived from the
raw Borda points assigned by the LLM jury
(Sec. C.3). For each criterion and model, scores
are averaged across judges and queries within the
overall set. Higher is better.

Accuracy. Figure 3 shows a size-tilted pattern:
QwQ-32B (reasoning) leads, followed by Gemma3-
27B-it and Gemma3-12B-it. Mistral-Small-24B sits
between this top cluster and the rest. The proposed
8B model is mid-pack—behind the leaders and the
24B baseline, but ahead of several 7–14B baselines.
This points to factual calibration and retrieval/verifi-
cation as the primary levers to close the gap, rather
than rewriting or stylistic tuning.

Plausibility. As shown in Fig. 4, QwQ-32B ranks
first, with Gemma3-27B-it next. The proposed 8B
clusters near the front: it exceeds the Mistral-Small-
24B baseline but trails Gemma3-12B-it. This sug-
gests that the dataset structure and few-shot con-
ditioning induce coherent reasoning steps and a
sensible flow even at mid scale.

Relevance. Figure 5 indicates strong task align-
ment at the top end (QwQ-32B, Gemma3-27B-it,

---

<!-- PAGE 17 -->

Figure 3: Accuracy (mean raw Borda points per query,
averaged over judges). A size-driven lead is visible; the
proposed 8B is mid-pack, indicating factual calibration
as the primary improvement lever.

Figure 4: Plausibility (mean raw Borda points). The
proposed 8B clusters near the front and matches or
exceeds several larger baselines, reflecting strong
logical flow and coherent reasoning.

Gemma3-12B-it). The proposed 8B ranks next
(4/8), ahead of the remaining baselines, suggest-
ing it reliably maps user constraints and addresses
all parts of the query without drifting into generic
preambles. The residual gap likely reflects cases
that require exhaustive edge handling (e.g., niche
eligibility rules) rather than broad intent recogni-
tion.

Cross-criterion takeaway. Across criteria, the
proposed 8B model is plausibility– and relevance-
competitive while lagging most on accuracy. The
next steps of improvement is therefore to prioritize
factual grounding and numeric checking: adding
targeted retrieval, rule tables, and lightweight cal-
culation guards should yield the largest absolute
gains relative to effort.

C.5 Parameter Efficiency: Category-wise
Borda per Billion Parameters

To evaluate parameter efficiency rather than abso-
lute quality, we compute a per-parameter utility
for each criterion. For model i with Pi billion pa-
rameters and mean raw Borda points ¯bi,c on crite-
rion c ∈ {Accuracy, Plausibility, Relevance} (av-
eraged over judges and queries within the category),
we define

ei,c =

¯bi,c
Pi

(Borda points per billion parameters).

This ratio captures the marginal productivity of
capacity: how much judged quality is obtained per

parameter, holding the evaluation protocol fixed. It
is not a substitute for absolute scores (Sec. C.4),
but a complementary lens for cost-, latency-, and
memory-constrained deployments.

Relevance efficiency. Figure 6 shows the pro-
posed 8B model with the highest Borda-per-
parameter in Relevance, followed by Gemma3-12B-
it, then Mistral-7B-v0.3 and Llama3-8B. Large rea-
soning models (e.g., QwQ-32B, Gemma3-27B-it)
trail on this per-parameter metric despite strong
absolute relevance (Fig. 5), indicating diminish-
ing returns in alignment per unit capacity at larger
scales.

Plausibility efficiency. As shown in Fig. 7, the
proposed 8B again leads, with Mistral-7B-v0.3 and
Gemma3-12B-it close behind (virtually tied), fol-
lowed by Llama3-8B. This suggests that the dataset
structure and few-shot conditioning yield coher-
ent reasoning with high utility density—quality per
parameter.

In Fig. 8, the proposed 8B
Accuracy efficiency.
tops Accuracy per parameter, followed by Mistral-
7B-v0.3 and Gemma3-12B-it (near-tie). Models
that dominate absolute accuracy (Sec. C.4) deliver
lower accuracy per parameter, implying that tar-
geted grounding and calculation checks can be
more cost-effective than increasing model size.

(1) The proposed 8B is
Takeaways and caveats.
the most parameter-efficient across all three cri-
teria, reinforcing the central claim that careful

---

<!-- PAGE 18 -->

Figure 5: Relevance (mean raw Borda points). The
proposed 8B ranks immediately behind the top three,
ahead of other baselines, indicating consistent mapping
from user constraints to concrete answers.

Figure 6: Relevance efficiency: mean raw Borda points
per billion parameters (higher is better). The proposed
8B leads, followed by Gemma3-12B-it and Llama3-8B.

supervision can substitute for scale in personal-
finance tasks. (2) Efficiency does not equal ab-
solute quality; it informs deployment decisions
where memory/latency are binding. (3) The ratio
ignores runtime constants (KV-cache bandwidth,
batch scheduling) and training cost; it should be
read alongside absolute Borda results and system-
level latency/memory budgets.

C.6 Qualitative Category-wise Evaluations

We analyze twelve personal-finance subdo-
mains—Auto, Budgeting, Credit, Debt, Employ-
ment, Housing, Insurance, Investing, Planning,
Retirement, Saving, Taxes. For each, we report
criterion-wise means derived from normalized
Borda points (Sec. C.3). The dashed horizontal
line in each panel marks the cohort-wide mean for
orientation.

Please note that the category-based evaluations
in this appendix use raw Reddit post flairs, which
differ from the eight thematic categories curated
for the main analysis.

C.6.1 Relevance by Subdomain

Relevance captures task alignment: covering all
parts of the user’s request, using their numbers/con-
straints, and answering without generic preambles
(Sec. C.1).

most categories and hovers around the cohort
mean.

• Strengths are most visible in Budgeting, Em-
ployment, Planning (and close-to-mean in Insur-
ance/Retirement).

• Wider gaps appear in Auto, Housing, Credit (and
occasionally Investing/Taxes), where locality-
and rule-heavy edge cases require more exhaus-
tive coverage.

C.6.2 Accuracy by Subdomain
Accuracy isolates financial correctness: advice and
calculations must be right for the stated scenario;
style and coverage are ignored (Sec. C.1).

• Absolute leaders are the larger models across

most subdomains.

• The proposed 8B model is mid-pack overall, with
competitive accuracy in Debt, Planning, Employ-
ment, and notably larger gaps in Housing, Insur-
ance, Taxes (and Credit).

• This pattern suggests targeted grounding (poli-
cy/limit tables, calculators) is a higher-leverage
fix than stylistic tuning for closing the remaining
gap.

C.6.3 Plausibility by Subdomain

• A consistent top cluster is formed by larger
reasoning-aligned models. The proposed 8B
model sits immediately behind this cluster in

Plausibility measures reasoning flow and readabil-
ity: clear structure, sensible steps, and absence of
unnecessary complexity (Sec. C.1).

---

<!-- PAGE 19 -->

Figure 7: Plausibility efficiency: mean raw Borda
points per billion parameters. The proposed 8B ranks
first; compact 7–8B baselines are competitive, while
very large models show lower utility density.

Figure 8: Accuracy efficiency: mean raw Borda points
per billion parameters. The proposed 8B tops the
cohort, indicating that factual calibration gains can be
achieved more cheaply than by scaling parameters
alone.

• The proposed 8B clusters close to the leaders
across most subdomains, with stronger relative
showings in Debt and Planning; margins are
lower in Taxes and Retirement.

• Lower margins in regulation-dense areas mir-
ror the accuracy pattern: where facts are brittle,
judges penalize circuitous explanations.

C.7 Overall Summary, Limitations, and Next

Steps

Summary. Taken together, the results tell a sim-
ple story. On absolute scores (Sec. C.4), the largest
baselines lead across Accuracy, Plausibility, and
Relevance, as expected. The proposed 8B model
sits just behind this front cluster on Relevance
and Plausibility and lands mid-pack on Accuracy.
When we switch to a parameter-efficiency lens
(Sec. C.5), the picture reverses: the 8B model deliv-
ers the highest Borda-per-parameter across all three
metrics, indicating unusually high utility density
for its size. The subdomain breakdown (Sec. C.6) is
consistent with both views: the 8B model is steady
or above-mean in everyday tasks such as Budgeting,
Planning, Employment (and shows strong plausi-
bility in Debt), while gaps widen in regulation-
and table-heavy areas such as Housing, Insurance,
Taxes, Credit (and occasionally Auto/Investing). In
short, scale drives absolute peaks, but careful su-
pervision yields competitive quality—and superior
efficiency—at mid-scale.

These results suggest prioritizing minimal, high-
leverage grounding over further size increases:
include compact, versioned rule/limit tables for
regulation-intensive domains (e.g., taxes, insurance,
credit), add lightweight calculators/unit-tests for
numeric steps, sharpen supervision with contrastive
edge cases in brittle areas (tax/retirement), diver-
sify judge checks (agreement and judge-swap), and
extend evaluation to short multi-turn interactions
that reward clarifying questions.

D Training Details

We fine-tuned the 8B parameter Qwen-3 model
with AdamW optimizer on bfloat16 precision and
a training split containing 15.6K samples and a
validation set containing 2.6k samples. We trained
the model for four epochs using an optimal batch
size of 256, resulting in around 220 steps overall.
The model underwent training on a solitary A100
GPU within the Runpod cloud GPU infrastructure
for 3 hours.

We preserved three checkpoints per epoch, with
the optimal validation loss attained at step 101. The
training used a cosine learning rate schedule with a
maximum learning rate of 5 × 10−5, a 10% linear
warm-up period of 21 steps (a warmup ratio of
10%), and a minimum learning rate of 5 × 10−6.
Gradients were constrained to a global norm of 1,
weight decay was established at 0.01, and all other
parameters adhered to the default conventions of
the Hugging Face Trainer.

---

<!-- PAGE 20 -->

Figure 9: Category-wise Relevance. The proposed 8B model typically sits just behind the leading cluster and near
the cohort mean; gaps are largest in edge-case, rule-dense areas (e.g., Auto, Housing, Credit).

---

<!-- PAGE 21 -->

Figure 10: Category-wise Accuracy. Larger models lead overall; the proposed 8B is mid-pack with smaller gaps in
everyday planning tasks and larger gaps where year-/jurisdiction-specific rules dominate (e.g., Housing, Insurance,
Taxes).

---

<!-- PAGE 22 -->

Figure 11: Category-wise Plausibility. The proposed 8B delivers coherent reasoning near the leading cluster, with
smaller margins in routine planning tasks and larger ones in regulation-dense areas (e.g., Taxes, Retirement).

---

<!-- PAGE 23 -->

E Sample Model Responses

To provide a qualitative assessment of our model’s
capabilities, this appendix details three compara-
tive case studies. Each case is structured around a
real-world user query, presenting the abridged re-
sponses from our model (Ours-8B) alongside two
baseline models of different sizes (Baseline-L and
Baseline-S). For each case, we outline the query,
summarize the context provided to the models, dis-
play the generated responses, and conclude with a
judge’s final ranking and a rationale based on the
core principles of accuracy, relevance, and plausi-
bility.

Case C1 (Comparative) — Budgeting & Early
Investing at 18

Query (Abridged)

“I’m 18 with about $40k in checking.
I run a
business (will reinvest some), have very low ex-
penses, and my parents cover college/housing.
What should I do so it’s not just sitting idle?”

Context Titles (Summary)

• Emergency fund (3–6 months of spend)

• Roth/SEP-IRA basics

• Low-cost index funds

• Business reinvestment discipline

Abridged Model Responses

start a side business, enjoy life.” (Not tailored to
the user; repeats “start a side business.

Analysis

• Judge Outcome: Baseline-L > Ours–8B >

Baseline-S

• Reasoning: Baseline-L is the most accu-
rate and relevant: it adds specifics for the
self-employed (SEP-IRA), provides a con-
crete allocation sketch, and outlines a clear se-
quence (EF → tax-advantaged → brokerage).
Ours–8B is strong, empathetic, and practical
but more high-level. Baseline-S is generic and
poorly targeted.

Case C2 (Comparative) — Full Roth
Conversion with Mixed Positions

Query (Abridged)
“Early 50s, Trad. IRA has two near-worthless po-
sitions and one large gainer. Full Roth conversion
would push income in the 32–35% bracket. Con-
vert all at once or phase it?”

Context Titles (Summary)

• Roth conversion taxation; Form 8606 report-

ing

• Bracket management and timing; liquidity to

pay tax

• Selling losers post-conversion; market-

volatility risk

Ours–8B I hear the mix of excitement and con-
fusion. . . Since you run a business, reinvest a
portion. For the rest, open a Roth IRA (after-tax,
long-horizon growth) and a taxable brokerage with
low-cost index funds. Before investing, hold 3–6
months of expenses in a high-yield savings account.
Then allocate across business, Roth IRA, and bro-
kerage based on comfort with risk.

Abridged Model Responses
Ours–8B Full conversion now makes strong
sense. Convert entire Trad. IRA, then immedi-
ately sell all three holdings inside the Roth and
reallocate to diversified funds. Steps: compute tax;
execute direct conversion; sell & reallocate; file
taxes: report as a ‘non-deductible contribution
(Form 8606)‘.

Baseline-L (32B) Secure an emergency fund in
a high-yield account; consider reinvesting in the
business with a written plan. As self-employed,
consider a SEP-IRA and Roth/Traditional IRA. Af-
ter that, diversify via a brokerage with index ETFs
(e.g., S&P 500). Includes a sample split: emer-
gency fund, business, retirement accounts, and
ETFs.

Baseline-L (32B) Explains that taxes are based
on total IRA value; losses can’t offset gains here.
Lays out full vs. phased conversion, bracket creep,
irreversibility, and liquidity (use outside funds for
tax). Emphasizes ability to liquidate losers tax-free
in Roth and notes market-drop risk post-conversion.
Provides actionable steps (run scenarios, convert
losers first if phasing).

Baseline-S (7B) Ten generic ideas: emergency
fund, pay off debt, invest in stocks/bonds/real es-
tate, retirement savings, education, charity, travel,

Baseline-S (7B) High-level overview of Roth
conversion basics; repeats general advice; defers to
an advisor; no bracket modelling or concrete steps.

---

<!-- PAGE 24 -->

Analysis

Analysis

• Judge Outcome: Baseline-L > Ours–8B >

• Judge Outcome: Baseline-L > Ours–8B >

Baseline-S

Baseline-S

• Reasoning: Baseline-L is most accurate and
relevant: it answers “am I missing a better
option?” with a structured comparison, con-
crete trade-offs, and clear next steps. Ours–8B
is strong and user-aligned but single-track
(HYSA only), offering less educational depth
for alternatives. Baseline-S is accurate but
generic and light on decision guidance.

Conclusion

These case studies culminate in a clear, yet nuanced,
conclusion about the trade-offs between model
scale, architecture, and performance. The consis-
tent top ranking of the 32B Baseline-L underscores
the value of a large-scale reasoning model for gen-
erating superior, detailed financial guidance. How-
ever, the most compelling finding emerges from
an efficiency perspective. Our 8B non-reasoning
model showed consistent performance at just a
quarter of the size of Baseline-L. It is, in essence,
punching significantly above its weight class, of-
fering a powerful balance of quality and resource
economy. The key differentiators were Baseline-
L’s ability to handle multi-step, nuanced reasoning
and maintain factual integrity, an area where our
model faltered in Case C2.

• Reasoning: Baseline-L is most accurate and
relevant: covers bracket spillover, irrevoca-
bility, external cash for taxes, and volatility
risk, with clear options (full vs. phased) and
steps. Ours–8B is confident and practical but
contains a material filing error (mislabels a
conversion as a non-deductible contribution
on Form 8606), reducing Accuracy. Baseline-
S is generic and least helpful.

Case C3 (Comparative) — Liquidity & Safety
with Uncertain Horizon

Query (Abridged)

“Life changes ahead (move/career/school). I have
$25,000 and may need it anytime. Worried about
market dips.
Is a high-yield savings account
(HYSA) the right place, or am I missing a better
option?”

Context Titles (Summary)

• HYSA basics and FDIC/coverage; money

market accounts

• Short CDs and ladders; T-bills; short-term

bond funds

• Liquidity vs. yield trade-offs; rate monitoring

Abridged Model Responses

Ours–8B Given immediate-access needs and
principal safety, parking the entire $25k in a HYSA
is optimal. HYSAs pay better than regular savings,
allow anytime withdrawals, and avoid CD penal-
ties. Verify a competitive APY and keep the funds
fully flexible.

Baseline-L (32B) Validates HYSA for immedi-
ate access, then compares liquid, low-risk alterna-
tives: money market accounts, short CD ladder-
ing, T-bills, and short-term bond funds. Outlines
pros/cons, insurance/volatility notes, and action-
able steps (open HYSA; optionally ladder a small
slice; monitor rates; named providers/tickers as
examples).

Baseline-S (7B) Confirms HYSA could be good,
mentions inflation in general terms, lists money
market and short CDs, but remains generic and de-
fers to an advisor without a comparison framework.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

|     | Synthesizing    |     | Behaviorally-Grounded |           |     |              | Reasoning |         | Chains: |      | A   |     |
| --- | --------------- | --- | --------------------- | --------- | --- | ------------ | --------- | ------- | ------- | ---- | --- | --- |
|     | Data-Generation |     |                       | Framework |     | for Personal |           | Finance |         | LLMs |     |     |
AkhilTheerthala
PerfiosSoftwareSolutions
|     |     | Abstract |     |     |     | et al., | 2024; | Luo et | al., 2025; | Takayanagi |     | et al., |
| --- | --- | -------- | --- | --- | --- | ------- | ----- | ------ | ---------- | ---------- | --- | ------- |
2023)
Personalizedfinancialadvicerequiresconsid-
|         |         |        |              |      |        | Recent | advances |     | in large | language |     | models |
| ------- | ------- | ------ | ------------ | ---- | ------ | ------ | -------- | --- | -------- | -------- | --- | ------ |
| eration | of user | goals, | constraints, | risk | toler- |        |          |     |          |          |     |        |
ance, and jurisdiction. Prior LLM work has (LLMs)haveshowneffectiveperformanceinact-
focusedonsupportsystemsforinvestorsandfi- ing as decision support systems for investors
nancialplanners. Simultaneously,numerousre- (Gupta,2023)andfinancialplanners(Huangetal.,
centstudiesexaminebroaderpersonalfinance
2024). Thecoreadvantageofnaturallanguagegen-
tasks,includingbudgeting,debtmanagement, erationpresentstheseautomatedsupportsystems
retirement,andestateplanning,throughagen-
|     |     |     |     |     |     | withaunique |     | advantagethat |     | wasneveravailable |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | ----------------- | --- | --- |
ticpipelinesthatincurhighmaintenancecosts,
|     |     |     |     |     |     | in previous | applications. |     |     | This advantage |     | has re- |
| --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | --- | -------------- | --- | ------- |
yieldinglessthan25%oftheirexpectedfinan-
cialreturns. Inthisstudy,weintroduceanovel peatedly shown itspower inlinguistic tasks such
asstreamliningcomplexfinancialnarrativesfrom
andreproducibleframeworkthatintegratesrel-
evantfinancialcontextwithbehavioralfinance extensivedocuments, corporatediscourses, news
studiestoconstructsupervisiondataforend-to-
sources,andsocialmedia.(Guetaetal.,2025;Lee
endadvisors. Usingthisframework,wecreate and Lay-Ki, 2024) The utility of these models is
a19ksamplereasoningdatasetandconducta
|     |     |     |     |     |     | also | being explored |     | in Time | series | (Liu | and Jia, |
| --- | --- | --- | --- | --- | --- | ---- | -------------- | --- | ------- | ------ | ---- | -------- |
comprehensivefine-tuningoftheQwen-3-8B
|                                      |     |     |                      |     |     | 2025)        | and Financial |     | reasoning |     | applications | (Liu |
| ------------------------------------ | --- | --- | -------------------- | --- | --- | ------------ | ------------- | --- | --------- | --- | ------------ | ---- |
| modelonthedataset.                   |     |     | Throughaheld-outtest |     |     |              |               |     |           |     |              |      |
| splitandablindLLM-jurystudy,wedemon- |     |     |                      |     |     | etal.,2025). |               |     |           |     |              |      |
Notwithstandingthiscapability,recentresearch
| strate | that through |     | careful data | curation | and |     |     |     |     |     |     |     |
| ------ | ------------ | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
behavioralintegration,our8Bmodelachieves indicatesthatnomodelexcelsacrossallfinancial
performancecomparabletosignificantlylarger
taskcategories,whichincludetextsummarization,
baselines (14-32B parameters) across factual sentiment analysis, causal analysis, forecasting,
accuracy,fluency,andpersonalizationmetrics
|     |     |     |     |     |     | and text | classification |     | (Matlin |     | et al., | 2025). It |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------- | --- | ------- | --------- |
whileincurring80%lowercoststhanthelarger
|     |     |     |     |     |     | has been | demonstrated |     | that | attaining |     | robust per- |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ---- | --------- | --- | ----------- |
counterparts.
formancefrequentlynecessitatestheutilizationof
| Keywords: |     | Financial | Datasets; | Personal | Fi- |     |     |     |     |     |     |     |
| --------- | --- | --------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
large,expensivemodels,therebyconstrainingthe
| nance; | Reasoning |     | Models; | Large Language |     |              |     |       |            |     |        |           |
| ------ | --------- | --- | ------- | -------------- | --- | ------------ | --- | ----- | ---------- | --- | ------ | --------- |
| Models |           |     |         |                |     | practicality | of  | these | solutions. |     | Due to | these in- |
herentlimitationsandthecomplexityoffinancial
1 Introduction
advisory,manystudiesfocusingonbroaderfinan-
Legal counseling, healthcare, and finance are cial decision systems have preferred an agentic
amongthenumeroushigh-stakesdomainsinwhich approach over training financial domain-specific
personalizedadviceisessential. However,thede- languagemodels. (Okpalaetal.,2025;Joshi,2025;
velopment of this personalized advice is fraught Takayanagietal.,2025a)
with obstacles, requiring substantial investments Althoughtheinitialagenticframeworksfocused
andyearsofhumanexpertise. Recentresearchef- on answering simple inquiries,(Lakkaraju et al.,
fortshavethoroughlyinvestigatedautomateddeci- 2023) recent studies have accelerated the devel-
sionsupportsystemsinvariousareas,emphasizing opmentofthesesystemstoprovidepracticaland
their cost-effectiveness. In the financial sector, a actionableadvicetotheenduser(Takayanagietal.,
varietyofsupportsystemshavebeeninvestigated, 2025b;Okpalaetal.,2025). Theseagentscannow
withaparticularemphasisonassetrecommenda- dynamically interact with users and can assist in
tions and investment predictions. (Sanz-Cruzado varioustaskssuchasrecommendation,questionan-
167
Proceedings of The 10th Workshop on Financial Technology and Natural Language. EMNLP-2025, Suzhou, China

swering,search,andcustomerprofiling. (Lietal., itly modelling this psychological dimension, our
2024;Takayanagietal.,2025a;Hanetal.,2024) frameworkensuresthatpersonalisationandempa-
Althoughagenticsystemsdemonstratepotential theticframingareintrinsictothemodel’sreasoning
inprovidingtailoredfinancialadvice,theirefficacy process,leadingtomoreeffectiveandtrustworthy
| ishinderedbyconsiderableconstraints,including |     |     |     |     |     | financialguidance. |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
the integration with legacy systems, compliance It should also be considered that although re-
withdatasecurityregulations,andhighinference cent agentic frameworks respond based on real-
costs. (Cemri et al., 2025; Wang et al., 2025). timeknowledge;mostoftheseknowledgesources
| In support | of these | concerns, |     | a recent | study by |     |     |     |     |     |     |
| ---------- | -------- | --------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
needtobemanuallycurated(AggarwalandSingh,
(Meimandietal.,2025)illustratesthataconfluence 2024). In addition to this, we should note that
oftechnicalandcost-relatedfactorshindersthese mostoftherecommendationsneededforgeneral
applicationsfromrealizingeven25%oftheiran-
financialadvicedonotrequirereal-timefinancial
ticipatedreturns. Thisresearchalsoestablishesan knowledge. Instead, this advice needs an agent
importantdifferentiation: successinbenchmarks that can inherently retrieve the relevant informa-
does not necessarily equate to success in deploy- tion from its memory. We address this problem
ment. Inpracticalterms,theseproactivefinancial bycarefullycraftingachain-of-thoughtsectionto
advisorsfrequentlyencounteraswiftdeterioration retrievethefinancialcontextrelevanttothequery.
inperformancewithinamatterofmonthsfollowing Recentstudieshaveshownthatinherentbiases
| their implementation, |               |     | attributable | to the        | inherent |             |           |            |     |           |            |
| --------------------- | ------------- | --- | ------------ | ------------- | -------- | ----------- | --------- | ---------- | --- | --------- | ---------- |
|                       |               |     |              |               |          | often limit | users’    | ability    | to  | make many | wealth-    |
| volatility            | of real-world |     | conditions.  | Concurrently, |          |             |           |            |     |           |            |
|                       |               |     |              |               |          | making      | financial | decisions. |     | (Baker et | al., 2017; |
studies show that the extent of personalization is Agrawal, 2012) These biases are highly variable
oftenlimitedbythevolumeofcontextandinforma- and often depend on the age, experience and lo-
tionthatcanbesuppliedtoanagent,impactingthe
|     |     |     |     |     |     | cation of | the | user. Many | financial | agents | do not |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --------- | ------ | ------ |
overall performance. (Zhou et al., 2025; Winder directlyaddressthesebiaseswhenprovidingfinan-
| etal.,2024) |               |      |     |               |         | cialadvicetotheuser. |     |     | Inthisstudy,wehavetried |     |     |
| ----------- | ------------- | ---- | --- | ------------- | ------- | -------------------- | --- | --- | ----------------------- | --- | --- |
| One         | of the direct | ways | to  | address these | limita- |                      |     |     |                         |     |     |
tointegratethesebiasesintothereasoningmodel’s
tions is to tune a model with a domain-specific naturalchain-of-thoughttotunethefinalresponses
context that integrates financial, behavioral, and towards acknowledging and addressing these bi-
| psychologicalinformation. |     |     | Thisworkaimstoclose |     |     | ases. |     |     |     |     |     |
| ------------------------- | --- | --- | ------------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
thisgapbyprovidingareproducibleframeworkto
Eachstageofchain-of-thoughtgenerationisver-
generatefinancialadvicethroughawell-structured
ifiedbyasetofLargeLanguageModeljuriesthat
chain-of-thought. In particular, the framework rankvariousgenerationsandpickthebestversion
| constructs | supervision |     | data to | train models | to (a) |                            |     |     |     |                  |     |
| ---------- | ----------- | --- | ------- | ------------ | ------ | -------------------------- | --- | --- | --- | ---------------- | --- |
|            |             |     |         |              |        | suitablefortheuserqueries. |     |     |     | Weusedthisframe- |     |
providepersonalizedguidanceforusers’financial
|     |     |     |     |     |     | work to | generate | a 19k | sample | dataset, | which is |
| --- | --- | --- | --- | --- | --- | ------- | -------- | ----- | ------ | -------- | -------- |
dilemmas,(b)reliablyapplycorefinancialknowl- usedtofinetuneaQwen-3-8Bmodel. Thismodel
edge,and(c)recognizeandmitigateuser-sidebe-
isthencomparedtomodelsofsimilarsizestode-
havioralbiasesbyintegratingbehavioralandhis-
terminetheimpactofthisframework.
toricalevidence.
Thispaperintroducesaprincipled,data-centric
To address these limitations, we propose a framework as a step toward smaller, more trust-
| novel, | data-centric | framework |     | for synthesising |     |     |     |     |     |     |     |
| ------ | ------------ | --------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
worthypersonalfinanceLLMs,andweoutlineits
| behaviorally-grounded |     |     | reasoning | chains. | Rather |     |     |     |     |     |     |
| --------------------- | --- | --- | --------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
useasabackbonepolicywithinagenticworkflows
thanrelyingoncomplexagenticarchitectures,our
|     |     |     |     |     |     | to thin | planning | chains | and | lower orchestration |     |
| --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | --- | ------------------- | --- |
approachdirectlybakesfinancial,behavioural,and
cost—anevaluationwedefertofuturework.
psychologicalknowledgeintothetrainingdatait-
self. Crucially,wetreattheinferenceoftheuser’s 2 RelatedWorks
| psychological | state | not | as an | afterthought, | but as |     |     |     |     |     |     |
| ------------- | ----- | --- | ----- | ------------- | ------ | --- | --- | --- | --- | --- | --- |
astandalone,foundationalphaseinthereasoning The application of automated systems to finan-
chain. Thisdesignchoiceisdirectlymotivatedby cialadviceisnotanewundertaking. Priortothe
recent findings that users’ trust and engagement widespreadadoptionoflargelanguagemodels,re-
are heavily influenced by the persona of the ad- searchfocusedonapplyingclassictechniquessuch
visor (Takayanagi et al., 2025a), not just the raw ascollaborativefilteringandcase-basedreasoning
accuracy of its advice. By isolating and explic- towell-defineddomainssuchasloanandinsurance
168

policyrecommendation,assurveyedbyZibriczky as anchoring and overconfidence. Their crucial
(2016). However, the advent of powerful LLMs findingthatfine-tuningonfinancialdatacansome-
hasopenednewfrontiersandpresentedadistinct timesexacerbatetheseirrationaltendenciesunder-
setofchallengesandapproaches. scorestheprofoundrisksofusinguncurateddata.
Much of the recent literature has focused on Thisissupportedbyempiricalstudiesexposinga
benchmarkingthecapabilitiesofgeneral-purpose significant "product bias" in leading LLMs (Zhi
LLMsonarangeofisolatedfinancialtasks. Forin- etal.,2025)andbyfindingsthatLLM-generated
stance,acomprehensivestudybyHeanetal.(2025) advice systematically increases portfolio risk by
evaluated leading models such as ChatGPT and reinforcing investment biases such as geographi-
Claudeagainststandardizedfinancialliteracyques- calconcentrationandtrendchasing(Winderetal.,
tionnairescoveringdiversetopicsfrommortgages 2024). Takentogether,thesefindingsrevealthata
to taxes. While their findings show that newer model’spre-trainedknowledgeisanunreliableand
modelsareconsistentlyimprovingandcanachieve potentiallyriskyfoundationforfinancialadvice.
highaccuracyonspecifictopics, theyalsoreveal Therefore, our work addresses a critical gap.
significantlimitations,concludingthatLLMsstill While large-scale financial language models like
struggle to provide accurate responses for com- FinGPT,whichcontinuouslyingestreal-timemar-
plex financial queries. This highlights a critical ketdatatoupdateandadapttheunderlyingmodel
performance gap: off-the-shelf models are often (Yangetal.,2023;Wangetal.,2023;Zhangetal.,
insufficient for the nuanced demands of holistic 2023; Liu et al., 2023), have been proposed, our
financialadvice. approachdiffersfundamentallyinitscorecontribu-
To overcome the limitations of single models tion. Whereassuchworkfocusesonscalingmodel
and address more complex, multi-step planning, capacity and live data ingestion, our work intro-
asignificantbodyofresearchhasshiftedtowards duces a novel and reproducible methodology for
developingsophisticatedagenticworkflows. Are- creating the supervision data itself. By integrat-
centsurveybyDingetal.(2024)providesacom- ingtherelevantfinancialcontextwithbehavioral
prehensive overview of this landscape, categoriz- financestudies,weconstructahigh-qualityreason-
ing these systems into distinct architectural pat- ingdatasetdesignedtotrainsmaller,moreefficient
terns such as reflection-driven and debate-driven end-to-end advisors that are grounded in sound,
agents. AclearexampleistheworkofOkpalaetal. unbiasedprinciplesfromtheirinception.
(2025), who designed "agentic crews" composed
ofmultiplespecializedLLMagents,suchasdata 3 Datasetconstruction
scientists and compliance checkers, to automate
3.1 DataCollectionandProcessing
the entire financial modelling and risk manage-
mentpipeline. Whilepowerful,suchmulti-agent Our first step was to collect a large pool of real-
systemsdemonstratesignificantarchitecturalcom- world finance questions. Reddit (Reddit, [2025])
plexityandhighmaintenancecosts. Furthermore, proved ideal as a source of complex scenarios
research into these conversational agents has re- that span the breadth of personal finance do-
vealedsignificantrisks;Takayanagietal.(2025a) mains—from debt consolidation and retirement
foundinauserstudythatparticipantsoftenplaced planning to tax optimization and insurance deci-
moretrustinaconfident,"extroverted"agenteven sions. Theplatform’ssubreddits,particularlyr/per-
whenitprovidedlower-qualityadvice,highlighting sonalfinance,whichreceiveshundredsofthousands
thepotentialforthesecomplexsystemstomislead tomillionsofuserqueries,containauthenticscenar-
inexpertusers. iosthatcapturetheintricate,multi-facetednatureof
Weargue,however,thattheprimarybottleneck realfinancialdecision-making,providingthesce-
is not architectural complexity, but the inherent nariodiversityessentialfortrainingcomprehensive
irrationalityofthemodelsthemselves,necessitat- advisorymodels.
ing a data-centric approach. This need is rooted TocomplywithReddit’stermsandconditions,
in the tendency of LLMs to amplify human cog- weexclusivelyutilizedpubliclyavailablearchived
nitive biases. The groundbreaking work of Zhou datafrompostspriortoJune2023,ensuringallcol-
et al. (2025) introduced a comprehensive frame- lectedquerieswereethicallysourcedandproperly
workbasedonbehavioralfinancetodemonstrate de-identified.
thatLLMsexhibitsignificantfinancialbiases,such Afteringestion,wefilteredtherawcorpusintwo
169

Table1: Adetailedbreakdownofthedatasetgeneratedviaourproposedframework. Thistablepresentsthe
distributionofapproximately19ksamplesacrosseightdistinctcategoriesofpersonalfinance. Eachcategory
includeskeymetrics,suchastheaveragetokencountfortheinitialquery,thegeneratedchain-of-thought
delineatingthereasoningsteps,andthefinalanswer.
|          |     |     |             |     |     |     |       | Avg.   | Avg.   | Avg.     |
| -------- | --- | --- | ----------- | --- | --- | --- | ----- | ------ | ------ | -------- |
| Category |     |     | Description |     |     |     | Count | Query  | CoT    | Response |
|          |     |     |             |     |     |     |       | Tokens | Tokens | Tokens   |
DebtManagement&Credit Strategiesfordebtreduction(e.g.snow- 5175 215.76 628.30 393.69
|     |     |     | ball, | avalanche), credit-scoreimprove- |     |     |     |     |     |     |
| --- | --- | --- | ----- | -------------------------------- | --- | --- | --- | --- | --- | --- |
ment,andloananalysis.
RetirementPlanning Strategies,income-needsanalysis,bene- 3286 198.10 648.28 407.02
fitsoptimization(e.g.401(k),pensions)
andwithdrawalstrategies.
TaxPlanning&Optimization Tax-minimization strategies, under- 3019 182.96 630.20 397.81
|     |     |     | standing | deductions | and credits, | and |     |     |     |     |
| --- | --- | --- | -------- | ---------- | ------------ | --- | --- | --- | --- | --- |
investment-taximplications.
Investing&WealthBuilding Investmentstrategiesbasedonrisktol- 2994 200.16 653.54 402.98
erance,diversification,assetallocation,
andlong-termgrowth.
Budgeting&Cash-FlowManagement Creating budgets, tracking expenses, 2503 221.53 628.71 394.47
managingincomestreams,andimprov-
ingcashflow.
Insurance&RiskManagement Assessinginsuranceneeds(life,health, 1035 213.86 621.53 389.65
|     |     |     | property), | understanding | policies, | and |     |     |     |     |
| --- | --- | --- | ---------- | ------------- | --------- | --- | --- | --- | --- | --- |
managingfinancialrisks.
Savings&EmergencyFunds Strategiesforbuildingsavings,establish- 638 177.18 652.25 382.95
|     |     |     | ing | emergency funds, | and goal-based |     |     |     |     |     |
| --- | --- | --- | --- | ---------------- | -------------- | --- | --- | --- | --- | --- |
saving.
EstatePlanning&Legacy Wills,trusts,inheritanceconsiderations, 196 216.90 653.47 409.06
andminimisingestatetaxes(accounting
forregionalvariations).
| stages: |     |     |     |     | modular | approach | helps | us focus | on  | developing |
| ------- | --- | --- | --- | --- | ------- | -------- | ----- | -------- | --- | ---------- |
anindependentrubricforeachphasewhilegiving
| • Topical | validity  | – retained | posts | that con-    |             |           |     |               |     |            |
| --------- | --------- | ---------- | ----- | ------------ | ----------- | --------- | --- | ------------- | --- | ---------- |
|           |           |            |       |              | the ability | to stitch |     | them together | as  | a coherent |
| tained an | explicit, | answerable |       | personal fi- |             |           |     |               |     |            |
chain-of-thought.
| nance question                             |     | (e.g., budgeting, |     | credit, re- |       |               |     |     |     |     |
| ------------------------------------------ | --- | ----------------- | --- | ----------- | ----- | ------------- | --- | --- | --- | --- |
| tirement),discardinggenericnews,advertise- |     |                   |     |             | 3.2.1 | QueryAnalysis |     |     |     |     |
ments,oroff-topiccommentary.
Theissuewithnaturallanguageinquiriesisthepo-
tentialinconsistencyoftheinformationsuppliedto
| • Contextual    | clustering |           | – grouped | seman- |              |             |     |                |           |             |
| --------------- | ---------- | --------- | --------- | ------ | ------------ | ----------- | --- | -------------- | --------- | ----------- |
|                 |            |           |           |        | the model.   | There       | may | be significant |           | redundancy, |
| tically similar |            | posts and | removed   | near-  |              |             |     |                |           |             |
|                 |            |           |           |        | or essential | information |     | may            | be hidden | at times.   |
duplicatestoreducenoise.
Thus,theinitialstageofanswercreation,theques-
| Thispipelineyielded405kuniquequestions. |     |     |     | We  |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionanalysisphase,servesasafundamentalstepin
sampled19krepresentativequeriesthatspaneight
whichtheuser’squestionisdeconstructedintoits
| thematiccategories. | Table1containsthedetailed |     |     |     |                      |     |     |                           |     |     |
| ------------------- | ------------------------- | --- | --- | --- | -------------------- | --- | --- | ------------------------- | --- | --- |
|                     |                           |     |     |     | essentialcomponents. |     |     | Thisisrequiredtoascertain |     |     |
descriptionofthefinaldatasetgeneratedusingthe the (i) primary conflict from the user’s input; (ii)
| framework. Theentire405k-itemcorpusremains |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theprincipalplayersinthedilemma;and(iii)the
| availableforfuturescaling. |     | Detailsaboutprompt |     |     |                                             |     |     |     |     |      |
| -------------------------- | --- | ------------------ | --- | --- | ------------------------------------------- | --- | --- | --- | --- | ---- |
|                            |     |                    |     |     | essentialfinancialfactstoaddresstheinquiry. |     |     |     |     | This |
templates and specific instructions used in each facilitatestheoptimizationofsubsequentcognitive
phaseofthegenerationframeworkarepresentedin
processeswhileremainingalignedwiththeuser’s
AppendixA.1.
inquiry.
| 3.2 Generationmethodology |     |     |     |     | 3.2.2 | ContextAnalysis |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | ----- | --------------- | --- | --- | --- | --- |
Onahighlevel,thedatasetgenerationframework Contextanalysis(ModularRAG). Afterintent
canbedividedintotwoparts: (i)chain-of-thought parsing,weassembleacompactevidencepackvia
generationand(ii)responsegeneration. amodularRAGframework(Gaoetal.,2024)built
Ourchain-of-thoughtgenerationisdividedinto on two self-curated corpora snapshotted through
four major phases, as illustrated in Fig. 1. This February2025: (i)afinancialcorpusof∼600k
170

Figure1: Datasetgenerationpipeline. Fourmodularchain-of-thoughtphasesfeedintofinalresponsegeneration.
EachphaseincludesLLM-juryvalidation(notshown)toensurequality.
tokens—practical sources such as Investopedia evaluationoftheuser’sintent. Thisintentisutilized
and a Bogleheads snapshot (Investopedia, 2025; todirectthefinalresponseintoatonethatismost
Bogleheads, 2025) covering core concepts (e.g., suitablefortheuser,ratherthandirectlyproviding
retirement accounts, debt-repayment strategies), themamonotonousresponse.
pluscuratedsummariesofpolicychangesforma- Tooperatethecue-identificationatscale,andin
jorU.S.credit-cardproductsandotherconsumer- linewiththepriorstudieswhichdemonstratethat
policy/marketupdates; and(ii)abehavioralcor- state-of-the-artlargelanguagemodelsoutperform
pus of ∼300k tokens—research and practitioner human annotators in judgment tasks(Bojic´ et al.,
write-ups spanning psychology of risk, investor 2025; O’Leary, 2025), we adopt an LLM-based
behavior, behavioral portfolio theory, behavioral frameworkforcueidentificationsimilartotheother
asset pricing, psychological effects of debt, and stagesintheframework.
generationaldifferences.
3.2.4 ResponseFormulation
Candidate chunks are retrieved with
text-embeddings-3-large (OpenAI, 2025b) Thefinalphaseofthechain-of-thoughtisadistinct
(top-25), re-ranked with all-MiniLM-L12-v2 response formulation phase, in which we synthe-
(Sentence-Transformers, 2021), and the top-15 sizeasetofinstructions,consolidatinginformation
arecondensedbygemini-2.0-flash(Google,2025; fromallprecedingphases. Thisproducesasetof
Team et al., 2025a) to remove residual noise and directivesthatmustbeadheredtothroughoutthe
unify terminology. The streamlined context and response-generationphase.
theuserquerythenfeedthedownstreamreasoning
3.3 Responsegeneration
stage. FurtherdetailsareprovidedinAppendixB.
Aconclusiveresponseisformulatedtoaddressthe
3.2.3 PsychologicalCueidentification user’s inquiry, utilizing the previously optimized
Inparalleltocontextidentification,apsychological stagesofinformation. Thisconcludingcomment
cue identification module is run to identify cues isbasedonthefinancialcontextpresentedandis
fromthetext. Weextracttheoverallsentimentof articulatedinasuitabletonefortheuser.
the text, the primary emotions identifiable from
3.4 DataValidation
thechoiceofwordsinthequery,andthelevelof
certainty present in the information. Using these GiventhatvariousopenandproprietaryLLMsau-
cues,wetrytogeneralizeasetofcommunicative tomate numerous generations, there is a clear ne-
intents that might be behind the user’s query. By cessitytoassessandauthenticatetheiroutputs. We
breaking down the assessment into four distinct employedaseriesofjuries,specificallygemini-2.0-
categories, the process ensures a comprehensive flashando4-mini(OpenAI,2025a),toevaluateand
171

| rankvariousgenerationsforeachphase. |             |     |             |        | Eachjuror |          |     |       |     |            |     |        |
| ----------------------------------- | ----------- | --- | ----------- | ------ | --------- | -------- | --- | ----- | --- | ---------- | --- | ------ |
|                                     |             |     |             |        |           |          |     | Model |     | BERTScore↑ |     | BLEURT |
| assessed                            | the created |     | information | within |           | a three- |     |       |     |            |     |        |
Gemma3-27B-IT
shotevaluationframework,ultimatelyselectingthe
|     |     |     |     |     |     |     |     |     |     |     | 0.7142 | 0.4374 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ |
(Teametal.,2025b)
highest-rankedresponseforsubsequentgeneration
| jobs. |     |     |     |     |     |     | Gemma3-12B-IT |     |     |     | 0.7139 | 0.4390 |
| ----- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | ------ | ------ |
Mistral-24B-2501
|              |     |     |     |     |     |     |                   |     |     |     | 0.7133 | 0.4464 |
| ------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | ------ | ------ |
| 4 Evaluation |     |     |     |     |     |     | (MistralAI,2025b) |     |     |     |        |        |
QWQ-32B(Qwen,2025)
| Totestwhetherourdatasetenablespracticaldeci- |     |     |     |     |     |     |     |     |     |     | 0.7069 | 0.4452 |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ |
(reasoning)
sionsupport,wefine-tuneQwen-3-8B(Yangetal.,
2025)forfiveepochsandcompareitwithbaselines DeepSeek-Qwen-14B
| ofsimilarsize. |     |     |     |     |     |     | (reasoning) |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
Weperformanadditionalassessmentoftheper- (DeepSeekAI,2025) 0.7069 0.4513
formanceusingtwoseparateheld-outdatasets. We Ours(8B) 0.7000 0.4600
employthesemethodstoassessthequalityofthe
|                                                |     |     |     |     |     |     | Llama-38B(Meta, |     |     |     | 0.6881 | 0.4547 |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ------ | ------ |
| responsesthroughbothquantitativeandqualitative |     |     |     |     |     |     | 2024)           |     |     |     |        |        |
| measures.                                      |     |     |     |     |     |     | Mistral-7Bv0.3  |     |     |     | 0.6650 | 0.4501 |
(MistralAI,2025a)
4.1 QuantitativeEvaluation
Toassessthequantitativeperformanceofthemod- Table2: Automaticevaluationonthe500-querytestset.
els, we utilize a held-out dataset comprising 500 Boldmarksthebestscoreineachcolumn;higheris
| distinct      | queries                       | across | various | categories |     | of per- | better. |     |     |     |     |     |
| ------------- | ----------------------------- | ------ | ------- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- |
| sonalfinance. | Groundtruthswereproducedbythe |        |         |            |     |         |         |     |     |     |     |     |
generationframeworkpresentedinSection3.2(not
|     |     |     |     |     |     |     | default | inference | settings | to  | get their | best perfor- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | -------- | --- | --------- | ------------ |
thefine-tunedmodel)priortotrainingandvalidated
|                      |     |     |                          |     |     |     | mance. | This | setup allows | us  | to evaluate | whether |
| -------------------- | --- | --- | ------------------------ | --- | --- | --- | ------ | ---- | ------------ | --- | ----------- | ------- |
| byindependentjurors. |     |     | Followingtheground-truth |     |     |     |        |      |              |     |             |         |
ourfine-tunedmodelhasmerelylearnedtomimic
| generation,   | we      | calculate | the                  | BERTScore |     | (Zhang |              |               |     |           |              |              |
| ------------- | ------- | --------- | -------------------- | --------- | --- | ------ | ------------ | ------------- | --- | --------- | ------------ | ------------ |
|               |         |           |                      |           |     |        | the training | data          | or  | if it has | successfully | internal-    |
| et al., 2020) | using   | the       | Qwen-3-8B-embeddings |           |     |        |              |               |     |           |              |              |
|               |         |           |                      |           |     |        | ized a       | generalizable |     | framework | for          | the response |
| (Zhang        | et al., | 2025)     | model                | to assess | the | seman- |              |               |     |           |              |              |
generationthatcanbeappliedtonoveluserprob-
| tic accuracy | of  | the responses. |     | We  | also calculate |     |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
lems.
theBLEURT(Sellametal.,2020)scoretoassess
the fluency (or) human-likeness of the responses, To mitigate familial bias and leakage, we ex-
cludedjudgesfrommodelfamiliesusedanywhere
| respectively. | The      | quantitative |            | scores | of       | various |                                             |     |                               |     |     |     |
| ------------- | -------- | ------------ | ---------- | ------ | -------- | ------- | ------------------------------------------- | --- | ----------------------------- | --- | --- | --- |
|               |          |              |            |        |          |         | inourpipeline.                              |     | Inparticular,Geminimodelswere |     |     |     |
| models        | utilized | in this      | evaluation | are    | detailed | in      |                                             |     |                               |     |     |     |
| Table2.       |          |              |            |        |          |         | omittedbecausetheywereusedduringdatasetgen- |     |                               |     |     |     |
eration/validation,andQwen-familyjudgeswere
Our8Bmodelachievessemanticaccuracycom-
omittedbecausethesystemundertestisQwen-8B.
| parable | to leading | baselines, |     | including | Gemma3- |     |     |     |     |     |     |     |
| ------- | ---------- | ---------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
27B/12BandMistral-24B.Inparticular,ourmodel Afewotherwisesuitablejudgeswerealsoexcluded
surpasses these larger models by approximately for cost reasons. The final judge pool comprises
modelsfromunrelatedfamilies;noneoverlapped
| 3–5% in | human-likeness |     | and | fluency. | This | indi- |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | -------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
withtrainingordata-creationcomponents.
| cates a reduced |     | deviation | from | ground-truth |     | data |     |     |     |     |     |     |
| --------------- | --- | --------- | ---- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- |
andenhancedfluencysignalscomparedtomodels For each query, every judge sees all k
| twiceitssize. |     |     |     |     |     |     | anonymizedcandidatessimultaneously(noground |        |       |             |     |                |
| ------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | ------ | ----- | ----------- | --- | -------------- |
|               |     |     |     |     |     |     | truth                                       | and no | model | identities) | and | returns a full |
4.2 QualitativeEvaluation
ranking;candidateorderisuniformlyrandomized
Tocomplementreference-basedmetricsand,criti- per replicate. We use two main judges, namely
cally,toassessthemodel’sgeneralizationcapabili- DeepSeek-V3-0324(DeepSeek-AIetal.,2025)and
ties,werunalist-wiseblindLLM-juryrankingon Kimi-k2 (AI, 2025). Kimi-k2 is run three times,
504queriesthatwereentirelyheldoutandunseen and DeepSeek-v3-0324 is run five times on inde-
duringthetrainingphase. Thesetestquerieswere pendently shuffled anonymized candidate orders
collectedfromasubsequenttimeperiodtoensure for each query to reduce possible biases. These
nodatacontamination. Meanwhile,allthecandi- judgeswerechoseninordertoavoidsame-family
dateswerezero-shotgeneratedintheirrespective biasprevalentinmodernLLM-judgestudies.
172

Table3: Rankcorrelationsbetweenjudgesets(higheris
better). τ measureshowoftenthejudgesagreewithA>
B,andρmeasureshowcloselythefullrankliststrack.
| Metric        |          | Kendall’sτ |           | Spearman’sρ |        |        |          |                                        |     |     |     |     |     |
| ------------- | -------- | ---------- | --------- | ----------- | ------ | ------ | -------- | -------------------------------------- | --- | --- | --- | --- | --- |
| Plausibility  |          | 0.6183     |           |             | 0.7711 |        |          |                                        |     |     |     |     |     |
| Accuracy      |          | 0.6183     |           |             | 0.7635 |        |          |                                        |     |     |     |     |     |
| Relevance     |          | 0.6910     |           |             | 0.8264 |        |          |                                        |     |     |     |     |     |
| Overall       |          | 0.6429     |           |             | 0.7904 |        |          |                                        |     |     |     |     |     |
| The           | rankings | are        | converted |             | to     | Borda  |          |                                        |     |     |     |     |     |
| points(Saari, |          | 2023) and  | averaged  |             | across | judges |          |                                        |     |     |     |     |     |
|               |          |            |           |             |        |        | Figure2: | LLM-juryevaluationon504unseensubreddit |     |     |     |     |     |
and replicates to obtain the representative score queries: stackedbarsshowBorda-averagescoresfor
accuracy(blue),plausibility(orange),andrelevance
| ofaresponse. |     | Wereceivetherankingjudgments |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accordingtothreecriteria,namelytheirfinancial (green);tallerbarsindicatestrongeroverallpreference.
Our8Bsystem(fourthfromleft)outperformsallother
| accuracy, | plausibility, |     | and relevance |     | to the | query, |     |     |     |     |     |     |     |
| --------- | ------------- | --- | ------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
sub-14Bmodelsandapproachesthe27B–32B
| and report | the      | aggregate | Borda        | scores | in  | Fig.2.   |          |                                          |     |     |     |     |     |
| ---------- | -------- | --------- | ------------ | ------ | --- | -------- | -------- | ---------------------------------------- | --- | --- | --- | --- | --- |
|            |          |           |              |        |     |          | leaders. | They-axisrepresentstheaverageBordapoints |     |     |     |     |     |
| Whereas    | Appendix |           | C.1 presents |        | the | in-depth |          |                                          |     |     |     |     |     |
amodelhasreceived.
analysisoftheevaluationresults.
Toexaminerankconsistencybetweenthejudge
sets, we compute Kendall’s τ and Spearman’s ρ user constraints even when containing factual er-
| overper-querymodelranks. |     |     |     | Kendall’sτ |     | assesses |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
rorsorpoorreasoning.
pairwiseorderagreement(dobothjudgesprioritize
|                      |     |     |     |                     |     |     | Strengths.      | The | model     | consistently |       | produces |     |
| -------------------- | --- | --- | --- | ------------------- | --- | --- | --------------- | --- | --------- | ------------ | ----- | -------- | --- |
| modelAabovemodelB?). |     |     |     | Spearman’sρassesses |     |     |                 |     |           |              |       |          |     |
|                      |     |     |     |                     |     |     | well-structured |     | responses | with         | clear | headers, | se- |
how closely the complete ranked lists move to- quentialactionsteps,andappropriateempathetic
| gether     | and penalizes |               | significant | rank  | differences. |     |          |             |          |               |     |     |         |
| ---------- | ------------- | ------------- | ----------- | ----- | ------------ | --- | -------- | ----------- | -------- | ------------- | --- | --- | ------- |
|            |               |               |             |       |              |     | framing. | It reliably | extracts | user-specific |     |     | details |
| We observe |               | τ ≈ 0.62-0.69 |             | and ρ | ≈ 0.76-0.83  |     |          |             |          |               |     |     |         |
(monetaryamounts,timelines,constraints)andin-
(overallτ = 0.64,ρ = 0.79),indicatingsubstantial corporates them into tailored advice. Responses
| agreement. | Theconsistentlyhigherρthanτ |     |     |     |     | sug- |           |             |     |           |         |     |        |
| ---------- | --------------------------- | --- | --- | --- | --- | ---- | --------- | ----------- | --- | --------- | ------- | --- | ------ |
|            |                             |     |     |     |     |      | typically | acknowledge |     | emotional | context |     | before |
gestsdisagreementsaremostlylocalswapsrather
|                |     |              |     |           |     |        | providing | practical | guidance—a |     | pattern | that | en- |
| -------------- | --- | ------------ | --- | --------- | --- | ------ | --------- | --------- | ---------- | --- | ------- | ---- | --- |
| than wholesale |     | reorderings. |     | Relevance |     | demon- |           |           |            |     |         |      |     |
hancesperceivedhelpfulness.
| strates | the strongest |     | alignment            | (τ  | = 0.691, | ρ = |               |     |                             |     |     |     |     |
| ------- | ------------- | --- | -------------------- | --- | -------- | --- | ------------- | --- | --------------------------- | --- | --- | --- | --- |
|         |               |     |                      |     |          |     | FailureModes. |     | Theprimaryweaknessisfactual |     |     |     |     |
| 0.826). | Table3showsτ  |     | andρforeachmetricand |     |          |     |               |     |                             |     |     |     |     |
hallucination,particularlyforjurisdiction-specific
overall.
|     |     |     |     |     |     |     | regulations | and | tax details. | The | model | occasion- |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ----- | --------- | --- |
Ourexperimentalresultsdemonstratethatawell-
|     |     |     |     |     |     |     | ally generates | plausible-sounding |     |     |     | but incorrect |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------ | --- | --- | --- | ------------- | --- |
curated,behavior-tunedfinancedatasetcanelevate
|            |       |     |         |             |     |        | specifics          | (e.g., non-existent |                            | grant | programs, |     | out- |
| ---------- | ----- | --- | ------- | ----------- | --- | ------ | ------------------ | ------------------- | -------------------------- | ----- | --------- | --- | ---- |
| an 8B open | model | to  | achieve | performance |     | parity |                    |                     |                            |       |           |     |      |
|            |       |     |         |             |     |        | datedtaxbrackets). |                     | Theseerrorsaremostfrequent |       |           |     |      |
withmodelstwotothreetimesitssize,thusvalidat-
inregulation-heavydomains(taxes,insurance)and
| ingthepracticalutilityofourframework. |     |     |     |     |     | Details |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
leastcommoningeneralplanningtasks(budgeting,
| abouttheentiretrainingenvironmentandsettings |     |     |     |     |     |     | debtmanagement). |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
arepresentedinAppendixD.
|     |     |     |     |     |     |     | Implications. |                | Whilethemodelmaintainsstrong |           |     |        |         |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | ---------------------------- | --------- | --- | ------ | ------- |
|     |     |     |     |     |     |     | structural    | and empathetic |                              | qualities |     | across | all re- |
4.3 QualitativeAnalysisandErrorPatterns
sponses,factualgroundingremainsthekeybottle-
Analysisofthe504held-outresponsesrevealscon- neck. Thissuggeststhataddingtargetedretrieval
sistentpatternsacrossthethreeevaluationdimen- forregulatoryinformationandcalculationverifica-
sions. Whenmodelsproduceinaccurateresponses, tionwouldyieldthehighestmarginalimprovement.
theytypicallyalsoexhibitdegradedreasoningqual- Evenwithcurrentlimitations,themodel’sconsis-
ity—accuracy and plausibility failures often co- tent task alignment and user-responsive framing
occur. However,relevanceremainsrelativelyinde- provide practical utility for non-critical advisory
| pendent;responsescanstayon-topicandaddress |     |     |     |     |     |     | scenarios. |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
173

4.4 CostAnalysis advice generation as an alignment problem, test-
ingpreference-basedoptimization(e.g.,DPO/IPO)
| Beyond        | performance     | metrics, | practical      | deploy- |                                |         |               |            |               |           |      |
| ------------- | --------------- | -------- | -------------- | ------- | ------------------------------ | ------- | ------------- | ---------- | ------------- | --------- | ---- |
|               |                 |          |                |         | to refine                      | outputs | and deploying |            | rule-based    |           | com- |
| ment requires | careful         | cost     | consideration. | Table   |                                |         |               |            |               |           |      |
|               |                 |          |                |         | pliance layers                 | to      | enforce       | regulatory |               | fidelity, | bias |
| 4 presents    | a comprehensive |          | cost analysis  | of the  |                                |         |               |            |               |           |      |
|               |                 |          |                |         | mitigation,andtoneconsistency. |         |               |            | Successwillbe |           |      |
modelproducedbyourframeworkagainstseveral
|     |     |     |     |     | quantified | through | targeted | evaluations |     | of  | safety, |
| --- | --- | --- | --- | --- | ---------- | ------- | -------- | ----------- | --- | --- | ------- |
baselines,comparinghostinginfrastructure,infer-
complianceadherence,andusertrustmetrics.
encelatency,andtotaloperationalexpenses.
Ourdata-centricapproachdeliversexceptional
6 Conclusion
| costefficiencyinthepersonalfinancedomain. |     |     |     | By  |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
enabling a compact 8B model to achieve perfor- Ourresearchestablishesadata-centricframework
mancecompetitivewithmuchlargersystems,our thatenablesan8B-parametermodeltoachievese-
methodfacilitatesatleastan80%reductioninop- mantic fidelity and human-likeness on par with,
| erational | costs when | compared | to baselines | with |     |     |     |     |     |     |     |
| --------- | ---------- | -------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
andsometimesexceeding,27–32Bbaselinesinour
over 12B parameters. This dramatic cost reduc- held-outevaluationsandblindLLM-jurystudy. On
tionstemsfromtargetedbehavioralintegrationand a500-querytest,themodeloutperformsGemma3-
principleddataconstruction,ratherthansheercom-
|                  |     |     |     |     | 27B by              | 5% on | BLEURT | and                    | is competitive |     | on  |
| ---------------- | --- | --- | --- | --- | ------------------- | ----- | ------ | ---------------------- | -------------- | --- | --- |
| putationalscale. |     |     |     |     | BERTScore,withonlya |       |        | 2%difference;juryrank- |                |     |     |
Theefficiencytranslatestopracticaldeployment ingsshowthe8Bsystemapproachingthe27–32B
advantages: at a hosting cost of $0.8 per hour leaders. These gains stem from three synergistic
and an average inference time of 34.15 seconds, components: explicitpsychologicalcues,retrieval-
our model enables responsive financial advisory augmented grounding, and a thin agentic execu-
serviceswithoutprohibitiveinfrastructurerequire- tionlayer. Themodulardesignsupportsincremen-
ments. Theseresultsvalidatetheeffectivenessof talextension(e.g.,regionalexpertswithminimal
ournoveldatagenerationframework. Theydemon- retraining). While geographic scope, behavioral
strate that by carefully integrating financial and depth,andprivacysafeguardsremainlimitations,
behavioralsignalsintotrainingdata,itispossible thisworkoffersacost-awarebackboneforstand-
tocreatecompetent,domain-specificmodelsthat alonepersonal-financeassistantsandaviablealter-
arealsoeconomicallyviable. Thispresentsacom- nativetomonolithicclouddeployments—leaving
pellingapproachfordevelopingproduction-ready aprecisecost/latencyaudittofuturework.
financialadvisorytoolsthatdonotrelysolelyon
| expensive,large-scalemodels. |     |     |     |     | Limitations |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Severalaspectsofourworkleaveroomforfuture
5 FutureWorks
|     |     |     |     |     | improvements. |     | First, | our study | is  | limited | to in- |
| --- | --- | --- | --- | --- | ------------- | --- | ------ | --------- | --- | ------- | ------ |
We will advance this research by first determin- quiries sourced solely from Reddit, which may
ing the optimal path for global scaling: either fi- overlook other demographics and query formats,
nalizing a US-optimized pipeline for systematic suggesting a need for more diverse data sources.
market porting or—contingent on high-precision Second,our19ksampledataset,thoughsufficient
detection of regional signals (e.g., currency sym- forproof-of-concept,lacksthescaleanddiversity
bols, policy terminology, and spelling conven- needed to cover the full spectrum of real-world
tions)—implementingaMixture-of-Experts(MoE) personalfinancescenarios. Futureworkshouldex-
framework. In the latter case, a shared backbone pandthecorpuswithvariedsourcesbeyondReddit
modelwillprocessuniversalfinanciallogicwhile to improve generalization. Third, our psycholog-
lightweight regional experts handle localized nu- ical analysis remains rudimentary, deriving only
ances. Thiscoremodelwilldeployasabackbone basicsentimentfromphrasesratherthanincorpo-
policywithinathinagenticstack, minimizingla- ratingenhancedpsychologicalindicatorssuchas
tencyandcostbyresolvingqueriesinternallyand risktoleranceorfinancialstressthroughspecialized
invokingexternaltools(e.g.,regulatorydatabases surveysortransferlearningfromclinicaldatasets.
or fact-checking APIs) only for uncertainty reso- Finally,ourframework’sscopeexcludestasksbe-
lution. Wewillrigorouslymeasureresultingcost- yondcorenaturallanguageprocessing,particularly
latencytrade-offsacrossregions. Ratherthanaddi- multi-modal data processing and reasoning capa-
tionalsupervisedfine-tuning,wewilltreatfinancial bilities, which represent critical areas for future
174

Table4: CostandInferencePerformanceAnalysisforDeployment. Totalcostsreflecttheexpensetoinfer504
queriesfromthetestset,witheachmodelbenchmarkedusingfourconcurrentrequests.
Model Size(GB) EndpointCost GPU InferenceTime TotalTime TotalCost
|                    |     |      |     | ($/h) |                       |     | (s/query) |     |     | (h)  | ($)   |
| ------------------ | --- | ---- | --- | ----- | --------------------- | --- | --------- | --- | --- | ---- | ----- |
| QWQ-32B            |     | 65.0 |     | 3.8   | 4xL4                  |     | 167.86    |     |     | 5.82 | 22.33 |
| Gemma3-27B         |     | 46.4 |     | 2.5   | 1xA100                |     | 64.34     |     |     | 2.23 | 5.63  |
| Gemma3-12B         |     | 20.0 |     | 1.8   | 1xL40S                |     | 58.26     |     |     | 2.02 | 3.67  |
| Ours(8B)           |     | 16.4 |     | 0.8   | 1xL4                  |     | 34.15     |     |     | 1.19 | 0.96  |
| Mistral-24B-2501   |     | 46.1 |     | 3.8   | 1xA100                |     | 37.99     |     |     | 1.32 | 5.05  |
| DeepSeek-Qwen-14B  |     | 29.5 |     | 1.8   | 1xL40S                |     | 54.18     |     |     | 1.88 | 3.41  |
| Llama3-8B          |     | 16.1 |     | 0.8   | 1xL4                  |     | 33.58     |     |     | 1.17 | 0.94  |
| Mistral-7B         |     | 14.5 |     | 0.8   | 1xL4                  |     | 29.15     |     |     | 1.01 | 0.82  |
| researchexpansion. |     |      |     |       | EthicalConsiderations |     |           |     |     |      |       |
Acknowledgements We curate data from publicly available Reddit
|                |                    |               |     |          | posts and            | aggressively |       | de-identify |          | them:      | user-  |
| -------------- | ------------------ | ------------- | --- | -------- | -------------------- | ------------ | ----- | ----------- | -------- | ---------- | ------ |
| I want to      | express my sincere | gratitude     |     | to Raghu |                      |              |       |             |          |            |        |
|                |                    |               |     |          | names/links/metadata |              |       | are         | removed, | PII        | (e.g., |
| Ram Theerthala | (KPIT              | Technologies) |     | for his  |                      |              |       |             |          |            |        |
|                |                    |               |     |          | names,               | emails,      | phone | numbers,    |          | addresses, | IDs)   |
valuablecontributionstotherelatedworkssection
|     |     |     |     |     | is scrubbed, | and | queries | are | lightly | rephrased | so  |
| --- | --- | --- | --- | --- | ------------ | --- | ------- | --- | ------- | --------- | --- |
andinsightfuldiscussionsduringthebrainstorming
onlythefinancialsituationremains;norawidenti-
| sessionsthathelpedshapethisresearch. |     |     |              | Iamgrate- |           |        |              |     |     |           |         |
| ------------------------------------ | --- | --- | ------------ | --------- | --------- | ------ | ------------ | --- | --- | --------- | ------- |
|                                      |     |     |              |           | fiers are | stored | or released. |     | The | system is | for ed- |
| fultoPrathyushaAkundi,SyedMd.        |     |     | Bilal,Ashish |           |           |        |              |     |     |           |         |
ucationaluseonly—notfiduciaryorpersonalized
Kubade,andSaiNarayanfortheircarefulreview
financialadvice—andourprompts/filtersforbidun-
| of the manuscript | and | constructive | feedback | that |     |     |     |     |     |     |     |
| ----------------- | --- | ------------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
safeguidance(e.g.,evasion,“guaranteedreturns”).
| improvedtheclarityandqualityofthiswork. |           |            |          | This |            |      |          |     |             |     |        |
| --------------------------------------- | --------- | ---------- | -------- | ---- | ---------- | ---- | -------- | --- | ----------- | --- | ------ |
|                                         |           |            |          |      | Evaluation | uses | multiple |     | LLM judges; | we  | report |
| research was                            | supported | by Perfios | Software | So-  |            |      |          |     |             |     |        |
inter-judgeagreementandrunjudge-swapchecks
lutions,whichsponsoredthecomputationalcosts
tolimitmodel-familybias.
andinfrastructurerequiredformodeltrainingand
evaluation.
References
Data&CodeAvailability
|     |     |     |     |     | RohitAggarwalandHarpreetSingh.2024. |     |     |     |     | Overcoming |     |
| --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | ---------- | --- |
The dataset, model, and code artifacts described limitationsofaiagents: Integratingtacitknowledge
in this paper are publicly available on Hugging throughinferredlatent themes. Availableat SSRN
4843878.
| Face. All | data has been | de-identified |     | following |     |     |     |     |     |     |     |
| --------- | ------------- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
theethicalguidelinesdescribedinSection6,with KhushbuAgrawal.2012. Aconceptualframeworkof
personallyidentifiableinformationremovedfrom behavioralbiasesinfinance. IUPJournalofBehav-
ioralFinance.
| Redditsources. | Theresourcesarereleasedunder |     |     |     |     |     |     |     |     |     |     |
| -------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theApache2.0licensetofacilitatereproducibility Moonshot AI. 2025. Kimi-k2-instruct (revision
| andfutureresearchinbehavioralfinanceandLLM |     |     |     |     | 2f7e011). |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
applications.
HKentBaker,GregFilbeck,andVictorRicciardi.2017.
Thefollowingresourcesareavailable:
Howbehaviouralbiasesaffectfinanceprofessionals.
• Model: Fine-tunedQwen-3-8Bmodelat TheEuropeanFinancialReview,pages25–29.
https://huggingface.co/
|                                      |     |     |     |     | Bogleheads.        | 2025. | Bogleheads |     | - investing | advice | in- |
| ------------------------------------ | --- | --- | --- | --- | ------------------ | ----- | ---------- | --- | ----------- | ------ | --- |
| Akhil-Theerthala/Kuvera-8B-qwen3-v0. |     |     |     |     | spiredbyjohnbogle. |       |            |     |             |        |     |
2.1
|            |                             |     |     |     | Ljubiša       | Bojic´, | Olga  | Zagovora,     | Asta  | Zelenkauskaite,   |     |
| ---------- | --------------------------- | --- | --- | --- | ------------- | ------- | ----- | ------------- | ----- | ----------------- | --- |
|            |                             |     |     |     | Vuk Vukovic´, |         | Milan | Cˇabarkapa,   |       | Selma Veseljevic´ |     |
| • Dataset: | 19ksamplereasoningdatasetat |     |     |     |               |         |       |               |       |                   |     |
|            |                             |     |     |     | Jerkovic´,    | and     | Ana   | Jovancˇevic´. | 2025. | Comparing         |     |
https://huggingface.co/
largelanguagemodelsandhumanannotatorsinla-
datasets/Akhil-Theerthala/
tentcontentanalysisofsentiment,politicalleaning,
Kuvera-PersonalFinance-V2.1 emotionalintensityandsarcasm. naturebriefing.
175

MertCemri,MelissaZ.Pan,ShuyiYang,LakshyaA. KausikLakkaraju,SaraEJones,SaiKrishnaRevanth
Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Vuruma,VishalPallagani,BharathCMuppasani,and
Keutzer,AdityaParameswaran,DanKlein,Kannan BiplavSrivastava.2023. Llmsforfinancialadvise-
Ramchandran, MateiZaharia, JosephE.Gonzalez, ment: Afairnessandefficacystudyinpersonalde-
andIonStoica.2025. Whydomulti-agentllmsys- cisionmaking. InProceedingsoftheFourthACM
temsfail? Preprint,arXiv:2503.13657. InternationalConferenceonAIinFinance, ICAIF
’23,page100–107,NewYork,NY,USA.Association
DeepSeek-AI,AixinLiu,BeiFeng,BingXue,Bingx- forComputingMachinery.
| uan Wang, | Bochao |     | Wu, Chengda |     | Lu, Chenggang |     |     |     |     |     |     |     |     |
| --------- | ------ | --- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Zhao,ChengqiDeng,ChenyuZhang,ChongRuan, MeisinLeeandSoonLay-Ki.2024. ’financewizard’at
Damai Dai, Daya Guo, Dejian Yang, Deli Chen, thefinllmchallengetask: Financialtextsummariza-
Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, tion. Preprint,arXiv:2408.03762.
| and181others.2025. |     |     | Deepseek-v3technicalreport. |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Preprint,arXiv:2412.19437.
JinzhengLi,JingshuZhang,HongguangLi,andYiqing
|     |     |     |     |     |     |     | Shen. | 2024. | An agent | framework | for | real-time | fi- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | -------- | --------- | --- | --------- | --- |
DeepSeekAI. 2025. deepseek-ai/deepseek-r1-distill- nancial information searching with large language
| qwen-14b. |     |     |     |     |     |     | models. | Preprint,arXiv:2502.15684. |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------- | -------------------------- | --- | --- | --- | --- | --- |
HanDing,YinhengLi,JunhaoWang,andHangChen.
Xiao-YangLiu,GuoxuanWang,HongyangYang,and
2024. Largelanguagemodelagentinfinancialtrad-
|     |     |     |     |     |     |     | DaochenZha.2023. |     |     | Data-centricfingpt: |     | Democra- |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ------------------- | --- | -------- | --- |
ing: Asurvey. Preprint,arXiv:2408.06361. tizinginternet-scaledataforfinanciallargelanguage
|             |     |        |      |       |     |        | models. | NeurIPSWorkshoponInstructionTuning |     |     |     |     |     |
| ----------- | --- | ------ | ---- | ----- | --- | ------ | ------- | ---------------------------------- | --- | --- | --- | --- | --- |
| Yunfan Gao, | Yun | Xiong, | Meng | Wang, | and | Haofen |         |                                    |     |     |     |     |     |
andInstructionFollowing.
| Wang.2024.                             |     | Modularrag:Transformingragsystems |     |     |     |           |         |          |      |        |               |     |       |
| -------------------------------------- | --- | --------------------------------- | --- | --- | --- | --------- | ------- | -------- | ---- | ------ | ------------- | --- | ----- |
| intolego-likereconfigurableframeworks. |     |                                   |     |     |     | Preprint, |         |          |      |        |               |     |       |
|                                        |     |                                   |     |     |     |           | Zhaowei | Liu, Xin | Guo, | Fangqi | Lou, Lingfeng |     | Zeng, |
arXiv:2407.21059. Jinyi Niu, Zixuan Wang, Jiajie Xu, Weige Cai, Zi-
weiYang,XueqianZhao,ChaoLi,ShengXu,Dezhi
| Google. | 2025. | Gemini | 2.0 flash. |     | https://cloud. |     |     |     |     |     |     |     |     |
| ------- | ----- | ------ | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Chen,YunChen,ZuoBai,andLiwenZhang.2025.
google.com/vertex-ai/generative-ai/docs/
|     |     |     |     |     |     |     | Fin-r1: | A large | language |     | model for | financial | rea- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | -------- | --- | --------- | --------- | ---- |
model-reference/inference.
|     |     |     |     |     |     |     | soning | through | reinforcement |     | learning. | Preprint, |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------------- | --- | --------- | --------- | --- |
arXiv:2503.16252.
AlmogGueta,AmirFeder,ZorikGekhman,ArielGold-
| stein,andRoiReichart.2025. |            |     |             | Canllmslearnmacroe- |     |           |          |            |      |       |          |           |     |
| -------------------------- | ---------- | --- | ----------- | ------------------- | --- | --------- | -------- | ---------- | ---- | ----- | -------- | --------- | --- |
|                            |            |     |             |                     |     |           | Zian Liu | and Renjun | Jia. | 2025. | Llm4fts: | Enhancing |     |
| conomic                    | narratives |     | from social | media?              |     | Preprint, |          |            |      |       |          |           |     |
largelanguagemodelsforfinancialtimeseriespre-
arXiv:2406.12109.
|             |       |               |     |           |     |       | diction. | Preprint,arXiv:2505.02880. |     |     |     |     |     |
| ----------- | ----- | ------------- | --- | --------- | --- | ----- | -------- | -------------------------- | --- | --- | --- | --- | --- |
| Udit Gupta. | 2023. | Gpt-investar: |     | Enhancing |     | stock |          |                            |     |     |     |     |     |
YichenLuo,YeboFeng,JiahuaXu,PaoloTasca,and
| investment | strategies |          | through | annual | report | analy-   |                                        |     |             |     |                   |     |       |
| ---------- | ---------- | -------- | ------- | ------ | ------ | -------- | -------------------------------------- | --- | ----------- | --- | ----------------- | --- | ----- |
|            |            |          |         |        |        |          | Yang Liu.2025.                         |     | Llm-powered |     | multi-agentsystem |     |       |
| sis with   | large      | language | models. |        | arXiv  | preprint |                                        |     |             |     |                   |     |       |
|            |            |          |         |        |        |          | forautomatedcryptoportfoliomanagement. |     |             |     |                   |     | arXiv |
arXiv:2309.03079.
preprintarXiv:2501.00826.
XuewenHan,NengWang,ShangkunChe,Hongyang
|                                        |            |        |           |      |            |           | Glenn Matlin, |       | Mika Okamoto, |     | Huzaifa      | Pardawala, |     |
| -------------------------------------- | ---------- | ------ | --------- | ---- | ---------- | --------- | ------------- | ----- | ------------- | --- | ------------ | ---------- | --- |
| Yang,                                  | Kunpeng    | Zhang, | and       | Sean | Xin        | Xu. 2024. |               |       |               |     |              |            |     |
|                                        |            |        |           |      |            |           | Yang Yang,    |       | and Sudheer   |     | Chava. 2025. | Finance    |     |
| Enhancing                              | investment |        | analysis: |      | Optimizing | ai-       |               |       |               |     |              |            |     |
|                                        |            |        |           |      |            |           | language      | model | evaluation    |     | (flame).     | Preprint,  |     |
| agentcollaborationinfinancialresearch. |            |        |           |      |            | Preprint, |               |       |               |     |              |            |     |
arXiv:2506.15846.
arXiv:2411.04788.
|                                         |     |     |     |     |             |     | Kiana Jafari       | Meimandi, |      | Gabriela                  | Aránguiz-Dias, |           |     |
| --------------------------------------- | --- | --- | --- | --- | ----------- | --- | ------------------ | --------- | ---- | ------------------------- | -------------- | --------- | --- |
| OudomHean,UtshaSaha,andBinitaSaha.2025. |     |     |     |     |             | Can |                    |           |      |                           |                |           |     |
|                                         |     |     |     |     |             |     | Grace              | Ra Kim,   | Lana | Saadeddin,                |                | and Mykel | J.  |
| aihelpwithyourpersonalfinances?         |     |     |     |     | AppliedEco- |     |                    |           |      |                           |                |           |     |
| nomics,page1–9.                         |     |     |     |     |             |     | Kochenderfer.2025. |           |      | Themeasurementimbalancein |                |           |     |
agenticaievaluationunderminesindustryproductiv-
|     |     |     |     |     |     |     | ityclaims. | Preprint,arXiv:2506.02064. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------------------- | --- | --- | --- | --- | --- |
ZengyiHuang,ChangChe,HaotianZheng,andChenLi.
2024. Researchongenerativeartificialintelligence
forvirtualfinancialrobo-advisor. AcademicJournal Meta.2024. meta-llama/llama-3.1-8b-instruct.
ofScienceandTechnology,10(1):74–80.
|               |       |     |               |     |              |     | MistralAI.2025a. |     | mistralai/mistral-7b-instruct-v0.3. |     |     |     |     |
| ------------- | ----- | --- | ------------- | --- | ------------ | --- | ---------------- | --- | ----------------------------------- | --- | --- | --- | --- |
| Investopedia. | 2025. |     | Investopedia. |     | https://www. |     |                  |     |                                     |     |     |     |     |
investopedia.com/. MistralAI.2025b. mistralai/mistral-small-24b-instruct-
2501.
| SatyadharJoshi.2025. |     |     | Acomprehensivereviewofgen |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aiagents: Applicationsandframeworksinfinance, IzunnaOkpala,AshkanGolgoon,andArjunRaviKan-
investments and risk domains. International Jour- nan. 2025. Agentic ai systems applied to tasks in
nalofInnovativeScienceandResearchTechnology, financialservices: Modelingandmodelriskmanage-
| pages1339–1355. |     |     |     |     |     |     | mentcrews. |     | Preprint,arXiv:2502.05439. |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------------------- | --- | --- | --- | --- |
176

DanielE.O’Leary.2025. Editorial: Analysisofsenti- GemmaTeam,AishwaryaKamath,JohanFerret,Shreya
ment estimates and cognitive fallacies in large lan- Pathak,NinoVieillard,RamonaMerhej,SarahPerrin,
guage models. Intelligent Systems in Accounting, Tatiana Matejovicova, Alexandre Ramé, Morgane
Finance and Management, 32(3):e70010. E70010 Rivière,LouisRouillard,ThomasMesnard,Geoffrey
| 9691779. |     |     |     |     |     | Cideron,JeanbastienGrill,SabelaRamos,Edouard |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
Yvinec,MichelleCasbon,EtiennePot,IvoPenchev,
OpenAI. 2025a. o3 and o4-mini system and197others.2025b. Gemma3technicalreport.
| card. |     | https://cdn.openai.com/pdf/ |     |     |     | Preprint,arXiv:2503.19786. |     |     |     |     |     |
| ----- | --- | --------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
2221c875-02dc-4789-800b-e7758f3722c1/
o3-and-o4-mini-system-card.pdf. KesenWang,DauletToibazar,AbdulrahmanAlfulayt,
AbdulazizS.Albadawi,RanyaA.Alkahtani,AsmaA.
OpenAI.2025b. Openaitext-embeddings-3. Ibrahim, Haneen A. Alhomoud, Sherif Mohamed,
|     |     |     |     |     |     | andPedroJ.Moreno.2025. |     |     |     | Multi-agentinteractive |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | ---------------------- | --- |
Qwen.2025. Qwen/qwq-32b. question generation framework for long document
|                 |         |     |       |        |           | understanding. |     | Preprint,arXiv:2507.20145. |     |     |     |
| --------------- | ------- | --- | ----- | ------ | --------- | -------------- | --- | -------------------------- | --- | --- | --- |
| Reddit. [2025]. | Reddit: | The | heart | of the | internet. |                |     |                            |     |     |     |
NengWang,HongyangYang,andChristinaDanWang.
https://www.reddit.com.
2023. Fingpt:Instructiontuningbenchmarkforopen-
DonaldG.Saari.2023. Selectingavotingmethod: the source large language models in financial datasets.
case for the borda count. Constitutional Political NeurIPSWorkshoponInstructionTuningandInstruc-
tionFollowing.
Economy,34(3):357–366.
PhilippWinder,ChristianHildebrand,andJochenHart-
| Javier Sanz-Cruzado, |     | Edward | Richards, | and | Richard |     |     |     |     |     |     |
| -------------------- | --- | ------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
McCreadie.2024. Far-ai: Amodularplatformforin- mann.2024. Biasedechoes: Generativeaimodels
vestmentrecommendationinthefinancialdomain. In reinforce investment biases and increase portfolio
risksofprivateinvestors.
AdvancesinInformationRetrieval,pages267–271,
Cham.SpringerNatureSwitzerland.
AnYang,AnfengLi,BaosongYang,BeichenZhang,
|                  |          |     |          |          |         | Binyuan | Hui, | Bo Zheng, | Bowen | Yu, | Chang Gao, |
| ---------------- | -------- | --- | -------- | -------- | ------- | ------- | ---- | --------- | ----- | --- | ---------- |
| Thibault Sellam, | Dipanjan |     | Das, and | Ankur P. | Parikh. |         |      |           |       |     |            |
2020. Bleurt: Learningrobustmetricsfortextgener- Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
|     |     |     |     |     |     | iheng | Liu, | Fan Zhou, | Fei | Huang, Feng | Hu, Hao |
| --- | --- | --- | --- | --- | --- | ----- | ---- | --------- | --- | ----------- | ------- |
ation. Preprint,arXiv:2004.04696.
|                             |     |     |                    |     |     | Ge, Haoran |       | Wei, Huan | Lin,      | Jialong Tang, | and 41    |
| --------------------------- | --- | --- | ------------------ | --- | --- | ---------- | ----- | --------- | --------- | ------------- | --------- |
|                             |     |     |                    |     |     | others.    | 2025. | Qwen3     | technical | report.       | Preprint, |
| Sentence-Transformers.2021. |     |     | all-minilm-l12-v2. |     |     |            |       |           |           |               |           |
arXiv:2505.09388.
| Takehiro Takayanagi, |            | Kiyoshi | Izumi, | Atsuo      | Kato, |            |       |                                       |      |               |     |
| -------------------- | ---------- | ------- | ------ | ---------- | ----- | ---------- | ----- | ------------------------------------- | ---- | ------------- | --- |
|                      |            |         |        |            |       | Hongyang   | Yang, | Xiao-Yang                             | Liu, | and Christina | Dan |
| Naoyuki              | Tsunedomi, | and     | Yukina | Abe. 2023. | Per-  |            |       |                                       |      |               |     |
|                      |            |         |        |            |       | Wang.2023. |       | Fingpt: Open-sourcefinanciallargelan- |      |               |     |
sonalizedstockrecommendationwithinvestors’at-
|                                  |     |     |     |               |     | guagemodels. |     | FinLLMSymposiumatIJCAI2023. |     |     |     |
| -------------------------------- | --- | --- | --- | ------------- | --- | ------------ | --- | --------------------------- | --- | --- | --- |
| tentionandcontextualinformation. |     |     |     | InProceedings |     |              |     |                             |     |     |     |
ofthe46thInternationalACMSIGIRConferenceon
BoyuZhang,HongyangYang,andXiao-YangLiu.2023.
ResearchandDevelopmentinInformationRetrieval,
|     |     |     |     |     |     | Instruct-fingpt: |     | Financial | sentiment | analysis | by in- |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | --------- | -------- | ------ |
SIGIR’23,page3339–3343,NewYork,NY,USA. struction tuning of general-purpose large language
AssociationforComputingMachinery.
|                      |     |         |        |        |       | models.       | FinLLMSymposiumatIJCAI2023. |                 |     |           |           |
| -------------------- | --- | ------- | ------ | ------ | ----- | ------------- | --------------------------- | --------------- | --- | --------- | --------- |
| Takehiro Takayanagi, |     | Kiyoshi | Izumi, | Javier | Sanz- |               |                             |                 |     |           |           |
|                      |     |         |        |        |       | Tianyi Zhang, |                             | Varsha Kishore, |     | Felix Wu, | Kilian Q. |
Cruzado,RichardMcCreadie,andIadhOunis.2025a.
|     |     |     |     |     |     | Weinberger, |     | and Yoav | Artzi. | 2020. | Bertscore: |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ------ | ----- | ---------- |
Aregenerativeaiagentseffectivepersonalizedfinan- Evaluating text generation with bert. Preprint,
| cialadvisors? | Preprint,arXiv:2504.05862. |     |     |     |     | arXiv:1904.09675. |     |     |     |     |     |
| ------------- | -------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
TakehiroTakayanagi,MasahiroSuzuki,KiyoshiIzumi,
YanzhaoZhang,MingxinLi,DingkunLong,XinZhang,
JavierSanz-Cruzado,RichardMcCreadie,andIadh
|     |     |     |     |     |     | Huan | Lin, | Baosong Yang, |     | Pengjun Xie, | An Yang, |
| --- | --- | --- | --- | --- | --- | ---- | ---- | ------------- | --- | ------------ | -------- |
Ounis. 2025b. Finpersona: An llm-driven conver- DayihengLiu,JunyangLin,FeiHuang,andJingren
sational agent for personalized financial advising. Zhou. 2025. Qwen3 embedding: Advancing text
InAdvancesinInformationRetrieval,pages13–18, embeddingandrerankingthroughfoundationmodels.
| Cham.SpringerNatureSwitzerland. |     |     |     |     |     | Preprint,arXiv:2506.05176. |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
GeminiTeam,RohanAnil,SebastianBorgeaud,Jean-
|     |     |     |     |     |     | Yuhan Zhi, | Xiaoyu | Zhang, | Longtian | Wang, | Shumin |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | ------ | -------- | ----- | ------ |
Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Jiang,ShiqingMa,XiaohongGuan,andChaoShen.
Schalkwyk, Andrew M. Dai, Anja Hauth, Katie 2025. Exposingproductbiasinllminvestmentrec-
Millican, David Silver, Melvin Johnson, Ioannis ommendation. Preprint,arXiv:2503.08750.
| Antonoglou, | Julian | Schrittwieser, |     | Amelia | Glaese, |     |     |     |     |     |     |
| ----------- | ------ | -------------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- |
JilinChen,EmilyPitler,TimothyLillicrap,Angeliki YuhangZhou,YuchenNi,ZhihengXi,ZhangyueYin,
Lazaridou,and1332others.2025a. Gemini: Afam- YuHe,GanYunhui,XiangLiu,ZhangJian,SenLiu,
ilyofhighlycapablemultimodalmodels. Preprint, XipengQiu,YixinCao,GuangnanYe,andHongfeng
arXiv:2312.11805. Chai.2025. AreLLMsrationalinvestors? astudy
177

|     | onthefinancialbiasinLLMs.             |              |     |         | InFindingsoftheAs- |              |     |                              |            |     |     |     |     |
| --- | ------------------------------------- | ------------ | --- | ------- | ------------------ | ------------ | --- | ---------------------------- | ---------- | --- | --- | --- | --- |
|     | sociationforComputationalLinguistics: |              |     |         |                    | ACL2025,6    |     |                              |            |     |     |     |     |
|     | pages                                 | 24139–24173, |     | Vienna, | Austria.           | Association7 |     | ###                          | Key Points | ### |     |     |     |
|     | forComputationalLinguistics.          |              |     |         |                    |              |     | {key_points_to_keep_in_mind} |            |     |     |     |     |
8
|     | David    | Zibriczky.         | 2016. | Recommender |                        | systems | meet9 |     |     |     |     |     |     |
| --- | -------- | ------------------ | ----- | ----------- | ---------------------- | ------- | ----- | --- | --- | --- | --- | --- | --- |
|     | finance: | Aliteraturereview. |       |             | InInternationalWork-10 |         |       | --- |     |     |     |     |     |
**Inputs**:
|     | shoponPersonalization&RecommenderSystemsin |     |     |     |     |     | 11  |          |     |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     | FinancialServices.                         |     |     |     |     |     |     | {inputs} |     |     |     |     |     |
12
---
13
|     |     |     |     |     |     |     | 14  | **Your | Response**:""" |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | --- | --- | --- |
Appendices
|     |     |     |     |     |     |     |     | A.1.2 | IndividualPhases |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | --- | --- | --- | --- |
A PromptingGuidelinesfollowedforthe
|     | generationandevaluationstages |     |     |     |     |     |     | 1.  | Classification: |     |     |     |     |
| --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
A.1 Guidelinesfollowedinthegeneration a. The primary goal of this stage is to
|     |              | stage. |         |     |           |                |     |     | classifyincominguserqueriesintosuit- |            |     |       |          |
| --- | ------------ | ------ | ------- | --- | --------- | -------------- | --- | --- | ------------------------------------ | ---------- | --- | ----- | -------- |
|     |              |        |         |     |           |                |     |     | ablecategoriesofpersonalfinance.     |            |     |       | The      |
|     | This section |        | focuses | on  | outlining | the guidelines |     |     |                                      |            |     |       |          |
|     |              |        |         |     |           |                |     |     | prompt                               | constrains | the | model | by forc- |
followedincraftingthepromptsforeachphaseof
ingasingle-labelclassification(ONEof
generatingandevaluatingtheoutputs.
thefollowing)basedonPRIMARYIN-
A.1.1 Overarchingprinciples TENT,whichpreventsambiguityanden-
There are three core principles followed for the sures a decisive output for downstream
|     | processofcraftingtheprompts: |     |     |     |     |     |     |     | routing. |          |       |       |            |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----- | ----- | ---------- |
|     |                              |     |     |     |     |     |     |     | b. Each  | category | has a | Scope | and an ex- |
a. Modularity
|     |                   |     |     |     |     |     |     |     | ample      | that                      | the model | uses | to make its |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------------- | --------- | ---- | ----------- |
|     | b. Deconstruction |     |     |     |     |     |     |     | decisions. | Ifthequerydoesnotfallinto |           |      |             |
anyofthecategories,thequeryislabeled
c. Personification
Not_Applicable.
|     | The | goal | of the | overall | prompt | crafting | is to |     |     |     |     |     |     |
| --- | --- | ---- | ------ | ------- | ------ | -------- | ----- | --- | --- | --- | --- | --- | --- |
2. QueryAnalysis:
|     | keep the | overall | structure |     | of the | prompts | similar |     |     |     |     |     |     |
| --- | -------- | ------- | --------- | --- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- |
andswappabledependingonthetaskathand. As a. The primary goal of this prompt is to
with the framework, where the complex task of directthemodeltobreakdowntheuser
generatingasuitableresponseisbrokendowninto queryintomorespecificandmanageable
individualphases,thepromptsarebrokendownto piecesofinformation.
makesurethestructureoftheinstructionsgivento
|     |                         |     |     |     |     |     |     |     | b. SincemostoftheuserqueriesonReddit |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
|     | themodelremainsthesame. |     |     |     |     |     |     |     | andingeneralareoftenfilledwithunre-  |     |     |     |     |
Eachstageofthepromptinghadaunique,suit- latednoise,thisstagedirectsthemodel
ablepersona(e.g.,linguisticanalysisexpert,expert
todistiltheuser’squeryintoessentialse-
|     | financialreasoningengine). |     |     |     | Thisrole-playingtech- |     |     |     |     |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
manticelements,eliminatingtheconver-
niqueprimesthemodeltoaccessrelevantknowl- sational distractions and concentrating
edge,adopttheappropriatetone,andconstrainits onactionableconcernsandtheirimpact
behaviortothespecificrequirementsofthetask.
onthekeystakeholders.
Thegenericstructureofthepromptisasfollows:
3. ContextAnalysis:
|     |     |     |     |     |     |     |     |     | a. The context |     | analysis | is one | of the key |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------ | ---------- |
"""
| 1   |         |     |            |     |       |         |     |     | promptsthatinfluencesthequalityofthe |        |            |     |            |
| --- | ------- | --- | ---------- | --- | ----- | ------- | --- | --- | ------------------------------------ | ------ | ---------- | --- | ---------- |
| 2   | You are | a   | {persona}, |     | whose | task is | to  |     |                                      |        |            |     |            |
|     |         |     |            |     |       |         |     |     | output                               | by the | framework. |     | The prompt |
{task_details}.
(cid:44)→
directsthefinalmodeltogenerateaction-
| 3   |                 |     |     |     |     |     |     |     | ableandinsightfulcontextualsummaries |        |      |             |         |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ------ | ---- | ----------- | ------- |
|     | ### INSTRUCTION |     |     | ### |     |     |     |     |                                      |        |      |             |         |
| 4   |                 |     |     |     |     |     |     |     | that are                             | placed | into | the model’s | natural |
{instructions_for_the_task}
5
chain-of-thought.
178

| b. ThepromptexplicitlyasksforaConcise |     |     |     |     |     | 6.  | ResponseGeneration |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
chain-of-thoughtAnalysisBlockandin-
|         |     |       |           |       |        |     | a.  | This final | stage synthesises | all preced- |
| ------- | --- | ----- | --------- | ----- | ------ | --- | --- | ---------- | ----------------- | ----------- |
| structs | the | model | that this | is an | inter- |     |     |            |                   |             |
inganalysesintoacoherent,user-facing
nalreasoningstep,notthefinalanswer.
response.
Thisstepforcesthemodeltoexternalise
|     |     |     |     |     |     |     | b.  | Thepromptprovidesthemodelwithall |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- |
itsreasoningprocess,exploringmultiple
previousoutputs(theoriginalqueryand
scenariosandtheirconsequencesbefore
thecomprehensivechain-of-thought)and
concluding.
explicitlyinstructsittointegratebothfac-
| c. By requiring |     | the | model | to detail | the |     |     |     |     |     |
| --------------- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
tualaccuracyandemotionalintelligence
| Stakeholder |     | Impact  | for each   | approach, |     |     |     |             |                          |     |
| ----------- | --- | ------- | ---------- | --------- | --- | --- | --- | ----------- | ------------------------ | --- |
|             |     |         |            |           |     |     |     | seamlessly. | Itactsasafinal"assembly" |     |
| the prompt  |     | ensures | a holistic | analysis  |     |     |     |             |                          |     |
instruction,guidingthemodelonhowto
| that considers |     | the | financial | and | emo- |     |     |     |     |     |
| -------------- | --- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- |
combinetherationalandaffectivecom-
tionalconsequencesforallrelevantpar-
ponents.
| ties mentioned |     | in       | the query. |     | This    |     |     |         |                   |               |
| -------------- | --- | -------- | ---------- | --- | ------- | --- | --- | ------- | ----------------- | ------------- |
|                |     |          |            |     |         |     | c.  | The use | of clear positive | (Do) and neg- |
| scenario-based |     | analysis | moves      |     | the re- |     |     |         |                   |               |
ative(Donot)instructionscreatesstrict
sponsesbeyondsimplefact-basedanal-
|         |        |               |     |      |     |     |     | behavioralboundaries. |     | Forinstance,"Do |
| ------- | ------ | ------------- | --- | ---- | --- | --- | --- | --------------------- | --- | --------------- |
| ysis to | a more | human-centred |     | form | of  |     |     |                       |     |                 |
notreferencethechain-of-thoughtanaly-
reasoning.
sis"ensuresthefinaloutputisnaturaland
user-friendly,hidingthecomplexunder-
4. Psychologicalanalysis
lyingcognitivearchitecturefromtheend-
| a. The goal | of  | this prompt | is  | to direct | the |     |     |     |     |     |
| ----------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- |
user. Theseinstructionscreateahelpful
| model | and | extract | the key | information |     |     |     |     |     |     |
| ----- | --- | ------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
responsewithoutbeingroboticortrans-
abouttheuser’sstateofmindwhenask-
parentaboutitsinnerworkings.
ingthequery.
|     |     |     |     |     |     |     | d.  | Theseresponsesaregeneratedinaway |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- |
b. Thepromptdemandsthateveryconclu-
|     |     |     |     |     |     |     |     | that ensure | the ability | to train non- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------------- |
sionaboutsentiment,emotion,orintent reasoningmodelsfromthesamedataset.
bejustifiedbyreferencingspecificwords
or phrases. This approach grounds the A.2 PromptGuidelinesforEvaluation
throughLLM-as-a-Judge
analysisintextualevidence,preventing
themodelfrommakingunfoundedpsy- The goal of the evaluation is to determine which
| chological |     | assumptions | and | improving |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- |
responsesarenaturallyrankedbetterthantheoth-
theexplainabilityof itsaffectiveunder- ers. Since this is a list-wise ranking with a high
| standing. |     |     |     |     |     | roomforconfusionorhallucination,theevaluation |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- |
c. Thisanalysisisaseparatestepfromthe criterionarestrictlydefined.
Theoverallpromptstructureforeachofthecase
| financial                            | reasoning  |            | (Context  | Analysis). |        |               |     |     |     |     |
| ------------------------------------ | ---------- | ---------- | --------- | ---------- | ------ | ------------- | --- | --- | --- | --- |
| This                                 | deliberate | separation |           | prevents   | the    | areasfollows: |     |     |     |     |
| user’s                               | emotional  | state      | from      | biasing    | the    |               |     |     |     |     |
| objective                            | financial  |            | analysis, | and        | vice-1 |               |     |     |     |     |
| versa,allowingforafinalresponsethat2 |            |            |           |            |        | """           |     |     |     |     |
cansynthesisebothaspectswithoutcom-3 You are a {persona}. Your task is to
|                  |     |     |     |     |     |           | rank | financial | advice         | responses |
| ---------------- | --- | --- | --- | --- | --- | --------- | ---- | --------- | -------------- | --------- |
| promisingeither. |     |     |     |     |     | (cid:44)→ |      |           |                |           |
|                  |     |     |     |     |     |           | from | best      | to worst based | *solely*  |
(cid:44)→
5. ResponseRubric
|     |     |     |     |     |     |     | on  | the strict | definition | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- |
(cid:44)→
{target_aspect}.
| a. Thisstageconsolidatesallthepreviously |     |     |     |     |     | (cid:44)→ |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
collectedinformationandcreatesacom-4
|     |     |     |     |     |     | ### | **Evaluation |     | Criteria** |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- |
pleterubricthatcandirectthemodelinto5
|     |     |     |     |     |     | 6 {Evaluation |     | Criterion} |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | --- | --- |
generatingthefinalresponse.
7
| b. The                             | key information |     | from | the | previ- |           |      |         |          |          |
| ---------------------------------- | --------------- | --- | ---- | --- | ------ | --------- | ---- | ------- | -------- | -------- |
|                                    |                 |     |      |     |        | ####      | **I. | Primary | Criteria | (What to |
| ousstagesgetshighlightedwhilebeing |                 |     |      |     |        | 8         |      |         |          |          |
|                                    |                 |     |      |     |        | (cid:44)→ | look | for):** |          |          |
linkedtodifferentpartsoftheuserquery
{primary_set_of_instructions}
9
foreasierreferenceandunderstanding.
179

a. A response is considered relevant if it
10
address every component of the user’s
#### **II. Explicit Penalties (What to
11
query. Arelevantresponseshouldincor-
penalize):**
(cid:44)→
porate the specific figures, constraints,
{penalizing_instructions}
12
anddetailsmentionedintheuser’squery,
13
and answer the questions immediately
#### ** III. Key Points to note:**
14
withoutgenericintroductions.
{additional_instructions}
15
b. Anypartialrelevanceoradditionalcon-
---
16
textnotrelevanttothequeryispenalized.
17
**Query:** {query}
18
B ModularRAGforContextAnalysis
19
**Responses to Rank:**
20 Goal. Given a user query, the context-analysis
{anonymized_shuffled_model_responses}
21 phase assembles a compact, high-signal context
"""
22 packfromtwospecializedcorpora: (i)Behavioral
insights (behavioral economics and psychology)
and(ii)Financialconcepts(mainstreampersonalfi-
1. Accuracy:
nanceknowledge). Thecontextpackisthenpassed
a. The goal of this prompt is to direct the totheresponsegenerator.
model to review the search results and
Corpora. Behavioralinsightsaresourcedfrom
thequerytoestimatetheaccuracyofthe
peer-reviewedresearchandreputablepsychology
output.
venues, complemented by carefully selected psy-
b. Theresponsesarepenalizedifandonlyif
chologyblogsforpractitionerframing. Financial
theresponsesdemonstratewrong/harm-
conceptsaredrawnfrompractical,high-visibility
ful advice (or) inappropriate financial
sources such as Investopedia, Bogleheads, and
conceptstothequery.
otherwidelycitedpersonal-financeviewpoints. All
c. Themodelisspecificallyinstructednot
rawpagesareconvertedtoMarkdownwithheaders
to penalise on the style or relevance of
andsectionstructurepreservedtoretaindocument
theresponseandsolelyfocusontheac-
semantics.
curacyofthefinancialconceptsprovided
inthetext. Thisguidesthemodeltorank Preprocessingandindexing.
solelybasedontheaccuracyofthefinan-
cialconceptspresentintheresponse. • Scraping & normalization: We scrape public
pages(respectingrobots/terms), removeboiler-
2. Plausibility:
plate(nav,ads),andnormalizetoMarkdownwith
a. A response is defined to be plausible if stableheadings.
itsoundsreasonableandbelievabletoa
• Semanticchunking: Documentsaresegmented
typicaluser. Someofthekeycharacter-
into modular chunks along header/semantic
isticsinclude
boundaries to keep each chunk topically coher-
• Logicalflowandcoherentreasoning
ent; we attach metadata (source, URL or han-
structure
dle, snapshot time, section path, corpus tag:
• Sensibleapproachtotheproblem
behavioralorfinancial).
b. Aresponseispenalizedifitcontainsun-
necessarilyverboseorcontainexcessive • Denseindexing: Eachchunkisembeddedwith
detail. Theresponsesarealsopenalized text-embeddings-large-003 and stored in a
iftheycontaincomplexorhard-to-follow vectordatabsase(ChromaDB).
reasoning.
c. Themodelisspecificallyinstructednot Retrievalandre-ranking(perquery).
topenaliseontheaccuracyorrelevance
1. Dual retrieval: From each index, retrieve the
oftheresponses.
top-k candidates (k=25) using the query em-
3. Relevance: bedding.
180

2. Cross-encoder re-ranking: Concate- • Penalties. Deductionsoccuriff theanswercon-
nate candidates from both corpora and tainswrongorharmfulguidance,ormisapplies
re-rank with a lightweight cross-encoder financialconceptstotheuser’ssituation.
(sentence-transformers/all-minilm-l12-v2);
|     |     |     |     |     |     | • Non-considerations. |     | Style,tone,verbosity,and |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | ------------------------ | --- | --- |
keeptop-m(m=15).
evenpartialcoveragearenotpenalized;thejudge
3. LLMsynthesis/filter: AfastLLM(gemini-2.0- isinstructedtofocusexclusivelyoncorrectness.
| flash) | receives {top-m | chunks, |     | query} | and (a) |     |     |     |     |     |
| ------ | --------------- | ------- | --- | ------ | ------- | --- | --- | --- | --- | --- |
Plausibility(reasoningquality).
| extractssalientfacts, |     | definitions, |     | anddecision |     |              |                               |     |     |     |
| --------------------- | --- | ------------ | --- | ----------- | --- | ------------ | ----------------------------- | --- | --- | --- |
|                       |     |              |     |             |     | • Objective. | Assesswhethertheanswerreadsas |     |     |     |
criteria;(b)discardsresidualoff-topicspans;(c)
reasonableandbelievabletoatypicaluser—i.e.,
emitsastreamlined,source-attributedcontext.
|     |     |     |     |     |     | it exhibits | a clear | logical flow and | a coherent |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | ---------------- | ---------- | --- |
problem-solvingstructure.
| Assemblyandhandoff. |     | Thestreamlinedcontext |     |     |     |     |     |     |     |     |
| ------------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(withinlinesourceattributionsandcorpustags)is
|         |               |          |        |     |           | • Penalties. | Overlyverbose,needlesslycomplex, |     |     |     |
| ------- | ------------- | -------- | ------ | --- | --------- | ------------ | -------------------------------- | --- | --- | --- |
| passed, | together with | the user | input, | to  | the final |              |                                  |     |     |     |
orhard-to-followchainsofreasoningarepenal-
LLMthatcompletesthecontext-analysisphase.
ized.
| Behavioralvs. | financialmoduleroles. |     |     |     | Thebe- |                       |     |                     |     |     |
| ------------- | --------------------- | --- | --- | --- | ------ | --------------------- | --- | ------------------- | --- | --- |
|               |                       |     |     |     |        | • Non-considerations. |     | Factual correctness |     | and |
havioralmodulesurfacescognitive-biasdescrip- topicalcoveragearenotscoredhere;thelensis
tors,debiasingtactics,anduser-statecues(e.g.,loss
purelyrhetorical/structural.
| aversionframing,presentbiasprompts). |     |     |     | Thefinan- |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
Relevance(taskalignment).
| cial module  | surfaces    | actionable | rules   | of          | thumb, |              |                                  |     |     |     |
| ------------ | ----------- | ---------- | ------- | ----------- | ------ | ------------ | -------------------------------- | --- | --- | --- |
|              |             |            |         |             |        | • Objective. | Verifythattheresponsedirectlyad- |     |     |     |
| definitions, | procedures, | and        | typical | constraints |        |              |                                  |     |     |     |
(e.g.,contributionlimits,insuranceconcepts,pay- dresseseverycomponentoftheuser’squery,in-
offorderingheuristics). Bothmodulescontributeto corporates the user’s numbers, constraints, and
thesamecontextpack;behavioralcuesguidehow context,andanswerswithoutgenericpreambles.
| advice is | framed, while | financial |     | chunks | ground |              |                   |            |     |          |
| --------- | ------------- | --------- | --- | ------ | ------ | ------------ | ----------------- | ---------- | --- | -------- |
|           |               |           |     |        |        | • Penalties. | Partial coverage, | tangential |     | content, |
whatadviceisprovided.
orextracontextnotpertinenttothequeryispe-
| Limitations. | (1)Coverageandstalenessdepend |     |     |     |     | nalized. |     |     |     |     |
| ------------ | ----------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
onthesnapshotofpublicsources;(2)blogscanin-
|     |     |     |     |     |     | • Non-considerations. |     | Factualaccuracyandstylis- |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | ------------------------- | --- | --- |
troducestylebiasdespitere-ranking;(3)thesynthe-
ticpolishareignoredforthisaxis.
sisstepmayover-prioritizewell-structuredsources.
| Wemitigatethesebypreservingsourceattributions, |     |     |     |     |     | C.2 BordaPoints |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
trackingsnapshottimestamps,andpromptingsyn-
|     |     |     |     |     |     | Definition. | For a listwise | ranking | of n systems, |     |
| --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------- | ------------- | --- |
thesistopreferhigher-prioritysourceswhencon-
|     |     |     |     |     |     | theitemplacedatrankr |     | (r = 1isbest)receivesa |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | ---------------------- | --- | --- |
flictsarise.
Bordascore
|     |     |     |     |     |     |     | b   | = n−r, |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
C DeeperEvaluationResults
sothetopentrygetsn−1pointsandthelastgets
C.1 ScoreDefinitionsandRationale
0.
| We evaluate | responses | along | three | orthogonal |     |             |                                 |     |     |     |
| ----------- | --------- | ----- | ----- | ---------- | --- | ----------- | ------------------------------- | --- | --- | --- |
|             |           |       |       |            |     | Motivation. | Bordaaggregationiswell–suitedto |     |     |     |
axes—Accuracy,Plausibility,andRelevance—to LLM-as-a-judgeexperimentswhererelativequal-
separatefactualcorrectness,reasoningquality,and
itymattersmorethanabsolutescores:
| taskalignment. | Thisdecompositionavoidsasingle |     |     |     |     |     |     |     |     |     |
| -------------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
scalar that can reward fluent but unsafe answers • Full-order utilisation: every position con-
or penalize terse yet correct ones, and it enables tributes signal, ensuring that small but con-
targetederroranalysisandablations. sistentadvantagesarecapturedratherthandis-
cardedbywinner-takes-allrules.
Accuracy(financialcorrectness).
• Objective. Judge reviews the response against • Cardinal comparability: with a fixed candi-
thequeryandretrievedevidenceandscoresonly date set, raw points can be averaged across
the validity of financial concepts, calculations, queriesandjudgeswithoutnormalisation,giv-
| andadvice. |     |     |     |     |     | ingastable,interpretablemean. |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
181

• Robustnesstomildnoise: swappingadjacent anyonedemonstrationset. Asubsampleofthese
middlerankschangesthetotalbyonly±1,so rankingswerefurthervalidatedbyo4-minimodel
individualjudgeidiosyncrasiesexertlimited toconsolidatetherelativeperformance.
influenceonthefinalaverage.
|     |     |     |     |     |     | Scoring | and aggregation |     | (per criterion). |     | For |
| --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ---------------- | --- | --- |
eachquery,judgesperformmulti-shotlistwiserank-
| Interpretation. |     | Higher | mean | Borda | points in- |     |     |     |     |     |     |
| --------------- | --- | ------ | ---- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
dicatethatasystemoutranksitspeersmoreoften. ingoveranonymizedoutputsusingtherubricsin
Themaximumpossiblemeanisn−1;thegapto Sec. C. Ranks are converted to raw Borda points
|     |     |     |     |     |     | b = n−r. | Wethen: |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ------- | --- | --- | --- | --- |
thisceilingoffersanintuitivesenseofhead-room.
Limitations.
1. averagebacrossshuffles/repeatsforeachjudge;
| • Rank-reversal: |     | insertingorremovingacandi- |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2. averageacrossthejudgestoobtainaper-query,
datecanchangeeverysystem’sscore,compli-
per-criterionscoreforeachmodel;
catinglongitudinalcomparisons.
3. averageacrossallquerieswithinacategory(e.g.,
• IndependenceofIrrelevantAlternatives(IIA)
the“overall”setoraPFsubcategory)toobtain
violation: a judge’s relative preference be- the model’s criterion-wise mean in that cate-
tweentwosystemscanaffect,andbeaffected
gory.
by,ranksassignedtoothers.
ThestackedbarsinFig.2displaythesecriterion-
• Equal-intervalassumption: themethodtreats wisemeans(Accuracy,Plausibility,Relevance)for
| the   | gap      | between    | successive | ranks | as uni-     |             |              |                |     |     |         |
| ----- | -------- | ---------- | ---------- | ----- | ----------- | ----------- | ------------ | -------------- | --- | --- | ------- |
|       |          |            |            |       |             | each model. | For a single | category-level |     |     | number, |
| form, | ignoring | situations |            | where | judges per- |             |              |                |     |     |         |
wealsoreporttheunweightedaverageofthethree
ceivelargerqualityjumpsnearthetop.
criterion-wisemeansasthemodel’sfinalrepresen-
tationscoreinthatcategory.
| • Strategicsusceptibility: |     |     | ifhumanjudgesknow |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
whatinfluencestheaggregation,theycouldin-
C.4 OverallCategoryScores(Accuracy,
flateordeflatelowerrankstobenefitafavored
Plausibility,Relevance)
system.
|     |     |     |     |     |     | We report | criterion-wise | means | derived | from | the |
| --- | --- | --- | --- | --- | --- | --------- | -------------- | ----- | ------- | ---- | --- |
C.3 LLM-JuryProtocol raw Borda points assigned by the LLM jury
LLM-based judging scales across topics, is inex- (Sec. C.3). For each criterion and model, scores
areaveragedacrossjudgesandquerieswithinthe
| pensive, | and achieves |     | strong | agreement | with hu- |             |                 |     |     |     |     |
| -------- | ------------ | --- | ------ | --------- | -------- | ----------- | --------------- | --- | --- | --- | --- |
|          |              |     |        |           |          | overallset. | Higherisbetter. |     |     |     |     |
manraterswhenrubricsareexplicitandtaskcon-
textisprovided. Italsocapturesholisticqualities Accuracy. Figure 3 shows a size-tilted pattern:
(e.g.,coherence,taskfit)thatsingle-numbersimi-
QwQ-32B(reasoning)leads,followedbyGemma3-
laritymetricsmaymiss.
|     |     |     |     |     |     | 27B-itandGemma3-12B-it. |     |     | Mistral-Small-24Bsits |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --------------------- | --- | --- |
Itshouldbenotedthatzero-shotjudgingisvul-
|     |     |     |     |     |     | betweenthistopclusterandtherest. |     |     |     | Theproposed |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | ----------- | --- |
nerabletopositionbias(earlieritemsrankhigher),
8Bmodelismid-pack—behindtheleadersandthe
same-familybias(preferenceforoutputsfromthe
24Bbaseline,butaheadofseveral7–14Bbaselines.
judge’sownfamily),andprompt/leniencyvariance.
Thispointstofactualcalibrationandretrieval/verifi-
Wetherefore(i)usemulti-shotpromptstoanchor
cationastheprimaryleverstoclosethegap,rather
| criteria, | (ii) evaluate | with | listwise | ranking | on in- |     |     |     |     |     |     |
| --------- | ------------- | ---- | -------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
thanrewritingorstylistictuning.
| dependently | shuffled | candidate |     | lists, | and (iii) di- |     |     |     |     |     |     |
| ----------- | -------- | --------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- |
AsshowninFig.4,QwQ-32Branks
| versifyjudgesacrossmodelfamiliestominimize |     |            |                     |            |          | Plausibility.                      |                 |                            |               |          |       |
| ------------------------------------------ | --- | ---------- | ------------------- | ---------- | -------- | ---------------------------------- | --------------- | -------------------------- | ------------- | -------- | ----- |
| correlatedbias.                            |     |            |                     |            |          | first,withGemma3-27B-itnext.       |                 |                            | Theproposed8B |          |       |
|                                            |     |            |                     |            |          | clustersnearthefront:              |                 | itexceedstheMistral-Small- |               |          |       |
| Judge pool                                 | and | prompting. |                     | We employ  | two      |                                    |                 |                            |               |          |       |
|                                            |     |            |                     |            |          | 24BbaselinebuttrailsGemma3-12B-it. |                 |                            |               | Thissug- |       |
| mainheterogeneousjudges:                   |     |            | DeepSeek-v3-0324(5- |            |          |                                    |                 |                            |               |          |       |
|                                            |     |            |                     |            |          | gests that                         | the dataset     | structure                  | and           | few-shot | con-  |
| shot), Kimi-k2                             |     | (3-shot).  | For                 | each query | and cri- |                                    |                 |                            |               |          |       |
|                                            |     |            |                     |            |          | ditioning                          | induce coherent |                            | reasoning     | steps    | and a |
terion(Accuracy,Plausibility,Relevance),judges
sensibleflowevenatmidscale.
| rank anonymized |     | model | outputs | in a | single list. |     |     |     |     |     |     |
| --------------- | --- | ----- | ------- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
Few-shotexemplarsareheldconstantwithinarun Relevance. Figure5indicatesstrongtaskalign-
and varied across repeats to reduce overfitting to ment at the top end (QwQ-32B, Gemma3-27B-it,
182

Figure3: Accuracy(meanrawBordapointsperquery, Figure4: Plausibility(meanrawBordapoints). The
averagedoverjudges). Asize-drivenleadisvisible;the proposed8Bclustersnearthefrontandmatchesor
proposed8Bismid-pack,indicatingfactualcalibration exceedsseverallargerbaselines,reflectingstrong
astheprimaryimprovementlever. logicalflowandcoherentreasoning.
Gemma3-12B-it). The proposed 8B ranks next parameter,holdingtheevaluationprotocolfixed. It
|        |       |                  |     |            |     |          | is not a | substitute | for | absolute | scores | (Sec. | C.4), |
| ------ | ----- | ---------------- | --- | ---------- | --- | -------- | -------- | ---------- | --- | -------- | ------ | ----- | ----- |
| (4/8), | ahead | of the remaining |     | baselines, |     | suggest- |          |            |     |          |        |       |       |
ingitreliablymapsuserconstraintsandaddresses butacomplementarylensforcost-,latency-,and
allpartsofthequerywithoutdriftingintogeneric memory-constraineddeployments.
| preambles. |     | The residual | gap | likely | reflects | cases |           |             |     |        |     |       |          |
| ---------- | --- | ------------ | --- | ------ | -------- | ----- | --------- | ----------- | --- | ------ | --- | ----- | -------- |
|            |     |              |     |        |          |       | Relevance | efficiency. |     | Figure | 6   | shows | the pro- |
thatrequireexhaustiveedgehandling(e.g.,niche
8B
|             |        |        |      |       |        |          | posed | model | with | the | highest | Borda-per- |     |
| ----------- | ------ | ------ | ---- | ----- | ------ | -------- | ----- | ----- | ---- | --- | ------- | ---------- | --- |
| eligibility | rules) | rather | than | broad | intent | recogni- |       |       |      |     |         |            |     |
parameterinRelevance,followedbyGemma3-12B-
tion.
it,thenMistral-7B-v0.3andLlama3-8B.Largerea-
Cross-criterion takeaway. Across criteria, the soningmodels(e.g.,QwQ-32B,Gemma3-27B-it)
|     |     |     |     |     |     |     | trail on | this per-parameter |     |     | metric | despite | strong |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | --- | ------ | ------- | ------ |
proposed8Bmodelisplausibility–andrelevance-
|                                        |     |     |     |     |     |     | absolute | relevance | (Fig. | 5), | indicating |     | diminish- |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | --- | ---------- | --- | --------- |
| competitivewhilelaggingmostonaccuracy. |     |     |     |     |     | The |          |           |       |     |            |     |           |
nextstepsofimprovementisthereforetoprioritize ingreturnsinalignmentperunitcapacityatlarger
scales.
| factual | grounding | and | numeric | checking: |     | adding |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
targetedretrieval,ruletables,andlightweightcal-
|          |        |        |       |     |         |          | Plausibilityefficiency. |     |     | AsshowninFig.7,the |     |     |     |
| -------- | ------ | ------ | ----- | --- | ------- | -------- | ----------------------- | --- | --- | ------------------ | --- | --- | --- |
| culation | guards | should | yield | the | largest | absolute |                         |     |     |                    |     |     |     |
proposed8Bagainleads,withMistral-7B-v0.3and
gainsrelativetoeffort.
|     |     |     |     |     |     |     | Gemma3-12B-it |     | closebehind(virtuallytied), |     |     |     | fol- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------------------- | --- | --- | --- | ---- |
lowedbyLlama3-8B.Thissuggeststhatthedataset
| C.5 | ParameterEfficiency: |     |     | Category-wise |     |     |           |     |          |              |     |       |        |
| --- | -------------------- | --- | --- | ------------- | --- | --- | --------- | --- | -------- | ------------ | --- | ----- | ------ |
|     |                      |     |     |               |     |     | structure | and | few-shot | conditioning |     | yield | coher- |
BordaperBillionParameters
entreasoningwithhighutilitydensity—qualityper
Toevaluateparameterefficiencyratherthanabso-
parameter.
| lute quality,     |     | we compute     | a   | per-parameter |              | utility |                     |     |     |                       |     |     |     |
| ----------------- | --- | -------------- | --- | ------------- | ------------ | ------- | ------------------- | --- | --- | --------------------- | --- | --- | --- |
|                   |     |                |     |               |              |         | Accuracyefficiency. |     |     | InFig.8,theproposed8B |     |     |     |
| foreachcriterion. |     | FormodeliwithP |     |               | i billionpa- |         |                     |     |     |                       |     |     |     |
rametersandmeanrawBordapoints ¯b oncrite- topsAccuracyperparameter,followedbyMistral-
i,c
|        |                                     |     |     |     |     |      | 7B-v0.3 | and Gemma3-12B-it |     |     | (near-tie). |     | Models |
| ------ | ----------------------------------- | --- | --- | --- | --- | ---- | ------- | ----------------- | --- | --- | ----------- | --- | ------ |
| rion c | ∈ {Accuracy,Plausibility,Relevance} |     |     |     |     | (av- |         |                   |     |     |             |     |        |
thatdominateabsoluteaccuracy(Sec.C.4)deliver
eragedoverjudgesandquerieswithinthecategory),
| wedefine |     |     |     |     |     |     | lower accuracy  |     | per parameter, |             | implying |        | that tar- |
| -------- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------- | ----------- | -------- | ------ | --------- |
|          |     |     |     |     |     |     | geted grounding |     | and            | calculation |          | checks | can be    |
¯b
morecost-effectivethanincreasingmodelsize.
| e = | i,c | (Bordapointsperbillionparameters). |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i,c
P
|     | i   |     |     |     |     |     | Takeawaysandcaveats. |     |     | (1)Theproposed8Bis |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------------ | --- | --- | --- |
This ratio captures the marginal productivity of the most parameter-efficient across all three cri-
capacity: howmuchjudgedqualityisobtainedper teria, reinforcing the central claim that careful
183

Figure5: Relevance(meanrawBordapoints). The Figure6: Relevanceefficiency: meanrawBordapoints
proposed8Branksimmediatelybehindthetopthree, perbillionparameters(higherisbetter). Theproposed
aheadofotherbaselines,indicatingconsistentmapping 8Bleads,followedbyGemma3-12B-itandLlama3-8B.
fromuserconstraintstoconcreteanswers.
|                 |        |                |            |     |           | most        | categories | and hovers   | around        | the cohort |
| --------------- | ------ | -------------- | ---------- | --- | --------- | ----------- | ---------- | ------------ | ------------- | ---------- |
| supervision     | can    | substitute     | for scale  | in  | personal- | mean.       |            |              |               |            |
| finance         | tasks. | (2) Efficiency | does       | not | equal ab- |             |            |              |               |            |
|                 |        |                |            |     |           | • Strengths | are        | most visible | in Budgeting, | Em-        |
| solute quality; |        | it informs     | deployment |     | decisions |             |            |              |               |            |
ployment,Planning(andclose-to-meaninInsur-
| wherememory/latencyarebinding. |     |     |     | (3)Theratio |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
ance/Retirement).
| ignores           | runtime | constants | (KV-cache      | bandwidth, |           |     |     |     |     |     |
| ----------------- | ------- | --------- | -------------- | ---------- | --------- | --- | --- | --- | --- | --- |
| batch scheduling) |         | and       | training cost; | it         | should be |     |     |     |     |     |
• WidergapsappearinAuto,Housing,Credit(and
readalongsideabsoluteBordaresultsandsystem- occasionally Investing/Taxes), where locality-
levellatency/memorybudgets. andrule-heavyedgecasesrequiremoreexhaus-
tivecoverage.
C.6 QualitativeCategory-wiseEvaluations
| We analyze |     | twelve | personal-finance |     | subdo- |     |     |     |     |     |
| ---------- | --- | ------ | ---------------- | --- | ------ | --- | --- | --- | --- | --- |
C.6.2 AccuracybySubdomain
| mains—Auto,    |     | Budgeting, | Credit,    | Debt, | Employ-   |                                       |     |     |     |           |
| -------------- | --- | ---------- | ---------- | ----- | --------- | ------------------------------------- | --- | --- | --- | --------- |
|                |     |            |            |       |           | Accuracyisolatesfinancialcorrectness: |     |     |     | adviceand |
| ment, Housing, |     | Insurance, | Investing, |       | Planning, |                                       |     |     |     |           |
calculationsmustberightforthestatedscenario;
| Retirement, | Saving, | Taxes. | For | each, | we report |     |     |     |     |     |
| ----------- | ------- | ------ | --- | ----- | --------- | --- | --- | --- | --- | --- |
styleandcoverageareignored(Sec.C.1).
| criterion-wise                            |       | means | derived from | normalized |            |                 |         |         |               |        |
| ----------------------------------------- | ----- | ----- | ------------ | ---------- | ---------- | --------------- | ------- | ------- | ------------- | ------ |
| Borda points                              | (Sec. | C.3). | The dashed   |            | horizontal |                 |         |         |               |        |
|                                           |       |       |              |            |            | • Absolute      | leaders | are the | larger models | across |
| lineineachpanelmarksthecohort-widemeanfor |       |       |              |            |            | mostsubdomains. |         |         |               |        |
orientation.
• Theproposed8Bmodelismid-packoverall,with
Pleasenotethatthecategory-basedevaluations
competitiveaccuracyinDebt,Planning,Employ-
inthisappendixuserawRedditpostflairs,which
ment,andnotablylargergapsinHousing,Insur-
| differ from         | the | eight thematic | categories |     | curated |                        |     |                   |           |        |
| ------------------- | --- | -------------- | ---------- | --- | ------- | ---------------------- | --- | ----------------- | --------- | ------ |
| forthemainanalysis. |     |                |            |     |         | ance,Taxes(andCredit). |     |                   |           |        |
|                     |     |                |            |     |         | • This pattern         |     | suggests targeted | grounding | (poli- |
C.6.1 RelevancebySubdomain
cy/limittables,calculators)isahigher-leverage
| Relevance | captures | task | alignment: | covering | all |     |     |     |     |     |
| --------- | -------- | ---- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
fixthanstylistictuningforclosingtheremaining
partsoftheuser’srequest,usingtheirnumbers/con-
gap.
straints,andansweringwithoutgenericpreambles
(Sec.C.1).
C.6.3 PlausibilitybySubdomain
• A consistent top cluster is formed by larger Plausibilitymeasuresreasoningflowandreadabil-
reasoning-aligned models. The proposed 8B ity: clearstructure,sensiblesteps,andabsenceof
model sits immediately behind this cluster in unnecessarycomplexity(Sec.C.1).
184

Figure7: Plausibilityefficiency: meanrawBorda Figure8: Accuracyefficiency: meanrawBordapoints
pointsperbillionparameters. Theproposed8Branks perbillionparameters. Theproposed8Btopsthe
first;compact7–8Bbaselinesarecompetitive,while cohort,indicatingthatfactualcalibrationgainscanbe
verylargemodelsshowlowerutilitydensity. achievedmorecheaplythanbyscalingparameters
alone.
• The proposed 8B clusters close to the leaders
Theseresultssuggestprioritizingminimal,high-
acrossmostsubdomains, withstrongerrelative
leverage grounding over further size increases:
showings in Debt and Planning; margins are
include compact, versioned rule/limit tables for
lowerinTaxesandRetirement.
regulation-intensivedomains(e.g.,taxes,insurance,
• Lower margins in regulation-dense areas mir- credit), add lightweight calculators/unit-tests for
rortheaccuracypattern: wherefactsarebrittle, numericsteps,sharpensupervisionwithcontrastive
judgespenalizecircuitousexplanations. edge cases in brittle areas (tax/retirement), diver-
sifyjudgechecks(agreementandjudge-swap),and
extend evaluationto shortmulti-turn interactions
C.7 OverallSummary,Limitations,andNext thatrewardclarifyingquestions.
Steps
D TrainingDetails
Summary. Takentogether,theresultstellasim-
plestory. Onabsolutescores(Sec.C.4),thelargest We fine-tuned the 8B parameter Qwen-3 model
baselines lead across Accuracy, Plausibility, and withAdamWoptimizeronbfloat16precisionand
Relevance, as expected. The proposed 8B model a training split containing 15.6K samples and a
sits just behind this front cluster on Relevance validationsetcontaining2.6ksamples. Wetrained
andPlausibilityandlandsmid-packonAccuracy. themodelforfourepochsusinganoptimalbatch
When we switch to a parameter-efficiency lens sizeof256,resultinginaround220stepsoverall.
(Sec.C.5),thepicturereverses: the8Bmodeldeliv- ThemodelunderwenttrainingonasolitaryA100
ersthehighestBorda-per-parameteracrossallthree GPUwithintheRunpodcloudGPUinfrastructure
metrics, indicating unusually high utility density for3hours.
foritssize. Thesubdomainbreakdown(Sec.C.6)is Wepreservedthreecheckpointsperepoch,with
consistentwithbothviews: the8Bmodelissteady theoptimalvalidationlossattainedatstep101. The
orabove-meanineverydaytaskssuchasBudgeting, trainingusedacosinelearningrateschedulewitha
Planning, Employment (and shows strong plausi- maximumlearningrateof5×10−5,a10%linear
bility in Debt), while gaps widen in regulation- warm-up period of 21 steps (a warmup ratio of
andtable-heavyareassuchasHousing,Insurance, 10%), and a minimum learning rate of 5×10−6.
Taxes,Credit(andoccasionallyAuto/Investing). In Gradientswereconstrainedtoaglobalnormof1,
short, scale drives absolute peaks, but careful su- weightdecaywasestablishedat0.01,andallother
pervisionyieldscompetitivequality—andsuperior parameters adhered to the default conventions of
efficiency—atmid-scale. theHuggingFaceTrainer.
185

Figure9: Category-wiseRelevance. Theproposed8Bmodeltypicallysitsjustbehindtheleadingclusterandnear
thecohortmean;gapsarelargestinedge-case,rule-denseareas(e.g.,Auto,Housing,Credit).
186

Figure10: Category-wiseAccuracy. Largermodelsleadoverall;theproposed8Bismid-packwithsmallergapsin
everydayplanningtasksandlargergapswhereyear-/jurisdiction-specificrulesdominate(e.g.,Housing,Insurance,
Taxes).
187

Figure11: Category-wisePlausibility. Theproposed8Bdeliverscoherentreasoningneartheleadingcluster,with
smallermarginsinroutineplanningtasksandlargeronesinregulation-denseareas(e.g.,Taxes,Retirement).
188

E SampleModelResponses
|     |     |     |     |     | start a side | business, | enjoy | life.” | (Not | tailored | to  |
| --- | --- | --- | --- | --- | ------------ | --------- | ----- | ------ | ---- | -------- | --- |
theuser;repeats“startasidebusiness.
Toprovideaqualitativeassessmentofourmodel’s
Analysis
| capabilities,                                | this appendix               | details | three | compara- |            |          |     |            |     |         |     |
| -------------------------------------------- | --------------------------- | ------- | ----- | -------- | ---------- | -------- | --- | ---------- | --- | ------- | --- |
| tivecasestudies.                             | Eachcaseisstructuredarounda |         |       |          |            |          |     |            |     |         |     |
|                                              |                             |         |       |          | • Judge    | Outcome: |     | Baseline-L | >   | Ours–8B | >   |
| real-worlduserquery,presentingtheabridgedre- |                             |         |       |          | Baseline-S |          |     |            |     |         |     |
sponsesfromourmodel(Ours-8B)alongsidetwo
baselinemodelsofdifferentsizes(Baseline-Land • Reasoning: Baseline-L is the most accu-
|              |          |          |         |            | rate          | and relevant: |            | it adds | specifics | for | the  |
| ------------ | -------- | -------- | ------- | ---------- | ------------- | ------------- | ---------- | ------- | --------- | --- | ---- |
| Baseline-S). | For each | case, we | outline | the query, |               |               |            |         |           |     |      |
|              |          |          |         |            | self-employed |               | (SEP-IRA), |         | provides  | a   | con- |
summarizethecontextprovidedtothemodels,dis-
creteallocationsketch,andoutlinesaclearse-
playthegeneratedresponses,andconcludewitha
judge’sfinalrankingandarationalebasedonthe quence(EF→tax-advantaged→brokerage).
Ours–8Bisstrong,empathetic,andpractical
coreprinciplesofaccuracy,relevance,andplausi-
|     |     |     |     |     | butmorehigh-level. |     |     | Baseline-Sisgenericand |     |     |     |
| --- | --- | --- | --- | --- | ------------------ | --- | --- | ---------------------- | --- | --- | --- |
bility.
poorlytargeted.
CaseC1(Comparative)—Budgeting&Early
CaseC2(Comparative)—FullRoth
Investingat18
ConversionwithMixedPositions
Query(Abridged)
Query(Abridged)
| “I’m 18  | with about $40k | in checking. |                  | I run a |                                    |     |                            |                    |     |     |      |
| -------- | --------------- | ------------ | ---------------- | ------- | ---------------------------------- | --- | -------------------------- | ------------------ | --- | --- | ---- |
|          |                 |              |                  |         | “Early50s,Trad.                    |     | IRAhastwonear-worthlesspo- |                    |     |     |      |
| business | (will reinvest  | some),       | have very        | low ex- |                                    |     |                            |                    |     |     |      |
|          |                 |              |                  |         | sitionsandonelargegainer.          |     |                            | FullRothconversion |     |     |      |
| penses,  | and my parents  | cover        | college/housing. |         |                                    |     |                            |                    |     |     |      |
|          |                 |              |                  |         | wouldpushincomeinthe32–35%bracket. |     |                            |                    |     |     | Con- |
WhatshouldIdosoit’snotjustsittingidle?”
vertallatonceorphaseit?”
ContextTitles(Summary)
ContextTitles(Summary)
• Emergencyfund(3–6monthsofspend)
• Rothconversiontaxation;Form8606report-
ing
• Roth/SEP-IRAbasics
• Bracketmanagementandtiming;liquidityto
• Low-costindexfunds
paytax
• Businessreinvestmentdiscipline
|     |     |     |     |     | • Selling | losers | post-conversion; |     |     | market- |     |
| --- | --- | --- | --- | --- | --------- | ------ | ---------------- | --- | --- | ------- | --- |
volatilityrisk
AbridgedModelResponses
Ours–8B Ihearthemixofexcitementandcon- AbridgedModelResponses
fusion... Since you run a business, reinvest a Ours–8B Full conversion now makes strong
| portion. | For the rest, open | a Roth | IRA | (after-tax, |        |         |        |       |           |         |     |
| -------- | ------------------ | ------ | --- | ----------- | ------ | ------- | ------ | ----- | --------- | ------- | --- |
|          |                    |        |     |             | sense. | Convert | entire | Trad. | IRA, then | immedi- |     |
long-horizongrowth)andataxablebrokeragewith ately sell all three holdings inside the Roth and
low-costindexfunds. Beforeinvesting,hold3–6 reallocatetodiversifiedfunds. Steps: computetax;
monthsofexpensesinahigh-yieldsavingsaccount.
|     |     |     |     |     | execute | direct conversion; |     | sell | & reallocate; |     | file |
| --- | --- | --- | --- | --- | ------- | ------------------ | --- | ---- | ------------- | --- | ---- |
Thenallocateacrossbusiness,RothIRA,andbro-
taxes: reportasa‘non-deductiblecontribution
| keragebasedoncomfortwithrisk. |     |     |     |     | (Form8606)‘. |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Baseline-L(32B) Secureanemergencyfundin Baseline-L(32B) Explainsthattaxesarebased
a high-yield account; consider reinvesting in the on total IRAvalue; lossescan’toffset gainshere.
business with a written plan. As self-employed, Laysoutfullvs. phasedconversion,bracketcreep,
consideraSEP-IRAandRoth/TraditionalIRA.Af- irreversibility,andliquidity(useoutsidefundsfor
terthat,diversifyviaabrokeragewithindexETFs tax). Emphasizesabilitytoliquidateloserstax-free
(e.g., S&P 500). Includes a sample split: emer- inRothandnotesmarket-dropriskpost-conversion.
| gency fund, | business, | retirement | accounts, | and |                        |            |       |      |            |         |     |
| ----------- | --------- | ---------- | --------- | --- | ---------------------- | ---------- | ----- | ---- | ---------- | ------- | --- |
|             |           |            |           |     | Provides               | actionable | steps | (run | scenarios, | convert |     |
| ETFs.       |           |            |           |     | losersfirstifphasing). |            |       |      |            |         |     |
Baseline-S (7B) Ten generic ideas: emergency Baseline-S (7B) High-level overview of Roth
fund, pay off debt, invest in stocks/bonds/real es- conversionbasics;repeatsgeneraladvice;defersto
tate,retirementsavings,education,charity,travel, anadvisor;nobracketmodellingorconcretesteps.
189

| Analysis |     |     |     |     |     |     | Analysis |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
• Judge Outcome: Baseline-L > Ours–8B > • Judge Outcome: Baseline-L > Ours–8B >
| Baseline-S |     |     |     |     |     |     | Baseline-S |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
• Reasoning: Baseline-Lismostaccurateand • Reasoning: Baseline-Lismostaccurateand
relevant: covers bracket spillover, irrevoca- relevant: it answers “am I missing a better
|                               |          |      |     |        |            |            | option?”                           | with | a structured |     | comparison, | con-    |
| ----------------------------- | -------- | ---- | --- | ------ | ---------- | ---------- | ---------------------------------- | ---- | ------------ | --- | ----------- | ------- |
| bility,                       | external | cash | for | taxes, | and        | volatility |                                    |      |              |     |             |         |
|                               |          |      |     |        |            |            | cretetrade-offs,andclearnextsteps. |      |              |     |             | Ours–8B |
| risk,withclearoptions(fullvs. |          |      |     |        | phased)and |            |                                    |      |              |     |             |         |
steps. Ours–8Bisconfidentandpracticalbut is strong and user-aligned but single-track
containsamaterialfilingerror(mislabelsa (HYSAonly),offeringlesseducationaldepth
|            |     |      |                |     |              |     | for alternatives. |     |     | Baseline-S | is  | accurate but |
| ---------- | --- | ---- | -------------- | --- | ------------ | --- | ----------------- | --- | --- | ---------- | --- | ------------ |
| conversion |     | as a | non-deductible |     | contribution |     |                   |     |     |            |     |              |
onForm8606),reducingAccuracy. Baseline- genericandlightondecisionguidance.
Sisgenericandleasthelpful.
Conclusion
CaseC3(Comparative)—Liquidity&Safety Thesecasestudiesculminateinaclear,yetnuanced,
withUncertainHorizon conclusion about the trade-offs between model
Query(Abridged) scale,architecture,andperformance. Theconsis-
tenttoprankingofthe32BBaseline-Lunderscores
| “Lifechangesahead(move/career/school). |     |     |     |     |     | Ihave |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
thevalueofalarge-scalereasoningmodelforgen-
| $25,000andmayneeditanytime. |           |        |            |      | Worriedabout |          |                                            |              |            |         |                  |      |
| --------------------------- | --------- | ------ | ---------- | ---- | ------------ | -------- | ------------------------------------------ | ------------ | ---------- | ------- | ---------------- | ---- |
|                             |           |        |            |      |              |          | eratingsuperior,detailedfinancialguidance. |              |            |         |                  | How- |
| market                      | dips.     | Is a   | high-yield |      | savings      | account  |                                            |              |            |         |                  |      |
|                             |           |        |            |      |              |          | ever, the                                  | most         | compelling | finding | emerges          | from |
| (HYSA)                      | the right | place, | or         | am I | missing      | a better |                                            |              |            |         |                  |      |
|                             |           |        |            |      |              |          | an efficiency                              | perspective. |            | Our     | 8B non-reasoning |      |
option?”
|     |     |     |     |     |     |     | model showed |     | consistent | performance |     | at just a |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ----------- | --- | --------- |
ContextTitles(Summary) quarterofthesizeofBaseline-L.Itis,inessence,
|        |        |     |                |     |     |       | punching | significantly |     | above | its weight | class, of- |
| ------ | ------ | --- | -------------- | --- | --- | ----- | -------- | ------------- | --- | ----- | ---------- | ---------- |
| • HYSA | basics | and | FDIC/coverage; |     |     | money |          |               |     |       |            |            |
feringapowerfulbalanceofqualityandresource
marketaccounts
|     |     |     |     |     |     |     | economy. | The | key differentiators |     | were | Baseline- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------------- | --- | ---- | --------- |
L’sabilitytohandlemulti-step,nuancedreasoning
| • Short   | CDs | and | ladders; | T-bills; |     | short-term |              |         |            |     |         |           |
| --------- | --- | --- | -------- | -------- | --- | ---------- | ------------ | ------- | ---------- | --- | ------- | --------- |
| bondfunds |     |     |          |          |     |            | and maintain | factual | integrity, |     | an area | where our |
modelfalteredinCaseC2.
| • Liquidityvs. |     | yieldtrade-offs;ratemonitoring |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AbridgedModelResponses
| Ours–8B | Given | immediate-access |     |     |     | needs and |     |     |     |     |     |     |
| ------- | ----- | ---------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
principalsafety,parkingtheentire$25kinaHYSA
| isoptimal.    | HYSAspaybetterthanregularsavings, |              |     |     |       |           |     |     |     |     |     |     |
| ------------- | --------------------------------- | ------------ | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
| allow anytime |                                   | withdrawals, |     | and | avoid | CD penal- |     |     |     |     |     |     |
ties. VerifyacompetitiveAPYandkeepthefunds
fullyflexible.
| Baseline-L(32B) |     | ValidatesHYSAforimmedi- |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ateaccess,thencomparesliquid,low-riskalterna-
| tives: money  | market               |            | accounts, | short  |        | CD ladder-  |     |     |     |     |     |     |
| ------------- | -------------------- | ---------- | --------- | ------ | ------ | ----------- | --- | --- | --- | --- | --- | --- |
| ing, T-bills, | and                  | short-term |           | bond   | funds. | Outlines    |     |     |     |     |     |     |
| pros/cons,    | insurance/volatility |            |           | notes, |        | and action- |     |     |     |     |     |     |
ablesteps(openHYSA;optionallyladderasmall
| slice; monitor |     | rates; | named | providers/tickers |     | as  |     |     |     |     |     |     |
| -------------- | --- | ------ | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
examples).
| Baseline-S(7B) |           | ConfirmsHYSAcouldbegood, |         |        |       |       |     |     |     |     |     |     |
| -------------- | --------- | ------------------------ | ------- | ------ | ----- | ----- | --- | --- | --- | --- | --- | --- |
| mentions       | inflation | in                       | general | terms, | lists | money |     |     |     |     |     |     |
marketandshortCDs,butremainsgenericandde-
ferstoanadvisorwithoutacomparisonframework.
190