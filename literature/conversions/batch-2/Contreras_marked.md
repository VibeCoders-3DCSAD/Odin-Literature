---
conversion_metadata:
  converted_at: "2026-07-22T13:01:36Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Contreras.pdf"
  source_pdf_sha256: "ad678840118b48b6aa1b830055102257b0c97de3c2774e764286a32bb511e05d"
  page_count: 13
  markdown_char_count: 144334
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

ICCK Journal of Software Engineering
http://dx.doi.org/10.62762/JSE.2026.605759

RESEARCH ARTICLE

Adaptive Risk Evaluation in FinTech Systems via
Reinforcement-Based Continuous Policy Optimization

Edimer Mahecha Contreras 1,2,*

1 University of the Llanos, Villavicencio 500001, Colombia
2 Elite Group Services, San Jose, CA 95125, United States

Abstract

The key feature of FinTech software systems is
the ability to accurately assess risk in real time,
making decisions on high-volume streams of
information that are associated with very low
latency and are robust to concept drift, and able
to be updated without disrupting services. This
paper addresses the problem of adaptive risk
scoring using a reinforcement learning approach
by modeling the risk evaluation problem as a
continuous-action Markov Decision Process and
continuously optimizing the policy via streaming
transactional, behavioral events and outcome
driven reward feedback. In addition to the learning
algorithm, we also view ARL-CPO as a deployable
software architecture that separates online learning
from inference serving to enable a modular
approach to integrating ARL into production
risk pipelines, such as an inference microservice,
which is wrapped around an asynchronous update
loop, updating ARL models continuously without
periodic batch retraining — a capability not
available in the Random Forest, Gradient Boosting,
or Transformer baselines. We assess the approach

Submitted: 04 May 2026
Accepted: 25 May 2026
Published: 11 June 2026

Vol. 2, No. 2, 2026.

10.62762/JSE.2026.605759

*Corresponding author:
(cid:0) Edimer Mahecha Contreras
edimer.mahecha@unillanos.edu.co

156

on the prediction of credit default and adaptive asset
allocation in a big data dataset of 8.5 million credit
records, generated in a custom FinTech environment
simulator. The performance based on precision
and F1 score, of ARL-CPO is compared with the
baselines, and it outperforms them with 97.4%
classiﬁcation accuracy, 98.8% trend adaptation
rate (responsiveness to distributional shifts), and
96.1% cumulative long-term performance index
(normalized long-horizon reward). The ﬁndings
show that reinforcement learning-based continuous
policy updates is an achievable, adaptive element
for real-time risk systems in FinTech under the
evolution of market and user conditions.

Keywords: reinforcement learning, continuous policy
optimization, adaptive risk evaluation, FinTech software
systems, sequential decision learning, credit risk modeling.

1 Introduction
In recent years, the rise of FinTech platforms has
revolutionized the way ﬁnancial services are being
delivered, with software ecosystems that need to
handle high-frequency transactions, varied types of
user behavior and ever-changing market signals at
a large scale [1]. These systems not only require
risk assessment to be a modeling exercise, but also a

Citation
Contreras, E. M. (2026). Adaptive Risk Evaluation in FinTech Systems

via Reinforcement-Based Continuous Policy Optimization.

ICCK

Journal of Software Engineering, 2(2), 156–168.

© 2026 by the Author. Published by Institute of
Central Computation and Knowledge. This is an open
access article under the CC BY license (https://creati
vecommons.org/licenses/by/4.0/).

---

<!-- PAGE 2 -->

production-critical software capability on the request
path of credit underwriting, fraud screening, wallet
limits and automated portfolio services. Therefore,
risk evaluation components need to be able to
meet software engineering requirements including
low inference latency for real-time decision-making,
high throughput to process event streams, high
availability to ensure service availability, auditability
for regulatory review, and safe update to maintain
service continuity while modifying the risk logic.
However, ﬁnancial environments are not stationary
and the distribution drift can aﬀect the quality of
predictions very quickly, putting extra operational
pressure on risk pipelines to keep up with the
changes while still guaranteeing the correctness of
the predictions and ensuring observability during
production [2].

Traditional risk assessment methods, such as logistic
regression, discriminant analysis, decision trees
and rule-based expert systems, have traditionally
been attractive due to their interpretability and
computational eﬃciency.
These approaches are
straightforward to implement and manage, however
they are fragile to drift as the decision logic is to a large
extent ﬁxed when deployed. These systems often need
to be analyzed manually, retrained or updated with
rules oﬄine, and deployed days or weeks later when
customer behavior changes, market regimes change,
or the possibility of fraud changes. This introduces
a risk of deploying a production risk service to an
environment that is not the same as it is when it
was created, leading to the introduction of incorrect
scores into the ﬁnancial loss and compliance exposure.
Thus, the central engineering challenge is not just
predictive performance, it’s continuous adaptation in
strict operational conditions.

Many risk-related tasks beneﬁt from machine learning
models like Random Forest, Gradient Boosting, and
deep learning models such as Transformer-based
models [4]. They are, however, usually deployed
as batch-trained artifacts, which are retrained and
redeployed periodically in normal FinTech scenarios.
This design adds
some software engineering
constraints. First, model changes are linked to release
pipelines, which can involve downtime or traﬃc
re-routing. Secondly, the rate of retraining slows
down the adaptation to drift. Third, there is typically
no feedback loop from decisions to downstream
results to improve and evolve the inference service.
Furthermore, most supervised methods view risk
scoring as a one-step prediction task and do not

ICCK Journal of Software Engineering

consider it as a decision making process over multiple
interactions and time horizons, so as to optimize the
long-term results.

Instead, Reinforcement learning (RL) gives another
paradigm of learning, which can be represented
as repeated interactions between an agent and
an environment, optimizing a policy to maximize
cumulative discounted reward [5]. DRL is an
extension of RL, with neural function approximation
to cope with high-dimensional state and action spaces,
and has promise in portfolio optimization, algorithmic
execution, market making, and hedging [6]. But
software engineering aspects related to the application
of DRL to real-time adaptive risk evaluation are
inadequate. Existing work often emphasizes learning
performance while under-specifying how an adaptive
policy can be deployed safely in a production
FinTech service with requirements for low-latency
inference, fault tolerance, continuous updates without
service interruption, versioning and rollback, and
auditable decision logging.
the
research gap is not only algorithmic, but also a
missing software capability. Most existing approaches,
including gradient boosting methods for bank distress
prediction [3], are batch-trained and do not support
continuous policy reﬁnement in response to streaming
drift, leaving a gap for deployable, observable, and
production-safe adaptive risk pipelines.

Consequently,

with

Learning

To address this gap, this paper proposes Adaptive
Continuous
Reinforcement
Policy Optimization ARL-CPO for FinTech risk
scoring. ARL-CPO formulates risk evaluation as a
continuous-action Markov Decision Process and uses
a dual-module actor-critic design consisting of a policy
learning module and a value estimation module that
updates online through gradient-based reﬁnement.
baselines,
batch-retrained
Unlike
ARL-CPO incorporates
streaming transactional
and behavioral data and outcome-driven reward
signals to support continuous policy improvement
as conditions evolve [7]. In addition to presenting
the learning formulation, we position ARL-CPO
as a software architecture pattern for adaptive risk
services, where inference and online learning are
operationally separated to enable continuous updates
without interrupting real-time scoring and to support
integration into FinTech risk pipelines.

supervised

The main contributions of this work are as follows.

1. Software engineering problem formulation for
adaptive risk scoring in FinTech systems. We

157

---

<!-- PAGE 3 -->

ICCK Journal of Software Engineering

describe risk evaluation as a production software
component that must operate under drift while
meeting real-time constraints and continuous
update expectations, motivating a sequential
decision formulation rather than a static batch
prediction pipeline.

2. Deployable adaptive risk scoring architecture
using reinforcement learning based continuous
policy optimization. We propose ARL-CPO,
modeling risk scoring as a continuous-action
Markov Decision Process with an online-updated
dual-module policy and value design that
supports ﬁne-grained risk scoring and continuous
adaptation in streaming settings.

3. Empirical evaluation in a streaming FinTech
simulator environment. We evaluate ARL-CPO
on credit default prediction and adaptive asset
allocation using a large-scale dataset of 8.5 million
records and compare against Random Forest,
Gradient Boosting, and Transformer baselines,
reporting classiﬁcation accuracy of 97.4 percent,
trend adaptation rate of 98.8 percent, and
cumulative long-term performance index of 96.1
percent in the experimental setting.

The remainder of this paper is organized as follows.
The related work is discussed in Section 2. The
proposed ARL-CPO method and system design is
presented in Section 3. Experimental result and
discussion are presented in Section 4, followed by
conclusions and future directions.

2.1 Supervised Learning

for

Financial Risk

Modeling

Capitalized by their interpretability and ability to
easily be incorporated into an existing scoring service,
supervised pipelines continue to be widely used for
the credit default early warning and risk prediction.
The predictive power is enhanced when using
macroeconomic and borrower features as a gradient
boosting decision tree [8]. Such solutions, however, are
based on cycles of redeployment and oﬄine retraining
that may cause delays in update when there are regime
shifts. Likewise, when considering ﬁxed distributions,
Data-driven machine learning analysis of systemic
risk propagation in ﬁnancial networks identiﬁes
key drivers of contagion using classiﬁcation-based
it doesn’t have much
boundaries [9]. However,
mechanisms to keep adapting and can break when
it comes to changes in the feature sets distributions
if it is not retrained. SHAP-based Random Forest
models are more transparent and explainable for
regulatory decision-making purposes [10]. Despite
this,
they are still type of supervised classiﬁers
which need retraining to adjust decision boundaries.
Bayesian neural models enhance the capability of
being aware of uncertainty, which may help to
better determine appropriate decision thresholds
and calibrated output [11]. However, uncertainty
modelling is not suﬃcient to give an operational
mechanism to help a running service continuously
improve and/or update its policies in a safe way. These
models when deployed as a stateless prediction service
are often treated as a heavyweight pipeline that needs
to be managed for refreshing the models. Disciplined
testing and release controls are needed for production
readiness, not just oﬄine testing, including structured
evaluation checklists and rubrics for readiness [23].

2 Literature Review
The shift from static, batch-trained predictors to
services that continuously serve customers requires
unprecedented software standards such as low
latency inference, high throughput, fault tolerant,
auditable, and model-safe updates to models in
production [24]. Previous research includes modeling
for credit and fraud, sequential decision optimization
with reinforcement learning, and architectures for the
system-level deployment and streaming. Another
issue is that many high-accuracy models are not built
to be used as a production service with a well-designed
workﬂow for updates, and built-in monitoring of
operational systems, which causes “hidden technical
debt” in the deployed ML systems [22].

2.2 Deep Learning Architectures

for Credit

Assessment

The complexity of ﬁnancial data is high-dimensional
and cannot be adequately represented using
traditional approaches, while deep learning reduces
the complexity of the representation learning, but
introduces a higher degree of complexity in serving
and operation. For online credit scoring, transfer
learning frameworks with extreme learning machines
enable continuous model adaptation for automated
credit assessment without full retraining [12].
In
reality, it is still mostly used as an add-on to a model
that needs a controlled retraining and release process.
A graph neural network for relational credit risk
models identiﬁes the network eﬀects that are not

158

---

<!-- PAGE 4 -->

ICCK Journal of Software Engineering

Table 1. Comparative analysis of existing approaches.

Ref. / Technique

Application

Gradient Boosting [8]
ML-based Network Analysis [9]
XAI Random Forest [10]
Bayesian Neural Network [11]
Transfer Learning / ELM [12]
Graph Neural Network [13]
Explainable AI [14]
DQN [15]
PPO [16]
Transfer RL [17]
Bayesian RL [18]
Concept Drift Detection [19]
MLOps Framework [20]

Credit Default Early Warning
Systemic Risk Propagation
Credit Risk Transparency
Uncertainty-Aware Risk
Online Credit Scoring Adaptation
Relational Credit Risk
Interpretable Risk Detection
Pairs Trading / Discrete Action Control
Automated Market-Making
Cross-Market Strategy Adaptation
Uncertainty-Aware Policy Learning
Financial Streaming Data
Production ML Deployment & Monitoring

ARL-CPO (Proposed)

Adaptive FinTech Risk Evaluation

Continuous
Adaptation
×
×
×
×
×
×
Partial
(cid:88)
(cid:88)
(cid:88)
×
Partial
(cid:88)
(cid:88)

Sequential
Optimization
×
×
×
×
×
×
×
(cid:88)
(cid:88)
(cid:88)
(cid:88)
×
×
(cid:88)

Continuous
Actions
×
×
×
×
×
×
×
×
(cid:88)
(cid:88)
×
×
×
(cid:88)

Long-Term
Reward
×
×
×
×
×
×
×
(cid:88)
(cid:88)
(cid:88)
×
×
×
(cid:88)

Personalization

×
×
Partial
(cid:88)
(cid:88)
(cid:88)
×
×
×
Partial
(cid:88)
×
×
(cid:88)

captured by tabular models [13]. But they could
also add an inference latency and an infrastructure
overhead because of the construction of the graph
and neighborhood aggregation.
Explainable AI
methods in FinTech risk management provide
interpretable anomaly and risk signals that must
be integrated into downstream decision logic [14].
However, it often yields scores that must be handled
by the downstream system logic, routed to decision
thresholds and reviewed by humans, introducing
complexity into the software pipeline. Research in
software engineering has highlighted the need to
make clear engineering choices about data pipelines,
feature stores, reproducibly, and monitoring to prevent
fragility as requirements evolve when building an ML
based system [25].

2.3 Reinforcement

Learning Applications

in

Financial Systems

Reinforcement learning is able to solve for sequential
decision making and long-horizon goals, which
are not addressed by a prediction-only model.
DQN-based pairs
trading demonstrates policy
learning through interaction with simulated market
environments, though its discrete action formulation
limits ﬁne-grained continuous control [15]. It may not
oﬀer as much ﬁne-grained control as continuous action,
due to its discrete action formulation. In the ﬁnancial
domain, PPO-based market-making shows excellent
results for continuous control, and encourages
The
actor-critic style policy optimization [16].
relevance of this is for cross-market adaptation that is
useful to FinTech services operating across regions and
market regimes [17]. Bayesian reinforcement learning
provides principled uncertainty quantiﬁcation over
policies, which can improve objective clarity and
support risk-aware decision making [18]. But much
work in RL remains poorly-deﬁned in the isolation of

online learning from online inference, the governance
of policy updates, and the auditability of decisions in
regulated contexts. Important operational guidance
for the production of ML systems is to have explicit
controls for testing, rollout, monitoring, and rollback
to prevent unwanted changes in behavior of the
deployed systems.

2.4 Real-Time Adaptive Frameworks for FinTech
Streaming and deployment frameworks solve key
challenges in the FinTech space. In ﬁnancial streams,
the concept drift detection system keeps track of the
distribution shifts and selectively updates models [19].
Drift-aware mechanisms provide temporal robustness
but tend to be "reactive" in that they may have
periods of poor performance as they retrain and
redeploy. Standardized market environments and
benchmarks for ﬁnancial reinforcement learning,
such as FinRL-Meta, provide reusable simulation
infrastructure that supports scalable evaluation of
adaptive risk policies [21]. They, however, do not
necessarily include sequential decision optimization
or continuous policy improvement. Recent studies
about MLOps also highlight the need for production
ML systems to be monitored, reproducible, and to have
controlled release mechanisms to avoid building up
technical debt and reliability issues [22].

Table 1 shows that a number of supervised techniques
have been developed and proved to have good
predictive accuracy, however,
they generally do
not continuously adapt and need oﬄine refresh
cycles [8]. Deep models have the ability to learn
good representations but can be expensive to
serve and update reliably at scale [13]. When
applied to always-on FinTech services, reinforcement
learning provides the ability to sequentially optimize
and long-horizon objectives, but the question of
operationalization is often underspeciﬁed [16].

159

---

<!-- PAGE 5 -->

ICCK Journal of Software Engineering

Figure 1. The ARL-CPO Pipeline for Adaptive Risk Evaluation in FinTech Systems.

Streaming and microservice frameworks enhance
deployability and service reliability, but they don’t
bring online decision optimization together with safe
continuous update workﬂows [20]. This situation
encourages a method to solve adaptive risk evaluation,
which not only views it as a learning problem but also
as an engineered system with quality monitoring tools
and update control mechanisms.

3 Proposed Method
The current FinTech software-based platforms are
evolving at an unprecedented pace with multiple
vectors of risk that need to be constantly and adaptively
evaluated instruments. The poor scalability of both
the static coding models and deterministic rule
engines have had challenges in non-stationary data
distribution, high dimensional continuous feature
space and subtle behavioral patterns of digital
ﬁnancial users. To alleviate these disadvantages, this
paper proposes the Adaptive Reinforcement Learning
with Continuous Policy Optimization (ARL-CPO)
framework, a learning-based framework, that aims
to reshape the risk evaluation as a Continuous
Markov Decision Process (MDP) with Continuous
The
Action Space and Continuous State Space.
ARL-CPO agent learns the best risk-mitigation policies
without the need to have hand-written rules. Reward
formulation in the agent is loss sensitive, while

the dual-network (policy-value) structure enables
the agent to converge stably (taking account the
market regime changes). ARL-CPO provides better
adaptiveness, granularity and robustness in FinTech
risk management software, compared to both legacy
static pipelines and discrete-action reinforcement
learning baselines.

From a software engineering perspective, the targeted
problem is not only predictive performance, but also
the design of a risk evaluation service that can (i)
ingest streaming transactional and behavioral data
at high throughput, (ii) return a calibrated risk
score with bounded inference latency suitable for
real-time user journeys, (iii) support continuous policy
updates without downtime, and (iv) provide fault
tolerance and observability for production monitoring
In this work, ARL-CPO
and regulatory audits.
is positioned as a deployment-oriented learning
component that can be integrated into a modular
FinTech risk pipeline, where online learning is isolated
from the inference path to prevent update-induced
service instability, while decision logs and model
versions are preserved for compliance and post-hoc
investigation.

The provided architecture is a closed-loop pipeline
of adaptive risk assessment of the FinTech software
systems. The ﬁnancial data simulation layer is fed

160

---

<!-- PAGE 6 -->

streaming market indicators and customer behavioral
telemetry that reﬂect real-time operating conditions.
The state encoder then transforms the raw inputs into
a small observation vector which is then processed by
the ARL-CPO Decision Engine comprising a policy
network and a value approximation network. The
engine creates continuous risk scores that can be used
to make decisions regarding the eligibility of credit
and the actions necessary to rebalance the portfolio.
The ﬂow of the reward signal is calculated based on
the attained monetary results and this is ﬂowed back
to correct the policy of the agent in an iterative manner.
This closed loop design guarantees personalization,
ﬂexibility and state of the art accuracy in volatile
ﬁnancial ecosystems, which is illustrated in Figure 1.

The MDP formulation is selected to align with
deployed FinTech risk services where decisions
are repeated over time and outcomes (defaults,
losses, missed opportunities) arrive
chargebacks,
with delay.
Continuous actions are necessary
because production risk systems commonly require a
real-valued score that can be calibrated, thresholded,
and composed with downstream rules, rather than
a coarse discrete label.
In ARL-CPO, the action
is therefore treated as a continuous score in a
bounded interval (e.g., [0, 1]) which can be mapped
to operational labels (Low/Moderate/Elevated) only
at the business-rule layer. This separation preserves a
stable API contract (continuous score output) while
allowing product teams to adjust thresholds without
retraining the policy.

Algorithm 1 evaluates the instantaneous risk posture of
a ﬁnancial entity or market condition using the trained
ARL-CPO agent. The process starts with the market
feature vectors and user activity metrics combined
to one observation ot. This observation is mapped
to a scalar action at = the estimated risk magnitude
by the policy network (continuous action generator)
which maps this observation to a scalar action a. The
algorithm uses a value from 0 to 2 to represent at,
with 0 being Minimal, 1 being Moderate, and 2 being
Elevated. As the scoring mechanism is updated in each
observation, the scoring mechanism automatically
adapts to behavioral drift, thus enabling individual
credit adjudication and asset allocations optimization.

In a real deployment, Algorithm 1 can be the
inference path of a risk scoring microservice. The
service is exposed and should take the encoded
observation (or state) in as an argument and return
the continuous score right away. Every answer is

ICCK Journal of Software Engineering

recorded with a model version identiﬁer, a time stamp
and request info to enable traceability, auditability,
operational debugging. This allows for proposed
learning component to be inserted into current FinTech
software systems without business decision logic being
integrated into learning loop.

Γ(t − 1) = F (o, θ) − H(ξ)

subject to V > L(t − g)
(1)

All symbols in Eq.
(1) are deﬁned as follows.
Γ(t − 1) is the performance signal at time step (t −
1), the current observation (state representation)
is o, and the current set of policy parameters is
The observation and policy parameters are
θ.
denoted as provided by the function F (o, θ), which
is an uncertainty-related scoring function,
like a
conﬁdence-aware scoring function, or an entropy
ξ denotes a vector of threat indicators or
proxy.
drift-sensitive signals extracted from the stream. H(ξ)
represents the uncertainty/entropy of the threat
indications. V is a form of conﬁdence (such as a
validity score from a calibration layer or critic estimate).
The lower bound on acceptable conﬁdence is called
L(t − g) and g is a lag parameter that determines the
window of assessment. The constraint V > L(t −
g) ensures that risk actions are only accepted if the
minimum conﬁdence requirement is fulﬁlled, relevant
for safe deployment under distributional shift.

Ψ = {qr−1}(u, ξ) :=(cid:0)λ(ξ − d) + Ω(λk − Cr{t − 1})(cid:1)
· Ωu{d − 1}

(2)

Eq. (2) is a plain deﬁnition of an adjusted performance
tensor for adaptation control, u is a normalized
adaptation index (such as an intensity factor for
updates), ξ represents drift or threat indicators, λ
is a scaling factor for sensitivity to drift, d is a
reference drift baseline (or detection threshold), and
Ω is a temporal normalization operator. λk is a
reference performance level (or metric). Ωu{d −
1} is a normalization term that adjusts updates
based on the evaluation window. Cr{t − 1} is the
observed performance or correction term at time (t −
1). Operationally, Eq. (2) is used to modulate how
strongly the agent corrects internal estimates when
behavioral patterns shift, which supports stable online
operation.

Figure 2 depicts the ARL-CPO architecture that
a Policy
consists of two collaborating modules:

161

---

<!-- PAGE 7 -->

ICCK Journal of Software Engineering

Figure 2. ARL-CPO Dual-Module Architecture with Gradient-Based Policy Reﬁnement.

Learning Module and a Value Estimation Module.
The observation vector ot is received by the Policy
Learning Module which generates a continuous
risk-control action using the policy network and
injects controlled perturbation to explore.
The
Value Estimation Module stores transition tuples in
a memory bank, approximates expected cumulative
reward via the value approximation network and
stabilizes training using a target synchronization unit.
The policy reﬁnement process via gradients is a ﬂow
directed by the value module to the policy network,
making it possible to continuously improve the
policy. This modular separation is stable-convergent
and is especially applicable to the high-dimensional,
continuous-control requirements of real-time ﬁnancial
risk management.

While the dual-module (policy-value) separation
resembles the general actor-critic concept,
the
software-level contribution in ARL-CPO is the update
and synchronization pattern for continuous operation.
The inference service uses a ﬁxed, versioned snapshot
of the policy for consistent low-latency scoring,
while the learning module updates parameters
asynchronously on streaming feedback. The policies
are updated via a controlled rollout process, such as a
shadow evaluation, canary release, or staged rollout,
to ensure that there are no unsafe policy changes. This
design also ensures that there is no “training-induced
downtime,” and it allows for the possibility of
reverting back to a previous stable version of the
model, while also providing the opportunity to
continuously improve policies without disrupting the
serving path, a requirement for production FinTech
platforms.

The Algorithm 2 will be used to guide the iterative
process of reﬁning the policy of the ARL-CPO agent
using outcome-driven feedback. Once an agent
performs an action and sees the change in the
environment, a scalar reward is calculated. This
reward is compared with a performance baseline by the
algorithm. When the reward is at or below the base, the
existing policy parameters are maintained with some
stabilization updates to avoid overﬁtting. Otherwise,
the weights of the policy network are corrected with
the help of gradient-based corrections in such a way
that suboptimal decisions are penalized. The resulting
feedback loop allows the ARL-CPO agent to observe
non-stationary ﬁnancial dynamics and aid resilient
and informed risk governance.

For reproducibility and deployment realism, the
reward signal should be implemented as an explicit
function of observable business outcomes and risk
objectives, such as realized loss, default/fraud events,
and risk-adjusted return measures computed over a
deﬁned horizon.
In a production system, reward
computation is typically delayed and arrives via
asynchronous outcome events; therefore, the system
logs (observation, score, decision context, outcome)
tuples to compute rewards consistently and to
enable audit trails. This also supports compliance
requirements by retaining evidence of how each
decision was generated, which model version was
used, and what outcome feedback triggered future
policy updates.

tV ≡ Λ1∗(Φ{t−1}) → (t−1) ≤ Jλ|c−(β−ηr) for u ≡ ∇
(3)

Eq. (3) is clariﬁed as follows. tV denotes an aggregate

162

---

<!-- PAGE 8 -->

quality index at time t. Λ1 denotes a scaling constant
for quality aggregation. The feature vector at the
previous step is denoted as Φ{t−1} (e.g., reward
statistics from previous steps or stability indicators).
The baseline time index (t − 1) is used to compare
its current performance with recent history. Jλ|c is a
composite objective term composed of a risk penalty
adjustment, ηr, a base performance measure, β, and
a constraint to limit the updates, c. For operation, Eq.
(3) is applied to monitor the trade-oﬀ between service
stability and proactive risk governance in drift.

(cid:107)Λ(u, ωr)(cid:107) = Dξ(χ − λb) + Gω(τ, ρk) := δ(u − ρw) ≥ ∇
(4)

Eq. (4) is clariﬁed as follows, the norm (cid:107)Λ(u, ωr)(cid:107) is a
measure of the adaptation performance of the system
with update intensity u and a risk-weight parameter ωr.
The drift sensitive term Dξ(χ − λb) is a term involving
observed behavioral shift statistics, λb is a baseline
drift tolerance, and ξ is the drift indicator space. The
stability term is denoted as Gω(τ, ρk), with τ being an
update/synchronization rate and ρk being a parameter
of performance boundary. An update intensity u is
compared with a control boundary, ρw, denoted as
δ(u − ρw). The ≥ ∇ condition represents satisfying
all conﬁg thresholds. In deployment, these quantities
correspond to monitoring signals and guardrails (for
example, update-rate caps and drift thresholds) that
prevent unstable behavior under high load or sudden
market regime changes.

The ARL-CPO model is based on the concept of
reward-based continuous policy optimization to
reduce ﬁnancial risks in real-time. The architecture
demonstrates how the adaptive reinforcement learning
can be applied to support FinTech software systems in
oﬀering ﬂexible credit decisions and dynamic portfolio
management. This continuous-action control that
is enabled by the dual policy-value structure and
the gradient-based reﬁnement is especially useful in
complex ﬁnancial situations, where ﬁne-grained risk
adjustments are needed.

the proposed framework software
To make
engineering more explained, an explicit integration
diagram is shown in Figure 3 that explains how
ARL-CPO connects to platform components such
as API gateways, message queues, databases, and
monitoring tools.
This diagram complements
Figures 1 and 2 by focusing on deployability, system
boundaries, and operational control points (logging,

ICCK Journal of Software Engineering

model registry, rollout/rollback), rather than only the
learning ﬂow.

Figure 3 illustrates how the ARL-CPO decision
engine can be embedded into a production-grade
FinTech risk evaluation pipeline as an always-on
software service. The client applications use the
API Gateway to make calls to the risk scoring
capability, which then forwards to the Risk Scoring
Service (inference microservice) that loads a versioned
policy snapshot πθ(vk) and returns a continuous risk
score that has a short latency. At the same time,
external market indicators and transaction or user
signals are continuously ingested into the system
via streaming. Meanwhile, market indicators and
transaction or user signals are continuously ingested
from the outside world and transformed by the
Feature/State Builder into the state representation
(st/ot) that is utilized for inference and learning.
Many downstream platform services (defaults, fraud
conﬁrmations, realized loss/return) trigger outcome
events, which are fed to the Outcome and Reward
Service to calculate rt, and to create training tuples
These tuples then go into
(st, at, rt, st{t + 1}).
an Online Learning Service that updates the actor
and critic, asynchronously, and stores the updated
policies in a Model Registry. A controlled canary or
shadow rollout loop helps ensure safe, downtime-free
updates through promoting new model versions after
validation, and the Audit/Compliance storage and
Monitoring/Observability provide logs, metrics, traces,
drift signals and alerts to meet operational reliability
and regulatory traceability requirements.
The
proposed methodology is based on continuous-action
reinforcement learning and uses a deployment-aware
software architecture as a means to separate inference
from training, to handle versioned deployment and to
provide monitoring and compliance logging. That is
the methodology for ARL-CPO as an adaptive learning
framework as well as a practical component of the
FinTech software system.

4 Results and Discussions
This section entails the experimental analysis of the
oﬀered ARL-CPO framework implemented to the
adaptive risk assessment in FinTech software systems.
It contrasts its framework to three frameworks that
are already in use: Random Forest (RF), Gradient
Boosting (GB), and Transformer-based models (TFM)
for credit default prediction and dynamic asset
allocation problems. The evaluation validates that
continuous optimization policy is more accurate,

163

---

<!-- PAGE 9 -->

ICCK Journal of Software Engineering

Figure 3. ARL-CPO Integration into a Production FinTech Risk System.

reactive and stable over time than other policy
optimization policies with single or batch trained
policies.

4.1 Dataset and Experimental Conﬁguration
These experiments make use of a large-scale ﬁnancial
dataset of 8.5 million records that have been generated
using advanced generative modeling methods, and
which are regulatory compliant and distributional
faithful
The
to real-world ﬁnancial patterns.
data includes the customer demographics proﬁles,
multi-channel transactions history, credit application
It is extensive
record and account lifecycle events.
and heterogeneous and, therefore, is highly tailored to
the evaluation of adaptive learning systems, ﬁnancial
forecasting modules, and behavioral segmentation
pipelines.
Table 2 will give a summary of the
experimental design.

4.2 Prediction Accuracy Analysis
The precision of prediction of all the four methods
at progressive levels of evaluation are shown
in Figure 4. The maximum prediction accuracy
of the ARL-CPO system, based on precision is
97.4% that is much higher than all the baselines.
This primacy is based on the ability of the agent
to keep evolving its internal representations in
response to interaction with non-stationary streams
of ﬁnancial data. The ARL-CPO agent also takes
advantage of each prediction as an element in a long
sequence of decisions, gradually learning complex
nonlinear relationships between user behavior and
market dynamics. The Transformer baseline shows
competitive performance at shorter intervals but

164

Table 2. Experimental conﬁguration.

Rate

Parameter
Environment
Task
State Space

/

Description / Value
FinTech adaptive risk scoring using streaming
market and transactional data
Market indicators, behavioral risk signals, credit
utilization metrics
Continuous risk score adjustment ∈ [0, 2]
3 hidden layers with 512, 384, and 256 units,
Leaky ReLU activations
3 hidden layers with 512, 384, and 256 units,
Leaky ReLU activations
0.0005

Action Space
Policy Network
Architecture
Value Network
Architecture
Learning
(Policy)
Learning
(Value)
Discount Factor
(γ)
Transition
Memory Capacity
Mini-batch Size
Exploration
Strategy
Training Episodes
Max Steps per
Episode
Reward Function Negative expected shortfall combined with

128
Gaussian noise injection, σ=0.18, decay rate
0.995
350 episodes
250 steps

1,500,000 tuples

0.0008

Rate

0.98

Target Network
Sync Rate
Hardware
Software

risk-adjusted return
Soft update parameter τ = 0.003

AMD EPYC 7742 CPU; NVIDIA A100 80GB GPU
PyTorch framework, Ubuntu 22.04; custom
FinTech environment simulator

plateaus over time, whereas ARL-CPO continues
improving through its reward-based adaptation
The continuous action formulation
mechanism.
also allows ﬁne-grained,
context-sensitive risk
quantiﬁcation as opposed to coarse categorical
assignments.

---

<!-- PAGE 10 -->

ICCK Journal of Software Engineering

percent cumulative performance index is evidence
that the algorithm is capable of optimizing sustained
performance as opposed to greedy short-horizon
returns. When the risk assessment is deﬁned as a
sequence of optimization problems in which the future
reward is discounted (γ = 0.98) and the future risk is
considered to determine the best strategy, the agent
learns strategies that trade the immediate reduction of
risk with the long-term health of the portfolio. This is
echoed in the reduced levels of default in credit rating
and more predictable risk adjusted returns in the asset
allocation. The area under curve comparison clearly
shows that ARL-CPO is continuing to increase the
gap between performance compared with baselines
as training continues: RF plateaus at 55.4%, GB
It
levels oﬀ at 63.2% and TFM levels oﬀ at 74.8%.
is discovered that the policy reﬁnement mechanism
has compounding advantages with longer training
horizons, which is a feature needed in FinTech systems
where long-term risk governance deﬁnes the viability
of the platform.

Figure 6. Cumulative Long-Term Performance Index over
Training Epochs.

respectively.

architectural beneﬁts

Table 3 summarizes the quantitative results of all
the three evaluation dimensions. The ARL-CPO
framework outperforms
the strongest baseline
(TFM) by 18.9%, 26.4%, and 21.3% in prediction
trend adaptation rate, and long-term
accuracy,
Such gains can be
performance,
attributed to three
(1)
continuous policy optimization mechanism that
removes batch-retraining latency (2) dual-module
separation that allows stable convergence under
distributional shift (3) reward-based sequential
formulation that must focus on cumulative risk
reduction rather than myopic predictions. Overall,
these ﬁndings support ARL-CPO as a resoundingly
better solution to adaptive risk evaluation within
modern FinTech software solutions.

165

Figure 4. Comparison of Accuracy of Prediction across
Evaluation Intervals.

4.3 Trend Adaptation Rate Analysis
The rate of trend adaptation that was plotted in
Figure 5, quantiﬁes the responsiveness of each method
to distributional changes in ﬁnancial behavior and
market regimes. The adaptation rate of ARL-CPO is
98.8% which conﬁrms that it is the most responsive
among all baselines. Conventional algorithms have a
high latency in detecting new patterns: RF converges
on about 48.1%, GB converges on about 58.6% and
TFM converges on about 72.4% at the last iteration. The
ARL-CPO agent updates its policy parameters at each
interaction cycle, and thus does not have the retraining
bottleneck at all. The dual-module architecture with
the separation of policy learning and value estimation
enables the stable and rapid convergence without
catastrophic forgetting, and the ability to accommodate
new distributional information. Such a property is
absolutely essential on FinTech platforms where user
behavior and regulatory environments may change at
any time.

Figure 5. Trend Adaptation Rate Across Test Iterations.

4.4 Long-Term Cumulative Performance Analysis
Figure 6 illustrates the cumulative performance
index of all the methods after 300 training epochs.
The fact that ARL-CPO is able to achieve 96.1

---

<!-- PAGE 11 -->

ICCK Journal of Software Engineering

Table 3. Comparative performance analysis of ARL-CPO against baseline methods.

Method

Random Forest (RF)
Gradient Boosting (GB)
Transformer (TFM)

Prediction
Accuracy (%)
62.3
71.2
78.5

Trend Adaptation
Rate (%)
48.1
58.6
72.4

Cumulative Long-Term
Performance (%)
55.4
63.2
74.8

ARL-CPO (Proposed)

97.4

98.8

96.1

Metric

Table 4. Software system performance evaluation (deployment-oriented metrics).
ARL-CPO
(Proposed)
7.6 / 18.4
5,200
3.2
42
31
2.7

Inference latency (ms/request), p50 / p95
Throughput (requests/second)
Peak memory usage (GB)
CPU utilization (%) at peak load
GPU utilization (%) at peak load
Model update time (sec/update)

2.1 / 4.8
18,500
1.1
68
Not used

3.4 / 7.2
12,400
1.6
71
Not used

Not applicable Not applicable

GB

RF

TFM

19.8 / 46.5
1,950
6.8
38
44
9.4

Table 4 reports the deployment-oriented software
performance metrics (inference latency, throughput,
resource utilization, and model update time),
demonstrating that ARL-CPO can support real-time
risk scoring while maintaining practical online
update overhead in a production-like FinTech service
environment. Each method was tested 10 times
independently with diﬀerent random seed, and the
results are presented as mean ± SD. Using the run
distribution, 95% conﬁdence intervals were computed
for all three primary metrics for Figures 4, 5 and
6; statistical signiﬁcance testing using the strongest
baseline (TFM) conﬁrmed the improvements of
ARL-CPO are statistically signiﬁcant (p < 0.01) for
all three primary metrics. To prevent exploiting
online updates, an extra online baseline (incremental
ﬁne-tuning of the Transformer at ﬁxed update periods
with a sliding window) was additionally tested,
which was more responsive than the TFM oﬄine,
but not as well as ARL-CPO on both adaptation and
long-horizon performance. The trend adaptation rate
(98.8%) is calculated as the percentage of post-drift
test iterations in which the method is recovered within
a predetermined recovery time window, to within 2%
of the pre-drift level. In addition to predictive metrics,
a deployment-oriented evaluation was performed
on the stated hardware to characterize operational
feasibility in real-time FinTech services.

The results of the experiment clearly prove the
originality and excellence of the proposed ARL-CPO
framework in comparison with the current ones in the
sphere of FinTech risk assessment. ARL-CPO is the ﬁrst
framework to unify continuous policy optimization,

dual-module gradient-based reﬁnement, and real-time
adaptive learning in a single architecture speciﬁcally
designed to govern ﬁnancial risk. Simultaneously
achieving 97.4% prediction accuracy, 98.8% trend
adaptation rate, and 96.1% cumulative long-term
performance — outperforming the strongest baseline
by margins over 18 percent — demonstrates that risk
assessment formulated as a continuous-action Markov
Decision Process with loss-sensitive reward signals
yields fundamentally superior decision intelligence
than prediction-only paradigms. The combination of
granular continuous scoring, real-time environmental
control and long-horizon reward maximization in a
single FinTech risk assessment pipeline does not exist
in prior work within the reviewed literature.

5 Conclusion
This article proposes an adaptive risk assessment
framework for FinTech software systems using
reinforcement-based continuous policy optimization
through the ARL-CPO architecture.
Beyond
algorithmic performance, the work contributes a
deployment-oriented design view of adaptive risk
scoring as an always-on software service, emphasizing
interrupting
continuous online updates without
and
inference, versioned model management,
operational monitoring for reliability and auditability.
Unlike models that are trained in batches (like Random
Forest, Gradient Boosting and Transformer-based
models), ARL-CPO continually adapts its decision
policy based on the changing ﬁnancial behaviors,
market regimes and user activity patterns. The
empirical testing of the credit default prediction and

166

---

<!-- PAGE 12 -->

the asset allocation with trend adaptation tasks in
a large-scale synthetic FinTech environment yields
a predictive accuracy of 97.4%, trend adaptation of
98.8%, and cumulative long-term performance index
of 96.1%. Moreover, it provides inference latency,
throughput, resource utilization, and online update
time at the system level, which helps in demonstrating
the practical feasibility of ARL-CPO for real-time
FinTech risk pipelines.

These ﬁndings are encouraging, but
the study
is constrained by the use of a dataset and a
simulated environment; and operational constraints,
feedback delays, and compliance requirements in real
deployments may vary signiﬁcantly. So, any reference
to real-world generalization must be understood
within this context and more testing is needed on
public or production datasets.

Future research will be based on production grade
software engineering problems that will facilitate
safe continuous learning in regulated FinTech
settings. This includes model versioning, lineage
tracking, controlled A/B testing and canary rollouts,
automated rollback strategies, drift monitoring and
alerting, and enhanced audit logging for regulatory
review. Further, mechanisms for interpreting policies
such as attention-based policy visualization and
counterfactual explanations will be discussed to
enhance interpretability and inter-agent extensions
will be explored for
interdependent ﬁnancial
ecosystems.

Data Availability Statement

Data will be made available on request.

Funding
This work was supported without any funding.

Conﬂicts of Interest
Edimer Mahecha Contreras is aﬃliated with the
Elite Group Services, San Jose, CA 95125, United
States. The author declares that this aﬃliation had no
inﬂuence on the study design, data collection, analysis,
interpretation, or the decision to publish. Edimer
Mahecha Contreras also served as an Associate Editor
of the ICCK Journal of Software Engineering at the time
of manuscript submission. To ensure the integrity of
the peer-review process, Edimer Mahecha Contreras
was not involved in the editorial handling, peer review,
or decision-making process for this manuscript, which
was handled independently by another editor.

ICCK Journal of Software Engineering

AI Use Statement

The author declares that no generative AI was used in
the preparation of this manuscript.

Ethical Approval and Consent to Participate

Not applicable.

References
[1] Mashrur, A., Luo, W., Zaidi, N. A., & Robles-Kelly,
A. (2020). Machine learning for ﬁnancial risk
management: a survey. IEEE Access, 8, 203203-203223.
[CrossRef]

[2] Lu, J., Liu, A., Dong, F., Gu, F., Gama, J., & Zhang, G.
(2018). Learning under concept drift: A review. IEEE
transactions on knowledge and data engineering, 31(12),
2346-2363. [CrossRef]

[3] Climent, F., Momparler, A., & Carmona, P. (2019).
Anticipating bank distress in the Eurozone: An
extreme gradient boosting approach. Journal of business
research, 101, 885-896. [CrossRef]

[4] Zeng, Z., Kaur, R., Siddagangappa, S., Rahimi, S.,
Balch, T., & Veloso, M. (2023). Financial time series
forecasting using CNN and transformer. arXiv preprint
arXiv:2304.04912. [CrossRef]

[5] Hambly, B., Xu, R., & Yang, H. (2023). Recent advances
in reinforcement learning in ﬁnance. Mathematical
Finance, 33(3), 437-503. [CrossRef]

[6] Liu, X. Y., Xiong, Z., Zhong, S., Yang, H., &
Walid, A. (2018). Practical deep reinforcement
learning approach for stock trading. arXiv preprint
arXiv:1811.07522. [CrossRef]

[7] Zhang, Y., Zhao, P., Wu, Q., Li, B., Huang, J., & Tan,
M. (2020). Cost-sensitive portfolio selection via deep
reinforcement learning. IEEE Transactions on knowledge
and data engineering, 34(1), 236-248. [CrossRef]

[8] Li, H., Cao, Y., Li, S., Zhao, J., & Sun, Y. (2020).
XGBoost model and its application to personal credit
evaluation. IEEE Intelligent Systems, 35(3), 52-61.
[CrossRef]

[9] Alexandre, M., Silva, T. C., Connaughton, C., &
Rodrigues, F. A. (2021). The drivers of systemic
risk in ﬁnancial networks: a data-driven machine
learning analysis. Chaos, Solitons & Fractals, 153, 111588.
[CrossRef]

[10] Xu, Q., Liao, Y., Li, Q., Zhang, J., Song, Z., Wang, L.,
& Yuan, X. (2024, August). SHAP-based Interpretable
Models for Credit Default Assessment Using Machine
Learning. In 2024 14th International Conference on
Software Technology and Engineering (ICSTE) (pp.
213-217). IEEE. [CrossRef]

[11] Jospin, L. V., Laga, H., Boussaid, F., Buntine,
W., & Bennamoun, M. (2022). Hands-on Bayesian
neural networks—A tutorial for deep learning users.

167

---

<!-- PAGE 13 -->

ICCK Journal of Software Engineering

IEEE Computational Intelligence Magazine, 17(2), 29-48.
[CrossRef]

[12] Alasbahi, R., & Zheng, X. (2022). An online
transfer learning framework with extreme learning
machine for automated credit scoring. IEEE Access, 10,
46697-46716. [CrossRef]

[13] Cheng, D., Niu, Z., Li, J., & Jiang, C. (2022). Regulating
systemic crises: Stemming the contagion risk in
networked-loans through deep graph learning. IEEE
Transactions on Knowledge and Data Engineering, 35(6),
6278-6289. [CrossRef]

[14] Bussmann, N., Giudici, P., Marinelli, D., & Papenbrock,
J. (2020). Explainable AI in ﬁntech risk management.
Frontiers in Artiﬁcial Intelligence, 3, 26. [CrossRef]

359-483. [CrossRef]

[19] Gama, J., Žliobait˙e, I., Bifet, A., Pechenizkiy, M., &
Bouchachia, A. (2014). A survey on concept drift
adaptation. ACM computing surveys (CSUR), 46(4),
1-37. [CrossRef]

[20] Kreuzberger, D., Kühl, N., & Hirschl, S. (2023).
Machine learning operations (mlops): Overview,
deﬁnition,
11,
31866-31879. [CrossRef]

and architecture.

IEEE Access,

[21] Liu, X. Y., Xia, Z., Rui, J., Gao, J., Yang, H., Zhu, M., ... &
Guo, J. (2022). FinRL-Meta: Market environments and
benchmarks for data-driven ﬁnancial reinforcement
learning. Advances in Neural Information Processing
Systems, 35, 1835-1849.

[15] Brim, A. (2020, January). Deep reinforcement learning
pairs trading with a double deep Q-network. In 2020
10th annual computing and communication workshop and
conference (CCWC) (pp. 0222-0227). IEEE. [CrossRef]

[22] Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips,
T., Ebner, D.,
... & Dennison, D. (2015). Hidden
technical debt in machine learning systems. Advances
in neural information processing systems, 28.

[16] Gašperov, B., & Kostanjčar, Z. (2022). Deep
reinforcement learning for market making under a
Hawkes process-based limit order book model. IEEE
control systems letters, 6, 2485-2490. [CrossRef]

[17] Mashetty, P. C., Gangabathula, S., Gangabathula, N.
V., Pullalarevu, N., Chaganti, K. R., & Chaganti, S.
R. (2025, July). Transfer Learning for Cross-Market
Predictions: Applications in Emerging and Volatile
Economies. In 2025 6th International Conference on
Data Intelligence and Cognitive Informatics (ICDICI) (pp.
621-626). IEEE. [CrossRef]

[18] Ghavamzadeh, M., Mannor, S., Pineau, J., & Tamar,
A. (2015). Bayesian reinforcement learning: A survey.
Foundations and Trends® in Machine Learning, 8(5-6),

[23] Breck, E., Cai, S., Nielsen, E., Salib, M., & Sculley, D.
(2017, December). The ML test score: A rubric for ML
production readiness and technical debt reduction. In
2017 IEEE international conference on big data (big data)
(pp. 1123-1132). IEEE. [CrossRef]

[24] Amershi, S., Begel, A., Bird, C., DeLine, R., Gall,
H., Kamar, E., ... & Zimmermann, T. (2019, May).
Software engineering for machine learning: A case
study. In 2019 IEEE/ACM 41st International Conference
on Software Engineering: Software Engineering in Practice
(ICSE-SEIP) (pp. 291-300). IEEE. [CrossRef]

[25] Kim, M., Zimmermann, T., DeLine, R., & Begel, A.
(2017). Data scientists in software teams: State of
the art and challenges. IEEE Transactions on Software
Engineering, 44(11), 1024-1038. [CrossRef]

168

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

ICCKJournalofSoftwareEngineering
http://dx.doi.org/10.62762/JSE.2026.605759
RESEARCH ARTICLE
Adaptive Risk Evaluation in FinTech Systems via
Reinforcement-Based Continuous Policy Optimization
1,2,*
EdimerMahechaContreras
1UniversityoftheLlanos,Villavicencio500001,Colombia
2EliteGroupServices,SanJose,CA95125,UnitedStates
Abstract onthepredictionofcreditdefaultandadaptiveasset
allocation in a big data dataset of 8.5 million credit
The key feature of FinTech software systems is
records,generatedinacustomFinTechenvironment
the ability to accurately assess risk in real time,
simulator. The performance based on precision
making decisions on high-volume streams of
and F1 score, of ARL-CPO is compared with the
information that are associated with very low
baselines, and it outperforms them with 97.4%
latency and are robust to concept drift, and able
classification accuracy, 98.8% trend adaptation
to be updated without disrupting services. This
rate (responsiveness to distributional shifts), and
paper addresses the problem of adaptive risk
96.1% cumulative long-term performance index
scoring using a reinforcement learning approach
(normalized long-horizon reward). The findings
by modeling the risk evaluation problem as a
showthatreinforcementlearning-basedcontinuous
continuous-action Markov Decision Process and
policy updates is an achievable, adaptive element
continuously optimizing the policy via streaming
for real-time risk systems in FinTech under the
transactional, behavioral events and outcome
evolutionofmarketanduserconditions.
drivenrewardfeedback. Inadditiontothelearning
algorithm, we also view ARL-CPO as a deployable
softwarearchitecturethatseparatesonlinelearning Keywords: reinforcement learning, continuous policy
from inference serving to enable a modular optimization, adaptive risk evaluation, FinTech software
approach to integrating ARL into production systems,sequentialdecisionlearning,creditriskmodeling.
risk pipelines, such as an inference microservice,
which is wrapped around an asynchronous update
1 Introduction
loop, updating ARL models continuously without
In recent years, the rise of FinTech platforms has
periodic batch retraining — a capability not
revolutionized the way financial services are being
available in the Random Forest, Gradient Boosting,
delivered, with software ecosystems that need to
or Transformer baselines. We assess the approach
handle high-frequency transactions, varied types of
user behavior and ever-changing market signals at
a large scale [1]. These systems not only require
riskassessmenttobeamodelingexercise,butalsoa
Citation
Submitted:04May2026
Contreras,E.M.(2026).AdaptiveRiskEvaluationinFinTechSystems
Accepted:25May2026
Published:11June2026 viaReinforcement-BasedContinuousPolicyOptimization. ICCK
JournalofSoftwareEngineering,2(2),156–168.
Vol.2,No.2,2026.
10.62762/JSE.2026.605759 © 2026 by the Author. Published by Institute of
CentralComputationandKnowledge.Thisisanopen
*Correspondingauthor: accessarticleundertheCCBYlicense(https://creati
(cid:0)EdimerMahechaContreras
vecommons.org/licenses/by/4.0/).
edimer.mahecha@unillanos.edu.co
156

ICCKJournalofSoftwareEngineering
production-criticalsoftwarecapabilityontherequest consideritasadecisionmakingprocessovermultiple
path of credit underwriting, fraud screening, wallet interactionsandtimehorizons,soastooptimizethe
limits and automated portfolio services. Therefore, long-termresults.
| risk evaluation |     | components  |            |              | need             | to be    | able      | to              |               |              |            |          |          |                |           |
| --------------- | --- | ----------- | ---------- | ------------ | ---------------- | -------- | --------- | --------------- | ------------- | ------------ | ---------- | -------- | -------- | -------------- | --------- |
|                 |     |             |            |              |                  |          |           | Instead,        | Reinforcement |              |            | learning | (RL)     | gives          | another   |
| meet software   |     | engineering |            | requirements |                  |          | including |                 |               |              |            |          |          |                |           |
|                 |     |             |            |              |                  |          |           | paradigm        | of            | learning,    |            | which    | can      | be represented |           |
| low inference   |     | latency     | for        | real-time    | decision-making, |          |           |                 |               |              |            |          |          |                |           |
|                 |     |             |            |              |                  |          |           | as repeated     |               | interactions |            | between  |          | an             | agent and |
| high throughput |     |             | to process |              | event            | streams, | high      |                 |               |              |            |          |          |                |           |
|                 |     |             |            |              |                  |          |           | an environment, |               |              | optimizing |          | a policy | to             | maximize  |
availabilitytoensureserviceavailability,auditability
|                |     |         |     |      |        |     |          | cumulative |     | discounted |     | reward | [5]. | DRL | is an |
| -------------- | --- | ------- | --- | ---- | ------ | --- | -------- | ---------- | --- | ---------- | --- | ------ | ---- | --- | ----- |
| for regulatory |     | review, | and | safe | update | to  | maintain |            |     |            |     |        |      |     |       |
extensionofRL,withneuralfunctionapproximation
| service | continuity |     | while | modifying |     | the risk | logic. |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ----- | --------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
tocopewithhigh-dimensionalstateandactionspaces,
| However, | financial |     | environments |     | are | not stationary |     |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------------ | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andhaspromiseinportfoliooptimization,algorithmic
| and the     | distribution |               | drift | can     | affect | the quality |     | of         |        |     |         |     |         |     |          |
| ----------- | ------------ | ------------- | ----- | ------- | ------ | ----------- | --- | ---------- | ------ | --- | ------- | --- | ------- | --- | -------- |
|             |              |               |       |         |        |             |     | execution, | market |     | making, | and | hedging |     | [6]. But |
| predictions |              | very quickly, |       | putting | extra  | operational |     |            |        |     |         |     |         |     |          |
softwareengineeringaspectsrelatedtotheapplication
| pressure        | on    | risk  | pipelines    | to  | keep          | up          | with the |             |     |                                     |          |     |      |            |     |
| --------------- | ----- | ----- | ------------ | --- | ------------- | ----------- | -------- | ----------- | --- | ----------------------------------- | -------- | --- | ---- | ---------- | --- |
|                 |       |       |              |     |               |             |          | of DRL      | to  | real-time                           | adaptive |     | risk | evaluation | are |
| changes         | while | still | guaranteeing |     | the           | correctness |          | of          |     |                                     |          |     |      |            |     |
|                 |       |       |              |     |               |             |          | inadequate. |     | Existingworkoftenemphasizeslearning |          |     |      |            |     |
| the predictions |       | and   | ensuring     |     | observability |             | during   |             |     |                                     |          |     |      |            |     |
performancewhileunder-specifyinghowanadaptive
production[2].
|     |     |     |     |     |     |     |     | policy | can | be deployed |     | safely | in  | a   | production |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------- | --- | ------ | --- | --- | ---------- |
Traditionalriskassessmentmethods,suchaslogistic FinTech service with requirements for low-latency
regression, discriminant analysis, decision trees inference,faulttolerance,continuousupdateswithout
|                |     |        |     |          |      |               |     | service | interruption, |     | versioning |     | and | rollback, | and |
| -------------- | --- | ------ | --- | -------- | ---- | ------------- | --- | ------- | ------------- | --- | ---------- | --- | --- | --------- | --- |
| and rule-based |     | expert |     | systems, | have | traditionally |     |         |               |     |            |     |     |           |     |
been attractive due to their interpretability and auditable decision logging. Consequently, the
computational efficiency. These approaches are research gap is not only algorithmic, but also a
|     |     |     |     |     |     |     |     | missingsoftwarecapability. |     |     |     | Mostexistingapproaches, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- |
straightforwardtoimplementandmanage,however
theyarefragiletodriftasthedecisionlogicistoalarge includinggradientboostingmethodsforbankdistress
extentfixedwhendeployed. Thesesystemsoftenneed prediction[3],arebatch-trainedanddonotsupport
to be analyzed manually, retrained or updated with continuouspolicyrefinementinresponsetostreaming
|     |     |     |     |     |     |     |     | drift, leaving |     | a gap | for | deployable, |     | observable, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --- | ----------- | --- | ----------- | --- |
rulesoffline,anddeployeddaysorweekslaterwhen
customer behavior changes, market regimes change, production-safeadaptiveriskpipelines.
| or the       | possibility  |         | of fraud     | changes.     |      | This introduces |           |               |              |      |            |       |          |            |          |
| ------------ | ------------ | ------- | ------------ | ------------ | ---- | --------------- | --------- | ------------- | ------------ | ---- | ---------- | ----- | -------- | ---------- | -------- |
|              |              |         |              |              |      |                 |           | To address    | this         | gap, | this       | paper | proposes |            | Adaptive |
| a risk       | of deploying |         | a production |              | risk | service         | to an     |               |              |      |            |       |          |            |          |
|              |              |         |              |              |      |                 |           | Reinforcement |              |      | Learning   |       | with     | Continuous |          |
| environment  |              | that    | is not       | the same     | as   | it is           | when      | it            |              |      |            |       |          |            |          |
|              |              |         |              |              |      |                 |           | Policy        | Optimization |      | ARL-CPO    |       | for      | FinTech    | risk     |
| was created, |              | leading | to the       | introduction |      | of              | incorrect |               |              |      |            |       |          |            |          |
|              |              |         |              |              |      |                 |           | scoring.      | ARL-CPO      |      | formulates |       | risk     | evaluation | as a     |
scoresintothefinanciallossandcomplianceexposure.
continuous-actionMarkovDecisionProcessanduses
| Thus, | the central |     | engineering |     | challenge | is  | not just |     |     |     |     |     |     |     |     |
| ----- | ----------- | --- | ----------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
adual-moduleactor-criticdesignconsistingofapolicy
predictiveperformance,it’scontinuousadaptationin
learningmoduleandavalueestimationmodulethat
strictoperationalconditions.
|     |     |     |     |     |     |     |     | updates | online          | through |     | gradient-based |     |     | refinement. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | ------- | --- | -------------- | --- | --- | ----------- |
|     |     |     |     |     |     |     |     | Unlike  | batch-retrained |         |     | supervised     |     |     | baselines,  |
Manyrisk-relatedtasksbenefitfrommachinelearning
models like Random Forest, Gradient Boosting, and ARL-CPO incorporates streaming transactional
|               |      |        |      |          |                      |     |          | and behavioral |            | data | and        | outcome-driven |        |             | reward |
| ------------- | ---- | ------ | ---- | -------- | -------------------- | --- | -------- | -------------- | ---------- | ---- | ---------- | -------------- | ------ | ----------- | ------ |
| deep learning |      | models |      | such     | as Transformer-based |     |          |                |            |      |            |                |        |             |        |
|               |      |        |      |          |                      |     |          | signals        | to support |      | continuous |                | policy | improvement |        |
| models        | [4]. | They   | are, | however, | usually              |     | deployed |                |            |      |            |                |        |             |        |
as batch-trained artifacts, which are retrained and as conditions evolve [7]. In addition to presenting
redeployedperiodicallyinnormalFinTechscenarios. the learning formulation, we position ARL-CPO
|      |        |      |      |          |     |             |     | as a software |     | architecture |     | pattern |     | for adaptive | risk |
| ---- | ------ | ---- | ---- | -------- | --- | ----------- | --- | ------------- | --- | ------------ | --- | ------- | --- | ------------ | ---- |
| This | design | adds | some | software |     | engineering |     |               |     |              |     |         |     |              |      |
constraints. First,modelchangesarelinkedtorelease services, where inference and online learning are
pipelines, which can involve downtime or traffic operationallyseparatedtoenablecontinuousupdates
withoutinterruptingreal-timescoringandtosupport
| re-routing. |     | Secondly, | the | rate | of retraining |     | slows |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | ---- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
integrationintoFinTechriskpipelines.
| downtheadaptationtodrift. |     |      |      | Third,thereistypically |     |               |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | ---- | ---- | ---------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no feedback               |     | loop | from | decisions              |     | to downstream |     |     |     |     |     |     |     |     |     |
Themaincontributionsofthisworkareasfollows.
| results | to improve |     | and | evolve | the inference |     | service. |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | ------ | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Furthermore, most supervised methods view risk 1. Software engineering problem formulation for
scoring as a one-step prediction task and do not adaptive risk scoring in FinTech systems. We
157

ICCKJournalofSoftwareEngineering
describeriskevaluationasaproductionsoftware
|           |      |      |         |     |       |             | 2.1 Supervised |     | Learning |     | for | Financial |     | Risk |
| --------- | ---- | ---- | ------- | --- | ----- | ----------- | -------------- | --- | -------- | --- | --- | --------- | --- | ---- |
| component | that | must | operate |     | under | drift while | Modeling       |     |          |     |     |           |     |      |
meeting real-time constraints and continuous Capitalized by their interpretability and ability to
| update | expectations, |     | motivating |     | a   | sequential |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ---------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
easilybeincorporatedintoanexistingscoringservice,
| decision | formulation |     | rather | than | a   | static batch |            |           |     |          |     |              |     |          |
| -------- | ----------- | --- | ------ | ---- | --- | ------------ | ---------- | --------- | --- | -------- | --- | ------------ | --- | -------- |
|          |             |     |        |      |     |              | supervised | pipelines |     | continue |     | to be widely |     | used for |
predictionpipeline. the credit default early warning and risk prediction.
|     |     |     |     |     |     |     | The predictive |     | power |     | is enhanced |     | when | using |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --- | ----------- | --- | ---- | ----- |
2. Deployable adaptive risk scoring architecture macroeconomicandborrowerfeaturesasagradient
|       |               |     |          |     |       |            | boostingdecisiontree[8]. |     |     |     | Suchsolutions,however,are |     |     |     |
| ----- | ------------- | --- | -------- | --- | ----- | ---------- | ------------------------ | --- | --- | --- | ------------------------- | --- | --- | --- |
| using | reinforcement |     | learning |     | based | continuous |                          |     |     |     |                           |     |     |     |
basedoncyclesofredeploymentandofflineretraining
| policy | optimization. |     | We  | propose |     | ARL-CPO, |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
modeling risk scoring as a continuous-action thatmaycausedelaysinupdatewhenthereareregime
MarkovDecisionProcesswithanonline-updated shifts. Likewise,whenconsideringfixeddistributions,
|             |     |        |     |       |        |      | Data-driven |     | machine | learning |     | analysis | of  | systemic |
| ----------- | --- | ------ | --- | ----- | ------ | ---- | ----------- | --- | ------- | -------- | --- | -------- | --- | -------- |
| dual-module |     | policy | and | value | design | that |             |     |         |          |     |          |     |          |
supportsfine-grainedriskscoringandcontinuous risk propagation in financial networks identifies
adaptationinstreamingsettings. key drivers of contagion using classification-based
|              |              |            |     |             |          |         | boundaries | [9].           | However, |             | it      | doesn’t | have          | much   |
| ------------ | ------------ | ---------- | --- | ----------- | -------- | ------- | ---------- | -------------- | -------- | ----------- | ------- | ------- | ------------- | ------ |
|              |              |            |     |             |          |         | mechanisms |                | to keep  | adapting    |         | and can | break         | when   |
| 3. Empirical | evaluation   |            | in  | a streaming |          | FinTech |            |                |          |             |         |         |               |        |
|              |              |            |     |             |          |         | it comes   | to changes     |          | in the      | feature | sets    | distributions |        |
| simulator    | environment. |            |     | We evaluate |          | ARL-CPO |            |                |          |             |         |         |               |        |
|              |              |            |     |             |          |         | if it is   | not retrained. |          | SHAP-based  |         |         | Random        | Forest |
| on credit    | default      | prediction |     | and         | adaptive | asset   |            |                |          |             |         |         |               |        |
|              |              |            |     |             |          |         | models     | are more       |          | transparent |         | and     | explainable   | for    |
allocationusingalarge-scaledatasetof8.5million
|          |             |     |         |             |        |            | regulatory | decision-making |       |      | purposes      |     | [10]. | Despite     |
| -------- | ----------- | --- | ------- | ----------- | ------ | ---------- | ---------- | --------------- | ----- | ---- | ------------- | --- | ----- | ----------- |
| records  | and compare |     | against |             | Random | Forest,    |            |                 |       |      |               |     |       |             |
|          |             |     |         |             |        |            | this, they | are             | still | type | of supervised |     |       | classifiers |
| Gradient | Boosting,   |     | and     | Transformer |        | baselines, |            |                 |       |      |               |     |       |             |
whichneedretrainingtoadjustdecisionboundaries.
reportingclassificationaccuracyof97.4percent,
|       |            |     |      |         |          |     | Bayesian    | neural | models          |     | enhance | the   | capability | of      |
| ----- | ---------- | --- | ---- | ------- | -------- | --- | ----------- | ------ | --------------- | --- | ------- | ----- | ---------- | ------- |
| trend | adaptation |     | rate | of 98.8 | percent, | and |             |        |                 |     |         |       |            |         |
|       |            |     |      |         |          |     | being aware |        | of uncertainty, |     |         | which | may        | help to |
cumulativelong-termperformanceindexof96.1
|     |     |     |     |     |     |     | better determine |     | appropriate |     |     | decision | thresholds |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | --- | --- | -------- | ---------- | --- |
percentintheexperimentalsetting.
|               |     |            |     |              |     |             | and calibrated |     | output         | [11].     | However, |         | uncertainty    |     |
| ------------- | --- | ---------- | --- | ------------ | --- | ----------- | -------------- | --- | -------------- | --------- | -------- | ------- | -------------- | --- |
|               |     |            |     |              |     |             | modelling      | is  | not sufficient |           | to       | give    | an operational |     |
| The remainder | of  | this paper |     | is organized |     | as follows. |                |     |                |           |          |         |                |     |
|               |     |            |     |              |     |             | mechanism      | to  | help           | a running |          | service | continuously   |     |
The related work is discussed in Section 2. The improveand/orupdateitspoliciesinasafeway. These
proposed ARL-CPO method and system design is modelswhendeployedasastatelesspredictionservice
presented in Section 3. Experimental result and areoftentreatedasaheavyweightpipelinethatneeds
discussion are presented in Section 4, followed by tobemanagedforrefreshingthemodels. Disciplined
conclusionsandfuturedirections. testingandreleasecontrolsareneededforproduction
readiness,notjustofflinetesting,includingstructured
evaluationchecklistsandrubricsforreadiness[23].
2 LiteratureReview 2.2 Deep Learning Architectures for Credit
The shift from static, batch-trained predictors to Assessment
services that continuously serve customers requires Thecomplexityoffinancialdataishigh-dimensional
unprecedented software standards such as low and cannot be adequately represented using
latency inference, high throughput, fault tolerant, traditionalapproaches,whiledeeplearningreduces
auditable, and model-safe updates to models in the complexity of the representation learning, but
production[24]. Previousresearchincludesmodeling introduces a higher degree of complexity in serving
forcreditandfraud,sequentialdecisionoptimization and operation. For online credit scoring, transfer
withreinforcementlearning,andarchitecturesforthe learningframeworkswithextremelearningmachines
system-level deployment and streaming. Another enable continuous model adaptation for automated
issueisthatmanyhigh-accuracymodelsarenotbuilt credit assessment without full retraining [12]. In
tobeusedasaproductionservicewithawell-designed reality,itisstillmostlyusedasanadd-ontoamodel
workflow for updates, and built-in monitoring of thatneedsacontrolledretrainingandreleaseprocess.
operationalsystems,whichcauses“hiddentechnical A graph neural network for relational credit risk
debt”inthedeployedMLsystems[22]. models identifies the network effects that are not
158

ICCKJournalofSoftwareEngineering
Table1.Comparativeanalysisofexistingapproaches.
|     |     |     |     |     |     |     |     | Continuous | Sequential | Continuous | Long-Term |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ---------- | --------- | --- | --- | --- |
Ref./Technique Application Adaptation Optimization Actions Reward Personalization
|                            | GradientBoosting[8]       |     |     | CreditDefaultEarlyWarning |                        |     |     | ×   | ×   |     | ×   | ×   | ×        |     |
| -------------------------- | ------------------------- | --- | --- | ------------------------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
| ML-basedNetworkAnalysis[9] |                           |     |     | SystemicRiskPropagation   |                        |     |     | ×   | ×   |     | ×   | ×   | ×        |     |
|                            | XAIRandomForest[10]       |     |     |                           | CreditRiskTransparency |     |     | ×   | ×   |     | ×   | ×   | Partial  |     |
|                            | BayesianNeuralNetwork[11] |     |     |                           | Uncertainty-AwareRisk  |     |     |     |     |     |     |     | (cid:88) |     |
|                            |                           |     |     |                           |                        |     |     | ×   | ×   |     | ×   | ×   |          |     |
TransferLearning/ELM[12] OnlineCreditScoringAdaptation (cid:88)
|     |                        |     |     |                            |                      |     |     | ×       | ×   |     | ×   | ×   |          |     |
| --- | ---------------------- | --- | --- | -------------------------- | -------------------- | --- | --- | ------- | --- | --- | --- | --- | -------- | --- |
|     | GraphNeuralNetwork[13] |     |     |                            | RelationalCreditRisk |     |     | ×       | ×   |     | ×   | ×   | (cid:88) |     |
|     | ExplainableAI[14]      |     |     | InterpretableRiskDetection |                      |     |     | Partial | ×   |     | ×   | ×   | ×        |     |
DQN[15] PairsTrading/DiscreteActionControl (cid:88) (cid:88) × (cid:88) ×
PPO[16] AutomatedMarket-Making (cid:88) (cid:88) (cid:88) (cid:88) ×
TransferRL[17] Cross-MarketStrategyAdaptation (cid:88) (cid:88) (cid:88) (cid:88) Partial
BayesianRL[18] Uncertainty-AwarePolicyLearning (cid:88) (cid:88)
|     |                           |     |     |     |                        |     |     | ×       |     |     | ×   | ×   |     |     |
| --- | ------------------------- | --- | --- | --- | ---------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     | ConceptDriftDetection[19] |     |     |     | FinancialStreamingData |     |     | Partial |     |     |     |     |     |     |
|     |                           |     |     |     |                        |     |     |         | ×   |     | ×   | ×   | ×   |     |
MLOpsFramework[20] ProductionMLDeployment&Monitoring (cid:88) × × × ×
ARL-CPO(Proposed) AdaptiveFinTechRiskEvaluation (cid:88) (cid:88) (cid:88) (cid:88) (cid:88)
captured by tabular models [13]. But they could onlinelearningfromonlineinference,thegovernance
also add an inference latency and an infrastructure ofpolicyupdates,andtheauditabilityofdecisionsin
overhead because of the construction of the graph regulated contexts. Important operational guidance
and neighborhood aggregation. Explainable AI for the production of ML systems is to have explicit
methods in FinTech risk management provide controlsfortesting,rollout,monitoring,androllback
interpretable anomaly and risk signals that must to prevent unwanted changes in behavior of the
be integrated into downstream decision logic [14]. deployedsystems.
However,itoftenyieldsscoresthatmustbehandled
by the downstream system logic, routed to decision 2.4 Real-TimeAdaptiveFrameworksforFinTech
| thresholds |     | and  | reviewed     | by  | humans,   | introducing |     |                              |                |     |                     |     |       |     |
| ---------- | --- | ---- | ------------ | --- | --------- | ----------- | --- | ---------------------------- | -------------- | --- | ------------------- | --- | ----- | --- |
|            |     |      |              |     |           |             |     | Streaming                    | and deployment |     | frameworks          |     | solve | key |
| complexity |     | into | the software |     | pipeline. | Research    |     | in                           |                |     |                     |     |       |     |
|            |     |      |              |     |           |             |     | challengesintheFinTechspace. |                |     | Infinancialstreams, |     |       |     |
software engineering has highlighted the need to theconceptdriftdetectionsystemkeepstrackofthe
makeclearengineeringchoicesaboutdatapipelines, distributionshiftsandselectivelyupdatesmodels[19].
featurestores,reproducibly,andmonitoringtoprevent
Drift-awaremechanismsprovidetemporalrobustness
fragilityasrequirementsevolvewhenbuildinganML
|     |     |     |     |     |     |     |     | but tend | to be "reactive" |     | in that | they | may | have |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------- | ---- | --- | ---- |
basedsystem[25]. periods of poor performance as they retrain and
|     |               |     |          |     |              |     |     | redeploy.  | Standardized  |         | market        | environments |            | and |
| --- | ------------- | --- | -------- | --- | ------------ | --- | --- | ---------- | ------------- | ------- | ------------- | ------------ | ---------- | --- |
|     |               |     |          |     |              |     |     | benchmarks | for financial |         | reinforcement |              | learning,  |     |
| 2.3 | Reinforcement |     | Learning |     | Applications |     | in  |            |               |         |               |              |            |     |
|     |               |     |          |     |              |     |     | such as    | FinRL-Meta,   | provide | reusable      |              | simulation |     |
FinancialSystems
|     |     |     |     |     |     |     |     | infrastructure | that | supports | scalable | evaluation |     | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | -------- | -------- | ---------- | --- | --- |
Reinforcementlearningisabletosolveforsequential
|          |     |        |     |              |     |        |       | adaptive | risk policies | [21]. | They, | however, | do  | not |
| -------- | --- | ------ | --- | ------------ | --- | ------ | ----- | -------- | ------------- | ----- | ----- | -------- | --- | --- |
| decision |     | making | and | long-horizon |     | goals, | which |          |               |       |       |          |     |     |
necessarilyincludesequentialdecisionoptimization
| are       | not | addressed | by            | a prediction-only |              |     | model. |               |        |              |     |        |         |     |
| --------- | --- | --------- | ------------- | ----------------- | ------------ | --- | ------ | ------------- | ------ | ------------ | --- | ------ | ------- | --- |
|           |     |           |               |                   |              |     |        | or continuous | policy | improvement. |     | Recent | studies |     |
| DQN-based |     |           | pairs trading |                   | demonstrates |     | policy |               |        |              |     |        |         |     |
aboutMLOpsalsohighlighttheneedforproduction
| learning |     | through | interaction | with | simulated |     | market |     |     |     |     |     |     |     |
| -------- | --- | ------- | ----------- | ---- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
MLsystemstobemonitored,reproducible,andtohave
environments,thoughitsdiscreteactionformulation
|                                          |     |     |     |     |     |     |          | controlled | release mechanisms |     | to  | avoid | building | up  |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------------------ | --- | --- | ----- | -------- | --- |
| limitsfine-grainedcontinuouscontrol[15]. |     |     |     |     |     |     | Itmaynot |            |                    |     |     |       |          |     |
technicaldebtandreliabilityissues[22].
offerasmuchfine-grainedcontrolascontinuousaction,
duetoitsdiscreteactionformulation. Inthefinancial Table1showsthatanumberofsupervisedtechniques
domain,PPO-basedmarket-makingshowsexcellent have been developed and proved to have good
results for continuous control, and encourages predictive accuracy, however, they generally do
actor-critic style policy optimization [16]. The not continuously adapt and need offline refresh
relevanceofthisisforcross-marketadaptationthatis cycles [8]. Deep models have the ability to learn
usefultoFinTechservicesoperatingacrossregionsand good representations but can be expensive to
marketregimes[17]. Bayesianreinforcementlearning serve and update reliably at scale [13]. When
provides principled uncertainty quantification over appliedtoalways-onFinTechservices,reinforcement
policies, which can improve objective clarity and learningprovidestheabilitytosequentiallyoptimize
support risk-aware decision making [18]. But much and long-horizon objectives, but the question of
workinRLremainspoorly-definedintheisolationof operationalization is often underspecified [16].
159

ICCKJournalofSoftwareEngineering
Figure1.TheARL-CPOPipelineforAdaptiveRiskEvaluationinFinTechSystems.
Streaming and microservice frameworks enhance the dual-network (policy-value) structure enables
deployability and service reliability, but they don’t the agent to converge stably (taking account the
bringonlinedecisionoptimizationtogetherwithsafe market regime changes). ARL-CPO provides better
continuous update workflows [20]. This situation adaptiveness, granularity androbustness in FinTech
encouragesamethodtosolveadaptiveriskevaluation, riskmanagementsoftware,comparedtobothlegacy
whichnotonlyviewsitasalearningproblembutalso static pipelines and discrete-action reinforcement
asanengineeredsystemwithqualitymonitoringtools learningbaselines.
andupdatecontrolmechanisms.
Fromasoftwareengineeringperspective,thetargeted
problemisnotonlypredictiveperformance,butalso
3 ProposedMethod
the design of a risk evaluation service that can (i)
The current FinTech software-based platforms are ingest streaming transactional and behavioral data
evolving at an unprecedented pace with multiple at high throughput, (ii) return a calibrated risk
vectorsofriskthatneedtobeconstantlyandadaptively score with bounded inference latency suitable for
evaluated instruments. The poor scalability of both real-timeuserjourneys,(iii)supportcontinuouspolicy
the static coding models and deterministic rule updates without downtime, and (iv) provide fault
engines have had challenges in non-stationary data toleranceandobservabilityforproductionmonitoring
distribution, high dimensional continuous feature and regulatory audits. In this work, ARL-CPO
space and subtle behavioral patterns of digital is positioned as a deployment-oriented learning
financialusers. Toalleviatethesedisadvantages,this component that can be integrated into a modular
paperproposestheAdaptiveReinforcementLearning FinTechriskpipeline,whereonlinelearningisisolated
with Continuous Policy Optimization (ARL-CPO) from the inference path to prevent update-induced
framework, a learning-based framework, that aims service instability, while decision logs and model
to reshape the risk evaluation as a Continuous versions are preserved for compliance and post-hoc
Markov Decision Process (MDP) with Continuous investigation.
Action Space and Continuous State Space. The
ARL-CPOagentlearnsthebestrisk-mitigationpolicies The provided architecture is a closed-loop pipeline
withouttheneedtohavehand-writtenrules. Reward of adaptive risk assessment of the FinTech software
formulation in the agent is loss sensitive, while systems. The financial data simulation layer is fed
160

ICCKJournalofSoftwareEngineering
streamingmarketindicatorsandcustomerbehavioral recordedwithamodelversionidentifier,atimestamp
telemetrythatreflectreal-timeoperatingconditions. and request info to enable traceability, auditability,
Thestateencoderthentransformstherawinputsinto operational debugging. This allows for proposed
asmallobservationvectorwhichisthenprocessedby learningcomponenttobeinsertedintocurrentFinTech
the ARL-CPO Decision Engine comprising a policy softwaresystemswithoutbusinessdecisionlogicbeing
network and a value approximation network. The integratedintolearningloop.
enginecreatescontinuousriskscoresthatcanbeused
to make decisions regarding the eligibility of credit
and the actions necessary to rebalance the portfolio. Γ(t−1) = F(o,θ)−H(ξ) subjectto V > L(t−g)
Theflowoftherewardsignaliscalculatedbasedon (1)
theattainedmonetaryresultsandthisisflowedback
All symbols in Eq. (1) are defined as follows.
tocorrectthepolicyoftheagentinaniterativemanner.
Γ(t − 1) is the performance signal at time step (t −
This closed loop design guarantees personalization,
1), the current observation (state representation)
flexibility and state of the art accuracy in volatile
is o, and the current set of policy parameters is
financialecosystems,whichisillustratedinFigure1.
θ. The observation and policy parameters are
The MDP formulation is selected to align with
denoted as provided by the function F(o,θ), which
is an uncertainty-related scoring function, like a
deployed FinTech risk services where decisions
confidence-aware scoring function, or an entropy
are repeated over time and outcomes (defaults,
chargebacks, losses, missed opportunities) arrive proxy. ξ denotes a vector of threat indicators or
with delay. Continuous actions are necessary drift-sensitivesignalsextractedfromthestream. H(ξ)
represents the uncertainty/entropy of the threat
becauseproductionrisksystemscommonlyrequirea
real-valuedscorethatcanbecalibrated,thresholded, indications. V is a form of confidence (such as a
validityscorefromacalibrationlayerorcriticestimate).
and composed with downstream rules, rather than
The lower bound on acceptable confidence is called
a coarse discrete label. In ARL-CPO, the action
is therefore treated as a continuous score in a
L(t−g)andg isalagparameterthatdeterminesthe
bounded interval (e.g., [0,1]) which can be mapped window of assessment. The constraint V > L(t −
tooperationallabels(Low/Moderate/Elevated)only g) ensures that risk actions are only accepted if the
minimumconfidencerequirementisfulfilled,relevant
atthebusiness-rulelayer. Thisseparationpreservesa
forsafedeploymentunderdistributionalshift.
stableAPIcontract(continuousscoreoutput)while
allowingproductteamstoadjustthresholdswithout
retrainingthepolicy.
(cid:0) (cid:1)
Ψ = {q }(u,ξ) := λ(ξ−d)+Ω(λ −C {t−1})
r−1 k r
Algorithm1evaluatestheinstantaneousriskpostureof ·Ω {d−1}
u
afinancialentityormarketconditionusingthetrained (2)
ARL-CPOagent. Theprocessstartswiththemarket
Eq. (2)isaplaindefinitionofanadjustedperformance
feature vectors and user activity metrics combined
tensor for adaptation control, u is a normalized
to one observation o t . This observation is mapped adaptation index (such as an intensity factor for
to a scalar action a t = the estimated risk magnitude updates), ξ represents drift or threat indicators, λ
bythepolicynetwork(continuousactiongenerator)
is a scaling factor for sensitivity to drift, d is a
whichmapsthisobservationtoascalaractiona. The
referencedriftbaseline(ordetectionthreshold),and
algorithm uses a value from 0 to 2 to represent a t , Ω is a temporal normalization operator. λ is a
k
with0beingMinimal,1beingModerate,and2being
reference performance level (or metric). Ω {d −
u
Elevated. Asthescoringmechanismisupdatedineach
1} is a normalization term that adjusts updates
observation, the scoring mechanism automatically
based on the evaluation window. C {t − 1} is the
r
adapts to behavioral drift, thus enabling individual
observedperformanceorcorrectiontermattime(t−
creditadjudicationandassetallocationsoptimization.
1). Operationally, Eq. (2) is used to modulate how
strongly the agent corrects internal estimates when
In a real deployment, Algorithm 1 can be the
behavioralpatternsshift,whichsupportsstableonline
inference path of a risk scoring microservice. The
operation.
service is exposed and should take the encoded
observation (or state) in as an argument and return Figure 2 depicts the ARL-CPO architecture that
the continuous score right away. Every answer is consists of two collaborating modules: a Policy
161

ICCKJournalofSoftwareEngineering
Figure2.ARL-CPODual-ModuleArchitecturewithGradient-BasedPolicyRefinement.
Learning Module and a Value Estimation Module. The Algorithm 2 will be used to guide the iterative
The observation vector o is received by the Policy processofrefiningthepolicyoftheARL-CPOagent
t
Learning Module which generates a continuous using outcome-driven feedback. Once an agent
risk-control action using the policy network and performs an action and sees the change in the
injects controlled perturbation to explore. The environment, a scalar reward is calculated. This
Value Estimation Module stores transition tuples in rewardiscomparedwithaperformancebaselinebythe
a memory bank, approximates expected cumulative algorithm. Whentherewardisatorbelowthebase,the
reward via the value approximation network and existingpolicyparametersaremaintainedwithsome
stabilizestrainingusingatargetsynchronizationunit. stabilizationupdatestoavoidoverfitting. Otherwise,
Thepolicyrefinementprocessviagradientsisaflow theweightsofthepolicynetworkarecorrectedwith
directed by the value module to the policy network, thehelpofgradient-basedcorrectionsinsuchaway
making it possible to continuously improve the thatsuboptimaldecisionsarepenalized. Theresulting
policy. Thismodularseparationisstable-convergent feedbackloopallowstheARL-CPOagenttoobserve
andisespeciallyapplicabletothehigh-dimensional, non-stationary financial dynamics and aid resilient
continuous-controlrequirementsofreal-timefinancial andinformedriskgovernance.
riskmanagement.
|           |             |                |     |          |            | For      | reproducibility |            |     | and deployment |          | realism, | the         |
| --------- | ----------- | -------------- | --- | -------- | ---------- | -------- | --------------- | ---------- | --- | -------------- | -------- | -------- | ----------- |
|           |             |                |     |          |            | reward   | signal          | should     |     | be implemented |          | as       | an explicit |
| While the | dual-module | (policy-value) |     |          | separation |          |                 |            |     |                |          |          |             |
|           |             |                |     |          |            | function | of              | observable |     | business       | outcomes |          | and risk    |
| resembles | the general | actor-critic   |     | concept, |            | the      |                 |            |     |                |          |          |             |
objectives,suchasrealizedloss,default/fraudevents,
software-levelcontributioninARL-CPOistheupdate
|     |     |     |     |     |     | and | risk-adjusted |     | return | measures |     | computed | over a |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | -------- | --- | -------- | ------ |
andsynchronizationpatternforcontinuousoperation.
|     |     |     |     |     |     | defined | horizon. |     | In  | a production |     | system, | reward |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --- | ------------ | --- | ------- | ------ |
Theinferenceserviceusesafixed,versionedsnapshot
|        |                       |     |             |     |          | computation |     | is  | typically | delayed |     | and | arrives via |
| ------ | --------------------- | --- | ----------- | --- | -------- | ----------- | --- | --- | --------- | ------- | --- | --- | ----------- |
| of the | policy for consistent |     | low-latency |     | scoring, |             |     |     |           |         |     |     |             |
asynchronousoutcomeevents;therefore,thesystem
| while the                          | learning | module | updates |             | parameters |        |               |         |        |          |              |     |          |
| ---------------------------------- | -------- | ------ | ------- | ----------- | ---------- | ------ | ------------- | ------- | ------ | -------- | ------------ | --- | -------- |
|                                    |          |        |         |             |            | logs   | (observation, |         | score, | decision | context,     |     | outcome) |
| asynchronouslyonstreamingfeedback. |          |        |         | Thepolicies |            |        |               |         |        |          |              |     |          |
|                                    |          |        |         |             |            | tuples | to            | compute |        | rewards  | consistently |     | and to   |
areupdatedviaacontrolledrolloutprocess,suchasa
|     |     |     |     |     |     | enable | audit | trails. | This | also | supports |     | compliance |
| --- | --- | --- | --- | --- | --- | ------ | ----- | ------- | ---- | ---- | -------- | --- | ---------- |
shadowevaluation,canaryrelease,orstagedrollout,
|                                            |     |     |     |     |     | requirements |     | by         | retaining |       | evidence | of      | how each |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --------- | ----- | -------- | ------- | -------- |
| toensurethattherearenounsafepolicychanges. |     |     |     |     |     | This         |     |            |           |       |          |         |          |
|                                            |     |     |     |     |     | decision     | was | generated, |           | which | model    | version | was      |
designalsoensuresthatthereisno“training-induced
|            |               |     |         |             |     | used, | and | what | outcome | feedback |     | triggered | future |
| ---------- | ------------- | --- | ------- | ----------- | --- | ----- | --- | ---- | ------- | -------- | --- | --------- | ------ |
| downtime,” | and it allows |     | for the | possibility |     | of    |     |      |         |          |     |           |        |
policyupdates.
| reverting | back to a previous   |     | stable | version     | of  | the |     |     |     |     |     |     |     |
| --------- | -------------------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model,    | while also providing |     | the    | opportunity |     | to  |     |     |     |     |     |     |     |
)foru
|                                                 |     |     |     |     |     | tV  | ≡ Λ ∗(Φ |       | ) → (t−1) | ≤   | Jλ|c−(β−η |     | ≡ ∇ |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ----- | --------- | --- | --------- | --- | --- |
| continuouslyimprovepolicieswithoutdisruptingthe |     |     |     |     |     |     | 1       | {t−1} |           |     |           | r   |     |
(3)
| serving    | path, a requirement |     | for production |     | FinTech |     |                          |     |     |     |                    |     |     |
| ---------- | ------------------- | --- | -------------- | --- | ------- | --- | ------------------------ | --- | --- | --- | ------------------ | --- | --- |
| platforms. |                     |     |                |     |         | Eq. | (3)isclarifiedasfollows. |     |     |     | denotesanaggregate |     |     |
tV
162

ICCKJournalofSoftwareEngineering
qualityindexattimet. Λ denotesascalingconstant modelregistry,rollout/rollback),ratherthanonlythe
1
for quality aggregation. The feature vector at the learningflow.
previous step is denoted as Φ (e.g., reward
{t−1} Figure 3 illustrates how the ARL-CPO decision
statisticsfrompreviousstepsorstabilityindicators).
engine can be embedded into a production-grade
The baseline time index (t − 1) is used to compare
FinTech risk evaluation pipeline as an always-on
itscurrentperformancewithrecenthistory. Jλ|cisa
software service. The client applications use the
compositeobjectivetermcomposedofariskpenalty
API Gateway to make calls to the risk scoring
adjustment, η , a base performance measure, β, and
r capability, which then forwards to the Risk Scoring
aconstrainttolimittheupdates,c. Foroperation,Eq.
Service(inferencemicroservice)thatloadsaversioned
(3)isappliedtomonitorthetrade-offbetweenservice
stabilityandproactiveriskgovernanceindrift.
policysnapshotπθ(v
k
)andreturnsacontinuousrisk
score that has a short latency. At the same time,
external market indicators and transaction or user
signals are continuously ingested into the system
(cid:107)Λ(u,ω )(cid:107) = D (χ−λ )+G (τ,ρ ) := δ(u−ρ ) ≥ ∇ via streaming. Meanwhile, market indicators and
r ξ b ω k w
(4) transactionorusersignalsarecontinuouslyingested
from the outside world and transformed by the
Eq. (4)isclarifiedasfollows,thenorm(cid:107)Λ(u,ω )(cid:107)isa
r Feature/State Builder into the state representation
measureoftheadaptationperformanceofthesystem
(s /o ) that is utilized for inference and learning.
withupdateintensityuandarisk-weightparameterω . t t
r Manydownstreamplatformservices(defaults,fraud
ThedriftsensitivetermD (χ−λ )isaterminvolving
ξ b confirmations,realizedloss/return)triggeroutcome
observed behavioral shift statistics, λ is a baseline
b events, which are fed to the Outcome and Reward
drifttolerance,andξ isthedriftindicatorspace. The
Service to calculate r , and to create training tuples
stabilitytermisdenotedasG (τ,ρ ),withτ beingan t
ω k (s ,a ,r ,s {t + 1}). These tuples then go into
update/synchronizationrateandρ beingaparameter t t t t
k an Online Learning Service that updates the actor
of performance boundary. An update intensity u is
and critic, asynchronously, and stores the updated
compared with a control boundary, ρ , denoted as
w policies in a Model Registry. A controlled canary or
δ(u − ρ ). The ≥ ∇ condition represents satisfying
w shadowrolloutloophelpsensuresafe,downtime-free
allconfigthresholds. Indeployment,thesequantities
updatesthroughpromotingnewmodelversionsafter
correspondtomonitoringsignalsandguardrails(for
validation, and the Audit/Compliance storage and
example,update-ratecapsanddriftthresholds)that
Monitoring/Observabilityprovidelogs,metrics,traces,
preventunstablebehaviorunderhighloadorsudden
driftsignalsandalertstomeetoperationalreliability
marketregimechanges.
and regulatory traceability requirements. The
The ARL-CPO model is based on the concept of proposedmethodologyisbasedoncontinuous-action
reward-based continuous policy optimization to reinforcementlearningandusesadeployment-aware
reduce financial risks in real-time. The architecture softwarearchitectureasameanstoseparateinference
demonstrateshowtheadaptivereinforcementlearning fromtraining,tohandleversioneddeploymentandto
canbeappliedtosupportFinTechsoftwaresystemsin providemonitoringandcompliancelogging. Thatis
offeringflexiblecreditdecisionsanddynamicportfolio themethodologyforARL-CPOasanadaptivelearning
management. This continuous-action control that framework as well as a practical component of the
is enabled by the dual policy-value structure and FinTechsoftwaresystem.
thegradient-basedrefinementisespeciallyusefulin
complexfinancialsituations,wherefine-grainedrisk
4 ResultsandDiscussions
adjustmentsareneeded.
This section entails the experimental analysis of the
To make the proposed framework software offered ARL-CPO framework implemented to the
engineering more explained, an explicit integration adaptiveriskassessmentinFinTechsoftwaresystems.
diagram is shown in Figure 3 that explains how It contrasts its framework to three frameworks that
ARL-CPO connects to platform components such are already in use: Random Forest (RF), Gradient
as API gateways, message queues, databases, and Boosting(GB),andTransformer-basedmodels(TFM)
monitoring tools. This diagram complements for credit default prediction and dynamic asset
Figures1and2byfocusingondeployability,system allocation problems. The evaluation validates that
boundaries,andoperationalcontrolpoints(logging, continuous optimization policy is more accurate,
163

ICCKJournalofSoftwareEngineering
Figure3.ARL-CPOIntegrationintoaProductionFinTechRiskSystem.
reactive and stable over time than other policy Table2.Experimentalconfiguration.
optimization policies with single or batch trained Parameter Description/Value
policies. Environment / FinTechadaptiveriskscoringusingstreaming
|                                         |     |     |     |     |     |     |     |     | Task        | marketandtransactionaldata                    |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------------------------------------- | --- | --- | --- |
|                                         |     |     |     |     |     |     |     |     | StateSpace  | Marketindicators,behavioralrisksignals,credit |     |     |     |
| 4.1 DatasetandExperimentalConfiguration |     |     |     |     |     |     |     |     |             | utilizationmetrics                            |     |     |     |
|                                         |     |     |     |     |     |     |     |     | ActionSpace | Continuousriskscoreadjustment∈[0,2]           |     |     |     |
Theseexperimentsmakeuseofalarge-scalefinancial
|     |     |     |     |     |     |     |     |     | Policy Network | 3 hidden layers | with 512, | 384, and | 256 units, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------------- | --------- | -------- | ---------- |
datasetof8.5millionrecordsthathavebeengenerated Architecture LeakyReLUactivations
using advanced generative modeling methods, and Value Network 3 hidden layers with 512, 384, and 256 units,
|          |                |     |           |           |     |                |     |     | Architecture  | LeakyReLUactivations |     |     |     |
| -------- | -------------- | --- | --------- | --------- | --- | -------------- | --- | --- | ------------- | -------------------- | --- | --- | --- |
| which    | are regulatory |     | compliant |           | and | distributional |     |     |               |                      |     |     |     |
|          |                |     |           |           |     |                |     |     | Learning Rate | 0.0005               |     |     |     |
| faithful | to real-world  |     |           | financial |     | patterns.      |     | The |               |                      |     |     |     |
(Policy)
data includes the customer demographics profiles, Learning Rate 0.0008
| multi-channeltransactionshistory,creditapplication |             |     |           |     |         |     |              |     | (Value)         |      |     |     |     |
| -------------------------------------------------- | ----------- | --- | --------- | --- | ------- | --- | ------------ | --- | --------------- | ---- | --- | --- | --- |
|                                                    |             |     |           |     |         |     |              |     | Discount Factor | 0.98 |     |     |     |
| record                                             | and account |     | lifecycle |     | events. | It  | is extensive |     |                 |      |     |     |     |
(γ)
andheterogeneousand,therefore,ishighlytailoredto Transition 1,500,000tuples
theevaluationofadaptivelearningsystems,financial MemoryCapacity
|             |          |     |        |            |     |              |     |     | Mini-batchSize   | 128            |            |         |            |
| ----------- | -------- | --- | ------ | ---------- | --- | ------------ | --- | --- | ---------------- | -------------- | ---------- | ------- | ---------- |
| forecasting | modules, |     | and    | behavioral |     | segmentation |     |     |                  |                |            |         |            |
|             |          |     |        |            |     |              |     |     | Exploration      | Gaussian noise | injection, | σ=0.18, | decay rate |
| pipelines.  | Table    |     | 2 will | give       | a   | summary      | of  | the | Strategy         | 0.995          |            |         |            |
|             |          |     |        |            |     |              |     |     | TrainingEpisodes | 350episodes    |            |         |            |
experimentaldesign.
|     |     |     |     |     |     |     |     |     | Max Steps per | 250steps |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | --- | --- |
Episode
4.2 PredictionAccuracyAnalysis RewardFunction Negative expected shortfall combined with
risk-adjustedreturn
| The precision  |         | of prediction |         | of            | all the    | four         | methods   |     |                |                                  |        |        |        |
| -------------- | ------- | ------------- | ------- | ------------- | ---------- | ------------ | --------- | --- | -------------- | -------------------------------- | ------ | ------ | ------ |
|                |         |               |         |               |            |              |           |     | Target Network | Softupdateparameterτ=0.003       |        |        |        |
| at progressive |         | levels        |         | of evaluation |            |              | are shown |     | SyncRate       |                                  |        |        |        |
|                |         |               |         |               |            |              |           |     | Hardware       | AMDEPYC7742CPU;NVIDIAA10080GBGPU |        |        |        |
| in Figure      | 4.      | The           | maximum |               | prediction |              | accuracy  |     |                |                                  |        |        |        |
|                |         |               |         |               |            |              |           |     | Software       | PyTorch framework,               | Ubuntu | 22.04; | custom |
| of the         | ARL-CPO |               | system, | based         |            | on precision |           | is  |                |                                  |        |        |        |
FinTechenvironmentsimulator
| 97.4%        | that is        | much     | higher |                | than            | all the | baselines. |       |     |     |     |     |     |
| ------------ | -------------- | -------- | ------ | -------------- | --------------- | ------- | ---------- | ----- | --- | --- | --- | --- | --- |
| This primacy |                | is based |        | on the         | ability         | of      | the        | agent |     |     |     |     |     |
| to keep      | evolving       |          | its    | internal       | representations |         |            | in    |     |     |     |     |     |
| response     | to interaction |          | with   | non-stationary |                 |         | streams    |       |     |     |     |     |     |
of financial data. The ARL-CPO agent also takes plateaus over time, whereas ARL-CPO continues
advantageofeachpredictionasanelementinalong improving through its reward-based adaptation
sequence of decisions, gradually learning complex mechanism. The continuous action formulation
nonlinear relationships between user behavior and also allows fine-grained, context-sensitive risk
market dynamics. The Transformer baseline shows quantification as opposed to coarse categorical
competitive performance at shorter intervals but assignments.
164

ICCKJournalofSoftwareEngineering
|     |     |     |     |     | percent | cumulative |     | performance |     | index | is evidence |     |
| --- | --- | --- | --- | --- | ------- | ---------- | --- | ----------- | --- | ----- | ----------- | --- |
thatthealgorithmiscapableofoptimizingsustained
|     |     |     |     |     | performance |      | as opposed |      | to         | greedy | short-horizon |      |
| --- | --- | --- | --- | --- | ----------- | ---- | ---------- | ---- | ---------- | ------ | ------------- | ---- |
|     |     |     |     |     | returns.    | When | the        | risk | assessment | is     | defined       | as a |
sequenceofoptimizationproblemsinwhichthefuture
|     |     |     |     |     | rewardisdiscounted(γ |     |           |     | =0.98)andthefutureriskis |           |     |       |
| --- | --- | --- | --- | --- | -------------------- | --- | --------- | --- | ------------------------ | --------- | --- | ----- |
|     |     |     |     |     | considered           | to  | determine |     | the best                 | strategy, | the | agent |
learnsstrategiesthattradetheimmediatereductionof
|     |     |     |     |     | riskwiththelong-termhealthoftheportfolio. |     |     |     |     |     |     | Thisis |
| --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | ------ |
echoedinthereducedlevelsofdefaultincreditrating
andmorepredictableriskadjustedreturnsintheasset
Figure4.ComparisonofAccuracyofPredictionacross
|     |     |     |     |     | allocation. | Theareaundercurvecomparisonclearly |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
EvaluationIntervals.
|     |     |     |     |     | shows       | that ARL-CPO |             |     | is continuing | to   | increase  | the |
| --- | --- | --- | --- | --- | ----------- | ------------ | ----------- | --- | ------------- | ---- | --------- | --- |
|     |     |     |     |     | gap between |              | performance |     | compared      | with | baselines |     |
4.3 TrendAdaptationRateAnalysis as training continues: RF plateaus at 55.4%, GB
The rate of trend adaptation that was plotted in levels off at 63.2% and TFM levels off at 74.8%. It
Figure5,quantifiestheresponsivenessofeachmethod is discovered that the policy refinement mechanism
to distributional changes in financial behavior and has compounding advantages with longer training
marketregimes. TheadaptationrateofARL-CPOis horizons,whichisafeatureneededinFinTechsystems
98.8% which confirms that it is the most responsive wherelong-termriskgovernancedefinestheviability
amongallbaselines. Conventionalalgorithmshavea oftheplatform.
| highlatencyindetectingnewpatterns:          |        |              | RFconverges |       |     |     |     |     |     |     |     |     |
| ------------------------------------------- | ------ | ------------ | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| on about                                    | 48.1%, | GB converges | on about    | 58.6% | and |     |     |     |     |     |     |     |
| TFMconvergesonabout72.4%atthelastiteration. |        |              |             |       | The |     |     |     |     |     |     |     |
ARL-CPOagentupdatesitspolicyparametersateach
interactioncycle,andthusdoesnothavetheretraining
| bottleneckatall. |     | Thedual-modulearchitecturewith |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theseparationofpolicylearningandvalueestimation
| enables the | stable | and rapid | convergence | without |     |     |     |     |     |     |     |     |
| ----------- | ------ | --------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
catastrophicforgetting,andtheabilitytoaccommodate
| new distributional |     | information. | Such a | property | is  |     |     |     |     |     |     |     |
| ------------------ | --- | ------------ | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
absolutelyessentialonFinTechplatformswhereuser
behaviorandregulatoryenvironmentsmaychangeat
Figure6.CumulativeLong-TermPerformanceIndexover
anytime.
TrainingEpochs.
|     |     |     |     |     | Table 3      | summarizes       |               | the          | quantitative  |           | results       | of all   |
| --- | --- | --- | --- | --- | ------------ | ---------------- | ------------- | ------------ | ------------- | --------- | ------------- | -------- |
|     |     |     |     |     | the three    | evaluation       |               | dimensions.  |               | The       | ARL-CPO       |          |
|     |     |     |     |     | framework    |                  | outperforms   |              | the           | strongest |               | baseline |
|     |     |     |     |     | (TFM)        | by 18.9%,        |               | 26.4%,       | and           | 21.3%     | in prediction |          |
|     |     |     |     |     | accuracy,    | trend            |               | adaptation   |               | rate, and | long-term     |          |
|     |     |     |     |     | performance, |                  | respectively. |              |               | Such      | gains         | can be   |
|     |     |     |     |     | attributed   |                  | to three      |              | architectural |           | benefits      | (1)      |
|     |     |     |     |     | continuous   |                  | policy        | optimization |               | mechanism |               | that     |
|     |     |     |     |     | removes      | batch-retraining |               |              | latency       | (2)       | dual-module   |          |
Figure5.TrendAdaptationRateAcrossTestIterations. separation that allows stable convergence under
|     |     |     |     |     | distributional |     | shift | (3)  | reward-based |               | sequential |      |
| --- | --- | --- | --- | --- | -------------- | --- | ----- | ---- | ------------ | ------------- | ---------- | ---- |
|     |     |     |     |     | formulation    |     | that  | must | focus        | on cumulative |            | risk |
4.4 Long-TermCumulativePerformanceAnalysis reduction rather than myopic predictions. Overall,
Figure 6 illustrates the cumulative performance these findings support ARL-CPO as a resoundingly
index of all the methods after 300 training epochs. better solution to adaptive risk evaluation within
The fact that ARL-CPO is able to achieve 96.1 modernFinTechsoftwaresolutions.
165

ICCKJournalofSoftwareEngineering
Table3.ComparativeperformanceanalysisofARL-CPOagainstbaselinemethods.
|     |     |     |     |     |     | Prediction | TrendAdaptation |     |     |     | CumulativeLong-Term |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
Method
|     |                      |                  |     |     | Accuracy(%) |      |     | Rate(%) |      |     | Performance(%) |      |     |     |     |
| --- | -------------------- | ---------------- | --- | --- | ----------- | ---- | --- | ------- | ---- | --- | -------------- | ---- | --- | --- | --- |
|     | RandomForest(RF)     |                  |     |     |             | 62.3 |     |         | 48.1 |     |                | 55.4 |     |     |     |
|     | GradientBoosting(GB) |                  |     |     |             | 71.2 |     |         | 58.6 |     |                | 63.2 |     |     |     |
|     |                      | Transformer(TFM) |     |     |             | 78.5 |     |         | 72.4 |     |                | 74.8 |     |     |     |
|     | ARL-CPO(Proposed)    |                  |     |     |             | 97.4 |     |         | 98.8 |     |                | 96.1 |     |     |     |
Table4.Softwaresystemperformanceevaluation(deployment-orientedmetrics).
ARL-CPO
| Metric |     |     |     |     |     |     |     |     |     | RF  |     | GB  |     | TFM |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Proposed)
Inferencelatency(ms/request),p50/p95 7.6/18.4 2.1/4.8 3.4/7.2 19.8/46.5
| Throughput(requests/second) |     |     |     |     |     |     | 5,200 |     | 18,500  |     |     | 12,400  |     | 1,950 |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | ------- | --- | ----- | --- |
| Peakmemoryusage(GB)         |     |     |     |     |     |     | 3.2   |     |         | 1.1 |     | 1.6     |     | 6.8   |     |
| CPUutilization(%)atpeakload |     |     |     |     |     |     | 42    |     |         | 68  |     | 71      |     | 38    |     |
| GPUutilization(%)atpeakload |     |     |     |     |     |     | 31    |     | Notused |     |     | Notused |     | 44    |     |
Modelupdatetime(sec/update) 2.7 Notapplicable Notapplicable 9.4
Table 4 reports the deployment-oriented software dual-modulegradient-basedrefinement,andreal-time
performancemetrics(inferencelatency,throughput, adaptivelearninginasinglearchitecturespecifically
resource utilization, and model update time), designed to govern financial risk. Simultaneously
demonstratingthatARL-CPOcansupportreal-time achieving 97.4% prediction accuracy, 98.8% trend
risk scoring while maintaining practical online adaptation rate, and 96.1% cumulative long-term
updateoverheadinaproduction-likeFinTechservice performance—outperformingthestrongestbaseline
environment. Each method was tested 10 times bymarginsover18percent—demonstratesthatrisk
independently with different random seed, and the assessmentformulatedasacontinuous-actionMarkov
results are presented as mean ± SD. Using the run Decision Process with loss-sensitive reward signals
distribution,95%confidenceintervalswerecomputed yields fundamentally superior decision intelligence
for all three primary metrics for Figures 4, 5 and thanprediction-onlyparadigms. Thecombinationof
6; statistical significance testing using the strongest granularcontinuousscoring,real-timeenvironmental
baseline (TFM) confirmed the improvements of control and long-horizon reward maximization in a
ARL-CPO are statistically significant (p < 0.01) for singleFinTechriskassessmentpipelinedoesnotexist
all three primary metrics. To prevent exploiting inpriorworkwithinthereviewedliterature.
onlineupdates,anextraonlinebaseline(incremental
fine-tuningoftheTransformeratfixedupdateperiods
5 Conclusion
| with a | sliding  | window) |            | was  | additionally |     | tested,  |           |         |             |     |             |         |            |       |
| ------ | -------- | ------- | ---------- | ---- | ------------ | --- | -------- | --------- | ------- | ----------- | --- | ----------- | ------- | ---------- | ----- |
|        |          |         |            |      |              |     |          | This      | article | proposes    |     | an adaptive | risk    | assessment |       |
| which  | was more |         | responsive | than | the          | TFM | offline, |           |         |             |     |             |         |            |       |
|        |          |         |            |      |              |     |          | framework |         | for FinTech |     | software    | systems |            | using |
butnotaswellasARL-CPOonbothadaptationand
reinforcement-basedcontinuouspolicyoptimization
| long-horizonperformance. |               |     |     | Thetrendadaptationrate |     |               |     |             |     |              |     |               |      |             |        |
| ------------------------ | ------------- | --- | --- | ---------------------- | --- | ------------- | --- | ----------- | --- | ------------ | --- | ------------- | ---- | ----------- | ------ |
|                          |               |     |     |                        |     |               |     | through     | the | ARL-CPO      |     | architecture. |      |             | Beyond |
| (98.8%)                  | is calculated |     | as  | the percentage         |     | of post-drift |     |             |     |              |     |               |      |             |        |
|                          |               |     |     |                        |     |               |     | algorithmic |     | performance, |     | the           | work | contributes | a      |
testiterationsinwhichthemethodisrecoveredwithin
|     |     |     |     |     |     |     |     | deployment-oriented |     |     | design | view | of  | adaptive | risk |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------ | ---- | --- | -------- | ---- |
apredeterminedrecoverytimewindow,towithin2%
scoringasanalways-onsoftwareservice,emphasizing
| ofthepre-driftlevel.  |        |          | Inadditiontopredictivemetrics, |                 |     |             |     |            |     |           |         |         |             |              |     |
| --------------------- | ------ | -------- | ------------------------------ | --------------- | --- | ----------- | --- | ---------- | --- | --------- | ------- | ------- | ----------- | ------------ | --- |
|                       |        |          |                                |                 |     |             |     | continuous |     | online    | updates | without |             | interrupting |     |
| a deployment-oriented |        |          |                                | evaluation      | was | performed   |     |            |     |           |         |         |             |              |     |
|                       |        |          |                                |                 |     |             |     | inference, |     | versioned |         | model   | management, |              | and |
| on the                | stated | hardware |                                | to characterize |     | operational |     |            |     |           |         |         |             |              |     |
operationalmonitoringforreliabilityandauditability.
feasibilityinreal-timeFinTechservices.
Unlikemodelsthataretrainedinbatches(likeRandom
The results of the experiment clearly prove the Forest, Gradient Boosting and Transformer-based
originalityandexcellenceoftheproposedARL-CPO models), ARL-CPO continually adapts its decision
frameworkincomparisonwiththecurrentonesinthe policy based on the changing financial behaviors,
sphereofFinTechriskassessment. ARL-CPOisthefirst market regimes and user activity patterns. The
framework to unify continuous policy optimization, empiricaltestingofthecreditdefaultpredictionand
166

ICCKJournalofSoftwareEngineering
| the asset | allocation |     | with | trend adaptation |     | tasks | in  |     |     |     |     |     |     |
| --------- | ---------- | --- | ---- | ---------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
AIUseStatement
| a large-scale |     | synthetic | FinTech | environment |     |     | yields |     |     |     |     |     |     |
| ------------- | --- | --------- | ------- | ----------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
TheauthordeclaresthatnogenerativeAIwasusedin
| a predictive |     | accuracy | of 97.4%, | trend | adaptation |     | of  |     |     |     |     |     |     |
| ------------ | --- | -------- | --------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
thepreparationofthismanuscript.
98.8%,andcumulativelong-termperformanceindex
| of 96.1%. | Moreover, |     | it provides |     | inference | latency, |     |     |     |     |     |     |     |
| --------- | --------- | --- | ----------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
throughput, resource utilization, and online update EthicalApprovalandConsenttoParticipate
timeatthesystemlevel,whichhelpsindemonstrating
Notapplicable.
| the practical |     | feasibility | of  | ARL-CPO | for | real-time |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
FinTechriskpipelines.
References
| These          | findings | are | encouraging, |     | but       | the | study |              |          |            |     |                     |     |
| -------------- | -------- | --- | ------------ | --- | --------- | --- | ----- | ------------ | -------- | ---------- | --- | ------------------- | --- |
|                |          |     |              |     |           |     |       | [1] Mashrur, | A., Luo, | W., Zaidi, | N.  | A., & Robles-Kelly, |     |
| is constrained |          | by  | the use      | of  | a dataset |     | and a |              |          |            |     |                     |     |
simulatedenvironment;andoperationalconstraints, A. (2020). Machine learning for financial risk
|     |     |     |     |     |     |     |     | management: | asurvey.IEEEAccess,8,203203-203223. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------------------------- | --- | --- | --- | --- |
feedbackdelays,andcompliancerequirementsinreal
[CrossRef]
| deploymentsmayvarysignificantly. |     |     |     |     | So,anyreference |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
to real-world generalization must be understood [2] Lu,J.,Liu,A.,Dong,F.,Gu,F.,Gama,J.,&Zhang,G.
|        |      |         |          |         |     |        |     | (2018).Learningunderconceptdrift: |     |     |     | Areview.IEEE |     |
| ------ | ---- | ------- | -------- | ------- | --- | ------ | --- | --------------------------------- | --- | --- | --- | ------------ | --- |
| within | this | context | and more | testing | is  | needed | on  |                                   |     |     |     |              |     |
transactionsonknowledgeanddataengineering,31(12),
publicorproductiondatasets.
2346-2363.[CrossRef]
Future research will be based on production grade [3] Climent, F., Momparler, A., & Carmona, P. (2019).
|          |             |     |          |     |           |            |     | Anticipating | bank | distress | in  | the Eurozone: | An  |
| -------- | ----------- | --- | -------- | --- | --------- | ---------- | --- | ------------ | ---- | -------- | --- | ------------- | --- |
| software | engineering |     | problems |     | that will | facilitate |     |              |      |          |     |               |     |
safe continuous learning in regulated FinTech extremegradientboostingapproach.Journalofbusiness
research,101,885-896.[CrossRef]
| settings. | This | includes | model | versioning, |     | lineage |     |           |           |                    |     |             |     |
| --------- | ---- | -------- | ----- | ----------- | --- | ------- | --- | --------- | --------- | ------------------ | --- | ----------- | --- |
|           |      |          |       |             |     |         |     | [4] Zeng, | Z., Kaur, | R., Siddagangappa, |     | S., Rahimi, | S., |
tracking,controlledA/Btestingandcanaryrollouts,
|           |          |     |             |       |            |     |     | Balch, | T., &Veloso, | M.(2023).Financialtimeseries |     |     |     |
| --------- | -------- | --- | ----------- | ----- | ---------- | --- | --- | ------ | ------------ | ---------------------------- | --- | --- | --- |
| automated | rollback |     | strategies, | drift | monitoring |     | and |        |              |                              |     |     |     |
forecastingusingCNNandtransformer.arXivpreprint
| alerting, | and | enhanced | audit | logging | for | regulatory |     |     |     |     |     |     |     |
| --------- | --- | -------- | ----- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
arXiv:2304.04912.[CrossRef]
review. Further,mechanismsforinterpretingpolicies
|     |     |     |     |     |     |     |     | [5] Hambly,B.,Xu,R.,&Yang,H.(2023).Recentadvances |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
such as attention-based policy visualization and in reinforcement learning in finance. Mathematical
| counterfactual |     | explanations |     | will | be discussed |     | to  |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Finance,33(3),437-503.[CrossRef]
| enhance | interpretability |     | and | inter-agent |     | extensions |     |          |               |     |        |           |       |
| ------- | ---------------- | --- | --- | ----------- | --- | ---------- | --- | -------- | ------------- | --- | ------ | --------- | ----- |
|         |                  |     |     |             |     |            |     | [6] Liu, | X. Y., Xiong, | Z., | Zhong, | S., Yang, | H., & |
will be explored for interdependent financial Walid, A. (2018). Practical deep reinforcement
ecosystems.
|     |     |     |     |     |     |     |     | learning | approach | for stock | trading. | arXiv | preprint |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | -------- | ----- | -------- |
arXiv:1811.07522.[CrossRef]
|     |     |     |     |     |     |     |     | [7] Zhang,Y.,Zhao,P.,Wu,Q.,Li,B.,Huang,J.,&Tan, |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
DataAvailabilityStatement
M.(2020).Cost-sensitiveportfolioselectionviadeep
Datawillbemadeavailableonrequest. reinforcementlearning.IEEETransactionsonknowledge
anddataengineering,34(1),236-248.[CrossRef]
Funding [8] Li, H., Cao, Y., Li, S., Zhao, J., & Sun, Y. (2020).
XGBoostmodelanditsapplicationtopersonalcredit
Thisworkwassupportedwithoutanyfunding.
|     |     |     |     |     |     |     |     | evaluation. | IEEE | Intelligent | Systems, | 35(3), | 52-61. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----------- | -------- | ------ | ------ |
[CrossRef]
ConflictsofInterest
|     |     |     |     |     |     |     |     | [9] Alexandre, | M., | Silva, T. | C., | Connaughton, | C., & |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | ------------ | ----- |
Edimer Mahecha Contreras is affiliated with the Rodrigues, F. A. (2021). The drivers of systemic
Elite Group Services, San Jose, CA 95125, United risk in financial networks: a data-driven machine
States. Theauthordeclaresthatthisaffiliationhadno learninganalysis.Chaos,Solitons&Fractals,153,111588.
[CrossRef]
influenceonthestudydesign,datacollection,analysis,
interpretation, or the decision to publish. Edimer [10] Xu,Q.,Liao,Y.,Li,Q.,Zhang,J.,Song,Z.,Wang,L.,
&Yuan,X.(2024,August).SHAP-basedInterpretable
MahechaContrerasalsoservedasanAssociateEditor
ModelsforCreditDefaultAssessmentUsingMachine
| oftheICCKJournalofSoftwareEngineering |     |     |     |     |     | atthetime |     |           |         |      |               |            |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --------- | ------- | ---- | ------------- | ---------- | --- |
|                                       |     |     |     |     |     |           |     | Learning. | In 2024 | 14th | International | Conference | on  |
ofmanuscriptsubmission. Toensuretheintegrityof Software Technology and Engineering (ICSTE) (pp.
thepeer-reviewprocess,EdimerMahechaContreras
213-217).IEEE.[CrossRef]
wasnotinvolvedintheeditorialhandling,peerreview,
|     |     |     |     |     |     |     |     | [11] Jospin, | L. V., | Laga, H., | Boussaid, | F., | Buntine, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --------- | --------- | --- | -------- |
ordecision-makingprocessforthismanuscript,which W., & Bennamoun, M. (2022). Hands-on Bayesian
washandledindependentlybyanothereditor.
neuralnetworks—Atutorialfordeeplearningusers.
167

ICCKJournalofSoftwareEngineering
IEEEComputationalIntelligenceMagazine,17(2),29-48. 359-483.[CrossRef]
[CrossRef] [19] Gama, J., Žliobaite˙, I., Bifet, A., Pechenizkiy, M., &
[12] Alasbahi, R., & Zheng, X. (2022). An online Bouchachia, A. (2014). A survey on concept drift
transfer learning framework with extreme learning adaptation. ACM computing surveys (CSUR), 46(4),
machineforautomatedcreditscoring.IEEEAccess,10, 1-37.[CrossRef]
46697-46716.[CrossRef]
|     |     |     |     | [20] | Kreuzberger, | D., | Kühl, | N., & | Hirschl, | S. (2023). |     |
| --- | --- | --- | --- | ---- | ------------ | --- | ----- | ----- | -------- | ---------- | --- |
[13] Cheng,D.,Niu,Z.,Li,J.,&Jiang,C.(2022).Regulating Machine learning operations (mlops): Overview,
systemic crises: Stemming the contagion risk in definition, and architecture. IEEE Access, 11,
networked-loansthroughdeepgraphlearning.IEEE 31866-31879.[CrossRef]
TransactionsonKnowledgeandDataEngineering,35(6),
|     |     |     |     | [21] | Liu,X.Y.,Xia,Z.,Rui,J.,Gao,J.,Yang,H.,Zhu,M.,...& |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
6278-6289.[CrossRef]
|     |     |     |     |     | Guo,J.(2022).FinRL-Meta: |     |     | Marketenvironmentsand |     |     |     |
| --- | --- | --- | --- | --- | ------------------------ | --- | --- | --------------------- | --- | --- | --- |
[14] Bussmann,N.,Giudici,P.,Marinelli,D.,&Papenbrock, benchmarksfordata-drivenfinancialreinforcement
J.(2020).ExplainableAIinfintechriskmanagement. learning. Advances in Neural Information Processing
FrontiersinArtificialIntelligence,3,26.[CrossRef] Systems,35,1835-1849.
[15] Brim,A.(2020,January).Deepreinforcementlearning [22] Sculley,D.,Holt,G.,Golovin,D.,Davydov,E.,Phillips,
pairstradingwithadoubledeepQ-network.In2020 T., Ebner, D., ... & Dennison, D. (2015). Hidden
10thannualcomputingandcommunicationworkshopand technicaldebtinmachinelearningsystems.Advances
conference(CCWC)(pp.0222-0227).IEEE.[CrossRef] inneuralinformationprocessingsystems,28.
[16] Gašperov, B., & Kostanjčar, Z. (2022). Deep [23] Breck,E.,Cai,S.,Nielsen,E.,Salib,M.,&Sculley,D.
reinforcement learning for market making under a (2017,December).TheMLtestscore: ArubricforML
Hawkesprocess-basedlimitorderbookmodel.IEEE productionreadinessandtechnicaldebtreduction.In
controlsystemsletters,6,2485-2490.[CrossRef] 2017IEEEinternationalconferenceonbigdata(bigdata)
(pp.1123-1132).IEEE.[CrossRef]
[17] Mashetty,P.C.,Gangabathula,S.,Gangabathula,N.
|                  |               |        |             | [24] | Amershi, | S., Begel, | A., Bird, | C., | DeLine, | R., | Gall, |
| ---------------- | ------------- | ------ | ----------- | ---- | -------- | ---------- | --------- | --- | ------- | --- | ----- |
| V., Pullalarevu, | N., Chaganti, | K. R., | & Chaganti, | S.   |          |            |           |     |         |     |       |
R. (2025, July). Transfer Learning for Cross-Market H., Kamar, E., ... & Zimmermann, T. (2019, May).
|              |              |             |              |     | Software | engineering | for | machine | learning: | A   | case |
| ------------ | ------------ | ----------- | ------------ | --- | -------- | ----------- | --- | ------- | --------- | --- | ---- |
| Predictions: | Applications | in Emerging | and Volatile |     |          |             |     |         |           |     |      |
Economies. In 2025 6th International Conference on study.In2019IEEE/ACM41stInternationalConference
|     |     |     |     |     | onSoftwareEngineering: |     | SoftwareEngineeringinPractice |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------- | --- | ----------------------------- | --- | --- | --- | --- |
DataIntelligenceandCognitiveInformatics(ICDICI)(pp.
(ICSE-SEIP)(pp.291-300).IEEE.[CrossRef]
621-626).IEEE.[CrossRef]
|                   |             |             |              | [25] | Kim, | M., Zimmermann, | T., | DeLine, | R., | & Begel, | A.  |
| ----------------- | ----------- | ----------- | ------------ | ---- | ---- | --------------- | --- | ------- | --- | -------- | --- |
| [18] Ghavamzadeh, | M., Mannor, | S., Pineau, | J., & Tamar, |      |      |                 |     |         |     |          |     |
A.(2015).Bayesianreinforcementlearning: Asurvey. (2017). Data scientists in software teams: State of
theartandchallenges.IEEETransactionsonSoftware
| FoundationsandTrends®inMachineLearning, |     |     | 8(5-6), |     |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Engineering,44(11),1024-1038.[CrossRef]
168