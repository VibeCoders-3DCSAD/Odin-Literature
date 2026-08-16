---
conversion_metadata:
  converted_at: "2026-07-21T08:06:22Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Patterson & Lindberg.pdf"
  source_pdf_sha256: "51c0277670adbb4e8e302b03eff9008416df85f37df2d3d91ed79167c6f2b610"
  page_count: 18
  markdown_char_count: 155982
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

JOURNAL OF GLOBAL ENGINEERING REVIEW

ISSN: 3071-4656

Concept drift monitoring and continual learning in production AI 
systems: an empirical cost–benefit comparison of detection 
methods and adaptation strategies 
Sarah M. Patterson1, Marcus J. Lindberg2

1 Department of Computer Science, University of California, Berkeley, CA, USA 
2 Institute for Computational and Mathematical Engineering, Stanford University, CA, USA

A b s t r a c t

Production machine learning systems face a persistent operational challenge: the distribution of input features and the 
conditional distribution of labels can shift over time, eroding the predictive performance that motivated deployment. 
This paper conducts an empirical comparison of three widely used concept drift detectors—ADWIN, DDM, and Page–
Hinkley—paired with two adaptation strategies, incremental learning and full retraining. Using two publicly available 
streaming  benchmarks  (Electricity  and  SEA)  augmented  with  a  synthetic  noisy  variant,  we  construct  a  cost–benefit 
framework that jointly accounts for predictive accuracy, drift-response latency, computational cost, and false-alarm 
rate. Across 60 controlled trials, ADWIN paired with incremental learning achieved the highest accuracy-to-cost ratio 
on stationary segments and gradual drifts, while DDM combined with periodic retraining reacted most decisively to 
abrupt shifts at the cost of higher compute. Page–Hinkley provided a useful middle ground when budget is moderately 
constrained.  No  single  configuration  dominated  across  regimes;  engineers  should  select  detectors  based  on  the 
dominant drift profile of their pipeline.

K e y w o r d s :   concept  drift,  continual  learning,  online  machine  learning,  production  AI  monitoring,  cost–benefit 
analysis

1.  Introduction 
Deploying a machine learning model into production rarely marks the end of engineering effort; it begins a 
new phase in which the operating environment becomes the dominant source of risk. The training distribution 
that informed model selection captures only a snapshot, and many real-world streams—financial transactions, 
click  logs,  sensor  telemetry,  healthcare  records—evolve  in  subtle  and  sometimes  abrupt  ways.  This 
phenomenon  is  broadly  known  as  concept  drift,  and  it  has  been  documented  across  high-stakes  domains 
including transaction fraud detection  [1], financial data quality monitoring  [2], cardiovascular risk prediction 
from  wearable  signals  [3],  and  microservice  performance  degradation  [4].  When  drift  goes  unnoticed, 
downstream consequences range from quiet revenue loss to safety-critical errors.

Production  teams  therefore  need  a  monitoring  and  adaptation  layer  that  does  three  things  at  once:  detects 
distributional shifts soon enough for action, decides whether to update or fully retrain the model, and keeps 
the operational cost of these decisions inside a predictable budget [5]. Each task involves trade-offs imperfectly 
captured by accuracy alone. Detecting drift earlier reduces error but raises the false-alarm rate [6]; incremental 
updates are cheap but may underfit abrupt shifts [7]; full retraining recovers accuracy but consumes compute 
and engineering attention [8].

A  wide  body  of  recent  applied  work  illustrates  how  drift-related  problems  arise  across  very  different 
application contexts. Real-time payment fraud detection with deep learning ensembles [9], adaptive thresholds 
for healthcare claims monitoring [10], multi-risk early warning for community banks [11], and zero-day anomaly 
detection  in  cloud  infrastructure  [12]  all  share  a  structural  pattern:  a  streaming  signal  whose  underlying 
generating  process  is  non-stationary.  The  methods  used  to  address  them—sliding  windows,  ensembling, 
retraining triggers—are conceptually related to the drift detectors studied in this paper.

The empirical study presented here is motivated by a gap practitioners frequently report: although individual 
drift  detectors  have  well-known  statistical  properties,  comparative  evidence  on  the  cost–benefit  profile  of 
detector–strategy  pairs  in  realistic  production  budgets  is  scarce.  We  focus  on  three  classical  detectors—
ADWIN, DDM,  and Page–Hinkley—because they are simple to  implement,  widely  available, and impose 
modest memory overhead. We pair each with two adaptation responses: incremental learning, in  which the 
model is updated on detected change without discarding existing weights, and full retraining, in which a new 
model is fitted on a fresh window. The contributions of this paper are: (1) a unified cost–benefit framework 
integrating  accuracy,  latency,  compute  cost,  and  false-alarm  rate;  (2)  a  controlled  empirical  study  on  the

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

1

---

<!-- PAGE 2 -->

Electricity and SEA benchmarks plus a synthetic noisy variant; and (3) practical decision rules for selecting 
detector–strategy pairs based on dominant drift type. Figure 1 illustrates the overall research framework.

The  remainder  of  this  paper  is  organized  as  follows.  Section  2  reviews  related  work  on  drift  detection, 
continual  learning,  and  adjacent  applied  areas.  Section  3  presents  the  methodology,  including  detector 
formulations and the cost–benefit model. Section 4 describes the experimental design. Section 5 reports results 
and ablation analysis. Section 6 discusses limitations and operational implications, and Section 7 concludes.

2. Related work 
2.1. Drift detection and streaming adaptation

Statistical change detection has a long history, and its application to streaming machine learning has produced 
a  small  set  of  detectors  used  widely  in  practice.  ADWIN  maintains  a  window  of  recent  observations  and 
triggers when two sub-windows show a statistically significant mean difference; DDM monitors error-rate 
changes  in  a  binary  classifier;  Page–Hinkley  aggregates  a  one-sided  cumulative  deviation  signal.  Recent 
applied  extensions  of  these  ideas  include  time-decay  aware  incremental  feature  extraction  for  fraud  [1], 
adaptive thresholds tuned to financial data quality [2], lightweight stress testing for small and medium financial 
institutions using variational  autoencoders with  extreme value theory  [13], and feature-selection screens for 
high-dimensional streams [14]. A consistent observation is that drift detectors rarely operate in isolation; they 
are components of larger early-warning pipelines that combine signals from multiple sources [11, 15]. Table 
1 summarizes a representative selection of these contributions.

Several authors study drift-adjacent problems through the lens of explainability and fairness. Fairness-aware 
feature attribution for credit scoring  [16] and feature attribution for market risk stress  [17] show that drift can 
manifest  not  only  as  accuracy  decay  but  also  as  subgroup-specific  reliability  changes.  Trustworthiness 
evaluation  of  AI-assisted  medical  imaging  that  integrates  confidence  calibration  and  distribution-shift 
detection [18] and fairness–accuracy trade-offs in credit scoring under reweighting and resampling [19] connect 
the drift literature to the broader trustworthy-ML agenda.

Table 1. Representative recent studies on drift detection, adaptive thresholds, and streaming risk monitoring.

Reference

Domain

Method family

Drift handling

[1]

[2]

[3]

[10]

[11]

[13]

[15]

[28]

Transaction fraud

Time-decay features

Incremental

Data quality monitoring

Adaptive threshold

Online

Cardiovascular risk

Adaptive threshold

Streaming

Healthcare claims

Temporal features

Threshold optimization

Community banks

Ensemble + XAI

Online warning

Stress testing

VAE + EVT

Periodic refit

Cross-market risk

Network analysis

Event-driven

Consumer credit

Time-series anomaly

Adaptive

2.2. Online fraud, risk and anomaly detection

Financial fraud detection has produced an unusually rich body of empirical work on streaming data, and the 
patterns reported there inform our experimental design. Comparative studies of unsupervised approaches for 
billing anomalies [20], graph-based representation learning for fraud [21], and graph-attention models for cross-
market contagion  [22] all confront the non-stationarity of fraud strategies. Behavioral sequence detection  [6], 
explainable risk stratification for hospital readmission  [23], and click-pattern anomaly studies [24, 25] cover 
similar  territory.  Synthetic-identity  fraud  feature  engineering  [26]  and  dynamic  margin-period-of-risk 
prediction  in  counterparty  management  [27]  add  further  evidence  that  streaming  feature  pipelines  must  be 
paired with monitoring.

Adjacent risk-warning studies include consumer credit default optimization [28], cross-border anomalous fund-
flow analysis  [29], fairness-aware multimodal chronic-disease risk  [30], and statistical  anomaly detection for

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

2

---

<!-- PAGE 3 -->

payroll field-mapping [31]. Although topically diverse, they share a methodological commitment to incremental 
updates and adaptive thresholds—both concepts central to our experiments.

2.3. Continual and federated learning

Beyond pure detection, the continual-learning literature addresses how a model should be updated once drift 
is confirmed. Federated approaches mitigate the cost of centralized retraining by distributing updates across 
clients [32], and adaptive privacy-budget allocation has been studied for healthcare federated learning [33] and 
federated  document  classification  [34].  A  practical  implementation  study  of  federated  learning  [35]  and  a 
systematic review of medical-AI federated learning [36] frame federation as a continual-learning enabler. The 
federated  transparent  adaptive  financial  optimizer  (FTAFO)  [37]  and  privacy-preserving  federated  risk 
monitoring  across  financial  institutions  [38]  illustrate  how  continual-learning  ideas  appear  in  financial 
workflows.

Privacy-preserving  variants  further  include  differential-privacy  approaches  to  feature  attribution  [39], 
multimedia content  [40], and click-through-rate prediction  [41], as well as rare-disease patient  discovery  [42], 
creator-platform revenue transparency  [43], collaborative healthcare learning with gradient compression  [44], 
and customer-service AI evaluation [45]. Privacy-preserving financial transaction analytics [46] complete the 
picture: adaptation under privacy constraints is a structurally similar problem to adaptation under drift.

2.4. Cross-domain methodological inspiration

Drift research benefits from cross-pollination with related areas. Multimodal fusion strategies developed for 
cardiovascular  prediction  [47,  48],  cancer  detection  [49],  biomarker  discovery  [50],  and  seasonal  demand 
forecasting [51] illustrate methods for combining heterogeneous inputs—a building block of many production 
pipelines.  Risk-prediction  frameworks  from  cybersecurity  contribute  relevant  ideas:  data-leakage  risk 
assessment  [52],  firmware  vulnerability  prioritization  [53],  graph-based  supply-chain  attack  detection  [54], 
industrial-control attack-path reasoning  [55], and ensemble threat-pattern recognition  [56]. LLM-driven threat 
intelligence [57] and jailbreak attack/defense studies [58] further extend the security-monitoring repertoire.

Healthcare  AI  provides  additional  methodological  reference  points.  Retrieval-augmented  generation  for 
medical question answering  [59], cross-cultural dialogue understanding  [60], PII detection in clinical text  [61], 
and clinical-trial recruitment with multi-modal deep learning [62] are all driven by streaming data with shifting 
characteristics. Hospital  readmission stratification  [23], hospital resource forecasting under epidemic surges 
[63], polypharmacy risk in elderly populations [64], community-level infection early warning [65], and intelligent 
recognition of insurance anomalies [66] all face concept-drift-style problems. Anatomy-aware contrastive pre-
training [67], multi-engine OCR for unstructured medical documents [68], OCR engine selection for government 
documents  [69], and pre-trained language models for medical workflow routing  [70] together emphasize that 
domain shifts in input modality matter as much as label-distribution drift.

Specialized medical AI applications include drug-combination optimization with reinforcement learning [71], 
Bayesian nanobody screening [72], radiotherapy dose optimization [73], breast-cancer recurrence prediction [74], 
ovarian-stimulation  protocol  optimization  [75],  gonadotoxicity  risk  in  young  cancer  patients  [76],  protein-
interface  analysis  for  inflammatory  targets  [77],  drug-target  prediction  with  graph  attention  [78],  and 
photodynamic-therapy  dose  optimization  [79].  Each  contains  a  streaming  or  feedback  element  where  drift 
detection could improve robustness. Medical animation generation [80, 81, 82] and noise suppression for LED 
imaging [83] add further breadth.

2.5. Operational AI systems and adjacent applications

Production AI systems must also handle non-trivial operational concerns: cloud resource scheduling under 
burst loads  [84], adaptive convex optimization for energy-efficient cloud scheduling  [85], carbon-aware geo-
distributed workload scheduling [86, 87], and ML-based building energy prediction [88]. Carbon-credit project 
quality assessment [89], vulnerable-population equity in energy transition  [90], retail transportation efficiency 
[91], last-mile delivery path optimization  [92], and supply-chain digital-twin scenario analysis  [93] connect AI 
monitoring  to  sustainability  concerns  and  face  streaming  inputs  with  seasonal  and  adversarial  drift.  Other 
adjacent  areas  include  e-commerce  return  management  with  reinforcement  learning  [94],  spatiotemporal 
preference  modeling  for  ride-hailing  [95],  advertising  creative  optimization  [96],  bot-traffic  and  click-fraud 
detection in mobile advertising  [97], luxury-brand seasonal forecasting  [98], commercial real-estate matching 
[99],  NLP  for  ESG  sentiment  [100],  NLP  for  UHNW  client  behavior  [101],  cryptocurrency  forecasting  via 
reinforcement learning [102], and pension target-date dynamic asset allocation [103]. Credit-related applications 
include credit-risk transmission in supply chains  [104], credit risk for SMEs  [105], asset-backed-securities text 
mining [106], anti-money-laundering automation comparisons [107], RPA financial audit efficiency [108], jump-
diffusion  CVA  importance  sampling  [109],  cross-asset  liquidity  contagion  [110],  and  intelligent  compliance 
reporting [111].

Compliance and document analytics include large-scale contract review for IPO audits [112], NER for M&A 
documents  [113],  jurisdiction-clause  identification  [114],  tenant  legal-inquiry  classification  [115],  contingent-

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

3

---

<!-- PAGE 4 -->

liability classification  [116], SEC disclosure discrepancy detection  [117], XBRL semantic mismatch detection 
[118],  cross-border  compliance  violation  detection 
[120], 
psychological-contract risk in cross-cultural teams  [121], welfare-program enrollment causal evaluation  [122], 
multi-objective  particle-swarm  optimization  for  renewable-energy  site  selection  [123],  and  ML-based 
government-document classification [124].

[119],  customer-service  quality  assessment

Vision and animation studies provide methodological references on representation learning and adaptation: 
deepfake detection [125], LiDAR–camera lightweight detection [126], multi-sensor adverse-weather fusion [127], 
V2X  cooperative  3D  detection  [128],  YOLO-based  3D-printed  defect  detection  [129],  depth  estimation  [130], 
illumination normalization for autonomous driving [131], low-light enhancement [132], super-resolution attention 
[133],  DeepMotionNet  for  FPS  games  [134],  facial-expression  communication  prediction  [135],  cross-lingual 
telemedicine animation [136], GAN keyframe interpolation [137], style-genes artwork authentication [138], CNN-
based Chinese artwork classification  [139], and blockchain provenance verification for art  [140]. Knowledge-
graph completion methods [141] and banking customer segmentation via deep embedding clustering [142] round 
out the methodological landscape. Specialized domains include adaptive interventions for autism spectrum 
disorder  [143,  144,  145,  146,  147,  148],  biomechanical  property  prediction  for  biomedical  materials  [149], 
dental  polymer  formulation  [150],  dental  shade  classification  [151],  NSGA-II  for  dental  resin  printing  [152], 
healthcare data-quality governance [153], misinformation detection via cross-modal verification [154], temporal-
graph  behavior  detection  on  social  platforms  [155,  156],  and  server  power-consumption  prediction  [157]. 
Methodological cross-references extend to oversampling–ensemble interactions for tabular imbalance [158], a 
comprehensive  review  of  agentic  AI  [159],  prompt-strategy  comparisons  for  code  generation  with  large 
language models [160, 161], LLM zero/few-shot translation in low-resource languages [162], prompt evaluation 
for AI agents  in programming  education  [163], discrete-diffusion versus  autoregressive text generation  [164], 
web-agent  reinforcement  learning  [165],  cooperative  multi-agent  online  learning  [166],  memory-poisoning  in 
multi-agent systems [167], and continuous reorganization of agent memory under distributed change [168].

[ Figure 1 (overall framework): Stream input → feature pipeline → deployed predictor → drift detector (ADWIN/DDM/Page-
Hinkley) → if drift signal: incremental update or full retrain → cost-benefit scoring → monitoring dashboard. ]

Figure 1. Overall research framework. The deployed predictor produces real-time outputs while three drift 
detectors  observe  error  and  feature  signals;  on  a  positive  trigger,  an  adaptation  policy  chooses  between 
incremental update and full retraining, and a cost–benefit module scores the round.

3. Methodology 
3.1. Problem formulation

Let the labeled stream be {(x_t, y_t)} for t = 1, …, T, where x_t is a d-dimensional feature vector and y_t ∈ 
{0,1} is the binary target. A predictor f_θ is deployed to produce ŷ_t = f_θ(x_t). Concept drift occurs when 
the joint distribution P_t(x, y) changes between two times t_a < t_b. We focus on virtual drift (changes in P(x) 
only) and real drift (changes in P(y ∣ x)), as production pipelines typically must respond to both.

3.2. Drift detectors

Three detectors were instantiated. ADWIN partitions a sliding window into all valid sub-windows and applies 
a Hoeffding bound to detect mean shifts; we used δ = 0.002 and a maximum window of 5,000. DDM tracks 
the error rate p_t and its standard deviation s_t of the deployed classifier, raising a warning at p_t + s_t ≥ 
p_min + 2 s_min and a drift signal at p_t + s_t ≥ p_min + 3 s_min. Page–Hinkley computes a cumulative one-
sided sum m_t = Σ (e_i − ē − δ_PH) and triggers when m_t − min_≤t m_i > λ_PH, with δ_PH = 0.005 and 
λ_PH = 50. Table 2 summarizes the configurations.

Table 2. Configuration of the three drift detectors used in this study and the comparison method category they 
instantiate.

Detector

Method category

Key parameter

Rationale

ADWIN

Window-based  mean 
test

δ = 0.002, w_max = 
5000

Strong theoretical guarantees, low false 
alarm

DDM

Error-rate monitor

warn at +2s, drift at +3s  Direct response to label-distribution

change

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

4

---

<!-- PAGE 5 -->

Page–
Hinkley

Cumulative deviation

δ_PH = 0.005, λ_PH = 
50

Conservative trigger, low compute

3.3. Adaptation strategies

Two adaptation responses were specified. Incremental learning updates the model parameters using the latest 
observation buffer (size 200) without discarding existing weights. We use a Hoeffding tree as the base learner 
because of its native streaming support and low memory footprint. Full retraining discards the current model 
and refits a new model on the most recent window of 5,000 examples, using gradient boosting; this strategy 
carries higher compute cost but recovers from severe drift more reliably.  The class-imbalance behavior of 
streaming classifiers under varying minority ratios has been studied empirically in tabular benchmarks  [158], 
which informs our buffer-sizing choices. Filter-based feature selection [14] is applied each retraining cycle.

3.4. Cost–benefit framework

We define the operational cost–benefit score S of a detector–strategy pair on a stream segment as S = α · Acc 
− β · Lat − γ · Cost − δ · FAR, where Acc is segment accuracy, Lat is mean drift-response latency in time 
steps, Cost is the per-step compute (proportional to update operations), and FAR is the false-alarm rate. The 
coefficients (α, β, γ, δ) encode operational priorities; we use a default of (1.0, 0.05, 0.1, 0.4) calibrated so that 
all four terms contribute non-trivially under our datasets. Figure 2 sketches the methodological pipeline from 
raw stream ingestion through detection, adaptation, and scoring. The framework is deliberately transparent: 
each term can be substituted with domain-specific cost models, mirroring how compliance-aware analytics 
frameworks have been designed in adjacent domains [110, 111].

[ Figure 2 (methodological pipeline): Raw stream → prequential evaluation loop: predict → score loss → detector update → 
if trigger: adaptation policy (incremental/retrain) → update model → record (Acc, Lat, Cost, FAR) → cost-benefit score S. ]

Figure 2. Methodological pipeline showing the prequential evaluation loop, detector–strategy interaction, and 
cost–benefit aggregation.

4. Experimental design 
4.1. Datasets

We selected two widely cited streaming benchmarks. The Electricity dataset contains 45,312 records of binary 
labels  (price  up/down)  sampled  half-hourly  over  two  years,  with  documented  gradual  and  recurring  drift 
induced  by  demand  cycles.  The  SEA  generator  was  configured  with  three  concept  changes  at  time  steps 
12,500, 25,000, and 37,500, producing 50,000 records of three-feature inputs and a binary label, simulating 
abrupt drift. To stress-test detectors under moderate noise—a common feature of production pipelines—we 
constructed a third dataset, SEA-Noisy, by injecting label noise with rate 0.10 throughout SEA and adding 
feature noise during the abrupt transitions. Table 3 summarizes the experimental configurations.

Table 3. Dataset configurations used in the empirical study.

Dataset

Records

Features

Drift type

Drift points

Electricity

45,312

SEA

50,000

SEA-Noisy

50,000

8

3

3

4.2. Models, metrics and protocol

Gradual / recurring

Continuous

Abrupt

12,500 / 25,000 / 37,500

Abrupt + label noise 0.10

12,500 / 25,000 / 37,500

The base learners were a Hoeffding tree (incremental) and an XGBoost ensemble (retraining), both configured 
with default settings except for buffer/window sizes already noted. Each detector–strategy pair was evaluated 
under five random seeds (different ordering, where applicable, and different stochastic noise) on each dataset. 
We report mean and standard deviation  across seeds. The four headline metrics are:  prequential  accuracy, 
mean detection delay (the time gap between the engineered drift point and the detector's first signal), update 
cost  (relative  units,  normalized  to  the  cheapest  configuration),  and  false-alarm  rate  (signals  fired  during 
stationary  segments  per  1,000  steps).  Adjacent  precedents  for  prequential  evaluation  appear  in  real-time 
transaction fraud benchmarks [1, 26] and adaptive HRV monitoring [3]. We additionally track segment-level

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

5

---

<!-- PAGE 6 -->

recovery time, which has previously been used to report degradation lead times in microservice telemetry [4, 
8].

5. Results and analysis 
5.1. Headline comparison

Table 4 reports the four headline metrics for each detector–strategy pair averaged across the three datasets and 
five seeds. ADWIN paired with  incremental  learning  achieved the highest  mean  accuracy (0.864) and the 
lowest update cost (1.00, by construction the reference baseline), at the expense of moderately higher detection 
delay on abrupt SEA shifts (mean 187 steps versus 142 for DDM + retraining). DDM combined with retraining 
showed the lowest detection delay (138 steps mean) and the highest abrupt-shift recovery, but its update cost 
was 4.7× the baseline and its false-alarm rate was 38% higher. Page–Hinkley with incremental learning sat 
between the two extremes, with cost 1.6× the baseline and the lowest false-alarm rate (0.42 per 1,000 steps).

Table 4. Headline performance comparison of detector–strategy pairs averaged across three datasets and five 
random seeds. Lower is better for Latency, Cost, and FAR; higher is better for Accuracy.

Detector + strategy

Accuracy  Latency (steps)  Cost (× baseline)

FAR (per 1k steps)

ADWIN + Incremental

ADWIN + Retraining

DDM + Incremental

DDM + Retraining

0.864

0.859

0.851

0.857

Page–Hinkley + Incremental

0.848

Page–Hinkley + Retraining

0.852

5.2. Stratified analysis by drift type

187

171

152

138

204

189

1.00

3.9

1.3

4.7

1.6

4.2

0.61

0.78

0.83

0.84

0.42

0.55

Stratifying by drift type sharpens the picture. On Electricity, where drift is gradual and recurring, ADWIN + 
Incremental dominated: highest accuracy (0.853), lowest cost, and the lowest false-alarm rate on stationary 
segments.  On SEA, where drift  is  abrupt,  DDM + Retraining recovered fastest  but  its accuracy advantage 
shrank (0.871 vs. 0.866 for ADWIN + Incremental) once detection delay was accounted for in the prequential 
window.  On  SEA-Noisy,  all  detectors  degraded—accuracy  dropped  by  approximately  4–6  percentage 
points—but ADWIN's controlled false-alarm rate continued to compound favorably across segments. Figure 
3 visualizes the per-segment accuracy and cost trade-off for the two leading configurations.

[ Figure 3 (per-segment trade-off): Two-line chart: x-axis = stream segment index; primary y-axis = accuracy (0.80–0.90); 
secondary y-axis = cumulative compute cost. ADWIN+Incremental (solid) keeps cost flat, accuracy gradually rising; 
DDM+Retraining (dashed) shows step-up cost spikes at drift points and faster recovery. ]

Figure 3. Per-segment accuracy versus cumulative compute cost for the two leading detector–strategy pairs 
(ADWIN + Incremental, solid; DDM + Retraining, dashed) across SEA. Cost spikes coincide with engineered 
drift points.

5.3. Ablation: cost-coefficient sensitivity

We varied the coefficient vector (α, β, γ, δ) to evaluate sensitivity. When compute is highly constrained (γ → 
0.5), incremental learning under any detector outperformed retraining on every dataset. When false alarms 
carry  high  penalty  (δ  →  1.0)—a  regime  relevant  to  compliance-sensitive  deployments  [111,  117]—Page–
Hinkley emerged as the preferred detector because its trigger rule is conservative. When detection latency is 
critical (β → 0.2)—as in fraud-scoring applications [9, 26]—DDM + Retraining was preferred despite its cost.

5.4. Qualitative observations

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

6

---

<!-- PAGE 7 -->

The  clearest  qualitative  finding  is  that  detector  quality  is  poorly  summarized  by  accuracy  alone.  Two 
configurations (ADWIN + Incremental and DDM + Retraining) achieved within 1 percentage point of each 
other on aggregate accuracy yet differed by nearly 5× in cost. Production decisions should therefore explicitly 
reflect  operational  coefficients,  much  as  they  do  in  adjacent  areas  where  multi-objective  evaluations  are 
standard, including supply-chain digital twins  [93], renewable-site optimization  [123], and dental 3D-printing 
optimization  [152].  Cross-domain  research  on  streaming  AI  deployments—covering  autism  intervention 
adaptation [144, 147], welfare-program reminder strategies  [122], cross-cultural team risk  [121], and last-mile 
delivery [92]—reinforces this point: a single accuracy figure rarely captures the relevant trade-offs.

6. Discussion 
6.1. Threats to validity

Three threats merit explicit acknowledgement. First, the Electricity and SEA benchmarks may not represent 
all  production  drift  profiles;  deployments  with  heavy  seasonal  cycles  (e.g.,  luxury  retail  forecasting  [98]  or 
hospital infection surges [65]) may favor different detector tunings. Second, the cost coefficients are illustrative 
rather than universal; teams should calibrate them against the true unit costs of compute, labeling, and false-
positive remediation, as is standard in audit-efficiency analyses  [108]. Third, our evaluation considered only 
binary  classification;  multi-class  and  regression  settings  introduce  additional  structure  that  may  shift  the 
relative ranking, much as multi-modal evaluation reshapes findings in other areas of medical AI [50, 67, 78].

6.2. Operational implications

For practitioners, three rules of thumb emerge. First, when the dominant drift profile is gradual and the false-
alarm  budget  is  small,  choose  ADWIN  paired  with  incremental  learning—this  configuration  consistently 
produced  the  best  accuracy-to-cost  ratio.  Second,  when  drift  is  abrupt  and  recovery  time  is  the  dominant 
business cost, choose DDM paired with retraining, accepting the higher compute and the higher false-alarm 
rate. Third, when compute is moderate and false alarms carry a heavy compliance cost, choose Page–Hinkley 
with incremental learning. These recommendations align with operational guidance offered in adjacent areas 
where decision rules must be transparent, including credit-scoring fairness [16, 19], compliance reporting [110], 
and cross-border financial monitoring [29, 119].

The framework also informs the design of monitoring dashboards and retraining triggers. Adaptive thresholds 
developed for cardiovascular risk [3], healthcare-claims warning [10], and microservice degradation [4] can be 
substituted  for  our  fixed  thresholds  when  domain-specific  calibration  data  is  available.  Cross-modal 
verification techniques used in misinformation detection [154] and ensemble methods evaluated under tabular 
imbalance [158] may further harden the detector layer in adversarial environments. Future work could integrate 
these ideas into a unified, configurable production-monitoring service.

6.3. Future directions

Three  directions  appear  especially  promising.  Embedding  drift  detectors  inside  larger  continual-learning 
systems with explicit memory management—motivated by recent multi-agent memory studies [167, 168]—
could  permit  selective  forgetting  under  bounded  resources.  Drift-aware  retraining  schedules  informed  by 
reinforcement-learning  controllers  [101,  102]  may  reduce  average  compute  without  sacrificing  recovery. 
Evaluating drift detectors in the presence of generative-model outputs—as in code generation [160, 161, 163], 
LLM  translation  [162],  programming  education  [163],  discrete-diffusion  text  [164],  and  web-agent  decision-
making  [165]—is  largely  uncharted;  sequential  agent-coordination  methods  [166]  also  raise  new  monitoring 
requirements. Hybrid systems that combine drift detection with domain-specific anomaly methods—building 
on  the  threat-pattern,  software-supply-chain,  and  attack-path  literature  [54,  55,  56],  cross-modal  artifact 
mining [125, 154], and edge-telemetry detection [8]—are a natural next step.

7. Conclusion 
We have presented an empirical comparison of three classical concept drift detectors—ADWIN, DDM, and 
Page–Hinkley—paired with incremental learning and full retraining strategies, evaluated under a unified cost–
benefit framework on two streaming benchmarks and a synthetic noisy variant. The headline finding is that 
no single configuration dominates across regimes. ADWIN + Incremental is preferred when drift is gradual 
and budget is tight; DDM + Retraining is preferred when drift is abrupt and recovery is critical; Page–Hinkley 
+  Incremental  sits  between  the  two  when  false  alarms  carry  compliance  cost.  The  proposed  cost–benefit 
framework  can  be  calibrated  against  domain-specific  operational  coefficients,  and  we  have  shown  how  it 
guides  selection  in  a  controlled  experimental  setting.  By  integrating  insight  from  adjacent  areas  including 
streaming fraud detection [1, 6, 9], multi-source data fusion [7, 51], explainability [16, 17, 19], and federated 
continual learning [32, 35, 36, 37], the framework offers a starting point for production teams that must move 
beyond accuracy-only metrics. Empirical validation on additional domains—covering health [62, 63, 64, 65], 
finance [109, 110, 111], operations [4, 8, 84], and vision [125, 126, 127, 132]—remains an open and important 
agenda.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

7

---

<!-- PAGE 8 -->

References 
[1]. Zhong, M. (2024). Time-Decay Aware Incremental Feature Extraction for Real-Time Transaction Fraud

Detection. Artificial Intelligence and Machine Learning Review, 5(3), 136-145.

[2]. Zhong,  M.  (2025,  September).  Adaptive  Anomaly  Detection  Threshold  for  Financial  Data  Quality 
Monitoring  Based  on  Time  Series  Features.  In  Proceedings  of  the  2025  International  Symposium  on 
Artificial Intelligence and Computational Social Sciences (pp. 578-587).

[3]. Shi, W., & Cheng, Z. (2024). Enhanced Adaptive Threshold Algorithms for Real-Time Cardiovascular

Risk Prediction from Wearable HRV Data. Journal of Advanced Computing Systems, 4(1), 46-57.

[4]. Cao, H., & Long, L. (2026). Empirical Evaluation of Multi-Source Monitoring Signal Effectiveness and 
Lead  Time  for  Performance  Degradation  Prediction  in  Kubernetes-Based  Microservices.  Journal  of 
Advanced Computing Systems, 6(4), 15-26.

[5]. Zhang,  J.  (2024).  Performance  Evaluation  and  Comparison  of  Machine  Learning  Algorithms  for 
Anomalous  Login  Behavior  Detection  in  Enterprise  Networks.  Artificial  Intelligence  and  Machine 
Learning Review, 5(2), 77-90.

[6]. Deng, M. (2025). Real-Time Fraud Risk Scoring through Behavioral Sequence Analysis: An Explainable 
Approach for Online Transaction Security. Journal of Sustainability, Policy, and Practice, 1(4), 130-142.

[7]. Han,  J.,  &  Cao,  G.  (2024).  A  Comparative  Study  of  Multi-source  Data  Fusion  Approaches  for  Credit

Default Early Warning. Artificial Intelligence and Machine Learning Review, 5(1), 105-116.

[8]. Long, X., Hu, J., & Ling, Z. (2026). A Comparative Analysis of Telemetry-Driven Anomaly Detection 
Approaches for Dual-Purpose Operational and Security Optimization in Edge Computing Infrastructure. 
Journal of Computing Innovations and Applications, 4(1), 79-88.

[9]. Zhang,  J.  (2026).  A  Comparative  Evaluation  of  Deep  Learning  and  Ensemble  Algorithms  for  Online

Payment Fraud Detection. Journal of Science, Innovation & Social Impact, 2(1), 164-177.

[10].  Han,  M.,  &  Lai,  J.  (2026).  Temporal  Feature  Engineering  and  Threshold  Optimization  for  Early 
Warning in Healthcare Claims Anomaly Detection. Journal of Advanced Computing Systems, 6(4), 27-
49.

[11].  Li,  Y.,  &  Ling,  Z.  (2026).  Real-Time  Multi-Risk  Early  Warning  for  Community  Banks:  An 
Application of Ensemble Anomaly Detection and Explainable Artificial Intelligence. Journal of Advanced 
Computing Systems, 6(2), 15-27.

[12].  Long,  X.  (2026).  Performance  Evaluation  of  Anomaly-Based  Detection  Approaches  for  Zero-Day 
Attack Early Warning in Cloud Infrastructure. Journal of Science, Innovation & Social Impact, 2(1), 352-
363.

[13].  Li, Y., &  Long, L. (2026). Lightweight AI-Driven Stress  Testing for Small and Medium Financial 
Institutions:  A  Variational  Autoencoder  Approach  with  Extreme  Value  Theory  for  Macroeconomic 
Scenario Generation. Artificial Intelligence and Machine Learning Review, 7(1), 108-119.

[14].  Min, S., & Wei, C. (2023). Comparative Analysis of Filter-based Feature Selection Methods for High-

Dimensional Data in Classification Tasks. Journal of Advanced Computing Systems, 3(8), 25-38.

[15].  Han, J. (2026). Network-Based Identification of Risk Contagion Pathways Between US Credit and

Equity Markets During Stress Periods. Journal of Advanced Computing Systems, 6(2), 50-63.

[16].  Zhong,  M.  (2025).  Fairness-Aware  Feature  Attribution  for  Credit  Scoring:  A  Causal  Path

Decomposition Approach. Journal of Science, Innovation & Social Impact, 1(1), 442-451.

[17].  Li, Z., Huang, Y., & Montgomery, I. (2024). Feature Attribution-Based Explainability Analysis for

Market Risk Stress Scenarios. Journal of Computing Innovations and Applications, 2(2), 136-150.

[18].  Chen, Y., & Lai, J. (2026). Multi-Metric Trustworthiness Evaluation of AI-Assisted Medical Imaging 
Diagnosis:  Integrating  Confidence  Calibration  and  Distribution  Shift  Detection.  Journal  of  Global 
Engineering Review, 4(1), 113-126.

[19].  Wang,  Z.,  &  Lai,  J.  (2026).  Fairness-Accuracy  Trade-offs  in  AI  Credit  Scoring:  A  Comparative 
Evaluation  of Reweighting  and Resampling  Strategies Under Multiple Fairness  Constraints. Journal  of 
Computing Innovations and Applications, 4(1), 117-126.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

8

---

<!-- PAGE 9 -->

[20].  Shi,  X.,  &  Weng,  H.  (2024).  Comparative  Analysis  of  Unsupervised  Learning  Approaches  for 
Anomalous Billing Pattern Detection in Healthcare Payment Integrity. Journal of Computing Innovations 
and Applications, 2(1), 111-127.

[21].  Wei, C., Ge, L., & Brooks, N. (2024). Graph-based Representation Learning for Financial Fraud and 
Anomaly Transaction Detection. Journal of Computing Innovations and Applications, 2(1), 153-164.

[22].  Li,  Y.,  Zhao,  F.,  &  Hu,  J.  (2026).  Identifying  Cross-Market  Risk  Contagion  Amplifiers  via  Graph 
Attention  Networks:  Empirical  Evidence  from  US  Financial  Stress  Periods.  Journal  of  Computing 
Innovations and Applications, 4(1), 164-175.

[23].  Liu, Y. (2025). Explainable Risk Stratification and Resource Coordination for Hospital Readmission 
Management  through  Integrated  Prediction-Intervention-Evaluation  Framework.  Journal  of  Science, 
Innovation & Social Impact, 1(2), 107-118.

[24].  Cao, H. (2024). Detecting Fraudulent Click Patterns in Mobile In-App Browsers: A Multi-dimensional 
Behavioral Analysis Approach. Artificial Intelligence and Machine Learning Review, 5(2), 130-142.

[25].  Cao,  H.  (2024).  Privacy-Preserving  Click  Pattern  Anomaly  Detection  for  Mobile  In-App  Browser

Advertising Fraud. Journal of Computing Innovations and Applications, 2(2), 151-161.

[26].  Huang,  Y.  (2025).  Enhanced  Feature  Engineering  and  Algorithm  Optimization  for  Real-Time 
Detection  of  Synthetic  Identity  Fraud  and  Money  Laundering  in  Financial  Transactions.  Journal  of 
Science, Innovation & Social Impact, 1(1), 384-397.

[27].  Huang,  Y.  (2025,  August).  Deep  learning-enhanced  dynamic  margin  period  of  risk  prediction  for 
counterparty credit risk management: A multi-modal approach integrating market sentiment analysis and 
real-time  exposure  assessment.  In  Proceedings  of  the  2nd  International  Conference  on  Intelligent 
Computing and Data Analysis (pp. 328-335).

[28].  Zhong, M. (2026). Optimization of Anomaly Detection Algorithms for Consumer Credit Default Rates 
Based on Time-Series Feature Extraction. Journal of Sustainability, Policy, and Practice, 2(1), 44-54.

[29].  Zhong, M. (2026). Multi-Dimensional Feature Analysis and Evaluation Methods for Anomalous Fund 
Flow  Identification  in  Cross-Border  Financial  Transactions.  Journal  of  Science,  Innovation  &  Social 
Impact, 2(2), 1-13.

[30].  Shi,  X.  (2026).  Fairness-Aware  Multimodal  Fusion  for  Early  Chronic  Disease  Risk  Prediction:  A 
Temporal Deep Learning Approach. Journal of Science, Innovation & Social Impact, 2(1), 217-231.

[31].  Cao, H., & Shi, W. (2026). Statistical Anomaly Detection Approach for Field Mapping Validation in 
Enterprise Payroll Data Migration. Journal of Computing Innovations and Applications, 4(1), 137-153.

[32].  Han,  J.  (2025).  AI-Enhanced  Cybersecurity  for  Financial  Networks:  A  Federated  Learning

Implementation. Journal of Science, Innovation & Social Impact, 1(1), 241-252.

[33].  Shi,  X. (2024). Adaptive Privacy Budget  Allocation Optimization for Multi-Institutional Federated

Learning in Healthcare. Journal of Advanced Computing Systems, 4(2), 50-61.

[34].  Zhang,  Q.  (2025,  December).  Adaptive  Differential  Privacy  Mechanism  for  Federated  Document 
Classification: A Gradient-Clipping Optimization Approach. In Proceedings of the 2025 6th International 
Conference on Computer Science and Management Technology (pp. 672-678).

[35].  Ren, W., Li, J.,  &  Wu,  X. (2024). Privacy-Preserving Data Analysis Using  Federated Learning:  A 
Practical Implementation Study. Artificial Intelligence and Machine Learning Review, 5(1), 40-50.

[36].  Wei,  C.,  &  Guan,  H.  (2024).  Privacy-Preserving  Federated  Learning  in  Medical  AI:  A  Systematic 
Review of Techniques, Challenges, and the Clinical Deployment Gap. Artificial Intelligence and Machine 
Learning Review, 5(3), 124-135.

[37].  Wang, Z., & Kang, A. (2025). FTAFO: A Federated Transparent Adaptive Financial Optimizer for 
Reducing Third-Party Dependencies in Workflow Management. Journal of Science, Innovation & Social 
Impact, 1(1), 329-339.

[38].  Zhong, M. (2026). Privacy-Preserving Federated Learning for Collaborative Risk Monitoring Across 
Financial  Institutions:  Balancing  Regulatory  Compliance  and  Intelligence  Sharing.  Journal  of 
Sustainability, Policy, and Practice, 2(2), 44-54.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

9

---

<!-- PAGE 10 -->

[39].  Li, X. (2025). Privacy-Preserving Feature Attribution Explanations for Large-Scale Recommendation 
Systems: A Differential Privacy Approach. Journal of Science, Innovation & Social Impact, 1(1), 19-32.

[40].  Lei, Y. (2025). Adaptive Privacy-Preserving Techniques for Multimedia Content Processing in Cloud 
Environments: A Differential Privacy Approach. Journal of Science, Innovation & Social Impact, 1(1), 
278-293.

[41].  Lu, X. (2025). Research on Mobile Advertising Click-Through Rate Prediction Algorithm Based on

Differential Privacy. Journal of Science, Innovation & Social Impact, 1(1), 362-371.

[42].  Pan,  Z.  (2024).  Privacy-Aware  AI  for  Rare-Disease  Patient  Discovery  and  Targeted  Outreach:  An

Effectiveness Study. Spectrum of Research, 4(1).

[43].  Zhang, J. (2025). Privacy-Preserving Revenue Transparency on Creator Platforms: An e-Differential-

Privacy Framework. Spectrum of Research, 5(2).

[44].  Han,  M.  (2025,  December).  Privacy-Preserving  Collaborative  Learning  Across  Healthcare 
Institutions: An Adaptive Approach with Gradient Compression and Dynamic Privacy Budget Allocation. 
In  Proceedings  of  the  2025  6th  International  Conference  on  Computer  Science  and  Management 
Technology (pp. 679-684).

[45].  Zhang, Y. (2026). Evaluation of Differential Privacy and Federated Learning for AI-Driven Customer

Service Applications. Journal of Sustainability, Policy, and Practice, 2(2), 55-66.

[46].  Wu,  Z.,  Zhang,  Z.,  Zhao,  Q.,  &  Yan,  L.  (2025).  Privacy-preserving  financial  transaction  analytics

under regulatory constraints. Journal of Science, Innovation & Social Impact, 1(2), 1-15.

[47].  Cheng,  Z.  (2025).  AI  Enabled  Cardiovascular  Disease  Risk  Prediction  through  Multimodal  Data 
Fusion: A Predictive Analytics Approach. Journal of Sustainability, Policy, and Practice, 1(2), 98-109.

[48].  Zhang,  F.,  Cheng,  Z.,  &  Holloway,  V.  (2024).  Deep  Learning  in  Cardiovascular  CT  Imaging: 
Evolution, Trends, and Clinical Translation from 2020 to 2025. Journal of Computing Innovations and 
Applications, 2(2), 88-99.

[49].  Zhang, C. (2025). Enhanced Multi-Modal Feature Fusion Algorithm for Early-Stage Cancer Detection: 
A Comparative Study of Optimization Strategies. Journal of Science, Innovation & Social Impact, 1(1), 
318-328.

[50].  Zhang, F., Ye, H., & Wei, C. (2024). Leveraging Multi-Modal Attention Mechanisms for Interpretable 
Biomarker Discovery and Early Disease Prediction. Journal of Computing Innovations and Applications, 
2(2), 111-121.

[51].  Wang, J. (2025). Multi-Source Data Fusion for Short-Term Demand Forecasting of Seasonal Retail 
Products: An Empirical Study Using Weather and Social Media Signals. Journal of Science, Innovation 
& Social Impact, 1(1), 340-349.

[52].  Wu, X., Li, J., & Ren, W. (2024). Risk Assessment Framework for Data Leakage Prevention Using

Machine Learning Techniques. Artificial Intelligence and Machine Learning Review, 5(3), 55-66.

[53].  Long, X. (2025). Research on Intelligent Firmware Vulnerability Detection and Priority Assessment 
Method Based on Hybrid Analysis. Journal of Science, Innovation & Social Impact, 1(1), 350-361.

[54].  Hu, J., & Long, X. (2024). Graph Learning-Based Behavioral Detection for Software Supply Chain

Attacks. Journal of Advanced Computing Systems, 4(4), 49-60.

[55].  Chen, Y. (2024). Explainable Attack Path Reasoning for Industrial Control Network Security Based

on Knowledge Graphs. Journal of Computing Innovations and Applications, 2(1), 128-139.

[56].  Ren,  W.,  Wu,  X.,  &  Li,  J.  (2025).  AI-Driven  Network  Threat  Behavior  Pattern  Recognition  and 
Classification:  An  Ensemble  Learning  Approach  with  Temporal  Analysis.  Journal  of  Advanced 
Computing Systems, 5(9), 1-13.

[57].

Jia, R., Zhang, J., & Prescot, J. (2024). An Empirical Study of Large Language Models  for Threat 
Intelligence Analysis and Incident Response. Journal of Computing Innovations and Applications, 2(1), 
99-110.

[58].  Shang, Z., Wei, W., & Bai, W. (2025). Evolving Security in LLMs: A Study of Jailbreak Attacks and

Defenses. arXiv preprint arXiv:2504.02080.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

10

---

<!-- PAGE 11 -->

[59].  Guan,  H.  (2025).  Medical  Terminology  Definition-Enhanced  Retrieval-Augmented  Generation  for 
Hallucination Mitigation in Medical Question Answering. Journal of Science, Innovation & Social Impact, 
1(1), 222-240.

[60].  Guan,  H.  (2025).  Context-Aware  Semantic  Ambiguity  Resolution  in  Cross-Cultural  Dialogue

Understanding. Journal of Sustainability, Policy, and Practice, 1(2), 136-147.

[61].  Guan, H. (2025). Intelligent Detection and Protection of Personally Identifiable Information in Clinical 
Text: An Advanced NLP Approach with Optimized Attention Mechanisms. Journal of Science, Innovation 
& Social Impact, 1(2), 41-52.

[62].  Wei, C., & Pan, Z. (2026). Accelerating Clinical Trial Recruitment Through Automated Eligibility 
Screening with Multi-Modal Deep Learning. Journal of Computing Innovations and Applications, 4(1), 1-
11.

[63].  Wang,  Y.  (2026).  Accuracy  Evaluation  of  Machine  Learning-Based  Hospital  Resource  Demand 
Forecasting During Infectious Disease Surges: A Comparative Analysis. Journal of Science, Innovation 
& Social Impact, 2(1), 314-327.

[64].  Wang,  Y.  (2026).  Explainable  Risk  Stratification  for  Polypharmacy-Related  Adverse  Outcomes  in 
Community-Dwelling Elderly: A Rule-Enhanced Machine Learning Approach. Journal of Sustainability, 
Policy, and Practice, 2(2), 18-31.

[65].  Wang, Y. (2025, December). Practical AI Approaches for Community Infection Early Warning: From 
Public Data to Actionable Insights. In Proceedings of the 2025 6th International Conference on Computer 
Science and Management Technology (pp. 1545-1552).

[66].  Han, M. (2025). Intelligent Recognition of Anomalous Behaviors in Medical Insurance Through Deep

Learning. Journal of Science, Innovation & Social Impact, 1(1), 410-426.

[67].  Han, M. (2026). Anatomy-Aware Contrastive Pre-training: Leveraging Spatial Consistency for Label-
Efficient Medical Image Diagnosis Across Multi-Modal Imaging. Journal of Sustainability, Policy, and 
Practice, 2(1), 55-70.

[68].  Zhang, Q. (2026). Improving Classification Accuracy for Unstructured Medical Documents via Multi-
Engine OCR and Deep Learning Collaboration. Journal of Advanced Computing Systems, 6(2), 1-14.

[69].  Zhang,  Q.  (2026).  Adaptive  OCR  Engine  Selection  and  Evaluation  for  Multi-Format  Government

Document Digitization. Artificial Intelligence and Machine Learning Review, 7(1), 29-39.

[70].  Zhang,  Q.  (2025).  Comparative  Analysis  of  Pre-Trained  Language  Models  for  Medical  Document 
Classification and Priority-Based Workflow Routing. Journal of Sustainability, Policy, and Practice, 1(4), 
205-221.

[71].  Ye,  H.  (2025).  Deep  Reinforcement  Learning-Driven  Efficacy-Toxicity  Balance  Optimization 
Strategy for Personalized Drug Combination in Cancer Patients. Journal of Science, Innovation & Social 
Impact, 1(1), 307-317.

[72].  Ye,  H.  (2025).  Bayesian  Optimization-Based  AI  Framework  for  Nanobody  Screening:  Minimizing 
Experimental Failures in ELISA Detection Systems. Journal of Sustainability, Policy, and Practice, 1(4), 
16-31.

[73].  Zhang, C. (2024). Deep Learning Dose Optimization with Uncertainty Quantification for Intensity-
Modulated  Radiotherapy:  A  3D  Radiomics  Approach.  Artificial  Intelligence  and  Machine  Learning 
Review, 5(2), 116-129.

[74].  Zhang, C., & Xiao, P. (2026). Optimizing Breast Cancer Recurrence Time Prediction with Attention-

Enhanced LSTM Networks. Journal of Advanced Computing Systems, 6(1), 80-98.

[75].  Zhang, C. (2025, October). Comparative Study of AI Algorithms in Personalized Ovarian Stimulation 
Protocol  Optimization:  Predictive  Performance  Analysis  Based  on  Patient  Baseline  Characteristics.  In 
Proceedings  of  the  4th  International  Conference  on  Artificial  Intelligence  and  Intelligent  Information 
Processing (pp. 654-662).

[76].  Zhang,  C.,  &  Liu,  M.  (2026).  Integrating  Ovarian  Reserve  Biomarkers  with  Machine  Learning  for 
Gonadotoxicity  Risk  Prediction  in  Young  Female  Cancer  Patients:  A  Scoping  Review.  Journal  of 
Computing Innovations and Applications, 4(1), 127-136.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

11

---

<!-- PAGE 12 -->

[77].  Ye, H. (2025, April). AI-Enhanced Detection of Dynamic Structural Changes in Inflammatory Protein 
Interfaces: A Case Study of CD11b/Mac-1 Interactions. In 2025 6th International Conference on Computer 
Engineering and Application (ICCEA) (pp. 2173-2180). IEEE.

[78].  Cheng, Z. (2025). Graph Attention-Based Feature Selection for Multi-Omics Drug Target Prediction

in Cardiovascular Diseases. Journal of Science, Innovation & Social Impact, 1(1), 294-306.

[79].  Dong,  Z.,  &  Jia,  R.  (2025).  Adaptive  Dose  Optimization  Algorithm  for  LED-based  Photodynamic 
Therapy Based on Deep Reinforcement Learning. Journal  of Sustainability, Policy, and Practice, 1(3), 
144-155.

[80].  Wang,  Z.  (2024).  Adaptive  Generation  of  Medical  Education  Animations  for  Enhanced  Health 
Literacy:  A  Personalization  Approach  for  Diabetes,  Vaccination,  and  Mental  Health  Communication. 
Journal of Advanced Computing Systems, 4(1), 30-45.

[81].  Li,  Z.,  &  Wang,  Z.  (2024).  AI-Driven  Procedural  Animation  Generation  for  Personalized  Medical 
Training  via  Diffusion-Based  Motion  Synthesis.  Artificial  Intelligence  and  Machine  Learning  Review, 
5(3), 111-123.

[82].  Li,  Z.,  &  Wang,  Z.  (2024).  Adaptive  Cross-Cultural  Medical  Animation:  Bridging  Language  and 
Context in AI-Driven Healthcare Communication. Artificial Intelligence and Machine Learning Review, 
5(1), 117-128.

[83].  Dong, Z., & Zhang, F. (2025). Deep Learning-Based Noise Suppression and Feature Enhancement 
Algorithm for LED Medical Imaging Applications. Journal of Science, Innovation & Social Impact, 1(1), 
9-18.

[84].  Lei,  Y.  (2025,  October).  Intelligent  Prediction  and  Dynamic  Scheduling  Optimization  Strategy  for 
Cloud  Computing  Resources  under  Burst  Load  Scenarios.  In  Proceedings  of  the  2025  International 
Symposium on Machine Learning and Social Computing (pp. 59-67).

[85].  Lei,  Y.,  &  Holloway,  V.  (2024).  Adaptive  Learning-Enhanced  Convex  Optimization  for  Energy-

Efficient Cloud Resource Scheduling. Journal of Advanced Computing Systems, 4(11), 73-85.

[86].  Chen,  Y.,  Chen,  Z.,  &  Zou,  D.  (2025).  CarbonShift:  Harnessing  Grid  Carbon  Variability  for  Geo-
Distributed Workload Scheduling. Artificial Intelligence and Machine Learning Review, 6(4), 18-31.

[87].  Chen,  Y.,  &  Chen,  Z.  (2025).  Multi-Objective  Deep  Reinforcement  Learning  for  Carbon-Aware 
Spatiotemporal Workload Scheduling in Geo-Distributed Data Centers. Journal of Advanced Computing 
Systems, 5(10), 18-30.

[88].  Zhang, D., & Zheng, Q. (2025). Machine Learning-Based Building Energy Consumption Prediction 
and Carbon Reduction Potential Assessment in US Metropolitan Areas. Journal of Industrial Engineering 
and Applied Science, 3(5), 27-40.

[89].  Zhang, D., & Wang, Y. (2025). AI-Driven Quality Assessment and Investment Risk Identification for 
Carbon Credit Projects in Developing Countries. Pinnacle Academic Press Proceedings Series, 3, 76-92.

[90].  Zhang,  D.,  &  Ma,  X.  (2025).  Machine  Learning-Based  Credit  Risk  Assessment  for  Green  Bonds: 
Climate Factor Integration and Default Prediction Analysis. Journal of Sustainability, Policy, and Practice, 
1(2), 121-135.

[91].  Zhang, D., & Zheng, Q. (2025). Machine Learning-Based Building Energy Consumption Prediction 
and Carbon Reduction Potential Assessment in US Metropolitan Areas. Journal of Industrial Engineering 
and Applied Science, 3(5), 27-40.

[92].  Zhang,  D.,  &  Zhang,  F.  (2025).  AI-Assisted  Identification  and  Equity  Assessment  of  Vulnerable 
Population Impacts in US Energy Transition. Journal of Advanced Computing Systems, 5(7), 1-17.

[93].  Zhang,  D.,  &  Zhang,  F.  (2025).  AI-Assisted  Identification  and  Equity  Assessment  of  Vulnerable 
Population Impacts in US Energy Transition. Journal of Advanced Computing Systems, 5(7), 1-17.

[94].  Wang,  Y.  (2025).  Data-Driven  Analysis  of  Transportation  Route  Efficiency  and  Carbon  Emission 
Correlation in Retail Distribution Networks. Journal of Science, Innovation & Social Impact, 1(1), 253-
264.

[95].  Shi, W., & Wang, J. (2026). Intelligent Path Optimization for Carbon-Constrained Last-Mile Delivery: 
A Reinforcement Learning and Heuristic Approach. Journal of Advanced Computing Systems, 6(1), 19-
31.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

12

---

<!-- PAGE 13 -->

[96].  Wang, J., & Jia, R. (2026). AI-Enhanced What-If Scenario Analysis in Supply Chain Digital Twins: 
A  Multi-Objective  Trade-Off  Perspective  on  Cost,  Resilience,  and  Carbon  Efficiency.  Journal  of 
Computing Innovations and Applications, 4(1), 97-105.

[97].  Xiao, P., Wang, Y., & Montgomery, I. (2024). Deep Reinforcement Learning for Route Optimization 
in E-commerce Return Management. Journal of Computing Innovations and Applications, 2(2), 100-110.

[98].  Shi,  X.  (2024).  Spatiotemporal  Preference  Modeling  for  Ride-Hailing  and  Context-Aware

Recommendations: A Machine-Learning Framework. Spectrum of Research, 4(2).

[99].  Lu,  X.  (2025,  August).  Adaptive  Optimization  of  Advertising  Creative  Visual  Elements  Based  on 
Multi-dimensional  User  Behavior  Data.  In  Proceedings  of  the  2025  International  Conference  on 
Generative Artificial Intelligence for Business (pp. 360-368).

[100].  Jia, R., Lu, X., & Whitmore, S. (2024). Feature-Based Detection of Bot Traffic and Click Fraud in 
Mobile Advertising: A Comparative Analysis. Journal of Computing Innovations and Applications, 2(1), 
140-152.

[101].  Liu,  H.,  Xu,  D.,  Ma,  Q.,  Xu,  S.,  &  Qiu,  D.  (2026).  Memory  Poisoning  Propagation  and  Repair 
Mechanism in Multi-Agent Collaborative Environments. Innovations and Applications, 2(1), 140-152.

[102].  Wang, X., Fu, X., & Zou, D. (2025). Passage, Sentence, or Proposition? An Empirical Comparison of 
Retrieval Granularity Effects on LLM Answer Accuracy in Retrieval-Augmented Generation. Journal of 
Global Engineering Review, 3(1), 81-90.

[103].  Xu, S., Ma, Q., Liu, H., & Yue, L. (2026). Continuous Reorganization and Performance Preservation 
of Agent Memory Structure Under Distributed Change Environments. Innovations and Applications, 4(1), 
127-136.

[104].  Pengyuan Xiao，Xuanyi Fu.  Comparative Evaluation of Post-Hoc Feature Attribution  Methods on

Tabular Financial Data: Faithfulness, Stability, and Computational Efficiency

[105].  Yifei  Li,Xuanyi  Fu.  Comparative  Evaluation  of  Graph  Neural  Networks  for  Cross-Market  Risk

Contagion Path Identification in Multi-Layer Financial Networks.

[106].  Tianxing Tang Xuanyi Fu

Chuankai  Luo.  An  Empirical  Comparison  of  High-Order  Feature 
Interaction Operators for Conversion Rate Prediction in Sparse, High-Cardinality Message-Ads Traffic：
Accuracy, Efficiency, and Offline–Online Consistency.

[107].  Xuanyi Fu, Tianxing Tang, Chuankai Luo. An Empirical Comparison of ReAct, Reflexion, Plan-and-
Solve,  and  Tree-of-Thought  Planning  Strategies  on  Financial  Question  Answering  and  Numerical 
Reasoning Tasks，

[108].  Xuanyi Fu, Danbing Zou.A Comparative Empirical Study of Over-Refusal Behavior in Closed-Source

Large Language Models on Pseudo-Harmful Prompts

[109].  Xuanyi Fu, Fanyi Zhao.An Empirical Comparison of Few-Shot Example Selection Strategies for In-

Context Learning on Public Reasoning and QA Benchmarks

[110].  Jiaying Li

,Minhao Li.Comparative Evaluation of Ensemble Learning Algorithms 
for  Visitor  Engagement  Prediction  and  Content  Recommendation  Optimization  in  Virtual  Museum 
Environments.Innovation & Social Impact, 2(1),.

,Muyu Liu

[111].  Wang,  J.  (2025,  October).  Artificial  Intelligence-Driven  Seasonal  Consumption  Forecasting  and 
Resource  Allocation  Optimization  in  Luxury  Brand  Marketing.  In  Proceedings  of  the  2025  2nd 
International Conference on Digital Economy and Computer Science (pp. 1119-1127).

[112].  Wang,  Z.  (2025,  October).  Machine  Learning-Driven  Investor-Asset  Matching  Optimization  in 
Commercial Real Estate Investment Decisions. In Proceedings of the 2025 2nd International Conference 
on Digital Economy and Computer Science (pp. 1110-1118).

[113].  Cai, Y. (2025). NLP-Quantified ESG News Sentiment and Portfolio Outcomes: Evidence from Real-

Time Signals. Annals of Applied Sciences, 6(1).

[114].  Cai, Y. (2025, June). NLP-Enhanced Predictive Analytics for UHNW Client Investment Behavior: A 
Risk-Aware  Portfolio  Optimization  Approach  in  Volatile  Markets.  In  Proceedings  of  the  2025  2nd 
International Conference on Digital Economy, Blockchain and Artificial Intelligence (pp. 185-191).

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

13

---

<!-- PAGE 14 -->

[115].  Zhao,  F.,  Zhang,  M.,  Zhou,  S.,  &  Lou,  Q.  (2024).  Application  of  deep  reinforcement  learning  for

cryptocurrency market trend forecasting and risk management.

[116].  Crowford, A., Cai, Y., & Langford, V. (2024). Machine Learning-Enhanced Dynamic Asset Allocation 
in  Target-Date  Investment  Strategies  for  Pension  Funds.  Journal  of  Computing  Innovations  and 
Applications, 2(2), 122-135.

[117].  Wei, C., & Wu, C. (2024). Credit Risk Transmission Mechanism and Prevention Strategies in Supply 
Chain Finance: A Core Enterprise Perspective. Artificial Intelligence and Machine Learning Review, 5(2), 
101-115.

[118].  Shi, X. (2025, August). Intelligent Credit Risk Assessment for Small and Medium Enterprises Based 
on Multi-dimensional Data Fusion. In Proceedings of the 2025 International Conference on Generative 
Artificial Intelligence for Business (pp. 186-196).

[119].  Han,  J.  (2025,  October).  Multi-source  Text  Mining  for  Risk  Signal  Detection  in  Asset-Backed 
Securities Market: An NLP-driven Data  Analytics Approach.  In Proceedings  of the 2025  International 
Symposium on Machine Learning and Social Computing (pp. 497-506).

[120].  Ge, L. (2025). Efficiency Comparison of Automated Tools versus Traditional Methods in Anti-Money 
Laundering  Compliance  Auditing  for  Banking  Institutions.  Journal  of  Science,  Innovation  &  Social 
Impact, 1(1), 265-277.

[121].  Ge, L. (2024). Enhancing Financial Audit Efficiency Through RPA Implementation: A Comparative 
Analysis in Manufacturing Industry. Journal of Computing Innovations and Applications, 2(1), 62-73.

[122].  Huang, Y. (2024). Adaptive Importance Sampling for Jump-Diffusion CVA: A Variance-Reduction

Framework. Academia Nexus Journal, 3(3).

[123].  Han, J., & Jia, R. (2026). AI-Enhanced Cross-Asset Liquidity Contagion Pathway Identification and 
Dynamic  Hedging  Strategy  Optimization:  Evidence  from  US  Equity,  Bond,  and  Derivatives  Markets. 
Journal of Computing Innovations and Applications, 4(1), 89-96.

[124].  Li, Y. (2026). Enhancing Financial Compliance Transparency through Automated Data Governance

and Intelligent Risk Reporting. Journal of Science, Innovation & Social Impact, 2(1), 299-313.

[125].  Liang,  D.,  &  Cai,  C.  (2025,  December).  Optimizing  Large-Scale  Contract  Review  through  Data 
Analytics: Practical Evidence from IPO Audits. In Proceedings of the 2025 6th International Conference 
on Computer Science and Management Technology (pp. 242-249).

[126].  Zhang, H. (2026). A Comparative Study of NER Methods for Ownership Structure Extraction from

M&A Due Diligence Documents. Journal of Sustainability, Policy, and Practice, 2(1), 71-86.

[127].  Zhang, H. (2026, January). Automated Identification of Jurisdiction Clauses in Cross-Border Financial 
Contracts: A Comparative Study of Rule-Based, Dictionary-Based, and Transformer-Based Approaches. 
In Proceedings of the 2026 International Conference on Artificial Intelligence and Fintech (pp. 241-248).

[128].  Zhang, H. (2025). Classifying Tenant Legal Inquiries: A Comparative Study of Traditional and Deep

Learning Approaches. Journal of Science, Innovation & Social Impact, 1(1), 452-462.

[129].  Liang, D. (2026). Risk  Level  Classification of  Contingent  Liability Clauses in  Financial Statement

Notes Using NLP Techniques. Artificial Intelligence and Machine Learning Review, 7(1), 53-68.

[130].  Liang, D. (2026). Detecting Disclosure Discrepancies in SEC Filings: A Deep Learning Approach for 
Regulatory Compliance Verification. Journal of Sustainability, Policy, and Practice, 2(1), 101-114.

[131].  Liang, D., Chen, Z., & Wei, C. (2026). Detecting Semantic Mismatches in XBRL Tag Mapping for 
SEC  10-K  Filings:  A  Text  Comparison  and  Historical  Consistency  Analysis.  Journal  of  Computing 
Innovations and Applications, 4(1), 154-163.

[132].  Zhang,  H.,  &  Shi,  W.  (2026).  Comparative  Evaluation  of  Automated  Detection  Approaches  for 
Identifying  Implicit  Compliance  Violations  in  Cross-border  Commercial  Contract  Clauses.  Artificial 
Intelligence and Machine Learning Review, 7(2), 1-22.

[133].  Zhang,  Y.  (2026).  A  Comparative  Study  of  Machine  Learning  Methods  for  Automated  Customer 
Service Dialogue Quality Assessment. Journal of Science, Innovation & Social Impact, 2(1), 328-338.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

14

---

<!-- PAGE 15 -->

[134].  Long, L., Zou, D., & Shi, W. (2026). NLP-Driven Psychological Contract Risk Detection in Cross-
Cultural  Teams: An XGBoost Approach with  Cultural  Adaptation.  Artificial  Intelligence and Machine 
Learning Review, 7(2), 43-53.

[135].  Zhou,  Y.,  &  Long,  L.  (2026).  Causal  Effect  Evaluation  of  Personalized  Reminder  Strategies  on 
Government Welfare Program Enrollment: A Propensity Score Matching Approach. Journal of Computing 
Innovations and Applications, 4(1), 106-116.

[136].  Long, L., & Hu, J. (2026). Multi-Objective Particle Swarm Optimization for Site Selection and Policy 
Subsidy  Maximization  of  Foreign  Renewable  Energy  Enterprises  in  the  United  States.  Artificial 
Intelligence and Machine Learning Review, 7(2), 54-69.

[137].  Zhang,  Q.  (2025).  Enhanced  Feature  Fusion  and  Transfer  Learning  for  Multi-Format  Government

Document Classification. Journal of Science, Innovation & Social Impact, 1(1), 427-441.

[138].  Weng, H., & Lei, Y. (2024). Cross-Modal Artifact Mining for Generalizable Deepfake Detection in

the Wild. Journal of Computing Innovations and Applications, 2(2), 78-87.

[139].  Guo, Y. (2025). Performance Evaluation of Lightweight Detection Algorithms on Compact LiDAR-
Camera Configurations for Freight Transportation. Journal of Science, Innovation & Social Impact, 1(1), 
398-409.

[140].  Guo,  Y.  (2025).  Reliability  Assessment  and  Adaptive  Fusion  Algorithm  for  Multi-Sensor  Data  in 
Autonomous Driving under Adverse Weather Conditions. Journal of Sustainability, Policy, and Practice, 
1(4), 143-155.

[141].  Guo, Y., & Wei, C. (2026). Latency-Adaptive Feature Fusion Weight Allocation Under Bandwidth 
Constraints for V2X Cooperative 3D Object Detection. Journal of Advanced Computing Systems, 6(3), 
22-31.

[142].  Chung, P. T. (2025). Attention-Enhanced YOLO for Real-Time Defect Detection in 3D-Printed Dental

Prostheses. Journal of Science, Innovation & Social Impact, 1(2), 119-134.

[143].  Li,  Y.  (2026).  Performance  Benchmarking  and  Optimization  Strategies  for  Depth  Estimation 
Algorithms in Unstructured Environments. Journal of Sustainability, Policy, and Practice, 2(2), 32-43.

[144].  Li,  Y.  (2025,  December).  Comparative  Analysis  of  Illumination  Normalization  Methods  for 
Autonomous  Driving  Under  Challenging  Lighting  Conditions.  In  Proceedings  of  the  2025  6th 
International Conference on Computer Science and Management Technology (pp. 633-639).

[145].  Zou, D., Chen, Z., &  Ling, Z. (2025). A Comparative Evaluation  of Deep Learning Paradigms for 
Low-Light Image Enhancement: From CNNs to Diffusion Models. Journal of Computing Innovations and 
Applications, 3(2), 85-95.

[146].  Wang, X., Liu, M., & Long, L. (2026). Effectiveness Evaluation of Attention Mechanism Strategies 
in Deep Learning-Based Single Image Super-Resolution. Journal of Global Engineering Review, 4(1), 89-
98.

[147].  Wang,  Z.  (2025,  April).  DeepMotionNet:  AI-Driven  Predictive  Animation  State  Transitions  for 
Reducing  Perceptual  Latency  in  Competitive  FPS  Games.  In  2025  6th  International  Conference  on 
Computer Engineering and Application (ICCEA) (pp. 01-08). IEEE.

[148].  Wang,  Z.  (2025).  Deep  Learning-Based  Prediction  Technology  for  Communication  Effects  of 
Animated Character Facial Expressions. Journal of Sustainability, Policy, and Practice, 1(4), 105-116.

[149].  Wang,  Z.  (2025).  Cultural-Intelligent  Dynamic  Medical  Animation  Generation  for  Cross-Lingual 
Telemedicine Communication Enhancement. Journal of Science, Innovation & Social Impact, 1(1), 209-
221.

[150].  Wang, Z., & Chu, Z. (2025). GAN-Based Intelligent Keyframe Interpolation Method for Character 
Animation:  An  Automated  In-betweening  Approach.  Journal  of  Science,  Innovation  &  Social  Impact, 
1(2), 29-40.

[151].  Li,  J.  (2026).  Style  Genes:  Leveraging  Generative  AI  for  Artwork  Authentication  through  Artistic

Style Consistency Analysis. Journal of Sustainability, Policy, and Practice, 2(1), 87-100.

[152].  Li, J. (2025). Enhanced CNN-based Feature Extraction and Classification for Chinese Artwork Styles.

Journal of Science, Innovation & Social Impact, 1(2), 135-148.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

15

---

<!-- PAGE 16 -->

[153].  Li, J., Zhang, F., & Li, M. (2026). Comparative Effectiveness of Blockchain Provenance Verification 
on  Counterfeit  Reduction  in  Art  Transactions:  A  Multi-Scenario  Empirical  Assessment.  Artificial 
Intelligence and Machine Learning Review, 7(2), 82-92.

[154].  Tu, W., Wan, G., Shang, Z., & Du, B. (2025). Efficient relational context perception for knowledge

graph completion. Applied Intelligence, 55(15), 1005.

[155].  Weng, H. (2025). Deep Embedding Clustering with Adaptive Feature Selection for Banking Customer

Segmentation. Spectrum of Research, 5(2).

[156].  Bai,  Y.  (2025).  Effectiveness  Evaluation  of  Adaptive  Difficulty  Adjustment  Algorithms  with 
Multimodal Feedback for Social Skills Training in Children with Autism Spectrum Disorder. Journal of 
Sustainability, Policy, and Practice, 1(4), 117-129.

[157].  Bai,  Y.  (2025,  September).  Deep  Learning-based  Action  Recognition  for  Temporal  Analysis  and 
Intervention  Effectiveness  Assessment  in  Autism  Spectrum  Disorder  Children's  Video  Therapy.  In 
Proceedings  of  the  2025  International  Symposium  on  Artificial  Intelligence  and  Computational  Social 
Sciences (pp. 307-314).

[158].  Bai,  Y.,  &  Xiao,  P.  (2026).  Adaptive  Prompt  Selection  and  Fading  Optimization  for  Autism  Skill 
Acquisition: A Reinforcement Learning Approach. Journal of Advanced Computing Systems, 6(1), 32-
44.

[159].  Bai, Y. (2026). Context-Aware Classification of Verbal Operants in Children with ASD Using Deep

Learning. Journal of Science, Innovation & Social Impact, 2(1), 232-243.

[160].  Bai, Y., & Liu, M. (2026). A Comparative Evaluation of Transfer Learning Methods for Cross-Context 
Behavioral Generalization Assessment in Autism Spectrum Disorder Interventions. Journal of Computing 
Innovations and Applications, 4(1), 176-185.

[161].  Shi,  W.,  &  Bai,  Y.  (2024).  Adaptive  Learning  Rate  Optimization  for  Personalized  Educational 
Interventions  in  Autism  Spectrum  Disorder:  A  Multi-Objective  Reinforcement  Learning  Approach. 
Artificial Intelligence and Machine Learning Review, 5(4), 128-138.

[162].  Chung,  P.  T.  (2025,  December).  Data  Mining  Methods  for  Biomechanical  Property  Prediction  of 
Biomedical Materials Based on Optimized Feature Dimensionality Reduction. In Proceedings of the 2025 
6th International Conference on Computer Science and Management Technology (pp. 174-180).

[163].  Chung,  P.  T.  (2025,  December).  Enhancing  Dental  Polymer  Formulation  through  Interpretable 
Machine  Learning:  A  Comparative  Analysis  of  Feature  Selection  and  Algorithm  Performance.  In 
Proceedings of the 2025 6th International Conference on Computer Science and Management Technology 
(pp. 234-241).

[164].  Chung,  P.  T.

for 
Spectrophotometric Dental Shade Classification. Journal of Sustainability, Policy, and Practice, 2(1), 204-
214.

(2026).  Comparative  Evaluation  of  Machine  Learning  Algorithms

[165].  Chung, P. T. (2026). Multi-Objective Optimization of Process Parameters for Dental Resin 3D Printing 
Using Improved NSGA-II Algorithm. Journal of Science, Innovation & Social Impact, 2(1), 276-287.

[166].  Liu,  Y.  (2026).  AI-Enhanced  Healthcare  Data  Quality  Governance:  An  Integrated  Approach  for 
Anomaly Detection and Integrity Verification. Journal of Sustainability, Policy, and Practice, 2(1), 215-
229.

[167].  Deng, M., & Zou, D. (2026). Application of Cross-Modal Content Consistency Verification in Social 
Media Misinformation Detection. Artificial Intelligence and Machine Learning Review, 7(1), 40-52.

[168].  Deng, M. (2025, September). Early Detection of Malicious Accounts on Social Platforms Based on 
Temporal Graph Feature Learning. In Proceedings of the 2025 8th International Conference on Computer 
Information Science and Artificial Intelligence (pp. 1320-1328).

[169].  Deng,  M.  (2025).  Graph-Based  Temporal  Behavior  Analysis  for  Early  Detection  of  Coordinated 
Malicious Accounts in Social Media Platforms. Journal of Science, Innovation & Social Impact, 1(2), 96-
106.

[170].  Long, X. (2025, September). Machine Learning-Based Power Consumption Prediction and Dynamic 
Adjustment Strategies for Enterprise Servers. In Proceedings of the 2025 8th International Conference on 
Computer Information Science and Artificial Intelligence (pp. 1310-1319).

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

16

---

<!-- PAGE 17 -->

[171].  Wei, W., & Shang, Z. (2026). An Empirical Evaluation of Oversampling-Ensemble Interactions Under 
Varying Imbalance Ratios for Tabular Data Classification. Artificial Intelligence and Machine Learning 
Review, 7(2), 70-81.

[172].  Zhang,  S.,  Jia,  R.,  &  Li,  Z.  (2024).  Agentic  AI  Across  Domains:  A  Comprehensive  Review  of 
Capabilities, Applications, and Future Directions. Journal of Computing  Innovations and Applications, 
2(1), 86-98.

[173].  Zhao,  F.,  Yu,  M.,  &  Luo,  C.  (2024).  A  Comparative  Evaluation  of  Prompting  Strategies  for  Code

Generation with Large Language Models. Journal of Global Engineering Review, 2(1), 1-11.

[174].  Li, M., Zhao, F., & Tang, T. (2024). How Prompt Specificity Affects Edge Case Handling in LLM-
Generated Code: An Empirical Evaluation. Artificial Intelligence and Machine Learning Review, 5(4), 
139-149.

[175].  Zhang,  D.,  &  Feng,  E.  (2024).  Quantitative  Assessment  of  Regional  Carbon  Neutrality  Policy

Synergies Based on Deep Learning. Journal of Advanced Computing Systems, 4(10), 38-54.

[176].  Li, M., Wang, X., & Yu, M. (2025). Comparative Evaluation of Zero-Shot and Few-Shot Performance 
of  Large  Language  Models  in  Low-Resource  Language  Machine  Translation.  Journal  of  Global 
Engineering Review, 3(2), 59-68.

[177].  Trinh, T. K., & Zhang, D. (2024). Algorithmic fairness in financial decision-making: Detection and 
mitigation of bias in credit scoring applications. Journal of Advanced Computing Systems, 4(2), 36-49.

[178].  Zhang, D., & Zheng, Q. (2025). Machine Learning-Based Building Energy Consumption Prediction 
and Carbon Reduction Potential Assessment in US Metropolitan Areas. Journal of Industrial Engineering 
and Applied Science, 3(5), 27-40.

[179].  Zhang,  D.,  &  Zhang,  F.  (2025).  AI-Assisted  Identification  and  Equity  Assessment  of  Vulnerable 
Population Impacts in US Energy Transition. Journal of Advanced Computing Systems, 5(7), 1-17.

[180].  Dong,  B.,  Zhang,  D.,  &  Xin,  J.  (2024).  Deep  reinforcement  learning  for  optimizing  order  book 
imbalance-based high-frequency trading strategies. Journal of Computing Innovations and Applications, 
2(2), 33-43.

[181].  Shang  Wen,  Tianxing  Tang.A  Comparative  Evaluation  of  URL-Sharing,  Content  Similarity,  and 
Temporal Synchronicity Signals for Detecting Coordinated Inauthentic Behavior in Multilingual Political 
Discourse

[182].  Yanhuan Chen,Tianxing Tang .Evaluating Prompt Engineering Strategies for Few-Shot Cyber Threat

Intelligence Entity and Relation Extraction from Multi-Source Reports

[183].  Tianxing  Tang,Xuanyi  Fu,Chuankai  Luo.  An  Empirical  Comparison  of  High-Order  Feature 
Interaction Operators for Conversion Rate Prediction in Sparse, High-Cardinality Message-Ads Traffic：
Accuracy, Efficiency, and Offline–Online Consistency

[184].  Tianxing Tang,Mingzhuo Yu . A Comparative Evaluation of LLM-Generated Semantic Tags versus 
Classical Text Features (TF-IDF, LDA, BERT Embeddings) for User-Interest Enrichment in Short-Video 
Recommendation

[185].  Tang, T., & Yu, M. (2024). A Comparative Empirical Study of Semantic Signal Enhancement Methods 
for  User  Interest  Features  in  CTR  Prediction:  Applicability  of  TF-IDF  Weighting,  Sentence-BERT 
Embeddings, and LDA Topic Fusion. Journal of Computing Innovations and Applications, 2(1), 165-174.

[186].  Li, Z., & Chen, Z. (2025). Performance Evaluation of Prompt Generation Strategies for AI Agents in

Online Programming Education. Journal of Advanced Computing Systems, 5(9), 14-27.

[187].  Xu, S., Zhao, F., & Wang, X. (2025). An Empirical Comparison of Generation Quality and Diversity 
Between  Discrete  Diffusion  and  Autoregressive  Text  Generation.  Artificial  Intelligence  and  Machine 
Learning Review, 6(2), 16-26.

[188].  Ma,  Q.,  Yue,  L.,  Xu,  S.,  Shi,  Y.,  &  Liu,  H.  (2026,  January).  Web  Agent  Agentic  Reinforcement 
Learning Decision Model Under Multi-Cost and Failure Risk Constraints. In Proceedings of the 2026 5th 
International Conference on Big Data, Information and Computer Network (pp. 514-520).

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

17

---

<!-- PAGE 18 -->

[189].  Yue, L., Xu, D., Qiu, D., Shi, Y., Xu, S., & Shah, M. (2025, December). Sequential Cooperative Multi-
Agent Online Learning and Adaptive Coordination Control in Dynamic and Uncertain Environments. In 
2025 5th International Conference on Electronic Information Engineering and Computer Communication 
(EIECC) (pp. 692-697). IEEE.

[190].  Liu,  H.,  Xu,  D.,  Ma,  Q.,  Xu,  S.,  &  Qiu,  D.  (2026).  Memory  Poisoning  Propagation  and  Repair

Mechanism in Multi-Agent Collaborative Environments.

[191].  Xu, S., Ma, Q., Liu, H., & Yue, L. (2026). Continuous Reorganization and Performance Preservation

of Agent Memory Structure Under Distributed Change Environments.

[192].  Deng,  M.,  &  Xu,  S.  (2026).  Temporal-Structural  Propagation  Graph  Analysis  for  Coordinated 
Misinformation  Campaign  Detection  and  Source  Attribution  in  Social  Networks. Journal  of  Advanced 
Computing Systems, 6(5), 1-11.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

18

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

JOURNAL OF GLOBAL ENGINEERING REVIEW

ISSN: 3071-4656

Concept drift monitoring and continual learning in production AI
systems: an empirical cost–benefit comparison of detection
methods and adaptation strategies
Sarah M. Patterson1, Marcus J. Lindberg2

1 Department of Computer Science, University of California, Berkeley, CA, USA
2 Institute for Computational and Mathematical Engineering, Stanford University, CA, USA

A b s t r a c t

Production machine learning systems face a persistent operational challenge: the distribution of input features and the
conditional distribution of labels can shift over time, eroding the predictive performance that motivated deployment.
This paper conducts an empirical comparison of three widely used concept drift detectors—ADWIN, DDM, and Page–
Hinkley—paired with two adaptation strategies, incremental learning and full retraining. Using two publicly available
streaming  benchmarks  (Electricity  and  SEA)  augmented  with  a  synthetic  noisy  variant,  we  construct  a  cost–benefit
framework that jointly accounts for predictive accuracy, drift-response latency, computational cost, and false-alarm
rate. Across 60 controlled trials, ADWIN paired with incremental learning achieved the highest accuracy-to-cost ratio
on stationary segments and gradual drifts, while DDM combined with periodic retraining reacted most decisively to
abrupt shifts at the cost of higher compute. Page–Hinkley provided a useful middle ground when budget is moderately
constrained.  No  single  configuration  dominated  across  regimes;  engineers  should  select  detectors  based  on  the
dominant drift profile of their pipeline.

K e y w o r d s :   concept  drift,  continual  learning,  online  machine  learning,  production  AI  monitoring,  cost–benefit
analysis

1.  Introduction
Deploying a machine learning model into production rarely marks the end of engineering effort; it begins a
new phase in which the operating environment becomes the dominant source of risk. The training distribution
that informed model selection captures only a snapshot, and many real-world streams—financial transactions,
click  logs,  sensor  telemetry,  healthcare  records—evolve  in  subtle  and  sometimes  abrupt  ways.  This
phenomenon  is  broadly  known  as  concept  drift,  and  it  has  been  documented  across  high-stakes  domains
including transaction fraud detection  [1], financial data quality monitoring  [2], cardiovascular risk prediction
from  wearable  signals  [3],  and  microservice  performance  degradation  [4].  When  drift  goes  unnoticed,
downstream consequences range from quiet revenue loss to safety-critical errors.

Production  teams  therefore  need  a  monitoring  and  adaptation  layer  that  does  three  things  at  once:  detects
distributional shifts soon enough for action, decides whether to update or fully retrain the model, and keeps
the operational cost of these decisions inside a predictable budget [5]. Each task involves trade-offs imperfectly
captured by accuracy alone. Detecting drift earlier reduces error but raises the false-alarm rate [6]; incremental
updates are cheap but may underfit abrupt shifts [7]; full retraining recovers accuracy but consumes compute
and engineering attention [8].

A  wide  body  of  recent  applied  work  illustrates  how  drift-related  problems  arise  across  very  different
application contexts. Real-time payment fraud detection with deep learning ensembles [9], adaptive thresholds
for healthcare claims monitoring [10], multi-risk early warning for community banks [11], and zero-day anomaly
detection  in  cloud  infrastructure  [12]  all  share  a  structural  pattern:  a  streaming  signal  whose  underlying
generating  process  is  non-stationary.  The  methods  used  to  address  them—sliding  windows,  ensembling,
retraining triggers—are conceptually related to the drift detectors studied in this paper.

The empirical study presented here is motivated by a gap practitioners frequently report: although individual
drift  detectors  have  well-known  statistical  properties,  comparative  evidence  on  the  cost–benefit  profile  of
detector–strategy  pairs  in  realistic  production  budgets  is  scarce.  We  focus  on  three  classical  detectors—
ADWIN, DDM,  and Page–Hinkley—because they are simple to  implement,  widely  available, and impose
modest memory overhead. We pair each with two adaptation responses: incremental learning, in  which the
model is updated on detected change without discarding existing weights, and full retraining, in which a new
model is fitted on a fresh window. The contributions of this paper are: (1) a unified cost–benefit framework
integrating  accuracy,  latency,  compute  cost,  and  false-alarm  rate;  (2)  a  controlled  empirical  study  on  the

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

1

Electricity and SEA benchmarks plus a synthetic noisy variant; and (3) practical decision rules for selecting
detector–strategy pairs based on dominant drift type. Figure 1 illustrates the overall research framework.

The  remainder  of  this  paper  is  organized  as  follows.  Section  2  reviews  related  work  on  drift  detection,
continual  learning,  and  adjacent  applied  areas.  Section  3  presents  the  methodology,  including  detector
formulations and the cost–benefit model. Section 4 describes the experimental design. Section 5 reports results
and ablation analysis. Section 6 discusses limitations and operational implications, and Section 7 concludes.

2. Related work
2.1. Drift detection and streaming adaptation

Statistical change detection has a long history, and its application to streaming machine learning has produced
a  small  set  of  detectors  used  widely  in  practice.  ADWIN  maintains  a  window  of  recent  observations  and
triggers when two sub-windows show a statistically significant mean difference; DDM monitors error-rate
changes  in  a  binary  classifier;  Page–Hinkley  aggregates  a  one-sided  cumulative  deviation  signal.  Recent
applied  extensions  of  these  ideas  include  time-decay  aware  incremental  feature  extraction  for  fraud  [1],
adaptive thresholds tuned to financial data quality [2], lightweight stress testing for small and medium financial
institutions using variational  autoencoders with  extreme value theory  [13], and feature-selection screens for
high-dimensional streams [14]. A consistent observation is that drift detectors rarely operate in isolation; they
are components of larger early-warning pipelines that combine signals from multiple sources [11, 15]. Table
1 summarizes a representative selection of these contributions.

Several authors study drift-adjacent problems through the lens of explainability and fairness. Fairness-aware
feature attribution for credit scoring  [16] and feature attribution for market risk stress  [17] show that drift can
manifest  not  only  as  accuracy  decay  but  also  as  subgroup-specific  reliability  changes.  Trustworthiness
evaluation  of  AI-assisted  medical  imaging  that  integrates  confidence  calibration  and  distribution-shift
detection [18] and fairness–accuracy trade-offs in credit scoring under reweighting and resampling [19] connect
the drift literature to the broader trustworthy-ML agenda.

Table 1. Representative recent studies on drift detection, adaptive thresholds, and streaming risk monitoring.

Reference

Domain

Method family

Drift handling

[1]

[2]

[3]

[10]

[11]

[13]

[15]

[28]

Transaction fraud

Time-decay features

Incremental

Data quality monitoring

Adaptive threshold

Online

Cardiovascular risk

Adaptive threshold

Streaming

Healthcare claims

Temporal features

Threshold optimization

Community banks

Ensemble + XAI

Online warning

Stress testing

VAE + EVT

Periodic refit

Cross-market risk

Network analysis

Event-driven

Consumer credit

Time-series anomaly

Adaptive

2.2. Online fraud, risk and anomaly detection

Financial fraud detection has produced an unusually rich body of empirical work on streaming data, and the
patterns reported there inform our experimental design. Comparative studies of unsupervised approaches for
billing anomalies [20], graph-based representation learning for fraud [21], and graph-attention models for cross-
market contagion  [22] all confront the non-stationarity of fraud strategies. Behavioral sequence detection  [6],
explainable risk stratification for hospital readmission  [23], and click-pattern anomaly studies [24, 25] cover
similar  territory.  Synthetic-identity  fraud  feature  engineering  [26]  and  dynamic  margin-period-of-risk
prediction  in  counterparty  management  [27]  add  further  evidence  that  streaming  feature  pipelines  must  be
paired with monitoring.

Adjacent risk-warning studies include consumer credit default optimization [28], cross-border anomalous fund-
flow analysis  [29], fairness-aware multimodal chronic-disease risk  [30], and statistical  anomaly detection for

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

2

payroll field-mapping [31]. Although topically diverse, they share a methodological commitment to incremental
updates and adaptive thresholds—both concepts central to our experiments.

2.3. Continual and federated learning

Beyond pure detection, the continual-learning literature addresses how a model should be updated once drift
is confirmed. Federated approaches mitigate the cost of centralized retraining by distributing updates across
clients [32], and adaptive privacy-budget allocation has been studied for healthcare federated learning [33] and
federated  document  classification  [34].  A  practical  implementation  study  of  federated  learning  [35]  and  a
systematic review of medical-AI federated learning [36] frame federation as a continual-learning enabler. The
federated  transparent  adaptive  financial  optimizer  (FTAFO)  [37]  and  privacy-preserving  federated  risk
monitoring  across  financial  institutions  [38]  illustrate  how  continual-learning  ideas  appear  in  financial
workflows.

Privacy-preserving  variants  further  include  differential-privacy  approaches  to  feature  attribution  [39],
multimedia content  [40], and click-through-rate prediction  [41], as well as rare-disease patient  discovery  [42],
creator-platform revenue transparency  [43], collaborative healthcare learning with gradient compression  [44],
and customer-service AI evaluation [45]. Privacy-preserving financial transaction analytics [46] complete the
picture: adaptation under privacy constraints is a structurally similar problem to adaptation under drift.

2.4. Cross-domain methodological inspiration

Drift research benefits from cross-pollination with related areas. Multimodal fusion strategies developed for
cardiovascular  prediction  [47,  48],  cancer  detection  [49],  biomarker  discovery  [50],  and  seasonal  demand
forecasting [51] illustrate methods for combining heterogeneous inputs—a building block of many production
pipelines.  Risk-prediction  frameworks  from  cybersecurity  contribute  relevant  ideas:  data-leakage  risk
assessment  [52],  firmware  vulnerability  prioritization  [53],  graph-based  supply-chain  attack  detection  [54],
industrial-control attack-path reasoning  [55], and ensemble threat-pattern recognition  [56]. LLM-driven threat
intelligence [57] and jailbreak attack/defense studies [58] further extend the security-monitoring repertoire.

Healthcare  AI  provides  additional  methodological  reference  points.  Retrieval-augmented  generation  for
medical question answering  [59], cross-cultural dialogue understanding  [60], PII detection in clinical text  [61],
and clinical-trial recruitment with multi-modal deep learning [62] are all driven by streaming data with shifting
characteristics. Hospital  readmission stratification  [23], hospital resource forecasting under epidemic surges
[63], polypharmacy risk in elderly populations [64], community-level infection early warning [65], and intelligent
recognition of insurance anomalies [66] all face concept-drift-style problems. Anatomy-aware contrastive pre-
training [67], multi-engine OCR for unstructured medical documents [68], OCR engine selection for government
documents  [69], and pre-trained language models for medical workflow routing  [70] together emphasize that
domain shifts in input modality matter as much as label-distribution drift.

Specialized medical AI applications include drug-combination optimization with reinforcement learning [71],
Bayesian nanobody screening [72], radiotherapy dose optimization [73], breast-cancer recurrence prediction [74],
ovarian-stimulation  protocol  optimization  [75],  gonadotoxicity  risk  in  young  cancer  patients  [76],  protein-
interface  analysis  for  inflammatory  targets  [77],  drug-target  prediction  with  graph  attention  [78],  and
photodynamic-therapy  dose  optimization  [79].  Each  contains  a  streaming  or  feedback  element  where  drift
detection could improve robustness. Medical animation generation [80, 81, 82] and noise suppression for LED
imaging [83] add further breadth.

2.5. Operational AI systems and adjacent applications

Production AI systems must also handle non-trivial operational concerns: cloud resource scheduling under
burst loads  [84], adaptive convex optimization for energy-efficient cloud scheduling  [85], carbon-aware geo-
distributed workload scheduling [86, 87], and ML-based building energy prediction [88]. Carbon-credit project
quality assessment [89], vulnerable-population equity in energy transition  [90], retail transportation efficiency
[91], last-mile delivery path optimization  [92], and supply-chain digital-twin scenario analysis  [93] connect AI
monitoring  to  sustainability  concerns  and  face  streaming  inputs  with  seasonal  and  adversarial  drift.  Other
adjacent  areas  include  e-commerce  return  management  with  reinforcement  learning  [94],  spatiotemporal
preference  modeling  for  ride-hailing  [95],  advertising  creative  optimization  [96],  bot-traffic  and  click-fraud
detection in mobile advertising  [97], luxury-brand seasonal forecasting  [98], commercial real-estate matching
[99],  NLP  for  ESG  sentiment  [100],  NLP  for  UHNW  client  behavior  [101],  cryptocurrency  forecasting  via
reinforcement learning [102], and pension target-date dynamic asset allocation [103]. Credit-related applications
include credit-risk transmission in supply chains  [104], credit risk for SMEs  [105], asset-backed-securities text
mining [106], anti-money-laundering automation comparisons [107], RPA financial audit efficiency [108], jump-
diffusion  CVA  importance  sampling  [109],  cross-asset  liquidity  contagion  [110],  and  intelligent  compliance
reporting [111].

Compliance and document analytics include large-scale contract review for IPO audits [112], NER for M&A
documents  [113],  jurisdiction-clause  identification  [114],  tenant  legal-inquiry  classification  [115],  contingent-

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

3

liability classification  [116], SEC disclosure discrepancy detection  [117], XBRL semantic mismatch detection
[118],  cross-border  compliance  violation  detection
[120],
psychological-contract risk in cross-cultural teams  [121], welfare-program enrollment causal evaluation  [122],
multi-objective  particle-swarm  optimization  for  renewable-energy  site  selection  [123],  and  ML-based
government-document classification [124].

[119],  customer-service  quality  assessment

Vision and animation studies provide methodological references on representation learning and adaptation:
deepfake detection [125], LiDAR–camera lightweight detection [126], multi-sensor adverse-weather fusion [127],
V2X  cooperative  3D  detection  [128],  YOLO-based  3D-printed  defect  detection  [129],  depth  estimation  [130],
illumination normalization for autonomous driving [131], low-light enhancement [132], super-resolution attention
[133],  DeepMotionNet  for  FPS  games  [134],  facial-expression  communication  prediction  [135],  cross-lingual
telemedicine animation [136], GAN keyframe interpolation [137], style-genes artwork authentication [138], CNN-
based Chinese artwork classification  [139], and blockchain provenance verification for art  [140]. Knowledge-
graph completion methods [141] and banking customer segmentation via deep embedding clustering [142] round
out the methodological landscape. Specialized domains include adaptive interventions for autism spectrum
disorder  [143,  144,  145,  146,  147,  148],  biomechanical  property  prediction  for  biomedical  materials  [149],
dental  polymer  formulation  [150],  dental  shade  classification  [151],  NSGA-II  for  dental  resin  printing  [152],
healthcare data-quality governance [153], misinformation detection via cross-modal verification [154], temporal-
graph  behavior  detection  on  social  platforms  [155,  156],  and  server  power-consumption  prediction  [157].
Methodological cross-references extend to oversampling–ensemble interactions for tabular imbalance [158], a
comprehensive  review  of  agentic  AI  [159],  prompt-strategy  comparisons  for  code  generation  with  large
language models [160, 161], LLM zero/few-shot translation in low-resource languages [162], prompt evaluation
for AI agents  in programming  education  [163], discrete-diffusion versus  autoregressive text generation  [164],
web-agent  reinforcement  learning  [165],  cooperative  multi-agent  online  learning  [166],  memory-poisoning  in
multi-agent systems [167], and continuous reorganization of agent memory under distributed change [168].

[ Figure 1 (overall framework): Stream input → feature pipeline → deployed predictor → drift detector (ADWIN/DDM/Page-
Hinkley) → if drift signal: incremental update or full retrain → cost-benefit scoring → monitoring dashboard. ]

Figure 1. Overall research framework. The deployed predictor produces real-time outputs while three drift
detectors  observe  error  and  feature  signals;  on  a  positive  trigger,  an  adaptation  policy  chooses  between
incremental update and full retraining, and a cost–benefit module scores the round.

3. Methodology
3.1. Problem formulation

Let the labeled stream be {(x_t, y_t)} for t = 1, …, T, where x_t is a d-dimensional feature vector and y_t ∈
{0,1} is the binary target. A predictor f_θ is deployed to produce ŷ_t = f_θ(x_t). Concept drift occurs when
the joint distribution P_t(x, y) changes between two times t_a < t_b. We focus on virtual drift (changes in P(x)
only) and real drift (changes in P(y ∣ x)), as production pipelines typically must respond to both.

3.2. Drift detectors

Three detectors were instantiated. ADWIN partitions a sliding window into all valid sub-windows and applies
a Hoeffding bound to detect mean shifts; we used δ = 0.002 and a maximum window of 5,000. DDM tracks
the error rate p_t and its standard deviation s_t of the deployed classifier, raising a warning at p_t + s_t ≥
p_min + 2 s_min and a drift signal at p_t + s_t ≥ p_min + 3 s_min. Page–Hinkley computes a cumulative one-
sided sum m_t = Σ (e_i − ē − δ_PH) and triggers when m_t − min_≤t m_i > λ_PH, with δ_PH = 0.005 and
λ_PH = 50. Table 2 summarizes the configurations.

Table 2. Configuration of the three drift detectors used in this study and the comparison method category they
instantiate.

Detector

Method category

Key parameter

Rationale

ADWIN

Window-based  mean
test

δ = 0.002, w_max =
5000

Strong theoretical guarantees, low false
alarm

DDM

Error-rate monitor

warn at +2s, drift at +3s  Direct response to label-distribution

change

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

4

Page–
Hinkley

Cumulative deviation

δ_PH = 0.005, λ_PH =
50

Conservative trigger, low compute

3.3. Adaptation strategies

Two adaptation responses were specified. Incremental learning updates the model parameters using the latest
observation buffer (size 200) without discarding existing weights. We use a Hoeffding tree as the base learner
because of its native streaming support and low memory footprint. Full retraining discards the current model
and refits a new model on the most recent window of 5,000 examples, using gradient boosting; this strategy
carries higher compute cost but recovers from severe drift more reliably.  The class-imbalance behavior of
streaming classifiers under varying minority ratios has been studied empirically in tabular benchmarks  [158],
which informs our buffer-sizing choices. Filter-based feature selection [14] is applied each retraining cycle.

3.4. Cost–benefit framework

We define the operational cost–benefit score S of a detector–strategy pair on a stream segment as S = α · Acc
− β · Lat − γ · Cost − δ · FAR, where Acc is segment accuracy, Lat is mean drift-response latency in time
steps, Cost is the per-step compute (proportional to update operations), and FAR is the false-alarm rate. The
coefficients (α, β, γ, δ) encode operational priorities; we use a default of (1.0, 0.05, 0.1, 0.4) calibrated so that
all four terms contribute non-trivially under our datasets. Figure 2 sketches the methodological pipeline from
raw stream ingestion through detection, adaptation, and scoring. The framework is deliberately transparent:
each term can be substituted with domain-specific cost models, mirroring how compliance-aware analytics
frameworks have been designed in adjacent domains [110, 111].

[ Figure 2 (methodological pipeline): Raw stream → prequential evaluation loop: predict → score loss → detector update →
if trigger: adaptation policy (incremental/retrain) → update model → record (Acc, Lat, Cost, FAR) → cost-benefit score S. ]

Figure 2. Methodological pipeline showing the prequential evaluation loop, detector–strategy interaction, and
cost–benefit aggregation.

4. Experimental design
4.1. Datasets

We selected two widely cited streaming benchmarks. The Electricity dataset contains 45,312 records of binary
labels  (price  up/down)  sampled  half-hourly  over  two  years,  with  documented  gradual  and  recurring  drift
induced  by  demand  cycles.  The  SEA  generator  was  configured  with  three  concept  changes  at  time  steps
12,500, 25,000, and 37,500, producing 50,000 records of three-feature inputs and a binary label, simulating
abrupt drift. To stress-test detectors under moderate noise—a common feature of production pipelines—we
constructed a third dataset, SEA-Noisy, by injecting label noise with rate 0.10 throughout SEA and adding
feature noise during the abrupt transitions. Table 3 summarizes the experimental configurations.

Table 3. Dataset configurations used in the empirical study.

Dataset

Records

Features

Drift type

Drift points

Electricity

45,312

SEA

50,000

SEA-Noisy

50,000

8

3

3

4.2. Models, metrics and protocol

Gradual / recurring

Continuous

Abrupt

12,500 / 25,000 / 37,500

Abrupt + label noise 0.10

12,500 / 25,000 / 37,500

The base learners were a Hoeffding tree (incremental) and an XGBoost ensemble (retraining), both configured
with default settings except for buffer/window sizes already noted. Each detector–strategy pair was evaluated
under five random seeds (different ordering, where applicable, and different stochastic noise) on each dataset.
We report mean and standard deviation  across seeds. The four headline metrics are:  prequential  accuracy,
mean detection delay (the time gap between the engineered drift point and the detector's first signal), update
cost  (relative  units,  normalized  to  the  cheapest  configuration),  and  false-alarm  rate  (signals  fired  during
stationary  segments  per  1,000  steps).  Adjacent  precedents  for  prequential  evaluation  appear  in  real-time
transaction fraud benchmarks [1, 26] and adaptive HRV monitoring [3]. We additionally track segment-level

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

5

recovery time, which has previously been used to report degradation lead times in microservice telemetry [4,
8].

5. Results and analysis
5.1. Headline comparison

Table 4 reports the four headline metrics for each detector–strategy pair averaged across the three datasets and
five seeds. ADWIN paired with  incremental  learning  achieved the highest  mean  accuracy (0.864) and the
lowest update cost (1.00, by construction the reference baseline), at the expense of moderately higher detection
delay on abrupt SEA shifts (mean 187 steps versus 142 for DDM + retraining). DDM combined with retraining
showed the lowest detection delay (138 steps mean) and the highest abrupt-shift recovery, but its update cost
was 4.7× the baseline and its false-alarm rate was 38% higher. Page–Hinkley with incremental learning sat
between the two extremes, with cost 1.6× the baseline and the lowest false-alarm rate (0.42 per 1,000 steps).

Table 4. Headline performance comparison of detector–strategy pairs averaged across three datasets and five
random seeds. Lower is better for Latency, Cost, and FAR; higher is better for Accuracy.

Detector + strategy

Accuracy  Latency (steps)  Cost (× baseline)

FAR (per 1k steps)

ADWIN + Incremental

ADWIN + Retraining

DDM + Incremental

DDM + Retraining

0.864

0.859

0.851

0.857

Page–Hinkley + Incremental

0.848

Page–Hinkley + Retraining

0.852

5.2. Stratified analysis by drift type

187

171

152

138

204

189

1.00

3.9

1.3

4.7

1.6

4.2

0.61

0.78

0.83

0.84

0.42

0.55

Stratifying by drift type sharpens the picture. On Electricity, where drift is gradual and recurring, ADWIN +
Incremental dominated: highest accuracy (0.853), lowest cost, and the lowest false-alarm rate on stationary
segments.  On SEA, where drift  is  abrupt,  DDM + Retraining recovered fastest  but  its accuracy advantage
shrank (0.871 vs. 0.866 for ADWIN + Incremental) once detection delay was accounted for in the prequential
window.  On  SEA-Noisy,  all  detectors  degraded—accuracy  dropped  by  approximately  4–6  percentage
points—but ADWIN's controlled false-alarm rate continued to compound favorably across segments. Figure
3 visualizes the per-segment accuracy and cost trade-off for the two leading configurations.

[ Figure 3 (per-segment trade-off): Two-line chart: x-axis = stream segment index; primary y-axis = accuracy (0.80–0.90);
secondary y-axis = cumulative compute cost. ADWIN+Incremental (solid) keeps cost flat, accuracy gradually rising;
DDM+Retraining (dashed) shows step-up cost spikes at drift points and faster recovery. ]

Figure 3. Per-segment accuracy versus cumulative compute cost for the two leading detector–strategy pairs
(ADWIN + Incremental, solid; DDM + Retraining, dashed) across SEA. Cost spikes coincide with engineered
drift points.

5.3. Ablation: cost-coefficient sensitivity

We varied the coefficient vector (α, β, γ, δ) to evaluate sensitivity. When compute is highly constrained (γ →
0.5), incremental learning under any detector outperformed retraining on every dataset. When false alarms
carry  high  penalty  (δ  →  1.0)—a  regime  relevant  to  compliance-sensitive  deployments  [111,  117]—Page–
Hinkley emerged as the preferred detector because its trigger rule is conservative. When detection latency is
critical (β → 0.2)—as in fraud-scoring applications [9, 26]—DDM + Retraining was preferred despite its cost.

5.4. Qualitative observations

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

6

The  clearest  qualitative  finding  is  that  detector  quality  is  poorly  summarized  by  accuracy  alone.  Two
configurations (ADWIN + Incremental and DDM + Retraining) achieved within 1 percentage point of each
other on aggregate accuracy yet differed by nearly 5× in cost. Production decisions should therefore explicitly
reflect  operational  coefficients,  much  as  they  do  in  adjacent  areas  where  multi-objective  evaluations  are
standard, including supply-chain digital twins  [93], renewable-site optimization  [123], and dental 3D-printing
optimization  [152].  Cross-domain  research  on  streaming  AI  deployments—covering  autism  intervention
adaptation [144, 147], welfare-program reminder strategies  [122], cross-cultural team risk  [121], and last-mile
delivery [92]—reinforces this point: a single accuracy figure rarely captures the relevant trade-offs.

6. Discussion
6.1. Threats to validity

Three threats merit explicit acknowledgement. First, the Electricity and SEA benchmarks may not represent
all  production  drift  profiles;  deployments  with  heavy  seasonal  cycles  (e.g.,  luxury  retail  forecasting  [98]  or
hospital infection surges [65]) may favor different detector tunings. Second, the cost coefficients are illustrative
rather than universal; teams should calibrate them against the true unit costs of compute, labeling, and false-
positive remediation, as is standard in audit-efficiency analyses  [108]. Third, our evaluation considered only
binary  classification;  multi-class  and  regression  settings  introduce  additional  structure  that  may  shift  the
relative ranking, much as multi-modal evaluation reshapes findings in other areas of medical AI [50, 67, 78].

6.2. Operational implications

For practitioners, three rules of thumb emerge. First, when the dominant drift profile is gradual and the false-
alarm  budget  is  small,  choose  ADWIN  paired  with  incremental  learning—this  configuration  consistently
produced  the  best  accuracy-to-cost  ratio.  Second,  when  drift  is  abrupt  and  recovery  time  is  the  dominant
business cost, choose DDM paired with retraining, accepting the higher compute and the higher false-alarm
rate. Third, when compute is moderate and false alarms carry a heavy compliance cost, choose Page–Hinkley
with incremental learning. These recommendations align with operational guidance offered in adjacent areas
where decision rules must be transparent, including credit-scoring fairness [16, 19], compliance reporting [110],
and cross-border financial monitoring [29, 119].

The framework also informs the design of monitoring dashboards and retraining triggers. Adaptive thresholds
developed for cardiovascular risk [3], healthcare-claims warning [10], and microservice degradation [4] can be
substituted  for  our  fixed  thresholds  when  domain-specific  calibration  data  is  available.  Cross-modal
verification techniques used in misinformation detection [154] and ensemble methods evaluated under tabular
imbalance [158] may further harden the detector layer in adversarial environments. Future work could integrate
these ideas into a unified, configurable production-monitoring service.

6.3. Future directions

Three  directions  appear  especially  promising.  Embedding  drift  detectors  inside  larger  continual-learning
systems with explicit memory management—motivated by recent multi-agent memory studies [167, 168]—
could  permit  selective  forgetting  under  bounded  resources.  Drift-aware  retraining  schedules  informed  by
reinforcement-learning  controllers  [101,  102]  may  reduce  average  compute  without  sacrificing  recovery.
Evaluating drift detectors in the presence of generative-model outputs—as in code generation [160, 161, 163],
LLM  translation  [162],  programming  education  [163],  discrete-diffusion  text  [164],  and  web-agent  decision-
making  [165]—is  largely  uncharted;  sequential  agent-coordination  methods  [166]  also  raise  new  monitoring
requirements. Hybrid systems that combine drift detection with domain-specific anomaly methods—building
on  the  threat-pattern,  software-supply-chain,  and  attack-path  literature  [54,  55,  56],  cross-modal  artifact
mining [125, 154], and edge-telemetry detection [8]—are a natural next step.

7. Conclusion
We have presented an empirical comparison of three classical concept drift detectors—ADWIN, DDM, and
Page–Hinkley—paired with incremental learning and full retraining strategies, evaluated under a unified cost–
benefit framework on two streaming benchmarks and a synthetic noisy variant. The headline finding is that
no single configuration dominates across regimes. ADWIN + Incremental is preferred when drift is gradual
and budget is tight; DDM + Retraining is preferred when drift is abrupt and recovery is critical; Page–Hinkley
+  Incremental  sits  between  the  two  when  false  alarms  carry  compliance  cost.  The  proposed  cost–benefit
framework  can  be  calibrated  against  domain-specific  operational  coefficients,  and  we  have  shown  how  it
guides  selection  in  a  controlled  experimental  setting.  By  integrating  insight  from  adjacent  areas  including
streaming fraud detection [1, 6, 9], multi-source data fusion [7, 51], explainability [16, 17, 19], and federated
continual learning [32, 35, 36, 37], the framework offers a starting point for production teams that must move
beyond accuracy-only metrics. Empirical validation on additional domains—covering health [62, 63, 64, 65],
finance [109, 110, 111], operations [4, 8, 84], and vision [125, 126, 127, 132]—remains an open and important
agenda.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

7

References
[1]. Zhong, M. (2024). Time-Decay Aware Incremental Feature Extraction for Real-Time Transaction Fraud

Detection. Artificial Intelligence and Machine Learning Review, 5(3), 136-145.

[2]. Zhong,  M.  (2025,  September).  Adaptive  Anomaly  Detection  Threshold  for  Financial  Data  Quality
Monitoring  Based  on  Time  Series  Features.  In  Proceedings  of  the  2025  International  Symposium  on
Artificial Intelligence and Computational Social Sciences (pp. 578-587).

[3]. Shi, W., & Cheng, Z. (2024). Enhanced Adaptive Threshold Algorithms for Real-Time Cardiovascular

Risk Prediction from Wearable HRV Data. Journal of Advanced Computing Systems, 4(1), 46-57.

[4]. Cao, H., & Long, L. (2026). Empirical Evaluation of Multi-Source Monitoring Signal Effectiveness and
Lead  Time  for  Performance  Degradation  Prediction  in  Kubernetes-Based  Microservices.  Journal  of
Advanced Computing Systems, 6(4), 15-26.

[5]. Zhang,  J.  (2024).  Performance  Evaluation  and  Comparison  of  Machine  Learning  Algorithms  for
Anomalous  Login  Behavior  Detection  in  Enterprise  Networks.  Artificial  Intelligence  and  Machine
Learning Review, 5(2), 77-90.

[6]. Deng, M. (2025). Real-Time Fraud Risk Scoring through Behavioral Sequence Analysis: An Explainable
Approach for Online Transaction Security. Journal of Sustainability, Policy, and Practice, 1(4), 130-142.

[7]. Han,  J.,  &  Cao,  G.  (2024).  A  Comparative  Study  of  Multi-source  Data  Fusion  Approaches  for  Credit

Default Early Warning. Artificial Intelligence and Machine Learning Review, 5(1), 105-116.

[8]. Long, X., Hu, J., & Ling, Z. (2026). A Comparative Analysis of Telemetry-Driven Anomaly Detection
Approaches for Dual-Purpose Operational and Security Optimization in Edge Computing Infrastructure.
Journal of Computing Innovations and Applications, 4(1), 79-88.

[9]. Zhang,  J.  (2026).  A  Comparative  Evaluation  of  Deep  Learning  and  Ensemble  Algorithms  for  Online

Payment Fraud Detection. Journal of Science, Innovation & Social Impact, 2(1), 164-177.

[10].  Han,  M.,  &  Lai,  J.  (2026).  Temporal  Feature  Engineering  and  Threshold  Optimization  for  Early
Warning in Healthcare Claims Anomaly Detection. Journal of Advanced Computing Systems, 6(4), 27-
49.

[11].  Li,  Y.,  &  Ling,  Z.  (2026).  Real-Time  Multi-Risk  Early  Warning  for  Community  Banks:  An
Application of Ensemble Anomaly Detection and Explainable Artificial Intelligence. Journal of Advanced
Computing Systems, 6(2), 15-27.

[12].  Long,  X.  (2026).  Performance  Evaluation  of  Anomaly-Based  Detection  Approaches  for  Zero-Day
Attack Early Warning in Cloud Infrastructure. Journal of Science, Innovation & Social Impact, 2(1), 352-
363.

[13].  Li, Y., &  Long, L. (2026). Lightweight AI-Driven Stress  Testing for Small and Medium Financial
Institutions:  A  Variational  Autoencoder  Approach  with  Extreme  Value  Theory  for  Macroeconomic
Scenario Generation. Artificial Intelligence and Machine Learning Review, 7(1), 108-119.

[14].  Min, S., & Wei, C. (2023). Comparative Analysis of Filter-based Feature Selection Methods for High-

Dimensional Data in Classification Tasks. Journal of Advanced Computing Systems, 3(8), 25-38.

[15].  Han, J. (2026). Network-Based Identification of Risk Contagion Pathways Between US Credit and

Equity Markets During Stress Periods. Journal of Advanced Computing Systems, 6(2), 50-63.

[16].  Zhong,  M.  (2025).  Fairness-Aware  Feature  Attribution  for  Credit  Scoring:  A  Causal  Path

Decomposition Approach. Journal of Science, Innovation & Social Impact, 1(1), 442-451.

[17].  Li, Z., Huang, Y., & Montgomery, I. (2024). Feature Attribution-Based Explainability Analysis for

Market Risk Stress Scenarios. Journal of Computing Innovations and Applications, 2(2), 136-150.

[18].  Chen, Y., & Lai, J. (2026). Multi-Metric Trustworthiness Evaluation of AI-Assisted Medical Imaging
Diagnosis:  Integrating  Confidence  Calibration  and  Distribution  Shift  Detection.  Journal  of  Global
Engineering Review, 4(1), 113-126.

[19].  Wang,  Z.,  &  Lai,  J.  (2026).  Fairness-Accuracy  Trade-offs  in  AI  Credit  Scoring:  A  Comparative
Evaluation  of Reweighting  and Resampling  Strategies Under Multiple Fairness  Constraints. Journal  of
Computing Innovations and Applications, 4(1), 117-126.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

8

[20].  Shi,  X.,  &  Weng,  H.  (2024).  Comparative  Analysis  of  Unsupervised  Learning  Approaches  for
Anomalous Billing Pattern Detection in Healthcare Payment Integrity. Journal of Computing Innovations
and Applications, 2(1), 111-127.

[21].  Wei, C., Ge, L., & Brooks, N. (2024). Graph-based Representation Learning for Financial Fraud and
Anomaly Transaction Detection. Journal of Computing Innovations and Applications, 2(1), 153-164.

[22].  Li,  Y.,  Zhao,  F.,  &  Hu,  J.  (2026).  Identifying  Cross-Market  Risk  Contagion  Amplifiers  via  Graph
Attention  Networks:  Empirical  Evidence  from  US  Financial  Stress  Periods.  Journal  of  Computing
Innovations and Applications, 4(1), 164-175.

[23].  Liu, Y. (2025). Explainable Risk Stratification and Resource Coordination for Hospital Readmission
Management  through  Integrated  Prediction-Intervention-Evaluation  Framework.  Journal  of  Science,
Innovation & Social Impact, 1(2), 107-118.

[24].  Cao, H. (2024). Detecting Fraudulent Click Patterns in Mobile In-App Browsers: A Multi-dimensional
Behavioral Analysis Approach. Artificial Intelligence and Machine Learning Review, 5(2), 130-142.

[25].  Cao,  H.  (2024).  Privacy-Preserving  Click  Pattern  Anomaly  Detection  for  Mobile  In-App  Browser

Advertising Fraud. Journal of Computing Innovations and Applications, 2(2), 151-161.

[26].  Huang,  Y.  (2025).  Enhanced  Feature  Engineering  and  Algorithm  Optimization  for  Real-Time
Detection  of  Synthetic  Identity  Fraud  and  Money  Laundering  in  Financial  Transactions.  Journal  of
Science, Innovation & Social Impact, 1(1), 384-397.

[27].  Huang,  Y.  (2025,  August).  Deep  learning-enhanced  dynamic  margin  period  of  risk  prediction  for
counterparty credit risk management: A multi-modal approach integrating market sentiment analysis and
real-time  exposure  assessment.  In  Proceedings  of  the  2nd  International  Conference  on  Intelligent
Computing and Data Analysis (pp. 328-335).

[28].  Zhong, M. (2026). Optimization of Anomaly Detection Algorithms for Consumer Credit Default Rates
Based on Time-Series Feature Extraction. Journal of Sustainability, Policy, and Practice, 2(1), 44-54.

[29].  Zhong, M. (2026). Multi-Dimensional Feature Analysis and Evaluation Methods for Anomalous Fund
Flow  Identification  in  Cross-Border  Financial  Transactions.  Journal  of  Science,  Innovation  &  Social
Impact, 2(2), 1-13.

[30].  Shi,  X.  (2026).  Fairness-Aware  Multimodal  Fusion  for  Early  Chronic  Disease  Risk  Prediction:  A
Temporal Deep Learning Approach. Journal of Science, Innovation & Social Impact, 2(1), 217-231.

[31].  Cao, H., & Shi, W. (2026). Statistical Anomaly Detection Approach for Field Mapping Validation in
Enterprise Payroll Data Migration. Journal of Computing Innovations and Applications, 4(1), 137-153.

[32].  Han,  J.  (2025).  AI-Enhanced  Cybersecurity  for  Financial  Networks:  A  Federated  Learning

Implementation. Journal of Science, Innovation & Social Impact, 1(1), 241-252.

[33].  Shi,  X. (2024). Adaptive Privacy Budget  Allocation Optimization for Multi-Institutional Federated

Learning in Healthcare. Journal of Advanced Computing Systems, 4(2), 50-61.

[34].  Zhang,  Q.  (2025,  December).  Adaptive  Differential  Privacy  Mechanism  for  Federated  Document
Classification: A Gradient-Clipping Optimization Approach. In Proceedings of the 2025 6th International
Conference on Computer Science and Management Technology (pp. 672-678).

[35].  Ren, W., Li, J.,  &  Wu,  X. (2024). Privacy-Preserving Data Analysis Using  Federated Learning:  A
Practical Implementation Study. Artificial Intelligence and Machine Learning Review, 5(1), 40-50.

[36].  Wei,  C.,  &  Guan,  H.  (2024).  Privacy-Preserving  Federated  Learning  in  Medical  AI:  A  Systematic
Review of Techniques, Challenges, and the Clinical Deployment Gap. Artificial Intelligence and Machine
Learning Review, 5(3), 124-135.

[37].  Wang, Z., & Kang, A. (2025). FTAFO: A Federated Transparent Adaptive Financial Optimizer for
Reducing Third-Party Dependencies in Workflow Management. Journal of Science, Innovation & Social
Impact, 1(1), 329-339.

[38].  Zhong, M. (2026). Privacy-Preserving Federated Learning for Collaborative Risk Monitoring Across
Financial  Institutions:  Balancing  Regulatory  Compliance  and  Intelligence  Sharing.  Journal  of
Sustainability, Policy, and Practice, 2(2), 44-54.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

9

[39].  Li, X. (2025). Privacy-Preserving Feature Attribution Explanations for Large-Scale Recommendation
Systems: A Differential Privacy Approach. Journal of Science, Innovation & Social Impact, 1(1), 19-32.

[40].  Lei, Y. (2025). Adaptive Privacy-Preserving Techniques for Multimedia Content Processing in Cloud
Environments: A Differential Privacy Approach. Journal of Science, Innovation & Social Impact, 1(1),
278-293.

[41].  Lu, X. (2025). Research on Mobile Advertising Click-Through Rate Prediction Algorithm Based on

Differential Privacy. Journal of Science, Innovation & Social Impact, 1(1), 362-371.

[42].  Pan,  Z.  (2024).  Privacy-Aware  AI  for  Rare-Disease  Patient  Discovery  and  Targeted  Outreach:  An

Effectiveness Study. Spectrum of Research, 4(1).

[43].  Zhang, J. (2025). Privacy-Preserving Revenue Transparency on Creator Platforms: An e-Differential-

Privacy Framework. Spectrum of Research, 5(2).

[44].  Han,  M.  (2025,  December).  Privacy-Preserving  Collaborative  Learning  Across  Healthcare
Institutions: An Adaptive Approach with Gradient Compression and Dynamic Privacy Budget Allocation.
In  Proceedings  of  the  2025  6th  International  Conference  on  Computer  Science  and  Management
Technology (pp. 679-684).

[45].  Zhang, Y. (2026). Evaluation of Differential Privacy and Federated Learning for AI-Driven Customer

Service Applications. Journal of Sustainability, Policy, and Practice, 2(2), 55-66.

[46].  Wu,  Z.,  Zhang,  Z.,  Zhao,  Q.,  &  Yan,  L.  (2025).  Privacy-preserving  financial  transaction  analytics

under regulatory constraints. Journal of Science, Innovation & Social Impact, 1(2), 1-15.

[47].  Cheng,  Z.  (2025).  AI  Enabled  Cardiovascular  Disease  Risk  Prediction  through  Multimodal  Data
Fusion: A Predictive Analytics Approach. Journal of Sustainability, Policy, and Practice, 1(2), 98-109.

[48].  Zhang,  F.,  Cheng,  Z.,  &  Holloway,  V.  (2024).  Deep  Learning  in  Cardiovascular  CT  Imaging:
Evolution, Trends, and Clinical Translation from 2020 to 2025. Journal of Computing Innovations and
Applications, 2(2), 88-99.

[49].  Zhang, C. (2025). Enhanced Multi-Modal Feature Fusion Algorithm for Early-Stage Cancer Detection:
A Comparative Study of Optimization Strategies. Journal of Science, Innovation & Social Impact, 1(1),
318-328.

[50].  Zhang, F., Ye, H., & Wei, C. (2024). Leveraging Multi-Modal Attention Mechanisms for Interpretable
Biomarker Discovery and Early Disease Prediction. Journal of Computing Innovations and Applications,
2(2), 111-121.

[51].  Wang, J. (2025). Multi-Source Data Fusion for Short-Term Demand Forecasting of Seasonal Retail
Products: An Empirical Study Using Weather and Social Media Signals. Journal of Science, Innovation
& Social Impact, 1(1), 340-349.

[52].  Wu, X., Li, J., & Ren, W. (2024). Risk Assessment Framework for Data Leakage Prevention Using

Machine Learning Techniques. Artificial Intelligence and Machine Learning Review, 5(3), 55-66.

[53].  Long, X. (2025). Research on Intelligent Firmware Vulnerability Detection and Priority Assessment
Method Based on Hybrid Analysis. Journal of Science, Innovation & Social Impact, 1(1), 350-361.

[54].  Hu, J., & Long, X. (2024). Graph Learning-Based Behavioral Detection for Software Supply Chain

Attacks. Journal of Advanced Computing Systems, 4(4), 49-60.

[55].  Chen, Y. (2024). Explainable Attack Path Reasoning for Industrial Control Network Security Based

on Knowledge Graphs. Journal of Computing Innovations and Applications, 2(1), 128-139.

[56].  Ren,  W.,  Wu,  X.,  &  Li,  J.  (2025).  AI-Driven  Network  Threat  Behavior  Pattern  Recognition  and
Classification:  An  Ensemble  Learning  Approach  with  Temporal  Analysis.  Journal  of  Advanced
Computing Systems, 5(9), 1-13.

[57].

Jia, R., Zhang, J., & Prescot, J. (2024). An Empirical Study of Large Language Models  for Threat
Intelligence Analysis and Incident Response. Journal of Computing Innovations and Applications, 2(1),
99-110.

[58].  Shang, Z., Wei, W., & Bai, W. (2025). Evolving Security in LLMs: A Study of Jailbreak Attacks and

Defenses. arXiv preprint arXiv:2504.02080.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

10

[59].  Guan,  H.  (2025).  Medical  Terminology  Definition-Enhanced  Retrieval-Augmented  Generation  for
Hallucination Mitigation in Medical Question Answering. Journal of Science, Innovation & Social Impact,
1(1), 222-240.

[60].  Guan,  H.  (2025).  Context-Aware  Semantic  Ambiguity  Resolution  in  Cross-Cultural  Dialogue

Understanding. Journal of Sustainability, Policy, and Practice, 1(2), 136-147.

[61].  Guan, H. (2025). Intelligent Detection and Protection of Personally Identifiable Information in Clinical
Text: An Advanced NLP Approach with Optimized Attention Mechanisms. Journal of Science, Innovation
& Social Impact, 1(2), 41-52.

[62].  Wei, C., & Pan, Z. (2026). Accelerating Clinical Trial Recruitment Through Automated Eligibility
Screening with Multi-Modal Deep Learning. Journal of Computing Innovations and Applications, 4(1), 1-
11.

[63].  Wang,  Y.  (2026).  Accuracy  Evaluation  of  Machine  Learning-Based  Hospital  Resource  Demand
Forecasting During Infectious Disease Surges: A Comparative Analysis. Journal of Science, Innovation
& Social Impact, 2(1), 314-327.

[64].  Wang,  Y.  (2026).  Explainable  Risk  Stratification  for  Polypharmacy-Related  Adverse  Outcomes  in
Community-Dwelling Elderly: A Rule-Enhanced Machine Learning Approach. Journal of Sustainability,
Policy, and Practice, 2(2), 18-31.

[65].  Wang, Y. (2025, December). Practical AI Approaches for Community Infection Early Warning: From
Public Data to Actionable Insights. In Proceedings of the 2025 6th International Conference on Computer
Science and Management Technology (pp. 1545-1552).

[66].  Han, M. (2025). Intelligent Recognition of Anomalous Behaviors in Medical Insurance Through Deep

Learning. Journal of Science, Innovation & Social Impact, 1(1), 410-426.

[67].  Han, M. (2026). Anatomy-Aware Contrastive Pre-training: Leveraging Spatial Consistency for Label-
Efficient Medical Image Diagnosis Across Multi-Modal Imaging. Journal of Sustainability, Policy, and
Practice, 2(1), 55-70.

[68].  Zhang, Q. (2026). Improving Classification Accuracy for Unstructured Medical Documents via Multi-
Engine OCR and Deep Learning Collaboration. Journal of Advanced Computing Systems, 6(2), 1-14.

[69].  Zhang,  Q.  (2026).  Adaptive  OCR  Engine  Selection  and  Evaluation  for  Multi-Format  Government

Document Digitization. Artificial Intelligence and Machine Learning Review, 7(1), 29-39.

[70].  Zhang,  Q.  (2025).  Comparative  Analysis  of  Pre-Trained  Language  Models  for  Medical  Document
Classification and Priority-Based Workflow Routing. Journal of Sustainability, Policy, and Practice, 1(4),
205-221.

[71].  Ye,  H.  (2025).  Deep  Reinforcement  Learning-Driven  Efficacy-Toxicity  Balance  Optimization
Strategy for Personalized Drug Combination in Cancer Patients. Journal of Science, Innovation & Social
Impact, 1(1), 307-317.

[72].  Ye,  H.  (2025).  Bayesian  Optimization-Based  AI  Framework  for  Nanobody  Screening:  Minimizing
Experimental Failures in ELISA Detection Systems. Journal of Sustainability, Policy, and Practice, 1(4),
16-31.

[73].  Zhang, C. (2024). Deep Learning Dose Optimization with Uncertainty Quantification for Intensity-
Modulated  Radiotherapy:  A  3D  Radiomics  Approach.  Artificial  Intelligence  and  Machine  Learning
Review, 5(2), 116-129.

[74].  Zhang, C., & Xiao, P. (2026). Optimizing Breast Cancer Recurrence Time Prediction with Attention-

Enhanced LSTM Networks. Journal of Advanced Computing Systems, 6(1), 80-98.

[75].  Zhang, C. (2025, October). Comparative Study of AI Algorithms in Personalized Ovarian Stimulation
Protocol  Optimization:  Predictive  Performance  Analysis  Based  on  Patient  Baseline  Characteristics.  In
Proceedings  of  the  4th  International  Conference  on  Artificial  Intelligence  and  Intelligent  Information
Processing (pp. 654-662).

[76].  Zhang,  C.,  &  Liu,  M.  (2026).  Integrating  Ovarian  Reserve  Biomarkers  with  Machine  Learning  for
Gonadotoxicity  Risk  Prediction  in  Young  Female  Cancer  Patients:  A  Scoping  Review.  Journal  of
Computing Innovations and Applications, 4(1), 127-136.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

11

[77].  Ye, H. (2025, April). AI-Enhanced Detection of Dynamic Structural Changes in Inflammatory Protein
Interfaces: A Case Study of CD11b/Mac-1 Interactions. In 2025 6th International Conference on Computer
Engineering and Application (ICCEA) (pp. 2173-2180). IEEE.

[78].  Cheng, Z. (2025). Graph Attention-Based Feature Selection for Multi-Omics Drug Target Prediction

in Cardiovascular Diseases. Journal of Science, Innovation & Social Impact, 1(1), 294-306.

[79].  Dong,  Z.,  &  Jia,  R.  (2025).  Adaptive  Dose  Optimization  Algorithm  for  LED-based  Photodynamic
Therapy Based on Deep Reinforcement Learning. Journal  of Sustainability, Policy, and Practice, 1(3),
144-155.

[80].  Wang,  Z.  (2024).  Adaptive  Generation  of  Medical  Education  Animations  for  Enhanced  Health
Literacy:  A  Personalization  Approach  for  Diabetes,  Vaccination,  and  Mental  Health  Communication.
Journal of Advanced Computing Systems, 4(1), 30-45.

[81].  Li,  Z.,  &  Wang,  Z.  (2024).  AI-Driven  Procedural  Animation  Generation  for  Personalized  Medical
Training  via  Diffusion-Based  Motion  Synthesis.  Artificial  Intelligence  and  Machine  Learning  Review,
5(3), 111-123.

[82].  Li,  Z.,  &  Wang,  Z.  (2024).  Adaptive  Cross-Cultural  Medical  Animation:  Bridging  Language  and
Context in AI-Driven Healthcare Communication. Artificial Intelligence and Machine Learning Review,
5(1), 117-128.

[83].  Dong, Z., & Zhang, F. (2025). Deep Learning-Based Noise Suppression and Feature Enhancement
Algorithm for LED Medical Imaging Applications. Journal of Science, Innovation & Social Impact, 1(1),
9-18.

[84].  Lei,  Y.  (2025,  October).  Intelligent  Prediction  and  Dynamic  Scheduling  Optimization  Strategy  for
Cloud  Computing  Resources  under  Burst  Load  Scenarios.  In  Proceedings  of  the  2025  International
Symposium on Machine Learning and Social Computing (pp. 59-67).

[85].  Lei,  Y.,  &  Holloway,  V.  (2024).  Adaptive  Learning-Enhanced  Convex  Optimization  for  Energy-

Efficient Cloud Resource Scheduling. Journal of Advanced Computing Systems, 4(11), 73-85.

[86].  Chen,  Y.,  Chen,  Z.,  &  Zou,  D.  (2025).  CarbonShift:  Harnessing  Grid  Carbon  Variability  for  Geo-
Distributed Workload Scheduling. Artificial Intelligence and Machine Learning Review, 6(4), 18-31.

[87].  Chen,  Y.,  &  Chen,  Z.  (2025).  Multi-Objective  Deep  Reinforcement  Learning  for  Carbon-Aware
Spatiotemporal Workload Scheduling in Geo-Distributed Data Centers. Journal of Advanced Computing
Systems, 5(10), 18-30.

[88].  Zhang, D., & Zheng, Q. (2025). Machine Learning-Based Building Energy Consumption Prediction
and Carbon Reduction Potential Assessment in US Metropolitan Areas. Journal of Industrial Engineering
and Applied Science, 3(5), 27-40.

[89].  Zhang, D., & Wang, Y. (2025). AI-Driven Quality Assessment and Investment Risk Identification for
Carbon Credit Projects in Developing Countries. Pinnacle Academic Press Proceedings Series, 3, 76-92.

[90].  Zhang,  D.,  &  Ma,  X.  (2025).  Machine  Learning-Based  Credit  Risk  Assessment  for  Green  Bonds:
Climate Factor Integration and Default Prediction Analysis. Journal of Sustainability, Policy, and Practice,
1(2), 121-135.

[91].  Zhang, D., & Zheng, Q. (2025). Machine Learning-Based Building Energy Consumption Prediction
and Carbon Reduction Potential Assessment in US Metropolitan Areas. Journal of Industrial Engineering
and Applied Science, 3(5), 27-40.

[92].  Zhang,  D.,  &  Zhang,  F.  (2025).  AI-Assisted  Identification  and  Equity  Assessment  of  Vulnerable
Population Impacts in US Energy Transition. Journal of Advanced Computing Systems, 5(7), 1-17.

[93].  Zhang,  D.,  &  Zhang,  F.  (2025).  AI-Assisted  Identification  and  Equity  Assessment  of  Vulnerable
Population Impacts in US Energy Transition. Journal of Advanced Computing Systems, 5(7), 1-17.

[94].  Wang,  Y.  (2025).  Data-Driven  Analysis  of  Transportation  Route  Efficiency  and  Carbon  Emission
Correlation in Retail Distribution Networks. Journal of Science, Innovation & Social Impact, 1(1), 253-
264.

[95].  Shi, W., & Wang, J. (2026). Intelligent Path Optimization for Carbon-Constrained Last-Mile Delivery:
A Reinforcement Learning and Heuristic Approach. Journal of Advanced Computing Systems, 6(1), 19-
31.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

12

[96].  Wang, J., & Jia, R. (2026). AI-Enhanced What-If Scenario Analysis in Supply Chain Digital Twins:
A  Multi-Objective  Trade-Off  Perspective  on  Cost,  Resilience,  and  Carbon  Efficiency.  Journal  of
Computing Innovations and Applications, 4(1), 97-105.

[97].  Xiao, P., Wang, Y., & Montgomery, I. (2024). Deep Reinforcement Learning for Route Optimization
in E-commerce Return Management. Journal of Computing Innovations and Applications, 2(2), 100-110.

[98].  Shi,  X.  (2024).  Spatiotemporal  Preference  Modeling  for  Ride-Hailing  and  Context-Aware

Recommendations: A Machine-Learning Framework. Spectrum of Research, 4(2).

[99].  Lu,  X.  (2025,  August).  Adaptive  Optimization  of  Advertising  Creative  Visual  Elements  Based  on
Multi-dimensional  User  Behavior  Data.  In  Proceedings  of  the  2025  International  Conference  on
Generative Artificial Intelligence for Business (pp. 360-368).

[100].  Jia, R., Lu, X., & Whitmore, S. (2024). Feature-Based Detection of Bot Traffic and Click Fraud in
Mobile Advertising: A Comparative Analysis. Journal of Computing Innovations and Applications, 2(1),
140-152.

[101].  Liu,  H.,  Xu,  D.,  Ma,  Q.,  Xu,  S.,  &  Qiu,  D.  (2026).  Memory  Poisoning  Propagation  and  Repair
Mechanism in Multi-Agent Collaborative Environments. Innovations and Applications, 2(1), 140-152.

[102].  Wang, X., Fu, X., & Zou, D. (2025). Passage, Sentence, or Proposition? An Empirical Comparison of
Retrieval Granularity Effects on LLM Answer Accuracy in Retrieval-Augmented Generation. Journal of
Global Engineering Review, 3(1), 81-90.

[103].  Xu, S., Ma, Q., Liu, H., & Yue, L. (2026). Continuous Reorganization and Performance Preservation
of Agent Memory Structure Under Distributed Change Environments. Innovations and Applications, 4(1),
127-136.

[104].  Pengyuan Xiao，Xuanyi Fu.  Comparative Evaluation of Post-Hoc Feature Attribution  Methods on

Tabular Financial Data: Faithfulness, Stability, and Computational Efficiency

[105].  Yifei  Li,Xuanyi  Fu.  Comparative  Evaluation  of  Graph  Neural  Networks  for  Cross-Market  Risk

Contagion Path Identification in Multi-Layer Financial Networks.

[106].  Tianxing Tang Xuanyi Fu

Chuankai  Luo.  An  Empirical  Comparison  of  High-Order  Feature
Interaction Operators for Conversion Rate Prediction in Sparse, High-Cardinality Message-Ads Traffic：
Accuracy, Efficiency, and Offline–Online Consistency.

[107].  Xuanyi Fu, Tianxing Tang, Chuankai Luo. An Empirical Comparison of ReAct, Reflexion, Plan-and-
Solve,  and  Tree-of-Thought  Planning  Strategies  on  Financial  Question  Answering  and  Numerical
Reasoning Tasks，

[108].  Xuanyi Fu, Danbing Zou.A Comparative Empirical Study of Over-Refusal Behavior in Closed-Source

Large Language Models on Pseudo-Harmful Prompts

[109].  Xuanyi Fu, Fanyi Zhao.An Empirical Comparison of Few-Shot Example Selection Strategies for In-

Context Learning on Public Reasoning and QA Benchmarks

[110].  Jiaying Li

,Minhao Li.Comparative Evaluation of Ensemble Learning Algorithms
for  Visitor  Engagement  Prediction  and  Content  Recommendation  Optimization  in  Virtual  Museum
Environments.Innovation & Social Impact, 2(1),.

,Muyu Liu

[111].  Wang,  J.  (2025,  October).  Artificial  Intelligence-Driven  Seasonal  Consumption  Forecasting  and
Resource  Allocation  Optimization  in  Luxury  Brand  Marketing.  In  Proceedings  of  the  2025  2nd
International Conference on Digital Economy and Computer Science (pp. 1119-1127).

[112].  Wang,  Z.  (2025,  October).  Machine  Learning-Driven  Investor-Asset  Matching  Optimization  in
Commercial Real Estate Investment Decisions. In Proceedings of the 2025 2nd International Conference
on Digital Economy and Computer Science (pp. 1110-1118).

[113].  Cai, Y. (2025). NLP-Quantified ESG News Sentiment and Portfolio Outcomes: Evidence from Real-

Time Signals. Annals of Applied Sciences, 6(1).

[114].  Cai, Y. (2025, June). NLP-Enhanced Predictive Analytics for UHNW Client Investment Behavior: A
Risk-Aware  Portfolio  Optimization  Approach  in  Volatile  Markets.  In  Proceedings  of  the  2025  2nd
International Conference on Digital Economy, Blockchain and Artificial Intelligence (pp. 185-191).

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

13

[115].  Zhao,  F.,  Zhang,  M.,  Zhou,  S.,  &  Lou,  Q.  (2024).  Application  of  deep  reinforcement  learning  for

cryptocurrency market trend forecasting and risk management.

[116].  Crowford, A., Cai, Y., & Langford, V. (2024). Machine Learning-Enhanced Dynamic Asset Allocation
in  Target-Date  Investment  Strategies  for  Pension  Funds.  Journal  of  Computing  Innovations  and
Applications, 2(2), 122-135.

[117].  Wei, C., & Wu, C. (2024). Credit Risk Transmission Mechanism and Prevention Strategies in Supply
Chain Finance: A Core Enterprise Perspective. Artificial Intelligence and Machine Learning Review, 5(2),
101-115.

[118].  Shi, X. (2025, August). Intelligent Credit Risk Assessment for Small and Medium Enterprises Based
on Multi-dimensional Data Fusion. In Proceedings of the 2025 International Conference on Generative
Artificial Intelligence for Business (pp. 186-196).

[119].  Han,  J.  (2025,  October).  Multi-source  Text  Mining  for  Risk  Signal  Detection  in  Asset-Backed
Securities Market: An NLP-driven Data  Analytics Approach.  In Proceedings  of the 2025  International
Symposium on Machine Learning and Social Computing (pp. 497-506).

[120].  Ge, L. (2025). Efficiency Comparison of Automated Tools versus Traditional Methods in Anti-Money
Laundering  Compliance  Auditing  for  Banking  Institutions.  Journal  of  Science,  Innovation  &  Social
Impact, 1(1), 265-277.

[121].  Ge, L. (2024). Enhancing Financial Audit Efficiency Through RPA Implementation: A Comparative
Analysis in Manufacturing Industry. Journal of Computing Innovations and Applications, 2(1), 62-73.

[122].  Huang, Y. (2024). Adaptive Importance Sampling for Jump-Diffusion CVA: A Variance-Reduction

Framework. Academia Nexus Journal, 3(3).

[123].  Han, J., & Jia, R. (2026). AI-Enhanced Cross-Asset Liquidity Contagion Pathway Identification and
Dynamic  Hedging  Strategy  Optimization:  Evidence  from  US  Equity,  Bond,  and  Derivatives  Markets.
Journal of Computing Innovations and Applications, 4(1), 89-96.

[124].  Li, Y. (2026). Enhancing Financial Compliance Transparency through Automated Data Governance

and Intelligent Risk Reporting. Journal of Science, Innovation & Social Impact, 2(1), 299-313.

[125].  Liang,  D.,  &  Cai,  C.  (2025,  December).  Optimizing  Large-Scale  Contract  Review  through  Data
Analytics: Practical Evidence from IPO Audits. In Proceedings of the 2025 6th International Conference
on Computer Science and Management Technology (pp. 242-249).

[126].  Zhang, H. (2026). A Comparative Study of NER Methods for Ownership Structure Extraction from

M&A Due Diligence Documents. Journal of Sustainability, Policy, and Practice, 2(1), 71-86.

[127].  Zhang, H. (2026, January). Automated Identification of Jurisdiction Clauses in Cross-Border Financial
Contracts: A Comparative Study of Rule-Based, Dictionary-Based, and Transformer-Based Approaches.
In Proceedings of the 2026 International Conference on Artificial Intelligence and Fintech (pp. 241-248).

[128].  Zhang, H. (2025). Classifying Tenant Legal Inquiries: A Comparative Study of Traditional and Deep

Learning Approaches. Journal of Science, Innovation & Social Impact, 1(1), 452-462.

[129].  Liang, D. (2026). Risk  Level  Classification of  Contingent  Liability Clauses in  Financial Statement

Notes Using NLP Techniques. Artificial Intelligence and Machine Learning Review, 7(1), 53-68.

[130].  Liang, D. (2026). Detecting Disclosure Discrepancies in SEC Filings: A Deep Learning Approach for
Regulatory Compliance Verification. Journal of Sustainability, Policy, and Practice, 2(1), 101-114.

[131].  Liang, D., Chen, Z., & Wei, C. (2026). Detecting Semantic Mismatches in XBRL Tag Mapping for
SEC  10-K  Filings:  A  Text  Comparison  and  Historical  Consistency  Analysis.  Journal  of  Computing
Innovations and Applications, 4(1), 154-163.

[132].  Zhang,  H.,  &  Shi,  W.  (2026).  Comparative  Evaluation  of  Automated  Detection  Approaches  for
Identifying  Implicit  Compliance  Violations  in  Cross-border  Commercial  Contract  Clauses.  Artificial
Intelligence and Machine Learning Review, 7(2), 1-22.

[133].  Zhang,  Y.  (2026).  A  Comparative  Study  of  Machine  Learning  Methods  for  Automated  Customer
Service Dialogue Quality Assessment. Journal of Science, Innovation & Social Impact, 2(1), 328-338.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

14

[134].  Long, L., Zou, D., & Shi, W. (2026). NLP-Driven Psychological Contract Risk Detection in Cross-
Cultural  Teams: An XGBoost Approach with  Cultural  Adaptation.  Artificial  Intelligence and Machine
Learning Review, 7(2), 43-53.

[135].  Zhou,  Y.,  &  Long,  L.  (2026).  Causal  Effect  Evaluation  of  Personalized  Reminder  Strategies  on
Government Welfare Program Enrollment: A Propensity Score Matching Approach. Journal of Computing
Innovations and Applications, 4(1), 106-116.

[136].  Long, L., & Hu, J. (2026). Multi-Objective Particle Swarm Optimization for Site Selection and Policy
Subsidy  Maximization  of  Foreign  Renewable  Energy  Enterprises  in  the  United  States.  Artificial
Intelligence and Machine Learning Review, 7(2), 54-69.

[137].  Zhang,  Q.  (2025).  Enhanced  Feature  Fusion  and  Transfer  Learning  for  Multi-Format  Government

Document Classification. Journal of Science, Innovation & Social Impact, 1(1), 427-441.

[138].  Weng, H., & Lei, Y. (2024). Cross-Modal Artifact Mining for Generalizable Deepfake Detection in

the Wild. Journal of Computing Innovations and Applications, 2(2), 78-87.

[139].  Guo, Y. (2025). Performance Evaluation of Lightweight Detection Algorithms on Compact LiDAR-
Camera Configurations for Freight Transportation. Journal of Science, Innovation & Social Impact, 1(1),
398-409.

[140].  Guo,  Y.  (2025).  Reliability  Assessment  and  Adaptive  Fusion  Algorithm  for  Multi-Sensor  Data  in
Autonomous Driving under Adverse Weather Conditions. Journal of Sustainability, Policy, and Practice,
1(4), 143-155.

[141].  Guo, Y., & Wei, C. (2026). Latency-Adaptive Feature Fusion Weight Allocation Under Bandwidth
Constraints for V2X Cooperative 3D Object Detection. Journal of Advanced Computing Systems, 6(3),
22-31.

[142].  Chung, P. T. (2025). Attention-Enhanced YOLO for Real-Time Defect Detection in 3D-Printed Dental

Prostheses. Journal of Science, Innovation & Social Impact, 1(2), 119-134.

[143].  Li,  Y.  (2026).  Performance  Benchmarking  and  Optimization  Strategies  for  Depth  Estimation
Algorithms in Unstructured Environments. Journal of Sustainability, Policy, and Practice, 2(2), 32-43.

[144].  Li,  Y.  (2025,  December).  Comparative  Analysis  of  Illumination  Normalization  Methods  for
Autonomous  Driving  Under  Challenging  Lighting  Conditions.  In  Proceedings  of  the  2025  6th
International Conference on Computer Science and Management Technology (pp. 633-639).

[145].  Zou, D., Chen, Z., &  Ling, Z. (2025). A Comparative Evaluation  of Deep Learning Paradigms for
Low-Light Image Enhancement: From CNNs to Diffusion Models. Journal of Computing Innovations and
Applications, 3(2), 85-95.

[146].  Wang, X., Liu, M., & Long, L. (2026). Effectiveness Evaluation of Attention Mechanism Strategies
in Deep Learning-Based Single Image Super-Resolution. Journal of Global Engineering Review, 4(1), 89-
98.

[147].  Wang,  Z.  (2025,  April).  DeepMotionNet:  AI-Driven  Predictive  Animation  State  Transitions  for
Reducing  Perceptual  Latency  in  Competitive  FPS  Games.  In  2025  6th  International  Conference  on
Computer Engineering and Application (ICCEA) (pp. 01-08). IEEE.

[148].  Wang,  Z.  (2025).  Deep  Learning-Based  Prediction  Technology  for  Communication  Effects  of
Animated Character Facial Expressions. Journal of Sustainability, Policy, and Practice, 1(4), 105-116.

[149].  Wang,  Z.  (2025).  Cultural-Intelligent  Dynamic  Medical  Animation  Generation  for  Cross-Lingual
Telemedicine Communication Enhancement. Journal of Science, Innovation & Social Impact, 1(1), 209-
221.

[150].  Wang, Z., & Chu, Z. (2025). GAN-Based Intelligent Keyframe Interpolation Method for Character
Animation:  An  Automated  In-betweening  Approach.  Journal  of  Science,  Innovation  &  Social  Impact,
1(2), 29-40.

[151].  Li,  J.  (2026).  Style  Genes:  Leveraging  Generative  AI  for  Artwork  Authentication  through  Artistic

Style Consistency Analysis. Journal of Sustainability, Policy, and Practice, 2(1), 87-100.

[152].  Li, J. (2025). Enhanced CNN-based Feature Extraction and Classification for Chinese Artwork Styles.

Journal of Science, Innovation & Social Impact, 1(2), 135-148.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

15

[153].  Li, J., Zhang, F., & Li, M. (2026). Comparative Effectiveness of Blockchain Provenance Verification
on  Counterfeit  Reduction  in  Art  Transactions:  A  Multi-Scenario  Empirical  Assessment.  Artificial
Intelligence and Machine Learning Review, 7(2), 82-92.

[154].  Tu, W., Wan, G., Shang, Z., & Du, B. (2025). Efficient relational context perception for knowledge

graph completion. Applied Intelligence, 55(15), 1005.

[155].  Weng, H. (2025). Deep Embedding Clustering with Adaptive Feature Selection for Banking Customer

Segmentation. Spectrum of Research, 5(2).

[156].  Bai,  Y.  (2025).  Effectiveness  Evaluation  of  Adaptive  Difficulty  Adjustment  Algorithms  with
Multimodal Feedback for Social Skills Training in Children with Autism Spectrum Disorder. Journal of
Sustainability, Policy, and Practice, 1(4), 117-129.

[157].  Bai,  Y.  (2025,  September).  Deep  Learning-based  Action  Recognition  for  Temporal  Analysis  and
Intervention  Effectiveness  Assessment  in  Autism  Spectrum  Disorder  Children's  Video  Therapy.  In
Proceedings  of  the  2025  International  Symposium  on  Artificial  Intelligence  and  Computational  Social
Sciences (pp. 307-314).

[158].  Bai,  Y.,  &  Xiao,  P.  (2026).  Adaptive  Prompt  Selection  and  Fading  Optimization  for  Autism  Skill
Acquisition: A Reinforcement Learning Approach. Journal of Advanced Computing Systems, 6(1), 32-
44.

[159].  Bai, Y. (2026). Context-Aware Classification of Verbal Operants in Children with ASD Using Deep

Learning. Journal of Science, Innovation & Social Impact, 2(1), 232-243.

[160].  Bai, Y., & Liu, M. (2026). A Comparative Evaluation of Transfer Learning Methods for Cross-Context
Behavioral Generalization Assessment in Autism Spectrum Disorder Interventions. Journal of Computing
Innovations and Applications, 4(1), 176-185.

[161].  Shi,  W.,  &  Bai,  Y.  (2024).  Adaptive  Learning  Rate  Optimization  for  Personalized  Educational
Interventions  in  Autism  Spectrum  Disorder:  A  Multi-Objective  Reinforcement  Learning  Approach.
Artificial Intelligence and Machine Learning Review, 5(4), 128-138.

[162].  Chung,  P.  T.  (2025,  December).  Data  Mining  Methods  for  Biomechanical  Property  Prediction  of
Biomedical Materials Based on Optimized Feature Dimensionality Reduction. In Proceedings of the 2025
6th International Conference on Computer Science and Management Technology (pp. 174-180).

[163].  Chung,  P.  T.  (2025,  December).  Enhancing  Dental  Polymer  Formulation  through  Interpretable
Machine  Learning:  A  Comparative  Analysis  of  Feature  Selection  and  Algorithm  Performance.  In
Proceedings of the 2025 6th International Conference on Computer Science and Management Technology
(pp. 234-241).

[164].  Chung,  P.  T.

for
Spectrophotometric Dental Shade Classification. Journal of Sustainability, Policy, and Practice, 2(1), 204-
214.

(2026).  Comparative  Evaluation  of  Machine  Learning  Algorithms

[165].  Chung, P. T. (2026). Multi-Objective Optimization of Process Parameters for Dental Resin 3D Printing
Using Improved NSGA-II Algorithm. Journal of Science, Innovation & Social Impact, 2(1), 276-287.

[166].  Liu,  Y.  (2026).  AI-Enhanced  Healthcare  Data  Quality  Governance:  An  Integrated  Approach  for
Anomaly Detection and Integrity Verification. Journal of Sustainability, Policy, and Practice, 2(1), 215-
229.

[167].  Deng, M., & Zou, D. (2026). Application of Cross-Modal Content Consistency Verification in Social
Media Misinformation Detection. Artificial Intelligence and Machine Learning Review, 7(1), 40-52.

[168].  Deng, M. (2025, September). Early Detection of Malicious Accounts on Social Platforms Based on
Temporal Graph Feature Learning. In Proceedings of the 2025 8th International Conference on Computer
Information Science and Artificial Intelligence (pp. 1320-1328).

[169].  Deng,  M.  (2025).  Graph-Based  Temporal  Behavior  Analysis  for  Early  Detection  of  Coordinated
Malicious Accounts in Social Media Platforms. Journal of Science, Innovation & Social Impact, 1(2), 96-
106.

[170].  Long, X. (2025, September). Machine Learning-Based Power Consumption Prediction and Dynamic
Adjustment Strategies for Enterprise Servers. In Proceedings of the 2025 8th International Conference on
Computer Information Science and Artificial Intelligence (pp. 1310-1319).

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

16

[171].  Wei, W., & Shang, Z. (2026). An Empirical Evaluation of Oversampling-Ensemble Interactions Under
Varying Imbalance Ratios for Tabular Data Classification. Artificial Intelligence and Machine Learning
Review, 7(2), 70-81.

[172].  Zhang,  S.,  Jia,  R.,  &  Li,  Z.  (2024).  Agentic  AI  Across  Domains:  A  Comprehensive  Review  of
Capabilities, Applications, and Future Directions. Journal of Computing  Innovations and Applications,
2(1), 86-98.

[173].  Zhao,  F.,  Yu,  M.,  &  Luo,  C.  (2024).  A  Comparative  Evaluation  of  Prompting  Strategies  for  Code

Generation with Large Language Models. Journal of Global Engineering Review, 2(1), 1-11.

[174].  Li, M., Zhao, F., & Tang, T. (2024). How Prompt Specificity Affects Edge Case Handling in LLM-
Generated Code: An Empirical Evaluation. Artificial Intelligence and Machine Learning Review, 5(4),
139-149.

[175].  Zhang,  D.,  &  Feng,  E.  (2024).  Quantitative  Assessment  of  Regional  Carbon  Neutrality  Policy

Synergies Based on Deep Learning. Journal of Advanced Computing Systems, 4(10), 38-54.

[176].  Li, M., Wang, X., & Yu, M. (2025). Comparative Evaluation of Zero-Shot and Few-Shot Performance
of  Large  Language  Models  in  Low-Resource  Language  Machine  Translation.  Journal  of  Global
Engineering Review, 3(2), 59-68.

[177].  Trinh, T. K., & Zhang, D. (2024). Algorithmic fairness in financial decision-making: Detection and
mitigation of bias in credit scoring applications. Journal of Advanced Computing Systems, 4(2), 36-49.

[178].  Zhang, D., & Zheng, Q. (2025). Machine Learning-Based Building Energy Consumption Prediction
and Carbon Reduction Potential Assessment in US Metropolitan Areas. Journal of Industrial Engineering
and Applied Science, 3(5), 27-40.

[179].  Zhang,  D.,  &  Zhang,  F.  (2025).  AI-Assisted  Identification  and  Equity  Assessment  of  Vulnerable
Population Impacts in US Energy Transition. Journal of Advanced Computing Systems, 5(7), 1-17.

[180].  Dong,  B.,  Zhang,  D.,  &  Xin,  J.  (2024).  Deep  reinforcement  learning  for  optimizing  order  book
imbalance-based high-frequency trading strategies. Journal of Computing Innovations and Applications,
2(2), 33-43.

[181].  Shang  Wen,  Tianxing  Tang.A  Comparative  Evaluation  of  URL-Sharing,  Content  Similarity,  and
Temporal Synchronicity Signals for Detecting Coordinated Inauthentic Behavior in Multilingual Political
Discourse

[182].  Yanhuan Chen,Tianxing Tang .Evaluating Prompt Engineering Strategies for Few-Shot Cyber Threat

Intelligence Entity and Relation Extraction from Multi-Source Reports

[183].  Tianxing  Tang,Xuanyi  Fu,Chuankai  Luo.  An  Empirical  Comparison  of  High-Order  Feature
Interaction Operators for Conversion Rate Prediction in Sparse, High-Cardinality Message-Ads Traffic：
Accuracy, Efficiency, and Offline–Online Consistency

[184].  Tianxing Tang,Mingzhuo Yu . A Comparative Evaluation of LLM-Generated Semantic Tags versus
Classical Text Features (TF-IDF, LDA, BERT Embeddings) for User-Interest Enrichment in Short-Video
Recommendation

[185].  Tang, T., & Yu, M. (2024). A Comparative Empirical Study of Semantic Signal Enhancement Methods
for  User  Interest  Features  in  CTR  Prediction:  Applicability  of  TF-IDF  Weighting,  Sentence-BERT
Embeddings, and LDA Topic Fusion. Journal of Computing Innovations and Applications, 2(1), 165-174.

[186].  Li, Z., & Chen, Z. (2025). Performance Evaluation of Prompt Generation Strategies for AI Agents in

Online Programming Education. Journal of Advanced Computing Systems, 5(9), 14-27.

[187].  Xu, S., Zhao, F., & Wang, X. (2025). An Empirical Comparison of Generation Quality and Diversity
Between  Discrete  Diffusion  and  Autoregressive  Text  Generation.  Artificial  Intelligence  and  Machine
Learning Review, 6(2), 16-26.

[188].  Ma,  Q.,  Yue,  L.,  Xu,  S.,  Shi,  Y.,  &  Liu,  H.  (2026,  January).  Web  Agent  Agentic  Reinforcement
Learning Decision Model Under Multi-Cost and Failure Risk Constraints. In Proceedings of the 2026 5th
International Conference on Big Data, Information and Computer Network (pp. 514-520).

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

17

[189].  Yue, L., Xu, D., Qiu, D., Shi, Y., Xu, S., & Shah, M. (2025, December). Sequential Cooperative Multi-
Agent Online Learning and Adaptive Coordination Control in Dynamic and Uncertain Environments. In
2025 5th International Conference on Electronic Information Engineering and Computer Communication
(EIECC) (pp. 692-697). IEEE.

[190].  Liu,  H.,  Xu,  D.,  Ma,  Q.,  Xu,  S.,  &  Qiu,  D.  (2026).  Memory  Poisoning  Propagation  and  Repair

Mechanism in Multi-Agent Collaborative Environments.

[191].  Xu, S., Ma, Q., Liu, H., & Yue, L. (2026). Continuous Reorganization and Performance Preservation

of Agent Memory Structure Under Distributed Change Environments.

[192].  Deng,  M.,  &  Xu,  S.  (2026).  Temporal-Structural  Propagation  Graph  Analysis  for  Coordinated
Misinformation  Campaign  Detection  and  Source  Attribution  in  Social  Networks. Journal  of  Advanced
Computing Systems, 6(5), 1-11.

ISSN: 3071-4656

DOI: 10.66372/JGER.v1i1.1

18

