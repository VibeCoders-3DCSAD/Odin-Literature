---
conversion_metadata:
  converted_at: "2026-07-22T13:26:52Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Gong.pdf"
  source_pdf_sha256: "384ab27cec57471d97762194e9ff9a48c44882ecd769b9e38bdf5efec2286592"
  page_count: 8
  markdown_char_count: 56728
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

Research Progress and Trends of Deep Learning 
in  Stock  Price  Prediction:  A  Systematic Review 
from LSTM to Transformer

Hanchen Gong1* 
1SWJTU-Leeds Joint School, Southwest Jiaotong University, 610031, Chengdu, China

Abstract. Stock price prediction is a key issue in quantitative finance. Due 
to the characteristics of the financial market, traditional prediction methods 
often fail to achieve accurate and stable prediction results. In recent years, 
deep learning technology, especially architectures such as Long Short-Term 
Memory (LSTM) and Transformer, have stood out with their excellent and 
stable  performance.  This  paper  systematically  reviews  the  update  and 
iteration  process  of  stock  prediction  methods  and  elaborates  on  the 
classification  of  mainstream  deep 
the 
characteristics,  advantages  and  limitations  of  different  models,  and 
comparing  the  differences  in  data  sets,  indicators  and  performance  in 
empirical  studies.  In  addition,  it  further  discusses  challenges  such  as  data 
noise, overfitting, interpretability and computational efficiency, and thereby 
looks forward to future research directions such as multimodal information 
fusion, interpretable artificial intelligence and real-time adaptive learning. 
This paper aims to provide a complete technical roadmap for researchers in 
the  field  of  stock  price  prediction  to  apply  deep  learning  methods 
systematically.

learning  models,  analysing

1 Introduction

The accuracy of stock price prediction is one of the ultimate goals in modern finance, directly 
determining  the  success  or  failure  of  quantitative  investment  strategies  and  the  effective 
management of downside risks. Stock prices are influenced by various factors such as the 
macroeconomic  environment, 
industry  development  prospects,  company  operating 
conditions, and market participants' sentiments, exhibiting significant characteristics such as 
high volatility,  non-linearity, and non-stationarity, which greatly  increase  the  difficulty of 
predicting  stock  prices.  Therefore,  how  to  construct  a  model  that  combines  accuracy  and 
stability to predict the complex and variable stock market has become the long-term research 
goal for relevant personnel.

Early stock predictions mainly utilized models such as ARIMA and GARCH, which are 
based on linear assumptions and applicable to stationary sequences. However, these models 
have limitations such as difficulty in capturing nonlinear features and sensitivity to noise [1]. 
Subsequently,  machine  learning  techniques  such  as  Support  Vector  Machines  (SVM),

*Corresponding author’s email: cn22h2g@leeds.ac.uk

© The   Authors,  published  by EDP  Sciences.  This  is  an  open  access  article  distributed  under  the  terms  of the Creative
Commons Attribution  License  4.0  (https://creativecommons.org/licenses/by/4.0/).

---

<!-- PAGE 2 -->

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

Random Forests (RF), and eXtreme Gradient Boosting (XGBoost) were widely applied in 
stock  market  predictions.  These  methods  improved  prediction  accuracy  and  had  stronger 
capabilities in capturing nonlinear relationships and extracting data features, but they relied 
on human assumptions and economic theories [2].

At the deep learning stage, based on the Recurrent Neural Network (RNN), optimization 
models such as LSTM and Gated Recurrent Unit (GRU) effectively overcome the problems 
of gradient disappearance and explosion through the gating mechanism, and can capture and 
predict the corresponding short-term dynamic features [1]. The emergence of LSTM is of 
epoch-making  significance,  but  when  dealing  with  sufficiently  long  sequences,  it  still 
inevitably experiences information attenuation, and its sequential processing mechanism also 
leads  to  low  computational  efficiency  and  other  problems.  Another  issue  is  that  LSTM 
models  are  modeled  along  the  time  axis  within  the  same  sequence,  resulting  in  relatively 
weak  modeling  of  cross-sequence  relationships.  This  pain  point  stimulated  and  drove  the 
development and transformation of technology. The Transformer model, due to its success 
in  the  sub-field  of  artificial  intelligence  and  its  excellent  self-attention  mechanism,  was 
eventually introduced into stock prediction. Its emergence successfully solved the bottleneck 
problem of LSTM and brought a new solution to stock prediction. Moreover, researchers are 
no  longer  satisfied  with  using  a  single  model  for  prediction  and  are  committed  to 
complementing the advantages of each model to build a more powerful hybrid model, such 
as LSTM-Transformer, to seek another breakthrough in model performance and prediction 
accuracy.

Although  some  studies  have  achieved  remarkable  results  and  there  are  several  related 
review papers that have explored the application of deep learning in the financial field, there 
is  still  a  lack  of  a  systematic  review  that  specifically  focuses  on  predicting  stock  prices, 
systematically  summarizes  the  development  process  from  LSTM  to  Transformer  hybrid 
architectures,  and  also  takes  into  account  the  analysis  of  model  principles  and  empirical 
comparisons. Therefore, this paper aims to fill this gap: systematically review the evolution 
process  of  stock  prediction  models,  in  detail  analyze  the  specific  characteristics  and 
advantages and disadvantages of mainstream deep learning models, summarize the existing 
research  results  and  compare  the  similarities  and  differences  among  models,  discuss  the 
current problems and future development directions.

2 Overview of Mainstream Technologies

The trend of deep learning models gradually becoming the mainstream in the field of stock 
prediction has been observed. The following content introduces several mainstream models: 
recurrent  models,  convolutional  models,  Transformer-related  models,  hybrid  models,  and 
some extension methods. At the same time, the corresponding characteristics, advantages, 
and disadvantages are elaborated.

2.1 RNN and Its Variants

RNN use a hidden state recurrence mechanism to remember historical information and handle 
the temporal correlation of sequential data. Their improved model, LSTM, introduces forget 
gates, input gates, and output gates, effectively solving the gradient problem of long sequence 
correlations that traditional RNNs have, and has significant advantages in capturing medium 
and  short-term  dependencies.  Moreover,  Fischer  &  Krauss'  research  shows  that  the 
performance of LSTM is significantly better than the memoryless model, so LSTM is widely 
used in financial market predictions [1].

Additionally, GRU achieves similar performance to LSTM with a simpler gating structure 
and  is  also  widely  used.  Rahmadeyan's  research  shows  that  GRU  is  significantly  more

2

---

<!-- PAGE 3 -->

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

efficient in terms of computational efficiency than LSTM, but for different time periods, the 
prediction  accuracy  of  GRU  is  slightly  better  or  worse  than  LSTM  [3].  However, 
LSTM/GRU is limited by the recursive calculation mode and the limited memory window. 
When  facing  issues  such  as  ultra-long  time  spans,  multi-sequence  modelling,  and  market 
state mutations, their performance is still relatively weak.

2.2 Convolutional Neural Network (CNN) and CNN-LSTM Hybrid Model

CNN initially performed well in computer vision. Its local receptive field and hierarchical 
feature  extraction  mechanism  were  later  applied  to  time  series  prediction  tasks,  used  to 
extract  local  trends  and  cycles,  etc.,  of  stock  market  information,  while  filtering  out 
interfering noise. Among them, when the time series is regarded as a one-dimensional image 
(1D image), CNN extracts multi-scale filtering features in a data-driven manner [4]. Then, 
Mehtab and Sen proposed to use CNN as the front-end encoder to read sequence data and 
extract key features, and LSTM as the back-end decoder to decode and predict the sequence, 
complementing the local perception of CNN and the temporal dependency of LSTM, forming 
a CNN-LSTM hybrid architecture for predicting the NIFTY 50 index value [5]. The results 
proved  that  this  hybrid  structure  performed  better  in  multi-step  prediction.  However,  the 
hybrid model inevitably brings problems such as complex structure, many hyperparameters, 
and has defects such as overfitting and being sensitive to abnormal fluctuations and sudden 
changes.

2.3 Transformer and Its Variants

The Transformer architecture was initially applied in Natural Language Processing (NLP), 
and it does not rely on traditional recursion and convolution. It achieves global information 
interaction through a unique self-attention mechanism (Self-Attention). Subsequently, due to 
its strong parallel computing and long-range dependency modelling capabilities, Transformer 
was introduced into time series prediction to leverage its advantages, for capturing long-range 
dependency  features  and  modelling  cross-asset  correlations.  In  recent  years,  many  stock 
prediction  models  based  on  Transformer  have  emerged.  For  example,  the  Stockformer 
architecture for multi-variable time series prediction tasks converts the input variables into a 
single-variable  output  [6].  There  are  also  studies  evaluating  the  performance  of  different 
structured Transformers (only encoder, only decoder, encoder + decoder (standard), standard 
without embedding layer, standard with ProbSparse Attention), and the experimental results 
show  that  the  Transformer  model  with  only  the  decoder  structure  performs  the  best  [7]. 
However, at the same time, Transformer also has the problem of financial sample quantity 
being  small,  which  is  prone  to  overfitting.  Its  self-attention  mechanism  inevitably  brings 
issues such as high computational cost and high existing occupancy, amplifying the impact 
of errors and noise in abnormal situations.

2.4 Hybrid Models and Other Extension Methods

To  mitigate  the  shortcomings of  a  single model,  the  extension of  model  structure  and  the 
mixture of models have been widely discussed.

One type is the direct fusion of LSTM and Transformer, which includes mechanisms such 
as cascading, parallel connection, and plug-and-play attention. Here, LSTM is responsible 
for  local  short-term  information,  while  Transformer  is  responsible  for  global  long-term 
information.  For  example,  Zhang  and  Li  adopted  a  dual-branch  structure  of  LSTM-
Transformer hybrid model to achieve multimodal fusion prediction of price and sentiment 
information, and the prediction accuracy was significantly higher than that of a single model

3

---

<!-- PAGE 4 -->

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

[8]. Another type is based on Transformer, introducing frequency domain decomposition and 
time  encoding  mechanisms  to  simultaneously  capture  the  periodic  and  non-periodic 
components in the time series. For instance, Zhang and Li proposed the CEEMD-Time2Vec-
Transformer  (ETT)  stock  prediction  model,  which  significantly  enhanced  the  prediction 
performance  compared  to other benchmark  deep  learning  models  [9].  Additionally,  graph 
neural networks (GNN) have also been widely discussed. Zhang et al. mentioned the Chart 
GCN, which converts sequence important nodes into graphs and uses GNN to compare their 
similarities [10]. There is also the Attribute-Driven Graph Attention Network (AD-GAT), 
which makes predictions through momentum overflow. Stock prediction models are being 
optimized  with  the  aims  of  cross-model  fusion,  multimodal  fusion,  and  interpretability  to 
significantly improve the model's usability.

3 Applications and Empirical Research

3.1 Dataset and Sample Description

At the data source level, commonly used datasets include national or regional stock market 
indices (such as the S&P 500 in the United States, NIFTY 50 in India, and the Moroccan 
Stock Exchange Index), industry sector indices (such as technology, energy, and finance), 
and multi-asset portfolio or individual stock sample data. In terms of time scale, daily data 
(daily data) is often used for medium and long-term trend prediction due to its lower noise 
and stable trend. Lahebb and Benaly compared the use of ARIMA, LSTM, and Transformer 
models to analyse the daily data of three well-known credit companies in Morocco and made 
short-term investment decisions [11]. In contrast, minute-level or high-frequency data (high-
frequency  data)  can  reveal  market  microstructure  and  is  often  used  to  analyse  short-term 
market dynamics, imbalance in order flow, and price shock mechanisms. Zhang et al. used 
Limit Order Book (LOB) data and developed a convolutional filter-LSTM model to explore 
the price dynamics under the microstructure [12].

In  recent  years,  data  structures  have  been  continuously  improved  and  are  gradually 
evolving  towards  multi-dimensional  and  multi-modal  directions.  At  the  same  time,  in 
addition to traditional sequences such as prices and trading volumes, researchers have begun 
to introduce exogenous features such as sentiment variables, macroeconomic and technical 
indicators to enhance the interpretability and generalization ability of the models.

3.2 Relevant Evaluation Criteria

In  the  review  by  Saberironaghi  et  al.,  four  categories  including  overall,  classification, 
regression, and profitability were mentioned, along with a total of 12 evaluation indicators 
[13].  This  comprehensive  and  in-depth  assessment  of  the deep  learning model  ensures  its 
usability and the accuracy of the prediction results. Depending on different research goals, 
researchers typically use the following indicators to evaluate the relevant performance of the 
deep learning model:

• Root Mean Squared Error (RMSE): Reflects the overall deviation between the model's 
predicted values and the actual values. The smaller the value, the better the fitting effect, and 
it is more sensitive to large deviations.

• Mean Absolute Error (MAE): Is the average deviation between the model's predicted

values and the actual values, reflecting the stability of the model's prediction.

•Mean Absolute Percentage Error (MAPE): Is the average percentage error between the

model's predicted values and the actual values.

4

---

<!-- PAGE 5 -->

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

•  Directional  Accuracy  (DA):  Reflects  the  accuracy  of  the  model  in  predicting  the 
direction of stock price changes, directly corresponding to the actual usability of the model 
in investment decisions.

• 𝑅2/ Adjusted 𝑅2: Indicates the model's ability to explain the variation of independent 
variables, also reflecting the fitting degree of the model, but only as a descriptive indicator. 
• Sharpe Ratio: Reflects the relationship between returns and risks. The higher the value,

the higher the return under the given risk.

3.3 Empirical Results Comparison and Trends

Based on multiple empirical studies, deep learning models outperform traditional machine 
learning and statistical methods in stock price prediction.

The LSTM model and its variants have been extensively proven to be reliable benchmark 
models, especially for medium and short-term prediction tasks. In a study by Fischer and 
Krauss  on  the  prediction  of  all  S&P  500  index  constituents  from  1992  to  2015,  the  daily 
return rate of LSTM was 0.46%, significantly higher than the standard DNN at 0.32% and 
logistic regression at 0.26%, among other non-memory classification methods [1]. Moreover, 
LSTM has a significant advantage in generating trading signals with direct economic value, 
with a Sharpe ratio of up to 2.34, while most other control methods are far less than 1.0 [1]. 
Subsequently, the Transformer model was further optimized based on LSTM, especially in 
long sequences, demonstrating the superiority of the self-attention mechanism in long-range 
dependencies  and  cross-asset  correlations.  Wang  et  al.  predicted  the  stock  prices  of  new 
energy vehicle enterprises and mentioned that the Transformer model has better prediction 
accuracy  compared  to  CNN,  RNN,  and  LSTM  traditional  deep  learning  models,  with  an 
average MAE decrease of approximately 20.73%, MSE decrease of approximately 34.84%, 
and MAPE decrease of approximately 25.63%, all demonstrating smaller errors and better fit 
[14].  However,  in  small  sample  scenarios,  LSTM  has  stronger  stability  due  to  its  simple 
model  architecture.  Nevertheless,  the  hybrid  model  LSTM-Transformer  has  become  the 
focus of research. Many research results show that by integrating the local dynamic capture 
of LSTM and the global dependency modelling of Transformer, it achieves comprehensive 
optimization based on the parent model. Zhao et al. mentioned that the MAE, RMSE, etc. 
indicators of the LSTM-Transformer hybrid model are reduced by more than 50% compared 
to LSTM and Transformer models, indicating lower errors and more stable models [15]. At 
the same time, the R² value of the hybrid architecture (0.9618) is higher than that of the parent 
model (LSTM: 0.8430; Transformer: 0.7763), representing stronger explanatory power [15]. 
From the overall trend, LSTM has a significant advantage in direction determination and 
generating  trading  signals  with  high  Sharpe  ratios,  while  the  Transformer  model  further 
improves  prediction  accuracy;  the  LSTM-Transformer  hybrid  architecture  simultaneously 
has  stronger  interpretability  based  on  higher  accuracy  and  stability.  In  summary,  stock 
prediction models have evolved in recent years from LSTM → CNN-LSTM → Transformer 
→ hybrid model → multimodal fusion model, with increasing complexity of architectures 
and  fusion  dimensions,  reflecting  the  design  paradigm  from  single  model  optimization  to 
collaborative integration.

4 Discussion and Outlook

Although deep learning models have made significant progress and breakthroughs in stock 
price  prediction  in  recent  years,  there  are  still  many  challenges  and  difficulties  between 
theoretical  knowledge  research  and  the  application  of  actual  models.  The  following  will

5

---

<!-- PAGE 6 -->

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

analyze the current problems from three levels: data, model, and deployment application, and 
propose future development trends and research directions.

4.1 Current Challenges

4.1.1 Data Level

Firstly, financial market data has extremely low signal-to-noise ratio and jump characteristics, 
which causes the model to easily overfit historical noise rather than learning the patterns of 
stock  price  fluctuations;  Secondly,  changes  in  macroeconomic  policies  and  black  swan 
events  can  lead  to  a  significant  decline  in  the  generalization  ability  of  models  based  on 
historical data in new environments; At the same time, problems such as the lag of up and 
down  labels  and  the  unidirectional  data  in  volatile  markets  pose  challenges  to  supervised 
learning;  Moreover,  continuous  bull  or  bear  markets  can  lead  to  unequal  sample  sizes, 
causing the prediction to be biased towards the majority category, and the data learned by the 
model usually does not include vanished companies, and the beautified data can also affect 
the prediction accuracy; Finally, how to deeply integrate diverse information such as news, 
social  media,  financial  reports,  and  macroeconomics  is  the  key  to  breaking  through  the 
performance bottleneck of existing models.

4.1.2 Model Level

Firstly,  the  "black  box"  nature  of  deep  models  makes  it  impossible  to  provide  the 
corresponding  basis  for  making  judgments,  although  post-event  explanation  techniques 
(attention weight visualization, SHAP values, LIME) are attempting to solve this problem, 
there  is  still  a  lack  of  a  unified  solution;  Secondly,  the  available  samples  for  financial 
prediction (N) are very few, but the models have a large number of parameters (P), this "N 
<< P" situation allows the model to have sufficient space to memorize the noise and specific 
patterns  in  the  training  data;  Moreover,  the  self-attention  mechanism  of  the  Transformer 
architecture associates elements in the sequence pairwise, and the huge computational load 
and  memory  usage  in  long  sequences  can  cause  some  delays,  affecting  efficiency; 
Additionally,  the  design  of  hybrid  models  lacks  theoretical  basis  guidance,  and  their 
performance improvement is mostly based on researchers' intuition and continuous trial and 
error, which is extremely costly and difficult to reproduce; Finally, existing models mostly 
follow the principle of offline training and static prediction, which is contrary to the dynamic 
changes of the financial market, resulting in the gradual decline of model performance over 
time.

4.1.3 Deployment and Application Level

Firstly, in scenarios such as high-frequency trading and decision implementation, there are 
extremely strict requirements for model running speed, and deep models often cannot meet 
these requirements; Secondly, if a financial crisis, epidemic, or other emergencies occur, the 
general  patterns  learned  by  the  model  instantly  become  invalid,  and  the  prediction 
performance drops significantly; Moreover, a single prediction model cannot directly create 
profits, and a complete closed loop of prediction-decision-execution-risk control is needed to 
exert its value; Finally, the "black box" characteristics of deep models and the transparency, 
explainability, fairness, bias control, and stability requirements of regulatory authorities are 
contradictory, which is not conducive to their development.

6

---

<!-- PAGE 7 -->

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

4.2 Future Trends and Research Directions

Looking forward, first, it is not limited to simple feature concatenation. By integrating diverse 
information on the Transformer architecture to build a large model in the financial field that 
can associate cross-modal information; Then, integrate the causal inference framework with 
deep learning to enable the model to complete the transformation from "black box" prediction 
to "glass box" diagnosis, to strengthen the credibility of the model's prediction results; At the 
same time, add AutoML and NAS technologies to enable the model to achieve automated 
search and automatically adjust the model architecture according to the current market regime, 
to adapt to increasingly complex hybrid models and massive hyperparameters; Furthermore, 
the design enables real-time learning from the data stream without the need for re-training, 
and can quickly adapt to new environments, optimizing parameters rapidly using only a small 
number of samples, thus enabling the model to have the ability for continuous learning; on 
this basis, introducing RL agents for decision-making, and the deep model to play the role of 
perceiving  the  environment,  forming  a  complete  closed  loop  from  market  perception  to 
investment decision-making, achieving the transformation from assisting human decision-
making to autonomous agent-driven; further, introducing Linear Transformer, Performer and 
other linear attention mechanisms, while exploring S4, Mamba and other state space models, 
fundamentally changing the computational paradigm of Transformer to solve the bottleneck 
of  low  efficiency  in  processing  long  sequences;  finally,  using  transfer  learning  and  meta-
learning techniques, transferring the knowledge and patterns learned by the model in a certain 
market environment to a completely new market with less historical data, to quickly obtain a 
highly performing predictive model.

5 Conclusion

With  the  continuous  development  of  the  field  of  deep  learning,  research  on  stock  price 
prediction based on LSTM, Transformer and their hybrid models has achieved significant 
results.  This  paper  systematically  reviews  the  model  development  process  from  RNN  to 
hybrid  Transformer  architectures,  analyzes  in  detail  their  principles,  advantages  and 
disadvantages,  and  application  scenarios,  and  collates  many  empirical  studies,  comparing 
their  performance  on  different  datasets  and  evaluation  metrics.  Finally,  this  paper  also 
discusses the current problems faced by the technology and future research directions.

Overall, LSTM has advantages in short-term prediction, while Transformer dominates in 
long-term dependence and cross-asset modeling. Hybrid models and multimodal fusion have 
become an inevitable development trend. Future research should focus on breakthroughs in 
interpretability,  real-time  performance  and adaptive  learning,  to  achieve  a  perfect  balance 
between accuracy, efficiency and robustness.

References

1.  T. Fischer, C. Krauss. Deep learning with long short-term memory networks for

financial market predictions. European Journal of Operational Research, 270(2): 654-
669 (2018)

2.  M. M. Kumbure C. Lohrmann, P. Luukka, et al. A systematic review of machine 
learning techniques in stock price prediction: The role of feature selection and 
preprocessing. Expert Systems with Applications, 200: 116966 (2022)

3.  S. Rahmadeyan, A. Maleki. A comparative analysis of GRU and LSTM networks for

sequential data forecasting. Procedia Computer Science, 237: 115-122 (2024)

7

---

<!-- PAGE 8 -->

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

4.  S. Kiranyaz, O. Avci, O. Abdeljaber, et al. 1D convolutional neural networks and 
applications: A survey. Mechanical Systems and Signal Processing, 151: 107398 
(2021)

5.  S. Mehtab, J. Sen. A CNN-LSTM hybrid model for stock market prediction using

multiple sources of data. In Proceedings of the 2021 IEEE International Conference on 
Big Data, 2311-2320 (2021)

6.  S. Li, Z. B. Schulwolf, R. Miikkulainen. Transformer-based time-series forecasting for

stock prediction. arXiv preprint arXiv:2305.10424, (2023)

7.  Q. Chen. Comparing different Transformer model structures for stock prediction. arXiv

preprint arXiv:2404.16361, (2024)

8.  W. Zhang, Y. Li. A dual-branch LSTM–Transformer framework for multi-modal stock

forecasting based on price and sentiment information. Journal of Economic Analysis, 
4(3): 109-125 (2023)

9.  Y. Zhang, T. Li. CEEMD-Time2Vec-Transformer: A novel hybrid model for financial

time series forecasting. EPJ Data Science, 13(1): 28 (2024)

10.  X. Zhang, Y. Wang, Z. Liu. Chart GCN: A graph convolutional network approach for

stock movement prediction. Procedia Computer Science, 214: 258-265 (2022)

11.  B. Lahebb, M. Benaly. Comparative study of ARIMA, LSTM and Transformer models 
for stock price forecasting: Evidence from Moroccan stock market. Journal of Risk and 
Financial Management, 17(7): 293 (2024)

12.  Z. Zhang, S. Zohren, S. Roberts. DeepLOB: Deep convolutional neural networks for

limit order books. IEEE Transactions on Signal Processing, 67(11): 3001-3012 (2019) 
13.  A. Saberironaghi, J. Ren, M. El-Gindy. Evaluation metrics for deep learning models in

stock prediction: A comprehensive survey. AppliedMath, 5(3): 76-95 (2025) 
14.  C. Wang, Y. Chen, S. Zhang, et al. Stock market index prediction using deep 
Transformer model. Expert Systems with Applications, 208: 118125 (2022)

15.  K. Zhao, X. Li, M. Yang. A novel LSTM–Transformer hybrid model for stock price 
prediction: Evidence from Chinese stock market. Mathematics, 13(10): 1551 (2025)

8

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

Research Progress and Trends of Deep Learning
in  Stock  Price  Prediction:  A  Systematic Review
from LSTM to Transformer

Hanchen Gong1*
1SWJTU-Leeds Joint School, Southwest Jiaotong University, 610031, Chengdu, China

Abstract. Stock price prediction is a key issue in quantitative finance. Due
to the characteristics of the financial market, traditional prediction methods
often fail to achieve accurate and stable prediction results. In recent years,
deep learning technology, especially architectures such as Long Short-Term
Memory (LSTM) and Transformer, have stood out with their excellent and
stable  performance.  This  paper  systematically  reviews  the  update  and
iteration  process  of  stock  prediction  methods  and  elaborates  on  the
classification  of  mainstream  deep
the
characteristics,  advantages  and  limitations  of  different  models,  and
comparing  the  differences  in  data  sets,  indicators  and  performance  in
empirical  studies.  In  addition,  it  further  discusses  challenges  such  as  data
noise, overfitting, interpretability and computational efficiency, and thereby
looks forward to future research directions such as multimodal information
fusion, interpretable artificial intelligence and real-time adaptive learning.
This paper aims to provide a complete technical roadmap for researchers in
the  field  of  stock  price  prediction  to  apply  deep  learning  methods
systematically.

learning  models,  analysing

1 Introduction

The accuracy of stock price prediction is one of the ultimate goals in modern finance, directly
determining  the  success  or  failure  of  quantitative  investment  strategies  and  the  effective
management of downside risks. Stock prices are influenced by various factors such as the
macroeconomic  environment,
industry  development  prospects,  company  operating
conditions, and market participants' sentiments, exhibiting significant characteristics such as
high volatility,  non-linearity, and non-stationarity, which greatly  increase  the  difficulty of
predicting  stock  prices.  Therefore,  how  to  construct  a  model  that  combines  accuracy  and
stability to predict the complex and variable stock market has become the long-term research
goal for relevant personnel.

Early stock predictions mainly utilized models such as ARIMA and GARCH, which are
based on linear assumptions and applicable to stationary sequences. However, these models
have limitations such as difficulty in capturing nonlinear features and sensitivity to noise [1].
Subsequently,  machine  learning  techniques  such  as  Support  Vector  Machines  (SVM),

*Corresponding author’s email: cn22h2g@leeds.ac.uk

 © The   Authors,  published  by EDP  Sciences.  This  is  an  open  access  article  distributed  under  the  terms  of the Creative
Commons Attribution  License  4.0  (https://creativecommons.org/licenses/by/4.0/).

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

Random Forests (RF), and eXtreme Gradient Boosting (XGBoost) were widely applied in
stock  market  predictions.  These  methods  improved  prediction  accuracy  and  had  stronger
capabilities in capturing nonlinear relationships and extracting data features, but they relied
on human assumptions and economic theories [2].

At the deep learning stage, based on the Recurrent Neural Network (RNN), optimization
models such as LSTM and Gated Recurrent Unit (GRU) effectively overcome the problems
of gradient disappearance and explosion through the gating mechanism, and can capture and
predict the corresponding short-term dynamic features [1]. The emergence of LSTM is of
epoch-making  significance,  but  when  dealing  with  sufficiently  long  sequences,  it  still
inevitably experiences information attenuation, and its sequential processing mechanism also
leads  to  low  computational  efficiency  and  other  problems.  Another  issue  is  that  LSTM
models  are  modeled  along  the  time  axis  within  the  same  sequence,  resulting  in  relatively
weak  modeling  of  cross-sequence  relationships.  This  pain  point  stimulated  and  drove  the
development and transformation of technology. The Transformer model, due to its success
in  the  sub-field  of  artificial  intelligence  and  its  excellent  self-attention  mechanism,  was
eventually introduced into stock prediction. Its emergence successfully solved the bottleneck
problem of LSTM and brought a new solution to stock prediction. Moreover, researchers are
no  longer  satisfied  with  using  a  single  model  for  prediction  and  are  committed  to
complementing the advantages of each model to build a more powerful hybrid model, such
as LSTM-Transformer, to seek another breakthrough in model performance and prediction
accuracy.

Although  some  studies  have  achieved  remarkable  results  and  there  are  several  related
review papers that have explored the application of deep learning in the financial field, there
is  still  a  lack  of  a  systematic  review  that  specifically  focuses  on  predicting  stock  prices,
systematically  summarizes  the  development  process  from  LSTM  to  Transformer  hybrid
architectures,  and  also  takes  into  account  the  analysis  of  model  principles  and  empirical
comparisons. Therefore, this paper aims to fill this gap: systematically review the evolution
process  of  stock  prediction  models,  in  detail  analyze  the  specific  characteristics  and
advantages and disadvantages of mainstream deep learning models, summarize the existing
research  results  and  compare  the  similarities  and  differences  among  models,  discuss  the
current problems and future development directions.

2 Overview of Mainstream Technologies

The trend of deep learning models gradually becoming the mainstream in the field of stock
prediction has been observed. The following content introduces several mainstream models:
recurrent  models,  convolutional  models,  Transformer-related  models,  hybrid  models,  and
some extension methods. At the same time, the corresponding characteristics, advantages,
and disadvantages are elaborated.

2.1 RNN and Its Variants

RNN use a hidden state recurrence mechanism to remember historical information and handle
the temporal correlation of sequential data. Their improved model, LSTM, introduces forget
gates, input gates, and output gates, effectively solving the gradient problem of long sequence
correlations that traditional RNNs have, and has significant advantages in capturing medium
and  short-term  dependencies.  Moreover,  Fischer  &  Krauss'  research  shows  that  the
performance of LSTM is significantly better than the memoryless model, so LSTM is widely
used in financial market predictions [1].

Additionally, GRU achieves similar performance to LSTM with a simpler gating structure
and  is  also  widely  used.  Rahmadeyan's  research  shows  that  GRU  is  significantly  more

2

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

efficient in terms of computational efficiency than LSTM, but for different time periods, the
prediction  accuracy  of  GRU  is  slightly  better  or  worse  than  LSTM  [3].  However,
LSTM/GRU is limited by the recursive calculation mode and the limited memory window.
When  facing  issues  such  as  ultra-long  time  spans,  multi-sequence  modelling,  and  market
state mutations, their performance is still relatively weak.

2.2 Convolutional Neural Network (CNN) and CNN-LSTM Hybrid Model

CNN initially performed well in computer vision. Its local receptive field and hierarchical
feature  extraction  mechanism  were  later  applied  to  time  series  prediction  tasks,  used  to
extract  local  trends  and  cycles,  etc.,  of  stock  market  information,  while  filtering  out
interfering noise. Among them, when the time series is regarded as a one-dimensional image
(1D image), CNN extracts multi-scale filtering features in a data-driven manner [4]. Then,
Mehtab and Sen proposed to use CNN as the front-end encoder to read sequence data and
extract key features, and LSTM as the back-end decoder to decode and predict the sequence,
complementing the local perception of CNN and the temporal dependency of LSTM, forming
a CNN-LSTM hybrid architecture for predicting the NIFTY 50 index value [5]. The results
proved  that  this  hybrid  structure  performed  better  in  multi-step  prediction.  However,  the
hybrid model inevitably brings problems such as complex structure, many hyperparameters,
and has defects such as overfitting and being sensitive to abnormal fluctuations and sudden
changes.

2.3 Transformer and Its Variants

The Transformer architecture was initially applied in Natural Language Processing (NLP),
and it does not rely on traditional recursion and convolution. It achieves global information
interaction through a unique self-attention mechanism (Self-Attention). Subsequently, due to
its strong parallel computing and long-range dependency modelling capabilities, Transformer
was introduced into time series prediction to leverage its advantages, for capturing long-range
dependency  features  and  modelling  cross-asset  correlations.  In  recent  years,  many  stock
prediction  models  based  on  Transformer  have  emerged.  For  example,  the  Stockformer
architecture for multi-variable time series prediction tasks converts the input variables into a
single-variable  output  [6].  There  are  also  studies  evaluating  the  performance  of  different
structured Transformers (only encoder, only decoder, encoder + decoder (standard), standard
without embedding layer, standard with ProbSparse Attention), and the experimental results
show  that  the  Transformer  model  with  only  the  decoder  structure  performs  the  best  [7].
However, at the same time, Transformer also has the problem of financial sample quantity
being  small,  which  is  prone  to  overfitting.  Its  self-attention  mechanism  inevitably  brings
issues such as high computational cost and high existing occupancy, amplifying the impact
of errors and noise in abnormal situations.

2.4 Hybrid Models and Other Extension Methods

To  mitigate  the  shortcomings of  a  single model,  the  extension of  model  structure  and  the
mixture of models have been widely discussed.

One type is the direct fusion of LSTM and Transformer, which includes mechanisms such
as cascading, parallel connection, and plug-and-play attention. Here, LSTM is responsible
for  local  short-term  information,  while  Transformer  is  responsible  for  global  long-term
information.  For  example,  Zhang  and  Li  adopted  a  dual-branch  structure  of  LSTM-
Transformer hybrid model to achieve multimodal fusion prediction of price and sentiment
information, and the prediction accuracy was significantly higher than that of a single model

3

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

[8]. Another type is based on Transformer, introducing frequency domain decomposition and
time  encoding  mechanisms  to  simultaneously  capture  the  periodic  and  non-periodic
components in the time series. For instance, Zhang and Li proposed the CEEMD-Time2Vec-
Transformer  (ETT)  stock  prediction  model,  which  significantly  enhanced  the  prediction
performance  compared  to other benchmark  deep  learning  models  [9].  Additionally,  graph
neural networks (GNN) have also been widely discussed. Zhang et al. mentioned the Chart
GCN, which converts sequence important nodes into graphs and uses GNN to compare their
similarities [10]. There is also the Attribute-Driven Graph Attention Network (AD-GAT),
which makes predictions through momentum overflow. Stock prediction models are being
optimized  with  the  aims  of  cross-model  fusion,  multimodal  fusion,  and  interpretability  to
significantly improve the model's usability.

3 Applications and Empirical Research

3.1 Dataset and Sample Description

At the data source level, commonly used datasets include national or regional stock market
indices (such as the S&P 500 in the United States, NIFTY 50 in India, and the Moroccan
Stock Exchange Index), industry sector indices (such as technology, energy, and finance),
and multi-asset portfolio or individual stock sample data. In terms of time scale, daily data
(daily data) is often used for medium and long-term trend prediction due to its lower noise
and stable trend. Lahebb and Benaly compared the use of ARIMA, LSTM, and Transformer
models to analyse the daily data of three well-known credit companies in Morocco and made
short-term investment decisions [11]. In contrast, minute-level or high-frequency data (high-
frequency  data)  can  reveal  market  microstructure  and  is  often  used  to  analyse  short-term
market dynamics, imbalance in order flow, and price shock mechanisms. Zhang et al. used
Limit Order Book (LOB) data and developed a convolutional filter-LSTM model to explore
the price dynamics under the microstructure [12].

In  recent  years,  data  structures  have  been  continuously  improved  and  are  gradually
evolving  towards  multi-dimensional  and  multi-modal  directions.  At  the  same  time,  in
addition to traditional sequences such as prices and trading volumes, researchers have begun
to introduce exogenous features such as sentiment variables, macroeconomic and technical
indicators to enhance the interpretability and generalization ability of the models.

3.2 Relevant Evaluation Criteria

In  the  review  by  Saberironaghi  et  al.,  four  categories  including  overall,  classification,
regression, and profitability were mentioned, along with a total of 12 evaluation indicators
[13].  This  comprehensive  and  in-depth  assessment  of  the deep  learning model  ensures  its
usability and the accuracy of the prediction results. Depending on different research goals,
researchers typically use the following indicators to evaluate the relevant performance of the
deep learning model:

• Root Mean Squared Error (RMSE): Reflects the overall deviation between the model's
predicted values and the actual values. The smaller the value, the better the fitting effect, and
it is more sensitive to large deviations.

• Mean Absolute Error (MAE): Is the average deviation between the model's predicted

values and the actual values, reflecting the stability of the model's prediction.

•Mean Absolute Percentage Error (MAPE): Is the average percentage error between the

model's predicted values and the actual values.

4

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

•  Directional  Accuracy  (DA):  Reflects  the  accuracy  of  the  model  in  predicting  the
direction of stock price changes, directly corresponding to the actual usability of the model
in investment decisions.

• 𝑅2/ Adjusted 𝑅2: Indicates the model's ability to explain the variation of independent
variables, also reflecting the fitting degree of the model, but only as a descriptive indicator.
• Sharpe Ratio: Reflects the relationship between returns and risks. The higher the value,

the higher the return under the given risk.

3.3 Empirical Results Comparison and Trends

Based on multiple empirical studies, deep learning models outperform traditional machine
learning and statistical methods in stock price prediction.

The LSTM model and its variants have been extensively proven to be reliable benchmark
models, especially for medium and short-term prediction tasks. In a study by Fischer and
Krauss  on  the  prediction  of  all  S&P  500  index  constituents  from  1992  to  2015,  the  daily
return rate of LSTM was 0.46%, significantly higher than the standard DNN at 0.32% and
logistic regression at 0.26%, among other non-memory classification methods [1]. Moreover,
LSTM has a significant advantage in generating trading signals with direct economic value,
with a Sharpe ratio of up to 2.34, while most other control methods are far less than 1.0 [1].
Subsequently, the Transformer model was further optimized based on LSTM, especially in
long sequences, demonstrating the superiority of the self-attention mechanism in long-range
dependencies  and  cross-asset  correlations.  Wang  et  al.  predicted  the  stock  prices  of  new
energy vehicle enterprises and mentioned that the Transformer model has better prediction
accuracy  compared  to  CNN,  RNN,  and  LSTM  traditional  deep  learning  models,  with  an
average MAE decrease of approximately 20.73%, MSE decrease of approximately 34.84%,
and MAPE decrease of approximately 25.63%, all demonstrating smaller errors and better fit
[14].  However,  in  small  sample  scenarios,  LSTM  has  stronger  stability  due  to  its  simple
model  architecture.  Nevertheless,  the  hybrid  model  LSTM-Transformer  has  become  the
focus of research. Many research results show that by integrating the local dynamic capture
of LSTM and the global dependency modelling of Transformer, it achieves comprehensive
optimization based on the parent model. Zhao et al. mentioned that the MAE, RMSE, etc.
indicators of the LSTM-Transformer hybrid model are reduced by more than 50% compared
to LSTM and Transformer models, indicating lower errors and more stable models [15]. At
the same time, the R² value of the hybrid architecture (0.9618) is higher than that of the parent
model (LSTM: 0.8430; Transformer: 0.7763), representing stronger explanatory power [15].
From the overall trend, LSTM has a significant advantage in direction determination and
generating  trading  signals  with  high  Sharpe  ratios,  while  the  Transformer  model  further
improves  prediction  accuracy;  the  LSTM-Transformer  hybrid  architecture  simultaneously
has  stronger  interpretability  based  on  higher  accuracy  and  stability.  In  summary,  stock
prediction models have evolved in recent years from LSTM → CNN-LSTM → Transformer
→ hybrid model → multimodal fusion model, with increasing complexity of architectures
and  fusion  dimensions,  reflecting  the  design  paradigm  from  single  model  optimization  to
collaborative integration.

4 Discussion and Outlook

Although deep learning models have made significant progress and breakthroughs in stock
price  prediction  in  recent  years,  there  are  still  many  challenges  and  difficulties  between
theoretical  knowledge  research  and  the  application  of  actual  models.  The  following  will

5

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

analyze the current problems from three levels: data, model, and deployment application, and
propose future development trends and research directions.

4.1 Current Challenges

4.1.1 Data Level

Firstly, financial market data has extremely low signal-to-noise ratio and jump characteristics,
which causes the model to easily overfit historical noise rather than learning the patterns of
stock  price  fluctuations;  Secondly,  changes  in  macroeconomic  policies  and  black  swan
events  can  lead  to  a  significant  decline  in  the  generalization  ability  of  models  based  on
historical data in new environments; At the same time, problems such as the lag of up and
down  labels  and  the  unidirectional  data  in  volatile  markets  pose  challenges  to  supervised
learning;  Moreover,  continuous  bull  or  bear  markets  can  lead  to  unequal  sample  sizes,
causing the prediction to be biased towards the majority category, and the data learned by the
model usually does not include vanished companies, and the beautified data can also affect
the prediction accuracy; Finally, how to deeply integrate diverse information such as news,
social  media,  financial  reports,  and  macroeconomics  is  the  key  to  breaking  through  the
performance bottleneck of existing models.

4.1.2 Model Level

Firstly,  the  "black  box"  nature  of  deep  models  makes  it  impossible  to  provide  the
corresponding  basis  for  making  judgments,  although  post-event  explanation  techniques
(attention weight visualization, SHAP values, LIME) are attempting to solve this problem,
there  is  still  a  lack  of  a  unified  solution;  Secondly,  the  available  samples  for  financial
prediction (N) are very few, but the models have a large number of parameters (P), this "N
<< P" situation allows the model to have sufficient space to memorize the noise and specific
patterns  in  the  training  data;  Moreover,  the  self-attention  mechanism  of  the  Transformer
architecture associates elements in the sequence pairwise, and the huge computational load
and  memory  usage  in  long  sequences  can  cause  some  delays,  affecting  efficiency;
Additionally,  the  design  of  hybrid  models  lacks  theoretical  basis  guidance,  and  their
performance improvement is mostly based on researchers' intuition and continuous trial and
error, which is extremely costly and difficult to reproduce; Finally, existing models mostly
follow the principle of offline training and static prediction, which is contrary to the dynamic
changes of the financial market, resulting in the gradual decline of model performance over
time.

4.1.3 Deployment and Application Level

Firstly, in scenarios such as high-frequency trading and decision implementation, there are
extremely strict requirements for model running speed, and deep models often cannot meet
these requirements; Secondly, if a financial crisis, epidemic, or other emergencies occur, the
general  patterns  learned  by  the  model  instantly  become  invalid,  and  the  prediction
performance drops significantly; Moreover, a single prediction model cannot directly create
profits, and a complete closed loop of prediction-decision-execution-risk control is needed to
exert its value; Finally, the "black box" characteristics of deep models and the transparency,
explainability, fairness, bias control, and stability requirements of regulatory authorities are
contradictory, which is not conducive to their development.

6

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

4.2 Future Trends and Research Directions

Looking forward, first, it is not limited to simple feature concatenation. By integrating diverse
information on the Transformer architecture to build a large model in the financial field that
can associate cross-modal information; Then, integrate the causal inference framework with
deep learning to enable the model to complete the transformation from "black box" prediction
to "glass box" diagnosis, to strengthen the credibility of the model's prediction results; At the
same time, add AutoML and NAS technologies to enable the model to achieve automated
search and automatically adjust the model architecture according to the current market regime,
to adapt to increasingly complex hybrid models and massive hyperparameters; Furthermore,
the design enables real-time learning from the data stream without the need for re-training,
and can quickly adapt to new environments, optimizing parameters rapidly using only a small
number of samples, thus enabling the model to have the ability for continuous learning; on
this basis, introducing RL agents for decision-making, and the deep model to play the role of
perceiving  the  environment,  forming  a  complete  closed  loop  from  market  perception  to
investment decision-making, achieving the transformation from assisting human decision-
making to autonomous agent-driven; further, introducing Linear Transformer, Performer and
other linear attention mechanisms, while exploring S4, Mamba and other state space models,
fundamentally changing the computational paradigm of Transformer to solve the bottleneck
of  low  efficiency  in  processing  long  sequences;  finally,  using  transfer  learning  and  meta-
learning techniques, transferring the knowledge and patterns learned by the model in a certain
market environment to a completely new market with less historical data, to quickly obtain a
highly performing predictive model.

5 Conclusion

With  the  continuous  development  of  the  field  of  deep  learning,  research  on  stock  price
prediction based on LSTM, Transformer and their hybrid models has achieved significant
results.  This  paper  systematically  reviews  the  model  development  process  from  RNN  to
hybrid  Transformer  architectures,  analyzes  in  detail  their  principles,  advantages  and
disadvantages,  and  application  scenarios,  and  collates  many  empirical  studies,  comparing
their  performance  on  different  datasets  and  evaluation  metrics.  Finally,  this  paper  also
discusses the current problems faced by the technology and future research directions.

Overall, LSTM has advantages in short-term prediction, while Transformer dominates in
long-term dependence and cross-asset modeling. Hybrid models and multimodal fusion have
become an inevitable development trend. Future research should focus on breakthroughs in
interpretability,  real-time  performance  and adaptive  learning,  to  achieve  a  perfect  balance
between accuracy, efficiency and robustness.

References

1.  T. Fischer, C. Krauss. Deep learning with long short-term memory networks for

financial market predictions. European Journal of Operational Research, 270(2): 654-
669 (2018)

2.  M. M. Kumbure C. Lohrmann, P. Luukka, et al. A systematic review of machine
learning techniques in stock price prediction: The role of feature selection and
preprocessing. Expert Systems with Applications, 200: 116966 (2022)

3.  S. Rahmadeyan, A. Maleki. A comparative analysis of GRU and LSTM networks for

sequential data forecasting. Procedia Computer Science, 237: 115-122 (2024)

7

ITM Web of  Conferences 84, 02004 (2026)
ATCIDS 2026

https://doi.org/10.1051/itmconf/20268402004

4.  S. Kiranyaz, O. Avci, O. Abdeljaber, et al. 1D convolutional neural networks and
applications: A survey. Mechanical Systems and Signal Processing, 151: 107398
(2021)

5.  S. Mehtab, J. Sen. A CNN-LSTM hybrid model for stock market prediction using

multiple sources of data. In Proceedings of the 2021 IEEE International Conference on
Big Data, 2311-2320 (2021)

6.  S. Li, Z. B. Schulwolf, R. Miikkulainen. Transformer-based time-series forecasting for

stock prediction. arXiv preprint arXiv:2305.10424, (2023)

7.  Q. Chen. Comparing different Transformer model structures for stock prediction. arXiv

preprint arXiv:2404.16361, (2024)

8.  W. Zhang, Y. Li. A dual-branch LSTM–Transformer framework for multi-modal stock

forecasting based on price and sentiment information. Journal of Economic Analysis,
4(3): 109-125 (2023)

9.  Y. Zhang, T. Li. CEEMD-Time2Vec-Transformer: A novel hybrid model for financial

time series forecasting. EPJ Data Science, 13(1): 28 (2024)

10.  X. Zhang, Y. Wang, Z. Liu. Chart GCN: A graph convolutional network approach for

stock movement prediction. Procedia Computer Science, 214: 258-265 (2022)

11.  B. Lahebb, M. Benaly. Comparative study of ARIMA, LSTM and Transformer models
for stock price forecasting: Evidence from Moroccan stock market. Journal of Risk and
Financial Management, 17(7): 293 (2024)

12.  Z. Zhang, S. Zohren, S. Roberts. DeepLOB: Deep convolutional neural networks for

limit order books. IEEE Transactions on Signal Processing, 67(11): 3001-3012 (2019)
13.  A. Saberironaghi, J. Ren, M. El-Gindy. Evaluation metrics for deep learning models in

stock prediction: A comprehensive survey. AppliedMath, 5(3): 76-95 (2025)
14.  C. Wang, Y. Chen, S. Zhang, et al. Stock market index prediction using deep
Transformer model. Expert Systems with Applications, 208: 118125 (2022)

15.  K. Zhao, X. Li, M. Yang. A novel LSTM–Transformer hybrid model for stock price
prediction: Evidence from Chinese stock market. Mathematics, 13(10): 1551 (2025)

8

