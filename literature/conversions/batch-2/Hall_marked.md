---
conversion_metadata:
  converted_at: "2026-07-22T13:29:36Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Hall.pdf"
  source_pdf_sha256: "9c8ed30add4951d5db5a12bba23596808eda42819155eb2044012c03dd7611fe"
  page_count: 20
  markdown_char_count: 62246
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

MACHINE LEARNING TIME SERIES FORECASTING: A 
COMPREHENSIVE SURVEY AND STOCK MARKET 
APPLICATION

by

TIMOTHY HALL

(Under the Direction of Khaled Rasheed)

ABSTRACT

This thesis presents two complementary studies that advance the understanding and application 
of machine learning techniques in time series forecasting, with a particular focus on financial 
markets. A comprehensive survey identifies top-performing techniques across tree-based 
models, deep learning architectures, and hybrid approaches. Building on these insights, the 
thesis applies a specialized forecasting framework to the domain of day trading. By leveraging a 
combination of LightGBM models with an extensive set of engineered features ranging from 
multi-timeframe technical indicators to contextual stock attributes, the model uses two years of 
second-by-second trade and quote data to estimate risk-reward ratios over multiple forward 
time horizons. Simulated results using realistic execution constraints demonstrate a pronounced 
performance advantage over human day traders, yielding daily returns several orders of 
magnitude higher.

INDEX WORDS:

TIME SERIES FORECASTING, DAY TRADING, STOCK MARKET, FINANCIAL 
MARKETS, MACHINE LEARNING, TREE-BASED, LIGHTGBM

---

<!-- PAGE 2 -->

MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK 
MARKET APPLICATION

by

TIMOTHY HALL

B.S., University of Georgia, 2024

A Thesis Submitted to the Graduate Faculty of the 
University of Georgia in Partial Fulfillment of the Requirements for the Degree.

MASTER OF SCIENCE

ATHENS, GEORGIA

2025

---

<!-- PAGE 3 -->

©2025

Timothy Hall

All Rights Reserved

---

<!-- PAGE 4 -->

MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK 
MARKET APPLICATION

by

TIMOTHY HALL

Major Professor:  Khaled Rasheed

Committee:

Frederick Maier  
 Jin Lu

Electronic Version Approved:

Ron Walcott 
Dean of the Graduate School 
The University of Georgia  
May 2025

---

<!-- PAGE 5 -->

ACKNOWLEDGEMENTS

I would like to thank my major professor, Dr. Rasheed Khaled, for his insight and guidance throughout

the writing of this thesis. I am also deeply grateful to my advisory committee, Frederick Maier and Jin Lu,

for their support and thoughtful feedback on both coursework and thesis work. I would like to thank all

my undergraduate and graduate instructors for equipping me with the knowledge and skills necessary to

undertake this research. Lastly, I am forever thankful to my parents for their unwavering support and

encouragement throughout my academic journey. This thesis would not have been possible without the

mentorship, love, and support I have received along the way.

iv

---

<!-- PAGE 6 -->

CONTENTS

Acknowledgements

List of Figures

List of Tables

iv

vi

vii

1 
1   Introduction 
     1.1    Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  1 
     1.2    Purpose and Scope  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2 
     1.3    Contributions of This Work  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2 
     1.4    Structure of the Thesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  4

2   A Survey of Machine Learning Methods for Time Series Prediction 
5 
     2.1    Introduction   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  6 
     2.2    Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  7 
     2.3    Tree-Based Machine Learning Architectures   . . . . . . . . . . . . . . . . . . . . . . . . . . . .  9 
     2.4    Deep Learning Architectures  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12 
     2.5    Experimental Results and Discussion   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  15 
     2.6    M5 and M6 Forecasting Competitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41 
     2.7    Conclusion  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  45

58 
3   Stock Market Application Paper 
     3.1    Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  59 
     3.2    Related Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  61 
     3.3    Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  64 
     3.4    Results  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  71 
     3.5    Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  81 
     3.6    Conclusion  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  85

4   Conclusion

89

v

---

<!-- PAGE 7 -->

LIST OF FIGURES

2.1      RF and GBDT Architecture  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  11 
2.2      FFNN, CNN, and RNN Architecture  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  13 
2.3      Overall Model Performance FPA and WRA scores . . . . . . . . . . . . . . . . . . . . . . . . .  18 
2.4      Sub-class Model Performance FPA and WRA scores  . . . . . . . . . . . . . . . . . . . . . . .  19 
2.5      Individual Model Performance FPA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20 
2.6      Individual Model Performance WRA scores  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21 
2.7      Time Series Prediction Task Categories  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22 
2.8      Task-Specific Model Performance FPA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24 
2.9      Task-Specific Model Performance WRA scores . . . . . . . . . . . . . . . . . . . . . . . . . . .  24 
2.10    Dataset Size Model Performance FPA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25 
2.11    Dataset Size Model Performance WRA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26 
2.12    Time Interval Model Performance FPA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27 
2.13    Time Interval Model Performance WRA scores . . . . . . . . . . . . . . . . . . . . . . . . . . .  28 
2.14    Research Focus Model Performance FPA scores  . . . . . . . . . . . . . . . . . . . . . . . . . .  29 
2.15    Research Focus Model Performance WRA scores  . . . . . . . . . . . . . . . . . . . . . . . . .  30 
2.16    Error Metrics for Classification Models  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  33 
2.17    Error Metrics for Regression Models  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  34 
2.18    Hyperparameter Optimization Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  35 
3.1      Model 1 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  72 
3.2      Model 1 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  73 
3.3      Model 2 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  74 
3.4      Model 2 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  75 
3.5      Model 3 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  76 
3.6      Model 3 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  77 
3.7      Model 4 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  78 
3.8      Model 4 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  79 
3.9      Model 5 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  80 
3.10    Model 5 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  80

vi

---

<!-- PAGE 8 -->

LIST OF TABLES

2.1    Time Series Prediction Tasks  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  23 
3.1    Model 1 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  74 
3.2    Model 2 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  75 
3.3    Model 3 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  77 
3.4    Model 4 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  78 
3.5    Model 5 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  81

vii

---

<!-- PAGE 9 -->

CHAPTER 1

Introduction

1.1 Motivation

Time series prediction is a widely recognized and important application of machine learning (ML). Time

series  prediction  usually  relies  on  using  historical  patterns  to  accurately  forecast  future  data  points.  Its

significance exists across many domains, including finance, healthcare, energy management, and weather

forecasting.  In  each  of  these  domains,  the  ability  to  accurately  model  and  forecast  future  values  holds

potential  to  optimize  decision-making,  improve  performance,  or  mitigate  risks.  Among  all  time  series

prediction tasks, forecasting stock market behavior is one of the most difficult. This is due to the many

complex factors including the countless individuals and institutions acting on the market at the same time.

Within this domain, day trading, where positions are opened and closed within the same trading day poses

an even greater challenge.

This  difficulty,  however,  also  presents  an  opportunity.  While  human  traders  are  constrained  by

cognitive biases, limited processing capacity, and delayed reaction times, ML systems offer the potential to

systematically uncover patterns that may be invisible to human traders. In this thesis, I explore the premise

that advanced time series prediction ML methods, through their capability to process large amounts of data,

identify subtle patterns, and execute rapid decision-making, offer compelling advantages over traditional

human expertise in time series prediction, particularly in the domain of financial trading.

1

---

<!-- PAGE 10 -->

1.2 Purpose and Scope

My central aim of this study is to extensively explore state-of-the-art ML methodologies for time series

prediction and apply the most promising methods to day trading forecasting in the stock market. This work

is structured as a manuscript-style thesis comprising two major studies.

The first paper, A Survey of Machine Learning Methods for Time Series Prediction, investigates the

landscape of ML techniques applied to time series forecasting. In it, I seek to identify which models offer

the most promise across different forecasting formats and tasks. Unlike many existing surveys, this study

narrows its focus to research that compares  state-of-the-art models within the same experimental setup,

allowing for more meaningful insights into their relative strengths, weaknesses, and situational advantages.

The second paper, Can AI Beat Human Traders? Exploring Machine Learning in Day Trading, applies

the insights gained from the survey to a real-world, trading problem. In it, I implement and evaluate a ML

model designed to replicate and surpass human day trading strategies by using second-by-second trade and

quote data from all U.S. equities over a two-year period.

1.3 Contributions of This Work

This thesis contributes to ML literature in time series forecasting through both a comprehensive review and

practical application. The survey of time series prediction addresses a notable gap in the existing literature.

Previous surveys face limitations in comparative analysis because they analyze independent studies which

each  utilize  a  different  implementation  and  dataset.  This  heterogeneity  prevents  apples  to  apples

comparison. My initial research indicated the superior performance of two classes of ML models:  tree-

based machine learning (TBML) and deep learning (DL) methods. Consequently, this study only reviews

research  that  compares  at  least  one  state-of-the-art  TBML  and  DL  methods  within  the  same  uniform

experimental settings so that nuanced conclusions can be drawn. These conclusions include investigating

in key factors that influence model performance, such as the type of time series task, dataset size, time

2

---

<!-- PAGE 11 -->

interval of historical data, potential biases in model development, and trade-offs between computational

costs and performance.

Key findings of this survey show that specialized TBML architectures like LightGBM and recurrent

neural  network  DL  architectures  like  long  short-term  memory  models  consistently  outperform  other

alternatives,  with  TBML  methods  showcasing  a  notable  advantage  in  computational  efficiency.

Additionally, this study emphasizes that the quality of data is the most influential factor affecting model

performance,  overshadowing  the  incremental  benefits  of  hyperparameter  tuning.  Thus,  considerable

emphasis is placed on feature selection and engineering in the second paper. Similarly, this study found

that  combining  models  and  leveraging  diverse  sources  of  information  further  boosts  forecasting

performance, an insight that heavily informed the construction of the trading model in the second paper.

The second paper applies insights from the survey to develop and evaluate ML models specifically for

a day trading application. Day trading refers to the short-term buying and selling of financial instruments

within a single trading day. Day trading is a risky endeavor and  necessitates rapid decision-making and

high-dimensional data processing capabilities. Only the top performing day trading humans actually make

a profit, and thus in this paper I create a model that mimics the strategies used by human day traders while

leveraging  the  unique  advantages  of  ML  processing  with  the  goal  of  surpassing  the  human  trading

benchmark.

Existing research in this area typically relies on models tailored to individual stocks, limited to longer

time  horizons,  and  often  lacking  in  feature  diversity.  In  contrast,  human  day  traders  face  different

constraints as they are prone to emotional decision-making, have slower processing speeds, and can only

monitor a few stocks at a time. The ML approach presented in this study overcomes these limitations by

simultaneously analyzing the entire universe of U.S. equities and can manage many positions at one time.

This  study  advances  the  current  literature  by  addressing  key  gaps  in  ML  applications,  leveraging  a

combination  of  models  trained  on  second-by-second  trade  and  quote  data,  and  operating  on  a

comprehensive, high-dimensional dataset.

3

---

<!-- PAGE 12 -->

In this paper, I conduct a series of experiments to test various regularization techniques, risk-reward

horizon weighting strategies, and execution pricing methods. I evaluate models using both idealized close

prices and realistic execution prices derived from the bid and ask prices at which investors are willing to

transact, with both methods resulting in profitable models. The model that performed best under realistic

trading environments incorporated a min-max regularized target feature based on a risk-reward ratio and

applied  an  equal  weighting  scheme  in  this  risk-reward  calculation.  The  results  of  this  model  show  an

average profit of 20,000 bps per day with a Sharpe ratio of 15.78 across an average of 999 trades per day.

This performance is driven by the model’s ability to simultaneously manage a large number of positions at

the same time.

The  findings  from  this  research  show  that  the  ML  model  I  developed  achieves  performance  far

exceeding the profitability of top human day traders, demonstrating average daily returns more than 500

times higher. Additionally, the methodological contributions provide a comprehensive, practical blueprint

for  high-frequency  data  acquisition,  preprocessing,  and  feature  engineering,  facilitating  replication  and

extension of the study by future researchers.

1.4 Structure of the Thesis

The remainder of this thesis is organized as follows: Chapter 2 presents a detailed survey on ML methods

for time series prediction, identifying best practices and critical factors that influence model effectiveness.

Chapter 3 introduces the empirical research of applying these methodologies to the challenge of day trading,

detailing  data  methodologies,  model  development,  and  performance  evaluation.  Finally,  Chapter  4

concludes with a summary of the contributions and recommendations for continued research in this area.

4

---

<!-- PAGE 13 -->

CHAPTER 2

A Survey of Machine Learning Methods for 
Time Series Prediction1

1 Timothy Hall. Submitted to Applied Sciences, 4/15/25

5

---

<!-- PAGE 14 -->

Abstract

This study provides a comprehensive survey of the top-performing research papers in the field of time

series prediction, offering insights into the most effective machine learning techniques, including tree-

based, deep learning, and hybrid methods. It explores key factors influencing model performance, such

as the type of time series task, dataset size, and the time interval of historical data. Additionally, the study

investigates potential biases in model development and weighs the trade-offs between computational costs

and performance. A detailed analysis of the most used error metrics and hyperparameter tuning methods

in  the  reviewed  papers  is  included.  Furthermore,  the  study  evaluates  the  results  from  prominent

forecasting competitions, such as M5 and M6, to enrich the analysis. The findings of this paper highlight

that tree-based methods like LightGBM and deep learning methods like recurrent neural networks deliver

the best performance in time series forecasting, with tree-based methods offering a significant advantage

in  terms  of  computational  efficiency.  The  paper  concludes  with  practical  recommendations  for

approaching  time  series forecasting  tasks, offering  valuable  insights and actionable  strategies  that can

enhance the accuracy and reliability of predictions derived from time series data.

2.1    Introduction

Time  Series  Prediction  is  the  process  of  predicting  a  future  value  based  on  historical  sequential

observations. Accurate predictions based on time series data plays a crucial role in a wide range of domains

where  forecasting  future  values  is  essential  for  strategic-planning,  resource  management,  and  decision-

making.  Applications  of  time  series  prediction  span  numerous  fields,  including  electricity  consumption

forecasting,  environmental  quality  assessments  (e.g.,  air  and  water  quality),  meteorological  predictions

(e.g., rainfall, solar radiation, and wind patterns), medical diagnostics (e.g., forecasting COVID-19 case

trends and pneumonia incidences), traffic flow prediction, and financial domains like sales forecasting and

stock market analysis.

6

---

<!-- PAGE 15 -->

In recent years, models based on Machine Learning (ML) have demonstrated the most success in time

series forecasting and are able to generalize well to unseen data, unlike models based solely on probability

and statistics. Specifically, Tree-Based Machine Learning (TBML) and Deep Learning (DL) have emerged

as  the  most  prominent  approaches,  excelling  in  scenarios  where  complex,  nonlinear  dependencies exist

within  the  data.  Their  ability  to  generalize  to  unseen  data  makes  them  highly  applicable  to  real-world

problems with diverse and dynamic characteristics.

While numerous studies have examined these techniques within specific domains, and several survey

papers (Lim & Zohren, 2021; Z. Liu et al., 2021) have analyzed various approaches to time series prediction

across domains, existing literature reviews face a significant limitation. Current survey papers struggle to

draw meaningful comparisons between models because they analyze independent studies, each utilizing

different implementations and datasets. This heterogeneity in experimental setups prevents direct model

comparisons  and  obscures  true  performance  differences.  This  paper  addresses  this  gap  by  exclusively

reviewing studies that compare both TBML methods and DL approaches within the same experimental

framework. By focusing on research where both methodologies are implemented and evaluated by the same

researchers using identical datasets, this survey enables more robust conclusions about the relative strengths

and weaknesses of these modeling approaches.

The remainder of this paper is organized as follows: Section 2.2 outlines the methodology employed

in  this  survey.  Section  2.3  reviews  TBML  architectures,  while  Section  2.4 examines  DL architectures.

Section 2.5 presents experimental results and discusses findings. Section 2.6 highlights recent time series

prediction competitions, and Section 2.7 concludes the paper.

2.2 Methodology

A rigorous and systematic methodology was employed to identify the most relevant research papers for this

survey. Web of Science was selected as the primary database because it is a trusted publisher-independent

source of data with comprehensive coverage of peer-reviewed scientific literature. Given the objective of

7

---

<!-- PAGE 16 -->

comparing TBML methods with DL approaches in time series prediction, this paper establishes specific

inclusion criteria for article selection:

1.  Focus on Time Series Applications: The research must address problems involving time series

data.

2.  Utilization of Advanced TBML Methods: Studies must implement advanced TBML architectures,

particularly  gradient-boosted  decision  trees  or  similar  structures  (e.g.,  XGBoost,  LightGBM,  or

CatBoost).

3.  Utilization of Advanced Neural Network (NN) Architectures: Papers must explore sophisticated

NN architectures, including but not limited to recurrent neural networks (RNN), feedforward neural

networks  (FFNN),  convolutional  neural  networks  (CNN),  long  short-term  memory  networks

(LSTM), gated recurrent units (GRU), or Transformers.

4.  Direct Comparisons Using Identical Datasets: The research must present comparative evaluations

of  at  least  one  TBML  and  one  DL  architecture  under  identical  experimental  setups,  ensuring

consistent datasets and conditions.

To identify relevant literature, a comprehensive search query was developed as follows:

(ALL=(XGBoost)  OR  ALL=(LightGBM)  OR  ALL=(CatBoost)  OR  ALL=("gradient  boost*"))  AND

(ALL=("time  series")  OR  ALL=("time  sequence")  OR  ALL=("temporal  series")  OR  ALL=("temporal

sequence") OR ALL=("time forecast*")) AND (ALL=("LSTM") OR ALL=("ANN") OR ALL=("CNN")

OR  ALL=("RNN")  OR  ALL=("transformer")  OR  ALL=("GRU")  OR  ALL=("deep  neur*")  OR

ALL=("deep lear*"))

This query yielded 589 papers published between 2017 and 2024. To ensure focus on the most

influential research, papers were initially selected based on citation count. From the top 100 most-cited

papers, 65 articles satisfied the inclusion criteria. To maintain contemporary relevance and capture recent

8

---

<!-- PAGE 17 -->

developments in the field, additional temporal criteria were implemented: a minimum of 10 papers per

year from 2020 to 2024 must be included. Consequently, 4 highly cited papers from 2023 and the 10

most-cited articles from 2024 were incorporated. In total, this survey encompasses 79 influential papers

investigating the comparative performance of TBML and DL approaches in time series analysis (see

Appendix A for the complete list of included studies).

2.3 Tree-Based Machine Learning Architectures

This section will present an overview of the best performing TBML Architectures, which are widely utilized

for both regression and classification tasks. These include Random Forests (RF), Gradient Boosted Decision

Trees  (GBDT),  and  three  prominent  implementations  of  GBDT:  XGBoost,  LightGBM,  and  CatBoost.

Figure 2.1 provides a comparative visualization of the structural differences between RF and GBDT.

2.3.1 Random Forests

Random Forests (RF) is an ensemble learning method that constructs multiple decision trees and combines

their  outputs  through  averaging for regression  tasks  or majority  voting  for  classification  tasks.  RF  uses

bootstrapping  to  train  individual  decision  trees  on  a  random  subset  of  the  data  at  each  split.  This

randomization,  coupled  with  its  ensemble  nature,  enhances  the  robustness  of  RF  compared  to  single

decision  trees,  significantly  reducing  the  risk  of  overfitting.  The  most  widely  used  library  for  RF

implementation in the studies reviewed in this paper is Scikit-learn.

2.3.2 Gradient Boosted Decision Trees

Gradient  Boosted  Decision  Trees  (GBDTs)  is  a  machine  learning  algorithm  that  aggregates  predictions

from multiple weak learners, typically decision trees. GBDTs use “boosting” to build models iteratively

where each subsequent models focuses on correcting mistakes made by previous models. The algorithm

achieves this by optimizing a differentiable loss function using gradient descent. GBDTs are suitable for

both  classification  tasks,  using  loss  functions  such  as  cross-entropy,  and  regression  tasks,  using  loss

9

---

<!-- PAGE 18 -->

functions like mean squared error. Key hyperparameters to tune in GBDT include tree depth and learning

rate,  which  are  crucial  for  balancing  model  complexity  and  reducing  overfitting.  While  Scikit-learn

provides  a  general  implementation  of  GBDT,  the  three  most  prominent  and  high-performing

implementations discussed in this survey are XGBoost, LightGBM, and CatBoost, each offering distinct

advantages.

2.3.2.1 XGBoost

XGBoost, eXtreme Gradient Boosting (Chen & Guestrin, 2016), introduced by Tianqi Chen in 2014, was

designed  to  address  key  limitations  of  traditional  GBDT,  particularly  computational  efficiency  and

scalability.  XGBoost  gained  immediate  popularity  due  to  its  significant  speed  improvements,  achieved

through innovative approaches in decision tree construction. Unlike the greedy splitting methods used in

standard GBDT, XGBoost employs a similarity score to evaluate potential splits. This score measures the

homogeneity of observations within a node relative to the target variable, assessing the gain provided by a

split.  To  further reduce  overfitting,  XGBoost  incorporates  several  techniques,  including  pruning,  where

branches with a gain below a threshold (hyperparameter gamma, γ) are removed. Similarly, XGBoost has

several regularization techniques that prevent overfitting by penalizing complex decision trees. XGBoost

also supports advanced features such as built-in cross-validation and highly scalable parallel processing,

making it ideal for large-scale datasets.

2.3.2.2 LightGBM

LightGBM (G. Ke et al., 2017), developed by Microsoft in 2017, shares many foundational principles with

XGBoost with an even larger focus on computational efficiency. LightGBM achieves superior speed by

employing  histogram-based  binning,  which  discretizes  continuous  features  into  bins,  trading  minor

accuracy losses for dramatic speed gains. Additionally, LightGBM introduces Exclusive Feature Bundling,

which is particularly effective for many real-world datasets with high-dimensional sparse features because

it consolidates mutually exclusive features into a single  representation. Another innovation is Gradient-

10

---

<!-- PAGE 19 -->

Based  One-Side  Sampling,  which  prioritizes  instances  with  large  gradients  while  randomly  sampling

smaller gradients, optimizing learning efficiency. LightGBM also utilizes a leaf-wise tree growth strategy,

as opposed to the level-wise growth used in traditional GBDT and XGBoost. This approach selectively

grows the leaf with the greatest potential to improve the model, enabling faster convergence and improved

accuracy.

Figure 2.1: Illustrates the architectural differences between RF and GBDT, highlighting attributes 
unique to RF in green and those specific to GBDT in blue.

11

---

<!-- PAGE 20 -->

2.3.2.3 CatBoost

CatBoost  (Prokhorenkova  et  al.,  2018),  developed  by  Yandex  in  2017,  was  designed  with  a  specific

emphasis  on  handling  datasets  with  categorical  features.  One  of  its  key  innovations  is  a  unique

implementation of target encoding which takes the concept of traditional target encoding, where categorical

values  are  replaced  with  the  mean  of  the  target  variable  for  each  category,  and  instead  constructs  the

encoding  process  using  only  previous  data  to  avoid  data  leakage.  Another  distinguishing  feature  of

CatBoost is its use of symmetric decision trees, where all leaves at the same depth use identical splitting

criteria.  This  structure  not  only  accelerates  training  but  also  significantly  reduces  inference  time,  an

essential advantage in some time-sensitive applications of real-world forecasting.

2.4 Deep Learning Architectures

This section presents an overview of the most prominent Deep Learning (DL) architectures encountered in

the surveyed literature. DL will be used in this paper to describe a subset of machine learning that utilizes

neural networks to perform classification and regression tasks. The architectures are categorized into four

primary  groups:  Feed-Forward  Neural  Networks  (FFNN),  Recurrent  Neural  Networks  (RNN),

Convolutional  Neural  Networks  (CNN),  and  Attention-based  architectures.  Figure  2.2  presents  a  visual

representation of a FFNN, highlighting the architectural modifications required to transform it into a RNN

or CNN.

2.4.1 Feed-Forward Neural Networks

The term Feed-Forward Neural Network (FFNN) is often used interchangeably with other terminologies in

the literature, including Artificial Neural Network (ANN), Neural Network (NN), Multilayer Perceptron

(MLP),  Back  Propagation  Neural  Network  (BPNN)  (Nan  et  al.,  2022;  Pan  et  al.,  2023),  Deep  Neural

Network (DNN), and Deep Feed-Forward Neural Network (DFFNN). These networks are characterized by

12

Reproduced with permission of copyright owner. Further reproduction prohibited without permission.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

MACHINE LEARNING TIME SERIES FORECASTING: A
COMPREHENSIVE SURVEY AND STOCK MARKET
APPLICATION

by

TIMOTHY HALL

(Under the Direction of Khaled Rasheed)

ABSTRACT

This thesis presents two complementary studies that advance the understanding and application
of machine learning techniques in time series forecasting, with a particular focus on financial
markets. A comprehensive survey identifies top-performing techniques across tree-based
models, deep learning architectures, and hybrid approaches. Building on these insights, the
thesis applies a specialized forecasting framework to the domain of day trading. By leveraging a
combination of LightGBM models with an extensive set of engineered features ranging from
multi-timeframe technical indicators to contextual stock attributes, the model uses two years of
second-by-second trade and quote data to estimate risk-reward ratios over multiple forward
time horizons. Simulated results using realistic execution constraints demonstrate a pronounced
performance advantage over human day traders, yielding daily returns several orders of
magnitude higher.

INDEX WORDS:

TIME SERIES FORECASTING, DAY TRADING, STOCK MARKET, FINANCIAL
MARKETS, MACHINE LEARNING, TREE-BASED, LIGHTGBM

MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK
MARKET APPLICATION

by

TIMOTHY HALL

B.S., University of Georgia, 2024

A Thesis Submitted to the Graduate Faculty of the
University of Georgia in Partial Fulfillment of the Requirements for the Degree.

MASTER OF SCIENCE

ATHENS, GEORGIA

2025

©2025

Timothy Hall

All Rights Reserved

MACHINE LEARNING TIME SERIES FORECASTING: A COMPREHENSIVE SURVEY AND STOCK
MARKET APPLICATION

by

TIMOTHY HALL

Major Professor:  Khaled Rasheed

Committee:

Frederick Maier
 Jin Lu

Electronic Version Approved:

Ron Walcott
Dean of the Graduate School
The University of Georgia
May 2025

ACKNOWLEDGEMENTS

I would like to thank my major professor, Dr. Rasheed Khaled, for his insight and guidance throughout

the writing of this thesis. I am also deeply grateful to my advisory committee, Frederick Maier and Jin Lu,

for their support and thoughtful feedback on both coursework and thesis work. I would like to thank all

my undergraduate and graduate instructors for equipping me with the knowledge and skills necessary to

undertake this research. Lastly, I am forever thankful to my parents for their unwavering support and

encouragement throughout my academic journey. This thesis would not have been possible without the

mentorship, love, and support I have received along the way.

 iv

CONTENTS

Acknowledgements

List of Figures

List of Tables

iv

vi

vii

1
1   Introduction
     1.1    Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  1
     1.2    Purpose and Scope  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2
     1.3    Contributions of This Work  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2
     1.4    Structure of the Thesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  4

2   A Survey of Machine Learning Methods for Time Series Prediction
5
     2.1    Introduction   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  6
     2.2    Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  7
     2.3    Tree-Based Machine Learning Architectures   . . . . . . . . . . . . . . . . . . . . . . . . . . . .  9
     2.4    Deep Learning Architectures  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12
     2.5    Experimental Results and Discussion   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  15
     2.6    M5 and M6 Forecasting Competitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
     2.7    Conclusion  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  45

58
3   Stock Market Application Paper
     3.1    Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  59
     3.2    Related Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  61
     3.3    Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  64
     3.4    Results  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  71
     3.5    Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  81
     3.6    Conclusion  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  85

4   Conclusion

89

 v

LIST OF FIGURES

2.1      RF and GBDT Architecture  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  11
2.2      FFNN, CNN, and RNN Architecture  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  13
2.3      Overall Model Performance FPA and WRA scores . . . . . . . . . . . . . . . . . . . . . . . . .  18
2.4      Sub-class Model Performance FPA and WRA scores  . . . . . . . . . . . . . . . . . . . . . . .  19
2.5      Individual Model Performance FPA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
2.6      Individual Model Performance WRA scores  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21
2.7      Time Series Prediction Task Categories  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22
2.8      Task-Specific Model Performance FPA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
2.9      Task-Specific Model Performance WRA scores . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
2.10    Dataset Size Model Performance FPA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
2.11    Dataset Size Model Performance WRA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
2.12    Time Interval Model Performance FPA scores . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
2.13    Time Interval Model Performance WRA scores . . . . . . . . . . . . . . . . . . . . . . . . . . .  28
2.14    Research Focus Model Performance FPA scores  . . . . . . . . . . . . . . . . . . . . . . . . . .  29
2.15    Research Focus Model Performance WRA scores  . . . . . . . . . . . . . . . . . . . . . . . . .  30
2.16    Error Metrics for Classification Models  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  33
2.17    Error Metrics for Regression Models  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  34
2.18    Hyperparameter Optimization Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  35
3.1      Model 1 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  72
3.2      Model 1 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  73
3.3      Model 2 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  74
3.4      Model 2 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  75
3.5      Model 3 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  76
3.6      Model 3 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  77
3.7      Model 4 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  78
3.8      Model 4 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  79
3.9      Model 5 Heatmap  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  80
3.10    Model 5 Cumulative Profit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  80

 vi

LIST OF TABLES

2.1    Time Series Prediction Tasks  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  23
3.1    Model 1 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  74
3.2    Model 2 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  75
3.3    Model 3 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  77
3.4    Model 4 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  78
3.5    Model 5 Performance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  81

 vii

CHAPTER 1

Introduction

1.1 Motivation

Time series prediction is a widely recognized and important application of machine learning (ML). Time

series  prediction  usually  relies  on  using  historical  patterns  to  accurately  forecast  future  data  points.  Its

significance exists across many domains, including finance, healthcare, energy management, and weather

forecasting.  In  each  of  these  domains,  the  ability  to  accurately  model  and  forecast  future  values  holds

potential  to  optimize  decision-making,  improve  performance,  or  mitigate  risks.  Among  all  time  series

prediction tasks, forecasting stock market behavior is one of the most difficult. This is due to the many

complex factors including the countless individuals and institutions acting on the market at the same time.

Within this domain, day trading, where positions are opened and closed within the same trading day poses

an even greater challenge.

This  difficulty,  however,  also  presents  an  opportunity.  While  human  traders  are  constrained  by

cognitive biases, limited processing capacity, and delayed reaction times, ML systems offer the potential to

systematically uncover patterns that may be invisible to human traders. In this thesis, I explore the premise

that advanced time series prediction ML methods, through their capability to process large amounts of data,

identify subtle patterns, and execute rapid decision-making, offer compelling advantages over traditional

human expertise in time series prediction, particularly in the domain of financial trading.

 1

1.2 Purpose and Scope

My central aim of this study is to extensively explore state-of-the-art ML methodologies for time series

prediction and apply the most promising methods to day trading forecasting in the stock market. This work

is structured as a manuscript-style thesis comprising two major studies.

The first paper, A Survey of Machine Learning Methods for Time Series Prediction, investigates the

landscape of ML techniques applied to time series forecasting. In it, I seek to identify which models offer

the most promise across different forecasting formats and tasks. Unlike many existing surveys, this study

narrows its focus to research that compares  state-of-the-art models within the same experimental setup,

allowing for more meaningful insights into their relative strengths, weaknesses, and situational advantages.

The second paper, Can AI Beat Human Traders? Exploring Machine Learning in Day Trading, applies

the insights gained from the survey to a real-world, trading problem. In it, I implement and evaluate a ML

model designed to replicate and surpass human day trading strategies by using second-by-second trade and

quote data from all U.S. equities over a two-year period.

1.3 Contributions of This Work

This thesis contributes to ML literature in time series forecasting through both a comprehensive review and

practical application. The survey of time series prediction addresses a notable gap in the existing literature.

Previous surveys face limitations in comparative analysis because they analyze independent studies which

each  utilize  a  different  implementation  and  dataset.  This  heterogeneity  prevents  apples  to  apples

comparison. My initial research indicated the superior performance of two classes of ML models:  tree-

based machine learning (TBML) and deep learning (DL) methods. Consequently, this study only reviews

research  that  compares  at  least  one  state-of-the-art  TBML  and  DL  methods  within  the  same  uniform

experimental settings so that nuanced conclusions can be drawn. These conclusions include investigating

in key factors that influence model performance, such as the type of time series task, dataset size, time

 2

interval of historical data, potential biases in model development, and trade-offs between computational

costs and performance.

Key findings of this survey show that specialized TBML architectures like LightGBM and recurrent

neural  network  DL  architectures  like  long  short-term  memory  models  consistently  outperform  other

alternatives,  with  TBML  methods  showcasing  a  notable  advantage  in  computational  efficiency.

Additionally, this study emphasizes that the quality of data is the most influential factor affecting model

performance,  overshadowing  the  incremental  benefits  of  hyperparameter  tuning.  Thus,  considerable

emphasis is placed on feature selection and engineering in the second paper. Similarly, this study found

that  combining  models  and  leveraging  diverse  sources  of  information  further  boosts  forecasting

performance, an insight that heavily informed the construction of the trading model in the second paper.

The second paper applies insights from the survey to develop and evaluate ML models specifically for

a day trading application. Day trading refers to the short-term buying and selling of financial instruments

within a single trading day. Day trading is a risky endeavor and  necessitates rapid decision-making and

high-dimensional data processing capabilities. Only the top performing day trading humans actually make

a profit, and thus in this paper I create a model that mimics the strategies used by human day traders while

leveraging  the  unique  advantages  of  ML  processing  with  the  goal  of  surpassing  the  human  trading

benchmark.

Existing research in this area typically relies on models tailored to individual stocks, limited to longer

time  horizons,  and  often  lacking  in  feature  diversity.  In  contrast,  human  day  traders  face  different

constraints as they are prone to emotional decision-making, have slower processing speeds, and can only

monitor a few stocks at a time. The ML approach presented in this study overcomes these limitations by

simultaneously analyzing the entire universe of U.S. equities and can manage many positions at one time.

This  study  advances  the  current  literature  by  addressing  key  gaps  in  ML  applications,  leveraging  a

combination  of  models  trained  on  second-by-second  trade  and  quote  data,  and  operating  on  a

comprehensive, high-dimensional dataset.

 3

In this paper, I conduct a series of experiments to test various regularization techniques, risk-reward

horizon weighting strategies, and execution pricing methods. I evaluate models using both idealized close

prices and realistic execution prices derived from the bid and ask prices at which investors are willing to

transact, with both methods resulting in profitable models. The model that performed best under realistic

trading environments incorporated a min-max regularized target feature based on a risk-reward ratio and

applied  an  equal  weighting  scheme  in  this  risk-reward  calculation.  The  results  of  this  model  show  an

average profit of 20,000 bps per day with a Sharpe ratio of 15.78 across an average of 999 trades per day.

This performance is driven by the model’s ability to simultaneously manage a large number of positions at

the same time.

The  findings  from  this  research  show  that  the  ML  model  I  developed  achieves  performance  far

exceeding the profitability of top human day traders, demonstrating average daily returns more than 500

times higher. Additionally, the methodological contributions provide a comprehensive, practical blueprint

for  high-frequency  data  acquisition,  preprocessing,  and  feature  engineering,  facilitating  replication  and

extension of the study by future researchers.

1.4 Structure of the Thesis

The remainder of this thesis is organized as follows: Chapter 2 presents a detailed survey on ML methods

for time series prediction, identifying best practices and critical factors that influence model effectiveness.

Chapter 3 introduces the empirical research of applying these methodologies to the challenge of day trading,

detailing  data  methodologies,  model  development,  and  performance  evaluation.  Finally,  Chapter  4

concludes with a summary of the contributions and recommendations for continued research in this area.

 4

CHAPTER 2

A Survey of Machine Learning Methods for
Time Series Prediction1

1 Timothy Hall. Submitted to Applied Sciences, 4/15/25

 5

Abstract

This study provides a comprehensive survey of the top-performing research papers in the field of time

series prediction, offering insights into the most effective machine learning techniques, including tree-

based, deep learning, and hybrid methods. It explores key factors influencing model performance, such

as the type of time series task, dataset size, and the time interval of historical data. Additionally, the study

investigates potential biases in model development and weighs the trade-offs between computational costs

and performance. A detailed analysis of the most used error metrics and hyperparameter tuning methods

in  the  reviewed  papers  is  included.  Furthermore,  the  study  evaluates  the  results  from  prominent

forecasting competitions, such as M5 and M6, to enrich the analysis. The findings of this paper highlight

that tree-based methods like LightGBM and deep learning methods like recurrent neural networks deliver

the best performance in time series forecasting, with tree-based methods offering a significant advantage

in  terms  of  computational  efficiency.  The  paper  concludes  with  practical  recommendations  for

approaching  time  series forecasting  tasks, offering  valuable  insights and actionable  strategies  that can

enhance the accuracy and reliability of predictions derived from time series data.

2.1    Introduction

Time  Series  Prediction  is  the  process  of  predicting  a  future  value  based  on  historical  sequential

observations. Accurate predictions based on time series data plays a crucial role in a wide range of domains

where  forecasting  future  values  is  essential  for  strategic-planning,  resource  management,  and  decision-

making.  Applications  of  time  series  prediction  span  numerous  fields,  including  electricity  consumption

forecasting,  environmental  quality  assessments  (e.g.,  air  and  water  quality),  meteorological  predictions

(e.g., rainfall, solar radiation, and wind patterns), medical diagnostics (e.g., forecasting COVID-19 case

trends and pneumonia incidences), traffic flow prediction, and financial domains like sales forecasting and

stock market analysis.

 6

In recent years, models based on Machine Learning (ML) have demonstrated the most success in time

series forecasting and are able to generalize well to unseen data, unlike models based solely on probability

and statistics. Specifically, Tree-Based Machine Learning (TBML) and Deep Learning (DL) have emerged

as  the  most  prominent  approaches,  excelling  in  scenarios  where  complex,  nonlinear  dependencies exist

within  the  data.  Their  ability  to  generalize  to  unseen  data  makes  them  highly  applicable  to  real-world

problems with diverse and dynamic characteristics.

While numerous studies have examined these techniques within specific domains, and several survey

papers (Lim & Zohren, 2021; Z. Liu et al., 2021) have analyzed various approaches to time series prediction

across domains, existing literature reviews face a significant limitation. Current survey papers struggle to

draw meaningful comparisons between models because they analyze independent studies, each utilizing

different implementations and datasets. This heterogeneity in experimental setups prevents direct model

comparisons  and  obscures  true  performance  differences.  This  paper  addresses  this  gap  by  exclusively

reviewing studies that compare both TBML methods and DL approaches within the same experimental

framework. By focusing on research where both methodologies are implemented and evaluated by the same

researchers using identical datasets, this survey enables more robust conclusions about the relative strengths

and weaknesses of these modeling approaches.

The remainder of this paper is organized as follows: Section 2.2 outlines the methodology employed

in  this  survey.  Section  2.3  reviews  TBML  architectures,  while  Section  2.4 examines  DL architectures.

Section 2.5 presents experimental results and discusses findings. Section 2.6 highlights recent time series

prediction competitions, and Section 2.7 concludes the paper.

2.2 Methodology

A rigorous and systematic methodology was employed to identify the most relevant research papers for this

survey. Web of Science was selected as the primary database because it is a trusted publisher-independent

source of data with comprehensive coverage of peer-reviewed scientific literature. Given the objective of

 7

comparing TBML methods with DL approaches in time series prediction, this paper establishes specific

inclusion criteria for article selection:

1.  Focus on Time Series Applications: The research must address problems involving time series

data.

2.  Utilization of Advanced TBML Methods: Studies must implement advanced TBML architectures,

particularly  gradient-boosted  decision  trees  or  similar  structures  (e.g.,  XGBoost,  LightGBM,  or

CatBoost).

3.  Utilization of Advanced Neural Network (NN) Architectures: Papers must explore sophisticated

NN architectures, including but not limited to recurrent neural networks (RNN), feedforward neural

networks  (FFNN),  convolutional  neural  networks  (CNN),  long  short-term  memory  networks

(LSTM), gated recurrent units (GRU), or Transformers.

4.  Direct Comparisons Using Identical Datasets: The research must present comparative evaluations

of  at  least  one  TBML  and  one  DL  architecture  under  identical  experimental  setups,  ensuring

consistent datasets and conditions.

To identify relevant literature, a comprehensive search query was developed as follows:

(ALL=(XGBoost)  OR  ALL=(LightGBM)  OR  ALL=(CatBoost)  OR  ALL=("gradient  boost*"))  AND

(ALL=("time  series")  OR  ALL=("time  sequence")  OR  ALL=("temporal  series")  OR  ALL=("temporal

sequence") OR ALL=("time forecast*")) AND (ALL=("LSTM") OR ALL=("ANN") OR ALL=("CNN")

OR  ALL=("RNN")  OR  ALL=("transformer")  OR  ALL=("GRU")  OR  ALL=("deep  neur*")  OR

ALL=("deep lear*"))

This query yielded 589 papers published between 2017 and 2024. To ensure focus on the most

influential research, papers were initially selected based on citation count. From the top 100 most-cited

papers, 65 articles satisfied the inclusion criteria. To maintain contemporary relevance and capture recent

 8

developments in the field, additional temporal criteria were implemented: a minimum of 10 papers per

year from 2020 to 2024 must be included. Consequently, 4 highly cited papers from 2023 and the 10

most-cited articles from 2024 were incorporated. In total, this survey encompasses 79 influential papers

investigating the comparative performance of TBML and DL approaches in time series analysis (see

Appendix A for the complete list of included studies).

2.3 Tree-Based Machine Learning Architectures

This section will present an overview of the best performing TBML Architectures, which are widely utilized

for both regression and classification tasks. These include Random Forests (RF), Gradient Boosted Decision

Trees  (GBDT),  and  three  prominent  implementations  of  GBDT:  XGBoost,  LightGBM,  and  CatBoost.

Figure 2.1 provides a comparative visualization of the structural differences between RF and GBDT.

2.3.1 Random Forests

Random Forests (RF) is an ensemble learning method that constructs multiple decision trees and combines

their  outputs  through  averaging for regression  tasks  or majority  voting  for  classification  tasks.  RF  uses

bootstrapping  to  train  individual  decision  trees  on  a  random  subset  of  the  data  at  each  split.  This

randomization,  coupled  with  its  ensemble  nature,  enhances  the  robustness  of  RF  compared  to  single

decision  trees,  significantly  reducing  the  risk  of  overfitting.  The  most  widely  used  library  for  RF

implementation in the studies reviewed in this paper is Scikit-learn.

2.3.2 Gradient Boosted Decision Trees

Gradient  Boosted  Decision  Trees  (GBDTs)  is  a  machine  learning  algorithm  that  aggregates  predictions

from multiple weak learners, typically decision trees. GBDTs use “boosting” to build models iteratively

where each subsequent models focuses on correcting mistakes made by previous models. The algorithm

achieves this by optimizing a differentiable loss function using gradient descent. GBDTs are suitable for

both  classification  tasks,  using  loss  functions  such  as  cross-entropy,  and  regression  tasks,  using  loss

 9

functions like mean squared error. Key hyperparameters to tune in GBDT include tree depth and learning

rate,  which  are  crucial  for  balancing  model  complexity  and  reducing  overfitting.  While  Scikit-learn

provides  a  general  implementation  of  GBDT,  the  three  most  prominent  and  high-performing

implementations discussed in this survey are XGBoost, LightGBM, and CatBoost, each offering distinct

advantages.

2.3.2.1 XGBoost

XGBoost, eXtreme Gradient Boosting (Chen & Guestrin, 2016), introduced by Tianqi Chen in 2014, was

designed  to  address  key  limitations  of  traditional  GBDT,  particularly  computational  efficiency  and

scalability.  XGBoost  gained  immediate  popularity  due  to  its  significant  speed  improvements,  achieved

through innovative approaches in decision tree construction. Unlike the greedy splitting methods used in

standard GBDT, XGBoost employs a similarity score to evaluate potential splits. This score measures the

homogeneity of observations within a node relative to the target variable, assessing the gain provided by a

split.  To  further reduce  overfitting,  XGBoost  incorporates  several  techniques,  including  pruning,  where

branches with a gain below a threshold (hyperparameter gamma, γ) are removed. Similarly, XGBoost has

several regularization techniques that prevent overfitting by penalizing complex decision trees. XGBoost

also supports advanced features such as built-in cross-validation and highly scalable parallel processing,

making it ideal for large-scale datasets.

2.3.2.2 LightGBM

LightGBM (G. Ke et al., 2017), developed by Microsoft in 2017, shares many foundational principles with

XGBoost with an even larger focus on computational efficiency. LightGBM achieves superior speed by

employing  histogram-based  binning,  which  discretizes  continuous  features  into  bins,  trading  minor

accuracy losses for dramatic speed gains. Additionally, LightGBM introduces Exclusive Feature Bundling,

which is particularly effective for many real-world datasets with high-dimensional sparse features because

it consolidates mutually exclusive features into a single  representation. Another innovation is Gradient-

 10

Based  One-Side  Sampling,  which  prioritizes  instances  with  large  gradients  while  randomly  sampling

smaller gradients, optimizing learning efficiency. LightGBM also utilizes a leaf-wise tree growth strategy,

as opposed to the level-wise growth used in traditional GBDT and XGBoost. This approach selectively

grows the leaf with the greatest potential to improve the model, enabling faster convergence and improved

accuracy.

Figure 2.1: Illustrates the architectural differences between RF and GBDT, highlighting attributes
unique to RF in green and those specific to GBDT in blue.

 11

2.3.2.3 CatBoost

CatBoost  (Prokhorenkova  et  al.,  2018),  developed  by  Yandex  in  2017,  was  designed  with  a  specific

emphasis  on  handling  datasets  with  categorical  features.  One  of  its  key  innovations  is  a  unique

implementation of target encoding which takes the concept of traditional target encoding, where categorical

values  are  replaced  with  the  mean  of  the  target  variable  for  each  category,  and  instead  constructs  the

encoding  process  using  only  previous  data  to  avoid  data  leakage.  Another  distinguishing  feature  of

CatBoost is its use of symmetric decision trees, where all leaves at the same depth use identical splitting

criteria.  This  structure  not  only  accelerates  training  but  also  significantly  reduces  inference  time,  an

essential advantage in some time-sensitive applications of real-world forecasting.

2.4 Deep Learning Architectures

This section presents an overview of the most prominent Deep Learning (DL) architectures encountered in

the surveyed literature. DL will be used in this paper to describe a subset of machine learning that utilizes

neural networks to perform classification and regression tasks. The architectures are categorized into four

primary  groups:  Feed-Forward  Neural  Networks  (FFNN),  Recurrent  Neural  Networks  (RNN),

Convolutional  Neural  Networks  (CNN),  and  Attention-based  architectures.  Figure  2.2  presents  a  visual

representation of a FFNN, highlighting the architectural modifications required to transform it into a RNN

or CNN.

2.4.1 Feed-Forward Neural Networks

The term Feed-Forward Neural Network (FFNN) is often used interchangeably with other terminologies in

the literature, including Artificial Neural Network (ANN), Neural Network (NN), Multilayer Perceptron

(MLP),  Back  Propagation  Neural  Network  (BPNN)  (Nan  et  al.,  2022;  Pan  et  al.,  2023),  Deep  Neural

Network (DNN), and Deep Feed-Forward Neural Network (DFFNN). These networks are characterized by

 12

Reproduced with permission of copyright owner. Further reproduction prohibited without permission.

