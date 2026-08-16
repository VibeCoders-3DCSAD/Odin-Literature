---
conversion_metadata:
  converted_at: "2026-07-21T08:39:22Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Shaha & Gavekar.pdf"
  source_pdf_sha256: "cdb38880aaa833d26ba9bf14123f013455890e4f8a85b77f72e168bd0e38b9b1"
  page_count: 12
  markdown_char_count: 114399
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

01003

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

Enhancing  Online  Fraud  Detection:  Leveraging 
Machine  Learning  and  Behavioral  Indicators  for 
Improved Accuracy and Real-Time Detection

Prasad Shaha1*, Vidya Gavekar2

1School of Management & Research, Dr. D. Y. Patil Dnyan Prasad University's School of 
Management & Research, Pune, Maharashtra, India 
2 Surydatta Institute of Management and Mass Communication, Pune, Maharashtra, India

Abstract - Fraud detection remains a critical challenge in financial security, 
requiring  robust  and  efficient  methodologies  to  identify  fraudulent 
transactions accurately. This study presents a comprehensive evaluation of 
machine learning (ML) models for fraud detection, emphasizing the role of 
behavioral  indicators  in  enhancing  model  performance.  A  comparative 
analysis  of  traditional  and  advanced  ML  models,  including  Logistic 
Regression,  Decision  Tree,  Random  Forest,  Support  Vector  Machine 
(SVM), Artificial Neural Networks (ANN), and LightGBM, was conducted 
using real-world fraud detection datasets. LightGBM, the proposed model, 
outperformed other methods, achieving the highest ROC-AUC (0.981), F1-
score  (0.902),  and  lowest  false  positive  rate  (0.006).  The  study  also 
highlights the importance of feature selection, class imbalance handling, and 
real-world  applicability  by  discussing  computational  efficiency  and 
deployment  challenges. These  findings  contribute to  the  growing body of 
fraud detection research by offering a practical, scalable, and high-accuracy 
ML approach for real-time fraud prevention systems.

1 Introduction

As  e-commerce  and  online  financial  transactions  continue  to  expand,  the  prevalence  of 
fraudulent activities has grown significantly. The ability to detect and mitigate fraud in real 
time has become essential for protecting businesses and consumers.  While traditional fraud 
detection  models  have  significantly  contributed  to  the  fight  against  cybercrime,  their 
limitations  often  stem  from  outdated  methodologies,  reliance  on  static  rules,  and  limited 
adaptability to the constantly evolving nature of online fraud. These limitations can lead to 
false positives, delayed detection, and missed fraudulent activities, resulting in both financial 
losses  and  compromised  security.  In  recent  years,  machine  learning  has  emerged  as  a 
powerful tool for enhancing fraud detection systems by leveraging advanced algorithms to 
learn  from  vast  amounts  of  transactional  data.  Machine  learning  models  have  shown 
promising results in improving the accuracy and speed of detecting fraudulent patterns.

*Corresponding author: shahaprasad@gmail.com

---

<!-- PAGE 2 -->

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

However, despite the progress, current models still face several deficiencies, such as handling 
imbalanced  datasets,  adapting  to  new  fraud  schemes,  and  identifying  subtle  transactional 
behavior that could indicate fraud. 
This paper seeks to address these limitations by evaluating the deficiencies and constraints 
of existing online transaction fraud detection models. Additionally, it aims to identify and 
extract key transactional behavior indicators, which could significantly enhance the detection 
process.  By  focusing  on  both  the  weaknesses  of  current  systems  and  the  opportunities 
presented by new approaches, this research intends to provide a more robust and adaptive 
solution to online fraud detection.

1.1 Machine Learning in Fraud Detection

ML has emerged as one of the most transformative technologies in recent years, significantly 
impacting  various  industries  by  automating  processes,  improving  efficiency,  and  enabling 
intelligent  decision-making.  As  a  subset  of  artificial  intelligence  (AI),  machine  learning 
focuses on building systems that learn from data, identify patterns, and make decisions with 
minimal human intervention. Complex algorithms enable machine learning models to evolve 
over time, enhancing their accuracy and adaptability with the introduction of more data. 
In the realm of online financial transactions, fraud detection has become a critical application 
area  for  machine  learning  due  to  the  increasing  sophistication  of  fraudulent  schemes. 
Traditional fraud detection methods, such as rule-based systems, rely heavily on predefined 
rules  and  patterns,  making  them  rigid  and  unable  to  adapt  to  the  ever-evolving  tactics  of 
fraudsters.  Often,  these  systems  lead  to  high  false  positive  rates,  incorrectly  flagging 
legitimate transactions as fraudulent, resulting in customer dissatisfaction and financial losses 
for businesses. 
Machine learning-based fraud detection models, on the other hand, can analyze vast amounts 
of transactional data in real time and uncover hidden patterns indicative of fraud. By learning 
from  historical  fraud  data  and  continuously  adapting  to  new  types  of  fraud,  these  models 
provide a more dynamic and efficient solution. Algorithms such as Decision Trees, Random 
Forests, and Neural Networks allow the detection of both known and unknown fraudulent 
activities by leveraging various features, such as transaction amounts, frequency, location, 
and user behavior. 
With  the  rapid  growth  of  online  financial  transactions,  fraud  detection  has  become 
increasingly critical for businesses and consumers alike. Traditional rule-based systems have 
been the primary method for identifying fraudulent activities, but they often struggle to keep 
up  with  the  sophistication  of  modern  fraud  schemes.  Machine  learning  (ML),  a  subset  of 
artificial  intelligence  (AI),  has  emerged  as  a  powerful  tool  in  combating  these  issues  by 
offering dynamic, adaptable, and data-driven solutions.

1.2 What is Machine Learning?

Machine learning is a branch of AI that focuses on building models capable of learning from 
data.  Unlike  traditional  programming,  which  dictates  actions  with  explicit  instructions, 
machine learning algorithms enhance their performance over time by processing data. This 
capability  to  self-learn  allows  ML  models  to  adapt  to  new  information  without  human 
intervention, making them particularly effective in environments where patterns evolve, such 
as fraud detection.

In  fraud  detection,  machine  learning  models  analyze  vast  amounts  of  transactional  data, 
identifying  patterns  that  indicate  potential  fraud.  These  models  can  automatically  detect

2

anomalies  and  irregularities,  even  in  real  time,  improving  the  speed  and  accuracy  of

identifying fraudulent transactions.

1.3 Limitations of Traditional Fraud Detection Methods

Traditional  fraud  detection  systems  are  typically  rule-based.  They  operate  by  applying

predefined sets of rules to transactional data, such as flagging a transaction if it exceeds a

certain amount or originates from an unfamiliar location. While effective in some cases, rule-

based systems suffer from significant drawbacks:

•  Static Rules: They cannot adapt to new and emerging fraud tactics without manual

updates.

•  High False Positives: Businesses frequently mistakenly flag legitimate transactions

as fraudulent, which leads to customer dissatisfaction and potential revenue loss.

•  Limited  Scalability:  These  systems  struggle  to  manage  large  volumes  of

transactions, especially in real-time applications.

As a result, there is a growing need for more advanced systems that can handle the dynamic

nature of fraud in today’s digital landscape.

1.4 Why Machine Learning is Effective in Fraud Detection

Machine learning offers several advantages over traditional methods in fraud detection:

•  Adaptability: ML models can learn from historical data and update themselves as

new fraud patterns emerge. This ensures that the model is continuously improving

its accuracy without the need for constant human intervention.

•  Real-Time  Detection:  ML  algorithms  can  process  large  volumes  of  data  in  real

time, enabling immediate identification of fraudulent activities as they occur.

•  Reduction of False Positives: By analyzing multiple features of a transaction, such

as  user  behavior,  device  usage,  and  geolocation,  ML  models  can  differentiate

between legitimate and fraudulent transactions with greater precision, thus reducing

the number of false positives.

1.5 Common Machine Learning Techniques in Fraud Detection

Various machine learning techniques are employed to enhance fraud detection capabilities,

including:

•  Decision Trees: A supervised learning technique that divides the data into smaller

subsets based on decision rules. It is particularly useful for classification problems

•  Random  Forests:  An  ensemble  method  that  builds  multiple  decision  trees  to

improve prediction accuracy and reduce overfitting, making it highly effective for

like fraud detection.

complex fraud patterns.

•  Neural  Networks: A  more  advanced  technique  that  mimics  the  workings  of  the

human brain to detect complex, non-linear relationships in data. Neural networks

---

<!-- PAGE 3 -->

However, despite the progress, current models still face several deficiencies, such as handling

imbalanced  datasets,  adapting  to  new  fraud  schemes,  and  identifying  subtle  transactional

anomalies  and  irregularities,  even  in  real  time,  improving  the  speed  and  accuracy  of 
identifying fraudulent transactions.

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

behavior that could indicate fraud.

This paper seeks to address these limitations by evaluating the deficiencies and constraints

of existing online transaction fraud detection models. Additionally, it aims to identify and

extract key transactional behavior indicators, which could significantly enhance the detection

process.  By  focusing  on  both  the  weaknesses  of  current  systems  and  the  opportunities

presented by new approaches, this research intends to provide a more robust and adaptive

solution to online fraud detection.

1.1 Machine Learning in Fraud Detection

ML has emerged as one of the most transformative technologies in recent years, significantly

impacting  various  industries  by  automating  processes,  improving  efficiency,  and  enabling

intelligent  decision-making.  As  a  subset  of  artificial  intelligence  (AI),  machine  learning

focuses on building systems that learn from data, identify patterns, and make decisions with

minimal human intervention. Complex algorithms enable machine learning models to evolve

over time, enhancing their accuracy and adaptability with the introduction of more data.

In the realm of online financial transactions, fraud detection has become a critical application

area  for  machine  learning  due  to  the  increasing  sophistication  of  fraudulent  schemes.

Traditional fraud detection methods, such as rule-based systems, rely heavily on predefined

rules  and  patterns,  making  them  rigid  and  unable  to  adapt  to  the  ever-evolving  tactics  of

fraudsters.  Often,  these  systems  lead  to  high  false  positive  rates,  incorrectly  flagging

legitimate transactions as fraudulent, resulting in customer dissatisfaction and financial losses

for businesses.

Machine learning-based fraud detection models, on the other hand, can analyze vast amounts

of transactional data in real time and uncover hidden patterns indicative of fraud. By learning

from  historical  fraud  data  and  continuously  adapting  to  new  types  of  fraud,  these  models

provide a more dynamic and efficient solution. Algorithms such as Decision Trees, Random

Forests, and Neural Networks allow the detection of both known and unknown fraudulent

activities by leveraging various features, such as transaction amounts, frequency, location,

and user behavior.

With  the  rapid  growth  of  online  financial  transactions,  fraud  detection  has  become

increasingly critical for businesses and consumers alike. Traditional rule-based systems have

been the primary method for identifying fraudulent activities, but they often struggle to keep

up  with  the  sophistication  of  modern  fraud  schemes.  Machine  learning  (ML),  a  subset  of

artificial  intelligence  (AI),  has  emerged  as  a  powerful  tool  in  combating  these  issues  by

offering dynamic, adaptable, and data-driven solutions.

1.2 What is Machine Learning?

Machine learning is a branch of AI that focuses on building models capable of learning from

data.  Unlike  traditional  programming,  which  dictates  actions  with  explicit  instructions,

machine learning algorithms enhance their performance over time by processing data. This

capability  to  self-learn  allows  ML  models  to  adapt  to  new  information  without  human

intervention, making them particularly effective in environments where patterns evolve, such

as fraud detection.

In  fraud  detection,  machine  learning  models  analyze  vast  amounts  of  transactional  data,

identifying  patterns  that  indicate  potential  fraud.  These  models  can  automatically  detect

1.3 Limitations of Traditional Fraud Detection Methods

Traditional  fraud  detection  systems  are  typically  rule-based.  They  operate  by  applying 
predefined sets of rules to transactional data, such as flagging a transaction if it exceeds a 
certain amount or originates from an unfamiliar location. While effective in some cases, rule-
based systems suffer from significant drawbacks:

•  Static Rules: They cannot adapt to new and emerging fraud tactics without manual

updates.

•  High False Positives: Businesses frequently mistakenly flag legitimate transactions 
as fraudulent, which leads to customer dissatisfaction and potential revenue loss. 
•  Limited  Scalability:  These  systems  struggle  to  manage  large  volumes  of

transactions, especially in real-time applications.

As a result, there is a growing need for more advanced systems that can handle the dynamic 
nature of fraud in today’s digital landscape.

1.4 Why Machine Learning is Effective in Fraud Detection

Machine learning offers several advantages over traditional methods in fraud detection:

•  Adaptability: ML models can learn from historical data and update themselves as 
new fraud patterns emerge. This ensures that the model is continuously improving 
its accuracy without the need for constant human intervention.

•  Real-Time  Detection:  ML  algorithms  can  process  large  volumes  of  data  in  real 
time, enabling immediate identification of fraudulent activities as they occur.

•  Reduction of False Positives: By analyzing multiple features of a transaction, such 
as  user  behavior,  device  usage,  and  geolocation,  ML  models  can  differentiate 
between legitimate and fraudulent transactions with greater precision, thus reducing 
the number of false positives.

1.5 Common Machine Learning Techniques in Fraud Detection

Various machine learning techniques are employed to enhance fraud detection capabilities, 
including:

•  Decision Trees: A supervised learning technique that divides the data into smaller 
subsets based on decision rules. It is particularly useful for classification problems 
like fraud detection.

•  Random  Forests:  An  ensemble  method  that  builds  multiple  decision  trees  to 
improve prediction accuracy and reduce overfitting, making it highly effective for 
complex fraud patterns.

•  Neural  Networks: A  more  advanced  technique  that  mimics  the  workings  of  the 
human brain to detect complex, non-linear relationships in data. Neural networks

3

---

<!-- PAGE 4 -->

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

are effective in uncovering subtle fraudulent behavior patterns that simpler models 
may miss.

Each  of  these  techniques  offers  unique  benefits,  but  they  all  share  the  common  goal  of 
improving fraud detection accuracy and minimizing false positives and negatives.

2 Scope of the Study

This study aims to address two key aspects:

1.  Assessing  the  Deficiencies  of  Existing  Models:  By  analyzing  current  fraud 
detection systems, this study will highlight the limitations of traditional methods, 
such as their inability to adapt to evolving fraud techniques and their high rate of 
false positives.

2.  Identifying  Key  Transactional  Behavior  Indicators:  A  major  focus  of  this 
research  will  be  on  extracting  and  analyzing  new  behavioral  indicators,  such  as 
transaction  frequency  and  user  interaction  times,  which  can  help  improve  the 
accuracy of fraud detection models.

By leveraging machine learning techniques, this study aims to overcome the limitations of 
traditional  fraud  detection  systems  and  contribute  to  the  development  of  more  robust  and 
efficient solutions for identifying fraudulent transactions in real time.

3 Literature Review

M. N. Alataw (2024) presents a novel approach to credit card fraud detection in an IoT-driven 
environment.  It  utilizes  advanced  ML  techniques  to  address  the  limitations  of  traditional 
fraud  detection  systems.  The  study  highlights  the  integration  of  IoT  data  and  big  data 
processing to build a real-time fraud detection framework, leveraging various ML models 
such as Random Forest (RF), Gradient Boosting Machine (GBM), and Multilayer Perceptron 
(MLP). The paper demonstrates improved accuracy, precision, recall, and F1 scores in fraud 
detection using these models.

Khyati Kapadiya et al. (2024) highlight the pivotal role of healthcare insurance in providing 
access  to  essential  medical  services  amidst  longer  life  expectancy  and  technological 
advancements while addressing the growing challenge of fraudulent claims that necessitate 
complex  procedures.  It  proposes  an  innovative  solution  combining  ensemble  learning 
techniques, specifically bagging and stacking, with blockchain technology to enhance fraud 
detection in healthcare insurance claims. By leveraging blockchain's decentralized security, 
the approach ensures robust protection of sensitive patient and healthcare data. Additionally, 
the  methodology  integrates  diverse  patient  data  including  in-patient,  out-patient,  and 
beneficiary  information—offering  a  comprehensive  and  practical  solution.  The  study 
compares  it  to  traditional  machine  learning  algorithms  (MLAs)  and  rates  its  performance 
using metrics such as recall, accuracy, precision, ROC, F1-score, and a confusion matrix. It 
also looks at how much it costs to use smart contracts for different purposes. This research 
presents a resilient and efficient framework to combat fraudulent activities, advancing the 
security and effectiveness of healthcare insurance systems.

Ju  Lu  et  al.  (2024)  present  a  scalable,  multi-model  ML  method  for  real-time  intrusion 
detection and secure cryptographic key distribution. Using the large number of IoT devices, 
the suggested ML-based IDS is designed to work in a variety of IoT settings, making it more

4

flexible  and  effective  at  detecting  threats. The  method  improves  the  accuracy  of  intrusion

detection and divides threats into nine different attack types by using Maximum–Minimum

(Max–Min)  normalization  on  datasets  such  as  UNSW-NB15  and  CICIoT2023.

Dimensionality  reduction  via  Principal  Component  Analysis  (PCA)  streamlines  data

processing and boosts efficiency, while six advanced ML models optimize threat detection.

Also, synchronized artificial neural networks (ANNs) are used in a secure key distribution

mechanism to make sure the safe exchange of cryptographic keys, which lowers the risk of

leaks. This new method not only improves real-time intrusion detection, but it also makes

information  management  systems  safer  overall.  It's  a  complete  and  effective  way  to  get

around the problems with current IDS solutions.

P.  Y.  Prasad  and  colleagues  (2023)  conducted  a  comparison  study  to  evaluate  the

effectiveness  of  various  machine  learning  models  in  the  identification  of fraudulent  credit

card  activity.  In  a  similar  vein,  R.  Aggarwal  and  colleagues  (2023)  examined  the

effectiveness of four different machine learning models in the detection of credit card fraud,

providing  insights  into  the  strengths  and  shortcomings  of  each  model  individually.  The

authors,  Fiore  et  al.  (2019),  investigated  the  possibility  of  using  GANs  to  enhance  the

efficiency of categorization in the detection of credit card fraud. Their Information Sciences

research  showcased  the  potential  of  GANs  as  a  supplementary  tool  to  enhance  datasets,

thereby boosting the effectiveness of conventional classifiers in identifying illicit financial

transactions.  Zhang  et  al.  (2018)  proposed  using  CNN  as  the  basis  for  a  model  to  detect

fraudulent activity in online financial transactions. Their strategy made use of CNNs' inherent

capacity  to  automatically  and  dynamically  learn  the  spatial  hierarchies  of  characteristics

underlying raw data.

4. Methodology

This study proposes a systematic approach to identify and address the limitations of existing

fraud  detection  systems  by  leveraging  key  transactional  behavior  indicators  and  advanced

machine  learning  techniques.  The  methodology  is  divided  into  two  primary  phases:  (1)

evaluation  of  current  fraud  detection  models,  and  (2)  development  of  a  hybrid  detection

framework utilizing behavioral insights and a Light Gradient Boosting Machine (LightGBM)

model.

The following actions are being taken to address the first objective, which involves assessing

the shortcomings and limitations of existing fraud detection models:

Literature Review and Model Identification

A  comprehensive  literature  review  was  conducted  to  analyze  prevalent  fraud  detection

methodologies,  including  rule-based  systems,  statistical  approaches,  and  machine  learning

models such as Decision Trees, Random Forests, Support Vector Machines (SVM), Neural

Networks,  and  Logistic  Regression.  This  review  revealed  several  persistent  challenges,

including high false positive rates, limited adaptability to evolving fraud patterns, and poor

performance in real-time environments.

5. Evaluation of Current Fraud Detection Techniques

After  identifying  existing  models,  their  performance  was  assessed  using  the  following

metrics:

•  Accuracy

:

(𝐴𝐴)

---

<!-- PAGE 5 -->

are effective in uncovering subtle fraudulent behavior patterns that simpler models

may miss.

Each  of  these  techniques  offers  unique  benefits,  but  they  all  share  the  common  goal  of

improving fraud detection accuracy and minimizing false positives and negatives.

2 Scope of the Study

This study aims to address two key aspects:

1.  Assessing  the  Deficiencies  of  Existing  Models:  By  analyzing  current  fraud

detection systems, this study will highlight the limitations of traditional methods,

such as their inability to adapt to evolving fraud techniques and their high rate of

false positives.

2.  Identifying  Key  Transactional  Behavior  Indicators:  A  major  focus  of  this

research  will  be  on  extracting  and  analyzing  new  behavioral  indicators,  such  as

transaction  frequency  and  user  interaction  times,  which  can  help  improve  the

accuracy of fraud detection models.

By leveraging machine learning techniques, this study aims to overcome the limitations of

traditional  fraud  detection  systems  and  contribute  to  the  development  of  more  robust  and

efficient solutions for identifying fraudulent transactions in real time.

3 Literature Review

M. N. Alataw (2024) presents a novel approach to credit card fraud detection in an IoT-driven

environment.  It  utilizes  advanced  ML  techniques  to  address  the  limitations  of  traditional

fraud  detection  systems.  The  study  highlights  the  integration  of  IoT  data  and  big  data

processing to build a real-time fraud detection framework, leveraging various ML models

such as Random Forest (RF), Gradient Boosting Machine (GBM), and Multilayer Perceptron

(MLP). The paper demonstrates improved accuracy, precision, recall, and F1 scores in fraud

detection using these models.

Khyati Kapadiya et al. (2024) highlight the pivotal role of healthcare insurance in providing

access  to  essential  medical  services  amidst  longer  life  expectancy  and  technological

advancements while addressing the growing challenge of fraudulent claims that necessitate

complex  procedures.  It  proposes  an  innovative  solution  combining  ensemble  learning

techniques, specifically bagging and stacking, with blockchain technology to enhance fraud

detection in healthcare insurance claims. By leveraging blockchain's decentralized security,

the approach ensures robust protection of sensitive patient and healthcare data. Additionally,

the  methodology  integrates  diverse  patient  data  including  in-patient,  out-patient,  and

beneficiary  information—offering  a  comprehensive  and  practical  solution.  The  study

compares  it  to  traditional  machine  learning  algorithms  (MLAs)  and  rates  its  performance

using metrics such as recall, accuracy, precision, ROC, F1-score, and a confusion matrix. It

also looks at how much it costs to use smart contracts for different purposes. This research

presents a resilient and efficient framework to combat fraudulent activities, advancing the

security and effectiveness of healthcare insurance systems.

Ju  Lu  et  al.  (2024)  present  a  scalable,  multi-model  ML  method  for  real-time  intrusion

detection and secure cryptographic key distribution. Using the large number of IoT devices,

the suggested ML-based IDS is designed to work in a variety of IoT settings, making it more

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

flexible  and  effective  at  detecting  threats. The  method  improves  the  accuracy  of  intrusion 
detection and divides threats into nine different attack types by using Maximum–Minimum 
(Max–Min)  normalization  on  datasets  such  as  UNSW-NB15  and  CICIoT2023. 
Dimensionality  reduction  via  Principal  Component  Analysis  (PCA)  streamlines  data 
processing and boosts efficiency, while six advanced ML models optimize threat detection. 
Also, synchronized artificial neural networks (ANNs) are used in a secure key distribution 
mechanism to make sure the safe exchange of cryptographic keys, which lowers the risk of 
leaks. This new method not only improves real-time intrusion detection, but it also makes 
information  management  systems  safer  overall.  It's  a  complete  and  effective  way  to  get 
around the problems with current IDS solutions.

P.  Y.  Prasad  and  colleagues  (2023)  conducted  a  comparison  study  to  evaluate  the 
effectiveness  of  various  machine  learning  models  in  the  identification  of fraudulent  credit 
card  activity.  In  a  similar  vein,  R.  Aggarwal  and  colleagues  (2023)  examined  the 
effectiveness of four different machine learning models in the detection of credit card fraud, 
providing  insights  into  the  strengths  and  shortcomings  of  each  model  individually.  The 
authors,  Fiore  et  al.  (2019),  investigated  the  possibility  of  using  GANs  to  enhance  the 
efficiency of categorization in the detection of credit card fraud. Their Information Sciences 
research  showcased  the  potential  of  GANs  as  a  supplementary  tool  to  enhance  datasets, 
thereby boosting the effectiveness of conventional classifiers in identifying illicit financial 
transactions.  Zhang  et  al.  (2018)  proposed  using  CNN  as  the  basis  for  a  model  to  detect 
fraudulent activity in online financial transactions. Their strategy made use of CNNs' inherent 
capacity  to  automatically  and  dynamically  learn  the  spatial  hierarchies  of  characteristics 
underlying raw data.

4. Methodology

This study proposes a systematic approach to identify and address the limitations of existing 
fraud  detection  systems  by  leveraging  key  transactional  behavior  indicators  and  advanced 
machine  learning  techniques.  The  methodology  is  divided  into  two  primary  phases:  (1) 
evaluation  of  current  fraud  detection  models,  and  (2)  development  of  a  hybrid  detection 
framework utilizing behavioral insights and a Light Gradient Boosting Machine (LightGBM) 
model. 
 The following actions are being taken to address the first objective, which involves assessing 
the shortcomings and limitations of existing fraud detection models:

Literature Review and Model Identification 
A  comprehensive  literature  review  was  conducted  to  analyze  prevalent  fraud  detection 
methodologies,  including  rule-based  systems,  statistical  approaches,  and  machine  learning 
models such as Decision Trees, Random Forests, Support Vector Machines (SVM), Neural 
Networks,  and  Logistic  Regression.  This  review  revealed  several  persistent  challenges, 
including high false positive rates, limited adaptability to evolving fraud patterns, and poor 
performance in real-time environments.

5. Evaluation of Current Fraud Detection Techniques

After  identifying  existing  models,  their  performance  was  assessed  using  the  following 
metrics:

•  Accuracy

:

(𝐴𝐴)

5

---

<!-- PAGE 6 -->

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

𝐹𝐹𝑇𝑇

:

(𝑇𝑇)

𝑇𝑇𝑇𝑇, 𝑇𝑇𝑇𝑇, 𝐹𝐹𝑇𝑇
•  Precision

𝐴𝐴 =

𝑇𝑇𝑇𝑇 + 𝑇𝑇𝑇𝑇
𝑇𝑇𝑇𝑇 + 𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇 + 𝐹𝐹𝑇𝑇

represent True  Positives, True  Negatives,  False  Positives,  and

where 
False Negatives, respectively.

,  and

•  Recall

:

(𝑅𝑅)

•  F1-Score (F1):

𝑇𝑇 =

𝑇𝑇𝑇𝑇
𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇

𝑅𝑅 =

𝑇𝑇𝑇𝑇
𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇

•  False Positive Rate (

):

𝐹𝐹1 = 2 ⋅

𝑇𝑇 ⋅ 𝑅𝑅
𝑇𝑇 + 𝑅𝑅

𝐹𝐹𝑇𝑇𝑅𝑅

These metrics were compared across various datasets to evaluate model performance under 
different transaction types and fraud schemes.

𝐹𝐹𝑇𝑇𝑅𝑅 =

𝐹𝐹𝑇𝑇
𝐹𝐹𝑇𝑇 + 𝑇𝑇𝑇𝑇

Identification of Deficiencies

5.1.2. Feature Engineering and Extraction

Based  on  the  metrics  above,  the  weaknesses  of  each  model  were  documented.  These 
included:

•  High False Positive Rates, leading to customer dissatisfaction. 
•  Poor Adaptability to new fraud schemes in dynamic environments. 
•  Slow Real-Time Processing of high transaction volumes. 
•  Limited Feature Scope, with reliance on basic transactional attributes.

5.1 Identifying and Extracting Key Transactional Behavior Indicators

For  the  second  objective,  the  methodology  focused  on  identifying  critical  indicators  to 
improve fraud detection models by capturing sophisticated transactional behavior patterns:

5.1.1 Data Collection and Preprocessing

The dataset used in this study is the Kaggle Credit Card Fraud Detection Dataset [1], which 
contains 284,807 transactions from European cardholders. Among these, 492 transactions are 
fraudulent, making the dataset highly imbalanced. Key features include time, amount, and 
anonymized variables V1–V28 derived via PCA, along with the target variable Class, where 
1 indicates fraud.

Key characteristics of the dataset:

6

•  Attributes: Includes anonymized features (V1–V28), Time, Amount, and the binary

class label Class (0 for genuine, 1 for fraud).

•  Reasons for selection: The dataset is publicly available, highly imbalanced (ideal

for fraud detection benchmarking), and includes transaction timing and monetary

features suitable for behavioral pattern extraction.

norm

𝑋𝑋

=

and

𝑋𝑋 − 𝑋𝑋min

𝑋𝑋max − 𝑋𝑋min

𝑋𝑋min

𝑋𝑋max

where

was  a  feature,  and

were  its  minimum  and  maximum  values,

Imbalanced  Data  Handling:  The  Synthetic  Minority  Oversampling  Technique

(SMOTE) [2] was applied to the training set to generate synthetic examples for the

Preprocessing Steps:

•  Normalization:

respectively.

𝑋𝑋

•

where

value.

𝑋𝑋𝑖𝑖

𝑋𝑋𝑘𝑘

minority (fraudulent) class:

new

and

were  two  samples  from  the  minority  class,  and

= 𝑋𝑋𝑖𝑖 + 𝛿𝛿 ⋅ (𝑋𝑋𝑘𝑘 − 𝑋𝑋𝑖𝑖) 𝛿𝛿 ∈ [0,1]

𝑋𝑋

was  a  random

•  Train-Test Split: The dataset was partitioned into 80% training and 20% testing sets

using stratified sampling to maintain class proportions.

𝛿𝛿 ∈ [0,1]

To enhance model learning, feature engineering was performed as follows:

•  Principal Component Analysis (PCA) was applied:

Dimensionality  reduction  was  applied  to  the  anonymized  variables  to  capture

maximum  variance  and  reduce  noise.  This  approach  helps  mitigate  noise  and

multicollinearity, which are common in high-dimensional datasets. By capturing the

principal  components  that  explain  the  majority  of  variance,  PCA  also  improves

model training efficiency and interpretability.

where

was the feature matrix, and

𝑍𝑍 = 𝑋𝑋 ⋅ 𝑊𝑊

was the matrix of principal components.

•  Recursive  Feature  Elimination  (RFE)  was  used  to  iteratively  remove  features

𝑊𝑊

𝑋𝑋

based  on  their  importance  until  the  optimal  set  was  achieved.  RFE  iteratively

removes  the  least  important  features  based  on  model  performance,  allowing  the

selection of an optimal subset that contributes meaningfully to fraud detection. This

reduces  the  risk  of  overfitting  and  enhances  model  generalization  across  unseen

data.

Key transactional indicators were identified, including:

---

<!-- PAGE 7 -->

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

•  Attributes: Includes anonymized features (V1–V28), Time, Amount, and the binary

class label Class (0 for genuine, 1 for fraud).

•  Reasons for selection: The dataset is publicly available, highly imbalanced (ideal 
for fraud detection benchmarking), and includes transaction timing and monetary 
features suitable for behavioral pattern extraction.

Preprocessing Steps:

•  Normalization:

𝑋𝑋

was  a  feature,  and

where 
respectively.

norm

=

𝑋𝑋
  and

𝑋𝑋 − 𝑋𝑋min
𝑋𝑋max − 𝑋𝑋min

were  its  minimum  and  maximum  values,

𝑋𝑋min

𝑋𝑋max

where

,  and

represent True  Positives, True  Negatives,  False  Positives,  and

𝑇𝑇𝑇𝑇 + 𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇 + 𝐹𝐹𝑇𝑇

𝑇𝑇𝑇𝑇 + 𝑇𝑇𝑇𝑇

𝐴𝐴 =

False Negatives, respectively.

𝑇𝑇𝑇𝑇, 𝑇𝑇𝑇𝑇, 𝐹𝐹𝑇𝑇

𝐹𝐹𝑇𝑇

•  Precision

:

(𝑇𝑇)

•  Recall

:

(𝑅𝑅)

•  F1-Score (F1):

𝑇𝑇 =

𝑇𝑇𝑇𝑇

𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇

𝑇𝑇𝑇𝑇

𝑅𝑅 =

𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇

•  False Positive Rate (

):

𝐹𝐹1 = 2 ⋅

𝑇𝑇 ⋅ 𝑅𝑅

𝑇𝑇 + 𝑅𝑅

𝐹𝐹𝑇𝑇𝑅𝑅

𝐹𝐹𝑇𝑇

𝐹𝐹𝑇𝑇𝑅𝑅 =

Identification of Deficiencies

included:

•  High False Positive Rates, leading to customer dissatisfaction.

•  Poor Adaptability to new fraud schemes in dynamic environments.

•  Slow Real-Time Processing of high transaction volumes.

•  Limited Feature Scope, with reliance on basic transactional attributes.

5.1 Identifying and Extracting Key Transactional Behavior Indicators

For  the  second  objective,  the  methodology  focused  on  identifying  critical  indicators  to

improve fraud detection models by capturing sophisticated transactional behavior patterns:

5.1.1 Data Collection and Preprocessing

The dataset used in this study is the Kaggle Credit Card Fraud Detection Dataset [1], which

contains 284,807 transactions from European cardholders. Among these, 492 transactions are

fraudulent, making the dataset highly imbalanced. Key features include time, amount, and

anonymized variables V1–V28 derived via PCA, along with the target variable Class, where

1 indicates fraud.

Key characteristics of the dataset:

•

Imbalanced  Data  Handling:  The  Synthetic  Minority  Oversampling  Technique 
(SMOTE) [2] was applied to the training set to generate synthetic examples for the 
minority (fraudulent) class:

new

were  two  samples  from  the  minority  class,  and

= 𝑋𝑋𝑖𝑖 + 𝛿𝛿 ⋅ (𝑋𝑋𝑘𝑘 − 𝑋𝑋𝑖𝑖) 𝛿𝛿 ∈ [0,1]

𝑋𝑋

where 
value.

and

𝑋𝑋𝑖𝑖

𝑋𝑋𝑘𝑘

was  a  random

𝛿𝛿 ∈ [0,1]

These metrics were compared across various datasets to evaluate model performance under

𝐹𝐹𝑇𝑇 + 𝑇𝑇𝑇𝑇

different transaction types and fraud schemes.

•  Train-Test Split: The dataset was partitioned into 80% training and 20% testing sets

using stratified sampling to maintain class proportions.

Based  on  the  metrics  above,  the  weaknesses  of  each  model  were  documented.  These

To enhance model learning, feature engineering was performed as follows:

5.1.2. Feature Engineering and Extraction

•  Principal Component Analysis (PCA) was applied:

Dimensionality  reduction  was  applied  to  the  anonymized  variables  to  capture 
maximum  variance  and  reduce  noise.  This  approach  helps  mitigate  noise  and 
multicollinearity, which are common in high-dimensional datasets. By capturing the 
principal  components  that  explain  the  majority  of  variance,  PCA  also  improves 
model training efficiency and interpretability.

where

was the feature matrix, and

𝑍𝑍 = 𝑋𝑋 ⋅ 𝑊𝑊

was the matrix of principal components.

𝑋𝑋

𝑊𝑊

•  Recursive  Feature  Elimination  (RFE)  was  used  to  iteratively  remove  features 
based  on  their  importance  until  the  optimal  set  was  achieved.  RFE  iteratively 
removes  the  least  important  features  based  on  model  performance,  allowing  the 
selection of an optimal subset that contributes meaningfully to fraud detection. This 
reduces  the  risk  of  overfitting  and  enhances  model  generalization  across  unseen 
data.

Key transactional indicators were identified, including:

7

---

<!-- PAGE 8 -->

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

Behavioral Patterns (

:

https://doi.org/10.1051/epjconf/202532801003

Sum of Transactions in Time Window 
𝐵𝐵𝐵𝐵)
 Time Window

•  Device and Location Consistency: Frequency of device or location changes were

𝐵𝐵𝐵𝐵 =

tracked as

freq  and

freq .

•  User Interaction Time (UT): 
𝐷𝐷

𝐿𝐿

end

start

6 MACHINE LEARNING MODEL DEVELOPMENT

𝑈𝑈𝑈𝑈 = 𝑈𝑈

− 𝑈𝑈

1) Proposed Model: LightGBM-Based Hybrid Approach 
The  core  model  of  this  study  is  a  Light  Gradient  Boosting  Machine  (LightGBM)  [3], 
selected for its high performance in handling large-scale, imbalanced data. It employs leaf-
wise tree growth, resulting in faster convergence and better accuracy compared to level-wise 
methods. Key benefits include:

•  Native support for categorical features 
•  Efficient memory usage 
•  Built-in support for imbalance handling (via parameter scale_pos_weight)

2) Baseline Models for Comparison 
To  benchmark  the  performance  of  the  proposed  model,  the  following  classical  machine 
learning models were implemented: 
•  Logistic Regression 
•  Decision Trees 
•  Random Forest 
•  Support Vector Machines (SVM) 
•  Artificial Neural Networks (ANN)

4. Model Testing and Evaluation

•  The models were evaluated using met

such as  ROC-AUC and tested for real-

time performance with high transaction volumes.

•  A  comparative  analysis  was  conducted  to  determine  the  impact  of  the  key

rics

transactional indicators on model performance.

7 Results and Discussion

This  section  presents  the  evaluation  outcomes  of  the  proposed  hybrid  fraud  detection 
framework, which incorporates behavioral indicators with a LightGBM model. Performance 
comparisons were made with classical machine learning models using standardized metrics 
and statistical validation. The study also highlights the significance of engineered features, 
particularly  behavioral  patterns,  and  assesses  the  model's  applicability  in  real-time  fraud 
detection environments.

7. 1 Model Performance Comparison

To  evaluate  model  effectiveness,  six  classifiers—Logistic  Regression,  Decision  Tree, 
Random Forest, SVM, Artificial Neural Network (ANN), and the proposed LightGBM-were 
assessed on the preprocessed Kaggle Credit Card Fraud Detection dataset. Evaluation metrics 
included Accuracy, Precision, Recall, F1-Score, False Positive Rate (FPR), and ROC-AUC, 
as shown in Table 1.

8

Table 1: Performance Metrics Comparison Across Models

Model

Accuracy  Precision  Recall  F1-Score  FPR  ROC-AUC

Logistic Regression

0.948

0.723

0.791

0.755

0.018

0.943

Decision Tree

0.951

0.759

0.803

0.780

0.015

0.949

Random Forest

0.967

0.842

0.873

0.857

0.010

0.970

SVM

0.958

0.802

0.812

0.807

0.013

0.958

ANN

0.963

0.827

0.849

0.838

0.011

0.965

LightGBM (Proposed)

0.976

0.891

0.914

0.902

0.006

0.981

Fig 1: Comparison of results

7.2 ROC Curve and Model Discrimination

The ROC curves shown in Fig 1 illustrate the trade-off between the True Positive Rate and

False Positive Rate for each model. The LightGBM model yielded the highest ROC-AUC

value (0.981), validating its superior discriminative ability in differentiating between genuine

and fraudulent transactions.

---

<!-- PAGE 9 -->

Behavioral Patterns (

:

Table 1: Performance Metrics Comparison Across Models

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

Sum of Transactions in Time Window

𝐵𝐵𝐵𝐵)

Time Window

•  Device and Location Consistency: Frequency of device or location changes were

𝐵𝐵𝐵𝐵 =

tracked as

freq  and

freq .

•  User Interaction Time (UT):

𝐷𝐷

𝐿𝐿

end

start

6 MACHINE LEARNING MODEL DEVELOPMENT

𝑈𝑈𝑈𝑈 = 𝑈𝑈

− 𝑈𝑈

1) Proposed Model: LightGBM-Based Hybrid Approach

The  core  model  of  this  study  is  a  Light  Gradient  Boosting  Machine  (LightGBM)  [3],

selected for its high performance in handling large-scale, imbalanced data. It employs leaf-

wise tree growth, resulting in faster convergence and better accuracy compared to level-wise

methods. Key benefits include:

•  Native support for categorical features

•  Efficient memory usage

•  Built-in support for imbalance handling (via parameter scale_pos_weight)

2) Baseline Models for Comparison

To  benchmark  the  performance  of  the  proposed  model,  the  following  classical  machine

learning models were implemented:

•  Logistic Regression

•  Decision Trees

•  Random Forest

•  Support Vector Machines (SVM)

•  Artificial Neural Networks (ANN)

4. Model Testing and Evaluation

•  The models were evaluated using met

such as  ROC-AUC and tested for real-

time performance with high transaction volumes.

•  A  comparative  analysis  was  conducted  to  determine  the  impact  of  the  key

rics

transactional indicators on model performance.

7 Results and Discussion

This  section  presents  the  evaluation  outcomes  of  the  proposed  hybrid  fraud  detection

framework, which incorporates behavioral indicators with a LightGBM model. Performance

comparisons were made with classical machine learning models using standardized metrics

and statistical validation. The study also highlights the significance of engineered features,

particularly  behavioral  patterns,  and  assesses  the  model's  applicability  in  real-time  fraud

detection environments.

7. 1 Model Performance Comparison

To  evaluate  model  effectiveness,  six  classifiers—Logistic  Regression,  Decision  Tree,

Random Forest, SVM, Artificial Neural Network (ANN), and the proposed LightGBM-were

assessed on the preprocessed Kaggle Credit Card Fraud Detection dataset. Evaluation metrics

included Accuracy, Precision, Recall, F1-Score, False Positive Rate (FPR), and ROC-AUC,

as shown in Table 1.

Model

Accuracy  Precision  Recall  F1-Score  FPR  ROC-AUC

Logistic Regression

0.948

0.723

0.791

0.755

0.018

0.943

Decision Tree

0.951

0.759

0.803

0.780

0.015

0.949

Random Forest

0.967

0.842

0.873

0.857

0.010

0.970

SVM

0.958

0.802

0.812

0.807

0.013

0.958

ANN

0.963

0.827

0.849

0.838

0.011

0.965

LightGBM (Proposed)

0.976

0.891

0.914

0.902

0.006

0.981

Fig 1: Comparison of results

7.2 ROC Curve and Model Discrimination

The ROC curves shown in Fig 1 illustrate the trade-off between the True Positive Rate and 
False Positive Rate for each model. The LightGBM model yielded the highest ROC-AUC 
value (0.981), validating its superior discriminative ability in differentiating between genuine 
and fraudulent transactions.

9

---

<!-- PAGE 10 -->

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

Fig 2. ROC Curve Comparison of Fraud Detection Models

7.3 Real-Time Viability and Runtime Performance

A runtime analysis was conducted to assess the efficiency of each model. Table 2 displays 
the average prediction time per transaction for each model, measured on a system with Intel 
i7 CPU, 16 GB RAM.

Table 2: Average Prediction Time Per Transaction

Model

Avg Prediction Time (ms)

0.32

0.47

1.25

3.12

Logistic Regression

Decision Tree

Random Forest

SVM

ANN

5.78

LightGBM

0.58

LightGBM maintained a strong balance between low latency (0.58 ms) and high predictive 
accuracy, making it well-suited for deployment in real-time fraud detection systems.

10

7.4 Discussion and Implications

•  Superior  Detection  Performance: The  LightGBM-based  framework  outperformed

all  baseline  models  in  recall  (91.4%)  and  F1-score  (90.2%),  crucial  for  detecting

fraudulent activities without overwhelming the system with false alarms.

•  Behavioral  Feature  Engineering:  The  contribution  of  behavioral  attributes

significantly  enhanced  the  model’s  ability  to  detect  anomalies. This  suggests  that

capturing temporal, spatial, and interaction-based patterns is a promising direction

•  Statistical  Robustness:  The  statistical  significance  of  the  model  improvements

reinforces  the  reliability  of  findings,  ensuring  the  model’s  superiority  is  not  by

for fraud analytics.

chance.

•  Scalability: Given its low computational cost and strong performance, LightGBM

is ideal for high-volume transactional environments such as banking, e-commerce,

and fintech platforms.

8 Conclusion

This study evaluated the effectiveness of machine learning models in fraud detection, with a

specific  focus  on  the  integration  of  behavioral  indicators.  The  results  demonstrated  that

LightGBM  outperformed  other models  in  terms  of  accuracy,  precision, recall,  and  overall

fraud  detection  capability,  making  it  a  highly  efficient  and  scalable  solution  for  real-time

fraud  detection.  The  inclusion  of  behavioral  indicators  significantly  enhanced  model

performance,  reinforcing  the  importance  of  feature  selection  in  fraud  analytics.  Beyond

performance  analysis,  this  research  also  addressed  practical  implementation  challenges,

including computational efficiency, deployment feasibility, and dataset biases. The findings

emphasize the need for real-time adaptability in financial fraud prevention and suggest that

future research should explore hybrid models incorporating deep learning and explainable AI

techniques to further enhance fraud detection transparency. While this study provides a strong

foundation for ML-based fraud detection, limitations such as dataset representativeness and

model generalizability must be addressed in future work. A comparative analysis with state-

of-the-art fraud detection methods in real-world financial systems will further validate the

proposed approach. Ultimately, this research contributes to the advancement of data-driven

fraud detection strategies, offering a practical pathway for financial institutions to strengthen

security measures.

REFERENCES

1.  Dal Pozzolo, O. Caelen, Y. Le Borgne, S. Waterschoot, and G. Bontempi, "Credit Card

Fraud  Detection:  A  Realistic  Modeling  and  a  Novel  Learning  Strategy,"  IEEE

Transactions on Neural Networks and Learning Systems, 2015. Dataset: Kaggle

2.  N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, "SMOTE: Synthetic

Minority  Over-sampling Technique,"  Journal  of Artificial Intelligence Research,  vol.

3.  G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, et al., "LightGBM: A Highly Efficient

Gradient Boosting Decision Tree," Advances in Neural Information Processing

16, pp. 321–357, 2002.

Systems, 2017.

4.  Mohammed Naif Alatawi, "Detection of fraud in IoT based credit card collected dataset

using machine learning", Machine Learning with Applications, 2024, 1-16.

5.  Khyati  Kapadiya,  Fenil  Ramoliya,  Keyaba  Gohil,  Usha  Patel,  Rajesh  Gupta,  Sudeep

Tanwar,  Joel  J.P.C.  Rodrigues,  "Blockchain-assisted  healthcare  insurance  fraud

---

<!-- PAGE 11 -->

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

7.4 Discussion and Implications

https://doi.org/10.1051/epjconf/202532801003

•  Superior  Detection  Performance: The  LightGBM-based  framework  outperformed 
all  baseline  models  in  recall  (91.4%)  and  F1-score  (90.2%),  crucial  for  detecting 
fraudulent activities without overwhelming the system with false alarms.

•  Behavioral  Feature  Engineering:  The  contribution  of  behavioral  attributes 
significantly  enhanced  the  model’s  ability  to  detect  anomalies. This  suggests  that 
capturing temporal, spatial, and interaction-based patterns is a promising direction 
for fraud analytics.

•  Statistical  Robustness:  The  statistical  significance  of  the  model  improvements 
reinforces  the  reliability  of  findings,  ensuring  the  model’s  superiority  is  not  by 
chance.

•  Scalability: Given its low computational cost and strong performance, LightGBM 
is ideal for high-volume transactional environments such as banking, e-commerce, 
and fintech platforms.

8 Conclusion

This study evaluated the effectiveness of machine learning models in fraud detection, with a 
specific  focus  on  the  integration  of  behavioral  indicators.  The  results  demonstrated  that 
LightGBM  outperformed  other models  in  terms  of  accuracy,  precision, recall,  and  overall 
fraud  detection  capability,  making  it  a  highly  efficient  and  scalable  solution  for  real-time 
fraud  detection.  The  inclusion  of  behavioral  indicators  significantly  enhanced  model 
performance,  reinforcing  the  importance  of  feature  selection  in  fraud  analytics.  Beyond 
performance  analysis,  this  research  also  addressed  practical  implementation  challenges, 
including computational efficiency, deployment feasibility, and dataset biases. The findings 
emphasize the need for real-time adaptability in financial fraud prevention and suggest that 
future research should explore hybrid models incorporating deep learning and explainable AI 
techniques to further enhance fraud detection transparency. While this study provides a strong 
foundation for ML-based fraud detection, limitations such as dataset representativeness and 
model generalizability must be addressed in future work. A comparative analysis with state-
of-the-art fraud detection methods in real-world financial systems will further validate the 
proposed approach. Ultimately, this research contributes to the advancement of data-driven 
fraud detection strategies, offering a practical pathway for financial institutions to strengthen 
security measures.

REFERENCES

1.  Dal Pozzolo, O. Caelen, Y. Le Borgne, S. Waterschoot, and G. Bontempi, "Credit Card 
Fraud  Detection:  A  Realistic  Modeling  and  a  Novel  Learning  Strategy,"  IEEE 
Transactions on Neural Networks and Learning Systems, 2015. Dataset: Kaggle 
2.  N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, "SMOTE: Synthetic 
Minority  Over-sampling Technique,"  Journal  of Artificial Intelligence Research,  vol. 
16, pp. 321–357, 2002.

3.  G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, et al., "LightGBM: A Highly Efficient 
Gradient Boosting Decision Tree," Advances in Neural Information Processing 
Systems, 2017.

4.  Mohammed Naif Alatawi, "Detection of fraud in IoT based credit card collected dataset

using machine learning", Machine Learning with Applications, 2024, 1-16.

5.  Khyati  Kapadiya,  Fenil  Ramoliya,  Keyaba  Gohil,  Usha  Patel,  Rajesh  Gupta,  Sudeep 
Tanwar,  Joel  J.P.C.  Rodrigues,  "Blockchain-assisted  healthcare  insurance  fraud

11

Fig 2. ROC Curve Comparison of Fraud Detection Models

7.3 Real-Time Viability and Runtime Performance

A runtime analysis was conducted to assess the efficiency of each model. Table 2 displays

the average prediction time per transaction for each model, measured on a system with Intel

i7 CPU, 16 GB RAM.

Table 2: Average Prediction Time Per Transaction

Model

Avg Prediction Time (ms)

0.32

0.47

1.25

3.12

Logistic Regression

Decision Tree

Random Forest

SVM

ANN

5.78

LightGBM

0.58

LightGBM maintained a strong balance between low latency (0.58 ms) and high predictive

accuracy, making it well-suited for deployment in real-time fraud detection systems.

---

<!-- PAGE 12 -->

EPJ Web of Conferences 328, 01003 (2025) 
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

detection framework using ensemble learning", Computers and Electrical Engineering, 
122, 2024.

6.  Ju  Lu, Arindam  Bhar,   Arindam  Sarkar, Abdulfattah  Noorwali,  Kamal  M.  Othman, 
"Enhancing real-time intrusion detection and secure key distribution using multi-model 
machine learning approach for mitigating confidentiality threats", Internet of things, 28, 
2024.

7.  P. Y. Prasad, A. S. Chowdary, C. Bavitha, E. Mounisha and C. Reethika, "A Comparison 
Study of Fraud Detection in Usage of Credit Cards using Machine Learning," 2023 7th 
International Conference on Trends in Electronics and Informatics (ICOEI), Tirunelveli, 
India, 2023, pp. 1204-1209, doi: 10.1109/ICOEI56765.2023.10125838.

8.  R. Aggarwal, P. K. Sarangi and A. K. Sahoo, "Credit Card Fraud Detection: Analyzing 
the Performance of Four Machine Learning Models," 2023 International Conference on 
Disruptive  Technologies  (ICDT),  Greater  Noida,  India,  2023,  pp.  650-654,  doi: 
10.1109/ICDT57929.2023.10150782.

9.  G.  M.  Suhas  Jain,  N.  Rakesh,  K.  Pranavi  and  L. Bale,  "A  Novel Approach  in  Credit 
Card Fraud Detection System Using Machine Learning Techniques," 2021 International 
Conference  on  Forensics,  Analytics,  Big  Data,  Security  (FABS),  Bengaluru,  India, 
2021, pp. 1-5, doi: 10.1109/FABS52071.2021.9702672.

10.  J.  Chaquet-ulldemolins,  S.  Moral-rubio,  S.  Mu˜  noz-romero,  On  the  black-box 
challenge  for  fraud  detection  using  machine  learning  (II):  nonlinear  analysis  through 
interpretable autoencoders, Appl. Sci. 12 (2022) 3856

11.  W.  Hilal,  S.A.  Gadsden,  J. Yawney,  Financial  fraud:  a  review  of  anomaly  detection

techniques and recent advances, Expert Syst. Appl. 193 (2021)

12.  M.N. Ashtiani,  B.  Raahemi,  Intelligent  fraud  detection  in  financial  statements  using 
machine  learning  and  data  mining:  a  systematic  literature  review,  IEEE  Access  10 
(2021) 72504–72525

13.  K.G.  Al-Hashedi,  P.  Magalingam,  Financial  fraud  detection  applying  data  mining 
techniques: a comprehensive review from 2009 to 2019, Comput. Sci. Rev. 40 (2021) 
14.  Ramkumar Jayaraman, Mohammed Alshehri, Manoj Kumar, Ahed Abugabah, Surender 
Singh  Samant,  Ahmed  A.  Mohamed,  Secure  biomedical  document  protection 
framework to ensure privacy through blockchain, Big Data 11 (6) (2023) 437–451.  
15.  Devandar  Rao,  Ramkumar  Jayaraman,  A  Novel  Quantum  Identity  Authentication 
protocol  without  entanglement  and  preserving  pre-shared  key  information,  Quantum 
Information Processing, Springer 22 (2023). Article No. 92.

16.  Faisal,  N.  A.,  Nahar,  J.,  Sultana,  N.,  &  Mintoo,  A.  A.  (2024).  Fraud  Detection  In 
Banking  Leveraging Ai To  Identify And  Prevent Fraudulent Activities  In  Real-Time. 
Journal of Machine Learning, Data Engineering and Data Science, 1(01), 181-197. 
17.  Oluwole,  V.,  2024.  4 African  countries  with  highest  scam  losses  in  2024.  Business 
Insider Africa.  https://africa.businessinsider.com/local/markets/african-countries-with- 
highest-scam-losses/wrvpj5k (Accessed 15 December 2024).

18.  Sharma,  R.,  Mehta,  K., Sharma,  P.,  2024.  Role  of  artificial  intelligence  and  machine 
learning  in  fraud  detection  and  prevention.  In:  Risks  and  Challenges  of  AI-Driven 
Finance: Bias, Ethics, and Security. IGI Global, pp. 90–120.

19.  Theodorakopoulos,  L.,  Theodoropoulou,  A.,  Stamatiou,  Y.,  2024.  A  state-of-the-art 
review  in  big  data  management  engineering:  real-life  case  studies,  challenges,  and 
future research directions. Eng 5 (3), 1266–1297.

20.  Takyar,  A.,  2024.  Financial  fraud  detection  using  machine  learning  models. 
https://www.leewayhertz.com/build-financial-fraud-detection-system-using-ML-
models/ (Accessed 19 March 2024).

12

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

01003

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

Enhancing  Online  Fraud  Detection:  Leveraging
Machine  Learning  and  Behavioral  Indicators  for
Improved Accuracy and Real-Time Detection

Prasad Shaha1*, Vidya Gavekar2

1School of Management & Research, Dr. D. Y. Patil Dnyan Prasad University's School of
Management & Research, Pune, Maharashtra, India
2 Surydatta Institute of Management and Mass Communication, Pune, Maharashtra, India

Abstract - Fraud detection remains a critical challenge in financial security,
requiring  robust  and  efficient  methodologies  to  identify  fraudulent
transactions accurately. This study presents a comprehensive evaluation of
machine learning (ML) models for fraud detection, emphasizing the role of
behavioral  indicators  in  enhancing  model  performance.  A  comparative
analysis  of  traditional  and  advanced  ML  models,  including  Logistic
Regression,  Decision  Tree,  Random  Forest,  Support  Vector  Machine
(SVM), Artificial Neural Networks (ANN), and LightGBM, was conducted
using real-world fraud detection datasets. LightGBM, the proposed model,
outperformed other methods, achieving the highest ROC-AUC (0.981), F1-
score  (0.902),  and  lowest  false  positive  rate  (0.006).  The  study  also
highlights the importance of feature selection, class imbalance handling, and
real-world  applicability  by  discussing  computational  efficiency  and
deployment  challenges. These  findings  contribute to  the  growing body of
fraud detection research by offering a practical, scalable, and high-accuracy
ML approach for real-time fraud prevention systems.

1 Introduction

As  e-commerce  and  online  financial  transactions  continue  to  expand,  the  prevalence  of
fraudulent activities has grown significantly. The ability to detect and mitigate fraud in real
time has become essential for protecting businesses and consumers.  While traditional fraud
detection  models  have  significantly  contributed  to  the  fight  against  cybercrime,  their
limitations  often  stem  from  outdated  methodologies,  reliance  on  static  rules,  and  limited
adaptability to the constantly evolving nature of online fraud. These limitations can lead to
false positives, delayed detection, and missed fraudulent activities, resulting in both financial
losses  and  compromised  security.  In  recent  years,  machine  learning  has  emerged  as  a
powerful tool for enhancing fraud detection systems by leveraging advanced algorithms to
learn  from  vast  amounts  of  transactional  data.  Machine  learning  models  have  shown
promising results in improving the accuracy and speed of detecting fraudulent patterns.

*Corresponding author: shahaprasad@gmail.com

© The Authors, published by EDP Sciences. This is an open access article distributed under the terms of the Creative Commons Attribution License 4.0 (https://creativecommons.org/licenses/by/4.0/).

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

However, despite the progress, current models still face several deficiencies, such as handling
imbalanced  datasets,  adapting  to  new  fraud  schemes,  and  identifying  subtle  transactional
behavior that could indicate fraud.
This paper seeks to address these limitations by evaluating the deficiencies and constraints
of existing online transaction fraud detection models. Additionally, it aims to identify and
extract key transactional behavior indicators, which could significantly enhance the detection
process.  By  focusing  on  both  the  weaknesses  of  current  systems  and  the  opportunities
presented by new approaches, this research intends to provide a more robust and adaptive
solution to online fraud detection.

1.1 Machine Learning in Fraud Detection

ML has emerged as one of the most transformative technologies in recent years, significantly
impacting  various  industries  by  automating  processes,  improving  efficiency,  and  enabling
intelligent  decision-making.  As  a  subset  of  artificial  intelligence  (AI),  machine  learning
focuses on building systems that learn from data, identify patterns, and make decisions with
minimal human intervention. Complex algorithms enable machine learning models to evolve
over time, enhancing their accuracy and adaptability with the introduction of more data.
In the realm of online financial transactions, fraud detection has become a critical application
area  for  machine  learning  due  to  the  increasing  sophistication  of  fraudulent  schemes.
Traditional fraud detection methods, such as rule-based systems, rely heavily on predefined
rules  and  patterns,  making  them  rigid  and  unable  to  adapt  to  the  ever-evolving  tactics  of
fraudsters.  Often,  these  systems  lead  to  high  false  positive  rates,  incorrectly  flagging
legitimate transactions as fraudulent, resulting in customer dissatisfaction and financial losses
for businesses.
Machine learning-based fraud detection models, on the other hand, can analyze vast amounts
of transactional data in real time and uncover hidden patterns indicative of fraud. By learning
from  historical  fraud  data  and  continuously  adapting  to  new  types  of  fraud,  these  models
provide a more dynamic and efficient solution. Algorithms such as Decision Trees, Random
Forests, and Neural Networks allow the detection of both known and unknown fraudulent
activities by leveraging various features, such as transaction amounts, frequency, location,
and user behavior.
With  the  rapid  growth  of  online  financial  transactions,  fraud  detection  has  become
increasingly critical for businesses and consumers alike. Traditional rule-based systems have
been the primary method for identifying fraudulent activities, but they often struggle to keep
up  with  the  sophistication  of  modern  fraud  schemes.  Machine  learning  (ML),  a  subset  of
artificial  intelligence  (AI),  has  emerged  as  a  powerful  tool  in  combating  these  issues  by
offering dynamic, adaptable, and data-driven solutions.

1.2 What is Machine Learning?

 Machine learning is a branch of AI that focuses on building models capable of learning from
data.  Unlike  traditional  programming,  which  dictates  actions  with  explicit  instructions,
machine learning algorithms enhance their performance over time by processing data. This
capability  to  self-learn  allows  ML  models  to  adapt  to  new  information  without  human
intervention, making them particularly effective in environments where patterns evolve, such
as fraud detection.

In  fraud  detection,  machine  learning  models  analyze  vast  amounts  of  transactional  data,
identifying  patterns  that  indicate  potential  fraud.  These  models  can  automatically  detect

2

anomalies  and  irregularities,  even  in  real  time,  improving  the  speed  and  accuracy  of

identifying fraudulent transactions.

1.3 Limitations of Traditional Fraud Detection Methods

 Traditional  fraud  detection  systems  are  typically  rule-based.  They  operate  by  applying

predefined sets of rules to transactional data, such as flagging a transaction if it exceeds a

certain amount or originates from an unfamiliar location. While effective in some cases, rule-

based systems suffer from significant drawbacks:

•  Static Rules: They cannot adapt to new and emerging fraud tactics without manual

updates.

•  High False Positives: Businesses frequently mistakenly flag legitimate transactions

as fraudulent, which leads to customer dissatisfaction and potential revenue loss.

•  Limited  Scalability:  These  systems  struggle  to  manage  large  volumes  of

transactions, especially in real-time applications.

As a result, there is a growing need for more advanced systems that can handle the dynamic

nature of fraud in today’s digital landscape.

1.4 Why Machine Learning is Effective in Fraud Detection

Machine learning offers several advantages over traditional methods in fraud detection:

•  Adaptability: ML models can learn from historical data and update themselves as

new fraud patterns emerge. This ensures that the model is continuously improving

its accuracy without the need for constant human intervention.

•  Real-Time  Detection:  ML  algorithms  can  process  large  volumes  of  data  in  real

time, enabling immediate identification of fraudulent activities as they occur.

•  Reduction of False Positives: By analyzing multiple features of a transaction, such

as  user  behavior,  device  usage,  and  geolocation,  ML  models  can  differentiate

between legitimate and fraudulent transactions with greater precision, thus reducing

the number of false positives.

1.5 Common Machine Learning Techniques in Fraud Detection

Various machine learning techniques are employed to enhance fraud detection capabilities,

including:

•  Decision Trees: A supervised learning technique that divides the data into smaller

subsets based on decision rules. It is particularly useful for classification problems

•  Random  Forests:  An  ensemble  method  that  builds  multiple  decision  trees  to

improve prediction accuracy and reduce overfitting, making it highly effective for

like fraud detection.

complex fraud patterns.

•  Neural  Networks: A  more  advanced  technique  that  mimics  the  workings  of  the

human brain to detect complex, non-linear relationships in data. Neural networks

However, despite the progress, current models still face several deficiencies, such as handling

imbalanced  datasets,  adapting  to  new  fraud  schemes,  and  identifying  subtle  transactional

anomalies  and  irregularities,  even  in  real  time,  improving  the  speed  and  accuracy  of
identifying fraudulent transactions.

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

behavior that could indicate fraud.

This paper seeks to address these limitations by evaluating the deficiencies and constraints

of existing online transaction fraud detection models. Additionally, it aims to identify and

extract key transactional behavior indicators, which could significantly enhance the detection

process.  By  focusing  on  both  the  weaknesses  of  current  systems  and  the  opportunities

presented by new approaches, this research intends to provide a more robust and adaptive

solution to online fraud detection.

1.1 Machine Learning in Fraud Detection

ML has emerged as one of the most transformative technologies in recent years, significantly

impacting  various  industries  by  automating  processes,  improving  efficiency,  and  enabling

intelligent  decision-making.  As  a  subset  of  artificial  intelligence  (AI),  machine  learning

focuses on building systems that learn from data, identify patterns, and make decisions with

minimal human intervention. Complex algorithms enable machine learning models to evolve

over time, enhancing their accuracy and adaptability with the introduction of more data.

In the realm of online financial transactions, fraud detection has become a critical application

area  for  machine  learning  due  to  the  increasing  sophistication  of  fraudulent  schemes.

Traditional fraud detection methods, such as rule-based systems, rely heavily on predefined

rules  and  patterns,  making  them  rigid  and  unable  to  adapt  to  the  ever-evolving  tactics  of

fraudsters.  Often,  these  systems  lead  to  high  false  positive  rates,  incorrectly  flagging

legitimate transactions as fraudulent, resulting in customer dissatisfaction and financial losses

for businesses.

Machine learning-based fraud detection models, on the other hand, can analyze vast amounts

of transactional data in real time and uncover hidden patterns indicative of fraud. By learning

from  historical  fraud  data  and  continuously  adapting  to  new  types  of  fraud,  these  models

provide a more dynamic and efficient solution. Algorithms such as Decision Trees, Random

Forests, and Neural Networks allow the detection of both known and unknown fraudulent

activities by leveraging various features, such as transaction amounts, frequency, location,

and user behavior.

With  the  rapid  growth  of  online  financial  transactions,  fraud  detection  has  become

increasingly critical for businesses and consumers alike. Traditional rule-based systems have

been the primary method for identifying fraudulent activities, but they often struggle to keep

up  with  the  sophistication  of  modern  fraud  schemes.  Machine  learning  (ML),  a  subset  of

artificial  intelligence  (AI),  has  emerged  as  a  powerful  tool  in  combating  these  issues  by

offering dynamic, adaptable, and data-driven solutions.

1.2 What is Machine Learning?

 Machine learning is a branch of AI that focuses on building models capable of learning from

data.  Unlike  traditional  programming,  which  dictates  actions  with  explicit  instructions,

machine learning algorithms enhance their performance over time by processing data. This

capability  to  self-learn  allows  ML  models  to  adapt  to  new  information  without  human

intervention, making them particularly effective in environments where patterns evolve, such

as fraud detection.

In  fraud  detection,  machine  learning  models  analyze  vast  amounts  of  transactional  data,

identifying  patterns  that  indicate  potential  fraud.  These  models  can  automatically  detect

1.3 Limitations of Traditional Fraud Detection Methods

 Traditional  fraud  detection  systems  are  typically  rule-based.  They  operate  by  applying
predefined sets of rules to transactional data, such as flagging a transaction if it exceeds a
certain amount or originates from an unfamiliar location. While effective in some cases, rule-
based systems suffer from significant drawbacks:

•  Static Rules: They cannot adapt to new and emerging fraud tactics without manual

updates.

•  High False Positives: Businesses frequently mistakenly flag legitimate transactions
as fraudulent, which leads to customer dissatisfaction and potential revenue loss.
•  Limited  Scalability:  These  systems  struggle  to  manage  large  volumes  of

transactions, especially in real-time applications.

As a result, there is a growing need for more advanced systems that can handle the dynamic
nature of fraud in today’s digital landscape.

1.4 Why Machine Learning is Effective in Fraud Detection

Machine learning offers several advantages over traditional methods in fraud detection:

•  Adaptability: ML models can learn from historical data and update themselves as
new fraud patterns emerge. This ensures that the model is continuously improving
its accuracy without the need for constant human intervention.

•  Real-Time  Detection:  ML  algorithms  can  process  large  volumes  of  data  in  real
time, enabling immediate identification of fraudulent activities as they occur.

•  Reduction of False Positives: By analyzing multiple features of a transaction, such
as  user  behavior,  device  usage,  and  geolocation,  ML  models  can  differentiate
between legitimate and fraudulent transactions with greater precision, thus reducing
the number of false positives.

1.5 Common Machine Learning Techniques in Fraud Detection

Various machine learning techniques are employed to enhance fraud detection capabilities,
including:

•  Decision Trees: A supervised learning technique that divides the data into smaller
subsets based on decision rules. It is particularly useful for classification problems
like fraud detection.

•  Random  Forests:  An  ensemble  method  that  builds  multiple  decision  trees  to
improve prediction accuracy and reduce overfitting, making it highly effective for
complex fraud patterns.

•  Neural  Networks: A  more  advanced  technique  that  mimics  the  workings  of  the
human brain to detect complex, non-linear relationships in data. Neural networks

3

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

are effective in uncovering subtle fraudulent behavior patterns that simpler models
may miss.

Each  of  these  techniques  offers  unique  benefits,  but  they  all  share  the  common  goal  of
improving fraud detection accuracy and minimizing false positives and negatives.

2 Scope of the Study

This study aims to address two key aspects:

1.  Assessing  the  Deficiencies  of  Existing  Models:  By  analyzing  current  fraud
detection systems, this study will highlight the limitations of traditional methods,
such as their inability to adapt to evolving fraud techniques and their high rate of
false positives.

2.  Identifying  Key  Transactional  Behavior  Indicators:  A  major  focus  of  this
research  will  be  on  extracting  and  analyzing  new  behavioral  indicators,  such  as
transaction  frequency  and  user  interaction  times,  which  can  help  improve  the
accuracy of fraud detection models.

By leveraging machine learning techniques, this study aims to overcome the limitations of
traditional  fraud  detection  systems  and  contribute  to  the  development  of  more  robust  and
efficient solutions for identifying fraudulent transactions in real time.

3 Literature Review

M. N. Alataw (2024) presents a novel approach to credit card fraud detection in an IoT-driven
environment.  It  utilizes  advanced  ML  techniques  to  address  the  limitations  of  traditional
fraud  detection  systems.  The  study  highlights  the  integration  of  IoT  data  and  big  data
processing to build a real-time fraud detection framework, leveraging various ML models
such as Random Forest (RF), Gradient Boosting Machine (GBM), and Multilayer Perceptron
(MLP). The paper demonstrates improved accuracy, precision, recall, and F1 scores in fraud
detection using these models.

Khyati Kapadiya et al. (2024) highlight the pivotal role of healthcare insurance in providing
access  to  essential  medical  services  amidst  longer  life  expectancy  and  technological
advancements while addressing the growing challenge of fraudulent claims that necessitate
complex  procedures.  It  proposes  an  innovative  solution  combining  ensemble  learning
techniques, specifically bagging and stacking, with blockchain technology to enhance fraud
detection in healthcare insurance claims. By leveraging blockchain's decentralized security,
the approach ensures robust protection of sensitive patient and healthcare data. Additionally,
the  methodology  integrates  diverse  patient  data  including  in-patient,  out-patient,  and
beneficiary  information—offering  a  comprehensive  and  practical  solution.  The  study
compares  it  to  traditional  machine  learning  algorithms  (MLAs)  and  rates  its  performance
using metrics such as recall, accuracy, precision, ROC, F1-score, and a confusion matrix. It
also looks at how much it costs to use smart contracts for different purposes. This research
presents a resilient and efficient framework to combat fraudulent activities, advancing the
security and effectiveness of healthcare insurance systems.

Ju  Lu  et  al.  (2024)  present  a  scalable,  multi-model  ML  method  for  real-time  intrusion
detection and secure cryptographic key distribution. Using the large number of IoT devices,
the suggested ML-based IDS is designed to work in a variety of IoT settings, making it more

4

flexible  and  effective  at  detecting  threats. The  method  improves  the  accuracy  of  intrusion

detection and divides threats into nine different attack types by using Maximum–Minimum

(Max–Min)  normalization  on  datasets  such  as  UNSW-NB15  and  CICIoT2023.

Dimensionality  reduction  via  Principal  Component  Analysis  (PCA)  streamlines  data

processing and boosts efficiency, while six advanced ML models optimize threat detection.

Also, synchronized artificial neural networks (ANNs) are used in a secure key distribution

mechanism to make sure the safe exchange of cryptographic keys, which lowers the risk of

leaks. This new method not only improves real-time intrusion detection, but it also makes

information  management  systems  safer  overall.  It's  a  complete  and  effective  way  to  get

around the problems with current IDS solutions.

P.  Y.  Prasad  and  colleagues  (2023)  conducted  a  comparison  study  to  evaluate  the

effectiveness  of  various  machine  learning  models  in  the  identification  of fraudulent  credit

card  activity.  In  a  similar  vein,  R.  Aggarwal  and  colleagues  (2023)  examined  the

effectiveness of four different machine learning models in the detection of credit card fraud,

providing  insights  into  the  strengths  and  shortcomings  of  each  model  individually.  The

authors,  Fiore  et  al.  (2019),  investigated  the  possibility  of  using  GANs  to  enhance  the

efficiency of categorization in the detection of credit card fraud. Their Information Sciences

research  showcased  the  potential  of  GANs  as  a  supplementary  tool  to  enhance  datasets,

thereby boosting the effectiveness of conventional classifiers in identifying illicit financial

transactions.  Zhang  et  al.  (2018)  proposed  using  CNN  as  the  basis  for  a  model  to  detect

fraudulent activity in online financial transactions. Their strategy made use of CNNs' inherent

capacity  to  automatically  and  dynamically  learn  the  spatial  hierarchies  of  characteristics

underlying raw data.

4. Methodology

This study proposes a systematic approach to identify and address the limitations of existing

fraud  detection  systems  by  leveraging  key  transactional  behavior  indicators  and  advanced

machine  learning  techniques.  The  methodology  is  divided  into  two  primary  phases:  (1)

evaluation  of  current  fraud  detection  models,  and  (2)  development  of  a  hybrid  detection

framework utilizing behavioral insights and a Light Gradient Boosting Machine (LightGBM)

model.

 The following actions are being taken to address the first objective, which involves assessing

the shortcomings and limitations of existing fraud detection models:

Literature Review and Model Identification

A  comprehensive  literature  review  was  conducted  to  analyze  prevalent  fraud  detection

methodologies,  including  rule-based  systems,  statistical  approaches,  and  machine  learning

models such as Decision Trees, Random Forests, Support Vector Machines (SVM), Neural

Networks,  and  Logistic  Regression.  This  review  revealed  several  persistent  challenges,

including high false positive rates, limited adaptability to evolving fraud patterns, and poor

performance in real-time environments.

5. Evaluation of Current Fraud Detection Techniques

After  identifying  existing  models,  their  performance  was  assessed  using  the  following

metrics:

•  Accuracy

 :

(𝐴𝐴)

are effective in uncovering subtle fraudulent behavior patterns that simpler models

may miss.

Each  of  these  techniques  offers  unique  benefits,  but  they  all  share  the  common  goal  of

improving fraud detection accuracy and minimizing false positives and negatives.

2 Scope of the Study

This study aims to address two key aspects:

1.  Assessing  the  Deficiencies  of  Existing  Models:  By  analyzing  current  fraud

detection systems, this study will highlight the limitations of traditional methods,

such as their inability to adapt to evolving fraud techniques and their high rate of

false positives.

2.  Identifying  Key  Transactional  Behavior  Indicators:  A  major  focus  of  this

research  will  be  on  extracting  and  analyzing  new  behavioral  indicators,  such  as

transaction  frequency  and  user  interaction  times,  which  can  help  improve  the

accuracy of fraud detection models.

By leveraging machine learning techniques, this study aims to overcome the limitations of

traditional  fraud  detection  systems  and  contribute  to  the  development  of  more  robust  and

efficient solutions for identifying fraudulent transactions in real time.

3 Literature Review

M. N. Alataw (2024) presents a novel approach to credit card fraud detection in an IoT-driven

environment.  It  utilizes  advanced  ML  techniques  to  address  the  limitations  of  traditional

fraud  detection  systems.  The  study  highlights  the  integration  of  IoT  data  and  big  data

processing to build a real-time fraud detection framework, leveraging various ML models

such as Random Forest (RF), Gradient Boosting Machine (GBM), and Multilayer Perceptron

(MLP). The paper demonstrates improved accuracy, precision, recall, and F1 scores in fraud

detection using these models.

Khyati Kapadiya et al. (2024) highlight the pivotal role of healthcare insurance in providing

access  to  essential  medical  services  amidst  longer  life  expectancy  and  technological

advancements while addressing the growing challenge of fraudulent claims that necessitate

complex  procedures.  It  proposes  an  innovative  solution  combining  ensemble  learning

techniques, specifically bagging and stacking, with blockchain technology to enhance fraud

detection in healthcare insurance claims. By leveraging blockchain's decentralized security,

the approach ensures robust protection of sensitive patient and healthcare data. Additionally,

the  methodology  integrates  diverse  patient  data  including  in-patient,  out-patient,  and

beneficiary  information—offering  a  comprehensive  and  practical  solution.  The  study

compares  it  to  traditional  machine  learning  algorithms  (MLAs)  and  rates  its  performance

using metrics such as recall, accuracy, precision, ROC, F1-score, and a confusion matrix. It

also looks at how much it costs to use smart contracts for different purposes. This research

presents a resilient and efficient framework to combat fraudulent activities, advancing the

security and effectiveness of healthcare insurance systems.

Ju  Lu  et  al.  (2024)  present  a  scalable,  multi-model  ML  method  for  real-time  intrusion

detection and secure cryptographic key distribution. Using the large number of IoT devices,

the suggested ML-based IDS is designed to work in a variety of IoT settings, making it more

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

flexible  and  effective  at  detecting  threats. The  method  improves  the  accuracy  of  intrusion
detection and divides threats into nine different attack types by using Maximum–Minimum
(Max–Min)  normalization  on  datasets  such  as  UNSW-NB15  and  CICIoT2023.
Dimensionality  reduction  via  Principal  Component  Analysis  (PCA)  streamlines  data
processing and boosts efficiency, while six advanced ML models optimize threat detection.
Also, synchronized artificial neural networks (ANNs) are used in a secure key distribution
mechanism to make sure the safe exchange of cryptographic keys, which lowers the risk of
leaks. This new method not only improves real-time intrusion detection, but it also makes
information  management  systems  safer  overall.  It's  a  complete  and  effective  way  to  get
around the problems with current IDS solutions.

P.  Y.  Prasad  and  colleagues  (2023)  conducted  a  comparison  study  to  evaluate  the
effectiveness  of  various  machine  learning  models  in  the  identification  of fraudulent  credit
card  activity.  In  a  similar  vein,  R.  Aggarwal  and  colleagues  (2023)  examined  the
effectiveness of four different machine learning models in the detection of credit card fraud,
providing  insights  into  the  strengths  and  shortcomings  of  each  model  individually.  The
authors,  Fiore  et  al.  (2019),  investigated  the  possibility  of  using  GANs  to  enhance  the
efficiency of categorization in the detection of credit card fraud. Their Information Sciences
research  showcased  the  potential  of  GANs  as  a  supplementary  tool  to  enhance  datasets,
thereby boosting the effectiveness of conventional classifiers in identifying illicit financial
transactions.  Zhang  et  al.  (2018)  proposed  using  CNN  as  the  basis  for  a  model  to  detect
fraudulent activity in online financial transactions. Their strategy made use of CNNs' inherent
capacity  to  automatically  and  dynamically  learn  the  spatial  hierarchies  of  characteristics
underlying raw data.

4. Methodology

This study proposes a systematic approach to identify and address the limitations of existing
fraud  detection  systems  by  leveraging  key  transactional  behavior  indicators  and  advanced
machine  learning  techniques.  The  methodology  is  divided  into  two  primary  phases:  (1)
evaluation  of  current  fraud  detection  models,  and  (2)  development  of  a  hybrid  detection
framework utilizing behavioral insights and a Light Gradient Boosting Machine (LightGBM)
model.
 The following actions are being taken to address the first objective, which involves assessing
the shortcomings and limitations of existing fraud detection models:

Literature Review and Model Identification
A  comprehensive  literature  review  was  conducted  to  analyze  prevalent  fraud  detection
methodologies,  including  rule-based  systems,  statistical  approaches,  and  machine  learning
models such as Decision Trees, Random Forests, Support Vector Machines (SVM), Neural
Networks,  and  Logistic  Regression.  This  review  revealed  several  persistent  challenges,
including high false positive rates, limited adaptability to evolving fraud patterns, and poor
performance in real-time environments.

5. Evaluation of Current Fraud Detection Techniques

After  identifying  existing  models,  their  performance  was  assessed  using  the  following
metrics:

•  Accuracy

 :

(𝐴𝐴)

5

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

𝐹𝐹𝑇𝑇

 :

(𝑇𝑇)

𝑇𝑇𝑇𝑇, 𝑇𝑇𝑇𝑇, 𝐹𝐹𝑇𝑇
•  Precision

𝐴𝐴 =

𝑇𝑇𝑇𝑇 + 𝑇𝑇𝑇𝑇
𝑇𝑇𝑇𝑇 + 𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇 + 𝐹𝐹𝑇𝑇

  represent True  Positives, True  Negatives,  False  Positives,  and

where
False Negatives, respectively.

,  and

•  Recall

 :

(𝑅𝑅)

•  F1-Score (F1):

𝑇𝑇 =

𝑇𝑇𝑇𝑇
𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇

𝑅𝑅 =

𝑇𝑇𝑇𝑇
𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇

•  False Positive Rate (

 ):

𝐹𝐹1 = 2 ⋅

𝑇𝑇 ⋅ 𝑅𝑅
𝑇𝑇 + 𝑅𝑅

𝐹𝐹𝑇𝑇𝑅𝑅

These metrics were compared across various datasets to evaluate model performance under
different transaction types and fraud schemes.

𝐹𝐹𝑇𝑇𝑅𝑅 =

𝐹𝐹𝑇𝑇
𝐹𝐹𝑇𝑇 + 𝑇𝑇𝑇𝑇

Identification of Deficiencies

5.1.2. Feature Engineering and Extraction

Based  on  the  metrics  above,  the  weaknesses  of  each  model  were  documented.  These
included:

•  High False Positive Rates, leading to customer dissatisfaction.
•  Poor Adaptability to new fraud schemes in dynamic environments.
•  Slow Real-Time Processing of high transaction volumes.
•  Limited Feature Scope, with reliance on basic transactional attributes.

5.1 Identifying and Extracting Key Transactional Behavior Indicators

For  the  second  objective,  the  methodology  focused  on  identifying  critical  indicators  to
improve fraud detection models by capturing sophisticated transactional behavior patterns:

5.1.1 Data Collection and Preprocessing

The dataset used in this study is the Kaggle Credit Card Fraud Detection Dataset [1], which
contains 284,807 transactions from European cardholders. Among these, 492 transactions are
fraudulent, making the dataset highly imbalanced. Key features include time, amount, and
anonymized variables V1–V28 derived via PCA, along with the target variable Class, where
1 indicates fraud.

Key characteristics of the dataset:

6

•  Attributes: Includes anonymized features (V1–V28), Time, Amount, and the binary

class label Class (0 for genuine, 1 for fraud).

•  Reasons for selection: The dataset is publicly available, highly imbalanced (ideal

for fraud detection benchmarking), and includes transaction timing and monetary

features suitable for behavioral pattern extraction.

norm

𝑋𝑋

=

  and

𝑋𝑋 − 𝑋𝑋min

𝑋𝑋max − 𝑋𝑋min

𝑋𝑋min

𝑋𝑋max

where

  was  a  feature,  and

  were  its  minimum  and  maximum  values,

Imbalanced  Data  Handling:  The  Synthetic  Minority  Oversampling  Technique

(SMOTE) [2] was applied to the training set to generate synthetic examples for the

Preprocessing Steps:

•  Normalization:

respectively.

𝑋𝑋

•

where

value.

𝑋𝑋𝑖𝑖

𝑋𝑋𝑘𝑘

minority (fraudulent) class:

new

  and

  were  two  samples  from  the  minority  class,  and

= 𝑋𝑋𝑖𝑖 + 𝛿𝛿 ⋅ (𝑋𝑋𝑘𝑘 − 𝑋𝑋𝑖𝑖) 𝛿𝛿 ∈ [0,1]

𝑋𝑋

  was  a  random

•  Train-Test Split: The dataset was partitioned into 80% training and 20% testing sets

using stratified sampling to maintain class proportions.

𝛿𝛿 ∈ [0,1]

To enhance model learning, feature engineering was performed as follows:

•  Principal Component Analysis (PCA) was applied:

Dimensionality  reduction  was  applied  to  the  anonymized  variables  to  capture

maximum  variance  and  reduce  noise.  This  approach  helps  mitigate  noise  and

multicollinearity, which are common in high-dimensional datasets. By capturing the

principal  components  that  explain  the  majority  of  variance,  PCA  also  improves

model training efficiency and interpretability.

where

 was the feature matrix, and

𝑍𝑍 = 𝑋𝑋 ⋅ 𝑊𝑊

 was the matrix of principal components.

•  Recursive  Feature  Elimination  (RFE)  was  used  to  iteratively  remove  features

𝑊𝑊

𝑋𝑋

based  on  their  importance  until  the  optimal  set  was  achieved.  RFE  iteratively

removes  the  least  important  features  based  on  model  performance,  allowing  the

selection of an optimal subset that contributes meaningfully to fraud detection. This

reduces  the  risk  of  overfitting  and  enhances  model  generalization  across  unseen

data.

Key transactional indicators were identified, including:

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

•  Attributes: Includes anonymized features (V1–V28), Time, Amount, and the binary

class label Class (0 for genuine, 1 for fraud).

•  Reasons for selection: The dataset is publicly available, highly imbalanced (ideal
for fraud detection benchmarking), and includes transaction timing and monetary
features suitable for behavioral pattern extraction.

Preprocessing Steps:

•  Normalization:

𝑋𝑋

  was  a  feature,  and

where
respectively.

norm

=

𝑋𝑋
  and

𝑋𝑋 − 𝑋𝑋min
𝑋𝑋max − 𝑋𝑋min

  were  its  minimum  and  maximum  values,

𝑋𝑋min

𝑋𝑋max

where

,  and

  represent True  Positives, True  Negatives,  False  Positives,  and

𝑇𝑇𝑇𝑇 + 𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇 + 𝐹𝐹𝑇𝑇

𝑇𝑇𝑇𝑇 + 𝑇𝑇𝑇𝑇

𝐴𝐴 =

False Negatives, respectively.

𝑇𝑇𝑇𝑇, 𝑇𝑇𝑇𝑇, 𝐹𝐹𝑇𝑇

𝐹𝐹𝑇𝑇

•  Precision

 :

(𝑇𝑇)

•  Recall

 :

(𝑅𝑅)

•  F1-Score (F1):

𝑇𝑇 =

𝑇𝑇𝑇𝑇

𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇

𝑇𝑇𝑇𝑇

𝑅𝑅 =

𝑇𝑇𝑇𝑇 + 𝐹𝐹𝑇𝑇

•  False Positive Rate (

 ):

𝐹𝐹1 = 2 ⋅

𝑇𝑇 ⋅ 𝑅𝑅

𝑇𝑇 + 𝑅𝑅

𝐹𝐹𝑇𝑇𝑅𝑅

𝐹𝐹𝑇𝑇

𝐹𝐹𝑇𝑇𝑅𝑅 =

Identification of Deficiencies

included:

•  High False Positive Rates, leading to customer dissatisfaction.

•  Poor Adaptability to new fraud schemes in dynamic environments.

•  Slow Real-Time Processing of high transaction volumes.

•  Limited Feature Scope, with reliance on basic transactional attributes.

5.1 Identifying and Extracting Key Transactional Behavior Indicators

For  the  second  objective,  the  methodology  focused  on  identifying  critical  indicators  to

improve fraud detection models by capturing sophisticated transactional behavior patterns:

5.1.1 Data Collection and Preprocessing

The dataset used in this study is the Kaggle Credit Card Fraud Detection Dataset [1], which

contains 284,807 transactions from European cardholders. Among these, 492 transactions are

fraudulent, making the dataset highly imbalanced. Key features include time, amount, and

anonymized variables V1–V28 derived via PCA, along with the target variable Class, where

1 indicates fraud.

Key characteristics of the dataset:

•

Imbalanced  Data  Handling:  The  Synthetic  Minority  Oversampling  Technique
(SMOTE) [2] was applied to the training set to generate synthetic examples for the
minority (fraudulent) class:

new

  were  two  samples  from  the  minority  class,  and

= 𝑋𝑋𝑖𝑖 + 𝛿𝛿 ⋅ (𝑋𝑋𝑘𝑘 − 𝑋𝑋𝑖𝑖) 𝛿𝛿 ∈ [0,1]

𝑋𝑋

where
value.

  and

𝑋𝑋𝑖𝑖

𝑋𝑋𝑘𝑘

  was  a  random

𝛿𝛿 ∈ [0,1]

These metrics were compared across various datasets to evaluate model performance under

𝐹𝐹𝑇𝑇 + 𝑇𝑇𝑇𝑇

different transaction types and fraud schemes.

•  Train-Test Split: The dataset was partitioned into 80% training and 20% testing sets

using stratified sampling to maintain class proportions.

Based  on  the  metrics  above,  the  weaknesses  of  each  model  were  documented.  These

To enhance model learning, feature engineering was performed as follows:

5.1.2. Feature Engineering and Extraction

•  Principal Component Analysis (PCA) was applied:

Dimensionality  reduction  was  applied  to  the  anonymized  variables  to  capture
maximum  variance  and  reduce  noise.  This  approach  helps  mitigate  noise  and
multicollinearity, which are common in high-dimensional datasets. By capturing the
principal  components  that  explain  the  majority  of  variance,  PCA  also  improves
model training efficiency and interpretability.

where

 was the feature matrix, and

𝑍𝑍 = 𝑋𝑋 ⋅ 𝑊𝑊

 was the matrix of principal components.

𝑋𝑋

𝑊𝑊

•  Recursive  Feature  Elimination  (RFE)  was  used  to  iteratively  remove  features
based  on  their  importance  until  the  optimal  set  was  achieved.  RFE  iteratively
removes  the  least  important  features  based  on  model  performance,  allowing  the
selection of an optimal subset that contributes meaningfully to fraud detection. This
reduces  the  risk  of  overfitting  and  enhances  model  generalization  across  unseen
data.

Key transactional indicators were identified, including:

7

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

Behavioral Patterns (

 :

https://doi.org/10.1051/epjconf/202532801003

 Sum of Transactions in Time Window
𝐵𝐵𝐵𝐵)
 Time Window

•  Device and Location Consistency: Frequency of device or location changes were

𝐵𝐵𝐵𝐵 =

tracked as

freq  and

freq .

•  User Interaction Time (UT):
𝐷𝐷

𝐿𝐿

end

start

6 MACHINE LEARNING MODEL DEVELOPMENT

𝑈𝑈𝑈𝑈 = 𝑈𝑈

− 𝑈𝑈

1) Proposed Model: LightGBM-Based Hybrid Approach
The  core  model  of  this  study  is  a  Light  Gradient  Boosting  Machine  (LightGBM)  [3],
selected for its high performance in handling large-scale, imbalanced data. It employs leaf-
wise tree growth, resulting in faster convergence and better accuracy compared to level-wise
methods. Key benefits include:

•  Native support for categorical features
•  Efficient memory usage
•  Built-in support for imbalance handling (via parameter scale_pos_weight)

2) Baseline Models for Comparison
To  benchmark  the  performance  of  the  proposed  model,  the  following  classical  machine
learning models were implemented:
•  Logistic Regression
•  Decision Trees
•  Random Forest
•  Support Vector Machines (SVM)
•  Artificial Neural Networks (ANN)

4. Model Testing and Evaluation

•  The models were evaluated using met

such as  ROC-AUC and tested for real-

time performance with high transaction volumes.

•  A  comparative  analysis  was  conducted  to  determine  the  impact  of  the  key

rics

transactional indicators on model performance.

7 Results and Discussion

This  section  presents  the  evaluation  outcomes  of  the  proposed  hybrid  fraud  detection
framework, which incorporates behavioral indicators with a LightGBM model. Performance
comparisons were made with classical machine learning models using standardized metrics
and statistical validation. The study also highlights the significance of engineered features,
particularly  behavioral  patterns,  and  assesses  the  model's  applicability  in  real-time  fraud
detection environments.

7. 1 Model Performance Comparison

To  evaluate  model  effectiveness,  six  classifiers—Logistic  Regression,  Decision  Tree,
Random Forest, SVM, Artificial Neural Network (ANN), and the proposed LightGBM-were
assessed on the preprocessed Kaggle Credit Card Fraud Detection dataset. Evaluation metrics
included Accuracy, Precision, Recall, F1-Score, False Positive Rate (FPR), and ROC-AUC,
as shown in Table 1.

8

Table 1: Performance Metrics Comparison Across Models

Model

Accuracy  Precision  Recall  F1-Score  FPR  ROC-AUC

Logistic Regression

0.948

0.723

0.791

0.755

0.018

0.943

Decision Tree

0.951

0.759

0.803

0.780

0.015

0.949

Random Forest

0.967

0.842

0.873

0.857

0.010

0.970

SVM

0.958

0.802

0.812

0.807

0.013

0.958

ANN

0.963

0.827

0.849

0.838

0.011

0.965

LightGBM (Proposed)

0.976

0.891

0.914

0.902

0.006

0.981

Fig 1: Comparison of results

7.2 ROC Curve and Model Discrimination

The ROC curves shown in Fig 1 illustrate the trade-off between the True Positive Rate and

False Positive Rate for each model. The LightGBM model yielded the highest ROC-AUC

value (0.981), validating its superior discriminative ability in differentiating between genuine

and fraudulent transactions.

Behavioral Patterns (

 :

Table 1: Performance Metrics Comparison Across Models

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

 Sum of Transactions in Time Window

𝐵𝐵𝐵𝐵)

 Time Window

•  Device and Location Consistency: Frequency of device or location changes were

𝐵𝐵𝐵𝐵 =

tracked as

freq  and

freq .

•  User Interaction Time (UT):

𝐷𝐷

𝐿𝐿

end

start

6 MACHINE LEARNING MODEL DEVELOPMENT

𝑈𝑈𝑈𝑈 = 𝑈𝑈

− 𝑈𝑈

1) Proposed Model: LightGBM-Based Hybrid Approach

The  core  model  of  this  study  is  a  Light  Gradient  Boosting  Machine  (LightGBM)  [3],

selected for its high performance in handling large-scale, imbalanced data. It employs leaf-

wise tree growth, resulting in faster convergence and better accuracy compared to level-wise

methods. Key benefits include:

•  Native support for categorical features

•  Efficient memory usage

•  Built-in support for imbalance handling (via parameter scale_pos_weight)

2) Baseline Models for Comparison

To  benchmark  the  performance  of  the  proposed  model,  the  following  classical  machine

learning models were implemented:

•  Logistic Regression

•  Decision Trees

•  Random Forest

•  Support Vector Machines (SVM)

•  Artificial Neural Networks (ANN)

4. Model Testing and Evaluation

•  The models were evaluated using met

such as  ROC-AUC and tested for real-

time performance with high transaction volumes.

•  A  comparative  analysis  was  conducted  to  determine  the  impact  of  the  key

rics

transactional indicators on model performance.

7 Results and Discussion

This  section  presents  the  evaluation  outcomes  of  the  proposed  hybrid  fraud  detection

framework, which incorporates behavioral indicators with a LightGBM model. Performance

comparisons were made with classical machine learning models using standardized metrics

and statistical validation. The study also highlights the significance of engineered features,

particularly  behavioral  patterns,  and  assesses  the  model's  applicability  in  real-time  fraud

detection environments.

7. 1 Model Performance Comparison

To  evaluate  model  effectiveness,  six  classifiers—Logistic  Regression,  Decision  Tree,

Random Forest, SVM, Artificial Neural Network (ANN), and the proposed LightGBM-were

assessed on the preprocessed Kaggle Credit Card Fraud Detection dataset. Evaluation metrics

included Accuracy, Precision, Recall, F1-Score, False Positive Rate (FPR), and ROC-AUC,

as shown in Table 1.

Model

Accuracy  Precision  Recall  F1-Score  FPR  ROC-AUC

Logistic Regression

0.948

0.723

0.791

0.755

0.018

0.943

Decision Tree

0.951

0.759

0.803

0.780

0.015

0.949

Random Forest

0.967

0.842

0.873

0.857

0.010

0.970

SVM

0.958

0.802

0.812

0.807

0.013

0.958

ANN

0.963

0.827

0.849

0.838

0.011

0.965

LightGBM (Proposed)

0.976

0.891

0.914

0.902

0.006

0.981

Fig 1: Comparison of results

7.2 ROC Curve and Model Discrimination

The ROC curves shown in Fig 1 illustrate the trade-off between the True Positive Rate and
False Positive Rate for each model. The LightGBM model yielded the highest ROC-AUC
value (0.981), validating its superior discriminative ability in differentiating between genuine
and fraudulent transactions.

9

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

Fig 2. ROC Curve Comparison of Fraud Detection Models

7.3 Real-Time Viability and Runtime Performance

A runtime analysis was conducted to assess the efficiency of each model. Table 2 displays
the average prediction time per transaction for each model, measured on a system with Intel
i7 CPU, 16 GB RAM.

Table 2: Average Prediction Time Per Transaction

Model

Avg Prediction Time (ms)

0.32

0.47

1.25

3.12

Logistic Regression

Decision Tree

Random Forest

SVM

ANN

5.78

LightGBM

0.58

LightGBM maintained a strong balance between low latency (0.58 ms) and high predictive
accuracy, making it well-suited for deployment in real-time fraud detection systems.

10

7.4 Discussion and Implications

•  Superior  Detection  Performance: The  LightGBM-based  framework  outperformed

all  baseline  models  in  recall  (91.4%)  and  F1-score  (90.2%),  crucial  for  detecting

fraudulent activities without overwhelming the system with false alarms.

•  Behavioral  Feature  Engineering:  The  contribution  of  behavioral  attributes

significantly  enhanced  the  model’s  ability  to  detect  anomalies. This  suggests  that

capturing temporal, spatial, and interaction-based patterns is a promising direction

•  Statistical  Robustness:  The  statistical  significance  of  the  model  improvements

reinforces  the  reliability  of  findings,  ensuring  the  model’s  superiority  is  not  by

for fraud analytics.

chance.

•  Scalability: Given its low computational cost and strong performance, LightGBM

is ideal for high-volume transactional environments such as banking, e-commerce,

and fintech platforms.

8 Conclusion

This study evaluated the effectiveness of machine learning models in fraud detection, with a

specific  focus  on  the  integration  of  behavioral  indicators.  The  results  demonstrated  that

LightGBM  outperformed  other models  in  terms  of  accuracy,  precision, recall,  and  overall

fraud  detection  capability,  making  it  a  highly  efficient  and  scalable  solution  for  real-time

fraud  detection.  The  inclusion  of  behavioral  indicators  significantly  enhanced  model

performance,  reinforcing  the  importance  of  feature  selection  in  fraud  analytics.  Beyond

performance  analysis,  this  research  also  addressed  practical  implementation  challenges,

including computational efficiency, deployment feasibility, and dataset biases. The findings

emphasize the need for real-time adaptability in financial fraud prevention and suggest that

future research should explore hybrid models incorporating deep learning and explainable AI

techniques to further enhance fraud detection transparency. While this study provides a strong

foundation for ML-based fraud detection, limitations such as dataset representativeness and

model generalizability must be addressed in future work. A comparative analysis with state-

of-the-art fraud detection methods in real-world financial systems will further validate the

proposed approach. Ultimately, this research contributes to the advancement of data-driven

fraud detection strategies, offering a practical pathway for financial institutions to strengthen

security measures.

REFERENCES

1.  Dal Pozzolo, O. Caelen, Y. Le Borgne, S. Waterschoot, and G. Bontempi, "Credit Card

Fraud  Detection:  A  Realistic  Modeling  and  a  Novel  Learning  Strategy,"  IEEE

Transactions on Neural Networks and Learning Systems, 2015. Dataset: Kaggle

2.  N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, "SMOTE: Synthetic

Minority  Over-sampling Technique,"  Journal  of Artificial Intelligence Research,  vol.

3.  G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, et al., "LightGBM: A Highly Efficient

Gradient Boosting Decision Tree," Advances in Neural Information Processing

16, pp. 321–357, 2002.

Systems, 2017.

4.  Mohammed Naif Alatawi, "Detection of fraud in IoT based credit card collected dataset

using machine learning", Machine Learning with Applications, 2024, 1-16.

5.  Khyati  Kapadiya,  Fenil  Ramoliya,  Keyaba  Gohil,  Usha  Patel,  Rajesh  Gupta,  Sudeep

Tanwar,  Joel  J.P.C.  Rodrigues,  "Blockchain-assisted  healthcare  insurance  fraud

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

7.4 Discussion and Implications

https://doi.org/10.1051/epjconf/202532801003

•  Superior  Detection  Performance: The  LightGBM-based  framework  outperformed
all  baseline  models  in  recall  (91.4%)  and  F1-score  (90.2%),  crucial  for  detecting
fraudulent activities without overwhelming the system with false alarms.

•  Behavioral  Feature  Engineering:  The  contribution  of  behavioral  attributes
significantly  enhanced  the  model’s  ability  to  detect  anomalies. This  suggests  that
capturing temporal, spatial, and interaction-based patterns is a promising direction
for fraud analytics.

•  Statistical  Robustness:  The  statistical  significance  of  the  model  improvements
reinforces  the  reliability  of  findings,  ensuring  the  model’s  superiority  is  not  by
chance.

•  Scalability: Given its low computational cost and strong performance, LightGBM
is ideal for high-volume transactional environments such as banking, e-commerce,
and fintech platforms.

8 Conclusion

This study evaluated the effectiveness of machine learning models in fraud detection, with a
specific  focus  on  the  integration  of  behavioral  indicators.  The  results  demonstrated  that
LightGBM  outperformed  other models  in  terms  of  accuracy,  precision, recall,  and  overall
fraud  detection  capability,  making  it  a  highly  efficient  and  scalable  solution  for  real-time
fraud  detection.  The  inclusion  of  behavioral  indicators  significantly  enhanced  model
performance,  reinforcing  the  importance  of  feature  selection  in  fraud  analytics.  Beyond
performance  analysis,  this  research  also  addressed  practical  implementation  challenges,
including computational efficiency, deployment feasibility, and dataset biases. The findings
emphasize the need for real-time adaptability in financial fraud prevention and suggest that
future research should explore hybrid models incorporating deep learning and explainable AI
techniques to further enhance fraud detection transparency. While this study provides a strong
foundation for ML-based fraud detection, limitations such as dataset representativeness and
model generalizability must be addressed in future work. A comparative analysis with state-
of-the-art fraud detection methods in real-world financial systems will further validate the
proposed approach. Ultimately, this research contributes to the advancement of data-driven
fraud detection strategies, offering a practical pathway for financial institutions to strengthen
security measures.

REFERENCES

1.  Dal Pozzolo, O. Caelen, Y. Le Borgne, S. Waterschoot, and G. Bontempi, "Credit Card
Fraud  Detection:  A  Realistic  Modeling  and  a  Novel  Learning  Strategy,"  IEEE
Transactions on Neural Networks and Learning Systems, 2015. Dataset: Kaggle
2.  N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, "SMOTE: Synthetic
Minority  Over-sampling Technique,"  Journal  of Artificial Intelligence Research,  vol.
16, pp. 321–357, 2002.

3.  G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, et al., "LightGBM: A Highly Efficient
Gradient Boosting Decision Tree," Advances in Neural Information Processing
Systems, 2017.

4.  Mohammed Naif Alatawi, "Detection of fraud in IoT based credit card collected dataset

using machine learning", Machine Learning with Applications, 2024, 1-16.

5.  Khyati  Kapadiya,  Fenil  Ramoliya,  Keyaba  Gohil,  Usha  Patel,  Rajesh  Gupta,  Sudeep
Tanwar,  Joel  J.P.C.  Rodrigues,  "Blockchain-assisted  healthcare  insurance  fraud

11

Fig 2. ROC Curve Comparison of Fraud Detection Models

7.3 Real-Time Viability and Runtime Performance

A runtime analysis was conducted to assess the efficiency of each model. Table 2 displays

the average prediction time per transaction for each model, measured on a system with Intel

i7 CPU, 16 GB RAM.

Table 2: Average Prediction Time Per Transaction

Model

Avg Prediction Time (ms)

0.32

0.47

1.25

3.12

Logistic Regression

Decision Tree

Random Forest

SVM

ANN

5.78

LightGBM

0.58

LightGBM maintained a strong balance between low latency (0.58 ms) and high predictive

accuracy, making it well-suited for deployment in real-time fraud detection systems.

EPJ Web of Conferences 328, 01003 (2025)
ICETSF-2025

https://doi.org/10.1051/epjconf/202532801003

detection framework using ensemble learning", Computers and Electrical Engineering,
122, 2024.

6.  Ju  Lu, Arindam  Bhar,   Arindam  Sarkar, Abdulfattah  Noorwali,  Kamal  M.  Othman,
"Enhancing real-time intrusion detection and secure key distribution using multi-model
machine learning approach for mitigating confidentiality threats", Internet of things, 28,
2024.

7.  P. Y. Prasad, A. S. Chowdary, C. Bavitha, E. Mounisha and C. Reethika, "A Comparison
Study of Fraud Detection in Usage of Credit Cards using Machine Learning," 2023 7th
International Conference on Trends in Electronics and Informatics (ICOEI), Tirunelveli,
India, 2023, pp. 1204-1209, doi: 10.1109/ICOEI56765.2023.10125838.

8.  R. Aggarwal, P. K. Sarangi and A. K. Sahoo, "Credit Card Fraud Detection: Analyzing
the Performance of Four Machine Learning Models," 2023 International Conference on
Disruptive  Technologies  (ICDT),  Greater  Noida,  India,  2023,  pp.  650-654,  doi:
10.1109/ICDT57929.2023.10150782.

9.  G.  M.  Suhas  Jain,  N.  Rakesh,  K.  Pranavi  and  L. Bale,  "A  Novel Approach  in  Credit
Card Fraud Detection System Using Machine Learning Techniques," 2021 International
Conference  on  Forensics,  Analytics,  Big  Data,  Security  (FABS),  Bengaluru,  India,
2021, pp. 1-5, doi: 10.1109/FABS52071.2021.9702672.

10.  J.  Chaquet-ulldemolins,  S.  Moral-rubio,  S.  Mu˜  noz-romero,  On  the  black-box
challenge  for  fraud  detection  using  machine  learning  (II):  nonlinear  analysis  through
interpretable autoencoders, Appl. Sci. 12 (2022) 3856

11.  W.  Hilal,  S.A.  Gadsden,  J. Yawney,  Financial  fraud:  a  review  of  anomaly  detection

techniques and recent advances, Expert Syst. Appl. 193 (2021)

12.  M.N. Ashtiani,  B.  Raahemi,  Intelligent  fraud  detection  in  financial  statements  using
machine  learning  and  data  mining:  a  systematic  literature  review,  IEEE  Access  10
(2021) 72504–72525

13.  K.G.  Al-Hashedi,  P.  Magalingam,  Financial  fraud  detection  applying  data  mining
techniques: a comprehensive review from 2009 to 2019, Comput. Sci. Rev. 40 (2021)
14.  Ramkumar Jayaraman, Mohammed Alshehri, Manoj Kumar, Ahed Abugabah, Surender
Singh  Samant,  Ahmed  A.  Mohamed,  Secure  biomedical  document  protection
framework to ensure privacy through blockchain, Big Data 11 (6) (2023) 437–451.
15.  Devandar  Rao,  Ramkumar  Jayaraman,  A  Novel  Quantum  Identity  Authentication
protocol  without  entanglement  and  preserving  pre-shared  key  information,  Quantum
Information Processing, Springer 22 (2023). Article No. 92.

16.  Faisal,  N.  A.,  Nahar,  J.,  Sultana,  N.,  &  Mintoo,  A.  A.  (2024).  Fraud  Detection  In
Banking  Leveraging Ai To  Identify And  Prevent Fraudulent Activities  In  Real-Time.
Journal of Machine Learning, Data Engineering and Data Science, 1(01), 181-197.
17.  Oluwole,  V.,  2024.  4 African  countries  with  highest  scam  losses  in  2024.  Business
Insider Africa.  https://africa.businessinsider.com/local/markets/african-countries-with-
highest-scam-losses/wrvpj5k (Accessed 15 December 2024).

18.  Sharma,  R.,  Mehta,  K., Sharma,  P.,  2024.  Role  of  artificial  intelligence  and  machine
learning  in  fraud  detection  and  prevention.  In:  Risks  and  Challenges  of  AI-Driven
Finance: Bias, Ethics, and Security. IGI Global, pp. 90–120.

19.  Theodorakopoulos,  L.,  Theodoropoulou,  A.,  Stamatiou,  Y.,  2024.  A  state-of-the-art
review  in  big  data  management  engineering:  real-life  case  studies,  challenges,  and
future research directions. Eng 5 (3), 1266–1297.

20.  Takyar,  A.,  2024.  Financial  fraud  detection  using  machine  learning  models.
https://www.leewayhertz.com/build-financial-fraud-detection-system-using-ML-
models/ (Accessed 19 March 2024).

12

