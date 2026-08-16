---
conversion_metadata:
  converted_at: "2026-07-21T13:36:29Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Jafarigol et al.pdf"
  source_pdf_sha256: "a52214eb2b7965a9d0b8589dfb0443ada19430a8556676aa73e29898093d8adb"
  page_count: 54
  markdown_char_count: 201338
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

A Review of Machine Learning Techniques in 
Imbalanced Data and Future Trends

Elaheh Jafarigola,1, Theodore B. Trafalisa, Neshat Mohammadia

aSchool of Industrial and Systems Engineering University of Oklahoma, 202 W. Boyd St., Room 124, Norman,

Oklahoma 73019, USA

Abstract

For  over  two  decades,  detecting  rare  events  has  been  a  challenging  task  among

researchers  in  the  data  mining  and  machine  learning  domain.  Real-life  problems

inspire researchers to navigate and further improve data processing and algorithmic

approaches to achieve effective and computationally ef(cid:976)icient methods for imbalanced

learning.  In  this  paper,  we  have  collected  and  reviewed  258  peer-reviewed  papers

from archival journals and  conference  papers  in  an  attempt to  provide  an  in-depth

review of various approaches in imbalanced learning from technical and application

perspectives.  This  work  aims  to  provide  a  structured  review  of  methods  used  to

address  the  problem  of  imbalanced  data  in  various  domains  and  create  a  general

guideline for researchers in academia or industry who want to dive into the broad (cid:976)ield

of machine learning using large-scale imbalanced data.

Keywords: imbalanced learning, rare events, data mining, classiﬁca(cid:415)on, predic(cid:415)on

Introduction

Classi(cid:976)ication problems are a major part of supervised learning and very often,

the data is not equally distributed between the classes.  The performance of the

classi(cid:976)ier is affected by the ratio of the majority class to the minority class, hence

1 Corresponding author

Email address: elaheh.jafarigol@ou.edu (Elaheh Jafarigol)

Preprint submitted to Elsevier

September 7, 2025

---

<!-- PAGE 2 -->

misclassi(cid:976)ication is more severe when the data is extremely imbalanced [1, 2, 3, 4,

5,  6].  In  addition  to  the  relative  proportion  of  classes,  the  absolute  number  of

available instances in the minority class is also an important factor. The problem

with imbalanced data is magni(cid:976)ied when the minority class consists of rare events.

Rare events are de(cid:976)ined as events that occur signi(cid:976)icantly less often than common

events.  In  the  case  of  rare  events,  classi(cid:976)ication  becomes  more  challenging,

because the classi(cid:976)ier is often overwhelmed by the majority class and the results

are biased. Therefore, without a signi(cid:976)icant loss in overall accuracy, the minority

class is misclassi(cid:976)ied. Based on the type of data, the size of the data set and the

distribution of data between classes, the issue of imbalanced learning can appear

at different levels. The problem de(cid:976)inition issues are caused by a lack of adequate

information  about  the  minority  class[7].  Problem  de(cid:976)inition  issues  can  cause

evaluation  metrics  such  as  accuracy  and  error  rate  to  fail  in  representing  the

minority  class.  Therefore,  other  evaluation  metrics  are  de(cid:976)ined  to  measure  the

classi(cid:976)ier in imbalanced learning problems.

The data issues are the result of absolute rarity and extremely imbalanced data.

Resampling methods are the standard solution to this issue. Algorithm issues are

caused  by  inadequacies  of  the  learning  algorithm  and  may  result  in  poor

classi(cid:976)ication accuracy of the minority class. Such issues are caused by the model’s

failure in learning the necessary criteria for classi(cid:976)ication. The goal of imbalanced

learning  is  to  (cid:976)ind  an  optimal  classi(cid:976)ier  that  is  capable  of  providing  a  balanced

degree of predictive accuracy for the minority class as well as the majority class

[8, 9, 10, 11, 12, 13, 14]. These methods are primarily attempting to address the

issue  of  absolute  class  imbalance  that  exists  in  some  datasets.  However,  the

relative class imbalance is still an important issue in datasets where we have an

abundance of training examples, but the distribution of the different classes might

be  severely  skewed.  In  this  latter  situation,  one  can  have  access  to  enough

examples from the  minority class, even if the frequency  of the minority class is

very small, as long as the total number of examples is suf(cid:976)iciently big [15]. With

the  broad  applications  of  imbalanced  learning  in  the  real  world,  this  area  has

attracted  the  interest  of  many  researchers  and  despite  the  advances,  most

2

---

<!-- PAGE 3 -->

imbalanced learning methods are still sensitive to highly imbalanced data. In this

survey, we have selected 258 peer-reviewed papers among the papers published

on  the  topic  of  imbalanced  learning  and  its  applications.  Figure  1  presents  the

technical key words used in our search.

Figure 1: Technical Keywords in Imbalanced Learning Literature

In this paper, an overview of different approaches for the problem of imbalanced

learning  categorized  based  on  the  format  provided  in  Figure  2,  followed  bu  its

applications in real-life problems is presented. The paper is organized as follows, in

section 1, we provide a categorized de(cid:976)inition of problem de(cid:976)inition approaches and

the  different  types  of  metrics  used  in  this  setting.  In  section  2,  we  focus  on  data

processing  approaches  and  extensively  study  different  over-sampling  and  under-

sampling  methods  used  in  the  literature.  Section  3  focuses  on  the  algorithmic

approach  and  the  core  machine  learning  methods  for  learning  from  large

imbalanced datasets. In section 4 an overview of imbalanced learning applications

is provided. Finally, we discuss some ideas of future research trends and conclude

the paper.

3

---

<!-- PAGE 4 -->

Figure 2: General Approaches in Imbalanced Learning

Current Approaches

1.  Problem De(cid:976)inition Approaches

1.1.  Evaluation Metrics

Evaluation is an important part of the learning process. Evaluation metrics are

generally  used  to  assess  the  generalization  ability  of  the  learning  method  on  test

data. One of the major issues that arise with imbalanced data is the inadequacy of

well-known metrics such as accuracy and error rate in the evaluation of classi(cid:976)ication

performance. Appropriate evaluation metrics are important in evaluating the quality

of learning. Therefore, several authors have addressed this major issue and a new set

of  functions  have  been  de(cid:976)ined  to  determine  how  the  classi(cid:976)ier  performs  in

classifying imbalanced data [16, 17, 18]. The authors of the paper published by Ferri

et al. [19] have used experimental and theoretical analysis to compare and rank the

evaluation  metrics  that  work  best  on  evaluating  the  learned  model  on  imbalance

data  and  analyze  the  identi(cid:976)iable  clusters  and  relationships  between  the  metrics.

These  experiments  provide  recommendations  on  the  metrics  that  would  be more

appropriate  for  any  speci(cid:976)ic  application.  Evaluation  metrics  are  categorized  into

three types in the literature; threshold, probability, and ranking metrics [20].

4

---

<!-- PAGE 5 -->

1.1.1.  Threshold Evaluation Metrics

The threshold type of evaluation metric is de(cid:976)ined based on a confusion matrix

as it is shown in Table 1. In binary classi(cid:976)ication, given that the predicted value of

test samples in the majority class is denoted as N (Negative), and the predicted

value  of  the  test  samples  in  the  minority  class  is  denoted  as  P  (Positive),  the

Confusion matrix is de(cid:976)ined. Note that, the de(cid:976)inition of a Confusion matrix can be

extended to multi-class classi(cid:976)ication as well.

Table 1: Confusion Matrix

Predictive Value

Positive  Negative

TP

FP

FN

TN

Actual Value

Positive

Negative

Based on this notation, Accuracy is de(cid:976)ined as a measure for performance of a

classi(cid:976)ication algorithm. Accuracy is de(cid:976)ined as:

Accuracy =

(1) TP + TN + FP + FN

TP + TN

Accuracy is easy to use and interpret, however, despite being widely used by

practitioners, it cannot provide enough information to ensure a reliable learning

method when the data is imbalanced [21].

Classi(cid:976)ication  performance  metrics  for  imbalanced  learning  based  on  the

confusion metrics are de(cid:976)ined as:

and,

Precision =

TP

TP + FP

Recall =

TP

TP + FN

(2)

(3)

Precision and recall have an inverse relationship and when used together can

provide valid insight into the performance of the classi(cid:976)ier with regard to the

minority class. Precision and recall measure how exact and complete the model is,

respectively. Also, the precision-recall curve allows us to study the changes in both

5

---

<!-- PAGE 6 -->

metrics simultaneously. In imbalanced learning, models with high recall on the

minority class and high precision on the majority class are desired. Thus, F-measure

is a valuable evaluation metric in imbalanced learning de(cid:976)ined as:

(4)

where β is the relative importance of precision versus recall, and it is usually set

equal to one. In the presence of rare events a common approach is to maximize

the F-measure. Musicant et al. [22] have developed an approach to maximize the

F-measure by using SVMs. Geometric mean/ G-mean is an important

evaluation metric that is used explicitly for imbalanced learning.

r

G − mean =(5)

TP

TN

·

TP + FN

TN + FP

A high G-mean indicates that the model is performing well in both classes.

Other metrics used in the literature are but not limited to:

r

r

NegativePredictiveV alue = TN + FN

Mathews Correlation Coef(cid:976)icient (MCC) [23] is de(cid:976)ines as:

MCC =

TP ∗ TN − FP ∗ FN

Sensitivity =(6)

Speci(cid:980)icity =(7)

TP 
TP+FN

TN 
TN+FP

r

TN

(8)

(9)

p

and Bookmaker Informedness/Youden’s index = Sensitivity + Speci(cid:976)icity – 1

(TP + FP)(TP + FN)(TP + FN)(TN + FN)

[24].

1.1.2.  Probability Evaluation Metrics

The probability evaluation metrics are used with classi(cid:976)ication problems that

focus  on  predicting  the  probability  of  a  class  label.  Two  popular  probability

predicting  models  are regression models  and  Arti(cid:976)icial  Neural  Networks (ANN)

[25]. Minimum Risk Metric (MRM) utilizes the posterior probability estimations

to minimize the misclassi(cid:976)ication risk and provide an optimal solution. There are

6

---

<!-- PAGE 7 -->

several probabilistic evaluation metrics such as Short and Fukunaga Metric, the

Value  Difference  Metric,  and  Euclidean-Hamming  metrics.  The  Short  and

Fukunaga,  the  Value  Difference  and  Euclidean-Hamming  metrics  are  distance

functions used in Nearest Neighbor (NN) learning models to measure the distance

between two instances, that can determine the associated attribute and classify

the instance in the test data [26]. Log Loss is a classi(cid:976)ication performance metric

based on the cross-entropy function. Given that the expected/known probability

of an instance in the training data is denoted as P and the predicted probability of

an instance in the test data is denoted as Q, the cross-entropy for an instance in

binary-classi(cid:976)ication is de(cid:976)ined as:

H(P,Q) = −(P(class0) ∗ log(Q(class0)) + P(class1) ∗ log(Q(class1))

(10)

In this equation, the probability P is de(cid:976)ined based on the Bernoulli distribution

for  the  positive  class  and  natural  logarithm.  When  the  instance  is  known,  the

cross-entropy  is  zero,  therefore,  we  try  to  minimize  the  cross-entropy  of  the

model.

1.1.3.  Ranking Evaluation Metrics

Sensitivity or TP rate and Speci(cid:976)icity or TN rate are used to de(cid:976)ine the Receiver

Operating  Characteristic  (ROC)  curve,  which  is  a  visual  representation  of  the

classi(cid:976)ication performance. The Area Under the Curve (AUC) is de(cid:976)ined

as

.

AUC does not depend on the classi(cid:976)ier and it is a

reliable tool for model comparison because it is scale-invariant, and the output is

the ranking of classi(cid:976)iers rather than their absolute value. AUC can also assess the

quality of models using a threshold-invariant [27, 28].

Although AUC is widely used for the evaluation and discrimination process of

binary classi(cid:976)ication models, it can be misleading sometimes. AUC uses a different

misclassi(cid:976)ication  cost  for  each  classi(cid:976)ier.  Some  researchers  have  addressed  this

issue  and  proposed  modi(cid:976)ications  or  alternative  metrics  such  as  the  H  measure

which uses a symmetric Beta distribution in the AUC [29, 30].

To summarize, we have presented the evaluation metrics categorized based on

their outcome in imbalanced learning studies in Tables 2 ,3, 4 and Figure 3.

7

---

<!-- PAGE 8 -->

Metrics

Accuracy

Table 2: Threshold Metrics in Supervised Learning

De(cid:976)inition

The  ratio  of  the  correctly  classi(cid:976)ied  instances  over  the 
total number of classi(cid:976)ied instances

Error Rate

The ratio of misclassi(cid:976)ication errors over the classi(cid:976)ied 
instances

Precision

Recall

The proportion of instances that were labeled correctly 
among those with the positive label in the test data

The  portion  of  positive  instances  in  the  test  data  that 
were labeled correctly

F-measure

The trade-off between precision and recall

G-mean

Sensitivity

Speci(cid:976)icity

The measure to maximize the accuracy of the model over 
each class by considering both classes for evaluation

The  relative  performance  of  the  classi(cid:976)ier  over  the 
minority class

The  relative  performance  of  the  classi(cid:976)ier  over  the 
minority class

Negative

Predictive

Value

The number of TN over the instances with positive label 
in the test data

Mathews  Correlation

The measure of quality in binary classi(cid:976)ication

Coef(cid:976)icient

Bookmaker

Informedness

The measure if discrimination capability of the classi(cid:976)ier

Table 3: Probabilistic Metrics in Supervised Learning

Metrics

De(cid:976)inition

Minimum Risk

The probability of minimizing the misclassofocation risk 
while maintaining an optimal solution

8

---

<!-- PAGE 9 -->

Short and Fukunaga

A measure of distance between instances in Nearest

Neighbor models

Euclidean-Hamming

A measure of distance between instances in Nearest

Neighbor models

Log-loss

The  negative

log-likelihood  under

the  Bernoulli

distribution

Table 4: Ranking Metrics in Supervised Learning

Metrics

De(cid:976)inition

ROC Curve

Evaluate and rank several classi(cid:976)iers

AUC

The  probability  of  correctly  classifying  the  positive 
instances  while  the  number  of  false  positives 
is 
minimized

9

---

<!-- PAGE 10 -->

Figure 3: Evaluation Metrics in Imbalanced Learning

2.  Data Processing Approaches

2.1.  Resampling Methods

Resampling  methods  are  developed  to  balance  the  ratio  of  the  classes  in

imbalanced  learning  by  adjusting  the  minority  class  or  the  majority  class  and

enhancing  the  performance  of  the  classi(cid:976)ier  [31].  Generally,  basic  resampling

10

---

<!-- PAGE 11 -->

methods follow two strategies. The (cid:976)irst strategy is removing instances from the

majority class known as Random Under-sampling (RUS) [32, 33]. The second is

adding  new  instances  to  the  minority  class,  known  as  Random  Over-sampling

(ROS)[34]. These methods can  be utilized on  their  own  or in combination  with

each other to adjust the distribution of the data before classi(cid:976)ication. A limitation

of  RUS  and  ROS  is  removing  valuable  information  in  the  resampling  process,

therefore, under-(cid:976)itting or over-(cid:976)itting the data, respectively. To avoid such issues,

advanced  resampling  methods  were  developed  based  on  the  idea  of  a  guided

resampling. Advanced resampling methods include multiple variations of under-

sampling and over-sampling methods [35, 36]

2.1.1.  Under-sampling Methods

Under-sampling following the Nearest Neighbor (NN0 rule is the classi(cid:976)ication of

data based on the similarities between the data point and its nearest neighbor. This

decision  rule  has  a  lower  probability  of  error  than  several  other  decision  rules.

Variation of under-sampling based on NN rule includes condensed NN method, the

edited  NN  method,  the  repeated  edited  NN  method,  and  neighborhood  cleaning

method [37] and other variations [38, 39]. Tomek’s links (T-link) is an enhancement

of  NN  rule  for  under-sampling  the  majority  class  in  which  the  pair  of  data  with

opposite labels in the same neighborhood create a Tomek link. The data point on the

link  that  belongs  to  the  majority  class  is  removed.  This  method  improves  the

classi(cid:976)ication accuracy of the minority class by creating a distinct margin between the

two  classes  [40].  Under-sampling  based  on  clustering  utilizes  the  clustering

algorithms such as K-means that show promising performance with imbalanced data

[41]. The one-sided selection method is an adaptation of Tomek’s link. In this method,

a subset of the  majority class is selected for classi(cid:976)ication  while the minority class

remains  untouched  [42].  Under-sampling  based  on  Instances  Hardness  Threshold

(IHT)  method  is  used  to  overcome  the  problem  of  imbalanced  data.  This  under-

sampling method reduces the size of the majority class by removing the data that has

a high hardness threshold,  which is the  probability  of  misclassi(cid:976)ication of the data

[43, 44, 45].

11

---

<!-- PAGE 12 -->

2.1.2.  Over-sampling Methods

An  effective  way  of  dealing  with  the  issue  of  imbalanced  data  is  Over-sampling.

Studies suggest that the number of features and imbalance ratio are important factors

in determining the best approach [46, 47]. Over-sampling methods such as bootstrap-

based  over-sampling,  over-sampling  based  on  Synthetic  Minority  Over-sampling

Technique (SMOTE), and over-sampling based on Adaptive Synthetic sampling method

(ADASYN)  are  widely  used  in  imbalanced  learning  [48,  49,  50,  51,  52,  53,  54]

Bootstrap-based  over-sampling  is  iteratively  replicating  the  instances  of  a  selected

sample, in which the instances are replaced and are probable to be selected more than

once. The number of iterations and the sample size is required before oversampling

[55, 56].

In over-sampling using SMOTE, the number of instances in the minority class

is increased by syntactically creating new instances instead of merely replicating

the existing instances. SMOTE generates data in the feature space, and it depends

on introducing new instances based on the nearest neighbors [57]. In this method,

the  new  examples  are  added  near  the  line  segment  that  joins  the  nearest

neighbors of the minority class. The nearest neighbors are selected to create the

instances required for over-sampling [58, 59, 60, 61, 62, 63, 64, 65, 66]. Inspired

by SMOTE, XiChen et al. [67] proposed a sampling method, in which new synthetic

neighborhood  samples  are  generated.  Controlling  the  number  of  generated

samples can improve the balance ratio and promote diversity in the data. Zhou et

al. [68] proposed a cost-sensitive SMOTE for data classi(cid:976)ication. Since the samples

are generated in the feature space, creating a new sample in a nonlinear space can

improve the results after resampling of the minority class [69].

Among  different  variations  of  SMOTE,  ADASYN,  motivated  by  SMOTE,  is  a

popular  oversampling  method,  in  which  the  data  is  synthetically  generated  to

increase the size of the minority class. The size of the generated data is determined

by the density distribution criteria de(cid:976)ined for each example which is an advantage

over SMOTE in that the number of generated data is predetermined [70, 71, 72].

The over-sampling methods are not limited to the ones mentioned in this paper.

These methods can be applied alone or in combination with each other to improve

12

---

<!-- PAGE 13 -->

classi(cid:976)ication results [73].  For example, in this paper, the authors combined the

ADASYN method with a cost-sensitive base model to improve the results in a study

of the transient stability of power systems [74].

Many studies have been carried out to evaluate the effectiveness and ef(cid:976)iciency

of resampling methods, and provide a guideline on selecting the best one for the

speci(cid:976)ic  data  [75,  76,  77,  78].  Figure  4  provides  a  structured  overview  of

resampling methods used in data processing approach. Over the years, different

variations  of  resampling  methods  are  used  in  combination  with  algorithmic

approaches to enhance the prediction accuracy in imbalanced data .

Basic Resampling  
Methods

Random Over - 
sampling 
Random Under - 
sampling

•  Condensed NN 
•  Edited NN 
•  Repeated Edited  
NN 
•  Neighborhood  
Cleaning  
Method

Data Processing Approach 
Resampling Methods

Advanced Resampling  
Methods

Advanced Under - 
sampling Methods 
Under - sampling  
based on Nearest  
Neighbor (NN) 
Tomek’s Link 
One - sided Selection  
Method 
Under - sampling  
Based on Instances  
Hardness Threshold

Advanced Over - 
sampling Methods 
Boot - strap based  
Over - sampling 
Over - sampling based  
on SMOTE 
Over - sampling  
Adaptive Synthetic  
Sampling Method  
( 
ADASYN)

Ensemble 
Methods

Combination of  
Over - sampling and  
Under - sampling  
methods

Figure 4: Data Processing Methods in Imbalanced Learning

3.  Algorithmic Approaches

3.1.  Cost-sensitive Methods

In real-world applications of imbalanced learning, such as cancer diagnosis,  fraud

detection,  or severe weather prediction;  the  misclassi(cid:976)ication  cost  is different  for the

minority class  and  the  majority class,  respectively.  In  imbalanced  learning  where  the

misclassi(cid:976)ication cost of the minority class is more important, cost-sensitive  methods

are used. In cost-sensitive methods, the cost of misclassi(cid:976)ication is known and de(cid:976)ined

in a cost matrix based on the cost associated with a false positive and a false negative.

The goal is to classify the data while minimizing the expected misclassi(cid:976)ication cost of

making  a  false  prediction.  In  imbalanced  learning,  we  can  bene(cid:976)it  from  shifting  the

13

---

<!-- PAGE 14 -->

classi(cid:976)ication algorithm towards further minimizing  the misclassi(cid:976)ication  error of the

minority  class  [79][80].  Cost-sensitive  methods  are  categorized  as  direct  and  meta-

learning methods.

3.1.1.  Direct Methods

In  the  direct  methods,  the  classi(cid:976)iers  are  designed  to  anticipate  different

misclassi(cid:976)ication costs for false positives and false negatives. Cost-sensitive decision

trees are an example of such methods that have improved the classi(cid:976)ication results

by incorporating the cost in the model and aiming to minimize the misclassi(cid:976)ication

cost [81, 82, 83, 84, 85, 86]. In other Cost-sensitive methods, weights are used in the

classi(cid:976)ication algorithm [87]. Studies show that iterative weighting of the samples

can improve the results as well as achieving computational ef(cid:976)iciency [88, 89]. Cost-

sensitive boosting methods have also been used to compare the effectiveness of such

algorithms  on  benchmark  datasets  [90,  91].  Wu  et  al.  [92]  used  a  cost-sensitive

multi-set  feature  learning  on  multiple  samples  constructed  by  partitioning  the

majority class and combining the blocks with the minority class to obtain balanced

datasets. The model is evaluated using benchmark data sets and recommended for

highly  imbalanced  data.  One  of  the  challenges  of  cost-sensitive  methods  is

identifying the misclassi(cid:976)ication costs.

Zhang et al [93] proposed an adaptive differential evolution  to  (cid:976)ind  the  optimal

misclassi(cid:976)ication costs.

3.1.2.  Meta-learning Methods

Meta-learning  methods  are  used  to  convert  cost-insensitive  classi(cid:976)iers  into

cost-sensitive  algorithms  without  making  modi(cid:976)ications  to  the  algorithm  by

thresholding  and  sampling  methods.  Thresholding  models  classify  the  data  by

producing  probability  estimations  using  a  cost-insensitive  algorithm  and  use  a

threshold to classify the data [94, 95, 96]. Thresholding is an effective method that

expands  the  space  and  increases  the  probability  of  classifying  the  instances

associated  with  the  minority  class.  Therefore,  they  often  produce  the  lower

misclassi(cid:976)ication  cost  comparing to  other  classi(cid:976)ication methods [97].  Sampling

meta-learning  methods  modify  the  class  distributions  in  the  dataset,  before

14

---

<!-- PAGE 15 -->

training  the  data  using  a  cost-insensitive  classi(cid:976)ier.  Weighing  is  also  a  type  of

sampling method in which a normalized weight based on the misclassi(cid:976)ication cost

is assigned to the data before classi(cid:976)ication[98, 99]. Cost-sensitive learning is most

effective  when  embedded  in  the  machine  learning  based  model,  categorized  as

Ensemble methods. Ensemble methods are discussed thoroughly in a separate

section.

3.2.  Machine Learning Based Modeling

Various machine learning models have been explored in the attempt to minimize

the  misclassi(cid:976)ication  error  of  the  minority  class  such  as  Logistic  Regression  (LR),

Arti(cid:976)icial Neural Networks (ANNs) [100], Random Forest (RF), Decision

Trees (DT), Naive Bayes (NB), and Gaussian NB, and K-Nearest-Neighbor (KNN),

Support  Vector  Machines  (SVM).Empirical  studies  on  benchmark  data  suggest

different base predictor models [101, 102].

3.2.1.  Tree-based Models

DT is a classi(cid:976)ication algorithm that splits the data set into smaller subsets to

predict the output value of the test data. The conditions by which the data is split

are called leaves, and the decision is known as a branch. The data is split until we

have reached the depth of the tree and no further split is possible. DT is a fast and

simple  algorithm  in  which  the  process  of  classi(cid:976)ication  and  inquiries  made  are

clear [103, 104, 105, 106, 107, 108].

RF is a powerful ensemble  method, which is  an aggregation of less  accurate

predictive models to create a better model. This model is used for regression or

classi(cid:976)ication.  In  RF  classi(cid:976)ication,  decision  trees  are  used  to  introduce

randomness when selecting the suboptimal splits, and the goal is to aggregate as

many uncorrelated trees as possible and improve the accuracy at each step [109,

110, 111, 112, 113].

3.2.2.  Probabilistic Models

NB is a supervised learning method. The (cid:976)irst assumption in this method is that

all the data points are independent of one another. This is an unrealistic yet helpful

assumption  for  training  the  data.  In  this  method,  the  training  data  is  used  to

15

---

<!-- PAGE 16 -->

calculate the probability of each class and the conditional probability of each class

for a given data point. These two pieces of information are used to predict the class

of new data points. Gaussian NB is a modi(cid:976)ication of the NB method, except that

for  the  input  data  in  real  values,  a  Gaussian  distribution  is  assumed  to  make

calculating the probabilities easier [114, 115]

3.2.3.  Neighborhood-based Models

KNN  is  a  simple  yet  powerful  algorithm  that  uses  the  whole  dataset  for

classi(cid:976)ication. To classify a new data point, KNN uses the data points closer to the

designated  point  based  on  their  Euclidean  distance.  Then  it  summarizes  their

output  values  and  assigns  the  result  as  the  label  of  the  new  data  point.  In  KNN,

training, and testing are combined in one step which increases the effectiveness and

ef(cid:976)iciency of the model which is one of the widely used imbalanced learning models.

The papers [116, 117, 118, 119, 120, 121, 122, 123, 124, 125,

126, 127] are representative of those methods.

3.2.4.  Kernel-based Models

Linear and logistic regression are probably the most well-known and widely

used machine learning algorithms. Linear regression is used for predicting values

that are in a range, but logistic regression is appropriate when  we are trying to

predict  categorical  output  values  such  as  binary  classi(cid:976)ication  [128].  LR  is

presented by a non-linear function, and the data is classi(cid:976)ied based on the features

correlated  with  the  output  variable  [129,  130,  131].  To  further  improve  the

traditional LR, Ohsaki et al. [132] proposed a novel confusion-based kernel logistic

regression  that  utilized  a  harmonic  mean  objective  function  to  improve

generalization and classi(cid:976)ication errors of the model. Historically, in the 1950s and

1960s, perceptron algorithms were used for detecting linear relations in the data.

Perceptron  algorithm  is  one  of  the  oldest  machine  learning  algorithms.  In  this

method, we need to associate a weight to the data points and de(cid:976)ine a threshold,

known as bias.  The weights and  the threshold  are extracted  from the  data.  The

weighted sum of the input data is calculated for predicting the output value. The

label is one if the sum is greater than the designated threshold, and zero otherwise.

16

---

<!-- PAGE 17 -->

In perceptron algorithm, the goal is to (cid:976)ind the set of weights that best classi(cid:976)ies

the data. Nieminen et al. [133] demonstrated the use of a single layer perceptron

based on a multi-criteria optimized MLP as the base model. Although perceptron

algorithms  were  useful  for  processing  linear  relations  in  the  data,  developing

ef(cid:976)icient  and  stable  algorithms  for  detecting  nonlinear  relations  was  a  major

challenge for researchers at the time. In the mid-1980s, back-propagation Neural

Networks (NNs) and decision trees revolutionized the (cid:976)ield of non-linear pattern

analysis. In the mid-1990s, kernel-based methods were developed for nonlinear

data  analysis  while  retaining  the  ef(cid:976)iciency  and  stability  of  previous  linear

algorithms. Kernel-based methods apply to a broad  range of data types such as

sequence, text, image, graph, and vectors. They can detect different types of linear

and  non-linear  relations  and  they  are  used  for  correlation,  factor,  cluster,  and

discriminant analysis. Kernel methods have a modular framework, in which (cid:976)irst

the data is processed into a kernel matrix, then the data is analyzed using various

pattern  analysis  algorithms  based  on  the  information  contained  in  the  kernel

matrix [134, 135, 136, 137, 138, 139]. Kernel matrix is obtained from mapping the

data  from  the  input  space  into  a  higher  dimensional  feature  space,  using  a

transformation function denoted as φ(x). One of the challenges in kernel method

is  (cid:976)inding  the  kernel  map,  which  is  computationally  expensive  and  sometimes

impossible, therefore, kernel functions are de(cid:976)ined by the dot product of the points

in  the  input  space.  Using  this  feature,  known  as  the  kernel  trick,  K(xi,yj)  =

φ(xi)T.φ(xj), the data is mapped into the feature space, without explicitly de(cid:976)ining

the map. Different kernel functions have been developed. Kernel methods utilize

a higher dimensional feature space to facilitate accurately classifying the minority

class [140].

Among different classi(cid:976)iers, kernel-based SVM as introduced by Vapnik [141][142]

has been widely used for imbalanced learning. SVM is a family of algorithms that use

kernel methods to solve problems in classi(cid:976)ication and regression [143, 144, 145, 146,

147]. The idea of kernel SVM is to map the data to a higher dimensional feature space

using a linear or nonlinear kernel [148, 149]. Then (cid:976)inding a separating hyperplane to

maximize the margin of separation while minimizing the misclassi(cid:976)ication error by

17

---

<!-- PAGE 18 -->

solving a  quadratic optimization  problem. SVMs are commonly  used for classifying

large  data  sets.  The  data  is  classi(cid:976)ied  based  on  its  location  on  either  side  of  a

hyperplane, which splits the input space. The separating hyperplane is  not unique;

however,  the  best  hyperplane  is  the  one  that  maximizes  the  margin  of  separation

while minimizing the misclassi(cid:976)ication error. Combining cost-sensitive methods with

SVM  is  a  useful  method  for  improving  the  misclassi(cid:976)ication  cost  [150,  151].  Cost-

sensitive  SVM  embedded  into  the  objective  function  can  directly  improve  the

classi(cid:976)ication performance when the feature set and tuning parameters are optimized

[152].  Focusing  on  ROC  and  the  AUC,  Hu  et  al.  [153]  proposed  the  kernel  online

imbalanced  learning  algorithm  that  aims  to  maximize  the  AUC  score  while

maintaining the regularization capabilities of the classi(cid:976)ier. Weighted under-sampling

SVM has improved the classi(cid:976)ication performance of SVM for imbalanced data [154].

Variations of SVM have been used for many applications such as fraud detection,

gene pro(cid:976)iling, weather prediction, etc [155, 156].

3.2.5.  Deep Imbalanced Learning

ANN is a machine learning algorithm developed for separating non-linear data.

In this method, a large number of units known as neurons are connected to form

a multi-layer neural network. The neurons are divided into three types, input units

that  receive  the  information  for  processing,  output  units  that  contain  the

processing results, and the units in between known as hidden units. The ef(cid:976)iciency

of ANNs depends on the input units and their corresponding activation functions,

the network architecture, and the weights of input connections, and the calculated

weights of hidden units updated throughout the learning process.

ANNs apply to various real-world problems as well as imbalanced data [157, 158].

ANNs are studied with cost-sensitive methods to improve misclassi(cid:976)ication cost by

moving the classi(cid:976)ication threshold closer to the majority class, which allows more

instances  to  be  classi(cid:976)ied  as  the  minority  class.  Other  methods  are  imposing

greater weights on the samples associated with the minority class

[159, 160]. Ya-Guan et al. [161] proposed an improved  ANNs method called the

Equilibrium  Mini-batch  Stochastic  Gradient  Descent  that  improves  the  model’s

training convergence error.

18

---

<!-- PAGE 19 -->

In recent years, Extreme Learning Machine (ELM) for NN structures proposed

by  Huang  et  al.  [162]  has  been  applied  extensively  for  real-world  imbalanced

learning problems. Some of  the proposed strategies  based on  ELM are Weighted

ELM [163, 164, 165]. Class-speci(cid:976)ic ELM [166], and Class-speci(cid:976)ic Kernel ELM [167,

168] that have had promising results.  When dealing  with  imbalanced data, deep

learning  algorithms  face  the  same  issues  as  traditional  machine  learning

algorithms,  and  they  fail  to  perform  equally  well  in  both  classes  [169].  Deep

imbalanced learning models are developed to address the issue of imbalanced data

in image recognition and computer vision [170? , 171].

Lin  et al.  [172] proposed a  hybrid sampling method  to  remove  the  between

class data points and guide the network to improve the classi(cid:976)ication results [173].

Dong et al.[174] developed a deep learning model to classify imbalanced datasets

by imposing a class recti(cid:976)ication loss as a regularization parameter to discover the

boundaries in the minority class and reduce the effect of the majority class on the

model. Bao et al. [175] introduced a deep learning framework to balance the data

in a deeply transformed latent space. The superiority of this model is that feature

learning,  balancing,  and  discriminative  learning  are  conducted  simultaneously

and it performs effectively on multi-classi(cid:976)ication problems. A cost-sensitive deep

NN proposed by Khan et al. [176] is a robust feature representation of both classes.

Therefore, it can have improved predictive capability. Lin et al. [177] proposed a

deep reinforcement learning model based on the reward function speci(cid:976)ied for the

minority and the majority class.

3.2.6.  Ensemble Methods

Ensemble  methods  is  an  approach  in  machine  learning  that  utilizes  multiple

machine learning based models to improve predictive accuracy. A group of ensemble

methods  is  formed  based  on  Bootstrap  Aggregating  (Bagging)  in  which  several

bootstrapped subsamples are created and trained using a  base  model [178,  179].

Later the model aggregates the decision tree models to create the optimal predicting

ensemble  method  [180].  Random  forest  models  are  another  type  of  ensemble

method which is a variation of Bagging, in which splitting the tree based on different

features  creates  a  more  accurate  model.  For  imbalanced  learning,  cost-sensitive

19

---

<!-- PAGE 20 -->

decision trees are introduced [181]. Another ensemble method called CSRoulette is

introduced that improves the performance by producing samples of different sizes

based on a cost-sensitive model, combined with Bagging [182]. An empirical study

of  ensemble  methods  and  meta-learning  methods  suggests  that  although  these

methods are effective for binary classi(cid:976)ication of imbalanced data, they might not

perform  well  on  multi-class  classi(cid:976)ication  problems.  For  multi-classi(cid:976)ication

problems,  a  combination  of  LR  and  KNN  is  used.  In  the  LR  part  of  the  model,  an

ensemble of Bagging  and Boosting  methods  has resulted  in  a  promising  outcome

[183]. Variations of the Boosting algorithms such as Adaptive Boosting (Adaboost)

have shown promising results

in classifying imbalanced data [184]. A comparison of various ensemble methods

suggests that combining data preprocessing approaches, such as RUS with Bagging

or  Boosting  methods  can  result  in  higher  performance  [185].  An  ensemble  of

random subsampling  with RF has reasonable  performance [186,  187]. Modifying

the  objective

function

to  anticipate  different

factors

to  minimize

the

misclassi(cid:976)ication error in combination with evolutionary under-sampling methods

is an example of ensemble  methods aiming to  improve the results of imbalanced

learning  [188].  Ensemble  methods  with  multi-objective  optimization  function

provide  powerful  algorithms  for  imbalanced  learning  [189,  190].  Ensemble

methods are also effective for highly imbalanced data [191]. For image recognition,

ensemble  deep  imbalanced  learning  with  a  focus  on  resampling  the  data,  and  a

weighted loss function has improved the image classi(cid:976)ication results [192]. Wu et

al. [193] used a genetic algorithm approach with a deep imbalanced learning model

to  optimize  oversampling  the  minority  class.  Despite  being  able  to  improve  the

classi(cid:976)ication results, ensemble methods are computationally complex. A structured

overview of the methods used in algorithmic approach is presented in Figure 5.

20

---

<!-- PAGE 21 -->

4.  Applications

Figure 5: Algorithmic Approaches in Imbalanced Learning

Classi(cid:976)ication  of  imbalanced  data  is  a  challenging  task  and  it  is  one  of  the 
popular research problems with many applications in the real world [194, 195]. 
In  this  section  we  have  presented  some  of  the  highly  impactful  imbalanced 
learning  problems,  however,  the  applications  of  imbalanced  learning  are  not 
limited  to  the  mentioned  examples.  Figure  6  provides  an  overview  of  areas  in 
which imbalanced learning is used.

Cybersecurity

Infrastructure and Industrial 
Systems Management

Bioengineering and 
Bioinformatics

Software Management 
and Malware Detection

Natural Disaster 
and Rare Event  
Prediction

Energy Management

Risk Assessment

Emergency and Resource 
Management

Other Areas

Computer Vision

Behavior  
Management

Figure 6: Applications of Imbalanced Learning

Financial  
Management

Business  
Management

21

---

<!-- PAGE 22 -->

4.1.  Risk Assessment in Business and Finance

In business analytics, bankruptcy prediction is an imbalanced learning problem.

Gnip  et  al.  [196]  used  multiple  ensemble  methods  to  accurately  predict  the  data

collected from medium-sized enterprises in the Slovak Republic [197]. In banking,

credit scoring and evaluating the potential risk posed by applicants’ unpaid loans is

an important issue, and due to frequency, it is an example of imbalanced data [198,

199, 200]. For example, detecting fraudulent transactions using ensemble methods

[201]  and  evaluating  loan  and  credit  applications  can  bene(cid:976)it  from  imbalanced

learning  to  support  the  decision-making  process.  Approval  or  rejection  of  loans

based  on  the  applicant’s  credit  history  is  an  imbalanced  learning  problem  with

unpaid loan creating the minority class [202, 203, 204].

Fraud detection is one of the major applications of imbalanced learning algorithms.

Bauder et al. [205] compared the performance of different resampling approaches

on highly imbalanced data from Medicare to detect fraudulent cases.

4.2.  Behavior Management

Imbalanced learning is also applicable to the data collected from Socioeconomic

systems. For example, Orooji et al. [206] predicted the rate of high school dropout

in Louisiana, US., which has negative impacts on the well-being of society, and Zheng

et al. [207] explored a short tree-based adaptive classi(cid:976)ication test to assess the risk

factors for juvenile delinquency.

4.3.  Cybersecurity and Software Management

In cybersecurity, spam and software defect detection is an example of imbalanced

learning [208, 209, 210, 211]. Chen et al. [212] proposed an ensemble model based

on  Choquet  fuzzy  integral  with an  improved  SMOTE resampling  technique  for  bug

report  identi(cid:976)ication  that  can  prevent  damage  to  software.  Developing  effective

Intrusion Detection systems (IDS) is essential to cybersecurity [213]. Karatas et al.

[214] used the SMOTE resampling method to improve IDS performance. Feng et al.

[215] tackled the issue of imbalanced data in IDS classi(cid:976)ication using a cost-sensitive

feature engineering method based on General Vector Machine(GVM) and Binary Ant

Lion Optimizer. Zheng et al. [216] used a modi(cid:976)ied SVM to improve of(cid:976)line signature

22

---

<!-- PAGE 23 -->

veri(cid:976)ication systems. Pang et al. [217] used an ensemble of SMOTE and SVM to detect

malicious apps for android

users.

4.4.  Natural Disasters and Emergency Management

An  impactful  application  of  imbalanced  learning  is  predicting  rare  natural

disasters. Fernandez-Gomez et al. [218] studied the use of ensemble methods on

predicting rare large magnitude earthquakes with a horizon of prediction of (cid:976)ive

days  in  Chile.  Seismic  capability  evaluation  of  buildings  is  also  an  imbalanced

learning  problem  in  earthquake  engineering  [219].  Predicting  severe  weather

events  such  as  tornado  is  an  imbalanced  learning  problem  in  meteorology  and

data mining [220, 221, 222]. Optimizing the available resources in urgent care is

important in times of crisis. An ensemble method consisting of Bagging and DT

can  improve  the  prediction  results  for  patient  readmission  to  the  emergency

department of a hospital in Chile [223].

4.5.  Bio-informatics and Bio-engineering

Medical diagnosis is an example of imbalanced learning in the (cid:976)ield of bioinformatics

and bioengineering. Zhang et al. [224], explored the use of an ensemble method of RUS

with  K-means  and  SVM  to  improve  the  diagnosis  accuracy.  Zheng  et  al.  [225]  used  a

Convolutional Neural Network (CNN) to detect exudate in optic images, that if detected

correctly can prevent diabetic retinopathy and blindness. Jeong et al. [226] addressed

the issue of multi-classi(cid:976)ication of imbalanced kidney data. In this paper, the glomerular

rate is de(cid:976)ined as target to diagnose chronic kidney disease. The goal is to classify the

data  into  (cid:976)ive  stages  using  four  methods  of  multinomial  LR,  and  ordinal  LR,  RF,  and

Autoencoder (AE). The comparison of the four models suggests that AE provides better

performance and is recommended for similar problems. Farhadi et al. [227] used a deep

transfer  learning  model  on  constructing  medical  image  data  to  evaluate  the  model’s

ef(cid:976)iciency in diagnosing high-grade  breast cancer. A breast cancer diagnosis has  been

improved  by  advanced  imbalanced  learning  methods  introduced  in  the  past  decade

[228,  229,  230].  Other  cost-sensitive  methods  have  also  been  used  to  improve  the

classi(cid:976)ication accuracy of medical diagnosis [231, 232]. Deng et al. [233] have introduced

23

---

<!-- PAGE 24 -->

a  dynamic  clustering  method  that  iteratively  adjusts  the  cluster  based  on  the  weight

changes  in  the  cluster.  This  algorithm  is  evaluated  using  gene  expression  cancer

diagnosis data and applies to biological and cyber-physical systems. A deep imbalanced

learning  framework  applies  to  different  (cid:976)ields  such  as  active  balancing  in  biomedical

data

[234].

4.6.  Computer Vision

Image processing and recognizing facial images and other attributes in detail

is a challenging task in computer vision, and the dif(cid:976)iculties escalate when the data

is imbalanced [235, 236, 237]. Various ensemble methods have been explored to

classify multimedia data [238]. Pouyanfar et al. [239] proposed an ensemble deep

learning framework based on the performance of SVM classi(cid:976)iers on deep feature

sets  which is evaluated using multi-media data for semantic event detection. In

terms of application, different packages exist that can be used to implement the

models in Python, R, or other scripting languages [240].

Future Research Trends

Learning from imbalanced data is one of the challenging tasks in data mining.

However, it gets even more dif(cid:976)icult when it is combined with other issues. Different

studies have been carried out to explore strategies for speci(cid:976)ic issues of the minority

class,  such  as  highly  imbalanced  cases,  noisy  data  [4],  outliers,  sparse  data  [241,

242]  and  the  problem  of  imbalanced  distribution  within  the  minority  class  [243,

244].  Another  category  of  imbalanced  learning  problems  is  multi-class  problems

that  require  more  advanced  techniques  to  deal  with  imbalanced  data  [245,  246].

Some  of  the  proposed  strategies  such  as  weighted  extreme  learning  machines,

weighted  support  vector  machines  [247],  and  sequential  ensemble  learning  have

been  relatively  effective  in  the  case  of  highly  imbalanced  data  [248,  249,  250].

However, these methods are computationally complex and further improvement is

desired. A real-world application of imbalanced learning is time series analysis with

imbalanced  and  skewed  data.  This  is  particularly  challenging  due  to  the  high

dimension  of  the  data  and  underlying  correlations  within  the  data,  and  further

24

---

<!-- PAGE 25 -->

exploration is desired [251, 252, 253]. Imbalanced learning is an often over-looked

issue in Online Learning of streaming data [254, 255].  Different methods such as

cost-sensitive methods have been explored in various studies evaluated  based  on

the imbalanced learning metrics [256].However,  extensive research is  required  to

address the issues in online imbalanced learning

of large scale data. The last but not least is the problem of imbalanced Learning in

distributed framework [257, 258]. Decentralized data centers often cause skewed

class  distribution  in  different  classes.  Distributed  learning  has  gained  more

attention in the past few years and tackling the issue of imbalanced data in such

framework is essential.

Conclusion

Extensive  research  has  been  carried  out  to  improve  and  identify  the  best

approaches for imbalanced data in different (cid:976)ields from cyber-security to business

analytic and bio-informatics. In this paper, we have provided a review of the wide

range  of  methods  applied  to  imbalanced  data  from  a  technical  perspective.

Examples of real-world applications have also been reviewed. We have collected

and reviewed the papers published in peer-reviewed journals from 2000 to 2020

to  understand  the  trends  and  advances  in  learning  from  imbalanced  data  and

provide insights for future research trends in this highly anticipated (cid:976)ield.

References

[1]  S.  M.  Abd  Elrahman,  A.  Abraham,  A  review  of  class  imbalance  problem,

Journal of Network and Innovative Computing 1 (2013) (2013) 332–340. [2] V.

Babar, R. Ade, A review on imbalanced learning methods, 2015.

[3]

J. Gu, Y. Zhou, X. Zuo, Making class bias useful: A strategy of learning from

imbalanced  data,

in:  International  Conference  on  Intelligent  Data

Engineering and Automated Learning, Springer, 2007, pp. 287–295.

25

---

<!-- PAGE 26 -->

[4]  T.  M.  Khoshgoftaar,  J.  Van  Hulse,  A.  Napolitano,  Comparing  boosting  and

bagging techniques with noisy and imbalanced data, IEEE Transactions on

Systems, Man, and Cybernetics-Part A: Systems and Humans 41 (3) (2010)

552–568.

[5]  A. Sonak, R. Patankar, A survey on methods to handle imbalance dataset,

Int. J. Comput. Sci. Mobile Comput 4 (11) (2015) 338–343.

[6]  N. Japkowicz, S. Stephen, The class imbalance problem: A systematic study,

Intelligent data analysis 6 (5) (2002) 429–449.

[7]  A. Fern´andez, S. del R´ıo, N. V. Chawla, F. Herrera, An insight into imbalanced

big  data  classi(cid:976)ication:  outcomes  and  challenges,  Complex  &  Intelligent

Systems 3 (2) (2017) 105–120.

[8]  B. Krawczyk, Learning  from imbalanced data: open challenges and  future

directions, Progress in Arti(cid:976)icial Intelligence 5 (4) (2016) 221–232.

[9]  G.  E.  Batista,  R.  C.  Prati,  M.  C.  Monard,  A  study  of  the  behavior  of  several

methods  for  balancing  machine  learning  training  data,  ACM  SIGKDD

explorations newsletter 6 (1) (2004) 20–29.

[10]  T. R. Hoens, N. V. Chawla, Imbalanced datasets: from sampling to classi(cid:976)iers,

Imbalanced learning: Foundations, algorithms, and applications (2013) 43–

59.

[11]  N. V. Chawla, Data mining for imbalanced datasets: An overview, in:

Data mining and knowledge discovery handbook, Springer, 2009, pp. 875–

886.

[12]  V.  Ganganwar,  An  overview  of  classi(cid:976)ication  algorithms  for  imbalanced

datasets,  International  Journal  of  Emerging  Technology  and  Advanced

Engineering 2 (4) (2012) 42–47.

[13]  G.  Haixiang,  L.  Yijing,  J.  Shang,  G.  Mingyun,  H.  Yuanyue,  G.  Bing,  Learning

from  class-imbalanced  data:  Review  of  methods  and  applications,  Expert

Systems with Applications 73 (2017) 220–239.

26

---

<!-- PAGE 27 -->

[14]  A.  Fern´andez,  S.  Garc´ıa,  M.  Galar,  R.  C.  Prati,  B.  Krawczyk,  F.  Herrera,

Learning from imbalanced data streams, in: Learning from imbalanced data

sets, Springer, 2018, pp. 279–303.

[15]  Y. Sun, A. K. Wong, M. S. Kamel, Classi(cid:976)ication of imbalanced data: A review,

International  journal  of  pattern  recognition  and  arti(cid:976)icial  intelligence  23

(04) (2009) 687–719.

[16]  A.  Luque,  A.  Carrasco,  A.  Mart´ın,  A.  de  las  Heras,  The  impact  of  class

imbalance  in  classi(cid:976)ication  performance  metrics  based  on  the  binary

confusion matrix, Pattern Recognition 91 (2019) 216–231.

[17]  D. J. Hand, Measuring classi(cid:976)ier performance: a coherent alternative to the

area under the roc curve, Machine learning 77 (1) (2009) 103–123.

[18]  M.  Bekkar,  H.  K.  Djemaa,  T.  A.  Alitouche,  Evaluation  measures  for  models

assessment over imbalanced data sets, J Inf Eng Appl 3 (10)

(2013).

[19]  C. Ferri, J. Hern´andez-Orallo, R. Modroiu, An experimental comparison of

performance measures for classi(cid:976)ication, Pattern Recognition Letters 30 (1)

(2009) 27–38.

[20]  M.  Hossin,  M.  Sulaiman,  A  review  on  evaluation  metrics  for  data

classi(cid:976)ication  evaluations,  International

Journal  of  Data  Mining  &

Knowledge Management Process 5 (2) (2015) 1.

[21]  M.  Fatourechi,  R.  K.  Ward,  S.  G.  Mason,  J.  Huggins,  A.  Schl¨ogl,  G.  E.  Birch,

Comparison  of  evaluation  metrics  in  classi(cid:976)ication  applications  with

imbalanced datasets, in: 2008 Seventh International Conference on Machine

Learning and Applications, IEEE, 2008, pp. 777–782.

[22]  D. R. Musicant, V. Kumar, A. Ozgur, et al., Optimizing f-measure with support

vector machines., in: FLAIRS conference, 2003, pp. 356–360.

27

---

<!-- PAGE 28 -->

[23]  S. Boughorbel, F. Jarray, M. El-Anbari, Optimal classi(cid:976)ier for imbalanced data

using  matthews  correlation  coef(cid:976)icient  metric,  PloS  one  12  (6)  (2017)

e0177678.

[24]  Y.  Rizk,  N.  Hajj,  N.  Mitri,  M.  Awad,  Deep  belief  networks  and  cortical

algorithms: A comparative study for supervised classi(cid:976)ication, Applied

Computing and Informatics 15 (2) (2019) 81–93.

[25]  Y.  S.  Aurelio,  G.  M.  de  Almeida,  C.  L.  de  Castro,  A.  P.  Braga,  Learning  from

imbalanced  data  sets  with  weighted  cross-entropy  function,  Neural

Processing Letters 50 (2) (2019) 1937–1949.

[26]  C.  Li,  H.  Li,  A  modi(cid:976)ied  short  and  fukunaga  metric  based  on  the  attribute

independence  assumption,  Pattern  Recognition  Letters  33  (9)  (2012)

1213–1218.

[27]  A. P. Bradley, The use of the area under the roc curve  in the evaluation of

machine  learning  algorithms,  Pattern  recognition  30  (7)  (1997)  1145–

1159.

[28]  C. X. Ling, J. Huang, H. Zhang, et al., Auc: a statistically consistent and more

discriminating measure than accuracy, in: Ijcai, Vol. 3, 2003, pp. 519–524.

[29]  N. Thai-Nghe, Z. Gantner, L. Schmidt-Thieme, A new evaluation measure for

learning from imbalanced data, in: The 2011 International Joint Conference

on Neural Networks, IEEE, 2011, pp. 537–542.

[30]  L. A.

Jeni,

Torre,  Facing

F.

J. 
imbalanced

Cohn,  F.

De

La

data–recommendations  for  the  use  of  performance  metrics,  in:  2013

Humaine  association  conference  on  affective  computing  and  intelligent

interaction, IEEE, 2013, pp. 245–251.

[31]  C.  Phua,  D.  Alahakoon,  V.  Lee,  Minority  report  in  fraud  detection:

classi(cid:976)ication  of  skewed  data,  Acm  sigkdd  explorations  newsletter  6  (1)

(2004) 50–59.

28

---

<!-- PAGE 29 -->

[32]  D.  A.  Cieslak,  N.  V.  Chawla,  A.  Striegel,  Combating  imbalance  in  network

intrusion datasets., in: GrC, 2006, pp. 732–737.

[33]  C.  Sarada,  M.  SathyaDevi,  Imbalanced  big data  classi(cid:976)ication  using  feature

selection under-sampling, CVR Journal of Science and Technology 17 (1)

(2019) 78–82.

[34]  A. Liu, J. Ghosh, C. E. Martin, Generative oversampling for mining imbalanced

datasets., in: DMIN, 2007, pp. 66–72.

[35]  A.  More,  Survey  of  resampling  techniques  for  improving  classi(cid:976)ication

performance  in  unbalanced  datasets,  arXiv  preprint  arXiv:1608.06048

(2016).

[36]  M. S. Shelke, P. R. Deshmukh, V. K. Shandilya, A review on imbalanced data

handling  using  undersampling  and  oversampling  technique,  Int  J  Recent

Trends in Eng & Res 3 (2017) 444–449.

[37]  J. Laurikkala, Improving identi(cid:976)ication of dif(cid:976)icult small classes by balancing

class  distribution,  in:  Conference  on  Arti(cid:976)icial  Intelligence  in  Medicine  in

Europe, Springer, 2001, pp. 63–66.

[38]  M. Koziarski, 
  data

Radial-based

undersampling  for

imbalanced

classi(cid:976)ication, Pattern Recognition 102 (2020) 107262.

[39]  C. Wang,  Y. Yang,  Nearest neighbor with double neighborhoods

algorithm  for  imbalanced  classi(cid:976)ication.,  International  Journal  of  Applied

Mathematics 50 (1) (2020).

[40]  S.  S.  Alduayj,  K.  Rajpoot,  Predicting  employee  attrition  using  machine

learning, in: 2018 International Conference on Innovations in Information

Technology (IIT), IEEE, 2018, pp. 93–98.

[41]  A.  Onan,  Consensus  clustering-based  undersampling  approach

to

imbalanced learning, Scienti(cid:976)ic Programming 2019 (2019).

29

---

<!-- PAGE 30 -->

[42]  G. E. Batista, A. C. Carvalho, M. C. Monard, Applying one-sided selection to

unbalanced  datasets,  in:  Mexican  International  Conference  on  Arti(cid:976)icial

Intelligence, Springer, 2000, pp. 315–325.

[43]  S.  Cateni,  V. 
resampling

Colla,  M.

Vannucci,

A

method for

imbalanced datasets in binary classi(cid:976)ication tasks for real-world problems,

Neurocomputing 135 (2014) 32–41.

[44]  B.  W.  Yap,  K.  Abd  Rani,  H.  A.  Abd  Rahman,  S.  Fong,  Z.  Khairudin,  N.  N.

Abdullah,  An  application  of  oversampling,  undersampling,  bagging  and

boosting  in  handling  imbalanced  datasets,  in:  Proceedings  of  the  (cid:976)irst

international  conference  on  advanced  data  and  information  engineering

(DaEng-2013), Springer, 2014, pp. 13–22.

[45]  X.-Y. Liu, J. Wu, Z.-H. Zhou, Exploratory undersampling for class-imbalance

learning,  IEEE  Transactions  on  Systems,  Man,  and  Cybernetics,  Part  B

(Cybernetics) 39 (2) (2008) 539–550.

[46]  S.  J.  Dattagupta,  A performance comparison  of  oversampling  methods  for

data generation in imbalanced learning tasks, Ph.D. thesis (2018).

[47]  Z.  Gong,  H.  Chen,  Model-based  oversampling  for  imbalanced  sequence

classi(cid:976)ication, in: Proceedings of the 25th ACM International on Conference

on Information and Knowledge Management, 2016, pp. 1009–1018.

[48]  G. Goel, L. Maguire, Y. Li, S.  McLoone,  Evaluation of sampling  methods for

learning from imbalanced data, in: International Conference on Intelligent

Computing, Springer, 2013, pp. 392–401.

[49]  A. Gosain, S. Sardana, Handling class imbalance problem using oversampling

techniques:  A  review,  in:  2017  International  Conference  on  Advances  in

Computing, Communications and Informatics (ICACCI), IEEE, 2017, pp. 79–

85.

30

---

<!-- PAGE 31 -->

[50]  R. Malhotra, J. Jain, Handling imbalanced data using  ensemble learning in

software defect prediction, in: 2020 10th International Conference on Cloud

Computing, Data Science & Engineering (Con(cid:976)luence), IEEE, 2020, pp. 300–

304.

[51]  Z. Wu, W. Lin, Y. Ji, An integrated ensemble learning model for imbalanced

fault diagnostics and prognostics, IEEE Access 6 (2018)

8394–8402.

[52]  Q. Wang, Y. Zhou, W. Zhang, Z. Tang, X. Chen, Adaptive sampling

using self-paced learning for imbalanced cancer data pre-diagnosis, Expert

Systems with Applications 152 (2020) 113334.

[53]  H. Guo, J. Zhou, C.-A. Wu, Imbalanced learning based on data-partition and

smote, Information 9 (9) (2018) 238.

[54]  P.  Skryjomski,  B.  Krawczyk,  In(cid:976)luence  of  minority  class  instance  types  on

smote imbalanced data  oversampling, in:  (cid:976)irst  international  workshop  on

learning with imbalanced domains: theory and applications, 2017, pp. 7–21.

[55]  M.  B.  Lyons,  D.  A.  Keith,  S.  R.  Phinn,  T.  J.  Mason,  J.  Elith,  A  comparison  of

resampling  methods  for  remote  sensing  classi(cid:976)ication  and  accuracy

assessment, Remote Sensing of Environment 208 (2018) 145–153.

[56]  W.  Zhang,  R.  Ramezani,  A.  Naeim,  Wotboost:  Weighted  oversampling

technique in boosting for imbalanced learning, in: 2019 IEEE

International  Conference  on  Big  Data  (Big  Data),  IEEE,  2019,  pp.  2523–

2531.

[57]  A. Fern´andez,  S. Garcia, F. Herrera, N. V. Chawla, Smote  for  learning  from

imbalanced data: progress and challenges, marking the 15-year anniversary,

Journal of arti(cid:976)icial intelligence research 61 (2018) 863–905.

[58]  Y. Xie, T. Zhang, Imbalanced learning for fault diagnosis problem of rotating

machinery based on generative adversarial networks, in: 2018 37th Chinese

Control Conference (CCC), IEEE, 2018, pp. 6017–6022.

31

---

<!-- PAGE 32 -->

[59]  N. V. Chawla,

K. W. Bowyer,

L. O. Hall,

W. P. Kegelmeyer,

Smote:  synthetic  minority  over-sampling  technique,  Journal  of  arti(cid:976)icial

intelligence research 16 (2002) 321–357.

[60]  X.-L.  Yang,  D.  Lo,  X.  Xia,  Q.  Huang,  J.-L.  Sun,  High-impact  bug  report

identi(cid:976)ication with imbalanced learning strategies, Journal of Computer

Science and Technology 32 (1) (2017) 181–198.

[61]  M.  M.  Rahman,  D.  N.  Davis,  Addressing  the  class  imbalance  problem  in

medical datasets, International Journal of Machine Learning and Computing

3 (2) (2013) 224.

[62]  W.  Deng,  L.  Deng,  J.  Liu,  J.  Qi,  Sampling  method  based  on  improved  c4.  5

decision tree and its application in prediction of telecom customer churn,

International  Journal  of  Information  Technology  and  Management  18  (1)

(2019) 93–109.

[63]  S.  Hukerikar,  A.  Tumma,  A.  Nikam,  V.  Attar,  Skewboost:  An  algorithm  for

classifying imbalanced datasets, in: 2011 2nd International Conference on

Computer  and  Communication  Technology  (ICCCT-2011),  IEEE,  2011,  pp.

46–52.

[64]  H.  Han,  W.-Y.  Wang,  B.-H.  Mao,  Borderline-smote:  a  new  over-sampling

method  in  imbalanced  data  sets  learning,  in:  International  conference  on

intelligent computing, Springer, 2005, pp. 878–887.

[65]  Z.  Hosenie,  R.  Lyon,  B.  Stappers,  A.  Mootoovaloo,  V.  McBride,  Imbalance

learning  for  variable  star  classi(cid:976)ication,  Monthly  Notices  of  the  Royal

Astronomical Society 493 (4) (2020) 6050–6059.

[66]  N. V. Chawla, A. Lazarevic, L. O. Hall, K. W. Bowyer, Smoteboost: Improving

prediction  of  the  minority  class  in  boosting,  in:  European  conference  on

principles of data mining and knowledge discovery, Springer, 2003, pp. 107–

119.

[67]  Z. Chen, T. Lin, X. Xia, H. Xu, S. Ding, A synthetic neighborhood

32

---

<!-- PAGE 33 -->

generation based ensemble learning for the imbalanced data classi(cid:976)ication,

Applied Intelligence 48 (8) (2018) 2441–2457.

[68]  C.  Zhou,  B.  Liu,  S.  Wang,  Cmo-smote:  misclassi(cid:976)ication  cost  minimization

oriented  synthetic  minority  oversampling  technique  for  imbalanced

learning,  in:  2016  8th  International  Conference  on  Intelligent  Human-

Machine Systems and Cybernetics (IHMSC), Vol. 2, IEEE, 2016, pp. 353–358.

[69]  T. Zhang, X. Yang, G-smote: A gmm-based synthetic minority oversampling

technique  for  imbalanced  learning,  arXiv  preprint  arXiv:1810.10363

(2018).

[70]  B.  Tang,  H.  He,  Kerneladasyn:  Kernel  based  adaptive  synthetic  data

generation for imbalanced learning, in: 2015 IEEE Congress on Evolutionary

Computation (CEC), IEEE, 2015, pp. 664–671.

[71]  S.  Sharma,  C.  Bellinger,  B.  Krawczyk,  O.  Zaiane,  N.  Japkowicz,  Synthetic

oversampling  with  the  majority  class:  A  new  perspective  on  handling

extreme imbalance, in: 2018 IEEE International Conference on Data Mining

(ICDM), IEEE, 2018, pp. 447–456.

[72]  H.  He,  Y.  Bai,  E.  A.  Garcia,  S.  Li,  Adasyn:  Adaptive  synthetic  sampling

approach  for  imbalanced  learning,  in:  2008  IEEE  international  joint

conference  on  neural  networks  (IEEE  world  congress  on  computational

intelligence), IEEE, 2008, pp. 1322–1328.

[73]  J.  Burez,  D.  Van  den  Poel,  Handling  class  imbalance  in  customer  churn

prediction, Expert Systems with Applications 36 (3) (2009) 4626–4636.

[74]  B. Tan, J. Yang, Y. Tang, S. Jiang, P. Xie, W. Yuan, A deep imbalanced learning

framework for transient stability assessment of power system, IEEE Access

7 (2019) 81759–81769.

[75]  G. M. Weiss, K. McCarthy, B. Zabar, Cost-sensitive learning vs. sampling:

Which is  best  for  handling  unbalanced  classes  with  unequal  error costs?,

Dmin 7 (35-41) (2007) 24.

33

---

<!-- PAGE 34 -->

[76]  C. Drummond, R. C. Holte, et al., C4. 5, class imbalance, and cost sensitivity:

why under-sampling beats over-sampling, in: Workshop on learning from

imbalanced datasets II, Vol. 11, Citeseer, 2003, pp. 1–8.

[77]  A.  O.  DURAHIM,  Comparison  of  sampling  techniques  for  imbalanced˙

learning, Y¨onetim Bili¸sim Sistemleri Dergisi 2 (2) (2016) 181–191.

[78]  P.  Poshala,  et  al.,  Why  oversample  when  undersampling  can  do  the  job?,

Texas Instruments, Dallas, TX, USA, Application Rep. SLAA594A (2013).

[79]  C. Elkan, The foundations of cost-sensitive learning, in: International joint

conference on arti(cid:976)icial intelligence, Vol. 17, Lawrence Erlbaum Associates

Ltd, 2001, pp. 973–978.

[80]  P.  Domingos,  Metacost:  A  general  method  for  making  classi(cid:976)iers  cost-

sensitive, in: Proceedings of the (cid:976)ifth ACM SIGKDD international conference

on Knowledge discovery and data mining, 1999, pp. 155–164.

[81]  S.  Lomax,  S.  Vadera,  A  survey  of  cost-sensitive  decision  tree  induction

algorithms, ACM Computing Surveys (CSUR) 45 (2) (2013) 1–35.

[82]  C.  X.  Ling,  V.  S.  Sheng,  Q.  Yang,  Test  strategies  for  cost-sensitive  decision

trees, IEEE Transactions on Knowledge and Data Engineering 18 (8) (2006)

1055–1067.

[83]  Y.  Sahin,  S.  Bulkan,  E.  Duman,  A  cost-sensitive  decision  tree  approach  for

fraud  detection,  Expert  Systems  with  Applications  40  (15)  (2013)  5916–

5923.

[84]  J. Li, X. Li, X. Yao, Cost-sensitive classi(cid:976)ication with genetic programming, in:

2005  IEEE  congress  on  evolutionary  computation,  Vol.  3,  IEEE,  2005,  pp.

2114–2121.

[85]  A. Freitas, A. Costa-Pereira, P. Brazdil, Cost-sensitive decision trees applied

to  medical  data,  in:  International  Conference  on  Data  Warehousing  and

Knowledge Discovery, Springer, 2007, pp. 303–312.

34

---

<!-- PAGE 35 -->

[86]  J.  V.  Davis,  J.  Ha,  C.  J.  Rossbach,  H.  E.  Ramadan,  E.  Witchel,  Cost-sensitive

decision tree learning for forensic classi(cid:976)ication, in:

European Conference on Machine Learning, Springer, 2006, pp. 622–629.

[87]  B.  Zadrozny,  J.  Langford,  N.  Abe,  Cost-sensitive

learning  by  cost-

proportionate example weighting, in: Third IEEE international conference

on data mining, IEEE, 2003, pp. 435–442.

[88]  N.  Abe,  B. Zadrozny,  J.  Langford,  An iterative  method  for  multi-class  cost-

sensitive learning, in: Proceedings of the tenth ACM SIGKDD international

conference on Knowledge discovery and data mining, 2004, pp. 3–11.

[89]  X.-Y.  Liu,  Z.-H.  Zhou,  The  in(cid:976)luence  of  class  imbalance  on  cost-sensitive

learning:  An  empirical  study,  in:  Sixth  International  Conference  on  Data

Mining (ICDM’06), IEEE, 2006, pp. 970–974.

[90]  Q.-Y.  Yin,  J.-S.  Zhang,  C.-X.  Zhang,  S.-C.  Liu,  An  empirical  study  on  the

performance of cost-sensitive  boosting algorithms with different levels of

class imbalance, Mathematical Problems in Engineering 2013 (2013).

[91]  Y.  Sun,  M.  S.  Kamel,  Y.  Wang,  Boosting  for  learning  multiple  classes  with

imbalanced  class  distribution,  in:  Sixth  International  Conference  on  Data

Mining (ICDM’06), IEEE, 2006, pp. 592–602.

[92]  F. Wu, X.-Y. Jing, S. Shan, W. Zuo, J.-Y. Yang, Multiset feature

learning  for  highly  imbalanced  data  classi(cid:976)ication,  in:  Thirty-First  AAAI

Conference on Arti(cid:976)icial Intelligence, 2017.

[93]  C. Zhang, K. C. Tan, H. Li, G. S. Hong, A cost-sensitive deep

belief  network  for  imbalanced  classi(cid:976)ication,  IEEE  transactions  on  neural

networks and learning systems 30 (1) (2018) 109–122.

[94]  N. A. Verdikha, T. B. Adji, A. E. Permanasari, Study of undersampling method:

Instance  hardness  threshold  with  various  estimators  for  hate  speech

classi(cid:976)ication, IJITEE (International Journal of Information

Technology and Electrical Engineering) 2 (2) (2018) 39–44.

35

---

<!-- PAGE 36 -->

[95]  Y. Jiang, B. Cukic, Misclassi(cid:976)ication cost-sensitive fault prediction models, in:

Proceedings  of  the  5th  international  conference  on  predictor  models  in

software engineering, 2009, pp. 1–10.

[96]  M. E. Bezerra, A. L. Oliveiray, P. J. Adeodatoz, Predicting software defects: A

cost-sensitive  approach,  in:  2011  IEEE  International  Conference  on

Systems, Man, and Cybernetics, IEEE, 2011, pp.

2515–2522.

[97]  V. S. Sheng, C. X. Ling, Thresholding for making classi(cid:976)iers cost-sensitive, in:

AAAI, Vol. 6, 2006, pp. 476–481.

[98]  K.  M.  Ting,  An  instance-weighting  method  to  induce  cost-sensitive  trees,

IEEE Transactions on Knowledge and Data Engineering 14 (3) (2002) 659–

665.

[99]  H.  Zhao,  Instance  weighting  versus  threshold  adjusting  for  cost-sensitive

classi(cid:976)ication, Knowledge and Information Systems 15 (3) (2008) 321–334.

[100] M. A. Mazurowski, P. A. Habas, J. M. Zurada, J. Y. Lo, J. A. Baker, G. D. Tourassi,

Training neural network classi(cid:976)iers for medical decision making: The effects

of imbalanced datasets on classi(cid:976)ication performance, Neural networks 21

(2-3) (2008) 427–436.

[101] A. Shen, R. Tong, Y. Deng, Application of classi(cid:976)ication models on credit card

fraud detection, in: 2007 International conference on service systems and

service management, IEEE, 2007, pp. 1–4.

[102] R.  Caruana,  A.  Niculescu-Mizil,  An  empirical  comparison  of  supervised

learning  algorithms.  proceedings  of  the  23rd  international  conference  on

machine learning, Pittsburgh (PA) (2006).

[103] J. R. Quinlan, Induction of decision trees, Machine learning 1 (1) (1986)

81–106.

36

---

<!-- PAGE 37 -->

[104] S. B. Kotsiantis, I. D. Zaharakis, P. E. Pintelas, Machine learning: a review of

classi(cid:976)ication  and  combining  techniques,  Arti(cid:976)icial  Intelligence  Review  26

(3) (2006) 159–190.

[105] E. W. Ngai, Y. Hu, Y. H. Wong, Y. Chen, X. Sun, The application of data mining

techniques in (cid:976)inancial fraud detection: A classi(cid:976)ication framework and an

academic review of literature, Decision support systems 50 (3) (2011) 559–

569.

[106] N.  V.  Chawla,  C4.  5  and  imbalanced  data  sets:  investigating  the  effect  of

sampling  method,  probabilistic  estimate,  and  decision  tree  structure,  in:

Proceedings of the ICML, Vol. 3, 2003, p. 66.

[107] W. Liu, S. Chawla, D. A. Cieslak, N. V. Chawla, A robust decision tree algorithm

for  imbalanced data  sets,  in: Proceedings of the  2010  SIAM  International

Conference on Data Mining, SIAM, 2010, pp. 766–777.

[108] V. Podgorelec, M. Zorman, Decision tree learning, Encyclopedia of

Complexity and Systems Science (2015) 1–28.

[109] L. Breiman, Random forests, Machine learning 45 (1) (2001) 5–32.

[110] I. Triguero, S. del R´ıo, V. L´opez, J. Bacardit, J. M. Ben´ıtez, F. Herrera, Rosefw-

rf: the winner algorithm for the ecbdl’14 big data competition: an extremely

imbalanced big data bioinformatics problem, Knowledge-Based Systems 87

(2015) 69–79.

[111] S. Del R´ıo, V. L´opez, J. M. Ben´ıtez, F. Herrera, On the use of mapreduce for

imbalanced big data using random forest, Information Sciences 285 (2014)

112–137.

[112] L. Zhou, H. Wang, Loan default prediction on large imbalanced data using

random forests, TELKOMNIKA Indonesian Journal of Electrical

Engineering 10 (6) (2012) 1519–1525.

37

---

<!-- PAGE 38 -->

[113] T. M. Khoshgoftaar, M. Golawala, J. Van Hulse, An empirical study of learning

from imbalanced data using random forest, in: 19th IEEE

International Conference on Tools with Arti(cid:976)icial Intelligence (ICTAI 2007),

Vol. 2, IEEE, 2007, pp. 310–317.

[114] I. Rish, et al., An empirical study of the naive bayes classi(cid:976)ier, in: IJCAI 2001

workshop on empirical methods in arti(cid:976)icial intelligence,  Vol. 3,  2001,  pp.

41–46.

[115] N. Friedman, D. Geiger, M. Goldszmidt, Bayesian network classi(cid:976)iers,

Machine learning 29 (2-3) (1997) 131–163.

[116] L.  Borrajo,  R.  Romero,  E.  L.  Iglesias,  C.  R.  Marey,  Improving  imbalanced

scienti(cid:976)ic  text  classi(cid:976)ication  using  sampling  strategies  and  dictionaries,

Journal of integrative bioinformatics 8 (3) (2011) 90–104.

[117] I.  Mani,  I.  Zhang,  knn  approach  to  unbalanced  data  distributions:  a  case

study  involving  information  extraction,  in:  Proceedings  of  workshop  on

learning from imbalanced datasets, Vol. 126, 2003.

[118] X. Zhang, Y. Li, R. Kotagiri, L. Wu, Z. Tari, M. Cheriet, Krnn: k

rare-class nearest neighbour classi(cid:976)ication, Pattern Recognition 62 (2017)

33–44.

[119] M. Beckmann, N. F. Ebecken, B. S. P. de Lima, et al., A knn

undersampling approach for data balancing, Journal of Intelligent Learning

Systems and Applications 7 (04) (2015) 104.

[120] A. Majid,  S. Ali, M. Iqbal,  N.  Kausar, Prediction  of human breast and colon

cancers from imbalanced data using nearest neighbor and support vector

machines, Computer methods and programs in biomedicine 113 (3) (2014)

792–808.

[121] N. Tomaˇsev, D. Mladeni´c, Class imbalance and the curse of minority hubs,

Knowledge-Based Systems 53 (2013) 157–172.

38

---

<!-- PAGE 39 -->

[122] Y.  Li,

with

Zhang,  Improving

X. 
exemplar

k

nearest  neighbor

generalization for imbalanced classi(cid:976)ication, in: Paci(cid:976)ic-Asia Conference on

Knowledge Discovery and Data Mining, Springer, 2011, pp. 321–332.

[123] T.  Gao,  Y.  Hao,  H.  Zhang,  L.  Hu,  H.  Li,  H.  Li,  L.  Hu,  B.  Han,  Predicting

pathological  response  to  neoadjuvant  chemotherapy  in  breast  cancer

patients  based  on  imbalanced  clinical  data,  Personal  and  Ubiquitous

Computing 22 (5-6) (2018) 1039–1047.

[124] J. Hu, Y. Li, W.-X. Yan, J.-Y. Yang, H.-B. Shen, D.-J. Yu, Knn-based dynamic query-

driven  sample

rescaling  strategy

for  class

imbalance

learning,

Neurocomputing 191 (2016) 363–373.

[125] C. Abeysinghe, J. Li, J. He, A classi(cid:976)ier hub for imbalanced (cid:976)inancial data, in:

Australasian Database Conference, Springer, 2016, pp. 476–479.

[126] X.-S. Hu, R.-J. Zhang, Clustering-based subset ensemble learning method for

imbalanced  data,  in:  2013  International  Conference  on  Machine  Learning

and Cybernetics, Vol. 1, IEEE, 2013, pp. 35–39.

[127] D.  Wu,  X.  Chen,  C.  Chen,  J.  Zhang,  Y.  Xiang,  W.  Zhou,  On  addressing  the

imbalance  problem:  a  correlated  knn  approach  for  network  traf(cid:976)ic

classi(cid:976)ication, in: International Conference on Network and System Security,

Springer, 2015, pp. 138–151.

[128] A. B. Owen, In(cid:976)initely imbalanced logistic regression, Journal of Machine

Learning Research 8 (Apr) (2007) 761–773.

[129] M.  Maalouf,  T.  B.  Trafalis,  Robust  weighted  kernel  logistic  regression  in

imbalanced and rare events data, Computational Statistics & Data Analysis

55 (1) (2011) 168–183.

[130] A. Dagliati, S. Marini, L.  Sacchi, G. Cogni, M.  Teliti, V. Tibollo, P. De Cata, L.

Chiovato,  R.  Bellazzi,  Machine  learning  methods  to  predict  diabetes

complications, Journal of diabetes science and technology 12 (2)

39

---

<!-- PAGE 40 -->

(2018) 295–302.

[131] S.  Dreiseitl,  L.  Ohno-Machado,  Logistic  regression  and  arti(cid:976)icial  neural

network classi(cid:976)ication models: a methodology review, Journal of biomedical

informatics 35 (5-6) (2002) 352–359.

[132] M.  Ohsaki,  P.  Wang,  K.  Matsuda,  S.  Katagiri,  H.  Watanabe,  A.  Ralescu,

Confusion-matrix-based  kernel  logistic  regression  for  imbalanced  data

classi(cid:976)ication, IEEE Transactions on Knowledge and Data Engineering 29 (9)

(2017) 1806–1819.

[133] P.  Nieminen,  T.  K¨arkk¨ainen,  Multicriteria  optimized  mlp  for  imbalanced

learning., in: ESANN, 2016.

[134] D.  Hand, The  elements  of statistical  learning:  Data  mining,  inference,  and

prediction, Biometrics 58 (1) (2002) 252.

[135] J. Breneman, Kernel methods for pattern analysis (2005).

[136] J. Han, M.  Kamber, J. Pei, Data mining: concepts and techniques, waltham,

ma, Morgan Kaufman Publishers 10 (2012) 978–1.

[137] I.  H.  Witten,  E.  Frank,  Data  mining:  practical  machine  learning  tools  and

techniques with java implementations, Acm Sigmod Record 31 (1) (2002)

76–77.

[138] T.  Evgeniou,  C.  A.  Micchelli,  M.  Pontil,  J.  Shawe-Taylor,  Learning  multiple

tasks  with  kernel  methods.,  Journal  of  machine  learning  research  6  (4)

(2005).

[139] J. Apostolakis, An introduction to data mining, in:

Data Mining in

Crystallography, Springer, 2009, pp. 1–35.

[140] T. Hofmann, B. Sch¨olkopf, A. J. Smola, Kernel methods in machine learning,

The annals of statistics (2008) 1171–1220.

[141] V. N. Vapnik, An overview of statistical learning theory, IEEE transactions on

neural networks 10 (5) (1999) 988–999.

40

---

<!-- PAGE 41 -->

[142] C. Cortes, V. Vapnik, Support-vector networks, Machine learning 20 (3)

(1995) 273–297.

[143] S.  Piri,  D.  Delen,  T.  Liu,  A  synthetic  informative  minority  over-sampling

(simo)  algorithm  leveraging  support  vector  machine  to  enhance  learning

from imbalanced datasets, Decision Support Systems 106 (2018) 15–29.

[144] M. E. Abbasnejad, D. Ramachandram, R. Mandava, A survey of the state of

the art in learning the kernels, Knowledge and information systems 31 (2)

(2012) 193–221.

[145] X. Wang, E. P. Xing, D. J. Schaid, Kernel methods for large-scale genomic data

analysis, Brie(cid:976)ings in bioinformatics 16 (2) (2015) 183–192.

[146] A. B. Parsa, H. Taghipour, S. Derrible, A. K. Mohammadian, Real-time accident

detection: coping with imbalanced data, Accident Analysis & Prevention 129

(2019) 202–210.

[147] L. Wei, Y. Yang, R. M. Nishikawa, Y. Jiang, A study on several machine-learning

methods

for

classi(cid:976)ication  of  malignant  and  benign

clustered

microcalci(cid:976)ications,  IEEE  transactions  on  medical  imaging  24  (3)  (2005)

371–380.

[148] S.-i.  Amari,  S.  Wu,  Improving  support  vector  machine  classi(cid:976)iers  by

modifying kernel functions, Neural Networks 12 (6) (1999) 783–789.

[149] Y. B. Wah, H. A. A. Rahman, H. He, A. Bulgiba, Handling imbalanced dataset

using  svm  and  k-nn  approach,  in: AIP  Conference  Proceedings,  Vol.  1750,

AIP Publishing LLC, 2016, p. 020023.

[150] N.  Thai-Nghe,  Z.  Gantner,  L.  Schmidt-Thieme,  Cost-sensitive  learning

methods for imbalanced data, in: The 2010 International joint conference

on neural networks (IJCNN), IEEE, 2010, pp. 1–8.

[151] Q. Yan,

S.

sensitive  svm

Xia, 
for

F.

Meng,  Optimizing

cost-

41

---

<!-- PAGE 42 -->

imbalanced  data:  Connecting  cluster  to  classi(cid:976)ication,  arXiv  preprint

arXiv:1702.01504 (2017).

[152] P. Cao, D. Zhao, O. Zaiane, An optimized cost-sensitive svm for imbalanced

data learning, in: Paci(cid:976)ic-Asia conference on knowledge discovery and data

mining, Springer, 2013, pp. 280–292.

[153] J.  Hu,  H.  Yang,  M.  R.  Lyu,  I.  King,  A.  M.-C.  So,  Online  nonlinear  auc

maximization  for  imbalanced  data  sets,  IEEE  transactions  on  neural

networks and learning systems 29 (4) (2017) 882–895.

[154] Q. Kang, L. Shi, M. Zhou, X. Wang, Q. Wu, Z. Wei, A distance-based weighted

undersampling scheme for support vector machines and its application to

imbalanced  classi(cid:976)ication,  IEEE  transactions  on  neural  networks  and

learning systems 29 (9) (2017) 4152–4165.

[155] Y.  Xu,  Maximum  margin  of  twin  spheres  support  vector  machine  for

imbalanced  data  classi(cid:976)ication,  IEEE  transactions  on  cybernetics  47  (6)

(2016) 1540–1550.

[156] E.  Jafarigol,  T.  Trafalis,  Imbalanced  learning  with  parametric  linear

programming  support  vector  machine  for  weather  data  application,  SN

Computer Science 1 (6) (2020) 1–11.

[157] J.  Schmidhuber,  Deep  learning  in  neural  networks:  An  overview,  Neural

networks 61 (2015) 85–117.

[158] A.  Sonak,  R.  Patankar,  N.  Pise,  A  new  approach  for  handling  imbalanced

dataset using ann and genetic algorithm, in: 2016 International Conference

on  Communication  and  Signal  Processing  (ICCSP),  IEEE,  2016,  pp.  1987–

1990.

[159] J.  Zheng,  Cost-sensitive  boosting  neural  networks  for  software  defect

prediction, Expert Systems with Applications 37 (6) (2010) 4537–4543.

42

---

<!-- PAGE 43 -->

[160] T.  Ashihara,  Y.  Shinohara,  H.  Sato,  T.  Moriya,  K.  Matsui,  T.  Fukutomi,  Y.

Yamaguchi,  Y.  Aono,  Neural  whispered  speech  detection  with  imbalanced

learning., in: INTERSPEECH, 2019, pp. 3352–3356.

[161] Q. Ya-Guan, M. Jun, Z. Xi-Min, P. Jun, Z. Wu-Jie, W. Shu-Hui, Y. Ben-Sheng, L.

Jing-Sheng,  Emsgd:  An  improved  learning  algorithm  of  neural  networks

with imbalanced data, IEEE Access 8 (2020)

64086–64098.

[162] G.-B.  Huang,  Q.-Y.  Zhu,  C.-K.  Siew,  Extreme  learning  machine:  theory  and

applications, Neurocomputing 70 (1-3) (2006) 489–501.

[163] H. Kaya, A. A. Karpov, Introducing weighted kernel classi(cid:976)iers for handling

imbalanced  paralinguistic  corpora:  Snoring,  addressee  and  cold.,  in:

INTERSPEECH, 2017, pp. 3527–3531.

[164] Y.  Zhang,  B.  Liu,  J.  Cai,  S.  Zhang,  Ensemble  weighted  extreme  learning

machine for imbalanced data classi(cid:976)ication based on differential evolution,

Neural Computing and Applications 28 (1) (2017) 259–267.

[165] W.  Zong,  G.-B.  Huang,  Y.  Chen,  Weighted  extreme  learning  machine  for

imbalance learning, Neurocomputing 101 (2013) 229–242.

[166] B. S. Raghuwanshi, S. Shukla, Generalized class-speci(cid:976)ic kernelized extreme

learning machine for multiclass imbalanced learning, Expert Systems with

Applications 121 (2019) 244–255.

[167] Y.-P. Zhao, Y.-B. Chen, Z. Hao, H. Wang, Z. Yang, J.-F. Tan, Imbalanced kernel

extreme learning machines for fault detection of aircraft engine, Journal of

Dynamic Systems, Measurement, and Control 142 (10) (2020).

[168] B. S. Raghuwanshi, S. Shukla, Smote based class-speci(cid:976)ic extreme  learning

machine  for  imbalanced  learning,  Knowledge-Based  Systems  187  (2020)

104814.

43

---

<!-- PAGE 44 -->

[169] J.  M.  Johnson,  T.  M.  Khoshgoftaar,  Survey  on  deep  learning  with  class

imbalance, Journal of Big Data 6 (1) (2019) 27.

[170] L. Zhang, C. Zhang, S. Quan, H. Xiao, G. Kuang, L. Liu, A class

imbalance loss for imbalanced object recognition, IEEE Journal of Selected

Topics in Applied Earth Observations and Remote Sensing 13 (2020) 2778–

2792.

[171] Q.  Dong,  S.  Gong,  X.  Zhu,  Imbalanced  deep  learning  by  minority  class

incremental  recti(cid:976)ication,  IEEE  transactions  on  pattern  analysis  and

machine intelligence 41 (6) (2018) 1367–1381.

[172] H.-I.  Lin, C.-M.  Nguyen, Boosting minority  class  prediction  on imbalanced

point cloud data, Applied Sciences 10 (3) (2020) 973.

[173] T. Guo, X. Zhu, Y. Wang, F. Chen, Discriminative sample generation for deep

imbalanced learning., in: IJCAI, 2019, pp. 2406–2412.

[174] Q. Dong, S. Gong, X. Zhu, Class recti(cid:976)ication hard mining for imbalanced deep

learning, in: Proceedings of the IEEE International Conference on Computer

Vision, 2017, pp. 1851–1860.

[175] F. Bao, Y. Deng, Y. Kong, Z. Ren, J. Suo, Q. Dai, Learning deep landmarks for

imbalanced  classi(cid:976)ication,  IEEE  Transactions  on  Neural  Networks  and

Learning Systems (2019).

[176] S. H. Khan, M. Hayat, M. Bennamoun, F. A. Sohel, R. Togneri,

Cost-sensitive  learning  of  deep  feature  representations  from  imbalanced

data,  IEEE  transactions  on  neural  networks  and  learning  systems  29  (8)

(2017) 3573–3587.

[177] E. Lin, Q. Chen, X. Qi, Deep reinforcement learning for imbalanced

classi(cid:976)ication, Applied Intelligence (2020) 1–15.

[178] S. E. Roshan, S. Asadi, Improvement of bagging performance for

44

---

<!-- PAGE 45 -->

classi(cid:976)ication  of  imbalanced  datasets  using  evolutionary  multi-objective

optimization, Engineering Applications of Arti(cid:976)icial Intelligence 87 (2020)

103319.

[179] G. Collell, D. Prelec, K. R. Patil, A simple plug-in bagging ensemble based on

threshold-moving for classifying binary and multiclass imbalanced data,

Neurocomputing 275 (2018) 330–340.

[180] B.  Wang,  J.  Pineau,  Online  bagging  and  boosting  for  imbalanced  data

streams,  IEEE  Transactions  on  Knowledge  and  Data  Engineering  28  (12)

(2016) 3353–3366.

[181] B.  Krawczyk,  M.  Wo´zniak,  G.  Schaefer,  Cost-sensitive  decision  tree

ensembles for effective imbalanced classi(cid:976)ication, Applied Soft Computing

14 (2014) 554–562.

[182] V.  S.  Sheng,  C.  X.  Ling,  Roulette  sampling  for  cost-sensitive  learning,  in:

European Conference on Machine Learning, Springer, 2007, pp. 724–731.

[183] M. M. Javidi, F. Shamsezat, Learning from imbalanced multi-label data sets

by  using  ensemble  strategies,  Computer  Engineering  and  Applications

Journal 4 (1) (2015) 61–81.

[184] C. Lingchi, D. Xiaoheng, S. Hailan, Z. Congxu, C.  Le, Dycusboost: Adaboost-

based  imbalanced  learning  using  dynamic  clustering  and  undersampling,

in: 2018 IEEE 16th Intl Conf on Dependable,

Autonomic and Secure Computing, 16th Intl Conf on Pervasive Intelligence

and Computing, 4th Intl Conf on Big Data Intelligence and Computing and

Cyber

Science

and

Technology

Congress

(DASC/PiCom/DataCom/CyberSciTech), IEEE, 2018, pp. 208–215.

[185] M. Galar, A. Fernandez, E. Barrenechea, H. Bustince, F. Herrera, A review on

ensembles for the class imbalance problem: bagging-, boosting-, and hybrid-

based  approaches,  IEEE  Transactions  on  Systems,  Man,  and  Cybernetics,

Part C (Applications and Reviews) 42 (4) (2011) 463–484.

45

---

<!-- PAGE 46 -->

[186] M. Khalilia, S. Chakraborty, M. Popescu, Predicting disease risks from highly

imbalanced  data  using  random  forest,  BMC  medical  informatics  and

decision making 11 (1) (2011) 51.

[187] L. Loezer, F. Enembreck, J. P. Barddal, A. de Souza Britto Jr,

Cost-sensitive learning for imbalanced data streams, in: Proceedings of the

35th Annual ACM Symposium on Applied Computing, 2020, pp. 498–504.

[188] B. Sun, H. Chen, J. Wang, H. Xie, Evolutionary under-sampling based bagging

ensemble method for imbalanced data classi(cid:976)ication, Frontiers of Computer

Science 12 (2) (2018) 331–350.

[189] V. H. A. Ribeiro, G. Reynoso-Meza, Ensemble learning by means of a multi-

objective optimization  design  approach for  dealing  with  imbalanced data

sets, Expert Systems with Applications 147 (2020) 113232.

[190] Q. Li, Y. Song, J. Zhang, V. S. Sheng, Multiclass imbalanced learning with one-

versus-one  decomposition  and  spectral  clustering,  Expert  Systems  with

Applications 147 (2020) 113152.

[191] Z. Liu, W. Cao, Z. Gao, J. Bian, H. Chen, Y. Chang, T.-Y. Liu, Self-paced ensemble

for  highly  imbalanced  massive  data  classi(cid:976)ication,  in:  2020  IEEE  36th

International Conference on Data Engineering (ICDE), IEEE, 2020, pp. 841–

852.

[192] R. Harliman, K. Uchida, Data-and algorithm-hybrid approach for imbalanced

data  problems  in  deep  neural  network,  International  Journal  of  Machine

Learning and Computing 8 (3) (2018) 208–213.

[193] S.  Dong,  Y.  Wu,  A  genetic  algorithm-based  approach  for  class-imbalanced

learning,  in:  Third  International  Workshop  on  Pattern  Recognition,  Vol.

10828, International Society for Optics and Photonics, 2018, p. 108281D.

[194] P.  Branco,  L.  Torgo,  R.  P.  Ribeiro,  A  survey  of  predictive  modeling  on

imbalanced domains, ACM Computing Surveys (CSUR) 49 (2) (2016)

1–50.

46

---

<!-- PAGE 47 -->

[195] H. Kaur, H. S. Pannu, A.  K. Malhi, A systematic review on imbalanced data

challenges in machine learning: Applications and solutions, ACM Computing

Surveys (CSUR) 52 (4) (2019) 1–36.

[196] P.  Gnip,  P.  Drot´ar,  Ensemble  methods  for  strongly  imbalanced  data:

bankruptcy  prediction,  in:  2019  IEEE  17th  International  Symposium  on

Intelligent Systems and Informatics (SISY), IEEE, 2019, pp. 155–160.

[197] M. Zoriˇc´ak, P. Gnip, P. Drot´ar, V. Gazda, Bankruptcy prediction for small-

and  medium-sized  companies  using  severely

imbalanced  datasets,

Economic Modelling 84 (2020) 165–176.

[198] Q.  Chang,  S.  Lin,  X.  Liu,  Stacked-svm:  A  dynamic  svm  framework  for

telephone fraud identi(cid:976)ication from imbalanced cdrs, in: Proceedings of the

2019 2nd International Conference on Algorithms, Computing and Arti(cid:976)icial

Intelligence, 2019, pp. 112–120.

[199] L. M. Junior, F. M. Nardini, C. Renso, R. Trani, J. A. Macedo, A novel approach

to  de(cid:976)ine  the  local  region  of  dynamic  selection  techniques  in  imbalanced

credit scoring problems, Expert Systems with Applications (2020) 113351.

[200] U.  R.  Salunkhe,  S.  N.  Mali,  Classi(cid:976)ier  ensemble  design  for imbalanced  data

classi(cid:976)ication:  a  hybrid  approach,  Procedia  Computer  Science  85  (2016)

725–732.

[201] S. Dhankhad, E. Mohammed, B. Far, Supervised machine learning

algorithms for credit card fraudulent transaction detection: a comparative

study,  in:  2018  IEEE  International  Conference  on  Information  Reuse  and

Integration (IRI), IEEE, 2018, pp. 122–125.

[202] L. E. B. Ferreira, J. P. Barddal, H. M. Gomes, F. Enembreck, Improving credit

risk  prediction  in  online  peer-to-peer  (p2p)  lending  using  imbalanced

learning techniques, in: 2017 IEEE 29th International

Conference  on  Tools  with  Arti(cid:976)icial  Intelligence  (ICTAI),  IEEE,  2017,  pp.

175–181.

47

---

<!-- PAGE 48 -->

[203] L. S. de Melo Junior, F. M. Nardini, C. Renso, J. A. F. de Macˆedo, An empirical

comparison  of  classi(cid:976)ication  algorithms  for  imbalanced  credit  scoring

datasets, in: 2019 18th IEEE International Conference On

Machine Learning And Applications (ICMLA), IEEE, 2019, pp. 747–754.

[204] A. Namvar, M.

Siami,  F.

Rabhi,  M.

Naderpour,

Credit  risk

prediction  in  an  imbalanced  social  lending  environment,  arXiv  preprint

arXiv:1805.00801 (2018).

[205] R. A. Bauder, T. M. Khoshgoftaar, T. Hasanin, Data sampling approaches with

severely imbalanced big data for medicare fraud detection, in: 2018

IEEE  30th  international  conference  on  tools  with  arti(cid:976)icial  intelligence

(ICTAI), IEEE, 2018, pp. 137–142.

[206] M. Orooji, J. Chen, Predicting louisiana public high school dropout through

imbalanced

learning  techniques,

in:  2019  18th  IEEE  International

Conference on Machine Learning and Applications (ICMLA), IEEE, 2019, pp.

456–461.

[207] Y. Zheng, H. Cheon, C. M. Katz, Using machine learning methods to develop a

short  tree-based  adaptive  classi(cid:976)ication  test:  Case  study  with  a  high-

dimensional  item  pool  and  imbalanced  data,  Applied  Psychological

Measurement (2020) 0146621620931198.

[208] C. Zhao, Y.  Xin,  X. Li, Y. Yang, Y. Chen, A heterogeneous  ensemble  learning

framework  for  spam  detection  in  social  networks  with  imbalanced  data,

Applied Sciences 10 (3) (2020) 936.

[209] Q. Song, Y. Guo, M. Shepperd, A comprehensive investigation of the role of

imbalanced learning for software defect prediction, IEEE  Transactions  on

Software Engineering 45 (12) (2018) 1253–1269.

[210] Y.-C. Chen, Y.-J. Li, A. Tseng, T. Lin, Deep learning for malicious (cid:976)low detection,

in: 2017 IEEE 28th Annual  International Symposium on Personal,  Indoor,

and Mobile Radio Communications (PIMRC), IEEE, 2017, pp. 1–7.

48

---

<!-- PAGE 49 -->

[211] H. Li, Y. Qu, S. Guo, G. Gao, R. Chen, G. Chen, Surprise bug

report prediction utilizing optimized integration with imbalanced learning

strategy, Complexity 2020 (2020).

[212] R. Chen, S.-K. Guo, X.-Z. Wang, T.-L. Zhang, Fusion of multi-rsmote with fuzzy

integral  to  classify  bug  reports  with  an  imbalanced  distribution,  IEEE

Transactions on Fuzzy Systems 27 (12) (2019) 2406–2420.

[213] R.  Abdulhammed,  M.  Faezipour,  A.  Abuzneid,  A.  AbuMallouh,  Deep  and

machine  learning  approaches  for  anomaly-based  intrusion  detection  of

imbalanced network traf(cid:976)ic, IEEE sensors letters 3 (1) (2018) 1–4.

[214] G. Karatas, O. Demir, O. K. Sahingoz, Increasing the performance of machine

learning-based idss on an imbalanced and up-to-date dataset, IEEE Access

8 (2020) 32150–32162.

[215] F. Feng, K.-C. Li, J. Shen, Q. Zhou, X. Yang, Using cost-sensitive learning and

feature  selection  algorithms  to  improve  the  performance  of  imbalanced

classi(cid:976)ication, IEEE Access 8 (2020) 69979–69996.

[216] Y. Zheng, Y. Zheng, W. Ohyama, D. Suehiro, S. Uchida, Ranksvm

for  of(cid:976)line  signature  veri(cid:976)ication,  in:  2019  International  Conference  on

Document Analysis and Recognition (ICDAR), IEEE, 2019, pp. 928–933.

[217] Y. Pang, Z. Chen, X. Li, S. Wang, C. Zhao, L. Wang, K. Ji, Z. Li, Finding android

malware  trace  from  highly  imbalanced  network  traf(cid:976)ic,  in:  2017  IEEE

International Conference on Computational Science and Engineering (CSE)

and  IEEE  International  Conference  on  Embedded  and  Ubiquitous

Computing (EUC), Vol. 1, IEEE, 2017, pp. 588–595.

[218] M.  J.  Fern´andez-G´omez,  G.  Asencio-Cort´es,  A.  Troncoso,  F.  Mart´ınez-

Alvarez, Large earthquake magnitude prediction in chile´ with imbalanced

classi(cid:976)iers and ensemble learning, Applied Sciences 7 (6) (2017) 625.

[219] N.-W. Chi,  J.-P. Wang,

J.-H. Liao,

W.-C. Cheng,

C.-S. Chen,

Machine learning-based seismic capability evaluation for school buildings,

49

---

<!-- PAGE 50 -->

Automation in Construction 118 (2020) 103274.

[220] T. B. Trafalis, I. Adrianto, M. B. Richman, Active learning with support vector

machines

for  tornado  prediction,

in:  International  Conference  on

Computational Science, Springer, 2007, pp. 1130–1137.

[221] T. B. Trafalis,

I. Adrianto,

M. B. Richman,  S. Lakshmivarahan,

Machine-learning  classi(cid:976)iers  for  imbalanced  tornado  data,  Computational

Management Science 11 (4) (2014) 403–418.

[222] T. B. Trafalis, H. Ince, M. B. Richman, Tornado detection with support vector

machines, in: International Conference on Computational Science, Springer,

2003, pp. 289–298.

[223] A.  Artetxe,  M.  Gran˜a,  A.  Beristain,  S.  R´ıos,  Balanced  training  of  a  hybrid

ensemble method for imbalanced datasets: a case of emergency department

readmission prediction, Neural Computing and Applications 32 (10) (2020)

5735–5744.

[224] J. Zhang, L. Chen, F. Abid, Prediction of breast cancer from imbalance respect

using  cluster-based  undersampling  method,

Journal  of  healthcare

engineering 2019 (2019).

[225] R. Zheng, L. Liu, S. Zhang, C. Zheng, F. Bunyak, R. Xu, B. Li, M. Sun, Detection

of  exudates  in  fundus  photographs  with  imbalanced  learning  using

conditional  generative  adversarial  network,  Biomedical  optics  express  9

(10) (2018) 4863–4878.

[226] B. Jeong, H. Cho, J. Kim, S. K. Kwon, S. Hong, C. Lee, T. Kim, M. S. Park, S. Hong,

T.-Y.  Heo,  Comparison  between  statistical  models  and  machine  learning

methods  on  classi(cid:976)ication  for  highly  imbalanced  multiclass  kidney  data,

Diagnostics 10 (6) (2020) 415.

[227] A. Farhadi, D. Chen, R. McCoy, C. Scott, J. A. Miller, C. M.  Vachon, C. Ngufor,

Breast  cancer  classi(cid:976)ication  using  deep  transfer  learning  on  structured

healthcare data, in: 2019 IEEE International Conference on

50

---

<!-- PAGE 51 -->

Data Science and Advanced Analytics (DSAA), IEEE, 2019, pp. 277–286.

[228] R. Singh, T. Ahmed, A. Kumar, A. K. Singh, A. K. Pandey, S. K.

Singh, Imbalanced breast cancer classi(cid:976)ication using transfer learning,

IEEE/ACM  Transactions  on  Computational  Biology  and  Bioinformatics

(2020).

[229] B.  Krawczyk,  M.  Galar,  L  .  Jelen´,  F.  Herrera,  Evolutionary  undersampling

boosting for imbalanced classi(cid:976)ication of breast cancer malignancy, Applied

Soft Computing 38 (2016) 714–726.

[230] T. Cai, H. He, W. Zhang, Breast cancer diagnosis using imbalanced learning

and  ensemble  method,  Applied  and  Computational  Mathematics  7  (3)

(2018) 146–154.

[231] D. Gan, J. Shen, B. An, M. Xu, N. Liu, Integrating tanbn with cost

sensitive classi(cid:976)ication algorithm for imbalanced data in medical diagnosis,

Computers & Industrial Engineering 140 (2020) 106266.

[232] F. Deeba, S. K. Mohammed, F. M. Bui, K. A. Wahid, Learning from imbalanced

data: A comprehensive comparison  of classi(cid:976)ier performance for bleeding

detection  in  endoscopic  video,  in:  2016  5th  International  Conference  on

Informatics, Electronics and Vision (ICIEV), IEEE, 2016, pp. 1006–1009.

[233] X.  Deng,  Y.  Xu,  L.  Chen,  W.  Zhong,  A.  Jolfaei,  X.  Zheng,  Dynamic  clustering

method  for  imbalanced  learning  based  on  adaboost,  The  Journal  of

Supercomputing (2020) 1–23.

[234] H.  Zhang,  H.  Zhang,  S.  Pirbhulal,  W.  Wu,  V.  H.  C.  D.  Albuquerque,  Active

balancing mechanism for imbalanced medical data in deep learning–based

classi(cid:976)ication  models,  ACM  Transactions  on  Multimedia  Computing,

Communications, and Applications (TOMM) 16 (1s) (2020) 1–15.

[235] J.  Jia,  L.  Zhai,  W.  Ren,  L.  Wang,  Y.  Ren,  An  effective  imbalanced  jpeg

steganalysis scheme based on adaptive cost-sensitive feature learning, IEEE

Transactions on Knowledge and Data Engineering (2020).

51

---

<!-- PAGE 52 -->

[236] Y. Huang, Y. Jin, Y. Li, Z. Lin, Towards imbalanced image classi(cid:976)ication:

A generative adversarial network ensemble learning method, IEEE Access 8

(2020) 88399–88409.

[237] M.  Hayat, S. Khan,  S.  W. Zamir,  J. Shen,  L.  Shao,  Gaussian  af(cid:976)inity  for  max-

margin class imbalanced learning, in: Proceedings of the IEEE International

Conference on Computer Vision, 2019, pp. 6469–6479.

[238] K.  H.  Kim,  S.  Y.  Sohn,  Hybrid  neural  network  with  cost-sensitive  support

vector  machine  for  class-imbalanced  multimodal  data,  Neural  Networks

(2020).

[239] S.  Pouyanfar,  S.-C.  Chen,  Semantic  event  detection  using  ensemble  deep

learning,  in:  2016  IEEE  International  Symposium  on  Multimedia  (ISM),

IEEE, 2016, pp. 203–208.

[240] G. Lemaˆıtre, F. Nogueira, C. K. Aridas, Imbalanced-learn: A python toolbox

to tackle the curse of imbalanced datasets in machine learning, The Journal

of Machine Learning Research 18 (1) (2017) 559–563.

[241] J.  Vanhoeyveld,  D.  Martens,  Imbalanced  classi(cid:976)ication  in  sparse  and  large

behaviour datasets,  Data Mining and Knowledge Discovery 32 (1) (2018)

25–82.

[242] K.  Napierala,  J.  Stefanowski,  Types  of  minority  class  examples  and  their

in(cid:976)luence on learning classi(cid:976)iers from imbalanced data, Journal of Intelligent

Information Systems 46 (3) (2016) 563–597.

[243] S.  Gupta,  A.  Jivani,  A  cluster  based  under-sampling  solution  for  handling

imbalanced data.

[244] X. Wang, H. Wang, D. Wu, Y. Wang, R. Zhou, A fuzzy consensus

clustering based undersampling approach for class imbalanced learning,

in:  Proceedings  of  the 2019  2nd  International  Conference  on Algorithms,

Computing and Arti(cid:976)icial Intelligence, 2019, pp. 133–137.

52

---

<!-- PAGE 53 -->

[245] M.  Lango,  J.  Stefanowski,  Multi-class  and  feature  selection  extensions  of

roughly  balanced  bagging  for  imbalanced  data,  Journal  of  Intelligent

Information Systems 50 (1) (2018) 97–127.

[246] V.  M.  S.  Esteves,  Techniques  to  deal  with  imbalanced  data  in  multi-class

problems: A review of existing methods (2020).

[247] J.-J. Zhang, P. Zhong, Learning biased svm with weighted within-class scatter

for imbalanced classi(cid:976)ication, Neural Processing Letters 51 (1) (2020) 797–

817.

[248] C.-M.  Vong,  J.  Du,  Accurate  and  ef(cid:976)icient  sequential  ensemble  learning  for

highly imbalanced multi-class data, Neural Networks (2020).

[249] B. Mirza, Z. Lin, Meta-cognitive online sequential extreme learning machine

for imbalanced and concept-drifting data classi(cid:976)ication, Neural Networks 80

(2016) 79–94.

[250] S.  Shukla,  B.  S.  Raghuwanshi,  Online  sequential  class-speci(cid:976)ic  extreme

learning  machine  for  binary  imbalanced  learning,  Neural  Networks  119

(2019) 235–248.

[251] T.  Zhu,  Y.  Lin,  Y.  Liu,  Oversampling  for imbalanced  time  series data,  arXiv

preprint arXiv:2004.06373 (2020).

[252] M. Andersson, Multi-class imbalanced learning for time series problem: An

industrial case study (2020).

[253] C.  Katrakazas,  C.  Antoniou,  G.  Yannis,  Time  series  classi(cid:976)ication  using

imbalanced learning for real-time safety assessment, in: Proceedings of the

Transportation Research Board (TRB) 98th Annual Meeting,

Washington, DC, January, 2019, pp. 13–17.

[254] H. M. Nguyen, E. W. Cooper, K. Kamei, Online learning from imbalanced data

streams, in: 2011 International Conference of Soft Computing and Pattern

Recognition (SoCPaR), IEEE, 2011, pp. 347–352.

53

---

<!-- PAGE 54 -->

[255] X.  Zhang,  T.  Yang,  P.  Srinivasan,  Online  asymmetric  active  learning  with

imbalanced data, Association for Computing Machinery, New York, NY,

USA, 2016. doi:10.1145/2939672.2939854.

URL h(cid:425)ps://doi.org/10.1145/2939672.2939854

[256] Y.  Yan,  T.  Yang,  Y.  Yang,  J.  Chen,  A  framework  of  online  learning  with

imbalanced  streaming  data,  in:  Proceedings  of  the  AAAI  Conference  on

Arti(cid:976)icial Intelligence, Vol. 31, 2017.

[257] L.  Wang,  S.  Xu,  X.  Wang,  Q.  Zhu,  Towards  class  imbalance  in  federated

learning, arXiv preprint arXiv:2008.06217 (2020).

[258] M.  Duan,  D.  Liu,  X.  Chen,  R.  Liu,  Y.  Tan,  L.  Liang,  Self-balancing  federated

learning with global imbalanced data in mobile systems, IEEE Transactions

on  Parallel  and  Distributed  Systems  32

(1)

(2021)  59–71.

doi:10.1109/TPDS.2020.3009406.

54

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

A Review of Machine Learning Techniques in
Imbalanced Data and Future Trends
Elaheh Jafarigola,1, Theodore B. Trafalisa, Neshat Mohammadia
aSchool of Industrial and Systems Engineering University of Oklahoma, 202 W. Boyd St., Room 124, Norman,
Oklahoma 73019, USA
Abstract
For over two decades, detecting rare events has been a challenging task among
researchers in the data mining and machine learning domain. Real-life problems
inspire researchers to navigate and further improve data processing and algorithmic
approaches to achieve effective and computationally ef(cid:976)icient methods for imbalanced
learning. In this paper, we have collected and reviewed 258 peer-reviewed papers
from archival journals and conference papers in an attempt to provide an in-depth
review of various approaches in imbalanced learning from technical and application
perspectives. This work aims to provide a structured review of methods used to
address the problem of imbalanced data in various domains and create a general
guideline for researchers in academia or industry who want to dive into the broad (cid:976)ield
of machine learning using large-scale imbalanced data.
Keywords: imbalanced learning, rare events, data mining, classifica(cid:415)on, predic(cid:415)on
Introduction
Classi(cid:976)ication problems are a major part of supervised learning and very often,
the data is not equally distributed between the classes. The performance of the
classi(cid:976)ier is affected by the ratio of the majority class to the minority class, hence
1 Corresponding author
Email address: elaheh.jafarigol@ou.edu (Elaheh Jafarigol)
Preprint submitted to Elsevier September 7, 2025

misclassi(cid:976)ication is more severe when the data is extremely imbalanced [1, 2, 3, 4,
5, 6]. In addition to the relative proportion of classes, the absolute number of
available instances in the minority class is also an important factor. The problem
with imbalanced data is magni(cid:976)ied when the minority class consists of rare events.
Rare events are de(cid:976)ined as events that occur signi(cid:976)icantly less often than common
events. In the case of rare events, classi(cid:976)ication becomes more challenging,
because the classi(cid:976)ier is often overwhelmed by the majority class and the results
are biased. Therefore, without a signi(cid:976)icant loss in overall accuracy, the minority
class is misclassi(cid:976)ied. Based on the type of data, the size of the data set and the
distribution of data between classes, the issue of imbalanced learning can appear
at different levels. The problem de(cid:976)inition issues are caused by a lack of adequate
information about the minority class[7]. Problem de(cid:976)inition issues can cause
evaluation metrics such as accuracy and error rate to fail in representing the
minority class. Therefore, other evaluation metrics are de(cid:976)ined to measure the
classi(cid:976)ier in imbalanced learning problems.
The data issues are the result of absolute rarity and extremely imbalanced data.
Resampling methods are the standard solution to this issue. Algorithm issues are
caused by inadequacies of the learning algorithm and may result in poor
classi(cid:976)ication accuracy of the minority class. Such issues are caused by the model’s
failure in learning the necessary criteria for classi(cid:976)ication. The goal of imbalanced
learning is to (cid:976)ind an optimal classi(cid:976)ier that is capable of providing a balanced
degree of predictive accuracy for the minority class as well as the majority class
[8, 9, 10, 11, 12, 13, 14]. These methods are primarily attempting to address the
issue of absolute class imbalance that exists in some datasets. However, the
relative class imbalance is still an important issue in datasets where we have an
abundance of training examples, but the distribution of the different classes might
be severely skewed. In this latter situation, one can have access to enough
examples from the minority class, even if the frequency of the minority class is
very small, as long as the total number of examples is suf(cid:976)iciently big [15]. With
the broad applications of imbalanced learning in the real world, this area has
attracted the interest of many researchers and despite the advances, most
2

imbalanced learning methods are still sensitive to highly imbalanced data. In this
survey, we have selected 258 peer-reviewed papers among the papers published
on the topic of imbalanced learning and its applications. Figure 1 presents the
technical key words used in our search.
Figure 1: Technical Keywords in Imbalanced Learning Literature
In this paper, an overview of different approaches for the problem of imbalanced
learning categorized based on the format provided in Figure 2, followed bu its
applications in real-life problems is presented. The paper is organized as follows, in
section 1, we provide a categorized de(cid:976)inition of problem de(cid:976)inition approaches and
the different types of metrics used in this setting. In section 2, we focus on data
processing approaches and extensively study different over-sampling and under-
sampling methods used in the literature. Section 3 focuses on the algorithmic
approach and the core machine learning methods for learning from large
imbalanced datasets. In section 4 an overview of imbalanced learning applications
is provided. Finally, we discuss some ideas of future research trends and conclude
the paper.
3

Figure 2: General Approaches in Imbalanced Learning
Current Approaches
1. Problem De(cid:976)inition Approaches
1.1. Evaluation Metrics
Evaluation is an important part of the learning process. Evaluation metrics are
generally used to assess the generalization ability of the learning method on test
data. One of the major issues that arise with imbalanced data is the inadequacy of
well-known metrics such as accuracy and error rate in the evaluation of classi(cid:976)ication
performance. Appropriate evaluation metrics are important in evaluating the quality
of learning. Therefore, several authors have addressed this major issue and a new set
of functions have been de(cid:976)ined to determine how the classi(cid:976)ier performs in
classifying imbalanced data [16, 17, 18]. The authors of the paper published by Ferri
et al. [19] have used experimental and theoretical analysis to compare and rank the
evaluation metrics that work best on evaluating the learned model on imbalance
data and analyze the identi(cid:976)iable clusters and relationships between the metrics.
These experiments provide recommendations on the metrics that would be more
appropriate for any speci(cid:976)ic application. Evaluation metrics are categorized into
three types in the literature; threshold, probability, and ranking metrics [20].
4

1.1.1. Threshold Evaluation Metrics
The threshold type of evaluation metric is de(cid:976)ined based on a confusion matrix
as it is shown in Table 1. In binary classi(cid:976)ication, given that the predicted value of
test samples in the majority class is denoted as N (Negative), and the predicted
value of the test samples in the minority class is denoted as P (Positive), the
Confusion matrix is de(cid:976)ined. Note that, the de(cid:976)inition of a Confusion matrix can be
extended to multi-class classi(cid:976)ication as well.
Table 1: Confusion Matrix
Predictive Value
Positive Negative
Actual Value Positive TP FN
Negative FP TN
Based on this notation, Accuracy is de(cid:976)ined as a measure for performance of a
classi(cid:976)ication algorithm. Accuracy is de(cid:976)ined as:
TP + TN
Accuracy = (1) TP + TN + FP + FN
Accuracy is easy to use and interpret, however, despite being widely used by
practitioners, it cannot provide enough information to ensure a reliable learning
method when the data is imbalanced [21].
Classi(cid:976)ication performance metrics for imbalanced learning based on the
confusion metrics are de(cid:976)ined as:
TP
Precision = (2)
TP + FP
and,
TP
Recall = (3)
TP + FN
Precision and recall have an inverse relationship and when used together can
provide valid insight into the performance of the classi(cid:976)ier with regard to the
minority class. Precision and recall measure how exact and complete the model is,
respectively. Also, the precision-recall curve allows us to study the changes in both
5

metrics simultaneously. In imbalanced learning, models with high recall on the
minority class and high precision on the majority class are desired. Thus, F-measure
is a valuable evaluation metric in imbalanced learning de(cid:976)ined as:
(4)
where β is the relative importance of precision versus recall, and it is usually set
equal to one. In the presence of rare events a common approach is to maximize
the F-measure. Musicant et al. [22] have developed an approach to maximize the
F-measure by using SVMs. Geometric mean/ G-mean is an important
evaluation metric that is used explicitly for imbalanced learning.
r TP TN
·
G − mean =(5)
TP + FN TN + FP
A high G-mean indicates that the model is performing well in both classes.
Other metrics used in the literature are but not limited to:
r TP
Sensitivity =(6) TP+FN
r TN
Speci(cid:980)icity =(7) TN+FP
r TN
NegativePredictiveV alue = TN + FN (8)
Mathews Correlation Coef(cid:976)icient (MCC) [23] is de(cid:976)ines as:
TP ∗ TN − FP ∗ FN
MCC =
(9)
p
(TP + FP)(TP + FN)(TP + FN)(TN + FN)
and Bookmaker Informedness/Youden’s index = Sensitivity + Speci(cid:976)icity – 1
[24].
1.1.2. Probability Evaluation Metrics
The probability evaluation metrics are used with classi(cid:976)ication problems that
focus on predicting the probability of a class label. Two popular probability
predicting models are regression models and Arti(cid:976)icial Neural Networks (ANN)
[25]. Minimum Risk Metric (MRM) utilizes the posterior probability estimations
to minimize the misclassi(cid:976)ication risk and provide an optimal solution. There are
6

several probabilistic evaluation metrics such as Short and Fukunaga Metric, the
Value Difference Metric, and Euclidean-Hamming metrics. The Short and
Fukunaga, the Value Difference and Euclidean-Hamming metrics are distance
functions used in Nearest Neighbor (NN) learning models to measure the distance
between two instances, that can determine the associated attribute and classify
the instance in the test data [26]. Log Loss is a classi(cid:976)ication performance metric
based on the cross-entropy function. Given that the expected/known probability
of an instance in the training data is denoted as P and the predicted probability of
an instance in the test data is denoted as Q, the cross-entropy for an instance in
binary-classi(cid:976)ication is de(cid:976)ined as:
H(P,Q) = −(P(class0) ∗ log(Q(class0)) + P(class1) ∗ log(Q(class1)) (10)
In this equation, the probability P is de(cid:976)ined based on the Bernoulli distribution
for the positive class and natural logarithm. When the instance is known, the
cross-entropy is zero, therefore, we try to minimize the cross-entropy of the
model.
1.1.3. Ranking Evaluation Metrics
Sensitivity or TP rate and Speci(cid:976)icity or TN rate are used to de(cid:976)ine the Receiver
Operating Characteristic (ROC) curve, which is a visual representation of the
classi(cid:976)ication performance. The Area Under the Curve (AUC) is de(cid:976)ined
as . AUC does not depend on the classi(cid:976)ier and it is a
reliable tool for model comparison because it is scale-invariant, and the output is
the ranking of classi(cid:976)iers rather than their absolute value. AUC can also assess the
quality of models using a threshold-invariant [27, 28].
Although AUC is widely used for the evaluation and discrimination process of
binary classi(cid:976)ication models, it can be misleading sometimes. AUC uses a different
misclassi(cid:976)ication cost for each classi(cid:976)ier. Some researchers have addressed this
issue and proposed modi(cid:976)ications or alternative metrics such as the H measure
which uses a symmetric Beta distribution in the AUC [29, 30].
To summarize, we have presented the evaluation metrics categorized based on
their outcome in imbalanced learning studies in Tables 2 ,3, 4 and Figure 3.
7

Table 2: Threshold Metrics in Supervised Learning
Metrics De(cid:976)inition
Accuracy The ratio of the correctly classi(cid:976)ied instances over the
total number of classi(cid:976)ied instances
Error Rate The ratio of misclassi(cid:976)ication errors over the classi(cid:976)ied
instances
Precision The proportion of instances that were labeled correctly
among those with the positive label in the test data
Recall The portion of positive instances in the test data that
were labeled correctly
F-measure The trade-off between precision and recall
G-mean The measure to maximize the accuracy of the model over
each class by considering both classes for evaluation
Sensitivity The relative performance of the classi(cid:976)ier over the
minority class
Speci(cid:976)icity The relative performance of the classi(cid:976)ier over the
minority class
Negative Predictive The number of TN over the instances with positive label
in the test data
Value
Mathews Correlation The measure of quality in binary classi(cid:976)ication
Coef(cid:976)icient
Bookmaker The measure if discrimination capability of the classi(cid:976)ier
Informedness
Table 3: Probabilistic Metrics in Supervised Learning
Metrics De(cid:976)inition
Minimum Risk The probability of minimizing the misclassofocation risk
while maintaining an optimal solution
8

Short and Fukunaga A measure of distance between instances in Nearest
Neighbor models
Euclidean-Hamming A measure of distance between instances in Nearest
Neighbor models
Log-loss The negative log-likelihood under the Bernoulli
distribution
Table 4: Ranking Metrics in Supervised Learning
Metrics De(cid:976)inition
ROC Curve Evaluate and rank several classi(cid:976)iers
AUC The probability of correctly classifying the positive
instances while the number of false positives is
minimized
9

Figure 3: Evaluation Metrics in Imbalanced Learning
2. Data Processing Approaches
2.1. Resampling Methods
Resampling methods are developed to balance the ratio of the classes in
imbalanced learning by adjusting the minority class or the majority class and
enhancing the performance of the classi(cid:976)ier [31]. Generally, basic resampling
10

methods follow two strategies. The (cid:976)irst strategy is removing instances from the
majority class known as Random Under-sampling (RUS) [32, 33]. The second is
adding new instances to the minority class, known as Random Over-sampling
(ROS)[34]. These methods can be utilized on their own or in combination with
each other to adjust the distribution of the data before classi(cid:976)ication. A limitation
of RUS and ROS is removing valuable information in the resampling process,
therefore, under-(cid:976)itting or over-(cid:976)itting the data, respectively. To avoid such issues,
advanced resampling methods were developed based on the idea of a guided
resampling. Advanced resampling methods include multiple variations of under-
sampling and over-sampling methods [35, 36]
2.1.1. Under-sampling Methods
Under-sampling following the Nearest Neighbor (NN0 rule is the classi(cid:976)ication of
data based on the similarities between the data point and its nearest neighbor. This
decision rule has a lower probability of error than several other decision rules.
Variation of under-sampling based on NN rule includes condensed NN method, the
edited NN method, the repeated edited NN method, and neighborhood cleaning
method [37] and other variations [38, 39]. Tomek’s links (T-link) is an enhancement
of NN rule for under-sampling the majority class in which the pair of data with
opposite labels in the same neighborhood create a Tomek link. The data point on the
link that belongs to the majority class is removed. This method improves the
classi(cid:976)ication accuracy of the minority class by creating a distinct margin between the
two classes [40]. Under-sampling based on clustering utilizes the clustering
algorithms such as K-means that show promising performance with imbalanced data
[41]. The one-sided selection method is an adaptation of Tomek’s link. In this method,
a subset of the majority class is selected for classi(cid:976)ication while the minority class
remains untouched [42]. Under-sampling based on Instances Hardness Threshold
(IHT) method is used to overcome the problem of imbalanced data. This under-
sampling method reduces the size of the majority class by removing the data that has
a high hardness threshold, which is the probability of misclassi(cid:976)ication of the data
[43, 44, 45].
11

2.1.2. Over-sampling Methods
An effective way of dealing with the issue of imbalanced data is Over-sampling.
Studies suggest that the number of features and imbalance ratio are important factors
in determining the best approach [46, 47]. Over-sampling methods such as bootstrap-
based over-sampling, over-sampling based on Synthetic Minority Over-sampling
Technique (SMOTE), and over-sampling based on Adaptive Synthetic sampling method
(ADASYN) are widely used in imbalanced learning [48, 49, 50, 51, 52, 53, 54]
Bootstrap-based over-sampling is iteratively replicating the instances of a selected
sample, in which the instances are replaced and are probable to be selected more than
once. The number of iterations and the sample size is required before oversampling
[55, 56].
In over-sampling using SMOTE, the number of instances in the minority class
is increased by syntactically creating new instances instead of merely replicating
the existing instances. SMOTE generates data in the feature space, and it depends
on introducing new instances based on the nearest neighbors [57]. In this method,
the new examples are added near the line segment that joins the nearest
neighbors of the minority class. The nearest neighbors are selected to create the
instances required for over-sampling [58, 59, 60, 61, 62, 63, 64, 65, 66]. Inspired
by SMOTE, XiChen et al. [67] proposed a sampling method, in which new synthetic
neighborhood samples are generated. Controlling the number of generated
samples can improve the balance ratio and promote diversity in the data. Zhou et
al. [68] proposed a cost-sensitive SMOTE for data classi(cid:976)ication. Since the samples
are generated in the feature space, creating a new sample in a nonlinear space can
improve the results after resampling of the minority class [69].
Among different variations of SMOTE, ADASYN, motivated by SMOTE, is a
popular oversampling method, in which the data is synthetically generated to
increase the size of the minority class. The size of the generated data is determined
by the density distribution criteria de(cid:976)ined for each example which is an advantage
over SMOTE in that the number of generated data is predetermined [70, 71, 72].
The over-sampling methods are not limited to the ones mentioned in this paper.
These methods can be applied alone or in combination with each other to improve
12

classi(cid:976)ication results [73]. For example, in this paper, the authors combined the
ADASYN method with a cost-sensitive base model to improve the results in a study
of the transient stability of power systems [74].
Many studies have been carried out to evaluate the effectiveness and ef(cid:976)iciency
of resampling methods, and provide a guideline on selecting the best one for the
speci(cid:976)ic data [75, 76, 77, 78]. Figure 4 provides a structured overview of
resampling methods used in data processing approach. Over the years, different
variations of resampling methods are used in combination with algorithmic
approaches to enhance the prediction accuracy in imbalanced data .
Data Processing Approach
Resampling Methods
Basic Resamp ling Advanced Resa mpling Ensemble
Methods Methods Methods
Random Ov er- Advanced Unde-r Advanced Over- Com bination of
sampling sampling Methods sampling Methods Over-sam pling and
Random Und er- Under- sampling Boot- s t rap based
Und
m
er
e
-s
th
a
o
m
d
p
s
l ing
sampling based on Neares t Over-sampling
Neighbor (NN)
• •
• •
C E
R N N C M
d o
e l N e e e
i
p
n
i t
t
a g e h
d e
n h a
d
o
e
i b t
n
n d e
N
o
s
g d r
e N
h
d
E o d
N
o i d t
N
e d One
T
-
o
s
m
i M d
e
e e
k
d t
’
h S
s
o e
L
d l
i
e
n
c
k
ti o n
O
A S
v
d a O
e
a m
r
(
o
-
v p A
s
n
p e t
a
D i r l
m
-
S
v i s n A e
M
a
p
g S m S
l
O
i
M Y y
n
p
T
n
g
N l e i t
E
t n h
b
) h
a
g e o t
s
d i
e
c
d
Under-sampling
H
B
a
a
r
s
d
e
n
d
e
o
ss
n
T
In
h
s
r
t
e
a
s
n
h
c
o
e
l
s
d
Figure 4: Data Processing Methods in Imbalanced Learning
3. Algorithmic Approaches
3.1. Cost-sensitive Methods
In real-world applications of imbalanced learning, such as cancer diagnosis, fraud
detection, or severe weather prediction; the misclassi(cid:976)ication cost is different for the
minority class and the majority class, respectively. In imbalanced learning where the
misclassi(cid:976)ication cost of the minority class is more important, cost-sensitive methods
are used. In cost-sensitive methods, the cost of misclassi(cid:976)ication is known and de(cid:976)ined
in a cost matrix based on the cost associated with a false positive and a false negative.
The goal is to classify the data while minimizing the expected misclassi(cid:976)ication cost of
making a false prediction. In imbalanced learning, we can bene(cid:976)it from shifting the
13

classi(cid:976)ication algorithm towards further minimizing the misclassi(cid:976)ication error of the
minority class [79][80]. Cost-sensitive methods are categorized as direct and meta-
learning methods.
3.1.1. Direct Methods
In the direct methods, the classi(cid:976)iers are designed to anticipate different
misclassi(cid:976)ication costs for false positives and false negatives. Cost-sensitive decision
trees are an example of such methods that have improved the classi(cid:976)ication results
by incorporating the cost in the model and aiming to minimize the misclassi(cid:976)ication
cost [81, 82, 83, 84, 85, 86]. In other Cost-sensitive methods, weights are used in the
classi(cid:976)ication algorithm [87]. Studies show that iterative weighting of the samples
can improve the results as well as achieving computational ef(cid:976)iciency [88, 89]. Cost-
sensitive boosting methods have also been used to compare the effectiveness of such
algorithms on benchmark datasets [90, 91]. Wu et al. [92] used a cost-sensitive
multi-set feature learning on multiple samples constructed by partitioning the
majority class and combining the blocks with the minority class to obtain balanced
datasets. The model is evaluated using benchmark data sets and recommended for
highly imbalanced data. One of the challenges of cost-sensitive methods is
identifying the misclassi(cid:976)ication costs.
Zhang et al [93] proposed an adaptive differential evolution to (cid:976)ind the optimal
misclassi(cid:976)ication costs.
3.1.2. Meta-learning Methods
Meta-learning methods are used to convert cost-insensitive classi(cid:976)iers into
cost-sensitive algorithms without making modi(cid:976)ications to the algorithm by
thresholding and sampling methods. Thresholding models classify the data by
producing probability estimations using a cost-insensitive algorithm and use a
threshold to classify the data [94, 95, 96]. Thresholding is an effective method that
expands the space and increases the probability of classifying the instances
associated with the minority class. Therefore, they often produce the lower
misclassi(cid:976)ication cost comparing to other classi(cid:976)ication methods [97]. Sampling
meta-learning methods modify the class distributions in the dataset, before
14

training the data using a cost-insensitive classi(cid:976)ier. Weighing is also a type of
sampling method in which a normalized weight based on the misclassi(cid:976)ication cost
is assigned to the data before classi(cid:976)ication[98, 99]. Cost-sensitive learning is most
effective when embedded in the machine learning based model, categorized as
Ensemble methods. Ensemble methods are discussed thoroughly in a separate
section.
3.2. Machine Learning Based Modeling
Various machine learning models have been explored in the attempt to minimize
the misclassi(cid:976)ication error of the minority class such as Logistic Regression (LR),
Arti(cid:976)icial Neural Networks (ANNs) [100], Random Forest (RF), Decision
Trees (DT), Naive Bayes (NB), and Gaussian NB, and K-Nearest-Neighbor (KNN),
Support Vector Machines (SVM).Empirical studies on benchmark data suggest
different base predictor models [101, 102].
3.2.1. Tree-based Models
DT is a classi(cid:976)ication algorithm that splits the data set into smaller subsets to
predict the output value of the test data. The conditions by which the data is split
are called leaves, and the decision is known as a branch. The data is split until we
have reached the depth of the tree and no further split is possible. DT is a fast and
simple algorithm in which the process of classi(cid:976)ication and inquiries made are
clear [103, 104, 105, 106, 107, 108].
RF is a powerful ensemble method, which is an aggregation of less accurate
predictive models to create a better model. This model is used for regression or
classi(cid:976)ication. In RF classi(cid:976)ication, decision trees are used to introduce
randomness when selecting the suboptimal splits, and the goal is to aggregate as
many uncorrelated trees as possible and improve the accuracy at each step [109,
110, 111, 112, 113].
3.2.2. Probabilistic Models
NB is a supervised learning method. The (cid:976)irst assumption in this method is that
all the data points are independent of one another. This is an unrealistic yet helpful
assumption for training the data. In this method, the training data is used to
15

calculate the probability of each class and the conditional probability of each class
for a given data point. These two pieces of information are used to predict the class
of new data points. Gaussian NB is a modi(cid:976)ication of the NB method, except that
for the input data in real values, a Gaussian distribution is assumed to make
calculating the probabilities easier [114, 115]
3.2.3. Neighborhood-based Models
KNN is a simple yet powerful algorithm that uses the whole dataset for
classi(cid:976)ication. To classify a new data point, KNN uses the data points closer to the
designated point based on their Euclidean distance. Then it summarizes their
output values and assigns the result as the label of the new data point. In KNN,
training, and testing are combined in one step which increases the effectiveness and
ef(cid:976)iciency of the model which is one of the widely used imbalanced learning models.
The papers [116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
126, 127] are representative of those methods.
3.2.4. Kernel-based Models
Linear and logistic regression are probably the most well-known and widely
used machine learning algorithms. Linear regression is used for predicting values
that are in a range, but logistic regression is appropriate when we are trying to
predict categorical output values such as binary classi(cid:976)ication [128]. LR is
presented by a non-linear function, and the data is classi(cid:976)ied based on the features
correlated with the output variable [129, 130, 131]. To further improve the
traditional LR, Ohsaki et al. [132] proposed a novel confusion-based kernel logistic
regression that utilized a harmonic mean objective function to improve
generalization and classi(cid:976)ication errors of the model. Historically, in the 1950s and
1960s, perceptron algorithms were used for detecting linear relations in the data.
Perceptron algorithm is one of the oldest machine learning algorithms. In this
method, we need to associate a weight to the data points and de(cid:976)ine a threshold,
known as bias. The weights and the threshold are extracted from the data. The
weighted sum of the input data is calculated for predicting the output value. The
label is one if the sum is greater than the designated threshold, and zero otherwise.
16

In perceptron algorithm, the goal is to (cid:976)ind the set of weights that best classi(cid:976)ies
the data. Nieminen et al. [133] demonstrated the use of a single layer perceptron
based on a multi-criteria optimized MLP as the base model. Although perceptron
algorithms were useful for processing linear relations in the data, developing
ef(cid:976)icient and stable algorithms for detecting nonlinear relations was a major
challenge for researchers at the time. In the mid-1980s, back-propagation Neural
Networks (NNs) and decision trees revolutionized the (cid:976)ield of non-linear pattern
analysis. In the mid-1990s, kernel-based methods were developed for nonlinear
data analysis while retaining the ef(cid:976)iciency and stability of previous linear
algorithms. Kernel-based methods apply to a broad range of data types such as
sequence, text, image, graph, and vectors. They can detect different types of linear
and non-linear relations and they are used for correlation, factor, cluster, and
discriminant analysis. Kernel methods have a modular framework, in which (cid:976)irst
the data is processed into a kernel matrix, then the data is analyzed using various
pattern analysis algorithms based on the information contained in the kernel
matrix [134, 135, 136, 137, 138, 139]. Kernel matrix is obtained from mapping the
data from the input space into a higher dimensional feature space, using a
transformation function denoted as φ(x). One of the challenges in kernel method
is (cid:976)inding the kernel map, which is computationally expensive and sometimes
impossible, therefore, kernel functions are de(cid:976)ined by the dot product of the points
in the input space. Using this feature, known as the kernel trick, K(x,y) =
i j
φ(x
i
)T.φ(x
j
), the data is mapped into the feature space, without explicitly de(cid:976)ining
the map. Different kernel functions have been developed. Kernel methods utilize
a higher dimensional feature space to facilitate accurately classifying the minority
class [140].
Among different classi(cid:976)iers, kernel-based SVM as introduced by Vapnik [141][142]
has been widely used for imbalanced learning. SVM is a family of algorithms that use
kernel methods to solve problems in classi(cid:976)ication and regression [143, 144, 145, 146,
147]. The idea of kernel SVM is to map the data to a higher dimensional feature space
using a linear or nonlinear kernel [148, 149]. Then (cid:976)inding a separating hyperplane to
maximize the margin of separation while minimizing the misclassi(cid:976)ication error by
17

solving a quadratic optimization problem. SVMs are commonly used for classifying
large data sets. The data is classi(cid:976)ied based on its location on either side of a
hyperplane, which splits the input space. The separating hyperplane is not unique;
however, the best hyperplane is the one that maximizes the margin of separation
while minimizing the misclassi(cid:976)ication error. Combining cost-sensitive methods with
SVM is a useful method for improving the misclassi(cid:976)ication cost [150, 151]. Cost-
sensitive SVM embedded into the objective function can directly improve the
classi(cid:976)ication performance when the feature set and tuning parameters are optimized
[152]. Focusing on ROC and the AUC, Hu et al. [153] proposed the kernel online
imbalanced learning algorithm that aims to maximize the AUC score while
maintaining the regularization capabilities of the classi(cid:976)ier. Weighted under-sampling
SVM has improved the classi(cid:976)ication performance of SVM for imbalanced data [154].
Variations of SVM have been used for many applications such as fraud detection,
gene pro(cid:976)iling, weather prediction, etc [155, 156].
3.2.5. Deep Imbalanced Learning
ANN is a machine learning algorithm developed for separating non-linear data.
In this method, a large number of units known as neurons are connected to form
a multi-layer neural network. The neurons are divided into three types, input units
that receive the information for processing, output units that contain the
processing results, and the units in between known as hidden units. The ef(cid:976)iciency
of ANNs depends on the input units and their corresponding activation functions,
the network architecture, and the weights of input connections, and the calculated
weights of hidden units updated throughout the learning process.
ANNs apply to various real-world problems as well as imbalanced data [157, 158].
ANNs are studied with cost-sensitive methods to improve misclassi(cid:976)ication cost by
moving the classi(cid:976)ication threshold closer to the majority class, which allows more
instances to be classi(cid:976)ied as the minority class. Other methods are imposing
greater weights on the samples associated with the minority class
[159, 160]. Ya-Guan et al. [161] proposed an improved ANNs method called the
Equilibrium Mini-batch Stochastic Gradient Descent that improves the model’s
training convergence error.
18

In recent years, Extreme Learning Machine (ELM) for NN structures proposed
by Huang et al. [162] has been applied extensively for real-world imbalanced
learning problems. Some of the proposed strategies based on ELM are Weighted
ELM [163, 164, 165]. Class-speci(cid:976)ic ELM [166], and Class-speci(cid:976)ic Kernel ELM [167,
168] that have had promising results. When dealing with imbalanced data, deep
learning algorithms face the same issues as traditional machine learning
algorithms, and they fail to perform equally well in both classes [169]. Deep
imbalanced learning models are developed to address the issue of imbalanced data
in image recognition and computer vision [170? , 171].
Lin et al. [172] proposed a hybrid sampling method to remove the between
class data points and guide the network to improve the classi(cid:976)ication results [173].
Dong et al.[174] developed a deep learning model to classify imbalanced datasets
by imposing a class recti(cid:976)ication loss as a regularization parameter to discover the
boundaries in the minority class and reduce the effect of the majority class on the
model. Bao et al. [175] introduced a deep learning framework to balance the data
in a deeply transformed latent space. The superiority of this model is that feature
learning, balancing, and discriminative learning are conducted simultaneously
and it performs effectively on multi-classi(cid:976)ication problems. A cost-sensitive deep
NN proposed by Khan et al. [176] is a robust feature representation of both classes.
Therefore, it can have improved predictive capability. Lin et al. [177] proposed a
deep reinforcement learning model based on the reward function speci(cid:976)ied for the
minority and the majority class.
3.2.6. Ensemble Methods
Ensemble methods is an approach in machine learning that utilizes multiple
machine learning based models to improve predictive accuracy. A group of ensemble
methods is formed based on Bootstrap Aggregating (Bagging) in which several
bootstrapped subsamples are created and trained using a base model [178, 179].
Later the model aggregates the decision tree models to create the optimal predicting
ensemble method [180]. Random forest models are another type of ensemble
method which is a variation of Bagging, in which splitting the tree based on different
features creates a more accurate model. For imbalanced learning, cost-sensitive
19

decision trees are introduced [181]. Another ensemble method called CSRoulette is
introduced that improves the performance by producing samples of different sizes
based on a cost-sensitive model, combined with Bagging [182]. An empirical study
of ensemble methods and meta-learning methods suggests that although these
methods are effective for binary classi(cid:976)ication of imbalanced data, they might not
perform well on multi-class classi(cid:976)ication problems. For multi-classi(cid:976)ication
problems, a combination of LR and KNN is used. In the LR part of the model, an
ensemble of Bagging and Boosting methods has resulted in a promising outcome
[183]. Variations of the Boosting algorithms such as Adaptive Boosting (Adaboost)
have shown promising results
in classifying imbalanced data [184]. A comparison of various ensemble methods
suggests that combining data preprocessing approaches, such as RUS with Bagging
or Boosting methods can result in higher performance [185]. An ensemble of
random subsampling with RF has reasonable performance [186, 187]. Modifying
the objective function to anticipate different factors to minimize the
misclassi(cid:976)ication error in combination with evolutionary under-sampling methods
is an example of ensemble methods aiming to improve the results of imbalanced
learning [188]. Ensemble methods with multi-objective optimization function
provide powerful algorithms for imbalanced learning [189, 190]. Ensemble
methods are also effective for highly imbalanced data [191]. For image recognition,
ensemble deep imbalanced learning with a focus on resampling the data, and a
weighted loss function has improved the image classi(cid:976)ication results [192]. Wu et
al. [193] used a genetic algorithm approach with a deep imbalanced learning model
to optimize oversampling the minority class. Despite being able to improve the
classi(cid:976)ication results, ensemble methods are computationally complex. A structured
overview of the methods used in algorithmic approach is presented in Figure 5.
20

Figure 5: Algorithmic Approaches in Imbalanced Learning
4.  Applications
Classi(cid:976)ication of imbalanced data is a challenging task and it is one of the
popular research problems with many applications in the real world [194, 195].
In this section we have presented some of the highly impactful imbalanced
learning problems, however, the applications of imbalanced learning are not
limited to the mentioned examples. Figure 6 provides an overview of areas in
which imbalanced learning is used.
|                     |               |                       |   Infr | a s tr u ctu r e a n d  I n du s t r ial  |
| ------------------- | ------------- | --------------------- | ------ | ----------------------------------------- |
|                     | Cybersecurity |                       |        | S y s t em s  M a n ag e m e n t          |
| Bioengineering and  |               | Software Management   |        |                                           |
|                     |               | and Malware Detection |        |                                           |
Bioinformatics

Risk Assessment

|     | Natural Disaster  | Energy Management |     |     |
| --- | ----------------- | ----------------- | --- | --- |
and Rare Event

Prediction
Emergency and Resource
|     |     |     |     | Management   |
| --- | --- | --- | --- | ------------ |
Financial
Management

|     |             |                 |     |              |
| --- | ----------- | --------------- | --- | ------------ |
|     | Other Areas |                 |     | Behavior     |
|     |             | Computer Vision |     | Management   |

Business
Management
Figure 6: Applications of Imbalanced Learning
21

4.1. Risk Assessment in Business and Finance
In business analytics, bankruptcy prediction is an imbalanced learning problem.
Gnip et al. [196] used multiple ensemble methods to accurately predict the data
collected from medium-sized enterprises in the Slovak Republic [197]. In banking,
credit scoring and evaluating the potential risk posed by applicants’ unpaid loans is
an important issue, and due to frequency, it is an example of imbalanced data [198,
199, 200]. For example, detecting fraudulent transactions using ensemble methods
[201] and evaluating loan and credit applications can bene(cid:976)it from imbalanced
learning to support the decision-making process. Approval or rejection of loans
based on the applicant’s credit history is an imbalanced learning problem with
unpaid loan creating the minority class [202, 203, 204].
Fraud detection is one of the major applications of imbalanced learning algorithms.
Bauder et al. [205] compared the performance of different resampling approaches
on highly imbalanced data from Medicare to detect fraudulent cases.
4.2. Behavior Management
Imbalanced learning is also applicable to the data collected from Socioeconomic
systems. For example, Orooji et al. [206] predicted the rate of high school dropout
in Louisiana, US., which has negative impacts on the well-being of society, and Zheng
et al. [207] explored a short tree-based adaptive classi(cid:976)ication test to assess the risk
factors for juvenile delinquency.
4.3. Cybersecurity and Software Management
In cybersecurity, spam and software defect detection is an example of imbalanced
learning [208, 209, 210, 211]. Chen et al. [212] proposed an ensemble model based
on Choquet fuzzy integral with an improved SMOTE resampling technique for bug
report identi(cid:976)ication that can prevent damage to software. Developing effective
Intrusion Detection systems (IDS) is essential to cybersecurity [213]. Karatas et al.
[214] used the SMOTE resampling method to improve IDS performance. Feng et al.
[215] tackled the issue of imbalanced data in IDS classi(cid:976)ication using a cost-sensitive
feature engineering method based on General Vector Machine(GVM) and Binary Ant
Lion Optimizer. Zheng et al. [216] used a modi(cid:976)ied SVM to improve of(cid:976)line signature
22

veri(cid:976)ication systems. Pang et al. [217] used an ensemble of SMOTE and SVM to detect
malicious apps for android
users.
4.4. Natural Disasters and Emergency Management
An impactful application of imbalanced learning is predicting rare natural
disasters. Fernandez-Gomez et al. [218] studied the use of ensemble methods on
predicting rare large magnitude earthquakes with a horizon of prediction of (cid:976)ive
days in Chile. Seismic capability evaluation of buildings is also an imbalanced
learning problem in earthquake engineering [219]. Predicting severe weather
events such as tornado is an imbalanced learning problem in meteorology and
data mining [220, 221, 222]. Optimizing the available resources in urgent care is
important in times of crisis. An ensemble method consisting of Bagging and DT
can improve the prediction results for patient readmission to the emergency
department of a hospital in Chile [223].
4.5. Bio-informatics and Bio-engineering
Medical diagnosis is an example of imbalanced learning in the (cid:976)ield of bioinformatics
and bioengineering. Zhang et al. [224], explored the use of an ensemble method of RUS
with K-means and SVM to improve the diagnosis accuracy. Zheng et al. [225] used a
Convolutional Neural Network (CNN) to detect exudate in optic images, that if detected
correctly can prevent diabetic retinopathy and blindness. Jeong et al. [226] addressed
the issue of multi-classi(cid:976)ication of imbalanced kidney data. In this paper, the glomerular
rate is de(cid:976)ined as target to diagnose chronic kidney disease. The goal is to classify the
data into (cid:976)ive stages using four methods of multinomial LR, and ordinal LR, RF, and
Autoencoder (AE). The comparison of the four models suggests that AE provides better
performance and is recommended for similar problems. Farhadi et al. [227] used a deep
transfer learning model on constructing medical image data to evaluate the model’s
ef(cid:976)iciency in diagnosing high-grade breast cancer. A breast cancer diagnosis has been
improved by advanced imbalanced learning methods introduced in the past decade
[228, 229, 230]. Other cost-sensitive methods have also been used to improve the
classi(cid:976)ication accuracy of medical diagnosis [231, 232]. Deng et al. [233] have introduced
23

a dynamic clustering method that iteratively adjusts the cluster based on the weight
changes in the cluster. This algorithm is evaluated using gene expression cancer
diagnosis data and applies to biological and cyber-physical systems. A deep imbalanced
learning framework applies to different (cid:976)ields such as active balancing in biomedical
data
[234].
4.6. Computer Vision
Image processing and recognizing facial images and other attributes in detail
is a challenging task in computer vision, and the dif(cid:976)iculties escalate when the data
is imbalanced [235, 236, 237]. Various ensemble methods have been explored to
classify multimedia data [238]. Pouyanfar et al. [239] proposed an ensemble deep
learning framework based on the performance of SVM classi(cid:976)iers on deep feature
sets which is evaluated using multi-media data for semantic event detection. In
terms of application, different packages exist that can be used to implement the
models in Python, R, or other scripting languages [240].
Future Research Trends
Learning from imbalanced data is one of the challenging tasks in data mining.
However, it gets even more dif(cid:976)icult when it is combined with other issues. Different
studies have been carried out to explore strategies for speci(cid:976)ic issues of the minority
class, such as highly imbalanced cases, noisy data [4], outliers, sparse data [241,
242] and the problem of imbalanced distribution within the minority class [243,
244]. Another category of imbalanced learning problems is multi-class problems
that require more advanced techniques to deal with imbalanced data [245, 246].
Some of the proposed strategies such as weighted extreme learning machines,
weighted support vector machines [247], and sequential ensemble learning have
been relatively effective in the case of highly imbalanced data [248, 249, 250].
However, these methods are computationally complex and further improvement is
desired. A real-world application of imbalanced learning is time series analysis with
imbalanced and skewed data. This is particularly challenging due to the high
dimension of the data and underlying correlations within the data, and further
24

exploration is desired [251, 252, 253]. Imbalanced learning is an often over-looked
issue in Online Learning of streaming data [254, 255]. Different methods such as
cost-sensitive methods have been explored in various studies evaluated based on
the imbalanced learning metrics [256].However, extensive research is required to
address the issues in online imbalanced learning
of large scale data. The last but not least is the problem of imbalanced Learning in
distributed framework [257, 258]. Decentralized data centers often cause skewed
class distribution in different classes. Distributed learning has gained more
attention in the past few years and tackling the issue of imbalanced data in such
framework is essential.
Conclusion
Extensive research has been carried out to improve and identify the best
approaches for imbalanced data in different (cid:976)ields from cyber-security to business
analytic and bio-informatics. In this paper, we have provided a review of the wide
range of methods applied to imbalanced data from a technical perspective.
Examples of real-world applications have also been reviewed. We have collected
and reviewed the papers published in peer-reviewed journals from 2000 to 2020
to understand the trends and advances in learning from imbalanced data and
provide insights for future research trends in this highly anticipated (cid:976)ield.
References
[1] S. M. Abd Elrahman, A. Abraham, A review of class imbalance problem,
Journal of Network and Innovative Computing 1 (2013) (2013) 332–340. [2] V.
Babar, R. Ade, A review on imbalanced learning methods, 2015.
[3] J. Gu, Y. Zhou, X. Zuo, Making class bias useful: A strategy of learning from
imbalanced data, in: International Conference on Intelligent Data
Engineering and Automated Learning, Springer, 2007, pp. 287–295.
25

[4] T. M. Khoshgoftaar, J. Van Hulse, A. Napolitano, Comparing boosting and
bagging techniques with noisy and imbalanced data, IEEE Transactions on
Systems, Man, and Cybernetics-Part A: Systems and Humans 41 (3) (2010)
552–568.
[5] A. Sonak, R. Patankar, A survey on methods to handle imbalance dataset,
Int. J. Comput. Sci. Mobile Comput 4 (11) (2015) 338–343.
[6] N. Japkowicz, S. Stephen, The class imbalance problem: A systematic study,
Intelligent data analysis 6 (5) (2002) 429–449.
[7] A. Fern´andez, S. del R´ıo, N. V. Chawla, F. Herrera, An insight into imbalanced
big data classi(cid:976)ication: outcomes and challenges, Complex & Intelligent
Systems 3 (2) (2017) 105–120.
[8] B. Krawczyk, Learning from imbalanced data: open challenges and future
directions, Progress in Arti(cid:976)icial Intelligence 5 (4) (2016) 221–232.
[9] G. E. Batista, R. C. Prati, M. C. Monard, A study of the behavior of several
methods for balancing machine learning training data, ACM SIGKDD
explorations newsletter 6 (1) (2004) 20–29.
[10] T. R. Hoens, N. V. Chawla, Imbalanced datasets: from sampling to classi(cid:976)iers,
Imbalanced learning: Foundations, algorithms, and applications (2013) 43–
59.
[11] N. V. Chawla, Data mining for imbalanced datasets: An overview, in:
Data mining and knowledge discovery handbook, Springer, 2009, pp. 875–
886.
[12] V. Ganganwar, An overview of classi(cid:976)ication algorithms for imbalanced
datasets, International Journal of Emerging Technology and Advanced
Engineering 2 (4) (2012) 42–47.
[13] G. Haixiang, L. Yijing, J. Shang, G. Mingyun, H. Yuanyue, G. Bing, Learning
from class-imbalanced data: Review of methods and applications, Expert
Systems with Applications 73 (2017) 220–239.
26

[14] A. Fern´andez, S. Garc´ıa, M. Galar, R. C. Prati, B. Krawczyk, F. Herrera,
Learning from imbalanced data streams, in: Learning from imbalanced data
sets, Springer, 2018, pp. 279–303.
[15] Y. Sun, A. K. Wong, M. S. Kamel, Classi(cid:976)ication of imbalanced data: A review,
International journal of pattern recognition and arti(cid:976)icial intelligence 23
(04) (2009) 687–719.
[16] A. Luque, A. Carrasco, A. Mart´ın, A. de las Heras, The impact of class
imbalance in classi(cid:976)ication performance metrics based on the binary
confusion matrix, Pattern Recognition 91 (2019) 216–231.
[17] D. J. Hand, Measuring classi(cid:976)ier performance: a coherent alternative to the
area under the roc curve, Machine learning 77 (1) (2009) 103–123.
[18] M. Bekkar, H. K. Djemaa, T. A. Alitouche, Evaluation measures for models
assessment over imbalanced data sets, J Inf Eng Appl 3 (10)
(2013).
[19] C. Ferri, J. Hern´andez-Orallo, R. Modroiu, An experimental comparison of
performance measures for classi(cid:976)ication, Pattern Recognition Letters 30 (1)
(2009) 27–38.
[20] M. Hossin, M. Sulaiman, A review on evaluation metrics for data
classi(cid:976)ication evaluations, International Journal of Data Mining &
Knowledge Management Process 5 (2) (2015) 1.
[21] M. Fatourechi, R. K. Ward, S. G. Mason, J. Huggins, A. Schl¨ogl, G. E. Birch,
Comparison of evaluation metrics in classi(cid:976)ication applications with
imbalanced datasets, in: 2008 Seventh International Conference on Machine
Learning and Applications, IEEE, 2008, pp. 777–782.
[22] D. R. Musicant, V. Kumar, A. Ozgur, et al., Optimizing f-measure with support
vector machines., in: FLAIRS conference, 2003, pp. 356–360.
27

[23] S. Boughorbel, F. Jarray, M. El-Anbari, Optimal classi(cid:976)ier for imbalanced data
using matthews correlation coef(cid:976)icient metric, PloS one 12 (6) (2017)
e0177678.
[24] Y. Rizk, N. Hajj, N. Mitri, M. Awad, Deep belief networks and cortical
algorithms: A comparative study for supervised classi(cid:976)ication, Applied
Computing and Informatics 15 (2) (2019) 81–93.
[25] Y. S. Aurelio, G. M. de Almeida, C. L. de Castro, A. P. Braga, Learning from
imbalanced data sets with weighted cross-entropy function, Neural
Processing Letters 50 (2) (2019) 1937–1949.
[26] C. Li, H. Li, A modi(cid:976)ied short and fukunaga metric based on the attribute
independence assumption, Pattern Recognition Letters 33 (9) (2012)
1213–1218.
[27] A. P. Bradley, The use of the area under the roc curve in the evaluation of
machine learning algorithms, Pattern recognition 30 (7) (1997) 1145–
1159.
[28] C. X. Ling, J. Huang, H. Zhang, et al., Auc: a statistically consistent and more
discriminating measure than accuracy, in: Ijcai, Vol. 3, 2003, pp. 519–524.
[29] N. Thai-Nghe, Z. Gantner, L. Schmidt-Thieme, A new evaluation measure for
learning from imbalanced data, in: The 2011 International Joint Conference
on Neural Networks, IEEE, 2011, pp. 537–542.
[30] L. A. Jeni, J. F. Cohn, F. De La
Torre, Facing imbalanced
data–recommendations for the use of performance metrics, in: 2013
Humaine association conference on affective computing and intelligent
interaction, IEEE, 2013, pp. 245–251.
[31] C. Phua, D. Alahakoon, V. Lee, Minority report in fraud detection:
classi(cid:976)ication of skewed data, Acm sigkdd explorations newsletter 6 (1)
(2004) 50–59.
28

[32] D. A. Cieslak, N. V. Chawla, A. Striegel, Combating imbalance in network
intrusion datasets., in: GrC, 2006, pp. 732–737.
[33] C. Sarada, M. SathyaDevi, Imbalanced big data classi(cid:976)ication using feature
selection under-sampling, CVR Journal of Science and Technology 17 (1)
(2019) 78–82.
[34] A. Liu, J. Ghosh, C. E. Martin, Generative oversampling for mining imbalanced
datasets., in: DMIN, 2007, pp. 66–72.
[35] A. More, Survey of resampling techniques for improving classi(cid:976)ication
performance in unbalanced datasets, arXiv preprint arXiv:1608.06048
(2016).
[36] M. S. Shelke, P. R. Deshmukh, V. K. Shandilya, A review on imbalanced data
handling using undersampling and oversampling technique, Int J Recent
Trends in Eng & Res 3 (2017) 444–449.
[37] J. Laurikkala, Improving identi(cid:976)ication of dif(cid:976)icult small classes by balancing
class distribution, in: Conference on Arti(cid:976)icial Intelligence in Medicine in
Europe, Springer, 2001, pp. 63–66.
[38] M. Koziarski, Radial-based undersampling for imbalanced
data
classi(cid:976)ication, Pattern Recognition 102 (2020) 107262.
[39] C. Wang, Y. Yang, Nearest neighbor with double neighborhoods
algorithm for imbalanced classi(cid:976)ication., International Journal of Applied
Mathematics 50 (1) (2020).
[40] S. S. Alduayj, K. Rajpoot, Predicting employee attrition using machine
learning, in: 2018 International Conference on Innovations in Information
Technology (IIT), IEEE, 2018, pp. 93–98.
[41] A. Onan, Consensus clustering-based undersampling approach to
imbalanced learning, Scienti(cid:976)ic Programming 2019 (2019).
29

[42] G. E. Batista, A. C. Carvalho, M. C. Monard, Applying one-sided selection to
unbalanced datasets, in: Mexican International Conference on Arti(cid:976)icial
Intelligence, Springer, 2000, pp. 315–325.
[43] S. Cateni, V. Colla, M. Vannucci, A method for
resampling
imbalanced datasets in binary classi(cid:976)ication tasks for real-world problems,
Neurocomputing 135 (2014) 32–41.
[44] B. W. Yap, K. Abd Rani, H. A. Abd Rahman, S. Fong, Z. Khairudin, N. N.
Abdullah, An application of oversampling, undersampling, bagging and
boosting in handling imbalanced datasets, in: Proceedings of the (cid:976)irst
international conference on advanced data and information engineering
(DaEng-2013), Springer, 2014, pp. 13–22.
[45] X.-Y. Liu, J. Wu, Z.-H. Zhou, Exploratory undersampling for class-imbalance
learning, IEEE Transactions on Systems, Man, and Cybernetics, Part B
(Cybernetics) 39 (2) (2008) 539–550.
[46] S. J. Dattagupta, A performance comparison of oversampling methods for
data generation in imbalanced learning tasks, Ph.D. thesis (2018).
[47] Z. Gong, H. Chen, Model-based oversampling for imbalanced sequence
classi(cid:976)ication, in: Proceedings of the 25th ACM International on Conference
on Information and Knowledge Management, 2016, pp. 1009–1018.
[48] G. Goel, L. Maguire, Y. Li, S. McLoone, Evaluation of sampling methods for
learning from imbalanced data, in: International Conference on Intelligent
Computing, Springer, 2013, pp. 392–401.
[49] A. Gosain, S. Sardana, Handling class imbalance problem using oversampling
techniques: A review, in: 2017 International Conference on Advances in
Computing, Communications and Informatics (ICACCI), IEEE, 2017, pp. 79–
85.
30

[50] R. Malhotra, J. Jain, Handling imbalanced data using ensemble learning in
software defect prediction, in: 2020 10th International Conference on Cloud
Computing, Data Science & Engineering (Con(cid:976)luence), IEEE, 2020, pp. 300–
304.
[51] Z. Wu, W. Lin, Y. Ji, An integrated ensemble learning model for imbalanced
fault diagnostics and prognostics, IEEE Access 6 (2018)
8394–8402.
[52] Q. Wang, Y. Zhou, W. Zhang, Z. Tang, X. Chen, Adaptive sampling
using self-paced learning for imbalanced cancer data pre-diagnosis, Expert
Systems with Applications 152 (2020) 113334.
[53] H. Guo, J. Zhou, C.-A. Wu, Imbalanced learning based on data-partition and
smote, Information 9 (9) (2018) 238.
[54] P. Skryjomski, B. Krawczyk, In(cid:976)luence of minority class instance types on
smote imbalanced data oversampling, in: (cid:976)irst international workshop on
learning with imbalanced domains: theory and applications, 2017, pp. 7–21.
[55] M. B. Lyons, D. A. Keith, S. R. Phinn, T. J. Mason, J. Elith, A comparison of
resampling methods for remote sensing classi(cid:976)ication and accuracy
assessment, Remote Sensing of Environment 208 (2018) 145–153.
[56] W. Zhang, R. Ramezani, A. Naeim, Wotboost: Weighted oversampling
technique in boosting for imbalanced learning, in: 2019 IEEE
International Conference on Big Data (Big Data), IEEE, 2019, pp. 2523–
2531.
[57] A. Fern´andez, S. Garcia, F. Herrera, N. V. Chawla, Smote for learning from
imbalanced data: progress and challenges, marking the 15-year anniversary,
Journal of arti(cid:976)icial intelligence research 61 (2018) 863–905.
[58] Y. Xie, T. Zhang, Imbalanced learning for fault diagnosis problem of rotating
machinery based on generative adversarial networks, in: 2018 37th Chinese
Control Conference (CCC), IEEE, 2018, pp. 6017–6022.
31

[59] N. V. Chawla, K. W. Bowyer, L. O. Hall, W. P. Kegelmeyer,
Smote: synthetic minority over-sampling technique, Journal of arti(cid:976)icial
intelligence research 16 (2002) 321–357.
[60] X.-L. Yang, D. Lo, X. Xia, Q. Huang, J.-L. Sun, High-impact bug report
identi(cid:976)ication with imbalanced learning strategies, Journal of Computer
Science and Technology 32 (1) (2017) 181–198.
[61] M. M. Rahman, D. N. Davis, Addressing the class imbalance problem in
medical datasets, International Journal of Machine Learning and Computing
3 (2) (2013) 224.
[62] W. Deng, L. Deng, J. Liu, J. Qi, Sampling method based on improved c4. 5
decision tree and its application in prediction of telecom customer churn,
International Journal of Information Technology and Management 18 (1)
(2019) 93–109.
[63] S. Hukerikar, A. Tumma, A. Nikam, V. Attar, Skewboost: An algorithm for
classifying imbalanced datasets, in: 2011 2nd International Conference on
Computer and Communication Technology (ICCCT-2011), IEEE, 2011, pp.
46–52.
[64] H. Han, W.-Y. Wang, B.-H. Mao, Borderline-smote: a new over-sampling
method in imbalanced data sets learning, in: International conference on
intelligent computing, Springer, 2005, pp. 878–887.
[65] Z. Hosenie, R. Lyon, B. Stappers, A. Mootoovaloo, V. McBride, Imbalance
learning for variable star classi(cid:976)ication, Monthly Notices of the Royal
Astronomical Society 493 (4) (2020) 6050–6059.
[66] N. V. Chawla, A. Lazarevic, L. O. Hall, K. W. Bowyer, Smoteboost: Improving
prediction of the minority class in boosting, in: European conference on
principles of data mining and knowledge discovery, Springer, 2003, pp. 107–
119.
[67] Z. Chen, T. Lin, X. Xia, H. Xu, S. Ding, A synthetic neighborhood
32

generation based ensemble learning for the imbalanced data classi(cid:976)ication,
Applied Intelligence 48 (8) (2018) 2441–2457.
[68] C. Zhou, B. Liu, S. Wang, Cmo-smote: misclassi(cid:976)ication cost minimization
oriented synthetic minority oversampling technique for imbalanced
learning, in: 2016 8th International Conference on Intelligent Human-
Machine Systems and Cybernetics (IHMSC), Vol. 2, IEEE, 2016, pp. 353–358.
[69] T. Zhang, X. Yang, G-smote: A gmm-based synthetic minority oversampling
technique for imbalanced learning, arXiv preprint arXiv:1810.10363
(2018).
[70] B. Tang, H. He, Kerneladasyn: Kernel based adaptive synthetic data
generation for imbalanced learning, in: 2015 IEEE Congress on Evolutionary
Computation (CEC), IEEE, 2015, pp. 664–671.
[71] S. Sharma, C. Bellinger, B. Krawczyk, O. Zaiane, N. Japkowicz, Synthetic
oversampling with the majority class: A new perspective on handling
extreme imbalance, in: 2018 IEEE International Conference on Data Mining
(ICDM), IEEE, 2018, pp. 447–456.
[72] H. He, Y. Bai, E. A. Garcia, S. Li, Adasyn: Adaptive synthetic sampling
approach for imbalanced learning, in: 2008 IEEE international joint
conference on neural networks (IEEE world congress on computational
intelligence), IEEE, 2008, pp. 1322–1328.
[73] J. Burez, D. Van den Poel, Handling class imbalance in customer churn
prediction, Expert Systems with Applications 36 (3) (2009) 4626–4636.
[74] B. Tan, J. Yang, Y. Tang, S. Jiang, P. Xie, W. Yuan, A deep imbalanced learning
framework for transient stability assessment of power system, IEEE Access
7 (2019) 81759–81769.
[75] G. M. Weiss, K. McCarthy, B. Zabar, Cost-sensitive learning vs. sampling:
Which is best for handling unbalanced classes with unequal error costs?,
Dmin 7 (35-41) (2007) 24.
33

[76] C. Drummond, R. C. Holte, et al., C4. 5, class imbalance, and cost sensitivity:
why under-sampling beats over-sampling, in: Workshop on learning from
imbalanced datasets II, Vol. 11, Citeseer, 2003, pp. 1–8.
[77] A. O. DURAHIM, Comparison of sampling techniques for imbalanced˙
learning, Y¨onetim Bili¸sim Sistemleri Dergisi 2 (2) (2016) 181–191.
[78] P. Poshala, et al., Why oversample when undersampling can do the job?,
Texas Instruments, Dallas, TX, USA, Application Rep. SLAA594A (2013).
[79] C. Elkan, The foundations of cost-sensitive learning, in: International joint
conference on arti(cid:976)icial intelligence, Vol. 17, Lawrence Erlbaum Associates
Ltd, 2001, pp. 973–978.
[80] P. Domingos, Metacost: A general method for making classi(cid:976)iers cost-
sensitive, in: Proceedings of the (cid:976)ifth ACM SIGKDD international conference
on Knowledge discovery and data mining, 1999, pp. 155–164.
[81] S. Lomax, S. Vadera, A survey of cost-sensitive decision tree induction
algorithms, ACM Computing Surveys (CSUR) 45 (2) (2013) 1–35.
[82] C. X. Ling, V. S. Sheng, Q. Yang, Test strategies for cost-sensitive decision
trees, IEEE Transactions on Knowledge and Data Engineering 18 (8) (2006)
1055–1067.
[83] Y. Sahin, S. Bulkan, E. Duman, A cost-sensitive decision tree approach for
fraud detection, Expert Systems with Applications 40 (15) (2013) 5916–
5923.
[84] J. Li, X. Li, X. Yao, Cost-sensitive classi(cid:976)ication with genetic programming, in:
2005 IEEE congress on evolutionary computation, Vol. 3, IEEE, 2005, pp.
2114–2121.
[85] A. Freitas, A. Costa-Pereira, P. Brazdil, Cost-sensitive decision trees applied
to medical data, in: International Conference on Data Warehousing and
Knowledge Discovery, Springer, 2007, pp. 303–312.
34

[86] J. V. Davis, J. Ha, C. J. Rossbach, H. E. Ramadan, E. Witchel, Cost-sensitive
decision tree learning for forensic classi(cid:976)ication, in:
European Conference on Machine Learning, Springer, 2006, pp. 622–629.
[87] B. Zadrozny, J. Langford, N. Abe, Cost-sensitive learning by cost-
proportionate example weighting, in: Third IEEE international conference
on data mining, IEEE, 2003, pp. 435–442.
[88] N. Abe, B. Zadrozny, J. Langford, An iterative method for multi-class cost-
sensitive learning, in: Proceedings of the tenth ACM SIGKDD international
conference on Knowledge discovery and data mining, 2004, pp. 3–11.
[89] X.-Y. Liu, Z.-H. Zhou, The in(cid:976)luence of class imbalance on cost-sensitive
learning: An empirical study, in: Sixth International Conference on Data
Mining (ICDM’06), IEEE, 2006, pp. 970–974.
[90] Q.-Y. Yin, J.-S. Zhang, C.-X. Zhang, S.-C. Liu, An empirical study on the
performance of cost-sensitive boosting algorithms with different levels of
class imbalance, Mathematical Problems in Engineering 2013 (2013).
[91] Y. Sun, M. S. Kamel, Y. Wang, Boosting for learning multiple classes with
imbalanced class distribution, in: Sixth International Conference on Data
Mining (ICDM’06), IEEE, 2006, pp. 592–602.
[92] F. Wu, X.-Y. Jing, S. Shan, W. Zuo, J.-Y. Yang, Multiset feature
learning for highly imbalanced data classi(cid:976)ication, in: Thirty-First AAAI
Conference on Arti(cid:976)icial Intelligence, 2017.
[93] C. Zhang, K. C. Tan, H. Li, G. S. Hong, A cost-sensitive deep
belief network for imbalanced classi(cid:976)ication, IEEE transactions on neural
networks and learning systems 30 (1) (2018) 109–122.
[94] N. A. Verdikha, T. B. Adji, A. E. Permanasari, Study of undersampling method:
Instance hardness threshold with various estimators for hate speech
classi(cid:976)ication, IJITEE (International Journal of Information
Technology and Electrical Engineering) 2 (2) (2018) 39–44.
35

[95] Y. Jiang, B. Cukic, Misclassi(cid:976)ication cost-sensitive fault prediction models, in:
Proceedings of the 5th international conference on predictor models in
software engineering, 2009, pp. 1–10.
[96] M. E. Bezerra, A. L. Oliveiray, P. J. Adeodatoz, Predicting software defects: A
cost-sensitive approach, in: 2011 IEEE International Conference on
Systems, Man, and Cybernetics, IEEE, 2011, pp.
2515–2522.
[97] V. S. Sheng, C. X. Ling, Thresholding for making classi(cid:976)iers cost-sensitive, in:
AAAI, Vol. 6, 2006, pp. 476–481.
[98] K. M. Ting, An instance-weighting method to induce cost-sensitive trees,
IEEE Transactions on Knowledge and Data Engineering 14 (3) (2002) 659–
665.
[99] H. Zhao, Instance weighting versus threshold adjusting for cost-sensitive
classi(cid:976)ication, Knowledge and Information Systems 15 (3) (2008) 321–334.
[100] M. A. Mazurowski, P. A. Habas, J. M. Zurada, J. Y. Lo, J. A. Baker, G. D. Tourassi,
Training neural network classi(cid:976)iers for medical decision making: The effects
of imbalanced datasets on classi(cid:976)ication performance, Neural networks 21
(2-3) (2008) 427–436.
[101] A. Shen, R. Tong, Y. Deng, Application of classi(cid:976)ication models on credit card
fraud detection, in: 2007 International conference on service systems and
service management, IEEE, 2007, pp. 1–4.
[102] R. Caruana, A. Niculescu-Mizil, An empirical comparison of supervised
learning algorithms. proceedings of the 23rd international conference on
machine learning, Pittsburgh (PA) (2006).
[103] J. R. Quinlan, Induction of decision trees, Machine learning 1 (1) (1986)
81–106.
36

[104] S. B. Kotsiantis, I. D. Zaharakis, P. E. Pintelas, Machine learning: a review of
classi(cid:976)ication and combining techniques, Arti(cid:976)icial Intelligence Review 26
(3) (2006) 159–190.
[105] E. W. Ngai, Y. Hu, Y. H. Wong, Y. Chen, X. Sun, The application of data mining
techniques in (cid:976)inancial fraud detection: A classi(cid:976)ication framework and an
academic review of literature, Decision support systems 50 (3) (2011) 559–
569.
[106] N. V. Chawla, C4. 5 and imbalanced data sets: investigating the effect of
sampling method, probabilistic estimate, and decision tree structure, in:
Proceedings of the ICML, Vol. 3, 2003, p. 66.
[107] W. Liu, S. Chawla, D. A. Cieslak, N. V. Chawla, A robust decision tree algorithm
for imbalanced data sets, in: Proceedings of the 2010 SIAM International
Conference on Data Mining, SIAM, 2010, pp. 766–777.
[108] V. Podgorelec, M. Zorman, Decision tree learning, Encyclopedia of
Complexity and Systems Science (2015) 1–28.
[109] L. Breiman, Random forests, Machine learning 45 (1) (2001) 5–32.
[110] I. Triguero, S. del R´ıo, V. L´opez, J. Bacardit, J. M. Ben´ıtez, F. Herrera, Rosefw-
rf: the winner algorithm for the ecbdl’14 big data competition: an extremely
imbalanced big data bioinformatics problem, Knowledge-Based Systems 87
(2015) 69–79.
[111] S. Del R´ıo, V. L´opez, J. M. Ben´ıtez, F. Herrera, On the use of mapreduce for
imbalanced big data using random forest, Information Sciences 285 (2014)
112–137.
[112] L. Zhou, H. Wang, Loan default prediction on large imbalanced data using
random forests, TELKOMNIKA Indonesian Journal of Electrical
Engineering 10 (6) (2012) 1519–1525.
37

[113] T. M. Khoshgoftaar, M. Golawala, J. Van Hulse, An empirical study of learning
from imbalanced data using random forest, in: 19th IEEE
International Conference on Tools with Arti(cid:976)icial Intelligence (ICTAI 2007),
Vol. 2, IEEE, 2007, pp. 310–317.
[114] I. Rish, et al., An empirical study of the naive bayes classi(cid:976)ier, in: IJCAI 2001
workshop on empirical methods in arti(cid:976)icial intelligence, Vol. 3, 2001, pp.
41–46.
[115] N. Friedman, D. Geiger, M. Goldszmidt, Bayesian network classi(cid:976)iers,
Machine learning 29 (2-3) (1997) 131–163.
[116] L. Borrajo, R. Romero, E. L. Iglesias, C. R. Marey, Improving imbalanced
scienti(cid:976)ic text classi(cid:976)ication using sampling strategies and dictionaries,
Journal of integrative bioinformatics 8 (3) (2011) 90–104.
[117] I. Mani, I. Zhang, knn approach to unbalanced data distributions: a case
study involving information extraction, in: Proceedings of workshop on
learning from imbalanced datasets, Vol. 126, 2003.
[118] X. Zhang, Y. Li, R. Kotagiri, L. Wu, Z. Tari, M. Cheriet, Krnn: k
rare-class nearest neighbour classi(cid:976)ication, Pattern Recognition 62 (2017)
33–44.
[119] M. Beckmann, N. F. Ebecken, B. S. P. de Lima, et al., A knn
undersampling approach for data balancing, Journal of Intelligent Learning
Systems and Applications 7 (04) (2015) 104.
[120] A. Majid, S. Ali, M. Iqbal, N. Kausar, Prediction of human breast and colon
cancers from imbalanced data using nearest neighbor and support vector
machines, Computer methods and programs in biomedicine 113 (3) (2014)
792–808.
[121] N. Tomaˇsev, D. Mladeni´c, Class imbalance and the curse of minority hubs,
Knowledge-Based Systems 53 (2013) 157–172.
38

[122] Y. Li, X. Zhang, Improving k nearest neighbor
with exemplar
generalization for imbalanced classi(cid:976)ication, in: Paci(cid:976)ic-Asia Conference on
Knowledge Discovery and Data Mining, Springer, 2011, pp. 321–332.
[123] T. Gao, Y. Hao, H. Zhang, L. Hu, H. Li, H. Li, L. Hu, B. Han, Predicting
pathological response to neoadjuvant chemotherapy in breast cancer
patients based on imbalanced clinical data, Personal and Ubiquitous
Computing 22 (5-6) (2018) 1039–1047.
[124] J. Hu, Y. Li, W.-X. Yan, J.-Y. Yang, H.-B. Shen, D.-J. Yu, Knn-based dynamic query-
driven sample rescaling strategy for class imbalance learning,
Neurocomputing 191 (2016) 363–373.
[125] C. Abeysinghe, J. Li, J. He, A classi(cid:976)ier hub for imbalanced (cid:976)inancial data, in:
Australasian Database Conference, Springer, 2016, pp. 476–479.
[126] X.-S. Hu, R.-J. Zhang, Clustering-based subset ensemble learning method for
imbalanced data, in: 2013 International Conference on Machine Learning
and Cybernetics, Vol. 1, IEEE, 2013, pp. 35–39.
[127] D. Wu, X. Chen, C. Chen, J. Zhang, Y. Xiang, W. Zhou, On addressing the
imbalance problem: a correlated knn approach for network traf(cid:976)ic
classi(cid:976)ication, in: International Conference on Network and System Security,
Springer, 2015, pp. 138–151.
[128] A. B. Owen, In(cid:976)initely imbalanced logistic regression, Journal of Machine
Learning Research 8 (Apr) (2007) 761–773.
[129] M. Maalouf, T. B. Trafalis, Robust weighted kernel logistic regression in
imbalanced and rare events data, Computational Statistics & Data Analysis
55 (1) (2011) 168–183.
[130] A. Dagliati, S. Marini, L. Sacchi, G. Cogni, M. Teliti, V. Tibollo, P. De Cata, L.
Chiovato, R. Bellazzi, Machine learning methods to predict diabetes
complications, Journal of diabetes science and technology 12 (2)
39

(2018) 295–302.
[131] S. Dreiseitl, L. Ohno-Machado, Logistic regression and arti(cid:976)icial neural
network classi(cid:976)ication models: a methodology review, Journal of biomedical
informatics 35 (5-6) (2002) 352–359.
[132] M. Ohsaki, P. Wang, K. Matsuda, S. Katagiri, H. Watanabe, A. Ralescu,
Confusion-matrix-based kernel logistic regression for imbalanced data
classi(cid:976)ication, IEEE Transactions on Knowledge and Data Engineering 29 (9)
(2017) 1806–1819.
[133] P. Nieminen, T. K¨arkk¨ainen, Multicriteria optimized mlp for imbalanced
learning., in: ESANN, 2016.
[134] D. Hand, The elements of statistical learning: Data mining, inference, and
prediction, Biometrics 58 (1) (2002) 252.
[135] J. Breneman, Kernel methods for pattern analysis (2005).
[136] J. Han, M. Kamber, J. Pei, Data mining: concepts and techniques, waltham,
ma, Morgan Kaufman Publishers 10 (2012) 978–1.
[137] I. H. Witten, E. Frank, Data mining: practical machine learning tools and
techniques with java implementations, Acm Sigmod Record 31 (1) (2002)
76–77.
[138] T. Evgeniou, C. A. Micchelli, M. Pontil, J. Shawe-Taylor, Learning multiple
tasks with kernel methods., Journal of machine learning research 6 (4)
(2005).
[139] J. Apostolakis, An introduction to data mining, in: Data Mining in
Crystallography, Springer, 2009, pp. 1–35.
[140] T. Hofmann, B. Sch¨olkopf, A. J. Smola, Kernel methods in machine learning,
The annals of statistics (2008) 1171–1220.
[141] V. N. Vapnik, An overview of statistical learning theory, IEEE transactions on
neural networks 10 (5) (1999) 988–999.
40

[142] C. Cortes, V. Vapnik, Support-vector networks, Machine learning 20 (3)
(1995) 273–297.
[143] S. Piri, D. Delen, T. Liu, A synthetic informative minority over-sampling
(simo) algorithm leveraging support vector machine to enhance learning
from imbalanced datasets, Decision Support Systems 106 (2018) 15–29.
[144] M. E. Abbasnejad, D. Ramachandram, R. Mandava, A survey of the state of
the art in learning the kernels, Knowledge and information systems 31 (2)
(2012) 193–221.
[145] X. Wang, E. P. Xing, D. J. Schaid, Kernel methods for large-scale genomic data
analysis, Brie(cid:976)ings in bioinformatics 16 (2) (2015) 183–192.
[146] A. B. Parsa, H. Taghipour, S. Derrible, A. K. Mohammadian, Real-time accident
detection: coping with imbalanced data, Accident Analysis & Prevention 129
(2019) 202–210.
[147] L. Wei, Y. Yang, R. M. Nishikawa, Y. Jiang, A study on several machine-learning
methods for classi(cid:976)ication of malignant and benign clustered
microcalci(cid:976)ications, IEEE transactions on medical imaging 24 (3) (2005)
371–380.
[148] S.-i. Amari, S. Wu, Improving support vector machine classi(cid:976)iers by
modifying kernel functions, Neural Networks 12 (6) (1999) 783–789.
[149] Y. B. Wah, H. A. A. Rahman, H. He, A. Bulgiba, Handling imbalanced dataset
using svm and k-nn approach, in: AIP Conference Proceedings, Vol. 1750,
AIP Publishing LLC, 2016, p. 020023.
[150] N. Thai-Nghe, Z. Gantner, L. Schmidt-Thieme, Cost-sensitive learning
methods for imbalanced data, in: The 2010 International joint conference
on neural networks (IJCNN), IEEE, 2010, pp. 1–8.
[151] Q. Yan, S. Xia, F. Meng, Optimizing cost-
sensitive svm for
41

imbalanced data: Connecting cluster to classi(cid:976)ication, arXiv preprint
arXiv:1702.01504 (2017).
[152] P. Cao, D. Zhao, O. Zaiane, An optimized cost-sensitive svm for imbalanced
data learning, in: Paci(cid:976)ic-Asia conference on knowledge discovery and data
mining, Springer, 2013, pp. 280–292.
[153] J. Hu, H. Yang, M. R. Lyu, I. King, A. M.-C. So, Online nonlinear auc
maximization for imbalanced data sets, IEEE transactions on neural
networks and learning systems 29 (4) (2017) 882–895.
[154] Q. Kang, L. Shi, M. Zhou, X. Wang, Q. Wu, Z. Wei, A distance-based weighted
undersampling scheme for support vector machines and its application to
imbalanced classi(cid:976)ication, IEEE transactions on neural networks and
learning systems 29 (9) (2017) 4152–4165.
[155] Y. Xu, Maximum margin of twin spheres support vector machine for
imbalanced data classi(cid:976)ication, IEEE transactions on cybernetics 47 (6)
(2016) 1540–1550.
[156] E. Jafarigol, T. Trafalis, Imbalanced learning with parametric linear
programming support vector machine for weather data application, SN
Computer Science 1 (6) (2020) 1–11.
[157] J. Schmidhuber, Deep learning in neural networks: An overview, Neural
networks 61 (2015) 85–117.
[158] A. Sonak, R. Patankar, N. Pise, A new approach for handling imbalanced
dataset using ann and genetic algorithm, in: 2016 International Conference
on Communication and Signal Processing (ICCSP), IEEE, 2016, pp. 1987–
1990.
[159] J. Zheng, Cost-sensitive boosting neural networks for software defect
prediction, Expert Systems with Applications 37 (6) (2010) 4537–4543.
42

[160] T. Ashihara, Y. Shinohara, H. Sato, T. Moriya, K. Matsui, T. Fukutomi, Y.
Yamaguchi, Y. Aono, Neural whispered speech detection with imbalanced
learning., in: INTERSPEECH, 2019, pp. 3352–3356.
[161] Q. Ya-Guan, M. Jun, Z. Xi-Min, P. Jun, Z. Wu-Jie, W. Shu-Hui, Y. Ben-Sheng, L.
Jing-Sheng, Emsgd: An improved learning algorithm of neural networks
with imbalanced data, IEEE Access 8 (2020)
64086–64098.
[162] G.-B. Huang, Q.-Y. Zhu, C.-K. Siew, Extreme learning machine: theory and
applications, Neurocomputing 70 (1-3) (2006) 489–501.
[163] H. Kaya, A. A. Karpov, Introducing weighted kernel classi(cid:976)iers for handling
imbalanced paralinguistic corpora: Snoring, addressee and cold., in:
INTERSPEECH, 2017, pp. 3527–3531.
[164] Y. Zhang, B. Liu, J. Cai, S. Zhang, Ensemble weighted extreme learning
machine for imbalanced data classi(cid:976)ication based on differential evolution,
Neural Computing and Applications 28 (1) (2017) 259–267.
[165] W. Zong, G.-B. Huang, Y. Chen, Weighted extreme learning machine for
imbalance learning, Neurocomputing 101 (2013) 229–242.
[166] B. S. Raghuwanshi, S. Shukla, Generalized class-speci(cid:976)ic kernelized extreme
learning machine for multiclass imbalanced learning, Expert Systems with
Applications 121 (2019) 244–255.
[167] Y.-P. Zhao, Y.-B. Chen, Z. Hao, H. Wang, Z. Yang, J.-F. Tan, Imbalanced kernel
extreme learning machines for fault detection of aircraft engine, Journal of
Dynamic Systems, Measurement, and Control 142 (10) (2020).
[168] B. S. Raghuwanshi, S. Shukla, Smote based class-speci(cid:976)ic extreme learning
machine for imbalanced learning, Knowledge-Based Systems 187 (2020)
104814.
43

[169] J. M. Johnson, T. M. Khoshgoftaar, Survey on deep learning with class
imbalance, Journal of Big Data 6 (1) (2019) 27.
[170] L. Zhang, C. Zhang, S. Quan, H. Xiao, G. Kuang, L. Liu, A class
imbalance loss for imbalanced object recognition, IEEE Journal of Selected
Topics in Applied Earth Observations and Remote Sensing 13 (2020) 2778–
2792.
[171] Q. Dong, S. Gong, X. Zhu, Imbalanced deep learning by minority class
incremental recti(cid:976)ication, IEEE transactions on pattern analysis and
machine intelligence 41 (6) (2018) 1367–1381.
[172] H.-I. Lin, C.-M. Nguyen, Boosting minority class prediction on imbalanced
point cloud data, Applied Sciences 10 (3) (2020) 973.
[173] T. Guo, X. Zhu, Y. Wang, F. Chen, Discriminative sample generation for deep
imbalanced learning., in: IJCAI, 2019, pp. 2406–2412.
[174] Q. Dong, S. Gong, X. Zhu, Class recti(cid:976)ication hard mining for imbalanced deep
learning, in: Proceedings of the IEEE International Conference on Computer
Vision, 2017, pp. 1851–1860.
[175] F. Bao, Y. Deng, Y. Kong, Z. Ren, J. Suo, Q. Dai, Learning deep landmarks for
imbalanced classi(cid:976)ication, IEEE Transactions on Neural Networks and
Learning Systems (2019).
[176] S. H. Khan, M. Hayat, M. Bennamoun, F. A. Sohel, R. Togneri,
Cost-sensitive learning of deep feature representations from imbalanced
data, IEEE transactions on neural networks and learning systems 29 (8)
(2017) 3573–3587.
[177] E. Lin, Q. Chen, X. Qi, Deep reinforcement learning for imbalanced
classi(cid:976)ication, Applied Intelligence (2020) 1–15.
[178] S. E. Roshan, S. Asadi, Improvement of bagging performance for
44

classi(cid:976)ication of imbalanced datasets using evolutionary multi-objective
optimization, Engineering Applications of Arti(cid:976)icial Intelligence 87 (2020)
103319.
[179] G. Collell, D. Prelec, K. R. Patil, A simple plug-in bagging ensemble based on
threshold-moving for classifying binary and multiclass imbalanced data,
Neurocomputing 275 (2018) 330–340.
[180] B. Wang, J. Pineau, Online bagging and boosting for imbalanced data
streams, IEEE Transactions on Knowledge and Data Engineering 28 (12)
(2016) 3353–3366.
[181] B. Krawczyk, M. Wo´zniak, G. Schaefer, Cost-sensitive decision tree
ensembles for effective imbalanced classi(cid:976)ication, Applied Soft Computing
14 (2014) 554–562.
[182] V. S. Sheng, C. X. Ling, Roulette sampling for cost-sensitive learning, in:
European Conference on Machine Learning, Springer, 2007, pp. 724–731.
[183] M. M. Javidi, F. Shamsezat, Learning from imbalanced multi-label data sets
by using ensemble strategies, Computer Engineering and Applications
Journal 4 (1) (2015) 61–81.
[184] C. Lingchi, D. Xiaoheng, S. Hailan, Z. Congxu, C. Le, Dycusboost: Adaboost-
based imbalanced learning using dynamic clustering and undersampling,
in: 2018 IEEE 16th Intl Conf on Dependable,
Autonomic and Secure Computing, 16th Intl Conf on Pervasive Intelligence
and Computing, 4th Intl Conf on Big Data Intelligence and Computing and
Cyber Science and Technology Congress
(DASC/PiCom/DataCom/CyberSciTech), IEEE, 2018, pp. 208–215.
[185] M. Galar, A. Fernandez, E. Barrenechea, H. Bustince, F. Herrera, A review on
ensembles for the class imbalance problem: bagging-, boosting-, and hybrid-
based approaches, IEEE Transactions on Systems, Man, and Cybernetics,
Part C (Applications and Reviews) 42 (4) (2011) 463–484.
45

[186] M. Khalilia, S. Chakraborty, M. Popescu, Predicting disease risks from highly
imbalanced data using random forest, BMC medical informatics and
decision making 11 (1) (2011) 51.
[187] L. Loezer, F. Enembreck, J. P. Barddal, A. de Souza Britto Jr,
Cost-sensitive learning for imbalanced data streams, in: Proceedings of the
35th Annual ACM Symposium on Applied Computing, 2020, pp. 498–504.
[188] B. Sun, H. Chen, J. Wang, H. Xie, Evolutionary under-sampling based bagging
ensemble method for imbalanced data classi(cid:976)ication, Frontiers of Computer
Science 12 (2) (2018) 331–350.
[189] V. H. A. Ribeiro, G. Reynoso-Meza, Ensemble learning by means of a multi-
objective optimization design approach for dealing with imbalanced data
sets, Expert Systems with Applications 147 (2020) 113232.
[190] Q. Li, Y. Song, J. Zhang, V. S. Sheng, Multiclass imbalanced learning with one-
versus-one decomposition and spectral clustering, Expert Systems with
Applications 147 (2020) 113152.
[191] Z. Liu, W. Cao, Z. Gao, J. Bian, H. Chen, Y. Chang, T.-Y. Liu, Self-paced ensemble
for highly imbalanced massive data classi(cid:976)ication, in: 2020 IEEE 36th
International Conference on Data Engineering (ICDE), IEEE, 2020, pp. 841–
852.
[192] R. Harliman, K. Uchida, Data-and algorithm-hybrid approach for imbalanced
data problems in deep neural network, International Journal of Machine
Learning and Computing 8 (3) (2018) 208–213.
[193] S. Dong, Y. Wu, A genetic algorithm-based approach for class-imbalanced
learning, in: Third International Workshop on Pattern Recognition, Vol.
10828, International Society for Optics and Photonics, 2018, p. 108281D.
[194] P. Branco, L. Torgo, R. P. Ribeiro, A survey of predictive modeling on
imbalanced domains, ACM Computing Surveys (CSUR) 49 (2) (2016)
1–50.
46

[195] H. Kaur, H. S. Pannu, A. K. Malhi, A systematic review on imbalanced data
challenges in machine learning: Applications and solutions, ACM Computing
Surveys (CSUR) 52 (4) (2019) 1–36.
[196] P. Gnip, P. Drot´ar, Ensemble methods for strongly imbalanced data:
bankruptcy prediction, in: 2019 IEEE 17th International Symposium on
Intelligent Systems and Informatics (SISY), IEEE, 2019, pp. 155–160.
[197] M. Zoriˇc´ak, P. Gnip, P. Drot´ar, V. Gazda, Bankruptcy prediction for small-
and medium-sized companies using severely imbalanced datasets,
Economic Modelling 84 (2020) 165–176.
[198] Q. Chang, S. Lin, X. Liu, Stacked-svm: A dynamic svm framework for
telephone fraud identi(cid:976)ication from imbalanced cdrs, in: Proceedings of the
2019 2nd International Conference on Algorithms, Computing and Arti(cid:976)icial
Intelligence, 2019, pp. 112–120.
[199] L. M. Junior, F. M. Nardini, C. Renso, R. Trani, J. A. Macedo, A novel approach
to de(cid:976)ine the local region of dynamic selection techniques in imbalanced
credit scoring problems, Expert Systems with Applications (2020) 113351.
[200] U. R. Salunkhe, S. N. Mali, Classi(cid:976)ier ensemble design for imbalanced data
classi(cid:976)ication: a hybrid approach, Procedia Computer Science 85 (2016)
725–732.
[201] S. Dhankhad, E. Mohammed, B. Far, Supervised machine learning
algorithms for credit card fraudulent transaction detection: a comparative
study, in: 2018 IEEE International Conference on Information Reuse and
Integration (IRI), IEEE, 2018, pp. 122–125.
[202] L. E. B. Ferreira, J. P. Barddal, H. M. Gomes, F. Enembreck, Improving credit
risk prediction in online peer-to-peer (p2p) lending using imbalanced
learning techniques, in: 2017 IEEE 29th International
Conference on Tools with Arti(cid:976)icial Intelligence (ICTAI), IEEE, 2017, pp.
175–181.
47

[203] L. S. de Melo Junior, F. M. Nardini, C. Renso, J. A. F. de Macˆedo, An empirical
| comparison  | of  | classi(cid:976)ication  | algorithms  |     | for  imbalanced  |     | credit  scoring  |
| ----------- | --- | ----------------------- | ----------- | --- | ---------------- | --- | ---------------- |
datasets, in: 2019 18th IEEE International Conference On
Machine Learning And Applications (ICMLA), IEEE, 2019, pp. 747–754.
| [204] A. Namvar, M.  |       | Siami,  | F.  | Rabhi,  | M.  | Naderpour, |     |
| -------------------- | ----- | ------- | --- | ------- | --- | ---------- | --- |
|   Credit             | risk  |         |     |         |     |            |     |
prediction in an imbalanced social lending environment, arXiv preprint
arXiv:1805.00801 (2018).
[205] R. A. Bauder, T. M. Khoshgoftaar, T. Hasanin, Data sampling approaches with
severely imbalanced big data for medicare fraud detection, in: 2018
IEEE 30th international conference on tools with arti(cid:976)icial intelligence
(ICTAI), IEEE, 2018, pp. 137–142.
[206] M. Orooji, J. Chen, Predicting louisiana public high school dropout through
| imbalanced  | learning  |     | techniques,  | in:  | 2019  18th  | IEEE  | International  |
| ----------- | --------- | --- | ------------ | ---- | ----------- | ----- | -------------- |
Conference on Machine Learning and Applications (ICMLA), IEEE, 2019, pp.
456–461.
[207] Y. Zheng, H. Cheon, C. M. Katz, Using machine learning methods to develop a
| short  tree-based  |       | adaptive  | classi(cid:976)ication  |             | test:  | Case  study  | with  a  high- |
| ------------------ | ----- | --------- | ----------------------- | ----------- | ------ | ------------ | -------------- |
| dimensional        | item  | pool      | and                     | imbalanced  | data,  | Applied      | Psychological  |
Measurement (2020) 0146621620931198.
[208] C. Zhao, Y. Xin, X. Li, Y. Yang, Y. Chen, A heterogeneous ensemble learning
framework for spam detection in social networks with imbalanced data,
Applied Sciences 10 (3) (2020) 936.
[209] Q. Song, Y. Guo, M. Shepperd, A comprehensive investigation of the role of
imbalanced learning for software defect prediction, IEEE Transactions on
Software Engineering 45 (12) (2018) 1253–1269.
[210] Y.-C. Chen, Y.-J. Li, A. Tseng, T. Lin, Deep learning for malicious (cid:976)low detection,
in: 2017 IEEE 28th Annual International Symposium on Personal, Indoor,
and Mobile Radio Communications (PIMRC), IEEE, 2017, pp. 1–7.
48

[211] H. Li, Y. Qu, S. Guo, G. Gao, R. Chen, G. Chen, Surprise bug
report prediction utilizing optimized integration with imbalanced learning
strategy, Complexity 2020 (2020).
[212] R. Chen, S.-K. Guo, X.-Z. Wang, T.-L. Zhang, Fusion of multi-rsmote with fuzzy
integral to classify bug reports with an imbalanced distribution, IEEE
Transactions on Fuzzy Systems 27 (12) (2019) 2406–2420.
[213] R. Abdulhammed, M. Faezipour, A. Abuzneid, A. AbuMallouh, Deep and
machine learning approaches for anomaly-based intrusion detection of
imbalanced network traf(cid:976)ic, IEEE sensors letters 3 (1) (2018) 1–4.
[214] G. Karatas, O. Demir, O. K. Sahingoz, Increasing the performance of machine
learning-based idss on an imbalanced and up-to-date dataset, IEEE Access
8 (2020) 32150–32162.
[215] F. Feng, K.-C. Li, J. Shen, Q. Zhou, X. Yang, Using cost-sensitive learning and
feature selection algorithms to improve the performance of imbalanced
classi(cid:976)ication, IEEE Access 8 (2020) 69979–69996.
[216] Y. Zheng, Y. Zheng, W. Ohyama, D. Suehiro, S. Uchida, Ranksvm
for of(cid:976)line signature veri(cid:976)ication, in: 2019 International Conference on
Document Analysis and Recognition (ICDAR), IEEE, 2019, pp. 928–933.
[217] Y. Pang, Z. Chen, X. Li, S. Wang, C. Zhao, L. Wang, K. Ji, Z. Li, Finding android
malware trace from highly imbalanced network traf(cid:976)ic, in: 2017 IEEE
International Conference on Computational Science and Engineering (CSE)
and IEEE International Conference on Embedded and Ubiquitous
Computing (EUC), Vol. 1, IEEE, 2017, pp. 588–595.
[218] M. J. Fern´andez-G´omez, G. Asencio-Cort´es, A. Troncoso, F. Mart´ınez-
Alvarez, Large earthquake magnitude prediction in chile´ with imbalanced
classi(cid:976)iers and ensemble learning, Applied Sciences 7 (6) (2017) 625.
[219] N.-W. Chi, J.-P. Wang, J.-H. Liao, W.-C. Cheng, C.-S. Chen,
Machine learning-based seismic capability evaluation for school buildings,
49

Automation in Construction 118 (2020) 103274.
[220] T. B. Trafalis, I. Adrianto, M. B. Richman, Active learning with support vector
machines for tornado prediction, in: International Conference on
Computational Science, Springer, 2007, pp. 1130–1137.
[221] T. B. Trafalis, I. Adrianto, M. B. Richman, S. Lakshmivarahan,
Machine-learning classi(cid:976)iers for imbalanced tornado data, Computational
Management Science 11 (4) (2014) 403–418.
[222] T. B. Trafalis, H. Ince, M. B. Richman, Tornado detection with support vector
machines, in: International Conference on Computational Science, Springer,
2003, pp. 289–298.
[223] A. Artetxe, M. Gran˜a, A. Beristain, S. R´ıos, Balanced training of a hybrid
ensemble method for imbalanced datasets: a case of emergency department
readmission prediction, Neural Computing and Applications 32 (10) (2020)
5735–5744.
[224] J. Zhang, L. Chen, F. Abid, Prediction of breast cancer from imbalance respect
using cluster-based undersampling method, Journal of healthcare
engineering 2019 (2019).
[225] R. Zheng, L. Liu, S. Zhang, C. Zheng, F. Bunyak, R. Xu, B. Li, M. Sun, Detection
of exudates in fundus photographs with imbalanced learning using
conditional generative adversarial network, Biomedical optics express 9
(10) (2018) 4863–4878.
[226] B. Jeong, H. Cho, J. Kim, S. K. Kwon, S. Hong, C. Lee, T. Kim, M. S. Park, S. Hong,
T.-Y. Heo, Comparison between statistical models and machine learning
methods on classi(cid:976)ication for highly imbalanced multiclass kidney data,
Diagnostics 10 (6) (2020) 415.
[227] A. Farhadi, D. Chen, R. McCoy, C. Scott, J. A. Miller, C. M. Vachon, C. Ngufor,
Breast cancer classi(cid:976)ication using deep transfer learning on structured
healthcare data, in: 2019 IEEE International Conference on
50

Data Science and Advanced Analytics (DSAA), IEEE, 2019, pp. 277–286.
[228] R. Singh, T. Ahmed, A. Kumar, A. K. Singh, A. K. Pandey, S. K.
Singh, Imbalanced breast cancer classi(cid:976)ication using transfer learning,
IEEE/ACM Transactions on Computational Biology and Bioinformatics
(2020).
[229] B. Krawczyk, M. Galar, L . Jelen´, F. Herrera, Evolutionary undersampling
boosting for imbalanced classi(cid:976)ication of breast cancer malignancy, Applied
Soft Computing 38 (2016) 714–726.
[230] T. Cai, H. He, W. Zhang, Breast cancer diagnosis using imbalanced learning
and ensemble method, Applied and Computational Mathematics 7 (3)
(2018) 146–154.
[231] D. Gan, J. Shen, B. An, M. Xu, N. Liu, Integrating tanbn with cost
sensitive classi(cid:976)ication algorithm for imbalanced data in medical diagnosis,
Computers & Industrial Engineering 140 (2020) 106266.
[232] F. Deeba, S. K. Mohammed, F. M. Bui, K. A. Wahid, Learning from imbalanced
data: A comprehensive comparison of classi(cid:976)ier performance for bleeding
detection in endoscopic video, in: 2016 5th International Conference on
Informatics, Electronics and Vision (ICIEV), IEEE, 2016, pp. 1006–1009.
[233] X. Deng, Y. Xu, L. Chen, W. Zhong, A. Jolfaei, X. Zheng, Dynamic clustering
method for imbalanced learning based on adaboost, The Journal of
Supercomputing (2020) 1–23.
[234] H. Zhang, H. Zhang, S. Pirbhulal, W. Wu, V. H. C. D. Albuquerque, Active
balancing mechanism for imbalanced medical data in deep learning–based
classi(cid:976)ication models, ACM Transactions on Multimedia Computing,
Communications, and Applications (TOMM) 16 (1s) (2020) 1–15.
[235] J. Jia, L. Zhai, W. Ren, L. Wang, Y. Ren, An effective imbalanced jpeg
steganalysis scheme based on adaptive cost-sensitive feature learning, IEEE
Transactions on Knowledge and Data Engineering (2020).
51

[236] Y. Huang, Y. Jin, Y. Li, Z. Lin, Towards imbalanced image classi(cid:976)ication:
A generative adversarial network ensemble learning method, IEEE Access 8
(2020) 88399–88409.
[237] M. Hayat, S. Khan, S. W. Zamir, J. Shen, L. Shao, Gaussian af(cid:976)inity for max-
margin class imbalanced learning, in: Proceedings of the IEEE International
Conference on Computer Vision, 2019, pp. 6469–6479.
[238] K. H. Kim, S. Y. Sohn, Hybrid neural network with cost-sensitive support
vector machine for class-imbalanced multimodal data, Neural Networks
(2020).
[239] S. Pouyanfar, S.-C. Chen, Semantic event detection using ensemble deep
learning, in: 2016 IEEE International Symposium on Multimedia (ISM),
IEEE, 2016, pp. 203–208.
[240] G. Lemaˆıtre, F. Nogueira, C. K. Aridas, Imbalanced-learn: A python toolbox
to tackle the curse of imbalanced datasets in machine learning, The Journal
of Machine Learning Research 18 (1) (2017) 559–563.
[241] J. Vanhoeyveld, D. Martens, Imbalanced classi(cid:976)ication in sparse and large
behaviour datasets, Data Mining and Knowledge Discovery 32 (1) (2018)
25–82.
[242] K. Napierala, J. Stefanowski, Types of minority class examples and their
in(cid:976)luence on learning classi(cid:976)iers from imbalanced data, Journal of Intelligent
Information Systems 46 (3) (2016) 563–597.
[243] S. Gupta, A. Jivani, A cluster based under-sampling solution for handling
imbalanced data.
[244] X. Wang, H. Wang, D. Wu, Y. Wang, R. Zhou, A fuzzy consensus
clustering based undersampling approach for class imbalanced learning,
in: Proceedings of the 2019 2nd International Conference on Algorithms,
Computing and Arti(cid:976)icial Intelligence, 2019, pp. 133–137.
52

[245] M. Lango, J. Stefanowski, Multi-class and feature selection extensions of
roughly balanced bagging for imbalanced data, Journal of Intelligent
Information Systems 50 (1) (2018) 97–127.
[246] V. M. S. Esteves, Techniques to deal with imbalanced data in multi-class
problems: A review of existing methods (2020).
[247] J.-J. Zhang, P. Zhong, Learning biased svm with weighted within-class scatter
for imbalanced classi(cid:976)ication, Neural Processing Letters 51 (1) (2020) 797–
817.
[248] C.-M. Vong, J. Du, Accurate and ef(cid:976)icient sequential ensemble learning for
highly imbalanced multi-class data, Neural Networks (2020).
[249] B. Mirza, Z. Lin, Meta-cognitive online sequential extreme learning machine
for imbalanced and concept-drifting data classi(cid:976)ication, Neural Networks 80
(2016) 79–94.
[250] S. Shukla, B. S. Raghuwanshi, Online sequential class-speci(cid:976)ic extreme
learning machine for binary imbalanced learning, Neural Networks 119
(2019) 235–248.
[251] T. Zhu, Y. Lin, Y. Liu, Oversampling for imbalanced time series data, arXiv
preprint arXiv:2004.06373 (2020).
[252] M. Andersson, Multi-class imbalanced learning for time series problem: An
industrial case study (2020).
[253] C. Katrakazas, C. Antoniou, G. Yannis, Time series classi(cid:976)ication using
imbalanced learning for real-time safety assessment, in: Proceedings of the
Transportation Research Board (TRB) 98th Annual Meeting,
Washington, DC, January, 2019, pp. 13–17.
[254] H. M. Nguyen, E. W. Cooper, K. Kamei, Online learning from imbalanced data
streams, in: 2011 International Conference of Soft Computing and Pattern
Recognition (SoCPaR), IEEE, 2011, pp. 347–352.
53

[255] X. Zhang, T. Yang, P. Srinivasan, Online asymmetric active learning with
imbalanced data, Association for Computing Machinery, New York, NY,
USA, 2016. doi:10.1145/2939672.2939854.
URL h(cid:425)ps://doi.org/10.1145/2939672.2939854
[256] Y. Yan, T. Yang, Y. Yang, J. Chen, A framework of online learning with
imbalanced streaming data, in: Proceedings of the AAAI Conference on
Arti(cid:976)icial Intelligence, Vol. 31, 2017.
[257] L. Wang, S. Xu, X. Wang, Q. Zhu, Towards class imbalance in federated
learning, arXiv preprint arXiv:2008.06217 (2020).
[258] M. Duan, D. Liu, X. Chen, R. Liu, Y. Tan, L. Liang, Self-balancing federated
learning with global imbalanced data in mobile systems, IEEE Transactions
on Parallel and Distributed Systems 32 (1) (2021) 59–71.
doi:10.1109/TPDS.2020.3009406.
54