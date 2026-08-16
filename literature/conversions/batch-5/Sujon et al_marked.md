---
conversion_metadata:
  converted_at: "2026-07-21T08:51:47Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Sujon et al.pdf"
  source_pdf_sha256: "056bd769441ff961955756636fb9c9c02c5e80c4e6c0736be0197d9f004d39ee"
  page_count: 45
  markdown_char_count: 252024
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Sujon et al. Journal of Big Data          (2025) 12:268 
https://doi.org/10.1186/s40537-025-01313-4

Journal of Big Data

Accuracy, precision, recall, f1-score, or MCC? 
empirical evidence from advanced statistics, 
ML, and XAI for evaluating business predictive 
models
Khaled Mahmud Sujon1, Rohayanti Hassan2, Kwonhue Choi3* and Md Abdus Samad3*

*Correspondence:
Kwonhue Choi
gonew@yu.ac.kr
Md Abdus Samad
masamad@yu.ac.kr
1Department of Software 
Engineering, Universiti Teknologi 
Malaysia (UTM), Johor Bahru,  
Johor 81310, Malaysia
2Faculty of Computing, Universiti 
Teknologi Malaysia (UTM), Johor 
Bahru, Johor 81310, Malaysia
3Department of Information and 
Communication Engineering, 
Yeungnam University,  
Gyeongsan 38541, South Korea

Abstract
Imbalanced datasets pose a persistent challenge in business data mining, particularly 
in high-stakes domains such as financial risk prediction and customer churn analysis, 
where the minority class often carries disproportionate operational and financial 
consequences. Although widely used evaluation metrics–such as accuracy, precision, 
recall, F1-score, and Matthews Correlation Coefficient (MCC)–are commonly applied 
in practice, there remains no empirical consensus on which metric offers the most 
reliable performance under real-world conditions. Existing studies lack a unified, 
statistically validated framework that accounts for threshold sensitivity, input noise, 
and interpretability–factors critical to business decision-making. To address this gap, 
we present a comprehensive and statistically rigorous evaluation of performance 
metrics for imbalanced business classification tasks. Using two benchmark datasets 
with distinct sizes and imbalance ratios–the Default of Credit Card Clients dataset 
and the Telco Customer Churn dataset–we evaluate five commonly used machine 
learning models: Logistic Regression (LR), Decision Tree (DT), Random Forest 
(RF), Extreme Gradient Boosting (XGBoost), and k-Nearest Neighbors (KNN). Our 
methodology incorporates static and dynamic threshold analysis, Gaussian noise 
robustness testing, bootstrap confidence intervals, McNemar’s test, Cohen’s kappa, 
and analysis of variance (ANOVA) to assess the statistical reliability of performance 
metrics. In addition, we introduce a novel two-stage explainable artificial intelligence 
(XAI) framework using SHapley Additive exPlanations (SHAP). The first stage 
employs standard SHAP visualizations (bar and beeswarm plots) to ensure baseline 
interpretability. The second stage extends this with a novel 3D metric-conditioned 
SHAP analysis, linking feature contributions to variations in classification thresholds 
and evaluation metrics. Our findings show that the F1-score consistently provides 
the most stable and balanced evaluation across datasets and testing conditions, with 
MCC offering complementary diagnostic value. In contrast, accuracy and precision 
demonstrate limited robustness under class imbalance. By combining statistical rigor 
with interpretable AI, this study offers the most comprehensive guidance to date for

© The Author(s) 2025. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International 
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate 
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. 
You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party 
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material 
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted 
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : /  / c r e a  t i v e c o  m m o n  s . o r g  / l i c e  n s 
e s / b  y - n c  - n d / 4 . 0 /.

---

<!-- PAGE 2 -->

Page 2 of 45

selecting performance metrics in imbalanced business classification, with practical 
implications for model deployment in finance, marketing, and customer analytics.

Keywords  Business, Data mining, Machine learning, Imbalanced datasets, Explainable 
AI (XAI), Statistics, Accuracy, Precision, F1, MCC

Introduction

In  contemporary  business  environments,  leveraging  machine  learning  (ML)  for  deci-
sion-making  has  become  indispensable.  Applications  in  customer  churn  prediction, 
fraud  detection,  and  financial  credit  scoring  often  rely  on  predictive  models  trained 
on  real-world  datasets  [1].  However,  such  datasets  are  frequently  imbalanced,  where 
instances of one class significantly outnumber the other. This imbalance poses substan-
tial  challenges  to  model  performance  and  evaluation,  as  standard  accuracy-focused 
metrics fail to adequately assess predictive power across classes. Metrics like precision, 
recall,  and  MCC  are  better  suited  to  these  scenarios  but  are  underutilized  in  business 
data  mining  applications  [2].  Consequently,  addressing  imbalances  effectively  while 
optimizing performance metrics is critical for deploying reliable ML models in business 
settings.  Existing  studies  have  advanced  our  understanding  of  metric  applicability  but 
have significant limitations. For instance, [3] demonstrated the inadequacies of accuracy 
in  imbalanced  datasets  but  did  not  explore  alternative  metrics  in  depth.  Similarly,  [4] 
advocated the use of MCC for binary classification but lacked a comparative evaluation 
of MCC against other metrics like F1-score and precision. [5] optimized oversampling 
techniques for imbalanced data but neglected to consider dynamic thresholds or noise 
robustness. Moreover, [6] demonstrated the potential of oversampling for yield estima-
tion in industrial applications but did not extend their methodology to broader business 
datasets.  Finally,  [7]  highlighted  the  effectiveness  of  Area  Under  the  Precision-Recall 
Curve (AUPRC) optimization for imbalanced datasets but did not integrate explainable 
AI (XAI) tools to interpret model outputs. Despite these advances in the current litera-
ture, several gaps remain. First, a comprehensive evaluation of many performance indi-
cators encompassing accuracy, precision, recall, F1, and MCC is still unexplored in the 
business  domain.  Second,  the  implementation  of  advanced  statistical  techniques,  such 
as  ANOVA  and  McNemar’s  tests,  for  optimal  metric  selection  is  still  underexplored. 
Second,  the  implementation  of  dynamic  and  static  threshold  sensitivity  analysis  has 
not  been  systematically  examined  in  business  data  mining.  Third,  while  noise  robust-
ness  testing  has  gained  traction  in  other  domains,  its  application  to  metric  evaluation 
in business data mining remains completely unexplored. Lastly, the implementation of 
XAI techniques like SHAP for metric-based feature impact analysis is still unexplored in 
current literature of business data mining. To address the identified gaps in the current 
literature on business data mining under class imbalance, the key contributions of our 
study are as follows:

• We  conduct  a  comprehensive  statistical  validation  of  five  most  commonly  used 
performance  metrics  using  ANOVA,  McNemar’s  test,  and  bootstrap  confidence 
intervals to quantify both inter-metric and inter-model differences under imbalanced 
conditions.

---

<!-- PAGE 3 -->

Page 3 of 45

• We  implement  both  static  and  dynamic  threshold  sensitivity  analyses  to  examine 
how classification thresholds affect each metric, providing a nuanced understanding 
of threshold dependence.

• We evaluate the robustness of performance metrics under varying levels of synthetic 
noise to simulate real-world data imperfections, identifying metrics most resilient to 
instability.

• We  introduce  a  novel  two-stage  explainable  AI  (XAI)  framework  using  SHAP. The 
first stage applies conventional SHAP plots for global and local interpretability, while 
the  second  leverages  3D  metric-conditioned  SHAP  visualizations  to  reveal  how 
feature importance interacts with threshold variation and metric outcomes.

To shed light on the above-mentioned contributions, our investigation is guided by the 
following research questions (RQs):

• RQ1: Which performance metrics among accuracy, precision, recall, F1-score, and 
MCC provide the most reliable evaluation for imbalanced classification in business 
domains?

• RQ2:  How  do  static  and  dynamic  threshold  sensitivity  analyses  impact  metric 
outcomes, and how can they be used to determine optimal decision boundaries?
  • RQ3: How can advanced statistical methods such as ANOVA, McNemar’s test, and 
bootstrap confidence intervals be used to validate and compare metric robustness?
  • RQ4: How does input noise affect the stability of different metrics, and which metric

remains most resilient under noisy, real-world business conditions?

• RQ5: How can explainable AI techniques like SHAP help interpret metric behavior 
across  features  and  thresholds,  and  what  actionable  insights  do  they  provide  for 
model evaluation?

The  reminder  sections  of  this  manuscript  are  structured  as  follows:  Section  Literature 
Review  reviews  related  work,  highlighting  gaps  in  the  literature.  Section  Methodol-
ogy details the methodology, including dataset preprocessing, modeling, and analytical 
techniques.  Section  Experimental  Results  presents  the  experimental  results,  integrat-
ing  statistical  insights  with  XAI  findings.  Section  Discussion  presents  the  discussion 
and  limitations.  Finally,  Section  Conclusion  outlines  conclusions  and  proposes  future 
research  directions.  With  the  problem  clearly  defined  in  the  introduction,  we  now 
review  the  related  literature  to  identify  prevailing  methodologies  and  highlight  unre-
solved questions.

Literature review

Imbalanced  datasets  pose  a  persistent  challenge  in  business  data  mining,  especially  in 
high-stakes domains such as credit risk, churn prediction, and fraud detection. In these 
settings,  minority  classes  often  represent  critical  outcomes  such  as  defaults,  cancella-
tions, and anomalies, yet their underrepresentation leads to biased models and distorted 
performance  evaluations  [8].  Traditional  metrics  like  accuracy  frequently  fail  under 
such conditions, as highlighted by [9] and empirically supported by [10], both of whom 
recommend alternatives like F1-score and MCC for more balanced evaluation. To miti-
gate sampling bias, [11] proposed one-sided selection, while [12] confirmed MCC and 
F1-score as the most stable across varying imbalance ratios in health data.

---

<!-- PAGE 4 -->

Page 4 of 45

Despite  this,  many  domain-specific  studies  still  rely  on  suboptimal  practices.  For 
example,  [13]  evaluated  fraud  detection  using  AUC  and  precision  alone,  without  sta-
tistical  or  explainability  validation,  typifying  a  broader  trend  where  metric  selection  is 
assumed rather than empirically supported. Similarly, studies like [14–17] rely solely on 
accuracy, while others such as [18–20] focus only on precision or recall, omitting met-
rics like MCC and F1 and lacking any statistical or explainability analysis.

Even  among  works  using  more  robust  metrics–such  as  [21]  (F1,  AUC),  [22–24] 
(MCC)–comparative  analysis  and  validation  remain  absent.  Recent  applications  in 
churn prediction and financial modeling [25–28] likewise neglect optimal metric selec-
tion,  threshold  sensitivity,  and  interpretability  via  XAI.  [29]  evaluated  metrics  such  as 
MCC and G-Mean in software defect prediction tasks, finding them to be more robust 
than accuracy or AUC. However, the study did not include threshold-based evaluation 
or  any  explainability  component.  A  simulation-based  comparison  by  [30]  further  ana-
lyzed twelve metrics, including MCC and Cohen’s Kappa, highlighting the superior reli-
ability of MCC under imbalance but lacking any XAI integration. Additional works such 
as [27, 28] use multiple metrics (MCC, AUC) but omit statistical or interpretability vali-
dation. Foundational works like [31, 32] discuss ROC limitations and metric bias but do 
not explore metric interactions or XAI.

In  contrast,  explainable  AI  (XAI)  has  increasingly  gained  attention  for  enhancing 
model  transparency  in  high-stakes  domains.  For  example,  [33]  integrated  SHAP  with 
embedded feature selection in electricity demand forecasting, demonstrating its value in 
improving interpretability. [34] proposed a novel metric to validate SHAP-based expla-
nations in time series forecasting, while [35] showcased SHAP’s applicability in health-
care for sleep apnea prediction. Additionally, [36] provided a comprehensive taxonomy 
of XAI evaluation techniques, though they noted the lack of standardized metrics and 
real-world  validations.  Despite  these  advancements,  existing  studies  often  treat  SHAP 
explanations and metric evaluation as separate concerns.

Unlike the study by [37], who examined the consistency of four metrics (AUC, F-mea-
sure, G-mean, MCC) under varying imbalance ratios using correlation and simulation, 
our study extends far beyond theoretical consistency analysis. We evaluate five metrics 
across real-world business datasets using rigorous statistical tests (ANOVA, McNemar’s 
test,  bootstrap  CI),  incorporate  static  and  dynamic  threshold  sensitivity  analysis,  and 
assess metric robustness under input noise. Whereas their analysis considered metrics 
in  isolation,  our  framework  explores  how  metric  behavior  evolves  across  model  types, 
input  noise,  threshold  dynamics,  and  explainability  layers.  Most  notably,  we  introduce 
a novel two-stage XAI framework, culminating in 3D metric-conditioned SHAP visual-
izations that link feature contributions to metric behavior across thresholds. Our work 
provides a unified, statistically grounded, threshold-aware, and explainability-enhanced 
approach to performance evaluation, offering greater practical utility than existing con-
sistency-focused studies.

The limitations of existing business studies in handling metric evaluation under class 
imbalance  are  summarized  in  Table  1,  while  Table  2  presents  recent  studies  focusing 
on evaluation metrics and explainability under imbalanced learning. Collectively, these 
studies  underscore  the  absence  of  a  unified,  statistically  validated,  and  explainability-
aware framework for evaluating performance metrics under class imbalance. To bridge 
this  gap,  we  evaluate  five  machine  learning  models  on  two  real-world  imbalanced

---

<!-- PAGE 5 -->

Page 5 of 45

Table 1  Empirical business studies using evaluation metrics under class imbalance and identified 
gaps
Ref.

Metric used Model used

Identified gap

Business dataset 
used
Fraud detection

[13]

[14]

Real-world datasets

AUC, 
precision
Accuracy

[21]

Marketing datasets

F1, AUC

[18]

Business performance Precision,

[19]

Financial datasets

recall
Precision

AdaBoost

No statistical validation or XAI

Ensemble learning Only accuracy used, no metric compari-
son or validation
No comparative analysis or statistical 
validation
Ignored MCC/F1, no statistical analysis

Evolutionary 
methods
Decision Trees

Neural networks

Precision only; no comparison, no 
validation

[15]

MBA student data

Accuracy

Ensemble learning Accuracy only; no metric selection

[22]

Banking datasets

MCC

[23]
 [17]
 [16]
 [20]
 [24]
 [25]
 [28]
 [26]
 [27]

MCC
F1

Financial datasets
Insurance datasets
Financial transactions Accuracy
Bankruptcy datasets
Credit scoring
Churn prediction
Business datasets
Churn prediction
Churn evaluation

Recall
F1
MCC
AUC
F1, G-Mean
MCC, AUC

Complexity-based 
classifiers
GANs
AdaBoost
Spark + SVM
SVM
RNS classifiers
Ensemble models
Boosting models
Hybrid ensemble
Multiple classifiers

analysis
No XAI or comparative metric analysis

Only MCC; no validation or explainability
No statistical validation
Accuracy only; ignores threshold/XAI
Recall only; no comparative or XAI analysis
No statistical or XAI validation
No comparison or explainability
No metric selection or validation
No comparative metric analysis; no XAI
No statistical methods or XAI applied

Table 2  Recent studies on metric evaluation and XAI under imbalanced learning
Ref.

Identified gap

Domain

Stat.?

XAI?

Metric
focus
Accuracy, F1, MCC
Accuracy, F1, ROC, MCC

General
General

General
Health data
General
General

Sampling, recall
Balanced Acc., MCC, F1
ROC
MCC, ROC

MCC, G-Mean

Software 
defects
General

12 metrics incl. MCC, Kappa ✗

[37]

General

AUC, F-measure, G-mean, 
MCC
SHAP + Feature selection

Electricity 
demand
Time series Metric for SHAP validation ✓
Healthcare
✓
General
✓

SHAP + Risk prediction
Taxonomy of XAI metrics

✓

[9]
 [10]

[11]
 [12]
 [31]
 [32]

[29]

[30]

[33]

[34]
 [35]
 [36]

✗
✗

✗
✗
✗
✗

✗

✗

✗

✓

✗

✓
✗

✓

✓

✓

✓

✗

✗
✗
✗

Conceptual, not empirical comparison
Compared metrics across domains; lacks 
business/XAI focus
Sampling-focused, not metric evaluation
No XAI or threshold variation
Lacks imbalance-specific insight
Focused on bias correction, not metric 
interaction
No threshold or explainability analysis

Lacks XAI and threshold-dependent 
behavior
Theoretical consistency only; no XAI or 
dynamic threshold
Lacks metric integration

Does not compare traditional metrics
SHAP only; no metric linkage
Review only; lacks experimental grounding

datasets–Default  of  Credit  Card  Clients  and  Telco  Customer  Churn–using  a  compre-
hensive  methodology  that  includes  ANOVA,  McNemar’s  test,  bootstrap  confidence 
intervals, threshold sensitivity analysis, noise robustness testing, and a novel two-stage 
SHAP-based  XAI  approach.  The  first  stage  applies  conventional  SHAP  visualizations 
(bar plots and beeswarm plots) for baseline interpretability using LR, while the second

---

<!-- PAGE 6 -->

Page 6 of 45

introduces 3D metric-conditioned SHAP analysis to explore how feature contributions 
vary across thresholds and relate to performance metrics. This is the first study to jointly 
analyze performance metrics across statistical, algorithmic, and interpretability dimen-
sions, offering a generalizable and practitioner-oriented framework for metric selection 
in imbalanced business classification tasks.

Methodology

In  this  section  the  study  presents  the  methodology  of  our  investigation.  The  method-
ology  of  our  study  is  designed  to  systematically  evaluate  and  select  the  optimal  per-
formance  metric  for  machine  learning  models  applied  to  business  data  mining,  with 
the  focus  on  a  large  imbalanced  Business  datasets.  To  conduct  a  detailed  analysis  this 
research  adopts  a  multi-faceted  analytical  framework  integrating  machine  learning, 
advanced statistical techniques, and explainable AI (XAI). Figure 1 presents the research 
framework of our investigation containing all the phases adopted in this analysis.

Data preparation and preprocessing

The dataset used in this study is the “Default of Credit Card Clients” dataset collected 
from UCI Machine Learning, available at the URL1, which consists of 30,000 instances 
and 23 features. It contains data from a Taiwanese bank’s credit card clients, specifically 
used to predict whether clients will default on their credit card payments. The features 
include  demographic  information,  credit-related  variables  and  payment  amounts  for 
six  months,  and  the  binary  target  variable  indicating  whether  a  client  defaulted  in  the 
following month. Specifically, the target variable is denoted as DEFAULT_PAYMENT_
NEXT_MONTH, where 1 represents default and 0 indicates no default. The features are

Fig. 1  Proposed research framework for selecting the best metric

1  h t t p s :  / / a r c  h i v e . i  c s . u  c i . e d  u / d a t  a s e t / 3  5 0 / d  e f a u l t + o f + c r e d i t + c a r d + c l i e n t s

---

<!-- PAGE 7 -->

Page 7 of 45

Table 3  Feature summary and descriptions
Feature Name
ID, SEX, EDUCA-
TION, MARRIAGE

Type
Categorical

LIMIT_BAL, AGE
PAY_0 to PAY_6

Numeric
Categorical

BILL_AMT1 to 
BILL_AMT6
PAY_AMT1 to 
PAY_AMT6
DEFAULT_PAY-
MENT
_NEXT_MONTH

Numeric

Numeric

Categorical

Note
ID: Unique identifier for each client. SEX: Gender of the client (Male/
Female). EDUCATION: Education level (1: Graduate school, 2: University, 
3: High school, 4: Others). MARRIAGE: Marital status (1: Married, 2: Single, 
3: Others).
LIMIT_BAL: Credit limit in the credit card account. AGE: Age of the client.
PAY_0 to PAY_6: Payment status for the last 6 months, where 0 means 
no delay and 1–9 indicates the number of months the payment was 
delayed. (Months: September 2005 to February 2005).
BILL_AMT1 to BILL_AMT6: Bill statement amounts for the last 6 months 
(Months: September 2005 to February 2005).
PAY_AMT1 to PAY_AMT6: Amount paid for the last 6 months (Months: 
September 2005 to February 2005).
DEFAULT_PAYMENT_NEXT_MONTH: Whether the client defaulted on 
the payment in the next month (1: Default, 0: No default).

Fig. 2  Class distribution with the imbalanced dataset

a mix of categorical and numerical variables. We provide a summary of the features and 
their respective types in Table 3. The distribution of the target variable of the dataset is 
presented  in  Figure  2,  which  demonstrates  the  imbalanced  nature  of  the  dataset.  The 
dataset  was  initially  examined  for  missing  values,  inconsistencies,  and  anomalies.  Fea-
tures with missing values were imputed to ensure the integrity of our selected dataset. 
For  categorical  features  such  as  education  and  marital  status,  we  converted  them  into 
numerical features using the hot encoder method.

Additional dataset

To  further  enhance  the  generalizability  of  our  findings,  we  extended  our  experiments 
to  another  dataset.  The  second  dataset  employed  in  this  study  is  the  Telco  Customer 
Churn dataset, sourced from Kaggle and available at the URL2. This dataset comprises 
7,043  instances  and  more  than  20  features,  collected  from  a  telecom  company’s  cus-
tomer database, and is used to predict customer churn–the likelihood that a customer 
will cancel their subscription to the service. The target variable in this dataset is Churn,

2  h t t p s :  / / w w w  . k a g g l  e . c o  m / d a t  a s e t s  / b l a s t  c h a r  / t e l c o - c u s t o m e r - c h u r n

---

<!-- PAGE 8 -->

Page 8 of 45

a  binary  indicator  where  ‘Yes’  signifies  a  customer  who  has  churned,  and  ‘No’  repre-
sents  a  customer  who  has  remained  with  the  company.  The  dataset  contains  a  mix  of 
numerical  and  categorical  features,  including  customer  demographics  (e.g.,  age,  gen-
der), account details (e.g., tenure, monthly charges), service usage patterns (e.g., internet 
service, online security), and payment methods (e.g., electronic billing). This dataset is 
well-suited for exploring imbalanced classification problems, with approximately 26.5% 
of customers having churned, which allows for a rigorous evaluation of different perfor-
mance metrics tailored to business data mining applications.

Feature scaling

Since the dataset contained various features with different units and ranges, all numeri-
cal features were standardized using z-score normalization. The study used standardiza-
tion  because  it  helps  to  increase  the  performance  of  business  predictive  models  while 
dealing with large business datasets [38].

X ′ =

X

µ

−
σ

(1)

where X is the original feature value, µ is the mean, and σ is the standard deviation. This 
ensures that models sensitive to feature magnitudes and perform effectively.

Dataset splitting

The data was split into training (80%) and testing (20%) subsets using stratified sampling 
to maintain the class imbalance ratio in both sets. Stratified sampling ensures that the 
minority class (clients who defaulted) is represented proportionally, which is crucial for 
reliable model evaluation.

Model selection and validation of use

In  this  study,  we  aimed  to  evaluate  the  optimal  performance  metric  for  business  data 
mining  on  imbalanced  datasets.  To  ensure  the  generalizability  and  robustness  of  our 
findings  on  performance  metric  evaluation,  we  selected  five  machine  learning  models 
representing diverse algorithmic paradigms: LR as a linear model, DT, RF, and XGB as 
tree-based models, and KNN as an instance-based method. This variety enables a com-
prehensive assessment of metric behavior across fundamentally different learning strate-
gies commonly used in business data mining.

Logistic Regression (LR)

LR  is  a  linear  model  widely  used  for  binary  classification  tasks.  It  is  interpretable  and 
computationally  efficient,  making  it  ideal  for  applications  such  as  credit  scoring  and 
fraud  detection  in  business  contexts  [39].  Its  probabilistic  output  makes  it  suitable  for 
threshold-based analyses. The decision boundary for LR is modeled as:

P (Y = 1

X) =
|

1

1 +e −

(β0+β1X1+...+βnXn)

(2)

where β0 is the intercept and β1, . . . , βn are the coefficients for the features X1, . . . , Xn. 
Regularization was applied to prevent overfitting, and hyperparameters were optimized 
using grid searching technique.

---

<!-- PAGE 9 -->

Page 9 of 45

Random Forest (RF)

RF is an ensemble learning method that builds multiple DTs and averages their outputs 
to  improve  robustness  and  reduce  overfitting  [40].  We  included  the  RF  model  due  to 
its  capability  to  manage  high-dimensional  datasets  and  capture  complex  interactions 
between  features.  Additionally,  it  is  robust  to  class  imbalances  and  can  rank  features’ 
importance, aligning well with explainability needs in business domains. The prediction 
for RF is given by:

ˆy = mode

{

h1(X), h2(X), . . . , hT (X)

}

(3)

where ht(X) is the prediction of the t-th tree. The number of trees (T ) and maximum 
tree depth were fine-tuned to achieve optimal performance.

Decision Tree (DT)

DT is an interpretable model that splits the dataset into subsets based on feature thresh-
olds. Our study used this model, as it offers a simple yet interpretable structure for clas-
sification problems [41]. Their tree-like representation makes them easy to understand, 
even for non-technical stakeholders. The splitting criterion is determined using metrics 
such as Gini impurity:

G = 1

C

−

i=1
∑

p2
i

(4)

where pi is the proportion of instances belonging to class i, and C is the total number of 
classes. Pruning was applied to prevent overfitting.

XGBoost (XGB)

XGB is a gradient-boosting algorithm that optimizes a regularized objective function. It 
is able to prevent overfitting, making it particularly effective for datasets like ours with 
diverse feature distributions [42]. XGB’s scalability and superior predictive performance 
make it highly applicable in business data mining. For binary classification, the objective 
function is defined as:

=

L

n

i=1
∑

ℓ(yi, ˆyi) +

T

j=1
∑

Ω(hj)

(5)

where ℓ is the loss function (log-loss for binary classification), and Ω(hj) is the regular-
ization  term.  Hyperparameters  such  as  learning  rate  and  tree  depth  were  tuned  using 
cross-validation.

k-Nearest Neighbors (KNN)

KNN is a distance-based algorithm that classifies instances based on the majority class 
among k nearest neighbors. We included KNN to analyze how non-parametric models, 
which rely on local decision boundaries, perform compared to parametric and ensemble 
models [43]. Its sensitivity to feature scaling allowed us to evaluate the impact of prepro-
cessing steps on metric performance.
The classification is determined as:

---

<!-- PAGE 10 -->

ˆy = argmaxc

k

i=1
∑

I(yi = c)

Page 10 of 45

(6)

where I is an indicator function that equals 1 if yi = c and 0 otherwise. The value of k 
and the distance metric (Euclidean distance) were optimized for best performance.

In this research, the study used multiple machine learning models and statistical tests 
to  assess  their  performance  in  selecting  the  best  performance  metrics.  Table  4  pres-
ents  the  configuration  of  each  model,  including  their  specific  hyperparameters  and 
key settings. In addition, we outline the statistical tests and performance metrics used 
to evaluate the models we selected in this research. We provide a clear overview of the 
experimental setup for reproducibility and understanding of the analysis process that we 
incorporated in this investigation.

Performance metric evaluation

The  evaluation  of  machine  learning  models  in  this  study  focused  on  five  key  perfor-
mance  metrics  encompassing  the  Accuracy,  Precision,  Recall,  MCC,  and  F1-Score. 
These  metrics  were  chosen  based  on  their  relevance  and  robustness  for  imbalanced 
datasets  and  their  ability  to  capture  different  dimensions  of  model  performance.  This 
section  discusses  the  significance  of  each  metric,  their  mathematical  formulation,  and 
why they were specifically chosen over other potential metrics.

Table 4  Parameter settings for selected models and techniques
Model/analysis
 Logistic regression

Random forest

Decision tree

XG boost

K-Nearest neighbors

Cross-validation

SHAP analysis

Statistical analysis

Parameter
Max_iter
Solver
Penalty
C
Random_state
N_estimators
Max_depth
Random_state
Max_depth
Random_state
n_estimators
Learning_rate
Max_depth
Subsample
n_neighbors
Weights
cv
Scoring
Explainer
Shap_values
Mean SHAP importance
Bootstrap Confidence Intervals
McNemar’s Test
Cohen’s Kappa
ANOVA
Significance Level

Setting
1000
’lbfgs’
’l2’
1.0
42
100
6
42
5
42
100
0.1
6
0.8
5
‘uniform’
5
[‘accuracy’,‘precision’,‘recall’,‘f1’,‘mcc’]
shap.Explainer(model, X_train)
explainer(X_test)
Absolute mean SHAP values per feature
1000 bootstraps
Exact p-value
Measure agreement between model
Testing significant differences across metrics
p-value < 0.05 for significance

---

<!-- PAGE 11 -->

Page 11 of 45

Accuracy

While it is widely recognized that accuracy is a poor standalone metric in imbalanced 
classification  settings–often  yielding  deceptively  high  values  by  favoring  the  majority 
class [9, 44]–its inclusion in this study serves a critical analytical role. Rather than using 
accuracy  as  a  primary  indicator  of  model  performance,  we  treat  it  as  a  control  metric 
or baseline to highlight the limitations of naive evaluation in the presence of imbalance. 
By systematically comparing accuracy to more robust alternatives (e.g., F1-score, MCC) 
across  varying  imbalance  ratios  and  classification  thresholds,  we  expose  the  instability 
and over-optimism of accuracy in high-stakes business domains such as churn and credit 
default  prediction.  Furthermore,  the  divergence  between  accuracy  and  minority-sen-
sitive  metrics  under  conditions  of  noise  and  threshold  shifts  is  quantitatively  analyzed 
using bootstrap confidence intervals and ANOVA, reinforcing the need for multi-metric 
evaluation. This comparative lens allows us not only to validate the inadequacy of accu-
racy empirically but also to showcase its misalignment with business-relevant decision-
making. Accuracy is mathematically expressed as:

Accuracy =

T P + T N
T P + T N + F P + F N

(7)

where T P  is true positives, T N  is true negatives, F P  is false positives, and F N  is false 
negatives.

Precision

Precision quantifies the proportion of positive predictions that are correct:

Precision =

T P
T P + F P

(8)

Precision has been included in our investigation because it plays a crucial role in busi-
ness applications where false positives have high costs, such as fraud detection or cus-
tomer churn prediction. It ensures that the model does not excessively classify instances 
as positive when they are not, which is highly relevant for business data mining [45].

Recall

Recall mainly refers to the percentage of actual positive cases that are correctly identified 
by the specific model:

Recall =

T P
T P + F N

(9)

Recall is vital when false negatives are costly, such as missing a default customer in credit 
scoring. It ensures the model captures as many true positives as possible, which is essen-
tial for risk management in business data mining [46].

F1-score

The  F1-Score  is  the  harmonic  mean  of  Precision  and  Recall,  balancing  the  trade-off 
between the two:

F1-Score = 2

Precision
Recall
·
Precision + Recall

·

(10)

---

<!-- PAGE 12 -->

Page 12 of 45

The F1-Score offers a single metric that balances precision and recall and provides equal 
importance  to  both,  making  it  particularly  useful  for  imbalanced  datasets.  It  prevents 
over-optimization of one metric at the expense of the other [47].

Matthews Correlation Coefficient (MCC)
MCC is a robust metric that considers all four confusion matrix elements (T P , T N , F P , 
F N ) to provide a balanced evaluation:

MCC =

(T P

T N )

(F P

F N )

·

−

·

(T P + F P )(T P + F N )(T N + F P )(T N + F N )

(11)

√

MCC  is  ideal  for  imbalanced  datasets  as  it  accounts  for  true  and  false  classifications 
of  both  classes.  Unlike  Accuracy,  it  remains  reliable  even  when  class  distributions  are 
highly skewed [48].

Evaluation of additional metrics

In addition to our selected five primary evaluation metrics, including Accuracy, Preci-
sion, Recall, F1-score, and MCC, we included four alternative metrics commonly used 
in imbalanced classification problems, such as Geometric Mean (G-Mean), Area Under 
the ROC Curve (AUC), Balanced Accuracy, and the Index of Balanced Accuracy (IBA). 
These metrics were computed using the same prediction outputs from the trained mod-
els at a fixed decision threshold of 0.5. Their inclusion aims to offer a broader perspective 
on model performance and to respond to established critiques in the literature regarding 
the limitations of conventional metrics in imbalanced scenarios. However, these alterna-
tive metrics were not included in subsequent robustness, statistical testing, or explain-
ability  analysis.  This  decision  was  based  on  their  performance  consistency  with  our 
selected five metrics during baseline comparison, as well as their lower interpretability 
in business decision-making contexts. As such, the remainder of the evaluation focuses 
on the five core metrics.

Cost-sensitive evaluation

To  assess  how  well  our  selected  conventional  evaluation  metrics  align  with  real-world 
financial decision-making, we implemented a cost-sensitive evaluation framework based 
on confusion matrix outputs. This approach simulates domain-specific misclassification 
penalties  by  applying  a  cost  matrix  where  false  positives  incur  a  cost  of  10  units,  and 
false negatives incur a cost of 100 units–reflecting business-critical contexts such as loan 
default or customer churn. For each model, we computed the Expected Cost of Misclas-
sification (ECM) using the formula:

ECM = (F P

CF P ) + (F N

CF N )

×

×

(12)

where  CF P = 10  and  CF N = 100.  We  also  derived  a  Net  Profit  score  by  taking  the 
inverse  of  the  ECM.  These  results  were  used  to  evaluate  the  practical  alignment  of 
F1-score and MCC with cost-based priorities.

Our  design  of  this  cost-sensitive  evaluation  is  motivated  by  prior  work  in  financial 
domains,  where  researchers  have  highlighted  the  limitations  of  accuracy-driven  met-
rics and proposed profit-oriented alternatives. For example, rank-based portfolio selec-
tion  approaches  have  been  shown  to  outperform  market  indices  by  explicitly  linking

---

<!-- PAGE 13 -->

Page 13 of 45

evaluation  to  investment  returns  [49].  Similarly,  cost-sensitive  prediction  frameworks 
have been applied to stock price forecasting, where tailored misclassification costs and 
feature selection improved investment outcomes [50]. Inspired by these studies, we inte-
grate  cost-adjusted  metrics  into  our  evaluation  pipeline  to  better  reflect  financial  and 
business realities.

Stratified 5-fold cross-validation

In this section, we implemented 5-fold stratified Cross-Validation as presented in Algo-
rithm  1  to  evaluate  multiple  models  on  our  selected  large  business  dataset,  consist-
ing  of  30,000  instances.  This  approach  balances  computational  efficiency  with  reliable 
performance  estimation  by  splitting  the  data  into  5  folds,  using  each  fold  as  a  test  set 
while  training  on  the  remaining  data.  The  process  is  repeated  across  all  folds,  and  for 
each model, we calculate the mean and standard deviation of the performance metrics–
accuracy,  precision,  recall,  F1-score,  and  MCC.  This  allows  us  to  assess  both  the  cen-
tral tendency and variability of model performance. The 5-fold cross-validation ensures 
that each model is evaluated across different data subsets, providing robust estimates of 
performance and helping to select the most appropriate metric for model comparison. 
This approach is particularly effective for large datasets like ours, as it mitigates the risk 
of  overfitting  while  offering  a  comprehensive  assessment  of  each  model’s  reliability  in 
a  business  data  mining  scenario  [51].  Our  proposed  Stratified  5-Fold  Cross-Validation 
process has been presented in Figure 3 meticulously.

Algorithm 1  5-Fold Stratified Cross-Validation for Model Evaluation

Statistical validation

In this study we implemented four statistical tests, including ANOVA, bootstrap confi-
dence intervals, McNemar’s test, and Cohen’s kappa. The combination of these statisti-
cal  techniques  ensures  that  the  selection  of  the  optimal  metric  is  not  based  solely  on

---

<!-- PAGE 14 -->

Page 14 of 45

Fig. 3  Proposed stratified 5-fold cross-validation

numerical differences but is statistically validated. By identifying significant differences 
and quantifying the reliability of the metric, this study ensures that the selected metric, 
whether F1-score, MCC, or another, provides the most robust and generalizable assess-
ment of the model performance for business data mining tasks. These methods directly 
address the gaps in current research, where statistical validation is often overlooked in 
metric selection.

Analysis of variance (ANOVA)

To  directly  evaluate  the  relative  reliability  of  performance  metrics  across  models 
and  thresholds,  we  applied  a  repeated-measures  analysis  of  variance  (ANOVA).  This 
approach  tests  for  significant  differences  between  metrics  while  accounting  for  the 
repeated structure of the data (i.e., metric scores across multiple models and thresholds).
For each of our selected metrics, including Accuracy, Precision, Recall, F1-score, and 
MCC, we collected scores across five classifiers and nine thresholds (0.1
0.9). We 
then performed a within-subjects repeated-measures ANOVA with Metric as the within 
factor. Formally, the ANOVA model can be expressed as:

≤

≤

τ

Yij = µ + αi + sj + ϵij

(13)

where  Yij  is  the  performance  score  of  metric i  for  subject  (model-threshold  combina-
tion) j, µ is the grand mean, αi is the effect of metric i, sj is the random effect of subject 
j, and ϵij is the residual error term. The null hypothesis tested was:

H0 : µ1 = µ2 =

= µk

· · ·

(14)

where k = 5 metrics, against the alternative that at least one metric mean differs. Where 
significant  main  effects  were  observed  (p < 0.05),  we  conducted  Holm-corrected  pair-
wise post-hoc comparisons. For each pair of metrics a and b, the test statistic was com-
puted as:

t =

¯Xb
¯Xa −
¯Xb)  
SE( ¯Xa −

(15)

with  adjusted  p-values  using  the  Holm-Bonferroni  method  to  control  the  family-wise 
error rate. To complement the inferential tests, we also computed descriptive statistics

---

<!-- PAGE 15 -->

Page 15 of 45

for each metric, including the mean, median, standard deviation (σ), interquartile range 
(IQR), and coefficient of variation (CV):

CV =

σ
µ

(16)

Boxplots were generated to visualize the distribution and stability of metric scores across 
all models and thresholds.

McNemar’s test

We use McNemar’s test to compare prediction errors between two models [52]. This test 
determines  if  there  is  a  statistically  significant  difference  in  the  classification  errors  of 
two models on the same dataset, making it especially relevant for metrics like precision 
and  recall.  It  highlights  differences  in  error  distributions,  which  are  critical  for  under-
standing trade-offs between precision and recall The test statistic is calculated as:

χ2 =

c)2
(b
−
b + c

where:

(17)

• b is the count of instances misclassified by model A but correctly classified by model

B,

• c is the count of instances correctly classified by model A but misclassified by model

B.

This  test  highlights  differences  in  the  models’  classification  capabilities,  particularly 
for  imbalanced  datasets,  where  error  patterns  are  critical  for  evaluating  performance 
metrics.

Bootstrap confidence intervals

Bootstrap confidence intervals (CIs) were calculated to quantify the variability and reli-
ability of each performance metric. It provides insights into metric variability, ensuring 
the reliability of selected metrics under different scenarios [53]. By resampling the data 
with replacement N  times (N = 1000), we obtained a distribution of metric values and 
computed the 95% confidence interval as:

CI95% = [P2.5%, P97.5%]

(18)

where, P2.5% and P97.5% are the 2.5th and 97.5th percentiles of the bootstrap distribu-
tion. Metrics with narrower confidence intervals were deemed more reliable, providing 
robust guidance for metric selection in noisy and imbalanced settings.

Cohen’s kappa
We used Cohen’s Kappa (κ) to measure the agreement between two models’ predictions, 
accounting for the agreement occurring by chance [54]. It is defined as:

κ =

Po −
1
−

Pe
Pe

where:

(19)

---

<!-- PAGE 16 -->

Page 16 of 45

• Po is the observed agreement between the two models,
  • Pe is the expected agreement due to chance.

Cohen’s Kappa provides a scale of agreement, where:

• κ > 0.8: strong agreement,
  • 0.6 < κ
  • κ

0.6: weak agreement.

≤

0.8: moderate agreement,

≤

This  metric  is  particularly  useful  for  validating  classification  consistency  across  mod-
els  and  evaluating  metrics  such  as  F1-Score  and  MCC,  which  are  sensitive  to  class 
imbalance.

Threshold sensitivity analysis

Static threshold sensitivity analysis

Static threshold analysis involves evaluating model performance metrics: accuracy, pre-
cision,  recall,  F1-score,  and  MCC  across  fixed  decision  thresholds,  ranging  from  0.1 
to  0.9. The  goal  is  to  understand  the  trade-offs  between  metrics  and  their  behavior  as 
thresholds change [55]. The performance metrics for a given threshold t are calculated 
based on predictions ˆy, defined as:

ˆy =

{

1
0

if P (y = 1
if P (y = 1

X)
t,
≥
X) < t.

|
|

Dynamic threshold sensitivity analysis

Dynamic  threshold  analysis  optimizes  thresholds  for  each  metric  to  maximize  perfor-
mance. For each metric M , the optimal threshold t∗ is determined as:

t∗ = arg max

t

M (t)

(20)

where M (t) is the value of the metric at the threshold t.

This analysis identifies the best threshold for accuracy, precision, recall, F1-score, and 
MCC  individually,  offering  tailored  insights  into  the  performance  of  metric-specific 
models.  This  analysis  helps  identify  decision  thresholds  where  specific  metrics  reach 
their peak performance. In addition, it provides actionable recommendations for busi-
ness decision-making, where balancing false positives and false negatives is crucial.

Noise robustness testing

Noise robustness testing evaluates how performance metrics behave under varying noise 
levels in feature inputs. Gaussian noise with standard deviation σ is added to the input 
features X to simulate real-world data inconsistencies [56]. The noisy feature Xnoisy is 
defined as:

Xnoisy = X + N (0, σ2)

(21)

We  trained  our  selected  models  on  the  original  dataset  and  tested  on  noisy  data,  the 
range of the noise levels was from σ = 0.0 (no noise) to σ = 0.3. It evaluates metric sta-
bility  under  noisy  conditions,  reflecting  real-world  scenarios  where  data  may  contain

---

<!-- PAGE 17 -->

Page 17 of 45

errors.  Finally,it  identifies  models  resistant  to  noise,  crucial  for  business  data  mining, 
where data quality often varies based on the scenario.

Explainable AI (XAI) analysis

To improve interpretability for business end-users, we employed SHAP (SHapley Addi-
tive  exPlanations),  a  widely  used  explainability  technique  based  on  cooperative  game 
theory. SHAP decomposes a model’s output f (x) into additive feature contributions:

f (x) = ϕ0 +

n

i=1
∑

ϕi

(22)

Here, ϕ0 is the expected model output, and ϕi represents the marginal contribution of 
feature xi to the prediction. We applied SHAP to an LR model using the LinearExplainer, 
with  a  representative  background  sample  from  the  training  set  to  ensure  stability.  We 
selected  the  LR  model  due  to  its  transparency  and  compatibility  with  additive  feature 
attribution methods, making it ideal for explainable business applications. Our analysis 
follows a two-stage framework. In the first stage, we generated conventional SHAP out-
puts, including summary bar plots and beeswarm plots, which highlight both global and 
local  feature  importance. These  plots  illustrate  the  average  and  instance-specific  influ-
ence of each feature on the model’s predictions.

In  the  second  stage,  we  introduce  a  novel  3D  SHAP  framework  to  link  model  inter-
pretability  with  metric-specific  performance  across  varying  classification  thresholds. 
Thresholds were varied from 0.1 to 0.9, and for each value, classification outcomes were 
generated on the test set. Evaluation metrics were computed alongside SHAP values. To 
quantify feature importance at each threshold, we computed the mean absolute SHAP 
value per feature across all test samples, defined as:

Si(t) =

1
n

n

ϕ(t)
i,j

j=1 (cid:30)
(cid:31)
(cid:30)
(cid:30)

(cid:30)
(cid:30)
(cid:30)

(23)

where Si(t) is the metric-conditioned SHAP importance of feature xi at threshold t, ϕ(t)
i,j  
is the SHAP value for feature xi and sample j at threshold t, and n is the number of test 
instances.

This  enabled  the  construction  of  3D  visualizations  in  which  the  X-axis  represents 
the  classification  threshold,  the  Y-axis  reflects  SHAP  importance,  and  the  Z-axis  cor-
responds to the value of a selected evaluation metric. These plots reveal how the influ-
ence of individual features shifts across different decision boundaries and performance 
criteria, offering deeper insight into metric behavior under realistic business constraints.
Finally, the combined use of static and dynamic threshold analysis, statistical analysis, 
noise robustness testing, and SHAP-based explainability creates a comprehensive frame-
work for selecting the optimal performance metric in business data mining. The general 
experimental design has been described in Figure 4. To provide the detailed phases of 
our analysis, Algorithm 2 presents the overall steps that have been followed in this rigor-
ous investigation. With the experimental setup in place, we now report the performance 
metrics and statistical outcomes derived from our evaluation.

---

<!-- PAGE 18 -->

Page 18 of 45

Algorithm 2  Framework for Optimal Performance Metric Selection

Experimental results

In  this  section  we  present  the  experimental  results  of  our  investigation.  To  evaluate 
the reliability of performance metrics in business data mining, we conducted extensive 
experiments  on  two  real-world  benchmark  datasets:  the  large-scale  Default  of  Credit 
Card Clients dataset and the smaller Telco Customer Churn dataset. These datasets dif-
fer  in  size  and  imbalance  levels  but  are  both  representative  of  practical  business  pre-
diction scenarios. For the first dataset, we applied a comprehensive suite of evaluations, 
including exploratory data analysis, cross-validation, static and dynamic threshold sen-
sitivity  analysis,  noise  robustness  testing,  statistical  significance  testing,  and  two-stage 
SHAP-based explainability.

---

<!-- PAGE 19 -->

Page 19 of 45

Fig. 4  Experimental design for selecting the best performance metrics

To ensure generalizability of our findings while considering the experimental length, 
we focused on key evaluations for the second dataset. Specifically, we conducted cross-
validation,  Gaussian  noise  robustness  testing,  and  bootstrap  confidence  intervals  and 
applied advanced statistical tools such as McNemar’s test and Cohen’s kappa to math-
ematically  assess  pairwise  model  agreement  and  classification  significance.  Addition-
ally, we employed SHAP-based explainable AI techniques to analyze feature importance 
across  performance  metrics  and  classification  thresholds.  This  structured  and  statisti-
cally rigorous approach ensures that our results are robust, interpretable, and applicable 
to diverse business data mining contexts.

Exploratory data analysis

To establish a robust foundation for analyzing the performance of our selected machine 
learning models, our study conducted an initial exploration of the dataset, focusing on 
the  distributional  properties  of  key  features.  To  better  understand  the  characteristics 
of  the  dataset,  Gaussian  distribution  plots  were  generated  for  12  selected  features  as

---

<!-- PAGE 20 -->

Page 20 of 45

displayed in Figure 5a to Figure 5i. These plots provide critical insights into the statistical 
properties of each feature, including their central tendency, spread, and skewness, which 
are essential to validate the suitability of different machine learning models and perfor-
mance metrics. Gaussian distribution analysis is particularly relevant, as many machine 
learning  algorithms,  such  as  LR,  assume  features  are  normally  distributed,  while  oth-
ers, such as tree-based models, are less sensitive to such assumptions. This analysis also 
helps identify features that may require scaling, transformation, or special handling [57], 
especially in the context of imbalanced distributions or outliers, which can impact met-
rics such as F1-Score and MCC that emphasize the balance between true positives and 
false negatives.

Key  insights  were  derived  from  individual  feature  distributions.  LIMIT_BAL  in  Fig-
ure  5a  exhibited  a  strong  right-skewed  distribution,  with  most  clients  concentrated  at 
lower  credit  limits,  potentially  leading  to  imbalances  during  training.  Binary  features 
such as SEX in Figure 5b displayed a bimodal distribution, confirming a balanced rep-
resentation of demographic groups, while categorical features such as EDUCATION in 
Figure 5c and MARRIAGE in Figure 5d demonstrated multi-modal distributions reflect-
ing  the  diversity  of  education  levels  and  marital  statuses.  Similarly,  AGE  in  Figure  5e 
showed a right-skewed distribution, with younger clients dominating the dataset and a 
long tail for older clients. Payment history features such as PAY_0, PAY_2, and PAY_3 in

Fig. 5  Gaussian distribution of the Default of Credit Card Clients dataset for different features. The description of 
the feature labels is given in [58] (a) LIMIT_BAL, (b) SEX, (c) EDUCATION, (d) MARRIAGE, (e) AGE, (f) PAY_0, (g) PAY_2, 
(h) PAY_3, (i) BILL_ATM1, (j) BILL_ATM2, (k) BILL_ATM4, (l) BILL_ATM6

---

<!-- PAGE 21 -->

Page 21 of 45

Figure 5f to Figure 5h revealed a significant peak at zero, corresponding to no delays in 
payments, while additional peaks indicated varying levels of delinquency, emphasizing 
the predictive importance of repayment behaviors.

Billing  amounts  BILL_AMT1,  BILL_AMT2,  and  BILL_AMT4  in  Figure  5i  to  Fig-
ure 5k displayed consistent right-skewed distributions, with most values clustered near 
zero  and  a  long  tail  extending  to  higher  billing  amounts.  This  variability  underscores 
the  importance  of  scaling  these  features  to  avoid  biasing  distance-based  models  such 
as  KNN.  Similarly,  PAY_AMT6  in  Figure  5l  exhibited  an  extreme  right-skewed  distri-
bution,  highlighting  the  need  to  account  for  rare  but  significant  large  payment  values 
during  model  training.  These  findings  emphasize  the  need  for  robust  preprocessing 
techniques, including standardization and transformations, to ensure fair contributions 
from all features. Moreover, the analysis provides valuable insights into how feature dis-
tributions impact the suitability of performance metrics, with metrics such as MCC and 
F1-Score being particularly effective in handling imbalanced and skewed data distribu-
tions. This  detailed  understanding  of  the  dataset  lays  the  groundwork  for  the  rigorous 
evaluation of machine learning models and performance metrics in subsequent sections.

Baseline performance evaluation

To establish a benchmark for performance metrics, we evaluated five machine learning 
models: LR, RF, DT, XGB, and KNN. The evaluation mainly focused on our selected five 
performance  metrics.  Table  5  provides  a  summary  of  the  baseline  performance  met-
rics for each model, while Figure 6a to Figure 6e present bar plots to visually assess and 
compare  the  performance  of  the  models  based  on  these  performance  indicators.  We 
observed  that  LR  achieved  the  highest  precision  (0.657),  indicating  its  effectiveness  in 
minimizing  false  positives,  although  it  struggled  with  recall  (0.197),  reflecting  limited 
sensitivity to correctly identify defaults [59]. XGB demonstrated the most balanced per-
formance, achieving the highest F1-Score (0.380) and MCC (0.287), making it robust in 
handling class imbalances [60]. DT, on the other hand, achieved the highest recall (0.404) 
but at the cost of low precision (0.346), resulting in a lower overall F1-Score and MCC. 
RF showed slightly better recall (0.238) compared to LR and KNN, but its performance 
was  less  consistent  across  all  metrics.  KNN  delivered  moderate  performance,  with  an 
Accuracy of 0.772 and MCC of 0.212, reflecting its sensitivity to feature scaling and its 
limitations in handling skewed distributions [61].

These results highlight the trade-offs that we encountered across models. For instance, 
while LR excelled in precision, it missed many true positives due to its lower recall. In 
contrast, DT and XGB captured more true positives, as evidenced by their higher recall, 
but  were  more  prone  to  false  positives.  Metrics  such  as  F1-Score  and  MCC  proved 
invaluable  in  balancing  these  trade-offs,  helping  us  identify  XGB  as  the  most  bal-
anced  baseline  model.  These  findings  underscore  the  critical  importance  of  selecting

Table 5  Baseline model performance for each metric
Model
LR
RF
DT
XGB
KNN

Precision
0.657
0.541
0.346
0.546
0.469

Accuracy
0.800
0.787
0.700
0.790
0.772

Recall
0.197
0.238
0.404
0.291
0.238

F1-Score
0.303
0.330
0.373
0.380
0.315

MCC
0.280
0.253
0.178
0.287
0.212

---

<!-- PAGE 22 -->

Page 22 of 45

Fig. 6  Baseline performance evaluation for all models across metrics: (a) accuracy, (b) precision, (c) recall, (d) F1, 
and (e) MCC

appropriate metrics for evaluating models in business data mining, where specific goals, 
such  as  reducing  false  positives  or  capturing  all  true  positives,  may  guide  both  metric 
and model selection.

Performance with cross validation

To evaluate the reliability and robustness of the models, we performed a 5-fold stratified 
cross-validation analysis across five metrics: Accuracy, Precision, Recall, F1-Score, and 
MCC. Table 6 summarizes the mean and standard deviation of each metric across the 
folds, while Figure 7a to Figure 7e present error bar plots that illustrate the variability in 
metric performance across folds. The error bar plots provided valuable insights into the 
consistency of the models. LR exhibited minimal variability in accuracy, with a mean of

---

<!-- PAGE 23 -->

Page 23 of 45

0.801 and a standard deviation of 0.006, suggesting that it performs consistently across 
different folds. Precision for LR also displayed tight error bars, highlighting its reliability 
in  minimizing  false  positives.  RF  and  XGB  exhibited  slightly  higher  variability  in  their 
F1-Scores and MCC values, although their average performance remained robust, with 
RF achieving the highest MCC (0.313) and XGB obtaining the second-highest F1-Score 
(0.391).  DT  showed  the  highest  variability  in  recall,  reflecting  its  sensitivity  to  class 
imbalance  and  fold-specific  characteristics,  while  KNN  demonstrated  the  largest  vari-
ability in F1-Score and MCC, indicating its reliance on consistent feature distributions 
across folds.

These  results  emphasize  the  importance  of  analyzing  metric  variability  alongside 
mean performance. Models like LR and RF demonstrated not only high average perfor-
mance but also low variability, making them suitable for business data mining tasks that 
demand reliability. In contrast, the higher variability observed for DT and KNN suggests 
that these models may require additional tuning or preprocessing to achieve consistent 
results in practice. The error bar analysis reinforces the importance of cross-validation 
as  a  tool  for  assessing  model  robustness  and  consistency,  ensuring  their  suitability  for 
real-world business applications.

Static threshold sensitivity analysis

To evaluate the impact of varying static classification thresholds on model performance, 
we  analyzed  five  key  metrics–Accuracy,  Precision,  Recall,  F1-Score,  and  MCC–across 
a  range  of  thresholds  (0.1  to  0.9).  The  goal  was  to  identify  the  trade-offs  inherent  in 
threshold adjustments and their effects on model performance, particularly for business 
data mining tasks where balancing Precision and Recall is critical. Table 7 summarizes 
the performance metrics for LR, RF, DT, XGB, and KNN models across thresholds. Fig-
ure  8a  to  Figure  8e  visualize  the  threshold-performance  relationships  in  three-dimen-
sional plots, where the x-axis denotes the threshold, the y-axis denotes the metric score, 
and the z-axis corresponds to the model.

The results demonstrate notable trade-offs between Precision and Recall as thresholds 
change. For example, Precision improves significantly for most models as the threshold 
increases, reflecting a reduction in false positives. In contrast, recall decreases sharply 
at higher thresholds as a result of stricter classification criteria, leading to an increased 
rate of false negatives [62]. This is evident in models such as LR and RF, which achieve 
high  precision  but  suffer  in  Recall  at  thresholds  above  0.5.  Metrics  like  Accuracy  and 
MCC exhibit more stability across intermediate thresholds, particularly for models like 
XGB and LR, suggesting their robustness in scenarios requiring a balance between false 
positives  and  false  negatives.  The  three-dimensional  plots  further  highlight  the  trends 
across models. For instance, in Figure 8a, Accuracy increases rapidly at lower thresholds 
and stabilizes around intermediate values for most models, with LR and XGB showing

Table 6  Results with 5-fold stratified cross-validation
Model Mean

Accuracy
0.801
0.799
0.716
0.785
0.779

LR
RF
DT
XGB
KNN

Std
Accuracy
0.006
0.006
0.015
0.009
0.008

Mean
Precision
0.688
0.597
0.370
0.525
0.498

Std
Precision
0.064
0.022
0.028
0.032
0.033

Mean
Recall
0.188
0.288
0.399
0.312
0.267

Std
Recall
0.021
0.029
0.035
0.030
0.036

Mean
F1
0.294
0.388
0.384
0.391
0.347

Std
F1
0.028
0.030
0.028
0.028
0.038

Mean
MCC
0.284
0.313
0.200
0.285
0.245

Std
MCC
0.031
0.027
0.036
0.030
0.038

---

<!-- PAGE 24 -->

Page 24 of 45

Fig. 7  Cross-validation mean and standard deviation for all models across metrics: (a) accuracy, (b) precision, (c) 
recall, (d) F1, and (e) MCC

the  most  consistent  performance.  Figure  8b  and  Figure  8c  reveal  opposing  trends  for 
Precision  and  Recall,  while  Figure  8d  shows  that  F1-Score,  which  balances  Precision 
and  Recall,  reaches  optimal  levels  at  thresholds  of  0.4  to  0.6.  Similarly,  Figure  8e  indi-
cates that MCC, which accounts for both true and false predictions, peaks around these 
intermediate thresholds. These results emphasize the need for careful threshold tuning, 
particularly in business applications where trade-offs between Precision and Recall must 
align with specific operational objectives. Through this analysis, we underline the impor-
tance  of  selecting  thresholds  that  maximize  overall  performance  while  accounting  for 
the priorities of the business context.

Dynamic threshold sensitivity analysis

In this section we conducted Dynamic threshold sensitivity analysis to identify the opti-
mal  thresholds  for  maximizing  key  performance  metrics–Accuracy,  Precision,  Recall,

---

<!-- PAGE 25 -->

Table 7  Static threshold sensitivity analysis across different metrics 
Model & Metric

Threshold
0.1
0.340
0.241
0.924
0.382
0.113
0.412
0.254
0.857
0.391
0.211
0.624
0.318
0.614
0.419
0.202
0.500
0.264
0.709
0.385
0.126

LR Accuracy
LR Precision
LR Recall
LR F1
LR MCC
RF Accuracy
RF Precision
RF Recall
RF F1
RF MCC
XGB Accuracy
XGB Precision
XGB Recall
XGB F1
XGB MCC
KNN Accuracy
KNN Precision
KNN Recall
KNN F1
KNN MCC
(LR: logistic regression, RF: random forest, XGB: XGBoost, KNN: k-nearest neighbors)

0.5
0.800
0.657
0.197
0.303
0.280
0.787
0.539
0.251
0.343
0.280
0.790
0.546
0.292
0.380
0.287
0.772
0.469
0.238
0.316
0.212

0.3
0.767
0.468
0.395
0.428
0.285
0.745
0.429
0.475
0.451
0.254
0.754
0.434
0.386
0.409
0.254
0.700
0.349
0.413
0.378
0.183

0.4
0.793
0.567
0.265
0.361
0.283
0.782
0.509
0.377
0.433
0.279
0.779
0.500
0.332
0.399
0.279
0.700
0.349
0.413
0.378
0.183

0.2
0.574
0.287
0.623
0.393
0.153
0.610
0.310
0.623
0.414
0.222
0.708
0.371
0.462
0.411
0.222
0.500
0.264
0.709
0.385
0.126

0.6
0.791
0.700
0.094
0.166
0.202
0.784
0.547
0.130
0.210
0.252
0.789
0.556
0.224
0.320
0.252
0.772
0.469
0.238
0.316
0.212

Page 25 of 45

0.7
0.782
0.588
0.045
0.083
0.116
0.785
0.625
0.067
0.122
0.259
0.795
0.614
0.193
0.294
0.259
0.790
0.649
0.108
0.185
0.201

0.8
0.782
0.667
0.027
0.052
0.102
0.782
0.636
0.031
0.060
0.226
0.792
0.628
0.144
0.234
0.226
0.790
0.649
0.108
0.185
0.201

0.9
0.778
0.400
0.009
0.018
0.031
0.780
1.000
0.005
0.009
0.184
0.788
0.636
0.094
0.164
0.184
0.778
0.429
0.014
0.026
0.042

F1-Score, and MCC–for each model, as summarized in Table 5. This evaluation provides 
a dual perspective by leveraging both tabular results and 3D visualizations in Figure 9a 
to Figure 9e to comprehensively assess model performance under varying threshold set-
tings.  The  integration  of  these  two  approaches  highlights  the  critical  role  of  threshold 
optimization  in  tailoring  machine  learning  models  to  business  data  mining  objectives. 
From  Table  8,  it  is  evident  that  LR  achieved  its  best  Accuracy  (0.80)  at  a  threshold  of 
0.5,  whereas  RF  peaked  at  a  slightly  lower  value  of  0.787  at  the  same  threshold.  Inter-
estingly,  KNN  exhibited  the  highest  accuracy  at  0.790  when  the  threshold  was  set  to 
0.7, suggesting its robustness under stricter classification criteria. Precision results also 
revealed that RF achieved a perfect score (1.00) at a threshold of 0.9, outperforming all 
other models. However, this high Precision came at the cost of Recall, where LR (0.924 
at  0.1  threshold)  and  KNN  (0.709  at  0.1  threshold)  performed  better,  indicating  their 
suitability  for  tasks  requiring  exhaustive  positive  detection.  F1-Score  analysis  reflected 
a balanced view, with XGB and LR achieving comparable F1 values of 0.419 and 0.428, 
respectively,  at  their  respective  thresholds.  MCC,  a  key  metric  for  imbalanced  data, 
showed XGB (0.287 at 0.5 threshold) and RF (0.307 at 0.4 threshold) leading in terms of 
overall classification stability. The 3D visualizations from Figure 9a to Figure 9e comple-
ment  the  tabular  results  by  illustrating  the  interplay  between  thresholds,  models,  and 
metric  performance.  This  analysis  underscores  the  trade-offs  associated  with  dynamic 
threshold  adjustment.  While  higher  thresholds  favor  metrics  like  Precision,  they  may 
compromise Recall, as seen in RF and KNN’s profiles. Conversely, lower thresholds opti-
mize Recall but diminish Precision, as evidenced by LR’s profile. Metrics like F1-Score 
and MCC provide balanced perspectives, capturing these trade-offs effectively.

---

<!-- PAGE 26 -->

Page 26 of 45

Fig. 8  Static threshold sensitivity analysis across different metrics: (a) accuracy, (b) precision, (c) recall, (d) F1, and 
(e) MCC

Before  proceeding  to  robustness  and  interpretability  analysis,  we  further  examine 
model  performance  through  alternative  evaluation  metrics  and  domain-specific  cost-
sensitive analysis, focusing on the Default of Credit Card Clients dataset.

Alternative metric evaluation

To broaden the depth of our analysis, we evaluated four additional performance metrics 
that are commonly used in imbalanced classification, such as G-Mean, AUC, Balanced 
Accuracy, and the IBA with α = 0.1 These metrics were calculated for all five classifiers 
using  a  fixed  decision  threshold  of  0.5.  Table  9  summarizes  the  results.  Among  these 
metrics, DT achieved the highest G-Mean (0.563) and IBA (0.541), indicating relatively 
balanced performance on both classes. RF performed best on AUC (0.681) and Balanced 
Accuracy  (0.595),  while  XGB  achieved  consistent  but  slightly  lower  values  across  all

---

<!-- PAGE 27 -->

Page 27 of 45

Fig. 9  Dynamic threshold sensitivity analysis comparison across metrics: (a) accuracy, (b) precision, (c) recall, (d) 
F1, and (e) MCC

Table 8  Dynamic threshold sensitivity analysis across different metrics
Model
LR
RF
DT
XGB
KNN
Note: LR = Logistic Regression, RF = Random Forest, XGB = XGBoost, KNN = k-Nearest Neighbors, DT = Decision Tree

Best MCC
0.285
0.307
0.178
0.287
0.212

Best F1
0.428
0.451
0.373
0.419
0.385

BA
0.800
0.787
0.700
0.795
0.790

BP
0.700
1.000
0.346
0.636
0.649

BR
0.924
0.857
0.404
0.614
0.709

BTR
0.1
0.1
0.1
0.1
0.1

BTA
0.5
0.5
0.1
0.7
0.7

BTP
0.6
0.9
0.1
0.9
0.7

BTF
0.3
0.3
0.1
0.1
0.1

BTM
0.3
0.4
0.1
0.5
0.5

BA = Best Accuracy, BP = Best Precision, BR = Best Recall

BTA = Best Threshold (Accuracy), BTP = Best Threshold (Precision), BTR = Best Threshold (Recall), BTF = Best Threshold (F1), 
BTM = Best Threshold (MCC)

---

<!-- PAGE 28 -->

Page 28 of 45

metrics. KNN and LR exhibited lower G-Mean and AUC values, reflecting their limited 
recall performance, as noted earlier. For clarity and interpretability, F1-score and MCC 
values are also included in Table 9 to facilitate direct comparison. Notably, while some 
alternative  metrics  appear  competitive,  F1-score  and  MCC  remain  consistently  strong 
across  models,  aligning  well  with  overall  model  behavior.  For  instance,  XGB  had  the 
highest  F1-score  (0.380)  and  MCC  (0.287),  along  with  solid  alternative  metric  values, 
supporting  its  well-rounded  performance.  Given  their  widespread  adoption,  statistical 
interpretability, and alignment with both threshold and cost-based analyses, our selected 
five metrics were retained as the primary focus for all subsequent robustness, explain-
ability, and statistical validation experiments.

Cost-sensitive evaluation

To assess the alignment between traditional evaluation metrics and real-world financial 
costs, we performed a cost-sensitive evaluation based on confusion matrix outputs. Each 
model’s false positives and false negatives were penalized using a domain-relevant cost 
matrix where false positives incurred a cost of 10 units, and false negatives incurred a 
cost of 100 units. The resulting Expected Cost of Misclassification (ECM) and Net Profit 
(as  the  negative  of  ECM)  are  reported  in  Table  10. The  results  reveal  clear  differences 
in cost-effectiveness across models. DT achieved the lowest ECM (15,000) and thus the 
highest  Net  Profit  (–15,000),  primarily  due  to  its  higher  recall  (0.404)  and  lower  false 
negative count (133). This highlights its suitability for scenarios where missing positive 
cases (e.g., loan defaults or customer churn) incurs high financial risk. By contrast, LR, 
which had the highest MCC (0.280) and good precision (0.657), resulted in the highest 
ECM (18,130) due to a very low recall (0.197) and high number of false negatives (179). 
This demonstrates that even models with high MCC may not be optimal in cost-sensi-
tive domains if they underperform in recall.

These  findings  reinforce  the  decision  to  prioritize  accuracy,  precision,  recall,  F1  and 
MCC as our core evaluation metrics. While cost-sensitive metrics provide an essential 
domain-aware  perspective,  F1-score–by  balancing  precision  and  recall–often  aligned 
more  closely  with  cost  efficiency,  and  MCC  provided  complementary  information  on 
class  imbalance.  Therefore,  both  metrics  remain  valid  and  robust  tools  for  evaluating 
predictive models in business-critical applications.

Noise robustness testing

The robustness of the models to increasing noise levels (0.0 to 0.3) was evaluated using 
metrics including Accuracy, Precision, Recall, F1-Score, and MCC. Table 11 details the 
results, while Figure 10a to Figure 10e illustrate the trends. LR and RF demonstrated sta-
ble performance, with LR achieving an accuracy of approximately 0.80, while RF showed 
a slight improvement to 0.802 at 30% noise. Precision also increased for these models,

Table 9  Performance of standard (F1, MCC) and alternative evaluation metrics across models
G-Mean
Model
0.486
RF
0.472
XGB
0.438
LR
0.469
KNN
0.563
DT

MCC
0.253
0.287
0.280
0.212
0.178

F1
0.330
0.380
0.303
0.315
0.373

AUC
0.681
0.665
0.653
0.625
0.594

BA
0.595
0.581
0.584
0.581
0.594

IBA (α=0.1)
0.452
0.440
0.404
0.436
0.541

---

<!-- PAGE 29 -->

Page 29 of 45

Table 10  Cost-based evaluation of model performance using confusion matrix analysis 
TPR
Model
0.197
LR
0.251
RF
0.404
DT
0.242
XGB
0.238
KNN
True Positive Rate (TPR), True Negative Rate (TNR), False Positive Rate (FPR), False Negative Rate (FNR), and Expected Cost 
of Misclassification (ECM) are reported

Net Profit
−18130
−17180
−15000
−17530
−17600

ECM
18130
17180
15000
17530
17600

TNR
0.971
0.939
0.784
0.920
0.924

FNR
0.803
0.749
0.596
0.758
0.762

FPR
0.029
0.061
0.216
0.080
0.076

TN
764
739
617
724
727

FN
179
167
133
169
170

FP
23
48
170
63
60

TP
44
56
90
54
53

Table 11  Noise robustness testing across metrics
Noise Level
0
0
0
0
0
0.1
0.1
0.1
0.1
0.1
0.2
0.2
0.2
0.2
0.2
0.3
0.3
0.3
0.3
0.3

Accuracy
0.800
0.787
0.700
0.790
0.772
0.797
0.794
0.756
0.781
0.766
0.800
0.797
0.728
0.777
0.777
0.797
0.803
0.764
0.790
0.771

Model
LR
RF
DT
XGB
KNN
LR
RF
DT
XGB
KNN
LR
RF
DT
XGB
KNN
LR
RF
DT
XGB
KNN

Precision
0.657
0.541
0.346
0.546
0.469
0.641
0.576
0.433
0.508
0.445
0.672
0.582
0.363
0.493
0.490
0.680
0.622
0.447
0.566
0.457

Recall
0.197
0.238
0.404
0.291
0.238
0.184
0.256
0.332
0.291
0.238
0.184
0.287
0.309
0.296
0.229
0.152
0.274
0.283
0.211
0.193

F1-Score
0.303
0.330
0.373
0.380
0.315
0.286
0.354
0.376
0.370
0.310
0.289
0.384
0.334
0.370
0.312
0.249
0.380
0.346
0.307
0.271

MCC
0.280
0.253
0.178
0.287
0.212
0.263
0.282
0.231
0.264
0.198
0.276
0.304
0.165
0.256
0.220
0.253
0.317
0.219
0.249
0.183

with  LR  and  RF  reaching  0.680  and  0.622,  respectively,  highlighting  their  resilience. 
Recall  trends  revealed  that  the  DT  had  the  highest  initial  recall  (0.403)  but  was  sensi-
tive to noise, rebounding slightly at higher noise levels. RF balanced precision and recall 
effectively, achieving the best F1-Score (0.380) and MCC (0.317) under noisy conditions. 
LR  showed  steady  MCC  values  (0.28),  while  XGB  and  KNN  exhibited  declines  across 
metrics,  indicating  reduced  noise  tolerance.  Overall,  RF  and  LR  emerged  as  the  most 
robust  models,  demonstrating  stability  and  suitability  for  noisy  environments,  making 
them strong candidates for business applications involving data uncertainty.

Statistical and mathematical validation

To ensure the robustness and reliability of the performance metrics across models, we 
performed repeated-measures ANOVA, Bootstrap analysis to estimate confidence inter-
vals (CIs) and conducted McNemar’s test alongside Cohen’s Kappa to statistically evalu-
ate  model  prediction  agreement.  This  comprehensive  approach  provides  both  metric 
stability assessments and inter-model prediction validation.

---

<!-- PAGE 30 -->

Page 30 of 45

Fig. 10  Noise robustness testing comparison across metrics for all models: (a) accuracy, (b) precision, (c) recall, 
(d) F1, and (e) MCC

ANOVA

To  investigate  the  stability  and  reliability  of  our  selected  evaluation  metrics  across 
models  and  thresholds,  we  conducted  a  repeated-measures  ANOVA.  The  analysis 
revealed  a  highly  significant  main  effect  of  metric  on  performance  scores  (F(4,176)  = 
77.62,  p < 0.001).  Descriptive  statistics  and  Holm-corrected  post-hoc  comparisons 
are reported in Table 12, and the distribution of scores is visualized in Figure 11. Accu-
racy  achieved  the  highest  overall  mean  score  (0.716)  and  the  lowest  variability  (CV  = 
0.146),  performing  significantly  better  than  all  other  metrics  (p < 0.001).  However,  its 
dominance  reflects  its  bias  toward  majority  classes  rather  than  balanced  evaluation 
under imbalance. F1-score (mean = 0.296, CV = 0.434) and MCC (mean = 0.183, CV = 
0.334) demonstrated more balanced performance across models and thresholds. F1 and 
Recall did not differ significantly from one another (p = 0.236), indicating they capture 
similar dynamics under imbalance. MCC was significantly lower than F1 and Precision 
but outperformed Recall, confirming its complementary role alongside F1 in reflecting 
trade-offs  between  false  positives  and  false  negatives.  Precision  (mean  =  0.462,  CV  = 
0.340)  performed  moderately  well,  significantly  better  than  Recall  and  F1  but  inferior

---

<!-- PAGE 31 -->

Page 31 of 45

Table 12  Descriptive statistics and significance tests for evaluation metrics across models and 
thresholds
Metric
Accuracy
MCC
Precision
F1-score
Recall
Standard deviation (Std), interquartile range (IQR), and coefficient of variation (CV) are reported. Significant differences are 
based on Holm-corrected pairwise comparisons at α = 0.05

Significant Differences
>MCC, Precision, F1, Recall
< Accuracy, F1, Precision; >Recall
< Accuracy; >F1, Recall
< Accuracy, Precision; >MCC;
< Accuracy, Precision;

Median
0.767
0.183
0.429
0.373
0.359

Mean
0.716
0.183
0.462
0.296
0.323

CV
0.146
0.334
0.340
0.433
0.708

Std
0.104
0.061
0.157
0.128
0.228

IQR
0.082
0.060
0.221
0.172
0.274

∼
F1 (ns)

Recall (ns)

∼

Fig. 11  Distribution of evaluation metric scores (Accuracy, Precision, Recall, F1-score, and MCC) across five classi-
fiers and nine decision thresholds (0.1–0.9)

to Accuracy. Recall (mean = 0.323, CV = 0.708) was the most unstable metric, with high 
variability across thresholds and models, making it less reliable as a standalone indica-
tor. Together, these results confirm that although Accuracy yields higher absolute values, 
F1-score  and  MCC  offer  more  reliable  and  interpretable  measures  under  class  imbal-
ance,  justifying  their  emphasis  in  subsequent  robustness  and  explainability  analyses  in 
business data mining. Full post-hoc statistics are provided in Table 13.

Bootstrap confidence intervals

Bootstrap CIs for Accuracy, Precision, Recall, F1-Score, and MCC were computed across 
models. Table 14 presents the Bootstrap confidence interval results across metrics, and 
Figure 12a to Figure 12e support the visualization of the findings. LR consistently dem-
onstrated  narrow  intervals  across  metrics,  reflecting  its  stability.  For  Accuracy,  the  CI 
was  (0.7752,  0.8248),  higher  than  DT  (0.6723,  0.7287),  indicating  superior  reliability. 
XGB  exhibited  tight  CIs  in  most  metrics,  particularly  for  MCC  (0.2082,  0.3578),  sug-
gesting balanced performance. In contrast, DT exhibited wider intervals, especially for 
Recall, highlighting potential instability under varying data conditions.

McNemar’s test and cohen’s kappa

McNemar’s  test  evaluated  significant  prediction  differences  across  paired  models. 
Table 15 and Figure 13 Presents the combined results of McNemar’s Test and Cohen’s 
Kappa  teast.  LR  and  RF  showed  statistically  significant  differences  in  predictions 
(p-value = 2.4439e-04), indicating non-identical model behaviors. Similarly, DT vs. XGB

---

<!-- PAGE 32 -->

Page 32 of 45

Table 13  Pairwise post-hoc comparisons between metrics using repeated-measures ANOVA. 
Reported values include the t-statistic, raw p-value, and Holm-corrected p-value for family-wise error 
rate control at α = 0.05
Metric A
Accuracy
Accuracy
Accuracy
Accuracy
MCC
MCC
MCC
Precision
Precision
F1-score

Significant (α = 0.05)
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
Yes
No

Holm-corrected p
<0.0001
<0.0001
<0.0001
<0.0001
<0.0001
<0.0001
0.0006
0.0005
0.0291
0.2356

Metric B
MCC
Precision
F1-score
Recall
Precision
F1-score
Recall
F1-score
Recall
Recall

p-value
<0.0001
<0.0001
<0.0001
<0.0001
<0.0001
<0.0001
0.0002
0.0001
0.0145
0.2356

t-stat
34.220
15.056
14.136
8.128
−11.227
7.302
−4.060
−4.213
2.544
−1.203

Table 14  Bootstrap confidence intervals for performance metrics across models 
Model
LR
RF
DT
XGB
KNN
(LR: logistic regression, RF: random forest, DT: decision tree, XGB: XGBoost, KNN: k-nearest neighbors)

Precision CI
(0.530, 0.768)
(0.444, 0.633)
(0.287, 0.403)
(0.454, 0.633)
(0.373, 0.570)

Recall CI
(0.148, 0.252)
(0.185, 0.293)
(0.341, 0.465)
(0.229, 0.348)
(0.181, 0.298)

Accuracy CI
(0.775, 0.825)
(0.762, 0.811)
(0.672, 0.729)
(0.763, 0.813)
(0.745, 0.798)

F1 CI
(0.234, 0.371)
(0.263, 0.394)
(0.318, 0.424)
(0.312, 0.441)
(0.249, 0.383)

MCC CI
(0.199, 0.355)
(0.177, 0.322)
(0.110, 0.239)
(0.208, 0.358)
(0.208, 0.358)

had  a  significant  p-value  of  3.5484e-22.  Cohen’s  Kappa  values,  which  quantify  agree-
ment, were highest for LR vs. RF (0.5460), suggesting moderate agreement, while RF vs. 
DT scored lower (0.3172), reflecting greater disparity in predictions.

The bootstrap analysis identified LR and XGB as the most stable models across met-
rics, with consistently narrow CIs. McNemar’s test further validated significant predic-
tive differences between DT and XGB, while Cohen’s Kappa indicated strong agreement 
between LR and RF. These findings underscore LR’s reliability for precision-critical tasks 
and XGB’s balance across metrics. DT’s variability suggests its use may be better suited 
for scenarios prioritizing Recall over precision or stability.

Explainable AI (XAI) analysis

To strengthen the interpretability of our framework, we implemented a two-stage SHAP 
analysis.  First,  we  applied  conventional  SHAP  techniques  (bar  plots  and  beeswarm 
visualizations)  to  LR  as  a  baseline  model,  providing  standard  global  and  local  feature 
importance  insights.  This  step  ensures  transparency  and  aligns  with  widely  adopted 
explainability practices. Building on this, we introduced a novel 3D metric-conditioned 
SHAP  analysis,  where  feature  contributions  were  examined  across  varying  thresholds 
and  linked  directly  to  performance  metrics  (Accuracy,  Precision,  Recall,  F1-score,  and 
MCC). This extension moves beyond static feature importance, offering a dynamic view 
of how interpretability interacts with metric reliability under class imbalance.

Conventional SHAP analysis

To enhance transparency and meet standard explainability requirements, we first applied 
conventional  SHAP  analysis  to  LR,  one  of  the  most  interpretable  models  in  our  study 
and a natural baseline for business applications. SHAP values were computed using the

---

<!-- PAGE 33 -->

Page 33 of 45

Fig. 12  Bootstrap confidence interval comparison for each metric: (a) accuracy, (b) precision, (c) recall, (d) F1, and 
(e) MCC

Table 15  Combined results of McNemar’s test and Cohen’s kappa for model comparisons
Model comparison
LR vs RF
RD vs DT
DT vs XGB
XGB vs KNN

McNemar p-value
0.00024439
3.0985E-32
3.5484E-22
0.63977

Cohen kappa
0.546
0.317
0.291
0.444

LinearExplainer,  with  results  visualized  as  global  feature  importance  rankings  in  Fig-
ure  14a  and  beeswarm  distributions  of  individual  SHAP  contributions  in  Figure  14b. 
The results confirm that repayment history (PAY_0, PAY_3, PAY_5) and billing amounts 
(BILL_AMT1–3, BILL_AMT5) are the most influential predictors of customer default, 
consistent with financial domain expectations. In contrast, demographic variables such

---

<!-- PAGE 34 -->

Page 34 of 45

Fig. 13  McNemar’s test and Cohen’s kappa comparisons

as  SEX  and  EDUCATION  exerted  negligible  influence,  highlighting  the  model’s  reli-
ance on behavioral rather than demographic signals. Importantly, these SHAP explana-
tions provide context for the evaluation metrics examined in this study. For example, the 
strong dominance of repayment-related variables explains why Recall remains unstable 
under threshold changes (since minority-class detection depends heavily on a few repay-
ment indicators). Similarly, the broader balance of billing and repayment features sup-
ports  the  complementary  nature  of  F1-score  and  MCC,  which  integrate  precision  and 
sensitivity trade-offs.

By  combining  conventional  SHAP  outputs  with  metric-specific  analyses,  our  frame-
work  demonstrates  how  interpretability  tools  can  bridge  the  gap  between  raw  perfor-
mance metrics and domain-level decision requirements, ensuring that metric selection 
is not only statistically rigorous but also practically explainable.

Metric-conditioned SHAP analysis (3D threshold interaction)

To  move  beyond  static  feature  importance,  we  applied  our  novel  3D  SHAP  analysis 
framework to investigate how individual features interact with evaluation metrics across 
varying thresholds. The 3D visualizations in Figure 15a through Figure 15e show SHAP 
importance  (Y-axis)  plotted  against  decision  thresholds  (X-axis)  and  metric  scores 
(Z-axis), enabling a dynamic interpretability view tailored to each performance metric.

In Figure 15a, which represents Accuracy, features like LIMIT_BAL and PAY_0 con-
sistently demonstrate high SHAP importance across threshold values. This stability sug-
gests  these  features  reliably  contribute  to  correct  classifications  regardless  of  decision 
boundaries, making accuracy-sensitive models suitable for high-confidence applications 
such as credit approval or transaction filtering. Precision in Figure 15b reveals a more 
selective pattern. SHAP contributions from LIMIT_BAL and PAY_0 peak at mid-range 
thresholds (0.4–0.6), aligning with the metric’s preference for minimizing false positives. 
However,  contributions  from  other  features  such  as  BILL_AMT1  and  PAY_3  sharply 
decline  as  thresholds  increase,  highlighting  the  trade-off  precision  makes  at  higher 
thresholds, often at the cost of sensitivity. The Recall visualization in Figure 15c presents

---

<!-- PAGE 35 -->

Page 35 of 45

Fig. 14  SHAP-based model interpretability for Logistic Regression. (a) Global feature importance based on mean 
absolute SHAP values. (b) Beeswarm plot showing the distribution of SHAP values across individual predictions

a  contrasting  behavior.  Here,  SHAP  values  for  almost  all  features,  particularly  PAY_0, 
AGE, and PAY_3, decrease rapidly as thresholds rise. This is consistent with recall’s sen-
sitivity to false negatives; as the model becomes more conservative, it misses more posi-
tive cases, and the features driving true positive capture lose influence. For business use 
cases focused on early risk detection or churn prevention, such patterns underscore the 
cost of threshold tuning on recall-driven models.

In Figure 15d, the F1-score–being the harmonic mean of precision and recall–exhib-
its a more balanced SHAP profile. Features like PAY_0, BILL_AMT2, and PAY_AMT1 
maintain  moderately  high  importance  across  thresholds,  particularly  in  the  0.3–0.6 
range where the F1-score tends to peak. This balanced feature attribution reinforces F1’s 
utility in capturing both class sensitivity and specificity, making it a stable and adaptable 
metric for business contexts with imbalanced classes.

The MCC plot in Figure 15e further validates these observations. LIMIT_BAL, PAY_0, 
and PAY_AMT1 show consistently strong SHAP contributions across thresholds, indi-
cating  that  MCC–like  F1–captures  balanced  class  performance  but  with  additional 
sensitivity  to  all  four  confusion  matrix  categories.  Notably,  MCC  also  reveals  subtler 
contributions  from secondary features like AGE and PAY_3, which are less prominent 
under metrics like Precision or Accuracy.

Taken  together,  these  visualizations  illustrate  how  each  metric  aligns  with  differ-
ent feature behaviors under threshold shifts. Our 3D SHAP analysis not only enhances 
model interpretability but also provides practical guidance: F1-score and MCC emerge 
as  the  most  stable  and  balanced  metrics  for  business  classification  under  class  imbal-
ance, while Accuracy and Precision may be preferable when robustness or specificity are 
prioritized. This analysis empowers practitioners to align metric choice with both per-
formance goals and feature behavior.

---

<!-- PAGE 36 -->

Page 36 of 45

Fig. 15  SHAP feature impact analysis across thresholds: (a) SHAP for accuracy, (b) SHAP for precision, (c) SHAP for 
recall, (d) SHAP for F1, and (e) SHAP for MCC

Additional experiment on telco customer churn dataset

To  further  validate  the  robustness  and  generalizability  of  our  results,  we  extended 
our  analysis  to  the  Telco  Customer  Churn  dataset  (7,043  instances  and  20+  features), 
sourced from Kaggle. This dataset addresses a binary classification problem predicting 
customer churn, where the target variable denotes whether a customer has left (’Yes’) or 
remained (’No’). The dataset is imbalanced, with approximately 26.5% of customers hav-
ing churned, making it suitable for examining the performance of models on imbalanced 
data.

---

<!-- PAGE 37 -->

Page 37 of 45

Cross-validation results

The cross-validation results in Table 16 highlight that LR achieved the highest Accuracy 
(0.803) but had a relatively low Recall (0.548), indicating its inability to effectively pre-
dict churned customers. RF performed slightly lower with Accuracy (0.793) but showed 
similarly  low  Recall  (0.493),  which  is  not  ideal  for  imbalanced  classification  problems. 
In contrast, XGB achieved the highest F1-score (0.562) by maintaining a good balance 
between Precision (0.611) and Recall (0.521). This suggests that the F1-score, which bal-
ances both Precision and Recall, is a highly effective metric in business data mining for 
imbalanced datasets. KNN and DT performed poorly in comparison, especially in Preci-
sion and MCC, underlining their limited suitability for this task.

Noise robustness testing

The  noise  robustness  testing  results  Table  17  indicate  that  XGB  remained  stable  even 
with  increasing  noise  levels  (0.0  to  0.3),  maintaining  solid  F1-scores  and  MCC  values. 
This resilience to noise makes XGB a robust model for real-world business applications, 
where  noisy  data  is  common.  LR  and  RF  showed  relatively  stable  MCC  values  under 
noise  conditions,  further  supporting  their  reliability.  However,  KNN  and  DT  showed 
more sensitivity to noise, with a more significant decline in performance.

Bootstrap confidence intervals

The bootstrap confidence intervals for each model Table 18 further validate XGB’s reli-
ability.  The  F1-score  and  MCC  for  XGB  showed  the  most  stable  confidence  intervals, 
with  F1-score  CI  ranging  from  0.2141  to  0.2968  and  MCC  CI  from  0.2279  to  0.3550. 
In  comparison,  LR  and  RF  showed  wider  intervals,  particularly  for  Recall  and  MCC, 
indicating  more  variability  in  performance.  The  narrow  confidence  intervals  for  XGB 
reinforce  the  conclusion  that  F1-score  and  MCC  are  the  best  metrics  for  evaluating 
imbalanced datasets in business data mining.

McNemar’s test & cohen’s kappa

Statistical  significance  between  model  pairs  was  assessed  using  McNemar’s  test  and 
Cohen’s  Kappa  Table  19.  XGB  showed  significant  performance  differences  compared 
to other models, particularly in its Precision and Recall, as evidenced by the McNemar 
p-value of 0.0245 in the comparison with KNN. Cohen’s Kappa confirmed that XGB had 
higher agreement with other models, particularly in predicting churn, further highlight-
ing its superiority in this task.

Metric-conditioned SHAP analysis with telco customer churn dataset

To  understand  the  influence  of  feature  importance  on  model  decisions  across  differ-
ent performance metrics, we conducted SHAP-based explainable AI analysis using 3D

Table 16  Cross-validation results for the Telco Customer Churn dataset, including accuracy, 
precision, recall, F1-score, and MCC
Model
LR
RF
DT
XGB
KNN

Precision
0.654
0.645
0.498
0.611
0.553

Accuracy
0.803
0.793
0.734
0.785
0.761

Recall
0.548
0.493
0.520
0.521
0.522

F1
0.596
0.558
0.510
0.562
0.537

MCC
0.470
0.430
0.330
0.420
0.380

---

<!-- PAGE 38 -->

Table 17  Noise robustness testing across metrics for the Telco Customer Churn dataset
F1-Score
Noise Level
0.609
0.0
0.569
0.0
0.470
0.0
0.541
0.0
0.540
0.0
0.609
0.1
0.563
0.1
0.534
0.1
0.596
0.1
0.531
0.1
0.599
0.2
0.577
0.2
0.538
0.2
0.555
0.2
0.540
0.2
0.591
0.3
0.550
0.3
0.554
0.3
0.581
0.3
0.552
0.3

Precision
0.648
0.620
0.472
0.568
0.540
0.653
0.636
0.544
0.568
0.535
0.650
0.651
0.496
0.640
0.525
0.641
0.646
0.564
0.555
0.544

Accuracy
0.804
0.788
0.719
0.767
0.756
0.805
0.792
0.757
0.774
0.753
0.802
0.798
0.731
0.791
0.748
0.798
0.792
0.767
0.766
0.758

Model
LR
RF
DT
XGB
KNN
LR
RF
DT
XGB
KNN
LR
RF
DT
XGB
KNN
LR
RF
DT
XGB
KNN

Recall
0.575
0.527
0.468
0.516
0.540
0.570
0.505
0.524
0.628
0.527
0.556
0.519
0.588
0.489
0.556
0.548
0.479
0.546
0.610
0.559

Page 38 of 45

MCC
0.480
0.433
0.279
0.386
0.374
0.482
0.434
0.370
0.441
0.363
0.472
0.452
0.353
0.428
0.368
0.460
0.426
0.397
0.420
0.386

Table 18  Bootstrap confidence intervals with the Telco Customer Churn dataset for performance 
metrics across models 
Model
LR
RF
DT
XGB
KNN
(LR: logistic regression, RF: random forest, DT: decision tree, XGB: XGBoost, KNN: k-nearest neighbors)

MCC CI
(−0.051, 0.050)
(0.199, 0.281)
(0.228, 0.304)
(0.228, 0.355)
(0.228, 0.355)

F1 CI
(0.209, 0.284)
(0.199, 0.281)
(0.228, 0.304)
(0.214, 0.297)
(0.228, 0.355)

Recall CI
(0.199, 0.275)
(0.187, 0.257)
(0.224, 0.303)
(0.205, 0.272)
(0.224, 0.305)

Accuracy CI
(0.601, 0.645)
(0.607, 0.654)
(0.589, 0.632)
(0.597, 0.645)
(0.586, 0.633)

Precision CI
(0.220, 0.307)
(0.221, 0.318)
(0.221, 0.277)
(0.216, 0.312)
(0.213, 0.309)

Table 19  Results of McNemar’s test and Cohen’s kappa for pairwise model comparisons on the 
Telco Customer Churn dataset
Model Comparison
LR vs RF
RF vs DT
DT vs XGB
XGB vs KNN

McNemar p-value
0.101
0.000
0.058
0.025

Cohen’s Kappa
0.669
0.527
0.528
0.595

visualizations. Figure 16a through Figure 16e illustrate the variation of SHAP values with 
respect to classification thresholds and their respective impact on Accuracy, Precision, 
Recall, F1-score, and MCC. Each figure represents a 3D plot where the x-axis denotes 
the classification threshold, the y-axis corresponds to the SHAP value (indicating feature 
importance),  and  the  z-axis  presents  the  value  of  the  respective  performance  metric. 
In  Figure  16a,  representing  SHAP  impact  on  Accuracy,  the  curves  reveal  that  Accu-
racy  peaks  around  threshold  values  of  0.5  to  0.6,  but  varies  significantly  with  feature 
influence.  Notably,  features  such  as  InternetService_No,  MonthlyCharges,  and  tenure 
dominate  the  model’s  predictive  power.  However,  the  sharp  drops  in  accuracy  beyond 
certain  thresholds  suggest  sensitivity  to  threshold  tuning  and  class  imbalance,  indicat-
ing that Accuracy alone may be unreliable in imbalanced business scenarios. Figure 16b

---

<!-- PAGE 39 -->

Page 39 of 45

Fig. 16  SHAP feature impact analysis across thresholds with the Telco Customer Churn dataset: (a) SHAP for ac-
curacy, (b) SHAP for precision, (c) SHAP for recall, (d) SHAP for F1, and (e) SHAP for MCC

demonstrates SHAP impact on Precision. Precision shows a noticeable spike at higher 
thresholds (around 0.7), but its distribution across features is more uneven. Certain fea-
tures,  especially  InternetService_No  and  ElectronicCheck,  produce  sharp  increases  in 
SHAP values, indicating high but potentially unstable influence. This suggests that while 
Precision may seem high at certain thresholds, it may favor false negatives and be mis-
leading  without  recall  context.  In  Figure  16c,  we  observe  the  SHAP  impact  on  Recall. 
Here,  most  features  demonstrate  a  steady  decline  in  recall  as  the  threshold  increases, 
confirming that lower thresholds tend to favor true positive recovery. While this stability 
is  beneficial,  high  recall  alone  without  balancing  false  positives  may  not  reflect  overall 
predictive reliability, particularly for business-critical applications like churn detection. 
Figure  16d  provides  insights  into  F1-score,  which  balances  Precision  and  Recall.  The 
SHAP  curves  here  are  more  evenly  distributed,  and  the  metric  reaches  optimal  values 
at  thresholds  around  0.4  to  0.6. This  balanced  behavior  across  features  and  thresholds 
suggests  that  F1-score  is  more  robust  and  interpretable  than  single-dimension  met-
rics,  making  it  highly  suitable  for  imbalanced  business  data  mining  problems.  Finally,

---

<!-- PAGE 40 -->

Page 40 of 45

Figure  16e  illustrates  the  SHAP  analysis  for  MCC.  Similar  to  F1-score,  MCC  also  dis-
plays  smooth  curves  across  thresholds  and  SHAP  values,  with  consistent  contribu-
tions from core features such as tenure, MonthlyCharges, and Contract_Two year. The 
metric’s stability across threshold changes further confirms its value as a balanced and 
reliable  indicator  of  classification  performance  under  imbalanced  conditions.  Overall, 
these SHAP-based visualizations reinforce our conclusion that both F1-score and MCC 
provide the most stable and interpretable metrics for model evaluation in business data 
mining.  Unlike  Accuracy  and  Precision,  which  can  mislead  in  the  presence  of  skewed 
class  distributions,  F1  and  MCC  reflect  more  nuanced,  threshold-robust  insights  into 
model behavior and feature influence.

The additional experiments on the Telco Customer Churn dataset reinforce our ear-
lier  findings  and  provide  further  evidence  for  effective  model  and  metric  selection  in 
imbalanced  business  classification.  Among  the  evaluated  models,  XGB  consistently 
outperformed  others  across  cross-validation,  noise  robustness,  bootstrap  confidence 
intervals, and statistical testing, making it the most reliable choice for churn prediction. 
F1-score and MCC again proved superior to traditional metrics like accuracy and preci-
sion, showing strong stability across thresholds and resilience to data noise. SHAP-based 
explainability  confirmed  these  results,  with  3D  SHAP  visualizations  revealing  that  F1 
and  MCC  captured  consistent,  interpretable  feature  contributions–particularly  from 
tenure,  MonthlyCharges,  and  contract  type–regardless  of  threshold  shifts.  In  contrast, 
accuracy and precision were more sensitive to individual features and less stable across 
decision  boundaries.  Overall,  this  extended  evaluation  confirms  that  XGB,  combined 
with F1-score and MCC, provides a robust and interpretable solution for business-criti-
cal tasks like churn prediction. These results highlight the importance of using advanced 
metrics  and  explainability  tools  when  developing  decision-support  systems  in  imbal-
anced, high-stakes domains.

Discussion

This  study  presents  a  comprehensive  evaluation  of  performance  metric  reliability  for 
imbalanced  classification  in  business  data  mining.  By  analyzing  two  real-world  datas-
ets of differing sizes and domains–the large-scale Default of Credit Card Clients data-
set  (30,000  instances)  and  the  moderately  sized  Telco  Customer  Churn  dataset  (7,043 
instances)–we systematically assessed five machine learning models (LR, RF, DT, XGB, 
and KNN) across a variety of metrics, threshold strategies, noise conditions, and inter-
pretability techniques.

Our  findings  reinforce  the  importance  of  aligning  metric  selection  with  both  the 
intrinsic  data  characteristics  and  the  operational  goals  of  business  decision-making. 
Across both datasets, we observed that threshold selection plays a pivotal role in deter-
mining metric behavior. Static threshold analysis revealed that Accuracy and Precision 
typically peaked at moderate thresholds (0.5–0.7), but consistently failed to account for 
minority class detection, favoring specificity over sensitivity. Conversely, Recall peaked 
at lower thresholds (e.g., 0.1) but rapidly degraded with threshold increases, highlight-
ing its trade-off bias and limited practical utility when used in isolation. These findings 
were  further  validated  through  dynamic  threshold  sensitivity  analysis,  which  allowed 
us to identify the exact thresholds at which each metric achieved optimal performance. 
Notably, both F1-score and MCC achieved their best balance between false positives and

---

<!-- PAGE 41 -->

Page 41 of 45

false negatives at thresholds between 0.3 and 0.5, a result consistently observed across 
both datasets and model architectures [63].

Robustness testing under varying levels of synthetic noise offered further insights into 
metric stability. As expected, LR and RF exhibited relatively stable Accuracy and Preci-
sion across noise conditions, particularly in the Telco dataset, where the signal-to-noise 
ratio  was  narrower.  DT  performance,  however,  fluctuated  considerably.  Importantly, 
Recall emerged as the most noise-sensitive metric, often producing unstable outputs in 
both datasets. In contrast, F1-score and MCC maintained more consistent performance 
across  all  noise  levels,  reaffirming  their  value  for  real-world  applications  where  data 
imperfections are common [64].

To establish statistical validity, we conducted ANOVA and McNemar’s tests across all 
model-metric  combinations  [65].  Accuracy  and  Precision  often  failed  to  yield  statisti-
cally significant differences between models, underscoring their limited discriminatory 
power in imbalanced settings [66]. On the other hand, F1-score and MCC showed sig-
nificant inter-model variation across both datasets. For instance, the F1-score was sta-
tistically superior when comparing RF to LR on the credit default dataset, while MCC 
significantly differentiated RF and XGB on the churn dataset [67]. These results demon-
strate that F1 and MCC are not only more stable but also more diagnostically useful for 
comparative model evaluation in imbalanced classification.

Beyond performance scores, we incorporated a two-stage explainable AI (XAI) analy-
sis using SHAP to examine feature contributions across evaluation metrics and decision 
thresholds. In the first stage, conventional SHAP plots (e.g., bar and beeswarm) applied 
to  the  LR  model  identified  key  predictive  drivers–such  as  PAY_0  and  LIMIT_BAL  in 
the  credit  default  dataset,  and  tenure  and  Contract  type  in  the  churn  dataset–consis-
tent  with  domain  expectations  [68].  In  the  second  stage,  we  introduced  a  novel  3D 
SHAP framework to assess how feature importance evolved across thresholds and met-
rics. This dynamic analysis revealed that Accuracy and Precision were driven by high-
specificity features whose contributions declined at extreme thresholds, while F1-score 
and MCC exhibited more stable and distributed feature influence. This dual-layer XAI 
approach  enhanced  both  global  and  threshold-specific  interpretability,  reinforcing  the 
practical advantage of metrics like F1 and MCC in real-world decision contexts where 
model transparency is essential [69].

From a business perspective, the cost of false negatives–such as missed loan defaults 
or undetected customer churn–is often significantly higher than that of false positives. 
In such high-stakes contexts, the F1-score offers a reliable trade-off metric by balancing 
precision and recall. MCC further strengthens evaluation by considering all elements of 
the confusion matrix, making it especially useful in operational settings where misclas-
sification costs are asymmetrical but not always explicitly defined.

To broaden our analysis, we also evaluated four alternative metrics commonly used in 
imbalanced classification: AUC, G-Mean, Balanced Accuracy, and the Index of Balanced 
Accuracy (IBA, with α = 0.1). Models such as DT and RF performed well under these 
metrics, particularly in terms of G-Mean and AUC. However, these alternatives lacked 
the statistical consistency and interpretive robustness observed with F1-score and MCC, 
reinforcing our choice to prioritize the latter in our main analysis.

In addition, we implemented a cost-sensitive evaluation framework that applied busi-
ness-relevant  penalties  to  misclassifications  using  Expected  Cost  of  Misclassification

---

<!-- PAGE 42 -->

Page 42 of 45

(ECM)  and  Net  Profit.  This  revealed  that  models  with  higher  recall–such  as  the  DT–
achieved  lower  overall  cost,  despite  having  lower  MCC  or  precision  scores.  These 
findings  underscore  the  importance  of  aligning  metric  selection  not  only  with  data 
characteristics  but  also  with  domain-specific  cost  structures.  Together,  they  reaffirm 
F1-score and MCC as both statistically sound and operationally meaningful metrics for 
imbalanced business classification.

In  conclusion,  our  study  proposes  a  statistically  grounded  and  interpretable  frame-
work for selecting performance metrics in business data mining. By integrating dynamic 
thresholding,  noise  robustness  testing,  inferential  statistics,  and  SHAP-based  explain-
ability,  we  provide  a  generalizable  methodology  for  model  evaluation  on  imbalanced 
datasets.  This  approach  equips  practitioners  and  researchers  with  the  tools  needed 
to  make  evidence-based  decisions  in  predictive  modeling,  ensuring  both  robustness 
and  transparency  in  high-stakes  applications.  Future  work  can  extend  this  framework 
to  unstructured  data  types  or  incorporate  real-time  cost-aware  decision  systems  in 
dynamic business environments.

Limitations

While  our  study  offers  a  comprehensive  and  statistically  rigorous  framework  for  eval-
uating  performance  metrics  in  imbalanced  business  data  mining,  several  limitations 
should  be  acknowledged.  First,  although  we  examined  two  real-world  business  datas-
ets–one  large-scale  (credit  card  default)  and  one  smaller-scale  (customer  churn)–both 
originate  from  structured  tabular  domains.  Future  research  should  consider  a  broader 
range  of  dataset  sizes,  structures,  and  industries  to  better  assess  the  generalizability 
of  our  findings.  Second,  our  evaluation  focused  on  five  widely  used  machine  learning 
models, including both linear and tree-based methods. However, we did not incorporate 
deep learning architectures, which may yield different patterns in both performance and 
explainability–particularly  in  high-dimensional  or  unstructured  data  contexts.  Third, 
while our primary analysis concentrated on five core evaluation metrics–Accuracy, Pre-
cision,  Recall,  F1-score,  and  MCC–we  also  included  supplementary  results  for  alter-
native  metrics  such  as  AUC,  G-Mean,  Balanced  Accuracy,  and  IBA.  These  additional 
metrics were analyzed descriptively to broaden the scope of our findings but were not 
subjected to the same level of statistical testing or interpretability analysis. Future stud-
ies  could  more  deeply  investigate  the  statistical  robustness  and  explainability  of  these 
alternative  metrics.  Fourth,  although  we  introduced  a  cost-sensitive  evaluation  frame-
work and analyzed Expected Cost of Misclassification (ECM) and Net Profit, we did not 
incorporate  other  domain-specific  constraints  such  as  real-time  decision  thresholds, 
risk-based  optimization,  or  adaptive  cost  matrices.  These  remain  important  areas  for 
operationalizing evaluation metrics in live business systems. Finally, this study focused 
on  classification-based  business  predictive  modeling.  Extending  the  framework  to 
other decision-support contexts such as forecasting, optimization, or recommendation 
remains an open avenue for future work.

Conclusion

This comprehensive research presents a statistically grounded and interpretable frame-
work for selecting performance metrics in business data mining tasks involving imbal-
anced  datasets.  Using  two  real-world  benchmarks–the  Default  of  Credit  Card  Clients

---

<!-- PAGE 43 -->

Page 43 of 45

and  the  Telco  Customer  Churn  datasets–we  evaluated  five  machine  learning  models 
through a multidimensional approach incorporating cross-validation, threshold sensitiv-
ity,  noise  robustness,  inferential  statistics,  and  SHAP-based  explainability.  Our  results 
show that Accuracy and Precision are inadequate in imbalanced contexts, as they favor 
the majority class and underrepresent minority outcomes. Recall, though more sensitive 
to the minority class, showed instability across thresholds and noise levels. In contrast, 
F1-score demonstrated the most reliable and balanced performance across all scenarios, 
while MCC offered complementary insights by incorporating all elements of the confu-
sion matrix. The addition of a two-layer SHAP framework linked feature importance to 
metric behavior, highlighting how F1-score and MCC maintain interpretability and fea-
ture stability across thresholds. This supports their use in business-critical applications 
where  transparency  and  robustness  are  essential.  Future  research  should  extend  this 
framework  to  multi-class  problems,  cost-sensitive  learning,  and  deep  learning  models 
tailored  for  skewed  data.  Incorporating  real-world  business  constraints  such  as  mone-
tary costs, regulatory compliance, or real-time adaptation will further enhance practical 
utility. In summary, this work provides a comprehensive, interpretable, and transferable 
methodology for metric evaluation in imbalanced classification–empowering practitio-
ners to make evidence-based, risk-aware decisions in predictive modeling.
Author contributions
KMS perceived the idea, carried out formal analysis, developed the visualization and methodology, and wrote the draft. 
RH investigated, validated, provided resources, and supervised the study. KC and MAS administrated the project, and 
participated in reviewing the initial draft, modified it, and considerably improved it.

Funding
This work was supported in part by the Institute of Information and Communications Technology Planning and 
Evaluation (IITP) funded by Korean Government through the Ministry of Science and ICT (MSIT) under Grant 2022-0-
00024, and in part by the National Research Foundation of Korea (NRF) funded by Korea Government (MSIT) under Grant 
RS-2024-00452791.

Data availability
The datasets analyzed during this study are publicly available at  h t t p s  : / / a r c  h i v e .  i c s .  u c i . e d u / d a t a s e t / 3 5 0 / d e f a u l t + o f + c r e 
d i t + c a r d + c l i e n t s (accessed on 16 Dec. 2024), and at  h t t p s  : / / w w w  . k a g g  l e . c  o m / d a t a s e t s / b l a s t c h a r / t e l c o - c u s t o m e r - c h u r n 
(accessed on 11 Jun. 2025).

Declarations

Competing interests
The authors declare no competing interests.

Received: 11 June 2025 / Accepted: 8 October 2025

References
1.

2.

3.

4.

5.

6.

Bhatia S, Sharma P, Burman R, Hazari S, Hande R. Credit scoring using machine learning techniques. Int J Comput Appl. 
2017;161(11):1–4.
Saito T, Rehmsmeier M. The precision-recall plot is more informative than the roc plot when evaluating binary classifiers 
on imbalanced datasets. PLoS ONE. 2015. https://doi.org/10.1371/journal.pone.0118432.
Juba B, Le HS. Precision-recall versus accuracy and the role of large data sets. Proceedings of the AAAI Conference on 
Artificial Intelligence. 2019;33:4039–48.
Boughorbel S, Jarray F, El-Anbari M. Optimal classifier for imbalanced data using matthews correlation coefficient metric. 
PLoS ONE. 2017. https://doi.org/10.1371/journal.pone.0177678.
Xu X, Chen W, Sun Y. Over-sampling algorithm for imbalanced data classification. JSEE. 2019.  h t t p s : / / d o i . o r g / 1 0 . 2 1 6 2 9 / j s e e . 
2 0 1 9 . 0 6 . 1 2     .   
Shaer L, Kanj R, Joshi R. Data imbalance handling approaches for accurate statistical modeling and yield analysis of 
memory designs. 2019 IEEE International Symposium on Circuits and Systems (ISCAS), 1–5 2019  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / I S 
C A S . 2 0 1 9 . 8 7 0 2 7 3 1

7.  Wu X, Huang F, Huang H. Fast stochastic recursive momentum methods for imbalanced data mining. 2022 IEEE Interna-

tional Conference on Data Mining (ICDM), 578–587 (2022) https://doi.org/10.1109/ICDM54844.2022.00068

---

<!-- PAGE 44 -->

Page 44 of 45

8.

9.

Sujon KM, Hassan R, Khairudin AR, Moi SH, Shafie MLM, Saringat Z, et al. The effects of imbalanced datasets on machine 
learning algorithms in predicting student performance. JOIV: International Journal on Informatics Visualization. 
2024;8(3–2):1599–605.
Japkowicz N. Assessment metrics for imbalanced learning. Imbalanced learning: Foundations, algorithms, and applica-
tions, 2013;187–206

10.  Ferri C, Hernández-Orallo J, Modroiu R. An experimental comparison of performance measures for classification. Pattern

Recogn Lett. 2009;30(1):27–38.

11.  Kubat M. Addressing the curse of imbalanced training sets: one-sided selection. In: Proceedings of the 14th International

Conference on Machine Learning, pp. 179–186 (1997). Morgan Kaufmann

12.  Diallo R, Edalo C, Awe OO. Machine learning evaluation of imbalanced health data: A comparative analysis of balanced

accuracy, mcc, and f1 score. In: Awe, O.O., Vance, E.A. (eds.) Practical Statistical Learning and Data Science Methods: Case 
Studies from LISA 2020 Global Network, USA. STEAM-H: Science, Technology, Engineering, Agriculture, Mathematics & 
Health, pp. 283–312. Springer, Cham (2024). https://doi.org/10.1007/978-3-031-72215-8_12

13.  Zareapoor M, Shamsolmoali P. Boosting prediction performance on imbalanced dataset. Int J Inf Commun Technol.

14.

2018;13:186–95. https://doi.org/10.1504/IJICT.2018.10011701.
Imran M, Qyser A, Ali SS, Kumar V, Jah M, Malla N. An overview on data mining designed for imbalanced datasets. Interna-
tional Journal of Research in Engineering and Technology. 2014;03:222–5. https://doi.org/10.15623/IJRET.2014.0310034.
15.  Chakraborty T. Imbalanced ensemble classifier for learning from imbalanced business school dataset. International Jour-
nal of Mathematical, Engineering and Management Sciences 2018; https://doi.org/10.33889/IJMEMS.2019.4.4-068

16.  Lee Z, Lee C-Y, Chou S-T, Ma W-P, Ye F, Chen Z. A hybrid system for imbalanced data mining. Microsyst Technol.

2020;26:3043–7. https://doi.org/10.1007/S00542-019-04566-1.

17.  Syaripudin A, Khodra ML. A comparison for handling imbalanced datasets. 2014 International Conference of Advanced 
Informatics: Concept, Theory and Application (ICAICTA), 293–298 (2014) https://doi.org/10.1109/ICAICTA.2014.7005957
18.  Vluymans S. Learning from imbalanced data. Dealing with Imbalanced and Weakly Labelled Data in Machine Learning

using Fuzzy and Rough Set Methods. 2018. https://doi.org/10.1007/978-3-030-04663-7_4.

19.  Yan Y, Liu Y, Shyu M, Chen M. Utilizing concept correlations for effective imbalanced data classification. Proceedings of the 
2014 IEEE 15th International Conference on Information Reuse and Integration (IEEE IRI 2014), 561–568 (2014)  h t t p s : / / d o i . 
o r g / 1 0 . 1 1 0 9 / I R I . 2 0 1 4 . 7 0 5 1 9 3 9

20.  Veganzones D, Séverin E. An investigation of bankruptcy prediction in imbalanced datasets. Decis Support Syst.

2018;112:111–24. https://doi.org/10.1016/j.dss.2018.06.011.

21.  Susan S, Kumar A. The balancing trick: optimized sampling of imbalanced datasets-a brief survey of the recent state of the

art. Eng Rep (Hoboken). 2020. https://doi.org/10.1002/eng2.12298.

22.  Barella VH, Garcia LPF, Souto MD, Lorena AC, Carvalho A. Assessing the data complexity of imbalanced datasets. Inf Sci.

2021;553:83–109. https://doi.org/10.1016/j.ins.2020.12.006.

23.  Wu F, Jing X, Shan S, Zuo W, Yang J-y. Multiset feature learning for highly imbalanced data classification. IEEE Trans Pattern

Anal Mach Intell. 2021;43:139–56.

24.  Tao X, Li Q, Ren C, Guo W, Li C, He Q, et al. Real-value negative selection over-sampling for imbalanced data set learning.

Expert Syst Appl. 2019;129:118–34. https://doi.org/10.1016/J.ESWA.2019.04.011.

25.  Mathews L, Hari S. Learning from imbalanced data. Advances in Computer and Electrical Engineering. 2019.  h t t p s :  / / d o i  . o r

g / 1  0 . 4 0  1 8 / 9 7  8 - 1 - 5  2 2 5 - 2 2  5 5 - 3  . C H 1 5 9.

26.  Zhao J, Jin J, Chen S, Zhang R, Yu B, Liu Q. A weighted hybrid ensemble method for classifying imbalanced data. Knowl-

Based Syst. 2020;203:106087. https://doi.org/10.1016/j.knosys.2020.106087.

27.  Bekkar M, Djemaa H, Alitouche TA. Evaluation measures for models assessment over imbalanced data sets. Journal of

Information Engineering and Applications. 2013;3:27–38.

28.  Basha SJ, Madala S, Vivek K, Kumar ES, Ammannamma T. A review on imbalanced data classification techniques. 2022

International Conference on Advanced Computing Technologies and Applications (ICACTA), 1–6 (2022)  h t t p s :  / / d o i  . o r g / 1  0 . 
1 1  0 9 / I C  A C T A 5  4 4 8 8 . 2  0 2 2 .  9 7 5 3 3 9 2

29.  Öztürk MM. Which type of metrics are useful to deal with class imbalance in software defect prediction? Inf Softw Technol.

2017;92:17–29.

30.  Cruz Huayanay A, Bazán JL, Russo CM. Performance of evaluation metrics for classification in imbalanced data. Comput

Stat. 2025;40(3):1447–73.

31.  Fawcett T. An introduction to roc analysis. Pattern Recognit Lett. 2006;27(8):861–74.
32.  García V, Mollineda RA, Sánchez JS. A bias correction function for classification performance assessment in two-class

33.

imbalanced problems. Knowledge-Based Systems. 2014;59:66–74.
Jiménez-Navarro M, Troncoso-García A, Troncoso A, Martínez-Álvarez F, Martínez-Ballesteros M. Explainable deep learning 
with embedded feature selection for electricity demand forecasting. In: 2024 International Conference on Smart Systems 
and Technologies (SST), pp. 153–158 (2024). IEEE

34.  Troncoso-Garcia AR, Martinez-Ballesteros M, Martinez-Alvarez F, Troncoso A. A new metric based on association rules to 
assess feature-attribution explainability techniques for time series forecasting. IEEE Trans Pattern Anal Mach Intell. 2025. 
https://doi.org/10.1109/TPAMI.2025.3540513.

35.  Troncoso-García A, Martínez-Ballesteros M, Martínez-Álvarez F, Troncoso A. Explainable machine learning for sleep apnea

prediction. Procedia Comput Sci. 2022;207:2930–9.

36.  Kadir MA, Mosavi A, Sonntag D. Evaluation metrics for xai: A review, taxonomy, and practical applications. In: 2023 IEEE

27th International Conference on Intelligent Engineering Systems (INES), pp. 000111–000124 (2023). IEEE

37.  Wong T-T, Chung P-C. A consistency analysis on four evaluation metrics for classifying imbalanced data. Knowledge and

Information Systems, 2025; 1–18

38.  Mahmud Sujon K, Binti Hassan R, Tusnia Towshi Z, Othman MA, Abdus Samad M, Choi K. When to use standardization and 
normalization: empirical evidence from machine learning models and xai. IEEE Access. 2024;12:135300–14.  h t t p s : / / d o i . o r g 
/ 1 0 . 1 1 0 9 / A C C E S S . 2 0 2 4 . 3 4 6 2 4 3 4     .

39.  Bolton RJ, Hand DJ. Statistical fraud detection: a review. Stat Sci. 2002;17(3):235–55.
40.  Khalilia M, Chakraborty S, Popescu M. Predicting disease risks from highly imbalanced data using random forest. BMC Med

Inform Decis Mak. 2011;11:1–13.

---

<!-- PAGE 45 -->

Page 45 of 45

41.  Gilmore E, Estivill-Castro V, Hexel R. More interpretable decision trees. In: Hybrid Artificial Intelligent Systems: 16th Interna-
tional Conference, HAIS 2021, Bilbao, Spain, September 22–24, 2021, Proceedings 16, pp. 280–292 (2021). Springer

42.  Chen T, Guestrin C. Xgboost: A scalable tree boosting system. In: Proceedings of the 22nd Acm Sigkdd International

Conference on Knowledge Discovery and Data Mining, 2016;pp. 785–794

43.  Halder RK, Uddin MN, Uddin MA, Aryal S, Khraisat A. Enhancing k-nearest neighbor algorithm: a comprehensive review

and performance analysis of modifications. J Big Data. 2024;11(1):113.

44.  Brownlee J. Failure of classification accuracy for imbalanced class distributions. Machine Learning Mastery. 2020;31.
45.  Najem SM, Kadeem SM. A survey on fraud detection techniques in e-commerce. Tech-Knowledge. 2021;1(1):33–47.
46.  Zeynali Tazehkandi M, Nowkarizi M. Three approaches to measuring recall on the web: a systematic review. Electron Libr.

47.

2020;38(3):477–92.
Jeni LA, Cohn JF, De La Torre F. Facing imbalanced data–recommendations for the use of performance metrics. In: 2013 
Humaine Association Conference on Affective Computing and Intelligent Interaction, pp. 245–251 (2013). IEEE

48.  Chicco D, Jurman G. The advantages of the matthews correlation coefficient (MCC) over f1 score and accuracy in binary

classification evaluation. BMC Genomics. 2020;21:1–13.

49.  Alsulmi M. From ranking search results to managing investment portfolios: exploring rank-based approaches for portfolio

stock selection. Electronics. 2022;11(23):4019.

50.  Alsubaie Y, El Hindi K, Alsalman H. Cost-sensitive prediction of stock price direction: selection of technical indicators. IEEE

Access. 2019;7:146876–92.

51.  Szeghalmy S, Fazekas A. A comparative study of the use of stratified cross-validation and distribution-balanced stratified

cross-validation in imbalanced learning. Sensors. 2023;23(4):2333.

52.  Pembury Smith MQ, Ruxton GD. Effective use of the mcnemar test. Behav Ecol Sociobiol. 2020;74:1–9.
53.  Aguirre-Urreta MI, Rönkkö M. Statistical inference with plsc using bootstrap confidence intervals. MIS Q.

2018;42(3):1001–10.

54.  Więckowska B, Kubiak KB, Jóźwiak P, Moryson W, Stawińska-Witoszyńska B. Cohen’s kappa coefficient as a measure to

assess classification improvement following the addition of a new marker to a regression model. Int J Environ Res Public 
Health. 2022;19(16):10213.

55.  Chase Lipton Z, Elkan C, Narayanaswamy B. Thresholding classifiers to maximize f1 score. arXiv e-prints, 2014; 1402
56.

Jiang J, Jiang X, Xu L, Zhang Y, Zheng Y, Kong D. Noise-robustness test for ultrasound breast nodule neural network mod-
els as medical devices. Front Oncol. 2023;13:1177225.

57.  Knief U, Forstmeier W. Violating the normality assumption may be the lesser of two evils. Behav Res Methods.

2021;53(6):2576–90.

58.  Yeh I-C, Lien C-h. Default of Credit Card Clients Dataset. UCI Machine Learning Repository 2009;  h t t p s : / / d o i . o r g / 1 0 . 2 4 4 3 2 /

C 5 5 S 3 H     .

59.  Azis H. Assessing the performance of logistic regression in heart disease detection through 5-fold cross-validation. Inter-

national Journal of Artificial Intelligence in Medical Issues. 2024;2(1):1–11.

60.  Maina DG, Moso JC, Gikunda PK. Detecting fraud in motor insurance claims using xgboost algorithm with smote. In: 2023 
International Conference on Information and Communication Technology for Development for Africa (ICT4DA), 2023;pp. 
61–66 . IEEE

61.  Basak S, Huber M. Evolutionary feature scaling in k-nearest neighbors based on label dispersion minimization. In: 2020 IEEE

International Conference on Systems, Man, and Cybernetics (SMC), 2020; pp. 928–935. IEEE

62.  Kusa W, Peikos G, Staudinger M, Lipani A, Hanbury A. Normalised precision at fixed recall for evaluating tar. In: Proceedings

of the 2024 ACM SIGIR International Conference on Theory of Information Retrieval, 2024; pp. 43–49

63.  Foody GM. Challenges in the real world use of classification accuracy metrics: from recall and precision to the matthews

correlation coefficient. PLoS ONE. 2023;18(10):0291908.

64.  Tang J, Li Y, Hou Z, Fu S, Tian Y. Robust two-stage instance-level cost-sensitive learning method for class imbalance prob-

lem. Knowledge-Based Systems. 2024;300:112143.

65.  Chen X, Chen P. A comparison of four methods for the analysis of n-of-1 trials. PLoS ONE. 2014.  h t t p s : / / d o i . o r g / 1 0 . 1 3 7 1 / j o u

r n a l . p o n e . 0 0 8 7 7 5 2     .

66.  Owusu-Adjei M, Hayfron-Acquah JB, Frimpong T, Abdul-Salaam G. Imbalanced class distribution and performance evalua-
tion metrics: a systematic review of prediction accuracy for determining model performance in healthcare systems. PLoS 
Digit Health. 2023. https://doi.org/10.1371/journal.pdig.0000290.

67.  Wardhani NWS, Rochayani MY, Iriany A, Sulistyono A, Lestantyo P. Cross-validation metrics for evaluating classification

performance on imbalanced data. 2019 International Conference on Computer, Control, Informatics and its Applications 
(IC3INA), 14–18 (2019)  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  3 I N A 4  8 0 3 4 . 2  0 1 9 .  8 9 4 9 5 6 8

68.  Explaining xgboost predictions with shap value. A comprehensive guide to interpreting decision tree-based models. New

Trends in Computer Sciences. 2023. https://doi.org/10.3846/ntcs.2023.17901.

69.  Mokhtari KE, Higdon BP, Başar A. Interpreting financial time series with shap values. In: Proceedings of the 29th Annual

International Conference on Computer Science and Software Engineering, 2019;pp. 166–172

Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Sujon et al. Journal of Big Data (2025) 12:268 Journal of Big Data
https://doi.org/10.1186/s40537-025-01313-4
RESEARCH Open Access
Accuracy, precision, recall, f1-score, or MCC?
empirical evidence from advanced statistics,
ML, and XAI for evaluating business predictive
models
Khaled Mahmud Sujon1, Rohayanti Hassan2, Kwonhue Choi3* and Md Abdus Samad3*
*Correspondence:
Kwonhue Choi Abstract
gonew@yu.ac.kr Imbalanced datasets pose a persistent challenge in business data mining, particularly
Md Abdus Samad
in high-stakes domains such as financial risk prediction and customer churn analysis,
masamad@yu.ac.kr
1Department of Software where the minority class often carries disproportionate operational and financial
Engineering, Universiti Teknologi consequences. Although widely used evaluation metrics–such as accuracy, precision,
Malaysia (UTM), Johor Bahru,
recall, F1-score, and Matthews Correlation Coefficient (MCC)–are commonly applied
Johor 81310, Malaysia
2Faculty of Computing, Universiti in practice, there remains no empirical consensus on which metric offers the most
Teknologi Malaysia (UTM), Johor reliable performance under real-world conditions. Existing studies lack a unified,
Bahru, Johor 81310, Malaysia
statistically validated framework that accounts for threshold sensitivity, input noise,
3Department of Information and
Communication Engineering, and interpretability–factors critical to business decision-making. To address this gap,
Yeungnam University, we present a comprehensive and statistically rigorous evaluation of performance
Gyeongsan 38541, South Korea
metrics for imbalanced business classification tasks. Using two benchmark datasets
with distinct sizes and imbalance ratios–the Default of Credit Card Clients dataset
and the Telco Customer Churn dataset–we evaluate five commonly used machine
learning models: Logistic Regression (LR), Decision Tree (DT), Random Forest
(RF), Extreme Gradient Boosting (XGBoost), and k-Nearest Neighbors (KNN). Our
methodology incorporates static and dynamic threshold analysis, Gaussian noise
robustness testing, bootstrap confidence intervals, McNemar’s test, Cohen’s kappa,
and analysis of variance (ANOVA) to assess the statistical reliability of performance
metrics. In addition, we introduce a novel two-stage explainable artificial intelligence
(XAI) framework using SHapley Additive exPlanations (SHAP). The first stage
employs standard SHAP visualizations (bar and beeswarm plots) to ensure baseline
interpretability. The second stage extends this with a novel 3D metric-conditioned
SHAP analysis, linking feature contributions to variations in classification thresholds
and evaluation metrics. Our findings show that the F1-score consistently provides
the most stable and balanced evaluation across datasets and testing conditions, with
MCC offering complementary diagnostic value. In contrast, accuracy and precision
demonstrate limited robustness under class imbalance. By combining statistical rigor
with interpretable AI, this study offers the most comprehensive guidance to date for
© The Author(s) 2025. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit h t t p : / / c e r a t i v e c o m m o n .s o r g / l i c e n s
e s / b y - n c - n d / 4 . 0. /

Sujon et al. Journal of Big Data (2025) 12:268 Page 2 of 45
selecting performance metrics in imbalanced business classification, with practical
implications for model deployment in finance, marketing, and customer analytics.
Keywords Business, Data mining, Machine learning, Imbalanced datasets, Explainable
AI (XAI), Statistics, Accuracy, Precision, F1, MCC
Introduction
In contemporary business environments, leveraging machine learning (ML) for deci-
sion-making has become indispensable. Applications in customer churn prediction,
fraud detection, and financial credit scoring often rely on predictive models trained
on real-world datasets [1]. However, such datasets are frequently imbalanced, where
instances of one class significantly outnumber the other. This imbalance poses substan-
tial challenges to model performance and evaluation, as standard accuracy-focused
metrics fail to adequately assess predictive power across classes. Metrics like precision,
recall, and MCC are better suited to these scenarios but are underutilized in business
data mining applications [2]. Consequently, addressing imbalances effectively while
optimizing performance metrics is critical for deploying reliable ML models in business
settings. Existing studies have advanced our understanding of metric applicability but
have significant limitations. For instance, [3] demonstrated the inadequacies of accuracy
in imbalanced datasets but did not explore alternative metrics in depth. Similarly, [4]
advocated the use of MCC for binary classification but lacked a comparative evaluation
of MCC against other metrics like F1-score and precision. [5] optimized oversampling
techniques for imbalanced data but neglected to consider dynamic thresholds or noise
robustness. Moreover, [6] demonstrated the potential of oversampling for yield estima-
tion in industrial applications but did not extend their methodology to broader business
datasets. Finally, [7] highlighted the effectiveness of Area Under the Precision-Recall
Curve (AUPRC) optimization for imbalanced datasets but did not integrate explainable
AI (XAI) tools to interpret model outputs. Despite these advances in the current litera-
ture, several gaps remain. First, a comprehensive evaluation of many performance indi-
cators encompassing accuracy, precision, recall, F1, and MCC is still unexplored in the
business domain. Second, the implementation of advanced statistical techniques, such
as ANOVA and McNemar’s tests, for optimal metric selection is still underexplored.
Second, the implementation of dynamic and static threshold sensitivity analysis has
not been systematically examined in business data mining. Third, while noise robust-
ness testing has gained traction in other domains, its application to metric evaluation
in business data mining remains completely unexplored. Lastly, the implementation of
XAI techniques like SHAP for metric-based feature impact analysis is still unexplored in
current literature of business data mining. To address the identified gaps in the current
literature on business data mining under class imbalance, the key contributions of our
study are as follows:
• We conduct a comprehensive statistical validation of five most commonly used
performance metrics using ANOVA, McNemar’s test, and bootstrap confidence
intervals to quantify both inter-metric and inter-model differences under imbalanced
conditions.

Sujon et al. Journal of Big Data (2025) 12:268 Page 3 of 45
• We implement both static and dynamic threshold sensitivity analyses to examine
how classification thresholds affect each metric, providing a nuanced understanding
of threshold dependence.
• We evaluate the robustness of performance metrics under varying levels of synthetic
noise to simulate real-world data imperfections, identifying metrics most resilient to
instability.
• We introduce a novel two-stage explainable AI (XAI) framework using SHAP. The
first stage applies conventional SHAP plots for global and local interpretability, while
the second leverages 3D metric-conditioned SHAP visualizations to reveal how
feature importance interacts with threshold variation and metric outcomes.
To shed light on the above-mentioned contributions, our investigation is guided by the
following research questions (RQs):
• RQ1: Which performance metrics among accuracy, precision, recall, F1-score, and
MCC provide the most reliable evaluation for imbalanced classification in business
domains?
• RQ2: How do static and dynamic threshold sensitivity analyses impact metric
outcomes, and how can they be used to determine optimal decision boundaries?
• RQ3: How can advanced statistical methods such as ANOVA, McNemar’s test, and
bootstrap confidence intervals be used to validate and compare metric robustness?
• RQ4: How does input noise affect the stability of different metrics, and which metric
remains most resilient under noisy, real-world business conditions?
• RQ5: How can explainable AI techniques like SHAP help interpret metric behavior
across features and thresholds, and what actionable insights do they provide for
model evaluation?
The reminder sections of this manuscript are structured as follows: Section Literature
Review reviews related work, highlighting gaps in the literature. Section Methodol-
ogy details the methodology, including dataset preprocessing, modeling, and analytical
techniques. Section Experimental Results presents the experimental results, integrat-
ing statistical insights with XAI findings. Section Discussion presents the discussion
and limitations. Finally, Section Conclusion outlines conclusions and proposes future
research directions. With the problem clearly defined in the introduction, we now
review the related literature to identify prevailing methodologies and highlight unre-
solved questions.
Literature review
Imbalanced datasets pose a persistent challenge in business data mining, especially in
high-stakes domains such as credit risk, churn prediction, and fraud detection. In these
settings, minority classes often represent critical outcomes such as defaults, cancella-
tions, and anomalies, yet their underrepresentation leads to biased models and distorted
performance evaluations [8]. Traditional metrics like accuracy frequently fail under
such conditions, as highlighted by [9] and empirically supported by [10], both of whom
recommend alternatives like F1-score and MCC for more balanced evaluation. To miti-
gate sampling bias, [11] proposed one-sided selection, while [12] confirmed MCC and
F1-score as the most stable across varying imbalance ratios in health data.

Sujon et al. Journal of Big Data (2025) 12:268 Page 4 of 45
Despite this, many domain-specific studies still rely on suboptimal practices. For
example, [13] evaluated fraud detection using AUC and precision alone, without sta-
tistical or explainability validation, typifying a broader trend where metric selection is
assumed rather than empirically supported. Similarly, studies like [14–17] rely solely on
accuracy, while others such as [18–20] focus only on precision or recall, omitting met-
rics like MCC and F1 and lacking any statistical or explainability analysis.
Even among works using more robust metrics–such as [21] (F1, AUC), [22–24]
(MCC)–comparative analysis and validation remain absent. Recent applications in
churn prediction and financial modeling [25–28] likewise neglect optimal metric selec-
tion, threshold sensitivity, and interpretability via XAI. [29] evaluated metrics such as
MCC and G-Mean in software defect prediction tasks, finding them to be more robust
than accuracy or AUC. However, the study did not include threshold-based evaluation
or any explainability component. A simulation-based comparison by [30] further ana-
lyzed twelve metrics, including MCC and Cohen’s Kappa, highlighting the superior reli-
ability of MCC under imbalance but lacking any XAI integration. Additional works such
as [27, 28] use multiple metrics (MCC, AUC) but omit statistical or interpretability vali-
dation. Foundational works like [31, 32] discuss ROC limitations and metric bias but do
not explore metric interactions or XAI.
In contrast, explainable AI (XAI) has increasingly gained attention for enhancing
model transparency in high-stakes domains. For example, [33] integrated SHAP with
embedded feature selection in electricity demand forecasting, demonstrating its value in
improving interpretability. [34] proposed a novel metric to validate SHAP-based expla-
nations in time series forecasting, while [35] showcased SHAP’s applicability in health-
care for sleep apnea prediction. Additionally, [36] provided a comprehensive taxonomy
of XAI evaluation techniques, though they noted the lack of standardized metrics and
real-world validations. Despite these advancements, existing studies often treat SHAP
explanations and metric evaluation as separate concerns.
Unlike the study by [37], who examined the consistency of four metrics (AUC, F-mea-
sure, G-mean, MCC) under varying imbalance ratios using correlation and simulation,
our study extends far beyond theoretical consistency analysis. We evaluate five metrics
across real-world business datasets using rigorous statistical tests (ANOVA, McNemar’s
test, bootstrap CI), incorporate static and dynamic threshold sensitivity analysis, and
assess metric robustness under input noise. Whereas their analysis considered metrics
in isolation, our framework explores how metric behavior evolves across model types,
input noise, threshold dynamics, and explainability layers. Most notably, we introduce
a novel two-stage XAI framework, culminating in 3D metric-conditioned SHAP visual-
izations that link feature contributions to metric behavior across thresholds. Our work
provides a unified, statistically grounded, threshold-aware, and explainability-enhanced
approach to performance evaluation, offering greater practical utility than existing con-
sistency-focused studies.
The limitations of existing business studies in handling metric evaluation under class
imbalance are summarized in Table 1, while Table 2 presents recent studies focusing
on evaluation metrics and explainability under imbalanced learning. Collectively, these
studies underscore the absence of a unified, statistically validated, and explainability-
aware framework for evaluating performance metrics under class imbalance. To bridge
this gap, we evaluate five machine learning models on two real-world imbalanced

Sujon et al. Journal of Big Data          (2025) 12:268  Page 5 of 45
Table 1 Empirical business studies using evaluation metrics under class imbalance and identified
gaps
| Ref. Business dataset  | Metric used | Model used | Identified gap |
| ---------------------- | ----------- | ---------- | -------------- |
used
|  [13] Fraud detection | AUC,  | AdaBoost | No statistical validation or XAI |
| --------------------- | ----- | -------- | -------------------------------- |
precision
 [14] Real-world datasets Accuracy Ensemble learning Only accuracy used, no metric compari-
son or validation
 [21] Marketing datasets F1, AUC Evolutionary  No comparative analysis or statistical
|     |     | methods | validation |
| --- | --- | ------- | ---------- |
 [18] Business performance Precision,  Decision Trees Ignored MCC/F1, no statistical analysis
recall
 [19] Financial datasets Precision Neural networks Precision only; no comparison, no
validation
 [15] MBA student data Accuracy Ensemble learning Accuracy only; no metric selection
analysis
 [22] Banking datasets MCC Complexity-based  No XAI or comparative metric analysis
classifiers
 [23] Financial datasets MCC GANs Only MCC; no validation or explainability
|  [17] Insurance datasets | F1  | AdaBoost | No statistical validation |
| ------------------------ | --- | -------- | ------------------------- |
 [16] Financial transactions Accuracy Spark + SVM Accuracy only; ignores threshold/XAI
 [20] Bankruptcy datasets Recall SVM Recall only; no comparative or XAI analysis
|  [24] Credit scoring    | F1  | RNS classifiers | No statistical or XAI validation  |
| ----------------------- | --- | --------------- | --------------------------------- |
|  [25] Churn prediction  | MCC | Ensemble models | No comparison or explainability   |
|  [28] Business datasets | AUC | Boosting models | No metric selection or validation |
 [26] Churn prediction F1, G-Mean Hybrid ensemble No comparative metric analysis; no XAI
 [27] Churn evaluation MCC, AUC Multiple classifiers No statistical methods or XAI applied
Table 2 Recent studies on metric evaluation and XAI under imbalanced learning
| Ref. Domain | Metric | XAI? Stat.? | Identified gap |
| ----------- | ------ | ----------- | -------------- |
focus
 [9] General Accuracy, F1, MCC ✗ ✗ Conceptual, not empirical comparison
 [10] General Accuracy, F1, ROC, MCC Compared metrics across domains; lacks
✗ ✓
business/XAI focus
 [11] General Sampling, recall ✗ ✗ Sampling-focused, not metric evaluation
|  [12] Health data | Balanced Acc., MCC, F1 | ✗ ✓ | No XAI or threshold variation    |
| ----------------- | ---------------------- | --- | -------------------------------- |
|  [31] General     | ROC                    |     | Lacks imbalance-specific insight |
✗ ✗
 [32] General MCC, ROC ✗ ✓ Focused on bias correction, not metric
interaction
 [29] Software  MCC, G-Mean ✗ ✓ No threshold or explainability analysis
defects
 [30] General 12 metrics incl. MCC, Kappa Lacks XAI and threshold-dependent
✗ ✓
behavior
 [37] General AUC, F-measure, G-mean,  ✗ ✓ Theoretical consistency only; no XAI or
|                    | MCC                      |     | dynamic threshold        |
| ------------------ | ------------------------ | --- | ------------------------ |
|  [33] Electricity  | SHAP + Feature selection | ✓ ✗ | Lacks metric integration |
demand
 [34] Time series Metric for SHAP validation Does not compare traditional metrics
✓ ✗
|  [35] Healthcare | SHAP + Risk prediction | ✓ ✗ | SHAP only; no metric linkage |
| ---------------- | ---------------------- | --- | ---------------------------- |
 [36] General Taxonomy of XAI metrics ✓ ✗ Review only; lacks experimental grounding
datasets–Default of Credit Card Clients and Telco Customer Churn–using a compre-
hensive methodology that includes ANOVA, McNemar’s test, bootstrap confidence
intervals, threshold sensitivity analysis, noise robustness testing, and a novel two-stage
SHAP-based XAI approach. The first stage applies conventional SHAP visualizations
(bar plots and beeswarm plots) for baseline interpretability using LR, while the second

Sujon et al. Journal of Big Data (2025) 12:268 Page 6 of 45
introduces 3D metric-conditioned SHAP analysis to explore how feature contributions
vary across thresholds and relate to performance metrics. This is the first study to jointly
analyze performance metrics across statistical, algorithmic, and interpretability dimen-
sions, offering a generalizable and practitioner-oriented framework for metric selection
in imbalanced business classification tasks.
Methodology
In this section the study presents the methodology of our investigation. The method-
ology of our study is designed to systematically evaluate and select the optimal per-
formance metric for machine learning models applied to business data mining, with
the focus on a large imbalanced Business datasets. To conduct a detailed analysis this
research adopts a multi-faceted analytical framework integrating machine learning,
advanced statistical techniques, and explainable AI (XAI). Figure 1 presents the research
framework of our investigation containing all the phases adopted in this analysis.
Data preparation and preprocessing
The dataset used in this study is the “Default of Credit Card Clients” dataset collected
from UCI Machine Learning, available at the URL1, which consists of 30,000 instances
and 23 features. It contains data from a Taiwanese bank’s credit card clients, specifically
used to predict whether clients will default on their credit card payments. The features
include demographic information, credit-related variables and payment amounts for
six months, and the binary target variable indicating whether a client defaulted in the
following month. Specifically, the target variable is denoted as DEFAULT_PAYMENT_
NEXT_MONTH, where 1 represents default and 0 indicates no default. The features are
Fig. 1 Proposed research framework for selecting the best metric
1 h t t p s : / / a r c h i v e . i c s . u c i . e d u / d a t a s e t / 3 5 0 / d e f a u l t + o f + c r e d i t + c a r d + c l i e n t s

Sujon et al. Journal of Big Data (2025) 12:268 Page 7 of 45
Table 3 Feature summary and descriptions
Feature Name Type Note
ID, SEX, EDUCA- Categorical ID: Unique identifier for each client. SEX: Gender of the client (Male/
TION, MARRIAGE Female). EDUCATION: Education level (1: Graduate school, 2: University,
3: High school, 4: Others). MARRIAGE: Marital status (1: Married, 2: Single,
3: Others).
LIMIT_BAL, AGE Numeric LIMIT_BAL: Credit limit in the credit card account. AGE: Age of the client.
PAY_0 to PAY_6 Categorical PAY_0 to PAY_6: Payment status for the last 6 months, where 0 means
no delay and 1–9 indicates the number of months the payment was
delayed. (Months: September 2005 to February 2005).
BILL_AMT1 to Numeric BILL_AMT1 to BILL_AMT6: Bill statement amounts for the last 6 months
BILL_AMT6 (Months: September 2005 to February 2005).
PAY_AMT1 to Numeric PAY_AMT1 to PAY_AMT6: Amount paid for the last 6 months (Months:
PAY_AMT6 September 2005 to February 2005).
DEFAULT_PAY- Categorical DEFAULT_PAYMENT_NEXT_MONTH: Whether the client defaulted on
MENT the payment in the next month (1: Default, 0: No default).
_NEXT_MONTH
Fig. 2 Class distribution with the imbalanced dataset
a mix of categorical and numerical variables. We provide a summary of the features and
their respective types in Table 3. The distribution of the target variable of the dataset is
presented in Figure 2, which demonstrates the imbalanced nature of the dataset. The
dataset was initially examined for missing values, inconsistencies, and anomalies. Fea-
tures with missing values were imputed to ensure the integrity of our selected dataset.
For categorical features such as education and marital status, we converted them into
numerical features using the hot encoder method.
Additional dataset
To further enhance the generalizability of our findings, we extended our experiments
to another dataset. The second dataset employed in this study is the Telco Customer
Churn dataset, sourced from Kaggle and available at the URL2. This dataset comprises
7,043 instances and more than 20 features, collected from a telecom company’s cus-
tomer database, and is used to predict customer churn–the likelihood that a customer
will cancel their subscription to the service. The target variable in this dataset is Churn,
2 h t t p s : / / w w w . k a g g l e . c o m / d a t a s e t s / b l a s t c h a r / t e l c o - c u s t o m er - c h u r n

Sujon et al. Journal of Big Data (2025) 12:268 Page 8 of 45
a binary indicator where ‘Yes’ signifies a customer who has churned, and ‘No’ repre-
sents a customer who has remained with the company. The dataset contains a mix of
numerical and categorical features, including customer demographics (e.g., age, gen-
der), account details (e.g., tenure, monthly charges), service usage patterns (e.g., internet
service, online security), and payment methods (e.g., electronic billing). This dataset is
well-suited for exploring imbalanced classification problems, with approximately 26.5%
of customers having churned, which allows for a rigorous evaluation of different perfor-
mance metrics tailored to business data mining applications.
Feature scaling
Since the dataset contained various features with different units and ranges, all numeri-
cal features were standardized using z-score normalization. The study used standardiza-
tion because it helps to increase the performance of business predictive models while
dealing with large business datasets [38].
X µ
X′ = − (1)
σ
where X is the original feature value, µ is the mean, and σ is the standard deviation. This
ensures that models sensitive to feature magnitudes and perform effectively.
Dataset splitting
The data was split into training (80%) and testing (20%) subsets using stratified sampling
to maintain the class imbalance ratio in both sets. Stratified sampling ensures that the
minority class (clients who defaulted) is represented proportionally, which is crucial for
reliable model evaluation.
Model selection and validation of use
In this study, we aimed to evaluate the optimal performance metric for business data
mining on imbalanced datasets. To ensure the generalizability and robustness of our
findings on performance metric evaluation, we selected five machine learning models
representing diverse algorithmic paradigms: LR as a linear model, DT, RF, and XGB as
tree-based models, and KNN as an instance-based method. This variety enables a com-
prehensive assessment of metric behavior across fundamentally different learning strate-
gies commonly used in business data mining.
Logistic Regression (LR)
LR is a linear model widely used for binary classification tasks. It is interpretable and
computationally efficient, making it ideal for applications such as credit scoring and
fraud detection in business contexts [39]. Its probabilistic output makes it suitable for
threshold-based analyses. The decision boundary for LR is modeled as:
1
P(Y =1X)=
| 1+e
−
(β0+β1X1+...+βnXn) (2)
where β 0 is the intercept and β 1 ,...,β n are the coefficients for the features X 1 ,...,X n.
Regularization was applied to prevent overfitting, and hyperparameters were optimized
using grid searching technique.

Sujon et al. Journal of Big Data (2025) 12:268 Page 9 of 45
Random Forest (RF)
RF is an ensemble learning method that builds multiple DTs and averages their outputs
to improve robustness and reduce overfitting [40]. We included the RF model due to
its capability to manage high-dimensional datasets and capture complex interactions
between features. Additionally, it is robust to class imbalances and can rank features’
importance, aligning well with explainability needs in business domains. The prediction
for RF is given by:
yˆ=mode h (X),h (X),...,h (X)
{ 1 2 T } (3)
where h t (X) is the prediction of the t-th tree. The number of trees (T) and maximum
tree depth were fine-tuned to achieve optimal performance.
Decision Tree (DT)
DT is an interpretable model that splits the dataset into subsets based on feature thresh-
olds. Our study used this model, as it offers a simple yet interpretable structure for clas-
sification problems [41]. Their tree-like representation makes them easy to understand,
even for non-technical stakeholders. The splitting criterion is determined using metrics
such as Gini impurity:
C
G=1 p2
− i (4)
i=1
∑
where p i is the proportion of instances belonging to class i, and C is the total number of
classes. Pruning was applied to prevent overfitting.
XGBoost (XGB)
XGB is a gradient-boosting algorithm that optimizes a regularized objective function. It
is able to prevent overfitting, making it particularly effective for datasets like ours with
diverse feature distributions [42]. XGB’s scalability and superior predictive performance
make it highly applicable in business data mining. For binary classification, the objective
function is defined as:
n T
= ℓ(y ,yˆ)+ Ω(h )
L i i j (5)
i=1 j=1
∑ ∑
where ℓ is the loss function (log-loss for binary classification), and Ω(h j ) is the regular-
ization term. Hyperparameters such as learning rate and tree depth were tuned using
cross-validation.
k-Nearest Neighbors (KNN)
KNN is a distance-based algorithm that classifies instances based on the majority class
among k nearest neighbors. We included KNN to analyze how non-parametric models,
which rely on local decision boundaries, perform compared to parametric and ensemble
models [43]. Its sensitivity to feature scaling allowed us to evaluate the impact of prepro-
cessing steps on metric performance.
The classification is determined as:

Sujon et al. Journal of Big Data          (2025) 12:268  Page 10 of 45
k
| yˆ=argmax | I(y | =c) |     |     |
| --------- | --- | --- | --- | --- |
|           | c i |     |     | (6) |
i=1
∑
where I is an indicator function that equals 1 if y i =c and 0 otherwise. The value of k
and the distance metric (Euclidean distance) were optimized for best performance.
In this research, the study used multiple machine learning models and statistical tests
to assess their performance in selecting the best performance metrics. Table 4 pres-
ents the configuration of each model, including their specific hyperparameters and
key settings. In addition, we outline the statistical tests and performance metrics used
to evaluate the models we selected in this research. We provide a clear overview of the
experimental setup for reproducibility and understanding of the analysis process that we
incorporated in this investigation.
Performance metric evaluation
The evaluation of machine learning models in this study focused on five key perfor-
mance metrics encompassing the Accuracy, Precision, Recall, MCC, and F1-Score.
These metrics were chosen based on their relevance and robustness for imbalanced
datasets and their ability to capture different dimensions of model performance. This
section discusses the significance of each metric, their mathematical formulation, and
why they were specifically chosen over other potential metrics.
Table 4 Parameter settings for selected models and techniques
| Model/analysis       | Parameter                      |     | Setting                                        |     |
| -------------------- | ------------------------------ | --- | ---------------------------------------------- | --- |
|  Logistic regression | Max_iter                       |     | 1000                                           |     |
|                      | Solver                         |     | ’lbfgs’                                        |     |
|                      | Penalty                        |     | ’l2’                                           |     |
|                      | C                              |     | 1.0                                            |     |
|                      | Random_state                   |     | 42                                             |     |
| Random forest        | N_estimators                   |     | 100                                            |     |
|                      | Max_depth                      |     | 6                                              |     |
|                      | Random_state                   |     | 42                                             |     |
| Decision tree        | Max_depth                      |     | 5                                              |     |
|                      | Random_state                   |     | 42                                             |     |
| XG boost             | n_estimators                   |     | 100                                            |     |
|                      | Learning_rate                  |     | 0.1                                            |     |
|                      | Max_depth                      |     | 6                                              |     |
|                      | Subsample                      |     | 0.8                                            |     |
| K-Nearest neighbors  | n_neighbors                    |     | 5                                              |     |
|                      | Weights                        |     | ‘uniform’                                      |     |
| Cross-validation     | cv                             |     | 5                                              |     |
|                      | Scoring                        |     | [‘accuracy’,‘precision’,‘recall’,‘f1’,‘mcc’]   |     |
| SHAP analysis        | Explainer                      |     | shap.Explainer(model, X_train)                 |     |
|                      | Shap_values                    |     | explainer(X_test)                              |     |
|                      | Mean SHAP importance           |     | Absolute mean SHAP values per feature          |     |
| Statistical analysis | Bootstrap Confidence Intervals |     | 1000 bootstraps                                |     |
|                      | McNemar’s Test                 |     | Exact p-value                                  |     |
|                      | Cohen’s Kappa                  |     | Measure agreement between model                |     |
|                      | ANOVA                          |     | Testing significant differences across metrics |     |
|                      | Significance Level             |     | p-value < 0.05 for significance                |     |

Sujon et al. Journal of Big Data (2025) 12:268 Page 11 of 45
Accuracy
While it is widely recognized that accuracy is a poor standalone metric in imbalanced
classification settings–often yielding deceptively high values by favoring the majority
class [9, 44]–its inclusion in this study serves a critical analytical role. Rather than using
accuracy as a primary indicator of model performance, we treat it as a control metric
or baseline to highlight the limitations of naive evaluation in the presence of imbalance.
By systematically comparing accuracy to more robust alternatives (e.g., F1-score, MCC)
across varying imbalance ratios and classification thresholds, we expose the instability
and over-optimism of accuracy in high-stakes business domains such as churn and credit
default prediction. Furthermore, the divergence between accuracy and minority-sen-
sitive metrics under conditions of noise and threshold shifts is quantitatively analyzed
using bootstrap confidence intervals and ANOVA, reinforcing the need for multi-metric
evaluation. This comparative lens allows us not only to validate the inadequacy of accu-
racy empirically but also to showcase its misalignment with business-relevant decision-
making. Accuracy is mathematically expressed as:
TP +TN
Accuracy= (7)
TP +TN +FP +FN
where TP is true positives, TN is true negatives, FP is false positives, and FN is false
negatives.
Precision
Precision quantifies the proportion of positive predictions that are correct:
TP
Precision= (8)
TP +FP
Precision has been included in our investigation because it plays a crucial role in busi-
ness applications where false positives have high costs, such as fraud detection or cus-
tomer churn prediction. It ensures that the model does not excessively classify instances
as positive when they are not, which is highly relevant for business data mining [45].
Recall
Recall mainly refers to the percentage of actual positive cases that are correctly identified
by the specific model:
TP
Recall= (9)
TP +FN
Recall is vital when false negatives are costly, such as missing a default customer in credit
scoring. It ensures the model captures as many true positives as possible, which is essen-
tial for risk management in business data mining [46].
F1-score
The F1-Score is the harmonic mean of Precision and Recall, balancing the trade-off
between the two:
Precision Recall
F1-Score=2 · (10)
· Precision+Recall

Sujon et al. Journal of Big Data (2025) 12:268 Page 12 of 45
The F1-Score offers a single metric that balances precision and recall and provides equal
importance to both, making it particularly useful for imbalanced datasets. It prevents
over-optimization of one metric at the expense of the other [47].
Matthews Correlation Coefficient (MCC)
MCC is a robust metric that considers all four confusion matrix elements (TP, TN, FP,
FN) to provide a balanced evaluation:
(TP TN) (FP FN)
MCC= · − ·
(11)
(TP +FP)(TP +FN)(TN +FP)(TN +FN)
√
MCC is ideal for imbalanced datasets as it accounts for true and false classifications
of both classes. Unlike Accuracy, it remains reliable even when class distributions are
highly skewed [48].
Evaluation of additional metrics
In addition to our selected five primary evaluation metrics, including Accuracy, Preci-
sion, Recall, F1-score, and MCC, we included four alternative metrics commonly used
in imbalanced classification problems, such as Geometric Mean (G-Mean), Area Under
the ROC Curve (AUC), Balanced Accuracy, and the Index of Balanced Accuracy (IBA).
These metrics were computed using the same prediction outputs from the trained mod-
els at a fixed decision threshold of 0.5. Their inclusion aims to offer a broader perspective
on model performance and to respond to established critiques in the literature regarding
the limitations of conventional metrics in imbalanced scenarios. However, these alterna-
tive metrics were not included in subsequent robustness, statistical testing, or explain-
ability analysis. This decision was based on their performance consistency with our
selected five metrics during baseline comparison, as well as their lower interpretability
in business decision-making contexts. As such, the remainder of the evaluation focuses
on the five core metrics.
Cost-sensitive evaluation
To assess how well our selected conventional evaluation metrics align with real-world
financial decision-making, we implemented a cost-sensitive evaluation framework based
on confusion matrix outputs. This approach simulates domain-specific misclassification
penalties by applying a cost matrix where false positives incur a cost of 10 units, and
false negatives incur a cost of 100 units–reflecting business-critical contexts such as loan
default or customer churn. For each model, we computed the Expected Cost of Misclas-
sification (ECM) using the formula:
ECM=(FP C )+(FN C )
× FP × FN (12)
where C FP =10 and C FN =100. We also derived a Net Profit score by taking the
inverse of the ECM. These results were used to evaluate the practical alignment of
F1-score and MCC with cost-based priorities.
Our design of this cost-sensitive evaluation is motivated by prior work in financial
domains, where researchers have highlighted the limitations of accuracy-driven met-
rics and proposed profit-oriented alternatives. For example, rank-based portfolio selec-
tion approaches have been shown to outperform market indices by explicitly linking

Sujon et al. Journal of Big Data (2025) 12:268 Page 13 of 45
evaluation to investment returns [49]. Similarly, cost-sensitive prediction frameworks
have been applied to stock price forecasting, where tailored misclassification costs and
feature selection improved investment outcomes [50]. Inspired by these studies, we inte-
grate cost-adjusted metrics into our evaluation pipeline to better reflect financial and
business realities.
Stratified 5-fold cross-validation
In this section, we implemented 5-fold stratified Cross-Validation as presented in Algo-
rithm 1 to evaluate multiple models on our selected large business dataset, consist-
ing of 30,000 instances. This approach balances computational efficiency with reliable
performance estimation by splitting the data into 5 folds, using each fold as a test set
while training on the remaining data. The process is repeated across all folds, and for
each model, we calculate the mean and standard deviation of the performance metrics–
accuracy, precision, recall, F1-score, and MCC. This allows us to assess both the cen-
tral tendency and variability of model performance. The 5-fold cross-validation ensures
that each model is evaluated across different data subsets, providing robust estimates of
performance and helping to select the most appropriate metric for model comparison.
This approach is particularly effective for large datasets like ours, as it mitigates the risk
of overfitting while offering a comprehensive assessment of each model’s reliability in
a business data mining scenario [51]. Our proposed Stratified 5-Fold Cross-Validation
process has been presented in Figure 3 meticulously.
Algorithm 1 5-Fold Stratified Cross-Validation for Model Evaluation
Statistical validation
In this study we implemented four statistical tests, including ANOVA, bootstrap confi-
dence intervals, McNemar’s test, and Cohen’s kappa. The combination of these statisti-
cal techniques ensures that the selection of the optimal metric is not based solely on

Sujon et al. Journal of Big Data          (2025) 12:268  Page 14 of 45

Fig. 3 Proposed stratified 5-fold cross-validation
numerical differences but is statistically validated. By identifying significant differences
and quantifying the reliability of the metric, this study ensures that the selected metric,
whether F1-score, MCC, or another, provides the most robust and generalizable assess-
ment of the model performance for business data mining tasks. These methods directly
address the gaps in current research, where statistical validation is often overlooked in
metric selection.
Analysis of variance (ANOVA)
To  directly  evaluate  the  relative  reliability  of  performance  metrics  across  models
and thresholds, we applied a repeated-measures analysis of variance (ANOVA). This
approach tests for significant differences between metrics while accounting for the
repeated structure of the data (i.e., metric scores across multiple models and thresholds).
For each of our selected metrics, including Accuracy, Precision, Recall, F1-score, and
MCC, we collected scores across five classifiers and nine thresholds (0.1 τ 0.9). We
≤ ≤
then performed a within-subjects repeated-measures ANOVA with Metric as the within
factor. Formally, the ANOVA model can be expressed as:
| Y =µ+α | +s +ϵ   |      |
| ------ | ------- | ---- |
| ij     | i j ij  | (13) |
where Y
ij is the performance score of metric i for subject (model-threshold combina-
tion) j, µ is the grand mean, α i is the effect of metric i, s j is the random effect of subject
j, and ϵ ij is the residual error term. The null hypothesis tested was:
| H :µ =µ | = =µ     |      |
| ------- | -------- | ---- |
| 0 1     | 2 ··· k  | (14) |
where k =5 metrics, against the alternative that at least one metric mean differs. Where
significant main effects were observed (p<0.05), we conducted Holm-corrected pair-
wise post-hoc comparisons. For each pair of metrics a and b, the test statistic was com-
puted as:
| X¯  | X¯  |     |
| --- | --- | --- |
| a   | b   |     |
t= −
| SE(X¯ | X¯   | (15) |
| ----- | ---- | ---- |
| a     | b )  |      |
−
with adjusted p-values using the Holm-Bonferroni method to control the family-wise
error rate. To complement the inferential tests, we also computed descriptive statistics

Sujon et al. Journal of Big Data (2025) 12:268 Page 15 of 45
for each metric, including the mean, median, standard deviation (σ), interquartile range
(IQR), and coefficient of variation (CV):
σ
CV =
µ (16)
Boxplots were generated to visualize the distribution and stability of metric scores across
all models and thresholds.
McNemar’s test
We use McNemar’s test to compare prediction errors between two models [52]. This test
determines if there is a statistically significant difference in the classification errors of
two models on the same dataset, making it especially relevant for metrics like precision
and recall. It highlights differences in error distributions, which are critical for under-
standing trade-offs between precision and recall The test statistic is calculated as:
(b c)2
χ2 = − (17)
b+c
where:
• b is the count of instances misclassified by model A but correctly classified by model
B,
• c is the count of instances correctly classified by model A but misclassified by model
B.
This test highlights differences in the models’ classification capabilities, particularly
for imbalanced datasets, where error patterns are critical for evaluating performance
metrics.
Bootstrap confidence intervals
Bootstrap confidence intervals (CIs) were calculated to quantify the variability and reli-
ability of each performance metric. It provides insights into metric variability, ensuring
the reliability of selected metrics under different scenarios [53]. By resampling the data
with replacement N times (N =1000), we obtained a distribution of metric values and
computed the 95% confidence interval as:
CI =[P ,P ]
95% 2.5% 97.5% (18)
where, P 2.5% and P 97.5% are the 2.5th and 97.5th percentiles of the bootstrap distribu-
tion. Metrics with narrower confidence intervals were deemed more reliable, providing
robust guidance for metric selection in noisy and imbalanced settings.
Cohen’s kappa
We used Cohen’s Kappa (κ) to measure the agreement between two models’ predictions,
accounting for the agreement occurring by chance [54]. It is defined as:
P P
κ= o − e
(19)
1 P
e
−
where:

Sujon et al. Journal of Big Data (2025) 12:268 Page 16 of 45
• P o is the observed agreement between the two models,
• P e is the expected agreement due to chance.
Cohen’s Kappa provides a scale of agreement, where:
• κ>0.8: strong agreement,
• 0.6<κ 0.8: moderate agreement,
≤
• κ 0.6: weak agreement.
≤
This metric is particularly useful for validating classification consistency across mod-
els and evaluating metrics such as F1-Score and MCC, which are sensitive to class
imbalance.
Threshold sensitivity analysis
Static threshold sensitivity analysis
Static threshold analysis involves evaluating model performance metrics: accuracy, pre-
cision, recall, F1-score, and MCC across fixed decision thresholds, ranging from 0.1
to 0.9. The goal is to understand the trade-offs between metrics and their behavior as
thresholds change [55]. The performance metrics for a given threshold t are calculated
based on predictions yˆ, defined as:
1 if P(y =1 X) t,
yˆ= | ≥
0 if P(y =1 X)<t.
{ |
Dynamic threshold sensitivity analysis
Dynamic threshold analysis optimizes thresholds for each metric to maximize perfor-
mance. For each metric M, the optimal threshold t ∗ is determined as:
t∗ =argmaxM(t)
t (20)
where M(t) is the value of the metric at the threshold t.
This analysis identifies the best threshold for accuracy, precision, recall, F1-score, and
MCC individually, offering tailored insights into the performance of metric-specific
models. This analysis helps identify decision thresholds where specific metrics reach
their peak performance. In addition, it provides actionable recommendations for busi-
ness decision-making, where balancing false positives and false negatives is crucial.
Noise robustness testing
Noise robustness testing evaluates how performance metrics behave under varying noise
levels in feature inputs. Gaussian noise with standard deviation σ is added to the input
features X to simulate real-world data inconsistencies [56]. The noisy feature X noisy is
defined as:
X =X+N(0,σ2)
noisy (21)
We trained our selected models on the original dataset and tested on noisy data, the
range of the noise levels was from σ =0.0 (no noise) to σ =0.3. It evaluates metric sta-
bility under noisy conditions, reflecting real-world scenarios where data may contain

Sujon et al. Journal of Big Data (2025) 12:268 Page 17 of 45
errors. Finally,it identifies models resistant to noise, crucial for business data mining,
where data quality often varies based on the scenario.
Explainable AI (XAI) analysis
To improve interpretability for business end-users, we employed SHAP (SHapley Addi-
tive exPlanations), a widely used explainability technique based on cooperative game
theory. SHAP decomposes a model’s output f(x) into additive feature contributions:
n
f(x)=ϕ + ϕ
0 i (22)
i=1
∑
Here, ϕ 0 is the expected model output, and ϕ i represents the marginal contribution of
feature x i to the prediction. We applied SHAP to an LR model using the LinearExplainer,
with a representative background sample from the training set to ensure stability. We
selected the LR model due to its transparency and compatibility with additive feature
attribution methods, making it ideal for explainable business applications. Our analysis
follows a two-stage framework. In the first stage, we generated conventional SHAP out-
puts, including summary bar plots and beeswarm plots, which highlight both global and
local feature importance. These plots illustrate the average and instance-specific influ-
ence of each feature on the model’s predictions.
In the second stage, we introduce a novel 3D SHAP framework to link model inter-
pretability with metric-specific performance across varying classification thresholds.
Thresholds were varied from 0.1 to 0.9, and for each value, classification outcomes were
generated on the test set. Evaluation metrics were computed alongside SHAP values. To
quantify feature importance at each threshold, we computed the mean absolute SHAP
value per feature across all test samples, defined as:
n
1
S (t)= ϕ(t)
i n i,j (23)
(cid:31) j=1(cid:30) (cid:30)
(cid:30) (cid:30)
(cid:30) (cid:30)
where S i (t) is the metric-conditioned SHAP importance of feature x i at threshold t, ϕ( i, t j )
is the SHAP value for feature x i and sample j at threshold t, and n is the number of test
instances.
This enabled the construction of 3D visualizations in which the X-axis represents
the classification threshold, the Y-axis reflects SHAP importance, and the Z-axis cor-
responds to the value of a selected evaluation metric. These plots reveal how the influ-
ence of individual features shifts across different decision boundaries and performance
criteria, offering deeper insight into metric behavior under realistic business constraints.
Finally, the combined use of static and dynamic threshold analysis, statistical analysis,
noise robustness testing, and SHAP-based explainability creates a comprehensive frame-
work for selecting the optimal performance metric in business data mining. The general
experimental design has been described in Figure 4. To provide the detailed phases of
our analysis, Algorithm 2 presents the overall steps that have been followed in this rigor-
ous investigation. With the experimental setup in place, we now report the performance
metrics and statistical outcomes derived from our evaluation.

Sujon et al. Journal of Big Data (2025) 12:268 Page 18 of 45
Algorithm 2 Framework for Optimal Performance Metric Selection
Experimental results
In this section we present the experimental results of our investigation. To evaluate
the reliability of performance metrics in business data mining, we conducted extensive
experiments on two real-world benchmark datasets: the large-scale Default of Credit
Card Clients dataset and the smaller Telco Customer Churn dataset. These datasets dif-
fer in size and imbalance levels but are both representative of practical business pre-
diction scenarios. For the first dataset, we applied a comprehensive suite of evaluations,
including exploratory data analysis, cross-validation, static and dynamic threshold sen-
sitivity analysis, noise robustness testing, statistical significance testing, and two-stage
SHAP-based explainability.

Sujon et al. Journal of Big Data (2025) 12:268 Page 19 of 45
Fig. 4 Experimental design for selecting the best performance metrics
To ensure generalizability of our findings while considering the experimental length,
we focused on key evaluations for the second dataset. Specifically, we conducted cross-
validation, Gaussian noise robustness testing, and bootstrap confidence intervals and
applied advanced statistical tools such as McNemar’s test and Cohen’s kappa to math-
ematically assess pairwise model agreement and classification significance. Addition-
ally, we employed SHAP-based explainable AI techniques to analyze feature importance
across performance metrics and classification thresholds. This structured and statisti-
cally rigorous approach ensures that our results are robust, interpretable, and applicable
to diverse business data mining contexts.
Exploratory data analysis
To establish a robust foundation for analyzing the performance of our selected machine
learning models, our study conducted an initial exploration of the dataset, focusing on
the distributional properties of key features. To better understand the characteristics
of the dataset, Gaussian distribution plots were generated for 12 selected features as

Sujon et al. Journal of Big Data (2025) 12:268 Page 20 of 45
displayed in Figure 5a to Figure 5i. These plots provide critical insights into the statistical
properties of each feature, including their central tendency, spread, and skewness, which
are essential to validate the suitability of different machine learning models and perfor-
mance metrics. Gaussian distribution analysis is particularly relevant, as many machine
learning algorithms, such as LR, assume features are normally distributed, while oth-
ers, such as tree-based models, are less sensitive to such assumptions. This analysis also
helps identify features that may require scaling, transformation, or special handling [57],
especially in the context of imbalanced distributions or outliers, which can impact met-
rics such as F1-Score and MCC that emphasize the balance between true positives and
false negatives.
Key insights were derived from individual feature distributions. LIMIT_BAL in Fig-
ure 5a exhibited a strong right-skewed distribution, with most clients concentrated at
lower credit limits, potentially leading to imbalances during training. Binary features
such as SEX in Figure 5b displayed a bimodal distribution, confirming a balanced rep-
resentation of demographic groups, while categorical features such as EDUCATION in
Figure 5c and MARRIAGE in Figure 5d demonstrated multi-modal distributions reflect-
ing the diversity of education levels and marital statuses. Similarly, AGE in Figure 5e
showed a right-skewed distribution, with younger clients dominating the dataset and a
long tail for older clients. Payment history features such as PAY_0, PAY_2, and PAY_3 in
Fig. 5 Gaussian distribution of the Default of Credit Card Clients dataset for different features. The description of
the feature labels is given in [58] (a) LIMIT_BAL, (b) SEX, (c) EDUCATION, (d) MARRIAGE, (e) AGE, (f) PAY_0, (g) PAY_2,
(h) PAY_3, (i) BILL_ATM1, (j) BILL_ATM2, (k) BILL_ATM4, (l) BILL_ATM6

Sujon et al. Journal of Big Data (2025) 12:268 Page 21 of 45
Figure 5f to Figure 5h revealed a significant peak at zero, corresponding to no delays in
payments, while additional peaks indicated varying levels of delinquency, emphasizing
the predictive importance of repayment behaviors.
Billing amounts BILL_AMT1, BILL_AMT2, and BILL_AMT4 in Figure 5i to Fig-
ure 5k displayed consistent right-skewed distributions, with most values clustered near
zero and a long tail extending to higher billing amounts. This variability underscores
the importance of scaling these features to avoid biasing distance-based models such
as KNN. Similarly, PAY_AMT6 in Figure 5l exhibited an extreme right-skewed distri-
bution, highlighting the need to account for rare but significant large payment values
during model training. These findings emphasize the need for robust preprocessing
techniques, including standardization and transformations, to ensure fair contributions
from all features. Moreover, the analysis provides valuable insights into how feature dis-
tributions impact the suitability of performance metrics, with metrics such as MCC and
F1-Score being particularly effective in handling imbalanced and skewed data distribu-
tions. This detailed understanding of the dataset lays the groundwork for the rigorous
evaluation of machine learning models and performance metrics in subsequent sections.
Baseline performance evaluation
To establish a benchmark for performance metrics, we evaluated five machine learning
models: LR, RF, DT, XGB, and KNN. The evaluation mainly focused on our selected five
performance metrics. Table 5 provides a summary of the baseline performance met-
rics for each model, while Figure 6a to Figure 6e present bar plots to visually assess and
compare the performance of the models based on these performance indicators. We
observed that LR achieved the highest precision (0.657), indicating its effectiveness in
minimizing false positives, although it struggled with recall (0.197), reflecting limited
sensitivity to correctly identify defaults [59]. XGB demonstrated the most balanced per-
formance, achieving the highest F1-Score (0.380) and MCC (0.287), making it robust in
handling class imbalances [60]. DT, on the other hand, achieved the highest recall (0.404)
but at the cost of low precision (0.346), resulting in a lower overall F1-Score and MCC.
RF showed slightly better recall (0.238) compared to LR and KNN, but its performance
was less consistent across all metrics. KNN delivered moderate performance, with an
Accuracy of 0.772 and MCC of 0.212, reflecting its sensitivity to feature scaling and its
limitations in handling skewed distributions [61].
These results highlight the trade-offs that we encountered across models. For instance,
while LR excelled in precision, it missed many true positives due to its lower recall. In
contrast, DT and XGB captured more true positives, as evidenced by their higher recall,
but were more prone to false positives. Metrics such as F1-Score and MCC proved
invaluable in balancing these trade-offs, helping us identify XGB as the most bal-
anced baseline model. These findings underscore the critical importance of selecting
Table 5 Baseline model performance for each metric
Model Accuracy Precision Recall F1-Score MCC
LR 0.800 0.657 0.197 0.303 0.280
RF 0.787 0.541 0.238 0.330 0.253
DT 0.700 0.346 0.404 0.373 0.178
XGB 0.790 0.546 0.291 0.380 0.287
KNN 0.772 0.469 0.238 0.315 0.212

Sujon et al. Journal of Big Data (2025) 12:268 Page 22 of 45
Fig. 6 Baseline performance evaluation for all models across metrics: (a) accuracy, (b) precision, (c) recall, (d) F1,
and (e) MCC
appropriate metrics for evaluating models in business data mining, where specific goals,
such as reducing false positives or capturing all true positives, may guide both metric
and model selection.
Performance with cross validation
To evaluate the reliability and robustness of the models, we performed a 5-fold stratified
cross-validation analysis across five metrics: Accuracy, Precision, Recall, F1-Score, and
MCC. Table 6 summarizes the mean and standard deviation of each metric across the
folds, while Figure 7a to Figure 7e present error bar plots that illustrate the variability in
metric performance across folds. The error bar plots provided valuable insights into the
consistency of the models. LR exhibited minimal variability in accuracy, with a mean of

Sujon et al. Journal of Big Data (2025) 12:268 Page 23 of 45
0.801 and a standard deviation of 0.006, suggesting that it performs consistently across
different folds. Precision for LR also displayed tight error bars, highlighting its reliability
in minimizing false positives. RF and XGB exhibited slightly higher variability in their
F1-Scores and MCC values, although their average performance remained robust, with
RF achieving the highest MCC (0.313) and XGB obtaining the second-highest F1-Score
(0.391). DT showed the highest variability in recall, reflecting its sensitivity to class
imbalance and fold-specific characteristics, while KNN demonstrated the largest vari-
ability in F1-Score and MCC, indicating its reliance on consistent feature distributions
across folds.
These results emphasize the importance of analyzing metric variability alongside
mean performance. Models like LR and RF demonstrated not only high average perfor-
mance but also low variability, making them suitable for business data mining tasks that
demand reliability. In contrast, the higher variability observed for DT and KNN suggests
that these models may require additional tuning or preprocessing to achieve consistent
results in practice. The error bar analysis reinforces the importance of cross-validation
as a tool for assessing model robustness and consistency, ensuring their suitability for
real-world business applications.
Static threshold sensitivity analysis
To evaluate the impact of varying static classification thresholds on model performance,
we analyzed five key metrics–Accuracy, Precision, Recall, F1-Score, and MCC–across
a range of thresholds (0.1 to 0.9). The goal was to identify the trade-offs inherent in
threshold adjustments and their effects on model performance, particularly for business
data mining tasks where balancing Precision and Recall is critical. Table 7 summarizes
the performance metrics for LR, RF, DT, XGB, and KNN models across thresholds. Fig-
ure 8a to Figure 8e visualize the threshold-performance relationships in three-dimen-
sional plots, where the x-axis denotes the threshold, the y-axis denotes the metric score,
and the z-axis corresponds to the model.
The results demonstrate notable trade-offs between Precision and Recall as thresholds
change. For example, Precision improves significantly for most models as the threshold
increases, reflecting a reduction in false positives. In contrast, recall decreases sharply
at higher thresholds as a result of stricter classification criteria, leading to an increased
rate of false negatives [62]. This is evident in models such as LR and RF, which achieve
high precision but suffer in Recall at thresholds above 0.5. Metrics like Accuracy and
MCC exhibit more stability across intermediate thresholds, particularly for models like
XGB and LR, suggesting their robustness in scenarios requiring a balance between false
positives and false negatives. The three-dimensional plots further highlight the trends
across models. For instance, in Figure 8a, Accuracy increases rapidly at lower thresholds
and stabilizes around intermediate values for most models, with LR and XGB showing
Table 6 Results with 5-fold stratified cross-validation
Model Mean Std Mean Std Mean Std Mean Std Mean Std
Accuracy Accuracy Precision Precision Recall Recall F1 F1 MCC MCC
LR 0.801 0.006 0.688 0.064 0.188 0.021 0.294 0.028 0.284 0.031
RF 0.799 0.006 0.597 0.022 0.288 0.029 0.388 0.030 0.313 0.027
DT 0.716 0.015 0.370 0.028 0.399 0.035 0.384 0.028 0.200 0.036
XGB 0.785 0.009 0.525 0.032 0.312 0.030 0.391 0.028 0.285 0.030
KNN 0.779 0.008 0.498 0.033 0.267 0.036 0.347 0.038 0.245 0.038

Sujon et al. Journal of Big Data (2025) 12:268 Page 24 of 45
Fig. 7 Cross-validation mean and standard deviation for all models across metrics: (a) accuracy, (b) precision, (c)
recall, (d) F1, and (e) MCC
the most consistent performance. Figure 8b and Figure 8c reveal opposing trends for
Precision and Recall, while Figure 8d shows that F1-Score, which balances Precision
and Recall, reaches optimal levels at thresholds of 0.4 to 0.6. Similarly, Figure 8e indi-
cates that MCC, which accounts for both true and false predictions, peaks around these
intermediate thresholds. These results emphasize the need for careful threshold tuning,
particularly in business applications where trade-offs between Precision and Recall must
align with specific operational objectives. Through this analysis, we underline the impor-
tance of selecting thresholds that maximize overall performance while accounting for
the priorities of the business context.
Dynamic threshold sensitivity analysis
In this section we conducted Dynamic threshold sensitivity analysis to identify the opti-
mal thresholds for maximizing key performance metrics–Accuracy, Precision, Recall,

Sujon et al. Journal of Big Data (2025) 12:268 Page 25 of 45
Table 7 Static threshold sensitivity analysis across different metrics
Model & Metric Threshold
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
LR Accuracy 0.340 0.574 0.767 0.793 0.800 0.791 0.782 0.782 0.778
LR Precision 0.241 0.287 0.468 0.567 0.657 0.700 0.588 0.667 0.400
LR Recall 0.924 0.623 0.395 0.265 0.197 0.094 0.045 0.027 0.009
LR F1 0.382 0.393 0.428 0.361 0.303 0.166 0.083 0.052 0.018
LR MCC 0.113 0.153 0.285 0.283 0.280 0.202 0.116 0.102 0.031
RF Accuracy 0.412 0.610 0.745 0.782 0.787 0.784 0.785 0.782 0.780
RF Precision 0.254 0.310 0.429 0.509 0.539 0.547 0.625 0.636 1.000
RF Recall 0.857 0.623 0.475 0.377 0.251 0.130 0.067 0.031 0.005
RF F1 0.391 0.414 0.451 0.433 0.343 0.210 0.122 0.060 0.009
RF MCC 0.211 0.222 0.254 0.279 0.280 0.252 0.259 0.226 0.184
XGB Accuracy 0.624 0.708 0.754 0.779 0.790 0.789 0.795 0.792 0.788
XGB Precision 0.318 0.371 0.434 0.500 0.546 0.556 0.614 0.628 0.636
XGB Recall 0.614 0.462 0.386 0.332 0.292 0.224 0.193 0.144 0.094
XGB F1 0.419 0.411 0.409 0.399 0.380 0.320 0.294 0.234 0.164
XGB MCC 0.202 0.222 0.254 0.279 0.287 0.252 0.259 0.226 0.184
KNN Accuracy 0.500 0.500 0.700 0.700 0.772 0.772 0.790 0.790 0.778
KNN Precision 0.264 0.264 0.349 0.349 0.469 0.469 0.649 0.649 0.429
KNN Recall 0.709 0.709 0.413 0.413 0.238 0.238 0.108 0.108 0.014
KNN F1 0.385 0.385 0.378 0.378 0.316 0.316 0.185 0.185 0.026
KNN MCC 0.126 0.126 0.183 0.183 0.212 0.212 0.201 0.201 0.042
(LR: logistic regression, RF: random forest, XGB: XGBoost, KNN: k-nearest neighbors)
F1-Score, and MCC–for each model, as summarized in Table 5. This evaluation provides
a dual perspective by leveraging both tabular results and 3D visualizations in Figure 9a
to Figure 9e to comprehensively assess model performance under varying threshold set-
tings. The integration of these two approaches highlights the critical role of threshold
optimization in tailoring machine learning models to business data mining objectives.
From Table 8, it is evident that LR achieved its best Accuracy (0.80) at a threshold of
0.5, whereas RF peaked at a slightly lower value of 0.787 at the same threshold. Inter-
estingly, KNN exhibited the highest accuracy at 0.790 when the threshold was set to
0.7, suggesting its robustness under stricter classification criteria. Precision results also
revealed that RF achieved a perfect score (1.00) at a threshold of 0.9, outperforming all
other models. However, this high Precision came at the cost of Recall, where LR (0.924
at 0.1 threshold) and KNN (0.709 at 0.1 threshold) performed better, indicating their
suitability for tasks requiring exhaustive positive detection. F1-Score analysis reflected
a balanced view, with XGB and LR achieving comparable F1 values of 0.419 and 0.428,
respectively, at their respective thresholds. MCC, a key metric for imbalanced data,
showed XGB (0.287 at 0.5 threshold) and RF (0.307 at 0.4 threshold) leading in terms of
overall classification stability. The 3D visualizations from Figure 9a to Figure 9e comple-
ment the tabular results by illustrating the interplay between thresholds, models, and
metric performance. This analysis underscores the trade-offs associated with dynamic
threshold adjustment. While higher thresholds favor metrics like Precision, they may
compromise Recall, as seen in RF and KNN’s profiles. Conversely, lower thresholds opti-
mize Recall but diminish Precision, as evidenced by LR’s profile. Metrics like F1-Score
and MCC provide balanced perspectives, capturing these trade-offs effectively.

Sujon et al. Journal of Big Data (2025) 12:268 Page 26 of 45
Fig. 8 Static threshold sensitivity analysis across different metrics: (a) accuracy, (b) precision, (c) recall, (d) F1, and
(e) MCC
Before proceeding to robustness and interpretability analysis, we further examine
model performance through alternative evaluation metrics and domain-specific cost-
sensitive analysis, focusing on the Default of Credit Card Clients dataset.
Alternative metric evaluation
To broaden the depth of our analysis, we evaluated four additional performance metrics
that are commonly used in imbalanced classification, such as G-Mean, AUC, Balanced
Accuracy, and the IBA with α=0.1 These metrics were calculated for all five classifiers
using a fixed decision threshold of 0.5. Table 9 summarizes the results. Among these
metrics, DT achieved the highest G-Mean (0.563) and IBA (0.541), indicating relatively
balanced performance on both classes. RF performed best on AUC (0.681) and Balanced
Accuracy (0.595), while XGB achieved consistent but slightly lower values across all

Sujon et al. Journal of Big Data          (2025) 12:268  Page 27 of 45

Fig. 9 Dynamic threshold sensitivity analysis comparison across metrics: (a) accuracy, (b) precision, (c) recall, (d)
F1, and (e) MCC
Table 8 Dynamic threshold sensitivity analysis across different metrics
| Model BA  | BP BR       | Best F1 Best MCC | BTA BTP | BTR BTF | BTM |
| --------- | ----------- | ---------------- | ------- | ------- | --- |
| LR 0.800  | 0.700 0.924 | 0.428 0.285      | 0.5 0.6 | 0.1 0.3 | 0.3 |
| RF 0.787  | 1.000 0.857 | 0.451 0.307      | 0.5 0.9 | 0.1 0.3 | 0.4 |
| DT 0.700  | 0.346 0.404 | 0.373 0.178      | 0.1 0.1 | 0.1 0.1 | 0.1 |
| XGB 0.795 | 0.636 0.614 | 0.419 0.287      | 0.7 0.9 | 0.1 0.1 | 0.5 |
| KNN 0.790 | 0.649 0.709 | 0.385 0.212      | 0.7 0.7 | 0.1 0.1 | 0.5 |
Note: LR = Logistic Regression, RF = Random Forest, XGB = XGBoost, KNN = k-Nearest Neighbors, DT = Decision Tree
BA = Best Accuracy, BP = Best Precision, BR = Best Recall
BTA = Best Threshold (Accuracy), BTP = Best Threshold (Precision), BTR = Best Threshold (Recall), BTF = Best Threshold (F1),
BTM = Best Threshold (MCC)

Sujon et al. Journal of Big Data (2025) 12:268 Page 28 of 45
metrics. KNN and LR exhibited lower G-Mean and AUC values, reflecting their limited
recall performance, as noted earlier. For clarity and interpretability, F1-score and MCC
values are also included in Table 9 to facilitate direct comparison. Notably, while some
alternative metrics appear competitive, F1-score and MCC remain consistently strong
across models, aligning well with overall model behavior. For instance, XGB had the
highest F1-score (0.380) and MCC (0.287), along with solid alternative metric values,
supporting its well-rounded performance. Given their widespread adoption, statistical
interpretability, and alignment with both threshold and cost-based analyses, our selected
five metrics were retained as the primary focus for all subsequent robustness, explain-
ability, and statistical validation experiments.
Cost-sensitive evaluation
To assess the alignment between traditional evaluation metrics and real-world financial
costs, we performed a cost-sensitive evaluation based on confusion matrix outputs. Each
model’s false positives and false negatives were penalized using a domain-relevant cost
matrix where false positives incurred a cost of 10 units, and false negatives incurred a
cost of 100 units. The resulting Expected Cost of Misclassification (ECM) and Net Profit
(as the negative of ECM) are reported in Table 10. The results reveal clear differences
in cost-effectiveness across models. DT achieved the lowest ECM (15,000) and thus the
highest Net Profit (–15,000), primarily due to its higher recall (0.404) and lower false
negative count (133). This highlights its suitability for scenarios where missing positive
cases (e.g., loan defaults or customer churn) incurs high financial risk. By contrast, LR,
which had the highest MCC (0.280) and good precision (0.657), resulted in the highest
ECM (18,130) due to a very low recall (0.197) and high number of false negatives (179).
This demonstrates that even models with high MCC may not be optimal in cost-sensi-
tive domains if they underperform in recall.
These findings reinforce the decision to prioritize accuracy, precision, recall, F1 and
MCC as our core evaluation metrics. While cost-sensitive metrics provide an essential
domain-aware perspective, F1-score–by balancing precision and recall–often aligned
more closely with cost efficiency, and MCC provided complementary information on
class imbalance. Therefore, both metrics remain valid and robust tools for evaluating
predictive models in business-critical applications.
Noise robustness testing
The robustness of the models to increasing noise levels (0.0 to 0.3) was evaluated using
metrics including Accuracy, Precision, Recall, F1-Score, and MCC. Table 11 details the
results, while Figure 10a to Figure 10e illustrate the trends. LR and RF demonstrated sta-
ble performance, with LR achieving an accuracy of approximately 0.80, while RF showed
a slight improvement to 0.802 at 30% noise. Precision also increased for these models,
Table 9 Performance of standard (F1, MCC) and alternative evaluation metrics across models
Model F1 MCC G-Mean AUC BA IBA (α=0.1)
RF 0.330 0.253 0.486 0.681 0.595 0.452
XGB 0.380 0.287 0.472 0.665 0.581 0.440
LR 0.303 0.280 0.438 0.653 0.584 0.404
KNN 0.315 0.212 0.469 0.625 0.581 0.436
DT 0.373 0.178 0.563 0.594 0.594 0.541

Sujon et al. Journal of Big Data          (2025) 12:268  Page 29 of 45
Table 10 Cost-based evaluation of model performance using confusion matrix analysis
| Model TN | FP FN   | TP TPR   | TNR   | FPR FNR ECM       | Net Profit |
| -------- | ------- | -------- | ----- | ----------------- | ---------- |
| LR 764   | 23 179  | 44 0.197 | 0.971 | 0.029 0.803 18130 | −18130     |
| RF 739   | 48 167  | 56 0.251 | 0.939 | 0.061 0.749 17180 | −17180     |
| DT 617   | 170 133 | 90 0.404 | 0.784 | 0.216 0.596 15000 | −15000     |
| XGB 724  | 63 169  | 54 0.242 | 0.920 | 0.080 0.758 17530 | −17530     |
| KNN 727  | 60 170  | 53 0.238 | 0.924 | 0.076 0.762 17600 | −17600     |
True Positive Rate (TPR), True Negative Rate (TNR), False Positive Rate (FPR), False Negative Rate (FNR), and Expected Cost
of Misclassification (ECM) are reported
Table 11 Noise robustness testing across metrics
| Noise Level | Model | Accuracy | Precision | Recall F1-Score | MCC   |
| ----------- | ----- | -------- | --------- | --------------- | ----- |
| 0           | LR    | 0.800    | 0.657     | 0.197 0.303     | 0.280 |
| 0           | RF    | 0.787    | 0.541     | 0.238 0.330     | 0.253 |
| 0           | DT    | 0.700    | 0.346     | 0.404 0.373     | 0.178 |
| 0           | XGB   | 0.790    | 0.546     | 0.291 0.380     | 0.287 |
| 0           | KNN   | 0.772    | 0.469     | 0.238 0.315     | 0.212 |
| 0.1         | LR    | 0.797    | 0.641     | 0.184 0.286     | 0.263 |
| 0.1         | RF    | 0.794    | 0.576     | 0.256 0.354     | 0.282 |
| 0.1         | DT    | 0.756    | 0.433     | 0.332 0.376     | 0.231 |
| 0.1         | XGB   | 0.781    | 0.508     | 0.291 0.370     | 0.264 |
| 0.1         | KNN   | 0.766    | 0.445     | 0.238 0.310     | 0.198 |
| 0.2         | LR    | 0.800    | 0.672     | 0.184 0.289     | 0.276 |
| 0.2         | RF    | 0.797    | 0.582     | 0.287 0.384     | 0.304 |
| 0.2         | DT    | 0.728    | 0.363     | 0.309 0.334     | 0.165 |
| 0.2         | XGB   | 0.777    | 0.493     | 0.296 0.370     | 0.256 |
| 0.2         | KNN   | 0.777    | 0.490     | 0.229 0.312     | 0.220 |
| 0.3         | LR    | 0.797    | 0.680     | 0.152 0.249     | 0.253 |
| 0.3         | RF    | 0.803    | 0.622     | 0.274 0.380     | 0.317 |
| 0.3         | DT    | 0.764    | 0.447     | 0.283 0.346     | 0.219 |
| 0.3         | XGB   | 0.790    | 0.566     | 0.211 0.307     | 0.249 |
| 0.3         | KNN   | 0.771    | 0.457     | 0.193 0.271     | 0.183 |
with LR and RF reaching 0.680 and 0.622, respectively, highlighting their resilience.
Recall trends revealed that the DT had the highest initial recall (0.403) but was sensi-
tive to noise, rebounding slightly at higher noise levels. RF balanced precision and recall
effectively, achieving the best F1-Score (0.380) and MCC (0.317) under noisy conditions.
LR showed steady MCC values (0.28), while XGB and KNN exhibited declines across
metrics, indicating reduced noise tolerance. Overall, RF and LR emerged as the most
robust models, demonstrating stability and suitability for noisy environments, making
them strong candidates for business applications involving data uncertainty.
Statistical and mathematical validation
To ensure the robustness and reliability of the performance metrics across models, we
performed repeated-measures ANOVA, Bootstrap analysis to estimate confidence inter-
vals (CIs) and conducted McNemar’s test alongside Cohen’s Kappa to statistically evalu-
ate model prediction agreement. This comprehensive approach provides both metric
stability assessments and inter-model prediction validation.

Sujon et al. Journal of Big Data (2025) 12:268 Page 30 of 45
Fig. 10 Noise robustness testing comparison across metrics for all models: (a) accuracy, (b) precision, (c) recall,
(d) F1, and (e) MCC
ANOVA
To investigate the stability and reliability of our selected evaluation metrics across
models and thresholds, we conducted a repeated-measures ANOVA. The analysis
revealed a highly significant main effect of metric on performance scores (F(4,176) =
77.62, p<0.001). Descriptive statistics and Holm-corrected post-hoc comparisons
are reported in Table 12, and the distribution of scores is visualized in Figure 11. Accu-
racy achieved the highest overall mean score (0.716) and the lowest variability (CV =
0.146), performing significantly better than all other metrics (p<0.001). However, its
dominance reflects its bias toward majority classes rather than balanced evaluation
under imbalance. F1-score (mean = 0.296, CV = 0.434) and MCC (mean = 0.183, CV =
0.334) demonstrated more balanced performance across models and thresholds. F1 and
Recall did not differ significantly from one another (p = 0.236), indicating they capture
similar dynamics under imbalance. MCC was significantly lower than F1 and Precision
but outperformed Recall, confirming its complementary role alongside F1 in reflecting
trade-offs between false positives and false negatives. Precision (mean = 0.462, CV =
0.340) performed moderately well, significantly better than Recall and F1 but inferior

Sujon et al. Journal of Big Data (2025) 12:268 Page 31 of 45
Table 12 Descriptive statistics and significance tests for evaluation metrics across models and
thresholds
Metric Mean Std Median IQR CV Significant Differences
Accuracy 0.716 0.104 0.767 0.082 0.146 >MCC, Precision, F1, Recall
MCC 0.183 0.061 0.183 0.060 0.334 < Accuracy, F1, Precision; >Recall
Precision 0.462 0.157 0.429 0.221 0.340 < Accuracy; >F1, Recall
F1-score 0.296 0.128 0.373 0.172 0.433 < Accuracy, Precision; >MCC; Recall (ns)
∼
Recall 0.323 0.228 0.359 0.274 0.708 < Accuracy, Precision; F1 (ns)
∼
Standard deviation (Std), interquartile range (IQR), and coefficient of variation (CV) are reported. Significant differences are
based on Holm-corrected pairwise comparisons at α=0.05
Fig. 11 Distribution of evaluation metric scores (Accuracy, Precision, Recall, F1-score, and MCC) across five classi-
fiers and nine decision thresholds (0.1–0.9)
to Accuracy. Recall (mean = 0.323, CV = 0.708) was the most unstable metric, with high
variability across thresholds and models, making it less reliable as a standalone indica-
tor. Together, these results confirm that although Accuracy yields higher absolute values,
F1-score and MCC offer more reliable and interpretable measures under class imbal-
ance, justifying their emphasis in subsequent robustness and explainability analyses in
business data mining. Full post-hoc statistics are provided in Table 13.
Bootstrap confidence intervals
Bootstrap CIs for Accuracy, Precision, Recall, F1-Score, and MCC were computed across
models. Table 14 presents the Bootstrap confidence interval results across metrics, and
Figure 12a to Figure 12e support the visualization of the findings. LR consistently dem-
onstrated narrow intervals across metrics, reflecting its stability. For Accuracy, the CI
was (0.7752, 0.8248), higher than DT (0.6723, 0.7287), indicating superior reliability.
XGB exhibited tight CIs in most metrics, particularly for MCC (0.2082, 0.3578), sug-
gesting balanced performance. In contrast, DT exhibited wider intervals, especially for
Recall, highlighting potential instability under varying data conditions.
McNemar’s test and cohen’s kappa
McNemar’s test evaluated significant prediction differences across paired models.
Table 15 and Figure 13 Presents the combined results of McNemar’s Test and Cohen’s
Kappa teast. LR and RF showed statistically significant differences in predictions
(p-value = 2.4439e-04), indicating non-identical model behaviors. Similarly, DT vs. XGB

Sujon et al. Journal of Big Data          (2025) 12:268  Page 32 of 45
Table 13 Pairwise post-hoc comparisons between metrics using repeated-measures ANOVA.
Reported values include the t-statistic, raw p-value, and Holm-corrected p-value for family-wise error
rate control at α=0.05
Metric A Metric B t-stat p-value Holm-corrected p Significant (α=0.05)
| Accuracy  | MCC       | 34.220 <0.0001  | <0.0001 | Yes |     |
| --------- | --------- | --------------- | ------- | --- | --- |
| Accuracy  | Precision | 15.056 <0.0001  | <0.0001 | Yes |     |
| Accuracy  | F1-score  | 14.136 <0.0001  | <0.0001 | Yes |     |
| Accuracy  | Recall    | 8.128 <0.0001   | <0.0001 | Yes |     |
| MCC       | Precision | −11.227 <0.0001 | <0.0001 | Yes |     |
| MCC       | F1-score  | 7.302 <0.0001   | <0.0001 | Yes |     |
| MCC       | Recall    | −4.060 0.0002   | 0.0006  | Yes |     |
| Precision | F1-score  | −4.213 0.0001   | 0.0005  | Yes |     |
| Precision | Recall    | 2.544 0.0145    | 0.0291  | Yes |     |
| F1-score  | Recall    | −1.203 0.2356   | 0.2356  | No  |     |
Table 14 Bootstrap confidence intervals for performance metrics across models
| Model | Accuracy CI | Precision CI | Recall CI | F1 CI | MCC CI |
| ----- | ----------- | ------------ | --------- | ----- | ------ |
LR (0.775, 0.825) (0.530, 0.768) (0.148, 0.252) (0.234, 0.371) (0.199, 0.355)
RF (0.762, 0.811) (0.444, 0.633) (0.185, 0.293) (0.263, 0.394) (0.177, 0.322)
DT (0.672, 0.729) (0.287, 0.403) (0.341, 0.465) (0.318, 0.424) (0.110, 0.239)
XGB (0.763, 0.813) (0.454, 0.633) (0.229, 0.348) (0.312, 0.441) (0.208, 0.358)
KNN (0.745, 0.798) (0.373, 0.570) (0.181, 0.298) (0.249, 0.383) (0.208, 0.358)
(LR: logistic regression, RF: random forest, DT: decision tree, XGB: XGBoost, KNN: k-nearest neighbors)
had a significant p-value of 3.5484e-22. Cohen’s Kappa values, which quantify agree-
ment, were highest for LR vs. RF (0.5460), suggesting moderate agreement, while RF vs.
DT scored lower (0.3172), reflecting greater disparity in predictions.
The bootstrap analysis identified LR and XGB as the most stable models across met-
rics, with consistently narrow CIs. McNemar’s test further validated significant predic-
tive differences between DT and XGB, while Cohen’s Kappa indicated strong agreement
between LR and RF. These findings underscore LR’s reliability for precision-critical tasks
and XGB’s balance across metrics. DT’s variability suggests its use may be better suited
for scenarios prioritizing Recall over precision or stability.
Explainable AI (XAI) analysis
To strengthen the interpretability of our framework, we implemented a two-stage SHAP
analysis. First, we applied conventional SHAP techniques (bar plots and beeswarm
visualizations) to LR as a baseline model, providing standard global and local feature
importance insights. This step ensures transparency and aligns with widely adopted
explainability practices. Building on this, we introduced a novel 3D metric-conditioned
SHAP analysis, where feature contributions were examined across varying thresholds
and linked directly to performance metrics (Accuracy, Precision, Recall, F1-score, and
MCC). This extension moves beyond static feature importance, offering a dynamic view
of how interpretability interacts with metric reliability under class imbalance.
Conventional SHAP analysis
To enhance transparency and meet standard explainability requirements, we first applied
conventional SHAP analysis to LR, one of the most interpretable models in our study
and a natural baseline for business applications. SHAP values were computed using the

Sujon et al. Journal of Big Data          (2025) 12:268  Page 33 of 45

Fig. 12 Bootstrap confidence interval comparison for each metric: (a) accuracy, (b) precision, (c) recall, (d) F1, and
(e) MCC
Table 15 Combined results of McNemar’s test and Cohen’s kappa for model comparisons
| Model comparison | McNemar p-value | Cohen kappa |
| ---------------- | --------------- | ----------- |
| LR vs RF         | 0.00024439      | 0.546       |
| RD vs DT         | 3.0985E-32      | 0.317       |
| DT vs XGB        | 3.5484E-22      | 0.291       |
| XGB vs KNN       | 0.63977         | 0.444       |
LinearExplainer, with results visualized as global feature importance rankings in Fig-
ure 14a and beeswarm distributions of individual SHAP contributions in Figure 14b.
The results confirm that repayment history (PAY_0, PAY_3, PAY_5) and billing amounts
(BILL_AMT1–3, BILL_AMT5) are the most influential predictors of customer default,
consistent with financial domain expectations. In contrast, demographic variables such

Sujon et al. Journal of Big Data (2025) 12:268 Page 34 of 45
Fig. 13 McNemar’s test and Cohen’s kappa comparisons
as SEX and EDUCATION exerted negligible influence, highlighting the model’s reli-
ance on behavioral rather than demographic signals. Importantly, these SHAP explana-
tions provide context for the evaluation metrics examined in this study. For example, the
strong dominance of repayment-related variables explains why Recall remains unstable
under threshold changes (since minority-class detection depends heavily on a few repay-
ment indicators). Similarly, the broader balance of billing and repayment features sup-
ports the complementary nature of F1-score and MCC, which integrate precision and
sensitivity trade-offs.
By combining conventional SHAP outputs with metric-specific analyses, our frame-
work demonstrates how interpretability tools can bridge the gap between raw perfor-
mance metrics and domain-level decision requirements, ensuring that metric selection
is not only statistically rigorous but also practically explainable.
Metric-conditioned SHAP analysis (3D threshold interaction)
To move beyond static feature importance, we applied our novel 3D SHAP analysis
framework to investigate how individual features interact with evaluation metrics across
varying thresholds. The 3D visualizations in Figure 15a through Figure 15e show SHAP
importance (Y-axis) plotted against decision thresholds (X-axis) and metric scores
(Z-axis), enabling a dynamic interpretability view tailored to each performance metric.
In Figure 15a, which represents Accuracy, features like LIMIT_BAL and PAY_0 con-
sistently demonstrate high SHAP importance across threshold values. This stability sug-
gests these features reliably contribute to correct classifications regardless of decision
boundaries, making accuracy-sensitive models suitable for high-confidence applications
such as credit approval or transaction filtering. Precision in Figure 15b reveals a more
selective pattern. SHAP contributions from LIMIT_BAL and PAY_0 peak at mid-range
thresholds (0.4–0.6), aligning with the metric’s preference for minimizing false positives.
However, contributions from other features such as BILL_AMT1 and PAY_3 sharply
decline as thresholds increase, highlighting the trade-off precision makes at higher
thresholds, often at the cost of sensitivity. The Recall visualization in Figure 15c presents

Sujon et al. Journal of Big Data (2025) 12:268 Page 35 of 45
Fig. 14 SHAP-based model interpretability for Logistic Regression. (a) Global feature importance based on mean
absolute SHAP values. (b) Beeswarm plot showing the distribution of SHAP values across individual predictions
a contrasting behavior. Here, SHAP values for almost all features, particularly PAY_0,
AGE, and PAY_3, decrease rapidly as thresholds rise. This is consistent with recall’s sen-
sitivity to false negatives; as the model becomes more conservative, it misses more posi-
tive cases, and the features driving true positive capture lose influence. For business use
cases focused on early risk detection or churn prevention, such patterns underscore the
cost of threshold tuning on recall-driven models.
In Figure 15d, the F1-score–being the harmonic mean of precision and recall–exhib-
its a more balanced SHAP profile. Features like PAY_0, BILL_AMT2, and PAY_AMT1
maintain moderately high importance across thresholds, particularly in the 0.3–0.6
range where the F1-score tends to peak. This balanced feature attribution reinforces F1’s
utility in capturing both class sensitivity and specificity, making it a stable and adaptable
metric for business contexts with imbalanced classes.
The MCC plot in Figure 15e further validates these observations. LIMIT_BAL, PAY_0,
and PAY_AMT1 show consistently strong SHAP contributions across thresholds, indi-
cating that MCC–like F1–captures balanced class performance but with additional
sensitivity to all four confusion matrix categories. Notably, MCC also reveals subtler
contributions from secondary features like AGE and PAY_3, which are less prominent
under metrics like Precision or Accuracy.
Taken together, these visualizations illustrate how each metric aligns with differ-
ent feature behaviors under threshold shifts. Our 3D SHAP analysis not only enhances
model interpretability but also provides practical guidance: F1-score and MCC emerge
as the most stable and balanced metrics for business classification under class imbal-
ance, while Accuracy and Precision may be preferable when robustness or specificity are
prioritized. This analysis empowers practitioners to align metric choice with both per-
formance goals and feature behavior.

Sujon et al. Journal of Big Data (2025) 12:268 Page 36 of 45
Fig. 15 SHAP feature impact analysis across thresholds: (a) SHAP for accuracy, (b) SHAP for precision, (c) SHAP for
recall, (d) SHAP for F1, and (e) SHAP for MCC
Additional experiment on telco customer churn dataset
To further validate the robustness and generalizability of our results, we extended
our analysis to the Telco Customer Churn dataset (7,043 instances and 20+ features),
sourced from Kaggle. This dataset addresses a binary classification problem predicting
customer churn, where the target variable denotes whether a customer has left (’Yes’) or
remained (’No’). The dataset is imbalanced, with approximately 26.5% of customers hav-
ing churned, making it suitable for examining the performance of models on imbalanced
data.

Sujon et al. Journal of Big Data (2025) 12:268 Page 37 of 45
Cross-validation results
The cross-validation results in Table 16 highlight that LR achieved the highest Accuracy
(0.803) but had a relatively low Recall (0.548), indicating its inability to effectively pre-
dict churned customers. RF performed slightly lower with Accuracy (0.793) but showed
similarly low Recall (0.493), which is not ideal for imbalanced classification problems.
In contrast, XGB achieved the highest F1-score (0.562) by maintaining a good balance
between Precision (0.611) and Recall (0.521). This suggests that the F1-score, which bal-
ances both Precision and Recall, is a highly effective metric in business data mining for
imbalanced datasets. KNN and DT performed poorly in comparison, especially in Preci-
sion and MCC, underlining their limited suitability for this task.
Noise robustness testing
The noise robustness testing results Table 17 indicate that XGB remained stable even
with increasing noise levels (0.0 to 0.3), maintaining solid F1-scores and MCC values.
This resilience to noise makes XGB a robust model for real-world business applications,
where noisy data is common. LR and RF showed relatively stable MCC values under
noise conditions, further supporting their reliability. However, KNN and DT showed
more sensitivity to noise, with a more significant decline in performance.
Bootstrap confidence intervals
The bootstrap confidence intervals for each model Table 18 further validate XGB’s reli-
ability. The F1-score and MCC for XGB showed the most stable confidence intervals,
with F1-score CI ranging from 0.2141 to 0.2968 and MCC CI from 0.2279 to 0.3550.
In comparison, LR and RF showed wider intervals, particularly for Recall and MCC,
indicating more variability in performance. The narrow confidence intervals for XGB
reinforce the conclusion that F1-score and MCC are the best metrics for evaluating
imbalanced datasets in business data mining.
McNemar’s test & cohen’s kappa
Statistical significance between model pairs was assessed using McNemar’s test and
Cohen’s Kappa Table 19. XGB showed significant performance differences compared
to other models, particularly in its Precision and Recall, as evidenced by the McNemar
p-value of 0.0245 in the comparison with KNN. Cohen’s Kappa confirmed that XGB had
higher agreement with other models, particularly in predicting churn, further highlight-
ing its superiority in this task.
Metric-conditioned SHAP analysis with telco customer churn dataset
To understand the influence of feature importance on model decisions across differ-
ent performance metrics, we conducted SHAP-based explainable AI analysis using 3D
Table 16 Cross-validation results for the Telco Customer Churn dataset, including accuracy,
precision, recall, F1-score, and MCC
Model Accuracy Precision Recall F1 MCC
LR 0.803 0.654 0.548 0.596 0.470
RF 0.793 0.645 0.493 0.558 0.430
DT 0.734 0.498 0.520 0.510 0.330
XGB 0.785 0.611 0.521 0.562 0.420
KNN 0.761 0.553 0.522 0.537 0.380

Sujon et al. Journal of Big Data          (2025) 12:268  Page 38 of 45
Table 17 Noise robustness testing across metrics for the Telco Customer Churn dataset
| Noise Level | Model | Accuracy | Precision | Recall F1-Score | MCC   |
| ----------- | ----- | -------- | --------- | --------------- | ----- |
| 0.0         | LR    | 0.804    | 0.648     | 0.575 0.609     | 0.480 |
| 0.0         | RF    | 0.788    | 0.620     | 0.527 0.569     | 0.433 |
| 0.0         | DT    | 0.719    | 0.472     | 0.468 0.470     | 0.279 |
| 0.0         | XGB   | 0.767    | 0.568     | 0.516 0.541     | 0.386 |
| 0.0         | KNN   | 0.756    | 0.540     | 0.540 0.540     | 0.374 |
| 0.1         | LR    | 0.805    | 0.653     | 0.570 0.609     | 0.482 |
| 0.1         | RF    | 0.792    | 0.636     | 0.505 0.563     | 0.434 |
| 0.1         | DT    | 0.757    | 0.544     | 0.524 0.534     | 0.370 |
| 0.1         | XGB   | 0.774    | 0.568     | 0.628 0.596     | 0.441 |
| 0.1         | KNN   | 0.753    | 0.535     | 0.527 0.531     | 0.363 |
| 0.2         | LR    | 0.802    | 0.650     | 0.556 0.599     | 0.472 |
| 0.2         | RF    | 0.798    | 0.651     | 0.519 0.577     | 0.452 |
| 0.2         | DT    | 0.731    | 0.496     | 0.588 0.538     | 0.353 |
| 0.2         | XGB   | 0.791    | 0.640     | 0.489 0.555     | 0.428 |
| 0.2         | KNN   | 0.748    | 0.525     | 0.556 0.540     | 0.368 |
| 0.3         | LR    | 0.798    | 0.641     | 0.548 0.591     | 0.460 |
| 0.3         | RF    | 0.792    | 0.646     | 0.479 0.550     | 0.426 |
| 0.3         | DT    | 0.767    | 0.564     | 0.546 0.554     | 0.397 |
| 0.3         | XGB   | 0.766    | 0.555     | 0.610 0.581     | 0.420 |
| 0.3         | KNN   | 0.758    | 0.544     | 0.559 0.552     | 0.386 |
Table 18 Bootstrap confidence intervals with the Telco Customer Churn dataset for performance
metrics across models
| Model Accuracy CI |     | Precision CI | Recall CI | F1 CI | MCC CI |
| ----------------- | --- | ------------ | --------- | ----- | ------ |
LR (0.601, 0.645) (0.220, 0.307) (0.199, 0.275) (0.209, 0.284) (−0.051, 0.050)
RF (0.607, 0.654) (0.221, 0.318) (0.187, 0.257) (0.199, 0.281) (0.199, 0.281)
DT (0.589, 0.632) (0.221, 0.277) (0.224, 0.303) (0.228, 0.304) (0.228, 0.304)
XGB (0.597, 0.645) (0.216, 0.312) (0.205, 0.272) (0.214, 0.297) (0.228, 0.355)
KNN (0.586, 0.633) (0.213, 0.309) (0.224, 0.305) (0.228, 0.355) (0.228, 0.355)
(LR: logistic regression, RF: random forest, DT: decision tree, XGB: XGBoost, KNN: k-nearest neighbors)
Table 19 Results of McNemar’s test and Cohen’s kappa for pairwise model comparisons on the
Telco Customer Churn dataset
| Model Comparison |     | McNemar p-value |     |     | Cohen’s Kappa |
| ---------------- | --- | --------------- | --- | --- | ------------- |
| LR vs RF         |     | 0.101           |     |     | 0.669         |
| RF vs DT         |     | 0.000           |     |     | 0.527         |
| DT vs XGB        |     | 0.058           |     |     | 0.528         |
| XGB vs KNN       |     | 0.025           |     |     | 0.595         |
visualizations. Figure 16a through Figure 16e illustrate the variation of SHAP values with
respect to classification thresholds and their respective impact on Accuracy, Precision,
Recall, F1-score, and MCC. Each figure represents a 3D plot where the x-axis denotes
the classification threshold, the y-axis corresponds to the SHAP value (indicating feature
importance), and the z-axis presents the value of the respective performance metric.
In Figure 16a, representing SHAP impact on Accuracy, the curves reveal that Accu-
racy peaks around threshold values of 0.5 to 0.6, but varies significantly with feature
influence. Notably, features such as InternetService_No, MonthlyCharges, and tenure
dominate the model’s predictive power. However, the sharp drops in accuracy beyond
certain thresholds suggest sensitivity to threshold tuning and class imbalance, indicat-
ing that Accuracy alone may be unreliable in imbalanced business scenarios. Figure 16b

Sujon et al. Journal of Big Data (2025) 12:268 Page 39 of 45
Fig. 16 SHAP feature impact analysis across thresholds with the Telco Customer Churn dataset: (a) SHAP for ac-
curacy, (b) SHAP for precision, (c) SHAP for recall, (d) SHAP for F1, and (e) SHAP for MCC
demonstrates SHAP impact on Precision. Precision shows a noticeable spike at higher
thresholds (around 0.7), but its distribution across features is more uneven. Certain fea-
tures, especially InternetService_No and ElectronicCheck, produce sharp increases in
SHAP values, indicating high but potentially unstable influence. This suggests that while
Precision may seem high at certain thresholds, it may favor false negatives and be mis-
leading without recall context. In Figure 16c, we observe the SHAP impact on Recall.
Here, most features demonstrate a steady decline in recall as the threshold increases,
confirming that lower thresholds tend to favor true positive recovery. While this stability
is beneficial, high recall alone without balancing false positives may not reflect overall
predictive reliability, particularly for business-critical applications like churn detection.
Figure 16d provides insights into F1-score, which balances Precision and Recall. The
SHAP curves here are more evenly distributed, and the metric reaches optimal values
at thresholds around 0.4 to 0.6. This balanced behavior across features and thresholds
suggests that F1-score is more robust and interpretable than single-dimension met-
rics, making it highly suitable for imbalanced business data mining problems. Finally,

Sujon et al. Journal of Big Data (2025) 12:268 Page 40 of 45
Figure 16e illustrates the SHAP analysis for MCC. Similar to F1-score, MCC also dis-
plays smooth curves across thresholds and SHAP values, with consistent contribu-
tions from core features such as tenure, MonthlyCharges, and Contract_Two year. The
metric’s stability across threshold changes further confirms its value as a balanced and
reliable indicator of classification performance under imbalanced conditions. Overall,
these SHAP-based visualizations reinforce our conclusion that both F1-score and MCC
provide the most stable and interpretable metrics for model evaluation in business data
mining. Unlike Accuracy and Precision, which can mislead in the presence of skewed
class distributions, F1 and MCC reflect more nuanced, threshold-robust insights into
model behavior and feature influence.
The additional experiments on the Telco Customer Churn dataset reinforce our ear-
lier findings and provide further evidence for effective model and metric selection in
imbalanced business classification. Among the evaluated models, XGB consistently
outperformed others across cross-validation, noise robustness, bootstrap confidence
intervals, and statistical testing, making it the most reliable choice for churn prediction.
F1-score and MCC again proved superior to traditional metrics like accuracy and preci-
sion, showing strong stability across thresholds and resilience to data noise. SHAP-based
explainability confirmed these results, with 3D SHAP visualizations revealing that F1
and MCC captured consistent, interpretable feature contributions–particularly from
tenure, MonthlyCharges, and contract type–regardless of threshold shifts. In contrast,
accuracy and precision were more sensitive to individual features and less stable across
decision boundaries. Overall, this extended evaluation confirms that XGB, combined
with F1-score and MCC, provides a robust and interpretable solution for business-criti-
cal tasks like churn prediction. These results highlight the importance of using advanced
metrics and explainability tools when developing decision-support systems in imbal-
anced, high-stakes domains.
Discussion
This study presents a comprehensive evaluation of performance metric reliability for
imbalanced classification in business data mining. By analyzing two real-world datas-
ets of differing sizes and domains–the large-scale Default of Credit Card Clients data-
set (30,000 instances) and the moderately sized Telco Customer Churn dataset (7,043
instances)–we systematically assessed five machine learning models (LR, RF, DT, XGB,
and KNN) across a variety of metrics, threshold strategies, noise conditions, and inter-
pretability techniques.
Our findings reinforce the importance of aligning metric selection with both the
intrinsic data characteristics and the operational goals of business decision-making.
Across both datasets, we observed that threshold selection plays a pivotal role in deter-
mining metric behavior. Static threshold analysis revealed that Accuracy and Precision
typically peaked at moderate thresholds (0.5–0.7), but consistently failed to account for
minority class detection, favoring specificity over sensitivity. Conversely, Recall peaked
at lower thresholds (e.g., 0.1) but rapidly degraded with threshold increases, highlight-
ing its trade-off bias and limited practical utility when used in isolation. These findings
were further validated through dynamic threshold sensitivity analysis, which allowed
us to identify the exact thresholds at which each metric achieved optimal performance.
Notably, both F1-score and MCC achieved their best balance between false positives and

Sujon et al. Journal of Big Data (2025) 12:268 Page 41 of 45
false negatives at thresholds between 0.3 and 0.5, a result consistently observed across
both datasets and model architectures [63].
Robustness testing under varying levels of synthetic noise offered further insights into
metric stability. As expected, LR and RF exhibited relatively stable Accuracy and Preci-
sion across noise conditions, particularly in the Telco dataset, where the signal-to-noise
ratio was narrower. DT performance, however, fluctuated considerably. Importantly,
Recall emerged as the most noise-sensitive metric, often producing unstable outputs in
both datasets. In contrast, F1-score and MCC maintained more consistent performance
across all noise levels, reaffirming their value for real-world applications where data
imperfections are common [64].
To establish statistical validity, we conducted ANOVA and McNemar’s tests across all
model-metric combinations [65]. Accuracy and Precision often failed to yield statisti-
cally significant differences between models, underscoring their limited discriminatory
power in imbalanced settings [66]. On the other hand, F1-score and MCC showed sig-
nificant inter-model variation across both datasets. For instance, the F1-score was sta-
tistically superior when comparing RF to LR on the credit default dataset, while MCC
significantly differentiated RF and XGB on the churn dataset [67]. These results demon-
strate that F1 and MCC are not only more stable but also more diagnostically useful for
comparative model evaluation in imbalanced classification.
Beyond performance scores, we incorporated a two-stage explainable AI (XAI) analy-
sis using SHAP to examine feature contributions across evaluation metrics and decision
thresholds. In the first stage, conventional SHAP plots (e.g., bar and beeswarm) applied
to the LR model identified key predictive drivers–such as PAY_0 and LIMIT_BAL in
the credit default dataset, and tenure and Contract type in the churn dataset–consis-
tent with domain expectations [68]. In the second stage, we introduced a novel 3D
SHAP framework to assess how feature importance evolved across thresholds and met-
rics. This dynamic analysis revealed that Accuracy and Precision were driven by high-
specificity features whose contributions declined at extreme thresholds, while F1-score
and MCC exhibited more stable and distributed feature influence. This dual-layer XAI
approach enhanced both global and threshold-specific interpretability, reinforcing the
practical advantage of metrics like F1 and MCC in real-world decision contexts where
model transparency is essential [69].
From a business perspective, the cost of false negatives–such as missed loan defaults
or undetected customer churn–is often significantly higher than that of false positives.
In such high-stakes contexts, the F1-score offers a reliable trade-off metric by balancing
precision and recall. MCC further strengthens evaluation by considering all elements of
the confusion matrix, making it especially useful in operational settings where misclas-
sification costs are asymmetrical but not always explicitly defined.
To broaden our analysis, we also evaluated four alternative metrics commonly used in
imbalanced classification: AUC, G-Mean, Balanced Accuracy, and the Index of Balanced
Accuracy (IBA, with α=0.1). Models such as DT and RF performed well under these
metrics, particularly in terms of G-Mean and AUC. However, these alternatives lacked
the statistical consistency and interpretive robustness observed with F1-score and MCC,
reinforcing our choice to prioritize the latter in our main analysis.
In addition, we implemented a cost-sensitive evaluation framework that applied busi-
ness-relevant penalties to misclassifications using Expected Cost of Misclassification

Sujon et al. Journal of Big Data (2025) 12:268 Page 42 of 45
(ECM) and Net Profit. This revealed that models with higher recall–such as the DT–
achieved lower overall cost, despite having lower MCC or precision scores. These
findings underscore the importance of aligning metric selection not only with data
characteristics but also with domain-specific cost structures. Together, they reaffirm
F1-score and MCC as both statistically sound and operationally meaningful metrics for
imbalanced business classification.
In conclusion, our study proposes a statistically grounded and interpretable frame-
work for selecting performance metrics in business data mining. By integrating dynamic
thresholding, noise robustness testing, inferential statistics, and SHAP-based explain-
ability, we provide a generalizable methodology for model evaluation on imbalanced
datasets. This approach equips practitioners and researchers with the tools needed
to make evidence-based decisions in predictive modeling, ensuring both robustness
and transparency in high-stakes applications. Future work can extend this framework
to unstructured data types or incorporate real-time cost-aware decision systems in
dynamic business environments.
Limitations
While our study offers a comprehensive and statistically rigorous framework for eval-
uating performance metrics in imbalanced business data mining, several limitations
should be acknowledged. First, although we examined two real-world business datas-
ets–one large-scale (credit card default) and one smaller-scale (customer churn)–both
originate from structured tabular domains. Future research should consider a broader
range of dataset sizes, structures, and industries to better assess the generalizability
of our findings. Second, our evaluation focused on five widely used machine learning
models, including both linear and tree-based methods. However, we did not incorporate
deep learning architectures, which may yield different patterns in both performance and
explainability–particularly in high-dimensional or unstructured data contexts. Third,
while our primary analysis concentrated on five core evaluation metrics–Accuracy, Pre-
cision, Recall, F1-score, and MCC–we also included supplementary results for alter-
native metrics such as AUC, G-Mean, Balanced Accuracy, and IBA. These additional
metrics were analyzed descriptively to broaden the scope of our findings but were not
subjected to the same level of statistical testing or interpretability analysis. Future stud-
ies could more deeply investigate the statistical robustness and explainability of these
alternative metrics. Fourth, although we introduced a cost-sensitive evaluation frame-
work and analyzed Expected Cost of Misclassification (ECM) and Net Profit, we did not
incorporate other domain-specific constraints such as real-time decision thresholds,
risk-based optimization, or adaptive cost matrices. These remain important areas for
operationalizing evaluation metrics in live business systems. Finally, this study focused
on classification-based business predictive modeling. Extending the framework to
other decision-support contexts such as forecasting, optimization, or recommendation
remains an open avenue for future work.
Conclusion
This comprehensive research presents a statistically grounded and interpretable frame-
work for selecting performance metrics in business data mining tasks involving imbal-
anced datasets. Using two real-world benchmarks–the Default of Credit Card Clients

Sujon et al. Journal of Big Data (2025) 12:268 Page 43 of 45
and the Telco Customer Churn datasets–we evaluated five machine learning models
through a multidimensional approach incorporating cross-validation, threshold sensitiv-
ity, noise robustness, inferential statistics, and SHAP-based explainability. Our results
show that Accuracy and Precision are inadequate in imbalanced contexts, as they favor
the majority class and underrepresent minority outcomes. Recall, though more sensitive
to the minority class, showed instability across thresholds and noise levels. In contrast,
F1-score demonstrated the most reliable and balanced performance across all scenarios,
while MCC offered complementary insights by incorporating all elements of the confu-
sion matrix. The addition of a two-layer SHAP framework linked feature importance to
metric behavior, highlighting how F1-score and MCC maintain interpretability and fea-
ture stability across thresholds. This supports their use in business-critical applications
where transparency and robustness are essential. Future research should extend this
framework to multi-class problems, cost-sensitive learning, and deep learning models
tailored for skewed data. Incorporating real-world business constraints such as mone-
tary costs, regulatory compliance, or real-time adaptation will further enhance practical
utility. In summary, this work provides a comprehensive, interpretable, and transferable
methodology for metric evaluation in imbalanced classification–empowering practitio-
ners to make evidence-based, risk-aware decisions in predictive modeling.
Author contributions
KMS perceived the idea, carried out formal analysis, developed the visualization and methodology, and wrote the draft.
RH investigated, validated, provided resources, and supervised the study. KC and MAS administrated the project, and
participated in reviewing the initial draft, modified it, and considerably improved it.
Funding
This work was supported in part by the Institute of Information and Communications Technology Planning and
Evaluation (IITP) funded by Korean Government through the Ministry of Science and ICT (MSIT) under Grant 2022-0-
00024, and in part by the National Research Foundation of Korea (NRF) funded by Korea Government (MSIT) under Grant
RS-2024-00452791.
Data availability
The datasets analyzed during this study are publicly available at h t t p s : / / a r c h i v e . i c s . u c i . e d u / d a t a s e t / 3 5 0 / d e f a u l t + o f + c r e
d i t + c a r d + c l i e n t s (accessed on 16 Dec. 2024), and at h t t p s : / / w w w . k a g g l e . c o m / d a t a s e t s / b l a s t c h a r / t e l c o - c u s t o m e r - c h u r n
(accessed on 11 Jun. 2025).
Declarations
Competing interests
The authors declare no competing interests.
Received: 11 June 2025 / Accepted: 8 October 2025
References
1. Bhatia S, Sharma P, Burman R, Hazari S, Hande R. Credit scoring using machine learning techniques. Int J Comput Appl.
2017;161(11):1–4.
2. Saito T, Rehmsmeier M. The precision-recall plot is more informative than the roc plot when evaluating binary classifiers
on imbalanced datasets. PLoS ONE. 2015. https://doi.org/10.1371/journal.pone.0118432.
3. Juba B, Le HS. Precision-recall versus accuracy and the role of large data sets. Proceedings of the AAAI Conference on
Artificial Intelligence. 2019;33:4039–48.
4. Boughorbel S, Jarray F, El-Anbari M. Optimal classifier for imbalanced data using matthews correlation coefficient metric.
PLoS ONE. 2017. https://doi.org/10.1371/journal.pone.0177678.
5. Xu X, Chen W, Sun Y. Over-sampling algorithm for imbalanced data classification. JSEE. 2019. h t t p s : / / d o i . o r g / 1 0 . 2 1 6 2 9 / j s e e .
2 0 1 9 . 0 6 . 1 2 .
6. Shaer L, Kanj R, Joshi R. Data imbalance handling approaches for accurate statistical modeling and yield analysis of
memory designs. 2019 IEEE International Symposium on Circuits and Systems (ISCAS), 1–5 2019 h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / I S
C A S . 2 0 1 9 . 8 7 0 2 7 3 1
7. Wu X, Huang F, Huang H. Fast stochastic recursive momentum methods for imbalanced data mining. 2022 IEEE Interna-
tional Conference on Data Mining (ICDM), 578–587 (2022) https://doi.org/10.1109/ICDM54844.2022.00068

Sujon et al. Journal of Big Data (2025) 12:268 Page 44 of 45
8. Sujon KM, Hassan R, Khairudin AR, Moi SH, Shafie MLM, Saringat Z, et al. The effects of imbalanced datasets on machine
learning algorithms in predicting student performance. JOIV: International Journal on Informatics Visualization.
2024;8(3–2):1599–605.
9. Japkowicz N. Assessment metrics for imbalanced learning. Imbalanced learning: Foundations, algorithms, and applica-
tions, 2013;187–206
10. Ferri C, Hernández-Orallo J, Modroiu R. An experimental comparison of performance measures for classification. Pattern
Recogn Lett. 2009;30(1):27–38.
11. Kubat M. Addressing the curse of imbalanced training sets: one-sided selection. In: Proceedings of the 14th International
Conference on Machine Learning, pp. 179–186 (1997). Morgan Kaufmann
12. Diallo R, Edalo C, Awe OO. Machine learning evaluation of imbalanced health data: A comparative analysis of balanced
accuracy, mcc, and f1 score. In: Awe, O.O., Vance, E.A. (eds.) Practical Statistical Learning and Data Science Methods: Case
Studies from LISA 2020 Global Network, USA. STEAM-H: Science, Technology, Engineering, Agriculture, Mathematics &
Health, pp. 283–312. Springer, Cham (2024). https://doi.org/10.1007/978-3-031-72215-8_12
13. Zareapoor M, Shamsolmoali P. Boosting prediction performance on imbalanced dataset. Int J Inf Commun Technol.
2018;13:186–95. https://doi.org/10.1504/IJICT.2018.10011701.
14. Imran M, Qyser A, Ali SS, Kumar V, Jah M, Malla N. An overview on data mining designed for imbalanced datasets. Interna-
tional Journal of Research in Engineering and Technology. 2014;03:222–5. https://doi.org/10.15623/IJRET.2014.0310034.
15. Chakraborty T. Imbalanced ensemble classifier for learning from imbalanced business school dataset. International Jour-
nal of Mathematical, Engineering and Management Sciences 2018; https://doi.org/10.33889/IJMEMS.2019.4.4-068
16. Lee Z, Lee C-Y, Chou S-T, Ma W-P, Ye F, Chen Z. A hybrid system for imbalanced data mining. Microsyst Technol.
2020;26:3043–7. https://doi.org/10.1007/S00542-019-04566-1.
17. Syaripudin A, Khodra ML. A comparison for handling imbalanced datasets. 2014 International Conference of Advanced
Informatics: Concept, Theory and Application (ICAICTA), 293–298 (2014) https://doi.org/10.1109/ICAICTA.2014.7005957
18. Vluymans S. Learning from imbalanced data. Dealing with Imbalanced and Weakly Labelled Data in Machine Learning
using Fuzzy and Rough Set Methods. 2018. https://doi.org/10.1007/978-3-030-04663-7_4.
19. Yan Y, Liu Y, Shyu M, Chen M. Utilizing concept correlations for effective imbalanced data classification. Proceedings of the
2014 IEEE 15th International Conference on Information Reuse and Integration (IEEE IRI 2014), 561–568 (2014) h t t p s : / / d o i .
o r g / 1 0 . 1 1 0 9 / I R I . 2 0 1 4 . 7 0 5 1 9 3 9
20. Veganzones D, Séverin E. An investigation of bankruptcy prediction in imbalanced datasets. Decis Support Syst.
2018;112:111–24. https://doi.org/10.1016/j.dss.2018.06.011.
21. Susan S, Kumar A. The balancing trick: optimized sampling of imbalanced datasets-a brief survey of the recent state of the
art. Eng Rep (Hoboken). 2020. https://doi.org/10.1002/eng2.12298.
22. Barella VH, Garcia LPF, Souto MD, Lorena AC, Carvalho A. Assessing the data complexity of imbalanced datasets. Inf Sci.
2021;553:83–109. https://doi.org/10.1016/j.ins.2020.12.006.
23. Wu F, Jing X, Shan S, Zuo W, Yang J-y. Multiset feature learning for highly imbalanced data classification. IEEE Trans Pattern
Anal Mach Intell. 2021;43:139–56.
24. Tao X, Li Q, Ren C, Guo W, Li C, He Q, et al. Real-value negative selection over-sampling for imbalanced data set learning.
Expert Syst Appl. 2019;129:118–34. https://doi.org/10.1016/J.ESWA.2019.04.011.
25. Mathews L, Hari S. Learning from imbalanced data. Advances in Computer and Electrical Engineering. 2019. h t t p s : / / d o i . o r
g / 1 0 . 4 0 1 8 / 9 7 8 - 1 - 5 2 2 5 - 2 2 5 5 - 3 . C H 1 5 9.
26. Zhao J, Jin J, Chen S, Zhang R, Yu B, Liu Q. A weighted hybrid ensemble method for classifying imbalanced data. Knowl-
Based Syst. 2020;203:106087. https://doi.org/10.1016/j.knosys.2020.106087.
27. Bekkar M, Djemaa H, Alitouche TA. Evaluation measures for models assessment over imbalanced data sets. Journal of
Information Engineering and Applications. 2013;3:27–38.
28. Basha SJ, Madala S, Vivek K, Kumar ES, Ammannamma T. A review on imbalanced data classification techniques. 2022
International Conference on Advanced Computing Technologies and Applications (ICACTA), 1–6 (2022) h t t p s : / / d o i . o r g / 1 0 .
1 1 0 9 / I C A C T A 5 4 4 8 8 . 2 0 2 2 . 9 7 5 3 3 9 2
29. Öztürk MM. Which type of metrics are useful to deal with class imbalance in software defect prediction? Inf Softw Technol.
2017;92:17–29.
30. Cruz Huayanay A, Bazán JL, Russo CM. Performance of evaluation metrics for classification in imbalanced data. Comput
Stat. 2025;40(3):1447–73.
31. Fawcett T. An introduction to roc analysis. Pattern Recognit Lett. 2006;27(8):861–74.
32. García V, Mollineda RA, Sánchez JS. A bias correction function for classification performance assessment in two-class
imbalanced problems. Knowledge-Based Systems. 2014;59:66–74.
33. Jiménez-Navarro M, Troncoso-García A, Troncoso A, Martínez-Álvarez F, Martínez-Ballesteros M. Explainable deep learning
with embedded feature selection for electricity demand forecasting. In: 2024 International Conference on Smart Systems
and Technologies (SST), pp. 153–158 (2024). IEEE
34. Troncoso-Garcia AR, Martinez-Ballesteros M, Martinez-Alvarez F, Troncoso A. A new metric based on association rules to
assess feature-attribution explainability techniques for time series forecasting. IEEE Trans Pattern Anal Mach Intell. 2025.
https://doi.org/10.1109/TPAMI.2025.3540513.
35. Troncoso-García A, Martínez-Ballesteros M, Martínez-Álvarez F, Troncoso A. Explainable machine learning for sleep apnea
prediction. Procedia Comput Sci. 2022;207:2930–9.
36. Kadir MA, Mosavi A, Sonntag D. Evaluation metrics for xai: A review, taxonomy, and practical applications. In: 2023 IEEE
27th International Conference on Intelligent Engineering Systems (INES), pp. 000111–000124 (2023). IEEE
37. Wong T-T, Chung P-C. A consistency analysis on four evaluation metrics for classifying imbalanced data. Knowledge and
Information Systems, 2025; 1–18
38. Mahmud Sujon K, Binti Hassan R, Tusnia Towshi Z, Othman MA, Abdus Samad M, Choi K. When to use standardization and
normalization: empirical evidence from machine learning models and xai. IEEE Access. 2024;12:135300–14. h t t p s : / / d o i . o r g
/ 1 0 . 1 1 0 9 / A C C E S S. 2 0 2 4 . 3 4 6 2 4 3 4 .
39. Bolton RJ, Hand DJ. Statistical fraud detection: a review. Stat Sci. 2002;17(3):235–55.
40. Khalilia M, Chakraborty S, Popescu M. Predicting disease risks from highly imbalanced data using random forest. BMC Med
Inform Decis Mak. 2011;11:1–13.

Sujon et al. Journal of Big Data (2025) 12:268 Page 45 of 45
41. Gilmore E, Estivill-Castro V, Hexel R. More interpretable decision trees. In: Hybrid Artificial Intelligent Systems: 16th Interna-
tional Conference, HAIS 2021, Bilbao, Spain, September 22–24, 2021, Proceedings 16, pp. 280–292 (2021). Springer
42. Chen T, Guestrin C. Xgboost: A scalable tree boosting system. In: Proceedings of the 22nd Acm Sigkdd International
Conference on Knowledge Discovery and Data Mining, 2016;pp. 785–794
43. Halder RK, Uddin MN, Uddin MA, Aryal S, Khraisat A. Enhancing k-nearest neighbor algorithm: a comprehensive review
and performance analysis of modifications. J Big Data. 2024;11(1):113.
44. Brownlee J. Failure of classification accuracy for imbalanced class distributions. Machine Learning Mastery. 2020;31.
45. Najem SM, Kadeem SM. A survey on fraud detection techniques in e-commerce. Tech-Knowledge. 2021;1(1):33–47.
46. Zeynali Tazehkandi M, Nowkarizi M. Three approaches to measuring recall on the web: a systematic review. Electron Libr.
2020;38(3):477–92.
47. Jeni LA, Cohn JF, De La Torre F. Facing imbalanced data–recommendations for the use of performance metrics. In: 2013
Humaine Association Conference on Affective Computing and Intelligent Interaction, pp. 245–251 (2013). IEEE
48. Chicco D, Jurman G. The advantages of the matthews correlation coefficient (MCC) over f1 score and accuracy in binary
classification evaluation. BMC Genomics. 2020;21:1–13.
49. Alsulmi M. From ranking search results to managing investment portfolios: exploring rank-based approaches for portfolio
stock selection. Electronics. 2022;11(23):4019.
50. Alsubaie Y, El Hindi K, Alsalman H. Cost-sensitive prediction of stock price direction: selection of technical indicators. IEEE
Access. 2019;7:146876–92.
51. Szeghalmy S, Fazekas A. A comparative study of the use of stratified cross-validation and distribution-balanced stratified
cross-validation in imbalanced learning. Sensors. 2023;23(4):2333.
52. Pembury Smith MQ, Ruxton GD. Effective use of the mcnemar test. Behav Ecol Sociobiol. 2020;74:1–9.
53. Aguirre-Urreta MI, Rönkkö M. Statistical inference with plsc using bootstrap confidence intervals. MIS Q.
2018;42(3):1001–10.
54. Więckowska B, Kubiak KB, Jóźwiak P, Moryson W, Stawińska-Witoszyńska B. Cohen’s kappa coefficient as a measure to
assess classification improvement following the addition of a new marker to a regression model. Int J Environ Res Public
Health. 2022;19(16):10213.
55. Chase Lipton Z, Elkan C, Narayanaswamy B. Thresholding classifiers to maximize f1 score. arXiv e-prints, 2014; 1402
56. Jiang J, Jiang X, Xu L, Zhang Y, Zheng Y, Kong D. Noise-robustness test for ultrasound breast nodule neural network mod-
els as medical devices. Front Oncol. 2023;13:1177225.
57. Knief U, Forstmeier W. Violating the normality assumption may be the lesser of two evils. Behav Res Methods.
2021;53(6):2576–90.
58. Yeh I-C, Lien C-h. Default of Credit Card Clients Dataset. UCI Machine Learning Repository 2009; h t t p s : / / d o i . o r g / 1 0 . 2 4 4 3 2 /
C 5 5 S 3 H .
59. Azis H. Assessing the performance of logistic regression in heart disease detection through 5-fold cross-validation. Inter-
national Journal of Artificial Intelligence in Medical Issues. 2024;2(1):1–11.
60. Maina DG, Moso JC, Gikunda PK. Detecting fraud in motor insurance claims using xgboost algorithm with smote. In: 2023
International Conference on Information and Communication Technology for Development for Africa (ICT4DA), 2023;pp.
61–66 . IEEE
61. Basak S, Huber M. Evolutionary feature scaling in k-nearest neighbors based on label dispersion minimization. In: 2020 IEEE
International Conference on Systems, Man, and Cybernetics (SMC), 2020; pp. 928–935. IEEE
62. Kusa W, Peikos G, Staudinger M, Lipani A, Hanbury A. Normalised precision at fixed recall for evaluating tar. In: Proceedings
of the 2024 ACM SIGIR International Conference on Theory of Information Retrieval, 2024; pp. 43–49
63. Foody GM. Challenges in the real world use of classification accuracy metrics: from recall and precision to the matthews
correlation coefficient. PLoS ONE. 2023;18(10):0291908.
64. Tang J, Li Y, Hou Z, Fu S, Tian Y. Robust two-stage instance-level cost-sensitive learning method for class imbalance prob-
lem. Knowledge-Based Systems. 2024;300:112143.
65. Chen X, Chen P. A comparison of four methods for the analysis of n-of-1 trials. PLoS ONE. 2014. h t t p s : / / d o i . o r g / 1 0 . 1 3 7 1 / j o u
r n a l . p o n e . 0 0 8 7 7 5 2 .
66. Owusu-Adjei M, Hayfron-Acquah JB, Frimpong T, Abdul-Salaam G. Imbalanced class distribution and performance evalua-
tion metrics: a systematic review of prediction accuracy for determining model performance in healthcare systems. PLoS
Digit Health. 2023. https://doi.org/10.1371/journal.pdig.0000290.
67. Wardhani NWS, Rochayani MY, Iriany A, Sulistyono A, Lestantyo P. Cross-validation metrics for evaluating classification
performance on imbalanced data. 2019 International Conference on Computer, Control, Informatics and its Applications
(IC3INA), 14–18 (2019) h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / I C 3 I N A 4 8 0 3 4 . 2 0 1 9 . 8 9 4 9 5 6 8
68. Explaining xgboost predictions with shap value. A comprehensive guide to interpreting decision tree-based models. New
Trends in Computer Sciences. 2023. https://doi.org/10.3846/ntcs.2023.17901.
69. Mokhtari KE, Higdon BP, Başar A. Interpreting financial time series with shap values. In: Proceedings of the 29th Annual
International Conference on Computer Science and Software Engineering, 2019;pp. 166–172
Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.