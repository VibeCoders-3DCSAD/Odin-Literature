---
conversion_metadata:
  converted_at: "2026-07-22T13:30:33Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Han & Lai.pdf"
  source_pdf_sha256: "c8d19ebd372cd7e8e5a7eb165e9eedeb9f0fe2f9a3f7e33ad632eec209947e3b"
  page_count: 23
  markdown_char_count: 280863
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Advanced Computing Systems (JACS) 
ISSN: 3066-3962 
Content Available at SciPublication

Temporal Feature Engineering and Threshold Optimization for Early Warning in 
Healthcare Claims Anomaly Detection 
Mingxuan Han1, Jiawen Lai1.2 
1 Computer Science, University of Utah, UT, USA 
1.2 Computer Engineering, University of California, Riverside, CA, USA

DOI: 10.69987/JACS.2026.60403

K e y w o r d s

A b s t r a c t

Healthcare claims fraud, 
Temporal feature 
engineering, Anomaly 
detection, Threshold 
optimization

that  can

identify  subtle

Healthcare insurance fraud represents a substantial financial burden on medical 
systems worldwide, with fraudulent claims accounting for billions of dollars in 
annual losses. Detecting anomalous patterns in medical claims data requires 
sophisticated  analytical  approaches 
temporal 
irregularities before significant financial damage occurs. This research presents 
a comprehensive investigation of temporal feature engineering methodologies 
and threshold optimization strategies specifically designed for early-warning 
mechanisms  in  healthcare  claims  anomaly  detection.  The  study  develops  a 
systematic framework for extracting meaningful temporal features from claims 
interval  patterns,  claim  frequency 
sequential  data, 
characteristics,  and  seasonal  variation 
feature 
construction techniques that combine statistical analysis and machine learning 
are  employed  to  capture  the  complex  temporal  dependencies  inherent  in 
fraudulent behavior patterns. We investigate threshold optimization strategies 
that balance detection sensitivity with operational constraints through adaptive 
adjustment mechanisms. A retrospective case study of Medicare claims data 
suggests  that  engineered  temporal  features  can  improve  anomaly-detection 
performance.  The  research  provides  practical  guidelines  for  threshold 
parameter selection and dynamic adjustment strategies suitable for production 
deployment. Results suggest improvements in early warning capability while 
maintaining practically manageable false positive rates.

indicators.  Advanced

including  service

1. Introduction

1.1. Research Background and Motivation

Healthcare  expenditure  in  the  United  States  exceeds 
$4.3 
trillion  annually,  representing  approximately 
17.8% of the national gross domestic product [1]. Within 
this  massive  financial  ecosystem,  fraudulent  activities 
pose  a  persistent  threat  to  program  sustainability  and 
beneficiary  welfare.  Federal  healthcare  programs, 
including Medicare and Medicaid, experience estimated 
fraud  rates  ranging  from  3% 
total 
expenditures  [2], translating to potential losses between 
$129 billion and $430 billion per year. The complexity 
of modern healthcare delivery systems, combined with 
the  volume  and  velocity  of  claims  processing,  creates 
opportunities for sophisticated fraud schemes that evade 
traditional detection mechanisms.

to  10%  of

Temporal  patterns  embedded  within  claim  sequences 
provide  critical  signals  for  identifying  anomalous 
behavior. Fraudulent providers often exhibit distinctive 
temporal  characteristics,  including  abnormal  claim 
submission frequencies, irregular service intervals, and 
atypical  billing  time  distributions.  Traditional  rule-
based  detection  systems  struggle  to  adapt  to  evolving 
fraud  tactics  and  generate  excessive  false  alarms, 
temporal 
burdening 
dimension of claims data remains underutilized despite 
its  potential  to  reveal  subtle  patterns  indicative  of 
coordinated  fraud  schemes  or  systematic  billing 
irregularities [3].

resources.  The

investigative

Recent  advances  in  machine  learning  and  time  series 
analysis  offer  promising  approaches  for  extracting 
meaningful  features  from  temporal  claims  data.  Deep 
learning  architectures,  including  Long  Short-Term 
Memory (LSTM) networks, have demonstrated superior 
performance 
temporal 
dependencies  compared  to  conventional  statistical

long-range

capturing

in

Vol. 6(4), pp. 27-49, April 2026 
[27]

---

<!-- PAGE 2 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

methods  [4].  The  challenge  lies  in  designing  feature-
engineering pipelines that transform raw temporal data 
into discriminative representations suitable for anomaly 
detection. Effective feature engineering requires domain 
expertise  to  identify  clinically  meaningful  temporal 
patterns while maintaining computational efficiency for 
real-time processing requirements.

1.2. Problem Statement and Research Objectives

The  primary  challenge  in  healthcare  claims  anomaly 
detection  is  extracting  informative  temporal  features 
that capture fraudulent behavior while minimizing false-
positive  rates  that  overwhelm  investigative  capacity. 
typically  rely  on  manually 
Existing  approaches 
engineered  features  based  on  domain  knowledge, 
limiting  their  ability  to  discover  novel  fraud  patterns. 
Threshold  selection  for  anomaly  alerts  poses  another 
critical  challenge:  overly  sensitive  thresholds  generate 
excessive  false  alarms,  while  conservative  thresholds 
miss  early-stage  fraud.  The  temporal  nature  of  claims 
data introduces additional complexity through seasonal 
patterns, concept drift, and varying baseline behaviors 
across provider specialties and geographic regions.

these

research

temporal

addresses 
investigating

challenges  by 
This 
systematically 
feature 
engineering  methodologies  and  adaptive  threshold 
optimization  strategies.  The  primary  objective  is  to 
develop  a  comprehensive  framework  for  extracting 
temporal features from claim sequences that effectively 
distinguish anomalous patterns from legitimate practice 
variations.  Secondary  objectives  include  designing 
that  dynamically 
threshold-optimization  algorithms 
balance 
operational 
constraints, evaluating the comparative performance of 
different 
real 
Medicare  claims  data,  and  providing  actionable 
guidelines  for  parameter  selection 
in  production 
deployment scenarios. The research specifically focuses 
on  early  warning  mechanisms  that  detect  anomalous 
patterns before substantial financial losses occur [5].

feature-engineering  approaches  on

sensitivity  with

detection

1.3. Contributions and Paper Organization

This  work  makes  several  contributions  to  research  on 
healthcare  claims  anomaly  detection.  A  systematic 
temporal  feature  engineering  framework  is  developed 
that combines statistical analysis with machine learning-
based feature construction to capture complex temporal 
dependencies  in  claims  sequences.  The  framework 
incorporates  multiple  temporal  scales  ranging  from 
short-term  service  intervals  to  long-term  seasonal 
patterns.  A  novel  adaptive  threshold  optimization 
methodology 
that  adjusts  detection 
thresholds  based  on  historical  false  positive  rates  and 
investigative  capacity  constraints.  The  approach 
maintains  detection  effectiveness  while  controlling 
operational  burden 
threshold 
comprehensive 
adjustment

through  dynamic 
A

is  proposed

mechanisms.

experimental evaluation of Medicare Part B claims data 
demonstrates the effectiveness of engineered temporal 
features compared to baseline approaches. Performance 
metrics, including precision, recall, and F1-scores, are 
reported  across  multiple  provider  specialty  categories 
and fraud types.

time  series  data,  and

The remainder of this paper is organized into six main 
sections.  Section  2  reviews  related  work  on  temporal 
anomaly  detection  for  healthcare  claims,  feature 
threshold 
engineering  for 
optimization  strategies  for  early  warning  systems. 
Section  3  presents  the  temporal  feature  engineering 
methodology,  including  feature  extraction  procedures, 
construction  techniques,  and  selection  algorithms. 
Section  4  describes 
threshold  optimization 
the 
framework including adaptive setting strategies, trade-
off  analysis  methods,  and  dynamic  adjustment 
algorithms.  Section  5  reports  experimental  results 
performance 
including 
comparisons, and practical implications for operational 
deployment.  Section  6  discusses  the  conclusions, 
research  limitations,  and  directions  for  future  work. 
Section 7 provides acknowledgments.

descriptions,

dataset

2. Related Work and Theoretical Foundation

2.1.  Temporal  Anomaly  Detection  in  Healthcare 
Claims

Research  in  healthcare  claims  anomaly  detection  has 
evolved from simple rule-based systems to sophisticated 
machine learning approaches. Early detection methods 
relied on manually defined business rules that captured 
known  fraud  indicators,  such  as  excessive  billing 
amounts  or  unusual  service  combinations.  These 
approaches suffered from limited adaptability and high 
false  positive  rates  as  fraudulent  tactics  evolved. 
Statistical methods based on outlier detection principles 
offered  improvements  through  automated  threshold 
determination  based  on  historical  data  distributions. 
Clustering  techniques  grouped  similar  providers  to 
identify deviations from peer behavior patterns. Graph-
based  methods 
relationships  between 
providers, beneficiaries, and services to detect collusive 
fraud networks [6].

analyzed

The  integration  of  temporal  information  into  anomaly 
detection  frameworks  has  gained  increasing  attention. 
Time  series  analysis  methods  model  normal  billing 
patterns  to  identify  temporal  deviations.  Recurrent 
(RNNs)  demonstrate  particular 
neural  networks 
effectiveness  in  capturing  sequential  dependencies 
within claims streams. Autoencoder architectures learn 
compressed 
temporal 
patterns,  flagging  reconstructions  with  high  error  as 
potential  anomalies.  The  temporal  dimension  enables 
the detection of subtle fraud patterns that manifest over 
extended periods, including gradual billing inflation or

representations  of  normal

Vol. 6(4), pp. 27-49, April 2026  
[28]

---

<!-- PAGE 3 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

the  strategic  timing  of  claim  submissions  to  avoid 
detection. Seasonal decomposition techniques separate 
legitimate periodic variations from genuine anomalies, 
reducing false positives caused by predictable cyclical 
patterns [7].

Recent work has explored hybrid approaches combining 
multiple  detection  methodologies.  Ensemble  methods 
aggregate  predictions  from  diverse  algorithms 
to 
improve robustness and reduce individual model biases. 
Cost-sensitive  learning  frameworks  explicitly  account 
for  the  asymmetric  costs  of  false  positives  and  false 
negatives  in  fraud  detection  applications.  Transfer 
learning  techniques  leverage  knowledge  from  related 
domains  or  historical  periods  to  improve  detection 
performance  on  new  fraud  patterns.  The  challenge 
remains  in  designing  systems  that  maintain  high 
detection rates while controlling false positive volumes 
to manageable levels for investigative follow-up. Real-
additional 
time  detection 
constraints  on  computational  complexity  and  on 
tolerance to latency.

requirements

impose

2.2.  Feature  Engineering  Approaches  for  Time 
Series Data

raw

for 
time

temporal  data 
series

involves 
Feature  engineering 
transforming 
into  meaningful 
representations that capture relevant patterns. Statistical 
features  including  mean,  variance,  skewness,  and 
kurtosis  provide  basic  distributional  characteristics  of 
temporal  sequences.  Trend  analysis  extracts  linear  or 
polynomial growth patterns. Autocorrelation functions 
lag 
measure 
intervals.  Spectral  analysis  decomposes  signals  into 
frequency  components  to  identify  periodic  patterns. 
Window-based features compute statistics over sliding 
temporal windows to capture local behavior variations. 
These  traditional  approaches  provide  interpretable 
features but may miss complex nonlinear patterns.

temporal  dependencies  at  different

temporal

trajectories

that  preserve  essential

Machine  learning-based  feature  construction  offers 
temporal 
automated  discovery  of  discriminative 
patterns.  Functional  Principal  Component  Analysis 
(FPCA)  decomposes 
into 
dominant  modes  of  variation,  creating  compact 
representations 
temporal 
structure [8]. Matrix profile techniques identify repeated 
patterns  and  discord  sequences  within  time  series. 
Shapelet  mining  discovers characteristic  subsequences 
that  distinguish  between  classes.  Deep 
learning 
approaches, including convolutional filters and attention 
temporal  features 
mechanisms, 
learn  hierarchical 
directly  from  raw  data.  The 
trade-off  between 
automated feature learning and interpretability remains 
a  central  consideration,  particularly 
in  regulated 
domains requiring explainable detection decisions.

Domain-specific  feature  engineering  for  healthcare 
claims requires incorporation of medical knowledge and

regulatory  constraints.  Recency-frequency-monetary 
(RFM)  features  borrowed  from  marketing  analytics 
capture  recent  billing intensity,  submission  frequency, 
and  financial  magnitude.  Service  sequence  features 
analyze  the  ordering  and  timing  of  procedure  codes. 
track 
Beneficiary-provider 
continuity  of  care  relationships.  Geographic  and 
temporal  clustering 
identify  coordinated 
features 
activity  across  multiple  providers  or  locations.  The 
effectiveness of engineered features depends on careful 
selection 
informed  by  fraud  domain  knowledge, 
combined with systematic evaluation on representative 
datasets.

interaction

patterns

2.3.  Threshold  Optimization  Strategies  in  Early 
Warning Systems

thresholds  derived

Threshold selection critically impacts  the performance 
and operational viability of anomaly detection systems. 
Fixed  thresholds  based  on  percentile  cutoffs  provide 
simplicity but fail to adapt to changing data distributions 
or  varying  baseline  behaviors  across  subgroups. 
Statistical 
from  normal  data 
characteristics,  such  as  three  standard  deviations  from 
the  mean,  offer  principled  approaches  but  assume 
specific  distributional  properties  that  may  not  hold  in 
practice.  Receiver  Operating  Characteristic  (ROC) 
curve  analysis  enables  systematic  exploration  of 
to  select  optimal 
trade-offs 
sensitivity-specificity 
operating points based on cost considerations [9].

adjust

threshold

strategies

Adaptive 
detection 
boundaries  based  on  operational 
feedback  and 
thresholding 
performance  monitoring.  Dynamic 
incorporates recent false positive rates to automatically 
tune  sensitivity 
levels.  Concept  drift  detection 
algorithms  identify  distribution  shifts  that  necessitate 
threshold  recalibration.  Multi-threshold  approaches 
employ different cutoffs for various risk levels, enabling 
tiered 
investigation  prioritization.  Context-aware 
thresholds  vary  by  provider  specialty,  geographic 
region,  or  temporal  period  to  account  for  legitimate 
practice  variation.  The  challenge  lies  in  balancing 
responsiveness  to  changing  patterns  with  stability  to 
avoid excessive fluctuations that confuse users.

Early  warning 
requires  careful 
system  design 
consideration  of  operational  constraints,  including 
investigative capacity, alert fatigue, and response time 
requirements. Threshold optimization must account for 
asymmetric  costs:  false  negatives  represent  potential 
fraud losses, while false positives consume investigative 
resources  without 
testing 
frameworks enable refinement of initial alerts through 
progressive analysis stages. Explainability requirements 
demand  that  threshold  crossings  trigger  actionable 
insights  rather  than  opaque  anomaly  scores.  The 
integration  of  domain  expertise  through  adjustable 
sensitivity  controls  empowers  investigators  to  tune

recovery.  Sequential

Vol. 6(4), pp. 27-49, April 2026  
[29]

---

<!-- PAGE 4 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

detection  based  on  emerging  fraud  intelligence  and 
changing enforcement priorities.

3. Methodology: Temporal Feature Engineering 
Framework

3.1.  Temporal  Feature  Extraction  from  Claims 
Sequential Data

Claim Timestamp Analysis

The foundation of temporal feature engineering rests on 
systematic analysis of claim submission timestamps and 
service  dates.  Each  claim  record  contains  multiple 
temporal attributes including service start date, service 
end  date,  submission  date,  and  processing  date.  The 
temporal features extracted from these attributes capture 
different  aspects  of  provider  behavior  and  billing 
patterns.  Service-to-submission  lag  measures  the  time 
interval between service delivery and claim filing, with 
abnormal  patterns 
indicating  potential  post-dating 
schemes or delayed batch submissions characteristic of 
certain fraud types. Submission date clustering analysis 
identifies  unusual  concentrations  of  claims  at  specific 
calendar  periods,  such  as  end-of-month  or  end-of-
quarter  submissions  that  may  signal  quota-driven 
fraudulent billing [10].

and

features

reveal 
day-of-week 
Time-of-day 
operational patterns that differ between legitimate and 
fraudulent  providers.  Extraction  procedures  compute 
submission-hour  distributions  to  identify  providers 
submitting  disproportionate  claims  during  off  hours, 
when  manual  review  processes  may  be  reduced. 
Weekend  submission  ratios  capture  abnormal  activity 
patterns  inconsistent  with  typical  medical  practice 
schedules.  Holiday  submission  indicators  flag  claims 
filed  during  periods  when  legitimate  medical  services 
typically decrease. These temporal fingerprints provide 
powerful  discriminative  features  when  aggregated 
across rolling window periods. The extraction pipeline 
processes  timestamp  fields  through  standardized  date 
parsing  and 
to  ensure 
consistency across geographically distributed providers 
[11].

timezone  normalization

Temporal  sequence  ordering  analysis  examines  the 
chronological  pattern  of  service  codes  within  patient 
episodes.  Legitimate  medical  care  follows  clinically 
appropriate  sequences  determined  by  diagnostic 
protocols  and  treatment  pathways.  Sequence  reversal 
indicators  identify  claims  in  which  diagnostic  tests 
occur after treatment procedures, suggesting fabricated 
medical-necessity  documentation.  Temporal  gap 
analysis within treatment sequences identifies unusually 
extended  intervals  between  related  services  that  may 
indicate  claim  splitting  strategies.  The  extraction 
methodology  constructs  directed  acyclic  graphs  that 
represent  temporal  dependencies  among  procedure

codes, and computes graph-based features such as path 
lengths, branching factors, and cycle-detection metrics. 
These structural temporal features complement simple 
timestamp  statistics  by  incorporating  medical  domain 
knowledge about appropriate care progression patterns.

Data access & compliance.

We used a de-identified Medicare Part B claims dataset 
(2020–2022) obtained through authorized access (e.g., 
[CMS  DUA  /  VRDC  /  institutional  agreement]).  The 
study  used  no  direct  identifiers,  and  analyses  were 
conducted on derived/aggregated features. Due to data-
use restrictions, the raw claims cannot be redistributed; 
however, we will release feature engineering code and 
evaluation scripts to support reproducibility.

Service Interval Pattern Mining

Service interval features quantify the temporal spacing 
between consecutive services for the same beneficiary 
or by the same provider. Inter-service intervals capture 
billing  rhythm  characteristics  that  distinguish  normal 
practice  patterns  from  systematic  fraud  schemes.  The 
extraction  methodology  computes  multiple  interval 
statistics, 
including  minimum,  maximum,  mean, 
median,  and  coefficient  of  variation,  across  rolling 
windows  of  varying  lengths.  Providers  engaged  in 
excessive  billing  schemes  often  exhibit  characteristic 
spikes 
interval 
corresponding to automated billing cycles or systematic 
overbilling  patterns.  Legitimate  providers  demonstrate 
more variable intervals reflecting genuine patient needs 
and appointment scheduling constraints.

distributions  with

periodic

Beneficiary-level  interval  analysis  examines  temporal 
patterns  of  services  received  by  individual  patients. 
Unusually frequent services within short time windows 
indicate  potential  phantom  billing  or  unnecessary 
treatment patterns. The extraction process uses sliding-
window algorithms to compute service counts and dollar 
amounts over configurable time periods ranging from 7 
days  to  90  days.  Statistical  outlier  detection  at  the 
interval 
beneficiary 
patterns  inconsistent  with  their  diagnosis  codes  and 
demographic  characteristics.  Cross-provider  interval 
analysis reveals beneficiaries receiving similar services 
from multiple providers within implausible time frames, 
suggesting  coordinated  fraud  networks  or  beneficiary 
cooperation in fraud schemes [12].

identifies  patients  with

level

The methodology incorporates domain-specific interval 
constraints  derived  from  clinical  guidelines  and 
regulatory requirements. Certain procedure codes have 
regulatory maximum frequency limits within specified 
time  periods  established  by  the  Centers  for  Medicare 
and  Medicaid  Services  (CMS).  Feature  extraction 
computes  violation  indicators  by  comparing  actual 
billing  intervals  against  these  regulatory  thresholds. 
Medical necessity intervals defined by clinical protocols

Vol. 6(4), pp. 27-49, April 2026  
[30]

---

<!-- PAGE 5 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

provide additional benchmarks for identifying temporal 
anomalies. The extraction framework maintains lookup 
tables  that  map  procedure  codes  to  the  appropriate 
minimum intervals based on medical standards of care. 
Deviations  from  these  clinically  appropriate  intervals

generate risk scores that feed into downstream anomaly 
detection 
the 
comprehensive taxonomy of temporal interval features 
extracted from claims data.

algorithms.  Table

presents

1

Table 1: Temporal Interval Feature Taxonomy

Feature Category

Specific Features

Calculation Method

Fraud Detection Relevance

Service-to-
Submission Lag

Mean  lag,  Std  dev,  Min, 
Max

Difference  between  service 
date and submission date

Identifies  post-dating  and 
delayed batch submissions

Inter-Service 
Intervals

Mean,  Median, 
Autocorrelation

CV,

Time  between  consecutive 
services for same beneficiary

Detects excessive billing and 
systematic patterns

Beneficiary  Interval 
Patterns

7-day  count,  30-day  count, 
90-day count

Service 
rolling windows

frequency  within

Reveals phantom billing and 
unnecessary treatments

Regulatory 
Compliance

Violation 
Frequency limits

indicators,

Comparison 
regulatory 
frequencies

against 
maximum

Flags  violations  of  billing 
frequency regulations

Clinical 
Appropriateness

Medical  necessity  intervals, 
Protocol deviations

Comparison  against  clinical 
guideline intervals

Identifies 
medically 
inappropriate service timing

The  temporal  interval  feature  space  captures  multiple 
dimensions of provider billing behavior across different 
time  scales.  Short-term  intervals  reveal  immediate 
billing patterns and response to regulatory requirements. 
Medium-term intervals expose seasonal variations and 
practice  evolution.  Long-term  intervals  enable  the 
detection of gradual trends indicating systematic fraud 
schemes  that  develop  slowly  to  avoid  detection.  The 
multi-scale 
temporal  analysis  provides  robustness 
against  fraud  tactics  that  operate  at  different  temporal 
resolutions.

Frequency Distribution Characterization

Claim  frequency  distributions  provide  critical  signals 
about  provider  billing 
intensity  and  consistency 
patterns.  The  extraction  methodology  computes 
frequency  features  at  multiple  aggregation  levels, 
including daily, weekly, monthly, and quarterly periods. 
Simple frequency counts measure the number of claims 
submitted  within  each 
time  window.  Frequency 
variability  metrics,  including  standard  deviation  and 
coefficient of variation, quantify consistency of billing 
patterns  over  time.  Sudden  changes  in  frequency 
detected by comparing consecutive period statistics may 
indicate  the  potential  onset  of  fraudulent  activity  or 
tactics.  The  extraction  pipeline 
shifts 
implements  change  point  detection  algorithms  to

fraud

in

identify statistically significant deviations from baseline 
frequency patterns [13].

Distribution  shape  characteristics  capture  more  subtle 
aspects  of  billing  patterns.  Skewness  measures 
asymmetry  in  frequency  distributions,  with  highly 
skewed patterns suggesting concentrated billing activity 
tail 
during  specific  periods.  Kurtosis  quantifies 
behavior, identifying providers with occasional extreme 
billing  spikes 
inconsistent  with  normal  practice 
variation. Entropy features measure the randomness of 
temporal  distributions;  low  entropy  indicates  highly 
structured,  potentially  artificial  billing  patterns.  The 
extraction  framework  computes  these  distributional 
statistics  across rolling  windows to track  the  temporal 
evolution  of  frequency  characteristics.  Comparative 
analysis  benchmarks  individual  provider  distributions 
against  peer  groups  defined  by  specialty,  geography, 
and practice size.

Procedure-specific frequency analysis examines billing 
patterns for individual service codes. Certain high-value 
procedures  have  expected  frequency  ranges  based  on 
population health statistics and specialty practice norms. 
The  extraction  methodology  maintains 
reference 
frequency distributions for common procedures derived 
from  aggregated  claims  data.  Provider-specific 
frequencies  are  compared  against  these  reference 
distributions  to  compute  statistical  divergence  scores.

Vol. 6(4), pp. 27-49, April 2026  
[31]

---

<!-- PAGE 6 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

Disproportionate billing of specific high-reimbursement 
procedures  represents  a  common  fraud  indicator.  The 
feature  set 
includes  procedure  diversity  metrics 
measuring  the  distribution  of  claim  volumes  across

different  service  codes.  Abnormally  concentrated 
billing  on  limited  procedure  sets  suggests  potential 
upcoding or phantom billing schemes targeting specific 
reimbursement opportunities.

Table 2: Frequency Distribution Feature Summary

Feature Type

Statistical Measures

Anomaly Indicators

Daily Frequency

Mean:  23.4  claims/day,  Std:  8.7,  CV: 
0.37

Sudden spikes >3 std deviations

Weekly Frequency

Mean:  164.2  claims/week,  Skewness: 
0.82

High  skewness  indicating  concentrated 
bursts

Monthly Frequency

Mean:  710.8  claims/month,  Kurtosis: 
4.3

High  kurtosis  revealing  extreme  billing 
spikes

Procedure-Specific 
Frequency

KL  divergence:  0.43,  JS  divergence: 
0.28

Large divergence from peer distributions

Temporal Entropy

Shannon  entropy:  3.2  bits  (legitimate: 
4.8)

Low entropy indicating structured patterns

Figure  1  illustrates  the  temporal  distribution  patterns 
observed in legitimate versus fraudulent provider billing 
behaviors across a twelve-month observation period.

Figure 1: Temporal Billing Frequency Distributions

Vol. 6(4), pp. 27-49, April 2026  
[32]

---

<!-- PAGE 7 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

claim

This  visualization  presents  a  multi-panel  comparative 
analysis  displaying  monthly 
submission 
frequencies for three provider categories over a twelve-
month period. The top panel shows legitimate provider 
patterns  characterized  by  relatively  stable  monthly 
frequencies with moderate variations ranging from 180 
to  240  claims  per  month  and  gradual  seasonal  trends 
including  a  typical  summer  reduction  and  year-end 
increase. The middle panel illustrates early-stage fraud 
patterns  exhibiting  a  characteristic  sudden  increase  in 
claim  frequency  beginning  at  month  6,  rising  from  a 
baseline of 200 claims per month to over 400 claims by 
month  12,  with  a  steep  linear  growth  trajectory.  The 
bottom  panel  depicts  sophisticated  fraud  patterns 
showing  periodic  spikes  every  three  months  in  claim 
frequencies  reaching  500  claims,  alternating  with 
baseline periods around 200 claims, creating a sawtooth 
pattern  designed  to  evade  simple  threshold-based 
detection  systems.  Each  panel  includes  error  bars 
representing the standard deviation within provider peer 
groups,  demonstrating  that  fraudulent  patterns  extend 
significantly  beyond  normal  variation  ranges.  The 
visualization  employs  a  consistent  color  scheme  with 
blue lines representing actual frequencies, gray shaded 
regions  indicating  normal  variation  ranges  defined  as 
mean  plus  or  minus  two  standard  deviations,  and  red 
dotted  lines  marking  regulatory  threshold  levels.  This 
multi-scale 
enables 
investigators to visually distinguish between legitimate 
practice  variation  and  anomalous  billing  patterns 
requiring detailed investigation.

representation

temporal

3.2. Statistical and Machine Learning-based Feature 
Construction

Statistical Transformation Features

Statistical  transformation  methods  construct  derived 
features 
that  capture  nonlinear  relationships  and 
complex  dependencies  within  temporal  claims  data. 
Moving average features smooth short-term fluctuations 
to  reveal  underlying  trends.  The  construction  process 
computes  simple  moving  averages  across  multiple 
window sizes ranging from seven days to ninety days. 
Exponentially  weighted  moving  averages  provide

adaptive smoothing that emphasizes recent observations 
while retaining historical context. Momentum features 
calculate the rate of change in moving averages to detect 
acceleration  or  deceleration  in  billing  patterns.  These 
trend-based  features  enable  identification  of  gradual 
fraud  schemes  that  slowly  escalate  billing  volumes  to 
avoid triggering fixed threshold alerts [14].

Seasonal  decomposition  techniques  separate  temporal 
signals  into  trend,  seasonal,  and  residual  components. 
The construction methodology applies classical additive 
or  multiplicative  decomposition  models  to  extract 
seasonality patterns with annual, quarterly, or monthly 
periodicities. Residual components after removing trend 
and seasonal effects represent deviations from expected 
patterns  that  may  indicate  anomalous  behavior.  The 
feature 
strength  metrics 
quantifying the magnitude of periodic variations relative 
to total signal variance. Providers with weak or absent 
seasonal patterns despite specialty norms raise suspicion 
of  artificial  billing  unconnected  to  actual  patient  care 
cycles.  De-seasoned  features  enable  fair  comparison 
across different calendar periods by removing legitimate 
periodic variations.

seasonal

includes

set

framework  computes

Distributional  distance  features  measure  divergence 
between  observed  temporal  patterns  and  reference 
distributions  representing  normal  behavior.  Kullback-
Leibler  (KL)  divergence  quantifies  information  loss 
when  using  a  reference  distribution  to  approximate 
observed patterns. Jensen-Shannon divergence provides 
a  symmetric  alternative  suitable 
for  comparing 
distributions without requiring absolute continuity. The 
these  distance 
construction 
metrics  comparing  individual  provider  distributions 
against peer group benchmarks. Earth mover's distance 
captures 
transforming  one 
distribution into another, providing an intuitive measure 
of  distributional  dissimilarity.  These  distance-based 
features effectively detect subtle deviations from normal 
patterns  that  may  escape  simpler  threshold-based 
detection  methods.  Table  3  summarizes  the  statistical 
their  fraud  detection 
transformation  features  and 
relevance.

the  minimal  cost  of

Table 3: Statistical Transformation Features

Transformation Type  Mathematical Formula

Detection Application

Moving Average (MA)  MA_t = Σ(x_{t-i})/n for i=0 to n-1

Smooths fluctuations revealing underlying trends

Exponential  Weighted 
MA

EWMA_t 
α)·EWMA_{t-1}

=

α·x_t

+

(1-

Adaptive smoothing emphasizing recent patterns

Momentum

M_t = MA_t - MA_{t-k}

Detects acceleration in billing volume changes

Vol. 6(4), pp. 27-49, April 2026  
[33]

---

<!-- PAGE 8 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

Transformation Type  Mathematical Formula

Detection Application

Seasonal Decomposition

x_t = T_t + S_t + R_t

Separates  trends  from  seasonal  and  residual 
components

KL Divergence

D_KL(P||Q) = Σ P(x)·log(P(x)/Q(x))  Measures

benchmarks

distribution

divergence

from

Functional Principal Component Analysis

time

Basis

Functional  Principal  Component  Analysis  provides 
dimensionality reduction for temporal trajectories while 
preserving  essential  dynamic  characteristics.  The 
construction  methodology 
treats  provider  billing 
sequences  as  functional  data  objects  defined  over 
continuous 
function 
domains. 
representations  including  B-splines  or  Fourier  series 
approximate 
smooth 
continuous  functions.  The  FPCA  procedure  computes 
representing  dominant  modes  of 
eigenfunctions 
the  dataset.  Projection  of 
temporal  variation 
individual  provider  trajectories  onto  these  principal 
components 
low-dimensional 
representations  capturing  essential  temporal  structure. 
The  first  few  principal  components  typically  explain 
substantial  proportions  of  total  variance,  enabling 
efficient representation of complex temporal patterns.

observations

compact

discrete

yields

as

in

Provider-specific  principal  component  scores  serve  as 
derived  features  for  downstream  anomaly  detection 
algorithms.  Extreme  scores  on  particular  components 
indicate unusual temporal patterns along specific modes 
of  variation.  Multivariate  outlier  detection  in  the 
component  score  space  identifies  providers  whose 
temporal profiles deviate substantially from population 
norms. The construction process computes both mean-
level  components  capturing  average  billing  intensity 
and  variance  components 
temporal 
volatility. Providers with unusual combinations of mean 
and  variance  characteristics  emerge  as  high-risk 
candidates  for  investigation.  Loading  patterns  on 
principal components provide interpretable insights into 
specific 
that  distinguish 
anomalous providers.

temporal  characteristics

representing

functions,

scalar-valued

time.  Rather

Distributional functional  principal  component  analysis 
extends  the  methodology  to  capture  evolution  of 
probability  distributions  over 
than 
the  approach 
modeling 
represents  empirical  claim  distributions  at  each  time 
point. The procedure computes principal components of 
distribution-valued  functions,  capturing  modes  of 
variation  in  how  providers'  claim  distributions  evolve 
temporally.  This  sophisticated  representation  detects 
fraud  patterns 
in 
distributional  characteristics  rather  than  simple  mean

through  changes

that  manifest

shifts. Providers systematically shifting their billing mix 
toward high-reimbursement services exhibit distinctive 
distributional  evolution  patterns  captured  by 
this 
approach.  The  construction  framework  implements 
efficient computational algorithms enabling application 
to  large-scale  claims  datasets  containing  millions  of 
providers.

Recurrent Neural Network Embeddings

to  generate

Deep  learning-based  feature  construction  leverages 
recurrent neural network architectures to learn compact 
representations  of  temporal  claims  sequences.  Long 
Short-Term  Memory  networks process  variable-length 
sequences  of  claim 
fixed-
records 
dimensional  embedding  vectors.  The  construction 
methodology  trains  LSTM  autoencoders  on  large 
corpora  of  claim  sequences  to  learn  generalizable 
temporal  patterns.  The  encoder  network  compresses 
input 
latent 
representations while the decoder reconstructs original 
sequences  from  these  representations.  Reconstruction 
error  serves  as  an  anomaly  indicator,  with  poor 
reconstructions  suggesting  deviations  from  learned 
normal patterns. The latent representations themselves 
provide 
features  capturing  complex 
temporal dependencies [15].

128-dimensional

informative

sequences

into

Attention  mechanisms  enhance  recurrent  network 
representations  by  identifying  important  time  steps 
within sequences. The construction process implements 
attention layers that compute weighted combinations of 
hidden  states  across  temporal  positions.  Attention 
weights indicate which time periods contribute most to 
final representations, providing interpretability for deep 
learning  features.  Providers  with  unusual  attention 
patterns  focusing  on  specific  temporal  windows  may 
exhibit targeted fraud strategies active during particular 
periods.  The 
framework 
processes  claims 
through  pre-trained 
networks  to  generate  128-dimensional  feature  vectors 
suitable for conventional machine learning algorithms. 
This  hybrid  approach  combines  deep 
learning 
representation  power  with  the  interpretability  and 
calibration properties of traditional methods.

embedding

sequences

extraction

Graph  neural  networks  provide  alternative  embedding 
approaches  for  claims  data  by  explicitly  modeling 
relationships  between  entities.  The  construction

Vol. 6(4), pp. 27-49, April 2026  
[34]

---

<!-- PAGE 9 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

methodology  represents  claims  data  as  heterogeneous 
graphs  with  nodes  for  providers,  beneficiaries,  and 
procedures  connected  by  edges  representing  claims 
transactions.  Graph  convolutional  layers  aggregate 
information from local neighborhoods to compute node 
embeddings.  Temporal  graph  networks  extend  this 
framework  by  incorporating  edge  timestamps  and 
evolving  graph  structures.  Provider  embeddings

through

these  graph-based  approaches 
generated 
capture both individual temporal patterns and relational 
context  within  broader  healthcare  delivery  networks. 
Collusive fraud schemes involving coordinated activity 
across  multiple  providers  emerge  through  unusual 
reflecting  anomalous  graph 
embedding  patterns 
structures.

Table 4: Deep Learning Feature Construction Performance

Architecture

Embedding Dimension  Training Time (hours)  Detection Rate Improvement

LSTM Autoencoder

LSTM with Attention

Bidirectional LSTM

128

128

256

Graph Neural Network

64

Temporal Graph Network

64

14.3

18.7

22.1

31.5

38.9

+0.06 (0.81→0.87)

+0.07 (0.81→0.88)

+0.08 (0.81→0.89)

+0.05 (0.81→0.86)

+0.06 (0.81→0.87)

Figure 2 visualizes the embedding space learned by the 
autoencoder  network,  projecting  high-
LSTM 
two 
dimensional

representations

temporal

into

dimensions  using  t-distributed  Stochastic  Neighbor 
Embedding (t-SNE) dimensionality reduction.

Figure 2: LSTM Autoencoder Embedding Space Visualization

This  two-dimensional  scatter  plot  displays  t-SNE 
projections  of  128-dimensional  LSTM  autoencoder 
embeddings for 5,000 healthcare providers. Each point 
represents  a  single  provider's  temporal  billing  pattern 
encoded as a latent vector. Color coding distinguishes 
three  provider  categories:  blue  points  (n=4,650) 
represent legitimate  providers forming  a dense  central

cluster  with  smooth  gradients  indicating  continuous 
variation in normal billing patterns. Red points (n=300) 
mark confirmed fraudulent providers primarily located 
in  the  periphery  of  the  embedding  space,  with  three 
distinct  sub-clusters  corresponding  to  different  fraud 
types:  Type  A  fraud  involving  phantom  billing  in  the 
upper-right quadrant showing embeddings distant from

Vol. 6(4), pp. 27-49, April 2026  
[35]

---

<!-- PAGE 10 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

legitimate  clusters,  Type  B  fraud  involving  upcoding 
schemes  in  the  lower-left  region  exhibiting  moderate 
separation, and Type C fraud involving excessive billing 
in the lower-right corner displaying partial overlap with 
legitimate provider distributions. Yellow points (n=50) 
investigation  occupying 
indicate  providers  under 
intermediate  positions  between 
and 
legitimate 
confirmed fraud clusters, suggesting behavioral patterns 
with  ambiguous  characteristics.  The  visualization 
includes  density  contours  derived  from  kernel  density 
estimation,  with  darker  regions  representing  higher 
concentration  of  legitimate  providers  and  providing 
visual  reference  for  identifying  unusual  embedding 
positions. Distance from the legitimate cluster centroid 
marked with a black cross correlates strongly with fraud 
likelihood,  with  providers  beyond  1.5  standard 
deviations  exhibiting  73%  fraud  detection  accuracy. 
The plot demonstrates the LSTM autoencoder's ability 
to  learn  meaningful  temporal  representations  that 
naturally  separate  anomalous  billing  patterns  in  latent 
space, supporting subsequent classification and ranking 
algorithms for fraud detection prioritization.

3.3. Feature Selection and Importance Ranking

Filter-based Selection Methods

Feature selection reduces dimensionality by identifying 
the  most  informative  temporal  features  for  anomaly 
detection.  Filter  methods  evaluate  individual  features 
independently  of 
specific  detection  algorithms. 
Correlation  analysis  identifies  features  with  strong 
associations  to  known  fraud  labels  while  removing 
redundant  features  with  high  inter-correlation.  The 
selection process computes Spearman rank correlations 
between  features  and  fraud  indicators  to  rank features 
by  discriminative  power.  Mutual  information  criteria 
measure  statistical  dependence  between  features  and 
fraud  labels,  capturing  nonlinear  relationships  missed

by  linear  correlation.  Features  with  high  mutual 
information receive priority in the selected subset. Chi-
square tests for categorical features assess independence 
from  fraud  labels,  with  high  chi-square  statistics 
indicating informative features.

removes

selection

Variance-based 
low-variance 
features  that  provide  minimal  information  across 
providers.  Features  with  variance  below  specified 
thresholds  are  eliminated  as  unlikely  to  discriminate 
between normal and anomalous patterns. Coefficient of 
variation normalizes variance by mean values to enable 
fair  comparison  across  features  with  different  scales. 
The  selection  methodology  implements  percentile-
based thresholds to retain features in the top deciles of 
variance 
distributions. 
Multicollinearity analysis identifies feature groups with 
high  pairwise  correlations,  retaining  only  a  single 
representative  from  each  correlated  cluster.  Principal 
component  analysis  on  feature  correlation  matrices 
guides  selection  of  maximally  independent  feature 
subsets spanning the full information space.

or  mutual

information

rankings  as

Information gain and Gini importance metrics derived 
from  decision  tree  algorithms  provide  supervised 
feature  ranking.  The  selection  process  trains  shallow 
decision  trees  and  extracts  feature  importance  scores 
based  on  their  contribution  to  classification  accuracy. 
Features selected for splits near tree roots receive higher 
importance 
they  provide  maximum 
information  gain  for  distinguishing  fraud  cases. 
Ensemble-based importance aggregates rankings across 
multiple  trees  to  obtain  stable  estimates  robust  to 
importance 
tree  variance.  Permutation 
individual 
evaluates feature relevance by measuring performance 
degradation when feature values are randomly shuffled, 
with  large  drops  indicating  critical  features.  Table  5 
presents  feature  importance  rankings  across  different 
selection methodologies.

Table 5: Feature Importance Rankings Across Selection Methods

Feature Name

Mutual 
Information

Random 
Importance

Forest

Permutation 
Importance

Service-to-Submission Lag Std Dev

0.087

Weekend Submission Ratio

0.074

Claim  Frequency  Coefficient  of 
Variation

0.069

Autocorrelation Lag-7

FPCA Principal Component 1

0.066

0.062

0.089

0.077

0.071

0.068

0.064

0.092

0.079

0.068

0.071

0.063

Vol. 6(4), pp. 27-49, April 2026  
[36]

---

<!-- PAGE 11 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

Wrapper-based Selection Algorithms

Wrapper  methods  evaluate  feature  subsets  based  on 
their  performance  with  specific  anomaly  detection 
algorithms.  Sequential  forward  selection  starts  with 
empty  feature  sets  and  iteratively  adds  features  that 
maximize  detection  performance.  The  algorithm 
evaluates  all  remaining  features  at  each  iteration, 
selecting the feature providing greatest improvement to 
a  held-out  validation  set.  Sequential  backward 
elimination  begins  with  all  features  and  iteratively 
removes 
feature  based  on 
important 
performance  impact.  This  computationally  intensive 
approach evaluates every possible removal candidate at 
each  step.  The  selection  process  continues  until 
performance degradation exceeds acceptable thresholds 
or reaches target feature set sizes.

least

the

importance

Recursive  feature  elimination  implements  efficient 
backward  selection  by  removing  multiple  features  per 
iteration  based  on 
rankings.  The 
methodology trains detection algorithms on full feature 
sets  and  extracts  feature  importance  scores.  Features 
with  lowest  importance  are  removed  in  batches,  with 
algorithm retraining and importance re-evaluation after 
each  elimination  round.  Cross-validation  estimates 
performance  for  each  feature  subset  size  to  identify 
optimal  dimensionality  balancing  detection  accuracy 
and computational efficiency. The procedure generates 
performance  curves  showing  detection  metrics  as 
functions of feature set size, enabling informed selection 
of appropriate feature subset cardinalities for production 
deployment.

through

evolution

Genetic  algorithms  provide  stochastic  optimization 
approaches  to  feature  selection.  The  methodology 
represents feature subsets as binary chromosomes where 
each gene indicates inclusion or exclusion of a feature. 
Population-based 
selection, 
crossover,  and mutation  operations  explores  the  space 
of  possible  feature  combinations.  Fitness  functions 
based  on  detection  algorithm  performance  guide 
evolution toward high-quality feature subsets. Multiple 
independent  runs  with  different  random  initializations 
improve  coverage  of  the  search  space  and  provide 
ensembles  of  candidate  feature  sets.  The  selection 
framework  evaluates  pareto-optimal  solutions  trading 
off  detection  performance  against  feature  set  size, 
enabling  decision-makers  to  choose  operating  points 
matching  operational  requirements  and  computational 
constraints.

Embedded Selection Through Regularization

training

algorithm

Embedded methods integrate feature selection directly 
into 
through 
regularization  penalties.  L1  regularization  encourages 
sparse  feature  weights  by  penalizing  the  absolute 
magnitude  of  coefficients.  The  resulting  models 
automatically  zero  out  uninformative  features  during

procedures

interpretable

optimization.  Lasso  regression  for  anomaly  scoring 
implements  L1  penalties  yielding  sparse  predictive 
models  with 
feature  subsets.  The 
regularization parameter controls the trade-off between 
model fit and sparsity, with larger penalties producing 
sparser  solutions.  Cross-validation  determines  optimal 
regularization strength balancing detection performance 
and feature set parsimony.

algorithms

Elastic  net  combines  L1  and  L2  regularization  to 
address  correlated  feature  groups.  The  methodology 
maintains  stability  when  handling  highly  correlated 
temporal features by distributing weights across related 
features  rather  than  arbitrarily  selecting  individual 
including 
representatives.  Tree-based 
gradient  boosting  machines  provide  implicit  feature 
selection  through  split  point  selection.  Features  never 
selected  for  splits receive zero importance  and  can be 
safely  removed.  The  embedded  selection  process 
extracts  feature  usage  frequencies  across  boosting 
iterations  and  eliminates  features  falling  below  usage 
thresholds. Random forest importance scores aggregate 
feature  contributions  across  ensemble  members, 
providing  stable  importance  estimates  for  selection 
decisions.

as

scores

feature

suggesting

interpretable

Neural  network-based  selection  employs  attention 
mechanisms  and  dropout  regularization  to  identify 
important  features.  Attention  weights  provide  feature 
importance 
selection 
probabilities.  Dropout  rates  calibrated  during  training 
redundancy,  with  high  dropout 
indicate 
tolerance 
features.  The 
framework  implements  learnable  feature  selection 
masks  updated  through  gradient  descent  to  jointly 
optimize  feature  subsets  and  detection  performance. 
End-to-end 
training  of  selection  and  detection 
components  ensures  selected  features  specifically 
support the downstream anomaly detection task rather 
than  general  predictive  power.  This  task-specific 
selection improves detection performance compared to 
generic filter or wrapper methods.

removable

4. Threshold Optimization for Early Warning 
Mechanism

4.1. Adaptive Threshold Setting Strategies

Statistical Threshold Determination

Threshold optimization for anomaly detection balances 
sensitivity requirements against operational constraints 
including  investigative  capacity  and  alert  fatigue. 
Statistical  approaches  establish  thresholds  based  on 
distributional  properties  of  anomaly  scores  computed 
from  historical  data.  Percentile-based  thresholds  flag 
providers  whose  anomaly  scores  exceed  specified 
quantiles  of  the  score  distribution.  Common  choices 
include  the  95th  or  99th  percentiles  corresponding  to

Vol. 6(4), pp. 27-49, April 2026  
[37]

---

<!-- PAGE 12 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

levels.  The  determination 
traditional  significance 
process  computes  empirical  score  distributions  from 
training  data  spanning  multiple  billing  cycles. 
Thresholds are set to achieve target false positive rates 
based on historical fraud prevalence. Providers scoring 
above thresholds receive priority for investigation based 
on their deviation from normal patterns.

Standard deviation-based thresholds  define  anomalous 
scores as those exceeding the mean by multiple standard 
deviations.  The three-sigma  rule  marks  scores  beyond 
three standard deviations as anomalies under Gaussian 
distribution assumptions. This approach requires careful 
evaluation of distribution assumptions, as heavy-tailed 
score  distributions  common  in  anomaly  detection 
contexts  violate  normality.  Robust  variants  employ 
median  absolute  deviation  (MAD)  as  an  alternative 
scale  estimate  resistant  to  outliers.  The  determination 
framework  tests  distributional  assumptions  through 
goodness-of-fit  analyses  and  selects  appropriate 
score 
threshold 
including 
distributions.

formulas  matching

observed

Power

logarithmic  or  Box-Cox  transformations  normalize 
skewed  score  distributions 
threshold 
calibration.

improve

to

scores

and  derives

Extreme  value  theory  provides  principled  approaches 
for  setting  thresholds  in  tail  regions  where  fraud 
typically  occurs.  Generalized  Pareto  distributions 
(GPD)  model  exceedances  over  high  thresholds.  The 
methodology  estimates  distribution  parameters  from 
observed  high 
thresholds 
corresponding  to  desired  false  positive  rates  in  tail 
regions. 
identify 
Peak-over-threshold  methods 
appropriate 
levels  for  parameter 
estimation by analyzing mean residual life plots. Return 
level  calculations  determine  scores  exceeded  with 
specified  probabilities,  enabling  threshold  selection 
based  on  risk  tolerance.  This  sophisticated  approach 
properly accounts for tail behavior critical for detecting 
rare  but  high-impact  fraud  events.  Table  6  compares 
statistical threshold determination methodologies across 
multiple evaluation criteria.

threshold

initial

transformations 
Table 6: Statistical Threshold Determination Methods Comparison

Method

Threshold Formula

Assumptions

Robustness

95th Percentile

Q_0.95

None (empirical)

High

Three Sigma Rule

μ + 3σ

Gaussian distribution

Low (sensitive to outliers)

Median 
Deviation

Absolute

median + k·MAD

Symmetric 
distribution

High (robust to outliers)

Extreme Value Theory

Based 
parameters

on

GPD

Tail follows GPD

Medium  (requires  sufficient  tail 
data)

Box-Cox Transformation  Transform  then  apply  σ

rule

Data 
normalized

can

be

Medium 
transformation)

(depends

on

Cost-sensitive Threshold Optimization

into

explicitly

approaches

losses  proportional

incorporate 
Cost-sensitive 
threshold 
asymmetric  misclassification  costs 
selection. False negatives represent missed fraud cases 
to  fraudulent  claim 
incurring 
amounts.  False  positives  consume 
investigative 
resources  without  recovery  benefits.  The  optimization 
as 
framework 
minimizing  expected  cost  combining  fraud  losses  and 
investigation  costs.  Cost  matrices  define  penalties  for 
different  error  types  based  on  average  fraud  amounts 
and  investigation  resource  requirements.  Threshold 
determination  procedures  evaluate  expected  costs 
across candidate threshold values and select thresholds 
minimizing  total  expected  cost.  Sensitivity  analyses

formulates

threshold

selection

assess cost-optimal threshold stability across ranges of 
assumed cost parameters.

into

Linear

capacity

threshold

investigative

fraud  detection

thresholds 
Budget-constrained  optimization  selects 
respecting 
limits.  The 
methodology  incorporates  constraints  on  maximum 
selection 
investigation  volumes 
formulations 
procedures. 
resource 
to 
maximize 
constraints. Threshold selection operates in conjunction 
with alert prioritization to ensure investigation budgets 
framework 
target 
algorithms 
implements 
efficiently solving large-scale constrained optimization 
problems.  Lagrangian  relaxation  techniques  convert 
hard  constraints  into  penalty  terms  enabling  gradient-

providers.  The 
programming

programming 
subject

highest-risk

dynamic

Vol. 6(4), pp. 27-49, April 2026  
[38]

---

<!-- PAGE 13 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

based  optimization.  Multi-objective  optimization 
addresses trade-offs between detection performance and 
resource consumption through Pareto frontier analysis.

by

vary

thresholds

Risk-adjusted 
provider 
characteristics  including  specialty,  practice  size,  and 
geographic location. The optimization process stratifies 
providers into homogeneous subgroups and establishes 
group-specific  thresholds.  This  approach  accounts  for 
legitimate  practice  variation  across  provider  types 
reducing false positives from specialty-specific patterns. 
Hierarchical  modeling  estimates  group-level  and 
provider-level  parameters  simultaneously 
through 
partial  pooling.  Shrinkage  estimation  balances  group 
averages with individual provider data to obtain stable 
threshold estimates even for small provider subgroups. 
The  stratified  threshold  framework  requires  careful 
management  of  threshold  proliferation  to  maintain 
operational 
relevant 
heterogeneity.

simplicity  while  capturing

Machine Learning-based Threshold Learning

Machine  learning  approaches  learn  optimal  thresholds 
directly  from  historical  detection  outcomes.  Meta-
learning  frameworks  treat  threshold  selection  as  a 
supervised 
learning  problem  predicting  optimal 
thresholds  from  data  characteristics  and  performance 
feedback.  Training  datasets  comprise  historical 
threshold  settings  and  corresponding  performance 
metrics  across  diverse  data  conditions.  Random  forest 
regressors predict optimal thresholds for new data based 
on  statistical  properties  including  score  distributions, 
fraud  prevalence,  and  operational  constraints.  The 
learning  framework  continuously  updates  threshold 
models incorporating recent performance data enabling 
adaptation  to  changing  fraud  patterns  and  operational 
conditions.

Reinforcement  learning  formulates  threshold  selection 
as  sequential  decision-making  under  uncertainty.  The 
agent  observes  current  system  state  including  recent 
alert  volumes,  investigation  outcomes,  and  fraud 
statistics.  Actions  consist  of  threshold  adjustments 
increasing or decreasing sensitivity. Rewards combine 
detection  performance  metrics  with  operational 
efficiency  measures.  Q-learning  algorithms 
learn 
optimal  threshold  policies  maximizing  cumulative 
rewards  over  time.  Policy  gradient  methods  directly 
optimize  parameterized  threshold  functions  through 
gradient ascent on expected rewards. Experience replay 
stabilizes  learning  by  reusing  historical  state-action-
reward tuples during training.

triggers

Online learning enables continuous threshold adaptation 
as  new  fraud  cases  and 
investigation  outcomes 
accumulate.  Stochastic  gradient  descent  updates 
threshold  parameters  based  on  mini-batches  of  recent 
data.  Adaptive  learning  rates  including  AdaGrad  and 
Adam  optimize  convergence  speed  and  stability. 
Concept  drift  detection 
threshold 
recalibration  when  statistical  tests  identify  significant 
distribution  shifts.  The  online  learning  framework 
maintains  computational  efficiency  suitable  for  real-
time 
update 
through 
procedures requiring minimal computation per update. 
Exponential  forgetting  weights  emphasize  recent 
observations while retaining long-term stability through 
gradual  decay  of  historical  influence.  This  adaptive 
approach  maintains  detection  effectiveness  as  fraud 
tactics evolve and operational environments change.

deployment

incremental

rapid

Figure  3  illustrates  the  relationship  between  detection 
thresholds and operational performance metrics across a 
range of threshold values.

Figure 3: Threshold Performance Trade-off Curves

Vol. 6(4), pp. 27-49, April 2026  
[39]

---

<!-- PAGE 14 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

line  graph  displays

four  key 
This  multi-curve 
performance  metrics  as  functions  of  anomaly  score 
threshold values ranging from 0.1 to 0.9 on the x-axis. 
The primary y-axis on the left shows detection rate (blue 
solid  line)  and  false  positive  rate  (red  solid  line)  both 
ranging from 0 to 1.0. The secondary y-axis on the right 
displays daily investigation volume (green dashed line, 
ranging 0-500 cases) and estimated cost savings (purple 
dotted line, ranging 0-10 million dollars). The detection 
rate  curve  demonstrates  expected  monotonic  decrease 
from 0.98 at threshold 0.1 to 0.45 at threshold 0.9, with 
the  steepest  decline  occurring  between  thresholds  0.3 
and  0.5.  The  false  positive  rate  exhibits  similar 
decreasing behavior dropping from 0.35 at threshold 0.1 
to  0.02  at  threshold  0.9.  Investigation  volume  closely 
tracks false positive rate, ranging from 450 daily cases 
at  low  thresholds  to  15  cases  at  high  thresholds.  Cost 
savings  curve  shows  a  characteristic  inverted  U-shape 
peaking  at  8.2  million  dollars  at  threshold  0.60, 
representing the optimal balance point where detection 
benefits  exceed 
investigation  costs.  This  peak 
corresponds  to  a  detection  rate  of  0.79,  false  positive 
rate of 0.03, and investigation volume of 64 cases per 
day. Shaded regions indicate 95% confidence intervals 
derived  from  bootstrap  resampling,  with  widening 
intervals  at  extreme 
reflecting 
increased  uncertainty.  Vertical  reference  lines  mark 
three  operating  points:  conservative  threshold  at  0.65 
prioritizing  specificity,  balanced  threshold  at  0.60 
maximizing  cost  savings,  and  aggressive  threshold  at 
0.25  prioritizing  sensitivity.  The  visualization  enables 
stakeholders  to  visualize  multi-dimensional  trade-offs 
inherent  in  threshold  selection  and  select  operating 
points  aligned  with  organizational  priorities  regarding 
detection  coverage,  investigation  capacity,  and  cost-
effectiveness.

threshold  values

4.2. Trade-off Analysis Between False Positives and 
False Negatives

ROC Curve Analysis and Optimal Operating Points

Receiver  operating  characteristic  curves  provide 
comprehensive  visualization  of  detection  trade-offs 
across  all  possible 
threshold  values.  The  ROC 
framework plots true positive rate against false positive 
rate as threshold varies from most to least conservative. 
Area  under  the  ROC  curve  (AUC-ROC)  quantifies 
overall  detection  capability  independent  of  specific 
threshold choices. Perfect detectors achieve AUC of 1.0 
while random guessing yields AUC of 0.5. The analysis 
compares  multiple  detection  algorithms  and  temporal 
feature  sets  through  AUC  comparisons.  Partial  AUC 
metrics focus evaluation on clinically relevant operating 
regions  with  acceptable  false  positive  rates.  DeLong 
tests assess statistical significance of AUC differences 
between competing approaches.

Optimal  operating  point  selection  from  ROC  curves 
cost 
depends

operational

objectives

and

on

considerations. The Youden index maximizes the sum 
of  sensitivity  and  specificity,  identifying  thresholds 
where vertical distance from the diagonal reference line 
reaches maximum. This approach treats false positives 
and false negatives equally. Alternative criteria weight 
error  types  differently.  The  closest-to-corner  criterion 
minimizes  Euclidean  distance 
the  perfect 
classification point at coordinates (0,1). Cost-weighted 
distance 
asymmetric 
misclassification  costs  through  appropriate  distance 
function modifications. The analysis framework enables 
interactive  exploration  of 
threshold  options  with 
immediate visualization of corresponding performance 
metrics.

incorporate

metrics

from

Precision-recall 
(PR)  curves  provide  alternative 
performance visualization emphasizing behavior under 
class imbalance. Precision measures positive predictive 
value  while  recall  equals  sensitivity.  PR  curves  better 
capture  performance  characteristics  relevant  for  fraud 
detection  where  anomalies  represent  small  minorities. 
Average  precision  summarizes  PR  curve  performance 
through  weighted  average  of  precision  values  at  each 
threshold.  The  F-beta  score  generalizes  the  F1  score 
through adjustable balance between precision and recall. 
Beta  values  less  than  one  emphasize  precision  while 
values exceeding one prioritize recall. The optimization 
framework  selects 
thresholds  maximizing  chosen 
performance  metrics  subject  to  operational  constraints 
on investigation volumes and acceptable false positive 
rates.

Cost-benefit Analysis Framework

fraud

prevent

identifications

Quantitative  cost-benefit  analysis  translates  detection 
performance  into  financial  terms  enabling  business-
oriented  threshold  selection.  The  framework  assigns 
monetary values to different detection outcomes. True 
positive 
losses 
proportional to typical fraudulent claim amounts. False 
positive  investigations  incur  costs  reflecting  resource 
consumption  without 
recovery.  False  negatives 
represent missed fraud accumulating undetected losses. 
True negatives correctly classified legitimate providers 
consume  no  investigation  resources.  The  analysis 
computes  expected  costs  or  net  benefits  for  candidate 
thresholds by combining detection rates with outcome 
valuations.  Optimal thresholds maximize  expected  net 
benefit balancing fraud prevention against investigation 
expenses.

threshold  robustness 
Sensitivity  analysis  explores 
across 
ranges  of  cost  assumptions.  Parameter 
uncertainty  regarding  average  fraud  amounts  and 
investigation  costs  necessitates  evaluation  across 
plausible value ranges. Monte Carlo simulation samples 
cost  parameters  from  specified  distributions  and 
computes  optimal 
sample. 
thresholds 
Distribution  of  optimal  thresholds  across  simulations 
quantifies  selection  uncertainty  attributable  to  cost

for  each

Vol. 6(4), pp. 27-49, April 2026  
[40]

---

<!-- PAGE 15 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

estimation  errors.  Robust  thresholds  perform  well 
across  broad  parameter  ranges  providing  stability 
against  cost  misspecification.  Scenario  analysis 
evaluates  thresholds  under  discrete  alternative  cost 
assumptions  representing  optimistic,  realistic,  and 
pessimistic  projections.  Break-even  analysis  identifies 
conditions  under  which  different  threshold  strategies 
achieve cost equivalence.

Long-term  value  considerations  incorporate  dynamic 
aspects of fraud  detection including  deterrence effects 
and recovery potential. Successful fraud detection may 
deter  future  fraudulent  activity  through  perceived 
enforcement  risk.  The  valuation  framework  models

efforts

following

through  reduced  future  fraud 
deterrence  benefits 
prevalence.  Recovery 
fraud 
identification  recoup  portions  of  losses  through  civil 
actions  or  criminal  prosecution.  Expected  recovery 
amounts depend on provider assets and legal framework 
characteristics.  Time  value  of  money  considerations 
discount 
The 
aggregates 
comprehensive 
cost-benefit  model 
immediate  detection  benefits  with 
longer-term 
deterrence  and  recovery  effects  providing  holistic 
threshold  optimization  accounting  for  full  program 
impact beyond immediate operational metrics. Table 7 
presents detailed cost-benefit calculations for threshold 
selection.

appropriately.

benefits

future

Table 7: Cost-Benefit Analysis for Threshold Selection

Threshold  Detection

Rate

False  Positive 
Rate

Annual 
Prevented ($M)

Fraud

Investigation  Cost 
($M)

Net  Benefit 
($M)

0.30

0.45

0.60

0.75

0.92

0.87

0.79

0.68

0.15

0.06

0.03

0.01

442.0

418.0

379.5

326.6

Multi-objective Optimization Approaches

addresses

Multi-objective  optimization 
threshold 
selection  as  simultaneous  optimization  of  multiple 
rate 
potentially  conflicting  objectives.  Detection 
maximization  conflicts  with 
rate 
false  positive 
Investigation 
constraints 
volume 
minimization. 
compete  with 
reduction  goals.  The 
loss 
fraud 
optimization  framework  formulates  these  as  distinct 
objective functions requiring joint consideration. Pareto 
efficiency  concepts  identify  threshold  solutions  where 
no objective can improve without degrading others. The 
Pareto frontier traces optimal trade-off surfaces in multi-
dimensional  objective  space.  Decision-makers  select 
final thresholds from Pareto-optimal alternatives based 
on  subjective  preference  weights  across  objectives. 
Interactive  visualization  tools  enable  exploration  of 
Pareto 
threshold 
selection.

supporting

informed

frontiers

Scalarization methods convert multi-objective problems 
into  single-objective  formulations  through  weighted 
combinations  of  objectives.  Linear  scalarization  sums 
weighted  objective  values  with  weights  reflecting 
scalarization 
relative 
minimizes  maximum  weighted  deviation  from  ideal 
objective  values.  Reference  point  methods  specify 
desired  performance  levels  for  each  objective  and

importance.  Achievement

319.5

127.8

63.9

21.3

122.5

290.2

315.6

305.3

minimize  distance  from  these  aspirations.  Different 
weight specifications generate different Pareto-optimal 
solutions  enabling  systematic  exploration  of 
the 
frontier.  Evolutionary  multi-objective  optimization 
algorithms  including  Non-dominated  Sorting  Genetic 
Algorithm  II  (NSGA-II)  maintain  populations  of 
candidate  solutions  evolving  toward  Pareto-optimal 
regions. 
approaches 
simultaneously  discover  multiple  efficient  solutions 
providing comprehensive threshold options.

population-based

These

such

handles

optimization

as  mandatory  detection

Lexicographic 
objective 
hierarchies  by  optimizing  objectives  sequentially 
according to priority orderings. Primary objectives are 
optimized  first  with  secondary  objectives  considered 
only  among  solutions  optimal  for  primary  objectives. 
This  approach  suits  contexts  with  clear  priority 
structures, 
rate 
requirements  followed  by  cost  minimization  within 
compliant  solutions.  Satisficing  frameworks  establish 
minimum  acceptable 
for  each  objective, 
levels 
restricting optimization to feasible regions satisfying all 
constraints.  Multi-attribute  utility 
theory  provides 
formal frameworks for aggregating multiple objectives 
through  utility  functions  encoding  decision-maker 
preferences.  The  elicitation  process  determines  utility 
function  parameters  through  preference  elicitation

Vol. 6(4), pp. 27-49, April 2026  
[41]

---

<!-- PAGE 16 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

procedures including pairwise comparisons and lottery 
assessments.  Resulting  utility 
enable 
principled 
threshold  selection  maximizing  overall 
utility.

functions

4.3. Dynamic Threshold Adjustment Algorithms

Concept Drift Detection and Response

fraud

tactics

evolution  of

Concept drift occurs when statistical properties of fraud 
time,  degrading  detection 
patterns  change  over 
performance  of  models  trained  on  historical  data. 
Temporal 
requires 
corresponding 
threshold  adjustments  maintaining 
detection  effectiveness.  Drift  detection  algorithms 
monitor  performance  metrics  and  statistical  properties 
to identify significant distribution shifts. Page-Hinkley 
test tracks cumulative sums of performance deviations 
from  expected 
triggering  alarms  when 
cumulative  deviations  exceed  control  limits.  The 
detection  framework  establishes  baseline  performance 
during initial deployment and tracks deviations through 
statistical process control charts. Control limits based on 
historical  variation  define  normal  performance  ranges 
with  exceedances  indicating  potential  drift  requiring 
threshold recalibration.

levels,

Statistical  distance  measures  quantify  distribution 
divergence  between  current  and  reference  periods. 
Kullback-Leibler  divergence  computed  from  recent 
anomaly score distributions compared against historical 
references  detects  significant  shifts.  Kolmogorov-
Smirnov  tests  assess  differences  between  cumulative 
distribution  functions  providing  nonparametric  drift 
detection.  The  monitoring  system  computes  these 
statistics over rolling windows and triggers recalibration 
when  divergence  exceeds  predetermined  thresholds. 
Adaptive windowing balances responsiveness to recent 
changes  against  stability  provided  by  larger  sample 
sizes.  Exponentially  weighted  statistics  emphasize 
recent observations while retaining longer-term context. 
The  drift 
threshold 
reoptimization  using  recent  data  when  drift  signals 
activate.

response  protocol

initiates

to

drift

detection

combines  multiple 
Ensemble 
complementary  detection  methods 
improve 
robustness  and  reduce  false  alarms.  Voting  schemes 
aggregate binary drift signals from individual detectors, 
declaring  drift  when  majorities  agree.  Confidence-
weighted  aggregation  weighs  detector  votes  by  their 
historical  reliability.  Sequential  hypothesis  testing 
frameworks including Sequential Probability Ratio Test 
(SPRT)  evaluate  evidence  accumulation  for  drift 
hypotheses, stopping when confidence reaches decision 
thresholds.  The  ensemble  approach  provides  earlier 
detection through sensitive methods while maintaining 
low  false  alarm  rates  through  conservative  methods. 
Meta-learning  algorithms 
learn  optimal  detector 
combinations and aggregation strategies from historical

drift  episodes.  Periodic  retraining  schedules  provide 
fallback recalibration even absent explicit drift signals 
ensuring continued performance.

Feedback-driven Threshold Adaptation

False

adequate

sensitivity

sensitivity.

Investigation  outcomes  provide  valuable  feedback  for 
threshold refinement. Each investigated case labeled as 
fraudulent  or  legitimate  updates  knowledge  about 
detection  algorithm  behavior.  Confirmed  fraud  cases 
misclassified  as  normal  indicate  threshold  settings 
lacking 
positive 
investigations  flagging  legitimate  providers  suggest 
excessive 
relaxation.  The 
adaptation mechanism tracks recent false positive rates 
comparing against target levels established during initial 
calibration.  Proportional-Integral-Derivative 
(PID) 
control  algorithms  adjust  thresholds  proportionally  to 
discrepancies between observed and target false positive 
rates. Integral control components accumulate historical 
errors  preventing  persistent  biases.  Derivative  control 
terms  respond  to  rate  of  change  in  performance 
preventing oscillation.

requiring

these

refined

outcomes

constitute

updating 
reflect

Bayesian updating provides principled frameworks for 
incorporating investigation feedback. Prior distributions 
encode initial threshold beliefs based on training data. 
Investigation 
likelihood 
beliefs.  Posterior 
information 
distributions 
threshold  knowledge 
combining  prior 
information  with  accumulating 
evidence.  The  adaptation  process  samples  thresholds 
from  posterior  distributions  enabling  probabilistic 
threshold  selection.  Sequential  Bayesian  updating 
naturally  handles  streaming  feedback  as  investigation 
outcomes arrive. Conjugate prior specifications enable 
closed-form  posterior  updates  ensuring  computational 
efficiency.  Non-conjugate  cases  employ  variational 
approximations or Markov chain Monte Carlo (MCMC) 
sampling.  The  probabilistic 
framework  provides 
confidence  intervals  quantifying  threshold  uncertainty 
decreasing as evidence accumulates.

Active learning strategies optimally select investigation 
targets  to  maximize  information  gain  for  threshold 
refinement.  Uncertainty  sampling  prioritizes  providers 
with  anomaly  scores  near  current  thresholds  where 
classification  uncertainty  peaks.  Query-by-committee 
approaches  investigate  cases  exhibiting  disagreement 
among  ensemble  members.  Expected  error  reduction 
criteria  estimate  potential  performance  improvements 
investigating  specific  cases.  The  adaptive 
from 
investigation  protocol  balances  exploitation  of  current 
knowledge through high-confidence fraud cases against 
exploration  of  uncertain  boundary  regions.  Budget 
constraints limit investigation capacity requiring careful 
selection of most informative cases. The feedback loop 
accelerates  threshold  convergence  to  optimal  settings 
through  strategic  information  acquisition  reducing 
calibration time and resource requirements.

Vol. 6(4), pp. 27-49, April 2026  
[42]

---

<!-- PAGE 17 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

Context-aware Threshold Adjustment

threshold  settings.  Seasonal  patterns

Contextual factors, including temporal periods, provider 
characteristics,  and  operational  conditions,  influence 
in 
optimal 
threshold 
legitimate  healthcare  utilization  require 
adaptation  across  calendar  periods.  Winter  influenza 
seasons  increase  claim  volumes  requiring  threshold 
relaxation  to  maintain  specificity.  Summer  vacation 
periods 
threshold 
tightening. The adjustment framework applies seasonal 
multiplicative  factors  that  scale  baseline  thresholds 
based  on  expected  claim  volume  patterns.  Holiday 
periods  and  weekend  days  may  motivate  specialized 
threshold  configurations,  depending  on  observed 
utilization patterns and operational staffing levels. The 
temporal  adaptation  maintains  consistent  detection 
performance despite predictable cyclical variations.

activity  necessitating

reduce

Provider  stratification  enables  customized  thresholds 
matching 
specific  characteristics.  Specialty-based 
thresholds  account  for  legitimate  practice  pattern 
differences  across  medical  disciplines.  High-volume 
specialties, such as emergency medicine, tolerate higher 
absolute  claim  volumes  than  low-volume  specialties, 
such  as  neurosurgery.  Geographic  adjustments  reflect 
regional  variation  in  practice  patterns  and  patient 
demographics. Urban providers exhibit different billing 
rhythms  than  rural  practices.  Practice  size  factors 
large  group 
distinguish  solo  practitioners

from

practices,  which  naturally  have  higher  aggregate 
volumes.  The  stratification  methodology  clusters 
relevant  characteristics  and 
providers  based  on 
establishes  group-specific 
thresholds  via  separate 
optimization procedures. Hierarchical modeling enables 
partial pooling of information across strata, stabilizing 
threshold estimates for small provider groups.

trigger

loosening,

enforcement

Operational  context,  including  investigation  capacity 
and 
threshold 
drives 
priorities, 
resource-constrained  periods, 
adjustments.  During 
thresholds must be tightened to maintain investigation 
limits.  Surplus  capacity 
volumes  within  capacity 
enables 
increasing  detection 
threshold 
breadth. Enforcement initiatives targeting specific fraud 
types 
threshold  adjustments  emphasizing 
relevant  detection  signatures.  Emergency  situations, 
including  pandemic 
rapid 
threshold reconfiguration, accommodating dramatically 
altered healthcare delivery patterns. The context-aware 
framework  implements  rule-based  logic  that  encodes 
institutional  knowledge  of  appropriate 
threshold 
responses  for  various  operational  scenarios.  Machine 
learning  components  learn  adaptation  policies  from 
historical  context-performance  relationships,  enabling 
data-driven threshold adjustments. Table 8 summarizes 
the  dynamic  threshold  adjustment  methodology  and 
performance outcomes.

responses,  necessitate

Table 8: Dynamic Threshold Adjustment Methodology Performance

Adaptation Strategy

Average 
Rate

Detection

FPR  Stability 
Dev)

(Std

Drift  Response  Time 
(days)

Fixed Threshold

0.73 (degrading)

Periodic Recalibration

PID Controller

Bayesian Updating

Proposed 
Framework

Adaptive

0.81

0.84

0.85

0.87

0.048

0.032

0.024

0.021

0.018

N/A

30.0

12.5

10.2

8.3

Figure 4 visualizes the temporal evolution of detection 
thresholds  under  the  adaptive  adjustment  framework 
over a twelve-month deployment period.

Vol. 6(4), pp. 27-49, April 2026  
[43]

---

<!-- PAGE 18 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

Figure 4: Adaptive Threshold Evolution and Performance Tracking

This  multi-panel  time-series  visualization  displays  the 
coordinated  evolution  of 
threshold  settings  and 
corresponding performance metrics over 12 months of 
operational  deployment.  The  top  panel  shows  the 
adaptive  threshold  trajectory  (blue  line)  starting  at  an 
initial  setting  of  0.50  and  dynamically  adjusting 
between  0.35  and  0.65  in  response  to  performance 
feedback and concept drift signals. Notable adjustment 
episodes  include:  a  sharp  decrease  to  0.38  during 
months 2-3, responding to elevated false negative rates, 
a gradual increase from 0.40 to 0.58 during months 5-7, 
reducing excessive false positive volumes, and a rapid 
decrease to 0.42 in month 9 following detection of new 
fraud pattern emergence. Gray-shaded regions indicate 
concept  drift  episodes  detected  by  the  monitoring 
system, with drift intensity proportional to the shading 
darkness. The middle panel tracks four key performance 
metrics:  detection  rate  (green  line,  range  0.75-0.92), 
false positive rate (red line, range 0.05-0.18), precision 
(purple line, range 0.42-0.68), and F1 score (orange line, 
range  0.51-0.74).  Horizontal  dashed  reference  lines 
mark  target  performance  levels,  including  minimum 
acceptable detection rate at 0.80 and maximum tolerable 
false  positive  rate  at  0.10.  The  bottom  panel  displays 
daily  investigation  volume  (blue  bars,  range  50-180 
cases) compared against available investigative capacity 
(red  horizontal  line  at  120  cases  per  day).  Yellow 
shading  indicates  periods  of  capacity  constraint  when

investigation  demand  exceeds  availability,  triggering 
threshold  tightening  responses.  Green  shading  marks 
surplus capacity  periods  enabling threshold loosening. 
Throughout the deployment period, the adaptive system 
maintains performance within acceptable ranges despite 
multiple drift events and varying operational conditions. 
The visualization demonstrates the effectiveness of the 
the 
threshold  adjustment  algorithm 
competing  objectives  of  detection  sensitivity,  false-
positive control, and operational feasibility. Annotation 
boxes highlight key decision points, including Month 3 
threshold decrease, improving detection rate from 0.78 
to  0.85,  Month  6  threshold  increase,  reducing  false 
positive  rate  from  0.15  to  0.08  while  maintaining 
detection rate above 0.80, and Month 9 rapid response 
to  emerging  fraud  pattern,  preventing  performance 
degradation.

in  balancing

5. Experimental Evaluation and Discussion

5.1. Experimental Setup and Dataset Description

The  experimental  evaluation  used  de-identified 
Medicare  Part  B  claims  data  spanning  a  three-year 
period from 2020 through 2022. The dataset comprises 
47.3  million  claims  submitted  by  892,450  healthcare 
providers  across  all  fifty  states  and  the  District  of 
Columbia.  Ground  truth  fraud  labels  were  established

Vol. 6(4), pp. 27-49, April 2026  
[44]

---

<!-- PAGE 19 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

population,

by  integrating  confirmed  investigation  outcomes  from 
the Centers for Medicare & Medicaid Services Office of 
Inspector General Exclusions Database and Department 
of  Justice  settlements  published  through  December 
2022.  The  labeled  subset  contains  3,845  confirmed 
fraudulent  providers  representing  0.43%  of  the  total 
provider 
fraud 
prevalence  in  operational  settings.  Claims  records 
include  temporal  attributes  such  as  service  dates, 
submission  dates,  and  processing  dates,  along  with 
provider  identifiers,  beneficiary  identifiers,  procedure 
codes  represented  using 
the  Current  Procedural 
Terminology  (CPT)  coding  system,  diagnosis  codes 
using the International Classification of Diseases, Tenth 
Revision (ICD-10) format, and reimbursement amounts 
in US dollars.

reflecting

realistic

label  construction  followed  strict

Data  preprocessing  involved  constructing  temporal 
sequences  and  organizing  claims  chronologically  by 
provider  and  beneficiary.  Claims  occurring  within 
ninety-day  windows  were  aggregated  into  episodes 
representing  coherent  treatment  sequences.  Ground 
truth 
temporal 
alignment  rules:  provider  fraud  labels  were  assigned 
based on investigation completion dates, with all claims 
submitted before the investigation initiation date labeled 
according  to  provider  status,  while  excluding  claims 
during  investigation  periods  to  prevent  label  leakage. 
Feature  engineering  pipelines  extracted  127  distinct 
temporal 
the  methodologies 
including 
described  in  Section  3.  Statistical  features  captured 
distributional  characteristics  of  claim  frequencies, 
service  intervals,  and  submission  patterns.  Functional 
principal  component  analysis  generated  15  trajectory 
features  representing  dominant 
temporal  variation 
modes.  LSTM  autoencoder  embeddings  yielded  128 
learned features, which were subsequently reduced to 32 
principal  features,  preserving  95%  of  the  variance. 
Feature selection procedures using mutual information-
based  ranking  reduced  the  total  dimensionality  to  45 
features,  balancing  detection  performance  with 
interpretability 
computational 
requirements.

efficiency

features,

and

Evaluation  methodology  employed  stratified  five-fold 
cross-validation,  preserving  fraud  prevalence  ratios 
across  folds.  Each  fold  contained  approximately 
178,490  providers  with  769  confirmed  fraud  cases. 
Training folds were used for feature extraction, model 
calibration,  and  threshold  optimization.  Held-out  test 
folds were used to evaluate detection performance and 
generalization. Performance metrics included detection 
rate (sensitivity), false positive rate, precision (positive 
predictive  value),  F1  score,  and  area  under  the  ROC 
curve.  Statistical  significance  testing  employed  the 
DeLong  test  for  AUC  comparisons and  the  McNemar 
test  for  paired  classification  results.  Computational 
experiments  utilized  a  high-performance  computing 
cluster with 96-core Intel Xeon processors and 512GB

RAM, enabling parallel processing of large-scale claims 
datasets.  The  parallelization 
strategy  processes 
providers  independently  across  48  worker  threads, 
achieving  an  aggregate  throughput  of  approximately 
15,000 provider evaluations per hour, with an average 
latency  of  2.4  seconds, 
per-provider  processing 
including feature extraction, scoring, and result logging.

5.2. Performance Comparison of Feature 
Engineering Approaches

the  proposed

Comparative  evaluation  assessed  multiple  feature 
engineering  strategies,  including  baseline  approaches 
temporal  framework.  Baseline 
and 
methods  used  simple  statistical  features,  such  as  total 
claim  counts,  average  claim  amounts,  and  billing 
frequency,  without  sophisticated  temporal  analysis. 
Traditional  RFM  features,  adapted  from  marketing 
analytics  computed  recency,  frequency,  and  monetary 
metrics.  The  proposed  temporal  feature  engineering 
framework,  incorporating  claim  timestamp  analysis, 
service  interval  patterns,  and  frequency  distribution 
characterization, demonstrated substantial performance 
improvements. Detection rates improved from 0.73 for 
baseline  features  to  0.87  for  the  complete  temporal 
feature set. False positive rates decreased from 0.14 to 
0.06, maintaining operational feasibility. The area under 
the ROC curve increased from 0.84 to 0.93, indicating 
significantly 
between 
fraudulent and legitimate providers.

discrimination

improved

Ablation  studies  isolated  contributions  of  individual 
feature  categories.  Removing  the  claim  timestamp 
features decreased the detection rate from 0.79 to 0.78, 
demonstrating their critical importance. Service interval 
features  contributed  a  0.05-point  improvement  in 
detection  rate.  Frequency  distribution  characteristics 
added  0.04  detection  rate  gains.  LSTM  autoencoder 
embeddings provided 0.06 improvement over statistical 
features alone, justifying their computational overhead 
through  substantial  performance  gains.  Functional 
principal  component  features  contributed  a  0.03 
increase in detection rate. The synergistic combination 
of multiple feature types achieved superior performance 
compared  to  any  individual  category,  validating  the 
comprehensive temporal feature engineering framework 
design philosophy.

Feature  importance  analysis  using  random  forest 
importance  scores  identified  the  most  discriminative 
temporal  features.  Service-to-submission  lag  standard 
deviation  ranked  highest  with  an  importance  score  of 
0.089,  capturing  providers  with  inconsistent  billing 
timing. The weekend submission ratio ranked second at 
0.077,  indicating  unusual  operational  patterns.  The 
claim  frequency  coefficient  of  variation  achieved  an 
importance  of  0.071,  detecting  providers  with  erratic 
billing  volumes.  Autocorrelation  at  a  7-day  lag  was

Vol. 6(4), pp. 27-49, April 2026  
[45]

---

<!-- PAGE 20 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

0.068,  revealing  an  artificial  weekly  periodicity  in 
fraudulent  billing.  The  FPCA’s 
first  principal 
component achieved an importance of 0.064, capturing 
dominant  trajectory  patterns.  These  findings  inform 
feature prioritization for real-time deployment scenarios 
requiring  computational  efficiency  through  selective 
feature calculation.

5.3. Threshold Strategy Evaluation and Practical 
Implications

including

The  threshold  optimization  methodology  evaluated 
multiple  approaches, 
fixed  percentile 
thresholds,  statistical  thresholds  based  on  standard 
deviations,  cost-sensitive  optimization,  and 
the 
proposed  adaptive  adjustment  framework.  Fixed  95th 
percentile thresholds achieved  a detection rate of 0.81 
and a false-positive rate of 0.09. Statistical three-sigma 
thresholds yielded a detection rate of 0.78 and a false-
positive  rate  of  0.11.  Cost-sensitive  optimization 
incorporating 
costs 
improved the detection rate to 0.84 while maintaining a 
false  positive  rate  of  0.08.  The  adaptive  adjustment 
framework achieved an optimal balance with a detection 
rate  of  0.87  and  a  false  positive  rate  of  0.06, 
outperforming  static  approaches  through  continuous 
calibration  based  on  operational  feedback.  The  cost-
benefit analysis identified threshold 0.60 as maximizing 
net  benefit  at  8.2  million  dollars  annually,  consistent 
with  the  Figure  3  visualization,  which  shows  this 
threshold achieving a detection rate of 0.79 and a false 
positive rate of 0.03, as documented in Table 7.

asymmetric  misclassification

Temporal 
threshold 
stability  analysis  evaluated 
performance over extended deployment periods. Fixed 
thresholds  exhibited  gradual  performance  degradation 
as  fraud  patterns  evolved,  and  concept  drift  occurred. 
Detection  rates  declined  by  0.12  over  12  months  for 
static thresholds, while false-positive rates increased by 
0.05.  The  adaptive  framework  maintained  stable 
performance 
recalibration 
responding  to  drift  signals.  Detection  rates  fluctuated 
within a 0.03 range around a mean of 0.87, while false 
positives  remained  within  0.02  of  the  target  0.06. 
Concept  drift  detection  successfully  identified  four 
major  distribution  shifts  during  the  evaluation  period, 
triggering  appropriate  threshold  adjustments.  Average 
adjustment  latency  measured  8.3  days  from  drift 
occurrence to corrective threshold modification.

continuous

through

efficiency,

deployment

considerations

interpretability,

include 
Practical 
computational 
and 
integration with existing investigation workflows. The 
temporal  feature  engineering  framework  processes 
approximately  15,000  provider  updates  per  hour  on 
real-time 
standard 
requirements,  achieved  through  parallel  processing  of 
48  concurrent  provider  evaluations  each  requiring  an

hardware  meeting

server

average of 2.4 seconds for complete feature extraction 
and scoring pipeline. The 2.4-second feature extraction 
latency per provider enables daily batch processing of 
the  entire  provider  population  within  operational  time 
windows. Threshold optimization procedures execute in 
under  five  minutes,  enabling  frequent  recalibration. 
Investigation  prioritization  ranks  flagged  providers  by 
anomaly scores facilitating efficient resource allocation. 
interpretable 
Explanation 
supporting 
descriptions  of 
investigator decision-making. The framework integrates 
with 
systems  via 
case  management 
Representational  State  Transfer  (REST)  Application 
Programming  Interfaces  (APIs),  enabling  seamless 
operational  deployment  without  major  infrastructure 
modifications.

anomalies

temporal

facilities

generate

existing

Cost-benefit analysis quantifies the financial impact of 
the  proposed  methodology.  Based  on  the  estimated 
average fraud loss of $125,000 per provider, established 
through  analysis  of  historical  investigation  recovery 
data,  and  the  investigation  cost  of  $8,500  per  case, 
derived  from  CMS  Office  of  Inspector  General  cost 
accounting  reports,  the  optimized  approach  generates 
net  annual  savings  of  $156  million  for  Medicare 
program  operations.  Improvements  in  detection  rates 
prevent  an  additional  $47  million  in  fraud  losses 
annually  compared  to  baseline  approaches.  False 
positive  reductions  save  $23  million  in  unnecessary 
investigation  costs.  The  rapid  deployment  timeline 
enables  cost  recovery  within  4.2  months.  Sensitivity 
analyses confirm robust positive returns across plausible 
ranges  of  cost  assumptions,  including  fraud  amounts 
between $100,000 and $150,000 and investigation costs 
between  $7,000  and  $10,000.  These  substantial 
financial benefits justify the investment in sophisticated 
temporal  analytics  infrastructure  and  the  associated 
ongoing maintenance costs. The methodology provides 
scalable 
supporting 
Medicare 
objectives  while 
maintaining operational efficiency suitable for resource-
constrained environments.

fraud  detection  capabilities

integrity

program

6. Conclusion, Limitations, and Future Work

6.1. Research Contributions and Key Findings

temporal

feature  engineering  and

This  research  developed  a  comprehensive  framework 
for 
threshold 
optimization to address critical challenges in healthcare 
claims anomaly detection. The systematic extraction of 
temporal  features  from  claims  sequences  enables  the 
identification  of  subtle  fraud  patterns  that  manifest 
through  abnormal 
irregular 
service  intervals,  and  unusual  billing  frequencies.  The 
proposed  feature  engineering  methodology  combines 
statistical  analysis,  functional  principal  component 
analysis,  and  deep  learning  representations  to  capture 
temporal  dependencies.  Experimental 
multi-scale

timing  characteristics,

Vol. 6(4), pp. 27-49, April 2026  
[46]

---

<!-- PAGE 21 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

results  show  a  consistent  improvement  over  baseline 
approaches, with higher detection rates and lower false-
positive rates in our evaluation.

algorithms

The  adaptive 
threshold  optimization  methodology 
addresses  operational  constraints  through  dynamic 
adjustment 
that  maintain  detection 
effectiveness  while  controlling  investigation  volumes. 
The framework balances competing objectives of fraud 
prevention  and  resource  efficiency  through  cost-
sensitive  optimization  and  multi-objective  decision 
analysis. Evaluation on Medicare claims data suggests 
the approach can improve cost-benefit trade-offs under 
assumed  investigation  and  loss-cost  settings.  The 
threshold adaptation mechanisms successfully respond 
to concept drift and changing fraud tactics, maintaining 
stable  performance  over  extended  deployment  periods 
where static thresholds exhibit significant degradation.

Key findings from the research include the importance 
of service-to-submission lag features, while submission-
time patterns (e.g., weekends) can be context-dependent 
signals  that  require  interpretation  aligned  with  claims 
processing  workflows.  The  study  explores  LSTM 
autoencoder  representations  for  capturing  complex 
temporal  dependencies  beyond  traditional  statistical 
features and demonstrates promising performance in our 
evaluation.  The  research 
threshold 
indicates 
should  explicitly  consider  operational 
selection 
constraints  and  asymmetric  costs,  rather  than  relying 
solely on label-dependent metrics such as classification 
accuracy. The adaptive framework's ability to maintain 
consistent performance despite concept drift highlights 
the value of continuous monitoring and recalibration in 
production fraud detection systems.

that

6.2. Research Limitations

Several  limitations  constrain  the  generalizability  and 
applicability  of  the  research  findings.  The  evaluation 
relies exclusively on Medicare Part B claims data, which 
represent  fee-for-service  reimbursement  structures. 
Performance characteristics may differ substantially in 
managed  care  environments,  Medicaid  programs,  or 
private  insurance  contexts  with  alternative  payment 
models  and  beneficiary  populations.  The  fraud  label 
construction  depends  on  completed  investigations, 
introducing  a  temporal  lag  between  the  onset  of 
fraudulent  activity  and  label  availability.  This  lag 
complicates  the  evaluation  of  early  warning  system 
effectiveness,  as 
the  methodology  cannot  assess 
detection  performance  for  fraud  schemes  identified 
before investigation completion.

The  ground-truth  fraud  labels  reflect  investigation 
selection  biases,  as  enforcement  agencies  prioritize 
high-value  cases  and  providers  with  prior  compliance 
issues. The labeled fraud sample may not represent the 
full spectrum of fraudulent behaviors, particularly novel 
schemes  not  yet  recognized  by  investigators.  Class

imbalance,  with  a  fraud  prevalence  of  0.43%,  poses 
challenges  for  model  calibration  and  performance 
estimation. Small numbers of fraud cases in individual 
provider specialty categories limit the ability to develop 
specialty-specific  detection  models.  The  experimental 
evaluation captures performance at specific timepoints 
but  cannot  fully  characterize  detection  latency  for 
identifying fraud at the earliest possible stages.

and

Computational  requirements  for  deep  learning  feature 
construction,  including  LSTM  autoencoder  training, 
impose infrastructure costs that may limit accessibility 
for  smaller  healthcare  organizations.  The  feature 
engineering  pipeline  requires  domain  expertise  to 
configure  appropriate  temporal  windows,  aggregation 
periods, 
reference  distributions.  Threshold 
optimization  assumes  stable  cost  parameters  for  fraud 
losses  and  investigation  expenses,  while  actual  costs 
exhibit uncertainty and temporal variation. The adaptive 
threshold  framework  requires  ongoing  performance-
monitoring  infrastructure  and  investigative  feedback 
mechanisms that may not be available in all operational 
contexts. Interpretability of complex temporal features 
and deep learning representations remains challenging 
despite  attention  mechanisms  and  visualization 
approaches.

6.3. Directions for Future Research

framework

Future  research  should  extend  the  temporal  feature 
engineering 
to  alternative  healthcare 
payment  models, 
including  bundled  payments, 
accountable  care  organizations,  and  value-based 
reimbursement  structures.  Fraud  patterns  in  these 
contexts  differ  from  traditional  fee-for-service  billing, 
requiring  adaptation  of  temporal  features  to  capture 
relevant  anomalies.  Cross-domain  transfer  learning 
approaches  could  leverage  fraud  detection  knowledge 
from  Medicare  data  to  improve  performance  on 
Medicaid  or  private  insurance  claims  with  limited 
labeled  fraud  cases.  Federated  learning  architectures 
enable  collaborative  model  development  across 
multiple  payer  organizations  while  preserving  data 
privacy and confidentiality.

feature

investigation

learning.  These

learning  architectures,

Advanced  deep 
including 
Transformer  models  and  attention-based  temporal 
for 
convolution  networks,  warrant 
temporal 
architectures 
demonstrate strong performance on sequential modeling 
tasks  and  may  capture 
temporal 
dependencies  than  LSTM  networks.  Graph  neural 
networks 
provider-beneficiary-
procedure  relationships  offer  promising  avenues  for 
detecting  collusive  fraud  networks.  Explainability 
research should develop interpretable temporal feature 
representations  enabling  investigators  to  understand 
detection rationales and validate algorithmic decisions. 
Causal inference methods could distinguish correlation

longer-range

incorporate

that

Vol. 6(4), pp. 27-49, April 2026  
[47]

---

<!-- PAGE 22 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

from  causation  in  temporal  fraud  patterns,  supporting 
more robust detection.

28(7), 
https://doi.org/10.1109/TKDE.2016.2535209

1610-1628.

optimization  methodology

Threshold 
should 
incorporate  reinforcement  learning  approaches  that 
learn optimal threshold policies through interaction with 
operational  environments.  Online  learning  algorithms 
that enable continuous adaptation without explicit drift-
detection mechanisms could improve responsiveness to 
emerging fraud tactics. Multi-armed bandit frameworks 
could  balance  exploration  of  alternative  threshold 
strategies  with  exploitation  of  known  effective 
approaches.  Research  on  fairness  and  bias  in  fraud 
threshold 
detection 
impact 
optimization  does  not  disproportionately 
providers  serving  vulnerable  populations  or  practicing 
in  underserved  areas.  Adversarial  robustness  analysis 
should evaluate the detection system’s vulnerability to 
strategic manipulation by sophisticated fraudsters  who 
are aware of its detection mechanisms.

algorithms

should

ensure

following  deployment.

Longitudinal  studies  tracking  the  impact  of  a  fraud 
detection  system  on  provider  behavior  could  quantify 
deterrence  effects  and  measure  changes  in  fraud 
Integration  of 
prevalence 
external  data  sources,  including  physician  licensing 
information,  prior  enforcement  actions,  and  network 
analysis  data,  may  enhance  detection 
through 
complementary  signal  sources.  Real-time  streaming 
architectures that enable immediate claims evaluation at 
submission  time,  rather  than  batch  processing,  could 
reduce  fraud  losses  by  enabling  faster  intervention. 
Research  on  optimal  investigation  resource  allocation 
that  help 
should  develop  decision-support 
investigators  prioritize  cases,  maximizing  expected 
recovery  while  accounting  for  capacity  constraints. 
These 
research  directions  would  advance  both 
theoretical understanding and practical effectiveness of 
temporal  anomaly  detection 
in  healthcare  fraud 
prevention.

tools

References

[1]. Centers for Medicare & Medicaid Services. (2023). 
National Health Expenditure Data: Historical. U.S. 
Department  of  Health  and  Human  Services. 
from  https://www.cms.gov/Research-
Retrieved 
Statistics-Data-and-Systems/Statistics-Trends-and-
Reports/NationalHealthExpendData

[2]. Federal  Bureau  of  Investigation.  (2022).  Financial 
Crimes Report: Healthcare Fraud. U.S. Department 
of 
from 
https://www.fbi.gov/stats-
services/publications/financial-crimes-report

Retrieved

Justice.

[3]. Ahmed,  M.,  Hu,  J.,  &  Luo,  X.  (2016).  Anomaly 
detection  for  temporal  data:  A  survey.  IEEE 
Transactions on Knowledge and Data Engineering,

[4]. Malhotra,  P.,  Vig,  L.,  Shroff,  G.,  &  Agarwal,  P. 
(2015).  Long  short  term  memory  networks  for 
anomaly detection in time series. In Proceedings of 
the 23rd European Symposium on Artificial Neural 
Networks, Computational Intelligence and Machine 
Learning (ESANN 2015), pp. 89-94.

[5]. Ahmad,  A.  M.,  Eckert,  C.,  Teredesai,  A.,  & 
McKelvey,  G. 
Interpretable  machine 
learning in healthcare. IEEE Intelligent Informatics 
Bulletin, 19(1), 1-7.

(2018).

[6]. Chen,  J.,  Sathe,  S.,  Aggarwal,  C.,  &  Turaga,  D. 
(2020). Embedding for anomaly detection on health 
insurance  claims.  In  2020  IEEE  International 
Conference  on  Data  Mining  (ICDM),  pp.  1003-
1008. 
https://doi.org/10.1109/ICDM50108.2020.00116

[7]. Zhang, C., Song, D., Chen, Y., Feng, X., Lumezanu, 
C.,  Cheng,  W.,  Ni,  J.,  Zong,  B.,  Chen,  H.,  & 
Chawla,  N.  V.  (2019).  A  deep  neural  network  for 
unsupervised  anomaly  detection  and  diagnosis  in 
multivariate time series data. In Proceedings of the 
33rd  AAAI  Conference  on  Artificial  Intelligence, 
33(1), 
1409-1416. 
https://doi.org/10.1609/aaai.v33i01.33011409

[8]. Bauder, R. A., & Khoshgoftaar, T. M. (2023). Cost-
sensitive  learning  for  medical  insurance  fraud 
IEEE 
detection  with 
Transactions on Knowledge and Data Engineering, 
35(10), 
10375-10389. 
https://doi.org/10.1109/TKDE.2023.3240431

information.

temporal

[9]. Xu,  H.,  Feng,  Y.,  Chen,  J.,  Wang,  Z.,  Qiao,  H., 
Chen, W., Zhao, N., Li, Z., Bu, J., Li, Z., & Liu, Y. 
(2018).  Unsupervised  anomaly  detection  via 
variational  auto-encoder  for  seasonal  KPIs in  web 
applications.  In  Proceedings  of  the  2018  World 
Wide  Web  Conference  (WWW  '18),  pp.  187-196. 
https://doi.org/10.1145/3178876.3185996

[10].  Alharbi,  A.,  Alshammari,  M.,  Okon,  O.  D., 
Alshdadi,  A.  A.,  Samha,  A.  K.,  &  Issaoui,  Y. 
(2023).  A  machine  learning-based  approach  for 
medical insurance anomaly detection by predicting 
indirect  outpatients'  claim  price.  In  2023  IEEE 
International Conference on Industrial Engineering 
and  Engineering  Management  (IEEM),  pp.  1425-
1429. 
https://doi.org/10.1109/IEEM58616.2023.1040689
1

[11].  Karadayi, Y., Aydin, M. N., & Öğrencı, A. S. 
(2020).  Unsupervised  anomaly  detection 
in 
multivariate  spatio-temporal  data  using  deep 
learning: Early detection of COVID-19 outbreak in

Vol. 6(4), pp. 27-49, April 2026  
[48]

---

<!-- PAGE 23 -->

Journal of Advanced Computing Systems (JACS)

ISSN: 3066-3962

Italy. 
https://doi.org/10.1109/ACCESS.2020.3022366

IEEE  Access,

164155-164177.

8,

[12].  Choi,  K.,  Yi, J.,  Park,  C., &  Yoon,  S. (2021). 
Deep learning for anomaly detection in time-series 
data:  Review,  analysis,  and  guidelines.  IEEE 
Access, 
120043-120065. 
https://doi.org/10.1109/ACCESS.2021.3090905

9,

[13].  Zhang,  Y.,  Chen,  Y.,  Wang,  J.,  &  Pan,  Z. 
(2022).  Threshold-free  anomaly  detection  for 
streaming  time  series  through  deep  learning.  In 
2022  IEEE  International  Conference  on  Data 
Mining 
758-767. 
https://doi.org/10.1109/ICDM54844.2022.00088

(ICDM),

pp.

[14].  Schmidl,  S.,  Wenig,  P.,  &  Papenbrock,  T. 
(2022).  Anomaly  detection  in  time  series:  A 
comprehensive  evaluation.  Proceedings  of  the 
1779-1797. 
VLDB 
https://doi.org/10.14778/3538598.3538602

Endowment,

15(9),

clustering

[15].  Rahman,  M. M., Watanobe,  Y.,  &  Nakamura, 
K.  (2024).  Detecting  anomalies  in  medical  claims 
IEEE 
algorithm. 
with 
International  Conference  on  Big  Data  (Big  Data), 
pp. 
2156-2163. 
https://doi.org/10.1109/BigData62323.2024.10825
476

In  2024

Vol. 6(4), pp. 27-49, April 2026  
[49]

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Advanced Computing Systems (JACS)
ISSN: 3066-3962
Content Available at SciPublication
Temporal Feature Engineering and Threshold Optimization for Early Warning in
Healthcare Claims Anomaly Detection
Mingxuan Han1, Jiawen Lai1.2
1 Computer Science, University of Utah, UT, USA
1.2 Computer Engineering, University of California, Riverside, CA, USA
DOI: 10.69987/JACS.2026.60403
Keywords Abstract
Healthcare claims fraud, Healthcare insurance fraud represents a substantial financial burden on medical
Temporal feature systems worldwide, with fraudulent claims accounting for billions of dollars in
engineering, Anomaly annual losses. Detecting anomalous patterns in medical claims data requires
detection, Threshold sophisticated analytical approaches that can identify subtle temporal
optimization irregularities before significant financial damage occurs. This research presents
a comprehensive investigation of temporal feature engineering methodologies
and threshold optimization strategies specifically designed for early-warning
mechanisms in healthcare claims anomaly detection. The study develops a
systematic framework for extracting meaningful temporal features from claims
sequential data, including service interval patterns, claim frequency
characteristics, and seasonal variation indicators. Advanced feature
construction techniques that combine statistical analysis and machine learning
are employed to capture the complex temporal dependencies inherent in
fraudulent behavior patterns. We investigate threshold optimization strategies
that balance detection sensitivity with operational constraints through adaptive
adjustment mechanisms. A retrospective case study of Medicare claims data
suggests that engineered temporal features can improve anomaly-detection
performance. The research provides practical guidelines for threshold
parameter selection and dynamic adjustment strategies suitable for production
deployment. Results suggest improvements in early warning capability while
maintaining practically manageable false positive rates.
Temporal patterns embedded within claim sequences
1. Introduction
provide critical signals for identifying anomalous
behavior. Fraudulent providers often exhibit distinctive
1.1. Research Background and Motivation
temporal characteristics, including abnormal claim
submission frequencies, irregular service intervals, and
Healthcare expenditure in the United States exceeds
atypical billing time distributions. Traditional rule-
$4.3 trillion annually, representing approximately
based detection systems struggle to adapt to evolving
17.8% of the national gross domestic product [1]. Within
fraud tactics and generate excessive false alarms,
this massive financial ecosystem, fraudulent activities
burdening investigative resources. The temporal
pose a persistent threat to program sustainability and
dimension of claims data remains underutilized despite
beneficiary welfare. Federal healthcare programs,
its potential to reveal subtle patterns indicative of
including Medicare and Medicaid, experience estimated
coordinated fraud schemes or systematic billing
fraud rates ranging from 3% to 10% of total
irregularities [3].
expenditures [2], translating to potential losses between
$129 billion and $430 billion per year. The complexity
Recent advances in machine learning and time series
of modern healthcare delivery systems, combined with
analysis offer promising approaches for extracting
the volume and velocity of claims processing, creates
meaningful features from temporal claims data. Deep
opportunities for sophisticated fraud schemes that evade
learning architectures, including Long Short-Term
traditional detection mechanisms.
Memory (LSTM) networks, have demonstrated superior
performance in capturing long-range temporal
dependencies compared to conventional statistical
Vol. 6(4), pp. 27-49, April 2026
[27]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

methods [4]. The challenge lies in designing feature- experimental evaluation of Medicare Part B claims data
engineering pipelines that transform raw temporal data  demonstrates the effectiveness of engineered temporal
into discriminative representations suitable for anomaly  features compared to baseline approaches. Performance
detection. Effective feature engineering requires domain  metrics, including precision, recall, and F1-scores, are
expertise  to  identify  clinically  meaningful  temporal  reported across multiple provider specialty categories
patterns while maintaining computational efficiency for  and fraud types.
real-time processing requirements.
The remainder of this paper is organized into six main
1.2. Problem Statement and Research Objectives  sections. Section 2 reviews related work on temporal
|     |     |     |     |     |     |     |     | anomaly  | detection  |     | for  healthcare  |     | claims,  | feature  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ---------------- | --- | -------- | -------- |
The primary challenge in healthcare claims anomaly
|     |     |     |     |     |     |     |     | engineering  | for  | time  | series  | data,  | and  | threshold  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ----- | ------- | ------ | ---- | ---------- |
detection is extracting informative temporal features
|     |     |     |     |     |     |     |     | optimization  | strategies  |     | for  | early  | warning  | systems.  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | ---- | ------ | -------- | --------- |
that capture fraudulent behavior while minimizing false- Section  3  presents  the  temporal feature  engineering
positive rates that overwhelm investigative capacity.  methodology, including feature extraction procedures,
| Existing    | approaches  |     | typically  |     | rely    | on  manually  |     |               |               |     |      |                 |     |               |
| ----------- | ----------- | --- | ---------- | --- | ------- | ------------- | --- | ------------- | ------------- | --- | ---- | --------------- | --- | ------------- |
|             |             |     |            |     |         |               |     | construction  | techniques,   |     |      | and  selection  |     | algorithms.   |
| engineered  | features    |     | based      | on  | domain  | knowledge,    |     |               |               |     |      |                 |     |               |
|             |             |     |            |     |         |               |     | Section       | 4  describes  |     | the  | threshold       |     | optimization  |
limiting their ability to discover novel fraud patterns.
framework including adaptive setting strategies, trade-
Threshold selection for anomaly alerts poses another  off  analysis  methods,  and  dynamic  adjustment
critical challenge: overly sensitive thresholds generate  algorithms.  Section  5  reports  experimental  results
excessive false alarms, while conservative thresholds
|     |     |     |     |     |     |     |     | including  | dataset  |     | descriptions,  |     |     | performance  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | -------------- | --- | --- | ------------ |
miss early-stage fraud. The temporal nature of claims
comparisons, and practical implications for operational
data introduces additional complexity through seasonal
|     |     |     |     |     |     |     |     | deployment.  | Section  |     | 6  discusses  |     | the  | conclusions,  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------- | --- | ---- | ------------- |
patterns, concept drift, and varying baseline behaviors  research  limitations, and directions for future  work.
across provider specialties and geographic regions.  Section 7 provides acknowledgments.
| This  | research  | addresses  |     | these  |     | challenges  | by  |     |     |     |     |     |     |     |
| ----- | --------- | ---------- | --- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
2. Related Work and Theoretical Foundation
| systematically  |                | investigating  |     |      | temporal  |            | feature  |     |     |     |     |     |     |     |
| --------------- | -------------- | -------------- | --- | ---- | --------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| engineering     | methodologies  |                |     | and  | adaptive  | threshold  |          |     |     |     |     |     |     |     |
optimization  strategies.  The  primary  objective  is  to  2.1.  Temporal  Anomaly  Detection  in  Healthcare
| develop  | a  comprehensive  |     |     | framework  |     | for  extracting  |     | Claims  |     |     |     |     |     |     |
| -------- | ----------------- | --- | --- | ---------- | --- | ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
temporal features from claim sequences that effectively
Research in healthcare claims anomaly detection has
distinguish anomalous patterns from legitimate practice
evolved from simple rule-based systems to sophisticated
| variations.  | Secondary  |     | objectives  |     | include  | designing  |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ----------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
threshold-optimization  algorithms  that  dynamically  machine learning approaches. Early detection methods
balance  detection  sensitivity  with  operational  relied on manually defined business rules that captured
|     |     |     |     |     |     |     |     | known  | fraud  | indicators,  |     | such  as  | excessive  | billing  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------------ | --- | --------- | ---------- | -------- |
constraints, evaluating the comparative performance of
|            |                      |     |     |     |             |     |       | amounts  | or  unusual  |     | service  | combinations.  |     | These  |
| ---------- | -------------------- | --- | --- | --- | ----------- | --- | ----- | -------- | ------------ | --- | -------- | -------------- | --- | ------ |
| different  | feature-engineering  |     |     |     | approaches  | on  | real  |          |              |     |          |                |     |        |
approaches suffered from limited adaptability and high
| Medicare  | claims  |     | data,  | and  | providing  | actionable  |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | ------ | ---- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
guidelines  for  parameter  selection  in  production  false  positive  rates  as  fraudulent  tactics  evolved.
deployment scenarios. The research specifically focuses  Statistical methods based on outlier detection principles
|     |     |     |     |     |     |     |     | offered  | improvements  |     | through  | automated  |     | threshold  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | -------- | ---------- | --- | ---------- |
on early warning mechanisms that detect anomalous
|     |     |     |     |     |     |     |     | determination  | based  |     | on  historical  |     | data  | distributions.  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | --- | --------------- | --- | ----- | --------------- |
patterns before substantial financial losses occur [5].
|     |     |     |     |     |     |     |     | Clustering  | techniques  |     | grouped  | similar  |     | providers  to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | -------- | -------- | --- | -------------- |
1.3. Contributions and Paper Organization  identify deviations from peer behavior patterns. Graph-
|     |     |     |     |     |     |     |     | based  | methods  | analyzed  |     | relationships  |     | between  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------- | --- | -------------- | --- | -------- |
This work makes several contributions to research on
providers, beneficiaries, and services to detect collusive
healthcare  claims  anomaly  detection.  A  systematic  fraud networks [6].
temporal feature engineering framework is developed
that combines statistical analysis with machine learning- The integration of temporal information into anomaly
based feature construction to capture complex temporal  detection frameworks has gained increasing attention.
dependencies  in  claims  sequences.  The  framework  Time  series  analysis  methods  model  normal  billing
incorporates  multiple  temporal  scales  ranging  from  patterns  to  identify  temporal  deviations.  Recurrent
short-term  service  intervals  to  long-term  seasonal  neural  networks  (RNNs)  demonstrate  particular
patterns.  A  novel  adaptive  threshold  optimization  effectiveness  in  capturing  sequential  dependencies
methodology  is  proposed  that  adjusts  detection  within claims streams. Autoencoder architectures learn
thresholds based on historical false positive rates and  compressed  representations  of  normal  temporal
investigative  capacity  constraints.  The  approach  patterns, flagging reconstructions with high error as
maintains  detection  effectiveness  while  controlling  potential anomalies. The temporal dimension enables
operational  burden  through  dynamic  threshold  the detection of subtle fraud patterns that manifest over
adjustment  mechanisms.  A  comprehensive  extended periods, including gradual billing inflation or
Vol. 6(4), pp. 27-49, April 2026
[28]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

the  strategic  timing  of  claim  submissions  to  avoid  regulatory  constraints.  Recency-frequency-monetary
detection. Seasonal decomposition techniques separate  (RFM)  features  borrowed  from  marketing  analytics
legitimate periodic variations from genuine anomalies,  capture recent billing intensity, submission frequency,
reducing false positives caused by predictable cyclical  and  financial  magnitude.  Service  sequence  features
patterns [7].  analyze the ordering and timing of procedure codes.
|     |     |     |     |     |     |     |     | Beneficiary-provider  |     |     | interaction  |     | patterns  |     | track  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ------------ | --- | --------- | --- | ------ |
Recent work has explored hybrid approaches combining
|     |     |     |     |     |     |     |     | continuity  | of  | care  | relationships.  |     | Geographic  |     | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --------------- | --- | ----------- | --- | ---- |
multiple detection methodologies. Ensemble methods
|            |              |     |       |          |             |     |     | temporal  | clustering  |           | features   | identify  |                 | coordinated  |      |
| ---------- | ------------ | --- | ----- | -------- | ----------- | --- | --- | --------- | ----------- | --------- | ---------- | --------- | --------------- | ------------ | ---- |
| aggregate  | predictions  |     | from  | diverse  | algorithms  |     | to  |           |             |           |            |           |                 |              |      |
|            |              |     |       |          |             |     |     | activity  | across      | multiple  | providers  |           | or  locations.  |              | The  |
improve robustness and reduce individual model biases.  effectiveness of engineered features depends on careful
Cost-sensitive learning frameworks explicitly account  selection  informed  by  fraud  domain  knowledge,
for the asymmetric costs of false positives and false
combined with systematic evaluation on representative
| negatives  | in  | fraud  | detection  | applications.  |     | Transfer  |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------ | ---------- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
datasets.
learning techniques leverage knowledge from related
domains  or  historical  periods  to  improve  detection  2.3.  Threshold  Optimization  Strategies  in  Early
performance  on  new  fraud  patterns.  The  challenge  Warning Systems
| remains  | in  designing  |     | systems  | that  | maintain  |     | high  |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | -------- | ----- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
detection rates while controlling false positive volumes  Threshold selection critically impacts the performance
to manageable levels for investigative follow-up. Real- and operational viability of anomaly detection systems.
Fixed thresholds based on percentile cutoffs provide
| time  | detection  | requirements  |     | impose  |     | additional  |     |     |     |     |     |     |     |     |     |
| ----- | ---------- | ------------- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
simplicity but fail to adapt to changing data distributions
| constraints  | on  | computational  |     | complexity  |     | and  | on  |              |     |           |            |     |         |             |     |
| ------------ | --- | -------------- | --- | ----------- | --- | ---- | --- | ------------ | --- | --------- | ---------- | --- | ------- | ----------- | --- |
|              |     |                |     |             |     |      |     | or  varying  |     | baseline  | behaviors  |     | across  | subgroups.  |     |
tolerance to latency.
|     |     |     |     |     |     |     |     | Statistical  | thresholds  |     | derived  |     | from  | normal  | data  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | -------- | --- | ----- | ------- | ----- |
2.2.  Feature  Engineering  Approaches  for  Time  characteristics, such as three standard deviations from
Series Data  the  mean,  offer  principled  approaches  but  assume
specific distributional properties that may not hold in
Feature  engineering  for  temporal  data  involves  practice.  Receiver  Operating  Characteristic  (ROC)
| transforming  |     | raw  | time  | series  | into  | meaningful  |     |        |           |          |             |     |              |     |     |
| ------------- | --- | ---- | ----- | ------- | ----- | ----------- | --- | ------ | --------- | -------- | ----------- | --- | ------------ | --- | --- |
|               |     |      |       |         |       |             |     | curve  | analysis  | enables  | systematic  |     | exploration  |     | of  |
representations that capture relevant patterns. Statistical
|           |            |     |        |            |            |     |      | sensitivity-specificity  |     |     | trade-offs  |     | to  select  |     | optimal  |
| --------- | ---------- | --- | ------ | ---------- | ---------- | --- | ---- | ------------------------ | --- | --- | ----------- | --- | ----------- | --- | -------- |
| features  | including  |     | mean,  | variance,  | skewness,  |     | and  |                          |     |     |             |     |             |     |          |
operating points based on cost considerations [9].
kurtosis provide basic distributional characteristics of
temporal sequences. Trend analysis extracts linear or  Adaptive  threshold  strategies  adjust  detection
polynomial growth patterns. Autocorrelation functions  boundaries  based  on  operational  feedback  and
measure  temporal  dependencies  at  different  lag  performance  monitoring.  Dynamic  thresholding
intervals.  Spectral  analysis  decomposes  signals  into  incorporates recent false positive rates to automatically
frequency  components  to  identify  periodic  patterns.  tune  sensitivity  levels.  Concept  drift  detection
Window-based features compute statistics over sliding  algorithms identify distribution shifts that necessitate
temporal windows to capture local behavior variations.  threshold  recalibration.  Multi-threshold  approaches
These  traditional  approaches  provide  interpretable  employ different cutoffs for various risk levels, enabling
features but may miss complex nonlinear patterns.  tiered  investigation  prioritization.  Context-aware
|          |                 |     |          |     |               |     |         | thresholds  | vary  | by  | provider  | specialty,  |     | geographic  |     |
| -------- | --------------- | --- | -------- | --- | ------------- | --- | ------- | ----------- | ----- | --- | --------- | ----------- | --- | ----------- | --- |
| Machine  | learning-based  |     | feature  |     | construction  |     | offers  |             |       |     |           |             |     |             |     |
region, or temporal period to account for legitimate
| automated  | discovery  |     | of  | discriminative  |     | temporal  |     |           |             |     |                 |     |       |                |     |
| ---------- | ---------- | --- | --- | --------------- | --- | --------- | --- | --------- | ----------- | --- | --------------- | --- | ----- | -------------- | --- |
|            |            |     |     |                 |     |           |     | practice  | variation.  |     | The  challenge  |     | lies  | in  balancing  |     |
patterns.  Functional  Principal  Component  Analysis  responsiveness to changing patterns with stability to
(FPCA)  decomposes  temporal  trajectories  into  avoid excessive fluctuations that confuse users.
| dominant  | modes  |     | of  variation,  |     | creating  | compact  |     |     |     |     |     |     |     |     |     |
| --------- | ------ | --- | --------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
representations  that  preserve  essential  temporal  Early  warning  system  design  requires  careful
structure [8]. Matrix profile techniques identify repeated  consideration  of  operational  constraints,  including
patterns  and  discord  sequences  within  time  series.  investigative capacity, alert fatigue, and response time
Shapelet mining discovers characteristic subsequences  requirements. Threshold optimization must account for
that  distinguish  between  classes.  Deep  learning  asymmetric costs: false negatives represent potential
approaches, including convolutional filters and attention  fraud losses, while false positives consume investigative
mechanisms,  learn  hierarchical  temporal  features  resources  without  recovery.  Sequential  testing
directly  from  raw  data.  The  trade-off  between  frameworks enable refinement of initial alerts through
automated feature learning and interpretability remains  progressive analysis stages. Explainability requirements
a  central  consideration,  particularly  in  regulated  demand  that  threshold  crossings  trigger  actionable
domains requiring explainable detection decisions.  insights  rather  than  opaque  anomaly  scores.  The
|                  |     |          |              |     |      |             |     | integration  | of        | domain  | expertise  |                | through  | adjustable  |           |
| ---------------- | --- | -------- | ------------ | --- | ---- | ----------- | --- | ------------ | --------- | ------- | ---------- | -------------- | -------- | ----------- | --------- |
| Domain-specific  |     | feature  | engineering  |     | for  | healthcare  |     |              |           |         |            |                |          |             |           |
|                  |     |          |              |     |      |             |     | sensitivity  | controls  |         | empowers   | investigators  |          |             | to  tune  |
claims requires incorporation of medical knowledge and
Vol. 6(4), pp. 27-49, April 2026
[29]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

detection  based  on  emerging  fraud  intelligence  and  codes, and computes graph-based features such as path
changing enforcement priorities.  lengths, branching factors, and cycle-detection metrics.
These structural temporal features complement simple
timestamp statistics by incorporating medical domain
3. Methodology: Temporal Feature Engineering
knowledge about appropriate care progression patterns.
Framework
Data access & compliance.
| 3.1.  Temporal  |     | Feature  | Extraction  |     | from  | Claims  |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ----------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Sequential Data  We used a de-identified Medicare Part B claims dataset
(2020–2022) obtained through authorized access (e.g.,
Claim Timestamp Analysis  [CMS DUA / VRDC / institutional agreement]). The
|     |     |     |     |     |     |     | study  used  | no  | direct  | identifiers,  |     | and  analyses  |     | were  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ------------- | --- | -------------- | --- | ----- |
The foundation of temporal feature engineering rests on
conducted on derived/aggregated features. Due to data-
systematic analysis of claim submission timestamps and
use restrictions, the raw claims cannot be redistributed;
| service  | dates.  | Each  | claim  | record  | contains  | multiple  |     |     |     |     |     |     |     |     |
| -------- | ------- | ----- | ------ | ------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
however, we will release feature engineering code and
temporal attributes including service start date, service  evaluation scripts to support reproducibility.
end date, submission date, and processing date. The
temporal features extracted from these attributes capture  Service Interval Pattern Mining
| different  | aspects  | of  | provider  | behavior  |     | and  billing  |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | --------- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
patterns. Service-to-submission lag measures the time  Service interval features quantify the temporal spacing
between consecutive services for the same beneficiary
interval between service delivery and claim filing, with
or by the same provider. Inter-service intervals capture
| abnormal  | patterns  | indicating  |     | potential  |     | post-dating  |     |     |     |     |     |     |     |     |
| --------- | --------- | ----------- | --- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
billing rhythm characteristics that distinguish normal
schemes or delayed batch submissions characteristic of
certain fraud types. Submission date clustering analysis  practice patterns from systematic fraud schemes. The
identifies unusual concentrations of claims at specific  extraction  methodology  computes  multiple  interval
|           |              |       |       |               |         |               | statistics,  | including  |              | minimum,  |             | maximum,  |          | mean,  |
| --------- | ------------ | ----- | ----- | ------------- | ------- | ------------- | ------------ | ---------- | ------------ | --------- | ----------- | --------- | -------- | ------ |
| calendar  | periods,     | such  | as    | end-of-month  |         | or  end-of-   |              |            |              |           |             |           |          |        |
|           |              |       |       |               |         |               | median,      | and        | coefficient  | of        | variation,  | across    | rolling  |        |
| quarter   | submissions  |       | that  | may           | signal  | quota-driven  |              |            |              |           |             |           |          |        |
|           |              |       |       |               |         |               | windows      | of         | varying      | lengths.  | Providers   |           | engaged  | in     |
fraudulent billing [10].
excessive billing schemes often exhibit characteristic
Time-of-day  and  day-of-week  features  reveal  interval  distributions  with  periodic  spikes
operational patterns that differ between legitimate and  corresponding to automated billing cycles or systematic
fraudulent  providers.  Extraction procedures  compute  overbilling patterns. Legitimate providers demonstrate
submission-hour  distributions  to  identify  providers  more variable intervals reflecting genuine patient needs
submitting disproportionate claims during off hours,  and appointment scheduling constraints.
| when  | manual  | review  | processes  |     | may  | be  reduced.  |     |     |     |     |     |     |     |     |
| ----- | ------- | ------- | ---------- | --- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Beneficiary-level interval analysis examines temporal
Weekend submission ratios capture abnormal activity
patterns  inconsistent  with  typical  medical  practice  patterns  of  services  received  by  individual  patients.
schedules. Holiday submission indicators flag claims  Unusually frequent services within short time windows
|     |     |     |     |     |     |     | indicate  | potential  | phantom  |     | billing  | or  unnecessary  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | -------- | --- | -------- | ---------------- | --- | --- |
filed during periods when legitimate medical services
treatment patterns. The extraction process uses sliding-
typically decrease. These temporal fingerprints provide
window algorithms to compute service counts and dollar
| powerful  | discriminative  |     | features  |     | when  | aggregated  |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | --------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
across rolling window periods. The extraction pipeline  amounts over configurable time periods ranging from 7
processes timestamp fields through standardized date  days  to  90  days.  Statistical  outlier  detection  at  the
|          |      |           |                |     |     |             | beneficiary  | level         | identifies  |       | patients          | with  | interval   |     |
| -------- | ---- | --------- | -------------- | --- | --- | ----------- | ------------ | ------------- | ----------- | ----- | ----------------- | ----- | ---------- | --- |
| parsing  | and  | timezone  | normalization  |     |     | to  ensure  |              |               |             |       |                   |       |            |     |
|          |      |           |                |     |     |             | patterns     | inconsistent  |             | with  | their  diagnosis  |       | codes and  |     |
consistency across geographically distributed providers
|     |     |     |     |     |     |     | demographic  |     | characteristics.  |     | Cross-provider  |     | interval  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------------- | --- | --------------- | --- | --------- | --- |
[11].
analysis reveals beneficiaries receiving similar services
Temporal  sequence  ordering  analysis  examines  the  from multiple providers within implausible time frames,
chronological pattern of service codes within patient  suggesting coordinated fraud networks or beneficiary
episodes.  Legitimate  medical  care  follows  clinically  cooperation in fraud schemes [12].
| appropriate  |     | sequences  | determined  |     | by  | diagnostic  |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
The methodology incorporates domain-specific interval
protocols and treatment pathways. Sequence reversal
|             |           |         |     |        |             |        | constraints  | derived  |     | from  | clinical  | guidelines  |     | and  |
| ----------- | --------- | ------- | --- | ------ | ----------- | ------ | ------------ | -------- | --- | ----- | --------- | ----------- | --- | ---- |
| indicators  | identify  | claims  | in  | which  | diagnostic  | tests  |              |          |     |       |           |             |     |      |
regulatory requirements. Certain procedure codes have
occur after treatment procedures, suggesting fabricated
medical-necessity  documentation.  Temporal  gap  regulatory maximum frequency limits within specified
analysis within treatment sequences identifies unusually  time periods established by the Centers for Medicare
|     |     |     |     |     |     |     | and  Medicaid  |     | Services  | (CMS).  |     | Feature  | extraction  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | ------- | --- | -------- | ----------- | --- |
extended intervals between related services that may
|              |        |             |              |     |          |               | computes  | violation  | indicators  |        | by          | comparing  |              | actual  |
| ------------ | ------ | ----------- | ------------ | --- | -------- | ------------- | --------- | ---------- | ----------- | ------ | ----------- | ---------- | ------------ | ------- |
| indicate     | claim  | splitting   | strategies.  |     | The      | extraction    |           |            |             |        |             |            |              |         |
|              |        |             |              |     |          |               | billing   | intervals  | against     | these  | regulatory  |            | thresholds.  |         |
| methodology  |        | constructs  | directed     |     | acyclic  | graphs  that  |           |            |             |        |             |            |              |         |
represent  temporal  dependencies  among  procedure  Medical necessity intervals defined by clinical protocols
Vol. 6(4), pp. 27-49, April 2026
[30]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

provide additional benchmarks for identifying temporal  generate risk scores that feed into downstream anomaly
anomalies. The extraction framework maintains lookup  detection  algorithms.  Table  1  presents  the
tables  that  map  procedure  codes  to  the  appropriate  comprehensive taxonomy of temporal interval features
minimum intervals based on medical standards of care.  extracted from claims data.
Deviations from these clinically appropriate intervals
Table 1: Temporal Interval Feature Taxonomy
Feature Category  Specific Features  Calculation Method  Fraud Detection Relevance
Service-to- Mean  lag,  Std  dev,  Min,  Difference  between  service  Identifies  post-dating  and
Submission Lag  Max  date and submission date  delayed batch submissions
Inter-Service  Mean,  Median,  CV,  Time  between  consecutive  Detects excessive billing and
Intervals  Autocorrelation  services for same beneficiary  systematic patterns
Beneficiary  Interval  7-day count, 30-day count,  Service  frequency  within  Reveals phantom billing and
Patterns  90-day count  rolling windows  unnecessary treatments
|     |     |     |     |     |     | Comparison  |     |     | against  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | -------- | --- | --- | --- | --- |
Regulatory  Violation  indicators,  Flags  violations  of  billing
|             |     |     |                   |     |     | regulatory  |     | maximum  |     |                        |     |     |     |
| ----------- | --- | --- | ----------------- | --- | --- | ----------- | --- | -------- | --- | ---------------------- | --- | --- | --- |
| Compliance  |     |     | Frequency limits  |     |     |             |     |          |     | frequency regulations  |     |     |     |
frequencies
Clinical  Medical necessity intervals,  Comparison  against  clinical  Identifies  medically
Appropriateness  Protocol deviations  guideline intervals  inappropriate service timing
The temporal interval feature space captures multiple  identify statistically significant deviations from baseline
dimensions of provider billing behavior across different  frequency patterns [13].
| time  scales.  |     | Short-term  | intervals  | reveal  | immediate  |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | ---------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Distribution shape characteristics capture more subtle
billing patterns and response to regulatory requirements.
|     |     |     |     |     |     |     | aspects  | of  | billing  | patterns.  | Skewness  |     | measures  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ---------- | --------- | --- | --------- |
Medium-term intervals expose seasonal variations and
|           |             |     |            |            |         |      | asymmetry  |     | in  frequency  |     | distributions,  |     | with  highly  |
| --------- | ----------- | --- | ---------- | ---------- | ------- | ---- | ---------- | --- | -------------- | --- | --------------- | --- | ------------- |
| practice  | evolution.  |     | Long-term  | intervals  | enable  | the  |            |     |                |     |                 |     |               |
detection of gradual trends indicating systematic fraud  skewed patterns suggesting concentrated billing activity
schemes that develop slowly to avoid detection. The  during  specific  periods.  Kurtosis  quantifies  tail
behavior, identifying providers with occasional extreme
| multi-scale  |     | temporal  | analysis  | provides  | robustness  |     |          |         |               |     |       |         |           |
| ------------ | --- | --------- | --------- | --------- | ----------- | --- | -------- | ------- | ------------- | --- | ----- | ------- | --------- |
|              |     |           |           |           |             |     | billing  | spikes  | inconsistent  |     | with  | normal  | practice  |
against fraud tactics that operate at different temporal
variation. Entropy features measure the randomness of
resolutions.
|     |     |     |     |     |     |     | temporal  | distributions;  |     | low  | entropy  | indicates  | highly  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | --- | ---- | -------- | ---------- | ------- |
Frequency Distribution Characterization  structured,  potentially  artificial  billing  patterns.  The
|     |     |     |     |     |     |     | extraction  | framework  |     | computes  |     | these  | distributional  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --------- | --- | ------ | --------------- |
Claim frequency distributions provide critical signals  statistics across rolling windows to track the temporal
about  provider  billing  intensity  and  consistency  evolution  of  frequency  characteristics.  Comparative
| patterns.  | The  | extraction  |     | methodology  | computes  |     |     |     |     |     |     |     |     |
| ---------- | ---- | ----------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
analysis benchmarks individual provider distributions
| frequency  | features  |     | at  multiple  | aggregation  |     | levels,  |     |     |     |     |     |     |     |
| ---------- | --------- | --- | ------------- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
against peer groups defined by specialty, geography,
including daily, weekly, monthly, and quarterly periods.
and practice size.
Simple frequency counts measure the number of claims
submitted  within  each  time  window.  Frequency  Procedure-specific frequency analysis examines billing
variability metrics, including standard deviation and  patterns for individual service codes. Certain high-value
coefficient of variation, quantify consistency of billing  procedures have expected frequency ranges based on
patterns  over  time.  Sudden  changes  in  frequency  population health statistics and specialty practice norms.
detected by comparing consecutive period statistics may  The  extraction  methodology  maintains  reference
indicate the potential onset of fraudulent activity or  frequency distributions for common procedures derived
shifts  in  fraud  tactics.  The  extraction  pipeline  from  aggregated  claims  data.  Provider-specific
implements  change  point  detection  algorithms  to  frequencies  are  compared  against  these  reference
distributions to compute statistical divergence scores.
Vol. 6(4), pp. 27-49, April 2026
[31]

Journal of Advanced Computing Systems (JACS) ISSN: 3066-3962
Disproportionate billing of specific high-reimbursement different service codes. Abnormally concentrated
procedures represents a common fraud indicator. The billing on limited procedure sets suggests potential
feature set includes procedure diversity metrics upcoding or phantom billing schemes targeting specific
measuring the distribution of claim volumes across reimbursement opportunities.
Table 2: Frequency Distribution Feature Summary
Feature Type Statistical Measures Anomaly Indicators
Mean: 23.4 claims/day, Std: 8.7, CV:
Daily Frequency Sudden spikes >3 std deviations
0.37
Mean: 164.2 claims/week, Skewness: High skewness indicating concentrated
Weekly Frequency
0.82 bursts
Mean: 710.8 claims/month, Kurtosis: High kurtosis revealing extreme billing
Monthly Frequency
4.3 spikes
Procedure-Specific KL divergence: 0.43, JS divergence:
Large divergence from peer distributions
Frequency 0.28
Shannon entropy: 3.2 bits (legitimate:
Temporal Entropy Low entropy indicating structured patterns
4.8)
Figure 1 illustrates the temporal distribution patterns
observed in legitimate versus fraudulent provider billing
behaviors across a twelve-month observation period.
Figure 1: Temporal Billing Frequency Distributions
Vol. 6(4), pp. 27-49, April 2026
[32]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

This visualization presents a multi-panel comparative  adaptive smoothing that emphasizes recent observations
analysis  displaying  monthly  claim  submission  while retaining historical context. Momentum features
frequencies for three provider categories over a twelve- calculate the rate of change in moving averages to detect
month period. The top panel shows legitimate provider  acceleration or deceleration in billing patterns. These
patterns  characterized  by  relatively  stable  monthly  trend-based  features  enable  identification  of  gradual
frequencies with moderate variations ranging from 180  fraud schemes that slowly escalate billing volumes to
avoid triggering fixed threshold alerts [14].
to 240 claims per month and gradual seasonal trends
| including  | a  typical  | summer  |     | reduction  | and  year-end  |     |     |     |     |     |     |     |     |
| ---------- | ----------- | ------- | --- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Seasonal decomposition techniques separate temporal
increase. The middle panel illustrates early-stage fraud
patterns exhibiting a characteristic sudden increase in  signals into trend, seasonal, and residual components.
claim frequency beginning at month 6, rising from a  The construction methodology applies classical additive
|     |     |     |     |     |     |     | or  multiplicative  |     | decomposition  |     |     | models  | to  extract  |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------------- | --- | --- | ------- | ------------ |
baseline of 200 claims per month to over 400 claims by
seasonality patterns with annual, quarterly, or monthly
month 12, with a steep linear growth trajectory. The
periodicities. Residual components after removing trend
| bottom  | panel  | depicts  | sophisticated  |     | fraud  | patterns  |     |     |     |     |     |     |     |
| ------- | ------ | -------- | -------------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
showing periodic spikes every three months in claim  and seasonal effects represent deviations from expected
frequencies  reaching  500  claims,  alternating  with  patterns that may indicate anomalous behavior. The
|     |     |     |     |     |     |     | feature  | set  | includes  | seasonal  |     | strength  | metrics  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --------- | --------- | --- | --------- | -------- |
baseline periods around 200 claims, creating a sawtooth
quantifying the magnitude of periodic variations relative
| pattern  | designed  | to  | evade  | simple  | threshold-based  |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------ | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
to total signal variance. Providers with weak or absent
| detection  | systems.  | Each  | panel  | includes  | error  | bars  |     |     |     |     |     |     |     |
| ---------- | --------- | ----- | ------ | --------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
representing the standard deviation within provider peer  seasonal patterns despite specialty norms raise suspicion
groups, demonstrating that fraudulent patterns extend  of artificial billing unconnected to actual patient care
cycles. De-seasoned features enable fair comparison
| significantly  | beyond  |     | normal  | variation  | ranges.  | The  |     |     |     |     |     |     |     |
| -------------- | ------- | --- | ------- | ---------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
across different calendar periods by removing legitimate
visualization employs a consistent color scheme with
periodic variations.
blue lines representing actual frequencies, gray shaded
regions indicating normal variation ranges defined as
|     |     |     |     |     |     |     | Distributional  |     | distance  | features  | measure  |     | divergence  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --------- | -------- | --- | ----------- |
mean plus or minus two standard deviations, and red
|     |     |     |     |     |     |     | between  | observed  | temporal  |     | patterns  | and  | reference  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --------- | --- | --------- | ---- | ---------- |
dotted lines marking regulatory threshold levels. This
distributions representing normal behavior. Kullback-
| multi-scale  |     | temporal  | representation  |     |     | enables  |                |             |     |             |     |              |       |
| ------------ | --- | --------- | --------------- | --- | --- | -------- | -------------- | ----------- | --- | ----------- | --- | ------------ | ----- |
|              |     |           |                 |     |     |          | Leibler  (KL)  | divergence  |     | quantifies  |     | information  | loss  |
investigators to visually distinguish between legitimate
|           |            |      |            |     |          |           | when  using  | a   | reference  | distribution  |     | to  | approximate  |
| --------- | ---------- | ---- | ---------- | --- | -------- | --------- | ------------ | --- | ---------- | ------------- | --- | --- | ------------ |
| practice  | variation  | and  | anomalous  |     | billing  | patterns  |              |     |            |               |     |     |              |
observed patterns. Jensen-Shannon divergence provides
requiring detailed investigation.
|     |     |     |     |     |     |     | a  symmetric  |     | alternative  |     | suitable  | for  | comparing  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | --------- | ---- | ---------- |
3.2. Statistical and Machine Learning-based Feature  distributions without requiring absolute continuity. The
Construction  construction  framework  computes  these  distance
|     |     |     |     |     |     |     | metrics  comparing  |     | individual  |     | provider  |     | distributions  |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------- | --- | --------- | --- | -------------- |
Statistical Transformation Features  against peer group benchmarks. Earth mover's distance
|              |                 |     |          |            |     |          | captures  | the  | minimal  | cost  | of  | transforming  | one  |
| ------------ | --------------- | --- | -------- | ---------- | --- | -------- | --------- | ---- | -------- | ----- | --- | ------------- | ---- |
| Statistical  | transformation  |     | methods  | construct  |     | derived  |           |      |          |       |     |               |      |
distribution into another, providing an intuitive measure
| features  | that          | capture  | nonlinear  | relationships  |         | and    |                     |     |                 |     |        |                 |     |
| --------- | ------------- | -------- | ---------- | -------------- | ------- | ------ | ------------------- | --- | --------------- | --- | ------ | --------------- | --- |
|           |               |          |            |                |         |        | of  distributional  |     | dissimilarity.  |     | These  | distance-based  |     |
| complex   | dependencies  |          | within     | temporal       | claims  | data.  |                     |     |                 |     |        |                 |     |
features effectively detect subtle deviations from normal
Moving average features smooth short-term fluctuations  patterns  that  may  escape  simpler  threshold-based
to reveal underlying trends. The construction process  detection methods. Table 3 summarizes the statistical
| computes  | simple  | moving  | averages  |     | across  | multiple  |                 |     |           |      |        |        |            |
| --------- | ------- | ------- | --------- | --- | ------- | --------- | --------------- | --- | --------- | ---- | ------ | ------ | ---------- |
|           |         |         |           |     |         |           | transformation  |     | features  | and  | their  | fraud  | detection  |
window sizes ranging from seven days to ninety days.
relevance.
| Exponentially  |     | weighted  | moving  | averages  |     | provide  |     |     |     |     |     |     |     |
| -------------- | --- | --------- | ------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Table 3: Statistical Transformation Features
Transformation Type  Mathematical Formula  Detection Application
Moving Average (MA)  MA_t = Σ(x_{t-i})/n for i=0 to n-1  Smooths fluctuations revealing underlying trends
| Exponential  |     | Weighted  | EWMA_t  |     | =   | α·x_t  | +  (1- |     |     |     |     |     |     |
| ------------ | --- | --------- | ------- | --- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- |
Adaptive smoothing emphasizing recent patterns
| MA  |     |     | α)·EWMA_{t-1}  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Momentum  M_t = MA_t - MA_{t-k}  Detects acceleration in billing volume changes
Vol. 6(4), pp. 27-49, April 2026
[33]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

Transformation Type  Mathematical Formula  Detection Application
|                         |     |     |                        |     |     |     | Separates  |     | trends  | from  | seasonal  | and  | residual  |
| ----------------------- | --- | --- | ---------------------- | --- | --- | --- | ---------- | --- | ------- | ----- | --------- | ---- | --------- |
| Seasonal Decomposition  |     |     | x_t = T_t + S_t + R_t  |     |     |     |            |     |         |       |           |      |           |
components
|                |     |     |                                     |     |     |     | Measures  |     | distribution  |     | divergence  |     | from  |
| -------------- | --- | --- | ----------------------------------- | --- | --- | --- | --------- | --- | ------------- | --- | ----------- | --- | ----- |
| KL Divergence  |     |     | D_KL(P||Q) = Σ P(x)·log(P(x)/Q(x))  |     |     |     |           |     |               |     |             |     |       |
benchmarks
Functional Principal Component Analysis  shifts. Providers systematically shifting their billing mix
toward high-reimbursement services exhibit distinctive
| Functional  | Principal  | Component  |     | Analysis  | provides  |     |                 |     |            |           |     |           |           |
| ----------- | ---------- | ---------- | --- | --------- | --------- | --- | --------------- | --- | ---------- | --------- | --- | --------- | --------- |
|             |            |            |     |           |           |     | distributional  |     | evolution  | patterns  |     | captured  | by  this  |
dimensionality reduction for temporal trajectories while  approach.  The  construction  framework  implements
preserving  essential  dynamic  characteristics.  The  efficient computational algorithms enabling application
| construction  | methodology  |     | treats  | provider  |     | billing  |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | ------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
to large-scale claims datasets containing millions of
| sequences  | as  functional  | data  | objects  | defined  |     | over  |     |     |     |     |     |     |     |
| ---------- | --------------- | ----- | -------- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
providers.
| continuous  | time  | domains.  |     | Basis  | function  |     |     |     |     |     |     |     |     |
| ----------- | ----- | --------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
representations including B-splines  or Fourier series  Recurrent Neural Network Embeddings
| approximate  | discrete  | observations  |     |     | as  smooth  |     |                       |     |     |          |               |     |            |
| ------------ | --------- | ------------- | --- | --- | ----------- | --- | --------------------- | --- | --- | -------- | ------------- | --- | ---------- |
|              |           |               |     |     |             |     | Deep  learning-based  |     |     | feature  | construction  |     | leverages  |
continuous functions. The FPCA procedure computes
eigenfunctions  representing  dominant  modes  of  recurrent neural network architectures to learn compact
temporal  variation  in  the  dataset.  Projection  of  representations  of  temporal  claims  sequences.  Long
Short-Term Memory networks process variable-length
| individual  | provider  trajectories  |          | onto  | these            | principal  |     |              |            |        |           |     |           |               |
| ----------- | ----------------------- | -------- | ----- | ---------------- | ---------- | --- | ------------ | ---------- | ------ | --------- | --- | --------- | ------------- |
|             |                         |          |       |                  |            |     | sequences    | of         | claim  | records   | to  | generate  | fixed-        |
| components  | yields                  | compact  |       | low-dimensional  |            |     |              |            |        |           |     |           |               |
|             |                         |          |       |                  |            |     | dimensional  | embedding  |        | vectors.  |     | The       | construction  |
representations capturing essential temporal structure.
The first few principal components typically explain  methodology  trains  LSTM  autoencoders  on  large
substantial  proportions  of  total  variance,  enabling  corpora  of  claim  sequences  to  learn  generalizable
|     |     |     |     |     |     |     | temporal  | patterns.  | The  | encoder  | network  |     | compresses  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ---- | -------- | -------- | --- | ----------- |
efficient representation of complex temporal patterns.
|     |     |     |     |     |     |     | input  | sequences  |     | into  128-dimensional  |     |     | latent  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | ---------------------- | --- | --- | ------- |
Provider-specific principal component scores serve as  representations while the decoder reconstructs original
derived  features  for  downstream  anomaly  detection  sequences from these representations. Reconstruction
algorithms. Extreme scores on particular components  error  serves  as  an  anomaly  indicator,  with  poor
indicate unusual temporal patterns along specific modes  reconstructions  suggesting  deviations  from  learned
of  variation.  Multivariate  outlier  detection  in  the  normal patterns. The latent representations themselves
component  score  space  identifies  providers  whose  provide  informative  features  capturing  complex
temporal dependencies [15].
temporal profiles deviate substantially from population
norms. The construction process computes both mean-
|     |     |     |     |     |     |     | Attention  | mechanisms  |     | enhance  | recurrent  |     | network  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | -------- | ---------- | --- | -------- |
level components capturing average billing intensity
and  variance  components  representing  temporal  representations  by  identifying  important  time  steps
volatility. Providers with unusual combinations of mean  within sequences. The construction process implements
attention layers that compute weighted combinations of
| and  variance  | characteristics      |     | emerge   |     | as  high-risk  |     |         |         |         |           |             |     |            |
| -------------- | -------------------- | --- | -------- | --- | -------------- | --- | ------- | ------- | ------- | --------- | ----------- | --- | ---------- |
|                |                      |     |          |     |                |     | hidden  | states  | across  | temporal  | positions.  |     | Attention  |
| candidates     | for  investigation.  |     | Loading  |     | patterns       | on  |         |         |         |           |             |     |            |
weights indicate which time periods contribute most to
principal components provide interpretable insights into
specific  temporal  characteristics  that  distinguish  final representations, providing interpretability for deep
anomalous providers.  learning  features.  Providers  with  unusual  attention
patterns focusing on specific temporal windows may
Distributional functional principal component analysis  exhibit targeted fraud strategies active during particular
extends  the  methodology  to  capture  evolution  of  periods.  The  embedding  extraction  framework
probability  distributions  over  time.  Rather  than  processes  claims  sequences  through  pre-trained
modeling  scalar-valued  functions,  the  approach  networks to generate 128-dimensional feature vectors
represents empirical claim distributions at each time  suitable for conventional machine learning algorithms.
point. The procedure computes principal components of  This  hybrid  approach  combines  deep  learning
distribution-valued  functions,  capturing  modes  of  representation  power  with  the  interpretability  and
variation in how providers' claim distributions evolve  calibration properties of traditional methods.
| temporally.  | This  sophisticated  |     | representation  |     |     | detects  |     |     |     |     |     |     |     |
| ------------ | -------------------- | --- | --------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Graph neural networks provide alternative embedding
| fraud  | patterns  that  | manifest  | through  |     | changes  | in  |     |     |     |     |     |     |     |
| ------ | --------------- | --------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
distributional characteristics rather than simple mean  approaches  for  claims  data  by  explicitly  modeling
|     |     |     |     |     |     |     | relationships  |     | between  | entities.  |     | The  | construction  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ---------- | --- | ---- | ------------- |
Vol. 6(4), pp. 27-49, April 2026
[34]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

methodology represents claims data as heterogeneous  generated  through  these  graph-based  approaches
graphs  with  nodes  for  providers,  beneficiaries,  and  capture both individual temporal patterns and relational
procedures  connected  by  edges  representing  claims  context within broader healthcare delivery networks.
transactions.  Graph  convolutional  layers  aggregate  Collusive fraud schemes involving coordinated activity
information from local neighborhoods to compute node  across  multiple  providers  emerge  through  unusual
embeddings.  Temporal  graph  networks  extend  this  embedding  patterns  reflecting  anomalous  graph
| framework  | by  incorporating   | edge  timestamps  | and         | structures.  |     |
| ---------- | ------------------- | ----------------- | ----------- | ------------ | --- |
| evolving   | graph  structures.  | Provider          | embeddings  |              |     |
Table 4: Deep Learning Feature Construction Performance
Architecture  Embedding Dimension  Training Time (hours)  Detection Rate Improvement
| LSTM Autoencoder        |     | 128  |     | 14.3  | +0.06 (0.81→0.87)  |
| ----------------------- | --- | ---- | --- | ----- | ------------------ |
| LSTM with Attention     |     | 128  |     | 18.7  | +0.07 (0.81→0.88)  |
| Bidirectional LSTM      |     | 256  |     | 22.1  | +0.08 (0.81→0.89)  |
| Graph Neural Network    |     | 64   |     | 31.5  | +0.05 (0.81→0.86)  |
| Temporal Graph Network  |     | 64   |     | 38.9  | +0.06 (0.81→0.87)  |
Figure 2 visualizes the embedding space learned by the  dimensions  using  t-distributed  Stochastic  Neighbor
LSTM  autoencoder  network,  projecting  high- Embedding (t-SNE) dimensionality reduction.
| dimensional  | temporal  | representations  | into  two  |     |     |
| ------------ | --------- | ---------------- | ---------- | --- | --- |
Figure 2: LSTM Autoencoder Embedding Space Visualization

This  two-dimensional  scatter  plot  displays  t-SNE  cluster  with  smooth  gradients  indicating  continuous
projections  of  128-dimensional  LSTM  autoencoder  variation in normal billing patterns. Red points (n=300)
embeddings for 5,000 healthcare providers. Each point  mark confirmed fraudulent providers primarily located
represents a single provider's temporal billing pattern  in the periphery of the embedding space, with three
encoded as a latent vector. Color coding distinguishes  distinct sub-clusters corresponding to different fraud
three  provider  categories:  blue  points  (n=4,650)  types: Type A fraud involving phantom billing in the
represent legitimate providers forming a dense central  upper-right quadrant showing embeddings distant from
Vol. 6(4), pp. 27-49, April 2026
[35]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

legitimate clusters, Type B fraud involving upcoding  by  linear  correlation.  Features  with  high  mutual
schemes in the lower-left region exhibiting moderate  information receive priority in the selected subset. Chi-
separation, and Type C fraud involving excessive billing  square tests for categorical features assess independence
in the lower-right corner displaying partial overlap with  from  fraud  labels,  with  high  chi-square  statistics
legitimate provider distributions. Yellow points (n=50)  indicating informative features.
| indicate      | providers  |            | under  | investigation  |             | occupying  |      |                 |       |            |          |              |               |         |
| ------------- | ---------- | ---------- | ------ | -------------- | ----------- | ---------- | ---- | --------------- | ----- | ---------- | -------- | ------------ | ------------- | ------- |
|               |            |            |        |                |             |            |      | Variance-based  |       | selection  |          | removes      | low-variance  |         |
| intermediate  |            | positions  |        | between        | legitimate  |            | and  |                 |       |            |          |              |               |         |
|               |            |            |        |                |             |            |      | features        | that  | provide    | minimal  | information  |               | across  |
confirmed fraud clusters, suggesting behavioral patterns
|                  |     |     |                   |     |      |                |     | providers.  | Features  | with  | variance  |     | below  | specified  |
| ---------------- | --- | --- | ----------------- | --- | ---- | -------------- | --- | ----------- | --------- | ----- | --------- | --- | ------ | ---------- |
| with  ambiguous  |     |     | characteristics.  |     | The  | visualization  |     |             |           |       |           |     |        |            |
includes density contours derived from kernel density  thresholds are eliminated as unlikely to discriminate
estimation,  with  darker  regions  representing  higher  between normal and anomalous patterns. Coefficient of
variation normalizes variance by mean values to enable
| concentration  |     | of  legitimate  |     | providers  |     | and  providing  |     |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
fair comparison across features with different scales.
| visual  | reference  | for  | identifying  |     | unusual  | embedding  |     |                 |     |              |     |             |     |             |
| ------- | ---------- | ---- | ------------ | --- | -------- | ---------- | --- | --------------- | --- | ------------ | --- | ----------- | --- | ----------- |
|         |            |      |              |     |          |            |     | The  selection  |     | methodology  |     | implements  |     | percentile- |
positions. Distance from the legitimate cluster centroid
marked with a black cross correlates strongly with fraud  based thresholds to retain features in the top deciles of
likelihood,  with  providers  beyond  1.5  standard  variance  or  mutual  information  distributions.
Multicollinearity analysis identifies feature groups with
| deviations  | exhibiting  |     | 73%  | fraud  | detection accuracy.  |     |     |                 |     |                |            |     |       |            |
| ----------- | ----------- | --- | ---- | ------ | -------------------- | --- | --- | --------------- | --- | -------------- | ---------- | --- | ----- | ---------- |
|             |             |     |      |        |                      |     |     | high  pairwise  |     | correlations,  | retaining  |     | only  | a  single  |
The plot demonstrates the LSTM autoencoder's ability
representative from each correlated cluster. Principal
| to  learn  | meaningful  |     | temporal  |     | representations  |     | that  |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --------- | --- | ---------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
naturally separate anomalous billing patterns in latent  component  analysis  on  feature  correlation  matrices
space, supporting subsequent classification and ranking  guides  selection  of  maximally  independent  feature
subsets spanning the full information space.
algorithms for fraud detection prioritization.
3.3. Feature Selection and Importance Ranking  Information gain and Gini importance metrics derived
|     |     |     |     |     |     |     |     | from  decision  |     | tree  algorithms  |     | provide  |     | supervised  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------- | --- | -------- | --- | ----------- |
Filter-based Selection Methods  feature ranking. The selection process trains shallow
decision trees and extracts feature importance scores
Feature selection reduces dimensionality by identifying
based on their contribution to classification accuracy.
the most informative temporal features for anomaly
Features selected for splits near tree roots receive higher
detection. Filter methods evaluate individual features
|     |     |     |     |     |     |     |     | importance  | rankings  |     | as  they  | provide  |     | maximum  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | --------- | -------- | --- | -------- |
independently  of  specific  detection  algorithms.  information  gain  for  distinguishing  fraud  cases.
Correlation  analysis  identifies  features  with  strong  Ensemble-based importance aggregates rankings across
| associations  | to        | known  | fraud  | labels  | while               | removing  |      |             |        |             |              |            |             |             |
| ------------- | --------- | ------ | ------ | ------- | ------------------- | --------- | ---- | ----------- | ------ | ----------- | ------------ | ---------- | ----------- | ----------- |
|               |           |        |        |         |                     |           |      | multiple    | trees  | to  obtain  | stable       | estimates  |             | robust  to  |
| redundant     | features  |        | with   | high    | inter-correlation.  |           | The  |             |        |             |              |            |             |             |
|               |           |        |        |         |                     |           |      | individual  | tree   | variance.   | Permutation  |            | importance  |             |
selection process computes Spearman rank correlations
evaluates feature relevance by measuring performance
between features and fraud indicators to rank features  degradation when feature values are randomly shuffled,
by discriminative power. Mutual information criteria  with large drops indicating critical features. Table 5
measure statistical dependence between features and
presents feature importance rankings across different
fraud labels, capturing nonlinear relationships missed
selection methodologies.
Table 5: Feature Importance Rankings Across Selection Methods
|     |     |     |     |     |     | Mutual  |     | Random  |     | Forest  | Permutation  |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | ------- | ------------ | --- | --- | --- |
Feature Name
|                                    |            |     |              |     |     | Information  |     | Importance  |     |     | Importance  |     |     |     |
| ---------------------------------- | ---------- | --- | ------------ | --- | --- | ------------ | --- | ----------- | --- | --- | ----------- | --- | --- | --- |
| Service-to-Submission Lag Std Dev  |            |     |              |     |     | 0.087        |     | 0.089       |     |     | 0.092       |     |     |     |
| Weekend Submission Ratio           |            |     |              |     |     | 0.074        |     | 0.077       |     |     | 0.079       |     |     |     |
| Claim                              | Frequency  |     | Coefficient  |     | of  |              |     |             |     |     |             |     |     |     |
|                                    |            |     |              |     |     | 0.069        |     | 0.071       |     |     | 0.068       |     |     |     |
Variation
| Autocorrelation Lag-7       |     |     |     |     |     | 0.066  |     | 0.068  |     |     | 0.071  |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- | ------ | --- | --- | --- |
| FPCA Principal Component 1  |     |     |     |     |     | 0.062  |     | 0.064  |     |     | 0.063  |     |     |     |
Vol. 6(4), pp. 27-49, April 2026
[36]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

Wrapper-based Selection Algorithms  optimization.  Lasso  regression  for  anomaly  scoring
|     |     |     |     |     |     |     | implements  | L1  penalties  |     | yielding  | sparse  | predictive  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | --------- | ------- | ----------- | --- |
Wrapper methods evaluate feature subsets based on
|                     |     |       |           |     |          |            | models  | with  interpretable  |     | feature  |     | subsets.  | The  |
| ------------------- | --- | ----- | --------- | --- | -------- | ---------- | ------- | -------------------- | --- | -------- | --- | --------- | ---- |
| their  performance  |     | with  | specific  |     | anomaly  | detection  |         |                      |     |          |     |           |      |
regularization parameter controls the trade-off between
algorithms.  Sequential  forward  selection  starts  with  model fit and sparsity, with larger penalties producing
empty feature sets and iteratively adds features that  sparser solutions. Cross-validation determines optimal
| maximize  | detection  |     | performance.  |     | The  | algorithm  |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
regularization strength balancing detection performance
| evaluates  | all  | remaining  | features  |     | at  each  | iteration,  |     |     |     |     |     |     |     |
| ---------- | ---- | ---------- | --------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
and feature set parsimony.
selecting the feature providing greatest improvement to
a  held-out  validation  set.  Sequential  backward  Elastic  net  combines  L1  and  L2  regularization  to
elimination  begins  with  all  features  and  iteratively  address  correlated  feature  groups.  The  methodology
removes  the  least  important  feature  based  on  maintains  stability  when  handling  highly  correlated
performance  impact.  This  computationally  intensive  temporal features by distributing weights across related
approach evaluates every possible removal candidate at  features  rather  than  arbitrarily  selecting  individual
each  step.  The  selection  process  continues  until  representatives.  Tree-based  algorithms  including
performance degradation exceeds acceptable thresholds  gradient  boosting  machines  provide  implicit  feature
or reaches target feature set sizes.  selection through split point selection. Features never
selected for splits receive zero importance and can be
Recursive  feature  elimination  implements  efficient  safely  removed.  The  embedded  selection  process
backward selection by removing multiple features per
|            |        |     |             |     |            |      | extracts  | feature  usage  | frequencies  |     | across  | boosting  |     |
| ---------- | ------ | --- | ----------- | --- | ---------- | ---- | --------- | --------------- | ------------ | --- | ------- | --------- | --- |
| iteration  | based  | on  | importance  |     | rankings.  | The  |           |                 |              |     |         |           |     |
iterations and eliminates features falling below usage
methodology trains detection algorithms on full feature
thresholds. Random forest importance scores aggregate
sets and extracts feature importance scores. Features  feature  contributions  across  ensemble  members,
with lowest importance are removed in batches, with  providing  stable  importance  estimates  for  selection
algorithm retraining and importance re-evaluation after
decisions.
| each  elimination  |     | round.  | Cross-validation  |     |     | estimates  |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | ----------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
performance for each feature subset size to identify  Neural  network-based  selection  employs  attention
optimal  dimensionality  balancing  detection  accuracy  mechanisms  and  dropout  regularization  to  identify
and computational efficiency. The procedure generates  important features. Attention weights provide feature
performance  curves  showing  detection  metrics  as  importance  scores  interpretable  as  selection
functions of feature set size, enabling informed selection  probabilities. Dropout rates calibrated during training
of appropriate feature subset cardinalities for production  indicate  feature  redundancy,  with  high  dropout
deployment.  tolerance  suggesting  removable  features.  The
|          |             |          |     |             |     |               | framework       | implements  | learnable  |     | feature  | selection  |          |
| -------- | ----------- | -------- | --- | ----------- | --- | ------------- | --------------- | ----------- | ---------- | --- | -------- | ---------- | -------- |
| Genetic  | algorithms  | provide  |     | stochastic  |     | optimization  |                 |             |            |     |          |            |          |
|          |             |          |     |             |     |               | masks  updated  | through     | gradient   |     | descent  | to         | jointly  |
approaches  to  feature  selection.  The  methodology  optimize feature  subsets  and  detection  performance.
represents feature subsets as binary chromosomes where  End-to-end  training  of  selection  and  detection
each gene indicates inclusion or exclusion of a feature.
|                   |     |            |     |          |     |             | components  | ensures  | selected  | features  |     | specifically  |     |
| ----------------- | --- | ---------- | --- | -------- | --- | ----------- | ----------- | -------- | --------- | --------- | --- | ------------- | --- |
| Population-based  |     | evolution  |     | through  |     | selection,  |             |          |           |           |     |               |     |
support the downstream anomaly detection task rather
crossover, and mutation operations explores the space
|     |     |     |     |     |     |     | than  general  | predictive  |     | power.  | This  | task-specific  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | ------- | ----- | -------------- | --- |
of  possible  feature  combinations.  Fitness  functions  selection improves detection performance compared to
based  on  detection  algorithm  performance  guide  generic filter or wrapper methods.
evolution toward high-quality feature subsets. Multiple
independent runs with different random initializations
4. Threshold Optimization for Early Warning
| improve  | coverage  | of  | the  search  |     | space  | and  provide  |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------------ | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
Mechanism
| ensembles  | of  | candidate  | feature  | sets.  | The  | selection  |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | -------- | ------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
framework evaluates pareto-optimal solutions trading
off  detection  performance  against  feature  set  size,  4.1. Adaptive Threshold Setting Strategies
enabling decision-makers to choose operating points
matching operational requirements and computational  Statistical Threshold Determination
constraints.
Threshold optimization for anomaly detection balances
Embedded Selection Through Regularization  sensitivity requirements against operational constraints
|     |     |     |     |     |     |     | including  | investigative  | capacity  |     | and  | alert  | fatigue.  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --------- | --- | ---- | ------ | --------- |
Embedded methods integrate feature selection directly  Statistical  approaches  establish  thresholds  based  on
into  algorithm  training  procedures  through  distributional properties of anomaly scores computed
regularization penalties. L1 regularization encourages  from historical data. Percentile-based thresholds flag
sparse  feature  weights  by  penalizing  the  absolute  providers  whose  anomaly  scores  exceed  specified
magnitude  of  coefficients.  The  resulting  models  quantiles of the score distribution. Common choices
automatically zero out uninformative features during  include the 95th or 99th percentiles corresponding to
Vol. 6(4), pp. 27-49, April 2026
[37]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

traditional  significance  levels.  The  determination  logarithmic  or  Box-Cox  transformations  normalize
process computes empirical score distributions from  skewed  score  distributions  to  improve  threshold
| training  data  | spanning  | multiple  | billing  cycles.  | calibration.  |     |     |
| --------------- | --------- | --------- | ----------------- | ------------- | --- | --- |
Thresholds are set to achieve target false positive rates
based on historical fraud prevalence. Providers scoring  Extreme value theory provides principled approaches
above thresholds receive priority for investigation based  for  setting  thresholds  in  tail  regions  where  fraud
|     |     |     |     | typically  occurs.  | Generalized  | Pareto  distributions  |
| --- | --- | --- | --- | ------------------- | ------------ | ---------------------- |
on their deviation from normal patterns.
(GPD) model exceedances over high thresholds. The
Standard deviation-based thresholds define anomalous  methodology  estimates  distribution  parameters  from
scores as those exceeding the mean by multiple standard  observed  high  scores  and  derives  thresholds
deviations. The three-sigma rule marks scores beyond  corresponding  to  desired  false  positive  rates  in  tail
three standard deviations as anomalies under Gaussian  regions.  Peak-over-threshold  methods  identify
distribution assumptions. This approach requires careful  appropriate  initial  threshold  levels  for  parameter
evaluation of distribution assumptions, as heavy-tailed  estimation by analyzing mean residual life plots. Return
score  distributions  common  in  anomaly  detection  level  calculations  determine  scores  exceeded  with
contexts  violate  normality.  Robust  variants  employ  specified  probabilities,  enabling  threshold  selection
median  absolute  deviation  (MAD)  as  an  alternative  based on risk tolerance. This sophisticated approach
scale estimate resistant to outliers. The determination  properly accounts for tail behavior critical for detecting
framework  tests  distributional  assumptions  through  rare but high-impact fraud events. Table 6 compares
goodness-of-fit  analyses  and  selects  appropriate  statistical threshold determination methodologies across
threshold  formulas  matching  observed  score  multiple evaluation criteria.
| distributions.  | Power  | transformations  | including  |     |     |     |
| --------------- | ------ | ---------------- | ---------- | --- | --- | --- |
Table 6: Statistical Threshold Determination Methods Comparison
| Method           |     | Threshold Formula  |     | Assumptions       | Robustness  |     |
| ---------------- | --- | ------------------ | --- | ----------------- | ----------- | --- |
| 95th Percentile  |     | Q_0.95             |     | None (empirical)  | High        |     |
Three Sigma Rule  μ + 3σ  Gaussian distribution  Low (sensitive to outliers)
| Median                | Absolute  |                 |          | Symmetric         |                            |                   |
| --------------------- | --------- | --------------- | -------- | ----------------- | -------------------------- | ----------------- |
|                       |           | median + k·MAD  |          |                   | High (robust to outliers)  |                   |
| Deviation             |           |                 |          | distribution      |                            |                   |
|                       |           | Based           | on  GPD  |                   | Medium  (requires          | sufficient  tail  |
| Extreme Value Theory  |           |                 |          | Tail follows GPD  |                            |                   |
|                       |           | parameters      |          |                   | data)                      |                   |
Transform then  apply σ  Data  can  be  Medium  (depends  on
Box-Cox Transformation
|     |     | rule  |     | normalized  | transformation)  |     |
| --- | --- | ----- | --- | ----------- | ---------------- | --- |
Cost-sensitive Threshold Optimization  assess cost-optimal threshold stability across ranges of
assumed cost parameters.
| Cost-sensitive  | approaches  | explicitly  | incorporate  |     |     |     |
| --------------- | ----------- | ----------- | ------------ | --- | --- | --- |
asymmetric  misclassification  costs  into  threshold  Budget-constrained  optimization  selects  thresholds
selection. False negatives represent missed fraud cases  respecting  investigative  capacity  limits.  The
incurring  losses  proportional  to  fraudulent  claim  methodology  incorporates  constraints  on  maximum
amounts.  False  positives  consume  investigative  investigation  volumes  into  threshold  selection
resources without recovery benefits. The optimization  procedures.  Linear  programming  formulations
framework  formulates  threshold  selection  as  maximize  fraud  detection  subject  to  resource
minimizing expected cost combining fraud losses and  constraints. Threshold selection operates in conjunction
investigation costs. Cost matrices define penalties for  with alert prioritization to ensure investigation budgets
different error types based on average fraud amounts  target  highest-risk  providers.  The  framework
and  investigation  resource  requirements.  Threshold  implements  dynamic  programming  algorithms
determination  procedures  evaluate  expected  costs  efficiently solving large-scale constrained optimization
across candidate threshold values and select thresholds  problems.  Lagrangian  relaxation  techniques  convert
minimizing  total  expected  cost.  Sensitivity  analyses  hard constraints into penalty terms enabling gradient-
Vol. 6(4), pp. 27-49, April 2026
[38]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

based  optimization.  Multi-objective  optimization  Reinforcement learning formulates threshold selection
addresses trade-offs between detection performance and  as sequential decision-making under uncertainty. The
resource consumption through Pareto frontier analysis.  agent observes current system state including recent
|     |     |     |     |     |     |     |     | alert  volumes,  |     | investigation  |     | outcomes,  | and  | fraud  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------- | --- | ---------- | ---- | ------ |
Risk-adjusted  thresholds  vary  by  provider  statistics.  Actions  consist  of  threshold  adjustments
characteristics including specialty, practice size, and  increasing or decreasing sensitivity. Rewards combine
geographic location. The optimization process stratifies
|     |     |     |     |     |     |     |     | detection  | performance  |     | metrics  | with  | operational  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | -------- | ----- | ------------ | --- |
providers into homogeneous subgroups and establishes
|     |     |     |     |     |     |     |     | efficiency  | measures.  |     | Q-learning  | algorithms  |     | learn  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ----------- | ----------- | --- | ------ |
group-specific thresholds. This approach accounts for
|     |     |     |     |     |     |     |     | optimal  | threshold  |     | policies  | maximizing  | cumulative  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------- | ----------- | ----------- | --- |
legitimate  practice  variation  across  provider  types  rewards over time. Policy gradient methods directly
reducing false positives from specialty-specific patterns.  optimize  parameterized  threshold  functions  through
| Hierarchical  | modeling  |     | estimates  |     | group-level  |     | and  |     |     |     |     |     |     |     |
| ------------- | --------- | --- | ---------- | --- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
gradient ascent on expected rewards. Experience replay
| provider-level  |     | parameters  |     | simultaneously  |     |     | through  |                      |     |     |             |             |               |     |
| --------------- | --- | ----------- | --- | --------------- | --- | --- | -------- | -------------------- | --- | --- | ----------- | ----------- | ------------- | --- |
|                 |     |             |     |                 |     |     |          | stabilizes learning  |     |     | by reusing  | historical  | state-action- |     |
partial pooling. Shrinkage estimation balances group
reward tuples during training.
averages with individual provider data to obtain stable
threshold estimates even for small provider subgroups.  Online learning enables continuous threshold adaptation
The  stratified  threshold  framework  requires  careful  as  new  fraud  cases  and  investigation  outcomes
management  of  threshold  proliferation  to  maintain  accumulate.  Stochastic  gradient  descent  updates
operational  simplicity  while  capturing  relevant  threshold parameters based on mini-batches of recent
heterogeneity.  data. Adaptive learning rates including AdaGrad and
|     |     |     |     |     |     |     |     | Adam  | optimize  | convergence  |     | speed  | and  | stability.  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ------------ | --- | ------ | ---- | ----------- |
Machine Learning-based Threshold Learning
|     |     |     |     |     |     |     |     | Concept  | drift  | detection  |     | triggers  rapid  |     | threshold  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | --- | ---------------- | --- | ---------- |
recalibration when statistical tests identify significant
Machine learning approaches learn optimal thresholds
|           |       |             |            |     |            |     |       | distribution  |     | shifts.  | The  online  | learning  | framework  |     |
| --------- | ----- | ----------- | ---------- | --- | ---------- | --- | ----- | ------------- | --- | -------- | ------------ | --------- | ---------- | --- |
| directly  | from  | historical  | detection  |     | outcomes.  |     | Meta- |               |     |          |              |           |            |     |
maintains computational efficiency suitable for real-
| learning    | frameworks  |     | treat  threshold  |             | selection  |     | as  a    |       |             |     |          |              |     |         |
| ----------- | ----------- | --- | ----------------- | ----------- | ---------- | --- | -------- | ----- | ----------- | --- | -------- | ------------ | --- | ------- |
|             |             |     |                   |             |            |     |          | time  | deployment  |     | through  | incremental  |     | update  |
| supervised  | learning    |     | problem           | predicting  |            |     | optimal  |       |             |     |          |              |     |         |
procedures requiring minimal computation per update.
thresholds from data characteristics and performance
|            |           |     |           |           |     |             |     | Exponential  |     | forgetting  | weights  | emphasize  |     | recent  |
| ---------- | --------- | --- | --------- | --------- | --- | ----------- | --- | ------------ | --- | ----------- | -------- | ---------- | --- | ------- |
| feedback.  | Training  |     | datasets  | comprise  |     | historical  |     |              |     |             |          |            |     |         |
observations while retaining long-term stability through
| threshold  | settings  | and  | corresponding  |     |     | performance  |     |          |        |                 |     |             |       |           |
| ---------- | --------- | ---- | -------------- | --- | --- | ------------ | --- | -------- | ------ | --------------- | --- | ----------- | ----- | --------- |
|            |           |      |                |     |     |              |     | gradual  | decay  | of  historical  |     | influence.  | This  | adaptive  |
metrics across diverse data conditions. Random forest
|     |     |     |     |     |     |     |     | approach  | maintains  |     | detection  | effectiveness  |     | as  fraud  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ---------- | -------------- | --- | ---------- |
regressors predict optimal thresholds for new data based
tactics evolve and operational environments change.
on statistical properties including score distributions,
| fraud  | prevalence,  | and  | operational  |     | constraints.  |     | The  |     |     |     |     |     |     |     |
| ------ | ------------ | ---- | ------------ | --- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Figure 3 illustrates the relationship between detection
| learning  | framework  |     | continuously  |     | updates  | threshold  |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
thresholds and operational performance metrics across a
models incorporating recent performance data enabling  range of threshold values.
adaptation to changing fraud patterns and operational
conditions.
Figure 3: Threshold Performance Trade-off Curves
Vol. 6(4), pp. 27-49, April 2026
[39]

Journal of Advanced Computing Systems (JACS) ISSN: 3066-3962
This multi-curve line graph displays four key considerations. The Youden index maximizes the sum
performance metrics as functions of anomaly score of sensitivity and specificity, identifying thresholds
threshold values ranging from 0.1 to 0.9 on the x-axis. where vertical distance from the diagonal reference line
The primary y-axis on the left shows detection rate (blue reaches maximum. This approach treats false positives
solid line) and false positive rate (red solid line) both and false negatives equally. Alternative criteria weight
ranging from 0 to 1.0. The secondary y-axis on the right error types differently. The closest-to-corner criterion
displays daily investigation volume (green dashed line, minimizes Euclidean distance from the perfect
ranging 0-500 cases) and estimated cost savings (purple classification point at coordinates (0,1). Cost-weighted
dotted line, ranging 0-10 million dollars). The detection distance metrics incorporate asymmetric
rate curve demonstrates expected monotonic decrease misclassification costs through appropriate distance
from 0.98 at threshold 0.1 to 0.45 at threshold 0.9, with function modifications. The analysis framework enables
the steepest decline occurring between thresholds 0.3 interactive exploration of threshold options with
and 0.5. The false positive rate exhibits similar immediate visualization of corresponding performance
decreasing behavior dropping from 0.35 at threshold 0.1 metrics.
to 0.02 at threshold 0.9. Investigation volume closely
tracks false positive rate, ranging from 450 daily cases Precision-recall (PR) curves provide alternative
at low thresholds to 15 cases at high thresholds. Cost performance visualization emphasizing behavior under
savings curve shows a characteristic inverted U-shape class imbalance. Precision measures positive predictive
peaking at 8.2 million dollars at threshold 0.60, value while recall equals sensitivity. PR curves better
representing the optimal balance point where detection capture performance characteristics relevant for fraud
benefits exceed investigation costs. This peak detection where anomalies represent small minorities.
corresponds to a detection rate of 0.79, false positive Average precision summarizes PR curve performance
rate of 0.03, and investigation volume of 64 cases per through weighted average of precision values at each
day. Shaded regions indicate 95% confidence intervals threshold. The F-beta score generalizes the F1 score
derived from bootstrap resampling, with widening through adjustable balance between precision and recall.
intervals at extreme threshold values reflecting Beta values less than one emphasize precision while
increased uncertainty. Vertical reference lines mark values exceeding one prioritize recall. The optimization
three operating points: conservative threshold at 0.65 framework selects thresholds maximizing chosen
prioritizing specificity, balanced threshold at 0.60 performance metrics subject to operational constraints
maximizing cost savings, and aggressive threshold at on investigation volumes and acceptable false positive
rates.
0.25 prioritizing sensitivity. The visualization enables
stakeholders to visualize multi-dimensional trade-offs
Cost-benefit Analysis Framework
inherent in threshold selection and select operating
points aligned with organizational priorities regarding Quantitative cost-benefit analysis translates detection
detection coverage, investigation capacity, and cost- performance into financial terms enabling business-
effectiveness. oriented threshold selection. The framework assigns
monetary values to different detection outcomes. True
4.2. Trade-off Analysis Between False Positives and
positive identifications prevent fraud losses
False Negatives
proportional to typical fraudulent claim amounts. False
ROC Curve Analysis and Optimal Operating Points positive investigations incur costs reflecting resource
consumption without recovery. False negatives
Receiver operating characteristic curves provide represent missed fraud accumulating undetected losses.
comprehensive visualization of detection trade-offs True negatives correctly classified legitimate providers
across all possible threshold values. The ROC consume no investigation resources. The analysis
framework plots true positive rate against false positive computes expected costs or net benefits for candidate
rate as threshold varies from most to least conservative. thresholds by combining detection rates with outcome
Area under the ROC curve (AUC-ROC) quantifies valuations. Optimal thresholds maximize expected net
overall detection capability independent of specific benefit balancing fraud prevention against investigation
threshold choices. Perfect detectors achieve AUC of 1.0 expenses.
while random guessing yields AUC of 0.5. The analysis
compares multiple detection algorithms and temporal Sensitivity analysis explores threshold robustness
feature sets through AUC comparisons. Partial AUC across ranges of cost assumptions. Parameter
metrics focus evaluation on clinically relevant operating uncertainty regarding average fraud amounts and
regions with acceptable false positive rates. DeLong investigation costs necessitates evaluation across
tests assess statistical significance of AUC differences plausible value ranges. Monte Carlo simulation samples
between competing approaches. cost parameters from specified distributions and
computes optimal thresholds for each sample.
Optimal operating point selection from ROC curves Distribution of optimal thresholds across simulations
depends on operational objectives and cost quantifies selection uncertainty attributable to cost
Vol. 6(4), pp. 27-49, April 2026
[40]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

estimation  errors.  Robust  thresholds  perform  well  deterrence  benefits  through  reduced  future  fraud
across  broad  parameter  ranges  providing  stability  prevalence.  Recovery  efforts  following  fraud
against  cost  misspecification.  Scenario  analysis  identification recoup portions of losses through civil
evaluates  thresholds  under  discrete  alternative  cost  actions  or  criminal  prosecution.  Expected  recovery
assumptions  representing  optimistic,  realistic,  and  amounts depend on provider assets and legal framework
pessimistic projections. Break-even analysis identifies  characteristics.  Time  value  of  money  considerations
conditions under which different threshold strategies  discount  future  benefits  appropriately.  The
achieve cost equivalence.  comprehensive  cost-benefit  model  aggregates
|     |     |     |     |     |     |     | immediate  | detection  | benefits  |     | with  | longer-term  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --------- | --- | ----- | ------------ |
Long-term value considerations incorporate dynamic  deterrence  and  recovery  effects  providing  holistic
aspects of fraud detection including deterrence effects  threshold  optimization  accounting  for  full  program
and recovery potential. Successful fraud detection may
impact beyond immediate operational metrics. Table 7
| deter  future  |     | fraudulent  | activity  | through  | perceived  |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
presents detailed cost-benefit calculations for threshold
| enforcement  |     | risk.  The  | valuation  | framework  |     | models  |     |     |     |     |     |     |
| ------------ | --- | ----------- | ---------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
selection.
Table 7: Cost-Benefit Analysis for Threshold Selection
Detection  False  Positive  Annual  Fraud  Investigation  Cost  Net  Benefit
Threshold
|       |     | Rate  |     | Rate  |     | Prevented ($M)  |     | ($M)   |     |     | ($M)   |     |
| ----- | --- | ----- | --- | ----- | --- | --------------- | --- | ------ | --- | --- | ------ | --- |
| 0.30  |     | 0.92  |     | 0.15  |     | 442.0           |     | 319.5  |     |     | 122.5  |     |
| 0.45  |     | 0.87  |     | 0.06  |     | 418.0           |     | 127.8  |     |     | 290.2  |     |
| 0.60  |     | 0.79  |     | 0.03  |     | 379.5           |     | 63.9   |     |     | 315.6  |     |
| 0.75  |     | 0.68  |     | 0.01  |     | 326.6           |     | 21.3   |     |     | 305.3  |     |
Multi-objective Optimization Approaches  minimize  distance  from  these  aspirations.  Different
weight specifications generate different Pareto-optimal
| Multi-objective  |     | optimization  |               | addresses  |     | threshold  |            |               |                  |              |               |          |
| ---------------- | --- | ------------- | ------------- | ---------- | --- | ---------- | ---------- | ------------- | ---------------- | ------------ | ------------- | -------- |
|                  |     |               |               |            |     |            | solutions  | enabling      | systematic       | exploration  |               | of  the  |
| selection        | as  | simultaneous  | optimization  |            | of  | multiple   |            |               |                  |              |               |          |
|                  |     |               |               |            |     |            | frontier.  | Evolutionary  | multi-objective  |              | optimization  |          |
potentially  conflicting  objectives.  Detection  rate  algorithms including Non-dominated Sorting Genetic
maximization  conflicts  with  false  positive  rate  Algorithm  II  (NSGA-II)  maintain  populations  of
| minimization.  |       | Investigation  |             | volume     | constraints  |           |                 |            |                   |         |                 |             |
| -------------- | ----- | -------------- | ----------- | ---------- | ------------ | --------- | --------------- | ---------- | ----------------- | ------- | --------------- | ----------- |
|                |       |                |             |            |              |           | candidate       | solutions  | evolving          | toward  | Pareto-optimal  |             |
| compete        | with  | fraud          | loss        | reduction  | goals.       | The       |                 |            |                   |         |                 |             |
|                |       |                |             |            |              |           | regions.        | These      | population-based  |         |                 | approaches  |
| optimization   |       | framework      | formulates  | these      | as           | distinct  |                 |            |                   |         |                 |             |
|                |       |                |             |            |              |           | simultaneously  | discover   | multiple          |         | efficient       | solutions   |
objective functions requiring joint consideration. Pareto  providing comprehensive threshold options.
efficiency concepts identify threshold solutions where
no objective can improve without degrading others. The  Lexicographic  optimization  handles  objective
Pareto frontier traces optimal trade-off surfaces in multi- hierarchies  by  optimizing  objectives  sequentially
dimensional  objective  space.  Decision-makers  select  according to priority orderings. Primary objectives are
final thresholds from Pareto-optimal alternatives based  optimized first with secondary objectives considered
on  subjective  preference  weights  across  objectives.  only among solutions optimal for primary objectives.
Interactive  visualization  tools  enable  exploration  of  This  approach  suits  contexts  with  clear  priority
Pareto  frontiers  supporting  informed  threshold  structures,  such  as  mandatory  detection  rate
selection.  requirements  followed  by  cost  minimization  within
compliant solutions. Satisficing frameworks establish
Scalarization methods convert multi-objective problems
|                         |     |     |               |          |     |           | minimum  | acceptable  | levels  | for  | each  | objective,  |
| ----------------------- | --- | --- | ------------- | -------- | --- | --------- | -------- | ----------- | ------- | ---- | ----- | ----------- |
| into  single-objective  |     |     | formulations  | through  |     | weighted  |          |             |         |      |       |             |
restricting optimization to feasible regions satisfying all
combinations of objectives. Linear scalarization sums  constraints.  Multi-attribute  utility  theory  provides
weighted  objective  values  with  weights  reflecting  formal frameworks for aggregating multiple objectives
| relative   | importance.  |     | Achievement  |            | scalarization  |        |          |          |                      |     |                 |     |
| ---------- | ------------ | --- | ------------ | ---------- | -------------- | ------ | -------- | -------- | -------------------- | --- | --------------- | --- |
|            |              |     |              |            |                |        | through  | utility  | functions  encoding  |     | decision-maker  |     |
| minimizes  | maximum      |     | weighted     | deviation  | from           | ideal  |          |          |                      |     |                 |     |
preferences. The elicitation process determines utility
| objective  | values.      | Reference  |         | point  methods  |            | specify  |           |             |          |             |     |              |
| ---------- | ------------ | ---------- | ------- | --------------- | ---------- | -------- | --------- | ----------- | -------- | ----------- | --- | ------------ |
|            |              |            |         |                 |            |          | function  | parameters  | through  | preference  |     | elicitation  |
| desired    | performance  |            | levels  | for  each       | objective  | and      |           |             |          |             |     |              |
Vol. 6(4), pp. 27-49, April 2026
[41]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

procedures including pairwise comparisons and lottery  drift  episodes.  Periodic  retraining  schedules  provide
assessments.  Resulting  utility  functions  enable  fallback recalibration even absent explicit drift signals
principled  threshold  selection  maximizing  overall  ensuring continued performance.
utility.
Feedback-driven Threshold Adaptation
4.3. Dynamic Threshold Adjustment Algorithms
Investigation outcomes provide valuable feedback for
Concept Drift Detection and Response  threshold refinement. Each investigated case labeled as
|     |     |     |     |     |     |     | fraudulent  | or  | legitimate  | updates  | knowledge  |     | about  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | -------- | ---------- | --- | ------ |
Concept drift occurs when statistical properties of fraud
detection algorithm behavior. Confirmed fraud cases
patterns  change  over  time,  degrading  detection  misclassified  as  normal  indicate  threshold  settings
performance  of  models  trained  on  historical  data.  lacking  adequate  sensitivity.  False  positive
| Temporal       | evolution       |            | of           | fraud      | tactics  | requires     |                 |              |           |             |              |     |          |
| -------------- | --------------- | ---------- | ------------ | ---------- | -------- | ------------ | --------------- | ------------ | --------- | ----------- | ------------ | --- | -------- |
|                |                 |            |              |            |          |              | investigations  |              | flagging  | legitimate  | providers    |     | suggest  |
| corresponding  |                 | threshold  | adjustments  |            |          | maintaining  |                 |              |           |             |              |     |          |
|                |                 |            |              |            |          |              | excessive       | sensitivity  |           | requiring   | relaxation.  |     | The      |
| detection      | effectiveness.  |            | Drift        | detection  |          | algorithms   |                 |              |           |             |              |     |          |
adaptation mechanism tracks recent false positive rates
monitor performance metrics and statistical properties  comparing against target levels established during initial
to identify significant distribution shifts. Page-Hinkley  calibration.  Proportional-Integral-Derivative  (PID)
test tracks cumulative sums of performance deviations
control algorithms adjust thresholds proportionally to
| from  | expected  | levels,  | triggering  |     | alarms  | when  |     |     |     |     |     |     |     |
| ----- | --------- | -------- | ----------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
discrepancies between observed and target false positive
| cumulative  | deviations  |     | exceed  | control  |     | limits.  The  |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | ------- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
rates. Integral control components accumulate historical
detection framework establishes baseline performance  errors preventing persistent biases. Derivative control
during initial deployment and tracks deviations through  terms  respond  to  rate  of  change  in  performance
statistical process control charts. Control limits based on
preventing oscillation.
historical variation define normal performance ranges
with exceedances indicating potential drift requiring  Bayesian updating provides principled frameworks for
threshold recalibration.  incorporating investigation feedback. Prior distributions
encode initial threshold beliefs based on training data.
| Statistical  | distance  |     | measures  | quantify  |     | distribution  |                |     |           |     |             |             |     |
| ------------ | --------- | --- | --------- | --------- | --- | ------------- | -------------- | --- | --------- | --- | ----------- | ----------- | --- |
|              |           |     |           |           |     |               | Investigation  |     | outcomes  |     | constitute  | likelihood  |     |
divergence  between  current  and  reference  periods.  information  updating  these  beliefs.  Posterior
Kullback-Leibler  divergence  computed  from  recent  distributions  reflect  refined  threshold  knowledge
anomaly score distributions compared against historical
|             |          |     |              |          |             |     | combining  |     | prior  information  |     | with  | accumulating  |     |
| ----------- | -------- | --- | ------------ | -------- | ----------- | --- | ---------- | --- | ------------------- | --- | ----- | ------------- | --- |
| references  | detects  |     | significant  | shifts.  | Kolmogorov- |     |            |     |                     |     |       |               |     |
evidence. The adaptation process samples thresholds
Smirnov tests assess differences between cumulative
|     |     |     |     |     |     |     | from  posterior  |     | distributions  |     | enabling  | probabilistic  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------- | --- | --------- | -------------- | --- |
distribution  functions  providing  nonparametric  drift  threshold  selection.  Sequential  Bayesian  updating
detection.  The  monitoring  system  computes  these  naturally handles streaming feedback as investigation
statistics over rolling windows and triggers recalibration
outcomes arrive. Conjugate prior specifications enable
| when  divergence  |     | exceeds  | predetermined  |     |     | thresholds.  |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | -------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
closed-form posterior updates ensuring computational
Adaptive windowing balances responsiveness to recent
|     |     |     |     |     |     |     | efficiency.  | Non-conjugate  |     |     | cases  employ  | variational  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | --- | -------------- | ------------ | --- |
changes  against  stability  provided  by  larger  sample  approximations or Markov chain Monte Carlo (MCMC)
sizes.  Exponentially  weighted  statistics  emphasize  sampling.  The  probabilistic  framework  provides
recent observations while retaining longer-term context.
confidence intervals quantifying threshold uncertainty
| The  drift  | response  |     | protocol  | initiates  |     | threshold  |     |     |     |     |     |     |     |
| ----------- | --------- | --- | --------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
decreasing as evidence accumulates.
| reoptimization  |     | using  | recent  | data  when  |     | drift  signals  |     |     |     |     |     |     |     |
| --------------- | --- | ------ | ------- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
activate.  Active learning strategies optimally select investigation
|           |        |     |            |           |     |           | targets  | to  maximize  |     | information  | gain  | for  threshold  |     |
| --------- | ------ | --- | ---------- | --------- | --- | --------- | -------- | ------------- | --- | ------------ | ----- | --------------- | --- |
| Ensemble  | drift  |     | detection  | combines  |     | multiple  |          |               |     |              |       |                 |     |
refinement. Uncertainty sampling prioritizes providers
complementary  detection  methods  to  improve  with  anomaly  scores  near  current  thresholds  where
robustness and reduce false alarms. Voting schemes  classification uncertainty peaks.  Query-by-committee
aggregate binary drift signals from individual detectors,
approaches investigate cases exhibiting disagreement
| declaring  | drift  | when  | majorities  | agree.  |     | Confidence- |     |     |     |     |     |     |     |
| ---------- | ------ | ----- | ----------- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
among ensemble members. Expected error reduction
weighted aggregation weighs detector votes by their
criteria estimate potential performance improvements
historical  reliability.  Sequential  hypothesis  testing  from  investigating  specific  cases.  The  adaptive
frameworks including Sequential Probability Ratio Test  investigation protocol balances exploitation of current
| (SPRT)  | evaluate  | evidence  |     | accumulation  |     | for  drift  |     |     |     |     |     |     |     |
| ------- | --------- | --------- | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
knowledge through high-confidence fraud cases against
hypotheses, stopping when confidence reaches decision
|              |      |           |           |     |           |          | exploration  |     | of  uncertain  | boundary  | regions.  |     | Budget  |
| ------------ | ---- | --------- | --------- | --- | --------- | -------- | ------------ | --- | -------------- | --------- | --------- | --- | ------- |
| thresholds.  | The  | ensemble  | approach  |     | provides  | earlier  |              |     |                |           |           |     |         |
constraints limit investigation capacity requiring careful
detection through sensitive methods while maintaining  selection of most informative cases. The feedback loop
low false alarm rates through conservative methods.  accelerates threshold convergence to optimal settings
| Meta-learning  |     | algorithms  |     | learn  | optimal  | detector  |          |            |              |     |              |           |     |
| -------------- | --- | ----------- | --- | ------ | -------- | --------- | -------- | ---------- | ------------ | --- | ------------ | --------- | --- |
|                |     |             |     |        |          |           | through  | strategic  | information  |     | acquisition  | reducing  |     |
combinations and aggregation strategies from historical
calibration time and resource requirements.
Vol. 6(4), pp. 27-49, April 2026
[42]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

Context-aware Threshold Adjustment  practices,  which  naturally  have  higher  aggregate
|     |     |     |     |     |     |     | volumes.  | The  stratification  |     | methodology  |     | clusters  |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------------- | --- | ------------ | --- | --------- |
Contextual factors, including temporal periods, provider
|                   |     |                   |     |              |     |            | providers    | based  on       | relevant  | characteristics  |      | and       |
| ----------------- | --- | ----------------- | --- | ------------ | --- | ---------- | ------------ | --------------- | --------- | ---------------- | ---- | --------- |
| characteristics,  |     | and  operational  |     | conditions,  |     | influence  |              |                 |           |                  |      |           |
|                   |     |                   |     |              |     |            | establishes  | group-specific  |           | thresholds       | via  | separate  |
optimal  threshold  settings.  Seasonal  patterns  in  optimization procedures. Hierarchical modeling enables
legitimate  healthcare  utilization  require  threshold  partial pooling of information across strata, stabilizing
adaptation across calendar periods. Winter influenza
threshold estimates for small provider groups.
| seasons  | increase  | claim  | volumes  |     | requiring  | threshold  |     |     |     |     |     |     |
| -------- | --------- | ------ | -------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
relaxation  to  maintain  specificity.  Summer  vacation  Operational context, including investigation capacity
periods  reduce  activity  necessitating  threshold  and  enforcement  priorities,  drives  threshold
tightening. The adjustment framework applies seasonal  adjustments.  During  resource-constrained  periods,
multiplicative  factors  that  scale  baseline  thresholds  thresholds must be tightened to maintain investigation
based  on  expected  claim  volume  patterns.  Holiday  volumes  within  capacity  limits.  Surplus  capacity
periods and weekend days may motivate specialized  enables  threshold  loosening,  increasing  detection
threshold  configurations,  depending  on  observed  breadth. Enforcement initiatives targeting specific fraud
utilization patterns and operational staffing levels. The  types  trigger  threshold  adjustments  emphasizing
temporal  adaptation  maintains  consistent  detection  relevant  detection  signatures.  Emergency  situations,
performance despite predictable cyclical variations.  including  pandemic  responses,  necessitate  rapid
threshold reconfiguration, accommodating dramatically
| Provider stratification enables customized  |     |     |     |     |     | thresholds  |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
altered healthcare delivery patterns. The context-aware
| matching  | specific  | characteristics.  |     |     | Specialty-based  |     |     |     |     |     |     |     |
| --------- | --------- | ----------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
framework implements rule-based logic that encodes
| thresholds  | account  | for  | legitimate  |     | practice  | pattern  |                |            |     |              |     |            |
| ----------- | -------- | ---- | ----------- | --- | --------- | -------- | -------------- | ---------- | --- | ------------ | --- | ---------- |
|             |          |      |             |     |           |          | institutional  | knowledge  | of  | appropriate  |     | threshold  |
differences  across  medical  disciplines.  High-volume  responses for various operational scenarios. Machine
specialties, such as emergency medicine, tolerate higher  learning  components  learn  adaptation  policies  from
absolute claim volumes than low-volume specialties,
historical context-performance relationships, enabling
such as neurosurgery. Geographic adjustments reflect
data-driven threshold adjustments. Table 8 summarizes
| regional  | variation  | in  | practice  | patterns  |     | and  patient  |               |            |             |              |     |      |
| --------- | ---------- | --- | --------- | --------- | --- | ------------- | ------------- | ---------- | ----------- | ------------ | --- | ---- |
|           |            |     |           |           |     |               | the  dynamic  | threshold  | adjustment  | methodology  |     | and  |
demographics. Urban providers exhibit different billing  performance outcomes.
| rhythms      | than  | rural          | practices.  | Practice  |     | size  factors  |     |     |     |     |     |     |
| ------------ | ----- | -------------- | ----------- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
| distinguish  | solo  | practitioners  |             | from      |     | large  group   |     |     |     |     |     |     |
Table 8: Dynamic Threshold Adjustment Methodology Performance
Average  Detection  FPR  Stability  (Std  Drift  Response  Time
Adaptation Strategy
|                         |     |     |           | Rate              |     |     | Dev)   |     | (days)  |     |     |     |
| ----------------------- | --- | --- | --------- | ----------------- | --- | --- | ------ | --- | ------- | --- | --- | --- |
| Fixed Threshold         |     |     |           | 0.73 (degrading)  |     |     | 0.048  |     | N/A     |     |     |     |
| Periodic Recalibration  |     |     |           | 0.81              |     |     | 0.032  |     | 30.0    |     |     |     |
| PID Controller          |     |     |           | 0.84              |     |     | 0.024  |     | 12.5    |     |     |     |
| Bayesian Updating       |     |     |           | 0.85              |     |     | 0.021  |     | 10.2    |     |     |     |
| Proposed                |     |     | Adaptive  |                   |     |     |        |     |         |     |     |     |
|                         |     |     |           | 0.87              |     |     | 0.018  |     | 8.3     |     |     |     |
Framework
Figure 4 visualizes the temporal evolution of detection

thresholds under the adaptive adjustment framework
| over a twelve-month deployment period.  |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Vol. 6(4), pp. 27-49, April 2026
[43]

Journal of Advanced Computing Systems (JACS) ISSN: 3066-3962
Figure 4: Adaptive Threshold Evolution and Performance Tracking
This multi-panel time-series visualization displays the investigation demand exceeds availability, triggering
coordinated evolution of threshold settings and threshold tightening responses. Green shading marks
corresponding performance metrics over 12 months of surplus capacity periods enabling threshold loosening.
operational deployment. The top panel shows the Throughout the deployment period, the adaptive system
adaptive threshold trajectory (blue line) starting at an maintains performance within acceptable ranges despite
initial setting of 0.50 and dynamically adjusting multiple drift events and varying operational conditions.
between 0.35 and 0.65 in response to performance The visualization demonstrates the effectiveness of the
feedback and concept drift signals. Notable adjustment threshold adjustment algorithm in balancing the
episodes include: a sharp decrease to 0.38 during competing objectives of detection sensitivity, false-
months 2-3, responding to elevated false negative rates, positive control, and operational feasibility. Annotation
a gradual increase from 0.40 to 0.58 during months 5-7, boxes highlight key decision points, including Month 3
reducing excessive false positive volumes, and a rapid threshold decrease, improving detection rate from 0.78
decrease to 0.42 in month 9 following detection of new to 0.85, Month 6 threshold increase, reducing false
fraud pattern emergence. Gray-shaded regions indicate positive rate from 0.15 to 0.08 while maintaining
concept drift episodes detected by the monitoring detection rate above 0.80, and Month 9 rapid response
system, with drift intensity proportional to the shading to emerging fraud pattern, preventing performance
darkness. The middle panel tracks four key performance degradation.
metrics: detection rate (green line, range 0.75-0.92),
false positive rate (red line, range 0.05-0.18), precision 5. Experimental Evaluation and Discussion
(purple line, range 0.42-0.68), and F1 score (orange line,
range 0.51-0.74). Horizontal dashed reference lines
5.1. Experimental Setup and Dataset Description
mark target performance levels, including minimum
acceptable detection rate at 0.80 and maximum tolerable The experimental evaluation used de-identified
false positive rate at 0.10. The bottom panel displays Medicare Part B claims data spanning a three-year
daily investigation volume (blue bars, range 50-180 period from 2020 through 2022. The dataset comprises
cases) compared against available investigative capacity 47.3 million claims submitted by 892,450 healthcare
(red horizontal line at 120 cases per day). Yellow providers across all fifty states and the District of
shading indicates periods of capacity constraint when Columbia. Ground truth fraud labels were established
Vol. 6(4), pp. 27-49, April 2026
[44]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

by integrating confirmed investigation outcomes from  RAM, enabling parallel processing of large-scale claims
the Centers for Medicare & Medicaid Services Office of  datasets.  The  parallelization  strategy  processes
Inspector General Exclusions Database and Department  providers  independently  across  48  worker  threads,
of  Justice  settlements  published  through  December  achieving an aggregate throughput of approximately
2022.  The  labeled  subset  contains  3,845  confirmed  15,000 provider evaluations per hour, with an average
fraudulent providers representing 0.43% of the total  per-provider  processing  latency  of  2.4  seconds,
provider  population,  reflecting  realistic  fraud  including feature extraction, scoring, and result logging.
| prevalence  | in        | operational  |     | settings.  |     | Claims   | records  |     |     |     |     |     |     |     |
| ----------- | --------- | ------------ | --- | ---------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| include     | temporal  | attributes   |     | such       | as  | service  | dates,   |     |     |     |     |     |     |     |
5.2. Performance Comparison of Feature
| submission  | dates,  |     | and  processing  |     | dates,  | along  | with  |     |     |     |     |     |     |     |
| ----------- | ------- | --- | ---------------- | --- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Engineering Approaches
provider identifiers, beneficiary identifiers, procedure
| codes  represented  |     |        | using   | the      | Current  | Procedural  |        |              |             |           |     |           |          |     |
| ------------------- | --- | ------ | ------- | -------- | -------- | ----------- | ------ | ------------ | ----------- | --------- | --- | --------- | -------- | --- |
|                     |     |        |         |          |          |             |        | Comparative  | evaluation  | assessed  |     | multiple  | feature  |     |
| Terminology         |     | (CPT)  | coding  | system,  |          | diagnosis   | codes  |              |             |           |     |           |          |     |
engineering strategies, including baseline approaches
using the International Classification of Diseases, Tenth
|     |     |     |     |     |     |     |     | and  the  | proposed  | temporal  | framework.  |     | Baseline  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --------- | ----------- | --- | --------- | --- |
Revision (ICD-10) format, and reimbursement amounts
in US dollars.  methods used simple statistical features, such as total
|     |     |     |     |     |     |     |     | claim  counts,  | average  | claim  | amounts,  |     | and  billing  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | ------ | --------- | --- | ------------- | --- |
Data  preprocessing  involved  constructing  temporal  frequency,  without  sophisticated  temporal  analysis.
sequences and organizing claims chronologically by  Traditional  RFM  features,  adapted  from  marketing
provider  and  beneficiary.  Claims  occurring  within  analytics computed recency, frequency, and monetary
ninety-day  windows  were  aggregated  into  episodes  metrics.  The  proposed  temporal  feature  engineering
representing  coherent  treatment  sequences.  Ground  framework,  incorporating  claim  timestamp  analysis,
truth  label  construction  followed  strict  temporal  service  interval  patterns,  and  frequency  distribution
alignment rules: provider fraud labels were assigned  characterization, demonstrated substantial performance
based on investigation completion dates, with all claims  improvements. Detection rates improved from 0.73 for
submitted before the investigation initiation date labeled  baseline  features to 0.87 for the  complete  temporal
according to provider status, while excluding claims  feature set. False positive rates decreased from 0.14 to
during investigation periods to prevent label leakage.  0.06, maintaining operational feasibility. The area under
Feature  engineering  pipelines  extracted  127  distinct  the ROC curve increased from 0.84 to 0.93, indicating
temporal  features,  including  the  methodologies  significantly  improved  discrimination  between
described  in  Section  3.  Statistical  features  captured  fraudulent and legitimate providers.
| distributional  |     | characteristics  |     | of  | claim  | frequencies,  |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------------- | --- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
service intervals, and submission patterns. Functional  Ablation  studies  isolated  contributions  of  individual
principal component analysis generated 15 trajectory  feature  categories.  Removing  the  claim  timestamp
features decreased the detection rate from 0.79 to 0.78,
| features  | representing  |     | dominant  |     | temporal  |     | variation  |     |     |     |     |     |     |     |
| --------- | ------------- | --- | --------- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
demonstrating their critical importance. Service interval
modes. LSTM autoencoder embeddings yielded 128
|     |     |     |     |     |     |     |     | features  contributed  |     | a  0.05-point  |     | improvement  |     | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | -------------- | --- | ------------ | --- | --- |
learned features, which were subsequently reduced to 32
principal  features,  preserving  95%  of  the  variance.  detection  rate.  Frequency  distribution  characteristics
Feature selection procedures using mutual information- added 0.04 detection rate gains. LSTM autoencoder
embeddings provided 0.06 improvement over statistical
based ranking reduced the total dimensionality to 45
features alone, justifying their computational overhead
| features,      | balancing  |             | detection  |     | performance  |                   | with  |                       |     |              |     |         |             |     |
| -------------- | ---------- | ----------- | ---------- | --- | ------------ | ----------------- | ----- | --------------------- | --- | ------------ | --- | ------- | ----------- | --- |
|                |            |             |            |     |              |                   |       | through  substantial  |     | performance  |     | gains.  | Functional  |     |
| computational  |            | efficiency  |            |     | and          | interpretability  |       |                       |     |              |     |         |             |     |
requirements.  principal  component  features  contributed  a  0.03
increase in detection rate. The synergistic combination
Evaluation methodology employed stratified five-fold  of multiple feature types achieved superior performance
cross-validation,  preserving  fraud  prevalence  ratios  compared to any individual category, validating the
across  folds.  Each  fold  contained  approximately  comprehensive temporal feature engineering framework
178,490  providers  with  769  confirmed  fraud  cases.  design philosophy.
Training folds were used for feature extraction, model
|     |     |     |     |     |     |     |     | Feature  importance  |     | analysis  | using  | random  |     | forest  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --------- | ------ | ------- | --- | ------- |
calibration, and threshold optimization. Held-out test
folds were used to evaluate detection performance and  importance scores identified the most discriminative
generalization. Performance metrics included detection  temporal features. Service-to-submission lag standard
deviation ranked highest with an importance score of
rate (sensitivity), false positive rate, precision (positive
|     |     |     |     |     |     |     |     | 0.089,  capturing  |     | providers  | with  inconsistent  |     | billing  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ---------- | ------------------- | --- | -------- | --- |
predictive value), F1 score, and area under the ROC
timing. The weekend submission ratio ranked second at
| curve.  Statistical  |     | significance  |     |     | testing  | employed  | the  |     |     |     |     |     |     |     |
| -------------------- | --- | ------------- | --- | --- | -------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
DeLong test for AUC comparisons and the McNemar  0.077,  indicating  unusual  operational  patterns.  The
test  for  paired  classification  results.  Computational  claim frequency coefficient of variation achieved an
importance of 0.071, detecting providers with erratic
| experiments  | utilized  |     | a  high-performance  |     |     | computing  |     |     |     |     |     |     |     |     |
| ------------ | --------- | --- | -------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
billing volumes. Autocorrelation at a 7-day lag was
cluster with 96-core Intel Xeon processors and 512GB
Vol. 6(4), pp. 27-49, April 2026
[45]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

0.068,  revealing  an  artificial  weekly  periodicity  in  average of 2.4 seconds for complete feature extraction
fraudulent  billing.  The  FPCA’s  first  principal  and scoring pipeline. The 2.4-second feature extraction
component achieved an importance of 0.064, capturing  latency per provider enables daily batch processing of
dominant  trajectory  patterns.  These  findings  inform  the entire provider population within operational time
feature prioritization for real-time deployment scenarios  windows. Threshold optimization procedures execute in
requiring  computational  efficiency  through  selective  under  five  minutes,  enabling  frequent  recalibration.
feature calculation.  Investigation prioritization ranks flagged providers by
anomaly scores facilitating efficient resource allocation.
|     |     |     |     |     |     |     |     | Explanation  |     | facilities  |     | generate  |     | interpretable  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | --- | --------- | --- | -------------- |
5.3. Threshold Strategy Evaluation and Practical
|     |     |     |     |     |     |     |     | descriptions  |     | of  temporal  |     | anomalies  |     | supporting  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | --- | ---------- | --- | ----------- |
Implications
investigator decision-making. The framework integrates
|                 |              |               |             |              |        |               |     | with  existing    |             | case        | management  |         | systems         | via          |
| --------------- | ------------ | ------------- | ----------- | ------------ | ------ | ------------- | --- | ----------------- | ----------- | ----------- | ----------- | ------- | --------------- | ------------ |
| The  threshold  |              | optimization  |             | methodology  |        | evaluated     |     |                   |             |             |             |         |                 |              |
|                 |              |               |             |              |        |               |     | Representational  |             | State       | Transfer    | (REST)  |                 | Application  |
| multiple        | approaches,  |               | including   |              | fixed  | percentile    |     |                   |             |             |             |         |                 |              |
|                 |              |               |             |              |        |               |     | Programming       |             | Interfaces  | (APIs),     |         | enabling        | seamless     |
| thresholds,     | statistical  |               | thresholds  | based        |        | on  standard  |     |                   |             |             |             |         |                 |              |
|                 |              |               |             |              |        |               |     | operational       | deployment  |             | without     | major   | infrastructure  |              |
deviations,  cost-sensitive  optimization,  and  the  modifications.
proposed adaptive adjustment framework. Fixed 95th
percentile thresholds achieved a detection rate of 0.81  Cost-benefit analysis quantifies the financial impact of
and a false-positive rate of 0.09. Statistical three-sigma  the  proposed  methodology.  Based  on  the  estimated
thresholds yielded a detection rate of 0.78 and a false- average fraud loss of $125,000 per provider, established
positive  rate  of  0.11.  Cost-sensitive  optimization  through  analysis  of  historical  investigation  recovery
incorporating  asymmetric  misclassification  costs  data, and the investigation cost of $8,500 per case,
improved the detection rate to 0.84 while maintaining a  derived from CMS Office of Inspector General cost
false positive rate of 0.08. The adaptive adjustment  accounting reports, the optimized approach generates
framework achieved an optimal balance with a detection  net  annual  savings  of  $156  million  for  Medicare
rate  of  0.87  and  a  false  positive  rate  of  0.06,  program operations. Improvements in detection rates
outperforming  static  approaches  through  continuous  prevent  an  additional  $47  million  in  fraud  losses
calibration based on operational feedback. The cost- annually  compared  to  baseline  approaches.  False
benefit analysis identified threshold 0.60 as maximizing  positive reductions save $23 million in unnecessary
net benefit at 8.2 million dollars annually, consistent  investigation  costs.  The  rapid  deployment  timeline
with  the  Figure  3  visualization,  which  shows  this  enables cost recovery within 4.2 months. Sensitivity
threshold achieving a detection rate of 0.79 and a false  analyses confirm robust positive returns across plausible
positive rate of 0.03, as documented in Table 7.  ranges of cost assumptions, including fraud amounts
between $100,000 and $150,000 and investigation costs
| Temporal  | stability  |     | analysis  | evaluated  |     | threshold  |     |          |         |      |           |     |        |              |
| --------- | ---------- | --- | --------- | ---------- | --- | ---------- | --- | -------- | ------- | ---- | --------- | --- | ------ | ------------ |
|           |            |     |           |            |     |            |     | between  | $7,000  | and  | $10,000.  |     | These  | substantial  |
performance over extended deployment periods. Fixed
financial benefits justify the investment in sophisticated
thresholds exhibited gradual performance degradation
|     |     |     |     |     |     |     |     | temporal  | analytics  |     | infrastructure  | and  | the  | associated  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | --------------- | ---- | ---- | ----------- |
as fraud patterns evolved, and concept drift occurred.  ongoing maintenance costs. The methodology provides
Detection rates declined by 0.12 over 12 months for  scalable  fraud  detection  capabilities  supporting
static thresholds, while false-positive rates increased by
|             |           |     |            |     |             |     |         | Medicare  | program  |     | integrity  |     | objectives  | while  |
| ----------- | --------- | --- | ---------- | --- | ----------- | --- | ------- | --------- | -------- | --- | ---------- | --- | ----------- | ------ |
| 0.05.  The  | adaptive  |     | framework  |     | maintained  |     | stable  |           |          |     |            |     |             |        |
maintaining operational efficiency suitable for resource-
| performance  |     | through  |     | continuous  |     | recalibration  |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | --- | ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
constrained environments.
responding to drift signals. Detection rates fluctuated
within a 0.03 range around a mean of 0.87, while false
6. Conclusion, Limitations, and Future Work
| positives  | remained  |            | within        | 0.02  of  | the         | target  | 0.06.  |     |     |     |     |     |     |     |
| ---------- | --------- | ---------- | ------------- | --------- | ----------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Concept    | drift     | detection  | successfully  |           | identified  |         | four   |     |     |     |     |     |     |     |
major distribution shifts during the evaluation period,  6.1. Research Contributions and Key Findings
triggering appropriate threshold adjustments. Average
This research developed a comprehensive framework
| adjustment  | latency  |     | measured  | 8.3  | days  | from  | drift  |                |     |          |              |     |      |            |
| ----------- | -------- | --- | --------- | ---- | ----- | ----- | ------ | -------------- | --- | -------- | ------------ | --- | ---- | ---------- |
|             |          |     |           |      |       |       |        | for  temporal  |     | feature  | engineering  |     | and  | threshold  |
occurrence to corrective threshold modification.
optimization to address critical challenges in healthcare
claims anomaly detection. The systematic extraction of
| Practical  | deployment  |     |     | considerations  |     |     | include  |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
temporal features from claims sequences enables the
| computational  |     | efficiency,  |     | interpretability,  |     |     | and  |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | ------------------ | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
integration with existing investigation workflows. The  identification  of  subtle  fraud  patterns  that  manifest
temporal  feature  engineering  framework  processes  through  abnormal  timing  characteristics,  irregular
service intervals, and unusual billing frequencies. The
| approximately  |     | 15,000  | provider  | updates  |     | per  hour on  |     |     |     |     |     |     |     |     |
| -------------- | --- | ------- | --------- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
proposed feature engineering methodology combines
| standard  | server  |     | hardware  | meeting  |     | real-time  |     |              |            |     |             |            |     |            |
| --------- | ------- | --- | --------- | -------- | --- | ---------- | --- | ------------ | ---------- | --- | ----------- | ---------- | --- | ---------- |
|           |         |     |           |          |     |            |     | statistical  | analysis,  |     | functional  | principal  |     | component  |
requirements, achieved through parallel processing of
48 concurrent provider evaluations each requiring an  analysis, and deep learning representations to capture
|     |     |     |     |     |     |     |     | multi-scale  | temporal  |     | dependencies.  |     | Experimental  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | -------------- | --- | ------------- | --- |
Vol. 6(4), pp. 27-49, April 2026
[46]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

results show a consistent improvement over baseline  imbalance, with a fraud prevalence of 0.43%, poses
approaches, with higher detection rates and lower false- challenges  for  model  calibration  and  performance
positive rates in our evaluation.  estimation. Small numbers of fraud cases in individual
provider specialty categories limit the ability to develop
The  adaptive  threshold  optimization  methodology  specialty-specific detection models. The experimental
addresses  operational  constraints  through  dynamic  evaluation captures performance at specific timepoints
| adjustment  | algorithms  |     |     | that  maintain  | detection  |              |     |        |               |     |            |          |      |
| ----------- | ----------- | --- | --- | --------------- | ---------- | ------------ | --- | ------ | ------------- | --- | ---------- | -------- | ---- |
|             |             |     |     |                 |            | but  cannot  |     | fully  | characterize  |     | detection  | latency  | for  |
effectiveness while controlling investigation volumes.
identifying fraud at the earliest possible stages.
The framework balances competing objectives of fraud
prevention  and  resource  efficiency  through  cost- Computational requirements for deep learning feature
sensitive  optimization  and  multi-objective  decision  construction,  including  LSTM  autoencoder  training,
analysis. Evaluation on Medicare claims data suggests  impose infrastructure costs that may limit accessibility
the approach can improve cost-benefit trade-offs under  for  smaller  healthcare  organizations.  The  feature
assumed  investigation  and  loss-cost  settings.  The  engineering  pipeline  requires  domain  expertise  to
threshold adaptation mechanisms successfully respond  configure appropriate temporal windows, aggregation
to concept drift and changing fraud tactics, maintaining  periods,  and  reference  distributions.  Threshold
stable performance over extended deployment periods  optimization assumes stable cost parameters for fraud
where static thresholds exhibit significant degradation.  losses and investigation expenses, while actual costs
exhibit uncertainty and temporal variation. The adaptive
Key findings from the research include the importance
|     |     |     |     |     |     | threshold  | framework  |     | requires  |     | ongoing  | performance- |     |
| --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | --------- | --- | -------- | ------------ | --- |
of service-to-submission lag features, while submission-
|     |     |     |     |     |     | monitoring  | infrastructure  |     |     | and  | investigative  |     | feedback  |
| --- | --- | --- | --- | --- | --- | ----------- | --------------- | --- | --- | ---- | -------------- | --- | --------- |
time patterns (e.g., weekends) can be context-dependent
mechanisms that may not be available in all operational
signals that require interpretation aligned with claims  contexts. Interpretability of complex temporal features
processing  workflows.  The  study  explores  LSTM  and deep learning representations remains challenging
| autoencoder  | representations  |     |         | for  capturing  | complex      |          |            |     |             |     |      |                |     |
| ------------ | ---------------- | --- | ------- | --------------- | ------------ | -------- | ---------- | --- | ----------- | --- | ---- | -------------- | --- |
|              |                  |     |         |                 |              | despite  | attention  |     | mechanisms  |     | and  | visualization  |     |
| temporal     | dependencies     |     | beyond  | traditional     | statistical  |          |            |     |             |     |      |                |     |
approaches.
features and demonstrates promising performance in our
evaluation.  The  research  indicates  that  threshold  6.3. Directions for Future Research
| selection  | should  |     | explicitly  | consider  | operational  |         |           |         |     |         |                |     |          |
| ---------- | ------- | --- | ----------- | --------- | ------------ | ------- | --------- | ------- | --- | ------- | -------------- | --- | -------- |
|            |         |     |             |           |              | Future  | research  | should  |     | extend  | the  temporal  |     | feature  |
constraints and asymmetric costs, rather than relying
solely on label-dependent metrics such as classification  engineering  framework  to  alternative  healthcare
accuracy. The adaptive framework's ability to maintain  payment  models,  including  bundled  payments,
|     |     |     |     |     |     | accountable  |     | care  | organizations,  |     | and  | value-based  |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | --------------- | --- | ---- | ------------ | --- |
consistent performance despite concept drift highlights
|     |     |     |     |     |     | reimbursement  |     | structures.  |     | Fraud  | patterns  |     | in  these  |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ------ | --------- | --- | ---------- |
the value of continuous monitoring and recalibration in
contexts differ from traditional fee-for-service billing,
production fraud detection systems.
requiring adaptation of temporal features to capture
6.2. Research Limitations  relevant  anomalies.  Cross-domain  transfer  learning
approaches could leverage fraud detection knowledge
Several limitations constrain the generalizability and  from  Medicare  data  to  improve  performance  on
applicability of the research findings. The evaluation  Medicaid  or  private  insurance  claims  with  limited
relies exclusively on Medicare Part B claims data, which
labeled fraud cases. Federated learning architectures
| represent  | fee-for-service  |     |     | reimbursement  | structures.  |         |                |     |     |        |              |     |         |
| ---------- | ---------------- | --- | --- | -------------- | ------------ | ------- | -------------- | --- | --- | ------ | ------------ | --- | ------- |
|            |                  |     |     |                |              | enable  | collaborative  |     |     | model  | development  |     | across  |
Performance characteristics may differ substantially in
|     |     |     |     |     |     | multiple  | payer  | organizations  |     |     | while  | preserving  | data  |
| --- | --- | --- | --- | --- | --- | --------- | ------ | -------------- | --- | --- | ------ | ----------- | ----- |
managed  care  environments,  Medicaid  programs,  or  privacy and confidentiality.
| private  | insurance  | contexts  |     | with  alternative  | payment  |     |     |     |     |     |     |     |     |
| -------- | ---------- | --------- | --- | ------------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
models and beneficiary populations. The fraud label  Advanced  deep  learning  architectures,  including
construction  depends  on  completed  investigations,  Transformer  models  and  attention-based  temporal
introducing  a  temporal  lag  between  the  onset  of  convolution  networks,  warrant  investigation  for
fraudulent  activity  and  label  availability.  This  lag  temporal  feature  learning.  These  architectures
complicates  the  evaluation  of  early  warning system  demonstrate strong performance on sequential modeling
effectiveness,  as  the  methodology  cannot  assess  tasks  and  may  capture  longer-range  temporal
detection  performance  for  fraud  schemes  identified  dependencies  than  LSTM  networks.  Graph  neural
before investigation completion.  networks  that  incorporate  provider-beneficiary-
|                    |          |        |              |                  |                | procedure  | relationships  |     |        | offer  promising  |     | avenues         | for  |
| ------------------ | -------- | ------ | ------------ | ---------------- | -------------- | ---------- | -------------- | --- | ------ | ----------------- | --- | --------------- | ---- |
| The  ground-truth  |          | fraud  |              | labels  reflect  | investigation  |            |                |     |        |                   |     |                 |      |
|                    |          |        |              |                  |                | detecting  | collusive      |     | fraud  | networks.         |     | Explainability  |      |
| selection          | biases,  | as     | enforcement  | agencies         | prioritize     |            |                |     |        |                   |     |                 |      |
research should develop interpretable temporal feature
high-value cases and providers with prior compliance  representations  enabling  investigators  to  understand
issues. The labeled fraud sample may not represent the  detection rationales and validate algorithmic decisions.
full spectrum of fraudulent behaviors, particularly novel
Causal inference methods could distinguish correlation
| schemes  | not  | yet  recognized  |     | by  investigators.  | Class  |     |     |     |     |     |     |     |     |
| -------- | ---- | ---------------- | --- | ------------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Vol. 6(4), pp. 27-49, April 2026
[47]

Journal of Advanced Computing Systems (JACS)    ISSN: 3066-3962

from causation in temporal fraud patterns, supporting  28(7),  1610-1628.
more robust detection.  https://doi.org/10.1109/TKDE.2016.2535209
Threshold  optimization  methodology  should  [4]. Malhotra, P., Vig, L., Shroff, G., & Agarwal, P.
incorporate  reinforcement  learning  approaches  that  (2015).  Long  short  term  memory  networks  for
learn optimal threshold policies through interaction with  anomaly detection in time series. In Proceedings of
operational environments. Online learning algorithms  the 23rd European Symposium on Artificial Neural
that enable continuous adaptation without explicit drift- Networks, Computational Intelligence and Machine
detection mechanisms could improve responsiveness to  Learning (ESANN 2015), pp. 89-94.
emerging fraud tactics. Multi-armed bandit frameworks
|             |          |               |     |     |              |     |            | [5]. Ahmad,  | A.  M.,  | Eckert,  |                | C.,  Teredesai,  |     | A.,  &   |
| ----------- | -------- | ------------- | --- | --- | ------------ | --- | ---------- | ------------ | -------- | -------- | -------------- | ---------------- | --- | -------- |
| could       | balance  | exploration   |     | of  | alternative  |     | threshold  |              |          |          |                |                  |     |          |
|             |          |               |     |     |              |     |            | McKelvey,    | G.       | (2018).  | Interpretable  |                  |     | machine  |
| strategies  | with     | exploitation  |     |     | of  known    |     | effective  |              |          |          |                |                  |     |          |
approaches.  Research  on  fairness  and  bias  in  fraud  learning in healthcare. IEEE Intelligent Informatics
detection  algorithms  should  ensure  threshold  Bulletin, 19(1), 1-7.
| optimization  |     | does  | not  | disproportionately  |     |     | impact  |     |     |     |     |     |     |     |
| ------------- | --- | ----- | ---- | ------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
[6]. Chen, J., Sathe, S., Aggarwal, C., & Turaga, D.
providers serving vulnerable populations or practicing
(2020). Embedding for anomaly detection on health
in underserved areas. Adversarial robustness analysis
|     |     |     |     |     |     |     |     | insurance  | claims.  | In  | 2020  | IEEE  | International  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ----- | ----- | -------------- | --- |
should evaluate the detection system’s vulnerability to
Conference on Data Mining (ICDM), pp. 1003-
strategic manipulation by sophisticated fraudsters who
1008.
are aware of its detection mechanisms.
https://doi.org/10.1109/ICDM50108.2020.00116
| Longitudinal  |     | studies  | tracking  | the  | impact  | of  | a  fraud  |     |     |     |     |     |     |     |
| ------------- | --- | -------- | --------- | ---- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[7]. Zhang, C., Song, D., Chen, Y., Feng, X., Lumezanu,
detection system on provider behavior could quantify
|             |          |     |               |     |          |     |            | C.,  Cheng,  | W.,  | Ni,  | J.,  Zong,  | B.,  | Chen,  | H.,  &  |
| ----------- | -------- | --- | ------------- | --- | -------- | --- | ---------- | ------------ | ---- | ---- | ----------- | ---- | ------ | ------- |
| deterrence  | effects  |     | and  measure  |     | changes  |     | in  fraud  |              |      |      |             |      |        |         |
Chawla, N. V. (2019). A deep neural network for
| prevalence  | following  |     | deployment.  |     |     | Integration  | of  |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------------ | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
unsupervised anomaly detection and diagnosis in
| external  | data  | sources,  | including  |     | physician  |     | licensing  |     |     |     |     |     |     |     |
| --------- | ----- | --------- | ---------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
multivariate time series data. In Proceedings of the
information, prior enforcement actions, and network
33rd AAAI Conference on Artificial Intelligence,
| analysis       | data,  | may     | enhance   |     | detection  |     | through    |         |     |     |     |     |             |     |
| -------------- | ------ | ------- | --------- | --- | ---------- | --- | ---------- | ------- | --- | --- | --- | --- | ----------- | --- |
|                |        |         |           |     |            |     |            | 33(1),  |     |     |     |     | 1409-1416.  |     |
| complementary  |        | signal  | sources.  |     | Real-time  |     | streaming  |         |     |     |     |     |             |     |
https://doi.org/10.1609/aaai.v33i01.33011409
architectures that enable immediate claims evaluation at
submission time, rather than batch processing, could
[8]. Bauder, R. A., & Khoshgoftaar, T. M. (2023). Cost-
| reduce  | fraud  | losses  | by  enabling  |     | faster  | intervention.  |     |            |           |      |          |     |            |        |
| ------- | ------ | ------- | ------------- | --- | ------- | -------------- | --- | ---------- | --------- | ---- | -------- | --- | ---------- | ------ |
|         |        |         |               |     |         |                |     | sensitive  | learning  | for  | medical  |     | insurance  | fraud  |
Research on optimal investigation resource allocation  detection  with  temporal  information.  IEEE
should  develop  decision-support  tools  that  help  Transactions on Knowledge and Data Engineering,
investigators  prioritize  cases,  maximizing  expected  35(10),  10375-10389.
| recovery  | while  | accounting  |     | for  | capacity  | constraints.  |     |     |     |     |     |     |     |     |
| --------- | ------ | ----------- | --- | ---- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1109/TKDE.2023.3240431
| These  | research  | directions  |     | would  |     | advance  | both  |     |     |     |     |     |     |     |
| ------ | --------- | ----------- | --- | ------ | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
[9]. Xu, H., Feng, Y., Chen, J., Wang, Z., Qiao, H.,
theoretical understanding and practical effectiveness of
temporal  anomaly  detection  in  healthcare  fraud  Chen, W., Zhao, N., Li, Z., Bu, J., Li, Z., & Liu, Y.
| prevention.  |     |     |     |     |     |     |     | (2018).  | Unsupervised  |     | anomaly  |     | detection  | via  |
| ------------ | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | -------- | --- | ---------- | ---- |
variational auto-encoder for seasonal KPIs in web
|     |     |     |     |     |     |     |     | applications.  | In  | Proceedings  |     | of the  | 2018  | World  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ------- | ----- | ------ |
References
Wide Web Conference (WWW '18), pp. 187-196.
https://doi.org/10.1145/3178876.3185996
[1]. Centers for Medicare & Medicaid Services. (2023).
National Health Expenditure Data: Historical. U.S.  [10].  Alharbi,  A.,  Alshammari,  M.,  Okon,  O.  D.,
| Department  |     | of    | Health                        | and  | Human  |     | Services.  |            |             |                 |     |          |              |      |
| ----------- | --- | ----- | ----------------------------- | ---- | ------ | --- | ---------- | ---------- | ----------- | --------------- | --- | -------- | ------------ | ---- |
|             |     |       |                               |      |        |     |            | Alshdadi,  | A.  A.,     | Samha,          |     | A.  K.,  | &  Issaoui,  | Y.   |
| Retrieved   |     | from  | https://www.cms.gov/Research- |      |        |     |            |            |             |                 |     |          |              |      |
|             |     |       |                               |      |        |     |            | (2023).    | A  machine  | learning-based  |     |          | approach     | for  |
Statistics-Data-and-Systems/Statistics-Trends-and- medical insurance anomaly detection by predicting
Reports/NationalHealthExpendData  indirect  outpatients'  claim  price.  In  2023  IEEE
International Conference on Industrial Engineering
[2]. Federal Bureau of Investigation. (2022). Financial
and Engineering Management (IEEM), pp. 1425-
Crimes Report: Healthcare Fraud. U.S. Department
1429.
| of  |     | Justice.  |     | Retrieved  |     |     | from  |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | ---------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1109/IEEM58616.2023.1040689
https://www.fbi.gov/stats-
1
services/publications/financial-crimes-report
[11].  Karadayi, Y., Aydin, M. N., & Öğrencı, A. S.
[3]. Ahmed, M., Hu, J., & Luo, X. (2016). Anomaly
|            |     |                |     |        |     |          |       | (2020).       | Unsupervised     |     | anomaly  |       | detection  | in    |
| ---------- | --- | -------------- | --- | ------ | --- | -------- | ----- | ------------- | ---------------- | --- | -------- | ----- | ---------- | ----- |
| detection  |     | for  temporal  |     | data:  | A   | survey.  | IEEE  |               |                  |     |          |       |            |       |
|            |     |                |     |        |     |          |       | multivariate  | spatio-temporal  |     |          | data  | using      | deep  |
Transactions on Knowledge and Data Engineering,
learning: Early detection of COVID-19 outbreak in
Vol. 6(4), pp. 27-49, April 2026
[48]

Journal of Advanced Computing Systems (JACS) ISSN: 3066-3962
Italy. IEEE Access, 8, 164155-164177.
https://doi.org/10.1109/ACCESS.2020.3022366
[12]. Choi, K., Yi, J., Park, C., & Yoon, S. (2021).
Deep learning for anomaly detection in time-series
data: Review, analysis, and guidelines. IEEE
Access, 9, 120043-120065.
https://doi.org/10.1109/ACCESS.2021.3090905
[13]. Zhang, Y., Chen, Y., Wang, J., & Pan, Z.
(2022). Threshold-free anomaly detection for
streaming time series through deep learning. In
2022 IEEE International Conference on Data
Mining (ICDM), pp. 758-767.
https://doi.org/10.1109/ICDM54844.2022.00088
[14]. Schmidl, S., Wenig, P., & Papenbrock, T.
(2022). Anomaly detection in time series: A
comprehensive evaluation. Proceedings of the
VLDB Endowment, 15(9), 1779-1797.
https://doi.org/10.14778/3538598.3538602
[15]. Rahman, M. M., Watanobe, Y., & Nakamura,
K. (2024). Detecting anomalies in medical claims
with clustering algorithm. In 2024 IEEE
International Conference on Big Data (Big Data),
pp. 2156-2163.
https://doi.org/10.1109/BigData62323.2024.10825
476
Vol. 6(4), pp. 27-49, April 2026
[49]