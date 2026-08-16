---
conversion_metadata:
  converted_at: "2026-07-21T14:05:20Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Lou et al.pdf"
  source_pdf_sha256: "d0dc8d891f44faae8d724bd353abf19da18167dbf6ae69c423325e4a326166ce"
  page_count: 27
  markdown_char_count: 184356
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Big Data
Article in Press

https://doi.org/10.1186/s40537-026-01464-y

Predicting customer buying habits using 
convolutional neural network

Received: 1 September 2025

Zhuang Lou, Shuai Wang, Xiaoyue Yu & Wei Song

Accepted: 2 May 2026

Cite this article as: Lou Z., Wang S., 
Yu X. et al. Predicting customer buying 
habits using convolutional neural 
network. J Big Data (2026). https://doi.
org/10.1186/s40537-026-01464-y

We are providing an unedited version of this manuscript to give early access to its 
findings. Before final publication, the manuscript will undergo further editing. Please 
note there may be errors present which affect the content, and all legal disclaimers 
apply.

If this paper is publishing under a Transparent Peer Review model then Peer

Review reports will publish with the final article.

© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International 
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit 
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do 
not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the 
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain 
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

---

<!-- PAGE 2 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Predicting customer buying habits using convolutional neural network 
Zhuang Lou1, Shuai Wang1, Xiaoyue Yu2*, Wei Song3

1Department of Business Administration, Shandong Women’s University, Jinan, 250000, China.

2Department of International Education, Zhujiang College, South China Agricultural University, Guangzhou, 510000, China.

3Direct, Macau Lotus TV, Macao SAR,999078, China.

*Corresponding Author: Xiaoyue Yu (xiaoyueyu20246552456@outlook.com)

ABSTRACT

The key to personalized retail is to accurately predict consumer behavior, but traditional models can be problematic 
due  to  the  large  dimensionality  of  demographic  data  and  non-linear  relationships  between  demographics  and 
behavior. In this paper, a new deep learning model is suggested, which applies a Convolutional Neural Network 
(CNN)  to  estimate  the  level  of  individual  income  and  provide  specific  product  suggestions.  In  contrast  to  the 
traditional tabular learners, our method converts normalized customer features to grayscale image matrices of size 
20×10, allowing the CNN to learn the complex spatial features and latent behavioral patterns in the hybrid pooling 
layers.  The  algorithm  is implemented in  two  combined steps:  high-granularity  income tier  categorization  and  a 
recommendation engine that is powered by a purchase probability matrix. The experimental findings using a dataset 
of 980 people prove that the proposed model is much better than state-of-the-art benchmarks and has statistically 
significant accuracy of 93.06 in income prediction and 95 in recommendation success. These results highlight how 
the use of spatial feature extraction can be more effective in consumer analytics and offer a scalable pipeline to e-
commerce real-time personalization.

Keywords: Convolutional neural network, Income prediction, Buying habits, Product recommendation.

1. INTRODUCTION 
Customers are being prioritized in the business and have emerged as the dominant factor. With this in mind, firms 
must present customers with incentives in order to lessen the likelihood of them switching to competitors. A modest 
unpleasant encounter with a client may indicate that the customer may churn [1]. Many e-commerce use cases rely 
heavily  on  predicting  future  consumer  behavior  [2].  In  other  words,  a  company's  customers  are  its  lifeblood. 
Customers  are  at  the  center  of  marketing  efforts,  and  organizations  frequently  make  poor  decisions  when  they 
ignore the behavior and motivations of their customers. Understanding the relationship between customer metrics 
and profitability and company value is crucial as marketing aims to become more accountable. There are many 
different types of customer metrics. It has been divided into two categories: perceptual and unobservable/behavioral 
metrics. Observable measurements comprise consumer behaviors that are usually associated with the acquisition or 
use of a good or service. Customer views (such as service quality), attitudes (such as customer satisfaction), and 
behavioral intents (such as purchase intention) are instances of unobservable constructs [3].

Market  basket  analysis,  according  to  Russell  and  Petersen  [4],  focuses  on  the  mechanism  by  which  customers 
choose products from a certain set of groups within a single shopping trip. Its goal is to find relationships between 
the selections of various products made in a certain retail establishment, like a supermarket. According to Wang 
and Hong [5], shifts in consumer behavior lead to erratic customer profitability as well as wasteful and unproductive 
marketing strategy. In order to accomplish their marketing objectives, the authors present a customer profitability 
management system that makes use of data mining techniques. The development of the internet and e-commerce 
has completely changed how consumers make purchases as well as how companies or brands promote to draw in 
and keep customers by sending communications that are tailored to their individual needs [6].

The emergence of these e-commerce platforms has also made it more difficult for marketers and business owners 
to manage their operations effectively. In order to enhance purchase revenue, e-commerce will rely entirely on 
1

---

<!-- PAGE 3 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

technology and experts who can create customized shopping experiences for potential customers [7]. Due to this 
new trend's entire reliance on technology, there are numerous additional obstacles that must be overcome in order 
to realize the benefits of this new framework. Personalized options, the internet, appropriate product presentation, 
and many other aspects can all have an impact on the e-commerce business [8, 9].

It  is  crucial  to  predict income levels and comprehend  the complex  connection  between  income  and  purchasing 
patterns since it has impacts on both the commercial and the private spheres. From the perspective of business, such 
knowledge can be utilized for the improvement of marketing communication, for customization of products and 
increasing customer satisfaction. Thus, the segmentation of the target market according to the income level is very 
beneficial for the companies as it allows to invest more effectively and generate the highest possible revenues. On 
the same  note,  for individuals,  a  better  understanding  of spending  behavior can  help  in making more informed 
decisions on their expenses and help in finding products and services that suit their needs and wants.

Moreover, the study of the correlation between purchasing behaviors and income also gives insights on consumers’ 
behaviors.  It  enables the  business to  target  the  right audience  and  market  its  products  and  services  to the right 
audience. For the researchers, the knowledge of this correlation can help to enhance the overall understanding of 
the economic drivers affecting consumers’ decisions. It can also help to reveal information about tendencies of the 
society and inequality in consumers’ behavior depending on income level.

Customer behavior analysis has been a process of identifying patterns in the data through techniques such as logistic 
regression.  However,  identifying  relationships  between  data  and  analyzing  patterns  become  complex  issues 
especially when solving problems in large datasets. Convolutional Neural Networks (CNNs) are in fact a type of 
Deep Learning (DL) that can be applied to solve this problem effectively. CNNs are good at feature extraction 
which helps in their application for customer data analysis, and since customer data can be represented in the form 
of multi-dimensional arrays.

While  numerous  methods  exist  for  predicting  income  and  analyzing  customer  behavior,  including  traditional 
machine learning algorithms [10-19] and sales prediction/product recommendation approaches [20-26], many of 
these  approaches  suffer  from limitations  when  dealing  with  the  high  dimensionality and complexity of modern 
datasets. Traditional machine learning methods together with basic neural networks face major challenges when 
attempting to identify the complex interactions between different customer characteristics, their earned income and 
purchase patterns. One of the greatest weaknesses of simple neural networks is that they cannot identify significant 
latent features of customer data in multi-dimension, which is a compounding of the problems that other conventional 
machine learning algorithms face with non-linear correlations between data. Basic neural networks demonstrate 
their ineffectiveness when processing complex data according to multiple research studies [27]. Machine learning 
Random forests show limitations when dealing with data sets that have very high dimensions [28]. The existing 
techniques need improvement because they fail to manage complex data requirements effectively.

Despite the fact that DL approaches are increasingly used for the analysis of customer behavior, there are no studies 
on  the  use  of  CNNs for  the  prediction  of  customers’ attributes  and  purchasing  behavior.  Previous  works  could 
utilize a basic neural network architecture or other machine learning approaches besides deep learning. This study 
explicitly fills this gap by showing how CNNs are distinctly able to rise above these constraints. Compared to the 
traditional machine learning models and simple neural  networks, which are not always able to capture complex 
feature interactions, CNNs have a greater ability to process high-dimensional structured data. In particular, using 
our proposed method, in which the standard one-dimensional demographic and behavioral data about customers 
are  converted  into  two-dimensional  20×10  feature  matrices,  the  CNN  will  be  able  to  extract  complex  spatial 
correlations and latent patterns in a unique way [29]. This special spatial processing of tabular data enables the 
network  to  isolate  very  small  correlations  that  earlier  algorithms  fail  to  capture,  thereby  greatly  improving  our 
accuracy in predicting income, and also making the results of our product recommendations very targeted.

2

---

<!-- PAGE 4 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Recent advances in deep learning [30-32], have shown promising results in various domains. The following research 
investigates the direct use of CNNs yet future work should consider integrating these approaches especially transfer 
learning methods to enhance model functionality. The mentioned strategies enhance model generalization while 
making it more resilient across different domains.

In our research, first, we endeavor to predict the income level using CNNs. Then, based on the projected income 
level, we aim to derive a more accurate model of individuals' purchasing habits. This, in turn, enables us to provide 
more precise recommendations. Our method not only predicts purchasing habits but also includes income level as 
a  factor  that  has  a  significant  impact  on  those  habits,  which  gives  a  better  view  of  the  customers.  The  key 
contributions of the work are summed up as follows:

•  Presenting a new architecture for CNN based on hybrid pooling layers for predicting people's income level. 
•  Presenting a probabilistic model for modeling the buying habits of customers and taking into account the

income level.

•  Using the combination of individual characteristics and customer behavioral records in buying products to

form a recommender system.

The  paper  follows  this  progression:  Similar  works  and  backgrounds  are  examined  in  the  second  section.  The 
introduced technique is explained in the third section, and the results obtained from its implementation are presented 
in the fourth section. Section 5 discusses the findings, implications, limitations and future works; and finally, the 
fifth section includes the conclusions.

2. Background and Related Works 
The current research includes two areas, one is predicting people's income level and the other is recommending 
products. In this section, some recent researches have been studied in each of these categories.

2.1. Predicting People's Income Levels

Yamnampet  [10]  focused  on  income  determination,  using  various  classifiers  to  reduce  cost  and  risk.  It  also 
demonstrates the performance of each algorithm in customer identification and analyzes scored probabilities, scored 
labels, false negatives, and true positives.

Thapa [11] evaluated the performance of five machine learning algorithms on an adult income dataset, revealing 
the Random Forest Classifier as the most effective with 86.3% training and 86% test accuracy.

Chen et al. [12] proposed random forest (RF) as a method for predicting salaries, demonstrating its superiority over 
traditional methods such as k-nearest neighbors, naive Bayes, logistic regression, and decision trees on the adult 
dataset. RF enhances accuracy through dataset preprocessing, variance reduction, and factor elimination.

Viroonluecha and Kaewkiriya [13] aimed to develop a system for predicting salary in Thailand based on Deep 
Learning,  analyzing  personal  data  from  a  job  search  website  with  over  1.7  million  users.  When  compared  to 
algorithms like Random Forest and Gradient Boost Trees, the model achieved an optimal R-squared result of 0.462.

Kablaoui and Salman [14] utilized a dataset of over 20,000 salaries in the USA to apply three supervised machine 
learning techniques: linear regression, random forest, and neural networks. It was found that the neural network 
outperformed the other models, achieving an accuracy of 83.2% .

Wang et al. [15] analyzed the factors influencing college graduates' starting salaries using machine learning methods 
at a 2020 financial university. The factors included academic qualifications, professional disciplines, employment 
regions, industries, gender, and student cadres, with the XGBoost model emerging as the best predictor .

Vemulapati  et  al.  [16]  discussed  income  prediction  methodologies  using  Long  Short-Term  Memory  (LSTM), 
ConvLSTM,  Bi-Directional  LSTM  (BiLSTM),  and  Stacked  LSTM  networks.  It  highlighted  pre-processing

3

---

<!-- PAGE 5 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

approaches and training mechanisms, and demonstrated successful implementations. It was found that the BiLSTM 
was more accurate.

Chakrabarty and Biswas [17] presented an Income Prediction Model using  Grid Search on Adult Census Data, 
Hyper-Parameter Tuning, Gradient Boosting, and Ensemble Learning, achieving a Validation Accuracy of 88.16%, 
the highest ever .

Rehman  et  al.  [18]  proposed  to  demonstrate the  use  of  data  mining  and  machine  learning  strategies  to  address 
income disparity issues. The study aimed to classify machine learning for predicting whether an individual has an 
annual income.

Wang  [19]  utilized  48,842  income  census  data  from  the  Adult  Data  Set  to  predict  annual  income  levels  using 
machine learning approaches. Thirteen attributes, including native-country, occupation, marital status, education, 
workclass, and age, were considered. A randomly divided 32,561 individuals were trained using various algorithms .

2.2.  Sales Prediction and Product Recommendation

Xian et al. [20] explored the use of historical sales and behavioral data analytics to create a recommendation model 
for online B2C businesses during the COVID-19 pandemic. They proposed a process model using RFM analysis, 
k-means clustering, and association rule theory for shopping basket analysis and product recommendations. This 
model improved sales, market responsiveness, and profitability for companies in similar situations .

Chaubey et al. [21] compared various machine learning techniques for predicting customer purchasing behavior. 
They  utilized  supervised  classification  methods  such  as  dummy  classifier,  XgBoost,  AdaBoost,  ANN,  SGD, 
random  forest,  SVM,  Naïve  Bayes,  KNN,  decision  trees,  and  logistic  regression.  Additionally,  they  employed 
hybrid methods like SvmAda, RfAda, and KnnSgd. The best classification model was a hybrid method using an 
ensemble stacking technique (KnnSgd), achieving an accuracy of 92.42%.

Kumar et al. [22] introduced a new algorithm for predicting customer interest that used pattern mining techniques 
and  Multi  Variant  K-means  clustering.  It  identified  user  purchase  histories,  enquires,  and  purchase  patterns, 
generating recommendations for advertisements and banner placement. This approach enhanced retail marketing 
strategies and customer retention.

Anitha and Patil [23] aimed to enhance business sales and profit by providing relevant and timely data on potential 
customers  in  the  retail  industry.  The  data  was  analyzed  using  a  systematic  approach  employing  the  K-Means 
algorithm.  The  study  used  the  Recency,  Frequency  and  Monetary  (RFM)  model  and  dataset  segmentation 
principles, validating various dataset clusters based on the Silhouette Coefficient.

Nguyen et al. [24] created a customized recommendation system based on a multi-stage retrieval approach. Their 
methodology is a combination of collaborative filtering, Bayesian Personalized Ranking (BPR) and popularity-
based algorithms to produce candidate items, which are ranked with LightGBM and Deep Neural Networks (DNN).

Parihar and Yadav [25] investigated the use of machine learning to predict customer behavior in  e-commerce by 
analyzing  clickstream  and  customer  data.  Their  goal  was  to  use  artificial  intelligence  to  investigate  output 
discrepancies  in models,  with  a focus  on sequential  clickstreams  and  static  consumer  data,  in  order to increase 
customer loyalty and transactions.

Zhao and Keikhosrokiani [26] created a novel data science life-cycle and process model that uses RFM analysis 
and other analytics algorithms to anticipate sales and recommend products. They used customer segmentation and 
machine learning techniques to examine traditional shop business transformation. The prediction system, which 
used  XGBoost  and  Random  Forest,  was  able  to  forecast  consumer  orders  with  77.82%  accuracy.  The 
recommendation system also used association rules to evaluate transaction statistics, revealing how online shopping 
platforms promote products to customers.

4

---

<!-- PAGE 6 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

In order to give a clear picture of the existing research field and point out the gaps in the methodology that this 
study fills, Table 1 will present the summaries of the methodologies, goals, strengths, and limitations of the recent 
literature in the field.

Table 1. Summary of the related studies

Reference

Year

Methodology

Goal

Strengths

Limitations

Yamnampet [10]  2017

Various Machine 
Learning Classifiers

Income determination 
and customer 
identification.

Thorough evaluation of 
scored probabilities and error 
rates (false 
negatives/positives).

Relies on traditional 
classifiers; may struggle with 
highly complex, non-linear 
data interactions.

Thapa [11]

2023

ML Algorithms 
(Random Forest, etc.)

Adult income 
prediction.

Achieves strong baseline 
accuracy (86%) and provides 
a broad algorithm 
comparison.

Basic ML architectures lack 
the ability to extract deep 
spatial/latent features from 
datasets.

Chen et al. [12]

2022

Random Forest (RF)

Viroonluecha & 
Kaewkiriya [13]

2018

Deep Learning vs. RF, 
Gradient Boosting

Salary prediction on the 
adult dataset.

Enhances accuracy via 
rigorous preprocessing, 
variance reduction, and factor 
elimination.

Tree-based models can be 
limited when scaling to very 
high-dimensional behavioral 
data.

Salary prediction for 
Thailand labor 
workforce.

Utilizes a massive real-world 
dataset (1.7M users); DL 
outperformed traditional ML.

R-squared value of 0.462 
indicates a significant portion 
of data variance remains 
unexplained.

Kablaoui & 
Salman [14]

2022

Neural Networks, 
Linear Regression, RF

Salary prediction on a 
USA dataset.

Demonstrates the superiority 
of basic neural networks 
(83.2% accuracy) over 
traditional ML.

Basic NNs are less effective 
than CNNs at capturing 
spatial relationships in 
structured data.

Wang et al. [15]

2022

XGBoost

Predict starting salary 
of college graduates.

High interpretability of 
demographic and academic 
influencing factors.

Vemulapati et al. 
[16]

2023

LSTM, ConvLSTM, 
BiLSTM, Stacked 
LSTM

Income prediction.

Effectively captures 
sequential data; BiLSTM 
showed high accuracy.

Highly domain-specific 
(financial university 
graduates); limited 
generalizability.

High computational 
complexity; RNN/LSTMs are 
less optimized for non-
sequential spatial data than 
CNNs.

Chakrabarty & 
Biswas [17]

2018

Gradient Boosting, 
Ensemble Learning, 
Grid Search

Adult census income 
level prediction.

Achieves high validation 
accuracy (88.16%) through 
rigorous hyperparameter 
tuning.

Reliance on traditional tabular 
ML limits deeper feature 
extraction capabilities.

Rehman et al. 
[18]

2022

Data Mining, Machine 
Learning

Classify existence of 
annual income to 
address disparity.

Strong socio-economic 
application and focus on 
income inequality.

Focuses on binary/simple 
classification rather than 
granular income tier 
prediction.

Wang [19]

2022

Various Machine 
Learning Approaches

Predict annual income 
levels based on 13 
attributes.

Comprehensive feature 
importance analysis on a 
standard dataset.

Constrained by the limitations 
of traditional ML in modeling 
complex behavioral matrices.

5

---

<!-- PAGE 7 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Reference

Year

Methodology

Goal

Strengths

Limitations

Xian et al. [20]

2022

RFM Analysis, K-
means, Association 
Rules

B2C product 
recommendation during 
COVID-19.

Direct real-world business 
applicability; improves 
market responsiveness.

Chaubey et al. 
[21]

2023

ML & Hybrid 
Ensembles (e.g., 
KnnSgd)

Predict customer 
purchasing behavior.

High accuracy (92.42%) 
achieved through advanced 
ensemble stacking techniques.

Kumar et al. [22]  2021

Pattern Mining, Multi 
Variant K-means

Customer interest 
prediction and ad 
recommendation.

Effectively uses purchase 
histories to optimize retail 
marketing strategies.

Anitha & Patil 
[23]

2022  K-Means, RFM Model

Enhance retail sales via 
customer segmentation.

Systematic validation of data 
clusters using the Silhouette 
Coefficient.

Nguyen et al. 
[24]

2024

Retrieval Strategy (CF, 
BPR) + 
LightGBM/DNN

Improve user 
engagement via 
personalized product 
recommendations.

Successfully combines 
multiple algorithms to handle 
large-scale data and the cold-
start problem.

Parihar & Yadav 
[25]

2021

Machine Learning

Predict consumer future 
preferences.

Successfully integrates both 
sequential clickstream data 
and static demographic data.

Static clustering approaches 
may fail to adapt to rapid, 
dynamic shifts in user 
behavior.

Complex hybrid ensembles 
can be computationally 
expensive and lack model 
interpretability.

Clustering-based 
recommendations often suffer 
from the "cold-start" problem 
for new customers.

K-Means assumes spherical 
data clusters, which may not 
accurately represent complex 
human behavior.

Performance highly 
dependent on the retrieval of 
candidates; DNN components 
showed lower MAP@K 
compared to boosted trees.

Output discrepancies require 
manual AI investigation, 
limiting end-to-end 
automation.

Zhao & 
Keikhosrokiani 
[26]

2022

XGBoost, RF, 
Association Rules, RFM

Sales prediction and 
product 
recommendation.

Provides a holistic life-cycle 
model combining both 
prediction and 
recommendation phases.

Accuracy of 77.82% suggests 
significant room for 
improvement via deep 
learning feature extraction.

2.3. CNNs with Hybrid Pooling

CNN models, despite their high efficiency in pattern learning, require a large training set. For small training sets, 
CNNs may face the problem of overfitting [33]. Overfitting reduces the generalizability of the CNN when applied 
to new instances. In many situations, the overfitting problem in CNNs can be attributed to the function used in the 
pooling layers, based on which one can obtain the feature map extracted from the data through the activations output 
of the convolutional layers [34]. In CNN designs today, two pooling algorithms are frequently utilized. The first 
function is called max pooling, and it takes each feature map region's maximum activation value. This allows for 
the extraction of the most prominent features and the elimination of less significant ones.  In real-world applications, 
this function causes overfitting [35].

Average  pooling,  the  second  operator,  takes  into  account  the  results  for  a  region  in  equal  measure.  The  ReLU 
activation  and  average  pooling  operator  work  together  to  lessen  the  impact  of  strong  activations  while 
simultaneously  producing  a  significant  amount of  zeros  in  the  feature  map.  However,  when  average  pooling  is 
combined  with  other  activation  operators—like  the  hyperbolic  tangent  function—it  may  cause  loss  of  data  by 
ignoring positive as well as negative activations. In light of these drawbacks, numerous research have introduced 
novel  pooling  techniques  in  an  effort  to  reduce  the  overfitting  issue  in  CNNs.    Hybrid  pooling  [36]  can  be  an

6

---

<!-- PAGE 8 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

efficient  solution.  It  combines  the  benefits  of  both  max  pooling  and  average  pooling,  thereby  improving  the 
generalizability of CNNs.

This strategy seeks to boost the adaptability of the CNN model by leveraging diverse pooling strategies during 
training and averaging their predictions at test time. During training, each feature map in the convolution layer 
undergoes  both  average  pooling  and  max  pooling.  The  choice  between  them  is  randomized,  governed  by  a 
probability (p) for average pooling and (1-p) for max pooling. This approach, as described in [36], essentially blends 
the benefits of both pooling methods, aiming to achieve superior generalizability compared to relying on a single 
strategy. This mechanism can be formulated as follows [36]:

𝑆 = {

𝑆𝑎𝑣𝑔                  𝑤𝑖𝑡ℎ 𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦 𝑝
𝑆𝑚𝑎𝑥         𝑤𝑖𝑡ℎ 𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦 1 − 𝑝

)1)

Where 𝑆𝑎𝑣𝑔  is  the  output  of  average  pooling  operator  for  various  regions  and  is  defined  by  the  set  𝑆𝑎𝑣𝑔 =
1
{𝑠𝑎𝑣𝑔

}. The following relationship holds for each member of this set:

, … , 𝑠𝑎𝑣𝑔

𝐽

𝑗 =
𝑠𝑎𝑣𝑔

1
|𝑅𝑗|

∑

𝑖∈𝑅𝑗

𝑎𝑖

(2)

where, 𝑅𝑗   shows the jth pooling segment, which includes a group of activations such as {𝑎1, … 𝑎|𝑅𝑗|}. On the other 
hand, in eq. (1), 𝑆𝑚𝑎𝑥   refers to the output of max pooling operator for various segments and is defined by the set 
}. For each member of this set, the following relationship holds: 
𝑆𝑚𝑎𝑥 = {𝑠𝑚𝑎𝑥

𝐽
, … , 𝑠𝑚𝑎𝑥

1

𝑗 = max
𝑠𝑚𝑎𝑥
𝑖∈𝑅𝑗

𝑎𝑖

Then, in the test phase, the result of any pooling area is measured using eq. (4) [36]:

𝑆 = 𝑆ℎ𝑦𝑏𝑟𝑖𝑑 = 𝑝 × 𝑆𝑎𝑣𝑔 + (1 − 𝑝) × 𝑆𝑚𝑎𝑥

(3)

(4)

This approach seeks to enhance CNN model diversity by strategically combining two distinct pooling operators for 
various feature maps.

3. Research Methodology 
This section provides a detailed description of the data collection process. It also outlines the steps of the proposed 
method for predicting customer purchasing habits. This method leverages deep learning techniques.

3.1. Data 
The  data  used  in  this  research  was  collected  through  a  comprehensive  questionnaire,  which  was  meticulously 
designed  to  capture  a  wide  range  of  variables.  The  gathered  information  through  each  questionnaire  from 
participants include demographics, shopping habits, income level, and product preferences of the participants. The 
used questionnaire and response options have been presented in Appendix A.  This questionnaire was distributed 
among 980 individuals, ensuring a diverse sample in terms of age, gender, and income levels. The 980 participants 
are well balanced in terms of demography: 48 of them were males and 52 of them were females. Age categories 
were divided into five with the highest proportion of 25-34 (31.10 %) and 35-44 (27.56%) representing the largest 
proportion of the workforce consumers. Geographically, respondents were mostly located in a wide range of urban 
and suburban areas to capture a wide range of retail accessibility and economic conditions. The responses were then 
organized  into  a  structured  dataset  for  further  analysis.  This  dataset  includes  detailed  information  about  the 
purchasing habits of individuals across six different categories of goods.  
The categorization of goods in this study includes mobile phones, tablets, laptops, clothing, entertainment items, 
and food. For each category, a set of brands available at the data collection site was identified, and respondents

7

---

<!-- PAGE 9 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

were asked to indicate their preferences. In addition to the information on people’s purchasing habits, a table was 
created to describe the characteristics and behavior of each individual. Table 2 provides a comprehensive overview 
of the collected information for each individual in this dataset.

Table 2. List of descriptive information for each individual.

Row  Feature 
Gender 
1 
Marital Status 
2 
Age 
3 
Education Level 
4 
Job Category 
5 
Job History 
6 
Place of Residence 
7 
Residential Status 
8 
Specific Disease 
9 
Alcohol Consumption 
10 
Consumption of Tobacco or Other Addictive Substances 
11 
Number of In-person Shopping Instances per Week 
12 
Number of Online Shopping Instances per Week 
13 
Quantity of cart during In-person Shopping 
14 
Quantity of cart during Online Shopping 
15 
Number of Working Hours per Week 
16 
Income Level 
-

Type 
Nominal 
Nominal 
Numeric 
Ordinal 
Nominal 
Numeric 
Nominal 
Ordinal 
Nominal 
Nominal 
Nominal 
Numeric 
Numeric 
Numeric 
Numeric 
Numeric 
Numeric

Based on the input information for the income level feature, respondents are divided into five categories of income 
levels: very low (164 samples), low (178 samples), average (208 samples), high (193 samples), and very high (237 
samples).  The  goal  of  the  proposed  method  is  to  predict  individuals’  income  levels  based  on  the  independent 
features listed in Table 2. Then, modeling the purchasing habits based on the determined income levels.

Although  the  data  used  in  this  study  has  a  solid  basis,  some  weaknesses  in  the  data  collection  process  can  be 
identified. The use of a questionnaire opens the possibility of self-reporting bias especially on sensitive variables 
like precise income or shopping frequency. Moreover, the sampling was also geographically limited to certain areas, 
which can affect the extrapolation of the buying patterns to other cultural or rural settings. These were alleviated 
by careful design of the questionnaire and the weighted cross- entropy loss function to make the model resilient to 
different samples.

3.2. Proposed Method 
It seems that a person’s habits and preferences during shopping are related to their behavioral characteristics and 
income level. Therefore, this research attempts to model people’s shopping habits based on the information obtained 
from their income classification. The proposed method models customer behavior and recommends goods in three 
steps:

1.  Preprocessing, 
2.  Classification of individuals based on income 
3.  Product recommendation based on income.

The structure of the presented approach is illustrated in Figure 1. First, the collected information from individuals 
(Table 2) is normalized and transformed so that it can be processed by learning models. Then, in the second step, 
the  individual’s  features  are  processed  by  a  CNN,  and  their  income  level  is  predicted  to  determine  the  target 
category for the individual based on the predicted value.

8

---

<!-- PAGE 10 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

In the third step of the presented approach, a suitable product is recommended based on the predicted income level. 
At this stage, a purchase probability matrix is utilized to model people’s shopping habits based on their income 
level. This matrix, which has a number of rows equal to the number of recommended categories for goods and a 
number of columns equal to the number of income groups, models the probability of purchasing a product in a 
specific category by individuals in different income groups.

As illustrated in Figure 1, the data collected via the questionnaire is divided into two categories: training data and 
test data. The dataset instances are permuted randomly and then partitioned into subsets using the cross-validation 
approach (as explained in section IV) to determine the training and test sets. Initially, in the training phase, the 
purchasing  habits  model,  denoted  as  P,  is  formed  based  on  the  purchase  histories  and  preferences  of  training 
instances. Then, for each sample belonging to the test set, they are first classified based on their income level using 
the CNN model. Based on the predicted income and the probability matrix P, a product is recommended to the 
individual.

Figure 1. Structure of the presented approach.

3.2.1 Preprocessing

The proposed method utilizes a straightforward mechanism for preprocessing the data, which encompasses three 
sub-steps: ‘value conversion’, ‘missing value management’, and ‘feature normalization’. The preprocessing begins 
with the conversion  of  nominal values into  numerical  ones.  In  this  process,  each  value in the  nominal  features 
is converted into a natural number. For ordinal nominal features, a unique list is compiled based on the rank of the 
values present in that feature. Subsequently, a value like IX is assigned to each value in the sorted list, proportional 
to its position. This approach ensures a streamlined and effective preprocessing of the data. For non-ordinal nominal 
features, a list of unique values is created based on the frequency of each nominal value. Ultimately, each value in 
the mentioned feature is replaced with a natural number corresponding to it in the IX set. By executing the above 
process, all features of the dataset are converted into a numerical format.

9

---

<!-- PAGE 11 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

The  choice  of  this  particular  numerical  mapping,  as  opposed  to  more  traditional  numerical  encoding  methods, 
including  direct  one-hot  encoding  or  target  encoding,  is  specifically  meant  to  be  compatible  with  the  high-
dimensional  feature-to-image  mapping  in  Section  3.2.2.  Although  standard  encoding  works  well  with  more 
traditional tabular learners, it usually creates sparse vectors which do not provide the structure density needed by 
convolutional filters. In our design, this preliminary mapping will give a standardized number base that will enable 
all the features to be divided into 100 fine-grained intervals. This generates the 1600-bit binary representation that 
is required to make a complete 20×10 grayscale image. Through the use of this approach instead of traditional 
approaches,  we  are  able  to  have  the  CNN  perceive  demographic  and  behavioral  characteristics  as  geometrical 
patterns, and the model is able to identify deep, non-linear relationships between disparate characteristics that would 
have been missed by standard encoding schemes.

Subsequently, records with missing values are corrected. For this purpose, if a feature with a missing value in a 
record is numerical, it is replaced with the mean of the existing values for that feature. Conversely, for nominal 
features with missing values, the missing value is replaced with the mode or the value with the highest frequency 
for that feature.

The preprocessing step concludes with feature normalization. During this process, the value vector of each feature, 
denoted as x, is mapped to the range [0,1] using eq. (5).

𝑁𝑥 =

𝑥−𝑥𝑚𝑖𝑛
𝑥𝑚𝑎𝑥−𝑥𝑚𝑖𝑛

(5)

Where 𝑥𝑚𝑖𝑛  and 𝑥𝑚𝑎𝑥  respectively describe the smallest and largest values for feature (x).

3.2.2 Classification of Individuals Based on Income Using CNN

In this step, a CNN with hybrid pooling layers is employed to classify individuals based on their income level. For 
this purpose, a matrix representation of the set of normalized features obtained from the previous step is used. The 
process of converting tabular customer data to a format that can be processed by convolutional processing consists 
of four steps of discretization and mapping:

1.  Interval Mapping: Each normalized feature 𝑥 ∈   [0, 1] is mapped to one of 100 equal intervals of length

0.01.

2.  High-Dimensional Encoding: Using one-hot encoding, each interval is converted into a binary string of 
length 100. As an example, a value between [0.01, 0.02) will give a 1 at the second position and 0 at other 
positions.

3.  Bit-Stream Aggregation: With each record being represented by a high-dimensional bit-stream of 1600 bits

(16×100), all 16 features are concatenated to generate a bit-stream.

4.  Spatial Grayscale Mapping: This bit-stream is divided into blocks of 8 bits with each block being mapped 
to a single pixel intensity (0-255). The pixels are then reformed into a 20×10 grayscale image matrix.

This organized representation enables the CNN to process customer profiles as spatial patterns to enable the latent 
feature correlations that are usually misplaced in traditional vector-based models to be identified. The obtained 
matrix is fed to a CNN classifier. The CNN model uses this input to predict the individual’s income level.

The reason for selecting CNNs for this research is their ability to efficiently handle large, structured data, such as 
the  matrix  representation  of  individual  characteristics  employed  in  our  study.  Their  hierarchical  organization, 
incapacity  for  translation,  and  abilities  in  parallel  processing  qualify  them  for  activities  that  involve  pattern 
recognition and classification in such data. When compared with additional deep learning methods like Recurrent 
Neural Networks (RNNs) or LSTMs, CNNs can deliver higher performance in tasks dedicated to spatial relations 
and  high-dimensional  data.  In  contrast,  RNNs  and  LSTMs are mainly  created  for  sequential  data,  in  which  the 
10

---

<!-- PAGE 12 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

arrangement of elements is important. Though they can comply with the data organization detailed in this study, 
they may not be as efficient as CNNs in capturing spatial features.

In order to increase the generalization capabilities of the model on small and imbalanced data, we apply the Hybrid 
Pooling strategy described in Section 2.3. This mechanism contrasts with max and average pooling by switching 
between max and average pooling stochastically during training unlike in the case of static pooling. This helps the 
model to avoid over-fitting to the most salient activations (which is one of the main causes of overfitting in customer 
behavior data) and to make sure that the feature maps do not lose the subtle behavioral indicators. Figure 2 shows 
the particular arrangement of these layers into our architecture.

Figure 2. The proposed CNN model for predicting individuals’ income levels.

Another major issue with income prediction is the imbalance in classes (164 very low vs. 237 very high samples). 
In  order  to  solve  this  without  losing  useful  data,  we  use  a  Weighted  Cross-Entropy  (WCE)  loss  function.  The 
technical explanation behind WCE is to impose a penalty weight 𝑤𝑖 on each of the classes inversely proportional 
to its frequency in the training set. This compels the gradient descent algorithm to make decisions that are more 
focused on the proper classification of minority groups, which practically eliminates the majority bias that is usually 
rife with conventional CNNs. The WCE loss is mathematically formulated as:

𝐿𝑜𝑠𝑠  =   −𝛴(𝑤𝑖 ∗   𝑦𝑖 ∗ log(𝑝𝑖) +   (1 − 𝑦𝑖) ∗ log(1 − 𝑝𝑖))

(6)

In Eq. (6), 𝑤𝑖 is the weight of the class i and for this class its true label is 𝑦𝑖. Furthermore, 𝑝𝑖 is the probability that 
is being predicted for the class i. 
The careful tuning of hyperparameters is essential to optimize the performance of CNN models. The optimal hyper 
parameter  setting  for  the  employed  CNN  structure  was  obtained  using  the  grid  search  strategy.  In  this  regard, 
various hyper parameter settings of the CNN were examined using the training loss metric. The examined hyper 
parameters for tuning the model include the dimensions and number of convolutional filters, dimensions of the 
pooling layers, and also type of activation layers. Additionally, various settings for training-related parameters of 
mini  batch  size  and  optimizer  were  considered  in  the  tuning  step.  Table  3  shows  the  search  space  for  each 
configurable parameter of the CNN in this research.

11

---

<!-- PAGE 13 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

The best obtained configuration of the CNN has been presented in Fig. 2. The inputs of the introduced CNN are 
defined as the matrix that described at the beginning of this section. This CNN comprises two layers of convolution 
with 16 and 24 filters, respectively. The width and length of these layers are 6×6 and 3×3, respectively. The output 
of each of these layers are processed through the ReLU activation function, and feature map extraction at each stage 
is performed by hybrid pooling with dimensions of 2×2. For both convolution and pooling layers, the stride was 
considered  as  1.  Finally,  two  consecutive  fully  connected  layers  are  utilized  to  extract  features.  The  first  one 
transforms the extracted features into a vector form. The second fully connected layer calculates the probability of 
the sample belonging to each of the target categories. This is done by outputting a posterior probability vector. 
Ultimately, these features are classified by a SoftMax layer to predict the income level for the sample based on it.

Table 3. the search space for each configurable CNN parameter

CNN parameter

Dimension of convolution layers 
Number of convolution filters 
Dimension of pooling layers 
Activation function 
Optimizer  
Mini batch size

Search space 
{2, 3, 5, 7, 9} 
{4, 8, 16, 24, 32, 48} 
{2, 3, 4, 5} 
ReLU, PReLU, Leaky ReLU 
SGDM, Adam 
{16, 32, 64}

3.2.3 Modeling Shopping Habits and Recommending Goods Based on Income

After employing the proposed CNN model for classifying individuals based on their income level, a matrix is used 
to model people’s shopping habits and offer suggestions to them based on the created model. This matrix shows 
which goods people with different incomes are more likely to buy and which category of goods they are less likely 
to purchase. The structure of the probability matrix used in the proposed method is shown in Figure 3.

Figure 3. The structure of the probability matrix for modeling shopping habits and recommending goods to 
individuals in the proposed method.

12

---

<!-- PAGE 14 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Referring to Figure 3, the depicted matrix is structured with its rows equivalent to the recommendable goods and 
its columns corresponding to the distinct income groups. Consequently, this probability matrix is characterized by 
N rows and K columns. Each matrix element specifies the probability that an individual, belonging to the income 
group represented  by  the  current  column,  will  purchase  the  goods  associated  with  the  current row  category.  In 
essence, Pi,j  in Figure 3 represents the probability of an individual from income category j purchasing a good from 
category  i.  During  the  data  collection  phase,  each  participant  provided  personal  information  and  responded  to 
queries about their purchasing habits for various goods. Consequently, each individual’s purchase record can be 
denoted as <Ni,Ki>, where Ni signifies the category of goods that the individual purchased, and Ki  designates the 
income group to which the individual belongs. Therefore, the database can be structured as depicted in Table 4, for 
each category of recommended goods.

Table 4. Data structure for storing individuals’ shopping habits in the proposed method.

Row 
1 
2 
… 
X

Income Group  Purchased Goods Category

K1 
K2 
… 
KX

N1 
N2 
… 
NX

In Table 4, X denotes the number of records in the database. To calculate the probability matrix presented in the 
proposed  method,  first,  the  total  selection  of  each  category  of  goods  by  each  income  group  of  individuals  is 
calculated as follows:

𝑀𝑖,𝑗 = |{< 𝑁𝑐, 𝐾𝑐 >|𝑁𝑐 = 𝑖 𝑎𝑛𝑑 𝐾𝑐 = 𝑗}|

(7)

Where 1 ≤ 𝑐 ≤ 𝑋 is the counter for the database records. In the above relation, the number of records where an 
individual in category j has chosen a good in category i is counted. After calculating the matrix M, each element 
located in the matrix M is divided by the sum of the elements of the column related to that element.

𝑃𝑖,𝑗 =

𝑀𝑖,𝑗

∑

𝑁
𝑘=1

𝑀𝑘,𝑗

(8)

By applying the above relation to each element of matrix M, the probability matrix P is obtained, which indicates 
the probability of different groups of individuals choosing different categories of goods. After forming the matrix 
P,  the  act  of  suggesting  goods  to  individuals  can  be  performed.  For  this  purpose,  after  receiving  the  personal 
information of each person, the classification operation is first performed using the CNN model. In the next step, if 
the individual is classified into class (j), the good with the highest probability in the (j)-th column of the matrix (P) 
is suggested to the individual.

4. Research Finding 
The  proposed  approach  was  implemented  and  evaluated  using  MATLAB  2020.  We  reviewed  the  presented 
approach in two scenarios: in the first scenario, we predict people's income level, and in the second phase, based 
on the model that was considered to predict people's buying habits, we make recommendations.

In this study, stratified 5-fold cross-validation (CV) was utilized for the proposed method. First, we permuted the 
dataset instances randomly and then, divided the data into 5 parts and each part made up 20% of the data set. Then 
we repeated the operation 5 times. During each repetition, 80% of the data was used for training (based on 70% of 
instances) and validating (based on 10% of the instances) the model. After training the model, the remaining 20% 
unseen data is used as test data, and the classification result for each test sample is compared with its ground-truth 
label, leading to the one of the following conditions:

•

True Positive (TP): The quantity of positive cases accurately detected by the model .

13

---

<!-- PAGE 15 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

False Negative (FN): The quantity of cases that the model incorrectly identified as negatives . 
False Positive (FP): The quantity of samples in which the model incorrectly classified as positive . 
True Negative (TN): The quantity of samples in which the model properly detected a negative.

• 
• 
• 
Accuracy represents the overall proportion of correct predictions made by a model. Mathematically, this can be 
expressed as:

𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 =  100 ×

𝑇𝑃+𝑇𝑁
𝑇𝑃+𝐹𝑃+𝑇𝑁+𝐹𝑁

(9)

Prioritizing  true  positives,  precision  measures  the  percentage  of  genuine  positives  among  all  model-predicted 
positives. Crucial for minimizing false positives. Mathematically:

𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 =

𝑇𝑃
𝑇𝑃+𝐹𝑃

(10)

Focusing on completeness, recall measures the percentage of true positives accurately identified out of all actual 
positive instances. Crucial for avoiding missed positives. Mathematically:

𝑅𝑒𝑐𝑎𝑙𝑙 =

𝑇𝑃
𝐹𝑁+𝑇𝑃

(11)

F-Measure provides a balanced assessment of both precision and recall. It is often employed when both metrics 
hold equal importance. Mathematically:

𝐹 − 𝑀𝑒𝑎𝑠𝑢𝑟𝑒 =

2∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙

4.1. Evaluation in terms of Predicting People's Income Level

(12)

We evaluated the proposed method in this phase based on individuals' income. This method was assessed using the 
criteria of f-measure, recall, precision, and accuracy, and we compared it to other methods.

We evaluated the recommended method in three different modes: the proposed method, CNN (Max.pool), and CNN 
(Avg.pool).  Due  to  the  use  of  hybrid  pooling  layers  that  combines  average  and  maximum  pooling  layers,  we 
compared our proposed CNN model with two other CNN models that only use max pooling and average pooling 
layers. Also, we compared our proposed method with references [17-19], which we named Chakrabarty & Biswas, 
Rehman et al and Wang respectively.

Figure  4  shows  the  average  accuracy,  precision,  recall,  and  f-measure  graphically.  In  Figure  4a,  our  method 
demonstrates superior performance in predicting individual income levels, exceeding both the CNN (Max.pool) 
and  Wang  methods  in  average  accuracy  by  margins  of  1.5%  and  2.7%  respectively.  This  clearly  indicates  the 
improved accuracy of our method .In Figure 4b, our method outperforms the CNN (Max.pool) and Wang methods 
in  precision  by  1.5%  and 2.6% respectively, indicating  fewer  false  positive  predictions  and  higher  precision  in 
identifying specific income levels. Additionally, our method surpasses Wang's method by a significant 2.8% in 
recall, demonstrating its superior ability to identify relevant instances within a dataset, including specific income 
levels.  Furthermore,  the  1.6%  increase  in  f-measure  compared  to  the  CNN  (Max.pool)  method  highlights  the 
superior balance between precision and recall offered by our proposed method. In conclusion, our proposed method 
excels in accurately predicting individual income levels, as evidenced by its superior f-measure, recall, precision, 
and accuracy metrics.

The  proposed  CNN  architecture  takes  the  advantage  of  both  average  and  max  pooling,  while  attempting  to 
overcome their limitations using the hybrid pooling layers. Average pooling aggregates all the feature activations 
in a given region and max pooling identifies the most active region. Using hybrid pooling layers, makes our model 
to more efficiently extract features from the customer data than models that employ one type of pooling only. This 
is likely to have been the reason for the enhanced performance as depicted by Figure 4.

14

---

<!-- PAGE 16 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Figure 4. Evaluating the quality of the classification.

The proposed method achieves the highest values across all metrics: precision 0.9295, recall 0.9321, F-measure 
0.9306,  and  accuracy  93.06%.  Following closely  are  CNN  (Max.Pool)  with  precision  0.9147,  recall 0.9146,  F-
measure  0.9145,  and  accuracy  91.53%,  and  CNN  (Avg.Pool)  with  precision  0.8996,  recall  0.9028,  F-measure 
0.9007,  and  accuracy  90.10%.  The  methods  Chakrabarty  &  Biswas,  Rehman  et  al.,  and  Wang  exhibit  lower 
performance, with Rehman et al. demonstrating the lowest values across all metrics.

Figure 5 presents an illustration of the confusion matrices pertaining to the introduced methodology and alternative 
comparative methodologies. Within this matrix, the rows depict the  ground-truth classification of the instances, 
while the columns refer to the output of each model, arranged in alphabetical order. The elements situated along 
the main diagonal signify the accurate classification of the samples, whereas the non-main elements signify the 
quantity of classification errors found in the test samples.

15

---

<!-- PAGE 17 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Figure 5. Evaluating the confusion matrix.

By segregating our confusion matrix from other confusion matrices, such as image 5b and image 5c, it becomes 
evident that our method, utilizing hybrid pooling layers, exhibits superior performance in segregating each group 
of data compared to the CNN (Max.pool) and CNN (Avg.pool) layers. Additionally, our matrix reveals that our 
proposed methodology has demonstrated better performance in segregating categories compared to the confusion 
matrices (5d, 5e, and 5f). The confusion matrix for our proposed method in figure 5a showed that the elements in 
the  diagonal  are  higher  than  the  other  methods,  meaning  more  number  of  elements  correctly  classified income 
levels.  Apart  from  this,  the  off-diagonal  elements  (errors)  are  also  less  in  our  matrix  as  compared  to  the  other 
methods which clearly explains that the proposed model is efficient enough to classify the individuals into their 
respective income category.

The proposed method yields the highest accuracy of 93.06% among all the methods under comparison. Our method 
yields the lowest value of false positive rate, but at the same time, it yields a higher true positive rate for each of 
the income groups, which is evidence of the fact that the improvement in accuracy is not only due to the reduction 
of false positives, but due to the increase of true positives as well.

Figure 6 depicts the ROC curve, presenting the FPR (false positive rate) and TPR (true positive rate) values for 
evaluating our multi-class classification. We computed the TPR and FPR for each class separately. After obtaining 
these TPR and FPR values, we aggregated and compared the ROC curve results for each method across all classes. 
The ROC curve for our proposed method exhibits a larger area under the curve compared to other approaches. This 
signifies  a  superior  balance  between  the  TPR  and  FPR  achieved  by  our  model.  In  simpler  terms,  our  method 
effectively identifies a higher proportion of true income levels (high TPR) while minimizing the number of false 
positive classifications.

16

---

<!-- PAGE 18 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Figure 6. Evaluating the ROC curve.

The methods presented by Chakrabarty & Biswas [17], Rehman et al. [18], and Wang [19] might face issues in 
terms of modeling the interactions of the features within the customer data due to the model complexity or inability 
to handle imbalanced datasets in which certain income brackets could be under-represented in the dataset. On the 
other hand, the proposed CNN with hybrid pooling has a more flexible architecture that can potentially capture a 
wider range of interactions between the features.

Table 5 compares the performance of various methods using precision, recall, F-measure, and accuracy metrics. In 
this  table,  in  addition  to  previously  compared  approached,  the  RF  [12]  and  BiLSTM  [16]  models  have  been 
considered for comparisons. For a fair comparative analysis, all of the models were trained and tested using the 
same instances. The proposed method achieves the highest values across all metrics. Following closely are CNN 
(Max.Pool) and CNN (Avg.Pool) confirming the effectiveness of CNNs in solving this problem, even while using 
conventional  pooling  layers.  The  BiLSTM  [16]  and  RF  [12]  models  show  performance  close  to  the  proposed 
method. This indicated the desirable performance of deep learning and ensemble learning approaches in predicting 
income  level.  The  methods  Chakrabarty  &  Biswas  [17],  Rehman  et  al.  [18],  and  Wang  [19]  exhibit  lower 
performance, with Rehman et al. demonstrating the lowest values across all metrics.

Table 5. Performance comparison between the proposed method and previous approaches in predicting income level.

Methods

Proposed 
CNN (Max.Pool) 
CNN (Avg.Pool) 
Chen et al. [12] 
Vemulapati et al. [16] 
Chakrabarty & Biswas [17] 
Rehman et al. [18] 
Wang [19]

Precision 
0.9295 
0.9147 
0.8996 
0.9077 
0.9125 
0.8734 
0.8133 
0.9027

Recall 
0.9321 
0.9146 
0.9028 
0.9084 
0.9108 
0.8755 
0.8159 
0.9041

F-Measure 
0.9306 
0.9145 
0.9007 
0.9079 
0.9111 
0.8743 
0.8141 
0.9029

Accuracy 
93.0612 
91.5306 
90.1020 
90.9184 
91.0204 
87.5510 
81.6327 
90.4082

The methods [17-19] might face issues in terms of modeling the interactions of the features within the customer 
data due to the model complexity or inability to handle imbalanced datasets in which certain income brackets could

17

---

<!-- PAGE 19 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

be under-represented in the dataset. On the other hand, the proposed CNN with hybrid pooling has a more flexible 
architecture that can potentially capture a wider range of interactions between the features.

4.2. Statistical Significance Analysis

As explained in Section 4.1, stratified 5-fold cross-validation was used to strictly assess the performance of the 
proposed framework. The findings of the suggested CNN model were contrasted with two architectural variants 
(Standard Max Pooling and Average Pooling) and five models of the recent literature [12, 16, 17, 18, 19] and the 
results were reported in Table 5. To show that the performance gains obtained by the proposed approach are not 
the result of chance, a statistical significance analysis was performed.

Table 6 provides the summary of the average accuracy, standard deviation, and the paired t-test results. The highest 
mean accuracy of 93.02% and the lowest standard deviation (0.53%), which was obtained with the proposed model, 
not only proves high performance but also demonstrates high stability of the model on various data subsets.

Table 6. Comparison of Statistical Analysis of Model Accuracy (5-Fold CV)

Model

proposed 
CNN(Max.Pool) 
CNN(Avg.Pool) 
Chen et al. [12] 
Vemulapati et al. [16] 
Chakrabarty & Biswas [17] 
Rehman et al [18] 
Wang [19]

Average Accuracy 
93.0612 
91.5306 
90.1020 
90.9184 
91.0204 
87.5510 
81.6327 
90.4082

Std. Dev. Acc. 
0.5332 
0.8396 
1.0290 
0.5773 
0.7287 
1.9962 
1.5962 
0.6981

p-value 
- 
0.00506 
0.00076 
0.00372 
0.01563 
0.00576 
0.00003 
0.00049

As shown in Table 6, all calculated p-values are significantly lower than the standard alpha level (𝛼  =  0.05). The 
fact  that  our  hybrid  pooling  method  is  significantly  better  than  standard  CNN  pooling  mechanisms  (p  <  0.01) 
confirms that our hybrid approach to pooling does not cause the loss of spatial information in feature extraction to 
the same extent as standard CNN pooling mechanisms. Moreover, the fact that our 20×10 spatial mapping strategy 
outperforms the established benchmarks like Vemulapati et al. [16] (p = 0.015) and Wang [19] (p < 0.001) shows 
that our strategy is more effective at capturing latent socio-economic correlations compared to the traditional deep 
learning or machine learning architecture. These results are strong statistical indicators that the suggested changes 
to the CNN pipeline bring a substantial improvement in customer behavior analytics.

4.3. Evaluations in terms of product recommendation

In  this  phase,  we  have  investigated  the  efficiency  of  the  presented  model  from  the  aspect  of  product 
recommendation. In other words, when we provide a recommendation for product types, we compared that product 
with customers' buying habits and based on this comparison, we estimated the accuracy using eq. (8) The results of 
the  proposed  approach  have  been  compared  with  several  models  including  CNN  with  Max  Pooling  layers  for 
(instead of hybrid pooling), and two baseline approaches: LightGBM [24], and RFM [26].

In Figure 7, the mean accuracy of product classification is illustrated. Our method has achieved a mean accuracy 
of 95% in category 1, and also reached average accuracies of 92.89% and 94.81% in categories 4 and 6, respectively. 
These results demonstrate that our approach has performed very well compared to the comparative method RFM 
and the CNN (Max. Pool) method.

18

---

<!-- PAGE 20 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

a. Product Category 1

b. Product Category 2

c. Product Category 3

d. Product Category 4

e. Product Category 5

f. Product Category 6

Figure 7. Evaluating the product categories accuracy.

4.3. Feature Importance Analysis 
This experiment analyzes the importance of various features and their contribution in prediction of income level by 
the  employed  CNN  structure.  To  do  this,  an  attention  layer  was  added  between  the  input  layer  and  the  first 
convolutional layer of the network. This layer, assigns weight to each input feature based on their importance and 
transfers the weights to the subsequent layers. Since in input feature was translated to a binary vector of length 100, 
the obtained weights for all 100 bits of each feature were summed to obtain the overall weight of the attribute. After 
that, the obtained sum of weights for all features were normalized using the max-min approach (Equation 1). Figure 
8 demonstrates the obtained normalized weight for each input feature which reflects its importance in predicting 
income level of the individuals.

19

---

<!-- PAGE 21 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Figure 8. The normalized importance of features obtained through employing an attention layer in the structure of 
the CNN

As it is depicted in Figure 8, the six most important variables that can be useful in determining the income level 
include “Job Category”, “Education Level”, “Age”, “Job History”, “Place of Residence”, and “Marital Status”.

It is common knowledge that job category is usually a pointer to income levels, particularly in the emerging markets. 
There is normally a positive relationship between the level of education and the income earner’s wages or salaries. 
The third dependent variable age is also taken into consideration as it defines the career level and further more 
earning capability in hierarchical corporate environment. Whereas, stable & progressive job history has possibility 
that only career advancement and higher earnings might be expected. Additionally, there is a higher probability of 
higher average income in the urban areas especially the tier 1 and tier 2 cities. Finally, some cultures may determine 
economical and financial aspects of a couple’s financial life based on marital status and therefore this factor, based 
on income level, is the sixth in the list. However, it should be pointed out that the significance of these factors may 
differ based on the cultural, economic and social environment of the place from which the data was collected.

4.4. Practical Implications and Real-World Applications

The  suggested  CNN-based  pipeline  and  probability  matrix  has  a  high  potential  of  practical  implementation, 
especially in e-commerce and retail ecosystems. When used to classify users in real-time as an income level by 
deploying  the  CNN  model,  platforms  can  automatically  classify  users  into  income  levels  based  on  initial 
demographic or session data. After classifying one into an income group, the system uses the purchase probability 
matrix (P) to customize user interfaces (UI) by ranking high-probability product categories in search results and 
recommendation banners. This architecture can support dynamically tuned marketing policies; an example would 
be to offer a 'High' income user premium electronics or luxury goods and offer a 'Low' income user value-oriented 
alternatives. This kind of focused strategy does not only improve the customer experience, but also helps retailers 
to manage their inventory effectively. By forecasting the demand of the income-specific products, businesses can 
optimize the stock levels and minimize the overhead expenses and the chances of stockouts.

In  the  financial  services  industry,  the  model  can  be  applied  to  evaluate  the  credit  status  of  individuals  thus 
minimizing  on  defaults.  Besides,  it  can  also  assist  financial institutions in  providing  relevant  financial  services 
including loans and investment products according to the customer’s financial strength.

20

---

<!-- PAGE 22 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

When applied to the public policy area, the model can be used to determine who among the population requires 
social  help  and  therefore  those  who  should  be  given  the  resources.  Furthermore,  the  model  can  be  used  by 
policymakers to understand the distributional effect of economic policies in order to make informed decisions.

Finally, in the area of consumer rights advocacy, the model can be applied to search for cases of unjustified or 
misleading  pricing  or  promotion  of  products  for  low-income  consumers.  Also,  through  the  knowledge  of  the 
consumer behavior and their choice, the advocacy groups can then call for the production of safer and cheaper 
products.

With the help of using the AI and machine learning possibilities in processes the suggested model can foster fair 
and progressive society.

5. Discussion, limitation, and Future Works 
The current study aimed at assessing the outcomes of a new CNN model with the incorporation of hybrid pooling 
layers for estimating customer income levels and then using it for the product recommendation tasks. The results 
show that the proposed method outperforms the previous methods in the accuracy, precision, recall and F1-measure. 
This section  provides  a  further  discussion  on the significance  of  these  findings, how  these findings  expand  the 
knowledge of consumers’ behavior, and possible applications. We also present the limitations that were experienced 
during the research and recommend future research directions.  
 The  success  of  our  CNN  architecture  in  predicting  income  levels,  achieving  an  overall  accuracy  of  93.06%, 
suggests its ability to capture complex relationships within customer data. By incorporating income level as a key 
factor, our approach offers a more nuanced understanding of how income demographics influence buying habits. 
This advancement goes beyond traditional methods that might struggle to capture these intricate interactions.  The 
proposed method gives insight into the possibility of using CNNs with hybrid pooling in the analysis of customer 
behavior.  To  validate  the  generalization  ability  of  the  proposed  model  we  used  5-fold  cross  validation.  This 
evaluation methodology ensured that there was no overfitting of the models since it was quite a rigorous process.  
Comparison  between  hybrid  pooling  and  the  other  forms  of  pooling  such  as  max  pooling  and  average  pooling 
showed that the former outperformed the latter in terms of accuracy, precision, recall and F1-score. These results 
decisively indicate that the employment of the hybrid pooling strategy positively contributes to the improvement 
of  the  model’s  capability  to  generalize  from  unseen  data.  The  use  of  average  and  max  pooling  through  hybrid 
pooling layers in our model allows for the extraction of more complete features from customer data as compared to 
the use of standard pooling alone.  
This finding contributes to the growing body of research exploring the effectiveness of deep learning techniques in 
understanding  consumer  behavior,  especially  considering  the  significant  improvement  of  2.7%  in  accuracy 
compared to the Wang method (90.4%) which utilizes conventional pooling layers. The fact that one can forecast 
the  income  levels  and  make  recommendations  based  on  this  data  (mean  accuracy  of  93.1%  for  product 
recommendations) is quite practical in reality.  
The possibility of precise income level forecasting and the factors influencing consumers’ behavior are significant 
for different industries. For instance, the information in this context can be used by retailers to manage their stocks, 
design and implement marketing strategies, and design new products that suit the needs of their target customers. 
This can have a positive impact on customer satisfaction, the conversion rate of sales, and better resource utilization. 
Such information may help to evaluate the credit standing of clients and adjust the offered financial services. In 
addition, such models can be useful for the policymakers in order to improve the economic policies and fight against 
the income disparity. Aside from the practical implications, our research contributes to the literature on consumer 
behavior and the part that income plays in consumers’ decisions. It can be useful for the public policy debate on 
issues such as income disparity and consumer rights.

5.1. Limitations and Future Works

Even though the proposed model is highly accurate and practically useful, certain limitations should be considered. 
These are divided into limitations of the present and future research directions. 
Research Limitations:

21

---

<!-- PAGE 23 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

•  Population Representativeness: Although the 980-sample sample is all-inclusive in this study, it might not 
be  an  accurate  reflection  of  the  entire  world  population,  which  can  create  predictive  biases  in  highly 
different socio-economic settings.

•  Geographic  and  Cultural  Specificity:  The  present  results  are  based  on  the  regional  data;  hence,  the 
performance of the model can differ in the case of other cultural backgrounds with their own shopping 
patterns.

•  Feature Engineering Scope: The existing feature set, although strong, might not have necessary granular

•

cultural or micro-economic indicators that can be used to determine individual buying choices. 
Internal  vs.  External  Validation:  Cross-validation  has  been  done  to  ensure  that  the  model  is  highly 
generalized in the given dataset, but the stress-testing of the model against completely external datasets that 
are independent of the given dataset has not been conducted yet.

Future Research Directions:

•

Increasing Data Sources: Future research must use a variety of data sources across different countries to 
enhance the external validity and globalizability of the results.

•  Adding Longitudinal Data: By adding variables that track time-series, the model would be able to adjust to

changing consumption trends as time progresses.

•  Advanced Architectures: We plan to explore Transformer-based models and transfer learning techniques 
to further enhance sequence modeling and reduce the data training requirements for unfamiliar domains. 
Interdisciplinary Integration: Cooperation with behavioral scientists to incorporate psychological profiling 
may offer a better insight into the reason behind the expected buying behavior.

•

•  Hardware  and  Efficiency Optimization:  Investigating  memristive  CNN  architectures  could  significantly 
improve  computational  and  energy  efficiency,  enabling  real-time  processing  for  large-scale  industrial 
applications.

6. Conclusion 
The paper focused on the utilization of a convolutional neural network to analyze and model customer purchasing 
habits  in  relation  to  their  income  levels.  The  study  consisted  of  three  primary  stages:  data  preprocessing, 
categorizing individuals based on their income levels, and providing product recommendations tailored to their 
income brackets. The primary aim of the paper was to enhance understanding of individuals' purchasing behaviors 
and to improve the accuracy and relevance of product recommendations personalized to their specific income levels. 
The  results  indicated  that  the  presented  approach  outperformed  alternative  techniques  by  increasing  average 
accuracy to 93.06% and precision to 92.95%, thus demonstrating superior performance in predicting individuals' 
income  levels.  Additionally,  the  proposed  method  achieved  at  least  2.77%  improvement  in  terms  of  f-measure 
compared to the benchmark methods. This significant improvement shows the high quality of the classification 
results  produced  by  the  proposed  method.  Furthermore,  in  the  phase  2,  our  method  showed  that  it  has  a  mean 
accuracy  of  95%  which  is  at  least  4.05%  higher  compared  to  other  comparative  methods  in  product 
recommendation.

APPENDIX A 
This appendix provides a comprehensive overview of the questionnaire used for data collection and includes the exact wording 
of questions and response options.

Gender:

Demographics 
1. 
o 
o 
o 
2. 
o 
o

Marital Status: 
Single 
Married

Male 
Female 
Prefer not to say

22

---

<!-- PAGE 24 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Job Category: (Please select the category that best describes your current job)

Job History (Years): (How many years have you been working in your current field?) 
Place of Residence:

Divorced 
Widowed 
Living with Partner 
Prefer not to say

Age: (Please enter your age) 
Education Level:

High School Diploma or Equivalent 
Associate's Degree 
Bachelor's Degree 
Master's Degree 
Doctorate or Professional Degree 
Prefer not to say

Management/Professional 
Sales/Service 
Skilled Trades/Labor 
Administrative/Clerical 
Student/Unemployed 
Retired 
Other (Please specify): _________

Urban Area (City) 
Suburban Area 
Rural Area

Residential Status:

Own Home 
Rent Apartment/House 
Live with Family/Friends 
Other (Please specify): _________ 
Do you have any specific chronic diseases? (Yes/No) 
If yes, please specify: _________

Alcohol Consumption:

Never drink alcohol 
Drink occasionally 
Drink regularly

o 
o 
o 
o 
3. 
4. 
o 
o 
o 
o 
o 
o 
5. 
o 
o 
o 
o 
o 
o 
o 
6. 
7. 
o 
o 
o 
8. 
o 
o 
o 
o 
9. 
o 
Shopping Habits 
10. 
o 
o 
o 
11. 
o 
12. 
13. 
14. 
15. 
16. 
Income Level 
17. 
select your income range:  
o 
o 
o 
o 
o 
o

Below $25,000  
$25,000 - $49,999  
$50,000 - $74,999  
$75,000 - $99,999  
$100,000 and above  
Prefer not to say

Consumption of Tobacco or Other Addictive Substances: (Yes/No)

If yes, please specify: _________

On average, how many times do you shop in person per week? 
On average, how many times do you shop online per week? 
On average, how many items do you typically add to your cart during in-person shopping trips? 
On average, how many items do you typically add to your cart during online shopping trips? 
On average, how many hours per week do you typically work?

We understand that income level can be a personal question. If you are comfortable sharing this information, please

Product Preferences  
Thank you for participating in this survey! This section focuses on your preferences for various product categories. 
Please note: There is no right or wrong answer. We are simply interested in understanding your brand choices.

23

---

<!-- PAGE 25 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

Brand 1: _________ 
Brand 2: _________ 
Brand 3: _________ (or "No Preference")

Brand 1: _________ 
Brand 2: _________ 
Brand 3: _________ (or "No Preference")

Brand 1: _________ 
Brand 2: _________ 
Brand 3: _________ (or "No Preference")

If you don't have a preference for a particular category, you can skip that section. 
Mobile Phones: 
• 
• 
• 
Tablets: 
• 
• 
• 
Laptops: 
• 
• 
• 
Clothing: 
• 
• 
• 
Entertainment Items: 
• 
• 
• 
Food: 
• 
• 
•

Brand 1: _________ (e.g., TVs, Video Game Consoles) 
Brand 2: _________ 
Brand 3: _________ (or "No Preference")

Brand 1: _________ (e.g., Grocery Stores, Restaurants) 
Brand 2: _________ 
Brand 3: _________ (or "No Preference")

Brand 1: _________ 
Brand 2: _________ 
Brand 3: _________ (or "No Preference")

Funding

The work described in this paper was supported by a  grant from Social Science Foundation of Shandong Province, China 
(Grant No. 17CGLJ15). This article is the research outcome of a university-level project at Shandong Women’s University 
(Project Approval Number: 2021RCYJ02/57).

Data availability

All data generated or analysed during this study are included in this published article.

REFERENCES 
[1]  Dingli, A., Marmara, V., & Fournier, N. S. (2017). Comparison of deep learning algorithms to predict customer churn

[2]

within a local retail industry. International journal of machine learning and computing, 7(5), 128-132. 
Lang,  T.,  &  Rettenmeier,  M.  (2017,  April).  Understanding  consumer  behavior  with  recurrent  neural  networks.  In 
Workshop on Machine Learning Methods for Recommender Systems.

[3]  Kalaivani, D., & Arunkumar, T. (2018). Multi process prediction model for customer behaviour analysis. International

[4]

Journal of Web Based Communities, 14(1), 54-63. 
Russell, G. J., & Petersen, A. (2000). Analysis of cross category dependence in market basket selection. Journal of 
Retailing, 76(3), 367-392.

[5]  Wang,  H.  F.,  &  Hong,  W.  K.  (2006).  Managing  customer  profitability  in  a  competitive  market  by  continuous  data

[6]

[7]

[8]

mining. Industrial marketing management, 35(6), 715-723. 
Rosário, A., & Raimundo, R. (2021). Consumer marketing strategy and E-commerce in the last decade: a  literature 
review. Journal of theoretical and applied electronic commerce research, 16(7), 3003-3024. 
Felix,  A.,  &  Rembulan,  G.  D.  (2023).  Analysis  of key factors  for  improved  customer  experience,  engagement,  and 
loyalty in the e-commerce industry in Indonesia. Aptisi Transactions on Technopreneurship (ATT), 5(2sp), 196-208. 
Li, Y. F., Guo, L. Z., & Zhou, Z. H. (2019). Towards safe weakly supervised learning. IEEE transactions on pattern 
analysis and machine intelligence, 43(1), 334-346.

24

---

<!-- PAGE 26 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

[9]

Parihar, V., & Yadav, S. (2021). Comparison estimation of effective consumer future preferences with the application 
of AI. Vivekananda Journal of Research, 10, 133-145.

[10]  Yamnampet, G. Comparative analysis of classification models on income prediction. International Journal on Recent

and Innovation Trends in Computing and Communication, 5(4), 451-455.

[11]  Thapa, S. (2023). Adult Income Prediction Using various ML Algorithms. Available at SSRN 4325813. 
[12]  Chen, J., Mao, S., & Yuan, Q. (2022, March). Salary prediction using random forest with fundamental features. In Third 
International Conference on Electronics and Communication; Network and Computer Technology (ECNCT 2021) (Vol. 
12167, pp. 491-498). SPIE.

[13]  Viroonluecha, P., & Kaewkiriya, T. (2018, September). Salary predictor system for thailand labour workforce using 
deep learning. In 2018 18th International Symposium on Communications and Information Technologies (ISCIT) (pp. 
473-478). IEEE.

[14]  Kablaoui, R., & Salman, A. (2022, November). Machine Learning Models for Salary Prediction Dataset using Python. 
In 2022 International Conference on Electrical and Computing Technologies and Applications (ICECTA) (pp. 143-
147). IEEE.

[15]  Wang,  P.,  Liao,  W.,  Zhao,  Z.,  &  Miu,  F.  (2022).  Prediction  of  Factors  Influencing  the  Starting  Salary  of  College

Graduates Based on Machine Learning. Wireless Communications and Mobile Computing, 2022.

[16]  Vemulapati, J., Bayyana, A., Bathula, S. H., Tokala, S., Hajarathaiah, K., & Enduri, M. K. (2023, February). Empirical 
Analysis of Income Prediction Using Deep Learning Techniques. In 2023 IEEE International Students' Conference on 
Electrical, Electronics and Computer Science (SCEECS) (pp. 1-6). IEEE.

[17]  Chakrabarty, N., & Biswas, S. (2018, October). A statistical approach to adult census income level prediction. In 2018 
International Conference on Advances in Computing, Communication Control and Networking (ICACCCN) (pp. 207-
212). IEEE.

[18]  Rehman, A. U., Saleem, R. M., Shafi, Z., Imran, M., Pradhan, M., & Alzoubi, H. M. (2022, February). Analysis of 
Income on the Basis of Occupation using Data Mining. In 2022 International Conference on Business Analytics for 
Technology and Security (ICBATS) (pp. 1-4). IEEE.

[19]  Wang, J. (2022, October). Research on Income Forecasting based on Machine Learning Methods and the Importance 
of  Features.  In  Proceedings  of  the  International  Conference  on  Information  Economy,  Data  Modeling  and  Cloud 
Computing, ICIDC 2022, 17-19 June 2022, Qingdao, China.

[20]  Xian,  Z.,  Keikhosrokiani,  P.,  XinYing,  C.,  &  Li,  Z.  (2022).  An  RFM  model  using  K-means  clustering  to  improve 
customer segmentation and product recommendation. In Handbook of Research on Consumer Behavior Change and 
Data Analytics in the Socio-Digital Era (pp. 124-145). IGI Global.

[21]  Chaubey,  G.,  Gavhane,  P.  R.,  Bisen,  D.,  &  Arjaria,  S.  K.  (2023).  Customer  purchasing  behavior  prediction  using 
machine learning classification techniques. Journal of Ambient Intelligence and Humanized Computing, 14(12), 16133-
16157.

[22]  Kumar,  M.  R.,  Venkatesh,  J.,  &  Rahman,  A.  M.  Z.  (2021).  Data  mining  and  machine  learning  in  retail  business: 
developing efficiencies for better customer retention. Journal of Ambient Intelligence and Humanized Computing, 1-
13.

[23]  Anitha, P., & Patil, M. M. (2022). RFM model for customer purchase behavior using K-Means algorithm. Journal of

King Saud University-Computer and Information Sciences, 34(5), 1785-1792.

[24]  Nguyen, D. N., Nguyen, V. H., Trinh, T., Ho, T., & Le, H. S. (2024). A personalized product recommendation model 
in e-commerce based on retrieval strategy. Journal of Open Innovation: Technology, Market, and Complexity, 10(2), 
100303.

[25]  Parihar, V., & Yadav, S. (2021). Comparison estimation of effective consumer future preferences with the application

of AI. Vivekananda Journal of Research, 10, 133-145.

[26]  Zhao, X., & Keikhosrokiani, P. (2022). Sales Prediction and Product Recommendation Model Through User Behavior

Analytics. Computers, Ma-terials & Continua, 70(2).

[27]  Hussain,  N.  Y.  (2024).  Deep  learning  architectures  enabling  sophisticated  feature  extraction  and  representation  for

[28]

complex data analysis. Int. J. Innov. Sci. Res. Technol.(IJISRT), 9, 2290-2300. 
Islam, M. R., Hossain, M., Alam, M., Khan, M. M., Rabbi, M. M. K., Rabby, M. F., ... & Tarafder, M. T. R. (2025). 
Leveraging Machine Learning for Insights and Predictions in Synthetic ECommerce Data in the USA: A Comprehensive 
Analysis. Journal of Ecohumanism, 4(2), 2394-2420.

[29]  Yang, Y., Wu, Z., Yang, Y., Lian, S., Guo, F., & Wang, Z. (2022). A survey of information extraction based on deep

learning. Applied Sciences, 12(19), 9691.

[30]  Dritsas, E., & Trigka, M. (2025). Machine learning in e-commerce: Trends, applications, and future challenges. IEEE

Access.

[31]  Zhang, P. (2021). E-commerce products recognition based on a deep learning architecture: Theory and implementation.

Future Generation Computer Systems, 125, 672-676.

25

---

<!-- PAGE 27 -->

ARTICLE IN PRESS
ACCEPTED MANUSCRIPT

[32]  Kostopoulos,  G.,  Stefani,  A.,  Vasiliadis,  V.,  &  Kotsiantis,  S.  (2026).  Deep  Learning  for  e-Commerce:  Recent

Developments in Prediction, Personalization and Decision Intelligence. Applied Sciences, 16(5), 2263.

[33]  Thanapol,  P., Lavangnananda, K., Bouvry, P., Pinel, F., & Leprévost,  F. (2020, October). Reducing overfitting and 
improving  generalization  in  training  convolutional  neural  network  (CNN)  under  limited  sample  sizes  in  image 
recognition. In 2020-5th International Conference on Information Tech-nology (InCIT) (pp. 300-305). IEEE. 
[34]  Boureau,  Y.  L.,  Ponce,  J.,  &  LeCun,  Y.  (2010).  A  theoretical  analysis  of  feature  pooling  in  visual  recognition.  In

Proceedings of the 27th international conference on machine learning (ICML-10) (pp. 111-118).

[35]  Zeiler, M. D., & Fergus, R. (2013). Stochastic pooling for regularization of deep convolutional neural networks. arXiv

preprint arXiv:1301.3557.

[36]  Tong, Z., & Tanaka, G. (2019). Hybrid pooling for enhancement of generalization ability in deep convolutional neural

networks. Neurocompu-ting, 333, 76-85.

26

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Big Data
https://doi.org/10.1186/s40537-026-01464-y
Article in Press
Predicting customer buying habits using
convolutional neural network
Received: 1 September 2025 Zhuang Lou, Shuai Wang, Xiaoyue Yu & Wei Song
Accepted: 2 May 2026
We are providing an unedited version of this manuscript to give early access to its
findings. Before final publication, the manuscript will undergo further editing. Please
Cite this article as: Lou Z., Wang S.,
note there may be errors present which affect the content, and all legal disclaimers
Yu X. et al. Predicting customer buying
apply. S
habits using convolutional neural
network. J Big Data (2026). https://doi. If this paper is publishing under a Tran S sparent Peer Review model then Peer
org/10.1186/s40537-026-01464-y Review reports will publish with the fiEnal article.
R
P
N
I
E
L
C
I
T
R
A
© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do
not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Predicting customer buying habits using convolutional neural network
Zhuang Lou1, Shuai Wang1, Xiaoyue Yu2*, Wei Song3
1Department of Business Administration, Shandong Women’s University, Jinan, 250000, China.
2Department of International Education, Zhujiang College, South China Agricultural University, Guangzhou, 510000, China.
3Direct, Macau Lotus TV, Macao SAR,999078, China.
*Corresponding Author: Xiaoyue Yu (xiaoyueyu20246552456@outlook.com)
ABSTRACT
The key to personalized retail is to accurately predict consumer behavior, but traditional models can be problematic
due to the large dimensionality of demographic data and non-linear relationships between demographics and
behavior. In this paper, a new deep learning model is suggested, which applies a Convolutional Neural Network
(CNN) to estimate the level of individual income and provide specific product suggestions. In contrast to the
traditional tabular learners, our method converts normalized customer features to grayscale image matrices of size
20×10, allowing the CNN to learn the complex spatial features and latent behavioral patterns in the hybrid pooling
layers. The algorithm is implemented in two combined steps: high-granularity income tier categorization and a
recommendation engine that is powered by a purchase probability matrix. ThSe experimental findings using a dataset
of 980 people prove that the proposed model is much better than state-Sof-the-art benchmarks and has statistically
significant accuracy of 93.06 in income prediction and 95 in recommEendation success. These results highlight how
the use of spatial feature extraction can be more effective in conRsumer analytics and offer a scalable pipeline to e-
commerce real-time personalization. P
N
Keywords: Convolutional neural network, Income pIrediction, Buying habits, Product recommendation.
E
L
1. INTRODUCTION C
Customers are being prioritized in theI business and have emerged as the dominant factor. With this in mind, firms
T
must present customers with incentives in order to lessen the likelihood of them switching to competitors. A modest
R
unpleasant encounter with a client may indicate that the customer may churn [1]. Many e-commerce use cases rely
A
heavily on predicting future consumer behavior [2]. In other words, a company's customers are its lifeblood.
Customers are at the center of marketing efforts, and organizations frequently make poor decisions when they
ignore the behavior and motivations of their customers. Understanding the relationship between customer metrics
and profitability and company value is crucial as marketing aims to become more accountable. There are many
different types of customer metrics. It has been divided into two categories: perceptual and unobservable/behavioral
metrics. Observable measurements comprise consumer behaviors that are usually associated with the acquisition or
use of a good or service. Customer views (such as service quality), attitudes (such as customer satisfaction), and
behavioral intents (such as purchase intention) are instances of unobservable constructs [3].
Market basket analysis, according to Russell and Petersen [4], focuses on the mechanism by which customers
choose products from a certain set of groups within a single shopping trip. Its goal is to find relationships between
the selections of various products made in a certain retail establishment, like a supermarket. According to Wang
and Hong [5], shifts in consumer behavior lead to erratic customer profitability as well as wasteful and unproductive
marketing strategy. In order to accomplish their marketing objectives, the authors present a customer profitability
management system that makes use of data mining techniques. The development of the internet and e-commerce
has completely changed how consumers make purchases as well as how companies or brands promote to draw in
and keep customers by sending communications that are tailored to their individual needs [6].
The emergence of these e-commerce platforms has also made it more difficult for marketers and business owners
to manage their operations effectively. In order to enhance purchase revenue, e-commerce will rely entirely on
1

ACCAERPTTICEDLE M IANN PURSECSRSIPT
technology and experts who can create customized shopping experiences for potential customers [7]. Due to this
new trend's entire reliance on technology, there are numerous additional obstacles that must be overcome in order
to realize the benefits of this new framework. Personalized options, the internet, appropriate product presentation,
and many other aspects can all have an impact on the e-commerce business [8, 9].
It is crucial to predict income levels and comprehend the complex connection between income and purchasing
patterns since it has impacts on both the commercial and the private spheres. From the perspective of business, such
knowledge can be utilized for the improvement of marketing communication, for customization of products and
increasing customer satisfaction. Thus, the segmentation of the target market according to the income level is very
beneficial for the companies as it allows to invest more effectively and generate the highest possible revenues. On
the same note, for individuals, a better understanding of spending behavior can help in making more informed
decisions on their expenses and help in finding products and services that suit their needs and wants.
Moreover, the study of the correlation between purchasing behaviors and income also gives insights on consumers’
behaviors. It enables the business to target the right audience and market its products and services to the right
audience. For the researchers, the knowledge of this correlation can help to enhance the overall understanding of
the economic drivers affecting consumers’ decisions. It can also help to reveal information about tendencies of the
society and inequality in consumers’ behavior depending on income level.
Customer behavior analysis has been a process of identifying patterns in the dSata through techniques such as logistic
regression. However, identifying relationships between data and anSalyzing patterns become complex issues
E
especially when solving problems in large datasets. Convolutional Neural Networks (CNNs) are in fact a type of
R
Deep Learning (DL) that can be applied to solve this problem effectively. CNNs are good at feature extraction
P
which helps in their application for customer data analysis, and since customer data can be represented in the form
N
of multi-dimensional arrays.
I
While numerous methods exist for predictingE income and analyzing customer behavior, including traditional
L
machine learning algorithms [10-19] and sales prediction/product recommendation approaches [20-26], many of
C
these approaches suffer from limitations when dealing with the high dimensionality and complexity of modern
I
datasets. Traditional machine learTning methods together with basic neural networks face major challenges when
R
attempting to identify the complex interactions between different customer characteristics, their earned income and
A
purchase patterns. One of the greatest weaknesses of simple neural networks is that they cannot identify significant
latent features of customer data in multi-dimension, which is a compounding of the problems that other conventional
machine learning algorithms face with non-linear correlations between data. Basic neural networks demonstrate
their ineffectiveness when processing complex data according to multiple research studies [27]. Machine learning
Random forests show limitations when dealing with data sets that have very high dimensions [28]. The existing
techniques need improvement because they fail to manage complex data requirements effectively.
Despite the fact that DL approaches are increasingly used for the analysis of customer behavior, there are no studies
on the use of CNNs for the prediction of customers’ attributes and purchasing behavior. Previous works could
utilize a basic neural network architecture or other machine learning approaches besides deep learning. This study
explicitly fills this gap by showing how CNNs are distinctly able to rise above these constraints. Compared to the
traditional machine learning models and simple neural networks, which are not always able to capture complex
feature interactions, CNNs have a greater ability to process high-dimensional structured data. In particular, using
our proposed method, in which the standard one-dimensional demographic and behavioral data about customers
are converted into two-dimensional 20×10 feature matrices, the CNN will be able to extract complex spatial
correlations and latent patterns in a unique way [29]. This special spatial processing of tabular data enables the
network to isolate very small correlations that earlier algorithms fail to capture, thereby greatly improving our
accuracy in predicting income, and also making the results of our product recommendations very targeted.
2

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Recent advances in deep learning [30-32], have shown promising results in various domains. The following research
investigates the direct use of CNNs yet future work should consider integrating these approaches especially transfer
learning methods to enhance model functionality. The mentioned strategies enhance model generalization while
making it more resilient across different domains.
In our research, first, we endeavor to predict the income level using CNNs. Then, based on the projected income
level, we aim to derive a more accurate model of individuals' purchasing habits. This, in turn, enables us to provide
more precise recommendations. Our method not only predicts purchasing habits but also includes income level as
a factor that has a significant impact on those habits, which gives a better view of the customers. The key
contributions of the work are summed up as follows:
• Presenting a new architecture for CNN based on hybrid pooling layers for predicting people's income level.
• Presenting a probabilistic model for modeling the buying habits of customers and taking into account the
income level.
• Using the combination of individual characteristics and customer behavioral records in buying products to
form a recommender system.
The paper follows this progression: Similar works and backgrounds are examined in the second section. The
introduced technique is explained in the third section, and the results obtained from its implementation are presented
in the fourth section. Section 5 discusses the findings, implications, limitatSions and future works; and finally, the
S
fifth section includes the conclusions.
E
R
2. Background and Related Works
P
The current research includes two areas, one is predicting people's income level and the other is recommending
products. In this section, some recent researches have bNeen studied in each of these categories.
I
2.1. Predicting People's Income Levels
E
L
Yamnampet [10] focused on income dCetermination, using various classifiers to reduce cost and risk. It also
demonstrates the performance of eachI algorithm in customer identification and analyzes scored probabilities, scored
T
labels, false negatives, and true positives.
R
A
Thapa [11] evaluated the performance of five machine learning algorithms on an adult income dataset, revealing
the Random Forest Classifier as the most effective with 86.3% training and 86% test accuracy.
Chen et al. [12] proposed random forest (RF) as a method for predicting salaries, demonstrating its superiority over
traditional methods such as k-nearest neighbors, naive Bayes, logistic regression, and decision trees on the adult
dataset. RF enhances accuracy through dataset preprocessing, variance reduction, and factor elimination.
Viroonluecha and Kaewkiriya [13] aimed to develop a system for predicting salary in Thailand based on Deep
Learning, analyzing personal data from a job search website with over 1.7 million users. When compared to
algorithms like Random Forest and Gradient Boost Trees, the model achieved an optimal R-squared result of 0.462.
Kablaoui and Salman [14] utilized a dataset of over 20,000 salaries in the USA to apply three supervised machine
learning techniques: linear regression, random forest, and neural networks. It was found that the neural network
outperformed the other models, achieving an accuracy of 83.2%.
Wang et al. [15] analyzed the factors influencing college graduates' starting salaries using machine learning methods
at a 2020 financial university. The factors included academic qualifications, professional disciplines, employment
regions, industries, gender, and student cadres, with the XGBoost model emerging as the best predictor.
Vemulapati et al. [16] discussed income prediction methodologies using Long Short-Term Memory (LSTM),
ConvLSTM, Bi-Directional LSTM (BiLSTM), and Stacked LSTM networks. It highlighted pre-processing
3

ACCAERPTTICEDLE M IANN PURSECSRSIPT
approaches and training mechanisms, and demonstrated successful implementations. It was found that the BiLSTM
was more accurate.
Chakrabarty and Biswas [17] presented an Income Prediction Model using Grid Search on Adult Census Data,
Hyper-Parameter Tuning, Gradient Boosting, and Ensemble Learning, achieving a Validation Accuracy of 88.16%,
the highest ever.
Rehman et al. [18] proposed to demonstrate the use of data mining and machine learning strategies to address
income disparity issues. The study aimed to classify machine learning for predicting whether an individual has an
annual income.
Wang [19] utilized 48,842 income census data from the Adult Data Set to predict annual income levels using
machine learning approaches. Thirteen attributes, including native-country, occupation, marital status, education,
workclass, and age, were considered. A randomly divided 32,561 individuals were trained using various algorithms.
2.2. Sales Prediction and Product Recommendation
Xian et al. [20] explored the use of historical sales and behavioral data analytics to create a recommendation model
for online B2C businesses during the COVID-19 pandemic. They proposed a process model using RFM analysis,
k-means clustering, and association rule theory for shopping basket analysis and product recommendations. This
model improved sales, market responsiveness, and profitability for companiSes in similar situations.
S
Chaubey et al. [21] compared various machine learning techniquesE for predicting customer purchasing behavior.
R
They utilized supervised classification methods such as dummy classifier, XgBoost, AdaBoost, ANN, SGD,
P
random forest, SVM, Naïve Bayes, KNN, decision trees, and logistic regression. Additionally, they employed
hybrid methods like SvmAda, RfAda, and KnnSgd. TNhe best classification model was a hybrid method using an
ensemble stacking technique (KnnSgd), achieving anI accuracy of 92.42%.
E
Kumar et al. [22] introduced a new algorithLm for predicting customer interest that used pattern mining techniques
C
and Multi Variant K-means clustering. It identified user purchase histories, enquires, and purchase patterns,
I
generating recommendations for aTdvertisements and banner placement. This approach enhanced retail marketing
strategies and customer retentiRon.
A
Anitha and Patil [23] aimed to enhance business sales and profit by providing relevant and timely data on potential
customers in the retail industry. The data was analyzed using a systematic approach employing the K-Means
algorithm. The study used the Recency, Frequency and Monetary (RFM) model and dataset segmentation
principles, validating various dataset clusters based on the Silhouette Coefficient.
Nguyen et al. [24] created a customized recommendation system based on a multi-stage retrieval approach. Their
methodology is a combination of collaborative filtering, Bayesian Personalized Ranking (BPR) and popularity-
based algorithms to produce candidate items, which are ranked with LightGBM and Deep Neural Networks (DNN).
Parihar and Yadav [25] investigated the use of machine learning to predict customer behavior in e-commerce by
analyzing clickstream and customer data. Their goal was to use artificial intelligence to investigate output
discrepancies in models, with a focus on sequential clickstreams and static consumer data, in order to increase
customer loyalty and transactions.
Zhao and Keikhosrokiani [26] created a novel data science life-cycle and process model that uses RFM analysis
and other analytics algorithms to anticipate sales and recommend products. They used customer segmentation and
machine learning techniques to examine traditional shop business transformation. The prediction system, which
used XGBoost and Random Forest, was able to forecast consumer orders with 77.82% accuracy. The
recommendation system also used association rules to evaluate transaction statistics, revealing how online shopping
platforms promote products to customers.
4

ACCAERPTTICEDLE M IANN PURSECSRSIPT
In order to give a clear picture of the existing research field and point out the gaps in the methodology that this
study fills, Table 1 will present the summaries of the methodologies, goals, strengths, and limitations of the recent
literature in the field.
Table 1. Summary of the related studies
| Reference  | Year  | Methodology  | Goal  | Strengths               | Limitations            |
| ---------- | ----- | ------------ | ----- | ----------------------- | ---------------------- |
|            |       |              |       | Thorough evaluation of  | Relies on traditional  |
Income determination
Various Machine  scored probabilities and error  classifiers; may struggle with
| Yamnampet [10]  | 2017  |     | and customer  |     |     |
| --------------- | ----- | --- | ------------- | --- | --- |
Learning Classifiers  rates (false  highly complex, non-linear
identification.
|     |     |     |     | negatives/positives).     | data interactions.           |
| --- | --- | --- | --- | ------------------------- | ---------------------------- |
|     |     |     |     | Achieves strong baseline  | Basic ML architectures lack  |
ML Algorithms  Adult income  accuracy (86%) and provides  the ability to extract deep
| Thapa [11]  | 2023  |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- |
(Random Forest, etc.)  prediction.  a broad algorithm  spatial/latent features from
|                   |                           |     |                           | comparison.                     | datasets.                     |
| ----------------- | ------------------------- | --- | ------------------------- | ------------------------------- | ----------------------------- |
|                   |                           |     |                           | Enhances accuracy via           | Tree-based models can be      |
|                   |                           |     | Salary prediction on the  | rigorous preprocessing,         | limited when scaling to very  |
| Chen et al. [12]  | 2022  Random Forest (RF)  |     |                           |                                 |                               |
|                   |                           |     | adult dataset.            | variance reduction, and factor  | high-dimensional behavioral   |
elimination.  data.
S
R-squared value of 0.462
|     |     |     | Salary prediction for  | Utilizes aS massive real-world  |     |
| --- | --- | --- | ---------------------- | ------------------------------- | --- |
Viroonluecha &  Deep Learning vs. RF,  indicates a significant portion
|     | 2018  |     | Thailand labor  | datEaset (1.7M users); DL  |     |
| --- | ----- | --- | --------------- | -------------------------- | --- |
Kaewkiriya [13]  Gradient Boosting  of data variance remains
|     |     |     | workforce.  | Routperformed traditional ML.  |     |
| --- | --- | --- | ----------- | ------------------------------ | --- |
unexplained.
P
|     |     |     |  Demonstrates the superiority  |     | Basic NNs are less effective  |
| --- | --- | --- | ------------------------------ | --- | ----------------------------- |
N
Kablaoui &  Neural Networks,  Salary prediction on a  of basic neural networks  than CNNs at capturing
|     | 2022  |     | I   |     |     |
| --- | ----- | --- | --- | --- | --- |
Salman [14]  Linear Regression, RF  USA dataset.    (83.2% accuracy) over  spatial relationships in
|     |     |     | E   | traditional ML.  | structured data.  |
| --- | --- | --- | --- | ---------------- | ----------------- |
L
|     |     |     | C   |     | Highly domain-specific  |
| --- | --- | --- | --- | --- | ----------------------- |
High interpretability of
|                   |       | I         | Predict starting salary  |                           | (financial university  |
| ----------------- | ----- | --------- | ------------------------ | ------------------------- | ---------------------- |
| Wang et al. [15]  | 2022  | XGBoTost  |                          | demographic and academic  |                        |
|                   |       |           | of college graduates.    |                           | graduates); limited    |
influencing factors.
R
generalizability.
A
High computational
LSTM, ConvLSTM,  Effectively captures  complexity; RNN/LSTMs are
Vemulapati et al.
2023  BiLSTM, Stacked  Income prediction.  sequential data; BiLSTM  less optimized for non-
[16]
|     |     | LSTM  |     | showed high accuracy.  | sequential spatial data than  |
| --- | --- | ----- | --- | ---------------------- | ----------------------------- |
CNNs.
Achieves high validation
|     |     | Gradient Boosting,  |     |     | Reliance on traditional tabular  |
| --- | --- | ------------------- | --- | --- | -------------------------------- |
Chakrabarty &  Adult census income  accuracy (88.16%) through
|              | 2018  | Ensemble Learning,  |                    |                          | ML limits deeper feature  |
| ------------ | ----- | ------------------- | ------------------ | ------------------------ | ------------------------- |
| Biswas [17]  |       |                     | level prediction.  | rigorous hyperparameter  |                           |
|              |       | Grid Search         |                    |                          | extraction capabilities.  |
tuning.
Focuses on binary/simple
|     |     |     | Classify existence of  | Strong socio-economic  |     |
| --- | --- | --- | ---------------------- | ---------------------- | --- |
Rehman et al.  Data Mining, Machine  classification rather than
|       | 2022  |           | annual income to    | application and focus on  |                       |
| ----- | ----- | --------- | ------------------- | ------------------------- | --------------------- |
| [18]  |       | Learning  |                     |                           | granular income tier  |
|       |       |           | address disparity.  | income inequality.        |                       |
prediction.
|     |     |     | Predict annual income  | Comprehensive feature  | Constrained by the limitations  |
| --- | --- | --- | ---------------------- | ---------------------- | ------------------------------- |
Various Machine
Wang [19]  2022  levels based on 13  importance analysis on a  of traditional ML in modeling
Learning Approaches
|     |     |     | attributes.  | standard dataset.  | complex behavioral matrices.  |
| --- | --- | --- | ------------ | ------------------ | ----------------------------- |
5

ACCAERPTTICEDLE M IANN PURSECSRSIPT
| Reference  | Year  |     | Methodology  |     |     | Goal  |     | Strengths  |     | Limitations  |
| ---------- | ----- | --- | ------------ | --- | --- | ----- | --- | ---------- | --- | ------------ |
Static clustering approaches
|     |     |     | RFM Analysis, K- |     |     | B2C product  | Direct real-world business  |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | ------------ | --------------------------- | --- | --- | --- |
may fail to adapt to rapid,
Xian et al. [20]  2022  means, Association  recommendation during  applicability; improves
dynamic shifts in user
|     |     |     | Rules  |     |     | COVID-19.  | market responsiveness.  |     |     |     |
| --- | --- | --- | ------ | --- | --- | ---------- | ----------------------- | --- | --- | --- |
behavior.
Complex hybrid ensembles
|                 |       |     | ML & Hybrid       |     |                       |                   | High accuracy (92.42%)         |     |                           |                         |
| --------------- | ----- | --- | ----------------- | --- | --------------------- | ----------------- | ------------------------------ | --- | ------------------------- | ----------------------- |
| Chaubey et al.  |       |     |                   |     |                       | Predict customer  |                                |     |                           | can be computationally  |
|                 | 2023  |     | Ensembles (e.g.,  |     |                       |                   | achieved through advanced      |     |                           |                         |
| [21]            |       |     |                   |     | purchasing behavior.  |                   |                                |     | expensive and lack model  |                         |
|                 |       |     | KnnSgd)           |     |                       |                   | ensemble stacking techniques.  |     |                           |                         |
interpretability.
Clustering-based
|     |     |                        |     |     |     | Customer interest  | Effectively uses purchase  |     |                               |     |
| --- | --- | ---------------------- | --- | --- | --- | ------------------ | -------------------------- | --- | ----------------------------- | --- |
|     |     | Pattern Mining, Multi  |     |     |     |                    |                            |     | recommendations often suffer  |     |
Kumar et al. [22]  2021  prediction and ad  histories to optimize retail
|     |     |     | Variant K-means  |     |     |                  |     |                        | from the "cold-start" problem  |     |
| --- | --- | --- | ---------------- | --- | --- | ---------------- | --- | ---------------------- | ------------------------------ | --- |
|     |     |     |                  |     |     | recommendation.  |     | marketing strategies.  |                                |     |
for new customers.
K-Means assumes spherical
Systematic validation of data
Anitha & Patil  Enhance retail sales via  data clusters, which may not
|       | 2022  | K-Means, RFM Model  |     |     |                         |     | clusters using the Silhouette  |     |                               |     |
| ----- | ----- | ------------------- | --- | --- | ----------------------- | --- | ------------------------------ | --- | ----------------------------- | --- |
| [23]  |       |                     |     |     | customer segmentation.  |     |                                |     | accurately represent complex  |     |
Coefficient.
human behavior.
Performance highly
|     |     |                          |     |     |     | Improve user  | Successfully combines  |     |                                |     |
| --- | --- | ------------------------ | --- | --- | --- | ------------- | ---------------------- | --- | ------------------------------ | --- |
|     |     | Retrieval Strategy (CF,  |     |     |     |               |                        | S   | dependent on the retrieval of  |     |
Nguyen et al.  engagement via  multiple algorithms to handle
|       | 2024  |     | BPR) +        |     |                       |                   |                                | S                 | candidates; DNN components  |     |
| ----- | ----- | --- | ------------- | --- | --------------------- | ----------------- | ------------------------------ | ----------------- | --------------------------- | --- |
| [24]  |       |     |               |     | personalized product  |                   | large-scale data and the cold- |                   |                             |     |
|       |       |     | LightGBM/DNN  |     |                       |                   |                                |                   | showed lower MAP@K          |     |
|       |       |     |               |     |                       | recommendations.  |                                | E start problem.  |                             |     |
compared to boosted trees.
R
P
Output discrepancies require
 Successfully integrates both
Parihar & Yadav  Predict consuNmer future  manual AI investigation,
|       | 2021  |     | Machine Learning  |     |     |                | sequential clickstream data   |     |     |                      |
| ----- | ----- | --- | ----------------- | --- | --- | -------------- | ----------------------------- | --- | --- | -------------------- |
| [25]  |       |     |                   |     |     | prefeIrences.  |                               |     |     | limiting end-to-end  |
|       |       |     |                   |     |     |                | and static demographic data.  |     |     |                      |
automation.
E
L
|                 |       |     |               |     |                        |          | Provides a holistic life-cycle  |     | Accuracy of 77.82% suggests  |                       |
| --------------- | ----- | --- | ------------- | --- | ---------------------- | -------- | ------------------------------- | --- | ---------------------------- | --------------------- |
| Zhao &          |       |     |               |     | CSales prediction and  |          |                                 |     |                              |                       |
|                 |       |     | XGBoost, RF,  |     |                        |          | model combining both            |     |                              | significant room for  |
| Keikhosrokiani  | 2022  |     |               | I   |                        | product  |                                 |     |                              |                       |
Association RTules, RFM  prediction and  improvement via deep
| [26]  |     |     |     |     |     | recommendation.  |                         |     |                               |     |
| ----- | --- | --- | --- | --- | --- | ---------------- | ----------------------- | --- | ----------------------------- | --- |
|       |     |     |     |     |     |                  | recommendation phases.  |     | learning feature extraction.  |     |
R
A

2.3. CNNs with Hybrid Pooling
CNN models, despite their high efficiency in pattern learning, require a large training set. For small training sets,
CNNs may face the problem of overfitting [33]. Overfitting reduces the generalizability of the CNN when applied
to new instances. In many situations, the overfitting problem in CNNs can be attributed to the function used in the
pooling layers, based on which one can obtain the feature map extracted from the data through the activations output
of the convolutional layers [34]. In CNN designs today, two pooling algorithms are frequently utilized. The first
function is called max pooling, and it takes each feature map region's maximum activation value. This allows for
the extraction of the most prominent features and the elimination of less significant ones.  In real-world applications,
this function causes overfitting [35].
Average pooling, the second operator, takes into account the results for a region in equal measure. The ReLU
activation  and  average  pooling  operator  work  together  to  lessen  the  impact  of  strong  activations  while
simultaneously producing a significant amount of zeros in the feature map. However, when average pooling is
combined with other activation operators—like the hyperbolic tangent function—it may cause loss of data by
ignoring positive as well as negative activations. In light of these drawbacks, numerous research have introduced
novel pooling techniques in an effort to reduce the overfitting issue in CNNs.  Hybrid pooling [36] can be an
6

ACCAERPTTICEDLE M IANN PURSECSRSIPT
efficient solution. It combines the benefits of both max pooling and average pooling, thereby improving the
generalizability of CNNs.
This strategy seeks to boost the adaptability of the CNN model by leveraging diverse pooling strategies during
training and averaging their predictions at test time. During training, each feature map in the convolution layer
undergoes both average pooling and max pooling. The choice between them is randomized, governed by a
probability (p) for average pooling and (1-p) for max pooling. This approach, as described in [36], essentially blends
the benefits of both pooling methods, aiming to achieve superior generalizability compared to relying on a single
strategy. This mechanism can be formulated as follows [36]:
| 𝑆   |                   𝑤𝑖𝑡ℎ 𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦 𝑝 |     |     |     |     |     |     |
| --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
𝑎𝑣𝑔
| 𝑆 = { |                               |     |     |     |     |     | )1)  |
| ----- | ----------------------------- | --- | --- | --- | --- | --- | ---- |
| 𝑆     |          𝑤𝑖𝑡ℎ 𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦 1−𝑝 |     |     |     |     |     |      |
𝑚𝑎𝑥
Where 𝑆  is the output of average pooling operator for various regions and is defined by the set 𝑆 =
𝑎𝑣𝑔 𝑎𝑣𝑔
𝐽
{𝑠1 ,…,𝑠 }. The following relationship holds for each member of this set:
| 𝑎𝑣𝑔 | 𝑎𝑣𝑔 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
1
| 𝑠 𝑗 = | ∑    | 𝑎   |     |     |     |     |  (2)  |
| ----- | ---- | --- | --- | --- | --- | --- | ----- |
| 𝑎𝑣𝑔   | 𝑖∈𝑅𝑗 | 𝑖   |     |     |     |     |       |
|𝑅𝑗|
where, 𝑅    shows the jth pooling segment, which includes a group of activatSions such as {𝑎 ,…𝑎 }. On the other
|     | 𝑗   |     |     |     |     |     | 1 |𝑅𝑗| |
| --- | --- | --- | --- | --- | --- | --- | ------ |
S
hand, in eq. (1), 𝑆    refers to the output of max pooling operator for various segments and is defined by the set
𝑚𝑎𝑥
|     |     | 𝐽   |     |     |     | E   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
𝑆 = {𝑠1 ,…,𝑠 }. For each member of this set, the following relationship holds:
| 𝑚𝑎𝑥 | 𝑚𝑎𝑥 | 𝑚𝑎𝑥 |     |     |     | R   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
P
| 𝑗   |      |     |     |     |     |     |      |
| --- | ---- | --- | --- | --- | --- | --- | ---- |
| 𝑠 = | max𝑎 |     |     |     | N   |     | (3)  |
| 𝑚𝑎𝑥 | 𝑖    |     |     |     |     |     |      |
𝑖∈𝑅𝑗
I

E
Then, in the test phase, the result of any pooling area is measured using eq. (4) [36]:
L
C
| 𝑆 = 𝑆  | =   | 𝑝×𝑆 +(1−𝑝)×I𝑆 |      |     |     |     |  (4)  |
| ------ | --- | ------------- | ---- | --- | --- | --- | ----- |
| ℎ𝑦𝑏𝑟𝑖𝑑 |     | 𝑎𝑣𝑔           | T𝑚𝑎𝑥 |     |     |     |       |
R
This approach seeks to enhance CNN model diversity by strategically combining two distinct pooling operators for
A
various feature maps.

3. Research Methodology
This section provides a detailed description of the data collection process. It also outlines the steps of the proposed
method for predicting customer purchasing habits. This method leverages deep learning techniques.
3.1. Data
The data used in this research was collected through a comprehensive questionnaire, which was meticulously
designed to capture a wide range of variables. The gathered information through each questionnaire from
participants include demographics, shopping habits, income level, and product preferences of the participants. The
used questionnaire and response options have been presented in Appendix A.  This questionnaire was distributed
among 980 individuals, ensuring a diverse sample in terms of age, gender, and income levels. The 980 participants
are well balanced in terms of demography: 48 of them were males and 52 of them were females. Age categories
were divided into five with the highest proportion of 25-34 (31.10 %) and 35-44 (27.56%) representing the largest
proportion of the workforce consumers. Geographically, respondents were mostly located in a wide range of urban
and suburban areas to capture a wide range of retail accessibility and economic conditions. The responses were then
organized into a structured dataset for further analysis. This dataset includes detailed information about the
purchasing habits of individuals across six different categories of goods.
The categorization of goods in this study includes mobile phones, tablets, laptops, clothing, entertainment items,
and food. For each category, a set of brands available at the data collection site was identified, and respondents
7

ACCAERPTTICEDLE M IANN PURSECSRSIPT
were asked to indicate their preferences. In addition to the information on people’s purchasing habits, a table was
created to describe the characteristics and behavior of each individual. Table 2 provides a comprehensive overview
of the collected information for each individual in this dataset.

Table 2. List of descriptive information for each individual.
| Row  Feature             |     | Type     |
| ------------------------ | --- | -------- |
| 1  Gender                |     | Nominal  |
| 2  Marital Status        |     | Nominal  |
| 3  Age                   |     | Numeric  |
| 4  Education Level       |     | Ordinal  |
| 5  Job Category          |     | Nominal  |
| 6  Job History           |     | Numeric  |
| 7  Place of Residence    |     | Nominal  |
| 8  Residential Status    |     | Ordinal  |
| 9  Specific Disease      |     | Nominal  |
| 10  Alcohol Consumption  |     | Nominal  |
11  Consumption of Tobacco or Other Addictive Substances  Nominal
12  Number of In-person Shopping Instances per Week  Numeric
| 13  Number of Online Shopping Instances per Week  |     | Numeric  |
| ------------------------------------------------- | --- | -------- |
| 14  Quantity of cart during In-person Shopping    |     | Numeric  |
| 15  Quantity of cart during Online Shopping       | S   | Numeric  |
S
| 16  Number of Working Hours per Week  |     | Numeric  |
| ------------------------------------- | --- | -------- |
| -  Income Level                       | E   | Numeric  |
R
Based on the input information for the income level feature, rPespondents are divided into five categories of income

levels: very low (164 samples), low (178 samples), average (208 samples), high (193 samples), and very high (237  N
samples). The goal of the proposed method is to predict individuals’ income levels based on the independent
I
features listed in Table 2. Then, modeling the purc hasing habits based on the determined income levels.
E
L
Although the data used in this study hCas a solid basis, some weaknesses in the data collection process can be
identified. The use of a questionnaireI opens the possibility of self-reporting bias especially on sensitive variables
like precise income or shopping frequency. Moreover, the sampling was also geographically limited to certain areas,  T
R
which can affect the extrapolation of the buying patterns to other cultural or rural settings. These were alleviated
A
by careful design of the questionnaire and the weighted cross- entropy loss function to make the model resilient to
different samples.

3.2. Proposed Method
It seems that a person’s habits and preferences during shopping are related to their behavioral characteristics and
income level. Therefore, this research attempts to model people’s shopping habits based on the information obtained
from their income classification. The proposed method models customer behavior and recommends goods in three
steps:
1.  Preprocessing,
2.  Classification of individuals based on income
3.  Product recommendation based on income.
The structure of the presented approach is illustrated in Figure 1. First, the collected information from individuals
(Table 2) is normalized and transformed so that it can be processed by learning models. Then, in the second step,
the individual’s features are processed by a CNN, and their income level is predicted to determine the target
category for the individual based on the predicted value.
8

In the third step of the presented approach, a suitable product is recommended based on the predicted income level.
At this stage, a purchase probability matrix is utilized to model people’s shopping habits based on their income
level. This matrix, which has a number of rows equal to the number of recommended categories for goods and a
number of columns equal to the number of income groups, models the probability of purchasing a product in a
specific category by individuals in different income groups.
As illustrated in Figure 1, the data collected via the questionnaire is divided into two categories: training data and
test data. The dataset instances are permuted randomly and then partitioned into subsets using the cross-validation
approach (as explained in section IV) to determine the training and test sets. Initially, in the training phase, the
purchasing habits model, denoted as P, is formed based on the purchase histories and preferences of training
instances. Then, for each sample belonging to the test set, they are first classified based on their income level using
the CNN model. Based on the predicted income and the probability matrix P, a product is recommended to the
individual.
Figure 1. Structure of the presented approach.
3.2.1 Preprocessing
The proposed method utilizes a straightforward mechanism for preprocessing the data, which encompasses three
sub-steps: ‘value conversion’, ‘missing value management’, and ‘feature normalization’. The preprocessing begins
with the conversion of nominal values into numerical ones. In this process, each value in the nominal features
is converted into a natural number. For ordinal nominal features, a unique list is compiled based on the rank of the
values present in that feature. Subsequently, a value like IX is assigned to each value in the sorted list, proportional
to its position. This approach ensures a streamlined and effective preprocessing of the data. For non-ordinal nominal
features, a list of unique values is created based on the frequency of each nominal value. Ultimately, each value in
the mentioned feature is replaced with a natural number corresponding to it in the IX set. By executing the above
process, all features of the dataset are converted into a numerical format.
9
2
C la
T e s t In s ta n c e s
s s ify u s in g C N N w
h y b r id p o o lin g
R e c o m m e n d a tio n
P
ith
r e
D
-p
a ta
r o c
s e t
e s s in g
C o n
T r a in In s ta n c e s
s tr u c t B u y in g H
M o d e l ( P )
P
a b its
1
ACCAERPTTICEDLE M IANN PURSECSRSIPT
S
S
E
R
P
N
I
E
L
C
I
T
R
A

ACCAERPTTICEDLE M IANN PURSECSRSIPT
The choice of this particular numerical mapping, as opposed to more traditional numerical encoding methods,
including direct one-hot encoding or target encoding, is specifically meant to be compatible with the high-
dimensional feature-to-image mapping in Section 3.2.2. Although standard encoding works well with more
traditional tabular learners, it usually creates sparse vectors which do not provide the structure density needed by
convolutional filters. In our design, this preliminary mapping will give a standardized number base that will enable
all the features to be divided into 100 fine-grained intervals. This generates the 1600-bit binary representation that
is required to make a complete 20×10 grayscale image. Through the use of this approach instead of traditional
approaches, we are able to have the CNN perceive demographic and behavioral characteristics as geometrical
patterns, and the model is able to identify deep, non-linear relationships between disparate characteristics that would
have been missed by standard encoding schemes.
Subsequently, records with missing values are corrected. For this purpose, if a feature with a missing value in a
record is numerical, it is replaced with the mean of the existing values for that feature. Conversely, for nominal
features with missing values, the missing value is replaced with the mode or the value with the highest frequency
for that feature.
The preprocessing step concludes with feature normalization. During this process, the value vector of each feature,
denoted as x, is mapped to the range [0,1] using eq. (5).
𝑁 =
𝑥−𝑥𝑚𝑖𝑛 S
(5)
𝑥
𝑥𝑚𝑎𝑥−𝑥𝑚𝑖𝑛 S
E
Where 𝑥 and 𝑥 respectively describe the smallest and laRrgest values for feature (x).
𝑚𝑖𝑛 𝑚𝑎𝑥
P
3.2.2 Classification of Individuals Based on Income NUsing CNN
I
In this step, a CNN with hybrid pooling layers Eis employed to classify individuals based on their income level. For
this purpose, a matrix representation of the sLet of normalized features obtained from the previous step is used. The
C
process of converting tabular customer data to a format that can be processed by convolutional processing consists
I
of four steps of discretization and Tmapping:
R
1. Interval Mapping:A Each normalized feature 𝑥 ∈ [0,1] is mapped to one of 100 equal intervals of length
0.01.
2. High-Dimensional Encoding: Using one-hot encoding, each interval is converted into a binary string of
length 100. As an example, a value between [0.01, 0.02) will give a 1 at the second position and 0 at other
positions.
3. Bit-Stream Aggregation: With each record being represented by a high-dimensional bit-stream of 1600 bits
(16×100), all 16 features are concatenated to generate a bit-stream.
4. Spatial Grayscale Mapping: This bit-stream is divided into blocks of 8 bits with each block being mapped
to a single pixel intensity (0-255). The pixels are then reformed into a 20×10 grayscale image matrix.
This organized representation enables the CNN to process customer profiles as spatial patterns to enable the latent
feature correlations that are usually misplaced in traditional vector-based models to be identified. The obtained
matrix is fed to a CNN classifier. The CNN model uses this input to predict the individual’s income level.
The reason for selecting CNNs for this research is their ability to efficiently handle large, structured data, such as
the matrix representation of individual characteristics employed in our study. Their hierarchical organization,
incapacity for translation, and abilities in parallel processing qualify them for activities that involve pattern
recognition and classification in such data. When compared with additional deep learning methods like Recurrent
Neural Networks (RNNs) or LSTMs, CNNs can deliver higher performance in tasks dedicated to spatial relations
and high-dimensional data. In contrast, RNNs and LSTMs are mainly created for sequential data, in which the
10

ACCAERPTTICEDLE M IANN PURSECSRSIPT
arrangement of elements is important. Though they can comply with the data organization detailed in this study,
they may not be as efficient as CNNs in capturing spatial features.
In order to increase the generalization capabilities of the model on small and imbalanced data, we apply the Hybrid
Pooling strategy described in Section 2.3. This mechanism contrasts with max and average pooling by switching
between max and average pooling stochastically during training unlike in the case of static pooling. This helps the
model to avoid over-fitting to the most salient activations (which is one of the main causes of overfitting in customer
behavior data) and to make sure that the feature maps do not lose the subtle behavioral indicators. Figure 2 shows
the particular arrangement of these layers into our architecture.
|     |     | In p u t (1 | 0 × 2 0 × 1 | )  C o | n v o lu tio | n  (6 × 6 × 1   | 6 )  |     | F u lly     |           | S o      | ftM a x      |     |
| --- | --- | ----------- | ----------- | ------ | ------------ | --------------- | ---- | --- | ----------- | --------- | -------- | ------------ | --- |
|     |     |             |             |        | R e          | L U             |      |     |             |           |          |              |     |
|     |     |             |             |        |              |                 |      |     | C o n n(5 e | c te  d   | C la s s | ific a tio n |     |
|     |     |             |             | H      | y b rid  P o | o lin g  (2 × 2 | )    |     |             |           |          |              |     |
|     |     |             |             |        |              |                 |      |     | 0           | )         |          |              |     |
S
S
E
|     |     |     |     |     |     | C   | o n v o lu tio | n  (3 × 3 × 2 | 4 )   | F u lly |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | ----- | ------- | --- | --- | --- |
R
|     |     |     |     |     |     |     | R e          | L U           |     | C o n n e | c te d   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | --------- | -------- | --- | --- |
|     |     |     |     |     |     |     |              | P             |     |           |          |     |     |
|     |     |     |     |     |     | H   | y b rid  P o | o lin g  (2 × | 2 ) | (5 )      |          |     |     |

N
I

|     |     |     |     |        |     |     |     |     |     | F u lly  C | o n n e c te | d   |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | ---------- | ------------ | --- | --- |
|     |     |     |     | In p u | t   | E   | R e | L U |     |            |              |     |     |
L
|     |     |     |     | C o n | v o lu tio n |     | H y | b rid  P o o lin | g   | S o ftM | a x  C la s s | ifie r   |     |
| --- | --- | --- | --- | ----- | ------------ | --- | --- | ---------------- | --- | ------- | ------------- | -------- | --- |
C

|     |     |     |     | I   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T
R
Figure 2. The proposed CNN model for predicting individuals’ income levels.
A
Another major issue with income prediction is the imbalance in classes (164 very low vs. 237 very high samples).
In order to solve this without losing useful data, we use a Weighted Cross-Entropy (WCE) loss function. The
technical explanation behind WCE is to impose a penalty weight 𝑤  on each of the classes inversely proportional
𝑖
to its frequency in the training set. This compels the gradient descent algorithm to make decisions that are more
focused on the proper classification of minority groups, which practically eliminates the majority bias that is usually
rife with conventional CNNs. The WCE loss is mathematically formulated as:
| 𝐿𝑜𝑠𝑠  = −𝛴(𝑤 |     | ∗ 𝑦 ∗log(𝑝 | )+ (1−𝑦 |     | )∗log(1−𝑝 |     | ))  |     |     |     |     |     | (6)  |
| ------------ | --- | ---------- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | ---- |
|              | 𝑖   | 𝑖          | 𝑖       |     | 𝑖         |     | 𝑖   |     |     |     |     |     |      |
In Eq. (6), 𝑤  is the weight of the class i and for this class its true label is 𝑦 . Furthermore, 𝑝  is the probability that
|     | 𝑖   |     |     |     |     |     |     |     |     | 𝑖   |     | 𝑖   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is being predicted for the class i.
The careful tuning of hyperparameters is essential to optimize the performance of CNN models. The optimal hyper
parameter setting for the employed CNN structure was obtained using the grid search strategy. In this regard,
various hyper parameter settings of the CNN were examined using the training loss metric. The examined hyper
parameters for tuning the model include the dimensions and number of convolutional filters, dimensions of the
pooling layers, and also type of activation layers. Additionally, various settings for training-related parameters of
mini batch size and optimizer were considered in the tuning step. Table 3 shows the search space for each
configurable parameter of the CNN in this research.
11

ACCAERPTTICEDLE M IANN PURSECSRSIPT
The best obtained configuration of the CNN has been presented in Fig. 2. The inputs of the introduced CNN are
defined as the matrix that described at the beginning of this section. This CNN comprises two layers of convolution
with 16 and 24 filters, respectively. The width and length of these layers are 6×6 and 3×3, respectively. The output
of each of these layers are processed through the ReLU activation function, and feature map extraction at each stage
is performed by hybrid pooling with dimensions of 2×2. For both convolution and pooling layers, the stride was
considered as 1. Finally, two consecutive fully connected layers are utilized to extract features. The first one
transforms the extracted features into a vector form. The second fully connected layer calculates the probability of
the sample belonging to each of the target categories. This is done by outputting a posterior probability vector.
Ultimately, these features are classified by a SoftMax layer to predict the income level for the sample based on it.
Table 3. the search space for each configurable CNN parameter
| CNN parameter                    |     |                          | Search space     |
| -------------------------------- | --- | ------------------------ | ---------------- |
| Dimension of convolution layers  |     |                          | {2, 3, 5, 7, 9}  |
| Number of convolution filters    |     | {4, 8, 16, 24, 32, 48}   |                  |
| Dimension of pooling layers      |     |                          | {2, 3, 4, 5}     |
| Activation function              |     | ReLU, PReLU, Leaky ReLU  |                  |
| Optimizer                        |     |                          | SGDM, Adam       |
| Mini batch size                  |     |                          | {16, 32, 64}     |

   S
S
3.2.3 Modeling Shopping Habits and Recommending Goods BasEed on Income
R
P
After employing the proposed CNN model for classifying individuals based on their income level, a matrix is used

to model people’s shopping habits and offer suggestioNns to them based on the created model. This matrix shows
which goods people with different incomes are moreI likely to buy and which category of goods they are less likely

to purchase. The structure of the probability maEtrix used in the proposed method is shown in Figure 3.
L

C
IK columns, each of which corresponds to an
T
 income category of the individuals
R
A
 a
 o
t
 s
| d   |  P  P   | P  … |  P  |
| --- | ------- | ---- | --- |
| n   | 1,1 1,2 | 1,3  | 1,K |
o
ps
d
| s o |  P  P   | P  … |  P  |
| --- | ------- | ---- | --- |
| e   | 2,1 2,2 | 2,3  | 2,K |
r r o
og
c e
 hh
| t    |  P  P   | P  … |  P  |
| ---- | ------- | ---- | --- |
| c  f | 3,1 3,2 | 3,3  | 3,K |
i ho
w y
|  f r |  …  … | … P |  …  |
| ---- | ----- | --- | --- |
| o o  |       |     | i,j |
g
 h e
c t
a a
| e c |  P  P   | P  … |  P  |
| --- | ------- | ---- | --- |
|  ,  | N,1 N,2 | N,3  | N,K |
s
w
o
r
N
Probability of buying the product in category (i) by
the individual with income category of (j)

Figure 3. The structure of the probability matrix for modeling shopping habits and recommending goods to
individuals in the proposed method.
12

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Referring to Figure 3, the depicted matrix is structured with its rows equivalent to the recommendable goods and
its columns corresponding to the distinct income groups. Consequently, this probability matrix is characterized by
N rows and K columns. Each matrix element specifies the probability that an individual, belonging to the income
group represented by the current column, will purchase the goods associated with the current row category. In
essence, P in Figure 3 represents the probability of an individual from income category j purchasing a good from
i,j
category i. During the data collection phase, each participant provided personal information and responded to
queries about their purchasing habits for various goods. Consequently, each individual’s purchase record can be
denoted as <N,K>, where N signifies the category of goods that the individual purchased, and K designates the
i i i i
income group to which the individual belongs. Therefore, the database can be structured as depicted in Table 4, for
each category of recommended goods.
Table 4. Data structure for storing individuals’ shopping habits in the proposed method.
Row Income Group Purchased Goods Category
1 K1 N1
2 K2 N2
… … …
X KX NX
In Table 4, X denotes the number of records in the database. To calculate the probability matrix presented in the
proposed method, first, the total selection of each category of goods by each income group of individuals is
S
calculated as follows:
S
E
𝑀 = |{<𝑁 ,𝐾 >|𝑁 = 𝑖 𝑎𝑛𝑑 𝐾 = 𝑗}| (7)
𝑖,𝑗 𝑐 𝑐 𝑐 𝑐 R
P
N
Where 1 ≤ 𝑐 ≤ 𝑋 is the counter for the database records. In the above relation, the number of records where an
individual in category j has chosen a good in categoIry i is counted. After calculating the matrix M, each element
located in the matrix M is divided by the sum oEf the elements of the column related to that element.
L
C
𝑃 =
𝑀𝑖,𝑗
I (8)
𝑖,𝑗 ∑𝑁
𝑘=1
𝑀𝑘,𝑗 T
R
A
By applying the above relation to each element of matrix M, the probability matrix P is obtained, which indicates
the probability of different groups of individuals choosing different categories of goods. After forming the matrix
P, the act of suggesting goods to individuals can be performed. For this purpose, after receiving the personal
information of each person, the classification operation is first performed using the CNN model. In the next step, if
the individual is classified into class (j), the good with the highest probability in the (j)-th column of the matrix (P)
is suggested to the individual.
4. Research Finding
The proposed approach was implemented and evaluated using MATLAB 2020. We reviewed the presented
approach in two scenarios: in the first scenario, we predict people's income level, and in the second phase, based
on the model that was considered to predict people's buying habits, we make recommendations.
In this study, stratified 5-fold cross-validation (CV) was utilized for the proposed method. First, we permuted the
dataset instances randomly and then, divided the data into 5 parts and each part made up 20% of the data set. Then
we repeated the operation 5 times. During each repetition, 80% of the data was used for training (based on 70% of
instances) and validating (based on 10% of the instances) the model. After training the model, the remaining 20%
unseen data is used as test data, and the classification result for each test sample is compared with its ground-truth
label, leading to the one of the following conditions:
• True Positive (TP): The quantity of positive cases accurately detected by the model.
13

ACCAERPTTICEDLE M IANN PURSECSRSIPT
• False Negative (FN): The quantity of cases that the model incorrectly identified as negatives.
• False Positive (FP): The quantity of samples in which the model incorrectly classified as positive.
• True Negative (TN): The quantity of samples in which the model properly detected a negative.
Accuracy represents the overall proportion of correct predictions made by a model. Mathematically, this can be
expressed as:
𝑇𝑃+𝑇𝑁
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 = 100× (9)
𝑇𝑃+𝐹𝑃+𝑇𝑁+𝐹𝑁
Prioritizing true positives, precision measures the percentage of genuine positives among all model-predicted
positives. Crucial for minimizing false positives. Mathematically:
𝑇𝑃
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 = (10)
𝑇𝑃+𝐹𝑃
Focusing on completeness, recall measures the percentage of true positives accurately identified out of all actual
positive instances. Crucial for avoiding missed positives. Mathematically:
𝑇𝑃
𝑅𝑒𝑐𝑎𝑙𝑙 = (11)
𝐹𝑁+𝑇𝑃
F-Measure provides a balanced assessment of both precision and recall. It is often employed when both metrics
S
hold equal importance. Mathematically:
S
2∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙 E
𝐹−𝑀𝑒𝑎𝑠𝑢𝑟𝑒 = (12)
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙 R
P
4.1. Evaluation in terms of Predicting People's Income Level
N
We evaluated the proposed method in this phase baseId on individuals' income. This method was assessed using the
criteria of f-measure, recall, precision, and accuEracy, and we compared it to other methods.
L
We evaluated the recommended methodC in three different modes: the proposed method, CNN (Max.pool), and CNN
(Avg.pool). Due to the use of hybriId pooling layers that combines average and maximum pooling layers, we
T
compared our proposed CNN Rmodel with two other CNN models that only use max pooling and average pooling
layers. Also, we comparedA our proposed method with references [17-19], which we named Chakrabarty & Biswas,
Rehman et al and Wang respectively.
Figure 4 shows the average accuracy, precision, recall, and f-measure graphically. In Figure 4a, our method
demonstrates superior performance in predicting individual income levels, exceeding both the CNN (Max.pool)
and Wang methods in average accuracy by margins of 1.5% and 2.7% respectively. This clearly indicates the
improved accuracy of our method .In Figure 4b, our method outperforms the CNN (Max.pool) and Wang methods
in precision by 1.5% and 2.6% respectively, indicating fewer false positive predictions and higher precision in
identifying specific income levels. Additionally, our method surpasses Wang's method by a significant 2.8% in
recall, demonstrating its superior ability to identify relevant instances within a dataset, including specific income
levels. Furthermore, the 1.6% increase in f-measure compared to the CNN (Max.pool) method highlights the
superior balance between precision and recall offered by our proposed method. In conclusion, our proposed method
excels in accurately predicting individual income levels, as evidenced by its superior f-measure, recall, precision,
and accuracy metrics.
The proposed CNN architecture takes the advantage of both average and max pooling, while attempting to
overcome their limitations using the hybrid pooling layers. Average pooling aggregates all the feature activations
in a given region and max pooling identifies the most active region. Using hybrid pooling layers, makes our model
to more efficiently extract features from the customer data than models that employ one type of pooling only. This
is likely to have been the reason for the enhanced performance as depicted by Figure 4.
14

a. Analyzing the Average Classification Accuracy
Figure 4. Evaluating the quality of the classification.
The proposed method achieves the highest values across all metrics: precision 0.9295, recall 0.9321, F-measure
0.9306, and accuracy 93.06%. Following closely are CNN (Max.Pool) with precision 0.9147, recall 0.9146, F-
measure 0.9145, and accuracy 91.53%, and CNN (Avg.Pool) with precision 0.8996, recall 0.9028, F-measure
0.9007, and accuracy 90.10%. The methods Chakrabarty & Biswas, Rehman et al., and Wang exhibit lower
performance, with Rehman et al. demonstrating the lowest values across all metrics.
Figure 5 presents an illustration of the confusion matrices pertaining to the introduced methodology and alternative
comparative methodologies. Within this matrix, the rows depict the ground-truth classification of the instances,
while the columns refer to the output of each model, arranged in alphabetical order. The elements situated along
the main diagonal signify the accurate classification of the samples, whereas the non-main elements signify the
quantity of classification errors found in the test samples.
b. Analyzing the Classification Rates
15
a . A n a ly z in
b . A n
g
a
th e A v e ra
ly z in g th e
g e C
C la
la s s ific a
s s ific a tio
tio n
n R
A c c u
a te s
ra c y
ACCAERPTTICEDLE M IANN PURSECSRSIPT
S
S
E
R
P
N
I
E
L
C
I
T
R
A

Figure 5. Evaluating the confusion matrix.
By segregating our confusion matrix from other confusion matrices, such as image 5b and image 5c, it becomes
evident that our method, utilizing hybrid pooling layers, exhibits superior performance in segregating each group
of data compared to the CNN (Max.pool) and CNN (Avg.pool) layers. Additionally, our matrix reveals that our
proposed methodology has demonstrated better performance in segregating categories compared to the confusion
matrices (5d, 5e, and 5f). The confusion matrix for our proposed method in figure 5a showed that the elements in
the diagonal are higher than the other methods, meaning more number of elements correctly classified income
levels. Apart from this, the off-diagonal elements (errors) are also less in our matrix as compared to the other
methods which clearly explains that the proposed model is efficient enough to classify the individuals into their
respective income category.
The proposed method yields the highest accuracy of 93.06% among all the methods under comparison. Our method
yields the lowest value of false positive rate, but at the same time, it yields a higher true positive rate for each of
the income groups, which is evidence of the fact that the improvement in accuracy is not only due to the reduction
of false positives, but due to the increase of true positives as well.
Figure 6 depicts the ROC curve, presenting the FPR (false positive rate) and TPR (true positive rate) values for
evaluating our multi-class classification. We computed the TPR and FPR for each class separately. After obtaining
these TPR and FPR values, we aggregated and compared the ROC curve results for each method across all classes.
The ROC curve for our proposed method exhibits a larger area under the curve compared to other approaches. This
signifies a superior balance between the TPR and FPR achieved by our model. In simpler terms, our method
effectively identifies a higher proportion of true income levels (high TPR) while minimizing the number of false
positive classifications.
16
ACCAERPTTICEDLE M IANN PURSECSRSIPT
S
S
E
R
P
N
I
E
L
C
I
T
R
A

ACCAERPTTICEDLE M IANN PURSECSRSIPT

S
       Figure 6. Evaluating the ROC curve.
S
E
The methods presented by Chakrabarty & Biswas [17], Rehman et al. [18], and Wang [19] might face issues in
R
terms of modeling the interactions of the features within the customer data due to the model complexity or inability
P
to handle imbalanced datasets in which certain income bra ckets could be under-represented in the dataset. On the
N
other hand, the proposed CNN with hybrid pooling has a more flexible architecture that can potentially capture a
I

wider range of interactions between the features.
E
L
Table 5 compares the performance of vaCrious methods using precision, recall, F-measure, and accuracy metrics. In
this table, in addition to previously Icompared approached, the RF [12] and BiLSTM [16] models have been
T
considered for comparisons. FRor a fair comparative analysis, all of the models were trained and tested using the
same instances. The propoAsed method achieves the highest values across all metrics. Following closely are CNN
(Max.Pool) and CNN (Avg.Pool) confirming the effectiveness of CNNs in solving this problem, even while using
conventional pooling layers. The BiLSTM [16] and RF [12] models show performance close to the proposed
method. This indicated the desirable performance of deep learning and ensemble learning approaches in predicting
income level. The methods Chakrabarty & Biswas [17], Rehman et al. [18], and Wang [19] exhibit lower
performance, with Rehman et al. demonstrating the lowest values across all metrics.
Table 5. Performance comparison between the proposed method and previous approaches in predicting income level.
| Methods                    | Precision  | Recall  | F-Measure  | Accuracy  |
| -------------------------- | ---------- | ------- | ---------- | --------- |
| Proposed                   | 0.9295     | 0.9321  | 0.9306     | 93.0612   |
| CNN (Max.Pool)             | 0.9147     | 0.9146  | 0.9145     | 91.5306   |
| CNN (Avg.Pool)             | 0.8996     | 0.9028  | 0.9007     | 90.1020   |
| Chen et al. [12]           | 0.9077     | 0.9084  | 0.9079     | 90.9184   |
| Vemulapati et al. [16]     | 0.9125     | 0.9108  | 0.9111     | 91.0204   |
| Chakrabarty & Biswas [17]  | 0.8734     | 0.8755  | 0.8743     | 87.5510   |
| Rehman et al. [18]         | 0.8133     | 0.8159  | 0.8141     | 81.6327   |
| Wang [19]                  | 0.9027     | 0.9041  | 0.9029     | 90.4082   |
The methods [17-19] might face issues in terms of modeling the interactions of the features within the customer
data due to the model complexity or inability to handle imbalanced datasets in which certain income brackets could
17

ACCAERPTTICEDLE M IANN PURSECSRSIPT
be under-represented in the dataset. On the other hand, the proposed CNN with hybrid pooling has a more flexible
architecture that can potentially capture a wider range of interactions between the features.
4.2. Statistical Significance Analysis
As explained in Section 4.1, stratified 5-fold cross-validation was used to strictly assess the performance of the
proposed framework. The findings of the suggested CNN model were contrasted with two architectural variants
(Standard Max Pooling and Average Pooling) and five models of the recent literature [12, 16, 17, 18, 19] and the
results were reported in Table 5. To show that the performance gains obtained by the proposed approach are not
the result of chance, a statistical significance analysis was performed.
Table 6 provides the summary of the average accuracy, standard deviation, and the paired t-test results. The highest
mean accuracy of 93.02% and the lowest standard deviation (0.53%), which was obtained with the proposed model,
not only proves high performance but also demonstrates high stability of the model on various data subsets.
Table 6. Comparison of Statistical Analysis of Model Accuracy (5-Fold CV)
Model Average Accuracy Std. Dev. Acc. p-value
proposed 93.0612 0.5332 -
CNN(Max.Pool) 91.5306 0.83S96 0.00506
CNN(Avg.Pool) 90.1020 S1.0290 0.00076
Chen et al. [12] 90.9184 E0.5773 0.00372
Vemulapati et al. [16] 91.0204 R0.7287 0.01563
Chakrabarty & Biswas [17] 87.5510 P 1.9962 0.00576
Rehman et al [18] 81.6327 1.5962 0.00003
N
Wang [19] 90.4082 0.6981 0.00049
I
E
As shown in Table 6, all calculated p-values are significantly lower than the standard alpha level (𝛼 = 0.05). The
L
fact that our hybrid pooling method isC significantly better than standard CNN pooling mechanisms (p < 0.01)
confirms that our hybrid approach to Ipooling does not cause the loss of spatial information in feature extraction to
T
the same extent as standard CNN pooling mechanisms. Moreover, the fact that our 20×10 spatial mapping strategy
R
outperforms the established benchmarks like Vemulapati et al. [16] (p = 0.015) and Wang [19] (p < 0.001) shows
A
that our strategy is more effective at capturing latent socio-economic correlations compared to the traditional deep
learning or machine learning architecture. These results are strong statistical indicators that the suggested changes
to the CNN pipeline bring a substantial improvement in customer behavior analytics.
4.3. Evaluations in terms of product recommendation
In this phase, we have investigated the efficiency of the presented model from the aspect of product
recommendation. In other words, when we provide a recommendation for product types, we compared that product
with customers' buying habits and based on this comparison, we estimated the accuracy using eq. (8) The results of
the proposed approach have been compared with several models including CNN with Max Pooling layers for
(instead of hybrid pooling), and two baseline approaches: LightGBM [24], and RFM [26].
In Figure 7, the mean accuracy of product classification is illustrated. Our method has achieved a mean accuracy
of 95% in category 1, and also reached average accuracies of 92.89% and 94.81% in categories 4 and 6, respectively.
These results demonstrate that our approach has performed very well compared to the comparative method RFM
and the CNN (Max. Pool) method.
18

ACCAERPTTICEDLE M IANN PURSECSRSIPT
a. Product Category 1 b. Product Category 2
S
S
E
R
P
N
I
c. Product Category 3 E d. Product Category 4
L
C
I
T
R
A
e. Product Category 5 f. Product Category 6
Figure 7. Evaluating the product categories accuracy.
4.3. Feature Importance Analysis
This experiment analyzes the importance of various features and their contribution in prediction of income level by
the employed CNN structure. To do this, an attention layer was added between the input layer and the first
convolutional layer of the network. This layer, assigns weight to each input feature based on their importance and
transfers the weights to the subsequent layers. Since in input feature was translated to a binary vector of length 100,
the obtained weights for all 100 bits of each feature were summed to obtain the overall weight of the attribute. After
that, the obtained sum of weights for all features were normalized using the max-min approach (Equation 1). Figure
8 demonstrates the obtained normalized weight for each input feature which reflects its importance in predicting
income level of the individuals.
19

ACCAERPTTICEDLE M IANN PURSECSRSIPT
Figure 8. The normalized importance of features obtained through employing an attention layer in the structure of
the CNN S
S
As it is depicted in Figure 8, the six most important variables that Ecan be useful in determining the income level
R
include “Job Category”, “Education Level”, “Age”, “Job History”, “Place of Residence”, and “Marital Status”.
P
It is common knowledge that job category is usually a pointe r to income levels, particularly in the emerging markets.
N
There is normally a positive relationship between theI level of education and the income earner’s wages or salaries.
The third dependent variable age is also takenE into consideration as it defines the career level and further more
earning capability in hierarchical corporate Lenvironment. Whereas, stable & progressive job history has possibility
C
that only career advancement and higher earnings might be expected. Additionally, there is a higher probability of
I
higher average income in the urbanT areas especially the tier 1 and tier 2 cities. Finally, some cultures may determine
economical and financial aspeRcts of a couple’s financial life based on marital status and therefore this factor, based
A
on income level, is the sixth in the list. However, it should be pointed out that the significance of these factors may
differ based on the cultural, economic and social environment of the place from which the data was collected.
4.4. Practical Implications and Real-World Applications
The suggested CNN-based pipeline and probability matrix has a high potential of practical implementation,
especially in e-commerce and retail ecosystems. When used to classify users in real-time as an income level by
deploying the CNN model, platforms can automatically classify users into income levels based on initial
demographic or session data. After classifying one into an income group, the system uses the purchase probability
matrix (P) to customize user interfaces (UI) by ranking high-probability product categories in search results and
recommendation banners. This architecture can support dynamically tuned marketing policies; an example would
be to offer a 'High' income user premium electronics or luxury goods and offer a 'Low' income user value-oriented
alternatives. This kind of focused strategy does not only improve the customer experience, but also helps retailers
to manage their inventory effectively. By forecasting the demand of the income-specific products, businesses can
optimize the stock levels and minimize the overhead expenses and the chances of stockouts.
In the financial services industry, the model can be applied to evaluate the credit status of individuals thus
minimizing on defaults. Besides, it can also assist financial institutions in providing relevant financial services
including loans and investment products according to the customer’s financial strength.
20

ACCAERPTTICEDLE M IANN PURSECSRSIPT
When applied to the public policy area, the model can be used to determine who among the population requires
social help and therefore those who should be given the resources. Furthermore, the model can be used by
policymakers to understand the distributional effect of economic policies in order to make informed decisions.
Finally, in the area of consumer rights advocacy, the model can be applied to search for cases of unjustified or
misleading pricing or promotion of products for low-income consumers. Also, through the knowledge of the
consumer behavior and their choice, the advocacy groups can then call for the production of safer and cheaper
products.
With the help of using the AI and machine learning possibilities in processes the suggested model can foster fair
and progressive society.
5. Discussion, limitation, and Future Works
The current study aimed at assessing the outcomes of a new CNN model with the incorporation of hybrid pooling
layers for estimating customer income levels and then using it for the product recommendation tasks. The results
show that the proposed method outperforms the previous methods in the accuracy, precision, recall and F1-measure.
This section provides a further discussion on the significance of these findings, how these findings expand the
knowledge of consumers’ behavior, and possible applications. We also present the limitations that were experienced
during the research and recommend future research directions.
The success of our CNN architecture in predicting income levels, achieving an overall accuracy of 93.06%,
S
suggests its ability to capture complex relationships within customer daSta. By incorporating income level as a key
factor, our approach offers a more nuanced understanding of how iEncome demographics influence buying habits.
This advancement goes beyond traditional methods that might stRruggle to capture these intricate interactions. The
proposed method gives insight into the possibility of using CPNNs with hybrid pooling in the analysis of customer
behavior. To validate the generalization ability of thNe proposed model we used 5-fold cross validation. This
evaluation methodology ensured that there was no overfitting of the models since it was quite a rigorous process.
I
Comparison between hybrid pooling and the othe r forms of pooling such as max pooling and average pooling
E
showed that the former outperformed the laLtter in terms of accuracy, precision, recall and F1-score. These results
decisively indicate that the employmentC of the hybrid pooling strategy positively contributes to the improvement
of the model’s capability to generaliIze from unseen data. The use of average and max pooling through hybrid
T
pooling layers in our model allows for the extraction of more complete features from customer data as compared to
R
the use of standard poolingA alone.
This finding contributes to the growing body of research exploring the effectiveness of deep learning techniques in
understanding consumer behavior, especially considering the significant improvement of 2.7% in accuracy
compared to the Wang method (90.4%) which utilizes conventional pooling layers. The fact that one can forecast
the income levels and make recommendations based on this data (mean accuracy of 93.1% for product
recommendations) is quite practical in reality.
The possibility of precise income level forecasting and the factors influencing consumers’ behavior are significant
for different industries. For instance, the information in this context can be used by retailers to manage their stocks,
design and implement marketing strategies, and design new products that suit the needs of their target customers.
This can have a positive impact on customer satisfaction, the conversion rate of sales, and better resource utilization.
Such information may help to evaluate the credit standing of clients and adjust the offered financial services. In
addition, such models can be useful for the policymakers in order to improve the economic policies and fight against
the income disparity. Aside from the practical implications, our research contributes to the literature on consumer
behavior and the part that income plays in consumers’ decisions. It can be useful for the public policy debate on
issues such as income disparity and consumer rights.
5.1. Limitations and Future Works
Even though the proposed model is highly accurate and practically useful, certain limitations should be considered.
These are divided into limitations of the present and future research directions.
Research Limitations:
21

ACCAERPTTICEDLE M IANN PURSECSRSIPT
• Population Representativeness: Although the 980-sample sample is all-inclusive in this study, it might not
be an accurate reflection of the entire world population, which can create predictive biases in highly
different socio-economic settings.
• Geographic and Cultural Specificity: The present results are based on the regional data; hence, the
performance of the model can differ in the case of other cultural backgrounds with their own shopping
patterns.
• Feature Engineering Scope: The existing feature set, although strong, might not have necessary granular
cultural or micro-economic indicators that can be used to determine individual buying choices.
• Internal vs. External Validation: Cross-validation has been done to ensure that the model is highly
generalized in the given dataset, but the stress-testing of the model against completely external datasets that
are independent of the given dataset has not been conducted yet.
Future Research Directions:
• Increasing Data Sources: Future research must use a variety of data sources across different countries to
enhance the external validity and globalizability of the results.
• Adding Longitudinal Data: By adding variables that track time-series, the model would be able to adjust to
changing consumption trends as time progresses.
• Advanced Architectures: We plan to explore Transformer-based models and transfer learning techniques
to further enhance sequence modeling and reduce the data training requirements for unfamiliar domains.
• Interdisciplinary Integration: Cooperation with behavioral scientists to incorporate psychological profiling
may offer a better insight into the reason behind the expected buyinSg behavior.
• Hardware and Efficiency Optimization: Investigating memristSive CNN architectures could significantly
improve computational and energy efficiency, enabling reEal-time processing for large-scale industrial
applications. R
P
N
6. Conclusion I
The paper focused on the utilization of a convoluti onal neural network to analyze and model customer purchasing
E
habits in relation to their income levels.L The study consisted of three primary stages: data preprocessing,
C
categorizing individuals based on their income levels, and providing product recommendations tailored to their
I
income brackets. The primary aimT of the paper was to enhance understanding of individuals' purchasing behaviors
and to improve the accuracy anRd relevance of product recommendations personalized to their specific income levels.
The results indicated thatA the presented approach outperformed alternative techniques by increasing average
accuracy to 93.06% and precision to 92.95%, thus demonstrating superior performance in predicting individuals'
income levels. Additionally, the proposed method achieved at least 2.77% improvement in terms of f-measure
compared to the benchmark methods. This significant improvement shows the high quality of the classification
results produced by the proposed method. Furthermore, in the phase 2, our method showed that it has a mean
accuracy of 95% which is at least 4.05% higher compared to other comparative methods in product
recommendation.
APPENDIX A
This appendix provides a comprehensive overview of the questionnaire used for data collection and includes the exact wording
of questions and response options.
Demographics
1. Gender:
o Male
o Female
o Prefer not to say
2. Marital Status:
o Single
o Married
22

ACCAERPTTICEDLE M IANN PURSECSRSIPT
| o   | Divorced             |     |     |
| --- | -------------------- | --- | --- |
| o   | Widowed              |     |     |
| o   | Living with Partner  |     |     |
| o   | Prefer not to say    |     |     |
3.  Age: (Please enter your age)
4.  Education Level:
| o   | High School Diploma or Equivalent  |     |     |
| --- | ---------------------------------- | --- | --- |
| o   | Associate's Degree                 |     |     |
| o   | Bachelor's Degree                  |     |     |
| o   | Master's Degree                    |     |     |
| o   | Doctorate or Professional Degree   |     |     |
| o   | Prefer not to say                  |     |     |
5.  Job Category: (Please select the category that best describes your current job)
| o   | Management/Professional  |     |     |
| --- | ------------------------ | --- | --- |
o
Sales/Service
| o   | Skilled Trades/Labor               |     |     |
| --- | ---------------------------------- | --- | --- |
| o   | Administrative/Clerical            |     |     |
| o   | Student/Unemployed                 |     |     |
| o   | Retired                            |     |     |
| o   | Other (Please specify): _________  |     |     |
6.  Job History (Years): (How many years have you been working in your current field?)
| 7.  Place of Residence:  |                    |     | S   |
| ------------------------ | ------------------ | --- | --- |
| o                        | Urban Area (City)  |     | S   |
| o                        | Suburban Area      |     |     |
E
o
|     | Rural Area  | R   |     |
| --- | ----------- | --- | --- |
8.  Residential Status:  P
| o   | Own Home  |     |     |
| --- | --------- | --- | --- |
N
| o   | Rent Apartment/House  |     |     |
| --- | --------------------- | --- | --- |
I
| o   | Live with Family/Friends            |     |     |
| --- | ----------------------------------- | --- | --- |
| o   | Other (Please specify): ________E_  |     |     |
9.  Do you have any specific chronic diseaLses? (Yes/No)
C
| o   | If yes, please specify: _________  |     |     |
| --- | ---------------------------------- | --- | --- |
I
Shopping Habits
T
10.  Alcohol Consumption: R
o
Never drinkA alcohol
| o   | Drink occasionally  |     |     |
| --- | ------------------- | --- | --- |
| o   | Drink regularly     |     |     |
11.  Consumption of Tobacco or Other Addictive Substances: (Yes/No)
| o   | If yes, please specify: _________  |     |     |
| --- | ---------------------------------- | --- | --- |
12.  On average, how many times do you shop in person per week?
13.  On average, how many times do you shop online per week?
14.  On average, how many items do you typically add to your cart during in-person shopping trips?
15.  On average, how many items do you typically add to your cart during online shopping trips?
16.  On average, how many hours per week do you typically work?
Income Level
17.  We understand that income level can be a personal question. If you are comfortable sharing this information, please
select your income range:
| o   | Below $25,000        |     |     |
| --- | -------------------- | --- | --- |
| o   | $25,000 - $49,999    |     |     |
| o   | $50,000 - $74,999    |     |     |
| o   | $75,000 - $99,999    |     |     |
| o   | $100,000 and above   |     |     |
| o   | Prefer not to say    |     |     |

Product Preferences
Thank you for participating in this survey! This section focuses on your preferences for various product categories.
Please note: There is no right or wrong answer. We are simply interested in understanding your brand choices.
23

ACCAERPTTICEDLE M IANN PURSECSRSIPT
If you don't have a preference for a particular category, you can skip that section.
Mobile Phones:
• Brand 1: _________
• Brand 2: _________
• Brand 3: _________ (or "No Preference")
Tablets:
• Brand 1: _________
• Brand 2: _________
• Brand 3: _________ (or "No Preference")
Laptops:
• Brand 1: _________
• Brand 2: _________
• Brand 3: _________ (or "No Preference")
Clothing:
• Brand 1: _________
• Brand 2: _________
• Brand 3: _________ (or "No Preference")
Entertainment Items:
• Brand 1: _________ (e.g., TVs, Video Game Consoles)
• Brand 2: _________
• Brand 3: _________ (or "No Preference") S
Food: S
• Brand 1: _________ (e.g., Grocery Stores, Restaurants) E
• Brand 2: _________ R
• Brand 3: _________ (or "No Preference") P
N
I
Funding
E
L
C
The work described in this paper was supported by a grant from Social Science Foundation of Shandong Province, China
I
(Grant No. 17CGLJ15). This article Tis the research outcome of a university-level project at Shandong Women’s University
(Project Approval Number: 2021RRCYJ02/57).
A
Data availability
All data generated or analysed during this study are included in this published article.
REFERENCES
[1] Dingli, A., Marmara, V., & Fournier, N. S. (2017). Comparison of deep learning algorithms to predict customer churn
within a local retail industry. International journal of machine learning and computing, 7(5), 128-132.
[2] Lang, T., & Rettenmeier, M. (2017, April). Understanding consumer behavior with recurrent neural networks. In
Workshop on Machine Learning Methods for Recommender Systems.
[3] Kalaivani, D., & Arunkumar, T. (2018). Multi process prediction model for customer behaviour analysis. International
Journal of Web Based Communities, 14(1), 54-63.
[4] Russell, G. J., & Petersen, A. (2000). Analysis of cross category dependence in market basket selection. Journal of
Retailing, 76(3), 367-392.
[5] Wang, H. F., & Hong, W. K. (2006). Managing customer profitability in a competitive market by continuous data
mining. Industrial marketing management, 35(6), 715-723.
[6] Rosário, A., & Raimundo, R. (2021). Consumer marketing strategy and E-commerce in the last decade: a literature
review. Journal of theoretical and applied electronic commerce research, 16(7), 3003-3024.
[7] Felix, A., & Rembulan, G. D. (2023). Analysis of key factors for improved customer experience, engagement, and
loyalty in the e-commerce industry in Indonesia. Aptisi Transactions on Technopreneurship (ATT), 5(2sp), 196-208.
[8] Li, Y. F., Guo, L. Z., & Zhou, Z. H. (2019). Towards safe weakly supervised learning. IEEE transactions on pattern
analysis and machine intelligence, 43(1), 334-346.
24

ACCAERPTTICEDLE M IANN PURSECSRSIPT
[9] Parihar, V., & Yadav, S. (2021). Comparison estimation of effective consumer future preferences with the application
of AI. Vivekananda Journal of Research, 10, 133-145.
[10] Yamnampet, G. Comparative analysis of classification models on income prediction. International Journal on Recent
and Innovation Trends in Computing and Communication, 5(4), 451-455.
[11] Thapa, S. (2023). Adult Income Prediction Using various ML Algorithms. Available at SSRN 4325813.
[12] Chen, J., Mao, S., & Yuan, Q. (2022, March). Salary prediction using random forest with fundamental features. In Third
International Conference on Electronics and Communication; Network and Computer Technology (ECNCT 2021) (Vol.
12167, pp. 491-498). SPIE.
[13] Viroonluecha, P., & Kaewkiriya, T. (2018, September). Salary predictor system for thailand labour workforce using
deep learning. In 2018 18th International Symposium on Communications and Information Technologies (ISCIT) (pp.
473-478). IEEE.
[14] Kablaoui, R., & Salman, A. (2022, November). Machine Learning Models for Salary Prediction Dataset using Python.
In 2022 International Conference on Electrical and Computing Technologies and Applications (ICECTA) (pp. 143-
147). IEEE.
[15] Wang, P., Liao, W., Zhao, Z., & Miu, F. (2022). Prediction of Factors Influencing the Starting Salary of College
Graduates Based on Machine Learning. Wireless Communications and Mobile Computing, 2022.
[16] Vemulapati, J., Bayyana, A., Bathula, S. H., Tokala, S., Hajarathaiah, K., & Enduri, M. K. (2023, February). Empirical
Analysis of Income Prediction Using Deep Learning Techniques. In 2023 IEEE International Students' Conference on
Electrical, Electronics and Computer Science (SCEECS) (pp. 1-6). IEEE.
[17] Chakrabarty, N., & Biswas, S. (2018, October). A statistical approach to adult census income level prediction. In 2018
International Conference on Advances in Computing, Communication Control and Networking (ICACCCN) (pp. 207-
212). IEEE. S
[18] Rehman, A. U., Saleem, R. M., Shafi, Z., Imran, M., Pradhan, M., & SAlzoubi, H. M. (2022, February). Analysis of
Income on the Basis of Occupation using Data Mining. In 2022 InEternational Conference on Business Analytics for
Technology and Security (ICBATS) (pp. 1-4). IEEE. R
[19] Wang, J. (2022, October). Research on Income ForecastingP based on Machine Learning Methods and the Importance
of Features. In Proceedings of the International Confer ence on Information Economy, Data Modeling and Cloud
N
Computing, ICIDC 2022, 17-19 June 2022, Qingdao, China.
I
[20] Xian, Z., Keikhosrokiani, P., XinYing, C., & Li, Z. (2022). An RFM model using K-means clustering to improve
customer segmentation and product recommEendation. In Handbook of Research on Consumer Behavior Change and
Data Analytics in the Socio-Digital Era (pLp. 124-145). IGI Global.
C
[21] Chaubey, G., Gavhane, P. R., Bisen, D., & Arjaria, S. K. (2023). Customer purchasing behavior prediction using
I
machine learning classification techniques. Journal of Ambient Intelligence and Humanized Computing, 14(12), 16133-
T
16157. R
[22] Kumar, M. R., VenkAatesh, J., & Rahman, A. M. Z. (2021). Data mining and machine learning in retail business:
developing efficiencies for better customer retention. Journal of Ambient Intelligence and Humanized Computing, 1-
13.
[23] Anitha, P., & Patil, M. M. (2022). RFM model for customer purchase behavior using K-Means algorithm. Journal of
King Saud University-Computer and Information Sciences, 34(5), 1785-1792.
[24] Nguyen, D. N., Nguyen, V. H., Trinh, T., Ho, T., & Le, H. S. (2024). A personalized product recommendation model
in e-commerce based on retrieval strategy. Journal of Open Innovation: Technology, Market, and Complexity, 10(2),
100303.
[25] Parihar, V., & Yadav, S. (2021). Comparison estimation of effective consumer future preferences with the application
of AI. Vivekananda Journal of Research, 10, 133-145.
[26] Zhao, X., & Keikhosrokiani, P. (2022). Sales Prediction and Product Recommendation Model Through User Behavior
Analytics. Computers, Ma-terials & Continua, 70(2).
[27] Hussain, N. Y. (2024). Deep learning architectures enabling sophisticated feature extraction and representation for
complex data analysis. Int. J. Innov. Sci. Res. Technol.(IJISRT), 9, 2290-2300.
[28] Islam, M. R., Hossain, M., Alam, M., Khan, M. M., Rabbi, M. M. K., Rabby, M. F., ... & Tarafder, M. T. R. (2025).
Leveraging Machine Learning for Insights and Predictions in Synthetic ECommerce Data in the USA: A Comprehensive
Analysis. Journal of Ecohumanism, 4(2), 2394-2420.
[29] Yang, Y., Wu, Z., Yang, Y., Lian, S., Guo, F., & Wang, Z. (2022). A survey of information extraction based on deep
learning. Applied Sciences, 12(19), 9691.
[30] Dritsas, E., & Trigka, M. (2025). Machine learning in e-commerce: Trends, applications, and future challenges. IEEE
Access.
[31] Zhang, P. (2021). E-commerce products recognition based on a deep learning architecture: Theory and implementation.
Future Generation Computer Systems, 125, 672-676.
25

ACCAERPTTICEDLE M IANN PURSECSRSIPT
[32] Kostopoulos, G., Stefani, A., Vasiliadis, V., & Kotsiantis, S. (2026). Deep Learning for e-Commerce: Recent
Developments in Prediction, Personalization and Decision Intelligence. Applied Sciences, 16(5), 2263.
[33] Thanapol, P., Lavangnananda, K., Bouvry, P., Pinel, F., & Leprévost, F. (2020, October). Reducing overfitting and
improving generalization in training convolutional neural network (CNN) under limited sample sizes in image
recognition. In 2020-5th International Conference on Information Tech-nology (InCIT) (pp. 300-305). IEEE.
[34] Boureau, Y. L., Ponce, J., & LeCun, Y. (2010). A theoretical analysis of feature pooling in visual recognition. In
Proceedings of the 27th international conference on machine learning (ICML-10) (pp. 111-118).
[35] Zeiler, M. D., & Fergus, R. (2013). Stochastic pooling for regularization of deep convolutional neural networks. arXiv
preprint arXiv:1301.3557.
[36] Tong, Z., & Tanaka, G. (2019). Hybrid pooling for enhancement of generalization ability in deep convolutional neural
networks. Neurocompu-ting, 333, 76-85.
S
S
E
R
P
N
I
E
L
C
I
T
R
A
26