---
conversion_metadata:
  converted_at: "2026-07-22T13:29:50Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Hamidi & Hagdi.pdf"
  source_pdf_sha256: "f96b6ffb88b35a972dc0924cefd1d85c82c29394f20d4fbef4eadac9206dbb2d"
  page_count: 18
  markdown_char_count: 182032
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Computers in Human Behavior Reports 16 (2024) 100520

Contents lists available at ScienceDirect

Computers in Human Behavior Reports

journal homepage: www.sciencedirect.com/journal/computers-in-human-behavior-reports

An approach based on data mining and genetic algorithm to optimizing 
time series clustering for efficient segmentation of customer behavior

Hodjat (Hojatollah) Hamidi *, Bahare Haghi

Department of Industrial Engineering, Information Technology Group, K. N. Toosi University of Technology, Iran

A R T I C L E  I N F O

A B S T R A C T

Keywords:
Dynamic segmentation
Feature optimization
Genetic algorithm
Time series analysis
Clustering techniques
Customer behavior analysis

In today’s highly competitive market, organizations face significant challenges in accurately understanding and 
segmenting customer behavior due to the inherently dynamic and evolving nature of customer interactions over 
time. Traditional customer segmentation methods often neglect these temporal variations, leading to ineffective 
business strategies and missed opportunities. This research addresses this critical gap by introducing an inno-
vative time series-based approach for customer behavior segmentation. By modeling each customer’s behavior as 
a time series capturing key metrics such as purchase frequency, transaction amounts, and customer lifecycle costs 
the proposed method dynamically adapts to behavioral changes over time. To enhance segmentation precision, a 
genetic algorithm is employed to optimize feature weights, ensuring that the most relevant factors are empha-
sized. These optimized features are then clustered using spectral clustering to identify distinct and meaningful 
customer segments. The effectiveness of the proposed method is validated using 30 months of transactional data 
from  a  payment  services  company.  The  results  demonstrate  that  the  proposed  approach,  particularly  when 
combined with spectral clustering and optimally weighted features, significantly surpassing the performance of 
traditional  static  segmentation  techniques.  This  research  not  only  provides  a  more  accurate  framework  for 
uncovering hidden patterns in customer behavior but also delivers actionable insights for targeted marketing and 
personalized customer strategies.

1. Introduction

Nowadays,  customer  relationship  management  has  become 
extremely  important  due  to  intense  competition  among  companies  in 
various  industries  (Kumar  &  Reinartz,  2018).  With  advancements  in 
information  and communication technologies, a large volume of  data 
about  customers  is  available  to  organizations.  To  utilize  this  data  for 
strategic  decision-making,  data  mining  techniques  have  emerged  as 
powerful  tools  for  data  analysis  and  knowledge  creation  (Parvaneh 
et al., 2014). This segmentation helps organizations interact more effi-
ciently with customers by leveraging data analysis methods.

In this paper, we present a new model for customer segmentation 
using  data  mining  techniques.  This  model,  using  appropriate  data 
mining algorithms and methods tailored to the organization’s dataset, 
can segment customers into different groups based on common features. 
In  the  proposed  model,  the  features  of  purchase  novelty,  number  of 
purchases,  purchase  amount,  and  customer  cost  are  extracted  from 
customer transaction data. The proposed model uses powerful clustering 
algorithms, including hierarchical clustering, spectral clustering, fuzzy

C-means  clustering,  and  K-means  clustering,  to  achieve  the  best  clus-
tering  results  (Akhondzadeh-Noughabi  &  Albadvi,  2015;  Seret  et  al., 
2014; Yanovitzky & VanLear, 2008).

The biggest limitation of static segmentation methods is that these 
methods are not able to model the dynamic behavior of customers and 
discover  meaningful  patterns  and  trends  (Khajvand  &  Tarokh,  2011; 
SARI  et  al.,  2016).  These  methods  are  more  descriptive  and  cannot 
predict the future behavior of customers. In this model, time series are 
used to record customer behavior and maintain the chronological order 
of observations. First, the features of purchase recency, purchase num-
ber,  purchase  amount,  customer  cost  was  extracted  from  customer 
transaction  data,  then  customers  were  segmented  using  time  series 
clustering. In this research, the cost has been investigated as one of the 
important features, which has not been sufficiently considered in pre-
vious researches. Considering cost as one of the important features in 
customer  analysis  and  business  management  is  very  important.  In 
various business fields, including banking, retail, services, etc., costs can 
be one of the determining factors in decisions. In the banking industry, 
an accurate understanding of the cost-benefit ratio for each customer

* Corresponding author. IT Information Technology Engineering Group K.N. Toosi University of Technology, Iran.

E-mail addresses: h_hamidi@kntu.ac.ir (H.(H. Hamidi), b.haghi@email.kntu.ac.ir (B. Haghi).

https://doi.org/10.1016/j.chbr.2024.100520
Received 2 September 2024; Received in revised form 25 October 2024; Accepted 29 October 2024  
Available online 1 November 2024 
2451-9588/© 2024 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by- 
nc-nd/4.0/ ).

---

<!-- PAGE 2 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

can help the bank to provide appropriate strategies to attract, retain and 
upgrade customers. By knowing this ratio for each customer, the bank 
can  evaluate  the  improvement  of  its  financial  performance,  establish 
purposefulness  in  the  use  of  financial  resources,  and  realize  the 
improvement of relations with customers who have a better cost-benefit 
ratio. In addition, in the existing research, multivariate time series have 
been used instead of univariate time series, and instead of examining the 
effect  of  individual  characteristics,  they  have  also  examined  their 
simultaneous effect together. By considering multivariate time series, it 
is possible to examine the simultaneous effect of different characteristics 
on  customer  behavior.  This  makes  it  possible  to  understand  the  con-
nections  and  interactions  between  attributes  and  to  analyze  their 
simultaneous influence on customer behavior. This more comprehensive 
analysis makes it possible to discover hidden patterns and more complex 
relationships that are not visible in the analysis of individual features. As 
a  result,  more  accurate  and  reliable  predictions  about  the  needs  and 
desires of customers can be reached.

In this paper, a model is presented that displays the behavior of each 
customer  as  a  time  sequence  of  the  variables  of  purchase  novelty, 
number of purchases, purchase amount, and customer cost, considering 
the time dimension of customer behavior. Then, using the genetic al-
gorithm, optimal weights are found for each feature, and customers are 
segmented with clustering algorithms. To demonstrate the utility of this 
model,  a  case  study  on  the  customers  of  a  banking  payment  service 
company is conducted.

The structure of the paper is as follows: Section 2 reviews  related 
works.  The  various  techniques  used  in  the  paper  and  the  proposed 
method for customer behavior analysis are presented in Section 3. The 
results of the proposed framework are reported in Section 4. Section 5 is 
dedicated  to  evaluating  the  performance  of  the  proposed  algorithm. 
Finally, Section 6 concludes the paper and suggests some directions for 
future research.

2. Literature review

In (SARI et al., 2016), the authors reviewed customer segmentation 
methods and highlighted that demographic segmentation (age, gender, 
education,  occupation,  income)  helps  in  understanding  customer 
behavior  and  optimizing  marketing  costs.  In  (Khajvand  &  Tarokh, 
2011), a banking study segmented customers based on new purchases, 
purchase frequency, and amount, predicting each segment using time 
series  analysis.  In (Khajvand et  al.,  2011), two  methods  for  customer 
segmentation  and  lifetime  value  calculation  were  presented,  showing 
that adding item count as a new parameter had no significant effect on 
clustering.

In  (Heldt  et  al.),  a  model  for  purchase  frequency  and  amount  per 
product showed that product data provides useful insights for marketing 
asset  management  and  reduces  customer  value  prediction  errors.  In 
(Anitha  &  Patil,  2019),  a  study  using  new  purchase  frequency  and 
amount  in  retail  employed  K-means  clustering,  evaluated  with  the 
silhouette index. In (Daneshvar et al., 2020), a new multi-criteria clus-
tering  method  with  bi-phase  optimization  was  introduced,  enhancing 
the  genetic  algorithm  with  heuristic  mutation  for  effective  yet 
time-consuming clustering.

In (Tavakoli et al., 2018), a hybrid model combining new purchase 
frequency,  amount, and  time series  was  proposed, showing  improved 
customer analysis and strategic decision-making through Short Message 
Service  (SMS)  campaigns.  In  (ABBASIMEHR  &  BAHRINI,  2022), 
advanced clustering and time series clustering considered the temporal 
dimension  of  customer  behavior,  using  transaction  data  for  new  pur-
chase  frequency  and  amount  features.  In  (Christy  et  al.,  2018),  new 
purchase frequency and amount analysis on transaction data, and clus-
tering  with  K-means  and  fuzzy  C-means,  introduced  a  new  idea  for 
initial cluster center selection.

In  (Çavdar  &  Ferhatosmano˘glu,  2018),  an  airline  industry  model 
estimated customer lifetime value using flight data and social network

data,  showing  improved  accuracy  with  social  factors.  In  (Emami  & 
Derakhshan, 2015), a company’s customers were analyzed using new 
purchase  frequency  and  amount,  employing  fuzzy  clustering  and 
customer portfolio analysis. The profitability index validated the results, 
categorizing  customers  into  three  clusters:  superstar,  regular,  and 
dormant based on lifetime value.

In  (Sivaguru,  2023),  a  dynamic  customer  segmentation  (DCS) 
framework  is  introduced,  comprising  three  phases:  the  first  phase  in-
volves using the modified fuzzy c-means (MdFCM) algorithm to cluster 
new data and identify changes in cluster structures; the second phase 
classifies  clusters  based  on  the  RFM  (Recency,  Frequency,  Monetary) 
pattern; and the third phase formulates marketing strategies based on 
identified  changes  in  the  clusters.  The  MdFCM  algorithm  calculates 
distances  between  cluster  centers,  selects  the  minimum  distance,  and 
compares new data distances with this minimum. If the new data dis-
tance exceeds the minimum, new clusters are created or old ones are 
removed; otherwise, clusters are adjusted. This framework helps man-
agers update customer segmentation with new information and enhance 
marketing strategies accordingly.

In (Luo et al., 2023), a new Bayesian nonparametric model named 
Hierarchical Fragmentation-Coagulation Processes (HFCP) is introduced 
for dynamic customer segmentation. This model works as follows: first, 
HFCP automatically determines the number of groups required to model 
diverse  customer  behavior.  Next,  the  model  can  identify  dynamic 
changes  in  customer  behavior,  such  as  the  splitting  and  merging  of 
groups. Using a hierarchical approach, HFCP discovers shared behavior 
patterns  across  different  products.  Additionally,  HFCP  outperforms 
previous  models  such  as  Homogeneous  Poisson  Processes  (HomoPP), 
Non-Homogeneous 
and 
Fragmentation-coagulation  process)FCP(in  predicting  the  purchase 
behavior of new customers and addresses overfitting issues. This model 
employs  Fragmentation-Coagulation  Processes  to  model  changes  in 
customer  purchasing  behavior  and  helps  companies  adjust  their  mar-
keting strategies  based  on  accurate behavioral patterns.  Empirical  re-
sults  demonstrate  that  HFCP  effectively  models  customer  purchasing 
behavior and improves performance.

Processes

(NHPP),

Poisson

In  (John  et  al.,  2023),  various  clustering  algorithms  for  customer 
segmentation in the UK online retail market were compared. The study 
used a UK-based online retail dataset and evaluated algorithms such as 
K-means, Gaussian Mixture Model (GMM), Density-Based Spatial Clus-
tering of Applications with Noise (DBSCAN), agglomerative clustering, 
and  Balanced  Iterative  Reducing  and  Clustering  using  Hierarchies 
(BIRCH).  The results  indicated  that  the  GMM  algorithm  achieved  the 
best performance with a Silhouette Score of 0.80. This research dem-
onstrates that advanced algorithms can improve the accuracy and effi-
ciency of customer segmentation, allowing companies to fine-tune their 
marketing  strategies  and  better  understand  customer  purchasing 
behavior.

Table 1 is related to the summary of the review of the theoretical 
foundations of customer segmentation, in which the  information pro-
vided in the literature review is summarized and the different types of 
segmentation  models  are  given  along  with  the  studies  conducted  by 
researchers and the years associated with each method. From Tables 1
and it can be concluded simply and briefly that the previous researches 
on  customer  segmentation  have  used  the  method  of  new  purchase, 
repeat purchase, and purchase amount.

Fig. 1 shows the algorithms used in the reviewed articles. Most of the 
reviewed  articles  have  used  unsupervised  learning  algorithms  for 
customer  segmentation.  Therefore,  unsupervised  learning  algorithms 
have been used in this research.

In Fig. 2, a comparison is made between the unsupervised learning 
algorithms  used  in  the  articles.  The  most  popular  algorithms  are  K- 
Means, fuzzy C-Means, Spectral, hierarchical, K-shape, self-organizing 
maps, concentration-based clustering and finally K-Medoids.

According to the literature review, it was concluded that unsuper-
vised  learning  algorithms  are  mostly  used  in  research.  Unsupervised

2

---

<!-- PAGE 3 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Table 1 
Summary of overview of the theoretical bases of customer segmentation.

Neural 
network

Time 
series

Clustering

Classification

Regression

New purchase 
Repeat 
purchase 
Purchase 
amount

(Akhondzadeh-Noughabi & Albadvi, 2015; Parvaneh et al., 2014; Yanovitzky & 
VanLear, 2008)
(SARI et al., 2016)
(Khajvand & Tarokh, 2011)
(Khajvand et al., 2011)
(Heldt et al.; Anitha & Patil, 2019)
(Daneshvar et al., 2020)
(Tavakoli et al., 2018)
(ABBASIMEHR & BAHRINI, 2022)
(Christy et al., 2018)
(Çavdar & Ferhatosmano˘glu, 2018)
(Emami & Derakhshan, 2015)
(Sivaguru, 2023)
(Luo et al., 2023)
(John et al., 2023)
(Batista et al., 2014)
(Arbelaitz et al., 2014)
(Dunn, 1973)
(Alboukaey et al., 2020)
(Montero-Manso & Hyndman, 2021)
(ABBASIMEHR & Shabani, 2021)
(Hamidi, 2016)

✓

✓
✓
✓

✓
✓
✓

✓

✓

✓

✓
✓
✓

✓

✓

✓
✓
✓

✓

✓
✓
✓

✓

✓

✓
✓

Fig. 1. Comparison chart of data mining methods used in articles.

learning algorithms are highly attractive to researchers due to capabil-
ities such as data clustering and discovering hidden patterns in them. 
These algorithms are used especially when the data is not labeled and 
there  is  a  need  to  segment  and  recognize  patterns  and  relationships 
between the data. After examining more details among the unsupervised 
algorithms,  the  top  four  unsupervised  algorithms  were  selected.  This 
choice was made based on the importance, performance and potential of 
these  algorithms  in  data  clustering.  Therefore,  in  this  research,  these 
four best algorithms (K-Means, Hierarchical Spectral, Fuzzy C-means) 
have been used to perform data clustering. This choice has been made 
according to the literature review and based on the ability and efficiency 
of these algorithms in the field of data clustering.

Reviewing  past  studies  reveals  that  most  customer  segmentation 
research  focuses  on  Recency,  Frequency,  and  Monetary  (RFM)  values 
due to their simplicity and efficiency. However, these studies treat RFM

features independently and assign equal weights, overlooking their in-
terrelationships and varying importance. Additionally, static RFM-based 
methods  fail  to  capture  the  dynamic  nature  of  customer  interactions, 
limiting their ability to adapt to evolving behaviors and market condi-
tions.  Moreover,  customer  lifecycle  costs  are  frequently  neglected 
despite  their  significance  in  understanding  customer  profitability.  To 
address  these  gaps,  this  paper  incorporates  Customer  Cost  into  the 
segmentation process, employs a genetic algorithm to optimize feature 
weights,  and  utilizes  time  series  analysis  to  account  for  temporal  dy-
namics.  These  enhancements  result  in  more  accurate  and  adaptive 
customer  segmentation,  providing  a  comprehensive  understanding  of 
customer  behavior  and  supporting  the  development  of  effective, 
responsive marketing strategies.

3

---

<!-- PAGE 4 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Fig. 2. Comparative diagram of unsupervised algorithms used in articles.

3. Research methodology

As shown in Fig. 3, the proposed model effectively integrates new 
transactions,  the  number  of  transactions,  transaction  profit,  and  cost 
with time series clustering. It extracts time series data from a stream of 
timestamped transactional data to depict the behavior of customers. The 
details of each step in the model are explained below.

3.1. CRISP methodology

CRISP is a common methodology in the field of data mining that is 
used  to  carry  out  data  mining  projects.  This  methodology  consists  of 
several steps that are executed sequentially and includes the complete 
process  of  data  analysis.  In  the  following,  its  steps  are  explained 
(ABBASIMEHR & SheikhBaghery, 2022).

3.1.1. Business understanding phase

The business understanding step in the CRISP methodology is related 
to the deep understanding that the researcher needs to know about the 
business under investigation. In this step, the researcher should examine 
and analyze the market, products and services, customers, competitors, 
organizational  structure  and  other  business-related  factors.  To  get  to 
know the business, different methods can be used, including:

Studying documents and related sources: By studying reports, arti-
cles,  books  and  other  sources  related  to  business,  one  can  get  the 
necessary information about the type of activities, target market, com-
petitors and other aspects of the business.

Interviewing  experts:  by  interviewing  people  who  work  in  the  in-
dustry or organization under investigation, you can gather their opin-
ions  and  knowledge  about  the  business  and  reach  a  higher 
understanding.

Direct observation: By directly observing the activities, products and 
services of the business, you can get a better understanding of its per-
formance and characteristics. As a result, by knowing the business, it is 
possible to consider the best approach and appropriate solutions for the 
successful implementation of the research and facilitate obtaining the 
desired results.

3.1.2. Data understanding phase

The step of data understanding in CRISP methodology is related to 
the  process  of  understanding  and  analyzing  data.  In  this  step,  the

researcher must collect the available data and analyze them in a regular 
and organized manner.  To understand the data, various methods and 
techniques can be used, including:

Data  Collection:  Business  related  data  is  collected.  This  data  in-
cludes  customer  transaction  data,  information  related  to  products  or 
services, financial data and other business related information.

Data Preprocessing: In this step, the data is preprocessed. It includes 
data cleaning, removing incomplete or duplicate data, converting data 
format and structuring them properly.

Data analysis: Using data analysis methods, patterns and trends in 
the data can be identified. Various techniques such as descriptive sta-
tistics, data mining methods, modeling and other methods are used. By 
doing  the  mentioned  steps,  a  better  understanding  of  the  data  and 
business characteristics can be achieved, which will help in the subse-
quent analysis and modeling.

3.1.3. Data collection and preparation phase

The data collection and preparation step in the CRISP methodology 
belongs  to  the  process  in  which  the  necessary  data  for  subsequent 
analysis and modeling are collected, extracted, cleaned and prepared. In 
this step, steps should be taken to make the data useable and reliable. To 
collect and prepare data, the following methods and techniques can be 
used:

Data collection: In this step, data related to the research is collected. 
It includes customer transaction data, product or service data, financial 
data,  historical  data  and  other  required  information.  Data  can  be 
collected from internal company sources (such as database management 
systems)  or  external  sources  (such  as  Internet  sources  or  public  data 
sources).

Data Cleansing: In this step, the data is cleaned and cleared of errors, 
mistakes  and  incomplete  data.  Methods  such  as  removing  duplicate 
data, compensating for missing data, converting data format, using data 
cleaning techniques and correcting invalid data can be used.

Selecting  and  extracting  features:  In  this  step,  the  important  and 
required features for analysis and modeling are extracted from the data. 
These  attributes  can  include numerical  attributes  such  as  mean,  vari-
ance, and categorical attributes such as product type, customer gender, 
etc. The correct selection of features is very important in data analysis 
and can have a great impact on the accuracy and efficiency of prediction 
models.

Data transformation and preparation: In this step, data is prepared

4

---

<!-- PAGE 5 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Fig. 3. Proposed research model.

for use in modeling. This includes converting the data into a suitable 
format for data mining algorithms, normalizing the data, reducing the 
dimensionality of the data, as well as dividing the data into two sets of 
training and testing. By performing the data collection and preparation 
steps  correctly,  the  data  will  be  ready  to  be  used  in  modeling  and 
analysis. This makes it more efficient to use the data and obtain more 
accurate and reliable results.

3.1.4. Modeling phase

The modeling phase in the CRISP methodology is the stage in which 
prediction,  classification  or  clustering  models  are  created  from  the 
collected and prepared data. The purpose of these models is to explain 
the patterns in the data and also to predict the behavior and events in the 
future. The main stages of the modeling phase are:

Selection of algorithms: In this step, based on the type of analysis 
desired (such as prediction, classification, or clustering) and the char-
acteristics of the data, suitable algorithms are selected for modeling. In

5

---

<!-- PAGE 6 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

other words, the type of problem and the nature of the data will deter-
mine the choice of algorithms.

Building models: In this step, using the selected algorithms, different 
models  are  created  on  the  data.  These  models  can  include  statistical 
models  such  as  regression  and  factor  analysis,  machine  models  and 
adaptive models such as clustering algorithms.

Training  and  evaluation  of  models:  The  built  models  are  trained 
using  training  data  and  then  evaluated  using  test  data.  Evaluation  of 
models  includes  criteria  of  accuracy,  correctness,  recall  and  other 
related  criteria. If needed, the models are  improved and  retrained by 
changing the parameters.

Selection  of  the  final  model:  After  evaluating  the  models  and 
comparing their performances, the model that has the best performance 
and  meets  the  analytical  needs  is  selected  as  the  final  model.  Using 
CRISP methodology in the modeling phase helps researchers to use data 
in a structured and step-by-step manner and to create acceptable and 
reliable models for data analysis.

3.1.5. The criterion phase of measurement and model evaluation

Model measurement and evaluation criteria in CRISP methodology 
are used to evaluate the performance of built models. These criteria are 
determined based on the problem under investigation and are usually 
used  for  prediction  and  classification  models.  Some  of  the  commonly 
used criteria are as follows:

aggregated  based  on  monthly  intervals.  Time  series  related  to  each 
variable for the customer are calculated. The definition of time series for 
the variables of transaction recency, number of transactions, transaction 
profit, and customer cost are as follows.

• Transaction Recency (t): The number of months that have passed

since the customer’s last transaction in a specified time period.

• Transaction Frequency (t): The number of transactions conducted

with the card reader during the specified time period.

• Transaction Profit (t): The amount of revenue generated from the

customer’s transactions during the specified time period.

• Customer Lifecycle Costs (t): The costs incurred by the organiza-
tion for the services and products provided to the customer during 
the  specified  time  period.  These  costs  include  expenses  for  card 
reader rolls, periodic visits, costs related to technical or consulting 
services,  costs  associated  with  the  use  of  specific  equipment  and 
technologies, and other related service provision costs.

In  this  methodology,  customer  behavior  analysis  is  performed 
considering four features: transaction recency, number of transactions, 
transaction  profit,  and  customer  cost.  This  comprehensive  approach 
allows for the examination of the impact of each of these features on 
customer behavior.

Accuracy: the ratio of the number of correct samples predicted by

3.3. Weighting features using a genetic algorithm

the model to the total number of samples.

Accuracy: The ratio of the number of real positive samples correctly 
identified by the model to the total number of positive samples predicted 
by the model.

Recall: The ratio of the number of true positive samples correctly 
identified by the model to the total number of positive samples in the 
data.

In this stage, a genetic algorithm is used to weight the features in 
time series clustering. The objective of this process is to find an optimal 
set  of  weights  that  appropriately  assign  importance  to  the  features 
during  clustering.  Using  these  weights  allows  for  more  precise 
clustering.

F-measure: A measure that is a combination of precision and recall

3.4. Time series clustering

and is used to balance the two measures.

Confusion  matrix:  a  table  that  shows  the  number  of  correct  and 
incorrect samples predicted by the model and is used as an evaluation 
tool in classification problems.

The area under the performance characteristic curve: This measure 
is used for classification models and indicates the ability of the model to 
distinguish between two different categories. Each of these criteria can 
be used to evaluate the performance of the models depending on the 
need  and  the  problem  under  investigation.  Also,  by  combining  these 
criteria and using other criteria, a more comprehensive evaluation of the 
models can be done.

3.1.6. Deployment phase

The development phase in CRISP methodology is the last phase of 
data mining research. In this phase, the models built by the researchers 
in the previous phases are used and used for the required predictions and 
analyses.  In  this  phase,  after  building  the  models  and  training  them 
using  the  training  data,  the  models  are  evaluated  using  the  test  or 
validation data. If the performance of the models is acceptable, they are 
used for use in the project or real applications. If the performance of the 
models  does  not  reach  the  desired  results,  researchers  may  need  to 
change the parameters, change the algorithms or use better and more 
suitable data to improve the performance of the models. Finally, after 
ensuring the performance of the models, they can be used for further 
predictions and analysis in projects and business decisions. As the final 
stage,  this  phase  shows  the  results  and  benefits  obtained  from  data 
mining research in real applications and plays a very important role in 
evaluating the effectiveness of research.

3.2. Representing customer behavior as recency, frequency, monetary, 
and cost (RFMC) time series

In  this  stage,  transactional  data  of  customers,  timestamped,  are

Time  series  clustering  is  an  analytical  method  that  allows  for  the 
grouping of  similar time series into  separate clusters. In this  method, 
time series are first extracted as samples of temporal data. Then, using 
appropriate  distance  metrics,  the  distances  between  time  series  are 
calculated.  These  metrics  can  include  Euclidean  distance,  Manhattan 
distance, and other similar measures based on the characteristics of the 
time series (Batista et al., 2014). Subsequently, four powerful clustering 
algorithms—hierarchical,  spectral,  K-means,  and  fuzzy  C-means  are 
employed for clustering.

3.5. Selecting the best clustering result by calculating Silhouette and 
Calinski-Harabasz indices

At this stage, after segmenting customers using various combinations 
of  algorithms  and  feature  weights,  the  quality  of  the  segmentation 
models  needs  to  be  evaluated  using  appropriate  clustering  validity 
indices. Clustering is an unsupervised method that aims to divide data 
into segments with high internal similarity and low inter-segment sim-
ilarity  (Arbelaitz  et  al.,  2014).  Internal  clustering  validity  indices 
examine how similar data points within each group are to each other, 
helping to select the best clustering result.

3.6. The main stages of the proposed methodology

3.6.1. Labeling and analyzing the behavior of each customer group

In  this  stage,  each  of  the  resulting  clusters  is  labeled,  and  the 
behavior of each group is examined to identify their dominant patterns 
over time. To summarize the main steps of the proposed methodology, 
Fig. 3 has been drawn. This model receives customer transactions with 
timestamps  as  inputs  and  creates  a  time  series  of  features  for  each 
customer, representing their behavior over time. Then, using a genetic 
algorithm,  appropriate  weights  for  each  feature  are  extracted,  and

6

---

<!-- PAGE 7 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

customer  segmentation  is  performed  through  time  series  clustering. 
Specifically, various combinations of algorithms and feature.

Table 2 
Sample data used in the research.

Data mining is a process that uses various techniques and algorithms 
to extract patterns, trends and useful information from a large volume of 
data. This process involves examining data, identifying hidden patterns 
and connections that can be used in decision making, forecasting and 
optimization. The main goal of data mining is to discover hidden pat-
terns and relationships that can be used to make decisions, make pre-
dictions,  and  improve  performance.  This  process  generally  includes 
steps  such as  data preprocessing, feature selection,  pattern discovery, 
and model evaluation. Data mining is used in various fields to obtain 
useful information and make decisions based on data (Sivaguru, 2023).
In this research, SQL Server software was used to extract data from 
the database. First, the required data was extracted from the database 
using SQL Server. Then, using the Python programming language and 
developing  the  corresponding  codes,  the  data  were  processed  and 
analyzed. This processing includes the use of Python libraries related to 
data mining.

In this research, various data mining techniques were used. These

techniques include.

• Data preprocessing to prepare the data for the next steps.
• Extracting important features related to changes and time patterns.
• Extracting the proper weight of features using genetic algorithm.
• Data clustering using clustering algorithms.
• Evaluation of clusters using Silhouette and Kalinsky criteria.
• Analyzing  customer  behavior  and  labeling  customers  based  on

clusters and forming specific groups.

weights are explored to find the best clustering model according to 
the clustering validity index. Finally, the resulting clusters are analyzed 
to reveal their dominant patterns over time.

4. Empirical study

This  section  presents  a  real-world  example  of  implementing  the 
proposed framework using data from a banking payment service com-
pany.  The  proposed  framework  and  all  its  components  have  been 
implemented using Python 3.7. The input data consists of 30 months of 
transactional data from card reader devices, including information such 
as  card  reader  ID,  transaction  ID,  date,  and  transaction  amount.  This 
dataset  comprises  195,844,085  detailed  purchase  transactions  by 
customers.

4.1. Data description

4.1.1. Software and implementation environment

In  this  research,  two  popular  and  powerful  softwares,  Python  and 
structured  query  language,  have  been  used  to  implement  customer 
segmentation models. Python programming language has been used as 
the main language for data analysis and running algorithms. By having 
various libraries and useful capabilities for data mining, Python helps to 
analyze customer data and perform segmentation with high accuracy. 
Also, a structured query language database has been used to store and 
manage customer data. Using a structured query language, information 
about  customers  is  stored  in  tables  and  used  for  data  extraction  and 
processing.

In this research, the database of a famous and large Iranian payment 
service provider company has been used. This data includes 195844058 
transaction  records  of  48948  customers  of  this  electronic  payment 
company in the historical period of thirty months. Some of these data are 
shown in Table 2. Each row of this table represents a customer. There are 
30 records for each customer for a 30-month period, considering that 30 
months of each customer have been used in a time series. The profit that 
reaches the organization from each customer transaction is collected in 
the period of one month and is placed in the transaction profit column.

7

Terminal 
number

Profit from the 
transaction

Number of 
transactions

Transaction 
recency

Customer 
cost

123456
678901
234567
890123

247000
342000
987000
102000

323
409
711
167

0
2
1
5

22000
123000
187000
145000

The  number  of  transactions  includes  the  number  of  customer  trans-
actions  in  a  month,  and  the  transaction  freshness  is  the  number  of 
months  that  have  passed  since  the  last  customer  transaction.  In  the 
beginning, the transactional data of customers were small and detailed, 
but due to the large volume of data and the complexity of the processing 
operations, the data were analyzed in the form of monthly summaries. 
By collecting and aggregating data, monthly data can be used to check 
the behavior of each customer in a time series. In this process, four main 
features  are  used,  including  the  number  of  transactions,  transaction 
freshness,  transaction  amount,  and  customer  cost.  The  customer  cost 
feature is calculated from the amount of roll consumed, the cost of pe-
riodic visits and other services provided to the customer. Then, for each 
customer, the information related to the last thirty months from the four 
aforementioned features was extracted monthly and the necessary an-
alyzes  were  performed  on  the  data.  It  should  be  noted  that  all  the 
characteristics  of  the  customers  have  a  value  in  the  30-month  period 
under review, (Description of the data used in the research is shown in 
Table 3).

4.1.2. Data processing

Data processing is done to prepare and improve their quality before 
using them in the next steps. Regarding the data used in this research, 
due to the use of transaction data of banking customers, the data has 
been collected from a clean and complete database, so there is no need 
for special pre-processing because the data has been collected from a 
clean and correct database. But a normalization step has been applied to 
the data and a monthly summary of microtransactions has been done. 
This operation has been done in order to use the data more easily and 
optimally in the next steps.

4.1.3. Feature extraction

Important features have been extracted from the data. At this stage, 
meaningful and useful features have been extracted from the customer 
data  set, which  play  an important role  in  describing and  interpreting 
customer  behavior.  These  attributes  are  usually  determined  based  on 
transactional  data  including  transaction  count,  transaction  recency, 
transaction  amount,  and  customer  cost.  Using  these  features,  it  is 
possible to identify customer patterns and behaviors. Extracting features 
from customer data is a key step in the process of analyzing and seg-
menting customers, which provides more possibilities and capabilities to 
interpret and predict the future behavior of customers. To extract the 
number of transactions feature, the number of transactions performed

Table 3 
Description of the data used in the research.

Feature

Description of the feature used

Transaction recency

Number of

transactions
Profit from the 
transaction

Customer cost

The number of months passed since the customer’s last 
transaction within a month is checked, the lower the better.
The number of transactions that a customer has reviewed 
within a month, the higher this feature is, the better.
The amount of profit obtained from a customer’s 
transactions in a period of one month, the higher this 
feature, the better.
The amount of money that the organization pays for a 
customer in a period of one month, this cost includes 
periodical visits, consumption roll and other services 
provided to the customer. The less this feature, the better.

---

<!-- PAGE 8 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

by each customer in a certain period of time is considered. To extract the 
transaction recency feature, the elapsed time since the last transaction 
performed by each customer is considered. To extract the transaction 
profit  feature,  the  total  profit  of  all  transactions  performed  by  each 
customer in a certain period of time is calculated from the transaction 
amount.  Finally,  to  derive  the  customer  cost  attribute,  the  total  cost 
amount  that  the  customer  received  for  the  services  and  products  is 
calculated.  Feature  extraction  has  been  done  on  customer  data  using 
calculations and operations appropriate to each feature. These features 
are then used in the next stages of customer segmentation to describe 
and interpret customer behavior.

4.1.4. Data normalization

The  purpose  of  data  normalization  is  to  create  conditions  where 
features are equal based on their importance and impact in analyzing 
and segmenting customers. This work helps to facilitate the process of 
data interpretation and analysis and increases the accuracy and usability 
of  the  analysis  results.  This  is  in  order  to  remove  any deviations  and 
differences in sizes between features and to create a balanced distribu-
tion  of  data.  Outliers  were  removed  before  data  normalization.  The 
outlier data were removed in such a way that only those customers who 
had  transactions  in  at  least  twenty  months  remained.  Then,  the  data 
were  normalized  using  the  MinMax  normalization  method.  In  this 
method, the feature values are normalized to a certain interval, usually 
between 0 and 1. There are different methods for data normalization, 
but  in  this  research,  the  min-max  normalization  method  was  used 
because the min-max method places the data values in a certain range, 
which made the data comparable and hence The impact of data drift on 
the final results is reduced. Also, by examining the literature review in 
the second chapter, it was observed that this normalization method is 
one  of  the  most  common  normalization  methods  used in  the  articles. 
Therefore,  according  to  the  advantages  and  literature  review,  it  was 
decided to use the Min-Max method for data normalization. 
Min max normalization = X (cid:0) Xmin
Xmax (cid:0) Xmin

(1)

In this formula, X represents the initial value of the feature. Xmin is the 
minimum feature value in the data and Xmax is the maximum feature 
value in the data. Using this formula, the features are normalized be-
tween the interval [0, 1].

4.1.5. Evolutionary algorithms

Evolutionary  algorithms  include  several  sub-branches.  One  of  the 
commonalities  between  these  algorithms  is  that  the  input  of  each  of 
these  algorithms  is  a  population  of  people.  The  pressure  of  the  envi-
ronment makes the most appropriate and compatible person with the 
environment  to  be  selected  as  the  final  solution.  For  this  purpose,  a 
quality  function  is  considered  for  each  person  in  the  population.  The 
general goal of these algorithms is to increase the value of the quality 
function related to each person and select the person with the highest 
quality function as the most compatible person from the population. The 
higher the value of the quality function, the more compatible that person 
is with the surrounding environment. Based on this function, individuals 
are selected as parents to produce the next generation. The act of pro-
ducing children is done by two operators, mutation and combination, 
which are applied to the parents. The act of compounding is an act that is 
applied to two parents and is created by those two children. The mu-
tation operator is performed only on a parent and a child is produced by 
it. The two operators of combination and mutation cause the emergence 
of new people in the society. Now these new people will compete with 
the  old  people  of  the  society  to  be  in  the  next  generation.  that  this 
competition  is  based  on  their  quality  function.  This  procedure  is 
repeated  until  the  person  with  the  appropriate  quality  function  is 
selected as a solution to the problem (Christy et al., 2018).

In evolutionary algorithms, a random optimization occurs, which is

modeled on evolution in nature and two main heuristics are obtained in 
these algorithms.

-  Survival of the fittest: It is important in the selection operator in such 
a way that the one who is the strongest has more chance of survival 
and has more possibility for mating.

-  Recombination:  by  combining  in  the  answer,  we  can  hope  to  get 
better answers. One of the characteristics of the evolutionary algo-
rithm is that it is blind, so that it does not see its way, and the only 
thing  it  needs  is  to  be  given  the  possibility  to  evaluate  its  perfor-
mance, because if it can evaluate its performance, it can find its way. 
Another feature is that it simplifies the problem and uses a series of 
codes to make decisions, which are generally binary, but there are 
other types as well (Emami & Derakhshan, 2015).

4.2. Representing customer behavior as RFMC time series

In this stage, the data was first normalized using min-max normali-
zation.  Then,  the  transactional  data  was  aggregated  into  monthly  in-
tervals. Based on the definitions of the RFMC variables, the R, F, M, and 
C time series for each month were extracted. Since all selected customers 
have  transactions  in  every  month,  the  R  variable  will  be  zero  for  all 
customers. Therefore, the R variable is not considered in the analyses as 
it  does  not  contribute to  distinguishing customer  segments. Addition-
ally, the transaction frequency of each customer indicates the number of 
transactions made by each customer. It is also evident that the monetary 
value of each transaction can vary. Thus, a high number of transactions 
does not necessarily equate to high monetary value. For this reason, the 
monetary variable is considered as the profit from the transaction rather 
than the transaction amount for analyzing customer behavior. The ul-
timate  goal  of  any  company  is  to  achieve  optimal  profitability.  In 
customer  segmentation,  the  cost  feature  is  also  considered.  In  the 
examined  sample,  which  includes  card  reader  transactions,  the  costs 
Incurred by customers during their relationship with the organization 
are  taken  into  account.  These  costs  include  expenses  for  card  reader 
rolls, periodic maintenance visits, card reader malfunctions, and other 
costs borne by the organization for its customers. By considering cost in 
customer segmentation, groups of customers with similar cost patterns 
can be identified, allowing for optimal strategies to manage costs and 
enhance organizational efficiency.

4.3. Weighting features using a genetic algorithm

In the feature weighting stage, a genetic algorithm is used to deter-
mine the appropriate weights for the features. The genetic algorithm is a 
computational  method  inspired  by  the  mechanisms  of  evolution  and 
natural  selection  in nature.  Using this algorithm,  suitable  weights for 
each feature are extracted to optimize their impact on customer analysis 
and segmentation. In this stage, after data preparation, the genetic al-
gorithm is applied. The genetic algorithm uses an evolutionary process 
to  identify  the  best  weight  for  each  feature.  Initially,  a  population  of 
weights is generated. Then, through the use of crossover and mutation 
operators, subsequent generations are created. In each generation, the 
weights are improved and adjusted based on an evaluation function to 
meet the optimal weight for each feature (Dunn, 1973).

After  running  the  genetic  algorithm  and  gradually  improving  the 
weights,  the  best  weight  values  for  each  feature  are  extracted.  This 
method uses a linear combination of features, meaning that the features 
are combined with different weights to obtain a final value for customer 
analysis  and  segmentation.  The  permissible  values  for  these  features 
range between [(cid:0) 1, 1], meaning that the weights for the features are 
between one and negative one. The values associated with the param-
eters of the genetic algorithm used are presented in Table 4.

The genetic algorithm was implemented using four clustering algo-
rithms: hierarchical, spectral, K-means, and fuzzy C-means, resulting in 
four  output  charts  corresponding  to  each  fitness  function.  Figs.  4–7

8

---

<!-- PAGE 9 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Table 4 
Describes the genetic algorithm optimization parameters.

Parameter Name

Parameter Description

Maximum Number of

Generations

Number of Individuals per

Generation

Mutation Probability

Elitism Ratio

Crossover Probability

Selection Ratio

Type of Crossover

Maximum Number of 
Generations without 
Improvement

The maximum number of generations 
that the genetic algorithm should run. 
After reaching this number of 
generations, the optimization operation 
stops.
The number of people (population) in 
each generation from the genetic 
algorithm,
The probability of performing mutation 
operations on each gene in each 
mutation generation means the random 
change of one bit of the gene at a certain 
point.
A proportion of the population that is 
passed on to the next generation as 
superior individuals (elite) and is 
excluded from the operations of 
combination and mutation.
Probability of combining operations on 
two individuals from the population. 
Fusion means combining different parts 
of two people to create a new person.
A proportion of the population used to 
select a parent for inclusion in the next 
generation.
The type of composition used in the 
composition operation may be uniform 
composition or other types.
The maximum number of generations 
during which no improvement in 
optimization has been made. This 
parameter can be useful to stop the 
algorithm if there is no improvement.

Value

100

200

0.1

0.01

0.5

0.3

uniform

None

Fig. 5. Output of the genetic algorithm with spectral fitness function.

Fig. 6. Output of the genetic algorithm with fuzzy C-means fitness function.

Fig. 4. Output of the genetic algorithm with K-means fitness function.

represent the performance of the genetic algorithm in segmenting cus-
tomers using each of these algorithms. Based on the outputs obtained 
from  these  charts,  the  spectral  clustering  algorithm  performed  with 
higher  accuracy  compared  to  the  other  algorithms.  Therefore,  to 
improve  clustering  accuracy,  the  spectral  algorithm  and  the  weights 
provided by it were used. These results indicate that the genetic algo-
rithm,  with  the  fitness  function  calculated  by  the  spectral  algorithm, 
offers greater capability in customer segmentation, contributing to the 
increased  accuracy  and  efficiency  of  the  segmentation  process.  Addi-
tionally, the best solution found by the genetic algorithm for weighting 
features  is  as  follows:  the  weights  for  the  three  features—number  of 
transactions,  transaction  profit,  and  cost—are  (cid:0) 0.70,  0.80,  and  0.90, 
respectively,  and  the  objective  function  is  0.91  for  the  spectral  algo-
rithm. In subsequent steps, the weights are multiplied by the features, 
and clustering is performed with the new values.

Fig. 7. Output of the genetic algorithm with hierarchical fitness function.

The general and comparative explanations of these charts are briefly 
presented  in  Fig.  8 so  that  the  results  and  evaluations  are  clearly 
understandable.

By using the genetic algorithm and the fitness function calculated by 
the Spectral algorithm, the best accuracy for customer segmentation was 
obtained. To compare the results, a bar graph has been drawn that shows 
the  segmentation  accuracy  using  different  algorithms  (K-Means,  hier-
archical and fuzzy C-Means) along with the Spectral algorithm. The bar 
chart  shows  that  by  using  the  genetic  algorithm  and  the  spectral  fit 
function, the accuracy of the segmentation has been improved and they 
have provided a significant improvement compared to other algorithms. 
This  means  that  the  genetic  algorithm  with  the  fitness  function

9

---

<!-- PAGE 10 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Fig. 8. The comparative diagram of the implementation of the genetic algorithm with different fitness functions.

calculated by the Spectral algorithm provides the best ability to segment 
customers and increases the accuracy and efficiency of the segmentation 
process. The best solution found by the genetic algorithm is as follows:

Table 5 
Dunn index calculation results.

Optimal Number of Clusters

Dunn Index

Weights: [-0.70162901, 0.80858289,0.901110443]

and the value of the objective function: 0.91.

The  genetic  algorithm  has  been  able  to  provide  a  high-accuracy 
clustering  model  by  optimally  assigning  the  weights.  The  value  of 
Don’s index obtained indicates a very good fit of the clustering with the 
data and a suitable separability between the clusters. This means that 
the optimal weights obtained by the genetic algorithm well represent the 
features in customer clustering and the resulting clustering model pro-
vides  more  accurate  results.  Then,  using  these  optimal  weights,  clus-
tering  algorithms  were  implemented  and  customers  were  segmented. 
These optimal weights have managed to adjust and select the best fea-
tures  for  clustering  customers.  The  result  of  clustering  with  these 
weights can be seen in the clustering section. Using these results, it can 
be  claimed  that  the  genetic  algorithm  with  selected  parameters  has 
succeeded in finding the optimal weights for customer clustering, and 
the resulting clustering is more accurate and better than before.

4.4. Time series clustering

After normalizing the data and weighting the features using a genetic 
algorithm,  the next step is customer segmentation using four popular 
algorithms  identified  in  the  literature  review.  The  prepared  data  is 
segmented  using  spectral,  hierarchical,  fuzzy  C-means,  and  K-means 
algorithms, and the best algorithm is identified based on the Silhouette 
and Calinski-Harabasz indices.

The optimal number of clusters for customer segmentation is deter-
mined using the Dunn index. The Dunn index is a quantitative measure 
that determines the optimal number of clusters based on the distance 
between  clusters  and  within  clusters.  By  calculating  this  index  for 
different numbers of clusters, the optimal number of clusters is obtained. 
The  higher  the  Dunn  index  value,  the  better  the  clustering  results 
(Alboukaey et al., 2020). The different Dunn index values calculated are 
shown  in  Table  5.  Additionally,  the  changes  in  the  Dunn  index  are 
illustrated in Fig. 9, where the highest Dunn index value is obtained for 
three clusters.

2
3
4
5
6
7
8
9

0.4190
0.4411
0.3983
0.4257
0.4268
0.4006
0.3997
0.3987

Fig. 9. Dunn index variation chart based on the number of clusters.

4.5. Selecting the best clustering result by calculating Silhouette and 
Calinski-Harabasz indices

In this stage, the accuracy of clustering is improved using a genetic 
algorithm. Initially, before applying the genetic algorithm, clustering is 
performed using four algorithms: spectral, hierarchical, fuzzy C- means, 
and  K-means.  Then,  after  executing  the  genetic  algorithm  with  opti-
mized weights, another round of clustering is conducted using the same 
four algorithms.

The  quality  of  clustering  is  evaluated  using  the  Silhouette  and 
Calinski-Harabasz  indices.  This  comparative  analysis  shows  that  the

10

---

<!-- PAGE 11 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

genetic  algorithm  with  optimized  weights  brings  significant  improve-
ment in clustering accuracy.

4.5.1. Segmentation using K-Means algorithm

In customer segmentation using K-Means algorithm, a method called 
K-Means is used to divide customers into different groups. In this algo-
rithm, first a number of primary centers (cluster centers) are determined 
and  customers  are  assigned  to  the  closest  cluster  center.  The  cluster 
centers  are  then  updated  based  on  the  average  number  of  customers 
assigned to them, and the customers are reassigned to the nearest cluster 
center. This process is repeated repeatedly until a stable state is estab-
lished and the cluster centers do not change. The K-Means algorithm has 
advantages  such  as  simplicity  and  relatively  high  speed  compared  to 
other algorithms for data segmentation. This algorithm is generally used 
in clustering problems and is considered as one of the most used and 
popular  algorithms  in  this  field  (Christy  et  al.,  2018).  The  results  of 
customer  segmentation  using  the  K-Means  algorithm  on  the  analyzed 
data are shown in Table 6.

4.5.2. Segmentation using C-Means fuzzy algorithm

Fuzzy C-Means (FCM) algorithm is a clustering algorithm used for 
data segmentation using a fuzzy approach. In this algorithm, each data is 
probabilistically  assigned  to  one  or  more  clusters,  instead  of  being 
explicitly  assigned  to  a  cluster.  In  the  C-Means  fuzzy  algorithm,  the 
centers of the clusters are initialized randomly. Then, for each data, the 
probability of belonging to each cluster is calculated using the concept of 
fuzzy membership. These membership probabilities are then weighted 
to update the cluster centers. This process is repeated until the changes 
in the cluster centers are less than a threshold value. The advantages of 
C-Means  fuzzy algorithm include the ability to model fuzzy data pat-
terns,  the ability to simultaneously assign to several clusters, and the 
ability to apply it to data with a complex structure (Hamidi & Vafaei, 
2009). The results of customer segmentation using the C-Means fuzzy 
algorithm on the analyzed data are shown in Table 7.

4.5.3. Segmentation using spectral clustering algorithm

The spectral clustering algorithm is a clustering algorithm based on 
the spectral analysis of graphical information from the data. In order to 
segment  the  data,  this  algorithm  uses  the  information  of  the  graph 
structure and places the data in different clusters based on the spectral 
characteristics of the graph. The performance of the spectral clustering 
algorithm is that first a graph is created for the data. Then the graph 
spectrum is calculated and clustering is done using the graph spectrum. 
For  this  purpose,  first  the  eigenvectors  corresponding  to  the  smallest 
values of the graph spectrum are extracted and then these vectors are 
used  as input  for the clustering algorithm,  such as the K-Means algo-
rithm.  The  main  advantage  of  spectral  clustering  algorithm  is  in 
modeling  and  clustering  data  with  complex  structure.  This  algorithm 
can identify hidden patterns in the data and carry out accurate clustering 
according to the structural information of the data (Luo et al., 2023). 
The results of customer segmentation using the spectral clustering al-
gorithm on the examined data are shown in Table 8.

4.5.4. Segmentation using hierarchical algorithm

Hierarchical  algorithm  is  a  clustering  algorithm  based  on  the  for-
mation of a hierarchy of clusters. In this algorithm, first each point is 
considered  as  a separate  cluster. Then, using the  distance criteria be-
tween the points, the clusters are ranked and hierarchically connected to

Table 7 
Results of C-Means fuzzy algorithm implementation before and after applying 
genetic algorithm weights.

Evaluation criteria

Before genetic algorithm

After genetic algorithm

Silhouette index
Calinski index

0.43
8523

0.67
16884

Table 8 
Results  of  spectral  clustering  algorithm  implementation  before  and  after 
applying genetic algorithm weights.

Evaluation criteria

Before genetic algorithm

After genetic algorithm

Silhouette index
Calinski index

0.43
7596

0.91
17307

each other to finally reach a single large cluster. Hierarchical algorithm 
works in such a way that in each step, two closer clusters are combined 
with each other and become a larger cluster. This combination of clus-
ters is done based on the criteria of the distance between the clusters. 
Distance measures may include Euclidean distance, Manhattan distance, 
or any other distance measure chosen based on the properties of the data 
and the clustering problem. The main advantage of the hierarchical al-
gorithm is the ability to represent the hierarchy of clusters. This algo-
rithm is able to divide points into different clusters and also display the 
hierarchical  structure  between  these  clusters  (Christy  et  al.,  2018; 
Çavdar &  Ferhatosmano˘glu, 2018). The results of customer segmenta-
tion using the hierarchical algorithm on the analyzed data are shown in 
Table 9.

4.6. Comparison of customer segmentation models

The comparison of customer segmentation models using genetic al-
gorithm  and  without  using  genetic  algorithm  has  been  discussed.  In 
order to check more precisely which model performed best in customer 
data analysis and to what extent the genetic algorithm was effective in 
improving clustering. All customer segmentation algorithms that were 
introduced in the previous sections are compared with each other and 
the best segmentation model is determined using two criteria, Silhouette 
and Kalinsky. To compare segmentation models, two criteria, Silhouette 
and  Kalinsky,  have  been  used.  The  silhouette  measure  measures  the 
degree of separation and integration between clusters. This measure is 
calculated based on the distance between samples within the cluster and 
the distance between samples in adjacent clusters. The silhouette value 
for each cluster ranges from (cid:0) 1 to 1, with higher values indicating better 
separation between clusters (Khajvand et al., 2011). 
Silhouette(i) = b(i) (cid:0) a(i)

(2)

max (a(i), b(i))

b: indicates the minimum average distance between points from a 
cluster that are not clustered to other points from adjacent clusters.
a:  represents  the  average  internal  distances  of  the  points  of  each 
cluster to the reference point (the central point of the cluster).

Calinski’s criterion measures the number of clusters and the quality 
of separation between clusters. This measure is calculated based on the 
difference between the internal average of the clusters and the average

Table 6 
K-Means algorithm implementation results before and after genetic algorithm 
weights are applied.

Table 9 
Results  of  the  implementation  of  the  hierarchical  algorithm  before  and  after 
applying the weights of the genetic algorithm.

Evaluation criteria

Before genetic algorithm

After genetic algorithm

Evaluation criteria

Before genetic algorithm

After genetic algorithm

Silhouette index
Calinski index

0.44
8608

0.67
15574

Silhouette index
Calinski index

0.39
7360

0.66
15373

11

---

<!-- PAGE 12 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

between  the  clusters. A high value  of this criterion  indicates that the 
clusters  are  separate  and  the  segmentation  quality 
is  better 
(ABBASIMEHR & BAHRINI, 2022).

Calinski Harabasz = b
w

+ N (cid:0) k
k (cid:0) 1

(3)

bindicates the interclusterity of the data and is calculated as the sum 
of  the  squares  of  the  distances  between  the  central  points  of  the 
clusters and the central point of the entire data. w indicates that the 
data are within a group and in sum

The  square  of  data  distances  is  calculated  from  the  center  of  the 
cluster  to  which  they  belong.  N  represents  the  total  number  of  data 
points. K represents the number of clusters.

Figs.  10–13 compare  the  Silhouette  and  Calinski-Harabasz  indices 
for the different algorithms before and after executing the genetic al-
gorithm. These charts illustrate a marked increase in the values of the 
Silhouette  and  Calinski-Harabasz  indices for  all  algorithms after opti-
mization by the genetic algorithm. This increase indicates better cluster 
segmentation after the genetic algorithm’s optimization. The results of 
the  Silhouette  and  Calinski-Harabasz  indices  show  that  the  spectral 
clustering algorithm performed with higher accuracy compared to the 
other  algorithms.  Therefore,  for  further  improvement  and  increased 
clustering  accuracy,  customer  segmentation  was  continued  using  the 
spectral algorithm.

According to the values of Silhouette and Calinski criteria for each 
algorithm and comparing them with each other, the best segmentation 
model for customers is the Spectral algorithm because it has the highest 
Silhouette and Calinski values.

4.6.1. Customer segmentation using genetic algorithm

By using genetic algorithm, optimal weights were obtained for the 
attributes of transaction number, transaction profit and customer cost. 
Then, using these optimal weights, the clustering algorithms were re-run 
with the same previous conditions, and it is shown in Figs. 12 and 13
that  the  clustering  models  with  optimal  weights  have  improved 
compared to the models without using optimal weights, and the accu-
racy and efficiency of clustering have improved.

4.7. The results of the implementation of the spectral algorithm with the 
optimal weights of the genetic algorithm

According to the values of silhouette and Kalinsky criteria for each 
algorithm and comparing them with each other, the best segmentation 
model for customers using genetic algorithm weights is Spectral because 
it has the highest silhouette and Kalinsky values compared to other al-
gorithms. For this reason, customer segmentation has been done using 
the Spectral algorithm and the optimal weights of the genetic algorithm, 
and the results are shown in Table 10.

In Table 10, the number of samples in each cluster is shown. Each 
row of this table represents a cluster and each column represents the 
number of samples in the same cluster. This information tells us how 
many customers each cluster contains and how large it is in terms of 
number of instances.

In  Table  11,  a  statistical  summary  of  the  data  in  each  cluster  is 
shown.  These  characteristics  can  include  mean,  variance,  median, 
minimum value, maximum value, etc. This information shows us how 
the customers of each cluster performed on various attributes (such as 
number  of  transactions,  transaction  profit,  and  customer  cost)  and 
whether these customers differ from each other on these attributes. Also, 
this table can provide information about the distribution of data in each 
cluster, and this information can be used in data analysis and review.

Fig. 14 shows the graph of changes in the average values of all three 
characteristics of transaction profit(a), transaction number(b) and cost 
(c) based on clustering groups. In this diagram, each clustering group is 
displayed with a specific color. The x-axis of the graph shows the dates, 
and the y-axis of the graph shows the average attribute values for each 
group on each date. By looking at this graph, you can see the changes in 
the average values of the features for each of the groups over time. This 
graph shows how the clustering groups’ performance has changed over 
time  and  whether  their  average  attribute  values  have  increased  or 
decreased.  Also, by  comparing  different groups, it  can be seen  which 
group had the best performance in terms of the average values of the 
features. In which periods of time there were visible changes and this 
information was used in the analysis and review of customer data.

4.8. Labeling each customer segment and analyzing the behavior of each 
group

This  section  of  the  paper  analyzes  different  customer  groups.  By 
calculating the center of each group, the temporal information of that 
segment is identified. Figs. 15–17 show line charts of the average values

Fig. 10. Comparison chart of accuracy of clustering algorithms with Silhouette criterion without genetic algorithm.

12

---

<!-- PAGE 13 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Fig. 11. Comparison chart of accuracy of clustering algorithms with Calinski criterion without genetic algorithm.

these two features, Group 2 ranks third, as customers in this group have 
the lowest share of transactions and profit compared to the other groups. 
On the other hand, it is observed that the cost for customers in Group 2 is 
lower than in the other two groups. This result indicates that Group 2 is 
the  best  group  in  terms  of  cost.  After  Group  2,  Group  3  comes  next, 
followed by Group 1. This point shows that, on average, customers in 
Group 2 conduct their transactions at a lower cost compared to the other 
two groups. Table 12 shows the behavioral analysis of each customer 
group. By analyzing these features and the associated statistical values 
for each group, one can better understand the differences and advan-
tages of each group in the business, leading to better decision-making 
regarding  strategies  and  customer  retention.  Additionally,  time  is  a 
crucial factor in this analysis. According to Figs. 15–17, which show the 
average values by group, it can be observed that customers in Group 3 
have  exhibited  consistent  and  balanced  behavior  over  the  30-month 
period studied. This indicates their loyalty. Customers in Group 2 had 
high profits and transactions in the initial months, but after some time, 
these values decreased, indicating that they are on the verge of being 
lost. This point highlights the need to adopt effective strategies to retain 
Group 2 customers and prevent their loss. Moreover, customers in Group 
1  had  few  transactions  initially  but  have  recently  shown  significant 
growth  and  have  become  profitable  customers.  Overall,  by  analyzing 
this statistical data and charts, one can better understand the differences 
and behaviors of each group and implement appropriate strategies to 
make necessary improvements and changes in the business.

5. Performance evaluation

This section evaluates the performance of the proposed framework,

divided into three subsections explained below.

5.1. Innovations of the research

One of the most significant innovations of this paper is that, unlike 
most previous methods that considered equal weights for the parameters 
of new purchase, purchase frequency, and purchase amount, this study 
uses a genetic algorithm to obtain optimal weights for customer features. 
In this model, by optimizing and adjusting weights using a genetic al-
gorithm,  various  features  are  appropriately  utilized  in  customer 
segmentation.

This research considers the cost feature in customer segmentation. In 
the examined sample, which includes card reader transactions, the costs 
incurred by customers during their relationship with the organization

Fig.  12. Comparison  chart  of  the  accuracy  of  clustering  algorithms  with  the 
Silhouette criterion with the genetic algorithm.

for  the  three features:  transaction profit,  number  of transactions, and 
cost,  based  on  the  clustering  groups.  In  these  charts,  each  feature 
transaction  profit,  number  of  transactions,  and  cost  is  displayed  in  a 
specific color. The x-axis represents the dates, and the y-axis represents 
the  average  values  of  the  features  for  each  group  on  each  date.  By 
observing these charts, one can see the changes in the average values of 
the features for each group over time. These charts illustrate how the 
performance  of  the  clustering  groups  has  changed  over  time  and 
whether  the  average  values  of  their  features  have  increased  or 
decreased. Additionally, by comparing different groups, one can deter-
mine  which  group  has  had  the  best  performance  in  terms  of  average 
feature  values,  observe  notable  changes  in  certain  time  periods,  and 
utilize this information for analyzing and reviewing customer data.

Fig. 18 displays the values of transaction features, profit, and cost for 
each of the clustered groups. In this chart, each column corresponds to a 
feature, and for each feature, 3 bars are drawn for groups one, two, and 
three, respectively. Each group is also distinguished by a different color. 
The  values  shown  in  this  chart  represent  the  average  values  for  each 
feature  for  each  group.  This  chart  generally  shows  how  each  group 
differs in terms of the examined features compared to the other groups. 
Based on this statistical information, it can be concluded that Group 3 
has  a  higher  average  number  of  transactions  and  transaction  profit 
compared to the other two groups. Therefore, this group consists of more 
active customers compared to the other two groups. Following Group 3, 
Group 1 has a higher share of transactions and profit overall. Based on

13

---

<!-- PAGE 14 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Fig. 13. Comparison chart of the accuracy of clustering algorithms with Calinski criterion and genetic algorithm.

Table 10 
The number of samples in each cluster of customers for k = 3.

Cluster number

Number of cluster samples

0
1
2

15513
3557
1814

Table 11 
Statistical summary of data in each cluster.

Second 
group

First

group

Zero

group

Number of 
transactions

Transaction 
Profit

Customer 
Cost

Count
mean
std
min
25%
50%
75%
max

30
0.58
0.3
0
0.42
0.62
0.81
1

30
0.64
0.31
0
0.51
0.73
0.87
1

30
0.55
0.3
0
0.43
0.60
0.75
1

Number of 
transactions

Transaction 
Profit

Customer 
Cost

Count
mean
std
min
25%
50%
75%
max

Count
mean
std
min
25%
50%
75%
max

30
0.40
0.32
0
0.09
0.34
0.69
1

30
0.40
0.32
0
0.10
0.37
0.72
1

30
0.43
0.34
0
0.12
0.42
0.69
1

Number of 
transactions

Transaction 
Profit

Customer 
Cost

30
0.48
0.33
0
0.11
0.55
0.75
1

30
0.49
0.34
0
0.10
0.59
0.77
1

30
0.56
0.40
0
0.06
0.78
0.92
1

are  taken  into  account.  These  costs  include  expenses  for  transaction 
rolls, periodic maintenance visits, card reader malfunctions, and other 
costs borne by the organization for its customers. By considering the cost 
feature in customer segmentation, the best strategies for cost manage-
ment and resource optimization can be found. Analyzing customer costs 
and  their  impact  on  the  organization’s  revenue  and  profit  can  help 
develop strategies to reduce costs. Moreover, it is possible to identify 
customer groups with similar cost patterns and provide optimal strate-
gies  for  managing  organizational  costs.  The  customer  segmentation 
model developed in this paper has been successfully implemented in an 
electronic payment company, delivering better results than the previous 
segmentation  model  used  by  the  company.  Thus,  this  model  is 
commercially viable and applicable in real-world scenarios.

5.2. Integrating the proposed framework into an information system for 
improved decision making

Some  of  the  applications  that  can  be  implemented  based  on  this

proposed approach include.

1.  Customer Segmentation: different behavioral groups of customers

can be analyzed over time.

2.  Customer Churn Detection: Identifying customers who are likely to 
churn  and  taking  appropriate  actions  to  retain  them  is  essential 
(Alboukaey  et  al.,  2020).  Recognizing  individuals  who  intend  to 
leave the customer list and taking suitable measures to retain them is 
crucial.  most  studies  in  the  field  of  churn  detection  are  based  on 
static approaches.

3.  Customer  Behavior  Prediction:  Predicting  customer  behavior  is 
critical  in  customer  relationship  management  (Montero-Manso  & 
Hyndman,  2021).  Robust  time  series  forecasting  methods  can 
become a valuable tool for managers. The main difference between 
this  approach  and  previous  research  is  its  exploitation  of  the  pre-
dictability feature.

5.3. Research limitations

The first limitation of the research was processing large volumes of 
data.  This  study  required  strong  hardware  resources  to  process  and 
analyze the extensive data. The second limitation is that only customer

14

---

<!-- PAGE 15 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Fig. 14. The linear graph of the average values of the features by features for each group.

transaction data was available; other information such as location, store 
size, and number of staff were not accessible for a more detailed analysis 
of the segments obtained.

6. Conclusion

In this paper, a customer segmentation model for dynamic segmen-
tation  based  on  modeling  customer  behavior  has  been  presented. 
Customer segmentation has been carried out by considering the entire 
customer lifetime from inception to the present, looking not only at past

behavior but also anticipating future behavior. Therefore, this research 
fully  accounts  for  the  customer  lifetime  in  segmentation.  This  study 
offers  a  dynamic  model  for  customer  segmentation,  capable  of  moni-
toring changes in customer behavior through time series clustering. This 
shift  from  static  to  dynamic  segmentation  enables  continuous 
improvement and adaptation to customer behavior. The study considers 
new purchases, purchase frequency, and purchase amount as a linear 
combination, without ignoring the relationships between these features. 
Using a genetic algorithm, optimal weights were assigned to customer 
features,  resulting  in  improved  segmentation  compared  to  previous

15

---

<!-- PAGE 16 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Fig. 15. Line Chart of the Average Values of Features for the first Cluster.

separability between clusters. This means that the optimal weights ob-
tained  by  the  genetic  algorithm  effectively  represent  the  features  in 
customer  clustering,  providing  more  accurate  results.  These  weights 
were used to execute clustering algorithms and perform customer seg-
mentation,  successfully  selecting  and  optimizing  the  best  features  for 
clustering. The results demonstrate that the genetic algorithm with the 
selected  parameters  successfully  found  optimal  weights  for  customer 
clustering,  resulting in  more accurate and improved  segmentation. In 
this study, a hybrid and efficient method for customer segmentation was 
achieved  using  the  genetic  algorithm  and  weight  optimization.  As 
shown in Table 13, the segmentation accuracy significantly improved 
compared to other methods. Additionally, the analysis revealed that the 
large  data  volume  (195,844,085  transactions  and  48,489  customers) 
provided comprehensive and extensive insights, resulting in more pre-
cise and reliable customer segmentation. Another distinguishing feature 
of this work is the inclusion of the cost feature in customer segmenta-
tion, unlike other studies that did not consider this feature. This research 
used a linear combination of features and analyzed customer data over 
30 months, while similar studies considered periods of seven to eleven 
months.  Therefore,  given  the  improved  segmentation  accuracy,  large 
data volume, inclusion of the cost feature, and extended analysis period, 
the results of this study are successful and effective, showing significant 
improvement over reference papers.

For  future  research,  the  scope  of  the  data  can  be  expanded  to 
include  other  customer  variables  such  as  geographic  location,  age,

Fig. 16. Line Chart of the Average Values of Features for The second cluster.

models.  The  innovations  of  this  research  include  modeling  customer 
segmentation based on behavioral changes over the customer lifetime, 
using time series analysis, considering cost features in segmentation, and 
the  ability  to  continually  improve  segmentation  based  on  behavioral 
changes. The model has been successfully implemented in an electronic 
payment company, yielding better results than the previous segmenta-
tion model. The genetic algorithm, by optimally weighting features, has 
provided a highly accurate clustering model. The obtained Dunn index 
indicates a very good fit of the clustering to the data and appropriate

Fig. 17. Line Chart of the Average Values of Features for the third cluster.

16

---

<!-- PAGE 17 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Fig. 18. Comparative chart of average feature values for each customer group.

Table 12 
Behavioral analysis of each customer group.

Label

Size

Segment

Behavioral Analysis

Silver

15,513

Cluster 
One

Bronze

3557

Cluster 
Two

Gold

1814

Cluster 
Three

Customers in this group initially had low profits 
but recently experienced significant growth and 
became profitable. Strategies should be devised 
to encourage these customers to engage in more 
transactions. Bank-centric strategies should 
focus on enhancing customer experience and 
satisfaction for this group.
Customers in this group initially had high profits 
and transactions, but over time, these features 
decreased, indicating they are at risk of being 
lost. This signals the need for effective strategies 
to retain these customers and prevent their 
attrition.
Known as the golden customers, this group 
includes the most profitable customers due to 
their consistent high revenue generation. This 
group shows stable and loyal behavior. 
Strategies should be designed by the bank to 
maintain and enhance their loyalty and 
satisfaction, considering their significant value 
to the organization.

Table 13 
Comparison of the present study with previous works.

Article

Algorithm

Data Volume

2,156,394 
transactions

259,000 
transactions

123,684 
customers

ABBASIMEHR

and BAHRINI 
(2022)

ABBASIMEHR 
and Shabani 
(2021)

Hamidi (2016)

Current Study

Spectral, 
Hierarchical, K- 
shape
Hierarchical

K-Medoids, K- 
Means, Fuzzy C- 
means, Self- 
Organizing Map
K-Means, Fuzzy C- 
means, Spectral, 
Hierarchical

Study 
Field

Silhouette 
Index Value

Bank

0.46

Bank

0.46

Bank

0.62

neural networks. These methods can identify more complex customer 
behavior patterns and enhance prediction accuracy. As indicated in this 
study,  using  evolutionary  algorithms  like  the  genetic  algorithm  can 
significantly improve feature extraction efficiency. Therefore, one of the 
latest members of the evolutionary algorithm family, Cartesian Genetic 
Programming  (CGP),  is  introduced.  Given  the  improved  results  in 
various papers using CGP compared to those using traditional genetic 
programming, it is suggested that feature combinations be performed 
using CGP. Continuing research based on the results of this paper can 
improve various aspects of the customer segmentation model and pro-
vide  optimal  strategies  for  enhancing  customer  relationships  and 
increasing their lifetime value.

CRediT authorship contribution statement

Hodjat (Hojatollah) Hamidi: Writing – review & editing, Writing – 
original  draft,  Visualization,  Validation,  Supervision,  Software,  Re-
sources,  Project  administration,  Methodology,  Investigation,  Funding 
acquisition, Formal analysis, Data curation, Conceptualization. Bahare 
Haghi: Writing – review & editing, Writing – original draft, Visualiza-
tion, Validation, Supervision, Software, Resources, Project administra-
tion, Methodology, Investigation, Funding acquisition, Formal analysis, 
Data curation, Conceptualization.

Availability of data and materials

The data used to support the findings of this study are available from

the corresponding author.

Declaration of competing interest

The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.

195,844,058 
transactions

Bank

0.91

Data availability

Data will be made available on request.

gender, and other features. Expanding the data scope will allow for more 
comprehensive  analysis  and  more  detailed  examinations  of  customer 
behavior. Additionally, significant improvements in predicting customer 
behavior  can  be  achieved  using  deep  learning  methods  such  as  deep

Abbasimehr, H., & Bahrini, A. (2022). An analytical framework based on the recency, 
frequency, and monetary model and time series clustering techniques for dynamic 
segmentation. Expert Systems with Applications, 192, Article 116373. https://doi.org/ 
10.1016/j.eswa.2021.116373

References

17

---

<!-- PAGE 18 -->

H.(H. Hamidi and B. Haghi

Computers in Human Behavior Reports 16 (2024) 100520

Abbasimehr, H., & Shabani, M. (2021). A new methodology for customer behavior

analysis using time series clustering A case study on a bank’s customers. Emerald, 50 
(2), 221–242. https://doi.org/10.1108/K-09-2018-0506

Abbasimehr, H., & SheikhBaghery, F. (2022). A novel time series clustering method with 
fine-tuned support vector regression for customer behavior analysis. Expert Systems 
with Applications, 204, Article 117584. https://doi.org/10.1016/j.eswa.2022.117584

Akhondzadeh-Noughabi, E., & Albadvi, A. (2015). Mining the dominant patterns of

customer shifts between segments by using top-k and distinguishing sequential rules. 
Management Decision, 53(9), 1976–2003. https://doi.org/10.1108/MD-09-2014- 
0551

Alboukaey, N., Joukhadar, A., & Ghneim, N. (2020). Dynamic behavior based churn

prediction in mobile telecom. Expert Systems with Applications, 162. https://doi.org/ 
10.1016/j.eswa.2020.113779

Anitha, P., & Patil, M. M. (2019). RFM model for customer purchase behavior using K- 
means algorithm. Journal of King Saud University-Computer and Information Sciences, 
1319–1578. https://doi.org/10.1016/j.jksuci.2019.12.011

Arbelaitz, O., Gurrutxaga, I., Muguerza, J., P´erez, J. M., & nigo Perona, I. (2014). “An 
extensive comparative study of cluster validity indices. Pattern Recognition, 46(1), 
243–256. https://doi.org/10.1016/j.patcog.2012.07.021

Batista, G. E., Keogh, E. J., Tataw, O. M., & De Souza, V. M. (2014). Cid: An efficient

complexity-invariant distance for time series. Data Mining and Knowledge Discovery, 
28(3), 634–669. https://doi.org/10.1007/s10618-013-0312-3

Çavdar, A. B., & Ferhatosmano˘glu, N. (2018). Airline customer lifetime value estimation 
using data analytics supported by social network information. Journal of Air 
Transport Management, 67, 19–33. https://doi.org/10.1016/j. 
jairtraman.2017.10.007

Christy, A. J., Umamakeswari, A., Priyatharsini, L., & Neyaa, A. (2018). RFM ranking–An

effective approach to customer segmentation. Journal of King Saud University- 
Computer and Information Sciences. https://doi.org/10.1016/j.jksuci.2018.09.004
Daneshvar, A., Homayounfar, M., & FarahmandNezhad, A. (2020). Development of an

intelligent multi-criteria clustering method based on Promethee. Industrial 
Management Perspective, 36, 41–46. https://doi.org/10.52547/jimp.9.4.41

Dunn, J. C. (1973). A fuzzy relative of the ISODATA process and its use in detecting

compact well-separated clusters. Journal of Cybernetics, 3(3), 32–57. https://doi.org/ 
10.1080/01969727308546046

Emami, H., & Derakhshan, F. (2015). Integrating fuzzy K-means, particle swarm

optimization, and imperialist competitive algorithm for data clustering. Arabian 
Journal for Science and Engineering, 40, 3545–3554. https://doi.org/10.1007/ 
s13369-015-1826-3

Hamidi, H. (2016). A combined fuzzy method for evaluating criteria in enterprise

resource planning implementation. International Journal of Intelligent Information 
Technologies, 12(2), 25–52. https://doi.org/10.4018/IJIIT.2016040103

Hamidi, H., & Vafaei, A. (2009). Evaluation of fault tolerant mobile agents in distributed 
systems. International Journal of Intelligent Information Technologies, 5(1), 43–60. 
https://doi.org/10.4018/jiit.2009010103

R. Heldt, C.S. Silveira and F.B. Luce, “Predicting customer value per product: From RFM 
to RFM/P”, Journal of Business Research, 148-2963. https://doi.org/10.1016/j. 
jbusres.2019.05.001.

John, J. M., Shobayo, O., & Ogunleye, B. (2023). An exploration of clustering algorithms 
for customer segmentation in the UK retail market. Analytics, 2, 809–823. https:// 
doi.org/10.3390/analytics2040042

Khajvand, M., & Tarokh, M. J. (2011). Estimating customer future value of different

customer segments based on adapted RFM model in retail banking context. Procedia 
Computer Science, 3, 1327–1332. https://doi.org/10.1016/j.procs.2011.01.011
Khajvand, M., Zolfaghar, K., Ashoori, S., & Alizadeh, S. (2011). Estimating customer

lifetime value based on RFM analysis of customer purchase behavior: Case study. 
Procedia Computer Science, 3, 57–63. https://doi.org/10.1016/j.procs.2010.12.011
Kumar, V., & Reinartz, W. (2018). Customer relationship management: Concept, strategy,

and tools. Springer. https://doi.org/10.1007/978-3-662-55381-7

Luo, L., Li, B., Fan, X., et al. (2023). Dynamic customer segmentation via hierarchical 
fragmentation-coagulation processes. Machine Learning, 112, 281–310. https://doi. 
org/10.1007/s10994-022-06276-8

Montero-Manso, P., & Hyndman, R. J. (2021). Principles and algorithms for forecasting 
groups of time series: Locality and globality. International Journal of Forecasting. 
https://doi.org/10.1016/j.ijforecast.2021.03.004

Parvaneh, A., Tarokh, M., & Abbasimehr, H. (2014). Combining data mining and group

decision making in retailer segmentation based on LRFMP variables. International 
Journal of Industrial Engineering & Production Research, 25(3), 197–206. https://sid. 
ir/paper/643235/en.

Sari, J. N., Nugroho, L. E., Ferdiana, R., & Santosa, P. I. (2016). Review on customer 
segmentation technique on ecommerce. Advanced Science Letters, 22, 3018–3022. 
https://doi.org/10.1166/asl.2016.7985

Seret, A., vanden Broucke, S. K., Baesens, B., & Vanthienen, J. (2014). A dynamic

understanding of customer behavior processes based on clustering and sequence 
mining. Expert Systems with Applications, 41(10), 4648–4657. https://doi.org/ 
10.1016/j.eswa.2014.01.022

Sivaguru, M. (2023). Dynamic customer segmentation: A case study using the modified 
dynamic fuzzy c-means clustering algorithm. Granul. Comput., 8, 345–360. https:// 
doi.org/10.1007/s41066-022-00335-0

Tavakoli, M., Molavi, M., & Masoumi, V. (2018). Customer segmentation and strategy

development based on user behavior analysis RFM model and data mining 
techniques: A case study. IEEE e-business engineering conf. https://doi.org/10.1109/ 
ICEBE.2018.00027

Yanovitzky, I., & VanLear, A. (2008). Time series analysis: Traditional and contemporary 
approaches (Vols. 89–124). The Sage Sourcebook of Advanced Data Analysis Methods 
for Communication Research. https://doi.org/10.4135/9781452272054.n4

18

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Computers in Human Behavior Reports 16 (2024) 100520
Contents lists available at ScienceDirect
Computers in Human Behavior Reports
journal homepage: www.sciencedirect.com/journal/computers-in-human-behavior-reports
An approach based on data mining and genetic algorithm to optimizing
time series clustering for efficient segmentation of customer behavior
Hodjat (Hojatollah) Hamidi*, Bahare Haghi
Department of Industrial Engineering, Information Technology Group, K. N. Toosi University of Technology, Iran
A R T I C L E I N F O A B S T R A C T
Keywords: In today’s highly competitive market, organizations face significant challenges in accurately understanding and
Dynamic segmentation segmenting customer behavior due to the inherently dynamic and evolving nature of customer interactions over
Feature optimization time. Traditional customer segmentation methods often neglect these temporal variations, leading to ineffective
Genetic algorithm
business strategies and missed opportunities. This research addresses this critical gap by introducing an inno-
Time series analysis
vative time series-based approach for customer behavior segmentation. By modeling each customer’s behavior as
Clustering techniques
a time series capturing key metrics such as purchase frequency, transaction amounts, and customer lifecycle costs
Customer behavior analysis
the proposed method dynamically adapts to behavioral changes over time. To enhance segmentation precision, a
genetic algorithm is employed to optimize feature weights, ensuring that the most relevant factors are empha-
sized. These optimized features are then clustered using spectral clustering to identify distinct and meaningful
customer segments. The effectiveness of the proposed method is validated using 30 months of transactional data
from a payment services company. The results demonstrate that the proposed approach, particularly when
combined with spectral clustering and optimally weighted features, significantly surpassing the performance of
traditional static segmentation techniques. This research not only provides a more accurate framework for
uncovering hidden patterns in customer behavior but also delivers actionable insights for targeted marketing and
personalized customer strategies.
1. Introduction C-means clustering, and K-means clustering, to achieve the best clus-
tering results (Akhondzadeh-Noughabi & Albadvi, 2015; Seret et al.,
Nowadays, customer relationship management has become 2014; Yanovitzky & VanLear, 2008).
extremely important due to intense competition among companies in The biggest limitation of static segmentation methods is that these
various industries (Kumar & Reinartz, 2018). With advancements in methods are not able to model the dynamic behavior of customers and
information and communication technologies, a large volume of data discover meaningful patterns and trends (Khajvand & Tarokh, 2011;
about customers is available to organizations. To utilize this data for SARI et al., 2016). These methods are more descriptive and cannot
strategic decision-making, data mining techniques have emerged as predict the future behavior of customers. In this model, time series are
powerful tools for data analysis and knowledge creation (Parvaneh used to record customer behavior and maintain the chronological order
et al., 2014). This segmentation helps organizations interact more effi- of observations. First, the features of purchase recency, purchase num-
ciently with customers by leveraging data analysis methods. ber, purchase amount, customer cost was extracted from customer
In this paper, we present a new model for customer segmentation transaction data, then customers were segmented using time series
using data mining techniques. This model, using appropriate data clustering. In this research, the cost has been investigated as one of the
mining algorithms and methods tailored to the organization’s dataset, important features, which has not been sufficiently considered in pre-
can segment customers into different groups based on common features. vious researches. Considering cost as one of the important features in
In the proposed model, the features of purchase novelty, number of customer analysis and business management is very important. In
purchases, purchase amount, and customer cost are extracted from various business fields, including banking, retail, services, etc., costs can
customer transaction data. The proposed model uses powerful clustering be one of the determining factors in decisions. In the banking industry,
algorithms, including hierarchical clustering, spectral clustering, fuzzy an accurate understanding of the cost-benefit ratio for each customer
* Corresponding author. IT Information Technology Engineering Group K.N. Toosi University of Technology, Iran.
E-mail addresses: h_hamidi@kntu.ac.ir(H.(H. Hamidi), b.haghi@email.kntu.ac.ir(B. Haghi).
https://doi.org/10.1016/j.chbr.2024.100520
Received 2 September 2024; Received in revised form 25 October 2024; Accepted 29 October 2024
Available online 1 November 2024
2451-9588/© 2024 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/) .

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
can help the bank to provide appropriate strategies to attract, retain and data, showing improved accuracy with social factors. In (Emami &
upgrade customers. By knowing this ratio for each customer, the bank Derakhshan, 2015), a company’s customers were analyzed using new
can evaluate the improvement of its financial performance, establish purchase frequency and amount, employing fuzzy clustering and
purposefulness in the use of financial resources, and realize the customer portfolio analysis. The profitability index validated the results,
improvement of relations with customers who have a better cost-benefit categorizing customers into three clusters: superstar, regular, and
ratio. In addition, in the existing research, multivariate time series have dormant based on lifetime value.
been used instead of univariate time series, and instead of examining the In (Sivaguru, 2023), a dynamic customer segmentation (DCS)
effect of individual characteristics, they have also examined their framework is introduced, comprising three phases: the first phase in-
simultaneous effect together. By considering multivariate time series, it volves using the modified fuzzy c-means (MdFCM) algorithm to cluster
is possible to examine the simultaneous effect of different characteristics new data and identify changes in cluster structures; the second phase
on customer behavior. This makes it possible to understand the con- classifies clusters based on the RFM (Recency, Frequency, Monetary)
nections and interactions between attributes and to analyze their pattern; and the third phase formulates marketing strategies based on
simultaneous influence on customer behavior. This more comprehensive identified changes in the clusters. The MdFCM algorithm calculates
analysis makes it possible to discover hidden patterns and more complex distances between cluster centers, selects the minimum distance, and
relationships that are not visible in the analysis of individual features. As compares new data distances with this minimum. If the new data dis-
a result, more accurate and reliable predictions about the needs and tance exceeds the minimum, new clusters are created or old ones are
desires of customers can be reached. removed; otherwise, clusters are adjusted. This framework helps man-
In this paper, a model is presented that displays the behavior of each agers update customer segmentation with new information and enhance
customer as a time sequence of the variables of purchase novelty, marketing strategies accordingly.
number of purchases, purchase amount, and customer cost, considering In (Luo et al., 2023), a new Bayesian nonparametric model named
the time dimension of customer behavior. Then, using the genetic al- Hierarchical Fragmentation-Coagulation Processes (HFCP) is introduced
gorithm, optimal weights are found for each feature, and customers are for dynamic customer segmentation. This model works as follows: first,
segmented with clustering algorithms. To demonstrate the utility of this HFCP automatically determines the number of groups required to model
model, a case study on the customers of a banking payment service diverse customer behavior. Next, the model can identify dynamic
company is conducted. changes in customer behavior, such as the splitting and merging of
The structure of the paper is as follows: Section 2 reviews related groups. Using a hierarchical approach, HFCP discovers shared behavior
works. The various techniques used in the paper and the proposed patterns across different products. Additionally, HFCP outperforms
method for customer behavior analysis are presented in Section 3. The previous models such as Homogeneous Poisson Processes (HomoPP),
results of the proposed framework are reported in Section 4. Section 5is Non-Homogeneous Poisson Processes (NHPP), and
dedicated to evaluating the performance of the proposed algorithm. Fragmentation-coagulation process)FCP(in predicting the purchase
Finally, Section 6concludes the paper and suggests some directions for behavior of new customers and addresses overfitting issues. This model
future research. employs Fragmentation-Coagulation Processes to model changes in
customer purchasing behavior and helps companies adjust their mar-
2. Literature review keting strategies based on accurate behavioral patterns. Empirical re-
sults demonstrate that HFCP effectively models customer purchasing
In (SARI et al., 2016), the authors reviewed customer segmentation behavior and improves performance.
methods and highlighted that demographic segmentation (age, gender, In (John et al., 2023), various clustering algorithms for customer
education, occupation, income) helps in understanding customer segmentation in the UK online retail market were compared. The study
behavior and optimizing marketing costs. In (Khajvand & Tarokh, used a UK-based online retail dataset and evaluated algorithms such as
2011), a banking study segmented customers based on new purchases, K-means, Gaussian Mixture Model (GMM), Density-Based Spatial Clus-
purchase frequency, and amount, predicting each segment using time tering of Applications with Noise (DBSCAN), agglomerative clustering,
series analysis. In (Khajvand et al., 2011), two methods for customer and Balanced Iterative Reducing and Clustering using Hierarchies
segmentation and lifetime value calculation were presented, showing (BIRCH). The results indicated that the GMM algorithm achieved the
that adding item count as a new parameter had no significant effect on best performance with a Silhouette Score of 0.80. This research dem-
clustering. onstrates that advanced algorithms can improve the accuracy and effi-
In (Heldt et al.), a model for purchase frequency and amount per ciency of customer segmentation, allowing companies to fine-tune their
product showed that product data provides useful insights for marketing marketing strategies and better understand customer purchasing
asset management and reduces customer value prediction errors. In behavior.
(Anitha & Patil, 2019), a study using new purchase frequency and Table 1is related to the summary of the review of the theoretical
amount in retail employed K-means clustering, evaluated with the foundations of customer segmentation, in which the information pro-
silhouette index. In (Daneshvar et al., 2020), a new multi-criteria clus- vided in the literature review is summarized and the different types of
tering method with bi-phase optimization was introduced, enhancing segmentation models are given along with the studies conducted by
the genetic algorithm with heuristic mutation for effective yet researchers and the years associated with each method. From Tables 1
time-consuming clustering. and it can be concluded simply and briefly that the previous researches
In (Tavakoli et al., 2018), a hybrid model combining new purchase on customer segmentation have used the method of new purchase,
frequency, amount, and time series was proposed, showing improved repeat purchase, and purchase amount.
customer analysis and strategic decision-making through Short Message Fig. 1shows the algorithms used in the reviewed articles. Most of the
Service (SMS) campaigns. In (ABBASIMEHR & BAHRINI, 2022), reviewed articles have used unsupervised learning algorithms for
advanced clustering and time series clustering considered the temporal customer segmentation. Therefore, unsupervised learning algorithms
dimension of customer behavior, using transaction data for new pur- have been used in this research.
chase frequency and amount features. In (Christy et al., 2018), new In Fig. 2, a comparison is made between the unsupervised learning
purchase frequency and amount analysis on transaction data, and clus- algorithms used in the articles. The most popular algorithms are K-
tering with K-means and fuzzy C-means, introduced a new idea for Means, fuzzy C-Means, Spectral, hierarchical, K-shape, self-organizing
initial cluster center selection. maps, concentration-based clustering and finally K-Medoids.
In (Çavdar & Ferhatosmanog˘lu, 2018), an airline industry model According to the literature review, it was concluded that unsuper-
estimated customer lifetime value using flight data and social network vised learning algorithms are mostly used in research. Unsupervised
2

H.(H. Hamidi and B. Haghi                                                                                                                                                           C  o  m  p  u  t e r  s   i n    H  u  m   a n    B  e  h a  v  i o r    R  e p  o  r t s  16 (2024) 100520
Table 1
Summary of overview of the theoretical bases of customer segmentation.
|     | New purchase  | Neural  | Time  Clustering | Classification Regression |
| --- | ------------- | ------- | ---------------- | ------------------------- |
|     | Repeat        | network | series           |                           |
purchase
Purchase
amount
(Akhondzadeh-Noughabi & Albadvi, 2015; Parvaneh et al., 2014; Yanovitzky &  ✓ ​ ​ ​ ​ ​
VanLear, 2008)
| (SARI et al., 2016)                  | ✓   | ​   | ​ ​ | ​ ​ |
| ------------------------------------ | --- | --- | --- | --- |
| (Khajvand & Tarokh, 2011)            | ✓   | ​   | ​ ​ | ​ ​ |
| (Khajvand et al., 2011)              | ✓   | ​   | ​ ​ | ​ ​ |
| (Heldt et al.; Anitha & Patil, 2019) | ​   | ✓   | ​ ✓ | ​ ✓ |
| (Daneshvar et al., 2020)             | ✓   | ​   | ​ ​ | ​ ​ |
|                                      | ✓   | ​   | ​ ​ | ✓ ​ |
(Tavakoli et al., 2018)
| (ABBASIMEHR & BAHRINI, 2022)      | ✓   | ​   | ​ ​ | ✓ ​ |
| --------------------------------- | --- | --- | --- | --- |
| (Christy et al., 2018)            | ​   | ​   | ​ ​ | ✓ ​ |
| (Çavdar & Ferhatosmanog˘lu, 2018) | ✓   | ​   | ​ ​ | ​ ​ |
| (Emami & Derakhshan, 2015)        | ​   | ​   | ​ ✓ | ✓ ​ |
| (Sivaguru, 2023)                  | ✓   | ​   | ​ ​ | ​ ​ |
| (Luo et al., 2023)                | ​   | ​   | ​ ​ | ​ ✓ |
|                                   | ​   | ​   | ​ ​ | ✓ ​ |
(John et al., 2023)
| (Batista et al., 2014)   | ​   | ​   | ​ ​ | ✓ ​ |
| ------------------------ | --- | --- | --- | --- |
| (Arbelaitz et al., 2014) | ​   | ​   | ​ ​ | ✓ ​ |
|                          | ​   | ​   | ✓ ​ | ​ ​ |
(Dunn, 1973)
| (Alboukaey et al., 2020)        | ​   | ​   | ✓ ​ | ​ ​ |
| ------------------------------- | --- | --- | --- | --- |
| (Montero-Manso & Hyndman, 2021) | ​   | ✓   | ​ ​ | ​ ​ |
| (ABBASIMEHR & Shabani, 2021)    | ​   | ✓   | ​ ​ | ​ ​ |
|                                 | ​   | ✓   | ​ ​ | ​ ​ |
(Hamidi, 2016)
Fig. 1. Comparison chart of data mining methods used in articles.
learning algorithms are highly attractive to researchers due to capabil- features independently and assign equal weights, overlooking their in-
ities such as data clustering and discovering hidden patterns in them.  terrelationships and varying importance. Additionally, static RFM-based
These algorithms are used especially when the data is not labeled and  methods fail to capture the dynamic nature of customer interactions,
there is a need to segment and recognize patterns and relationships  limiting their ability to adapt to evolving behaviors and market condi-
between the data. After examining more details among the unsupervised  tions. Moreover, customer lifecycle costs are frequently neglected
algorithms, the top four unsupervised algorithms were selected. This  despite their significance in understanding customer profitability. To
choice was made based on the importance, performance and potential of  address these gaps, this paper incorporates Customer Cost into the
these algorithms in data clustering. Therefore, in this research, these  segmentation process, employs a genetic algorithm to optimize feature
four best algorithms (K-Means, Hierarchical Spectral, Fuzzy C-means)  weights, and utilizes time series analysis to account for temporal dy-
have been used to perform data clustering. This choice has been made  namics. These enhancements result in more accurate and adaptive
according to the literature review and based on the ability and efficiency  customer segmentation, providing a comprehensive understanding of
of these algorithms in the field of data clustering. customer  behavior  and  supporting  the  development  of  effective,
Reviewing past studies reveals that most customer segmentation  responsive marketing strategies.
research focuses on Recency, Frequency, and Monetary (RFM) values
due to their simplicity and efficiency. However, these studies treat RFM
3

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
Fig. 2. Comparative diagram of unsupervised algorithms used in articles.
3. Research methodology researcher must collect the available data and analyze them in a regular
and organized manner. To understand the data, various methods and
As shown in Fig. 3, the proposed model effectively integrates new techniques can be used, including:
transactions, the number of transactions, transaction profit, and cost Data Collection: Business related data is collected. This data in-
with time series clustering. It extracts time series data from a stream of cludes customer transaction data, information related to products or
timestamped transactional data to depict the behavior of customers. The services, financial data and other business related information.
details of each step in the model are explained below. Data Preprocessing: In this step, the data is preprocessed. It includes
data cleaning, removing incomplete or duplicate data, converting data
3.1. CRISP methodology format and structuring them properly.
Data analysis: Using data analysis methods, patterns and trends in
CRISP is a common methodology in the field of data mining that is the data can be identified. Various techniques such as descriptive sta-
used to carry out data mining projects. This methodology consists of tistics, data mining methods, modeling and other methods are used. By
several steps that are executed sequentially and includes the complete doing the mentioned steps, a better understanding of the data and
process of data analysis. In the following, its steps are explained business characteristics can be achieved, which will help in the subse-
(ABBASIMEHR & SheikhBaghery, 2022). quent analysis and modeling.
3.1.1. Business understanding phase 3.1.3. Data collection and preparation phase
The business understanding step in the CRISP methodology is related The data collection and preparation step in the CRISP methodology
to the deep understanding that the researcher needs to know about the belongs to the process in which the necessary data for subsequent
business under investigation. In this step, the researcher should examine analysis and modeling are collected, extracted, cleaned and prepared. In
and analyze the market, products and services, customers, competitors, this step, steps should be taken to make the data useable and reliable. To
organizational structure and other business-related factors. To get to collect and prepare data, the following methods and techniques can be
know the business, different methods can be used, including: used:
Studying documents and related sources: By studying reports, arti- Data collection: In this step, data related to the research is collected.
cles, books and other sources related to business, one can get the It includes customer transaction data, product or service data, financial
necessary information about the type of activities, target market, com- data, historical data and other required information. Data can be
petitors and other aspects of the business. collected from internal company sources (such as database management
Interviewing experts: by interviewing people who work in the in- systems) or external sources (such as Internet sources or public data
dustry or organization under investigation, you can gather their opin- sources).
ions and knowledge about the business and reach a higher Data Cleansing: In this step, the data is cleaned and cleared of errors,
understanding. mistakes and incomplete data. Methods such as removing duplicate
Direct observation: By directly observing the activities, products and data, compensating for missing data, converting data format, using data
services of the business, you can get a better understanding of its per- cleaning techniques and correcting invalid data can be used.
formance and characteristics. As a result, by knowing the business, it is Selecting and extracting features: In this step, the important and
possible to consider the best approach and appropriate solutions for the required features for analysis and modeling are extracted from the data.
successful implementation of the research and facilitate obtaining the These attributes can include numerical attributes such as mean, vari-
desired results. ance, and categorical attributes such as product type, customer gender,
etc. The correct selection of features is very important in data analysis
3.1.2. Data understanding phase and can have a great impact on the accuracy and efficiency of prediction
The step of data understanding in CRISP methodology is related to models.
the process of understanding and analyzing data. In this step, the Data transformation and preparation: In this step, data is prepared
4

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
Fig. 3. Proposed research model.
for use in modeling. This includes converting the data into a suitable 3.1.4. Modeling phase
format for data mining algorithms, normalizing the data, reducing the The modeling phase in the CRISP methodology is the stage in which
dimensionality of the data, as well as dividing the data into two sets of prediction, classification or clustering models are created from the
training and testing. By performing the data collection and preparation collected and prepared data. The purpose of these models is to explain
steps correctly, the data will be ready to be used in modeling and the patterns in the data and also to predict the behavior and events in the
analysis. This makes it more efficient to use the data and obtain more future. The main stages of the modeling phase are:
accurate and reliable results. Selection of algorithms: In this step, based on the type of analysis
desired (such as prediction, classification, or clustering) and the char-
acteristics of the data, suitable algorithms are selected for modeling. In
5

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
other words, the type of problem and the nature of the data will deter- aggregated based on monthly intervals. Time series related to each
mine the choice of algorithms. variable for the customer are calculated. The definition of time series for
Building models: In this step, using the selected algorithms, different the variables of transaction recency, number of transactions, transaction
models are created on the data. These models can include statistical profit, and customer cost are as follows.
models such as regression and factor analysis, machine models and
adaptive models such as clustering algorithms. • Transaction Recency (t): The number of months that have passed
Training and evaluation of models: The built models are trained since the customer’s last transaction in a specified time period.
using training data and then evaluated using test data. Evaluation of • Transaction Frequency (t): The number of transactions conducted
models includes criteria of accuracy, correctness, recall and other with the card reader during the specified time period.
related criteria. If needed, the models are improved and retrained by • Transaction Profit (t): The amount of revenue generated from the
changing the parameters. customer’s transactions during the specified time period.
Selection of the final model: After evaluating the models and • Customer Lifecycle Costs (t): The costs incurred by the organiza-
comparing their performances, the model that has the best performance tion for the services and products provided to the customer during
and meets the analytical needs is selected as the final model. Using the specified time period. These costs include expenses for card
CRISP methodology in the modeling phase helps researchers to use data reader rolls, periodic visits, costs related to technical or consulting
in a structured and step-by-step manner and to create acceptable and services, costs associated with the use of specific equipment and
reliable models for data analysis. technologies, and other related service provision costs.
3.1.5. The criterion phase of measurement and model evaluation In this methodology, customer behavior analysis is performed
Model measurement and evaluation criteria in CRISP methodology considering four features: transaction recency, number of transactions,
are used to evaluate the performance of built models. These criteria are transaction profit, and customer cost. This comprehensive approach
determined based on the problem under investigation and are usually allows for the examination of the impact of each of these features on
used for prediction and classification models. Some of the commonly customer behavior.
used criteria are as follows:
Accuracy: the ratio of the number of correct samples predicted by 3.3. Weighting features using a genetic algorithm
the model to the total number of samples.
Accuracy: The ratio of the number of real positive samples correctly In this stage, a genetic algorithm is used to weight the features in
identified by the model to the total number of positive samples predicted time series clustering. The objective of this process is to find an optimal
by the model. set of weights that appropriately assign importance to the features
Recall: The ratio of the number of true positive samples correctly during clustering. Using these weights allows for more precise
identified by the model to the total number of positive samples in the clustering.
data.
F-measure: A measure that is a combination of precision and recall 3.4. Time series clustering
and is used to balance the two measures.
Confusion matrix: a table that shows the number of correct and Time series clustering is an analytical method that allows for the
incorrect samples predicted by the model and is used as an evaluation grouping of similar time series into separate clusters. In this method,
tool in classification problems. time series are first extracted as samples of temporal data. Then, using
The area under the performance characteristic curve: This measure appropriate distance metrics, the distances between time series are
is used for classification models and indicates the ability of the model to calculated. These metrics can include Euclidean distance, Manhattan
distinguish between two different categories. Each of these criteria can distance, and other similar measures based on the characteristics of the
be used to evaluate the performance of the models depending on the time series (Batista et al., 2014). Subsequently, four powerful clustering
need and the problem under investigation. Also, by combining these algorithms—hierarchical, spectral, K-means, and fuzzy C-means are
criteria and using other criteria, a more comprehensive evaluation of the employed for clustering.
models can be done.
3.5. Selecting the best clustering result by calculating Silhouette and
3.1.6. Deployment phase Calinski-Harabasz indices
The development phase in CRISP methodology is the last phase of
data mining research. In this phase, the models built by the researchers At this stage, after segmenting customers using various combinations
in the previous phases are used and used for the required predictions and of algorithms and feature weights, the quality of the segmentation
analyses. In this phase, after building the models and training them models needs to be evaluated using appropriate clustering validity
using the training data, the models are evaluated using the test or indices. Clustering is an unsupervised method that aims to divide data
validation data. If the performance of the models is acceptable, they are into segments with high internal similarity and low inter-segment sim-
used for use in the project or real applications. If the performance of the ilarity (Arbelaitz et al., 2014). Internal clustering validity indices
models does not reach the desired results, researchers may need to examine how similar data points within each group are to each other,
change the parameters, change the algorithms or use better and more helping to select the best clustering result.
suitable data to improve the performance of the models. Finally, after
ensuring the performance of the models, they can be used for further 3.6. The main stages of the proposed methodology
predictions and analysis in projects and business decisions. As the final
stage, this phase shows the results and benefits obtained from data 3.6.1. Labeling and analyzing the behavior of each customer group
mining research in real applications and plays a very important role in In this stage, each of the resulting clusters is labeled, and the
evaluating the effectiveness of research. behavior of each group is examined to identify their dominant patterns
over time. To summarize the main steps of the proposed methodology,
3.2. Representing customer behavior as recency, frequency, monetary, Fig. 3has been drawn. This model receives customer transactions with
and cost (RFMC) time series timestamps as inputs and creates a time series of features for each
customer, representing their behavior over time. Then, using a genetic
In this stage, transactional data of customers, timestamped, are algorithm, appropriate weights for each feature are extracted, and
6

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
customer segmentation is performed through time series clustering. Table 2
Specifically, various combinations of algorithms and feature. Sample data used in the research.
Data mining is a process that uses various techniques and algorithms Terminal Profit from the Number of Transaction Customer
to extract patterns, trends and useful information from a large volume of number transaction transactions recency cost
data. This process involves examining data, identifying hidden patterns
123456 247000 323 0 22000
and connections that can be used in decision making, forecasting and 678901 342000 409 2 123000
optimization. The main goal of data mining is to discover hidden pat- 234567 987000 711 1 187000
terns and relationships that can be used to make decisions, make pre- 890123 102000 167 5 145000
dictions, and improve performance. This process generally includes
steps such as data preprocessing, feature selection, pattern discovery,
The number of transactions includes the number of customer trans-
and model evaluation. Data mining is used in various fields to obtain
actions in a month, and the transaction freshness is the number of
useful information and make decisions based on data (Sivaguru, 2023).
months that have passed since the last customer transaction. In the
In this research, SQL Server software was used to extract data from
beginning, the transactional data of customers were small and detailed,
the database. First, the required data was extracted from the database
but due to the large volume of data and the complexity of the processing
using SQL Server. Then, using the Python programming language and
operations, the data were analyzed in the form of monthly summaries.
developing the corresponding codes, the data were processed and
By collecting and aggregating data, monthly data can be used to check
analyzed. This processing includes the use of Python libraries related to
the behavior of each customer in a time series. In this process, four main
data mining.
features are used, including the number of transactions, transaction
In this research, various data mining techniques were used. These
freshness, transaction amount, and customer cost. The customer cost
techniques include.
feature is calculated from the amount of roll consumed, the cost of pe-
riodic visits and other services provided to the customer. Then, for each
• Data preprocessing to prepare the data for the next steps.
customer, the information related to the last thirty months from the four
• Extracting important features related to changes and time patterns.
aforementioned features was extracted monthly and the necessary an-
• Extracting the proper weight of features using genetic algorithm.
alyzes were performed on the data. It should be noted that all the
• Data clustering using clustering algorithms.
characteristics of the customers have a value in the 30-month period
• Evaluation of clusters using Silhouette and Kalinsky criteria.
under review, (Description of the data used in the research is shown in
• Analyzing customer behavior and labeling customers based on
Table 3).
clusters and forming specific groups.
4.1.2. Data processing
weights are explored to find the best clustering model according to
Data processing is done to prepare and improve their quality before
the clustering validity index. Finally, the resulting clusters are analyzed
using them in the next steps. Regarding the data used in this research,
to reveal their dominant patterns over time.
due to the use of transaction data of banking customers, the data has
been collected from a clean and complete database, so there is no need
4. Empirical study
for special pre-processing because the data has been collected from a
clean and correct database. But a normalization step has been applied to
This section presents a real-world example of implementing the
the data and a monthly summary of microtransactions has been done.
proposed framework using data from a banking payment service com-
This operation has been done in order to use the data more easily and
pany. The proposed framework and all its components have been
optimally in the next steps.
implemented using Python 3.7. The input data consists of 30 months of
transactional data from card reader devices, including information such
4.1.3. Feature extraction
as card reader ID, transaction ID, date, and transaction amount. This
Important features have been extracted from the data. At this stage,
dataset comprises 195,844,085 detailed purchase transactions by
meaningful and useful features have been extracted from the customer
customers.
data set, which play an important role in describing and interpreting
customer behavior. These attributes are usually determined based on
4.1. Data description transactional data including transaction count, transaction recency,
transaction amount, and customer cost. Using these features, it is
4.1.1. Software and implementation environment possible to identify customer patterns and behaviors. Extracting features
In this research, two popular and powerful softwares, Python and from customer data is a key step in the process of analyzing and seg-
structured query language, have been used to implement customer menting customers, which provides more possibilities and capabilities to
segmentation models. Python programming language has been used as interpret and predict the future behavior of customers. To extract the
the main language for data analysis and running algorithms. By having number of transactions feature, the number of transactions performed
various libraries and useful capabilities for data mining, Python helps to
analyze customer data and perform segmentation with high accuracy.
Also, a structured query language database has been used to store and Table 3
manage customer data. Using a structured query language, information Description of the data used in the research.
about customers is stored in tables and used for data extraction and Feature Description of the feature used
processing.
Transaction recency The number of months passed since the customer’s last
In this research, the database of a famous and large Iranian payment transaction within a month is checked, the lower the better.
service provider company has been used. This data includes 195844058 Number of The number of transactions that a customer has reviewed
transaction records of 48948 customers of this electronic payment transactions within a month, the higher this feature is, the better.
company in the historical period of thirty months. Some of these data are Profit from the The amount of profit obtained from a customer’s
transaction transactions in a period of one month, the higher this
shown in Table 2. Each row of this table represents a customer. There are
feature, the better.
30 records for each customer for a 30-month period, considering that 30 Customer cost The amount of money that the organization pays for a
months of each customer have been used in a time series. The profit that customer in a period of one month, this cost includes
reaches the organization from each customer transaction is collected in periodical visits, consumption roll and other services
provided to the customer. The less this feature, the better.
the period of one month and is placed in the transaction profit column.
7

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
by each customer in a certain period of time is considered. To extract the modeled on evolution in nature and two main heuristics are obtained in
transaction recency feature, the elapsed time since the last transaction these algorithms.
performed by each customer is considered. To extract the transaction
profit feature, the total profit of all transactions performed by each - Survival of the fittest: It is important in the selection operator in such
customer in a certain period of time is calculated from the transaction a way that the one who is the strongest has more chance of survival
amount. Finally, to derive the customer cost attribute, the total cost and has more possibility for mating.
amount that the customer received for the services and products is - Recombination: by combining in the answer, we can hope to get
calculated. Feature extraction has been done on customer data using better answers. One of the characteristics of the evolutionary algo-
calculations and operations appropriate to each feature. These features rithm is that it is blind, so that it does not see its way, and the only
are then used in the next stages of customer segmentation to describe thing it needs is to be given the possibility to evaluate its perfor-
and interpret customer behavior. mance, because if it can evaluate its performance, it can find its way.
Another feature is that it simplifies the problem and uses a series of
4.1.4. Data normalization codes to make decisions, which are generally binary, but there are
The purpose of data normalization is to create conditions where other types as well (Emami & Derakhshan, 2015).
features are equal based on their importance and impact in analyzing
and segmenting customers. This work helps to facilitate the process of 4.2. Representing customer behavior as RFMC time series
data interpretation and analysis and increases the accuracy and usability
of the analysis results. This is in order to remove any deviations and In this stage, the data was first normalized using min-max normali-
differences in sizes between features and to create a balanced distribu- zation. Then, the transactional data was aggregated into monthly in-
tion of data. Outliers were removed before data normalization. The tervals. Based on the definitions of the RFMC variables, the R, F, M, and
outlier data were removed in such a way that only those customers who C time series for each month were extracted. Since all selected customers
had transactions in at least twenty months remained. Then, the data have transactions in every month, the R variable will be zero for all
were normalized using the MinMax normalization method. In this customers. Therefore, the R variable is not considered in the analyses as
method, the feature values are normalized to a certain interval, usually it does not contribute to distinguishing customer segments. Addition-
between 0 and 1. There are different methods for data normalization, ally, the transaction frequency of each customer indicates the number of
but in this research, the min-max normalization method was used transactions made by each customer. It is also evident that the monetary
because the min-max method places the data values in a certain range, value of each transaction can vary. Thus, a high number of transactions
which made the data comparable and hence The impact of data drift on does not necessarily equate to high monetary value. For this reason, the
the final results is reduced. Also, by examining the literature review in monetary variable is considered as the profit from the transaction rather
the second chapter, it was observed that this normalization method is than the transaction amount for analyzing customer behavior. The ul-
one of the most common normalization methods used in the articles. timate goal of any company is to achieve optimal profitability. In
Therefore, according to the advantages and literature review, it was customer segmentation, the cost feature is also considered. In the
decided to use the Min-Max method for data normalization. examined sample, which includes card reader transactions, the costs
X(cid:0) Xmin Incurred by customers during their relationship with the organization
Min maxnormalization= Xmax(cid:0) Xmin (1) are taken into account. These costs include expenses for card reader
rolls, periodic maintenance visits, card reader malfunctions, and other
In this formula, X represents the initial value of the feature. Xmin is the costs borne by the organization for its customers. By considering cost in
minimum feature value in the data and Xmax is the maximum feature customer segmentation, groups of customers with similar cost patterns
value in the data. Using this formula, the features are normalized be- can be identified, allowing for optimal strategies to manage costs and
tween the interval [0, 1]. enhance organizational efficiency.
4.1.5. Evolutionary algorithms 4.3. Weighting features using a genetic algorithm
Evolutionary algorithms include several sub-branches. One of the
commonalities between these algorithms is that the input of each of In the feature weighting stage, a genetic algorithm is used to deter-
these algorithms is a population of people. The pressure of the envi- mine the appropriate weights for the features. The genetic algorithm is a
ronment makes the most appropriate and compatible person with the computational method inspired by the mechanisms of evolution and
environment to be selected as the final solution. For this purpose, a natural selection in nature. Using this algorithm, suitable weights for
quality function is considered for each person in the population. The each feature are extracted to optimize their impact on customer analysis
general goal of these algorithms is to increase the value of the quality and segmentation. In this stage, after data preparation, the genetic al-
function related to each person and select the person with the highest gorithm is applied. The genetic algorithm uses an evolutionary process
quality function as the most compatible person from the population. The to identify the best weight for each feature. Initially, a population of
higher the value of the quality function, the more compatible that person weights is generated. Then, through the use of crossover and mutation
is with the surrounding environment. Based on this function, individuals operators, subsequent generations are created. In each generation, the
are selected as parents to produce the next generation. The act of pro- weights are improved and adjusted based on an evaluation function to
ducing children is done by two operators, mutation and combination, meet the optimal weight for each feature (Dunn, 1973).
which are applied to the parents. The act of compounding is an act that is After running the genetic algorithm and gradually improving the
applied to two parents and is created by those two children. The mu- weights, the best weight values for each feature are extracted. This
tation operator is performed only on a parent and a child is produced by method uses a linear combination of features, meaning that the features
it. The two operators of combination and mutation cause the emergence are combined with different weights to obtain a final value for customer
of new people in the society. Now these new people will compete with analysis and segmentation. The permissible values for these features
the old people of the society to be in the next generation. that this range between [(cid:0) 1, 1], meaning that the weights for the features are
competition is based on their quality function. This procedure is between one and negative one. The values associated with the param-
repeated until the person with the appropriate quality function is eters of the genetic algorithm used are presented in Table 4.
selected as a solution to the problem (Christy et al., 2018). The genetic algorithm was implemented using four clustering algo-
In evolutionary algorithms, a random optimization occurs, which is rithms: hierarchical, spectral, K-means, and fuzzy C-means, resulting in
four output charts corresponding to each fitness function. Figs. 4–7
8

H.(H. Hamidi and B. Haghi                                                                                                                                                           C  o  m  p  u  t e r  s   i n    H  u  m   a n    B  e  h a  v  i o r    R  e p  o  r t s  16 (2024) 100520
Table 4
Describes the genetic algorithm optimization parameters.
| Parameter Name     | Parameter Description                   | Value |
| ------------------ | --------------------------------------- | ----- |
| Maximum Number of  | The maximum number of generations       | 100   |
| Generations        | that the genetic algorithm should run.  |       |
After reaching this number of
generations, the optimization operation
stops.
| Number of Individuals per  | The number of people (population) in  | 200 |
| -------------------------- | ------------------------------------- | --- |
| Generation                 | each generation from the genetic      |     |
algorithm,
| Mutation Probability | The probability of performing mutation  | 0.1 |
| -------------------- | --------------------------------------- | --- |
operations on each gene in each
mutation generation means the random
change of one bit of the gene at a certain
point.
| Elitism Ratio | A proportion of the population that is  | 0.01 |
| ------------- | --------------------------------------- | ---- |
passed on to the next generation as  Fig. 5. Output of the genetic algorithm with spectral fitness function.
superior individuals (elite) and is
excluded from the operations of
combination and mutation.
| Crossover Probability | Probability of combining operations on  | 0.5 |
| --------------------- | --------------------------------------- | --- |
two individuals from the population.
Fusion means combining different parts
of two people to create a new person.
| Selection Ratio | A proportion of the population used to  | 0.3 |
| --------------- | --------------------------------------- | --- |
select a parent for inclusion in the next
generation.
| Type of Crossover | The type of composition used in the  | uniform |
| ----------------- | ------------------------------------ | ------- |
composition operation may be uniform
composition or other types.
| Maximum Number of    | The maximum number of generations  | None |
| -------------------- | ---------------------------------- | ---- |
| Generations without  | during which no improvement in     |      |
| Improvement          | optimization has been made. This   |      |
parameter can be useful to stop the
algorithm if there is no improvement.
Fig. 6. Output of the genetic algorithm with fuzzy C-means fitness function.
Fig. 4. Output of the genetic algorithm with K-means fitness function.
represent the performance of the genetic algorithm in segmenting cus-
tomers using each of these algorithms. Based on the outputs obtained
Fig. 7. Output of the genetic algorithm with hierarchical fitness function.
from these charts, the spectral clustering algorithm performed with
higher accuracy compared to the other algorithms. Therefore, to  The general and comparative explanations of these charts are briefly
improve clustering accuracy, the spectral algorithm and the weights  presented in Fig. 8 so that the results and evaluations are clearly
provided by it were used. These results indicate that the genetic algo-
understandable.
rithm, with the fitness function calculated by the spectral algorithm,
By using the genetic algorithm and the fitness function calculated by
offers greater capability in customer segmentation, contributing to the
the Spectral algorithm, the best accuracy for customer segmentation was
increased accuracy and efficiency of the segmentation process. Addi-
obtained. To compare the results, a bar graph has been drawn that shows
tionally, the best solution found by the genetic algorithm for weighting
the segmentation accuracy using different algorithms (K-Means, hier-
features is as follows: the weights for the three features—number of
archical and fuzzy C-Means) along with the Spectral algorithm. The bar
transactions, transaction profit, and cost—are (cid:0) 0.70, 0.80, and 0.90,
chart shows that by using the genetic algorithm and the spectral fit
respectively, and the objective function is 0.91 for the spectral algo-
function, the accuracy of the segmentation has been improved and they
rithm. In subsequent steps, the weights are multiplied by the features,
have provided a significant improvement compared to other algorithms.
and clustering is performed with the new values. This  means  that  the  genetic  algorithm  with  the  fitness  function
9

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
Fig. 8. The comparative diagram of the implementation of the genetic algorithm with different fitness functions.
calculated by the Spectral algorithm provides the best ability to segment
Table 5
customers and increases the accuracy and efficiency of the segmentation
Dunn index calculation results.
process. The best solution found by the genetic algorithm is as follows:
Optimal Number of Clusters Dunn Index
Weights: [-0.70162901, 0.80858289,0.901110443]
2 0.4190
3 0.4411
and the value of the objective function: 0.91.
4 0.3983
5 0.4257
The genetic algorithm has been able to provide a high-accuracy
6 0.4268
clustering model by optimally assigning the weights. The value of
7 0.4006
Don’s index obtained indicates a very good fit of the clustering with the 8 0.3997
data and a suitable separability between the clusters. This means that 9 0.3987
the optimal weights obtained by the genetic algorithm well represent the
features in customer clustering and the resulting clustering model pro-
vides more accurate results. Then, using these optimal weights, clus-
tering algorithms were implemented and customers were segmented.
These optimal weights have managed to adjust and select the best fea-
tures for clustering customers. The result of clustering with these
weights can be seen in the clustering section. Using these results, it can
be claimed that the genetic algorithm with selected parameters has
succeeded in finding the optimal weights for customer clustering, and
the resulting clustering is more accurate and better than before.
4.4. Time series clustering
After normalizing the data and weighting the features using a genetic
algorithm, the next step is customer segmentation using four popular
algorithms identified in the literature review. The prepared data is
segmented using spectral, hierarchical, fuzzy C-means, and K-means
algorithms, and the best algorithm is identified based on the Silhouette
and Calinski-Harabasz indices.
The optimal number of clusters for customer segmentation is deter- Fig. 9. Dunn index variation chart based on the number of clusters.
mined using the Dunn index. The Dunn index is a quantitative measure
that determines the optimal number of clusters based on the distance 4.5. Selecting the best clustering result by calculating Silhouette and
between clusters and within clusters. By calculating this index for Calinski-Harabasz indices
different numbers of clusters, the optimal number of clusters is obtained.
The higher the Dunn index value, the better the clustering results In this stage, the accuracy of clustering is improved using a genetic
(Alboukaey et al., 2020). The different Dunn index values calculated are algorithm. Initially, before applying the genetic algorithm, clustering is
shown in Table 5. Additionally, the changes in the Dunn index are performed using four algorithms: spectral, hierarchical, fuzzy C- means,
illustrated in Fig. 9, where the highest Dunn index value is obtained for and K-means. Then, after executing the genetic algorithm with opti-
three clusters. mized weights, another round of clustering is conducted using the same
four algorithms.
The quality of clustering is evaluated using the Silhouette and
Calinski-Harabasz indices. This comparative analysis shows that the
10

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
genetic algorithm with optimized weights brings significant improve- Table 7
ment in clustering accuracy. Results of C-Means fuzzy algorithm implementation before and after applying
genetic algorithm weights.
4.5.1. Segmentation using K-Means algorithm Evaluation criteria Before genetic algorithm After genetic algorithm
In customer segmentation using K-Means algorithm, a method called
Silhouette index 0.43 0.67
K-Means is used to divide customers into different groups. In this algo- Calinski index 8523 16884
rithm, first a number of primary centers (cluster centers) are determined
and customers are assigned to the closest cluster center. The cluster
centers are then updated based on the average number of customers
Table 8
assigned to them, and the customers are reassigned to the nearest cluster
Results of spectral clustering algorithm implementation before and after
center. This process is repeated repeatedly until a stable state is estab- applying genetic algorithm weights.
lished and the cluster centers do not change. The K-Means algorithm has
Evaluation criteria Before genetic algorithm After genetic algorithm
advantages such as simplicity and relatively high speed compared to
other algorithms for data segmentation. This algorithm is generally used Silhouette index 0.43 0.91
Calinski index 7596 17307
in clustering problems and is considered as one of the most used and
popular algorithms in this field (Christy et al., 2018). The results of
customer segmentation using the K-Means algorithm on the analyzed each other to finally reach a single large cluster. Hierarchical algorithm
data are shown in Table 6. works in such a way that in each step, two closer clusters are combined
with each other and become a larger cluster. This combination of clus-
4.5.2. Segmentation using C-Means fuzzy algorithm ters is done based on the criteria of the distance between the clusters.
Fuzzy C-Means (FCM) algorithm is a clustering algorithm used for Distance measures may include Euclidean distance, Manhattan distance,
data segmentation using a fuzzy approach. In this algorithm, each data is or any other distance measure chosen based on the properties of the data
probabilistically assigned to one or more clusters, instead of being and the clustering problem. The main advantage of the hierarchical al-
explicitly assigned to a cluster. In the C-Means fuzzy algorithm, the gorithm is the ability to represent the hierarchy of clusters. This algo-
centers of the clusters are initialized randomly. Then, for each data, the rithm is able to divide points into different clusters and also display the
probability of belonging to each cluster is calculated using the concept of hierarchical structure between these clusters (Christy et al., 2018;
fuzzy membership. These membership probabilities are then weighted Çavdar & Ferhatosmanog˘lu, 2018). The results of customer segmenta-
to update the cluster centers. This process is repeated until the changes tion using the hierarchical algorithm on the analyzed data are shown in
in the cluster centers are less than a threshold value. The advantages of Table 9.
C-Means fuzzy algorithm include the ability to model fuzzy data pat-
terns, the ability to simultaneously assign to several clusters, and the 4.6. Comparison of customer segmentation models
ability to apply it to data with a complex structure (Hamidi & Vafaei,
2009). The results of customer segmentation using the C-Means fuzzy The comparison of customer segmentation models using genetic al-
algorithm on the analyzed data are shown in Table 7. gorithm and without using genetic algorithm has been discussed. In
order to check more precisely which model performed best in customer
4.5.3. Segmentation using spectral clustering algorithm data analysis and to what extent the genetic algorithm was effective in
The spectral clustering algorithm is a clustering algorithm based on improving clustering. All customer segmentation algorithms that were
the spectral analysis of graphical information from the data. In order to introduced in the previous sections are compared with each other and
segment the data, this algorithm uses the information of the graph the best segmentation model is determined using two criteria, Silhouette
structure and places the data in different clusters based on the spectral and Kalinsky. To compare segmentation models, two criteria, Silhouette
characteristics of the graph. The performance of the spectral clustering and Kalinsky, have been used. The silhouette measure measures the
algorithm is that first a graph is created for the data. Then the graph degree of separation and integration between clusters. This measure is
spectrum is calculated and clustering is done using the graph spectrum. calculated based on the distance between samples within the cluster and
For this purpose, first the eigenvectors corresponding to the smallest the distance between samples in adjacent clusters. The silhouette value
values of the graph spectrum are extracted and then these vectors are for each cluster ranges from (cid:0) 1 to 1, with higher values indicating better
used as input for the clustering algorithm, such as the K-Means algo- separation between clusters (Khajvand et al., 2011).
rithm. The main advantage of spectral clustering algorithm is in
modeling and clustering data with complex structure. This algorithm Silhouette(i)=
b(i)(cid:0) a(i)
(2)
can identify hidden patterns in the data and carry out accurate clustering
max(a(i),b(i))
according to the structural information of the data (Luo et al., 2023).
The results of customer segmentation using the spectral clustering al-
b: indicates the minimum average distance between points from a
gorithm on the examined data are shown in Table 8.
cluster that are not clustered to other points from adjacent clusters.
a: represents the average internal distances of the points of each
4.5.4. Segmentation using hierarchical algorithm
cluster to the reference point (the central point of the cluster).
Hierarchical algorithm is a clustering algorithm based on the for-
mation of a hierarchy of clusters. In this algorithm, first each point is Calinski’s criterion measures the number of clusters and the quality
considered as a separate cluster. Then, using the distance criteria be-
of separation between clusters. This measure is calculated based on the
tween the points, the clusters are ranked and hierarchically connected to
difference between the internal average of the clusters and the average
Table 6 Table 9
K-Means algorithm implementation results before and after genetic algorithm Results of the implementation of the hierarchical algorithm before and after
weights are applied. applying the weights of the genetic algorithm.
Evaluation criteria Before genetic algorithm After genetic algorithm Evaluation criteria Before genetic algorithm After genetic algorithm
Silhouette index 0.44 0.67 Silhouette index 0.39 0.66
Calinski index 8608 15574 Calinski index 7360 15373
11

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
between the clusters. A high value of this criterion indicates that the 4.7. The results of the implementation of the spectral algorithm with the
clusters are separate and the segmentation quality is better optimal weights of the genetic algorithm
(ABBASIMEHR & BAHRINI, 2022).
According to the values of silhouette and Kalinsky criteria for each
b N(cid:0) k
Calinski Harabasz= + (3) algorithm and comparing them with each other, the best segmentation
w k(cid:0) 1
model for customers using genetic algorithm weights is Spectral because
it has the highest silhouette and Kalinsky values compared to other al-
bindicates the interclusterity of the data and is calculated as the sum gorithms. For this reason, customer segmentation has been done using
of the squares of the distances between the central points of the the Spectral algorithm and the optimal weights of the genetic algorithm,
clusters and the central point of the entire data. w indicates that the and the results are shown in Table 10.
data are within a group and in sum In Table 10, the number of samples in each cluster is shown. Each
row of this table represents a cluster and each column represents the
The square of data distances is calculated from the center of the number of samples in the same cluster. This information tells us how
cluster to which they belong. N represents the total number of data many customers each cluster contains and how large it is in terms of
points. K represents the number of clusters. number of instances.
Figs. 10–13 compare the Silhouette and Calinski-Harabasz indices In Table 11, a statistical summary of the data in each cluster is
for the different algorithms before and after executing the genetic al- shown. These characteristics can include mean, variance, median,
gorithm. These charts illustrate a marked increase in the values of the minimum value, maximum value, etc. This information shows us how
Silhouette and Calinski-Harabasz indices for all algorithms after opti- the customers of each cluster performed on various attributes (such as
mization by the genetic algorithm. This increase indicates better cluster number of transactions, transaction profit, and customer cost) and
segmentation after the genetic algorithm’s optimization. The results of whether these customers differ from each other on these attributes. Also,
the Silhouette and Calinski-Harabasz indices show that the spectral this table can provide information about the distribution of data in each
clustering algorithm performed with higher accuracy compared to the cluster, and this information can be used in data analysis and review.
other algorithms. Therefore, for further improvement and increased Fig. 14shows the graph of changes in the average values of all three
clustering accuracy, customer segmentation was continued using the characteristics of transaction profit(a), transaction number(b) and cost
spectral algorithm. (c) based on clustering groups. In this diagram, each clustering group is
According to the values of Silhouette and Calinski criteria for each displayed with a specific color. The x-axis of the graph shows the dates,
algorithm and comparing them with each other, the best segmentation and the y-axis of the graph shows the average attribute values for each
model for customers is the Spectral algorithm because it has the highest group on each date. By looking at this graph, you can see the changes in
Silhouette and Calinski values. the average values of the features for each of the groups over time. This
graph shows how the clustering groups’ performance has changed over
4.6.1. Customer segmentation using genetic algorithm time and whether their average attribute values have increased or
By using genetic algorithm, optimal weights were obtained for the decreased. Also, by comparing different groups, it can be seen which
attributes of transaction number, transaction profit and customer cost. group had the best performance in terms of the average values of the
Then, using these optimal weights, the clustering algorithms were re-run features. In which periods of time there were visible changes and this
with the same previous conditions, and it is shown in Figs. 12 and 13 information was used in the analysis and review of customer data.
that the clustering models with optimal weights have improved
compared to the models without using optimal weights, and the accu- 4.8. Labeling each customer segment and analyzing the behavior of each
racy and efficiency of clustering have improved. group
This section of the paper analyzes different customer groups. By
calculating the center of each group, the temporal information of that
segment is identified. Figs. 15–17show line charts of the average values
Fig. 10. Comparison chart of accuracy of clustering algorithms with Silhouette criterion without genetic algorithm.
12

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
Fig. 11. Comparison chart of accuracy of clustering algorithms with Calinski criterion without genetic algorithm.
these two features, Group 2 ranks third, as customers in this group have
the lowest share of transactions and profit compared to the other groups.
On the other hand, it is observed that the cost for customers in Group 2 is
lower than in the other two groups. This result indicates that Group 2 is
the best group in terms of cost. After Group 2, Group 3 comes next,
followed by Group 1. This point shows that, on average, customers in
Group 2 conduct their transactions at a lower cost compared to the other
two groups. Table 12shows the behavioral analysis of each customer
group. By analyzing these features and the associated statistical values
for each group, one can better understand the differences and advan-
tages of each group in the business, leading to better decision-making
regarding strategies and customer retention. Additionally, time is a
crucial factor in this analysis. According to Figs. 15–17, which show the
average values by group, it can be observed that customers in Group 3
have exhibited consistent and balanced behavior over the 30-month
Fig. 12. Comparison chart of the accuracy of clustering algorithms with the period studied. This indicates their loyalty. Customers in Group 2 had
Silhouette criterion with the genetic algorithm. high profits and transactions in the initial months, but after some time,
these values decreased, indicating that they are on the verge of being
for the three features: transaction profit, number of transactions, and lost. This point highlights the need to adopt effective strategies to retain
cost, based on the clustering groups. In these charts, each feature Group 2 customers and prevent their loss. Moreover, customers in Group
transaction profit, number of transactions, and cost is displayed in a 1 had few transactions initially but have recently shown significant
specific color. The x-axis represents the dates, and the y-axis represents growth and have become profitable customers. Overall, by analyzing
the average values of the features for each group on each date. By this statistical data and charts, one can better understand the differences
observing these charts, one can see the changes in the average values of and behaviors of each group and implement appropriate strategies to
the features for each group over time. These charts illustrate how the make necessary improvements and changes in the business.
performance of the clustering groups has changed over time and
whether the average values of their features have increased or 5. Performance evaluation
decreased. Additionally, by comparing different groups, one can deter-
mine which group has had the best performance in terms of average This section evaluates the performance of the proposed framework,
feature values, observe notable changes in certain time periods, and divided into three subsections explained below.
utilize this information for analyzing and reviewing customer data.
Fig. 18displays the values of transaction features, profit, and cost for 5.1. Innovations of the research
each of the clustered groups. In this chart, each column corresponds to a
feature, and for each feature, 3 bars are drawn for groups one, two, and One of the most significant innovations of this paper is that, unlike
three, respectively. Each group is also distinguished by a different color. most previous methods that considered equal weights for the parameters
The values shown in this chart represent the average values for each of new purchase, purchase frequency, and purchase amount, this study
feature for each group. This chart generally shows how each group uses a genetic algorithm to obtain optimal weights for customer features.
differs in terms of the examined features compared to the other groups. In this model, by optimizing and adjusting weights using a genetic al-
Based on this statistical information, it can be concluded that Group 3 gorithm, various features are appropriately utilized in customer
has a higher average number of transactions and transaction profit segmentation.
compared to the other two groups. Therefore, this group consists of more This research considers the cost feature in customer segmentation. In
active customers compared to the other two groups. Following Group 3, the examined sample, which includes card reader transactions, the costs
Group 1 has a higher share of transactions and profit overall. Based on incurred by customers during their relationship with the organization
13

H.(H. Hamidi and B. Haghi                                                                                                                                                           C  o  m  p  u  t e r  s   i n    H  u  m   a n    B  e  h a  v  i o r    R  e p  o  r t s  16 (2024) 100520
Fig. 13. Comparison chart of the accuracy of clustering algorithms with Calinski criterion and genetic algorithm.
are taken into account. These costs include expenses for transaction
Table 10
rolls, periodic maintenance visits, card reader malfunctions, and other
The number of samples in each cluster of customers for k =3.
costs borne by the organization for its customers. By considering the cost
Cluster number Number of cluster samples feature in customer segmentation, the best strategies for cost manage-
0 15513 ment and resource optimization can be found. Analyzing customer costs
1 3557 and their impact on the organization’s revenue and profit can help
2 1814 develop strategies to reduce costs. Moreover, it is possible to identify
customer groups with similar cost patterns and provide optimal strate-
gies for managing organizational costs. The customer segmentation
Table 11  model developed in this paper has been successfully implemented in an
Statistical summary of data in each cluster.
electronic payment company, delivering better results than the previous
Number of  Transaction  Customer  segmentation  model  used  by  the  company.  Thus,  this  model  is
transactions Profit Cost commercially viable and applicable in real-world scenarios.
| Second  Count | 30  | 30  | 30  |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- |
group mean 0.58 0.64 0.55 5.2. Integrating the proposed framework into an information system for
| std | 0.3  | 0.31 | 0.3  | improved decision making |     |     |     |
| --- | ---- | ---- | ---- | ------------------------ | --- | --- | --- |
| min | 0    | 0    | 0    |                          |     |     |     |
| 25% | 0.42 | 0.51 | 0.43 |                          |     |     |     |
Some of the applications that can be implemented based on this
| 50% | 0.62 | 0.73 | 0.60 |     |     |     |     |
| --- | ---- | ---- | ---- | --- | --- | --- | --- |
proposed approach include.
| 75% | 0.81 | 0.87 | 0.75 |     |     |     |     |
| --- | ---- | ---- | ---- | --- | --- | --- | --- |
| max | 1    | 1    | 1    |     |     |     |     |
Number of  Transaction  Customer  1. Customer Segmentation: different behavioral groups of customers
|     | transactions | Profit | Cost | can be analyzed over time. |     |     |     |
| --- | ------------ | ------ | ---- | -------------------------- | --- | --- | --- |
First  Count 30 30 30 2. Customer Churn Detection: Identifying customers who are likely to
group mean 0.40 0.40 0.43 churn and taking appropriate actions to retain them is essential
std 0.32 0.32 0.34 (Alboukaey et al., 2020). Recognizing individuals who intend to
| min | 0   | 0   | 0   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
leave the customer list and taking suitable measures to retain them is
| 25% | 0.09 | 0.10 | 0.12 |     |     |     |     |
| --- | ---- | ---- | ---- | --- | --- | --- | --- |
crucial. most studies in the field of churn detection are based on
| 50% | 0.34 | 0.37 | 0.42 |     |     |     |     |
| --- | ---- | ---- | ---- | --- | --- | --- | --- |
static approaches.
| 75% | 0.69 | 0.72 | 0.69 |     |     |     |     |
| --- | ---- | ---- | ---- | --- | --- | --- | --- |
max 1 1 1 3. Customer Behavior Prediction: Predicting customer behavior is
critical in customer relationship management (Montero-Manso &
|     | Number of    | Transaction  | Customer  |                   |               |                      |               |
| --- | ------------ | ------------ | --------- | ----------------- | ------------- | -------------------- | ------------- |
|     |              |              |           | Hyndman,  2021).  | Robust  time  | series  forecasting  | methods  can  |
|     | transactions | Profit       | Cost      |                   |               |                      |               |
Zero  Count 30 30 30 become a valuable tool for managers. The main difference between
group mean 0.48 0.49 0.56 this approach and previous research is its exploitation of the pre-
| std | 0.33 | 0.34 | 0.40 | dictability feature. |     |     |     |
| --- | ---- | ---- | ---- | -------------------- | --- | --- | --- |
| min | 0    | 0    | 0    |                      |     |     |     |
| 25% | 0.11 | 0.10 | 0.06 |                      |     |     |     |
5.3. Research limitations
| 50% | 0.55 | 0.59 | 0.78 |     |     |     |     |
| --- | ---- | ---- | ---- | --- | --- | --- | --- |
| 75% | 0.75 | 0.77 | 0.92 |     |     |     |     |
max 1 1 1 The first limitation of the research was processing large volumes of
data. This study required strong hardware resources to process and
analyze the extensive data. The second limitation is that only customer
14

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
Fig. 14. The linear graph of the average values of the features by features for each group.
transaction data was available; other information such as location, store behavior but also anticipating future behavior. Therefore, this research
size, and number of staff were not accessible for a more detailed analysis fully accounts for the customer lifetime in segmentation. This study
of the segments obtained. offers a dynamic model for customer segmentation, capable of moni-
toring changes in customer behavior through time series clustering. This
6. Conclusion shift from static to dynamic segmentation enables continuous
improvement and adaptation to customer behavior. The study considers
In this paper, a customer segmentation model for dynamic segmen- new purchases, purchase frequency, and purchase amount as a linear
tation based on modeling customer behavior has been presented. combination, without ignoring the relationships between these features.
Customer segmentation has been carried out by considering the entire Using a genetic algorithm, optimal weights were assigned to customer
customer lifetime from inception to the present, looking not only at past features, resulting in improved segmentation compared to previous
15

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
Fig. 15. Line Chart of the Average Values of Features for the first Cluster.
separability between clusters. This means that the optimal weights ob-
tained by the genetic algorithm effectively represent the features in
customer clustering, providing more accurate results. These weights
were used to execute clustering algorithms and perform customer seg-
mentation, successfully selecting and optimizing the best features for
clustering. The results demonstrate that the genetic algorithm with the
selected parameters successfully found optimal weights for customer
clustering, resulting in more accurate and improved segmentation. In
this study, a hybrid and efficient method for customer segmentation was
achieved using the genetic algorithm and weight optimization. As
shown in Table 13, the segmentation accuracy significantly improved
compared to other methods. Additionally, the analysis revealed that the
large data volume (195,844,085 transactions and 48,489 customers)
provided comprehensive and extensive insights, resulting in more pre-
Fig. 16. Line Chart of the Average Values of Features for The second cluster. cise and reliable customer segmentation. Another distinguishing feature
of this work is the inclusion of the cost feature in customer segmenta-
tion, unlike other studies that did not consider this feature. This research
models. The innovations of this research include modeling customer
used a linear combination of features and analyzed customer data over
segmentation based on behavioral changes over the customer lifetime,
30 months, while similar studies considered periods of seven to eleven
using time series analysis, considering cost features in segmentation, and
months. Therefore, given the improved segmentation accuracy, large
the ability to continually improve segmentation based on behavioral
data volume, inclusion of the cost feature, and extended analysis period,
changes. The model has been successfully implemented in an electronic
the results of this study are successful and effective, showing significant
payment company, yielding better results than the previous segmenta-
improvement over reference papers.
tion model. The genetic algorithm, by optimally weighting features, has
For future research, the scope of the data can be expanded to
provided a highly accurate clustering model. The obtained Dunn index
include other customer variables such as geographic location, age,
indicates a very good fit of the clustering to the data and appropriate
Fig. 17. Line Chart of the Average Values of Features for the third cluster.
16

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
Fig. 18. Comparative chart of average feature values for each customer group.
neural networks. These methods can identify more complex customer
Table 12
behavior patterns and enhance prediction accuracy. As indicated in this
Behavioral analysis of each customer group.
study, using evolutionary algorithms like the genetic algorithm can
Label Size Segment Behavioral Analysis significantly improve feature extraction efficiency. Therefore, one of the
Silver 15,513 Cluster Customers in this group initially had low profits latest members of the evolutionary algorithm family, Cartesian Genetic
One but recently experienced significant growth and Programming (CGP), is introduced. Given the improved results in
became profitable. Strategies should be devised various papers using CGP compared to those using traditional genetic
to encourage these customers to engage in more
programming, it is suggested that feature combinations be performed
transactions. Bank-centric strategies should
focus on enhancing customer experience and using CGP. Continuing research based on the results of this paper can
satisfaction for this group. improve various aspects of the customer segmentation model and pro-
Bronze 3557 Cluster Customers in this group initially had high profits vide optimal strategies for enhancing customer relationships and
Two and transactions, but over time, these features
increasing their lifetime value.
decreased, indicating they are at risk of being
lost. This signals the need for effective strategies
to retain these customers and prevent their CRediT authorship contribution statement
attrition.
Gold 1814 Cluster Known as the golden customers, this group Hodjat (Hojatollah) Hamidi: Writing – review & editing, Writing –
Three includes the most profitable customers due to
original draft, Visualization, Validation, Supervision, Software, Re-
their consistent high revenue generation. This
group shows stable and loyal behavior. sources, Project administration, Methodology, Investigation, Funding
Strategies should be designed by the bank to acquisition, Formal analysis, Data curation, Conceptualization. Bahare
maintain and enhance their loyalty and Haghi: Writing – review & editing, Writing – original draft, Visualiza-
satisfaction, considering their significant value
tion, Validation, Supervision, Software, Resources, Project administra-
to the organization.
tion, Methodology, Investigation, Funding acquisition, Formal analysis,
Data curation, Conceptualization.
Table 13
Availability of data and materials
Comparison of the present study with previous works.
Article Algorithm Data Volume Study Silhouette The data used to support the findings of this study are available from
Field Index Value
the corresponding author.
ABBASIMEHR Spectral, 2,156,394 Bank 0.46
and BAHRINI Hierarchical, K- transactions
Declaration of competing interest
(2022) shape
ABBASIMEHR Hierarchical 259,000 Bank 0.46
and Shabani transactions The authors declare that they have no known competing financial
(2021) interests or personal relationships that could have appeared to influence
Hamidi (2016) K-Medoids, K- 123,684 Bank 0.62
the work reported in this paper.
Means, Fuzzy C- customers
means, Self-
Organizing Map Data availability
Current Study K-Means, Fuzzy C- 195,844,058 Bank 0.91
means, Spectral, transactions Data will be made available on request.
Hierarchical
References
gender, and other features. Expanding the data scope will allow for more
comprehensive analysis and more detailed examinations of customer Abbasimehr, H., & Bahrini, A. (2022). An analytical framework based on the recency,
frequency, and monetary model and time series clustering techniques for dynamic
behavior. Additionally, significant improvements in predicting customer
segmentation. Expert Systems with Applications, 192, Article 116373. https://doi.org/
behavior can be achieved using deep learning methods such as deep 10.1016/j.eswa.2021.116373
17

H.(H. Hamidi and B. Haghi C o m p u t e r s i n H u m a n B e h a v i o r R e p o r t s 16 (2024) 100520
Abbasimehr, H., & Shabani, M. (2021). A new methodology for customer behavior Hamidi, H., & Vafaei, A. (2009). Evaluation of fault tolerant mobile agents in distributed
analysis using time series clustering A case study on a bank’s customers. Emerald, 50 systems. International Journal of Intelligent Information Technologies, 5(1), 43–60.
(2), 221–242. https://doi.org/10.1108/K-09-2018-0506 https://doi.org/10.4018/jiit.2009010103
Abbasimehr, H., & SheikhBaghery, F. (2022). A novel time series clustering method with R. Heldt, C.S. Silveira and F.B. Luce, “Predicting customer value per product: From RFM
fine-tuned support vector regression for customer behavior analysis. Expert Systems to RFM/P”, Journal of Business Research, 148-2963. https://doi.org/10.1016/j.
with Applications, 204, Article 117584. https://doi.org/10.1016/j.eswa.2022.117584 jbusres.2019.05.001.
Akhondzadeh-Noughabi, E., & Albadvi, A. (2015). Mining the dominant patterns of John, J. M., Shobayo, O., & Ogunleye, B. (2023). An exploration of clustering algorithms
customer shifts between segments by using top-k and distinguishing sequential rules. for customer segmentation in the UK retail market. Analytics, 2, 809–823. https://
Management Decision, 53(9), 1976–2003. https://doi.org/10.1108/MD-09-2014- doi.org/10.3390/analytics2040042
0551 Khajvand, M., & Tarokh, M. J. (2011). Estimating customer future value of different
Alboukaey, N., Joukhadar, A., & Ghneim, N. (2020). Dynamic behavior based churn customer segments based on adapted RFM model in retail banking context. Procedia
prediction in mobile telecom. Expert Systems with Applications, 162. https://doi.org/ Computer Science, 3, 1327–1332. https://doi.org/10.1016/j.procs.2011.01.011
10.1016/j.eswa.2020.113779 Khajvand, M., Zolfaghar, K., Ashoori, S., & Alizadeh, S. (2011). Estimating customer
Anitha, P., & Patil, M. M. (2019). RFM model for customer purchase behavior using K- lifetime value based on RFM analysis of customer purchase behavior: Case study.
means algorithm. Journal of King Saud University-Computer and Information Sciences, Procedia Computer Science, 3, 57–63. https://doi.org/10.1016/j.procs.2010.12.011
1319–1578. https://doi.org/10.1016/j.jksuci.2019.12.011 Kumar, V., & Reinartz, W. (2018). Customer relationship management: Concept, strategy,
Arbelaitz, O., Gurrutxaga, I., Muguerza, J., P´erez, J. M., & nigo Perona, I. (2014). “An and tools. Springer. https://doi.org/10.1007/978-3-662-55381-7
extensive comparative study of cluster validity indices. Pattern Recognition, 46(1), Luo, L., Li, B., Fan, X., et al. (2023). Dynamic customer segmentation via hierarchical
243–256. https://doi.org/10.1016/j.patcog.2012.07.021 fragmentation-coagulation processes. Machine Learning, 112, 281–310. https://doi.
Batista, G. E., Keogh, E. J., Tataw, O. M., & De Souza, V. M. (2014). Cid: An efficient org/10.1007/s10994-022-06276-8
complexity-invariant distance for time series. Data Mining and Knowledge Discovery, Montero-Manso, P., & Hyndman, R. J. (2021). Principles and algorithms for forecasting
28(3), 634–669. https://doi.org/10.1007/s10618-013-0312-3 groups of time series: Locality and globality. International Journal of Forecasting.
Çavdar, A. B., & Ferhatosmanog˘lu, N. (2018). Airline customer lifetime value estimation https://doi.org/10.1016/j.ijforecast.2021.03.004
using data analytics supported by social network information. Journal of Air Parvaneh, A., Tarokh, M., & Abbasimehr, H. (2014). Combining data mining and group
Transport Management, 67, 19–33. https://doi.org/10.1016/j. decision making in retailer segmentation based on LRFMP variables. International
jairtraman.2017.10.007 Journal of Industrial Engineering & Production Research, 25(3), 197–206. https://sid.
Christy, A. J., Umamakeswari, A., Priyatharsini, L., & Neyaa, A. (2018). RFM ranking–An ir/paper/643235/en.
effective approach to customer segmentation. Journal of King Saud University- Sari, J. N., Nugroho, L. E., Ferdiana, R., & Santosa, P. I. (2016). Review on customer
Computer and Information Sciences. https://doi.org/10.1016/j.jksuci.2018.09.004 segmentation technique on ecommerce. Advanced Science Letters, 22, 3018–3022.
Daneshvar, A., Homayounfar, M., & FarahmandNezhad, A. (2020). Development of an https://doi.org/10.1166/asl.2016.7985
intelligent multi-criteria clustering method based on Promethee. Industrial Seret, A., vanden Broucke, S. K., Baesens, B., & Vanthienen, J. (2014). A dynamic
Management Perspective, 36, 41–46. https://doi.org/10.52547/jimp.9.4.41 understanding of customer behavior processes based on clustering and sequence
Dunn, J. C. (1973). A fuzzy relative of the ISODATA process and its use in detecting mining. Expert Systems with Applications, 41(10), 4648–4657. https://doi.org/
compact well-separated clusters. Journal of Cybernetics, 3(3), 32–57. https://doi.org/ 10.1016/j.eswa.2014.01.022
10.1080/01969727308546046 Sivaguru, M. (2023). Dynamic customer segmentation: A case study using the modified
Emami, H., & Derakhshan, F. (2015). Integrating fuzzy K-means, particle swarm dynamic fuzzy c-means clustering algorithm. Granul. Comput., 8, 345–360. https://
optimization, and imperialist competitive algorithm for data clustering. Arabian doi.org/10.1007/s41066-022-00335-0
Journal for Science and Engineering, 40, 3545–3554. https://doi.org/10.1007/ Tavakoli, M., Molavi, M., & Masoumi, V. (2018). Customer segmentation and strategy
s13369-015-1826-3 development based on user behavior analysis RFM model and data mining
Hamidi, H. (2016). A combined fuzzy method for evaluating criteria in enterprise techniques: A case study. IEEE e-business engineering conf. https://doi.org/10.1109/
resource planning implementation. International Journal of Intelligent Information ICEBE.2018.00027
Technologies, 12(2), 25–52. https://doi.org/10.4018/IJIIT.2016040103 Yanovitzky, I., & VanLear, A. (2008). Time series analysis: Traditional and contemporary
approaches (Vols. 89–124). The Sage Sourcebook of Advanced Data Analysis Methods
for Communication Research. https://doi.org/10.4135/9781452272054.n4
18