---
conversion_metadata:
  converted_at: "2026-07-21T09:27:45Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Yachamaneni et al.pdf"
  source_pdf_sha256: "bfec3ab38b34c71bcf07e2f753882bec39cede906f67345220df57bd5a2f7eb0"
  page_count: 10
  markdown_char_count: 88119
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of Artificial Intelligence, Data Science, and Machine Learning 
Grace Horizon Publication | Volume 6, Issue 1, 164 -173, 2025

ISSN: 3050-9262 | https://doi.org/10.63282/3050-9262.IJAIDSML-V6I1P118

Original Article

Credit Card Customer Profiling Using Self-Supervised 
Representation Learning on Multi-Source Financial Data

Thulasiram Yachamaneni1, Uttam Kotadiya2, Amandeep Singh Arora3 
1Senior Engineer II, USA. 
2Software Engineer II, USA. 
3Senior Engineer I, USA.

Received On: 14/12/2024       Revised On: 24/12/2024         Accepted On: 15/01/2024        Published On: 02/02/2025

Abstract  -  The  recent  improvement  of  machine  learning  and  data  integration  has  marked  new  heights  in  financial 
analytics. A major area here that has become very popular is credit card customer profiling, which aims to identify 
and classify  the  behavior,  preferences  and  risks of  the customer.  Traditional  methods  depend  largely  on  supervised 
learning,  which  has  to  be  based  on  large  labeled  data  points.  Nonetheless,  since  the  emergence  of  Self-Supervised 
Learning  (SSL),  it  is  possible  to  derive  meaningful  representations  by  selecting  unlabeled  and  heterogeneous  data 
sources.  This  paper  presents  an  original  scheme  for  credit  card  customer  profiling  based  on  self-supervised 
representation learning and financial data from multiple sources. The transaction records, customer demographics, 
online banking activity and credit scores are brought together through a single analytical model. The method builds 
into contrastive learning and transformer-based architectures to learn feature embeddings that are robust. We show 
high-quality  profiling,  clustering,  and  downstream  tasks  like  creditworthiness  assessment  problems  and  churn 
prediction on a real-world financial dataset that was collected prior to February 2025 and made up a significant bulk 
of  our  experiments,  stating  that  our  framework  essentially  outperforms  baselines  in  terms  of  profiling  accuracy, 
clustering  performance,  and  downstream  tasks  accurately.  We  elaborate  on  the  comparisons  of  performance  to 
standard  models,  the  advantages  of  multiple-source  merging,  as  well  as  what  this  could  mean  to  the  individual 
tailored  financial  services.  We  have  also  added  thorough  visualization,  flowcharts  and  ablation  studies  to 
complement our findings.

Keywords - Self- Supervised Learning, Multi-Source Data Integration, Representation Learning, Financial Analytics, 
Customer Segmentation, Contrastive Learning, Deep Learning, Churn Prediction.

1. Introduction

Figure 1: Credit Card Fraud Detection System Using ML-Based Scoring Engine

Profiling of customers forms an imperative base activity 
within  the  credit  card  sector  and  helps  facilitate  most  of  its 
imperative  basis  operations  like  risk  evaluation,  one-on-one 
relations 
fraud  prevention  and  customer 
marketing,

management.  [1-4]  Proper  and 
live  profiling  enables 
financial institutions to know the behavior of the customers, 
predict 
risks. 
their  needs,  and  overcome  perceived 
Conventionally,  the  process  has relied  strongly  on  manually

---

<!-- PAGE 2 -->

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025

is

then

information.  The  former

engineered features of demographic, transactional, and credit 
history 
into 
supervised machine learning algorithms to help forecast how 
creditworthy one is or whether one is likely to churn. These 
methods,  although  efficient  in  other  scenarios,  have  a 
number  of  drawbacks,  especially  the  lack  of  sufficient 
amounts of labeled data, which are generally not available or 
quite costly and sensitive by nature.

thrown

Labeling  of  the  financial  data  also  comes  with  its 
privacy  implications  since,  in  some  cases;  it  might  involve 
information  or  even 
identifiable 
access

to  personally

1.1. Emergence of Self-Supervised Learning (SSL)

indicators  of  customer  behavior,  which  customers  might 
regard as personal. In addition, it is known that static feature 
engineering commonly fails to acquire more complicated and 
non-linear  patterns  and  time-related  trends  in  consumer 
behaviour.  With  financial  systems  becoming  increasingly 
digitalised and data-abundant, there is an emerging need for 
more  scalable,  flexible,  and  privacy-friendly  methods  of 
customer  profiling 
the  richness  of 
that  can  extract 
information from multiple-source data without being limited 
by the presence or absence of labels.

Definition and Core Principles

Other Domain Success

Applicability to Financial Data

Benefits of Using It in Place of Conventional Methods

Raising Research and Industry Profession

Figure 2: Emergence of Self-Supervised Learning (SSL)

  Definition  and  Core  Principles:  Self-Supervised 
Learning  (SSL)  is  a  field  in  machine  learning  in 
which  models  are  trained  to  learn  meaningful 
representations  of  unlabeled  training  data  through 
solving  auxiliary  or  alternate  (pretext)  tasks.  It 
differs  from  supervised  learning,  which  requires 
costly  and  sometimes  rarely  available  labeled  data 
and instead uses unlabeled data best parts to assign 
pseudo-labels  based  on  the  inherent  data  structure. 
For  example,  Predicting  missing  values,  reordering 
sequences,  or  finding  augmented  variants  of  the 
same  input  are  tasks  that  can  guide  the  model  to 
learn  meaningful  patterns  without  requiring  human 
annotation.  Such  representations  can,  in  turn,  be 
used  in  downstream  tasks  such  as  classification  or 
clustering.

  Other  Domain  Success:  SSL  has  been  attracting 
much attention in such areas as computer vision and 
Natural Language Processing (NLP). Measurements 
Contrastive 
already 
performed as well as or even better than supervised 
models  on  general  benchmarks  in  vision.  Pre-
trained Transformers In NLP practice, Transformer-
based models are pre-trained on large corpora using 
and  next-sentence 
masked

learning  methods  have

token  prediction

165

tasks.  These

prediction, achieving new state-of-the-art results on 
multiple 
have 
demonstrated that SSL can reveal deep and general 
benefits 
high-dimensional 
in 
information.

achievements

complex

and

  Applicability to Financial Data: The popularity of 
the SSL has increased in other spheres, but its use in 
customer  profiling in  the  financial  service  sector  is 
just coming of age. Financial data, which manifests 
in  multiple  modalities  (including  tabular  records, 
time  series,  and  behavioural  logs),  serves  as  a  rich 
environment for applying SSL. SSL can be applied 
to  learning  robust  representations  of  customers  by 
devising  and  matching  suitable  pretext  tasks  (e.g., 
masked  transaction  prediction,  temporal  shuffling, 
and behavioral similarity detection) and the required 
spending  habits,  risk  indicators,  and  engagement 
profiles  can  be  learned  in  an  entirely  unsupervised 
way without relying on manual labels or search. 
  Benefits  of  Using  It  in  Place  of  Conventional 
Methods:  Compared  to  the  traditional  supervised 
and  unsupervised  learning  techniques,  SSL  has  a 
number of advantages. It alleviates the need to have 
labeled  data,  and  the  financial  institutions  can 
therefore use the humongous quantities of unlabeled

---

<!-- PAGE 3 -->

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025

historical  reports.  It  also  facilitates  representation 
learning,  in  which the model  itself  acquires  feature 
hierarchies  which  are  frequently  superior  to  hand-
designed features. Moreover, being more flexible in 
adapting  to  new  or  changing  trends  in  customer 
behaviour  patterns,  SSL  is  more  appropriate  in  a 
dynamic environment such as the financial sector. 
  Raising  Research  and  Industry  Profession: 
Research into the use of SSL with tabular and time-
series  data,  including  financial  transactions,  is

1.2. Challenges in Traditional Approaches

developing. Early industry adoption has come along 
with  academic  interest  as  the  financial  industry 
experiments  with  SSL  to  better  spot  fraud,  credit 
scoring,  and  churn  prediction  on  financial  product 
consumers.  Due  to  its  scalability  and  labelling 
efficiency,  SSL  is  one  of  the  potential  paths  for 
future  financial  machine-learning  systems  as  the 
demand  for  privacy  increases  and  data  volumes 
expand exponentially.

Constraints to Data 
Labeling

Isolated Data Sources

Limited Generalization

Figure 3: Challenges in Traditional Approaches



issue  of

finances.  Tagging  of

  Constraints  to  Data  Labeling:  The  need  to  use 
labeled data is one of the most prominent obstacles 
to  traditional  supervised  learning  when  applied  to 
the 
financial 
information-  e.g.  detecting  high-risk  customers  or 
detecting a fraudulent transaction is a job that needs 
much  domain  knowledge,  as  well  as  access  to 
sensitive information. Not only does this render the 
process  time-consuming  and  costly,  but  it  also 
raises  considerable  privacy  concerns,  given  that 
regulatory  pressure  is  on  the  rise  to  adhere  to 
standards such as GDPR and CCPA. The effect of it 
is  that  much  potentially  useful  data  is  either  not 
labeled  or  makes  use  of  only  a  few  labels,  so 
conventional modeling approaches are limited. 
Isolated  Data  Sources:  Customer  data  is  often 
managed in multiple, disconnected systems at most 
financial institutions. Data silos are inevitable, with 
transactional  logs,  demographic  data,  credit  data 
and  web  interactions  typically  stored  in  individual 
databases  or 
separate  business  units.  This 
disintegration  interferes  with  the  formation  of  an 
all-rounded  customer  profile  and  denies  models  a 
chance to  make  use  of  the  entire range  of  behavior 
and  contextual 
is 
difficult  to  merge  and  preprocess  these  wildly 
different  data  sources;  not  only  is  it  technically 
is  also  constrained  by 
challenging,  but 
organizational rules and compliance regulations. 
  Limited  Generalization:  Labeled  data  models, 
whether handled by a supervisor, require supervised 
learning  and  tend  to  overfit  to  the  training  dataset 
distribution  (depending  on  variables,  segments, 
geographies and timeframes), and lack the ability to 
generalize further. The behavior of financial entities 
on  macroeconomic 
is 
phenomena,  policy  changes,  or  personal  factors- 
which  creates  discrepancies  in  what  is  called  data 
drift which, in turn, non-learned models will not be

indications.  Technically,

depending

variable

it

it

time  without  constant

able to adjust to. These models become irrelevant in 
retraining  or 
a  short 
adaptation  to  a  domain.  This  inflexibility  impairs 
the use of a traditional approach in flexible or data-
deficient settings.

2. Literature Survey 
2.1. Traditional Customer Profiling Techniques

Conventional  techniques  of  customer  profiling  have 
been  using  algorithms  like  K-Means  and  the  Gaussian 
Mixture  Model  of  clustering.  [5-8]  These  techniques  are 
generally  applied 
in 
to  hand-crafted 
transaction  data and  demographic  data, i.e. age,  income  and 
spending  patterns.  As  an  example,  the  K-Means  algorithm 
divides  the  customers  into  specific  groups  based  on  the 
similarity  of  their  features  but  takes  the  linear  separability 
assumption,  which  restricts 
the  representation  of  any 
complex pattern in the high-dimension data.

features  mined

The  Decision  Trees  were  quite  popular,  using 
characteristics  such  as  credit  score  and the  mean  amount  of 
transactions  to  classify  the  customer  profiles.  Nonetheless, 
such  models  tend  to  overfit,  especially  when  over-fitted 
small  or  noisy  data  is  used.  These  traditional  methods, 
despite being simple and interpretable, cannot understand the 
complexity  and  dynamism  of  contemporary  customer 
behaviour very well.

2.2. Finance Finance Supervised Machine Learning

As  more  labeled  financial  data  becomes  available, 
supervised machine learning models are starting to see wider 
application  in  fraud  detection,  customer  segmentation,  and 
credit  scores.  Random  Forests,  XGBoost,  and  Neural 
Networks  algorithms  have  proven  to  have  great  predictive 
abilities,  as  they  learn  complex,  non-linear  patterns  from 
large  datasets.  These  models  enjoy  the  richness  of  features 
and  may  accept  a  wide  range  of  input  classes,  and  yet  they 
are  very  sensitive  to  the  availability  and  quality  of  labeled 
data.  Moreover,  they  are  especially  prone  to  problems  such

166

---

<!-- PAGE 4 -->

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025

as  class  imbalance,  which  frequently  occurs  in  financial 
realms,  e.g.,  a  few  fraudulent  transactions  make  up  a 
negligible  proportion  of  the  data.  This  sensitivity  usually 
demands  employing  data  augmentation  methods  or  loss 
functions in the production of sturdy performance.

2.3. Development of self-supervised methods

Self-Supervised  Learning  (SSL)  has  become  a  strong 
paradigm,  particularly  in  fields  where  costly  or  limited 
labeled  data  is  available.  Methods  like  contrastive  learning- 
Contrastive methods have proven to be hugely successful in 
the  field  of  computer  vision  by  learning  representations  via 
the comparison of augmented image pairs as seen via models 
like SimCLR and MoCo. Transformer-based models, such as 
BERT,  have  succeeded  in  transforming  natural  language 
processing  by  allowing  for  deep  contextual  interpretation  of 
unlabeled text.

These  advances  have  given  impetus  to  the  adoption  of 
SSL  to  structured data,  such as  tabulated  data, although  this 
is  a  growing  field.  Self-supervised  methods  have  started 
becoming  used  in  the  field  of  finance;  one  example  where 
transaction  anomaly  detection. 
they  are  applied

is

3. Methodology 
3.1. System Architecture

Nevertheless,  they  are  not  extensively  used  to  profile 
customers  on  a  wider  scale,  which  is  explained  partly  by 
technological  difficulties  in  adapting  such  models  to  multi-
modal and multi-source financial data.

2.4. Gaps identified

Although there are some breakthroughs both in the field 
of  machine learning  and deep  learning,  there is  still a  set  of 
gaps that are  yet  to  be  filled  in  applying  such  techniques  to 
customer  profiling in  finance. To  begin  with, little  seems  to 
have  been  done  about  the  application  of  self-supervised 
learning  to  heterogeneous  financial  data  that  consists  of 
transactional,  demographic,  and  behavioral  data.  Second, 
interpretability  remains  a  concern,  particularly  in  regulated 
industries  where  transparency  is  imperative,  such  as  the 
financial  sector.  Lastly, a  large part  of  existing models  does 
not  fully  utilise  the  temporal  and  contextual  cues  present  in 
customer  behaviour,  e.g.,  the  time  of  day  of  the  transaction 
or scenario. Filling such gaps offers  the prospect of creating 
stronger, interpretable and generalizable systems of customer 
profiling.

Figure 4: System Architecture

  Data  Preprocessing:  Cleaning  and  transformation 
of raw financial data into a structured form in which 
the data can be modeled occur at the first stage.  [9-
12] This involves dealing with missing data, scaling 
categorical 
continuation 
variables, 
attributes  as  well  as  synchronizing 
temporal 
information  in  various  modalities  like  transactions, 
demographics 
logs.  The 
preprocessing  ensures  data  consistency,  thereby 
quantifying 
learned 
quality 
representations.

behavioural

encoding

and

the

the

of

  Multi-Modal  Feature  Encoding:  The  system  uses 
separate  encoders  to  accommodate  its  modality  in 
order to  manage  the  variety  of  data  sources.  As  an 
example,  transactional  sequences  are  rolled  out  by 
temporal  encoders  and  static  demographic  features 
are  rolled  out  by  feedforward  layers.  The  encoders 
learn  to  map  the  raw  inputs  to  a  common  latent 
space,  retaining  modality-specific  information  and 
allowing joint learning.

  SSL Pretext Task Unit: The model is trained using 
Self-Supervised  Learning  (SSL)  module  and  does 
not require labeled  data.  The types  of  pretext  tasks

167

in

this  module

presented 
include  contrastive 
learning, masked feature reconstruction, or temporal 
order  prediction.  By  effectively  solving  such tasks, 
the  model  encodes 
interesting  patterns  and 
structures  within  the  data,  which  improves  the 
quality of the learned representations.

  Feature  Aggregation:  The  features  represented 
across  modalities  are  then  pooled  into  a  single 
unified  representation.  Information  is  integrated  in 
terms  of  relevance  using  such 
techniques  as 
attention  mechanisms  or  weighted  averaging.  Such 
a  step  is  required  to  explore  the  interdependence 
between  different  types  of  data,  which,  in  turn, 
results in a comprehensive picture of each customer 
profile.

  Downstream  Task  Heads:  The  aggregated 
representation  is  finally  fed  to  a  series  of  task-
specific  heads  with numerous  supervised  tasks  like 
the  segmentation  of  customers,  risk  scoring  or 
predicting  churn.  Heads  are  finetuned  by  labeled 
data and make use of all of the rich representations 
acquired  in  the  self-supervised  stage  to  achieve 
higher performance on specialized business tasks

---

<!-- PAGE 5 -->

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025

3.2. Data Sources

  Transaction  Logs:  Purchases  and

that

logs

financial 
operations  of  customers  are  stored  in  the  form  of 
transaction 
illustrate  a  chronological 
history  of  customer  transactions.  Some  of  the 
attributes that a given entry usually contains are the 
amount  of 
time  and  category  of 
spending.  This  is  time-series  information  in  nature 
per  se,  and  this  would  be  very  useful  in  giving 
critical information regarding the financial behavior

transaction,

of  a  customer,  the  character  of  spending,  and  so, 
anomalies which can occur with time.

  Demographics:

data

Demographic

are 
structured information that includes age, gender, 
and  the  level  of  income  of  customers.  In  tabular 
form, these features form the necessary features  for 
profiling  users  and  separating  them  according  to 
socioeconomic  significance. These  are also  used as 
bases  for  assessing  creditworthiness  and  targeting 
products.

Figure 5: Data Sources

  Credit  Bureau  Reports:  Credit  reports  show  the 
history  by  collectively  referring  to  a  customer 
where  his/her  credit 
score,  accounts,  credit 
repayment history and default are shown. This data 
is  typically  presented  in  the  form  of  a  table  and  is 
essential  in  determining  financial  risk.  It  is  usually 
employed  in  terms  of  loan  approval,  credit  score 
and fraud prevention.

  Web  Activity:  Data  on  web  activity  will  show  the 
customer  activity  on  the  digital  banking  platform, 
such as the number of logins, the number of clicks, 
the  number  of  views  per  session  and  clickstreams. 
This  time  series  data  gives  the  context  associated 
with  user  activity  and  online  behavior,  and  it 
presents  important  indications  of  how  to  further 
business  knowledge  can  be  built  to  do  behavior 
modeling,  churn  forecasting  and  personalization 
tactics.

3.3. Feature Engineering

Figure 6: Feature Engineering

  Numerical  Normalization:  Numerical  features  are 
normalised,  e.g.  through  min-max  scaling  and  z-
score  normalization,  to  enable  uniform  scale  and

168

intact.

enhance  model  convergence.  [13-16]  Min-max 
normalization  normalizes  the  features  to  the  fixed 
range  (for  instance,  0  to  1)  and  keeps  relative 
relationships 
z-score 
normalization  normalizes  the  features  by  centering 
and  scaling  around  the  mean  and  the  standard 
deviation.  This  measure  is  necessary,  especially  in 
sensitivity-to-feature 
algorithms 
(especially neural networks).

magnitude

contrast,

In

training

  Categorical Embeddings: Discrete variables, i.e., a 
customer  occupation  or  a  transaction  category,  are 
encoded as high-dimensional dense vectors (i.e., the 
so-called  embedding).  Model 
learns 
embeddings  instead  of  encoding  with  a  sparse, 
often 
inefficient 
accompanies  a  one-hot  implementation.  The  effect 
is  that this  technique  is  used  to  cause  the  model  to 
embrace 
categories 
independently,  and  the  performance  becomes  very 
good,  most  importantly,  when  the  variables  are 
high-cardinality ones.

encoding,  which

semantics

between

one-hot

transform

encodings

  Temporal  Encoding:  To represent the  time  aspect 
of sequential data, sinusoidal position encodings are 
the 
employed.  These 
timestamps  into  functions  that  enable  the  model  to 
learn  some  temporal  relationships  and  the  ordering 
of  the  sequences  by  mapping  each  timestamp  as  a 
continuous  periodically  called  parameter.  Modeled 
after transformer architectures, sinusoidal encodings 
can  help  the  model  discriminate  short-run  patterns 
and  long-run  patterns  on  the  time-series  data  and 
learn  more  about  the  transaction  history  or  that  of 
the web activities.

---

<!-- PAGE 6 -->

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025

3.4. Self-Supervised Learning Design 
3.4.1. Contrastive Learning Objective

The essence of contrastive learning is to teach the model 
to  make 
the  differentiation  between  comparable  and 
dissimilar  pieces  of  data  without  necessitating  reliance  on 
explicit images.  With  two  augmented  views  of  a  given  data 
instance, the goal is to maximise the cosine similarity of the 
representations  of  the  two  views  and  minimise  similarity 
with representations of other instances in the batch.

3.4.2. Pretext Tasks

The  logits  are  passed  through  a  temperature  parameter 
before  the  softmax  function  is  applied,  and  this  adjusts  the 
sharpness of the output distribution. This promotes the model 
to learn discriminating and powerful features by drawing the 
positive pairs nearer and exerting the negatives further apart 
in the embedding space.

Figure 7: Self-Supervised Learning Design

transaction data or weblogs. Its multi-head attention 
enables  different heads  to attend  to  various regions 
of the sequence, which learns complex and context-
sensitive  representations,  which  is  vital  in  learning 
the sequences of customer behavior.

  MLP  Head:  After  the  transformer  encoder,  the 
learned  features  are  refined  and  aggregated  with  a 
head called Multi-Layer Perceptron (MLP). It is one 
or  more  fully  connected  layers  that  use  non-linear 
activations 
high-dimensional 
normalise 
embeddings into task-specific representations). This 
part  conducts  downstream  work  like  risk  scoring, 
purchase prediction, or fraud detection and converts 
the  acquired  temporal  and  contextual  signals  into 
functioning results.

(to

  Clustering  Layer:  On  top  of  the  learned  feature 
representations, a clustering layer is applied in order 
to  generate  interpretable  customer  profiles.  This 
layer  segments  customers  with  similar  encoded 
behaviours  and  attributes  and  makes  use  of 
algorithms  like  K-Means  or  even  deep  clustering. 
The resulting clusters are representative of different 
groups of customers, and this can be used to market 
to  specific  groups,  provide  them  with  personal 
services, or risk stratification.

  Masked  Attribute  Forecasting: In  this task,  some 
of  the  attributes  or  features  in  the  input  data  are 
randomly occluded, and the model is supplied with 
the task of predicting the occluded values. This task 
is  motivated  by  the  BERT-style  training  since  they 
provide a contextual relationship among features to 
the  model,  enhancing  its  knowledge  of  underlying 
data  structures  and  dependency,  which  is  useful  in 
tabular and multi-modal data. 
  Time  Series  Forecasting:  The

involves 
randomly  permuting  a  sequence  of  events  (e.g., 
transaction records or web interactions) and training 
the  model  to  predict  the  correct  order.  It  helps  the 
model  capture 
time-related  dependencies  and 
tendencies  in  data  that  benefit  it,  especially  when 
interacting  with  time-series  or  sequential  data  sets 
in financial applications.

task

  AVP  -  Augmented  View  Prediction:  Here,  the 
same data point is augmented (e.g. by adding noise 
or  removal  of  features  or  random  permutations  of 
features, etc.) many times, and the model is trained 
to learn to identify or match these augmentations. In 
learning  to  identify  multiple  permutations  of  the 
same  underlying 
learns 
entity, 
invariances  with  respect  to  small  distortions  and 
noise,  thereby  enhancing  its  generalization  ability 
and robustness.

the  model

3.5. Model Architecture

  Transformer Encoder: The model has at its center 
a Transformer encoder with self-attention sequential 
data  processing.  The  encoder  extracts  temporal 
time-series  data,  such  as 
dependencies

from

169

---

<!-- PAGE 7 -->

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025

bottlenecks. The configuration was also enabled to do large-
scale  hyperparameter  tuning,  as  well  as  ablation  studies  to 
distinguish  the  effect  of  each  module.  On  the  whole,  the 
experimental  environment  met  the  requirements  of  both 
computational  and  real-world  feasibility  for  the  assessment 
that  aimed  to  create  a  solid  benchmarking  scenario  for  the 
proposed  self-supervised  learning  model  in  comparison  to 
classical machine learning approaches.

4.2. Metrics

A  wide  range  of  evaluation  metrics  was  used  to  assess 
the performance of the proposed system in a comprehensive 
way  in  both  unsupervised  and  supervised  learning  tasks.  In 
terms of clustering performance, two metrics commonly used 
were  the  Silhouette  Score  and  the  Davies-Bouldin  Index. 
Silhouette Score is a method that measures the unity among 
clusters  and  the  dissimilarity  of  the  cluster  by  contrasting 
intra-cluster mean distance and the mean distance to clusters' 
neighbouring points. A Greater Silhouette Score implies that 
data points are coupled to a cluster they belong at and do not 
go  fairly  coupled  to  other  clusters,  denoting  distinct  and 
isolated clusters.

As opposed to that, the Davies-Bouldin Index measures 
the average similarity of every cluster with its closest one by 
taking  into  account  the  intra-cluster  compactness  as  well  as 
the  inter-cluster  separation.  In  this  instance,  the  smaller  the 
number, the better the clustering is, as it indicates a low level 
of dispersion of each cluster and a large delineation between 
clusters. A combination of these measures provides a reliable 
in  segmenting 
indication  of 
the  model's  effectiveness 
supervised 
in 
customer  profiles.  The  performance 
classification  in  classification  problems,  specifically  credit 
risk  prediction  and  churn  classification,  was  determined  in 
terms  of  F1-Score,  AUC  (Area  Under 
the  Receiver 
Operating  Characteristic  Curve)  and  Accuracy.  F1-Score  is 
also handy in case of imbalanced responses since it produces 
a more  informative  statistic than  the accuracy  level  because 
it balances between precision and recall.

Precision  indicates  how  well  a  model  can  avoid  false 
positive  results,  and  recall  is  used  to  measure  how  well  a 
model  can  identify  the  true  positive  result,  which is  vital  in 
the sense of risk in a high-stakes financial model. AUC is a 
threshold-free  indicator  of  the  quality  of  ranking  of  the 
model in terms of how effectively a model separates classes 
at  every  possible  threshold.  Finally,  the  most  intuitive 
measure  is  called  Accuracy,  defined  as  the  quotient  of  the 
number of correctly predicted instances and the total number 
of predictions. Although it is an easy measure to understand, 
accuracy can be misguiding in distorted data, which is why it 
is complemented with the rest of the metrics. This is a multi-
metric  assessment  that  allows  a  balanced  analysis  of 
clustering and classification model qualities.

Figure 8: Model Architecture

4. Results and Discussion 
4.1. Experimental Setup

The experimental setup aimed to assess the performance 
of  the  proposed  self-supervised  learning  architecture  with 
large-scale real-world data of a financial nature. The sample 
consisted  of  100,000  records  of  customers  of  a  privately 
owned  banking  company,  where  data  was  collected  until 
February  2025.  It  was  multi-modal  data,  including  four 
sources  of  information:  transactional  logs,  demographics 
information, credit bureau records and traces of web activity. 
Transactional  data  gave  a  timeline  of  customer  spending 
behavior  in  terms  of  the  amount  spent,  the  time  of  the 
transaction and the category.

characteristics

(age,  gender

involved 
and

fixed 
 Demographic 
demographic  variables 
income). 
Information  in  credit  bureaus  provides  background  into  the 
financial  faithfulness  of  every  client,  such  as  their  credit 
ratings  and  credit  history  of  loan  repayment  and  liabilities. 
Activity  in  web-based  logs  retrieved  behavioral  patterns, 
namely  log-in  frequency,  click  trail  directions,  and  user 
activity  with  online  banks.  In  order to  have  rigorous  testing 
and avoid leaking of data, the given dataset was divided into 
80% as training, 10% as validation and 10% as testing.

This  stratification  allowed  one  to  fine-tune  the  model 
over the validation set and measure performance over the test 
set in an unbiased manner. The experimentation and training 
process  was  performed  in  a  high-performance  computing 
environment  that  consists  of  two  NVIDIA  A100  GPUs, 
capable  of  massively  parallel  computing,  and  512GB  of 
RAM  to  support  training  with  large  batches  and  memory-
intensive  operations.  That  hardware  allowed  the  system  to 
efficiently  train  complex  architectures,  like  transformer 
encoders  and  multi-modal  feature  aggregators,  without  any

170

---

<!-- PAGE 8 -->

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025

4.3. Quantitative Results

Method 
Baseline (K-Means) 
XGBoost 
Proposed SSL

Table 1: Quantitative Results

Silhouette  AUC (Credit Risk)  F1 (Churn Prediction)

0.35 
0.41 
0.56

0.71 
0.84 
0.91

0.58 
0.69 
0.81

1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0

4.4. Quantitative Results

Baseline (K-Means)

XGBoost

Proposed SSL

Silhouette

AUC (Credit Risk)

F1 (Churn
Prediction)

Figure 9: Graph representing Quantitative Results

only

considering

  Baseline (K-Means): K-Means was incorporated as 
a  control  clustering  algorithm  to  test  customer 
segmentation 
traditional 
unsupervised  learning.  It  obtained  a  Silhouette 
Score  of  0.35,  which  represents  fairly  weak  and 
overlapping measures. Given that K-Means lacks in 
terms of using temporal and contextual information, 
the  algorithm  also  fails  to  develop  clear  customer 
profiles.  Furthermore,  it  has  demonstrated  limited 
predictive capabilities, with an AUC of 0.71 and an 
F1-score  of  0.58  on  the  churn  prediction  task,  as 
well as an F1-score of 0.36 on credit risk, due to its 
simple and linear nature when its clusters were used 
as feature inputs to downstream tasks.

  XGBoost: Being a supervised learning algorithm on 
a  hyper-modern  level,  XGBoost  fared  much  better 
than  K-Means  in  classification  assignments.  It 
scored  an  AUC  of  0.84 and an  F1-score  of  0.69  in 
credit 
risk  assessment  and  churn  prediction, 
respectively,  representing  its  strength  in  processing 
tabular data and ability to fit non-linear interactions. 
However,  its  Silhouette  Score  of  0.41,  calculated 
based  on intermediary representations  generated  by 
the last layer, hints at moderate improvements in the 
quality  of  clustering  yet  projects  it  as  being 
backwards in terms of producing global, behaviour-
sensitive representations that more powerful models 
are capable of generating.

  Self-Supervised  Learning  (SSL):  The  SSL  model 
presented  outperformed  all  baselines  on  every  one 
of  the  metrics,  which  proves  the  worth  of  learning

through  multi-modal  signals  in  a  label-efficient 
way. Silhouette's Score was 0.56, which means that 
more  coherent  and  meaningful  customer  clusters 
were formed. The model performed incredibly well, 
with a very high AUC of 0.91 to predict credit risk 
and  a  remarkable  F1-score  of  0.81  to  determine 
churn. These findings make these results support the 
skill  of  the  model  to  learn  a  rich  generalizing 
representation  out  of  unlabeled  data  apriori  with 
pretext  tasks  and  temporal  encoding  that  beat  both 
clustering and supervised methods.

4.5. Ablation Study

To know the individual effect of the key elements of the 
proposed  self-supervised  learning  (SSL)  framework,  an 
ablation  study  was  carried  out.  The  study  can  provide 
information  on  the  relative  significance  of  each  element  of 
architecture  by  observing  the  effect  of  selective  removal  of 
each  module  at  a  time  on  the  corresponding  decrease  in  its 
credit  risk  prediction  performance  (measured  by  AUC). 
Table 2 contains a summary of the findings, which have been 
contained in detail below.

Table 2: Ablation Study Results 
Module Removed

AUC Drop

Temporal Encoding 
Web Activity 
Pretext Task

4.2% 
3.8% 
2.7%

171

---

<!-- PAGE 9 -->

4.50%

4.00%

3.50%

3.00%

2.50%

2.00%

1.50%

1.00%

0.50%

0.00%

4.20%

3.80%

2.70%

Temporal Encoding

Web Activity

Pretext Task

AUC Drop

Figure 10: Graph representing Ablation Study Results

  Temporal  Encoding:  The  removal  of  temporal 
encoding led to the greatest decline in performance, 
whereby 
the  AUC  slumped  by  4.2%.  This 
emphasizes the importance of the modeling of time-
varying  dynamics  of  customer  behavior.  The 
property of temporal encoding enables the model to 
be  sensitive  to  out-of-sequence  and  out-of-trend 
patterns,  i.e.,  a  history  of  sporadic  transactions, 
delayed  payments,  or 
in 
expenditure, which are highly correlated with credit 
risk.  In  its  absence,  the  model  can  no  longer 
contextualise  behaviours  across  time,  also  resulting 
in  more 
transient  representations  and  reduced 
predictive capability.

increases

recent

  Web Activity: Web activity features were removed 
and resulted in a 3.8% decrease in AUC; this meant 
the features provided significant information on the 
behavior  image  of  people  using  online  banking 
portals.  The  implicit  clues  of  user  engagement, 
financial  intents  and  reliance  on  digital  channels 
occur with metrics such as logins, session duration, 
and  sequence  of  clicks.  Although  these  signals  are 
frequently  under-exploited,  they  bring  significant 
value  to  the  table  when  they  are  combined  into  a 
multi-modal  model.  When  they  are  removed,  this 
impoverishes  the  input  behavior  and  limits  the 
model view of user intent.

  Pretext  Task:  The  overall  removal  of  the  pretext 
task module led to a 2.7 per cent decrease in AUC, 
emphasizing  the  significance  of  self-supervised 
goals  in  influencing  high-quality  representations  of 
features.  Pretext  games,  such  as  masked  attribute 
prediction  and  temporal  order  learning,  allow  for 
the  discovery  of  latent  patterns  and  associations  in 
the  data.  Whereas the  effect  is not as  significant as 
that  of  temporal  encoding  or  web  activity,  this 
the  models 
element 
generalizability  and  transferability  to  subsequent 
tasks.

is  crucial

improving

in

5. Conclusion

This  paper  reviews  the  use  of  a  Self-Supervised 
Learning  (SSL)  approach,  which  is  being  applied  to  profile 
customers  within  the  financial  industry,  specifically  credit 
card  users.  The  framework  suggested  was  based  on  using 
multi-source  data,  including  transaction  logs,  demographic 
information,  credit  bureau  reports,  and  web  activity, 
compiled  to  create  comprehensive  representations  of  the 
customers. With the help of contrastive learning and pretext 
tasks, including  masked attribute  prediction and recognising 
temporal  order, the  model  was  trained to  extract  underlying 
patterns  and  dependencies  both  over  time  and  across 
modalities without relying on labelled data. The outcomes of 
the  experiment  showed  that  the  proposed  SSL-based  model 
significantly  outperformed  classical  approaches,  such  as  K-
Means  and  XGBoost,  in  terms  of  clustering  quality,  credit 
risk  prediction,  and  churn  classification.  It  is  noteworthy 
that,  in  terms  of  Silhouette,  the  model  displayed  even  more 
excellent  results  in  both  unsupervised  and  supervised  tasks 
and performed well in F1 and AUC indicators. The ablation 
study  also  supported  the  fact  that  the  effectiveness  of  the 
model  owed  heavily  to  the  existence  of  parts  like  temporal 
encoding, behavior characteristics based on web activity, and 
self-supervised purposes

fraud

These  findings  have  tremendous  implications  for  the 
financial industry. Due to the greater accuracy and resilience 
of  customer  segmentation  and  risk  modeling,  financial 
institutions  move  on  to  work  more  intensively  on  credit 
scoring, 
lifecycle 
customer 
management.  Besides, 
the  detailed  representations  of 
features  acquired  with  the  help  of  SSL  can  provide 
personalized  product  suggestions,  adjustable  credit  limits, 
and real-time intervention plans. To the customer, this means 
more  customized  financial  products,  quicker  decision  times 
and more personalized online experiences.

detection,

and

With

customer 
expectations  changing,  the  capability  to  know  and  serve

competition  getting

fierce

and

172

---

<!-- PAGE 10 -->

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025

clients in a precise manner became a strategic capability. To 
anticipate,  a  number  of  directions  can  contribute  to  the 
strength of this research further. To begin with, the methods 
of  federated  learning  would  enable  the  training  of  models 
amid  remote  financial  institutions,  and  it  would  be  possible 
to  train  models  on  a  large  scale  without  compromising  the 
privacy  of  users  and  abiding  by 
regulatory 
requirements.  Second,  generalizability  might  be  enhanced, 
and a bigger scope of financial behavior might be covered by 
enlarging  the  model  to  a  cross-bank  consortium  dataset. 
Lastly,  the  inclusion  of  reinforcement  learning  may  allow 
personalization  techniques  to  be  adaptive,  such  that  offers, 
alerts,  or  risk  scores  may  be  changed  on  the  fly  based  on 
customer  reactions  or  actions.  All  combined,  these  future 
improvements  will  continue  to  advance  intelligent  financial 
services,  making  them  more  responsive,  secure,  and  user-
friendly.

their

References 
[1]  MacQueen,  J.  (1967,  January).  Some  methods  for 
classification  and  analysis  of  multivariate  observations. 
In  Proceedings  of  the  Fifth  Berkeley  Symposium  on 
Mathematical  Statistics  and  Probability,  Volume  1: 
Statistics (Vol. 5, pp. 281-298). University of California 
Press.

[2]  Reynolds,  D.  (2009).  Gaussian  mixture  models.  In 
Encyclopedia  of  Biometrics  (pp.  659-663).  Springer, 
Boston, MA.

[3]  Quinlan,  J.  R.  (1986).  Induction  of  decision  trees.

Machine learning, 1, 81-106.

[4]  Breiman,  L.  (2001).  Random  forests.  Machine learning,

45, 5-32.

sigkdd

[5]  Chen,  T.,  &  Guestrin,  C.  (2016,  August).  Xgboost:  A 
scalable  tree-boosting  system.  In  Proceedings  of  the 
22nd  ACM 
International  Conference  on 
Knowledge Discovery and Data Mining (pp. 785-794). 
[6]  Dal Pozzolo, A., Boracchi, G., Caelen, O., Alippi, C., & 
Bontempi,  G.  (2017).  Credit  card  fraud  detection: 
realistic  modeling  and  a  novel  learning  strategy.  IEEE 
transactions  on  neural  networks  and  learning  systems, 
29(8), 3784-3797.

[7]  He,  H.,  &  Garcia,  E.  A.  (2009).  Learning  from 
imbalanced  data.  IEEE  Transactions  on  knowledge  and 
data engineering, 21(9), 1263-1284.

[8]  Chen,  X.,  Fan,  H.,  Girshick,  R.,  &  He,  K.  (2020). 
contrastive

Improved  baselines  with  momentum 
learning. arXiv preprint arXiv:2003.04297.

[9]  Chen,  T.,  Kornblith,  S.,  Norouzi,  M.,  &  Hinton,  G. 
(2020,  November).  A  simple  framework  for  contrastive 
learning  of  visual  representations.  In  International

conference  on  machine 
PmLR.

learning  (pp.  1597-1607).

[10] Devlin,  J.,  Chang,  M.  W.,  Lee,  K.,  &  Toutanova,  K. 
(2019,  June).  Bert:  Pre-training  of  deep  bidirectional 
transformers for language understanding. In Proceedings 
of the 2019 conference of the North American chapter of 
the  Association  for  Computational  Linguistics:  human 
language technologies, volume 1 (long and short papers) 
(pp. 4171-4186).

[11] Somepalli, G., Goldblum, M., Schwarzschild, A., Bruss, 
C.  B.,  &  Goldstein,  T.  (2021).  Saint:  Improved  neural 
tabular  data  via  row  attention  and 
networks  for 
contrastive 
preprint 
arXiv:2106.01342.

pre-training.

arXiv

[12] Liu, X., Zhang, F., Hou, Z., Mian, L., Wang, Z., Zhang, 
learning: 
transactions  on

J.,  &  Tang,  J. 
Generative  or  contrastive. 
knowledge and data engineering, 35(1), 857-876.

(2021).  Self-supervised

IEEE

[13] Adewumi, A. O., & Akinyelu, A. A. (2017). A survey of 
machine-learning  and  nature-inspired  based  credit  card 
fraud  detection  techniques.  International  Journal  of 
System  Assurance  Engineering  and  Management,  8, 
937-953.

[14] Ileberi,  E.,  Sun,  Y.,  &  Wang,  Z.  (2021).  Performance 
evaluation  of  machine  learning  methods  for  credit  card 
fraud  detection  using  SMOTE  and  AdaBoost.  Ieee 
Access, 9, 165286-165294.

[15] Gui, J., Chen, T., Zhang, J., Cao, Q., Sun, Z., Luo, H., & 
Tao,  D.  (2024).  A  survey  on  self-supervised  learning: 
Algorithms,  applications,  and  future 
trends.  IEEE 
Transactions  on  Pattern  Analysis  and  Machine 
Intelligence.

[16] Ericsson, L., Gouk, H., Loy, C. C., & Hospedales, T. M. 
(2022). 
learning: 
Introduction,  advances,  and  challenges.  IEEE  Signal 
Processing Magazine, 39(3), 42-62.

Self-supervised

representation

[17] Dixon,  M.  F.,  Halperin,  I.,  &  Bilokon,  P.  (2020). 
Machine  learning  in  finance  (Vol.  1170).  New  York, 
NY, USA: Springer International Publishing.

[18] Lei,  X.,  Mohamad,  U.  H.,  Sarlan,  A.,  Shutaywi,  M., 
Daradkeh,  Y.  I.,  &  Mohammed,  H.  O.  (2022).  The 
development  of  an  intelligent  information  system  for 
financial  analysis  depends  on  supervised  machine 
learning 
Information  Processing  & 
Management, 59(5), 103036.

algorithms.

[19] Liu, Y., Jin, M., Pan, S., Zhou, C., Zheng, Y., Xia, F., & 
Yu,  P.  S.  (2022).  Graph  self-supervised  learning:  A 
survey.  IEEE  transactions  on  knowledge  and  data 
engineering, 35(6), 5879-5900.

[20] Garbarino,  S.,  &  Holland,  J.  (2009).  Quantitative  and 
qualitative methods in impact evaluation and measuring 
results.

173

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal of Artificial Intelligence, Data Science, and Machine Learning
Grace Horizon Publication | Volume 6, Issue 1, 164 -173, 2025
ISSN: 3050-9262 | https://doi.org/10.63282/3050-9262.IJAIDSML-V6I1P118
Original Article
Credit Card Customer Profiling Using Self-Supervised
Representation Learning on Multi-Source Financial Data
Thulasiram Yachamaneni1, Uttam Kotadiya2, Amandeep Singh Arora3
1Senior Engineer II, USA.
2Software Engineer II, USA.
3Senior Engineer I, USA.
Received On: 14/12/2024 Revised On: 24/12/2024 Accepted On: 15/01/2024 Published On: 02/02/2025
Abstract - The recent improvement of machine learning and data integration has marked new heights in financial
analytics. A major area here that has become very popular is credit card customer profiling, which aims to identify
and classify the behavior, preferences and risks of the customer. Traditional methods depend largely on supervised
learning, which has to be based on large labeled data points. Nonetheless, since the emergence of Self-Supervised
Learning (SSL), it is possible to derive meaningful representations by selecting unlabeled and heterogeneous data
sources. This paper presents an original scheme for credit card customer profiling based on self-supervised
representation learning and financial data from multiple sources. The transaction records, customer demographics,
online banking activity and credit scores are brought together through a single analytical model. The method builds
into contrastive learning and transformer-based architectures to learn feature embeddings that are robust. We show
high-quality profiling, clustering, and downstream tasks like creditworthiness assessment problems and churn
prediction on a real-world financial dataset that was collected prior to February 2025 and made up a significant bulk
of our experiments, stating that our framework essentially outperforms baselines in terms of profiling accuracy,
clustering performance, and downstream tasks accurately. We elaborate on the comparisons of performance to
standard models, the advantages of multiple-source merging, as well as what this could mean to the individual
tailored financial services. We have also added thorough visualization, flowcharts and ablation studies to
complement our findings.
Keywords - Self- Supervised Learning, Multi-Source Data Integration, Representation Learning, Financial Analytics,
Customer Segmentation, Contrastive Learning, Deep Learning, Churn Prediction.
1. Introduction
Figure 1: Credit Card Fraud Detection System Using ML-Based Scoring Engine
Profiling of customers forms an imperative base activity management. [1-4] Proper and live profiling enables
within the credit card sector and helps facilitate most of its financial institutions to know the behavior of the customers,
imperative basis operations like risk evaluation, one-on-one predict their needs, and overcome perceived risks.
marketing, fraud prevention and customer relations Conventionally, the process has relied strongly on manually

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025
engineered features of demographic, transactional, and credit indicators of customer behavior, which customers might
history information. The former is then thrown into regard as personal. In addition, it is known that static feature
supervised machine learning algorithms to help forecast how engineering commonly fails to acquire more complicated and
creditworthy one is or whether one is likely to churn. These non-linear patterns and time-related trends in consumer
methods, although efficient in other scenarios, have a behaviour. With financial systems becoming increasingly
number of drawbacks, especially the lack of sufficient digitalised and data-abundant, there is an emerging need for
amounts of labeled data, which are generally not available or more scalable, flexible, and privacy-friendly methods of
quite costly and sensitive by nature. customer profiling that can extract the richness of
information from multiple-source data without being limited
Labeling of the financial data also comes with its by the presence or absence of labels.
privacy implications since, in some cases; it might involve
access to personally identifiable information or even
1.1. Emergence of Self-Supervised Learning (SSL)
Definition and Core Principles
Other Domain Success
Applicability to Financial Data
Benefits of Using It in Place of Conventional Methods
Raising Research and Industry Profession
Figure 2: Emergence of Self-Supervised Learning (SSL)
 Definition and Core Principles: Self-Supervised prediction, achieving new state-of-the-art results on
Learning (SSL) is a field in machine learning in multiple tasks. These achievements have
which models are trained to learn meaningful demonstrated that SSL can reveal deep and general
representations of unlabeled training data through benefits in complex and high-dimensional
solving auxiliary or alternate (pretext) tasks. It information.
differs from supervised learning, which requires  Applicability to Financial Data: The popularity of
costly and sometimes rarely available labeled data the SSL has increased in other spheres, but its use in
and instead uses unlabeled data best parts to assign customer profiling in the financial service sector is
pseudo-labels based on the inherent data structure. just coming of age. Financial data, which manifests
For example, Predicting missing values, reordering in multiple modalities (including tabular records,
sequences, or finding augmented variants of the time series, and behavioural logs), serves as a rich
same input are tasks that can guide the model to environment for applying SSL. SSL can be applied
learn meaningful patterns without requiring human to learning robust representations of customers by
annotation. Such representations can, in turn, be devising and matching suitable pretext tasks (e.g.,
used in downstream tasks such as classification or masked transaction prediction, temporal shuffling,
clustering. and behavioral similarity detection) and the required
 Other Domain Success: SSL has been attracting spending habits, risk indicators, and engagement
much attention in such areas as computer vision and profiles can be learned in an entirely unsupervised
Natural Language Processing (NLP). Measurements way without relying on manual labels or search.
Contrastive learning methods have already  Benefits of Using It in Place of Conventional
performed as well as or even better than supervised Methods: Compared to the traditional supervised
models on general benchmarks in vision. Pre- and unsupervised learning techniques, SSL has a
trained Transformers In NLP practice, Transformer- number of advantages. It alleviates the need to have
based models are pre-trained on large corpora using labeled data, and the financial institutions can
masked token prediction and next-sentence therefore use the humongous quantities of unlabeled
165

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025
historical reports. It also facilitates representation developing. Early industry adoption has come along
learning, in which the model itself acquires feature with academic interest as the financial industry
hierarchies which are frequently superior to hand- experiments with SSL to better spot fraud, credit
designed features. Moreover, being more flexible in scoring, and churn prediction on financial product
adapting to new or changing trends in customer consumers. Due to its scalability and labelling
behaviour patterns, SSL is more appropriate in a efficiency, SSL is one of the potential paths for
dynamic environment such as the financial sector. future financial machine-learning systems as the
 Raising Research and Industry Profession: demand for privacy increases and data volumes
Research into the use of SSL with tabular and time- expand exponentially.
series data, including financial transactions, is
1.2. Challenges in Traditional Approaches
Constraints to Data
Isolated Data Sources Limited Generalization
Labeling
Figure 3: Challenges in Traditional Approaches
 Constraints to Data Labeling: The need to use able to adjust to. These models become irrelevant in
labeled data is one of the most prominent obstacles a short time without constant retraining or
to traditional supervised learning when applied to adaptation to a domain. This inflexibility impairs
the issue of finances. Tagging of financial the use of a traditional approach in flexible or data-
information- e.g. detecting high-risk customers or deficient settings.
detecting a fraudulent transaction is a job that needs
much domain knowledge, as well as access to 2. Literature Survey
sensitive information. Not only does this render the 2.1. Traditional Customer Profiling Techniques
process time-consuming and costly, but it also Conventional techniques of customer profiling have
raises considerable privacy concerns, given that been using algorithms like K-Means and the Gaussian
regulatory pressure is on the rise to adhere to Mixture Model of clustering. [5-8] These techniques are
standards such as GDPR and CCPA. The effect of it generally applied to hand-crafted features mined in
is that much potentially useful data is either not transaction data and demographic data, i.e. age, income and
labeled or makes use of only a few labels, so spending patterns. As an example, the K-Means algorithm
conventional modeling approaches are limited. divides the customers into specific groups based on the
 Isolated Data Sources: Customer data is often similarity of their features but takes the linear separability
managed in multiple, disconnected systems at most assumption, which restricts the representation of any
financial institutions. Data silos are inevitable, with complex pattern in the high-dimension data.
transactional logs, demographic data, credit data
and web interactions typically stored in individual The Decision Trees were quite popular, using
databases or separate business units. This characteristics such as credit score and the mean amount of
disintegration interferes with the formation of an transactions to classify the customer profiles. Nonetheless,
all-rounded customer profile and denies models a such models tend to overfit, especially when over-fitted
chance to make use of the entire range of behavior small or noisy data is used. These traditional methods,
and contextual indications. Technically, it is despite being simple and interpretable, cannot understand the
difficult to merge and preprocess these wildly complexity and dynamism of contemporary customer
different data sources; not only is it technically behaviour very well.
challenging, but it is also constrained by
organizational rules and compliance regulations. 2.2. Finance Finance Supervised Machine Learning
 Limited Generalization: Labeled data models, As more labeled financial data becomes available,
whether handled by a supervisor, require supervised supervised machine learning models are starting to see wider
learning and tend to overfit to the training dataset application in fraud detection, customer segmentation, and
distribution (depending on variables, segments, credit scores. Random Forests, XGBoost, and Neural
geographies and timeframes), and lack the ability to Networks algorithms have proven to have great predictive
generalize further. The behavior of financial entities abilities, as they learn complex, non-linear patterns from
is variable depending on macroeconomic large datasets. These models enjoy the richness of features
phenomena, policy changes, or personal factors- and may accept a wide range of input classes, and yet they
which creates discrepancies in what is called data are very sensitive to the availability and quality of labeled
drift which, in turn, non-learned models will not be data. Moreover, they are especially prone to problems such
166

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025
as class imbalance, which frequently occurs in financial Nevertheless, they are not extensively used to profile
realms, e.g., a few fraudulent transactions make up a customers on a wider scale, which is explained partly by
negligible proportion of the data. This sensitivity usually technological difficulties in adapting such models to multi-
demands employing data augmentation methods or loss modal and multi-source financial data.
functions in the production of sturdy performance.
2.4. Gaps identified
2.3. Development of self-supervised methods Although there are some breakthroughs both in the field
Self-Supervised Learning (SSL) has become a strong of machine learning and deep learning, there is still a set of
paradigm, particularly in fields where costly or limited gaps that are yet to be filled in applying such techniques to
labeled data is available. Methods like contrastive learning- customer profiling in finance. To begin with, little seems to
Contrastive methods have proven to be hugely successful in have been done about the application of self-supervised
the field of computer vision by learning representations via learning to heterogeneous financial data that consists of
the comparison of augmented image pairs as seen via models transactional, demographic, and behavioral data. Second,
like SimCLR and MoCo. Transformer-based models, such as interpretability remains a concern, particularly in regulated
BERT, have succeeded in transforming natural language industries where transparency is imperative, such as the
processing by allowing for deep contextual interpretation of financial sector. Lastly, a large part of existing models does
unlabeled text. not fully utilise the temporal and contextual cues present in
customer behaviour, e.g., the time of day of the transaction
These advances have given impetus to the adoption of or scenario. Filling such gaps offers the prospect of creating
SSL to structured data, such as tabulated data, although this stronger, interpretable and generalizable systems of customer
is a growing field. Self-supervised methods have started profiling.
becoming used in the field of finance; one example where
they are applied is transaction anomaly detection.
3. Methodology
3.1. System Architecture
Figure 4: System Architecture
 Data Preprocessing: Cleaning and transformation presented in this module include contrastive
of raw financial data into a structured form in which learning, masked feature reconstruction, or temporal
the data can be modeled occur at the first stage. [9- order prediction. By effectively solving such tasks,
12] This involves dealing with missing data, scaling the model encodes interesting patterns and
continuation variables, encoding categorical structures within the data, which improves the
attributes as well as synchronizing temporal quality of the learned representations.
information in various modalities like transactions,  Feature Aggregation: The features represented
demographics and behavioural logs. The across modalities are then pooled into a single
preprocessing ensures data consistency, thereby unified representation. Information is integrated in
quantifying the quality of the learned terms of relevance using such techniques as
representations. attention mechanisms or weighted averaging. Such
 Multi-Modal Feature Encoding: The system uses a step is required to explore the interdependence
separate encoders to accommodate its modality in between different types of data, which, in turn,
order to manage the variety of data sources. As an results in a comprehensive picture of each customer
example, transactional sequences are rolled out by profile.
temporal encoders and static demographic features  Downstream Task Heads: The aggregated
are rolled out by feedforward layers. The encoders representation is finally fed to a series of task-
learn to map the raw inputs to a common latent specific heads with numerous supervised tasks like
space, retaining modality-specific information and the segmentation of customers, risk scoring or
allowing joint learning. predicting churn. Heads are finetuned by labeled
 SSL Pretext Task Unit: The model is trained using data and make use of all of the rich representations
Self-Supervised Learning (SSL) module and does acquired in the self-supervised stage to achieve
not require labeled data. The types of pretext tasks higher performance on specialized business tasks
167

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025
3.2. Data Sources of a customer, the character of spending, and so,
 Transaction Logs: Purchases and financial anomalies which can occur with time.
operations of customers are stored in the form of  Demographics: Demographic data are
transaction logs that illustrate a chronological structured information that includes age, gender,
history of customer transactions. Some of the and the level of income of customers. In tabular
attributes that a given entry usually contains are the form, these features form the necessary features for
amount of transaction, time and category of profiling users and separating them according to
spending. This is time-series information in nature socioeconomic significance. These are also used as
per se, and this would be very useful in giving bases for assessing creditworthiness and targeting
critical information regarding the financial behavior products.
Figure 5: Data Sources
 Credit Bureau Reports: Credit reports show the enhance model convergence. [13-16] Min-max
history by collectively referring to a customer normalization normalizes the features to the fixed
where his/her credit score, accounts, credit range (for instance, 0 to 1) and keeps relative
repayment history and default are shown. This data relationships intact. In contrast, z-score
is typically presented in the form of a table and is normalization normalizes the features by centering
essential in determining financial risk. It is usually and scaling around the mean and the standard
employed in terms of loan approval, credit score deviation. This measure is necessary, especially in
and fraud prevention. sensitivity-to-feature magnitude algorithms
 Web Activity: Data on web activity will show the (especially neural networks).
customer activity on the digital banking platform,  Categorical Embeddings: Discrete variables, i.e., a
such as the number of logins, the number of clicks, customer occupation or a transaction category, are
the number of views per session and clickstreams. encoded as high-dimensional dense vectors (i.e., the
This time series data gives the context associated so-called embedding). Model training learns
with user activity and online behavior, and it embeddings instead of encoding with a sparse,
presents important indications of how to further inefficient one-hot encoding, which often
business knowledge can be built to do behavior accompanies a one-hot implementation. The effect
modeling, churn forecasting and personalization is that this technique is used to cause the model to
tactics. embrace semantics between categories
independently, and the performance becomes very
3.3. Feature Engineering good, most importantly, when the variables are
high-cardinality ones.
 Temporal Encoding: To represent the time aspect
of sequential data, sinusoidal position encodings are
employed. These encodings transform the
timestamps into functions that enable the model to
learn some temporal relationships and the ordering
of the sequences by mapping each timestamp as a
continuous periodically called parameter. Modeled
after transformer architectures, sinusoidal encodings
can help the model discriminate short-run patterns
Figure 6: Feature Engineering and long-run patterns on the time-series data and
learn more about the transaction history or that of
 Numerical Normalization: Numerical features are the web activities.
normalised, e.g. through min-max scaling and z-
score normalization, to enable uniform scale and
168

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025
3.4. Self-Supervised Learning Design The logits are passed through a temperature parameter
3.4.1. Contrastive Learning Objective before the softmax function is applied, and this adjusts the
The essence of contrastive learning is to teach the model sharpness of the output distribution. This promotes the model
to make the differentiation between comparable and to learn discriminating and powerful features by drawing the
dissimilar pieces of data without necessitating reliance on positive pairs nearer and exerting the negatives further apart
explicit images. With two augmented views of a given data in the embedding space.
instance, the goal is to maximise the cosine similarity of the
representations of the two views and minimise similarity
with representations of other instances in the batch.
3.4.2. Pretext Tasks
Figure 7: Self-Supervised Learning Design
 Masked Attribute Forecasting: In this task, some transaction data or weblogs. Its multi-head attention
of the attributes or features in the input data are enables different heads to attend to various regions
randomly occluded, and the model is supplied with of the sequence, which learns complex and context-
the task of predicting the occluded values. This task sensitive representations, which is vital in learning
is motivated by the BERT-style training since they the sequences of customer behavior.
provide a contextual relationship among features to  MLP Head: After the transformer encoder, the
the model, enhancing its knowledge of underlying learned features are refined and aggregated with a
data structures and dependency, which is useful in head called Multi-Layer Perceptron (MLP). It is one
tabular and multi-modal data. or more fully connected layers that use non-linear
 Time Series Forecasting: The task involves activations (to normalise high-dimensional
randomly permuting a sequence of events (e.g., embeddings into task-specific representations). This
transaction records or web interactions) and training part conducts downstream work like risk scoring,
the model to predict the correct order. It helps the purchase prediction, or fraud detection and converts
model capture time-related dependencies and the acquired temporal and contextual signals into
tendencies in data that benefit it, especially when functioning results.
interacting with time-series or sequential data sets  Clustering Layer: On top of the learned feature
in financial applications. representations, a clustering layer is applied in order
 AVP - Augmented View Prediction: Here, the to generate interpretable customer profiles. This
same data point is augmented (e.g. by adding noise layer segments customers with similar encoded
or removal of features or random permutations of behaviours and attributes and makes use of
features, etc.) many times, and the model is trained algorithms like K-Means or even deep clustering.
to learn to identify or match these augmentations. In The resulting clusters are representative of different
learning to identify multiple permutations of the groups of customers, and this can be used to market
same underlying entity, the model learns to specific groups, provide them with personal
invariances with respect to small distortions and services, or risk stratification.
noise, thereby enhancing its generalization ability
and robustness.
3.5. Model Architecture
 Transformer Encoder: The model has at its center
a Transformer encoder with self-attention sequential
data processing. The encoder extracts temporal
dependencies from time-series data, such as
169

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025
bottlenecks. The configuration was also enabled to do large-
scale hyperparameter tuning, as well as ablation studies to
distinguish the effect of each module. On the whole, the
experimental environment met the requirements of both
computational and real-world feasibility for the assessment
that aimed to create a solid benchmarking scenario for the
proposed self-supervised learning model in comparison to
classical machine learning approaches.
4.2. Metrics
A wide range of evaluation metrics was used to assess
the performance of the proposed system in a comprehensive
way in both unsupervised and supervised learning tasks. In
terms of clustering performance, two metrics commonly used
were the Silhouette Score and the Davies-Bouldin Index.
Silhouette Score is a method that measures the unity among
clusters and the dissimilarity of the cluster by contrasting
intra-cluster mean distance and the mean distance to clusters'
neighbouring points. A Greater Silhouette Score implies that
Figure 8: Model Architecture data points are coupled to a cluster they belong at and do not
go fairly coupled to other clusters, denoting distinct and
4. Results and Discussion isolated clusters.
4.1. Experimental Setup
The experimental setup aimed to assess the performance As opposed to that, the Davies-Bouldin Index measures
of the proposed self-supervised learning architecture with the average similarity of every cluster with its closest one by
large-scale real-world data of a financial nature. The sample taking into account the intra-cluster compactness as well as
consisted of 100,000 records of customers of a privately the inter-cluster separation. In this instance, the smaller the
owned banking company, where data was collected until number, the better the clustering is, as it indicates a low level
February 2025. It was multi-modal data, including four of dispersion of each cluster and a large delineation between
sources of information: transactional logs, demographics clusters. A combination of these measures provides a reliable
information, credit bureau records and traces of web activity. indication of the model's effectiveness in segmenting
Transactional data gave a timeline of customer spending customer profiles. The performance in supervised
behavior in terms of the amount spent, the time of the classification in classification problems, specifically credit
transaction and the category. risk prediction and churn classification, was determined in
terms of F1-Score, AUC (Area Under the Receiver
Demographic characteristics involved fixed Operating Characteristic Curve) and Accuracy. F1-Score is
demographic variables (age, gender and income). also handy in case of imbalanced responses since it produces
Information in credit bureaus provides background into the a more informative statistic than the accuracy level because
financial faithfulness of every client, such as their credit it balances between precision and recall.
ratings and credit history of loan repayment and liabilities.
Activity in web-based logs retrieved behavioral patterns, Precision indicates how well a model can avoid false
namely log-in frequency, click trail directions, and user positive results, and recall is used to measure how well a
activity with online banks. In order to have rigorous testing model can identify the true positive result, which is vital in
and avoid leaking of data, the given dataset was divided into the sense of risk in a high-stakes financial model. AUC is a
80% as training, 10% as validation and 10% as testing. threshold-free indicator of the quality of ranking of the
model in terms of how effectively a model separates classes
This stratification allowed one to fine-tune the model at every possible threshold. Finally, the most intuitive
over the validation set and measure performance over the test measure is called Accuracy, defined as the quotient of the
set in an unbiased manner. The experimentation and training number of correctly predicted instances and the total number
process was performed in a high-performance computing of predictions. Although it is an easy measure to understand,
environment that consists of two NVIDIA A100 GPUs, accuracy can be misguiding in distorted data, which is why it
capable of massively parallel computing, and 512GB of is complemented with the rest of the metrics. This is a multi-
RAM to support training with large batches and memory- metric assessment that allows a balanced analysis of
intensive operations. That hardware allowed the system to clustering and classification model qualities.
efficiently train complex architectures, like transformer
encoders and multi-modal feature aggregators, without any
170

Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025
4.3. Quantitative Results
Table 1: Quantitative Results
Method Silhouette AUC (Credit Risk) F1 (Churn Prediction)
Baseline (K-Means) 0.35 0.71 0.58
XGBoost 0.41 0.84 0.69
Proposed SSL 0.56 0.91 0.81
1
0.9
0.8
0.7
0.6
Baseline (K-Means)
0.5
0.4 XGBoost
0.3
Proposed SSL
0.2
0.1
0
Silhouette AUC (Credit Risk) F1 (Churn
Prediction)
Figure 9: Graph representing Quantitative Results
4.4. Quantitative Results through multi-modal signals in a label-efficient
 Baseline (K-Means): K-Means was incorporated as way. Silhouette's Score was 0.56, which means that
a control clustering algorithm to test customer more coherent and meaningful customer clusters
segmentation considering only traditional were formed. The model performed incredibly well,
unsupervised learning. It obtained a Silhouette with a very high AUC of 0.91 to predict credit risk
Score of 0.35, which represents fairly weak and and a remarkable F1-score of 0.81 to determine
overlapping measures. Given that K-Means lacks in churn. These findings make these results support the
terms of using temporal and contextual information, skill of the model to learn a rich generalizing
the algorithm also fails to develop clear customer representation out of unlabeled data apriori with
profiles. Furthermore, it has demonstrated limited pretext tasks and temporal encoding that beat both
predictive capabilities, with an AUC of 0.71 and an clustering and supervised methods.
F1-score of 0.58 on the churn prediction task, as
well as an F1-score of 0.36 on credit risk, due to its 4.5. Ablation Study
simple and linear nature when its clusters were used To know the individual effect of the key elements of the
as feature inputs to downstream tasks. proposed self-supervised learning (SSL) framework, an
 XGBoost: Being a supervised learning algorithm on ablation study was carried out. The study can provide
a hyper-modern level, XGBoost fared much better information on the relative significance of each element of
than K-Means in classification assignments. It architecture by observing the effect of selective removal of
scored an AUC of 0.84 and an F1-score of 0.69 in each module at a time on the corresponding decrease in its
credit risk assessment and churn prediction, credit risk prediction performance (measured by AUC).
respectively, representing its strength in processing Table 2 contains a summary of the findings, which have been
tabular data and ability to fit non-linear interactions. contained in detail below.
However, its Silhouette Score of 0.41, calculated Table 2: Ablation Study Results
based on intermediary representations generated by Module Removed AUC Drop
the last layer, hints at moderate improvements in the
Temporal Encoding 4.2%
quality of clustering yet projects it as being
Web Activity 3.8%
backwards in terms of producing global, behaviour-
Pretext Task 2.7%
sensitive representations that more powerful models
are capable of generating.
 Self-Supervised Learning (SSL): The SSL model
presented outperformed all baselines on every one
of the metrics, which proves the worth of learning
171

4.50% 4.20%
3.80%
4.00%
3.50%
3.00% 2.70%
2.50%
2.00%
1.50%
1.00%
0.50%
0.00%
Temporal Encoding Web Activity Pretext Task
AUC Drop
Figure 10: Graph representing Ablation Study Results
 Temporal Encoding: The removal of temporal 5. Conclusion
encoding led to the greatest decline in performance, This paper reviews the use of a Self-Supervised
whereby the AUC slumped by 4.2%. This Learning (SSL) approach, which is being applied to profile
emphasizes the importance of the modeling of time- customers within the financial industry, specifically credit
varying dynamics of customer behavior. The card users. The framework suggested was based on using
property of temporal encoding enables the model to multi-source data, including transaction logs, demographic
be sensitive to out-of-sequence and out-of-trend information, credit bureau reports, and web activity,
patterns, i.e., a history of sporadic transactions, compiled to create comprehensive representations of the
delayed payments, or recent increases in customers. With the help of contrastive learning and pretext
expenditure, which are highly correlated with credit tasks, including masked attribute prediction and recognising
risk. In its absence, the model can no longer temporal order, the model was trained to extract underlying
contextualise behaviours across time, also resulting patterns and dependencies both over time and across
in more transient representations and reduced modalities without relying on labelled data. The outcomes of
predictive capability. the experiment showed that the proposed SSL-based model
 Web Activity: Web activity features were removed significantly outperformed classical approaches, such as K-
and resulted in a 3.8% decrease in AUC; this meant Means and XGBoost, in terms of clustering quality, credit
the features provided significant information on the risk prediction, and churn classification. It is noteworthy
behavior image of people using online banking that, in terms of Silhouette, the model displayed even more
portals. The implicit clues of user engagement, excellent results in both unsupervised and supervised tasks
financial intents and reliance on digital channels and performed well in F1 and AUC indicators. The ablation
occur with metrics such as logins, session duration, study also supported the fact that the effectiveness of the
and sequence of clicks. Although these signals are model owed heavily to the existence of parts like temporal
frequently under-exploited, they bring significant encoding, behavior characteristics based on web activity, and
value to the table when they are combined into a self-supervised purposes
multi-modal model. When they are removed, this
impoverishes the input behavior and limits the These findings have tremendous implications for the
model view of user intent. financial industry. Due to the greater accuracy and resilience
 Pretext Task: The overall removal of the pretext of customer segmentation and risk modeling, financial
task module led to a 2.7 per cent decrease in AUC, institutions move on to work more intensively on credit
emphasizing the significance of self-supervised scoring, fraud detection, and customer lifecycle
goals in influencing high-quality representations of management. Besides, the detailed representations of
features. Pretext games, such as masked attribute features acquired with the help of SSL can provide
prediction and temporal order learning, allow for personalized product suggestions, adjustable credit limits,
the discovery of latent patterns and associations in and real-time intervention plans. To the customer, this means
the data. Whereas the effect is not as significant as more customized financial products, quicker decision times
that of temporal encoding or web activity, this and more personalized online experiences.
element is crucial in improving the models
generalizability and transferability to subsequent With competition getting fierce and customer
tasks. expectations changing, the capability to know and serve
172

  Thulasiram Yachamaneni et al. / IJAIDSML, 6(1), 164-173, 2025

clients in a precise manner became a strategic capability. To  conference  on  machine  learning  (pp.  1597-1607).
| anticipate,  | a  number  | of  directions  |     | can  contribute  |     | to  the  | PmLR.  |     |     |     |     |     |     |
| ------------ | ---------- | --------------- | --- | ---------------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- |
strength of this research further. To begin with, the methods  [10] Devlin, J., Chang, M. W., Lee, K., & Toutanova, K.
of federated learning would enable the training of models  (2019, June). Bert: Pre-training of deep  bidirectional
amid remote financial institutions, and it would be possible  transformers for language understanding. In Proceedings
to train models on a large scale without compromising the  of the 2019 conference of the North American chapter of
privacy  of  users  and  abiding  by  their  regulatory  the Association for Computational Linguistics: human
requirements. Second, generalizability might be enhanced,  language technologies, volume 1 (long and short papers)
and a bigger scope of financial behavior might be covered by  (pp. 4171-4186).
enlarging  the  model  to  a  cross-bank  consortium  dataset.  [11] Somepalli, G., Goldblum, M., Schwarzschild, A., Bruss,
Lastly, the inclusion of reinforcement learning may allow  C. B., & Goldstein, T. (2021). Saint: Improved neural
personalization techniques to be adaptive, such that offers,  networks  for  tabular  data  via  row  attention  and
alerts, or risk scores may be changed on the fly based on  contrastive  pre-training.  arXiv  preprint
customer reactions or actions. All combined, these future  arXiv:2106.01342.
improvements will continue to advance intelligent financial  [12] Liu, X., Zhang, F., Hou, Z., Mian, L., Wang, Z., Zhang,
services, making them more responsive, secure, and user- J.,  &  Tang,  J.  (2021).  Self-supervised  learning:
friendly.  Generative  or  contrastive.  IEEE  transactions  on
|     |     |     |     |     |     |     | knowledge and data engineering, 35(1), 857-876.  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
References  [13] Adewumi, A. O., & Akinyelu, A. A. (2017). A survey of
machine-learning and nature-inspired based credit card
| [1]  MacQueen,  | J.  (1967,  | January).  |     | Some  | methods  | for  |     |     |     |     |     |     |     |
| --------------- | ----------- | ---------- | --- | ----- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
classification and analysis of multivariate observations.  fraud  detection  techniques.  International  Journal  of
In Proceedings of the Fifth  Berkeley Symposium on  System  Assurance  Engineering  and  Management,  8,
937-953.
| Mathematical  | Statistics  |     | and  Probability,  |     | Volume  | 1:  |     |     |     |     |     |     |     |
| ------------- | ----------- | --- | ------------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Statistics (Vol. 5, pp. 281-298). University of California  [14] Ileberi, E., Sun, Y., & Wang, Z. (2021). Performance
Press.  evaluation of machine learning methods for credit card
|                 |              |           |     |          |          |     | fraud  | detection  | using  | SMOTE  | and  | AdaBoost.  | Ieee  |
| --------------- | ------------ | --------- | --- | -------- | -------- | --- | ------ | ---------- | ------ | ------ | ---- | ---------- | ----- |
| [2]  Reynolds,  | D.  (2009).  | Gaussian  |     | mixture  | models.  | In  |        |            |        |        |      |            |       |
Access, 9, 165286-165294.
| Encyclopedia  | of  | Biometrics  | (pp.  | 659-663).  | Springer,  |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | ----- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Boston, MA.  [15] Gui, J., Chen, T., Zhang, J., Cao, Q., Sun, Z., Luo, H., &
Tao, D. (2024). A survey on self-supervised learning:
| [3]  Quinlan,  | J.  R.  | (1986).  | Induction  | of  | decision  | trees.  |              |     |                |      |         |          |       |
| -------------- | ------- | -------- | ---------- | --- | --------- | ------- | ------------ | --- | -------------- | ---- | ------- | -------- | ----- |
|                |         |          |            |     |           |         | Algorithms,  |     | applications,  | and  | future  | trends.  | IEEE  |
Machine learning, 1, 81-106.
[4]  Breiman, L. (2001). Random forests. Machine learning,  Transactions  on  Pattern  Analysis  and  Machine
| 45, 5-32.  |     |     |     |     |     |     | Intelligence.  |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
[16] Ericsson, L., Gouk, H., Loy, C. C., & Hospedales, T. M.
[5]  Chen, T., & Guestrin, C. (2016, August). Xgboost: A
scalable  tree-boosting  system.  In  Proceedings  of  the  (2022).  Self-supervised  representation  learning:
22nd  ACM  sigkdd  International  Conference  on  Introduction,  advances,  and  challenges.  IEEE  Signal
Processing Magazine, 39(3), 42-62.
Knowledge Discovery and Data Mining (pp. 785-794).
|     |     |     |     |     |     |     | [17] Dixon,  | M.  | F.,  Halperin,  | I.,  | &  Bilokon,  | P.  | (2020).  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | ---- | ------------ | --- | -------- |
[6]  Dal Pozzolo, A., Boracchi, G., Caelen, O., Alippi, C., &
Bontempi,  G.  (2017).  Credit  card  fraud  detection:  Machine learning in finance (Vol. 1170). New York,
NY, USA: Springer International Publishing.
realistic modeling and a novel learning strategy. IEEE
[18] Lei, X., Mohamad, U. H., Sarlan, A., Shutaywi, M.,
transactions on neural networks and learning systems,
29(8), 3784-3797.  Daradkeh,  Y.  I.,  &  Mohammed,  H.  O.  (2022).  The
He,  H.,  &  Garcia,  E.  A.  (2009).  Learning  from  development of an intelligent information system for
[7]
|     |     |     |     |     |     |     | financial  | analysis  | depends  |     | on  supervised  |     | machine  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | -------- | --- | --------------- | --- | -------- |
imbalanced data. IEEE Transactions on knowledge and
data engineering, 21(9), 1263-1284.  learning  algorithms.  Information  Processing  &
[8]  Chen,  X.,  Fan,  H.,  Girshick,  R.,  &  He,  K.  (2020).  Management, 59(5), 103036.
[19] Liu, Y., Jin, M., Pan, S., Zhou, C., Zheng, Y., Xia, F., &
| Improved  | baselines  | with  | momentum  |     | contrastive  |     |      |                  |        |                  |     |            |     |
| --------- | ---------- | ----- | --------- | --- | ------------ | --- | ---- | ---------------- | ------ | ---------------- | --- | ---------- | --- |
|           |            |       |           |     |              |     | Yu,  | P.  S.  (2022).  | Graph  | self-supervised  |     | learning:  | A   |
learning. arXiv preprint arXiv:2003.04297.
[9]  Chen, T.,  Kornblith,  S.,  Norouzi,  M.,  &  Hinton,  G.  survey.  IEEE  transactions  on  knowledge  and  data
engineering, 35(6), 5879-5900.
(2020, November). A simple framework for contrastive
[20] Garbarino, S., & Holland, J. (2009). Quantitative and
| learning  | of  visual  | representations.  |     | In  | International  |     |     |     |     |     |     |     |     |
| --------- | ----------- | ----------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
qualitative methods in impact evaluation and measuring
results.

173