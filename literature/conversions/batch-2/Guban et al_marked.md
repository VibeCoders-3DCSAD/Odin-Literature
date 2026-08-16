---
conversion_metadata:
  converted_at: "2026-07-22T13:27:29Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Guban et al.pdf"
  source_pdf_sha256: "09a679095092534bf92e8a20a7e6cc6959ec014b945f2a1d80a1888ea3b891e4"
  page_count: 7
  markdown_char_count: 76954
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Technological University of the Philippines - Manila  
College of Science  
IT323 - Business Intelligence

WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION

MEMBERS: 
Josef Christopher R. Guban 
Christian Dayne R. Menderico 
Don Marco G. Montalban

INSTRUCTOR: 
Mr. Jonathan Caballero

May 22, 2025

---

<!-- PAGE 2 -->

ABSTRACT

In  today’s  increasingly  competitive  streaming 
landscape,  understanding  user  preferences in subscription 
plan  selection  is  vital  for  implementing  data-driven 
strategies.  This  study  examines 
the  impact  of  key 
demographic  and  behavioral  attributes—namely  age, 
type,  and  subscription  start 
gender,  country,  device 
month—on  the  selection  of  Basic,  Standard,  or Premium 
plans on a major streaming platform. Utilizing a dataset of 
2,500 anonymized user records, a supervised classification 
model  was  developed  and  validated  using  the  J48 
decision-tree algorithm in WEKA. An 80/20 train-test split 
was  applied,  and  the  model’s  performance  was  assessed 
using  standard  evaluation  metrics,  including  accuracy, 
Kappa  statistic,  precision,  recall,  F-measure,  and  ROC 
area.

The model achieved an overall accuracy of 72%, 
with  country  identified  as  the  most  influential  predictor, 
followed  by  age  and  device  type.  Results  revealed 
interpretable  decision  rules  that  highlight  how  different 
user  profiles 
subscription 
preferences.  For  example,  younger  smartphone  users 
subscribing  later  in  the  year  often  chose  Premium  plans, 
whereas older users on Smart TVs tended toward Standard 
or  Basic  tiers.  The  decision  tree  effectively  captured 
complex  attribute  combinations,  offering  clarity 
in 
understanding plan selection behavior.

correspond

specific

to

By  transforming  raw  user  data  into  meaningful 
patterns,  this  study  underscores  the value of interpretable 
machine learning models in generating actionable insights. 
These  insights  can  inform  subscription  plan  design  and 
targeted  strategy  development,  illustrating  the  role  of 
Business  Intelligence  in  bridging  user  behavior  with 
platform optimization.

CHAPTER I: INTRODUCTION

The Problem and Its Background

In

the

ever-evolving  digital  entertainment 
industry,  streaming  platforms such as Netflix rely heavily 
on Business Intelligence (BI) to understand their users and 
competitive.  As  user  behavior  becomes 
remain 
increasingly  diverse  and  complex,  understanding  the 
factors  that  influence  subscription  choices  has  become  a 
critical area for data-driven decision-making. While many 
studies  have  explored  content  recommendation  and  user 
engagement,  there  remains  a  gap  in  analyzing  how 
individual  user  attributes  affect 
selection  of 
subscription plans such as Basic, Standard, or Premium.

the

not

only

these

patterns

Consumer  choices  are  often  shaped  by variables 
such as age, device preference,   and engagement patterns. 
Identifying 
improves 
personalization  but  also  supports  marketing  strategies, 
customer  retention,  and  service  optimization.  Chaurasia 
and  Pal  (2019)  emphasized  that  data  mining  techniques 
can  uncover  valuable  insights  into  user  decisions,  while 
Dey  and  Haque  (2021)  highlighted  the  importance  of 
predictive  analytics  in  understanding  user  behavior  in 
subscription-based platforms.

With  the  growing  amount of data available from 
user  interactions,  machine  learning  and  classification 
models  offer  promising  tools  for  predicting  subscription 
types and analyzing consumer trends. Effective application 
of  these  models  can  lead  to  enhanced  service  offerings 
tailored  to  different  customer  segments  (Zhang,  S.,  Yao,

L.,  Sun,  A.,  & Tay, Y., 2019). Additionally, García-Gil et 
al.  (2019)  noted  that preprocessing and intelligent feature 
selection significantly enhance model performance in large 
datasets—an 
streaming 
important 
platforms with millions of active users.

consideration

in

This  study  explored  how  user  data,  such as age, 
device usage, and viewing behavior, was transformed into 
meaningful  insights  using  Business Intelligence tools and 
machine learning models, enabling a deeper understanding 
of  the  factors influencing subscription plan selection on a 
streaming platform like Netflix.

OBJECTIVES 
This study aims to derive actionable insights by evaluating 
user subscription behavior through data analytics.

Specific Objectives:

1.  To develop and validate a decision‑tree model for 
accurately  predicting  users’  future  subscription 
plans.

2.  To  generate  data-driven 
influence

that

attributes 
selection.

insights  from  user 
subscription  plan

Scope

and

attributes

This  research  investigates  how  a combination of 
demographic 
shapes 
behavioral 
subscription‑plan choices on an online streaming platform. 
Leveraging a real‑world dataset of 2,500 anonymized user 
records,  the  study  focuses  on  five  key  predictors  like 
country,  age,  gender,  device  type,  and  subscription  start 
month  to  understand  their  joint  influence  on  selecting 
among Basic, Premium, and Standard tiers. The analysis is 
confined  to  complete  cases  for  these  attributes  and 
employs  a  decision‑tree  classifier  to  extract  interpretable 
rules. Performance is gauged via a percentage split of 80% 
by  20%,  reporting  overall  accuracy, Kappa statistic, error 
metrics,  and  class‑specific  precision,  recall,  F‑measure, 
and  ROC  area.  Findings  will  illuminate  which  attribute 
combinations  most  strongly  predict  each  subscription 
for 
category,  offering  actionable 
targeted 
insights 
the  studied 
marketing  and  product  design  within 
eight‑country market.

CHAPTER II: RELATED LITERATURE

Business Intelligence in Subscription Management

In

revenues.

(2024)  highlight

subscription 
streaming  market,  platforms

Business  Intelligence  (BI)  tools  have  become 
central  to  streaming  platforms’  ability  to  segment  users, 
optimize  offerings,  and drive revenue growth. Nwaimo et 
software  empowers 
that  BI 
al. 
decision‑makers  to  translate  large  volumes  of  user  data 
into  actionable  strategies,  from  tailoring  plan  features  to 
the  highly 
forecasting 
leverage 
fragmented 
dashboards  and  reporting  to  track  real‑time  subscription 
uptake,  detect  underperforming  tiers  early,  and reallocate 
marketing  spend  efficiently  (Palani,  2025).  This  aligns 
with the growing use of machine learning models, such as 
decision  trees,  to  uncover  patterns  in  demographic  and 
behavioral  data,  like  age,  gender,  and  device  type  that 
influence subscription choices (Garcia & Lee, 2022). Chen 
and  Zhang (2023) further demonstrate that BI-driven user 
clustering enhances content delivery and subscription plan 
alignment,  leading  to  higher  retention.  Park  and Sullivan

---

<!-- PAGE 3 -->

(2023)  also  stress  the  strategic  advantage  of real-time BI 
dashboards  in  responding  to  shifts  in  user  preferences 
across  regions  and  subscription  tiers.  These  insights 
support  the  analytical  approach  of  this  study,  which 
applied  classification  models  to  predict  user  subscription 
types  and  guide  segmentation  strategies  across  eight 
countries.

Demographic Drivers of Subscription Choice

likely

are  more

is  Geneva  (2023)  report

A  growing  body  of  work  examines  how  user 
demographics  (age,  gender,  geography,  device  usage) 
influence  plan  selection. Joshi (2024) shows that younger 
to  adopt  higher‑priced, 
cohorts 
multi‑device tiers, whereas older segments often remain on 
basic plans. Some study highlights that demographics and 
connectivity  strongly  influence  subscription  choices. One 
notable  example 
in  stark 
international gaps in broadband access and usage, it shows 
high‐income  countries  average  257 GB/month  per  fixed 
in 
broadband 
low‐income countries, and 5G mobile coverage is 89% in 
wealthy  countries  but  nearly  0%  in  the  least  developed 
country.  Such  disparities 
in 
lower‐bandwidth  regions  (often  with fewer smart TVs or 
4G  devices)  may  favor basic, lower-cost streaming plans, 
whereas  users  in  high‑speed  markets  can  more  easily 
choose  premium,  high‑definition  plans.  This  consistently 
proves  analyses  showing  that  regional  broadband  and 
device  adoption  patterns  drive  basic  and  premium 
subscription preferences.

that  consumers

only  161 GB

subscription

versus

imply

Predictive Modeling of Subscription Plans

in

Machine-learning

stakeholders  who

approaches  have  become 
forecasting  user  subscription  choices, 
essential 
particularly  in  dynamic  and  user-driven  platforms  like 
video  streaming  services.  Among  various  algorithms 
explored,  Akar  (2023)  compares  logistic  regression, 
random  forests,  and  decision  trees,  concluding  that 
tree-based  classifiers  strike  an  ideal  balance  between 
predictive accuracy and interpretability, an essential factor 
for  business 
transparent 
decision-making  processes.  R.  Gustavo  et  al.  (2023) 
further demonstrate how feature-importance scores derived 
from models can drive personalized marketing campaigns, 
enabling  companies  to  target  users  based  on  their  most 
influential  characteristics,  such  as  device 
type  or 
that 
subscription  month.  Patil 
explainable  models  like  the  C4.5  decision  tree  not  only 
boost  transparency  but  also  foster  trust  in  automated 
systems  by  providing  human-readable  rules  for  strategic 
marketing.

(2024)  emphasizes

require

Furthermore,  predictive  performance  must  meet 
industry  reliability  thresholds  for  practical  deployment. 
Hsiao (2023) highlights that an accuracy of at least 70% is 
considered  a  benchmark  for  commercial  applications, 
ensuring  the  model  delivers  actionable  and  generalizable 
insights.  This  is  particularly  important  in  environments 
where  misclassifying  a  high-value  user  could  result  in 
substantial  revenue  loss.  Supporting  this,  Kim,  Lee,  and 
Park (2022) applied decision tree models in the context of 
influencer-driven  commerce  to  predict  customer  churn, 
achieving  over  80%  accuracy.  Their  work  stresses  the 
importance of not only high overall performance, but also 
strong  class-level  precision  and  recall  metrics  that  are 
critical in capturing the behavior of smaller, more valuable

user  segments  like  Premium  subscribers  in  streaming 
platforms.

The  inclusion  of  behavioral  variables  such  as 
session  length,  time  of  day,  and  content  interaction 
frequency  was  also  shown  to  improve  model  granularity 
and  reduce  classification  bias.  These  findings  translate 
services,  where 
directly 
understanding  nuanced  user  habits  can  significantly 
improve tier targeting.

subscription-based

to

Decision‑Tree Applications in Streaming Analytics

Decision

trees  have  seen  wide  adoption  in 
streaming analytics because they produce human‑readable 
rules.  Gomez‑Uribe & Hunt (2015) originally applied tree 
models  to  viewer  engagement,  showing  how  splitting  on 
country,  device  type,  and  user  tenure  yields  coherent 
segments.  In  the  context,  J48’s  ability  to  partition  on 
month  of  subscription start further captures seasonality in 
plan uptake. Contrary to the notion that deep trees always 
overfit,  recent  work  shows  very  large  trees  can  still 
generalize  well  with  proper  validation.  For  instance, 
Aouad et al. (2023) report final decision trees with depths 
52–78 containing 800–4100 leaves; despite their size these 
models  achieved  superior 
test-set  performance  (e.g. 
significant  improvements  in  AUC  and lower MSE) when 
properly  cross-validated.  In  other  words,  trees  with 
hundreds of leaves can retain strong predictive accuracy if 
pruned  or  validated,  this  substantiates  that  “trees  with 
300+  leaves  can  still  generalize  well  when  properly 
validated. In practice, an 80/20 train-test split is commonly 
employed  to  evaluate  the  performance  of  decision  tree 
models. This approach ensures that the model is trained on 
a substantial portion of the data while reserving a separate 
subset  for  unbiased  testing,  thereby  providing  a  reliable 
assessment of the model's generalization capabilities. Such 
validation  strategies  are  crucial  for  developing  robust 
models that perform well on unseen data (Awad & Fraihat, 
2023). Emerging research also explores the adaptability of 
decision  trees in streaming data contexts. Manapragada et 
al.  (2020)  discuss  the  use  of  Hoeffding  trees  in evolving 
data  streams,  highlighting  their  efficiency  in  real-time 
applications. Haug et al. (2022) introduce Dynamic Model 
Trees  for  interpretable  data  stream  learning, emphasizing 
their ability to maintain flexible and robust representations 
in active data concepts.

Performance Metrics for Subscription Classification

thresholds

(Orozco-Arias,

less‑common  plans

Evaluating  predictive  models  for  plan  choice 
requires  both  aggregate and class‑level measures. Beyond 
overall  accuracy  and  the  Kappa  statistic,  precision  and 
recall  for  each  tier  illuminate  where  a  model  may 
underpredict 
(e.g.,  Premium). 
ROC‑area analysis further quantifies discrimination power 
across 
The 
confusion‑matrix  approach  provides  a  granular  view  of 
misclassification  patterns,  crucial  for  assessing  revenue 
impact  when  a  high‑value  user  is  misassigned to a lower 
tier.  As  noted  by  Sokolova  and  Lapalme  (2009), 
multi-class  performance  analysis  is  essential  when  class 
imbalance  affects  business-critical  segments.  Powers 
(2011)  emphasizes  that  relying  solely  on  accuracy  may 
obscure  model 
in  uneven  class 
distributions.  Similarly,  Wu  et  al.  (2021)  highlight  that 
ROC  and  precision-recall  curves  are  more informative in 
in 
identifying

threshold-sensitive  errors,  particularly

flaws,  especially

2020).

---

<!-- PAGE 4 -->

digital consumer modeling. Lastly, Huang and Ling (2005) 
show  that  ROC  analysis  remains  robust  even  under 
skewed  class  distributions,  making  it  a  reliable  tool  for 
evaluating subscription classification systems.

CHAPTER III: METHODOLOGY

Research Design

estimates

that  performance

This  study  adopts  a  quantitative,  predictive 
framework in which a supervised decision‑tree model (J48 
in Weka) is used to classify users into Basic, Premium, or 
Standard subscription plan based on their profile attributes. 
An 80 % by 20 % split is applied, 80 % of the data is used 
for  training  the  model  and  20 %  for  independent  testing, 
ensuring 
true 
out‑of‑sample  accuracy.  By  structuring  the  work  as  an 
experiment  in  rule  induction  and  validation,  researchers 
systematically  uncover  patterns  in  how  combinations  of 
country,  age,  gender,  device  type,  and  subscription  start 
month drive plan selection. The use of an interpretable tree 
structure allows for the derivation of clear, actionable rules 
that marketing and product teams can leverage. Moreover, 
framing the analysis as a controlled validation experiment 
ensures that findings are both reliable and generalizable to 
new user cohorts.

reflect

Data Collection and Preparation

The  researchers exported 2,500 anonymized user 
the  streaming  platform’s  subscription 
from 
records 
database,  each  containing  the five predictor variables and 
the 
target  subscription  plan.  During  preprocessing, 
duplicate entries and any records with missing values were 
removed to preserve data integrity and avoid bias in model 
training  (Nasima,  2025).  Categorical  fields  like  country, 
gender,  and  device  type  were  encoded  as  nominal 
attributes,  while 
the  subscription  start  month  was 
formatted as an integer (1–12). Continuous variables such 
as age were retained to allow the decision‑tree algorithm to 
determine  data‑driven  split  points,  enhancing the model’s 
ability to capture nonlinear patterns in the data.

Model Training and Validation

The  cleaned  dataset  was  subjected  to  the  J48 
decision‑tree  algorithm  to  construct  a  hierarchical  set  of 
decision  rules  that  map  user  attributes  to  subscription 
outcomes (Razzaq, 2017). To guard against overfitting and 
to  gauge  true  predictive  power, the researchers employed 
an  80 %  by  20 %  percentage  split,  training  the  model on 
80 %  of  the records and testing it on the remaining 20 %, 
while  preserving  class  proportions  in  both  subsets.  The 
study  recorded  overall  accuracy,  Kappa  statistic,  mean 
absolute  error,  and  root  mean  squared  error,  as  well  as 
precision,  recall,  F‑measure,  and  ROC  area  for  each 
subscription 
comprehensive 
assessment  of  model  performance.  Finally,  the  resulting 
confusion matrix and per‑class ROC curves were analyzed 
to  pinpoint  where  the  model  excels  and  where  further 
refinement is needed.

category,  providing

a

CHAPTER IV: RESULTS AND DISCUSSION

Decision Tree - Classification Model

The  J48 decision tree, trained on 2,499 instances 
using  six  attributes,  identified  country  as  the  most 
significant predictor of subscription type. Branches further

split based on age, gender, device, and start month. In the 
United States, Smartphone users aged ≤31 who started on 
or  before  May  were  classified  as  Basic  (6  instances). 
When  starting  after  May  and  aged  ≤30,  users  were 
assigned  to  Premium.  Older  Smartphone  users  showed 
gender-based  splits:  males  aged  33–44  starting  mid-year 
were classified as Standard, while females aged ≤40 using 
Smart  TVs  were  split  between  Premium,  Basic,  or 
Standard based on finer age and timing (2–9 instances). In 
Canada,  male  Smartphone users starting before or in July 
were  mostly  classified  as  Basic  or  Standard  (3–21 
instances),  while  female  Tablet  users  aged  ≤41  starting 
after  May  were  directed  to  Premium  (up  to  9 instances). 
Device and start month were influential across the board.

showed

two  Premium-leaning

All  United  Kingdom  users,

regardless  of 
demographic or device, were assigned to the Standard plan 
(195  instances),  indicating  consistent  behavior.  In  Brazil, 
most females and males using Tablets or Smart TVs were 
linked  to  the Basic plan, especially when starting early in 
the  year  (3–23  instances),  with  occasional  variation. 
Australia 
segments: 
Smartphone  users  aged  ≤28  starting  before  August  (4–6 
instances)  and  older  Laptop/Smart  TV  users  starting 
mid-year  (up  to 18 instances). In Mexico, users aged >28 
were  strongly  associated  with  the  Standard  plan  (181 
instances),  while  younger  users  showed  more  diversity. 
Germany’s  males  aged  ≤33  were  assigned  to  Basic  (19 
instances).  Older  users’  classifications  varied  based  on 
device  and  start  month,  with  Tablets  leaning  Basic  and 
others  mixed.  In  France,  younger  users  and  early-year 
Smart  TV/Laptop  users  leaned  Premium  (up  to  26 
instances),  while  older  users  generally  shifted  toward 
Basic, with gender and device also affecting classification.

72%

28%

Table 1: Split Percentage Testing Summary

Correctly Classified Instances

360

Incorrectly Classified Instances

140

Kappa statistic

0.5797

Mean absolute error

0.2216

Root mean squared error

0.3882

Relative absolute error

49.86%

Root relative squared error

82.34%

Total Number of Instances

500

Table  1  summarizes  the model’s performance on 
the  testing  set,  including  the  total  number  of  correct and 
incorrect  classifications,  overall  accuracy,  and  the  Kappa 
statistic  for  agreement  between  actual  and  predicted 
values.  It  also  presents  error-based  metrics  such as mean 
absolute  error,  root  mean  squared  error,  and  their 
respective  relative  errors.  The  total  number  of  evaluated 
instances  is  provided,  reflecting  the  dataset  size  used for 
validation.

---

<!-- PAGE 5 -->

DISCUSSION OF FINDINGS

Table 2. Identifying User Profile Combinations that Predict Specific Subscription Plans

Country

United States

United States

United States

United States

Canada

Canada

United Kingdom

Brazil

Australia

Australia

Mexico

Germany

Germany

France

Key Attributes

Likely Subscription

Smartphone users aged ≤31, start_month ≤5

Smartphone users aged ≤30, start_month >5

Smart TV users (M) aged 33–44, start_month 
5–9

Smart TV users (F) aged ≤40, start_month 
≤10

Basic

Premium

Standard

Premium or Basic

Male Smartphone users, start_month ≤7

Standard or Basic

Female Tablet users aged ≤41, start_month 
>5

All users regardless of demographics or 
device

Most females and males using Smart 
TVs/Tablets

Smartphone users aged ≤28, start_month ≤8

Laptop or Smart TV users aged >35, 
start_month mid-year

Users aged >28

Males aged ≤33

Older males on various devices

Younger users and Smart TV/Laptop users, 
early start_month

Premium

Standard

Basic

Premium

Premium

Standard

Basic

Mixed

Premium

The  decision  tree  reveals  that  subscription  plan 
selection  is  strongly  influenced  by  a  combination  of 
country, age, device, gender, and start month. In the United 
States, 
the  model  shows  a  nuanced  segmentation: 
Smartphone  users  aged  31  and  below  tend  to  choose the 
Basic plan if they subscribe early in the year (start_month 
≤  5),  but  shift  toward  Premium  when  subscribing  later 
(start_month  >  5).  The  preferences  of  Smart  TV  users 
further  segment  by  gender and age. Females aged 40 and 
below  alternate  between  Basic  and  Premium,  depending 
on  exact  age  and  start  month, while males aged 33 to 44 
often  align  with  the  Standard  plan,  particularly  in  the 
mid-year period. These findings illustrate that subscription 
behavior  in  the  U.S.  varies  with  time,  age,  and  access 
device,  allowing  precise  targeting  strategies  that  match 
subscription plan with user lifecycle stages.

and

In  Canada,  the decision rules highlight that male 
Smartphone  users  who start their subscription before July 
typically  fall  into  Standard  or  Basic, while female Tablet 
users  aged  41  and  below  tend  to  choose  Premium  when 
starting after May. This underlines the relevance of device 
type 
in  Canadian  market 
timing 
segmentation.  In  contrast,  the  United  Kingdom  shows  a 
highly  uniform  trend:  regardless  of  user  age,  gender,  or 
tier.  This 
into 
device,  all  users  fall 
homogeneity enables simplified campaigns focused solely 
on promoting the Standard plan’s features without need for 
personalization.

the  Standard

seasonal

Other  markets  exhibit  stronger  correlations  with 
price  sensitivity  and  device  preference.  In  Brazil,  a

regardless  of  device,

dominant  trend  toward  the  Basic  plan  is  seen  among 
females  and  Smart  TV  or  Tablet  users,  particularly  with 
early-year  subscriptions,  suggesting  that  affordability and 
accessibility  are  key  decision  factors.  In  Australia,  two 
distinct  Premium  segments  emerge:  younger  Smartphone 
users  (aged  ≤28)  starting  before  August,  and  older  users 
using  Smart  TVs  or  Laptops,  especially  mid-year.  This 
indicates dual targeting strategies based on age and device 
sophistication. In Mexico, the primary determinant is age; 
users  older  than  28  are  strongly  associated  with  the 
simplifying 
Standard  plan 
segmentation  efforts.  Meanwhile,  Germany  presents 
age-divided  behavior:  younger  males  (≤33)  prefer  Basic, 
but older users show mixed preferences that vary with both 
device  and  subscription  timing.  France  demonstrates  a 
stronger  lean  toward  Premium  among  younger  users  and 
Smart  TV  or  Laptop  users,  especially  when  subscribing 
early in the year, while older users transition toward Basic. 
Overall,  the  decision  tree  structure confirms that 
is  shaped  by  complex 
user  subscription  behavior 
combinations  of  demographic  and  behavioral  variables, 
fulfilling  the  study's  first  objective.  The  insights  derived 
from  the  model  provide  a  granular understanding of how 
different  segments  respond  to  service  offerings,  enabling 
data-driven  recommendations  for targeted acquisition and 
retention  strategies.  These  patterns,  identified  across 
markets,  present  actionable  frameworks  for  subscription 
platforms  aiming  to  optimize  user  engagement  through 
tailored plan offerings.

---

<!-- PAGE 6 -->

followed  by  age,  device  type,  gender,  and  subscription 
start  month.  The  classification  tree  revealed  that  user 
preferences are shaped by multi-factor combinations rather 
than  isolated  variables.  For  instance,  the  same age group 
may  exhibit  differing  plan  preferences  based  on  device 
usage  or  start  timing,  depending  on  the  regional context. 
This confirms the complexity of user decision-making and 
highlights 
to  reflect  real-world 
behavioral diversity. 
The

learning 
models,  particularly  interpretable ones like decision trees, 
can  offer  granular  insights  into  subscriber  segmentation, 
enabling streaming platforms to design targeted marketing 
tiers,  and  enhance  user 
strategies,  adjust  pricing 
acquisition  and 
through  proactive, 
data-driven personalization.

the  model's  ability

retention  efforts

findings  affirm

that  machine

RECOMMENDATION

indicators  such  as  watch

results,  exploring  ensemble  methods

While the model demonstrated solid performance, 
several  areas  offer  opportunities  for  enhancement.  The 
dataset  was  limited  to  five  user  attributes,  excluding 
behavioral 
time,  session 
frequency,  or genre preferences, which may further refine 
prediction  accuracy.  Future  research  should  incorporate 
these  variables  to  capture  a  broader  behavioral  context. 
While  the  J48  decision  tree  provided  interpretable  and 
effective 
like 
Random Forests or Gradient Boosted Trees could improve 
predictive robustness and reduce overfitting. These models 
may  capture  complex  nonlinear  interactions  that  a  single 
tree might miss, especially in regions with more diverse or 
ambiguous  subscription  patterns.  It  is  also  recommended 
to  test  the  model  on  a  different  dataset  to  assess  its 
generalizability and strengthen its integrity across varying 
data  distributions.  Furthermore,  deploying  the model in a 
real-time  setting  and  evaluating  it  against  live  streaming 
platform data could validate its operational value and help 
fine-tune  the  system  in  evolving  markets.  This  would 
support  the  development  of  adaptive  BI  tools  capable  of 
responding to dynamic consumer behaviors.

Table 3. Predictive Performance of Decision Tree Model

Metric

Basic

Premium

Standard

True Positive 
Rate (Recall)

0.699

0.724

0.739

Precision

0.711

0.667

0.793

F-Measure

0.705

0.694

0.765

ROC Area

0.816

0.817

0.871

that

indicating

The  data  supports  the  decision  tree  model’s 
predictive  performance  by  showing  strong  classification 
results across all subscription plans. The Standard category 
achieved  the  highest  precision  (0.793)  and  ROC  area 
(0.871), 
the  model  consistently  and 
accurately  identifies  users  in  this group. While Basic and 
Premium  had  slightly  lower  precision  scores  (0.711  and 
0.667,  respectively),  their  ROC  areas  above 0.81 suggest 
reliable overall performance in distinguishing these classes 
as well. The F-measure values (0.705 for Basic, 0.694 for 
Premium,  and  0.765  for  Standard)  reflect  a  balanced 
trade-off between precision and recall, with Standard again 
performing best.

Table 4. Confusion Matrix

basic

123

32

18

premium

standard

35

118

24

18

13

119

Table 4 shows how well the model classified each 
subscription  plan  using  a  confusion  matrix.  The  actual 
subscription  plans  are  listed  in  the  rows,  while  the 
predicted types are in the columns. Correct predictions are 
found  along  the  diagonal  of  the  matrix,  where the actual 
and  predicted  classes  match.  The  model  correctly 
identified  123  Basic,  119  Standard,  and  118  Premium 
users.  Incorrect  predictions  appear  in  the  other  cells  and 
are  fairly  evenly  spread,  indicating  that  the  model 
performed  consistently  across  the  different  subscription 
plans.  The  confusion  matrix  further  reinforces  these 
findings,  highlighting  the  model’s  balanced  and  reliable 
classification  performance  across  all  three  subscription 
plans.

CONCLUSION

This study successfully developed and validated a 
predictive  decision-tree  model  using  the J48 algorithm in 
Weka  to  classify  users  into  Basic,  Premium,  or  Standard 
subscription  plans  based  on  key  demographic  and 
behavioral  attributes.  The  model  achieved  an  overall 
accuracy of 72%, with a weighted F-measure of 0.721 and 
ROC area of 0.834, demonstrating strong predictive power 
and generalizability across unseen data.

country 
consistently  emerged  as  the  most  influential  predictor,

attributes

studied,

Among

the

---

<!-- PAGE 7 -->

References

1.  Orozco-Arias,  S.,  Piña,  J.  S.,  Tabares-Soto,  R.,  Castillo-Ossa,  L.  F.,  Guyot,  R.,  &  Isaza,  G.  (2020, May 27). Measuring 
performance  metrics  of  machine  learning  algorithms  for  detecting  and  classifying  transposable  elements.  MDPI. 
https://www.mdpi.com/2227-9717/8/6/638#:~:text=In%20ML%2C%20the%20selection%20of,because%20only%20a%20s
mall%20portion

2.  Aouad,  A.,  Elmachtoub,  A.  N.,  Ferreira,  K.  J.,  &  McNellis,  R.  (2023,  January  13). Market segmentation trees. Harvard 
School. 
Business 
https://www.hbs.edu/ris/Publication%20Files/Market%20Segmentation%20Trees_a03adc41-cbba-451c-b1be-a3e156b9fe18
.pdf

3.  Geneva.  (2023,  November  27).  New  global  connectivity  data  shows  growth,  but  divides  persist.  Press  Release. 
https://www.itu.int/en/mediacentre/Pages/PR-2023-11-27-facts-and-figures-measuring-digital-development.aspx#:~:text=Gl
obally%2C%20the%20monthly%20average%20for,only%201%20GB%20for%20mobile

4.  Patil,  D.  (2024,  November  8).  Explainable  artificial  intelligence  (XAI):  Enhancing  transparency  and  trust  in  Machine 
ResearchGate. 
Models.

Learning 
https://www.researchgate.net/publication/385629166_Explainable_Artificial_Intelligence_XAI_Enhancing_transparency_a
nd_trust_in_machine_learning_models

5.  Nasima.  (2025,  April  7).  Effective  strategies  for  handling  missing  values  in  data  analysis.  Analytics  Vidhya.

https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/

6.  Razzaq,  H.

(2017,  July  1).  Decision

for  Data  Mining.  Academia.edu. 
https://www.academia.edu/33724543/Decision_Tree_Analysis_on_J48_Algorithm_for_Data_Mining#loswp-work-container 
from

(2023).  Predictive  Modeling  Guidelines  &  Best  Practices.  Dow  Jones  Tech.  Retrieved

tree  analysis  on  J48  algorithm

7.  Hsiao,  D.

https://medium.com/dowjones/predictive-modeling-guidelines-best-practices-e99111c5588

8.  Awad, M., & Fraihat, S. (2023). Recursive Feature Elimination with Cross-Validation with Decision Tree: Feature Selection 
Method  for  Machine  Learning-Based  Intrusion  Detection  Systems.  Journal  of  Sensor  and  Actuator Networks, 12(5), 67. 
https://doi.org/10.3390/jsan12050067

9.  Manapragada, C., Webb, G. I., & Salehi, M. (2020). Emergent and unspecified behaviors in streaming decision trees. arXiv

preprint arXiv:2010.08199. https://arxiv.org/abs/2010.08199

10.  Haug, J. T., Nguyen, T. D., & Huellermeier, E. (2022). Dynamic model trees for interpretable data stream learning. arXiv

preprint arXiv:2203.10938. https://arxiv.org/abs/2203.10938

11.  Chen, H., & Zhang, L. (2023). Data-driven personalization in OTT platforms: The role of business intelligence. Journal of

Media Analytics, 7(2), 115–132. https://doi.org/10.1016/j.jma.2023.02.006

12.  Garcia,  M.,  &  Lee,  T.  (2022). Predictive analytics for churn prevention in subscription services. International Journal of

Business Intelligence, 14(3), 198–211. https://doi.org/10.1080/ijbi.2022.14.3.198

13.  Nwaimo, A., Okeke, T., & Udoh, C. (2024). Business Intelligence Applications in the Digital Economy. TechInsights Press.

https://techinsightspress.org/books/bi-digital-economy-2024

14.  Park, J., & Sullivan, B. (2023). Adaptive BI systems for real-time media consumption tracking. Information Systems Review,

19(4), 233–250. https://isrjournal.org/vol19/issue4/park-sullivan-bi-2023

15.  Huang,  J.,  &  Ling,  C.  X.  (2005).  Using  AUC  and  accuracy  in  evaluating  learning  algorithms.  IEEE  Transactions  on

Knowledge and Data Engineering, 17(3), 299–310. https://doi.org/10.1109/TKDE.2005.50

16.  Powers,  D.  M.  W.  (2011).  Evaluation:  From  precision,  recall  and  F-measure  to  ROC,  informedness,  markedness  &

correlation. Journal of Machine Learning Technologies, 2(1), 37–63. https://www.researchgate.net/publication/220766891

17.  Sokolova,  M., & Lapalme, G. (2009). A systematic analysis of performance measures for classification tasks. Information

Processing & Management, 45(4), 427–437. https://doi.org/10.1016/j.ipm.2009.03.002

18.  Wu,  X.,  Zhang,  C.,  &  Zhang,  S.  (2021).  Threshold-aware  evaluation  of  machine  learning  models  in  digital  consumer 
analytics. ACM Transactions on Intelligent Systems and Technology, 12(2), 1–20. https://dl.acm.org/doi/10.1145/3447541 
19.  Chaurasia,  V.,  &  Pal,  S.  (2019).  A  novel  approach  for  Netflix  subscription  prediction  using  data  mining  techniques.

International Journal of Computer Applications, 178(7), 14–19. https://doi.org/10.5120/ijca2019918660

20.  García-Gil, D., Luque, M., García, S., & Herrera, F. (2019). Enabling smart data: Noise filtering in big data classification.

Information Sciences, 479, 135–152. https://doi.org/10.1016/j.ins.2018.01.044

21.  Zhang, S., Yao, L., Sun, A., & Tay, Y. (2019). Deep Learning based Recommender System: A Survey and New Perspectives.

ACM Computing Surveys, 52(1), 1–38. https://doi.org/10.1145/3285029

22.  Dey,  L.,  & Haque, S. (2021). Predictive analytics in subscription-based services: A Netflix case study. Proceedings of the 
89–95.

Applications,

Conference

Intelligent

Science

Data

and

on

International 
https://doi.org/10.1007/978-981-33-4367-2_10

23.  Kim, H., Lee, J., & Park, S. (2022). Customer Churn Prediction in Influencer Commerce: An Application of Decision Trees.

International Journal of Computer Applications, 185(44), 21-27. 
www.researchgate.net/publication/367917198_Customer_Churn_Prediction_in_Influencer_Commerce_An_Application_of_
Decision_Trees?

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Technological University of the Philippines - Manila
College of Science
IT323 - Business Intelligence
WEKA-BASED DECISION-TREE MODEL FOR USER SUBSCRIPTION PLAN PREDICTION
MEMBERS:
Josef Christopher R. Guban
Christian Dayne R. Menderico
Don Marco G. Montalban
INSTRUCTOR:
Mr. Jonathan Caballero
May 22, 2025

ABSTRACT L., Sun, A., & Tay, Y., 2019). Additionally, García-Gil et
In today’s increasingly competitive streaming al. (2019) noted that preprocessing and intelligent feature
landscape, understanding user preferences in subscription selection significantly enhance model performance in large
plan selection is vital for implementing data-driven datasets—an important consideration in streaming
strategies. This study examines the impact of key platforms with millions of active users.
demographic and behavioral attributes—namely age, This study explored how user data, such as age,
gender, country, device type, and subscription start device usage, and viewing behavior, was transformed into
month—on the selection of Basic, Standard, or Premium meaningful insights using Business Intelligence tools and
plans on a major streaming platform. Utilizing a dataset of machine learning models, enabling a deeper understanding
2,500 anonymized user records, a supervised classification of the factors influencing subscription plan selection on a
model was developed and validated using the J48 streaming platform like Netflix.
decision-tree algorithm in WEKA. An 80/20 train-test split
was applied, and the model’s performance was assessed OBJECTIVES
using standard evaluation metrics, including accuracy, This study aims to derive actionable insights by evaluating
Kappa statistic, precision, recall, F-measure, and ROC user subscription behavior through data analytics.
area.
The model achieved an overall accuracy of 72%, Specific Objectives:
with country identified as the most influential predictor, 1. To develop and validate a decision‑tree model for
followed by age and device type. Results revealed accurately predicting users’ future subscription
interpretable decision rules that highlight how different plans.
user profiles correspond to specific subscription 2. To generate data-driven insights from user
preferences. For example, younger smartphone users attributes that influence subscription plan
subscribing later in the year often chose Premium plans, selection.
whereas older users on Smart TVs tended toward Standard
or Basic tiers. The decision tree effectively captured Scope
complex attribute combinations, offering clarity in This research investigates how a combination of
understanding plan selection behavior. demographic and behavioral attributes shapes
By transforming raw user data into meaningful subscription‑plan choices on an online streaming platform.
patterns, this study underscores the value of interpretable Leveraging a real‑world dataset of 2,500 anonymized user
machine learning models in generating actionable insights. records, the study focuses on five key predictors like
These insights can inform subscription plan design and country, age, gender, device type, and subscription start
targeted strategy development, illustrating the role of month to understand their joint influence on selecting
Business Intelligence in bridging user behavior with among Basic, Premium, and Standard tiers. The analysis is
platform optimization. confined to complete cases for these attributes and
employs a decision‑tree classifier to extract interpretable
CHAPTER I: INTRODUCTION rules. Performance is gauged via a percentage split of 80%
by 20%, reporting overall accuracy, Kappa statistic, error
The Problem and Its Background metrics, and class‑specific precision, recall, F‑measure,
In the ever-evolving digital entertainment and ROC area. Findings will illuminate which attribute
industry, streaming platforms such as Netflix rely heavily combinations most strongly predict each subscription
on Business Intelligence (BI) to understand their users and category, offering actionable insights for targeted
remain competitive. As user behavior becomes marketing and product design within the studied
increasingly diverse and complex, understanding the eight‑country market.
factors that influence subscription choices has become a
critical area for data-driven decision-making. While many CHAPTER II: RELATED LITERATURE
studies have explored content recommendation and user
engagement, there remains a gap in analyzing how Business Intelligence in Subscription Management
individual user attributes affect the selection of Business Intelligence (BI) tools have become
subscription plans such as Basic, Standard, or Premium. central to streaming platforms’ ability to segment users,
Consumer choices are often shaped by variables optimize offerings, and drive revenue growth. Nwaimo et
such as age, device preference, and engagement patterns. al. (2024) highlight that BI software empowers
Identifying these patterns not only improves decision‑makers to translate large volumes of user data
personalization but also supports marketing strategies, into actionable strategies, from tailoring plan features to
customer retention, and service optimization. Chaurasia forecasting subscription revenues. In the highly
and Pal (2019) emphasized that data mining techniques fragmented streaming market, platforms leverage
can uncover valuable insights into user decisions, while dashboards and reporting to track real‑time subscription
Dey and Haque (2021) highlighted the importance of uptake, detect underperforming tiers early, and reallocate
predictive analytics in understanding user behavior in marketing spend efficiently (Palani, 2025). This aligns
subscription-based platforms. with the growing use of machine learning models, such as
With the growing amount of data available from decision trees, to uncover patterns in demographic and
user interactions, machine learning and classification behavioral data, like age, gender, and device type that
models offer promising tools for predicting subscription influence subscription choices (Garcia & Lee, 2022). Chen
types and analyzing consumer trends. Effective application and Zhang (2023) further demonstrate that BI-driven user
of these models can lead to enhanced service offerings clustering enhances content delivery and subscription plan
tailored to different customer segments (Zhang, S., Yao, alignment, leading to higher retention. Park and Sullivan

(2023) also stress the strategic advantage of real-time BI user segments like Premium subscribers in streaming
dashboards in responding to shifts in user preferences platforms.
across regions and subscription tiers. These insights The inclusion of behavioral variables such as
support the analytical approach of this study, which session length, time of day, and content interaction
applied classification models to predict user subscription frequency was also shown to improve model granularity
types and guide segmentation strategies across eight and reduce classification bias. These findings translate
countries. directly to subscription-based services, where
understanding nuanced user habits can significantly
Demographic Drivers of Subscription Choice improve tier targeting.
A growing body of work examines how user
demographics (age, gender, geography, device usage) Decision‑Tree Applications in Streaming Analytics
influence plan selection. Joshi (2024) shows that younger Decision trees have seen wide adoption in
cohorts are more likely to adopt higher‑priced, streaming analytics because they produce human‑readable
multi‑device tiers, whereas older segments often remain on rules. Gomez‑Uribe & Hunt (2015) originally applied tree
basic plans. Some study highlights that demographics and models to viewer engagement, showing how splitting on
connectivity strongly influence subscription choices. One country, device type, and user tenure yields coherent
notable example is Geneva (2023) report in stark segments. In the context, J48’s ability to partition on
international gaps in broadband access and usage, it shows month of subscription start further captures seasonality in
high‐income countries average 257 GB/month per fixed plan uptake. Contrary to the notion that deep trees always
broadband subscription versus only 161 GB in overfit, recent work shows very large trees can still
low‐income countries, and 5G mobile coverage is 89% in generalize well with proper validation. For instance,
wealthy countries but nearly 0% in the least developed Aouad et al. (2023) report final decision trees with depths
country. Such disparities imply that consumers in 52–78 containing 800–4100 leaves; despite their size these
lower‐bandwidth regions (often with fewer smart TVs or models achieved superior test-set performance (e.g.
4G devices) may favor basic, lower-cost streaming plans, significant improvements in AUC and lower MSE) when
whereas users in high‑speed markets can more easily properly cross-validated. In other words, trees with
choose premium, high‑definition plans. This consistently hundreds of leaves can retain strong predictive accuracy if
proves analyses showing that regional broadband and pruned or validated, this substantiates that “trees with
device adoption patterns drive basic and premium 300+ leaves can still generalize well when properly
subscription preferences. validated. In practice, an 80/20 train-test split is commonly
employed to evaluate the performance of decision tree
Predictive Modeling of Subscription Plans models. This approach ensures that the model is trained on
Machine-learning approaches have become a substantial portion of the data while reserving a separate
essential in forecasting user subscription choices, subset for unbiased testing, thereby providing a reliable
particularly in dynamic and user-driven platforms like assessment of the model's generalization capabilities. Such
video streaming services. Among various algorithms validation strategies are crucial for developing robust
explored, Akar (2023) compares logistic regression, models that perform well on unseen data (Awad & Fraihat,
random forests, and decision trees, concluding that 2023). Emerging research also explores the adaptability of
tree-based classifiers strike an ideal balance between decision trees in streaming data contexts. Manapragada et
predictive accuracy and interpretability, an essential factor al. (2020) discuss the use of Hoeffding trees in evolving
for business stakeholders who require transparent data streams, highlighting their efficiency in real-time
decision-making processes. R. Gustavo et al. (2023) applications. Haug et al. (2022) introduce Dynamic Model
further demonstrate how feature-importance scores derived Trees for interpretable data stream learning, emphasizing
from models can drive personalized marketing campaigns, their ability to maintain flexible and robust representations
enabling companies to target users based on their most in active data concepts.
influential characteristics, such as device type or
subscription month. Patil (2024) emphasizes that Performance Metrics for Subscription Classification
explainable models like the C4.5 decision tree not only Evaluating predictive models for plan choice
boost transparency but also foster trust in automated requires both aggregate and class‑level measures. Beyond
systems by providing human-readable rules for strategic overall accuracy and the Kappa statistic, precision and
marketing. recall for each tier illuminate where a model may
Furthermore, predictive performance must meet underpredict less‑common plans (e.g., Premium).
industry reliability thresholds for practical deployment. ROC‑area analysis further quantifies discrimination power
Hsiao (2023) highlights that an accuracy of at least 70% is across thresholds (Orozco-Arias, 2020). The
considered a benchmark for commercial applications, confusion‑matrix approach provides a granular view of
ensuring the model delivers actionable and generalizable misclassification patterns, crucial for assessing revenue
insights. This is particularly important in environments impact when a high‑value user is misassigned to a lower
where misclassifying a high-value user could result in tier. As noted by Sokolova and Lapalme (2009),
substantial revenue loss. Supporting this, Kim, Lee, and multi-class performance analysis is essential when class
Park (2022) applied decision tree models in the context of imbalance affects business-critical segments. Powers
influencer-driven commerce to predict customer churn, (2011) emphasizes that relying solely on accuracy may
achieving over 80% accuracy. Their work stresses the obscure model flaws, especially in uneven class
importance of not only high overall performance, but also distributions. Similarly, Wu et al. (2021) highlight that
strong class-level precision and recall metrics that are ROC and precision-recall curves are more informative in
critical in capturing the behavior of smaller, more valuable identifying threshold-sensitive errors, particularly in

digital consumer modeling. Lastly, Huang and Ling (2005) split based on age, gender, device, and start month. In the
show that ROC analysis remains robust even under United States, Smartphone users aged ≤31 who started on
skewed class distributions, making it a reliable tool for or before May were classified as Basic (6 instances).
evaluating subscription classification systems. When starting after May and aged ≤30, users were
assigned to Premium. Older Smartphone users showed
CHAPTER III: METHODOLOGY gender-based splits: males aged 33–44 starting mid-year
were classified as Standard, while females aged ≤40 using
Research Design Smart TVs were split between Premium, Basic, or
This study adopts a quantitative, predictive Standard based on finer age and timing (2–9 instances). In
framework in which a supervised decision‑tree model (J48 Canada, male Smartphone users starting before or in July
in Weka) is used to classify users into Basic, Premium, or were mostly classified as Basic or Standard (3–21
Standard subscription plan based on their profile attributes. instances), while female Tablet users aged ≤41 starting
An 80 % by 20 % split is applied, 80 % of the data is used after May were directed to Premium (up to 9 instances).
for training the model and 20 % for independent testing, Device and start month were influential across the board.
ensuring that performance estimates reflect true All United Kingdom users, regardless of
out‑of‑sample accuracy. By structuring the work as an demographic or device, were assigned to the Standard plan
experiment in rule induction and validation, researchers (195 instances), indicating consistent behavior. In Brazil,
systematically uncover patterns in how combinations of most females and males using Tablets or Smart TVs were
country, age, gender, device type, and subscription start linked to the Basic plan, especially when starting early in
month drive plan selection. The use of an interpretable tree the year (3–23 instances), with occasional variation.
structure allows for the derivation of clear, actionable rules Australia showed two Premium-leaning segments:
that marketing and product teams can leverage. Moreover, Smartphone users aged ≤28 starting before August (4–6
framing the analysis as a controlled validation experiment instances) and older Laptop/Smart TV users starting
ensures that findings are both reliable and generalizable to mid-year (up to 18 instances). In Mexico, users aged >28
new user cohorts. were strongly associated with the Standard plan (181
instances), while younger users showed more diversity.
Data Collection and Preparation Germany’s males aged ≤33 were assigned to Basic (19
The researchers exported 2,500 anonymized user instances). Older users’ classifications varied based on
records from the streaming platform’s subscription device and start month, with Tablets leaning Basic and
database, each containing the five predictor variables and others mixed. In France, younger users and early-year
the target subscription plan. During preprocessing, Smart TV/Laptop users leaned Premium (up to 26
duplicate entries and any records with missing values were instances), while older users generally shifted toward
removed to preserve data integrity and avoid bias in model Basic, with gender and device also affecting classification.
training (Nasima, 2025). Categorical fields like country,
gender, and device type were encoded as nominal Table 1: Split Percentage Testing Summary
attributes, while the subscription start month was
Correctly Classified Instances 360 72%
formatted as an integer (1–12). Continuous variables such
as age were retained to allow the decision‑tree algorithm to
determine data‑driven split points, enhancing the model’s Incorrectly Classified Instances 140 28%
ability to capture nonlinear patterns in the data.
Kappa statistic 0.5797
Model Training and Validation
The cleaned dataset was subjected to the J48
Mean absolute error 0.2216
decision‑tree algorithm to construct a hierarchical set of
decision rules that map user attributes to subscription
Root mean squared error 0.3882
outcomes (Razzaq, 2017). To guard against overfitting and
to gauge true predictive power, the researchers employed
an 80 % by 20 % percentage split, training the model on Relative absolute error 49.86%
80 % of the records and testing it on the remaining 20 %,
while preserving class proportions in both subsets. The Root relative squared error 82.34%
study recorded overall accuracy, Kappa statistic, mean
absolute error, and root mean squared error, as well as Total Number of Instances 500
precision, recall, F‑measure, and ROC area for each
subscription category, providing a comprehensive
assessment of model performance. Finally, the resulting Table 1 summarizes the model’s performance on
confusion matrix and per‑class ROC curves were analyzed the testing set, including the total number of correct and
to pinpoint where the model excels and where further incorrect classifications, overall accuracy, and the Kappa
refinement is needed. statistic for agreement between actual and predicted
values. It also presents error-based metrics such as mean
CHAPTER IV: RESULTS AND DISCUSSION absolute error, root mean squared error, and their
respective relative errors. The total number of evaluated
Decision Tree - Classification Model instances is provided, reflecting the dataset size used for
The J48 decision tree, trained on 2,499 instances validation.
using six attributes, identified country as the most
significant predictor of subscription type. Branches further

DISCUSSION OF FINDINGS
Table 2. Identifying User Profile Combinations that Predict Specific Subscription Plans
Country Key Attributes Likely Subscription
United States Smartphone users aged ≤31, start_month ≤5 Basic
United States Smartphone users aged ≤30, start_month >5 Premium
Smart TV users (M) aged 33–44, start_month
United States Standard
5–9
Smart TV users (F) aged ≤40, start_month
United States Premium or Basic
≤10
Canada Male Smartphone users, start_month ≤7 Standard or Basic
Female Tablet users aged ≤41, start_month
Canada Premium
>5
All users regardless of demographics or
United Kingdom Standard
device
Most females and males using Smart
Brazil Basic
TVs/Tablets
Australia Smartphone users aged ≤28, start_month ≤8 Premium
Laptop or Smart TV users aged >35,
Australia Premium
start_month mid-year
Mexico Users aged >28 Standard
Germany Males aged ≤33 Basic
Germany Older males on various devices Mixed
Younger users and Smart TV/Laptop users,
France Premium
early start_month
The decision tree reveals that subscription plan dominant trend toward the Basic plan is seen among
selection is strongly influenced by a combination of females and Smart TV or Tablet users, particularly with
country, age, device, gender, and start month. In the United early-year subscriptions, suggesting that affordability and
States, the model shows a nuanced segmentation: accessibility are key decision factors. In Australia, two
Smartphone users aged 31 and below tend to choose the distinct Premium segments emerge: younger Smartphone
Basic plan if they subscribe early in the year (start_month users (aged ≤28) starting before August, and older users
≤ 5), but shift toward Premium when subscribing later using Smart TVs or Laptops, especially mid-year. This
(start_month > 5). The preferences of Smart TV users indicates dual targeting strategies based on age and device
further segment by gender and age. Females aged 40 and sophistication. In Mexico, the primary determinant is age;
below alternate between Basic and Premium, depending users older than 28 are strongly associated with the
on exact age and start month, while males aged 33 to 44 Standard plan regardless of device, simplifying
often align with the Standard plan, particularly in the segmentation efforts. Meanwhile, Germany presents
mid-year period. These findings illustrate that subscription age-divided behavior: younger males (≤33) prefer Basic,
behavior in the U.S. varies with time, age, and access but older users show mixed preferences that vary with both
device, allowing precise targeting strategies that match device and subscription timing. France demonstrates a
subscription plan with user lifecycle stages. stronger lean toward Premium among younger users and
In Canada, the decision rules highlight that male Smart TV or Laptop users, especially when subscribing
Smartphone users who start their subscription before July early in the year, while older users transition toward Basic.
typically fall into Standard or Basic, while female Tablet Overall, the decision tree structure confirms that
users aged 41 and below tend to choose Premium when user subscription behavior is shaped by complex
starting after May. This underlines the relevance of device combinations of demographic and behavioral variables,
type and seasonal timing in Canadian market fulfilling the study's first objective. The insights derived
segmentation. In contrast, the United Kingdom shows a from the model provide a granular understanding of how
highly uniform trend: regardless of user age, gender, or different segments respond to service offerings, enabling
device, all users fall into the Standard tier. This data-driven recommendations for targeted acquisition and
homogeneity enables simplified campaigns focused solely retention strategies. These patterns, identified across
on promoting the Standard plan’s features without need for markets, present actionable frameworks for subscription
personalization. platforms aiming to optimize user engagement through
Other markets exhibit stronger correlations with tailored plan offerings.
price sensitivity and device preference. In Brazil, a

Table 3. Predictive Performance of Decision Tree Model  followed by age, device type, gender, and subscription
Metric  Basic  Premium  Standard  start  month.  The  classification  tree  revealed  that user
preferences are shaped by multi-factor combinations rather
True Positive  than isolated variables. For instance, the same age group
|     |     |     | 0.699  |     | 0.724  |     | 0.739  |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- |
Rate (Recall)
may exhibit differing plan preferences based on device
usage or start timing, depending on the regional context.
This confirms the complexity of user decision-making and
|     | Precision  |     | 0.711  |     | 0.667  |     | 0.793  |             |      |          |          |     |                      |
| --- | ---------- | --- | ------ | --- | ------ | --- | ------ | ----------- | ---- | -------- | -------- | --- | -------------------- |
|     |            |     |        |     |        |     |        | highlights  | the  | model's  | ability  | to  | reflect  real-world  |
behavioral diversity.
F-Measure  0.705  0.694  0.765  The  findings  affirm  that  machine  learning
models, particularly interpretable ones like decision trees,
can offer granular insights into subscriber segmentation,
|     | ROC Area  |     | 0.816  |     | 0.817  |     | 0.871  |     |     |     |     |     |     |
| --- | --------- | --- | ------ | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- |
enabling streaming platforms to design targeted marketing
|     |     |            |           |     |                |       |          | strategies,  | adjust  | pricing    | tiers,   | and      | enhance  user  |
| --- | --- | ---------- | --------- | --- | -------------- | ----- | -------- | ------------ | ------- | ---------- | -------- | -------- | -------------- |
|     |     |            |           |     |                |       |          | acquisition  | and     | retention  | efforts  | through  | proactive,     |
|     |     | The  data  | supports  |     | the  decision  | tree  | model’s  |              |         |            |          |          |                |
data-driven personalization.
predictive performance by showing strong classification

results across all subscription plans. The Standard category
RECOMMENDATION
| achieved  |     | the  highest  | precision  |     | (0.793)  | and ROC area  |     |     |     |     |     |     |     |
| --------- | --- | ------------- | ---------- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
While the model demonstrated solid performance,
| (0.871),  |     | indicating  | that  | the  | model  | consistently  | and  |     |     |     |     |     |     |
| --------- | --- | ----------- | ----- | ---- | ------ | ------------- | ---- | --- | --- | --- | --- | --- | --- |
several  areas offer opportunities for enhancement. The
accurately identifies users in this group. While Basic and  dataset  was  limited  to  five  user  attributes,  excluding
Premium had slightly lower precision scores (0.711 and
|     |     |     |     |     |     |     |     | behavioral  | indicators  |     | such  | as  watch  | time,  session  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ----- | ---------- | --------------- |
0.667, respectively), their ROC areas above 0.81 suggest
frequency, or genre preferences, which may further refine
reliable overall performance in distinguishing these classes  prediction accuracy. Future research should incorporate
as well. The F-measure values (0.705 for Basic, 0.694 for
these variables to capture a broader behavioral context.
| Premium,  |     | and  0.765  | for  | Standard)  | reflect  |     | a  balanced  |     |     |     |     |     |     |
| --------- | --- | ----------- | ---- | ---------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
While the J48 decision tree provided interpretable and
trade-off between precision and recall, with Standard again
|     |     |     |     |     |     |     |     | effective  | results,  | exploring  |     | ensemble  | methods  like  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ---------- | --- | --------- | -------------- |
performing best.
Random Forests or Gradient Boosted Trees could improve
predictive robustness and reduce overfitting. These models
Table 4. Confusion Matrix
may capture complex nonlinear interactions that a single
tree might miss, especially in regions with more diverse or
|     | basic  |     |     | premium  |     | standard  |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
ambiguous subscription patterns. It is also recommended
|     |      |     |     |     |     |     |     | to  test  | the  model  | on  | a  different dataset to assess its  |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ----------------------------------- | --- | --- |
|     | 123  |     |     | 35  |     |     | 18  |           |             |     |                                     |     |     |
generalizability and strengthen its integrity across varying
32  118  13  data distributions. Furthermore, deploying the model in a
real-time setting and evaluating it against live streaming
platform data could validate its operational value and help
|     | 18  |     |     | 24  |     |     | 119  |                                                          |              |     |                                  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------------------------------------------------------- | ------------ | --- | -------------------------------- | --- | --- |
|     |     |     |     |     |     |     |      | fine-tune                                                | the  system  |     | in evolving markets. This would  |     |     |
|     |     |     |     |     |     |     |      | support the development of adaptive BI tools capable of  |              |     |                                  |     |     |
Table 4 shows how well the model classified each  responding to dynamic consumer behaviors.
| subscription plan using a confusion matrix. The actual       |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| ------------------------------------------------------------ | ---------- | -------------------------------------------------- | -------- | -------------------------------- | ----------------------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- |
| subscription                                                 |            | plans                                              | are      | listed                           | in  the                 | rows,        | while  the   |     |     |     |     |     |     |
| predicted types are in the columns. Correct predictions are  |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| found along the diagonal of the matrix, where the actual     |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| and                                                          | predicted  |                                                    | classes  | match.                           | The                     | model        | correctly    |     |     |     |     |     |     |
| identified                                                   |            | 123  Basic, 119 Standard, and 118 Premium          |          |                                  |                         |              |              |     |     |     |     |     |     |
| users. Incorrect predictions appear in the other cells and   |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| are                                                          | fairly     | evenly                                             | spread,  | indicating                       |                         | that         | the  model   |     |     |     |     |     |     |
| performed consistently across the different subscription     |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| plans.                                                       | The        | confusion                                          |          | matrix                           | further                 | reinforces   | these        |     |     |     |     |     |     |
| findings, highlighting the model’s balanced and reliable     |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| classification                                               |            | performance                                        |          | across                           | all three subscription  |              |              |     |     |     |     |     |     |
| plans.                                                       |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
|                                                              |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| CONCLUSION                                                   |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
|                                                              |            | This study successfully developed and validated a  |          |                                  |                         |              |              |     |     |     |     |     |     |
| predictive decision-tree model using the J48 algorithm in    |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| Weka to classify users into Basic, Premium, or Standard      |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| subscription                                                 |            | plans                                              | based    | on                               | key                     | demographic  | and          |     |     |     |     |     |     |
| behavioral                                                   |            | attributes.                                        |          | The  model                       | achieved                |              | an  overall  |     |     |     |     |     |     |
| accuracy of 72%, with a weighted F-measure of 0.721 and      |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| ROC area of 0.834, demonstrating strong predictive power     |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
| and generalizability across unseen data.                     |            |                                                    |          |                                  |                         |              |              |     |     |     |     |     |     |
|                                                              |            | Among                                              | the      | attributes                       |                         | studied,     | country      |     |     |     |     |     |     |
| consistently                                                 |            | emerged                                            | as       | the most influential predictor,  |                         |              |              |     |     |     |     |     |     |

References
1. Orozco-Arias, S., Piña, J. S., Tabares-Soto, R., Castillo-Ossa, L. F., Guyot, R., & Isaza, G. (2020, May 27). Measuring
performance metrics of machine learning algorithms for detecting and classifying transposable elements. MDPI.
https://www.mdpi.com/2227-9717/8/6/638#:~:text=In%20ML%2C%20the%20selection%20of,because%20only%20a%20s
mall%20portion
2. Aouad, A., Elmachtoub, A. N., Ferreira, K. J., & McNellis, R. (2023, January 13). Market segmentation trees. Harvard
Business School.
https://www.hbs.edu/ris/Publication%20Files/Market%20Segmentation%20Trees_a03adc41-cbba-451c-b1be-a3e156b9fe18
.pdf
3. Geneva. (2023, November 27). New global connectivity data shows growth, but divides persist. Press Release.
https://www.itu.int/en/mediacentre/Pages/PR-2023-11-27-facts-and-figures-measuring-digital-development.aspx#:~:text=Gl
obally%2C%20the%20monthly%20average%20for,only%201%20GB%20for%20mobile
4. Patil, D. (2024, November 8). Explainable artificial intelligence (XAI): Enhancing transparency and trust in Machine
Learning Models. ResearchGate.
https://www.researchgate.net/publication/385629166_Explainable_Artificial_Intelligence_XAI_Enhancing_transparency_a
nd_trust_in_machine_learning_models
5. Nasima. (2025, April 7). Effective strategies for handling missing values in data analysis. Analytics Vidhya.
https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/
6. Razzaq, H. (2017, July 1). Decision tree analysis on J48 algorithm for Data Mining. Academia.edu.
https://www.academia.edu/33724543/Decision_Tree_Analysis_on_J48_Algorithm_for_Data_Mining#loswp-work-container
7. Hsiao, D. (2023). Predictive Modeling Guidelines & Best Practices. Dow Jones Tech. Retrieved from
https://medium.com/dowjones/predictive-modeling-guidelines-best-practices-e99111c5588
8. Awad, M., & Fraihat, S. (2023). Recursive Feature Elimination with Cross-Validation with Decision Tree: Feature Selection
Method for Machine Learning-Based Intrusion Detection Systems. Journal of Sensor and Actuator Networks, 12(5), 67.
https://doi.org/10.3390/jsan12050067
9. Manapragada, C., Webb, G. I., & Salehi, M. (2020). Emergent and unspecified behaviors in streaming decision trees. arXiv
preprint arXiv:2010.08199. https://arxiv.org/abs/2010.08199
10. Haug, J. T., Nguyen, T. D., & Huellermeier, E. (2022). Dynamic model trees for interpretable data stream learning. arXiv
preprint arXiv:2203.10938. https://arxiv.org/abs/2203.10938
11. Chen, H., & Zhang, L. (2023). Data-driven personalization in OTT platforms: The role of business intelligence. Journal of
Media Analytics, 7(2), 115–132. https://doi.org/10.1016/j.jma.2023.02.006
12. Garcia, M., & Lee, T. (2022). Predictive analytics for churn prevention in subscription services. International Journal of
Business Intelligence, 14(3), 198–211. https://doi.org/10.1080/ijbi.2022.14.3.198
13. Nwaimo, A., Okeke, T., & Udoh, C. (2024). Business Intelligence Applications in the Digital Economy. TechInsights Press.
https://techinsightspress.org/books/bi-digital-economy-2024
14. Park, J., & Sullivan, B. (2023). Adaptive BI systems for real-time media consumption tracking. Information Systems Review,
19(4), 233–250. https://isrjournal.org/vol19/issue4/park-sullivan-bi-2023
15. Huang, J., & Ling, C. X. (2005). Using AUC and accuracy in evaluating learning algorithms. IEEE Transactions on
Knowledge and Data Engineering, 17(3), 299–310. https://doi.org/10.1109/TKDE.2005.50
16. Powers, D. M. W. (2011). Evaluation: From precision, recall and F-measure to ROC, informedness, markedness &
correlation. Journal of Machine Learning Technologies, 2(1), 37–63. https://www.researchgate.net/publication/220766891
17. Sokolova, M., & Lapalme, G. (2009). A systematic analysis of performance measures for classification tasks. Information
Processing & Management, 45(4), 427–437. https://doi.org/10.1016/j.ipm.2009.03.002
18. Wu, X., Zhang, C., & Zhang, S. (2021). Threshold-aware evaluation of machine learning models in digital consumer
analytics. ACM Transactions on Intelligent Systems and Technology, 12(2), 1–20. https://dl.acm.org/doi/10.1145/3447541
19. Chaurasia, V., & Pal, S. (2019). A novel approach for Netflix subscription prediction using data mining techniques.
International Journal of Computer Applications, 178(7), 14–19. https://doi.org/10.5120/ijca2019918660
20. García-Gil, D., Luque, M., García, S., & Herrera, F. (2019). Enabling smart data: Noise filtering in big data classification.
Information Sciences, 479, 135–152. https://doi.org/10.1016/j.ins.2018.01.044
21. Zhang, S., Yao, L., Sun, A., & Tay, Y. (2019). Deep Learning based Recommender System: A Survey and New Perspectives.
ACM Computing Surveys, 52(1), 1–38. https://doi.org/10.1145/3285029
22. Dey, L., & Haque, S. (2021). Predictive analytics in subscription-based services: A Netflix case study. Proceedings of the
International Conference on Data Science and Intelligent Applications, 89–95.
https://doi.org/10.1007/978-981-33-4367-2_10
23. Kim, H., Lee, J., & Park, S. (2022). Customer Churn Prediction in Influencer Commerce: An Application of Decision Trees.
International Journal of Computer Applications, 185(44), 21-27.
www.researchgate.net/publication/367917198_Customer_Churn_Prediction_in_Influencer_Commerce_An_Application_of_
Decision_Trees?