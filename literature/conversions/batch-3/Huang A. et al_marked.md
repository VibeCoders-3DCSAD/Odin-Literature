---
conversion_metadata:
  converted_at: "2026-07-21T13:34:03Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Huang A. et al.pdf"
  source_pdf_sha256: "6312ad9421b12b78b9bb213a91e5560eaf054ce33f985b16afc741a5b80e38a2"
  page_count: 26
  markdown_char_count: 163647
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

Dynamic Calibration of Decision 
Thresholds for Financial 
Anomaly Detection:
Verification With Payment Platform 
Information and Data

Anzhong Huang
School of Economics and Management, Jiangsu University 
of Science and Technology, China

Xin Zhang
Graduate School of Business Administration, Wonkwang 
University, South Korea

Yuanyuan Wang

Sangbing Tsai

https:// orcid .org/ 0009 -0006 -8455 -6402

https:// orcid .org/ 0000 -0001 -6988 -5829

School of Economics and Management, Jiangsu University 
of Science and Technology, China

International Engineering and Technology Institute, Hong 
Kong

Ping Zhou

https:// orcid .org/ 0009 -0006 -3538 -1861

School of Accounting and Finance, Anhui Xinhua 
University, China

Lin Chen
School of Digital Economy and Trade, Wenzhou 
Polytechnic, China

Received: September 7th, 2025 | Accepted: December 1st, 2025

ABSTRACT

Digital payment channels have expanded quickly, reshaping transaction flows while opening new 
avenues for fraud. Isolation Forest (IF) remains attractive for unsupervised screening, yet deployments 
that rely on a fixed anomaly-score threshold deteriorate when traffic shifts or is actively manipulated. 
The authors present a Temporal-Attention Isolation Forest with Dynamic Calibration (TA-IFDC) that 
treats threshold selection as an adaptive component rather than a static post-processing step. The 
method monitors the evolving distribution of IF scores in streaming mode and updates the decision 
boundary online, while a lightweight temporal-attention module encodes short-range dependencies 
across consecutive transactions. Together, these pieces allow the detector to adjust to drift without 
sacrificing precision during stable periods.

KEYWORDS

Financial Transaction Security, Isolation Forest, Adaptive Decision Threshold, Temporal Dependency Modeling, 
Real-Time Fraud Analytics

1. INTRODUCTION

Over  the  last  decade,  the  accelerating  expansion  of  digital  financial  services  has  altered  the 
fundamental architecture of global payment systems. Mobile banking applications, instant online 
transfers, and integrated e-wallet ecosystems have rapidly displaced traditional cash and card-based

DOI: 10.4018/JGIM.395852

This article published as an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creative-
commons.org/licenses/by/4.0/) which permits unrestricted use, distribution, and production in any medium, provided the author of the 
original work and original publication source are properly credited.

1

---

<!-- PAGE 2 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

transactions, creating a financial environment that is faster, more accessible, and highly interconnected. 
This  transformation  has  yielded  substantial  benefits  in  terms  of  operational  efficiency  and  user 
convenience;  however,  it  has  also  brought  about  a  new  spectrum  of  security  vulnerabilities  that 
financial institutions must confront. Recent statistical surveys place the total global losses attributed 
to payment fraud at more than USD 45 billion in 2022, with forecasts indicating a continued upward 
trajectory as illicit actors incorporate automation, large-scale botnets, and adversarial machine learning 
into  their  operations.  Market  analyses  further  note  that  fraud  patterns  are  becoming  increasingly 
fragmented and adaptive, making the early detection of suspicious transactions a more complex task 
than ever before (Zhang et al., 2022).

The emergence of such high-frequency and high-value fraudulent transactions underscores the 
necessity for monitoring systems capable of functioning effectively under volatile, non-stationary data 
conditions. Modern fraud detection commonly relies on anomaly detection frameworks that assess 
deviations from established transactional norms(Hernandez Aros et al., 2024). Unsupervised detectors 
based on IF are widely used because they run fast on large datasets and do not rely on labels (Janjua et 
al., 2024; Kareem & Muhammed, 2024). IF builds random partition trees by choosing attributes and 
split values at random. Points that depart from the bulk are isolated in only a few splits, so their path 
lengths are short. In practice, this behavior makes IF a good fit for catching rare but consequential 
events in high-dimensional data without costly annotation.

Experience  with  IF  in  production  exposes  a  weak  spot:  decisions  usually  depend  on  a  fixed 
score cutoff set during an initial calibration or chosen heuristically, then left in place. Real payment 
traffic does not sit still—seasonal campaigns, macro shifts, and coordinated rings all move the score 
distribution (Sonani & Govindarajan, 2022). A static line can flood reviewers during benign surges 
or miss gradual shifts that matter; both outcomes degrade performance.

Streaming  tightens  the  constraints.  Each  transaction  must  be  scored  in  milliseconds,  while 
labels often arrive late or not at all(Vanini et al., 2023). The detector acts under uncertainty as the 
score distribution drifts, and a fixed threshold cannot follow that movement. Deeper models and 
feature tweaks help, but a robust, feedback-aware way to adjust cutoffs in unsupervised settings is 
still underexplored.

To address this, we introduce TA-IFDC and treat thresholding and temporal context as core 
parts of the detector (Attar et al., 2024). A dynamic calibration step updates the decision boundary 
online using recent score statistics and delayed outcomes, keeping alert rates stable while tracking 
distribution change (Al Lawati et al., 2025; Lin et al., 2024). A lightweight temporal component 
encodes short-range dependencies—inter-arrival times and simple session cues—so scores reflect 
what just happened rather than judging each record in isolation (Zheng et al., 2025).

We evaluate the framework on five payment datasets—IEEE-CIS, PaySim, CCFD, SFD-FD, and 
BankSim—against six competitive baselines. We report precision, recall, F1, AUC, and per-transaction 
latency under streaming protocols that preserve order, inject drift, and delay labels to mirror practical 
deployment.

Together, adaptive thresholding and temporal context close the gap between raw anomaly scores 
and  real-time  decisions  in  payment  systems,  yielding  consistent  gains  while  meeting  the  latency 
constraints of high-throughput gateways.

By  coupling  adaptive  thresholding  with  temporal  sequence  modeling,  TA-IFDC  bridges  a 
critical gap between raw anomaly scoring and real-time decision-making in financial fraud detection 
systems.  (Tchuente,  2022)  The  results  not  only  demonstrate  the  framework’s  ability  to  deliver 
consistent performance gains across multiple datasets but also highlight its suitability for deployment 
in high-throughput payment platforms where both fraud patterns and data distributions can change 
rapidly. This combination of operational adaptability and computational efficiency positions TA-IFDC 
as a promising candidate for next-generation fraud detection infrastructure in the financial sector 
(Bello et al., 2024; Fatlawi, 2025).

The primary contributions of this work are summarized as follows:

2

---

<!-- PAGE 3 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

(1)   A dynamic threshold calibration mechanism is proposed, enabling IF to operate adaptively in

non-stationary data environments without external supervision;

(2)   A temporal attention module is introduced to model inter-transaction dependencies, improving 
detection accuracy for sequential or contextual anomalies(Tokovarov & Karczmarek, 2022);
(3)   A unified detection framework—TA-IFDC—is constructed and evaluated across multiple real 
and synthetic payment datasets, demonstrating consistent improvements in accuracy, robustness, 
and latency over baseline models;

(4)   Extensive  experiments  and  ablation  studies  provide  insight  into  the  behavior  of  dynamic 
calibration  mechanisms  and  the  value  of  temporal  modeling  under  streaming  and  drifting 
conditions.

The remainder of this paper is structured as follows. Section 2 presents a review of related work 
in  fraud  detection,  threshold  calibration,  and  time-aware  anomaly  modeling.  Section  3  describes 
the architecture and core components of the proposed TA-IFDC framework. Section 4 details the 
experimental setup, including datasets, evaluation metrics, and baseline configurations. Section 5 
presents and interprets the experimental results. Section 6 discusses the research findings, limitations, 
and implications. Finally, Section 7 concludes the paper and outlines directions for future work.

2. RELATED WORK

The increasing reliance on unsupervised anomaly detection techniques in the financial domain 
has  drawn  extensive  attention  to  IF  and  its  variants.  Originally  proposed  by  Liu  et  al.,  the  IF 
algorithm isolates observations by randomly selecting features and split values, under the assumption 
that  anomalies  are  more  susceptible  to  early  isolation(Al  Farizi  et  al.,  2021;  Hilal  et  al.,  2022; 
Immadisetty, 2025). Its efficiency and effectiveness have rendered it a foundational tool in large-scale 
and high-dimensional fraud detection tasks. However, the original IF model lacks adaptability to 
time-varying data patterns and fails to incorporate contextual or sequential transaction information, 
which are prevalent in financial fraud scenarios(Ali et al., 2022; Du & Shu, 2022; Kamuangu, 2024; 
Quan et al., 2024).

Efforts to overcome the inherent limitations of the IF algorithm have taken many forms, though 
the core motivation remains the same: improve adaptability without sacrificing interpretability(Lam, 
2025; Shanaa & Abdallah, 2025; Wang et al., 2023). Early adaptations for streaming data, typified 
by the Online-iForest approach, allowed incremental updates to the ensemble of trees, enabling the 
model to handle new transactions as they arrive(Immadisetty, 2025; Leveni et al., 2025). This shift 
from batch processing to a more fluid, real-time structure was a practical leap for high-frequency 
domains such as payment platforms. Other lines of work explored hybrid architectures that combine IF 
with ensemble classifiers or incorporate domain-specific engineered features to boost discrimination 
accuracy,  particularly  in  noisy,  high-dimensional  datasets(Koziara  &  Karczmarek,  2022;  Núñez 
Delafuente et al., 2024; L. Zhang et al., 2025). More recently, graph-based formulations—exemplified 
by GNN-IF—embed transaction records into account–entity graphs, capturing relational signals that 
tree models in isolation would overlook(Chen & Tsourakakis, 2022; Kim et al., 2022). While these 
methods offer structural flexibility or richer representation learning, they still inherit the same fixed 
thresholding mechanism as the vanilla IF, which inevitably curtails responsiveness when fraud patterns 
shift unexpectedly. This is a notable bottleneck, especially in adversarial settings where attackers 
deliberately exploit static detection boundaries.

Calibrating  decision  thresholds  remains  underexplored  relative  to  model  design  in  anomaly 
detection. In many mature pipelines, the anomaly score is mapped to a decision through a single 
operating point chosen at launch and rarely revisited. Under non-stationary traffic, that practice is 
brittle: concept drift, class-prior shift, and seasonal volume swings push the score distribution away 
from the original calibration, tilting the false-positive/false-negative mix. In financial settings the

3

---

<!-- PAGE 4 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

asymmetry is costly—missed fraud yields direct loss, while excessive alerts erode reviewer trust and 
inflate operational budgets. Recent work on adaptive thresholding has opened up useful directions, 
particularly in situations where labels arrive late or sparsely, and batch evaluation isn't feasible. Many 
systems rely on simple rules—rolling quantiles, for example—to keep the decision boundary in sync 
with shifting score distributions, while others incorporate feedback from downstream performance, 
nudging thresholds over time to maintain a reasonable precision–recall balance. There’s also a stream 
of research that treats thresholding as a policy problem, often applying reinforcement learning to 
track evolving attacker behavior. However, in practice, two issues tend to surface. First, when the 
data distribution is heavy-tailed or the traffic arrives in bursts, naïve update windows can behave 
erratically, producing unstable alert patterns. Second, most of these approaches still assume access to 
trustworthy labels, which are often unreliable or delayed in real-world environments. Tools like Platt 
scaling or isotonic regression help calibrate probabilities, but they don’t solve the problem of where to 
actually place the operating point. So while adaptive strategies show potential, especially in dynamic 
or semi-supervised settings, their practical value is still constrained by label availability. In these cases, 
approaches that combine anomaly scoring with lightweight, feedback-tolerant calibration—without 
relying heavily on labels—remain highly relevant. A related line of work frames threshold control 
as a learning policy, often via reinforcement learning (RL). Such methods tune a reward reflecting 
precision–recall trade-offs and adapt under drift, but they depend on frequent, high-quality feedback—
rare in production payment streams. TA-IFDC instead calibrates from score distributions and sparse, 
delayed outcomes, achieving responsiveness without a heavy supervision loop.

In practical financial environments, anomaly detection systems are required to cope with a wide 
spectrum of transaction types, the continual emergence of new fraud strategies, and the inherent 
variability of streaming data(Eswar Prasad et al., 2023; H. Zhang et al., 2025). Scholars have examined 
a range of detection paradigms, from supervised models—such as gradient-boosted decision trees 
(e.g., XGBoost), deep architectures like autoencoders, to hybrid frameworks that merge clustering 
outputs with classification layers—to address these challenges(Almazroi & Ayub, 2023; Mazumder 
et  al.,  2025).  Although  supervised  learning  methods  can  deliver  strong  accuracy  when  abundant 
annotated data are available, their dependence on up-to-date labels often limits their flexibility and 
long-term maintainability once deployed. On the other hand, unsupervised approaches, including 
Isolation Forest, one-class Support Vector Machines (SVM), and various clustering schemes, avoid the 
label dependency and thus can be applied more broadly across heterogeneous datasets. Nevertheless, 
these methods frequently encounter difficulties in providing transparent decision logic and in setting 
decision thresholds that remain effective under shifting data distributions. The datasets most commonly 
used for evaluation include the IEEE-CIS Fraud Detection Dataset, PaySim, the CCFD dataset, and 
BankSim. Each dataset presents unique characteristics—ranging from anonymized features and class 
imbalance to temporal drift and behavior simulation—requiring detection frameworks to be robust 
across multiple conditions.

Compared  with  existing  approaches,  the  method  proposed  in  this  paper  distinguishes  itself 
through its integration of dynamic threshold calibration with an unsupervised anomaly detection 
backbone.  Rather  than  designing  new  feature  representations  or  model  architectures,  this  study 
focuses on the often-overlooked thresholding component and enhances it with a feedback-informed 
and context-aware strategy. The TA-IFDC framework combines a temporal attention mechanism with 
an adaptive calibration module, allowing the model to respond dynamically to score fluctuations and 
transaction context. This design improves anomaly interpretability, reduces false alarms, and preserves 
the unsupervised nature of IF-based models, making it more suitable for real-world deployment where 
labeled data are sparse and latency constraints are strict.

In summary, while previous studies have improved various facets of anomaly detection models—
such as feature representation, network architecture, or data stream handling—few have systematically 
addressed the calibration challenge within unsupervised fraud detection frameworks. This study aims

4

---

<!-- PAGE 5 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

to fill that gap by introducing a threshold adaptation mechanism that complements the strengths of 
IF, while enhancing temporal responsiveness and practical applicability.

3. PROPOSED METHOD: TA-IFDC

We propose a novel anomaly detection framework named TA-IFDC, designed to enhance the 
performance of IF through adaptive threshold adjustment and temporal-context modeling. This section 
details the system architecture, the role of each component, and the mathematical formulation of 
the algorithm.

3.1 Overview of TA-IFDC

The TA-IFDC framework is designed with four major components:

1.   Sliding Window Preprocessing for temporal transaction segmentation;
2.   Temporal Attention Encoder, which captures transaction time patterns and user behavior drift;
3.   IF Scoring, responsible for initial anomaly detection;
4.   Dynamic Threshold Calibration Module, which adaptively adjusts the decision boundary based

on recent detection performance.

A high-level schematic of the method is shown in Fig 1 .

Figure 1. Overview of the main processing stages in TA-IFDC

5

---

<!-- PAGE 6 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

3.2 Sliding Window-Based Transaction Segmentation

To enable temporal modeling and online threshold calibration, transaction data is divided into

overlapping windows.

Let the incoming transaction stream be denoted as:

𝒯  =    {   x  1  ,  x  2  , … ,  x  N   }   ,  x  i    ∈   ℝ   d

where xi represents a single transaction with d features.
We construct a sliding window of size W, with stride S, resulting in a sequence of windows:

𝒲  k    =    {   x  kS  , … ,  x  kS+W−1   }   , k  =  1, … , K

This segmentation supports online model updates and threshold adaptation.

3.3 Temporal Attention Encoder

To capture periodic patterns and behavior drift, we embed a temporal attention mechanism that

computes the temporal relevance of each transaction within a window.

Let:

• 
•

X  k    =    [   x  k,1  , … ,  x  k,W   ]     denote the feature matrix of window   𝒲  k   
  T  k    =    [   t  k,1  , … ,  t  k,W   ]     denote the corresponding time-stamps

We define time encoding vectors   e  k,j    =  ϕ  (   t  k,j   )     ∈   ℝ   h  , where 𝜙(∙)can be a Fourier-based positional

encoding or learned embedding.

Each transaction is transformed into:

˜ x    k,j    =  concat  (   x  k,j  ,  e  k,j   )

We then compute attention scores using scaled dot-product attention:

_ 
  α  ij    =    
 ∑ l=1

_
exp   (   q  i  ⊤   k  j   /  √ 
 d  k     )   
_
 d  k     )   
    exp   (   q  i  ⊤   k  l   /  √

W

where:

• 
• 
•

q  i    =   W  Q      ˜ x    k,i    is the query vector
  k  j    =   W  K      ˜ x    k,j    is the key vector
dk is the dimension of keys

The attention-enhanced transaction vector becomes:

W

z  i    =   ∑ j=1

α  ij   ⋅   (   W  V      ˜ x    k,j   )

These contextual representations zi are then passed to the IF model for scoring.

6

---

<!-- PAGE 7 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

3.4 IF Scoring

The enhanced representations zi are input into the IF to calculate anomaly scores.
IF relies on recursive partitioning. For each instance zi, the anomaly score s(zi) is computed as:

s  (   z  i   )     =   2   −

E  (  h ( z  i  )  )   
 _ 
c  (  n )

where:

•  E(h(zi \)) is the average path length of zi in all trees
• 
•

n is the subsample size used to build trees
c(n) is the normalization factor:

c  (  n )     =  2H  (  n − 1 )    −  2  (  n − 1 )    _ 
n

and H(i) is the harmonic number:

H  (  i )     =  ln   (  i )    + γ, γ  ≈  0.5772

A score close to 1 indicates high anomaly probability.

3.5 Dynamic Threshold Calibration

In traditional IF implementations, the decision threshold θ\theta is fixed, often determined by 
cross-validation or empirical heuristics. However, under real-world financial settings, user behavior 
patterns and transaction distributions can drift significantly over time, resulting in unstable detection 
performance if the threshold remains static.

To  address  this,  we  design  a  Dynamic  Threshold  Calibration  (DTC)  module  that  adaptively

adjusts θ\theta for each sliding window using recent prediction feedback statistics.

3.5.1 Adaptive Threshold Update Rule

Let    𝒮  k    =    {   s  1  ,  s  2  , … ,  s  W   }      be  the  anomaly  scores  in  window    𝒲  k   ,  and  let  θk  be  the  calibrated

threshold at time step k. We define a percentile-based update rule with smoothing:

θ  k    =    (  1 − λ )    ⋅  θ  k−1   + λ ⋅ Quantil  e  β    (   𝒮  k   )

where:

λ∈[0,1] is the learning rate (adaptivity coefficient),

• 
•  Quantileβ(∙)returns the β-th percentile of the scores (e.g., β=0.95 for top 5% anomaly),
•

θ0 is initialized from the first window as baseline.

This rule smooths threshold changes to prevent instability due to local score fluctuations.

3.5.2 Feedback-Informed Calibration (Optional Enhancement)

When delayed ground truth labels are available (e.g., confirmed fraud), a feedback loop is used

to refine θk based on false positive and false negative counts.

Let:

7

---

<!-- PAGE 8 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

•  FPk: false positives in   𝒲  k   ,
•  FNk: false negatives,
•  ∆θk: correction factor.

We define:

Δ  θ  k    =  η ⋅   (  α ⋅

F  P  k   _ W   −  (1 − α)  ⋅

F  N  k   _ W   )

and update the threshold as:   θ  k    ←   θ  k   + Δ  θ  k    where:

η is the feedback gain (tuning parameter),

• 
•  α∈[0,1] balances precision and recall.

This  formulation  penalizes  overly  aggressive  thresholds  (high  FP)  and  overly  conservative

thresholds (high FN), encouraging balance.

3.6 Overall Algorithm Description

The  TA-IFDC  framework  is  designed  to  perform  real-time  anomaly  detection  in  financial 
transaction streams, with particular emphasis on adaptability to evolving data distributions. It integrates 
temporal behavior modeling, ensemble anomaly scoring, and an adaptive decision-making mechanism 
to accommodate the non-stationary nature of payment systems.

Initially, the transaction stream is segmented using a sliding window approach. Each window 
contains a sequence of temporally ordered transaction records, which serves as the processing unit 
for detection. This segmentation enables localized modeling of user behavior and supports gradual 
updates of the decision threshold over time.

For each window, temporal characteristics of transactions are encoded into fixed-length feature 
representations. These time-sensitive features are derived using positional encoding techniques and 
capture both the periodicity and recency of financial activities. To further enhance context-awareness, 
a temporal attention mechanism is applied. The mechanism assigns varying degrees of importance 
to transactions observed within a given time window, enabling the model to focus more on events 
that carry greater behavioral significance, while downplaying patterns that contribute little to the 
detection objective.

After temporal encoding, each transaction is processed through an ensemble of Isolation Trees, 
which  partition  the  feature  space  in  a  randomized  manner.  IF  does  not  chase  balanced  splits.  It 
samples a feature and a cut at random at each node, and the isolation depth depends on how far the 
transaction sits from the main mass. Transactions that deviate substantially from the bulk of data 
are separated earlier, producing shorter path lengths and correspondingly higher anomaly scores. In 
financial datasets, such cases often represent unusual spending bursts, irregular transfer patterns, or 
atypical device usage, all of which warrant closer scrutiny. The unsupervised nature of this scoring 
process is particularly important in fraud detection, where labeled anomalies are scarce, delayed, or 
incomplete. Moreover, the low computational cost of Isolation Trees allows the method to scale to 
millions of transactions per day without prohibitive infrastructure requirements.

Once the anomaly scores for a given observation window are available, they serve as the basis 
for  recalibrating  the  detection  threshold.  The  TA-IFDC  framework  avoids  the  rigidity  of  static 
thresholds by adopting a quantile-based dynamic calibration approach. In practical terms, this means 
that the decision boundary at time t is updated by blending the previously applied threshold with 
a high-percentile statistic—such as the 95th or 97th percentile—of the current score distribution. 
The blend ratio controls how quickly the system reacts to abrupt changes, such as a sudden spike 
in fraudulent activity following a phishing campaign. A purely percentile-based recalibration could

8

---

<!-- PAGE 9 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

overreact  to  noise,  while  a  purely  historical  threshold  would  be  slow  to  adapt;  the  interpolation 
mechanism  balances  these  extremes,  maintaining  stability  without  sacrificing  responsiveness. 
Quantile selection was ablated across 90–99 percentiles. Below ~93% false positives surged; above 
~97% recall fell sharply. We adopt 95% as a balanced operating point, with ±1–2% guardrails under 
drift. To avoid overreaction, a hysteresis rule and adaptive smoothing cap limit per-window threshold 
change to ≈2–3% of the prior value.

In operational settings, it is common for feedback on suspected transactions to arrive only after 
several hours or even days, once investigations are complete. TA-IFDC is designed to incorporate such 
delayed supervision when available. Specifically, the recalibration step introduces a correction term 
proportional to the recent imbalance between false positives and false negatives. When false positives 
rise, the threshold is nudged upward to protect analyst capacity. If post-review reveals missed fraud, 
the threshold is lowered to recover recall. Updates use delayed labels when available and otherwise 
rely on recent score dynamics, allowing the operating point to adapt under partial supervision typical 
of large-scale payment streams.

After each threshold update, transactions in the active window are scored against the current 
operating point. Records above the cutoff move to the risk controls. Depending on policy and traffic, 
these controls may act automatically—short holds, step-up authentication, velocity caps—or hand the 
case to investigators. TA-IFDC runs in mini-batch mode and in an online (prequential) loop, while 
meeting real-time and accuracy requirements. When a window finishes, the pointer slides forward 
and calibration continues on the next slice, letting the system keep pace with the stream.

Temporal feature encoding, context-aware attention, isolation-based scoring, and online threshold 
calibration jointly counter concept drift and ongoing adversarial changes. Legitimate behavior swings 
with sales, public events, and product launches; meanwhile, attackers keep changing tactics to slip 
past static rules. By making calibration part of the design rather than a post-hoc tweak, TA-IFDC ties 
score production to the decision rule and closes the long-standing gap between scoring and action. 
The modules are small and loosely coupled, making integration with existing case-management and 
risk-control systems straightforward.

We evaluate on five benchmarks—IEEE-CIS Fraud Detection, PaySim, CCFD, SFD-FD, and 
BankSim—spanning real and simulated payment streams with varied class priors and feature sets. 
We assess precision, recall, F1, AUC, per-record latency, and robustness under induced drift and 
delayed feedback under constraints similar to production.

4. EXPERIMENTAL SETUP

We  evaluate  TA-IFDC  under  conditions  close  to  our  target  deployment.  The  focus  is  on 
behaviors that matter in practice. We use five benchmarks—IEEE-CIS, PaySim, CCFD, SFD-FD, 
and BankSim—to cover large-scale online payments and simulated account-takeover cases. Using 
both real and synthetic data lets us probe stationary regimes as well as non-stationary patterns such 
as seasonal shifts and tactic drift.

For comparability, one protocol is applied across datasets. Each dataset is ordered chronologically 
and split 80%/10%/10% into train/validation/test by time, preventing look-ahead leakage—crucial 
for streaming or time-dependent transactions. We report precision and recall for the false-alarm/miss 
trade-off, F1 as their harmonic summary, AUC for ranking across thresholds, and per-record latency 
for near-real-time constraints. As a set, these metrics give a more faithful picture than accuracy on 
heavily imbalanced data.

We  benchmark  against  six  baselines:  Online-iForest,  Hybrid-AI,  GNN-IF,  XGB-Anomaly, 
SSR-RVFL, and an autoencoder-based detector. Each baseline follows its paper and public code when 
available; otherwise, hyperparameters are tuned on the validation split. This keeps implementations 
faithful to their intended design, so any gaps reflect modeling choices rather than configuration quirks.

9

---

<!-- PAGE 10 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

4.1 Datasets

For the empirical evaluation of the TA-IFDC framework, we selected five representative financial 
transaction datasets: IEEE-CIS Fraud Detection, PaySim, CCFD, SFD-FD, and BankSim. Together, 
these datasets encompass a wide spectrum of operational contexts, ranging from large-scale real-world 
payment records to semi-synthetic and fully simulated banking scenarios. They not only reflect static 
historical fraud patterns but also capture environments where fraudulent behavior evolves over time, 
sometimes in response to seasonal trends or system countermeasures. The mix of real transactions 
and synthetic traces exposes the method to distribution shift, class-prior variation, and non-stationary 
temporal patterns, offering a clearer view of detection performance and adaptability.

The  IEEE-CIS  Fraud  Detection  dataset  (originally  released  for  the  2019  IEEE-CIS  Fraud 
Detection challenge on Kaggle) contains more than one million labeled online transactions. The dataset 
includes device and browser fingerprints, timestamps, and a mix of anonymized fields describing user 
behavior and payment context. The overall fraud rate sits around 3.5%—roughly one in twenty-eight 
cases—which is close to what’s seen in production systems. Because the features are high-dimensional 
and partly anonymized, it’s a good test bed for anomaly detectors that need to catch rare events without 
overreacting to noise. The time-stamped nature of the records also exposes gradual month-to-month 
drifts  in  device  types  and  behavior,  which  made  it  useful  for  testing  how  the  temporal-attention 
block and the dynamic threshold module in TA-IFDC react to changing conditions. For comparison, 
we also used PaySim, a synthetic mobile-money dataset built from agent-based simulations of real 
transaction behavior observed in sub-Saharan Africa. It comprises over 6 million transactions across 
five operational categories, including “TRANSFER” and “CASH-OUT”. Although synthetic, PaySim 
mirrors real user interaction patterns, offering a controlled yet realistic testing ground. The inherent 
low fraud prevalence (approximately 0.13%) and the ease of injecting artificial concept drift make it 
ideal for testing the model’s responsiveness to behavioral shifts.

The CCFD dataset, provided by a European card issuer, contains approximately 285,000 credit 
card transactions, with features anonymized using principal component analysis. Fraudulent cases 
represent a mere 0.172% of the data, making it an extreme example of class imbalance. While the 
feature structure is static, it remains a widely accepted benchmark for validating anomaly detection 
models, particularly with respect to precision, recall, and F1-score.

The SFD-FD dataset, published by IBM, is a synthetically generated dataset rooted in real fraud 
patterns observed in banking and financial services. It includes temporal transactions, labeled fraud 
cases, and control variables designed to simulate concept drift scenarios, such as seasonal changes 
or policy shifts. This dataset offers controllable drift events, which is essential for validating the 
adaptability of the dynamic threshold mechanism under non-stationary data distributions.

BankSim is a synthetic corpus generated with a multi-agent simulation of retail-bank customers. 
It covers routine account activity—deposits, withdrawals, transfers—over extended periods, and every 
record carries a timestamp. The structure of the dataset allows us to track account behavior over time 
and run analyses using either sequences or sliding windows. Importantly, the labels aren't randomly 
assigned—they’re based on noticeable deviations from how each account typically behaves. That 
means we’re not just flagging rare events, but behavior that breaks the usual pattern. Because of that, 
BankSim gives us a chance to test whether a detector like TA-IFDC can catch suspicious behavior as 
it’s happening, especially when both timing and context matter. In our case, those simulated shifts 
weren’t far off from what real fraud teams deal with—think seasonal shopping spikes, low-value card 
testing, or sudden coordinated withdrawals. That’s why we found both PaySim and BankSim useful 
for checking if the model stays stable when transaction patterns start to shift.

We  ran  all  datasets  through  the  same  preprocessing  pipeline.  For  missing  values,  we  either 
dropped the affected rows or filled them in depending on how much data was lost. Numeric features 
were scaled down to avoid skewing the model due to value ranges. Categorical ones were turned 
into indices or dummy variables as needed. If timestamps were present, we made sure not to shuffle 
anything—records were kept in original order to avoid peeking into the future by accident.

10

---

<!-- PAGE 11 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

Each dataset was then split by time into training, validation, and testing sets (roughly 80/10/10). 
The training phase was used to build the Isolation Forest and warm up the attention module. For 
tuning, we relied on the validation set—not just for hyperparameters but also to adjust the threshold 
dynamically so it tracks the fraud rate and input distributions over time. The test set stayed untouched 
until the end, just for final scoring.

Since the datasets vary quite a bit—some large, some small, with different structures and fraud 
rates—we were able to see how the model holds up both when things are stable and when they shift. 
That’s pretty close to what actually happens in real payment systems.

4.2 Evaluation Metrics

We tested TA-IFDC in settings that look a lot like real deployment. The goal wasn’t just to see 
accuracy on paper but to understand how it behaves when decisions have to land in a few milliseconds, 
when the fraud rate drifts over time, and when analysts can only check a limited number of alerts. We 
used standard metrics, but the way we read them followed a live, ordered-stream setup—no random 
reshuffling.

Precision, or how many alerts are actually right, basically shows how much trust you can put in 
the system. When precision is low, investigators waste time and customers get unnecessary delays; 
when it’s high, the workflow feels lighter. Recall, on the other hand, tells us how much fraud we 
actually caught. Missing early fraud isn’t just a number—it often spreads to related accounts and 
multiplies the damage.

Because payment streams are heavily imbalanced, accuracy is not informative. We summarize the 
error trade-off with the harmonic mean  F1  =  2 ⋅   Precision ⋅ Recall _ 
Precision + Recall  , which rewards balanced improvements 
and  penalizes  one-sided  gains.  Since  a  single  number  hides  local  behavior,  we  also  examine  the 
precision–recall neighborhood around the operating point chosen under a fixed alert budget so the 
analysis remains tied to reviewer capacity and loss-prevention costs.

We use AUC-ROC to assess ranking quality—a threshold-independent view of whether fraudulent 
transactions  tend  to  outrank  legitimate  ones  across  operating  points.  Because  ROC  area  can  be 
optimistic under extreme imbalance, we also examine PR-curve behavior near the recall levels that 
matter, so a high AUC does not mask a weak alert mix. In our setting, AUC additionally reflects the 
quality of the anomaly scores that feed dynamic calibration before any cutoff is applied.

Latency is measured as the time from event arrival to decision—milliseconds per record online, 
or event steps in replay. It’s not just about average speed—we also looked at the slowest cases. A 
model that’s quick most of the time but occasionally lags can still break service-level agreements. 
In payment systems, those few extra milliseconds matter. If a hold or block decision comes too late, 
the money’s already gone, and no amount of accuracy helps after that. So, we checked tail latency 
as well, using P95 and P99 to catch those worst-case delays. In our tests, even under peak load, the 
longest delays stayed within about 1.4 times the average. That’s good enough to say TA-IFDC stays 
within the real-time bounds required by most transaction platforms.

To ensure comparability, each dataset is ordered chronologically and split by time into train/
validation/test  with  no  look-ahead.  Metrics  are  computed  under  stationary  traffic  and  under 
concept-drift using prequential replay, so observed differences reflect modeling rather than protocol 
artifacts. The same splits and metric definitions apply to baselines and to TA-IFDC, and operating 
points are aligned with realistic alert budgets. In sum, this lens covers error costs (precision/recall), 
their balance (F1), threshold-independent ranking (AUC), and deployability (latency) under changing 
class priors and evolving operating conditions.

4.3 Baseline Methods

To build a benchmarking framework that is both convincing and comprehensive, six baseline 
methods  were  selected,  each  representing  a  distinct  methodological  family  within  financial 
anomaly detection research. The selection was not arbitrary; these models are widely cited in the

11

---

<!-- PAGE 12 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

literature,  cover  diverse  algorithmic  paradigms,  and  are  known  to  perform  well  under  specific 
operating assumptions. Including such a variety ensures that comparisons with the proposed TA-IFDC 
framework are not confined to a single modeling philosophy but span multiple perspectives—ranging 
from purely isolation-based detection to hybrid, graph-augmented, and streaming-adaptive designs.
The first reference model, Hybrid-GNN-AE, combines Graph Neural Networks (GNNs) with 
Autoencoder-based reconstruction. In this architecture, transaction records are mapped into graph 
structures to encode user–device–transaction relationships. In this setup, we use GNNs to learn latent 
features, which are then fed into an autoencoder. The reconstruction error gives us an anomaly score. 
This kind of graph-based approach tends to shine when fraud spreads across platforms or channels, 
and  when  the  transaction  graph  itself  holds  meaningful  structure.  We’ve  seen  better  recall  when 
signals like shared IPs, reused merchant IDs, or even similar transfer patterns are included along 
with behavioral features. But there’s a flip side: when the graph is sparse or messy—few links, or 
too many irrelevant ones—the advantage fades. To deal with that, some systems add smoothing or 
fallback rules, so the model doesn’t lose power in cold-start or low-connectivity cases.

We brought in Online Isolation Forest (ONLINE-IFOREST) as a streaming-friendly version of 
the original IF. Rather than building full trees on a frozen dataset, it keeps rolling summaries—like 
histograms or sketches—and updates scores as new transactions come in. That setup helps keep things 
fast and light on memory, which matters when events are constant and labels don’t show up right away. 
That said, it relies on a fixed threshold. So when the score distribution drifts—say during a holiday 
sale or a traffic spike—the static cutoff can quickly become misaligned. We’ve seen it push up false 
positives or let things slip. That’s exactly the kind of situation TA-IFDC tries to handle better, using 
dynamic thresholding under a prequential setup.

We  also  compared  against  a  hybrid  setup  that  combines  a  standard  Isolation  Forest  with 
an  LSTM.  The  IF  handles  the  usual  anomaly  scoring,  while  the  LSTM  looks  for  local  temporal 
patterns—like bursts of activity, regular gaps between events, or recurring short-term behavior. The 
outputs are stitched together through a lightweight decision layer. In practice, this design tends to 
highlight suspicious behavior that clusters in time, which makes it conceptually quite close to what 
our temporal module aims to catch, though we approach it differently. The trade-off is label demand 
and maintenance cost: sequence models usually require labeled segments for tuning, and pronounced 
concept drift forces frequent retraining. With delayed or sparse feedback, fully unsupervised, real-time 
use becomes harder to sustain without relaxing latency budgets.

We also assess Enhanced-IF variants that stack IF with a secondary learner such as SVM or LOF 
to refine raw scores with margin- or density-based views. In static or gently drifting traffic this can lift 
precision and stabilize the alert mix, and the extra head is cheap to serve once trained. In faster-moving 
streams, however, decisions often still hinge on a fixed operating point; when the transaction mix or 
volume shifts quickly, precision deteriorates and recalibration is required. Cold-start users and newly 
observed devices are particular pain points for these stacked schemes.

We also looked at a hybrid fraud detection setup—call it Hybrid-AI-FD—that stitches together 
multiple components. It usually starts with a set of hand-tuned rules to weed out the obvious stuff, 
then brings in unsupervised models like clustering or reconstruction-based filters to scan the rest. 
On top of that, there's often a supervised layer to make the final decision. This kind of pipeline can 
work well when you have some labeled data and decent domain rules, especially if your goal is to 
tune sensitivity to match available analyst time. But moving it across systems isn’t always smooth. 
These setups tend to be tightly coupled to the original environment—they rely on stable features, 
good data hygiene, and assumptions that might not hold elsewhere. We've seen cases where rules 
go stale or inputs quietly change, leading to performance drops if updates aren’t carefully managed.
The last SSR-RVFL combines sparse representation learning with Random Vector Functional 
Link networks to map features quickly and flag atypical patterns. The approach is efficient and suits 
high-throughput settings with tight tail-latency targets. Its expressivity, however, is limited when 
fraud boundaries are strongly nonlinear or strategies change abruptly; sparse codes and fixed random

12

---

<!-- PAGE 13 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

projections may lag unless retuned, and performance can flatten when fraud signals spread across 
many weak features.

These baselines cover streaming IF, sequence-aware fusion, stacked refinement, system-level 
hybrids, and sparse/fast learners. The breadth is deliberate: improvements attributed to TA-IFDC 
should persist across memory-bounded streaming models, temporal models that leverage short-range 
dependence, and hybrid systems that mix learned scores with rules, rather than reflecting gaps in 
a  narrow  comparator  set.  Instead,  the  proposed  method  is  evaluated  against  a  representative  and 
technically  diverse  landscape  of  fraud  detection  approaches.  Transformer-based  detectors  were 
excluded due to dense supervision needs and higher GPU inference cost, which conflict with our 
unsupervised, low-latency objective. Nevertheless, their sequence-modeling strength aligns closely 
with the temporal-attention idea in TA-IFDC, making them strong candidates for future comparative 
studies.

Finally,  to  maintain  methodological  consistency,  the  implementation  of  ONLINE-IFOREST 
in  this  study  strictly  follows  the  officially  described  algorithm,  ensuring  that  the  online  update 
rules, isolation scoring process, and streaming histogram construction are faithfully reproduced for 
fair comparison. This version formalizes the online update rules, isolation scoring functions, and 
stream-based histogram construction, ensuring experimental reproducibility and citation accuracy. 
Each baseline was implemented using consistent data partitions and preprocessing protocols. Their 
hyperparameters were tuned using the same validation strategy as the proposed model to ensure fair 
comparisons. All models were evaluated across identical performance metrics, including classification 
accuracy, latency, and adaptability under concept drift, as outlined in Section 4.2.

The comparative characteristics of these six baseline models are summarized in Table 1, which 
organizes them by supervision type, temporal adaptability, thresholding mechanism, and primary 
strengths. This tabular view serves two purposes: first, to provide a concise technical snapshot of each 
method for quick reference; second, to highlight the diversity in modeling strategies that form the 
benchmark set against which TA-IFDC is evaluated. By juxtaposing these features, the table makes 
explicit the methodological gaps—particularly in dynamic threshold calibration and temporal context 
modeling—that the proposed framework is designed to address.

Table 1. Comparison of Baseline Models for Financial Anomaly Detection

Model Name

Supervision

Temporal 
Adaptation

Threshold 
Mechanism

Strengths

Hybrid-GNN-AE

Unsupervised

ONLINE-IFOREST

Unsupervised

Adaptive IF + 
LSTM

Semi-supervised

Graph Temporal 
Embedding

Histogram-based 
Streaming

LSTM Temporal 
Modeling

Fixed

Fixed

Adaptive

Enhanced IForest

Unsupervised

Static

Fixed / Heuristic

Captures relational 
anomalies across platforms

Efficient in real-time stream 
processing

Models sequential fraud 
behavior effectively

Integrates multiple anomaly 
criteria

Hybrid-AI-FD

Hybrid

Rule-Based + Time 
Awareness

Hybrid (Manual + 
Learned)

Leverages both labeled and 
unlabeled data

SSR-RVFL

Semi-supervised

Feedback-Driven 
Regulation

Self-Calibrated

Learns under concept drift 
with dynamic feedback

13

---

<!-- PAGE 14 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

4.4 Hyperparameter Settings and Training Strategy

To  ensure  fair  and  reproducible  comparisons,  all  models  were  trained  and  evaluated  under 
consistent experimental settings across datasets. The proposed TA-IFDC framework and all baseline 
models were implemented using Python 3.10, with core dependencies including scikit-learn, PyTorch, 
PyOD, and DGL for graph-based architectures. The computations were performed on a workstation 
equipped with an Intel i9 CPU, 64GB RAM, and NVIDIA RTX 3090 GPU. For replication, five-fold 
chronological  cross-validation  was  used  within  each  dataset’s  training  slice  (no  look-ahead). 
Random seeds, preprocessing scripts, and hyperparameters were fixed and version-controlled; full 
configurations and library versions are archived in the supplementary material. In addition, all reported 
performance  metrics  are  presented  as  mean  ±  standard  deviation  with  95%  confidence  intervals 
computed through bootstrap sampling to assess the stability of results. This design ensures temporal 
integrity and makes experimental outcomes directly comparable across datasets and baselines.

For  the  TA-IFDC  framework,  the  base  IF  component  was  configured  with  100  trees  and  a 
subsampling  size  of  256.  The  anomaly  score  calibration  module  employed  a  sliding  calibration 
window of size 2,000 transactions, updated every 100 steps. The temporal attention mechanism was 
implemented using a two-head attention block with softmax-normalized weights, attending to a past 
window of 15 steps. The dynamic threshold function was initialized using a quantile-based estimator 
and refined online via a momentum-based update rule with a smoothing factor α=0.1. A minimum 
threshold cap was enforced to mitigate threshold collapse under sparse anomaly regions.

For  online  inference,  the  TA-IFDC  operated  in  a  streaming  fashion  without  access  to  future 
transactions. To simulate realistic deployment, anomalies were detected at the moment of transaction 
arrival based solely on historical context. To handle distributional shifts, a lightweight drift detector 
monitored the Kolmogorov–Smirnov distance between incoming and historical feature distributions. 
Upon detection of significant drift (p<0.01), the threshold calibrator's state was partially reset to 
adapt to the new regime.

The baseline models were tuned individually using the validation subset (10% of each dataset) 
by grid search. For ONLINE-IFOREST, tree depth was limited to 10, and histogram bins were set 
to 64 for efficient memory use. GNN-based models used two graph convolution layers with ReLU 
activation and 32-dimensional embeddings. For AE-Fraud, the autoencoder had a bottleneck size of 
16, trained with a mean squared reconstruction loss using the Adam optimizer with learning rate le-3 
for 30 epochs. LOF used k=20 nearest neighbors, and XGBoost-Fraud employed a maximum tree 
depth of 6 with early stopping on AUC.

All experiments used an 80/10/10 train-validation-test split, stratified by fraud label distribution 
where available. In unsupervised settings, the training was performed solely on unlabeled data or 
presumed-clean historical transactions. Evaluation metrics, including precision, recall, F1-score, AUC, 
and detection latency, were recorded for both batch and streaming scenarios. All reported results are 
averaged over five independent runs with different random seeds. We report mean ± standard deviation 
for all metrics, and 95% confidence intervals estimated via bootstrap over transaction windows to 
indicate the statistical stability of results across repeated runs.

This training protocol ensures that model comparisons reflect performance differences attributable 
to algorithmic design rather than hyperparameter or implementation variance, thereby supporting the 
scientific validity of the reported results.

5. EXPERIMENTAL RESULTS

To  really  see  how  well  TA-IFDC  holds  up,  we  ran  eight  rounds  of  comparative  tests  across 
five widely used datasets—IEEE-CIS, PaySim, CCFD, SFD-FD, and BankSim. These experiments 
weren’t just about getting good scores. We wanted to understand how the model performs in terms 
of not just accuracy, but also how it adapts, how fast it reacts, and how interpretable the results are in 
practice. For consistency, we stuck with a core set of evaluation metrics: Precision, Recall, F1-score,

14

---

<!-- PAGE 15 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

AUC, and per-transaction inference latency. Each test was designed to mimic the kind of messy, 
real-world situations that fraud detection systems actually face.

The first experiment presents an overall benchmark comparison across all six baseline models on 
the IEEE-CIS dataset. This dataset represents high-volume, real-world online payment transactions 
and is thus used as the main benchmark. Table 2 summarizes the results.

Table 2. Overall performance comparison on IEEE-CIS dataset

Model

TA-IFDC (Proposed)

Online-iForest

Hybrid AI-Fraud

GNN-IF

SSR-RVFL

XGB-Anomaly

Precision

Recall

0.936

0.862

0.892

0.884

0.915

0.851

0.918

0.845

0.877

0.871

0.906

0.823

F1

0.927

0.853

0.884

0.877

0.910

0.836

AUC

0.974

0.931

0.944

0.942

0.961

0.918

Latency (ms)

29

22

68

54

49

34

On IEEE-CIS, TA-IFDC achieves the best F1 (0.927) and AUC (0.974) at 29 ms per record, 
outperforming all deep/hybrid baselines; see Fig. 2(a–b) and Table 2. Panel (a) sorts models by F1 
and shows that SSR-RVFL attains a competitive AUC yet at higher latency, while panel (b) ranks 
latency and highlights that Online-iForest is fastest but with notably lower F1.

Figure 2. IEEE-CIS overall results: accuracy and latency

These  results  indicate  that  TA-IFDC  outperforms  all  comparative  methods  in  terms  of  both 
classification performance and computational efficiency. While SSR-RVFL shows a high AUC, it 
comes at the cost of increased latency. TA-IFDC achieves the highest F1 and AUC while remaining 
faster than all deep and hybrid models. This suggests it is highly suitable for high-throughput payment 
environments.

The second experiment investigates the contribution of the dynamic threshold calibration module. 
A variant without this module is compared with the full model on the same dataset. The results are 
shown in Table 3.

15

---

<!-- PAGE 16 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

Table 3. Effect of dynamic threshold calibration

Model

TA-IFDC

TA-IFDC (w/o DynThreshold)

Precision

Recall

F1

0.936

0.871

0.918

0.835

0.927

0.852

AUC

0.974

0.923

Latency (ms)

29

31

We ablate the calibration loop and compare the variant with the full model on IEEE-CIS (Fig. 
3a–b; Table 3). Recall drops from 0.918 to 0.835 and F1 from 0.927 to 0.852, while latency stays 
within 29–31 ms.

Figure 3. Effect of dynamic threshold calibration on IEEE-CIS

Removing the dynamic threshold module leads to significant performance degradation across 
all metrics, particularly recall. This confirms that fixed-threshold approaches are less effective in 
adapting to evolving transaction distributions. Dynamic calibration enables more flexible anomaly 
decision-making and enhances robustness.

The third experiment analyzes the impact of removing the temporal attention mechanism. Table

4 presents results with and without attention layers on PaySim data.

Table 4. Impact of temporal attention mechanism

Model

Precision

Recall

TA-IFDC

TA-IFDC (w/o Attention)

0.918

0.877

0.904

0.848

F1

0.911

0.862

AUC

0.968

0.938

Latency (ms)

28

29

Performance drops are notable, especially in recall and AUC. Attention mechanisms enhance the 
model’s sensitivity to temporal context, allowing it to better capture sequences of small anomalies 
which may appear benign in isolation but are indicative of fraud in context.

Figure 4 shows the performance of two versions of the TA-IFDC model on the PaySim dataset. 
The blue line represents the version with temporal attention, which has an AUC of 0.968. The red 
dashed line is the model without attention, which scored an AUC of 0.938. The gray dashed line 
marks the baseline for a random classifier, at 0.5 AUC. As you can see, adding temporal attention

16

---

<!-- PAGE 17 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

boosts  the  model's  performance,  especially  in  catching  small  anomalies  that  might  otherwise  be 
missed. This suggests that keeping track of time-based patterns helps the model better spot fraudulent 
behavior. Readability was improved by enlarging fonts and legend markers, offsetting overlapping 
points, and using a higher-contrast palette, so that ROC curves and model names remain legible even 
where lines intersect.

Figure 4. ROC Curve Comparison of TA-IFDC Models with and without Temporal Attention Mechanism

The fourth experiment evaluates robustness to concept drift using the SFD-FD dataset. Artificial 
behavioral changes are introduced at defined intervals to simulate evolving fraud patterns. Table 5 
reports F1-scores before and after drift events.

Table 5. Concept drift response (SFD-FD)

Model

TA-IFDC

Online-iForest

SSR-RVFL

F1 (Pre-drift)

F1 (Post-drift)

0.914

0.869

0.888

0.902

0.784

0.821

ΔF1

-0.012

-0.085

-0.067

TA-IFDC  demonstrates  superior  adaptability  to  evolving  patterns.  Its  feedback  and  adaptive 
thresholding mechanisms help mitigate abrupt distribution shifts. In contrast, static baselines suffer 
significant performance loss, underscoring the importance of real-time recalibration in fraud detection.
We tested TA-IFDC on the SFD-FD dataset to see how well it could handle changes in fraud 
patterns  over  time.  In  this  setup,  we  deliberately  altered  transaction  behavior  at  set  intervals  to 
simulate concept drift. Figure 5 shows the results: before the drift, TA-IFDC’s F1-score was 0.914, 
dropping  slightly  to  0.902  afterward.  By  contrast,  Online-iForest  fell  from  0.869  to  0.784,  and 
SSR-RVFL from 0.888 to 0.821. The much smaller drop for TA-IFDC (−0.012) suggests that its

17

---

<!-- PAGE 18 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

adaptive thresholding and feedback updates helped it maintain performance when the data distribution 
shifted.

Figure 5. Performance Comparison Before and After Concept Drift on the SFD-FD Dataset.

The  fifth  experiment  focuses  on  sliding  window-based  online  detection  using  the  BankSim 
dataset, which naturally supports stream processing. Table 6 reports average latency and F1 under 
three window sizes.

Table 6. Online window analysis (BankSim)

Window Size

TA-IFDC F1

Latency (ms)

Online-iForest F1

Latency (ms)

24h

48h

72h

0.909

0.912

0.905

26

29

31

0.846

0.842

0.834

21

23

25

TA-IFDC retains strong performance and acceptable latency across all windows. Online-iForest,

though faster, suffers in recall and general accuracy, particularly for longer transaction sequences.

In Figure 6, the performance of TA-IFDC and Online-iForest is compared under three sliding 
window settings using the BankSim dataset. TA-IFDC keeps its F1-score close to 0.91 across all 
windows, with latency rising slightly from 26 ms to 31 ms. Online-iForest processes marginally faster 
but shows a drop in accuracy, especially with longer windows, where its F1-score falls below 0.84.

18

---

<!-- PAGE 19 -->

Figure 6. F1-score and Latency Across Different Window Sizes on the BankSim Dataset.

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

The sixth experiment studies detection on minority class transactions using CCFD. Given its

severe imbalance, the focus is on F1-score for fraud cases. Results are shown in Table 7.

Table 7. Minority class detection (CCFD)

Model

TA-IFDC

SSR-RVFL

XGB-Anomaly

Precision

0.903

0.864

0.788

Recall

0.889

0.850

0.741

F1

0.896

0.857

0.764

The  results  show  that  TA-IFDC  maintains  high  performance  on  rare  fraud  instances,  where 
most models falter. This capability stems from its temporal modeling and calibration sensitivity to 
unusual transaction densities.

The seventh experiment explores cross-dataset generalization. Models trained on PaySim are

evaluated on CCFD without fine-tuning. Table 8 reports generalization scores.

Table 8. Cross-dataset generalization (Train: PaySim → Test: CCFD)

Model

TA-IFDC

SSR-RVFL

Online-iForest

F1

0.841

0.798

0.772

AUC

0.904

0.878

0.856

19

---

<!-- PAGE 20 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

TA-IFDC exhibits the best transferability, suggesting that its learning structure is less reliant 
on dataset-specific distributions. Its performance remains robust even when exposed to unfamiliar 
transaction patterns.

Figure 7 shows two evaluations involving the CCFD dataset. In the left panel, which focuses on 
minority class fraud detection, TA-IFDC records an F1-score of 0.896, ahead of SSR-RVFL (0.857) 
and XGB-Anomaly (0.764). The right panel presents a cross-dataset test, where models trained on 
PaySim are applied to CCFD without fine-tuning. Here, TA-IFDC again ranks highest, with an F1-score 
of 0.841 and an AUC of 0.904, indicating better adaptation to previously unseen transaction patterns.

Figure 7. Performance on Minority Class Detection and Cross-Dataset Generalization

The eighth and final experiment presents qualitative insights using two real transaction cases from 
IEEE-CIS. One case involves a high-value early morning transaction flagged only by TA-IFDC due 
to time-aware scoring. Another case, a legitimate charity transfer often misclassified by static models, 
was correctly identified as normal by TA-IFDC after feedback adjustment. These examples illustrate 
the model’s interpretability and practical reliability in real-world settings. Two additional narratives 
illustrate practical interpretability. (i) In PaySim, a sequence of small transfers spaced only minutes 
apart but executed from different devices was flagged solely through the temporal-attention layer. (ii) 
In BankSim, repeated withdrawals looked routine in isolation but revealed a suspicious rhythm when 
aggregated over a day. These cases highlight how temporal context helps analysts connect scattered 
clues that static models would overlook.

6. DISCUSSION

This study introduces a TA-IFDC, specifically designed for real-time financial fraud detection 
on digital payment platforms. The findings demonstrate the viability of this approach in overcoming 
several limitations observed in prior work, particularly those relying on static thresholds, heuristic 
post-processing, or single-modality models. Compared to widely used methods such as Online-iForest, 
GNN-based detection models, and SSR-RVFL, TA-IFDC consistently achieves superior results across 
multiple datasets, including IEEE-CIS, PaySim, CCFD, SFD-FD, and BankSim, as demonstrated 
through precision, recall, F1-score, AUC, and latency analyses.

In relation to previous research, much of the existing literature has acknowledged the importance 
of IF as an efficient anomaly detection method, particularly for its unsupervised nature and capacity 
to  handle  large-scale  datasets  with  high-dimensional  sparse  features.  However,  prior  IF-based 
applications often applied a fixed global threshold or required manual tuning, which can be suboptimal 
under dynamic transaction environments. What this work adds to the literature is the integration of a

20

---

<!-- PAGE 21 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

feedback-informed dynamic calibration mechanism, which adaptively adjusts the decision threshold 
in response to real-time transaction distributions. This dynamic calibration mechanism is further 
augmented by temporal attention modeling, which captures transaction sequencing patterns without 
requiring explicit supervision. Both components, when analyzed through ablation experiments, are 
shown to contribute significantly to model robustness, especially under concept drift and streaming 
conditions.

One notable insight from this research is the model’s ability to retain strong performance not 
only on traditional benchmark datasets like CCFD, but also under simulated real-world changes, 
such as evolving fraud tactics and delayed feedback in user behavior (as modeled via SFD-FD and 
BankSim). This reinforces the notion that static anomaly detection pipelines, though interpretable, 
lack the flexibility needed in production-grade fraud monitoring systems. Moreover, while existing 
hybrid or deep learning-based methods (e.g., Hybrid-AI-FD or GNN-IF) demonstrate good recall, 
they typically suffer from latency issues, making them less viable for high-frequency transaction 
systems. In contrast, TA-IFDC presents a practical compromise, offering high responsiveness with 
negligible latency cost. Operational overhead remains modest—less than 8% CPU above a static IF 
pipeline—while sustaining approximately 25–30k transactions per second on standard CPUs. GPU 
acceleration is optional. Energy consumption stays below 0.5 Wh per 1 k transactions. By stabilizing 
alert volumes, TA-IFDC reduced manual review time by around 12% in pilot replay.

Despite these strengths, the study also reveals several limitations. First, while the model performs 
well across all datasets, its efficacy may still depend on the availability of transaction timestamps 
and partial temporal continuity. In legacy banking infrastructures, where data logging practices may 
be inconsistent or constrained by outdated systems, deploying the proposed framework can present 
practical difficulties. Such environments often lack the granularity or continuity in transaction records 
that the model implicitly assumes, potentially reducing the reliability of anomaly scoring. Moreover, 
although the feedback module does improve adaptability in changing fraud landscapes, its current 
design relies primarily on a soft adjustment of decision thresholds derived from patterns of historical 
model consensus. This means that direct, high-quality supervisory signals—such as confirmed fraud 
annotations from domain experts or real-time user reports—are not yet part of the recalibration process. 
We’ve noticed that when feedback signals dry up—for example, when labels are extremely scarce—the 
system doesn’t completely break. It falls back to using only the scoring trend to adjust its thresholds 
gradually, which avoids any sudden spikes in alert volume. That said, this fallback mode isn’t perfect: 
over time, recall tends to slide a bit. Still, the system keeps things stable enough without triggering too 
many false alarms. In future work, it would make sense to fold in some semi-supervised methods or 
even light-touch user feedback. That way, even partial confirmations could help the model recalibrate 
faster. Interestingly, in our tests, just a few validated cases were enough to bring the thresholds back 
into balance within a handful of cycles—no manual tuning required.

When we looked across all six baselines, TA-IFDC didn’t just come out ahead on the numbers—it 
also highlighted something that’s often overlooked: how much the threshold matters. In a lot of older 
systems, thresholds were either hand-picked or barely tuned, almost like an afterthought. But here, 
adjusting them dynamically had a huge impact. It helped us cut down false positives, which in real 
ops means fewer wasted analyst hours and less risk of flagging good users—or worse, missing fraud 
that matters. That’s not just a minor tweak; it suggests thresholding deserves to be treated as part of 
the model design, not a bolt-on at the end.

Once we made calibration adaptive, it blurred the line between model training and live deployment. 
The threshold became something that moves with the stream, not something frozen at launch. When 
patterns shift—say, a holiday rush or a new promo changes user behavior—the system adjusts the 
boundary on its own, staying within limits like alert caps and stability guards. On a real-time pipeline 
where every millisecond counts, that makes a difference. It can mean the difference between catching 
fraud early or catching up after losses hit.

21

---

<!-- PAGE 22 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

So  rather  than  separating  the  model  and  the  calibration  logic,  we  treated  them  as  one.  The 
threshold updates with the same temporal cues that feed the model. We made sure the scores remain 
interpretable, which matters for audit, and kept the adaptation traceable. In short, we ended up with 
something we can actually deploy: it adapts when needed, stays within operational bounds, and avoids 
surprises for both fraud teams and risk officers.

7. CONCLUSION

TA-IFDC extends the basic Isolation Forest by adding two pieces that real systems often need. 
One is a feedback loop that keeps the decision threshold in sync with the current score distribution 
instead of letting it drift. The other is a temporal-attention block that captures short-term timing 
patterns—because, in practice, coordinated fraud tends to show up in bursts, not as isolated points. 
Together they fix two common problems we’ve seen again and again: thresholds that get stuck on 
old data, and models that ignore when things happen.

This built-in adaptation also changes how training and deployment connect. The model isn’t a 
“train-once-and-ship” artifact anymore. Under a prequential setup, the threshold moves with the stream, 
adjusting for seasonal swings, policy shifts, or class-prior changes without retraining everything from 
scratch. On payment systems that run under millisecond deadlines, that alone cuts the detection delay 
for fraud rings that would otherwise slip through.

In use, the model reads events in context rather than as isolated spikes. The attention layer learns 
timing cues, while the Isolation Forest handles the point-level anomaly scoring. Across five public 
datasets—IEEE-CIS, PaySim, CCFD, SFD-FD, and BankSim—we saw consistent gains in recall 
and F1, while latency stayed flat at around 35 ms per record (P95). In live terms, that means better 
coverage without slowing down the decision path, which matters far more than squeezing out another 
fraction of a point on an offline benchmark.

Operationally, the design stays modular. TA-IFDC fits into risk engines that already produce 
probabilistic anomaly scores or mix unsupervised layers with case queues. Calibration runs online 
against the evolving score distribution and uses delayed confirmations when available; boundary 
moves are time-stamped and logged so model-risk teams can audit changes and align operating points 
with alert budgets and reviewer capacity.

There are caveats. Continuous, time-stamped streams are assumed; legacy stacks with coarse 
or  asynchronous  logging  may  need  ordering  and  clock-alignment  shims.  The  current  calibration 
loop leans on model-derived agreement signals; bringing in external feedback—analyst decisions, 
customer reports, inter-bank intelligence—should help under extreme imbalance, though privacy and 
integration constraints must be handled.

Two extensions are natural. Multimodal signals (device fingerprints, coarse geolocation, step-up 
outcomes) can sharpen early screening, and federated training would let institutions adapt thresholds 
locally while preserving data sovereignty. One thing that could make the system easier to trust is a 
simple, human-readable note explaining why a threshold changed — something analysts can glance 
at before digging deeper. In the next round of work, we plan to bring in more signal types: device 
fingerprints, rough location data, and basic behavioral biometrics to add richer timing context. The 
challenge will be to fuse those sources without adding lag. Keeping the tail latency low while mixing 
different data streams is tricky, but that’s where most of the deployment work will probably focus next.
By dropping the fixed threshold and adding a sense of timing, the Isolation Forest turns from a 
static scoring tool into something you can actually run in production. It keeps its accuracy even when 
data drifts, reacts fast enough to meet real-time limits, and leaves a clear trail for audits. In short, it 
bridges a piece of the gap between models that sit on paper and the messy, shifting reality of fraud 
in live payment systems.

22

---

<!-- PAGE 23 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

FUNDING STATEMENT

This research was funded by the Key Project of Scientific Research Plan of Universities of Anhui 
Province (Humanities and Social Sciences) “Research on high-quality development Mechanism and 
Path of innovative SMEs in Anhui Province (2024AH052558)”; and the Key Research Project of 
Anhui Xinhua University “Investigation of the Policies of Anhui Province to Support the High-quality 
development the Innovative SMEs(2023rw001)

CONFLICTS OF INTEREST

We wish to confirm that there are no known conflicts of interest associated with this publication 
and there has been no significant financial support for this work that could have influenced its outcome.

CORRESPONDING AUTHOR

Correspondence should be addressed to Ping Zhou: zhouping0118@ 126 .com

23

---

<!-- PAGE 24 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

REFERENCES

Al Farizi, W. S., Hidayah, I., & Rizal, M. N. (2021). Isolation forest based anomaly detection: A systematic 
literature  review.  2021  8th  International  Conference  on  Information  Technology,  Computer  and  Electrical 
Engineering (ICITACEE) (pp. 118-122), IEEE.

Al Lawati, H. M., Zainal, A., Al-Rimy, B. A. S., Al-Azawi, M., Kassim, M. N., Almalki, S. A., & Alghamdi, 
T. A. (2025). An Integrated Preprocessing and Drift Detection Approach With Adaptive Windowing For Fraud 
Detection In Payment Systems (February 2025). IEEE Access : Practical Innovations, Open Solutions.

Ali, A., Abd Razak, S., Othman, S. H., Eisa, T. A. E., Al-Dhaqm, A., Nasser, M., Elhassan, T., Elshafie, H., & 
Saif, A. (2022). Financial fraud detection based on machine learning: A systematic literature review. Applied 
Sciences (Basel, Switzerland), 12(19), 9637. DOI: 10.3390/app12199637

Almazroi, A. A., & Ayub, N. (2023). Online payment fraud detection model using machine learning techniques. 
IEEE Access : Practical Innovations, Open Solutions, 11, 137188–137203. DOI: 10.1109/ACCESS.2023.3339226

Attar, A. A., Bao, K., Hagenmeyer, V., Fabarisov, T., & Morozov, A. (2024). Improving Anomaly Detection 
with Adaptive Dynamic Threshold: A Review and Enhanced Method. 2024 8th International Conference on 
System Reliability and Safety (ICSRS) (pp. 662-666), IEEE.

Bello, H. O., Ige, A. B., & Ameyaw, M. N. (2024). Adaptive machine learning models: Concepts for real-time 
financial fraud prevention in dynamic environments. World Journal of Advanced Engineering Technology and 
Sciences, 12(2), 21-34.

Chen,  T.,  &  Tsourakakis,  C.  (2022).  Antibenford  subgraphs:  Unsupervised  anomaly  detection  in  financial 
networks. Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (pp. 
2762-2770) DOI: 10.1145/3534678.3539100

Du, P., & Shu, H. (2022). Exploration of financial market credit scoring and risk management and prediction 
using  deep  learning  and  bionic  algorithm.  Journal  of  Global  Information  Management,  30(9),  1–29.  DOI: 
10.4018/JGIM.293286

Eswar Prasad, G., Hemanth Kumar, G., Venkata Nagesh, B., Manikanth, S., & Kiran, P. (2023). Enhancing 
Performance of Financial Fraud Detection Through Machine Learning Model. J Contemp Edu Theo Artific 
Intel: JCETAI-101.

Fatlawi, H. K. (2025). Enhanced Fraudulent Detection Using Isolation Forest and Multi-Cluster Deep Learning. 
Journal of Al-Qadisiyah for Computer Science and Mathematics, 17(1), 72–80.

Hernandez Aros, L., Bustamante Molano, L. X., Gutierrez-Portela, F., Moreno Hernandez, J. J., & Rodríguez 
Barrero, M. S. (2024). Financial fraud detection through the application of machine learning techniques: A 
literature review. Humanities & Social Sciences Communications, 11(1), 1–22. DOI: 10.1057/s41599-024-03606-0

Hilal, W., Gadsden, S. A., & Yawney, J. (2022). Financial fraud: A review of anomaly detection techniques and 
recent advances. Expert Systems with Applications, 193, 116429. DOI: 10.1016/j.eswa.2021.116429

Immadisetty, A. (2025). Real-time fraud detection using streaming data in financial transactions. [JRTCSE]. 
Journal of Recent Trends in Computer Science and Engineering, 13(1), 66–76. DOI: 10.70589/JRTCSE.2025.13.1.9

Janjua, A. N., Abdulraheem, A., & Tariq, Z. (2024). Big Data Analysis Using Unsupervised Machine Learning: 
K-means Clustering and Isolation Forest Models for Efficient Anomaly Detection and Removal in Complex 
Lithologies. International Petroleum Technology Conference (pp. IPTC-23580-EA), IPTC.

Kamuangu, P. (2024). A review on financial fraud detection using ai and machine learning. Journal of Economics, 
Finance, and Accounting Studies, 6(1), 67–77. DOI: 10.32996/jefas.2024.6.1.7

Kareem,  M.  S.,  &  Muhammed,  L.  A.  (2024).  Anomaly  detection  in  streaming  data  using  isolation  forest. 
2024 Seventh International Women in Data Science Conference at Prince Sultan University (WiDS PSU) (pp. 
223-228), IEEE.

Kim,  H.,  Lee,  B.  S.,  Shin,  W.-Y.,  &  Lim,  S.  (2022).  Graph  anomaly  detection  with  graph  neural  networks: 
Current status and challenges. IEEE Access : Practical Innovations, Open Solutions, 10, 111820–111829. DOI: 
10.1109/ACCESS.2022.3211306

24

---

<!-- PAGE 25 -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025

Koziara, M., & Karczmarek, P. (2022). On a combination of clustering methods and isolation forest. International 
Conference on Artificial Intelligence and Soft Computing, (pp. 114-126), Springer.

Lam, H. Y. J. (2025). Reducing Fraud with Anomaly Detection Algorithms. Journal of Financial Technology, 
22(4), 231–245.

Leveni, F., Cassales, G. W., Pfahringer, B., Bifet, A., & Boracchi, G. (2025). Online isolation forest. arXiv 
preprint arXiv:2505.09593.

Lin, C., Du, B., Sun, L., & Li, L. (2024). Hierarchical context representation and self-adaptive thresholding for 
multivariate anomaly detection. IEEE Transactions on Knowledge and Data Engineering, 36(7), 3139–3150. 
DOI: 10.1109/TKDE.2024.3360640

Mazumder, M. T. R., Shourov, M. S. H., Rasul, I., Akter, S., & Miah, M. K. (2025). Anomaly Detection in 
Financial Transactions Using Convolutional Neural Networks. Journal of Economics. Finance and Accounting 
Studies, 7(2), 195–207.

Núñez Delafuente, H., Astudillo, C. A., & Díaz, D. (2024). Ensemble approach using k-partitioned isolation 
forests for the detection of stock market manipulation. Mathematics, 12(9), 1336. DOI: 10.3390/math12091336

Quan, C., Yuan, Y.-H., Wang, G., & Wu, H.-T. (2024). Optimization of Enterprise Financial Risk Management 
and Crisis Early Warning System Supported by AI. Journal of Global Information Management, 32(1), 1–21. 
DOI: 10.4018/JGIM.356490

Shanaa, M., & Abdallah, S. (2025). A hybrid anomaly detection framework combining supervised and unsupervised 
learning for credit card fraud detection. F1000 Research, 14, 664. DOI: 10.12688/f1000research.166350.1

Sonani,  R.,  &  Govindarajan,  V.  (2022).  A  Hybrid  Cloud-Integrated  Autoencoder-GNN  Architecture  for 
Adaptive, High-Dimensional Anomaly Detection in US Financial Services Compliance Monitoring. Spectrum 
of Research, 2(1).

Tchuente,  D.  (2022).  User  modeling  and  profiling  in  information  systems:  A  bibliometric  study  and  future 
research directions. Journal of Global Information Management, 30(1), 1–25. DOI: 10.4018/JGIM.307116

Tokovarov, M., & Karczmarek, P. (2022). A probabilistic generalization of isolation forest. Information Sciences, 
584, 433–449. DOI: 10.1016/j.ins.2021.10.075

Vanini, P., Rossi, S., Zvizdic, E., & Domenig, T. (2023). Online payment fraud: From anomaly detection to risk 
management. Financial Innovation, 9(1), 66. DOI: 10.1186/s40854-023-00470-w

Wang, J., Liu, J., Pu, J., Yang, Q., Miao, Z., Gao, J., & Song, Y. (2023). An anomaly prediction framework for 
financial IT systems using hybrid machine learning methods. Journal of Ambient Intelligence and Humanized 
Computing, 14(11), 15277–15286. DOI: 10.1007/s12652-019-01645-z

Zhang, H., Jia, X., & Chen, C. (2025). Deep Learning-Based Real-Time Data Quality Assessment and Anomaly 
Detection for Large-Scale Distributed Data Streams. International Journal of Medical and All Body Health 
Research, 6(1), 1.01-11.

Zhang, L., Xuan, Y., Liu, Z., Du, Z., Wang, S., & Wang, J. (2025). A hybrid ensemble model to detect Bitcoin 
fraudulent  transactions.  Engineering  Applications  of  Artificial  Intelligence,  141,  109810.  DOI:  10.1016/j.
engappai.2024.109810

Zhang, W., Xu, Y., Zheng, H., & Li, L. (2022). Verbal vs. Nonverbal Cues in Static and Dynamic Contexts of 
Fraud Detection in Crowdsourcing: A Comparative Study. Journal of Global Information Management, 30(1), 
1–28. DOI: 10.4018/JGIM.310928

Zheng,  Z.,  Zhou,  B.,  &  Song,  Y.  (2025).  Temporal-Aware  Graph  Attention  Network  for  Cryptocurrency 
Transaction Fraud Detection. arXiv preprint arXiv:2506.21382.

25

---

<!-- PAGE 26 -->

Reproduced with permission of copyright owner. Further

reproduction prohibited without permission.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
Dynamic Calibration of Decision
Thresholds for Financial
Anomaly Detection:
Verification With Payment Platform
Information and Data
Anzhong Huang Xin Zhang
School of Economics and Management, Jiangsu University Graduate School of Business Administration, Wonkwang
of Science and Technology, China University, South Korea
Yuanyuan Wang Sangbing Tsai
https://o rcid .org/ 0009 -0006 -8455 -6402 https://o rcid .org/ 0000 -0001 -6988 -5829
School of Economics and Management, Jiangsu University International Engineering and Technology Institute, Hong
of Science and Technology, China Kong
Ping Zhou Lin Chen
https://o rcid .org/ 0009 -0006 -3538 -1861 School of Digital Economy and Trade, Wenzhou
School of Accounting and Finance, Anhui Xinhua Polytechnic, China
University, China
Received: September 7th, 2025 | Accepted: December 1st, 2025
ABSTRACT
Digital payment channels have expanded quickly, reshaping transaction flows while opening new
avenues for fraud. Isolation Forest (IF) remains attractive for unsupervised screening, yet deployments
that rely on a fixed anomaly-score threshold deteriorate when traffic shifts or is actively manipulated.
The authors present a Temporal-Attention Isolation Forest with Dynamic Calibration (TA-IFDC) that
treats threshold selection as an adaptive component rather than a static post-processing step. The
method monitors the evolving distribution of IF scores in streaming mode and updates the decision
boundary online, while a lightweight temporal-attention module encodes short-range dependencies
across consecutive transactions. Together, these pieces allow the detector to adjust to drift without
sacrificing precision during stable periods.
KEYWORDS
Financial Transaction Security, Isolation Forest, Adaptive Decision Threshold, Temporal Dependency Modeling,
Real-Time Fraud Analytics
1. INTRODUCTION
Over the last decade, the accelerating expansion of digital financial services has altered the
fundamental architecture of global payment systems. Mobile banking applications, instant online
transfers, and integrated e-wallet ecosystems have rapidly displaced traditional cash and card-based
DOI: 10.4018/JGIM.395852
This article published as an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creative-
commons.org/licenses/by/4.0/) which permits unrestricted use, distribution, and production in any medium, provided the author of the
original work and original publication source are properly credited.
1

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
transactions, creating a financial environment that is faster, more accessible, and highly interconnected.
This transformation has yielded substantial benefits in terms of operational efficiency and user
convenience; however, it has also brought about a new spectrum of security vulnerabilities that
financial institutions must confront. Recent statistical surveys place the total global losses attributed
to payment fraud at more than USD 45 billion in 2022, with forecasts indicating a continued upward
trajectory as illicit actors incorporate automation, large-scale botnets, and adversarial machine learning
into their operations. Market analyses further note that fraud patterns are becoming increasingly
fragmented and adaptive, making the early detection of suspicious transactions a more complex task
than ever before (Zhang et al., 2022).
The emergence of such high-frequency and high-value fraudulent transactions underscores the
necessity for monitoring systems capable of functioning effectively under volatile, non-stationary data
conditions. Modern fraud detection commonly relies on anomaly detection frameworks that assess
deviations from established transactional norms(Hernandez Aros et al., 2024). Unsupervised detectors
based on IF are widely used because they run fast on large datasets and do not rely on labels (Janjua et
al., 2024; Kareem & Muhammed, 2024). IF builds random partition trees by choosing attributes and
split values at random. Points that depart from the bulk are isolated in only a few splits, so their path
lengths are short. In practice, this behavior makes IF a good fit for catching rare but consequential
events in high-dimensional data without costly annotation.
Experience with IF in production exposes a weak spot: decisions usually depend on a fixed
score cutoff set during an initial calibration or chosen heuristically, then left in place. Real payment
traffic does not sit still—seasonal campaigns, macro shifts, and coordinated rings all move the score
distribution (Sonani & Govindarajan, 2022). A static line can flood reviewers during benign surges
or miss gradual shifts that matter; both outcomes degrade performance.
Streaming tightens the constraints. Each transaction must be scored in milliseconds, while
labels often arrive late or not at all(Vanini et al., 2023). The detector acts under uncertainty as the
score distribution drifts, and a fixed threshold cannot follow that movement. Deeper models and
feature tweaks help, but a robust, feedback-aware way to adjust cutoffs in unsupervised settings is
still underexplored.
To address this, we introduce TA-IFDC and treat thresholding and temporal context as core
parts of the detector (Attar et al., 2024). A dynamic calibration step updates the decision boundary
online using recent score statistics and delayed outcomes, keeping alert rates stable while tracking
distribution change (Al Lawati et al., 2025; Lin et al., 2024). A lightweight temporal component
encodes short-range dependencies—inter-arrival times and simple session cues—so scores reflect
what just happened rather than judging each record in isolation (Zheng et al., 2025).
We evaluate the framework on five payment datasets—IEEE-CIS, PaySim, CCFD, SFD-FD, and
BankSim—against six competitive baselines. We report precision, recall, F1, AUC, and per-transaction
latency under streaming protocols that preserve order, inject drift, and delay labels to mirror practical
deployment.
Together, adaptive thresholding and temporal context close the gap between raw anomaly scores
and real-time decisions in payment systems, yielding consistent gains while meeting the latency
constraints of high-throughput gateways.
By coupling adaptive thresholding with temporal sequence modeling, TA-IFDC bridges a
critical gap between raw anomaly scoring and real-time decision-making in financial fraud detection
systems. (Tchuente, 2022) The results not only demonstrate the framework’s ability to deliver
consistent performance gains across multiple datasets but also highlight its suitability for deployment
in high-throughput payment platforms where both fraud patterns and data distributions can change
rapidly. This combination of operational adaptability and computational efficiency positions TA-IFDC
as a promising candidate for next-generation fraud detection infrastructure in the financial sector
(Bello et al., 2024; Fatlawi, 2025).
The primary contributions of this work are summarized as follows:
2

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
(1) A dynamic threshold calibration mechanism is proposed, enabling IF to operate adaptively in
non-stationary data environments without external supervision;
(2) A temporal attention module is introduced to model inter-transaction dependencies, improving
detection accuracy for sequential or contextual anomalies(Tokovarov & Karczmarek, 2022);
(3) A unified detection framework—TA-IFDC—is constructed and evaluated across multiple real
and synthetic payment datasets, demonstrating consistent improvements in accuracy, robustness,
and latency over baseline models;
(4) Extensive experiments and ablation studies provide insight into the behavior of dynamic
calibration mechanisms and the value of temporal modeling under streaming and drifting
conditions.
The remainder of this paper is structured as follows. Section 2 presents a review of related work
in fraud detection, threshold calibration, and time-aware anomaly modeling. Section 3 describes
the architecture and core components of the proposed TA-IFDC framework. Section 4 details the
experimental setup, including datasets, evaluation metrics, and baseline configurations. Section 5
presents and interprets the experimental results. Section 6 discusses the research findings, limitations,
and implications. Finally, Section 7 concludes the paper and outlines directions for future work.
2. RELATED WORK
The increasing reliance on unsupervised anomaly detection techniques in the financial domain
has drawn extensive attention to IF and its variants. Originally proposed by Liu et al., the IF
algorithm isolates observations by randomly selecting features and split values, under the assumption
that anomalies are more susceptible to early isolation(Al Farizi et al., 2021; Hilal et al., 2022;
Immadisetty, 2025). Its efficiency and effectiveness have rendered it a foundational tool in large-scale
and high-dimensional fraud detection tasks. However, the original IF model lacks adaptability to
time-varying data patterns and fails to incorporate contextual or sequential transaction information,
which are prevalent in financial fraud scenarios(Ali et al., 2022; Du & Shu, 2022; Kamuangu, 2024;
Quan et al., 2024).
Efforts to overcome the inherent limitations of the IF algorithm have taken many forms, though
the core motivation remains the same: improve adaptability without sacrificing interpretability(Lam,
2025; Shanaa & Abdallah, 2025; Wang et al., 2023). Early adaptations for streaming data, typified
by the Online-iForest approach, allowed incremental updates to the ensemble of trees, enabling the
model to handle new transactions as they arrive(Immadisetty, 2025; Leveni et al., 2025). This shift
from batch processing to a more fluid, real-time structure was a practical leap for high-frequency
domains such as payment platforms. Other lines of work explored hybrid architectures that combine IF
with ensemble classifiers or incorporate domain-specific engineered features to boost discrimination
accuracy, particularly in noisy, high-dimensional datasets(Koziara & Karczmarek, 2022; Núñez
Delafuente et al., 2024; L. Zhang et al., 2025). More recently, graph-based formulations—exemplified
by GNN-IF—embed transaction records into account–entity graphs, capturing relational signals that
tree models in isolation would overlook(Chen & Tsourakakis, 2022; Kim et al., 2022). While these
methods offer structural flexibility or richer representation learning, they still inherit the same fixed
thresholding mechanism as the vanilla IF, which inevitably curtails responsiveness when fraud patterns
shift unexpectedly. This is a notable bottleneck, especially in adversarial settings where attackers
deliberately exploit static detection boundaries.
Calibrating decision thresholds remains underexplored relative to model design in anomaly
detection. In many mature pipelines, the anomaly score is mapped to a decision through a single
operating point chosen at launch and rarely revisited. Under non-stationary traffic, that practice is
brittle: concept drift, class-prior shift, and seasonal volume swings push the score distribution away
from the original calibration, tilting the false-positive/false-negative mix. In financial settings the
3

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
asymmetry is costly—missed fraud yields direct loss, while excessive alerts erode reviewer trust and
inflate operational budgets. Recent work on adaptive thresholding has opened up useful directions,
particularly in situations where labels arrive late or sparsely, and batch evaluation isn't feasible. Many
systems rely on simple rules—rolling quantiles, for example—to keep the decision boundary in sync
with shifting score distributions, while others incorporate feedback from downstream performance,
nudging thresholds over time to maintain a reasonable precision–recall balance. There’s also a stream
of research that treats thresholding as a policy problem, often applying reinforcement learning to
track evolving attacker behavior. However, in practice, two issues tend to surface. First, when the
data distribution is heavy-tailed or the traffic arrives in bursts, naïve update windows can behave
erratically, producing unstable alert patterns. Second, most of these approaches still assume access to
trustworthy labels, which are often unreliable or delayed in real-world environments. Tools like Platt
scaling or isotonic regression help calibrate probabilities, but they don’t solve the problem of where to
actually place the operating point. So while adaptive strategies show potential, especially in dynamic
or semi-supervised settings, their practical value is still constrained by label availability. In these cases,
approaches that combine anomaly scoring with lightweight, feedback-tolerant calibration—without
relying heavily on labels—remain highly relevant. A related line of work frames threshold control
as a learning policy, often via reinforcement learning (RL). Such methods tune a reward reflecting
precision–recall trade-offs and adapt under drift, but they depend on frequent, high-quality feedback—
rare in production payment streams. TA-IFDC instead calibrates from score distributions and sparse,
delayed outcomes, achieving responsiveness without a heavy supervision loop.
In practical financial environments, anomaly detection systems are required to cope with a wide
spectrum of transaction types, the continual emergence of new fraud strategies, and the inherent
variability of streaming data(Eswar Prasad et al., 2023; H. Zhang et al., 2025). Scholars have examined
a range of detection paradigms, from supervised models—such as gradient-boosted decision trees
(e.g., XGBoost), deep architectures like autoencoders, to hybrid frameworks that merge clustering
outputs with classification layers—to address these challenges(Almazroi & Ayub, 2023; Mazumder
et al., 2025). Although supervised learning methods can deliver strong accuracy when abundant
annotated data are available, their dependence on up-to-date labels often limits their flexibility and
long-term maintainability once deployed. On the other hand, unsupervised approaches, including
Isolation Forest, one-class Support Vector Machines (SVM), and various clustering schemes, avoid the
label dependency and thus can be applied more broadly across heterogeneous datasets. Nevertheless,
these methods frequently encounter difficulties in providing transparent decision logic and in setting
decision thresholds that remain effective under shifting data distributions. The datasets most commonly
used for evaluation include the IEEE-CIS Fraud Detection Dataset, PaySim, the CCFD dataset, and
BankSim. Each dataset presents unique characteristics—ranging from anonymized features and class
imbalance to temporal drift and behavior simulation—requiring detection frameworks to be robust
across multiple conditions.
Compared with existing approaches, the method proposed in this paper distinguishes itself
through its integration of dynamic threshold calibration with an unsupervised anomaly detection
backbone. Rather than designing new feature representations or model architectures, this study
focuses on the often-overlooked thresholding component and enhances it with a feedback-informed
and context-aware strategy. The TA-IFDC framework combines a temporal attention mechanism with
an adaptive calibration module, allowing the model to respond dynamically to score fluctuations and
transaction context. This design improves anomaly interpretability, reduces false alarms, and preserves
the unsupervised nature of IF-based models, making it more suitable for real-world deployment where
labeled data are sparse and latency constraints are strict.
In summary, while previous studies have improved various facets of anomaly detection models—
such as feature representation, network architecture, or data stream handling—few have systematically
addressed the calibration challenge within unsupervised fraud detection frameworks. This study aims
4

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
to fill that gap by introducing a threshold adaptation mechanism that complements the strengths of
IF, while enhancing temporal responsiveness and practical applicability.
3. PROPOSED METHOD: TA-IFDC
We propose a novel anomaly detection framework named TA-IFDC, designed to enhance the
performance of IF through adaptive threshold adjustment and temporal-context modeling. This section
details the system architecture, the role of each component, and the mathematical formulation of
the algorithm.
3.1 Overview of TA-IFDC
The TA-IFDC framework is designed with four major components:
1. Sliding Window Preprocessing for temporal transaction segmentation;
2. Temporal Attention Encoder, which captures transaction time patterns and user behavior drift;
3. IF Scoring, responsible for initial anomaly detection;
4. Dynamic Threshold Calibration Module, which adaptively adjusts the decision boundary based
on recent detection performance.
A high-level schematic of the method is shown in Fig 1 .
Figure 1. Overview of the main processing stages in TA-IFDC
5

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
3.2 Sliding Window-Based Transaction Segmentation
To enable temporal modeling and online threshold calibration, transaction data is divided into
overlapping windows.
Let the incoming transaction stream be denoted as:
 𝒯 = {      x    ,  x    , … ,  x     }   ,  x     ∈  ℝ   d
| 1 2 | N i |     |
| --- | --- | --- |
where x represents a single transaction with d features.
i
We construct a sliding window of size W, with stride S, resulting in a sequence of windows:
|   𝒲     =   {   x    , … ,  x   |    }   , k = 1, … , K  |     |
| ------------------------------- | ---------------------- | --- |
| k kS                            | kS+W−1                 |     |
This segmentation supports online model updates and threshold adaptation.
3.3 Temporal Attention Encoder
To capture periodic patterns and behavior drift, we embed a temporal attention mechanism that
computes the temporal relevance of each transaction within a window.
Let:
| •    X     = [     x     , … ,  x   |    ]     denote the feature matrix of window   𝒲      |     |
| ----------------------------------- | ----------------------------------------------------- | --- |
| k k,1                               | k,W                                                   | k   |
  T     =   [   t     , … ,  t
| •     |    ]     denote the corresponding time-stamps |     |
| ----- | --------------------------------------------- | --- |
| k k,1 | k,W                                           |     |
We define time encoding vectors   e      = ϕ(     t     )    ∈  ℝ   h  , where 𝜙(∙)canbeaFourier-basedpositional
k,j k,j
encoding or learned embedding.
Each transaction is transformed into:
| x    ˜         = concat(     x   |   ,  e      )      |     |
| -------------------------------- | ------------------ | --- |
| k,j                              | k,j k,j            |     |
We then compute attention scores using scaled dot-product attention:
_
| e x p  (      q i  ⊤       k j       /  √                |   d k        )         |     |
| -------------------------------------------------------- | ---------------------- | --- |
|   α       =  _                                           | _                      |     |
| i j  ∑   W        e x p   (      q i   ⊤       k l     / |  √     d k       )     |     |
l = 1
where:
| •    q     =  W     x   ˜      |     is the query vector |     |
| ------------------------------ | ----------------------- | --- |
i Q k,i
| •    k     =  W     x   ˜      |     is the key vector |     |
| ------------------------------ | --------------------- | --- |
j K k,j
•  d is the dimension of keys
k
The attention-enhanced transaction vector becomes:
W
  z     = ∑         α     ⋅   (   W     x   ˜
|          |    )      |     |
| -------- | --------- | --- |
| i j=1 ij | V k,j     |     |
These contextual representations z are then passed to the IF model for scoring.
i
6

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
3.4 IF Scoring
The enhanced representations z are input into the IF to calculate anomaly scores.
i
IF relies on recursive partitioning. For each instance z, the anomaly score s(z) is computed as:
i i
s ( z ) = 2 −_ E( c h ( ( n z )i ) )
i
where:
• E(h(z \)) is the average path length of z in all trees
i i
• n is the subsample size used to build trees
• c(n) is the normalization factor:
c ( n ) = 2H( n − 1) − 2_ ( n n − 1)
and H(i) is the harmonic number:
H ( i ) = ln ( i ) + γ, γ ≈ 0.5772
A score close to 1 indicates high anomaly probability.
3.5 Dynamic Threshold Calibration
In traditional IF implementations, the decision threshold θ\theta is fixed, often determined by
cross-validation or empirical heuristics. However, under real-world financial settings, user behavior
patterns and transaction distributions can drift significantly over time, resulting in unstable detection
performance if the threshold remains static.
To address this, we design a Dynamic Threshold Calibration (DTC) module that adaptively
adjusts θ\theta for each sliding window using recent prediction feedback statistics.
3.5.1 Adaptive Threshold Update Rule
Let 𝒮 = { s , s , … , s } be the anomaly scores in window 𝒲 , and let θ be the calibrated
k 1 2 W k k
threshold at time step k. We define a percentile-based update rule with smoothing:
θ = ( 1 − λ) ⋅ θ + λ ⋅ Quantil e ( 𝒮 )
k k−1 β k
where:
• λ∈[0,1] is the learning rate (adaptivity coefficient),
• Quantile(∙)returns the β-th percentile of the scores (e.g., β=0.95 for top 5% anomaly),
β
• θ is initialized from the first window as baseline.
0
This rule smooths threshold changes to prevent instability due to local score fluctuations.
3.5.2 Feedback-Informed Calibration (Optional Enhancement)
When delayed ground truth labels are available (e.g., confirmed fraud), a feedback loop is used
to refine θ based on false positive and false negative counts.
k
Let:
7

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
• FP: false positives in 𝒲 ,
k k
• FN: false negatives,
k
• ∆θ: correction factor.
k
We define:
Δ θ k = η ⋅ ( α ⋅ _F W P k − ( 1 − α) ⋅ F_ W N k )
and update the threshold as: θ ← θ + Δ θ where:
k k k
• η is the feedback gain (tuning parameter),
• α∈[0,1] balances precision and recall.
This formulation penalizes overly aggressive thresholds (high FP) and overly conservative
thresholds (high FN), encouraging balance.
3.6 Overall Algorithm Description
The TA-IFDC framework is designed to perform real-time anomaly detection in financial
transaction streams, with particular emphasis on adaptability to evolving data distributions. It integrates
temporal behavior modeling, ensemble anomaly scoring, and an adaptive decision-making mechanism
to accommodate the non-stationary nature of payment systems.
Initially, the transaction stream is segmented using a sliding window approach. Each window
contains a sequence of temporally ordered transaction records, which serves as the processing unit
for detection. This segmentation enables localized modeling of user behavior and supports gradual
updates of the decision threshold over time.
For each window, temporal characteristics of transactions are encoded into fixed-length feature
representations. These time-sensitive features are derived using positional encoding techniques and
capture both the periodicity and recency of financial activities. To further enhance context-awareness,
a temporal attention mechanism is applied. The mechanism assigns varying degrees of importance
to transactions observed within a given time window, enabling the model to focus more on events
that carry greater behavioral significance, while downplaying patterns that contribute little to the
detection objective.
After temporal encoding, each transaction is processed through an ensemble of Isolation Trees,
which partition the feature space in a randomized manner. IF does not chase balanced splits. It
samples a feature and a cut at random at each node, and the isolation depth depends on how far the
transaction sits from the main mass. Transactions that deviate substantially from the bulk of data
are separated earlier, producing shorter path lengths and correspondingly higher anomaly scores. In
financial datasets, such cases often represent unusual spending bursts, irregular transfer patterns, or
atypical device usage, all of which warrant closer scrutiny. The unsupervised nature of this scoring
process is particularly important in fraud detection, where labeled anomalies are scarce, delayed, or
incomplete. Moreover, the low computational cost of Isolation Trees allows the method to scale to
millions of transactions per day without prohibitive infrastructure requirements.
Once the anomaly scores for a given observation window are available, they serve as the basis
for recalibrating the detection threshold. The TA-IFDC framework avoids the rigidity of static
thresholds by adopting a quantile-based dynamic calibration approach. In practical terms, this means
that the decision boundary at time t is updated by blending the previously applied threshold with
a high-percentile statistic—such as the 95th or 97th percentile—of the current score distribution.
The blend ratio controls how quickly the system reacts to abrupt changes, such as a sudden spike
in fraudulent activity following a phishing campaign. A purely percentile-based recalibration could
8

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
overreact to noise, while a purely historical threshold would be slow to adapt; the interpolation
mechanism balances these extremes, maintaining stability without sacrificing responsiveness.
Quantile selection was ablated across 90–99 percentiles. Below ~93% false positives surged; above
~97% recall fell sharply. We adopt 95% as a balanced operating point, with ±1–2% guardrails under
drift. To avoid overreaction, a hysteresis rule and adaptive smoothing cap limit per-window threshold
change to ≈2–3% of the prior value.
In operational settings, it is common for feedback on suspected transactions to arrive only after
several hours or even days, once investigations are complete. TA-IFDC is designed to incorporate such
delayed supervision when available. Specifically, the recalibration step introduces a correction term
proportional to the recent imbalance between false positives and false negatives. When false positives
rise, the threshold is nudged upward to protect analyst capacity. If post-review reveals missed fraud,
the threshold is lowered to recover recall. Updates use delayed labels when available and otherwise
rely on recent score dynamics, allowing the operating point to adapt under partial supervision typical
of large-scale payment streams.
After each threshold update, transactions in the active window are scored against the current
operating point. Records above the cutoff move to the risk controls. Depending on policy and traffic,
these controls may act automatically—short holds, step-up authentication, velocity caps—or hand the
case to investigators. TA-IFDC runs in mini-batch mode and in an online (prequential) loop, while
meeting real-time and accuracy requirements. When a window finishes, the pointer slides forward
and calibration continues on the next slice, letting the system keep pace with the stream.
Temporal feature encoding, context-aware attention, isolation-based scoring, and online threshold
calibration jointly counter concept drift and ongoing adversarial changes. Legitimate behavior swings
with sales, public events, and product launches; meanwhile, attackers keep changing tactics to slip
past static rules. By making calibration part of the design rather than a post-hoc tweak, TA-IFDC ties
score production to the decision rule and closes the long-standing gap between scoring and action.
The modules are small and loosely coupled, making integration with existing case-management and
risk-control systems straightforward.
We evaluate on five benchmarks—IEEE-CIS Fraud Detection, PaySim, CCFD, SFD-FD, and
BankSim—spanning real and simulated payment streams with varied class priors and feature sets.
We assess precision, recall, F1, AUC, per-record latency, and robustness under induced drift and
delayed feedback under constraints similar to production.
4. EXPERIMENTAL SETUP
We evaluate TA-IFDC under conditions close to our target deployment. The focus is on
behaviors that matter in practice. We use five benchmarks—IEEE-CIS, PaySim, CCFD, SFD-FD,
and BankSim—to cover large-scale online payments and simulated account-takeover cases. Using
both real and synthetic data lets us probe stationary regimes as well as non-stationary patterns such
as seasonal shifts and tactic drift.
For comparability, one protocol is applied across datasets. Each dataset is ordered chronologically
and split 80%/10%/10% into train/validation/test by time, preventing look-ahead leakage—crucial
for streaming or time-dependent transactions. We report precision and recall for the false-alarm/miss
trade-off, F1 as their harmonic summary, AUC for ranking across thresholds, and per-record latency
for near-real-time constraints. As a set, these metrics give a more faithful picture than accuracy on
heavily imbalanced data.
We benchmark against six baselines: Online-iForest, Hybrid-AI, GNN-IF, XGB-Anomaly,
SSR-RVFL, and an autoencoder-based detector. Each baseline follows its paper and public code when
available; otherwise, hyperparameters are tuned on the validation split. This keeps implementations
faithful to their intended design, so any gaps reflect modeling choices rather than configuration quirks.
9

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
4.1 Datasets
For the empirical evaluation of the TA-IFDC framework, we selected five representative financial
transaction datasets: IEEE-CIS Fraud Detection, PaySim, CCFD, SFD-FD, and BankSim. Together,
these datasets encompass a wide spectrum of operational contexts, ranging from large-scale real-world
payment records to semi-synthetic and fully simulated banking scenarios. They not only reflect static
historical fraud patterns but also capture environments where fraudulent behavior evolves over time,
sometimes in response to seasonal trends or system countermeasures. The mix of real transactions
and synthetic traces exposes the method to distribution shift, class-prior variation, and non-stationary
temporal patterns, offering a clearer view of detection performance and adaptability.
The IEEE-CIS Fraud Detection dataset (originally released for the 2019 IEEE-CIS Fraud
Detection challenge on Kaggle) contains more than one million labeled online transactions. The dataset
includes device and browser fingerprints, timestamps, and a mix of anonymized fields describing user
behavior and payment context. The overall fraud rate sits around 3.5%—roughly one in twenty-eight
cases—which is close to what’s seen in production systems. Because the features are high-dimensional
and partly anonymized, it’s a good test bed for anomaly detectors that need to catch rare events without
overreacting to noise. The time-stamped nature of the records also exposes gradual month-to-month
drifts in device types and behavior, which made it useful for testing how the temporal-attention
block and the dynamic threshold module in TA-IFDC react to changing conditions. For comparison,
we also used PaySim, a synthetic mobile-money dataset built from agent-based simulations of real
transaction behavior observed in sub-Saharan Africa. It comprises over 6 million transactions across
five operational categories, including “TRANSFER” and “CASH-OUT”. Although synthetic, PaySim
mirrors real user interaction patterns, offering a controlled yet realistic testing ground. The inherent
low fraud prevalence (approximately 0.13%) and the ease of injecting artificial concept drift make it
ideal for testing the model’s responsiveness to behavioral shifts.
The CCFD dataset, provided by a European card issuer, contains approximately 285,000 credit
card transactions, with features anonymized using principal component analysis. Fraudulent cases
represent a mere 0.172% of the data, making it an extreme example of class imbalance. While the
feature structure is static, it remains a widely accepted benchmark for validating anomaly detection
models, particularly with respect to precision, recall, and F1-score.
The SFD-FD dataset, published by IBM, is a synthetically generated dataset rooted in real fraud
patterns observed in banking and financial services. It includes temporal transactions, labeled fraud
cases, and control variables designed to simulate concept drift scenarios, such as seasonal changes
or policy shifts. This dataset offers controllable drift events, which is essential for validating the
adaptability of the dynamic threshold mechanism under non-stationary data distributions.
BankSim is a synthetic corpus generated with a multi-agent simulation of retail-bank customers.
It covers routine account activity—deposits, withdrawals, transfers—over extended periods, and every
record carries a timestamp. The structure of the dataset allows us to track account behavior over time
and run analyses using either sequences or sliding windows. Importantly, the labels aren't randomly
assigned—they’re based on noticeable deviations from how each account typically behaves. That
means we’re not just flagging rare events, but behavior that breaks the usual pattern. Because of that,
BankSim gives us a chance to test whether a detector like TA-IFDC can catch suspicious behavior as
it’s happening, especially when both timing and context matter. In our case, those simulated shifts
weren’t far off from what real fraud teams deal with—think seasonal shopping spikes, low-value card
testing, or sudden coordinated withdrawals. That’s why we found both PaySim and BankSim useful
for checking if the model stays stable when transaction patterns start to shift.
We ran all datasets through the same preprocessing pipeline. For missing values, we either
dropped the affected rows or filled them in depending on how much data was lost. Numeric features
were scaled down to avoid skewing the model due to value ranges. Categorical ones were turned
into indices or dummy variables as needed. If timestamps were present, we made sure not to shuffle
anything—records were kept in original order to avoid peeking into the future by accident.
10

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
Each dataset was then split by time into training, validation, and testing sets (roughly 80/10/10).
The training phase was used to build the Isolation Forest and warm up the attention module. For
tuning, we relied on the validation set—not just for hyperparameters but also to adjust the threshold
dynamically so it tracks the fraud rate and input distributions over time. The test set stayed untouched
until the end, just for final scoring.
Since the datasets vary quite a bit—some large, some small, with different structures and fraud
rates—we were able to see how the model holds up both when things are stable and when they shift.
That’s pretty close to what actually happens in real payment systems.
4.2 Evaluation Metrics
We tested TA-IFDC in settings that look a lot like real deployment. The goal wasn’t just to see
accuracy on paper but to understand how it behaves when decisions have to land in a few milliseconds,
when the fraud rate drifts over time, and when analysts can only check a limited number of alerts. We
used standard metrics, but the way we read them followed a live, ordered-stream setup—no random
reshuffling.
Precision, or how many alerts are actually right, basically shows how much trust you can put in
the system. When precision is low, investigators waste time and customers get unnecessary delays;
when it’s high, the workflow feels lighter. Recall, on the other hand, tells us how much fraud we
actually caught. Missing early fraud isn’t just a number—it often spreads to related accounts and
multiplies the damage.
Because payment streams are heavily imbalanced, accuracy is not informative. We summarize the
error trade-off with the harmonic mean F 1 = 2 ⋅ _ Precision ⋅ Recall , which rewards balanced improvements
Precision + Recall
and penalizes one-sided gains. Since a single number hides local behavior, we also examine the
precision–recall neighborhood around the operating point chosen under a fixed alert budget so the
analysis remains tied to reviewer capacity and loss-prevention costs.
We use AUC-ROC to assess ranking quality—a threshold-independent view of whether fraudulent
transactions tend to outrank legitimate ones across operating points. Because ROC area can be
optimistic under extreme imbalance, we also examine PR-curve behavior near the recall levels that
matter, so a high AUC does not mask a weak alert mix. In our setting, AUC additionally reflects the
quality of the anomaly scores that feed dynamic calibration before any cutoff is applied.
Latency is measured as the time from event arrival to decision—milliseconds per record online,
or event steps in replay. It’s not just about average speed—we also looked at the slowest cases. A
model that’s quick most of the time but occasionally lags can still break service-level agreements.
In payment systems, those few extra milliseconds matter. If a hold or block decision comes too late,
the money’s already gone, and no amount of accuracy helps after that. So, we checked tail latency
as well, using P95 and P99 to catch those worst-case delays. In our tests, even under peak load, the
longest delays stayed within about 1.4 times the average. That’s good enough to say TA-IFDC stays
within the real-time bounds required by most transaction platforms.
To ensure comparability, each dataset is ordered chronologically and split by time into train/
validation/test with no look-ahead. Metrics are computed under stationary traffic and under
concept-drift using prequential replay, so observed differences reflect modeling rather than protocol
artifacts. The same splits and metric definitions apply to baselines and to TA-IFDC, and operating
points are aligned with realistic alert budgets. In sum, this lens covers error costs (precision/recall),
their balance (F1), threshold-independent ranking (AUC), and deployability (latency) under changing
class priors and evolving operating conditions.
4.3 Baseline Methods
To build a benchmarking framework that is both convincing and comprehensive, six baseline
methods were selected, each representing a distinct methodological family within financial
anomaly detection research. The selection was not arbitrary; these models are widely cited in the
11

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
literature, cover diverse algorithmic paradigms, and are known to perform well under specific
operating assumptions. Including such a variety ensures that comparisons with the proposed TA-IFDC
framework are not confined to a single modeling philosophy but span multiple perspectives—ranging
from purely isolation-based detection to hybrid, graph-augmented, and streaming-adaptive designs.
The first reference model, Hybrid-GNN-AE, combines Graph Neural Networks (GNNs) with
Autoencoder-based reconstruction. In this architecture, transaction records are mapped into graph
structures to encode user–device–transaction relationships. In this setup, we use GNNs to learn latent
features, which are then fed into an autoencoder. The reconstruction error gives us an anomaly score.
This kind of graph-based approach tends to shine when fraud spreads across platforms or channels,
and when the transaction graph itself holds meaningful structure. We’ve seen better recall when
signals like shared IPs, reused merchant IDs, or even similar transfer patterns are included along
with behavioral features. But there’s a flip side: when the graph is sparse or messy—few links, or
too many irrelevant ones—the advantage fades. To deal with that, some systems add smoothing or
fallback rules, so the model doesn’t lose power in cold-start or low-connectivity cases.
We brought in Online Isolation Forest (ONLINE-IFOREST) as a streaming-friendly version of
the original IF. Rather than building full trees on a frozen dataset, it keeps rolling summaries—like
histograms or sketches—and updates scores as new transactions come in. That setup helps keep things
fast and light on memory, which matters when events are constant and labels don’t show up right away.
That said, it relies on a fixed threshold. So when the score distribution drifts—say during a holiday
sale or a traffic spike—the static cutoff can quickly become misaligned. We’ve seen it push up false
positives or let things slip. That’s exactly the kind of situation TA-IFDC tries to handle better, using
dynamic thresholding under a prequential setup.
We also compared against a hybrid setup that combines a standard Isolation Forest with
an LSTM. The IF handles the usual anomaly scoring, while the LSTM looks for local temporal
patterns—like bursts of activity, regular gaps between events, or recurring short-term behavior. The
outputs are stitched together through a lightweight decision layer. In practice, this design tends to
highlight suspicious behavior that clusters in time, which makes it conceptually quite close to what
our temporal module aims to catch, though we approach it differently. The trade-off is label demand
and maintenance cost: sequence models usually require labeled segments for tuning, and pronounced
concept drift forces frequent retraining. With delayed or sparse feedback, fully unsupervised, real-time
use becomes harder to sustain without relaxing latency budgets.
We also assess Enhanced-IF variants that stack IF with a secondary learner such as SVM or LOF
to refine raw scores with margin- or density-based views. In static or gently drifting traffic this can lift
precision and stabilize the alert mix, and the extra head is cheap to serve once trained. In faster-moving
streams, however, decisions often still hinge on a fixed operating point; when the transaction mix or
volume shifts quickly, precision deteriorates and recalibration is required. Cold-start users and newly
observed devices are particular pain points for these stacked schemes.
We also looked at a hybrid fraud detection setup—call it Hybrid-AI-FD—that stitches together
multiple components. It usually starts with a set of hand-tuned rules to weed out the obvious stuff,
then brings in unsupervised models like clustering or reconstruction-based filters to scan the rest.
On top of that, there's often a supervised layer to make the final decision. This kind of pipeline can
work well when you have some labeled data and decent domain rules, especially if your goal is to
tune sensitivity to match available analyst time. But moving it across systems isn’t always smooth.
These setups tend to be tightly coupled to the original environment—they rely on stable features,
good data hygiene, and assumptions that might not hold elsewhere. We've seen cases where rules
go stale or inputs quietly change, leading to performance drops if updates aren’t carefully managed.
The last SSR-RVFL combines sparse representation learning with Random Vector Functional
Link networks to map features quickly and flag atypical patterns. The approach is efficient and suits
high-throughput settings with tight tail-latency targets. Its expressivity, however, is limited when
fraud boundaries are strongly nonlinear or strategies change abruptly; sparse codes and fixed random
12

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
projections may lag unless retuned, and performance can flatten when fraud signals spread across
many weak features.
These baselines cover streaming IF, sequence-aware fusion, stacked refinement, system-level
hybrids, and sparse/fast learners. The breadth is deliberate: improvements attributed to TA-IFDC
should persist across memory-bounded streaming models, temporal models that leverage short-range
dependence, and hybrid systems that mix learned scores with rules, rather than reflecting gaps in
a narrow comparator set. Instead, the proposed method is evaluated against a representative and
technically diverse landscape of fraud detection approaches. Transformer-based detectors were
excluded due to dense supervision needs and higher GPU inference cost, which conflict with our
unsupervised, low-latency objective. Nevertheless, their sequence-modeling strength aligns closely
with the temporal-attention idea in TA-IFDC, making them strong candidates for future comparative
studies.
Finally, to maintain methodological consistency, the implementation of ONLINE-IFOREST
in this study strictly follows the officially described algorithm, ensuring that the online update
rules, isolation scoring process, and streaming histogram construction are faithfully reproduced for
fair comparison. This version formalizes the online update rules, isolation scoring functions, and
stream-based histogram construction, ensuring experimental reproducibility and citation accuracy.
Each baseline was implemented using consistent data partitions and preprocessing protocols. Their
hyperparameters were tuned using the same validation strategy as the proposed model to ensure fair
comparisons. All models were evaluated across identical performance metrics, including classification
accuracy, latency, and adaptability under concept drift, as outlined in Section 4.2.
The comparative characteristics of these six baseline models are summarized in Table 1, which
organizes them by supervision type, temporal adaptability, thresholding mechanism, and primary
strengths. This tabular view serves two purposes: first, to provide a concise technical snapshot of each
method for quick reference; second, to highlight the diversity in modeling strategies that form the
benchmark set against which TA-IFDC is evaluated. By juxtaposing these features, the table makes
explicit the methodological gaps—particularly in dynamic threshold calibration and temporal context
modeling—that the proposed framework is designed to address.
Table 1. Comparison of Baseline Models for Financial Anomaly Detection
Model Name Supervision Temporal Threshold Strengths
Adaptation Mechanism
Hybrid-GNN-AE Unsupervised Graph Temporal Fixed Captures relational
Embedding anomalies across platforms
ONLINE-IFOREST Unsupervised Histogram-based Fixed Efficient in real-time stream
Streaming processing
Adaptive IF + Semi-supervised LSTM Temporal Adaptive Models sequential fraud
LSTM Modeling behavior effectively
Enhanced IForest Unsupervised Static Fixed / Heuristic Integrates multiple anomaly
criteria
Hybrid-AI-FD Hybrid Rule-Based + Time Hybrid (Manual + Leverages both labeled and
Awareness Learned) unlabeled data
SSR-RVFL Semi-supervised Feedback-Driven Self-Calibrated Learns under concept drift
Regulation with dynamic feedback
13

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
4.4 Hyperparameter Settings and Training Strategy
To ensure fair and reproducible comparisons, all models were trained and evaluated under
consistent experimental settings across datasets. The proposed TA-IFDC framework and all baseline
models were implemented using Python 3.10, with core dependencies including scikit-learn, PyTorch,
PyOD, and DGL for graph-based architectures. The computations were performed on a workstation
equipped with an Intel i9 CPU, 64GB RAM, and NVIDIA RTX 3090 GPU. For replication, five-fold
chronological cross-validation was used within each dataset’s training slice (no look-ahead).
Random seeds, preprocessing scripts, and hyperparameters were fixed and version-controlled; full
configurations and library versions are archived in the supplementary material. In addition, all reported
performance metrics are presented as mean ± standard deviation with 95% confidence intervals
computed through bootstrap sampling to assess the stability of results. This design ensures temporal
integrity and makes experimental outcomes directly comparable across datasets and baselines.
For the TA-IFDC framework, the base IF component was configured with 100 trees and a
subsampling size of 256. The anomaly score calibration module employed a sliding calibration
window of size 2,000 transactions, updated every 100 steps. The temporal attention mechanism was
implemented using a two-head attention block with softmax-normalized weights, attending to a past
window of 15 steps. The dynamic threshold function was initialized using a quantile-based estimator
and refined online via a momentum-based update rule with a smoothing factor α=0.1. A minimum
threshold cap was enforced to mitigate threshold collapse under sparse anomaly regions.
For online inference, the TA-IFDC operated in a streaming fashion without access to future
transactions. To simulate realistic deployment, anomalies were detected at the moment of transaction
arrival based solely on historical context. To handle distributional shifts, a lightweight drift detector
monitored the Kolmogorov–Smirnov distance between incoming and historical feature distributions.
Upon detection of significant drift (p<0.01), the threshold calibrator's state was partially reset to
adapt to the new regime.
The baseline models were tuned individually using the validation subset (10% of each dataset)
by grid search. For ONLINE-IFOREST, tree depth was limited to 10, and histogram bins were set
to 64 for efficient memory use. GNN-based models used two graph convolution layers with ReLU
activation and 32-dimensional embeddings. For AE-Fraud, the autoencoder had a bottleneck size of
16, trained with a mean squared reconstruction loss using the Adam optimizer with learning rate le-3
for 30 epochs. LOF used k=20 nearest neighbors, and XGBoost-Fraud employed a maximum tree
depth of 6 with early stopping on AUC.
All experiments used an 80/10/10 train-validation-test split, stratified by fraud label distribution
where available. In unsupervised settings, the training was performed solely on unlabeled data or
presumed-clean historical transactions. Evaluation metrics, including precision, recall, F1-score, AUC,
and detection latency, were recorded for both batch and streaming scenarios. All reported results are
averaged over five independent runs with different random seeds. We report mean ± standard deviation
for all metrics, and 95% confidence intervals estimated via bootstrap over transaction windows to
indicate the statistical stability of results across repeated runs.
This training protocol ensures that model comparisons reflect performance differences attributable
to algorithmic design rather than hyperparameter or implementation variance, thereby supporting the
scientific validity of the reported results.
5. EXPERIMENTAL RESULTS
To really see how well TA-IFDC holds up, we ran eight rounds of comparative tests across
five widely used datasets—IEEE-CIS, PaySim, CCFD, SFD-FD, and BankSim. These experiments
weren’t just about getting good scores. We wanted to understand how the model performs in terms
of not just accuracy, but also how it adapts, how fast it reacts, and how interpretable the results are in
practice. For consistency, we stuck with a core set of evaluation metrics: Precision, Recall, F1-score,
14

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
AUC, and per-transaction inference latency. Each test was designed to mimic the kind of messy,
real-world situations that fraud detection systems actually face.
The first experiment presents an overall benchmark comparison across all six baseline models on
the IEEE-CIS dataset. This dataset represents high-volume, real-world online payment transactions
and is thus used as the main benchmark. Table 2 summarizes the results.
Table 2. Overall performance comparison on IEEE-CIS dataset
| Model              | Precision | Recall F1   | AUC   | Latency (ms) |
| ------------------ | --------- | ----------- | ----- | ------------ |
| TA-IFDC (Proposed) | 0.936     | 0.918 0.927 | 0.974 | 29           |
| Online-iForest     | 0.862     | 0.845 0.853 | 0.931 | 22           |
| Hybrid AI-Fraud    | 0.892     | 0.877 0.884 | 0.944 | 68           |
| GNN-IF             | 0.884     | 0.871 0.877 | 0.942 | 54           |
| SSR-RVFL           | 0.915     | 0.906 0.910 | 0.961 | 49           |
| XGB-Anomaly        | 0.851     | 0.823 0.836 | 0.918 | 34           |
On IEEE-CIS, TA-IFDC achieves the best F1 (0.927) and AUC (0.974) at 29 ms per record,
outperforming all deep/hybrid baselines; see Fig. 2(a–b) and Table 2. Panel (a) sorts models by F1
and shows that SSR-RVFL attains a competitive AUC yet at higher latency, while panel (b) ranks
latency and highlights that Online-iForest is fastest but with notably lower F1.
Figure 2. IEEE-CIS overall results: accuracy and latency
These results indicate that TA-IFDC outperforms all comparative methods in terms of both
classification performance and computational efficiency. While SSR-RVFL shows a high AUC, it
comes at the cost of increased latency. TA-IFDC achieves the highest F1 and AUC while remaining
faster than all deep and hybrid models. This suggests it is highly suitable for high-throughput payment
environments.
The second experiment investigates the contribution of the dynamic threshold calibration module.
A variant without this module is compared with the full model on the same dataset. The results are
shown in Table 3.
15

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
Table 3. Effect of dynamic threshold calibration
| Model                      |     | Precision | Recall | F1 AUC      | Latency (ms) |
| -------------------------- | --- | --------- | ------ | ----------- | ------------ |
| TA-IFDC                    |     | 0.936     | 0.918  | 0.927 0.974 | 29           |
| TA-IFDC (w/o DynThreshold) |     | 0.871     | 0.835  | 0.852 0.923 | 31           |
We ablate the calibration loop and compare the variant with the full model on IEEE-CIS (Fig.
3a–b; Table 3). Recall drops from 0.918 to 0.835 and F1 from 0.927 to 0.852, while latency stays
within 29–31 ms.
Figure 3. Effect of dynamic threshold calibration on IEEE-CIS
Removing the dynamic threshold module leads to significant performance degradation across
all metrics, particularly recall. This confirms that fixed-threshold approaches are less effective in
adapting to evolving transaction distributions. Dynamic calibration enables more flexible anomaly
decision-making and enhances robustness.
The third experiment analyzes the impact of removing the temporal attention mechanism. Table
4 presents results with and without attention layers on PaySim data.
Table 4. Impact of temporal attention mechanism
|                         | Model | Precision | Recall | F1 AUC      | Latency (ms) |
| ----------------------- | ----- | --------- | ------ | ----------- | ------------ |
| TA-IFDC                 |       | 0.918     | 0.904  | 0.911 0.968 | 28           |
| TA-IFDC (w/o Attention) |       | 0.877     | 0.848  | 0.862 0.938 | 29           |
Performance drops are notable, especially in recall and AUC. Attention mechanisms enhance the
model’s sensitivity to temporal context, allowing it to better capture sequences of small anomalies
which may appear benign in isolation but are indicative of fraud in context.
Figure 4 shows the performance of two versions of the TA-IFDC model on the PaySim dataset.
The blue line represents the version with temporal attention, which has an AUC of 0.968. The red
dashed line is the model without attention, which scored an AUC of 0.938. The gray dashed line
marks the baseline for a random classifier, at 0.5 AUC. As you can see, adding temporal attention
16

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
boosts the model's performance, especially in catching small anomalies that might otherwise be
missed. This suggests that keeping track of time-based patterns helps the model better spot fraudulent
behavior. Readability was improved by enlarging fonts and legend markers, offsetting overlapping
points, and using a higher-contrast palette, so that ROC curves and model names remain legible even
where lines intersect.
Figure 4. ROC Curve Comparison of TA-IFDC Models with and without Temporal Attention Mechanism
The fourth experiment evaluates robustness to concept drift using the SFD-FD dataset. Artificial
behavioral changes are introduced at defined intervals to simulate evolving fraud patterns. Table 5
reports F1-scores before and after drift events.
Table 5. Concept drift response (SFD-FD)
Model F1 (Pre-drift) F1 (Post-drift) ΔF1
TA-IFDC 0.914 0.902 -0.012
Online-iForest 0.869 0.784 -0.085
SSR-RVFL 0.888 0.821 -0.067
TA-IFDC demonstrates superior adaptability to evolving patterns. Its feedback and adaptive
thresholding mechanisms help mitigate abrupt distribution shifts. In contrast, static baselines suffer
significant performance loss, underscoring the importance of real-time recalibration in fraud detection.
We tested TA-IFDC on the SFD-FD dataset to see how well it could handle changes in fraud
patterns over time. In this setup, we deliberately altered transaction behavior at set intervals to
simulate concept drift. Figure 5 shows the results: before the drift, TA-IFDC’s F1-score was 0.914,
dropping slightly to 0.902 afterward. By contrast, Online-iForest fell from 0.869 to 0.784, and
SSR-RVFL from 0.888 to 0.821. The much smaller drop for TA-IFDC (−0.012) suggests that its
17

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
adaptive thresholding and feedback updates helped it maintain performance when the data distribution
shifted.
Figure 5. Performance Comparison Before and After Concept Drift on the SFD-FD Dataset.
The fifth experiment focuses on sliding window-based online detection using the BankSim
dataset, which naturally supports stream processing. Table 6 reports average latency and F1 under
three window sizes.
Table 6. Online window analysis (BankSim)
Window Size TA-IFDC F1 Latency (ms) Online-iForest F1 Latency (ms)
24h 0.909 26 0.846 21
48h 0.912 29 0.842 23
72h 0.905 31 0.834 25
TA-IFDC retains strong performance and acceptable latency across all windows. Online-iForest,
though faster, suffers in recall and general accuracy, particularly for longer transaction sequences.
In Figure 6, the performance of TA-IFDC and Online-iForest is compared under three sliding
window settings using the BankSim dataset. TA-IFDC keeps its F1-score close to 0.91 across all
windows, with latency rising slightly from 26 ms to 31 ms. Online-iForest processes marginally faster
but shows a drop in accuracy, especially with longer windows, where its F1-score falls below 0.84.
18

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
Figure 6. F1-score and Latency Across Different Window Sizes on the BankSim Dataset.
The sixth experiment studies detection on minority class transactions using CCFD. Given its
severe imbalance, the focus is on F1-score for fraud cases. Results are shown in Table 7.
Table 7. Minority class detection (CCFD)
| Model       | Precision | Recall | F1    |
| ----------- | --------- | ------ | ----- |
| TA-IFDC     | 0.903     | 0.889  | 0.896 |
| SSR-RVFL    | 0.864     | 0.850  | 0.857 |
| XGB-Anomaly | 0.788     | 0.741  | 0.764 |
The results show that TA-IFDC maintains high performance on rare fraud instances, where
most models falter. This capability stems from its temporal modeling and calibration sensitivity to
unusual transaction densities.
The seventh experiment explores cross-dataset generalization. Models trained on PaySim are
evaluated on CCFD without fine-tuning. Table 8 reports generalization scores.
Table 8. Cross-dataset generalization (Train: PaySim → Test: CCFD)
| Model          |     | F1    | AUC   |
| -------------- | --- | ----- | ----- |
| TA-IFDC        |     | 0.841 | 0.904 |
| SSR-RVFL       |     | 0.798 | 0.878 |
| Online-iForest |     | 0.772 | 0.856 |
19

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
TA-IFDC exhibits the best transferability, suggesting that its learning structure is less reliant
on dataset-specific distributions. Its performance remains robust even when exposed to unfamiliar
transaction patterns.
Figure 7 shows two evaluations involving the CCFD dataset. In the left panel, which focuses on
minority class fraud detection, TA-IFDC records an F1-score of 0.896, ahead of SSR-RVFL (0.857)
and XGB-Anomaly (0.764). The right panel presents a cross-dataset test, where models trained on
PaySim are applied to CCFD without fine-tuning. Here, TA-IFDC again ranks highest, with an F1-score
of 0.841 and an AUC of 0.904, indicating better adaptation to previously unseen transaction patterns.
Figure 7. Performance on Minority Class Detection and Cross-Dataset Generalization
The eighth and final experiment presents qualitative insights using two real transaction cases from
IEEE-CIS. One case involves a high-value early morning transaction flagged only by TA-IFDC due
to time-aware scoring. Another case, a legitimate charity transfer often misclassified by static models,
was correctly identified as normal by TA-IFDC after feedback adjustment. These examples illustrate
the model’s interpretability and practical reliability in real-world settings. Two additional narratives
illustrate practical interpretability. (i) In PaySim, a sequence of small transfers spaced only minutes
apart but executed from different devices was flagged solely through the temporal-attention layer. (ii)
In BankSim, repeated withdrawals looked routine in isolation but revealed a suspicious rhythm when
aggregated over a day. These cases highlight how temporal context helps analysts connect scattered
clues that static models would overlook.
6. DISCUSSION
This study introduces a TA-IFDC, specifically designed for real-time financial fraud detection
on digital payment platforms. The findings demonstrate the viability of this approach in overcoming
several limitations observed in prior work, particularly those relying on static thresholds, heuristic
post-processing, or single-modality models. Compared to widely used methods such as Online-iForest,
GNN-based detection models, and SSR-RVFL, TA-IFDC consistently achieves superior results across
multiple datasets, including IEEE-CIS, PaySim, CCFD, SFD-FD, and BankSim, as demonstrated
through precision, recall, F1-score, AUC, and latency analyses.
In relation to previous research, much of the existing literature has acknowledged the importance
of IF as an efficient anomaly detection method, particularly for its unsupervised nature and capacity
to handle large-scale datasets with high-dimensional sparse features. However, prior IF-based
applications often applied a fixed global threshold or required manual tuning, which can be suboptimal
under dynamic transaction environments. What this work adds to the literature is the integration of a
20

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
feedback-informed dynamic calibration mechanism, which adaptively adjusts the decision threshold
in response to real-time transaction distributions. This dynamic calibration mechanism is further
augmented by temporal attention modeling, which captures transaction sequencing patterns without
requiring explicit supervision. Both components, when analyzed through ablation experiments, are
shown to contribute significantly to model robustness, especially under concept drift and streaming
conditions.
One notable insight from this research is the model’s ability to retain strong performance not
only on traditional benchmark datasets like CCFD, but also under simulated real-world changes,
such as evolving fraud tactics and delayed feedback in user behavior (as modeled via SFD-FD and
BankSim). This reinforces the notion that static anomaly detection pipelines, though interpretable,
lack the flexibility needed in production-grade fraud monitoring systems. Moreover, while existing
hybrid or deep learning-based methods (e.g., Hybrid-AI-FD or GNN-IF) demonstrate good recall,
they typically suffer from latency issues, making them less viable for high-frequency transaction
systems. In contrast, TA-IFDC presents a practical compromise, offering high responsiveness with
negligible latency cost. Operational overhead remains modest—less than 8% CPU above a static IF
pipeline—while sustaining approximately 25–30k transactions per second on standard CPUs. GPU
acceleration is optional. Energy consumption stays below 0.5 Wh per 1 k transactions. By stabilizing
alert volumes, TA-IFDC reduced manual review time by around 12% in pilot replay.
Despite these strengths, the study also reveals several limitations. First, while the model performs
well across all datasets, its efficacy may still depend on the availability of transaction timestamps
and partial temporal continuity. In legacy banking infrastructures, where data logging practices may
be inconsistent or constrained by outdated systems, deploying the proposed framework can present
practical difficulties. Such environments often lack the granularity or continuity in transaction records
that the model implicitly assumes, potentially reducing the reliability of anomaly scoring. Moreover,
although the feedback module does improve adaptability in changing fraud landscapes, its current
design relies primarily on a soft adjustment of decision thresholds derived from patterns of historical
model consensus. This means that direct, high-quality supervisory signals—such as confirmed fraud
annotations from domain experts or real-time user reports—are not yet part of the recalibration process.
We’ve noticed that when feedback signals dry up—for example, when labels are extremely scarce—the
system doesn’t completely break. It falls back to using only the scoring trend to adjust its thresholds
gradually, which avoids any sudden spikes in alert volume. That said, this fallback mode isn’t perfect:
over time, recall tends to slide a bit. Still, the system keeps things stable enough without triggering too
many false alarms. In future work, it would make sense to fold in some semi-supervised methods or
even light-touch user feedback. That way, even partial confirmations could help the model recalibrate
faster. Interestingly, in our tests, just a few validated cases were enough to bring the thresholds back
into balance within a handful of cycles—no manual tuning required.
When we looked across all six baselines, TA-IFDC didn’t just come out ahead on the numbers—it
also highlighted something that’s often overlooked: how much the threshold matters. In a lot of older
systems, thresholds were either hand-picked or barely tuned, almost like an afterthought. But here,
adjusting them dynamically had a huge impact. It helped us cut down false positives, which in real
ops means fewer wasted analyst hours and less risk of flagging good users—or worse, missing fraud
that matters. That’s not just a minor tweak; it suggests thresholding deserves to be treated as part of
the model design, not a bolt-on at the end.
Once we made calibration adaptive, it blurred the line between model training and live deployment.
The threshold became something that moves with the stream, not something frozen at launch. When
patterns shift—say, a holiday rush or a new promo changes user behavior—the system adjusts the
boundary on its own, staying within limits like alert caps and stability guards. On a real-time pipeline
where every millisecond counts, that makes a difference. It can mean the difference between catching
fraud early or catching up after losses hit.
21

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
So rather than separating the model and the calibration logic, we treated them as one. The
threshold updates with the same temporal cues that feed the model. We made sure the scores remain
interpretable, which matters for audit, and kept the adaptation traceable. In short, we ended up with
something we can actually deploy: it adapts when needed, stays within operational bounds, and avoids
surprises for both fraud teams and risk officers.
7. CONCLUSION
TA-IFDC extends the basic Isolation Forest by adding two pieces that real systems often need.
One is a feedback loop that keeps the decision threshold in sync with the current score distribution
instead of letting it drift. The other is a temporal-attention block that captures short-term timing
patterns—because, in practice, coordinated fraud tends to show up in bursts, not as isolated points.
Together they fix two common problems we’ve seen again and again: thresholds that get stuck on
old data, and models that ignore when things happen.
This built-in adaptation also changes how training and deployment connect. The model isn’t a
“train-once-and-ship” artifact anymore. Under a prequential setup, the threshold moves with the stream,
adjusting for seasonal swings, policy shifts, or class-prior changes without retraining everything from
scratch. On payment systems that run under millisecond deadlines, that alone cuts the detection delay
for fraud rings that would otherwise slip through.
In use, the model reads events in context rather than as isolated spikes. The attention layer learns
timing cues, while the Isolation Forest handles the point-level anomaly scoring. Across five public
datasets—IEEE-CIS, PaySim, CCFD, SFD-FD, and BankSim—we saw consistent gains in recall
and F1, while latency stayed flat at around 35 ms per record (P95). In live terms, that means better
coverage without slowing down the decision path, which matters far more than squeezing out another
fraction of a point on an offline benchmark.
Operationally, the design stays modular. TA-IFDC fits into risk engines that already produce
probabilistic anomaly scores or mix unsupervised layers with case queues. Calibration runs online
against the evolving score distribution and uses delayed confirmations when available; boundary
moves are time-stamped and logged so model-risk teams can audit changes and align operating points
with alert budgets and reviewer capacity.
There are caveats. Continuous, time-stamped streams are assumed; legacy stacks with coarse
or asynchronous logging may need ordering and clock-alignment shims. The current calibration
loop leans on model-derived agreement signals; bringing in external feedback—analyst decisions,
customer reports, inter-bank intelligence—should help under extreme imbalance, though privacy and
integration constraints must be handled.
Two extensions are natural. Multimodal signals (device fingerprints, coarse geolocation, step-up
outcomes) can sharpen early screening, and federated training would let institutions adapt thresholds
locally while preserving data sovereignty. One thing that could make the system easier to trust is a
simple, human-readable note explaining why a threshold changed — something analysts can glance
at before digging deeper. In the next round of work, we plan to bring in more signal types: device
fingerprints, rough location data, and basic behavioral biometrics to add richer timing context. The
challenge will be to fuse those sources without adding lag. Keeping the tail latency low while mixing
different data streams is tricky, but that’s where most of the deployment work will probably focus next.
By dropping the fixed threshold and adding a sense of timing, the Isolation Forest turns from a
static scoring tool into something you can actually run in production. It keeps its accuracy even when
data drifts, reacts fast enough to meet real-time limits, and leaves a clear trail for audits. In short, it
bridges a piece of the gap between models that sit on paper and the messy, shifting reality of fraud
in live payment systems.
22

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
FUNDING STATEMENT
This research was funded by the Key Project of Scientific Research Plan of Universities of Anhui
Province (Humanities and Social Sciences) “Research on high-quality development Mechanism and
Path of innovative SMEs in Anhui Province (2024AH052558)”; and the Key Research Project of
Anhui Xinhua University “Investigation of the Policies of Anhui Province to Support the High-quality
development the Innovative SMEs(2023rw001)
CONFLICTS OF INTEREST
We wish to confirm that there are no known conflicts of interest associated with this publication
and there has been no significant financial support for this work that could have influenced its outcome.
CORRESPONDING AUTHOR
Correspondence should be addressed to Ping Zhou: zhouping0118@ 126 .com
23

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
REFERENCES
Al Farizi, W. S., Hidayah, I., & Rizal, M. N. (2021). Isolation forest based anomaly detection: A systematic
literature review. 2021 8th International Conference on Information Technology, Computer and Electrical
Engineering (ICITACEE) (pp. 118-122), IEEE.
Al Lawati, H. M., Zainal, A., Al-Rimy, B. A. S., Al-Azawi, M., Kassim, M. N., Almalki, S. A., & Alghamdi,
T. A. (2025). An Integrated Preprocessing and Drift Detection Approach With Adaptive Windowing For Fraud
Detection In Payment Systems (February 2025). IEEE Access : Practical Innovations, Open Solutions.
Ali, A., Abd Razak, S., Othman, S. H., Eisa, T. A. E., Al-Dhaqm, A., Nasser, M., Elhassan, T., Elshafie, H., &
Saif, A. (2022). Financial fraud detection based on machine learning: A systematic literature review. Applied
Sciences (Basel, Switzerland), 12(19), 9637. DOI: 10.3390/app12199637
Almazroi, A. A., & Ayub, N. (2023). Online payment fraud detection model using machine learning techniques.
IEEE Access : Practical Innovations, Open Solutions, 11, 137188–137203. DOI: 10.1109/ACCESS.2023.3339226
Attar, A. A., Bao, K., Hagenmeyer, V., Fabarisov, T., & Morozov, A. (2024). Improving Anomaly Detection
with Adaptive Dynamic Threshold: A Review and Enhanced Method. 2024 8th International Conference on
System Reliability and Safety (ICSRS) (pp. 662-666), IEEE.
Bello, H. O., Ige, A. B., & Ameyaw, M. N. (2024). Adaptive machine learning models: Concepts for real-time
financial fraud prevention in dynamic environments. World Journal of Advanced Engineering Technology and
Sciences, 12(2), 21-34.
Chen, T., & Tsourakakis, C. (2022). Antibenford subgraphs: Unsupervised anomaly detection in financial
networks. Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (pp.
2762-2770) DOI: 10.1145/3534678.3539100
Du, P., & Shu, H. (2022). Exploration of financial market credit scoring and risk management and prediction
using deep learning and bionic algorithm. Journal of Global Information Management, 30(9), 1–29. DOI:
10.4018/JGIM.293286
Eswar Prasad, G., Hemanth Kumar, G., Venkata Nagesh, B., Manikanth, S., & Kiran, P. (2023). Enhancing
Performance of Financial Fraud Detection Through Machine Learning Model. J Contemp Edu Theo Artific
Intel: JCETAI-101.
Fatlawi, H. K. (2025). Enhanced Fraudulent Detection Using Isolation Forest and Multi-Cluster Deep Learning.
Journal of Al-Qadisiyah for Computer Science and Mathematics, 17(1), 72–80.
Hernandez Aros, L., Bustamante Molano, L. X., Gutierrez-Portela, F., Moreno Hernandez, J. J., & Rodríguez
Barrero, M. S. (2024). Financial fraud detection through the application of machine learning techniques: A
literature review. Humanities & Social Sciences Communications, 11(1), 1–22. DOI: 10.1057/s41599-024-03606-0
Hilal, W., Gadsden, S. A., & Yawney, J. (2022). Financial fraud: A review of anomaly detection techniques and
recent advances. Expert Systems with Applications, 193, 116429. DOI: 10.1016/j.eswa.2021.116429
Immadisetty, A. (2025). Real-time fraud detection using streaming data in financial transactions. [JRTCSE].
Journal of Recent Trends in Computer Science and Engineering, 13(1), 66–76. DOI: 10.70589/JRTCSE.2025.13.1.9
Janjua, A. N., Abdulraheem, A., & Tariq, Z. (2024). Big Data Analysis Using Unsupervised Machine Learning:
K-means Clustering and Isolation Forest Models for Efficient Anomaly Detection and Removal in Complex
Lithologies. International Petroleum Technology Conference (pp. IPTC-23580-EA), IPTC.
Kamuangu, P. (2024). A review on financial fraud detection using ai and machine learning. Journal of Economics,
Finance, and Accounting Studies, 6(1), 67–77. DOI: 10.32996/jefas.2024.6.1.7
Kareem, M. S., & Muhammed, L. A. (2024). Anomaly detection in streaming data using isolation forest.
2024 Seventh International Women in Data Science Conference at Prince Sultan University (WiDS PSU) (pp.
223-228), IEEE.
Kim, H., Lee, B. S., Shin, W.-Y., & Lim, S. (2022). Graph anomaly detection with graph neural networks:
Current status and challenges. IEEE Access : Practical Innovations, Open Solutions, 10, 111820–111829. DOI:
10.1109/ACCESS.2022.3211306
24

Journal of Global Information Management
Volume 33 • Issue 1 • January-December 2025
Koziara, M., & Karczmarek, P. (2022). On a combination of clustering methods and isolation forest. International
Conference on Artificial Intelligence and Soft Computing, (pp. 114-126), Springer.
Lam, H. Y. J. (2025). Reducing Fraud with Anomaly Detection Algorithms. Journal of Financial Technology,
22(4), 231–245.
Leveni, F., Cassales, G. W., Pfahringer, B., Bifet, A., & Boracchi, G. (2025). Online isolation forest. arXiv
preprint arXiv:2505.09593.
Lin, C., Du, B., Sun, L., & Li, L. (2024). Hierarchical context representation and self-adaptive thresholding for
multivariate anomaly detection. IEEE Transactions on Knowledge and Data Engineering, 36(7), 3139–3150.
DOI: 10.1109/TKDE.2024.3360640
Mazumder, M. T. R., Shourov, M. S. H., Rasul, I., Akter, S., & Miah, M. K. (2025). Anomaly Detection in
Financial Transactions Using Convolutional Neural Networks. Journal of Economics. Finance and Accounting
Studies, 7(2), 195–207.
Núñez Delafuente, H., Astudillo, C. A., & Díaz, D. (2024). Ensemble approach using k-partitioned isolation
forests for the detection of stock market manipulation. Mathematics, 12(9), 1336. DOI: 10.3390/math12091336
Quan, C., Yuan, Y.-H., Wang, G., & Wu, H.-T. (2024). Optimization of Enterprise Financial Risk Management
and Crisis Early Warning System Supported by AI. Journal of Global Information Management, 32(1), 1–21.
DOI: 10.4018/JGIM.356490
Shanaa, M., & Abdallah, S. (2025). A hybrid anomaly detection framework combining supervised and unsupervised
learning for credit card fraud detection. F1000 Research, 14, 664. DOI: 10.12688/f1000research.166350.1
Sonani, R., & Govindarajan, V. (2022). A Hybrid Cloud-Integrated Autoencoder-GNN Architecture for
Adaptive, High-Dimensional Anomaly Detection in US Financial Services Compliance Monitoring. Spectrum
of Research, 2(1).
Tchuente, D. (2022). User modeling and profiling in information systems: A bibliometric study and future
research directions. Journal of Global Information Management, 30(1), 1–25. DOI: 10.4018/JGIM.307116
Tokovarov, M., & Karczmarek, P. (2022). A probabilistic generalization of isolation forest. Information Sciences,
584, 433–449. DOI: 10.1016/j.ins.2021.10.075
Vanini, P., Rossi, S., Zvizdic, E., & Domenig, T. (2023). Online payment fraud: From anomaly detection to risk
management. Financial Innovation, 9(1), 66. DOI: 10.1186/s40854-023-00470-w
Wang, J., Liu, J., Pu, J., Yang, Q., Miao, Z., Gao, J., & Song, Y. (2023). An anomaly prediction framework for
financial IT systems using hybrid machine learning methods. Journal of Ambient Intelligence and Humanized
Computing, 14(11), 15277–15286. DOI: 10.1007/s12652-019-01645-z
Zhang, H., Jia, X., & Chen, C. (2025). Deep Learning-Based Real-Time Data Quality Assessment and Anomaly
Detection for Large-Scale Distributed Data Streams. International Journal of Medical and All Body Health
Research, 6(1), 1.01-11.
Zhang, L., Xuan, Y., Liu, Z., Du, Z., Wang, S., & Wang, J. (2025). A hybrid ensemble model to detect Bitcoin
fraudulent transactions. Engineering Applications of Artificial Intelligence, 141, 109810. DOI: 10.1016/j.
engappai.2024.109810
Zhang, W., Xu, Y., Zheng, H., & Li, L. (2022). Verbal vs. Nonverbal Cues in Static and Dynamic Contexts of
Fraud Detection in Crowdsourcing: A Comparative Study. Journal of Global Information Management, 30(1),
1–28. DOI: 10.4018/JGIM.310928
Zheng, Z., Zhou, B., & Song, Y. (2025). Temporal-Aware Graph Attention Network for Cryptocurrency
Transaction Fraud Detection. arXiv preprint arXiv:2506.21382.
25

Reproduced with permission of copyright owner. Further
reproduction prohibited without permission.