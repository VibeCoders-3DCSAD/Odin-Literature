---
conversion_metadata:
  converted_at: "2026-07-21T07:43:52Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Nagaraj.pdf"
  source_pdf_sha256: "ee38a159fa658d40eaa870dceebbeba486d634287d515ea9cb93005ba1f65e1e"
  page_count: 8
  markdown_char_count: 96390
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of Emerging Research in Engineering and Technology 
Pearl Blue Research Group| Volume 6 Issue 2 PP 81-88, 2025 
ISSN: 3050-922X | https://doi.org/10.63282/3050-922X.IJERET-V6I2P110

Original Article

A Study on Credit Default Prediction Using Hybrid AI Models 
Combining Neural Architectures and Econometric Features

Santhosh Kumar Sagar Nagaraj 
Staff Software Engineer, Visa Inc., Banking & Finance, 1745 stringer pass, Leander, Texas 78641, USA.

Received On: 25/03/2025            Revised On: 20/04/2025            Accepted On: 04/05/2025              Published On: 23/05/2025

Abstract - Credit default prediction plays a vital role in risk 
management,  lending  strategies,  and  financial  stability. 
While  traditional  econometric  models  offer  interpretability, 
they often lack the predictive power of contemporary neural 
networks. This study proposes a novel hybrid approach that 
integrates deep neural network (DNN) architectures with key 
econometric  indicators  to  improve  the  prediction  of  credit 
default  risk.  We  develop  and  evaluate  several  model 
configurations, including a hybrid Long Short-Term Memory 
(LSTM)  and  logistic  regression  framework,  on  publicly 
available  credit  datasets.  The  results  show  that  hybrid 
models outperform standalone econometric or deep learning 
models in terms of accuracy, AUC-ROC, and F1-score. The 
study  also  explores  feature  importance  to  enhance  model 
explainability.  Our  findings  underscore  the  potential  of 
combining  statistical  and  AI  methodologies 
for  more 
accurate and interpretable financial risk assessments.

Keywords  -  Credit  Default  Prediction,  Hybrid  AI  Models, 
Econometric  Features,  Deep  Learning,  Neural  Networks, 
Logistic Regression, LSTM, Financial Risk Modeling, AUC-
ROC, Interpretable AI.

1. Introduction

Credit  default  prediction  is  a  central  problem  in  the 
domain of financial risk management, influencing everything 
from  loan  approvals  to  regulatory  oversight.  The  ability  of 
financial institutions to accurately forecast the likelihood that 
a  borrower  will  default  on  their  loan  obligations  directly 
impacts profitability, portfolio health, and systemic financial 
stability. Traditionally, credit risk models have relied heavily 
on  econometric  techniquessuch  as  logistic  regression  or 
discriminant  analysisthat  use  structured 
financial  and 
demographic  variables.  These  models  are  known  for  their 
interpretability  and  compliance  with  regulatory  frameworks 
like Basel II/III. However, they often  fall short in capturing 
complex,  nonlinear  relationships 
in  borrower 
behavior,  particularly  as  financial  data  becomes  more 
dynamic and multidimensional.

inherent

In  recent  years,  the  rise  of  machine  learning  (ML)  and 
artificial  intelligence  (AI)  has  opened  new  avenues  for 
enhancing 
assessment.  Neural  network 
architectures,  particularly  deep  learning  models  like  Long 
Short-Term  Memory  (LSTM)  networks,  have  demonstrated 
superior  performance  in  a  variety  of  predictive  tasks,

credit

risk

including  fraud  detection,  stock  forecasting,  and  customer 
segmentation.  These  models  are  capable  of  modeling 
temporal dependencies, capturing latent representations, and 
uncovering  subtle  patterns  that  econometric  models  may 
miss.  However,  this  increased  predictive  power  comes  at  a 
cost:  deep  learning  models  are  often  criticized  for  their 
“black-box”  nature,  making  them  difficult  to  interpret  or 
justify in high-stakes financial decisions.

integrate

traditional

delinquencywith

The  limitations  of  using  either  econometric  or  deep 
learning  models  in  isolation,  this  study  proposes  a  hybrid 
approach  that  combines  the  strengths  of  both  paradigms. 
Specifically,  we 
econometric 
featuressuch  as  debt-to-income  ratio,  credit  utilization,  and 
historical 
temporal  modeling 
capabilities  of  neural  networks.  The  proposed  model  fuses 
the outputs of an LSTM network, which processes sequential 
the 
behavioral  data 
predictions of a logistic regression model based on structured 
financial indicators. This hybridization is designed to achieve 
a  balance  between  predictive  accuracy  and  model 
interpretability,  which  is  critical  for  real-world  applications 
in banking and finance.

transaction  history),  with

(e.g.,

the

The  rationale  behind  the  hybrid  model  is  not  merely 
empirical  but  also  conceptual.  While  econometric  models 
offer  clarity  and  justification  for  decisionsmaking  them 
suitable  for  regulated  environmentsneural  models  can 
identify latent patterns and interactions that are often beyond 
human  intuition.  For  instance,  an  LSTM  model  can  detect 
emerging  default  patterns  based  on  time-series  data  such  as 
monthly  repayments,  spending  fluctuations,  or ATM  usage, 
which may not be directly encoded in traditional features. By 
combining these sources of information, we aim to develop a 
predictive  model  that  is  both  powerful  and  transparent, 
satisfying both technical and regulatory demands.

This study situates itself within a broader shift in credit 
analyticsfrom static, snapshot-based assessments to dynamic, 
data-driven  risk  evaluations.  With  the  proliferation  of  big 
data technologies and the increasing digitization of financial 
services,  credit  risk  modeling  can  now  incorporate  vast 
volumes of information, ranging from social media behavior 
to  mobile  phone  usage  patterns.  Although  such  data  is 
beyond the scope of this current work, the hybrid framework 
we  propose  can  be  extended  to  accommodate  these  richer

---

<!-- PAGE 2 -->

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025

in

future  studies.  This  adaptability

further 
datasets 
underscores  the  potential  utility  of  hybrid  AI  models  in 
evolving financial ecosystems.

The  contribution  of  this  paper  is  threefold.  First,  we 
present  a  rigorous  hybrid  architecture  that  integrates  neural 
network and econometric components, validated on publicly 
available and proprietary datasets. Second, we systematically 
evaluate  the  performance  of  this  hybrid  model  against 
baseline  approaches  using  multiple  evaluation  metrics  such 
as accuracy, AUC-ROC, and F1-score. Third, we address the 
issue  of  explainability  by  employing  SHAP  (SHapley 
Additive exPlanations) values to interpret the contribution of 
individual  features,  offering  insights  into  the  decision-
making process of the model. These contributions align with 
current academic and industry needs for models that are both 
effective and accountable.

2. Literature Review

index

Altman,  E.  (1968).  Altman’s  work  is  one  of  the 
earliest and most influential studies in credit risk analysis. 
He introduced the Z-score model, which uses discriminant 
analysis to combine multiple financial ratios into a single 
predictive 
risk.  The  study 
for  bankruptcy 
demonstrated  that  statistical  techniques  could  outperform 
expert  judgment  in  identifying  distressed  firms,  thereby 
the  groundwork  for  quantitative  credit  risk 
laying 
modeling.  It  remains  a  benchmark  in  financial  risk 
literature  and  is  widely  cited  in  both  academic  and 
industry settings. [1]

Thomas,  L.  C.,  Edelman,  D.  B.,  &  Crook,  J.  N. 
(2002). This book provides a comprehensive examination 
of  credit  scoring  methods,  covering  both  theoretical 
models  and  their  practical  deployment  in  consumer 
lending. The authors discuss statistical techniques such as 
logistic 
scorecard 
development.  Their  work  emphasizes  the  importance  of 
model  validation,  regulatory  compliance,  and  risk-based 
pricing,  and  it  has  become  a  foundational  reference  for 
practitioners  and  researchers  working  on  the  design  and 
application of credit scoring systems. [2]

regression,  decision

trees,  and

Tian, S., Yu, Y., & Gu, D. (2015). Tian et al. focused 
on  the  variable  selection  process,  which  is  critical  for 
building robust predictive models. They evaluated various 
feature  selection  techniquessuch  as  stepwise  regression 
and  principal  component  analysis  (PCA)to  determine  the 
most  informative  financial  indicators  for  bankruptcy 
forecasting. Their  findings  show  that  model  performance 
is highly sensitive to the chosen input features, reinforcing 
the  need  for  thoughtful  feature  engineering  and  selection 
in credit default prediction. [3]

Yeh, I. C., & Lien, C. H. (2009). This study compared 
several  machine  learning  algorithms,  including  decision 
trees,  neural  networks,  and  support  vector  machines,  for 
predicting  default  among  credit  card  users.  Using  a  real-
world  dataset  from  a  financial  institution,  Yeh  and  Lien 
found  that  neural  networks  and  SVMs  outperformed

in  terms  of  predictive 
traditional  statistical  models 
accuracy.  Their  work  was  among  the  early  efforts  to 
introduce  AI-based  methods 
scoring, 
demonstrating 
learning  for 
complex financial data. [4]

the  value  of  non-linear

into  credit

Lessmann,  S.,  Baesens,  B.,  Seow,  H. V.,  & Thomas, 
L. C. (2015). Lessmann et al. conducted a comprehensive 
benchmarking study of classification algorithmsincluding 
ensemble  methods,  boosting,  bagging,  and  neural 
networksacross  multiple  credit  scoring  datasets.  They 
evaluated  models  based  on  performance  metrics  such  as 
AUC  and  accuracy.  The  study  concluded  that  ensemble 
methods  like  random  forests  and  gradient  boosting 
consistently  yielded  superior  performance,  challenging 
the  dominance  of  logistic  regression  in  the  industry  and 
encouraging adoption of more advanced techniques. [5]

tested  various  classification

Brown,  I.,  &  Mues,  C.  (2012).  Brown  and  Mues 
addressed  the  issue  of  class  imbalance,  a  common 
challenge  in  credit  risk  datasets  where  defaults  are  rare. 
They 
techniques  and 
resampling strategies, such as SMOTE and cost-sensitive 
learning,  to  improve  model  performance  on  the  minority 
class.  Their  results  highlight  that  handling  imbalance 
effectively is crucial for real-world deployment, as models 
trained  on  skewed  data  often  exhibit  biased  predictions. 
This  work  is  especially  relevant  for  institutions  focused 
on  reducing  false  negatives  (i.e.,  undetected  defaulters). 
[6]

3. Objective and Research Questions 
3.1. Objective

The  primary  objective  of  this  study  is  to  develop  and 
evaluate  a  hybrid  credit  default  prediction  model  that 
combines  the  interpretability  of  traditional  econometric 
methods  with  the  nonlinear  predictive  power  of  neural 
network  architectures.  Specifically,  we  aim  to  construct  a 
computational  framework  that  integrates  Long  Short-Term 
capturing 
Memory 
sequential patterns in behavioral datawith logistic regression 
models  based  on  structured  financial  and  demographic 
features.  This  fusion  is  intended  to  address  the  limitations 
inherent  in  using  either  modeling  paradigm  alone:  the 
rigidity and linearity of classical statistical models on the one 
hand,  and  the  opacity  and  regulatory  challenges  of  deep 
learning models on the other.

(LSTM)  networkswell-suited

for

The hybrid model is designed to process two complementary 
sources of information:

  Time-series  behavioral  data  such  as  monthly 
repayment  records,  credit  usage  patterns,  and 
delinquency  events,  which  are  fed  into  the  LSTM 
layers.

  Static  or  aggregated  econometric  variables  like 
credit 
and 
employment  status,  which  are  modeled  using 
logistic regression.

income-to-debt

scores,

ratios,

82

---

<!-- PAGE 3 -->

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025

By  combining  these  two  dimensions,  the  study  seeks  to 
accomplish several key goals:



Improve  predictive  performance  by  capturing  both 
linear 
in 
borrower behavior.

trends  and  nonlinear  dependencies

  Enhance  model  explainability  through  the  use  of 
interpretable  features  from  logistic  regression  and 
post  hoc  tools  such  as  SHAP  (SHapley  Additive 
exPlanations).

  Ensure  adaptability  and  scalability  of  the  hybrid 
framework  to  real-world  financial  environments 
where  both 
regulatory  compliance  and  high 
accuracy are critical.

  Bridge  methodological  gaps  in  the  literature  by 
theory  with  neural

synthesizing  econometric 
computation in a unified modeling approach.

4. Dataset and Preprocessing

financial

To develop and evaluate the proposed hybrid model for 
credit  default  prediction,  this  study  utilized  two  distinct 
datasets:  (1)  the  UCI  Credit  Card  Default  Dataset,  which  is 
publicly  available,  and  (2)  a  proprietary  dataset  obtained 
institution  under  a  confidentiality 
from  a 
agreement.  The  inclusion  of  these  two  datasets  enables  a 
more  comprehensive  evaluation  across  different  data 
environmentsone  standardized  and  widely  used  in  academic 
research,  the  other  representative  of  real-world  financial 
applications.  Together,  they  provide  a  balanced  and  robust 
foundation  for  training,  validating,  and  testing  the  hybrid 
model.

The UCI Credit Card Default Dataset consists of 30,000 
instances  with  24  features,  capturing  demographic  and 
financial  characteristics  of  Taiwanese  credit  card  clients  for 
the  year  2005.  Key  variables  include  age,  sex,  education, 
marital  status,  payment  history  for  the  previous  six  months, 
bill amounts, and payment amounts. The target variable is a 
binary  flag  indicating  whether  a  client  defaulted  on  their 
payment in the next month. Despite being dated, this dataset 
remains  a  benchmark  in  credit  risk  prediction  due  to  its 
structured format and clean labeling.

The proprietary dataset, on the other hand, is larger and 
more diverse, consisting of 45,000 customer records with 32 
features  collected  over  a  24-month  period.  This  dataset 
includes  transaction-level  behavior  logs,  such  as  ATM 
withdrawals,  mobile  banking  usage,  credit  utilization 
patterns,  monthly income, account balance  fluctuations, and

repayment behaviors. It also  contains standard demographic 
and  financial  indicators.  The  default  flag  here  represents  a 
failure  to  meet  minimum  repayment  obligations  for  at  least 
90  consecutive  daysa  definition  consistent  with  regulatory 
standards (e.g., Basel III guidelines).

Both datasets required extensive preprocessing to ensure 
compatibility  with  machine  learning  workflows.  The  first 
step  involved  data  cleaning,  where  missing  values  were 
handled  using  the  k-Nearest  Neighbors  (k-NN)  imputation 
method  for  numerical  attributes,  and  mode  imputation  for 
categorical attributes. Extreme outliersespecially in financial 
attributes  like  bill  amountswere  capped  using  winsorization 
at the 1st and 99th percentiles to mitigate the impact of data 
skewness.

Feature  encoding  was  applied  to  categorical  variables. 
For  low-cardinality  categorical  features  such  as  gender  or 
education  level,  one-hot  encoding  was  used.  For  high-
cardinality fields (e.g., occupation or employer region in the 
proprietary  data),  target  encoding  was  employed  to  avoid 
dimensional  explosion.  All  numerical  features  were  then 
normalized using Min-Max scaling to transform them into a 
[0,  1]  range,  ensuring  that  they  contribute  equally  to  the 
training process of neural networks.

For  the  time-series  components  in  the  proprietary 
dataset, sequences  were constructed by organizing customer 
behavior  over  sliding  6-month  windows.  Each  customer 
record  was  transformed  into  a  sequence  of  behavioral 
vectors,  allowing  the  LSTM  layers  in  the  hybrid  model  to 
learn  temporal  dependencies.  Sequences  shorter  than  six 
months  were  excluded  from  LSTM  training  to  maintain 
sequence 
to 
incorporate  behavioral  trends  such  as  increasing  payment 
delays or decreasing account balances.

length  uniformity.  This  step  allowed  us

To  prevent  data  leakage,  all  temporal  variables  were 
carefully  aligned  to  ensure  that  no  future  information  was 
available at the point of prediction. Additionally, the dataset 
was  randomly  split  into  training  (70%),  validation  (15%), 
and test sets (15%), stratified on the default flag to preserve 
the  class  distribution.  Class  imbalancewhich  is  common  in 
credit default prediction taskswas addressed using  Synthetic 
Minority  Over-sampling  Technique  (SMOTE)  applied  only 
to  the  training  data,  ensuring  the  model  had  sufficient 
exposure to default cases without biasing evaluation results.

Dataset 
UCI Credit Card Default 
Financial Institution

Instances  Features  Default Rate

30,000 
45,000

24 
32

22.1% 
18.7%

Time-Series Data 
No

Source Type 
Public Benchmark 
Yes (6-month window)  Proprietary Dataset

Table 1: Dataset Overview

5.  Model  Architecture  and  Hybridization 
Strategy

In this study, we propose a hybrid AI model designed to 
effectively  combine  the  temporal  learning  capabilities  of 
deep neural networks  with the interpretability and statistical

reliability  of  traditional  econometric  models.  The  hybrid 
architecture  integrates  two  key  components:  (1)  a  Long 
for  modeling 
Short-Term  Memory 
behavioral  time-series  data,  and  (2)  a  logistic  regression 
that  operates  on  structured,  static  econometric 
layer 
two  branches  are 
variables.  The  outputs  from

(LSTM)  network

these

83

---

<!-- PAGE 4 -->

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025

concatenated  and  passed  through  a  final  sigmoid  activation 
to yield the probability of credit default. This architecture is 
designed  to  achieve  both  high  predictive  accuracy  and 
explainable  outputs,  addressing  a  crucial 
in 
financial machine learning applications.

trade-off

the  Adam  optimizer. A  learning  rate  scheduler  was  used  to 
adjust the rate based on validation loss. Early stopping based 
on  validation  AUC  was  applied  to  prevent  overtraining. 
Batch  normalization  and  dropout  layers  (with  a  rate  of  0.3) 
were introduced after dense layers to stabilize learning.

The rationale for including LSTM layers is their proven 
ability to capture long-term dependencies in sequential data. 
In  our  context,  behavioral  features  such  as  monthly 
repayments, bill amounts, and credit utilization trends across 
multiple  time  points  form  sequences  that  contain  predictive 
patterns  related  to  emerging  credit  risk.  Traditional  models, 
which  aggregate  or  summarize  these  variables,  often  lose 
temporal  information.  The  LSTM  model  maintains  a  cell 
state  and  memory  gates  that  allow  it  to  learn  whether  a 
customer’s risk trajectory is improving or deteriorating over 
for  dynamic  credit  scoring. 
timecapabilities  essential 
Logistic  regression 
to  model  structured 
is  employed 
econometric  indicators  such  as  income  level,  employment 
status,  debt-to-income  ratio,  number  of  dependents,  and 
education.

interpretable

These features are generally  not temporal in  nature  and 
provide  valuable, 
information  about  a 
customer’s  creditworthiness.  Logistic  regression  has  long 
been  favored  in  credit  risk  modeling  due  to  its  ease  of 
explanation,  compliance  with  regulatory  standards  (e.g., 
Basel II/III), and ability to provide odds ratios that make risk 
assessments  transparent  to  both  analysts  and  auditors.  The 
hybridization strategy involves parallel processing of the two 
input  branches.  The  behavioral  sequence  is  passed  through 
one  or  more  LSTM  layers,  followed  by  a  dense  (fully 
connected) layer that reduces the hidden representation into a 
fixed-dimensional  vector. Simultaneously, the  static  features 
are  passed  directly  into  a  logistic  regression  layer.  The 
outputs of both models are concatenated and passed through 
a  final  sigmoid-activated  dense  layer,  which  produces  the 
final probability of default. This fused output leverages both 
historical behavioral trends and static risk indicators.

Equation 1: Hybrid Output Probability

Where:

To  ensure  alignment  between  the  dimensions  of  the 
LSTM  and 
logistic  regression  outputs,  both  branches 
undergo  a  dimensionality  reduction  step  using  dense  layers 
before  concatenation.  This  ensures  efficient  training  and 
avoids  overfitting  due 
to  excessive  parameterization. 
Additionally,  we  use  dropout  layers  in  the  LSTM  branch  to 
prevent  overfitting,  and  L2  regularization  in  the  logistic 
regression component to control coefficient magnitudes. The 
model  was  implemented  using  TensorFlow  2.x  and  trained 
using  the  binary  cross-entropy  loss  function  optimized  with

Fig 1: Proposed Hybrid Architecture

This  Figure  1,  hybrid  framework  serves  as  a  modular 
and extensible structure, allowing for the future inclusion of 
additional  components  (e.g.,  attention  mechanisms,  GRU 
layers,  or  external  macroeconomic  data  streams).  Its  dual-
branch design not only improves predictive performance but 
interpretability  and  auditability  crucial 
also  enhances 
financial 
deployment 
for 
elements 
environments.

regulated

in

6. Performance Evaluation and Metrics

Evaluating  the  performance  of  a  hybrid  credit  default 
prediction  model  requires  a  rigorous,  multi-metric  approach 
that accounts for both classification accuracy and the ability 
to  generalize  in  imbalanced  financial  datasets.  Given  the 
asymmetric  cost  of  misclassifying  defaulters  versus  non-
a 
defaulters 
comprehensive  suite  of  evaluation  metrics  that  includes: 
Accuracy,  Precision,  Recall,  F1-score,  and  Area  Under  the 
Receiver Operating Characteristic Curve (AUC-ROC). These 
metrics  provide  complementary  insights  into  the  model’s 
utility in both operational and risk-sensitive contexts.

applications,  we

real-world

adopt

in

To  begin  with,  Accuracy  offers  a  straightforward 
measure  of  correct  classifications  over  all  predictions. 
However,  due  to  the  inherent  class  imbalance  in  credit 
default  data  where  defaulters  typically  constitute  less  than 
25%  of  the  sample  accuracy  alone  can  be  misleading. 
Therefore,  we  focus  closely  on  Precision  (the  proportion  of 
predicted  defaulters  who  actually  default)  and  Recall  (the 
proportion  of  actual  defaulters  correctly  predicted),  both  of 
which  capture  the  model's  sensitivity  and  specificity  in  a 
more nuanced way.

The F1-score, being the harmonic mean of precision and 
recall,  is  especially  critical  in  scenarios  where  both  false 
positives and false negatives have financial implications. For

84

---

<!-- PAGE 5 -->

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025

instance, high false negatives (missed defaulters) can lead to 
unrecovered  loans,  while  high  false  positives  (incorrectly 
lending 
flagged  non-defaulters)  may  result

in  missed

opportunities.  Hence,  a  high  F1-score  indicates  a  well-
balanced model capable of minimizing both risk types.

Table 2: Model Performance Comparison

Model 
Logistic Regression 
LSTM Only 
Hybrid Model

Accuracy  Precision  Recall  F1-score  AUC-ROC 
0.72 
0.78 
0.85

0.81 
0.85 
0.91

0.69 
0.74 
0.80

0.65 
0.70 
0.76

0.78 
0.82 
0.87

Most  importantly,  evaluate  the AUC-ROC,  which  plots 
the true positive rate (Recall) against the false positive rate (1 
-  Specificity)  at  various  threshold  settings.  AUC-ROC  is 
particularly  useful  in  credit  scoring  because  it  is  threshold-
independent  and  captures  the  model’s  ability  to  rank  risk 
levels  across  the  entire  population.  An  AUC  of  1  indicates 
perfect  classification,  while  0.5  corresponds  to  random 
guessing.  In  this  study,  AUC-ROC  serves  as  the  primary 
metric for model comparison.

Table 2, the hybrid model consistently outperforms both 
the  standalone  logistic  regression  and  the  LSTM-only 
models  across  all  key  metrics.  Notably,  the  hybrid  model 
achieves  an  F1-score  of  0.80  and  an  AUC-ROC  of  0.91, 
indicating  not  only  robust  classification  ability  but  also 
superior ranking capability. These gains validate the synergy 
between  the  temporal  sequence  learning  of  LSTM  and  the 
interpretable static feature modeling of logistic regression.

Fig 2: ROC Curves for All Models

In Figure 2, the ROC curve of the hybrid model clearly 
dominates the others, with the greatest distance from the 45-
degree  diagonal  line  (random  classifier).  The  hybrid  model 
achieves  consistently  higher  true  positive  rates  across  all 
thresholds,  making  it  especially  suitable  for  deployment  in 
settings  where  risk-based  pricing  or  threshold  adjustments 
are  required.  To  ensure  the  robustness  of  these  results,  we 
conducted  5-fold  cross-validation  and  reported  the  average 
metric  values  across  folds.  Variance  in  AUC-ROC  and  F1-
scores was below 1.5% across folds, indicating strong model 
stability. We  also  validated  the  model  on  a  hold-out  test  set 
representing 15% of the total data, stratified to maintain class 
balance.  Results  on  this  test  set  closely  mirrored  validation 
performance, confirming the generalizability of the model.

7. Feature Importance and Explainability

In  the  domain  of  credit  risk  modeling,  predictive 
performance  alone  is  insufficient  model  explainability  is 
equally  critical,  particularly  in  regulated  financial  sectors.

Lenders,  auditors,  and  regulators  require  transparency  to 
ensure  that  credit  decisions  are  fair,  accountable,  and  free 
from  discriminatory  biases.  To  address  this  need,  we 
employed  SHAP (SHapley Additive exPlanations)a state-of-
the-art method rooted in cooperative game theory to interpret 
the contributions of individual features in the hybrid model. 
SHAP assigns each feature an importance value representing 
its  impact  on  the  model’s  output  for  a  given  prediction, 
allowing for both global and local interpretability.

SHAP was applied separately to both components of the 
hybrid  model.  For  the  logistic  regression  branch,  SHAP 
explanations  aligned  well  with  coefficient  magnitudes, 
confirming the reliability of the linear model’s structure. For 
the  LSTM  component,  SHAP  values  were  computed  using 
Deep SHAP, an extension designed for deep learning models. 
interactions  between 
These  values  captured  complex 
behavioral  trends  such  as  increasing  monthly  balances  and

85

---

<!-- PAGE 6 -->

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025

delayed  repaymentsand  credit  default  risk,  highlighting  the 
LSTM’s ability to detect non-linear patterns.

Equation 2: SHAP Value Computation

Results indicated variables such as credit utilization, past 
defaults, and income level were most predictive.

The  global  SHAP  analysis  revealed  that  a  few  econometric 
features  consistently  played  dominant  roles  in  predicting 
credit default. These include:

  Debt-to-Income  Ratio  (DTI):  High  DTI  values

significantly increased default probability.

  Past  Delinquency  Events:  A  strong  positive 
association with default, confirming prior literature. 
  Credit  Utilization  Rate:  Borrowers  with  utilization 
above  80%  were  substantially  more  likely  to 
default. 
Income  Level:  Lower  income  segments  showed 
elevated SHAP values for default risk.



  Age:  Younger  borrowers  contributed  more

to 
industry

predicted  defaults, 
expectations.

consistent  with

Fig 3: SHAP Summary Plot for Econometric Features

Figure 3 shows the distribution of feature impacts on the 
model’s  output.  Each  point  represents  a  SHAP  value  for  a 
feature  in  an  individual  prediction.  Red  points  denote  high 
feature  values,  while  blue  points  indicate  low  values.  For 
example,  the  DTI  feature  shows  a  clear  gradient:  high  DTI 
(in  red)  corresponds  to  high  SHAP  values,  increasing  the 
likelihood of default. This visualization aids in understanding 
feature  effects  across  the  population,  not  just  for  individual 
predictions.

Furthermore,  we

individual  prediction 
explored 
explanations  using  SHAP  force  plots  to  visualize  how  each 
feature  pushed  the  model  output  toward  or  away  from  the 
decision  threshold.  In  one  representative  case,  a  borrower 
with  high  income  and  moderate  utilization  but  a  recent  late 
payment  showed  a  nuanced  risk  profile:  static  features 
lowered  the  default  probability,  but  the  temporal  trend  in

repayment  delays  from  the  LSTM  component  increased  the 
riskhighlighting  the  advantage  of  a  hybrid  model  that 
integrates both dimensions.

To  validate  these  findings,  we  conducted  a  correlation 
analysis  between  SHAP  values  and  raw  feature  values, 
confirming  that  the  model’s  learned  behavior  aligned  with 
economic  theory  and  domain  knowledge.  For  instance,  the 
positive  correlation  between  utilization  rate  and  SHAP 
values matched expectations that higher credit usage implies 
higher risk.

8. Comparative Analysis and Visualization

To  critically  assess  the  performance  of  the  proposed 
hybrid  AI  model  in  contrast  to  traditional  and  standalone 
machine  learning  approaches,  we  conducted  a  comparative 
analysis  across  three  key  models:  (1)  Logistic  Regression, 
(2)  LSTM-only,  and  (3)  the  Hybrid  LSTM  +  Logistic 
Regression  model.  This  comparative  evaluation  is  essential 
to  quantify  the  added  value  of  hybridization,  not  only  in 
numerical  performance  metrics  but  also 
terms  of 
in 
classification behavior across various thresholds.

Equation 3: AUC Calculation

ROC and AUC clearly favor the hybrid approach, especially 
in high-recall zones.

All  three  models  were  trained  on  the  same  datasets, 
train-validation-test  splits,  preprocessing 
using  identical 
pipelines,  and  evaluation  protocols.  Metrics 
including 
accuracy,  precision,  recall,  F1-score,  and  AUC-ROC  were 
computed  to  offer  a  multidimensional  view  of  model 
effectiveness. However, the most insightful comparative tool 
for  imbalanced  binary  classification  problems  like  credit 
default  prediction  is  the  Receiver  Operating  Characteristic 
(ROC)  curve,  which  allows  for  visual  comparison  of 
classifier  performance 
all  possible  decision 
across 
thresholds.

Figure  4  shows  the  ROC  curves  for  each  model  on  the 
test  set.  The  curve  corresponding  to  the  Hybrid  model  lies 
clearly  above  those  of  the  Logistic  Regression  and  LSTM-
only  models,  reflecting  a  superior  trade-off  between  true 
positive  rate  (TPR)  and  false  positive  rate  (FPR). The Area 
Under the Curve (AUC) values further corroborate this: 0.91 
for  the  Hybrid  model,  0.85  for  the  LSTM,  and  0.81  for 
Logistic  Regression.  These  results  confirm  that  the  hybrid 
approach  delivers  enhanced  discriminatory  power  and  more 
reliable risk ranking.

The  curve  for  the  LSTM-only  model  also  outperforms 
logistic  regression  across  most  thresholds,  indicating  its 
strength in capturing behavioral patterns in time-series data. 
However,  it  falls  short  of  the  hybrid  model,  particularly  in 
low  FPR  regions,  which  are  critical  in  financial  settings 
where  false  positives  (i.e.,  denying  credit  to  a  creditworthy 
customer)  must  be  minimized.  This  highlights  a  key 
advantage  of  the  hybrid  approachit  retains  the  temporal

86

---

<!-- PAGE 7 -->

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025

sensitivity  of  LSTM  while  incorporating  the  economic 
rationale  and  calibration  of  logistic  regression,  resulting  in 
more balanced performance.

Fig 4: Data Flow through Each Model

Further analysis shows that the  hybrid  model  maintains 
a higher TPR without a significant increase in FPR, making 
it  suitable  for  credit  risk  environments  where  high  recall 
(catching  true  defaulters)  is  critical,  but  false  alarms  must 
still  be  controlled.  For  example,  at  a  decision  threshold 
yielding a TPR of 85%, the hybrid model records an FPR of 
only 15%, compared to 23% for the LSTM-only  model and 
29% 
regression.  This  efficiency  directly 
translates  into  lower  credit  losses  and  better  risk-adjusted 
lending decisions.

logistic

for

We also visualized  Precision-Recall (PR) curves,  which 
are  more  informative  for  imbalanced  datasets.  The  hybrid 
model again showed dominance with the highest area under 
the  PR  curve,  affirming  that  its  predictive  power  is  not  an 
artifact of majority class learning, but rather a genuine ability 
to discriminate minority class events (defaults). Additionally, 
we used calibration plots to assess the reliability of predicted 
probabilities.  The  hybrid  model  exhibited  near-perfect 
calibration, while the LSTM showed signs of overconfidence 
and logistic regression tended to underestimate risk at higher 
score bands.

The  comparative  visualizations  thus  reinforce  both  the 
quantitative  superiority  and  qualitative  robustness  of  the 
hybrid  architecture.  The  ROC  and  PR  curves  provide 
intuitive evidence that the hybrid model is better at managing 
the risk-reward trade-offs essential in credit decision-making. 
It  adapts  to  behavioral  trends  through  LSTM  layers  while

anchoring  predictions  in  interpretable,  domain-grounded 
features via logistic regression.

9. Discussion, Limitations, and Future Work 
9.1. Discussion

This  study  demonstrates  the  efficacy  of  a  hybrid 
modeling  approach  that  integrates  deep  learning  (LSTM) 
with  traditional  econometric  techniques  (logistic  regression) 
for  the  purpose  of  predicting  credit  default.  The  hybrid 
model  outperformed  both  standalone  models  in  all  major 
performance  metrics,  particularly  in  AUC-ROC  and  F1-
score,  suggesting  it  not  only  identifies  defaulters  more 
accurately  but  also  balances  false  positives  and  false 
negatives  more  effectively.  This  balance  is  essential  for 
financial  institutions  aiming  to  maximize  profitability  while 
maintaining regulatory compliance and operational fairness.

The  strength  of  the  hybrid  model  lies  in  its  ability  to 
capture  both  temporal  and  static  risk  signals.  The  LSTM 
component  effectively  processes  behavioral  trendssuch  as 
rising credit utilization or erratic payment behaviorover time, 
which  are  early  indicators  of  deteriorating  creditworthiness. 
The  logistic  regression  component,  meanwhile,  provides 
interpretable  outputs  based  on  well-established  financial 
indicators  like  debt-to-income  ratio,  credit  history,  and 
income  level.  By  merging  these  insights  in  a  single 
richer, 
the  hybrid  model  provides 
architecture, 
multidimensional understanding of credit risk.

a

The  use  of  SHAP  (SHapley  Additive  exPlanations) 
values  further  enhances  the  model’s  interpretability.  SHAP 
analyses confirmed that key features like past delinquencies, 
utilization  rate,  and  income  had  consistent  and  theoretically 
sound impacts on default predictions. This interpretability is 
vital  in  regulated  domains,  where  model  decisions  must  be 
explainable to regulators, auditors, and consumers. Thus, the 
transparency  for 
hybrid  model  does  not  compromise 
performance  a  common 
learning 
applications.

in  deep

trade-off

9.2. Limitations 
Despite

limitations 
the  promising  results,  several 
warrant discussion. The generalizability of the model may be 
constrained  by  the  characteristics  of  the  datasets  used.  The 
UCI  dataset,  while  popular,  is  based  on  credit  data  from 
Taiwanese  consumers  in  2005,  and  the  proprietary  dataset, 
although  more  recent,  reflects  the  credit  practices  and 
demographic  structure  of  a  single  financial  institution. As  a 
result,  the  model’s  performance  may  vary  when  applied  to 
different populations, geographies, or lending environments.

tuning.  This

Next  LSTM  networks  are  powerful  for  sequence 
modeling;  they  are  also  computationally  intensive  and 
require  significant 
increases  deployment 
complexity,  especially  in  low-latency  environments  such  as 
real-time credit scoring. Additionally, LSTM’s internal states 
and gate mechanisms remain opaque despite SHAP post-hoc 
explanations, limiting the full interpretability of the temporal 
component.

87

---

<!-- PAGE 8 -->

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025

Finance:  A  Literature  Review.  Risks  2021,  9,  192. 
https://doi.org/10.3390/risks9110192

[8]  Longyue  Liang.  et  al.  2020.  Forecasting  peer-to-peer 
platform  default  rate  with  LSTM  neural  network. 
Electronic  Commerce  Research  and  Applications. 
100997. 
2020, 
Volume 
https://doi.org/10.1016/j.elerap.2020.100997

43,  September–October

[9]  Ala’raj,  M.,  &  Abbod,  M.  (2016).  A  new  hybrid 
ensemble  credit  scoring  model  based  on  classifiers 
consensus  system  approach.  Expert  Systems  with 
Applications, 64, 36–55.

[10] Bo-Wen Chi. et la. 2012. A hybrid approach to integrate 
genetic algorithm into dual scoring  model in enhancing 
the  performance  of  credit  scoring  model.  Expert 
Systems  with  Applications.  Volume  39,  Issue  3,  15 
February 
2650-2661. 
https://doi.org/10.1016/j.eswa.2011.08.120

Pages

2012,

[11] Bo-Wen  Chi  and  Chiun-Chieh  Hsu.  2012.  A  hybrid 
approach to integrate genetic algorithm into dual scoring 
model  in  enhancing  the  performance  of  credit  scoring 
model. Expert Syst. Appl. 39, 3 (February, 2012), 2650–
2661. https://doi.org/10.1016/j.eswa.2011.08.120  
[12] https://bura.brunel.ac.uk/bitstream/2438/17809/2/FullTe

xt.pdf

Another  challenge  is  data  availability  and  quality.  The 
hybrid  model  assumes  access  to  high-frequency  behavioral 
data  (e.g.,  monthly  repayment  patterns),  which  may  not  be 
consistently  recorded  or  standardized  across  all  institutions. 
Moreover, synthetic balancing techniques like SMOTE, used 
to  address  class  imbalance,  may  introduce  bias  or  inflate 
model confidence if not carefully validated.

9.3. Future Work

attention  mechanisms

Several  directions  for  future  research  emerge  from  this 
study.  First,  there  is  significant  potential  in  incorporating 
macroeconomic  variables  and  external  data  streams  such  as 
interest  rates,  unemployment  levels,  or  consumer  sentiment 
indicesinto the hybrid framework. These could be fed into a 
third  model  branch  or  dynamically  interact  with  existing 
inputs  to  better  reflect  changing  economic  conditions  that 
affect  default  risk.  Next,  the  hybrid  model  can  be  extended 
with 
transformer-based 
architectures in place of or alongside LSTM. These  modern 
neural  architectures  have  shown  superior  performance  in 
other sequence learning tasks by better capturing long-range 
dependencies  and  allowing  the  model  to  focus  on  the  most 
relevant  time  steps.  Third,  future  work  should  consider 
multi-class  or  survival  analysis  frameworks  to  predict  not 
just  whether  a  default  will  occur,  but  when  it  is  likely  to 
happen.  This  temporal  dimension  would  be  particularly 
valuable  in  managing  portfolio  risk  and  setting  dynamic 
interest rates.

or

From  a  deployment  perspective,  efforts  should  also  be 
directed  toward  model  compression,  explainable  AI  (XAI) 
real-time  scoring  systems,  enabling 
dashboards,  and 
integration into production environments. Ensuring fairness, 
transparency,  and  compliance  with  data  privacy  regulations 
(e.g.,  GDPR,  CCPA)  will  also  be  critical  for  large-scale 
adoption.

References 
[1]  Altman,  E.

(1968).  Financial

ratios,  discriminant 
analysis and the prediction of corporate bankruptcy. The 
Journal of Finance, 23(4), 589–609.

[2]  Thomas, L. C., Edelman, D. B., & Crook, J. N. (2002).

Credit Scoring and Its Applications. SIAM.

[3]  Tian, S., Yu, Y., & Gu, D. (2015). Variable selection and 
Computational

bankruptcy

forecasts.

corporate 
Economics, 45(1), 41–62.

[4]  Yeh,  I.  C.,  &  Lien,  C.  H.  (2009).  The  comparisons  of 
data  mining  techniques  for  the  predictive  accuracy  of 
probability  of  default  of  credit  card  clients.  Expert 
Systems with Applications, 36(2), 2473–2480.

[5]  Lessmann,  S.,  Baesens,  B.,  Seow,  H. V.,  & Thomas,  L. 
C.  (2015).  Benchmarking  state-of-the-art  classification 
algorithms  for  credit  scoring.  European  Journal  of 
Operational Research, 247(1), 124–136.

[6]  Brown,  I.,  &  Mues,  C.  (2012).  An  experimental 
comparison  of  classification  algorithms  for  imbalanced 
credit 
sets.  Expert  Systems  with 
scoring  data 
Applications, 39(3), 3446–3453.

[7]  Kumar, A.; Sharma, S.; Mahdavi, M. Machine Learning 
(ML)  Technologies  for  Digital  Credit  Scoring  in  Rural

88

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal of Emerging Research in Engineering and Technology
Pearl Blue Research Group| Volume 6 Issue 2 PP 81-88, 2025
ISSN: 3050-922X | https://doi.org/10.63282/3050-922X.IJERET-V6I2P110
Original Article
A Study on Credit Default Prediction Using Hybrid AI Models
Combining Neural Architectures and Econometric Features
Santhosh Kumar Sagar Nagaraj
Staff Software Engineer, Visa Inc., Banking & Finance, 1745 stringer pass, Leander, Texas 78641, USA.
Received On: 25/03/2025 Revised On: 20/04/2025 Accepted On: 04/05/2025 Published On: 23/05/2025
Abstract - Credit default prediction plays a vital role in risk including fraud detection, stock forecasting, and customer
management, lending strategies, and financial stability. segmentation. These models are capable of modeling
While traditional econometric models offer interpretability, temporal dependencies, capturing latent representations, and
they often lack the predictive power of contemporary neural uncovering subtle patterns that econometric models may
networks. This study proposes a novel hybrid approach that miss. However, this increased predictive power comes at a
integrates deep neural network (DNN) architectures with key cost: deep learning models are often criticized for their
econometric indicators to improve the prediction of credit “black-box” nature, making them difficult to interpret or
default risk. We develop and evaluate several model justify in high-stakes financial decisions.
configurations, including a hybrid Long Short-Term Memory
(LSTM) and logistic regression framework, on publicly The limitations of using either econometric or deep
available credit datasets. The results show that hybrid learning models in isolation, this study proposes a hybrid
models outperform standalone econometric or deep learning approach that combines the strengths of both paradigms.
models in terms of accuracy, AUC-ROC, and F1-score. The Specifically, we integrate traditional econometric
study also explores feature importance to enhance model featuressuch as debt-to-income ratio, credit utilization, and
explainability. Our findings underscore the potential of historical delinquencywith the temporal modeling
combining statistical and AI methodologies for more capabilities of neural networks. The proposed model fuses
accurate and interpretable financial risk assessments. the outputs of an LSTM network, which processes sequential
behavioral data (e.g., transaction history), with the
Keywords - Credit Default Prediction, Hybrid AI Models, predictions of a logistic regression model based on structured
Econometric Features, Deep Learning, Neural Networks, financial indicators. This hybridization is designed to achieve
Logistic Regression, LSTM, Financial Risk Modeling, AUC- a balance between predictive accuracy and model
ROC, Interpretable AI. interpretability, which is critical for real-world applications
in banking and finance.
1. Introduction
Credit default prediction is a central problem in the The rationale behind the hybrid model is not merely
domain of financial risk management, influencing everything empirical but also conceptual. While econometric models
from loan approvals to regulatory oversight. The ability of offer clarity and justification for decisionsmaking them
financial institutions to accurately forecast the likelihood that suitable for regulated environmentsneural models can
a borrower will default on their loan obligations directly identify latent patterns and interactions that are often beyond
impacts profitability, portfolio health, and systemic financial human intuition. For instance, an LSTM model can detect
stability. Traditionally, credit risk models have relied heavily emerging default patterns based on time-series data such as
on econometric techniquessuch as logistic regression or monthly repayments, spending fluctuations, or ATM usage,
discriminant analysisthat use structured financial and which may not be directly encoded in traditional features. By
demographic variables. These models are known for their combining these sources of information, we aim to develop a
interpretability and compliance with regulatory frameworks predictive model that is both powerful and transparent,
like Basel II/III. However, they often fall short in capturing satisfying both technical and regulatory demands.
complex, nonlinear relationships inherent in borrower
behavior, particularly as financial data becomes more This study situates itself within a broader shift in credit
dynamic and multidimensional. analyticsfrom static, snapshot-based assessments to dynamic,
data-driven risk evaluations. With the proliferation of big
In recent years, the rise of machine learning (ML) and data technologies and the increasing digitization of financial
artificial intelligence (AI) has opened new avenues for services, credit risk modeling can now incorporate vast
enhancing credit risk assessment. Neural network volumes of information, ranging from social media behavior
architectures, particularly deep learning models like Long to mobile phone usage patterns. Although such data is
Short-Term Memory (LSTM) networks, have demonstrated beyond the scope of this current work, the hybrid framework
superior performance in a variety of predictive tasks, we propose can be extended to accommodate these richer

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025
datasets  in  future  studies.  This  adaptability  further  traditional  statistical  models  in  terms  of  predictive
underscores  the  potential  utility  of  hybrid AI  models  in  accuracy.  Their  work  was  among  the  early  efforts  to
evolving financial ecosystems.  introduce  AI-based  methods  into  credit  scoring,
|     |     |     |     |     | demonstrating  |     | the  value  | of  non-linear  |     | learning  | for  |
| --- | --- | --- | --- | --- | -------------- | --- | ----------- | --------------- | --- | --------- | ---- |
The contribution of this paper is threefold. First, we  complex financial data. [4]
| present a rigorous hybrid architecture that integrates neural  |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
network and econometric components, validated on publicly  Lessmann, S., Baesens, B., Seow, H. V., & Thomas,
available and proprietary datasets. Second, we systematically  L. C. (2015). Lessmann et al. conducted a comprehensive
evaluate  the  performance  of  this  hybrid  model  against  benchmarking study of classification algorithmsincluding
baseline approaches using multiple evaluation metrics such  ensemble  methods,  boosting,  bagging,  and  neural
as accuracy, AUC-ROC, and F1-score. Third, we address the  networksacross  multiple  credit  scoring  datasets.  They
issue  of  explainability  by  employing  SHAP  (SHapley  evaluated models based on performance metrics such as
Additive exPlanations) values to interpret the contribution of  AUC and accuracy. The study concluded that ensemble
individual  features,  offering  insights  into  the  decision- methods  like  random  forests  and  gradient  boosting
making process of the model. These contributions align with  consistently  yielded  superior  performance,  challenging
current academic and industry needs for models that are both  the dominance of logistic regression in the industry and
effective and accountable.  encouraging adoption of more advanced techniques. [5]
|     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2. Literature Review  Brown,  I.,  &  Mues,  C.  (2012).  Brown  and  Mues
|          |              |           |       |                   | addressed  |     | the  issue  of  | class  imbalance,  |     | a  common  |     |
| -------- | ------------ | --------- | ----- | ----------------- | ---------- | --- | --------------- | ------------------ | --- | ---------- | --- |
| Altman,  | E.  (1968).  | Altman’s  | work  | is  one  of  the  |            |     |                 |                    |     |            |     |
earliest and most influential studies in credit risk analysis.  challenge in credit risk datasets where defaults are rare.
He introduced the Z-score model, which uses discriminant  They  tested  various  classification  techniques  and
resampling strategies, such as SMOTE and cost-sensitive
analysis to combine multiple financial ratios into a single
predictive  index  for  bankruptcy  risk.  The  study  learning, to improve model performance on the minority
demonstrated that statistical techniques could outperform  class.  Their  results  highlight  that  handling  imbalance
effectively is crucial for real-world deployment, as models
expert judgment in identifying distressed firms, thereby
trained on skewed data often exhibit biased predictions.
| laying  | the  groundwork  | for  | quantitative  | credit  risk  |     |     |     |     |     |     |     |
| ------- | ---------------- | ---- | ------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
modeling.  It  remains  a  benchmark  in  financial  risk  This work is especially relevant for institutions focused
literature  and  is  widely  cited  in  both  academic  and  on reducing false negatives (i.e., undetected defaulters).
[6]
industry settings. [1]
|     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thomas,  L.  C.,  Edelman,  D.  B.,  &  Crook,  J.  N.  3. Objective and Research Questions
| (2002). This book provides a comprehensive examination  |     |     |     |     | 3.1. Objective  |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
of  credit  scoring  methods,  covering  both  theoretical  The primary objective of this study is to develop and
models  and  their  practical  deployment  in  consumer  evaluate  a  hybrid  credit  default  prediction  model  that
lending. The authors discuss statistical techniques such as  combines  the  interpretability  of  traditional  econometric
logistic  regression,  decision  trees,  and  scorecard  methods  with  the  nonlinear  predictive  power  of  neural
development. Their work emphasizes the importance of  network architectures. Specifically, we aim to construct a
model validation, regulatory compliance, and risk-based  computational framework that integrates Long Short-Term
pricing, and it has become a foundational reference for  Memory  (LSTM)  networkswell-suited  for  capturing
practitioners and researchers working on the design and  sequential patterns in behavioral datawith logistic regression
application of credit scoring systems. [2]  models  based  on  structured  financial  and  demographic
  features. This fusion is intended to address the limitations
Tian, S., Yu, Y., & Gu, D. (2015). Tian et al. focused  inherent  in  using  either  modeling  paradigm  alone:  the
on the variable selection process, which is critical for  rigidity and linearity of classical statistical models on the one
building robust predictive models. They evaluated various  hand, and the opacity and regulatory challenges of deep
feature selection techniquessuch as stepwise regression  learning models on the other.
| and principal component analysis (PCA)to determine the  |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
most  informative  financial  indicators  for  bankruptcy  The hybrid model is designed to process two complementary
forecasting. Their findings show that model performance  sources of information:
is highly sensitive to the chosen input features, reinforcing    Time-series  behavioral  data  such  as  monthly
the need for thoughtful feature engineering and selection
|     |     |     |     |     |     | repayment  | records,  | credit  | usage  | patterns,  | and  |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | ------- | ------ | ---------- | ---- |
in credit default prediction. [3]  delinquency events, which are fed into the LSTM
|     |     |     |     |     |     | layers.  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
Yeh, I. C., & Lien, C. H. (2009). This study compared
|     |     |     |     |     |     |   Static  | or  aggregated  | econometric  |     | variables  | like  |
| --- | --- | --- | --- | --- | --- | ---------- | --------------- | ------------ | --- | ---------- | ----- |
several machine learning algorithms, including decision  credit  scores,  income-to-debt  ratios,  and
trees, neural networks, and support vector machines, for  employment  status,  which  are  modeled  using
predicting default among credit card users. Using a real- logistic regression.
| world dataset from a financial institution, Yeh and Lien  |                   |      |       |               |     |     |     |     |     |     |     |
| --------------------------------------------------------- | ----------------- | ---- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| found  that                                               | neural  networks  | and  | SVMs  | outperformed  |     |     |     |     |     |     |     |
82

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025
By combining these two dimensions, the study seeks to repayment behaviors. It also contains standard demographic
accomplish several key goals: and financial indicators. The default flag here represents a
 Improve predictive performance by capturing both failure to meet minimum repayment obligations for at least
linear trends and nonlinear dependencies in 90 consecutive daysa definition consistent with regulatory
borrower behavior. standards (e.g., Basel III guidelines).
 Enhance model explainability through the use of
interpretable features from logistic regression and Both datasets required extensive preprocessing to ensure
post hoc tools such as SHAP (SHapley Additive compatibility with machine learning workflows. The first
exPlanations). step involved data cleaning, where missing values were
 Ensure adaptability and scalability of the hybrid handled using the k-Nearest Neighbors (k-NN) imputation
framework to real-world financial environments method for numerical attributes, and mode imputation for
where both regulatory compliance and high categorical attributes. Extreme outliersespecially in financial
accuracy are critical. attributes like bill amountswere capped using winsorization
 Bridge methodological gaps in the literature by at the 1st and 99th percentiles to mitigate the impact of data
synthesizing econometric theory with neural skewness.
computation in a unified modeling approach.
Feature encoding was applied to categorical variables.
For low-cardinality categorical features such as gender or
4. Dataset and Preprocessing
education level, one-hot encoding was used. For high-
To develop and evaluate the proposed hybrid model for
cardinality fields (e.g., occupation or employer region in the
credit default prediction, this study utilized two distinct
proprietary data), target encoding was employed to avoid
datasets: (1) the UCI Credit Card Default Dataset, which is
dimensional explosion. All numerical features were then
publicly available, and (2) a proprietary dataset obtained
normalized using Min-Max scaling to transform them into a
from a financial institution under a confidentiality
[0, 1] range, ensuring that they contribute equally to the
agreement. The inclusion of these two datasets enables a
training process of neural networks.
more comprehensive evaluation across different data
environmentsone standardized and widely used in academic
For the time-series components in the proprietary
research, the other representative of real-world financial
dataset, sequences were constructed by organizing customer
applications. Together, they provide a balanced and robust
behavior over sliding 6-month windows. Each customer
foundation for training, validating, and testing the hybrid
record was transformed into a sequence of behavioral
model.
vectors, allowing the LSTM layers in the hybrid model to
learn temporal dependencies. Sequences shorter than six
The UCI Credit Card Default Dataset consists of 30,000
months were excluded from LSTM training to maintain
instances with 24 features, capturing demographic and
sequence length uniformity. This step allowed us to
financial characteristics of Taiwanese credit card clients for
incorporate behavioral trends such as increasing payment
the year 2005. Key variables include age, sex, education,
delays or decreasing account balances.
marital status, payment history for the previous six months,
bill amounts, and payment amounts. The target variable is a
To prevent data leakage, all temporal variables were
binary flag indicating whether a client defaulted on their
carefully aligned to ensure that no future information was
payment in the next month. Despite being dated, this dataset
available at the point of prediction. Additionally, the dataset
remains a benchmark in credit risk prediction due to its
was randomly split into training (70%), validation (15%),
structured format and clean labeling.
and test sets (15%), stratified on the default flag to preserve
the class distribution. Class imbalancewhich is common in
The proprietary dataset, on the other hand, is larger and
credit default prediction taskswas addressed using Synthetic
more diverse, consisting of 45,000 customer records with 32
Minority Over-sampling Technique (SMOTE) applied only
features collected over a 24-month period. This dataset
to the training data, ensuring the model had sufficient
includes transaction-level behavior logs, such as ATM
exposure to default cases without biasing evaluation results.
withdrawals, mobile banking usage, credit utilization
patterns, monthly income, account balance fluctuations, and
Table 1: Dataset Overview
Dataset Instances Features Default Rate Time-Series Data Source Type
UCI Credit Card Default 30,000 24 22.1% No Public Benchmark
Financial Institution 45,000 32 18.7% Yes (6-month window) Proprietary Dataset
5. Model Architecture and Hybridization reliability of traditional econometric models. The hybrid
Strategy architecture integrates two key components: (1) a Long
Short-Term Memory (LSTM) network for modeling
In this study, we propose a hybrid AI model designed to
behavioral time-series data, and (2) a logistic regression
effectively combine the temporal learning capabilities of
layer that operates on structured, static econometric
deep neural networks with the interpretability and statistical
variables. The outputs from these two branches are
83

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025
concatenated and passed through a final sigmoid activation  the Adam optimizer. A learning rate scheduler was used to
to yield the probability of credit default. This architecture is  adjust the rate based on validation loss. Early stopping based
designed  to  achieve  both  high  predictive  accuracy  and  on  validation  AUC  was  applied  to  prevent  overtraining.
explainable  outputs,  addressing  a  crucial  trade-off  in  Batch normalization and dropout layers (with a rate of 0.3)
financial machine learning applications.  were introduced after dense layers to stabilize learning.

The rationale for including LSTM layers is their proven
ability to capture long-term dependencies in sequential data.
| In  our  | context,  | behavioral  |     | features  | such  | as  | monthly  |     |     |     |     |     |     |     |
| -------- | --------- | ----------- | --- | --------- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
repayments, bill amounts, and credit utilization trends across
multiple time points form sequences that contain predictive
patterns related to emerging credit risk. Traditional models,
which aggregate or summarize these variables, often lose
temporal information. The LSTM model maintains a cell
state and memory gates that allow it to learn whether a
customer’s risk trajectory is improving or deteriorating over
| timecapabilities  |             | essential  | for           | dynamic  |            | credit      | scoring.  |     |     |     |     |     |     |     |
| ----------------- | ----------- | ---------- | ------------- | -------- | ---------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| Logistic          | regression  |            | is  employed  |          | to  model  | structured  |           |     |     |     |     |     |     |     |
econometric indicators such as income level, employment
| status,  | debt-to-income  |     | ratio,  | number  | of  | dependents,  | and  |     |     |     |     |     |     |     |
| -------- | --------------- | --- | ------- | ------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
education.

These features are generally not temporal in nature and
Fig 1: Proposed Hybrid Architecture
| provide     | valuable,          | interpretable  |     |           | information  | about  | a     |     |     |     |     |     |     |     |
| ----------- | ------------------ | -------------- | --- | --------- | ------------ | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
| customer’s  | creditworthiness.  |                |     | Logistic  | regression   | has    | long  |     |     |     |     |     |     |     |
This Figure 1, hybrid framework serves as a modular
| been  favored  |     | in  credit  | risk  | modeling  | due  | to  its  | ease  of  |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | ----- | --------- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
and extensible structure, allowing for the future inclusion of
| explanation,  | compliance  |     | with  | regulatory  |     | standards  | (e.g.,  |             |             |         |            |     |              |      |
| ------------- | ----------- | --- | ----- | ----------- | --- | ---------- | ------- | ----------- | ----------- | ------- | ---------- | --- | ------------ | ---- |
|               |             |     |       |             |     |            |         | additional  | components  | (e.g.,  | attention  |     | mechanisms,  | GRU  |
Basel II/III), and ability to provide odds ratios that make risk
layers, or external macroeconomic data streams). Its dual-
assessments transparent to both analysts and auditors. The
branch design not only improves predictive performance but
hybridization strategy involves parallel processing of the two
|     |     |     |     |     |     |     |     | also  enhances  | interpretability  |     |     | and  auditability  |     | crucial  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----------------- | --- | --- | ------------------ | --- | -------- |
input branches. The behavioral sequence is passed through  elements  for  deployment  in  regulated  financial
| one  or  | more  | LSTM  | layers,  | followed  | by  | a  dense  | (fully  |     |     |     |     |     |     |     |
| -------- | ----- | ----- | -------- | --------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
environments.
connected) layer that reduces the hidden representation into a

fixed-dimensional vector. Simultaneously, the static features  6. Performance Evaluation and Metrics
| are  passed  | directly  | into  | a   | logistic  | regression  | layer.  | The  |     |     |     |     |     |     |     |
| ------------ | --------- | ----- | --- | --------- | ----------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Evaluating the performance of a hybrid credit default
outputs of both models are concatenated and passed through
prediction model requires a rigorous, multi-metric approach
a final sigmoid-activated dense layer, which produces the
that accounts for both classification accuracy and the ability
final probability of default. This fused output leverages both
to generalize in imbalanced financial datasets. Given the
historical behavioral trends and static risk indicators.
|     |     |     |     |     |     |     |     | asymmetric  | cost  of  | misclassifying  |     | defaulters  | versus  | non- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --------------- | --- | ----------- | ------- | ---- |

|     |     |     |     |     |     |     |     | defaulters  | in  real-world  |     | applications,  |     | we  | adopt  a  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | --- | -------------- | --- | --- | --------- |
Equation 1: Hybrid Output Probability
|     |     |     |     |     |     |     |     | comprehensive  | suite  | of  | evaluation  | metrics  | that  | includes:  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | --- | ----------- | -------- | ----- | ---------- |
Accuracy, Precision, Recall, F1-score, and Area Under the

Where:  Receiver Operating Characteristic Curve (AUC-ROC). These
|     |     |     |     |     |     |     |     | metrics  | provide  complementary  |     |     | insights  | into  the  | model’s  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------------- | --- | --- | --------- | ---------- | -------- |
utility in both operational and risk-sensitive contexts.

|     |     |     |     |     |     |     |     | To        | begin  with,  | Accuracy         |     | offers            | a  straightforward  |               |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ---------------- | --- | ----------------- | ------------------- | ------------- |
|     |     |     |     |     |     |     |     | measure   | of  correct   | classifications  |     | over              | all                 | predictions.  |
|     |     |     |     |     |     |     |     | However,  | due  to       | the  inherent    |     | class  imbalance  |                     | in  credit    |

  default data where defaulters typically constitute less than
To  ensure  alignment  between  the  dimensions  of  the  25%  of  the  sample  accuracy  alone  can  be  misleading.
LSTM  and  logistic  regression  outputs,  both  branches  Therefore, we focus closely on Precision (the proportion of
undergo a dimensionality reduction step using dense layers  predicted defaulters who actually default) and Recall (the
before  concatenation.  This  ensures  efficient  training  and  proportion of actual defaulters correctly predicted), both of
avoids  overfitting  due  to  excessive  parameterization.  which capture the model's sensitivity and specificity in a
more nuanced way.
Additionally, we use dropout layers in the LSTM branch to
| prevent  | overfitting,  | and  | L2  | regularization  |     | in  the  | logistic  |     |     |     |     |     |     |     |
| -------- | ------------- | ---- | --- | --------------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
regression component to control coefficient magnitudes. The  The F1-score, being the harmonic mean of precision and
model was implemented using TensorFlow 2.x and trained  recall, is especially critical in scenarios where both false
using the binary cross-entropy loss function optimized with  positives and false negatives have financial implications. For
84

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025
instance, high false negatives (missed defaulters) can lead to  opportunities.  Hence,  a  high  F1-score  indicates  a  well-
unrecovered loans,  while high  false positives (incorrectly  balanced model capable of minimizing both risk types.
| flagged  | non-defaulters)  | may  | result  in  | missed  | lending  |     |     |     |     |     |
| -------- | ---------------- | ---- | ----------- | ------- | -------- | --- | --- | --- | --- | --- |

Table 2: Model Performance Comparison
|     |     | Model                |     | Accuracy  | Precision  | Recall  | F1-score  | AUC-ROC  |     |     |
| --- | --- | -------------------- | --- | --------- | ---------- | ------- | --------- | -------- | --- | --- |
|     |     | Logistic Regression  |     | 0.78      | 0.65       | 0.72    | 0.69      | 0.81     |     |     |
|     |     | LSTM Only            |     | 0.82      | 0.70       | 0.78    | 0.74      | 0.85     |     |     |
|     |     | Hybrid Model         |     | 0.87      | 0.76       | 0.85    | 0.80      | 0.91     |     |     |

Most importantly, evaluate the AUC-ROC, which plots  Table 2, the hybrid model consistently outperforms both
the true positive rate (Recall) against the false positive rate (1  the  standalone  logistic  regression  and  the  LSTM-only
-  Specificity)  at  various  threshold  settings. AUC-ROC  is  models across all key metrics. Notably, the hybrid model
particularly useful in credit scoring because it is threshold- achieves an F1-score of 0.80 and an AUC-ROC of 0.91,
independent and captures the model’s ability to rank risk  indicating  not  only  robust  classification  ability  but  also
levels across the entire population. An AUC of 1 indicates  superior ranking capability. These gains validate the synergy
perfect  classification,  while  0.5  corresponds  to  random  between the temporal sequence learning of LSTM and the
guessing. In this study, AUC-ROC serves as the primary  interpretable static feature modeling of logistic regression.
metric for model comparison.

Fig 2: ROC Curves for All Models

In Figure 2, the ROC curve of the hybrid model clearly  Lenders,  auditors,  and  regulators  require  transparency  to
dominates the others, with the greatest distance from the 45- ensure that credit decisions are fair, accountable, and free
degree diagonal line (random classifier). The hybrid model  from  discriminatory  biases.  To  address  this  need,  we
achieves consistently  higher true  positive rates across all  employed SHAP (SHapley Additive exPlanations)a state-of-
thresholds, making it especially suitable for deployment in  the-art method rooted in cooperative game theory to interpret
settings where risk-based pricing or threshold adjustments  the contributions of individual features in the hybrid model.
are required. To ensure the robustness of these results, we  SHAP assigns each feature an importance value representing
conducted 5-fold cross-validation and reported the average  its impact on the  model’s  output  for a given prediction,
metric values across folds. Variance in AUC-ROC and F1- allowing for both global and local interpretability.
| scores was below 1.5% across folds, indicating strong model  |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stability. We also validated the model on a hold-out test set  SHAP was applied separately to both components of the
representing 15% of the total data, stratified to maintain class  hybrid  model.  For  the  logistic  regression  branch,  SHAP
balance. Results on this test set closely mirrored validation  explanations  aligned  well  with  coefficient  magnitudes,
performance, confirming the generalizability of the model.  confirming the reliability of the linear model’s structure. For
|     |     |     |     |     |     | the LSTM component, SHAP values were computed using  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
7. Feature Importance and Explainability  Deep SHAP, an extension designed for deep learning models.
|          |         |             |                  |             |     | These  values  | captured  | complex  | interactions  | between  |
| -------- | ------- | ----------- | ---------------- | ----------- | --- | -------------- | --------- | -------- | ------------- | -------- |
| In  the  | domain  | of  credit  | risk  modeling,  | predictive  |     |                |           |          |               |          |
behavioral trends such as increasing monthly balances and
| performance  | alone  | is  insufficient  | model  | explainability  | is  |     |     |     |     |     |
| ------------ | ------ | ----------------- | ------ | --------------- | --- | --- | --- | --- | --- | --- |
equally critical, particularly in regulated financial sectors.
85

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025
delayed repaymentsand credit default risk, highlighting the  repayment delays from the LSTM component increased the
LSTM’s ability to detect non-linear patterns.  riskhighlighting  the  advantage  of  a  hybrid  model  that
|                                     |     |     |     |     |     |     | integrates both dimensions.  |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Equation 2: SHAP Value Computation  |     |     |     |     |     |     |                              |     |     |     |     |     |     |     |
To validate these findings, we conducted a correlation
|     |     |     |     |     |     |     | analysis  | between  | SHAP  | values  | and  | raw  | feature  | values,  |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----- | ------- | ---- | ---- | -------- | -------- |
confirming that the model’s learned behavior aligned with

Results indicated variables such as credit utilization, past
economic theory and domain knowledge. For instance, the
defaults, and income level were most predictive.  positive  correlation  between  utilization  rate  and  SHAP
  values matched expectations that higher credit usage implies
The global SHAP analysis revealed that a few econometric
higher risk.
| features  | consistently  | played  | dominant  | roles  | in  predicting  |     |     |     |     |     |     |     |     |     |
| --------- | ------------- | ------- | --------- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
credit default. These include:  8. Comparative Analysis and Visualization
|     |   Debt-to-Income  |     | Ratio  (DTI):  | High  | DTI  | values  |                                          |     |     |     |     |     |               |     |
| --- | ------------------ | --- | -------------- | ----- | ---- | ------- | ---------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- |
|     |                    |     |                |       |      |         | To critically assess the performance of  |     |     |     |     |     | the proposed  |     |
significantly increased default probability.  hybrid AI model in contrast to traditional and standalone
|     |   Past  Delinquency  |     | Events:  | A  strong  | positive  |     |     |     |     |     |     |     |     |     |
| --- | --------------------- | --- | -------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
machine learning approaches, we conducted a comparative
association with default, confirming prior literature.
analysis across three key models: (1) Logistic Regression,
  Credit Utilization Rate: Borrowers with utilization  (2)  LSTM-only,  and  (3)  the  Hybrid  LSTM  +  Logistic
|     | above  80%  | were  | substantially  | more  | likely  | to  |     |     |     |     |     |     |     |     |
| --- | ----------- | ----- | -------------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Regression model. This comparative evaluation is essential
default.
to quantify the added value of hybridization, not only in
  Income  Level:  Lower  income  segments  showed  numerical  performance  metrics  but  also  in  terms  of
elevated SHAP values for default risk.  classification behavior across various thresholds.
|     |   Age:  Younger  |     | borrowers  | contributed  | more  | to  |     |     |     |     |     |     |     |     |
| --- | ----------------- | --- | ---------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
predicted  defaults,  consistent  with  industry  Equation 3: AUC Calculation
expectations.

ROC and AUC clearly favor the hybrid approach, especially
in high-recall zones.

All three models were trained on the same datasets,
|     |     |     |     |     |     |     | using  identical  |      | train-validation-test  |             |     | splits,  | preprocessing  |            |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---- | ---------------------- | ----------- | --- | -------- | -------------- | ---------- |
|     |     |     |     |     |     |     | pipelines,        | and  | evaluation             | protocols.  |     | Metrics  |                | including  |
accuracy, precision, recall, F1-score, and AUC-ROC were
|     |     |     |     |     |     |     | computed  | to  | offer  a  | multidimensional  |     |     | view  | of  model  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ----------------- | --- | --- | ----- | ---------- |
effectiveness. However, the most insightful comparative tool
|     |     |     |     |     |     |     | for  imbalanced  |     | binary  | classification  |     | problems  | like  | credit  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | --------------- | --- | --------- | ----- | ------- |
default prediction is the Receiver Operating Characteristic
|     |     |     |     |     |     |     | (ROC)       | curve,       | which  | allows  | for  | visual    | comparison  | of        |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | ------ | ------- | ---- | --------- | ----------- | --------- |
|     |     |     |     |     |     |     | classifier  | performance  |        | across  | all  | possible  |             | decision  |
thresholds.

Fig 3: SHAP Summary Plot for Econometric Features  Figure 4 shows the ROC curves for each model on the
  test set. The curve corresponding to the Hybrid model lies
Figure 3 shows the distribution of feature impacts on the  clearly above those of the Logistic Regression and LSTM-
model’s output. Each point represents a SHAP value for a  only  models, reflecting a  superior trade-off between true
positive rate (TPR) and false positive rate (FPR). The Area
feature in an individual prediction. Red points denote high
feature values, while blue points indicate low values. For  Under the Curve (AUC) values further corroborate this: 0.91
example, the DTI feature shows a clear gradient: high DTI  for the Hybrid model, 0.85 for the LSTM, and 0.81 for
(in red) corresponds to high SHAP values, increasing the  Logistic Regression. These results confirm that the hybrid
likelihood of default. This visualization aids in understanding  approach delivers enhanced discriminatory power and more
feature effects across the population, not just for individual  reliable risk ranking.
| predictions.   |     |     |     |     |     |     |             |      |                 |     |        |       |              |     |
| -------------- | --- | --- | --- | --- | --- | --- | ----------- | ---- | --------------- | --- | ------ | ----- | ------------ | --- |
|                |     |     |     |     |     |     | The  curve  | for  | the  LSTM-only  |     | model  | also  | outperforms  |     |

Furthermore,  we  explored  individual  prediction  logistic  regression  across  most  thresholds,  indicating  its
explanations using SHAP force plots to visualize how each  strength in capturing behavioral patterns in time-series data.
However, it falls short of the hybrid model, particularly in
feature pushed the model output toward or away from the
decision threshold. In one representative case, a borrower  low  FPR  regions,  which  are  critical  in  financial  settings
with high income and moderate utilization but a recent late  where false positives (i.e., denying credit to a creditworthy
payment  showed  a  nuanced  risk  profile:  static  features  customer)  must  be  minimized.  This  highlights  a  key
lowered the default probability, but the temporal trend in  advantage  of  the  hybrid  approachit  retains  the  temporal
86

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025
sensitivity  of  LSTM  while  incorporating  the  economic  anchoring  predictions  in  interpretable,  domain-grounded
rationale and calibration of logistic regression, resulting in  features via logistic regression.
| more balanced performance.  |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
9. Discussion, Limitations, and Future Work
9.1. Discussion
|     |     |     |     |     | This      | study     | demonstrates  |             | the  efficacy  |           | of  a  | hybrid  |
| --- | --- | --- | --- | --- | --------- | --------- | ------------- | ----------- | -------------- | --------- | ------ | ------- |
|     |     |     |     |     | modeling  | approach  | that          | integrates  | deep           | learning  |        | (LSTM)  |
with traditional econometric techniques (logistic regression)
|     |     |     |     |     | for  the  purpose  |     | of  predicting  |     | credit  | default.  | The  | hybrid  |
| --- | --- | --- | --- | --- | ------------------ | --- | --------------- | --- | ------- | --------- | ---- | ------- |
model outperformed both standalone models in all major
|     |     |     |     |     | performance         | metrics,  | particularly    |       | in          | AUC-ROC     | and        | F1-    |
| --- | --- | --- | --- | --- | ------------------- | --------- | --------------- | ----- | ----------- | ----------- | ---------- | ------ |
|     |     |     |     |     | score,  suggesting  |           | it  not         | only  | identifies  | defaulters  |            | more   |
|     |     |     |     |     | accurately          | but       | also  balances  |       | false       | positives   | and        | false  |
|     |     |     |     |     | negatives           | more      | effectively.    | This  | balance     | is          | essential  | for    |
financial institutions aiming to maximize profitability while
maintaining regulatory compliance and operational fairness.

The strength of the hybrid model lies in its ability to
capture both temporal and static risk signals. The LSTM
|     |     |     |     |     | component  | effectively  | processes  |     | behavioral  |     | trendssuch  | as  |
| --- | --- | --- | --- | --- | ---------- | ------------ | ---------- | --- | ----------- | --- | ----------- | --- |
rising credit utilization or erratic payment behaviorover time,
which are early indicators of deteriorating creditworthiness.
|     |     |     |     |     | The  logistic  | regression  |                 | component,  |                   | meanwhile,  | provides   |          |
| --- | --- | --- | --- | --- | -------------- | ----------- | --------------- | ----------- | ----------------- | ----------- | ---------- | -------- |
|     |     |     |     |     | interpretable  | outputs     | based           | on          | well-established  |             | financial  |          |
|     |     |     |     |     | indicators     | like        | debt-to-income  |             | ratio,            | credit      | history,   | and      |
|     |     |     |     |     | income         | level.      | By  merging     |             | these             | insights    | in  a      | single   |
|     |     |     |     |     | architecture,  | the         | hybrid          | model       |                   | provides    | a          | richer,  |
multidimensional understanding of credit risk.
|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig 4: Data Flow through Each Model
|     |     |     |     |     | The  | use  of  | SHAP  | (SHapley  | Additive  |     | exPlanations)  |     |
| --- | --- | --- | --- | --- | ---- | -------- | ----- | --------- | --------- | --- | -------------- | --- |

values further enhances the model’s interpretability. SHAP
Further analysis shows that the hybrid model maintains
analyses confirmed that key features like past delinquencies,
a higher TPR without a significant increase in FPR, making
utilization rate, and income had consistent and theoretically
it suitable for credit risk environments where high recall
sound impacts on default predictions. This interpretability is
(catching true defaulters) is critical, but false alarms must
vital in regulated domains, where model decisions must be
| still  be  | controlled.  | For  | example,  at  a  decision  | threshold  |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ---- | -------------------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
yielding a TPR of 85%, the hybrid model records an FPR of  explainable to regulators, auditors, and consumers. Thus, the
|     |     |     |     |     | hybrid  model  |     | does  not  | compromise  |     | transparency  |     | for  |
| --- | --- | --- | --- | --- | -------------- | --- | ---------- | ----------- | --- | ------------- | --- | ---- |
only 15%, compared to 23% for the LSTM-only model and
|                                                               |           |              |                   |           | performance    | a   | common  | trade-off  |     | in  deep  |     | learning  |
| ------------------------------------------------------------- | --------- | ------------ | ----------------- | --------- | -------------- | --- | ------- | ---------- | --- | --------- | --- | --------- |
| 29%  for                                                      | logistic  | regression.  | This  efficiency  | directly  |                |     |         |            |     |           |     |           |
| translates into lower credit losses and better risk-adjusted  |           |              |                   |           | applications.  |     |         |            |     |           |     |           |

lending decisions.
9.2. Limitations

|     |     |     |     |     | Despite  | the  | promising  |     | results,  | several  | limitations  |     |
| --- | --- | --- | --- | --- | -------- | ---- | ---------- | --- | --------- | -------- | ------------ | --- |
We also visualized Precision-Recall (PR) curves, which
warrant discussion. The generalizability of the model may be
are more informative for imbalanced datasets. The hybrid
constrained by the characteristics of the datasets used. The
model again showed dominance with the highest area under
UCI dataset, while popular, is based on credit data from
the PR curve, affirming that its predictive power is not an
artifact of majority class learning, but rather a genuine ability  Taiwanese consumers in 2005, and the proprietary dataset,
|     |     |     |     |     | although  | more  | recent,  | reflects  | the  | credit  | practices  | and  |
| --- | --- | --- | --- | --- | --------- | ----- | -------- | --------- | ---- | ------- | ---------- | ---- |
to discriminate minority class events (defaults). Additionally,
demographic structure of a single financial institution. As a
we used calibration plots to assess the reliability of predicted
probabilities.  The  hybrid  model  exhibited  near-perfect  result, the model’s performance may vary when applied to
different populations, geographies, or lending environments.
calibration, while the LSTM showed signs of overconfidence

and logistic regression tended to underestimate risk at higher
|     |     |     |     |     | Next  | LSTM  | networks  | are  | powerful  |     | for  sequence  |     |
| --- | --- | --- | --- | --- | ----- | ----- | --------- | ---- | --------- | --- | -------------- | --- |
score bands.
|     |     |     |     |     | modeling;  | they  | are  also  | computationally  |     |     | intensive  | and  |
| --- | --- | --- | --- | --- | ---------- | ----- | ---------- | ---------------- | --- | --- | ---------- | ---- |

|     |     |     |     |     | require  | significant  | tuning.  | This  | increases  |     | deployment  |     |
| --- | --- | --- | --- | --- | -------- | ------------ | -------- | ----- | ---------- | --- | ----------- | --- |
The comparative visualizations thus reinforce both the
complexity, especially in low-latency environments such as
| quantitative  | superiority  | and  | qualitative  robustness  | of  the  |     |     |     |     |     |     |     |     |
| ------------- | ------------ | ---- | ------------------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
hybrid  architecture.  The  ROC  and  PR  curves  provide  real-time credit scoring. Additionally, LSTM’s internal states
and gate mechanisms remain opaque despite SHAP post-hoc
intuitive evidence that the hybrid model is better at managing
explanations, limiting the full interpretability of the temporal
the risk-reward trade-offs essential in credit decision-making.
| It adapts to behavioral trends through LSTM layers while  |     |     |     |     | component.  |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |

87

Santhosh Kumar Sagar Nagaraj / IJERET, 6(2), 81-88, 2025
Another challenge is data availability and quality. The Finance: A Literature Review. Risks 2021, 9, 192.
hybrid model assumes access to high-frequency behavioral https://doi.org/10.3390/risks9110192
data (e.g., monthly repayment patterns), which may not be [8] Longyue Liang. et al. 2020. Forecasting peer-to-peer
consistently recorded or standardized across all institutions. platform default rate with LSTM neural network.
Moreover, synthetic balancing techniques like SMOTE, used Electronic Commerce Research and Applications.
to address class imbalance, may introduce bias or inflate Volume 43, September–October 2020, 100997.
model confidence if not carefully validated. https://doi.org/10.1016/j.elerap.2020.100997
[9] Ala’raj, M., & Abbod, M. (2016). A new hybrid
9.3. Future Work ensemble credit scoring model based on classifiers
Several directions for future research emerge from this consensus system approach. Expert Systems with
study. First, there is significant potential in incorporating Applications, 64, 36–55.
macroeconomic variables and external data streams such as [10] Bo-Wen Chi. et la. 2012. A hybrid approach to integrate
interest rates, unemployment levels, or consumer sentiment genetic algorithm into dual scoring model in enhancing
indicesinto the hybrid framework. These could be fed into a the performance of credit scoring model. Expert
third model branch or dynamically interact with existing Systems with Applications. Volume 39, Issue 3, 15
inputs to better reflect changing economic conditions that February 2012, Pages 2650-2661.
affect default risk. Next, the hybrid model can be extended https://doi.org/10.1016/j.eswa.2011.08.120
with attention mechanisms or transformer-based [11] Bo-Wen Chi and Chiun-Chieh Hsu. 2012. A hybrid
architectures in place of or alongside LSTM. These modern approach to integrate genetic algorithm into dual scoring
neural architectures have shown superior performance in model in enhancing the performance of credit scoring
other sequence learning tasks by better capturing long-range model. Expert Syst. Appl. 39, 3 (February, 2012), 2650–
dependencies and allowing the model to focus on the most 2661. https://doi.org/10.1016/j.eswa.2011.08.120
relevant time steps. Third, future work should consider [12] https://bura.brunel.ac.uk/bitstream/2438/17809/2/FullTe
multi-class or survival analysis frameworks to predict not xt.pdf
just whether a default will occur, but when it is likely to
happen. This temporal dimension would be particularly
valuable in managing portfolio risk and setting dynamic
interest rates.
From a deployment perspective, efforts should also be
directed toward model compression, explainable AI (XAI)
dashboards, and real-time scoring systems, enabling
integration into production environments. Ensuring fairness,
transparency, and compliance with data privacy regulations
(e.g., GDPR, CCPA) will also be critical for large-scale
adoption.
References
[1] Altman, E. (1968). Financial ratios, discriminant
analysis and the prediction of corporate bankruptcy. The
Journal of Finance, 23(4), 589–609.
[2] Thomas, L. C., Edelman, D. B., & Crook, J. N. (2002).
Credit Scoring and Its Applications. SIAM.
[3] Tian, S., Yu, Y., & Gu, D. (2015). Variable selection and
corporate bankruptcy forecasts. Computational
Economics, 45(1), 41–62.
[4] Yeh, I. C., & Lien, C. H. (2009). The comparisons of
data mining techniques for the predictive accuracy of
probability of default of credit card clients. Expert
Systems with Applications, 36(2), 2473–2480.
[5] Lessmann, S., Baesens, B., Seow, H. V., & Thomas, L.
C. (2015). Benchmarking state-of-the-art classification
algorithms for credit scoring. European Journal of
Operational Research, 247(1), 124–136.
[6] Brown, I., & Mues, C. (2012). An experimental
comparison of classification algorithms for imbalanced
credit scoring data sets. Expert Systems with
Applications, 39(3), 3446–3453.
[7] Kumar, A.; Sharma, S.; Mahdavi, M. Machine Learning
(ML) Technologies for Digital Credit Scoring in Rural
88