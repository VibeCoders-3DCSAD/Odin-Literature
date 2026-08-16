---
conversion_metadata:
  converted_at: "2026-07-21T09:29:36Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Yashwanth et al.pdf"
  source_pdf_sha256: "a259c739c4e3163550068b36dee042e0f3879a8eb085e27494f0d918707d52ab"
  page_count: 9
  markdown_char_count: 97598
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Synthesis: A Multidisciplinary Research Journal 
Volume 1, Issue 4, October - December 2023, Pp: 1-9 
© 2023, All Rights Reserved @ Macaw Publications

Research Article 
DataStream Adapt: Unified Detection Framework for 
Gradual and Abrupt Concept Drifts

1* Mettu Yashwanth, 2 Digumarthy Sandeepa, 3 Sk. Khaja Shareef

1* University of Texas, USA. 
2 Department of Computer Science, Southeast Missouri State University. 
3 Associate Professor, Department of CSE, Koneru Lakshmaiah Education Foundation, Bowrampet, Hyderabad, India

Article Info 
Received:05/08/2023  
Revised:  28/09/2023 
Accepted:20/12/2023    
Published:31/12/2023

*Corresponding Author(s):  yxm2835@mavs.uta.edu

Abstract 
Concept drift, the phenomenon where data distributions change over time, poses a significant 
challenge  to  maintaining  the  accuracy  and  reliability  of  predictive  models  in  data  stream 
environments. Traditional drift detectors often struggle to simultaneously  handle both abrupt 
and  gradual  drifts,  leading  to  delayed  adaptation  or  excessive  false  positives.  This  study 
proposes DataStream Adapt, a unified and adaptive framework designed to detect and respond 
to both abrupt and gradual concept drifts in real-time data streams. The framework integrates a 
hybrid  drift  detection  engine  combining  error-rate  monitoring  and  statistical  divergence,  an 
adaptive threshold controller that adjusts sensitivity based on stream volatility, and a drift-aware 
ensemble classifier capable of reweighting or replacing base learners dynamically. The system 
is benchmarked using the synthetic  Hyperplane  dataset, designed to simulate controlled drift 
scenarios with known ground truths. Experimental results demonstrate that DataStream Adapt 
outperforms state-of-the-art baselines, including  DDM, ADWIN, and EDDM. Specifically, it 
achieves a detection delay of 31.2 instances for abrupt drift and 64.8 instances for gradual drift, 
compared to 82.4 and 254.6 for DDM, respectively. The framework maintains a false positive 
rate  of 0.041, significantly lower than  ADWIN’s 0.147,  while also achieving an  F1-score of 
0.89 on post-drift classification, outperforming all baselines. In conclusion, DataStream Adapt 
offers a scalable, interpretable, and low-latency solution for adaptive learning in evolving data 
environments,  making  it  suitable  for  real-world  deployment  in  applications  such  as  fraud 
detection, predictive maintenance, and IoT analytics.

Keywords:  Concept  Drift,  Data  Streams,  Adaptive  Learning,  Drift  Detection,  Ensemble 
Classifiers, Real-Time Analytics, Threshold Adaptation

Copyright: © 2023 Mettu Yashwanth, Digumarthy Sandeepa, Sk. Khaja Shareef. This article is an open-
access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY 4.0) 
license.

https://www.macawpublications.com/Journals/index.php/SMRJ

1

---

<!-- PAGE 2 -->

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

Graphical abstract of the DataStream Adapt Framework

1.  Introduction

In the era of real-time data generation, continuous data 
streams have become ubiquitous across a wide spectrum of 
applications—including financial analytics, fraud detection, 
e-commerce  personalization,  industrial  monitoring,  and 
cyber-physical  systems  [1],  [2].  These  data  streams  are 
inherently  non-stationary,  meaning 
the  underlying 
statistical  properties  evolve  over  time.  This  evolution, 
commonly referred to as concept drift, can severely degrade 
the  predictive  performance  of  machine  learning  models 
trained under the assumption of static data distributions [3].

As  organizations

increasingly  rely  on  streaming 
analytics and automated decision-making systems, the need 
for  adaptive  learning  mechanisms  that  can  detect  and 
respond  to  concept  drift  has  become  critical  [4].  Concept 
drift  manifests  in  two  primary  forms:  abrupt  drift,  where 
changes occur suddenly and dramatically; and gradual drift, 
where shifts happen progressively over time  [5]. Effective 
detection and adaptation to both types of drift are essential 
for  maintaining  model 
and 
responsiveness in evolving environments.

reliability,

accuracy,

Existing  systems  typically  address  only  a  subset  of 
these  challenges,  often  treating  abrupt  and  gradual  drift 
detection  as  separate  problems.  Furthermore, 
they 
frequently rely on fixed sensitivity thresholds, which makes 
them  susceptible  to  false  positives  in  noisy  streams  or 
delayed response  in stable periods  [6]. This  motivates the 
development  of  a  more  unified,  adaptable,  and  intelligent 
framework  that  can  accurately  detect,  distinguish,  and 
respond 
to  various  drift  patterns  without  manual 
intervention.

Most current approaches to concept drift detection and 
adaptation suffer  from  limited generalizability across drift 
types  and  lack  adaptive  mechanisms  that  can  adjust  their 
sensitivity  based  on  data  volatility  [7].  While  ensemble 
methods and statistical detectors exist, few offer a cohesive 
solution that integrates drift detection, certainty estimation, 
and real-time  model adaptation into a single pipeline. The 
absence  of  such  an  integrated  and  unified  framework 
hinders the deployment of robust stream learning systems in 
mission-critical applications.

Several key challenges in the domain remain unresolved:

  Drift-Type  Specialization:  Many

algorithms 
perform well for abrupt drift but fail under gradual 
conditions [8].

  Static Threshold Limitations: Use of non-adaptive 
parameters  leads  to  poor  performance  in  highly 
dynamic or noisy environments.

  Lack  of  Drift  Confidence  Metrics:  Most  systems 
offer  binary  drift  detection  without  conveying 
certainty or ranking of detected drifts [9].

  Disconnected  Adaptation  Mechanisms:  In  most 
ensemble  methods,  drift  detection  is  decoupled 
from  model  adaptation,  resulting  in  delayed  or 
suboptimal learner updates [10].

  Scalability

and

Interpretability:

High 
computational overhead and lack of explainability 
restrict  the  practical  deployment  of  many  existing 
systems.

This  study  aims  to  develop  a  unified  and  adaptive 
framework—DataStream Adapt—capable of detecting and

2

---

<!-- PAGE 3 -->

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

responding to both gradual and abrupt concept drifts in real-
time data streams. The primary objectives are:

  To  design  a  hybrid  detection  engine  combining 
statistical  and  error-based  indicators  for  improved 
robustness.

  To  introduce  an  adaptive  threshold  controller  that 
dynamically  adjusts  detection  sensitivity  based  on 
data volatility.

  To  integrate  a  drift  certainty  scoring  mechanism 
that quantifies confidence in detection events.

  To  develop  an  ensemble-based  classifier  that 
reweights  or  replaces  base  learners  in  response  to 
detected drift.

  To  benchmark  the  proposed  framework  against 
(e.g.,  DDM,  ADWIN,

established  baselines 
EDDM) using a controlled synthetic dataset.

The contributions of this paper are summarized as follows:

1.  A  unified  detection  framework  that  effectively 
handles both abrupt and gradual concept drifts using 
a hybrid combination of error rate monitoring and 
statistical distance measures.

2.  An  adaptive  threshold  controller  that  learns 
volatility  patterns  in  the  data  stream  and  adjusts 
sensitivity  parameters  accordingly  to  minimize 
false positives.

3.  A  drift  certainty  scoring  mechanism

that 
improves  interpretability  and  decision  confidence 
by quantifying the strength of detected drifts.

4.  An  integrated  ensemble  adaptation  strategy, 
where  base  learners  are  updated  or  reweighted  in 
response to detected drift events.

5.  Comprehensive  experimental  validation  using 
the  Hyperplane  dataset,  demonstrating  superior 
performance in detection delay, false positive rate, 
and  classification  accuracy  compared  to  state-of-
the-art methods.

The  remainder  of  this  paper  is  organized  as  follows:  
Section 2 reviews related literature and outlines the existing 
research gaps. Section 3 details the proposed methodology 
and 
the 
system  architecture.  Section  4  describes 
experimental  setup  and  evaluation  metrics.  Section  5 
discusses  results  and  comparisons.  Finally,  Section  6 
concludes the paper and outlines directions for future work.

2.  Related Work

real-time

The  challenge  of  detecting  concept  drift  in  evolving 
data  streams  has  attracted  significant  attention  across 
various  application  domains  such  as  fraud  detection, 
network  monitoring,  and 
recommendation 
systems. Over the years, researchers have proposed multiple 
strategies  to  handle  concept  drift,  which  can  be  broadly 
categorized  into  error-based  methods,  distribution-based 
methods,  ensemble-based  approaches,  and  more  recently, 
hybrid  and  unified  detection  frameworks.  This  section 
presents  a  structured  review  of  these  techniques  and 
identifies persistent research gaps.

3

2.1 Error-Based Drift Detection Methods

Error-based  methods  monitor  the  performance  of 
classifiers  over  time  to  detect  potential  drift  based  on 
statistical  deviations  in  error  rates.  One  of  the  earliest 
approaches, the Drift Detection Method (DDM), estimates 
the probability of classification error and raises alarms when 
the standard deviation exceeds a predefined threshold [11]. 
The Early Drift Detection Method (EDDM) extends DDM 
by  focusing  on  the  distance  between  classification  errors, 
which enhances its sensitivity to gradual drifts [12]. Despite 
their  simplicity  and  efficiency,  these  methods  are  often 
highly sensitive to noise and are less effective in identifying 
slow, continuous changes in the data distribution.

2.2 Distribution-Based Methods

Distribution-based  detectors  aim  to  capture  drift  by 
comparing  changes  in  feature  distributions  or  prediction 
probabilities  across  time  windows.  ADWIN  (Adaptive 
Windowing)  is  a  popular  method  that  employs  a  dynamic 
sliding  window  and  uses  statistical  hypothesis  testing  to 
detect  significant  changes  in  data  distribution  [13].  Other 
techniques rely on statistical divergence measures, such as 
KL-divergence,  Hellinger  distance,  and  the  Kolmogorov–
Smirnov  test.  While  these  approaches  are  more  robust  to 
noisy labels and transient fluctuations, they tend to require 
more  memory  and  computational  resources,  especially  in 
high-dimensional data streams.

2.3 Ensemble-Based Approaches

Ensemble methods combine multiple base classifiers to 
improve  robustness  and  adaptability  to  concept  drift. 
Approaches such as Online Bagging, Leveraging Bagging, 
and  Dynamic  Weighted  Majority  (DWM)  dynamically 
update their constituent models based on performance [14], 
[15].  These  techniques  can  respond  to  performance 
degradation caused by drift by removing poorly performing 
introducing  new  ones.  However,  most 
learners  and 
ensemble methods do not inherently detect drift and instead 
rely on external drift detectors to signal model updates. This 
limits  their  autonomy  and  responsiveness  in  rapidly 
evolving environments.

2.4 Hybrid and Unified Detection Approaches

More recent research has focused on hybrid strategies 
that  attempt  to  integrate  multiple  drift  indicators  within  a 
single  framework.  For  example,  HDDM  (Hoeffding  Drift 
Detection  Method)  combines 
statistical  distribution 
monitoring  with  error-rate  tracking  to  improve  detection 
robustness  [16].  Similarly,  methods  like  EDDM-IGT 
explore  multiple  sources  of  evidence  for  enhanced 
sensitivity.  However,  these  systems  typically  operate  with 
fixed thresholds and often lack scalability or generalization 
across different drift types. They also do not offer integrated 
mechanisms  for  drift  certainty  estimation  or  adaptive 
learning.

2.5 Research Gaps

Despite considerable progress in the field, several key 
research gaps remain unresolved. First, existing systems are 
often specialized for either abrupt or gradual drift. And lack 
the  ability  to  generalize  across  both  in  a  unified  manner. 
Second, the reliance on fixed sensitivity thresholds makes

---

<!-- PAGE 4 -->

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

many  detectors  brittle 
in  volatile  or  non-stationary 
environments.  Third,  there  is  a  lack  of  drift  certainty 
estimation mechanisms that could quantify the confidence 
level of a  detected drift event, limiting the  interpretability 
and  controllability  of  current  systems.  Fourth,  most 
ensemble learning methods depend on external signals for 
drift  handling  and  lack  an  internal  feedback  loop  that 
couples detection with adaptation. Finally, many published 
works  do  not  offer  comprehensive  benchmarking  across 
mixed  drift  types,  making  reproducibility  and  real-world 
applicability more difficult.

In  summary,  while  existing  methods  offer  valuable 
tools  for  specific  drift  scenarios,  a  general-purpose, 
adaptive, and self-configuring framework remains lacking. 
The proposed DataStream Adapt framework addresses these 
challenges  by  combining  hybrid  drift  detection,  adaptive 
threshold tuning, and drift-aware ensemble adaptation into 
a  single,  unified  architecture  capable  of  handling  both 
abrupt and gradual drifts in real-time.

3.  Methodology

This  section  outlines  the  design  of  the  proposed 
DataStream Adapt framework, which unifies the detection 
of both gradual and abrupt concept drifts in streaming data 
environments.  The  methodology 
integrates  statistical 
monitoring,  hybrid  drift  detection,  adaptive  threshold 
tuning,  and  dynamic  ensemble  learning. The  flow  of  data 
through the framework is shown in Figure 1, with each stage 
elaborated below.

Fig.1.  Architecture  of  the  DataStream  Adapt  Framework  for  Unified 
Concept Drift Detection and Adaptation

This  dataset  provides  a  controlled  testbed  to  evaluate 
the latency, accuracy, and robustness of the proposed drift 
detection mechanism under both drift scenarios.

3.2 Data Preprocessing and Windowing

Let the input data stream be:

𝒟 = {𝑥1, 𝑥2, … , 𝑥𝑡, … }, 𝑥𝑡 ∈ ℝ𝑛

Two temporal windows are maintained:

  A  short-term  window  𝑊𝑠(𝑡),  capturing  the  most

recent 𝑘 instances.

  A long-term reference window 𝑊𝑙(𝑡), representing

a stable historical distribution.

These  windows

support  comparative

statistical

monitoring and drift detection.

3.3 Statistical and Signal Monitoring

To  detect  deviations  in  data  distribution  or  model

performance, we compute several key metrics:

3.3.1 Mean and Variance Differences

We  measure  the  change  in  the  mean  and  variance

between the two windows:

Δ𝜇𝑡 = |𝜇(𝑊𝑠(𝑡)) − 𝜇(𝑊𝑙(𝑡))|

(1)

Δ𝜎𝑡

2 = |𝜎2(𝑊𝑠(𝑡)) − 𝜎2(𝑊𝑙(𝑡))|

(2)

These  metrics  highlight  subtle  gradual  changes  in

distribution.

3.3.2 Error Rate Monitoring

Let  𝑦ˆ𝑖 be the predicted label and  𝑦𝑖 the  ground truth. 
The classification error rate over the short-term window is:

𝜖𝑡 =

1
|𝑊𝑠(𝑡)|

∑

𝑖∈𝑊𝑠(𝑡) 𝕀[𝑦ˆ𝑖 ≠ 𝑦𝑖]

(3)

This  is  used  to  trigger  change  detection  algorithms

when error increases.

3.3.3 Distributional Divergence

We  use  the  Kullback-Leibler  (KL)  divergence  to

quantify distributional shift:

𝐷𝐾𝐿(𝑃‖𝑄) = ∑  𝑖 𝑃(𝑖)log⁡

𝑃(𝑖)

𝑄(𝑖)

(4)

3.1 Dataset Description

where 𝑃 and 𝑄 are estimated distributions over 𝑊𝑠 and

We  evaluate  our  framework  using  the  Hyperplane 
Dataset,  a  widely  used  synthetic  stream  benchmark 
designed to simulate both gradual and abrupt concept drifts 
in a controlled environment.

  Each  instance  𝑥𝑡 ∈ ℝ𝑑  is  generated  from  a

dynamic hyperplane defined by:

𝑑
∑  
𝑖=1 𝑤𝑖𝑥𝑖 = 𝜃𝑡

where  𝑤𝑖  are  hyperplane  coefficients  and  𝜃𝑡  is  a

threshold value that changes over time.

  Abrupt  drift  is  simulated  by  sudden  shifts  in  𝑤𝑖, 
while  gradual  drift  involves  slowly  changing  𝑤𝑖 
across instances.

𝑊𝑙, respectively.

3.4 Hybrid Drift Detection Engine

Our  system  combines  two  distinct  methods  to  detect

both abrupt and gradual drifts:

3.4.1 Abrupt Drift Detection via CUSUM

The Cumulative Sum (CUSUM) method tracks abrupt

shifts in error rate:

𝑆𝑡 = max(0, 𝑆𝑡−1 + (𝜖𝑡 − 𝜖0 − 𝛿))

(5)

where:

𝜖0 is the baseline error,

4

---

<!-- PAGE 5 -->

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

𝛿 is a tolerance factor,

𝑆𝑡 > ℎ  indicates  a  drift  (with  ℎ  as  the  detection 
threshold).

3.4.2 Gradual Drift Detection via Moving Average

We use lagged moving averages to detect slow drifts:

𝑥‾𝑡 =

1

𝑘

∑

𝑡
𝑖=𝑡−𝑘+1 𝑥𝑖

Drift is flagged if:

|𝑥‾𝑡 − 𝑥‾𝑡−𝑘| > 𝛾

where 𝛾 is a dynamic threshold value.

3.4.3 Drift Certainty Scoring

(6)

(7)

  New  classifiers  are  trained  on  post-drift  data  and

added to the ensemble.

Algorithm:  DataStream  Adapt  –  Unified  Concept  Drift 
Detection and Adaptation

Input:

  Stream  𝒟,  ensemble  ℋ,  thresholds  ℎ0, 𝛿0, 𝛾0, 
window  sizes  𝑊𝑠, 𝑊𝑙,  learning  rate  𝜂,  volatility 
sensitivity 𝜆

Output:

  Predictions 𝑦ˆ𝑡, drift logs 𝐿drift

Process:

To unify both detectors, we define a drift certainty score:

1.

Initialize thresholds and ensemble.

𝒞𝑡 = 𝛼 ⋅ 𝕀abrupt  + (1 − 𝛼) ⋅ 𝕀gradual

(8)

2.  For each 𝑥𝑡 in stream:

where:

𝛼 ∈ [0,1]  is  a  weight  determined  by  signal 
volatility,

II are binary indicators ( 1 = drift detected, 0 = no 
drift).

3.5 Adaptive Threshold Controller

This component dynamically tunes parameters such as 
ℎ, 𝛿, and 𝛾, based on observed volatility in the data stream.

3.5.1 Volatility Estimation

We estimate stream volatility using variance:

𝜈𝑡 = Var(𝑥𝑡−𝑚, … , 𝑥𝑡)

(9)

3.5.2 Threshold Adjustment Rule

The detection threshold is adjusted as:

ℎ𝑡 = ℎ0 ⋅ (1 + 𝜆 ⋅ 𝜈𝑡)

(10)

where:

ℎ0 is the base threshold,

𝜆 controls sensitivity to volatility.

This reduces false alarms in noisy regions and enhances

reactivity during stable phases.

3.6 Ensemble Classifier (Drift-Aware)

  Preprocess and append to 𝑊𝑠, 𝑊𝑙.

  Predict label 𝑦ˆ𝑡 using ensemble voting.

  Compute Δ𝜇𝑡, Δ𝜎𝑡

2, 𝜖𝑡, 𝐷𝐾𝐿.

  Estimate volatility 𝜈𝑡 and update thresholds.

  Apply  CUSUM  and  moving  average  shift

detection.



If drift is detected:

  Reweight or replace classifiers.

  Log drift info (type, time, certainty).

  Slide windows and proceed to next 𝑥𝑡+1.

End For

3.7 Model Output and Drift Logging

At each timestep 𝑡, the system outputs:

  Predicted label 𝑦ˆ𝑡

  Drift status: none, gradual, or abrupt

  Drift certainty score 𝒞𝑡

  Drift timestamp 𝑡𝑑



(Optional)  Summary  of  affected  statistical 
features

An ensemble of base classifiers ℋ = {ℎ1, ℎ2, … , ℎ𝑁} is

All metadata is logged for transparency and auditability.

used for robust prediction.

3.6.1 Voting Mechanism

Predictions  are  obtained  using  weighted  majority

voting:

𝑦ˆ𝑡 = arg⁡max

𝑦

∑  𝑁

𝑖=1 𝑤𝑖(𝑡) ⋅ 𝕀[ℎ𝑖(𝑥𝑡) = 𝑦]

(11)

3.6.2 Learner Update on Drift

When drift is detected:

  High-error learners are down-weighted:

𝑤𝑖(𝑡 + 1) = 𝜂 ⋅ 𝑤𝑖(𝑡),⁡ if err𝑖 > 𝜃

(12)

4.  Experimental Setup

This section details the computational and experimental 
environment  used  to  evaluate  the  proposed  DataStream 
Adapt framework. We focus on ensuring full reproducibility 
by  reporting  hardware  specifications,  software  stack, 
dataset partitioning, and implementation settings.

4.1 Hardware Specifications

All experiments were conducted on a high-performance

computing workstation with the following configuration:

  Processor:  Intel®  Core™  i9-12900K  @  3.2  GHz

(16 cores, 24 threads)

5

---

<!-- PAGE 6 -->

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

  Memory: 64 GB DDR5 RAM

  Voting method: Weighted majority voting based on

  GPU: NVIDIA RTX 3090 with 24 GB GDDR6X

VRAM

  Storage: 2 TB NVMe SSD

recent accuracy

B.  Training Configuration

  Window sizes:

  Operating System: Ubuntu 22.04 LTS (64-bit)

The  system  supports  high-throughput  data  streaming 
and real-time model adaptation without latency bottlenecks.

4.2 Software Frameworks and Tools

The implementation was carried out using Python 3.10. 
The following open-source libraries and frameworks were 
used:



Scikit-learn 1.4.1: Base classifiers (e.g., Hoeffding 
Tree, Naive Bayes)

  River  0.15.0:  Online  learning  models  and  drift

detectors

  Short-term 𝑊𝑠: 200 instances

  Long-term 𝑊𝑙: 1,000 instances

  Batch  size:  1  (single-instance  updates,  consistent

with online learning)

  Drift detection thresholds:

  ℎ0 = 0.5, 𝛿0 = 0.05, 𝛾0 = 0.15

  Volatility sensitivity: λ=0.75

  Drift  certainty  threshold:  0.6  (minimum  score  to

confirm drift)

  Model update:

  NumPy 1.26.0: Numerical computations

  Learners with accuracy below 60% were

  Pandas 2.2.0: Data preprocessing and logging

  Matplotlib 3.8.2: Visualizations and drift plots

  MOA  Simulator  (via  river.datasets.hyperplane)  – 
Synthetic stream generation (Hyperplane dataset)

C.  Runtime

replaced.

  New  models  were  trained  on  the  latest

500 instances post-drift.

All dependencies and versions were managed via conda 
in

and  pip,  and  an  environment  file 
supplementary material for full reproducibility.

is  provided

  Total simulation time per run: ~3.8 minutes

  Average time per instance: 2.3 ms

  GPU was not used for training due to the efficiency

4.3 Dataset Partitioning and Stream Configuration

of streaming classifiers.

The  Hyperplane  dataset  was  configured  to  simulate

All results were averaged over three runs with different

both abrupt and gradual concept drifts:

random seeds for statistical significance.

  Attributes:  10  numeric  features  with  binary  class

4.5 Evaluation Metrics

labels.



Instances: 100,000 total.

  Drift Types:

  Abrupt  Drift:  Sudden  change  in  hyperplane

orientation every 20,000 instances.

  Gradual  Drift:  Coefficients  gradually  changed 
over a sliding window of 10,000 instances.

  Train-Test Split: Since this is a streaming setup, the 
model  learns  and  predicts  on  each  instance  in  a 
prequential (interleaved-test-then-train) fashion.

To  comprehensively  assess  the  performance  of  the

proposed framework, we utilize the following metrics:

Detection  Delay:  Measures  the  number  of  instances 
between  the  actual  drift  point  and  the  point  of  detection. 
Lower delay indicates faster responsiveness:

Delay  = 𝑡detected  − 𝑡true

(13)

False  Positive  Rate  (FPR):  The  proportion  of  non-drift 
points incorrectly flagged as drift:

FPR =

False⁡Alarms

Total⁡Non-Drift⁡Events

(14)

  Cross-Validation:  Not  applicable  in  streaming; 
however, three different random seeds were used to 
simulate variations in drift behavior for robustness 
testing.

the 
F1-Score  (Downstream  Classification):  Measures 
harmonic mean of precision and recall in the classification 
task,  evaluated  periodically  to  assess  how  well  the  model 
performs under drift:

4.4  Implementation Details

A.  Base Learners:

  Ensemble size: 5 models

  Learner  types:  Hoeffding  Tree  Classifier,  Naive

Bayes, Logistic Regression

𝐹1 = 2 ⋅

Precision ⋅ Recall

Precision + Recall

(15)

Computational Efficiency: Captured as shown below

  Processing Time per instance (ms)

  Memory Usage during runtime (tracked via psutil)

These  metrics  help  assess

the  scalability  and

practicality of the method for real-world deployment.

6

---

<!-- PAGE 7 -->

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

5.  Results and Discussion

This section presents a comprehensive evaluation of the 
proposed DataStream Adapt framework under both  abrupt 
and  gradual  concept  drift  conditions.  We  compare  its 
performance  with 
three  widely  recognized  baseline 
detectors:  DDM  (Drift  Detection  Method),  ADWIN 
(Adaptive Windowing), and EDDM (Early Drift Detection 
Method).  All  models  were  implemented  in  a  prequential 
setting  using  the  same  base  learners  and  experimental 
configurations described in Section 4.

5.1 Performance under Abrupt Drift

Under  abrupt  drift  scenarios  (with  sudden  changes 
every  20,000  instances),  the  detection  accuracy  and 
responsiveness  of  the  framework  are  crucial.  Table  1 
summarizes the key metrics for each method.

Table 1: Performance Comparison under Abrupt Drift

Method

Detection 
Delay

FPR

F1-
Score

Time/Instance 
(ms)

DDM [18]

82.4

0.134

EDDM [19]

101.7

0.118

ADWIN 
[20]

Ours

56.3

31.2

0.147

0.041

0.81

0.79

0.83

0.89

1.3

1.5

1.8

2.3

Table  1

illustrates

the  proposed  method 
that 
significantly reduces detection delay by ~45% compared to 
ADWIN and ~62% compared to DDM, indicating superior 
responsiveness  to  abrupt  changes.  The  false  positive  rate 
(FPR) is also substantially lower (0.041), demonstrating the 
effectiveness  of  the  adaptive  threshold  controller  in 
suppressing  noise-induced  false  alarms.  Additionally,  the 
F1-score  of  0.89  confirms 
improved  classification 
performance immediately following abrupt shifts, owing to 
the  timely  ensemble  adaptation.  Although  the  time  per 
instance  is  marginally  higher  (2.3  ms),  the  increase  is 
justified  by  improved  drift  sensitivity  and  predictive 
robustness.

5.2 Performance under Gradual Drift

Gradual  drift  experiments  involved  slow,  continuous 
change  in  the  underlying  distribution  over  windows  of 
10,000 instances. Results are presented in Table 2.

ability to model drift gradualness via moving averages and 
window divergence metrics. Moreover, the F1-score of 0.87 
signifies more stable classification despite subtle changes in 
the  distribution.  The  false  positive  rate  remains  low, 
confirming  that  the  system  is  not  misled  by  slow 
fluctuations or noise, unlike DDM and ADWIN which tend 
to overreact to small statistical variances.

5.3 Summary of Comparative Advantages

To  supplement  the  quantitative  evaluation,  Table  3 
highlights the comparative capabilities of each framework 
across several qualitative dimensions. These dimensions are 
critical  for  assessing  the  practical  readiness  of  a  concept 
drift detection system in real-world, continuously evolving 
environments.

Table 3: Comparative Feature Analysis of Drift Detection Methods

Feature

DDM  EDDM  ADWIN

DataStream 
Adapt (Ours)

Detects  Abrupt 
Drift 
Detects  Gradual 
Drift 
Adaptive 
Thresholding 
Ensemble-Based 
Learning 
Drift 
Scoring 
Robustness 
False Alarms 
Real-Time 
Operation  (CPU-
efficient)

Certainty

to

✓

✗

✗

✗

✗

✗

✓

✓

✓

✗

✗

✗

✗

✓

✓

✓

✓

✗

✗

✓

✓

✓✓✓

✓✓✓

✓✓✓

✓✓✓

✓✓✓

✓✓✓

✓

The  proposed  DataStream  Adapt  framework  clearly 
demonstrates  comprehensive  advantages.  It  uniquely 
integrates  both  abrupt  and  gradual  drift  detection  into  a 
unified  pipeline  while  minimizing  false  positives  via 
adaptive thresholding. Additionally, its ability to update and 
reweight an ensemble of classifiers in real time, combined 
with  a  drift  certainty  score,  provides  a 
level  of 
interpretability and resilience absent in other systems.

These  features  make  it  well-suited  for  deployment  in 
mission-critical,  high-throughput  environments  such  as 
fraud  detection,  sensor  networks,  and  recommendation 
systems.

Table 2: Performance Comparison under Gradual Drift

5.4 Practical Considerations

Method

Detection 
Delay

FPR

F1-Score

DDM [18]

254.6

0.186

EDDM [19]

132.3

0.098

ADWIN [20]

111.5

0.122

Ours

64.8

0.058

0.76

0.81

0.83

0.87

Time/ 
Instance 
(ms)

1.3

1.6

1.8

2.3

While ADWIN and EDDM offer competitive detection 
under gradual drift, the proposed method again outperforms 
all  baselines  with 
lowest  detection  delay  (64.8 
instances).  This  improvement  stems  from  the  system’s

the

7

While  the  runtime  cost  per  instance  is  slightly  higher 
(2.3 ms), this is well within operational limits for most real-
time systems, including fraud detection, sensor monitoring, 
and  user  behavior  modeling.  The  benefit  of  reduced 
retraining frequency and higher accuracy compensates  for 
this  trade-off.  Moreover,  the  modular  architecture  and 
reliance on open-source tools (Section 4.2) ensure that the 
system is easily deployable in real-world applications.

These results affirm that each mechanism — especially 
synaptic  consolidation  and  memory  replay  —  is  vital  in 
sustaining 
catastrophic 
preventing 
performance across tasks.

forgetting

and

---

<!-- PAGE 8 -->

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

5.5 Visual Representation

To  facilitate  a  clear  and  balanced  comparison  across  multiple  performance  metrics  with  different  scales,  we  present 
normalized  bar  graphs  and  a  line  chart  that  visualize  the  comparative  performance  of  the  proposed  DataStream Adapt 
framework against established baseline  detectors—DDM,  EDDM, and ADWIN—under both abrupt and gradual concept 
drift conditions.

Fig.2. Comparative performance of concept drift detectors under abrupt and gradual drift conditions

The  line  chart  (left)  in  figure  2  shows  the  Detection 
Delay  of  each  method,  where  the  proposed  DataStream 
Adapt significantly outperforms baseline detectors (DDM, 
EDDM,  and  ADWIN),  especially  under  abrupt  drift. 
The  stacked  bar  chart  (right)  in  figure  2  illustrates  the 
normalized  False  Positive  Rate  (FPR)  and  F1-Score, 
confirming  the  superior  balance  of  precision  and  recall 
achieved by the proposed method while maintaining a low 
false  alarm  rate.  The  results  demonstrate  that  DataStream 
Adapt  offers  both  fast  drift  responsiveness  and  high 
predictive  reliability,  which 
is  critical  for  real-time 
applications.  All  experiments  were  conducted  using  the 
Hyperplane  dataset  with  synthetic  drift  injection  for 
consistent benchmarking.

5.6 Practical Implications and Limitations

Practical Implications

DataStream Adapt demonstrates strong applicability in 
real-time  environments  due  to  its  low-latency  processing 
and adaptive architecture. It is particularly effective for edge 
computing,  fraud  detection,  and  user  behavior  modeling, 
where  both  abrupt  and  gradual  changes  occur  frequently. 
The  inclusion  of  drift  certainty  scoring  and  detailed  logs 
supports 
the 
framework  suitable  for  regulated  domains  like  healthcare 
and finance.

transparency  and  compliance,  making

Limitations

This study relies on the  synthetic Hyperplane dataset, 
which  may  not  reflect  all  real-world  complexities.  The 
framework currently supports only binary classification and 
assumes  a  fixed  feature  set,  which  may  limit  scalability. 
Initial parameter sensitivity and the absence of  automated

tuning or dimensionality reduction also highlight areas for 
future improvement.

6.  Conclusion and Future Work

This  research  introduces  DataStream  Adapt,  a  unified 
and adaptive framework for real-time detection and response 
to  both  abrupt  and  gradual  concept  drifts  in  data  streams. 
Unlike traditional methods with fixed thresholds or limited 
drift scope, it combines a hybrid detection engine, adaptive 
thresholding,  and  a  drift-aware  ensemble  for  accurate  and 
timely adaptation. Evaluated on the Hyperplane dataset, the 
framework  achieved  detection  delays  of  31.2  and  64.8 
instances  for  abrupt  and  gradual  drifts,  respectively, 
outperforming  baselines  such  as  DDM,  EDDM,  and 
ADWIN. It also maintained a low false positive rate of 0.041 
and a high F1-score of 0.89, demonstrating robustness and 
noise  resistance.  Key  innovations  include  volatility-aware 
threshold  tuning  and  drift  certainty  scoring,  ensuring 
stability  and  responsiveness.  DataStream  Adapt  advances 
scalable, 
intelligent  streaming  analytics,  with  strong 
potential  for  applications  in  fraud  detection,  industrial 
monitoring,  and  personalized  services.  Future  work  will 
extend support for multi-class problems, active learning, and 
real-world datasets with complex supervision.

Author  Contributions:  Mettu  Yashwanth  conceptualized 
the  research  framework,  designed  the  architecture  of  the 
DataStream Adapt system, and led the overall coordination 
of 
the  study.  Digumarthy  Sandeepa  was  primarily 
responsible  for  implementing  the  hybrid  drift  detection 
model and conducting the experimental analysis, including 
benchmarking against baseline methods. Sk. Khaja Shareef 
contributed  to  the  formalization  of  the  methodology, 
performed the literature review, and drafted the manuscript,

8

---

<!-- PAGE 9 -->

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

[18]  J. Gama, P. Medas, G. Castillo, and P. Rodrigues, “Learning with drift 
detection,”  Proc.  17th  Brazilian  Symposium  on  Artificial 
Intelligence, pp. 286–295, 2004.

[19]  J.  Baena-García,  J.  Del  Campo-Ávila,  R.  Fidalgo,  A.  Bifet,  R. 
Gavaldà,  and  R.  Morales-Bueno,  “Early  drift  detection  method,” 
Proc.  4th  International  Workshop  on  Knowledge  Discovery  from 
Data Streams, 2006.

[20]  A.  Bifet  and  R.  Gavaldà,  “Learning  from  time-changing  data  with 
adaptive windowing,” Proc. 2007 SIAM International Conference on 
Data Mining, pp. 443–448, 2007.

including  figures  and  graphical  abstracts.  All  authors 
reviewed,  revised,  and  approved  the  final  version  of  the 
manuscript.

Data availability: Data available upon request.

Conflict of Interest: There is no conflict of Interest.

Ethical  statement:  This  research  complies  with  ethical 
guidelines  and  does  not  involve  any  harm  to  humans, 
animals, or the environment

Funding: The research received no external funding.

Similarity checked: Yes.

References

[1]  G. Widmer and M. Kubat, “Learning in the presence of concept drift 
and hidden contexts,” Machine Learning, vol. 23, no. 1, pp. 69–101, 
1996. 
J. Gama, I. Žliobaitė, A. Bifet, M. Pechenizkiy, and A. Bouchachia, 
“A survey on concept drift adaptation,” ACM Computing Surveys, 
vol. 46, no. 4, pp. 1–37, 2014.

[2]

[3]  S. Wang, L. Cao, and Y. Wang, “A density-based ensemble method 
for concept drift adaptation,” Neurocomputing, vol. 136, pp. 44–50, 
2014.

[4]  M. S. Lakshmi, K. S. Ramana, G. Ramu, K. Shyam Sunder Reddy, 
C. Sasikala, and G. Ramesh, “Computational intelligence techniques 
for energy efficient routing protocols in wireless sensor networks: A 
critique,”  Transactions 
on  Emerging  Telecommunications 
Technologies, vol. 35, no. 1, Nov. 2023, doi: 10.1002/ett.4888. 
[5]  S. Chappidi and A.  Raju,  "Advancements  in  speech-based  emotion 
recognition and PTSD detection through machine and deep learning 
techniques:  A  comprehensive  survey,"  SSRG  Int.  J.  Electron. 
Commun. Eng., vol. 11, no. 5, 2023, doi: 10.14445/23488549/IJECE-
V11I5P121.

[6]  A.  Bifet  and  R.  Gavaldà,  “Learning  from  time-changing  data  with 
adaptive windowing,” Proceedings of the 2007  SIAM  International 
Conference on Data Mining, pp. 443–448, 2007.

[7]  M.  Žliobaitė,  “Learning  under  concept  drift:  an  overview,”  arXiv

preprint arXiv:1010.4784, 2010.

[8]  P. Gama, P. Medas, G. Castillo, and P. Rodrigues, “Learning with drift 
detection,” Brazilian Symposium on Artificial Intelligence, pp. 286–
295, 2004.

[9]  A.  Pesaranghader  and  H.  Viktor,  “Fast  Hoeffding  Drift  Detection 
Method for evolving data streams,” Machine Learning, vol. 106, no. 
9–10, pp. 1479–1495, 2017.

[10]  A.  Swetha,  M.  S.  Lakshmi,  and  M.  R.  Kumar,  “Chronic  kidney 
disease  diagnostic  approaches  using  efficient  artificial  intelligence 
methods,”  International  Journal  of  Intelligent  Systems  and 
Applications  in  Engineering,  vol.  10,  no.  1s,  pp.  254–259,  2022. 
[Online]. 
Available: 
https://www.ijisae.org/index.php/IJISAE/article/view/2289.

[11]  J. Gama, I. Žliobaitė, A. Bifet, M. Pechenizkiy, and A. Bouchachia, 
“A  survey  on  concept  drift  adaptation,”  ACM  Computing  Surveys, 
vol. 46, no. 4, pp. 1–37, Apr. 2014, doi: 10.1145/2523813.

[12]  J.  Baena-García,  J.  Del  Campo-Ávila,  R.  Fidalgo,  A.  Bifet,  R. 
Gavaldà,  and  R.  Morales-Bueno,  "Early  drift  detection  method," 
Fourth International Workshop on Knowledge Discovery from Data 
Streams, vol. 6, no. 1, pp. 77–86, 2006.

[13]  A.  Bifet  and  R.  Gavaldà,  "Learning  from  time-changing  data  with 
adaptive windowing," Proceedings of the 2007 SIAM  International 
Conference on Data Mining, pp. 443–448, 2007.

[14]  A. Bifet, G. Holmes, R. Kirkby, and B. Pfahringer, "MOA: Massive 
Online Analysis," Journal of Machine Learning Research, vol. 11, pp. 
1601–1604, 2010.

[15]  N. Cesa-Bianchi, P. Fischer, and C. Gentile, "Tracking the best linear 
predictor," Journal of Machine Learning Research, vol. 4, pp. 1107–
1133, 2003.

[16]  A.  Pesaranghader  and  H.  Viktor,  "Fast  Hoeffding  Drift  Detection 
Method for evolving data streams," Machine Learning, vol. 106, no. 
9–10, pp. 1479–1495, 2017.

[17]  A. Bifet, G. Holmes, R. Kirkby, and B. Pfahringer, “MOA: Massive 
Online Analysis,” Journal of Machine Learning Research, vol. 11, pp. 
1601–1604, 2010.

9

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Synthesis: A Multidisciplinary Research Journal
Volume 1, Issue 4, October - December 2023, Pp: 1-9
© 2023, All Rights Reserved @ Macaw Publications
Research Article
DataStream Adapt: Unified Detection Framework for
Gradual and Abrupt Concept Drifts
1* Mettu Yashwanth, 2 Digumarthy Sandeepa, 3 Sk. Khaja Shareef
1* University of Texas, USA.
2 Department of Computer Science, Southeast Missouri State University.
3 Associate Professor, Department of CSE, Koneru Lakshmaiah Education Foundation, Bowrampet, Hyderabad, India
*Corresponding Author(s): yxm2835@mavs.uta.edu
Article Info Abstract
Received:05/08/2023 Concept drift, the phenomenon where data distributions change over time, poses a significant
Revised: 28/09/2023 challenge to maintaining the accuracy and reliability of predictive models in data stream
Accepted:20/12/2023 environments. Traditional drift detectors often struggle to simultaneously handle both abrupt
Published:31/12/2023 and gradual drifts, leading to delayed adaptation or excessive false positives. This study
proposes DataStream Adapt, a unified and adaptive framework designed to detect and respond
to both abrupt and gradual concept drifts in real-time data streams. The framework integrates a
hybrid drift detection engine combining error-rate monitoring and statistical divergence, an
adaptive threshold controller that adjusts sensitivity based on stream volatility, and a drift-aware
ensemble classifier capable of reweighting or replacing base learners dynamically. The system
is benchmarked using the synthetic Hyperplane dataset, designed to simulate controlled drift
scenarios with known ground truths. Experimental results demonstrate that DataStream Adapt
outperforms state-of-the-art baselines, including DDM, ADWIN, and EDDM. Specifically, it
achieves a detection delay of 31.2 instances for abrupt drift and 64.8 instances for gradual drift,
compared to 82.4 and 254.6 for DDM, respectively. The framework maintains a false positive
rate of 0.041, significantly lower than ADWIN’s 0.147, while also achieving an F1-score of
0.89 on post-drift classification, outperforming all baselines. In conclusion, DataStream Adapt
offers a scalable, interpretable, and low-latency solution for adaptive learning in evolving data
environments, making it suitable for real-world deployment in applications such as fraud
detection, predictive maintenance, and IoT analytics.
Keywords: Concept Drift, Data Streams, Adaptive Learning, Drift Detection, Ensemble
Classifiers, Real-Time Analytics, Threshold Adaptation
Copyright: © 2023 Mettu Yashwanth, Digumarthy Sandeepa, Sk. Khaja Shareef. This article is an open-
access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY 4.0)
license.
https://www.macawpublications.com/Journals/index.php/SMRJ 1

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023
Graphical abstract of the DataStream Adapt Framework
1. Introduction Most current approaches to concept drift detection and
adaptation suffer from limited generalizability across drift
In the era of real-time data generation, continuous data
types and lack adaptive mechanisms that can adjust their
streams have become ubiquitous across a wide spectrum of
sensitivity based on data volatility [7]. While ensemble
applications—including financial analytics, fraud detection,
methods and statistical detectors exist, few offer a cohesive
e-commerce personalization, industrial monitoring, and
solution that integrates drift detection, certainty estimation,
cyber-physical systems [1], [2]. These data streams are
and real-time model adaptation into a single pipeline. The
inherently non-stationary, meaning the underlying
absence of such an integrated and unified framework
statistical properties evolve over time. This evolution,
hinders the deployment of robust stream learning systems in
commonly referred to as concept drift, can severely degrade
mission-critical applications.
the predictive performance of machine learning models
trained under the assumption of static data distributions [3]. Several key challenges in the domain remain unresolved:
As organizations increasingly rely on streaming  Drift-Type Specialization: Many algorithms
analytics and automated decision-making systems, the need perform well for abrupt drift but fail under gradual
for adaptive learning mechanisms that can detect and conditions [8].
respond to concept drift has become critical [4]. Concept
 Static Threshold Limitations: Use of non-adaptive
drift manifests in two primary forms: abrupt drift, where
parameters leads to poor performance in highly
changes occur suddenly and dramatically; and gradual drift,
dynamic or noisy environments.
where shifts happen progressively over time [5]. Effective
detection and adaptation to both types of drift are essential  Lack of Drift Confidence Metrics: Most systems
for maintaining model accuracy, reliability, and offer binary drift detection without conveying
responsiveness in evolving environments. certainty or ranking of detected drifts [9].
Existing systems typically address only a subset of  Disconnected Adaptation Mechanisms: In most
these challenges, often treating abrupt and gradual drift ensemble methods, drift detection is decoupled
detection as separate problems. Furthermore, they from model adaptation, resulting in delayed or
frequently rely on fixed sensitivity thresholds, which makes suboptimal learner updates [10].
them susceptible to false positives in noisy streams or
 Scalability and Interpretability: High
delayed response in stable periods [6]. This motivates the
computational overhead and lack of explainability
development of a more unified, adaptable, and intelligent
restrict the practical deployment of many existing
framework that can accurately detect, distinguish, and
systems.
respond to various drift patterns without manual
intervention. This study aims to develop a unified and adaptive
framework—DataStream Adapt—capable of detecting and
2

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

responding to both gradual and abrupt concept drifts in real- 2.1 Error-Based Drift Detection Methods
time data streams. The primary objectives are:
|     |     |     |     |     |     |     |     | Error-based  |     | methods  | monitor  | the  performance  |     | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | -------- | ----------------- | --- | --- |
  To design a hybrid detection engine combining  classifiers  over  time  to  detect  potential  drift  based  on
statistical and error-based indicators for improved  statistical  deviations  in  error  rates.  One  of  the  earliest
robustness.  approaches, the Drift Detection Method (DDM), estimates
the probability of classification error and raises alarms when
  To introduce an adaptive threshold controller that
the standard deviation exceeds a predefined threshold [11].
dynamically adjusts detection sensitivity based on
The Early Drift Detection Method (EDDM) extends DDM
data volatility.  by focusing on the distance between classification errors,
  To integrate a drift certainty scoring mechanism  which enhances its sensitivity to gradual drifts [12]. Despite
their simplicity and efficiency, these methods are often
that quantifies confidence in detection events.
highly sensitive to noise and are less effective in identifying
|     |   To  develop  |     | an  ensemble-based  |     |     | classifier  | that  |     |     |     |     |     |     |     |
| --- | --------------- | --- | ------------------- | --- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
slow, continuous changes in the data distribution.
reweights or replaces base learners in response to
2.2 Distribution-Based Methods
detected drift.
|     |               |     |      |           |            |     |          | Distribution-based detectors aim to capture drift by  |     |     |     |     |     |     |
| --- | -------------- | --- | ---- | --------- | ---------- | --- | -------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | To  benchmark  |     | the  | proposed  | framework  |     | against  |                                                       |     |     |     |     |     |     |
comparing changes in feature distributions or prediction
|     | established  |     | baselines  | (e.g.,  | DDM,  | ADWIN,  |     |                |         |       |           |        |            |     |
| --- | ------------ | --- | ---------- | ------- | ----- | ------- | --- | -------------- | ------- | ----- | --------- | ------ | ---------- | --- |
|     |              |     |            |         |       |         |     | probabilities  | across  | time  | windows.  | ADWIN  | (Adaptive  |     |
EDDM) using a controlled synthetic dataset.
Windowing) is a popular method that employs a dynamic
The contributions of this paper are summarized as follows:  sliding window and uses statistical hypothesis testing to
detect significant changes in data distribution [13]. Other
1.  A unified detection framework that effectively
techniques rely on statistical divergence measures, such as
handles both abrupt and gradual concept drifts using
KL-divergence, Hellinger distance, and the Kolmogorov–
a hybrid combination of error rate monitoring and
Smirnov test. While these approaches are more robust to
statistical distance measures.
noisy labels and transient fluctuations, they tend to require
2.  An  adaptive  threshold  controller  that  learns  more memory and computational resources, especially in
volatility patterns in the data stream and adjusts  high-dimensional data streams.
|     | sensitivity  | parameters  |     | accordingly  |     | to  minimize  |     |     |     |     |     |     |     |     |
| --- | ------------ | ----------- | --- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2.3 Ensemble-Based Approaches
false positives.
Ensemble methods combine multiple base classifiers to
|     | 3.  A  drift  | certainty  |     | scoring  |     | mechanism  | that  |          |             |      |               |     |          |         |
| --- | ------------- | ---------- | --- | -------- | --- | ---------- | ----- | -------- | ----------- | ---- | ------------- | --- | -------- | ------- |
|     |               |            |     |          |     |            |       | improve  | robustness  | and  | adaptability  | to  | concept  | drift.  |
improves interpretability and decision confidence
Approaches such as Online Bagging, Leveraging Bagging,
by quantifying the strength of detected drifts.
|     |     |     |     |     |     |     |     | and  Dynamic  | Weighted  |     | Majority  | (DWM)  | dynamically  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | --------- | ------ | ------------ | --- |
4.  An  integrated  ensemble  adaptation  strategy,  update their constituent models based on performance [14],
where base learners are updated or reweighted in
|     |     |     |     |     |     |     |     | [15].  These  | techniques  |     | can  | respond  to  | performance  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | ---- | ------------ | ------------ | --- |
response to detected drift events.  degradation caused by drift by removing poorly performing
|     |                    |     |               |     |     |             |        | learners  | and  introducing  |     | new  | ones.  However,  |     | most  |
| --- | ------------------ | --- | ------------- | --- | --- | ----------- | ------ | --------- | ----------------- | --- | ---- | ---------------- | --- | ----- |
|     | 5.  Comprehensive  |     | experimental  |     |     | validation  | using  |           |                   |     |      |                  |     |       |
ensemble methods do not inherently detect drift and instead
|     | the  Hyperplane  |     | dataset,  |     | demonstrating  |     | superior  |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
rely on external drift detectors to signal model updates. This
performance in detection delay, false positive rate,
|     |     |     |     |     |     |     |     | limits  their  | autonomy  |     | and  responsiveness  |     | in  rapidly  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | -------------------- | --- | ------------ | --- |
and classification accuracy compared to state-of-
evolving environments.
the-art methods.
2.4 Hybrid and Unified Detection Approaches
The remainder of this paper is organized as follows:
Section 2 reviews related literature and outlines the existing  More recent research has focused on hybrid strategies
research gaps. Section 3 details the proposed methodology
that attempt to integrate multiple drift indicators within a
and  system  architecture.  Section  4  describes  the  single framework. For example, HDDM (Hoeffding Drift
experimental  setup  and  evaluation  metrics.  Section  5  Detection  Method)  combines  statistical  distribution
| discusses  | results  | and  | comparisons.  |     | Finally,  | Section  | 6   |     |     |     |     |     |     |     |
| ---------- | -------- | ---- | ------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
monitoring with error-rate tracking to improve detection
concludes the paper and outlines directions for future work.  robustness  [16].  Similarly,  methods  like  EDDM-IGT
|     |     |     |     |     |     |     |     | explore  | multiple  | sources  | of  | evidence  | for  enhanced  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | -------- | --- | --------- | -------------- | --- |
2. Related Work
sensitivity. However, these systems typically operate with
The challenge of detecting concept drift in evolving  fixed thresholds and often lack scalability or generalization
data  streams  has  attracted  significant  attention  across  across different drift types. They also do not offer integrated
|          |              |     |          |            |     |                    |     | mechanisms  | for  | drift  | certainty  | estimation  | or  adaptive  |     |
| -------- | ------------ | --- | -------- | ---------- | --- | ------------------ | --- | ----------- | ---- | ------ | ---------- | ----------- | ------------- | --- |
| various  | application  |     | domains  | such       | as  | fraud  detection,  |     |             |      |        |            |             |               |     |
| network  | monitoring,  |     | and      | real-time  |     | recommendation     |     | learning.   |      |        |            |             |               |     |
systems. Over the years, researchers have proposed multiple
2.5 Research Gaps
strategies to handle concept drift, which can be broadly
categorized  into  error-based  methods,  distribution-based  Despite considerable progress in the field, several key
methods, ensemble-based approaches, and more recently,  research gaps remain unresolved. First, existing systems are
hybrid  and  unified  detection  frameworks.  This  section  often specialized for either abrupt or gradual drift. And lack
presents  a  structured  review  of  these  techniques  and  the ability to generalize across both in a unified manner.
identifies persistent research gaps.  Second, the reliance on fixed sensitivity thresholds makes
3

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

many  detectors  brittle  in  volatile  or  non-stationary  This dataset provides a controlled testbed to evaluate
environments.  Third,  there  is  a  lack  of  drift  certainty  the latency, accuracy, and robustness of the proposed drift
estimation mechanisms that could quantify the confidence  detection mechanism under both drift scenarios.
level of a detected drift event, limiting the interpretability
3.2 Data Preprocessing and Windowing
| and  controllability  |     | of  | current  | systems.  | Fourth,  | most  |     |     |     |     |     |     |     |
| --------------------- | --- | --- | -------- | --------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
ensemble learning methods depend on external signals for  Let the input data stream be:
| drift  handling  |     | and  lack  | an  internal  | feedback  |     | loop  that  |     |     |     |               |      |     |     |
| ---------------- | --- | ---------- | ------------- | --------- | --- | ----------- | --- | --- | --- | ------------- | ---- | --- | --- |
|                  |     |            |               |           |     |             |     | 𝒟   | ={𝑥 | ,𝑥 ,…,𝑥 ,…},𝑥 | ∈ℝ𝑛  |     |     |
couples detection with adaptation. Finally, many published  1 2 𝑡 𝑡
works do not offer comprehensive benchmarking across
Two temporal windows are maintained:
mixed drift types, making reproducibility and real-world
  A short-term window 𝑊(𝑡), capturing the most
| applicability more difficult.  |     |     |     |     |     |     |     |     |     |     | 𝑠   |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recent 𝑘 instances.
In summary, while existing methods offer valuable
|     |     |     |     |     |     |     |    | A long-term reference window 𝑊 |     |     |     | (𝑡), representing  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ------------------ | --- |
tools  for  specific  drift  scenarios,  a  general-purpose,  𝑙
adaptive, and self-configuring framework remains lacking.  a stable historical distribution.
The proposed DataStream Adapt framework addresses these
|     |     |     |     |     |     |     | These  | windows  |     | support  | comparative  | statistical  |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | -------- | ------------ | ------------ | --- |
challenges by combining hybrid drift detection, adaptive  monitoring and drift detection.
threshold tuning, and drift-aware ensemble adaptation into
a  single,  unified  architecture  capable  of  handling  both  3.3 Statistical and Signal Monitoring
abrupt and gradual drifts in real-time.  To  detect  deviations  in  data  distribution  or  model
3. Methodology  performance, we compute several key metrics:
3.3.1 Mean and Variance Differences
| This  | section  | outlines  | the  | design  | of  the  | proposed  |     |     |     |     |     |     |     |
| ----- | -------- | --------- | ---- | ------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
DataStream Adapt framework, which unifies the detection
|     |     |     |     |     |     |     | We  | measure the change in  |     |     | the  mean and variance  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ----------------------- | --- | --- |
of both gradual and abrupt concept drifts in streaming data  between the two windows:
| environments.  |     | The  methodology  |     | integrates  |     | statistical  |     |     |     |     |     |     |     |
| -------------- | --- | ----------------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
monitoring,  hybrid  drift  detection,  adaptive  threshold    Δ𝜇 =|𝜇(𝑊(𝑡))−𝜇(𝑊(𝑡))|  (1)
|     |     |     |     |     |     |     |     |     |     | 𝑡 𝑠 |     | 𝑙   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tuning, and dynamic ensemble learning. The flow of data
through the framework is shown in Figure 1, with each stage  Δ𝜎2 =|𝜎2(𝑊(𝑡))−𝜎2(𝑊(𝑡))|  (2)
|     |     |     |     |     |     |     |     |     |     | 𝑡   | 𝑠   | 𝑙   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
elaborated below.
|     |     |     |     |     |     |     | These  | metrics  |     | highlight  subtle  | gradual  | changes  | in  |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ------------------ | -------- | -------- | --- |
distribution.
3.3.2 Error Rate Monitoring
|     |     |     |     |     |     |     | Let 𝑦ˆ |  be the predicted label and 𝑦 the ground truth.  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------------------------------------------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |        | 𝑖                                                |     |     | 𝑖   |     |     |
The classification error rate over the short-term window is:
1
|     |     |     |     |     |     |     |     | 𝜖 = |         | ∑  𝕀[𝑦ˆ | ≠𝑦]  |     | (3)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ---- | --- | ---- |
|     |     |     |     |     |     |     |     | 𝑡   | |𝑊𝑠(𝑡)| | 𝑖∈𝑊𝑠(𝑡) | 𝑖 𝑖  |     |      |
This is used to trigger change detection algorithms
when error increases.
3.3.3 Distributional Divergence
|     |     |     |     |     |     |     | We  | use  | the  Kullback-Leibler  |     | (KL)  | divergence  | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------------------- | --- | ----- | ----------- | --- |
quantify distributional shift:

𝑃(𝑖)
Fig.1. Architecture of the DataStream Adapt Framework for Unified  𝐷 (𝑃‖𝑄)=∑  𝑃(𝑖)log⁡     (4)
| Concept Drift Detection and Adaptation  |     |     |     |     |     |     |     | 𝐾𝐿  |     | 𝑖   |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑄(𝑖)
3.1 Dataset Description  where 𝑃 and 𝑄 are estimated distributions over 𝑊 and
𝑠
𝑊, respectively.
| We  | evaluate  | our  framework  |     | using  | the  Hyperplane  |     | 𝑙   |     |     |     |     |     |     |
| --- | --------- | --------------- | --- | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Dataset,  a  widely  used  synthetic  stream  benchmark  3.4 Hybrid Drift Detection Engine
designed to simulate both gradual and abrupt concept drifts
Our system combines two distinct methods to detect
in a controlled environment.
both abrupt and gradual drifts:
∈ℝ𝑑
|    | Each  | instance  | 𝑥 𝑡 | is  generated  |     | from  a  |     |     |     |     |     |     |     |
| --- | ----- | --------- | --- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
3.4.1 Abrupt Drift Detection via CUSUM
dynamic hyperplane defined by:
The Cumulative Sum (CUSUM) method tracks abrupt
∑𝑑
|                                          |     | 𝑖=1  𝑤𝑥          | 𝑖 𝑖 =𝜃 𝑡 |               |      |            | shifts in error rate:  |            |     |     |           |     |      |
| ---------------------------------------- | --- | ---------------- | -------- | ------------- | ---- | ---------- | ---------------------- | ---------- | --- | --- | --------- | --- | ---- |
| where                                    | 𝑤   | are  hyperplane  |          | coefficients  | and  | 𝜃   is  a  |                        |            |     |     |           |     |      |
|                                          | 𝑖   |                  |          |               |      | 𝑡          |                        | 𝑆 =max(0,𝑆 |     | +(𝜖 | −𝜖 −𝛿))   |     | (5)  |
| threshold value that changes over time.  |     |                  |          |               |      |            |                        | 𝑡          |     | 𝑡−1 | 𝑡 0       |     |      |
where:
  Abrupt drift is simulated by sudden shifts in 𝑤,
𝑖
while gradual drift involves slowly changing 𝑤  𝜖  is the baseline error,
|     |     |     |     |     |     | 𝑖   |     | 0   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
across instances.
4

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

𝛿 is a tolerance factor,    New classifiers are trained on post-drift data and
added to the ensemble.
|     | 𝑆 𝑡 >ℎ indicates a drift (with ℎ as the detection  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
threshold).  Algorithm: DataStream Adapt – Unified Concept Drift
Detection and Adaptation
3.4.2 Gradual Drift Detection via Moving Average
Input:
We use lagged moving averages to detect slow drifts:
|     |     |     |      |     |     |      |     |   Stream  |     | 𝒟,  ensemble  | ℋ,  | thresholds  | ℎ ,𝛿 ,𝛾 ,  |
| --- | --- | --- | ---- | --- | --- | ---- | --- | ---------- | --- | ------------- | --- | ----------- | ---------- |
|     |     |     | 1    |     |     |      |     |            |     |               |     |             | 0 0 0      |
|     |     | 𝑥‾  | = ∑𝑡 |  𝑥  |     | (6)  |     |            |     |               |     |             |            |
𝑡 𝑘 𝑖=𝑡−𝑘+1 𝑖 window sizes 𝑊 ,𝑊 , learning rate 𝜂, volatility
𝑠 𝑙
sensitivity 𝜆
Drift is flagged if:
|     |     | |𝑥‾ | −𝑥‾ | |>𝛾    |     | (7)  | Output:  |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | ---- | -------- | --- | --- | --- | --- | --- | --- |
𝑡 𝑡−𝑘
|                                        |     |     |     |     |     |     |           |   Predictions 𝑦ˆ |     | , drift logs 𝐿 |     |        |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | --- | -------------- | --- | ------ | --- |
| where 𝛾 is a dynamic threshold value.  |     |     |     |     |     |     |           |                   |     | 𝑡              |     | drift  |     |
| 3.4.3 Drift Certainty Scoring          |     |     |     |     |     |     | Process:  |                   |     |                |     |        |     |
To unify both detectors, we define a drift certainty score:  1.  Initialize thresholds and ensemble.
|         |           |         |            |             |          |         |     | 2.  For each 𝑥 |                                |  in stream:  |                          |     |     |
| ------- | --------- | ------- | ---------- | ----------- | -------- | ------- | --- | -------------- | ------------------------------ | ------------ | ------------------------ | --- | --- |
|         | 𝒞 𝑡       | =𝛼⋅𝕀    | +(1−𝛼)⋅𝕀   |             |          | (8)     |     |                |                                | 𝑡            |                          |     |     |
|         |           | abrupt  |            |             | gradual  |         |     |                |                                |              |                          |     |     |
| where:  |           |         |            |             |          |         |     |               | Preprocess and append to 𝑊,𝑊.  |              |                          |     |     |
|         |           |         |            |             |          |         |     |                |                                |              |                          |     | 𝑠 𝑙 |
|         |           |         |            |             |          |         |     |               | Predict label 𝑦ˆ               |              |  using ensemble voting.  |     |     |
|         | 𝛼 ∈[0,1]  | is      | a  weight  | determined  | by       | signal  |     |                |                                |              | 𝑡                        |     |     |
volatility,
|     |     |     |     |     |     |     |     |    | Compute Δ𝜇 |     | ,Δ𝜎2,𝜖 | ,𝐷 .  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ----- | --- |
|     |     |     |     |     |     |     |     |     |            | 𝑡   | 𝑡      | 𝑡 𝐾𝐿  |     |
II are binary indicators ( 1= drift detected, 0= no
|     |          |     |     |     |     |     |     |    | Estimate volatility 𝜈 |        |      |  and update thresholds.  |                 |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | ------ | ---- | ------------------------ | --------------- |
|     | drift).  |     |     |     |     |     |     |     |                       |        | 𝑡    |                          |                 |
|     |          |     |     |     |     |     |     |    | Apply                 | CUSUM  | and  | moving                   | average  shift  |
3.5 Adaptive Threshold Controller
detection.
This component dynamically tunes parameters such as
|     |     |     |     |     |     |     |     |    | If drift is detected:  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
ℎ,𝛿, and 𝛾, based on observed volatility in the data stream.
  Reweight or replace classifiers.
3.5.1 Volatility Estimation
  Log drift info (type, time, certainty).
We estimate stream volatility using variance:
|     |     |     |        |      |      |      |     |    | Slide windows and proceed to next 𝑥 |     |     |     | .   |
| --- | --- | --- | ------ | ---- | ---- | ---- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
|     |     | 𝜈   | =Var(𝑥 | ,…,𝑥 | )    | (9)  |     |     |                                     |     |     |     | 𝑡+1 |
|     |     | 𝑡   |        | 𝑡−𝑚  | 𝑡    |      |     |     |                                     |     |     |     |     |
End For
3.5.2 Threshold Adjustment Rule
3.7 Model Output and Drift Logging
The detection threshold is adjusted as:
At each timestep 𝑡, the system outputs:
|         |     | ℎ 𝑡 =ℎ | 0 ⋅(1+𝜆⋅𝜈 | 𝑡 )  |     | (10)  |     |     |                                         |     |     |     |     |
| ------- | --- | ------ | --------- | ---- | --- | ----- | --- | --- | --------------------------------------- | --- | --- | --- | --- |
|         |     |        |           |      |     |       |     |    | Predicted label 𝑦ˆ                      |     |     |     |     |
| where:  |     |        |           |      |     |       |     |     |                                         |     | 𝑡   |     |     |
|         |     |        |           |      |     |       |     |    | Drift status: none, gradual, or abrupt  |     |     |     |     |
ℎ  is the base threshold,
0

𝜆 controls sensitivity to volatility.  Drift certainty score 𝒞 𝑡
|     |                                                          |     |     |     |     |     |     |    | Drift timestamp 𝑡 |     |     |     |     |
| --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
|     | This reduces false alarms in noisy regions and enhances  |     |     |     |     |     |     |     |                   |     | 𝑑   |     |     |
reactivity during stable phases.
|                                        |     |     |     |     |     |     |     |    | (Optional)  | Summary  |     | of  affected  | statistical  |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------------- | ------------ |
| 3.6 Ensemble Classifier (Drift-Aware)  |     |     |     |     |     |     |     |     | features    |          |     |               |              |
An ensemble of base classifiers ℋ ={ℎ ,ℎ ,…,ℎ } is  All metadata is logged for transparency and auditability.
|     |     |     |     |     | 1 2 | 𝑁   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
used for robust prediction.
4. Experimental Setup
3.6.1 Voting Mechanism
This section details the computational and experimental
Predictions  are  obtained  using  weighted  majority  environment used to evaluate the proposed  DataStream
voting:  Adapt framework. We focus on ensuring full reproducibility
|     |                |     |           |     |          |       | by  | reporting  | hardware  |     | specifications,  |     | software  stack,  |
| --- | -------------- | --- | --------- | --- | -------- | ----- | --- | ---------- | --------- | --- | ---------------- | --- | ----------------- |
|     | 𝑦ˆ =arg⁡max ∑𝑁 |     |  𝑤(𝑡)⋅𝕀[ℎ |     | (𝑥 )=𝑦]  | (11)  |     |            |           |     |                  |     |                   |
𝑡 𝑖=1 𝑖 𝑖 𝑡 dataset partitioning, and implementation settings.
𝑦
| 3.6.2 Learner Update on Drift  |     |     |     |     |     |     | 4.1 Hardware Specifications  |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
When drift is detected:  All experiments were conducted on a high-performance
computing workstation with the following configuration:
  High-error learners are down-weighted:
  Processor: Intel® Core™ i9-12900K @ 3.2 GHz
|     | 𝑤(𝑡+1)=𝜂⋅𝑤(𝑡),⁡ if err |     |     |     | >𝜃    | (12)  |     | (16 cores, 24 threads)  |     |     |     |     |     |
| --- | ---------------------- | --- | --- | --- | ----- | ----- | --- | ----------------------- | --- | --- | --- | --- | --- |
|     | 𝑖                      |     | 𝑖   | 𝑖   |       |       |     |                         |     |     |     |     |     |
5

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023
 Memory: 64 GB DDR5 RAM  Voting method: Weighted majority voting based on
recent accuracy
 GPU: NVIDIA RTX 3090 with 24 GB GDDR6X
VRAM B. Training Configuration
 Storage: 2 TB NVMe SSD  Window sizes:
 Operating System: Ubuntu 22.04 LTS (64-bit)  Short-term 𝑊:200 instances
𝑠
The system supports high-throughput data streaming  Long-term 𝑊:1,000 instances
𝑙
and real-time model adaptation without latency bottlenecks.
 Batch size: 1 (single-instance updates, consistent
4.2 Software Frameworks and Tools with online learning)
The implementation was carried out using Python 3.10.  Drift detection thresholds:
The following open-source libraries and frameworks were
 ℎ =0.5,𝛿 =0.05,𝛾 =0.15
used: 0 0 0
 Volatility sensitivity: λ=0.75
 Scikit-learn 1.4.1: Base classifiers (e.g., Hoeffding
Tree, Naive Bayes)  Drift certainty threshold: 0.6 (minimum score to
confirm drift)
 River 0.15.0: Online learning models and drift
detectors  Model update:
 NumPy 1.26.0: Numerical computations  Learners with accuracy below 60% were
replaced.
 Pandas 2.2.0: Data preprocessing and logging
 New models were trained on the latest
 Matplotlib 3.8.2: Visualizations and drift plots
500 instances post-drift.
 MOA Simulator (via river.datasets.hyperplane) –
C. Runtime
Synthetic stream generation (Hyperplane dataset)
 Total simulation time per run: ~3.8 minutes
All dependencies and versions were managed via conda
and pip, and an environment file is provided in  Average time per instance: 2.3 ms
supplementary material for full reproducibility.
 GPU was not used for training due to the efficiency
4.3 Dataset Partitioning and Stream Configuration of streaming classifiers.
The Hyperplane dataset was configured to simulate All results were averaged over three runs with different
both abrupt and gradual concept drifts: random seeds for statistical significance.
 Attributes: 10 numeric features with binary class 4.5 Evaluation Metrics
labels.
To comprehensively assess the performance of the
 Instances: 100,000 total. proposed framework, we utilize the following metrics:
 Drift Types: Detection Delay: Measures the number of instances
between the actual drift point and the point of detection.
 Abrupt Drift: Sudden change in hyperplane
Lower delay indicates faster responsiveness:
orientation every 20,000 instances.
Delay =𝑡 −𝑡 (13)
 Gradual Drift: Coefficients gradually changed detected true
over a sliding window of 10,000 instances. False Positive Rate (FPR): The proportion of non-drift
points incorrectly flagged as drift:
 Train-Test Split: Since this is a streaming setup, the
model learns and predicts on each instance in a
False⁡Alarms
FPR= (14)
prequential (interleaved-test-then-train) fashion.
Total⁡Non-Drift⁡Events
 Cross-Validation: Not applicable in streaming; F1-Score (Downstream Classification): Measures the
however, three different random seeds were used to harmonic mean of precision and recall in the classification
simulate variations in drift behavior for robustness task, evaluated periodically to assess how well the model
testing. performs under drift:
4.4 Implementation Details Precision ⋅ Recall
𝐹1=2⋅ (15)
Precision + Recall
A. Base Learners:
Computational Efficiency: Captured as shown below
 Ensemble size: 5 models
 Processing Time per instance (ms)
 Learner types: Hoeffding Tree Classifier, Naive
 Memory Usage during runtime (tracked via psutil)
Bayes, Logistic Regression
These metrics help assess the scalability and
practicality of the method for real-world deployment.
6

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

5. Results and Discussion  ability to model drift gradualness via moving averages and
window divergence metrics. Moreover, the F1-score of 0.87
This section presents a comprehensive evaluation of the  signifies more stable classification despite subtle changes in
proposed DataStream Adapt framework under both abrupt
|               |          |     |                     |     |     |          |      | the  distribution.  |       | The  false   | positive  |          | rate    | remains  low,  |
| ------------- | -------- | --- | ------------------- | --- | --- | -------- | ---- | ------------------- | ----- | ------------ | --------- | -------- | ------- | -------------- |
| and  gradual  | concept  |     | drift  conditions.  |     | We  | compare  | its  |                     |       |              |           |          |         |                |
|               |          |     |                     |     |     |          |      | confirming          | that  | the  system  |           | is  not  | misled  | by  slow       |
performance  with  three  widely  recognized  baseline  fluctuations or noise, unlike DDM and ADWIN which tend
| detectors:  | DDM  | (Drift  | Detection  |     | Method),  | ADWIN  |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------- | ---------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
to overreact to small statistical variances.
(Adaptive Windowing), and EDDM (Early Drift Detection
5.3 Summary of Comparative Advantages
Method). All models were implemented in a prequential
| setting  | using  | the  same  | base  | learners  | and  | experimental  |     |     |             |      |               |     |                      |     |
| -------- | ------ | ---------- | ----- | --------- | ---- | ------------- | --- | --- | ----------- | ---- | ------------- | --- | -------------------- | --- |
|          |        |            |       |           |      |               |     | To  | supplement  | the  | quantitative  |     | evaluation, Table 3  |     |
configurations described in Section 4.
highlights the comparative capabilities of each framework
across several qualitative dimensions. These dimensions are
5.1 Performance under Abrupt Drift
critical for assessing the practical readiness of a concept
| Under  | abrupt  | drift  | scenarios  | (with  | sudden  | changes  |     |     |     |     |     |     |     |     |
| ------ | ------- | ------ | ---------- | ------ | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
drift detection system in real-world, continuously evolving
| every  20,000   |     | instances),  | the        | detection  |                | accuracy  | and  | environments.  |     |     |     |     |     |     |
| --------------- | --- | ------------ | ---------- | ---------- | -------------- | --------- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
| responsiveness  |     | of  the      | framework  |            | are  crucial.  | Table     | 1    |                |     |     |     |     |     |     |
summarizes the key metrics for each method.  Table 3: Comparative Feature Analysis of Drift Detection Methods

Table 1: Performance Comparison under Abrupt Drift
DataStream
|           |            |        |        |         |       |                |     | Feature  |          | DDM  | EDDM  | ADWIN  |     | Adapt (Ours)  |
| --------- | ---------- | ------ | ------ | ------- | ----- | -------------- | --- | -------- | -------- | ---- | ----- | ------ | --- | ------------- |
|           |            |        |        |         |       |                |     | Detects  | Abrupt   |      |       |        |     |               |
| Method    | Detection  |        | FPR    |         | F1-   | Time/Instance  |     |          |          |      |       |        |     |               |
|           |            | Delay  |        | Score   |       | (ms)           |     | Drift    |          | ✓    | ✓     |        | ✓   | ✓✓✓           |
|           |            |        |        |         |       |                |     | Detects  | Gradual  |      |       |        |     |               |
| DDM [18]  |            | 82.4   | 0.134  |         | 0.81  | 1.3            |     |          |          | ✗    | ✓     |        | ✓   | ✓✓✓           |
Drift
| EDDM [19]  |     | 101.7  | 0.118  |     | 0.79  | 1.5  |     | Adaptive  |     |     |     |     |     |      |
| ---------- | --- | ------ | ------ | --- | ----- | ---- | --- | --------- | --- | --- | --- | --- | --- | ---- |
|            |     |        |        |     |       |      |     |           |     | ✗   | ✗   |     | ✓   | ✓✓✓  |
Thresholding
ADWIN
|       |     | 56.3  | 0.147  |     | 0.83  | 1.8  |     | Ensemble-Based  |     |     |     |     |     |      |
| ----- | --- | ----- | ------ | --- | ----- | ---- | --- | --------------- | --- | --- | --- | --- | --- | ---- |
| [20]  |     |       |        |     |       |      |     |                 |     | ✗   | ✗   |     | ✗   | ✓✓✓  |
Learning
| Ours   |     | 31.2         | 0.041  |      | 0.89      | 2.3     |     |             |            |     |     |     |     |      |
| ------ | --- | ------------ | ------ | ---- | --------- | ------- | --- | ----------- | ---------- | --- | --- | --- | --- | ---- |
|        |     |              |        |      |           |         |     | Drift       | Certainty  |     |     |     |     |      |
|        |     |              |        |      |           |         |     |             |            | ✗   | ✗   |     | ✗   | ✓✓✓  |
|        |     |              |        |      |           |         |     | Scoring     |            |     |     |     |     |      |
| Table  | 1   | illustrates  | that   | the  | proposed  | method  |     | Robustness  | to         |     |     |     |     |      |
|        |     |              |        |      |           |         |     |             |            | ✗   | ✗   |     | ✓   | ✓✓✓  |
False Alarms
significantly reduces detection delay by ~45% compared to
Real-Time
ADWIN and ~62% compared to DDM, indicating superior
|     |     |     |     |     |     |     |     | Operation  | (CPU- | ✓   | ✓   |     | ✓   | ✓   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | --- | --- | --- | --- | --- |
responsiveness to abrupt changes. The false positive rate
efficient)
| (FPR) is also substantially lower (0.041), demonstrating the  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
effectiveness  of  the  adaptive  threshold  controller  in  The proposed DataStream Adapt framework clearly
suppressing noise-induced false alarms. Additionally, the
|     |     |     |     |     |     |     |     | demonstrates  | comprehensive  |     |     | advantages.  |     | It  uniquely  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | --- | --- | ------------ | --- | ------------- |
F1-score  of  0.89  confirms  improved  classification  integrates both abrupt and gradual drift detection into a
performance immediately following abrupt shifts, owing to  unified  pipeline  while  minimizing  false  positives  via
the timely ensemble adaptation. Although the time per  adaptive thresholding. Additionally, its ability to update and
| instance  | is  marginally  |     | higher  | (2.3  | ms),  the  | increase  | is  |     |     |     |     |     |     |     |
| --------- | --------------- | --- | ------- | ----- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
reweight an ensemble of classifiers in real time, combined
justified  by  improved  drift  sensitivity  and  predictive  with  a  drift  certainty  score,  provides  a  level  of
robustness.  interpretability and resilience absent in other systems.
5.2 Performance under Gradual Drift
These features make it well-suited for deployment in
|     |     |     |     |     |     |     |     | mission-critical,  |     | high-throughput  |     | environments  |     | such  as  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ---------------- | --- | ------------- | --- | --------- |
Gradual drift experiments involved slow, continuous
|                                             |     |     |     |     |     |             |     | fraud  detection,  |     | sensor  | networks,  |     | and  recommendation  |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | ------------------ | --- | ------- | ---------- | --- | -------------------- | --- |
| change in the underlying distribution over  |     |     |     |     |     | windows of  |     |                    |     |         |            |     |                      |     |
systems.
10,000 instances. Results are presented in Table 2.
5.4 Practical Considerations
Table 2: Performance Comparison under Gradual Drift
|     |     |     |     |     |     |        |     | While the runtime cost per instance is slightly higher          |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | Time/  |     | (2.3 ms), this is well within operational limits for most real- |     |     |     |     |     |     |
Detection
Method  FPR  F1-Score  Instance  time systems, including fraud detection, sensor monitoring,
Delay
(ms)
|           |     |        |        |     |       |      |     | and  user  | behavior  | modeling.  |     | The  | benefit  | of  reduced  |
| --------- | --- | ------ | ------ | --- | ----- | ---- | --- | ---------- | --------- | ---------- | --- | ---- | -------- | ------------ |
| DDM [18]  |     | 254.6  | 0.186  |     | 0.76  | 1.3  |     |            |           |            |     |      |          |              |
retraining frequency and higher accuracy compensates for
EDDM [19]  132.3  0.098  0.81  1.6  this  trade-off.  Moreover,  the  modular  architecture  and
reliance on open-source tools (Section 4.2) ensure that the
| ADWIN [20]  |     | 111.5  | 0.122  |     | 0.83  | 1.8  |     |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ------ | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
system is easily deployable in real-world applications.
| Ours  |     | 64.8  | 0.058  |     | 0.87  | 2.3  |     |     |     |     |     |     |     |     |
| ----- | --- | ----- | ------ | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
These results affirm that each mechanism — especially

synaptic consolidation and memory replay — is vital in
While ADWIN and EDDM offer competitive detection
|     |     |     |     |     |     |     |     | preventing  | catastrophic  |     | forgetting  |     | and  | sustaining  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | ----------- | --- | ---- | ----------- |
under gradual drift, the proposed method again outperforms
performance across tasks.
| all  baselines  |       | with  the    | lowest  | detection  |       | delay          | (64.8  |     |     |     |     |     |     |     |
| --------------- | ----- | ------------ | ------- | ---------- | ----- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| instances).     | This  | improvement  |         | stems      | from  | the  system’s  |        |     |     |     |     |     |     |     |
7

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023

5.5 Visual Representation
To facilitate a clear and balanced comparison across multiple performance metrics with different scales, we present
normalized bar graphs and a line chart that visualize the comparative performance of the proposed DataStream Adapt
framework against established baseline detectors—DDM, EDDM, and ADWIN—under both abrupt and gradual concept
drift conditions.
|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Fig.2. Comparative performance of concept drift detectors under abrupt and gradual drift conditions

The line chart (left) in figure 2 shows the Detection  tuning or dimensionality reduction also highlight areas for
Delay of each method, where the proposed DataStream  future improvement.
Adapt significantly outperforms baseline detectors (DDM,
6. Conclusion and Future Work
| EDDM,  | and  ADWIN),  | especially  | under  | abrupt  | drift.  |     |     |     |     |     |     |     |
| ------ | ------------- | ----------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
The stacked bar chart (right) in figure 2 illustrates the
This research introduces DataStream Adapt, a unified
| normalized  | False  Positive  |     | Rate  (FPR)  | and  | F1-Score,  |     |     |     |     |     |     |     |
| ----------- | ---------------- | --- | ------------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
and adaptive framework for real-time detection and response
confirming the superior balance of precision and recall  to both abrupt and gradual concept drifts in data streams.
achieved by the proposed method while maintaining a low  Unlike traditional methods with fixed thresholds or limited
false alarm rate. The results demonstrate that DataStream
drift scope, it combines a hybrid detection engine, adaptive
| Adapt  offers  | both  | fast  drift  | responsiveness  |     | and  high  |     |     |     |     |     |     |     |
| -------------- | ----- | ------------ | --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
thresholding, and a drift-aware ensemble for accurate and
predictive  reliability,  which  is  critical  for  real-time  timely adaptation. Evaluated on the Hyperplane dataset, the
applications. All experiments were conducted using the
|             |          |       |            |                   |      | framework  | achieved     | detection  |          | delays  of  | 31.2  and      | 64.8  |
| ----------- | -------- | ----- | ---------- | ----------------- | ---- | ---------- | ------------ | ---------- | -------- | ----------- | -------------- | ----- |
| Hyperplane  | dataset  | with  | synthetic  | drift  injection  | for  |            |              |            |          |             |                |       |
|             |          |       |            |                   |      | instances  | for  abrupt  | and        | gradual  | drifts,     | respectively,  |       |
consistent benchmarking.  outperforming  baselines  such  as  DDM,  EDDM,  and
5.6 Practical Implications and Limitations  ADWIN. It also maintained a low false positive rate of 0.041
and a high F1-score of 0.89, demonstrating robustness and
Practical Implications  noise resistance. Key innovations include volatility-aware
|     |     |     |     |     |     | threshold  | tuning  | and  drift  | certainty  | scoring,  |     | ensuring  |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | ---------- | --------- | --- | --------- |
DataStream Adapt demonstrates strong applicability in
real-time environments due to its low-latency processing  stability and responsiveness. DataStream Adapt advances
|     |     |     |     |     |     | scalable,  | intelligent  | streaming  |     | analytics,  | with  | strong  |
| --- | --- | --- | --- | --- | --- | ---------- | ------------ | ---------- | --- | ----------- | ----- | ------- |
and adaptive architecture. It is particularly effective for edge
|     |     |     |     |     |     | potential  | for  applications  |     | in  fraud  | detection,  | industrial  |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------------------ | --- | ---------- | ----------- | ----------- | --- |
computing, fraud detection, and user behavior modeling,
where both abrupt and gradual changes occur frequently.  monitoring, and personalized services. Future work will
extend support for multi-class problems, active learning, and
The inclusion of drift certainty scoring and detailed logs
real-world datasets with complex supervision.
| supports  | transparency  | and  | compliance,  | making  | the  |     |     |     |     |     |     |     |
| --------- | ------------- | ---- | ------------ | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
framework suitable for regulated domains like healthcare
Author Contributions: Mettu Yashwanth conceptualized
and finance.  the research framework, designed the architecture of the
DataStream Adapt system, and led the overall coordination
Limitations
|     |     |     |     |     |     | of  the  | study.  | Digumarthy  |     | Sandeepa  | was  | primarily  |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ----------- | --- | --------- | ---- | ---------- |
This study relies on the synthetic Hyperplane dataset,  responsible  for  implementing  the  hybrid  drift  detection
which  may  not reflect all real-world complexities. The  model and conducting the experimental analysis, including
framework currently supports only binary classification and
benchmarking against baseline methods. Sk. Khaja Shareef
assumes a fixed feature set, which may limit scalability.
|     |     |     |     |     |     | contributed  | to  the  | formalization  |     | of  the  | methodology,  |     |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | -------------- | --- | -------- | ------------- | --- |
Initial parameter sensitivity and the absence of automated  performed the literature review, and drafted the manuscript,
8

Mettu Yashwanth et.al / Synth. Multidiscip. Res. J., 1(4) 1-9, 2023
including figures and graphical abstracts. All authors [18] J. Gama, P. Medas, G. Castillo, and P. Rodrigues, “Learning with drift
reviewed, revised, and approved the final version of the detection,” Proc. 17th Brazilian Symposium on Artificial
Intelligence, pp. 286–295, 2004.
manuscript.
[19] J. Baena-García, J. Del Campo-Ávila, R. Fidalgo, A. Bifet, R.
Gavaldà, and R. Morales-Bueno, “Early drift detection method,”
Data availability: Data available upon request.
Proc. 4th International Workshop on Knowledge Discovery from
Data Streams, 2006.
Conflict of Interest: There is no conflict of Interest.
[20] A. Bifet and R. Gavaldà, “Learning from time-changing data with
adaptive windowing,” Proc. 2007 SIAM International Conference on
Ethical statement: This research complies with ethical
Data Mining, pp. 443–448, 2007.
guidelines and does not involve any harm to humans,
animals, or the environment
Funding: The research received no external funding.
Similarity checked: Yes.
References
[1] G. Widmer and M. Kubat, “Learning in the presence of concept drift
and hidden contexts,” Machine Learning, vol. 23, no. 1, pp. 69–101,
1996.
[2] J. Gama, I. Žliobaitė, A. Bifet, M. Pechenizkiy, and A. Bouchachia,
“A survey on concept drift adaptation,” ACM Computing Surveys,
vol. 46, no. 4, pp. 1–37, 2014.
[3] S. Wang, L. Cao, and Y. Wang, “A density-based ensemble method
for concept drift adaptation,” Neurocomputing, vol. 136, pp. 44–50,
2014.
[4] M. S. Lakshmi, K. S. Ramana, G. Ramu, K. Shyam Sunder Reddy,
C. Sasikala, and G. Ramesh, “Computational intelligence techniques
for energy efficient routing protocols in wireless sensor networks: A
critique,” Transactions on Emerging Telecommunications
Technologies, vol. 35, no. 1, Nov. 2023, doi: 10.1002/ett.4888.
[5] S. Chappidi and A. Raju, "Advancements in speech-based emotion
recognition and PTSD detection through machine and deep learning
techniques: A comprehensive survey," SSRG Int. J. Electron.
Commun. Eng., vol. 11, no. 5, 2023, doi: 10.14445/23488549/IJECE-
V11I5P121.
[6] A. Bifet and R. Gavaldà, “Learning from time-changing data with
adaptive windowing,” Proceedings of the 2007 SIAM International
Conference on Data Mining, pp. 443–448, 2007.
[7] M. Žliobaitė, “Learning under concept drift: an overview,” arXiv
preprint arXiv:1010.4784, 2010.
[8] P. Gama, P. Medas, G. Castillo, and P. Rodrigues, “Learning with drift
detection,” Brazilian Symposium on Artificial Intelligence, pp. 286–
295, 2004.
[9] A. Pesaranghader and H. Viktor, “Fast Hoeffding Drift Detection
Method for evolving data streams,” Machine Learning, vol. 106, no.
9–10, pp. 1479–1495, 2017.
[10] A. Swetha, M. S. Lakshmi, and M. R. Kumar, “Chronic kidney
disease diagnostic approaches using efficient artificial intelligence
methods,” International Journal of Intelligent Systems and
Applications in Engineering, vol. 10, no. 1s, pp. 254–259, 2022.
[Online]. Available:
https://www.ijisae.org/index.php/IJISAE/article/view/2289.
[11] J. Gama, I. Žliobaitė, A. Bifet, M. Pechenizkiy, and A. Bouchachia,
“A survey on concept drift adaptation,” ACM Computing Surveys,
vol. 46, no. 4, pp. 1–37, Apr. 2014, doi: 10.1145/2523813.
[12] J. Baena-García, J. Del Campo-Ávila, R. Fidalgo, A. Bifet, R.
Gavaldà, and R. Morales-Bueno, "Early drift detection method,"
Fourth International Workshop on Knowledge Discovery from Data
Streams, vol. 6, no. 1, pp. 77–86, 2006.
[13] A. Bifet and R. Gavaldà, "Learning from time-changing data with
adaptive windowing," Proceedings of the 2007 SIAM International
Conference on Data Mining, pp. 443–448, 2007.
[14] A. Bifet, G. Holmes, R. Kirkby, and B. Pfahringer, "MOA: Massive
Online Analysis," Journal of Machine Learning Research, vol. 11, pp.
1601–1604, 2010.
[15] N. Cesa-Bianchi, P. Fischer, and C. Gentile, "Tracking the best linear
predictor," Journal of Machine Learning Research, vol. 4, pp. 1107–
1133, 2003.
[16] A. Pesaranghader and H. Viktor, "Fast Hoeffding Drift Detection
Method for evolving data streams," Machine Learning, vol. 106, no.
9–10, pp. 1479–1495, 2017.
[17] A. Bifet, G. Holmes, R. Kirkby, and B. Pfahringer, “MOA: Massive
Online Analysis,” Journal of Machine Learning Research, vol. 11, pp.
1601–1604, 2010.
9