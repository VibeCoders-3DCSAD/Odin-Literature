---
conversion_metadata:
  converted_at: "2026-07-21T10:04:55Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Zhang & Hou.pdf"
  source_pdf_sha256: "7c7ade6031132a07f23c885b56849d134211a94e9c78b6d90d35664932aa1479"
  page_count: 6
  markdown_char_count: 61293
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Available online at www.sciencedirect.com 
Available online at www.sciencedirect.com 
ScienceDirect 
ScienceDirect

Procedia Computer Science 00 (2025) 000–000

Procedia Computer Science 00 (2025) 000–000

Procedia Computer Science 281 (2026) 1463–1468

www.elsevier.com/locate/procedia

www.elsevier.com/locate/procedia

The 6th International Conference on Multi-modal Information Analytics (MMIA) 
The 6th International Conference on Multi-modal Information Analytics (MMIA) 
Consumer Behavior Data Mining and Analysis Using Machine 
Consumer Behavior Data Mining and Analysis Using Machine 
Learning Algorithms 
Learning Algorithms 
Hanwen Zhanga* , Yueyue Houb 
Hanwen Zhanga* , Yueyue Houb 
 aCollege of Business, Cheongju University, Cheongju, Republic of Korea 
bGuangzhou Software Institute, Guangzhou, China 
 aCollege of Business, Cheongju University, Cheongju, Republic of Korea 
bGuangzhou Software Institute, Guangzhou, China

Abstract 
Abstract 
In the era of digital economy, the vast amount of consumer online behavior data provides unprecedented possibilities for accurate 
insight  into  market  demand  and  prediction  of  individual  behavior.  This  study  aims  to  systematically  explore  and  compare  the 
In the era of digital economy, the vast amount of consumer online behavior data provides unprecedented possibilities for accurate 
effectiveness of different machine learning algorithms in consumer behavior data mining and analysis. Focusing on the core task 
insight  into  market  demand  and  prediction  of  individual  behavior.  This  study  aims  to  systematically  explore  and  compare  the 
of "prediction of customers' future purchase intention", the research selects four typical algorithms, including logical regression, 
effectiveness of different machine learning algorithms in consumer behavior data mining and analysis. Focusing on the core task 
support vector machine, random forest and XGboost, and constructs a complete analysis process from data preprocessing, feature 
of "prediction of customers' future purchase intention", the research selects four typical algorithms, including logical regression, 
engineering to  model training  evaluation  on  a  real  e-commerce  data  set.  This  paper  systematically  reviews  the  evolution  from 
support vector machine, random forest and XGboost, and constructs a complete analysis process from data preprocessing, feature 
classical  behavior  theory  to  modern  data  mining  technology.  In  terms  of  methodology,  this  paper  describes  the  key  steps  of 
engineering to  model training  evaluation  on  a  real  e-commerce  data  set.  This  paper  systematically  reviews  the  evolution  from 
experimental conditions, data cleaning, feature construction (including RFM and extended features) and model implementation in 
classical  behavior  theory  to  modern  data  mining  technology.  In  terms  of  methodology,  this  paper  describes  the  key  steps  of 
detail. The experimental results are presented clearly through the comprehensive performance table, efficiency comparison table 
experimental conditions, data cleaning, feature construction (including RFM and extended features) and model implementation in 
and feature importance table. The analysis shows that XGboost algorithm performs best in accuracy, F1 score, AUC and other 
detail. The experimental results are presented clearly through the comprehensive performance table, efficiency comparison table 
key  indicators,  showing  a  strong  ability  to  deal  with  complex  nonlinear  relationships;  The  Stochastic  Forest  achieves  a  good 
and feature importance table. The analysis shows that XGboost algorithm performs best in accuracy, F1 score, AUC and other 
balance in stability and efficiency; However, logistic regression maintains the best explicability. This study not only verifies the 
key  indicators,  showing  a  strong  ability  to  deal  with  complex  nonlinear  relationships;  The  Stochastic  Forest  achieves  a  good 
superiority of ensemble learning in consumer behavior prediction, but also provides empirical basis and selection guidance for 
balance in stability and efficiency; However, logistic regression maintains the best explicability. This study not only verifies the 
enterprises in the trade-off between accuracy, efficiency and interpretability. 
superiority of ensemble learning in consumer behavior prediction, but also provides empirical basis and selection guidance for 
© 2026 The Authors. Published by ELSEVIER B.V. 
enterprises in the trade-off between accuracy, efficiency and interpretability. 
© 2026 The Authors. Published by Elsevier B.V.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) 
© 2026 The Authors. Published by ELSEVIER B.V. 
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee  
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) 
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee
Keywords: Machine learning, Consumer behavior analysis, Data mining, Predictive model, XGBoost, RFM model; 
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee  
Keywords: Machine learning, Consumer behavior analysis, Data mining, Predictive model, XGBoost, RFM model;

* Corresponding author. Tel.: +0-000-000-0000 ; fax: +0-000-000-0000 .

E-mail address: zhw0314@gmail.com

* Corresponding author. Tel.: +0-000-000-0000 ; fax: +0-000-000-0000 .

E-mail address: zhw0314@gmail.com

1877-0509 © 2026 The Authors. Published by ELSEVIER B.V. 
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) 
1877-0509 © 2026 The Authors. Published by ELSEVIER B.V. 
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee 
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) 
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee

1877-0509 © 2026 The Authors. Published by Elsevier B.V.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee

10.1016/j.procs.2026.05.035

1877-0509

---

<!-- PAGE 2 -->

1464 
2

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468
Author name / Procedia Computer Science 00 (2025) 000–000

1. Introduction

With  the  rapid  development  of  e-commerce,  mobile  Internet  and  Internet  of  things  technology,  a  series  of 
consumer behaviors such as browsing, searching, clicking, buying and evaluating have been completely recorded on 
the digital platform, forming a huge, diverse and real-time big data resource. This marks a profound transformation 
of  the  research  paradigm  of  consumer  behavior  from  causal  inference  based  on  sampling  survey  to  correlation 
mining and predictive analysis based on full data [1].

However,  in  the  face  of  such  complex  data  forms,  the  traditional  statistical  analysis  tools  (such  as  linear 
regression and analysis of variance) have become inadequate. As the core branch of artificial intelligence, machine 
learning automatically learns patterns and rules from data through algorithms, and shows significant advantages in 
dealing with high-dimensional, nonlinear and complex big data. In recent years, machine learning has been widely 
used in many business scenarios, such as customer churn prediction, marketing response modeling, credit scoring 
and  so  on,  from  classic  logical  regression  and  support  vector  machines  to  modern  integrated  learning  algorithms 
(such  as  random  forest  and  gradient  lifting  tree)  [2].  In  view  of  this,  this  study  aims  to  empirically  compare  and 
deeply  analyze  four  mainstream  machine  learning  algorithms  through  a  rigorous  and  reproducible  data  science 
process. We not only pay attention to the prediction accuracy of the model, but also incorporate engineering practice 
indicators such as training efficiency and feature importance into the comprehensive evaluation system, in order to 
provide researchers and practitioners in related fields with a clear and comprehensive algorithm performance map 
and selection decision reference.

2. Related Works

Data driven research on consumer behavior is a cross field integrating marketing, computer science and statistics.

Its development closely follows the evolution of theoretical basis, data form and analysis technology.

In  terms  of  analysis  methods,  early  data  mining  technologies  focused  on  discovering  patterns  from  structured 
transaction data. The Apriori algorithm proposed by Lin J[3] and others is a milestone in association rule mining. It 
makes it possible to automatically discover the symbiotic relationship between "beer and diapers" from large-scale 
transaction  data,  and  is  widely  used  in  shopping  basket  analysis  and  cross  selling.  The  FP  growth  algorithm 
proposed by Ebrahimi P[4] and others has greatly improved the efficiency of association rule mining through novel 
data structure. For sequential patterns, the sequential pattern mining algorithm proposed by Mohan L[5] can analyze 
the purchase order of customers across time periods and provide a tool for predicting the next possible purchase. In 
the  field  of  customer  segmentation,  the  K-means  clustering  algorithm  and  its  subsequent  variants  proposed  by 
Chaubey G[6] and others have become one of the most commonly used unsupervised learning methods for market 
clustering based on customer attributes or behavior characteristics. These traditional methods are good at descriptive 
analysis and pattern discovery, but their ability is often limited in complex predictive modeling.

The rise of machine learning has brought a paradigm level breakthrough for consumer behavior analysis. In the 
field of supervised learning, classification and regression prediction have become the core applications. The support 
vector  machine  proposed  by  Li  H[7]  has  been  widely  used  in  customer  classification  and  text  sentiment  analysis 
because  of  its  solid  foundation  based  on  statistical  learning  theory  and  the  ability  to  handle  nonlinear  problems 
through  kernel  functions.  The  random  forest  algorithm  proposed  by  Bhoyar  S[8]  and  others  has  significantly 
improved  the  accuracy  and  robustness  of  the  model  by  integrating  multiple  decision  trees  and  introducing 
randomness.  It  is  widely  used  in  customer  churn  prediction  and  credit  risk  assessment.  The  concept  of  gradient 
elevator proposed by Abdul Aziz M[9] and Zvarikova K[10] and others, as well as the efficient implementation of 
XGboost, have achieved the performance of state of the art in many data science competitions and industrial scenes 
by  iteratively  optimizing  the  loss  function  and  integrating  weak  learners,  and  become  one  of  the  preferred 
algorithms for processing table data.

In  recent  years,  with  the  increase  of  data  complexity,  more  advanced  models  have  been  introduced.  For  the 
temporal dependence of behavior sequence, the long-term and short-term memory network and its variants proposed 
by  Ghorbantanhaei  H[11]  and  others  can  effectively  capture  long-term  dependence  and  be  applied  to  the  next 
recommendation  and  loss  warning.  Xu  Z[12]  and  others  successfully  applied  deep  reinforcement  learning  in  the 
field  of  go,  which  also  inspired  their  application  and  exploration  in  sequential  decision-making  problems  such  as 
personalized marketing and dynamic pricing.

To  sum  up,  the  existing  research  has  fully  proved  the  great  value  of  machine  learning  in  consumer  behavior

---

<!-- PAGE 3 -->

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468 
Author name / Procedia Computer Science 00 (2025) 000–000

1465
 3

analysis, and has developed from linear model and kernel method to today's deep learning and integrated learning. 
This  study  aims  to  fill  this  gap,  through  rigorous  controlled  experiments,  quantitative  evaluation  of  logistic 
regression  SVM.  The  comprehensive  performance  of  random  forest  and  XGboost  under  the  same  data  and 
evaluation system, and the root causes of their performance differences are discussed in depth.

3. Method

3.1. Data sources and experimental conditions

This  study  used  the publicly available  "Online  Retail"  dataset  from  the  UCI  machine  learning repository.  This 
dataset  records  all  cross-border  transactions  of  an  online  retail  company  from  December  1,  2020  to  December  9, 
2021, including fields such as InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, Customer ID, 
and Country.

The hardware environment for the experiment is an Intel Core i7-12700H processor with 16GB DDR4 memory. 
The  software  environment  is  Python  3.9,  with  main  libraries  including  Pandas  1.4.2,  NumPy  1.22.3,  Scikit  learn 
1.0.2, XGBoost 1.5.0, and visualization using Matplotlib and Seaborn.

3.2. Data Preprocessing and Feature Engineering

3.2.1 Data Preprocessing

Firstly,  perform  data  cleaning:  delete  duplicate  records;  Exclude  records  with  empty  Customer  ID  (unable  to 
associate  with  specific  individuals);  Delete  records  that  are  clearly  unrelated  to  purchase  predictions  or  represent 
abnormal behavior, such as return records with invoice numbers starting with 'C' and entries with negative Quantity. 
This study focuses on predicting positive purchasing behavior.

Secondly, defining prediction tasks and constructing labels: The core of this study is a binary prediction problem, 
which predicts whether a customer will make another purchase within a fixed time window in the future (such as the 
following month). We will set November 1, 2021 to December 9, 2021 as the forecast period, and mark customers 
who have made at least one purchase during this period as positive samples (y=1), otherwise as negative samples 
(y=0). All historical data prior to the forecast period (December 1, 2020 to October 31, 2021) were used to construct 
features for each customer.

Finally, perform dataset partitioning: randomly divide the dataset into a training set and an independent testing 
set in a 7:3 ratio based on the Customer ID. This partitioning ensures that all data from the same client will only 
appear  in  one  of  the  training  or  testing  sets,  effectively  avoiding  the  problem  of  model  evaluation  results  being 
inflated due to data leakage. 
3.2.2 Feature Engineering

Based on the customer's historical transaction records, four categories of 28 numerical features were constructed

for each customer:

RFM core features: Recency, frequency, and monetary amount of the most recent purchase. 
Behavioral  breadth  and  depth  characteristics:  the  number  of  unique  products  purchased,  the  number  of  unique

product categories visited, and the average number of products purchased per invoice.

Consumption pattern characteristics: average order value, standard deviation of order value, average unit price of

goods, standard deviation of unit price, and proportion of discounted goods purchased.

Time  pattern  characteristics:  average  purchase  interval  days,  standard  deviation  of  purchase  interval  days, 
proportion of purchases made on weekends, distribution of purchases during different time periods such as morning, 
afternoon, and evening on weekdays.

3.3. Model selection and implementation

Four representative machine learning algorithms were selected for comparative research, and their core formulas

were briefly explained:

Logistic  regression:  serves  as  a  benchmark  for  linear  models.  It  maps  the  linear  combination  of  features  to 
probability through the Sigmoid function, as follows. This model is known for its good interpretability (coefficient

---

<!-- PAGE 4 -->

1466 
4

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468
Author name / Procedia Computer Science 00 (2025) 000–000

size and direction representing feature influence) and efficiency.

(1)

Among them, x is the feature vector, w and b are the model weights and biases. 
Support Vector Machine: A powerful classifier based on statistical learning theory. The core idea is to find an 
optimal  hyperplane  to  maximize  the  classification  interval  between  samples  of  different categories.  For  nonlinear 
problems, linear separability is achieved by mapping the samples to a high-dimensional space using kernel functions 
(in this study, radial basis kernels are used). The decision function is:

P(y = 1 ∣ x) =

1+e−(w

x+b)

T

1

n

(2)

Among them, α i is the Lagrange multiplier, and K (
f(x) = sign(∑ αiyiK(xi, x) + b)
i=1
Random  Forest:  A  Representative  of  Bagging  Ensemble  Learning.  By  constructing  a  large  number  of  decision 
xi, x
trees and synthesizing their voting results for prediction. When a single decision tree is growing, the Gini coefficient 
is often used to select the optimal splitting feature to minimize the "impurity" of nodes.

) is the kernel function.

Gini(D)=1−k=1K(pk)2                                                                      (3) 
Among them, D is the current node sample set, K is the number of categories, and pk is the proportion of samples 
belonging  to  the  k-th  category.  Random  forest  effectively  reduces  model  variance  and  prevents  overfitting  by 
introducing dual randomness of samples and features.

XGBoost:  An  advanced  representative  of  Boosting  ensemble  learning.  It  fits  the  data  using  an  additive  model 
(weighted sum of multiple decision trees) and iteratively adds new trees to fit the residuals from the previous round 
of predictions. The objective function includes a loss function and a regularization term to control model complexity 
and prevent overfitting.

(4) 
Among them, l is the loss function (such as logarithmic loss), Ω (ft) is the regularization term used to control the 
(t−1)
complexity  of  the  t-th  tree  f.  XGBoost  optimizes  the  objective  through  second-order  Taylor  expansion 
approximation, demonstrating excellent performance in both accuracy and efficiency.

n
= ∑ l(yi, y�i
i=1

(xi)) + Ω(ft)

+ f

(t)

L

t

All features were standardized before training. Use grid search combined with 5-fold cross validation to optimize 
key  hyperparameters  for  each  model  on  the  training  set,  such  as  the  regularization  coefficient  C  of  logistic 
regression and SVM, the number and maximum depth of trees in random forests, the learning rate and maximum 
depth of trees in XGBoost, etc. The final evaluation of model performance is conducted on an independent test set 
that has never been involved in training and tuning.

4. Result and Discussion

4.1. Result

After completing data preprocessing, feature engineering, and model tuning, the performance of each model was 
evaluated on a unified test set. The evaluation used five indicators, namely accuracy, precision, recall, F1 score, and 
AUC (area under the ROC curve), to comprehensively reflect the classification ability of the model. The results are 
shown in Table 1.

Table 1 Comprehensive Comparison of Prediction Performance of Different Machine Learning Models

Model

Accuracy

Precision

Recall

F1 score

AUC

Logistic regression

SVM

SF

XGBoost

0.834

0.848

0.862

0.876

0.701

0.732

0.758

0.781

0.468

0.512

0.570

0.602

0.562

0.602

0.651

0.680

0.792

0.821

0.853

0.872

Table 1 shows the five core performance indicators of four models on the test set. Accuracy measures the proportion 
of  correct  overall  classification;  Accuracy  measures  the  proportion  of  customers  predicted  by  the  model  to  actually 
make  a  purchase;  Recall  rate  measures  the  proportion  of  customers  who  will  actually  make  a  purchase  that  is 
successfully  predicted  by  the  model;  The  F1  score  is  the  harmonic  mean  of  precision  and  recall,  used  for 
comprehensive evaluation; The AUC measurement model has the overall ability to rank positive samples higher than

---

<!-- PAGE 5 -->

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468 
Author name / Procedia Computer Science 00 (2025) 000–000

1467
 5

negative samples, and the closer it is to 1, the better. As can be seen from the table, XGBoost leads in all indicators.

In  addition  to  prediction  accuracy,  the  computational  efficiency  of  the  model  is  an  important  consideration  in 
practical applications. Table 2 records the time it takes for each model to complete training and test set prediction in the 
same hardware environment.

Model

Logistic regression

SVM

SF

XGBoost

Table 2 Comparison of Model Training and Prediction Efficiency (Unit: Second)

Training time

Prediction time (test set)

0.8

125.3

15.2

9.5

0.02

18.7

0.35

0.08

Table 2 illustrates: This table compares the operational efficiency of four models. Training time refers to the total 
time required to complete model training (including cross validation tuning) on the training set; Prediction time refers 
to the time it takes to make forward predictions on the test set. Logistic regression has the fastest speed, SVM is the 
slowest, and Random Forest and XGBoost are in between. Among them, XGBoost achieves the best accuracy while 
maintaining high training and prediction efficiency.

To understand the decision-making basis of the model, we analyzed the feature importance ranking of each model. 
Table  3  shows  the  three  most  important  features  identified  by  logistic  regression  (based  on  normalized  coefficient 
absolute values), random forest, and XGBoost.

Table 3 Model Feature Importance Ranking (Top 3)

Ranking

Logistic regression (coefficient absolute value)

SF

XGBoost

1

2

3

Recent purchase time (Recency)

Total consumption amount (Monetary)

Total frequency of purchases

purchase

Latest 
time(Recency) 
Total frequency of purchases

purchase

Latest 
time(Recency) 
Total frequency of purchases

Total  consumption  amount 
(Monetary)

Average order value

Table 3 shows the three most important features that different models consider for prediction. Logistic regression 
determines  importance  by  the  size  and  direction  of  feature  weights,  while  Random  Forest  and  XGBoost  determine 
importance  by  calculating  the  reduction  in  impurity  (or  information  gain)  caused  by  features  when  splitting  nodes. 
Although the model principles are different, "recent purchase time" is unanimously considered as the primary predictor, 
verifying the core position of R (proximity) in the RFM framework. XGBoost recognizes the importance of the derived 
feature of "average order value", reflecting its ability to capture more complex patterns.

4.2. Discussion

The  recall  rate  of  logistic  regression  is  the  lowest  (0.468),  indicating  that  its  prediction  strategy  is  relatively 
conservative  and  tends  to  misjudge  more  potential  customers  as  not  purchasing.  This  may  be  due  to  its  strong 
assumption of linearly separable data not being valid on complex behavioral data. SVM uses kernel function mapping 
to  find  nonlinear  interfaces  in  high-dimensional  space,  which  performs  better  than  logistic  regression.  However,  its 
performance  is  highly  dependent  on  the  selection  of  kernel  function  and  penalty  parameter  C,  resulting  in  high 
optimization costs.  Random forest constructs a large number of decision trees with high diversity through Bootstrap 
aggregation  and  random  feature  subset  strategy,  and  smooths  the  prediction  variance  of  individual  trees  through  the 
"voting" mechanism,  thus achieving stable and excellent performance. XGBoost uses a  Boosting mechanism, where 
subsequent  trees  focus  on  learning  difficult  samples  that  were  misjudged  earlier,  and  combine  the  predictions  of  all 
trees  in  the  form  of  additive  models.  At  the  same  time,  the  regularization  term  in  its  objective  function  effectively 
controls complexity, ultimately achieving the best prediction accuracy.

Logistic regression has the fastest training and prediction speed, and is suitable for online reasoning scenarios that 
require extremely high real-time performance or extremely limited resources. The training time of SVM far exceeds

---

<!-- PAGE 6 -->

1468 
6

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468
Author name / Procedia Computer Science 00 (2025) 000–000

other  models,  and  its  time  complexity  becomes  the  main  bottleneck  in  large-scale  data,  with  poor  scalability.  The 
training of random forests can be highly parallelized and the time is acceptable. XGBoost achieves top-level prediction 
accuracy  while  optimizing  its  weighted  quantile  sketch,  histogram  algorithm,  and  other  features,  resulting  in 
significantly higher training efficiency than random forests. It demonstrates an excellent balance between accuracy and 
efficiency, making it highly suitable for large-scale industrial applications.

In terms of model interpretability, the coefficients of logistic regression have the most direct interpretability, and the 
size  and  direction  of  feature  weights  clearly  indicate  their  marginal  impact  on  purchase  probability.  The  tree  model 
provides  global  interpretation  through  feature  importance.  A  highly  insightful  finding  is  that  regardless  of  model 
complexity,  'recent  purchase  time'  remains  the  most  important  predictive  feature  among  all  models,  which  strongly 
validates  the  classic  business  rule  (R  in  RFM  models)  that  'customer  recent  activity  is  the  best  predictor  of  future 
behavior' in a data-driven manner. The three core indicators (R, F, M) in the RFM framework consistently rank high in 
importance  ranking,  which  deeply  indicates  that  domain  knowledge  based  careful  feature  engineering  is  the 
cornerstone of improving the performance of any machine learning model. XGBoost further explores the importance of 
the derived feature of "average order value", reflecting its ability to capture more subtle consumption patterns.

5. Conclusion

This  study  systematically  compared  the  performance  of  four  machine  learning  algorithms,  namely  logistic 
regression,  support  vector  machine,  random  forest,  and  XGBoost,  in  predicting  consumer  purchasing  behavior.  The 
experimental  results  show  that  under  the  same  feature  engineering  and  evaluation  framework,  XGBoost  algorithm 
achieves  the  best  balance  between  prediction  accuracy  (F1  score  0.680,  AUC  0.872)  and  training  efficiency, 
significantly better than other comparative models, demonstrating the powerful ability of gradient boosting ensemble 
algorithm in processing complex and non-linear consumer behavior data. Random forests  exhibit excellent accuracy 
and  robustness,  while  logistic  regression  holds  irreplaceable  value  in  specific  scenarios  due  to  its  outstanding 
interpretability  and  computational  efficiency.  The  analysis  of  feature  importance  consistently  confirms  the  core 
predictive power of RFM features such as "recent purchase time", highlighting the importance of combining domain 
knowledge with data-driven modeling.

Reference

[1] Li L. Analysis of e-commerce customers' shopping behavior based on data mining and machine learning[J]. Soft Computing, 2023: 1-10.

[2] Akram N, Aravindhan K, Sujatha K, et al. Consumer behavior prediction using machine learning algorithms[M]//Exploring psychology, social

innovation and advanced applications of machine learning. IGI Global Scientific Publishing, 2025: 109-130.

[3] Lin J. Application of machine learning in predicting consumer behavior and precision marketing[J]. PLoS One, 2025, 20(5): e0321854.

[4]  Ebrahimi  P,  Basirat  M,  Yousefi  A,  et  al.  Social  networks  marketing  and  consumer  purchase  behavior:  The  combination  of  SEM  and

unsupervised machine learning approaches[J]. Big Data and Cognitive Computing, 2022, 6(2): 35.

[5]  Mohan  L,  Devarajan  M,  Alotoum  F  J,  et  al.  Advanced  Data  Analytics  for  Predicting  Consumer  Behavior  Using  Machine  Learning  and 
Association Rule Mining[C]//2025 International Conference on Technology Enabled Economic Changes (InTech). IEEE, 2025: 908-914.

[6]  Chaubey  G,  Gavhane  P  R,  Bisen  D,  et  al.  Customer  purchasing  behavior  prediction  using  machine  learning  classification  techniques[J].

Journal of Ambient Intelligence and Humanized Computing, 2023, 14(12): 16133-16157.

[7] Li H. Social Media Data Mining and Online Consumer Behavior Analysis[J]. Procedia Computer Science, 2025, 261: 406-413.

[8] Bhoyar S, Bhoyar P, Shah M A. A machine learning-based predictive approach in evaluating consumer behavior[J]. Journal of Statistics and

Management Systems, 2023, 26(8): 1955-1963.

[9]  Abdul  Aziz  M,  Mustakim  N  A,  Abdul  Rahman  S.  Decision  tree  and  rule-based  classification  for  predicting  online  purchase  behavior  in

Malaysia[J]. Malaysian Journal of Computing (MJoC), 2024, 9(2): 1905-1915.

[10]  Zvarikova  K,  Machova  V,  Nica  E.  Cognitive  artificial  intelligence  algorithms,  movement  and  behavior  tracking  tools,  and  customer

identification technology in the metaverse commerce[J]. Review of Contemporary Philosophy, 2022, 21: 171-187.

[11] GhorbanTanhaei H, Boozary P, Sheykhan S, et al. Predictive analytics in customer behavior: Anticipating trends and preferences[J]. Results

in Control and Optimization, 2024, 17: 100462.

[12]  Xu  Z,  Zhu  G,  Metawa  N,  et  al.  Machine  learning  based  customer  meta-combination  brand  equity  analysis  for  marketing  behavior

evaluation[J]. Information Processing & Management, 2022, 59(1): 102800.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Available online at www.sciencedirect.com
Available online at www.sciencedirect.com
ScienceDirect
ScienceDirect

Procedia Computer Science 00 (2025) 000–000

Procedia Computer Science 00 (2025) 000–000

Procedia Computer Science 281 (2026) 1463–1468

www.elsevier.com/locate/procedia

www.elsevier.com/locate/procedia

The 6th International Conference on Multi-modal Information Analytics (MMIA)
The 6th International Conference on Multi-modal Information Analytics (MMIA)
Consumer Behavior Data Mining and Analysis Using Machine
Consumer Behavior Data Mining and Analysis Using Machine
Learning Algorithms
Learning Algorithms
Hanwen Zhanga* , Yueyue Houb
Hanwen Zhanga* , Yueyue Houb
 aCollege of Business, Cheongju University, Cheongju, Republic of Korea
bGuangzhou Software Institute, Guangzhou, China
 aCollege of Business, Cheongju University, Cheongju, Republic of Korea
bGuangzhou Software Institute, Guangzhou, China

Abstract
Abstract
In the era of digital economy, the vast amount of consumer online behavior data provides unprecedented possibilities for accurate
insight  into  market  demand  and  prediction  of  individual  behavior.  This  study  aims  to  systematically  explore  and  compare  the
In the era of digital economy, the vast amount of consumer online behavior data provides unprecedented possibilities for accurate
effectiveness of different machine learning algorithms in consumer behavior data mining and analysis. Focusing on the core task
insight  into  market  demand  and  prediction  of  individual  behavior.  This  study  aims  to  systematically  explore  and  compare  the
of "prediction of customers' future purchase intention", the research selects four typical algorithms, including logical regression,
effectiveness of different machine learning algorithms in consumer behavior data mining and analysis. Focusing on the core task
support vector machine, random forest and XGboost, and constructs a complete analysis process from data preprocessing, feature
of "prediction of customers' future purchase intention", the research selects four typical algorithms, including logical regression,
engineering to  model training  evaluation  on  a  real  e-commerce  data  set.  This  paper  systematically  reviews  the  evolution  from
support vector machine, random forest and XGboost, and constructs a complete analysis process from data preprocessing, feature
classical  behavior  theory  to  modern  data  mining  technology.  In  terms  of  methodology,  this  paper  describes  the  key  steps  of
engineering to  model training  evaluation  on  a  real  e-commerce  data  set.  This  paper  systematically  reviews  the  evolution  from
experimental conditions, data cleaning, feature construction (including RFM and extended features) and model implementation in
classical  behavior  theory  to  modern  data  mining  technology.  In  terms  of  methodology,  this  paper  describes  the  key  steps  of
detail. The experimental results are presented clearly through the comprehensive performance table, efficiency comparison table
experimental conditions, data cleaning, feature construction (including RFM and extended features) and model implementation in
and feature importance table. The analysis shows that XGboost algorithm performs best in accuracy, F1 score, AUC and other
detail. The experimental results are presented clearly through the comprehensive performance table, efficiency comparison table
key  indicators,  showing  a  strong  ability  to  deal  with  complex  nonlinear  relationships;  The  Stochastic  Forest  achieves  a  good
and feature importance table. The analysis shows that XGboost algorithm performs best in accuracy, F1 score, AUC and other
balance in stability and efficiency; However, logistic regression maintains the best explicability. This study not only verifies the
key  indicators,  showing  a  strong  ability  to  deal  with  complex  nonlinear  relationships;  The  Stochastic  Forest  achieves  a  good
superiority of ensemble learning in consumer behavior prediction, but also provides empirical basis and selection guidance for
balance in stability and efficiency; However, logistic regression maintains the best explicability. This study not only verifies the
enterprises in the trade-off between accuracy, efficiency and interpretability.
superiority of ensemble learning in consumer behavior prediction, but also provides empirical basis and selection guidance for
© 2026 The Authors. Published by ELSEVIER B.V.
enterprises in the trade-off between accuracy, efficiency and interpretability.
© 2026 The Authors. Published by Elsevier B.V.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
© 2026 The Authors. Published by ELSEVIER B.V.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee
Keywords: Machine learning, Consumer behavior analysis, Data mining, Predictive model, XGBoost, RFM model;
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee
Keywords: Machine learning, Consumer behavior analysis, Data mining, Predictive model, XGBoost, RFM model;

* Corresponding author. Tel.: +0-000-000-0000 ; fax: +0-000-000-0000 .

E-mail address: zhw0314@gmail.com

* Corresponding author. Tel.: +0-000-000-0000 ; fax: +0-000-000-0000 .

E-mail address: zhw0314@gmail.com

1877-0509 © 2026 The Authors. Published by ELSEVIER B.V.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
1877-0509 © 2026 The Authors. Published by ELSEVIER B.V.
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee

1877-0509 © 2026 The Authors. Published by Elsevier B.V.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
Peer-review under responsibility of the scientific committee of MMIA conference Program Committee

10.1016/j.procs.2026.05.035

1877-0509

ScienceDirectAvailable online at www.sciencedirect.com

1464
2

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468
Author name / Procedia Computer Science 00 (2025) 000–000

1. Introduction

With  the  rapid  development  of  e-commerce,  mobile  Internet  and  Internet  of  things  technology,  a  series  of
consumer behaviors such as browsing, searching, clicking, buying and evaluating have been completely recorded on
the digital platform, forming a huge, diverse and real-time big data resource. This marks a profound transformation
of  the  research  paradigm  of  consumer  behavior  from  causal  inference  based  on  sampling  survey  to  correlation
mining and predictive analysis based on full data [1].

However,  in  the  face  of  such  complex  data  forms,  the  traditional  statistical  analysis  tools  (such  as  linear
regression and analysis of variance) have become inadequate. As the core branch of artificial intelligence, machine
learning automatically learns patterns and rules from data through algorithms, and shows significant advantages in
dealing with high-dimensional, nonlinear and complex big data. In recent years, machine learning has been widely
used in many business scenarios, such as customer churn prediction, marketing response modeling, credit scoring
and  so  on,  from  classic  logical  regression  and  support  vector  machines  to  modern  integrated  learning  algorithms
(such  as  random  forest  and  gradient  lifting  tree)  [2].  In  view  of  this,  this  study  aims  to  empirically  compare  and
deeply  analyze  four  mainstream  machine  learning  algorithms  through  a  rigorous  and  reproducible  data  science
process. We not only pay attention to the prediction accuracy of the model, but also incorporate engineering practice
indicators such as training efficiency and feature importance into the comprehensive evaluation system, in order to
provide researchers and practitioners in related fields with a clear and comprehensive algorithm performance map
and selection decision reference.

2. Related Works

Data driven research on consumer behavior is a cross field integrating marketing, computer science and statistics.

Its development closely follows the evolution of theoretical basis, data form and analysis technology.

In  terms  of  analysis  methods,  early  data  mining  technologies  focused  on  discovering  patterns  from  structured
transaction data. The Apriori algorithm proposed by Lin J[3] and others is a milestone in association rule mining. It
makes it possible to automatically discover the symbiotic relationship between "beer and diapers" from large-scale
transaction  data,  and  is  widely  used  in  shopping  basket  analysis  and  cross  selling.  The  FP  growth  algorithm
proposed by Ebrahimi P[4] and others has greatly improved the efficiency of association rule mining through novel
data structure. For sequential patterns, the sequential pattern mining algorithm proposed by Mohan L[5] can analyze
the purchase order of customers across time periods and provide a tool for predicting the next possible purchase. In
the  field  of  customer  segmentation,  the  K-means  clustering  algorithm  and  its  subsequent  variants  proposed  by
Chaubey G[6] and others have become one of the most commonly used unsupervised learning methods for market
clustering based on customer attributes or behavior characteristics. These traditional methods are good at descriptive
analysis and pattern discovery, but their ability is often limited in complex predictive modeling.

The rise of machine learning has brought a paradigm level breakthrough for consumer behavior analysis. In the
field of supervised learning, classification and regression prediction have become the core applications. The support
vector  machine  proposed  by  Li  H[7]  has  been  widely  used  in  customer  classification  and  text  sentiment  analysis
because  of  its  solid  foundation  based  on  statistical  learning  theory  and  the  ability  to  handle  nonlinear  problems
through  kernel  functions.  The  random  forest  algorithm  proposed  by  Bhoyar  S[8]  and  others  has  significantly
improved  the  accuracy  and  robustness  of  the  model  by  integrating  multiple  decision  trees  and  introducing
randomness.  It  is  widely  used  in  customer  churn  prediction  and  credit  risk  assessment.  The  concept  of  gradient
elevator proposed by Abdul Aziz M[9] and Zvarikova K[10] and others, as well as the efficient implementation of
XGboost, have achieved the performance of state of the art in many data science competitions and industrial scenes
by  iteratively  optimizing  the  loss  function  and  integrating  weak  learners,  and  become  one  of  the  preferred
algorithms for processing table data.

In  recent  years,  with  the  increase  of  data  complexity,  more  advanced  models  have  been  introduced.  For  the
temporal dependence of behavior sequence, the long-term and short-term memory network and its variants proposed
by  Ghorbantanhaei  H[11]  and  others  can  effectively  capture  long-term  dependence  and  be  applied  to  the  next
recommendation  and  loss  warning.  Xu  Z[12]  and  others  successfully  applied  deep  reinforcement  learning  in  the
field  of  go,  which  also  inspired  their  application  and  exploration  in  sequential  decision-making  problems  such  as
personalized marketing and dynamic pricing.

To  sum  up,  the  existing  research  has  fully  proved  the  great  value  of  machine  learning  in  consumer  behavior

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468
Author name / Procedia Computer Science 00 (2025) 000–000

1465
 3

analysis, and has developed from linear model and kernel method to today's deep learning and integrated learning.
This  study  aims  to  fill  this  gap,  through  rigorous  controlled  experiments,  quantitative  evaluation  of  logistic
regression  SVM.  The  comprehensive  performance  of  random  forest  and  XGboost  under  the  same  data  and
evaluation system, and the root causes of their performance differences are discussed in depth.

3. Method

3.1. Data sources and experimental conditions

This  study  used  the publicly available  "Online  Retail"  dataset  from  the  UCI  machine  learning repository.  This
dataset  records  all  cross-border  transactions  of  an  online  retail  company  from  December  1,  2020  to  December  9,
2021, including fields such as InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, Customer ID,
and Country.

The hardware environment for the experiment is an Intel Core i7-12700H processor with 16GB DDR4 memory.
The  software  environment  is  Python  3.9,  with  main  libraries  including  Pandas  1.4.2,  NumPy  1.22.3,  Scikit  learn
1.0.2, XGBoost 1.5.0, and visualization using Matplotlib and Seaborn.

3.2. Data Preprocessing and Feature Engineering

3.2.1 Data Preprocessing

Firstly,  perform  data  cleaning:  delete  duplicate  records;  Exclude  records  with  empty  Customer  ID  (unable  to
associate  with  specific  individuals);  Delete  records  that  are  clearly  unrelated  to  purchase  predictions  or  represent
abnormal behavior, such as return records with invoice numbers starting with 'C' and entries with negative Quantity.
This study focuses on predicting positive purchasing behavior.

Secondly, defining prediction tasks and constructing labels: The core of this study is a binary prediction problem,
which predicts whether a customer will make another purchase within a fixed time window in the future (such as the
following month). We will set November 1, 2021 to December 9, 2021 as the forecast period, and mark customers
who have made at least one purchase during this period as positive samples (y=1), otherwise as negative samples
(y=0). All historical data prior to the forecast period (December 1, 2020 to October 31, 2021) were used to construct
features for each customer.

Finally, perform dataset partitioning: randomly divide the dataset into a training set and an independent testing
set in a 7:3 ratio based on the Customer ID. This partitioning ensures that all data from the same client will only
appear  in  one  of  the  training  or  testing  sets,  effectively  avoiding  the  problem  of  model  evaluation  results  being
inflated due to data leakage.
3.2.2 Feature Engineering

Based on the customer's historical transaction records, four categories of 28 numerical features were constructed

for each customer:

RFM core features: Recency, frequency, and monetary amount of the most recent purchase.
Behavioral  breadth  and  depth  characteristics:  the  number  of  unique  products  purchased,  the  number  of  unique

product categories visited, and the average number of products purchased per invoice.

Consumption pattern characteristics: average order value, standard deviation of order value, average unit price of

goods, standard deviation of unit price, and proportion of discounted goods purchased.

Time  pattern  characteristics:  average  purchase  interval  days,  standard  deviation  of  purchase  interval  days,
proportion of purchases made on weekends, distribution of purchases during different time periods such as morning,
afternoon, and evening on weekdays.

3.3. Model selection and implementation

Four representative machine learning algorithms were selected for comparative research, and their core formulas

were briefly explained:

Logistic  regression:  serves  as  a  benchmark  for  linear  models.  It  maps  the  linear  combination  of  features  to
probability through the Sigmoid function, as follows. This model is known for its good interpretability (coefficient

1466
4

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468
Author name / Procedia Computer Science 00 (2025) 000–000

size and direction representing feature influence) and efficiency.

                                                                  (1)

Among them, x is the feature vector, w and b are the model weights and biases.
Support Vector Machine: A powerful classifier based on statistical learning theory. The core idea is to find an
optimal  hyperplane  to  maximize  the  classification  interval  between  samples  of  different categories.  For  nonlinear
problems, linear separability is achieved by mapping the samples to a high-dimensional space using kernel functions
(in this study, radial basis kernels are used). The decision function is:

P(y = 1 ∣ x) =

1+e−(w

x+b)

T

1

n

                                                               (2)

Among them, α i is the Lagrange multiplier, and K (
f(x) = sign(∑ αiyiK(xi, x) + b)
i=1
Random  Forest:  A  Representative  of  Bagging  Ensemble  Learning.  By  constructing  a  large  number  of  decision
xi, x
trees and synthesizing their voting results for prediction. When a single decision tree is growing, the Gini coefficient
is often used to select the optimal splitting feature to minimize the "impurity" of nodes.

) is the kernel function.

Gini(D)=1−k=1K(pk)2                                                                      (3)
Among them, D is the current node sample set, K is the number of categories, and pk is the proportion of samples
belonging  to  the  k-th  category.  Random  forest  effectively  reduces  model  variance  and  prevents  overfitting  by
introducing dual randomness of samples and features.

XGBoost:  An  advanced  representative  of  Boosting  ensemble  learning.  It  fits  the  data  using  an  additive  model
(weighted sum of multiple decision trees) and iteratively adds new trees to fit the residuals from the previous round
of predictions. The objective function includes a loss function and a regularization term to control model complexity
and prevent overfitting.

                                                       (4)
Among them, l is the loss function (such as logarithmic loss), Ω (ft) is the regularization term used to control the
(t−1)
complexity  of  the  t-th  tree  f.  XGBoost  optimizes  the  objective  through  second-order  Taylor  expansion
approximation, demonstrating excellent performance in both accuracy and efficiency.

n
= ∑ l(yi, y�i
i=1

(xi)) + Ω(ft)

+ f

(t)

L

t

All features were standardized before training. Use grid search combined with 5-fold cross validation to optimize
key  hyperparameters  for  each  model  on  the  training  set,  such  as  the  regularization  coefficient  C  of  logistic
regression and SVM, the number and maximum depth of trees in random forests, the learning rate and maximum
depth of trees in XGBoost, etc. The final evaluation of model performance is conducted on an independent test set
that has never been involved in training and tuning.

4. Result and Discussion

4.1. Result

After completing data preprocessing, feature engineering, and model tuning, the performance of each model was
evaluated on a unified test set. The evaluation used five indicators, namely accuracy, precision, recall, F1 score, and
AUC (area under the ROC curve), to comprehensively reflect the classification ability of the model. The results are
shown in Table 1.

Table 1 Comprehensive Comparison of Prediction Performance of Different Machine Learning Models

Model

Accuracy

Precision

Recall

F1 score

AUC

Logistic regression

SVM

SF

XGBoost

0.834

0.848

0.862

0.876

0.701

0.732

0.758

0.781

0.468

0.512

0.570

0.602

0.562

0.602

0.651

0.680

0.792

0.821

0.853

0.872

Table 1 shows the five core performance indicators of four models on the test set. Accuracy measures the proportion
of  correct  overall  classification;  Accuracy  measures  the  proportion  of  customers  predicted  by  the  model  to  actually
make  a  purchase;  Recall  rate  measures  the  proportion  of  customers  who  will  actually  make  a  purchase  that  is
successfully  predicted  by  the  model;  The  F1  score  is  the  harmonic  mean  of  precision  and  recall,  used  for
comprehensive evaluation; The AUC measurement model has the overall ability to rank positive samples higher than

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468
Author name / Procedia Computer Science 00 (2025) 000–000

1467
 5

negative samples, and the closer it is to 1, the better. As can be seen from the table, XGBoost leads in all indicators.

In  addition  to  prediction  accuracy,  the  computational  efficiency  of  the  model  is  an  important  consideration  in
practical applications. Table 2 records the time it takes for each model to complete training and test set prediction in the
same hardware environment.

Model

Logistic regression

SVM

SF

XGBoost

Table 2 Comparison of Model Training and Prediction Efficiency (Unit: Second)

Training time

Prediction time (test set)

0.8

125.3

15.2

9.5

0.02

18.7

0.35

0.08

Table 2 illustrates: This table compares the operational efficiency of four models. Training time refers to the total
time required to complete model training (including cross validation tuning) on the training set; Prediction time refers
to the time it takes to make forward predictions on the test set. Logistic regression has the fastest speed, SVM is the
slowest, and Random Forest and XGBoost are in between. Among them, XGBoost achieves the best accuracy while
maintaining high training and prediction efficiency.

To understand the decision-making basis of the model, we analyzed the feature importance ranking of each model.
Table  3  shows  the  three  most  important  features  identified  by  logistic  regression  (based  on  normalized  coefficient
absolute values), random forest, and XGBoost.

Table 3 Model Feature Importance Ranking (Top 3)

Ranking

Logistic regression (coefficient absolute value)

SF

XGBoost

1

2

3

Recent purchase time (Recency)

Total consumption amount (Monetary)

Total frequency of purchases

purchase

Latest
time(Recency)
Total frequency of purchases

purchase

Latest
time(Recency)
Total frequency of purchases

Total  consumption  amount
(Monetary)

Average order value

Table 3 shows the three most important features that different models consider for prediction. Logistic regression
determines  importance  by  the  size  and  direction  of  feature  weights,  while  Random  Forest  and  XGBoost  determine
importance  by  calculating  the  reduction  in  impurity  (or  information  gain)  caused  by  features  when  splitting  nodes.
Although the model principles are different, "recent purchase time" is unanimously considered as the primary predictor,
verifying the core position of R (proximity) in the RFM framework. XGBoost recognizes the importance of the derived
feature of "average order value", reflecting its ability to capture more complex patterns.

4.2. Discussion

The  recall  rate  of  logistic  regression  is  the  lowest  (0.468),  indicating  that  its  prediction  strategy  is  relatively
conservative  and  tends  to  misjudge  more  potential  customers  as  not  purchasing.  This  may  be  due  to  its  strong
assumption of linearly separable data not being valid on complex behavioral data. SVM uses kernel function mapping
to  find  nonlinear  interfaces  in  high-dimensional  space,  which  performs  better  than  logistic  regression.  However,  its
performance  is  highly  dependent  on  the  selection  of  kernel  function  and  penalty  parameter  C,  resulting  in  high
optimization costs.  Random forest constructs a large number of decision trees with high diversity through Bootstrap
aggregation  and  random  feature  subset  strategy,  and  smooths  the  prediction  variance  of  individual  trees  through  the
"voting" mechanism,  thus achieving stable and excellent performance. XGBoost uses a  Boosting mechanism, where
subsequent  trees  focus  on  learning  difficult  samples  that  were  misjudged  earlier,  and  combine  the  predictions  of  all
trees  in  the  form  of  additive  models.  At  the  same  time,  the  regularization  term  in  its  objective  function  effectively
controls complexity, ultimately achieving the best prediction accuracy.

Logistic regression has the fastest training and prediction speed, and is suitable for online reasoning scenarios that
require extremely high real-time performance or extremely limited resources. The training time of SVM far exceeds

1468
6

Hanwen Zhang  et al. / Procedia Computer Science 281 (2026) 1463–1468
Author name / Procedia Computer Science 00 (2025) 000–000

other  models,  and  its  time  complexity  becomes  the  main  bottleneck  in  large-scale  data,  with  poor  scalability.  The
training of random forests can be highly parallelized and the time is acceptable. XGBoost achieves top-level prediction
accuracy  while  optimizing  its  weighted  quantile  sketch,  histogram  algorithm,  and  other  features,  resulting  in
significantly higher training efficiency than random forests. It demonstrates an excellent balance between accuracy and
efficiency, making it highly suitable for large-scale industrial applications.

In terms of model interpretability, the coefficients of logistic regression have the most direct interpretability, and the
size  and  direction  of  feature  weights  clearly  indicate  their  marginal  impact  on  purchase  probability.  The  tree  model
provides  global  interpretation  through  feature  importance.  A  highly  insightful  finding  is  that  regardless  of  model
complexity,  'recent  purchase  time'  remains  the  most  important  predictive  feature  among  all  models,  which  strongly
validates  the  classic  business  rule  (R  in  RFM  models)  that  'customer  recent  activity  is  the  best  predictor  of  future
behavior' in a data-driven manner. The three core indicators (R, F, M) in the RFM framework consistently rank high in
importance  ranking,  which  deeply  indicates  that  domain  knowledge  based  careful  feature  engineering  is  the
cornerstone of improving the performance of any machine learning model. XGBoost further explores the importance of
the derived feature of "average order value", reflecting its ability to capture more subtle consumption patterns.

5. Conclusion

This  study  systematically  compared  the  performance  of  four  machine  learning  algorithms,  namely  logistic
regression,  support  vector  machine,  random  forest,  and  XGBoost,  in  predicting  consumer  purchasing  behavior.  The
experimental  results  show  that  under  the  same  feature  engineering  and  evaluation  framework,  XGBoost  algorithm
achieves  the  best  balance  between  prediction  accuracy  (F1  score  0.680,  AUC  0.872)  and  training  efficiency,
significantly better than other comparative models, demonstrating the powerful ability of gradient boosting ensemble
algorithm in processing complex and non-linear consumer behavior data. Random forests  exhibit excellent accuracy
and  robustness,  while  logistic  regression  holds  irreplaceable  value  in  specific  scenarios  due  to  its  outstanding
interpretability  and  computational  efficiency.  The  analysis  of  feature  importance  consistently  confirms  the  core
predictive power of RFM features such as "recent purchase time", highlighting the importance of combining domain
knowledge with data-driven modeling.

Reference

[1] Li L. Analysis of e-commerce customers' shopping behavior based on data mining and machine learning[J]. Soft Computing, 2023: 1-10.

[2] Akram N, Aravindhan K, Sujatha K, et al. Consumer behavior prediction using machine learning algorithms[M]//Exploring psychology, social

innovation and advanced applications of machine learning. IGI Global Scientific Publishing, 2025: 109-130.

[3] Lin J. Application of machine learning in predicting consumer behavior and precision marketing[J]. PLoS One, 2025, 20(5): e0321854.

[4]  Ebrahimi  P,  Basirat  M,  Yousefi  A,  et  al.  Social  networks  marketing  and  consumer  purchase  behavior:  The  combination  of  SEM  and

unsupervised machine learning approaches[J]. Big Data and Cognitive Computing, 2022, 6(2): 35.

[5]  Mohan  L,  Devarajan  M,  Alotoum  F  J,  et  al.  Advanced  Data  Analytics  for  Predicting  Consumer  Behavior  Using  Machine  Learning  and
Association Rule Mining[C]//2025 International Conference on Technology Enabled Economic Changes (InTech). IEEE, 2025: 908-914.

[6]  Chaubey  G,  Gavhane  P  R,  Bisen  D,  et  al.  Customer  purchasing  behavior  prediction  using  machine  learning  classification  techniques[J].

Journal of Ambient Intelligence and Humanized Computing, 2023, 14(12): 16133-16157.

[7] Li H. Social Media Data Mining and Online Consumer Behavior Analysis[J]. Procedia Computer Science, 2025, 261: 406-413.

[8] Bhoyar S, Bhoyar P, Shah M A. A machine learning-based predictive approach in evaluating consumer behavior[J]. Journal of Statistics and

Management Systems, 2023, 26(8): 1955-1963.

[9]  Abdul  Aziz  M,  Mustakim  N  A,  Abdul  Rahman  S.  Decision  tree  and  rule-based  classification  for  predicting  online  purchase  behavior  in

Malaysia[J]. Malaysian Journal of Computing (MJoC), 2024, 9(2): 1905-1915.

[10]  Zvarikova  K,  Machova  V,  Nica  E.  Cognitive  artificial  intelligence  algorithms,  movement  and  behavior  tracking  tools,  and  customer

identification technology in the metaverse commerce[J]. Review of Contemporary Philosophy, 2022, 21: 171-187.

[11] GhorbanTanhaei H, Boozary P, Sheykhan S, et al. Predictive analytics in customer behavior: Anticipating trends and preferences[J]. Results

in Control and Optimization, 2024, 17: 100462.

[12]  Xu  Z,  Zhu  G,  Metawa  N,  et  al.  Machine  learning  based  customer  meta-combination  brand  equity  analysis  for  marketing  behavior

evaluation[J]. Information Processing & Management, 2022, 59(1): 102800.

