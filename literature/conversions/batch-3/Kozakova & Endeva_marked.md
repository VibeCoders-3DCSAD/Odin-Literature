---
conversion_metadata:
  converted_at: "2026-07-21T13:50:42Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Kozakova & Endeva.pdf"
  source_pdf_sha256: "69887b591431b64400c76e4fb90a559a65773c5c0d0475aaf599307eb0ed72b0"
  page_count: 8
  markdown_char_count: 32170
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

UDC 004.8                                                                               doi: 10.15421/322509

N.L. Kozakova (https://orcid.org/0000-0002-7780-7617), M.H. Endeka 
Oles Honchar Dnipro National University

SMART FINANCE MANAGEMENT SYSTEM  
BASED ON ARTIFICIAL INTELLIGENCE TECHNOLOGIES

This  paper  presents  the  development  of  an  intelligent  personal  finance  management 
system  –  “Smart  Wallet”.  The  proposed  system  integrates  modern  artificial  intelligence 
methods for automated analysis, anomaly detection, expense forecasting, budget optimiza-
tion, and personalized recommendation generation. The architecture combines supervised 
and unsupervised learning algorithms, including k-Nearest Neighbors (k-NN) and decision 
trees for transaction classification, ARIMA and LSTM for financial forecasting, and Isola-
tion Forests, autoencoders, and SVM for anomaly detection. Matrix factorization and col-
laborative  filtering  methods  are  used  for  generating  recommendations.  Furthermore,  the 
system  employs  large  language  models  (LLMs)  to  produce  real-time  textual  advice  based 
on  aggregated  financial  activity.  Data  input  includes  categorized  transaction  history, 
timestamps, amounts, and merchant descriptions. The system is able to connect to external 
banking APIs for data retrieval and supports authentication via OAuth2. Thus, the “Smart 
Wallet” automates key financial operations and provides actionable recommendations tai-
lored to individual user behavior. The integration of classical machine learning algorithms 
with generative AI creates a hybrid, extensible framework suitable for real-time financial 
support.

Key words: personal finance, smart assistant, anomaly detection, expense forecasting,

artificial intelligence, machine learning, LLM, budget optimization.

Н.Л. Козакова (https://orcid.org/0000-0002-7780-7617), М.Г. Ендека 
Дніпровський національний університет імені Олеся Гончара

ЗАСТОСУВАННЯ ШТУЧНОГО ІНТЕЛЕКТУ  
В УПРАВЛІННІ ОСОБИСТИМИ ФІНАНСАМИ

У  роботі  представлено

інтелектуальну  систему  управління  особистими  
фінансами  –  «Розумний  гаманець»,  що  поєднує  сучасні  методи  штучного  інтелекту 
для автоматизації фінансового аналізу, виявлення аномалій, прогнозування витрат і 
формування  персоналізованих  рекомендацій.  Розроблена  система  орієнтована  на 
користувачів,  які  прагнуть  ефективно  контролювати  свої  витрати,  оптимізувати 
бюджет і приймати обґрунтовані фінансові рішення на основі аналітичних даних. 
Архітектура  «Розумного  гаманця»  включає  кілька  функціональних  модулів: 
класифікацію транзакцій із використанням алгоритмів  k-найближчих сусідів (k-NN) 
та  дерев  рішень;  прогнозування  витрат  на  основі  моделей  ARIMA  та  LSTM; 
виявлення підозрілих операцій за допомогою  автоенкодерів, Isolation Forest та SVM; 
генерацію  персоналізованих  порад  із  застосуванням  великих  мовних  моделей  (LLM). 
Рекомендаційний блок базується на методах колаборативної фільтрації та матричної 
факторизації, що забезпечує адаптацію системи до індивідуальних фінансових звичок 
користувача.  Вхідними  даними  є  транзакційна  історія  з  інформацією  про  категорії, 
суми,  часові  мітки  та  описи  операцій.  Дані  надходять  із  банківських  API  або 
_____________________________________ 
 Kozakova  N.L., Endeka M.H., 2025

104

---

<!-- PAGE 2 -->

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

імпортуються  з  файлів  CSV  і  зберігаються  в  базі  PostgreSQL,  що  забезпечує 
масштабоване  та  надійне  зберігання.  Система  генерує  аналітичні  візуалізації, 
виявляє аномалії, прогнозує фінансову активність і формує персоналізовані текстові 
рекомендації. Реалізація виконана мовою Python із використанням бібліотек  pandas, 
scikit-learn, tensorflow, statsmodels, surprise та openai.

Отже,  створена  система  забезпечує  комплексну  автоматизацію  управління 
особистими  фінансами,  поєднуючи  аналітичну  точність,  адаптивність  і  високий 
рівень персоналізації.

Ключові  слова:  штучний  інтелект,  особисті  фінанси,  прогнозування  витрат,

виявлення аномалій, рекомендаційна система, LLM, машинне навчання.

Introduction.  The  modern  world  is  rapidly  advancing  toward  digitalization 
and automation in all areas of life, and personal finance management is no excep-
tion. With the growing complexity of financial data, traditional budgeting methods 
are no longer sufficient for achieving the desired level of accuracy and adaptabil-
ity.  Artificial  Intelligence  (AI)  technologies  have  demonstrated  great  potential  in 
transforming how individuals interact with financial systems. One of the promising 
directions is the creation of the “Smart Wallet” – an intelligent system designed to 
automate financial record-keeping, analysis, and optimization of user financial ac-
tivity.

This  study  focuses on  the key  aspects of such  a system,  including  automated 
transaction categorization, expense forecasting, budget optimization, anomaly de-
tection, and personalized recommendation generation. Special attention is given to 
the use of machine learning algorithms in financial data analysis and prediction.

Analysis  of  research  and  publications.  Over  the  past  five  years,  research 
aimed  at  automating  financial  monitoring  and  forecasting  costs  using  machine 
learning and deep learning algorithms has intensified. In particular, Mienye (2024) 
and Li, Ding, and Chen (2023) discuss the application of deep learning models and 
large language models (LLMs) in financial analytics.

LSTM  and  GRU  algorithms  continue  to  demonstrate  high  efficiency  in  fore-
casting financial time series (Kong et al., 2025), but recent studies emphasize the 
advantages of Transformer architectures for long-term forecasting (Su et al., 2024). 
In  parallel,  hybrid  models  are  being  developed  that  combine  statistical  methods 
(ARIMA) with neural networks (Li et al., 2025).

Density-based  clustering  methods,  such  as  HDBSCAN,  are  successfully  used 
to segment customers and detect anomalies in transaction data (Afzal et al., 2024). 
In addition, research on NLP approaches demonstrates the effectiveness of vector-
izing  text  descriptions  of  transactions  for  their  automatic  categorization  (Re-
searchGate, 2023).

Thus, current trends are aimed at integrating various approaches – from statis-
tical and neural to generative – to create adaptive financial systems capable of self-
learning and personalization.

System Architecture. The Smart Wallet system has a two-level modular archi-

tecture consisting of two main functional blocks:

105

---

<!-- PAGE 3 -->

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

Block  A  –  Analytical  and  Computational  Unit  Responsible  for  data  preparation, 
classification, anomaly detection, and forecasting of financial information. 
Block B – Artificial Intelligence and Recommendation Unit utilizes the results of 
Block  A  to  generate  personalized  recommendations  using  large  language  models 
(LLMs).

The modular structure allows scalability, simple integration with external bank-
ing APIs, and flexibility in data processing. All data are stored in a PostgreSQL da-
tabase, while inter-module communication is handled via REST API.

Applied Methods. The k-NN algorithm is used for automatic categorization of 
transactions based on similarity to historical samples. The similarity is computed 
using the Euclidean distance:

where 


and

– two objects (feature vectors) between which the distance is meas-

ured;

 m – the number of features in each object;





– the value of the  -th feature in vector

;

– the Euclidean distance between objects

and

.

Decision trees. The information gain criterion is the main method used in deci-
sion tree  algorithms  (in particular, ID3, C4.5, C5.0) to select the best attribute  at 
each step of tree construction. At each stage, the decision tree selects the feature 
whose  division  provides  the  greatest  information  gain,  i.e.,  the  one  that  most  re-
duces entropy (uncertainty) in the sample. Information gain is defined as the dif-
ference between the entropy of the initial sample and the weighted average entropy 
of the subsets after division by attribute A:

where

– information gain obtained by using attribute

;

– the entropy of the current dataset  ;

Values

– all possible values of attribute

;

– the subset of

, where attribute

has value

;

106

---

<!-- PAGE 4 -->

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

– he proportion of samples that fall into subset

;

– the entropy of subset

ARIMA (Auto Regressive Integrated Moving Average). 
ARIMA models are used for expense forecasting based on previous data:

where

– lag operator, such that

;

– the number of differences required to make the series stationary;

– differentiation operator, i.e.:

  at

  at

;

;

– coefficients

- parts;

– coefficients

- parts;

– random error at the moment  .

LSTM (Long Short-Term Memory)

LSTM neural networks capture long-term dependencies in financial sequences.

Their internal mechanisms are defined by the following equations:

Forget Gate:

Input Gate:

Output Gate:

where

[0,1];

– renewable gate output (value between 0 і 1);

–  sigmoid activation function, which compresses values across the range

– weight matrix;

107

---

<!-- PAGE 5 -->

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

– hidden state in the previous step;

– output data at the current step;

– output reset gate (value between 0 і 1);

– candidate for a new hidden state;

– new hidden state at the current step.

Autoencoders. 
Autoencoders detect anomalies by measuring reconstruction error:

where

toencoder;

– input data vector;

– reconstructed data vector after passing through the au-

– number of features (dimensionality of the input vector);

– reconstruction loss value;

– squared difference between actual and reconstructed features.

Support Vector Machines (SVM). 
SVM identifies the boundary between normal and anomalous transactions:

where

– the new input object being tested;

– support vectors from the training dataset;

– number of support vectors;

– Lagrange multipliers (weights), most of which are zero;

– kernel function measuring similarity between

and

;

– bias term (threshold);

– decision function returning:

+1, if the result is > 0 → normal point;

−1, if the result is < 0 → anomaly.

A  distinctive  feature  of  Smart  Wallet  is  the  use  of  large  language  models 
(LLM) to generate text recommendations. After calculations, the system transmits

108

---

<!-- PAGE 6 -->

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

the summarized data to the LLM, which forms conclusions in a format that is un-
derstandable to the user, for example:

"Your transportation expenses have increased by 15% this month. We recom-

mend switching to a monthly pass to reduce your expenses."

Thus, the system not only analyzes data but also provides intelligent communi-

cation with the user.

Experimental  Results.  Testing  on  a  dataset  of  1000  transactions  (Fig.  1)

demonstrated the following results:

  Classification accuracy: 91.2% (k-NN + Decision Trees). 
  Mean  Absolute  Percentage  Error  (MAPE):  6.8%  (ARIMA),  5.4%

(LSTM).

  F1-score for anomaly detection: 0.86 (Autoencoders + Isolation Forest). 
  Recommendation precision: 0.89.

The  experimental  results  demonstrate  that  combining  traditional  statistical 
models with modern AI techniques enhances the performance of personal finance 
management systems.

After passing through Block A, the dataset is normalized, cleaned of redundant

information, and structured for further analysis (Fig. 2).

At  this  stage,  the  data  has  been  normalized,  categorized  for  more  efficient

analysis, and cleared of irrelevant elements.

Fig. 1. Example of the raw DataFrame containing users’ transactional data prior to pre-
processing

109

---

<!-- PAGE 7 -->

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

Fig. 2. Processed DataFrame ready for model training

The processed DataFrame is then transferred to Block B, where it is analyzed 
by  a  locally  deployed  and  configured  AI  module  that  generates  insights  and  rec-
ommendations (Fig.3).

Fig. 3.  AI-generated feedback and recommendations

The system consists of seven main modules responsible for data preprocessing, 
transaction  analysis,  anomaly  detection,  forecasting,  and  AI-driven  recommenda-
tions. The integrated workflow provides users with actionable insights to enhance 
their financial management.

The key modules of the system are as follows:

data_loader.py – responsible for preparing and loading raw financial data; 
classification.py – identifies potentially fraudulent transactions; 
anomaly_detection.py  –  detection  of  transactions  that  significantly  deviate  from 
normal user behavior;

110

---

<!-- PAGE 8 -->

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

forecasting.py – predicts future expenses, taking into account upcoming events and 
holidays; 
recommender.py – generates personalized recommendations based on user prefer-
ences and spending patterns; 
ai_answer.py – produces contextual responses and insights from the AI model; 
index.py – serves as the main script that integrates and executes all system mod-
ules.

As a result, the user receives clear, data-driven recommendations aimed at im-

proving their financial well-being.

Conclusions. The developed prototype of an intelligent personal finance man-
agement system has demonstrated high efficiency in performing the tasks set. The 
main  advantages  of  the  system  are  high  accuracy  of  expense  classification,  the 
ability to predict future financial events based on historical trends, and reliable de-
tection of anomalies that may indicate technical errors or potential fraud.

An additional advantage is the implementation of a personalized recommenda-
tion module that generates advice based on an analysis of the user's individual fi-
nancial  behavior.  This  ensures  the  practical  usefulness  of  the  system  and  creates 
the  conditions  for  its  further  integration  into  financial  applications  and  decision 
support  services.  In  the  future,  further  research  plans  include  expanding  the  sys-
tem's  functionality  through  deeper  integration  with  banking  APIs  and  the  use  of 
hybrid machine learning models.

Bibliographic references

1.  Mienye E.  Deep learning in finance: A survey of applications and techniques. MDPI. 2024.

Р. 2066-2091. https://www.mdpi.com/2673-2688/5/4/101

2.  Li  Y.,  Ding  H.,  &  Chen  H.  Large  language  models  in  finance:  A  survey.  arXiv.  2023.

https://arxiv.org/abs/2311.10723. arxiv.org

3.  Kong  X.,  et  al.  Deep  learning  for  time  series  forecasting:  A  survey.  Springer.  2025.

P. 5079–5112. https://doi.org/10.1007/s13042-025-02560-w. link.springer.com

4.  Su L., et al. A systematic review for transformer-based long-term series forecasting. Artificial 
https://doi.org/10.1007/s10462-024-11044-2.

Review.

2024.

33

p.

Intelligence 
link.springer.com

5.   Li J. C., et al. Enhancing financial time series forecasting with hybrid deep-learning models.

Information Sciences (Elsevier). 2025. 19 p. tandfonline.com

6.  Afzal,  M.,  et  al.  Segmentation  and  churn  analysis  using  HDBSCAN  and  alternatives.  DiVA

Portal. 2024.  https://www.diva-portal.org

7.  Machine  learning  for  financial  transaction  classification  using  character-level  embeddings.

ResearchGate. 2023. P. 159–172. https://www.researchgate.net

Received 02.09.2025.

111

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

 ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

UDC 004.8                                                                               doi: 10.15421/322509

N.L. Kozakova (https://orcid.org/0000-0002-7780-7617), M.H. Endeka
Oles Honchar Dnipro National University

SMART FINANCE MANAGEMENT SYSTEM
BASED ON ARTIFICIAL INTELLIGENCE TECHNOLOGIES

This  paper  presents  the  development  of  an  intelligent  personal  finance  management
system  –  “Smart  Wallet”.  The  proposed  system  integrates  modern  artificial  intelligence
methods for automated analysis, anomaly detection, expense forecasting, budget optimiza-
tion, and personalized recommendation generation. The architecture combines supervised
and unsupervised learning algorithms, including k-Nearest Neighbors (k-NN) and decision
trees for transaction classification, ARIMA and LSTM for financial forecasting, and Isola-
tion Forests, autoencoders, and SVM for anomaly detection. Matrix factorization and col-
laborative  filtering  methods  are  used  for  generating  recommendations.  Furthermore,  the
system  employs  large  language  models  (LLMs)  to  produce  real-time  textual  advice  based
on  aggregated  financial  activity.  Data  input  includes  categorized  transaction  history,
timestamps, amounts, and merchant descriptions. The system is able to connect to external
banking APIs for data retrieval and supports authentication via OAuth2. Thus, the “Smart
Wallet” automates key financial operations and provides actionable recommendations tai-
lored to individual user behavior. The integration of classical machine learning algorithms
with generative AI creates a hybrid, extensible framework suitable for real-time financial
support.

Key words: personal finance, smart assistant, anomaly detection, expense forecasting,

artificial intelligence, machine learning, LLM, budget optimization.

Н.Л. Козакова (https://orcid.org/0000-0002-7780-7617), М.Г. Ендека
Дніпровський національний університет імені Олеся Гончара

ЗАСТОСУВАННЯ ШТУЧНОГО ІНТЕЛЕКТУ
В УПРАВЛІННІ ОСОБИСТИМИ ФІНАНСАМИ

У  роботі  представлено

інтелектуальну  систему  управління  особистими
фінансами  –  «Розумний  гаманець»,  що  поєднує  сучасні  методи  штучного  інтелекту
для автоматизації фінансового аналізу, виявлення аномалій, прогнозування витрат і
формування  персоналізованих  рекомендацій.  Розроблена  система  орієнтована  на
користувачів,  які  прагнуть  ефективно  контролювати  свої  витрати,  оптимізувати
бюджет і приймати обґрунтовані фінансові рішення на основі аналітичних даних.
Архітектура  «Розумного  гаманця»  включає  кілька  функціональних  модулів:
класифікацію транзакцій із використанням алгоритмів  k-найближчих сусідів (k-NN)
та  дерев  рішень;  прогнозування  витрат  на  основі  моделей  ARIMA  та  LSTM;
виявлення підозрілих операцій за допомогою  автоенкодерів, Isolation Forest та SVM;
генерацію  персоналізованих  порад  із  застосуванням  великих  мовних  моделей  (LLM).
Рекомендаційний блок базується на методах колаборативної фільтрації та матричної
факторизації, що забезпечує адаптацію системи до індивідуальних фінансових звичок
користувача.  Вхідними  даними  є  транзакційна  історія  з  інформацією  про  категорії,
суми,  часові  мітки  та  описи  операцій.  Дані  надходять  із  банківських  API  або
_____________________________________
 Kozakova  N.L., Endeka M.H., 2025

 104

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

імпортуються  з  файлів  CSV  і  зберігаються  в  базі  PostgreSQL,  що  забезпечує
масштабоване  та  надійне  зберігання.  Система  генерує  аналітичні  візуалізації,
виявляє аномалії, прогнозує фінансову активність і формує персоналізовані текстові
рекомендації. Реалізація виконана мовою Python із використанням бібліотек  pandas,
scikit-learn, tensorflow, statsmodels, surprise та openai.

Отже,  створена  система  забезпечує  комплексну  автоматизацію  управління
особистими  фінансами,  поєднуючи  аналітичну  точність,  адаптивність  і  високий
рівень персоналізації.

Ключові  слова:  штучний  інтелект,  особисті  фінанси,  прогнозування  витрат,

виявлення аномалій, рекомендаційна система, LLM, машинне навчання.

Introduction.  The  modern  world  is  rapidly  advancing  toward  digitalization
and automation in all areas of life, and personal finance management is no excep-
tion. With the growing complexity of financial data, traditional budgeting methods
are no longer sufficient for achieving the desired level of accuracy and adaptabil-
ity.  Artificial  Intelligence  (AI)  technologies  have  demonstrated  great  potential  in
transforming how individuals interact with financial systems. One of the promising
directions is the creation of the “Smart Wallet” – an intelligent system designed to
automate financial record-keeping, analysis, and optimization of user financial ac-
tivity.

This  study  focuses on  the key  aspects of such  a system,  including  automated
transaction categorization, expense forecasting, budget optimization, anomaly de-
tection, and personalized recommendation generation. Special attention is given to
the use of machine learning algorithms in financial data analysis and prediction.

Analysis  of  research  and  publications.  Over  the  past  five  years,  research
aimed  at  automating  financial  monitoring  and  forecasting  costs  using  machine
learning and deep learning algorithms has intensified. In particular, Mienye (2024)
and Li, Ding, and Chen (2023) discuss the application of deep learning models and
large language models (LLMs) in financial analytics.

LSTM  and  GRU  algorithms  continue  to  demonstrate  high  efficiency  in  fore-
casting financial time series (Kong et al., 2025), but recent studies emphasize the
advantages of Transformer architectures for long-term forecasting (Su et al., 2024).
In  parallel,  hybrid  models  are  being  developed  that  combine  statistical  methods
(ARIMA) with neural networks (Li et al., 2025).

Density-based  clustering  methods,  such  as  HDBSCAN,  are  successfully  used
to segment customers and detect anomalies in transaction data (Afzal et al., 2024).
In addition, research on NLP approaches demonstrates the effectiveness of vector-
izing  text  descriptions  of  transactions  for  their  automatic  categorization  (Re-
searchGate, 2023).

Thus, current trends are aimed at integrating various approaches – from statis-
tical and neural to generative – to create adaptive financial systems capable of self-
learning and personalization.

System Architecture. The Smart Wallet system has a two-level modular archi-

tecture consisting of two main functional blocks:

105

 ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

Block  A  –  Analytical  and  Computational  Unit  Responsible  for  data  preparation,
classification, anomaly detection, and forecasting of financial information.
Block B – Artificial Intelligence and Recommendation Unit utilizes the results of
Block  A  to  generate  personalized  recommendations  using  large  language  models
(LLMs).

The modular structure allows scalability, simple integration with external bank-
ing APIs, and flexibility in data processing. All data are stored in a PostgreSQL da-
tabase, while inter-module communication is handled via REST API.

Applied Methods. The k-NN algorithm is used for automatic categorization of
transactions based on similarity to historical samples. The similarity is computed
using the Euclidean distance:

where


 and

 – two objects (feature vectors) between which the distance is meas-

ured;

 m – the number of features in each object;





 – the value of the  -th feature in vector

;

 – the Euclidean distance between objects

 and

.

Decision trees. The information gain criterion is the main method used in deci-
sion tree  algorithms  (in particular, ID3, C4.5, C5.0) to select the best attribute  at
each step of tree construction. At each stage, the decision tree selects the feature
whose  division  provides  the  greatest  information  gain,  i.e.,  the  one  that  most  re-
duces entropy (uncertainty) in the sample. Information gain is defined as the dif-
ference between the entropy of the initial sample and the weighted average entropy
of the subsets after division by attribute A:

where

 – information gain obtained by using attribute

;

 – the entropy of the current dataset  ;

Values

 – all possible values of attribute

;

 – the subset of

, where attribute

 has value

;

 106

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

 – he proportion of samples that fall into subset

;

 – the entropy of subset

ARIMA (Auto Regressive Integrated Moving Average).
ARIMA models are used for expense forecasting based on previous data:

where

 – lag operator, such that

;

 – the number of differences required to make the series stationary;

 – differentiation operator, i.e.:

  at

  at

;

;

 – coefficients

- parts;

 – coefficients

- parts;

 – random error at the moment  .

LSTM (Long Short-Term Memory)

LSTM neural networks capture long-term dependencies in financial sequences.

Their internal mechanisms are defined by the following equations:

Forget Gate:

Input Gate:

Output Gate:

where

[0,1];

 – renewable gate output (value between 0 і 1);

  –  sigmoid activation function, which compresses values across the range

 – weight matrix;

107

 ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

 – hidden state in the previous step;

 – output data at the current step;

 – output reset gate (value between 0 і 1);

 – candidate for a new hidden state;

 – new hidden state at the current step.

Autoencoders.
Autoencoders detect anomalies by measuring reconstruction error:

where

toencoder;

 – input data vector;

 – reconstructed data vector after passing through the au-

 – number of features (dimensionality of the input vector);

 – reconstruction loss value;

 – squared difference between actual and reconstructed features.

Support Vector Machines (SVM).
SVM identifies the boundary between normal and anomalous transactions:

where

 – the new input object being tested;

 – support vectors from the training dataset;

 – number of support vectors;

 – Lagrange multipliers (weights), most of which are zero;

 – kernel function measuring similarity between

 and

;

 – bias term (threshold);

 – decision function returning:

+1, if the result is > 0 → normal point;

−1, if the result is < 0 → anomaly.

A  distinctive  feature  of  Smart  Wallet  is  the  use  of  large  language  models
(LLM) to generate text recommendations. After calculations, the system transmits

 108

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

the summarized data to the LLM, which forms conclusions in a format that is un-
derstandable to the user, for example:

"Your transportation expenses have increased by 15% this month. We recom-

mend switching to a monthly pass to reduce your expenses."

Thus, the system not only analyzes data but also provides intelligent communi-

cation with the user.

Experimental  Results.  Testing  on  a  dataset  of  1000  transactions  (Fig.  1)

demonstrated the following results:

  Classification accuracy: 91.2% (k-NN + Decision Trees).
  Mean  Absolute  Percentage  Error  (MAPE):  6.8%  (ARIMA),  5.4%

(LSTM).

  F1-score for anomaly detection: 0.86 (Autoencoders + Isolation Forest).
  Recommendation precision: 0.89.

The  experimental  results  demonstrate  that  combining  traditional  statistical
models with modern AI techniques enhances the performance of personal finance
management systems.

After passing through Block A, the dataset is normalized, cleaned of redundant

information, and structured for further analysis (Fig. 2).

At  this  stage,  the  data  has  been  normalized,  categorized  for  more  efficient

analysis, and cleared of irrelevant elements.

Fig. 1. Example of the raw DataFrame containing users’ transactional data prior to pre-
processing

109

 ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

Fig. 2. Processed DataFrame ready for model training

The processed DataFrame is then transferred to Block B, where it is analyzed
by  a  locally  deployed  and  configured  AI  module  that  generates  insights  and  rec-
ommendations (Fig.3).

Fig. 3.  AI-generated feedback and recommendations

The system consists of seven main modules responsible for data preprocessing,
transaction  analysis,  anomaly  detection,  forecasting,  and  AI-driven  recommenda-
tions. The integrated workflow provides users with actionable insights to enhance
their financial management.

The key modules of the system are as follows:

data_loader.py – responsible for preparing and loading raw financial data;
classification.py – identifies potentially fraudulent transactions;
anomaly_detection.py  –  detection  of  transactions  that  significantly  deviate  from
normal user behavior;

 110

ISSN 2074-5893 Problems of applied mathematics and mathematical modeling.  Volume 25

forecasting.py – predicts future expenses, taking into account upcoming events and
holidays;
recommender.py – generates personalized recommendations based on user prefer-
ences and spending patterns;
ai_answer.py – produces contextual responses and insights from the AI model;
index.py – serves as the main script that integrates and executes all system mod-
ules.

As a result, the user receives clear, data-driven recommendations aimed at im-

proving their financial well-being.

Conclusions. The developed prototype of an intelligent personal finance man-
agement system has demonstrated high efficiency in performing the tasks set. The
main  advantages  of  the  system  are  high  accuracy  of  expense  classification,  the
ability to predict future financial events based on historical trends, and reliable de-
tection of anomalies that may indicate technical errors or potential fraud.

An additional advantage is the implementation of a personalized recommenda-
tion module that generates advice based on an analysis of the user's individual fi-
nancial  behavior.  This  ensures  the  practical  usefulness  of  the  system  and  creates
the  conditions  for  its  further  integration  into  financial  applications  and  decision
support  services.  In  the  future,  further  research  plans  include  expanding  the  sys-
tem's  functionality  through  deeper  integration  with  banking  APIs  and  the  use  of
hybrid machine learning models.

Bibliographic references

1.  Mienye E.  Deep learning in finance: A survey of applications and techniques. MDPI. 2024.

Р. 2066-2091. https://www.mdpi.com/2673-2688/5/4/101

2.  Li  Y.,  Ding  H.,  &  Chen  H.  Large  language  models  in  finance:  A  survey.  arXiv.  2023.

https://arxiv.org/abs/2311.10723. arxiv.org

3.  Kong  X.,  et  al.  Deep  learning  for  time  series  forecasting:  A  survey.  Springer.  2025.

P. 5079–5112. https://doi.org/10.1007/s13042-025-02560-w. link.springer.com

4.  Su L., et al. A systematic review for transformer-based long-term series forecasting. Artificial
https://doi.org/10.1007/s10462-024-11044-2.

Review.

2024.

33

p.

Intelligence
link.springer.com

5.   Li J. C., et al. Enhancing financial time series forecasting with hybrid deep-learning models.

Information Sciences (Elsevier). 2025. 19 p. tandfonline.com

6.  Afzal,  M.,  et  al.  Segmentation  and  churn  analysis  using  HDBSCAN  and  alternatives.  DiVA

Portal. 2024.  https://www.diva-portal.org

7.  Machine  learning  for  financial  transaction  classification  using  character-level  embeddings.

ResearchGate. 2023. P. 159–172. https://www.researchgate.net

Received 02.09.2025.

111

