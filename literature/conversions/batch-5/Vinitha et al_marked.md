---
conversion_metadata:
  converted_at: "2026-07-21T09:12:29Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Vinitha et al.pdf"
  source_pdf_sha256: "df52fc5c3b5b00fe3e54eeead3cda3268ed11f0a54ca12e754a3091a0ff42c0b"
  page_count: 9
  markdown_char_count: 59910
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

International Journal of

DATA SCIENCE AND IOT MANAGEMENT SYSTEM

Peer Reviewed, Referred & Indexed Journal 
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper 
AI-Driven Personal Finance Management: Predictive Expense Forecasting 
and Behavioural Clustering

C. Vinitha1*, Arra Hari Krishna2, Eyikyala Manikanta Reddy2, Pullala Javari2

1Assistant Professor, 2UG Student, 1,2Department of Computer Science and Engineering

1,2Kommuri Pratap Reddy Institute of Technology, Ghanpur, Ghatkesar, 501301, Telangana, India.

*Correspondence: C. Vinitha (vnreddy61@gmail.com)

ABSTRACT

Financial  planning  and  expense  management  have  become  increasingly  essential  as  individuals 
struggle  to  monitor  daily  spending,  interpret  financial  behavior,  and  plan  future  investments 
effectively. With the rapid growth of digital transactions and diverse expenditure categories, manual 
financial  tracking  becomes  complex,  time-consuming,  and  prone  to  errors.  Traditional  financial 
management systems, such as spreadsheets and basic budgeting tools, allow users to store transaction 
data but lack advanced analytical capabilities, making accurate prediction of future expenses difficult 
and  leading  to  inefficient  financial  decisions.  To  address  these  limitations,  the  proposed  system 
introduces  an  intelligent  financial  prediction  and  analysis  platform  developed  using  the  Django 
framework  with  a  MySQL  (Structured  Query  Language-based  relational  database  management 
system) database for secure data storage and management. The system incorporates email-based One-
Time  Password  (OTP)  authentication  using  the  Simple  Mail  Transfer  Protocol  (SMTP)  to  ensure 
secure and verified user access. A Long Short-Term Memory (LSTM) deep learning model is utilized 
to  analyze  historical  financial  data  and  predict  future  expenses  by  capturing  temporal  patterns  and 
trends.  Additionally,  K-Means  clustering  is  applied  to  group  expenses  into  different  categories, 
enabling users to better understand their spending behavior and identify financial patterns. The system 
further  integrates  sentiment  analysis  using  VADER  (Valence  Aware  Dictionary  and  Sentiment 
Reasoner)  to  evaluate  user  feedback  and  classify  it  as  positive,  negative,  or  neutral,  supporting 
continuous system improvement. By combining predictive modeling, clustering techniques, sentiment 
evaluation, and secure authentication mechanisms, the system provides automated financial insights, 
personalized  recommendations,  and  enhanced  decision-making  support,  helping  users  manage 
finances more efficiently.

Key words:   Financial Prediction, Expense Analysis, Sentiment Analysis, Machine Learning, Deep 
Learning, Django Web Framework.

1. INTRODUCTION

Anticipating future outcomes has become an essential capability across multiple economic domains, 
particularly for shaping decisions at both local and regional governance levels [1]. Within the business 
environment,  especially  in  wholesale  and  retail  trade,  the  projection  of  financial  measures  plays  a 
central  role  in  guiding  operational  and  strategic  actions,  including  production  scheduling,  sales 
planning,  and  inventory  control.  This  sector  is  uniquely  complex  due  to  fluctuating  consumer 
preferences,  pronounced  seasonal  demand  patterns,  and  the  impact  of  external  forces  such  as 
economic  conditions  and  political  developments  [2].  Despite  these  challenges,  estimating  key 
financial  metrics—such  as  revenue  streams,  expenditure  levels,  and  overall  profitability—is 
fundamental  for  designing  effective  corporate  strategies,  sustaining  long-term  growth,  and 
maintaining  competitive  positioning.  In  particular,  profit  estimation  supports  efficient  cash  flow

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  460

---

<!-- PAGE 2 -->

International Journal of

DATA SCIENCE AND IOT MANAGEMENT SYSTEM

Peer Reviewed, Referred & Indexed Journal 
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

management, liquidity planning, and performance evaluation, making it an indispensable component 
of financial decision-making in retail-oriented enterprises.

To predict the future trajectory of financial variables, as shown in Fig. 1,  it is necessary to analyze 
their historical progression over time. In certain technical fields, such behavior is often modeled using 
mathematical  formulations  like  partial  differential  equations.  However,  when  sufficiently  large 
datasets are available in economic contexts, advanced analytical methods—especially those based on 
time series modeling—can be employed to capture patterns and forecast future values. The growing 
reliance on historical time series information highlights its importance as a predictive foundation in 
modern  analytics  [3].  Such  data  enables  organizations  to  anticipate  upcoming  trends  and  make 
informed  replaceions  about  revenues,  costs,  and  profit,  which  are  vital  for  effective  planning  and 
operational success in retail businesses [4].

Fig. 1: Finance Management

Revenue  forecasting,  in  particular,  serves  as  a  cornerstone  for  cross-functional  decision-making: 
finance  teams  can  estimate  profitability  and  funding  needs,  sales  units  can  evaluate  demand  levels, 
procurement  departments  can  optimize  purchasing  strategies,  marketing  teams  can  assess  campaign 
effectiveness,  and  logistics  divisions  can  align  supply  chain  operations  accordingly.  Moreover, 
accurate replaceions of sales and expenses can assist investors in predicting fluctuations in retail stock 
performance. Profit, defined as the surplus remaining after deducting direct costs from total revenue, 
acts  as  a  key  indicator  of  financial  health  and  enables  comparisons  across  competing  firms  [5]. 
Therefore,  reliable  profit  forecasting  is  instrumental  in  supporting  strategic  choices  and  ensuring 
sustained financial stability.

1.1 Problem Definition

The central challenge in personal financial management is transforming voluminous, raw transaction 
data  into  accurate,  actionable,  and  personalized  insights  regarding  future  financial  status.  Users 
typically struggle with two key aspects, accurately predicting future expenses given non-linear trends, 
seasonal variations, and irregular large payments traditional methods often fail to capture the complex 
temporal  dependencies  inherent  in  spending  habits.  Understanding  how  and  why  money  is  spent, 
beyond simple category totals. Users need to identify underlying spending patterns, detect anomalies, 
and link their qualitative financial feelings to quantitative expense data.

2. LITERATURE SURVEY

Shiyyab et al. [6] proposed an AI disclosure index to quantitatively evaluate the extent of AI adoption 
within  financial  institutions  and  to  analyze  its  relationship  with  financial  performance.  The  study

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  461

---

<!-- PAGE 3 -->

International Journal of

DATA SCIENCE AND IOT MANAGEMENT SYSTEM

Peer Reviewed, Referred & Indexed Journal 
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

emphasizes  that  transparent  reporting  of  AI  usage  enhances  stakeholder  confidence  and  supports 
better  governance  practices.  By  systematically  measuring  disclosure  levels,  the  research  provides 
insights  into  how  organizations  communicate  their  AI  integration  strategies  and  highlights  the 
importance  of  standardized  disclosure  frameworks.  It  further  supports  policymakers  and  regulatory 
authorities in formulating guidelines that ensure accountability, transparency, and ethical deployment 
of AI systems in the banking sector. Yaseen, et al. [7] investigated the role of transparency, fairness, 
and  trust  in  influencing  the  adoption  of  AI  technologies  within  financial  environments.  The  study 
demonstrates  that  transparency  acts  as  a  primary  driver  of  trust,  which  directly  impacts  user 
acceptance  of  AI  systems.  It  also  shows  that  fairness  perception  plays  a  critical  role  in  mitigating 
concerns related to algorithmic bias, thereby improving system credibility. Additionally, the research 
identifies  variations  in  adoption  readiness  across  different  professional  groups  and  regions, 
highlighting the influence of experience and exposure to AI. The findings emphasize that regulatory 
compliance  and  the  development  of  explainable  and  unbiased  AI  models  are  essential  for  fostering 
adoption in highly regulated financial  sectors. El Hajj, et al. [8] utilized a mixed-methods approach 
combining  quantitative  surveys  and  qualitative  analysis  to  assess  the  adoption  of  AI  and  ML  in 
financial  markets.  The  study  identifies  widespread  use  cases  such  as  algorithmic  trading,  fraud 
detection,  credit  scoring,  and  customer  service  automation.  It  also  explores  challenges  including 
regulatory  compliance,  ethical  concerns,  workforce  transformation,  and  data  privacy  issues.  The 
findings emphasize the need for continuous skill development and organizational adaptation to fully 
leverage AI technologies in finance.

Aleksandrova, et al. [9] conducted a comprehensive review of AI adoption across finance, insurance, 
and financial controlling, focusing on the economic implications and technological advancements in 
these  sectors.  The  study  identifies  key  trends  such  as  increased  automation,  enhanced  predictive 
analytics, and improved risk assessment capabilities. It also highlights challenges including regulatory 
constraints,  implementation  costs,  and  skill  gaps.  By  analyzing  existing  literature,  the  authors 
establish  a  strong  relationship  between  AI  integration  and  the  evolution  of  financial  systems, 
emphasizing  its  role  in  driving  efficiency  and  innovation.  Yang,  et  al.  [10]  explored  the  behavioral 
and  perceptual  factors  influencing  the  adoption  of  GenAI  in  financial  advisory  services.  The  study 
developed a research framework based on SDL and AIDUA models to examine how personalization, 
human-like  empathy,  and  continuous  learning  capabilities  of  AI  systems  affect  user  trust  and 
acceptance.  The  findings  reveal  that  users  are  more  likely  to  adopt  AI-generated  financial  advice 
when it demonstrates contextual understanding and adaptive responses. The study also highlights the 
importance  of  perceived  authenticity  and  usefulness  in  shaping  user  attitudes  toward  AI-driven 
financial decision support systems. Shaban, et al. [11] investigated the relationship between AI-driven 
financial  transparency  and  corporate  governance  using  quantitative  techniques  such  as  SEM  and 
regression analysis. Based on data collected from corporate professionals, the study demonstrates that 
AI  significantly  enhances  governance  effectiveness,  improves  risk  management  practices,  and 
increases  stakeholder  engagement.  It  also  highlights  AI’s  role  in  automating  compliance  processes, 
while  acknowledging  challenges  such  as  algorithmic  bias,  data  privacy  concerns,  and  the  need  for 
updated regulatory frameworks.

Artene,  et  al.  [12]  investigated  the  combined  impact  of  AI,  DT,  and  financial  reporting  systems  on 
modern  business  environments,  emphasizing  how  their  integration  enhances  analytical  capabilities 
and  strategic  decision-making.  The  study  explains  that  organizations  adopting  AI-driven  financial 
reporting  can  automate  complex  accounting  processes,  reduce  human  intervention,  and  improve 
accuracy in financial statements. It further highlights the role of neural networks in modeling complex

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  462

---

<!-- PAGE 4 -->

International Journal of

DATA SCIENCE AND IOT MANAGEMENT SYSTEM

Peer Reviewed, Referred & Indexed Journal 
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

financial relationships, enabling pattern recognition, anomaly detection, and predictive analytics. The 
synergy  between  intelligent  systems  and  DT  initiatives  is  shown  to  create  adaptive,  data-driven 
ecosystems  that  improve  transparency,  operational  efficiency,  and  long-term  business  value.  
Mhlanga, et al. [13] explored the impact of AI on digital financial inclusion through a conceptual and 
documentary  review  of  scholarly  and  institutional  sources.  The  study  demonstrates  that  AI 
significantly  enhances  financial  accessibility  by  improving  risk  assessment  models,  reducing 
information  asymmetry,  and  enabling  automated  customer  interaction  through  chatbots.  It  further 
emphasizes  AI’s  role  in  strengthening  fraud  detection  and  cybersecurity  mechanisms,  thereby 
increasing trust and participation in digital financial systems, especially in underserved populations. 
Bayakhmetova,  et  al.  [14]  conducted  an  in-depth  bibliometric  analysis  using  Bibliometrix  and 
Bibliophagy tools to map the intellectual structure of AI research in finance. Their findings reveal a 
strong upward publication trend with a 13.34% annual growth rate, indicating rapid expansion of the 
field. The study identifies dominant research clusters, including ML applications, financial inclusion 
strategies,  and  intelligent  decision-support  systems.  Additionally,  it  highlights  underexplored  areas 
such as ethical AI design, regional inequalities in adoption, and limited deployment in low-resource 
environments, while also identifying leading journals and contributors shaping the research landscape. 
Liu,  et  al.  [15]  evaluated  the  capabilities  of  ChatGPT-4o  in  financial  reasoning  by  designing 
structured,  multi-step  analytical  tasks  that  simulate  real-world  financial  problem-solving.  The  study 
benchmarks AI performance against human analysts using task-specific evaluation metrics, revealing 
that  while  the  model  performs  effectively  in  structured  reasoning  and  data  interpretation,  it  faces 
limitations  in  handling  highly  complex  or  ambiguous  financial  scenarios.  The  research  underscores 
the  potential  of  conversational  AI  in  financial  analytics  while  also  identifying  areas  requiring 
improvement.

3. PROPOSED SYSTEM

This  research  presents  a  comprehensive,  data-centric  framework  designed  to  enable  personalized 
expense  prediction  and  intelligent  investment  guidance  through  advanced  analytics  and  machine 
learning techniques, as illustrated in Fig. 2. The system is developed using the Django web framework 
and extends beyond conventional financial tracking by integrating predictive modeling and behavioral 
analysis to enhance financial awareness and decision-making. At its core, the architecture combines 
two major ML approaches: an LSTM model for capturing temporal dependencies in expense data and 
generating accurate time-series forecasts, and a K-Means clustering algorithm for identifying hidden 
spending patterns and segmenting user behavior.

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  463

---

<!-- PAGE 5 -->

International Journal of

DATA SCIENCE AND IOT MANAGEMENT SYSTEM

Peer Reviewed, Referred & Indexed Journal 
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

Fig. 2: Proposed System architecture

The system follows a structured three-layer architecture consisting of a MySQL database for secure 
storage  and  user  management,  a  Python-based  backend  responsible  for  preprocessing  and  ML 
computations,  and  an  interactive  web  interface  that  facilitates  seamless  user  interaction.  Security  is 
ensured  through  a  multi-level  authentication  mechanism  that  incorporates  Base64-based  password 
encoding  along  with  OTP-based  2FA  via  SMTP,  thereby  safeguarding  user  accounts  and  sensitive 
financial information. Once authenticated, users upload their financial dataset (budget.csv), which is 
processed  using  Pandas,  where  date  features  such  as  year,  month,  and  day  are  extracted,  and  both 
numerical and categorical data are normalized using MinMaxScaler and StandardScaler to prepare it 
for ML models. The system then applies K-Means clustering on expense categories and amounts to 
group  similar  spending  behaviors,  enabling  users  to  visualize  and  understand  their  financial  habits 
more effectively. Simultaneously, the LSTM model is trained on historical daily expense data to learn 
sequential  patterns  and  generate  accurate  future  expense  predictions,  with  performance  evaluated 
using  metrics  such  as  score  and  MSE.  These  predicted  values  are  further  utilized  in  the 
recommendation  module,  where  a  practical  surplus  is  computed  by  comparing  estimated  expenses 
with  a  generated  income  approximation,  allowing  the  system  to  suggest  potential  savings  or 
investment opportunities. In addition to quantitative analysis, the framework incorporates a qualitative 
feedback  mechanism  where  users  can  submit  feedback  that  is  analyzed  using  VADER  sentiment 
analysis, enabling continuous monitoring of user satisfaction and system performance. The analyzed 
sentiment  results  are  stored  in  the  database  to  support  ongoing  improvements  and  adaptive  system 
behavior.  Overall,  this  integrated  pipeline  combines  forecasting,  clustering,  recommendation,  and 
sentiment analysis into a unified system that not only predicts future financial trends but also delivers 
personalized, actionable insights, thereby empowering users to make informed and effective financial 
decisions.

3.1 LSTM

The  LSTM  is  a  specialized  type  of  Recurrent  Neural  Network  designed  to  overcome  the  vanishing 
gradient  problem,  enabling  it  to  learn  long-term  dependencies  essential  for  time-series  forecasting 
(like expense trends).  Its core strength lies in the memory cell and three gates that regulate the flow 
of  information:  the  Forget  Gate  decides  which  information  to  discard  from  the  cell  state;  the  Input 
Gate decides which new information to store in the cell state; and the Output Gate determines which

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  464

---

<!-- PAGE 6 -->

International Journal of

DATA SCIENCE AND IOT MANAGEMENT SYSTEM

Peer Reviewed, Referred & Indexed Journal 
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

part  of  the  current  cell  state  is  outputted  as  the  hidden  state  for  the  current  timestamp.  This  gating 
mechanism  allows  the  LSTM  to  remember  patterns  that  occurred  months  ago  (like  annual  fees  or 
seasonal spending) and integrate them effectively into the current day's expense prediction as depicted 
in Fig. 3.

Fig. 3: Internal Workflow of LSTM.

Data Sequence Preparation: Raw time features (year, month, day) and total expenses are scaled. 
Input features are reshaped into sequences (3D format: [samples, timesteps, features]) required by the 
LSTM.

Forward Pass (Per Timestep): For each input sequence, the data passes through the gates 
sequentially:

●  Forget Gate: Multiplies the old cell state by a value between 0 and 1 (output of a sigmoid

function) to decide what to discard.

●  Input Gate: Determines new information to add to the cell state (using sigmoid for filtering

and tanh for creating candidate values).

●  Cell State Update: The old cell state is updated by forgetting old info and adding new info.

●  Output Gate: Determines the final output (hidden state) based on the new cell state.

Prediction: After processing the sequence, the output from the final LSTM layer feeds into a dense 
layer to produce the single-day expense forecast.

Backpropagation: The prediction error is calculated using the Mean Squared Error (MSE) loss 
function, and weights are adjusted using the Adam optimizer.

Iteration: Steps 2-4 are repeated over multiple epochs (1000 in the code) to minimize the loss and 
optimize model performance.

4. RESULTS DESCRIPTION

Fig. 4 illustrates the application of the K-Means clustering algorithm for analyzing expense behavior 
patterns.  The  clustering  model  groups  transaction  records  into  clusters  based  on  similarities  in

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  465

---

<!-- PAGE 7 -->

International Journal of

DATA SCIENCE AND IOT MANAGEMENT SYSTEM

Peer Reviewed, Referred & Indexed Journal 
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

spending  categories  and  expense  amounts.  Each  cluster  represents  a  distinct  pattern  of  financial 
activity  that  helps  identify  how  expenses  are  distributed  across  different  categories.  The  graphical 
representation provides insights into spending trends and financial behavior. This clustering analysis 
assists users in understanding their expense distribution and supports better financial planning.

Fig. 4: K-means clustering for personal finance

Fig. 5 depicts the evaluation results of the Long Short-Term Memory (LSTM) deep learning model 
used for expense prediction. The model performance is measured using evaluation metrics including 
Accuracy  of  0.9993  (99.93%)  and  Mean  Squared  Error  of  35.41.  A  graphical  comparison  between 
predicted  expenses  and  actual  test  expenses  is  also  displayed  to  illustrate  the  effectiveness  of  the 
prediction model. The graph demonstrates how closely the predicted values follow the actual financial 
expense  patterns.  This  evaluation  confirms  the  ability  of  the  LSTM  model  to  accurately  forecast 
future financial expenses.

Fig. 5: LSTM Model Evaluation Screen

Fig.  6  illustrates  the  budget  recommendation  module  of  the  system  where  financial  predictions  are 
used  to  generate  investment  suggestions.  Based  on  the  predicted  expenses  calculated  by  the  LSTM 
model,  the  system  estimates  the  user’s  expected  financial  expenditure.  For  example,  if  the  system 
assumes  an  income  of  45,648  units  and  predicted  expenses  of  36,987  units,  the  recommended 
investment  amount  is  calculated  as  8,661  units.  This  module  helps  users  allocate  their  income 
efficiently and make better financial planning decisions.

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  466

---

<!-- PAGE 8 -->

International Journal of

DATA SCIENCE AND IOT MANAGEMENT SYSTEM

Peer Reviewed, Referred & Indexed Journal 
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

Fig. 6: Recommend budget Screen

Fig. 7 depicts the feedback analysis module of the Personal Finance Manager system.  In this stage, 
users can submit feedback regarding their experience with the financial recommendation services. The 
system processes the feedback using VADER sentiment analysis to classify the feedback as positive, 
negative,  or  neutral.  In  the  displayed  example,  the  system  identifies  the  feedback  sentiment  as 
Neutral. This analysis  helps  evaluate  user satisfaction  and  improves  the overall effectiveness  of the 
financial management platform.

5. CONCLUSION

Fig. 7: Predicting Feedback Screen

This research successfully integrates ML and DL techniques to provide personalized financial insights 
and  enhanced  decision-making  support.  K-Means  clustering  is  utilized  to  analyze  user  spending 
behavior  by  grouping  expenses  into  meaningful  categories.  The  LSTM  model  accurately  forecasts 
future expenses based on historical financial data. These combined techniques enable users to make 
informed  decisions  regarding  budgeting  and  investment  planning.  The  system  also  incorporates 
sentiment  analysis  to  evaluate  user  feedback  and  improve  overall  user  interaction.  A  Django-based 
web interface ensures seamless visualization of prediction graphs and clustering results. Performance 
metrics such as MSE and R² score validate the accuracy and reliability of the predictions. Overall, the 
system delivers a comprehensive and efficient solution for personal finance management.

REFERENCES

[1]  Ramezanian,  M.;  Haghdoost,  A.A.;  Mehrolhassani,  M.H.;  Abolhallaje,  M.;  Dehnavieh,  R.; 
Najafi,  B.;  Fazaeli,  A.A.  Forecasting  health  expenditures  in  Iran  using  the  ARIMA  model 
(2016–2020). Med. J. Islam. Repub. Iran 2019, 33, 25.

[2]  Rubio,  L.;  Gutiérrez-Rodríguez,  A.J.;  Forero,  M.G.  EBITDA  index  prediction  using

exponential smoothing and ARIMA model. Mathematics 2021, 9, 2538.

[3]  Zhang, P.; Joshi, M.; Lingras, P. Use of stability and seasonality analysis for optimal inventory

prediction models. J. Intell. Syst. 2011, 20, 147–166

[4]  Amirkhanov,  I.V.;  Puzynina,  T.P.;  Puzynin,  I.V.;  Sarhadov,  I.;  Pavlušová,  E.;  Pavluš,  M. 
Numerical  simulations  of  heat  and  moisture  transfer  subject  to  the  phase  transition.  In 
Mathematical  Modeling  and  Computational  Science,  Proceedings  of  the  International

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  467

---

<!-- PAGE 9 -->

International Journal of

DATA SCIENCE AND IOT MANAGEMENT SYSTEM

Peer Reviewed, Referred & Indexed Journal 
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

Conference, MMCP 2011, Stará Lesná, Slovakia, 4–8 July 2011; Springer: Berlin/Heidelberg, 
Germany; pp. 195–200.

[5]  Sirisha,  U.M.;  Belavagi,  M.C.;  Attigeri,  G.  Profit  prediction  using  ARIMA,  SARIMA  and 
LSTM  models  in  time  series  forecasting:  A  comparison.  IEEE  Access  2022,  10,  124715–
124727.

[6]  Shiyyab, F.S.; Alzoubi, A.B.; Obidat, Q.M.; Alshurafat, H. The Impact of Artificial Intelligence 
115.

Performance. Int.

Stud. 2023, 11,

Financial

Financial

on

J.

Disclosure 
https://doi.org/10.3390/ijfs11030115

[7]  Yaseen,  H.;  Al-Amarneh,  A.  Adoption  of  Artificial  Intelligence-Driven  Fraud  Detection  in 
Banking: The Role of Trust, Transparency, and Fairness Perception in Financial Institutions in 
the  United  Arab  Emirates  and  Qatar. J.  Risk  Financial  Manag. 2025, 18,  217. 
https://doi.org/10.3390/jrfm18040217

[8]  El  Hajj,  M.;  Hammoud,  J.  Unveiling  the  Influence  of  Artificial  Intelligence  and  Machine 
Learning on Financial Markets: A Comprehensive Analysis of AI Applications in Trading, Risk 
Management,  and  Financial  Operations. J.  Risk  Financial  Manag. 2023, 16,  434. 
https://doi.org/10.3390/jrfm16100434

[9]  Aleksandrova, A.; Ninova, V.; Zhelev, Z. A Survey on AI Implementation in Finance, (Cyber) 
Insurance and Financial Controlling. Risks 2023, 11, 91. https://doi.org/10.3390/risks11050091 
[10]  Yang,  Q.;  Lee,  Y.-C.  Enhancing  Financial  Advisory  Services  with  GenAI:  Consumer 
Perceptions and Attitudes Through Service-Dominant Logic and Artificial Intelligence Device 
Use 
470. 
Risk 
https://doi.org/10.3390/jrfm17100470

Financial  Manag. 2024, 17,

Perspectives. J.

Acceptance

[11]  Shaban,  O.S.;  Omoush,  A.  AI-Driven  Financial  Transparency  and  Corporate  Governance: 
Enhancing  Accounting  Practices  with  Evidence  from  Jordan. Sustainability 2025, 17,  3818. 
https://doi.org/10.3390/su17093818

[12]  Artene,  A.E.;  Domil,  A.E.;  Ivascu,  L.  Unlocking  Business  Value:  Integrating  AI-Driven 
3069. 
Reporting

Systems. Electronics 2024, 13,

Financial

in 
Decision-Making 
https://doi.org/10.3390/electronics13153069

[13]  Mhlanga,  D.  Industry  4.0  in  Finance:  The  Impact  of  Artificial  Intelligence  (AI)  on  Digital 
Financial Inclusion. Int. J. Financial Stud. 2020, 8, 45. https://doi.org/10.3390/ijfs8030045 
[14]  Bayakhmetova,  A.;  Rudenko,  L.;  Krylova,  L.;  Suleimenova,  B.;  Niyazbekova,  S.; 
Nurpeisova,  A.  Artificial  Intelligence  in  Financial  Behavior:  Bibliometric  Ideas  and  New 
Opportunities. J. Risk Fi

[15]  Liu,  L.X.;  Sun,  Z.;  Xu,  K.;  Chen,  C.  AI-Driven  Financial  Analysis:  Exploring  ChatGPT’s 
60.

Challenges. Int.

Stud. 2024, 12,

Financial

and

J.

Capabilities 
https://doi.org/10.3390/ijfs12030060

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  468

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

  International Journal of

                  DATA SCIENCE AND IOT MANAGEMENT SYSTEM

        Peer Reviewed, Referred & Indexed Journal
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper
AI-Driven Personal Finance Management: Predictive Expense Forecasting
and Behavioural Clustering

C. Vinitha1*, Arra Hari Krishna2, Eyikyala Manikanta Reddy2, Pullala Javari2

1Assistant Professor, 2UG Student, 1,2Department of Computer Science and Engineering

1,2Kommuri Pratap Reddy Institute of Technology, Ghanpur, Ghatkesar, 501301, Telangana, India.

*Correspondence: C. Vinitha (vnreddy61@gmail.com)

ABSTRACT

Financial  planning  and  expense  management  have  become  increasingly  essential  as  individuals
struggle  to  monitor  daily  spending,  interpret  financial  behavior,  and  plan  future  investments
effectively. With the rapid growth of digital transactions and diverse expenditure categories, manual
financial  tracking  becomes  complex,  time-consuming,  and  prone  to  errors.  Traditional  financial
management systems, such as spreadsheets and basic budgeting tools, allow users to store transaction
data but lack advanced analytical capabilities, making accurate prediction of future expenses difficult
and  leading  to  inefficient  financial  decisions.  To  address  these  limitations,  the  proposed  system
introduces  an  intelligent  financial  prediction  and  analysis  platform  developed  using  the  Django
framework  with  a  MySQL  (Structured  Query  Language-based  relational  database  management
system) database for secure data storage and management. The system incorporates email-based One-
Time  Password  (OTP)  authentication  using  the  Simple  Mail  Transfer  Protocol  (SMTP)  to  ensure
secure and verified user access. A Long Short-Term Memory (LSTM) deep learning model is utilized
to  analyze  historical  financial  data  and  predict  future  expenses  by  capturing  temporal  patterns  and
trends.  Additionally,  K-Means  clustering  is  applied  to  group  expenses  into  different  categories,
enabling users to better understand their spending behavior and identify financial patterns. The system
further  integrates  sentiment  analysis  using  VADER  (Valence  Aware  Dictionary  and  Sentiment
Reasoner)  to  evaluate  user  feedback  and  classify  it  as  positive,  negative,  or  neutral,  supporting
continuous system improvement. By combining predictive modeling, clustering techniques, sentiment
evaluation, and secure authentication mechanisms, the system provides automated financial insights,
personalized  recommendations,  and  enhanced  decision-making  support,  helping  users  manage
finances more efficiently.

Key words:   Financial Prediction, Expense Analysis, Sentiment Analysis, Machine Learning, Deep
Learning, Django Web Framework.

1. INTRODUCTION

Anticipating future outcomes has become an essential capability across multiple economic domains,
particularly for shaping decisions at both local and regional governance levels [1]. Within the business
environment,  especially  in  wholesale  and  retail  trade,  the  projection  of  financial  measures  plays  a
central  role  in  guiding  operational  and  strategic  actions,  including  production  scheduling,  sales
planning,  and  inventory  control.  This  sector  is  uniquely  complex  due  to  fluctuating  consumer
preferences,  pronounced  seasonal  demand  patterns,  and  the  impact  of  external  forces  such  as
economic  conditions  and  political  developments  [2].  Despite  these  challenges,  estimating  key
financial  metrics—such  as  revenue  streams,  expenditure  levels,  and  overall  profitability—is
fundamental  for  designing  effective  corporate  strategies,  sustaining  long-term  growth,  and
maintaining  competitive  positioning.  In  particular,  profit  estimation  supports  efficient  cash  flow

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  460

  International Journal of

                  DATA SCIENCE AND IOT MANAGEMENT SYSTEM

        Peer Reviewed, Referred & Indexed Journal
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

management, liquidity planning, and performance evaluation, making it an indispensable component
of financial decision-making in retail-oriented enterprises.

To predict the future trajectory of financial variables, as shown in Fig. 1,  it is necessary to analyze
their historical progression over time. In certain technical fields, such behavior is often modeled using
mathematical  formulations  like  partial  differential  equations.  However,  when  sufficiently  large
datasets are available in economic contexts, advanced analytical methods—especially those based on
time series modeling—can be employed to capture patterns and forecast future values. The growing
reliance on historical time series information highlights its importance as a predictive foundation in
modern  analytics  [3].  Such  data  enables  organizations  to  anticipate  upcoming  trends  and  make
informed  replaceions  about  revenues,  costs,  and  profit,  which  are  vital  for  effective  planning  and
operational success in retail businesses [4].

Fig. 1: Finance Management

Revenue  forecasting,  in  particular,  serves  as  a  cornerstone  for  cross-functional  decision-making:
finance  teams  can  estimate  profitability  and  funding  needs,  sales  units  can  evaluate  demand  levels,
procurement  departments  can  optimize  purchasing  strategies,  marketing  teams  can  assess  campaign
effectiveness,  and  logistics  divisions  can  align  supply  chain  operations  accordingly.  Moreover,
accurate replaceions of sales and expenses can assist investors in predicting fluctuations in retail stock
performance. Profit, defined as the surplus remaining after deducting direct costs from total revenue,
acts  as  a  key  indicator  of  financial  health  and  enables  comparisons  across  competing  firms  [5].
Therefore,  reliable  profit  forecasting  is  instrumental  in  supporting  strategic  choices  and  ensuring
sustained financial stability.

1.1 Problem Definition

The central challenge in personal financial management is transforming voluminous, raw transaction
data  into  accurate,  actionable,  and  personalized  insights  regarding  future  financial  status.  Users
typically struggle with two key aspects, accurately predicting future expenses given non-linear trends,
seasonal variations, and irregular large payments traditional methods often fail to capture the complex
temporal  dependencies  inherent  in  spending  habits.  Understanding  how  and  why  money  is  spent,
beyond simple category totals. Users need to identify underlying spending patterns, detect anomalies,
and link their qualitative financial feelings to quantitative expense data.

2. LITERATURE SURVEY

Shiyyab et al. [6] proposed an AI disclosure index to quantitatively evaluate the extent of AI adoption
within  financial  institutions  and  to  analyze  its  relationship  with  financial  performance.  The  study

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  461

  International Journal of

                  DATA SCIENCE AND IOT MANAGEMENT SYSTEM

        Peer Reviewed, Referred & Indexed Journal
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

emphasizes  that  transparent  reporting  of  AI  usage  enhances  stakeholder  confidence  and  supports
better  governance  practices.  By  systematically  measuring  disclosure  levels,  the  research  provides
insights  into  how  organizations  communicate  their  AI  integration  strategies  and  highlights  the
importance  of  standardized  disclosure  frameworks.  It  further  supports  policymakers  and  regulatory
authorities in formulating guidelines that ensure accountability, transparency, and ethical deployment
of AI systems in the banking sector. Yaseen, et al. [7] investigated the role of transparency, fairness,
and  trust  in  influencing  the  adoption  of  AI  technologies  within  financial  environments.  The  study
demonstrates  that  transparency  acts  as  a  primary  driver  of  trust,  which  directly  impacts  user
acceptance  of  AI  systems.  It  also  shows  that  fairness  perception  plays  a  critical  role  in  mitigating
concerns related to algorithmic bias, thereby improving system credibility. Additionally, the research
identifies  variations  in  adoption  readiness  across  different  professional  groups  and  regions,
highlighting the influence of experience and exposure to AI. The findings emphasize that regulatory
compliance  and  the  development  of  explainable  and  unbiased  AI  models  are  essential  for  fostering
adoption in highly regulated financial  sectors. El Hajj, et al. [8] utilized a mixed-methods approach
combining  quantitative  surveys  and  qualitative  analysis  to  assess  the  adoption  of  AI  and  ML  in
financial  markets.  The  study  identifies  widespread  use  cases  such  as  algorithmic  trading,  fraud
detection,  credit  scoring,  and  customer  service  automation.  It  also  explores  challenges  including
regulatory  compliance,  ethical  concerns,  workforce  transformation,  and  data  privacy  issues.  The
findings emphasize the need for continuous skill development and organizational adaptation to fully
leverage AI technologies in finance.

Aleksandrova, et al. [9] conducted a comprehensive review of AI adoption across finance, insurance,
and financial controlling, focusing on the economic implications and technological advancements in
these  sectors.  The  study  identifies  key  trends  such  as  increased  automation,  enhanced  predictive
analytics, and improved risk assessment capabilities. It also highlights challenges including regulatory
constraints,  implementation  costs,  and  skill  gaps.  By  analyzing  existing  literature,  the  authors
establish  a  strong  relationship  between  AI  integration  and  the  evolution  of  financial  systems,
emphasizing  its  role  in  driving  efficiency  and  innovation.  Yang,  et  al.  [10]  explored  the  behavioral
and  perceptual  factors  influencing  the  adoption  of  GenAI  in  financial  advisory  services.  The  study
developed a research framework based on SDL and AIDUA models to examine how personalization,
human-like  empathy,  and  continuous  learning  capabilities  of  AI  systems  affect  user  trust  and
acceptance.  The  findings  reveal  that  users  are  more  likely  to  adopt  AI-generated  financial  advice
when it demonstrates contextual understanding and adaptive responses. The study also highlights the
importance  of  perceived  authenticity  and  usefulness  in  shaping  user  attitudes  toward  AI-driven
financial decision support systems. Shaban, et al. [11] investigated the relationship between AI-driven
financial  transparency  and  corporate  governance  using  quantitative  techniques  such  as  SEM  and
regression analysis. Based on data collected from corporate professionals, the study demonstrates that
AI  significantly  enhances  governance  effectiveness,  improves  risk  management  practices,  and
increases  stakeholder  engagement.  It  also  highlights  AI’s  role  in  automating  compliance  processes,
while  acknowledging  challenges  such  as  algorithmic  bias,  data  privacy  concerns,  and  the  need  for
updated regulatory frameworks.

Artene,  et  al.  [12]  investigated  the  combined  impact  of  AI,  DT,  and  financial  reporting  systems  on
modern  business  environments,  emphasizing  how  their  integration  enhances  analytical  capabilities
and  strategic  decision-making.  The  study  explains  that  organizations  adopting  AI-driven  financial
reporting  can  automate  complex  accounting  processes,  reduce  human  intervention,  and  improve
accuracy in financial statements. It further highlights the role of neural networks in modeling complex

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  462

  International Journal of

                  DATA SCIENCE AND IOT MANAGEMENT SYSTEM

        Peer Reviewed, Referred & Indexed Journal
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

financial relationships, enabling pattern recognition, anomaly detection, and predictive analytics. The
synergy  between  intelligent  systems  and  DT  initiatives  is  shown  to  create  adaptive,  data-driven
ecosystems  that  improve  transparency,  operational  efficiency,  and  long-term  business  value.
Mhlanga, et al. [13] explored the impact of AI on digital financial inclusion through a conceptual and
documentary  review  of  scholarly  and  institutional  sources.  The  study  demonstrates  that  AI
significantly  enhances  financial  accessibility  by  improving  risk  assessment  models,  reducing
information  asymmetry,  and  enabling  automated  customer  interaction  through  chatbots.  It  further
emphasizes  AI’s  role  in  strengthening  fraud  detection  and  cybersecurity  mechanisms,  thereby
increasing trust and participation in digital financial systems, especially in underserved populations.
Bayakhmetova,  et  al.  [14]  conducted  an  in-depth  bibliometric  analysis  using  Bibliometrix  and
Bibliophagy tools to map the intellectual structure of AI research in finance. Their findings reveal a
strong upward publication trend with a 13.34% annual growth rate, indicating rapid expansion of the
field. The study identifies dominant research clusters, including ML applications, financial inclusion
strategies,  and  intelligent  decision-support  systems.  Additionally,  it  highlights  underexplored  areas
such as ethical AI design, regional inequalities in adoption, and limited deployment in low-resource
environments, while also identifying leading journals and contributors shaping the research landscape.
Liu,  et  al.  [15]  evaluated  the  capabilities  of  ChatGPT-4o  in  financial  reasoning  by  designing
structured,  multi-step  analytical  tasks  that  simulate  real-world  financial  problem-solving.  The  study
benchmarks AI performance against human analysts using task-specific evaluation metrics, revealing
that  while  the  model  performs  effectively  in  structured  reasoning  and  data  interpretation,  it  faces
limitations  in  handling  highly  complex  or  ambiguous  financial  scenarios.  The  research  underscores
the  potential  of  conversational  AI  in  financial  analytics  while  also  identifying  areas  requiring
improvement.

3. PROPOSED SYSTEM

This  research  presents  a  comprehensive,  data-centric  framework  designed  to  enable  personalized
expense  prediction  and  intelligent  investment  guidance  through  advanced  analytics  and  machine
learning techniques, as illustrated in Fig. 2. The system is developed using the Django web framework
and extends beyond conventional financial tracking by integrating predictive modeling and behavioral
analysis to enhance financial awareness and decision-making. At its core, the architecture combines
two major ML approaches: an LSTM model for capturing temporal dependencies in expense data and
generating accurate time-series forecasts, and a K-Means clustering algorithm for identifying hidden
spending patterns and segmenting user behavior.

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  463

  International Journal of

                  DATA SCIENCE AND IOT MANAGEMENT SYSTEM

        Peer Reviewed, Referred & Indexed Journal
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

Fig. 2: Proposed System architecture

The system follows a structured three-layer architecture consisting of a MySQL database for secure
storage  and  user  management,  a  Python-based  backend  responsible  for  preprocessing  and  ML
computations,  and  an  interactive  web  interface  that  facilitates  seamless  user  interaction.  Security  is
ensured  through  a  multi-level  authentication  mechanism  that  incorporates  Base64-based  password
encoding  along  with  OTP-based  2FA  via  SMTP,  thereby  safeguarding  user  accounts  and  sensitive
financial information. Once authenticated, users upload their financial dataset (budget.csv), which is
processed  using  Pandas,  where  date  features  such  as  year,  month,  and  day  are  extracted,  and  both
numerical and categorical data are normalized using MinMaxScaler and StandardScaler to prepare it
for ML models. The system then applies K-Means clustering on expense categories and amounts to
group  similar  spending  behaviors,  enabling  users  to  visualize  and  understand  their  financial  habits
more effectively. Simultaneously, the LSTM model is trained on historical daily expense data to learn
sequential  patterns  and  generate  accurate  future  expense  predictions,  with  performance  evaluated
using  metrics  such  as  score  and  MSE.  These  predicted  values  are  further  utilized  in  the
recommendation  module,  where  a  practical  surplus  is  computed  by  comparing  estimated  expenses
with  a  generated  income  approximation,  allowing  the  system  to  suggest  potential  savings  or
investment opportunities. In addition to quantitative analysis, the framework incorporates a qualitative
feedback  mechanism  where  users  can  submit  feedback  that  is  analyzed  using  VADER  sentiment
analysis, enabling continuous monitoring of user satisfaction and system performance. The analyzed
sentiment  results  are  stored  in  the  database  to  support  ongoing  improvements  and  adaptive  system
behavior.  Overall,  this  integrated  pipeline  combines  forecasting,  clustering,  recommendation,  and
sentiment analysis into a unified system that not only predicts future financial trends but also delivers
personalized, actionable insights, thereby empowering users to make informed and effective financial
decisions.

3.1 LSTM

The  LSTM  is  a  specialized  type  of  Recurrent  Neural  Network  designed  to  overcome  the  vanishing
gradient  problem,  enabling  it  to  learn  long-term  dependencies  essential  for  time-series  forecasting
(like expense trends).  Its core strength lies in the memory cell and three gates that regulate the flow
of  information:  the  Forget  Gate  decides  which  information  to  discard  from  the  cell  state;  the  Input
Gate decides which new information to store in the cell state; and the Output Gate determines which

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  464

  International Journal of

                  DATA SCIENCE AND IOT MANAGEMENT SYSTEM

        Peer Reviewed, Referred & Indexed Journal
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

part  of  the  current  cell  state  is  outputted  as  the  hidden  state  for  the  current  timestamp.  This  gating
mechanism  allows  the  LSTM  to  remember  patterns  that  occurred  months  ago  (like  annual  fees  or
seasonal spending) and integrate them effectively into the current day's expense prediction as depicted
in Fig. 3.

Fig. 3: Internal Workflow of LSTM.

Data Sequence Preparation: Raw time features (year, month, day) and total expenses are scaled.
Input features are reshaped into sequences (3D format: [samples, timesteps, features]) required by the
LSTM.

Forward Pass (Per Timestep): For each input sequence, the data passes through the gates
sequentially:

●  Forget Gate: Multiplies the old cell state by a value between 0 and 1 (output of a sigmoid

function) to decide what to discard.

●  Input Gate: Determines new information to add to the cell state (using sigmoid for filtering

and tanh for creating candidate values).

●  Cell State Update: The old cell state is updated by forgetting old info and adding new info.

●  Output Gate: Determines the final output (hidden state) based on the new cell state.

Prediction: After processing the sequence, the output from the final LSTM layer feeds into a dense
layer to produce the single-day expense forecast.

Backpropagation: The prediction error is calculated using the Mean Squared Error (MSE) loss
function, and weights are adjusted using the Adam optimizer.

Iteration: Steps 2-4 are repeated over multiple epochs (1000 in the code) to minimize the loss and
optimize model performance.

4. RESULTS DESCRIPTION

Fig. 4 illustrates the application of the K-Means clustering algorithm for analyzing expense behavior
patterns.  The  clustering  model  groups  transaction  records  into  clusters  based  on  similarities  in

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  465

  International Journal of

                  DATA SCIENCE AND IOT MANAGEMENT SYSTEM

        Peer Reviewed, Referred & Indexed Journal
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

spending  categories  and  expense  amounts.  Each  cluster  represents  a  distinct  pattern  of  financial
activity  that  helps  identify  how  expenses  are  distributed  across  different  categories.  The  graphical
representation provides insights into spending trends and financial behavior. This clustering analysis
assists users in understanding their expense distribution and supports better financial planning.

Fig. 4: K-means clustering for personal finance

Fig. 5 depicts the evaluation results of the Long Short-Term Memory (LSTM) deep learning model
used for expense prediction. The model performance is measured using evaluation metrics including
Accuracy  of  0.9993  (99.93%)  and  Mean  Squared  Error  of  35.41.  A  graphical  comparison  between
predicted  expenses  and  actual  test  expenses  is  also  displayed  to  illustrate  the  effectiveness  of  the
prediction model. The graph demonstrates how closely the predicted values follow the actual financial
expense  patterns.  This  evaluation  confirms  the  ability  of  the  LSTM  model  to  accurately  forecast
future financial expenses.

Fig. 5: LSTM Model Evaluation Screen

Fig.  6  illustrates  the  budget  recommendation  module  of  the  system  where  financial  predictions  are
used  to  generate  investment  suggestions.  Based  on  the  predicted  expenses  calculated  by  the  LSTM
model,  the  system  estimates  the  user’s  expected  financial  expenditure.  For  example,  if  the  system
assumes  an  income  of  45,648  units  and  predicted  expenses  of  36,987  units,  the  recommended
investment  amount  is  calculated  as  8,661  units.  This  module  helps  users  allocate  their  income
efficiently and make better financial planning decisions.

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  466

  International Journal of

                  DATA SCIENCE AND IOT MANAGEMENT SYSTEM

        Peer Reviewed, Referred & Indexed Journal
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

Fig. 6: Recommend budget Screen

Fig. 7 depicts the feedback analysis module of the Personal Finance Manager system.  In this stage,
users can submit feedback regarding their experience with the financial recommendation services. The
system processes the feedback using VADER sentiment analysis to classify the feedback as positive,
negative,  or  neutral.  In  the  displayed  example,  the  system  identifies  the  feedback  sentiment  as
Neutral. This analysis  helps  evaluate  user satisfaction  and  improves  the overall effectiveness  of the
financial management platform.

5. CONCLUSION

Fig. 7: Predicting Feedback Screen

This research successfully integrates ML and DL techniques to provide personalized financial insights
and  enhanced  decision-making  support.  K-Means  clustering  is  utilized  to  analyze  user  spending
behavior  by  grouping  expenses  into  meaningful  categories.  The  LSTM  model  accurately  forecasts
future expenses based on historical financial data. These combined techniques enable users to make
informed  decisions  regarding  budgeting  and  investment  planning.  The  system  also  incorporates
sentiment  analysis  to  evaluate  user  feedback  and  improve  overall  user  interaction.  A  Django-based
web interface ensures seamless visualization of prediction graphs and clustering results. Performance
metrics such as MSE and R² score validate the accuracy and reliability of the predictions. Overall, the
system delivers a comprehensive and efficient solution for personal finance management.

REFERENCES

[1]  Ramezanian,  M.;  Haghdoost,  A.A.;  Mehrolhassani,  M.H.;  Abolhallaje,  M.;  Dehnavieh,  R.;
Najafi,  B.;  Fazaeli,  A.A.  Forecasting  health  expenditures  in  Iran  using  the  ARIMA  model
(2016–2020). Med. J. Islam. Repub. Iran 2019, 33, 25.

[2]  Rubio,  L.;  Gutiérrez-Rodríguez,  A.J.;  Forero,  M.G.  EBITDA  index  prediction  using

exponential smoothing and ARIMA model. Mathematics 2021, 9, 2538.

[3]  Zhang, P.; Joshi, M.; Lingras, P. Use of stability and seasonality analysis for optimal inventory

prediction models. J. Intell. Syst. 2011, 20, 147–166

[4]  Amirkhanov,  I.V.;  Puzynina,  T.P.;  Puzynin,  I.V.;  Sarhadov,  I.;  Pavlušová,  E.;  Pavluš,  M.
Numerical  simulations  of  heat  and  moisture  transfer  subject  to  the  phase  transition.  In
Mathematical  Modeling  and  Computational  Science,  Proceedings  of  the  International

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  467

  International Journal of

                  DATA SCIENCE AND IOT MANAGEMENT SYSTEM

        Peer Reviewed, Referred & Indexed Journal
                                            ISSN: 3068-272X                                          www.ijdim.com                                      Original Research Paper

Conference, MMCP 2011, Stará Lesná, Slovakia, 4–8 July 2011; Springer: Berlin/Heidelberg,
Germany; pp. 195–200.

[5]  Sirisha,  U.M.;  Belavagi,  M.C.;  Attigeri,  G.  Profit  prediction  using  ARIMA,  SARIMA  and
LSTM  models  in  time  series  forecasting:  A  comparison.  IEEE  Access  2022,  10,  124715–
124727.

[6]  Shiyyab, F.S.; Alzoubi, A.B.; Obidat, Q.M.; Alshurafat, H. The Impact of Artificial Intelligence
115.

Performance. Int.

Stud. 2023, 11,

Financial

Financial

on

J.

Disclosure
https://doi.org/10.3390/ijfs11030115

[7]  Yaseen,  H.;  Al-Amarneh,  A.  Adoption  of  Artificial  Intelligence-Driven  Fraud  Detection  in
Banking: The Role of Trust, Transparency, and Fairness Perception in Financial Institutions in
the  United  Arab  Emirates  and  Qatar. J.  Risk  Financial  Manag. 2025, 18,  217.
https://doi.org/10.3390/jrfm18040217

[8]  El  Hajj,  M.;  Hammoud,  J.  Unveiling  the  Influence  of  Artificial  Intelligence  and  Machine
Learning on Financial Markets: A Comprehensive Analysis of AI Applications in Trading, Risk
Management,  and  Financial  Operations. J.  Risk  Financial  Manag. 2023, 16,  434.
https://doi.org/10.3390/jrfm16100434

[9]  Aleksandrova, A.; Ninova, V.; Zhelev, Z. A Survey on AI Implementation in Finance, (Cyber)
Insurance and Financial Controlling. Risks 2023, 11, 91. https://doi.org/10.3390/risks11050091
[10]  Yang,  Q.;  Lee,  Y.-C.  Enhancing  Financial  Advisory  Services  with  GenAI:  Consumer
Perceptions and Attitudes Through Service-Dominant Logic and Artificial Intelligence Device
Use
470.
Risk
https://doi.org/10.3390/jrfm17100470

Financial  Manag. 2024, 17,

Perspectives. J.

Acceptance

[11]  Shaban,  O.S.;  Omoush,  A.  AI-Driven  Financial  Transparency  and  Corporate  Governance:
Enhancing  Accounting  Practices  with  Evidence  from  Jordan. Sustainability 2025, 17,  3818.
https://doi.org/10.3390/su17093818

[12]  Artene,  A.E.;  Domil,  A.E.;  Ivascu,  L.  Unlocking  Business  Value:  Integrating  AI-Driven
3069.
Reporting

Systems. Electronics 2024, 13,

in
Decision-Making
https://doi.org/10.3390/electronics13153069

Financial

[13]  Mhlanga,  D.  Industry  4.0  in  Finance:  The  Impact  of  Artificial  Intelligence  (AI)  on  Digital
Financial Inclusion. Int. J. Financial Stud. 2020, 8, 45. https://doi.org/10.3390/ijfs8030045
[14]  Bayakhmetova,  A.;  Rudenko,  L.;  Krylova,  L.;  Suleimenova,  B.;  Niyazbekova,  S.;
Nurpeisova,  A.  Artificial  Intelligence  in  Financial  Behavior:  Bibliometric  Ideas  and  New
Opportunities. J. Risk Fi

[15]  Liu,  L.X.;  Sun,  Z.;  Xu,  K.;  Chen,  C.  AI-Driven  Financial  Analysis:  Exploring  ChatGPT’s
60.

Challenges. Int.

Stud. 2024, 12,

Financial

and

J.

Capabilities
https://doi.org/10.3390/ijfs12030060

International Journal of Data Science and IoT Management System

IJDIM, 2026, 5 (2(1)), 460-468  |  468

