---
conversion_metadata:
  converted_at: "2026-07-21T08:41:43Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Shuryhin & Zinovatna.pdf"
  source_pdf_sha256: "0060aab621d432a60c3c3e1967f4c728a024b702e939addfeed6368c67f785e8"
  page_count: 11
  markdown_char_count: 107059
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

DOI: https://doi.org/10.15276/aait.07.2024.24 
UDC 004.414.32

Recommendation system for financial decision-making using 
Artificial intelligence

Kostiantyn A. Shuryhin1)  
ORCID: https://orcid.org/0009-0002-1000-303X; ksurygin5@gmail.com 
Svitlana L. Zinovatna1)  
ORCID: https://orcid.org/0000-0002-9190-6486; zinovatnaya.svetlana@op.edu.ua. Scopus Author ID: 57219779480 
1) Odesa Polytechnic National University, Shevchenko Ave. Odesa, 65044, Ukraine

ABSTRACT

The rapid expansion of artificial intelligence (AI) in consumer markets presents challenges, particularly in how cognitive biases 
influence  financial  decision-making.  These biases  can lead to  irrational  spending, raising  ethical  concerns  about AI’s  role in  such 
applications.  This  research  explores  how  AI  can  enhance  decision-making  effectiveness  and  support  consumers  in  making  more 
rational financial choices. The focus is on developing an intelligent financial management system that applies modern AI algorithms 
to  analyze  financial  behavior,  detect  anomalies,  and  offer  personalized  recommendations.  The  article  considers  a  system  for 
generating personalized financial recommendations based on large language models, which uses transaction history, predicted costs, 
and anomaly information to generate individual advice.  Techniques include using Isolation Forest for identifying atypical financial 
actions and a combination of ARIMA and LSTM models for budget forecasting. The research also considers integrating these models 
with  large  language  models  (LLMs)  to  generate  personalized recommendations.  The  methodological  part  of  the  work includes an 
analysis of existing models and their areas of application, defining data types and structures for processing, developing a system that 
integrates the available models, and testing it. The process of generating recommendations is described, which includes the stages of 
processing input  data,  forming  context,  generating  recommendations  and evaluating  them  taking  into  account  user  characteristics, 
such  as  risk  level,  financial  goals  and  preferences.  The  generated  recommendations  are  aimed  at  optimizing  the  user's  financi al 
behavior and can be adapted to different income levels. Special attention is paid  to the ethical aspects of the system, which include 
ensuring  confidentiality,  fairness  and  transparency,  as  well  as  the  importance  of  supporting  user  autonomy  in  making  financial 
decisions.  The  system  promotes  responsible  financial  behavior  by  helping  to  avoid  impulsive  spending  and  increasing  financial 
awareness without manipulation or imposing specific decisions.

Keywords: Artificial Intelligence; machine learning; cognitive biases; financial decisions; ethics

For citation: Shuryhin K. A., Zinovatna S. L. “Recommendation system for financial decision-making using Artificial Intelligence”. Applied 
Aspects of Information Technology. 2024; Vol.7 No.4: 348–358. DOI: https://doi.org/10.15276/aait.07.2024.24

INTRODUCTION

issues

The modern financial landscape faces numerous 
challenges,  among  which  key 
include 
ineffective  financial  management  and  financial 
illiteracy,  both  among  individual  consumers  and 
organizations.  Many 
lack  sufficient 
knowledge 
to  make  sound  financial  decisions, 
making  them  vulnerable  to  aggressive  marketing 
strategies.  This  is  especially  relevant  in  the  context 
of increasingly sophisticated AI-enhanced marketing 
techniques  that  can  manipulate  consumer  behavior, 
promoting irrational expenditures.

individuals

Research  in  behavioral  economics  shows  that 
cognitive  biases,  such  as  loss  aversion  or  framing 
effects,  significantly  impact  consumer  decision-
making,  often  leading  to  deviations  from  rational 
behavior.  This  highlights  the  need  for  intelligent 
systems  that  can  help  consumers  overcome  these 
financial 
biases

and  make  more

informed

© Shuryhin K., Zinovatna S., 2024

decisions.AI  is  already  demonstrating  considerable 
potential in the financial sector, particularly through 
its  ability  to  analyze  large  volumes  of  data  and 
uncover  hidden  patterns.  For  example,  systems  that 
combine  cognitive  psychology  with  machine 
learning algorithms can personalize user experiences 
and  offer  recommendations  based  on  an  analysis  of 
their  behavior  and  preferences.  This  enables AI  not 
only  to  predict  consumer  behavior  but  also  to 
provide  more  accurate 
for 
financial planning, budgeting, and investing.

recommendations

The  goal  of  this  study  is  to  develop  principles 
for  creating  financial  recommendations  using  AI 
models, regardless of user’s income levels.

1. LITERATURE OVERVIEW

At  present,  there  is  a  significant  body  of  work 
about

information

extensive

provides

that 
recommendation systems (RS).

In [1], theoretical studies for RS are described, 
along  with  new  developments  of  applications, 
prototypes and real examples of such systems.

This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/deed.uk)

348

Software engineering and systems analysis

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

---

<!-- PAGE 2 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

Recommendation systems play a crucial role in 
many areas: e-commerce websites, online shopping, 
dating  apps,  social  media,  digital  marketing,  online 
advertising,  etc.,  as 
they  provide  users  with 
personalized  recommendations  and  feedback  based 
on their preferences and choices [2].

Sources  [3,  4]  describe  the  main  models 
underlying  the  construction  of  RS,  highlight  the 
primary  sectors  where  such  systems  are  used,  and 
outline  the  distribution  of  publications  for  various 
application areas. It is noted that e-commerce, which 
can  be  considered  a  part  of  financial  services, 
accounts for 17% of all reviewed studies.

Authors  in  [5]  focus  on  the  psychological 
mechanisms 
impacts  user 
through  which  RS 
satisfaction. It is shown that the type  of search goal 
types  of  recommendations. 
interacts  with 
Psychological reactance, a resistance that users may 
feel  towards  RS  recommendations  perceived  as  a 
threat to their freedom of choice, is also discussed as 
reject 
one  of 
recommendations.

reasons  users

the  primary

the

In RS, there are two roles: predicting the value 
(how a user will rate a resource)  [6]. The  education 
sector is used as an example in this study.

the

When

it  comes

specifically

financial  sector, 
to 
publications  most  often  describe  recommendations 
financial  consulting. 
for 
systems 
Financial  consultants  can  improve  the  trading  skills 
of  investors;  however,  the  presences  of  trading 
experience  and  professional  complexity  negatively 
correlates  with  the  use  of  financial  consultations, 
meaning  that  more  experienced  investors  are  less 
likely  to  use  recommendations  [7].  There  is  also 
study  that  found  the  connection  between  financial 
consultations  and  subjective  well-being  is  stronger 
for  households 
income 
growth, individuals who do not consider themselves 
financially knowledgeable, and those  with a weaker 
internal  locus  of  control  [8].  The  foundation  of  the 
research is the idea that households face the need to 
make  decisions  with  financial  consequences  every 
day,  and  the  ultimate  goal  of  decision-making  is  to 
achieve  outcomes  that  enhance  the  quality-of-life 
experiences by individuals (subjective well-being).

that  have  experienced

investor’s

that  reflect  an

For providing financial consultations, the GPT-
4 bot can be used, which “offers specific investment 
individual 
portfolios 
circumstances,  such  as  risk  tolerance,  risk  capacity, 
and preference for stability”. 
There  are  other

financial  sectors  where 
recommendation  principles  can  be  applied,  such  as 
banking,  stocks,  and  insurance  [10],  in  these  areas, 
users  are  viewed  as  active  entities  who  engage  in

interactions  (such  as  browsing,  selling,  buying, 
rating etc.) within the system.

In  [11],  it  was  noted  that  a  certain  limit  of 
development has been reached for recommendations 
systems  in  the  financial  sector.  At  the  same  time, 
such  systems  are  “considered  to  be  intelligent  and 
experienced  financial  managers,  well-informed  and 
aware of each client’s financial situations, regardless 
of  their  location”.  Further  expenditures  on  their 
promotion can only be justified by economic impact.  
Recommendation  systems  exist  for  banks;  in 
particular,  such  system  can  provide  personalized 
recommendations on spending opportunities near the 
user  based  on  their  credit  card  usage  history  and 
geolocation  data  [12],  thereby  taking  context  into 
account. However, the authors of the study highlight 
the  aspect  that  user  preferences  are  unstable  and 
highly  dependent  on  the  user’s  actual  goal.  Since 
these  systems  focus  on  money  management  and 
spending opportunities, there is a significant need to 
explain the systems’ results.

In  [13]  a  recommendation  system  is  presented 
for  managing  and  utilizing  three  components  of 
salary:  savings,  investments  and  expenses.  The 
system 
salary-related 
recommendations,  but  it  concludes  that  such  a 
system is useful when a person has a high income.

specifically  on

focuses

recommendations  systems

A  large  number  of  studies  are  dedicated  to  the 
development  of 
for 
financial  products.  Specifically,  [14]  proposes  an 
innovation  that  involves  the  seamless  integration  of 
Transformers,  transfer  learning  and  graph  neural 
networks  (GNN) 
issues  faced  by 
to  address 
traditional  methods,  such  as  user  cold  start,  data 
sparsity, and complex relationship modeling. In [15] 
are 
generative 
considered  as  a  predominant AI  technique/model  in 
[16]  an 
various 
interpretable  model 
financial 
service recommendations it proposed, based on self-
attention mechanisms, by combining the long short-
term  memory  (LSTM)  model  and  the  topic  model 
Linear  Discriminant  Analysis  (LDA)  with  AI 
support.

In 
for  personalized

recommendation  systems.

adversarial  networks

(GANs)

In [17], the  need to understand the specifics  of 
the  recommendation  system  environment  and  the 
expected  impact  of  the  system  on  its  users  is 
emphasized. It is necessary to evaluate the quality of 
recommendation  systems  not  only  in  terms  of  the 
accuracy of the recommendations provided but also 
by considering the diversity and novelty of the items 
included  in  the  recommendations  [5,  17].  Users  are 
likely  to  follow  recommendations  only  if  they  have 
developed  trust  in  the  system  over  time.  Therefore,

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

Software engineering and systems analysis

349

---

<!-- PAGE 3 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

recommendations should also be evaluated based on 
whether the provided recommendation was utilized. 
Acceptance  of  AI-generated  recommendations 
is a function of attitudes toward AI, trust, perceived 
accuracy,  and  the  level  of  uncertainty  [18].  The 
described 
attitude-perception-intention  model 
defines the basic psychological mechanism by which 
users decide to accept AI-supported advice.

Consumers  often  prefer  human  interaction  in 
fields  characterized  by  high  consumer  involvement, 
such  as  healthcare  and  financial  services,  over 
computer-generated advice [19]. However, AI is still 
rapidly  being  implemented  in  the  financial  sector. 
The  concept  of  a  robo-advisor  has  even  emerged, 
offering  “personalized  risk  analysis  and  real-time 
service  adjustments  based  on  self-service,  requiring 
minimal  human  interaction”  [20].  A  robo-advisor 
essentially  offers  software  for  retail  investors  who 
lack sufficient experience or funds to hire a personal 
financial 
potential 
Neuro-Linguistic 
enhancement, 
Programming  (NLP)  technology  into  robo-advisor 
software  could  improve  AI  chatbots,  increasing 
customer  satisfaction  and  the  likelihood  that  clients 
will follow portfolio guidance.

[21].  As

integrating

consultant

a

Privacy  and  security  are  important  issue  for 
recommendation  systems.  Even  with  excellent 
performance,  users  find  it  difficult  to  trust  such 
systems due to opacity and privacy concerns [22].

In general, the ethical implications of using AI-
based recommendation systems are a distinct area of 
research.  For  instance,  [23]  provides  a  conceptual 
assessment  of  human  autonomy  when  using  a 
universal  recommendation  system.  The  concept  of 
human autonomy is defined in [24] as “the ability to 
be  one’s  own person, to live  one’s life according to 
reasons and motives that are taken as one’s own, and 
not  the  product  of  manipulative  or  external  forces 
that distort, thus being independent”. The conclusion 
of  the  study  [22]  is  that  not  everything  needs  to  be 
recommended,  and  people  should  be  aware  of  the 
potential 
impact  of  automated  recommendation 
technologies.

Thus, when designing recommendation systems 
to  support  financial  decision-making,  the  following 
aspects must be considered; accuracy, completeness, 
privacy, and adherence to ethical standards.

2. USING AI MODELS TO ADDRESS THE 
ISSUE OF FINANCIAL RECOMMENDATION 
FORMATION

In  the  financial  sector,  AI  is  also  used  for 
detecting  anomalous  financial 
transactions  and 
preventing fraud. The Isolation Forest model, which

is well-suited for anomaly detection, can be applied 
to  analyze  consumer  behavior,  particularly 
to 
identify spontaneous expenses or impulsive financial 
decisions. Additionally, deep neural networks (CNN, 
RNN)  are  actively  used  to  analyze  consumer  data 
and  predict  behavioral  patterns,  enabling 
the 
optimization of marketing strategies.

AI  also  plays  an  important  role  in  financial 
recommendation systems that help users choose the 
best financial products or services. Algorithms based 
on collaborative filtering and deep learning methods 
are used to analyze user behavior and create targeted 
offers  that  meet  their  needs.  These  systems  can 
significantly 
financial 
decisions by reducing the impact of cognitive biases 
on consumer behavior.

the  quality  of

improve

2.1. Detection  of  anomalous  expenses  using

isolation forest

The concept of Isolation Forest was used as the 
basis for detecting anomalous user expenses, with its 
core  idea  being  the  isolation  of  anomalies  from 
normal data.

randomly

To  achieve  this  goal,  a  binary  tree  is  initially 
features  and 
created  by 
distributing values. The next step is to determine the 
anomaly  score  by  calculating  the  path  length  from 
the root of the tree to the terminal node. The shortest 
paths are considered anomalies.

selecting

The  mathematical  basis  for  calculating  the

expected path length is the following formula:

𝐸(ℎ(𝑥)) = 𝑐(𝑛) +

2𝑙𝑜𝑔𝑙𝑜𝑔 (𝑛−1) −

2(𝑛−1)
𝑛
,

𝑛

is

the  average  path

where  𝑐(𝑛) 
for 
unsuccessful  searches  in  a  binary  tree;  ℎ(𝑥)  is  the 
path  length  for  point  𝑥  in  the  isolation  tree  (the 
number  of  edges  traversed  from  the  root  to  the 
terminal node).

length

𝑐(𝑛) = 2𝐻(𝑛 − 1) − (

2(𝑛 − 1)
𝑛

),

where 𝐻(𝑖)  is the harmonic number, calculated as:

𝐻(𝑖) = ∑

1
𝑖
𝑘=1 . 
𝑘

The  anomaly  score  for  a  point  is  calculated

based on the average path length across all trees:

−
𝑠(𝑥, 𝑛) = 2

𝐸(ℎ(𝑥))
𝑐(𝑛)

,

where  𝑠(𝑥, 𝑛) ≈ 1,  if  the  point  is  an  anomaly;  
𝑠(𝑥, 𝑛) ≈ 0.5,  if the point is normal.

350

Software engineering and systems analysis

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

---

<!-- PAGE 4 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

2.2.  Budget  prediction  using  ARIMA  and

LSTM

Information Criterion (BIC), the model is trained on 
the training data and used for short-term forecasting.

To predict user budget expenses, a combination 
of two  models  was used: ARIMA (Auto Regressive 
Integrated  Moving  Average)  and  LSTM  (Long 
Short-Term  Memory).  Both  models  are  designed  to 
work  with  time  series  data  but  have  different 
approaches  to  solving  the  problem.  In  this  context, 
ARIMA  was  used  for  short-term  forecasts,  and 
LSTM  for  long-term  forecasts,  allowing  for  more 
accurate  and  stable  predictions.  The  first  stage  of 
prediction  is  data  preparation.  This  includes  data 
cleaning, handling missing values, and standardizing 
the  data  format.  The  main  focus  is  on  removing 
trends and seasonality from the data series, as these 
factors can affect the accuracy of the forecast.

2.2.1. ARIMA model

The  ARIMA  model

consists  of

three

components:

•  AR  (AutoRegressive)  component,  which 
models the dependency between an observation and 
several previous observations.

•  I  (Integrated)  component,  used  to  eliminate

non-stationarity.

•  MA  (Moving  Average)  component,  which 
models the dependency between an observation and 
the forecast error.

Mathematically 
described by the equation:

the  ARIMA(p,  d,  q)

is

𝑦𝑡 = 𝑐 + 𝜙1𝑦𝑡−1 + 𝜙2𝑦𝑡−2 + ⋯ + 𝜙𝑝𝑦𝑡−𝑝 +
𝜃1𝜖𝑡−1 + 𝜃2𝜖𝑡−2 + ⋯ + 𝜃𝑞𝜖𝑡−𝑞 + 𝜖𝑡, 
where 𝑦𝑡 is the value  of the series at time 𝑡, 𝜙𝑖 are 
the  coefficients  of  the  AR  component;  𝜃𝑗  are  the 
coefficients of the MA component  𝜖𝑡 is the random 
error term, c is a constant.

it

for

forecasting;

the  order  of 
i.e.,

The  process  of  building  an  ARIMA  model 
includes  determining  the  orders  p,  d,  q.  The 
the 
represents 
parameter  p 
the  number  of 
autoregressive  component, 
previous  values  used 
is 
represented in the formula by the coefficients  𝜙𝑖 for 
values  𝑦𝑡−𝑖. The  parameter  d  denotes  the  degree  of 
differencing, which determines how  many times the 
series  needs to be  differences to  ensure stationarity; 
this operation is performed on the time series before 
applying the formula. The parameter q indicates the 
order  of  the  moving  average  component,  meaning 
the number of previous random errors considered in 
forecasting;  it  is  represented  by  the  coefficients  𝜃𝑗 
for  the  error  terms  𝜖𝑡−𝑗.  After  determining  these 
the  Akaike 
parameters,  usually  selected  using 
or  Bayesian 
Information  Criterion

(AIC)

2.2.2. LSTM model

For  long-term  forecasts,  the  LSTM  model  is 
used,  which  is  a  type  of  recurrent  neural  network 
(RNN).  The  LSTM  model  can  capture  long-term 
dependencies  in  time  series  data  due  to  its  specific 
architecture,  which  includes  memory  cells  and 
mechanisms 
retaining 
information.  Mathematically,  the  behavior  of  a 
single  LSTM  block  is  described  by  the  following 
equations:

forgetting

and

for

𝑓𝑡 = 𝜎(𝑊𝑓 ⋅ [ℎ𝑡−1, 𝑥𝑡] + 𝑏𝑓) 
𝑖𝑡 = 𝜎(𝑊𝑖 ⋅ [ℎ𝑡−1, 𝑥𝑡] + 𝑏𝑖) 
~ =𝑡𝑎𝑛ℎ 𝑡𝑎𝑛ℎ (𝑊𝐶 ⋅ [ℎ𝑡−1, 𝑥𝑡] + 𝑏𝐶) ,

𝐶𝑡

~

𝐶𝑡 = 𝑓𝑡 ∗ 𝐶𝑡−1 + 𝑖𝑡 ∗ 𝐶𝑡
𝑜𝑡 = 𝜎(𝑊𝑜 ⋅ [ℎ𝑡−1, 𝑥𝑡] + 𝑏𝑜) 
ℎ𝑡 = 𝑜𝑡 ∗𝑡𝑎𝑛ℎ 𝑡𝑎𝑛ℎ (𝐶𝑡)  
where  𝑓𝑡  is  the  forget  vector  𝑖𝑡  is  the  input  vector, 
~ is the  new candidate for the cell state value; 𝐶𝑡 
𝐶𝑡
is the updated cell state, 𝑜𝑡  is the output vector; ℎ𝑡 
is the vector of output values from the LSTM block; 
𝑊𝑓 , 𝑊𝑖, 𝑊𝐶, 𝑊𝑜 are weight matrices; 𝑏𝑓, 𝑏𝑖, 𝑏𝐶, 𝑏𝑜 
are bias vectors.

The  LSTM  network  is  trained  on  historical 
spending  data  to  create  long-term  forecasts,  taking 
long-term  dependencies  between 
into  account 
observations.

2.2.3. Combination of forecasts

The  final  step  is  the  combination  of  forecasts 
obtained  from  the  ARIMA  and  LSTM  models.  For 
this,  a  weighted  average  method  is  used,  where  the 
results  of  both  models  are  combined  to  obtain  the 
final expense forecast.

The formula for the final forecast is as follows:

^ = 𝛼 ⋅ 𝑦𝑡

𝐴𝑅𝐼𝑀𝐴^

𝑦𝑡

+ (1 − 𝛼) ⋅ 𝑦𝑡

𝐿𝑆𝑇𝑀 ^

,

where  𝛼    is  the  weight  coefficient  that  determines 
the influence of each model on the final result.

The combination of ARIMA and LSTM allows 
for  consideration  of  both  short-term  and  long-term 
trends,  enhancing  the  accuracy  of  user  expense 
forecasts.

2.3.  LLM 
recommendations

for

generating

financial

A large language model (LLM), such as LLaMa 
3.1, can be effectively used to generate personalized 
financial recommendations based  on the analysis of 
previous  financial  data,  spending  anomalies,  and 
budget  forecasts.  This  section  provides  a  detailed 
look at the approach to using LLM for this task and

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

Software engineering and systems analysis

351

---

<!-- PAGE 5 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

the  process  of 
presents  a  diagram  describing 
integrating  the  LLM  model  into  the  overall  system 
architecture.

2.3.1. Data collections and preparation

To  generate  personalized  recommendations,  it

is important to ensure high-quality input data.

This data includes: 
– historical transaction data of the user; 
– data on detected spending anomalies; 
–  budget  expenditure  forecasts  based  on

ARIMA and LSTM models;

  additional  parameters,  such  as  the  user’s 
financial  goals,  risk  tolerance,  and  typical  spending 
patterns.

The  data  is  transferred  to  the  LLM  after 
normalization,

preprocessing,  which 
categorization, and extraction of the key features.

includes

2.3.2. Generation of personalized advice

After  configuring  the  LLM,  the  model  can  use 
personalized

create

data

to

the 
available 
recommendations.

The

recommendation

generation

process

proceeds as follows:

1.  Processing  input  data:  The  LLM  receives 
input  data,  including  transaction  history,  projected 
expenses, and anomaly information.

2.  Context  formation:  The  model  defines  the 
context  based  on  the  user’s  current  financial  status, 
forecasts, and identified anomalies.

3.  Generating  recommendations:  Based  on  the 
context,  the  model  generates  several  options  for 
financial advice, taking into account both the user’s 
short-term and long-term goals.

of

4. Evaluation

recommendations:  Each 
its 
is  evaluated 
recommendation 
alignment  with  the  user’s  individual  characteristics, 
such as risk level, financial goals, and preferences.

terms  of

in

and

including

explanations

The  generated  recommendations  are  delivered 
to the user through the system interface as structured 
suggestions, 
an 
assessment  of  the  potential  consequences  of  each 
decision. The user can select one of the suggestions 
or  request  additional  recommendation  of  the  initial 
set does not meet their needs. The recommendations 
are  adapted 
financial  capacity, 
providing  valuable  advice  for  individuals  with 
various  income  levels,  from  low  to  high.  Since  the 
analysis,  forecasting  and  advice  generation  occur 
within  the  context  of  the  user’s  specific  financial 
operations,  the  system  will  be  beneficial  regardless 
of the user’s income level.

the  user’s

to

Fig. 1 illustrates an example of a request to the 
financial

personalized

obtain

to

a

LLM

recommendation.  Fig.  2  shows  an  example  of  the 
model’s response based on the provided context.

Figure  3  demonstrates  the  interaction  of  AI 
components  within  the  financial  system.  In  the 
initial  stage,  the  system  receives  input  data  on  the 
user’s  financial 
then  pass 
through the data preprocessing module. This module 
is  responsible  for  data  cleaning,  normalization,  and 
preparation for further analysis by the models.

transactions,  which

3. ENSURING COMPLIANCE WITH 
ETHICAL PRINCIPLES IN THE SYSTEM

Ethics  is  an  important  aspect  in  designing 
recommendation  systems 
for  supporting 
financial  decisions,  as  it  affects  how  much  users 
trust the  system  and  how  willing  they  are  to  accept 
recommendations as objective and unbiased.

(RS)

system:

its 
impact  the  utility  for  each  of

In  [25],  an  analysis  of  ethical  issues  created  by 
recommendation  systems  is  conducted.  The  study 
describes  how  ethical  consequences  can  arise  in  a 
can 
recommendation 
(negatively) 
its 
their  rights.  Ethical 
stakeholders  and/or  violate 
impacts  can  be 
inaccurate 
recommendation  leading  to  reduced  utility  for  the 
user)  or  expose  relevant  parties  to  future  risks  (such 
as  the  influence  of  potentially  irrelevant  or  harmful 
content).

immediate  (e.g.,  an

operations

The  authors  of  [26]  analyze  recommendation 
system  technology  from  the  perspective  of  methods 
used to address issues in the following areas: privacy, 
personal  data, 
transparency,  personal 
fairness, 
identity, and the proper functioning of society.

An  AI-powered  system  must  ensure  a  balance 
between its ability influence the user and the user’s 
autonomy,  promoting  more 
financial 
behavior.  One  of  the  ethical  advantages  of  such  a 
system  is  its  ability  to  help  users  become  aware  of 
their financial habits without judgement, offering the 
opportunity  for  an  objective  analysis  of  spending 
and savings, regardless of income level.

rational

An  AI-based  recommendation  system  can 
promote responsible financial behavior by enhancing 
the  user’s  financial  awareness  and  helping  them 
avoid  potentially  irrational  expenditures.  In  an 
aggressive  marketing  environment,  where  users  are 
constantly  exposed  to  advertising,  an  ethically  built 
recommendation  system  allows  users  to  maintain 
control over their financial decisions. AI algorithms 
analyze  data  to  ensure  the  accuracy  and  usefulness 
of  recommendations,  avoiding  manipulation  and 
supporting  user’s  long-term  financial  goals.  This 
informational 
helps  users  navigate  a  complex 
landscape  where  marketing  influences  often  lead  to 
impulsive purchases and irrational spending.

352

Software engineering and systems analysis

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

---

<!-- PAGE 6 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

Fig. 1. Diagram of the request implementation to the LLM for obtaining a personalized  
financial recommendation 
Source: compiled by the authors

Fig. 2. Example of the model’s response based on the provided context 
Source: compiled by the authors

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

Software engineering and systems analysis

353

---

<!-- PAGE 7 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

Fig. 3. Diagram of the interaction of AI components within the system 
Source: compiled by the authors

The  ethical  nature  of  the  system  is  reinforced 
by  its  focus  on  the  user’s  interests.  Instead  of 
evaluating or judging financial behavior, the system 
provides  structured,  well-founded  advice  that  helps 
users  better  understand  their  spending  patterns, 
identify potential saving opportunities, and optimize 
their  budget.  Importantly,  the  recommendations  are 
individual  goals  and 
to 
tailored 
preferences,  preserving 
independence  and 
autonomy in making financial decisions. The system 
does not impose specific actions but instead offers a 
variety  of  options  from  which  the  user  can  choose 
that best meet their needs and goals.

the  user’s

their

4. IMPLEMENTATION OF THE 
RECOMMENDATION SYSTEM

is

The architecture of the system is built on an event-
driven  approach  with  a  high-level  of  module 
independence.  The  overall  operations  principle  of  the 
system,  which  supports  core  financial  operations, 
integration  with  banking  systems,  as  well  as  data 
cleaning  and  preparation  processes  for  further  AI 
module  analysis, 
that  each  module  operates 
the  Budget  Module 
autonomously.  For  example, 
remains operations even if the AI module is temporarily 
unavailable,  and  vice  versa.  The  AI  module 
is 
responsible  for  key  functions  such  as  detecting 
anomalous expenses, forecasting future expenses during 
budgeting, generating personalized financial advice, and 
recommending alternative spending options. The Build-
Train-Deploy  pattern  is used  to  integrate  the AI  model 
into  the  microservices  architecture,  supported  by AWS 
SageMaker,  which  automates  model  training,  testing, 
and deployment [27].

A  database  has  been  developed  to  store  data 
the 
that 
provides 
recommendation 
Entity-
Relationship Diagram (ERD) model shown in Fig. 4,

input 
system,  with

information

for

its

illustrating the main entities of the financial platform 
and  the  relationships  between  them.  The  diagram 
covers  various  aspects  of  the  system’s  operation, 
including  user  management,  transactions,  budgets, 
financial goals, subscriptions, and categories.

Fig. 5 and Fig. 6 provide examples of the screen

forms of the developed system.

The  system’s  software  implementation  is  built 
on  a  modular  architecture, 
including  several 
components,  each  responsible  for  a  specific  part  of 
the  functionality.  The  main  components  are  the  AI 
Budget  Module,  API  Gateway, 
Module, 
Authentication  Module,  and  other  integrations  with 
cloud services such as AWS Glue and AWS SQS.

like

scikit-learn,  TensorFlow,

The AI Module is implemented in Python using 
and 
libraries 
statsmodels. Python was chosen for this module due 
to  its  powerful  data  processing  capabilities,  ease  of 
integrating machine learning algorithms, and support 
for a wide range of analytics libraries.

The  Budget  Module  is  implemented  in  Java 
using  the  Spring  Framework  to  ensure  fast  and 
reliable  processing  of  user  financial  transactions. 
transactions, 
This  module  allows  adding  new 
creating budgets, and retrieving expense data. Using 
Spring  facilitates  easy  configuration  of  REST APIs 
for  interaction  with  other  modules  and  the  client 
its 
side.  The  choice  of  Spring 
effectiveness  for  building  scalable  web  applications 
and  microservices. Additionally,  using  Java  ensures 
reliability  and  a  high  level  of  security  in  data 
processing.

is  based  on

The API  Gateway  is  implemented  with  Spring 
Cloud  Gateway,  allowing  efficient  routing  of 
requests  between  different  microservices  in  the 
system.  This  solution  provides  a  centralized  entry 
point  for  all  client  requests  and  enables 
the 
application of security policies and load balancing.

354

Software engineering and systems analysis

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

---

<!-- PAGE 8 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

Fig. 4. ERD for the recommendation system 
Source: compiled by the authors

Spring  Cloud  Gateway  was  chosen  for  its  ease 
of configuration and ability to scale with the system, 
which  is  critically  important  to  ensure  continuous 
availability of services.

resources  via

To  ensure  reliable  user  authentication,  OAuth 
2.0  is  used,  which  allows  for  controlling  access  to 
tokens. 
the  system’s  protected 
Implementing  OAuth  2.0  on  the  basis  of  Spring 
Security  makes  it  easy  to  integrate  authentication 
with other modules and ensures reliable control over 
access to important data. Spring Security was chosen 
for  this  task  due  to  its  seamless  integration  with 
OAuth  2.0  and  its  ability  to  quickly  adapt  to 
different levels of user access.

For processing large volumes of transaction and 
budget  data,  AWS  Glue  is  used  to  perform  ETL 
(Extract,  Transform,  Load)  operations  to  prepare 
data  for  further  analysis  in  the  AI  Module.  Glue 
Crawler  automatically  determines  the  schema  of 
data  stored  in  S3  and  makes  it  available  for  further 
processing.

Fig. 5. Main page 
Source: compiled by the authors

Fig. 6. Use of AI models for anomaly detection 
Source: compiled by the authors

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

Software engineering and systems analysis

355

---

<!-- PAGE 9 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

AWS  SQS

is  used  for  message  queuing 
between  microservices.  This  enables  asynchronous 
event processing and reliable  message  transmission, 
for example, about anomalies in financial expenses.

Terraform  is  used  to  automate  the  creation  of 
AWS  infrastructure,  including  configuring  SQS 
queues and S3 buckets. This makes it easy to set up 
and  scale  the  cloud  infrastructure  to  meet  system 
requirements.

The client side of the system is implemented in 
React.js,  providing  an  interactive  and  fast  user 
interface.  React  enables  the  construction  of  Single 
Page  Applications  (SPA),  ensuring  quick  response 
and  dynamic  data  updates  without  page  reloads. 
React.js was chosen for its popularity, performance, 
and extensive capabilities for integration with REST 
APIs.

CONCLUSIONS

The  use  of  AI  models  for  a  system  that 
generates personalized financial recommendations is 
described.  The  Isolation  Forest  model  is  applied  to 
detect  anomalous  transactions,  using  a  tree-like 
structure to isolate deviations in the user’s financial 
behavior.  This  enables  the  model  to  effectively

identify  potentially  spontaneous  or  uncharacteristic 
expenses.

In parallel, ARIMA and LSTM models are used 
to forecast future  expenses. ARIMA provides short-
term  forecasts,  accounting  for  seasonal  fluctuations 
and  dependencies in time series, while LSTM, with 
its ability to capture long-term dependencies, is used 
for more stable long-term forecasts.

The data generated by these models is fed into a 
large  language  model  (LLM),  which  integrates 
anomaly results, short-term, and long-term forecasts 
to produce personalized financial recommendations. 
These  recommendations  are  tailored  to  the  user’s 
specific  financial  goals  and  behavior  and  can  help 
optimize  the  budget,  reduce  risks,  or  increase 
savings.

The  system  ensures  high  accuracy  through  the 
combination  of  various  AI  models  (ARIMA  and 
LSTM  for  forecasting,  Isolation  Forest  for anomaly 
for  generating  advice), 
detection,  and  LLM 
completeness  by  training  on  user’s  transactions  and 
financial  operations, as well as privacy and security 
by adhering to OAuth 2 standards and OWASP Top 
10 principles. The systems’ ethical aspect is reflected 
in  its  support  for  users  in  managing  their  finances 
rationally,  without  judgement  of  their  decisions.

REFERENCES

1.  Lu,

J.,  Zhang,  Q.  &  Zhang,  G.  “Intelligent

information

systems”.  2020.  DOI:

https://doi.org/10.1142/11947.

2.  Verma,  P.  &  Sharma  S.  “Artificial  Intelligence  based  recommendation  system”.  2nd  International 
Conference  on  Advances  in  Computing,  Communication  Control  and  Networking.  Greater  Noida,  India. 
2020. p. 669–673. DOI: https://doi.org/10.1109/ICACCCN51052.2020.9362962.

3.  Roy,  D.  &  Dutta,  M.  “A  systematic  review  and  research  perspective  on  recommender  systems”.

Journal of Big Data. 2022; 9: 59. DOI: https://doi.org/10.1186/s40537-022-00592-5.

4.  Hodovychenko  M.  A.,  Gorbatenko  A.  A.  “Recommender  systems:  models,  challenges  and 
308–319.

of  Advanced

Technology.

Information

2023;

(4):

6

opportunities”.  Herald 
DOI: https://doi.org/10.15276/hait.06.2023.20.

5.  He, X., Liu, Q. & Jung, S. “The impact of recommendation system on user satisfaction: A moderated 
mediation  approach”.  J  Journal  of  Theoretical  and  Applied  Electronic  Commerce  Research.  2024;  19  (1): 
448–466. DOI: https://doi.org/10.3390/jtaer19010024.

6.  Deschênes,  M.  “Recommender  systems  to  support  learners’  Agency  in  a  learning  context:  a 
systematic  review”.  International  Journal  of  Educational  Technology  in  Higher  Education.  2020;  17:  50.  
DOI: https://doi.org/10.1186/s41239-020-00219-w.

7.  Reiter-Gavish, L., Qadan, M. & Yagil, J. “Financial advice: Who Exactly Follows It?”  Research in

Economics. 2021; 75 (3): 244–258. DOI: https://doi.org/10.1016/j.rie.2021.06.003.

8.  Schepen,  A.  &  Burger,  M.  J.  “Professional  financial  advice  and  subjective  Well-Being”.  Applied

Research Quality Life. 2022; 17: 2967–3004. DOI: https://doi.org/10.1007/s11482-022-10049-9.

9.  Fieberg,  C.,  Hornuf,  L.  &  Streich,  D.  “Using  GPT-4  for  financial  advice”.  CESifo.  2023.

DOI: http://dx.doi.org/10.2139/ssrn.4499485.

356

Software engineering and systems analysis

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

---

<!-- PAGE 10 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

10.  Sharaf,  M.,  Hemdan,  E.  E.  D.,  El-Sayed,  A.  et  al.  “A  survey  on  recommendation  systems  for 
financial  services”.  Multimedia  Tools  and  Applications.  2022.  DOI:  https://doi.org/10.1007/s11042-022-
12564-1.

11.  Zatevakhina, A., Dedyukhina, N. & Klioutchnikov O. “Recommender systems – The foundation of 
an  intelligent  financial  platform:  Prospects  of  development”.  International  Conference  on  Artificial 
Intelligence:  Applications  and 
(IC-AIAI).  Belgrade,  Serbia.  2019.  p.  104–1046.  
DOI: https://doi.org/10.1109/IC-AIAI48757.2019.00029.

Innovations

12.  Zibriczky,  D.  “Recommender  systems  meet  finance:  A  literature  review”.  2nd  International 
Workshop  on  Personalization  and  Recommender  Systems  in  Financial  Services.  Bari,  Italy.  2016.  
DOI: https://doi.org/10.13140/RG.2.1.1249.2405.

13.  Kanaujia, P. K. M., Behera, N., Pandey, M. & Rautaray S. S. “Recommendation system for financial 
Industry  &  Government.  2016.

International  Conference  on

in  Business

ICT 
analytics”. 
DOI: https://doi.org/10.1109/ICTBIG.2016.7892673.

14.  Li,  T.  &  Song,  J.  “Deep  learning-powered  financial  product  recommendation  system  in  banks: 
Integration of transformer and transfer learning”. Journal of Organizational and End User Computing. 2024; 
36 (1): 1–29. DOI: https://doi.org/10.4018/JOEUC.343257.

15.  Ayemowa, M. O., Ibrahim, R. & Khan, M. M. “Analysis of  recommender system using generative 
IEEE  Access.  2024;  12:  87742–87766.  
review”.

intelligence:  A  systematic

literature

artificial 
DOI: https://doi.org/10.1109/ACCESS.2024.3416962.

16. Yue,  X.  “Application  of  AI  technology  in  personalized  recommendation  system  for  financial 
services”.  Applied  Mathematics  and  Nonlinear  Sciences.  2024;  9  (1).  DOI:  https://doi.org/10.2478/amns-
2024-1349.

17.  Jannach,  D.,  Pu,  P.,  Ricci,  F.  &  Zanker,  M.  “Recommender  systems:  Past,  present,  future”.  AI

Magazine. 2021; 42: 3–6. DOI: https://doi.org/10.1609/aimag.v42i3.18139.

18.  Chua,  A.  Y.K.,  Pal,  A.  &  Banerjee,  S.  “AI-enabled  investment  advice:  Will  users  buy  it?”.

Computers in Human Behavior. 2023; 138: 107481.  DOI: https://doi.org/10.1016/j.chb.2022.107481

19.  Longoni,  C.,  Bonezzi,  A.  &  Morewedge,  C.  K.  “Resistance  to  medical  artificial  intelligence”.

Journal of Consumer Research. 2019; 46 (4): 629–650. DOI: https://doi.org/10.1093/jcr/ucz013.

20.  Zhang, L., Pentina, I. & Fan, Y.  “Who do you choose? Comparing perceptions of human vs robo-
advisor  in  the  context  of  financial  services”.  The  Journal  of  Services  Marketing;  2021;35  (5):  634–646. 
DOI: https://doi.org/10.1108/JSM-05-2020-0162.

21.  Bonelli, M. I. & Döngül, E. S. “Robo-advisors in the financial services industry: recommendations 
for full-scale optimization, digital twin integration, and leveraging natural language processing trends”. 9th 
International  Conference 
268–275.  
DOI: https://doi.org/10.1109/ICVR57957.2023.10169615.

Reality.  Xianyang,  China.

Virtual

2023.

on

p.

22.  Zhang, Q., Lu, J. & Jin, Y. “Artificial intelligence in recommender systems”. Complex & Intelligent

Systems. 2020; 7. DOI: https://doi.org/10.1007/s40747-020-00212-w.

23.  del  Valle,  J.  I.  &  Lara,  F.  “AI-powered  recommender  systems  and  the  preservation  of  personal

autonomy”. AI & Society. 2024; 39: 2479–2491. DOI: https://doi.org/10.1007/s00146-023-01720-2.

24.  Christman,  J.  “Autonomy  in  moral  and  political  philosophy.  The  stanford  encyclopedia  of

philosophy”. 2020. – Available from: https://plato.stanford.edu/archives/fall2020/entries/autonomy-moral.

25.  Milano,  S., Taddeo,  M.  &  Floridi,  L.  “Recommender  systems  and  their  ethical  challenges”.  AI  &

Society. 2020; 35: 957–967. DOI: https://doi.org/10.1007/s00146-020-00950-y.

26.  Karakolis, E., Oikonomidis, P. F. & Askounis, D. "Identifying and  addressing ethical challenges in 
recommender systems". 13th International Conference on Information, Intelligence, Systems & Applications. 
Corfu, Greece. 2022. p. 1–6. DOI: https://doi.org/10.1109/IISA56318.2022.9904386.

27.  Shuryhin  K.  A.,  Zinovatna  S.  L.  “Architecture  of  the  financial  manager  system  using  AI 
Conference 
DOI:

International 
Ukraine.

Scientific 
2024;

Х 
Odesa,

and 
1

118–123.

Practical

(1):

technologies” 
(In  Ukrainian). 
“Informatics.Culture.Technology”. 
https://doi.org/10.15276/ict.01.2024.17.

Conflicts of Interest: The authors declare that they have no conflict of interest regarding this study, including financial, personal, authorship or other, 
which could influence the research and its results presented in this article

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

Software engineering and systems analysis

357

---

<!-- PAGE 11 -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology                                    
                                                                                          2024; Vol.7 No.4: 348–358

Received        29.08.2024 
Received after revision   09.10.2024 
Accepted       30.1.2024

DOI: https://doi.org/10.15276/aait.07.2024.24 
УДК 004.414.32

Рекомендаційна система для прийняття фінансових  
рішень з використанням штучного інтелекту

Шуригін Костянтин Андрійович1)  
                           ORCID: https://orcid.org/0009-0002-1000-303X; ksurygin5@gmail.com 
                                                                                          Зіноватна Світлана Леонідівна1)  
ORCID: https://orcid.org/0000-0002-9190-6486; zinovatnaya.svetlana@op.edu.ua. Scopus Author ID: 57219779480 
1) Національний університет «Одеська політехніка», пр. Шевченка, 1. Одеса, 65044, Україна

АНОТАЦІЯ

Стрімке поширення штучного інтелекту (ШІ) на споживчих ринках створює серйозні виклики для суспільства, зокрема 
в  контексті  використання  когнітивних  упереджень,  що  впливають  на  ухвалення  фінансових  рішень  споживачами.  Ці 
упередження  можуть  призводити  до  нераціональних  витрат, що  ставить  під  сумнів  етичність  застосування  ШІ  у  подібних 
сферах. У цьому дослідженні розглядається, як ШІ може не тільки підвищувати ефективність ухвалення фінансових рішень, 
але й допомагати споживачам приймати більш обґрунтовані та раціональні рішення. Основна увага зосереджена на розробці 
інтелектуальної  системи  управління  фінансами,  яка  застосовує  сучасні  алгоритми  ШІ  для  аналізу  фінансової  поведінки, 
виявлення аномалій та надання персоналізованих рекомендацій.  У статті розглядається система генерації персоналізованих 
фінансових рекомендацій на основі великих мовних моделей, яка використовує історію транзакцій, прогнозовані витрати та 
інформацію про аномалії для створення індивідуальних порад. Зокрема, досліджуються моделі машинного навчання, такі як 
Isolation  Forest  для  ідентифікації  атипових  фінансових  дій,  а  також  поєднання  ARIMA  та  LSTM  для  прогнозування 
бюджетів.  Дослідження  також  розглядає  можливість  інтеграції  цих  моделей  із  використанням  великих  мовних  моделей 
(LLM) для генерування персоналізованих рекомендацій. Методологічна частина роботи включає аналіз існуючих моделей і 
сфер їхнього застосування, визначення типів та структури даних для обробки, розробку системи, що інтегрує наявні моделі, 
та  її  тестування.  Описано  процес  формування  рекомендацій,  що  включає  етапи  обробки  вхідних  даних,  формування 
контексту, генерації рекомендацій та їх оцінки з урахуванням характеристик користувача, таких як рівень ризику, фінансові 
цілі та  уподобання.  Генеровані  рекомендації  спрямовані на  оптимізацію фінансової  поведінки  користувача  та можуть бути 
адаптовані  до  різних  рівнів  доходів.  Окрему  увагу  приділено  етичним  аспектам  системи,  що  включають  забезпечення 
конфіденційності,  справедливості  та  прозорості,  а  також  важливості  підтримки  автономії  користувача  у  прийнятті 
фінансових  рішень.  Система  сприяє  розвитку  відповідальної  фінансової  поведінки,  допомагаючи  уникати  імпульсивних 
витрат та підвищуючи фінансову обізнаність без маніпуляцій чи нав’язування конкретних рішень.

Ключові слова: штучний інтелект, машинне навчання, когнітивні упередження, фінансові рішення, етичність.

ABOUT THE AUTHORS

Kostiantyn A. Shuryhin - Master, Software Engineering Department. Odesа Polytechnic National University, 1, Shevchenko 
Ave. Odesa, 65044, Ukraine 
ORCID: https://orcid.org/0009-0002-1000-303X; ksurygin5@gmail.com. 
Research field: Software architecture; data processing; distributed systems

Шуригін Костянтин Андрійович - магістр кафедри Інженерії програмного забезпечення. Національний університет 
«Одеська політехніка», пр. Шевченка, 1. Одеса, 65044, Україна

Svitlana L. Zinovatna - Candidate of Engineering Sciences, Associate Professor, Software Engineering Department. Odesа 
Polytechnic National University, 1, Shevchenko Ave. Odesa, 65044, Ukraine 
ORCID: https://orcid.org/0000-0002-9190-6486; zinovatnaya.svetlana@op.edu.ua. Scopus Author ID: 57219779480 
Research field: Information technology; data processing, improving the performance of information systems

Зіноватна Світлана Леонідівна - кандидат технічних наук, доцент кафедри Інженерії програмного забезпечення. 
Національний університет «Одеська політехніка», пр. Шевченка, 1. Одеса, 65044, Україна

358

Software engineering and systems analysis

ISSN 2617-4316 (Print) 
ISSN 2663-7723 (Online)

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology
                                                                                          2024; Vol.7 No.4: 348–358
DOI: https://doi.org/10.15276/aait.07.2024.24
UDC 004.414.32

Recommendation system for financial decision-making using
Artificial intelligence
Kostiantyn A. Shuryhin1)
ORCID: https://orcid.org/0009-0002-1000-303X; ksurygin5@gmail.com
Svitlana L. Zinovatna1)
ORCID: https://orcid.org/0000-0002-9190-6486; zinovatnaya.svetlana@op.edu.ua. Scopus Author ID: 57219779480
1) Odesa Polytechnic National University, Shevchenko Ave. Odesa, 65044, Ukraine
ABSTRACT
The rapid expansion of artificial intelligence (AI) in consumer markets presents challenges, particularly in how cognitive biases
influence financial decision-making. These biases can lead to irrational spending, raising ethical concerns about AI’s role in such
applications. This research explores how AI can enhance decision-making effectiveness and support consumers in making more
rational financial choices. The focus is on developing an intelligent financial management system that applies modern AI algorithms
to analyze financial behavior, detect anomalies, and offer personalized recommendations. The article considers a system for
generating personalized financial recommendations based on large language models, which uses transaction history, predicted costs,
and anomaly information to generate individual advice. Techniques include using Isolation Forest for identifying atypical financial
actions and a combination of ARIMA and LSTM models for budget forecasting. The research also considers integrating these models
with large language models (LLMs) to generate personalized recommendations. The methodological part of the work includes an
analysis of existing models and their areas of application, defining data types and structures for processing, developing a system that
integrates the available models, and testing it. The process of generating recommendations is described, which includes the stages of
processing input data, forming context, generating recommendations and evaluating them taking into account user characteristics,
such as risk level, financial goals and preferences. The generated recommendations are aimed at optimizing the user's financial
behavior and can be adapted to different income levels. Special attention is paid to the ethical aspects of the system, which include
ensuring confidentiality, fairness and transparency, as well as the importance of supporting user autonomy in making financial
decisions. The system promotes responsible financial behavior by helping to avoid impulsive spending and increasing financial
awareness without manipulation or imposing specific decisions.
Keywords: Artificial Intelligence; machine learning; cognitive biases; financial decisions; ethics

For citation: Shuryhin K. A., Zinovatna S. L. “Recommendation system for financial decision-making using Artificial Intelligence”. Applied
Aspects of Information Technology. 2024; Vol.7 No.4: 348–358. DOI: https://doi.org/10.15276/aait.07.2024.24
INTRODUCTION  decisions.AI is already demonstrating considerable
potential in the financial sector, particularly through
The modern financial landscape faces numerous
|              |        |        |      |         |     |          | its  ability  | to  | analyze  large  | volumes  |     | of  data  | and  |
| ------------ | ------ | ------ | ---- | ------- | --- | -------- | ------------- | --- | --------------- | -------- | --- | --------- | ---- |
| challenges,  | among  | which  | key  | issues  |     | include  |               |     |                 |          |     |           |      |
uncover hidden patterns. For example, systems that
| ineffective  | financial    | management  |     |            | and  financial  |      |          |            |             |     |       |          |     |
| ------------ | ------------ | ----------- | --- | ---------- | --------------- | ---- | -------- | ---------- | ----------- | --- | ----- | -------- | --- |
|              |              |             |     |            |                 |      | combine  | cognitive  | psychology  |     | with  | machine  |     |
| illiteracy,  | both  among  | individual  |     | consumers  |                 | and  |          |            |             |     |       |          |     |
learning algorithms can personalize user experiences
| organizations.  | Many  | individuals  |     | lack  | sufficient  |     |     |     |     |     |     |     |     |
| --------------- | ----- | ------------ | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
and offer recommendations based on an analysis of
| knowledge  | to  make  | sound  | financial  |     | decisions,  |     |     |     |     |     |     |     |     |
| ---------- | --------- | ------ | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
their behavior and preferences. This enables AI not
| making  | them  vulnerable  |     | to  aggressive  |     | marketing  |     |           |          |           |           |     |            |     |
| ------- | ----------------- | --- | --------------- | --- | ---------- | --- | --------- | -------- | --------- | --------- | --- | ---------- | --- |
|         |                   |     |                 |     |            |     | only  to  | predict  | consumer  | behavior  |     | but  also  | to  |
strategies. This is especially relevant in the context
|     |     |     |     |     |     |     | provide  | more  | accurate  | recommendations  |     |     | for  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | ---------------- | --- | --- | ---- |
of increasingly sophisticated AI-enhanced marketing
financial planning, budgeting, and investing.
techniques that can manipulate consumer behavior,
The goal of this study is to develop principles
promoting irrational expenditures.
|     |     |     |     |     |     |     | for  creating  |     | financial  recommendations  |     |     | using  | AI  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------------------- | --- | --- | ------ | --- |
Research in behavioral economics shows that
models, regardless of user’s income levels.
cognitive biases, such as loss aversion or framing
| effects,  | significantly  | impact  | consumer  |     | decision- |     |     |     |     |     |     |     |     |
| --------- | -------------- | ------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
1. LITERATURE OVERVIEW
| making,  | often leading to  |     | deviations  |     | from rational  |     |     |     |     |     |     |     |     |
| -------- | ----------------- | --- | ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
At present, there is a significant body of work
| behavior.  | This  highlights  |                  | the  need  |           | for  intelligent  |        |       |           |            |     |              |     |        |
| ---------- | ----------------- | ---------------- | ---------- | --------- | ----------------- | ------ | ----- | --------- | ---------- | --- | ------------ | --- | ------ |
|            |                   |                  |            |           |                   |        | that  | provides  | extensive  |     | information  |     | about  |
| systems    | that  can         | help  consumers  |            | overcome  |                   | these  |       |           |            |     |              |     |        |
recommendation systems (RS).
| biases  | and  make  | more  | informed  |     | financial  |     |     |     |     |     |     |     |     |
| ------- | ---------- | ----- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
In [1], theoretical studies for RS are described,

|     |     |     |     |     |     |     | along  | with  | new  developments  |     | of  | applications,  |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------------------ | --- | --- | -------------- | --- |
© Shuryhin K., Zinovatna S., 2024  prototypes and real examples of such systems.
This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/deed.uk)
348  Software engineering and systems analysis  ISSN 2617-4316 (Print)
|     |     |     |     |     |     |     |     |     |     | ISSN 2663-7723 (Online)  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |

Shuryhin K. A., Zinovatna S. L. / Applied Aspects of Information Technology
2024; Vol.7 No.4: 348–358
Recommendation systems play a crucial role in interactions (such as browsing, selling, buying,
many areas: e-commerce websites, online shopping, rating etc.) within the system.
dating apps, social media, digital marketing, online In [11], it was noted that a certain limit of
advertising, etc., as they provide users with development has been reached for recommendations
personalized recommendations and feedback based systems in the financial sector. At the same time,
on their preferences and choices [2]. such systems are “considered to be intelligent and
Sources [3, 4] describe the main models experienced financial managers, well-informed and
underlying the construction of RS, highlight the aware of each client’s financial situations, regardless
primary sectors where such systems are used, and of their location”. Further expenditures on their
outline the distribution of publications for various promotion can only be justified by economic impact.
application areas. It is noted that e-commerce, which Recommendation systems exist for banks; in
can be considered a part of financial services, particular, such system can provide personalized
accounts for 17% of all reviewed studies. recommendations on spending opportunities near the
Authors in [5] focus on the psychological user based on their credit card usage history and
mechanisms through which RS impacts user geolocation data [12], thereby taking context into
satisfaction. It is shown that the type of search goal account. However, the authors of the study highlight
interacts with the types of recommendations. the aspect that user preferences are unstable and
Psychological reactance, a resistance that users may highly dependent on the user’s actual goal. Since
feel towards RS recommendations perceived as a these systems focus on money management and
threat to their freedom of choice, is also discussed as spending opportunities, there is a significant need to
one of the primary reasons users reject explain the systems’ results.
recommendations. In [13] a recommendation system is presented
In RS, there are two roles: predicting the value for managing and utilizing three components of
(how a user will rate a resource) [6]. The education salary: savings, investments and expenses. The
sector is used as an example in this study. system focuses specifically on salary-related
When it comes to the financial sector, recommendations, but it concludes that such a
publications most often describe recommendations system is useful when a person has a high income.
systems specifically for financial consulting. A large number of studies are dedicated to the
Financial consultants can improve the trading skills development of recommendations systems for
of investors; however, the presences of trading financial products. Specifically, [14] proposes an
experience and professional complexity negatively innovation that involves the seamless integration of
correlates with the use of financial consultations, Transformers, transfer learning and graph neural
meaning that more experienced investors are less networks (GNN) to address issues faced by
likely to use recommendations [7]. There is also traditional methods, such as user cold start, data
study that found the connection between financial sparsity, and complex relationship modeling. In [15]
consultations and subjective well-being is stronger generative adversarial networks (GANs) are
for households that have experienced income considered as a predominant AI technique/model in
growth, individuals who do not consider themselves various recommendation systems. In [16] an
financially knowledgeable, and those with a weaker interpretable model for personalized financial
internal locus of control [8]. The foundation of the service recommendations it proposed, based on self-
research is the idea that households face the need to attention mechanisms, by combining the long short-
make decisions with financial consequences every term memory (LSTM) model and the topic model
day, and the ultimate goal of decision-making is to Linear Discriminant Analysis (LDA) with AI
achieve outcomes that enhance the quality-of-life support.
experiences by individuals (subjective well-being). In [17], the need to understand the specifics of
For providing financial consultations, the GPT- the recommendation system environment and the
4 bot can be used, which “offers specific investment expected impact of the system on its users is
portfolios that reflect an investor’s individual emphasized. It is necessary to evaluate the quality of
circumstances, such as risk tolerance, risk capacity, recommendation systems not only in terms of the
and preference for stability”. accuracy of the recommendations provided but also
There are other financial sectors where by considering the diversity and novelty of the items
recommendation principles can be applied, such as included in the recommendations [5, 17]. Users are
banking, stocks, and insurance [10], in these areas, likely to follow recommendations only if they have
users are viewed as active entities who engage in developed trust in the system over time. Therefore,
ISSN 2617-4316 (Print) Software engineering and systems analysis 349
ISSN 2663-7723 (Online)

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology
                                                                                          2024; Vol.7 No.4: 348–358
recommendations should also be evaluated based on  is well-suited for anomaly detection, can be applied
whether the provided recommendation was utilized.  to  analyze  consumer  behavior,  particularly  to
Acceptance of AI-generated recommendations  identify spontaneous expenses or impulsive financial
is a function of attitudes toward AI, trust, perceived  decisions. Additionally, deep neural networks (CNN,
accuracy,  and  the  level  of  uncertainty  [18].  The  RNN) are actively used to analyze consumer data
described  attitude-perception-intention  model  and  predict  behavioral  patterns,  enabling  the
defines the basic psychological mechanism by which  optimization of marketing strategies.
users decide to accept AI-supported advice.  AI  also  plays  an  important  role  in  financial
Consumers  often prefer human interaction  in  recommendation systems that help users choose the
fields characterized by high consumer involvement,  best financial products or services. Algorithms based
such  as  healthcare  and  financial  services,  over  on collaborative filtering and deep learning methods
computer-generated advice [19]. However, AI is still  are used to analyze user behavior and create targeted
rapidly being implemented in the financial sector.  offers  that  meet  their  needs.  These  systems  can
The concept of a robo-advisor has even emerged,  significantly  improve  the  quality  of  financial
offering  “personalized  risk  analysis  and  real-time  decisions by reducing the impact of cognitive biases
service adjustments based on self-service, requiring  on consumer behavior.
| minimal  | human  | interaction”  |     | [20].  | A  robo-advisor  |     |     |                              |     |     |     |           |        |
| -------- | ------ | ------------- | --- | ------ | ---------------- | --- | --- | ---------------------------- | --- | --- | --- | --------- | ------ |
|          |        |               |     |        |                  |     |     | 2.1. Detection of anomalous  |     |     |     | expenses  | using  |
essentially offers software for retail investors who
isolation forest
lack sufficient experience or funds to hire a personal
The concept of Isolation Forest was used as the
| financial  | consultant  |     | [21].  | As  | a  potential  |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
enhancement,  integrating  Neuro-Linguistic  basis for detecting anomalous user expenses, with its
|                               |        |          |     |                    |             |     | core          | idea  | being  | the  | isolation  | of  anomalies  | from  |
| ----------------------------- | ------ | -------- | --- | ------------------ | ----------- | --- | ------------- | ----- | ------ | ---- | ---------- | -------------- | ----- |
| Programming (NLP) technology  |        |          |     | into robo-advisor  |             |     |               |       |        |      |            |                |       |
| software                      | could  | improve  |     | AI  chatbots,      | increasing  |     | normal data.  |       |        |      |            |                |       |
customer satisfaction and the likelihood that clients  To achieve this goal, a binary tree is initially
will follow portfolio guidance.  created  by  randomly  selecting  features  and
Privacy  and  security  are  important  issue  for  distributing values. The next step is to determine the
recommendation  systems.  Even  with  excellent  anomaly score by calculating the path length from
performance,  users  find  it  difficult  to  trust  such  the root of the tree to the terminal node. The shortest
systems due to opacity and privacy concerns [22].   paths are considered anomalies.
In general, the ethical implications of using AI- The  mathematical  basis  for  calculating  the
based recommendation systems are a distinct area of  expected path length is the following formula:
research. For instance, [23] provides a conceptual
2(𝑛−1)
assessment  of  human  autonomy  when  using  a  2𝑙𝑜𝑔𝑙𝑜𝑔 (𝑛−1) −
|     |     |     |     |     |     |     |     | 𝐸(ℎ(𝑥))= |     | 𝑐(𝑛)+ |     |     | 𝑛 ,  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- | --- | --- | ---- |
𝑛
universal recommendation system. The concept of
human autonomy is defined in [24] as “the ability to  where  𝑐(𝑛)  is  the  average  path  length  for
be one’s own person, to live one’s life according to  unsuccessful searches in a binary tree; ℎ(𝑥) is the
|     |     |     |     |     |     |     | path  | length  | for  | point  | 𝑥  in  | the  isolation  | tree  (the  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ---- | ------ | ------ | --------------- | ----------- |
reasons and motives that are taken as one’s own, and
not the product of manipulative or external forces  number  of  edges  traversed  from  the  root  to  the
terminal node).
that distort, thus being independent”. The conclusion
of the study [22] is that not everything needs to be
2(𝑛−1)
recommended, and people should be aware of the  𝑐(𝑛)= 2𝐻(𝑛−1)−( ),
𝑛
| potential  | impact  | of  | automated  |     | recommendation  |     |     |     |     |     |     |     |     |
| ---------- | ------- | --- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
technologies.  where 𝐻(𝑖)  is the harmonic number, calculated as:
Thus, when designing recommendation systems
|     |     |     |     |     |     |     |     |     |     |     | ∑𝑖  | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to support financial decision-making, the following  𝐻(𝑖)= .
𝑘=1𝑘
aspects must be considered; accuracy, completeness,
|     |     |     |     |     |     |     |     | The  | anomaly  | score  | for  | a  point  | is  calculated  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------ | ---- | --------- | --------------- |
privacy, and adherence to ethical standards.
based on the average path length across all trees:
2. USING AI MODELS TO ADDRESS THE
𝐸(ℎ(𝑥))
| ISSUE OF FINANCIAL RECOMMENDATION  |     |     |     |     |     |     |     |     |     |        | −   |         |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------- | --- |
|                                    |     |     |     |     |     |     |     |     |     | 𝑠(𝑥,𝑛) | = 2 | 𝑐(𝑛) ,  |     |
FORMATION
|                                                       |                 |     |            |               |             |      | where  | 𝑠(𝑥,𝑛)                          |     | ≈ 1,  if  | the  | point  is  | an  anomaly;   |
| ----------------------------------------------------- | --------------- | --- | ---------- | ------------- | ----------- | ---- | ------ | ------------------------------- | --- | --------- | ---- | ---------- | -------------- |
| In                                                    | the  financial  |     | sector,    | AI  is        | also  used  | for  |        |                                 |     |           |      |            |                |
|                                                       |                 |     |            |               |             |      | 𝑠(𝑥,𝑛) | ≈0.5,  if the point is normal.  |     |           |      |            |                |
| detecting                                             | anomalous       |     | financial  | transactions  |             | and  |        |                                 |     |           |      |            |                |
| preventing fraud. The Isolation Forest model, which   |                 |     |            |               |             |      |        |                                 |     |           |      |            |                |

350  Software engineering and systems analysis  ISSN 2617-4316 (Print)
|     |     |     |     |     |     |     |     |     |     |     |     | ISSN 2663-7723 (Online)  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- |

Shuryhin K. A., Zinovatna S. L. / Applied Aspects of Information Technology
2024; Vol.7 No.4: 348–358
2.2. Budget prediction using ARIMA and Information Criterion (BIC), the model is trained on
LSTM the training data and used for short-term forecasting.
To predict user budget expenses, a combination 2.2.2. LSTM model
of two models was used: ARIMA (Auto Regressive
For long-term forecasts, the LSTM model is
Integrated Moving Average) and LSTM (Long
used, which is a type of recurrent neural network
Short-Term Memory). Both models are designed to
(RNN). The LSTM model can capture long-term
work with time series data but have different
dependencies in time series data due to its specific
approaches to solving the problem. In this context,
architecture, which includes memory cells and
ARIMA was used for short-term forecasts, and
mechanisms for forgetting and retaining
LSTM for long-term forecasts, allowing for more
information. Mathematically, the behavior of a
accurate and stable predictions. The first stage of
single LSTM block is described by the following
prediction is data preparation. This includes data
equations:
cleaning, handling missing values, and standardizing
the data format. The main focus is on removing 𝑓 = 𝜎(𝑊 ⋅[ℎ ,𝑥 ]+𝑏 )
𝑡 𝑓 𝑡−1 𝑡 𝑓
trends and seasonality from the data series, as these 𝑖 = 𝜎(𝑊 ⋅[ℎ ,𝑥 ]+𝑏 )
𝑡 𝑖 𝑡−1 𝑡 𝑖
factors can affect the accuracy of the forecast. 𝐶 ~ =𝑡𝑎𝑛ℎ𝑡𝑎𝑛ℎ (𝑊 ⋅[ℎ ,𝑥 ]+𝑏 ) ,
𝑡 𝐶 𝑡−1 𝑡 𝐶
𝐶 =𝑓 ∗𝐶 +𝑖 ∗𝐶 ~
2.2.1. ARIMA model 𝑡 𝑡 𝑡−1 𝑡 𝑡
𝑜 = 𝜎(𝑊 ⋅[ℎ ,𝑥 ]+𝑏 )
𝑡 𝑜 𝑡−1 𝑡 𝑜
The ARIMA model consists of three ℎ =𝑜 ∗𝑡𝑎𝑛ℎ𝑡𝑎𝑛ℎ (𝐶 )
𝑡 𝑡 𝑡
components:
• AR (AutoRegressive) component, which where 𝑓 𝑡 is the forget vector 𝑖 𝑡 is the input vector,
models the dependency between an observation and 𝐶 𝑡 ~ is the new candidate for the cell state value; 𝐶 𝑡
several previous observations. is the updated cell state, 𝑜 𝑡 is the output vector; ℎ 𝑡
• I (Integrated) component, used to eliminate is the vector of output values from the LSTM block;
non-stationarity. 𝑊 𝑓 , 𝑊 𝑖 , 𝑊 𝐶 , 𝑊 𝑜 are weight matrices; 𝑏 𝑓 , 𝑏 𝑖 , 𝑏 𝐶 , 𝑏 𝑜
• MA (Moving Average) component, which are bias vectors.
models the dependency between an observation and The LSTM network is trained on historical
the forecast error. spending data to create long-term forecasts, taking
Mathematically the ARIMA(p, d, q) is into account long-term dependencies between
described by the equation: observations.
𝑦 = 𝑐+𝜙 𝑦 +𝜙 𝑦 +⋯+𝜙 𝑦 + 2.2.3. Combination of forecasts
𝑡 1 𝑡−1 2 𝑡−2 𝑝 𝑡−𝑝
𝜃 𝜖 +𝜃 𝜖 +⋯+𝜃 𝜖 +𝜖 ,
1 𝑡−1 2 𝑡−2 𝑞 𝑡−𝑞 𝑡 The final step is the combination of forecasts
obtained from the ARIMA and LSTM models. For
where 𝑦 is the value of the series at time 𝑡, 𝜙 are
𝑡 𝑖 this, a weighted average method is used, where the
the coefficients of the AR component; 𝜃 are the
𝑗 results of both models are combined to obtain the
coefficients of the MA component 𝜖 is the random
𝑡 final expense forecast.
error term, c is a constant.
The formula for the final forecast is as follows:
The process of building an ARIMA model
includes determining the orders p, d, q. The 𝑦 ^ = 𝛼⋅𝑦𝐴𝑅𝐼𝑀𝐴^ +(1−𝛼)⋅𝑦𝐿𝑆𝑇𝑀^ ,
𝑡 𝑡 𝑡
parameter p represents the order of the
where 𝛼 is the weight coefficient that determines
autoregressive component, i.e., the number of
the influence of each model on the final result.
previous values used for forecasting; it is
The combination of ARIMA and LSTM allows
represented in the formula by the coefficients 𝜙 for
𝑖
for consideration of both short-term and long-term
values 𝑦 . The parameter d denotes the degree of
𝑡−𝑖
trends, enhancing the accuracy of user expense
differencing, which determines how many times the
forecasts.
series needs to be differences to ensure stationarity;
this operation is performed on the time series before 2.3. LLM for generating financial
applying the formula. The parameter q indicates the recommendations
order of the moving average component, meaning
A large language model (LLM), such as LLaMa
the number of previous random errors considered in
3.1, can be effectively used to generate personalized
forecasting; it is represented by the coefficients 𝜃
𝑗
financial recommendations based on the analysis of
for the error terms 𝜖 . After determining these
𝑡−𝑗 previous financial data, spending anomalies, and
parameters, usually selected using the Akaike
budget forecasts. This section provides a detailed
Information Criterion (AIC) or Bayesian
look at the approach to using LLM for this task and
ISSN 2617-4316 (Print) Software engineering and systems analysis 351
ISSN 2663-7723 (Online)

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology
                                                                                          2024; Vol.7 No.4: 348–358
presents  a  diagram  describing  the  process  of  recommendation. Fig. 2 shows an example of the
integrating the LLM model into the overall system  model’s response based on the provided context.
architecture.  Figure  3  demonstrates  the  interaction  of  AI
|     |     |     |     |     |     |     | components  |     | within  | the  | financial  | system.  |     | In  the  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ---- | ---------- | -------- | --- | -------- |
2.3.1. Data collections and preparation
initial stage, the system receives input data on the
To generate personalized recommendations, it  user’s  financial  transactions,  which  then  pass
is important to ensure high-quality input data.   through the data preprocessing module. This module
This data includes:  is responsible for data cleaning, normalization, and
– historical transaction data of the user;  preparation for further analysis by the models.
– data on detected spending anomalies;
3. ENSURING COMPLIANCE WITH
| –   | budget  | expenditure  |     | forecasts  | based  | on  |     |     |     |     |     |     |     |     |
| --- | ------- | ------------ | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ETHICAL PRINCIPLES IN THE SYSTEM
ARIMA and LSTM models;
 additional  Ethics  is  an  important  aspect  in  designing
|     |     | parameters,  |     | such  as  | the  | user’s  |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
financial goals, risk tolerance, and typical spending  recommendation  systems  (RS)  for  supporting
|     |     |     |     |     |     |     | financial  | decisions,  |     | as  it affects  |     | how  | much  | users  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --------------- | --- | ---- | ----- | ------ |
patterns.
The  data  is  transferred  to  the  LLM  after  trust the system and how willing they are to accept
recommendations as objective and unbiased.
| preprocessing,  |     | which  | includes  | normalization,  |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In [25], an analysis of ethical issues created by
categorization, and extraction of the key features.
|     |     |     |     |     |     |     | recommendation  |     | systems  |     | is  conducted.  |     | The  | study  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --- | --------------- | --- | ---- | ------ |
2.3.2. Generation of personalized advice  describes  how ethical consequences  can arise in a
|     |     |     |     |     |     |     | recommendation  |     |     | system:  | its  | operations  |     | can  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | -------- | ---- | ----------- | --- | ---- |
After configuring the LLM, the model can use
|                 |     |       |     |         |               |     | (negatively)  |     | impact  | the      | utility  | for  | each     | of  its  |
| --------------- | --- | ----- | --- | ------- | ------------- | --- | ------------- | --- | ------- | -------- | -------- | ---- | -------- | -------- |
| the  available  |     | data  | to  | create  | personalized  |     |               |     |         |          |          |      |          |          |
|                 |     |       |     |         |               |     | stakeholders  |     | and/or  | violate  | their    |      | rights.  | Ethical  |
recommendations.
|      |                 |     |     |             |          |     | impacts  | can  | be  immediate  |     |     | (e.g.,  | an  inaccurate  |     |
| ---- | --------------- | --- | --- | ----------- | -------- | --- | -------- | ---- | -------------- | --- | --- | ------- | --------------- | --- |
| The  | recommendation  |     |     | generation  | process  |     |          |      |                |     |     |         |                 |     |
proceeds as follows:  recommendation  leading  to  reduced  utility  for  the
user) or expose relevant parties to future risks (such
| 1.  | Processing  | input  | data: The  | LLM  | receives  |     |     |     |     |     |     |     |     |     |
| --- | ----------- | ------ | ---------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
input data, including transaction history, projected  as the influence of potentially irrelevant or harmful
content).
expenses, and anomaly information.
2.  Context formation: The model defines  the  The  authors  of  [26]  analyze  recommendation
system technology from the perspective of methods
context based on the user’s current financial status,
forecasts, and identified anomalies.  used to address issues in the following areas: privacy,
|     |     |     |     |     |     |     | personal  | data,  | fairness,  |     | transparency,  |     |     | personal  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---------- | --- | -------------- | --- | --- | --------- |
3. Generating recommendations: Based on the
context,  the  model  generates  several  options  for  identity, and the proper functioning of society.
An AI-powered system must ensure a balance
financial advice, taking into account both the user’s
short-term and long-term goals.  between its ability influence the user and the user’s
|                |     |     |                   |     |     |       | autonomy,  | promoting  |     |     | more  | rational  |     | financial  |
| -------------- | --- | --- | ----------------- | --- | --- | ----- | ---------- | ---------- | --- | --- | ----- | --------- | --- | ---------- |
| 4. Evaluation  |     | of  | recommendations:  |     |     | Each  |            |            |     |     |       |           |     |            |
behavior. One of the ethical advantages of such a
| recommendation  |     | is  evaluated  |     | in  terms  |     | of  its  |     |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
system is its ability to help users become aware of
alignment with the user’s individual characteristics,
their financial habits without judgement, offering the
such as risk level, financial goals, and preferences.
|     |     |     |     |     |     |     | opportunity  | for  | an  | objective  | analysis  |     | of  spending  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | --- | ---------- | --------- | --- | ------------- | --- |
The generated recommendations are delivered
and savings, regardless of income level.
to the user through the system interface as structured
|               |     |            |               |     |      |     | An  | AI-based  |     | recommendation  |     |     | system  | can  |
| ------------- | --- | ---------- | ------------- | --- | ---- | --- | --- | --------- | --- | --------------- | --- | --- | ------- | ---- |
| suggestions,  |     | including  | explanations  |     | and  | an  |     |           |     |                 |     |     |         |      |
promote responsible financial behavior by enhancing
| assessment of the potential consequences  |     |     |     |     | of  | each  |              |            |     |            |     |      |          |       |
| ----------------------------------------- | --- | --- | --- | --- | --- | ----- | ------------ | ---------- | --- | ---------- | --- | ---- | -------- | ----- |
|                                           |     |     |     |     |     |       | the  user’s  | financial  |     | awareness  |     | and  | helping  | them  |
decision. The user can select one of the suggestions
|     |     |     |     |     |     |     | avoid  | potentially  |     | irrational  | expenditures.  |     |     | In  an  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ----------- | -------------- | --- | --- | ------- |
or request additional recommendation of the initial
aggressive marketing environment, where users are
set does not meet their needs. The recommendations
constantly exposed to advertising, an ethically built
| are  adapted  |           | to  the  | user’s  | financial         | capacity,  |       |                 |     |         |     |         |        |     |           |
| ------------- | --------- | -------- | ------- | ----------------- | ---------- | ----- | --------------- | --- | ------- | --- | ------- | ------ | --- | --------- |
|               |           |          |         |                   |            |       | recommendation  |     | system  |     | allows  | users  | to  | maintain  |
| providing     | valuable  | advice   |         | for  individuals  |            | with  |                 |     |         |     |         |        |     |           |
control over their financial decisions. AI algorithms
various income levels, from low to high. Since the
analyze data to ensure the accuracy and usefulness
| analysis,  | forecasting  | and  | advice  | generation  |     | occur  |                       |     |     |           |     |               |     |      |
| ---------- | ------------ | ---- | ------- | ----------- | --- | ------ | --------------------- | --- | --- | --------- | --- | ------------- | --- | ---- |
|            |              |      |         |             |     |        | of  recommendations,  |     |     | avoiding  |     | manipulation  |     | and  |
within the context of the user’s specific financial
|     |     |     |     |     |     |     | supporting  | user’s  |     | long-term  | financial  |     | goals.  | This  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | ---------- | ---------- | --- | ------- | ----- |
operations, the system will be beneficial regardless
|     |     |     |     |     |     |     | helps  | users  | navigate  | a   | complex  |     | informational  |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --------- | --- | -------- | --- | -------------- | --- |
of the user’s income level.
landscape where marketing influences often lead to
Fig. 1 illustrates an example of a request to the
impulsive purchases and irrational spending.
| LLM  | to  | obtain  | a  personalized  |     | financial  |     |     |     |     |     |     |     |     |     |
| ---- | --- | ------- | ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
352  Software engineering and systems analysis  ISSN 2617-4316 (Print)
|     |     |     |     |     |     |     |     |     |     |     | ISSN 2663-7723 (Online)  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |

Shuryhin K. A., Zinovatna S. L. / Applied Aspects of Information Technology
2024; Vol.7 No.4: 348–358
Fig. 1. Diagram of the request implementation to the LLM for obtaining a personalized
financial recommendation
Source: compiled by the authors
Fig. 2. Example of the model’s response based on the provided context
Source: compiled by the authors
ISSN 2617-4316 (Print) Software engineering and systems analysis 353
ISSN 2663-7723 (Online)

Shuryhin K. A., Zinovatna S. L. / Applied Aspects of Information Technology
2024; Vol.7 No.4: 348–358
Fig. 3. Diagram of the interaction of AI components within the system
Source: compiled by the authors
The ethical nature of the system is reinforced illustrating the main entities of the financial platform
by its focus on the user’s interests. Instead of and the relationships between them. The diagram
evaluating or judging financial behavior, the system covers various aspects of the system’s operation,
provides structured, well-founded advice that helps including user management, transactions, budgets,
users better understand their spending patterns, financial goals, subscriptions, and categories.
identify potential saving opportunities, and optimize Fig. 5 and Fig. 6 provide examples of the screen
their budget. Importantly, the recommendations are forms of the developed system.
tailored to the user’s individual goals and The system’s software implementation is built
preferences, preserving their independence and on a modular architecture, including several
autonomy in making financial decisions. The system components, each responsible for a specific part of
does not impose specific actions but instead offers a the functionality. The main components are the AI
variety of options from which the user can choose Module, Budget Module, API Gateway,
that best meet their needs and goals. Authentication Module, and other integrations with
cloud services such as AWS Glue and AWS SQS.
4. IMPLEMENTATION OF THE
The AI Module is implemented in Python using
RECOMMENDATION SYSTEM
libraries like scikit-learn, TensorFlow, and
The architecture of the system is built on an event- statsmodels. Python was chosen for this module due
driven approach with a high-level of module to its powerful data processing capabilities, ease of
independence. The overall operations principle of the integrating machine learning algorithms, and support
system, which supports core financial operations, for a wide range of analytics libraries.
integration with banking systems, as well as data The Budget Module is implemented in Java
cleaning and preparation processes for further AI using the Spring Framework to ensure fast and
module analysis, is that each module operates reliable processing of user financial transactions.
autonomously. For example, the Budget Module This module allows adding new transactions,
remains operations even if the AI module is temporarily creating budgets, and retrieving expense data. Using
unavailable, and vice versa. The AI module is Spring facilitates easy configuration of REST APIs
responsible for key functions such as detecting for interaction with other modules and the client
anomalous expenses, forecasting future expenses during side. The choice of Spring is based on its
budgeting, generating personalized financial advice, and effectiveness for building scalable web applications
recommending alternative spending options. The Build- and microservices. Additionally, using Java ensures
Train-Deploy pattern is used to integrate the AI model reliability and a high level of security in data
into the microservices architecture, supported by AWS processing.
SageMaker, which automates model training, testing, The API Gateway is implemented with Spring
and deployment [27]. Cloud Gateway, allowing efficient routing of
A database has been developed to store data requests between different microservices in the
that provides input information for the system. This solution provides a centralized entry
recommendation system, with its Entity- point for all client requests and enables the
Relationship Diagram (ERD) model shown in Fig. 4, application of security policies and load balancing.
354 Software engineering and systems analysis ISSN 2617-4316 (Print)
ISSN 2663-7723 (Online)

Shuryhin K. A., Zinovatna S. L.                 /       Applied Aspects of Information Technology
                                                                                          2024; Vol.7 No.4: 348–358

Fig. 4. ERD for the recommendation system
Source: compiled by the authors
Spring Cloud Gateway was chosen for its ease
of configuration and ability to scale with the system,
which is critically important to ensure continuous
availability of services.
To ensure reliable user authentication, OAuth
2.0 is used, which allows for controlling access to
|     | the  system’s  |        | protected                            | resources  |             | via  | tokens.  |
| --- | -------------- | ------ | ------------------------------------ | ---------- | ----------- | ---- | -------- |
|     | Implementing   | OAuth  | 2.0                                  | on         | the  basis  | of   | Spring   |
|     | Security       | makes  | it easy to integrate authentication  |            |             |      |          |
Fig. 5. Main page
with other modules and ensures reliable control over
Source: compiled by the authors
access to important data. Spring Security was chosen
|     | for  this   | task  due  | to  its       | seamless  | integration  |        | with  |
| --- | ----------- | ---------- | ------------- | --------- | ------------ | ------ | ----- |
|     | OAuth  2.0  | and        | its  ability  | to        | quickly      | adapt  | to    |
different levels of user access.
For processing large volumes of transaction and
|     | budget  data, AWS          |             | Glue   | is  used                | to  | perform  | ETL      |
| --- | -------------------------- | ----------- | ------ | ----------------------- | --- | -------- | -------- |
|     | (Extract,                  | Transform,  | Load)  | operations              |     | to       | prepare  |
|     | data for further analysis  |             |        | in the AI Module. Glue  |     |          |          |

|     | Crawler  | automatically  |     | determines  | the  | schema  | of  |
| --- | -------- | -------------- | --- | ----------- | ---- | ------- | --- |
Fig. 6. Use of AI models for anomaly detection
data stored in S3 and makes it available for further
Source: compiled by the authors
processing.
ISSN 2617-4316 (Print)  Software engineering and systems analysis  355
ISSN 2663-7723 (Online)

Shuryhin K. A., Zinovatna S. L. / Applied Aspects of Information Technology
2024; Vol.7 No.4: 348–358
AWS SQS is used for message queuing identify potentially spontaneous or uncharacteristic
between microservices. This enables asynchronous expenses.
event processing and reliable message transmission, In parallel, ARIMA and LSTM models are used
for example, about anomalies in financial expenses. to forecast future expenses. ARIMA provides short-
Terraform is used to automate the creation of term forecasts, accounting for seasonal fluctuations
AWS infrastructure, including configuring SQS and dependencies in time series, while LSTM, with
queues and S3 buckets. This makes it easy to set up its ability to capture long-term dependencies, is used
and scale the cloud infrastructure to meet system for more stable long-term forecasts.
requirements. The data generated by these models is fed into a
The client side of the system is implemented in large language model (LLM), which integrates
React.js, providing an interactive and fast user anomaly results, short-term, and long-term forecasts
interface. React enables the construction of Single to produce personalized financial recommendations.
Page Applications (SPA), ensuring quick response These recommendations are tailored to the user’s
and dynamic data updates without page reloads. specific financial goals and behavior and can help
React.js was chosen for its popularity, performance, optimize the budget, reduce risks, or increase
and extensive capabilities for integration with REST savings.
APIs. The system ensures high accuracy through the
combination of various AI models (ARIMA and
CONCLUSIONS
LSTM for forecasting, Isolation Forest for anomaly
The use of AI models for a system that detection, and LLM for generating advice),
generates personalized financial recommendations is completeness by training on user’s transactions and
described. The Isolation Forest model is applied to financial operations, as well as privacy and security
detect anomalous transactions, using a tree-like by adhering to OAuth 2 standards and OWASP Top
structure to isolate deviations in the user’s financial 10 principles. The systems’ ethical aspect is reflected
behavior. This enables the model to effectively in its support for users in managing their finances
rationally, without judgement of their decisions.
REFERENCES
1. Lu, J., Zhang, Q. & Zhang, G. “Intelligent information systems”. 2020. DOI:
https://doi.org/10.1142/11947.
2. Verma, P. & Sharma S. “Artificial Intelligence based recommendation system”. 2nd International
Conference on Advances in Computing, Communication Control and Networking. Greater Noida, India.
2020. p. 669–673. DOI: https://doi.org/10.1109/ICACCCN51052.2020.9362962.
3. Roy, D. & Dutta, M. “A systematic review and research perspective on recommender systems”.
Journal of Big Data. 2022; 9: 59. DOI: https://doi.org/10.1186/s40537-022-00592-5.
4. Hodovychenko M. A., Gorbatenko A. A. “Recommender systems: models, challenges and
opportunities”. Herald of Advanced Information Technology. 2023; 6 (4): 308–319.
DOI: https://doi.org/10.15276/hait.06.2023.20.
5. He, X., Liu, Q. & Jung, S. “The impact of recommendation system on user satisfaction: A moderated
mediation approach”. J Journal of Theoretical and Applied Electronic Commerce Research. 2024; 19 (1):
448–466. DOI: https://doi.org/10.3390/jtaer19010024.
6. Deschênes, M. “Recommender systems to support learners’ Agency in a learning context: a
systematic review”. International Journal of Educational Technology in Higher Education. 2020; 17: 50.
DOI: https://doi.org/10.1186/s41239-020-00219-w.
7. Reiter-Gavish, L., Qadan, M. & Yagil, J. “Financial advice: Who Exactly Follows It?” Research in
Economics. 2021; 75 (3): 244–258. DOI: https://doi.org/10.1016/j.rie.2021.06.003.
8. Schepen, A. & Burger, M. J. “Professional financial advice and subjective Well-Being”. Applied
Research Quality Life. 2022; 17: 2967–3004. DOI: https://doi.org/10.1007/s11482-022-10049-9.
9. Fieberg, C., Hornuf, L. & Streich, D. “Using GPT-4 for financial advice”. CESifo. 2023.
DOI: http://dx.doi.org/10.2139/ssrn.4499485.
356 Software engineering and systems analysis ISSN 2617-4316 (Print)
ISSN 2663-7723 (Online)

Shuryhin K. A., Zinovatna S. L. / Applied Aspects of Information Technology
2024; Vol.7 No.4: 348–358
10. Sharaf, M., Hemdan, E. E. D., El-Sayed, A. et al. “A survey on recommendation systems for
financial services”. Multimedia Tools and Applications. 2022. DOI: https://doi.org/10.1007/s11042-022-
12564-1.
11. Zatevakhina, A., Dedyukhina, N. & Klioutchnikov O. “Recommender systems – The foundation of
an intelligent financial platform: Prospects of development”. International Conference on Artificial
Intelligence: Applications and Innovations (IC-AIAI). Belgrade, Serbia. 2019. p. 104–1046.
DOI: https://doi.org/10.1109/IC-AIAI48757.2019.00029.
12. Zibriczky, D. “Recommender systems meet finance: A literature review”. 2nd International
Workshop on Personalization and Recommender Systems in Financial Services. Bari, Italy. 2016.
DOI: https://doi.org/10.13140/RG.2.1.1249.2405.
13. Kanaujia, P. K. M., Behera, N., Pandey, M. & Rautaray S. S. “Recommendation system for financial
analytics”. International Conference on ICT in Business Industry & Government. 2016.
DOI: https://doi.org/10.1109/ICTBIG.2016.7892673.
14. Li, T. & Song, J. “Deep learning-powered financial product recommendation system in banks:
Integration of transformer and transfer learning”. Journal of Organizational and End User Computing. 2024;
36 (1): 1–29. DOI: https://doi.org/10.4018/JOEUC.343257.
15. Ayemowa, M. O., Ibrahim, R. & Khan, M. M. “Analysis of recommender system using generative
artificial intelligence: A systematic literature review”. IEEE Access. 2024; 12: 87742–87766.
DOI: https://doi.org/10.1109/ACCESS.2024.3416962.
16. Yue, X. “Application of AI technology in personalized recommendation system for financial
services”. Applied Mathematics and Nonlinear Sciences. 2024; 9 (1). DOI: https://doi.org/10.2478/amns-
2024-1349.
17. Jannach, D., Pu, P., Ricci, F. & Zanker, M. “Recommender systems: Past, present, future”. AI
Magazine. 2021; 42: 3–6. DOI: https://doi.org/10.1609/aimag.v42i3.18139.
18. Chua, A. Y.K., Pal, A. & Banerjee, S. “AI-enabled investment advice: Will users buy it?”.
Computers in Human Behavior. 2023; 138: 107481. DOI: https://doi.org/10.1016/j.chb.2022.107481
19. Longoni, C., Bonezzi, A. & Morewedge, C. K. “Resistance to medical artificial intelligence”.
Journal of Consumer Research. 2019; 46 (4): 629–650. DOI: https://doi.org/10.1093/jcr/ucz013.
20. Zhang, L., Pentina, I. & Fan, Y. “Who do you choose? Comparing perceptions of human vs robo-
advisor in the context of financial services”. The Journal of Services Marketing; 2021;35 (5): 634–646.
DOI: https://doi.org/10.1108/JSM-05-2020-0162.
21. Bonelli, M. I. & Döngül, E. S. “Robo-advisors in the financial services industry: recommendations
for full-scale optimization, digital twin integration, and leveraging natural language processing trends”. 9th
International Conference on Virtual Reality. Xianyang, China. 2023. p. 268–275.
DOI: https://doi.org/10.1109/ICVR57957.2023.10169615.
22. Zhang, Q., Lu, J. & Jin, Y. “Artificial intelligence in recommender systems”. Complex & Intelligent
Systems. 2020; 7. DOI: https://doi.org/10.1007/s40747-020-00212-w.
23. del Valle, J. I. & Lara, F. “AI-powered recommender systems and the preservation of personal
autonomy”. AI & Society. 2024; 39: 2479–2491. DOI: https://doi.org/10.1007/s00146-023-01720-2.
24. Christman, J. “Autonomy in moral and political philosophy. The stanford encyclopedia of
philosophy”. 2020. – Available from: https://plato.stanford.edu/archives/fall2020/entries/autonomy-moral.
25. Milano, S., Taddeo, M. & Floridi, L. “Recommender systems and their ethical challenges”. AI &
Society. 2020; 35: 957–967. DOI: https://doi.org/10.1007/s00146-020-00950-y.
26. Karakolis, E., Oikonomidis, P. F. & Askounis, D. "Identifying and addressing ethical challenges in
recommender systems". 13th International Conference on Information, Intelligence, Systems & Applications.
Corfu, Greece. 2022. p. 1–6. DOI: https://doi.org/10.1109/IISA56318.2022.9904386.
27. Shuryhin K. A., Zinovatna S. L. “Architecture of the financial manager system using AI
technologies” (In Ukrainian). Х International Scientific and Practical Conference
“Informatics.Culture.Technology”. Odesa, Ukraine. 2024; 1 (1): 118–123. DOI:
https://doi.org/10.15276/ict.01.2024.17.
Conflicts of Interest: The authors declare that they have no conflict of interest regarding this study, including financial, personal, authorship or other,
which could influence the research and its results presented in this article
ISSN 2617-4316 (Print) Software engineering and systems analysis 357
ISSN 2663-7723 (Online)

Shuryhin K. A., Zinovatna S. L. / Applied Aspects of Information Technology
2024; Vol.7 No.4: 348–358
Received 29.08.2024
Received after revision 09.10.2024
Accepted 30.1.2024
DOI: https://doi.org/10.15276/aait.07.2024.24
УДК 004.414.32
Рекомендаційна система для прийняття фінансових
рішень з використанням штучного інтелекту
Шуригін Костянтин Андрійович1)
ORCID: https://orcid.org/0009-0002-1000-303X; ksurygin5@gmail.com
Зіноватна Світлана Леонідівна1)
ORCID: https://orcid.org/0000-0002-9190-6486; zinovatnaya.svetlana@op.edu.ua. Scopus Author ID: 57219779480
1) Національний університет «Одеська політехніка», пр. Шевченка, 1. Одеса, 65044, Україна
АНОТАЦІЯ
Стрімке поширення штучного інтелекту (ШІ) на споживчих ринках створює серйозні виклики для суспільства, зокрема
в контексті використання когнітивних упереджень, що впливають на ухвалення фінансових рішень споживачами. Ці
упередження можуть призводити до нераціональних витрат, що ставить під сумнів етичність застосування ШІ у подібних
сферах. У цьому дослідженні розглядається, як ШІ може не тільки підвищувати ефективність ухвалення фінансових рішень,
але й допомагати споживачам приймати більш обґрунтовані та раціональні рішення. Основна увага зосереджена на розробці
інтелектуальної системи управління фінансами, яка застосовує сучасні алгоритми ШІ для аналізу фінансової поведінки,
виявлення аномалій та надання персоналізованих рекомендацій. У статті розглядається система генерації персоналізованих
фінансових рекомендацій на основі великих мовних моделей, яка використовує історію транзакцій, прогнозовані витрати та
інформацію про аномалії для створення індивідуальних порад. Зокрема, досліджуються моделі машинного навчання, такі як
Isolation Forest для ідентифікації атипових фінансових дій, а також поєднання ARIMA та LSTM для прогнозування
бюджетів. Дослідження також розглядає можливість інтеграції цих моделей із використанням великих мовних моделей
(LLM) для генерування персоналізованих рекомендацій. Методологічна частина роботи включає аналіз існуючих моделей і
сфер їхнього застосування, визначення типів та структури даних для обробки, розробку системи, що інтегрує наявні моделі,
та її тестування. Описано процес формування рекомендацій, що включає етапи обробки вхідних даних, формування
контексту, генерації рекомендацій та їх оцінки з урахуванням характеристик користувача, таких як рівень ризику, фінансові
цілі та уподобання. Генеровані рекомендації спрямовані на оптимізацію фінансової поведінки користувача та можуть бути
адаптовані до різних рівнів доходів. Окрему увагу приділено етичним аспектам системи, що включають забезпечення
конфіденційності, справедливості та прозорості, а також важливості підтримки автономії користувача у прийнятті
фінансових рішень. Система сприяє розвитку відповідальної фінансової поведінки, допомагаючи уникати імпульсивних
витрат та підвищуючи фінансову обізнаність без маніпуляцій чи нав’язування конкретних рішень.
Ключові слова: штучний інтелект, машинне навчання, когнітивні упередження, фінансові рішення, етичність.
ABOUT THE AUTHORS
Kostiantyn A. Shuryhin - Master, Software Engineering Department. Odesа Polytechnic National University, 1, Shevchenko
Ave. Odesa, 65044, Ukraine
ORCID: https://orcid.org/0009-0002-1000-303X; ksurygin5@gmail.com.
Research field: Software architecture; data processing; distributed systems
Шуригін Костянтин Андрійович - магістр кафедри Інженерії програмного забезпечення. Національний університет
«Одеська політехніка», пр. Шевченка, 1. Одеса, 65044, Україна
Svitlana L. Zinovatna - Candidate of Engineering Sciences, Associate Professor, Software Engineering Department. Odesа
Polytechnic National University, 1, Shevchenko Ave. Odesa, 65044, Ukraine
ORCID: https://orcid.org/0000-0002-9190-6486; zinovatnaya.svetlana@op.edu.ua. Scopus Author ID: 57219779480
Research field: Information technology; data processing, improving the performance of information systems
Зіноватна Світлана Леонідівна - кандидат технічних наук, доцент кафедри Інженерії програмного забезпечення.
Національний університет «Одеська політехніка», пр. Шевченка, 1. Одеса, 65044, Україна
358 Software engineering and systems analysis ISSN 2617-4316 (Print)
ISSN 2663-7723 (Online)