---
conversion_metadata:
  converted_at: "2026-07-21T08:46:31Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Sireesha et al.pdf"
  source_pdf_sha256: "bbce4ef04a97bcbd4fc9d47f71067fb533594987767ea9e7239ec68ef2e19779"
  page_count: 8
  markdown_char_count: 65310
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of 
AI Electronics and Nexus Energy 
Peer Reviewed, Referred & Indexed Journal 
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

AI-BASEDPERSONAL FINANCE MANAGER (AI)

1Ms.B.Sireesha/ sireesha@city.ac.in

2Dr.K.Kiran Kumar / kirankommineni@city.ac.in

3,4,5,6Oruganti Lavanya, Shaik Keshan, Nalabotu Ramsai, Kolli Latheesh Kumar

DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING,

CHALAPATHI INSTITUTE OF TECHNOLOGY, MOTHADAKA, GUNTUR, ANDHRA

PRADESH, INDIA-522016.

classification,  budget  planning,  financial

forecasting, savings optimization, bill

ABSTRACT

The  rapid  growth  of  digital  financial

services  has  resulted  in  an  overwhelming

reminders,  and  anomaly  detection  for

increase

in

the  volume,  variety,  and

unusual transactions. The proposed system

complexity  of  personal  financial  data.

Users

frequently  struggle

to  monitor

spending

patterns,  manage

budgets,

forecast  savings,  and  make

informed

financial  decisions  due  to  a  lack  of  time,

financial  literacy,  or  analytical  tools.  To

address

these

challenges,  Artificial

Intelligence  (AI)  provides  an  effective

solution

by

enabling

automated,

personalized,  and  data-driven  financial

management.  This  paper  presents

the

design, development, and evaluation of an

AI-Based  Personal  Finance  Manager

capable

of

automating

expense

integrates  supervised  machine  learning,

deep

learning  models,  and  rule-based

intelligence  to  deliver  real-time  financial

insights tailored to individual user profiles.

The  system  architecture  consists  of  four

primary  modules:  data  acquisition,  AI-

driven

analytics,

prediction

and

recommendation engine, and user interface

layer.  Users  upload  or

link  financial

transaction  data,  which  is  then  cleaned,

tokenized,  and  classified  using  machine

learning  models  such  as  Random  Forest,

Gradient  Boosting  Machines,  or  LSTM-

based  sequence  models  for

long-term

Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026

2026, Vol 2 Issue 2 | 304

---

<!-- PAGE 2 -->

International Journal of 
AI Electronics and Nexus Energy 
Peer Reviewed, Referred & Indexed Journal 
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

financial

pattern

recognition.

The

making.  It  demonstrates

that  AI  can

recommendation

engine

generates

transform traditional financial tracking into

suggestions related to saving opportunities,

a  personalized,  intelligent,  and  proactive

budget  adherence,  expense

reduction,

financial assistant.

investment

options,

and

goal-based

financial  planning.  The

system  also

incorporates  reinforcement

learning

to

refine  recommendations  based  on  user

behavior  and  historical  response  patterns,

ensuring continuous improvement.

Experimental evaluation demonstrates that

the  model  achieves  high  accuracy

in

expense

categorization

(93–96%),

outperforming  conventional

rule-based

systems.  Financial

forecasting  using

LSTM  models  also  shows  promising

accuracy

in

predicting

monthly

expenditures,

recurring  payments,  and

potential

savings.  Usability

studies

indicate  that  users  strongly  benefit  from

automated

financial  planning

features,

especially real-time alerts and personalized

budget  recommendations.  The  integration

of  explainable  AI  techniques  enhances

transparency by providing justifications for

financial  suggestions,  thereby  improving

user trust.

Keywords

AI,  Personal  Finance,  Budget  Planning,

Financial  Forecasting,  Machine  Learning,

Deep Learning, Recommendation Systems

I. INTRODUCTION

Managing  personal  finances  effectively  is

a  critical  aspect  of  modern  living,  yet

many  individuals  face  obstacles  such  as

inadequate  financial  knowledge,  lack  of

time, and difficulty analyzing large sets of

digital  financial  data.  With  the  increasing

use  of  online  banking,  e-commerce,  UPI

payments,  and  digital  wallets,  users

generate

thousands

of

transactions

monthly,  making  manual  monitoring

impractical.

Traditional

finance-

management  tools  rely  heavily  on  static

rules,  offering  limited  personalization  and

insight.  In  contrast,  AI  brings  dynamic,

adaptive,  and  intelligent  capabilities  to

personal finance management.

Overall,

the

proposed  AI-powered

personal

finance  management

system

reduces  manual  effort,  enhances  financial

literacy,  and  supports  informed  decision-

An AI-Based Personal Finance Manager

leverages machine learning, deep learning,

and natural language processing to analyze

financial  data,  detect

trends,  classify

Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026

2026, Vol 2 Issue 2 | 305

---

<!-- PAGE 3 -->

International Journal of 
AI Electronics and Nexus Energy 
Peer Reviewed, Referred & Indexed Journal 
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

expenses,  forecast  future  spending,  and

data  cleaning,  normalization,  tokenization

generate  personalized  recommendations.

of  merchant

names,

and  mapping

These  intelligent  systems  can  assess  risk,

transaction

labels

to

standardized

identify  cost-saving  opportunities,  and

categories.

guide  users  toward  long-term  financial

stability.  Such  models  also

support

predictive  analytics  to  forecast  cash  flow,

predict  monthly  budgets,  and  evaluate  the

impact of financial decisions.

Machine learning models such as Random

Forest, SVM, and neural networks classify

transactions

into  categories

like  food,

transportation,  entertainment,

rent,  or

utilities.  An  LSTM  model  predicts  future

This  paper  highlights

the  design  and

expenses  and  revenue  streams  based  on

implementation  of  a  comprehensive  AI

historical  patterns.  Clustering  algorithms

system

that

automates

these

tasks,

like  K-Means  identify  unusual  spending

enabling users to make informed decisions

patterns  and  categorize  user  behavioral

without

requiring  advanced

financial

profiles.

skills.  The  introduction  also  discusses

current  challenges,  such  as  fragmented

data sources, security concerns, and model

interpretability.  The  proposed  solution

demonstrates  how  AI  bridges  these  gaps

through

automated

data

integration,

adaptive  algorithms,  and  customizable

interfaces.

The

system

also

includes

anomaly

detection  using  Isolation  Forest  to  alert

users  about  suspicious

transactions  or

overspending.  Final  recommendations  are

generated using a hybrid model combining

rule-based

logic,  supervised  ML,  and

reinforcement learning.

II. METHODOLOGY

III. RELATED WORK

The  methodology  involves  four  phases:

data  collection,  data  preprocessing,  AI

model

development,

and

recommendation  generation.  Financial

transaction  data  is  collected  from  banking

statements, e-commerce receipts, and user-

provided  inputs.  Preprocessing  includes

The  development  of  AI-based  personal

finance  management  systems  has  been

influenced  by  several  existing  financial

technologies,  machine  learning  models,

and  intelligent  recommendation  systems.

Traditional  personal  finance  applications

such  as  Mint  and  YNAB  (You  Need  A

Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026

2026, Vol 2 Issue 2 | 306

---

<!-- PAGE 4 -->

International Journal of 
AI Electronics and Nexus Energy 
Peer Reviewed, Referred & Indexed Journal 
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

Budget)  primarily

focus  on  expense

Natural  Language  Processing  (NLP)  has

tracking,

budgeting,

and

financial

also  been

incorporated

into

finance

reporting.  However,  these  systems  lack

management

systems

to

analyze

advanced  predictive

capabilities

and

transaction

descriptions,

categorize

personalized insights powered by artificial

expenses

automatically,

and  provide

intelligence.

Recent

research

has

explored

the

integration of machine learning algorithms

into  financial  management.  Supervised

chatbot-based  financial  assistance.  AI-

powered chatbots enhance user interaction

by  offering  real-time  financial  advice  and

answering user queries.

learning  models

such

as

Linear

Recommendation

systems

based

on

Regression,  Decision  Trees,  and  Random

collaborative  filtering  and  content-based

Forests have been widely used for expense

filtering  techniques  have  been  used  to

prediction  and  income  forecasting.  These

suggest  budgeting  strategies,  investment

models  analyze  historical  transaction  data

options,  and  saving  plans

tailored

to

to  identify  spending  patterns  and  predict

individual  users.  These  systems  improve

future  financial  behavior.  However,  their

personalization  but  may  suffer  from  cold-

accuracy  depends  heavily  on  data  quality

start problems when user data is limited.

and  may  not  adapt  well  to  dynamic  user

behavior.

Recent  advancements  include  the  use  of

reinforcement

learning

to

optimize

Deep

learning

techniques,

including

spending  behavior  and  financial  decision-

Recurrent  Neural  Networks  (RNNs)  and

making.  These  systems  learn  from  user

Long  Short-Term  Memory

(LSTM)

interactions  and  continuously

improve

networks, have been applied to time-series

recommendations over time.

financial  data  for  better  prediction  of

expenses and savings trends. These models

capture

temporal

dependencies

and

provide  more

accurate

forecasting

compared

to

traditional  methods.

Nonetheless,  they  require  large  datasets

and computational resources.

Despite

these  developments,  existing

systems  still  face  challenges  such  as  data

privacy concerns, lack of explainability in

AI  models,  and  limited  integration  of

multiple  AI  techniques  into  a  unified

platform. The proposed AI-Based Personal

Finance  Manager  aims  to  address  these

Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026

2026, Vol 2 Issue 2 | 307

---

<!-- PAGE 5 -->

International Journal of 
AI Electronics and Nexus Energy 
Peer Reviewed, Referred & Indexed Journal 
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

gaps by combining machine learning, deep

dependencies.  The  LSTM

forecasting

learning,  and  intelligent  recommendation

model  delivered  notable  performance  in

techniques  to  deliver  a  comprehensive,

predicting

monthly

expenditures,

adaptive,

and

user-centric

financial

achieving  a  Mean  Absolute  Error  (MAE)

management solution.

of  4.7%,  and  effectively  estimating

III. SYSTEM ARCHITECTURE

IV. RESULTS & DISCUSSION

The  experimental  evaluation  of  the  AI-

Based

Personal

Finance  Manager

demonstrates  significant  improvements  in

financial

tracking  accuracy,  prediction

performance, user engagement, and overall

decision-making support. A diverse dataset

of  transactional  logs  from  digital  wallets,

online banking statements, and categorized

receipts was used to test the robustness of

the  machine  learning  and  deep  learning

models.  The  Random  Forest–based

expense  classifier  achieved  an  accuracy

range  of  93%  to  96%,  outperforming

traditional

rule-based

categorization

systems, which typically plateau at around

75–80%  accuracy  due  to  rigid  keyword

recurring

payments

such

as

rent,

subscriptions,  and  utility  bills.  These

predictions help users anticipate upcoming

financial  obligations  and  manage  cash

flow more effectively.

User  behavior  analysis  using  clustering

algorithms  such  as  K-Means  revealed

distinctive  spending  patterns,  enabling  the

system

to

label  users

into

financial

personas

such  as  "budget-conscious,"

"impulsive

spender,"

or

"balanced

planner."  The  recommendation  engine’s

ability to personalize suggestions increased

user  satisfaction,  as  verified  by  a  small

usability  study  involving  50  participants.

Out  of  these  users,  84%  reported  better

awareness  of their spending, while 78%

claimed  increased  control  over  their

savings  after  using  the  system  for  one

month. Real-time alerts helped users avoid

unnecessary

spending,

and

anomaly

detection  effectively

flagged  unusual

transactions  with  a  precision  of  92%,

demonstrating

strong

fraud-prevention

ability.

Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026

2026, Vol 2 Issue 2 | 308

---

<!-- PAGE 6 -->

International Journal of 
AI Electronics and Nexus Energy 
Peer Reviewed, Referred & Indexed Journal 
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

Visualization

tools

integrated

into

the

dashboard  were

also

evaluated

for

usability. Heat maps of spending, monthly

trend  lines,  and  category-wise  pie  charts

helped users interpret their financial habits

quickly.  Feedback  highlighted  that  users

preferred  visual,  data-driven  insights  over

textual summaries. The study also revealed

that  younger  users  benefited  significantly

from  automated  budgeting,  while  older

users  valued

the  system’s  predictive

features more.

Discussion  of  results  indicates  that  AI-

driven

personalization

is

the

key

differentiator compared to existing finance

apps.  Unlike  static  budgeting  tools,  the

proposed

system  adapts  continuously

using reinforcement learning,  adjusting its

recommendations

according

to

user

compliance patterns. For example, if a user

consistently

ignores

dining-budget

warnings,

the  system  recalibrates  and

suggests  realistic,  achievable budget  goals

rather than fixed thresholds.

Overall,

the  results  confirm

that

the

proposed  AI-based  solution  provides  a

proactive  financial  assistant  rather  than

merely  a

tracking

tool.  Its  accuracy,

adaptability, and interpretability contribute

to  a  more  informed,  efficient,  and  user-

V. CONCLUSION

This  research  demonstrates  that  artificial

intelligence  can  significantly  transform

personal

financial  management

by

providing

users

with

accurate,

personalized,  and  actionable  insights.  The

AI-Based  Personal  Finance  Manager

effectively  overcomes

limitations  of

conventional

budgeting

applications

through  advanced  capabilities  such  as

automated expense classification, financial

forecasting,

anomaly

detection,

and

dynamic

recommendations.

The

integration  of  machine  learning  and  deep

learning

enables

the

system

to

continuously  learn  from  user  behavior,

adapt  to  evolving  financial  patterns,  and

improve prediction accuracy over time.

The system not only helps users track their

financial  activities  but  also  empowers

them  to  make  informed  decisions  by

predicting future expenditures and offering

strategic  guidance.  The  experimental

results  validate  its  effectiveness,  showing

considerable  improvements  in  accuracy,

user  engagement,  and  overall  financial

discipline.  Moreover,

the

inclusion  of

explainable  AI

fosters

transparency,

allowing  users  to  understand  the  basis

behind  predictions  and  recommendations,

friendly financial management experience.

thereby building trust.

Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026

2026, Vol 2 Issue 2 | 309

---

<!-- PAGE 7 -->

International Journal of 
AI Electronics and Nexus Energy 
Peer Reviewed, Referred & Indexed Journal 
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

From  a  practical  perspective,  the  model

[1]  K.  Patel  and  S.  Kumar,  “AI-driven

supports  a  wide  range  of  real-world

personal

finance

automation

using

applications such  as  automated budgeting,

machine  learning,”  IEEE  Access,  vol.  10,

savings  optimization,

fraud  detection,

pp.

45021–45033,

2022.

goal-based  planning,  and  early  warning

[2]  M.  Chen  et  al.,  “Deep  learning  for

systems  for  overspending.  Its  modular

financial

forecasting:  A

systematic

architecture

also

enables

seamless

review,” IEEE Trans. Neural Netw. Learn.

integration  with  banking  APIs,  digital

Syst., vol. 33, no. 9, pp. 4860–4877, 2022.

wallets, and financial advisory platforms.

[3]  A.  Singh  and  R.  Sharma,  “Personal

Future  work  may  focus  on  enhancing

security using blockchain for tamper-proof

financial  logs,  extending  the  system  to

support investment portfolio analysis using

reinforcement  learning,  and  incorporating

voice-driven

interaction

for

greater

accessibility.  Additionally,  scaling

the

system  with  federated

learning  could

enable  privacy-preserving  model  training

without

exposing

sensitive

personal

financial data.

In  conclusion,

the  AI-Based  Personal

Finance  Manager

demonstrates

the

transformative

potential

of  AI

in

improving

financial

literacy,

reducing

cognitive load, and supporting responsible

financial  behavior.  It  paves  the  way  for

intelligent,  automated,  and  user-centered

personal finance ecosystems.

REFERENCES

expense

prediction

using

LSTM

networks,”  in  Proc.  IEEE  ICMLA,  2021,

pp.

112–118.

[4]  L.  Brown  and  J.  Li,  “Automated

budgeting

using  machine

learning

classification,”

IEEE  Trans.  Consum.

Electron.,  vol.  67,  no.  3,  pp.  121–130,

2021.

[5]  H.  Zhao,  “Anomaly  detection

in

financial

transactions  using

isolation

forest,”  IEEE  Access,  vol.  9,  pp.  118990–

119002,

2021.

[6]  S.  Roy,  “Explainable  AI  for  personal

finance,”  in  Proc.  IEEE  Big  Data,  2022,

pp.

3042–3049.

[7]  F.  Ahmed  and  T.  George,  “Predictive

analytics  for  savings  and  expenditure

optimization,”  IEEE  Intell.  Syst.,  vol.  37,

no.

6,

pp.

58–67,

2022.

[8]  Y.  Park  and  K.  Lee,  “Reinforcement

learning-based  financial  decision  support

systems,” IEEE Trans. Syst. Man Cybern.,

vol.  52,  no.  4,  pp.  2450–2462,  2022.

Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026

2026, Vol 2 Issue 2 | 310

---

<!-- PAGE 8 -->

International Journal of 
AI Electronics and Nexus Energy 
Peer Reviewed, Referred & Indexed Journal 
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

[9]  S.  Das,  “User-centric  dashboards  for

AI-powered  finance  applications,”  IEEE

Comput.  Graph.  Appl.,  vol.  42,  no.  5,  pp.

95–103,

2022.

[10]  P.  Mahapatra  and  R.  Rao,  “Secure

integration  of  AI  financial  systems  with

blockchain,”  IEEE  Blockchain,  pp.  584–

592, 2023.

Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026

2026, Vol 2 Issue 2 | 311

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

International Journal of
AI Electronics and Nexus Energy
Peer Reviewed, Referred & Indexed Journal
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

AI-BASEDPERSONAL FINANCE MANAGER (AI)

1Ms.B.Sireesha/ sireesha@city.ac.in
2Dr.K.Kiran Kumar / kirankommineni@city.ac.in
3,4,5,6Oruganti Lavanya, Shaik Keshan, Nalabotu Ramsai, Kolli Latheesh Kumar

DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING,
CHALAPATHI INSTITUTE OF TECHNOLOGY, MOTHADAKA, GUNTUR, ANDHRA

PRADESH, INDIA-522016.

|     |     |     |     |     |     | classification,  |     | budget  | planning,  | financial  |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ---------- | ---------- | --- |
forecasting, savings optimization, bill
ABSTRACT

| The  rapid  | growth  |     | of  digital  |     | financial  |             |      |          |     |            |      |
| ----------- | ------- | --- | ------------ | --- | ---------- | ----------- | ---- | -------- | --- | ---------- | ---- |
|             |         |     |              |     |            | reminders,  | and  | anomaly  |     | detection  | for  |
services has resulted in an overwhelming
unusual transactions. The proposed system
| increase    | in  the     | volume,   |            | variety,  | and       |                  |             |          |                      |             |     |
| ----------- | ----------- | --------- | ---------- | --------- | --------- | ---------------- | ----------- | -------- | -------------------- | ----------- | --- |
| complexity  | of          | personal  | financial  |           | data.     |                  |             |          |                      |             |     |
|             |             |           |            |           |           | integrates       | supervised  |          | machine              | learning,   |     |
| Users       | frequently  | struggle  |            | to        | monitor   |                  |             |          |                      |             |     |
|             |             |           |            |           |           | deep             | learning    | models,  | and                  | rule-based  |     |
| spending    | patterns,   |           | manage     |           | budgets,  |                  |             |          |                      |             |     |
|             |             |           |            |           |           | intelligence to  |             | deliver  | real-time financial  |             |     |
| forecast    | savings,    | and       | make       | informed  |           |                  |             |          |                      |             |     |
insights tailored to individual user profiles.
financial decisions due to a lack of time,
| financial     | literacy,  | or           | analytical  | tools.      | To         |              |             |               |                     |     |           |
| ------------- | ---------- | ------------ | ----------- | ----------- | ---------- | ------------ | ----------- | ------------- | ------------------- | --- | --------- |
|               |            |              |             |             |            | The  system  |             | architecture  | consists            |     | of  four  |
| address       | these      | challenges,  |             | Artificial  |            |              |             |               |                     |     |           |
|               |            |              |             |             |            | primary      | modules:    |               | data  acquisition,  |     | AI-       |
| Intelligence  | (AI)       | provides     |             | an          | effective  |              |             |               |                     |     |           |
|               |            |              |             |             |            | driven       | analytics,  |               | prediction          |     | and       |
| solution      | by         | enabling     |             | automated,  |            |              |             |               |                     |     |           |
recommendation engine, and user interface
| personalized,  |     | and  data-driven  |        |           | financial  |              |        |         |     |                  |           |
| -------------- | --- | ----------------- | ------ | --------- | ---------- | ------------ | ------ | ------- | --- | ---------------- | --------- |
|                |     |                   |        |           |            | layer.       | Users  | upload  | or  | link  financial  |           |
| management.    |     | This              | paper  | presents  | the        |              |        |         |     |                  |           |
|                |     |                   |        |           |            | transaction  | data,  | which   | is  | then             | cleaned,  |
design, development, and evaluation of an
|           |           |     |          |     |          | tokenized,  | and  | classified  | using  | machine  |     |
| --------- | --------- | --- | -------- | --- | -------- | ----------- | ---- | ----------- | ------ | -------- | --- |
| AI-Based  | Personal  |     | Finance  |     | Manager  |             |      |             |        |          |     |
learning models such as Random Forest,
| capable  | of  | automating  |     |     | expense  |           |           |         |            |                 |       |
| -------- | --- | ----------- | --- | --- | -------- | --------- | --------- | ------- | ---------- | --------------- | ----- |
|          |     |             |     |     |          | Gradient  | Boosting  |         | Machines,  | or              | LSTM- |
|          |     |             |     |     |          | based     | sequence  | models  |            | for  long-term  |       |
Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026  2026, Vol 2 Issue 2 | 304

International Journal of
AI Electronics and Nexus Energy
Peer Reviewed, Referred & Indexed Journal
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper
financial  pattern  recognition.  The  making.  It  demonstrates  that  AI  can
recommendation  engine  generates  transform traditional financial tracking into
suggestions related to saving opportunities,  a  personalized,  intelligent,  and  proactive
budget  adherence,  expense  reduction,  financial assistant.
| investment  |     | options,  | and  |     | goal-based  |     |     |     |     |     |     |
| ----------- | --- | --------- | ---- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Keywords
| financial     | planning.        |                | The  | system    | also      |                |           |     |         |            |     |
| ------------- | ---------------- | -------------- | ---- | --------- | --------- | -------------- | --------- | --- | ------- | ---------- | --- |
| incorporates  |                  | reinforcement  |      | learning  | to        |                |           |     |         |            |     |
|               |                  |                |      |           |           | AI,  Personal  | Finance,  |     | Budget  | Planning,  |     |
| refine        | recommendations  |                |      | based     | on  user  |                |           |     |         |            |     |
Financial Forecasting, Machine Learning,
behavior and historical response patterns,
Deep Learning, Recommendation Systems
ensuring continuous improvement.
I. INTRODUCTION
Experimental evaluation demonstrates that
| the  model  |     | achieves  | high  | accuracy  | in  |     |     |     |     |     |     |
| ----------- | --- | --------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
Managing personal finances effectively is
| expense  |     | categorization  |     |     | (93–96%),  |              |         |             |     |          |      |
| -------- | --- | --------------- | --- | --- | ---------- | ------------ | ------- | ----------- | --- | -------- | ---- |
|          |     |                 |     |     |            | a  critical  | aspect  | of  modern  |     | living,  | yet  |
outperforming  conventional  rule-based  many  individuals  face  obstacles  such  as
systems.  Financial  forecasting  using  inadequate  financial  knowledge,  lack  of
| LSTM  | models  | also  | shows  |     | promising  |     |     |     |     |     |     |
| ----- | ------- | ----- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
time, and difficulty analyzing large sets of
| accuracy  |     | in  | predicting  |     | monthly  |     |     |     |     |     |     |
| --------- | --- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
digital financial data. With the increasing
| expenditures,  |     | recurring  |     | payments,  | and  |     |     |     |     |     |     |
| -------------- | --- | ---------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
use of online banking, e-commerce, UPI
| potential  | savings.  |        | Usability  |          | studies  |            |            |          |           |               |        |
| ---------- | --------- | ------ | ---------- | -------- | -------- | ---------- | ---------- | -------- | --------- | ------------- | ------ |
|            |           |        |            |          |          | payments,  | and        | digital  | wallets,  |               | users  |
| indicate   | that      | users  | strongly   | benefit  | from     |            |            |          |           |               |        |
|            |           |        |            |          |          | generate   | thousands  |          | of        | transactions  |        |
automated  financial  planning  features,  monthly,  making  manual  monitoring
especially real-time alerts and personalized  impractical.  Traditional  finance-
budget recommendations. The integration
|                  |     |     |             |     |           | management  | tools  | rely  | heavily  | on  | static  |
| ---------------- | --- | --- | ----------- | --- | --------- | ----------- | ------ | ----- | -------- | --- | ------- |
| of  explainable  |     | AI  | techniques  |     | enhances  |             |        |       |          |     |         |
rules, offering limited personalization and
transparency by providing justifications for
|            |               |     |          |     |            | insight.   | In  contrast,     | AI  | brings        | dynamic,  |     |
| ---------- | ------------- | --- | -------- | --- | ---------- | ---------- | ----------------- | --- | ------------- | --------- | --- |
| financial  | suggestions,  |     | thereby  |     | improving  |            |                   |     |               |           |     |
|            |               |     |          |     |            | adaptive,  | and  intelligent  |     | capabilities  |           | to  |
user trust.
personal finance management.
| Overall,  | the  | proposed  |     | AI-powered  |     |     |     |     |     |     |     |
| --------- | ---- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
An AI-Based Personal Finance Manager
| personal  | finance  |     | management  |     | system  |     |     |     |     |     |     |
| --------- | -------- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- |
leverages machine learning, deep learning,
reduces manual effort, enhances financial  and natural language processing to analyze
literacy, and supports informed decision-
|     |     |     |     |     |     | financial  | data,  detect  |     | trends,  | classify  |     |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | -------- | --------- | --- |
Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026  2026, Vol 2 Issue 2 | 305

International Journal of
AI Electronics and Nexus Energy
Peer Reviewed, Referred & Indexed Journal
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper
expenses,  forecast  future  spending,  and  data cleaning, normalization, tokenization
generate  personalized  recommendations.  of  merchant  names,  and  mapping
These intelligent systems can assess risk,  transaction  labels  to  standardized
| identify  | cost-saving  |         | opportunities,  |     |            | and  | categories.  |     |     |     |     |     |
| --------- | ------------ | ------- | --------------- | --- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- |
| guide     | users        | toward  | long-term       |     | financial  |      |              |     |     |     |     |     |
Machine learning models such as Random
| stability.  | Such  |     | models  | also  |     | support  |     |     |     |     |     |     |
| ----------- | ----- | --- | ------- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- |
Forest, SVM, and neural networks classify
predictive analytics to forecast cash flow,
|     |     |     |     |     |     |     | transactions  |     | into  | categories  | like  | food,  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ----------- | ----- | ------ |
predict monthly budgets, and evaluate the
|     |     |     |     |     |     |     | transportation,  |     | entertainment,  |     | rent,  | or  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------- | --- | ------ | --- |
impact of financial decisions.
utilities. An LSTM model predicts future
This  paper  highlights  the  design  and  expenses  and  revenue  streams  based  on
implementation  of  a  comprehensive  AI  historical  patterns.  Clustering  algorithms
system  that  automates  these  tasks,  like  K-Means  identify  unusual  spending
enabling users to make informed decisions  patterns  and  categorize  user  behavioral
| without  | requiring    |               | advanced  |       | financial   |     | profiles.  |         |            |           |         |            |
| -------- | ------------ | ------------- | --------- | ----- | ----------- | --- | ---------- | ------- | ---------- | --------- | ------- | ---------- |
| skills.  | The          | introduction  |           | also  | discusses   |     |            |         |            |           |         |            |
|          |              |               |           |       |             |     | The        | system  | also       | includes  |         | anomaly    |
| current  | challenges,  |               | such      | as    | fragmented  |     |            |         |            |           |         |            |
|          |              |               |           |       |             |     | detection  | using   | Isolation  |           | Forest  | to  alert  |
data sources, security concerns, and model
|                    |     |      |     |           |           |     | users  | about  | suspicious  |     | transactions  | or  |
| ------------------ | --- | ---- | --- | --------- | --------- | --- | ------ | ------ | ----------- | --- | ------------- | --- |
| interpretability.  |     | The  |     | proposed  | solution  |     |        |        |             |     |               |     |
overspending. Final recommendations are
demonstrates how AI bridges these gaps
generated using a hybrid model combining
| through   | automated    |     |     | data  | integration,  |     |             |     |         |             |      |      |
| --------- | ------------ | --- | --- | ----- | ------------- | --- | ----------- | --- | ------- | ----------- | ---- | ---- |
|           |              |     |     |       |               |     | rule-based  |     | logic,  | supervised  | ML,  | and  |
| adaptive  | algorithms,  |     |     | and   | customizable  |     |             |     |         |             |      |      |
reinforcement learning.
interfaces.
III. RELATED WORK
II. METHODOLOGY
|                   |     |     |           |     |       |          | The  development  |             |     | of  AI-based  |      | personal  |
| ----------------- | --- | --- | --------- | --- | ----- | -------- | ----------------- | ----------- | --- | ------------- | ---- | --------- |
| The  methodology  |     |     | involves  |     | four  | phases:  |                   |             |     |               |      |           |
|                   |     |     |           |     |       |          | finance           | management  |     | systems       | has  | been      |
data collection, data preprocessing, AI
|                 |     |               |              |     |            |      | influenced        | by  | several         | existing  |     | financial  |
| --------------- | --- | ------------- | ------------ | --- | ---------- | ---- | ----------------- | --- | --------------- | --------- | --- | ---------- |
| model           |     | development,  |              |     |            | and  |                   |     |                 |           |     |            |
|                 |     |               |              |     |            |      | technologies,     |     | machine         | learning  |     | models,    |
| recommendation  |     |               | generation.  |     | Financial  |      |                   |     |                 |           |     |            |
|                 |     |               |              |     |            |      | and  intelligent  |     | recommendation  |           |     | systems.   |
transaction data is collected from banking
|     |     |     |     |     |     |     | Traditional  |     | personal  | finance  | applications  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | -------- | ------------- | --- |
statements, e-commerce receipts, and user-
|           |          |     |                |     |           |     | such  as  | Mint  | and  | YNAB  | (You  | Need  A  |
| --------- | -------- | --- | -------------- | --- | --------- | --- | --------- | ----- | ---- | ----- | ----- | -------- |
| provided  | inputs.  |     | Preprocessing  |     | includes  |     |           |       |      |       |       |          |
Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026  2026, Vol 2 Issue 2 | 306

International Journal of
AI Electronics and Nexus Energy
Peer Reviewed, Referred & Indexed Journal
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper
Budget)  primarily  focus  on  expense  Natural  Language  Processing  (NLP)  has
tracking,  budgeting,  and  financial  also  been  incorporated  into  finance
reporting.  However,  these  systems  lack  management  systems  to  analyze
advanced  predictive  capabilities  and  transaction  descriptions,  categorize
personalized insights powered by artificial  expenses  automatically,  and  provide
| intelligence.  |     |     |     |     |     |     | chatbot-based  |     | financial  | assistance.  |     | AI- |
| -------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ------------ | --- | --- |
powered chatbots enhance user interaction
| Recent  | research  |     | has  | explored  |     | the  |     |     |     |     |     |     |
| ------- | --------- | --- | ---- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- |
by offering real-time financial advice and
integration of machine learning algorithms
answering user queries.
| into  financial  |     | management.  |     |     | Supervised  |     |     |     |     |     |     |     |
| ---------------- | --- | ------------ | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
learning  models  such  as  Linear  Recommendation  systems  based  on
Regression, Decision Trees, and Random  collaborative  filtering  and  content-based
Forests have been widely used for expense  filtering  techniques  have  been  used  to
prediction and income forecasting. These  suggest  budgeting  strategies,  investment
models analyze historical transaction data  options,  and  saving  plans  tailored  to
to identify spending patterns and predict  individual  users.  These  systems  improve
future financial behavior. However, their  personalization but may suffer from cold-
accuracy depends heavily on data quality  start problems when user data is limited.
and may not adapt well to dynamic user
|     |     |     |     |     |     |     | Recent  advancements  |     |     | include  | the  use  | of  |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | -------- | --------- | --- |
behavior.
|     |     |     |     |     |     |     | reinforcement  |     | learning  | to  | optimize  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | --------- | --- |
Deep  learning  techniques,  including  spending behavior and financial decision-
Recurrent  Neural  Networks  (RNNs)  and  making.  These  systems  learn  from  user
Long  Short-Term  Memory  (LSTM)  interactions  and  continuously  improve
networks, have been applied to time-series  recommendations over time.
| financial  | data  | for  | better  | prediction  |     | of  |          |        |                |     |           |     |
| ---------- | ----- | ---- | ------- | ----------- | --- | --- | -------- | ------ | -------------- | --- | --------- | --- |
|            |       |      |         |             |     |     | Despite  | these  | developments,  |     | existing  |     |
expenses and savings trends. These models
systems still face challenges such as data
| capture  | temporal  |     | dependencies  |     |     | and  |     |     |     |     |     |     |
| -------- | --------- | --- | ------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
privacy concerns, lack of explainability in
| provide       | more  |       | accurate     |        | forecasting  |     |              |                 |          |              |             |     |
| ------------- | ----- | ----- | ------------ | ------ | ------------ | --- | ------------ | --------------- | -------- | ------------ | ----------- | --- |
|               |       |       |              |        |              |     | AI  models,  | and             | limited  | integration  |             | of  |
| compared      |       | to    | traditional  |        | methods.     |     |              |                 |          |              |             |     |
|               |       |       |              |        |              |     | multiple     | AI  techniques  |          | into         | a  unified  |     |
| Nonetheless,  |       | they  | require      | large  | datasets     |     |              |                 |          |              |             |     |
platform. The proposed AI-Based Personal
and computational resources.
|     |     |     |     |     |     |     | Finance  Manager  |     | aims  | to  address  |     | these  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----- | ------------ | --- | ------ |
Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026  2026, Vol 2 Issue 2 | 307

International Journal of
AI Electronics and Nexus Energy
Peer Reviewed, Referred & Indexed Journal
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper
gaps by combining machine learning, deep  dependencies.  The  LSTM  forecasting
learning,  and  intelligent  recommendation  model  delivered  notable  performance  in
techniques  to  deliver  a  comprehensive,  predicting  monthly  expenditures,
adaptive,  and  user-centric  financial  achieving a Mean Absolute Error (MAE)
management solution.  of  4.7%,  and  effectively  estimating
|     |     |     |     |     | recurring  |     | payments  |     | such  | as  | rent,  |
| --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | ----- | --- | ------ |
III. SYSTEM ARCHITECTURE
|     |     |     |     |     | subscriptions,  |     | and  | utility  |     | bills.  | These  |
| --- | --- | --- | --- | --- | --------------- | --- | ---- | -------- | --- | ------- | ------ |
predictions help users anticipate upcoming
|     |     |     |     |     | financial  | obligations  |     |     | and  manage  |     | cash  |
| --- | --- | --- | --- | --- | ---------- | ------------ | --- | --- | ------------ | --- | ----- |
flow more effectively.
|     |     |     |     |     | User  behavior  |     | analysis  |     | using    | clustering  |           |
| --- | --- | --- | --- | --- | --------------- | --- | --------- | --- | -------- | ----------- | --------- |
|     |     |     |     |     | algorithms      |     | such      | as  | K-Means  |             | revealed  |
  distinctive spending patterns, enabling the
|     |     |     |     |     | system  | to  | label  | users  | into  | financial  |     |
| --- | --- | --- | --- | --- | ------- | --- | ------ | ------ | ----- | ---------- | --- |
IV. RESULTS & DISCUSSION

|                    |           |             |     |              | personas    | such  |                 | as  "budget-conscious,"  |     |            |           |
| ------------------ | --------- | ----------- | --- | ------------ | ----------- | ----- | --------------- | ------------------------ | --- | ---------- | --------- |
|                    |           |             |     |              | "impulsive  |       | spender,"       |                          | or  | "balanced  |           |
| The  experimental  |           | evaluation  |     | of  the  AI- |             |       |                 |                          |     |            |           |
|                    |           |             |     |              | planner."   | The   | recommendation  |                          |     |            | engine’s  |
| Based              | Personal  | Finance     |     | Manager      |             |       |                 |                          |     |            |           |
ability to personalize suggestions increased
demonstrates significant improvements in
|            |           |            |     |             | user  satisfaction,  |     |     | as  verified  |     | by  | a  small  |
| ---------- | --------- | ---------- | --- | ----------- | -------------------- | --- | --- | ------------- | --- | --- | --------- |
| financial  | tracking  | accuracy,  |     | prediction  |                      |     |     |               |     |     |           |
usability study involving 50 participants.
performance, user engagement, and overall
Out of these users, 84% reported better
decision-making support. A diverse dataset
awareness of their spending, while 78%
of transactional logs from digital wallets,
|     |     |     |     |     | claimed  | increased  |     | control  |     | over  | their  |
| --- | --- | --- | --- | --- | -------- | ---------- | --- | -------- | --- | ----- | ------ |
online banking statements, and categorized
|     |     |     |     |     | savings  | after  | using  | the  | system  |     | for  one  |
| --- | --- | --- | --- | --- | -------- | ------ | ------ | ---- | ------- | --- | --------- |
receipts was used to test the robustness of
month. Real-time alerts helped users avoid
| the  machine  | learning    | and       | deep            | learning      |                |              |            |               |                   |     |          |
| ------------- | ----------- | --------- | --------------- | ------------- | -------------- | ------------ | ---------- | ------------- | ----------------- | --- | -------- |
|               |             |           |                 |               | unnecessary    |              | spending,  |               | and               |     | anomaly  |
| models.       | The         | Random    | Forest–based    |               |                |              |            |               |                   |     |          |
|               |             |           |                 |               | detection      | effectively  |            |               | flagged           |     | unusual  |
| expense       | classifier  | achieved  |                 | an  accuracy  |                |              |            |               |                   |     |          |
|               |             |           |                 |               | transactions   |              | with       | a  precision  |                   | of  | 92%,     |
| range         | of  93%     | to  96%,  | outperforming   |               |                |              |            |               |                   |     |          |
|               |             |           |                 |               | demonstrating  |              | strong     |               | fraud-prevention  |     |          |
| traditional   | rule-based  |           | categorization  |               |                |              |            |               |                   |     |          |
ability.
systems, which typically plateau at around
| 75–80%  | accuracy  | due  | to  rigid  | keyword  |     |     |     |     |     |     |     |
| ------- | --------- | ---- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026  2026, Vol 2 Issue 2 | 308

International Journal of
AI Electronics and Nexus Energy
Peer Reviewed, Referred & Indexed Journal
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper

| Visualization  |     | tools  | integrated  | into       | the  | V. CONCLUSION  |     |     |     |     |     |
| -------------- | --- | ------ | ----------- | ---------- | ---- | -------------- | --- | --- | --- | --- | --- |
| dashboard      |     | were   | also        | evaluated  | for  |                |     |     |     |     |     |
usability. Heat maps of spending, monthly  This  research  demonstrates  that  artificial
trend lines, and category-wise pie charts  intelligence  can  significantly  transform
helped users interpret their financial habits  personal  financial  management  by
|           |           |     |              |       |        | providing  | users  |     | with  | accurate,  |     |
| --------- | --------- | --- | ------------ | ----- | ------ | ---------- | ------ | --- | ----- | ---------- | --- |
| quickly.  | Feedback  |     | highlighted  | that  | users  |            |        |     |       |            |     |
personalized, and actionable insights. The
preferred visual, data-driven insights over
|     |     |     |     |     |     | AI-Based  | Personal  |     | Finance  | Manager  |     |
| --- | --- | --- | --- | --- | --- | --------- | --------- | --- | -------- | -------- | --- |
textual summaries. The study also revealed
|     |     |     |     |     |     | effectively  | overcomes  |     | limitations  |     | of  |
| --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ------------ | --- | --- |
that younger users benefited significantly
from  automated  budgeting,  while  older  conventional  budgeting  applications
users  valued  the  system’s  predictive  through  advanced  capabilities  such  as
| features more.  |     |          |            |       |     | automated expense classification, financial  |                   |     |             |     |      |
| --------------- | --- | -------- | ---------- | ----- | --- | -------------------------------------------- | ----------------- | --- | ----------- | --- | ---- |
|                 |     |          |            |       |     | forecasting,                                 | anomaly           |     | detection,  |     | and  |
| Discussion      | of  | results  | indicates  | that  | AI- |                                              |                   |     |             |     |      |
|                 |     |          |            |       |     | dynamic                                      | recommendations.  |     |             |     | The  |
driven  personalization  is  the  key  integration of machine learning and deep
differentiator compared to existing finance  learning  enables  the  system  to
| apps.  Unlike  |         | static  | budgeting  | tools,        | the  |               |               |            |       |            |      |
| -------------- | ------- | ------- | ---------- | ------------- | ---- | ------------- | ------------- | ---------- | ----- | ---------- | ---- |
|                |         |         |            |               |      | continuously  | learn         | from       | user  | behavior,  |      |
| proposed       | system  |         | adapts     | continuously  |      |               |               |            |       |            |      |
|                |         |         |            |               |      | adapt         | to  evolving  | financial  |       | patterns,  | and  |
using reinforcement learning, adjusting its
improve prediction accuracy over time.
| recommendations  |     |     | according  | to  | user  |     |     |     |     |     |     |
| ---------------- | --- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- |
compliance patterns. For example, if a user  The system not only helps users track their
|               |      |          |               |                |      | financial  | activities  | but       | also  | empowers   |     |
| ------------- | ---- | -------- | ------------- | -------------- | ---- | ---------- | ----------- | --------- | ----- | ---------- | --- |
| consistently  |      | ignores  |               | dining-budget  |      |            |             |           |       |            |     |
|               |      |          |               |                |      | them       | to  make    | informed  |       | decisions  | by  |
| warnings,     | the  | system   | recalibrates  |                | and  |            |             |           |       |            |     |
predicting future expenditures and offering
suggests realistic, achievable budget goals
|     |     |     |     |     |     | strategic  | guidance.  |     | The  | experimental  |     |
| --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---- | ------------- | --- |
rather than fixed thresholds.
results validate its effectiveness, showing
| Overall,   | the          | results  | confirm    | that            | the   |                    |               |          |          |                |     |
| ---------- | ------------ | -------- | ---------- | --------------- | ----- | ------------------ | ------------- | -------- | -------- | -------------- | --- |
|            |              |          |            |                 |       | considerable       | improvements  |          |          | in  accuracy,  |     |
| proposed   | AI-based     |          | solution   | provides        | a     |                    |               |          |          |                |     |
|            |              |          |            |                 |       | user  engagement,  |               | and      | overall  | financial      |     |
| proactive  | financial    |          | assistant  | rather          | than  |                    |               |          |          |                |     |
|            |              |          |            |                 |       | discipline.        | Moreover,     |          | the      | inclusion      | of  |
| merely     | a  tracking  |          | tool.      | Its  accuracy,  |       |                    |               |          |          |                |     |
|            |              |          |            |                 |       | explainable        | AI            | fosters  |          | transparency,  |     |
adaptability, and interpretability contribute
|     |     |     |     |     |     | allowing  | users  | to  understand  |     | the  | basis  |
| --- | --- | --- | --- | --- | --- | --------- | ------ | --------------- | --- | ---- | ------ |
to  a  more  informed,  efficient,  and  user- behind predictions and recommendations,
friendly financial management experience.  thereby building trust.
Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026  2026, Vol 2 Issue 2 | 309

International Journal of
AI Electronics and Nexus Energy
Peer Reviewed, Referred & Indexed Journal
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper
From  a  practical  perspective,  the  model  [1]  K.  Patel  and  S.  Kumar,  “AI-driven
supports  a  wide  range  of  real-world  personal  finance  automation  using
applications such as automated budgeting,  machine learning,” IEEE Access, vol. 10,
savings  optimization,  fraud  detection,  pp.  45021–45033,  2022.
goal-based  planning,  and  early  warning  [2]  M.  Chen  et  al.,  “Deep  learning  for
systems  for  overspending.  Its  modular  financial  forecasting:  A  systematic
architecture  also  enables  seamless  review,” IEEE Trans. Neural Netw. Learn.
integration  with  banking  APIs,  digital  Syst., vol. 33, no. 9, pp. 4860–4877, 2022.
wallets, and financial advisory platforms.  [3]  A.  Singh  and  R.  Sharma,  “Personal
|         |       |      |        |     |            |     | expense  |     | prediction  |     | using  | LSTM  |     |
| ------- | ----- | ---- | ------ | --- | ---------- | --- | -------- | --- | ----------- | --- | ------ | ----- | --- |
| Future  | work  | may  | focus  | on  | enhancing  |     |          |     |             |     |        |       |     |
networks,” in Proc. IEEE ICMLA, 2021,
security using blockchain for tamper-proof
|            |        |            |     |      |         |     | pp.      |        |      |     |                  | 112–118.  |     |
| ---------- | ------ | ---------- | --- | ---- | ------- | --- | -------- | ------ | ---- | --- | ---------------- | --------- | --- |
| financial  | logs,  | extending  |     | the  | system  | to  |          |        |      |     |                  |           |     |
|            |        |            |     |      |         |     | [4]  L.  | Brown  | and  | J.  | Li,  “Automated  |           |     |
support investment portfolio analysis using
|     |     |     |     |     |     |     | budgeting  |     | using  | machine  |     | learning  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | -------- | --- | --------- | --- |
reinforcement learning, and incorporating
|                 |     |                |     |      |          |          | classification,”  |       | IEEE  | Trans.  |          | Consum.   |     |
| --------------- | --- | -------------- | --- | ---- | -------- | -------- | ----------------- | ----- | ----- | ------- | -------- | --------- | --- |
| voice-driven    |     | interaction    |     | for  |          | greater  |                   |       |       |         |          |           |     |
|                 |     |                |     |      |          |          | Electron.,        | vol.  | 67,   | no.     | 3,  pp.  | 121–130,  |     |
| accessibility.  |     | Additionally,  |     |      | scaling  | the      |                   |       |       |         |          |           |     |
2021.
| system   | with                | federated  |            | learning  |           | could  |            |               |           |     |            |            |     |
| -------- | ------------------- | ---------- | ---------- | --------- | --------- | ------ | ---------- | ------------- | --------- | --- | ---------- | ---------- | --- |
|          |                     |            |            |           |           |        | [5]  H.    | Zhao,         | “Anomaly  |     | detection  |            | in  |
| enable   | privacy-preserving  |            |            | model     | training  |        |            |               |           |     |            |            |     |
|          |                     |            |            |           |           |        | financial  | transactions  |           |     | using      | isolation  |     |
| without  | exposing            |            | sensitive  |           | personal  |        |            |               |           |     |            |            |     |
forest,” IEEE Access, vol. 9, pp. 118990–
financial data.
|     |     |     |     |     |     |     | 119002,  |     |     |     |     |     | 2021.  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | ------ |
[6] S. Roy, “Explainable AI for personal
| In  conclusion,  |     | the  | AI-Based  |     | Personal  |     |     |     |     |     |     |     |     |
| ---------------- | --- | ---- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
finance,” in Proc. IEEE Big Data, 2022,
| Finance         | Manager  |            | demonstrates  |     |     | the  |      |     |     |     |             |     |     |
| --------------- | -------- | ---------- | ------------- | --- | --- | ---- | ---- | --- | --- | --- | ----------- | --- | --- |
|                 |          |            |               |     |     |      | pp.  |     |     |     | 3042–3049.  |     |     |
| transformative  |          | potential  |               | of  | AI  | in   |      |     |     |     |             |     |     |
[7] F. Ahmed and T. George, “Predictive
| improving  |     | financial  | literacy,  |     | reducing  |     |            |      |          |      |              |     |     |
| ---------- | --- | ---------- | ---------- | --- | --------- | --- | ---------- | ---- | -------- | ---- | ------------ | --- | --- |
|            |     |            |            |     |           |     | analytics  | for  | savings  | and  | expenditure  |     |     |
cognitive load, and supporting responsible
optimization,” IEEE Intell. Syst., vol. 37,
| financial     | behavior.   |     | It  paves  |                     | the  way  | for  |      |     |      |         |     |     |        |
| ------------- | ----------- | --- | ---------- | ------------------- | --------- | ---- | ---- | --- | ---- | ------- | --- | --- | ------ |
|               |             |     |            |                     |           |      | no.  | 6,  | pp.  | 58–67,  |     |     | 2022.  |
| intelligent,  | automated,  |     |            | and  user-centered  |           |      |      |     |      |         |     |     |        |
[8] Y. Park and K. Lee, “Reinforcement
personal finance ecosystems.
|              |     |     |     |     |     |     | learning-based                            |      | financial  |             | decision  | support  |        |
| ------------ | --- | --- | --- | --- | --- | --- | ----------------------------------------- | ---- | ---------- | ----------- | --------- | -------- | ------ |
| REFERENCES   |     |     |     |     |     |     | systems,” IEEE Trans. Syst. Man Cybern.,  |      |            |             |           |          |        |
|              |     |     |     |     |     |     | vol.  52,                                 | no.  | 4,  pp.    | 2450–2462,  |           |          | 2022.  |
Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026  2026, Vol 2 Issue 2 | 310

International Journal of
AI Electronics and Nexus Energy
Peer Reviewed, Referred & Indexed Journal
                                         ISSN: 3070-0515                                    www.zesterapublications.com                                  Original Research Paper
| [9] S. Das, “User-centric dashboards  |          |                 |     | for   |
| ------------------------------------- | -------- | --------------- | --- | ----- |
| AI-powered                            | finance  | applications,”  |     | IEEE  |
Comput. Graph. Appl., vol. 42, no. 5, pp.
| 95–103,       |            |              |           | 2022.     |
| ------------- | ---------- | ------------ | --------- | --------- |
| [10]  P.      | Mahapatra  | and          | R.  Rao,  | “Secure   |
| integration   | of  AI     | financial    | systems   | with      |
| blockchain,”  | IEEE       | Blockchain,  |           | pp.  584– |
592, 2023.

Received: 03-03-2026 | Accepted: 01-04-2026 | Published: 19-04-2026  2026, Vol 2 Issue 2 | 311