---
conversion_metadata:
  converted_at: "2026-07-21T14:16:54Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Mienye et al-2026.pdf"
  source_pdf_sha256: "ca154b8acaa81686ba5d2e17c5cb90e88160c7858bdba3a5508f1bf341f95b2d"
  page_count: 29
  markdown_char_count: 195169
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Review
Deep Learning for Credit Risk Prediction: A Survey of Methods,
Applications, and Challenges

Ibomoiye Domor Mienye

, Ebenezer Esenogho *

and Cameron Modisane

Centre for Artificial Intelligence and Multidisciplinary Innovations, Department of Auditing, College of
Accounting Sciences, University of South Africa, Pretoria 0002, South Africa; emienyid@unisa.ac.za (I.D.M.);
modistc@unisa.ac.za (C.M.)
* Correspondence: esenoe@unisa.ac.za

Abstract

Credit risk prediction is central to financial stability and regulatory compliance, guiding
lending decisions and portfolio risk management. While traditional approaches such as
logistic regression and tree-based models have long been the industry standard, recent
advances in deep learning (DL) have introduced architectures capable of capturing complex
nonlinearities, temporal dynamics, and relational dependencies in borrower data. This
study provides a comprehensive review of DL methods applied to credit risk prediction,
covering multi-layer perceptron, recurrent and convolutional neural networks, transformer,
and graph neural networks. We examine benchmark and large-scale datasets, highlight
peer-reviewed applications across corporate, consumer, and peer-to-peer lending, and
evaluate the benefits of DL relative to classical machine learning. In addition, we critically
assess key challenges and identify emerging opportunities. By synthesising methods,
applications, and open challenges, this paper offers a roadmap for advancing trustworthy
deep learning in credit risk modelling and bridging the gap between academic research
and industry deployment.

Keywords:
transformers; machine learning

credit risk prediction; deep learning; convolutional neural networks;

1. Introduction

Credit risk prediction is a fundamental component of financial risk management,
enabling institutions to evaluate the likelihood of borrower default and to make informed
lending decisions [1–3]. Accurate modelling of credit risk supports financial stability,
reduces loan losses, and contributes to regulatory compliance. Traditionally, logistic regres-
sion (LR) has been the dominant model in credit scoring due to its simplicity, interpretability,
and ease of deployment in regulated environments [4]. However, as financial datasets have
grown in size and complexity, conventional LR models have struggled to capture nonlinear
relationships and interactions among features. This limitation has motivated the adoption
of more advanced machine learning (ML) methods such as random forests, support vector
machines (SVMs), and gradient boosting, which often achieve higher predictive accuracy
but at the expense of interpretability [5–7].

Deep learning has broadened credit risk modelling by enabling representation learning
on borrower data that is nonlinear, time-dependent, and sometimes networked. Recent
work explores feed-forward tabular networks, sequence models, attention-based trans-
formers, and graph neural networks to capture signals that are difficult to express in
conventional scorecards [8–10].

Academic Editors: Agnes

Vathy-Fogarassy and János Abonyi

Received: 6 December 2025

Revised: 25 February 2026

Accepted: 27 February 2026

Published: 21 April 2026

Copyright: © 2026 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license.

Information 2026, 17, 395

https://doi.org/10.3390/info17040395

---

<!-- PAGE 2 -->

Information 2026, 17, 395

2 of 28

Alongside these methodological developments, a growing body of survey work has
reviewed credit risk models and related financial risk applications, as summarised in
Table 1. Early systematic reviews by Bhatore et al. [11], Shi et al. [12], Noriega et al. [13], and
Montevechi et al. [14] focus on ML-based credit scoring, synthesising algorithms, datasets,
and evaluation metrics but treating deep neural networks largely as one model family
among many. Other reviews concentrate on specific perspectives: Kim et al. [15] and Çallı
and Co¸skun [16] examine corporate default prediction and long-run default predictors,
while Mhlanga [17] discusses ML- and AI-enabled credit assessment in the context of
financial inclusion. Deep learning-centred surveys, such as Hayashi [18], Peng and Yan [19],
Hoyos et al. [20], and Demma et al. [21], identify emerging DL techniques for credit scoring
and broader financial risk, but mainly emphasise tabular models and do not systematically
cover sequential, transformer, and graph-based architectures for borrower-level credit risk.
Meanwhile, Mienye et al. [22] provided a broad overview of DL in financial services, yet its
treatment of credit risk was at a high-level. In short, much of the review literature either
prioritises broad ML coverage, narrows deep learning discussion to tabular scorecard-style
settings, or treats responsible AI topics without a model-family-level synthesis tailored to
borrower-level credit risk.

This study addresses that gap by organising modern deep learning methods for
borrower-level credit risk prediction, cataloguing recent peer-reviewed applications, and
synthesising deployment-relevant challenges and research opportunities. We focus on
borrower-, facility-, and firm-level settings where the objective is to estimate default-related
outcomes over a specified prediction horizon using application, behavioural, bureau, trans-
actional, textual, or relational data. The primary target is probability of default (PD) and
closely related delinquency outcomes. The reviewed evidence covers consumer lending,
SME lending, corporate credit, and peer-to-peer lending using both public benchmarks
and institution-scale datasets reported in peer-reviewed studies. We exclude work that
focuses on market or liquidity risk, portfolio optimisation without borrower-level labelling,
or purely methodological contributions that do not evaluate on an empirical credit-risk
task. The main contributions of this paper are as follows:

• We present a unified overview of credit risk prediction tasks and benchmark datasets,
and trace the evolution from logistic regression to deep architectures, including MLPs,
CNNs, RNNs, transformers, and GNNs, highlighting how each class aligns with
different credit-risk objectives and data modalities.

• We provide a modality-aware synthesis of recent deep learning applications in credit
risk, organising studies by tabular, sequential, transformer-based, and graph-based
models, and collating their datasets, architectures, and reported performance.

• We critically analyse methodological and operational challenges for deploying DL-
based credit risk models and derive concrete research directions for developing trust-
worthy, regulation-ready deep learning solutions.

The remainder of this paper is organised as follows. Section 2 presents the review
methodology. Section 3 provides an overview of credit risk prediction tasks and commonly
used datasets. Section 4 traces the evolution from statistical to deep learning models,
detailing key architectures. Section 5 reviews peer-reviewed DL applications in credit
risk across data modalities. Section 6 presents a synthesis of major challenges and future
research directions. Section 7 concludes the paper.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 3 -->

Information 2026, 17, 395

3 of 28

Table 1. Summary of related reviews on credit risk modelling and financial risk prediction.

Study

Year

Scope

Valdrighi et al. [23]

2025

Best practices for responsible ML in credit scoring, covering fairness, explainability,
and governance.

Paz et al. [24]

2025

Systematic review of ML and metaheuristics for individual credit risk assessment.

Alvi et al. [25]

2024

Systematic review of default prediction ML models and their role in strengthening
credit risk management.

Montevechi et al. [14]

2024

Comprehensive review of state-of-the-art ML models for credit risk.

Demma Wube et al. [21] 2024

Review of ML and DL techniques for credit scoring.

Noriega et al. [13]

2023

Systematic review of ML methods for credit risk prediction, with emphasis on algo-
rithms, datasets, and performance metrics.

Bhattacharya et al. [26] 2023

Comprehensive study of credit risk evaluation methods, including statistical and ML
models.

Hoyos et al. [20]

Hayashi [18]

Shi et al. [12]

2023

2022

2022

Systematic review of DL-based credit risk assessment systems, summarising architec-
tures, application settings, and evaluation measures.

Review of emerging trends in DL for credit scoring, focusing on neural network
architectures, feature learning, and interpretability.

A survey of ML-driven credit risk, organising algorithms, data sources, and evaluation
methods.

Çallı and Co¸skun [16]

2021

Longitudinal systematic review of credit risk assessment and default predictors.

Mhlanga [17]

2021

Review of ML for credit risk assessment in the context of financial inclusion in
emerging economies.

Peng and Yan [19]

2021

Survey of DL for financial risk prediction across multiple tasks, with credit risk as
one application area.

Gunnarsson et al. [27]

2021

Empirical study on when DL is beneficial for credit scoring, practical adoption, and
comparison with traditional scoring.

Bhatore et al. [11]

2020

Systematic review of ML techniques for credit risk evaluation, covering classifiers,
feature selection, and benchmark datasets.

Kim et al. [15]

2020

Literature review of corporate default prediction models, summarising statistical and
ML approaches.

2. Review Methodology

We conducted a structured literature search and screening exercise to assemble recent
peer-reviewed work on deep learning for borrower-level credit risk prediction. The goal
is a comprehensive and transparent narrative synthesis of the field rather than a formal
systematic review or meta-analysis.

To cover both computing and finance outlets, we searched IEEE Xplore, Scopus, ACM
Digital Library, ScienceDirect, SpringerLink, Web of Science, and Google Scholar. Web
of Science was included to broaden coverage of finance and operations research venues
that are not always well represented in engineering-focused indexes. Queries paired
credit-risk terms (e.g., credit scoring, default prediction, probability of default) with deep
learning terms (e.g., CNN, RNN, LSTM, GRU, Transformer, graph neural network). Where
supported, we restricted searches to title/abstract/keywords and refined query variants
iteratively using highly cited seed papers to limit irrelevant returns. We targeted journal
articles and full conference papers from 2015 to 2025, and added foundational earlier
studies via backward/forward citation tracking.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 4 -->

Information 2026, 17, 395

4 of 28

Search Strategy and Screening Protocol

The initial search identified approximately 380 records across all databases after merg-
ing results. Duplicate records were removed using title, author, venue, and year matching.
Following de-duplication and removal of clearly out-of-scope records, 208 studies were
retained for title and abstract screening, as summarised in Figure 1. The remaining studies
were screened in two stages: (i) title and abstract screening, followed by (ii) full-text assess-
ment. During title and abstract screening, studies were excluded if they focused exclusively
on market or liquidity risk, macroeconomic default modelling without borrower-level
prediction, or methodological deep learning contributions without an empirical credit risk
application. Full-text screening was then used to confirm relevance, extract methodological
details, and verify that the study addressed borrower-, facility-, or entity-level credit risk.

Figure 1. PRISMA flowchart of the literature search and screening process used in this survey. The
diagram summarises database querying, de-duplication, title and abstract screening, and full-text
eligibility assessment.

Studies were included if they satisfied at least one of the following criteria: (i) proposed
or empirically evaluated a deep learning architecture for credit risk prediction; (ii) provided
a survey or structured review of machine learning or deep learning methods for credit
risk; or (iii) addressed interpretability, fairness, robustness, or governance explicitly in a
credit risk context. Meanwhile, studies were excluded if they lacked quantitative evalu-
ation, provided insufficient methodological detail to assess the learning architecture, or
focused solely on regulatory or policy discussion without a modelling component. Unlike
systematic reviews, no strict performance-improvement threshold was imposed; how-
ever, studies were required to report at least one standard evaluation metric to support
empirical comparison.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 5 -->

Information 2026, 17, 395

5 of 28

The final corpus comprises 140 deep learning application studies and 18 survey or
guideline papers. For each included study, we recorded the data modality (tabular, sequen-
tial, textual, or relational), model architecture (MLP, CNN, RNN/LSTM/GRU, Transformer,
GNN, or hybrid), credit product segment (consumer, SME, corporate, interbank, or mixed),
prediction target, and reported evaluation metrics. We did not apply a formal risk-of-bias
scoring protocol (given the non-systematic scope and heterogeneous study designs), but we
extracted reporting attributes relevant to interpretability, validation design (e.g., out-of-time
vs random splits), and deployment considerations where available. These attributes under-
pin the taxonomy used in Sections 4 and 5, and the related survey literature is summarised
in Table 1.

3. Overview of Credit Risk Prediction and Datasets

Credit risk refers to the potential loss that a lender or investor faces when a borrower
fails to meet contractual financial obligations [17]. Accurate credit risk prediction is funda-
mental to financial stability, guiding capital allocation, pricing, and provisioning decisions
under regulatory frameworks such as Basel III. Traditionally, credit risk has been assessed
through statistical scorecards and expert judgment; however, the rise of data-driven lending
and digital credit platforms has produced large-scale, high-dimensional borrower data
that demand more advanced modelling approaches. This section provides an overview of
the key predictive tasks in credit risk management and summarises benchmark datasets
commonly employed in empirical studies.

3.1. Credit Risk Prediction Tasks

Credit risk prediction aims to estimate the likelihood and magnitude of potential
losses associated with lending activities. In regulatory and research practice, three main
quantitative tasks are typically addressed:

•

•

•

Probability of Default: The likelihood that a borrower will fail to meet contractual
repayment obligations within a specified horizon. PD modelling forms the foundation
of most credit scoring systems and risk-based pricing frameworks [28].
Loss Given Default (LGD): The proportion of the exposure that is not recovered in the
event of default, reflecting collateral values, recovery processes, and legal costs [29].
Exposure at Default (EAD): The total outstanding amount a lender is exposed to when
default occurs, which is particularly important for revolving facilities such as credit
cards and overdrafts [30].

Across the reviewed literature, PD-style targets (default or closely related delinquency
outcomes) dominate, and they form the primary basis for comparing deep learning model
families in this survey. Prediction horizons and label definitions vary across studies and
products; where reported, we capture these details in the study summaries to support
consistent interpretation. LGD and EAD are discussed only in studies that explicitly
model them using deep architectures, reflecting their comparatively limited coverage in
the deep learning credit-risk literature. These quantities determine the Expected Loss (EL),
a cornerstone of risk-weighted asset (RWA) calculation in Basel frameworks, defined as:

EL = PD × LGD × EAD.

(1)

Though EL is crucial in credit risk, it is inconsistently reported and is not comparable
across heterogeneous datasets and horizons in the surveyed studies. Accordingly, the
synthesis in Section 5 focuses on the evaluation metrics most commonly reported for
PD-style prediction.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 6 -->

Information 2026, 17, 395

6 of 28

3.2. Benchmark Datasets

Empirical research on credit risk frequently relies on benchmark datasets to evaluate
and compare modelling approaches. The most widely used public datasets include the
German Credit, Australian Credit, and Taiwan Credit Card Default datasets, which have
become standard baselines for ML algorithms. The German Credit dataset, compiled by
the UCI ML Repository, contains 1000 loan applicants with 20 demographic and financial
attributes labeled as good or bad credit risk [31]. The Australian Credit dataset is smaller,
comprising 690 records with mixed categorical and numerical features for binary credit-
worthiness classification. The Taiwan Credit Card Default dataset is substantially larger,
featuring 30,000 clients with detailed billing, repayment, and demographic information,
and is widely used in deep learning benchmarks [32].

While these datasets facilitate reproducibility and algorithmic comparison, their lim-
ited sample sizes, static structures, and lack of temporal or behavioural features constrain
generalisability to real-world portfolios [33]. Small benchmarks also create high-variance
evaluation regimes in which apparent performance differences are unstable and can be
driven by a few influential cases rather than a durable risk signal. For example, with
only 1000 observations, the German Credit dataset can yield materially different estimates
across random splits, and high-capacity models may overfit idiosyncratic correlations that
do not transfer to new borrower cohorts. This effect is compounded by sample-selection
mechanisms that are absent or unobserved in public benchmarks (e.g., lender acceptance
policies and underwriting rules), meaning the observed labels may reflect a filtered sub-
population rather than the full applicant pool. Consequently, models trained and reported
on such datasets often overestimate out-of-sample performance and understate uncertainty
in comparative claims.

To address these shortcomings, contemporary studies increasingly adopt larger and
more heterogeneous datasets. For example, the Home Credit Default Risk dataset [34]
includes over 300,000 loan applications enriched with demographic, behavioural, and
bureau records, representing a closer approximation to industrial settings. Similarly, the
Lending Club peer-to-peer lending dataset contains millions of transactions and repayment
records, enabling large-scale evaluations of ensemble and deep learning models [35].

Despite these advances, much of the academic literature continues to rely on small,
static benchmarks that fail to capture macroeconomic shifts and dynamic borrower be-
haviour. Bridging this gap requires longitudinal, multimodal datasets with explicit time
structure and stable label definitions, so that models can be evaluated under out-of-time val-
idation and assessed for drift, calibration decay, and subgroup performance. Such datasets
are essential for benchmarking emerging deep learning architectures under realistic and
regulatory-compliant conditions (Table 2).

Table 2. Summary of Benchmark Datasets Commonly Used in Credit Risk Prediction.

Dataset

Sample Size

Features

Description

German Credit

Australian Credit

1000

690

Taiwan Credit Card Default

30,000

Home Credit Default Risk

300,000+

Lending Club

Millions

20

14

24

122

100+

Demographic and financial attributes with binary
good/bad credit labels.

Mixed categorical and numerical features for
creditworthiness classification.

Client payment history, billing amounts, and demographics.

Realistic industrial dataset combining behavioural and
bureau information.

Peer-to-peer lending records, including loan, borrower, and
repayment details.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 7 -->

Information 2026, 17, 395

7 of 28

4. Evolution of Models for Credit Risk

Credit risk modelling has progressed from interpretable linear methods to deep archi-
tectures that capture nonlinear interactions, sequential behaviour, and relational dependen-
cies among borrowers. This section reviews the methodological evolution across the main
model families.

4.1. Logistic Regression and Classical Machine Learning

Logistic regression (LR) remains the cornerstone of credit scoring due to its trans-
parency and regulatory acceptance [36,37]. Given input features x ∈ Rd and parameters
(w, b), LR models the probability of default as:

P(y = 1 | x) = σ(w⊤x + b) =

1
1 + exp(−w⊤x − b)

,

(2)

where σ(·) is the logistic sigmoid and y ∈ {0, 1} denotes default status. Despite its sim-
plicity, LR assumes a linear log-odds relationship, limiting its ability to capture nonlinear
feature effects and interactions in high-dimensional data. Subsequent classical ML models,
such as support vector machines, random forests, and gradient boosting, enhanced flexibil-
ity by learning nonlinear decision boundaries. These methods typically outperform LR in
accuracy but at the cost of interpretability, motivating subsequent research into models that
balance both properties [5].

4.2. Early Deep Learning for Tabular Credit Risk

The introduction of deep learning brought neural architectures capable of learning
complex, nonlinear transformations directly from tabular credit data. Unlike traditional
logistic regression (LR), which models linear relationships, deep neural networks can
capture hierarchical feature interactions through multiple hidden layers. A multi-layer
perceptron (MLP), illustrated in Figure 2, extends LR by stacking hidden layers with
nonlinear activations that enable the automatic extraction of latent feature representations.
Mathematically, the forward propagation in an MLP is given by:

h(l) = ϕ(W(l)h(l−1) + b(l)),

(3)

where ϕ(·) denotes a nonlinear activation function such as ReLU. This hierarchical structure
allows MLPs to approximate complex functions on large datasets, thereby uncovering
nonlinear relationships between borrower characteristics and default probabilities [38].

Figure 2. Basic structure of a feed-forward neural network used for tabular credit data. The network
consists of an input layer, one or more hidden layers with nonlinear activations, and an output layer
for default prediction.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 8 -->

Information 2026, 17, 395

8 of 28

4.3. Sequential and Temporal Behaviour Modelling

Creditworthiness evolves over time as borrowers make repayments, accumulate bal-
ances, adjust spending behaviour, or experience income fluctuations. Sequential neural
networks explicitly model these behavioural trajectories by capturing temporal dependen-
cies that static models cannot. These architectures process credit-related sequences—such
as monthly repayment histories, rolling utilisation rates, or delinquency transitions—in a
step-wise manner, enabling the extraction of long-range behavioural patterns. Recurrent
neural networks (RNNs) form the foundation for sequential modelling. At each time step t,
an RNN updates its hidden state according to

ht = tanh(Whht−1 + Wxxt + b),

(4)

where xt is the input vector at time t, ht is the hidden state, Wh and Wx are learnable weight
matrices, and b is a bias term. Although RNNs can capture short-term temporal structure,
they struggle with long-range dependencies due to vanishing gradients [39].

4.3.1. Long Short-Term Memory Networks

To address the limitations of standard RNNs, long short-term memory (LSTM) net-
works introduce gating mechanisms that regulate information flow and preserve long-term
temporal patterns. The LSTM architecture (Figure 3) uses three gates—forget, input, and
output—to update an internal memory cell Ct:

ft = σ(Wf [ht−1, xt] + b f ),
it = σ(Wi[ht−1, xt] + bi),
˜Ct = tanh(Wc[ht−1, xt] + bc),
Ct = ft ⊙ Ct−1 + it ⊙ ˜Ct,
ot = σ(Wo[ht−1, xt] + bo),

ht = ot ⊙ tanh(Ct),

(5)

(6)

(7)

(8)

(9)

Here, the hidden state and cell state are denoted by ht and Ct, respectively, and xt is the
input vector at time step t. The gates ft, it, and ot control forgetting, updating, and output,
while ˜Ct denotes the candidate cell update. σ(·) is the sigmoid activation function and ⊙
denotes elementwise multiplication [40].

Figure 3. Architecture of the LSTM network showing gating mechanisms for input, forget, and
output regulation.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 9 -->

Information 2026, 17, 395

9 of 28

4.3.2. Gated Recurrent Unit Networks

The gated recurrent unit (GRU), illustrated in Figure 4, simplifies the LSTM architec-
ture by using a single state variable and two gates. GRUs compute their hidden state using:

zt = σ(Wz[ht−1, xt] + bz),
rt = σ(Wr[ht−1, xt] + br),
˜ht = tanh(Wh[rt ⊙ ht−1, xt] + bh),
ht = (1 − zt) ⊙ ht−1 + zt ⊙ ˜ht,

(10)

(11)

(12)

(13)

where xt is the input vector at time step t and ht is the GRU hidden state. The vectors zt and
rt denote the update and reset gates, respectively, and ˜ht is the candidate hidden state [39].

Figure 4. Architecture of the GRU network, highlighting the update and reset gates that control
information flow across time steps.

4.3.3. Temporal Convolutional Networks

Temporal convolutional networks (TCNs) offer an alternative to recurrent architectures
by applying one-dimensional dilated convolutions to capture long-range dependencies
without recursion:

ht =

K−1
∑
k=0

Wk xt−d·k,

(14)

where d denotes the dilation factor and K the kernel size [41]. Unlike RNNs and LSTMs,
TCNs process sequences in parallel, preserving causality through zero-padding while
enabling efficient training on long temporal windows [42,43]. This property makes TCNs
particularly valuable for high-frequency repayment data and real-time transaction streams
where parallel computation and long-horizon forecasting are advantageous.

4.4. Convolutional and Hybrid Architectures

CNNs, though historically associated with image processing, have become effective
tools for modelling structured financial sequences [44]. In credit risk, one-dimensional
convolutions slide learnable filters over borrower histories—capturing local temporal pat-
terns such as consecutive delinquencies, abrupt utilisation jumps, or irregular repayment
intervals. These filters extract short-range behavioural motifs while sharing parameters
across time steps, yielding models that are both computationally efficient and less prone

https://doi.org/10.3390/info17040395

---

<!-- PAGE 10 -->

Information 2026, 17, 395

10 of 28

to overfitting than dense architectures. Figure 5 illustrates this structure, where con-
volutional and pooling layers form hierarchical representations of borrower behaviour
before classification.

Figure 5. Basic CNN architecture adapted for one-dimensional financial sequences. Convolutional
and pooling layers capture local repayment or utilisation patterns, which are then passed to dense
layers for classification.

Several studies report that CNN-based sequence encoders are competitive with re-
current architectures in credit-risk sequence modelling when local behavioural patterns
dominate the signal, while offering faster training due to parallelism [44,45]. Their par-
allelism offers significant speed advantages for large portfolios, and their stable train-
ing dynamics make them well suited for industrial settings where rapid retraining and
consistent convergence are required. This has motivated hybrid credit-risk models that
integrate CNN modules with other deep architectures. Wide–deep networks combine
a linear branch—reflecting scorecard-style interpretability—with nonlinear deep compo-
nents that capture higher-order interactions. Other hybrids, such as CNN–LSTM and
CNN–Transformer models, leverage convolutions to encode short-term behaviour before
passing features to recurrent or attention-based layers to capture long-range dependen-
cies. These designs offer a practical balance between interpretability, expressive capac-
ity, and computational scalability, making them increasingly relevant in modern credit
risk pipelines.

4.5. Transformer

Transformer architectures introduce a fundamentally different approach to modelling
sequence and tabular credit data by replacing recurrence with self-attention, enabling the
capture of global dependencies in parallel rather than stepwise [46]. Instead of processing
borrower histories chronologically, as RNNs do, the transformer computes pairwise inter-
actions across all feature dimensions or time steps simultaneously. The core self-attention
mechanism is defined as:

Attention(Q, K, V) = softmax

(cid:32)

(cid:33)

V,

QK⊤
√
dk

(15)

https://doi.org/10.3390/info17040395

---

<!-- PAGE 11 -->

Information 2026, 17, 395

11 of 28

where Q, K, and V denote the query, key, and value matrices representing latent projections
of input features or time steps, and dk is a scaling constant to stabilise gradients. This
formulation enables the model to assign adaptive relevance weights across the entire
behavioural sequence, allowing it to capture long-range delinquency signatures, cyclical
utilisation trends, and cross-feature interactions that traditional recurrent networks struggle
to retain.

Recent adaptations demonstrate how transformers can be repurposed from natural
language processing to structured financial learning. TabTransformer [47] contextualises
categorical embeddings, improving discrimination on tabular credit datasets with high-
cardinality socio-economic attributes.

4.6. Graph Neural Networks

Borrowers often participate in interdependent financial ecosystems through co-
applicant ties, shared employers, guarantor structures, fund-flow relationships, or supply-
chain linkages. These relational patterns give rise to correlated credit exposures and
potential contagion pathways that cannot be represented in i.i.d. tabular data. Graph
neural networks (GNNs) model such relational dependencies via iterative message passing,
where each node updates its representation by aggregating transformed messages from
neighbouring nodes. The generic update rule for a message-passing layer is expressed as


 ∑

= σ

(l+1)
v

h

u∈N (v)



W(l)h

(l)
u

,

1
cvu

(16)

(l)
v

is the embedding of borrower v at layer l, N (v) denotes neighbouring nodes (e.g.,
where h
borrowers, firms, accounts, or counterparties connected through ownership, transactions,
or contractual ties), cvu is a normalisation coefficient (e.g., node degree), W(l) is a learnable
weight transform, and σ(·) is a nonlinear activation. Figure 6 visualises this pipeline:
neighbours send learned messages, the messages are pooled, and the central borrower
embedding is updated to reflect relational credit risk factors.

Figure 6. Message passing mechanism in a GNN for borrower networks. Neighbouring borrower
representations are collected, aggregated, and used to update each node, enabling propagation of
financial influence signals.

Table 3 summarises the various DL architectures for credit risk modelling.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 12 -->

Information 2026, 17, 395

12 of 28

Table 3. Summary of deep learning architectures discussed for credit risk modelling.

Model Class

Input Modality

Core Mechanism

Credit-Risk Strengths

Key Limitations

MLP

CNN

Tabular features

Feed-forward non-linear
transformation

Sequential/behavioural
time-series

Local shared-weight
convolutions with pooling

Recurrent Models (RNN,
LSTM, GRU)

Temporal behavioural
sequences

Hidden state propagation
with gating

Transformers

Tabular or sequential data

Global multi-head
self-attention, contextual
embeddings

Learns complex
interactions beyond
linear scorecards; scalable
and easy to deploy

Detects repayment and
utilisation motifs; efficient
training and parallelisable

Models long-term
delinquency, repayment
evolution, and
behavioural drift

Captures global
temporal/feature
interactions; scalable
training; interpretability
via attention

No temporal or relational
reasoning; feature
engineering required

Captures only local
temporal patterns;
struggles with long-range
dependencies

Training cost increases
with long sequences;
vanishing gradients;
limited parallelism

Requires larger data
volume and tuning; less
effective on tiny datasets

GNNs

Relational borrower
networks

Iterative message passing
and neighbour
aggregation

Models contagion effects,
systemic dependencies,
and hidden risk
propagation

Requires graph
construction; sensitive to
noise and missing
relationships

Hybrid Architectures (e.g.,
CNN–LSTM)

Heterogeneous data
(tabular, text, sequence,
network)

Combined feature
extractors and fusion
layers

Balances interpretability,
scalability, and
multimodal learning;
strongest performance on
real-world data

Increased complexity;
harder to interpret and
validate for regulation

5. Notable DL Applications in Peer-Reviewed Credit Risk Studies

This section synthesises peer-reviewed applications of deep learning to credit risk. We
map empirical studies to the same three axes: modality, architecture, and objective, and
report the evaluation metrics they used and the quantitative performance obtained.

5.1. Tabular Deep Networks for Credit Risk

Deep learning for tabular borrower data has evolved from simple multilayer per-
ceptrons (MLPs) to specialised architectures that leverage regularisation, attention, em-
beddings, and hybrid ensembling. This subsection reviews representative studies that
apply deep tabular models to corporate, retail, and institutional lending data, highlighting
methodological contributions, empirical findings, and comparative performance relative to
conventional ML models.

Yang et al. [48] proposed a high-dimensional deep neural network (HDNN) for corpo-
rate credit risk using supply-chain augmented financial data. Their model incorporated
combined L1–L2 penalties to address feature sparsity and batch-normalisation effects,
achieving an accuracy of 80.12%, outperforming logistic regression (area under the receiver
operating characteristic curve (AUC) = 0.717), support vector machines (AUC = 0.738), and
a standard neural network baseline (AUC = 0.692). Lin et al. [49] introduced a penalised
deep neural network (PDNN) based on survival modelling, embedding a one-to-one pe-
nalisation layer that supported variable selection alongside time-to-default estimation on
peer-to-peer lending data, consistently outperforming non-penalised deep variants.

Recent studies have further examined interpretability and profit-aware optimisation
within deep tabular learning. Asencios et al. [50] compared MLP, XGBoost, and TabNet
on 36,402 Peruvian cooperative-lending applications using regression-based profit scor-
ing. XGBoost achieved the best results (R2 = 0.7906), although TabNet (R2 = 0.7465)
offered more transparent feature-level interpretability through attentive embeddings. In
large-scale settings, Wang and Zhang [51] proposed a TabNet-Stacking ensemble that inte-

https://doi.org/10.3390/info17040395

---

<!-- PAGE 13 -->

Information 2026, 17, 395

13 of 28

grated TabNet, XGBoost, LightGBM, CatBoost, SVM, and KNN, reaching accuracy = 0.979,
recall = 0.856, F1 = 0.817, and AUC = 0.941 on the Tianchi dataset (≈800,000 cases), sub-
stantially outperforming single-model baselines.

Beyond architecture design, explainability has become central to tabular deep learning
deployment. Hjelkrem and de Lange [52] trained an MLP using open banking transac-
tion data and compared it with a bidirectional encoder representations from transformers
(BERT)-based model, reporting that the MLP achieved superior predictive performance
while maintaining practical explainability using SHAP attribution visualisations. Their
results showed that SHAP detected intuitive behavioural risk factors, supporting suitability
for regulated financial settings. Li et al. [53] introduced an incremental DNN (I-DNN) for
borrower credit scoring on agricultural microloan records (22,475 examples), demonstrat-
ing AUC improvements ranging between 1.4% and 7.8% compared with standard DNN,
XGBoost, and random forest baselines under concept drift scenarios.

Advances in deep tabular modelling have also explored ensemble-driven generalisa-
tion. Popov et al. [54] introduced Neural Oblivious Decision Ensembles (NODE), replacing
discrete tree splits with differentiable soft-gating, producing competitive performance
with gradient boosting while enhancing differentiability and calibration under stochastic
optimisation. Building on ensemble reasoning, Shan and Gao [55] proposed an enhanced
TabNet stacking model for SME supply-chain financial risk prediction using multi-stage
optimisation, achieving AUC = 0.9616 and Accuracy = 0.9277, outperforming standard
TabNet, LightGBM, and CatBoost baselines.

These works demonstrate that tabular DL has advanced from simple feed-forward net-
works toward architectures that integrate regularization, attention, and ensemble learning.
Overall, these studies suggest that deep tabular models are often competitive with strong
tree-based ensembles on larger datasets, particularly when the feature space includes
high-cardinality categorical variables, complex interactions, or multimodal extensions
that benefit from representation learning. On smaller benchmarks, reported gains are
frequently modest and can be sensitive to split design and tuning, meaning gradient
boosting remains a strong and frequently hard-to-beat baseline. Deep networks therefore
complement rather than replace classical methods, with their main advantage arising when
data scale, heterogeneity, or unified multimodal pipelines justify the added modelling and
operational complexity.

5.2. Sequential Models and Event–Time Targets

Sequential deep learning approaches model the evolution of borrower or portfolio
behaviour over time, offering substantial advantages over static classifiers that ignore
risk trajectories. These models capture temporal patterns linked to repayment behaviour,
behavioural drifts, cyclical spending, macroeconomic shocks, and post-origination delin-
quency paths. Compared with conventional panel regression and tree-based models,
sequential architectures integrate information across ordered observations and enable
dynamic probability-of-default estimation rather than static, single-point predictions.

Liang and Cai [56] applied long short-term memory (LSTM) networks to forecast
monthly default rates on the Lending Club peer-to-peer platform. The LSTM consistently
outperformed ARIMA, SVM, and ANN across multiple cross-validation schemes, reducing
MAE from 0.095 to 0.072 and RMSE from 0.119 to 0.093. Further support for recurrent
credit modelling appears in Ala’raj et al. [57], who developed two behavioural LSTM
variants (MP–LSTM and PE–LSTM) for real retail banking credit card customers. Their
models surpassed SVM, RF, MLP, and LR baselines across predictive and calibration metrics,
demonstrating that temporal representation learning enhances behavioural default scoring
in operational settings.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 14 -->

Information 2026, 17, 395

14 of 28

Beyond standard LSTMs, hybrid deep temporal architectures have gained promi-
nence. Zhang [58] proposed a CNN–LSTM attention model for enterprise credit risk,
achieving AUC = 0.92 and F1 = 0.91, outperforming CNN- and LSTM-only baselines.
Li et al. [59] extended this approach for listed corporate risk and reported that CNN layers
effectively extract short-term temporal motifs, while LSTM components encode longer be-
havioural transitions, confirming that hierarchical temporal modelling improves enterprise
credit discrimination.

Survival-driven architectures further generalise temporal credit modelling by estimat-
ing hazard rather than static outcomes. Wang et al. [60] implemented a deep discrete-time
survival model that decomposes credit outcomes into age, period, and cohort dimensions,
generating interpretable hazard curves with a smoother temporal structure than classical
econometric approaches. Chen and Long [61] similarly advanced temporal modelling
through a self-attention-based end-to-end corporate credit rating framework, which re-
moved the need for manual feature aggregation and improved rating classification stability
relative to traditional ML competitors.

More recent developments incorporate fusion and cross-feature interaction within
sequential networks. Han et al. [62] introduced a default-prediction framework com-
bining self-attention with a cross-network mechanism, demonstrating that modelling
interactive temporal dependencies yields higher accuracy, precision, recall, and F1-score
relative to standard deep learning architectures. Shi et al. [63] also benchmarked CNN,
RNN, and DNN models in financial-sector credit scoring and observed that recurrent
architectures maintained superior temporal sensitivity, while CNNs provided parameter
efficiency benefits.

Bidirectional and residual-enhanced architectures have been explored to stabilise
recurrent training and preserve long-range gradients. Yang et al. [64] introduced a residual-
enhanced bidirectional long short-term memory (BiLSTM) framework incorporating multi-
head attention, achieving AUC = 0.982 and F1 = 0.958 on the Freddie Mac Single-Family
dataset, outperforming BiLSTM, GRU, CNN, and RNN baselines. Complementary research
explores coupling sequential encoders with probabilistic reasoning: Zhang [65] integrated
LSTM encoders with Bayesian calibration modules, achieving AUC = 0.981 and reducing
uncertainty miscalibration relative to RF and LR baselines.

These results indicate that sequential architectures are most valuable when lenders
possess rich post-origination histories or portfolio-level time series and care about how risk
evolves, not just whether a borrower eventually defaults. LSTM- and GRU-like models
offer clear gains for dynamic behavioural scoring and vintage-level forecasting, while
CNN–LSTM hybrids and survival-based networks help bridge the gap between point
predictions and time-to-event outcomes. However, the empirical lift over strong tabular
baselines tends to appear only when sequences are sufficiently long and informative;
on static benchmarks with limited behavioural content, sequential models mainly add
complexity without delivering commensurate practical benefit.

5.3. Transformer-Based Models for Credit Risk

Transformers represent a major departure from recurrent architectures by replacing
sequential recurrence with self-attention, enabling parallel computation and global depen-
dency modelling across features, time steps, or modalities [46]. The key mechanism, scaled
dot-product attention, allows each element in a sequence or feature vector to condition on
all others, overcoming long-term dependency limitations typical of LSTMs and GRUs. This
property is attractive in credit modelling, where behavioural variables, categorical features,
and text-based signals interact in complex, non-local patterns.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 15 -->

Information 2026, 17, 395

15 of 28

Early adoption has focused on adapting the transformer encoder to tabular and be-
havioural credit data. Huang et al. [47] introduced the TabTransformer, demonstrating
performance gains on high-cardinality categorical financial datasets by replacing conven-
tional one-hot encodings with contextual embeddings. Gorishniy et al. [66] later improved
architectural efficiency with the FT-Transformer, showing that attention-based tabular
models can be competitive with strong tree-ensemble baselines such as CatBoost and XG-
Boost on several tabular tasks, particularly when feature interactions are complex and
heterogeneously distributed. Wang and Xiao [67] extended this paradigm by embedding
behavioural sequences alongside static features, achieving AUC = 0.72 and KS = 0.32 on an
online lending dataset, outperforming both LSTM and XGBoost baselines.

Recent work has started to specialise transformer architectures for different segments
of the credit market. Korangi et al. [68] framed mid-cap corporate default prediction as
a multi-label panel classification task, using a transformer to learn the term structure of
default probabilities over horizons from a few months to three years. Their multi-channel
design ingests accounting, pricing, and market variables and applies a task-specific loss for
multi-horizon default prediction, yielding sizeable AUC improvements over traditional
statistical and LSTM-based benchmarks. Li et al. [69] proposed HFTCRNet, a hierarchical
fusion transformer for interbank credit rating and systemic risk assessment. The model
combines a long-term temporal transformer for bank growth trajectories, a short-term
cross-graph transformer for dynamic interbank exposures, and an attentive contagion
module, trained in a semi-supervised fashion using both credit ratings and SRISK labels.
On a dataset of 4548 banks with quarterly balance sheets and network data, HFTCRNet
outperformed deep and non-deep baselines in rating accuracy while also capturing systemic
risk patterns in the interbank network.

In the retail and SME space, transformer-based models have been applied to both
tabular and sequential credit signals. Kakadiya et al. [70] investigated transformer archi-
tectures for bank loan default prediction and reported performance gains over logistic
regression and tree-based methods, arguing that self-attention captures higher-order de-
pendencies among financial variables that are missed by conventional models. Zhang and
Liang [71] proposed a minimum weighted value error combination model that integrates a
BERT-based transformer for temporal features with DNN and MLP components for static,
non-sequential attributes. Features are first selected using chi-square tests and gradient
boosting decision trees, and the final prediction is obtained by dynamically weighting the
sequence and non-sequence experts according to an improved minimum weighted error
criterion. Experiments on personal credit data showed that the combined model achieves
higher classification accuracy than any individual transformer or feed-forward baseline.

Addressing class imbalance and transparency, Hartomo et al. [72] introduced a
weighted-loss TabTransformer with integrated explainable AI for MSME and consumer
credit datasets. Using cost-sensitive weighting, their model improved accuracy on the BI-
SAID and German Credit datasets from 86.35% to 89.27% and from 93% to 95%, respectively,
while also boosting minority-class AUC and precision–recall. SHAP-based explanations
highlighted economically meaningful drivers such as financing needs and credit amount,
illustrating how attention-based tabular models can be combined with explainable AI
(XAI) to support more accountable decision-making. Wu [73] developed a BiLSTM-fused
transformer for enterprise financial risk identification within a blockchain-based financial
sharing platform. The model jointly processes textual and visual financial information to
classify firms into five risk levels and, in experiments, achieved risk identification accuracy
above 94% with AUC exceeding 0.95, outperforming baseline RNNs while operating on
securely shared financial records.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 16 -->

Information 2026, 17, 395

16 of 28

Textual transformers have also gained prominence where loan assessments, credit
memos, and SME narratives remain human-authored. Stevenson et al. [74] showed that
BERT-derived embeddings from lender-written documents produced competitive default
prediction results without structured data. Lu et al. [75] extended BERT embeddings
into a hybrid architecture with residual blocks to fuse textual and numeric signals for
corporate credit. This trend aligns with regulatory interest in leveraging unstructured and
semi-structured disclosures rather than purely tabular indicators.

A frontier research area involves transformer robustness, adversarial safety, and
regulatory alignment. Schwab and Kriebel [76] demonstrated that transformer encoders
can be sensitive to adversarial perturbations and proposed gradient-based regularisation
defenses. Given that financial systems are highly sensitive to stability and fairness, future
deployments of transformers must incorporate calibration diagnostics, imbalance-aware
loss functions, explainability tooling, and context-aware adversarial safeguards.

The recent contributions indicate that transformers are moving from experimental
architectures to practical candidates for large-scale, multimodal, and system-level credit risk
models. Their main advantage lies not only in predictive lift but also in their ability to unify
behavioural sequences, categorical embeddings, textual narratives, interbank networks,
and graph-structured relationships within a single modelling interface, while increasingly
accommodating class imbalance, interpretability, and systemic risk considerations.

The emerging evidence suggests that transformers are most promising in settings
where credit risk depends on high-dimensional, heterogeneous, or multimodal signals
that interact in non-local ways. Self-attention is particularly effective when modelling the
joint influence of long repayment histories, bureau or transactional text, and rich categor-
ical attributes, and it enables a single architecture to operate across these modalities. At
the same time, transformers typically require larger training datasets, more parameters,
and longer training times than conventional models, and the number of truly large-scale,
production-grade credit studies is still small. In practice, they should be viewed as candi-
dates for portfolios with abundant data and complex interactions, rather than as drop-in
replacements for tree ensembles or recurrent networks on small tabular datasets.

5.4. Graph Neural Networks for Relational Credit Risk

Graph neural networks (GNNs) have gained significant traction for credit risk predic-
tion due to their ability to encode relational dependencies that conventional tabular and
sequential models ignore. Borrowers interact within rich financial ecosystems involving
co-application, ownership links, shared directorship, supplier–customer contracts, and
transaction flows, making relational learning a natural extension to deep credit scoring.
Unlike feed-forward or recurrent architectures that assume independent records, GNNs
perform iterative message passing, enabling representation learning that captures both
direct and indirect risk propagation across financial networks.

Wang et al. [77] construct small and medium enterprise (SME) relational graphs using
shared director and business-interaction information and apply a relational graph attention
network (RGAT) for default prediction. Their inductive testing protocol shows that graph
baselines such as graph convolutional network (GCN), graph attention network (GAT), and
relational GCN (RGCN) outperform non-graph models, with RGAT achieving AUC = 0.797
and KS = 0.457, while a multi-head extension reaches AUC = 0.799 and KS = 0.528. The
results demonstrate that relational signals remain predictive even without transactional
features. Similarly, Song et al. [78] proposed the multi-structure cascaded GNN (MS-
CGNN), integrating pairwise graphs with heterogeneous hypergraph structures to model
higher-order interactions. The method achieved Recall = 0.8863, Accuracy = 0.9442, and

https://doi.org/10.3390/info17040395

---

<!-- PAGE 17 -->

Information 2026, 17, 395

17 of 28

F1-score = 0.9300, outperforming several GNN baselines and confirming that multi-level
topology strengthens risk representation.

Temporal and behavioural dynamics have also been incorporated into graph mod-
elling. Yuan et al. [79] introduce DGNN-SR, which fuses static fund-transfer graphs with
dynamic user–merchant payment graphs using multi-view time encoders. Experiments on
Tencent datasets containing more than 2.8M nodes and 200M edges show AUC improve-
ments between 0.85% and 2.5% over the best continuous-time GNN baselines. From a
supply-chain financing perspective, Mojdehi et al. [80] combine topological data analysis
with GNNs (BM–GNN), attaining maximum accuracy of 93.56% across multiple scenarios
while consistently outperforming classical ML models in stability and robustness, despite
similar point-estimate accuracy on some subsets.

Recent work has emphasised higher-order graph structures, regulatory alignment,
and training stability. Wang et al. [81] proposed a motif-preserving GNN with curricu-
lum learning to capture subgraph patterns frequently observed in enterprise networks,
demonstrating improved performance across one public and two industrial datasets. The
curriculum design helped mitigate convergence instability arising from noisy relational
substructures. In another direction, Liu et al. [82] constructed enterprise credit graphs using
a maximum spanning tree derived from 29 financial indicators and applied GraphSAGE
to multi-level credit grading. Their results confirmed higher ROC values than tree-based
and neural baselines, despite using a sparse graph, highlighting the value of relational
inductive bias even in limited-connectivity settings.

Scalability has become a core evaluation criterion for real-world deployment. Zhang
et al. [83] developed a large-scale industrial GNN pipeline comprising 23.4M nodes
for supply-chain mining and 8.6M nodes for default prediction. Their model achieved
AUC = 0.995 on supply-chain tie mining and 0.701 on loan-default prediction, outper-
forming static graph-learning competitors and demonstrating that GNNs can operate at
web-scale for national credit infrastructure. Furthermore, Cheng and Luo [84] propose a
metapath-driven risk contagion GNN (RCGNN) using heterogeneous paths (investment,
geography, and industry), reporting superior performance to homogeneous GNNs for
enterprise credit classification, although detailed metrics were not published.

Overall, GNN-based credit models are most compelling when relational structure is
intrinsic to the risk problem, such as SME supply chains, interbank exposures, enterprise
ownership networks, or fund-transfer graphs. In these environments, message passing
captures contagion and correlated risk that tabular or sequential models are structurally
unable to represent, and the empirical studies show consistent gains in discrimination
and stability under sparse or noisy features. The trade-off is engineering complexity:
constructing, maintaining, and governing large-scale financial graphs is non-trivial, and
the marginal benefit of GNNs is limited when relational information is weak or unavailable.
Consequently, GNNs are best viewed as targeted tools for systemically interconnected
portfolios rather than as universal replacements for borrower-level scorecards.

Table 4 consolidates the peer-reviewed deep learning applications discussed in this
section, grouped by model family for readability and direct linkage to the preceding
subsections. Reported metrics and values are reproduced as stated in the source studies
and are not standardised across datasets, targets, horizons, or label definitions, which limits
direct cross-paper comparability.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 18 -->

Information 2026, 17, 395

18 of 28

Table 4. Summary of deep learning applications in credit risk prediction.

Modelling Focus

Reference

Year Methods and Application

Tabular DL Models

Popov et al. [54]

2019

Lin et al. [49]

2022

Yang et al. [48]

2023

Asencios et al. [50]

2023

Hjelkrem and
Lange [52]

Li et al. [53]

Wang and
Zhang [51]

2023

2023

2024

Shan and Gao [55]

2025

Sequential Models

Liang and Cai [56]

2020

Chen and Long [61]

2020

Ala’raj et al. [57]

Zhang [58]

Li et al. [59]

2022

2022

2023

Wang et al. [60]

2024

Han et al. [62]

2024

Shi et al. [63]

2025

Yang et al. [64]

2025

Zhang [65]

2025

Transformer-Based
Models

Huang et al. [47]

2020

Gorishniy et al. [66]

2021

Stevenson et al. [74]

2021

NODE differentiable tree ensembles; match gradient
boosting on credit-style tabular tasks while remaining
fully differentiable.
Penalised DNN survival model for P2P time-to-default;
embedded penalties support feature selection and improve
PD estimation.
HDNN with L1–L2 regularisation for corporate credit;
Acc = 80.12% and outperforms LR, SVM, and baseline DNN.
MLP, XGBoost, and TabNet for profit scoring; XGBoost best
R2 = 0.7906, TabNet slightly lower but more interpretable.
MLP on open-banking transactions with SHAP; outperforms
a BERT model and yields intuitive behavioural risk drivers.
Incremental DNN for agricultural microloans under concept
drift; 1.4–7.8 pp AUC gains over DNN, XGBoost, and RF.
TabNet–stacking ensemble on large-scale credit; Acc = 0.979,
AUC = 0.941 on Tianchi.
Stacked TabNet with multi-stage optimisation for SME
supply-chain risk; AUC = 0.9616, Acc = 0.9277, above
TabNet, LightGBM, and CatBoost.

LSTM for Lending Club monthly default-rate forecasts; MAE
0.072 and RMSE 0.093, better than ARIMA, SVM, and ANN.
Self-attention end-to-end corporate rating; removes manual
aggregation and stabilises ratings vs classical ML.
Behavioural LSTM variants for credit cards; exceed SVM, RF,
MLP, and LR in PD prediction and calibration.
CNN–LSTM–attention for enterprise credit; AUC = 0.92 and
F1 = 0.91, outperforming CNN-only and LSTM-only models.
CNN–LSTM for listed corporates; CNN captures short-term
motifs, LSTM long-term behaviour, improving
discrimination.
Deep discrete-time survival with age–period–cohort
decomposition; yields smooth credit hazard curves and
macro/maturity structure.
Self-attention plus cross-network for default prediction;
improves accuracy, precision, recall, and F1 over
baseline DL.
Benchmark of CNN, RNN, and DNN for financial credit
scoring; RNN best temporal sensitivity, CNN most
parameter-efficient.
Residual-enhanced BiLSTM with multi-head attention on
Freddie Mac data; AUC = 0.982, F1 = 0.958, beating BiLSTM,
GRU, CNN, and RNN.
LSTM encoders with Bayesian calibration for corporate risk;
Acc = 0.972, AUC = 0.981 and reduced uncertainty
miscalibration vs RF and LR.

TabTransformer with contextual embeddings for
high-cardinality categorical features; improves over MLP
and tree baselines.
FT-Transformer for tabular data; attention blocks match or
surpass CatBoost/XGBoost on nonlinear financial tasks.
BERT embeddings from SME loan texts; text alone gives
competitive default prediction without structured variables.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 19 -->

Information 2026, 17, 395

19 of 28

Table 4. Cont.

Modelling Focus

Reference

Year Methods and Application

Transformer-Based
Models

Wang and Xiao [67]

2022

Korangi et al. [68]

2023

Li et al. [69]

2024

Kakadiya et al. [70]

2024

Wu [73]

2024

Hartomo et al. [72]

2025

Zhang and
Liang [71]

2025

Lu et al. [75]

2025

Schwab and
Kriebel [76]

2025

GNN-based Models

Wang et al. [81]

2023

Wang et al. [77]

2024

Song et al. [78]

2024

Liu et al. [82]

2024

Yuan et al. [79]

2025

Mojdehi et al. [80]

2025

Zhang et al. [83]

2025

Cheng and Luo [84]

2025

Feature-embedded transformer fusing behavioural
sequences and static features for online lending; AUC = 0.72,
KS = 0.32, better than LR, XGBoost, and LSTM.
Transformer for mid-cap corporate multi-horizon default;
multi-channel panel design yields higher AUC than
statistical and LSTM baselines.
HFTCRNet hierarchical fusion transformer for interbank
ratings and systemic risk; temporal + graph transformers
and contagion module outperform other models on
4548 banks.
Transformer models for bank loan default; self-attention
captures higher-order interactions and beats LR and
tree ensembles.
BiLSTM-Transformer on a blockchain financial sharing
platform; multimodal text/visual enterprise risk
identification with Acc > 94% and AUC > 0.95.
Weighted-loss TabTransformer with SHAP-based XAI for
imbalanced MSME and consumer credit; increases accuracy
and minority-class AUC/PR (e.g., 86.35%→89.27%).
Minimum weighted value error combination of BERT-based
temporal encoder and DNN/MLP experts; dynamic
weighting improves personal credit classification vs single
models.
BERT plus residual blocks to fuse textual and numeric
signals for corporate credit; improves classification vs.
single-modality and non-residual baselines.
Analysis of transformer robustness in financial tasks; shows
adversarial sensitivity and proposes
gradient-regularised defences.

Motif-preserving GNN with curriculum learning for
enterprise networks; improves accuracy and convergence
stability across public and industrial datasets.
RGAT on SME graphs from shared directors and
interactions; multi-head RGAT achieves AUC = 0.799 and
KS = 0.528, above non-graph baselines.
MS-CGNN combining pairwise graphs and hypergraphs;
Recall = 0.8863, Acc = 0.9442, F1 = 0.93, outperforming
several GNN variants.
GraphSAGE on maximum-spanning-tree enterprise credit
graphs; higher ROC than tree and neural baselines despite
sparse connectivity.
DGNN-SR fusing static fund-transfer and dynamic payment
graphs with multi-view time encoders; gains 0.85–2.5 pp
AUC over continuous-time GNNs.
BM–GNN using topological data analysis and GNNs for
supply-chain finance; max Acc = 93.56% with robust
performance vs classical ML.
Large-scale industrial GNN pipeline (23.4 M and 8.6 M
nodes) for supply-chain mining and default; AUC = 0.995
(links) and 0.701 (default).
Metapath-driven RCGNN using heterogeneous paths
(investment, geography, industry); improves multi-class
enterprise credit classification vs. homogeneous GNNs.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 20 -->

Information 2026, 17, 395

20 of 28

6. Challenges, Limitations, and Future Research Directions

Deep learning can improve risk discrimination, but deploying such models in reg-
ulated credit environments introduces constraints that go beyond accuracy. This section
summarises the main challenges and then distils research directions aimed at trustworthy,
regulation-ready credit risk modelling.

6.1. Challenges and Limitations
6.1.1. Evaluation Integrity

Credit risk evolves over time in response to behavioural, policy, and macroeconomic
shifts, making random k-fold cross-validation prone to temporal leakage. When observa-
tions from later periods appear in both training and test folds, performance estimates can
implicitly rely on future information that would not be available at decision time. Time-
ordered evaluation schemes, including out-of-time splits and rolling-origin validation in
which the training window strictly precedes the evaluation window, provide a more faith-
ful estimate of deployment performance under regime change and stress conditions [85].
However, a non-trivial portion of deep credit risk studies still relies on random splits,
weakening external validity and complicating comparisons across model families.

A second source of fragility is over-reliance on threshold-agnostic summary met-
rics such as AUC, which aggregate performance across all score cut-offs and can mask
behaviour in the operating region where lending decisions are actually made. In highly im-
balanced portfolios, complementary measures such as the area under the precision–recall
curve (AUPRC) and cost-sensitive metrics better reflect minority-class performance and
the economic consequences of misclassification [33]. Equally important, probability cal-
ibration is rarely assessed, despite being central to decisioning and risk quantification:
poorly calibrated scores can lead to unstable approval rates, mis-priced credit, and biased
downstream estimates of portfolio risk, even when ranking performance (AUC) improves.
Calibration-sensitive reporting using the Brier score and expected calibration error, together
with reliability diagrams, provides direct evidence of whether predicted probabilities match
observed default frequencies [86]. When miscalibration is detected, post hoc methods such
as Platt scaling, isotonic regression, and temperature scaling can improve alignment be-
tween predicted and empirical default rates [87], but these steps are seldom documented in
deep credit risk papers.

Finally, decision-facing evaluation should make explicit how metrics map to lend-
ing outcomes. For PD-style models, this includes reporting performance at operationally
relevant thresholds and, where inputs are available, quantifying utility using simple cost
proxies (false-approval loss versus false-rejection opportunity cost) or by propagating cali-
brated PD into downstream loss constructs (e.g., EL-style estimates), while acknowledging
that EL is not comparable across heterogeneous datasets and recovery definitions. These
considerations jointly form a de facto evaluation checklist for deployment-aligned credit
risk modelling.

6.1.2. Imbalanced Learning and Reject Inference

Default datasets are heavily imbalanced, and naïve resampling can distort temporal
and behavioural structure. Over-sampling techniques such as SMOTE are often applied
indiscriminately without temporal safeguards, while cost-sensitive learning better reflects
economic risk but is infrequently employed [88,89]. A further complication is reject infer-
ence: declined applicants lack observed outcomes, leading to structurally biased training
data and unreliable generalisation [28,90,91]. Observed outcomes are conditional on accep-
tance policies, leading to sample-selection bias that inflates apparent model performance

https://doi.org/10.3390/info17040395

---

<!-- PAGE 21 -->

Information 2026, 17, 395

21 of 28

when applied to rejected populations. Existing proxy-based inference methods remain
heuristic and are not aligned with regulatory transparency expectations.

6.1.3. Interpretability and Fairness

Although deep models improve predictive power, their opacity conflicts with reg-
ulatory explainability requirements. Post hoc explanation tools, including SHAP and
integrated gradients, may not provide stable, counterfactual-faithful explanations [92]. In
practice, the appropriate explanation tool depends on the model family and the decision
artefact being justified: for MLP-style tabular networks, feature attribution methods and
monotonic or sparse constraints can support reasoned factor narratives; for tree-like base-
lines and tree–neural hybrids, TreeSHAP-style decompositions often provide the most
auditable feature-level breakdown; for transformer-based credit models, attribution over
token/feature embeddings (with attention used as a supportive diagnostic rather than
a standalone explanation) is typically more reliable than raw attention maps; and for
GNN-based credit models, subgraph- or message-passing explanations can localise which
relations drive a risk score.

Fairness is also inconsistently operationalised in the DL credit-risk literature. Metrics
such as equalised odds [93] are rarely integrated into training objectives, despite evidence
that automated lending can amplify existing socio-economic inequalities. Fairness targets
are context dependent: demographic parity may be inappropriate when base rates differ
for legitimate reasons, whereas error-rate constraints such as equalised odds may be
more suitable when the aim is to control differential misclassification harms. Accordingly,
the selected fairness definition should be justified relative to the lending decision, the
attributes available for monitoring, and the governing legal regime, and it should be
assessed alongside model calibration and operating-threshold behaviour. Counterfactual
explanation approaches remain promising, but deployment at scale is often hindered by
feasibility constraints and by the need to ensure plausibility under real credit policy and
data-generating processes [94].

Among the surveyed deep learning studies, only a small subset explicitly incorporates
post hoc explainability tools or fairness metrics, and even fewer optimise fairness-aware
objectives during training, which shows the gap between regulatory aspirations and cur-
rent practice.

6.1.4. Robustness and Privacy

Deep learning models are sensitive to concept drift caused by macroeconomic shocks,
behavioural changes, and portfolio rebalancing, leading to calibration decay over time [95].
Existing studies seldom incorporate drift-aware retraining or automated change detection.
For deployment-aligned robustness, studies should distinguish (i) temporal drift (vintage
and macro shifts), (ii) population drift (portfolio mix changes), and (iii) label/definition
drift (policy or collections-rule changes), and then evaluate mitigation using time-ordered
backtests rather than random re-sampling. Operationally, this translates to monitoring both
discrimination and calibration over time (e.g., AUC/AUPRC alongside Brier/ECE), trig-
gering review when calibration deviates materially even if ranking metrics appear stable.
At the same time, sharing granular data across institutions introduces privacy and
confidentiality constraints. Differentially private training and synthetic data generation
partially address these limitations but introduce accuracy trade-offs. Where collaboration
is required, privacy-preserving learning should be framed as an end-to-end design choice
(e.g., federated training with secure aggregation, differential privacy with documented
privacy budgets, or controlled synthetic-data release), accompanied by utility and bias
testing to show what decision quality is lost or retained under privacy constraints.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 22 -->

Information 2026, 17, 395

22 of 28

6.1.5. Operational Deployment and Governance

Operational success requires structured machine learning operations (MLOps)
pipelines with versioning, lineage tracking, monitoring, and challenger-champion testing.
Without these, systems accumulate technical debt that weakens compliance and under-
mines model lifecycle management [96]. In regulated credit settings, deployment discipline
is typically enforced through a model risk management workflow that makes each stage au-
ditable: reproducible feature pipelines, immutable training and evaluation datasets, signed
model artefacts, and traceable decision records that link every production score to a specific
model version and data snapshot. A common rollout pattern is staged release, in which
a candidate model first passes offline backtesting, then runs in shadow scoring (producing
scores without affecting approvals), and only then progresses to limited exposure with
pre-defined promotion gates based on calibration, drift, and stability checks. These gates
reduce failures that frequently occur in practice, such as silent calibration decay after policy
or collections-rule changes, performance drops under macroeconomic regime shifts, and
inconsistent feature computation between training and serving.

Moreover, existing governance artefacts, including datasheets and model cards, are
rarely integrated with regulatory processes such as Basel III, SR 11-7, or the EU AI Act,
reducing organisational readiness for external audit. To make interpretability and fairness
operational rather than ad hoc, explanation and bias-assessment outputs should be gener-
ated automatically per model version within the CI/CD workflow and stored as part of
the model evidence pack. Concretely, this means logging (i) global and local explanation
artefacts aligned with the deployed model family, (ii) fairness reports computed on the
production decision population (and, where feasible, on approved-outcome populations),
and (iii) monitoring dashboards that track both discrimination and calibration over time.
When exceptions occur (e.g., manual overrides, policy-driven rule changes, or temporary
risk controls), the governance layer should record the override rationale and its impact
on observed outcomes so that future retraining does not unknowingly encode short-term
interventions as predictive signals.

6.2. Future Research Directions

Future research should adopt evaluation frameworks that reflect realistic data-
generating processes, including temporally constrained train-test splits, multi-horizon
performance tracking, and calibration-aware reporting. This includes benchmarking on
large-scale, longitudinal datasets with explicit temporal structure and economic annota-
tions, enabling fair comparison across model families and reducing over-optimism asso-
ciated with small public datasets. Moreover, future work should prioritise cost-aligned
performance reporting, where model utility is quantified in terms of expected loss reduc-
tion, capital efficiency, default timing, and resilience across macroeconomic stress regimes
(Table 5).

Another direction is the development of learning objectives that integrate fairness, in-
terpretability, and economic cost at training time rather than relying on post hoc adjustment.
Interpretable-by-design architectures, monotonic neural networks, sparse attention mecha-
nisms, and hybrid symbolic-neural models can provide greater regulatory compatibility
while retaining feature interaction capacity. Causal fairness, adversarial debiasing, and
counterfactual training pipelines represent promising frameworks for mitigating disparate
impact without suppressing predictive power.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 23 -->

Information 2026, 17, 395

23 of 28

Table 5. Challenges in deep learning credit risk modelling and aligned research directions.

Challenge

Description

Emerging Research Directions

Evaluation Integrity

Temporal leakage and weak calibration
undermine external validity [18,23,58,87].

Imbalance and Reject Inference

Rare defaults and missing counterfactual
labels distort learning signals [88–90].

Interpretability and Fairness

Deep models violate explainability and
anti-bias compliance [92,97].

Robustness and Privacy

Drift and privacy constraints limit
long-term reliability [95,98].

Operational Deployment and Governance

Insufficient deployment discipline
increases regulatory risk [96,99].

Out-of-time and rolling validation;
calibration-aware reporting; cost-sensitive
and utility-aligned scoring.

Causal estimation, selective abstention,
semi-supervised reject inference, and
cost-sensitive objectives.

Interpretable-by-design architectures,
causal fairness constraints, certified
explanation mechanisms.

Drift-robust adaptive training, federated
learning, synthetic financial digital twins,
DP-SGD optimisation.

Automated monitoring frameworks,
model-card pipelines, Basel-aligned
documentation standards.

Research should also focus on designing models that adapt under uncertainty while
maintaining stability guarantees. Drift-aware architectures, online continual learning
mechanisms, uncertainty-calibrated predictions, and stress-testing under macroeconomic
scenario simulation may improve long-term reliability. Privacy-preserving collaborative
learning, through federated optimisation, secure multiparty computation, and high-fidelity
synthetic digital twins, would enable cross-institutional learning while respecting confiden-
tiality and regulation. This agenda also requires governance and regulatory alignment for
cross-institutional data sharing, including clear accountability for consent, access control,
retention, and auditability. Similarly, synthetic data should be governed with documented
generation protocols, privacy-risk testing, and downstream-use restrictions to avoid leakage
and unwarranted reliance in regulated decision-making.

Finally, there is a need for deployment-aligned governance frameworks that stan-
dardise model documentation, monitoring, and auditability. Integrated pipelines that
combine MLOps with regulatory artefacts, such as model cards linked to validation logs
and challenger-champion performance trails, could accelerate institutional trust and re-
duce compliance costs. Long-term progress will require systems that are not only more
accurate, but also certifiably fair, transparent, and robust—making deep learning suitable
for production-grade financial risk management.

7. Conclusions

This survey reviewed deep learning methods for credit risk prediction across tabu-
lar, sequential, transformer-based, and graph-structured settings. By organising existing
research through a unified taxonomy that links model families to data structures and
credit-risk objectives, the survey provides conceptual clarity on when and why specific
architectures are appropriate. Across the peer-reviewed evidence, deep models tend to
outperform traditional scorecard and ensemble methods when trained on sufficiently large,
temporally representative datasets with rich behavioural and relational information.

However, the literature also reveals gaps that constrain reliable real-world adoption.
Reporting standards are inconsistent, with limited use of temporally valid evaluation,
calibration metrics, and cost-aligned performance reporting. Interpretability and fairness
are often treated as add-ons rather than requirements, and robustness under concept drift,
data-sharing constraints, and operational governance remains weakly addressed, shifting
success criteria toward predictive accuracy rather than lifecycle reliability and auditability.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 24 -->

Information 2026, 17, 395

24 of 28

Future work should therefore prioritise deployment-aligned research: interpretable-
by-design modelling, temporally realistic benchmarks, fairness strategies grounded in the
decision and legal context, privacy-preserving collaborative learning, and governance-
ready monitoring and documentation pipelines. This survey is limited to peer-reviewed
English-language studies indexed in major databases and does not cover proprietary
implementations or regulatory grey literature; future syntheses could extend the evidence
base using secure-access supervisory data or meta-analyses where study designs and
outcomes are sufficiently comparable.

Author Contributions: Conceptualisation, I.D.M., E.E. and C.M.; methodology, I.D.M., E.E. and
C.M.; validation, I.D.M., E.E. and C.M.; investigation, I.D.M., E.E. and C.M.; writing—original draft
preparation, I.D.M.; writing—review and editing, I.D.M., E.E. and C.M.; visualisation, I.D.M., E.E.
and C.M.; supervision, E.E. and C.M. All authors have read and agreed to the published version of
the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: No new data were created or analysed in this study. Data sharing is
not applicable to this article.

Conflicts of Interest: The authors declare no conflicts of interest.

Abbreviations

The following abbreviations are used in this manuscript:

Artificial intelligence
Area under the receiver operating characteristic curve
Area under the precision–recall curve
Convolutional neural networks
Deep learning
Exposure at default
Expected loss
Graph neural networks
Gated recurrent unit
High-dimensional deep neural network
Incremental DNN
Loss given default
Logistic regression
Long short-term memory
Machine learning
Machine learning operations
Multi-layer perceptron

AI
AUC
AUPRC
CNNs
DL
EAD
EL
GNNs
GRU
HDNN
I-DNN
LGD
LR
LSTM
ML
MLOps
MLP
MS-CGNN Multi-structure cascaded GNN
NODE
PD
PDNN
RNNs
RWA
SME
SVMs
TCNs
XAI

Neural Oblivious Decision Ensembles
Probability of default
Penalised deep neural network
Recurrent neural networks
Risk-weighted asset
Small and medium enterprise
Support vector machines
Temporal convolutional networks
Explainable AI

https://doi.org/10.3390/info17040395

---

<!-- PAGE 25 -->

Information 2026, 17, 395

References

25 of 28

1.

2.

3.

4.

5.

Zhu, Y.; Wu, D. P2P credit risk management with KG-GNN: A knowledge graph and graph neural network-based approach.
J. Oper. Res. Soc. 2025, 76, 866–880. [CrossRef]
Alagic, A.; Zivic, N.; Kadusic, E.; Hamzic, D.; Hadzajlic, N.; Dizdarevic, M.; Selmanovic, E. Machine learning for an enhanced
credit risk analysis: A comparative study of loan approval prediction models integrating mental health data. Mach. Learn. Knowl.
Extr. 2024, 6, 53–77. [CrossRef]
Karami, A.; Igbokwe, C. The impact of big data characteristics on credit risk assessment. Int. J. Data Sci. Anal. 2025, 20, 4239–4259.
[CrossRef]
Talaat, F.M.; Aljadani, A.; Badawy, M.; Elhosseini, M. Toward interpretable credit scoring: Integrating explainable artificial
intelligence with deep learning for credit card default prediction. Neural Comput. Appl. 2024, 36, 4847–4865. [CrossRef]
Aruleba, I.; Sun, Y. Effective credit risk prediction using ensemble classifiers with model explanation. IEEE Access 2024, 12,
115015–115025. [CrossRef]

6. Machado, M.R.; Chen, D.T.; Osterrieder, J.R. An analytical approach to credit risk assessment using machine learning models.

7.

8.

9.

Decis. Anal. J. 2025, 16, 100605. [CrossRef]
Tian, Z.; Xiao, J.; Feng, H.; Wei, Y. Credit risk assessment based on gradient boosting decision tree. Procedia Comput. Sci. 2020,
174, 150–160. [CrossRef]
Aruleba, I.; Sun, Y. Enhanced credit risk prediction using deep learning and SMOTE-ENN resampling. Mach. Learn. Appl. 2025,
21, 100692. [CrossRef]
Sun, P.; Jia, Y.; Shi, Y.; Ren, J.; Li, Z.; Li, X. Artificial Intelligence Credit Risk Assessment Model Based on MLP-Hybrid Clustering.
Complexity 2025, 2025, 3308222. [CrossRef]

10. Mienye, I.D.; Esenogho, E.; Modisane, C. Deep Reinforcement Learning in the Era of Foundation Models: A Survey. Computers

2026, 15, 40. [CrossRef]

11. Bhatore, S.; Mohan, L.; Reddy, Y.R. Machine learning techniques for credit risk evaluation: A systematic literature review. J. Bank.

12.

Financ. Technol. 2020, 4, 111–138. [CrossRef]
Shi, S.; Tse, R.; Luo, W.; D’Addona, S.; Pau, G. Machine learning-driven credit risk: A systemic review. Neural Comput. Appl. 2022,
34, 14327–14339. [CrossRef]

13. Noriega, J.P.; Rivera, L.A.; Herrera, J.A. Machine learning for credit risk prediction: A systematic literature review. Data 2023,

8, 169. [CrossRef]

14. Montevechi, A.A.; de Carvalho Miranda, R.; Medeiros, A.L.; Montevechi, J.A.B. Advancing credit risk modelling with Machine

Learning: A comprehensive review of the state-of-the-art. Eng. Appl. Artif. Intell. 2024, 137, 109082. [CrossRef]

15. Kim, H.; Cho, H.; Ryu, D. Corporate default predictions using machine learning: Literature review. Sustainability 2020, 12, 6325.

[CrossRef]

16. Çallı, B.A.; Co¸skun, E. A longitudinal systematic review of credit risk assessment and credit default predictors. Sage Open 2021,

11, 21582440211061333. [CrossRef]

17. Mhlanga, D. Financial inclusion in emerging economies: The application of machine learning and artificial intelligence in credit

risk assessment. Int. J. Financ. Stud. 2021, 9, 39. [CrossRef]

18. Hayashi, Y. Emerging trends in deep learning for credit scoring: A review. Electronics 2022, 11, 3181. [CrossRef]
19. Peng, K.; Yan, G. A survey on deep learning for financial risk prediction. Quant. Financ. Econ. 2021, 5, 716–737. [CrossRef]
20. Hoyos Gutiérrez, S.P.; Santos López, F.M. Credit Risk Assessment System Based on Deep Learning: A Systematic Literature
Review. In Proceedings of the International Conference on Computer Science, Electronics and Industrial Engineering (CSEI); Springer:
Berlin/Heidelberg, Germany, 2023; pp. 395–413.

21. Demma Wube, H.; Zekarias Esubalew, S.; Fayiso Weldesellasie, F.; Girma Debelee, T. Deep learning and machine learning tech-
niques for credit scoring: A review. In Proceedings of the Pan African Conference on Artificial Intelligence; Springer: Berlin/Heidelberg,
Germany, 2024; pp. 30–61.

22. Mienye, E.; Jere, N.; Obaido, G.; Mienye, I.D.; Aruleba, K. Deep Learning in Finance: A Survey of Applications and Techniques.

AI 2024, 5, 2066–2091. [CrossRef]

23. Valdrighi, G.; M Ribeiro, A.; SB Pereira, J.; Guardieiro, V.; Hendricks, A.; Miranda Filho, D.; Nieto Garcia, J.D.; F Bocca, F.;
B Veronese, T.; Wanner, L.; et al. Best practices for responsible machine learning in credit scoring. Neural Comput. Appl. 2025, 37,
20781–20821. [CrossRef]

24. Paz, Á.; Crawford, B.; Monfroy, E.; Barrera-García, J.; Peña Fritz, Á.; Soto, R.; Cisternas-Caneo, F.; Yáñez, A. Machine Learning
and Metaheuristics Approach for Individual Credit Risk Assessment: A Systematic Literature Review. Biomimetics 2025, 10, 326.
[CrossRef]

25. Alvi, J.; Arif, I.; Nizam, K. Advancing financial resilience: A systematic review of default prediction models and future directions

in credit risk management. Heliyon 2024, 10, e39770. [CrossRef]

https://doi.org/10.3390/info17040395

---

<!-- PAGE 26 -->

Information 2026, 17, 395

26 of 28

26. Bhattacharya, A.; Biswas, S.K.; Mandal, A. Credit risk evaluation: A comprehensive study. Multimed. Tools Appl. 2023,

82, 18217–18267. [CrossRef]

27. Gunnarsson, B.R.; Vanden Broucke, S.; Baesens, B.; Óskarsdóttir, M.; Lemahieu, W. Deep learning for credit scoring: Do or don’t?

Eur. J. Oper. Res. 2021, 295, 292–305. [CrossRef]

28. Thomas, L.; Crook, J.; Edelman, D. Credit Scoring and Its Applications; SIAM: Philadelphia, PA, USA, 2017.
29. Bandyopadhyay, A. Loan level loss given default (LGD) study of Indian banks. IIMB Manag. Rev. 2022, 34, 168–177. [CrossRef]
30. Wattanawongwan, S.; Mues, C.; Okhrati, R.; Choudhry, T.; So, M.C. Modelling credit card exposure at default using vine copula

quantile regression. Eur. J. Oper. Res. 2023, 311, 387–399. [CrossRef]

31. Hofmann, H. Statlog (German Credit Data). UCI Machine Learning Repository. 1994. Available online: https://archive.ics.uci.

edu/dataset/144/statlog+german+credit+data (accessed on 1 October 2025).

32. Yeh, I.C.; Lien, C.H. The comparisons of data mining techniques for the predictive accuracy of probability of default of credit

card clients. Expert Syst. Appl. 2009, 36, 2473–2480. [CrossRef]

33. Lessmann, S.; Baesens, B.; Seow, H.V.; Thomas, L.C. Benchmarking state-of-the-art classification algorithms for credit scoring: An

update of research. Eur. J. Oper. Res. 2015, 247, 124–136. [CrossRef]

34. Montoya, A.; Inversion; KirillOdintsov; Kotek, M. Home Credit Default Risk. Kaggle. 2018. Available online: https://kaggle.

com/competitions/home-credit-default-risk (accessed on 5 December 2025).

35. Malekipirbazari, M.; Aksakalli, V. Risk assessment in social lending via random forests. Expert Syst. Appl. 2015, 42, 4621–4631.

[CrossRef]

36. Nwafor, C.N.; Nwafor, O.; Brahma, S. Enhancing transparency and fairness in automated credit decisions: An explainable novel

hybrid machine learning approach. Sci. Rep. 2024, 14, 25174. [CrossRef]

37. de Oliveira, N.A.; Basso, L.F.C. Advancing Credit Rating Prediction: The Role of Machine Learning in Corporate Credit Rating

Assessment. Risks 2025, 13, 116. [CrossRef]

38. LeCun, Y.; Bengio, Y.; Hinton, G. Deep learning. Nature 2015, 521, 436–444. [CrossRef]
39. Mienye, I.D.; Swart, T.G.; Obaido, G. Recurrent neural networks: A comprehensive review of architectures, variants, and

applications. Information 2024, 15, 517. [CrossRef]

40. Mienye, I.D.; Esenogho, E.; Modisane, C. Detecting Imbalanced Credit Card Fraud via Hybrid Graph Attention and Variational

Autoencoder Ensembles. AppliedMath 2025, 5, 131. [CrossRef]

41. Bai, S.; Kolter, J.Z.; Koltun, V. An empirical evaluation of generic convolutional and recurrent networks for sequence modeling.

arXiv 2018, arXiv:1803.01271. [CrossRef]

42. Liu, M.; Xia, C.; Xia, Y.; Deng, S.; Wang, Y. TDCN: A novel temporal depthwise convolutional network for short-term load

forecasting. Int. J. Electr. Power Energy Syst. 2025, 165, 110512. [CrossRef]

43. Dong, A.; Starr, A.; Zhao, Y. An interpretable temporal convolutional framework for Granger causality analysis. IEEE/CAA J.

Autom. Sin. 2025, 13, 1–15. [CrossRef]

44. Vashishth, T.K.; Sharma, V.; Sharma, K.K.; Ahamad, S.; Kaushik, V. Financial Forecasting with Convolutional Neural Networks
(CNNs): Trends and Challenges. In Shaping Cutting-Edge Technologies and Applications for Digital Banking and Financial Services;
Taylor & Francis: Abingdon, UK, 2025; pp. 62–81.

45. Mienye, I.D.; Swart, T.G. A comprehensive review of deep learning: Architectures, recent advances, and applications. Information

2024, 15, 755. [CrossRef]

46. Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, Ł.; Polosukhin, I. Attention is all you need.

Adv. Neural Inf. Process. Syst. 2017, 30, 6000–6010.

47. Huang, X.; Khetan, A.; Cvitkovic, M.; Karnin, Z. Tabtransformer: Tabular data modeling using contextual embeddings. arXiv

2020, arXiv:2012.06678. [CrossRef]

48. Yang, M.; Lim, M.K.; Qu, Y.; Li, X.; Ni, D. Deep neural networks with L1 and L2 regularization for high dimensional corporate

credit risk prediction. Expert Syst. Appl. 2023, 213, 118873. [CrossRef]

49. Lin, C.; Qiao, N.; Zhang, W.; Li, Y.; Ma, S. Default risk prediction and feature extraction using a penalized deep neural network.

Stat. Comput. 2022, 32, 76. [CrossRef]

50. Asencios, R.; Asencios, C.; Ramos, E. Profit scoring for credit unions using the multilayer perceptron, XGBoost and TabNet

algorithms: Evidence from Peru. Expert Syst. Appl. 2023, 213, 119201. [CrossRef]

51. Wang, S.; Zhang, X. Research on credit default prediction model based on TabNet-stacking. Entropy 2024, 26, 861. [CrossRef]
52. Hjelkrem, L.O.; Lange, P.E.d. Explaining deep learning models for credit scoring with SHAP: A case study using Open Banking

Data. J. Risk Financ. Manag. 2023, 16, 221. [CrossRef]

53. Li, G.; Zhu, F.; Zhang, Y.; Li, M. A Data-Driven Incremental Deep Neural Network for Borrower Credit Scoring. SSRN 2023.

[CrossRef]

54. Popov, S.; Morozov, S.; Babenko, A. Neural oblivious decision ensembles for deep learning on tabular data.

arXiv 2019,

arXiv:1909.06312. [CrossRef]

https://doi.org/10.3390/info17040395

---

<!-- PAGE 27 -->

Information 2026, 17, 395

27 of 28

55.

Shan, W.; Gao, B. Stacked Ensemble Model with Enhanced TabNet for SME Supply Chain Financial Risk Prediction. Systems 2025,
13, 892. [CrossRef]

56. Liang, L.; Cai, X. Forecasting peer-to-peer platform default rate with LSTM neural network. Electron. Commer. Res. Appl. 2020,

43, 100997. [CrossRef]

57. Ala’raj, M.; Abbod, M.F.; Majdalawieh, M.; Jum’a, L. A deep learning model for behavioural credit scoring in banks. Neural

Comput. Appl. 2022, 34, 5839–5866. [CrossRef]

58. Zhang, L. The Evaluation on the Credit Risk of Enterprises with the CNN-LSTM-ATT Model. Comput. Intell. Neurosci. 2022,

2022, 6826573. [CrossRef] [PubMed]

59. Li, J.; Xu, C.; Feng, B.; Zhao, H. Credit risk prediction model for listed companies based on CNN-LSTM and attention mechanism.

Electronics 2023, 12, 1643. [CrossRef]

60. Wang, H.; Bellotti, A.; Qu, R.; Bai, R. Discrete-Time Survival Models with Neural Networks for Age–Period–Cohort Analysis of

Credit Risk. Risks 2024, 12, 31.

61. Chen, B.; Long, S. A novel end-to-end corporate credit rating model based on self-attention mechanism.

IEEE Access 2020,

8, 203876–203889. [CrossRef]

62. Han, D.; Guo, W.; Chen, Y.; Wang, B.; Li, W. Personal credit default prediction fusion framework based on self-attention and

63.

cross-network algorithms. Eng. Appl. Artif. Intell. 2024, 133, 107977. [CrossRef]
Shi, X.; Tang, D.; Yu, Y. Credit Scoring Prediction Using Deep Learning Models in the Financial Sector. IEEE Access 2025, 13,
130731–130746. [CrossRef]

64. Yang, Y.; Lin, Y.; Zhang, Y.; Su, Z.; Goh, C.C.; Fang, T.; Bellotti, A.G.; Lee, B.G. Transforming Credit Risk Analysis: A Time-Series-

Driven ResE-BiLSTM Framework for Post-Loan Default Detection. arXiv 2025, arXiv:2508.00415. [CrossRef]

65. Zhang, Y. AI-Driven Framework for Financial Risk Management: Enhancing Decision-Making with LSTM Networks and
Probabilistic Models. In Proceedings of the 2025 2nd International Conference on Intelligent Computing and Robotics (ICICR); IEEE:
Piscataway, NJ, USA, 2025; pp. 176–181.

66. Gorishniy, Y.; Rubachev, I.; Khrulkov, V.; Babenko, A. Revisiting deep learning models for tabular data. Adv. Neural Inf. Process.

Syst. 2021, 34, 18932–18943.

67. Wang, C.; Xiao, Z. A deep learning approach for credit scoring using feature embedded transformer. Appl. Sci. 2022, 12, 10995.

[CrossRef]

68. Korangi, K.; Mues, C.; Bravo, C. A transformer-based model for default prediction in mid-cap corporate markets. Eur. J. Oper.

Res. 2023, 308, 306–320. [CrossRef]

69. Li, J.; Zhou, Z.; Zhang, J.; Cheng, D.; Jiang, C. HFTCRNet: Hierarchical fusion transformer for interbank credit rating and risk

assessment. IEEE Trans. Neural Netw. Learn. Syst. 2024, 36, 13006–13020. [CrossRef]

70. Kakadiya, R.; Khan, T.; Diwan, A.; Mahadeva, R. Transformer Models for Predicting Bank Loan Defaults a Next-Generation Risk
Management. In Proceedings of the 2024 IEEE 6th International Conference on Cybernetics, Cognition and Machine Learning Applications
(ICCCMLA); IEEE: Piscataway, NJ, USA, 2024; pp. 26–31.

71. Zhang, Y.; Liang, X. Personal Credit Risk Prediction Based on Minimum Weight Value Error Combination Model. In Proceedings
of the 2025 8th International Conference on Advanced Algorithms and Control Engineering (ICAACE); IEEE: Piscataway, NJ, USA, 2025;
pp. 307–313.

72. Hartomo, K.D.; Arthur, C.; Nataliani, Y. A novel weighted loss tabtransformer integrating explainable ai for imbalanced credit

risk datasets. IEEE Access 2025, 13, 31045–31056. [CrossRef]

73. Wu, Y. Enterprise financial sharing and risk identification model combining recurrent neural networks with transformer model

74.

supported by blockchain. Heliyon 2024, 10, e32639. [CrossRef]
Stevenson, M.; Mues, C.; Bravo, C. The value of text for small business default prediction: A deep learning approach. Eur. J. Oper.
Res. 2021, 295, 758–771. [CrossRef]

75. Lu, S.; Zhang, X.; Su, Y.; Liu, X.; Yu, L. Efficient multimodal learning for corporate credit risk prediction with an extended deep

76.

belief network. In Annals of Operations Research; Springer: Berlin/Heidelberg, Germany, 2025; pp. 1–38.
Schwab, B.; Kriebel, J. Mitigating adversarial attacks on transformer models in credit scoring. Eur. J. Oper. Res. 2025, 328, 309–323.
[CrossRef]

77. Wang, J.; Liu, G.; Xu, X.; Xing, X. Credit risk prediction for small and medium enterprises utilizing adjacent enterprise data and a

78.

relational graph attention network. J. Manag. Sci. Eng. 2024, 9, 177–192. [CrossRef]
Song, L.; Li, H.; Tan, Y.; Li, Z.; Shang, X. Enhancing enterprise credit risk assessment with cascaded multi-level graph
representation learning. Neural Netw. 2024, 169, 475–484. [CrossRef] [PubMed]

79. Yuan, Q.; Liu, Y.; Tang, Y.; Chen, X.; Zheng, X.; He, Q.; Ao, X. Dynamic Graph Learning with Static Relations for Credit Risk
Assessment. In Proceedings of the AAAI Conference on Artificial Intelligence, Philadelphia, PA, USA, 25 February–4 March 2025;
Volume 39, pp. 13133–13141.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 28 -->

Information 2026, 17, 395

28 of 28

80. Mojdehi, K.F.; Amiri, B.; Haddadi, A. A Novel Hybrid Model for Credit Risk Assessment of Supply Chain Finance Based on

Topological Data Analysis and Graph Neural Network. IEEE Access 2025, 13, 13101–13127. [CrossRef]

81. Wang, D.; Zhang, Z.; Zhao, Y.; Huang, K.; Kang, Y.; Zhou, J. Financial default prediction via motif-preserving graph neural
network with curriculum learning. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data
Mining, Long Beach, CA, USA, 6–10 August 2023; pp. 2233–2242.

82. Liu, B.; Li, I.; Yao, J.; Chen, Y.; Huang, G.; Wang, J. Unveiling the Potential of Graph Neural Networks in SME Credit Risk
Assessment. In Proceedings of the 2024 5th International Conference on Intelligent Computing and Human-Computer Interaction (ICHCI);
IEEE: Piscataway, NJ, USA, 2024; pp. 562–566.

83. Zhang, Z.; Shen, Q.; Hu, Z.; Liu, Q.; Shen, H. Credit risk analysis for SMEs using graph neural networks in supply chain. In
Proceedings of the 2025 International Conference on Big Data, Artificial Intelligence and Digital Economy, Kunming, China,
18–20 July 2025; pp. 81–85.

84. Cheng, C.; Luo, C. Enterprise Credit Rating Framework Based on Risk Contagion Graph Neural Network. In Proceedings of the
International Conference on Machine Learning and Soft Computing; Springer: Berlin/Heidelberg, Germany, 2025; pp. 243–254.

85. Bergmeir, C.; Benítez, J.M. On the use of cross-validation for time series predictor evaluation.

Inf. Sci. 2012, 191, 192–213.

86.

[CrossRef]
Fonseca, P.G.; Lopes, H.D. Calibration of machine learning classifiers for probability of default modelling.
arXiv:1710.08901. [CrossRef]

arXiv 2017,

87. Guo, C.; Pleiss, G.; Sun, Y.; Weinberger, K.Q. On calibration of modern neural networks. In Proceedings of the International

88.

Conference on Machine Learning, Sydney, Australia, 6–11 August 2017; pp. 1321–1330.
Idwan, S.; Etaiwi, W.; Rafayia, H.; Matar, I. A comprehensive review of statistical variants and enhancements of SMOTE
oversampling method. Int. J. Data Sci. Anal. 2025, 20, 6887–6904. [CrossRef]

89. Hu, X.; Chen, H.; Zhang, J.; Chen, H.; Liu, S.; Li, X.; Wang, Y.; Xue, X. GAT-COBO: Cost-sensitive graph neural network for

telecom fraud detection. IEEE Trans. Big Data 2024, 10, 528–542. [CrossRef]

90. Andrae, S. Fairness and bias in machine learning models for credit decisions. In Machine Learning and Modeling Techniques in

Financial Data Science; IGI Global Scientific Publishing: Hershey, PA, USA, 2025; pp. 1–24.

91. Liao, J.; Wang, W.; Xue, J.; Lei, A.; Han, X.; Lu, K. Combating sampling bias: A self-training method in credit risk models. In
Proceedings of the AAAI Conference on Artificial Intelligence, Online, 22 February–1 March 2022; Volume 36, pp. 12566–12572.
92. Rudin, C. Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead.

Nat. Mach. Intell. 2019, 1, 206–215. [CrossRef]

93. Hardt, M.; Price, E.; Srebro, N. Equality of opportunity in supervised learning. Adv. Neural Inf. Process. Syst. 2016, 29, 3323–3331.
94. Wachter, S.; Mittelstadt, B.; Russell, C. Counterfactual explanations without opening the black box: Automated decisions and the

GDPR. Harv. JL Tech. 2017, 31, 841. [CrossRef]

95. Greco, S.; Vacchetti, B.; Apiletti, D.; Cerquitelli, T. Unsupervised concept drift detection from deep learning representations in

real-time. IEEE Trans. Knowl. Data Eng. 2025, 37, 6232–6245. [CrossRef]

96. Ximenes, R.; Alves, A.P.S.; Escovedo, T.; Spinola, R.; Kalinowski, M. Investigating Issues that Lead to Code Technical Debt in
Machine Learning Systems. In Proceedings of the 2025 IEEE/ACM 4th International Conference on AI Engineering–Software Engineering
for AI (CAIN); IEEE: Piscataway, NJ, USA, 2025; pp. 173–183.

97. Bartlett, R.; Morse, A.; Stanton, R.; Wallace, N. Consumer-lending discrimination in the FinTech Era.

J. Financ. Econ. 2022,

143, 30–56. [CrossRef]

98. Pradhan, R.; Alazzam, M.B.; Keswani, S.; Bhasin, N.K.; Jaff, N.A.; Muthuperumal, S. A Hybrid GRU-Transformer Model for
In Proceedings of the 2025 3rd International Conference on Integrated Circuits and

Financial Forecasting and Risk Management.
Communication Systems (ICICACS); IEEE: Piscataway, NJ, USA, 2025; pp. 1–5.

99. Amershi, S.; Begel, A.; Bird, C.; DeLine, R.; Gall, H.; Kamar, E.; Nagappan, N.; Nushi, B.; Zimmermann, T. Software engineering
for machine learning: A case study. In Proceedings of the 2019 IEEE/ACM 41st International Conference on Software Engineering:
Software Engineering in Practice (ICSE-SEIP); IEEE: Piscataway, NJ, USA, 2019; pp. 291–300.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

https://doi.org/10.3390/info17040395

---

<!-- PAGE 29 -->

Reproduced with permission of copyright owner. Further reproduction

prohibited without permission.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

informatio n
Review
Deep Learning for Credit Risk Prediction: A Survey of Methods,
Applications, and Challenges
IbomoiyeDomorMienye ,EbenezerEsenogho* andCameronModisane
CentreforArtificialIntelligenceandMultidisciplinaryInnovations,DepartmentofAuditing,Collegeof
AccountingSciences,UniversityofSouthAfrica,Pretoria0002,SouthAfrica;emienyid@unisa.ac.za(I.D.M.);
modistc@unisa.ac.za(C.M.)
* Correspondence:esenoe@unisa.ac.za
Abstract
Creditriskpredictioniscentraltofinancialstabilityandregulatorycompliance,guiding
lendingdecisionsandportfolioriskmanagement. Whiletraditionalapproachessuchas
logisticregressionandtree-basedmodelshavelongbeentheindustrystandard, recent
advancesindeeplearning(DL)haveintroducedarchitecturescapableofcapturingcomplex
nonlinearities, temporaldynamics, andrelationaldependenciesinborrowerdata. This
studyprovidesacomprehensivereviewofDLmethodsappliedtocreditriskprediction,
coveringmulti-layerperceptron,recurrentandconvolutionalneuralnetworks,transformer,
andgraphneuralnetworks. Weexaminebenchmarkandlarge-scaledatasets,highlight
peer-reviewed applications across corporate, consumer, and peer-to-peer lending, and
evaluatethebenefitsofDLrelativetoclassicalmachinelearning. Inaddition,wecritically
assess key challenges and identify emerging opportunities. By synthesising methods,
applications,andopenchallenges,thispaperoffersaroadmapforadvancingtrustworthy
deeplearningincreditriskmodellingandbridgingthegapbetweenacademicresearch
andindustrydeployment.
Keywords: credit risk prediction; deep learning; convolutional neural networks;
transformers;machinelearning
1. Introduction
Credit risk prediction is a fundamental component of financial risk management,
enablinginstitutionstoevaluatethelikelihoodofborrowerdefaultandtomakeinformed
lending decisions [1–3]. Accurate modelling of credit risk supports financial stability,
reducesloanlosses,andcontributestoregulatorycompliance. Traditionally,logisticregres-
sion(LR)hasbeenthedominantmodelincreditscoringduetoitssimplicity,interpretability,
andeaseofdeploymentinregulatedenvironments[4]. However,asfinancialdatasetshave
AcademicEditors:Agnes
Vathy-FogarassyandJánosAbonyi growninsizeandcomplexity,conventionalLRmodelshavestruggledtocapturenonlinear
relationshipsandinteractionsamongfeatures. Thislimitationhasmotivatedtheadoption
Received:6December2025
Revised:25February2026 ofmoreadvancedmachinelearning(ML)methodssuchasrandomforests,supportvector
Accepted:27February2026 machines(SVMs),andgradientboosting,whichoftenachievehigherpredictiveaccuracy
Published:21April2026 butattheexpenseofinterpretability[5–7].
Copyright:©2026bytheauthors. Deeplearninghasbroadenedcreditriskmodellingbyenablingrepresentationlearning
LicenseeMDPI,Basel,Switzerland.
onborrowerdatathatisnonlinear,time-dependent,andsometimesnetworked. Recent
Thisarticleisanopenaccessarticle
work explores feed-forward tabular networks, sequence models, attention-based trans-
distributedunderthetermsand
formers, and graph neural networks to capture signals that are difficult to express in
conditionsofthe CreativeCommons
Attribution(CCBY)license. conventionalscorecards[8–10].
Information2026,17,395 https://doi.org/10.3390/info17040395

Information2026,17,395 2of28
Alongsidethesemethodologicaldevelopments,agrowingbodyofsurveyworkhas
reviewed credit risk models and related financial risk applications, as summarised in
Table1.EarlysystematicreviewsbyBhatoreetal.[11],Shietal.[12],Noriegaetal.[13],and
Montevechietal.[14]focusonML-basedcreditscoring,synthesisingalgorithms,datasets,
and evaluation metrics but treating deep neural networks largely as one model family
amongmany. Otherreviewsconcentrateonspecificperspectives: Kimetal.[15]andÇallı
andCos¸kun[16]examinecorporatedefaultpredictionandlong-rundefaultpredictors,
while Mhlanga [17] discusses ML- and AI-enabled credit assessment in the context of
financialinclusion. Deeplearning-centredsurveys,suchasHayashi[18],PengandYan[19],
Hoyosetal.[20],andDemmaetal.[21],identifyemergingDLtechniquesforcreditscoring
andbroaderfinancialrisk,butmainlyemphasisetabularmodelsanddonotsystematically
coversequential,transformer,andgraph-basedarchitecturesforborrower-levelcreditrisk.
Meanwhile,Mienyeetal.[22]providedabroadoverviewofDLinfinancialservices,yetits
treatmentofcreditriskwasatahigh-level. Inshort,muchofthereviewliteratureeither
prioritisesbroadMLcoverage,narrowsdeeplearningdiscussiontotabularscorecard-style
settings,ortreatsresponsibleAItopicswithoutamodel-family-levelsynthesistailoredto
borrower-levelcreditrisk.
This study addresses that gap by organising modern deep learning methods for
borrower-levelcreditriskprediction,cataloguingrecentpeer-reviewedapplications,and
synthesising deployment-relevant challenges and research opportunities. We focus on
borrower-,facility-,andfirm-levelsettingswheretheobjectiveistoestimatedefault-related
outcomesoveraspecifiedpredictionhorizonusingapplication,behavioural,bureau,trans-
actional,textual,orrelationaldata. Theprimarytargetisprobabilityofdefault(PD)and
closelyrelateddelinquencyoutcomes. Thereviewedevidencecoversconsumerlending,
SMElending,corporatecredit,andpeer-to-peerlendingusingbothpublicbenchmarks
andinstitution-scaledatasetsreportedinpeer-reviewedstudies. Weexcludeworkthat
focusesonmarketorliquidityrisk,portfoliooptimisationwithoutborrower-levellabelling,
orpurelymethodologicalcontributionsthatdonotevaluateonanempiricalcredit-risk
task. Themaincontributionsofthispaperareasfollows:
• Wepresentaunifiedoverviewofcreditriskpredictiontasksandbenchmarkdatasets,
andtracetheevolutionfromlogisticregressiontodeeparchitectures,includingMLPs,
CNNs, RNNs, transformers, and GNNs, highlighting how each class aligns with
differentcredit-riskobjectivesanddatamodalities.
• Weprovideamodality-awaresynthesisofrecentdeeplearningapplicationsincredit
risk,organisingstudiesbytabular,sequential,transformer-based,andgraph-based
models,andcollatingtheirdatasets,architectures,andreportedperformance.
• WecriticallyanalysemethodologicalandoperationalchallengesfordeployingDL-
basedcreditriskmodelsandderiveconcreteresearchdirectionsfordevelopingtrust-
worthy,regulation-readydeeplearningsolutions.
Theremainderofthispaperisorganisedasfollows. Section2presentsthereview
methodology. Section3providesanoverviewofcreditriskpredictiontasksandcommonly
used datasets. Section 4 traces the evolution from statistical to deep learning models,
detailing key architectures. Section 5 reviews peer-reviewed DL applications in credit
riskacrossdatamodalities. Section6presentsasynthesisofmajorchallengesandfuture
researchdirections. Section7concludesthepaper.
https://doi.org/10.3390/info17040395

Information2026,17,395 3of28
Table1.Summaryofrelatedreviewsoncreditriskmodellingandfinancialriskprediction.
Study Year Scope
BestpracticesforresponsibleMLincreditscoring,coveringfairness,explainability,
Valdrighietal.[23] 2025
andgovernance.
Pazetal.[24] 2025 SystematicreviewofMLandmetaheuristicsforindividualcreditriskassessment.
SystematicreviewofdefaultpredictionMLmodelsandtheirroleinstrengthening
Alvietal.[25] 2024
creditriskmanagement.
Montevechietal.[14] 2024 Comprehensivereviewofstate-of-the-artMLmodelsforcreditrisk.
DemmaWubeetal.[21] 2024 ReviewofMLandDLtechniquesforcreditscoring.
SystematicreviewofMLmethodsforcreditriskprediction,withemphasisonalgo-
Noriegaetal.[13] 2023
rithms,datasets,andperformancemetrics.
Comprehensivestudyofcreditriskevaluationmethods,includingstatisticalandML
Bhattacharyaetal.[26] 2023
models.
SystematicreviewofDL-basedcreditriskassessmentsystems,summarisingarchitec-
Hoyosetal.[20] 2023
tures,applicationsettings,andevaluationmeasures.
Review of emerging trends in DL for credit scoring, focusing on neural network
Hayashi[18] 2022
architectures,featurelearning,andinterpretability.
AsurveyofML-drivencreditrisk,organisingalgorithms,datasources,andevaluation
Shietal.[12] 2022
methods.
ÇallıandCos¸kun[16] 2021 Longitudinalsystematicreviewofcreditriskassessmentanddefaultpredictors.
Review of ML for credit risk assessment in the context of financial inclusion in
Mhlanga[17] 2021
emergingeconomies.
SurveyofDLforfinancialriskpredictionacrossmultipletasks,withcreditriskas
PengandYan[19] 2021
oneapplicationarea.
EmpiricalstudyonwhenDLisbeneficialforcreditscoring,practicaladoption,and
Gunnarssonetal.[27] 2021
comparisonwithtraditionalscoring.
SystematicreviewofMLtechniquesforcreditriskevaluation,coveringclassifiers,
Bhatoreetal.[11] 2020
featureselection,andbenchmarkdatasets.
Literaturereviewofcorporatedefaultpredictionmodels,summarisingstatisticaland
Kimetal.[15] 2020
MLapproaches.
2. ReviewMethodology
Weconductedastructuredliteraturesearchandscreeningexercisetoassemblerecent
peer-reviewedworkondeeplearningforborrower-levelcreditriskprediction. Thegoal
isacomprehensiveandtransparentnarrativesynthesisofthefieldratherthanaformal
systematicreviewormeta-analysis.
Tocoverbothcomputingandfinanceoutlets,wesearchedIEEEXplore,Scopus,ACM
Digital Library, ScienceDirect, SpringerLink, Web of Science, and Google Scholar. Web
ofSciencewasincludedtobroadencoverageoffinanceandoperationsresearchvenues
that are not always well represented in engineering-focused indexes. Queries paired
credit-riskterms(e.g.,creditscoring,defaultprediction,probabilityofdefault)withdeep
learningterms(e.g.,CNN,RNN,LSTM,GRU,Transformer,graphneuralnetwork). Where
supported,werestrictedsearchestotitle/abstract/keywordsandrefinedqueryvariants
iterativelyusinghighlycitedseedpaperstolimitirrelevantreturns. Wetargetedjournal
articles and full conference papers from 2015 to 2025, and added foundational earlier
studiesviabackward/forwardcitationtracking.
https://doi.org/10.3390/info17040395

Information2026,17,395 4of28
SearchStrategyandScreeningProtocol
Theinitialsearchidentifiedapproximately380recordsacrossalldatabasesaftermerg-
ingresults. Duplicaterecordswereremovedusingtitle,author,venue,andyearmatching.
Followingde-duplicationandremovalofclearlyout-of-scoperecords,208studieswere
retainedfortitleandabstractscreening,assummarisedinFigure1. Theremainingstudies
werescreenedintwostages: (i)titleandabstractscreening,followedby(ii)full-textassess-
ment. Duringtitleandabstractscreening,studieswereexcludediftheyfocusedexclusively
on market or liquidity risk, macroeconomic default modelling without borrower-level
prediction,ormethodologicaldeeplearningcontributionswithoutanempiricalcreditrisk
application. Full-textscreeningwasthenusedtoconfirmrelevance,extractmethodological
details,andverifythatthestudyaddressedborrower-,facility-,orentity-levelcreditrisk.
Figure1.PRISMAflowchartoftheliteraturesearchandscreeningprocessusedinthissurvey.The
diagramsummarisesdatabasequerying,de-duplication,titleandabstractscreening,andfull-text
eligibilityassessment.
Studieswereincludediftheysatisfiedatleastoneofthefollowingcriteria:(i)proposed
orempiricallyevaluatedadeeplearningarchitectureforcreditriskprediction;(ii)provided
asurveyorstructuredreview ofmachinelearningordeep learningmethodsforcredit
risk;or(iii)addressedinterpretability,fairness,robustness,orgovernanceexplicitlyina
creditriskcontext. Meanwhile,studieswereexcludediftheylackedquantitativeevalu-
ation,providedinsufficientmethodologicaldetailtoassessthelearningarchitecture,or
focusedsolelyonregulatoryorpolicydiscussionwithoutamodellingcomponent. Unlike
systematic reviews, no strict performance-improvement threshold was imposed; how-
ever,studieswererequiredtoreportatleastonestandardevaluationmetrictosupport
empiricalcomparison.
https://doi.org/10.3390/info17040395

Information2026,17,395 5of28
Thefinalcorpuscomprises140deeplearningapplicationstudiesand18surveyor
guidelinepapers. Foreachincludedstudy,werecordedthedatamodality(tabular,sequen-
tial,textual,orrelational),modelarchitecture(MLP,CNN,RNN/LSTM/GRU,Transformer,
GNN,orhybrid),creditproductsegment(consumer,SME,corporate,interbank,ormixed),
predictiontarget,andreportedevaluationmetrics. Wedidnotapplyaformalrisk-of-bias
scoringprotocol(giventhenon-systematicscopeandheterogeneousstudydesigns),butwe
extractedreportingattributesrelevanttointerpretability,validationdesign(e.g.,out-of-time
vsrandomsplits),anddeploymentconsiderationswhereavailable. Theseattributesunder-
pinthetaxonomyusedinSections4and5,andtherelatedsurveyliteratureissummarised
inTable1.
3. OverviewofCreditRiskPredictionandDatasets
Creditriskreferstothepotentiallossthatalenderorinvestorfaceswhenaborrower
failstomeetcontractualfinancialobligations[17]. Accuratecreditriskpredictionisfunda-
mentaltofinancialstability,guidingcapitalallocation,pricing,andprovisioningdecisions
underregulatoryframeworkssuchasBaselIII.Traditionally,creditriskhasbeenassessed
throughstatisticalscorecardsandexpertjudgment;however,theriseofdata-drivenlending
and digital credit platforms has produced large-scale, high-dimensional borrower data
thatdemandmoreadvancedmodellingapproaches. Thissectionprovidesanoverviewof
thekeypredictivetasksincreditriskmanagementandsummarisesbenchmarkdatasets
commonlyemployedinempiricalstudies.
3.1. CreditRiskPredictionTasks
Credit risk prediction aims to estimate the likelihood and magnitude of potential
lossesassociatedwithlendingactivities. Inregulatoryandresearchpractice,threemain
quantitativetasksaretypicallyaddressed:
• ProbabilityofDefault: Thelikelihoodthataborrowerwillfailtomeetcontractual
repaymentobligationswithinaspecifiedhorizon. PDmodellingformsthefoundation
ofmostcreditscoringsystemsandrisk-basedpricingframeworks[28].
• LossGivenDefault(LGD):Theproportionoftheexposurethatisnotrecoveredinthe
eventofdefault,reflectingcollateralvalues,recoveryprocesses,andlegalcosts[29].
• ExposureatDefault(EAD):Thetotaloutstandingamountalenderisexposedtowhen
defaultoccurs,whichisparticularlyimportantforrevolvingfacilitiessuchascredit
cardsandoverdrafts[30].
Acrossthereviewedliterature,PD-styletargets(defaultorcloselyrelateddelinquency
outcomes)dominate,andtheyformtheprimarybasisforcomparingdeeplearningmodel
familiesinthissurvey. Predictionhorizonsandlabeldefinitionsvaryacrossstudiesand
products; where reported, we capture these details in the study summaries to support
consistent interpretation. LGD and EAD are discussed only in studies that explicitly
modelthemusingdeeparchitectures,reflectingtheircomparativelylimitedcoveragein
thedeeplearningcredit-riskliterature. ThesequantitiesdeterminetheExpectedLoss(EL),
acornerstoneofrisk-weightedasset(RWA)calculationinBaselframeworks,definedas:
EL = PD×LGD×EAD. (1)
ThoughELiscrucialincreditrisk,itisinconsistentlyreportedandisnotcomparable
across heterogeneous datasets and horizons in the surveyed studies. Accordingly, the
synthesis in Section 5 focuses on the evaluation metrics most commonly reported for
PD-styleprediction.
https://doi.org/10.3390/info17040395

Information2026,17,395 6of28
3.2. BenchmarkDatasets
Empiricalresearchoncreditriskfrequentlyreliesonbenchmarkdatasetstoevaluate
andcomparemodellingapproaches. Themostwidelyusedpublicdatasetsincludethe
GermanCredit,AustralianCredit,andTaiwanCreditCardDefaultdatasets,whichhave
becomestandardbaselinesforMLalgorithms. TheGermanCreditdataset,compiledby
theUCIMLRepository,contains1000loanapplicantswith20demographicandfinancial
attributeslabeledasgoodorbadcreditrisk[31]. TheAustralianCreditdatasetissmaller,
comprising690recordswithmixedcategoricalandnumericalfeaturesforbinarycredit-
worthinessclassification. TheTaiwanCreditCardDefaultdatasetissubstantiallylarger,
featuring30,000clientswithdetailedbilling,repayment,anddemographicinformation,
andiswidelyusedindeeplearningbenchmarks[32].
Whilethesedatasetsfacilitatereproducibilityandalgorithmiccomparison,theirlim-
itedsamplesizes,staticstructures,andlackoftemporalorbehaviouralfeaturesconstrain
generalisabilitytoreal-worldportfolios[33]. Smallbenchmarksalsocreatehigh-variance
evaluationregimesinwhichapparentperformancedifferencesareunstableandcanbe
driven by a few influential cases rather than a durable risk signal. For example, with
only1000observations,theGermanCreditdatasetcanyieldmateriallydifferentestimates
acrossrandomsplits,andhigh-capacitymodelsmayoverfitidiosyncraticcorrelationsthat
donottransfertonewborrowercohorts. Thiseffectiscompoundedbysample-selection
mechanismsthatareabsentorunobservedinpublicbenchmarks(e.g.,lenderacceptance
policiesandunderwritingrules),meaningtheobservedlabelsmayreflectafilteredsub-
populationratherthanthefullapplicantpool. Consequently,modelstrainedandreported
onsuchdatasetsoftenoverestimateout-of-sampleperformanceandunderstateuncertainty
incomparativeclaims.
Toaddresstheseshortcomings,contemporarystudiesincreasinglyadoptlargerand
more heterogeneous datasets. For example, the Home Credit Default Risk dataset [34]
includes over 300,000 loan applications enriched with demographic, behavioural, and
bureaurecords,representingacloserapproximationtoindustrialsettings. Similarly,the
LendingClubpeer-to-peerlendingdatasetcontainsmillionsoftransactionsandrepayment
records,enablinglarge-scaleevaluationsofensembleanddeeplearningmodels[35].
Despitetheseadvances,muchoftheacademicliteraturecontinuestorelyonsmall,
static benchmarks that fail to capture macroeconomic shifts and dynamic borrower be-
haviour. Bridgingthisgaprequireslongitudinal,multimodaldatasetswithexplicittime
structureandstablelabeldefinitions,sothatmodelscanbeevaluatedunderout-of-timeval-
idationandassessedfordrift,calibrationdecay,andsubgroupperformance. Suchdatasets
areessentialforbenchmarkingemergingdeeplearningarchitecturesunderrealisticand
regulatory-compliantconditions(Table2).
Table2.SummaryofBenchmarkDatasetsCommonlyUsedinCreditRiskPrediction.
Dataset SampleSize Features Description
Demographicandfinancialattributeswithbinary
GermanCredit 1000 20
good/badcreditlabels.
Mixedcategoricalandnumericalfeaturesfor
AustralianCredit 690 14
creditworthinessclassification.
TaiwanCreditCardDefault 30,000 24 Clientpaymenthistory,billingamounts,anddemographics.
Realisticindustrialdatasetcombiningbehaviouraland
HomeCreditDefaultRisk 300,000+ 122
bureauinformation.
Peer-to-peerlendingrecords,includingloan,borrower,and
LendingClub Millions 100+
repaymentdetails.
https://doi.org/10.3390/info17040395

Information2026,17,395 7of28
4. EvolutionofModelsforCreditRisk
Creditriskmodellinghasprogressedfrominterpretablelinearmethodstodeeparchi-
tecturesthatcapturenonlinearinteractions,sequentialbehaviour,andrelationaldependen-
ciesamongborrowers. Thissectionreviewsthemethodologicalevolutionacrossthemain
modelfamilies.
4.1. LogisticRegressionandClassicalMachineLearning
Logistic regression (LR) remains the cornerstone of credit scoring due to its trans-
parencyandregulatoryacceptance[36,37]. Giveninputfeaturesx ∈ Rd andparameters
(w,b),LRmodelstheprobabilityofdefaultas:
1
P(y =1| x) = σ(w ⊤ x+b) = , (2)
1+exp(−w⊤x−b)
whereσ(·)isthelogisticsigmoidandy ∈ {0,1}denotesdefaultstatus. Despiteitssim-
plicity,LRassumesalinearlog-oddsrelationship,limitingitsabilitytocapturenonlinear
featureeffectsandinteractionsinhigh-dimensionaldata. SubsequentclassicalMLmodels,
suchassupportvectormachines,randomforests,andgradientboosting,enhancedflexibil-
itybylearningnonlineardecisionboundaries. ThesemethodstypicallyoutperformLRin
accuracybutatthecostofinterpretability,motivatingsubsequentresearchintomodelsthat
balancebothproperties[5].
4.2. EarlyDeepLearningforTabularCreditRisk
Theintroductionofdeeplearningbroughtneuralarchitecturescapableoflearning
complex,nonlineartransformationsdirectlyfromtabularcreditdata. Unliketraditional
logistic regression (LR), which models linear relationships, deep neural networks can
capturehierarchicalfeatureinteractionsthroughmultiplehiddenlayers. Amulti-layer
perceptron (MLP), illustrated in Figure 2, extends LR by stacking hidden layers with
nonlinearactivationsthatenabletheautomaticextractionoflatentfeaturerepresentations.
Mathematically,theforwardpropagationinanMLPisgivenby:
h (l) = ϕ(W (l) h (l−1)+b (l)), (3)
whereϕ(·)denotesanonlinearactivationfunctionsuchasReLU.Thishierarchicalstructure
allows MLPs to approximate complex functions on large datasets, thereby uncovering
nonlinearrelationshipsbetweenborrowercharacteristicsanddefaultprobabilities[38].
Figure2.Basicstructureofafeed-forwardneuralnetworkusedfortabularcreditdata.Thenetwork
consistsofaninputlayer,oneormorehiddenlayerswithnonlinearactivations,andanoutputlayer
fordefaultprediction.
https://doi.org/10.3390/info17040395

Information2026,17,395
8of28
4.3. SequentialandTemporalBehaviourModelling
Creditworthinessevolvesovertimeasborrowersmakerepayments,accumulatebal-
ances,adjustspendingbehaviour,orexperienceincomefluctuations. Sequentialneural
networksexplicitlymodelthesebehaviouraltrajectoriesbycapturingtemporaldependen-
ciesthatstaticmodelscannot. Thesearchitecturesprocesscredit-relatedsequences—such
asmonthlyrepaymenthistories,rollingutilisationrates,ordelinquencytransitions—ina
step-wisemanner,enablingtheextractionoflong-rangebehaviouralpatterns. Recurrent
neuralnetworks(RNNs)formthefoundationforsequentialmodelling. Ateachtimestept,
anRNNupdatesitshiddenstateaccordingto
|     |     | h   | =tanh(W | h t−1 | +W x +b), |     |     | (4) |
| --- | --- | --- | ------- | ----- | --------- | --- | --- | --- |
|     |     | t   |         | h     | x t       |     |     |     |
wherex istheinputvectorattimet,h isthehiddenstate,W andW arelearnableweight
| t   |     |     |     | t   |     | h   | x   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
matrices,andbisabiasterm. AlthoughRNNscancaptureshort-termtemporalstructure,
theystrugglewithlong-rangedependenciesduetovanishinggradients[39].
4.3.1. LongShort-TermMemoryNetworks
ToaddressthelimitationsofstandardRNNs,longshort-termmemory(LSTM)net-
worksintroducegatingmechanismsthatregulateinformationflowandpreservelong-term
temporalpatterns. TheLSTMarchitecture(Figure3)usesthreegates—forget,input,and
| output—toupdateaninternalmemorycellC |     |     |     | :   |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     | f =        | σ(W [h   | ,x     | ]+b ),     |     |           |     | (5) |
| --- | ---------- | -------- | ------ | ---------- | --- | --------- | --- | --- |
|     | t          | f        | t−1    | t f        |     |           |     |     |
|     | i t =      | σ(W i [h | t−1 ,x | t ]+b i ), |     |           |     | (6) |
|     | C˜ =tanh(W |          | [h     | ,x ]+b ),  |     |           |     | (7) |
|     | t          |          | c t−1  | t c        |     |           |     |     |
|     | C =        | f ⊙C     | +i     | ⊙C˜        |     |           |     |     |
|     | t          | t        | t−1    | t t ,      |     |           |     | (8) |
|     | o =        | σ(W [h   | t−1 ,x | ]+b ),     | h = | o ⊙tanh(C | ),  | (9) |
|     | t          | o        |        | t o        | t   | t         | t   |     |
Here,thehiddenstateandcellstatearedenotedbyh andC ,respectively,andx isthe
|     |     |     |     |     | t   | t   |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
inputvectorattimestept. Thegates f t ,i t ,ando t controlforgetting,updating,andoutput,
| whileC˜ |     |     |     | σ(·)isthesigmoidactivationfunctionand⊙ |     |     |     |     |
| ------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
t denotesthecandidatecellupdate.
denoteselementwisemultiplication[40].
Figure3. ArchitectureoftheLSTMnetworkshowinggatingmechanismsforinput, forget, and
outputregulation.
https://doi.org/10.3390/info17040395

Information2026,17,395
9of28
4.3.2. GatedRecurrentUnitNetworks
Thegatedrecurrentunit(GRU),illustratedinFigure4,simplifiestheLSTMarchitec-
turebyusingasinglestatevariableandtwogates. GRUscomputetheirhiddenstateusing:
|     | z = | σ(W [h | ,x ]+b   | ),  |     | (10) |
| --- | --- | ------ | -------- | --- | --- | ---- |
|     | t   | z      | t−1 t    | z   |     |      |
|     | =   | σ(W [h | ]+b      | ),  |     |      |
|     | r t | r      | t−1 ,x t | r   |     | (11) |
h˜
|     | =tanh(W |      | [r ⊙h   | ,x ]+b | ),  | (12) |
| --- | ------- | ---- | ------- | ------ | --- | ---- |
|     | t       |      | h t t−1 | t      | h   |      |
|     | h =     | (1−z | )⊙h +z  | ⊙h˜    | ,   | (13) |
|     | t       |      | t t−1   | t      | t   |      |
wherex istheinputvectorattimesteptandh istheGRUhiddenstate. Thevectorsz and
| t   |     |     | t   |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- |
r denotetheupdateandresetgates,respectively,andh˜ isthecandidatehiddenstate[39].
| t   |     |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- |
Figure4. ArchitectureoftheGRUnetwork,highlightingtheupdateandresetgatesthatcontrol
informationflowacrosstimesteps.
4.3.3. TemporalConvolutionalNetworks
Temporalconvolutionalnetworks(TCNs)offeranalternativetorecurrentarchitectures
byapplyingone-dimensionaldilatedconvolutionstocapturelong-rangedependencies
withoutrecursion:
K−1
= ∑
|     |     | h t | W k x | t−d·k , |     | (14) |
| --- | --- | --- | ----- | ------- | --- | ---- |
k=0
whereddenotesthedilationfactorandKthekernelsize[41]. UnlikeRNNsandLSTMs,
TCNs process sequences in parallel, preserving causality through zero-padding while
enablingefficienttrainingonlongtemporalwindows[42,43]. ThispropertymakesTCNs
particularlyvaluableforhigh-frequencyrepaymentdataandreal-timetransactionstreams
whereparallelcomputationandlong-horizonforecastingareadvantageous.
4.4. ConvolutionalandHybridArchitectures
CNNs,thoughhistoricallyassociatedwithimageprocessing,havebecomeeffective
tools for modelling structured financial sequences [44]. In credit risk, one-dimensional
convolutionsslidelearnablefiltersoverborrowerhistories—capturinglocaltemporalpat-
ternssuchasconsecutivedelinquencies,abruptutilisationjumps,orirregularrepayment
intervals. Thesefiltersextractshort-rangebehaviouralmotifswhilesharingparameters
acrosstimesteps,yieldingmodelsthatarebothcomputationallyefficientandlessprone
https://doi.org/10.3390/info17040395

Information2026,17,395 10of28
to overfitting than dense architectures. Figure 5 illustrates this structure, where con-
volutional and pooling layers form hierarchical representations of borrower behaviour
beforeclassification.
Figure5.BasicCNNarchitectureadaptedforone-dimensionalfinancialsequences.Convolutional
andpoolinglayerscapturelocalrepaymentorutilisationpatterns,whicharethenpassedtodense
layersforclassification.
SeveralstudiesreportthatCNN-basedsequenceencodersarecompetitivewithre-
currentarchitecturesincredit-risksequencemodellingwhenlocalbehaviouralpatterns
dominatethesignal,whileofferingfastertrainingduetoparallelism[44,45]. Theirpar-
allelism offers significant speed advantages for large portfolios, and their stable train-
ingdynamicsmakethemwellsuitedforindustrialsettingswhererapidretrainingand
consistentconvergencearerequired. Thishasmotivatedhybridcredit-riskmodelsthat
integrate CNN modules with other deep architectures. Wide–deep networks combine
alinearbranch—reflectingscorecard-styleinterpretability—withnonlineardeepcompo-
nents that capture higher-order interactions. Other hybrids, such as CNN–LSTM and
CNN–Transformermodels,leverageconvolutionstoencodeshort-termbehaviourbefore
passingfeaturestorecurrentorattention-basedlayerstocapturelong-rangedependen-
cies. These designs offer a practical balance between interpretability, expressive capac-
ity, and computational scalability, making them increasingly relevant in modern credit
riskpipelines.
4.5. Transformer
Transformerarchitecturesintroduceafundamentallydifferentapproachtomodelling
sequenceandtabularcreditdatabyreplacingrecurrencewithself-attention,enablingthe
captureofglobaldependenciesinparallelratherthanstepwise[46]. Insteadofprocessing
borrowerhistorieschronologically,asRNNsdo,thetransformercomputespairwiseinter-
actionsacrossallfeaturedimensionsortimestepssimultaneously. Thecoreself-attention
mechanismisdefinedas:
(cid:32) (cid:33)
QK⊤
Attention(Q,K,V) =softmax √ V, (15)
d
k
https://doi.org/10.3390/info17040395

Information2026,17,395 11of28
whereQ,K,andVdenotethequery,key,andvaluematricesrepresentinglatentprojections
of input features or time steps, and d is a scaling constant to stabilise gradients. This
k
formulation enables the model to assign adaptive relevance weights across the entire
behaviouralsequence,allowingittocapturelong-rangedelinquencysignatures,cyclical
utilisationtrends,andcross-featureinteractionsthattraditionalrecurrentnetworksstruggle
toretain.
Recentadaptationsdemonstratehowtransformerscanberepurposedfromnatural
languageprocessingtostructuredfinanciallearning. TabTransformer[47]contextualises
categoricalembeddings,improvingdiscriminationontabularcreditdatasetswithhigh-
cardinalitysocio-economicattributes.
4.6. GraphNeuralNetworks
Borrowers often participate in interdependent financial ecosystems through co-
applicantties,sharedemployers,guarantorstructures,fund-flowrelationships,orsupply-
chain linkages. These relational patterns give rise to correlated credit exposures and
potential contagion pathways that cannot be represented in i.i.d. tabular data. Graph
neuralnetworks(GNNs)modelsuchrelationaldependenciesviaiterativemessagepassing,
whereeachnodeupdatesitsrepresentationbyaggregatingtransformedmessagesfrom
neighbouringnodes. Thegenericupdateruleforamessage-passinglayerisexpressedas
 
h (
v
l+1) = σ ∑ 1 W (l) h (
u
l) , (16)
c
u∈N(v) vu
whereh
(l)
istheembeddingofborrowervatlayerl,N(v)denotesneighbouringnodes(e.g.,
v
borrowers,firms,accounts,orcounterpartiesconnectedthroughownership,transactions,
orcontractualties),c isanormalisationcoefficient(e.g.,nodedegree),W(l) isalearnable
vu
weight transform, and σ(·) is a nonlinear activation. Figure 6 visualises this pipeline:
neighbours send learned messages, the messages are pooled, and the central borrower
embeddingisupdatedtoreflectrelationalcreditriskfactors.
Figure6.MessagepassingmechanisminaGNNforborrowernetworks.Neighbouringborrower
representationsarecollected,aggregated,andusedtoupdateeachnode,enablingpropagationof
financialinfluencesignals.
Table3summarisesthevariousDLarchitecturesforcreditriskmodelling.
https://doi.org/10.3390/info17040395

Information2026,17,395
12of28
Table3.Summaryofdeeplearningarchitecturesdiscussedforcreditriskmodelling.
ModelClass InputModality CoreMechanism Credit-RiskStrengths KeyLimitations
Learnscomplex
Notemporalorrelational
|     |                 | Feed-forwardnon-linear | interactionsbeyond        |                   |
| --- | --------------- | ---------------------- | ------------------------- | ----------------- |
| MLP | Tabularfeatures |                        |                           | reasoning;feature |
|     |                 | transformation         | linearscorecards;scalable |                   |
engineeringrequired
andeasytodeploy
Capturesonlylocal
Detectsrepaymentand
|     | Sequential/behavioural | Localshared-weight      |                             | temporalpatterns;       |
| --- | ---------------------- | ----------------------- | --------------------------- | ----------------------- |
| CNN |                        |                         | utilisationmotifs;efficient |                         |
|     | time-series            | convolutionswithpooling |                             | struggleswithlong-range |
trainingandparallelisable
dependencies
|     |     |     | Modelslong-term | Trainingcostincreases |
| --- | --- | --- | --------------- | --------------------- |
RecurrentModels(RNN, Temporalbehavioural Hiddenstatepropagation delinquency,repayment withlongsequences;
LSTM,GRU) sequences withgating evolution,and vanishinggradients;
|     |     |     | behaviouraldrift | limitedparallelism |
| --- | --- | --- | ---------------- | ------------------ |
Capturesglobal
|     |     | Globalmulti-head | temporal/feature | Requireslargerdata |
| --- | --- | ---------------- | ---------------- | ------------------ |
Transformers Tabularorsequentialdata self-attention,contextual interactions;scalable volumeandtuning;less
|     |     | embeddings | training;interpretability | effectiveontinydatasets |
| --- | --- | ---------- | ------------------------- | ----------------------- |
viaattention
|     |     | Iterativemessagepassing | Modelscontagioneffects, | Requiresgraph |
| --- | --- | ----------------------- | ----------------------- | ------------- |
Relationalborrower systemicdependencies, construction;sensitiveto
| GNNs |          | andneighbour |               |                 |
| ---- | -------- | ------------ | ------------- | --------------- |
|      | networks |              | andhiddenrisk | noiseandmissing |
aggregation
|     |     |     | propagation | relationships |
| --- | --- | --- | ----------- | ------------- |
Balancesinterpretability,
Heterogeneousdata Combinedfeature scalability,and Increasedcomplexity;
HybridArchitectures(e.g.,
(tabular,text,sequence, extractorsandfusion multimodallearning; hardertointerpretand
CNN–LSTM)
|     | network) | layers | strongestperformanceon | validateforregulation |
| --- | -------- | ------ | ---------------------- | --------------------- |
real-worlddata
5. NotableDLApplicationsinPeer-ReviewedCreditRiskStudies
Thissectionsynthesisespeer-reviewedapplicationsofdeeplearningtocreditrisk. We
mapempiricalstudiestothesamethreeaxes: modality,architecture,andobjective,and
reporttheevaluationmetricstheyusedandthequantitativeperformanceobtained.
5.1. TabularDeepNetworksforCreditRisk
Deep learning for tabular borrower data has evolved from simple multilayer per-
ceptrons(MLPs)tospecialisedarchitecturesthatleverageregularisation, attention, em-
beddings, and hybrid ensembling. This subsection reviews representative studies that
applydeeptabularmodelstocorporate,retail,andinstitutionallendingdata,highlighting
methodologicalcontributions,empiricalfindings,andcomparativeperformancerelativeto
conventionalMLmodels.
Yangetal.[48]proposedahigh-dimensionaldeepneuralnetwork(HDNN)forcorpo-
ratecreditriskusingsupply-chainaugmentedfinancialdata. Theirmodelincorporated
combined L1–L2 penalties to address feature sparsity and batch-normalisation effects,
achievinganaccuracyof80.12%,outperforminglogisticregression(areaunderthereceiver
operatingcharacteristiccurve(AUC)=0.717),supportvectormachines(AUC=0.738),and
astandardneuralnetworkbaseline(AUC=0.692). Linetal.[49]introducedapenalised
deepneuralnetwork(PDNN)basedonsurvivalmodelling,embeddingaone-to-onepe-
nalisationlayerthatsupportedvariableselectionalongsidetime-to-defaultestimationon
peer-to-peerlendingdata,consistentlyoutperformingnon-penaliseddeepvariants.
Recentstudieshavefurtherexaminedinterpretabilityandprofit-awareoptimisation
withindeeptabularlearning. Asenciosetal.[50]comparedMLP,XGBoost,andTabNet
on36,402Peruviancooperative-lendingapplicationsusingregression-basedprofitscor-
ing. XGBoost achieved the best results (R2 = 0.7906), although TabNet (R2 = 0.7465)
offeredmoretransparentfeature-levelinterpretabilitythroughattentiveembeddings. In
large-scalesettings,WangandZhang[51]proposedaTabNet-Stackingensemblethatinte-
https://doi.org/10.3390/info17040395

Information2026,17,395 13of28
gratedTabNet,XGBoost,LightGBM,CatBoost,SVM,andKNN,reachingaccuracy=0.979,
recall=0.856,F1=0.817,andAUC=0.941ontheTianchidataset(≈800,000cases),sub-
stantiallyoutperformingsingle-modelbaselines.
Beyondarchitecturedesign,explainabilityhasbecomecentraltotabulardeeplearning
deployment. Hjelkrem and de Lange [52] trained an MLP using open banking transac-
tiondataandcompareditwithabidirectionalencoderrepresentationsfromtransformers
(BERT)-basedmodel,reportingthattheMLPachievedsuperiorpredictiveperformance
whilemaintainingpracticalexplainabilityusingSHAPattributionvisualisations. Their
resultsshowedthatSHAPdetectedintuitivebehaviouralriskfactors,supportingsuitability
forregulatedfinancialsettings. Lietal.[53]introducedanincrementalDNN(I-DNN)for
borrowercreditscoringonagriculturalmicroloanrecords(22,475examples),demonstrat-
ingAUCimprovementsrangingbetween1.4%and7.8%comparedwithstandardDNN,
XGBoost,andrandomforestbaselinesunderconceptdriftscenarios.
Advancesindeeptabularmodellinghavealsoexploredensemble-drivengeneralisa-
tion. Popovetal.[54]introducedNeuralObliviousDecisionEnsembles(NODE),replacing
discrete tree splits with differentiable soft-gating, producing competitive performance
withgradientboostingwhileenhancingdifferentiabilityandcalibrationunderstochastic
optimisation. Buildingonensemblereasoning,ShanandGao[55]proposedanenhanced
TabNetstackingmodelforSMEsupply-chainfinancialriskpredictionusingmulti-stage
optimisation, achievingAUC=0.9616andAccuracy=0.9277, outperformingstandard
TabNet,LightGBM,andCatBoostbaselines.
TheseworksdemonstratethattabularDLhasadvancedfromsimplefeed-forwardnet-
workstowardarchitecturesthatintegrateregularization,attention,andensemblelearning.
Overall,thesestudiessuggestthatdeeptabularmodelsareoftencompetitivewithstrong
tree-based ensembles on larger datasets, particularly when the feature space includes
high-cardinality categorical variables, complex interactions, or multimodal extensions
that benefit from representation learning. On smaller benchmarks, reported gains are
frequently modest and can be sensitive to split design and tuning, meaning gradient
boostingremainsastrongandfrequentlyhard-to-beatbaseline. Deepnetworkstherefore
complementratherthanreplaceclassicalmethods,withtheirmainadvantagearisingwhen
datascale,heterogeneity,orunifiedmultimodalpipelinesjustifytheaddedmodellingand
operationalcomplexity.
5.2. SequentialModelsandEvent–TimeTargets
Sequentialdeeplearningapproachesmodeltheevolutionofborrowerorportfolio
behaviour over time, offering substantial advantages over static classifiers that ignore
risktrajectories. Thesemodelscapturetemporalpatternslinkedtorepaymentbehaviour,
behaviouraldrifts,cyclicalspending,macroeconomicshocks,andpost-originationdelin-
quency paths. Compared with conventional panel regression and tree-based models,
sequential architectures integrate information across ordered observations and enable
dynamicprobability-of-defaultestimationratherthanstatic,single-pointpredictions.
Liang and Cai [56] applied long short-term memory (LSTM) networks to forecast
monthlydefaultratesontheLendingClubpeer-to-peerplatform. TheLSTMconsistently
outperformedARIMA,SVM,andANNacrossmultiplecross-validationschemes,reducing
MAE from 0.095 to 0.072 and RMSE from 0.119 to 0.093. Further support for recurrent
credit modelling appears in Ala’raj et al. [57], who developed two behavioural LSTM
variants(MP–LSTMandPE–LSTM)forrealretailbankingcreditcardcustomers. Their
modelssurpassedSVM,RF,MLP,andLRbaselinesacrosspredictiveandcalibrationmetrics,
demonstratingthattemporalrepresentationlearningenhancesbehaviouraldefaultscoring
inoperationalsettings.
https://doi.org/10.3390/info17040395

Information2026,17,395 14of28
Beyond standard LSTMs, hybrid deep temporal architectures have gained promi-
nence. Zhang [58] proposed a CNN–LSTM attention model for enterprise credit risk,
achieving AUC = 0.92 and F1 = 0.91, outperforming CNN- and LSTM-only baselines.
Lietal.[59]extendedthisapproachforlistedcorporateriskandreportedthatCNNlayers
effectivelyextractshort-termtemporalmotifs,whileLSTMcomponentsencodelongerbe-
haviouraltransitions,confirmingthathierarchicaltemporalmodellingimprovesenterprise
creditdiscrimination.
Survival-drivenarchitecturesfurthergeneralisetemporalcreditmodellingbyestimat-
inghazardratherthanstaticoutcomes. Wangetal.[60]implementedadeepdiscrete-time
survivalmodelthatdecomposescreditoutcomesintoage,period,andcohortdimensions,
generatinginterpretablehazardcurveswithasmoothertemporalstructurethanclassical
econometric approaches. Chen and Long [61] similarly advanced temporal modelling
throughaself-attention-basedend-to-endcorporatecreditratingframework, whichre-
movedtheneedformanualfeatureaggregationandimprovedratingclassificationstability
relativetotraditionalMLcompetitors.
More recent developments incorporate fusion and cross-feature interaction within
sequential networks. Han et al. [62] introduced a default-prediction framework com-
bining self-attention with a cross-network mechanism, demonstrating that modelling
interactivetemporaldependenciesyieldshigheraccuracy,precision,recall,andF1-score
relativetostandarddeeplearningarchitectures. Shietal.[63]alsobenchmarkedCNN,
RNN, and DNN models in financial-sector credit scoring and observed that recurrent
architecturesmaintainedsuperiortemporalsensitivity,whileCNNsprovidedparameter
efficiencybenefits.
Bidirectional and residual-enhanced architectures have been explored to stabilise
recurrenttrainingandpreservelong-rangegradients. Yangetal.[64]introducedaresidual-
enhancedbidirectionallongshort-termmemory(BiLSTM)frameworkincorporatingmulti-
headattention,achievingAUC=0.982andF1=0.958ontheFreddieMacSingle-Family
dataset,outperformingBiLSTM,GRU,CNN,andRNNbaselines. Complementaryresearch
explorescouplingsequentialencoderswithprobabilisticreasoning: Zhang[65]integrated
LSTMencoderswithBayesiancalibrationmodules,achievingAUC=0.981andreducing
uncertaintymiscalibrationrelativetoRFandLRbaselines.
Theseresultsindicatethatsequentialarchitecturesaremostvaluablewhenlenders
possessrichpost-originationhistoriesorportfolio-leveltimeseriesandcareabouthowrisk
evolves,notjustwhetheraborrowereventuallydefaults. LSTM-andGRU-likemodels
offer clear gains for dynamic behavioural scoring and vintage-level forecasting, while
CNN–LSTM hybrids and survival-based networks help bridge the gap between point
predictionsandtime-to-eventoutcomes. However,theempiricalliftoverstrongtabular
baselines tends to appear only when sequences are sufficiently long and informative;
on static benchmarks with limited behavioural content, sequential models mainly add
complexitywithoutdeliveringcommensuratepracticalbenefit.
5.3. Transformer-BasedModelsforCreditRisk
Transformersrepresentamajordeparturefromrecurrentarchitecturesbyreplacing
sequentialrecurrencewithself-attention,enablingparallelcomputationandglobaldepen-
dencymodellingacrossfeatures,timesteps,ormodalities[46]. Thekeymechanism,scaled
dot-productattention,allowseachelementinasequenceorfeaturevectortoconditionon
allothers,overcominglong-termdependencylimitationstypicalofLSTMsandGRUs. This
propertyisattractiveincreditmodelling,wherebehaviouralvariables,categoricalfeatures,
andtext-basedsignalsinteractincomplex,non-localpatterns.
https://doi.org/10.3390/info17040395

Information2026,17,395 15of28
Earlyadoptionhasfocusedonadaptingthetransformerencodertotabularandbe-
havioural credit data. Huang et al. [47] introduced the TabTransformer, demonstrating
performancegainsonhigh-cardinalitycategoricalfinancialdatasetsbyreplacingconven-
tionalone-hotencodingswithcontextualembeddings. Gorishniyetal.[66]laterimproved
architectural efficiency with the FT-Transformer, showing that attention-based tabular
modelscanbecompetitivewithstrongtree-ensemblebaselinessuchasCatBoostandXG-
Boost on several tabular tasks, particularly when feature interactions are complex and
heterogeneouslydistributed. WangandXiao[67]extendedthisparadigmbyembedding
behaviouralsequencesalongsidestaticfeatures,achievingAUC=0.72andKS=0.32onan
onlinelendingdataset,outperformingbothLSTMandXGBoostbaselines.
Recentworkhasstartedtospecialisetransformerarchitecturesfordifferentsegments
ofthecreditmarket. Korangietal.[68]framedmid-capcorporatedefaultpredictionas
amulti-labelpanelclassificationtask,usingatransformertolearnthetermstructureof
defaultprobabilitiesoverhorizonsfromafewmonthstothreeyears. Theirmulti-channel
designingestsaccounting,pricing,andmarketvariablesandappliesatask-specificlossfor
multi-horizondefaultprediction,yieldingsizeableAUCimprovementsovertraditional
statisticalandLSTM-basedbenchmarks. Lietal.[69]proposedHFTCRNet,ahierarchical
fusiontransformerforinterbankcreditratingandsystemicriskassessment. Themodel
combines a long-term temporal transformer for bank growth trajectories, a short-term
cross-graph transformer for dynamic interbank exposures, and an attentive contagion
module,trainedinasemi-supervisedfashionusingbothcreditratingsandSRISKlabels.
Onadatasetof4548bankswithquarterlybalancesheetsandnetworkdata,HFTCRNet
outperformeddeepandnon-deepbaselinesinratingaccuracywhilealsocapturingsystemic
riskpatternsintheinterbanknetwork.
In the retail and SME space, transformer-based models have been applied to both
tabularandsequentialcreditsignals. Kakadiyaetal.[70]investigatedtransformerarchi-
tectures for bank loan default prediction and reported performance gains over logistic
regressionandtree-basedmethods,arguingthatself-attentioncaptureshigher-orderde-
pendenciesamongfinancialvariablesthataremissedbyconventionalmodels. Zhangand
Liang[71]proposedaminimumweightedvalueerrorcombinationmodelthatintegratesa
BERT-basedtransformerfortemporalfeatureswithDNNandMLPcomponentsforstatic,
non-sequentialattributes. Featuresarefirstselectedusingchi-squaretestsandgradient
boostingdecisiontrees,andthefinalpredictionisobtainedbydynamicallyweightingthe
sequenceandnon-sequenceexpertsaccordingtoanimprovedminimumweightederror
criterion. Experimentsonpersonalcreditdatashowedthatthecombinedmodelachieves
higherclassificationaccuracythananyindividualtransformerorfeed-forwardbaseline.
Addressing class imbalance and transparency, Hartomo et al. [72] introduced a
weighted-lossTabTransformerwithintegratedexplainableAIforMSMEandconsumer
creditdatasets. Usingcost-sensitiveweighting,theirmodelimprovedaccuracyontheBI-
SAIDandGermanCreditdatasetsfrom86.35%to89.27%andfrom93%to95%,respectively,
whilealsoboostingminority-classAUCandprecision–recall. SHAP-basedexplanations
highlightedeconomicallymeaningfuldriverssuchasfinancingneedsandcreditamount,
illustrating how attention-based tabular models can be combined with explainable AI
(XAI)tosupportmoreaccountabledecision-making. Wu[73]developedaBiLSTM-fused
transformerforenterprisefinancialriskidentificationwithinablockchain-basedfinancial
sharingplatform. Themodeljointlyprocessestextualandvisualfinancialinformationto
classifyfirmsintofiverisklevelsand,inexperiments,achievedriskidentificationaccuracy
above94%withAUCexceeding0.95,outperformingbaselineRNNswhileoperatingon
securelysharedfinancialrecords.
https://doi.org/10.3390/info17040395

Information2026,17,395 16of28
Textualtransformershavealsogainedprominencewhereloanassessments, credit
memos,andSMEnarrativesremainhuman-authored. Stevensonetal.[74]showedthat
BERT-derivedembeddingsfromlender-writtendocumentsproducedcompetitivedefault
prediction results without structured data. Lu et al. [75] extended BERT embeddings
into a hybrid architecture with residual blocks to fuse textual and numeric signals for
corporatecredit. Thistrendalignswithregulatoryinterestinleveragingunstructuredand
semi-structureddisclosuresratherthanpurelytabularindicators.
A frontier research area involves transformer robustness, adversarial safety, and
regulatoryalignment. SchwabandKriebel[76]demonstratedthattransformerencoders
canbesensitivetoadversarialperturbationsandproposedgradient-basedregularisation
defenses. Giventhatfinancialsystemsarehighlysensitivetostabilityandfairness,future
deploymentsoftransformersmustincorporatecalibrationdiagnostics,imbalance-aware
lossfunctions,explainabilitytooling,andcontext-awareadversarialsafeguards.
Therecentcontributionsindicatethattransformersaremovingfromexperimental
architecturestopracticalcandidatesforlarge-scale,multimodal,andsystem-levelcreditrisk
models. Theirmainadvantageliesnotonlyinpredictiveliftbutalsointheirabilitytounify
behaviouralsequences,categoricalembeddings,textualnarratives,interbanknetworks,
andgraph-structuredrelationshipswithinasinglemodellinginterface,whileincreasingly
accommodatingclassimbalance,interpretability,andsystemicriskconsiderations.
The emerging evidence suggests that transformers are most promising in settings
where credit risk depends on high-dimensional, heterogeneous, or multimodal signals
thatinteractinnon-localways. Self-attentionisparticularlyeffectivewhenmodellingthe
jointinfluenceoflongrepaymenthistories,bureauortransactionaltext,andrichcategor-
icalattributes,anditenablesasinglearchitecturetooperateacrossthesemodalities. At
thesametime,transformerstypicallyrequirelargertrainingdatasets,moreparameters,
andlongertrainingtimesthanconventionalmodels,andthenumberoftrulylarge-scale,
production-gradecreditstudiesisstillsmall. Inpractice,theyshouldbeviewedascandi-
datesforportfolioswithabundantdataandcomplexinteractions,ratherthanasdrop-in
replacementsfortreeensemblesorrecurrentnetworksonsmalltabulardatasets.
5.4. GraphNeuralNetworksforRelationalCreditRisk
Graphneuralnetworks(GNNs)havegainedsignificanttractionforcreditriskpredic-
tionduetotheirabilitytoencoderelationaldependenciesthatconventionaltabularand
sequentialmodelsignore. Borrowersinteractwithinrichfinancialecosystemsinvolving
co-application, ownership links, shared directorship, supplier–customer contracts, and
transactionflows,makingrelationallearninganaturalextensiontodeepcreditscoring.
Unlikefeed-forwardorrecurrentarchitecturesthatassumeindependentrecords,GNNs
performiterativemessagepassing, enablingrepresentationlearningthatcapturesboth
directandindirectriskpropagationacrossfinancialnetworks.
Wangetal.[77]constructsmallandmediumenterprise(SME)relationalgraphsusing
shareddirectorandbusiness-interactioninformationandapplyarelationalgraphattention
network(RGAT)fordefaultprediction. Theirinductivetestingprotocolshowsthatgraph
baselinessuchasgraphconvolutionalnetwork(GCN),graphattentionnetwork(GAT),and
relationalGCN(RGCN)outperformnon-graphmodels,withRGATachievingAUC=0.797
andKS=0.457,whileamulti-headextensionreachesAUC=0.799andKS=0.528. The
resultsdemonstratethatrelationalsignalsremainpredictiveevenwithouttransactional
features. Similarly, Song et al. [78] proposed the multi-structure cascaded GNN (MS-
CGNN),integratingpairwisegraphswithheterogeneoushypergraphstructurestomodel
higher-orderinteractions. ThemethodachievedRecall=0.8863,Accuracy=0.9442,and
https://doi.org/10.3390/info17040395

Information2026,17,395 17of28
F1-score=0.9300,outperformingseveralGNNbaselinesandconfirmingthatmulti-level
topologystrengthensriskrepresentation.
Temporalandbehaviouraldynamicshavealsobeenincorporatedintographmod-
elling. Yuanetal.[79]introduceDGNN-SR,whichfusesstaticfund-transfergraphswith
dynamicuser–merchantpaymentgraphsusingmulti-viewtimeencoders. Experimentson
Tencentdatasetscontainingmorethan2.8Mnodesand200MedgesshowAUCimprove-
ments between 0.85% and 2.5% over the best continuous-time GNN baselines. From a
supply-chainfinancingperspective,Mojdehietal.[80]combinetopologicaldataanalysis
withGNNs(BM–GNN),attainingmaximumaccuracyof93.56%acrossmultiplescenarios
whileconsistentlyoutperformingclassicalMLmodelsinstabilityandrobustness,despite
similarpoint-estimateaccuracyonsomesubsets.
Recentworkhasemphasisedhigher-ordergraphstructures, regulatoryalignment,
and training stability. Wang et al. [81] proposed a motif-preserving GNN with curricu-
lumlearningtocapturesubgraphpatternsfrequentlyobservedinenterprisenetworks,
demonstratingimprovedperformanceacrossonepublicandtwoindustrialdatasets. The
curriculumdesignhelpedmitigateconvergenceinstabilityarisingfromnoisyrelational
substructures.Inanotherdirection,Liuetal.[82]constructedenterprisecreditgraphsusing
amaximumspanningtreederivedfrom29financialindicatorsandappliedGraphSAGE
tomulti-levelcreditgrading. TheirresultsconfirmedhigherROCvaluesthantree-based
and neural baselines, despite using a sparse graph, highlighting the value of relational
inductivebiaseveninlimited-connectivitysettings.
Scalabilityhasbecomeacoreevaluationcriterionforreal-worlddeployment. Zhang
et al. [83] developed a large-scale industrial GNN pipeline comprising 23.4M nodes
for supply-chain mining and 8.6M nodes for default prediction. Their model achieved
AUC=0.995 on supply-chain tie mining and 0.701 on loan-default prediction, outper-
formingstaticgraph-learningcompetitorsanddemonstratingthatGNNscanoperateat
web-scalefornationalcreditinfrastructure. Furthermore,ChengandLuo[84]proposea
metapath-drivenriskcontagionGNN(RCGNN)usingheterogeneouspaths(investment,
geography, and industry), reporting superior performance to homogeneous GNNs for
enterprisecreditclassification,althoughdetailedmetricswerenotpublished.
Overall,GNN-basedcreditmodelsaremostcompellingwhenrelationalstructureis
intrinsictotheriskproblem,suchasSMEsupplychains,interbankexposures,enterprise
ownershipnetworks,orfund-transfergraphs. Intheseenvironments,messagepassing
capturescontagionandcorrelatedriskthattabularorsequentialmodelsarestructurally
unable to represent, and the empirical studies show consistent gains in discrimination
and stability under sparse or noisy features. The trade-off is engineering complexity:
constructing,maintaining,andgoverninglarge-scalefinancialgraphsisnon-trivial,and
themarginalbenefitofGNNsislimitedwhenrelationalinformationisweakorunavailable.
Consequently, GNNs are best viewed as targeted tools for systemically interconnected
portfoliosratherthanasuniversalreplacementsforborrower-levelscorecards.
Table4consolidatesthepeer-revieweddeeplearningapplicationsdiscussedinthis
section, grouped by model family for readability and direct linkage to the preceding
subsections. Reportedmetricsandvaluesarereproducedasstatedinthesourcestudies
andarenotstandardisedacrossdatasets,targets,horizons,orlabeldefinitions,whichlimits
directcross-papercomparability.
https://doi.org/10.3390/info17040395

Information2026,17,395
18of28
Table4.Summaryofdeeplearningapplicationsincreditriskprediction.
| ModellingFocus | Reference | Year MethodsandApplication |
| -------------- | --------- | -------------------------- |
NODEdifferentiabletreeensembles;matchgradient
TabularDLModels Popovetal.[54] 2019 boostingoncredit-styletabulartaskswhileremaining
fullydifferentiable.
PenalisedDNNsurvivalmodelforP2Ptime-to-default;
Linetal.[49] 2022 embeddedpenaltiessupportfeatureselectionandimprove
PDestimation.
HDNNwithL1–L2regularisationforcorporatecredit;
|     | Yangetal.[48] | 2023 |
| --- | ------------- | ---- |
Acc=80.12%andoutperformsLR,SVM,andbaselineDNN.
MLP,XGBoost,andTabNetforprofitscoring;XGBoostbest
|     | Asenciosetal.[50] | 2023 |
| --- | ----------------- | ---- |
R2 =0.7906,TabNetslightlylowerbutmoreinterpretable.
Hjelkremand MLPonopen-bankingtransactionswithSHAP;outperforms
2023
Lange[52] aBERTmodelandyieldsintuitivebehaviouralriskdrivers.
IncrementalDNNforagriculturalmicroloansunderconcept
|     | Lietal.[53] | 2023 |
| --- | ----------- | ---- |
drift;1.4–7.8ppAUCgainsoverDNN,XGBoost,andRF.
Wangand TabNet–stackingensembleonlarge-scalecredit;Acc=0.979,
2024
|     | Zhang[51] | AUC=0.941onTianchi. |
| --- | --------- | ------------------- |
StackedTabNetwithmulti-stageoptimisationforSME
ShanandGao[55] 2025 supply-chainrisk;AUC=0.9616,Acc=0.9277,above
TabNet,LightGBM,andCatBoost.
LSTMforLendingClubmonthlydefault-rateforecasts;MAE
| SequentialModels | LiangandCai[56] | 2020 |
| ---------------- | --------------- | ---- |
0.072andRMSE0.093,betterthanARIMA,SVM,andANN.
Self-attentionend-to-endcorporaterating;removesmanual
|     | ChenandLong[61] | 2020 |
| --- | --------------- | ---- |
aggregationandstabilisesratingsvsclassicalML.
BehaviouralLSTMvariantsforcreditcards;exceedSVM,RF,
|     | Ala’rajetal.[57] | 2022 |
| --- | ---------------- | ---- |
MLP,andLRinPDpredictionandcalibration.
CNN–LSTM–attentionforenterprisecredit;AUC=0.92and
|     | Zhang[58] | 2022 |
| --- | --------- | ---- |
F1=0.91,outperformingCNN-onlyandLSTM-onlymodels.
CNN–LSTMforlistedcorporates;CNNcapturesshort-term
|     | Lietal.[59] | 2023 motifs,LSTMlong-termbehaviour,improving |
| --- | ----------- | -------------------------------------------- |
discrimination.
Deepdiscrete-timesurvivalwithage–period–cohort
Wangetal.[60] 2024 decomposition;yieldssmoothcredithazardcurvesand
macro/maturitystructure.
Self-attentionpluscross-networkfordefaultprediction;
Hanetal.[62] 2024 improvesaccuracy,precision,recall,andF1over
baselineDL.
BenchmarkofCNN,RNN,andDNNforfinancialcredit
|     | Shietal.[63] | 2025 scoring;RNNbesttemporalsensitivity,CNNmost |
| --- | ------------ | ----------------------------------------------- |
parameter-efficient.
Residual-enhancedBiLSTMwithmulti-headattentionon
Yangetal.[64] 2025 FreddieMacdata;AUC=0.982,F1=0.958,beatingBiLSTM,
GRU,CNN,andRNN.
LSTMencoderswithBayesiancalibrationforcorporaterisk;
|     | Zhang[65] | 2025 Acc=0.972,AUC=0.981andreduceduncertainty |
| --- | --------- | --------------------------------------------- |
miscalibrationvsRFandLR.
TabTransformerwithcontextualembeddingsfor
Transformer-Based
Huangetal.[47] 2020 high-cardinalitycategoricalfeatures;improvesoverMLP
Models
andtreebaselines.
FT-Transformerfortabulardata;attentionblocksmatchor
|     | Gorishniyetal.[66] | 2021 |
| --- | ------------------ | ---- |
surpassCatBoost/XGBoostonnonlinearfinancialtasks.
BERTembeddingsfromSMEloantexts;textalonegives
|     | Stevensonetal.[74] | 2021 |
| --- | ------------------ | ---- |
competitivedefaultpredictionwithoutstructuredvariables.
https://doi.org/10.3390/info17040395

Information2026,17,395 19of28
Table4.Cont.
ModellingFocus Reference Year MethodsandApplication
Feature-embeddedtransformerfusingbehavioural
Transformer-Based
WangandXiao[67] 2022 sequencesandstaticfeaturesforonlinelending;AUC=0.72,
Models
KS=0.32,betterthanLR,XGBoost,andLSTM.
Transformerformid-capcorporatemulti-horizondefault;
Korangietal.[68] 2023 multi-channelpaneldesignyieldshigherAUCthan
statisticalandLSTMbaselines.
HFTCRNethierarchicalfusiontransformerforinterbank
ratingsandsystemicrisk;temporal+graphtransformers
Lietal.[69] 2024
andcontagionmoduleoutperformothermodelson
4548banks.
Transformermodelsforbankloandefault;self-attention
Kakadiyaetal.[70] 2024 captureshigher-orderinteractionsandbeatsLRand
treeensembles.
BiLSTM-Transformeronablockchainfinancialsharing
Wu[73] 2024 platform;multimodaltext/visualenterpriserisk
identificationwithAcc>94%andAUC>0.95.
Weighted-lossTabTransformerwithSHAP-basedXAIfor
Hartomoetal.[72] 2025 imbalancedMSMEandconsumercredit;increasesaccuracy
andminority-classAUC/PR(e.g.,86.35%→89.27%).
MinimumweightedvalueerrorcombinationofBERT-based
Zhangand temporalencoderandDNN/MLPexperts;dynamic
2025
Liang[71] weightingimprovespersonalcreditclassificationvssingle
models.
BERTplusresidualblockstofusetextualandnumeric
Luetal.[75] 2025 signalsforcorporatecredit;improvesclassificationvs.
single-modalityandnon-residualbaselines.
Analysisoftransformerrobustnessinfinancialtasks;shows
Schwaband
2025 adversarialsensitivityandproposes
Kriebel[76]
gradient-regulariseddefences.
Motif-preservingGNNwithcurriculumlearningfor
GNN-basedModels Wangetal.[81] 2023 enterprisenetworks;improvesaccuracyandconvergence
stabilityacrosspublicandindustrialdatasets.
RGATonSMEgraphsfromshareddirectorsand
Wangetal.[77] 2024 interactions;multi-headRGATachievesAUC=0.799and
KS=0.528,abovenon-graphbaselines.
MS-CGNNcombiningpairwisegraphsandhypergraphs;
Songetal.[78] 2024 Recall=0.8863,Acc=0.9442,F1=0.93,outperforming
severalGNNvariants.
GraphSAGEonmaximum-spanning-treeenterprisecredit
Liuetal.[82] 2024 graphs;higherROCthantreeandneuralbaselinesdespite
sparseconnectivity.
DGNN-SRfusingstaticfund-transferanddynamicpayment
Yuanetal.[79] 2025 graphswithmulti-viewtimeencoders;gains0.85–2.5pp
AUCovercontinuous-timeGNNs.
BM–GNNusingtopologicaldataanalysisandGNNsfor
Mojdehietal.[80] 2025 supply-chainfinance;maxAcc=93.56%withrobust
performancevsclassicalML.
Large-scaleindustrialGNNpipeline(23.4Mand8.6M
Zhangetal.[83] 2025 nodes)forsupply-chainmininganddefault;AUC=0.995
(links)and0.701(default).
Metapath-drivenRCGNNusingheterogeneouspaths
ChengandLuo[84] 2025 (investment,geography,industry);improvesmulti-class
enterprisecreditclassificationvs. homogeneousGNNs.
https://doi.org/10.3390/info17040395

Information2026,17,395 20of28
6. Challenges,Limitations,andFutureResearchDirections
Deeplearningcanimproveriskdiscrimination, butdeployingsuchmodelsinreg-
ulatedcreditenvironmentsintroducesconstraintsthatgobeyondaccuracy. Thissection
summarisesthemainchallengesandthendistilsresearchdirectionsaimedattrustworthy,
regulation-readycreditriskmodelling.
6.1. ChallengesandLimitations
6.1.1. EvaluationIntegrity
Creditriskevolvesovertimeinresponsetobehavioural,policy,andmacroeconomic
shifts,makingrandomk-foldcross-validationpronetotemporalleakage. Whenobserva-
tionsfromlaterperiodsappearinbothtrainingandtestfolds,performanceestimatescan
implicitlyrelyonfutureinformationthatwouldnotbeavailableatdecisiontime. Time-
orderedevaluationschemes,includingout-of-timesplitsandrolling-originvalidationin
whichthetrainingwindowstrictlyprecedestheevaluationwindow,provideamorefaith-
fulestimateofdeploymentperformanceunderregimechangeandstressconditions[85].
However, a non-trivial portion of deep credit risk studies still relies on random splits,
weakeningexternalvalidityandcomplicatingcomparisonsacrossmodelfamilies.
A second source of fragility is over-reliance on threshold-agnostic summary met-
rics such as AUC, which aggregate performance across all score cut-offs and can mask
behaviourintheoperatingregionwherelendingdecisionsareactuallymade. Inhighlyim-
balancedportfolios,complementarymeasuressuchastheareaundertheprecision–recall
curve(AUPRC)andcost-sensitivemetricsbetterreflectminority-classperformanceand
theeconomicconsequencesofmisclassification[33]. Equallyimportant,probabilitycal-
ibration is rarely assessed, despite being central to decisioning and risk quantification:
poorlycalibratedscorescanleadtounstableapprovalrates,mis-pricedcredit,andbiased
downstreamestimatesofportfoliorisk,evenwhenrankingperformance(AUC)improves.
Calibration-sensitivereportingusingtheBrierscoreandexpectedcalibrationerror,together
withreliabilitydiagrams,providesdirectevidenceofwhetherpredictedprobabilitiesmatch
observeddefaultfrequencies[86]. Whenmiscalibrationisdetected,posthocmethodssuch
asPlattscaling,isotonicregression,andtemperaturescalingcanimprovealignmentbe-
tweenpredictedandempiricaldefaultrates[87],butthesestepsareseldomdocumentedin
deepcreditriskpapers.
Finally, decision-facing evaluation should make explicit how metrics map to lend-
ingoutcomes. ForPD-stylemodels,thisincludesreportingperformanceatoperationally
relevantthresholdsand,whereinputsareavailable,quantifyingutilityusingsimplecost
proxies(false-approvallossversusfalse-rejectionopportunitycost)orbypropagatingcali-
bratedPDintodownstreamlossconstructs(e.g.,EL-styleestimates),whileacknowledging
thatELisnotcomparableacrossheterogeneousdatasetsandrecoverydefinitions. These
considerationsjointlyformadefactoevaluationchecklistfordeployment-alignedcredit
riskmodelling.
6.1.2. ImbalancedLearningandRejectInference
Defaultdatasetsareheavilyimbalanced,andnaïveresamplingcandistorttemporal
andbehaviouralstructure. Over-samplingtechniquessuchasSMOTEareoftenapplied
indiscriminatelywithouttemporalsafeguards,whilecost-sensitivelearningbetterreflects
economicriskbutisinfrequentlyemployed[88,89]. Afurthercomplicationisrejectinfer-
ence: declinedapplicantslackobservedoutcomes,leadingtostructurallybiasedtraining
dataandunreliablegeneralisation[28,90,91]. Observedoutcomesareconditionalonaccep-
tancepolicies,leadingtosample-selectionbiasthatinflatesapparentmodelperformance
https://doi.org/10.3390/info17040395

Information2026,17,395 21of28
when applied to rejected populations. Existing proxy-based inference methods remain
heuristicandarenotalignedwithregulatorytransparencyexpectations.
6.1.3. InterpretabilityandFairness
Although deep models improve predictive power, their opacity conflicts with reg-
ulatory explainability requirements. Post hoc explanation tools, including SHAP and
integratedgradients,maynotprovidestable,counterfactual-faithfulexplanations[92]. In
practice,theappropriateexplanationtooldependsonthemodelfamilyandthedecision
artefactbeingjustified: forMLP-styletabularnetworks,featureattributionmethodsand
monotonicorsparseconstraintscansupportreasonedfactornarratives;fortree-likebase-
lines and tree–neural hybrids, TreeSHAP-style decompositions often provide the most
auditablefeature-levelbreakdown;fortransformer-basedcreditmodels,attributionover
token/feature embeddings (with attention used as a supportive diagnostic rather than
a standalone explanation) is typically more reliable than raw attention maps; and for
GNN-basedcreditmodels,subgraph-ormessage-passingexplanationscanlocalisewhich
relationsdriveariskscore.
FairnessisalsoinconsistentlyoperationalisedintheDLcredit-riskliterature. Metrics
suchasequalisedodds[93]arerarelyintegratedintotrainingobjectives,despiteevidence
thatautomatedlendingcanamplifyexistingsocio-economicinequalities. Fairnesstargets
arecontextdependent: demographicparitymaybeinappropriatewhenbaseratesdiffer
for legitimate reasons, whereas error-rate constraints such as equalised odds may be
moresuitablewhentheaimistocontroldifferentialmisclassificationharms. Accordingly,
the selected fairness definition should be justified relative to the lending decision, the
attributes available for monitoring, and the governing legal regime, and it should be
assessedalongsidemodelcalibrationandoperating-thresholdbehaviour. Counterfactual
explanationapproachesremainpromising,butdeploymentatscaleisoftenhinderedby
feasibilityconstraintsandbytheneedtoensureplausibilityunderrealcreditpolicyand
data-generatingprocesses[94].
Amongthesurveyeddeeplearningstudies,onlyasmallsubsetexplicitlyincorporates
posthocexplainabilitytoolsorfairnessmetrics,andevenfeweroptimisefairness-aware
objectivesduringtraining,whichshowsthegapbetweenregulatoryaspirationsandcur-
rentpractice.
6.1.4. RobustnessandPrivacy
Deeplearningmodelsaresensitivetoconceptdriftcausedbymacroeconomicshocks,
behaviouralchanges,andportfoliorebalancing,leadingtocalibrationdecayovertime[95].
Existingstudiesseldomincorporatedrift-awareretrainingorautomatedchangedetection.
Fordeployment-alignedrobustness,studiesshoulddistinguish(i)temporaldrift(vintage
andmacroshifts),(ii)populationdrift(portfoliomixchanges),and(iii)label/definition
drift(policyorcollections-rulechanges),andthenevaluatemitigationusingtime-ordered
backtestsratherthanrandomre-sampling. Operationally,thistranslatestomonitoringboth
discriminationandcalibrationovertime(e.g.,AUC/AUPRCalongsideBrier/ECE),trig-
geringreviewwhencalibrationdeviatesmateriallyevenifrankingmetricsappearstable.
Atthesametime,sharinggranulardataacrossinstitutionsintroducesprivacyand
confidentialityconstraints. Differentiallyprivatetrainingandsyntheticdatageneration
partiallyaddresstheselimitationsbutintroduceaccuracytrade-offs. Wherecollaboration
isrequired,privacy-preservinglearningshouldbeframedasanend-to-enddesignchoice
(e.g., federatedtrainingwithsecureaggregation, differentialprivacywithdocumented
privacy budgets, or controlled synthetic-data release), accompanied by utility and bias
testingtoshowwhatdecisionqualityislostorretainedunderprivacyconstraints.
https://doi.org/10.3390/info17040395

Information2026,17,395 22of28
6.1.5. OperationalDeploymentandGovernance
Operational success requires structured machine learning operations (MLOps)
pipelineswithversioning,lineagetracking,monitoring,andchallenger-championtesting.
Withoutthese, systemsaccumulatetechnicaldebtthatweakenscomplianceandunder-
minesmodellifecyclemanagement[96]. Inregulatedcreditsettings,deploymentdiscipline
istypicallyenforcedthroughamodelriskmanagementworkflowthatmakeseachstageau-
ditable: reproduciblefeaturepipelines,immutabletrainingandevaluationdatasets,signed
modelartefacts,andtraceabledecisionrecordsthatlinkeveryproductionscoretoaspecific
modelversionanddatasnapshot. Acommonrolloutpatternisstagedrelease,inwhich
acandidatemodelfirstpassesofflinebacktesting,thenrunsinshadowscoring(producing
scoreswithoutaffectingapprovals), andonlythenprogressestolimitedexposurewith
pre-definedpromotiongatesbasedoncalibration,drift,andstabilitychecks. Thesegates
reducefailuresthatfrequentlyoccurinpractice,suchassilentcalibrationdecayafterpolicy
orcollections-rulechanges,performancedropsundermacroeconomicregimeshifts,and
inconsistentfeaturecomputationbetweentrainingandserving.
Moreover,existinggovernanceartefacts,includingdatasheetsandmodelcards,are
rarelyintegratedwithregulatoryprocessessuchasBaselIII,SR11-7, ortheEUAIAct,
reducingorganisationalreadinessforexternalaudit. Tomakeinterpretabilityandfairness
operationalratherthanadhoc,explanationandbias-assessmentoutputsshouldbegener-
atedautomaticallypermodelversionwithintheCI/CDworkflowandstoredaspartof
themodelevidencepack. Concretely,thismeanslogging(i)globalandlocalexplanation
artefactsalignedwiththedeployedmodelfamily,(ii)fairnessreportscomputedonthe
productiondecisionpopulation(and,wherefeasible,onapproved-outcomepopulations),
and(iii)monitoringdashboardsthattrackbothdiscriminationandcalibrationovertime.
Whenexceptionsoccur(e.g.,manualoverrides,policy-drivenrulechanges,ortemporary
riskcontrols),thegovernancelayershouldrecordtheoverriderationaleanditsimpact
onobservedoutcomessothatfutureretrainingdoesnotunknowinglyencodeshort-term
interventionsaspredictivesignals.
6.2. FutureResearchDirections
Future research should adopt evaluation frameworks that reflect realistic data-
generating processes, including temporally constrained train-test splits, multi-horizon
performancetracking,andcalibration-awarereporting. Thisincludesbenchmarkingon
large-scale,longitudinaldatasetswithexplicittemporalstructureandeconomicannota-
tions,enablingfaircomparisonacrossmodelfamiliesandreducingover-optimismasso-
ciatedwithsmallpublicdatasets. Moreover,futureworkshouldprioritisecost-aligned
performancereporting,wheremodelutilityisquantifiedintermsofexpectedlossreduc-
tion,capitalefficiency,defaulttiming,andresilienceacrossmacroeconomicstressregimes
(Table5).
Anotherdirectionisthedevelopmentoflearningobjectivesthatintegratefairness,in-
terpretability,andeconomiccostattrainingtimeratherthanrelyingonposthocadjustment.
Interpretable-by-designarchitectures,monotonicneuralnetworks,sparseattentionmecha-
nisms,andhybridsymbolic-neuralmodelscanprovidegreaterregulatorycompatibility
whileretainingfeatureinteractioncapacity. Causalfairness,adversarialdebiasing,and
counterfactualtrainingpipelinesrepresentpromisingframeworksformitigatingdisparate
impactwithoutsuppressingpredictivepower.
https://doi.org/10.3390/info17040395

Information2026,17,395 23of28
Table5.Challengesindeeplearningcreditriskmodellingandalignedresearchdirections.
Challenge Description EmergingResearchDirections
Out-of-timeandrollingvalidation;
Temporalleakageandweakcalibration
EvaluationIntegrity calibration-awarereporting;cost-sensitive
undermineexternalvalidity[18,23,58,87].
andutility-alignedscoring.
Causalestimation,selectiveabstention,
Raredefaultsandmissingcounterfactual
ImbalanceandRejectInference semi-supervisedrejectinference,and
labelsdistortlearningsignals[88–90].
cost-sensitiveobjectives.
Interpretable-by-designarchitectures,
Deepmodelsviolateexplainabilityand
InterpretabilityandFairness causalfairnessconstraints,certified
anti-biascompliance[92,97].
explanationmechanisms.
Drift-robustadaptivetraining,federated
Driftandprivacyconstraintslimit
RobustnessandPrivacy learning,syntheticfinancialdigitaltwins,
long-termreliability[95,98].
DP-SGDoptimisation.
Automatedmonitoringframeworks,
Insufficientdeploymentdiscipline
OperationalDeploymentandGovernance model-cardpipelines,Basel-aligned
increasesregulatoryrisk[96,99].
documentationstandards.
Researchshouldalsofocusondesigningmodelsthatadaptunderuncertaintywhile
maintaining stability guarantees. Drift-aware architectures, online continual learning
mechanisms,uncertainty-calibratedpredictions,andstress-testingundermacroeconomic
scenariosimulationmayimprovelong-termreliability. Privacy-preservingcollaborative
learning,throughfederatedoptimisation,securemultipartycomputation,andhigh-fidelity
syntheticdigitaltwins,wouldenablecross-institutionallearningwhilerespectingconfiden-
tialityandregulation. Thisagendaalsorequiresgovernanceandregulatoryalignmentfor
cross-institutionaldatasharing,includingclearaccountabilityforconsent,accesscontrol,
retention,andauditability. Similarly,syntheticdatashouldbegovernedwithdocumented
generationprotocols,privacy-risktesting,anddownstream-userestrictionstoavoidleakage
andunwarrantedrelianceinregulateddecision-making.
Finally, there is a need for deployment-aligned governance frameworks that stan-
dardise model documentation, monitoring, and auditability. Integrated pipelines that
combineMLOpswithregulatoryartefacts,suchasmodelcardslinkedtovalidationlogs
andchallenger-championperformancetrails,couldaccelerateinstitutionaltrustandre-
ducecompliancecosts. Long-termprogresswillrequiresystemsthatarenotonlymore
accurate,butalsocertifiablyfair,transparent,androbust—makingdeeplearningsuitable
forproduction-gradefinancialriskmanagement.
7. Conclusions
Thissurveyrevieweddeeplearningmethodsforcreditriskpredictionacrosstabu-
lar,sequential,transformer-based,andgraph-structuredsettings. Byorganisingexisting
research through a unified taxonomy that links model families to data structures and
credit-riskobjectives,thesurveyprovidesconceptualclarityonwhenandwhyspecific
architecturesareappropriate. Acrossthepeer-reviewedevidence,deepmodelstendto
outperformtraditionalscorecardandensemblemethodswhentrainedonsufficientlylarge,
temporallyrepresentativedatasetswithrichbehaviouralandrelationalinformation.
However,theliteraturealsorevealsgapsthatconstrainreliablereal-worldadoption.
Reporting standards are inconsistent, with limited use of temporally valid evaluation,
calibrationmetrics,andcost-alignedperformancereporting. Interpretabilityandfairness
areoftentreatedasadd-onsratherthanrequirements,androbustnessunderconceptdrift,
data-sharingconstraints,andoperationalgovernanceremainsweaklyaddressed,shifting
successcriteriatowardpredictiveaccuracyratherthanlifecyclereliabilityandauditability.
https://doi.org/10.3390/info17040395

Information2026,17,395 24of28
Futureworkshouldthereforeprioritisedeployment-alignedresearch: interpretable-
by-designmodelling,temporallyrealisticbenchmarks,fairnessstrategiesgroundedinthe
decision and legal context, privacy-preserving collaborative learning, and governance-
readymonitoringanddocumentationpipelines. Thissurveyislimitedtopeer-reviewed
English-language studies indexed in major databases and does not cover proprietary
implementationsorregulatorygreyliterature;futuresynthesescouldextendtheevidence
base using secure-access supervisory data or meta-analyses where study designs and
outcomesaresufficientlycomparable.
AuthorContributions: Conceptualisation,I.D.M.,E.E.andC.M.; methodology,I.D.M.,E.E.and
C.M.;validation,I.D.M.,E.E.andC.M.;investigation,I.D.M.,E.E.andC.M.;writing—originaldraft
preparation,I.D.M.;writing—reviewandediting,I.D.M.,E.E.andC.M.;visualisation,I.D.M.,E.E.
andC.M.;supervision,E.E.andC.M.Allauthorshavereadandagreedtothepublishedversionof
themanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Nonewdatawerecreatedoranalysedinthisstudy.Datasharingis
notapplicabletothisarticle.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
AI Artificialintelligence
AUC Areaunderthereceiveroperatingcharacteristiccurve
AUPRC Areaundertheprecision–recallcurve
CNNs Convolutionalneuralnetworks
DL Deeplearning
EAD Exposureatdefault
EL Expectedloss
GNNs Graphneuralnetworks
GRU Gatedrecurrentunit
HDNN High-dimensionaldeepneuralnetwork
I-DNN IncrementalDNN
LGD Lossgivendefault
LR Logisticregression
LSTM Longshort-termmemory
ML Machinelearning
MLOps Machinelearningoperations
MLP Multi-layerperceptron
MS-CGNN Multi-structurecascadedGNN
NODE NeuralObliviousDecisionEnsembles
PD Probabilityofdefault
PDNN Penaliseddeepneuralnetwork
RNNs Recurrentneuralnetworks
RWA Risk-weightedasset
SME Smallandmediumenterprise
SVMs Supportvectormachines
TCNs Temporalconvolutionalnetworks
XAI ExplainableAI
https://doi.org/10.3390/info17040395

Information2026,17,395 25of28
References
1. Zhu,Y.;Wu,D. P2PcreditriskmanagementwithKG-GNN:Aknowledgegraphandgraphneuralnetwork-basedapproach.
J.Oper.Res.Soc.2025,76,866–880.[CrossRef]
2. Alagic,A.;Zivic,N.;Kadusic,E.;Hamzic,D.;Hadzajlic,N.;Dizdarevic,M.;Selmanovic,E. Machinelearningforanenhanced
creditriskanalysis:Acomparativestudyofloanapprovalpredictionmodelsintegratingmentalhealthdata. Mach.Learn.Knowl.
Extr.2024,6,53–77.[CrossRef]
3. Karami,A.;Igbokwe,C. Theimpactofbigdatacharacteristicsoncreditriskassessment. Int.J.DataSci.Anal.2025,20,4239–4259.
[CrossRef]
4. Talaat,F.M.;Aljadani,A.;Badawy,M.;Elhosseini,M. Towardinterpretablecreditscoring: Integratingexplainableartificial
intelligencewithdeeplearningforcreditcarddefaultprediction. NeuralComput.Appl.2024,36,4847–4865.[CrossRef]
5. Aruleba,I.;Sun,Y. Effectivecreditriskpredictionusingensembleclassifierswithmodelexplanation. IEEEAccess2024,12,
115015–115025.[CrossRef]
6. Machado,M.R.;Chen,D.T.;Osterrieder,J.R. Ananalyticalapproachtocreditriskassessmentusingmachinelearningmodels.
Decis.Anal.J.2025,16,100605.[CrossRef]
7. Tian,Z.;Xiao,J.;Feng,H.;Wei,Y. Creditriskassessmentbasedongradientboostingdecisiontree. ProcediaComput.Sci.2020,
174,150–160.[CrossRef]
8. Aruleba,I.;Sun,Y. EnhancedcreditriskpredictionusingdeeplearningandSMOTE-ENNresampling. Mach.Learn.Appl.2025,
21,100692.[CrossRef]
9. Sun,P.;Jia,Y.;Shi,Y.;Ren,J.;Li,Z.;Li,X. ArtificialIntelligenceCreditRiskAssessmentModelBasedonMLP-HybridClustering.
Complexity2025,2025,3308222.[CrossRef]
10. Mienye,I.D.;Esenogho,E.;Modisane,C. DeepReinforcementLearningintheEraofFoundationModels:ASurvey. Computers
2026,15,40.[CrossRef]
11. Bhatore,S.;Mohan,L.;Reddy,Y.R. Machinelearningtechniquesforcreditriskevaluation:Asystematicliteraturereview. J.Bank.
Financ.Technol.2020,4,111–138.[CrossRef]
12. Shi,S.;Tse,R.;Luo,W.;D’Addona,S.;Pau,G. Machinelearning-drivencreditrisk:Asystemicreview. NeuralComput.Appl.2022,
34,14327–14339.[CrossRef]
13. Noriega,J.P.;Rivera,L.A.;Herrera,J.A. Machinelearningforcreditriskprediction:Asystematicliteraturereview. Data2023,
8,169.[CrossRef]
14. Montevechi,A.A.;deCarvalhoMiranda,R.;Medeiros,A.L.;Montevechi,J.A.B. AdvancingcreditriskmodellingwithMachine
Learning:Acomprehensivereviewofthestate-of-the-art. Eng.Appl.Artif.Intell.2024,137,109082.[CrossRef]
15. Kim,H.;Cho,H.;Ryu,D. Corporatedefaultpredictionsusingmachinelearning:Literaturereview. Sustainability2020,12,6325.
[CrossRef]
16. Çallı,B.A.;Cos¸kun,E. Alongitudinalsystematicreviewofcreditriskassessmentandcreditdefaultpredictors. SageOpen2021,
11,21582440211061333.[CrossRef]
17. Mhlanga,D. Financialinclusioninemergingeconomies:Theapplicationofmachinelearningandartificialintelligenceincredit
riskassessment. Int.J.Financ.Stud.2021,9,39.[CrossRef]
18. Hayashi,Y. Emergingtrendsindeeplearningforcreditscoring:Areview. Electronics2022,11,3181.[CrossRef]
19. Peng,K.;Yan,G. Asurveyondeeplearningforfinancialriskprediction. Quant.Financ.Econ.2021,5,716–737.[CrossRef]
20. HoyosGutiérrez,S.P.;SantosLópez,F.M. CreditRiskAssessmentSystemBasedonDeepLearning: ASystematicLiterature
Review. InProceedingsoftheInternationalConferenceonComputerScience,ElectronicsandIndustrialEngineering(CSEI);Springer:
Berlin/Heidelberg,Germany,2023;pp.395–413.
21. DemmaWube,H.;ZekariasEsubalew,S.;FayisoWeldesellasie,F.;GirmaDebelee,T. Deeplearningandmachinelearningtech-
niquesforcreditscoring:Areview. InProceedingsofthePanAfricanConferenceonArtificialIntelligence;Springer:Berlin/Heidelberg,
Germany,2024;pp.30–61.
22. Mienye,E.;Jere,N.;Obaido,G.;Mienye,I.D.;Aruleba,K. DeepLearninginFinance:ASurveyofApplicationsandTechniques.
AI2024,5,2066–2091.[CrossRef]
23. Valdrighi, G.; MRibeiro, A.; SBPereira, J.; Guardieiro, V.; Hendricks, A.; MirandaFilho, D.; NietoGarcia, J.D.; FBocca, F.;
BVeronese,T.;Wanner,L.;etal. Bestpracticesforresponsiblemachinelearningincreditscoring. NeuralComput.Appl.2025,37,
20781–20821.[CrossRef]
24. Paz,Á.;Crawford,B.;Monfroy,E.;Barrera-García,J.;PeñaFritz,Á.;Soto,R.;Cisternas-Caneo,F.;Yáñez,A. MachineLearning
andMetaheuristicsApproachforIndividualCreditRiskAssessment:ASystematicLiteratureReview. Biomimetics2025,10,326.
[CrossRef]
25. Alvi,J.;Arif,I.;Nizam,K. Advancingfinancialresilience:Asystematicreviewofdefaultpredictionmodelsandfuturedirections
increditriskmanagement. Heliyon2024,10,e39770.[CrossRef]
https://doi.org/10.3390/info17040395

Information2026,17,395 26of28
26. Bhattacharya, A.; Biswas, S.K.; Mandal, A. Credit risk evaluation: A comprehensive study. Multimed. Tools Appl. 2023,
82,18217–18267.[CrossRef]
27. Gunnarsson,B.R.;VandenBroucke,S.;Baesens,B.;Óskarsdóttir,M.;Lemahieu,W. Deeplearningforcreditscoring:Doordon’t?
Eur.J.Oper.Res.2021,295,292–305.[CrossRef]
28. Thomas,L.;Crook,J.;Edelman,D. CreditScoringandItsApplications;SIAM:Philadelphia,PA,USA,2017.
29. Bandyopadhyay,A. Loanlevellossgivendefault(LGD)studyofIndianbanks. IIMBManag.Rev.2022,34,168–177.[CrossRef]
30. Wattanawongwan,S.;Mues,C.;Okhrati,R.;Choudhry,T.;So,M.C. Modellingcreditcardexposureatdefaultusingvinecopula
quantileregression. Eur.J.Oper.Res.2023,311,387–399.[CrossRef]
31. Hofmann,H.Statlog(GermanCreditData). UCIMachineLearningRepository.1994.Availableonline:https://archive.ics.uci.
edu/dataset/144/statlog+german+credit+data(accessedon1October2025).
32. Yeh,I.C.;Lien,C.H. Thecomparisonsofdataminingtechniquesforthepredictiveaccuracyofprobabilityofdefaultofcredit
cardclients. ExpertSyst.Appl.2009,36,2473–2480.[CrossRef]
33. Lessmann,S.;Baesens,B.;Seow,H.V.;Thomas,L.C. Benchmarkingstate-of-the-artclassificationalgorithmsforcreditscoring:An
updateofresearch. Eur.J.Oper.Res.2015,247,124–136.[CrossRef]
34. Montoya,A.;Inversion;KirillOdintsov;Kotek,M. HomeCreditDefaultRisk.Kaggle.2018. Availableonline:https://kaggle.
com/competitions/home-credit-default-risk(accessedon5December2025).
35. Malekipirbazari,M.;Aksakalli,V. Riskassessmentinsociallendingviarandomforests. ExpertSyst.Appl.2015,42,4621–4631.
[CrossRef]
36. Nwafor,C.N.;Nwafor,O.;Brahma,S. Enhancingtransparencyandfairnessinautomatedcreditdecisions:Anexplainablenovel
hybridmachinelearningapproach. Sci.Rep.2024,14,25174.[CrossRef]
37. deOliveira,N.A.;Basso,L.F.C. AdvancingCreditRatingPrediction:TheRoleofMachineLearninginCorporateCreditRating
Assessment. Risks2025,13,116.[CrossRef]
38. LeCun,Y.;Bengio,Y.;Hinton,G. Deeplearning. Nature2015,521,436–444.[CrossRef]
39. Mienye, I.D.; Swart, T.G.; Obaido, G. Recurrent neural networks: A comprehensive review of architectures, variants, and
applications. Information2024,15,517.[CrossRef]
40. Mienye,I.D.;Esenogho,E.;Modisane,C. DetectingImbalancedCreditCardFraudviaHybridGraphAttentionandVariational
AutoencoderEnsembles. AppliedMath2025,5,131.[CrossRef]
41. Bai,S.;Kolter,J.Z.;Koltun,V. Anempiricalevaluationofgenericconvolutionalandrecurrentnetworksforsequencemodeling.
arXiv2018,arXiv:1803.01271.[CrossRef]
42. Liu,M.;Xia,C.;Xia,Y.;Deng,S.;Wang,Y. TDCN:Anoveltemporaldepthwiseconvolutionalnetworkforshort-termload
forecasting. Int.J.Electr.PowerEnergySyst.2025,165,110512.[CrossRef]
43. Dong,A.;Starr,A.;Zhao,Y. AninterpretabletemporalconvolutionalframeworkforGrangercausalityanalysis. IEEE/CAAJ.
Autom.Sin.2025,13,1–15.[CrossRef]
44. Vashishth,T.K.;Sharma,V.;Sharma,K.K.;Ahamad,S.;Kaushik,V. FinancialForecastingwithConvolutionalNeuralNetworks
(CNNs):TrendsandChallenges. InShapingCutting-EdgeTechnologiesandApplicationsforDigitalBankingandFinancialServices;
Taylor&Francis:Abingdon,UK,2025;pp.62–81.
45. Mienye,I.D.;Swart,T.G. Acomprehensivereviewofdeeplearning:Architectures,recentadvances,andapplications. Information
2024,15,755.[CrossRef]
46. Vaswani,A.;Shazeer,N.;Parmar,N.;Uszkoreit,J.;Jones,L.;Gomez,A.N.;Kaiser,Ł.;Polosukhin,I. Attentionisallyouneed.
Adv.NeuralInf.Process.Syst.2017,30,6000–6010.
47. Huang,X.;Khetan,A.;Cvitkovic,M.;Karnin,Z. Tabtransformer:Tabulardatamodelingusingcontextualembeddings. arXiv
2020,arXiv:2012.06678.[CrossRef]
48. Yang,M.;Lim,M.K.;Qu,Y.;Li,X.;Ni,D. DeepneuralnetworkswithL1andL2regularizationforhighdimensionalcorporate
creditriskprediction. ExpertSyst.Appl.2023,213,118873.[CrossRef]
49. Lin,C.;Qiao,N.;Zhang,W.;Li,Y.;Ma,S. Defaultriskpredictionandfeatureextractionusingapenalizeddeepneuralnetwork.
Stat.Comput.2022,32,76.[CrossRef]
50. Asencios,R.;Asencios,C.;Ramos,E. Profitscoringforcreditunionsusingthemultilayerperceptron,XGBoostandTabNet
algorithms:EvidencefromPeru. ExpertSyst.Appl.2023,213,119201.[CrossRef]
51. Wang,S.;Zhang,X. ResearchoncreditdefaultpredictionmodelbasedonTabNet-stacking. Entropy2024,26,861.[CrossRef]
52. Hjelkrem,L.O.;Lange,P.E.d. ExplainingdeeplearningmodelsforcreditscoringwithSHAP:AcasestudyusingOpenBanking
Data. J.RiskFinanc.Manag.2023,16,221.[CrossRef]
53. Li,G.;Zhu,F.;Zhang,Y.;Li,M. AData-DrivenIncrementalDeepNeuralNetworkforBorrowerCreditScoring. SSRN2023.
[CrossRef]
54. Popov, S.; Morozov, S.; Babenko, A. Neural oblivious decision ensembles for deep learning on tabular data. arXiv 2019,
arXiv:1909.06312.[CrossRef]
https://doi.org/10.3390/info17040395

Information2026,17,395 27of28
55. Shan,W.;Gao,B. StackedEnsembleModelwithEnhancedTabNetforSMESupplyChainFinancialRiskPrediction. Systems2025,
13,892.[CrossRef]
56. Liang,L.;Cai,X. Forecastingpeer-to-peerplatformdefaultratewithLSTMneuralnetwork. Electron.Commer.Res.Appl.2020,
43,100997.[CrossRef]
57. Ala’raj,M.;Abbod,M.F.;Majdalawieh,M.;Jum’a,L. Adeeplearningmodelforbehaviouralcreditscoringinbanks. Neural
Comput.Appl.2022,34,5839–5866.[CrossRef]
58. Zhang,L. TheEvaluationontheCreditRiskofEnterpriseswiththeCNN-LSTM-ATTModel. Comput. Intell. Neurosci. 2022,
2022,6826573.[CrossRef][PubMed]
59. Li,J.;Xu,C.;Feng,B.;Zhao,H. CreditriskpredictionmodelforlistedcompaniesbasedonCNN-LSTMandattentionmechanism.
Electronics2023,12,1643.[CrossRef]
60. Wang,H.;Bellotti,A.;Qu,R.;Bai,R. Discrete-TimeSurvivalModelswithNeuralNetworksforAge–Period–CohortAnalysisof
CreditRisk. Risks2024,12,31.
61. Chen,B.;Long,S. Anovelend-to-endcorporatecreditratingmodelbasedonself-attentionmechanism. IEEEAccess2020,
8,203876–203889.[CrossRef]
62. Han,D.;Guo,W.;Chen,Y.;Wang,B.;Li,W. Personalcreditdefaultpredictionfusionframeworkbasedonself-attentionand
cross-networkalgorithms. Eng.Appl.Artif.Intell.2024,133,107977.[CrossRef]
63. Shi,X.;Tang,D.;Yu,Y. CreditScoringPredictionUsingDeepLearningModelsintheFinancialSector. IEEEAccess2025,13,
130731–130746.[CrossRef]
64. Yang,Y.;Lin,Y.;Zhang,Y.;Su,Z.;Goh,C.C.;Fang,T.;Bellotti,A.G.;Lee,B.G. TransformingCreditRiskAnalysis:ATime-Series-
DrivenResE-BiLSTMFrameworkforPost-LoanDefaultDetection. arXiv2025,arXiv:2508.00415.[CrossRef]
65. Zhang, Y. AI-Driven Framework for Financial Risk Management: Enhancing Decision-Making with LSTM Networks and
ProbabilisticModels. InProceedingsofthe20252ndInternationalConferenceonIntelligentComputingandRobotics(ICICR);IEEE:
Piscataway,NJ,USA,2025;pp.176–181.
66. Gorishniy,Y.;Rubachev,I.;Khrulkov,V.;Babenko,A. Revisitingdeeplearningmodelsfortabulardata. Adv.NeuralInf.Process.
Syst.2021,34,18932–18943.
67. Wang,C.;Xiao,Z. Adeeplearningapproachforcreditscoringusingfeatureembeddedtransformer. Appl.Sci.2022,12,10995.
[CrossRef]
68. Korangi,K.;Mues,C.;Bravo,C. Atransformer-basedmodelfordefaultpredictioninmid-capcorporatemarkets. Eur.J.Oper.
Res.2023,308,306–320.[CrossRef]
69. Li,J.;Zhou,Z.;Zhang,J.;Cheng,D.;Jiang,C. HFTCRNet:Hierarchicalfusiontransformerforinterbankcreditratingandrisk
assessment. IEEETrans.NeuralNetw.Learn.Syst.2024,36,13006–13020.[CrossRef]
70. Kakadiya,R.;Khan,T.;Diwan,A.;Mahadeva,R. TransformerModelsforPredictingBankLoanDefaultsaNext-GenerationRisk
Management. InProceedingsofthe2024IEEE6thInternationalConferenceonCybernetics,CognitionandMachineLearningApplications
(ICCCMLA);IEEE:Piscataway,NJ,USA,2024;pp.26–31.
71. Zhang,Y.;Liang,X. PersonalCreditRiskPredictionBasedonMinimumWeightValueErrorCombinationModel. InProceedings
ofthe20258thInternationalConferenceonAdvancedAlgorithmsandControlEngineering(ICAACE);IEEE:Piscataway,NJ,USA,2025;
pp.307–313.
72. Hartomo,K.D.;Arthur,C.;Nataliani,Y. Anovelweightedlosstabtransformerintegratingexplainableaiforimbalancedcredit
riskdatasets. IEEEAccess2025,13,31045–31056.[CrossRef]
73. Wu,Y. Enterprisefinancialsharingandriskidentificationmodelcombiningrecurrentneuralnetworkswithtransformermodel
supportedbyblockchain. Heliyon2024,10,e32639.[CrossRef]
74. Stevenson,M.;Mues,C.;Bravo,C. Thevalueoftextforsmallbusinessdefaultprediction:Adeeplearningapproach. Eur.J.Oper.
Res.2021,295,758–771.[CrossRef]
75. Lu,S.;Zhang,X.;Su,Y.;Liu,X.;Yu,L. Efficientmultimodallearningforcorporatecreditriskpredictionwithanextendeddeep
beliefnetwork. InAnnalsofOperationsResearch;Springer:Berlin/Heidelberg,Germany, 2025;pp.1–38.
76. Schwab,B.;Kriebel,J. Mitigatingadversarialattacksontransformermodelsincreditscoring. Eur.J.Oper.Res.2025,328,309–323.
[CrossRef]
77. Wang,J.;Liu,G.;Xu,X.;Xing,X. Creditriskpredictionforsmallandmediumenterprisesutilizingadjacententerprisedataanda
relationalgraphattentionnetwork. J.Manag.Sci.Eng.2024,9,177–192.[CrossRef]
78. Song, L.; Li, H.; Tan, Y.; Li, Z.; Shang, X. Enhancing enterprise credit risk assessment with cascaded multi-level graph
representationlearning. NeuralNetw.2024,169,475–484.[CrossRef][PubMed]
79. Yuan,Q.;Liu,Y.;Tang,Y.;Chen,X.;Zheng,X.;He,Q.;Ao,X. DynamicGraphLearningwithStaticRelationsforCreditRisk
Assessment. InProceedingsoftheAAAIConferenceonArtificialIntelligence,Philadelphia,PA,USA,25February–4March2025;
Volume39,pp.13133–13141.
https://doi.org/10.3390/info17040395

Information2026,17,395 28of28
80. Mojdehi,K.F.;Amiri,B.;Haddadi,A. ANovelHybridModelforCreditRiskAssessmentofSupplyChainFinanceBasedon
TopologicalDataAnalysisandGraphNeuralNetwork. IEEEAccess2025,13,13101–13127.[CrossRef]
81. Wang,D.;Zhang,Z.;Zhao,Y.;Huang,K.;Kang,Y.;Zhou,J. Financialdefaultpredictionviamotif-preservinggraphneural
networkwithcurriculumlearning. InProceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandData
Mining,LongBeach,CA,USA,6–10August2023;pp.2233–2242.
82. Liu,B.; Li,I.; Yao,J.; Chen,Y.; Huang,G.; Wang,J. UnveilingthePotentialofGraphNeuralNetworksinSMECreditRisk
Assessment. InProceedingsofthe20245thInternationalConferenceonIntelligentComputingandHuman-ComputerInteraction(ICHCI);
IEEE:Piscataway,NJ,USA,2024;pp.562–566.
83. Zhang,Z.;Shen,Q.;Hu,Z.;Liu,Q.;Shen,H. CreditriskanalysisforSMEsusinggraphneuralnetworksinsupplychain. In
Proceedingsofthe2025InternationalConferenceonBigData,ArtificialIntelligenceandDigitalEconomy,Kunming,China,
18–20July2025;pp.81–85.
84. Cheng,C.;Luo,C. EnterpriseCreditRatingFrameworkBasedonRiskContagionGraphNeuralNetwork. InProceedingsofthe
InternationalConferenceonMachineLearningandSoftComputing;Springer:Berlin/Heidelberg,Germany,2025;pp.243–254.
85. Bergmeir,C.; Benítez,J.M. Ontheuseofcross-validationfortimeseriespredictorevaluation. Inf. Sci. 2012,191,192–213.
[CrossRef]
86. Fonseca, P.G.; Lopes, H.D. Calibration of machine learning classifiers for probability of default modelling. arXiv 2017,
arXiv:1710.08901.[CrossRef]
87. Guo,C.;Pleiss,G.;Sun,Y.;Weinberger,K.Q. Oncalibrationofmodernneuralnetworks. InProceedingsoftheInternational
ConferenceonMachineLearning,Sydney,Australia,6–11August2017;pp.1321–1330.
88. Idwan, S.; Etaiwi, W.; Rafayia, H.; Matar, I. A comprehensive review of statistical variants and enhancements of SMOTE
oversamplingmethod. Int.J.DataSci.Anal.2025,20,6887–6904.[CrossRef]
89. Hu,X.;Chen,H.;Zhang,J.;Chen,H.;Liu,S.;Li,X.;Wang,Y.;Xue,X. GAT-COBO:Cost-sensitivegraphneuralnetworkfor
telecomfrauddetection. IEEETrans.BigData2024,10,528–542.[CrossRef]
90. Andrae,S. Fairnessandbiasinmachinelearningmodelsforcreditdecisions. InMachineLearningandModelingTechniquesin
FinancialDataScience;IGIGlobalScientificPublishing:Hershey,PA,USA,2025;pp.1–24.
91. Liao,J.;Wang,W.;Xue,J.;Lei,A.;Han,X.;Lu,K. Combatingsamplingbias:Aself-trainingmethodincreditriskmodels. In
ProceedingsoftheAAAIConferenceonArtificialIntelligence,Online,22February–1March2022;Volume36,pp.12566–12572.
92. Rudin,C. Stopexplainingblackboxmachinelearningmodelsforhighstakesdecisionsanduseinterpretablemodelsinstead.
Nat.Mach.Intell.2019,1,206–215.[CrossRef]
93. Hardt,M.;Price,E.;Srebro,N. Equalityofopportunityinsupervisedlearning. Adv.NeuralInf.Process.Syst.2016,29,3323–3331.
94. Wachter,S.;Mittelstadt,B.;Russell,C. Counterfactualexplanationswithoutopeningtheblackbox:Automateddecisionsandthe
GDPR. Harv.JLTech.2017,31,841.[CrossRef]
95. Greco,S.;Vacchetti,B.;Apiletti,D.;Cerquitelli,T. Unsupervisedconceptdriftdetectionfromdeeplearningrepresentationsin
real-time. IEEETrans.Knowl.DataEng.2025,37,6232–6245.[CrossRef]
96. Ximenes,R.;Alves,A.P.S.;Escovedo,T.;Spinola,R.;Kalinowski,M. InvestigatingIssuesthatLeadtoCodeTechnicalDebtin
MachineLearningSystems. InProceedingsofthe2025IEEE/ACM4thInternationalConferenceonAIEngineering–SoftwareEngineering
forAI(CAIN);IEEE:Piscataway,NJ,USA,2025;pp.173–183.
97. Bartlett,R.;Morse,A.;Stanton,R.;Wallace,N. Consumer-lendingdiscriminationintheFinTechEra. J.Financ. Econ. 2022,
143,30–56.[CrossRef]
98. Pradhan,R.;Alazzam,M.B.;Keswani,S.;Bhasin,N.K.;Jaff,N.A.;Muthuperumal,S. AHybridGRU-TransformerModelfor
FinancialForecastingandRiskManagement. InProceedingsofthe20253rdInternationalConferenceonIntegratedCircuitsand
CommunicationSystems(ICICACS);IEEE:Piscataway,NJ,USA,2025;pp.1–5.
99. Amershi,S.;Begel,A.;Bird,C.;DeLine,R.;Gall,H.;Kamar,E.;Nagappan,N.;Nushi,B.;Zimmermann,T. Softwareengineering
formachinelearning: Acasestudy. InProceedingsofthe2019IEEE/ACM41stInternationalConferenceonSoftwareEngineering:
SoftwareEngineeringinPractice(ICSE-SEIP);IEEE:Piscataway,NJ,USA,2019;pp.291–300.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/info17040395

Reproduced with permission of copyright owner. Further reproduction
prohibited without permission.