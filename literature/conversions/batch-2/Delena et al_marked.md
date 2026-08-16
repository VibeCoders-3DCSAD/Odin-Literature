---
conversion_metadata:
  converted_at: "2026-07-22T13:05:08Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Delena et al.pdf"
  source_pdf_sha256: "f1aac24a206237bbdec25d22102fdad258a7852820075bf0e8f03eaf37d6e727"
  page_count: 14
  markdown_char_count: 163295
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Systems and Soft Computing 7 (2025) 200352

Contents lists available at ScienceDirect

Systems and Soft Computing

journal homepage: www.journals.elsevier.com/soft-computing-letters

Predicting student retention: A comparative study of machine learning 
approach utilizing sociodemographic and academic factors

, Norni˜na J. Dia b, Redeemtor R. Sacayan c, Joseph C. Sieras b,

Reymark D. Dele˜na a,*
Suhaina A. Khalid b, Amer Hussien T. Macatotong b, Sacaria B. Gulam d
a Faculty, Department of Information Technology, College of Computer Studies, Mindanao State University – Iligan Institute of Technology, Iligan City 9200, Philippines
b Faculty, Department of Information Sciences, College of Information and Computing Sciences, Mindanao State University – Main Campus, Marawi City, Lanao Del Sur, 
9700, Philippines
c Faculty, Department of Mathematics and Statistics, College of Science and Mathematics, Mindanao State University-Iligan Institute of Technology, Iligan City 9200, 
Philippines
d Faculty, Department of Computing Sciences, College of Information and Computing Sciences, Mindanao State University – Main Campus, Marawi City, Lanao Del Sur, 
9700, Philippines

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Student retention
Educational data mining
Machine learning algorithms
Data visualization
Higher Education Analytics
Data-driven Education
Sociodemographic Factors
Academic Factors
eXtreme Gradient Boosting

Student dropout remains a persistent challenge in higher education, particularly in developing regions where 
institutional  resources  for  intervention  are  limited.  This  study  explores  the  predictive  potential  of  machine 
learning  (ML)  algorithms  in  identifying  students  at  risk  of  dropping  out  using  historical  academic  and  socio-
demographic data from Mindanao State University–Main Campus, covering a ten-year period (2012–2022). A 
total of 482 student records and 146 variables were preprocessed using Power BI and prepared via the CRISP-DM 
methodology before being modeled in Jupyter Notebook. Ten ML algorithms such asExtreme Gradient Boosting 
(XGBoost), Gradient Boosting (GB), Artificial Neural Network (ANN), Decision Tree (DT), Random Forest (RF), 
Multilayer  Perceptron  (MLP),  Logistic  Regression  (LR),  K-Nearest  Neighbor  (KNN),  Support  Vector  Machine 
(SVM),  and  Naïve  Bayes (NB)  were  evaluated  using both  train-test  split  and  5-fold  cross-validation to  ensure 
robustness  and  generalizability.  Results  indicate  that  XGBoost  outperformed  all  other  models,  achieving  the 
highest cross-validated accuracy (90.66 %), F1 Score (90.72), and one of the lowest error values (Mean Square 
Error  (MSE) = 9.34, Log Loss = 0.26). GB and ANN followed closely, demonstrating strong balance between 
precision, recall, and low misclassification rates. While models like Naïve Bayes recorded high recall, they also 
produced  excessive  false  positives,  limiting  their  practical  use.  The  study  offers  a  scalable  and  transferable 
modeling  framework  for  higher  education  institutions  seeking  to  implement  early  warning  systems.  It  also 
emphasizes the pedagogical value of integrating educational data science into Information Technology Education 
(ITE) curricula to foster real-world AI application. Limitations and future directions are discussed, particularly 
regarding behavioral data integration and model interpretability.

1. Introduction

Student  attrition  in  university  settings  has  long  been  a  pressing 
concern among educators and administrators, as it significantly affects 
institutional  rankings,  reputation,  workforce  readiness,  and  financial 
sustainability  [1,2].  Globally,  high  dropout  rates  are  associated  with 
wasted  educational  resources,  decreased  graduation  outputs,  and 
weakened national educational goals. In many developing and under-
represented contexts, particularly in Southeast Asia, challenges related 
to academic persistence are compounded by socioeconomic disparities

and infrastructure limitations. A wide range of factors contribute to a 
student’s decision to withdraw from a program, but academic perfor-
mance and sociodemographic characteristics remain the most frequently 
examined variables in retention studies [3,4].

In response to this challenge, Educational Data Mining (EDM) has 
emerged  as  a  key  area  within  educational  research,  focusing  on  the 
application of machine learning techniques to institutional data in order 
to  predict  student  outcomes  and  inform  strategic  interventions  [5]. 
Numerous  studies  have  established  that  academic  records  and  de-
mographic profiles are strong indicators of student persistence or risk of

* Corresponding author.

E-mail address: reymark.delena@g.msuiit.edu.ph (R.D. Dele˜na).

https://doi.org/10.1016/j.sasc.2025.200352
Received 14 July 2024; Received in revised form 15 June 2025; Accepted 14 July 2025  
Available online 18 July 2025 
2772-9419/© 2025 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by- 
nc-nd/4.0/ ).

---

<!-- PAGE 2 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

dropout  [3,4,6].  The  integration  of  EDM  and  machine  learning  into 
university  systems  allows  institutions—both  locally  and  globally—to 
analyze historical student data to identify learning gaps, anticipate ac-
ademic  failures,  and  predict  future  academic  trajectories  [7].  These 
predictive  insights  can  guide  data-informed  decisions  aimed  at 
improving  institutional  effectiveness and  creating supportive  learning 
environments  [8],  ultimately  helping  students  stay  on  track  toward 
timely graduation.

The  College  of  Information  and  Computing  Sciences  (CICS)  of 
Mindanao  State  University  –  Main  Campus  has  one  of  the  highest 
attrition rates within the university, which piqued the researcher’s in-
terest in this subject matter. However, the significance of this research 
extends far beyond the boundaries of one institution. As higher educa-
tion  institutions  worldwide  contend  with  increased  student  diversity, 
massification of enrollment, and post-pandemic educational disruptions, 
the ability to accurately model and address student attrition becomes a 
global imperative. Retention metrics are now pivotal not just for insti-
tutional  planning but also for  national education performance bench-
marks, accreditation compliance, and international university rankings.
Moreover, diversity and inclusion goals, particularly disaggregated 
retention statistics by gender, socio-economic status, and ethnicity, have 
gained prominence as critical indicators of how well institutions support 
marginalized student populations. These data-driven approaches offer 
powerful tools to inform not only curriculum design and student services 
but  also  equitable  resource  distribution  and  strategic  policy  develop-
ment. On a global scale, retention and graduation rates are among the 
most  scrutinized  indicators  by  ranking  bodies  and  education  quality 
assurance  agencies,  making  predictive  analytics  in  this  domain  both 
timely and globally significant.

Recent  studies  apply  diverse predictive  models  for  predicting aca-
demic  performance,  graduation,  and  dropout  [9],  enabled  by  the 
increasing availability of institutional datasets. As model performance 
depends heavily on dataset quality and size [10], large-scale research 
such  as  that  by  Alhazmi  &  Sheneamer  [11]  (275,000  students)  and 
Rodríguez-Hern´andez  et  al.  [12]  (162,030  students)  reinforces  the 
reliability of data-driven modeling. Several others, Beckham et al. [13], 
Niyogisubizo et al. [14], Ghorbani & Ghousi [15], Marbouti et al. [16], 
Lam et al. [17], and Gonzalez-Nucamendi et al. [18], explore the pre-
dictive power of various machine learning models, including hybrid and 
ensemble  approaches,  in  student  dropout  forecasting  across  countries 
such as Portugal, Colombia, Iran, and Mexico. These global efforts un-
derscore the importance of localized yet scalable modeling approaches, 
especially for contexts with high dropout risk but low representation in 
existing literature.

This  study  makes  several  key  contributions  to  the  field  of  student 
retention  analytics.  First,  it  integrates  a  comprehensive  set  of  socio-
demographic and academic variables to develop predictive models for 
student  retention  within  the  context  of  a  state  university  in  the 
Philippines, an underrepresented setting in existing literature. Second, it 
conducts a rigorous comparative evaluation of ten (10) widely adopted 
machine  learning  (ML)  algorithms,  identifying  Extreme  Gradient 
Boosting (XGBoost) as the most accurate across multiple standardized 
metrics. Third, the study leverages actual student data spanning a full 
decade  (2012–2022)  from  the  College  of  Information  and  Computing 
Sciences  (CICS)  at  Mindanao  State  University–Main  Campus,  encom-
passing its Computer Science, Information Technology, and Information 
Systems programs. This longitudinal dataset enables deeper insights into 
student  behavior  and  retention  trends  over  time,  supporting  more 
effective early intervention strategies.

The novelty of this research lies in its context-specific focus, breadth 
of model comparison, and practical implementation using institutional 
data  visualized  through  Python  in  a  Jupyter  Notebook  environment. 
While the effectiveness of ML in predicting student performance is well- 
established, much of the existing literature relies on short-term datasets, 
simulated  environments,  or  limited  algorithm  selection.  Some  studies 
also  emphasize  hybrid  model  development  without  conducting

systematic benchmarking. In contrast, this study addresses these gaps by 
employing ten ML models evaluated using six performance metrics such 
as Accuracy, F1 Score, Precision, Recall, Mean Squared Error (MSE), log 
loss, and by conducting a thorough review to identify the most relevant 
data inputs and modeling strategies.

Ultimately,  the  goal  of  this  research  is  not  only  to  achieve  high 
predictive  performance  but  also  to  provide  actionable  insights  that 
inform institutional policy, guide academic interventions, and support 
program-level strategies to reduce student attrition and improve timely 
graduation rates. By  contributing findings  from a region  with limited 
representation in literature, this study aims to support more inclusive 
and globally relevant approaches to student success analytics.

2. Material and methods

In  conducting  the  study,  secondary  data  of  CICS  students  was 
sourced from the Information and Communication Technology Center 
(ICTC), following the guidelines established by the Preferred Reporting 
Items  for  Systematic  Reviews and  Meta-Analyses  (PRISMA).  The data 
underwent  the  CRISP-DM  process.  First,  an  in-depth  analysis  of  the 
business objectives and needs was done. Next, the quality of gathered 
data was examined and cleaned. Subsequently, the data was organized 
for modeling. Ten (10) data modeling techniques were applied to predict 
the outcomes which were then evaluated using six (6) evaluation met-
rics  to  identify  the  optimal  model  that  provides  the  most  accurate 
results.

2.1. Systematic review

2.1.1. Data collection and extraction

For the systematic review, two (2) journal databases were used to 
find the recent and relevant articles necessary to conduct the systematic 
review. To find the relevant papers, the researcher used the keywords 
“Data mining”  AND “Student retention”  OR “Student performance”  in 
Science  Direct  and  “Predicting  student  retention”  + “data  mining”  in 
IEEE Xplore. Furthermore, the search was filtered to restrict the publi-
cation year between 2013 and 2023 spanning ten (10) years; this was to 
ensure that all selected papers are relevant and up to date. The query 
resulted in a total of 364 journals (see Table 1). Subsequently, MS Excel 
was used to organize, sort, and eliminate duplicates from the retrieved 
data set

2.1.2. PRISMA model

In this process as illustrated in Fig. 1, 336 records were excluded in 
the screening process due to its irrelevancy based on their title and ab-
stract. The remaining articles were then assessed for eligibility based on 
the  criteria  listed  in  Table  2 by  reviewing  them  in  full  text,  and  this 
assessment retained 21 studies listed in Table 3 .

2.1.3. Key findings

Fig.  2a  illustrates  the  frequency  with  which  various  sociodemo-
graphic factors were utilized across a set of studies. The data reveals that 
gender (9 studies) was the most frequently used factor, followed closely 
by marital status (8 studies) and age (7 studies). These results suggest 
that these variables are considered highly relevant in research exploring

Table 1 
Databases and keywords used.

No.

Database

URL

Retrieved 
Papers

1

2

Elseiver (Science 
Direct)
IEEE Xplore Digital 
Library

https://www.sciencedirect. 
com/
https://www.ieeexplore.ieee. 
org/
Total

277

87

364

2

---

<!-- PAGE 3 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

Fig. 1. PRISMA flow diagram illustrating the systematic review process for the selection of studies related to data mining and student retention/performance.

Table 2 
Inclusion and exclusion criteria.

No.

Inclusion Criteria

Exclusion Criteria

1

2
3

4

5
6

Using algorithms to predict student 
retention
Articles between 2013 and 2023
Sample population is college 
students
Journal, Conference, Thesis/ 
Dissertation
Written in English Language
Open access

Studies not utilizing predictive 
analytics
Articles older than 2013
Sample population other than college 
students
Review articles, book chapters, etc.

Not written in English Language
Paid

social or behavioral outcomes. Other moderately used factors include 
parent’s  occupation  (4  studies),  family  size  and  financial  support  (3 
studies  each),  and  guardian  and  parent’s  education/qualification  (2 
studies each). Several factors, such as address, family responsibilities, 
religious affiliation, parent’s school issues, school, travel time to school, 
and working status, were only used in a single study, indicating limited 
application or relevance in most contexts analyzed. Further, this varia-
tion in usage frequency highlights a trend in which basic demographic 
variables  like gender, age, and marital status are prioritized, possibly 
due to their availability, perceived impact, or ease of interpretation in 
predictive modeling and statistical analyses.

On the other hand, Fig. 2b depicts presents the frequency with which 
specific  academic-related  variables  were  included  across  different 
research studies. The most used academic factor was expected gradua-
tion year (n = 8), followed by grades or GPA (n = 7) and project grades 
(n = 7). These variables likely reflect students’ academic performance 
and trajectory, making them strong predictors in educational analytics.

Other  academic  factors  with  moderate  usage  include  admission  test 
score (n = 4), dropout status (n = 3), and high school GPA and year level 
(n = 3 each). Several variables such as enrollment status, student clas-
sification,  socioemotional  support,  transfer  status,  and  middle  school 
performance  were  only  used  in  one  or  two  studies,  indicating  lower 
prevalence or relevance depending on the study’s objectives. Moreover, 
the  variety  in  factor  usage  suggests  that  while  some  indicators  like 
grades and graduation timelines are central to academic studies, others 
are context-dependent and possibly underexplored. This also highlights 
an opportunity to investigate the value of less commonly used academic 
variables in future predictive or evaluative studies.

Fig.  2c  shows  the  frequency  of  usage  of  various machine  learning 
(ML) models in the studies, distinguishing between supervised and un-
supervised learning methods. It is evident that Decision Tree (n = 8), 
Multilayer  Perceptron  (MLP)  (n  = 8),  and  Support  Vector  Machine 
(SVM)  (n  = 8)  are  the  most  widely  used  supervised  learning  models, 
reflecting  their  popularity  due  to  interpretability,  accuracy,  and 
robustness  in  classification  tasks.  Other  frequently  applied  models 
include Logistic Regression (n = 6) and K-Nearest Neighbor (KNN) (n =
5). These classical models are still highly valued for their simplicity and 
effectiveness. Less frequently used models, each appearing in just one 
study, include Bayesian Network, Extreme Gradient Boosting (XGBoost), 
and Long Short-Term Memory (LSTM), among others. Notably, only a 
few models were classified under unsupervised learning (in gray), such 
as K-Means Clustering (n = 2) and J48/JRip, indicating a predominant 
focus on supervised techniques in the reviewed studies. This highlights a 
potential  research  gap  where  unsupervised  or  hybrid  learning  ap-
proaches could be further explored.

Fig. 2d illustrates the frequency of various evaluation metrics used 
across studies related to predictive modeling. Accuracy emerges as the

3

---

<!-- PAGE 4 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

Table 3 
Eligible articles that employ data mining on student retention.

No.

Author

Year

Article

Prediction Goal

Dataset 
Size

No. of 
Variables

Algorithm 
(s)

1

2

3

4

5

6

7

8

9

10

11

12
13

14

(Alhazmi & 
Sheneamer)
(Beckham et al.)

2023

2023

(Alwarthan et al.)

2022

(Feng et al.)

2022

(Mariano et al.)

2022

(Niyogisubizo 
et al.)

2022

(Singh et al.)

2022

(Marbouti et al.)

2021

(Nabil et al.)

2021

(Prabowo et al.)

2021

(Rodríguez- 
Hernandez et al.)

(Uliyan et al.)
(Fern´andez-García 
et al.)
(Ghorbani & 
Ghousi)

2021

2021
2020

2020

15

(Mengash)

2020

16

17

18

(Cardona & 
Cudney)
(Viloria et al.)

2019

2019

(Lesinski & Corns)

2018

19

(Lesinski, et al.)

2016

20

(Marbouti et al.)

2016

Early predicting of student performance in higher 
education
Determining factors that affect student performance 
using various machine learning method
An explainable model for identifying at-risk student at 
higher education
Analysis and prediction of students’ academic 
performance based on education data mining
Decision trees for predicting dropout in Engineering 
Course students in Brazil

Predicting student’s dropout in university classes using 
two-layer ensemble machine learning approach: A 
novel stacked generalization
Predicting student-teachers dropout risk and early 
identification: A four-step logistic regression approach
Academic and demographic cluster analysis of 
engineering student success
Prediction of Students’ Academic Performance Based 
on Courses’ Grades Using Deep Neural Networks
Aggregating time series and tabular data in deep 
learning model for university students’ GPA prediction
Artificial neural networks in academic performance 
prediction: Systematic implementation and predictor 
evaluation
Student retention (retention rate)
Creating a recommender system to support higher 
education students in the subject enrollment decision
Comparing different resampling methods in predicting 
students’ performance using machine learning 
techniques
Using data mining techniques to predict student 
performance to support decision making in university 
admission systems
Predicting Student Retention Using Support Vector 
Machines
Integration of data technology for analyzing university 
dropout
Multi-objective evolutionary neural network to predict 
graduation success at the United States Military 
Academy
Application of an Artificial Neural Network to Predict 
Graduation Success at the United States Military 
Academy
Models for early prediction of at-risk students in a 
course using standards-based grading

Student’s performance (CGPA)

275,000

395

N/A

N/A

91

216

1723

Factors affecting student 
performance (Correlation Score)
At-risk Students (CGPA)

Student’s performance (Poor, 
Good, Excellent)
Factors affecting student 
performance (Correlation score), 
and Dropout rate
Student dropout (Dropout or 
Non-dropout)

At-risk Students (Dropout or 
Non-dropout)
Factors affecting student 
performance (P-Value)
Student’s performance (Pass or 
Fail)
Student’s performance (GPA)

16

13

XGBoost, LR, 
SVM, KNN, RF
MLP, DT, RF

RF, ANN, SVM

[19]

7

1

2

8

8

K-means 
Clustering
DT

RF, XGBoost, GB, 
FNN

LR

12,053

10

4266

46,670

1

7

K-means 
clustering
DNN, DT, RF, GB, 
LR, SVC, KNN
MLP, LSTM

Student’s performance (Level to 
Level 4)

16,2030

11

MLP

GPA, Subjects’ grades
Student’s performance (Pass or 
Fail)
Algorithm Performance (Model 
Accuracy Scores)

Student’s performance 
(Excellent, Very Good, Good, 
Acceptable, Poor)
Algorithm performance (Model 
accuracy score)
Student dropout (Dropout or 
Non-dropout)
Graduation Status (Graduates, 
Late Graduates, Non-graduates)

2949
6948

650

2039

904

19,300

5100

Graduation Status (Graduates, 
Late graduates, Non-graduates)

5100

At-risk Students (Pass or Fail)

1600

2
14

19

2

6

4

7

7

5

BLSTM, CRF
RF, LR, DT, SVM, 
KNN, MLP, GB
RF, KNN, ANN, 
XGBoost, SVM, 
DT, LR, NB
ANN, DT, SVM, 
NB

SVM

Bayesian 
Network, DT, NN
MLP, MOEA

MLP

NB Classifier, 
SVM, KNN, LR, 
DT, MLP
RF, Random Tree, 
J48, Decision 
Stump, REPTree, 
JRip, OneR, 
ZeroR, PART, 
Decision Table, 
MLP

Ref.

[11]

[13]

[20]

[21]

[14]

[22]

[23]

[24]

[25]

[26]

[12]
[27]

[15]

[28]

[29]

[30]

[31]

[32]

[16]

[33]

21

(Goga et al.)

2015

A recommender for improving the student academic 
performance

Student’s performance (GPA)

7500

10

most  employed  metric,  reported  in  13  studies,  highlighting  its  popu-
larity  due  to  its  simplicity  and  intuitive  interpretation.  Following 
closely,  F1  Score,  Precision,  and  Recall  are  each  used  in  11  studies. 
These  three  metrics  are  especially  important  in  imbalanced  datasets 
where focusing solely on accuracy could be misleading. Other metrics 
such as MSE (used in 2 studies) and a range of others (each used once) — 
including ROC curve, R2, AUC, MAE, and RMSE — suggest that while 
diversity  exists  in  evaluation  practices,  there  is  a  clear  concentration 
around  a  few  key  indicators.  This  trend  may  reflect  a  preference  for 
metrics  that  balance  interpretability  with  robustness,  especially  in 
classification  tasks.  Interestingly,  statistical  tests  like  the  Hosmer  & 
Lemeshow test, Wald test, and Likelihood Ratio Test, though rarely used 
(only once each), indicate occasional application of inferential statistical 
methods to complement predictive accuracy. This distribution provides 
insight  into  how  performance  is  validated  in  student  retention  and

academic prediction models, pointing to a need for more consistent use 
of  varied  and  task-appropriate  evaluation  metrics  to  ensure  balanced 
model assessment.

2.2. CRISP-DM

The  Cross-Industry  Standard  Process  for  Data  Mining  (CRISP-DM) 
(Fig. 3) is widely adopted, industry - independent process model for data 
mining, extensively used in both practical applications and in research 
[34]. This cycle is composed of six phases: (1) Business Understanding 
which  focuses  on  the  understanding  of  the  project  objectives  and  re-
quirements  from  a  business  perspective;  (2)  Data  Understanding  or 
determining the data to be collected and discovering insights from it; (3) 
Data Preparation which encompasses all activities that result in the final 
dataset; (4) Modeling, where various modeling techniques are chosen

4

---

<!-- PAGE 5 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

Fig. 2. Comprehensive summary of factors, models, and evaluation metrics used in student retention prediction studies. (a) Sociodemographic factors frequently 
included in predictive models, with gender, parent’s educational attainment, and age among the most cited attributes. (b) Academic factors considered in prior 
studies, where high school GPA, failed courses, and dropout status were the most prominent predictors. (c) Machine learning models used in the literature, showing 
that  decision  tree,  random  forest,  support  vector  machine  (SVM),  and  multilayer  perceptron  (MLP)  are  the  most  employed,  all  of  which  fall  under  supervised 
learning. (d) Evaluation metrics applied in model assessment. Accuracy was the most frequently used metric, followed by F1 score, precision, and recall, reflecting a 
focus on classification performance in most studies.

5

---

<!-- PAGE 6 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

Fig. 2. (continued).

6

---

<!-- PAGE 7 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

selected were tested by setting the X and Y variables, then dividing the 
dataset into training and testing data. After that, the models were built 
for prediction using the test data.

In the evaluation stage, the algorithms were tested using the selected 
six  (6)  evaluation  metrics  to  calculate  the  accuracy  of  the  predicted 
values.  The  model  with  highest  accuracy  rate  was  the  algorithm 
deployed  for  the  final  prediction  of  student’s  probability  rate  of 
withdrawal.

2.3. Machine learning algorithms

In predictive analytics, ML algorithms are essential tools for identi-
fying trends and patterns in educational data, particularly in modeling 
student retention. These algorithms must first be trained on historical 
data to ensure accurate predictions and can be categorized into classi-
fication,  ensemble,  and  neural  network  models.  Classification  algo-
rithms  such  as  SVM  [37],  Logistic  Regression  [22],  KNN  [38],  Naïve 
Bayes [39], and Decision Tree [37] are widely used to label students as 
either  at  risk  or  likely  to  persist,  each  with  varying  assumptions  and 
sensitivities to educational data structures. SVM and LR assume Inde-
pendent  and  Identically  Distributed  (IID)  data,  though  LR  can  be 
adapted  using  generalized  estimating  equations  (GEE)  to  account  for 
clustered  errors.  KNN  is  a  non-parametric  model  sensitive  to  de-
mographic  clustering,  while  Naïve  Bayes,  despite  its  strong  indepen-
dence  assumption,  remains  useful  in  large  datasets  when  paired  with 
feature selection. Decision Trees are intuitive and flexible but prone to 
overfitting without pruning. Ensemble models like Random Forest and 
Gradient Boosting [14] combine multiple learners to improve accuracy 
and generalization [18], with Random Forest offering simplicity, short 
training time, and improved forecasting accuracy, albeit with increased 
model complexity as more trees are added [19]. XGBoost, an optimized 
implementation of gradient boosting, has emerged as a leading model 
due to its speed, built-in regularization, early stopping, and ability to 
handle  structured  and  nested  data  using  parameters  such  as  “group” 
[14]. The heterogeneity among ensemble learners helps mitigate bias 
and variance, making them robust in handling diverse student profiles 
[40].

Moreover, Neural network models are powerful algorithms inspired 
by  the  structure  and  function  of  the  human  brain.  They  process  data 
through  interconnected  layers  of  artificial  neurons,  enabling  the 
learning of non-linear relationships and adaptive weight adjustments. 
These models are particularly effective for complex prediction tasks in 
EDM environments [41]. One common variant is the ANN, which con-
sists of an input layer, one or more hidden layers, and an output layer. 
Each artificial neuron receives inputs, computes weighted sums, applies 
activation  functions,  and  passes  outputs  to  the  next  layer.  During 
training, these weights are adjusted iteratively to minimize prediction 
error. ANNs are widely applied in EDM because they can model intricate 
relationships between variables, even with small datasets, and capture 
subtle patterns in student data [28]. While standard ANN architectures 
assume IID data, educational datasets often include correlated or nested 
structures. To address this, methods such as recurrent architectures for 
time-series  data  and  dropout  layers  for  regularization  are  frequently 
used. Another variant, the MLP, expands on the ANN by incorporating 
multiple  hidden  layers,  enabling  deeper  representation  learning.  An 
MLP typically includes an input layer for features, one or more hidden 
layers for transformation, and an output layer that produces classifica-
tion  or  regression  outputs.  MLPs  are  particularly  useful  for  solving 
prediction  tasks  related  to  academic  performance and  retention [26]. 
Like  other  neural  models,  MLPs  assume  IID  inputs,  and  thus  pre-
processing  steps  such  as  batch  normalization  or  the  integration  of 
institutional-level  variables  are  recommended  when  working  with  hi-
erarchical educational data.

Fig.  3. The  CRISP-DM  (cross-industry  standard  process  for  data  mining) 
methodology adopted in this study [44]. The framework consists of six iterative 
phases:  business  understanding,  data  understanding,  data  preparation, 
modeling, evaluation, and deployment. This cyclic approach ensured that the 
predictive  modeling  process  remained  aligned  with  institutional  goals,  data 
quality, and model performance throughout the project.

and applied, and their parameters are calibrated to optimal values; and 
(5) Evaluation, where algorithms are tested to find the optimal model 
[35,36].

Higher Education Institutions (HEIs) suffer intensely from students’ 
withdrawal  as  they  are  highly  interested  and  invested  in  producing 
competent students which could positively affect their reputation in the 
market. The College of Information and Computing Sciences (CICS) in 
MSU-Main Campus is not an exemption as most of the enrolled students 
took 5 years or more to pass and complete the program (shown in Fig. 4). 
Seemingly, half of the overall population from A.Y. 2012–2022 opted to 
withdraw from the course and shift to other college to graduate early. 
Therefore, having a strong understanding of the business aspects related 
to  student  retention 
leaders  and 
administrators.

for  educational

is  essential

For data preparation stage, the data gathered from the Information 
and Communication Technology Center (ICTC) through the permission 
of the Office of the Vice Chancellor for Academic Affairs (OVCAA) of the 
Mindanao State University-Marawi (MSU-Main Campus) was inspected 
and cleaned where data was corrected, and null and erroneous values 
were imputed with zero (0). The multiple files were then integrated in a 
single  file.  Afterwards,  the  categorical  data  was  transformed  into  nu-
merical to perform the data analysis without difficulty, and the unnec-
essary attributes and period were excluded in the final dataset that was 
fed into the models used.

In  the  modeling  stage,  the  ten  (10)  machine  learning  algorithms

Fig. 4. Distribution of student academic status in the dataset.

7

---

<!-- PAGE 8 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

2.4. Evaluation metrics

To assess the performance of the machine learning models used in 
this study, six evaluation metrics were employed: Accuracy, Precision, 
Recall, F1 Score, MSE, and log loss. Accuracy measures the proportion of 
correctly predicted instances, both positive and negative, relative to the 
total number of predictions, offering a general sense of model perfor-
mance,  especially  in  balanced  datasets  [42].  Precision  quantifies  the 
number  of  correctly  predicted  positive  cases  out  of  all  instances  pre-
dicted  as  positive,  thereby  reflecting  the  model’s  ability  to  minimize 
false positives. In contrast, Recall, or sensitivity, evaluates the model’s 
capacity to identify all relevant positive instances, making it crucial in 
contexts  where  missing  at-risk  students  has  significant  consequences. 
The  F1  Score,  which  is  the  harmonic  mean  of  Precision  and  Recall, 
provides a balanced assessment when there is a trade-off between the 
two, and is especially useful in handling imbalanced educational data 
[43]. Moreover, MSE is applied to measure the average squared differ-
ence between actual and predicted values in regression-based outputs, 
with lower values indicating more accurate models. Lastly, the log loss, 
used to evaluate the performance of probabilistic classification where 
lower  log  loss  indicates  better  performance.  These  metrics  together 
enable  a  comprehensive  evaluation  of  classification  and  regression 
performance in predicting student retention outcomes.

2.5. Modeling setup

All machine learning models were implemented using Python 3.10 in 
a  Jupyter  Notebook  environment.  The  following  libraries  were  used: 
pandas  for  data  preprocessing,  scikit-learn  for  model  training  and 
evaluation,  xgboost  for  gradient  boosting  implementation,  and  mat-
plotlib/seaborn for visualization. To ensure robustness in model evalu-
ation, a 5-fold cross-validation approach was adopted using KFold from 
the scikit-learn library. This method randomly splits the dataset into five 
equally sized folds. For each iteration, four folds were used to train the 
model while the remaining fold was used for validation. This process 
was repeated five times so that each data point served as a validation 
sample  once.  The  use  of  cross-validation  reduces  the  likelihood  of 
overfitting and ensures the generalizability of results. Hyperparameter 
tuning was done manually for transparency, and all models were eval-
uated  using  the  six  standard  metrics  described  in  Section  2.4.  No 
mathematical  derivations  were  included,  as  this  study  focuses  on  the 
applied implementation of machine learning for institutional decision 
support in student retention.

2.6. Dataset description

The dataset utilized in this study comprises 482 anonymized student 
records drawn from the Information Technology Education (ITE) pro-
gram at Mindanao State University –  Main Campus across curriculum 
(see Table 4). It contains 146 variables, meticulously curated to repre-
sent  a  comprehensive  view  of  each  student’s  academic  journey,

Table 4 
Summary of dataset characteristics for student retention modeling.

Characteristic

Description

Sample size (records)
Number of features
Dropout rate
Retention rate
Missing values
Feature categories
• Sociodemographic
• Academic

Performance

• Program Progression

• Target Variable

482 student records
146 total variables
50.2 % (242 students)
49.8 % (240 students)
None (dataset is 100 % complete)

Age, Sex, Province, City, Civil Status, Parent’s Income
Course grades (e.g., CCC, ITE, STT, MAT subjects), 
normalized on a [0,1] scale
Year Level, Program Code, Total Units Earned, Course 
History
DROPOUT (binary: 0 = retained, 1 = withdrawn)

demographic background, and socio-economic context. These attributes 
serve as predictive inputs for modeling student retention outcomes, with 
the DROPOUT variable encoded as a binary target (0 = retained, 1 =
withdrawn).

The dataset is entirely complete, containing no missing values, which 
enhances  its  integrity  for  robust  machine  learning  applications.  The 
feature set is composed of two primary categories: (1) sociodemographic 
attributes, such as AGE, SEX, CITY, PROVINCE, CIVILSTATUS, MOTH-
ERINCOME, and FATHERINCOME, which provide insight into the stu-
dents’  geographic  and  economic  contexts;  (2)  academic  attributes, 
encompassing raw or normalized performance indicators derived from 
institutional  grading  systems—examples  include  PED001  to  PED012, 
STT071,  and  STT101,  which  likely  correspond  to  core  and  technical 
courses  specified  in  the  university’s  prospectus;  and  (3)  program- 
specific variables, such as PROGRAM, YEARLEVEL, and COURSE HIS-
TORY, capturing progression within the prescribed BSIT-D track.

These academic features reflect the learning milestones embedded in 
the  ITE  curriculum,  such  as  basic  computer  programming  subjects, 
mathematics, probability and statistics for computing, data structures. 
and advanced database systems. Many of the performance variables are 
likely derived from institutional logs and standardized academic met-
rics, normalized within a [0,1] scale, allowing for effective comparison 
across subjects and semesters. The inclusion of longitudinal academic 
indicators and technical subject coverage enables the model to capture 
performance trends critical to predicting attrition.

Furthermore,  the  dataset’s  balanced  class  distribution  (approxi-
mately 50 % dropout, 50 % retained) supports fair model training and 
evaluation without the need for resampling or synthetic balancing. The 
presence of highly granular features, such as course-level assessments 
and  regional  identifiers,  adds  dimensional  richness  to  the  analysis, 
enabling  the  exploration  of  intersectional  retention  risks  (e.g.,  by 
geographic origin or year level).

This dataset exemplifies the growing intersection between academic 
analytics and educational data mining in the Philippine higher educa-
tion landscape. It offers a rare opportunity to apply machine learning 
models to real-world academic data with direct implications for insti-
tutional  policy,  early  warning  systems,  and  student  support  in-
terventions. By aligning variable design with curriculum structure and 
institutional  reporting  systems,  the  dataset  ensures  both  contextual 
relevance and technical rigor for predictive modeling of student reten-
tion  and  also  was  reportedly  used  by  this  study  [44].  The  dataset  is 
openly available for public access through CodeOcean [45].

3. Results

This section presents the results of machine learning model assess-
ments conducted on historical data collected over a decade (2012–2022) 
from the Information and Communication Technology Center (ICTC) of 
Mindanao  State  University-Main  Campus.  The  data  underwent  pre-
processing in Power BI using the CRISP-DM methodology before being 
imported into Jupyter Notebook for further analysis. Subsequently, the 
dataset was partitioned into X (independent variables) and Y (dependent 
variables) and split into training (70 %) and testing (30 %) sets. During 
analysis, variables highly correlated with the dependent variable were 
identified through Spearman coefficient (ρ or rho) in correlation analysis 
(Table  5)  and  subsequently  removed  to  avoid  multicollinearity,

Table 5 
Rule of thumb or interpretation of Spearman’s correlation value [46].

Size of correlation

Interpretation

±.90 to ±1.0
±.70 to ±.90
±.50 to ±.70
±.30 to ±.50
.00 to ±.30

8

Very high positive/negative correlation
High positive/negative correlation
Moderate positive/negative correlation
Low positive/negative correlation
Negligible correlation

---

<!-- PAGE 9 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

Fig. 5. Number of actual and correct prediciton comparison.

resulting  in  the  retainment  of  79  columns  out  of  the  initial  134.  See 
Appendix A for the code of removing multicollinearity.

Fig. 5 illustrates the number of actual and correctly predicted results 
by  the  ten  (10)  machine  learning  algorithms.  Results  indicate  that 
among  the  evaluated  models,  the  XgBoost  algorithm  achieves  the 
highest accuracy, correctly predicting 136 instances when compared to 
the actual y-values in the test dataset. This performance is then followed 
by the GB and Decision Tree (DT) models, which correctly predicted 134 
and 131 instances, respectively, out of a total of 145. Further, the sample 
code used to assess the prediction accuracy of XgBoost is listed in Ap-
pendix B. A confusion matrix was also created to quantify correct pre-
dictions for the y-values (Dropout or Non-dropout).

On the other hand, Fig. 6 presents the confusion matrices for each 
classification model, while Table 6 provides a comparative summary of 
their predictive performance in identifying student dropout. Among the 
evaluated models, XGBoost demonstrated the most robust classification 
capability, achieving 67 true positives (correctly identified dropouts), 5 
false  positives  (non-dropouts  misclassified  as  dropouts),  4  false

negatives (dropouts misclassified as non-dropouts), and 69 true nega-
tives  (correctly  identified  non-dropouts).  These  results  indicate  that 
XGBoost achieved the highest overall classification accuracy across both 
dropout and retention classes. As a reference, in the standard confusion 
matrix  layout,  the  top-left  cell  represents  true  positives,  top-right  in-
dicates false positives, bottom-left corresponds to false negatives, and 
bottom-right denotes true negatives.

Close behind XGBoost were the GB and ANN models, both of which 
exhibited strong and balanced predictive performance. The GB model 
yielded 66 true positives, 6 false positives, 5 false negatives, and 68 true 
negatives,  indicating  a  high  degree  of  precision  and  recall.  The  ANN 
model achieved 60 true positives, 12 false positives, 5 false negatives, 
and  68  true  negatives.  Although  both  models  performed  well,  they 
incurred  slightly  higher  misclassification  rates  compared  to  XGBoost. 
Nevertheless, GB and ANN demonstrated commendable levels of sensi-
tivity (recall of actual dropouts) and specificity (correct identification of 
non-dropouts),  supporting  their  utility  in  retention-related  prediction 
tasks.

Fig. 6. Confusion matrix summary for each machine learning model.

9

---

<!-- PAGE 10 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

Table 6 
Confusion matrix components and dropout detection rates of machine learning 
models.

Model

True 
Positive 
(Correct 
Dropout)

False 
Negative 
(Missed 
Dropout)

False 
Positive 
(False 
Dropout)

True 
Negatives 
(Correct 
Not 
Dropout)

SVM

RF

MLP

DT

LR

KNN

ANN

61

64

66

67

63

71

68

XGBoost

69

GB

NB

68

67

12

17

9

7

6

10

2

5

4

5

6

8

9

8

12

29

12

5

6

31

55

64

63

64

60

43

60

67

66

41

Dropout 
Detection 
Rate (TPR / 
Recall)

61 / 
(61+12) =
0.836
64 / (64+9) 
= 0.877
66 / (66+7) 
= 0.904
67 / (67+6) 
= 0.918
63 / 
(63+10) =
0.863
71 / (71+2) 
= 0.972
68 / (68+5) 
= 0.932
69 / 
(69þ4) ¼
0.945
68 / (68+5) 
= 0.932
67 / (67+6) 
= 0.918

Table 7 presents the initial evaluation results of ten machine learning 
models based on a standard train-test split. The assessment covers key 
classification metrics, such as Accuracy, Precision, Recall, and F1 Score, 
as  well  as  error  metrics  like  MSE  and  Log  Loss.  Among  all  models, 
Extreme Gradient Boosting (XGBoost) demonstrated the strongest per-
formance, achieving the highest accuracy (93.79 %), F1 Score (93.88), 
and  lowest  MSE  (6.21),  with  a  competitive  Log  Loss  value  of  3.98. 
Similarly,  Gradient  Boosting  yielded  high  classification  scores,  with 
92.41 % accuracy and 92.52 F1 Score, and matched the lowest Log Loss 
value  (3.23),  suggesting  well-calibrated  probability  estimates.  Multi-
layer  Perceptron  (MLP)  and  Artificial  Neural  Network  (ANN)  models 
also performed strongly, particularly in recall (90.41 % and 93.15 %, 
respectively), indicating their sensitivity in identifying students at risk of 
withdrawal.

The Decision Tree classifier recorded competitive scores, including a 
90.34 % accuracy and 90.54 F1 Score. However, its Log Loss was rela-
tively high at 5.47, suggesting less confidence in its probability estimates 
despite good classification performance. Conversely, Naïve Bayes, while 
achieving a high recall of 91.78 %, posted the lowest precision (68.37 %) 
and the poorest error scores, with the highest MSE (25.52) and Log Loss 
(9.45), reflecting a high false positive rate and poor calibration. Support 
Vector Machine (SVM) similarly underperformed, with an accuracy of 
80.00 %, MSE of 20.00, and a Log Loss of 5.72.

The  addition  of  MSE  and  Log  Loss  in  this  preliminary  evaluation

Table 7 
Assessment scores of each model.

provides  a  more  nuanced  view  of  each  model’s  performance.  While 
traditional  classification  metrics  suggest  strong  outcomes,  the  error 
metrics, particularly Log Loss, highlight how well each model estimates 
class probabilities. A lower Log Loss indicates that the model is not only 
predicting correctly but is also confident and accurate in its probability 
estimates  [47].  In  this  context,  XGBoost  and  Gradient  Boosting  are 
shown to be not just accurate, but also well-calibrated.

However,  these  results  are  derived  from  a  single  train-test  split, 
which  may  be  subject  to  sampling  bias  and  overfitting,  especially  in 
datasets  with  class  imbalance  or  limited  size  [48].  The observed  per-
formance could therefore be overly optimistic. As such, further valida-
tion using K-Fold cross-validation was performed and is discussed in the 
succeeding section to assess the stability and generalizability of these 
models.

To address this, 5-fold cross-validation was applied to each model, 
offering  a  more  reliable  measure  of  generalization.  When  validated 
using this method, as shown in Fig. 7, several models exhibited perfor-
mance  declines.  Notably,  the  Decision  Tree  classifier,  which  initially 
recorded over 90 % accuracy, saw a reduction to 84.44 %, with a cor-
responding  drop  in  F1  Score  and  an  increase  in  error  metrics.  This 
suggests  that  its  original  performance  was  likely  influenced  by  over-
fitting. Similarly, XGBoost, while still the top performer, experienced a 
slight reduction in accuracy to 90.66 % and a modest increase in error, 
reflecting  a  more  realistic  estimate  of  its  predictive  strength.  Naïve 
Bayes continued to display high recall but was again marked by poor 
precision and increased error, further confirming its tendency to over-
predict positive cases. In contrast, models such as Random Forest, Lo-
gistic  Regression,  and  Multilayer  Perceptron  maintained  relatively 
consistent  performance  across  both  evaluation  strategies,  suggesting 
more stable generalization.

These results underscore the necessity of employing cross-validation 
techniques  when  evaluating  machine  learning  models,  especially  in 
sensitive domains like education. While initial single-split evaluations 
are  useful  for  exploratory  comparisons,  they  do  not  account  for  vari-
ability and are prone to optimistic bias. Cross-validation mitigates these 
risks  by  ensuring  each  data  point  contributes  to  both  training  and 
testing,  resulting  in  more  robust  and  generalizable  performance 
estimates.

Furthermore  cross-validation  revealed  meaningful  differences  in 
model  performance,  correcting  overestimations  observed  in  pre- 
validation results. The XGBoost model remained the most reliable and 
consistent across all metrics, reinforcing its suitability for deployment in 
early warning systems aimed at reducing student attrition. These find-
ings  highlight  the  importance  of  rigorous  validation  when  applying 
predictive analytics to educational decision-making.

4. Discussion

Student  retention  continues  to  be  a  persistent  challenge  in  higher 
education,  with  significant  implications  for  institutional  rankings, 
reputational standing, and financial sustainability. As such, it remains a 
widely  studied  area  in  academic  literature.  Traditional  approaches

No.

MODEL

Accuracy ( %)

Precision ( %)

Recall ( %)

F1 score ( %)

1
2
3
4
5
6
7
8
9
10

Support Vector Machine
Random Forest
Multilayer Perceptron
Decision Tree
Logistic Regression
K-Nearest Neighbor
Artificial Neural Network
Extreme Gradient Boosting
Gradient Boosting
Naive Bayes

80.00
88.28
88.97
90.34
84.83
83.45
88.28
93.79
92.41
74.48

83.56
87.67
90.41
91.78
86.30
91.78
93.15
94.52
93.15
91.78

80.79
88.28
89.19
90.54
85.14
84.81
88.89
93.88
92.52
78.36

78.21
88.89
88.00
89.33
84.00
78.82
85.00
93.24
91.89
68.37

10

MSE

20.0
11.7
11.0
9.66
15.1
16.55
10.61
6.21
7.59
25.52

Log Loss

5.72
3.98
3.23
5.47
8.20
7.21
4.23
3.98
3.23
9.45

---

<!-- PAGE 11 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

Fig. 7. Model performance based on classification and error metrics (5-fold cross-validation). This figure compares ten machine learning models using classification 
metrics—accuracy, precision, recall, and F1 score (left panel), alongside error metrics, MSE and log loss (right panel), evaluated using 5-fold cross-validation. Among 
the models, extreme gradient boosting (XGBoost) achieved the highest accuracy (90.66 %), F1 score (90.72), and one of the lowest error values (MSE = 9.34, log loss 
= 0.26), indicating superior predictive performance. Gradient boosting and multilayer perceptron (MLP) also exhibited competitive results with strong classification 
scores and low error values. Conversely, Naïve Bayes and support vector machine (SVM) showed higher error metrics, reflecting less consistent predictive reliability. 
These metrics provide a balanced view of both classification correctness and model confidence, aiding in robust model selection for student retention prediction tasks.

relying on subjective assessments and historical trends are often insuf-
ficient to capture the complexity of student attrition. To improve pre-
dictive capability and support timely interventions, ML techniques have 
become  increasingly  prominent.  These  methods  enable  institutions  to 
extract patterns from diverse data sources, generate accurate dropout 
predictions, and inform data-driven policies aimed at improving student 
outcomes.

In this study, multiple ML models were evaluated to predict student 
dropout using a combination of academic and sociodemographic factors. 
The  models were first  assessed using  a  traditional train-test split,  fol-
lowed by a more rigorous 5-fold cross-validation, to ensure robustness 
and generalizability of results. Across both evaluation phases, Extreme 
Gradient Boosting (XGBoost) consistently outperformed other models. 
In the initial evaluation, XGBoost achieved an accuracy of 93.79 %, F1 
Score  of  93.88,  and  the  lowest  MSE  of  6.21.  After  cross-validation, 
XGBoost  maintained  its  top-ranking  performance,  achieving  an 
average accuracy of 90.66 %, F1 Score of 90.72, and low error metrics 
(MSE = 9.34, Log Loss = 0.26). The confusion matrix also reinforced 
these findings, with XGBoost yielding 67 true positives, 69 true nega-
tives,  5  false  positives,  and  only  4  false  negatives—the  lowest  total 
misclassifications among all models tested. Moreover, these results are 
strongly supported by prior literature. Study [49] found that XGBoost 
consistently outperformed alternative models in forecasting tasks such 
as  stock  price  movements.  Similarly  [50],  emphasized  XGBoost’s  ca-
pacity for generalization, reduced overfitting, and enhanced predictive 
accuracy  [51].  noted  that  XGBoost  is  uniquely  capable  of  handling 
heterogeneous and noisy datasets, outperforming models that perform 
best only under controlled or homogeneous input conditions. Further-
more  [52],  reported  that  XGBoost  achieves  superior  accuracy,  speci-
ficity, and sensitivity compared to Logistic Regression, particularly in 
handling  class-imbalanced  datasets,  an  important  feature  in  dropout 
prediction,  where  class  imbalance  is  often  present.  Together,  these 
findings  and  our  results  strongly  establish  XGBoost  as  a  robust  and 
adaptable model for educational prediction tasks.

Conversely,  Naïve  Bayes  was  consistently  the  weakest  performer

across all evaluation phases. It yielded the lowest accuracy (74.48 %) in 
the initial evaluation and the highest error metrics after cross-validation 
(MSE = 24.06, Log Loss = 8.67). Although Naïve Bayes recorded the 
highest recall (97.21 %), it also produced 31 false positives, indicating a 
tendency to over-predict dropout risk. While its simplicity and compu-
tational  efficiency  may  still  make  it  suitable  for  certain  contexts  or 
ensemble integration, the high misclassification rates suggest it may not 
be  ideal  for  high-stakes  educational  interventions  without  further 
refinement.

The  analysis  also  highlighted  important  trade-offs  between  para-
metric  and  nonparametric  models.  For  example,  K-Nearest  Neighbors 
(KNN), a nonparametric algorithm, achieved the highest recall (97.2 %) 
but  also  had  one  of  the  highest  false  positive  counts  (29).  Likewise, 
Decision  Tree,  another  nonparametric  method,  showed  strong  recall 
(91.8  %)  but  relatively  poor  error  metrics,  reflecting  sensitivity  to 
overfitting and variability across folds. These models are highly effective 
in pattern detection but may require careful tuning and ensemble inte-
gration to enhance stability.

On the other hand, ensemble and hybrid models such as GB and ANN 
offered  competitive, balanced  performance. GB achieved 89.42 %  ac-
curacy  post-cross-validation  with  a  low  Log  Loss  of  0.25,  the  lowest 
among all models, and maintained strong classification results (66 true 
positives,  68  true  negatives). ANN  followed  closely with  88.39  %  ac-
curacy, 86.35 % precision, and a high recall of 91.48 %. These models 
demonstrate  high  sensitivity  and  specificity  while  maintaining  fewer 
misclassifications,  supporting  their  reliability  for  real-world  applica-
tions. Also, the potential of neural network models is further supported 
by [53], which found that deep learning architectures, including MLP 
and ANN, outperform traditional statistical methods in modeling com-
plex  and  nonlinear  patterns  in  student  data.  However,  our  findings 
suggest that while ANN performed competitively, XGBoost retained a 
performance  edge  in  terms  of  both  classification  accuracy  and  error 
minimization, suggesting greater generalizability and practical usabil-
ity, especially when false positives must be minimized in institutional 
settings.

11

---

<!-- PAGE 12 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

The integration of the predictive modeling framework developed in 
this study demonstrates substantial pedagogical and institutional value 
for ITE curricula in the Philippines. Although the analysis was conducted 
using  data  from  a  single  institution,  Mindanao  State  University  Main 
Campus in Marawi City, the design and structure of the dataset establish 
a scalable and transferable foundation that can be readily adopted by 
other higher education institutions. The dataset comprises 482 complete 
student records and 146 variables, encompassing essential dimensions 
of student profiling such as sociodemographic indicators (e.g., age, sex, 
parental income), academic performance (e.g., normalized grades), and 
program progression metrics (e.g., year level, total units earned, course 
history).  These  data  dimensions  are  consistent  with  widely  accepted 
frameworks in educational data mining and learning analytics [54,55], 
making the model broadly applicable across academic settings.

Importantly,  this  framework  offers  a  replicable  blueprint  for  in-
stitutions aiming to develop their own student retention analytics. Prior 
studies emphasize that predictive models based on institutional data can 
effectively  identify  at-risk  students  and  guide  timely  interventions 
[9–11,13–16]. Since the variables used in this study are generalizable 
and align with common student information systems, other universities 
can  easily  adapt  their  internal  data  infrastructures  to  adopt  similar 
models. This creates a pathway for ITE programs to lead institutional 
analytics initiatives, fostering real-world engagement with artificial in-
telligence  while strengthening  the  culture of  data-informed  decision--
making in education.

Moreover, this study underscores the strategic role of ITE programs 
in driving institutional digital transformation. As digital transformation 
in  education  increasingly  relies  on  data-driven  approaches  [53], 
equipping students and faculty with the capability to build and interpret 
predictive  models  using  academic  data  is  both  timely  and  necessary. 
Engaging with real institutional data not only cultivates technical skills 
but also develops ethical reasoning and accountability in the use of AI in 
education—a point highlighted in literature on educational data science 
[14,18,37]. By empowering students to apply these models within their 
own institutions, ITE departments position themselves as active agents 
of  change,  contributing  to  improved  educational  outcomes  through 
interpretable, context-aware, and impactful computing solutions.

Looking forward, future research on student retention should prior-
itize the integration of psychosocial, behavioral, and engagement-based 
features  [56]  such  as  attendance,  motivation,  learning  management 
system (LMS) activity [57], and peer interaction data [58], to enhance 
predictive power. Moreover, temporal modeling using architectures like 
Long Short-Term Memory (LSTM) networks offers promising potential 
for real-time risk monitoring and longitudinal trend analysis across se-
mesters [25]. To improve both model performance and interpretability, 
researchers are also encouraged to explore Deep P-Spline Models [59], 
Additive Gaussian Process Models [60], and hybrid ensemble strategies, 
which  offer  scalable  and  flexible  frameworks  for  capturing  complex 
non-linear patterns in large, structured educational datasets.

Furthermore, the results of this study affirm that XGBoost is the most 
accurate,  stable,  and  generalizable  model  for  predicting  student 
dropout,  outperforming  both  traditional  and  deep  learning  methods. 
However,  the  continued  development  of  richer  datasets,  more  inter-
pretable models, and ethically aligned deployment practices will be vital 
in  advancing  the  field  of  educational  data  mining  and  its  impact  on 
student success, particularly when integrated into IT education for both 
instructional and institutional innovation.

5. Conclusions

This study evaluated ten machine learning algorithms for predicting 
student dropout using historical data from MSU-Marawi spanning 2012 
to 2022. Through the application of the CRISP-DM methodology, com-
bined  with  Power  BI  for  preprocessing  and  Jupyter  Notebook  for 
modeling, the data was rigorously prepared for analysis. After filtering 
variables  using  Spearman  correlation  to  minimize  multicollinearity,

models were assessed using both a traditional train-test split and 5-fold 
cross-validation. Among the tested models, XGBoost consistently deliv-
ered the highest performance in both classification and error metrics, 
with an average cross-validated accuracy of 90.66 %, F1 Score of 90.72, 
and low error values (MSE = 9.34, Log Loss = 0.26). Ensemble models 
such  as  GB and  ANN  also showed  strong  and  balanced  results.  These 
findings  demonstrate  that  predictive  modeling,  particularly  using 
ensemble and neural network techniques, offers significant promise for 
building  early  warning  systems  that  can  identify  students  at  risk  of 
attrition. Moreover, the dataset and modeling approach are structured in 
a  generalizable  format,  offering  a  transferable  framework  for  other 
higher  education  institutions  aiming  to  improve  student  retention 
through  analytics.  From  a  pedagogical  perspective,  the  integration  of 
predictive modeling into ITE programs can cultivate technical compe-
tence in educational data science while reinforcing real-world applica-
tion of AI in institutional contexts.

Despite its promising outcomes, this study is not without limitations. 
First, the data was sourced from a single institution, which may limit the 
external validity of the findings despite the dataset’s broad and gener-
alized features. Further, while 5-fold cross-validation mitigated risks of 
overfitting and sampling bias, more advanced validation strategies such 
as  stratified  or  nested  cross-validation  could  yield  even  more  robust 
generalization. In addition, the study focused primarily on academic and 
sociodemographic  variables;  behavioral  and  psychosocial  dimensions, 
such  as  LMS  engagement,  motivation,  or  peer  interaction,  were  not 
included but are known to be significant predictors of student success. 
The inclusion of these features in future studies may improve the pre-
cision and contextual relevance of predictive models. Similarly, while 
XGBoost  achieved  the  strongest  performance,  model  interpretability 
remains a challenge for deployment in sensitive domains like education. 
Institutions seeking to implement such models should complement high- 
performance  algorithms  with  explainable  AI  tools  to  ensure  trans-
parency,  fairness,  and  ethical  accountability.  Lastly,  this  study  re-
inforces  the  emerging  role  of  ITE  programs  in  driving  institutional 
digital transformation by equipping both faculty and students with the 
skills  to  develop  intelligent  systems  grounded  in  real-world  data. 
Looking ahead, future research can build on this work by investigating 
hybrid  ensemble  techniques,  Deep  P-Spline  architectures,  Additive 
Gaussian  Process  Models,  and  longitudinal  approaches  such  as  LSTM 
networks to capture more nuanced patterns in student dropout behavior. 
As higher education institutions increasingly embrace data-driven de-
cision-making, this study serves as both a foundational benchmark and a 
transferable framework for embedding predictive analytics into educa-
tional practice and strategic policy formulation.

Acknowledgment

The authros would like to express their sincere gratitude to Mind-
anao State University - Main Campus, and the Office of the Vice Chan-
celor for Academic Affairs for granting permissoin to utilize students’ 
academic and sociodemographic data for this research. Special thanks 
are also extended to the Mamitua Saber Institute of Research and Cre-
ation (MSIRC) for their valuable support throughout the conduct of the 
study.

CRediT authorship contribution statement

Reymark D. Dele˜na: Writing – review & editing, Writing – original 
draft,  Visualization,  Validation,  Supervision,  Software,  Resources, 
Project  administration,  Methodology,  Investigation,  Funding  acquisi-
tion,  Formal  analysis,  Data  curation,  Conceptualization.  Norni˜na  J. 
Dia: Writing – original draft, Visualization, Software, Resources, Project 
administration,  Methodology,  Investigation,  Formal  analysis,  Data 
curation, Conceptualization. Redeemtor R. Sacayan: Writing – original 
draft,  Validation,  Funding  acquisition,  Formal  analysis.  Joseph  C. 
Sieras:  Supervision,  Funding  acquisition,  Conceptualization.  Suhaina

12

---

<!-- PAGE 13 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

A.  Khalid:  Resources,  Investigation,  Funding  acquisition.  Amer  Hus-
sien T. Macatotong: Software, Resources, Funding acquisition. Sacaria 
B. Gulam: Resources, Funding acquisition, Data curation.

Declaration of competing interest

("Recall  Score:  ",  recall_xgb)  print("F1  Score:  ",  f1_xgb)  print("Mean 
Squared Error: ", mse_xgb)

# GENERATING THE CONFUSION MATRIX cm = confusion_matrix 
(y_test,  prediction_xgb)  sns.heatmap(cm,  annot=True)  plt.ylabel(’Pre-
diction’,fontsize=13)  plt.xlabel(’Actual’,fontsize=13)  plt.title(’Confu-
sion Matrix’,fontsize=17) plt.show()

The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.

#COMPUTING THE LOG LOSS OF THE MODEL from sklearn.metrics 
import log_loss ll_xgb = log_loss(y_test, prediction_xgb) print(’Log Loss 
of Extreme Gradient Boosting:’, ll_xgb)

Appendices

Data availability

Splitting the data into training and testing data then removing 
multicollinearity

If this paper is accepted for publication, the data will be published in

a separate article.

#TRANSFORMING  THE  CATEGORICAL  INTO  NUMERICAL  DATA

References

from sklearn.preprocessing import LabelEncoder

#creating an instance of Label Encoder le = LabelEncoder()
#Using .fit_transform function to fit label encoder and return enco-

ded label label = le.fit_transform(student_df[’DROPOUT’])

#removing  the  categorized  (old)  column  ’TARGET’  and  adding 
student_df.drop 
contains  numerical  data.

‘DROPOUT’  which 
(’DROPOUT’, axis=1, inplace=True) student_df[’DROPOUT’] = label

#SPLITTING  THE  DATA  INTO  TESTING  AND  TRAINING  from

sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
#GENERATING THE CORRELATION MATRIX corrmat = student_df. 
corr(method = "spearman") corrmat plt.figure(figsize=(50,50)) mask =
np.triu(np.ones_like(corrmat, 
sns.heatmap(corrmat, 
annot=True,  annot_kws={"size":4},  mask=mask,  vmin=-1,  vmax=1) 
plt.title(’Correlation Coefficient of Predictors’) plt.show

dtype=bool))

#REMOVING THE HIGHLY CORRELATED VARIABLES (WITH ≥70 
% THRESHOLD) def correlation(student_df, threshold): correlated_cols 
= set() corr_matrix = student_df.corr(method="spearman") for i in range 
(len(corr_matrix.columns)):  for j in range (i):  if abs(corr_matrix.iloc[i, 
j])> threshold:  colname  = corr_matrix.columns[i]  correlated_cols.add 
(colname) return correlated_cols

#storing the variables with ≥70 % threshold in corr_features then

removing them. corr_feature = correlation(student_df, 0.7)
X_train.drop(labels=corr_feature, axis=1, inplace=True)
X_test.drop(labels=corr_feature, axis=1, inplace=True)
#plotting the new matrix corr = X_train.corr(method="spearman") 
plt.figure(figsize=(30,30))  mask  = np.triu(np.ones_like(corr,  dty-
pe=bool)) 
sns.heatmap(corr,  annot=True,  annot_kws={"size":4}, 
mask=mask,  vmin=-1,  vmax=1)  plt.title(’Correlation  Coefficient  of 
Predictors’) plt.show

Sample code for identifying the prediction performance of a model

#importing  evaluation  metrics  from  sklearn.metrics  import  accu-
racy_score,  precision_score,  recall_score,  f1_score,  mean_squared_error 
from sklearn.metrics import confusion_matrix

#importing the model import xgboost as xgb xgb = xgb.XGBClassi-

fier()

#fitting the model xgb.fit(X_train, y_train)
#TESTING  THE PREDICTION prediction_xgb = xgb.predict(X_test)

prediction_xgb

Assessing the accuracy rate of the model

#checking the evaluation metrics score of the model accuracy_xgb =
accuracy_score(y_test, prediction_xgb)*100 precision_xgb = precision_-
score(y_test,  prediction_xgb)*100  recall_xgb  = recall_score(y_test,  pre-
diction_xgb)*100 f1_xgb = f1_score(y_test, prediction_xgb)*100 mse_xgb 
= mean_squared_error(y_test,  prediction_xgb)*100  print("Accuracy 
Score:  ",  accuracy_xgb)  print("Precision  Score:  ",  precision_xgb)  print

[1] S. Ameri, M.J. Fard, R.B. Chinnam, C.K. Reddy, Survival analysis based framework

for early prediction of student dropouts, in: International Conference on 
Information and Knowledge Management, Proceedings, 2016, pp. 903–912, 
https://doi.org/10.1145/2983323.2983351, 24-28-October-2016.

[2] S. Trivedi, Improving students’ retention using machine learning: impacts and 
implications, Sci. Prepr. (2022), https://doi.org/10.14293/S2199-1006.1.SOR-. 
PPZMB0B.V2.

[3] Bineid, A.A. (2022). Predicting student withdrawal from UAE CHEDS repository 
using data mining methodology. 1–72. https://bspace.buid.ac.ae/handle/1234/ 
2130.

[4] Calvert, C.E. (2014). Developing a model and applications for probabilities of

student success: a case study of predictive analytics. 29(2), 160–173. https://doi. 
org/10.1080/02680513.2014.931805.

[5] R.S.J.d. Baker, K. Yacef, The State of educational data mining in 2009: a review and 
future visions, J. Educ. Data Min. 1 (1) (2009) 3–17, https://doi.org/10.5281/ 
ZENODO.3554657.

[6] Fain, P. (2016). Data on student engagement with an LMS is a key to predicting 
retention. https://www.insidehighered.com/news/2016/06/13/data-student- 
engagement-lms-key-predicting-retention.

[7] A.I. Adekitan, E. Noma-Osaghae, Data mining approach to predicting the

performance of first year student in a university using the admission requirements, 
Educ. Inf. Technol. 24 (2) (2018) 1527–1543, https://doi.org/10.1007/S10639- 
018-9839-7, 2018 24:2.

[8] M. Bucos, B. Dr˘agulescu, Predicting student success using data generated in

traditional educational environments, TEM J. 7 (3) (2018) 617, https://doi.org/ 
10.18421/TEM73-19.

[9] A.I. Adekitan, E. Noma-Osaghae, Data mining approach to predicting the

performance of first year student in a university using the admission requirements, 
Educ. Inf. Technol. 24 (2) (2018) 1527–1543, https://doi.org/10.1007/S10639- 
018-9839-7, 2018 24:2.

[10] H. Almarabeh, Analysis of students’ performance by using different data mining

classifiers, Int. J. Mod. Educ. Comput. Sci. 9 (8) (2017) 9–15, https://doi.org/ 
10.5815/IJMECS.2017.08.02.

[11] E. Alhazmi, A. Sheneamer, Early predicting of students performance in higher 
education, IEEE Access 11 (2023) 27579–27589, https://doi.org/10.1109/ 
ACCESS.2023.3250702.

[12] D. Uliyan, A.S. Aljaloud, A. Alkhalil, H.S.A. Amer, M.A.E.A. Mohamed, A.F.

M. Alogali, Deep learning model to predict students retention using BLSTM and 
CRF, IEEE Access 9 (2021) 135550–135558, https://doi.org/10.1109/ 
ACCESS.2021.3117117.

[13] N.R. Beckham, L.J. Akeh, G.N.P. Mitaart, J.v. Moniaga, Determining factors that

affect student performance using various machine learning methods, Procedia 
Comput. Sci. 216 (2023) 597–603, https://doi.org/10.1016/j.procs.2022.12.174.
[14] J. Niyogisubizo, L. Liao, E. Nziyumva, E. Murwanashyaka, P.C. Nshimyumukiza, 
Predicting student’s dropout in university classes using two-layer ensemble 
machine learning approach: a novel stacked generalization, Comput. Educ. 3 
(2022) 100066, https://doi.org/10.1016/j.caeai.2022.100066.

[15] R. Ghorbani, R. Ghousi, Comparing different resampling methods in predicting 
students’ performance using machine learning techniques, IEEE Access 8 (2020) 
67899–67911, https://doi.org/10.1109/ACCESS.2020.2986809.

[16] F. Marbouti, J. Ulas, C.-H. Wang, Academic and demographic cluster analysis of 
engineering student success, IEEE Trans. Educ. 64 (3) (2021) 261–266, https://doi. 
org/10.1109/TE.2020.3036824.

[17] P. Xuan Lam, P.Q.H. Mai, Q.H. Nguyen, T. Pham, T.H.H. Nguyen, T.H Nguyen, 
Enhancing educational evaluation through predictive student assessment 
modeling, Comput. Educ. 6 (2024) 100244, https://doi.org/10.1016/J. 
CAEAI.2024.100244.

[18] A. Gonzalez-Nucamendi, J. Noguez, L. Neri, V. Robledo-Rella, R.M.G. García-

Castel´an, Predictive analytics study to determine undergraduate students at risk of 
dropout, Front. Educ. 8 (2023) 1244686, https://doi.org/10.3389/ 
FEDUC.2023.1244686.

[19] S. Alwarthan, N. Aslam, I.U. Khan, An explainable model for identifying at-risk

student at higher education, IEEE Access 10 (2022) 107649–107668, https://doi. 
org/10.1109/ACCESS.2022.3211070.

13

---

<!-- PAGE 14 -->

R.D. Dele˜na et al.

Systems and Soft Computing 7 (2025) 200352

[20] G. Feng, M. Fan, Y. Chen, Analysis and prediction of students’ academic

performance based on educational data mining, IEEE Access 10 (2022) 
19558–19571, https://doi.org/10.1109/ACCESS.2022.3151652.

[21] A.M. Mariano, A.B. de Magalh˜aes Lelis Ferreira, M.R. Santos, M.L. Castilho, A.C.F. 
L.C Bastos, Decision trees for predicting dropout in engineering course students in 
Brazil, Procedia Comput. Sci. 214 (2022) 1113–1120, https://doi.org/10.1016/j. 
procs.2022.11.285.

[22] H.P. Singh, H.N. Alhulail, Predicting student-teachers dropout risk and early

identification: a four-step logistic regression approach, IEEE Access 10 (2022) 
6470–6482, https://doi.org/10.1109/ACCESS.2022.3141992.

[23] F. Marbouti, J. Ulas, C.-H. Wang, Academic and demographic cluster analysis of 
engineering student success, IEEE Trans. Educ. 64 (3) (2021) 261–266, https://doi. 
org/10.1109/TE.2020.3036824.

[24] A. Nabil, M. Seyam, A. Abou-Elfetouh, Prediction of students’ academic

performance based on courses’ grades using deep neural networks, IEEE Access 9 
(2021) 140731–140746, https://doi.org/10.1109/ACCESS.2021.3119596.
[25] H. Prabowo, A.A. Hidayat, T.W. Cenggoro, R. Rahutomo, K. Purwandari,

B. Pardamean, Aggregating time series and tabular data in deep learning model for 
university students’ GPA prediction, IEEE Access 9 (2021) 87370–87377, https:// 
doi.org/10.1109/ACCESS.2021.3088152.

[26] C.F. Rodríguez-Hern´andez, M. Musso, E. Kyndt, E. Cascallar, Artificial neural 
networks in academic performance prediction: systematic implementation and 
predictor evaluation, Comput. Educ. 2 (2021) 100018, https://doi.org/10.1016/j. 
caeai.2021.100018.

[27] A.J. Fern´andez-García, R. Rodríguez-Echeverría, J.C. Preciado, J.M.C. Manzano,

F. S´anchez-Figueroa, Creating a recommender system to support higher education 
students in the subject enrollment decision, IEEE Access 8 (2020) 189069–189088, 
https://doi.org/10.1109/ACCESS.2020.3031572.

[28] H.A. Mengash, Using data mining techniques to predict student performance to 
support decision making in university admission systems, IEEE Access 8 (2020) 
55462–55470, https://doi.org/10.1109/ACCESS.2020.2981905.

[29] T.A. Cardona, E.A. Cudney, Predicting student retention using support vector 
machines, Procedia Manuf. 39 (2019) 1827–1833, https://doi.org/10.1016/J. 
PROMFG.2020.01.256.

[30] A. Viloria, J.G. Padilla, C. Vargas-Mercado, H. Hern´andez-Palma, N.O. Llinas, M. 
A. David, Integration of data technology for analyzing university dropout, Procedia 
Comput. Sci. 155 (2019) 569–574, https://doi.org/10.1016/j.procs.2019.08.079.

[31] G. Lesinski, S. Corns, Multi-objective evolutionary neural network to predict

graduation success at the United States military academy, Procedia Comput. Sci. 
140 (2018) 196–205, https://doi.org/10.1016/J.PROCS.2018.10.329.

[32] G. Lesinski, S. Corns, C. Dagli, Application of an artificial neural network to predict 
graduation success at the United States military academy, Procedia Comput. Sci. 95 
(2016) 375–382, https://doi.org/10.1016/J.PROCS.2016.09.348.

[33] M. Goga, S. Kuyoro, N. Goga, A recommender for improving the student academic 
performance, Procedia - Soc. Behav. Sci. 180 (2015) 1481–1488, https://doi.org/ 
10.1016/j.sbspro.2015.02.296.

[34] C. Schr¨oer, F. Kruse, J.M. G´omez, A systematic literature review on applying

CRISP-DM process model, Procedia Comput. Sci. 181 (2021) 526–534, https://doi. 
org/10.1016/J.PROCS.2021.01.199.

[40] A.M. Dur´an-Rosal, T. Ashley, J. P´erez-Rodríguez, F. Fern´andez-Navarro, Global and 
diverse ensemble model for regression, Neurocomputing 647 (2025) 130520, 
https://doi.org/10.1016/J.NEUCOM.2025.130520.

[41] R.E. Uhrig, Introduction to artificial neural networks, in: Proceedings of IECON ’95 
- 21st Annual Conference on IEEE Industrial Electronics 1, 2002, pp. 33–37, 
https://doi.org/10.1109/IECON.1995.483329.

[42] Accuracy, I.S.O., Of Measurement Methods and Results—Part 1: General principles

and Definitions, International Organization for Standardization, Geneva, 
Switzerland, 1994.

[43] D. Chicco, G. Jurman, The advantages of the Matthews correlation coefficient

(MCC) over F1 score and accuracy in binary classification evaluation, BMC Genom. 
21 (1) (2020) 1–13, https://doi.org/10.1186/S12864-019-6413-7/TABLES/5.
[44] N.J. Dia, J.C. Sieras, S.A. Khalid, A.H.T. Macatotong, J.M. Mondejar, E.R. Genotiva, 
R.D. Delena, EduGuard RetainX: an advanced analytical dashboard for predicting 
and improving student retention in tertiary education, SoftwareX 29 (2025) 
102057, https://doi.org/10.1016/j.softx.2025.102057.

[45] N. Dia, R. Delena, EduGuard RetainX: an Advanced Analytical Dashboard For

Predicting and Improving Student Retention in Tertiary Education (Version V1), 
CodeOcean, 2024. https://codeocean.com/capsule/2453835/tree/v1. 
</Dataset>.

[46] M. Mukaka, Statistics corner: a guide to appropriate use of correlation coefficient

in medical research, Malawi Med. J. 24 (3) (2012) 69–71.

[47] Setia, M. (2023, September 14). Log loss - logistic regression’s cost function for 
beginners. https://www.analyticsvidhya.com/blog/2020/11/binary-cross-entro 
pyaka-log-loss-the-cost-function-used-in-logistic-regression/.

[48] H. Babaei, M. Zamani, S. Mohammadi, The impact of data splitting methods on

machine learning models: a case study for predicting concrete workability, Mach. 
Learn. Comput. Sci. Eng. 1 (1) (2025), https://doi.org/10.1007/s44379-025- 
00021-3.

[49] Dey, S., Kumar, Y., Saha, S., & Basak, S. (2016). Forecasting to classification:

predicting the direction of stock market price using Xtreme gradient boosting. http 
s://doi.org/10.13140/RG.2.2.15294.48968.

[50] P. Carmona, F. Climent, A. Momparler, Predicting failure in the U.S. banking

sector: an extreme gradient boosting approach, Int. Rev. Econ. Finance 61 (2019) 
304–323, https://doi.org/10.1016/J.IREF.2018.03.008.

[51] I. Babajide Mustapha, F. Saeed, Bioactive molecule prediction using extreme 
gradient boosting, Molecules 21 (8) (2016), https://doi.org/10.3390/ 
MOLECULES21080983.

[52] Hanif, I. (2020). Implementing extreme gradient boosting (XGBoost) classifier to 
improve customer churn prediction. https://doi.org/10.4108/EAI.2-8-201 
9.2290338.

[53] M.F. Flayyih, H. Hassan TOUT, Predictive analytics model for students’ grade

prediction using machine learning. a review, EDRAAK 2023 (2023) 1–4, https:// 
doi.org/10.70470/EDRAAK/2023/001.

[54] C. Romero, S. Ventura, Educational data mining and learning analytics: an updated

survey, Wiley Interdiscip. Rev. Data Min. Knowl. Discov. 10 (3) (2020), https:// 
doi.org/10.1002/widm.1355.

[55] G. Siemens, P. Long, Penetrating the fog: analytics in learning and education, Educ.

Rev. 46 (5) (2011) 30. https://eric.ed.gov/?id=EJ950794.

[35] N. Caetano, P. Cortez, R.M.S. Laureano, Using data mining for prediction of

[56] B. Chahar, S.R. Jain, V. Hatwal, Mediating role of employee motivation for

hospital length of stay: an application of the CRISP-DM methodology, Lect. Notes 
Bus. Inf. Process. 227 (2015) 149–166, https://doi.org/10.1007/978-3-319-22348- 
3_9.

[36] Wirth, R., & Hipp, J. (2000). Crisp-dm: towards a standard process model for data

mining.

[37] V. Vijayalakshmi, K. Venkatachalapathy, Comparison of predicting student‘s

performance using machine learning algorithms, Int. J. Intell. Syst. Appl. 11 (12) 
(2019) 34–45, https://doi.org/10.5815/IJISA.2019.12.04.

[38] S. Hansun, J. Tanuwijaya, LQ45 stock index prediction using k-nearest neighbors 
regression, Int. J. Recent Technol. Eng. 8 (3) (2019) 2277–3878, https://doi.org/ 
10.35940/ijrte.C4663.098319 (IJRTE).

training, commitment, retention, and performance in higher education institutions, 
Probl. Perspect. Manag. 19 (3) (2021) 95–106, https://doi.org/10.21511/ppm.19 
(3).2021.09.

[57] N. Nithiyanandam, S. Dhanasekaran, A.S. Kumar, D. Gobinath, P. Vijayakarthik, G. 
V. Rajkumar, U. Muthuraman, Artificial intelligence assisted student learning and 
performance analysis using instructor evaluation model, in: 2022 3rd International 
Conference on Electronics and Sustainable Communication Systems (ICESC), 2022, 
pp. 1555–1561, https://doi.org/10.1109/icesc54411.2022.9885462.

[58] S. Xiao, A. Shanthini, D. Thilak, Instructor performance prediction model using

artificial intelligence for higher education systems, J. Interconnect. Netw. 22 
(Supp03) (2021), https://doi.org/10.1142/s0219265921440035.

[39] E. Osmanbegovic, M. Suljic, Data mining approach for predicting student

[59] N.Y. Hung, L. Lin, V.D. Calhoun, Deep P-Spline: theory, fast tuning, and

performance, J. Econ. Bus. 10 (1) (2012) 3–12. https://www.researchgate.net/ 
publication/242341193_DATA_MINING_APPROACH_FOR_PREDICTING_STUDE 
NT_PERFORMANCE.

application, arXiv (Cornell Univ.) (2025), https://doi.org/10.48550/ 
arxiv.2501.01376.

[60] L. Lin, V.R. Joseph, Transformation and additivity in gaussian processes, 
Technometrics 62 (4) (2019) 525–535, https://doi.org/10.1080/ 
00401706.2019.1665592.

14

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Systems and Soft Computing 7 (2025) 200352
Contents lists available at ScienceDirect
Systems and Soft Computing
journal homepage: www.journals.elsevier.com/soft-computing-letters
Predicting student retention: A comparative study of machine learning
approach utilizing sociodemographic and academic factors
Reymark D. Delen ˜ aa,* , Nornin ˜ a J. Diab, Redeemtor R. Sacayanc, Joseph C. Sierasb,
Suhaina A. Khalidb, Amer Hussien T. Macatotongb, Sacaria B. Gulamd
aFaculty, Department of Information Technology, College of Computer Studies, Mindanao State University – Iligan Institute of Technology, Iligan City 9200, Philippines
bFaculty, Department of Information Sciences, College of Information and Computing Sciences, Mindanao State University – Main Campus, Marawi City, Lanao Del Sur,
9700, Philippines
cFaculty, Department of Mathematics and Statistics, College of Science and Mathematics, Mindanao State University-Iligan Institute of Technology, Iligan City 9200,
Philippines
dFaculty, Department of Computing Sciences, College of Information and Computing Sciences, Mindanao State University – Main Campus, Marawi City, Lanao Del Sur,
9700, Philippines
A R T I C L E I N F O A B S T R A C T
Keywords: Student dropout remains a persistent challenge in higher education, particularly in developing regions where
Student retention institutional resources for intervention are limited. This study explores the predictive potential of machine
Educational data mining learning (ML) algorithms in identifying students at risk of dropping out using historical academic and socio-
Machine learning algorithms demographic data from Mindanao State University–Main Campus, covering a ten-year period (2012–2022). A
Data visualization
total of 482 student records and 146 variables were preprocessed using Power BI and prepared via the CRISP-DM
Higher Education Analytics
Data-driven Education methodology before being modeled in Jupyter Notebook. Ten ML algorithms such asExtreme Gradient Boosting
Sociodemographic Factors (XGBoost), Gradient Boosting (GB), Artificial Neural Network (ANN), Decision Tree (DT), Random Forest (RF),
Academic Factors Multilayer Perceptron (MLP), Logistic Regression (LR), K-Nearest Neighbor (KNN), Support Vector Machine
eXtreme Gradient Boosting (SVM), and Naïve Bayes (NB) were evaluated using both train-test split and 5-fold cross-validation to ensure
robustness and generalizability. Results indicate that XGBoost outperformed all other models, achieving the
highest cross-validated accuracy (90.66 %), F1 Score (90.72), and one of the lowest error values (Mean Square
Error (MSE) =9.34, Log Loss =0.26). GB and ANN followed closely, demonstrating strong balance between
precision, recall, and low misclassification rates. While models like Naïve Bayes recorded high recall, they also
produced excessive false positives, limiting their practical use. The study offers a scalable and transferable
modeling framework for higher education institutions seeking to implement early warning systems. It also
emphasizes the pedagogical value of integrating educational data science into Information Technology Education
(ITE) curricula to foster real-world AI application. Limitations and future directions are discussed, particularly
regarding behavioral data integration and model interpretability.
1. Introduction and infrastructure limitations. A wide range of factors contribute to a
student’s decision to withdraw from a program, but academic perfor-
Student attrition in university settings has long been a pressing mance and sociodemographic characteristics remain the most frequently
concern among educators and administrators, as it significantly affects examined variables in retention studies [3,4].
institutional rankings, reputation, workforce readiness, and financial In response to this challenge, Educational Data Mining (EDM) has
sustainability [1,2]. Globally, high dropout rates are associated with emerged as a key area within educational research, focusing on the
wasted educational resources, decreased graduation outputs, and application of machine learning techniques to institutional data in order
weakened national educational goals. In many developing and under- to predict student outcomes and inform strategic interventions [5].
represented contexts, particularly in Southeast Asia, challenges related Numerous studies have established that academic records and de-
to academic persistence are compounded by socioeconomic disparities mographic profiles are strong indicators of student persistence or risk of
* Corresponding author.
E-mail address: reymark.delena@g.msuiit.edu.ph(R.D. Delen˜a).
https://doi.org/10.1016/j.sasc.2025.200352
Received 14 July 2024; Received in revised form 15 June 2025; Accepted 14 July 2025
Available online 18 July 2025
2772-9419/© 2025 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/) .

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
dropout [3,4,6]. The integration of EDM and machine learning into systematic benchmarking. In contrast, this study addresses these gaps by
university systems allows institutions—both locally and globally—to employing ten ML models evaluated using six performance metrics such
analyze historical student data to identify learning gaps, anticipate ac- as Accuracy, F1 Score, Precision, Recall, Mean Squared Error (MSE), log
ademic failures, and predict future academic trajectories [7]. These loss, and by conducting a thorough review to identify the most relevant
predictive insights can guide data-informed decisions aimed at data inputs and modeling strategies.
improving institutional effectiveness and creating supportive learning Ultimately, the goal of this research is not only to achieve high
environments [8], ultimately helping students stay on track toward predictive performance but also to provide actionable insights that
timely graduation. inform institutional policy, guide academic interventions, and support
The College of Information and Computing Sciences (CICS) of program-level strategies to reduce student attrition and improve timely
Mindanao State University – Main Campus has one of the highest graduation rates. By contributing findings from a region with limited
attrition rates within the university, which piqued the researcher’s in- representation in literature, this study aims to support more inclusive
terest in this subject matter. However, the significance of this research and globally relevant approaches to student success analytics.
extends far beyond the boundaries of one institution. As higher educa-
tion institutions worldwide contend with increased student diversity, 2. Material and methods
massification of enrollment, and post-pandemic educational disruptions,
the ability to accurately model and address student attrition becomes a In conducting the study, secondary data of CICS students was
global imperative. Retention metrics are now pivotal not just for insti- sourced from the Information and Communication Technology Center
tutional planning but also for national education performance bench- (ICTC), following the guidelines established by the Preferred Reporting
marks, accreditation compliance, and international university rankings. Items for Systematic Reviews and Meta-Analyses (PRISMA). The data
Moreover, diversity and inclusion goals, particularly disaggregated underwent the CRISP-DM process. First, an in-depth analysis of the
retention statistics by gender, socio-economic status, and ethnicity, have business objectives and needs was done. Next, the quality of gathered
gained prominence as critical indicators of how well institutions support data was examined and cleaned. Subsequently, the data was organized
marginalized student populations. These data-driven approaches offer for modeling. Ten (10) data modeling techniques were applied to predict
powerful tools to inform not only curriculum design and student services the outcomes which were then evaluated using six (6) evaluation met-
but also equitable resource distribution and strategic policy develop- rics to identify the optimal model that provides the most accurate
ment. On a global scale, retention and graduation rates are among the results.
most scrutinized indicators by ranking bodies and education quality
assurance agencies, making predictive analytics in this domain both
timely and globally significant. 2.1. Systematic review
Recent studies apply diverse predictive models for predicting aca-
demic performance, graduation, and dropout [9], enabled by the 2.1.1. Data collection and extraction
increasing availability of institutional datasets. As model performance For the systematic review, two (2) journal databases were used to
depends heavily on dataset quality and size [10], large-scale research find the recent and relevant articles necessary to conduct the systematic
such as that by Alhazmi & Sheneamer [11] (275,000 students) and review. To find the relevant papers, the researcher used the keywords
Rodríguez-Hern´andez et al. [12] (162,030 students) reinforces the “Data mining” AND “Student retention” OR “Student performance” in
reliability of data-driven modeling. Several others, Beckham et al. [13], Science Direct and “Predicting student retention” + “data mining” in
Niyogisubizo et al. [14], Ghorbani & Ghousi [15], Marbouti et al. [16], IEEE Xplore. Furthermore, the search was filtered to restrict the publi-
Lam et al. [17], and Gonzalez-Nucamendi et al. [18], explore the pre- cation year between 2013 and 2023 spanning ten (10) years; this was to
dictive power of various machine learning models, including hybrid and ensure that all selected papers are relevant and up to date. The query
ensemble approaches, in student dropout forecasting across countries resulted in a total of 364 journals (see Table 1). Subsequently, MS Excel
such as Portugal, Colombia, Iran, and Mexico. These global efforts un- was used to organize, sort, and eliminate duplicates from the retrieved
derscore the importance of localized yet scalable modeling approaches, data set
especially for contexts with high dropout risk but low representation in
existing literature. 2.1.2. PRISMA model
This study makes several key contributions to the field of student In this process as illustrated in Fig. 1, 336 records were excluded in
retention analytics. First, it integrates a comprehensive set of socio- the screening process due to its irrelevancy based on their title and ab-
demographic and academic variables to develop predictive models for stract. The remaining articles were then assessed for eligibility based on
student retention within the context of a state university in the the criteria listed in Table 2 by reviewing them in full text, and this
Philippines, an underrepresented setting in existing literature. Second, it assessment retained 21 studies listed in Table 3.
conducts a rigorous comparative evaluation of ten (10) widely adopted
machine learning (ML) algorithms, identifying Extreme Gradient 2.1.3. Key findings
Boosting (XGBoost) as the most accurate across multiple standardized Fig. 2a illustrates the frequency with which various sociodemo-
metrics. Third, the study leverages actual student data spanning a full graphic factors were utilized across a set of studies. The data reveals that
decade (2012–2022) from the College of Information and Computing gender (9 studies) was the most frequently used factor, followed closely
Sciences (CICS) at Mindanao State University–Main Campus, encom- by marital status (8 studies) and age (7 studies). These results suggest
passing its Computer Science, Information Technology, and Information that these variables are considered highly relevant in research exploring
Systems programs. This longitudinal dataset enables deeper insights into
student behavior and retention trends over time, supporting more Table 1
effective early intervention strategies. Databases and keywords used.
The novelty of this research lies in its context-specific focus, breadth
No. Database URL Retrieved
of model comparison, and practical implementation using institutional Papers
data visualized through Python in a Jupyter Notebook environment.
1 Elseiver (Science https://www.sciencedirect. 277
While the effectiveness of ML in predicting student performance is well- Direct) com/
established, much of the existing literature relies on short-term datasets, 2 IEEE Xplore Digital https://www.ieeexplore.ieee. 87
simulated environments, or limited algorithm selection. Some studies Library org/
​ ​ Total 364
also emphasize hybrid model development without conducting
2

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
Fig. 1. PRISMA flow diagram illustrating the systematic review process for the selection of studies related to data mining and student retention/performance.
Other academic factors with moderate usage include admission test
Table 2 score (n =4), dropout status (n =3), and high school GPA and year level
Inclusion and exclusion criteria. (n =3 each). Several variables such as enrollment status, student clas-
No. Inclusion Criteria Exclusion Criteria sification, socioemotional support, transfer status, and middle school
1 Using algorithms to predict student Studies not utilizing predictive performance were only used in one or two studies, indicating lower
retention analytics prevalence or relevance depending on the study’s objectives. Moreover,
2 Articles between 2013 and 2023 Articles older than 2013 the variety in factor usage suggests that while some indicators like
3 Sample population is college Sample population other than college
grades and graduation timelines are central to academic studies, others
students students
4 Journal, Conference, Thesis/ Review articles, book chapters, etc. are context-dependent and possibly underexplored. This also highlights
Dissertation an opportunity to investigate the value of less commonly used academic
5 Written in English Language Not written in English Language variables in future predictive or evaluative studies.
6 Open access Paid Fig. 2c shows the frequency of usage of various machine learning
(ML) models in the studies, distinguishing between supervised and un-
social or behavioral outcomes. Other moderately used factors include supervised learning methods. It is evident that Decision Tree (n =8),
parent’s occupation (4 studies), family size and financial support (3 Multilayer Perceptron (MLP) (n = 8), and Support Vector Machine
studies each), and guardian and parent’s education/qualification (2 (SVM) (n = 8) are the most widely used supervised learning models,
studies each). Several factors, such as address, family responsibilities, reflecting their popularity due to interpretability, accuracy, and
religious affiliation, parent’s school issues, school, travel time to school, robustness in classification tasks. Other frequently applied models
and working status, were only used in a single study, indicating limited include Logistic Regression (n =6) and K-Nearest Neighbor (KNN) (n =
application or relevance in most contexts analyzed. Further, this varia- 5). These classical models are still highly valued for their simplicity and
tion in usage frequency highlights a trend in which basic demographic effectiveness. Less frequently used models, each appearing in just one
variables like gender, age, and marital status are prioritized, possibly study, include Bayesian Network, Extreme Gradient Boosting (XGBoost),
due to their availability, perceived impact, or ease of interpretation in and Long Short-Term Memory (LSTM), among others. Notably, only a
predictive modeling and statistical analyses. few models were classified under unsupervised learning (in gray), such
On the other hand, Fig. 2b depicts presents the frequency with which as K-Means Clustering (n =2) and J48/JRip, indicating a predominant
specific academic-related variables were included across different focus on supervised techniques in the reviewed studies. This highlights a
research studies. The most used academic factor was expected gradua- potential research gap where unsupervised or hybrid learning ap-
tion year (n =8), followed by grades or GPA (n =7) and project grades proaches could be further explored.
(n =7). These variables likely reflect students’ academic performance Fig. 2d illustrates the frequency of various evaluation metrics used
and trajectory, making them strong predictors in educational analytics. across studies related to predictive modeling. Accuracy emerges as the
3

R.D. Delen˜a et al.                                                                                                                                                                                          S  y  s t e  m  s    a n  d    S  o f  t   C  o m   p  u  t ing 7 (2025) 200352
Table 3
Eligible articles that employ data mining on student retention.
No. Author Year Article Prediction Goal Dataset  No. of  Algorithm  Ref.
|     |     |     | Size | Variables (s) |     |
| --- | --- | --- | ---- | ------------- | --- |
1 (Alhazmi &  2023 Early predicting of student performance in higher  Student’s performance (CGPA) 275,000 16 XGBoost, LR,  [11]
| Sheneamer) | education |     |     | SVM, KNN, RF |     |
| ---------- | --------- | --- | --- | ------------ | --- |
2 (Beckham et al.) 2023 Determining factors that affect student performance  Factors affecting student  395 13 MLP, DT, RF [13]
|     | using various machine learning method | performance (Correlation Score) |     |     |     |
| --- | ------------------------------------- | ------------------------------- | --- | --- | --- |
3 (Alwarthan et al.) 2022 An explainable model for identifying at-risk student at  At-risk Students (CGPA) N/A 7 RF, ANN, SVM [19]
higher education
|                 | Analysis and prediction of students’ academic  | Student’s performance (Poor,  |     |            |      |
| --------------- | ---------------------------------------------- | ----------------------------- | --- | ---------- | ---- |
| 4 (Feng et al.) | 2022                                           |                               | N/A | 1 K-means  | [20] |
performance based on education data mining Good, Excellent) Clustering
5 (Mariano et al.) 2022 Decision trees for predicting dropout in Engineering  Factors affecting student  91 2 DT [21]
|     | Course students in Brazil | performance (Correlation score),  |     |     |     |
| --- | ------------------------- | --------------------------------- | --- | --- | --- |
and Dropout rate
6 (Niyogisubizo  2022 Predicting student’s dropout in university classes using  Student dropout (Dropout or  216 8 RF, XGBoost, GB,  [14]
et al.) two-layer ensemble machine learning approach: A  Non-dropout) FNN
novel stacked generalization
7 (Singh et al.) 2022 Predicting student-teachers dropout risk and early  At-risk Students (Dropout or  1723 8 LR [22]
|     | identification: A four-step logistic regression approach | Non-dropout) |     |     |     |
| --- | -------------------------------------------------------- | ------------ | --- | --- | --- |
8 (Marbouti et al.) 2021 Academic and demographic cluster analysis of  Factors affecting student  12,053 10 K-means  [23]
|     | engineering student success | performance (P-Value) |     | clustering |     |
| --- | --------------------------- | --------------------- | --- | ---------- | --- |
9 (Nabil et al.) 2021 Prediction of Students’ Academic Performance Based  Student’s performance (Pass or  4266 1 DNN, DT, RF, GB,  [24]
on Courses’ Grades Using Deep Neural Networks Fail) LR, SVC, KNN
Student’s performance (GPA)
10 (Prabowo et al.) 2021 Aggregating time series and tabular data in deep  46,670 7 MLP, LSTM [25]
learning model for university students’ GPA prediction
11 (Rodríguez-  2021 Artificial neural networks in academic performance  Student’s performance (Level to  16,2030 11 MLP [26]
| Hernandez et al.) | prediction: Systematic implementation and predictor  | Level 4) |     |     |     |
| ----------------- | ---------------------------------------------------- | -------- | --- | --- | --- |
evaluation
12 (Uliyan et al.) 2021 Student retention (retention rate) GPA, Subjects’ grades 2949 2 BLSTM, CRF [12]
13 (Ferna´ndez-García  2020 Creating a recommender system to support higher  Student’s performance (Pass or  6948 14 RF, LR, DT, SVM,  [27]
et al.) education students in the subject enrollment decision Fail) KNN, MLP, GB
14 (Ghorbani &  2020 Comparing different resampling methods in predicting  Algorithm Performance (Model  650 19 RF, KNN, ANN,  [15]
Ghousi) students’ performance using machine learning  Accuracy Scores) XGBoost, SVM,
|     | techniques |     |     | DT, LR, NB |     |
| --- | ---------- | --- | --- | ---------- | --- |
Student’s performance
15 (Mengash) 2020 Using data mining techniques to predict student  2039 2 ANN, DT, SVM,  [28]
performance to support decision making in university  (Excellent, Very Good, Good,  NB
|     | admission systems | Acceptable, Poor) |     |     |     |
| --- | ----------------- | ----------------- | --- | --- | --- |
(Cardona &
16 2019 Predicting Student Retention Using Support Vector  Algorithm performance (Model  904 6 SVM [29]
| Cudney) | Machines | accuracy score) |     |     |     |
| ------- | -------- | --------------- | --- | --- | --- |
17 (Viloria et al.) 2019 Integration of data technology for analyzing university  Student dropout (Dropout or  19,300 4 Bayesian  [30]
|     | dropout | Non-dropout) |     | Network, DT, NN |     |
| --- | ------- | ------------ | --- | --------------- | --- |
(Lesinski & Corns)
18 2018 Multi-objective evolutionary neural network to predict  Graduation Status (Graduates,  5100 7 MLP, MOEA [31]
|     | graduation success at the United States Military  | Late Graduates, Non-graduates) |     |     |     |
| --- | ------------------------------------------------- | ------------------------------ | --- | --- | --- |
Academy
19 (Lesinski, et al.) 2016 Application of an Artificial Neural Network to Predict  Graduation Status (Graduates,  5100 7 MLP [32]
|     | Graduation Success at the United States Military  | Late graduates, Non-graduates) |     |     |     |
| --- | ------------------------------------------------- | ------------------------------ | --- | --- | --- |
Academy
20 (Marbouti et al.) 2016 Models for early prediction of at-risk students in a  At-risk Students (Pass or Fail) 1600 5 NB Classifier,  [16]
|     | course using standards-based grading |     |     | SVM, KNN, LR,  |     |
| --- | ------------------------------------ | --- | --- | -------------- | --- |
DT, MLP
21 (Goga et al.) 2015 A recommender for improving the student academic  Student’s performance (GPA) 7500 10 RF, Random Tree,  [33]
|     | performance |     |     | J48, Decision  |     |
| --- | ----------- | --- | --- | -------------- | --- |
Stump, REPTree,
JRip, OneR,
ZeroR, PART,
Decision Table,
MLP
most employed metric, reported in 13 studies, highlighting its popu- academic prediction models, pointing to a need for more consistent use
larity due to its simplicity and intuitive interpretation. Following  of varied and task-appropriate evaluation metrics to ensure balanced
closely, F1 Score, Precision, and Recall are each used in 11 studies.  model assessment.
These three metrics are especially important in imbalanced datasets
where focusing solely on accuracy could be misleading. Other metrics
2.2. CRISP-DM
such as MSE (used in 2 studies) and a range of others (each used once) —
including ROC curve, R2, AUC, MAE, and RMSE — suggest that while
diversity exists in evaluation practices, there is a clear concentration  The Cross-Industry Standard Process for Data Mining (CRISP-DM)
around a few key indicators. This trend may reflect a preference for  (Fig. 3) is widely adopted, industry - independent process model for data
metrics that balance interpretability with robustness, especially in  mining, extensively used in both practical applications and in research
classification tasks. Interestingly, statistical tests like the Hosmer &  [34]. This cycle is composed of six phases: (1) Business Understanding
Lemeshow test, Wald test, and Likelihood Ratio Test, though rarely used  which focuses on the understanding of the project objectives and re-
quirements from a business perspective; (2) Data Understanding or
(only once each), indicate occasional application of inferential statistical
determining the data to be collected and discovering insights from it; (3)
methods to complement predictive accuracy. This distribution provides
Data Preparation which encompasses all activities that result in the final
insight into how performance is validated in student retention and
dataset; (4) Modeling, where various modeling techniques are chosen
4

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
Fig. 2. Comprehensive summary of factors, models, and evaluation metrics used in student retention prediction studies. (a) Sociodemographic factors frequently
included in predictive models, with gender, parent’s educational attainment, and age among the most cited attributes. (b) Academic factors considered in prior
studies, where high school GPA, failed courses, and dropout status were the most prominent predictors. (c) Machine learning models used in the literature, showing
that decision tree, random forest, support vector machine (SVM), and multilayer perceptron (MLP) are the most employed, all of which fall under supervised
learning. (d) Evaluation metrics applied in model assessment. Accuracy was the most frequently used metric, followed by F1 score, precision, and recall, reflecting a
focus on classification performance in most studies.
5

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
Fig. 2. (continued).
6

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
selected were tested by setting the X and Y variables, then dividing the
dataset into training and testing data. After that, the models were built
for prediction using the test data.
In the evaluation stage, the algorithms were tested using the selected
six (6) evaluation metrics to calculate the accuracy of the predicted
values. The model with highest accuracy rate was the algorithm
deployed for the final prediction of student’s probability rate of
withdrawal.
2.3. Machine learning algorithms
In predictive analytics, ML algorithms are essential tools for identi-
fying trends and patterns in educational data, particularly in modeling
student retention. These algorithms must first be trained on historical
data to ensure accurate predictions and can be categorized into classi-
fication, ensemble, and neural network models. Classification algo-
rithms such as SVM [37], Logistic Regression [22], KNN [38], Naïve
Bayes [39], and Decision Tree [37] are widely used to label students as
either at risk or likely to persist, each with varying assumptions and
sensitivities to educational data structures. SVM and LR assume Inde-
Fig. 3. The CRISP-DM (cross-industry standard process for data mining)
pendent and Identically Distributed (IID) data, though LR can be
methodology adopted in this study [44]. The framework consists of six iterative
adapted using generalized estimating equations (GEE) to account for
phases: business understanding, data understanding, data preparation,
clustered errors. KNN is a non-parametric model sensitive to de-
modeling, evaluation, and deployment. This cyclic approach ensured that the
mographic clustering, while Naïve Bayes, despite its strong indepen-
predictive modeling process remained aligned with institutional goals, data
quality, and model performance throughout the project. dence assumption, remains useful in large datasets when paired with
feature selection. Decision Trees are intuitive and flexible but prone to
overfitting without pruning. Ensemble models like Random Forest and
and applied, and their parameters are calibrated to optimal values; and
Gradient Boosting [14] combine multiple learners to improve accuracy
(5) Evaluation, where algorithms are tested to find the optimal model
and generalization [18], with Random Forest offering simplicity, short
[35,36].
Higher Education Institutions (HEIs) suffer intensely from students’ training time, and improved forecasting accuracy, albeit with increased
model complexity as more trees are added [19]. XGBoost, an optimized
withdrawal as they are highly interested and invested in producing
implementation of gradient boosting, has emerged as a leading model
competent students which could positively affect their reputation in the
due to its speed, built-in regularization, early stopping, and ability to
market. The College of Information and Computing Sciences (CICS) in
handle structured and nested data using parameters such as “group”
MSU-Main Campus is not an exemption as most of the enrolled students
[14]. The heterogeneity among ensemble learners helps mitigate bias
took 5 years or more to pass and complete the program (shown in Fig. 4).
Seemingly, half of the overall population from A.Y. 2012–2022 opted to and variance, making them robust in handling diverse student profiles
[40].
withdraw from the course and shift to other college to graduate early.
Moreover, Neural network models are powerful algorithms inspired
Therefore, having a strong understanding of the business aspects related
by the structure and function of the human brain. They process data
to student retention is essential for educational leaders and
through interconnected layers of artificial neurons, enabling the
administrators.
learning of non-linear relationships and adaptive weight adjustments.
For data preparation stage, the data gathered from the Information
These models are particularly effective for complex prediction tasks in
and Communication Technology Center (ICTC) through the permission
EDM environments [41]. One common variant is the ANN, which con-
of the Office of the Vice Chancellor for Academic Affairs (OVCAA) of the
sists of an input layer, one or more hidden layers, and an output layer.
Mindanao State University-Marawi (MSU-Main Campus) was inspected
Each artificial neuron receives inputs, computes weighted sums, applies
and cleaned where data was corrected, and null and erroneous values
activation functions, and passes outputs to the next layer. During
were imputed with zero (0). The multiple files were then integrated in a
training, these weights are adjusted iteratively to minimize prediction
single file. Afterwards, the categorical data was transformed into nu-
error. ANNs are widely applied in EDM because they can model intricate
merical to perform the data analysis without difficulty, and the unnec-
relationships between variables, even with small datasets, and capture
essary attributes and period were excluded in the final dataset that was
subtle patterns in student data [28]. While standard ANN architectures
fed into the models used.
assume IID data, educational datasets often include correlated or nested
In the modeling stage, the ten (10) machine learning algorithms
structures. To address this, methods such as recurrent architectures for
time-series data and dropout layers for regularization are frequently
used. Another variant, the MLP, expands on the ANN by incorporating
multiple hidden layers, enabling deeper representation learning. An
MLP typically includes an input layer for features, one or more hidden
layers for transformation, and an output layer that produces classifica-
tion or regression outputs. MLPs are particularly useful for solving
prediction tasks related to academic performance and retention [26].
Like other neural models, MLPs assume IID inputs, and thus pre-
processing steps such as batch normalization or the integration of
institutional-level variables are recommended when working with hi-
erarchical educational data.
Fig. 4. Distribution of student academic status in the dataset.
7

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
2.4. Evaluation metrics demographic background, and socio-economic context. These attributes
serve as predictive inputs for modeling student retention outcomes, with
To assess the performance of the machine learning models used in the DROPOUT variable encoded as a binary target (0 =retained, 1 =
this study, six evaluation metrics were employed: Accuracy, Precision, withdrawn).
Recall, F1 Score, MSE, and log loss. Accuracy measures the proportion of The dataset is entirely complete, containing no missing values, which
correctly predicted instances, both positive and negative, relative to the enhances its integrity for robust machine learning applications. The
total number of predictions, offering a general sense of model perfor- feature set is composed of two primary categories: (1) sociodemographic
mance, especially in balanced datasets [42]. Precision quantifies the attributes, such as AGE, SEX, CITY, PROVINCE, CIVILSTATUS, MOTH-
number of correctly predicted positive cases out of all instances pre- ERINCOME, and FATHERINCOME, which provide insight into the stu-
dicted as positive, thereby reflecting the model’s ability to minimize dents’ geographic and economic contexts; (2) academic attributes,
false positives. In contrast, Recall, or sensitivity, evaluates the model’s encompassing raw or normalized performance indicators derived from
capacity to identify all relevant positive instances, making it crucial in institutional grading systems—examples include PED001 to PED012,
contexts where missing at-risk students has significant consequences. STT071, and STT101, which likely correspond to core and technical
The F1 Score, which is the harmonic mean of Precision and Recall, courses specified in the university’s prospectus; and (3) program-
provides a balanced assessment when there is a trade-off between the specific variables, such as PROGRAM, YEARLEVEL, and COURSE HIS-
two, and is especially useful in handling imbalanced educational data TORY, capturing progression within the prescribed BSIT-D track.
[43]. Moreover, MSE is applied to measure the average squared differ- These academic features reflect the learning milestones embedded in
ence between actual and predicted values in regression-based outputs, the ITE curriculum, such as basic computer programming subjects,
with lower values indicating more accurate models. Lastly, the log loss, mathematics, probability and statistics for computing, data structures.
used to evaluate the performance of probabilistic classification where and advanced database systems. Many of the performance variables are
lower log loss indicates better performance. These metrics together likely derived from institutional logs and standardized academic met-
enable a comprehensive evaluation of classification and regression rics, normalized within a [0,1] scale, allowing for effective comparison
performance in predicting student retention outcomes. across subjects and semesters. The inclusion of longitudinal academic
indicators and technical subject coverage enables the model to capture
2.5. Modeling setup performance trends critical to predicting attrition.
Furthermore, the dataset’s balanced class distribution (approxi-
All machine learning models were implemented using Python 3.10 in mately 50 % dropout, 50 % retained) supports fair model training and
a Jupyter Notebook environment. The following libraries were used: evaluation without the need for resampling or synthetic balancing. The
pandas for data preprocessing, scikit-learn for model training and presence of highly granular features, such as course-level assessments
evaluation, xgboost for gradient boosting implementation, and mat- and regional identifiers, adds dimensional richness to the analysis,
plotlib/seaborn for visualization. To ensure robustness in model evalu- enabling the exploration of intersectional retention risks (e.g., by
ation, a 5-fold cross-validation approach was adopted using KFold from geographic origin or year level).
the scikit-learn library. This method randomly splits the dataset into five This dataset exemplifies the growing intersection between academic
equally sized folds. For each iteration, four folds were used to train the analytics and educational data mining in the Philippine higher educa-
model while the remaining fold was used for validation. This process tion landscape. It offers a rare opportunity to apply machine learning
was repeated five times so that each data point served as a validation models to real-world academic data with direct implications for insti-
sample once. The use of cross-validation reduces the likelihood of tutional policy, early warning systems, and student support in-
overfitting and ensures the generalizability of results. Hyperparameter terventions. By aligning variable design with curriculum structure and
tuning was done manually for transparency, and all models were eval- institutional reporting systems, the dataset ensures both contextual
uated using the six standard metrics described in Section 2.4. No relevance and technical rigor for predictive modeling of student reten-
mathematical derivations were included, as this study focuses on the tion and also was reportedly used by this study [44]. The dataset is
applied implementation of machine learning for institutional decision openly available for public access through CodeOcean [45].
support in student retention.
3. Results
2.6. Dataset description
This section presents the results of machine learning model assess-
The dataset utilized in this study comprises 482 anonymized student ments conducted on historical data collected over a decade (2012–2022)
records drawn from the Information Technology Education (ITE) pro- from the Information and Communication Technology Center (ICTC) of
gram at Mindanao State University – Main Campus across curriculum Mindanao State University-Main Campus. The data underwent pre-
(see Table 4). It contains 146 variables, meticulously curated to repre- processing in Power BI using the CRISP-DM methodology before being
sent a comprehensive view of each student’s academic journey, imported into Jupyter Notebook for further analysis. Subsequently, the
dataset was partitioned into X (independent variables) and Y (dependent
Table 4 variables) and split into training (70 %) and testing (30 %) sets. During
Summary of dataset characteristics for student retention modeling. analysis, variables highly correlated with the dependent variable were
identified through Spearman coefficient (ρ or rho) in correlation analysis
Characteristic Description
(Table 5) and subsequently removed to avoid multicollinearity,
Sample size (records) 482 student records
Number of features 146 total variables
Dropout rate 50.2 % (242 students)
Retention rate 49.8 % (240 students) Table 5
Missing values None (dataset is 100 % complete) Rule of thumb or interpretation of Spearman’s correlation value [46].
Feature categories ​
• Sociodemographic Age, Sex, Province, City, Civil Status, Parent’s Income Size of correlation Interpretation
• Academic Course grades (e.g., CCC, ITE, STT, MAT subjects), ±.90 to ±1.0 Very high positive/negative correlation
Performance normalized on a [0,1] scale ±.70 to ±.90 High positive/negative correlation
• Program Progression Year Level, Program Code, Total Units Earned, Course ±.50 to ±.70 Moderate positive/negative correlation
History ±.30 to ±.50 Low positive/negative correlation
• Target Variable DROPOUT (binary: 0 =retained, 1 =withdrawn) .00 to ±.30 Negligible correlation
8

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
Fig. 5. Number of actual and correct prediciton comparison.
resulting in the retainment of 79 columns out of the initial 134. See negatives (dropouts misclassified as non-dropouts), and 69 true nega-
Appendix A for the code of removing multicollinearity. tives (correctly identified non-dropouts). These results indicate that
Fig. 5illustrates the number of actual and correctly predicted results XGBoost achieved the highest overall classification accuracy across both
by the ten (10) machine learning algorithms. Results indicate that dropout and retention classes. As a reference, in the standard confusion
among the evaluated models, the XgBoost algorithm achieves the matrix layout, the top-left cell represents true positives, top-right in-
highest accuracy, correctly predicting 136 instances when compared to dicates false positives, bottom-left corresponds to false negatives, and
the actual y-values in the test dataset. This performance is then followed bottom-right denotes true negatives.
by the GB and Decision Tree (DT) models, which correctly predicted 134 Close behind XGBoost were the GB and ANN models, both of which
and 131 instances, respectively, out of a total of 145. Further, the sample exhibited strong and balanced predictive performance. The GB model
code used to assess the prediction accuracy of XgBoost is listed in Ap- yielded 66 true positives, 6 false positives, 5 false negatives, and 68 true
pendix B. A confusion matrix was also created to quantify correct pre- negatives, indicating a high degree of precision and recall. The ANN
dictions for the y-values (Dropout or Non-dropout). model achieved 60 true positives, 12 false positives, 5 false negatives,
On the other hand, Fig. 6presents the confusion matrices for each and 68 true negatives. Although both models performed well, they
classification model, while Table 6provides a comparative summary of incurred slightly higher misclassification rates compared to XGBoost.
their predictive performance in identifying student dropout. Among the Nevertheless, GB and ANN demonstrated commendable levels of sensi-
evaluated models, XGBoost demonstrated the most robust classification tivity (recall of actual dropouts) and specificity (correct identification of
capability, achieving 67 true positives (correctly identified dropouts), 5 non-dropouts), supporting their utility in retention-related prediction
false positives (non-dropouts misclassified as dropouts), 4 false tasks.
Fig. 6. Confusion matrix summary for each machine learning model.
9

R.D. Delen˜a et al.                                                                                                                                                                                          S  y  s t e  m  s    a n  d    S  o f  t   C  o m   p  u  t ing 7 (2025) 200352
Table 6  provides a more nuanced view of each model’s performance. While
Confusion matrix components and dropout detection rates of machine learning  traditional classification metrics suggest strong outcomes, the error
models. metrics, particularly Log Loss, highlight how well each model estimates
Model True  False  False  True  Dropout  class probabilities. A lower Log Loss indicates that the model is not only
Positive  Negative  Positive  Negatives  Detection  predicting correctly but is also confident and accurate in its probability
| (Correct  | (Missed  (False  | (Correct  Rate (TPR /  |     |     |     |     |
| --------- | ---------------- | ---------------------- | --- | --- | --- | --- |
estimates [47]. In this context, XGBoost and Gradient Boosting are
| Dropout) | Dropout) Dropout) | Not  Recall) |     |     |     |     |
| -------- | ----------------- | ------------ | --- | --- | --- | --- |
shown to be not just accurate, but also well-calibrated.
Dropout)
However, these results are derived from a single train-test split,
| SVM 61 | 12 17 | 55 61 /  |     |     |     |     |
| ------ | ----- | -------- | --- | --- | --- | --- |
which may be subject to sampling bias and overfitting, especially in
(61+12) =
datasets with class imbalance or limited size [48]. The observed per-
0.836
64 / (64+9)  formance could therefore be overly optimistic. As such, further valida-
| RF 64 | 9 8 | 64  |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
=0.877 tion using K-Fold cross-validation was performed and is discussed in the
MLP 66 7 9 63 66 / (66+7)  succeeding section to assess the stability and generalizability of these
=0.904
models.
| DT 67 | 6 8 | 64 67 / (67+6)  |                                                                      |     |     |     |
| ----- | --- | --------------- | -------------------------------------------------------------------- | --- | --- | --- |
|       |     | =0.918          | To address this, 5-fold cross-validation was applied to each model,  |     |     |     |
LR 63 10 12 60 63 /  offering a more reliable measure of generalization. When validated
(63+10) =
using this method, as shown in Fig. 7, several models exhibited perfor-
0.863
mance declines. Notably, the Decision Tree classifier, which initially
| KNN 71 | 2 29 | 43 71 / (71+2)  |     |     |     |     |
| ------ | ---- | --------------- | --- | --- | --- | --- |
=0.972 recorded over 90 % accuracy, saw a reduction to 84.44 %, with a cor-
ANN 68 5 12 60 68 / (68+5)  responding drop in F1 Score and an increase in error metrics. This
=0.932 suggests that its original performance was likely influenced by over-
XGBoost 69 4 5 67 69 /  fitting. Similarly, XGBoost, while still the top performer, experienced a
(69þ4) ¼
slight reduction in accuracy to 90.66 % and a modest increase in error,
0.945
reflecting a more realistic estimate of its predictive strength. Naïve
| GB 68 | 5 6 | 66 68 / (68+5)  |     |     |     |     |
| ----- | --- | --------------- | --- | --- | --- | --- |
=0.932 Bayes continued to display high recall but was again marked by poor
| NB 67 | 6 31 | 41 67 / (67+6)  |     |     |     |     |
| ----- | ---- | --------------- | --- | --- | --- | --- |
precision and increased error, further confirming its tendency to over-
=0.918
predict positive cases. In contrast, models such as Random Forest, Lo-
gistic Regression, and Multilayer Perceptron maintained relatively
Table 7presents the initial evaluation results of ten machine learning  consistent performance across both evaluation strategies, suggesting
models based on a standard train-test split. The assessment covers key  more stable generalization.
These results underscore the necessity of employing cross-validation
classification metrics, such as Accuracy, Precision, Recall, and F1 Score,
techniques when evaluating machine learning models, especially in
as well as error metrics like MSE and Log Loss. Among all models,
sensitive domains like education. While initial single-split evaluations
Extreme Gradient Boosting (XGBoost) demonstrated the strongest per-
are useful for exploratory comparisons, they do not account for vari-
formance, achieving the highest accuracy (93.79 %), F1 Score (93.88),
ability and are prone to optimistic bias. Cross-validation mitigates these
and lowest MSE (6.21), with a competitive Log Loss value of 3.98.
risks by ensuring each data point contributes to both training and
Similarly, Gradient Boosting yielded high classification scores, with
92.41 % accuracy and 92.52 F1 Score, and matched the lowest Log Loss  testing,  resulting  in  more  robust  and  generalizable  performance
| value (3.23), suggesting well-calibrated probability estimates. Multi- |     |     | estimates. |     |     |     |
| ---------------------------------------------------------------------- | --- | --- | ---------- | --- | --- | --- |
layer Perceptron (MLP) and Artificial Neural Network (ANN) models  Furthermore cross-validation revealed meaningful differences in
also performed strongly, particularly in recall (90.41 % and 93.15 %,  model  performance,  correcting  overestimations  observed  in  pre-
respectively), indicating their sensitivity in identifying students at risk of  validation results. The XGBoost model remained the most reliable and
consistent across all metrics, reinforcing its suitability for deployment in
withdrawal.
early warning systems aimed at reducing student attrition. These find-
The Decision Tree classifier recorded competitive scores, including a
ings highlight the importance of rigorous validation when applying
90.34 % accuracy and 90.54 F1 Score. However, its Log Loss was rela-
predictive analytics to educational decision-making.
tively high at 5.47, suggesting less confidence in its probability estimates
despite good classification performance. Conversely, Naïve Bayes, while
| achieving a high recall of 91.78 %, posted the lowest precision (68.37 %)  |     |     | 4. Discussion |     |     |     |
| -------------------------------------------------------------------------- | --- | --- | ------------- | --- | --- | --- |
and the poorest error scores, with the highest MSE (25.52) and Log Loss
(9.45), reflecting a high false positive rate and poor calibration. Support  Student retention continues to be a persistent challenge in higher
Vector Machine (SVM) similarly underperformed, with an accuracy of  education,  with  significant  implications  for  institutional  rankings,
80.00 %, MSE of 20.00, and a Log Loss of 5.72. reputational standing, and financial sustainability. As such, it remains a
The addition of MSE and Log Loss in this preliminary evaluation  widely studied area in academic literature. Traditional approaches
Table 7
Assessment scores of each model.
No. MODEL Accuracy ( %) Precision ( %) Recall ( %) F1 score ( %) MSE Log Loss
| 1 Support Vector Machine |     | 80.00 | 78.21 | 83.56 | 80.79 | 20.0 5.72  |
| ------------------------ | --- | ----- | ----- | ----- | ----- | ---------- |
| 2 Random Forest          |     | 88.28 | 88.89 | 87.67 | 88.28 | 11.7 3.98  |
| 3 Multilayer Perceptron  |     | 88.97 | 88.00 | 90.41 | 89.19 | 11.0 3.23  |
| 4 Decision Tree          |     | 90.34 | 89.33 | 91.78 | 90.54 | 9.66 5.47  |
| 5 Logistic Regression    |     | 84.83 | 84.00 | 86.30 | 85.14 | 15.1 8.20  |
| 6 K-Nearest Neighbor     |     | 83.45 | 78.82 | 91.78 | 84.81 | 16.55 7.21 |
7 Artificial Neural Network 88.28 85.00 93.15 88.89 10.61 4.23
8 Extreme Gradient Boosting 93.79 93.24 94.52 93.88 6.21 3.98
| 9 Gradient Boosting |     | 92.41 | 91.89 | 93.15 | 92.52 | 7.59 3.23  |
| ------------------- | --- | ----- | ----- | ----- | ----- | ---------- |
| 10 Naive Bayes      |     | 74.48 | 68.37 | 91.78 | 78.36 | 25.52 9.45 |
10

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
Fig. 7. Model performance based on classification and error metrics (5-fold cross-validation). This figure compares ten machine learning models using classification
metrics—accuracy, precision, recall, and F1 score (left panel), alongside error metrics, MSE and log loss (right panel), evaluated using 5-fold cross-validation. Among
the models, extreme gradient boosting (XGBoost) achieved the highest accuracy (90.66 %), F1 score (90.72), and one of the lowest error values (MSE =9.34, log loss
=0.26), indicating superior predictive performance. Gradient boosting and multilayer perceptron (MLP) also exhibited competitive results with strong classification
scores and low error values. Conversely, Naïve Bayes and support vector machine (SVM) showed higher error metrics, reflecting less consistent predictive reliability.
These metrics provide a balanced view of both classification correctness and model confidence, aiding in robust model selection for student retention prediction tasks.
relying on subjective assessments and historical trends are often insuf- across all evaluation phases. It yielded the lowest accuracy (74.48 %) in
ficient to capture the complexity of student attrition. To improve pre- the initial evaluation and the highest error metrics after cross-validation
dictive capability and support timely interventions, ML techniques have (MSE = 24.06, Log Loss = 8.67). Although Naïve Bayes recorded the
become increasingly prominent. These methods enable institutions to highest recall (97.21 %), it also produced 31 false positives, indicating a
extract patterns from diverse data sources, generate accurate dropout tendency to over-predict dropout risk. While its simplicity and compu-
predictions, and inform data-driven policies aimed at improving student tational efficiency may still make it suitable for certain contexts or
outcomes. ensemble integration, the high misclassification rates suggest it may not
In this study, multiple ML models were evaluated to predict student be ideal for high-stakes educational interventions without further
dropout using a combination of academic and sociodemographic factors. refinement.
The models were first assessed using a traditional train-test split, fol- The analysis also highlighted important trade-offs between para-
lowed by a more rigorous 5-fold cross-validation, to ensure robustness metric and nonparametric models. For example, K-Nearest Neighbors
and generalizability of results. Across both evaluation phases, Extreme (KNN), a nonparametric algorithm, achieved the highest recall (97.2 %)
Gradient Boosting (XGBoost) consistently outperformed other models. but also had one of the highest false positive counts (29). Likewise,
In the initial evaluation, XGBoost achieved an accuracy of 93.79 %, F1 Decision Tree, another nonparametric method, showed strong recall
Score of 93.88, and the lowest MSE of 6.21. After cross-validation, (91.8 %) but relatively poor error metrics, reflecting sensitivity to
XGBoost maintained its top-ranking performance, achieving an overfitting and variability across folds. These models are highly effective
average accuracy of 90.66 %, F1 Score of 90.72, and low error metrics in pattern detection but may require careful tuning and ensemble inte-
(MSE =9.34, Log Loss =0.26). The confusion matrix also reinforced gration to enhance stability.
these findings, with XGBoost yielding 67 true positives, 69 true nega- On the other hand, ensemble and hybrid models such as GB and ANN
tives, 5 false positives, and only 4 false negatives—the lowest total offered competitive, balanced performance. GB achieved 89.42 % ac-
misclassifications among all models tested. Moreover, these results are curacy post-cross-validation with a low Log Loss of 0.25, the lowest
strongly supported by prior literature. Study [49] found that XGBoost among all models, and maintained strong classification results (66 true
consistently outperformed alternative models in forecasting tasks such positives, 68 true negatives). ANN followed closely with 88.39 % ac-
as stock price movements. Similarly [50], emphasized XGBoost’s ca- curacy, 86.35 % precision, and a high recall of 91.48 %. These models
pacity for generalization, reduced overfitting, and enhanced predictive demonstrate high sensitivity and specificity while maintaining fewer
accuracy [51]. noted that XGBoost is uniquely capable of handling misclassifications, supporting their reliability for real-world applica-
heterogeneous and noisy datasets, outperforming models that perform tions. Also, the potential of neural network models is further supported
best only under controlled or homogeneous input conditions. Further- by [53], which found that deep learning architectures, including MLP
more [52], reported that XGBoost achieves superior accuracy, speci- and ANN, outperform traditional statistical methods in modeling com-
ficity, and sensitivity compared to Logistic Regression, particularly in plex and nonlinear patterns in student data. However, our findings
handling class-imbalanced datasets, an important feature in dropout suggest that while ANN performed competitively, XGBoost retained a
prediction, where class imbalance is often present. Together, these performance edge in terms of both classification accuracy and error
findings and our results strongly establish XGBoost as a robust and minimization, suggesting greater generalizability and practical usabil-
adaptable model for educational prediction tasks. ity, especially when false positives must be minimized in institutional
Conversely, Naïve Bayes was consistently the weakest performer settings.
11

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
The integration of the predictive modeling framework developed in models were assessed using both a traditional train-test split and 5-fold
this study demonstrates substantial pedagogical and institutional value cross-validation. Among the tested models, XGBoost consistently deliv-
for ITE curricula in the Philippines. Although the analysis was conducted ered the highest performance in both classification and error metrics,
using data from a single institution, Mindanao State University Main with an average cross-validated accuracy of 90.66 %, F1 Score of 90.72,
Campus in Marawi City, the design and structure of the dataset establish and low error values (MSE =9.34, Log Loss =0.26). Ensemble models
a scalable and transferable foundation that can be readily adopted by such as GB and ANN also showed strong and balanced results. These
other higher education institutions. The dataset comprises 482 complete findings demonstrate that predictive modeling, particularly using
student records and 146 variables, encompassing essential dimensions ensemble and neural network techniques, offers significant promise for
of student profiling such as sociodemographic indicators (e.g., age, sex, building early warning systems that can identify students at risk of
parental income), academic performance (e.g., normalized grades), and attrition. Moreover, the dataset and modeling approach are structured in
program progression metrics (e.g., year level, total units earned, course a generalizable format, offering a transferable framework for other
history). These data dimensions are consistent with widely accepted higher education institutions aiming to improve student retention
frameworks in educational data mining and learning analytics [54,55], through analytics. From a pedagogical perspective, the integration of
making the model broadly applicable across academic settings. predictive modeling into ITE programs can cultivate technical compe-
Importantly, this framework offers a replicable blueprint for in- tence in educational data science while reinforcing real-world applica-
stitutions aiming to develop their own student retention analytics. Prior tion of AI in institutional contexts.
studies emphasize that predictive models based on institutional data can Despite its promising outcomes, this study is not without limitations.
effectively identify at-risk students and guide timely interventions First, the data was sourced from a single institution, which may limit the
[9–11,13–16]. Since the variables used in this study are generalizable external validity of the findings despite the dataset’s broad and gener-
and align with common student information systems, other universities alized features. Further, while 5-fold cross-validation mitigated risks of
can easily adapt their internal data infrastructures to adopt similar overfitting and sampling bias, more advanced validation strategies such
models. This creates a pathway for ITE programs to lead institutional as stratified or nested cross-validation could yield even more robust
analytics initiatives, fostering real-world engagement with artificial in- generalization. In addition, the study focused primarily on academic and
telligence while strengthening the culture of data-informed decision-- sociodemographic variables; behavioral and psychosocial dimensions,
making in education. such as LMS engagement, motivation, or peer interaction, were not
Moreover, this study underscores the strategic role of ITE programs included but are known to be significant predictors of student success.
in driving institutional digital transformation. As digital transformation The inclusion of these features in future studies may improve the pre-
in education increasingly relies on data-driven approaches [53], cision and contextual relevance of predictive models. Similarly, while
equipping students and faculty with the capability to build and interpret XGBoost achieved the strongest performance, model interpretability
predictive models using academic data is both timely and necessary. remains a challenge for deployment in sensitive domains like education.
Engaging with real institutional data not only cultivates technical skills Institutions seeking to implement such models should complement high-
but also develops ethical reasoning and accountability in the use of AI in performance algorithms with explainable AI tools to ensure trans-
education—a point highlighted in literature on educational data science parency, fairness, and ethical accountability. Lastly, this study re-
[14,18,37]. By empowering students to apply these models within their inforces the emerging role of ITE programs in driving institutional
own institutions, ITE departments position themselves as active agents digital transformation by equipping both faculty and students with the
of change, contributing to improved educational outcomes through skills to develop intelligent systems grounded in real-world data.
interpretable, context-aware, and impactful computing solutions. Looking ahead, future research can build on this work by investigating
Looking forward, future research on student retention should prior- hybrid ensemble techniques, Deep P-Spline architectures, Additive
itize the integration of psychosocial, behavioral, and engagement-based Gaussian Process Models, and longitudinal approaches such as LSTM
features [56] such as attendance, motivation, learning management networks to capture more nuanced patterns in student dropout behavior.
system (LMS) activity [57], and peer interaction data [58], to enhance As higher education institutions increasingly embrace data-driven de-
predictive power. Moreover, temporal modeling using architectures like cision-making, this study serves as both a foundational benchmark and a
Long Short-Term Memory (LSTM) networks offers promising potential transferable framework for embedding predictive analytics into educa-
for real-time risk monitoring and longitudinal trend analysis across se- tional practice and strategic policy formulation.
mesters [25]. To improve both model performance and interpretability,
researchers are also encouraged to explore Deep P-Spline Models [59], Acknowledgment
Additive Gaussian Process Models [60], and hybrid ensemble strategies,
which offer scalable and flexible frameworks for capturing complex The authros would like to express their sincere gratitude to Mind-
non-linear patterns in large, structured educational datasets. anao State University - Main Campus, and the Office of the Vice Chan-
Furthermore, the results of this study affirm that XGBoost is the most celor for Academic Affairs for granting permissoin to utilize students’
accurate, stable, and generalizable model for predicting student academic and sociodemographic data for this research. Special thanks
dropout, outperforming both traditional and deep learning methods. are also extended to the Mamitua Saber Institute of Research and Cre-
However, the continued development of richer datasets, more inter- ation (MSIRC) for their valuable support throughout the conduct of the
pretable models, and ethically aligned deployment practices will be vital study.
in advancing the field of educational data mining and its impact on
student success, particularly when integrated into IT education for both CRediT authorship contribution statement
instructional and institutional innovation.
Reymark D. Delen˜a: Writing – review & editing, Writing – original
5. Conclusions draft, Visualization, Validation, Supervision, Software, Resources,
Project administration, Methodology, Investigation, Funding acquisi-
This study evaluated ten machine learning algorithms for predicting tion, Formal analysis, Data curation, Conceptualization. Nornin˜a J.
student dropout using historical data from MSU-Marawi spanning 2012 Dia: Writing – original draft, Visualization, Software, Resources, Project
to 2022. Through the application of the CRISP-DM methodology, com- administration, Methodology, Investigation, Formal analysis, Data
bined with Power BI for preprocessing and Jupyter Notebook for curation, Conceptualization. Redeemtor R. Sacayan: Writing – original
modeling, the data was rigorously prepared for analysis. After filtering draft, Validation, Funding acquisition, Formal analysis. Joseph C.
variables using Spearman correlation to minimize multicollinearity, Sieras: Supervision, Funding acquisition, Conceptualization. Suhaina
12

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
A. Khalid: Resources, Investigation, Funding acquisition. Amer Hus- ("Recall Score: ", recall_xgb) print("F1 Score: ", f1_xgb) print("Mean
sien T. Macatotong: Software, Resources, Funding acquisition. Sacaria Squared Error: ", mse_xgb)
B. Gulam: Resources, Funding acquisition, Data curation. # GENERATING THE CONFUSION MATRIX cm =confusion_matrix
(y_test, prediction_xgb) sns.heatmap(cm, annot=True) plt.ylabel(’Pre-
Declaration of competing interest diction’,fontsize=13) plt.xlabel(’Actual’,fontsize=13) plt.title(’Confu-
sion Matrix’,fontsize=17) plt.show()
The authors declare that they have no known competing financial #COMPUTING THE LOG LOSS OF THE MODEL from sklearn.metrics
interests or personal relationships that could have appeared to influence import log_loss ll_xgb =log_loss(y_test, prediction_xgb) print(’Log Loss
the work reported in this paper. of Extreme Gradient Boosting:’, ll_xgb)
Appendices Data availability
Splitting the data into training and testing data then removing If this paper is accepted for publication, the data will be published in
multicollinearity a separate article.
#TRANSFORMING THE CATEGORICAL INTO NUMERICAL DATA References
from sklearn.preprocessing import LabelEncoder
#creating an instance of Label Encoder le =LabelEncoder() [1] S. Ameri, M.J. Fard, R.B. Chinnam, C.K. Reddy, Survival analysis based framework
for early prediction of student dropouts, in: International Conference on
#Using .fit_transform function to fit label encoder and return enco- Information and Knowledge Management, Proceedings, 2016, pp. 903–912,
ded label label =le.fit_transform(student_df[’DROPOUT’]) https://doi.org/10.1145/2983323.2983351, 24-28-October-2016.
#removing the categorized (old) column ’TARGET’ and adding [2] S. Trivedi, Improving students’ retention using machine learning: impacts and
‘DROPOUT’ which contains numerical data. student_df.drop implications, Sci. Prepr. (2022), https://doi.org/10.14293/S2199-1006.1.SOR-.
PPZMB0B.V2.
(’DROPOUT’, axis=1, inplace=True) student_df[’DROPOUT’] =label
[3] Bineid, A.A. (2022). Predicting student withdrawal from UAE CHEDS repository
#SPLITTING THE DATA INTO TESTING AND TRAINING from using data mining methodology. 1–72. https://bspace.buid.ac.ae/handle/1234/
2130.
sklearn.model_selection import train_test_split
[4] Calvert, C.E. (2014). Developing a model and applications for probabilities of
X_train, X_test, y_train, y_test =train_test_split(X, Y, test_size=0.3) student success: a case study of predictive analytics. 29(2), 160–173. https://doi.
#GENERATING THE CORRELATION MATRIX corrmat =student_df. org/10.1080/02680513.2014.931805.
corr(method ="spearman") corrmat plt.figure(figsize=(50,50)) mask = [5] R.S.J.d. Baker, K. Yacef, The State of educational data mining in 2009: a review and
future visions, J. Educ. Data Min. 1 (1) (2009) 3–17, https://doi.org/10.5281/
np.triu(np.ones_like(corrmat, dtype=bool)) sns.heatmap(corrmat, ZENODO.3554657.
annot=True, annot_kws={"size":4}, mask=mask, vmin=-1, vmax=1) [6] Fain, P. (2016). Data on student engagement with an LMS is a key to predicting
plt.title(’Correlation Coefficient of Predictors’) plt.show retention. https://www.insidehighered.com/news/2016/06/13/data-student-
#REMOVING THE HIGHLY CORRELATED VARIABLES (WITH ≥70 engagement-lms-key-predicting-retention.
[7] A.I. Adekitan, E. Noma-Osaghae, Data mining approach to predicting the
% THRESHOLD) def correlation(student_df, threshold): correlated_cols performance of first year student in a university using the admission requirements,
=set() corr_matrix =student_df.corr(method="spearman") for i in range Educ. Inf. Technol. 24 (2) (2018) 1527–1543, https://doi.org/10.1007/S10639-
018-9839-7, 2018 24:2.
(len(corr_matrix.columns)): for j in range (i): if abs(corr_matrix.iloc[i, [8] M. Bucos, B. Dr˘agulescu, Predicting student success using data generated in
j])> threshold: colname = corr_matrix.columns[i] correlated_cols.add traditional educational environments, TEM J. 7 (3) (2018) 617, https://doi.org/
(colname) return correlated_cols 10.18421/TEM73-19.
#storing the variables with ≥70 % threshold in corr_features then [9] A.I. Adekitan, E. Noma-Osaghae, Data mining approach to predicting the
performance of first year student in a university using the admission requirements,
removing them. corr_feature =correlation(student_df, 0.7) Educ. Inf. Technol. 24 (2) (2018) 1527–1543, https://doi.org/10.1007/S10639-
X_train.drop(labels=corr_feature, axis=1, inplace=True) 018-9839-7, 2018 24:2.
X_test.drop(labels=corr_feature, axis=1, inplace=True) [10] H. Almarabeh, Analysis of students’ performance by using different data mining
classifiers, Int. J. Mod. Educ. Comput. Sci. 9 (8) (2017) 9–15, https://doi.org/
#plotting the new matrix corr =X_train.corr(method="spearman") 10.5815/IJMECS.2017.08.02.
plt.figure(figsize=(30,30)) mask = np.triu(np.ones_like(corr, dty- [11] E. Alhazmi, A. Sheneamer, Early predicting of students performance in higher
pe=bool)) sns.heatmap(corr, annot=True, annot_kws={"size":4}, education, IEEE Access 11 (2023) 27579–27589, https://doi.org/10.1109/
ACCESS.2023.3250702.
mask=mask, vmin=-1, vmax=1) plt.title(’Correlation Coefficient of [12] D. Uliyan, A.S. Aljaloud, A. Alkhalil, H.S.A. Amer, M.A.E.A. Mohamed, A.F.
Predictors’) plt.show M. Alogali, Deep learning model to predict students retention using BLSTM and
CRF, IEEE Access 9 (2021) 135550–135558, https://doi.org/10.1109/
ACCESS.2021.3117117.
Sample code for identifying the prediction performance of a model [13] N.R. Beckham, L.J. Akeh, G.N.P. Mitaart, J.v. Moniaga, Determining factors that
affect student performance using various machine learning methods, Procedia
#importing evaluation metrics from sklearn.metrics import accu- Comput. Sci. 216 (2023) 597–603, https://doi.org/10.1016/j.procs.2022.12.174.
[14] J. Niyogisubizo, L. Liao, E. Nziyumva, E. Murwanashyaka, P.C. Nshimyumukiza,
racy_score, precision_score, recall_score, f1_score, mean_squared_error Predicting student’s dropout in university classes using two-layer ensemble
from sklearn.metrics import confusion_matrix machine learning approach: a novel stacked generalization, Comput. Educ. 3
#importing the model import xgboost as xgb xgb =xgb.XGBClassi- (2022) 100066, https://doi.org/10.1016/j.caeai.2022.100066.
[15] R. Ghorbani, R. Ghousi, Comparing different resampling methods in predicting
fier() students’ performance using machine learning techniques, IEEE Access 8 (2020)
#fitting the model xgb.fit(X_train, y_train) 67899–67911, https://doi.org/10.1109/ACCESS.2020.2986809.
#TESTING THE PREDICTION prediction_xgb = xgb.predict(X_test) [16] F. Marbouti, J. Ulas, C.-H. Wang, Academic and demographic cluster analysis of
engineering student success, IEEE Trans. Educ. 64 (3) (2021) 261–266, https://doi.
prediction_xgb
org/10.1109/TE.2020.3036824.
[17] P. Xuan Lam, P.Q.H. Mai, Q.H. Nguyen, T. Pham, T.H.H. Nguyen, T.H Nguyen,
Assessing the accuracy rate of the model Enhancing educational evaluation through predictive student assessment
modeling, Comput. Educ. 6 (2024) 100244, https://doi.org/10.1016/J.
CAEAI.2024.100244.
#checking the evaluation metrics score of the model accuracy_xgb = [18] A. Gonzalez-Nucamendi, J. Noguez, L. Neri, V. Robledo-Rella, R.M.G. García-
accuracy_score(y_test, prediction_xgb)*100 precision_xgb =precision_- Castela´n, Predictive analytics study to determine undergraduate students at risk of
score(y_test, prediction_xgb)*100 recall_xgb = recall_score(y_test, pre- dropout, Front. Educ. 8 (2023) 1244686, https://doi.org/10.3389/
FEDUC.2023.1244686.
diction_xgb)*100 f1_xgb =f1_score(y_test, prediction_xgb)*100 mse_xgb [19] S. Alwarthan, N. Aslam, I.U. Khan, An explainable model for identifying at-risk
= mean_squared_error(y_test, prediction_xgb)*100 print("Accuracy student at higher education, IEEE Access 10 (2022) 107649–107668, https://doi.
Score: ", accuracy_xgb) print("Precision Score: ", precision_xgb) print org/10.1109/ACCESS.2022.3211070.
13

R.D. Delen˜a et al. S y s t e m s a n d S o f t C o m p u t ing 7 (2025) 200352
[20] G. Feng, M. Fan, Y. Chen, Analysis and prediction of students’ academic [40] A.M. Dur´an-Rosal, T. Ashley, J. P´erez-Rodríguez, F. Fern´andez-Navarro, Global and
performance based on educational data mining, IEEE Access 10 (2022) diverse ensemble model for regression, Neurocomputing 647 (2025) 130520,
19558–19571, https://doi.org/10.1109/ACCESS.2022.3151652. https://doi.org/10.1016/J.NEUCOM.2025.130520.
[21] A.M. Mariano, A.B. de Magalh˜aes Lelis Ferreira, M.R. Santos, M.L. Castilho, A.C.F. [41] R.E. Uhrig, Introduction to artificial neural networks, in: Proceedings of IECON ’95
L.C Bastos, Decision trees for predicting dropout in engineering course students in - 21st Annual Conference on IEEE Industrial Electronics 1, 2002, pp. 33–37,
Brazil, Procedia Comput. Sci. 214 (2022) 1113–1120, https://doi.org/10.1016/j. https://doi.org/10.1109/IECON.1995.483329.
procs.2022.11.285. [42] Accuracy, I.S.O., Of Measurement Methods and Results—Part 1: General principles
[22] H.P. Singh, H.N. Alhulail, Predicting student-teachers dropout risk and early and Definitions, International Organization for Standardization, Geneva,
identification: a four-step logistic regression approach, IEEE Access 10 (2022) Switzerland, 1994.
6470–6482, https://doi.org/10.1109/ACCESS.2022.3141992. [43] D. Chicco, G. Jurman, The advantages of the Matthews correlation coefficient
[23] F. Marbouti, J. Ulas, C.-H. Wang, Academic and demographic cluster analysis of (MCC) over F1 score and accuracy in binary classification evaluation, BMC Genom.
engineering student success, IEEE Trans. Educ. 64 (3) (2021) 261–266, https://doi. 21 (1) (2020) 1–13, https://doi.org/10.1186/S12864-019-6413-7/TABLES/5.
org/10.1109/TE.2020.3036824. [44] N.J. Dia, J.C. Sieras, S.A. Khalid, A.H.T. Macatotong, J.M. Mondejar, E.R. Genotiva,
[24] A. Nabil, M. Seyam, A. Abou-Elfetouh, Prediction of students’ academic R.D. Delena, EduGuard RetainX: an advanced analytical dashboard for predicting
performance based on courses’ grades using deep neural networks, IEEE Access 9 and improving student retention in tertiary education, SoftwareX 29 (2025)
(2021) 140731–140746, https://doi.org/10.1109/ACCESS.2021.3119596. 102057, https://doi.org/10.1016/j.softx.2025.102057.
[25] H. Prabowo, A.A. Hidayat, T.W. Cenggoro, R. Rahutomo, K. Purwandari, [45] N. Dia, R. Delena, EduGuard RetainX: an Advanced Analytical Dashboard For
B. Pardamean, Aggregating time series and tabular data in deep learning model for Predicting and Improving Student Retention in Tertiary Education (Version V1),
university students’ GPA prediction, IEEE Access 9 (2021) 87370–87377, https:// CodeOcean, 2024. https://codeocean.com/capsule/2453835/tree/v1.
doi.org/10.1109/ACCESS.2021.3088152. </Dataset>.
[26] C.F. Rodríguez-Herna´ndez, M. Musso, E. Kyndt, E. Cascallar, Artificial neural [46] M. Mukaka, Statistics corner: a guide to appropriate use of correlation coefficient
networks in academic performance prediction: systematic implementation and in medical research, Malawi Med. J. 24 (3) (2012) 69–71.
predictor evaluation, Comput. Educ. 2 (2021) 100018, https://doi.org/10.1016/j. [47] Setia, M. (2023, September 14). Log loss - logistic regression’s cost function for
caeai.2021.100018. beginners. https://www.analyticsvidhya.com/blog/2020/11/binary-cross-entro
[27] A.J. Fern´andez-García, R. Rodríguez-Echeverría, J.C. Preciado, J.M.C. Manzano, pyaka-log-loss-the-cost-function-used-in-logistic-regression/.
F. Sa´nchez-Figueroa, Creating a recommender system to support higher education [48] H. Babaei, M. Zamani, S. Mohammadi, The impact of data splitting methods on
students in the subject enrollment decision, IEEE Access 8 (2020) 189069–189088, machine learning models: a case study for predicting concrete workability, Mach.
https://doi.org/10.1109/ACCESS.2020.3031572. Learn. Comput. Sci. Eng. 1 (1) (2025), https://doi.org/10.1007/s44379-025-
[28] H.A. Mengash, Using data mining techniques to predict student performance to 00021-3.
support decision making in university admission systems, IEEE Access 8 (2020) [49] Dey, S., Kumar, Y., Saha, S., & Basak, S. (2016). Forecasting to classification:
55462–55470, https://doi.org/10.1109/ACCESS.2020.2981905. predicting the direction of stock market price using Xtreme gradient boosting. http
[29] T.A. Cardona, E.A. Cudney, Predicting student retention using support vector s://doi.org/10.13140/RG.2.2.15294.48968.
machines, Procedia Manuf. 39 (2019) 1827–1833, https://doi.org/10.1016/J. [50] P. Carmona, F. Climent, A. Momparler, Predicting failure in the U.S. banking
PROMFG.2020.01.256. sector: an extreme gradient boosting approach, Int. Rev. Econ. Finance 61 (2019)
[30] A. Viloria, J.G. Padilla, C. Vargas-Mercado, H. Herna´ndez-Palma, N.O. Llinas, M. 304–323, https://doi.org/10.1016/J.IREF.2018.03.008.
A. David, Integration of data technology for analyzing university dropout, Procedia [51] I. Babajide Mustapha, F. Saeed, Bioactive molecule prediction using extreme
Comput. Sci. 155 (2019) 569–574, https://doi.org/10.1016/j.procs.2019.08.079. gradient boosting, Molecules 21 (8) (2016), https://doi.org/10.3390/
[31] G. Lesinski, S. Corns, Multi-objective evolutionary neural network to predict MOLECULES21080983.
graduation success at the United States military academy, Procedia Comput. Sci. [52] Hanif, I. (2020). Implementing extreme gradient boosting (XGBoost) classifier to
140 (2018) 196–205, https://doi.org/10.1016/J.PROCS.2018.10.329. improve customer churn prediction. https://doi.org/10.4108/EAI.2-8-201
[32] G. Lesinski, S. Corns, C. Dagli, Application of an artificial neural network to predict 9.2290338.
graduation success at the United States military academy, Procedia Comput. Sci. 95 [53] M.F. Flayyih, H. Hassan TOUT, Predictive analytics model for students’ grade
(2016) 375–382, https://doi.org/10.1016/J.PROCS.2016.09.348. prediction using machine learning. a review, EDRAAK 2023 (2023) 1–4, https://
[33] M. Goga, S. Kuyoro, N. Goga, A recommender for improving the student academic doi.org/10.70470/EDRAAK/2023/001.
performance, Procedia - Soc. Behav. Sci. 180 (2015) 1481–1488, https://doi.org/ [54] C. Romero, S. Ventura, Educational data mining and learning analytics: an updated
10.1016/j.sbspro.2015.02.296. survey, Wiley Interdiscip. Rev. Data Min. Knowl. Discov. 10 (3) (2020), https://
[34] C. Schro¨er, F. Kruse, J.M. Go´mez, A systematic literature review on applying doi.org/10.1002/widm.1355.
CRISP-DM process model, Procedia Comput. Sci. 181 (2021) 526–534, https://doi. [55] G. Siemens, P. Long, Penetrating the fog: analytics in learning and education, Educ.
org/10.1016/J.PROCS.2021.01.199. Rev. 46 (5) (2011) 30. https://eric.ed.gov/?id=EJ950794.
[35] N. Caetano, P. Cortez, R.M.S. Laureano, Using data mining for prediction of [56] B. Chahar, S.R. Jain, V. Hatwal, Mediating role of employee motivation for
hospital length of stay: an application of the CRISP-DM methodology, Lect. Notes training, commitment, retention, and performance in higher education institutions,
Bus. Inf. Process. 227 (2015) 149–166, https://doi.org/10.1007/978-3-319-22348- Probl. Perspect. Manag. 19 (3) (2021) 95–106, https://doi.org/10.21511/ppm.19
3_9. (3).2021.09.
[36] Wirth, R., & Hipp, J. (2000). Crisp-dm: towards a standard process model for data [57] N. Nithiyanandam, S. Dhanasekaran, A.S. Kumar, D. Gobinath, P. Vijayakarthik, G.
mining. V. Rajkumar, U. Muthuraman, Artificial intelligence assisted student learning and
[37] V. Vijayalakshmi, K. Venkatachalapathy, Comparison of predicting student‘s performance analysis using instructor evaluation model, in: 2022 3rd International
performance using machine learning algorithms, Int. J. Intell. Syst. Appl. 11 (12) Conference on Electronics and Sustainable Communication Systems (ICESC), 2022,
(2019) 34–45, https://doi.org/10.5815/IJISA.2019.12.04. pp. 1555–1561, https://doi.org/10.1109/icesc54411.2022.9885462.
[38] S. Hansun, J. Tanuwijaya, LQ45 stock index prediction using k-nearest neighbors [58] S. Xiao, A. Shanthini, D. Thilak, Instructor performance prediction model using
regression, Int. J. Recent Technol. Eng. 8 (3) (2019) 2277–3878, https://doi.org/ artificial intelligence for higher education systems, J. Interconnect. Netw. 22
10.35940/ijrte.C4663.098319 (IJRTE). (Supp03) (2021), https://doi.org/10.1142/s0219265921440035.
[39] E. Osmanbegovic, M. Suljic, Data mining approach for predicting student [59] N.Y. Hung, L. Lin, V.D. Calhoun, Deep P-Spline: theory, fast tuning, and
performance, J. Econ. Bus. 10 (1) (2012) 3–12. https://www.researchgate.net/ application, arXiv (Cornell Univ.) (2025), https://doi.org/10.48550/
publication/242341193_DATA_MINING_APPROACH_FOR_PREDICTING_STUDE arxiv.2501.01376.
NT_PERFORMANCE. [60] L. Lin, V.R. Joseph, Transformation and additivity in gaussian processes,
Technometrics 62 (4) (2019) 525–535, https://doi.org/10.1080/
00401706.2019.1665592.
14