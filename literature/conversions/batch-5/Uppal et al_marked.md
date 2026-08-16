---
conversion_metadata:
  converted_at: "2026-07-21T09:07:13Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Uppal et al.pdf"
  source_pdf_sha256: "63a1f783ba4044d60b1ab021f3c0db5488b51fca31f4517c84ed5021c692ce1b"
  page_count: 22
  markdown_char_count: 135643
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Uppal et al. Discover Artificial Intelligence           (2026) 6:248 
https://doi.org/10.1007/s44163-026-00949-2

Discover Artificial Intelligence

Translating artificial intelligence into socio-
economic insight: a hybrid deep learning 
approach to employee financial well-being
Aakanksha Uppal1*, Anubha Srivastava2, Yashmita Awasthi3, Anjita Srivastava4 and Barkha Kakkar2

*Correspondence:
Aakanksha Uppal
aakanksha.uppal@symlaw.edu.in
1Symbiosis International (Deemed 
University) Pune, Symbiosis Law 
School Noida Campus, Noida, 
Ghaziabad, India
2Institute of Technology & Science, 
Mohan Nagar, Ghaziabad, India
3School of Commerce, Finance and 
Accountancy, Christ University, 
Bengaluru, India
4Bundelkhand University, Jhansi, 
India

Abstract
This study aims to translate recent advancements in hybrid artificial intelligence (AI) 
modeling into a functional tool for assessing individual financial well-being. The 
objective is to develop a system that aids organizations in understanding employees’ 
financial stress, with broader implications for enhancing workplace productivity and 
societal economic resilience. A deep learning pipeline was developed to classify 
individuals into three financial well-being categories: Financially Secure, Moderately 
Stable, and Financially At-Risk. The approach utilizes a structured dataset of 20,000 
Indian individuals and implements 15 advanced deep learning models, including 
Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), Gated 
Recurrent Units (GRU), Bidirectional Long Short-Term Memory (BiLSTM), and Wide & 
Deep networks. Model performance was assessed using standard evaluation metrics, 
including validation accuracy and ROC-AUC scores. Among the tested models, the 
hybrid Wide & Deep + CNN configuration yielded the highest performance, achieving 
a validation accuracy of 99.44% and a perfect ROC-AUC score of 1.0000. These results 
validate the model’s capacity for robust classification and real-world applicability to 
financial profiling. This study demonstrates a practical application of AI in financial 
decision support systems and contributes to organizational research by offering a 
scalable solution to assess and mitigate employee financial stress.

Keywords  Financial well-being assessment, Deep learning, Wide & deep network, 
CNN, Employee financial stress, Organizational productivity, Societal economic stability

1  Introduction

In  the  context  of  organizational  dynamics,  financial  decision-making  is  not  merely  a 
technical or administrative function, but a reflection of deeper organizational structures, 
behaviors,  and  societal  interactions.  The  journal  underscores  the  need  to  explore  how 
financial  practices  influence  and  are  influenced  by  the  lived  experiences  of  individuals 
within  organizations.  This  encourages  studies  that  move  beyond  abstract  theorizing, 
focusing instead on the transformative application of theoretical insights into real-world 
organizational practices. Thus, integrating financial analysis with organizational theory

© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International 
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate 
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. 
You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party 
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material 
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted 
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : /  / c r e a  t i v e c o  m m o n  s . o r g  / l i c e  n s 
e s / b  y - n c  - n d / 4 . 0 /.

---

<!-- PAGE 2 -->

Page 2 of 22

contributes not only to scholarly understanding, but also to the practical improvement 
of life within and across institutions.

Finance  refers  to  the  systematic  management,  investment,  and  allocation  of  money 
to preserve its value, build it over time, or simply for efficient utilization. It is a critical 
tool in the decision-making process of an individual, an organization, or a government. 
Finance  has  generally  been  divided  into  three  major  fields:  public  finance,  corporate 
finance,  and  personal  finance  [24].  Public  finance  deals  with  a  nation’s  revenues  and 
expenditures  including  tax  policies,  budgeting,  public  debt,  and  economic  stabilizing 
efforts. The idea of corporate finance reveals how a corporation may manage its financial 
actions with regard to the acquisition of assets, liabilities, investments, and the raising of 
capital through debt to ensure profitability and sustainability. Personal finance refers to 
money management by an individual or family, including budgeting and saving, invest-
ing, insurance planning, mortgage management, and retirement planning [4, 25].

At its core, the concept of financial literacy focuses on how to manage money wisely, 
which can be encapsulated by two key principles saving and investing. An essential rule 
is “pay yourself first,” which acknowledges putting your financial well-being left first sav-
ing and investing prior to spending on any frivolities. An extension of this line of thought 
is  investment  in  oneself  through  education  or  furthering  skill  development,  which  is 
arguably a key step toward long-term financial independence [8]. Equally important is 
being wary of bad debt-typically, a concept borrowed for non-productive purposes that 
offers no possibility of return, such as impulsive purchasing of luxury items. Conversely, 
a debit for education or even starting a business may pay off in the near or distant future. 
An emergency fund is another must-have item to stay cushioned by the financial shocks 
arising  from  unexpected  events.  Thus,  getting  our  personal  finance  in  shape  through 
wise decisions brings about security, less stress, and a peaceful and stable life [14].

The  graph  “Financial  Security  and  Stress  Indicators  (2025),”  as  shown  in  Fig.  1,  pro-
vides  a  comparative  overview  of  the  key  financial  well-being  indicators.  It  divides  the 
world from U.S. survey data. The emphasis is on at mere 29% of the global population 
that  feels  optimistic  about  its  financial  future,  indicating  a  sharp  decline  in  the  pub-
lic’s  confidence  in  recent  times  due  to  inflation,  rising  costs  of  living,  and  economic

Fig. 1  Financial security and stress indicators [9]

---

<!-- PAGE 3 -->

Page 3 of 22

instability. In the United States, 44% of the population reports that they feel financially 
secure  from  the  increase  from  the  previous  year,  yet  the  majority  of  the  people  seem 
to  be  fighting  some  level  of  financial  strain.  The  age  bracket  between  30  and  44  years 
has been cited as particularly at risk, with 77% of adults feeling financially insecure. This 
group generally encounters major expenses, such as student loans, mortgage payments, 
and  child  expenses,  thus  placing  them  under  enormous  economic  pressure.  There  are 
64%  of  Americans  feel  financially  insecure;  this,  implies  systemic  challenges  faced  in 
achieving economic stability, even in a high-income economy. In addition, 54% of adults 
in the U.S. claimed to feel stressed because of indebtedness, which significantly affects 
mental health and overall well-being [9].

This visualization again speaks of continuous financial insecurity and calls for urgent 
interventions such as debt management, financial literacy, and policy reforms that will 
build long-term economic resilience, particularly for the working population.

The conventional approach to measuring financial well-being involves manual analysis 
of records of income and expenditure, credit scores, budget worksheets, or self-reported 
surveys.  Financial  institutions  and  policymakers  rely  on  static  indicators  to  measure 
individuals’ and households’ financial health. Such static markers may include debt-to-
income  ratios,  savings  rates,  or  credit  utilization.  These  indicators  can  provide  a  gen-
eral measure, but often fail to represent true financial behavior, which is both dynamic 
and  nonlinear  [12].  On  the  contrary,  they  are  reactive,  mostly  descriptive  rather  than 
predictive, lack personal customization, and do not accommodate the real-time variabil-
ity exhibited in financial patterns. Their set limitations include an inability to scale effi-
ciently, a high degree of susceptibility to reporting errors, dependence on lengthy data 
collection  procedures,  and  an  inability  to  detect  intricate  behavioral  patterns,  such  as 
impulsive  spending  or  irregular  income  streams—behaviors  fairly  common  among  gig 
workers [20].

Artificial Intelligence (AI) and Hybrid Deep Learning models overcome the limitations 
that  hinder  real-time  data-driven  financial  well-being  assessments. These  models  han-
dle massive amounts of structured and unstructured financial data, such as transaction 
logs,  digital  receipts,  behavioral  trends,  and  lifestyle  patterns.  Hybrid  models  combine 
CNNs Convolutional Neural Networks (CNN) for feature extraction with RNNs Recur-
rent Neural Networks (RNN) for sequence modeling to capture complex temporal pat-
terns  in  income  and  expenditure  over  time.  These  can  identify  early  warning  signs  of 
an  impending  financial  freeze,  predict  the  future  financial  state,  and  offer  customized 
financial relief. Furthermore, AI systems adapt and learn with the arrival of each set of 
new  data,  thereby  increasing  their  accuracy  and  relevance.  With  this,  they  provide  far 
broader, predictive, and scalable approaches to assessing financial well-being compared 
to conventional approaches [5, 15, 17].

1.1  Contribution

The following points summarize the primary contributions of this study, focusing on the 
core innovations and technical achievements that define its impact and significance.

1.  A comprehensive dataset of 20,000 Indian individuals was developed, incorporating 
detailed  financial  information,  such  as  potential  savings  in  nine  specific  categories, 
desired savings percentage, debt ratio, occupation, and city tier.

---

<!-- PAGE 4 -->

Page 4 of 22

2.  Engineered  new  features  such  as  the  Savings  Ratio  (Desired  Savings ÷ Income)  and 
Debt Ratio (Loan Repayment ÷ Income), were shown to significantly influence model 
predictions, accounting for up to 50% of decision-making in the TabNet model. These 
types of features are rarely used in the existing financial profiling studies. Designed 
a  unique  hybrid  machine  learning  model  combining  Wide  &  Deep  learning  with 
Convolutional Neural Networks (CNNs), even though the data were non-sequential. 
This  approach  treats  financial  records  as  sequences  by  reshaping  the  data,  thereby 
allowing CNNs to learn complex patterns.

3.  Two  types  of  correlation  heatmaps  were  used  one  for  the  original  data  and  the 
anotherfor  savings-related  features  to  uncover  hidden  financial  behaviors.  For 
example,  astrong  correlation  (r  =  0.89)  was  found  between  grocery  expenses  and 
grocery savingspotential, guiding both the feature selection and model interpretation.
4.  TabNet  was  applied  to  understand  which  features  the  model  relied  on  the  most.
Surprisingly,  traditional  metrics  such  as  income  and  age  were  less  important 
thanbehavioral  indicators  such  as  debt  ratio  and  miscellaneous  savings  potential. 
Thisinsight challenges existing financial modeling practices and emphasizes the value 
ofbehavior-based features.

2  Related work

In recent years, a growing body of interdisciplinary research has sought to unravel the 
multifaceted  dimensions  of  financial  well-being  and  systemic  stability,  using  advanced 
computational  methods,  machine  learning,  and  behavioral  modeling.  The  collective 
objective is to understand financial stress better, predict financial risks, and build resil-
ient systems that bridge the gap between individual experiences and broader economic 
phenomena.

Ghashti  et  al.  [11]  conducted  a  foundational  study  in  this  direction  with  the  inten-
tion  of  identifying  the  major  sources  of  financial  stress  by  analyzing  the  responses  of 
1,874  individuals  to  a  set  of  68  mixed-type  survey  questions  collected  in  2022.  Dis-
tance-based  clustering  an  effective  tool  in  the  toolkit  of  any  financial  segmented,  was 
employed  with  a  mixed-type  distance  incorporating  variable-specific  kernel  functions 
with  cross-validated  bandwidths  in  order  to  discriminate  between  relevant  and  irrele-
vant variables effectively. The analysis yielded two major clusters: steady savers, indicat-
ing strong financial well-being and financial strivers, comprising individuals undergoing 
high financial stress. The segmentation yielded actionable insights into personal finan-
cial advices and paved the way for automated financial advising and investment genera-
tion. While individual stress is critical, Polyzos et al. [22] expanded the lens to systemic 
shocks, such as banking crises, affecting subjective well-being. By setting an agent-based 
modeling  framework  alongside  a  support  vector  machine  (SVM)  subjective  well-being 
function, researchers simulated the direct and indirect effects of economic downturns, 
such  as  income  loss,  unemployment,  and  psychological  distress.  However,  the  associ-
ated research findings, show that welfare losses from bank failures often exceed the fiscal 
cost of government bailouts. They further underscored the asymmetry in losses among 
various  segments  of  the  population,  thus  revealing  the  social  complexity  underlying 
economic policymaking. Gensler & Bailey [10] focused on the emerging systemic risks 
brought about by the widespread adoption of deep learning-based systems in financial 
ecosystems,  mapping  this  impact  across  five  transmission  pathways.  A  paradox  was

---

<!-- PAGE 5 -->

Page 5 of 22

brought  out:  while  these  models  provide  stellar  levels  of  prediction  and  efficient  per-
formance, they simultaneously increase interconnectedness within the systems and may 
even lend new forms of fragility to these systems. The study concluded that traditional 
regulatory frameworks are insufficient for the evolving challenges, and it proposed that 
policy tools should be reconsidered to protect the stability of the financial system in the 
AI  age.  To  complement  this,  Alessi  and  Savona  [2]  addressed  the  technical  limitations 
of  conventional  financial  risk  models.  They  state  that  traditional  empirical  methods 
are  incapable  of  representing  the  complex,  nonlinear,  and  multidimensional  nature  of 
financial data. The imbalanced and high-dimensional nature of datasets makes them an 
ideal  domain  for  machine  learning,  which  provides  a  more  robust  solution.  However, 
despite being extraordinarily good in terms of predictive accuracy, such models, which 
are largely taken to be black boxes, ironically remain the least used in the assessments of 
mainstream  financial  stability,  primarily  due  to  their  perceived  lack  of  interpretability, 
thus signaling the gap between innovation and regulatory acceptance. To address these 
issues,  Khunger  [16]  proposed  a  deep  learning-based  framework  for  financial  stress 
testing  Their  architecture,  Correlation  CNN-LSTM,  combines  both  quantitative  and 
qualitative  indicators.  The  model  was  highly  accurate  with  an  almost  negligible  train-
ing loss (0.0013) and testing loss (0.003). It predicts core financial variables fairly well. 
The model was able to decrease major financial risk types, such as credit, liquidity, mar-
ket, and operational risks, to a great extent, thereby furthering the usefulness of financial 
risk  measurements  and  systemic  resilience.  Building  on  this,  Shi  et  al.  [23]  developed 
the Hybrid Financial Risk Predictor (HFRP), which is a model similar to the CNN and 
LSTM architectures but is especially useful in combining numerical data with financial 
text  analytics.  Similar  to  the  earlier  setup,  it  achieved  very  high  accuracy  and  stability 
with  training  and  testing  losses  again  posted  at  0.0013  and  0.003,  respectively.  It  pro-
vided accurate forecasts for important variables, such as revenue, net income, and EPS, 
while also mitigating different categories of risks. The hybrid nature of the model shows 
how combining data modalities can enrich the provisions of risk information, that can 
be used to make dependable financial decisions. Further refinement of model selection 
led to the development by Elhoseny et al. [7] of a novel Adaptive Whale Optimization 
Algorithm with Deep Learning (AWOA-DL) for the prediction of financial distress. The 
three-step pipeline, namely data preprocessing, hyperparameter optimization based on 
AWOA, and prediction using a multilayer perceptron-based deep neural network, was 
validated on four datasets. With an average accuracy of 95.8%, the models were found 
to  be  superior  to  the  classical  methods,  with  corresponding  benchmark  accuracies 
of  93.8%,  89.6%,  84.5%,  and  78.2%. This  study  went  a  long  way  in  supports  the  notion 
that  evolutionary  optimization  techniques  can  significantly  improve  the  accuracy  and 
robustness of deep learning models in finance. In continuation with predictive model-
ing  for  distress  scenarios,  Naved  et  al.  [21]  dealt  with  bankruptcy  prediction  aided  by 
machine learning and metaheuristic optimization. This research applied the Histogram 
Gradient  Boosting  Classification  (HGBC)  model  and  hybridized  it  with  three  optimi-
zation algorithms: Snake Optimization Algorithm (SOA), Gradient-Based Optimization 
(GBO),  and  Bonobo  Optimization  Algorithm  (BOA),  resulting  in  the  three  hybridized 
models HGSO, HGGB, and HGBO, respectively. With pure HGBC, precision was 0.940, 
while  HGBO  and  HGGB  increased  it  to  0.950  and  0.960,  respectively.  However,  the 
HGSO model stands out with the highest precision level of 0.980, establishing it as an

---

<!-- PAGE 6 -->

Page 6 of 22

Fig. 2  Proposed system to detect and classify the financial status

Table 1  Categorization and description of features used for financial well-being analysis
Category
Income & demographics

Feature
Income
Age
Occupation
Rent
Loan_Repayment
Insurance
Desired_Savings
Disposable_Income

Description
Monthly income of the individual
Age in years
Type of employment or job role
Monthly rent payments
Monthly loan repayment obligations
Insurance premiums paid monthly
Targeted monthly savings amount
Remaining income after deducting all expenses

Monthly expenses

Financial goals & savings

elite  early  bankruptcy  detector  and  holds  great  promise  for  the  preemptive  mitigation 
of  financial  risk.  Finally,  Akash  et  al.  [1]  study  the  relationship  between  systemic  risk 
and  financial  indicators  through  a  regression  study  of  Yahoo  stock  market  data.  With 
liquidity, solvency, profitability, and risk exposure, a strong positive correlation is found, 
mainly between liquidity and profitability, indicating that firms with a high liquidity level 
tend to perform well financially. The regression also shows that as much as 94% of the 
variance in profitability can be predicted from these indicators, and price-earnings (PE) 
ratios are affected mostly by stock price trends. They further emphasized that compre-
hensive financial analysis ensures risk management for long-term financial stability.

3  Proposed pipeline to analyse the financial status

The  pipeline  proposed  in  this  section  helps  understand  and  classify  people  based  on 
their financial behavior. As shown in Fig. 2, different deep learning models are applied 
to  the  data  to  learn  higher-level  abstractions.  To  further  increase  performance,  hybrid 
models are established by two or several existing neural architectures and finally the sys-
tem assigns individuals to the three major financial states of Financially At-Risk, Finan-
cially Stable, and Financially Secure.

3.1  Financial dataset description

The  data  contains  detailed  information  on  the  financial  and  demographic  aspects  of 
20,000 individuals from India. It includes details on monthly income, expenditure pat-
terns, goals for savings, and potentials savings in categories such as groceries, transport, 
and healthcare as shown in Table 1. This rich dataset is well suited for personal finance

---

<!-- PAGE 7 -->

Page 7 of 22

behaviors,  cost-optimization  opportunities,  and  predictive  model  developments  in 
financial planning. As a wider snapshot of expenditures and their present saving capac-
ity,  the  dataset  may  act  as  an  important  resource  for  researchers,  data  scientists,  and 
financial analysts interested in the Indian financial industry [13].

Additional supporting features include Dependents, which signify the number of peo-
ple  financially  supported  by  the  person,  and  City_Tier,  which  corresponds  to  regional 
economic disparities by assigning cities into tiers. Expenses from the dataset were finely 
detailed and split by month for various categories, including Groceries, Transport, Eat-
ing_Out,  Entertainment,  Utilities,  Healthcare,  Education,  and  Miscellaneous.  These 
are crucial for estimating Potential Savings, which is an assessment of opportunities to 
reduce  spending  and  thereby  improve  financial  outcomes.  Furthermore,  Desired_Sav-
ings_Percentage functions as a subjective metric for financial goal setting, thereby assist-
ing in measuring the gap between the desired and actual saving behavior. Together, these 
variables support the study of financial wellness and spending patterns fairly thoroughly.

3.2  Data preprocessing and visualization of financial data

Several  preprocessing  steps  are  required  to  effectively  prepare  dataset  for  machine-
learning  models.  First,  categorical  features  such  as  “Occupation”  and  “City_Tier”  are 
Label Encoded so as to convert categories represented by textual characters into numer-
ical values without losing relational semantics, thus allowing the algorithms to process 
them. Subsequently, feature engineering is applied to create new meaningful variables, 
such  as  the  Savings  Ratio  (Desired_Savings  divided  by  Income)  and  Debt  Ratio  (Loan 
Repayment  divided  by  Income). These  ratios  provide  normalized  insight  into  personal 
saving  behavior  and  financial  liability,  so  that  the  model  reviews  personal  financial 
health across various income levels. Finally, standardization was applied to all numerical 
features to rescale the data to have a mean of 0 and a standard deviation of 1. In this way, 
larger measurements do not dominate smaller ones and help in faster convergence and 
more stable learning using gradient-based algorithms. These steps boost the goodness of 
prediction for the dataset thus, models can learn more efficiently and accurately.

As  presented  in  Fig.  3,  the  graph  titled  Income  Distribution  with  Mean  and  Median 
provides  a  visual  perception  of  how  the  incomes  of  individuals  are  distributed  within 
this  particular  dataset.  The  distribution  is  highly  right-skewed;  this  means  that,  while 
most individuals earn lower and moderate incomes, a small number of people earn very 
high  incomes,  pulling  the  tail  of  the  distribution  to  the  right.  This  is  further  validated 
by the fact that the mean income (41,585) is above the median (30,185), which is a well-
known feature of skewed data. The importance of this graph lies in its implications for 
the statistical analysis and model building. In a skewed dataset, such as this, the median 
often acts as a better measure of central tendency than the mean and is especially used 
for  describing  the  income  of  a  typical  individual.  In  addition,  this  skewness  advocates 
employing normalization techniques (for example, log transformation) to income values 
before feeding such features to machine-learning algorithms to reduce bias and improve 
convergence.  The  application  of  this  skew  can  result  in  different  feature  engineering 
strategies, such as Income brackets or percentiles, for example, allowing models to bet-
ter  distinguish  between  low-,  middle-,  and  high-income  groups.  Ultimately,  the  graph 
conveys that income data needs to be treated with care to avoid distortions in income-
based predictions and ensure that models learn in a fair and balanced manner.

---

<!-- PAGE 8 -->

Page 8 of 22

Fig. 3  Income distribution with mean & median

Fig. 4  Correlation heatmap of numerical features

The  correlation  heatmap  in  Fig.  4  provides  a  detailed  view  of  the  interrelationships 
among all the numerical features in the personal finance dataset. One of the key obser-
vations is the positive correlation of Income with the following expense categories: gro-
ceries (0.99), insurance (0.94), education (0.79), and healthcare (0.94). This means that 
income  goes  up,  and  so  does  expenditure  of  the  individuals  across  these  categories-a 
proportional spending style. There are high positive correlations between Potential Sav-
ings and Income across all categories (groceries, utilities, education, etc.), as well as the 
actual  expenditures  for  these  categories  (≥ 0.75).  For  example,  Potential_Savings_Gro-
ceries  correlates  at  0.89,  and  Potential_Savings_Utilities  at  0.82,  with  actual  spending, 
meaning that potential savings are calculated as fraction of current spending, which is 
correlated  with  income.  Similarly,  Disposable_Income  positively  correlates  with  desire

---

<!-- PAGE 9 -->

Page 9 of 22

savings  (0.86)  and  income  (0.88),  which  is  logical:  those  with  higher  residual  income 
after  expenses  tend  to  aim  for  higher  savings.  Desired_Savings_Percentage,  however, 
moderately correlates with Income (0.35), and hence, saving intent (as a proportion of 
income) varies independently of actual income levels and probably reflects behavior or 
attitudes.  The  heatmap  also  reveals  clusters  that  comprise  highly  correlated  features, 
such as expenses (Groceries, Transport, Healthcare, etc.) and Potential Savings variables. 
Such clusters could imply multicollinearity, which is important to consider when making 
decisions about feature selection or dimensionality reduction in predictive modeling.

The potential Savings correlation heatmap in Fig. 5 shows moderate to strong positive 
correlations across categories, mostly ranging from 0.60 to 0.70. For example, Potential_
Savings_Groceries has a correlation of 0.70 with Transport, 0.68 with Eating_Out, and 
0.69 with Miscellaneous. This implies that people who can save in one category tend to 
show a similar potential to others. This observation hints at higher-level financial behav-
ior  groups:  people  who  manage  spending  of  discretionary  nature  well  in  one  category 
typically  display  capacity  in  others  as  well.  Interestingly,  Potential_Savings_Education 
shows the overall lowest correlation compared to other categories, such as Eating_Out 
(0.49)  and  Healthcare  (0.50),  which  may  reflect  that  it  is  more  of  the  planned  or  non-
discretionary type of expense that varies much on the basis of life stage or structure of 
the household. The declining correlation of educational savings potential with other cat-
egories constitutes an argument that educational expenses are less substitutable and less 
behavior-driven, as opposed to lifestyle-related expenses. The utility of this heatmap lies 
in its importance for dimensionality reduction and feature selection for predictive mod-
eling, with the majority of features being highly correlated and probably suffering from 
multicollinearity.  Hence,  could  be  resolved  by  PCA  or  regularization  to  avoid  overfit-
ting of the model. Clustering of these variables can be used in the definition of compos-
ite  indices  of  financial  behavior  or  in  the  segmentation  of  user  profiles,  both  of  which 
are extremely useful in applications such as personalized financial planning or targeted 
intervention strategies.

Fig. 5  Correlation heatmap of potential saving features

---

<!-- PAGE 10 -->

Page 10 of 22

A  bar  chart  titled  “Average  Monthly  Expenses  by  Occupation”  in  Fig.  6  compares 
average  monthly  spending  for  Groceries,  Transport,  and  Healthcare  for  a  range  of 
occupational  groups:  Professional,  Retired,  Self-Employed,  and  Student.  The  trend  in 
the  data  remains  consistent  throughout  the  chart;  groceries  have  the  highest  average 
monthly expenses for all occupational categories, more than ₹5,000. This suggests that 
food-related  expenses  mostly  take  precedence  as  a  financial  consideration,  regardless 
of  employment  situation.  Once  again,  transportation  comes  next,  and  then  healthcare 
maintains a relatively constant level for all groups at ₹1,600–₹1,700. This presentational 
view  shows  that  there  seems  to  be  little  variation  among  the  different  occupational 
groups  in  the  expenditures  for  these  essentials,  which  might  insinuate  that  lifestyle 
expenses are more or less the same due to possibly unified pricing or almost equivalent 
access levels.

The significance of the graph lies in its implications for personalized financial planning 
and  targeted savings  interventions. Social spending patterns, depending upon occupa-
tion, may, therefore, also be largely similar, since similar social spending baskets, policy-
makers, app developers, or financial institutions could target generic budgeting or saving 
advice that applies to almost all end-buyer segments. The graph also serves as a starting 
point for the analysis of spending efficiency or potential savings with reference to occu-
pational profiles.

3.3  Feature scaling

To scale the important features, the TabNet Feature Importance illustrated in Fig. 7 indi-
cates the relative contribution of each feature toward the model’s prediction of financial 
categorization or stability [18]. Debt_Ratio was the predominant feature, accounting for 
almost 50% of the decision weight of the model. The dominant position of Debt_Ratio 
clearly shows that the amount of income paid for loans is perhaps the most important 
indicator  of  financial  well-being  or  risk.  Potential_Savings_Miscellaneous  and  Savings 
Ratio  are  key  features,  indicating  that  miscellaneous  cash  spending  and  the  propor-
tion  of  income  saved  are  strong  predictors  of  financial  wellbeing.  Other  features  such 
as  Desired_Savings_Percentage,  Insurance,  Occupation,  and  Potential_Savings_Utili-
ties  exhibit  moderate  importance,  indicating  that  while  they  impact  the  outcome,  this 
influence can be situational and somewhat indirect. Surprisingly, basic variables such as

Fig. 6  Average monthly expenses by occupation

---

<!-- PAGE 11 -->

Page 11 of 22

Fig. 7  Feature importance using TabNet

Income, Disposable_Income, and Age show minimal importance, which could arise with 
some of their information being indirectly captured or normalized through constructed 
ratios,  such  as  the  Debt  Ratio  or  Savings  Ratio.  Similarly,  the  standalone  categories  of 
Groceries,  Transport,  and  Healthcare  show  low  predictive  power,  reinforcing  that  the 
model finds more value in composite financial behavior (in terms of ratios and potential 
savings) than in raw monetary values.

The  importance  of  this  section  lies  in  guiding  the  selection  of  features,  intervention 
strategies, and model interpretability. For instance, financial advisory systems may focus 
on  monitoring  and  reducing  users’  debt  ratios  and  increasing  savings  in  discretionary 
areas  at  the  model  level  rather  than  simply  increasing  users’  income.  It  also  validates 
feature engineering (e.g., ratio-based variables) that help with the model as well as real-
world insight.

3.4  Classifiers for analysing the pattern of finance

{

Rd

x1, x2, . . . , xn},  where  each  xi ∈

To model and classify patterns from the Indian Personal Finance and Spending Habits 
dataset, we adopted a sequence of advanced deep-learning architectures, each tailored 
to the unique characteristics of the data. The dataset, consisting of both categorical and 
numerical features such as income, investment preference, credit card usage, and spend-
ing  tendencies,  was  first  preprocessed  and  transformed  into  a  normalized  numerical 
form  X =
  represents  a  d-dimensional  feature 
vector  for  the  i-th  individual.  We  began  by  applying  Deep  Neural  Networks  (DNNs) 
and  Fully  Connected  Neural  Networks  (FCNNs),  which  utilized  multiple  hidden  lay-
ers  with  ReLU  activation  f (x) = max(0, x)  to  learn  complex,  nonlinear  feature  inter-
actions [20]. To capture localized feature dependencies, we reshaped the tabular input 
into  pseudo-sequences  and  applied  Convolutional  Neural  Networks  (CNNs),  where 
the  convolution  operation  was  defined  as  hi = σ
,  allow-
ing  the  model  to  learn  spatial  hierarchies  among  grouped  financial  indicators.  Given 
the  potential  temporal  influence  on  decision-making  (e.g.,  prior  savings  affecting  cur-
rent  investments),  we  integrated  Recurrent  Neural  Networks  (RNNs)  and  advanced 
them  using  Gated  Recurrent  Units  (GRUs)  and  Bidirectional  Long  Short-Term  Mem-
ory  networks  (BiLSTMs),  where  the  cell  state  updates  are  governed  by  gates  such  as 
1, xt] + bf ),  enabling  effective  modeling  of  sequential  financial 
ft = σ (Wf ·

j=1wj ·

1 + b

xi+j

(∑

[ht

)

−

−

k

---

<!-- PAGE 12 -->

Page 12 of 22

Algorithm 1  Feature importance using TabNet

W T

widex + W T

behaviors.  Recognizing  that  some  survey  responses  might  exhibit  long-range  depen-
dencies,  BiLSTM  offers  a  bidirectional  context  across  time  [3].  To  simultaneously 
benefit  from  memorization  and  generalization,  we  implemented  at  the  Wide  &  Deep 
model, where the prediction was computed as  y = σ
, where 
x  represents  the  raw  features  and  φ (x)  is  the  transformation  learned  by  the  DNN. 
We  extended  this  paradigm  by  combining  the  wide  component  with  sequential  layers 
such  as  BiLSTM,  CNN,  GRU,  and  Attention,  forming  Wide  &  Deep  +  BiLSTM,  Wide 
&  Deep  +  CNN,  and  Wide  &  Deep  +  Attention  models,  each  designed  to  simultane-
ously  learn  low-level  interactions  and  temporal  abstractions  [22].  Furthermore,  we 
incorporated autoencoders to compress the high-dimensional feature space into a latent 
representation  z = fenc (x),  followed  by  decoding 
x = fdec (z),  using  the  reconstruc-
2
tion loss  Lrec =
 to guide representation learning. These encodings are then 
fed  into  classifiers  or  RNNs  for  downstream  classification.  Hybrid  architectures,  such

deepφ (x)
)

−

(

(cid:31)

x

x

∥

∥

(cid:31)

---

<!-- PAGE 13 -->

Page 13 of 22

Algorithm 2  Wide & deep + BiLSTM for financial behavior classification

as  CNN  +  LSTM  and  CNN  +  MLP,  were  used  to  first  extract  patterns  using  convolu-
tional layers and subsequently model sequential or dense interactions through LSTM or 
MLP  units.  To  enhance  attention  toward  critical  features  (e.g.,  those  influencing  debt 
or savings behavior), we employed Attention-based CNNs and Wide & Deep + Atten-
tion  mechanisms,  where  the  attention  score  was  computed  as  α i = exp(ei)
j exp(ej )   with

ei = vT tanh (W xi + b),  dynamically  weighting  the  key  features  in  the  decision  pro-
cess. Collectively, this ensemble of models enables comprehensive representation learn-
ing from heterogeneous personal finance attributes, capturing both static and dynamic 
behavioral patterns to yield robust classification outcomes [19].

∑

A  hybrid  architecture  combining  a  Wide  &  Deep  learning  framework  with  a  Con-
volutional  Neural  Network  (CNN)  is  shown  in  Algorithm  1  for  classifying  individuals 
based on their financial behavior. In this manner, a model can capture the interactions 
of  low-order  features  in  parallel  with  computations  to  extracting  patterns  of  higher 
order  through  one-dimensional  convolutions  applied  to  appropriately  reshaped

---

<!-- PAGE 14 -->

Page 14 of 22

financial-feature vectors. Because the data are structured in tabular format, wherein the 
absence of temporal ordering is associated with embedded local correlations, this archi-
tecture  is  ideal  for  such  cases.  This  algorithm  provides  the  details  for  pre-processing, 
architectural  flow,  and  optimization  to  be  used  for  training  the  Wide  &  Deep + CNN 
model on multi-financial-classification tasks [26].

Algorithm  2  provides  an  outline  of  building  and  training  the  hybrid  Wide  &  Deep 
model using the BiLSTM network for financial behavior classification. This model uses 
the  generalization  and  memorization  of  the  third  layer.  Hence,  the  wide  layer  is  con-
sidered for memorization and pooling the specification of feature interactions, and the 
deep BiLSTM layer is considered for generalization by militating sequential or pseudo-
sequential  patterns  inherent  in  behavioral  financial  data.  The  algorithm  starts  with 
structured preprocessing, with the distortion of wide and deep components in parallel, 
which are later joined and optimized using a supervised learning procedure with Adam 
optimizer [6].

4  Result and analysis

This section presents the empirical outcomes obtained by applying various deep learn-
ing classifiers to the Indian personal finance and spending habit dataset.

In Table 2, the training and validation performance metrics reveal several key insights 
into model behavior on the Indian personal finance dataset. First, models such as Wide 
&  Deep + CNN,  Wide  &  Deep + BiLSTM,  and  BiLSTM  not  only  achieved  the  highest 
validation accuracies (≥ 0.988), but also maintained very low validation losses (~ 0.025–
0.026), indicating their strong generalization ability. This suggests that models capable of 
both memorization (via wide components) and sequence modeling (via BiLSTM/CNN) 
are  particularly  effective  at  capturing  the  complex  interdependencies  among  features, 
such  as  income,  expense  categories,  city  tier,  and  savings  behavior.  The  minimal  gap 
between  the  training  and  validation  metrics  in  these  models  indicated  stable  learning 
and a low risk of overfitting.

Train loss

0.3006
0.0525
0.0379
0.0324
0.0219
0.0283
0.0457
0.0602
0.2798
0.0480

Table 2  Performance comparison of deep learning models on financial data
Model
CNN
RNN
DNN
BiLSTM
GRU
Wide & Deep
Autoencoder + Classifier
FCNN
Attention-CNN
Residual MLP
Hybrid CNN + MLP
Hybrid CNN + LSTM
Hybrid CNN + GRU
Hybrid RNN + BiLSTM
Autoencoder + RNN
Wide & Deep + BiLSTM
Wide & Deep + CNN
Wide & Deep + RNN
Wide & Deep + Attention

Train accuracy
0.8788
0.9773
0.9845
0.9851
0.9905
0.9916
0.9827
0.9743
0.8835
0.9798
0.7165
0.8717
0.8783
0.9834
0.9643
0.9880
0.9937
0.9772
0.9879

Val accuracy
0.8687
0.9791
0.9766
0.9884
0.9859
0.9831
0.9803
0.9762
0.8697
0.9578
0.7025
0.8544
0.8622
0.9781
0.9584
0.9900
0.9944
0.9844
0.9897

0.3232
0.2975
0.0403
0.0856
0.0305
0.0268
0.0571
0.0354

− 94653360.0

Val loss

0.3182
0.0440
0.0511
0.0256
0.0255
0.0456
0.0438
0.0683
0.2901
0.1066
− 103436192.0
0.3617
0.3315
0.0464
0.0941
0.0261
0.0259
0.0441
0.0368

---

<!-- PAGE 15 -->

Page 15 of 22

By  contrast,  models  such  as  CNN,  Hybrid  CNN + GRU,  and  Attention-CNN  show 
larger  validation  losses  (~ 0.29–0.33)  and  slightly  lower  accuracies  (~ 0.86),  reflect-
ing  their  inability  to  fully  capture  high-dimensional  financial  patterns.  This  limitation 
likely stems from their reliance on local feature extraction without recurrent memory or 
dynamic feature weighting, which are essential given the dataset’s multi-feature correla-
tions (e.g., income vs. groceries and, income vs. savings).

Moreover, the Hybrid CNN + MLP model is severely unstable, showing negative loss 
values  in  the  order  of  millions,  indicating  a  critical  training  failure,  possibly  due  to 
incompatible layer integration or numerical overflow. Interestingly, even simpler models, 
such as RNN, FCNN, and Autoencoder + Classifier, maintain robust validation accuracy 
(> 0.95) and low loss, highlighting that even without sophisticated hybridization, models 
that can extract latent feature relationships perform well because of the structured and 
patterned nature of the dataset.

In summary, the performance table clearly supports the conclusion that models with 
architectural components for hierarchical abstraction (deep layers), temporal/sequential 
modeling  (RNN,  BiLSTM),  and  feature  attention  or  selection  (Wide  &  Deep,  TabNet) 
are the most suitable for this type of financial behavior data.

Additionally,  the  learning  curves  and  confusion  matrix  of  the  best-performing  mod-
els are also presented in Fig. 8, where both hybrid models show a good fit of models in 
training and validation.

The overall performance of the models on the Indian Personal Finance and Spending 
Habits dataset reflects the nature of the data, which are highly structured, multivariate, 
and  deeply  interdependent,  as  shown  in  Table  3.  Models  such  as  BiLSTM,  GRU,  and 
hybrid architectures such as Wide & Deep + CNN, Wide & Deep + BiLSTM, and TabNet 
achieve perfect or near-perfect scores (F1 ≈ 0.99–1.00), showcasing their ability to model 
complex  feature  interactions,  temporal  dependencies,  and  hierarchical  relationships. 
These models excel because the dataset contains patterns such as strong positive corre-
lations between income and multiple expense categories (e.g., rent, groceries, transport) 
and  between  income  and  savings,  which  are  best  captured  by  architectures  capable  of 
nonlinear representation learning and memory mechanisms. For instance, the BiLSTM 
and GRU models retain long-range dependencies and are robust to feature skewness and 
class imbalance, explaining their 1.00 precision, recall, and F1 scores.

Deep neural models such as DNN, FCNN, and Residual MLP also perform competi-
tively  (F1 ≈ 0.94–0.97)  owing  to  their  capacity  to  learn  hierarchical  abstractions  from 
numeric input features. By compressing high-dimensional data into efficient latent rep-
resentations,  autoencoder-based  models  also  preserve  essential  variance  while  reduc-
ing  redundancy,  resulting  in  F1  scores  of  up  to  0.98. The  Wide  &  Deep  model  and  its 
enhanced  hybrids  benefit  from  combining  memorization  (wide  component)  with  gen-
eralization (deep component), particularly in a domain such as personal finance where 
both rare and frequent patterns coexist.

On  the  other  hand,  CNN-based  architectures,  including  Hybrid  CNN + GRU/LSTM 
and  Attention-CNN,  show  lower  performance  (F1 ≈ 0.84–0.86),  and  in  the  case  of 
Hybrid  CNN + MLP,  they  drastically  underperform  (F1 ≈ 0.28).  This  underperformance 
likely  stems  from  CNNs’  limited  capacity  of  CNNs  to  model  long-range  dependencies 
in  non-spatial  tabular  data,  making  them  less  suited  for  financial  datasets  that  require 
an understanding of contextual interactions across features. Moreover, models such as

---

<!-- PAGE 16 -->

Page 16 of 22

Fig. 8  Analysis of the best performing models

Table 3  Examination of the trained classifiers for analysing financial dataset
Precision Recall F1-Score
Precision Recall F1-Score Model
Model
0.97
0.97
FCNN
0.90
CNN
0.84
0.92
Attention-CNN
0.98
RNN
0.92
0.97
Residual MLP
0.98
DNN
0.99
0.99
TabNet
1.00
BiLSTM
0.33
0.23
Hybrid CNN + MLP
1.00
GRU
0.81
0.92
Hybrid CNN + LSTM
Wide & Deep
0.99
0.82
0.90
Hybrid CNN + GRU
Autoencoder + Classifier 0.97
1.00
1.00
Wide & Deep + CNN
0.98
Hybrid RNN + BiLSTM
0.99
Wide & Deep + RNN
Autoencoder + RNN
0.99
0.94
0.99
Wide & Deep + Attention 0.99
Wide & Deep + BiLSTM 0.99

0.86
0.99
0.97
1.00
1.00
0.98
0.98
0.98
0.95
0.99

0.97
0.86
0.94
0.99
0.28
0.84
0.85
1.00
0.99
0.99

0.84
0.99
0.97
1.00
1.00
0.98
0.98
0.98
0.96
0.99

Attention-CNN  and  Hybrid  CNN + LSTM  may  suffer  from  overfitting  or  ineffective 
attention calibration, particularly when feature importance is unevenly distributed.

Likewise,  Table  4  contains  precision,  recall,  and  F1-score  data  for  the  applied  deep 
learning architectures evaluated in the financial health categories of Financially At-Risk, 
Financially Secure, and Moderately Stable.

---

<!-- PAGE 17 -->

Page 17 of 22

The  outstanding  performance  of  advanced  sequence-based  models  such  as  BiLSTM, 
GRU, and various hybrid architectures (e.g., Wide & Deep + CNN, Wide & Deep + BiL-
STM) on this dataset likely stems from the rich multivariate structure and strong inter-
feature correlations of the dataset. Seq-models, such as RNNs, LSTMs, and GRUs, are 
adept at capturing complex, context-dependent patterns with sequential or time-related 
features,  allowing  them  to  tease  apart  subtle  distinctions  among  classes.  Indeed,  RNN 
achieved  nearly  perfect  metrics  across  categories,  whereas  BiLSTM  and  GRU  reached 
near-ideal precision, recall, and F1 across all classes. These models can effectively model 
interactions  (e.g.,  how  income  interacts  with  multiple  expense  categories  and  demo-
graphics) and are robust to the noise and outliers common in skewed financial data. In 
contrast, simpler CNNs and hybrid shallow-deep models may struggle to fully represent 
these  multifaceted  relationships.  For  example,  CNNs  showed  drops  in  F1  for  “Moder-
ately Stable” (~ 0.67), likely because convolutional filters alone do not adequately model 
feature interactions over all input vectors. Similarly, models such as Attention-CNN or 
Hybrid  CNN+LSTM/GRU  improved  stability  moderately  but  still  lagged  behind  full 
RNN  architectures.  Autoencoders  with  classifiers  also  scored  well  (~ 0.97  F1)  because 
they adaptively compressed the high-dimensional skewed input features before classifi-
cation, effectively performing manifold learning that benefits downstream classification. 
TabNet, with its sequential attention mechanism over tabular data, performed extremely 
well (F1 ~ 0.99) by dynamically selecting and weighting the relevant feature subsets.

Similarly, Fig. 9 illustrates the ROC-AUC scores of various deep learning and hybrid 
models developed for financial health prediction. ROC-AUC (Receiver Operating Char-
acteristic - Area Under the Curve) is a critical metric that evaluates a model’s ability to 
distinguish between different classes and in this case, individuals categorized as Finan-
cially Secure, Moderately Stable, or Financially At-Risk. Models such as BiLSTM, GRU, 
and the Wide & Deep + CNN hybrid achieved a perfect ROC-AUC score of 1.0000, indi-
cating  flawless  discrimination  across  financial  well-being  categories.  This  underscores 
their  exceptional  reliability  in  real-world  deployment  in  personal  finance  advisory  sys-
tems.  Other  top-performing  models  include  TabNet,  RNN,  Wide  &  Deep + BiLSTM, 
Autoencoder + Classifier,  and  Wide  &  Deep + RNN,  all  exceeding  a  score  of  0.999, 
reflecting near-perfect classification ability. Traditional architectures such as CNN and 
hybrids  such  as  CNN + LSTM  and  CNN + GRU  showed  relatively  lower  but  still  com-
mendable ROC-AUC values, ranging from 0.9286 to 0.9428. This finding suggests room 
for  improvement,  particularly  in  handling  the  nonlinearity  and  complexity  of  financial 
behavior  patterns.  The  graph  highlights  a  clear  trend:  hybrid  models  leveraging  archi-
tectural synergies such as Wide & Deep sequence models) outperform standalone mod-
els.  This  aligns  with  contemporary  machine  learning  theory,  which  posits  that  hybrid 
architectures can capture both static and sequential patterns in complex datasets crucial 
for financial well-being assessments that depend on both categorical traits and spending 
behaviors. Overall, the graph provides compelling evidence for the superiority of hybrid 
deep  learning  architectures  in  achieving  robust  financial  classification  and  actionable 
insights  for  researchers  and  practitioners  aiming  to  build  scalable  and  interpretable 
financial decision support systems.

Furthermore,  Table  5  compares  existing  work  on  segmentation,  systemic  risks,  and 
stress  testing  with  the  proposed  framework  that  uses  large-scale  real-world  data  and 
hybrid, highly synergistic deep learning models to segregate individual clients as either

---

<!-- PAGE 18 -->

Page 18 of 22

GRU

RNN

DNN

FCNN

BiLSTM

Wide & Deep

Autoencoder + Classifier

Table 4  Class-wise performance metrics of deep learning models for financial health classification
Model
F1-Score
0.99
CNN
0.92
0.67
0.99
1.00
0.98
0.96
0.99
0.96
1.00
1.00
0.99
1.00
1.00
0.99
0.98
1.00
0.98
0.97
0.99
0.97
0.96
0.99
0.96
0.98
0.93
0.67
0.88
0.99
0.94
0.99
1.00
0.99
0.98
0.92
0.62
0.98
0.92
0.65
0.97
0.99
0.97
0.94
0.98
0.93
0.99
1.00
0.99
1.00
1.00
0.99

Class
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable

Precision
0.99
0.88
0.85
0.98
1.00
0.98
0.97
0.99
0.98
1.00
1.00
1.00
1.00
1.00
1.00
0.99
0.99
0.98
0.95
1.00
0.97
0.94
0.99
0.97
0.97
0.87
0.92
1.00
0.99
0.92
0.99
1.00
0.98
0.98
0.86
0.94
0.98
0.87
0.85
0.95
0.99
0.98
0.90
0.99
0.93
1.00
1.00
0.98
1.00
1.00
0.99

Recall
1.00
0.97
0.56
1.00
0.99
0.98
0.95
1.00
0.95
1.00
1.00
0.99
1.00
1.00
0.99
0.96
1.00
0.98
0.99
0.99
0.97
0.98
0.99
0.94
0.99
0.99
0.53
0.79
0.99
0.97
0.99
1.00
1.00
0.97
0.99
0.46
0.97
0.97
0.53
0.99
1.00
0.96
0.98
0.98
0.92
0.99
0.99
1.00
1.00
1.00
0.99

Wide & Deep + BiLSTM

Hybrid RNN + BiLSTM

Wide & Deep + CNN

Autoencoder + RNN

Hybrid CNN + LSTM

Hybrid CNN + GRU

Attention-CNN

Residual MLP

TabNet

---

<!-- PAGE 19 -->

Page 19 of 22

Table 4  (continued)

Model
Wide & Deep + RNN

Wide & Deep + Attention

Class
Financially At-Risk
Financially Secure
Moderately Stable
Financially At-Risk
Financially Secure
Moderately Stable

Precision
0.98
0.99
1.00
0.98
1.00
0.98

Recall
1.00
1.00
0.96
1.00
1.00
0.99

F1-Score
0.99
0.99
0.98
0.99
1.00
0.99

Fig. 9  ROC-AUC score of financial health prediction models

Financially  Secure,  Moderately  Stable,  or  Financially  At-Risk.  It  is  superior  to  existing 
approaches  in  all  key  performance  metrics,  allowing  for  greater  interpretability  and  a 
consequential  deployment  scope  for  integration  into  financial  advisory  and  wellness 
platforms.

5  Conclusion, limitations, and future scope

This  study  proposes  a  novel  hybrid  deep  learning  framework  for  carrying  out  robust 
financial profiling of persons into Financially Secure, Moderately Stable, and Financially 
At-Risk. Using a large-scale dataset of 20,000 Indian individuals with income, expenses, 
savings, and demographic features, this study presents the higher efficacy of advanced 
hybrid  models,  especially  Wide  &  Deep + CNN  and  Wide  &  Deep + BiLSTM.  These 
models  achieved  almost  perfect  classification  metrics  (Validation  Accuracy:  99.44%, 
F1-Score: 1.00, ROC-AUC: 1.0000), thus outperforming regular CNNs and less-complex 
hybrid models. Furthermore, the pipeline uses TabNet to improve explainability, which 
supports  transparency  during  decisions,  thus  moving  toward  real-world  applications 
such as finance advice, stress detection, and aided budgeting. However, there are some 
limitations to this work despite its impressive performance. A primary limitation is that, 
while  the  dataset  has  considerable  variables  pertaining  to  structure,  it  lacks  temporal 
sequences  or  longitudinal  financial  behaviors,  which  are  important  in  both  real-time 
financial forecasts and modeling trajectories of stress. Second, the data remained geo-
graphically and culturally confined to Indian individuals, possibly limiting the general-
izability of the models to other populations with different financial habits or economic 
systems. Furthermore, some hybrid models (e.g., CNN + MLP) were found to be unstable 
because  of  architectural  incompatibilities,  suggesting  that  rigorous  integration  should

---

<!-- PAGE 20 -->

Page 20 of 22

Table 5  Comparative analysis of existing techniques vs. the proposed hybrid deep learning 
approach for financial health classification
Dimension
Research 
objective

Proposed technique
Accurately classify individuals into 
Financially Secure, Moderately Stable, and 
Financially At-Risk using hybrid deep learn-
ing models

Existing techniques
Focused on segmentation (Researcher 1), 
welfare impact of banking crises (Researcher 
2), systemic AI risks (Researcher 3), financial 
stress testing (Researchers 5 & 6), and early 
bankruptcy prediction (Researchers 7 & 8)
Small-scale or synthetic datasets: 1,874 survey 
responses (Researcher 1), simulation data (Re-
searcher 2), or stock indicators (Researcher 9)
Survey-based (Researcher 1), macroeconomic 
indicators (Researcher 2), stock returns and 
liquidity ratios (Researcher 9)
Clustering (Researcher 1), Agent-Based + SVM 
(Researcher 2), Gradient Boosting + Optimizers 
(Researcher 8), CNN + LSTM (Researcher 5)

CNN + LSTM/GRU (Researcher 5), CNN + Text 
Analysis (Researcher 6), optimization-driven DL 
(Researcher 7)
Accuracy: ~95.8% (AWOA-DL, Researcher 7), 
Precision: 0.980 (HGSO, Researcher 8), moder-
ate ROC-AUC (CNN-based models)
Binary segmentation (Researcher 1), risk clas-
sification (Researchers 5–8)
Often criticized as black-box (Researcher 4); 
limited transparency

Dataset

Input features

Modeling 
techniques

Hybridization

Key metrics

Model output

Interpretability

Systemic insights Highlights macroeconomic resilience and

regulatory blind spots (Researcher 3)

Deployment 
readiness

Conceptual or research-stage tools; not linked 
to real-time systems

Real-world, large-scale dataset of 20,000 
Indian individuals with detailed income, ex-
penditure, savings, and demographic data
Multivariate features: income, savings 
ratio, debt ratio, monthly expenses across 
categories, city tier, occupation, etc.
15 + deep learning models including CNN, 
RNN, BiLSTM, GRU, DNN, FCNN, TabNet, 
Autoencoder-based classifiers, and Wide & 
Deep hybrids
Wide & Deep integrated with CNN, BiLSTM, 
RNN, and Attention mechanisms for joint 
memorization and generalization
Validation Accuracy: 99.44%; ROC-AUC: 
1.0000; F1-Score: 1.00 (GRU, BiLSTM, Wide & 
Deep + CNN)
Multi-class classification with granular 
breakdown of three financial health levels
Uses TabNet, feature engineering (Savings/
Debt Ratio) to improve model explainability
Supports individual-level predictions with 
potential for integration into organizational 
wellness systems
Designed for real-time financial profiling, 
robo-advisory, and employee stress mitiga-
tion platforms

be designed. While interpretability remains aided by feature selection, some stakehold-
ers  unfamiliar  with  AI  techniques  find  it  a  complex  challenge.  Several  promising  ave-
nues for future research can be explored. Real-time financial transaction data could be 
included in the pipeline, and metrics from behavioral psychology could be integrated to 
make predictions more dynamic and personalized. Enriching the dataset to contain indi-
viduals from different geographies and socioeconomic backgrounds will put the model 
on a more robust footing. The predictive pipeline can also be implemented in a mobile 
application or a financial chatbot to connect academic innovations with their practical 
deployment Finally, in sensitive areas like finance, AI deployment should be considered 
with aspects such as fairness, mitigation of biases, and transparency.
Author contributions
[AU]: Conception and design of the study, supervision of the research process, and critical revision of the manuscript 
for intellectual content.AS]: Data curation, model development, and analysis and interpretation of results.[YA]: Drafting 
of the manuscript, literature review, and visualization of findings.[AS & BK]: Editing, proofreading, and ensuring 
methodological rigor.All authors were involved in critically revising the paper for its intellectual content, approved the 
final version to be published, and agreed to be accountable for all aspects of the work, ensuring that questions related to 
accuracy or integrity were appropriately investigated and resolved.

Funding
Open access funding provided by Symbiosis International (Deemed University). (APC): Symbiosis International University, 
PUNE.

---

<!-- PAGE 21 -->

Page 21 of 22

Data availability
The data that support the findings of this study are openly available in [Kaggle.com]at  [ h t t p s  : / / w w  w . k a g g  l e . c  o m / d a t a s e 
t s / s h r i y a s h j a g t a p / i n d i a n - p e r s o n a l - fi  n a n c e - a n d - s p e n d i n g -  h a b i t s ] ( h t t p s : / w w w . k a g g l e . c o m / d a t a s e t s / s h r i y a s h j a g t a p / i n d i a 
n - p e r s o n a l - fi  n a n c e - a n d - s p e n d i n g - % 2 0 h a b i t s ) , [13].

Declarations

Ethics approval and consent to participate
Not applicable.

Consent for publication
Not applicable.

Informed consent
This study did not involves human participants.

Human and animals participants
This research did not involve any studies with human participants or animals performed by any of the authors.

Competing interests
The authors declare no competing interests.

Received: 24 October 2025 / Accepted: 2 February 2026

References
1.

3.

2.

Akash TR, Reza J, Alam MA. Evaluating financial risk management in corporation financial security systems. World J Adv 
Res Reviews. 2024;23(1):2203–13.
Alessi L, Savona R. Machine learning for financial stability. Data science for economics and finance: methodologies and 
applications. Cham: Springer International Publishing; 2021. pp. 65–87.
Behera S, Kalagudi V, Das SR. Generative AI-based financial fraud detection system. In: 2025 International conference on 
intelligent and innovative technologies in computing, electrical and electronics (IITCEE). IEEE. 2025, pp. 1–7.
Chen Z, Chen W, Smiley C, Shah S, Borova I, Langdon D, Moussa R, Beane M, Huang TH, Routledge B, Wang WY. 2021. 
Finqa: A dataset of numerical reasoning over financial data. arXiv preprint https://arxiv.org/abs/2109.00122.
Chhikara H, Chhikara S, Gupta L. Predictive analytics in finance: leveraging AI and machine learning for investment strate-
gies. In: Utilizing AI and machine learning in financial analysis. IGI Global Scientific Publishing; 2025. pp. 325–36.
6.  Dhaka P, Nagpal B. WoM-based deep bilstm: smart disease prediction model using WoM-based deep BiLSTM classifier.

5.

4.

7.

8.

Multimedia Tools Appl. 2023;82(16):25061–82.
Elhoseny M, Metawa N, Sztano G, El-Hasnony IM. Deep learning-based model for financial distress prediction. Ann Oper 
Res. 2025;345(2):885–907.
Fernando J. Financial literacy: What it is, and why it is so important to teach teens.2025.  h t t p s :  / / w w w  . i n v e s  t o p e  d i a . c  o m / t e  r 
m s / f /  fi  n a  n c i a l - l i t e r a c y . a s p

9.  Gailey A. (2024) Survey: 44% of Americans believe their finances will improve in 2025, an increase from previous years.  h t t

p s :  / / fi  n  a n c e . y  a h o o  . c o m /  n e w s /  s u r v e y  - 4 4 -  a m e r i  c a n s -  b e l i e v  e - fi   n a n c e s - 0 5 1 0 0 0 4 0 8

10.  Gensler G, Bailey L. 2020. Deep learning and financial stability. Available from SSRN 3723132.
11.  Ghashti JS, Thompson JR. The complexity of financial wellness: examining survey patterns via kernel metric learning and 
clustering of mixed-type data. In: Proceedings of the fourth ACM international conference on AI in finance; 2023, pp. 
314–322.

12.  Gregova E, Valaskova K, Adamko P, Tumpach M, Jaros J. Predicting financial distress of Slovak enterprises: comparison of

13.

selected traditional and learning algorithms methods. Sustainability. 2020;12(10):3954.
Indian personal finance and spending habits (2024).  h t t p s :  / / w w w  . k a g g l  e . c o  m / d a t  a s e t s  / s h r i y  a s h j  a g t a p  / i n d i  a n - p e r  s o n a  l - fi  n  
a n c e -  a n d - s p  e n d i  n g - h a b i t s

14.  Kalyugina S, Strielkowski W, Ushvitsky L, Astachova E. Sustainable and secure development: facet of personal financial

issues. J Secur Sustain Issues. 2015;5(2):297–304.

15.  Kaur K, Kumar Y, Kaur S. Artificial intelligence and machine learning in financial services to improve the business system. 
Computational intelligence for modern business systems: emerging applications and strategies. Singapore: Springer 
Nature Singapore; 2023. pp. 3–30.

16.  Khunger A. DEEP learning for financial stress testing: a data-driven approach to risk management. Int J Innov Stud.2022.

http://dx.doi.org/10.2139/ssrn.5146509.

17.  Kuizinienė D, Krilavičius T, Damaševičius R, Maskeliūnas R. Systematic review of financial distress identification using artifi-

cial intelligence methods. Appl Artif Intell. 2022;36(1):2138124.

18.  Li W. TabNet for high-dimensional tabular data: advancing interpretability and performance with feature fusion. In: IET 
Conference Proceedings CP915. Stevenage, UK: The Institution of Engineering and Technology; 2025, pp. 168–173.
19.  Luo A, Zhong L, Wang J, Wang Y, Li S, Tai W. Short-term stock correlation forecasting based on CNN-BiLSTM enhanced by

attention mechanism. IEEE Access; 2024.

20.  Mazancová K. Non-Traditional methods for assessing the financial situation of a farm. Econ Bus. 2024;38:68–85.
21.  Naved M, Kumar R, Saheb SS. Analyzing financial stability by predicting bankruptcy situations with machine learning. J

Artif Intell Syst Modelling. 2024;1(03):18–35.

22.  Polyzos S, Abdulrahman K, Dandu J. Effects of financial instability on subjective well-being: a preference-based approach.

Int J Soc Econ. 2021;48(7):982–98. https://doi.org/10.1108/ijse-10-2020-0693.

---

<!-- PAGE 22 -->

Page 22 of 22

23.  Shi X, Zhang Y, Yu M, Zhang L. Deep learning for enhanced risk management: a novel approach to analyzing financial

reports. PeerJ Comput Sci. 2025;11:e2661.

24.  Strutner S. (2024) Financial Management explained: scope, objectives & importance.  h t t p s :  / / w w w  . n e t s u  i t e .  c o m / p  o r t a l  / r e s

o u  r c e /  a r t i c  l e s / fi   n a n c i  a l - m  a n a g e  m e n t /  fi  n a n c  i a l -  m a n a g e m e n t . s h t m l

25.  Vipond T. (2025) Public finance.  h t t p s :  / / c o r  p o r a t e  fi  n a  n c e i n  s t i t u  t e . c o m  / r e s  o u r c e  s / e c o  n o m i c s  / p u b  l i c - fi  n a n c e /
26.  Zheng Z, Yang Y, Niu X, Dai HN, Zhou Y. Wide and deep convolutional neural networks for electricity-theft detection to

secure smart grids. IEEE Trans Industr Inf. 2017;14(4):1606–15.

Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Discover Artificial Intelligence
https://doi.org/10.1007/s44163-026-00949-2
RESEARCH Open Access
Translating artificial intelligence into socio-
economic insight: a hybrid deep learning
approach to employee financial well-being
Aakanksha Uppal1*, Anubha Srivastava2, Yashmita Awasthi3, Anjita Srivastava4 and Barkha Kakkar2
*Correspondence:
Aakanksha Uppal Abstract
aakanksha.uppal@symlaw.edu.in This study aims to translate recent advancements in hybrid artificial intelligence (AI)
1Symbiosis International (Deemed
modeling into a functional tool for assessing individual financial well-being. The
University) Pune, Symbiosis Law
School Noida Campus, Noida, objective is to develop a system that aids organizations in understanding employees’
Ghaziabad, India financial stress, with broader implications for enhancing workplace productivity and
2Institute of Technology & Science,
societal economic resilience. A deep learning pipeline was developed to classify
Mohan Nagar, Ghaziabad, India
3School of Commerce, Finance and individuals into three financial well-being categories: Financially Secure, Moderately
Accountancy, Christ University, Stable, and Financially At-Risk. The approach utilizes a structured dataset of 20,000
Bengaluru, India
Indian individuals and implements 15 advanced deep learning models, including
4Bundelkhand University, Jhansi,
India Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), Gated
Recurrent Units (GRU), Bidirectional Long Short-Term Memory (BiLSTM), and Wide &
Deep networks. Model performance was assessed using standard evaluation metrics,
including validation accuracy and ROC-AUC scores. Among the tested models, the
hybrid Wide & Deep + CNN configuration yielded the highest performance, achieving
a validation accuracy of 99.44% and a perfect ROC-AUC score of 1.0000. These results
validate the model’s capacity for robust classification and real-world applicability to
financial profiling. This study demonstrates a practical application of AI in financial
decision support systems and contributes to organizational research by offering a
scalable solution to assess and mitigate employee financial stress.
Keywords Financial well-being assessment, Deep learning, Wide & deep network,
CNN, Employee financial stress, Organizational productivity, Societal economic stability
1 Introduction
In the context of organizational dynamics, financial decision-making is not merely a
technical or administrative function, but a reflection of deeper organizational structures,
behaviors, and societal interactions. The journal underscores the need to explore how
financial practices influence and are influenced by the lived experiences of individuals
within organizations. This encourages studies that move beyond abstract theorizing,
focusing instead on the transformative application of theoretical insights into real-world
organizational practices. Thus, integrating financial analysis with organizational theory
© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit h t t p : / / c e r a t i v e c o m m o n .s o r g / l i c e n s
e s / b y - n c - n d / 4 . 0. /

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 2 of 22
contributes not only to scholarly understanding, but also to the practical improvement
of life within and across institutions.
Finance refers to the systematic management, investment, and allocation of money
to preserve its value, build it over time, or simply for efficient utilization. It is a critical
tool in the decision-making process of an individual, an organization, or a government.
Finance has generally been divided into three major fields: public finance, corporate
finance, and personal finance [24]. Public finance deals with a nation’s revenues and
expenditures including tax policies, budgeting, public debt, and economic stabilizing
efforts. The idea of corporate finance reveals how a corporation may manage its financial
actions with regard to the acquisition of assets, liabilities, investments, and the raising of
capital through debt to ensure profitability and sustainability. Personal finance refers to
money management by an individual or family, including budgeting and saving, invest-
ing, insurance planning, mortgage management, and retirement planning [4, 25].
At its core, the concept of financial literacy focuses on how to manage money wisely,
which can be encapsulated by two key principles saving and investing. An essential rule
is “pay yourself first,” which acknowledges putting your financial well-being left first sav-
ing and investing prior to spending on any frivolities. An extension of this line of thought
is investment in oneself through education or furthering skill development, which is
arguably a key step toward long-term financial independence [8]. Equally important is
being wary of bad debt-typically, a concept borrowed for non-productive purposes that
offers no possibility of return, such as impulsive purchasing of luxury items. Conversely,
a debit for education or even starting a business may pay off in the near or distant future.
An emergency fund is another must-have item to stay cushioned by the financial shocks
arising from unexpected events. Thus, getting our personal finance in shape through
wise decisions brings about security, less stress, and a peaceful and stable life [14].
The graph “Financial Security and Stress Indicators (2025),” as shown in Fig. 1, pro-
vides a comparative overview of the key financial well-being indicators. It divides the
world from U.S. survey data. The emphasis is on at mere 29% of the global population
that feels optimistic about its financial future, indicating a sharp decline in the pub-
lic’s confidence in recent times due to inflation, rising costs of living, and economic
Fig. 1 Financial security and stress indicators [9]

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 3 of 22
instability. In the United States, 44% of the population reports that they feel financially
secure from the increase from the previous year, yet the majority of the people seem
to be fighting some level of financial strain. The age bracket between 30 and 44 years
has been cited as particularly at risk, with 77% of adults feeling financially insecure. This
group generally encounters major expenses, such as student loans, mortgage payments,
and child expenses, thus placing them under enormous economic pressure. There are
64% of Americans feel financially insecure; this, implies systemic challenges faced in
achieving economic stability, even in a high-income economy. In addition, 54% of adults
in the U.S. claimed to feel stressed because of indebtedness, which significantly affects
mental health and overall well-being [9].
This visualization again speaks of continuous financial insecurity and calls for urgent
interventions such as debt management, financial literacy, and policy reforms that will
build long-term economic resilience, particularly for the working population.
The conventional approach to measuring financial well-being involves manual analysis
of records of income and expenditure, credit scores, budget worksheets, or self-reported
surveys. Financial institutions and policymakers rely on static indicators to measure
individuals’ and households’ financial health. Such static markers may include debt-to-
income ratios, savings rates, or credit utilization. These indicators can provide a gen-
eral measure, but often fail to represent true financial behavior, which is both dynamic
and nonlinear [12]. On the contrary, they are reactive, mostly descriptive rather than
predictive, lack personal customization, and do not accommodate the real-time variabil-
ity exhibited in financial patterns. Their set limitations include an inability to scale effi-
ciently, a high degree of susceptibility to reporting errors, dependence on lengthy data
collection procedures, and an inability to detect intricate behavioral patterns, such as
impulsive spending or irregular income streams—behaviors fairly common among gig
workers [20].
Artificial Intelligence (AI) and Hybrid Deep Learning models overcome the limitations
that hinder real-time data-driven financial well-being assessments. These models han-
dle massive amounts of structured and unstructured financial data, such as transaction
logs, digital receipts, behavioral trends, and lifestyle patterns. Hybrid models combine
CNNs Convolutional Neural Networks (CNN) for feature extraction with RNNs Recur-
rent Neural Networks (RNN) for sequence modeling to capture complex temporal pat-
terns in income and expenditure over time. These can identify early warning signs of
an impending financial freeze, predict the future financial state, and offer customized
financial relief. Furthermore, AI systems adapt and learn with the arrival of each set of
new data, thereby increasing their accuracy and relevance. With this, they provide far
broader, predictive, and scalable approaches to assessing financial well-being compared
to conventional approaches [5, 15, 17].
1.1 Contribution
The following points summarize the primary contributions of this study, focusing on the
core innovations and technical achievements that define its impact and significance.
1. A comprehensive dataset of 20,000 Indian individuals was developed, incorporating
detailed financial information, such as potential savings in nine specific categories,
desired savings percentage, debt ratio, occupation, and city tier.

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 4 of 22
2. Engineered new features such as the Savings Ratio (Desired Savings ÷ Income) and
Debt Ratio (Loan Repayment ÷ Income), were shown to significantly influence model
predictions, accounting for up to 50% of decision-making in the TabNet model. These
types of features are rarely used in the existing financial profiling studies. Designed
a unique hybrid machine learning model combining Wide & Deep learning with
Convolutional Neural Networks (CNNs), even though the data were non-sequential.
This approach treats financial records as sequences by reshaping the data, thereby
allowing CNNs to learn complex patterns.
3. Two types of correlation heatmaps were used one for the original data and the
anotherfor savings-related features to uncover hidden financial behaviors. For
example, astrong correlation (r = 0.89) was found between grocery expenses and
grocery savingspotential, guiding both the feature selection and model interpretation.
4. TabNet was applied to understand which features the model relied on the most.
Surprisingly, traditional metrics such as income and age were less important
thanbehavioral indicators such as debt ratio and miscellaneous savings potential.
Thisinsight challenges existing financial modeling practices and emphasizes the value
ofbehavior-based features.
2 Related work
In recent years, a growing body of interdisciplinary research has sought to unravel the
multifaceted dimensions of financial well-being and systemic stability, using advanced
computational methods, machine learning, and behavioral modeling. The collective
objective is to understand financial stress better, predict financial risks, and build resil-
ient systems that bridge the gap between individual experiences and broader economic
phenomena.
Ghashti et al. [11] conducted a foundational study in this direction with the inten-
tion of identifying the major sources of financial stress by analyzing the responses of
1,874 individuals to a set of 68 mixed-type survey questions collected in 2022. Dis-
tance-based clustering an effective tool in the toolkit of any financial segmented, was
employed with a mixed-type distance incorporating variable-specific kernel functions
with cross-validated bandwidths in order to discriminate between relevant and irrele-
vant variables effectively. The analysis yielded two major clusters: steady savers, indicat-
ing strong financial well-being and financial strivers, comprising individuals undergoing
high financial stress. The segmentation yielded actionable insights into personal finan-
cial advices and paved the way for automated financial advising and investment genera-
tion. While individual stress is critical, Polyzos et al. [22] expanded the lens to systemic
shocks, such as banking crises, affecting subjective well-being. By setting an agent-based
modeling framework alongside a support vector machine (SVM) subjective well-being
function, researchers simulated the direct and indirect effects of economic downturns,
such as income loss, unemployment, and psychological distress. However, the associ-
ated research findings, show that welfare losses from bank failures often exceed the fiscal
cost of government bailouts. They further underscored the asymmetry in losses among
various segments of the population, thus revealing the social complexity underlying
economic policymaking. Gensler & Bailey [10] focused on the emerging systemic risks
brought about by the widespread adoption of deep learning-based systems in financial
ecosystems, mapping this impact across five transmission pathways. A paradox was

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 5 of 22
brought out: while these models provide stellar levels of prediction and efficient per-
formance, they simultaneously increase interconnectedness within the systems and may
even lend new forms of fragility to these systems. The study concluded that traditional
regulatory frameworks are insufficient for the evolving challenges, and it proposed that
policy tools should be reconsidered to protect the stability of the financial system in the
AI age. To complement this, Alessi and Savona [2] addressed the technical limitations
of conventional financial risk models. They state that traditional empirical methods
are incapable of representing the complex, nonlinear, and multidimensional nature of
financial data. The imbalanced and high-dimensional nature of datasets makes them an
ideal domain for machine learning, which provides a more robust solution. However,
despite being extraordinarily good in terms of predictive accuracy, such models, which
are largely taken to be black boxes, ironically remain the least used in the assessments of
mainstream financial stability, primarily due to their perceived lack of interpretability,
thus signaling the gap between innovation and regulatory acceptance. To address these
issues, Khunger [16] proposed a deep learning-based framework for financial stress
testing Their architecture, Correlation CNN-LSTM, combines both quantitative and
qualitative indicators. The model was highly accurate with an almost negligible train-
ing loss (0.0013) and testing loss (0.003). It predicts core financial variables fairly well.
The model was able to decrease major financial risk types, such as credit, liquidity, mar-
ket, and operational risks, to a great extent, thereby furthering the usefulness of financial
risk measurements and systemic resilience. Building on this, Shi et al. [23] developed
the Hybrid Financial Risk Predictor (HFRP), which is a model similar to the CNN and
LSTM architectures but is especially useful in combining numerical data with financial
text analytics. Similar to the earlier setup, it achieved very high accuracy and stability
with training and testing losses again posted at 0.0013 and 0.003, respectively. It pro-
vided accurate forecasts for important variables, such as revenue, net income, and EPS,
while also mitigating different categories of risks. The hybrid nature of the model shows
how combining data modalities can enrich the provisions of risk information, that can
be used to make dependable financial decisions. Further refinement of model selection
led to the development by Elhoseny et al. [7] of a novel Adaptive Whale Optimization
Algorithm with Deep Learning (AWOA-DL) for the prediction of financial distress. The
three-step pipeline, namely data preprocessing, hyperparameter optimization based on
AWOA, and prediction using a multilayer perceptron-based deep neural network, was
validated on four datasets. With an average accuracy of 95.8%, the models were found
to be superior to the classical methods, with corresponding benchmark accuracies
of 93.8%, 89.6%, 84.5%, and 78.2%. This study went a long way in supports the notion
that evolutionary optimization techniques can significantly improve the accuracy and
robustness of deep learning models in finance. In continuation with predictive model-
ing for distress scenarios, Naved et al. [21] dealt with bankruptcy prediction aided by
machine learning and metaheuristic optimization. This research applied the Histogram
Gradient Boosting Classification (HGBC) model and hybridized it with three optimi-
zation algorithms: Snake Optimization Algorithm (SOA), Gradient-Based Optimization
(GBO), and Bonobo Optimization Algorithm (BOA), resulting in the three hybridized
models HGSO, HGGB, and HGBO, respectively. With pure HGBC, precision was 0.940,
while HGBO and HGGB increased it to 0.950 and 0.960, respectively. However, the
HGSO model stands out with the highest precision level of 0.980, establishing it as an

Uppal et al. Discover Artificial Intelligence           (2026) 6:248  Page 6 of 22

Fig. 2 Proposed system to detect and classify the financial status
Table 1 Categorization and description of features used for financial well-being analysis
| Category                  | Feature           | Description                                   |
| ------------------------- | ----------------- | --------------------------------------------- |
| Income & demographics     | Income            | Monthly income of the individual              |
|                           | Age               | Age in years                                  |
|                           | Occupation        | Type of employment or job role                |
| Monthly expenses          | Rent              | Monthly rent payments                         |
|                           | Loan_Repayment    | Monthly loan repayment obligations            |
|                           | Insurance         | Insurance premiums paid monthly               |
| Financial goals & savings | Desired_Savings   | Targeted monthly savings amount               |
|                           | Disposable_Income | Remaining income after deducting all expenses |
elite early bankruptcy detector and holds great promise for the preemptive mitigation
of financial risk. Finally, Akash et al. [1] study the relationship between systemic risk
and financial indicators through a regression study of Yahoo stock market data. With
liquidity, solvency, profitability, and risk exposure, a strong positive correlation is found,
mainly between liquidity and profitability, indicating that firms with a high liquidity level
tend to perform well financially. The regression also shows that as much as 94% of the
variance in profitability can be predicted from these indicators, and price-earnings (PE)
ratios are affected mostly by stock price trends. They further emphasized that compre-
hensive financial analysis ensures risk management for long-term financial stability.
3  Proposed pipeline to analyse the financial status
The pipeline proposed in this section helps understand and classify people based on
their financial behavior. As shown in Fig. 2, different deep learning models are applied
to the data to learn higher-level abstractions. To further increase performance, hybrid
models are established by two or several existing neural architectures and finally the sys-
tem assigns individuals to the three major financial states of Financially At-Risk, Finan-
cially Stable, and Financially Secure.
3.1 Financial dataset description
The data contains detailed information on the financial and demographic aspects of
20,000 individuals from India. It includes details on monthly income, expenditure pat-
terns, goals for savings, and potentials savings in categories such as groceries, transport,
and healthcare as shown in Table 1. This rich dataset is well suited for personal finance

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 7 of 22
behaviors, cost-optimization opportunities, and predictive model developments in
financial planning. As a wider snapshot of expenditures and their present saving capac-
ity, the dataset may act as an important resource for researchers, data scientists, and
financial analysts interested in the Indian financial industry [13].
Additional supporting features include Dependents, which signify the number of peo-
ple financially supported by the person, and City_Tier, which corresponds to regional
economic disparities by assigning cities into tiers. Expenses from the dataset were finely
detailed and split by month for various categories, including Groceries, Transport, Eat-
ing_Out, Entertainment, Utilities, Healthcare, Education, and Miscellaneous. These
are crucial for estimating Potential Savings, which is an assessment of opportunities to
reduce spending and thereby improve financial outcomes. Furthermore, Desired_Sav-
ings_Percentage functions as a subjective metric for financial goal setting, thereby assist-
ing in measuring the gap between the desired and actual saving behavior. Together, these
variables support the study of financial wellness and spending patterns fairly thoroughly.
3.2 Data preprocessing and visualization of financial data
Several preprocessing steps are required to effectively prepare dataset for machine-
learning models. First, categorical features such as “Occupation” and “City_Tier” are
Label Encoded so as to convert categories represented by textual characters into numer-
ical values without losing relational semantics, thus allowing the algorithms to process
them. Subsequently, feature engineering is applied to create new meaningful variables,
such as the Savings Ratio (Desired_Savings divided by Income) and Debt Ratio (Loan
Repayment divided by Income). These ratios provide normalized insight into personal
saving behavior and financial liability, so that the model reviews personal financial
health across various income levels. Finally, standardization was applied to all numerical
features to rescale the data to have a mean of 0 and a standard deviation of 1. In this way,
larger measurements do not dominate smaller ones and help in faster convergence and
more stable learning using gradient-based algorithms. These steps boost the goodness of
prediction for the dataset thus, models can learn more efficiently and accurately.
As presented in Fig. 3, the graph titled Income Distribution with Mean and Median
provides a visual perception of how the incomes of individuals are distributed within
this particular dataset. The distribution is highly right-skewed; this means that, while
most individuals earn lower and moderate incomes, a small number of people earn very
high incomes, pulling the tail of the distribution to the right. This is further validated
by the fact that the mean income (41,585) is above the median (30,185), which is a well-
known feature of skewed data. The importance of this graph lies in its implications for
the statistical analysis and model building. In a skewed dataset, such as this, the median
often acts as a better measure of central tendency than the mean and is especially used
for describing the income of a typical individual. In addition, this skewness advocates
employing normalization techniques (for example, log transformation) to income values
before feeding such features to machine-learning algorithms to reduce bias and improve
convergence. The application of this skew can result in different feature engineering
strategies, such as Income brackets or percentiles, for example, allowing models to bet-
ter distinguish between low-, middle-, and high-income groups. Ultimately, the graph
conveys that income data needs to be treated with care to avoid distortions in income-
based predictions and ensure that models learn in a fair and balanced manner.

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 8 of 22
Fig. 3 Income distribution with mean & median
Fig. 4 Correlation heatmap of numerical features
The correlation heatmap in Fig. 4 provides a detailed view of the interrelationships
among all the numerical features in the personal finance dataset. One of the key obser-
vations is the positive correlation of Income with the following expense categories: gro-
ceries (0.99), insurance (0.94), education (0.79), and healthcare (0.94). This means that
income goes up, and so does expenditure of the individuals across these categories-a
proportional spending style. There are high positive correlations between Potential Sav-
ings and Income across all categories (groceries, utilities, education, etc.), as well as the
actual expenditures for these categories (≥ 0.75). For example, Potential_Savings_Gro-
ceries correlates at 0.89, and Potential_Savings_Utilities at 0.82, with actual spending,
meaning that potential savings are calculated as fraction of current spending, which is
correlated with income. Similarly, Disposable_Income positively correlates with desire

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 9 of 22
savings (0.86) and income (0.88), which is logical: those with higher residual income
after expenses tend to aim for higher savings. Desired_Savings_Percentage, however,
moderately correlates with Income (0.35), and hence, saving intent (as a proportion of
income) varies independently of actual income levels and probably reflects behavior or
attitudes. The heatmap also reveals clusters that comprise highly correlated features,
such as expenses (Groceries, Transport, Healthcare, etc.) and Potential Savings variables.
Such clusters could imply multicollinearity, which is important to consider when making
decisions about feature selection or dimensionality reduction in predictive modeling.
The potential Savings correlation heatmap in Fig. 5 shows moderate to strong positive
correlations across categories, mostly ranging from 0.60 to 0.70. For example, Potential_
Savings_Groceries has a correlation of 0.70 with Transport, 0.68 with Eating_Out, and
0.69 with Miscellaneous. This implies that people who can save in one category tend to
show a similar potential to others. This observation hints at higher-level financial behav-
ior groups: people who manage spending of discretionary nature well in one category
typically display capacity in others as well. Interestingly, Potential_Savings_Education
shows the overall lowest correlation compared to other categories, such as Eating_Out
(0.49) and Healthcare (0.50), which may reflect that it is more of the planned or non-
discretionary type of expense that varies much on the basis of life stage or structure of
the household. The declining correlation of educational savings potential with other cat-
egories constitutes an argument that educational expenses are less substitutable and less
behavior-driven, as opposed to lifestyle-related expenses. The utility of this heatmap lies
in its importance for dimensionality reduction and feature selection for predictive mod-
eling, with the majority of features being highly correlated and probably suffering from
multicollinearity. Hence, could be resolved by PCA or regularization to avoid overfit-
ting of the model. Clustering of these variables can be used in the definition of compos-
ite indices of financial behavior or in the segmentation of user profiles, both of which
are extremely useful in applications such as personalized financial planning or targeted
intervention strategies.
Fig. 5 Correlation heatmap of potential saving features

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 10 of 22
A bar chart titled “Average Monthly Expenses by Occupation” in Fig. 6 compares
average monthly spending for Groceries, Transport, and Healthcare for a range of
occupational groups: Professional, Retired, Self-Employed, and Student. The trend in
the data remains consistent throughout the chart; groceries have the highest average
monthly expenses for all occupational categories, more than ₹5,000. This suggests that
food-related expenses mostly take precedence as a financial consideration, regardless
of employment situation. Once again, transportation comes next, and then healthcare
maintains a relatively constant level for all groups at ₹1,600–₹1,700. This presentational
view shows that there seems to be little variation among the different occupational
groups in the expenditures for these essentials, which might insinuate that lifestyle
expenses are more or less the same due to possibly unified pricing or almost equivalent
access levels.
The significance of the graph lies in its implications for personalized financial planning
and targeted savings interventions. Social spending patterns, depending upon occupa-
tion, may, therefore, also be largely similar, since similar social spending baskets, policy-
makers, app developers, or financial institutions could target generic budgeting or saving
advice that applies to almost all end-buyer segments. The graph also serves as a starting
point for the analysis of spending efficiency or potential savings with reference to occu-
pational profiles.
3.3 Feature scaling
To scale the important features, the TabNet Feature Importance illustrated in Fig. 7 indi-
cates the relative contribution of each feature toward the model’s prediction of financial
categorization or stability [18]. Debt_Ratio was the predominant feature, accounting for
almost 50% of the decision weight of the model. The dominant position of Debt_Ratio
clearly shows that the amount of income paid for loans is perhaps the most important
indicator of financial well-being or risk. Potential_Savings_Miscellaneous and Savings
Ratio are key features, indicating that miscellaneous cash spending and the propor-
tion of income saved are strong predictors of financial wellbeing. Other features such
as Desired_Savings_Percentage, Insurance, Occupation, and Potential_Savings_Utili-
ties exhibit moderate importance, indicating that while they impact the outcome, this
influence can be situational and somewhat indirect. Surprisingly, basic variables such as
Fig. 6 Average monthly expenses by occupation

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 11 of 22
Fig. 7 Feature importance using TabNet
Income, Disposable_Income, and Age show minimal importance, which could arise with
some of their information being indirectly captured or normalized through constructed
ratios, such as the Debt Ratio or Savings Ratio. Similarly, the standalone categories of
Groceries, Transport, and Healthcare show low predictive power, reinforcing that the
model finds more value in composite financial behavior (in terms of ratios and potential
savings) than in raw monetary values.
The importance of this section lies in guiding the selection of features, intervention
strategies, and model interpretability. For instance, financial advisory systems may focus
on monitoring and reducing users’ debt ratios and increasing savings in discretionary
areas at the model level rather than simply increasing users’ income. It also validates
feature engineering (e.g., ratio-based variables) that help with the model as well as real-
world insight.
3.4 Classifiers for analysing the pattern of finance
To model and classify patterns from the Indian Personal Finance and Spending Habits
dataset, we adopted a sequence of advanced deep-learning architectures, each tailored
to the unique characteristics of the data. The dataset, consisting of both categorical and
numerical features such as income, investment preference, credit card usage, and spend-
ing tendencies, was first preprocessed and transformed into a normalized numerical
form X = { x 1 ,x 2 ,... ,x n } , where each x i ∈ Rd represents a d-dimensional feature
vector for the i-th individual. We began by applying Deep Neural Networks (DNNs)
and Fully Connected Neural Networks (FCNNs), which utilized multiple hidden lay-
ers with ReLU activation f(x)=max(0,x) to learn complex, nonlinear feature inter-
actions [20]. To capture localized feature dependencies, we reshaped the tabular input
into pseudo-sequences and applied Convolutional Neural Networks (CNNs), where
the convolution operation was defined as h i =σ k j=1 w j · x i+j − 1 +b , allow-
ing the model to learn spatial hierarchies among gro(u∑ped financial indicator)s. Given
the potential temporal influence on decision-making (e.g., prior savings affecting cur-
rent investments), we integrated Recurrent Neural Networks (RNNs) and advanced
them using Gated Recurrent Units (GRUs) and Bidirectional Long Short-Term Mem-
ory networks (BiLSTMs), where the cell state updates are governed by gates such as
f t =σ (W f · [h t − 1 ,x t ]+b f ), enabling effective modeling of sequential financial

Uppal et al. Discover Artificial Intelligence           (2026) 6:248  Page 12 of 22

Algorithm 1 Feature importance using TabNet
behaviors. Recognizing that some survey responses might exhibit long-range depen-
dencies, BiLSTM offers a bidirectional context across time [3]. To simultaneously
benefit from memorization and generalization, we implemented at the Wide & Deep
| model, where the prediction was computed as y |     |     | =σ W | T x+W T | φ (x) |
| --------------------------------------------- | --- | --- | ---- | ------- | ----- |
, where
|                                    |     |                    |                         | w ide d eep |         |
| ---------------------------------- | --- | ------------------ | ----------------------- | ----------- | ------- |
| x represents the raw features and  |     | φ (x) is the trans | (                       |             | )       |
|                                    |     |                    | formation learned by th |             | e DNN.  |
We extended this paradigm by combining the wide component with sequential layers
such as BiLSTM, CNN, GRU, and Attention, forming Wide & Deep + BiLSTM, Wide
& Deep + CNN, and Wide & Deep + Attention models, each designed to simultane-
ously learn low-level interactions and temporal abstractions [22]. Furthermore, we
incorporated autoencoders to compress the high-dimensional feature space into a latent
| z               | =f (x), followed by decoding  |     | x=f | (z), using the reconstruc- |     |
| --------------- | ----------------------------- | --- | --- | -------------------------- | --- |
| representation  | enc                           |     |     | dec                        |     |
2
tion loss L = x x  to guide representation learning. These encodings are then
rec ∥ − ∥
| fed into classifiers or RNNs for downstream classification. Hybrid architectures, such  |     |     | (cid:31) |     |     |
| --------------------------------------------------------------------------------------- | --- | --- | -------- | --- | --- |
(cid:31)

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 13 of 22
Algorithm 2 Wide & deep + BiLSTM for financial behavior classification
as CNN + LSTM and CNN + MLP, were used to first extract patterns using convolu-
tional layers and subsequently model sequential or dense interactions through LSTM or
MLP units. To enhance attention toward critical features (e.g., those influencing debt
or savings behavior), we employed Attention-based CNNs and Wide & Deep + Atten-
tion mechanisms, where the attention score was computed as α i = exp(ei) with
jexp(ej)
e i =vTtanh(Wx i +b), dynamically weighting the key features in th ∑ e decision pro-
cess. Collectively, this ensemble of models enables comprehensive representation learn-
ing from heterogeneous personal finance attributes, capturing both static and dynamic
behavioral patterns to yield robust classification outcomes [19].
A hybrid architecture combining a Wide & Deep learning framework with a Con-
volutional Neural Network (CNN) is shown in Algorithm 1 for classifying individuals
based on their financial behavior. In this manner, a model can capture the interactions
of low-order features in parallel with computations to extracting patterns of higher
order through one-dimensional convolutions applied to appropriately reshaped

Uppal et al. Discover Artificial Intelligence           (2026) 6:248  Page 14 of 22
financial-feature vectors. Because the data are structured in tabular format, wherein the
absence of temporal ordering is associated with embedded local correlations, this archi-
tecture is ideal for such cases. This algorithm provides the details for pre-processing,
architectural flow, and optimization to be used for training the Wide & Deep + CNN
model on multi-financial-classification tasks [26].
Algorithm 2 provides an outline of building and training the hybrid Wide & Deep
model using the BiLSTM network for financial behavior classification. This model uses
the generalization and memorization of the third layer. Hence, the wide layer is con-
sidered for memorization and pooling the specification of feature interactions, and the
deep BiLSTM layer is considered for generalization by militating sequential or pseudo-
sequential patterns inherent in behavioral financial data. The algorithm starts with
structured preprocessing, with the distortion of wide and deep components in parallel,
which are later joined and optimized using a supervised learning procedure with Adam
optimizer [6].
4  Result and analysis
This section presents the empirical outcomes obtained by applying various deep learn-
ing classifiers to the Indian personal finance and spending habit dataset.
In Table 2, the training and validation performance metrics reveal several key insights
into model behavior on the Indian personal finance dataset. First, models such as Wide
& Deep + CNN, Wide & Deep + BiLSTM, and BiLSTM not only achieved the highest
validation accuracies (≥ 0.988), but also maintained very low validation losses (~ 0.025–
0.026), indicating their strong generalization ability. This suggests that models capable of
both memorization (via wide components) and sequence modeling (via BiLSTM/CNN)
are particularly effective at capturing the complex interdependencies among features,
such as income, expense categories, city tier, and savings behavior. The minimal gap
between the training and validation metrics in these models indicated stable learning
and a low risk of overfitting.
Table 2 Performance comparison of deep learning models on financial data
| Model                    | Train accuracy | Train loss   | Val accuracy | Val loss      |
| ------------------------ | -------------- | ------------ | ------------ | ------------- |
| CNN                      | 0.8788         | 0.3006       | 0.8687       | 0.3182        |
| RNN                      | 0.9773         | 0.0525       | 0.9791       | 0.0440        |
| DNN                      | 0.9845         | 0.0379       | 0.9766       | 0.0511        |
| BiLSTM                   | 0.9851         | 0.0324       | 0.9884       | 0.0256        |
| GRU                      | 0.9905         | 0.0219       | 0.9859       | 0.0255        |
| Wide & Deep              | 0.9916         | 0.0283       | 0.9831       | 0.0456        |
| Autoencoder + Classifier | 0.9827         | 0.0457       | 0.9803       | 0.0438        |
| FCNN                     | 0.9743         | 0.0602       | 0.9762       | 0.0683        |
| Attention-CNN            | 0.8835         | 0.2798       | 0.8697       | 0.2901        |
| Residual MLP             | 0.9798         | 0.0480       | 0.9578       | 0.1066        |
| Hybrid CNN + MLP         | 0.7165         | − 94653360.0 | 0.7025       | − 103436192.0 |
| Hybrid CNN + LSTM        | 0.8717         | 0.3232       | 0.8544       | 0.3617        |
| Hybrid CNN + GRU         | 0.8783         | 0.2975       | 0.8622       | 0.3315        |
| Hybrid RNN + BiLSTM      | 0.9834         | 0.0403       | 0.9781       | 0.0464        |
| Autoencoder + RNN        | 0.9643         | 0.0856       | 0.9584       | 0.0941        |
| Wide & Deep + BiLSTM     | 0.9880         | 0.0305       | 0.9900       | 0.0261        |
| Wide & Deep + CNN        | 0.9937         | 0.0268       | 0.9944       | 0.0259        |
| Wide & Deep + RNN        | 0.9772         | 0.0571       | 0.9844       | 0.0441        |
| Wide & Deep + Attention  | 0.9879         | 0.0354       | 0.9897       | 0.0368        |

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 15 of 22
By contrast, models such as CNN, Hybrid CNN + GRU, and Attention-CNN show
larger validation losses (~ 0.29–0.33) and slightly lower accuracies (~ 0.86), reflect-
ing their inability to fully capture high-dimensional financial patterns. This limitation
likely stems from their reliance on local feature extraction without recurrent memory or
dynamic feature weighting, which are essential given the dataset’s multi-feature correla-
tions (e.g., income vs. groceries and, income vs. savings).
Moreover, the Hybrid CNN + MLP model is severely unstable, showing negative loss
values in the order of millions, indicating a critical training failure, possibly due to
incompatible layer integration or numerical overflow. Interestingly, even simpler models,
such as RNN, FCNN, and Autoencoder + Classifier, maintain robust validation accuracy
(> 0.95) and low loss, highlighting that even without sophisticated hybridization, models
that can extract latent feature relationships perform well because of the structured and
patterned nature of the dataset.
In summary, the performance table clearly supports the conclusion that models with
architectural components for hierarchical abstraction (deep layers), temporal/sequential
modeling (RNN, BiLSTM), and feature attention or selection (Wide & Deep, TabNet)
are the most suitable for this type of financial behavior data.
Additionally, the learning curves and confusion matrix of the best-performing mod-
els are also presented in Fig. 8, where both hybrid models show a good fit of models in
training and validation.
The overall performance of the models on the Indian Personal Finance and Spending
Habits dataset reflects the nature of the data, which are highly structured, multivariate,
and deeply interdependent, as shown in Table 3. Models such as BiLSTM, GRU, and
hybrid architectures such as Wide & Deep + CNN, Wide & Deep + BiLSTM, and TabNet
achieve perfect or near-perfect scores (F1 ≈ 0.99–1.00), showcasing their ability to model
complex feature interactions, temporal dependencies, and hierarchical relationships.
These models excel because the dataset contains patterns such as strong positive corre-
lations between income and multiple expense categories (e.g., rent, groceries, transport)
and between income and savings, which are best captured by architectures capable of
nonlinear representation learning and memory mechanisms. For instance, the BiLSTM
and GRU models retain long-range dependencies and are robust to feature skewness and
class imbalance, explaining their 1.00 precision, recall, and F1 scores.
Deep neural models such as DNN, FCNN, and Residual MLP also perform competi-
tively (F1 ≈ 0.94–0.97) owing to their capacity to learn hierarchical abstractions from
numeric input features. By compressing high-dimensional data into efficient latent rep-
resentations, autoencoder-based models also preserve essential variance while reduc-
ing redundancy, resulting in F1 scores of up to 0.98. The Wide & Deep model and its
enhanced hybrids benefit from combining memorization (wide component) with gen-
eralization (deep component), particularly in a domain such as personal finance where
both rare and frequent patterns coexist.
On the other hand, CNN-based architectures, including Hybrid CNN + GRU/LSTM
and Attention-CNN, show lower performance (F1 ≈ 0.84–0.86), and in the case of
Hybrid CNN + MLP, they drastically underperform (F1 ≈ 0.28). This underperformance
likely stems from CNNs’ limited capacity of CNNs to model long-range dependencies
in non-spatial tabular data, making them less suited for financial datasets that require
an understanding of contextual interactions across features. Moreover, models such as

Uppal et al. Discover Artificial Intelligence           (2026) 6:248  Page 16 of 22

Fig. 8 Analysis of the best performing models
Table 3 Examination of the trained classifiers for analysing financial dataset
Model Precision Recall F1-Score Model Precision Recall F1-Score
| CNN         | 0.90 0.84 | 0.86 FCNN              | 0.97 0.97 | 0.97 |
| ----------- | --------- | ---------------------- | --------- | ---- |
| RNN         | 0.98 0.99 | 0.99 Attention-CNN     | 0.92 0.84 | 0.86 |
| DNN         | 0.98 0.97 | 0.97 Residual MLP      | 0.97 0.92 | 0.94 |
| BiLSTM      | 1.00 1.00 | 1.00 TabNet            | 0.99 0.99 | 0.99 |
| GRU         | 1.00 1.00 | 1.00 Hybrid CNN + MLP  | 0.23 0.33 | 0.28 |
| Wide & Deep | 0.99 0.98 | 0.98 Hybrid CNN + LSTM | 0.92 0.81 | 0.84 |
Autoencoder + Classifier 0.97 0.98 0.98 Hybrid CNN + GRU 0.90 0.82 0.85
Hybrid RNN + BiLSTM 0.98 0.98 0.98 Wide & Deep + CNN 1.00 1.00 1.00
Autoencoder + RNN 0.94 0.96 0.95 Wide & Deep + RNN 0.99 0.99 0.99
Wide & Deep + BiLSTM 0.99 0.99 0.99 Wide & Deep + Attention 0.99 0.99 0.99
Attention-CNN and Hybrid CNN + LSTM may suffer from overfitting or ineffective
attention calibration, particularly when feature importance is unevenly distributed.
Likewise, Table 4 contains precision, recall, and F1-score data for the applied deep
learning architectures evaluated in the financial health categories of Financially At-Risk,
Financially Secure, and Moderately Stable.

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 17 of 22
The outstanding performance of advanced sequence-based models such as BiLSTM,
GRU, and various hybrid architectures (e.g., Wide & Deep + CNN, Wide & Deep + BiL-
STM) on this dataset likely stems from the rich multivariate structure and strong inter-
feature correlations of the dataset. Seq-models, such as RNNs, LSTMs, and GRUs, are
adept at capturing complex, context-dependent patterns with sequential or time-related
features, allowing them to tease apart subtle distinctions among classes. Indeed, RNN
achieved nearly perfect metrics across categories, whereas BiLSTM and GRU reached
near-ideal precision, recall, and F1 across all classes. These models can effectively model
interactions (e.g., how income interacts with multiple expense categories and demo-
graphics) and are robust to the noise and outliers common in skewed financial data. In
contrast, simpler CNNs and hybrid shallow-deep models may struggle to fully represent
these multifaceted relationships. For example, CNNs showed drops in F1 for “Moder-
ately Stable” (~ 0.67), likely because convolutional filters alone do not adequately model
feature interactions over all input vectors. Similarly, models such as Attention-CNN or
Hybrid CNN+LSTM/GRU improved stability moderately but still lagged behind full
RNN architectures. Autoencoders with classifiers also scored well (~ 0.97 F1) because
they adaptively compressed the high-dimensional skewed input features before classifi-
cation, effectively performing manifold learning that benefits downstream classification.
TabNet, with its sequential attention mechanism over tabular data, performed extremely
well (F1 ~ 0.99) by dynamically selecting and weighting the relevant feature subsets.
Similarly, Fig. 9 illustrates the ROC-AUC scores of various deep learning and hybrid
models developed for financial health prediction. ROC-AUC (Receiver Operating Char-
acteristic - Area Under the Curve) is a critical metric that evaluates a model’s ability to
distinguish between different classes and in this case, individuals categorized as Finan-
cially Secure, Moderately Stable, or Financially At-Risk. Models such as BiLSTM, GRU,
and the Wide & Deep + CNN hybrid achieved a perfect ROC-AUC score of 1.0000, indi-
cating flawless discrimination across financial well-being categories. This underscores
their exceptional reliability in real-world deployment in personal finance advisory sys-
tems. Other top-performing models include TabNet, RNN, Wide & Deep + BiLSTM,
Autoencoder + Classifier, and Wide & Deep + RNN, all exceeding a score of 0.999,
reflecting near-perfect classification ability. Traditional architectures such as CNN and
hybrids such as CNN + LSTM and CNN + GRU showed relatively lower but still com-
mendable ROC-AUC values, ranging from 0.9286 to 0.9428. This finding suggests room
for improvement, particularly in handling the nonlinearity and complexity of financial
behavior patterns. The graph highlights a clear trend: hybrid models leveraging archi-
tectural synergies such as Wide & Deep sequence models) outperform standalone mod-
els. This aligns with contemporary machine learning theory, which posits that hybrid
architectures can capture both static and sequential patterns in complex datasets crucial
for financial well-being assessments that depend on both categorical traits and spending
behaviors. Overall, the graph provides compelling evidence for the superiority of hybrid
deep learning architectures in achieving robust financial classification and actionable
insights for researchers and practitioners aiming to build scalable and interpretable
financial decision support systems.
Furthermore, Table 5 compares existing work on segmentation, systemic risks, and
stress testing with the proposed framework that uses large-scale real-world data and
hybrid, highly synergistic deep learning models to segregate individual clients as either

Uppal et al. Discover Artificial Intelligence           (2026) 6:248  Page 18 of 22
Table 4 Class-wise performance metrics of deep learning models for financial health classification
| Model                    | Class               | Precision | Recall | F1-Score |
| ------------------------ | ------------------- | --------- | ------ | -------- |
| CNN                      | Financially At-Risk | 0.99      | 1.00   | 0.99     |
|                          | Financially Secure  | 0.88      | 0.97   | 0.92     |
|                          | Moderately Stable   | 0.85      | 0.56   | 0.67     |
| RNN                      | Financially At-Risk | 0.98      | 1.00   | 0.99     |
|                          | Financially Secure  | 1.00      | 0.99   | 1.00     |
|                          | Moderately Stable   | 0.98      | 0.98   | 0.98     |
| DNN                      | Financially At-Risk | 0.97      | 0.95   | 0.96     |
|                          | Financially Secure  | 0.99      | 1.00   | 0.99     |
|                          | Moderately Stable   | 0.98      | 0.95   | 0.96     |
| BiLSTM                   | Financially At-Risk | 1.00      | 1.00   | 1.00     |
|                          | Financially Secure  | 1.00      | 1.00   | 1.00     |
|                          | Moderately Stable   | 1.00      | 0.99   | 0.99     |
| GRU                      | Financially At-Risk | 1.00      | 1.00   | 1.00     |
|                          | Financially Secure  | 1.00      | 1.00   | 1.00     |
|                          | Moderately Stable   | 1.00      | 0.99   | 0.99     |
| Wide & Deep              | Financially At-Risk | 0.99      | 0.96   | 0.98     |
|                          | Financially Secure  | 0.99      | 1.00   | 1.00     |
|                          | Moderately Stable   | 0.98      | 0.98   | 0.98     |
| Autoencoder + Classifier | Financially At-Risk | 0.95      | 0.99   | 0.97     |
|                          | Financially Secure  | 1.00      | 0.99   | 0.99     |
|                          | Moderately Stable   | 0.97      | 0.97   | 0.97     |
| FCNN                     | Financially At-Risk | 0.94      | 0.98   | 0.96     |
|                          | Financially Secure  | 0.99      | 0.99   | 0.99     |
|                          | Moderately Stable   | 0.97      | 0.94   | 0.96     |
| Attention-CNN            | Financially At-Risk | 0.97      | 0.99   | 0.98     |
|                          | Financially Secure  | 0.87      | 0.99   | 0.93     |
|                          | Moderately Stable   | 0.92      | 0.53   | 0.67     |
| Residual MLP             | Financially At-Risk | 1.00      | 0.79   | 0.88     |
|                          | Financially Secure  | 0.99      | 0.99   | 0.99     |
|                          | Moderately Stable   | 0.92      | 0.97   | 0.94     |
| TabNet                   | Financially At-Risk | 0.99      | 0.99   | 0.99     |
|                          | Financially Secure  | 1.00      | 1.00   | 1.00     |
|                          | Moderately Stable   | 0.98      | 1.00   | 0.99     |
| Hybrid CNN + LSTM        | Financially At-Risk | 0.98      | 0.97   | 0.98     |
|                          | Financially Secure  | 0.86      | 0.99   | 0.92     |
|                          | Moderately Stable   | 0.94      | 0.46   | 0.62     |
| Hybrid CNN + GRU         | Financially At-Risk | 0.98      | 0.97   | 0.98     |
|                          | Financially Secure  | 0.87      | 0.97   | 0.92     |
|                          | Moderately Stable   | 0.85      | 0.53   | 0.65     |
| Hybrid RNN + BiLSTM      | Financially At-Risk | 0.95      | 0.99   | 0.97     |
|                          | Financially Secure  | 0.99      | 1.00   | 0.99     |
|                          | Moderately Stable   | 0.98      | 0.96   | 0.97     |
| Autoencoder + RNN        | Financially At-Risk | 0.90      | 0.98   | 0.94     |
|                          | Financially Secure  | 0.99      | 0.98   | 0.98     |
|                          | Moderately Stable   | 0.93      | 0.92   | 0.93     |
| Wide & Deep + BiLSTM     | Financially At-Risk | 1.00      | 0.99   | 0.99     |
|                          | Financially Secure  | 1.00      | 0.99   | 1.00     |
|                          | Moderately Stable   | 0.98      | 1.00   | 0.99     |
| Wide & Deep + CNN        | Financially At-Risk | 1.00      | 1.00   | 1.00     |
|                          | Financially Secure  | 1.00      | 1.00   | 1.00     |
|                          | Moderately Stable   | 0.99      | 0.99   | 0.99     |

Uppal et al. Discover Artificial Intelligence           (2026) 6:248  Page 19 of 22
T able 4 (continued)
| Model                   | Class               | Precision | Recall | F1-Score |
| ----------------------- | ------------------- | --------- | ------ | -------- |
| Wide & Deep + RNN       | Financially At-Risk | 0.98      | 1.00   | 0.99     |
|                         | Financially Secure  | 0.99      | 1.00   | 0.99     |
|                         | Moderately Stable   | 1.00      | 0.96   | 0.98     |
| Wide & Deep + Attention | Financially At-Risk | 0.98      | 1.00   | 0.99     |
|                         | Financially Secure  | 1.00      | 1.00   | 1.00     |
|                         | Moderately Stable   | 0.98      | 0.99   | 0.99     |

Fig. 9 ROC-AUC score of financial health prediction models
Financially Secure, Moderately Stable, or Financially At-Risk. It is superior to existing
approaches in all key performance metrics, allowing for greater interpretability and a
consequential deployment scope for integration into financial advisory and wellness
platforms.
5  Conclusion, limitations, and future scope
This study proposes a novel hybrid deep learning framework for carrying out robust
financial profiling of persons into Financially Secure, Moderately Stable, and Financially
At-Risk. Using a large-scale dataset of 20,000 Indian individuals with income, expenses,
savings, and demographic features, this study presents the higher efficacy of advanced
hybrid models, especially Wide & Deep + CNN and Wide & Deep + BiLSTM. These
models achieved almost perfect classification metrics (Validation Accuracy: 99.44%,
F1-Score: 1.00, ROC-AUC: 1.0000), thus outperforming regular CNNs and less-complex
hybrid models. Furthermore, the pipeline uses TabNet to improve explainability, which
supports transparency during decisions, thus moving toward real-world applications
such as finance advice, stress detection, and aided budgeting. However, there are some
limitations to this work despite its impressive performance. A primary limitation is that,
while the dataset has considerable variables pertaining to structure, it lacks temporal
sequences or longitudinal financial behaviors, which are important in both real-time
financial forecasts and modeling trajectories of stress. Second, the data remained geo-
graphically and culturally confined to Indian individuals, possibly limiting the general-
izability of the models to other populations with different financial habits or economic
systems. Furthermore, some hybrid models (e.g., CNN + MLP) were found to be unstable
because of architectural incompatibilities, suggesting that rigorous integration should

Uppal et al. Discover Artificial Intelligence           (2026) 6:248  Page 20 of 22
Table 5 Comparative analysis of existing techniques vs. the proposed hybrid deep learning
approach for financial health classification
| Dimension | Existing techniques                      | Proposed technique                    |
| --------- | ---------------------------------------- | ------------------------------------- |
| Research  | Focused on segmentation (Researcher 1),  | Accurately classify individuals into  |
objective welfare impact of banking crises (Researcher  Financially Secure, Moderately Stable, and
|     | 2), systemic AI risks (Researcher 3), financial  | Financially At-Risk using hybrid deep learn- |
| --- | ------------------------------------------------ | -------------------------------------------- |
|     | stress testing (Researchers 5 & 6), and early    | ing models                                   |
bankruptcy prediction (Researchers 7 & 8)
Dataset Small-scale or synthetic datasets: 1,874 survey  Real-world, large-scale dataset of 20,000
|     | responses (Researcher 1), simulation data (Re-  | Indian individuals with detailed income, ex- |
| --- | ----------------------------------------------- | -------------------------------------------- |
|     | searcher 2), or stock indicators (Researcher 9) | penditure, savings, and demographic data     |
Input features Survey-based (Researcher 1), macroeconomic  Multivariate features: income, savings
|     | indicators (Researcher 2), stock returns and  | ratio, debt ratio, monthly expenses across  |
| --- | --------------------------------------------- | ------------------------------------------- |
|     | liquidity ratios (Researcher 9)               | categories, city tier, occupation, etc.     |
Modeling  Clustering (Researcher 1), Agent-Based + SVM  15 + deep learning models including CNN,
techniques (Researcher 2), Gradient Boosting + Optimizers  RNN, BiLSTM, GRU, DNN, FCNN, TabNet,
|     | (Researcher 8), CNN + LSTM (Researcher 5) | Autoencoder-based classifiers, and Wide &  |
| --- | ----------------------------------------- | ------------------------------------------ |
Deep hybrids
Hybridization CNN + LSTM/GRU (Researcher 5), CNN + Text  Wide & Deep integrated with CNN, BiLSTM,
|     | Analysis (Researcher 6), optimization-driven DL  | RNN, and Attention mechanisms for joint  |
| --- | ------------------------------------------------ | ---------------------------------------- |
|     | (Researcher 7)                                   | memorization and generalization          |
Key metrics Accuracy: ~95.8% (AWOA-DL, Researcher 7),  Validation Accuracy: 99.44%; ROC-AUC:
|     | Precision: 0.980 (HGSO, Researcher 8), moder- | 1.0000; F1-Score: 1.00 (GRU, BiLSTM, Wide &  |
| --- | --------------------------------------------- | -------------------------------------------- |
|     | ate ROC-AUC (CNN-based models)                | Deep + CNN)                                  |
Model output Binary segmentation (Researcher 1), risk clas- Multi-class classification with granular
|     | sification (Researchers 5–8) | breakdown of three financial health levels |
| --- | ---------------------------- | ------------------------------------------ |
Interpretability Often criticized as black-box (Researcher 4);  Uses TabNet, feature engineering (Savings/
|     | limited transparency | Debt Ratio) to improve model explainability |
| --- | -------------------- | ------------------------------------------- |
Systemic insights Highlights macroeconomic resilience and  Supports individual-level predictions with
|     | regulatory blind spots (Researcher 3) | potential for integration into organizational  |
| --- | ------------------------------------- | ---------------------------------------------- |
wellness systems
Deployment  Conceptual or research-stage tools; not linked  Designed for real-time financial profiling,
readiness to real-time systems robo-advisory, and employee stress mitiga-
tion platforms
be designed. While interpretability remains aided by feature selection, some stakehold-
ers unfamiliar with AI techniques find it a complex challenge. Several promising ave-
nues for future research can be explored. Real-time financial transaction data could be
included in the pipeline, and metrics from behavioral psychology could be integrated to
make predictions more dynamic and personalized. Enriching the dataset to contain indi-
viduals from different geographies and socioeconomic backgrounds will put the model
on a more robust footing. The predictive pipeline can also be implemented in a mobile
application or a financial chatbot to connect academic innovations with their practical
deployment Finally, in sensitive areas like finance, AI deployment should be considered
with aspects such as fairness, mitigation of biases, and transparency.
Author contributions
[AU]: Conception and design of the study, supervision of the research process, and critical revision of the manuscript
for intellectual content.AS]: Data curation, model development, and analysis and interpretation of results.[YA]: Drafting
of the manuscript, literature review, and visualization of findings.[AS & BK]: Editing, proofreading, and ensuring
methodological rigor.All authors were involved in critically revising the paper for its intellectual content, approved the
final version to be published, and agreed to be accountable for all aspects of the work, ensuring that questions related to
accuracy or integrity were appropriately investigated and resolved.
Funding
Open access funding provided by Symbiosis International (Deemed University). (APC): Symbiosis International University,
PUNE.

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 21 of 22
Data availability
The data that support the findings of this study are openly available in [Kaggle.com]at [ h t t p s : / / w w w . k a g g l e . c o m / d a t a s e
t s / s h r i y a s h j a g t a p / i n d i a n - p e r s o n a l - fi n a n c e - a n d - s p e n d i n g - h a b i t s ] ( h t t p s : / w w w . k a g g l e . c o m / d a t a s e t s / s h r i y a s h j a g t a p / i n d i a
n - p er s o n a l - fi n a n c e - a n d - s p e n d i n g - % 2 0 h a b i t s ) , [13].
Declarations
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Informed consent
This study did not involves human participants.
Human and animals participants
This research did not involve any studies with human participants or animals performed by any of the authors.
Competing interests
The authors declare no competing interests.
Received: 24 October 2025 / Accepted: 2 February 2026
References
1. Akash TR, Reza J, Alam MA. Evaluating financial risk management in corporation financial security systems. World J Adv
Res Reviews. 2024;23(1):2203–13.
2. Alessi L, Savona R. Machine learning for financial stability. Data science for economics and finance: methodologies and
applications. Cham: Springer International Publishing; 2021. pp. 65–87.
3. Behera S, Kalagudi V, Das SR. Generative AI-based financial fraud detection system. In: 2025 International conference on
intelligent and innovative technologies in computing, electrical and electronics (IITCEE). IEEE. 2025, pp. 1–7.
4. Chen Z, Chen W, Smiley C, Shah S, Borova I, Langdon D, Moussa R, Beane M, Huang TH, Routledge B, Wang WY. 2021.
Finqa: A dataset of numerical reasoning over financial data. arXiv preprint https://arxiv.org/abs/2109.00122.
5. Chhikara H, Chhikara S, Gupta L. Predictive analytics in finance: leveraging AI and machine learning for investment strate-
gies. In: Utilizing AI and machine learning in financial analysis. IGI Global Scientific Publishing; 2025. pp. 325–36.
6. Dhaka P, Nagpal B. WoM-based deep bilstm: smart disease prediction model using WoM-based deep BiLSTM classifier.
Multimedia Tools Appl. 2023;82(16):25061–82.
7. Elhoseny M, Metawa N, Sztano G, El-Hasnony IM. Deep learning-based model for financial distress prediction. Ann Oper
Res. 2025;345(2):885–907.
8. Fernando J. Financial literacy: What it is, and why it is so important to teach teens.2025. h t t p s : / / w w w . i n v e s t o p e d i a . c o m / t e r
m s / f / fi n a n c i a l - l i t e r a c y . a s p
9. Gailey A. (2024) Survey: 44% of Americans believe their finances will improve in 2025, an increase from previous years. h t t
p s : / / fi n a n c e . y a h o o . c o m / n e w s / s u r v e y - 4 4 - a m e r i c a n s - b e l i e v e - fi n a n c e s - 0 5 1 0 0 0 4 0 8
10. Gensler G, Bailey L. 2020. Deep learning and financial stability. Available from SSRN 3723132.
11. Ghashti JS, Thompson JR. The complexity of financial wellness: examining survey patterns via kernel metric learning and
clustering of mixed-type data. In: Proceedings of the fourth ACM international conference on AI in finance; 2023, pp.
314–322.
12. Gregova E, Valaskova K, Adamko P, Tumpach M, Jaros J. Predicting financial distress of Slovak enterprises: comparison of
selected traditional and learning algorithms methods. Sustainability. 2020;12(10):3954.
13. Indian personal finance and spending habits (2024). h t t p s : / / w w w . k a g g l e . c o m / d a t a s e t s / s h r i y a s h j a g t a p / i n d i a n - p e r s o n a l - fi n
a n c e - a n d - s p e n d i n g - h a b i t s
14. Kalyugina S, Strielkowski W, Ushvitsky L, Astachova E. Sustainable and secure development: facet of personal financial
issues. J Secur Sustain Issues. 2015;5(2):297–304.
15. Kaur K, Kumar Y, Kaur S. Artificial intelligence and machine learning in financial services to improve the business system.
Computational intelligence for modern business systems: emerging applications and strategies. Singapore: Springer
Nature Singapore; 2023. pp. 3–30.
16. Khunger A. DEEP learning for financial stress testing: a data-driven approach to risk management. Int J Innov Stud.2022.
http://dx.doi.org/10.2139/ssrn.5146509.
17. Kuizinienė D, Krilavičius T, Damaševičius R, Maskeliūnas R. Systematic review of financial distress identification using artifi-
cial intelligence methods. Appl Artif Intell. 2022;36(1):2138124.
18. Li W. TabNet for high-dimensional tabular data: advancing interpretability and performance with feature fusion. In: IET
Conference Proceedings CP915. Stevenage, UK: The Institution of Engineering and Technology; 2025, pp. 168–173.
19. Luo A, Zhong L, Wang J, Wang Y, Li S, Tai W. Short-term stock correlation forecasting based on CNN-BiLSTM enhanced by
attention mechanism. IEEE Access; 2024.
20. Mazancová K. Non-Traditional methods for assessing the financial situation of a farm. Econ Bus. 2024;38:68–85.
21. Naved M, Kumar R, Saheb SS. Analyzing financial stability by predicting bankruptcy situations with machine learning. J
Artif Intell Syst Modelling. 2024;1(03):18–35.
22. Polyzos S, Abdulrahman K, Dandu J. Effects of financial instability on subjective well-being: a preference-based approach.
Int J Soc Econ. 2021;48(7):982–98. https://doi.org/10.1108/ijse-10-2020-0693.

Uppal et al. Discover Artificial Intelligence (2026) 6:248 Page 22 of 22
23. Shi X, Zhang Y, Yu M, Zhang L. Deep learning for enhanced risk management: a novel approach to analyzing financial
reports. PeerJ Comput Sci. 2025;11:e2661.
24. Strutner S. (2024) Financial Management explained: scope, objectives & importance. h t t p s : / / w w w . n e t s u i t e . c o m / p o r t a l / r e s
o u r c e / a r t i c l e s / fi n a n c i a l - m a na g e m e n t / fi n a n c i a l - m a n a g e m e n t . s h t m l
25. Vipond T. (2025) Public finance. h t t p s : / / c o r p o r a t e fi n a n c e i n s t i t u t e . c o m / r e s o u r c e s / e c o n o m i c s / p u b l i c - fi n a n c e /
26. Zheng Z, Yang Y, Niu X, Dai HN, Zhou Y. Wide and deep convolutional neural networks for electricity-theft detection to
secure smart grids. IEEE Trans Industr Inf. 2017;14(4):1606–15.
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.