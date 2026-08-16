---
conversion_metadata:
  converted_at: "2026-07-21T08:05:18Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Papanastassiou et al.pdf"
  source_pdf_sha256: "44245a6f28ff0388c6d6b9f0b462ffabefb705f70a122485d20842eda7dfc089"
  page_count: 16
  markdown_char_count: 96349
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Article
A Reinforcement Learning Framework for Fraud Detection in
Highly Imbalanced Financial Data

Alkis Papanastassiou 1,2,*

, Benedetta Camaiani 1,2

, Piergiulio Lenzi 1,2

and Riccardo Crupi 3

1

Istituto Nazionale di Fisica Nucleare (INFN), Sezione di Firenze, 50019 Sesto Fiorentino, Italy;
benedetta.camaiani@unifi.it (B.C.); piergiulio.lenzi@unifi.it (P.L.)

2 Dipartimento di Fisica e Astronomia, Università degli Studi di Firenze (UNIFI), 50019 Sesto Fiorentino, Italy
3 Data Artificial Intelligence Office, Intesa Sanpaolo S.p.A., 10138 Torino, Italy;

riccardo.crupi@intesasanpaolo.com

* Correspondence: alkis.papanastassiou@unifi.it

Abstract

Anomaly detection in financial transactions is a challenging task, primarily due to severe
class imbalance and the adaptive behavior of fraudulent activities. This paper presents
a reinforcement learning framework for fraud detection (RLFD) to address this problem.
We train a deep Q-network (DQN) agent with a long short-term memory (LSTM) encoder
to process sequences of financial events and identify anomalies. On a proprietary, highly
imbalanced dataset, 10-fold cross-validation highlights a distinct trade-off in performance.
While a gradient boosted trees (GBT) baseline demonstrates superior global ranking ca-
pabilities (higher ROC and PR AUC), the RLFD agent successfully learns a high-recall
policy directly from the reward signal, meeting operational needs for rare event detection.
Importantly, a dynamic orthogonality analysis proves that the two models detect distinct
subsets of fraudulent activity. The RLFD agent consistently identifies unique fraudulent
transactions that the tree-based model misses, regardless of the decision threshold. Even at
high-confidence operating points, the RLFD agent accounts for nearly 30% of the detected
anomalies. These results suggest that while tree-based models offer high precision for
static patterns, RL-based agents capture sequential anomalies that are otherwise missed,
supporting for a hybrid, parallel deployment strategy.

Keywords: fraud detection; reinforcement learning; deep q-network; anomaly detection;
imbalanced data; sequential data; data-driven finance

1. Introduction

The detection of fraudulent activities in financial data represents a critical and persis-
tent challenge, primarily due to the severe class imbalance of datasets and the dynamic,
adaptive nature of fraudulent activities, as outlined in comprehensive reviews such as Com-
pagnino et al. (2025) [1], Hernandez Aros et al. (2024) [2], Ali et al. (2022) [3], Al-Hashedi
and Magalingam (2021) [4], and others [5–8]. Financial fraud is multifaceted, encompassing
schemes from credit card and insurance fraud to sophisticated money laundering and
emerging typologies like authorized push payment (APP) fraud [1]. Many of these schemes
are not isolated events but are composed of sequences of actions designed to appear legiti-
mate. For example, money muling involves chains of transactions across multiple accounts
to obscure the origin of funds, while account takeover (ATO) fraud may be preceded by a
series of unusual login activities.

Academic Editor: Rui Araújo

Received: 24 November 2025

Revised: 15 December 2025

Accepted: 24 December 2025

Published: 26 December 2025

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license.

Appl. Sci. 2026, 16, 252

https://doi.org/10.3390/app16010252

---

<!-- PAGE 2 -->

Appl. Sci. 2026, 16, 252

2 of 16

Traditional machine learning models, such as Gradient Boosted Trees (GBTs) or Ran-
dom Forests, typically treat transactions as independent tabular data points. While effective
for static classification, this independence assumption renders them inherently blind to
the temporal correlations and sequential patterns characteristic of sophisticated fraud. As
recent empirical studies have demonstrated [1], this limitation often results in low detection
rates for rare fraudulent events, necessitating the exploration of fundamentally different
paradigms such as Reinforcement Learning (RL).

In this work, we present the Reinforcement Learning for Fraud Detection (RLFD)
framework. We position this contribution not as a novel deep learning architecture, but as
a domain-specific adaptation of the existing RLAD framework (Reinforcement Learning for
Anomaly Detection) [9], specifically engineered for the constraints of banking transaction
streams. The innovation of this study lies in the adaptation of the existing formulation,
specifically the client-centric state windowing and asymmetric reward shaping, to address
the severe class imbalance and operational costs of financial fraud. We hypothesize that
this targeted adaptation enables the agent to capture sequential behavioral patterns that
remain invisible to the static classifiers currently dominating the industry.

To investigate this hypothesis and assess the operational value of the framework, this

study addresses the following research questions:

•

Can a sequential reinforcement learning agent, trained with asymmetric rewards,
achieve superior detection rates (recall) for rare fraudulent events compared to tradi-
tional static baselines in highly imbalanced financial datasets?

• Does the RLFD framework detect a distinct subset of fraudulent activities com-
pared to tree-based models, thereby providing orthogonal and complementary opera-
tional value?
To what extent does the sequential RL approach generalize to standard public
benchmarks that lack strong temporal dependencies, compared to state-of-the-art
static classifiers?

•

2. Theoretical Background and Literature Review

The application of machine learning to financial fraud detection has evolved signif-
icantly, transitioning from rule-based expert systems to sophisticated statistical learning
algorithms. This section reviews the existing scholarship regarding static classification
methods, the challenges of imbalanced sequential data, and the emergence of reinforcement
learning as a viable alternative for anomaly detection.

2.1. Supervised Learning and Class Imbalance

Traditional supervised learning algorithms, particularly ensemble methods such as
Random Forests and Gradient Boosted Trees (GBTs), represent the current industrial stan-
dard for fraud detection [1,10]. These models excel at capturing non-linear interactions
between features in tabular data. However, their standard formulation relies on the in-
dependent and identically distributed (i.i.d.) assumption, treating each transaction as an
isolated event. This limitation is relevant in financial contexts, where fraudulent behavior
often manifests as a sequence of actions rather than a single anomalous data point [5].

Furthermore, the extreme class imbalance characterizing financial datasets
(typically < 5% fraud rate) poses a severe theoretical challenge. Standard objective func-
tions tend to bias the model towards the majority class to maximize global accuracy [3,4].
As demonstrated by Compagnino et al. (2025) [1] on the same proprietary banking dataset
used in this study, ensemble methods often struggle to achieve high recall without generat-
ing excessive false positives; in their benchmark, a Random Forest model achieved a fraud
recall of only 0.36, highlighting the need for alternative approaches.

https://doi.org/10.3390/app16010252

---

<!-- PAGE 3 -->

Appl. Sci. 2026, 16, 252

3 of 16

2.2. Deep Learning and Sequence Modeling

To address the temporal limitations of static models, Deep Learning architectures such
as Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks
have been adopted to model transaction sequences [11]. LSTMs are theoretically well-
suited for this domain because they maintain an internal state that can capture long-term
dependencies. However, in a purely supervised setting, LSTMs are typically optimized to
minimize a classification loss function (e.g., cross-entropy). This objective does not always
align with the operational goal of fraud detection, which is to maximize the cumulative
financial savings of correctly blocking fraud while minimizing customer friction.

2.3. Reinforcement Learning for Anomaly Detection

Reinforcement Learning (RL) reframes the classification problem as a Markov Decision
Process (MDP). Unlike supervised learning, which provides a static label for every input,
RL involves an agent that interacts with an environment (the stream of transactions) and
receives a reward signal based on its actions [12]. This paradigm allows for the direct
optimization of non-differentiable business metrics through reward shaping.

Recent literature has begun to explore RL for anomaly detection. The RLAD frame-
work proposed by Wu and Ortiz [9] demonstrated that a Deep Q-Network (DQN) could
effectively learn to identify anomalies in time-series data by treating the classification
decision as an action in an MDP. By decoupling the learning process from static loss mini-
mization, RL agents can learn aggressive policies that prioritize rare events if the reward
structure incentivizes it. This study builds upon these theoretical foundations to answer
the research questions posed in Section 1.

2.4. Mapping Financial Fraud to RL

To bridge the gap between financial anomaly detection and reinforcement learning
theory, we formalize the fraud detection problem not as a static classification task, but as a
sequential interaction between a monitor (the agent) and a client profile (the environment).
This conceptual model is based on three theoretical links:

1.

Sequentiality of fraud: Unlike static anomalies, financial fraud often evolves through
a trajectory of events (e.g., an initial phase of low-risk, apparently legitimate transac-
tions followed by a sudden escalation into illicit activity). The RL framework captures
this via the state representation (st), which is not a single point but a history win-
dow, allowing the agent to detect patterns based on temporal context rather than
instantaneous feature values.

2. Action-consequence feedback: In a banking context, every decision has an immediate
operational consequence. Blocking a legitimate user (False Positive) incurs a “cus-
tomer friction” cost, while allowing a fraud (False Negative) incurs a direct financial li-
ability. This aligns naturally with the RL reward signal (rt), which effectively translates
the asymmetric cost matrix of the business directly into the optimization objective.

3. Adaptive decision boundary: Traditional classifiers optimize a fixed decision bound-
ary based on a training set distribution. In contrast, an RL agent optimizes a policy
π(st) to maximize long-term rewards. This theoretically allows the system to adapt
its sensitivity based on the state of the client (e.g., becoming more aggressive if the
recent sequence shows rising entropy), rather than applying a global threshold to
all users.

By framing the problem through this conceptual lens, we justify the selection of a DQN
with LSTM encoders as the appropriate methodological vehicle to answer the research
questions posed in Section 1.

https://doi.org/10.3390/app16010252

---

<!-- PAGE 4 -->

Appl. Sci. 2026, 16, 252

4 of 16

3. Materials and Methods

Our study utilizes two distinct datasets to evaluate the RLFD framework, selected to
assess performance in both a complex, real-world banking scenario and a standardized
public environment.

3.1. Proprietary Transaction Dataset

The primary dataset employed in this study is a proprietary collection of financial
transactions provided by Intesa Sanpaolo (ISP), comprising 90,314 bank transfers from
anonymized users. The dataset is highly imbalanced, containing 3285 fraudulent transac-
tions, which represent approximately 3.6% of the total. To ensure privacy and regulatory
compliance, all data were encrypted and anonymized: categorical and textual variables
were hashed using the Secure Hash Algorithm 256-bit (SHA-256) [13] prior to being trans-
formed into numerical representations for machine learning models.

A feature engineering process was carried out to construct a rich and structured set of

variables for each transaction, organized into the following categories:

•
•

•

•

•

1.

2.

3.

Temporal: Hour, day, day of the week, and a weekend indicator.
Spatial: Latitude and longitude of the transaction origin, along with a client-specific
distance from spatial median feature. Specifically, for each client, the median latitude
and longitude across all transactions are computed, and the Euclidean distance of
each transaction from this spatial median is calculated, providing a measure of geo-
graphic deviation.
Financial: Transaction amount, currency code, divisibility flags (e.g., by 2, 5, or 10),
and decimal patterns (e.g., 0.00, 0.50).
Contextual and technical: Bank Identifier Code (BIC), bank codes, client type, mobile
carrier, and decomposed/encrypted IP address octets. Semantic information from the
transaction description field is captured using a 10-dimensional Word2Vec embedding.
Security and authentication: Flags indicating secure app usage, fingerprint authentica-
tion, instant payment, and digital signatures.

The raw data undergo a preprocessing procedure to prepare it for the RLFD agent:

Chronological sorting: Transactions are first grouped by client ID and then sorted
chronologically by timestamp to preserve temporal dependencies.
Categorical feature selection: To manage the high dimensionality of categorical vari-
ables, a two-stage selection process is applied. First, features are ranked by their
Mutual Information (MI) score with respect to the fraud label, and the top-N features
are retained. Then, for each selected feature, only the top-M most frequent values are
preserved, with all others aggregated into a single “Other” category.
Encoding and scaling: The selected categorical features are one-hot encoded, while all
numerical variables are normalized to the [0, 1] range using Min–Max scaling.

Finally, we note that synthetic oversampling techniques (e.g., SMOTE) were explicitly
excluded from the pipeline. In sequential domains, generating synthetic transaction vectors
can disrupt the temporal coherence of client histories, introducing look-ahead bias and
invalidating the Markov property required for the RL agent.

3.2. UCI Credit Card Default Benchmark

To assess the generalizability of our framework, we also employ the public “Default of
Credit Card Clients” dataset from the UCI Machine Learning Repository [14]. This dataset,
which contains records for 30,000 unique clients, is a standard benchmark for classification
tasks. It has been used in numerous studies, including a recent comparative analysis of
various machine learning models for fraud detection by Seera et al. [10]. The dataset

https://doi.org/10.3390/app16010252

---

<!-- PAGE 5 -->

Appl. Sci. 2026, 16, 252

5 of 16

includes demographic data and a six-month history of bill amounts, payment amounts, and
repayment statuses. The target label indicates whether a client defaulted on their payment
in the subsequent month, with a default rate of approximately 0.22.

While the dataset contains a six-month history, it is not primarily known for strong,
long-term temporal correlations and is treated in the literature as a static, tabular problem.
This makes it a particularly challenging benchmark for our sequential model. By testing our
framework here, we evaluate its performance in a scenario where it is not inherently favored
over tabular-optimized methods like GBT, which can process all features simultaneously.
This serves as a test of our model’s ability to generalize its feature-extraction and decision-
making capabilities to different problem structures.

Since this dataset is in a wide format (one row per client), a specific preprocessing step
is required to adapt it for our sequential model. We transform the data into a long format,
creating a sequence of six time-steps for each client. Each time-step contains the client’s
static demographic features combined with their monthly payment/billing variables for that
specific month. The final client label (default or not) is propagated to all six time-steps for that
client. The resulting features are then one-hot encoded where appropriate and scaled.

3.3. Windowing

For both datasets, the processed time-series data for each client are transformed into
overlapping sliding windows of a fixed length window_size (w). Each window serves as the
state representation for the agent. For clients with fewer than w transactions, the sequences
are left-padded with a distinct placeholder value (−10), and a binary mask is generated to
differentiate real observations from padding. We will refer to w (window_size) throughout.

3.4. RLFD Framework as a Markov Decision Process (MDP)

We formulate the fraud detection task as an MDP [12] defined by the tuple

(S, A, R, P, γ):

•

•

•

•

State (S): a state at time t, denoted st, is a window of w preprocessed transaction
vectors and is represented as a matrix st ∈ Rw×d, where d is the number of features.
hlAction (A): the agent takes one of two discrete actions at each time: at ∈ {0, 1},
where at = 0 denotes classifying the transaction as normal and at = 1 as fraudulent.
Reward (R): the reward rt is asymmetric to reflect the higher cost of missing a
fraudulent transaction. Given the true label yt ∈ {0, 1},

rt(at, yt) =






+r1
−r1
+r2
−r2

if at = 1 and yt = 1 (True Positive, TP),
if at = 0 and yt = 1 (False Negative, FN),
if at = 0 and yt = 0 (True Negative, TN),
if at = 1 and yt = 0 (False Positive, FP),

(1)

where r1 > r2 > 0. In configuration files these are denoted r1 and r2.
Transition Kernel (P): state transitions are deterministic within a client’s transaction
history: the next state st+1 is the subsequent overlapping window from the same
client’s sequence.

• Discount Factor (γ): a scalar γ ∈ [0, 1) balancing immediate and future rewards

(configuration key: gamma).

3.5. Model Architecture and Training Strategy

Our agent utilizes a Deep Q-Network (DQN) [15] with a Long Short-Term Memory
(LSTM) [16] encoder to model sequential dependencies. While the fundamental network
topology is adopted from the RLAD framework [9], we distinguish our approach by re-

https://doi.org/10.3390/app16010252

---

<!-- PAGE 6 -->

Appl. Sci. 2026, 16, 252

6 of 16

engineering the interaction loop for the financial domain. Unlike generic anomaly detection
tasks where errors may be symmetric, we implement an asymmetric reward structure
and a strictly chronological client-centric windowing mechanism. This ensures the agent
is optimized not just for pattern recognition, but for the specific operational objective of
maximizing fraud recall under imbalance. The architecture is depicted in Figure 1.

Padding Mask

Input State st

w × d

LSTM

controls

Select last valid
w × H
hidden state hw

Fully Connected
Layer

Q(st, 0)

Q(st, 1)

at
(ϵ-greedy)

rt

at

rt

Next State st+1

gradients

Transition (st, at, rt, st+1)

TD Loss & Backprop

sample

Replay
Buffer

Mini-batch

Figure 1. Expanded agent architecture and training loop. The network outputs Q-values for normal
and fraud; an ϵ-greedy selector chooses at, leading through the environment to rt and st+1. The transi-
tion (st, at, rt, st+1) is appended to the replay buffer (max size: replay_buffer_size). Mini-batches
from the buffer drive temporal-difference (TD) loss (model updated every target_update_freq
episodes) and backpropagation (dashed arrows). Here, w is the window length (window_size) and d
is the feature count.

The input state st is passed to the LSTM, which outputs a sequence of hidden states.
We extract the last valid hidden state hw (using the padding mask) as a compressed repre-
sentation and set z := hw. A linear layer then computes the action–value vector:

Q(st; θ) = Wz + b ∈ R2,

Q(st, a; θ) = [Q(st; θ)]a,

(2)

https://doi.org/10.3390/app16010252

---

<!-- PAGE 7 -->

Appl. Sci. 2026, 16, 252

7 of 16

where θ represents the network weights. Following best practices [9], the LSTM’s forget-
gate bias is initialized to 1.0.

•

•

Training is stabilized using two relevant DQN mechanisms [15]:
Experience Replay: All transitions (st, at, rt, st+1) are stored in a replay buffer. The
agent learns by sampling mini-batches from this buffer. The maximum replay buffer
size (replay_buffer_size) is treated as a hyperparameter and has been tuned to
balance sample diversity and memory efficiency.
Target Network: A separate, fixed target network Q′ is used to generate the temporal-
difference (TD) target, reducing instability by decoupling the target from the online
network. The TD target yt is

yt = rt + γ max

a′

Q′(st+1, a′; θ′).

(3)

The online network parameters θ are updated by minimizing the mean squared error.
The target network parameters are updated during training with a fixed frequency
(target_update_freq), which is also tuned as a hyperparameter.

Training is structured into episodes, where each episode corresponds to the full

transaction history of a single client. An ϵ-greedy strategy is used for action selection.

3.6. Evaluation Strategy

Our evaluation strategy differs between the two datasets to adhere to best practices

for each.

•

Proprietary Dataset: We employ a two-stage evaluation. First, for initial development
and hyperparameter tuning, we use a single, stratified holdout split: training (0.64),
validation (0.16), and testing (0.20). During this stage, we save the “Best Validation
Model” that maximizes fraud recall while maintaining normal-class recall above a
high threshold (e.g., 0.90). This specific selection criterion was driven by the bank’s
operational requirements, which mandated a minimum fraud recall of ≈65% due to
the high imbalance and the pattern of fraudulent behavior. Consequently, our tuning
process prioritized pushing the recall for the fraud class to reach this limit, rather
than solely optimizing global metrics like the Area Under the Receiver Operating
Characteristic Curve (ROC AUC) or the Area Under the Precision–Recall Curve (PR
AUC) which can yield low detection rates in highly imbalanced scenarios. Second, for
a more robust and unbiased performance assessment, we conduct a 10-fold stratified
cross-validation. This allows for a direct comparison against gradient boosted trees
(GBT) baselines, which were evaluated using the identical cross-validation scheme
and data preprocessing.

• UCI Benchmark Dataset: For this standard benchmark, we employ a 10-fold stratified
cross-validation as in Seera et al. [10]. In each fold, the data are split into 8 folds for training,
1 for validation, and 1 for testing. A fresh model is trained for each of the 10 folds, and
its best performance (based on its validation set) is evaluated on the test fold. The final
reported metrics are aggregated from the out-of-fold predictions from all 10 runs.

3.7. Performance Metrics

Evaluating the performance of fraud detection models requires a set of metrics that
handle severe class imbalance and asymmetric misclassification costs [1]. Throughout, we
define the positive class as y = 1 (fraud for the proprietary dataset and default for the UCI
dataset). The confusion-matrix entries TP, TN, FP, and FN are with respect to y = 1.

Accuracy: the overall proportion of correctly classified instances relative to all transactions:

https://doi.org/10.3390/app16010252

---

<!-- PAGE 8 -->

Appl. Sci. 2026, 16, 252

Accuracy =

TP + TN
TP + TN + FP + FN

.

8 of 16

(4)

While commonly reported, Accuracy can be misleading under extreme imbalance [17].

Precision and Recall: precision (Positive Predictive Value) measures the proportion of

correctly identified positives among all predicted positives:

Precision =

TP
TP + FP

.

(5)

Recall (Sensitivity, True Positive Rate) measures the proportion of actual positives that
were detected:

Recall =

TP
TP + FN

.

(6)

High recall reduces Type II error (missed positives), whereas high precision reduces Type I
error (false alarms) [18].

F1-Score: the harmonic mean of Precision and Recall:

F1-Score = 2 ·

Precision · Recall
Precision + Recall

.

(7)

Threshold-Independent Metrics: to assess ranking performance across thresholds,
we report the ROC AUC and the PR AUC, the latter being often more informative under
imbalance [19].

4. Results
4.1. Proprietary Dataset Performance on Holdout Set

The model was first trained on our proprietary dataset using the holdout split method-
ology. The specific hyperparameters, detailed in Table 1, were selected through a grid
search optimization process on the validation set. The rationale for the key parameter
choices is as follows:

•

•

•

•

•

Reward Ratio (r1/r2 = 4): The positive reward for catching fraud (r1) is set four
times higher than the reward for correct normal classification (r2). This asymme-
try is necessary to counteract the severe class imbalance (3.6% fraud), ensuring the
agent finds it mathematically advantageous to pursue rare fraud events rather than
converging to a trivial “always normal” policy.
Exploration (epsilon_min = 0.22): Unlike standard RL tasks where ϵ often decays to
0.01, we maintain a higher minimum exploration rate. This prevents the Q-network
from overfitting to the majority class and encourages the agent to continuously test
the decision boundary around rare events.
Feature Thresholds (N = 10, M = 10): These parameters were treated as hyperparame-
ters within the optimization loop. Preliminary sensitivity analysis on the validation
set indicated this configuration offered the optimal trade-off; increasing dimensions
beyond this point introduced state sparsity that destabilized the DQN convergence
without improving recall, while lower values discarded predictive signal.
replay_buffer (80): A constrained buffer size was chosen to ensure the agent
learns from relatively fresh, on-policy experiences, which is beneficial given the
non-stationary nature of user transaction patterns.
window_size (18): Empirically determined to balance the capture of sufficient tempo-
ral context against the inclusion of irrelevant historical noise.

The performance in Table 2 indicates that the Best Validation Model is superior for
fraud detection, achieving a fraud recall of 0.67. This performance reflects a deliberate trade-

https://doi.org/10.3390/app16010252

---

<!-- PAGE 9 -->

Appl. Sci. 2026, 16, 252

9 of 16

off driven by our validation strategy: the model identifies most frauds while maintaining
a recall of 0.90 for normal transactions. It is important to note that the achieved recall of
0.67 satisfies the explicit requirement to push fraud recall above 65%, thus sacrificing some
accuracy. This demonstrates that the RLFD agent can be effectively tuned to meet strict
operational thresholds that prioritize detecting rare events, a capability often compromised
when optimizing solely for standard aggregated metrics.

Table 1. Hyperparameter configuration and training parameters for the RLFD Agent (propri-
etary dataset).

Hyperparameter

window_size
hidden_size (LSTM)
Top-N Features N
Top-M Categories M

Preprocessing & Model Architecture

Training

learning_rate
gamma
batch_size
replay_buffer_size
inner_epochs
target_update_freq
epsilon_min
r1 (Positive-class reward)
r2 (Negative-class reward)

Value

18
64
10
10

0.001
0.95
8
80
200
40
0.22
4.0
1.0

Table 2. Performance on the proprietary dataset test set (holdout split). All metrics are proportions
in [0, 1]. The best recall for the fraud class, obtained with the Best Validation Model, is in bold.

Model

Precision (Normal) Recall (Normal) Precision (Fraud) Recall (Fraud)

Class-Wise Performance

Overall Accuracy

Final Model
Best Validation Model

0.98
0.99

0.93
0.90

0.21
0.19

0.53
0.67

0.9160
0.8903

4.2. Cross-Validation Benchmark on Proprietary Dataset

To provide a more robust evaluation, we conducted a 10-fold cross-validation on the
proprietary dataset, comparing our RLFD framework against GBT baselines. The results,
averaged across the 10 folds, are reported in Table 3.

The standard GBT model demonstrates strong statistical capabilities, achieving the
highest overall ROC AUC (0.886) and PR AUC (0.443), as evidenced in Figure 2. This indi-
cates that the tree-based model is highly effective at ranking transactions and distinguishing
classes when the decision threshold is optimized globally. However, at the default decision
threshold of 0.5, the GBT yields a low recall for the fraud class (0.226 ± 0.042), heavily
favoring precision. Applying class weighting (GBT Weighted) improves the recall to 0.450,
but still falls short of the RLFD agent in pure sensitivity. Infact, the RLFD framework, while
achieving lower aggregate ranking metrics (ROC AUC 0.773, PR AUC 0.222), successfully
learns an aggressive policy from the asymmetric reward signal. It achieves the highest
fraud recall of 0.549 ± 0.062, directly meeting the operational requirement to prioritize the
detection of rare events. To assess statistical significance, we rely on the standard deviation
across the 10 folds as a proxy for confidence intervals. The RLFD fraud recall presents

https://doi.org/10.3390/app16010252

---

<!-- PAGE 10 -->

Appl. Sci. 2026, 16, 252

10 of 16

a distribution that is strictly superior to the standard GBT with no overlap in the ±1σ
intervals, confirming the significance of the sensitivity improvement.

The discrepancy between the high recall and lower AUC suggests that while the RLFD
agent is less precise globally, it is particularly effective at flagging a specific subset of
suspicious activities that align with the high-reward criteria.

Table 3. 10-fold cross-validation performance on the proprietary dataset. Values are mean ± std. dev.
across 10 folds.

Model

Accuracy

ROC AUC

PR AUC

Recall (Normal) Recall (Fraud) Precision (Fraud)

F1 (Fraud)

GBT
GBT (Weighted)
RLFD

0.969 ± 0.002
0.962 ± 0.002
0.906 ± 0.012

0.886 ± 0.010
0.891 ± 0.012
0.773 ± 0.041

0.443 ± 0.030
0.445 ± 0.030
0.222 ± 0.042

0.997 ± 0.001
0.981 ± 0.001
0.919 ± 0.012

0.226 ± 0.042
0.450 ± 0.029
0.549 ± 0.062

0.726 ± 0.066
0.474 ± 0.030
0.197 ± 0.028

0.343 ± 0.051
0.462 ± 0.029
0.289 ± 0.036

(a)

(c)

(b)

(d)

Figure 2. Aggregated ROC and Precision–Recall curves from the 10-fold cross-validation on the
proprietary dataset, comparing the RLFD (DQN-based) framework and the GBT model. (a) RLFD
Global ROC Curve. (b) RLFD Global Precision–Recall Curve. (c) GBT Global ROC Curve. (d) GBT
Global Precision–Recall Curve. In the ROC plots (a,c), the blue dashed diagonal line represents the
performance of a random classifier (AUC = 0.5).

4.3. Orthogonality and Complementary Detection

To better understand the operational value of the RLFD framework beyond aggre-
gate metrics, we performed a dynamic orthogonality analysis. Instead of relying on a
single overlap snapshot, we examined the intersection of detected frauds across different
operating points on the holdout set.

Figure 3a displays the overlap composition as a function of the target fraud recall.
While the symmetry between the unique sets is mathematically enforced by equating the
recall of both models, the magnitude of these unique sets is relevant. If the models relied
on similar decision boundaries, the “Common” area would dominate and the unique
bands would be negligible. Instead, the persistent width of the “Unique to RLFD” band
demonstrates that for any given sensitivity level, the RLFD agent captures a substantial

https://doi.org/10.3390/app16010252

---

<!-- PAGE 11 -->

Appl. Sci. 2026, 16, 252

11 of 16

volume of fraud that the GBT inherently misses, proving that the agent is not merely a
redundant classifier but a source of orthogonal information.

Figure 3b visualizes the overlap as a function of the decision threshold, moving
from strict (high probability) to loose (low probability) classifiers. At very strict thresholds
(e.g., >0.8), the RLFD agent is notably more effective, capturing the vast majority of detected
frauds. Even as the threshold is lowered and the GBT becomes more effective, the RLFD
agent continues to contribute a distinct set of unique detections, comprising approximately
30% of the total union of detected frauds at threshold 0.4, and over 40% unique cases at
threshold 0.5, that are never captured by the tree-based model. This persistent orthogonality
confirms that the two models rely on fundamentally different decision boundaries: the
GBT exploits feature interactions in tabular space, while the RL agent leverages temporal
transitions to catch sequential anomalies.

(a) Overlap vs. Target Recall

(b) Overlap vs. Decision Threshold

Figure 3. Dynamic orthogonality analysis between the RLFD agent and the GBT baseline. (a) Evolu-
tion of fraud overlap as a function of target fraud recall (sensitivity). (b) Evolution of fraud overlap
as a function of the decision threshold (probability cut-off), ordered from strict (1.0) to loose (0.0). In
both views, the blue area highlights the unique contribution of the RLFD agent, which persists across
all operating points.

4.4. UCI Benchmark Performance

To address our third research question regarding generalizability, we evaluated the
framework on the UCI Credit Card Default dataset. This environment differs fundamen-
tally from the proprietary bank dataset: the sequences are short (only 6 time-steps), the

https://doi.org/10.3390/app16010252

---

<!-- PAGE 12 -->

Appl. Sci. 2026, 16, 252

12 of 16

granularity is coarse (monthly aggregates vs. timestamps), and the class imbalance is
moderate (22% vs. 3.6%).

Consequently, the agent’s hyperparameters required logical adaptation, as detailed
in Table 4. The window_size was reduced to 4 to accommodate the limited six-month
history available per client. Furthermore, the positive reward scalar (r1) was lowered
from 4.0 to 3.0; because the default class is less rare than banking fraud, the agent requires
less aggressive incentivization to learn the minority class distribution.

Table 4. Key hyperparameters for the UCI benchmark experiment.

Hyperparameter

window_size
hidden_size (LSTM)
r1 (Positive-class reward)
r2 (Negative-class reward)
learning_rate

Value

4
32
3.0
1.0
0.001

The comparative results are presented in Table 5. Our RLFD framework achieves
an Accuracy of 0.802 and a ROC AUC of 0.696. When compared to the suite of static
classifiers evaluated by Seera et al. [10], the RL agent performs competitively with standard
distance-based methods (e.g., k-NN) but trails behind ensemble tree methods like GBT
(Accuracy 0.821, ROC AUC 0.778).

This result provides a relevant boundary condition for our research questions. It
suggests that the RLFD framework’s advantage is heavily dependent on the presence of
high-frequency sequential signals. In the UCI dataset, where temporal resolution is low
(monthly snapshots) and feature interactions are largely static, the GBT leverage their
superior ability to partition tabular space. However, the fact that the RL agent maintains ro-
bust performance (within 2% Accuracy of the state-of-the-art) despite being architecturally
optimized for sequential tasks confirms its flexibility across different financial domains.

Table 5. Comparison of RLFD performance on the UCI benchmark against results reported by
Seera et al. [10]. Bold values indicate the performance of the proposed RLFD framework. Source
results from Feng et al. [20] and Jadhav et al. [21]. Accuracy is reported as a proportion in [0, 1].
Acronyms: k-NN, k-nearest neighbours; NB, Naïve Bayes; SVM, support vector machine; BagDT,
bagged decision trees; BagNN, bagged neural networks; BagSVM, bagged support vector machines.

Model

k-NN [21]
NB [21]
SVM [20]
Random Forest [20]
BagDT [20]
BagNN [20]
BagSVM [20]
Neural Network [20]
GBT [10]

RLFD

5. Discussion

Accuracy

ROC AUC

0.8080
0.7136
0.8200
0.8200
0.8200
0.8200
0.8100
0.8205
0.8206

0.8016

0.627
0.699
0.643
0.625
0.665
0.660
0.620
0.660
0.778

0.696

This study aimed to evaluate the efficacy of reinforcement learning for financial
fraud detection, specifically addressing the capability of sequential agents to identify rare
events in highly imbalanced domains. Interpreting our findings through the lens of the

https://doi.org/10.3390/app16010252

---

<!-- PAGE 13 -->

Appl. Sci. 2026, 16, 252

13 of 16

primary research questions reveals a distinct trade-off between statistical ranking power
and operational coverage.

Regarding the first research question on detection efficacy, the empirical results on
the proprietary dataset affirm that the RLFD agent can achieve superior recall for rare
events compared to static baselines. While the standard GBT model prioritized precision,
resulting in a low fraud recall of 0.226, the RLFD agent leveraged the asymmetric reward
signal (r1/r2 = 4) to achieve a fraud recall of 0.549. This demonstrates that in operational
contexts where the financial liability of a false negative vastly outweighs the friction cost of
a false positive, the RL framework offers a more tunable and effective optimization objec-
tive than standard cross-entropy loss minimization. Regarding computational efficiency,
the RLFD framework requires significantly higher training resources compared to GBT
(approximately 2× wall-clock time in our experiments) due to the episodic nature of the
interaction loop. However, inference latency remains comparable, as the trained Q-network
processes sequence windows in constant time.

The most relevant finding, however, addresses the operational orthogonality of the
models. The dynamic orthogonality analysis presented in Figure 3 provides strong evidence
that the RLFD framework detects a distinct subset of fraudulent activities. The persistence
of the “Unique to RLFD” detection band across the entire threshold spectrum indicates
that the agent is not merely acting as a noisier classifier, but is sensitive to fundamentally
different patterns that are invisible to the tree-based model. Notably, at high-confidence
thresholds, the RL agent contributed over 30% of the unique detections. This confirms its
value as a complementary safety net that captures temporal correlations missed by the
independence assumption of static classifiers.

To define the boundary conditions of this approach, we examined the framework’s
performance on the UCI benchmark, which lacks high-frequency temporal data. The
results show that while RLFD is competitive (Accuracy 0.802), it does not outperform the
GBT (Accuracy 0.821) in purely tabular environments. This establishes a clear limitation:
the RLFD framework provides maximum value in domains with rich sequential signals
(e.g., timestamped banking logs) and offers diminishing returns in static classification tasks
where feature interactions dominate.

These findings have both theoretical and practical implications. Theoretically, the
study reinforces the distinction between classification error minimization and operational
utility maximization. By framing fraud detection as a Markov Decision Process, the decision
boundary is allowed to evolve based on the sequential state of the client, contrasting with
the fixed hyperplane approaches of supervised learning. Methodologically, our analysis
highlights the danger of relying solely on global metrics like ROC AUC or Accuracy
in highly imbalanced settings, a choice made on the UCI benchmark to align with the
comparative analysis by Seera et al. [10]. As shown in Table 3, a model can achieve superior
ROC AUC (0.886 vs. 0.773) while failing the primary business objective of detecting
fraud (Recall 0.22 vs. 0.55). Consequently, future comparisons should prioritize threshold-
dependent metrics and dynamic overlap analyses. From a practical standpoint, the findings
speak against a “winner-takes-all” model selection. The optimal strategy for financial
institutions is possibly an hybrid parallel deployment: using GBTs as a primary high-
precision filter, while deploying RL agents in parallel to intercept the significant fraction of
complex, sequential attacks that bypass static rules.

6. Conclusions

We adapted and evaluated a Reinforcement Learning for Fraud Detection (RLFD)
framework alongside a Gradient Boosted Trees (GBTs) baseline on both a proprietary,
real-world financial dataset and a public credit default benchmark. The investigation

https://doi.org/10.3390/app16010252

---

<!-- PAGE 14 -->

Appl. Sci. 2026, 16, 252

14 of 16

reveals that statistical superiority (as measured by Area Under the Curve, AUC) does not
necessarily imply operational completeness. While the GBT baseline provides a robust
primary filter with high precision, our dynamic orthogonality analysis proves it remains
blind to specific anomalies across the entire decision spectrum. The RLFD framework,
employing an episodic training loop, asymmetric reward shaping, and LSTM-based state
encoding, successfully captures these elusive patterns. On the proprietary dataset, this
approach consistently identifies a unique set of fraudulent transactions that the GBT misses;
conversely, on the static public benchmark, the sequential advantage diminishes. We
therefore caution that the magnitude of the complementary effect observed here (e.g., the
≈30% unique detections) is likely dataset-dependent and contingent on the prevalence of
high-frequency sequential patterns in the target financial stream.

We conclude that the optimal deployment strategy for financial fraud detection is
not a monolithic choice between static or sequential models, but rather a hybrid parallel
architecture. In such a system, the RLFD agent serves as a specialized “safety net” for
complex, sequence-dependent fraud scenarios that evade traditional tree-based classifiers,
thereby significantly enhancing the total fraud coverage of the banking system. Future
evolution of this framework will focus on the integration of Explainable AI (XAI) methods
to bridge the gap between the high sensitivity of Deep RL agents and the regulatory
requirement for interpretability in the financial sector.

Author Contributions: Conceptualization, A.P.; Methodology, A.P.; Software, A.P.; Validation, A.P.;
Formal analysis, A.P.; Investigation, A.P.; Writing—original draft, A.P.; Writing—review & editing,
A.P., B.C., P.L. and R.C.; Visualization, A.P. and P.L.; Supervision, P.L. and R.C. All authors have read
and agreed to the published version of the manuscript.

Funding: This research was funded by the European Union—NextGenerationEU under the National
Recovery and Resilience Plan (PNRR)—Missione 4 “Istruzione e Ricerca”—Componente 2 “Dalla
Ricerca all’Impresa”—Investimento 1.4 “Campioni nazionali di R&S”, Project “National Centre for
HPC, Big Data and Quantum Computing”—CN1 (Spoke 2) “Simulazioni, calcolo e analisi dei dati ad
alte prestazioni”, CUP: B83C22002830001.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The proprietary dataset used in this study consists of bank transactions
protected by legal and contractual restrictions; raw data cannot be shared. The public benchmark
dataset is available at the UCI Machine Learning Repository at https://archive.ics.uci.edu/dataset/
350/default+of+credit+card+clients (accessed on 21 December 2025).

Acknowledgments: We thank Intesa Sanpaolo for providing the anonymized dataset for this research.
The views and opinions expressed are those of the authors and do not necessarily reflect the views of
Intesa Sanpaolo, its affiliates, or its employees.

Conflicts of Interest: Author Riccardo Crupi was employed by the company Intesa Sanpaolo S.p.A.
The remaining authors declare that the research was conducted in the absence of any commercial or
financial relationships that could be construed as a potential conflict of interest.

Abbreviations

The following abbreviations are used in this manuscript:

APP
ATO
AUC
BagDT
BagNN

Authorized Push Payment
Account Takeover
Area Under the Curve
Bagged Decision Trees
Bagged Neural Networks

https://doi.org/10.3390/app16010252

---

<!-- PAGE 15 -->

Appl. Sci. 2026, 16, 252

15 of 16

BagSVM
BIC
DQN
GBT
ISP
k-NN
LSTM
MDP
MI
NB
PR
RL
RLAD
RLFD
ROC
SHA-256
SVM
TD
UCI
XAI

Bagged Support Vector Machines
Bank Identifier Code
Deep Q-Network
Gradient Boosted Trees
Intesa Sanpaolo
k-Nearest Neighbours
Long Short-Term Memory
Markov Decision Process
Mutual Information
Naïve Bayes
Precision–Recall
Reinforcement Learning
Reinforcement Learning for Anomaly Detection
Reinforcement Learning for Fraud Detection
Receiver Operating Characteristic
Secure Hash Algorithm 256-bit
Support Vector Machine
Temporal Difference
University of California Irvine (Repository)
Explainable Artificial Intelligence

References

1.

Compagnino, A.A.; Maruccia, Y.; Cavuoti, S.; Riccio, G.; Tutone, A.; Crupi, R.; Pagliaro, A. An introduction to machine learning
methods for fraud detection. Appl. Sci. 2025, 15, 11787. [CrossRef]

2. Hernandez Aros, L.; Bustamante Molano, L.X.; Gutierrez-Portela, F.; Moreno Hernandez, J.J.; Rodríguez Barrero, M.S. Financial
fraud detection through the application of machine learning techniques: A literature review. Humanit. Soc. Sci. Commun. 2024,
11, 1130. [CrossRef]
Ali, A.; Abd Razak, S.; Othman, S.H.; Eisa, T.A.E.; Al-Dhaqm, A.; Nasser, M.; Elhassan, T.; Saif, A. Financial fraud detection based
on machine learning: A systematic literature review. Appl. Sci. 2022, 12, 9637. [CrossRef]
Al-Hashedi, K.G.; Magalingam, P. Financial fraud detection applying data mining techniques: A comprehensive review from
2009 to 2019. Comput. Sci. Rev. 2021, 40, 100402. [CrossRef]

3.

4.

5. West, J.; Bhattacharya, M. Intelligent financial fraud detection: A comprehensive review. Comput. Secur. 2016, 57, 47–66.

[CrossRef]
Abdallah, A.; Maarof, M.A.; Zainal, A. Fraud detection system: A survey. J. Netw. Comput. Appl. 2016, 68, 90–113. [CrossRef]

6.
7. Ngai, E.W.T.; Hu, Y.; Wong, Y.h.; Chen, Y.; Sun, X. The application of data mining techniques in financial fraud detection: A

10.

classification framework and an academic review of literature. Decis. Support Syst. 2011, 50, 559–569. [CrossRef]
Bolton, R.J.; Hand, D.J. Statistical fraud detection: A review. Stat. Sci. 2002, 17, 235–255. [CrossRef]

8.
9. Wu, T.; Ortiz, J. RLAD: Time series anomaly detection through reinforcement learning and active learning. In Proceedings
of the 7th ACM SIGKDD Workshop on Mining and Learning from Time Series (MiLeTS’21), Virtual Event, Singapore, 14–18
August 2021.
Seera, M.; Lim, C.P.; Kumar, A.; Dhamotharan, L.; Tan, K.H. An intelligent payment card fraud detection system. Ann. Oper. Res.
2024, 334, 445–467. [CrossRef] [PubMed]
Jurgovsky, J.; Granitzer, M.; Ziegler, K.; Calabretto, S.; Portier, P.E.; He-Guelton, L.; Caelen, O. Sequence classification for
credit-card fraud detection. Expert Syst. Appl. 2018, 100, 234–245. [CrossRef]
Sutton, R.S.; Barto, A.G. Reinforcement Learning: An Introduction, 2nd ed.; MIT Press: Cambridge, MA, USA, 2018.

12.
13. Penard, W.; Van Werkhoven, T. On the secure hash algorithm family. In Cryptography in Context; Wiley: Hoboken, NJ, USA, 2008;
pp. 1–18. Available online: https://blog.infocruncher.com/resources/ethereum-whitepaper-annotated/On%20the%20Secure%
20Hash%20Algorithm%20family%20%282008%29.pdf (accessed on 21 December 2025).

11.

14. Dua, D.; Graff, C. UCI Machine Learning Repository. 2019. Available online: http://archive.ics.uci.edu/ml (accessed on

10 November 2025).

15. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.;
Ostrovski, G.; et al. Human-level control through deep reinforcement learning. Nature 2015, 518, 529–533. [CrossRef] [PubMed]

16. Hochreiter, S.; Schmidhuber, J. Long short-term memory. Neural Comput. 1997, 9, 1735–1780. [CrossRef]

https://doi.org/10.3390/app16010252

---

<!-- PAGE 16 -->

Appl. Sci. 2026, 16, 252

16 of 16

17. Ramírez-Alpízar, A.; Jenkins, M.; Martínez, A.; Quesada-López, C. Use of data mining and machine learning techniques for fraud
detection in financial statements: A systematic mapping study. RISTI—Iber. J. Inf. Syst. Technol. 2020, E28, 97–109. Available
online: https://www.risti.xyz/issues/ristie28.pdf (accessed on 21 December 2025).

18. Bakumenko, A.; Elragal, A. Detecting anomalies in financial data using machine learning algorithms. Systems 2022, 10, 130.

19.

20.

21.

[CrossRef]
Saito, T.; Rehmsmeier, M. The precision–recall plot is more informative than the ROC plot when evaluating binary classifiers on
imbalanced datasets. PLoS ONE 2015, 10, e0118432. [CrossRef] [PubMed]
Feng, X.; Xiao, Z.; Zhong, B.; Qiu, J.; Dong, Y. Dynamic ensemble classification for credit scoring using soft probability. Appl. Soft
Comput. 2018, 65, 139–151. [CrossRef]
Jadhav, S.; He, H.; Jenkins, K. Information gain directed genetic algorithm wrapper feature selection for credit rating. Appl. Soft
Comput. 2018, 69, 541–553. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

https://doi.org/10.3390/app16010252

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Article
A Reinforcement Learning Framework for Fraud Detection in
Highly Imbalanced Financial Data
AlkisPapanastassiou1,2,* ,BenedettaCamaiani1,2 ,PiergiulioLenzi1,2 andRiccardoCrupi3
1 IstitutoNazionalediFisicaNucleare(INFN),SezionediFirenze,50019SestoFiorentino,Italy;
benedetta.camaiani@unifi.it(B.C.);piergiulio.lenzi@unifi.it(P.L.)
2 DipartimentodiFisicaeAstronomia,UniversitàdegliStudidiFirenze(UNIFI),50019SestoFiorentino,Italy
3 DataArtificialIntelligenceOffice,IntesaSanpaoloS.p.A.,10138Torino,Italy;
riccardo.crupi@intesasanpaolo.com
* Correspondence:alkis.papanastassiou@unifi.it
Abstract
Anomalydetectioninfinancialtransactionsisachallengingtask,primarilyduetosevere
classimbalanceandtheadaptivebehavioroffraudulentactivities. Thispaperpresents
areinforcementlearningframeworkforfrauddetection(RLFD)toaddressthisproblem.
WetrainadeepQ-network(DQN)agentwithalongshort-termmemory(LSTM)encoder
toprocesssequencesoffinancialeventsandidentifyanomalies. Onaproprietary,highly
imbalanceddataset,10-foldcross-validationhighlightsadistincttrade-offinperformance.
Whileagradientboostedtrees(GBT)baselinedemonstratessuperiorglobalrankingca-
pabilities (higher ROC and PR AUC), the RLFD agent successfully learns a high-recall
policydirectlyfromtherewardsignal,meetingoperationalneedsforrareeventdetection.
Importantly,adynamicorthogonalityanalysisprovesthatthetwomodelsdetectdistinct
subsetsoffraudulentactivity. TheRLFDagentconsistentlyidentifiesuniquefraudulent
transactionsthatthetree-basedmodelmisses,regardlessofthedecisionthreshold. Evenat
high-confidenceoperatingpoints,theRLFDagentaccountsfornearly30%ofthedetected
anomalies. These results suggest that while tree-based models offer high precision for
staticpatterns,RL-basedagentscapturesequentialanomaliesthatareotherwisemissed,
supportingforahybrid,paralleldeploymentstrategy.
Keywords: frauddetection;reinforcementlearning;deepq-network;anomalydetection;
imbalanceddata;sequentialdata;data-drivenfinance
1. Introduction
Thedetectionoffraudulentactivitiesinfinancialdatarepresentsacriticalandpersis-
tentchallenge,primarilyduetothesevereclassimbalanceofdatasetsandthedynamic,
AcademicEditor:RuiAraújo adaptivenatureoffraudulentactivities,asoutlinedincomprehensivereviewssuchasCom-
Received:24November2025 pagninoetal. (2025)[1],HernandezArosetal. (2024)[2],Alietal. (2022)[3],Al-Hashedi
Revised:15December2025 andMagalingam(2021)[4],andothers[5–8]. Financialfraudismultifaceted,encompassing
Accepted:24December2025
schemes from credit card and insurance fraud to sophisticated money laundering and
Published:26December2025
emergingtypologieslikeauthorizedpushpayment(APP)fraud[1]. Manyoftheseschemes
Copyright:©2025bytheauthors.
arenotisolatedeventsbutarecomposedofsequencesofactionsdesignedtoappearlegiti-
LicenseeMDPI,Basel,Switzerland.
mate. Forexample,moneymulinginvolveschainsoftransactionsacrossmultipleaccounts
Thisarticleisanopenaccessarticle
distributedunderthetermsand toobscuretheoriginoffunds,whileaccounttakeover(ATO)fraudmaybeprecededbya
conditionsoftheCreativeCommons seriesofunusualloginactivities.
Attribution(CCBY)license.
Appl.Sci.2026,16,252 https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 2of16
Traditionalmachinelearningmodels,suchasGradientBoostedTrees(GBTs)orRan-
domForests,typicallytreattransactionsasindependenttabulardatapoints.Whileeffective
forstaticclassification,thisindependenceassumptionrenderstheminherentlyblindto
thetemporalcorrelationsandsequentialpatternscharacteristicofsophisticatedfraud. As
recentempiricalstudieshavedemonstrated[1],thislimitationoftenresultsinlowdetection
ratesforrarefraudulentevents,necessitatingtheexplorationoffundamentallydifferent
paradigmssuchasReinforcementLearning(RL).
In this work, we present the Reinforcement Learning for Fraud Detection (RLFD)
framework. Wepositionthiscontributionnotasanoveldeeplearningarchitecture,butas
adomain-specificadaptationoftheexistingRLADframework(ReinforcementLearningfor
AnomalyDetection)[9],specificallyengineeredfortheconstraintsofbankingtransaction
streams. Theinnovationofthisstudyliesintheadaptationoftheexistingformulation,
specificallytheclient-centricstatewindowingandasymmetricrewardshaping,toaddress
thesevereclassimbalanceandoperationalcostsoffinancialfraud. Wehypothesizethat
thistargetedadaptationenablestheagenttocapturesequentialbehavioralpatternsthat
remaininvisibletothestaticclassifierscurrentlydominatingtheindustry.
Toinvestigatethishypothesisandassesstheoperationalvalueoftheframework,this
studyaddressesthefollowingresearchquestions:
• Can a sequential reinforcement learning agent, trained with asymmetric rewards,
achievesuperiordetectionrates(recall)forrarefraudulenteventscomparedtotradi-
tionalstaticbaselinesinhighlyimbalancedfinancialdatasets?
• Does the RLFD framework detect a distinct subset of fraudulent activities com-
paredtotree-basedmodels,therebyprovidingorthogonalandcomplementaryopera-
tionalvalue?
• To what extent does the sequential RL approach generalize to standard public
benchmarks that lack strong temporal dependencies, compared to state-of-the-art
staticclassifiers?
2. TheoreticalBackgroundandLiteratureReview
Theapplicationofmachinelearningtofinancialfrauddetectionhasevolvedsignif-
icantly,transitioningfromrule-basedexpertsystemstosophisticatedstatisticallearning
algorithms. This section reviews the existing scholarship regarding static classification
methods,thechallengesofimbalancedsequentialdata,andtheemergenceofreinforcement
learningasaviablealternativeforanomalydetection.
2.1. SupervisedLearningandClassImbalance
Traditionalsupervisedlearningalgorithms,particularlyensemblemethodssuchas
RandomForestsandGradientBoostedTrees(GBTs),representthecurrentindustrialstan-
dardforfrauddetection[1,10]. Thesemodelsexcelatcapturingnon-linearinteractions
betweenfeaturesintabulardata. However, theirstandardformulationreliesonthein-
dependentandidenticallydistributed(i.i.d.) assumption,treatingeachtransactionasan
isolatedevent. Thislimitationisrelevantinfinancialcontexts,wherefraudulentbehavior
oftenmanifestsasasequenceofactionsratherthanasingleanomalousdatapoint[5].
Furthermore, the extreme class imbalance characterizing financial datasets
(typically< 5%fraudrate)posesaseveretheoreticalchallenge. Standardobjectivefunc-
tionstendtobiasthemodeltowardsthemajorityclasstomaximizeglobalaccuracy[3,4].
AsdemonstratedbyCompagninoetal. (2025)[1]onthesameproprietarybankingdataset
usedinthisstudy,ensemblemethodsoftenstruggletoachievehighrecallwithoutgenerat-
ingexcessivefalsepositives;intheirbenchmark,aRandomForestmodelachievedafraud
recallofonly0.36,highlightingtheneedforalternativeapproaches.
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 3of16
2.2. DeepLearningandSequenceModeling
Toaddressthetemporallimitationsofstaticmodels,DeepLearningarchitecturessuch
asRecurrentNeuralNetworks(RNNs)andLongShort-TermMemory(LSTM)networks
have been adopted to model transaction sequences [11]. LSTMs are theoretically well-
suitedforthisdomainbecausetheymaintainaninternalstatethatcancapturelong-term
dependencies. However,inapurelysupervisedsetting,LSTMsaretypicallyoptimizedto
minimizeaclassificationlossfunction(e.g.,cross-entropy). Thisobjectivedoesnotalways
alignwiththeoperationalgoaloffrauddetection,whichistomaximizethecumulative
financialsavingsofcorrectlyblockingfraudwhileminimizingcustomerfriction.
2.3. ReinforcementLearningforAnomalyDetection
ReinforcementLearning(RL)reframestheclassificationproblemasaMarkovDecision
Process(MDP).Unlikesupervisedlearning,whichprovidesastaticlabelforeveryinput,
RLinvolvesanagentthatinteractswithanenvironment(thestreamoftransactions)and
receives a reward signal based on its actions [12]. This paradigm allows for the direct
optimizationofnon-differentiablebusinessmetricsthroughrewardshaping.
RecentliteraturehasbeguntoexploreRLforanomalydetection. TheRLADframe-
workproposedbyWuandOrtiz[9]demonstratedthataDeepQ-Network(DQN)could
effectively learn to identify anomalies in time-series data by treating the classification
decisionasanactioninanMDP.Bydecouplingthelearningprocessfromstaticlossmini-
mization,RLagentscanlearnaggressivepoliciesthatprioritizerareeventsifthereward
structureincentivizesit. Thisstudybuildsuponthesetheoreticalfoundationstoanswer
theresearchquestionsposedinSection1.
2.4. MappingFinancialFraudtoRL
Tobridgethegapbetweenfinancialanomalydetectionandreinforcementlearning
theory,weformalizethefrauddetectionproblemnotasastaticclassificationtask,butasa
sequentialinteractionbetweenamonitor (theagent)andaclientprofile(theenvironment).
Thisconceptualmodelisbasedonthreetheoreticallinks:
1. Sequentialityoffraud: Unlikestaticanomalies,financialfraudoftenevolvesthrough
atrajectoryofevents(e.g.,aninitialphaseoflow-risk,apparentlylegitimatetransac-
tionsfollowedbyasuddenescalationintoillicitactivity). TheRLframeworkcaptures
this via the state representation (s ), which is not a single point but a history win-
t
dow, allowing the agent to detect patterns based on temporal context rather than
instantaneousfeaturevalues.
2. Action-consequencefeedback: Inabankingcontext,everydecisionhasanimmediate
operationalconsequence. Blockingalegitimateuser(FalsePositive)incursa“cus-
tomerfriction”cost,whileallowingafraud(FalseNegative)incursadirectfinancialli-
ability. ThisalignsnaturallywiththeRLrewardsignal(r ),whicheffectivelytranslates
t
theasymmetriccostmatrixofthebusinessdirectlyintotheoptimizationobjective.
3. Adaptivedecisionboundary: Traditionalclassifiersoptimizeafixeddecisionbound-
arybasedonatrainingsetdistribution. Incontrast,anRLagentoptimizesapolicy
π(s )tomaximizelong-termrewards. Thistheoreticallyallowsthesystemtoadapt
t
itssensitivitybasedonthestateoftheclient(e.g.,becomingmoreaggressiveifthe
recent sequence shows rising entropy), rather than applying a global threshold to
allusers.
Byframingtheproblemthroughthisconceptuallens,wejustifytheselectionofaDQN
with LSTM encoders as the appropriate methodological vehicle to answer the research
questionsposedinSection1.
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 4of16
3. MaterialsandMethods
OurstudyutilizestwodistinctdatasetstoevaluatetheRLFDframework,selectedto
assessperformanceinbothacomplex,real-worldbankingscenarioandastandardized
publicenvironment.
3.1. ProprietaryTransactionDataset
Theprimarydatasetemployedinthisstudyisaproprietarycollectionoffinancial
transactions provided by Intesa Sanpaolo (ISP), comprising 90,314 bank transfers from
anonymizedusers. Thedatasetishighlyimbalanced,containing3285fraudulenttransac-
tions,whichrepresentapproximately3.6%ofthetotal. Toensureprivacyandregulatory
compliance,alldatawereencryptedandanonymized: categoricalandtextualvariables
werehashedusingtheSecureHashAlgorithm256-bit(SHA-256)[13]priortobeingtrans-
formedintonumericalrepresentationsformachinelearningmodels.
Afeatureengineeringprocesswascarriedouttoconstructarichandstructuredsetof
variablesforeachtransaction,organizedintothefollowingcategories:
• Temporal: Hour,day,dayoftheweek,andaweekendindicator.
• Spatial: Latitudeandlongitudeofthetransactionorigin,alongwithaclient-specific
distancefromspatialmedianfeature. Specifically,foreachclient,themedianlatitude
and longitude across all transactions are computed, and the Euclidean distance of
eachtransactionfromthisspatialmedianiscalculated,providingameasureofgeo-
graphicdeviation.
• Financial: Transactionamount,currencycode,divisibilityflags(e.g.,by2,5,or10),
anddecimalpatterns(e.g.,0.00,0.50).
• Contextualandtechnical: BankIdentifierCode(BIC),bankcodes,clienttype,mobile
carrier,anddecomposed/encryptedIPaddressoctets. Semanticinformationfromthe
transactiondescriptionfieldiscapturedusinga10-dimensionalWord2Vecembedding.
• Securityandauthentication: Flagsindicatingsecureappusage,fingerprintauthentica-
tion,instantpayment,anddigitalsignatures.
TherawdataundergoapreprocessingproceduretoprepareitfortheRLFDagent:
1. Chronologicalsorting: TransactionsarefirstgroupedbyclientIDandthensorted
chronologicallybytimestamptopreservetemporaldependencies.
2. Categoricalfeatureselection: Tomanagethehighdimensionalityofcategoricalvari-
ables, a two-stage selection process is applied. First, features are ranked by their
MutualInformation(MI)scorewithrespecttothefraudlabel,andthetop-Nfeatures
areretained. Then,foreachselectedfeature,onlythetop-Mmostfrequentvaluesare
preserved,withallothersaggregatedintoasingle“Other”category.
3. Encodingandscaling: Theselectedcategoricalfeaturesareone-hotencoded,whileall
numericalvariablesarenormalizedtothe[0,1]rangeusingMin–Maxscaling.
Finally,wenotethatsyntheticoversamplingtechniques(e.g.,SMOTE)wereexplicitly
excludedfromthepipeline. Insequentialdomains,generatingsynthetictransactionvectors
candisruptthetemporalcoherenceofclienthistories, introducinglook-aheadbiasand
invalidatingtheMarkovpropertyrequiredfortheRLagent.
3.2. UCICreditCardDefaultBenchmark
Toassessthegeneralizabilityofourframework,wealsoemploythepublic“Defaultof
CreditCardClients”datasetfromtheUCIMachineLearningRepository[14]. Thisdataset,
whichcontainsrecordsfor30,000uniqueclients,isastandardbenchmarkforclassification
tasks. Ithasbeenusedinnumerousstudies,includingarecentcomparativeanalysisof
various machine learning models for fraud detection by Seera et al. [10]. The dataset
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252
5of16
includesdemographicdataandasix-monthhistoryofbillamounts,paymentamounts,and
repaymentstatuses. Thetargetlabelindicateswhetheraclientdefaultedontheirpayment
inthesubsequentmonth,withadefaultrateofapproximately0.22.
Whilethedatasetcontainsasix-monthhistory,itisnotprimarilyknownforstrong,
long-termtemporalcorrelationsandistreatedintheliteratureasastatic,tabularproblem.
Thismakesitaparticularlychallengingbenchmarkforoursequentialmodel.Bytestingour
frameworkhere,weevaluateitsperformanceinascenariowhereitisnotinherentlyfavored
overtabular-optimizedmethodslikeGBT,whichcanprocessallfeaturessimultaneously.
Thisservesasatestofourmodel’sabilitytogeneralizeitsfeature-extractionanddecision-
makingcapabilitiestodifferentproblemstructures.
Sincethisdatasetisinawideformat(onerowperclient),aspecificpreprocessingstep
isrequiredtoadaptitforoursequentialmodel. Wetransformthedataintoalongformat,
creating a sequence of six time-steps for each client. Each time-step contains the client’s
staticdemographicfeaturescombinedwiththeirmonthlypayment/billingvariablesforthat
specificmonth.Thefinalclientlabel(defaultornot)ispropagatedtoallsixtime-stepsforthat
client.Theresultingfeaturesarethenone-hotencodedwhereappropriateandscaled.
3.3. Windowing
Forbothdatasets,theprocessedtime-seriesdataforeachclientaretransformedinto
overlappingslidingwindowsofafixedlengthwindow_size(w).Eachwindowservesasthe
staterepresentationfortheagent. Forclientswithfewerthanwtransactions,thesequences
areleft-paddedwithadistinctplaceholdervalue(−10),andabinarymaskisgeneratedto
differentiaterealobservationsfrompadding. Wewillrefertow(window_size)throughout.
3.4. RLFDFrameworkasaMarkovDecisionProcess(MDP)
We formulate the fraud detection task as an MDP [12] defined by the tuple
(S,A,R,P,γ):
• State (S): a state at time t, denoted s , is a window of w preprocessed transaction
t
∈Rw×d,wheredisthenumberoffeatures.
vectorsandisrepresentedasamatrixs
t
• hlAction (A): the agent takes one of two discrete actions at each time: a t ∈ {0,1},
|        | =0denotesclassifyingthetransactionasnormalanda |     |     |     | =1asfraudulent. |     |
| ------ | ---------------------------------------------- | --- | --- | --- | --------------- | --- |
| wherea | t                                              |     |     |     | t               |     |
• Reward (R): the reward r is asymmetric to reflect the higher cost of missing a
t
| fraudulenttransaction. |     | Giventhetruelabely |     | ∈ {0,1}, |     |     |
| ---------------------- | --- | ------------------ | --- | -------- | --- | --- |
t

|     |         | +           | =           | =                    |                         |     |
| --- | ------- | ----------- | ----------- | -------------------- | ----------------------- | --- |
|     |         | − r 1 | i f a t 1 a | n d y t 1 ( T r u e  | P o s it iv e , T P ) , |     |
|     |         | r           | i f a = 0 a | n d y = 1 ( F a ls e | N e g a ti v e , F N ), |     |
|     | r (a ,y | ) = 1       | t           | t                    |                         | (1) |
t t t
|     |     |  + r | i f a = 0 a | n d y = 0 ( T r u e  | N e g a t i v e , T N ), |     |
| --- | --- | ---------- | ----------- | -------------------- | ------------------------ | --- |
|     |     | 2          | t           | t                    |                          |     |
|     |     | −          | =           | =                    |                          |     |
|     |     | r 2        | i f a t 1 a | n d y t 0 ( F a ls e | P o si t i v e , F P ),  |     |
>r >0. Inconfigurationfilesthesearedenotedr1andr2.
| wherer | 1 2 |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
• TransitionKernel(P): statetransitionsaredeterministicwithinaclient’stransaction
history: the next state s is the subsequent overlapping window from the same
t+1
client’ssequence.
∈ [0,1)
• Discount Factor (γ): a scalar γ balancing immediate and future rewards
| (configurationkey: |     | gamma). |     |     |     |     |
| ------------------ | --- | ------- | --- | --- | --- | --- |
3.5. ModelArchitectureandTrainingStrategy
OuragentutilizesaDeepQ-Network(DQN)[15]withaLongShort-TermMemory
(LSTM)[16]encodertomodelsequentialdependencies. Whilethefundamentalnetwork
topologyisadoptedfromtheRLADframework[9],wedistinguishourapproachbyre-
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 6of16
engineeringtheinteractionloopforthefinancialdomain.Unlikegenericanomalydetection
tasks where errors may be symmetric, we implement an asymmetric reward structure
andastrictlychronologicalclient-centricwindowingmechanism. Thisensurestheagent
isoptimizednotjustforpatternrecognition,butforthespecificoperationalobjectiveof
maximizingfraudrecallunderimbalance. ThearchitectureisdepictedinFigure1.
PaddingMask InputStatest
w×d
LSTM
controls Selectlastvalid
w×H
hiddenstatehw
FullyConnected
Layer
Q(st,0) Q(st,1)
at
(ϵ-greedy)
at
gradients
rt
rt
NextStates t+1
TDLoss&Backprop
Transition(st,at,rt,s
t+1
)
sample
Replay
Mini-batch
Buffer
Figure1.Expandedagentarchitectureandtrainingloop.ThenetworkoutputsQ-valuesfornormal
andfraud;anϵ-greedyselectorchoosesat,leadingthroughtheenvironmenttortands t+1 .Thetransi-
tion(st,at,rt,s
t+1
)isappendedtothereplaybuffer(maxsize:replay_buffer_size).Mini-batches
from the buffer drive temporal-difference (TD) loss (model updated every target_update_freq
episodes)andbackpropagation(dashedarrows).Here,wisthewindowlength(window_size)andd
isthefeaturecount.
Theinputstates ispassedtotheLSTM,whichoutputsasequenceofhiddenstates.
t
Weextractthelastvalidhiddenstateh (usingthepaddingmask)asacompressedrepre-
w
sentationandsetz := h . Alinearlayerthencomputestheaction–valuevector:
w
Q(s ;θ) =Wz+b ∈R2, Q(s ,a;θ) = [Q(s ;θ)] , (2)
t t t a
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 7of16
whereθrepresentsthenetworkweights. Followingbestpractices[9],theLSTM’sforget-
gatebiasisinitializedto1.0.
TrainingisstabilizedusingtworelevantDQNmechanisms[15]:
• ExperienceReplay: Alltransitions (s t ,a t ,r t ,s t+1 ) arestoredinareplaybuffer. The
agentlearnsbysamplingmini-batchesfromthisbuffer. Themaximumreplaybuffer
size (replay_buffer_size) is treated as a hyperparameter and has been tuned to
balancesamplediversityandmemoryefficiency.
• TargetNetwork: Aseparate,fixedtargetnetworkQ′ isusedtogeneratethetemporal-
difference(TD)target,reducinginstabilitybydecouplingthetargetfromtheonline
network. TheTDtargety is
t
y t =r t +γmaxQ ′(s t+1 ,a ′ ;θ ′). (3)
a′
Theonlinenetworkparametersθareupdatedbyminimizingthemeansquarederror.
Thetargetnetworkparametersareupdatedduringtrainingwithafixedfrequency
(target_update_freq),whichisalsotunedasahyperparameter.
Training is structured into episodes, where each episode corresponds to the full
transactionhistoryofasingleclient. Anϵ-greedystrategyisusedforactionselection.
3.6. EvaluationStrategy
Ourevaluationstrategydiffersbetweenthetwodatasetstoadheretobestpractices
foreach.
• ProprietaryDataset: Weemployatwo-stageevaluation. First,forinitialdevelopment
andhyperparametertuning,weuseasingle,stratifiedholdoutsplit: training(0.64),
validation(0.16),andtesting(0.20). Duringthisstage,wesavethe“BestValidation
Model”thatmaximizesfraudrecallwhilemaintainingnormal-classrecallabovea
highthreshold(e.g.,0.90). Thisspecificselectioncriterionwasdrivenbythebank’s
operationalrequirements,whichmandatedaminimumfraudrecallof≈65%dueto
thehighimbalanceandthepatternoffraudulentbehavior. Consequently,ourtuning
process prioritized pushing the recall for the fraud class to reach this limit, rather
than solely optimizing global metrics like the Area Under the Receiver Operating
CharacteristicCurve(ROCAUC)ortheAreaUnderthePrecision–RecallCurve(PR
AUC)whichcanyieldlowdetectionratesinhighlyimbalancedscenarios. Second,for
amorerobustandunbiasedperformanceassessment,weconducta10-foldstratified
cross-validation. Thisallowsforadirectcomparisonagainstgradientboostedtrees
(GBT)baselines,whichwereevaluatedusingtheidenticalcross-validationscheme
anddatapreprocessing.
• UCIBenchmarkDataset: Forthisstandardbenchmark,weemploya10-foldstratified
cross-validationasinSeeraetal.[10].Ineachfold,thedataaresplitinto8foldsfortraining,
1forvalidation,and1fortesting. Afreshmodelistrainedforeachofthe10folds,and
itsbestperformance(basedonitsvalidationset)isevaluatedonthetestfold. Thefinal
reportedmetricsareaggregatedfromtheout-of-foldpredictionsfromall10runs.
3.7. PerformanceMetrics
Evaluatingtheperformanceoffrauddetectionmodelsrequiresasetofmetricsthat
handlesevereclassimbalanceandasymmetricmisclassificationcosts[1]. Throughout,we
definethepositiveclassasy =1(fraudfortheproprietarydatasetanddefaultfortheUCI
dataset). Theconfusion-matrixentriesTP,TN,FP,andFNarewithrespecttoy =1.
Accuracy:theoverallproportionofcorrectlyclassifiedinstancesrelativetoalltransactions:
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 8of16
TP+TN
Accuracy= . (4)
TP+TN+FP+FN
Whilecommonlyreported,Accuracycanbemisleadingunderextremeimbalance[17].
PrecisionandRecall: precision(PositivePredictiveValue)measurestheproportionof
correctlyidentifiedpositivesamongallpredictedpositives:
TP
Precision= . (5)
TP+FP
Recall (Sensitivity, True Positive Rate) measures the proportion of actual positives that
weredetected:
TP
Recall= . (6)
TP+FN
HighrecallreducesTypeIIerror(missedpositives),whereashighprecisionreducesTypeI
error(falsealarms)[18].
F1-Score: theharmonicmeanofPrecisionandRecall:
Precision·Recall
F1-Score=2· . (7)
Precision+Recall
Threshold-Independent Metrics: to assess ranking performance across thresholds,
wereporttheROCAUCandthePRAUC,thelatterbeingoftenmoreinformativeunder
imbalance[19].
4. Results
4.1. ProprietaryDatasetPerformanceonHoldoutSet
Themodelwasfirsttrainedonourproprietarydatasetusingtheholdoutsplitmethod-
ology. The specific hyperparameters, detailed in Table 1, were selected through a grid
search optimization process on the validation set. The rationale for the key parameter
choicesisasfollows:
• Reward Ratio (r1/r2 = 4): The positive reward for catching fraud (r1) is set four
times higher than the reward for correct normal classification (r2). This asymme-
tryisnecessarytocounteractthesevereclassimbalance(3.6%fraud),ensuringthe
agentfindsitmathematicallyadvantageoustopursuerarefraudeventsratherthan
convergingtoatrivial“alwaysnormal”policy.
• Exploration(epsilon_min=0.22): UnlikestandardRLtaskswhereϵoftendecaysto
0.01,wemaintainahigherminimumexplorationrate. ThispreventstheQ-network
fromoverfittingtothemajorityclassandencouragestheagenttocontinuouslytest
thedecisionboundaryaroundrareevents.
• FeatureThresholds(N=10,M=10): Theseparametersweretreatedashyperparame-
terswithintheoptimizationloop. Preliminarysensitivityanalysisonthevalidation
setindicatedthisconfigurationofferedtheoptimaltrade-off;increasingdimensions
beyondthispointintroducedstatesparsitythatdestabilizedtheDQNconvergence
withoutimprovingrecall,whilelowervaluesdiscardedpredictivesignal.
• replay_buffer (80): A constrained buffer size was chosen to ensure the agent
learns from relatively fresh, on-policy experiences, which is beneficial given the
non-stationarynatureofusertransactionpatterns.
• window_size(18): Empiricallydeterminedtobalancethecaptureofsufficienttempo-
ralcontextagainsttheinclusionofirrelevanthistoricalnoise.
TheperformanceinTable2indicatesthattheBestValidationModelissuperiorfor
frauddetection,achievingafraudrecallof0.67.Thisperformancereflectsadeliberatetrade-
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252
9of16
offdrivenbyourvalidationstrategy: themodelidentifiesmostfraudswhilemaintaining
arecallof0.90fornormaltransactions. Itisimportanttonotethattheachievedrecallof
0.67satisfiestheexplicitrequirementtopushfraudrecallabove65%,thussacrificingsome
accuracy. ThisdemonstratesthattheRLFDagentcanbeeffectivelytunedtomeetstrict
operationalthresholdsthatprioritizedetectingrareevents,acapabilityoftencompromised
whenoptimizingsolelyforstandardaggregatedmetrics.
Table 1. Hyperparameter configuration and training parameters for the RLFD Agent (propri-
etarydataset).
|     | Hyperparameter |     |     | Value |     |
| --- | -------------- | --- | --- | ----- | --- |
Preprocessing&ModelArchitecture
window_size
18
|     | hidden_size(LSTM) |     |     | 64  |     |
| --- | ----------------- | --- | --- | --- | --- |
|     | Top-NFeaturesN    |     |     | 10  |     |
|     | Top-MCategoriesM  |     |     | 10  |     |
Training
|     | learning_rate            |     |     | 0.001 |     |
| --- | ------------------------ | --- | --- | ----- | --- |
|     | gamma                    |     |     | 0.95  |     |
|     | batch_size               |     |     | 8     |     |
|     | replay_buffer_size       |     |     | 80    |     |
|     | inner_epochs             |     |     | 200   |     |
|     | target_update_freq       |     |     | 40    |     |
|     | epsilon_min              |     |     | 0.22  |     |
|     | r1(Positive-classreward) |     |     | 4.0   |     |
r2(Negative-classreward)
1.0
Table2.Performanceontheproprietarydatasettestset(holdoutsplit).Allmetricsareproportions
in[0,1].Thebestrecallforthefraudclass,obtainedwiththeBestValidationModel,isinbold.
Class-WisePerformance
| Model |     |     |     | OverallAccuracy |     |
| ----- | --- | --- | --- | --------------- | --- |
Precision(Normal) Recall(Normal) Precision(Fraud) Recall(Fraud)
| FinalModel          | 0.98 | 0.93 | 0.21 | 0.53 | 0.9160 |
| ------------------- | ---- | ---- | ---- | ---- | ------ |
| BestValidationModel | 0.99 | 0.90 | 0.19 | 0.67 | 0.8903 |
4.2. Cross-ValidationBenchmarkonProprietaryDataset
Toprovideamorerobustevaluation,weconducteda10-foldcross-validationonthe
proprietarydataset,comparingourRLFDframeworkagainstGBTbaselines. Theresults,
averagedacrossthe10folds,arereportedinTable3.
ThestandardGBTmodeldemonstratesstrongstatisticalcapabilities,achievingthe
highestoverallROCAUC(0.886)andPRAUC(0.443),asevidencedinFigure2. Thisindi-
catesthatthetree-basedmodelishighlyeffectiveatrankingtransactionsanddistinguishing
classeswhenthedecisionthresholdisoptimizedglobally. However,atthedefaultdecision
±
threshold of 0.5, the GBT yields a low recall for the fraud class (0.226 0.042), heavily
favoringprecision. Applyingclassweighting(GBTWeighted)improvestherecallto0.450,
butstillfallsshortoftheRLFDagentinpuresensitivity. Infact,theRLFDframework,while
achievingloweraggregaterankingmetrics(ROCAUC0.773,PRAUC0.222),successfully
learnsanaggressivepolicyfromtheasymmetricrewardsignal. Itachievesthehighest
fraudrecallof0.549±0.062,directlymeetingtheoperationalrequirementtoprioritizethe
detectionofrareevents. Toassessstatisticalsignificance,werelyonthestandarddeviation
across the 10 folds as a proxy for confidence intervals. The RLFD fraud recall presents
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 10of16
a distribution that is strictly superior to the standard GBT with no overlap in the ±1σ
intervals,confirmingthesignificanceofthesensitivityimprovement.
ThediscrepancybetweenthehighrecallandlowerAUCsuggeststhatwhiletheRLFD
agent is less precise globally, it is particularly effective at flagging a specific subset of
suspiciousactivitiesthatalignwiththehigh-rewardcriteria.
Table3.10-foldcross-validationperformanceontheproprietarydataset.Valuesaremean±std.dev.
across10folds.
Model Accuracy ROCAUC PRAUC Recall(Normal) Recall(Fraud) Precision(Fraud) F1(Fraud)
GBT 0.969±0.002 0.886±0.010 0.443±0.030 0.997±0.001 0.226±0.042 0.726±0.066 0.343±0.051
GBT(Weighted) 0.962±0.002 0.891±0.012 0.445±0.030 0.981±0.001 0.450±0.029 0.474±0.030 0.462±0.029
RLFD 0.906±0.012 0.773±0.041 0.222±0.042 0.919±0.012 0.549±0.062 0.197±0.028 0.289±0.036
(a) (b)
(c) (d)
Figure2. AggregatedROCandPrecision–Recallcurvesfromthe10-foldcross-validationonthe
proprietarydataset,comparingtheRLFD(DQN-based)frameworkandtheGBTmodel.(a)RLFD
GlobalROCCurve.(b)RLFDGlobalPrecision–RecallCurve.(c)GBTGlobalROCCurve.(d)GBT
GlobalPrecision–RecallCurve.IntheROCplots(a,c),thebluedasheddiagonallinerepresentsthe
performanceofarandomclassifier(AUC=0.5).
4.3. OrthogonalityandComplementaryDetection
TobetterunderstandtheoperationalvalueoftheRLFDframeworkbeyondaggre-
gate metrics, we performed a dynamic orthogonality analysis. Instead of relying on a
singleoverlapsnapshot,weexaminedtheintersectionofdetectedfraudsacrossdifferent
operatingpointsontheholdoutset.
Figure 3a displays the overlap composition as a function of the target fraud recall.
Whilethesymmetrybetweentheuniquesetsismathematicallyenforcedbyequatingthe
recallofbothmodels,themagnitudeoftheseuniquesetsisrelevant. Ifthemodelsrelied
on similar decision boundaries, the “Common” area would dominate and the unique
bandswouldbenegligible. Instead,thepersistentwidthofthe“UniquetoRLFD”band
demonstratesthatforanygivensensitivitylevel,theRLFDagentcapturesasubstantial
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 11of16
volumeoffraudthattheGBTinherentlymisses, provingthattheagentisnotmerelya
redundantclassifierbutasourceoforthogonalinformation.
Figure 3b visualizes the overlap as a function of the decision threshold, moving
fromstrict(highprobability)toloose(lowprobability)classifiers. Atverystrictthresholds
(e.g.,>0.8),theRLFDagentisnotablymoreeffective,capturingthevastmajorityofdetected
frauds. EvenasthethresholdisloweredandtheGBTbecomesmoreeffective,theRLFD
agentcontinuestocontributeadistinctsetofuniquedetections,comprisingapproximately
30%ofthetotalunionofdetectedfraudsatthreshold0.4,andover40%uniquecasesat
threshold0.5,thatarenevercapturedbythetree-basedmodel.Thispersistentorthogonality
confirmsthatthetwomodelsrelyonfundamentallydifferentdecisionboundaries: the
GBTexploitsfeatureinteractionsintabularspace,whiletheRLagentleveragestemporal
transitionstocatchsequentialanomalies.
(a)Overlapvs.TargetRecall
(b)Overlapvs.DecisionThreshold
Figure3.DynamicorthogonalityanalysisbetweentheRLFDagentandtheGBTbaseline.(a)Evolu-
tionoffraudoverlapasafunctionoftargetfraudrecall(sensitivity).(b)Evolutionoffraudoverlap
asafunctionofthedecisionthreshold(probabilitycut-off),orderedfromstrict(1.0)toloose(0.0).In
bothviews,theblueareahighlightstheuniquecontributionoftheRLFDagent,whichpersistsacross
alloperatingpoints.
4.4. UCIBenchmarkPerformance
Toaddressourthirdresearchquestionregardinggeneralizability,weevaluatedthe
frameworkontheUCICreditCardDefaultdataset. Thisenvironmentdiffersfundamen-
tallyfromtheproprietarybankdataset: thesequencesareshort(only6time-steps),the
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252
12of16
granularity is coarse (monthly aggregates vs. timestamps), and the class imbalance is
moderate(22%vs. 3.6%).
Consequently,theagent’shyperparametersrequiredlogicaladaptation,asdetailed
in Table 4. The window_size was reduced to 4 to accommodate the limited six-month
history available per client. Furthermore, the positive reward scalar (r1) was lowered
from4.0to3.0;becausethedefaultclassislessrarethanbankingfraud,theagentrequires
lessaggressiveincentivizationtolearntheminorityclassdistribution.
Table4.KeyhyperparametersfortheUCIbenchmarkexperiment.
| Hyperparameter           | Value |     |
| ------------------------ | ----- | --- |
| window_size              |       | 4   |
| hidden_size(LSTM)        |       | 32  |
| r1(Positive-classreward) |       | 3.0 |
r2(Negative-classreward)
1.0
| learning_rate | 0.001 |     |
| ------------- | ----- | --- |
The comparative results are presented in Table 5. Our RLFD framework achieves
an Accuracy of 0.802 and a ROC AUC of 0.696. When compared to the suite of static
classifiersevaluatedbySeeraetal.[10],theRLagentperformscompetitivelywithstandard
distance-basedmethods(e.g.,k-NN)buttrailsbehindensembletreemethodslikeGBT
(Accuracy0.821,ROCAUC0.778).
This result provides a relevant boundary condition for our research questions. It
suggeststhattheRLFDframework’sadvantageisheavilydependentonthepresenceof
high-frequencysequentialsignals. IntheUCIdataset,wheretemporalresolutionislow
(monthly snapshots) and feature interactions are largely static, the GBT leverage their
superiorabilitytopartitiontabularspace. However,thefactthattheRLagentmaintainsro-
bustperformance(within2%Accuracyofthestate-of-the-art)despitebeingarchitecturally
optimizedforsequentialtasksconfirmsitsflexibilityacrossdifferentfinancialdomains.
Table 5. Comparison of RLFD performance on the UCI benchmark against results reported by
Seeraetal.[10]. BoldvaluesindicatetheperformanceoftheproposedRLFDframework. Source
resultsfromFengetal.[20]andJadhavetal.[21]. Accuracyisreportedasaproportionin[0,1].
Acronyms: k-NN,k-nearestneighbours;NB,NaïveBayes;SVM,supportvectormachine;BagDT,
baggeddecisiontrees;BagNN,baggedneuralnetworks;BagSVM,baggedsupportvectormachines.
| Model             | Accuracy | ROCAUC |
| ----------------- | -------- | ------ |
| k-NN[21]          | 0.8080   | 0.627  |
| NB[21]            | 0.7136   | 0.699  |
| SVM[20]           | 0.8200   | 0.643  |
| RandomForest[20]  | 0.8200   | 0.625  |
| BagDT[20]         | 0.8200   | 0.665  |
| BagNN[20]         | 0.8200   | 0.660  |
| BagSVM[20]        | 0.8100   | 0.620  |
| NeuralNetwork[20] | 0.8205   | 0.660  |
| GBT[10]           | 0.8206   | 0.778  |
| RLFD              | 0.8016   | 0.696  |
5. Discussion
This study aimed to evaluate the efficacy of reinforcement learning for financial
frauddetection,specificallyaddressingthecapabilityofsequentialagentstoidentifyrare
eventsinhighlyimbalanceddomains. Interpretingourfindingsthroughthelensofthe
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 13of16
primaryresearchquestionsrevealsadistincttrade-offbetweenstatisticalrankingpower
andoperationalcoverage.
Regardingthefirstresearchquestionondetectionefficacy,theempiricalresultson
the proprietary dataset affirm that the RLFD agent can achieve superior recall for rare
eventscomparedtostaticbaselines. WhilethestandardGBTmodelprioritizedprecision,
resultinginalowfraudrecallof0.226,theRLFDagentleveragedtheasymmetricreward
signal(r /r =4)toachieveafraudrecallof0.549. Thisdemonstratesthatinoperational
1 2
contextswherethefinancialliabilityofafalsenegativevastlyoutweighsthefrictioncostof
afalsepositive,theRLframeworkoffersamoretunableandeffectiveoptimizationobjec-
tivethanstandardcross-entropylossminimization. Regardingcomputationalefficiency,
theRLFDframeworkrequiressignificantlyhighertrainingresourcescomparedtoGBT
(approximately2×wall-clocktimeinourexperiments)duetotheepisodicnatureofthe
interactionloop. However,inferencelatencyremainscomparable,asthetrainedQ-network
processessequencewindowsinconstanttime.
Themostrelevantfinding,however,addressestheoperationalorthogonalityofthe
models.ThedynamicorthogonalityanalysispresentedinFigure3providesstrongevidence
thattheRLFDframeworkdetectsadistinctsubsetoffraudulentactivities. Thepersistence
ofthe“UniquetoRLFD”detectionbandacrosstheentirethresholdspectrumindicates
thattheagentisnotmerelyactingasanoisierclassifier,butissensitivetofundamentally
differentpatternsthatareinvisibletothetree-basedmodel. Notably,athigh-confidence
thresholds,theRLagentcontributedover30%oftheuniquedetections. Thisconfirmsits
valueasacomplementarysafetynetthatcapturestemporalcorrelationsmissedbythe
independenceassumptionofstaticclassifiers.
Todefinetheboundaryconditionsofthisapproach,weexaminedtheframework’s
performance on the UCI benchmark, which lacks high-frequency temporal data. The
resultsshowthatwhileRLFDiscompetitive(Accuracy0.802),itdoesnotoutperformthe
GBT(Accuracy0.821)inpurelytabularenvironments. Thisestablishesaclearlimitation:
theRLFDframeworkprovidesmaximumvalueindomainswithrichsequentialsignals
(e.g.,timestampedbankinglogs)andoffersdiminishingreturnsinstaticclassificationtasks
wherefeatureinteractionsdominate.
These findings have both theoretical and practical implications. Theoretically, the
studyreinforcesthedistinctionbetweenclassificationerrorminimizationandoperational
utilitymaximization.ByframingfrauddetectionasaMarkovDecisionProcess,thedecision
boundaryisallowedtoevolvebasedonthesequentialstateoftheclient,contrastingwith
thefixedhyperplaneapproachesofsupervisedlearning. Methodologically,ouranalysis
highlights the danger of relying solely on global metrics like ROC AUC or Accuracy
in highly imbalanced settings, a choice made on the UCI benchmark to align with the
comparativeanalysisbySeeraetal.[10]. AsshowninTable3,amodelcanachievesuperior
ROC AUC (0.886 vs. 0.773) while failing the primary business objective of detecting
fraud(Recall0.22vs. 0.55). Consequently,futurecomparisonsshouldprioritizethreshold-
dependentmetricsanddynamicoverlapanalyses.Fromapracticalstandpoint,thefindings
speak against a “winner-takes-all” model selection. The optimal strategy for financial
institutions is possibly an hybrid parallel deployment: using GBTs as a primary high-
precisionfilter,whiledeployingRLagentsinparalleltointerceptthesignificantfractionof
complex,sequentialattacksthatbypassstaticrules.
6. Conclusions
We adapted and evaluated a Reinforcement Learning for Fraud Detection (RLFD)
framework alongside a Gradient Boosted Trees (GBTs) baseline on both a proprietary,
real-world financial dataset and a public credit default benchmark. The investigation
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 14of16
revealsthatstatisticalsuperiority(asmeasuredbyAreaUndertheCurve,AUC)doesnot
necessarilyimplyoperationalcompleteness. WhiletheGBTbaselineprovidesarobust
primaryfilterwithhighprecision,ourdynamicorthogonalityanalysisprovesitremains
blind to specific anomalies across the entire decision spectrum. The RLFD framework,
employinganepisodictrainingloop,asymmetricrewardshaping,andLSTM-basedstate
encoding, successfullycapturestheseelusivepatterns. Ontheproprietarydataset, this
approachconsistentlyidentifiesauniquesetoffraudulenttransactionsthattheGBTmisses;
conversely, on the static public benchmark, the sequential advantage diminishes. We
thereforecautionthatthemagnitudeofthecomplementaryeffectobservedhere(e.g.,the
≈30%uniquedetections)islikelydataset-dependentandcontingentontheprevalenceof
high-frequencysequentialpatternsinthetargetfinancialstream.
We conclude that the optimal deployment strategy for financial fraud detection is
notamonolithicchoicebetweenstaticorsequentialmodels,butratherahybridparallel
architecture. In such a system, the RLFD agent serves as a specialized “safety net” for
complex,sequence-dependentfraudscenariosthatevadetraditionaltree-basedclassifiers,
therebysignificantlyenhancingthetotalfraudcoverageofthebankingsystem. Future
evolutionofthisframeworkwillfocusontheintegrationofExplainableAI(XAI)methods
to bridge the gap between the high sensitivity of Deep RL agents and the regulatory
requirementforinterpretabilityinthefinancialsector.
AuthorContributions:Conceptualization,A.P.;Methodology,A.P.;Software,A.P.;Validation,A.P.;
Formalanalysis,A.P.;Investigation,A.P.;Writing—originaldraft,A.P.;Writing—review&editing,
A.P.,B.C.,P.L.andR.C.;Visualization,A.P.andP.L.;Supervision,P.L.andR.C.Allauthorshaveread
andagreedtothepublishedversionofthemanuscript.
Funding:ThisresearchwasfundedbytheEuropeanUnion—NextGenerationEUundertheNational
RecoveryandResiliencePlan(PNRR)—Missione4“IstruzioneeRicerca”—Componente2“Dalla
Ricercaall’Impresa”—Investimento1.4“CampioninazionalidiR&S”,Project“NationalCentrefor
HPC,BigDataandQuantumComputing”—CN1(Spoke2)“Simulazioni,calcoloeanalisideidatiad
alteprestazioni”,CUP:B83C22002830001.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Theproprietarydatasetusedinthisstudyconsistsofbanktransactions
protectedbylegalandcontractualrestrictions;rawdatacannotbeshared. Thepublicbenchmark
datasetisavailableattheUCIMachineLearningRepositoryathttps://archive.ics.uci.edu/dataset/
350/default+of+credit+card+clients(accessedon21December2025).
Acknowledgments:WethankIntesaSanpaoloforprovidingtheanonymizeddatasetforthisresearch.
Theviewsandopinionsexpressedarethoseoftheauthorsanddonotnecessarilyreflecttheviewsof
IntesaSanpaolo,itsaffiliates,oritsemployees.
ConflictsofInterest:AuthorRiccardoCrupiwasemployedbythecompanyIntesaSanpaoloS.p.A.
Theremainingauthorsdeclarethattheresearchwasconductedintheabsenceofanycommercialor
financialrelationshipsthatcouldbeconstruedasapotentialconflictofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
APP AuthorizedPushPayment
ATO AccountTakeover
AUC AreaUndertheCurve
BagDT BaggedDecisionTrees
BagNN BaggedNeuralNetworks
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 15of16
BagSVM BaggedSupportVectorMachines
BIC BankIdentifierCode
DQN DeepQ-Network
GBT GradientBoostedTrees
ISP IntesaSanpaolo
k-NN k-NearestNeighbours
LSTM LongShort-TermMemory
MDP MarkovDecisionProcess
MI MutualInformation
NB NaïveBayes
PR Precision–Recall
RL ReinforcementLearning
RLAD ReinforcementLearningforAnomalyDetection
RLFD ReinforcementLearningforFraudDetection
ROC ReceiverOperatingCharacteristic
SHA-256 SecureHashAlgorithm256-bit
SVM SupportVectorMachine
TD TemporalDifference
UCI UniversityofCaliforniaIrvine(Repository)
XAI ExplainableArtificialIntelligence
References
1. Compagnino,A.A.;Maruccia,Y.;Cavuoti,S.;Riccio,G.;Tutone,A.;Crupi,R.;Pagliaro,A. Anintroductiontomachinelearning
methodsforfrauddetection. Appl.Sci.2025,15,11787.[CrossRef]
2. HernandezAros,L.;BustamanteMolano,L.X.;Gutierrez-Portela,F.;MorenoHernandez,J.J.;RodríguezBarrero,M.S. Financial
frauddetectionthroughtheapplicationofmachinelearningtechniques:Aliteraturereview. Humanit.Soc.Sci.Commun.2024,
11,1130.[CrossRef]
3. Ali,A.;AbdRazak,S.;Othman,S.H.;Eisa,T.A.E.;Al-Dhaqm,A.;Nasser,M.;Elhassan,T.;Saif,A. Financialfrauddetectionbased
onmachinelearning:Asystematicliteraturereview. Appl.Sci.2022,12,9637.[CrossRef]
4. Al-Hashedi,K.G.;Magalingam,P. Financialfrauddetectionapplyingdataminingtechniques:Acomprehensivereviewfrom
2009to2019. Comput.Sci.Rev.2021,40,100402.[CrossRef]
5. West, J.; Bhattacharya, M. Intelligent financial fraud detection: A comprehensive review. Comput. Secur. 2016, 57, 47–66.
[CrossRef]
6. Abdallah,A.;Maarof,M.A.;Zainal,A. Frauddetectionsystem:Asurvey. J.Netw.Comput.Appl.2016,68,90–113.[CrossRef]
7. Ngai,E.W.T.;Hu,Y.;Wong,Y.h.;Chen,Y.;Sun,X. Theapplicationofdataminingtechniquesinfinancialfrauddetection: A
classificationframeworkandanacademicreviewofliterature. Decis.SupportSyst.2011,50,559–569.[CrossRef]
8. Bolton,R.J.;Hand,D.J. Statisticalfrauddetection:Areview. Stat.Sci.2002,17,235–255.[CrossRef]
9. Wu,T.;Ortiz,J. RLAD:Timeseriesanomalydetectionthroughreinforcementlearningandactivelearning. InProceedings
ofthe7thACMSIGKDDWorkshoponMiningandLearningfromTimeSeries(MiLeTS’21),VirtualEvent,Singapore,14–18
August 2021.
10. Seera,M.;Lim,C.P.;Kumar,A.;Dhamotharan,L.;Tan,K.H. Anintelligentpaymentcardfrauddetectionsystem. Ann.Oper.Res.
2024,334,445–467.[CrossRef][PubMed]
11. Jurgovsky, J.; Granitzer, M.; Ziegler, K.; Calabretto, S.; Portier, P.E.; He-Guelton, L.; Caelen, O. Sequence classification for
credit-cardfrauddetection. ExpertSyst.Appl.2018,100,234–245.[CrossRef]
12. Sutton,R.S.;Barto,A.G. ReinforcementLearning:AnIntroduction,2nded.;MITPress:Cambridge,MA,USA,2018.
13. Penard,W.;VanWerkhoven,T. Onthesecurehashalgorithmfamily. InCryptographyinContext;Wiley:Hoboken,NJ,USA,2008;
pp.1–18. Availableonline:https://blog.infocruncher.com/resources/ethereum-whitepaper-annotated/On%20the%20Secure%
20Hash%20Algorithm%20family%20%282008%29.pdf(accessedon21December2025).
14. Dua, D.; Graff, C. UCIMachineLearningRepository. 2019. Availableonline: http://archive.ics.uci.edu/ml (accessedon
10November2025).
15. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.;
Ostrovski,G.;etal. Human-levelcontrolthroughdeepreinforcementlearning. Nature2015,518,529–533.[CrossRef][PubMed]
16. Hochreiter,S.;Schmidhuber,J. Longshort-termmemory. NeuralComput.1997,9,1735–1780.[CrossRef]
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 16of16
17. Ramírez-Alpízar,A.;Jenkins,M.;Martínez,A.;Quesada-López,C. Useofdataminingandmachinelearningtechniquesforfraud
detectioninfinancialstatements:Asystematicmappingstudy. RISTI—Iber. J.Inf. Syst. Technol. 2020,E28,97–109. Available
online:https://www.risti.xyz/issues/ristie28.pdf(accessedon21December2025).
18. Bakumenko,A.;Elragal,A. Detectinganomaliesinfinancialdatausingmachinelearningalgorithms. Systems2022,10,130.
[CrossRef]
19. Saito,T.;Rehmsmeier,M. Theprecision–recallplotismoreinformativethantheROCplotwhenevaluatingbinaryclassifierson
imbalanceddatasets. PLoSONE2015,10,e0118432.[CrossRef][PubMed]
20. Feng,X.;Xiao,Z.;Zhong,B.;Qiu,J.;Dong,Y. Dynamicensembleclassificationforcreditscoringusingsoftprobability. Appl.Soft
Comput.2018,65,139–151.[CrossRef]
21. Jadhav,S.;He,H.;Jenkins,K. Informationgaindirectedgeneticalgorithmwrapperfeatureselectionforcreditrating. Appl.Soft
Comput.2018,69,541–553.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/app16010252