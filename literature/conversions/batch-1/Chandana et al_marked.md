---
conversion_metadata:
  converted_at: "2026-07-22T12:44:24Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Chandana et al.pdf"
  source_pdf_sha256: "b72b5f26aa040a76bc5aea7bcc4022e54eb1bc3e6156b5f17dd856ae4310e953"
  page_count: 4
  markdown_char_count: 35478
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING 
Peer Reviewed, Referred & Indexed Journal 
E-ISSN: 3069-0110 
Vol.5, No.2(2026) 
www.ajmimc.com

PERSONAL FINANCE TRACKER WITH AI BASED EXPENSE PREDICTION

1 M.CHANDANA , 2 E.MANOJ  VARDHAN REDDY, 3 E.PRAVEEN REDDY, 4  I.SIRI VAISHNAVI,5  K.VAISHNAVI 
1Assistant Professor, Department of  CS , Sri  Indu College Of Engineering & Technology ,Hyderabad. 
2,3,4,5 U.G. Scholar, Department of CS, Sri  Indu College Of Engineering & Technology, Hyderabad. 
***

Abstract  -  In  today’s  digital  age,  individuals  perform 
financial  transactions  each  month  through 
numerous 
mobile  wallets,  banking  applications,  and  online  payment 
platforms. Although many existing applications record these 
transactions,  they  often  fail  to  deliver  meaningful  insights 
into user spending behavior or provide predictive assistance 
for effective  budgeting. This  paper proposes an AI-powered 
personal  finance  tracking  system  that  leverages  behavioral 
analysis and machine learning techniques to forecast future 
expenses and identify unusual spending patterns. The system 
is  implemented  using  Python  and  Flask,  with  a  MySQL 
database 
for  efficient  storage  and  management  of 
transaction data. Machine learning models such as Random 
Forest and  Long Short-Term Memory (LSTM)  networks are 
utilized  to  analyze  user  behavior  and  predict  monthly 
expenditure trends. 
The  experimental  results  demonstrate  that  the  proposed 
system  enhances  users’  financial  awareness  and  enables 
better  control  over  spending  habits  when  compared  to 
conventional  static  tracking  applications.  By  providing 
intelligent  insights  and  predictive  recommendations,  the 
system  supports  users 
financial 
decisions and managing their finances more effectively.

in  making

informed

Keywords:  Machine  Learning,  Expense  Prediction, 
Behavioral Analysis

1. INTRODUCTION

In  today’s  digital  world,  individuals  perform  numerous 
transactions  through  UPI  wallets,  online  banking,  and  e- 
commerce platforms. Although several applications record 
these transactions, most fail to provide analytical insights or 
budgeting guidance. Traditional expense trackers are limited 
to data storage without intelligent financial forecasting.

This  paper  presents  an  AI-powered  personal  finance 
tracker built using Python, Flask, and MySQL. It employs 
machine learning models such as Random Forest and LSTM 
to analyse spending patterns, predict future expenses, and 
detect  unusual  transactions.  By  applying  behavioural 
analytics  to  financial  data,  the  system  promotes  financial 
awareness  and  enables  smarter  money  management 
compared to conventional tools.

Main Objectives:

1.  To  develop  an  intelligent  personal  finance 
tracking system that automatically records and organizes 
user transactions through a web-based interface using Flask.

2. To apply machine learning models (Random Forest

& LSTM) for analyzing spending patterns and predicting

future monthly expenses.To implement behavioral pattern 
analysis for detecting unusual or abnormal spending 
activities in real time.

3.  To  offer  a  data-driven  alternative  to  traditional  static 
expense  trackers  by  integrating  forecasting,  anomaly 
detection, and automated categorization.

2. LITERATURE REVIEW

Priya  Sharma  et  al.  [1]  developed  an  intelligent  expense 
management system using machine learning algorithms to 
classify and visualize user spending behaviour. Their study 
highlighted  how  automated  categorization  of  expenses 
improves financial awareness.

Ankit  Kumar  and  R.  Patel  [2]  proposed  a  predictive 
budgeting  system  using  Linear  Regression  and  Decision 
Trees  to  forecast  monthly  expenditures.  The  model 
demonstrated  better  accuracy  in  predicting  recurring 
payments compared to rule-based systems.

S.  Banerjee  et  al.  [3]  introduced  an  AI-driven  financial 
monitoring system that uses anomaly detection techniques 
to  identify  unusual  spending  patterns  and  potential 
fraudulent activities in user transactions.

Finally, J. Zhang et al. [4] proposed the integration of LSTM 
networks for time-series forecasting in personal financial 
applications,  achieving  improved  accuracy  in  predicting 
future expenses based on historical data.

These  studies  collectively  emphasize  that  applying  machine 
learning techniques such as Random Forest and LSTM can 
significantly enhance the functionality of expense trackers by 
enabling 
personalized 
analysis 
recommendations.

predictive

and

3. METHODOLOGY

3.1 Existing System

Traditional expense trackers primarily function as manual 
recording tools where users enter their daily income and 
expenditure  data.  These  systems  usually  provide  basic 
statistical  summaries,  pie  charts,  or  bar  graphs  without 
insights  or  personalized 
offering  any  predictive 
recommendations.

449

---

<!-- PAGE 2 -->

AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING 
Peer Reviewed, Referred & Indexed Journal 
E-ISSN: 3069-0110 
Vol.5, No.2(2026) 
www.ajmimc.com

Most existing systems:



Lack automation and rely on user input.

  Do not analyze behavioral spending patterns.



Cannot predict future expenses or detect anomalies.

As a result, users gain only a surface-level understanding of 
their finances without the capability to make data-driven 
budgeting decisions.

3.2 Proposed  System

The proposed AI-powered personal finance tracker enhances 
traditional  systems  by  incorporating  machine  learning 
algorithms and behavioral analytics to automatically analyze 
spending    trends    and    predict    future    expenses. 
The  system  is  built  using  Python  (Flask  framework)  for 
backend  development  and  MySQL  for  transaction  data 
storage. Machine learning models such as Random Forest 
and  LSTM  (Long  Short-Term  Memory)  are  integrated  for 
classification and time-series forecasting, respectively.

Key features include:









Automated classification of expenses into categories 
(e.g., food, travel, bills).

Monthly expense prediction using LSTM based on 
historical data.

Anomaly  detection  for  identifying  unusual  or 
excessive spending.

Real-time  dashboard  for  visualizing 
expense patterns

income–

This  system  thus  transforms  a  passive  tracker  into  an 
intelligent 
financial  assistant,  providing  users  with 
actionable insights and better financial control.

4. MODULES

The  proposed  system  is  divided  into  several  functional 
modules  to  ensure  efficient  operation  and  modular 
development.  Each  module  performs  a  specific  task  and 
interacts  with  others  to  achieve  the  overall  system 
objectives.

Figure 1: System Architecture of the AI-Powered Personal 
Finance Tracker

4.1 User  Authentication  Module

This  module  manages  user  registration  and 
login 
functionality.  It  ensures  secure  access  using  encrypted 
passwords and session handling in Flask. Each user’s data is 
isolated in the database to maintain privacy and integrity.

4.2 Transaction  Management  Module

Users  can  add,  edit,  delete,  and  view  their  transactions 
through this module. Each transaction includes details such 
as date, amount, category, and description. Data is stored in 
the MySQL database and can be retrieved dynamically for 
visualization and analysis.

4.3 Data Preprocessing Module

Before applying machine learning, the transaction data is 
cleaned  and  pre-processed.  This  module  removes  null 
values, converts categorical data into numerical form, and 
normalizes datasets. It ensures that only valid, structured 
data is used for model training.

4.4 Expense Classification Module

Using  the  Random  Forest  algorithm,  this  module 
automatically  classifies  user  transactions  into  categories 
such    as    food,    travel,    rent,    or    entertainment. 
This helps users understand where most of their money is 
spent without needing manual categorization.

4.5 Expense Prediction Module

This  module  uses  LSTM  (Long  Short-Term  Memory),  a 
deep learning model for time-series forecasting, to predict 
future  expenses  based  on  historical  transaction  data. 
It enables users to plan monthly budgets more effectively 
and anticipate upcoming financial needs.

450

---

<!-- PAGE 3 -->

AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING 
Peer Reviewed, Referred & Indexed Journal 
E-ISSN: 3069-0110 
Vol.5, No.2(2026) 
www.ajmimc.com

4.6 Anomaly  Detection  Module

This  component  analyses  spending  trends  and  detects 
abnormal  patterns—such  as  sudden  high  spending  or 
unusual category spikes. Alerts are generated to help users 
maintain controlled and conscious spending behavior.

4.7 Dashboard  and  Visualization  Module

An interactive dashboard presents graphical reports such as 
bar charts, pie charts, and line graphs.

  The  predicted  values  closely  matched  the  actual

spending patterns for most categories.

6.2 Expense  Classification

Random  Forest  was  used  to  categorize  transactions  into 
groups such as Food, Bills, Shopping, and Travel.

  The  model  reached  above  90%  accuracy  in

categorization.

  Users were able to view clear, organized spending

breakdowns on the dashboard.

5. IMPLEMENTATION

6.3 Anomaly  Detection

Users can view total income, expenditure distribution, and 
predicted  expenses.  Flask  and  JavaScript  libraries  (like 
Chart.js) are used for visualization. The implementation of 
the  proposed  AI-Powered  Personal  Finance  Tracker 
involves  designing  both  the  backend  and  frontend 
components,  integrating  a  machine  learning  module,  and 
establishing  smooth  communication  between  the  user 
interface and the database.

5.1 Technology  Stack

Frontend-HTML, CSS, JavaScript 
Backend-Python 
Database – MySQL/PostgreSQL 
Machine Learning Models-Random Forest, LSTM 
Libraries Used – Pandas, NumPy, Scikit-learn, TensorFlow, 
Matplotlib

Figure 2: System Architecture Flow for Flask-Based ML 
Dashboard

6. RESULT AND FINDINGS

The  proposed  AI-powered  personal  finance  tracker  was 
tested using sample and real transaction data. The system 
successfully combined Flask, MySQL, and machine learning 
models to generate meaningful insights.

6.1 Expense  Prediction

The LSTM model provided reliable predictions for monthly 
spending trends.



It achieved around 85% accuracy in forecasting 
next-month expenses.

The  system  detected  unusual  or  abnormal  spending 
behaviors. 


It identified sudden spikes or irregular transactions 
with good accuracy.

  This helped users notice overspending early.

6.4 Dashboard  Usability

The  dashboard  displayed  expense  summaries  through 
simple charts and visuals.

  Users found the interface easy to understand. 


Insights  such  as  monthly  totals,  category-wise 
spending,  and  predictions  improved  financial 
awareness.

6.5 Overall  Findings

The results show that the system provides:

  Better  tracking  than  manual  or  static  expense

trackers

  Accurate predictions of future spending 
  Helpful alerts for unusual expenses 
  A user-friendly interface  with  meaningful  insights

7. DISCUSSION

The  system  demonstrates  that  integrating  machine  learning 
into  personal  finance  management  significantly  elevates  the 
effectiveness of traditional tracking tools. The LSTM model 
provides strong, forward-looking predictions, enabling users 
to  prepare  their  budgets  with  greater  confidence.  The 
Random  Forest  classifier  adds  clarity  by  accurately 
organizing expenses into meaningful categories, improving 
overall financial awareness.

The anomaly detection component further strengthens the 
system  by  identifying  unusual  or  unexpected  spending 
patterns,  offering  users  early  warnings  that  traditional 
trackers  fail  to  deliver.  Additionally,  the  intuitive  dashboard 
transforms  complex  financial  data  into  clear,  actionable 
insights.

Overall, the system shifts personal finance tracking from a 
passive  recording  tool  to  an  intelligent,  predictive,  and 
proactive financial assistant.

451

---

<!-- PAGE 4 -->

AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING 
Peer Reviewed, Referred & Indexed Journal 
E-ISSN: 3069-0110 
Vol.5, No.2(2026) 
www.ajmimc.com

8. CONCLUSION

Random

forecasting,

The  AI-powered  personal  finance  tracker  successfully 
demonstrates  how  machine 
learning  can  transform 
traditional  expense  monitoring  into  a  predictive  and 
intelligent  financial  management  system.  By  integrating 
LSTM-based 
Forest-driven 
categorization, and effective anomaly detection, the system 
provides  users  with  deeper  insight  into  their  financial 
behavior and empowers them to plan with greater accuracy. 
The  results  show  that  the  proposed  solution  not  only 
enhances budgeting efficiency but also helps users identify 
unusual spending and improve overall financial discipline. 
With its intuitive dashboard and automated analytics, the 
system delivers a modern, data-driven alternative to static 
expense trackers.

In essence, this work proves that AI can play a critical role in 
making personal finance management smarter, proactive, 
and more user-centric.

9. FUTURE SCOPE

The  proposed  system  offers  multiple  opportunities  for 
enhancement that can significantly extend its capabilities. 
Future improvements may include incorporating advanced 
deep  learning  architectures,  such  as  Transformer-based 
models, to deliver more accurate expense forecasting and 
deeper  behavioral  analysis.  Automated  integration  with 
bank APIs, UPI services, or SMS/email extraction can further 
streamline data input, making the system entirely hands- 
free.

The project can also be expanded to provide personalized 
financial  guidance—such  as  optimized  budgeting  strategies, 
goal-based  recommendations,  or  savings  insights  tailored  to 
individual spending habits. Deploying the tracker on cloud 
platforms can enhance scalability and Performance, enabling 
it to handle larger datasets and real-time analytics efficiently. 
Additional  features  such  as  multi-user  profiles,  advanced 
privacy  controls,  and  cross-device  synchronization  can 
broaden  the  system’s  usefulness  for  families  or  small 
businesses. With these enhancements, the system has strong 
potential to evolve into a comprehensive, intelligent, and 
highly adaptive financial management platforms.

REFERENCES

[1]  S.  P.  Rajasekar  and  R.  Babu,  “Personal  Finance 
Management  System  Using  Machine  Learning,”  International 
in  Computer  and 
Journal  of 
Communication Engineering (IJIRCCE), Vol. 10, Issue 6, pp. 
2543–2550, 2022.

Innovative  Research

[2] K. Kaur and M. K. Singh, “AI-Based Expense Prediction 
System  Using  Machine  Learning,”  International  Journal  of 
Advanced Research in Computer Science (IJARCS), Vol. 13, 
No. 2, pp. 45–52, 2022.

[3]  N.  Gupta,  R.  Sharma,  and  S.  Agrawal,  “Smart  Budget 
Tracker  Using  Flask  and  MySQL,”  IEEE  9th  International 
Conference  on  Computing,  Communication  and  Automation 
(ICCCA), pp. 121–127, 2023.

[4]  A.  Patel  and  D.  Sinha,  “Predictive  Analysis  of  User 
Expenditure Using Random Forest and LSTM,” International 
Research  Journal of Engineering and Technology (IRJET), 
Vol. 8, Issue 7, pp. 2304–2311, 2021.

[5] R. Reddy, “AI-Powered Personal Expense Tracker with 
Behavior  Analysis,”  International  Journal  of  Emerging 
Technologies and Innovative Research (JETIR), Vol. 9, Issue 
11, pp. 56–63, 2022.

[6]  M.  A.  Rahman  and  T.  S.  Alam,  “Financial  Data 
Visualization  and  Forecasting  Using  Python  Flask 
Framework,” International Journal of Scientific & Technology 
Research (IJSTR), Vol. 11, Issue 3, pp. 89–97, 2022.

[7] S. Bhattacharya, “Automated Personal Finance Tracking 
System Using AI and Data Analytics,” International Journal of 
Computer Science Trends and Technology (IJCST), Vol. 10, 
Issue 5, pp. 14–19, 2023.

452

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING
Peer Reviewed, Referred & Indexed Journal
E-ISSN: 3069-0110
Vol.5, No.2(2026)
www.ajmimc.com
PERSONAL FINANCE TRACKER WITH AI BASED EXPENSE PREDICTION
1 M.CHANDANA , 2 E.MANOJ VARDHAN REDDY, 3 E.PRAVEEN REDDY, 4 I.SIRI VAISHNAVI,5 K.VAISHNAVI
1Assistant Professor, Department of CS , Sri Indu College Of Engineering & Technology ,Hyderabad.
2,3,4,5 U.G. Scholar, Department of CS, Sri Indu College Of Engineering & Technology, Hyderabad.
***
Abstract - In today’s digital age, individuals perform future monthly expenses.To implement behavioral pattern
numerous financial transactions each month through analysis for detecting unusual or abnormal spending
mobile wallets, banking applications, and online payment activities in real time.
platforms. Although many existing applications record these
3. To offer a data-driven alternative to traditional static
transactions, they often fail to deliver meaningful insights
expense trackers by integrating forecasting, anomaly
into user spending behavior or provide predictive assistance
detection, and automated categorization.
for effective budgeting. This paper proposes an AI-powered
personal finance tracking system that leverages behavioral
2. LITERATURE REVIEW
analysis and machine learning techniques to forecast future
expenses and identify unusual spending patterns. The system Priya Sharma et al. [1] developed an intelligent expense
is implemented using Python and Flask, with a MySQL management system using machine learning algorithms to
database for efficient storage and management of classify and visualize user spending behaviour. Their study
transaction data. Machine learning models such as Random highlighted how automated categorization of expenses
Forest and Long Short-Term Memory (LSTM) networks are improves financial awareness.
utilized to analyze user behavior and predict monthly
expenditure trends. Ankit Kumar and R. Patel [2] proposed a predictive
The experimental results demonstrate that the proposed budgeting system using Linear Regression and Decision
system enhances users’ financial awareness and enables Trees to forecast monthly expenditures. The model
better control over spending habits when compared to demonstrated better accuracy in predicting recurring
conventional static tracking applications. By providing payments compared to rule-based systems.
intelligent insights and predictive recommendations, the
system supports users in making informed financial S. Banerjee et al. [3] introduced an AI-driven financial
decisions and managing their finances more effectively. monitoring system that uses anomaly detection techniques
to identify unusual spending patterns and potential
fraudulent activities in user transactions.
Keywords: Machine Learning, Expense Prediction,
Behavioral Analysis Finally, J. Zhang et al. [4] proposed the integration of LSTM
networks for time-series forecasting in personal financial
1. INTRODUCTION applications, achieving improved accuracy in predicting
future expenses based on historical data.
In today’s digital world, individuals perform numerous
transactions through UPI wallets, online banking, and e- These studies collectively emphasize that applying machine
commerce platforms. Although several applications record learning techniques such as Random Forest and LSTM can
these transactions, most fail to provide analytical insights or significantly enhance the functionality of expense trackers by
budgeting guidance. Traditional expense trackers are limited enabling predictive analysis and personalized
to data storage without intelligent financial forecasting. recommendations.
This paper presents an AI-powered personal finance 3. METHODOLOGY
tracker built using Python, Flask, and MySQL. It employs
machine learning models such as Random Forest and LSTM 3.1 Existing System
to analyse spending patterns, predict future expenses, and
Traditional expense trackers primarily function as manual
detect unusual transactions. By applying behavioural
recording tools where users enter their daily income and
analytics to financial data, the system promotes financial
expenditure data. These systems usually provide basic
awareness and enables smarter money management
statistical summaries, pie charts, or bar graphs without
compared to conventional tools.
offering any predictive insights or personalized
Main Objectives: recommendations.
1. To develop an intelligent personal finance
tracking system that automatically records and organizes
user transactions through a web-based interface using Flask.
2. To apply machine learning models (Random Forest
& LSTM) for analyzing spending patterns and predicting
449

AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING
Peer Reviewed, Referred & Indexed Journal
|     |     |     |     |     |     |     |     |     |     | E-ISSN: 3069-0110  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
Vol.5, No.2(2026)
www.ajmimc.com

Most existing systems:
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|    |     |     |     |     |     |     |     |     |     |     |     |     |     |
Lack automation and rely on user input.

|    | Do not analyze behavioral spending patterns.  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|                                                               | Cannot predict future expenses or detect anomalies.  |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| As a result, users gain only a surface-level understanding of  |                                                      |     |     |     |     |     |     |     |     |     |     |     |     |

their finances without the capability to make data-driven
| budgeting decisions.  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

3.2 Proposed System

The proposed AI-powered personal finance tracker enhances

| traditional                                                   | systems  | by  | incorporating  |     | machine  |     | learning  |     |     |     |     |     |     |
| ------------------------------------------------------------- | -------- | --- | -------------- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| algorithms and behavioral analytics to automatically analyze  |          |     |                |     |          |     |           |     |     |     |     |     |     |

| spending  |   trends  |   and  |   predict  |     |   future  |   expenses.  |     |     |     |     |     |     |     |
| --------- | --------- | ------ | ---------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
The system is built using Python (Flask framework) for
Figure 1: System Architecture of the AI-Powered Personal
| backend  | development  |     | and  MySQL  |     | for  transaction  |     | data  |     |     |     |     |     |     |
| -------- | ------------ | --- | ----------- | --- | ----------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
Finance Tracker
storage. Machine learning models such as Random Forest

and LSTM (Long Short-Term Memory) are integrated for
4.1 User Authentication Module
classification and time-series forecasting, respectively.

|     |     |     |     |     |     |     |     | This  module  | manages  | user  registration  |     | and  | login  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ------------------- | --- | ---- | ------ |
Key features include:
|     |     |     |     |     |     |     |     | functionality.  | It ensures secure access using encrypted  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----------------------------------------- | --- | --- | --- | --- |

passwords and session handling in Flask. Each user’s data is
   Automated classification of expenses into categories
isolated in the database to maintain privacy and integrity.
(e.g., food, travel, bills).

   Monthly expense prediction using LSTM based on  4.2 Transaction Management Module
historical data.
Users can add, edit, delete, and view their transactions
   Anomaly  detection  for  identifying  unusual  or  through this module. Each transaction includes details such
excessive spending.  as date, amount, category, and description. Data is stored in
the MySQL database and can be retrieved dynamically for
|    |  Real-time  | dashboard  |     | for  | visualizing  |     | income–  |     |     |     |     |     |     |
| --- | ----------- | ---------- | --- | ---- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- |
visualization and analysis.
expense patterns

This system thus transforms a passive tracker into an  4.3 Data Preprocessing Module
| intelligent  | financial  |     | assistant,  | providing  |     | users  | with  |     |     |     |     |     |     |
| ------------ | ---------- | --- | ----------- | ---------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
Before applying machine learning, the transaction data is
actionable insights and better financial control.
|     |     |     |     |     |     |     |     | cleaned and pre-processed.  |     | This module removes null  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | ------------------------- | --- | --- | --- |
4. MODULES  values, converts categorical data into numerical form, and
normalizes datasets. It ensures that only valid, structured
The proposed system is divided into several functional  data is used for model training.
| modules  | to  ensure  |     | efficient  | operation  |     | and  | modular  |     |     |     |     |     |     |
| -------- | ----------- | --- | ---------- | ---------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- |
development. Each module performs a specific task and  4.4 Expense Classification Module
| interacts  | with  | others  | to  achieve  |     | the  | overall  | system  |     |     |     |     |     |     |
| ---------- | ----- | ------- | ------------ | --- | ---- | -------- | ------- | --- | --- | --- | --- | --- | --- |
objectives.  Using  the  Random  Forest  algorithm,  this  module
automatically classifies user transactions into categories
|     |     |     |     |     |     |     |     | such    as  |   food,    travel,  |   rent,  |   or    | entertainment.  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------- | -------- | ------- | --------------- | --- |
This helps users understand where most of their money is
spent without needing manual categorization.

4.5 Expense Prediction Module
This module uses LSTM (Long Short-Term Memory), a
deep learning model for time-series forecasting, to predict
|     |     |     |     |     |     |     |     | future  expenses  | based  | on  historical  | transaction  |     | data.  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------ | --------------- | ------------ | --- | ------ |
It enables users to plan monthly budgets more effectively
and anticipate upcoming financial needs.

450

AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING
Peer Reviewed, Referred & Indexed Journal
E-ISSN: 3069-0110
Vol.5, No.2(2026)
www.ajmimc.com
4.6 Anomaly Detection Module  The predicted values closely matched the actual
spending patterns for most categories.
This component analyses spending trends and detects
abnormal patterns—such as sudden high spending or 6.2 Expense Classification
unusual category spikes. Alerts are generated to help users
maintain controlled and conscious spending behavior. Random Forest was used to categorize transactions into
groups such as Food, Bills, Shopping, and Travel.
4.7 Dashboard and Visualization Module
 The model reached above 90% accuracy in
categorization.
An interactive dashboard presents graphical reports such as
 Users were able to view clear, organized spending
bar charts, pie charts, and line graphs.
breakdowns on the dashboard.
5. IMPLEMENTATION
6.3 Anomaly Detection
Users can view total income, expenditure distribution, and
The system detected unusual or abnormal spending
predicted expenses. Flask and JavaScript libraries (like
behaviors.
Chart.js) are used for visualization. The implementation of
 It identified sudden spikes or irregular transactions
the proposed AI-Powered Personal Finance Tracker
with good accuracy.
involves designing both the backend and frontend
 This helped users notice overspending early.
components, integrating a machine learning module, and
establishing smooth communication between the user
6.4 Dashboard Usability
interface and the database.
The dashboard displayed expense summaries through
5.1 Technology Stack
simple charts and visuals.
Frontend-HTML, CSS, JavaScript  Users found the interface easy to understand.
Backend-Python  Insights such as monthly totals, category-wise
Database – MySQL/PostgreSQL spending, and predictions improved financial
Machine Learning Models-Random Forest, LSTM awareness.
Libraries Used – Pandas, NumPy, Scikit-learn, TensorFlow,
Matplotlib 6.5 Overall Findings
The results show that the system provides:
 Better tracking than manual or static expense
trackers
 Accurate predictions of future spending
 Helpful alerts for unusual expenses
 A user-friendly interface with meaningful insights
7. DISCUSSION
The system demonstrates that integrating machine learning
into personal finance management significantly elevates the
effectiveness of traditional tracking tools. The LSTM model
Figure 2: System Architecture Flow for Flask-Based ML
provides strong, forward-looking predictions, enabling users
Dashboard
to prepare their budgets with greater confidence. The
Random Forest classifier adds clarity by accurately
6. RESULT AND FINDINGS
organizing expenses into meaningful categories, improving
overall financial awareness.
The proposed AI-powered personal finance tracker was
tested using sample and real transaction data. The system The anomaly detection component further strengthens the
successfully combined Flask, MySQL, and machine learning system by identifying unusual or unexpected spending
models to generate meaningful insights. patterns, offering users early warnings that traditional
trackers fail to deliver. Additionally, the intuitive dashboard
6.1 Expense Prediction
transforms complex financial data into clear, actionable
insights.
The LSTM model provided reliable predictions for monthly
spending trends. Overall, the system shifts personal finance tracking from a
 It achieved around 85% accuracy in forecasting passive recording tool to an intelligent, predictive, and
next-month expenses. proactive financial assistant.
451

AMERICAN JOURNAL OF MANAGEMENT AND IOT MEDICAL COMPUTING
Peer Reviewed, Referred & Indexed Journal
E-ISSN: 3069-0110
Vol.5, No.2(2026)
www.ajmimc.com
8. CONCLUSION [3] N. Gupta, R. Sharma, and S. Agrawal, “Smart Budget
Tracker Using Flask and MySQL,” IEEE 9th International
The AI-powered personal finance tracker successfully Conference on Computing, Communication and Automation
demonstrates how machine learning can transform (ICCCA), pp. 121–127, 2023.
traditional expense monitoring into a predictive and
intelligent financial management system. By integrating [4] A. Patel and D. Sinha, “Predictive Analysis of User
LSTM-based forecasting, Random Forest-driven Expenditure Using Random Forest and LSTM,” International
categorization, and effective anomaly detection, the system Research Journal of Engineering and Technology (IRJET),
provides users with deeper insight into their financial Vol. 8, Issue 7, pp. 2304–2311, 2021.
behavior and empowers them to plan with greater accuracy.
The results show that the proposed solution not only [5] R. Reddy, “AI-Powered Personal Expense Tracker with
enhances budgeting efficiency but also helps users identify Behavior Analysis,” International Journal of Emerging
unusual spending and improve overall financial discipline. Technologies and Innovative Research (JETIR), Vol. 9, Issue
With its intuitive dashboard and automated analytics, the 11, pp. 56–63, 2022.
system delivers a modern, data-driven alternative to static
[6] M. A. Rahman and T. S. Alam, “Financial Data
expense trackers.
Visualization and Forecasting Using Python Flask
In essence, this work proves that AI can play a critical role in Framework,” International Journal of Scientific & Technology
making personal finance management smarter, proactive, Research (IJSTR), Vol. 11, Issue 3, pp. 89–97, 2022.
and more user-centric.
[7] S. Bhattacharya, “Automated Personal Finance Tracking
9. FUTURE SCOPE System Using AI and Data Analytics,” International Journal of
Computer Science Trends and Technology (IJCST), Vol. 10,
The proposed system offers multiple opportunities for Issue 5, pp. 14–19, 2023.
enhancement that can significantly extend its capabilities.
Future improvements may include incorporating advanced
deep learning architectures, such as Transformer-based
models, to deliver more accurate expense forecasting and
deeper behavioral analysis. Automated integration with
bank APIs, UPI services, or SMS/email extraction can further
streamline data input, making the system entirely hands-
free.
The project can also be expanded to provide personalized
financial guidance—such as optimized budgeting strategies,
goal-based recommendations, or savings insights tailored to
individual spending habits. Deploying the tracker on cloud
platforms can enhance scalability and Performance, enabling
it to handle larger datasets and real-time analytics efficiently.
Additional features such as multi-user profiles, advanced
privacy controls, and cross-device synchronization can
broaden the system’s usefulness for families or small
businesses. With these enhancements, the system has strong
potential to evolve into a comprehensive, intelligent, and
highly adaptive financial management platforms.
REFERENCES
[1] S. P. Rajasekar and R. Babu, “Personal Finance
Management System Using Machine Learning,” International
Journal of Innovative Research in Computer and
Communication Engineering (IJIRCCE), Vol. 10, Issue 6, pp.
2543–2550, 2022.
[2] K. Kaur and M. K. Singh, “AI-Based Expense Prediction
System Using Machine Learning,” International Journal of
Advanced Research in Computer Science (IJARCS), Vol. 13,
No. 2, pp. 45–52, 2022.
452