---
conversion_metadata:
  converted_at: "2026-07-22T12:02:06Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Asemi et al-2024.pdf"
  source_pdf_sha256: "9a434de72e9ea541a978ecac5e178d2d79617ed525a2f51ed346d477177b9883"
  page_count: 16
  markdown_char_count: 77127
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Asemi et al. Journal of Big Data          (2024) 11:128  
https://doi.org/10.1186/s40537-024-00965-y

Journal of Big Data

RESEARCH

Open Access

A model for investment type recommender 
system based on the potential investors based 
on investors and experts feedback using ANFIS 
and MNN

Asefeh Asemi1*, Adeleh Asemi2 and Andrea Ko1

*Correspondence:   
Asemi.asefeh@uni-corvinus.hu

1 Corvinus University 
of Budapest, Budapest 1093, 
Hungary
2 Universiti Malaya, 50603 Kuala 
Lumpur, Malaysia

Abstract 
This article presents an investment recommender system based on an Adaptive Neuro-
Fuzzy Inference System (ANFIS) and pre-trained weights from a Multimodal Neural 
Network (MNN). The model is designed to support the investment process for the cus-
tomers and takes into consideration seven factors to implement the proposed invest-
ment system model through the customer or potential investor data set. The system 
takes input from a web-based questionnaire that collects data on investors’ prefer-
ences and investment goals. The data is then preprocessed and clustered using ETL 
tools, JMP, MATLAB, and Python. The ANFIS-based recommender system is designed 
with three inputs and one output and trained using a hybrid approach over three 
epochs with 188 data pairs and 18 fuzzy rules. The system’s performance is evalu-
ated using metrics such as RMSE, accuracy, precision, recall, and F1-score. The system 
is also designed to incorporate expert feedback and opinions from investors to cus-
tomize and improve investment recommendations. The article concludes that the pro-
posed ANFIS-based investment recommender system is effective and accurate in gen-
erating investment recommendations that meet investors’ preferences and goals.

Keywords:  Adaptive neuro-fuzzy inference system (ANFIS), Investment recommender 
system, Multimodal neural network, Clustering, JMP, MATLAB, Python, Fuzzy rules, 
Investor feedback, Expert feedback

© The Author(s) 2024. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Inter-
national License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you 
give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified 
the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The 
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a 
credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by 
statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of 
this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

---

<!-- PAGE 2 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 2 of 16

Graphical abstract

---

<!-- PAGE 3 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 3 of 16

Introduction

The  investment  recommender  systems  (IRSs)  have  become  increasingly  important  as 
individual investors face difficulties in making informed investment decisions in today’s 
complex  financial  markets.  This  paper  proposes  the  development  of  a  hybrid  recom-
mendation system that integrates fuzzy logic and neural networks to provide personal-
ized investment advice based on an individual investor’s preferences, risk tolerance, and 
financial goals. Specifically, the proposed system uses the Adaptive Neuro-Fuzzy Infer-
ence System (ANFIS) and multimodal neural network pretraining to improve its accu-
racy  and  effectiveness  [1,  2].  The  research  aims  to  investigate  the  potential  benefits  of 
this approach, answering several research questions related to the system’s accuracy and 
effectiveness, optimal pretraining objectives, data preparation, and training and valida-
tion  procedures.  Overall,  the  proposed  IRS  has  the  potential  to  provide  valuable  sup-
port to individual investors in making informed investment decisions, ultimately helping 
them achieve their financial goals.

Literature review

Recommender systems are widely used in investment decision-making to help individ-
ual investors choose suitable financial products based on their risk tolerance, financial 
goals, and investment experience [3]. However, traditional recommender systems have 
limitations,  such  as  the  reliance  on  a  limited  set  of  user  attributes  and  the  inability  to 
consider the dynamic nature of financial markets or user feedback. To overcome these 
limitations, recent research has explored the use of multimodal neural network pretrain-
ing techniques, such as ANFIS [4], that can model complex relationships between inputs 
and outputs and adapt to changing conditions. A variety of studies have investigated the 
use of machine learning and artificial intelligence methods, such as genetic algorithms, 
data clustering, and sentiment analysis, for stock prediction and investment efficiency. 
For  example,  Abraham  et  al.  [5]  explored  the  use  of  GA  and  random  forest  to  predict 
stock  trends,  while  Aggarwal  et  al.  [6]  examined  data  clustering  algorithms  and  their 
applications in stock prediction. Huang et al. [6] investigated neural network models for 
stock selection based on fundamental analysis, and Faridniya and Faridnia [7] provided 
a model for allocating resources and choosing investment types using Data Envelopment 
Analysis. Researchers have also explored the impact of factors such as economic policy 
uncertainty,  corporate  governance,  creative  accounting,  and  customer  experience  on 
investment  decision-making. Benkraiem et al. [8] investigated the impact of economic 
policy uncertainty, investor protection, and excess cash on stock value in a cross-coun-
try comparison, while Aksar et al. [9] examined the relationship between cash holding 
and  investment efficiency  for financially distressed firms, and the moderating effect of 
corporate  governance.  AL-Khafaji  et  al.  [10]  studied  the  role  of  creative  accounting  in 
increasing  the  marketing  of  shares  and  profits  in  the  Iraqi  stock  exchange,  and  Anda-
jani  [11]  examined  customer  experience  management  in  retailing.  Furthermore,  some 
studies propose novel combined business recommender system models that incorporate 
customer  investment  service  feedback  to  provide  personalized  investment  recommen-
dations.  Asemi  and  Ko  [4]  proposed  a  novel  combined  business  recommender  system 
model  using  customer  investment  service  feedback,  and  Chen  et  al.  [12]  studied  user 
perception of sentiment-integrated critiquing in recommender systems. Chen et al. [13]

---

<!-- PAGE 4 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 4 of 16

proposed  a  cluster-based  mutual  fund  classification  and  price  prediction  system  using 
machine learning for Robo-advisors, while Chatterjee et al. [14] proposed an NLP and 
LSTM-based  stock  prediction  and  recommender  system  for  KOSDAQ  and  KOSPI. 
Finally, various studies have applied ANFIS to evaluate dysarthric automatic speech rec-
ognition systems [15] or to estimate the return rate of blockchain financial products [16]. 
D’lima and Khan [17] used ANN and ANFIS to predict FOREX rates, while Davies et al. 
[18]  implemented  a  type-2  fuzzy  logic-based  prediction  system  for  the  Nigerian  stock 
exchange. Ezhilarasi and Sashi Rekha [19] proposed a secure recommendation applica-
tion for environment crops using big data analytics with a fuzzy framework. Asemi et al. 
[20]  propose  a  model  for  an  investment  recommender  system  using  ANFIS  based  on 
the potential investors’ decision key factors. They analyze big data to identify key factors 
influencing  investment  decisions  and  utilize  ANFIS  to  make  personalized  investment 
recommendations.  In  another  study,  Asemi  et  al.  [21]  investigate  the  impact  of  mana-
gerial  traits  on  investor  decision  prediction  using  ANFIS,  revealing  valuable  insights 
into the role of managers in influencing investment outcomes. Additionally, Asemi et al. 
[22] present an adaptive neuro-fuzzy inference system for customizing investment types 
based on potential investors’ demographics and feedback. Their research highlights the 
importance  of  incorporating  demographic  information  and  feedback  into  investment 
recommendations.  Finally,  Asemi  et  al.  [23]  conduct  a  systematic  review  and  propose 
an ANFIS-based investment-type recommender system that considers investors’ demo-
graphics. The authors present their findings at the 8th International Congress on Infor-
mation  and  Communication  Technology,  emphasizing  the  potential  of  ANFIS-based 
recommender systems in providing personalized investment advice. These studies col-
lectively contribute to the understanding of ANFIS-based investment recommender sys-
tems and their application in the financial domain. In summary, these studies provide a 
comprehensive examination of various aspects of stock prediction and investment effi-
ciency, utilizing a range of methods and techniques including machine learning, artifi-
cial  intelligence,  and  data  analysis.  The  use  of  multimodal  neural  network  pretraining 
techniques, such as ANFIS, has helped to overcome the limitations of traditional recom-
mender systems and allowed for the modeling of complex relationships between inputs 
and outputs while adapting to changing conditions.

Methods

This  study  proposes  a  novel  approach  to  developing  an  ANFIS-based  IRS  using  Mul-
timodal  Neural  Network  Pretraining.  ANFIS  is  a  hybrid  artificial  neural  network  that 
combines fuzzy logic and neural networks to perform data analysis and decision-mak-
ing.  Multimodal  Neural  Network  Pretraining  is  a  technique  used  in  deep  learning  to 
improve the overall performance of the neural network by allowing it to learn from mul-
tiple  sources  of  information  simultaneously.  The  proposed  approach  jointly  pre-trains 
all modalities using a predictive objective to improve the accuracy and effectiveness of 
investment  recommendations.  The  implementation  of  this  approach  was  carried  out 
using  MATLAB,  Python,  Anaconda,  and  Jupyter,  and  all  codes  and  data  used  in  this 
work  are  presented  in  this  article.  Predictive  pretraining  can  help  improve  the  perfor-
mance of ANFIS models by initializing the weights with a useful representation of the

---

<!-- PAGE 5 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 5 of 16

Table 1  Description of research methodology

Stage

Data collection

Data preprocessing

Machine learning

ANFIS training and testing

Multimodal neural network pretrain-
ing

Initializing neural network weights

Model evaluation

Expert feedback

Predictions on the new data

Description

Tools and techniques

Collection of data, in eight catego-
ries. Demographic, financial, experi-
ences, managerial traits, personality 
traits, key decision factors, invest-
ment products preferences, current 
investment, 1542 respondents

Translating, cleaning, transforming, 
clustering the data to make it suit-
able for analysis. Includes tasks such 
as outlier detection, missing value 
imputation, and feature selection

K-Means, Elbow Curve, Silhouette 
score, ANFIS Model Design

Training the new FIS using a hybrid 
approach over three epochs with 
188 data pairs and 18 fuzzy rules, 
Testing ANFIS by RMSE

Jointly pretraining all modalities of 
data using a predictive objective to 
improve the accuracy and effective-
ness of the ANFIS-based IRS

Initializing the ANFIS-based IRS with 
pre-trained weights from the Multi-
modal Neural Network Pretraining 
step

Evaluating the performance of the 
ANFIS-based IRS using metrics such 
as RMSE, accuracy, precision, recall, 
and F1-score

Incorporating expert opinions and 
feedback from investors to custom-
ize and improve rules and the 
investment recommendations

Mapping between predicted values 
and investment products

Portfolio Investment web question-
naire

ETL tools, JMP, MATLAB, Python, 
Anaconda, Jupyter

Adaptive Neuro-Fuzzy Inference 
Solutions, MATLAB, Python, Ana-
conda, Jupyter

Adaptive Neuro-Fuzzy Inference 
Solutions, fuzzification, implication 
rules, normalization, defuzzification, 
and integration, MATLAB, Python, 
Anaconda, Jupyter

Python, Anaconda, Jupyter

Python, Anaconda, Jupyter

Python, Anaconda, Jupyter

Adaptive Neuro-Fuzzy Inference 
Solutions, MATLAB, Python

Python, Anaconda, Jupyter

input data, leading to faster learning, better generalization performance, and more accu-
rate investment recommendations (Table 1).

Experimental results

The  experimental  results  demonstrate  the  effectiveness  of  the  proposed  ANFIS-based 
IRS  in  predicting  investment  types  based  on  a  combination  of  demographic,  decision 
key factors, personality traits, experiences, and financial and managerial traits. The sys-
tem  outperformed  traditional  methods  such  as  decision  trees  and  logistic  regression, 
highlighting the superiority of ANFIS-based approaches for investment prediction. The 
results included the following sections.

Preprocessing and clustering data

To  develop  an  ANFIS-based  IRS,  the  dataset  used  in  this  study  was  preprocessed  and 
clustered. The dataset consisted of eight columns, six of which contained clustered data

---

<!-- PAGE 6 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 6 of 16

related to types of investors based on demographic characteristics, financial status, man-
agement  characteristics,  and  more.  Duplicate  and  infrequent  rows  were  eliminated, 
resulting  in  188  potential  investor  groups.  Three  columns  related  to  investment  data 
were clustered using Python and k-means, including financial information, investment 
experiences,  and  other  features  such  as  personality  and  management  characteristics. 
These three columns were combined into three inputs for ANFIS, with the output con-
sisting  of  the  combination  of  clustered  data  related  to  investment  type  preference  and 
current investment type. The final dataset contained 188 data rows in four columns, and 
ANFIS was built using this dataset after preprocessing and clustering (Table 2).

ANFIS design model

The ANFIS-based IRS is a powerful tool for providing personalized investment recom-
mendations to potential investors.

Figure  1  in  MATLAB  shows  the  data  imported  for  the  ANFIS,  with  3  columns  for 
potential  investor  clusters  and  the  final  column  for  investing  product  clusters.  The 
ANFIS  model  was  designed  using  a  Sugeno-type  fuzzy  function  with  MFs  displayed 
in the graph. A total of 188 train data pairs were used, with max aggregation and min 
implication. The MFs are trimf and the output MF type is constant. Aggregation com-
bines fuzzy sets representing rule outputs and occurs once before the final defuzzifica-
tion stage for each output variable.

ANFIS training and testing

Figure 2 displays the trained grid of the ANFIS system, which has three inputs and 
one  output  for  investment  type.  The  system  was  trained  using  a  hybrid  approach 
over  three  epochs,  and  the  error  for  each  epoch  is  ~  0.72.  The  ANFIS  info  section 
provides  information  about  the  training  process  of  the  Combined  ANFIS  system,

Table 2  Description of data preprocessing

Data columns

Data description

Demographic data

Financial data and experi-
ences

Other traits

Investment type prefer-
ence and current invest-
ment type

Data related to potential 
investors’ demographic 
characteristics such as age, 
gender, education level, 
job, location, and income

Data related to potential 
investors’ financial status 
and experiences such as 
income, savings, invest-
ment portfolio, etc

Data related to potential 
investors’ personality 
characteristics, manage-
ment characteristics, and 
key factors for investment 
decision-making

Data related to poten-
tial investors’ preferred 
investment type and their 
current investment type

Preprocessing steps 
clustering technique

Clustering technique

Cleaning and preparing 
data
K-means clustering by JMP

K-means clustering by JMP

Re-clustering by Python 
using k-means after initial 
clustering using JMP 
software
Using the Elbow curve 
and Silhouette score to 
determine the optimal 
number of clusters
K-means clustering

K-means clustering by JMP

Cleaning and filtering to 
remove data rows with 
less than 20 frequencies

---

<!-- PAGE 7 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 7 of 16

including  the  number  of  nodes,  parameters,  and  fuzzy  rules.  The  system  has  been 
successfully trained using 188 data pairs, with a minimal training root mean squared 
error of 0.721054. The model achieved an F1-score of 0.6667 and a minimal training 
RMSE of 0.721054. An F1-score of 0.6667 indicates that the model’s performance is 
reasonably  good,  as  it  considers  both  precision  and  recall.  A  perfect  F1  score  is  1, 
while an F1 score of 0 indicates that the model’s predictions are completely wrong. 
Therefore,  an  F1-score  of  0.6667  suggests  that  the  model’s  precision  and  recall 
are  both  reasonably  high,  although  there  is  room  for  improvement.  Overall,  this 
F1-score indicates that the model can make accurate predictions, but there may be 
some  misclassifications.  The  trained  ANFIS  system,  which  generated  a  total  of  18 
rules  that  are  the  decision-making  mechanisms  for  investment  recommendations. 
As the following:

Fig. 1  Data and fuzzy function for ANFIS model

---

<!-- PAGE 8 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 8 of 16

Fig. 2  Trained and tested grid of the ANFIS system for investment type prediction with hybrid approach

Figure 3 depicts the structure of the ANFIS Model, including fuzzification, impli-
cation  rules,  normalization,  defuzzification,  and  integration,  resulting  in  an  invest-
ment  recommendation  for  the  investor.  Overall,  the  ANFIS-based  IRS  provides  a 
powerful and customizable tool for personalized investment recommendations.

---

<!-- PAGE 9 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 9 of 16

Fig. 3  Proposed ANFIS structure

Multimodal neural network pretraining

Result Test MSE is 0.0011995050086818341. A low test MSE indicates that your model is

---

<!-- PAGE 10 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 10 of 16

performing well on the test data, which is a good sign. However, it’s important to keep in 
mind that a low test MSE doesn’t necessarily mean that our model is perfect. Thus, the 
other metrics considered such as accuracy or precision to solve the problem. Now that 
we  have  a  pre-trained  neural  network  model,  we  can  use  it  for  making  predictions  on 
new data. To do this, we can use the prediction method of the Keras model object, which 
takes  an  input  array  of  the  same  shape  as  the  training  data  and  returns  the  predicted 
output values. Here, new_data is a numpy array with two new input samples, which we 
normalize using the same scaler object that was used to normalize the training data. We 
then reshape the new data to have the same shape as the training data and use the pre-
diction method of the model to obtain the predicted output values. Finally, we print the 
predictions to the console.

Initializing neural network weights

---

<!-- PAGE 11 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 11 of 16

Model evaluation

Prediction on the new data

Discussion

The  investment  industry  is  one  of  the  most  important  sectors  in  the  global  economy, 
with  trillions  of  dollars  in  assets  under  management.  Investors  face  many  challenges, 
including  market  volatility,  changing  economic  conditions,  and  increasing  amounts  of 
data  to  analyze.  IRSs  are  becoming  increasingly  popular  to  help  investors  make  more 
informed  decisions  about  where  to  allocate  their  funds.  Previous  studies  have  utilized 
ANFIS for investment prediction, such as predicting stock market and real estate invest-
ment trust prices. However, these studies did not focus on predicting investment type

---

<!-- PAGE 12 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 12 of 16

based  on a combination  of  inputs, as this study does. Other studies proposed ANFIS-
based  models  for  stock  price  prediction  or  investment  type  prediction  using  demo-
graphic characteristics and investment behavior. Hybrid systems combining ANFIS with 
particle swarm optimization or GA have also been proposed for investment type predic-
tion  with  better  performance  than  traditional  methods.  However,  none  of  these  stud-
ies  specifically  focus  on  predicting  investment  type  based  on  a  combination  of  inputs 
including demographic, decision key factors, personality traits, experiences, and finan-
cial  and  managerial  traits  as  this  study  does  [4,  5,  16,  20,  21,  24–27].  In  this  research, 
we  presented  an  IRS  based  on  an  ANFIS.  ANFIS  is  a  type  of  artificial  neural  network 
that combines fuzzy logic and neural networks to create a powerful prediction engine. 
In this section, we analyze and discuss the results of implementing the proposed invest-
ment  recommender  system  framework,  focusing  on  the  effectiveness  and  accuracy  of 
the model across various phases of development (Fig. 4). Our system takes as input a set 
of user preferences and investment goals and provides a list of recommended investment 
products based on these inputs as the following:

Phase 1: Data Collection • Inputs from the Web-based Questionnaire: ○ Data Cat-
egories: □ Demographics: Age, Gender, Education, Income Level, etc. □ Financial 
Information: Income, Assets, Investment Capital, etc. □ Investment Experience: Past 
investments,  success  rates,  risk  tolerance,  etc.  □  Personality  &  Managerial  Traits: 
Decision-making style, leadership qualities, etc. □ Investment Preferences: Preferred 
types of investments, expected returns, investment horizon, etc.
Phase 2: Data Preprocessing & Clustering • Data Preprocessing: ○ Tools Used: ETL 
Tools, Python, JMP, MATLAB. ○ Objective: Clean and structure the raw data to pre-
pare it for clustering and model training. • Clustering Process: ○ K-Means Cluster-
ing (Elbow Curve & Silhouette score): □ Clustered Columns: □ Financial Informa-
tion: Clusters investors based on their financial profiles. □ Investment Experiences: 
Clusters investors based on their previous investment experiences and outcomes. □ 
Personality & Managerial Traits: Clusters investors based on their personal charac-
teristics and management styles. □ Clustering Approach: Use Python and K-Means 
to identify optimal clusters for each column. ○ Combined Inputs for ANFIS: □ The 
clustered  data  from  the  three  columns  (Financial  Information,  Investment  Experi-
ences,  Personality  &  Managerial  Traits)  are  combined  into  three  inputs  for  the 
ANFIS model.
Phase 3: ANFIS-Based Recommender System • ANFIS Model: ○ Design: □ Inputs: 
□  Three  inputs  representing  the  clustered  data:  Financial  Information,  Investment 
Experiences, Personality & Managerial Traits. □ Output: □ A combination of clus-
tered data related to Investment Type Preference and Current Investment Type. ○ 
Training:  □  Dataset:  The  final  dataset  contains  188  rows  and  four  columns  after 
preprocessing and clustering. □ Hybrid Training Approach: □ The ANFIS model is 
trained using a hybrid approach over three epochs. □ Fuzzy Rules: Incorporates 18 
fuzzy rules to drive decision-making and recommendations. ○ Objective: To provide 
personalized investment recommendations based on the clustered inputs.
Phase 4: Multimodal Neural Network Pretraining • Pretraining the Neural Network: 
○ Purpose: Enhance the ANFIS model’s accuracy by pretraining the neural network

---

<!-- PAGE 13 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 13 of 16

components.  ○  Approach:  Fine-tune  the  neural  network  layers,  ensuring  optimal 
performance in recommending investment types.
Phase 5: Model Training and Testing • Training & Performance Evaluation: ○ Train-
ing: Continuous refinement of the ANFIS model using the dataset to enhance predic-
tive capabilities. ○ Testing Metrics: □ Root Mean Square Error (RMSE): Measures 
the  prediction  error.  □  Precision:  Assesses  the  accuracy  of  the  investment  recom-
mendations.  □  Recall:  Evaluates  the  model’s  ability  to  identify  relevant  investment 
options. □ F1-Score: Balances precision and recall for overall model assessment.
Phase 6: Expert Feedback Loop • Continuous Improvement: ○ Expert Input: Finan-
cial experts provide ongoing feedback to refine fuzzy rules and adjust model param-
eters. ○ Error Correction: Incorporate expert insights to improve the accuracy and 
relevance of recommendations.
Phase 7: Final Output & Decision-Making • Final Output: ○ Personalized Investment 
Recommendations: □ Tailored investment strategies generated based on the ANFIS 
model’s  output,  reflecting  the  investor’s  unique  profile.  □ The  output  is  influenced 
by the combined data clusters, ensuring that recommendations are well-aligned with 
the investor’s preferences and current portfolio. o Feedback from Investors: □ Appli-
cation  Layer:  The  recommendations  are  implemented,  and  feedback  is  gathered  to 
improve  the  recommender  system.  □  Objective:  To  continuously  enhance  the  sys-
tem’s performance and investor satisfaction (Additional file 1).

Our results show that our ANFIS-based IRS performs well in recommending investment 
products  based  on  user  preferences  and  investment  goals.  Our  system  provides  accu-
rate and personalized investment recommendations to investors, allowing them to make 
more informed decisions about where to allocate their funds. Our system can be used 
by both novice and experienced investors, making it an effective tool for anyone looking 
to optimize their investment portfolio. One limitation of our system is that it requires a 
significant amount of data to train the ANFIS model. Collecting this data can be time-
consuming and costly, particularly for smaller investment firms or individual investors. 
Additionally,  our  system  is  designed  for  retail  investors,  and  may  not  be  suitable  for 
institutional investors or investors with very complex investment portfolios. Overall, our 
ANFIS-based IRS is an effective tool for investors looking to optimize their investment 
portfolios. By combining fuzzy logic and neural networks, our system provides person-
alized  investment  recommendations  based  on  user  preferences  and  investment  goals. 
Our system is easy to use and can be customized based on expert opinions and feedback 
from investors. With further development, our system has the potential to revolutionize 
the investment industry and provide investors with more accurate and effective invest-
ment recommendations.

Conclusion

In  conclusion,  the  ANFIS-based  IRS  has  demonstrated  promising  results  in  recom-
mending suitable investment types to investors. By using data collected through a web 
questionnaire,  preprocessing  it  with  ETL  tools,  and  training  the  ANFIS  model  with  a 
hybrid  approach  over  three  epochs,  the  system  achieved  a  low  RMSE  and  high  accu-
racy  in  predicting  suitable  investments.  Furthermore,  the  system’s  performance  was

---

<!-- PAGE 14 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 14 of 16

Fig. 4  Comprehensive Framework for the Proposed Investment Recommender System

enhanced  through  multimodal  neural  network  pretraining  and  expert  feedback.  The 
system’s  results  have  several  practical  implications  for  the  financial  industry,  as  it  can 
assist investors in making informed investment decisions based on their preferences and 
risk tolerance. The system’s ability to incorporate expert feedback and customize rules 
and recommendations based on investor feedback can lead to increased satisfaction and 
trust in the investment recommendations. However, there are several avenues for future 
research that can further improve the ANFIS-based IRS. One potential area of research 
is the integration of alternative data sources, such as social media sentiment analysis or 
news sentiment analysis, to enhance the system’s accuracy and predictive power. Addi-
tionally,  incorporating  more  sophisticated  machine  learning  algorithms,  such  as  deep 
learning, can improve the system’s ability to capture complex patterns and relationships 
in the data. Moreover, future research can investigate the system’s scalability and appli-
cability in different investment contexts, such as international investments or real estate 
investments.  Finally,  the  system’s  ethical  implications  and  potential  biases  should  be 
thoroughly examined, as it relies on historical data to make future predictions, which can 
perpetuate existing biases and inequalities. In summary, the ANFIS-based IRS has the 
potential to revolutionize the investment decision-making process by providing custom-
ized and accurate recommendations to investors. Future research can further enhance 
the system’s performance and applicability, paving the way for more efficient and effec-
tive investment decisions while addressing ethical concerns and potential biases.

Supplementary Information
The online version contains supplementary material available at https:// doi. org/ 10. 1186/ s40537- 024- 00965-y.

Additional file 1: Comprehensive Framework for the Investment Recommender System.

Acknowledgements
Not applicable.

Author contributions
Asefeh Asemi played the role of the main researcher, Adeleh Asemi provided guidance as the research advisor, and 
Andrea Ko served as the research supervisor.

Funding
No funding was received for this study.

---

<!-- PAGE 15 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 15 of 16

Availability of data and materials
The original data used in this research was collected through a collaborative effort involving the Corvinus University of 
Budapest, the Dorsum company, and the Portfolio in the 1.3.1-VKE-2018-00007 project, conducted in the Hungarian lan-
guage. The consortium agreement and project leader’s consent allow for the use of project data in additional research 
and publications by the authors. The authors have translated, cleaned, and prepared the data specifically for this study. 
New data can be accessed at [28] in title of "Data for Adaptive Neuro-Fuzzy Inference System for Customizing Investment 
Type based on the Potential Investors’ Demographics", available at Mendeley Data.

Declarations

Ethics approval and consent to participate
This article does not involve any studies that were conducted on human or animal participants by any of the authors. 
Not applicable as there were no participants involved in the study.

Competing interests
The authors disclose that their work at the Corvinus University of Budapest involved collaboration with commercial 
companies (Dorsum and Portfolio) in the design and development of the survey used in this research.

Received: 30 November 2022   Accepted: 16 July 2024

References
 1.  Hervella ÁS, Rouco J, Novo J, Ortega M. Self-supervised multimodal reconstruction pre-training for retinal

2.

computer-aided diagnosis. Expert Syst Appl. 2021;185: 115598. https:// doi. org/ 10. 1016/j. eswa. 2021. 115598.
Jang JSR. ANFIS: Adaptive-network-based fuzzy inference system. IEEE Trans Syst Man Cybern. 1993;23(3):665–85. 
https:// doi. org/ 10. 1109/ 21. 256541.

3.  Chen J. Investment product. Reviewed by Godon Scott, Investopedia.Com. https:// www. inves toped ia. com/ terms/i/

inves tment- produ ct. asp. 2020.

4.  Asemi A, Ko A. A novel combined business recommender system model using customer investment service feed-
back. In: 34th Bled EConference Digital Support from Crisis to Progressive Change: Conference Proceedings, 2021; 
pp. 223–237. https:// doi. org/ 10. 18690/ 978- 961- 286- 485-9. 17.

5.  Abraham R, Samad ME, Bakhach AM, El-Chaarani H, Sardouk A, Nemar SE, Jaber D. Forecasting a stock trend using

genetic algorithm and random forest. J Risk Financ Manage. 2022;15(5):5. https:// doi. org/ 10. 3390/ jrfm1 50501 88.
 6.  Aggarwal A, Hess O, Lockman JL, Smith L, Stevens M, Bruce J, Caruso T. Anesthesiologists with advanced degrees

in education: qualitative study of a changing paradigm. JMIR Med Educ. 2022;8(2):e38050. https:// doi. org/ 10. 2196/ 
38050.
Faridniya A, Faridnia M. Providing a model for allocating resources and choosing investment type using data envel-
opment analysis (DEA) (case study: social security organization). J Adv Pharm Educ Res. 2019;9(S2):112–24.

7.

8.  Benkraiem R, Gaaya S, Lakhal F, Lakhal N. Economic policy uncertainty, investor protection, and the value of excess 
cash: a cross-country comparison. Financ Res Lett. 2023;52: 103572. https:// doi. org/ 10. 1016/j. frl. 2022. 103572.
 9.  Aksar M, Hassan S, Kayani MB, Khan S, Ahmed T. Cash holding and investment efficiency nexus for financially dis-

tressed firms: the moderating role of corporate governance. Manage Sci Lett. 2022;12(1):67–74. https:// doi. org/ 10. 
5267/j. msl. 2021.7. 001.

10.  AL-Khafaji AAK, Mustangs RF, Alsaalim FHAJ. The role of creative accounting in increasing the marketing of shares 
and their profits in the Iraqi stock exchange. Period Eng Nat Sci. 2022;10(2):323–35. https:// doi. org/ 10. 21533/ pen. 
v10i2. 2886.

11.  Andajani E. Understanding customer experience management in retailing. Proc Soc Behav Sci. 2015;211:629–33.

https:// doi. org/ 10. 1016/j. sbspro. 2015. 11. 082.

12.  Chen L, Yan D, Wang F. User perception of sentiment-integrated critiquing in recommender systems. Int J Hum

Comput Stud. 2019;121:4–20. https:// doi. org/ 10. 1016/j. ijhcs. 2017. 09. 005.

13.  Chen X, Ye S, Huang C. Cluster-based mutual fund classification and price prediction using machine learning for

robo-advisors. Comput Intell Neurosci. 2021;2021: e4984265. https:// doi. org/ 10. 1155/ 2021/ 49842 65.

14.  Chatterjee I, Gwan J, Kim YJ, Lee MS, Cho M. An NLP and LSTM based stock prediction and recommender system

for KOSDAQ and KOSPI. In: Singh M, Kang DK, Lee JH, Tiwary US, Singh D, Chung WY, editors. Intelligent human 
computer interaction, Pt I, vol. 12615. Cham: Springer International Publishing; 2021. p. 403–13. https:// doi. org/ 10. 
1007/ 978-3- 030- 68449-5_ 40.

15.  Asemi A, Salim SSB, Shahamiri SR, Asemi A, Houshangi N. Adaptive neuro-fuzzy inference system for evaluating

dysarthric automatic speech recognition (ASR) systems. Soft Comput. 2019;23:3529–44. https:// doi. org/ 10. 1007/ 
s00500- 018- 3013-4.

16.  Birim ŞÖ, Sönmez FE, Liman YS. Estimating return rate of blockchain financial product by ANFIS-PSO method. In:

Lecture notes in networks and systems, 504 LNNS, pp. 802–809. Scopus. 2022. https:// doi. org/ 10. 1007/ 978-3- 031- 
09173-5_ 92.

17.  D’lima N, Khan S. FOREX rate prediction using ANN and ANFIS Conference. https:// www. seman ticsc holar. org/ paper/ 
FOREX- rate- predi ction- using- ANN- and- ANFIS-D% 27lima- Khan/ 6817d 1cc9f 7ac35 cf284 04f0e 17e35 8b54f a16d1. 
2016.

18.  Davies IN, Ene D, Cookey IB, Lenu GF. Implementation of a type-2 fuzzy logic based prediction system for the Nige-

rian stock exchange. 2022.

---

<!-- PAGE 16 -->

Asemi et al. Journal of Big Data          (2024) 11:128

Page 16 of 16

19.  Ezhilarasi TP, Sashi Rekha K. Secure recommendation application for environment crop using big data analytics with

fuzzy framework. J Green Eng. 2020;10(4):1799–815.

20.  Asemi A, Asemi A, Ko A. Investment recommender system model based on the potential investors’ key decision

factors. Big Data. 2023. https:// doi. org/ 10. 1089/ big. 2022. 0302.

21.  Asemi A, Asemi A, Ko A. A systematic review and propose an ANFIS-based investment type recommender system

using investors’ demographic. In: A Hybrid Conference 8th International Congress on Information and Communica-
tion Technology ICICT 2023, London, UK, 20–23. https:// www. resea rchga te. net/ publi cation/ 36901 9468_ Syste matic_ 
Review_ and_ Propo se_ an_ ANFIS- Based_ Inves tment_ Type_ Recom mender_ System_ using_ Inves tors’_ Demog raphic. 
2023b.

22.  Asemi A, Asemi A, Ko A. Adaptive neuro-fuzzy inference system for customizing investment type based

on the potential investors’ demographics and feedback. J Big Data. 2023;10(1):87. https:// doi. org/ 10. 1186/ 
s40537- 023- 00784-7.

23.  Asemi A, Asemi A, Ko A. Unveiling the impact of managerial traits on investor decision prediction: ANFIS approach.

Soft Comput. 2023. https:// doi. org/ 10. 1007/ s00500- 023- 08102-2.

24.  Asemi A, Asemi A. Intelligent MCDM method for supplier selection under fuzzy environment. Int J Inf Sci Manage

(IJISM). https:// ijism. ricest. ac. ir/ index. php/ ijism/ artic le/ view/ 346. 2014.

25.  Huang Y, Capretz LF, Ho D. Neural network models for stock selection based on fundamental analysis. IEEE Can Conf

Electr Comput Eng (CCECE). 2019;2019:1–4. https:// doi. org/ 10. 1109/ CCECE. 2019. 88615 50.

26.  Kovács T, Ko A, Asemi A. Exploration of the investment patterns of potential retail banking customers using two-

stage cluster analysis. J Big Data, 2021; 8(1). https:// doi. org/ 10. 1186/ s40537- 021- 00529-4.

27.  Wang Y, Zhang M. Simulation analysis of regional real estate investment risk based on system dynamics. E3S Web

Conf. 2021;251:01070. https:// doi. org/ 10. 1051/ e3sco nf/ 20212 51010 70.

28.  Asemi A. Data for adaptive neuro-fuzzy inference system for customizing investment type based on the potential

investors’ demographics. Available at Mendeley Data, V1, 2022. https:// doi. org/ 10. 17632/ 93dmw j5yhk.1.

Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Asemi et al. Journal of Big Data          (2024) 11:128
https://doi.org/10.1186/s40537-024-00965-y

Journal of Big Data

RESEARCH

Open Access

A model for investment type recommender
system based on the potential investors based
on investors and experts feedback using ANFIS
and MNN

Asefeh Asemi1*, Adeleh Asemi2 and Andrea Ko1

*Correspondence:
Asemi.asefeh@uni-corvinus.hu

1 Corvinus University
of Budapest, Budapest 1093,
Hungary
2 Universiti Malaya, 50603 Kuala
Lumpur, Malaysia

Abstract
This article presents an investment recommender system based on an Adaptive Neuro-
Fuzzy Inference System (ANFIS) and pre-trained weights from a Multimodal Neural
Network (MNN). The model is designed to support the investment process for the cus-
tomers and takes into consideration seven factors to implement the proposed invest-
ment system model through the customer or potential investor data set. The system
takes input from a web-based questionnaire that collects data on investors’ prefer-
ences and investment goals. The data is then preprocessed and clustered using ETL
tools, JMP, MATLAB, and Python. The ANFIS-based recommender system is designed
with three inputs and one output and trained using a hybrid approach over three
epochs with 188 data pairs and 18 fuzzy rules. The system’s performance is evalu-
ated using metrics such as RMSE, accuracy, precision, recall, and F1-score. The system
is also designed to incorporate expert feedback and opinions from investors to cus-
tomize and improve investment recommendations. The article concludes that the pro-
posed ANFIS-based investment recommender system is effective and accurate in gen-
erating investment recommendations that meet investors’ preferences and goals.

Keywords:  Adaptive neuro-fuzzy inference system (ANFIS), Investment recommender
system, Multimodal neural network, Clustering, JMP, MATLAB, Python, Fuzzy rules,
Investor feedback, Expert feedback

© The Author(s) 2024. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Inter-
national License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you
give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified
the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a
credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by
statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of
this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

Asemi et al. Journal of Big Data          (2024) 11:128

Page 2 of 16

Graphical abstract

Asemi et al. Journal of Big Data          (2024) 11:128

Page 3 of 16

Introduction

The  investment  recommender  systems  (IRSs)  have  become  increasingly  important  as
individual investors face difficulties in making informed investment decisions in today’s
complex  financial  markets.  This  paper  proposes  the  development  of  a  hybrid  recom-
mendation system that integrates fuzzy logic and neural networks to provide personal-
ized investment advice based on an individual investor’s preferences, risk tolerance, and
financial goals. Specifically, the proposed system uses the Adaptive Neuro-Fuzzy Infer-
ence System (ANFIS) and multimodal neural network pretraining to improve its accu-
racy  and  effectiveness  [1,  2].  The  research  aims  to  investigate  the  potential  benefits  of
this approach, answering several research questions related to the system’s accuracy and
effectiveness, optimal pretraining objectives, data preparation, and training and valida-
tion  procedures.  Overall,  the  proposed  IRS  has  the  potential  to  provide  valuable  sup-
port to individual investors in making informed investment decisions, ultimately helping
them achieve their financial goals.

Literature review

Recommender systems are widely used in investment decision-making to help individ-
ual investors choose suitable financial products based on their risk tolerance, financial
goals, and investment experience [3]. However, traditional recommender systems have
limitations,  such  as  the  reliance  on  a  limited  set  of  user  attributes  and  the  inability  to
consider the dynamic nature of financial markets or user feedback. To overcome these
limitations, recent research has explored the use of multimodal neural network pretrain-
ing techniques, such as ANFIS [4], that can model complex relationships between inputs
and outputs and adapt to changing conditions. A variety of studies have investigated the
use of machine learning and artificial intelligence methods, such as genetic algorithms,
data clustering, and sentiment analysis, for stock prediction and investment efficiency.
For  example,  Abraham  et  al.  [5]  explored  the  use  of  GA  and  random  forest  to  predict
stock  trends,  while  Aggarwal  et  al.  [6]  examined  data  clustering  algorithms  and  their
applications in stock prediction. Huang et al. [6] investigated neural network models for
stock selection based on fundamental analysis, and Faridniya and Faridnia [7] provided
a model for allocating resources and choosing investment types using Data Envelopment
Analysis. Researchers have also explored the impact of factors such as economic policy
uncertainty,  corporate  governance,  creative  accounting,  and  customer  experience  on
investment  decision-making. Benkraiem et al. [8] investigated the impact of economic
policy uncertainty, investor protection, and excess cash on stock value in a cross-coun-
try comparison, while Aksar et al. [9] examined the relationship between cash holding
and  investment efficiency  for financially distressed firms, and the moderating effect of
corporate  governance.  AL-Khafaji  et  al.  [10]  studied  the  role  of  creative  accounting  in
increasing  the  marketing  of  shares  and  profits  in  the  Iraqi  stock  exchange,  and  Anda-
jani  [11]  examined  customer  experience  management  in  retailing.  Furthermore,  some
studies propose novel combined business recommender system models that incorporate
customer  investment  service  feedback  to  provide  personalized  investment  recommen-
dations.  Asemi  and  Ko  [4]  proposed  a  novel  combined  business  recommender  system
model  using  customer  investment  service  feedback,  and  Chen  et  al.  [12]  studied  user
perception of sentiment-integrated critiquing in recommender systems. Chen et al. [13]

 Asemi et al. Journal of Big Data          (2024) 11:128

Page 4 of 16

proposed  a  cluster-based  mutual  fund  classification  and  price  prediction  system  using
machine learning for Robo-advisors, while Chatterjee et al. [14] proposed an NLP and
LSTM-based  stock  prediction  and  recommender  system  for  KOSDAQ  and  KOSPI.
Finally, various studies have applied ANFIS to evaluate dysarthric automatic speech rec-
ognition systems [15] or to estimate the return rate of blockchain financial products [16].
D’lima and Khan [17] used ANN and ANFIS to predict FOREX rates, while Davies et al.
[18]  implemented  a  type-2  fuzzy  logic-based  prediction  system  for  the  Nigerian  stock
exchange. Ezhilarasi and Sashi Rekha [19] proposed a secure recommendation applica-
tion for environment crops using big data analytics with a fuzzy framework. Asemi et al.
[20]  propose  a  model  for  an  investment  recommender  system  using  ANFIS  based  on
the potential investors’ decision key factors. They analyze big data to identify key factors
influencing  investment  decisions  and  utilize  ANFIS  to  make  personalized  investment
recommendations.  In  another  study,  Asemi  et  al.  [21]  investigate  the  impact  of  mana-
gerial  traits  on  investor  decision  prediction  using  ANFIS,  revealing  valuable  insights
into the role of managers in influencing investment outcomes. Additionally, Asemi et al.
[22] present an adaptive neuro-fuzzy inference system for customizing investment types
based on potential investors’ demographics and feedback. Their research highlights the
importance  of  incorporating  demographic  information  and  feedback  into  investment
recommendations.  Finally,  Asemi  et  al.  [23]  conduct  a  systematic  review  and  propose
an ANFIS-based investment-type recommender system that considers investors’ demo-
graphics. The authors present their findings at the 8th International Congress on Infor-
mation  and  Communication  Technology,  emphasizing  the  potential  of  ANFIS-based
recommender systems in providing personalized investment advice. These studies col-
lectively contribute to the understanding of ANFIS-based investment recommender sys-
tems and their application in the financial domain. In summary, these studies provide a
comprehensive examination of various aspects of stock prediction and investment effi-
ciency, utilizing a range of methods and techniques including machine learning, artifi-
cial  intelligence,  and  data  analysis.  The  use  of  multimodal  neural  network  pretraining
techniques, such as ANFIS, has helped to overcome the limitations of traditional recom-
mender systems and allowed for the modeling of complex relationships between inputs
and outputs while adapting to changing conditions.

Methods

This  study  proposes  a  novel  approach  to  developing  an  ANFIS-based  IRS  using  Mul-
timodal  Neural  Network  Pretraining.  ANFIS  is  a  hybrid  artificial  neural  network  that
combines fuzzy logic and neural networks to perform data analysis and decision-mak-
ing.  Multimodal  Neural  Network  Pretraining  is  a  technique  used  in  deep  learning  to
improve the overall performance of the neural network by allowing it to learn from mul-
tiple  sources  of  information  simultaneously.  The  proposed  approach  jointly  pre-trains
all modalities using a predictive objective to improve the accuracy and effectiveness of
investment  recommendations.  The  implementation  of  this  approach  was  carried  out
using  MATLAB,  Python,  Anaconda,  and  Jupyter,  and  all  codes  and  data  used  in  this
work  are  presented  in  this  article.  Predictive  pretraining  can  help  improve  the  perfor-
mance of ANFIS models by initializing the weights with a useful representation of the

Asemi et al. Journal of Big Data          (2024) 11:128

Page 5 of 16

Table 1  Description of research methodology

Stage

Data collection

Data preprocessing

Machine learning

ANFIS training and testing

Multimodal neural network pretrain-
ing

Initializing neural network weights

Model evaluation

Expert feedback

Predictions on the new data

Description

Tools and techniques

Collection of data, in eight catego-
ries. Demographic, financial, experi-
ences, managerial traits, personality
traits, key decision factors, invest-
ment products preferences, current
investment, 1542 respondents

Translating, cleaning, transforming,
clustering the data to make it suit-
able for analysis. Includes tasks such
as outlier detection, missing value
imputation, and feature selection

K-Means, Elbow Curve, Silhouette
score, ANFIS Model Design

Training the new FIS using a hybrid
approach over three epochs with
188 data pairs and 18 fuzzy rules,
Testing ANFIS by RMSE

Jointly pretraining all modalities of
data using a predictive objective to
improve the accuracy and effective-
ness of the ANFIS-based IRS

Initializing the ANFIS-based IRS with
pre-trained weights from the Multi-
modal Neural Network Pretraining
step

Evaluating the performance of the
ANFIS-based IRS using metrics such
as RMSE, accuracy, precision, recall,
and F1-score

Incorporating expert opinions and
feedback from investors to custom-
ize and improve rules and the
investment recommendations

Mapping between predicted values
and investment products

Portfolio Investment web question-
naire

ETL tools, JMP, MATLAB, Python,
Anaconda, Jupyter

Adaptive Neuro-Fuzzy Inference
Solutions, MATLAB, Python, Ana-
conda, Jupyter

Adaptive Neuro-Fuzzy Inference
Solutions, fuzzification, implication
rules, normalization, defuzzification,
and integration, MATLAB, Python,
Anaconda, Jupyter

Python, Anaconda, Jupyter

Python, Anaconda, Jupyter

Python, Anaconda, Jupyter

Adaptive Neuro-Fuzzy Inference
Solutions, MATLAB, Python

Python, Anaconda, Jupyter

input data, leading to faster learning, better generalization performance, and more accu-
rate investment recommendations (Table 1).

Experimental results

The  experimental  results  demonstrate  the  effectiveness  of  the  proposed  ANFIS-based
IRS  in  predicting  investment  types  based  on  a  combination  of  demographic,  decision
key factors, personality traits, experiences, and financial and managerial traits. The sys-
tem  outperformed  traditional  methods  such  as  decision  trees  and  logistic  regression,
highlighting the superiority of ANFIS-based approaches for investment prediction. The
results included the following sections.

Preprocessing and clustering data

To  develop  an  ANFIS-based  IRS,  the  dataset  used  in  this  study  was  preprocessed  and
clustered. The dataset consisted of eight columns, six of which contained clustered data

 Asemi et al. Journal of Big Data          (2024) 11:128

Page 6 of 16

related to types of investors based on demographic characteristics, financial status, man-
agement  characteristics,  and  more.  Duplicate  and  infrequent  rows  were  eliminated,
resulting  in  188  potential  investor  groups.  Three  columns  related  to  investment  data
were clustered using Python and k-means, including financial information, investment
experiences,  and  other  features  such  as  personality  and  management  characteristics.
These three columns were combined into three inputs for ANFIS, with the output con-
sisting  of  the  combination  of  clustered  data  related  to  investment  type  preference  and
current investment type. The final dataset contained 188 data rows in four columns, and
ANFIS was built using this dataset after preprocessing and clustering (Table 2).

ANFIS design model

The ANFIS-based IRS is a powerful tool for providing personalized investment recom-
mendations to potential investors.

Figure  1  in  MATLAB  shows  the  data  imported  for  the  ANFIS,  with  3  columns  for
potential  investor  clusters  and  the  final  column  for  investing  product  clusters.  The
ANFIS  model  was  designed  using  a  Sugeno-type  fuzzy  function  with  MFs  displayed
in the graph. A total of 188 train data pairs were used, with max aggregation and min
implication. The MFs are trimf and the output MF type is constant. Aggregation com-
bines fuzzy sets representing rule outputs and occurs once before the final defuzzifica-
tion stage for each output variable.

ANFIS training and testing

Figure 2 displays the trained grid of the ANFIS system, which has three inputs and
one  output  for  investment  type.  The  system  was  trained  using  a  hybrid  approach
over  three  epochs,  and  the  error  for  each  epoch  is  ~  0.72.  The  ANFIS  info  section
provides  information  about  the  training  process  of  the  Combined  ANFIS  system,

Table 2  Description of data preprocessing

Data columns

Data description

Demographic data

Financial data and experi-
ences

Other traits

Investment type prefer-
ence and current invest-
ment type

Data related to potential
investors’ demographic
characteristics such as age,
gender, education level,
job, location, and income

Data related to potential
investors’ financial status
and experiences such as
income, savings, invest-
ment portfolio, etc

Data related to potential
investors’ personality
characteristics, manage-
ment characteristics, and
key factors for investment
decision-making

Data related to poten-
tial investors’ preferred
investment type and their
current investment type

Preprocessing steps
clustering technique

Clustering technique

Cleaning and preparing
data
K-means clustering by JMP

K-means clustering by JMP

Re-clustering by Python
using k-means after initial
clustering using JMP
software
Using the Elbow curve
and Silhouette score to
determine the optimal
number of clusters
K-means clustering

K-means clustering by JMP

Cleaning and filtering to
remove data rows with
less than 20 frequencies

Asemi et al. Journal of Big Data          (2024) 11:128

Page 7 of 16

including  the  number  of  nodes,  parameters,  and  fuzzy  rules.  The  system  has  been
successfully trained using 188 data pairs, with a minimal training root mean squared
error of 0.721054. The model achieved an F1-score of 0.6667 and a minimal training
RMSE of 0.721054. An F1-score of 0.6667 indicates that the model’s performance is
reasonably  good,  as  it  considers  both  precision  and  recall.  A  perfect  F1  score  is  1,
while an F1 score of 0 indicates that the model’s predictions are completely wrong.
Therefore,  an  F1-score  of  0.6667  suggests  that  the  model’s  precision  and  recall
are  both  reasonably  high,  although  there  is  room  for  improvement.  Overall,  this
F1-score indicates that the model can make accurate predictions, but there may be
some  misclassifications.  The  trained  ANFIS  system,  which  generated  a  total  of  18
rules  that  are  the  decision-making  mechanisms  for  investment  recommendations.
As the following:

Fig. 1  Data and fuzzy function for ANFIS model

 Asemi et al. Journal of Big Data          (2024) 11:128

Page 8 of 16

Fig. 2  Trained and tested grid of the ANFIS system for investment type prediction with hybrid approach

Figure 3 depicts the structure of the ANFIS Model, including fuzzification, impli-
cation  rules,  normalization,  defuzzification,  and  integration,  resulting  in  an  invest-
ment  recommendation  for  the  investor.  Overall,  the  ANFIS-based  IRS  provides  a
powerful and customizable tool for personalized investment recommendations.

Asemi et al. Journal of Big Data          (2024) 11:128

Page 9 of 16

Fig. 3  Proposed ANFIS structure

Multimodal neural network pretraining

Result Test MSE is 0.0011995050086818341. A low test MSE indicates that your model is

 Asemi et al. Journal of Big Data          (2024) 11:128

Page 10 of 16

performing well on the test data, which is a good sign. However, it’s important to keep in
mind that a low test MSE doesn’t necessarily mean that our model is perfect. Thus, the
other metrics considered such as accuracy or precision to solve the problem. Now that
we  have  a  pre-trained  neural  network  model,  we  can  use  it  for  making  predictions  on
new data. To do this, we can use the prediction method of the Keras model object, which
takes  an  input  array  of  the  same  shape  as  the  training  data  and  returns  the  predicted
output values. Here, new_data is a numpy array with two new input samples, which we
normalize using the same scaler object that was used to normalize the training data. We
then reshape the new data to have the same shape as the training data and use the pre-
diction method of the model to obtain the predicted output values. Finally, we print the
predictions to the console.

Initializing neural network weights

Asemi et al. Journal of Big Data          (2024) 11:128

Page 11 of 16

Model evaluation

Prediction on the new data

Discussion

The  investment  industry  is  one  of  the  most  important  sectors  in  the  global  economy,
with  trillions  of  dollars  in  assets  under  management.  Investors  face  many  challenges,
including  market  volatility,  changing  economic  conditions,  and  increasing  amounts  of
data  to  analyze.  IRSs  are  becoming  increasingly  popular  to  help  investors  make  more
informed  decisions  about  where  to  allocate  their  funds.  Previous  studies  have  utilized
ANFIS for investment prediction, such as predicting stock market and real estate invest-
ment trust prices. However, these studies did not focus on predicting investment type

 Asemi et al. Journal of Big Data          (2024) 11:128

Page 12 of 16

based  on a combination  of  inputs, as this study does. Other studies proposed ANFIS-
based  models  for  stock  price  prediction  or  investment  type  prediction  using  demo-
graphic characteristics and investment behavior. Hybrid systems combining ANFIS with
particle swarm optimization or GA have also been proposed for investment type predic-
tion  with  better  performance  than  traditional  methods.  However,  none  of  these  stud-
ies  specifically  focus  on  predicting  investment  type  based  on  a  combination  of  inputs
including demographic, decision key factors, personality traits, experiences, and finan-
cial  and  managerial  traits  as  this  study  does  [4,  5,  16,  20,  21,  24–27].  In  this  research,
we  presented  an  IRS  based  on  an  ANFIS.  ANFIS  is  a  type  of  artificial  neural  network
that combines fuzzy logic and neural networks to create a powerful prediction engine.
In this section, we analyze and discuss the results of implementing the proposed invest-
ment  recommender  system  framework,  focusing  on  the  effectiveness  and  accuracy  of
the model across various phases of development (Fig. 4). Our system takes as input a set
of user preferences and investment goals and provides a list of recommended investment
products based on these inputs as the following:

Phase 1: Data Collection • Inputs from the Web-based Questionnaire: ○ Data Cat-
egories: □ Demographics: Age, Gender, Education, Income Level, etc. □ Financial
Information: Income, Assets, Investment Capital, etc. □ Investment Experience: Past
investments,  success  rates,  risk  tolerance,  etc.  □  Personality  &  Managerial  Traits:
Decision-making style, leadership qualities, etc. □ Investment Preferences: Preferred
types of investments, expected returns, investment horizon, etc.
Phase 2: Data Preprocessing & Clustering • Data Preprocessing: ○ Tools Used: ETL
Tools, Python, JMP, MATLAB. ○ Objective: Clean and structure the raw data to pre-
pare it for clustering and model training. • Clustering Process: ○ K-Means Cluster-
ing (Elbow Curve & Silhouette score): □ Clustered Columns: □ Financial Informa-
tion: Clusters investors based on their financial profiles. □ Investment Experiences:
Clusters investors based on their previous investment experiences and outcomes. □
Personality & Managerial Traits: Clusters investors based on their personal charac-
teristics and management styles. □ Clustering Approach: Use Python and K-Means
to identify optimal clusters for each column. ○ Combined Inputs for ANFIS: □ The
clustered  data  from  the  three  columns  (Financial  Information,  Investment  Experi-
ences,  Personality  &  Managerial  Traits)  are  combined  into  three  inputs  for  the
ANFIS model.
Phase 3: ANFIS-Based Recommender System • ANFIS Model: ○ Design: □ Inputs:
□  Three  inputs  representing  the  clustered  data:  Financial  Information,  Investment
Experiences, Personality & Managerial Traits. □ Output: □ A combination of clus-
tered data related to Investment Type Preference and Current Investment Type. ○
Training:  □  Dataset:  The  final  dataset  contains  188  rows  and  four  columns  after
preprocessing and clustering. □ Hybrid Training Approach: □ The ANFIS model is
trained using a hybrid approach over three epochs. □ Fuzzy Rules: Incorporates 18
fuzzy rules to drive decision-making and recommendations. ○ Objective: To provide
personalized investment recommendations based on the clustered inputs.
Phase 4: Multimodal Neural Network Pretraining • Pretraining the Neural Network:
○ Purpose: Enhance the ANFIS model’s accuracy by pretraining the neural network

Asemi et al. Journal of Big Data          (2024) 11:128

Page 13 of 16

components.  ○  Approach:  Fine-tune  the  neural  network  layers,  ensuring  optimal
performance in recommending investment types.
Phase 5: Model Training and Testing • Training & Performance Evaluation: ○ Train-
ing: Continuous refinement of the ANFIS model using the dataset to enhance predic-
tive capabilities. ○ Testing Metrics: □ Root Mean Square Error (RMSE): Measures
the  prediction  error.  □  Precision:  Assesses  the  accuracy  of  the  investment  recom-
mendations.  □  Recall:  Evaluates  the  model’s  ability  to  identify  relevant  investment
options. □ F1-Score: Balances precision and recall for overall model assessment.
Phase 6: Expert Feedback Loop • Continuous Improvement: ○ Expert Input: Finan-
cial experts provide ongoing feedback to refine fuzzy rules and adjust model param-
eters. ○ Error Correction: Incorporate expert insights to improve the accuracy and
relevance of recommendations.
Phase 7: Final Output & Decision-Making • Final Output: ○ Personalized Investment
Recommendations: □ Tailored investment strategies generated based on the ANFIS
model’s  output,  reflecting  the  investor’s  unique  profile.  □ The  output  is  influenced
by the combined data clusters, ensuring that recommendations are well-aligned with
the investor’s preferences and current portfolio. o Feedback from Investors: □ Appli-
cation  Layer:  The  recommendations  are  implemented,  and  feedback  is  gathered  to
improve  the  recommender  system.  □  Objective:  To  continuously  enhance  the  sys-
tem’s performance and investor satisfaction (Additional file 1).

Our results show that our ANFIS-based IRS performs well in recommending investment
products  based  on  user  preferences  and  investment  goals.  Our  system  provides  accu-
rate and personalized investment recommendations to investors, allowing them to make
more informed decisions about where to allocate their funds. Our system can be used
by both novice and experienced investors, making it an effective tool for anyone looking
to optimize their investment portfolio. One limitation of our system is that it requires a
significant amount of data to train the ANFIS model. Collecting this data can be time-
consuming and costly, particularly for smaller investment firms or individual investors.
Additionally,  our  system  is  designed  for  retail  investors,  and  may  not  be  suitable  for
institutional investors or investors with very complex investment portfolios. Overall, our
ANFIS-based IRS is an effective tool for investors looking to optimize their investment
portfolios. By combining fuzzy logic and neural networks, our system provides person-
alized  investment  recommendations  based  on  user  preferences  and  investment  goals.
Our system is easy to use and can be customized based on expert opinions and feedback
from investors. With further development, our system has the potential to revolutionize
the investment industry and provide investors with more accurate and effective invest-
ment recommendations.

Conclusion

In  conclusion,  the  ANFIS-based  IRS  has  demonstrated  promising  results  in  recom-
mending suitable investment types to investors. By using data collected through a web
questionnaire,  preprocessing  it  with  ETL  tools,  and  training  the  ANFIS  model  with  a
hybrid  approach  over  three  epochs,  the  system  achieved  a  low  RMSE  and  high  accu-
racy  in  predicting  suitable  investments.  Furthermore,  the  system’s  performance  was

 Asemi et al. Journal of Big Data          (2024) 11:128

Page 14 of 16

Fig. 4  Comprehensive Framework for the Proposed Investment Recommender System

enhanced  through  multimodal  neural  network  pretraining  and  expert  feedback.  The
system’s  results  have  several  practical  implications  for  the  financial  industry,  as  it  can
assist investors in making informed investment decisions based on their preferences and
risk tolerance. The system’s ability to incorporate expert feedback and customize rules
and recommendations based on investor feedback can lead to increased satisfaction and
trust in the investment recommendations. However, there are several avenues for future
research that can further improve the ANFIS-based IRS. One potential area of research
is the integration of alternative data sources, such as social media sentiment analysis or
news sentiment analysis, to enhance the system’s accuracy and predictive power. Addi-
tionally,  incorporating  more  sophisticated  machine  learning  algorithms,  such  as  deep
learning, can improve the system’s ability to capture complex patterns and relationships
in the data. Moreover, future research can investigate the system’s scalability and appli-
cability in different investment contexts, such as international investments or real estate
investments.  Finally,  the  system’s  ethical  implications  and  potential  biases  should  be
thoroughly examined, as it relies on historical data to make future predictions, which can
perpetuate existing biases and inequalities. In summary, the ANFIS-based IRS has the
potential to revolutionize the investment decision-making process by providing custom-
ized and accurate recommendations to investors. Future research can further enhance
the system’s performance and applicability, paving the way for more efficient and effec-
tive investment decisions while addressing ethical concerns and potential biases.

Supplementary Information
The online version contains supplementary material available at https:// doi. org/ 10. 1186/ s40537- 024- 00965-y.

Additional file 1: Comprehensive Framework for the Investment Recommender System.

Acknowledgements
Not applicable.

Author contributions
Asefeh Asemi played the role of the main researcher, Adeleh Asemi provided guidance as the research advisor, and
Andrea Ko served as the research supervisor.

Funding
No funding was received for this study.

Asemi et al. Journal of Big Data          (2024) 11:128

Page 15 of 16

Availability of data and materials
The original data used in this research was collected through a collaborative effort involving the Corvinus University of
Budapest, the Dorsum company, and the Portfolio in the 1.3.1-VKE-2018-00007 project, conducted in the Hungarian lan-
guage. The consortium agreement and project leader’s consent allow for the use of project data in additional research
and publications by the authors. The authors have translated, cleaned, and prepared the data specifically for this study.
New data can be accessed at [28] in title of "Data for Adaptive Neuro-Fuzzy Inference System for Customizing Investment
Type based on the Potential Investors’ Demographics", available at Mendeley Data.

Declarations

Ethics approval and consent to participate
This article does not involve any studies that were conducted on human or animal participants by any of the authors.
Not applicable as there were no participants involved in the study.

Competing interests
The authors disclose that their work at the Corvinus University of Budapest involved collaboration with commercial
companies (Dorsum and Portfolio) in the design and development of the survey used in this research.

Received: 30 November 2022   Accepted: 16 July 2024

References
 1.  Hervella ÁS, Rouco J, Novo J, Ortega M. Self-supervised multimodal reconstruction pre-training for retinal

 2.

computer-aided diagnosis. Expert Syst Appl. 2021;185: 115598. https:// doi. org/ 10. 1016/j. eswa. 2021. 115598.
Jang JSR. ANFIS: Adaptive-network-based fuzzy inference system. IEEE Trans Syst Man Cybern. 1993;23(3):665–85.
https:// doi. org/ 10. 1109/ 21. 256541.

 3.  Chen J. Investment product. Reviewed by Godon Scott, Investopedia.Com. https:// www. inves toped ia. com/ terms/i/

inves tment- produ ct. asp. 2020.

 4.  Asemi A, Ko A. A novel combined business recommender system model using customer investment service feed-
back. In: 34th Bled EConference Digital Support from Crisis to Progressive Change: Conference Proceedings, 2021;
pp. 223–237. https:// doi. org/ 10. 18690/ 978- 961- 286- 485-9. 17.

 5.  Abraham R, Samad ME, Bakhach AM, El-Chaarani H, Sardouk A, Nemar SE, Jaber D. Forecasting a stock trend using

genetic algorithm and random forest. J Risk Financ Manage. 2022;15(5):5. https:// doi. org/ 10. 3390/ jrfm1 50501 88.
 6.  Aggarwal A, Hess O, Lockman JL, Smith L, Stevens M, Bruce J, Caruso T. Anesthesiologists with advanced degrees

in education: qualitative study of a changing paradigm. JMIR Med Educ. 2022;8(2):e38050. https:// doi. org/ 10. 2196/
38050.
Faridniya A, Faridnia M. Providing a model for allocating resources and choosing investment type using data envel-
opment analysis (DEA) (case study: social security organization). J Adv Pharm Educ Res. 2019;9(S2):112–24.

 7.

 8.  Benkraiem R, Gaaya S, Lakhal F, Lakhal N. Economic policy uncertainty, investor protection, and the value of excess
cash: a cross-country comparison. Financ Res Lett. 2023;52: 103572. https:// doi. org/ 10. 1016/j. frl. 2022. 103572.
 9.  Aksar M, Hassan S, Kayani MB, Khan S, Ahmed T. Cash holding and investment efficiency nexus for financially dis-

tressed firms: the moderating role of corporate governance. Manage Sci Lett. 2022;12(1):67–74. https:// doi. org/ 10.
5267/j. msl. 2021.7. 001.

 10.  AL-Khafaji AAK, Mustangs RF, Alsaalim FHAJ. The role of creative accounting in increasing the marketing of shares
and their profits in the Iraqi stock exchange. Period Eng Nat Sci. 2022;10(2):323–35. https:// doi. org/ 10. 21533/ pen.
v10i2. 2886.

 11.  Andajani E. Understanding customer experience management in retailing. Proc Soc Behav Sci. 2015;211:629–33.

https:// doi. org/ 10. 1016/j. sbspro. 2015. 11. 082.

 12.  Chen L, Yan D, Wang F. User perception of sentiment-integrated critiquing in recommender systems. Int J Hum

Comput Stud. 2019;121:4–20. https:// doi. org/ 10. 1016/j. ijhcs. 2017. 09. 005.

 13.  Chen X, Ye S, Huang C. Cluster-based mutual fund classification and price prediction using machine learning for

robo-advisors. Comput Intell Neurosci. 2021;2021: e4984265. https:// doi. org/ 10. 1155/ 2021/ 49842 65.

 14.  Chatterjee I, Gwan J, Kim YJ, Lee MS, Cho M. An NLP and LSTM based stock prediction and recommender system

for KOSDAQ and KOSPI. In: Singh M, Kang DK, Lee JH, Tiwary US, Singh D, Chung WY, editors. Intelligent human
computer interaction, Pt I, vol. 12615. Cham: Springer International Publishing; 2021. p. 403–13. https:// doi. org/ 10.
1007/ 978-3- 030- 68449-5_ 40.

 15.  Asemi A, Salim SSB, Shahamiri SR, Asemi A, Houshangi N. Adaptive neuro-fuzzy inference system for evaluating

dysarthric automatic speech recognition (ASR) systems. Soft Comput. 2019;23:3529–44. https:// doi. org/ 10. 1007/
s00500- 018- 3013-4.

 16.  Birim ŞÖ, Sönmez FE, Liman YS. Estimating return rate of blockchain financial product by ANFIS-PSO method. In:

Lecture notes in networks and systems, 504 LNNS, pp. 802–809. Scopus. 2022. https:// doi. org/ 10. 1007/ 978-3- 031-
09173-5_ 92.

 17.  D’lima N, Khan S. FOREX rate prediction using ANN and ANFIS Conference. https:// www. seman ticsc holar. org/ paper/
FOREX- rate- predi ction- using- ANN- and- ANFIS-D% 27lima- Khan/ 6817d 1cc9f 7ac35 cf284 04f0e 17e35 8b54f a16d1.
2016.

 18.  Davies IN, Ene D, Cookey IB, Lenu GF. Implementation of a type-2 fuzzy logic based prediction system for the Nige-

rian stock exchange. 2022.

 Asemi et al. Journal of Big Data          (2024) 11:128

Page 16 of 16

 19.  Ezhilarasi TP, Sashi Rekha K. Secure recommendation application for environment crop using big data analytics with

fuzzy framework. J Green Eng. 2020;10(4):1799–815.

 20.  Asemi A, Asemi A, Ko A. Investment recommender system model based on the potential investors’ key decision

factors. Big Data. 2023. https:// doi. org/ 10. 1089/ big. 2022. 0302.

 21.  Asemi A, Asemi A, Ko A. A systematic review and propose an ANFIS-based investment type recommender system

using investors’ demographic. In: A Hybrid Conference 8th International Congress on Information and Communica-
tion Technology ICICT 2023, London, UK, 20–23. https:// www. resea rchga te. net/ publi cation/ 36901 9468_ Syste matic_
Review_ and_ Propo se_ an_ ANFIS- Based_ Inves tment_ Type_ Recom mender_ System_ using_ Inves tors’_ Demog raphic.
2023b.

 22.  Asemi A, Asemi A, Ko A. Adaptive neuro-fuzzy inference system for customizing investment type based

on the potential investors’ demographics and feedback. J Big Data. 2023;10(1):87. https:// doi. org/ 10. 1186/
s40537- 023- 00784-7.

 23.  Asemi A, Asemi A, Ko A. Unveiling the impact of managerial traits on investor decision prediction: ANFIS approach.

Soft Comput. 2023. https:// doi. org/ 10. 1007/ s00500- 023- 08102-2.

 24.  Asemi A, Asemi A. Intelligent MCDM method for supplier selection under fuzzy environment. Int J Inf Sci Manage

(IJISM). https:// ijism. ricest. ac. ir/ index. php/ ijism/ artic le/ view/ 346. 2014.

 25.  Huang Y, Capretz LF, Ho D. Neural network models for stock selection based on fundamental analysis. IEEE Can Conf

Electr Comput Eng (CCECE). 2019;2019:1–4. https:// doi. org/ 10. 1109/ CCECE. 2019. 88615 50.

 26.  Kovács T, Ko A, Asemi A. Exploration of the investment patterns of potential retail banking customers using two-

stage cluster analysis. J Big Data, 2021; 8(1). https:// doi. org/ 10. 1186/ s40537- 021- 00529-4.

 27.  Wang Y, Zhang M. Simulation analysis of regional real estate investment risk based on system dynamics. E3S Web

Conf. 2021;251:01070. https:// doi. org/ 10. 1051/ e3sco nf/ 20212 51010 70.

 28.  Asemi A. Data for adaptive neuro-fuzzy inference system for customizing investment type based on the potential

investors’ demographics. Available at Mendeley Data, V1, 2022. https:// doi. org/ 10. 17632/ 93dmw j5yhk.1.

Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

